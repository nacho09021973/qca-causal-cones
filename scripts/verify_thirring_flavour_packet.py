#!/usr/bin/env python3
"""Exact checks for the Thirring flavour-packet gate.

Contract: theory/THIRRING_FLAVOUR_PACKET_GATE.md (frozen at d0c59cb).
Report:   reports/2026-11-14--thirring-flavour-packet.md

Conventions and helpers imported read-only from
scripts/verify_thirring_low_energy_packet.py (contract 2): |q> = (2pi)^(-1/2)
sum_x e^{-iqx}|x>, W(q) = [[nu e^{iq}, -i mu], [-i mu, nu e^{-iq}]],
v^s_q = (-i mu, g_s(q)), g_s(q) = -i(s sin omega(q) + nu sin q),
cos omega = nu cos q; U = F J; basis (RR, RL, LR, LL), R = up;
Gamma = sigma_z (-1)^x. That file is not modified.

Certified (exact SymPy):
  F1  g_-(q + pi) = -g_+(q) (symbolic), so T_- of the (+,-) sector at
      (q1, q2 + pi) equals (a1 - z a2)/(z a1 - a2) with g_+ = -i a.
  F2  (+,-) four-plane-wave function (1711.03920 Eq.(12) lower sign
      pattern: v+_{q1} x v-_{q2'} with its Gamma1 Gamma2 partner, swap with
      phase T_-, contact phase on RL at y = 0, antisymmetric extension) is an
      exact lattice eigenvector of U with eigenvalue e^{-i omega(q1)}
      e^{+i omega(q2')}, at two algebraic momentum pairs, mu = 3/5, chi = pi/2
      and chi = 0 (where T_- = 1, eigenvector of F); |T_-| = 1.
  F3  code algebra in the faithful finite model (one-particle orthonormal
      phi_r, Gamma phi_r, phi_l, Gamma phi_l; Gamma the involution swapping
      each pair; G = Gamma wedge Gamma on Lambda^2): columns orthonormal;
      AA, BB have G = +1; AB = P(phi_r^phi_l) - P(phi_r^Gamma phi_l),
      BA = P(phi_r^phi_l) + P(phi_r^Gamma phi_l); the two P-vectors are
      orthogonal with norm^2 1/2.
  F4  given the bridge limits U^T X -> T X' on each P-sector (written proof),
      the logical map is V = 1 (+) [[al, be], [be, al]] (+) 1, unitary, with
      al = (T+ + T-)/2, be = (T+ - T-)/2.
  F5  T+ - T- = 2 a1 a2 (z^2 - 1) / ((a2 + z a1)(z a1 - a2)): be = 0 iff
      z^2 = 1 (a1, a2 > 0).
  F6  limiting values at chi = pi/2, K_r = 1, K_l = -2: a_r = sqrt2 + 1,
      a_l = sqrt5 - 2 (from the certified limit g_+(mu Q)/(-i mu) ->
      sqrt(1+Q^2) + Q of contract 2 P6); |T+| = |T-| = 1;
      |be| = 2 a_r a_l / (a_r^2 + a_l^2) > 0; concurrence of V|AB> equals
      2 |al be| > 0; consistency: |T+ - 1|^2/4 equals the contract-2 limit
      l01 = (sqrt10 + 1)/(2(sqrt10 + 2)).
  F7  momentum supports for 0 < mu < 1/10, delta = mu^(3/2): right packet in
      (0, 4mu), left packet in (-4mu, 0), the two disjoint; pi-shifted copies
      within 4mu of pi, hence disjoint from the unshifted ones.

Not certified (written proof in the report): the packet/scattering bridge
for the (+,+) sector (contract 2, reused) and its adaptation to the (+,-)
sector, the U^2 admission argument, and the verdict.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-14--thirring-flavour-packet"
_spec = importlib.util.spec_from_file_location(
    "c2", ROOT / "scripts/verify_thirring_low_energy_packet.py")
c2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c2)
F_op, J_op, onepart, BASIS, R, L = c2.F_op, c2.J_op, c2.onepart, c2.BASIS, c2.R, c2.L
iszero = c2.iszero
I = sp.I
CHECKS = []


def exact(name, cond):
    CHECKS.append(dict(name=name, passed=bool(cond)))


# ---------------- F1 ----------------
def check_F1():
    q = sp.symbols("q", real=True)
    n = sp.symbols("n", positive=True)
    sw = sp.sqrt(1 - n**2 * sp.cos(q)**2)            # sin omega(q) = sin omega(q+pi)
    gplus = -I * (sw + n * sp.sin(q))
    gminus_shift = -I * (-sw + n * sp.sin(q + sp.pi))
    exact("F1-g_-(q+pi)=-g_+(q)", iszero(gminus_shift + gplus))


# ---------------- F2 ----------------
def onepart_minus(z, MU, NU):
    """Band '-' at e^{iq} = z: (g_-, eigenvalue e^{+i omega})."""
    c = sp.re(z); s = sp.im(z)
    sw = sp.sqrt(1 - NU**2 * c**2)
    gm = -I * (-sw + NU * s)
    eom_plus = NU * c + I * sw
    return gm, eom_plus


def eigenfunction_pm(z1, z2, MU, NU, Z):
    """(+,-) sector: particle 1 band + at z1, particle 2 band - at z2."""
    g1, e1 = onepart(z1, MU, NU)
    g2, e2 = onepart_minus(z2, MU, NU)
    Zc = sp.conjugate(Z)
    T = (g1 + Zc * g2) / (g2 + Zc * g1)
    vin = [-MU**2, -I * MU * g2, -I * MU * g1, g1 * g2]       # v+_{q1} x v-_{q2}
    vin_d = [-MU**2, I * MU * g2, I * MU * g1, g1 * g2]        # Gamma x Gamma partner
    vout = [-MU**2, -I * MU * g1, -I * MU * g2, g1 * g2]       # v-_{q2} x v+_{q1}
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


def check_F2():
    MU, NU = sp.Rational(3, 5), sp.Rational(4, 5)
    pts = {"generic": ((4 + 3 * I) / 5, (-12 + 5 * I) / 13),
           "second": ((4 + 3 * I) / 5, (-4 - 3 * I) / 5)}
    res = {}
    for tag, (z1, z2) in pts.items():
        for chi_tag, Z in (("chi=pi/2", I), ("chi=0", sp.Integer(1))):
            psi, lam, T = eigenfunction_pm(z1, z2, MU, NU, Z)
            Upsi = F_op(J_op(psi, Z), MU, NU)
            ok, nonzero = True, False
            for x1 in range(-3, 4):
                for x2 in range(-3, 4):
                    for a1, a2 in BASIS:
                        ok &= iszero(Upsi(x1, a1, x2, a2) - lam * psi(x1, a1, x2, a2))
                        nonzero |= not iszero(psi(x1, a1, x2, a2))
            exact(f"F2-{tag}-{chi_tag}-(+,-)-four-wave-eigenfunction", ok and nonzero)
            exact(f"F2-{tag}-{chi_tag}-|T_-|=1", iszero(sp.Abs(T)**2 - 1))
            if Z == 1:
                exact(f"F2-{tag}-chi=0-T_-=1", iszero(T - 1))
            res[f"{tag},{chi_tag}"] = str(sp.nsimplify(sp.simplify(T)))
    return res


# ---------------- F3 / F4 ----------------
def wedge(u, v):
    return sp.Matrix(4, 4, lambda i, j: (u[i] * v[j] - u[j] * v[i]) / sp.sqrt(2))


def inner(X, Y):
    return sp.simplify(sp.expand(sum(sp.conjugate(X[i, j]) * Y[i, j] for i in range(4) for j in range(4))))


def n2(x):
    return sp.expand(x * sp.conjugate(x))


def check_F3_F4(Tp, Tm):
    e = [sp.Matrix([1 if k == i else 0 for k in range(4)]) for i in range(4)]
    phr, gphr, phl, gphl = e
    Gam = sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    def G(X):
        return Gam * X * Gam.T

    def P(X):
        return (X - G(X)) / 2

    chi = {("A", "r"): (phr + gphr) / sp.sqrt(2), ("B", "r"): (phr - gphr) / sp.sqrt(2),
           ("A", "l"): (phl + gphl) / sp.sqrt(2), ("B", "l"): (phl - gphl) / sp.sqrt(2)}
    labels = ["AA", "AB", "BA", "BB"]
    col = {lab: wedge(chi[(lab[0], "r")], chi[(lab[1], "l")]) for lab in labels}
    gram = sp.Matrix(4, 4, lambda i, j: inner(col[labels[i]], col[labels[j]]))
    exact("F3-columns-orthonormal", gram == sp.eye(4))
    exact("F3-AA,BB-have-G=+1", G(col["AA"]) == col["AA"] and G(col["BB"]) == col["BB"])
    S = P(wedge(phr, phl))
    X = P(wedge(phr, gphl))
    exact("F3-AB=P(phr^phl)-P(phr^Gphl)", sp.simplify(col["AB"] - (S - X)) == sp.zeros(4))
    exact("F3-BA=P(phr^phl)+P(phr^Gphl)", sp.simplify(col["BA"] - (S + X)) == sp.zeros(4))
    exact("F3-P-vectors-orthogonal", inner(S, X) == 0)
    exact("F3-P-vectors-norm^2=1/2", inner(S, S) == sp.Rational(1, 2) and inner(X, X) == sp.Rational(1, 2))

    # F4: outgoing images (free frame identified with the same finite model):
    # AA, BB free (G=+1); S -> Tp S, X -> Tm X.
    out = {"AA": col["AA"], "BB": col["BB"],
           "AB": Tp * S - Tm * X, "BA": Tp * S + Tm * X}
    V = sp.Matrix(4, 4, lambda i, j: sp.simplify(inner(col[labels[i]], out[labels[j]])))
    al, be = (Tp + Tm) / 2, (Tp - Tm) / 2
    Vexp = sp.Matrix([[1, 0, 0, 0], [0, al, be, 0], [0, be, al, 0], [0, 0, 0, 1]])
    exact("F4-V=1+[[al,be],[be,al]]+1", sp.simplify(V - Vexp) == sp.zeros(4))
    leak = [sp.expand(inner(out[l], out[l]) - sum(n2(V[k, labels.index(l)]) for k in range(4)))
            for l in labels]
    exact("F4-no-leakage-in-model", all(x == 0 for x in leak))
    return V


# ---------------- F5 / F6 ----------------
def check_F5():
    a1, a2 = sp.symbols("a1 a2", positive=True)
    z = sp.symbols("z")
    Tp = (a1 + z * a2) / (a2 + z * a1)
    Tm = (a1 - z * a2) / (z * a1 - a2)
    diff = sp.together(Tp - Tm)
    num, den = sp.fraction(diff)
    exact("F5-numerator=2a1a2(z^2-1)", iszero(sp.expand(num) - sp.expand(2 * a1 * a2 * (z**2 - 1))))
    exact("F5-denominator=(a2+z a1)(z a1-a2)", iszero(sp.expand(den) - sp.expand((a2 + z * a1) * (z * a1 - a2))))


def check_F6():
    ar = sp.sqrt(2) + 1          # K_r = 1:  sqrt(1+1) + 1
    alft = sp.sqrt(5) - 2        # K_l = -2: sqrt(1+4) - 2
    z = -I                       # e^{-i chi}, chi = pi/2
    Tp = (ar + z * alft) / (alft + z * ar)
    Tm = (ar - z * alft) / (z * ar - alft)
    exact("F6-|T+|=1", iszero(sp.Abs(Tp)**2 - 1))
    exact("F6-|T-|=1", iszero(sp.Abs(Tm)**2 - 1))
    be = (Tp - Tm) / 2
    al = (Tp + Tm) / 2
    be_abs_claim = 2 * ar * alft / (ar**2 + alft**2)
    exact("F6-|be|=2 a_r a_l/(a_r^2+a_l^2)", iszero(sp.Abs(be)**2 - be_abs_claim**2))
    exact("F6-|be|>0", bool(sp.N(be_abs_claim, 30) > 0) and iszero(sp.Abs(al)**2 + sp.Abs(be)**2 - 1))
    conc = 2 * sp.Abs(al) * sp.Abs(be)
    exact("F6-concurrence(V|AB>)=2|al be|>0", bool(sp.N(conc, 30) > 0))
    l01 = (sp.sqrt(10) + 1) / (2 * (sp.sqrt(10) + 2))
    exact("F6-consistency-|T+-1|^2/4=contract2-l01", iszero(sp.Abs(Tp - 1)**2 / 4 - l01))
    return dict(a_r=str(ar), a_l=str(alft), T_plus=str(sp.nsimplify(sp.simplify(Tp))),
                T_minus=str(sp.nsimplify(sp.simplify(Tm))),
                abs_beta=str(sp.radsimp(be_abs_claim)), abs_beta_float=float(sp.N(be_abs_claim, 20)),
                abs_beta_sq_float=float(sp.N(be_abs_claim**2, 20)),
                concurrence_float=float(sp.N(conc, 20))), Tp, Tm


# ---------------- F7 ----------------
def check_F7():
    m = sp.symbols("m", positive=True)       # m = sqrt(mu), 0 < m < 1/sqrt10
    mb = 1 / sp.sqrt(10)
    # right: [mu - d, mu + d]/mu = [1 - m, 1 + m]; left: [-2 - m, -2 + m]
    conds = {"right-positive(1-m>0)": 1 - m, "right-inside-4mu(3-m>0)": 3 - m,
             "left-negative(2-m>0)": 2 - m, "left-inside-4mu(2-m>0)": 2 - m}
    for k, f in conds.items():
        exact(f"F7-{k}", bool(f.subs(m, mb) > 0) and sp.diff(f, m) < 0)
    mu_max = sp.Rational(1, 10)
    exact("F7-pi-shift-disjoint(8mu<pi)", bool(8 * mu_max < sp.pi))


def main():
    check_F1()
    t2 = check_F2()
    vals, Tp, Tm = check_F6()
    check_F5()
    check_F3_F4(sp.Symbol("Tp"), sp.Symbol("Tm"))
    check_F7()
    paths = ("scripts/verify_thirring_flavour_packet.py", "scripts/verify_thirring_low_energy_packet.py",
             "theory/THIRRING_FLAVOUR_PACKET_GATE.md", "sources/1711.03920v1.pdf")
    data = dict(T_minus_at_check_points=t2, limits=vals, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    lines += ["", f"|beta| = {vals['abs_beta']} ~ {vals['abs_beta_float']:.6f}; "
              f"|beta|^2 ~ {vals['abs_beta_sq_float']:.6f}; concurrence ~ {vals['concurrence_float']:.6f}"]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
