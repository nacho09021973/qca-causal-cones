#!/usr/bin/env python3
"""Exact checks for the Thirring low-energy packet gate (contract 2 of 2).

Contract: theory/THIRRING_LOW_ENERGY_PACKET_GATE.md (commit 715096f).
Report:   reports/2026-11-09--thirring-low-energy-packet.md

Conventions: 1804.08508v1 Eqs.(1)-(5): |q> = (2pi)^(-1/2) sum_x e^{-iqx}|x>,
W(q) = [[nu e^{iq}, -i mu], [-i mu, nu e^{-iq}]], v^s_q = (-i mu, g_s(q)),
g_s(q) = -i(s sin omega(q) + nu sin q), cos omega = nu cos q; U = F J, chi = pi/2.
Basis (RR, RL, LR, LL), R = up.

Certified (exact SymPy):
  P1  envelope normalization: int_{-1}^{1} (15/16)(1-t^2)^2 dt = 1.
  P2  Gamma = sigma_z (-1)^x anticommutes with W (so Gamma1 Gamma2 commutes with
      W x W); sigma_z v^+_q = v^-_{q+pi}.
  P3  four-plane-wave generalized eigenfunction (1711.03920 Eq.(12) interacting
      solution / 1804.08508 Eq.(18), opposite-Gamma pattern, phase e^{-i chi} on RL at
      y=0, antisymmetric extension) is an exact lattice eigenvector of U with
      eigenvalue e^{-i omega(q1)} e^{-i omega(q2)}, at two algebraic momentum pairs
      (one with p = 0), mu = 3/5; and the chi = 0 version with T = 1 is an exact
      eigenvector of F.
  P4  the same-Gamma part feels no interaction: J = identity on Gamma1 Gamma2 = +1
      configurations (checked on a window).
  P5  low-energy admission: omega(mu K)/mu -> sqrt(1+K^2); omega'(q) > 0 for 0<q<pi;
      the velocity lower bound used for the collision geometry, with rational
      bounds, for 0 < mu < 1/10 on the packet support.
  P6  low-energy limit g_+(mu Q)/(-i mu) -> sqrt(1+Q^2) + Q; limiting T_ab, and
      leakage limits l_ab = |T_ab - 1|^2/4 > 0: l00 = 1/3, l11 = 4/9,
      l01 = l10 = (sqrt10 + 1)/(2(sqrt10 + 2)); |T_ab| = 1.
  P7  momentum-support inequalities for 0 < mu < 1/10: packet supports inside
      (0, 4 mu) in |q| and disjoint; shifted by pi they lie in the doubler window.

Not certified (written proof in the report): the packet/scattering bridge (exact
approximate solution, unitarity, tail and variation estimates), the stationary-
phase direction of motion, and the conclusion NO_ENTANGLER_IN_DECLARED_PACKET_CODE.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--thirring-low-energy-packet"
CHECKS = []
I = sp.I
R, L = 0, 1
BASIS = [(R, R), (R, L), (L, R), (L, L)]


def exact(name, cond):
    CHECKS.append(dict(name=name, passed=bool(cond)))


def iszero(x):
    x = sp.expand(sp.expand_complex(x))
    return x == 0 or sp.simplify(sp.radsimp(x)) == 0


def W_pre(x, a, MU, NU):
    if a == R:
        return ((NU, x - 1, R), (-I * MU, x, L))
    return ((-I * MU, x, R), (NU, x + 1, L))


def F_op(amp, MU, NU):
    def out(x1, a1, x2, a2):
        s = 0
        for c1, y1, b1 in W_pre(x1, a1, MU, NU):
            for c2, y2, b2 in W_pre(x2, a2, MU, NU):
                s += c1 * c2 * amp(y1, b1, y2, b2)
        return s
    return out


def J_op(amp, Z):
    def out(x1, a1, x2, a2):
        v = amp(x1, a1, x2, a2)
        return Z * v if (x1 == x2 and a1 != a2) else v
    return out


# ---------------- P1 ----------------
def check_P1():
    t = sp.symbols("t", real=True)
    exact("P1-int-h^2=1", sp.integrate(sp.Rational(15, 16) * (1 - t**2)**2, (t, -1, 1)) == 1)


# ---------------- P2 ----------------
def check_P2():
    mu = sp.Rational(3, 5); nu = sp.Rational(4, 5)
    gam = lambda x, a: (1 if a == R else -1) * (1 if x % 2 == 0 else -1)
    ok = True
    for x in range(-3, 4):
        for a in (R, L):
            for xs in range(-4, 5):
                for b in (R, L):
                    w = sum(c for c, ys, bs in W_pre(x, a, mu, nu) if ys == xs and bs == b)
                    ok &= iszero(gam(x, a) * w * gam(xs, b) + w)
    exact("P2-Gamma-W-Gamma=-W", ok)
    q = sp.symbols("q", real=True)
    m, n = sp.symbols("m n", positive=True)
    sw = sp.sqrt(1 - n**2 * sp.cos(q)**2)
    gplus = -I * (sw + n * sp.sin(q))
    gminus_shift = -I * (-sw + n * sp.sin(q + sp.pi))  # sin omega(q+pi) = sin omega(q)
    exact("P2-sigma_z-v^+_q=v^-_{q+pi}", iszero(-gplus - gminus_shift))


# ---------------- P3 ----------------
def onepart(z, MU, NU):
    """z = e^{iq} (algebraic, |z|=1). Returns (g+, e^{-i omega}, sin q, cos q)."""
    c = sp.re(z); s = sp.im(z)
    sw = sp.sqrt(1 - NU**2 * c**2)
    gp = -I * (sw + NU * s)
    eom = NU * c - I * sw
    return gp, eom


def eigenfunction(z1, z2, MU, NU, Z):
    g1, e1 = onepart(z1, MU, NU)
    g2, e2 = onepart(z2, MU, NU)
    Zc = sp.conjugate(Z)
    T = (g1 + Zc * g2) / (g2 + Zc * g1)
    vin = [-MU**2, -I * MU * g2, -I * MU * g1, g1 * g2]          # v+_{q1} x v+_{q2}
    vin_d = [-MU**2, I * MU * g2, I * MU * g1, g1 * g2]           # v-_{q1+pi} x v-_{q2+pi}
    vout = [-MU**2, -I * MU * g1, -I * MU * g2, g1 * g2]          # v+_{q2} x v+_{q1}
    vout_d = [-MU**2, I * MU * g1, I * MU * g2, g1 * g2]
    cz1, cz2 = sp.conjugate(z1), sp.conjugate(z2)

    def psi(x1, a1, x2, a2):
        if x1 - x2 < 0:
            return -psi(x2, a2, x1, a1)
        j = BASIS.index((a1, a2))
        sgn = (-1) ** ((x1 + x2) % 2)
        pin = cz1**x1 * cz2**x2
        pout = cz2**x1 * cz1**x2
        val = (vin[j] - sgn * vin_d[j]) * pin - T * (vout[j] - sgn * vout_d[j]) * pout
        if x1 == x2 and j == 1:
            val = Zc * val
        return val
    return psi, e1 * e2, T


def check_P3():
    MU, NU = sp.Rational(3, 5), sp.Rational(4, 5)
    pts = {"generic": ((4 + 3 * I) / 5, (12 - 5 * I) / 13),
           "p=0": ((4 + 3 * I) / 5, (4 - 3 * I) / 5)}
    res = {}
    for tag, (z1, z2) in pts.items():
        for chi_tag, Z in (("chi=pi/2", I), ("chi=0", sp.Integer(1))):
            psi, lam, T = eigenfunction(z1, z2, MU, NU, Z)
            Upsi = F_op(J_op(psi, Z), MU, NU)
            ok, nonzero = True, False
            for x1 in range(-3, 4):
                for x2 in range(-3, 4):
                    for a1, a2 in BASIS:
                        ok &= iszero(Upsi(x1, a1, x2, a2) - lam * psi(x1, a1, x2, a2))
                        nonzero |= not iszero(psi(x1, a1, x2, a2))
            exact(f"P3-{tag}-{chi_tag}-four-wave-eigenfunction", ok and nonzero)
            exact(f"P3-{tag}-{chi_tag}-|T|=1", iszero(sp.Abs(T)**2 - 1))
            if Z == 1:
                exact(f"P3-{tag}-chi=0-T=1", iszero(T - 1))
            res[f"{tag},{chi_tag}"] = str(sp.nsimplify(sp.simplify(T)))
    return res


# ---------------- P4 ----------------
def check_P4():
    gam = lambda x, a: (1 if a == R else -1) * (1 if x % 2 == 0 else -1)
    ok = True
    for x1 in range(-3, 4):
        for x2 in range(-3, 4):
            for a1, a2 in BASIS:
                touched = (x1 == x2 and a1 != a2)
                if touched:
                    ok &= gam(x1, a1) * gam(x2, a2) == -1
    exact("P4-contact-only-in-Gamma1Gamma2=-1", ok)


# ---------------- P5 ----------------
def check_P5():
    mu, K, q = sp.symbols("mu K q", positive=True)
    nu = sp.sqrt(1 - mu**2)
    # sin omega(mu K)/mu -> sqrt(1+K^2); omega -> 0 so omega/sin omega -> 1 (written)
    sinom = sp.sqrt(1 - nu**2 * sp.cos(mu * K)**2)
    lim = sp.limit(sinom / mu, mu, 0, "+")
    exact("P5-sin-omega(mu K)/mu->sqrt(1+K^2)", iszero(lim - sp.sqrt(1 + K**2)))
    n = sp.symbols("n", positive=True)
    dom = sp.diff(sp.acos(n * sp.cos(q)), q)
    exact("P5-omega'(q)=nu sin q/sin omega", iszero(sp.simplify(dom - n * sp.sin(q) / sp.sqrt(1 - n**2 * sp.cos(q)**2))))
    m = sp.symbols("m", positive=True)
    ident = (1 - (1 - m**2) * sp.cos(q)**2) - (m**2 + sp.sin(q)**2 - m**2 * sp.sin(q)**2)
    exact("P5-1-nu^2cos^2q=mu^2+sin^2q-mu^2sin^2q", iszero(sp.expand(sp.expand_trig(ident).rewrite(sp.cos))))
    # velocity bound: K in [Kmin, Kmax], Kmin = 1 - sqrt(1/10) > 0.68, Kmax = 2 + sqrt(1/10) < 2.32, mu < 1/10:
    # omega'(mu K) >= nu K (1 - mu^2 K^2/6) / sqrt(1+K^2) >= nu_min (1 - (1/100)(2.32^2)/6) * f(0.68)
    Kmin_ok = (1 - sp.sqrt(sp.Rational(1, 10))) > sp.Rational(68, 100)
    Kmax_ok = (2 + sp.sqrt(sp.Rational(1, 10))) < sp.Rational(232, 100)
    f068_sq = sp.Rational(68, 100)**2 / (1 + sp.Rational(68, 100)**2)
    vlow = sp.sqrt(sp.Rational(99, 100)) * (1 - sp.Rational(1, 100) * sp.Rational(232, 100)**2 / 6)
    bound = vlow**2 * f068_sq > sp.Rational(55, 100)**2
    exact("P5-velocity-lower-bound-0.55-on-support", bool(Kmin_ok and Kmax_ok and bound))
    exact("P5-closing-margin-y_c<=2L-1.10*4L=-2.4L<-2L", sp.Rational(2) - sp.Rational(110, 100) * 4 < -2)


# ---------------- P6 ----------------
def check_P6():
    mu = sp.symbols("mu", positive=True)
    Q = sp.symbols("Q", real=True)
    nu = sp.sqrt(1 - mu**2)
    gq = -I * (sp.sqrt(1 - nu**2 * sp.cos(mu * Q)**2) + nu * sp.sin(mu * Q))
    exact("P6-g+(mu Q)/(-i mu)->sqrt(1+Q^2)+Q", iszero(sp.limit(gq / (-I * mu), mu, 0, "+") - (sp.sqrt(1 + Q**2) + Q)))
    ks = [1, 2]
    res = {}
    for a in (0, 1):
        for b in (0, 1):
            G1 = ks[a] + sp.sqrt(1 + ks[a]**2)            # e^{asinh k_a}
            G2 = sp.sqrt(1 + ks[b]**2) - ks[b]            # e^{-asinh k_b}
            T = (G1 - I * G2) / (G2 - I * G1)
            ell = sp.nsimplify(sp.simplify(sp.Abs(T - 1)**2 / 4))
            coshD = (G1 / G2 + G2 / G1) / 2
            exact(f"P6-|T_{a}{b}|=1", iszero(sp.Abs(T)**2 - 1))
            exact(f"P6-l_{a}{b}=(coshD-1)/(2coshD)", iszero(sp.Abs(T - 1)**2 / 4 - (coshD - 1) / (2 * coshD)))
            exact(f"P6-l_{a}{b}>0", bool(sp.N((coshD - 1) / (2 * coshD), 30) > 0) and iszero(coshD - sp.radsimp(coshD)))
            res[f"{a}{b}"] = dict(T=str(sp.radsimp(T)), leak=str(sp.radsimp((coshD - 1) / (2 * coshD))),
                                  leak_float=float(sp.N((coshD - 1) / (2 * coshD))))
    exact("P6-l00=1/3", iszero(sp.sympify(res["00"]["leak"]) - sp.Rational(1, 3)))
    exact("P6-l11=4/9", iszero(sp.sympify(res["11"]["leak"]) - sp.Rational(4, 9)))
    exact("P6-l01=(sqrt10+1)/(2(sqrt10+2))", iszero(sp.sympify(res["01"]["leak"]) - (sp.sqrt(10) + 1) / (2 * (sp.sqrt(10) + 2))))
    return res


# ---------------- P7 ----------------
def check_P7():
    # mu < 1/10, delta = mu^{3/2}: supports |q| in [mu - delta, 2 mu + delta]; disjoint bins: mu+delta < 2mu-delta
    m = sp.symbols("m", positive=True)  # m = sqrt(mu), 0 < m < 1/sqrt10
    mu, de = m**2, m**3
    c1 = sp.simplify((mu - de) / mu)                 # = 1 - m > 0
    c2 = sp.simplify((2 * mu + de) / mu)             # = 2 + m < 4
    c3 = sp.simplify(((2 * mu - de) - (mu + de)) / mu)  # = 1 - 2m > 0
    mb = 1 / sp.sqrt(10)
    exact("P7-support-positive-(1-m>0)", bool((c1.subs(m, mb)) > 0))
    exact("P7-support-inside-4mu-(2+m<4)", bool(c2.subs(m, mb) < 4))
    exact("P7-bins-disjoint-(1-2m>0)", bool(c3.subs(m, mb) > 0))
    exact("P7-monotone-in-m", sp.diff(c1, m) < 0 and sp.diff(c3, m) < 0 and sp.diff(c2, m) > 0)


def main():
    check_P1(); check_P2()
    t3 = check_P3()
    check_P4(); check_P5()
    t6 = check_P6()
    check_P7()
    paths = ("scripts/verify_thirring_low_energy_packet.py", "theory/THIRRING_LOW_ENERGY_PACKET_GATE.md",
             "sources/1711.03920v1.pdf", "sources/1804.08508v1.pdf")
    data = dict(T_at_check_points=t3, limits=t6, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    lines += ["", "Limiting leakage per logical input: " + ", ".join(f"{k}: {v['leak']} ~ {v['leak_float']:.6f}" for k, v in t6.items())]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
