"""Exact algebra for reports/2026-09-22--ir-projection-leakage-and-conditioning.md.

Does not certify Fourier/Poisson remainder estimates, Lpp asymptotics,
independent review, or canonical promotion. No numerical N scan.
Run: python3 -B scripts/verify_ir_projection_leakage.py
Requires sympy (verified with 1.14.0).
"""

import sys

import sympy as sp


def main():
    checks = 0

    def equal(actual, expected, label):
        nonlocal checks
        difference = actual - expected
        entries = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
        if any(sp.simplify(entry) != 0 for entry in entries):
            raise AssertionError(label)
        checks += 1
        print(f"[PASS] {label}")

    q, z = sp.symbols("q z", real=True)
    off = sp.sqrt(q * (1 - q))
    error = sp.Matrix([[0, off], [off, q]])
    equal(error.trace(), q, "discarded operator trace q; compressed trace -q")
    equal((z * sp.eye(2) - error).det(), z**2 - q*z - q*(1-q),
          "rank-two characteristic polynomial")
    disc = 4*q - 3*q**2
    for sign in (-1, 1):
        eigenvalue = (q + sign * sp.sqrt(disc)) / 2
        equal(eigenvalue**2 - q*eigenvalue - q*(1-q), 0,
              f"eigenvalue sign {sign}")

    lpp, p0 = sp.symbols("Lpp p0", real=True)
    conditional = (lpp + p0) / (1-q) - p0
    equal(conditional, (lpp + q*p0)/(1-q), "conditional signed signal")
    equal(conditional-lpp, q*(p0+lpp)/(1-q), "normalization correction")

    t = sp.symbols("t", real=True)
    B, B1, B2 = sp.symbols("B B1 B2", real=True)
    radius = sp.Rational(1, 4)
    F = (1 - 16*(radius-t)**2)**2
    equal(sp.expand(F).coeff(t, 2), 64, "quadratic profile at Alice boundary")
    phase = sp.pi*F/2
    sine = sp.series(sp.sin(phase), t, 0, 5).removeO()
    cosine_minus_one = sp.series(sp.cos(phase)-1, t, 0, 5).removeO()
    equal(cosine_minus_one.coeff(t, 4), -512*sp.pi**2,
          "cosine term first appears at fourth order")
    chi = sp.Matrix([0, 1])
    encoders = {
        "I": sp.eye(2),
        "sigma1": sp.Matrix([[0, 1], [1, 0]]),
        "sigma2": sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        "sigma3": sp.diag(1, -1),
    }
    for name, M in encoders.items():
        source = (B+B1*t+B2*t**2) * (cosine_minus_one*chi + sp.I*sine*M*chi)
        coefficient = source.applyfunc(lambda entry: sp.expand(entry).coeff(t, 2))
        equal(coefficient, sp.I*32*sp.pi*B*M*chi, f"source boundary: {name}")
        equal(2*radius*coefficient, sp.I*16*sp.pi*B*M*chi,
              f"radial h second boundary derivative: {name}")
        equal((M*chi).H*(M*chi), sp.ones(1, 1), f"unit boundary spinor: {name}")

    k, r = sp.symbols("k r", positive=True)
    # Independent exact radial transform of the polynomial profile fixes
    # the integration-by-parts sign and all Fourier normalization factors.
    radial = 4*sp.pi/k * sp.integrate(r*(1-16*r**2)**2*sp.sin(k*r), (r, 0, radius))
    expected = (128*sp.pi*sp.cos(k/4)/k**4
                -3072*sp.pi*sp.sin(k/4)/k**5
                -30720*sp.pi*sp.cos(k/4)/k**6
                +122880*sp.pi*sp.sin(k/4)/k**7)
    equal(radial, expected, "exact radial profile transform and leading sign")
    equal(128*sp.pi * sp.pi*B/2, 64*sp.pi**2*B,
          "encoder transform leading coefficient")
    equal(4*sp.pi/(2*sp.pi)**3 * (64*sp.pi**2*B)**2 / 10,
          1024*sp.pi**2*B**2/5, "positive tail constant D")
    equal(sp.Rational(13, 2)-sp.Rational(5, 4), sp.Rational(21, 4),
          "trace error to total signal power")

    lam = sp.symbols("lambda", positive=True)
    kernel = sp.integrate(k*sp.sin(k*r), (k, 0, lam))/(2*sp.pi**2*r)
    target = (sp.sin(lam*r)-lam*r*sp.cos(lam*r))/(2*sp.pi**2*r**3)
    equal(kernel, target, "sharp ball projector kernel")
    equal(sp.limit(kernel, r, 0), lam**3/(6*sp.pi**2), "projector diagonal")
    n, s = sp.symbols("N s", positive=True)
    equal(target.subs({lam: 1/sp.sqrt(n), r: s*n}),
          -sp.cos(s*sp.sqrt(n))/(2*sp.pi**2*s**2*n**sp.Rational(5, 2))
          +sp.sin(s*sp.sqrt(n))/(2*sp.pi**2*s**3*n**3),
          "projector at distance sN")
    print(f"PASS: {checks} exact algebra checks; analytic remainders UNREVIEWED.")
    print(f"Python {sys.version.split()[0]}; SymPy {sp.__version__}")


if __name__ == "__main__":
    main()
