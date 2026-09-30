"""Exact certificate for theory/W8_TT_GAUGE_COMPLETION_GATE.md."""

import sympy as sp


def main():
    ax, ay, az = sp.symbols("xi_x xi_y xi_z")
    # k=(0,0,1), traceless-projected sym gradient.
    G = sp.Matrix([
        -sp.Rational(2,3)*az,  # xx
        -sp.Rational(2,3)*az,  # yy
         sp.Rational(4,3)*az,  # zz
         0,                    # xy
         ax,                   # xz
         ay,                   # yz
    ])
    vars_ = (ax,ay,az)
    M = sp.Matrix.hstack(*[
        sp.Matrix([sp.diff(G[i],v) for i in range(6)])
        for v in vars_
    ])
    assert M.rank() == 3
    print("[PASS] traceless vector-gauge orbit rank = 3 for k along z")

    # Generic symmetric-traceless tensor in components.
    qxx,qyy,qxy,qxz,qyz = sp.symbols("qxx qyy qxy qxz qyz")
    qzz = -qxx-qyy
    # Gauge choice: kill xz,yz,zz.
    sol = {
        ax: -qxz,
        ay: -qyz,
        az: -sp.Rational(3,4)*qzz,
    }
    qxxp = sp.simplify(qxx + G[0].subs(sol))
    qyyp = sp.simplify(qyy + G[1].subs(sol))
    qzzp = sp.simplify(qzz + G[2].subs(sol))
    qxzp = sp.simplify(qxz + G[4].subs(sol))
    qyzp = sp.simplify(qyz + G[5].subs(sol))
    assert qzzp == 0 and qxzp == 0 and qyzp == 0
    assert sp.simplify(qxxp+qyyp) == 0
    print("[PASS] gauge can set Q_xz=Q_yz=Q_zz=0, leaving Q_xx=-Q_yy and Q_xy")

    print("\nVERDICT: proposed local vector gauge symmetry would reduce the 5-component spin-2 tensor to 2 TT components.")


if __name__ == "__main__":
    main()
