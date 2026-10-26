"""Exact symbolic certificate for theory/W3_BACKREACTING_TETRAD_FLOQUET_GATE.md."""

import sympy as sp
from certificate_utils import assert_sym_equal, sym_zero
from tetrad_transport import transport_jet


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
    assert_sym_equal(Zrot, expected, "occupied-sector Z rotation")
    print("[PASS] R_e rotates Z exactly to Z cos(2g)-X sin(2g) on occupied endpoints")

    x, z, a = sp.symbols("x z a", real=True)
    dz = sp.expand(a * ((sp.cos(2*g) - 1) * z - sp.sin(2*g) * x))
    slope = sp.simplify(sp.diff(dz, g).subs(g, 0))
    assert_sym_equal(slope, -2*a*x, "initial product-state slope")
    print("[PASS] z'-z = -2 g x a + O(g^2)")

    # W2 direction matrix and W3 tetrad control.
    D = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
    assert D.det() == 1
    E0 = sp.diag(1, -1, 1)
    z1, z2, z3 = sp.symbols("z1 z2 z3", real=True)
    E, _ = transport_jet({(i, i): z for i, z in enumerate((z1, z2, z3))}, g)
    assert_sym_equal(E, E0 - 2*g*sp.diag(z1, z2, z3)*D,
                     "E derived from edge Fourier currents and CJWW jet")
    assert_sym_equal(E.subs(g, 0), E0, "flat transport")
    assert not sym_zero(E-(E0+2*g*sp.diag(z1, z2, z3)*D)), "reversed sign undetected"
    print("[PASS] E derived from transport currents and the CJWW step, including sign control")

    # Matter-dependent correction after one backreaction kick:
    x1, x2, x3, a1, a2, a3 = sp.symbols("x1 x2 x3 a1 a2 a3", real=True)
    dz_vec = sp.Matrix([-2*g*x1*a1, -2*g*x2*a2, -2*g*x3*a3])
    dE_back = sp.simplify(-2*g*sp.diag(*list(dz_vec))*D)
    expected_back = 4*g**2*sp.diag(x1*a1, x2*a2, x3*a3)*D
    derived_change = E.subs(dict(zip((z1,z2,z3), sp.Matrix([z1,z2,z3])+dz_vec)), simultaneous=True)-E
    assert_sym_equal(derived_change, expected_back, "mean-field transport feedback")
    assert_sym_equal(dE_back, expected_back, "feedback matrix check")
    print("[PASS] O(g^2) feedback is the mean-field contribution only")

    print("\nVERDICT: W3 transport jet derived; feedback remains mean-field, not a full correlated coefficient.")


if __name__ == "__main__":
    main()
