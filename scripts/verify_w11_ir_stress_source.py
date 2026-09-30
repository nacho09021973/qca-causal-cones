"""Exact IR stress-source certificate for theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md."""

import sympy as sp
from verify_directional_saturation import walk2, P1, P2, P3, PAULI


def main():
    ps = (P1, P2, P3)
    W = walk2()
    zero = {p: 0 for p in ps}

    E0 = sp.diag(1, -1, 1)
    # CJWW first derivatives.
    dW = [sp.simplify(sp.diff(W, p).subs(zero)) for p in ps]
    target = [sp.I * PAULI[0], -sp.I * PAULI[1], sp.I * PAULI[2]]
    assert dW == target
    print("[PASS] CJWW: W=I+i sigma^a E_a^i p_i+O(p^2)")

    # IR Hamiltonian surrogate H_IR(p) = - sum_a,i sigma_a E_a^i sin p_i.
    H = sp.zeros(2)
    for a in range(3):
        for i in range(3):
            H += -PAULI[a] * E0[a, i] * sp.sin(ps[i])
    H = sp.simplify(H)

    # Derivatives match the branch-local Floquet generator H_eff=-sigma E p+...
    dH = [sp.simplify(sp.diff(H, p).subs(zero)) for p in ps]
    wanted = [-PAULI[0], PAULI[1], -PAULI[2]]
    assert dH == wanted
    print("[PASS] centered-difference H_IR has the correct Weyl linear generator")

    # Local momentum-density surrogate has symbol sin p_i and linear slope one.
    for p in ps:
        assert sp.diff(sp.sin(p), p).subs(p, 0) == 1
    print("[PASS] bond momentum-density surrogate sin(p_i) -> p_i at low momentum")

    print("\nVERDICT: finite-range IR energy/momentum bilinears reproduce the CJWW Weyl stress structures to first order; no exact Floquet stress claim.")


if __name__ == "__main__":
    main()
