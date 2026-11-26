"""Exact checks for the repairs to the dispersive-horizon transfer-matrix audit
after the Astra review (reports/reviews/2026-11-26-dispersive-horizon-transfer-astra/).

Imports scripts/verify_dispersive_horizon_transfer_matrix.py read-only (its bytes
were reviewed by Astra and are not changed). The import runs that verifier's 61
checks first; any failure there aborts this script too. Then:

  R1  T3 of the reviewed verifier compares exactly 21 interior sites (the audit
      text said 22).
  R2  At the nominal horizon t = 3/8, (z, lambda) = (1, 1) is a root of
      algebraic multiplicity 4 of det(lambda - M_hom) and geometric
      multiplicity 2: two explicit independent eigenvectors and a nonzero
      10x10 minor of M - I.
  R3  At t = 5/16 and t = 7/16 the same point has algebraic multiplicity 2.

Exact SymPy only; fails closed.
"""
import importlib.util
import itertools
import pathlib
import time

import sympy as sp
from sympy import I, Matrix, Rational as R, eye

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'reviewed', HERE / 'verify_dispersive_horizon_transfer_matrix.py')
rv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rv)          # runs the 61 reviewed checks

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


# ---------------------------------------------------------------- R1
ok('R1 reviewed T3 checks exactly 21 interior sites (6..26)',
   sorted(rv.interior) == list(range(6, 27)))

# ---------------------------------------------------------------- R2, R3
lam = sp.symbols('lambda')


def hom_matrix(tt, z):
    p, q = sp.sqrt(tt), sp.sqrt(1 - tt)
    cc, ss = rv.hom_cs(p, q)
    return rv.M_report(cc, ss, cc[6], ss[6], z), p, q


def multiplicity_at_one(M):
    cp = sp.Poly(sp.expand((lam * eye(12) - M).det(method='berkowitz')), lam)
    cp = sp.Poly([sp.radsimp(co) for co in cp.all_coeffs()], lam)
    m = 0
    lin = sp.Poly(lam - 1, lam)
    while all(sp.radsimp(co) == 0 for co in cp.rem(lin).all_coeffs()):
        cp = cp.quo(lin)
        m += 1
    # the remaining value at lambda = 1 is certified nonzero exactly
    return m, rv.nonzero_alg(cp.eval(1))


M38, p, q = hom_matrix(R(3, 8), 1)
m, rest_nonzero = multiplicity_at_one(M38)
ok('R2 t=3/8, z=1: lambda=1 has algebraic multiplicity exactly 4',
   m == 4 and rest_nonzero)
# Two Bloch eigenvectors at k = 0 (S(0) = I, lambda = 1): Y = (a_j, b_j).
vecs = []
for v in (Matrix([1, 0]), Matrix([0, 1])):
    qs = [v]
    for mm in rv.order[:5]:
        cm, sm = (p, q) if mm == 1 else (p * p - q * q, -2 * p * q)
        qs.append(Matrix([[cm, -sm], [sm, cm]]) * qs[-1])
    Y = Matrix([qj[0] for qj in qs] + [qj[1] for qj in qs])
    ok(f'R2 t=3/8: Bloch vector e{len(vecs) + 1} at k=0 is an eigenvector (lambda=1)',
       all(sp.radsimp(x) == 0 for x in (M38 * Y - Y)))
    vecs.append(Y)
B = Matrix.hstack(*vecs)
ok('R2 t=3/8: the two eigenvectors are independent',
   any(rv.nonzero_alg(B[i, 0] * B[j, 1] - B[j, 0] * B[i, 1])
       for i in range(12) for j in range(i + 1, 12)))
K = M38 - eye(12)
found = None
for rows in itertools.combinations(range(12), 2):
    for cols in itertools.combinations(range(12), 2):
        keep_r = [r for r in range(12) if r not in rows]
        keep_c = [c for c in range(12) if c not in cols]
        minor = sp.expand(K.extract(keep_r, keep_c).det(method='berkowitz'))
        if rv.nonzero_alg(minor):
            found = (rows, cols)
            break
    if found:
        break
ok(f'R2 t=3/8: rank(M - I) >= 10 (nonzero minor deleting rows {found and found[0]}, '
   f'cols {found and found[1]}), so geometric multiplicity exactly 2',
   found is not None)
for tt in (R(5, 16), R(7, 16)):
    Mt, _, _ = hom_matrix(tt, 1)
    m, rest_nonzero = multiplicity_at_one(Mt)
    ok(f'R3 t={tt}, z=1: lambda=1 has algebraic multiplicity exactly 2',
       m == 2 and rest_nonzero)

print(f'{len(checks)}/{len(checks)} repair checks PASS '
      f'(after {len(rv.checks)}/{len(rv.checks)} reviewed checks)')
