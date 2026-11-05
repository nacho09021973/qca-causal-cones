"""Exact checks of the user-supplied S19 trace proof (2026-11-05).

Run: python3 -B scripts/verify_hex_trace_s19.py
Contract: theory/HEX_TRACE_SCALAR_GATE.md.
No imports from the matrix certificate. SymPy only; no floating point,
solver search, external data, or assert statements that -O can disable.
The analytic implications of unitarity/averaging/rigidity are in the report.
"""
from collections import Counter

import sympy as s


CHECKS = []


def record(label, condition):
    ok = bool(condition)
    CHECKS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")


def zero(expr):
    return s.simplify(s.expand_trig(expr)) == 0


def rotate(h):
    a, b = h
    return -b, a + b


def reflect(h):
    a, b = h
    return a + b, -b


def orbit(h):
    result = set()
    for _ in range(6):
        result.update((h, reflect(h)))
        h = rotate(h)
    return result


def main():
    # h=(a*g1+b*g2)/2. Hexagon inequalities in lattice coordinates.
    support = {(a, b) for a in range(-2, 3) for b in range(-2, 3)
               if max(abs(a), abs(b), abs(a + b)) <= 2}
    rings = [orbit(h) for h in ((1, 0), (1, 1), (2, 0))]
    record("19 points; origin plus three disjoint six-point D6 orbits",
           len(support) == 19 and all(len(o) == 6 for o in rings)
           and set.union({(0, 0)}, *rings) == support
           and sum(len(o) for o in rings) == len(set.union(*rings)))
    record("D6 preserves support", all(rotate(h) in support and reflect(h) in support
                                      for h in support))
    record("maximum physical radius is 1",
           max(s.Rational(a*a + a*b + b*b, 4) for a, b in support) == 1)

    p, q, t = s.symbols('p q t', real=True)
    a0, a1, a2, a3 = s.symbols('a0 a1 a2 a3', real=True)
    S = [2*(s.cos(p)+s.cos(q)+s.cos(p-q)),
         2*(s.cos(p+q)+s.cos(2*p-q)+s.cos(p-2*q)),
         2*(s.cos(2*p)+s.cos(2*q)+s.cos(2*(p-q)))]
    record("orbit sums equal the three stated cosine sums",
           all(zero(sum(s.cos(a*p+b*q) for a, b in ring)-expr)
               for ring, expr in zip(rings, S)))
    f = a0 + sum(a*expr for a, expr in zip((a1, a2, a3), S))
    # Along p=0, collect exact Fourier coefficients from the actual points.
    layer = Counter({0: a0})
    for coefficient, ring in zip((a1, a2, a3), rings):
        for _, b in ring:
            layer[b] += coefficient
    equations = [layer[0], layer[1], layer[2]-s.Rational(1, 2)]
    solutions = s.solve(equations, (a0, a2, a3), dict=True)
    expected = {a0: -s.Rational(1, 2)-3*a1, a2: -a1,
                a3: (1+2*a1)/4}
    record("normal-line coefficients leave exactly the stated one-parameter family",
           solutions == [expected])
    reduced = f.subs(expected)
    record("family has f(0)=1 and all three normal-line cosines",
           zero(reduced.subs({p: 0, q: 0})-1)
           and zero(reduced.subs({p: 0, q: t})-s.cos(2*t))
           and zero(reduced.subs({p: t, q: 0})-s.cos(2*t))
           and zero(reduced.subs({p: t, q: t})-s.cos(2*t)))
    P, Q = {p: s.pi/3, q: 2*s.pi/3}, {p: 2*s.pi/3, q: 4*s.pi/3}
    record("P and Q orbit values (second direct evaluation)",
           [s.simplify(expr.subs(P)) for expr in S] == [1, -2, -3]
           and [s.simplify(expr.subs(Q)) for expr in S] == [-3, 6, -3])
    fP, fQ = s.simplify(reduced.subs(P)), s.simplify(reduced.subs(Q))
    record("P and Q affine values", zero(fP+s.Rational(5, 4)+3*a1/2)
           and zero(fQ+s.Rational(5, 4)+27*a1/2))
    record("bounds force a1=-1/6",
           s.solve_univariate_inequality(fP >= -1, a1).as_set()
           == s.Interval(-s.oo, -s.Rational(1, 6))
           and s.solve_univariate_inequality(fQ <= 1, a1).as_set()
           == s.Interval(-s.Rational(1, 6), s.oo))
    candidate = reduced.subs(a1, -s.Rational(1, 6))
    record("unique candidate is (S2+S3-S1)/6",
           zero(candidate-(S[1]+S[2]-S[0])/6))
    C = {p: 3*s.pi/5, q: 3*s.pi/10}
    value = (2-s.sqrt(5)-s.sqrt(20+8*s.sqrt(5)))/6
    record("C exact radical value", zero(candidate.subs(C)-value))
    record("C value is strictly below -1 by exact positive radicals",
           s.sqrt(5) > 2 and 20+8*s.sqrt(5) > 36
           and s.sqrt(20+8*s.sqrt(5)) > 6 and value < -1)
    # Independent contradiction point with simpler rational cosine values.
    # q=p/2, cos(q)=3/5. No angle simplification or nested radical is required.
    x = s.symbols('x', real=True)
    slice_polynomial = (2*(2*s.chebyshevt(3, x)+1)
                        +2*(s.chebyshevt(4, x)+2*s.chebyshevt(2, x))
                        -2*(s.chebyshevt(2, x)+2*x))/6
    record("second route: q=p/2 has polynomial expression in cos(q)",
           zero(candidate.subs({p: 2*t, q: t})-slice_polynomial.subs(x, s.cos(t))))
    record("second contradiction: cos(q)=3/5 gives -1997/1875 < -1",
           s.expand(slice_polynomial).subs(x, s.Rational(3, 5)) == -s.Rational(1997, 1875)
           and -s.Rational(1997, 1875) < -1)
    print(f"{sum(CHECKS)}/{len(CHECKS)} exact checks passed")
    return 0 if all(CHECKS) else 1


if __name__ == '__main__':
    raise SystemExit(main())
