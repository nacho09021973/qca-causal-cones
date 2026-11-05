"""Exact bounded scalar test for m=3; no floating point or external solver.

Run: python3 -B scripts/verify_hex_trace_m3.py
Contract: theory/HEX_TRACE_M3_GATE.md. All point-generation and elimination
code is permanent here. Point feasibility alone is never a global witness.
"""
from fractions import Fraction as F
import json
import time

import sympy as s


def multiply(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def power(z, n):
    if n < 0:
        return power((z[0], -z[1]), -n)
    result = (F(1), F(0))
    for _ in range(n):
        result = multiply(result, z)
    return result


def phase(t):
    if t is None:
        return (F(-1), F(0))
    return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def point_values(z, w):
    zw = multiply(z, (w[0], -w[1]))
    base = (power(z, 3)[0]+power(w, 3)[0]+power(zw, 3)[0]-1)/2
    delta = (1-z[0])*(1-w[0])*(1-zw[0])/8
    S1 = 2*(z[0]+w[0]+zw[0])
    return base, delta, S1


def restrictions():
    out = []
    # Rational points of the two-torus: cos and sin from stereographic t.
    ts = [F(0), F(1, 2), F(-1, 2), F(1), F(-1), F(2), F(-2), None]
    for t in ts:
        for u in ts:
            z, w = phase(t), phase(u)
            base, delta, S1 = point_values(z, w)
            if delta:
                data = {'point': 'rational_torus', 'z': z, 'w': w,
                        'base': base, 'delta': delta, 'S1': S1}
                out.append(dict(data, A=F(1), B=S1, C=(1-base)/delta, bound='upper'))
                out.append(dict(data, A=F(-1), B=-S1, C=(1+base)/delta, bound='lower'))
    # Vertex-axis slice p=2q, x=cos(q); every x in [-1,1] is realizable.
    x = s.symbols('x')
    base_poly = s.Poly((s.chebyshevt(6, x)+2*s.chebyshevt(3, x)-1)/2, x)
    for j in range(-16, 17):
        v = F(j, 16)
        base = F(base_poly.eval(s.Rational(v.numerator, v.denominator)))
        delta = (1-v*v)*(1-v)**2/4
        S1 = 4*v*v+4*v-2
        if delta:
            data = {'point': 'p=2q', 'cos_q': v, 'base': base, 'delta': delta, 'S1': S1}
            out.append(dict(data, A=F(1), B=S1, C=(1-base)/delta, bound='upper'))
            out.append(dict(data, A=F(-1), B=-S1, C=(1+base)/delta, bound='lower'))
    return out


def eliminate(rows):
    upper = [i for i, r in enumerate(rows) if r['A'] == 1]
    lower = [i for i, r in enumerate(rows) if r['A'] == -1]
    lo, hi = None, None
    for i in upper:
        for j in lower:
            B, C = rows[i]['B']+rows[j]['B'], rows[i]['C']+rows[j]['C']
            if B == 0:
                if C < 0:
                    return [(i, F(1)), (j, F(1))], None
                continue
            bound = C/B
            if B > 0 and (hi is None or bound < hi[0]):
                hi = bound, i, j, B
            if B < 0 and (lo is None or bound > lo[0]):
                lo = bound, i, j, B
    if lo is not None and hi is not None and lo[0] > hi[0]:
        return [(hi[1], 1/hi[3]), (hi[2], 1/hi[3]),
                (lo[1], -1/lo[3]), (lo[2], -1/lo[3])], None
    beta = (lo[0]+hi[0])/2 if lo and hi else (lo[0] if lo else (hi[0] if hi else F(0)))
    alpha_lo = max(-rows[j]['C']+rows[j]['B']*beta for j in lower)
    alpha_hi = min(rows[i]['C']-rows[i]['B']*beta for i in upper)
    return None, (F(alpha_lo+alpha_hi, 2), beta)


def recheck_point(row):
    """Second evaluation via Laurent characters, separate from tuple powers."""
    z, w = s.symbols('z w', nonzero=True)
    def cosine(i, j):
        return (z**i*w**j+z**(-i)*w**(-j))/2
    base = (cosine(3, 0)+cosine(0, 3)+cosine(3, -3)-1)/2
    delta = (1-cosine(1, 0))*(1-cosine(0, 1))*(1-cosine(1, -1))/8
    S1 = 2*(cosine(1, 0)+cosine(0, 1)+cosine(1, -1))
    if row['point'] == 'rational_torus':
        zz = s.Rational(row['z'][0])+s.I*s.Rational(row['z'][1])
        ww = s.Rational(row['w'][0])+s.I*s.Rational(row['w'][1])
    else:
        v = s.Rational(row['cos_q'])
        ww = v+s.I*s.sqrt(1-v*v)
        zz = s.expand(ww**2)
    return all(s.simplify(expr.subs({z: zz, w: ww})-s.Rational(row[key])) == 0
               for expr, key in ((base, 'base'), (delta, 'delta'), (S1, 'S1')))


def main():
    start = time.monotonic()
    rows = restrictions()
    checks = []
    def record(label, condition):
        checks.append(bool(condition))
        print(f"[{'PASS' if checks[-1] else 'FAIL'}] {label}")
    support = {(i, j) for i in range(-3, 4) for j in range(-3, 4)
               if max(abs(i), abs(j), abs(i+j)) <= 3}
    residual = {(i, j) for i in range(-1, 2) for j in range(-1, 2)
                if max(abs(i), abs(j), abs(i+j)) <= 1}
    record('support count: 37 points; residual support: origin plus six-point orbit',
           len(support) == 37 and len(residual) == 7)
    record('point budget <=256 and every retained Delta is strictly positive',
           0 < len(rows) <= 256 and all(r['delta'] > 0 for r in rows))
    certificate, candidate = eliminate(rows)
    elapsed = time.monotonic()-start
    record('exact elimination completed within 300 s', elapsed <= 300)
    print(f'point inequalities: {len(rows)}; elimination seconds: {elapsed:.6f}')
    if certificate is not None:
        record('certificate point evaluations checked by independent Laurent substitution',
               all(recheck_point(rows[i]) for i, _ in certificate))
        weights = [w for _, w in certificate]
        A = sum(w*rows[i]['A'] for i, w in certificate)
        B = sum(w*rows[i]['B'] for i, w in certificate)
        C = sum(w*rows[i]['C'] for i, w in certificate)
        record('nonnegative exact weights yield 0 <= a strictly negative rational',
               all(w >= 0 for w in weights) and A == 0 and B == 0 and C < 0)
        print('CERTIFICATE '+json.dumps([{'weight': str(w),
              'restriction': {k: [str(vv) for vv in v] if isinstance(v, tuple) else str(v)
                              for k, v in rows[i].items()}} for i, w in certificate], indent=2))
        print(f'contradiction: 0 <= {C}')
        print('OUTCOME: SCALAR_INFEASIBLE_M3 (PRELIMINARY, independently unreviewed)')
    else:
        alpha, beta = candidate
        record('finite point candidate satisfies every retained restriction',
               all(r['A']*alpha+r['B']*beta <= r['C'] for r in rows))
        print(f'FINITE_POINTS_ONLY alpha={alpha}, beta={beta}; not a global witness')
        print('OUTCOME: OPEN_AFTER_FINITE_M3_RESTRICTIONS')
    print(f'{sum(checks)}/{len(checks)} exact checks passed')
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
