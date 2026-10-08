#!/usr/bin/env python3
"""Exact IG1a constraint algebra; no QCA tick or spectrum is tested.

Contract: theory/INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md.
Primary stencil source: biblioteca/arXiv-0907.1203.pdf pp.13-15.
SymPy Laurent identities and independently entered real-space overlaps.
"""

from collections import defaultdict
from itertools import product

import sympy as sp


Q = 3
COMPONENTS = ((0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0))


def unit_shift(axis, amount):
    out = [0, 0, 0]
    out[axis] = amount
    return tuple(out)


def real_scalar_stencils():
    stencils = []
    for a, b in COMPONENTS:
        terms = defaultdict(int)
        if a == b:
            terms[(0, 0, 0)] = 4
            for other in range(3):
                if other != a:
                    for sign in (-1, 1):
                        terms[unit_shift(other, 2 * sign)] += 1
        else:
            for sa, sb in product((-1, 1), repeat=2):
                shift = [0, 0, 0]
                shift[a], shift[b] = sa, sb
                terms[tuple(shift)] -= 1
        stencils.append(dict(terms))
    return stencils


def real_vector_stencils(direction):
    stencils = []
    for a, b in COMPONENTS:
        terms = {}
        if a == b == direction:
            terms = {unit_shift(direction, s): 1 for s in (-1, 1)}
        elif a != b and direction in (a, b):
            other = b if a == direction else a
            terms = {unit_shift(other, s): 1 for s in (-1, 1)}
        stencils.append(terms)
    return stencils


def overlap_by_translation(scalars, vectors):
    # Relative vector-center translation d: scalar site r = d + vector site s.
    overlaps = defaultdict(int)
    for scalar, vector in zip(scalars, vectors):
        for r, cr in scalar.items():
            for s, vs in vector.items():
                d = tuple(ri - si for ri, si in zip(r, s))
                overlaps[d] += cr * vs
    return dict(overlaps)


def main():
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    X = sp.zeros(Q)
    for n in range(Q):
        X[(n + 1) % Q, n] = 1
    Z = sp.diag(*[sp.simplify(omega**n) for n in range(Q)])
    assert sp.simplify(X**Q - sp.eye(Q)) == sp.zeros(Q)
    assert sp.simplify(Z**Q - sp.eye(Q)) == sp.zeros(Q)
    assert sp.simplify(Z * X - omega * X * Z) == sp.zeros(Q)
    print("PASS clock algebra: q=3, X^3=Z^3=I, ZX=omega XZ")

    x, y, z = sp.symbols("x y z", nonzero=True)
    tx, ty, tz = (p + 1 / p for p in (x, y, z))
    scalar = sp.Matrix([
        ty**2 + tz**2, tx**2 + tz**2, tx**2 + ty**2,
        -tx * ty, -ty * tz, -tz * tx,
    ])
    vectors = (
        sp.Matrix([tx, 0, 0, ty, 0, tz]),
        sp.Matrix([0, ty, 0, tx, tz, 0]),
        sp.Matrix([0, 0, tz, 0, ty, tx]),
    )
    for direction, vector in zip("xyz", vectors):
        assert sp.expand(scalar.dot(vector)) == 0
        print(f"PASS Laurent correlation: scalar/vector {direction}, all translations")

    scalars = real_scalar_stencils()
    for direction in range(3):
        vectors_real = real_vector_stencils(direction)
        overlaps = overlap_by_translation(scalars, vectors_real)
        assert overlaps and all(value == 0 for value in overlaps.values())
        reduced = [{r: value % Q for r, value in s.items()} for s in scalars]
        overlaps_mod = overlap_by_translation(reduced, vectors_real)
        assert all(value % Q == 0 for value in overlaps_mod.values())
        print(f"PASS independent real-space overlaps: axis={direction}, integer and mod 3")

    print("VERDICT: FINITE_CONSTRAINT_ALGEBRA_PASS_AUTHOR_SIDE")
    print("Scope: commuting finite tensor constraints only; no tick, IR, modes, or gravity.")


if __name__ == "__main__":
    main()
