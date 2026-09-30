"""Fail-closed certificate for theory/ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md.

This checks the contract's orientation-independence premise before any
four-species metric calculation.
"""

import sympy as sp
from verify_directional_saturation import walk2, laurent, Z


def blocks():
    out = {}
    W = walk2()
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(W[i, j]) * Z[0]*Z[1]*Z[2]), *Z)
            for mono, coeff in poly.terms():
                h = tuple(int(m)-1 for m in mono)
                if coeff != 0:
                    out.setdefault(h, sp.zeros(2))[i, j] = sp.simplify(coeff)
    return out


def K_at_zero(Fplus, B):
    K = sp.zeros(2)
    for h in Fplus:
        # isotropic strain u=I gives rho_h=1 for every nonzero bond
        M = B[h]
        K += M + M.H
    return sp.simplify(K)


def main():
    B = blocks()
    assert len(B) == 14

    mismatches = []
    for h, M in sorted(B.items()):
        hm = tuple(-x for x in h)
        if sp.simplify(B[hm] - M.H) != sp.zeros(2):
            mismatches.append(h)
    assert mismatches
    print(f"[PASS] W_-h != W_h^dagger for {len(mismatches)}/14 support vectors")

    # Two equally admissible orientation choices under the frozen text:
    # first coordinate +1 versus first coordinate -1.
    Fp = sorted(h for h in B if h[0] == 1)
    Fm = sorted(h for h in B if h[0] == -1)
    assert len(Fp) == len(Fm) == 7

    Kp = K_at_zero(Fp, B)
    Km = K_at_zero(Fm, B)

    assert Kp == sp.Matrix([[1, 1], [1, 1]])
    assert Km == sp.Matrix([[1, -1], [-1, 1]])
    assert Kp != Km

    print("[PASS] for u=I,p=0 the two admissible choices give")
    print(f"       K_(h1=+1) = {Kp.tolist()}")
    print(f"       K_(h1=-1) = {Km.tolist()}")
    print("[PASS] the frozen generator depends on arbitrary F_+ orientation")
    print("\nVERDICT: UNITARY_ELASTIC_RESPONSE_INCONSISTENT")


if __name__ == "__main__":
    main()
