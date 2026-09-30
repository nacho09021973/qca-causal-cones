"""Exact certificate for theory/ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md.

Run from repository root:
    python3 -B scripts/verify_elastic_hopping_hermitian_response.py

Scope:
- exact CJWW (5.15) Fourier blocks;
- full 14-hop orientation-independent bond weighting;
- first order in elastic parameter epsilon and species momentum;
- four decisive +I Weyl nodes;
- common physical coordinates.

No coefficient search or tuning is performed.
"""

import sympy as sp

from verify_directional_saturation import (
    PAULI, P1, P2, P3, Z, laurent, walk2
)

PS = (P1, P2, P3)
I2 = sp.eye(2)
PLUS = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
COMPONENTS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]

u11, u22, u33, u12, u13, u23 = sp.symbols(
    "u11 u22 u33 u12 u13 u23", real=True
)
UV = (u11, u22, u33, u12, u13, u23)
U = sp.Matrix([
    [u11, u12, u13],
    [u12, u22, u23],
    [u13, u23, u33],
])


def simp(M):
    return M.applyfunc(lambda x: sp.simplify(sp.expand(x)))


def fourier_blocks():
    out = {}
    W = walk2()
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(
                sp.expand(laurent(W[i, j]) * Z[0] * Z[1] * Z[2]), *Z
            )
            for mono, coeff in poly.terms():
                if sp.simplify(coeff) == 0:
                    continue
                h = tuple(int(m) - 1 for m in mono)
                out.setdefault(h, sp.zeros(2))[i, j] = sp.simplify(coeff)
    return out


def rho(h):
    hv = sp.Matrix(h)
    return sp.simplify((hv.T * U * hv)[0] / (hv.dot(hv)))


def node_subs(bits):
    return dict(zip(PS, [sp.pi * b for b in bits]))


def frame_from_walk(W, bits):
    at = node_subs(bits)
    assert simp(W.subs(at) - I2) == sp.zeros(2)
    E = sp.zeros(3)
    for i, p in enumerate(PS):
        dW = sp.diff(W, p).subs(at)
        for a, sigma in enumerate(PAULI):
            E[a, i] = sp.simplify(
                sp.trace(dW * sigma) / (2 * sp.I)
            )
    return E


def pauli_decomp(H):
    scalar = sp.simplify(sp.trace(H) / 2)
    vec = sp.Matrix([
        sp.simplify(sp.trace(H * sigma) / 2)
        for sigma in PAULI
    ])
    return scalar, vec


def vec6(M):
    return sp.Matrix([sp.simplify(M[i, j]) for i, j in COMPONENTS])


def main():
    W = walk2()
    B = fourier_blocks()

    # HH0 / flat data.
    assert len(B) == 14
    assert set(B) == {tuple(-x for x in h) for h in B}
    print("[PASS] HH0 flat CJWW support recovered: 14 directed hops")

    # Full orientation-independent weighted symbol.
    R = sp.zeros(2)
    for h, Wh in B.items():
        hm = tuple(-x for x in h)
        assert sp.simplify(rho(h) - rho(hm)) == 0
        phase = sp.exp(sp.I * sum(PS[i] * h[i] for i in range(3)))
        R += rho(h) * phase * Wh

    K = sp.simplify((R + R.H) / 2)
    assert simp(K - K.H) == sp.zeros(2)
    print("[PASS] HH1 rho_-h=rho_h and full-support K=(R+R^dag)/2 is Hermitian")

    # HH2: exact unitarity follows algebraically from Hermitian K and flat
    # unitary W. We certify the two ingredients exactly.
    assert simp(W.H * W - I2) == sp.zeros(2)
    print("[PASS] HH2 ingredients: K Hermitian and W0 unitary => exp(-i eps K) W0 unitary exactly")

    metric_rows = []
    hopping_frames = []

    for bits in PLUS:
        at = node_subs(bits)
        E = frame_from_walk(W, bits)
        assert simp(E.T * E - sp.eye(3)) == sp.zeros(3)

        K0 = simp(K.subs(at))
        alpha, kvec = pauli_decomp(K0)

        want_alpha = sp.simplify((u11 + u22 + u33) / 3)
        assert sp.simplify(alpha - want_alpha) == 0
        assert kvec == sp.zeros(3, 1)

        # HH3: there is no traceless constant term, hence no node displacement.
        dq = sp.zeros(3, 1)
        print(
            f"[HH3] node {bits}: K(p*)=(tr u/3) I; "
            "delta q*=0; scalar quasienergy phase only"
        )

        # First-order hopping correction:
        # F = (I - i eps K) W + O(eps^2).
        A = sp.simplify(-sp.I * K * W)

        # Remove the scalar phase exp(-i eps alpha).  Since delta q*=0, no
        # Hessian/node-shift contribution occurs.
        dE_hop = sp.zeros(3)
        tilt = sp.zeros(1, 3)
        for j, p in enumerate(PS):
            corr = sp.simplify(
                sp.diff(A, p).subs(at)
                + sp.I * alpha * sp.diff(W, p).subs(at)
            )
            tilt[0, j] = sp.simplify(sp.trace(corr) / 2)
            for a, sigma in enumerate(PAULI):
                dE_hop[a, j] = sp.simplify(
                    sp.trace(corr * sigma) / (2 * sp.I)
                )

        assert dE_hop == sp.zeros(3)
        assert tilt == sp.zeros(1, 3)
        hopping_frames.append(dE_hop)

        # Common physical embedding p=(I+eps u)^T q adds E u to the frame.
        dE_total = sp.simplify(E * U + dE_hop)
        dh = simp(E.T * dE_total + dE_total.T * E)
        assert simp(dh - 2 * U) == sp.zeros(3)
        metric_rows.append(dh)

        print(
            f"[HH4/HH6] node {bits}: hopping-induced deltaE=0; "
            "delta h = 2u from common embedding only"
        )

    # HH4: exact equality of the first-order metric maps at all four species.
    ref = metric_rows[0]
    assert all(simp(M - ref) == sp.zeros(3) for M in metric_rows[1:])
    print("[PASS] HH4 four-species metric universality: delta h_* = 2u for all +I nodes")

    # HH5: rank on the six independent metric components.
    Hmap = sp.Matrix([
        [sp.diff(x, v) for v in UV]
        for x in vec6(ref)
    ])
    assert Hmap.rank() == 6
    print("[PASS] HH5 universal metric rank = 6/6")

    # HH6: hopping contribution is exactly zero at retained order.
    assert all(M == sp.zeros(3) for M in hopping_frames)
    print("[PASS] HH6 hopping contribution to the principal spatial metric is zero")
    print("       universal rank-6 response is entirely the common-embedding term")

    print(
        "\nVERDICT: HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY"
    )
    print(
        "Scope: first order in epsilon and species momentum, four +I nodes, "
        "common physical coordinates. No dynamical-strain/gravity claim."
    )


if __name__ == "__main__":
    main()
