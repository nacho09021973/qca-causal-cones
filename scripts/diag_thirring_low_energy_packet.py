#!/usr/bin/env python3
"""DIAGNOSTIC ONLY (floating point): direct lattice evolution of the frozen packet code.

Contract: theory/THIRRING_LOW_ENERGY_PACKET_GATE.md (commit 715096f). Frozen choices:
chi = pi/2, delta = mu^{3/2}, L = ceil(mu^{-2}), T = 4L, k_a = 1 + a, A modes at +L
with momentum +mu k_a, B modes at -L with -mu k_b, envelope sqrt(15)/4 (1-t^2),
positive-band normalized v^+_q, output frame F^T B.

One parameter value, mu = 1/11 (frozen here before running). Periodic box of N sites;
reported box-wrap and norm diagnostics. This file decides no verdict (contract:
no finite computation decides an asymptotic claim). It compares the finite-mu
leakage ||E|ab>||^2 and doubler content ||Q_D U^T B|ab>||^2 with the predicted
finite-mu value |T(q1c,q2c) - 1|^2/4 at the packet centres.
"""
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--thirring-low-energy-packet-diagnostic"
MU = 1.0 / 11.0
NU = math.sqrt(1 - MU**2)
DELTA = MU**1.5
LL = math.ceil(MU**-2)
TT = 4 * LL
KS = (1, 2)
X0 = 760                      # box x in [-X0, X0)
N = 2 * X0
NQ = 3001                     # quadrature points per packet


def omega(q):
    return np.arccos(NU * np.cos(q))


def gplus(q):
    return -1j * (np.sin(omega(q)) + NU * np.sin(q))


def vplus(q):
    v = np.stack([-1j * MU * np.ones_like(q), gplus(q)])
    return v / np.linalg.norm(v, axis=0)


def packet(qc, x_center):
    """psi[c, i] on the box, i = x + X0."""
    t = np.linspace(-1, 1, NQ)
    q = qc + DELTA * t
    w = np.full(NQ, 2.0 / (NQ - 1)); w[0] = w[-1] = 1.0 / (NQ - 1)   # trapezoid in t
    amp = DELTA**-0.5 * math.sqrt(15) / 4 * (1 - t**2) * np.exp(1j * q * x_center) * DELTA * w
    v = vplus(q)
    x = np.arange(-X0, X0)
    ph = np.exp(-1j * np.outer(x, q)) / math.sqrt(2 * math.pi)
    return np.stack([ph @ (amp * v[0]), ph @ (amp * v[1])])


def W1(psi):
    """single particle W: (W psi)_R(x) = nu psi_R(x-1) - i mu psi_L(x); (W psi)_L(x) = -i mu psi_R(x) + nu psi_L(x+1)."""
    R, Lc = psi
    return np.stack([NU * np.roll(R, 1) - 1j * MU * Lc, -1j * MU * R + NU * np.roll(Lc, -1)])


def W2(Psi, axis_particle):
    """apply W on particle 1 (axis_particle=0) or 2 (=1) of Psi[c1,c2,i1,i2]."""
    if axis_particle == 0:
        R, Lc = Psi[0], Psi[1]
        return np.stack([NU * np.roll(R, 1, axis=1) - 1j * MU * Lc, -1j * MU * R + NU * np.roll(Lc, -1, axis=1)])
    R, Lc = Psi[:, 0], Psi[:, 1]
    return np.stack([NU * np.roll(R, 1, axis=2) - 1j * MU * Lc, -1j * MU * R + NU * np.roll(Lc, -1, axis=2)], axis=1)


def step_U(Psi):
    idx = np.arange(N)
    Psi[0, 1, idx, idx] *= 1j
    Psi[1, 0, idx, idx] *= 1j
    return W2(W2(Psi, 0), 1)


def wedge(a, b):
    return (np.einsum("ci,dj->cdij", a, b) - np.einsum("ci,dj->cdij", b, a)) / math.sqrt(2)


def doubler_projectors():
    """Pd[q] (2x2) onto the negative band for periodic distance(q, pi) < 4 mu, else 0.
    q_k = 2 pi k / N; transform psihat(q) = sum_x e^{iqx} psi(x)/sqrt(N) (box phase e^{-iqX0}
    is diagonal and irrelevant for a q-diagonal projector)."""
    qgrid = 2 * math.pi * np.fft.fftfreq(N)
    Pd = np.zeros((N, 2, 2), complex)
    dist = np.abs(((qgrid - math.pi) + math.pi) % (2 * math.pi) - math.pi)
    for iq in np.nonzero(dist < 4 * MU)[0]:
        q = qgrid[iq]
        Wq = np.array([[NU * np.exp(1j * q), -1j * MU], [-1j * MU, NU * np.exp(-1j * q)]])
        evals, evecs = np.linalg.eig(Wq)
        om = math.acos(NU * math.cos(q))
        k = int(np.argmin(np.abs(evals - np.exp(1j * om))))     # negative band: e^{+i omega}
        v = evecs[:, k] / np.linalg.norm(evecs[:, k])
        Pd[iq] = np.outer(v, np.conj(v))
    return Pd


def doubler_content(Psi, Pd):
    """||Q_D Psi||^2, Q_D = 1 - (1-D) x (1-D)."""
    hat = np.fft.ifft(np.fft.ifft(Psi, axis=2, norm="ortho"), axis=3, norm="ortho")
    M = np.eye(2)[None, :, :] - Pd                                 # [q, a, c]
    kept = np.einsum("qac,rbd,cdqr->abqr", M, M, hat, optimize=True)
    diff = hat - kept
    return float(np.vdot(diff, diff).real)


def T_center(a, b):
    q1, q2 = MU * KS[a], -MU * KS[b]
    g1, g2 = gplus(np.array(q1)), gplus(np.array(q2))
    return complex((g1 - 1j * g2) / (g2 - 1j * g1))


def main():
    PD = doubler_projectors()
    A = [packet(MU * k, +LL) for k in KS]
    B = [packet(-MU * k, -LL) for k in KS]
    norms = [float(np.vdot(p, p).real) for p in A + B]
    Af, Bf = [], []
    for p in A + B:
        q = p.copy()
        for _ in range(TT):
            q = W1(q)
        (Af if len(Af) < 2 else Bf).append(q)
    rows = {}
    for a in (0, 1):
        for b in (0, 1):
            Psi = wedge(A[a], B[b])
            for _ in range(TT):
                Psi = step_U(Psi)
            K = np.array([[math.sqrt(2) * np.einsum("ci,dj,cdij->", np.conj(Af[a2]), np.conj(Bf[b2]), Psi)
                           for b2 in (0, 1)] for a2 in (0, 1)])
            leak = 1 - float(np.sum(np.abs(K)**2))
            dcont = doubler_content(Psi, PD)
            Tc = T_center(a, b)
            rows[f"{a}{b}"] = dict(leakage=leak, doubler_content=dcont, K=[[str(z) for z in r] for r in K],
                                   predicted_finite_mu=abs(Tc - 1)**2 / 4, T_center=str(Tc))
            print(a, b, rows[f"{a}{b}"]["leakage"], dcont, abs(Tc - 1)**2 / 4, flush=True)
    data = dict(label="DIAGNOSTIC ONLY, floating point, feeds no verdict", mu="1/11", L=LL, T=TT, delta=DELTA,
                box=[-X0, X0], packet_norms=norms, rows=rows)
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    lines = ["DIAGNOSTIC ONLY (floating point); feeds no verdict.",
             f"mu=1/11, L={LL}, T={TT}, delta={DELTA:.6g}, box=[-{X0},{X0}), packet norms={['%.8f' % n for n in norms]}"]
    lines += [f"input {k}: leakage={v['leakage']:.6f} doubler={v['doubler_content']:.6f} predicted |T_c-1|^2/4={v['predicted_finite_mu']:.6f}"
              for k, v in rows.items()]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
