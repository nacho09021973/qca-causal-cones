"""Exact linear-algebra certificate for theory/W7_SPIN2_KINEMATICS_GATE.md."""

import sympy as sp


def vec(M):
    return sp.Matrix([M[i,j] for i in range(3) for j in range(3)])


def main():
    a = sp.symbols("a0:9")
    A = sp.Matrix(3,3,a)
    Omega = sp.simplify((A-A.T)/2)
    S = sp.simplify((A+A.T)/2)
    phi = sp.simplify(sp.trace(S))
    Q = sp.simplify(S - phi*sp.eye(3)/3)

    assert sp.simplify(A-(Omega + phi*sp.eye(3)/3 + Q)) == sp.zeros(3)
    assert sp.simplify(Omega+Omega.T) == sp.zeros(3)
    assert sp.simplify(Q-Q.T) == sp.zeros(3)
    assert sp.simplify(sp.trace(Q)) == 0
    print("[PASS] A = antisymmetric(3) + trace(1) + symmetric-traceless(5)")

    # Rank/dimension checks via coefficient matrices.
    def coeff_rank(exprs):
        cols=[]
        for x in a:
            cols.append(sp.Matrix([sp.diff(e,x) for e in exprs]))
        return sp.Matrix.hstack(*cols).rank()

    om_rank = coeff_rank(list(vec(Omega)))
    s_rank = coeff_rank(list(vec(S)))
    q_rank = coeff_rank(list(vec(Q)))
    assert (om_rank,s_rank,q_rank) == (3,6,5)
    print("[PASS] dimensions are 3, 6, 5 respectively")

    dh = sp.simplify(A + A.T)
    assert sp.simplify(dh - (2*phi*sp.eye(3)/3 + 2*Q)) == sp.zeros(3)
    assert sp.simplify(dh.subs({x:0 for x in a}) - sp.zeros(3)) == sp.zeros(3)
    print("[PASS] metric sees trace + spin-2 sector, antisymmetric frame sector drops out")

    # Infinitesimal rotation: Q -> Q + [Omega_r,Q] preserves symmetry/tracelessness.
    x,y,z = sp.symbols("x y z")
    Rgen = sp.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
    dQ = sp.simplify(Rgen*Q - Q*Rgen)
    assert sp.simplify(dQ-dQ.T) == sp.zeros(3)
    assert sp.simplify(sp.trace(dQ)) == 0
    print("[PASS] symmetric-traceless sector is closed under infinitesimal SO(3) rotations")

    print("\nVERDICT: W6 contains a 5-component kinematic spin-2 sector; TT reduction is not supplied.")


if __name__ == "__main__":
    main()
