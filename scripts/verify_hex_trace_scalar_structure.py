"""Exact algebra for the aligned-hexagon scalar reduction, 2026-11-05.

Run: python3 -B scripts/verify_hex_trace_scalar_structure.py
Contract: theory/HEX_TRACE_SCALAR_GATE.md. This checks Laurent identities
and the Newton polygon of Delta, not universal scalar feasibility or the
analytic divisibility theorem (proved in the companion report).
"""
import sympy as s


def main():
    z, w, a = s.symbols('z w a', nonzero=True)
    checks = []

    def record(name, ok):
        checks.append(bool(ok))
        print(f"[{'PASS' if checks[-1] else 'FAIL'}] {name}")

    def c(i, j):
        return (z**i*w**j + z**(-i)*w**(-j))/2

    def equal(x, y):
        return s.cancel(x-y) == 0

    S1 = 2*(c(1, 0)+c(0, 1)+c(1, -1))
    S2 = 2*(c(1, 1)+c(2, -1)+c(1, -2))
    S3 = 2*(c(2, 0)+c(0, 2)+c(2, -2))
    delta = (1-c(1, 0))*(1-c(0, 1))*(1-c(1, -1))/8
    factor = -(z-1)**2*(w-1)**2*(z-w)**2/(64*z**2*w**2)
    record("Delta exact Laurent factorization", equal(delta, factor))
    record("Delta normal-line double factors", all(s.diff(s.cancel(delta), v, j).subs(v, val) == 0
           for v, val in ((z, 1), (w, 1)) for j in (0, 1))
           and equal(delta.subs(z, w), 0)
           and equal(s.diff(delta, z).subs(z, w), 0))
    # Reciprocal-coordinate maps induced by a 60-degree rotation and a reflection.
    record("Delta is real/even and D6 invariant",
           equal(delta.subs({z: 1/z, w: 1/w}, simultaneous=True), delta)
           and equal(delta.subs({z: w, w: w/z}, simultaneous=True), delta)
           and equal(delta.subs({z: 1/z, w: w/z}, simultaneous=True), delta))
    poly = s.Poly(s.expand(s.cancel(delta*z**2*w**2)), z, w)
    support = {(i-2, j-2) for (i, j), coeff in poly.terms() if coeff != 0}
    vertices = {(2, 0), (0, 2), (-2, 2), (-2, 0), (0, -2), (2, -2)}
    record("Delta Newton polygon is exactly the radius-two hexagon",
           vertices <= support and all(max(abs(i), abs(j), abs(i+j)) <= 2 for i, j in support))
    f0 = -s.Rational(1, 2)+S3/4
    family = -s.Rational(1, 2)-3*a+a*S1-a*S2+(1+2*a)*S3/4
    record("S19 family equals f0 - 32*a1*Delta", equal(family, f0-32*a*delta))
    record("S19 forced candidate has residual coefficient 16/3",
           equal(family.subs(a, -s.Rational(1, 6)), f0+s.Rational(16, 3)*delta))
    print(f"{sum(checks)}/{len(checks)} exact checks passed")
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
