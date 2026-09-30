"""W9 repaired algebraic gauge-variation check (2026-09-30, D1).

Explicit symmetric h,T and gauge parameter xi; conserved-shell index split.
No division by a momentum component, no derivation of Weyl stress conservation,
no local-Lorentz Ward identity, and no microscopic W6 source matching.
Fourier integration by parts is an analytic convention, not a separate test.
"""

import sympy as sp


def symmetric(name):
    entries = {(i, j): sp.Symbol(f'{name}{i}{j}')
               for i in range(4) for j in range(i, 4)}
    return sp.Matrix(4, 4, lambda i, j: entries[min(i, j), max(i, j)])


def main():
    lam, eps = sp.symbols('lambda epsilon')
    k = sp.Matrix(sp.symbols('k0:4'))
    xi = sp.Matrix(sp.symbols('xi0:4'))
    h, T = symmetric('h'), symmetric('T')
    delta_h = sp.I * (k * xi.T + xi * k.T)

    def coupling(metric):
        return lam * sum(metric[i, j] * T[i, j]
                         for i in range(4) for j in range(4)) / 2

    variation = sp.expand(sp.diff(coupling(h + eps * delta_h), eps))
    divergence = T * k
    assert sp.expand(variation - sp.I * lam * xi.dot(divergence)) == 0
    # h and xi carry k, T carries -k. Moving a derivative to T gives -i k;
    # this convention is not an independent assertion of integration by parts.
    print('[PASS] symmetric h,T: full coupling variation and factor 1/2 checked')

    spatial = lam * sum(delta_h[i, j] * T[i, j]
                        for i in range(1, 4) for j in range(1, 4)) / 2
    residual = -sp.I * lam * k[0] * sum(xi[j] * T[0, j] for j in range(1, 4))
    conservation_term = sp.I * lam * sum(xi[j] * divergence[j] for j in range(1, 4))
    assert sp.expand(spatial - residual - conservation_term) == 0
    print('[PASS] computed spatial variation minus temporal residual equals the conservation term')

    # Independent polynomial conserved-stress witness, including k0=0 without
    # division. This is an algebraic test family, not a constructed Weyl stress.
    v = sp.Matrix([k[1], -k[0] + k[2], -k[1] + k[3], -k[2]])
    conserved_T = v * v.T
    assert (conserved_T * k).applyfunc(sp.expand) == sp.zeros(4, 1)
    on_shell = {T[i, j]: conserved_T[i, j] for i in range(4) for j in range(i, 4)}
    full_on_shell = sp.expand(variation.subs(on_shell, simultaneous=True))
    spatial_on_shell = sp.expand(spatial.subs(on_shell, simultaneous=True))
    assert full_on_shell == 0
    assert sp.expand(spatial_on_shell.subs(k[0], 0)) == 0
    moving = {k[0]: 1, k[1]: 1, k[2]: 0, k[3]: 0,
              xi[0]: 0, xi[1]: 1, xi[2]: 0, xi[3]: 0}
    assert sp.expand(spatial_on_shell.subs(moving) - sp.I * lam) == 0
    print('[PASS] conserved-stress witness: full variation zero; spatial variation static zero, moving nonzero')
    print('VERDICT: algebraic on-shell O(lambda) consistency only; conservation and microscopic matching are inputs.')


if __name__ == '__main__':
    main()
