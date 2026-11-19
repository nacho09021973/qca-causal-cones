#!/usr/bin/env python3
"""Exact certificate for theory/ONSITE_SCALAR_FLAT_BAND_GATE.md (frozen b2ffcdc).

Claim: on the support S = N3 ∪ {0} in d=3 (N3 = (±1,±1,±1)/sqrt3), a unitary
symbol U(k) = λ I + sum_h e^{-ik.h} T_h with scalar on-site term has
T_{-h} = -T_h^dagger, hence U + U^dagger = 2λ I, hence every eigenvalue is a
root of z^2 - 2λ z + 1, independent of k (flat bands, no cone with c_0 > 0).

Checks (contract Sec. 3):
 1. support combinatorics (integer coordinates; the 1/sqrt3 scale is common);
 2. mutation control: an extra displacement creates a third pair, detected;
 3. V + V^dagger = 0 after imposing T_{-h} = -T_h^dagger (plus a wrong-sign
    negative control), generic complex
    entries, s = 2 and s = 3, real k;
 4. noncommutative identity U^2 - 2λU + I - U(U + U^dagger - 2λI) = I - U U^dagger,
    and roots of z^2 - 2λ z + 1 have modulus 1 and contain no k.

Does NOT certify: Schur's lemma or the irreducibility of the T3/O3/O4
representations (cited from the predecessor gate); existence of any symbol
in the class; anything about non-scalar on-site terms or other supports.
Fails closed: any failed check or exception exits nonzero.
"""
import itertools
import sys

import sympy as sp

RESULTS = []


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}: {name}")


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def pairs_for(support, ell):
    return {(h1, h2) for h1 in support for h2 in support if sub(h2, h1) == ell}


def main():
    zero = (0, 0, 0)
    n3 = [tuple(s) for s in itertools.product((1, -1), repeat=3)]
    support = n3 + [zero]

    # 1. support combinatorics
    diffs_n3 = {sub(b, a) for a in n3 for b in n3}
    check("|N3 - N3| = 27 and coordinates in {0,±2}",
          len(diffs_n3) == 27 and all(c in (0, 2, -2) for d in diffs_n3 for c in d))
    check("N3 ∩ (N3 - N3) = ∅", not (set(n3) & diffs_n3))
    check("for each ell in N3 the pairs are exactly {(0,ell),(-ell,0)}",
          all(pairs_for(support, ell) == {(zero, ell), (neg(ell), zero)} for ell in n3))
    check("for ell in (N3 - N3) minus 0, no pair involves the origin",
          all(zero not in p for ell in diffs_n3 - {zero} for p in pairs_for(support, ell)))
    check("ell = 0 pairs are the nine diagonal pairs (h,h), h in S",
          pairs_for(support, zero) == {(h, h) for h in support})
    all_diffs = {sub(b, a) for a in support for b in support}
    check("difference set of S is (N3 - N3) ∪ N3, 35 vectors",
          all_diffs == diffs_n3 | set(n3) and len(all_diffs) == 35)

    # 2. mutation control
    mutated = support + [(2, 0, 0)]
    ell = (1, 1, 1)
    check("mutation (2,0,0) adds the pair ((1,-1,-1),(2,0,0)) for ell=(1,1,1)",
          pairs_for(mutated, ell) == {(zero, ell), (neg(ell), zero), ((1, -1, -1), (2, 0, 0))})

    # 3. V + V^dagger = 0 with T_{-h} = -T_h^dagger
    kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
    k = (kx, ky, kz)
    plus =[h for h in n3 if (h[0], h[1], h[2]) > neg(h)]
    if len(plus) != 4 or {neg(h) for h in plus} | set(plus) != set(n3):
        raise RuntimeError("bad split of N3 into ± pairs")

    def phase(h):
        return sp.exp(-sp.I * sum(ki * hi for ki, hi in zip(k, h)) / sp.sqrt(3))

    for s in (2, 3):
        mats = []
        for j in range(4):
            ent = [[sp.Symbol(f"a{j}_{p}{q}_r", real=True) + sp.I * sp.Symbol(f"a{j}_{p}{q}_i", real=True)
                    for q in range(s)] for p in range(s)]
            mats.append(sp.Matrix(ent))
        V = sp.zeros(s, s)
        for h, A in zip(plus, mats):
            V += phase(h) * A + phase(neg(h)) * (-A.H)
        M = (V + V.H).applyfunc(lambda e: sp.simplify(sp.expand(e)))
        check(f"V + V^dagger = 0 for generic T_h, s = {s}", M == sp.zeros(s, s))
        if s == 2:
            W = sp.zeros(s, s)
            for h, A in zip(plus, mats):
                W += phase(h) * A + phase(neg(h)) * A.H
            Mw = (W + W.H).applyfunc(lambda e: sp.simplify(sp.expand(e)))
            check("negative control: with T_{-h} = +T_h^dagger, V + V^dagger != 0",
                  Mw != sp.zeros(s, s))

    # 4. polynomial identity and roots
    U, Ud = sp.symbols("U Ud", commutative=False)
    lam = sp.Symbol("lambda", positive=True)
    lhs = U * U - 2 * lam * U + 1 - U * (U + Ud - 2 * lam)
    check("U^2 - 2λU + I - U(U + U^† - 2λ) = I - U U^† (noncommutative)",
          sp.expand(lhs - (1 - U * Ud)) == 0)
    z = sp.Symbol("z")
    mu = sp.sqrt(1 - lam**2)
    expected = [lam + sp.I * mu, lam - sp.I * mu]
    poly = z**2 - 2 * lam * z + 1
    check("λ ± i sqrt(1-λ^2) are the two roots of z^2 - 2λz + 1",
          all(sp.expand(poly.subs(z, r)) == 0 for r in expected)
          and sp.expand((z - expected[0]) * (z - expected[1]) - poly) == 0)
    # for 0<λ<1, mu is real, so |λ ± i mu|^2 = λ^2 + mu^2
    check("λ^2 + (1-λ^2) = 1, so both roots have modulus 1 for 0<λ<1",
          sp.expand(lam**2 + mu**2 - 1) == 0)
    check("roots contain no k symbol", all(not (r.free_symbols & set(k)) for r in expected))

    failed = [n for n, ok in RESULTS if not ok]
    print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} checks passed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # fail closed
        print(f"FAIL: exception {exc!r}")
        sys.exit(2)
