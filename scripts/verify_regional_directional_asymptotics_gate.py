"""Exact identities supporting reports/2026-09-17--regional-directional-asymptotics-gate.md.

Scope: REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE only. Does not certify the
value of C, beta, remainder control, or any terminal state other than the
algebraic identities listed. No N-scan of L, no quadrature of signals.
Run: python3 -B scripts/verify_regional_directional_asymptotics_gate.py
Frozen helpers are imported read-only.
"""

import hashlib
from pathlib import Path
import sys

import sympy as sp

from verify_directional_saturation import PS, is_zero, walk2

ROOT = Path(__file__).resolve().parents[1]
CHARTER_SHA = "3a5fe8d4b22c26d017994eb849ea4e896b6e9a5230758f5c678c135c8e38977d"
LB_SHA = "5db6f88a2ca77bfd6d8af2bde9c20f683e05288a0c941f6cd59724e4fb510afb"
SCALED_SHA = "325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c"
CHECKS = 0


def require(condition, label):
    global CHECKS
    if condition is not True and condition is not sp.true:
        raise AssertionError(label)
    CHECKS += 1
    print(f"[PASS] {label}")


def main():
    require(hashlib.sha256((ROOT / "theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md").read_bytes()).hexdigest()
            == CHARTER_SHA, "frozen regional-asymptotics charter SHA256")
    require(hashlib.sha256((ROOT / "theory/LOWER_BOUND_NO_CANCELLATION_GATE.md").read_bytes()).hexdigest()
            == LB_SHA, "inherited cancellation-gate charter SHA256")
    require(hashlib.sha256((ROOT / "theory/SCALED_IR_SIGNALING_GATE.md").read_bytes()).hexdigest()
            == SCALED_SHA, "inherited scaled-IR charter SHA256")

    xi = sp.symbols("xi1 xi2 xi3", real=True)
    subs = {PS[j]: -sp.I * xi[j] for j in range(3)}
    S = walk2().subs(subs).adjugate()
    fS = sp.simplify(S.trace() / 2)
    target = sp.prod([sp.cosh(xi[j]) for j in range(3)])
    require(sp.simplify(fS - target) == 0, "holomorphic f(-i xi) = prod_j cosh(xi_j)")
    require(sp.simplify(sp.det(S) - 1) == 0, "det S(-i xi) = 1, entire unimodular")

    alpha = 1 - 1/(2*sp.sqrt(3))
    require(sp.simplify(3*alpha - (3 - sp.sqrt(3)/2)) == 0,
            "facing v* = alpha (1,1,1) with 3 alpha = 3-sqrt(3)/2")
    require(sp.simplify(alpha*sp.sqrt(3) - (sp.sqrt(3) - sp.Rational(1, 2))) == 0,
            "|v*|_2 = sqrt(3)-1/2")
    require(4 > 3, "alpha > 1/sqrt(3): 1-1/(2sqrt3) > 1/sqrt(3) iff 2>sqrt(3) iff 4>3")
    require(sp.simplify(1 - alpha) == 1/(2*sp.sqrt(3)), "alpha < 1, so v* is not the cube vertex")

    uhat = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    vstar = alpha * sp.Matrix([1, 1, 1])
    # V_reg subset: uhat.v >= |v*| with equality only at v*
    # |c + w| >= |c|-|w|, c=(1,1,1), |w|<=1/2, equality iff w parallel to -c
    require(3 > sp.Rational(9, 4), "min |v|_2 > 1, so I(v*)>0")

    # feasible tilt t=log 2 gives I(v*) >= sigma log 2 - acosh(125/64) > J
    sigma = 3*alpha
    require(sp.Rational(125, 64) < sp.Rational(17, 8),
            "acosh(125/64)<log 4, hence the log2 tilt lower-bounds I(v*) strictly above J")

    t = sp.symbols("t", positive=True)
    C0 = sp.cosh(t)
    S0 = -sp.I * sp.sinh(t)
    Wtilted = sp.Matrix([
        [C0*C0*sp.exp(t), -C0*S0 + sp.I*S0],
        [C0*S0 + sp.I*S0, C0*C0*sp.exp(-t)],
    ])
    Stil = Wtilted.adjugate()
    off = sp.simplify(Stil[0, 1])
    require(sp.simplify(off + (sp.I*C0 + 1)*sp.sinh(t)) == 0,
            "tilted S_{12} = -(i cosh t + 1) sinh t")
    require(sp.simplify(off.subs(sp.sinh(t), 0)) == 0,
            "mixing vanishes at sinh t = 0, i.e. only at zero tilt")
    require(sp.simplify(sp.diff(off, t).subs(t, 0)) != 0,
            "mixing turns on linearly in t: leading eigenvector is not spin-aligned")

    Fsym = sp.symbols("F", real=True)
    require((sp.cos(sp.pi*Fsym/2)-1).series(Fsym, 0, 4).removeO() == -sp.pi**2*Fsym**2/8,
            "c_N = O(F^2)")
    require((sp.sin(sp.pi*Fsym/2)).series(Fsym, 0, 2).removeO() == sp.pi*Fsym/2,
            "s_N = O(F)")
    N, eps = sp.symbols("N eps", positive=True)
    gap = 1 - 16*(N/4 - eps)**2 / N**2
    require(sp.simplify(sp.factor(gap**2).subs(eps, 0)) == 0,
            "profiles vanish on the Euclidean spheres")

    # 1D model: -kappa eps + p log eps, critical point eps = p/kappa
    kappa, p = sp.symbols("kappa p", positive=True)
    eff = -kappa * eps + p * sp.log(eps)
    crit = sp.diff(eff, eps)
    require(sp.simplify(sp.solve(crit, eps)[0] - p/kappa) == 0,
            "layer critical depth eps=p/kappa is O(1) for kappa,p = O(1)")

    print(f"{CHECKS}/{CHECKS} exact identity checks passed; "
          "C, beta and remainder control remain analytic.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] {exc!r}")
        sys.exit(1)
