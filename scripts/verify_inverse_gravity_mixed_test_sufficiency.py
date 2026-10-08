#!/usr/bin/env python3
"""Exact auxiliary moments for the sufficiency audit frozen at cb25f19.

No many-body Hamiltonian, ground projector, or SDP is constructed.
"""

import argparse
from itertools import product
from pathlib import Path

import sympy as sp

from verify_inverse_gravity_constraint_module import real_scalar_stencils
from verify_inverse_gravity_local_gates import real_r
from verify_inverse_gravity_curvature_probes import real_rxy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    lines = []

    def note(message):
        print(message, flush=True)
        lines.append(message)

    f = lambda n: sp.Rational(3, 2) if n % 3 else sp.S.Zero

    def diagonal_energy(a):
        return 3 * (sum(f(n) for n in a) - f(sum(a)) / 2)

    stencil = real_scalar_stencils()
    faces = sum(sum(c % 3 != 0 for c in row.values()) for row in stencil[3:])
    assert faces == 12
    central_cost = sum(
        diagonal_energy(tuple(n + 1 for n in a)) - diagonal_energy(a)
        for a in product(range(3), repeat=3) if a[0] == 0
    ) / 27
    assert central_cost == sp.Rational(3, 2)
    full_average = sum(
        diagonal_energy(tuple(n + shift for n, shift in zip(a, delta))) - diagonal_energy(a)
        for a in product(range(3), repeat=3)
        for delta in [(1, 1, 0)]
    ) / 27
    assert full_average == 0
    kinetic_cost = central_cost + faces * 9 / sp.Integer(3)
    assert kinetic_cost == sp.Rational(75, 2)
    note("PASS tau conditional central kinetic cost=3 J/2; other diagonal averages unchanged")
    note("PASS twelve scalar face shifts: <T^dagger[H_J,T]>_tau=75 J/2")

    face_counts = []
    for probe in [real_r(0), real_r(1), real_rxy()]:
        face_counts.append(sum(sum(c % 3 != 0 for c in row.values()) for row in probe[3:]))
    assert face_counts == [4, 4, 11]
    assert 9 * (face_counts[0] + face_counts[1]) / sp.Integer(2) == 36
    assert 9 * face_counts[2] / sp.Integer(2) == sp.Rational(99, 2)
    note("PASS tau curvature numerator coefficients: diag(36,99/2)*J")

    u2, j = sp.symbols("U2 J", positive=True)
    m = sp.Matrix([[0, -u2 / 2], [-u2 / 2, sp.Rational(75, 2) * j]])
    assert m.det() == -u2**2 / 4
    t = u2 / (75 * j)
    v = sp.Matrix([1, t])
    assert sp.simplify((v.T * m * v)[0]) == -u2**2 / (150 * j)
    note("PASS coherent mixed cost determinant=-U2^2/4; explicit cost=-U2^2/(150 J)")
    note(f"Environment: SymPy {sp.__version__}")
    note("VERDICT: MIXED_TEST_SUFFICIENCY_AUXILIARY_CONTROLS_PASS")
    note("Scope: local conditional averages, stencil counts, symbolic 2x2 matrix.")
    note("No true-ground numerator, Gram or spectrum computed.")
    if args.output:
        args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
