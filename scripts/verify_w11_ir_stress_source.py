"""W11 A1/A2 repair certificate (2026-09-30).

Run: python3 scripts/verify_w11_ir_stress_source.py
Original first-order checker: git show 97592a4:scripts/verify_w11_ir_stress_source.py
Uses the original CJWW (5.15) symbol, extracts its real-space hopping matrices,
and checks conservation both in Bloch space and by real-space convolution.
Scope: free walk, integrated charges, all eight nodes; no q != 0 Belinfante
stress kernel, interacting constraint identity, or Floquet logarithm no-go.
"""

from itertools import product

import sympy as sp

from verify_directional_saturation import PAULI, P1, P2, P3, Z, laurent, walk2

PS = (P1, P2, P3)
I2 = sp.eye(2)
ZERO = sp.zeros(2)


def equal(left, right):
    assert all(sp.simplify(laurent(e)) == 0 for e in left - right)


def hopping(symbol):
    """symbol = sum_r A_r exp(i p.r); (A psi)_x = sum_r A_r psi_(x+r)."""
    out = {}
    for row in range(2):
        for col in range(2):
            poly = sp.Poly(sp.expand(laurent(symbol[row, col]) * sp.prod(Z)), *Z)
            for mono, coeff in poly.terms():
                if coeff != 0:
                    r = tuple(int(m) - 1 for m in mono)
                    out.setdefault(r, sp.zeros(2))[row, col] = coeff
    return out


def adjoint(hops):
    return {tuple(-x for x in r): a.H for r, a in hops.items()}


def convolution(left, right):
    out = {}
    for r, a in left.items():
        for s, b in right.items():
            rs = tuple(x + y for x, y in zip(r, s))
            out[rs] = out.get(rs, ZERO) + a * b
    return {r: a.applyfunc(sp.simplify) for r, a in out.items() if a != ZERO}


def equal_hops(left, right):
    for r in left.keys() | right.keys():
        assert (left.get(r, ZERO) - right.get(r, ZERO)).applyfunc(sp.simplify) == ZERO


def symbol(hops):
    return sum((a * sp.exp(sp.I * sum(p * x for p, x in zip(PS, r)))
                for r, a in hops.items()), sp.zeros(2))


def sig(v):
    return sum((x * s for x, s in zip(v, PAULI)), sp.zeros(2))


def main():
    W = walk2()
    equal(W.H * W, I2)
    assert sp.simplify(W.det()) == 1
    # Exact SU(2) decomposition, derived independently from the matrix entries.
    a0 = sp.prod(sp.cos(p) for p in PS)
    a = sp.Matrix([sp.sin(P1), -sp.cos(P1) * sp.sin(P2),
                   sp.cos(P1) * sp.cos(P2) * sp.sin(P3)])
    equal(W, a0 * I2 + sp.I * sig(a))
    assert sp.trigsimp(a.dot(a) + a0**2 - 1) == 0

    U = hopping(W)
    Ud = adjoint(U)
    Khops = {r: sp.I * (U.get(r, ZERO) - Ud.get(r, ZERO)) / 2
             for r in U.keys() | Ud.keys()}
    K = symbol(Khops)
    equal(K, sp.I * (W - W.H) / 2)
    equal(K, -sig(a))
    equal(K.H, K)
    equal(K * W, W * K)
    equal_hops(Khops, adjoint(Khops))
    equal_hops(convolution(Ud, U), {(0, 0, 0): I2})
    equal_hops(convolution(convolution(Ud, Khops), U), Khops)
    assert len(U) == 14
    assert max(max(abs(x) for x in r) for r in Khops) == 1
    print('[PASS] K built from the 14 CJWW hoppings: Hermitian, range <= 1 per coordinate', flush=True)
    print('[PASS] [K,W]=0 and U^dag K U=K, also by real-space convolution', flush=True)

    # W(p_star+k)=s[I+i sigma.E k+O(k^2)]; H_shift=-sigma.E k+...
    print('node/pi | W sign | diag(E), normalized by W sign | det(E) | chirality(H_shift)')
    plus_chiralities = []
    for bits in product((0, 1), repeat=3):
        at = dict(zip(PS, (b * sp.pi for b in bits)))
        signs = [(-1)**b for b in bits]
        s = sp.prod(signs)
        equal(W.subs(at), s * I2)
        E = sp.diag(signs[1] * signs[2], -signs[2], 1)
        shifted = {p: p + b * sp.pi for p, b in zip(PS, bits)}
        # Exact recentering, not just node derivatives: all +I neighborhoods
        # share the scalar dispersion and odd vector Taylor order.
        equal(s * W.subs(shifted, simultaneous=True),
              a0 * I2 + sp.I * sig(E * sp.diag(1, -1, 1) * a))
        for i, p in enumerate(PS):
            equal(sp.diff(W, p).subs(at), s * sp.I * sig(E[:, i]))
            equal(sp.diff(K, p).subs(at), -s * sig(E[:, i]))
        equal(K.subs(at), ZERO)
        chirality = (-E).det()
        if s == 1:
            plus_chiralities.append(chirality)
        print(f'{bits} | {int(s):+} | {tuple(E.diagonal())} | {int(E.det()):+} | {int(chirality):+}', flush=True)
    assert sorted(plus_chiralities) == [-1, -1, 1, 1]
    print('[PASS] four zero-quasienergy species, net chirality zero; four pi nodes', flush=True)
    # Completeness: W=+-I implies |a0|=1. Each |cos p_i|<=1, so all p_i=0 or pi.

    # Build the OLD H_IR and pi_i from their real-space bond coefficients.
    E0 = sp.diag(1, -1, 1)
    old_hops = {}
    for i in range(3):
        e = tuple(int(j == i) for j in range(3))
        minus_e = tuple(-x for x in e)
        M = sig(E0[:, i])
        old_hops[e], old_hops[minus_e] = sp.I * M / 2, -sp.I * M / 2
        pi_hops = {e: -sp.I * I2 / 2, minus_e: sp.I * I2 / 2}
        Pi = symbol(pi_hops)
        equal(Pi, sp.sin(PS[i]) * I2)
        equal_hops(convolution(convolution(Ud, pi_hops), U), pi_hops)
    Hir = symbol(old_hops)
    equal(Hir, -sig(E0 * sp.Matrix([sp.sin(p) for p in PS])))
    print('[PASS] old bond pi_i has exactly conserved integrated charge (not a Belinfante kernel)', flush=True)

    t = sp.symbols('t', real=True)
    v = sp.Matrix(sp.symbols('v1 v2 v3', real=True))
    ray = dict(zip(PS, t * v))

    def jet(expr, order):
        return sp.expand(sp.series(expr.subs(ray), t, 0, order).removeO())

    # H_eff=-(asin(|a|)/|a|)a.sigma near +I; ratio=1+|a|^2/6+O(|a|^4).
    K3 = (-a).applyfunc(lambda e: jet(e, 4))
    Heff3 = (-(1 + a.dot(a) / 6) * a).applyfunc(lambda e: jet(e, 4))
    Hir3 = (-E0 * sp.Matrix([sp.sin(p) for p in PS])).applyfunc(lambda e: jet(e, 4))
    for e in Heff3 - Hir3:
        assert e.coeff(t, 0) == e.coeff(t, 1) == e.coeff(t, 2) == 0
    expected = E0 * v * v.dot(v) * t**3 / 6
    assert (K3 - Heff3 - expected).applyfunc(sp.simplify) == sp.zeros(3, 1)
    comm4 = (Hir * W - W * Hir).applyfunc(lambda e: jet(e, 5))
    assert all(e.coeff(t, n) == 0 for e in comm4 for n in range(4))
    assert any(e.coeff(t, 4).subs(dict(zip(v, (1, 2, 3)))) != 0 for e in comm4)
    print('[PASS] arbitrary-direction jets: K-H_eff=O(|p|^3); old H_IR commutator has nonzero quartic term', flush=True)

    # Independent exact axis witness: W=exp(i p3 sigma3), H_eff=-p3 sigma3.
    equal(W.subs({P1: 0, P2: 0}), sp.diag(sp.exp(sp.I * P3), sp.exp(-sp.I * P3)))
    equal(K.subs({P1: 0, P2: 0}), -sp.sin(P3) * PAULI[2])
    assert sp.limit((P3 - sp.sin(P3)) / P3**3, P3, 0) == sp.Rational(1, 6)
    print('[PASS] exact p3-axis check: cubic energy error coefficient 1/6')
    print('VERDICT: A1/A2 checks pass for free integrated charges; full local stress and coupled gate OPEN.')


if __name__ == '__main__':
    main()
