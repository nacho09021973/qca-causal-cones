#!/usr/bin/env python3
"""Exact algebra for THIRRING_BOUND_SCALING_LIMIT_GATE.

No floats and no parameter sweep. Analytic square-root branches, the
implicit-function theorem, and the bound-state identification require
the accompanying written proof.
"""

import sympy as s


def verify(name, residual):
    value = s.simplify(s.expand_complex(residual))
    if value != 0:
        raise AssertionError(f"{name}: nonzero residual {value}")
    print(f"PASS {name}")


def main():
    mu, z = s.symbols("mu z")
    Q = s.symbols("Q", real=True)
    x = Q / 2
    a = s.sqrt(Q**2 + 2) / 2
    zeta = x - s.I * a
    w = a - s.I * x
    X = w - zeta

    # The exact bound equation is Re X = Im X, with
    # X = sin(omega(z))-nu*sin(z) and nu=sqrt(1-mu**2).
    exact_radicand = 1 - (1 - mu**2) * s.cos(mu * z) ** 2
    exact_sine = s.sqrt(1 - mu**2) * s.sin(mu * z)
    verify("radicand leading mu^2 coefficient",
           s.diff(exact_radicand, mu, 2).subs(mu, 0) / 2 - (1 + z**2))
    verify("nu sine leading mu coefficient",
           s.diff(exact_sine, mu).subs(mu, 0) - z)

    verify("a^2-x^2=1/2", a**2 - x**2 - s.Rational(1, 2))
    verify("physical positive-root square", w**2 - 1 - zeta**2)
    verify("leading bound condition Re X=Im X", s.re(X) - s.im(X))
    verify("leading bound amplitude", X - (a - x) * (1 + s.I))

    # Differentiate F(r)=Re X(x+i*r)-Im X(x+i*r);
    # dX/dr=i*(zeta/sqrt(1+zeta**2)-1)=-i*X/w.
    aa, xx = s.symbols("a x", real=True)
    leading_X = (aa - xx) * (1 + s.I)
    leading_w = aa - s.I * xx
    derivative = -s.I * leading_X / leading_w
    target_derivative = 2 * aa * (aa - xx) / (aa**2 + xx**2)
    verify("nondegenerate implicit derivative",
           s.re(derivative) - s.im(derivative) - target_derivative)

    # Given Q real, a>abs(x), so r=-a<0 and F_r>0.
    energy = 2 * a
    verify("full scaling invariant D(Q)=2", energy**2 - Q**2 - 2)
    verify("zero momentum rest energy sqrt(2)", energy.subs(Q, 0) - s.sqrt(2))
    print("RESULT e(Q)=sqrt(Q^2+2), D(Q)=2 for all real fixed Q")
    print("SCOPE: finite exact identities only; see proof for branch and limits")


if __name__ == "__main__":
    main()
