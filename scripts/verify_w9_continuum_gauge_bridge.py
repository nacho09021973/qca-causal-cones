"""W9 repaired algebraic gauge-variation check (2026-09-30, D1).

Explicit symmetric h,T and gauge parameter xi; Fourier integration by parts.
No division by a momentum component, no derivation of Weyl stress conservation,
no local-Lorentz Ward identity, and no microscopic W6 source matching.
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
    # h and xi carry k, T carries -k. The derivative on T is therefore -i k.
    after_ibp = -lam * xi.dot(-sp.I * divergence)
    assert sp.expand(variation - after_ibp) == 0
    print('[PASS] symmetric h,T: factor 1/2 cancels; Fourier integration by parts checked')

    spatial = lam * sum(delta_h[i, j] * T[i, j]
                        for i in range(1, 4) for j in range(1, 4)) / 2
    split = sp.I * lam * sum(xi[j] * (divergence[j] - k[0] * T[0, j])
                            for j in range(1, 4))
    assert sp.expand(spatial - split) == 0
    residual = -sp.I * lam * k[0] * sum(xi[j] * T[0, j] for j in range(1, 4))
    assert residual.subs(k[0], 0) == 0
    print('[PASS] spatial variation = conserved-shell temporal residual; static residual gauge passes')
    print('VERDICT: algebraic on-shell O(lambda) consistency only; conservation and microscopic matching are inputs.')


if __name__ == '__main__':
    main()
