#!/usr/bin/env python3
"""Exact physical energy witness for option A0; no many-body diagonalization.

Contract: theory/INVERSE_GRAVITY_A0_CONSERVATION_GATE.md.
All scientific computations remain in this permanent certificate.
"""

from fractions import Fraction

import sympy as sp

from verify_inverse_gravity_constraint_module import overlap_by_translation
from verify_inverse_gravity_local_gates import real_r, real_w
from verify_inverse_gravity_full_tick_dynamics import stencil_charges, geometric_charges


def rank_mod3(matrix):
    a = [[int(v) % 3 for v in row] for row in matrix]
    if not a:
        return 0
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = 1 if a[rank][col] == 1 else 2
        a[rank] = [(v * inv) % 3 for v in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor * y) % 3 for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def main():
    g0 = sp.Rational(1, 2) - sp.I * sp.sqrt(3) / 2
    g1 = sp.sqrt(3) / 2 + sp.I / 2
    phases = [g0, g1, g1]
    factors = []
    for s in (-1, 1):
        factor = sp.simplify(sum(sp.conjugate(phases[n]) * phases[(n + s) % 3]
                                 for n in range(3)) / 3)
        assert factor == sp.Rational(1, 3)
        factors.append(factor)
    print("PASS independent root-phase calculation: both Weyl signs give constant 1/3")

    expectations = []
    for r_axis in range(3):
        affected = []
        for t_axis in range(3):
            for center, exponent in overlap_by_translation(real_r(r_axis), real_w(t_axis)).items():
                if exponent % 3:
                    affected.append((t_axis, center))
        columns = []
        for axis, center in affected:
            assert all(c % 2 for c in center)
            charges = stencil_charges(axis, center)
            origin = tuple((c - 1) // 2 for c in center)
            assert charges == geometric_charges(axis, origin)
            columns.append(charges)
        rows = sorted(set().union(*(column.keys() for column in columns)))
        matrix = [[column.get(row, 0) for column in columns] for row in rows]
        rank = rank_mod3(matrix)
        print(f"R axis={r_axis}: affected T gates={len(affected)}, charge rank F3={rank}")
        if rank != len(affected):
            print("VERDICT: A0_METHOD_UNRESOLVED")
            return
        expectation = Fraction(1, 3)**len(affected)
        expectations.append(expectation)
        print(f"Exact <U_T^dag R U_T>_psi0={expectation}")
    assert expectations[0] == expectations[1] == expectations[2]
    density = sum((1 - value for value in expectations), Fraction(0))
    print(f"Delta <H_A>/L^3={density} (exact)")
    if density:
        print("VERDICT: A0_FAIL_NONCONSERVED_PHYSICAL_PARENT")
        print("NEXT: B0 activated with the already frozen beta=1 seed; no gate change.")
    else:
        print("VERDICT: FROZEN_ENERGY_WITNESS_ZERO")
    print("Scope: exact physical state energy witness; not a Gibbs or IR spectrum computation.")


if __name__ == "__main__":
    main()
