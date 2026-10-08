#!/usr/bin/env python3
"""Exact certificate for the explicitly specified dressed commuting parent.

Contract: theory/INVERSE_GRAVITY_DRESSED_PARENT_GATE.md.
Spatial claims are proved in the report; no many-body matrix is simulated.
"""

from itertools import product

import sympy as sp

from verify_inverse_gravity_constraint_module import (
    overlap_by_translation, real_scalar_stencils, real_vector_stencils,
)
from verify_inverse_gravity_local_gates import real_r, real_w, polynomial
from verify_inverse_gravity_full_tick_dynamics import stencil_charges, geometric_charges


def zero(matrix):
    return all(sp.simplify(value) == 0 for value in matrix)


def main():
    print(f"SymPy {sp.__version__}; exact arithmetic")
    for a in range(3):
        for b in range(3):
            assert all(v % 3 == 0 for v in overlap_by_translation(
                real_r(a), real_vector_stencils(b)).values())
        assert all(v % 3 == 0 for v in overlap_by_translation(
            real_scalar_stencils(), real_w(a)).values())
    variables = sp.symbols("x y z", nonzero=True)
    assert zero(sum((polynomial(real_r(a), variables) for a in range(3)), sp.zeros(6, 1))
                - polynomial(real_scalar_stencils(), variables))
    print("PASS spatial algebra: R/V and T/S; redundancy sum r_aa=c")

    omega = -sp.Rational(1, 2) + sp.I*sp.sqrt(3)/2
    r = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    z = sp.diag(1, omega, sp.simplify(omega**2))
    t = z.adjoint()
    pi = (sp.eye(3)+r+r*r)/3
    h = sp.eye(3)-pi
    pi_t = (sp.eye(3)+t+t*t)/3
    d = (sp.sqrt(3)/2+sp.I/2)*(sp.eye(3)+(-sp.I-1)*pi_t)
    assert zero(pi*pi-pi) and zero(h*h-h)
    assert zero(d.adjoint()*d-sp.eye(3))
    dressed_h = (d*h*d.adjoint()).applyfunc(sp.simplify)
    ground = (d*pi*d.adjoint()).applyfunc(sp.simplify)
    phase = sp.symbols("phase", nonzero=True)
    f = pi+phase*h
    f_inverse = pi+h/phase  # Equals F† for a unit-modulus phase.
    u = d*f*d.adjoint()
    u_inverse = d*f_inverse*d.adjoint()
    assert zero(u_inverse*u-sp.eye(3))
    assert zero(u_inverse*dressed_h*u-dressed_h)
    assert zero(u*ground-ground) and zero(dressed_h*ground)
    assert dressed_h != h
    assert sp.simplify(sp.trace(dressed_h)) == 2
    assert sp.simplify(sp.trace(ground)) == 1
    print("PASS auxiliary dressing: changed parent, exact inverse, conserved energy, fixed ground projector")

    nonzero_weights = []
    for chars in product(range(3), repeat=3):
        if sum(chars) % 3 == 0:
            count = sum(v != 0 for v in chars)
            if count:
                nonzero_weights.append(count)
    assert min(nonzero_weights) == 2
    assert set(nonzero_weights) == {2, 3}
    print("PASS vertex characters: S=1 excludes exactly one violated R; global positive gap >=2")

    charges = stencil_charges(0, (1, 1, 1))
    assert charges == geometric_charges(0, (0, 0, 0))
    violated = [value for value in charges.values() if value % 3]
    assert len(violated) == 16
    assert all(sum(charges.get((a, vertex), 0) for a in range(3)) % 3 == 0
               for vertex in set(vertex for _, vertex in charges))
    print("PASS fixed physical excitation: T_x creates 16 violated R, energy=16")
    print("CERTIFIED ENERGY GAP INTERVAL: 2 <= gap(K_E|physical) <= 16")
    print("Scope: interval uniform on admitted tori; no claim that either endpoint is the exact gap")
    print("VERDICT: DRESSED_PARENT_ALGEBRA_PASS_AUTHOR_SIDE")


if __name__ == "__main__":
    main()
