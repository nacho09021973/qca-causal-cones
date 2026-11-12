"""Fixed diagnostic under theory/TETRAHEDRAL_IR_SIGNAL_GATE.md.

Known: tetrahedral U(k), c_IR=1/3 and faster spectral modes.
Question: signed signal for the frozen IR resource/encoder/effect?
Stop on grid/norm failure; samples never replace admissibility or nonzero proof.
Run from root: python3 -B scripts/diagnose_tetrahedral_ir_signal.py
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
from fractions import Fraction
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/2026-11-10--tetrahedral-ir-signal-diagnostic.json'
P = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
I4 = np.eye(4, dtype=complex)
G = [np.kron(p, p) for p in P]
W = np.kron(np.eye(2), (np.eye(2)-1j*sum(P)/np.sqrt(3))/np.sqrt(2))
M = np.kron(P[1], np.eye(2))
eta = np.array([np.sqrt((1+1/np.sqrt(3))/2),
                np.exp(1j*np.pi/4)*np.sqrt((1-1/np.sqrt(3))/2)])
CHI = np.kron([1, 0], eta)
VCELL = 4/(3*np.sqrt(3))
CR = np.sqrt(3465)/(64*np.pi**2)
STEPS = [h for h in itertools.product((-1, 1), repeat=3) if math.prod(h) == -1]


def cubature(order):
    z, w = np.polynomial.legendre.leggauss(order)
    r, wr = (z+1)/2, w/2
    phi = 2*np.pi*np.arange(2*order)/(2*order)
    r, mu, phi = np.meshgrid(r, z, phi, indexing='ij')
    weights = wr[:, None, None]*w[None, :, None]*np.ones((1, 1, 2*order))*np.pi/order
    weights = (weights*r*r*(1-r*r)**2).ravel()
    q = np.stack([r*np.sqrt(1-mu*mu)*np.cos(phi),
                  r*np.sqrt(1-mu*mu)*np.sin(phi), r*mu], axis=-1).reshape(-1, 3)
    return q, weights


def sites(center, radius):
    # Raw integer coordinates, physical positions raw/sqrt(3).
    lo = np.floor(center-np.sqrt(3)*radius).astype(int)
    hi = np.ceil(center+np.sqrt(3)*radius).astype(int)
    result = [v for v in itertools.product(*(range(a,b+1) for a,b in zip(lo,hi)))
              if v[0]%2 == v[1]%2 == v[2]%2
              and np.sum((np.array(v)-center)**2) <= 3*radius*radius+1e-12]
    return np.asarray(result, dtype=int).reshape(-1, 3)


def reference(N, positions, q, weights, evolved):
    if evolved:
        U = np.broadcast_to(W, (len(q), 4, 4)).copy()
        for j in range(3):
            k = q[:, j]/(N*np.sqrt(3))
            factor = np.cos(k)[:, None, None]*I4-1j*np.sin(k)[:, None, None]*G[j]
            U = U@factor
        spin = np.broadcast_to(CHI, (len(q), 4)).copy()
        for _ in range(N):
            spin = np.einsum('qij,qj->qi', U, spin)
    else:
        spin = np.broadcast_to(CHI, (len(q), 4))
    phase = np.exp(1j*(positions/(np.sqrt(3)*N))@q.T)
    return np.sqrt(VCELL)*CR*N**(-1.5)*(phase*weights)@spin


def compact_evolution(N, a, perturbation):
    bound = N+int(np.max(np.abs(a)))
    shape = (2*bound+1,)*3+(4,)
    psi = np.zeros(shape, dtype=complex)
    psi[tuple((a+bound).T)] = perturbation
    initial_norm = np.sum(np.abs(psi)**2)
    if not initial_norm > 0:
        raise ArithmeticError('Zero encoded difference')
    channels = []
    for h in STEPS:
        E = I4.copy()
        for j in range(3):
            E = E@(I4+h[j]*G[j])/2
        col = E[:, np.argmax(np.sum(np.abs(E)**2, axis=0))]
        vector = col/np.linalg.norm(col)
        channels.append((h, vector, W@vector))
    worst = 0.
    for step in range(N):
        # The support after this update is contained in [-bound,bound]^3.
        assert int(np.max(np.abs(a)))+step+1 <= bound
        out = np.zeros_like(psi)
        for h, vector, shifted in channels:
            src = tuple(slice(0, -1) if v == 1 else slice(1, None) for v in h)
            dst = tuple(slice(1, None) if v == 1 else slice(0, -1) for v in h)
            amplitude = np.einsum('...i,i->...', psi[src], vector.conj())
            out[dst] += amplitude[..., None]*shifted
        psi = out
        err = abs(np.sum(np.abs(psi)**2)/initial_norm-1)
        worst = max(worst, float(err))
        if not np.isfinite(err) or err > 1e-10:
            raise ArithmeticError(f'Norm failure at N={N}, step={step+1}: {err}')
    return psi, bound, worst


def sample(N, order):
    q, weights = cubature(order)
    radius = N/32
    a = sites(np.zeros(3), radius)
    center = -np.ones(3)*3*N/4
    b = sites(center, radius)
    phi = reference(N, a, q, weights, False)
    F = np.maximum(1-np.sum(a*a, axis=1)/(3*radius*radius), 0)**2
    angle = np.pi*F/2
    perturbation = ((np.cos(angle)-1)[:, None]*phi
                    +1j*np.sin(angle)[:, None]*(phi@M.T))
    psi, offset, norm_error = compact_evolution(N, a, perturbation)
    difference = psi[tuple((b+offset).T)]
    unencoded = reference(N, b, q, weights, True)
    h = np.maximum(1-np.sum((b-center)**2, axis=1)/(3*radius*radius), 0)**2
    interference = float(2*np.real(np.sum(h[:, None]*unencoded.conj()*difference)))
    quadratic = float(np.sum(h[:, None]*np.abs(difference)**2))
    L = interference+quadratic
    if not all(np.isfinite(x) for x in (interference, quadratic, L)):
        raise ArithmeticError('Nonfinite signal diagnostic')
    active_a = int(np.count_nonzero(F))
    active_b = int(np.count_nonzero(h))
    path_counts = [Fraction(13*N, 16)]+[Fraction(N, 16)]*3
    if active_a == active_b == 1 and any(n.denominator != 1 for n in path_counts):
        if np.any(difference[h > 0] != 0) or L != 0:
            raise ArithmeticError('Signal violates exact unreachable-site rule')
    return dict(N=N, order=order, alice_sites=len(a), bob_sites=len(b),
                active_alice_sites=active_a, active_bob_sites=active_b,
                necessary_center_path_counts=[str(n) for n in path_counts],
                signed_signal=L, delta=abs(L), interference=interference,
                quadratic=quadratic, max_relative_norm_error=norm_error,
                grid_side=2*offset+1, periodic_boundary=False)


def main():
    rows = []
    for N in (8, 16, 24, 32):
        for order in (8, 12):
            row = sample(N, order)
            rows.append(row)
            print(json.dumps(row), flush=True)
    comparisons = []
    for low, high in zip(rows[::2], rows[1::2]):
        difference = abs(low['signed_signal']-high['signed_signal'])
        scale = max(abs(high['signed_signal']), np.finfo(float).tiny)
        comparisons.append(dict(N=high['N'], order_difference=difference,
                                relative_order_difference=difference/scale))
    result = dict(status='DIAGNOSTIC_ONLY_NOT_A_NONZERO_PROOF', rows=rows,
                  comparisons=comparisons, numpy=np.__version__,
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                  working_tree=True, charter_commit='07d7ce6',
                  meaning='Two cubatures are sensitivity checks, not certified error bounds. No fit or asymptotic inference.')
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(OUT)


if __name__ == '__main__':
    main()
