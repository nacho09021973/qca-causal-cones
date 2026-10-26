"""Derive W5 local source and transport-first-order variation for all families.

No complete Floquet stress tensor, conservation law or correlated-state closure.
"""

import sympy as sp

from certificate_utils import assert_sym_equal, sym_zero
from tetrad_transport import (DIRECTIONS, MOMENTA, PAULI, ZERO,
                              current_kick_checks, current_symbol, transport_jet)


def main():
    eta, g = sp.symbols("eta g", real=True)
    zs = sp.symbols("z1 z2 z3", real=True)
    _, H = transport_jet({(a, a): zs[a] for a in range(3)}, g)
    for a in range(3):
        J, A, R, slope = current_kick_checks(a, eta)
        symbol = current_symbol(a, a)
        phase = sum(p*d for p, d in zip(MOMENTA, DIRECTIONS[a]))
        assert_sym_equal(symbol, 2*sp.sin(phase)*PAULI[a], "Fourier current")
        assert_sym_equal(symbol.subs(ZERO), sp.zeros(2), "zero-momentum current")
        for i, p in enumerate(MOMENTA):
            assert_sym_equal(sp.diff(symbol, p).subs(ZERO),
                             2*DIRECTIONS[a][i]*PAULI[a], "directional slope")
        assert_sym_equal(sp.diff(H, zs[a]), g*symbol, "transport variation")
        assert not sym_zero(sp.diff(H, zs[a])+g*symbol), "reversed source sign undetected"
        assert_sym_equal(R.subs(eta, 0), sp.eye(R.rows), "spectator-inclusive flat gate")
        print(f"[PASS] a={a+1}: J^2=A, exact kick including zero sector, current symbol and dH/dz")

    # Trace the operator slope against arbitrary independent factor densities.
    x, y, z = sp.symbols("x y z", real=True)
    X, Y, Z = PAULI
    rho_g = (sp.eye(2)+x*X+y*Y+z*Z)/2
    matter = sp.Matrix(6, 6, sp.symbols("m0:36"))
    J, _, _, slope = current_kick_checks(2, eta)
    observed = sp.trace(sp.kronecker_product(rho_g, matter)*slope)
    assert_sym_equal(observed, -2*x*sp.trace(matter*J), "product-state source expectation")
    print("[PASS] operator slope -2 X tensor J gives -2 x <J> on independent states")
    print("\nVERDICT: all three W5 sources derived; variational identity is transport-first-order only.")


if __name__ == "__main__":
    main()
