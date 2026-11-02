"""Exact algebra for the preregistered small Gaussian profile gate.

Run from repo root using Python with SymPy 1.14.0. This verifies Gaussian
Fourier moments, the exact resource L1 constant, channel parity, a formal
three-step noncommuting expansion (not lattice evolution or an N scan),
the positive Hessian factorization, geometric sums and exponent bookkeeping.
It does NOT certify analytic kernel bounds, uniform remainders, sign survival,
or any nonzero quadratic/asymptotic coefficient. Those are report proofs.
"""

import hashlib
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CHARTER_SHA = "d739db6b4b476c79c4a51d9a26f0dcf03dda31b5c3d818b8b0d040f6e972cddd"
CHECKS = 0


def require(condition, label):
    global CHECKS
    if condition is not True and condition is not sp.true:
        raise AssertionError(label)
    CHECKS += 1
    print(f"[PASS] {label}")


def zero(expr):
    return sp.expand(expr) == 0


def main():
    require(sp.__version__ == "1.14.0", "SymPy version 1.14.0")
    charter = ROOT / "theory/H1_SMALL_GAUSSIAN_PROFILE_GATE.md"
    require(hashlib.sha256(charter.read_bytes()).hexdigest() == CHARTER_SHA,
            "corrected pre-execution contract SHA256")
    r = sp.symbols("r", positive=True)
    radial = sp.pi ** sp.Rational(3, 2) * 4 * sp.pi / (2 * sp.pi) ** 3
    a0 = sp.simplify(radial * sp.integrate(r**2 * sp.exp(-r**2 / 4), (r, 0, sp.oo)))
    a1 = sp.simplify(radial * sp.integrate(r**3 * sp.exp(-r**2 / 4), (r, 0, sp.oo)))
    require(a0 == 1, "Gaussian Fourier mass a0=1")
    require(a1 == 4 / sp.sqrt(sp.pi), "Gaussian Fourier first moment a1=4/sqrt(pi)")
    k, x = sp.symbols("k x", real=True)
    one_dim = sp.integrate(sp.exp(-k**2 / 4) * sp.exp(-sp.I * k * x),
                           (k, -sp.oo, sp.oo)) / (2 * sp.sqrt(sp.pi))
    require(sp.simplify(one_dim - sp.exp(-x**2)) == 0,
            "one-dimensional Gaussian Fourier convention")
    ball_g = sp.integrate(4 * sp.pi * r**2 * (1 - r**2)**2, (r, 0, 1))
    resource_l1 = sp.simplify(ball_g / (2 * sp.pi)**3 * sp.sqrt(3465 * sp.pi**2 / 64))
    require(resource_l1 == sp.sqrt(3465) / (210 * sp.pi),
            "exact C_phi for ||phi_hat||_1=C_phi N^-3/2")

    z = sp.diag(1, -1)
    beta = sp.Matrix([[0, 1], [1, 0]])
    require(z * beta * z == -beta, "channel Z beta Z=-beta")
    S, V = sp.symbols("S V", commutative=False)
    D = sp.diag(S, S**-1)
    require(z * D * z == D, "channel Z D Z=D for generic invertible S")

    # One formal three-step operator identity, keeping all factors ordered.
    # This is not a simulation, finite-size diagnostic or asymptotic test.
    e = sp.symbols("epsilon", real=True)
    steps = 3
    C = sp.Matrix([[1 - e**2 * V**2 / (2 * steps**2), -sp.I * e * V / steps],
                   [-sp.I * e * V / steps, 1 - e**2 * V**2 / (2 * steps**2)]])
    evolved = (C * D) ** steps
    plus = sp.expand(evolved[0, 0])
    require(zero(plus.coeff(e, 0) - S**steps), "free plus channel equals S^3")
    require(plus.coeff(e, 1) == 0, "linear plus-channel coefficient vanishes")
    require(plus.coeff(e, 3) == 0, "odd plus-channel cubic coefficient vanishes")
    same = -sum(S**(steps-1-j) * V**2 * S**(j+1) for j in range(steps)) / (2 * steps**2)
    distinct = -sum(S**(steps-1-l) * V * S**(-(l-j)) * V * S**(j+1)
                    for j in range(steps) for l in range(j+1, steps)) / steps**2
    require(zero(plus.coeff(e, 2) - same - distinct),
            "quadratic coefficient includes same-coin and ordered two-time terms")
    require(not zero(plus.coeff(e, 2) - distinct),
            "negative control: dropping same-coin insertions fails")
    minus = sp.expand(evolved[1, 0])
    first_minus = -sp.I * sum(S**(-(steps-1-j)) * V * S**(j+1)
                              for j in range(steps)) / steps
    require(zero(minus.coeff(e, 1) - first_minus),
            "first minus-channel insertion has correct inverse evolution")

    n = sp.symbols("N", integer=True, positive=True)
    t = sp.symbols("t")
    require(sp.diff(sp.exp(n * t), t, 2).subs(t, 0) / (2 * n**2) == sp.Rational(1, 2),
            "multinomial coefficient majorant at second order is 1/2")
    c = sp.symbols("c")
    require(zero(c**6 - 3*c**2 + 2 - (c**2-1)**2 * (c**2+2)),
            "normal Hessian numerator factors positively for c>1")
    q = sp.symbols("q", positive=True)
    s2 = sp.diff(q / (1-q), q)
    require(sp.simplify(s2 - (1+q) / (1-q)**3) != 0,
            "negative control: one derivative is not the square-moment series")
    actual_s2 = sp.diff(q * sp.diff(q / (1-q), q), q)
    actual_s3 = sp.diff(q * actual_s2, q)
    require(sp.simplify(actual_s2 - (1+q)/(1-q)**3) == 0,
            "sum_(j>=0) (j+1)^2 q^j=(1+q)/(1-q)^3")
    require(sp.simplify(actual_s3 - (1+4*q+q**2)/(1-q)**4) == 0,
            "sum_(j>=0) (j+1)^3 q^j=(1+4q+q^2)/(1-q)^4")
    require(-sp.Rational(5, 2) * 2 - sp.Rational(3, 2) == -sp.Rational(13, 2),
            "two layer L1 masses and kernel L1 give power 13/2")
    require(-7 + sp.Rational(13, 2) == -sp.Rational(1, 2),
            "uniform bridge error has relative power N^-1/2")
    print(f"PASS: {CHECKS} exact algebra checks; analytic survival proof remains unreviewed.")


if __name__ == "__main__":
    main()
