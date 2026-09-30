"""Exact symbolic certificate for theory/W5_TETRAD_CONJUGATE_SOURCE_GATE.md."""

import sympy as sp

from verify_directional_saturation import PAULI


def main():
    # Two-site position factor ordered as |x>, |y>.
    I2 = sp.eye(2)
    Yg = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    Zg = sp.diag(1, -1)
    Xg = sp.Matrix([[0, 1], [1, 0]])

    # Spatial current i(|y><x|-|x><y|).
    Q = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma = PAULI[0]
    J = sp.kronecker_product(Q, sigma)
    A = sp.kronecker_product(sp.eye(2), sp.eye(2))

    # On the declared two-endpoint matter sector J^2=I; in the full lattice this
    # identity is J_e^2=A_e (endpoint projector).
    assert sp.simplify(J*J - A) == sp.zeros(4)
    print("[PASS] edge current squares to the endpoint projector on its support")

    eta = sp.symbols("eta", real=True)
    # Functional identities implied by spectrum {-1,0,+1}.
    c, s = sp.cos(2*eta), sp.sin(2*eta)

    # Check the Pauli rotation sign on each J eigenvalue +/-1.
    for lam in (+1, -1):
        Rg = sp.cos(eta)*I2 - sp.I*sp.sin(eta)*lam*Yg
        Zrot = sp.simplify(Rg.H*Zg*Rg)
        expected = sp.simplify(c*Zg - lam*s*Xg)
        assert sp.simplify(Zrot-expected) == sp.zeros(2)
    print("[PASS] Z rotation is Z cos(2 eta J)-X sin(2 eta J)")

    x, z, a, j = sp.symbols("x z a j", real=True)
    dz = sp.expand(z*(1+(c-1)*a) - x*s*j - z)
    slope = sp.simplify(sp.diff(dz, eta).subs(eta, 0))
    assert slope == -2*x*j
    print("[PASS] z'-z = -2 eta x <J> + O(eta^2)")

    # Continuum current symbol.
    q = sp.symbols("q", real=True)
    jsym = sp.simplify(sp.I*(sp.exp(-sp.I*q)-sp.exp(sp.I*q)))
    assert sp.simplify(jsym-2*sp.sin(q)) == 0
    assert sp.diff(jsym, q).subs(q, 0) == 2
    print("[PASS] J_a(p)=2 sin(p.d_a) sigma_a = 2(d_a.p) sigma_a + O(p^3)")

    print("\nVERDICT: W5 source is exactly tetrad-conjugate at the declared perturbative level.")


if __name__ == "__main__":
    main()
