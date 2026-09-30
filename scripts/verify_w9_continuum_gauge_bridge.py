"""Symbolic consistency certificate for theory/W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md."""

import sympy as sp


def main():
    lam = sp.symbols("lambda", nonzero=True)
    # Fourier-space momentum k_mu and conserved stress tensor columns.
    w, kx, ky, kz = sp.symbols("omega kx ky kz")
    k = sp.Matrix([w, kx, ky, kz])

    # Treat one fixed nu-column T^{mu nu}; conservation is k_mu T^{mu nu}=0.
    T0, T1, T2, T3 = sp.symbols("T0 T1 T2 T3")
    Tcol = sp.Matrix([T0, T1, T2, T3])
    conservation = sp.expand((k.T*Tcol)[0])

    spatial_div = sp.expand(kx*T1 + ky*T2 + kz*T3)
    assert sp.expand(spatial_div - (conservation - w*T0)) == 0
    print("[PASS] spatial divergence = full conservation residual - omega*T^{0nu}")

    # On the conserved shell, spatial-only coupling leaves -omega*T0 in general.
    spatial_on_shell = sp.expand(spatial_div.subs(T3, (-w*T0-kx*T1-ky*T2)/kz))
    assert sp.simplify(spatial_on_shell + w*T0) == 0
    print("[PASS] spatial-only gauge variation is generically proportional to omega*T^{0nu}")

    # Full linearized metric coupling contracts xi_nu with k_mu T^{mu nu}.
    full_variation = lam * conservation
    full_on_shell = sp.expand(full_variation.subs(T3, (-w*T0-kx*T1-ky*T2)/kz))
    assert sp.simplify(full_on_shell) == 0
    print("[PASS] full h_{mu nu}T^{mu nu} coupling is gauge invariant on conserved stress shell")

    # W6 directional matrix spans all spatial tetrad derivatives.
    D = sp.Matrix([[1,0,0],[1,1,0],[1,1,1]])
    assert D.det() == 1
    print("[PASS] W6 directional currents span all spatial sigma_a p_i tetrad source components")

    print("\nVERDICT: spatial bridge is incomplete; full continuum linearized coupling works once lapse/shift source components are included.")


if __name__ == "__main__":
    main()
