#!/usr/bin/env python3
"""S4 family: isotropy in the sense of D'Ariano-Erba-Perinotti (1708.00826).

Contract: theory/S4_DEP_ISOTROPY_GATE.md, frozen at 9188755.
Family rebuilt from theory/S4_STRICT_CONE_COUNTEREXAMPLE.md Secs. 2-4
(theta = pi/4, a symbolic in (0,1), b = sqrt(1-a^2) as a positive symbol
with a^2 + b^2 = 1 imposed). Standalone: no reviewed verifier is imported
or modified.

Tasks C1-C5 of the contract, all exact:
  C1  A_h != 0 for the eight BCC displacements, for every a in (0,1);
  C2  U_l A_h U_l^dagger = A_{l(h)} for l in the Klein group L;
  C3  L transitive on S_+ and on S_-; no nontrivial l fixes any h;
  C4  [U_l, A_h] != 0 for the 3 x 8 pairs; set of a in (0,1) where any
      commutator vanishes;
  C5  U_l U_m = phase * U_{lm} (projective representation).
Sanity checks (fail closed): Gamma_i Hermitian involutions, P projectors,
W unitary, eight coefficients sum to a unitary symbol at k = 0.

Exit status: 1 on an exception or a failed sanity check. Otherwise 0, with
the contract verdict printed (a C-task failing is an outcome, not a crash).

Run 1 (2026-11-17, fdae12c) stopped with NotImplementedError in sp.solve
after C1-C3 PASS; output retained in
reports/2026-11-17--s4-dep-isotropy-run1.txt. Zero sets are now computed
on M_h (A_h = W M_h, W unitary and commuting with every U_l, both checked)
by an exact rational parametrization of the arc; no expectation changed.
"""
import itertools
import sys

import sympy as sp
from sympy.physics.quantum import TensorProduct as TP

a, b = sp.symbols("a b", positive=True)
tt = sp.symbols("t", positive=True)
REL = a**2 + b**2 - 1
I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I4 = sp.eye(4)

T = {"x": b * sx + a * sz, "y": b * sy + a * sz, "z": -b * sx + a * sz}
SIG = {"x": sx, "y": sy, "z": sz}
G = {i: TP(SIG[i], T[i]) for i in "xyz"}
P = {(i, s): (I4 + s * G[i]) / 2 for i in "xyz" for s in (1, -1)}
W = TP(I2, sp.diag(sp.exp(-sp.I * sp.pi / 4), sp.exp(sp.I * sp.pi / 4)))

H = list(itertools.product((1, -1), repeat=3))
M = {h: P[("x", h[0])] * P[("y", h[1])] * P[("z", h[2])] for h in H}
A = {h: W * M[h] for h in H}
SPLUS = [h for h in H if h[0] * h[1] * h[2] == 1]
SMINUS = [h for h in H if h[0] * h[1] * h[2] == -1]

LMAP = {"id": lambda h: h,
        "x": lambda h: (h[0], -h[1], -h[2]),
        "y": lambda h: (-h[0], h[1], -h[2]),
        "z": lambda h: (-h[0], -h[1], h[2])}
U = {"id": I4, "x": TP(sx, I2), "y": TP(sy, I2), "z": TP(sz, I2)}


def red(e):
    """Reduce modulo b^2 = 1 - a^2 and simplify."""
    e = sp.expand(e)
    e = sp.expand(e.subs(b**2, 1 - a**2))
    e = sp.expand(e.subs(b**3, b * (1 - a**2)).subs(b**4, (1 - a**2) ** 2))
    return sp.simplify(e)


def mzero(M):
    return all(red(x) == 0 for x in M)


def zeros_in_domain(entries):
    """Exact zero set on 0<a<1, b>0 of a list of entries in Q(i)[a,b].

    Rational parametrization a = (1-t^2)/(1+t^2), b = 2t/(1+t^2), t in (0,1)
    (a bijection onto the arc). Real and imaginary parts of each numerator
    are polynomials in t over QQ; their gcd carries the common zeros, located
    exactly by real_roots (Sturm) and mapped back to a.
    Returns "ALL", or a sorted list of exact a-values (possibly empty).
    """
    polys = []
    for x in entries:
        x = sp.together(sp.expand(x).subs({a: (1 - tt**2) / (1 + tt**2),
                                           b: 2 * tt / (1 + tt**2)}))
        num = sp.expand(sp.numer(x))
        for part in (sp.re(num), sp.im(num)):
            part = sp.expand(part)
            if part != 0:
                polys.append(sp.Poly(part, tt, domain="QQ"))
    if not polys:
        return "ALL"
    g = polys[0]
    for q in polys[1:]:
        g = sp.gcd(g, q)
    if g.degree() <= 0:
        return []
    out = []
    for r in sp.Poly(g, tt).real_roots():
        if (r > 0) == True and (r < 1) == True:
            out.append(sp.simplify((1 - r**2) / (1 + r**2)))
    return out


sanity = []
results = {}


def sanity_check(name, ok):
    sanity.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + "[sanity] " + name)


try:
    for i in "xyz":
        sanity_check(f"Gamma_{i} Hermitian", mzero(G[i] - G[i].H))
        sanity_check(f"Gamma_{i}^2 = I", mzero(G[i] * G[i] - I4))
    sanity_check("W unitary", mzero(W * W.H - I4))
    for l in "xyz":
        sanity_check(f"U_{l} W = W U_{l}", mzero(U[l] * W - W * U[l]))
    sanity_check("sum_h A_h = W (k=0 symbol)", mzero(sum((A[h] for h in H), sp.zeros(4)) - W))

    # C1
    c1_zero_sets = {}
    for h in H:
        c1_zero_sets[h] = zeros_in_domain(list(M[h]))  # A_h = W M_h, W unitary
    c1 = all(z == [] for z in c1_zero_sets.values())
    results["C1"] = c1
    print(("PASS " if c1 else "FAIL ") + "C1 A_h != 0 on (0,1) for all eight h;",
          {h: z for h, z in c1_zero_sets.items() if z != []} or "no zeros")

    # C2
    c2 = all(mzero(U[l] * A[h] * U[l].H - A[LMAP[l](h)]) for l in "xyz" for h in H)
    results["C2"] = c2
    print(("PASS " if c2 else "FAIL ") + "C2 U_l A_h U_l^dagger = A_{l(h)} (24 identities)")

    # C3
    orbit_plus = {LMAP[l](SPLUS[0]) for l in LMAP}
    orbit_minus = {LMAP[l](SMINUS[0]) for l in LMAP}
    c3 = (orbit_plus == set(SPLUS) and orbit_minus == set(SMINUS)
          and all(LMAP[l](h) != h for l in "xyz" for h in H))
    results["C3"] = c3
    print(("PASS " if c3 else "FAIL ") + "C3 transitive on S_+ and S_-, no fixed generator")

    # C4
    c4_zero_sets = {}
    for l in "xyz":
        for h in H:
            comm = U[l] * M[h] - M[h] * U[l]  # [U_l, A_h] = W [U_l, M_h]
            c4_zero_sets[(l, h)] = zeros_in_domain(list(comm))
    bad_all = [k for k, z in c4_zero_sets.items() if z == "ALL"]
    undecided = [k for k, z in c4_zero_sets.items() if z == "UNDECIDED"]
    exceptional = sorted({v for z in c4_zero_sets.values() if isinstance(z, list) for v in z},
                         key=lambda v: float(v))
    results["C4_all_a_fail_pairs"] = bad_all
    results["C4_undecided"] = undecided
    results["C4_exceptional_a"] = exceptional
    print("C4 pairs with commutator identically zero:", bad_all or "none")
    print("C4 pairs undecided:", undecided or "none")
    print("C4 values of a in (0,1) where some commutator vanishes:", exceptional or "none")
    for k, z in c4_zero_sets.items():
        if isinstance(z, list) and z:
            print("   ", k, "->", z)

    # C5
    prod_table = {("x", "y"): "z", ("y", "z"): "x", ("z", "x"): "y",
                  ("y", "x"): "z", ("z", "y"): "x", ("x", "z"): "y"}
    c5 = True
    for (l, m), n in prod_table.items():
        M = U[l] * U[m]
        ratio = None
        for i in range(4):
            for j in range(4):
                if U[n][i, j] != 0:
                    ratio = sp.simplify(M[i, j] / U[n][i, j])
                    break
            if ratio is not None:
                break
        c5 = c5 and ratio is not None and sp.Abs(ratio) == 1 and mzero(M - ratio * U[n])
    c5 = c5 and all(mzero(U[l] * U[l] - I4) for l in "xyz")
    results["C5"] = c5
    print(("PASS " if c5 else "FAIL ") + "C5 projective representation of the Klein group")
except Exception as exc:  # fail closed
    print("FAIL exception:", repr(exc))
    sys.exit(1)

if not all(ok for _, ok in sanity):
    print("FAIL sanity; no verdict")
    sys.exit(1)
if undecided:
    print("VERDICT: none (C4 undecided by exact solver)")
    sys.exit(1)

base = results["C1"] and results["C2"] and results["C3"] and results["C5"]
if not (results["C2"] and results["C3"]) or bad_all:
    verdict = "NOT_DEP_ISOTROPIC_IN_DECLARED_L"
elif base and not exceptional:
    verdict = "DEP_ISOTROPIC_IN_DECLARED_L"
elif base and exceptional:
    verdict = "DEP_ISOTROPIC_EXCEPT_FINITE_SET"
else:
    verdict = "NONE_OF_THE_DECLARED (C1 or C5 failed; see output)"
print("VERDICT:", verdict)
sys.exit(0)
