#!/usr/bin/env python3
"""Exact algebra controls for IG1d, not a spectrum of the spatial QCA.

Contract: theory/INVERSE_GRAVITY_IR_REFERENCE_GATE.md.
General proofs are recorded in the corresponding report.
"""

import sympy as sp


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def gate(word):
    projector = (sp.eye(3) + word + word**2) / 3
    phase = sp.sqrt(3) / 2 + sp.I / 2
    return phase * (sp.eye(3) + (-sp.I - 1) * projector)


def main():
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    X = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Z = sp.diag(1, omega, sp.simplify(omega**2))
    R, T = X, Z.H
    assert clean(T * R - sp.conjugate(omega) * R * T) == sp.zeros(3)
    assert (R - sp.eye(3)).col_join(T - sp.eye(3)).rank() == 3
    print("PASS Weyl pair: no common vector R=T=1 in exact qutrit control")

    rho = sp.eye(3) / 3
    U = clean(gate(T) * gate(R))
    assert clean(U.H * U - sp.eye(3)) == sp.zeros(3)
    A, B = clean((T + T.H) / 2), clean((R + R.H) / 2)
    evolved = A
    positive_witness = False
    for n in range(3):
        comm = clean(B * evolved - evolved * B)
        response = sp.simplify(sp.I * sp.trace(rho * comm))
        assert response == 0
        squared = sp.simplify(sp.trace(rho * comm.H * comm))
        positive_witness |= squared.is_positive is True
        print(f"PASS algebra control n={n}: response=0; commutator squared mean={squared}")
        evolved = clean(U.H * evolved * U)
    assert positive_witness
    assert clean(U * rho * U.H - rho) == sp.zeros(3)
    print("PASS invariant tracial state and nonzero squared commutator coexist")

    # Positive control: same A/B, explicitly fixed non-tracial state.
    psi = sp.Matrix([1, sp.I, 0]) / sp.sqrt(2)
    pure = psi * psi.H
    response = sp.simplify(sp.I * sp.trace(pure * (B * A - A * B)))
    assert response != 0
    print(f"PASS non-tracial positive control: response={response}")
    print("VERDICT: TRACIAL_REFERENCE_RESPONSE_NULL / TERMWISE_VACUUM_INCOMPATIBLE")
    print("Scope: algebra controls; general sector proof in report; no QCA modes or IR.")


if __name__ == "__main__":
    main()
