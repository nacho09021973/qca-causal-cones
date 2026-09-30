"""Exact symbolic certificate for theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md.

Checks the CJWW (5.15) linear symbol and the declared transport-current
principal-symbol deformation. No floating point and no gravity claim.

Run:
    python3 scripts/verify_w2_transport_tetrad.py
"""

import sympy as sp

from verify_directional_saturation import walk2, P1, P2, P3, PAULI


def main():
    W = walk2()
    zero = {P1: 0, P2: 0, P3: 0}
    dW = [sp.simplify(sp.diff(W, p).subs(zero)) for p in (P1, P2, P3)]

    assert dW[0] == sp.I * PAULI[0]
    assert dW[1] == -sp.I * PAULI[1]
    assert dW[2] == sp.I * PAULI[2]
    print("[PASS] CJWW linear symbol is I+i(p1 sigma1-p2 sigma2+p3 sigma3)+O(p^2)")

    D = sp.Matrix([
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
    ])
    assert D.det() == 1
    print("[PASS] selected support directions span R^3 with det D = 1")

    g, b1, b2, b3 = sp.symbols("g b1 b2 b3", real=True)
    E0 = sp.diag(1, -1, 1)
    E = E0 - 2 * g * sp.diag(b1, b2, b3) * D

    expected = sp.Matrix([
        [1 - 2*g*b1, 0, 0],
        [-2*g*b2, -1 - 2*g*b2, 0],
        [-2*g*b3, -2*g*b3, 1 - 2*g*b3],
    ])
    assert E == expected
    print("[PASS] first-order Weyl coefficient matrix E(g) is geometry dependent")

    # Isolated family-1 deformation changes the p1 characteristic coefficient.
    E1 = sp.simplify(E.subs({b2: 0, b3: 0}))
    metric1 = sp.simplify(E1.T * E1)
    assert metric1[0, 0] == (1 - 2*g*b1)**2
    assert metric1[1, 1] == 1
    assert metric1[2, 2] == 1
    print("[PASS] isolated b1 changes the local cone coefficient along p1")

    # Current Fourier symbol: i(T_d-T_-d) sigma_a = 2 sin(p.d) sigma_a.
    q = sp.symbols("q", real=True)
    current_scalar = sp.simplify(sp.I * (sp.exp(-sp.I*q) - sp.exp(sp.I*q)))
    assert sp.simplify(current_scalar - 2*sp.sin(q)) == 0
    assert sp.diff(current_scalar, q).subs(q, 0) == 2
    print("[PASS] edge current has symbol 2 sin(p.d) sigma_a and linear slope 2 d.p")

    # Nondegeneracy is stable for sufficiently small g.
    assert sp.simplify(sp.det(E).subs(g, 0) + 1) == 0
    print("[PASS] det E(0) = -1, so the perturbed tetrad stays nondegenerate near g=0")

    print("\nVERDICT: W2 has an explicit geometry-dependent principal-symbol deformation.")


if __name__ == "__main__":
    main()
