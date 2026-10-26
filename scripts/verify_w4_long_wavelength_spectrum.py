"""W4 one-defect spectrum, with the phase relative to the fixed vacuum.

Exact algebra only; no metric-wave or 3D/tensor interpretation. See
reports/2026-10-26--w4-spectrum-audit.md for branches, units and exclusions.
The finite-qubit/observable cross-check is verify_w4_spectrum_observables.py.
"""

import sympy as sp

from certificate_utils import assert_sym_equal, sym_zero


def bloch_layers(k, kap, second_sign):
    """Phase-stripped layers for psi_(A/B,m) = exp(i*k*m) u_(A/B)."""
    assert second_sign in (-1, 1)
    c, s = sp.cos(kap), sp.sin(kap)
    even = sp.Matrix([[c, sp.I*s], [sp.I*s, c]])
    odd = sp.Matrix([[c, second_sign*sp.I*s*sp.exp(-sp.I*k)],
                     [second_sign*sp.I*s*sp.exp(sp.I*k), c]])
    return even, odd


def bloch_step(k, kap, second_sign):
    """Full K_odd K_even in the one-defect sector; vacuum eigenvalue is 1."""
    even, odd = bloch_layers(k, kap, second_sign)
    return sp.exp(-sp.I*(1+second_sign)*kap) * odd * even


def main():
    k, kap = sp.symbols("k kap", real=True)
    c, s = sp.cos(kap), sp.sin(kap)
    swap = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                      [0, 1, 0, 0], [0, 0, 0, 1]])
    gate = sp.exp(-sp.I*kap)*(c*sp.eye(4)+sp.I*s*swap)
    assert_sym_equal(gate.H*gate, sp.eye(4), "local unitarity")
    assert_sym_equal(sp.diff(gate, kap).subs(kap, 0),
                     -sp.I*(sp.eye(4)-swap), "declared generator")
    assert_sym_equal(gate[:, 0], sp.eye(4)[:, 0], "fixed vacuum")
    even, _ = bloch_layers(k, kap, 1)
    assert_sym_equal(gate.extract([1, 2], [1, 2]),
                     sp.exp(-sp.I*kap)*even, "occupied bond phase")
    a, b = sp.symbols("a b")
    pair = sp.Matrix([a*a, a*b, b*a, b*b])
    assert_sym_equal(gate*pair, pair, "every identical pure pair fixed")
    print("[PASS] full local gate: generator, unitarity, vacuum and occupied-bond phase")

    traces = {}
    stripped = {}
    for sign in (1, -1):
        even, odd = bloch_layers(k, kap, sign)
        stripped[sign] = odd*even
        traces[sign] = c**2-sign*s**2*sp.cos(k)
        assert_sym_equal(sp.trace(stripped[sign])/2, traces[sign])
        assert_sym_equal(stripped[sign].det(), 1)
        full = bloch_step(k, kap, sign)
        assert_sym_equal(full.H*full, sp.eye(2))
        assert_sym_equal(full.det(), sp.exp(-2*sp.I*(1+sign)*kap))
    print("[PASS] both traces, determinants and full Bloch unitaries with sector phases")

    full_plus = bloch_step(k, kap, 1)
    uniform, antisymmetric = sp.Matrix([1, 1]), sp.Matrix([1, -1])
    assert_sym_equal(full_plus.subs(k, 0)*uniform, uniform)
    assert_sym_equal(full_plus.subs(k, 0)*antisymmetric,
                     sp.exp(-4*sp.I*kap)*antisymmetric)
    assert_sym_equal(full_plus.subs(k, sp.pi), sp.exp(-2*sp.I*kap)*sp.eye(2))
    # Mutation guard: stripping the phase loses the eigenvalue 1 relative to vacuum.
    assert not sym_zero((stripped[1].subs({k: 0, kap: sp.pi/4})-sp.eye(2))*uniform)
    print("[PASS] same-sign uniform eigenvalue 1; zone-edge crossing at quasienergy 2*kappa")

    # lambda=exp(-i*epsilon); for fixed 0<kap<pi/2, epsilon(0)=0.
    # F_epsilon=sin(2*kap) != 0 gives an analytic even implicit branch.
    eps = sp.symbols("eps", real=True)
    equation = sp.cos(2*kap-eps)-traces[1]
    zero = {k: 0, eps: 0}
    assert_sym_equal(equation.subs(zero), 0)
    assert_sym_equal(sp.diff(equation, eps).subs(zero), sp.sin(2*kap))
    assert_sym_equal(sp.diff(equation, k).subs(zero), 0)
    second = -sp.diff(equation, k, 2).subs(zero)/sp.diff(equation, eps).subs(zero)
    assert_sym_equal(second/2, sp.tan(kap)/4, "quadratic coefficient")
    assert_sym_equal(equation.subs(k, -k), equation, "even branch")
    # A distinct characteristic-polynomial check through second order.
    trial = 1-sp.I*sp.tan(kap)*k**2/4
    poly = trial**2-sp.trace(full_plus)*trial+full_plus.det()
    for order in range(3):
        assert_sym_equal(sp.diff(poly, k, order).subs(k, 0), 0)
    print("[PASS] 0<kappa<pi/2 fixed: uniform quasienergy = tan(kappa)*k^2/4 + O(k^4)")

    assert_sym_equal((1-traces[-1])/2, s**2*sp.sin(k/2)**2)
    assert_sym_equal((1-traces[1].subs(k, sp.pi+k))/2, s**2*sp.sin(k/2)**2)
    # v=|sin kap| in [0,1]; analytic signed branch near k=0.
    v = sp.symbols("v", nonnegative=True)
    signed_branch = 2*sp.asin(v*sp.sin(k/2))
    assert_sym_equal(sp.diff(signed_branch, k).subs(k, 0), v)
    assert_sym_equal(sp.diff(signed_branch, k, 2).subs(k, 0), 0)
    assert_sym_equal(sp.diff(signed_branch, k, 3).subs(k, 0)/6, v*(v*v-1)/24)
    assert_sym_equal(bloch_step(0, kap, -1), sp.eye(2))
    print("[PASS] opposite-sign node: omega=2 asin(|sin kappa| |sin(k/2)|), slope |sin kappa|")

    for sign in (1, -1):
        for angle in (0, sp.pi):
            assert_sym_equal(bloch_step(k, angle, sign), sp.eye(2))
        assert_sym_equal(bloch_step(k, sp.pi/2, sign),
                         sp.diag(sp.exp(-sp.I*k), sp.exp(sp.I*k)))
    print("[PASS] degenerate zero-coupling cases and exceptional full-SWAP endpoint")

    spacing, period = sp.symbols("a tau", positive=True)
    momentum = sp.symbols("p", real=True)
    omega = sp.Function("omega")
    physical = omega(2*spacing*momentum)/period
    expected = 2*spacing/period*sp.Subs(sp.diff(omega(k), k), k, 2*spacing*momentum)
    assert_sym_equal(sp.diff(physical, momentum), expected)
    print("[PASS] k=2*a*p: physical group speed = (2*a/tau)*domega/dk")
    print("\nVERDICT: full same-sign smooth branch quadratic for 0<kappa<pi/2; "
          "opposite-sign control linear in 1D. AUTHOR_CHECKED; metric interpretation open.")


if __name__ == "__main__":
    main()
