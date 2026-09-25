"""Exact identities supporting reports/2026-09-17--scaled-ir-signaling-gate.md.

Scope: SCALED_IR_SIGNALING_GATE only. Analytic inequalities, operator bounds,
and asymptotic nonvanishing are NOT certified by this identity checker.
No lattice truncation, quadrature, floating point, or signal scan.
Run: python3 -B scripts/verify_scaled_ir_gate.py
Frozen helpers are imported read-only; numpy is a transitive dependency.
"""

import hashlib
from pathlib import Path
import sys

import sympy as sp

from verify_directional_saturation import PAULI, PS, is_zero, walk2
from verify_signaling_witness import exact_blocks

ROOT = Path(__file__).resolve().parents[1]
CHARTER_SHA = "325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c"
CHECKS = 0


def require(condition, label):
    global CHECKS
    if condition is not True and condition is not sp.true:
        raise AssertionError(label)
    CHECKS += 1
    print(f"[PASS] {label}")


def main():
    require(hashlib.sha256((ROOT / "theory/SCALED_IR_SIGNALING_GATE.md").read_bytes()).hexdigest()
            == CHARTER_SHA, "frozen charter SHA256")

    # Step 1: geometry/chart/normalization.
    require(3 > sp.Rational(17, 10)**2, "exact complete-region margin sqrt(3)-3/2 > 1/5")
    require(3**2 > 8, "chart arithmetic: 3 > 2sqrt(2), together with analytic pi > 3")
    blocks = exact_blocks()
    require(blocks[(1, 1, 1)] == sp.diag(sp.Rational(1, 4), 0)
            and blocks[(-1, -1, -1)] == sp.diag(0, sp.Rational(1, 4)),
            "both oriented vertex blocks, W and S convention")
    for direction in ((1, 1, 1), (-1, -1, -1)):
        b = blocks[direction]
        require(b*b == b/4, f"vertex recurrence at {direction}; unique-path proof is analytic")
    W = walk2()
    S = W.adjugate()
    require(is_zero(W.det()-1) and all(is_zero(e) for e in S-W.H),
            "holomorphic S=adj W equals W dagger on real torus")
    f = sp.prod(sp.cos(p) for p in PS)
    require(is_zero(S.trace()-2*f) and all(is_zero(e) for e in S*S-2*f*S+sp.eye(2)),
            "trace and Cayley-Hamilton")
    origin = dict.fromkeys(PS, 0)
    H = (PAULI[0], -PAULI[1], PAULI[2])
    require(W.subs(origin) == sp.eye(2) and all(
        sp.simplify(sp.diff(W, p).subs(origin)-sp.I*h) == sp.zeros(2)
        for p, h in zip(PS, H)), "node and frozen linear Weyl symbol")
    r = sp.symbols("r", nonnegative=True)
    z0 = sp.integrate(r**2*(1-r**2)**4, (r, 0, 1))/(2*sp.pi**2)
    g0 = sp.integrate(r**2*(1-r**2)**2, (r, 0, 1))/(2*sp.pi**2)
    require(z0 == 64/(3465*sp.pi**2) and g0 == 4/(105*sp.pi**2), "radial normalization and integral")
    require(sp.simplify(g0*g0/z0-11/(140*sp.pi**2)) == 0, "origin probability constant")

    # Step 2: identities supporting the explicitly proved IR inequalities.
    require((1-16*3*sp.Rational(1, 32)**2)**2 == sp.Rational(61, 64)**2
            and sp.Rational(61, 64)**2 > sp.Rational(1, 2), "inner cube profile floor")
    require(sp.Rational(5, 8)**2+2*sp.Rational(1, 8)**2 < 1,
            "outer proof cube stays within |x|<N")
    theta = sp.symbols("theta", real=True)
    down = sp.Matrix([0, 1])
    for name, M in zip(("I", "sigma1", "sigma2", "sigma3"), (sp.eye(2), *PAULI)):
        U = sp.cos(theta)*sp.eye(2)+sp.I*sp.sin(theta)*M
        a = U-sp.eye(2)
        require(M*M == sp.eye(2) and sp.simplify(a.H*a-2*(1-sp.cos(theta))*sp.eye(2)) == sp.zeros(2),
                f"encoder {name}: norm identity for every local phase")
        expected = {"I": sp.exp(sp.I*theta), "sigma1": sp.cos(theta),
                    "sigma2": sp.cos(theta), "sigma3": sp.exp(-sp.I*theta)}[name]
        require(sp.simplify(sp.expand_complex((down.H*U*down)[0]-expected)) == 0,
                f"encoder {name}: down-spin overlap")
    for name, B in zip(("I", "+1", "+2", "+3"), (sp.eye(2), *((sp.eye(2)+p)/2 for p in PAULI))):
        require(B*B == B and B.H == B and 1 in B.eigenvals(), f"detector {name}: norm-one positive projection")
    n = sp.symbols("N", positive=True)
    k = 1/(6*sp.pi**2*n**sp.Rational(3, 2))
    s = 11/(140*sp.pi**2*n**3)
    require(sp.limit(sp.sqrt(1-k), n, sp.oo) == 1
            and sp.limit((1-k)*(1-3*s*(1-k))/(1-s), n, sp.oo) == 1,
            "point sanity limits with the two frozen scales")

    # Step 3: product-of-ellipses calculation, used by the analytic proof.
    # a^2=A, c^2=C, b^2=A-1, d^2=C-1, cos(p)^2=u.
    A, C, u = sp.symbols("A C u", real=True)
    B2 = A*C-1
    # Matrix L = diag(1/ac,1/sqrt(B2)) [[a cos p,-b sin p],[b sin p,a cos p]] diag(c,d).
    # Tr(L^T L) and det(L)^2, with radicals eliminated exactly.
    trace = u + (A-1)*(1-u)*(C-1)/(A*C) + (A-1)*(1-u)*C/B2 + A*u*(C-1)/B2
    determinant_squared = (A-1+u)**2*(C-1)/(A*B2)
    determinant_gap = (C-1)*(1-u)*(A-1+C*(1-u))/(A*C*(A*C-1))
    require(sp.factor(1-trace+determinant_squared-determinant_gap) == 0,
            "ellipse product: determinant of I-L^T L factors into nonnegative terms")
    first_gap = 1-u-(A-1)*(1-u)*C/B2
    require(sp.factor(first_gap-(1-u)*(C-1)/B2) == 0,
            "ellipse product: first diagonal gap")
    second_gap = 1-(A-1)*(1-u)*(C-1)/(A*C)-A*u*(C-1)/B2
    require(sp.factor(second_gap-((1-u)*(A+C-1)/(A*C)+u*(A-1)/B2)) == 0,
            "ellipse product: second diagonal gap is a convex combination of positive terms")
    require(sp.simplify(sp.cosh(sp.log(2)).rewrite(sp.exp)) == sp.Rational(5, 4),
            "contour t=log 2: cosh(t)=5/4")
    require(sp.Rational(5, 4)**3 == sp.Rational(125, 64)
            and sp.Rational(125, 64) < sp.Rational(17, 8),
            "trace ellipse semiaxis < cosh(log 4): spectral radius < 4")
    block_norm_sum = sum(sp.sqrt(max((b.H*b).eigenvals())) for b in blocks.values())
    require(block_norm_sum == 4, "exact sum of norms of the fourteen Laurent blocks")
    require(sp.Rational(3, 1) < 4, "J=(1-sqrt(3)/2)log(2) is strictly positive")

    # Step 4: response identities for every frozen internal direction.
    c, s = sp.symbols("c s", real=True)
    encoder_columns = (sp.Matrix([0, c+sp.I*s]), sp.Matrix([sp.I*s, c]),
                       sp.Matrix([s, c]), sp.Matrix([0, c-sp.I*s]))
    for name, M, expected in zip(("I", "sigma1", "sigma2", "sigma3"),
                                  (sp.eye(2), *PAULI), encoder_columns):
        require((c*sp.eye(2)+sp.I*s*M)*down == expected,
                f"physical response input column {name}")
    r0, r1, x0, x1 = sp.symbols("r0 r1 x0 x1", real=True)
    R = sp.Matrix([[r0, x0+sp.I*x1], [x0-sp.I*x1, r1]])
    effects = (sp.eye(2), *((sp.eye(2)+p)/2 for p in PAULI))
    expected_readouts = (r0+r1, (r0+r1)/2+x0, (r0+r1)/2-x1, r0)
    for name in ("I", "sigma1", "sigma2", "sigma3"):
        for label, B, expected in zip(("I", "+1", "+2", "+3"), effects, expected_readouts):
            require(sp.expand(sp.trace(B*R)-expected) == 0,
                    f"pair {name}/{label}: exact Hermitian response functional (no nonzero claim)")
    print(f"{CHECKS}/{CHECKS} exact identity checks passed; analytic proof coverage is separate.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] {exc!r}")
        sys.exit(1)
