"""Exact analytic certificate for theory/NARROW_BAND_SIGNALING_GATE.md, steps 0-2.

Backs reports/2026-09-17--narrow-band-signaling-gate.md. Run from the repository
root:

    python3 scripts/verify_narrow_band_gate.py

Exact SymPy only: no floating point, quadrature, lattice truncation, Lambda scan
or optimization. The band-limited packet is spatially extended, so the
finite-support helpers of verify_signaling_witness.py cannot represent it; only
the frozen symbol walk2() and the Laurent equality test are reused, read-only.

Scope is the charter order: class and chart, pre-choice IR control, then the
encoded-difference test of Sec. 7. That test fails, so the Sec. 7 stop rule
applies: no propagated difference, Bob state or D_B is constructed here.
"""

import hashlib
from pathlib import Path
import sys

import sympy as sp

from verify_directional_saturation import C as COS, PAULI, PS, S as SIN, is_zero, walk2


ROOT = Path(__file__).resolve().parents[1]
CHARTER = ROOT / "theory/NARROW_BAND_SIGNALING_GATE.md"
CHARTER_SHA256 = "3d559cedefa0b6c25bd0af7ef13a993e2b71e1a8f7f97ae4f29f988147541ba9"
P1, P2, P3 = PS
c1, c2, c3 = COS
s1, s2, s3 = SIN
LAM = sp.symbols("Lambda", positive=True)
CHECKS = 0


def verify(condition, message):
    global CHECKS
    # Only Python True or SymPy's decided true passes; undecided relations fail.
    if not (condition is True or condition is sp.true):
        raise AssertionError(message)
    CHECKS += 1
    print(f"[PASS] {message}")


def zero_matrix(M):
    return all(is_zero(entry) for entry in M)


def ball_integral(radial):
    """int_{|p|<=Lambda} radial(|p|) dmu, dmu = d^3p/(2 pi)^3; ball inside B."""
    r = sp.symbols("r", nonnegative=True)
    return sp.simplify(sp.integrate(4 * sp.pi * r**2 * radial(r), (r, 0, LAM)) / (2 * sp.pi)**3)


def trace_norm_rank2(X):
    """||X||_1 for Hermitian X with det X = 0 and e2(X) <= 0 (sign checked by caller)."""
    tr = X.trace()
    e2 = sp.expand((tr**2 - (X * X).trace()) / 2)
    return sp.expand(tr**2 - 4 * e2), e2


def main():
    # ---------------------------------------------------------------- preflight
    verify(hashlib.sha256(CHARTER.read_bytes()).hexdigest() == CHARTER_SHA256,
           "charter bytes are the published preregistration (817050d blob)")

    # ------------------------------------------- step 0: class, node and chart
    W = walk2()
    S = W.H
    verify(zero_matrix(W.H * W - sp.eye(2)) and is_zero(W.det() - 1),
           "CJWW (5.15) symbol is unitary with det 1")
    verify(W.subs({P1: 0, P2: 0, P3: 0}) == sp.eye(2), "node: W(0) = I")
    H_terms = (PAULI[0], -PAULI[1], PAULI[2])
    verify(all(sp.simplify(sp.diff(W, p).subs({P1: 0, P2: 0, P3: 0}) - sp.I * h) == sp.zeros(2)
               for p, h in zip(PS, H_terms)),
           "linear term W = I + i H_W + O(p^2), H_W = p1 s1 - p2 s2 + p3 s3")
    H_W = sum((p * h for p, h in zip(PS, H_terms)), sp.zeros(2))
    verify(sp.expand(H_W * H_W - (P1**2 + P2**2 + P3**2) * sp.eye(2)) == sp.zeros(2),
           "H_W^2 = |p|^2 I: eigenvalues +-|p|, c_IR = 1")
    f = c1 * c2 * c3
    verify(is_zero(S.trace() / 2 - f) and zero_matrix(S * S - 2 * f * S + sp.eye(2)),
           "tr S/2 = c1 c2 c3 and Cayley-Hamilton S^2 = 2 f S - I")

    # Concavity of u -> log cos(sqrt u) on (0, (pi/2)^2) gives prod cos p_i >= cos|p|.
    u, t = sp.symbols("u t", positive=True)
    h2 = sp.diff(sp.log(sp.cos(sp.sqrt(u))), u, 2).subs(u, t**2)
    verify(sp.simplify(h2 + (2*t - sp.sin(2*t)) / (8 * t**3 * sp.cos(t)**2)) == 0
           and sp.simplify(sp.diff(2*t - sp.sin(2*t), t) - 4 * sp.sin(t)**2) == 0
           and (2*t - sp.sin(2*t)).subs(t, 0) == 0,
           "h''(u) = -(2t - sin 2t)/(8t^3 cos^2 t), (2t - sin 2t)' = 4 sin^2 t, zero at t=0 => h concave")
    verify(sp.simplify(2 * sp.cos(t)**2 - 1 - sp.cos(2*t)) == 0,
           "2cos^2 t - 1 = cos 2t (with concavity: 2 prod c_i^2 - 1 >= cos 2|p| > 0 on |p|<pi/4)")
    a, b, c = sp.symbols("a b c", nonnegative=True)
    verify(sp.expand((1-a)*(1-b)*(1-c) - (1-a-b-c) - (a*b + b*c + c*a - a*b*c)) == 0,
           "(1-a)(1-b)(1-c) = 1-a-b-c + ab+bc+ca-abc (elementary route on |p|<=1/sqrt2)")

    # ------------------------------------------ step 1: pre-choice IR control
    kappa = ball_integral(lambda r: 1)
    verify(sp.simplify(kappa - LAM**3 / (6 * sp.pi**2)) == 0,
           "ball measure kappa(L) = L^3/(6 pi^2): in-band share of any one-site vector")
    q = sp.symbols("q", nonnegative=True)
    g = (1 - q**2)**2
    verify(g.subs(q, 1) == 0 and sp.diff(g, q).subs(q, 1) == 0,
           "envelope g vanishes to first order at |q| = 1 (smoothed compact edge)")
    Z = ball_integral(lambda r: g.subs(q, r / LAM)**2)
    I_g = ball_integral(lambda r: g.subs(q, r / LAM))
    verify(sp.simplify(Z - 64 * LAM**3 / (3465 * sp.pi**2)) == 0
           and sp.simplify(I_g - 4 * LAM**3 / (105 * sp.pi**2)) == 0,
           "Z_Lambda = 64 L^3/(3465 pi^2), int g(p/L) dmu = 4 L^3/(105 pi^2)")
    s_max = sp.simplify(I_g**2 / Z)
    verify(sp.simplify(s_max - sp.Rational(11, 140) * LAM**3 / sp.pi**2) == 0
           and sp.Rational(11, 140) < sp.Rational(1, 6),
           "(int g)^2/Z = 11 L^3/(140 pi^2) < kappa")

    x, tt = sp.symbols("x t", real=True)
    verify(sp.simplify(sp.integrate((x - tt) * sp.exp(sp.I * tt), (tt, 0, x))
                       + (sp.exp(sp.I * x) - 1 - sp.I * x)) == 0
           and sp.simplify(sp.integrate((x - tt) * sp.cos(tt), (tt, 0, x))
                           + (sp.cos(x) - 1)) == 0
           and sp.simplify(sp.integrate((x - tt)**2 / 2 * sp.cos(tt), (tt, 0, x))
                           + (sp.sin(x) - x)) == 0,
           "Taylor integral remainders of e^{ix}, cos x, sin x (=> x^2/2, x^2/2, |x|^3/6)")
    E = W - sp.eye(2) - sp.I * H_W
    decomposition = sp.Matrix([
        [(c1*c2 - 1) * sp.exp(sp.I*P3) + (sp.exp(sp.I*P3) - 1 - sp.I*P3),
         -(c1 - 1) * s2 - (s2 - P2) + sp.I * (s1 - P1)],
        [(c1 - 1) * s2 + (s2 - P2) + sp.I * (s1 - P1),
         (c1*c2 - 1) * sp.exp(-sp.I*P3) + (sp.exp(-sp.I*P3) - 1 + sp.I*P3)],
    ])
    verify(zero_matrix(E - decomposition) and is_zero((c1*c2 - 1) - (c2*(c1 - 1) + (c2 - 1))),
           "W - I - iH_W decomposes entrywise into those remainders (bounds: report Sec. 3)")
    A, B = sp.symbols("A B", commutative=False)
    verify(sp.expand(A**2 - B**2 - (A*(A - B) + (A - B)*B)) == 0
           and sp.expand(A**3 - B**3 - (A**2*(A - B) + A*(A - B)*B + (A - B)*B**2)) == 0,
           "telescoping identities S^j - V^j, j = 2, 3 (=> <= j ||S - V|| for unitaries)")
    R_W = 3 * LAM**2 * (sp.Rational(1, 2) + sp.sqrt(sp.Rational(1, 2) + sp.Rational(25, 18) * LAM**2))
    verify(sp.limit(R_W, LAM, 0, "+") == 0,
           "R_W(L) = 3L^2(1/2 + sqrt(1/2 + 25L^2/18)) -> 0 (r_W <= R_W: report Sec. 3)")
    xx = sp.symbols("x", real=True)
    verify(sp.integrate(xx**4 * (1 - xx)**4 / (1 + xx**2), (xx, 0, 1)) == sp.Rational(22, 7) - sp.pi,
           "Dalzell: 22/7 - pi = int_0^1 x^4(1-x)^4/(1+x^2) dx > 0, so pi < 22/7")
    verify(sp.Rational(1, 2) + sp.Rational(25, 18) * (sp.Rational(22, 7) / 4)**2 < sp.Rational(7, 6)**2,
           "on the chart L < pi/4 < 11/14: sqrt(1/2 + 25L^2/18) < 7/6, hence R_W(L) < 5 L^2")

    # --------------------------------------------- step 2: encoded difference
    down = sp.Matrix([0, 1])
    column = S * S * down
    upper = 2 * c1**2 * c2 * c3 * s2 - 2 * sp.I * f * s1
    lower_even = 2 * c1**2 * c2**2 * c3**2 - 1
    lower_odd = 2 * c1**2 * c2**2 * c3 * s3
    verify(is_zero(column[0] - upper) and is_zero(column[1] - lower_even - sp.I * lower_odd),
           "S^2|down>: upper = 2c1^2c2c3 s2 - 2i f s1, lower = (2 prod c^2 - 1) + 2i c1^2c2^2c3 s3")
    odd_p2 = 2 * c1**2 * c2 * c3 * s2
    odd_p1 = -2 * sp.I * f * s1
    verify(sp.expand(odd_p2.subs(P2, -P2) + odd_p2) == 0
           and sp.expand(odd_p1.subs(P1, -P1) + odd_p1) == 0
           and sp.expand(lower_odd.subs(P3, -P3) + lower_odd) == 0
           and all(sp.expand(lower_even.subs(p, -p) - lower_even) == 0 for p in PS),
           "parity: upper parts odd in p2 / p1, Im lower odd in p3, Re lower even (radial g kills odd parts)")
    verify(sp.limit(sp.cos(2*LAM), LAM, 0, "+") == 1 and sp.limit(s_max, LAM, 0, "+") == 0,
           "cos 2L -> 1 and 11L^3/(140pi^2) -> 0 (two-sided bounds on s: report Sec. 4)")

    # Faithful model: Delta, L, R live on V = span{psi, Pi e, (I-Pi) e}, which Pi
    # preserves; the Gram data below fix them up to a unitary on V.
    s, k = sp.symbols("s kappa", positive=True)
    psi = sp.Matrix([sp.sqrt(s / k), sp.sqrt(1 - s / k), 0])
    e_in = sp.Matrix([sp.sqrt(s * k), 0, 0])
    e_out = sp.Matrix([0, 0, sp.sqrt(s * (1 - k))])
    e = e_in + e_out
    Pi = sp.diag(1, 1, 0)
    gram = sp.Matrix(3, 3, lambda i, j: sp.expand(([psi, e_in, e_out][i].T * [psi, e_in, e_out][j])[0]))
    verify((gram - sp.Matrix([[1, s, 0], [s, s * k, 0], [0, 0, s * (1 - k)]])).applyfunc(sp.expand)
           == sp.zeros(3)
           and Pi * psi == psi and Pi * e_in == e_in and Pi * e_out == sp.zeros(3, 1),
           "model Gram data: <psi|psi>=1, <psi|Pi e>=s, ||Pi e||^2=s kappa, ||(I-Pi)e||^2=s(1-kappa)")
    psi1 = psi - 2 * e
    Delta = (psi1 * psi1.T - psi * psi.T).applyfunc(sp.expand)
    L = (Pi * Delta * Pi).applyfunc(sp.expand)
    R = (Delta - L).applyfunc(sp.expand)
    verify(all(sp.simplify(X.det()) == 0 for X in (Delta, L, R)),
           "det = 0 for Delta, L = Pi Delta Pi and R = Delta - L on V (rank <= 2)")
    nD2, e2D = trace_norm_rank2(Delta)
    nL2, e2L = trace_norm_rank2(L)
    nR2, e2R = trace_norm_rank2(R)
    verify(sp.simplify(e2D + 4*s*(1 - s)) == 0
           and sp.simplify(e2L + 4*s*(k - s)) == 0
           and sp.simplify(e2R + 4*s*(1 - k)*(1 - 4*s*(1 - k))) == 0,
           "e2 = -4s(1-s), -4s(kappa-s), -4s(1-kappa)(1-4s(1-kappa)): all <= 0 for 0<s<=kappa<1/4")
    verify(sp.simplify(nD2 - 16*s*(1 - s)) == 0,
           "||Delta||_1^2 = 16 s(1-s) (> 0 as 0<s<1: Delta = 0 convention not triggered)")
    verify(sp.simplify(nR2 - 16*s*(1 - k)*(1 - 3*s*(1 - k))) == 0,
           "||R||_1^2 = 16 s(1-kappa)(1-3s(1-kappa))")
    verify(sp.simplify(nL2 - 16*(s**2*(1 - k)**2 + s*(k - s))) == 0,
           "||L||_1^2 = 16 (s^2(1-kappa)^2 + s(kappa-s))")
    verify(sp.expand(((psi1 - Pi * psi1).T * (psi1 - Pi * psi1))[0] - 4*s*(1 - k)) == 0
           and sp.limit(4 * s_max, LAM, 0, "+") == 0,
           "eps_1(0,L) = ||(I-Pi)U_1 psi||^2 = 4s(1-kappa), and 11L^3/(35pi^2) -> 0")

    eta2 = (1 - k) * (1 - 3*s*(1 - k)) / (1 - s)
    verify(sp.simplify(nR2 / nD2 - eta2) == 0,
           "eta_enc^2 = (1-kappa)(1-3s(1-kappa))/(1-s)")
    floor = (1 - k) * (1 - 3*k)
    verify(sp.simplify((1 - eta2) - (k - s + 3*s*(1 - k)**2) / (1 - s)) == 0
           and sp.simplify((eta2 - floor)
                           - (3*(1 - k)*(k - s*(1 - k)) + s*floor) / (1 - s)) == 0,
           "1 - eta^2 and eta^2 - (1-kappa)(1-3kappa) have numerators >= 0 for 0<s<=kappa<1/3")
    verify(sp.simplify(nL2 / nD2 - (s*(1 - k)**2 + k - s) / (1 - s)) == 0,
           "||L||_1^2/||Delta||_1^2 = (s(1-kappa)^2 + kappa - s)/(1-s) (<= kappa/(1-kappa))")
    k_chart = sp.Rational(22, 7) / 384
    verify(k_chart == sp.Rational(11, 1344)
           and sp.expand(sp.diff(floor, k)) == 6*k - 4
           and floor.subs(k, k_chart) > sp.Rational(24, 25),
           "floor decreasing for kappa<2/3 and floor(11/1344) > 24/25: eta_enc > 2sqrt(6)/5 on chart")
    floor_L = floor.subs(k, kappa)
    verify(sp.limit(floor_L, LAM, 0, "+") == 1 and sp.limit(kappa, LAM, 0, "+") == 0,
           "floor(kappa(L)) -> 1: squeeze gives eta_enc(L) -> 1, never -> 0 near L = 0")

    print(f"\n{CHECKS}/{CHECKS} exact checks passed.")
    print("Sec. 6 absolute control: eps_pre = 0, eps_UV -> 0, R_W -> 0 (holds, not sufficient).")
    print("Sec. 7 relative control: eta_enc -> 1. STOP RULE: FAIL.")
    print("Verdict: NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS "
          "(reason: encoder incompatible with the IR criterion). D_B not computed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:                            # fail closed
        print(f"[FAIL] {exc!r}")
        sys.exit(1)
