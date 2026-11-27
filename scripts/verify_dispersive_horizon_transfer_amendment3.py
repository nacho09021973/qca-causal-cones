"""Exact checks for Amendment 3 of the dispersive-horizon transfer-matrix audit,
after the Astra review of Amendment 2
(reports/reviews/2026-11-26-dispersive-horizon-amendment2-astra/).

Imports scripts/verify_dispersive_horizon_transfer_amendment2.py read-only
(which imports the repairs and the reviewed verifiers read-only); the import
runs their 61 + 8 + 39 checks first and aborts on any failure. No earlier
verifier's bytes are changed. Then:

  J1  t = 3/8, (z, lambda) = (1, 1) and (-1, -1): with K = M - lambda I,
      dim ker K = 2, dim ker K^2 = 3, dim ker K^3 = dim ker K^4 = 4, by exact
      rank over the number field Q(sqrt 6, sqrt 10). Jordan partition 3 + 1.
  J2  the horizon threshold polynomial is divisible by (u-1)^2 and not by
      (u-1)^3.
  B1  identity 4(1-C^2) g'^2 - (1 - g^2) = (1 - g^2)(4 E'^2 - 1) with
      E'^2 = (1-C^2) g'^2 / (1 - g^2), i.e. P_t(u(k)) = sin^2 E * v (v + 2),
      v = 2E' - 1 on the outgoing branch.
  B2  t = 5/16: P'(u*) = -(3/1024)(1 - u*) sqrt(168025) < 0 at the interior
      root u* = (5245 - sqrt 168025)/5250, and 0 < u* < 1.
  B3  t = 5/16: 0 < f(k*) < 1 at the edge (0 < E < pi/2: the two bands are
      distinct there), from 0 < u* < 1 and g(0) = 0, g(1) = 1, g' > 0 on [0,1]
      (reviewed T8 / A2 ingredients).

Written steps (not machine-checked) are listed in scripts/README.md.
Exact SymPy only; fails closed.
"""
import importlib.util
import pathlib
import time

import sympy as sp
from sympy import Rational as R, eye
from sympy.polys.matrices import DomainMatrix

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'amendment2', HERE / 'verify_dispersive_horizon_transfer_amendment2.py')
a2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a2)          # runs 61 + 8 + 39 earlier checks
rv = a2.rv

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


# ---------------------------------------------------------------- J1
t38 = R(3, 8)
p, q = sp.sqrt(t38), sp.sqrt(1 - t38)               # sqrt(6)/4, sqrt(10)/4
K_field = sp.QQ.algebraic_field(sp.sqrt(6), sp.sqrt(10))
for z0 in (1, -1):
    cc, ss = rv.hom_cs(p, q)
    M = rv.M_report(cc, ss, cc[6], ss[6], z0)
    Kmat = (M - z0 * eye(12)).applyfunc(sp.radsimp)
    Kd = DomainMatrix.from_Matrix(Kmat).convert_to(K_field)
    ranks = []
    P_ = DomainMatrix.eye(12, K_field)
    for j in range(1, 5):
        P_ = P_ * Kd
        ranks.append(P_.rank())
    nul = [12 - r for r in ranks]
    ok(f'J1 t=3/8, (z,lambda)=({z0},{z0}): dim ker K^j, j=1..4, = {nul} (exact rank over '
       'Q(sqrt6, sqrt10))', nul == [2, 3, 4, 4])
    ok(f'J1 t=3/8, (z,lambda)=({z0},{z0}): Jordan partition 3 + 1 '
       '(two blocks; one of size >= 3; generalized eigenspace 4)',
       nul[0] == 2 and nul[1] - nul[0] == 1 and nul[2] - nul[1] == 1 and nul[3] == nul[2] == 4)

# ---------------------------------------------------------------- J2
u = a2.u
C_ = sp.symbols('C_')


def edge_poly(tt):
    AA = tt * (2 * tt - 1)
    g = 4 * AA * C_**3 + (1 - 4 * AA) * C_
    gp = 12 * AA * C_**2 + 1 - 4 * AA
    expr = sp.expand(4 * (1 - C_**2) * gp**2 - (1 - g**2))
    assert sp.expand(expr - expr.subs(C_, -C_)) == 0
    return sp.Poly(sp.expand(expr).subs(C_**2, u).subs(C_, sp.sqrt(u)), u)


P38 = edge_poly(t38)
q2, r2 = sp.div(P38, sp.Poly((u - 1)**2, u))
q3, r3 = sp.div(P38, sp.Poly((u - 1)**3, u))
ok('J2 t=3/8: (u-1)^2 divides the threshold polynomial and (u-1)^3 does not',
   r2.is_zero and not r3.is_zero and q2.eval(1) != 0)

# ---------------------------------------------------------------- B1
Cc, Gs, Gp = sp.symbols('C G Gp')
Ep2 = (1 - Cc**2) * Gp**2 / (1 - Gs**2)
ok("B1 4(1-C^2)g'^2 - (1-g^2) = (1-g^2)(4E'^2 - 1), E'^2 = (1-C^2)g'^2/(1-g^2)",
   sp.simplify(4 * (1 - Cc**2) * Gp**2 - (1 - Gs**2) - (1 - Gs**2) * (4 * Ep2 - 1)) == 0)
vv = sp.symbols('v')
ok('B1 4E\'^2 - 1 = v(v+2) with v = 2E\' - 1',
   sp.expand(4 * ((vv + 1) / 2)**2 - 1 - vv * (vv + 2)) == 0)

# ---------------------------------------------------------------- B2
t516 = R(5, 16)
P516 = edge_poly(t516)
ustar = (5245 - sp.sqrt(168025)) / 5250
dP = sp.diff(P516.as_expr(), u)
ok("B2 t=5/16: P_t'(u*) = -(3/1024)(1-u*) sqrt(168025)",
   sp.simplify(sp.expand(dP.subs(u, ustar) + R(3, 1024) * (1 - ustar) * sp.sqrt(168025))) == 0)
# u* > 0 iff sqrt(168025) < 5245 iff 168025 < 5245^2 (integers); u* < 1 since sqrt > 0.
ok('B2 t=5/16: 0 < u* < 1 (168025 < 5245^2), so P_t\'(u*) < 0 and '
   'u\'(k*) = -sin 2k* < 0 on (0, pi/2)', 168025 < 5245**2)

# ---------------------------------------------------------------- B3
A516 = t516 * (2 * t516 - 1)
gC = 4 * A516 * C_**3 + (1 - 4 * A516) * C_
gpC = sp.diff(gC, C_)
ok('B3 t=5/16: g(0) = 0, g(1) = 1 and g\' >= g\'(1) = (4t-1)^2 = 1/16 > 0 on [0,1] (A < 0), so '
   '0 < f(k*) = g(sqrt u*) < 1 for 0 < u* < 1 (0 < E < pi/2, bands distinct)',
   gC.subs(C_, 0) == 0 and gC.subs(C_, 1) == 1 and A516 < 0
   and sp.expand(gpC.subs(C_, 1)) == (4 * t516 - 1)**2 == R(1, 16)
   and sp.expand(gpC - gpC.subs(C_, 1) - 12 * A516 * (C_**2 - 1)) == 0)

print(f'{len(checks)}/{len(checks)} amendment-3 checks PASS '
      f'(after {len(rv.checks)} reviewed, {len(a2.rp.checks)} repair and '
      f'{len(a2.checks)} amendment-2 checks)')
assert len(a2.checks) == 39 and len(a2.rp.checks) == 8 and len(rv.checks) == 61
