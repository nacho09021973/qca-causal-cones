#!/usr/bin/env python3
"""Reproducible certificate for the BCC s=4 family A_{a,theta}.

SymPy-only, zero tolerance. The accompanying analytic note carries the all-
parameter proofs; this script supplies exact algebraic spot checks of the
construction, the original six-point a panel, irreducibility, Weyl slope, and
the theta-deformed quantum-metric sum rule.
"""

from itertools import product
import sympy as sp

I = sp.I
SQRT3 = sp.sqrt(3)
I2 = sp.eye(2)
I4 = sp.eye(4)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = (SX, SY, SZ)


def kron(a, b):
    return sp.kronecker_product(a, b)


def dagger(m):
    return m.conjugate().T


def zmat(m):
    return all(sp.simplify(sp.expand_complex(x)) == 0 for x in m)


def core(a, theta):
    b = sp.sqrt(1 - a**2)
    ts = (
        b * SX + a * SZ,
        b * SY + a * SZ,
        -b * SX + a * SZ,
    )
    gammas = tuple(kron(s, t) for s, t in zip(PAULI, ts))
    wt = sp.diag(sp.cos(theta) - I * sp.sin(theta),
                 sp.cos(theta) + I * sp.sin(theta))
    w = kron(I2, wt)
    rs = tuple(kron(s, I2) for s in PAULI)
    return b, w, ts, gammas, rs


def coefficients(a, theta):
    b, w, ts, gammas, rs = core(a, theta)
    coeffs = {}
    for signs in product((1, -1), repeat=3):
        m = w
        for sign, gamma in zip(signs, gammas):
            m = m * (I4 + sign * gamma) / 2
        coeffs[signs] = m
    return b, w, ts, gammas, rs, coeffs


def vec(m):
    return sp.Matrix([m[r, c] for c in range(m.cols) for r in range(m.rows)])


def commutant_nullity(mats):
    basis = []
    for c in range(4):
        for r in range(4):
            e = sp.zeros(4)
            e[r, c] = 1
            basis.append(e)
    blocks = []
    for a in mats:
        blocks.append(sp.Matrix.hstack(*(vec(e*a-a*e) for e in basis)))
    return 16 - sp.Matrix.vstack(*blocks).rank()


def structural_check():
    a = sp.Rational(1, 2)
    theta = sp.pi / 4
    b, w, ts, gammas, rs, coeffs = coefficients(a, theta)

    for t in ts:
        assert zmat(dagger(t) - t)
        assert zmat(t*t - I2)
    for gamma in gammas:
        assert zmat(dagger(gamma) - gamma)
        assert zmat(gamma*gamma - I4)
    assert zmat(w*dagger(w)-I4)

    assert len(coeffs) == 8 and (0, 0, 0) not in coeffs
    total = sum(coeffs.values(), sp.zeros(4))
    assert zmat(total-w)

    transforms = (
        lambda s: (s[0], -s[1], -s[2]),
        lambda s: (-s[0], s[1], -s[2]),
        lambda s: (-s[0], -s[1], s[2]),
    )
    for rmat, tfm in zip(rs, transforms):
        for signs, ah in coeffs.items():
            assert zmat(rmat*ah*dagger(rmat)-coeffs[tfm(signs)])

    # If X commutes with every A_h, it commutes with W=sum A_h and with
    # W Gamma_i=sum s_i A_h. Hence scalar commutant of {W,Gamma_i} is enough.
    for axis, gamma in enumerate(gammas):
        weighted = sp.zeros(4)
        for signs, ah in coeffs.items():
            weighted += signs[axis] * ah
        assert zmat(weighted-w*gamma)
    assert commutant_nullity([w, *gammas]) == 1

    # Exact Weyl projection P_+ Gamma_i P_+ = a sigma_i on tau_z=+.
    p_tau = sp.diag(1, 0)
    p = kron(I2, p_tau)
    for sigma, gamma in zip(PAULI, gammas):
        assert zmat(p*gamma*p - a*kron(sigma, p_tau))


def original_a_panel_check():
    panel = (
        sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(1, 2),
        1/sp.sqrt(2), sp.Rational(4, 5), sp.Rational(99, 100),
    )
    theta = sp.pi / 4
    for a in panel:
        b, w, ts, gammas, rs, coeffs = coefficients(a, theta)
        for signs, ah in coeffs.items():
            parity = signs[0]*signs[1]*signs[2]
            expected = sp.sqrt(2)/4 * (1 + parity*a*(2*a**2-1))
            tr = sp.trace(ah)
            assert sp.simplify(sp.expand_complex(tr-expected)) == 0
            assert sp.simplify(expected) != 0
        assert commutant_nullity([w, *gammas]) == 1


def theta_metric_check():
    # The all-theta identity is proved in the note. Verify exact representative
    # points with independently variable theta.
    a = sp.Rational(1, 2)
    for theta in (sp.pi/6, sp.pi/4, sp.pi/3):
        b, w, ts, gammas, rs = core(a, theta)
        p = kron(I2, sp.diag(1, 0))
        q = I4-p
        lp = sp.cos(theta)-I*sp.sin(theta)
        lm = sp.cos(theta)+I*sp.sin(theta)
        gap_sq = sp.simplify((lp-lm)*sp.conjugate(lp-lm))
        assert sp.simplify(gap_sq-4*sp.sin(theta)**2) == 0
        for gamma in gammas:
            du = -I*w*gamma/SQRT3
            k = q*du*p/(lp-lm)
            gii = sp.simplify(sp.expand_complex(sp.trace(dagger(k)*k)))
            expected_g = sp.simplify(b**2/(6*sp.sin(theta)**2))
            assert sp.simplify(gii-expected_g) == 0
            lhs = sp.simplify(a**2/3 + 2*sp.sin(theta)**2*gii)
            assert sp.simplify(lhs-sp.Rational(1, 3)) == 0


def main():
    structural_check()
    original_a_panel_check()
    theta_metric_check()
    print('S4_STRICT_CONE_COUNTEREXAMPLE_CERTIFICATE: PASS')
    print('a_panel=1/5,2/5,1/2,1/sqrt(2),4/5,99/100')
    print('theta_panel=pi/6,pi/4,pi/3 at a=1/2')
    print('backend=sympy_exact')
    print('tolerance=0')


if __name__ == '__main__':
    main()
