"""Exact rank certificate for W5 spatial tetrad completeness."""

import sympy as sp


def main():
    z1,z2,z3,g = sp.symbols("z1 z2 z3 g")
    E0 = sp.diag(1,-1,1)
    D = sp.Matrix([[1,0,0],[1,1,0],[1,1,1]])
    dE = -2*g*sp.diag(z1,z2,z3)*D

    mats_E = [sp.diff(dE, z) for z in (z1,z2,z3)]
    M_E = sp.Matrix.hstack(*[sp.Matrix(m).reshape(9,1) for m in mats_E])
    assert M_E.rank() == 3
    print("[PASS] linearized tetrad image rank = 3 of 9")

    dh = sp.simplify(E0.T*dE + dE.T*E0)
    comps = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
    cols=[]
    for z in (z1,z2,z3):
        cols.append(sp.Matrix([sp.diff(dh[i,j],z) for (i,j) in comps]))
    M_h = sp.Matrix.hstack(*cols)
    assert M_h.rank() == 3
    print("[PASS] linearized metric image rank = 3 of 6")

    print("\nVERDICT: current W3-W5 geometry spans only a restricted spatial-metric submanifold.")


if __name__ == "__main__":
    main()
