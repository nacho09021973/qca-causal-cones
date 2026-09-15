#!/usr/bin/env python3
"""Independent symbolic review of commit 1dae941 (no certificate imports).

Frozen checks: both Laurent unitarity identities at every difference,
D2 covariance, general trace, both Weyl blocks, projector differential
equations, full metric tensor and weighted identity. All checks are exact
polynomial identities on a^2+b^2=c^2+d^2=1, with d != 0 for projectors.
The report supplies the open-domain inequalities and commutant proof.
"""

from itertools import product
import sympy as sp

a, b, c, d = sp.symbols("a b c d", real=True)
eye2, eye4 = sp.eye(2), sp.eye(4)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.diag(1, -1)
pauli = (sx, sy, sz)
checks = 0


def reduced(expr):
    """Reduce modulo b^2=1-a^2 and c^2=1-d^2; no sampling."""
    poly = sp.Poly(sp.expand(expr), a, b, c, d)
    return sp.expand(sum(
        coeff * a**ia * b**(ib % 2) * (1-a*a)**(ib // 2)
        * c**(ic % 2) * (1-d*d)**(ic // 2) * d**idd
        for (ia, ib, ic, idd), coeff in poly.terms()
    ))


def matrix_reduced(matrix):
    return matrix.applyfunc(reduced)


def require_zero(matrix, label):
    global checks
    if any(reduced(entry) != 0 for entry in matrix):
        raise AssertionError(label)
    checks += 1


def main():
    # c=cos(theta), d=sin(theta). Build coefficients directly as polynomials.
    tau = (b*sx+a*sz, b*sy+a*sz, -b*sx+a*sz)
    gamma = tuple(sp.kronecker_product(s, t) for s, t in zip(pauli, tau))
    w = sp.kronecker_product(eye2, c*eye2-sp.I*d*sz)
    signs = tuple(product((-1, 1), repeat=3))
    coeff = {}
    for h in signs:
        value = w
        for hi, gi in zip(h, gamma):
            value = matrix_reduced(value*(eye4+hi*gi)/2)
        coeff[h] = value

    # This checks convolution of actual coefficients, rather than relying
    # on a product-of-unitaries assertion or testing momenta on a mesh.
    right, left = {}, {}
    for h in signs:
        for hp in signs:
            ell = tuple(v-u for u, v in zip(h, hp))
            right.setdefault(ell, sp.zeros(4))
            left.setdefault(ell, sp.zeros(4))
            right[ell] += coeff[h].H*coeff[hp]
            left[ell] += coeff[hp]*coeff[h].H
    for ell in right:
        target = eye4 if ell == (0, 0, 0) else sp.zeros(4)
        require_zero(right[ell]-target, f"UdagU at {ell}")
        require_zero(left[ell]-target, f"UUdag at {ell}")
    print("both_fourier_unitarity_identities: PASS (27 differences each)", flush=True)

    require_zero(sum(coeff.values(), sp.zeros(4))-w, "zero momentum")
    for axis, sigma in enumerate(pauli):
        weighted = sum((h[axis]*coeff[h] for h in signs), sp.zeros(4))
        require_zero(weighted-w*gamma[axis], "signed coefficient moment")
        rotation = sp.kronecker_product(sigma, eye2)
        for h in signs:
            rotated = tuple(hi if j == axis else -hi for j, hi in enumerate(h))
            require_zero(rotation*coeff[h]*rotation.H-coeff[rotated], "D2")
    for h in signs:
        parity = h[0]*h[1]*h[2]
        expected = (c+parity*a*(d-2*b*b*c))/2
        require_zero(sp.Matrix([sp.trace(coeff[h])-expected]), "general trace")
    print("covariance_moments_and_all_parameter_trace: PASS", flush=True)

    p = sp.kronecker_product(eye2, sp.diag(1, 0))
    q = eye4-p
    differential_scaled = []
    for sigma, gi in zip(pauli, gamma):
        require_zero(p*gi*p-a*sp.kronecker_product(sigma, sp.diag(1, 0)), "plus Weyl")
        require_zero(q*gi*q+a*sp.kronecker_product(sigma, sp.diag(0, 1)), "minus Weyl")
        # J = d * partial_k P: polynomial even though partial_k P has 1/d.
        # Obtain it from the off-block differentiated [U,P]=0 equation.
        lower = q*w*gi*p/(2*sp.sqrt(3))
        j = lower+lower.H
        du = -sp.I*w*gi/sp.sqrt(3)
        require_zero(p*j+j*p-j, "differentiated P^2=P")
        require_zero(j-j.H, "projector derivative Hermiticity")
        require_zero(w*j-j*w+d*(du*p-p*du), "differentiated [U,P]=0")
        differential_scaled.append(j)

    for i in range(3):
        for j in range(3):
            # d^2*g_ij = Tr(J_i J_j)/2; no band metric substituted.
            metric_scaled = sp.trace(differential_scaled[i]*differential_scaled[j])/2
            target = b*b/6 if i == j else 0
            require_zero(sp.Matrix([metric_scaled-target]), f"metric {i},{j}")
            if i == j:
                require_zero(sp.Matrix([a*a/3+2*metric_scaled-sp.Rational(1, 3)]), "sum rule")
    print("both_weyl_blocks_projector_equations_and_full_metric: PASS", flush=True)
    print("S4_INDEPENDENT_SYMBOLIC_REVIEW: PASS")
    print(f"matrix_or_scalar_identities={checks}")
    print(f"sympy={sp.__version__}; tolerance=0; parameter_sampling=none")


if __name__ == "__main__":
    main()
