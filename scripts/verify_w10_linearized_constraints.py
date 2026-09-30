"""W10 B1/B2/B3 repair certificate, 2026-09-30.

Run: python3 -B scripts/verify_w10_linearized_constraints.py
Frozen target: linearized Einstein continuum, eta=(-,+,+,+), g=eta+h.
S_g=-1/2 integral h_(mu nu) G_lin^(mu nu)(h), S_int=lambda/2 integral h T.
Formal commuting derivative symbols verify the quadratic variational operator,
constraint coefficients, Bianchi identity and a transverse-traceless limit.
This is not a lattice Gu-Wen L-model calculation or a coupled Ward identity.
"""

import sympy as sp


def main():
    eta = sp.diag(-1, 1, 1, 1)
    d = sp.Matrix(sp.symbols('d0:4'))
    dup = eta * d
    hs = {(i, j): sp.Symbol(f'h{i}{j}') for i in range(4) for j in range(i, 4)}
    h = sp.Matrix(4, 4, lambda i, j: hs[min(i, j), max(i, j)])
    ts = {(i, j): sp.Symbol(f'T{i}{j}') for i in range(4) for j in range(i, 4)}
    T = sp.Matrix(4, 4, lambda i, j: ts[min(i, j), max(i, j)])  # upper indices
    lam = sp.Symbol('lambda')
    box = d.dot(dup)
    trace = sp.trace(eta * h)
    div = h * dup
    scalar = dup.dot(div) - box * trace
    G = (d * div.T + div * d.T - box * h - d * d.T * trace - eta * scalar) / 2
    Gup = (eta * G * eta).applyfunc(sp.expand)
    assert (Gup * d).applyfunc(sp.expand) == sp.zeros(4, 1)
    xi = sp.Matrix(sp.symbols('xi0:4'))
    gauge = d * xi.T + xi * d.T
    assert Gup.subs({hs[i, j]: gauge[i, j] for i, j in hs}, simultaneous=True).applyfunc(sp.expand) == sp.zeros(4)
    print('[PASS] linearized Einstein operator: Bianchi and gauge identities for arbitrary momentum')

    # Two derivatives make the formal adjoint even under d -> -d. Differentiating
    # this quadratic form checks self-adjointness and off-diagonal multiplicity.
    L = -sum(h[i, j] * Gup[i, j] for i in range(4) for j in range(4)) / 2
    L += lam * sum(h[i, j] * T[i, j] for i in range(4) for j in range(4)) / 2
    for (i, j), field in hs.items():
        weight = 1 if i == j else 2
        assert sp.expand(sp.diff(L, field) - weight * (-Gup[i, j] + lam * T[i, j] / 2)) == 0
    print('[PASS] all ten variations: G^mu nu=lambda*T^mu nu/2; lapse/shift factors fixed')

    spatial_trace = sum(h[i, i] for i in range(1, 4))
    lap = sum(d[i]**2 for i in range(1, 4))
    C0 = sum(d[i] * d[j] * h[i, j] for i in range(1, 4) for j in range(1, 4)) - lap * spatial_trace
    assert sp.expand(2 * Gup[0, 0] - C0) == 0
    for i in range(1, 4):
        Ci = -sum(d[j] * d[0] * h[i, j] for j in range(1, 4)) + d[i] * d[0] * spatial_trace
        Ci += lap * h[0, i] - d[i] * sum(d[j] * h[0, j] for j in range(1, 4))
        assert sp.expand(2 * Gup[0, i] - Ci) == 0
    print('[PASS] scalar/vector constraints agree with component formulae; no second time derivative')

    # Independent TT limit: only h12=h21 survives, propagation along x3.
    tt = {field: 0 for pair, field in hs.items() if pair != (1, 2)}
    wave = Gup[1, 2].subs(tt).subs({d[1]: 0, d[2]: 0})
    assert sp.expand(wave - (d[0]**2 - d[3]**2) * h[1, 2] / 2) == 0
    print('[PASS] TT limit has the wave operator, not cubic lattice dispersion')
    print('VERDICT: continuum test-source consistency at O(lambda); microscopic and reciprocal completion OPEN.')


if __name__ == '__main__':
    main()
