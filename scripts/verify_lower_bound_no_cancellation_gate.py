"""Exact identities supporting reports/2026-09-17--lower-bound-no-cancellation-gate.md.

Scope: LOWER_BOUND_NO_CANCELLATION_GATE only. Does not certify a leading
amplitude, non-cancellation, exact vanishing, or any terminal state.
No lattice truncation, quadrature, floating point, or N-scan of delta.
Run: python3 -B scripts/verify_lower_bound_no_cancellation_gate.py
Frozen helpers are imported read-only.
"""

import hashlib
from pathlib import Path
import sys

import sympy as sp

from verify_directional_saturation import PAULI, is_zero, walk2
from verify_signaling_witness import exact_blocks

ROOT = Path(__file__).resolve().parents[1]
CHARTER_SHA = "5db6f88a2ca77bfd6d8af2bde9c20f683e05288a0c941f6cd59724e4fb510afb"
SCALED_SHA = "325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c"
CHECKS = 0


def require(condition, label):
    global CHECKS
    if condition is not True and condition is not sp.true:
        raise AssertionError(label)
    CHECKS += 1
    print(f"[PASS] {label}")


def main():
    require(hashlib.sha256((ROOT / "theory/LOWER_BOUND_NO_CANCELLATION_GATE.md").read_bytes()).hexdigest()
            == CHARTER_SHA, "frozen lower-bound charter SHA256")
    require(hashlib.sha256((ROOT / "theory/SCALED_IR_SIGNALING_GATE.md").read_bytes()).hexdigest()
            == SCALED_SHA, "inherited scaled-IR charter SHA256")

    blocks = exact_blocks()
    # States evolve by S = W^dagger, so S_d = W_{-d}^H.
    S_plus = blocks[(-1, -1, -1)].H
    S_minus = blocks[(1, 1, 1)].H
    down = sp.Matrix([0, 1])
    up = sp.Matrix([1, 0])
    require(S_plus == sp.diag(0, sp.Rational(1, 4)) and S_plus*up == sp.zeros(2, 1)
            and S_plus*down == down/4,
            "S_(1,1,1)=(1/4)|down><down|; unique path kills up")
    require(S_minus == sp.diag(sp.Rational(1, 4), 0) and S_minus*down == sp.zeros(2, 1),
            "S_(-1,-1,-1) kills down; opposite vertex is up-preserving")
    require(S_plus*S_plus == S_plus/4, "vertex recurrence: (S_(1,1,1))^N = 4^{-N} |down><down|")

    W = walk2()
    S = W.adjugate()
    require(all(is_zero(e) for e in S*S - S.trace()*S + sp.eye(2)),
            "Cayley-Hamilton of S, inherited")

    require(3 > sp.Rational(9, 4), "facing |v|_2 = sqrt(3)-1/2 > 1, i.e. outside the IR ball")
    facing_factor = 1 - 1/(2*sp.sqrt(3))
    require(sp.simplify(facing_factor*sp.sqrt(3) - (sp.sqrt(3) - sp.Rational(1, 2))) == 0,
            "facing displacement |d|_2/N = sqrt(3)-1/2 along u")
    require(sp.simplify(3*facing_factor - (3 - sp.sqrt(3)/2)) == 0,
            "facing tilt u.(y-x)/N = 3-sqrt(3)/2, the (G) minimum")

    N, eps = sp.symbols("N eps", positive=True)
    r = N/4 - eps
    gap = 1 - 16*r**2/N**2
    require(sp.factor(sp.simplify(gap - 8*eps*(N-2*eps)/N**2)) == 0,
            "radial gap at depth eps: 8 eps (N-2eps)/N^2")
    F = gap**2
    require(sp.factor(sp.simplify(F - 64*eps**2*(N-2*eps)**2/N**4)) == 0,
            "F_N = (1-16 r^2/N^2)^2 vanishes quadratically in depth at the sphere")
    require(sp.simplify(F.subs(eps, 0)) == 0, "profiles are exactly zero on the Euclidean sphere")

    Fsym = sp.symbols("F", real=True)
    cN = sp.cos(sp.pi*Fsym/2) - 1
    sN = sp.sin(sp.pi*Fsym/2)
    require(cN.series(Fsym, 0, 4).removeO() == -sp.pi**2*Fsym**2/8,
            "c_N = cos(pi F/2)-1 = -pi^2 F^2/8 + O(F^4); second order in F")
    require(sN.series(Fsym, 0, 2).removeO() == sp.pi*Fsym/2,
            "s_N = sin(pi F/2) = pi F/2 + O(F^3); first order in F")

    theta = sp.pi/2
    for name, M in zip(("I", "sigma1", "sigma2", "sigma3"), (sp.eye(2), *PAULI)):
        U = sp.cos(theta)*sp.eye(2) + sp.I*sp.sin(theta)*M
        require(M*M == sp.eye(2) and U == sp.I*M,
                f"at the profile maximum F=1, encoder {name} is iM")

    c, s = sp.symbols("c s", real=True)
    encoder_columns = (sp.Matrix([0, c+sp.I*s]), sp.Matrix([sp.I*s, c]),
                       sp.Matrix([s, c]), sp.Matrix([0, c-sp.I*s]))
    for name, M, expected in zip(("I", "sigma1", "sigma2", "sigma3"),
                                  (sp.eye(2), *PAULI), encoder_columns):
        require((c*sp.eye(2)+sp.I*s*M)*down == expected,
                f"inherited amplitude column {name}")

    t = sp.log(2)
    f0 = sp.cosh(t)**3
    require(sp.simplify(f0.rewrite(sp.exp)) == sp.Rational(125, 64),
            "tilted trace at p=0, t=log 2: cosh(t)^3 = 125/64")
    require(sp.Rational(125, 64) < 4, "rho(p=0) < 4, so vertex rate log 4 is strictly faster than the t=log2 bound")

    print(f"{CHECKS}/{CHECKS} exact identity checks passed; "
          "leader identification and remainder control are analytic and open.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] {exc!r}")
        sys.exit(1)
