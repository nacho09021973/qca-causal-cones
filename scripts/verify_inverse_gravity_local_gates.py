#!/usr/bin/env python3
"""IG1b exact local gate tests; no many-body spectrum or IR claim.

Contract: theory/INVERSE_GRAVITY_LOCAL_GATE_GATE.md.
Primary stencils: Gu-Wen arXiv:0907.1203v3, PDF pp.15-16, Eqs.48-49.
"""

from itertools import product

import sympy as sp

from verify_inverse_gravity_constraint_module import (
    COMPONENTS, overlap_by_translation, real_scalar_stencils,
    real_vector_stencils, unit_shift,
)


def real_r(axis):
    out = [{} for _ in COMPONENTS]
    other = [i for i in range(3) if i != axis]
    for diagonal in other:
        shift_axis = next(i for i in other if i != diagonal)
        out[diagonal] = {
            (0, 0, 0): 2,
            unit_shift(shift_axis, -2): 1,
            unit_shift(shift_axis, 2): 1,
        }
    face = next(j for j, ab in enumerate(COMPONENTS) if set(ab) == set(other))
    for sa, sb in product((-1, 1), repeat=2):
        shift = [0, 0, 0]
        shift[other[0]], shift[other[1]] = sa, sb
        out[face][tuple(shift)] = -1
    return out


def real_w(axis):
    # Cyclic permutations of +Lxy(z endpoints) -Lzx(y endpoints).
    b, c = (axis + 1) % 3, (axis + 2) % 3
    out = [{} for _ in COMPONENTS]
    positive = next(j for j, ab in enumerate(COMPONENTS) if set(ab) == {axis, b})
    negative = next(j for j, ab in enumerate(COMPONENTS) if set(ab) == {axis, c})
    out[positive] = {unit_shift(c, s): 1 for s in (-1, 1)}
    out[negative] = {unit_shift(b, s): -1 for s in (-1, 1)}
    return out


def polynomial(stencils, variables):
    return sp.Matrix([
        sp.expand(sum(coef * sp.prod(p**e for p, e in zip(variables, shift))
                      for shift, coef in stencil.items()))
        for stencil in stencils
    ])


def zero_overlaps(first, second):
    overlaps = overlap_by_translation(first, second)
    return all(value == 0 for value in overlaps.values())


def main():
    variables = sp.symbols("x y z", nonzero=True)
    tx, ty, tz = [p + 1 / p for p in variables]
    c = sp.Matrix([ty**2 + tz**2, tx**2 + tz**2, tx**2 + ty**2,
                   -tx * ty, -ty * tz, -tz * tx])
    vs = [sp.Matrix(v) for v in (
        [tx, 0, 0, ty, 0, tz], [0, ty, 0, tx, tz, 0], [0, 0, tz, 0, ty, tx])]
    rs = [sp.Matrix(r) for r in (
        [0, tz**2, ty**2, 0, -ty * tz, 0],
        [tz**2, 0, tx**2, 0, 0, -tz * tx],
        [ty**2, tx**2, 0, -tx * ty, 0, 0])]
    ws = [sp.Matrix(w) for w in (
        [0, 0, 0, tz, 0, -ty], [0, 0, 0, -tz, tx, 0], [0, 0, 0, 0, -tx, ty])]

    for a in range(3):
        assert (polynomial(real_r(a), variables) - rs[a]).applyfunc(sp.expand) == sp.zeros(6, 1)
        assert (polynomial(real_w(a), variables) - ws[a]).applyfunc(sp.expand) == sp.zeros(6, 1)
        for b in range(3):
            assert sp.expand(rs[a].dot(vs[b])) == 0
            assert zero_overlaps(real_r(a), real_vector_stencils(b))
        assert sp.expand(c.dot(ws[a])) == 0
        assert zero_overlaps(real_scalar_stencils(), real_w(a))
        print(f"PASS axis={a}: R/V and T/S, Laurent and real space, all translations")

    assert (sum(rs, sp.zeros(6, 1)) - c).applyfunc(sp.expand) == sp.zeros(6, 1)
    assert sum(ws, sp.zeros(6, 1)) == sp.zeros(6, 1)
    print("PASS redundancies: Rxx Ryy Rzz=S; Tx Ty Tz=I")

    overlap = overlap_by_translation(real_r(2), real_w(0))[(1, 1, 1)]
    assert overlap == -1 and overlap % 3 != 0
    print("PASS fixed physical Weyl witness: Rzz(0), Tx at (1,1,1), overlap=-1 mod 3")

    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    R = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Z = sp.diag(1, omega, sp.simplify(omega**2))
    T = Z.H
    assert sp.simplify(T * R - sp.conjugate(omega) * R * T) == sp.zeros(3)
    projector = (sp.eye(3) + R + R**2) / 3
    assert projector**2 == projector and projector.H == projector
    phase = sp.sqrt(3) / 2 + sp.I / 2  # exp(i*pi/6)
    G = phase * (sp.eye(3) + (-sp.I - 1) * projector)
    assert sp.simplify(G.H * G - sp.eye(3)) == sp.zeros(3)
    assert sp.simplify(G * T - T * G) != sp.zeros(3)
    print("PASS exact local qutrit gate: unitary, noncommuting with physical T")
    print("VERDICT: LOCAL_CONSTRAINT_PRESERVING_NONSCALAR_GATE_PASS_AUTHOR_SIDE")
    print("Scope: local gate algebra only; tick locality/state argued separately; no modes or IR.")


if __name__ == "__main__":
    main()
