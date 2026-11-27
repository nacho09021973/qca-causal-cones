"""Exact checks for Amendment 2 of the dispersive-horizon transfer-matrix audit,
after the Grok review of Amendment 1
(reports/reviews/2026-11-26-dispersive-horizon-amendment1-grok/).

Imports scripts/verify_dispersive_horizon_transfer_repairs.py read-only, which
itself imports verify_dispersive_horizon_transfer_matrix.py read-only; the
import runs their 61 + 8 checks first and aborts on any failure. Neither file's
bytes are changed. Then:

  G1  t = 3/8, (z, lambda) = (-1, -1): algebraic multiplicity exactly 4,
      geometric exactly 2 (two Bloch eigenvectors at k = pi, nonzero 10x10
      minor of M + I).
  G2  t = 5/16, 7/16: at (1, 1) and (-1, -1), algebraic 2 and geometric 2
      (semisimple).
  G3  t = 3/8: E = k/2 + (35/64) k^3 + O(k^5), so Omega_+ = (35/32) k^3 + O(k^5).
  G4  zero of the outgoing velocity on (0, pi/2): with u = cos^2 k,
      v_+ = 0 there iff 4(1-u) g'(C)^2 = 1 - g(C)^2 (C = cos k); the polynomial
      factors as (u-1) * quadratic; t = 5/16: quadratic proportional to
      2625 w^2 + 5 w - 16 (w = u - 1), one root u in (0, 1), simple;
      t = 3/8: factor (u-1)^2, no root in (0, 1); t = 7/16: no root in [0, 1].

Exact SymPy only; fails closed. The equivalence of v_+ = 0 with the squared
equation on (0, pi/2) is a written step (-f' = sin k * g'(C) > 0 and
sin E > 0 there), not machine-checked.
"""
import importlib.util
import itertools
import pathlib
import time

import sympy as sp
from sympy import Matrix, Rational as R, eye

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'repairs', HERE / 'verify_dispersive_horizon_transfer_repairs.py')
rp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rp)          # runs 61 reviewed + 8 repair checks
rv = rp.rv

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


lam = sp.symbols('lambda')


def algebraic_multiplicity(M, l0):
    cp = sp.Poly(sp.expand((lam * eye(12) - M).det(method='berkowitz')), lam)
    cp = sp.Poly([sp.radsimp(co) for co in cp.all_coeffs()], lam)
    m = 0
    lin = sp.Poly(lam - l0, lam)
    while all(sp.radsimp(co) == 0 for co in cp.rem(lin).all_coeffs()):
        cp = cp.quo(lin)
        m += 1
    return m, rv.nonzero_alg(cp.eval(l0))


def bloch_vectors(p, q, l0):
    """Bloch eigenvectors of M at k = 0 (l0 = 1) or k = pi (l0 = -1).
    S(k) = diag(1/l0, l0) = l0 * I for l0 = +-1; Y = (a_j, b_j / l0)."""
    vecs = []
    for v in (Matrix([1, 0]), Matrix([0, 1])):
        qs = [v]
        for mm in rv.order[:5]:
            cm, sm = (p, q) if mm == 1 else (p * p - q * q, -2 * p * q)
            qs.append(l0 * Matrix([[cm, -sm], [sm, cm]]) * qs[-1])
        vecs.append(Matrix([qj[0] for qj in qs] + [qj[1] / l0 for qj in qs]))
    return vecs


def geometric_two(M, p, q, l0, tag):
    vecs = bloch_vectors(p, q, l0)
    for n, Y in enumerate(vecs, 1):
        ok(f'{tag}: Bloch vector e{n} is an eigenvector (lambda={l0})',
           all(sp.radsimp(x) == 0 for x in (M * Y - l0 * Y)))
    B = Matrix.hstack(*vecs)
    ok(f'{tag}: the two eigenvectors are independent',
       any(rv.nonzero_alg(B[i, 0] * B[j, 1] - B[j, 0] * B[i, 1])
           for i in range(12) for j in range(i + 1, 12)))
    K = M - l0 * eye(12)
    found = None
    for rows in itertools.combinations(range(12), 2):
        for cols in itertools.combinations(range(12), 2):
            keep_r = [r for r in range(12) if r not in rows]
            keep_c = [c for c in range(12) if c not in cols]
            if rv.nonzero_alg(sp.expand(K.extract(keep_r, keep_c).det(method='berkowitz'))):
                found = (rows, cols)
                break
        if found:
            break
    ok(f'{tag}: nonzero 10x10 minor of M - lambda (rows {found and found[0]} and '
       f'cols {found and found[1]} deleted), geometric multiplicity exactly 2',
       found is not None)


def hom(tt, z):
    p, q = sp.sqrt(tt), sp.sqrt(1 - tt)
    cc, ss = rv.hom_cs(p, q)
    return rv.M_report(cc, ss, cc[6], ss[6], z), p, q


# ---------------------------------------------------------------- G1
M, p, q = hom(R(3, 8), -1)
m, rest = algebraic_multiplicity(M, -1)
ok('G1 t=3/8, z=-1: lambda=-1 has algebraic multiplicity exactly 4', m == 4 and rest)
geometric_two(M, p, q, -1, 'G1 t=3/8, z=-1')

# ---------------------------------------------------------------- G2
for tt in (R(5, 16), R(7, 16)):
    for z0 in (1, -1):
        M, p, q = hom(tt, z0)
        m, rest = algebraic_multiplicity(M, z0)
        ok(f'G2 t={tt}, z={z0}: lambda={z0} has algebraic multiplicity exactly 2',
           m == 2 and rest)
        geometric_two(M, p, q, z0, f'G2 t={tt}, z={z0}')

# ---------------------------------------------------------------- G3
k, beta = sp.symbols('k beta')
A38 = R(3, 8) * (2 * R(3, 8) - 1)
f38 = A38 * sp.cos(3 * k) + (1 - A38) * sp.cos(k)
ok('G3 t=3/8: f = 1 - k^2/8 - (13/48) k^4 + O(k^6)',
   sp.expand(sp.series(f38, k, 0, 6).removeO() - (1 - k**2 / 8 - R(13, 48) * k**4)) == 0)
ser = sp.expand(sp.series(sp.cos(k / 2 + beta * k**3) - f38, k, 0, 6).removeO())
ok('G3 t=3/8: k^2 term of cos(E) - f vanishes for E = k/2 + beta k^3',
   sp.expand(ser.coeff(k, 2)) == 0)
ok('G3 t=3/8: k^4 term fixes beta = 35/64, so Omega_+ = (35/32) k^3 + O(k^5)',
   sp.solve(ser.coeff(k, 4), beta) == [R(35, 64)])

# ---------------------------------------------------------------- G4
C, u, w = sp.symbols('C u w')


def edge_poly(tt):
    AA = tt * (2 * tt - 1)
    g = 4 * AA * C**3 + (1 - 4 * AA) * C
    gp = 12 * AA * C**2 + 1 - 4 * AA
    expr = sp.expand(4 * (1 - C**2) * gp**2 - (1 - g**2))
    ok(f'G4 t={tt}: edge equation is even in C', sp.expand(expr - expr.subs(C, -C)) == 0)
    return sp.Poly(sp.expand(expr).subs(C**2, u).subs(C, sp.sqrt(u)), u)


def roots_in_open_unit(Pu):
    """Exact count of distinct real roots in (0, 1) by Sturm's theorem."""
    return sp.Poly(Pu, u).count_roots(0, 1) - (1 if Pu.eval(1) == 0 else 0) \
        - (1 if Pu.eval(0) == 0 else 0)


P516 = edge_poly(R(5, 16))
Q516, r516 = sp.div(P516, sp.Poly(u - 1, u))
ok('G4 t=5/16: (u - 1) divides the edge polynomial', r516.is_zero)
quad_w = sp.Poly(sp.expand(Q516.as_expr().subs(u, w + 1)), w)
target = sp.Poly(2625 * w**2 + 5 * w - 16, w)
ratio = sp.cancel(quad_w.as_expr() / target.as_expr())
ok('G4 t=5/16: quotient is proportional to 2625 w^2 + 5 w - 16 (w = u - 1)',
   ratio.is_number and ratio != 0)
ok('G4 t=5/16: discriminant 168025 != 0 (simple roots)',
   sp.discriminant(target.as_expr(), w) == 168025)
ok('G4 t=5/16: exactly one root u = cos^2 k in (0, 1), i.e. one k in (0, pi/2)',
   roots_in_open_unit(Q516) == 1)
P38 = edge_poly(R(3, 8))
Q38, r38 = sp.div(P38, sp.Poly((u - 1)**2, u))
ok('G4 t=3/8: (u - 1)^2 divides the edge polynomial (the k^3 contact at k = 0)',
   r38.is_zero)
ok('G4 t=3/8: no root u in (0, 1)', roots_in_open_unit(P38) == 0)
P716 = edge_poly(R(7, 16))
Q716, r716 = sp.div(P716, sp.Poly(u - 1, u))
ok('G4 t=7/16: (u - 1) divides the edge polynomial', r716.is_zero)
ok('G4 t=7/16: no root u in [0, 1] of the quotient',
   sp.Poly(Q716, u).count_roots(0, 1) == 0)

print(f'{len(checks)}/{len(checks)} amendment-2 checks PASS '
      f'(after {len(rv.checks)}/{len(rv.checks)} reviewed and '
      f'{len(rp.checks)}/{len(rp.checks)} repair checks)')
