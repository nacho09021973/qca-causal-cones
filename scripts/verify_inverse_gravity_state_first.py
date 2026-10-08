#!/usr/bin/env python3
"""Exact auxiliary controls for the state-first architecture preflight.

Contract: theory/INVERSE_GRAVITY_STATE_FIRST_GATE.md.
These matrices are not a spatial QCA or an emergent-gravity calculation.
"""

import sympy as sp


def reduced_left(vector, left_dim, right_dim):
    """Partial trace in the declared left-major product basis."""
    return sp.Matrix(left_dim, left_dim, lambda i, j: sum(
        vector[i * right_dim + b] * sp.conjugate(vector[j * right_dim + b])
        for b in range(right_dim)))


def zero(matrix):
    return all(sp.simplify(value) == 0 for value in matrix)


def schmidt_controls():
    identity = sp.eye(2)
    z = sp.diag(1, -1)
    d = sp.Matrix(2, 2, sp.symbols("d0:4", complex=True))
    basis = []
    for a in range(2):
        for b in range(2):
            e = sp.zeros(2)
            e[a, b] = 1
            basis.append(e)
    for p, expected_rank in ((sp.Rational(1, 3), 4), (sp.S.Zero, 2)):
        omega = sp.Matrix([sp.sqrt(p), 0, 0, sp.sqrt(1-p)])
        rho = reduced_left(omega, 2, 2)
        assert rho == sp.diag(p, 1-p)
        action = sp.Matrix.hstack(*[
            sp.kronecker_product(e, identity) * omega for e in basis])
        assert action.rank() == expected_rank
        if p != 0:
            assert sp.simplify(action.det() - p*(1-p)) == 0
        vector = sp.kronecker_product(d, identity) * omega
        assert sp.simplify((vector.adjoint()*vector)[0] - sp.trace(rho*d.adjoint()*d)) == 0
        assert zero(sp.kronecker_product(z, z)*omega - omega)
        if p == 0:
            assert zero(sp.kronecker_product(-z, identity)*omega - omega)
        else:
            # One Z changes the ray although their full product fixes it.
            assert sp.Matrix.hstack(omega, sp.kronecker_product(z, identity)*omega).rank() == 2
        print(f"PASS Schmidt p={p}: local action rank={expected_rank}; norm identity; full product fixes state")


def common_kernel_controls():
    t = sp.symbols("t", positive=True)
    c, s = (1-t**2)/(1+t**2), 2*t/(1+t**2)
    p = sp.diag(0, 1, 0)
    v = sp.Matrix([0, c, s])
    q = v*v.T
    k = p+q
    u = (sp.eye(3)-2*q)*(sp.eye(3)-2*p)
    omega = sp.Matrix([1, 0, 0])
    assert zero(q*q-q) and zero(p*p-p)
    assert zero(k*omega) and zero(u*omega-omega)
    assert zero(u.adjoint()*u-sp.eye(3))
    e = sp.symbols("e", real=True)
    assert sp.simplify(k[1:, 1:].charpoly(e).as_expr() - (e-(1-c))*(e-(1+c))) == 0
    assert sp.simplify(sp.trace(u[1:, 1:])-2*(2*c*c-1)) == 0
    assert sp.simplify(u[1:, 1:].det()-1) == 0
    delta = (u.adjoint()*k*u-k).subs(t, sp.Rational(1, 2)).applyfunc(sp.simplify)
    defect_squared = sp.trace(delta.adjoint()*delta)
    assert defect_squared > 0
    # 0<t<1: c=cos(2 atan t); excited phases are +/-4 atan t.
    gap = 1-c
    phase = 4*sp.atan(t)
    assert sp.limit(phase**2/gap, t, 0, dir="+") == 8
    print(f"PASS common kernel: fixed vacuum, unitary tick, ||U†KU-K||_HS^2={defect_squared} at t=1/2")
    print("PASS phase/gap distinction: phase^2/gap -> 8; auxiliary parameter limit only")


def band_controls():
    momenta = sp.symbols("kx ky kz", real=True)
    laplacian = 2*sum(1-sp.cos(k) for k in momenta)
    origin = dict.fromkeys(momenta, 0)
    assert laplacian.subs(origin) == 0
    assert all(sp.diff(laplacian, k).subs(origin) == 0 for k in momenta)
    assert sp.hessian(laplacian, momenta).subs(origin) == 2*sp.eye(3)
    k = momenta[0]
    signed = sp.sin(k)*sp.diag(1, -1)
    assert signed.subs(k, sp.pi/6) == sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2))
    assert zero(signed*signed-sp.sin(k)**2*sp.eye(2))
    print("PASS bands: positive Laplacian has zero slope and quadratic Hessian; signed linear control is not positive")


def main():
    print(f"SymPy {sp.__version__}; exact arithmetic; auxiliary controls only")
    schmidt_controls()
    common_kernel_controls()
    band_controls()
    print("VERDICT: STATE_FIRST_AUXILIARY_CONTROLS_PASS")
    print("New QCA rule, physical IR state, spin-2 spectrum and gravity: NOT_COMPUTED")


if __name__ == "__main__":
    main()
