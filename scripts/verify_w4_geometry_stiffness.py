"""Exact symbolic certificate for theory/W4_GEOMETRY_STIFFNESS_GATE.md."""

import sympy as sp


def kron(a, b):
    return sp.kronecker_product(a, b)


def main():
    k = sp.symbols("k", real=True)
    I2 = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Z = sp.diag(1, -1)
    I4 = sp.eye(4)

    # SWAP in computational basis.
    S = sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ])
    assert S.H == S and S*S == I4
    pauli_swap = sp.simplify((I4 + kron(X, X) + kron(Y, Y) + kron(Z, Z))/2)
    assert pauli_swap == S
    print("[PASS] SWAP is Hermitian/unitary and equals (I+XX+YY+ZZ)/2")

    # Exact partial-SWAP form.
    K = sp.exp(-sp.I*k) * (sp.cos(k)*I4 + sp.I*sp.sin(k)*S)
    H = I4 - S
    # Differentiate at k=0 to verify generator.
    dK0 = sp.simplify(sp.diff(K, k).subs(k, 0))
    assert dK0 == -sp.I*H
    print("[PASS] K(k)=exp[-ik(I-S)] has the declared generator")

    # Homogeneous two-qubit state is fixed because it is symmetric.
    a, b = sp.symbols("a b")
    n = sp.Matrix([a, b])
    nn = kron(n, n)
    assert sp.simplify(S*nn - nn) == sp.zeros(4, 1)
    assert sp.simplify(H*nn) == sp.zeros(4, 1)
    print("[PASS] every identical-product pair |n,n> is fixed exactly")

    # Local Z-defect propagation.
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    psi0 = kron(ket1, ket0)  # |1,0>
    psi = sp.simplify(K*psi0)
    expected = sp.exp(-sp.I*k)*(sp.cos(k)*kron(ket1, ket0) + sp.I*sp.sin(k)*kron(ket0, ket1))
    assert sp.simplify(psi-expected) == sp.zeros(4, 1)

    Ze = kron(Z, I2)
    Zf = kron(I2, Z)
    ze = sp.simplify((psi.H*Ze*psi)[0])
    zf = sp.simplify((psi.H*Zf*psi)[0])
    assert sp.trigsimp(ze + sp.cos(2*k)) == 0
    assert sp.trigsimp(zf - sp.cos(2*k)) == 0
    assert sp.simplify(ze+zf) == 0
    print("[PASS] |1,0> spreads autonomously: <Z_e>=-cos(2k), <Z_f>=cos(2k)")

    # At k=pi/2 the defect swaps fully.
    psi_swap = sp.simplify(psi.subs(k, sp.pi/2))
    target = sp.simplify(sp.exp(-sp.I*sp.pi/2)*sp.I*kron(ket0, ket1))
    assert sp.simplify(psi_swap-target) == sp.zeros(4, 1)
    print("[PASS] k=pi/2 gives a full one-bond geometry transfer")

    print("\nVERDICT: geometry-only partial-SWAP transports the tetrad-control variable in vacuum.")


if __name__ == "__main__":
    main()
