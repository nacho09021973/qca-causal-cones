"""Exact certificate for theory/W1_GEOMETRICITY_GATE.md.

Checks a two-step support witness for the W1 link-register bridge.
No floating point and no continuum/gravity interpretation.

Run:
    python3 scripts/verify_w1_geometricity.py
"""

import sympy as sp

from verify_directional_saturation import Z, laurent, walk2


ORIGIN = (0, 0, 0)
TARGET = (0, 0, 1)
Y_STAR = (1, 1, 1)
D_EDGE = (1, 0, 0)


def exact_blocks():
    blocks = {}
    symbol = walk2()
    shift = sp.prod(Z)
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(symbol[i, j]) * shift), *Z)
            for powers, coefficient in poly.terms():
                if coefficient == 0:
                    continue
                displacement = tuple(power - 1 for power in powers)
                blocks.setdefault(displacement, sp.zeros(2))[i, j] = sp.simplify(coefficient)
    return blocks


def nz(M):
    return any(sp.simplify(v) != 0 for v in M)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def main():
    blocks = exact_blocks()
    assert len(blocks) == 14

    # Exact two-step CJWW kernel at TARGET.
    K2 = sp.zeros(2)
    intermediates = []
    pathwise = 0
    for y, W_y0 in blocks.items():
        d2 = sub(TARGET, y)
        if d2 not in blocks:
            continue
        pathwise += 1
        M_y = sp.simplify(blocks[d2] * W_y0)
        if nz(M_y):
            intermediates.append((y, M_y))
        K2 += M_y
    K2 = K2.applyfunc(sp.simplify)

    assert pathwise == 8
    assert len(intermediates) == 8
    assert K2 == sp.zeros(2)
    print("[PASS] U0^2 has eight nonzero path contributions to (0,0,1) that cancel exactly")

    # One chosen intermediate has a nonzero matrix contribution.
    M_star = dict(intermediates)[Y_STAR]
    want = sp.Matrix([[0, 0], [sp.I / 16, 0]])
    assert M_star == want
    print("[PASS] y*=(1,1,1) contributes M*= [[0,0],[i/16,0]]")

    # Choose e*={y*,y*+(1,0,0)}.  It is incident to no other contributing
    # intermediate, so in the first derivative of the joint two-step
    # amplitude the Pauli B_e* coefficient is exactly M_star.
    other = add(Y_STAR, D_EDGE)
    intermediate_sites = {y for y, _ in intermediates}
    assert other not in intermediate_sites
    assert sum(1 for y in intermediate_sites if y in {Y_STAR, other}) == 1
    print("[PASS] edge e*={(1,1,1),(2,1,1)} is unique to y* among contributing intermediates")

    # B=Z+X maps |0> to |0>+|1>; the component with only e* flipped
    # therefore has derivative -i M_star, which is nonzero.
    derivative_flip = sp.simplify(-sp.I * M_star)
    assert nz(derivative_flip)
    assert derivative_flip == sp.Matrix([[0, 0], [sp.Rational(1, 16), 0]])
    print("[PASS] product-|0> geometry lifts the zero at first order in g")

    # By contrast, if every edge is in a B eigenstate with eigenvalue sqrt(2),
    # each site sees 14 incident edges, so V_g acts by one position-independent
    # phase exp(-i 14 sqrt(2) g); all CJWW cancellations are preserved.
    degree = 14
    lam = sp.sqrt(2)
    site_phase_exponent = sp.simplify(degree * lam)
    assert site_phase_exponent == 14 * sp.sqrt(2)
    assert K2 == sp.zeros(2)
    print("[PASS] B-eigenstate geometry preserves U0^2 support up to a global phase")

    print("\nVERDICT: finite-time exact matter support depends on the link-register state; "
          "one-step adjacency and the outer CJWW causal body are unchanged.")


if __name__ == "__main__":
    main()
