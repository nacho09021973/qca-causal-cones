"""Check (not a gate certificate) of two statements used in the dispersive-horizon
line and so far taken from reviewer text:

  (i)  the band of U = L_- W^2 through k = 0 that the turning-branch report calls
       the low-k sheet has group velocity d omega/dk = 8t - 3 at k = 0;
  (ii) at the horizon t = 3/8 that band is omega = (35/32) k^3 + O(k^5).

Source of the dispersion relation: the reviewed channels verifier,
scripts/verify_dispersive_horizon_channels.py, check C2 (lines 210-213):
    h(k) = 2 f(k)^2 - 1 - cos(omega + k) = 0,
    f(k) = A cos 3k + (1 - A) cos k,   A = t (2t - 1),
with lambda = e^{-ik}, z = e^{i omega}. It is restated here rather than
imported, because importing that verifier re-runs its whole chain (~25 min).

Route 1 (exact, SymPy). Write cos E = f with E odd and analytic in k,
E = a k + b k^3 + O(k^5). Then 2 f^2 - 1 = cos 2E, so the bands are
omega = -k +- 2E (mod 2 pi). The band omega = -k + 2E has slope -1 + 2a. The
coefficients come from matching the series of cos E and f; the result is
checked by substituting omega(k) back into h(k) to order k^5.

Route 2 (numerical, independent of the series). At t = 3/8 and at t = 5/16 and
7/16, the root omega of h near the predicted value is solved with mpmath
(findroot on the full trigonometric h, 50 digits) at small k, and compared
with the series. Orientation only: floating point, no certified quantity.

Output: reports/2026-11-27--dispersive-horizon-low-k-sheet-check.txt.
"""
import mpmath as mp
import sympy as sp
from sympy import Rational as R

k, t, a, b, om = sp.symbols('k t a b omega')
A = t * (2 * t - 1)
f = A * sp.cos(3 * k) + (1 - A) * sp.cos(k)

print('Route 1: exact series')
fs = sp.series(f, k, 0, 6).removeO()
E = a * k + b * k**3
cE = sp.series(sp.cos(E), k, 0, 6).removeO()
diff = sp.Poly(sp.expand(cE - fs), k)
c2 = sp.expand(diff.coeff_monomial(k**2))
c4 = sp.expand(diff.coeff_monomial(k**4))
a_sq = sp.solve(c2, a**2)
assert len(a_sq) == 1
a_sq = sp.factor(a_sq[0])
print(f'  a^2 = {a_sq}')
assert sp.expand(a_sq - (4 * t - 1)**2) == 0
a_val = 4 * t - 1                      # positive branch, t > 1/4
b_sol = sp.solve(c4.subs(a, a_val), b)
assert len(b_sol) == 1
b_val = sp.factor(b_sol[0])
print(f'  a = 4t - 1 (t > 1/4);  b = {b_val}')
omega_k = sp.expand(-k + 2 * (a_val * k + b_val * k**3))
v0 = sp.expand(sp.diff(omega_k, k).subs(k, 0))
gam = sp.factor(sp.expand(omega_k).coeff(k, 3))
print(f'  band omega = -k + 2E:  omega(k) = ({sp.factor(v0)}) k + ({gam}) k^3 + O(k^5)')
assert sp.expand(v0 - (8 * t - 3)) == 0
print('  (i)  d omega/dk at k = 0 equals 8t - 3: TRUE')
g38 = sp.nsimplify(gam.subs(t, R(3, 8)))
print(f'  (ii) cubic coefficient at t = 3/8: {g38}')
assert g38 == R(35, 32)
print('  (ii) equals 35/32: TRUE')
# substitute back into h to order k^5 (consistency of the whole series)
h = 2 * f**2 - 1 - sp.cos(omega_k + k)
hs = sp.series(h, k, 0, 6).removeO()
assert all(sp.simplify(sp.expand(hs).coeff(k, n)) == 0 for n in range(0, 6))
print('  h(k, omega(k)) = O(k^6) identically in t: TRUE')
for tv in (R(5, 16), R(3, 8), R(7, 16)):
    print(f'  t = {tv}: v0 = {8 * tv - 3}, cubic coefficient = {sp.nsimplify(gam.subs(t, tv))}')

print('\nRoute 2: numerical roots of the full h (mpmath, 50 digits; orientation)')
mp.mp.dps = 50
for tv in (R(5, 16), R(3, 8), R(7, 16)):
    Av = mp.mpf(tv.p) / tv.q * (2 * mp.mpf(tv.p) / tv.q - 1)
    v0n = 8 * mp.mpf(tv.p) / tv.q - 3
    gn = mp.mpf(sp.Rational(gam.subs(t, tv)).p) / sp.Rational(gam.subs(t, tv)).q
    for kv in (mp.mpf('1e-2'), mp.mpf('1e-3')):
        def hn(w):
            fv = Av * mp.cos(3 * kv) + (1 - Av) * mp.cos(kv)
            return 2 * fv**2 - 1 - mp.cos(w + kv)
        pred = v0n * kv + gn * kv**3
        wr = mp.findroot(hn, pred)
        # the two bands through this region are -k + 2E and -k - 2E; make sure we
        # landed on the predicted one and not on the other (slope -(8t - 1))
        other = -(8 * mp.mpf(tv.p) / tv.q - 1) * kv
        assert abs(wr - pred) < abs(wr - other)
        rel = (wr - v0n * kv) / kv**3
        print(f'  t = {tv}, k = {mp.nstr(kv, 3)}: omega root = {mp.nstr(wr, 20)}; '
              f'(omega - v0 k)/k^3 = {mp.nstr(rel, 12)} (series: {mp.nstr(gn, 12)})')
print('\nAll assertions passed.')
