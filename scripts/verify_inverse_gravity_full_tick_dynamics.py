#!/usr/bin/env python3
"""Frozen IG1c one-step physical witness; exact finite incidence arithmetic.

No many-body diagonalization, spectral fitting, IR assumption, or gate changes.
Contract: theory/INVERSE_GRAVITY_FULL_TICK_DYNAMICS_GATE.md.
"""

from itertools import product

from verify_inverse_gravity_constraint_module import overlap_by_translation
from verify_inverse_gravity_local_gates import real_r, real_w


Q = 3
O_AXIS, B_AXIS = 0, 1
O_CENTER, B_CENTER = (1, 1, 1), (3, 3, 3)


def support(axis, center):
    return {
        (component, tuple(a + b for a, b in zip(center, shift)))
        for component, stencil in enumerate(real_w(axis))
        for shift, value in stencil.items() if value % Q
    }


def stencil_charges(axis, center):
    charges = {}
    for r_axis in range(3):
        overlaps = overlap_by_translation(real_r(r_axis), real_w(axis))
        for relative, value in overlaps.items():
            if value % Q:
                r_center = tuple(c - d for c, d in zip(center, relative))
                assert all(c % 2 == 0 for c in r_center)
                # R C = omega^(-overlap) C R; R eigenvalue on C|psi0>.
                charges[(r_axis, r_center)] = (-value) % Q
    return charges


def geometric_charges(axis, cube_origin):
    # Source-derived cyclic charge vector: Tx -> (0,-1,+1), etc.
    charge_vector = [0, 0, 0]
    charge_vector[(axis + 1) % 3] = -1
    charge_vector[(axis + 2) % 3] = 1
    charges = {}
    for corner in product((0, 1), repeat=3):
        vertex = tuple(2 * (i + b) for i, b in zip(cube_origin, corner))
        for r_axis, value in enumerate(charge_vector):
            if value % Q:
                charges[(r_axis, vertex)] = value % Q
    return charges


def add_charges(first, second):
    return {
        key: value for key in first.keys() | second.keys()
        if (value := (first.get(key, 0) + second.get(key, 0)) % Q)
    }


def exact_phase(delta_m):
    # exp[-i*pi*delta_m/2], represented by integer real/imaginary parts.
    return ((1, 0), (0, -1), (-1, 0), (0, 1))[delta_m % 4]


def main():
    assert support(O_AXIS, O_CENTER).isdisjoint(support(B_AXIS, B_CENTER))
    print("PASS initial O/B physical-word supports disjoint; [O,B]=0")
    o = stencil_charges(O_AXIS, O_CENTER)
    b = stencil_charges(B_AXIS, B_CENTER)
    assert o == geometric_charges(O_AXIS, (0, 0, 0))
    assert b == geometric_charges(B_AXIS, (1, 1, 1))
    print("PASS two formulations: all stencil incidences equal cube-vertex charges")
    ob = add_charges(o, b)
    m_o, m_b, m_ob = len(o), len(b), len(ob)
    f0, fb = exact_phase(m_o), exact_phase(m_ob - m_b)
    norm_squared = sum((x - y)**2 for x, y in zip(fb, f0))
    print(f"M(O)={m_o}; M(B)={m_b}; M(OB)={m_ob}")
    print(f"f0(real,imag)={f0}; fB(real,imag)={fb}")
    assert norm_squared <= 4
    print(f"||[U^dag O U,B] psi0||^2={norm_squared} (exact)")
    if norm_squared == 0:
        print("VERDICT: FROZEN_WITNESS_NO_INFLUENCE")
        return
    print("VERDICT: FULL_TICK_ONE_STEP_PHYSICAL_INFLUENCE_PASS_AUTHOR_SIDE")
    print("Scope: frozen tick, physical sector, one step; no IR, modes, or gravity.")


if __name__ == "__main__":
    main()
