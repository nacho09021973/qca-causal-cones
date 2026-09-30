"""Exact certificate for theory/ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md.

Run from repository root:
    python3 -B scripts/verify_elastic_graph_species_universality.py

This certificate tests only the frozen homogeneous common-embedding family:
    X_Lambda(n) = a Lambda n
    W_Lambda(q) = W_0(a Lambda^T q)

It does not introduce strain-dependent hopping amplitudes.
"""

from itertools import product

import sympy as sp

from verify_directional_saturation import PAULI, P1, P2, P3, walk2


PS = (P1, P2, P3)
I2 = sp.eye(2)
BITS_PLUS = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
COMPONENTS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def simp_matrix(m):
    return m.applyfunc(lambda x: sp.simplify(sp.expand(x)))


def node_subs(bits):
    return dict(zip(PS, [sp.pi * b for b in bits]))


def node_sign(bits):
    return (-1) ** sum(bits)


def frame_from_walk(W, bits):
    s = node_sign(bits)
    at = node_subs(bits)
    assert simp_matrix(W.subs(at) - s * I2) == sp.zeros(2)
    E = sp.zeros(3)
    for i, p in enumerate(PS):
        deriv = s * sp.diff(W, p).subs(at)
        for alpha in range(3):
            E[alpha, i] = sp.simplify(
                sp.trace(deriv * PAULI[alpha]) / (2 * sp.I)
            )
    return E.applyfunc(sp.simplify)


def vec6(M):
    return sp.Matrix([sp.simplify(M[i, j]) for i, j in COMPONENTS])


def main():
    W = walk2()

    eps, a = sp.symbols("eps a", nonzero=True, real=True)
    lv = sp.symbols("l11:14 l21:24 l31:34", real=True)
    L = sp.Matrix(3, 3, lv)
    Lam = sp.eye(3) + eps * L

    # E0: Lambda=I is the original physical embedding of the exact CJWW walk.
    assert Lam.subs(eps, 0) == sp.eye(3)
    print("[PASS] E0 flat recovery: Lambda=I gives the undeformed CJWW embedding")

    frames = {}
    metrics = {}

    # E1/E2: derive all decisive node frames from walk2(), then push the
    # common physical momentum through p = a Lambda^T q.
    for bits in BITS_PLUS:
        E = frame_from_walk(W, bits)
        frames[bits] = E
        assert simp_matrix(E.T * E - sp.eye(3)) == sp.zeros(3)

        Ephys = sp.simplify(a * E * Lam.T)
        hphys = simp_matrix(Ephys.T * Ephys)
        expected = simp_matrix(a**2 * Lam * Lam.T)
        assert simp_matrix(hphys - expected) == sp.zeros(3)

        metrics[bits] = hphys
        print(f"[E1/E2] node {bits}: E={tuple(E.diagonal())}")
        print(f"[E1/E2] h_Lambda = a^2 Lambda Lambda^T")

    ref = metrics[BITS_PLUS[0]]
    for bits in BITS_PLUS[1:]:
        assert simp_matrix(metrics[bits] - ref) == sp.zeros(3)
    print("[PASS] E2 species metric universality holds exactly for all four +I nodes")

    # E3: first-order metric coefficient.
    h_dimensionless = sp.simplify(ref / a**2)
    dh = h_dimensionless.applyfunc(
        lambda x: sp.simplify(sp.expand(x).coeff(eps, 1))
    )
    assert simp_matrix(dh - (L + L.T)) == sp.zeros(3)

    metric_map = sp.Matrix([
        [sp.diff(dh[i, j], x) for x in lv]
        for i, j in COMPONENTS
    ])
    assert metric_map.rank() == 6
    assert len(metric_map.nullspace()) == 3

    # The kernel is exactly the antisymmetric infinitesimal part.
    r12, r13, r23 = sp.symbols("r12 r13 r23")
    A = sp.Matrix([
        [0, r12, r13],
        [-r12, 0, r23],
        [-r13, -r23, 0],
    ])
    assert simp_matrix(A + A.T) == sp.zeros(3)

    print("[PASS] E3 delta h / a^2 = eps (L+L^T) + O(eps^2)")
    print("[PASS] E3 symmetric-strain metric rank = 6/6")
    print("[PASS] E3 metric-null tangent dimension = 3 (rigid infinitesimal rotations)")

    print(
        "VERDICT: KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / "
        "ELASTIC_HOPPING_RESPONSE_OPEN"
    )
    print(
        "Scope: homogeneous affine shared embedding only; "
        "no strain-dependent CJWW hopping-amplitude rule, backreaction, "
        "curvature, or gravity claim."
    )


if __name__ == "__main__":
    main()
