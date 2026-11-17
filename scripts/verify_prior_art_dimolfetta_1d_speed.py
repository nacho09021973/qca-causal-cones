#!/usr/bin/env python3
"""Prior-art check: Di Molfetta-Arrighi plastic walk, massless alpha=0 case.

Source: G. Di Molfetta, P. Arrighi, arXiv:1906.04483v2, Eq. (1)-(3) and
Theorem III.1 case (iii). With m=0 and alpha=0: kappa=1, theta=arccos(c),
zeta=0, so the rule does not depend on epsilon. One step is S C with
C = -c sigma_z + sqrt(1-c^2) sigma_x and S = diag(e^{ik}, e^{-ik})
(nearest-neighbour shifts; the paper's W is Lambda^{-1} (S C)^2 Lambda,
and constant conjugation by Lambda changes neither spectrum nor support).

Checks, exact SymPy, for symbolic 0 < c < 1:
  1. C and U(k) = S C are unitary.
  2. det U^2 = 1 and tr U^2 = 2 (1 - 2 c^2 sin^2 k), hence the two-step
     eigenphases satisfy cos Omega = 1 - 2 c^2 sin^2 k (massless node at k=0).
  3. 1 - 2 c^2 sin^2 k - cos(2 c k) = O(k^4): two-step slope 2c, i.e. the
     low-energy speed is c per step.
  4. With U = e^{ik} A_+ + e^{-ik} A_-, A_+^2 = -c A_+ and A_-^2 = c A_-, so
     the extreme coefficients A_+^n, A_-^n of U^n are nonzero for c > 0:
     exact support {-n, ..., n} extremes attained, strict causal body = [-1,1].

Run 1 (2026-11-17) failed only the two unitarity checks: sqrt(1-c^2) was not known
real; s is now a positive symbol with s^2 = 1 - c^2 imposed. No expectation
changed.

Does not certify: anything beyond this one-dimensional walk; whether the walk
lies in D'Ariano-Perinotti's isotropy class; any statement of the source
paper other than the equations used above. Fails closed.
"""
import sys

import sympy as sp

c = sp.symbols("c", positive=True)
k = sp.symbols("k", real=True)
s = sp.symbols("s", positive=True)  # s = sqrt(1 - c^2), imposed via red()
sx = sp.Matrix([[0, 1], [1, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
C = -c * sz + s * sx
S = sp.diag(sp.exp(sp.I * k), sp.exp(-sp.I * k))
U = S * C
Pp = sp.diag(1, 0)
Pm = sp.diag(0, 1)
Ap = Pp * C
Am = Pm * C

checks = []


def check(name, expr_is_zero):
    ok = bool(expr_is_zero)
    checks.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)


def red(e):
    return sp.simplify(sp.expand(e).subs(s**2, 1 - c**2))


def zero(m):
    if hasattr(m, "shape"):
        return m.applyfunc(red) == sp.zeros(*m.shape)
    return red(m) == 0


try:
    check("C unitary", zero(C * C.H - I2))
    check("U(k) unitary", zero(sp.simplify(U * U.H) - I2))
    U2 = U * U
    check("det U^2 = 1", zero(sp.simplify(U2.det()) - 1))
    tr = sp.simplify(sp.expand(U2.trace().rewrite(sp.cos)))
    check("tr U^2 = 2(1 - 2 c^2 sin^2 k)",
          zero(sp.simplify(tr - 2 * (1 - 2 * c**2 * sp.sin(k) ** 2))))
    ser = sp.series(1 - 2 * c**2 * sp.sin(k) ** 2 - sp.cos(2 * c * k), k, 0, 4).removeO()
    check("cos Omega - cos(2ck) = O(k^4)", zero(sp.expand(ser)))
    check("U = e^{ik} A_+ + e^{-ik} A_-",
          zero(sp.simplify(U - sp.exp(sp.I * k) * Ap - sp.exp(-sp.I * k) * Am)))
    check("A_+^2 = -c A_+", zero(Ap * Ap + c * Ap))
    check("A_-^2 = c A_-", zero(Am * Am - c * Am))
    check("A_+ != 0 and A_- != 0 for c > 0",
          Ap[0, 0] == -c and Am[1, 1] == c)
except Exception as exc:  # fail closed
    print("FAIL exception:", exc)
    sys.exit(1)

n_fail = sum(1 for _, ok in checks if not ok)
print(f"{len(checks) - n_fail}/{len(checks)} checks passed")
sys.exit(1 if n_fail else 0)
