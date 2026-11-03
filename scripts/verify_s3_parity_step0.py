"""Step 0 (determinant parity lemma, anticipation B5) of theory/S3_ISOTROPIC_RIGIDITY_GATE.md.

Claim: for s = 3, support N_3 = {+-1}^3 (epsilon labels), no on-site term, and any G among the five
geometric classes of the minimal s=2 charter's stage (a) (V4, T, C4 face; D4, O), there is no
unitary covariant symbol, for any projective unitary R.

Proof skeleton (written in reports/2026-10-29--s3-parity-step0.md):
 (1) every monomial of det U has all three exponents odd (sum of three vectors of {+-1}^3);
 (2) a unimodular Laurent polynomial on the torus is a monomial (extremal-exponent argument);
 (3) det(R U R^dag) = det U, so det U(gk) = det U(k) and the exponent m satisfies g^T m = m for
     every g in G; the common fixed space of G meets the odd coset trivially.

Checks:
 1. generic symbolic expansion of det U at s = 3: every exponent odd; the constant term absent;
 2. the extremal-exponent step: for the 64 odd exponents of (1), the lex-max and lex-min
    exponents of f give a unique pair in f * conj(f);
 3. per group, the common fixed space of {g^T} (exact nullspace) and its intersection with the
    odd coset; element-wise control: a 3-fold rotation alone fixes (1,1,1);
 4. negative control: at s = 2 and s = 4 the constant frequency occurs (exact integer instance);
 5. positive control: the certified s=2 witness (Pavia chirality -1) and both published Pavia
    symbols have constant determinant.

What it does NOT certify: the written proof of (2) beyond the extremal-pair check, and anything
beyond Step 0.
"""

import itertools
import sys
import time

import sympy as sp

sys.path.insert(0, "scripts")
import verify_minimal_s2_step00 as S0  # stage (a) groups, read-only
import verify_weyl_dirac_gate as WD  # published Pavia symbols, read-only

CHECKS = 0
I = sp.I
X = sp.symbols("x1:4")
N3 = S0.N3


def require(cond, label):
    global CHECKS
    if not cond:
        print(f"[FAIL] {label}")
        raise SystemExit(1)
    CHECKS += 1
    print(f"[PASS] {label}", flush=True)


def laurent_exponents(expr):
    """Exponents of a Laurent polynomial in X (multiply by a large monomial first)."""
    shift = 8
    P = sp.Poly(sp.expand(expr * sp.prod([x ** shift for x in X])), *X)
    return {tuple(e - shift for e in mono): c for mono, c in P.terms()}


def symbol(s, coeff):
    return sum((coeff(h) * sp.prod([X[j] ** h[j] for j in range(3)]) for h in N3), sp.zeros(s))


def groups():
    subs = {S0.closure([a, b]) for a in S0.O for b in S0.O}
    pairs_pm = [(v, tuple(-x for x in v)) for v in N3 if v[0] == 1]
    choices = [frozenset(c) for c in itertools.product(*pairs_pm)]
    named = {}
    for G in subs:
        for S in choices:
            if (all(S0.act(g, v) in S for g in G for v in S) and len(S0.orbits(G, S)) == 1):
                key = {(4, "tetrahedron"): "V4", (12, "tetrahedron"): "T",
                       (4, "face"): "C4_face"}.get((len(G), S0.kind(S)))
                if key and key not in named:
                    named[key] = G
        if len(S0.orbits(G, N3)) == 1:
            key = {8: "D4", 24: "O"}.get(len(G))
            if key and key not in named:
                named[key] = G
    return named


def main():
    t0 = time.time()
    # 1. generic expansion at s = 3
    cs = {}
    def gen(h):
        M = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"t_{''.join('p' if x > 0 else 'm' for x in h)}_{i}{j}"))
        cs[h] = M
        return M
    U = symbol(3, gen)
    t1 = time.time()
    E = laurent_exponents(U.det(method="berkowitz"))
    odd = all(all(e % 2 != 0 for e in m) for m in E)
    require(odd and (0, 0, 0) not in E and set(E) == set(itertools.product((-3, -1, 1, 3), repeat=3)),
            f"s=3 generic det U: its {len(E)} exponents are exactly {{+-1,+-3}}^3 (all odd), "
            f"constant term identically absent ({time.time() - t1:.0f} s)")

    # 2. extremal-exponent step: lex-max a and lex-min b of the exponent set; a - b arises from a
    #    unique pair (a, b) in f * conj(f), whose exponents are {e - e' : e, e' in support}
    supp = sorted(E)
    a, b = supp[-1], supp[0]
    diff = tuple(p - q for p, q in zip(a, b))
    pairs = [(e, f) for e in supp for f in supp if tuple(p - q for p, q in zip(e, f)) == diff]
    require(pairs == [(a, b)] and a != b,
            f"extremal step: exponent a - b = {diff} of f*conj(f) comes only from (lex-max, lex-min) "
            f"= ({a}, {b}); its coefficient c_a conj(c_b) must vanish, so a unimodular f on this "
            "support has a single monomial")

    # 3. common fixed spaces
    named = groups()
    require(sorted(named) == ["C4_face", "D4", "O", "T", "V4"],
            "the five geometric classes of stage (a) are reconstructed")
    for name in ("V4", "T", "D4", "O", "C4_face"):
        G = named[name]
        A = sp.Matrix.vstack(*[sp.Matrix(g).T - sp.eye(3) for g in G])
        basis = A.nullspace()
        if basis:
            # every vector of the fixed space has at least one coordinate identically zero
            zero_coord = [j for j in range(3) if all(v[j] == 0 for v in basis)]
            ok = len(zero_coord) >= 1
            desc = f"fixed space spanned by {[tuple(v) for v in basis]}, coordinates {zero_coord} vanish"
        else:
            ok, desc = True, "fixed space {0}"
        require(ok, f"{name}: common fixed space of g^T meets the odd coset trivially ({desc})")
    g3 = next(g for g in named["T"] if sp.Matrix(g) ** 3 == sp.eye(3) and sp.Matrix(g) != sp.eye(3))
    fixed3 = (sp.Matrix(g3).T - sp.eye(3)).nullspace()
    require(len(fixed3) == 1 and all(x % 2 != 0 for x in (fixed3[0] / fixed3[0][0])),
            f"element-wise control: a 3-fold rotation alone fixes the odd direction "
            f"{tuple(fixed3[0] / fixed3[0][0])}; only the common fixed space decides")

    # 4. negative control: the constant frequency occurs at s = 2 and s = 4 (exact integers)
    import random
    rng = random.Random(20261029)
    for s in (2, 4):
        Us = symbol(s, lambda h: sp.Matrix(s, s, lambda i, j: rng.randint(-3, 3)))
        Es = laurent_exponents(Us.det(method="berkowitz"))
        require(Es.get((0, 0, 0), 0) != 0 and all(all(e % 2 == 0 for e in m) for m in Es),
                f"negative control s={s}: exponents all even, constant coefficient "
                f"{Es.get((0, 0, 0))} != 0 (integer instance)")

    # 5. positive control: s=2 witness and published Pavia symbols have constant det
    W = {h: sp.prod([(sp.eye(2) + h[j] * WD_PAULI[j]) / 2 for j in range(3)]) for h in N3}
    Ew = laurent_exponents(symbol(2, lambda h: W[h]).det())
    require(set(Ew) == {(0, 0, 0)} and sp.simplify(Ew[(0, 0, 0)] - 1) == 0,
            "positive control: the 4b-1 witness (Pavia chirality -1) has det U = 1")
    z = sp.symbols("z1:4")
    for ch in (1, -1):
        Mz, _ = WD.published_symbol(3, ch, z)
        d = sp.factor(sp.simplify(Mz.det()))
        free = d.free_symbols & set(z)
        require(not free and sp.simplify(sp.Abs(d) - 1) == 0,
                f"positive control: published Pavia chirality {ch} has constant det = {d}")
    print(f"VERDICT: {CHECKS}/{CHECKS} exact checks passed in {time.time() - t0:.0f} s. "
          "s=3, families P and F, N_3 without on-site term: every class EMPTY_CLASS for every "
          "projective unitary R (given the written extremal-exponent lemma).")


WD_PAULI = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

if __name__ == "__main__":
    main()
