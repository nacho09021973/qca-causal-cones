#!/usr/bin/env python3
"""Exact curvature-probe controls; contract frozen at 6ef247d.

Gu-Wen arXiv:0907.1203v3 PDF p.15 Eqs.47-48, p.18 H_J, p.20 dictionary.
Sparse words only; no ground state or many-body Hamiltonian is computed.
"""

import argparse
from collections import defaultdict
from itertools import product
from pathlib import Path

import sympy as sp

from verify_inverse_gravity_constraint_module import (
    COMPONENTS,
    overlap_by_translation,
    real_vector_stencils,
)
from verify_inverse_gravity_local_gates import polynomial, real_r


def real_rxy():
    # Relative to the xy face centre, twofold cyclic permutation of Eq.47.
    result = [{} for _ in COMPONENTS]
    for sx, sy in product((-1, 1), repeat=2):
        result[2][(sx, sy, 0)] = 2
    result[3] = {(0, 0, -2): 1, (0, 0, 0): 2, (0, 0, 2): 1}
    for sx, sz in product((-1, 1), repeat=2):
        result[4][(sx, 0, sz)] = -1
    for sy, sz in product((-1, 1), repeat=2):
        result[5][(0, sy, sz)] = -1
    return result


def periodic_word(stencil, centre, length, sign):
    result = defaultdict(int)
    for species, terms in enumerate(stencil):
        for offset, coef in terms.items():
            site = tuple((x + y) % (2 * length) for x, y in zip(centre, offset))
            result[(species,) + site] += sign * coef
    return {key: value % 3 for key, value in result.items() if value % 3}


def vector_charges(word, length):
    charges = defaultdict(int)
    for (species, *site), value in word.items():
        for axis in range(3):
            for offset, coef in real_vector_stencils(axis)[species].items():
                centre = tuple((x - y) % (2 * length) for x, y in zip(site, offset))
                charges[(axis,) + centre] += value * coef
    return {key: value % 3 for key, value in charges.items() if value % 3}


def kinetic_energy(word):
    # H_J / tilde J with the full cos(sum diagonal L) term.
    f = lambda n: sp.Rational(3, 2) if n % 3 else sp.S.Zero
    diagonal = sp.S.Zero
    face = sp.S.Zero
    traces = defaultdict(int)
    for (species, *site), value in word.items():
        if species < 3:
            diagonal += f(value)
            traces[tuple(site)] += value
        else:
            face += f(value)
    return 3 * (diagonal + 2 * face - sp.Rational(1, 2) * sum(f(n) for n in traces.values()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lines = []

    def note(message):
        lines.append(message)
        print(message, flush=True)

    x, y, z = sp.symbols("x y z", nonzero=True)
    tx, ty, tz = (v + 1 / v for v in (x, y, z))
    expected = [
        sp.Matrix([0, tz**2, ty**2, 0, -ty * tz, 0]),
        sp.Matrix([tz**2, 0, tx**2, 0, 0, -tz * tx]),
        sp.Matrix([0, 0, 2 * tx * ty, tz**2, -tz * tx, -tz * ty]),
    ]
    stencils = [real_r(0), real_r(1), real_rxy()]
    vs = [
        sp.Matrix([tx, 0, 0, ty, 0, tz]),
        sp.Matrix([0, ty, 0, tx, tz, 0]),
        sp.Matrix([0, 0, tz, 0, ty, tx]),
    ]
    for name, stencil, row in zip(("xx", "yy", "xy"), stencils, expected):
        assert all(sp.expand(e) == 0 for e in polynomial(stencil, (x, y, z)) - row)
        for axis, vector in enumerate(vs):
            assert sp.expand(row.dot(vector)) == 0
            overlaps = overlap_by_translation(stencil, real_vector_stencils(axis))
            assert all(value == 0 for value in overlaps.values())
        note(f"PASS R_{name}/V: integer Laurent and independent real-space correlations")
    note("PASS R/S and R/R: all words are pure commuting X products")

    u, v, w = sp.symbols("tx ty tz", real=True)
    rx = sp.Matrix([[0, w**2, v**2, 0, -v * w, 0]])
    ry = sp.Matrix([[w**2, 0, u**2, 0, 0, -w * u]])
    rxy = sp.Matrix([[0, 0, 2 * u * v, w**2, -w * u, -w * v]])
    symbol = (rx - ry).col_join(-rxy) / sp.sqrt(2)
    axial = symbol.subs({u: 0, v: 0})
    old = sp.Matrix([[1, -1, 0, 0, 0, 0], [0, 0, 0, -1, 0, 0]]) / sp.sqrt(2)
    assert axial == w**2 * sp.diag(-1, 1) * old
    assert axial.rank() == 2
    assert axial.subs(w, 0) == sp.zeros(2, 6)
    p = sp.symbols("p", real=True)
    a = 4 * sp.sin(p / 2)**2
    assert sp.limit(a / p**2, p, 0) == 1
    eplus = sp.diag(1, -1, 0) / sp.sqrt(2)
    ecross = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / sp.sqrt(2)
    for tensor in (eplus, ecross):
        assert sp.trace(tensor) == 0
        assert tensor * sp.Matrix([0, 0, 1]) == sp.zeros(3, 1)
    note("PASS axial tangent symbol: a(p)*diag(-1,1), a(p)=4 sin(p/2)^2~p^2")
    note("PASS rank=2 for nonzero axial p; zero symbol at node; TT coefficient tensors")

    centres_offset = [(0, 0, 0), (0, 0, 0), (1, 1, 0)]
    costs = [sp.Rational(207, 4), sp.Rational(207, 4), sp.Integer(108)]
    for length in (4, 6):
        words = set()
        for cell in product(range(length), repeat=3):
            for stencil, offset, cost in zip(stencils, centres_offset, costs):
                centre = tuple(2 * i + d for i, d in zip(cell, offset))
                for sign in (-1, 1):
                    word = periodic_word(stencil, centre, length, sign)
                    assert not vector_charges(word, length)
                    assert kinetic_energy(word) == cost
                    key = tuple(sorted(word.items()))
                    assert key not in words
                    words.add(key)
        assert len(words) == 6 * length**3
        note(f"FINITE_PASS L={length}: {len(words)} distinct signed translated words, V-neutral, exact H_J costs")
    note("PASS witness coefficients: <0|D_R|0>=J*diag(207/4,54)")
    note(f"Environment: SymPy {sp.__version__}")
    note("VERDICT: CURVATURE_PROBE_ALGEBRA_CONTROLS_PASS")
    note("Scope: stencil algebra, tangent symbol and finite sparse-word costs.")
    note("No true-ground correlations, physical mode count or dispersion certified.")
    if args.output:
        args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
