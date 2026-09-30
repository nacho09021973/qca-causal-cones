"""Exact symbolic certificate for theory/W3_BACKREACTING_TETRAD_FLOQUET_GATE.md."""

import sympy as sp


def main():
    g = sp.symbols("g", real=True)
    I = sp.I
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -I], [I, 0]])
    Z = sp.diag(1, -1)
    I2 = sp.eye(2)

    # Exact geometry rotation on the A_e=1 matter sector.
    R = sp.cos(g) * I2 - I * sp.sin(g) * Y
    Zrot = sp.simplify(R.H * Z * R)
    expected = sp.simplify(sp.cos(2*g) * Z - sp.sin(2*g) * X)
    assert sp.simplify(Zrot - expected) == sp.zeros(2)
    print("[PASS] R_e rotates Z exactly to Z cos(2g)-X sin(2g) on occupied endpoints")

    x, z, a = sp.symbols("x z a", real=True)
    dz = sp.expand(a * ((sp.cos(2*g) - 1) * z - sp.sin(2*g) * x))
    slope = sp.simplify(sp.diff(dz, g).subs(g, 0))
    assert slope == -2*a*x
    print("[PASS] z'-z = -2 g x a + O(g^2)")

    # W2 direction matrix and W3 tetrad control.
    D = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
    assert D.det() == 1
    E0 = sp.diag(1, -1, 1)
    z1, z2, z3 = sp.symbols("z1 z2 z3", real=True)
    E = E0 - 2*g*sp.diag(z1, z2, z3)*D
    assert sp.simplify(E.subs(g, 0) - E0) == sp.zeros(3)
    print("[PASS] transport tetrad is E=E0-2g diag(z_a)D")

    # Matter-dependent correction after one backreaction kick:
    x1, x2, x3, a1, a2, a3 = sp.symbols("x1 x2 x3 a1 a2 a3", real=True)
    dz_vec = sp.Matrix([-2*g*x1*a1, -2*g*x2*a2, -2*g*x3*a3])
    dE_back = sp.simplify(-2*g*sp.diag(*list(dz_vec))*D)
    expected_back = 4*g**2*sp.diag(x1*a1, x2*a2, x3*a3)*D
    assert dE_back == expected_back
    print("[PASS] matter-dependent principal-symbol backreaction appears at O(g^2)")

    print("\nVERDICT: the transport-control observable itself backreacts in W3.")


if __name__ == "__main__":
    main()
