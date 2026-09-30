"""Certify the scoped factorization audit frozen at f9dcb46.

Run from the repository root:
    python3 -B scripts/verify_cjww_coordinate_factorization.py

One CJWW (5.15) tick, original C^2 cell, three original momenta,
one invertible differentiable factor per coordinate. No grouping,
ancillas, repeated coordinate factors, powers of W, or coordinate mixing.
This is author-side verification, not an independent review.
"""

from itertools import permutations

import sympy as sp

from verify_directional_saturation import (
    I2, PAULI, PS, is_zero, walk1, walk2,
)


def zero_matrix(matrix):
    return all(is_zero(entry) for entry in matrix)


def exact_at(matrix, point):
    return matrix.subs(dict(zip(PS, point))).applyfunc(sp.simplify)


def main():
    W = walk2()
    p1, p2, p3 = PS
    c1, c2 = sp.cos(p1), sp.cos(p2)
    s1, s2 = sp.sin(p1), sp.sin(p2)
    reference = sp.Matrix([
        [c1 * c2 * sp.exp(sp.I * p3), -c1 * s2 + sp.I * s1],
        [c1 * s2 + sp.I * s1, c1 * c2 * sp.exp(-sp.I * p3)],
    ])
    assert zero_matrix(W - reference)
    assert zero_matrix(W.H * W - I2)
    assert is_zero(W.det() - 1)
    print("[PASS] Original walk2 symbol: exact unitarity and determinant 1")

    origin = (0, 0, 0)
    # A first-coordinate factor requires L_i=(d_i W) W^-1 to depend
    # only on p_i. Nonzero cross derivatives disprove this requirement.
    witness_axes = {0: 1, 1: 0, 2: 0}
    left_logs = [sp.diff(W, p) * W.H for p in PS]
    excluded_first = set()
    for i, j in witness_axes.items():
        derivative = exact_at(sp.diff(left_logs[i], PS[j]), origin)
        assert derivative != sp.zeros(2)

        # A second exact test uses separated parameter points, not a
        # numerical scan or a derivative estimate.
        point = [0, 0, 0]
        point[j] = sp.pi / 2
        difference = exact_at(left_logs[i], point) - exact_at(left_logs[i], origin)
        assert difference != sp.zeros(2)
        excluded_first.add(i)
        print(f"[PASS] First axis {i+1} excluded: d_{j+1} L_{i+1}(0)={derivative.tolist()}")
        print(f"       L_{i+1} differs at p_{j+1}=pi/2 with p_{i+1}=0 fixed")

    orders = list(permutations(range(3)))
    assert len(orders) == 6
    assert all(order[0] in excluded_first for order in orders)
    print("[PASS] All six orders excluded by a necessary condition")

    # Second formulation: on p1=pi/2 the entire walk is constant.
    # In a product with one invertible factor per coordinate, fixing p1
    # and p3 would force the p2 factor to be constant; then W must be
    # independent of p2 everywhere, contradicted on p1=0. Likewise p3.
    collapsed = W.subs(p1, sp.pi / 2)
    assert zero_matrix(collapsed - sp.I * PAULI[0])
    expected_other_axes = {1: -sp.I * PAULI[1], 2: sp.I * PAULI[2]}
    for j, expected in expected_other_axes.items():
        varying = exact_at(sp.diff(W, PS[j]), origin)
        assert varying == expected
        assert zero_matrix(sp.diff(collapsed, PS[j]))
    print("[PASS] Second formulation: W(pi/2,p2,p3)=i sigma1, while W varies in p2,p3 at p1=0")

    # A known product-form walk must pass the same necessary criterion.
    factors = [sp.cos(p) * I2 + sp.I * sp.sin(p) * sigma
               for p, sigma in zip(PS, PAULI)]
    W1 = walk1()
    assert zero_matrix(W1 - factors[0] * factors[1] * factors[2])
    left_log_positive = sp.diff(W1, p1) * W1.H
    assert zero_matrix(left_log_positive - sp.I * PAULI[0])
    assert all(zero_matrix(sp.diff(left_log_positive, p)) for p in (p2, p3))
    print("[PASS] Positive control: walk1 has the 1,2,3 product and passes its first-axis condition")

    # Illustrate the invariance that follows for every constant invertible S:
    # d_j[(d_i(SWS^-1))(SWS^-1)^-1] = S(d_j L_i)S^-1.
    # A nonzero witness cannot become zero under invertible conjugation.
    S = (I2 + sp.I * PAULI[2]) / sp.sqrt(2)
    assert zero_matrix(S.H * S - I2)
    for i, j in witness_axes.items():
        witness = exact_at(sp.diff(left_logs[i], PS[j]), origin)
        conjugated = sp.diff(S * W * S.H, PS[i]) * S * W.H * S.H
        transformed = exact_at(sp.diff(conjugated, PS[j]), origin)
        assert zero_matrix(transformed - S * witness * S.H)
        assert transformed != sp.zeros(2)
    print("[PASS] Constant on-site conjugation: covariance identity and nonzero witnesses")
    print("VERDICT: SINGLE_COORDINATE_FACTORIZATION_EXCLUDED")
    print("Scope: one factor per original coordinate, one tick, original two-component cell only")
    print("Evidence: AUTHOR_SIDE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING")


if __name__ == "__main__":
    main()
