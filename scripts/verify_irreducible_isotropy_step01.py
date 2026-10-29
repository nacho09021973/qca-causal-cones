#!/usr/bin/env python3
"""Steps 0-1 of theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md (exact, fail-closed).

Run from the repository root:
    python3 -B scripts/verify_irreducible_isotropy_step01.py

What it certifies (SymPy, exact rational/algebraic arithmetic, zero tolerance):
  0.2  Binary groups 2T (24) and 2O (48), their maps to the rotation groups T and O,
       orbit structure on N_3, and complete character tables (irreducible dimensions).
  0.3  Control A: the two published Pavia d=3 Weyl symbols are D2-covariant (Pauli
       image) and are not covariant under the 3-fold or 4-fold cube rotations.
  0.4  Control B: the s=4 family A_a (theta=pi/4) has no nonzero intertwiner for the
       3-fold rotation, for generic a (all a follows from the O4 result below).
  1    Class derivation: for T3, O3, O4 (and the s=2 controls T2s, O2s) the
       unitarity identities of a full-support N_3 symbol with irreducible covariance
       generate the unit ideal (Groebner basis [1]): no such symbol exists.
  Controls: the equation generator vanishes on the s=4 family and on the Pavia
       symbols; without the normalization every system is homogeneous (so the unit ideal
       comes from the normalization alone); the D2/Q8 spin-1/2 class on N_3 (where the
       Pavia symbols are covariant) gives a non-unit ideal.
       For O, the vertex-stabilizer commutant has the independently expected
       complex dimensions 2 (spin 1/2) and 6 (spin 3/2).

What it does NOT certify: the linear 2O irrep E, reducible representations, other groups,
supports other than N_3, symbols with an on-site term, or Steps 2-3 of the charter.
"""

import itertools
import sys
import time

import sympy as sp
from sympy.combinatorics import Permutation

sys.path.insert(0, "scripts")
import cert_Aa_s4_counterexample as C4  # reviewed helper, read-only
import verify_weyl_dirac_gate as WD  # reviewed helper, read-only
from certificate_utils import assert_sym_equal, sym_zero

I = sp.I
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)
N3 = [tuple(v) for v in itertools.product((1, -1), repeat=3)]
H0 = sp.Matrix([1, 1, 1])
CHECKS = 0


def require(cond, label):
    global CHECKS
    if not cond:
        print(f"[FAIL] {label}")
        sys.exit(1)
    CHECKS += 1
    print(f"[PASS] {label}", flush=True)


def simp(e):
    return sp.simplify(sp.expand_complex(e))


def key(m):
    return tuple(sp.nsimplify(simp(x)) for x in m)


def is_zero(m):
    return sym_zero(m)


# ---------------------------------------------------------------- groups
G1 = sp.diag(sp.exp(-I * sp.pi / 4), sp.exp(I * sp.pi / 4)).applyfunc(simp)  # pi/2 about z
G2 = (sp.eye(2) - I * (SX + SY + SZ)) / 2  # 2pi/3 about (1,1,1)
C2 = -I * SZ  # pi about z
GENERATORS = {"2O": [G1, G2], "2T": [G2, C2], "Q8": [-I * SX, -I * SY]}


def generate(gens):
    elems, seen, front = [sp.eye(2)], {key(sp.eye(2))}, [sp.eye(2)]
    while front:
        new = []
        for x in front:
            for g in gens:
                y = (x * g).applyfunc(simp)
                k = key(y)
                if k not in seen:
                    seen.add(k)
                    elems.append(y)
                    new.append(y)
        front = new
    return elems


def rotation(u):
    return sp.Matrix(3, 3, lambda i, j: simp((u * PAULI[j] * u.H * PAULI[i]).trace() / 2))


def spin(u, n):
    """Spin-n/2 representation by symmetric powers, orthonormal monomial basis."""
    x, y = sp.symbols("x y")
    norm = [sp.sqrt(sp.binomial(n, k)) for k in range(n + 1)]
    X = u[0, 0] * x + u[1, 0] * y
    Y = u[0, 1] * x + u[1, 1] * y
    m = sp.zeros(n + 1)
    for k in range(n + 1):
        p = sp.Poly(sp.expand(X ** (n - k) * Y ** k), x, y)
        for r in range(n + 1):
            m[r, k] = p.coeff_monomial(x ** (n - r) * y ** r) * norm[k] / norm[r]
    return m.applyfunc(simp)


def orbits(rots):
    seen, sizes = set(), []
    for v in N3:
        if v in seen:
            continue
        orb = {tuple(r * sp.Matrix(v)) for r in rots}
        seen |= orb
        sizes.append(len(orb))
    return sorted(sizes)


def conj_classes(elems):
    keys = [key(g) for g in elems]
    idx = {k: i for i, k in enumerate(keys)}
    left = set(range(len(elems)))
    classes = []
    while left:
        i = min(left)
        cl = {idx[key((h * elems[i] * h.H).applyfunc(simp))] for h in elems}
        classes.append(sorted(cl))
        left -= cl
    return classes


def diagonal_sign(rot):
    """Sign of the permutation of the four body diagonals (A2 of O)."""
    diags = [sp.Matrix(d) for d in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
    perm = []
    for d in diags:
        img = rot * d
        perm.append(next(j for j, e in enumerate(diags) if img == e or img == -e))
    return Permutation(perm).signature()


def z3_label(rot, rot_gen3):
    """Index k with rot in g3^k V4 for T = A4 acting on S_+ (T -> Z3)."""
    v4 = [sp.eye(3), sp.diag(1, -1, -1), sp.diag(-1, 1, -1), sp.diag(-1, -1, 1)]
    for k in range(3):
        if any(sym_zero(rot - rot_gen3 ** k * v) for v in v4):
            return k
    raise AssertionError("not in T")


def character_table_checks(name, elems, rots, chars, order, n_classes):
    classes = conj_classes(elems)
    require(len(classes) == n_classes, f"{name}: {n_classes} conjugacy classes")
    gram = [[simp(sum(c1[i] * sp.conjugate(c2[i]) for i in range(len(elems))) / order)
             for c2 in chars.values()] for c1 in chars.values()]
    require(all(sym_zero(gram[i][j] - (1 if i == j else 0)) for i in range(len(chars))
                for j in range(len(chars))),
            f"{name}: the {len(chars)} listed characters are orthonormal (each irreducible)")
    dims = [simp(c[0]) for c in chars.values()]
    require(sum(d ** 2 for d in dims) == order and len(chars) == n_classes,
            f"{name}: complete; irreducible dimensions {sorted(dims)}")


# ------------------------------------------------------- class equations
def unitarity_equations(T, s, normalize=True):
    diffs = {}
    for h in N3:
        for hp in N3:
            diffs.setdefault(tuple(a - b for a, b in zip(hp, h)), []).append((h, hp))
    eqs = set()
    for ell, pairs in diffs.items():
        S = sp.zeros(s)
        for h, hp in pairs:
            S += T[h].H * T[hp]
        if normalize and ell == (0, 0, 0):
            S -= sp.eye(s)
        for x in S:
            x = sp.expand(sp.expand_complex(x))
            for part in (sp.expand(sp.re(x)), sp.expand(sp.im(x))):
                if not sym_zero(part):
                    eqs.add(part)
    return list(eqs)


def covariant_class(group, n, bases, commutant=True):
    """Symbols on N_3 with T_{gh} = D(u) T_h D(u)^dagger, one free coefficient per orbit."""
    elems = generate(GENERATORS[group])
    s = n + 1
    D = {key(u): spin(u, n) for u in elems}
    R = {key(u): rotation(u) for u in elems}
    params, T = [], {}
    for bi, base in enumerate(bases):
        xs = sp.symbols(f"x{bi}_0:{s * s}")
        X = sp.Matrix(s, s, xs)
        eqs = []
        if commutant:
            for u in elems:
                if sym_zero(R[key(u)] * base - base):
                    eqs += list(D[key(u)] * X - X * D[key(u)])
        sol = list(sp.linsolve(eqs, xs))[0] if eqs else xs
        free = sorted(sp.Matrix(sol).free_symbols, key=str)
        re = sp.symbols(f"q{bi}_0:{2 * len(free)}", real=True)
        params += list(re)
        A = sp.Matrix(s, s, list(sol)).subs({f: re[2 * i] + I * re[2 * i + 1]
                                             for i, f in enumerate(free)})
        for v in N3:
            reps = [u for u in elems if sym_zero(R[key(u)] * base - sp.Matrix(v))]
            if reps:
                cands = [sp.expand(D[key(u)] * A * D[key(u)].H) for u in reps]
                for c in cands:
                    assert_sym_equal(c, cands[0], "ill-defined orbit map")
                T[v] = cands[0]
    return T, params, s


def groebner_is_unit(eqs, params):
    basis = sp.groebner(eqs, *params, order="grevlex").exprs
    return len(basis) == 1 and sym_zero(basis[0] - 1)


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    # 0.2 groups and character tables
    g2O, g2T = generate(GENERATORS["2O"]), generate(GENERATORS["2T"])
    require(len(g2O) == 48 and len(g2T) == 24, "|2O| = 48, |2T| = 24")
    for name, elems, order in (("2O", g2O, 24), ("2T", g2T, 12)):
        rots = {key(u): rotation(u) for u in elems}
        ok = all(sym_zero(rots[key(u)] * rots[key(v)] - rots[key((u * v).applyfunc(simp))])
                 for u in elems for v in elems)
        require(ok and len({tuple(r) for r in rots.values()}) == order
                and all(sym_zero(r.det() - 1) for r in rots.values()),
                f"{name} -> rotation map is a homomorphism onto a group of order {order}")
    rotO = [rotation(u) for u in g2O]
    rotT = [rotation(u) for u in g2T]
    rotD2 = [sp.eye(3), sp.diag(1, -1, -1), sp.diag(-1, 1, -1), sp.diag(-1, -1, 1)]
    require(orbits(rotO) == [8], "O is transitive on N_3")
    require(orbits(rotT) == [4, 4] and orbits(rotD2) == [4, 4],
            "T and D2 each have two orbits of size 4 on N_3")
    require(all(is_zero(spin(u, 3) * spin(v, 3) - spin((u * v).applyfunc(simp), 3))
                for u in g2O[:12] for v in g2O),
            "spin-3/2 map is multiplicative on 2O (12 x 48 products)")

    chi = {j: [simp(spin(u, j).trace()) for u in g2O] for j in (0, 1, 2, 3, 4)}
    a2 = [diagonal_sign(rotation(u)) for u in g2O]
    t2 = [chi[2][i] * a2[i] for i in range(48)]
    chars_O = {"A1": chi[0], "A2": a2, "E": [chi[4][i] - t2[i] for i in range(48)],
               "T1": chi[2], "T2": t2, "E1/2": chi[1],
               "E5/2": [chi[1][i] * a2[i] for i in range(48)], "G3/2": chi[3]}
    character_table_checks("2O", g2O, rotO, chars_O, 48, 8)

    w = sp.exp(2 * sp.pi * I / 3)
    r3 = rotation(G2)
    lab = [z3_label(rotation(u), r3) for u in g2T]
    chiT = {j: [simp(spin(u, j).trace()) for u in g2T] for j in (0, 1, 2)}
    chars_T = {"A": chiT[0], "A'": [w ** k for k in lab], "A''": [w ** (2 * k) for k in lab],
               "T": chiT[2], "E": chiT[1], "E'": [chiT[1][i] * w ** lab[i] for i in range(24)],
               "E''": [chiT[1][i] * w ** (2 * lab[i]) for i in range(24)]}
    character_table_checks("2T", g2T, rotT, chars_T, 24, 7)
    print("NOTE  Spin-1 and spin-3/2 cover the declared T3/O3/O4 classes up to "
          "characters. The spin-1/2 O control does not cover the linear 2O irrep E.")

    # The threefold stabilizer has distinct eigenvalue multiplicities (1, 1)
    # for spin 1/2 and (1, 1, 2) for spin 3/2. Its commutant dimensions
    # are therefore 1²+1²=2 and 1²+1²+2²=6, respectively.
    for n, expected in ((1, 2), (3, 6)):
        _, params, _ = covariant_class("2O", n, [H0])
        require(len(params) == 2 * expected,
                f"O vertex stabilizer: spin {sp.Rational(n, 2)} commutant "
                f"has expected complex dimension {expected}")

    # controls on the equation generator
    a = sp.Rational(3, 5)
    _, _, _, _, _, coeffs = C4.coefficients(a, sp.pi / 4)
    T4 = {tuple(-x for x in k): v for k, v in coeffs.items()}
    require(all(sym_zero(e) for e in unitarity_equations(T4, 4)),
            "unitarity equations vanish on the s=4 family (a=3/5, theta=pi/4)")
    z = sp.symbols("z1:4")
    pavia = {}
    for ch in (1, -1):
        M, _ = WD.published_symbol(3, ch, z)
        T2 = {}
        for v in N3:
            mono = sp.prod([zi ** (vi + 1) for zi, vi in zip(z, v)])
            T2[tuple(-x for x in v)] = M.applyfunc(
                lambda e: sp.Poly(sp.expand(e * sp.prod(z)), *z).coeff_monomial(mono))
        pavia[ch] = T2
        require(all(sym_zero(e) for e in unitarity_equations(T2, 2))
                and all(not is_zero(t) for t in T2.values()),
                f"unitarity equations vanish on Pavia chirality {ch}; full N_3 support")

    # 0.3 Control A
    def intertwiners(T, rot, s):
        X = sp.Matrix(s, s, sp.symbols(f"v0:{s * s}"))
        eqs = []
        for h, Th in T.items():
            eqs += [sp.expand(e) for e in (X * Th - T[tuple(rot * sp.Matrix(h))] * X)]
        return list(sp.linsolve(eqs, list(X)))[0]

    rz, rx = sp.diag(-1, -1, 1), sp.diag(1, -1, -1)
    rq = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    for ch, T2 in pavia.items():
        require(any(not sym_zero(x) for x in intertwiners(T2, rz, 2))
                and any(not sym_zero(x) for x in intertwiners(T2, rx, 2)),
                f"Control A: Pavia chirality {ch} has nonzero intertwiners for the D2 half-turns")
        require(all(sym_zero(x) for x in intertwiners(T2, r3, 2))
                and all(sym_zero(x) for x in intertwiners(T2, rq, 2)),
                f"Control A: Pavia chirality {ch} is not covariant under the 3-fold or 4-fold "
                "rotation (only the zero intertwiner)")

    # 0.4 Control B (generic a)
    asym = sp.symbols("a", positive=True)
    _, _, _, _, _, coeffs = C4.coefficients(asym, sp.pi / 4)
    T4a = {tuple(-x for x in k): v for k, v in coeffs.items()}
    require(all(sym_zero(x) for x in intertwiners(T4a, r3, 4)),
            "Control B: s=4 family has only the zero intertwiner for the 3-fold rotation "
            "(generic a)")

    # Step 1 classes
    cases = [("T3", "2T", 2, [H0, -H0]), ("O3", "2O", 2, [H0]), ("O4", "2O", 3, [H0]),
             ("T2s (control)", "2T", 1, [H0, -H0]), ("O2s (control)", "2O", 1, [H0])]
    for name, group, n, bases in cases:
        T, params, s = covariant_class(group, n, bases)
        eqs = unitarity_equations(T, s)
        require(groebner_is_unit(eqs, params),
                f"{name}: s={s}, irreducible spin-{sp.Rational(n, 2)} covariance under "
                f"{group[1:]}, {len(params)} real parameters: unitarity ideal is (1) "
                "-> EMPTY_CLASS")
        relaxed = unitarity_equations(T, s, normalize=False)
        require(all(sym_zero(sp.Poly(e, *params).coeff_monomial(1)) for e in relaxed),
                f"{name}: without the normalization the equations are homogeneous, so the "
                "unit ideal comes from sum T^dagger T = I alone")
        print(f"      ({time.time() - t0:.0f} s elapsed)", flush=True)

    T, params, s = covariant_class("Q8", 1, [H0, -H0], commutant=False)
    require(not groebner_is_unit(unitarity_equations(T, s), params),
            "positive control: D2 (Q8) spin-1/2 class on N_3 is non-empty")

    print(f"{CHECKS}/{CHECKS} exact checks passed in {time.time() - t0:.0f} s. "
          "Steps 2-3 and reducible representations are not covered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
