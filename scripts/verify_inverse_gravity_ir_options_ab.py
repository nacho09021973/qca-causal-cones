#!/usr/bin/env python3
"""IG1e exact algebra controls; never a verdict on the spatial QCA options.

Contract: theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md.
"""

import sympy as sp

from verify_inverse_gravity_ir_reference import clean, gate


def main():
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    R = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    T = sp.diag(1, sp.conjugate(omega), omega)
    U_control = clean(gate(T) * gate(R))
    H_control = clean(-(R + R.H + T + T.H) / 2)
    residual = clean(U_control * H_control - H_control * U_control)
    assert residual != sp.zeros(3)
    print("PASS A control: auxiliary local terms do not automatically define a conserved H")
    print("Scope: qutrit control only; A0 of the spatial constrained tick NOT_TESTED")

    V = sp.diag(1, sp.I, -1)  # Explicit finite-period control, not QCA tick.
    seed = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(1, 6), 0],
        [sp.Rational(1, 6), sp.Rational(1, 3), 0],
        [0, 0, sp.Rational(1, 6)],
    ])
    assert seed.det() > 0 and sp.trace(seed) == 1
    rho = clean(sum((V**n * seed * (V.H)**n for n in range(4)), sp.zeros(3)) / 4)
    assert rho == sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 6))
    assert V * rho * V.H == rho and rho != sp.eye(3) / 3
    A = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    B = sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]])
    A1 = V.H * A * V
    response = sp.simplify(sp.I * sp.trace(rho * (B * A1 - A1 * B)))
    assert response != 0
    print("PASS B control: full-period average stationary, non-tracial, positive and normalized")
    print(f"PASS B control response at n=1: {response}")

    # Degenerate eigenphases must retain intra-block coherence.
    V_degenerate = sp.diag(1, 1, -1)
    pinched = (seed + V_degenerate * seed * V_degenerate.H) / 2
    assert pinched[0, 1] == sp.Rational(1, 6)
    assert V_degenerate * pinched * V_degenerate.H == pinched
    print("PASS degenerate-phase control: intra-block coherence retained")
    print("VERDICT: AB_ALGEBRA_CONTROLS_PASS / SPATIAL_A_AND_B_OPEN")


if __name__ == "__main__":
    main()
