"""Verifier for theory/DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md (frozen at 204f33b):
F1 regime boundary, F2 sharp-profile frequency scan, F3 truncated tanh profile.

Imports scripts/verify_dispersive_horizon_transmission.py read-only, after a
SHA256 check. That verifier checks and imports the channels and transfer-matrix
verifiers, so the 61 + 53 + 33 reviewed checks run first (about 25 min). Its
helpers (M_TEMPLATE, eval_CI, HN_at, H_of, G_hom, horner, gauss_to_CI, zCI)
are reused unchanged. Its sharp-profile enclosures at z0 and z1 are used as a
cross-check of the new pipeline.

Certification. Every certified number is an exact rational or a rational
interval (Fractions; outward rounding to dyadic grids; integer square roots;
mpmath `iv` with outward rounding only for exp in the tanh enclosure). Floating
point / mpmath plain arithmetic only supplies root guesses and preconditioners;
each guess is certified exactly (Krawczyk for roots, ||I - RA|| < 1/2 with an
interval residual for linear solves).

Points: z(s) = (1 - s^2 + 2 i s)/(1 + s^2).
  On I:            s = 1/4, 1/2, 3/4.
  Horizon arc:     s = 1/200, 1/50, 1/30.

  F1  (a) critical-value branch. On a regular level the real double roots of
      H(tau) are the collisions z = +-1, +-i (t-independent) and the critical
      values (reviewed C3: 4f'^2 = 1 - f^2, f != 0). With u = cos^2 k,
      f = C gt(u), f' = -sin k gp(u), the threshold polynomial is
      thr(u, A) = (u - 1) q(u, A), and Re z_c = C R(u, A), y = (Re z_c)^2 =
      u R^2. The first-quadrant critical value of a medium A has
      cos^2(arg z_c) = y. The verifier certifies, over A in
      [A(5/16), A(7/16)]: the event polynomials q(0, A), lc_u q, disc_u q and
      res_u(q, J) (J = y_A q_u - y_u q_A, stationarity of y along the branch)
      have no root, and q(1, A) has exactly one root A_d; q has one root in
      (0, 1) at A(5/16) and none at A(7/16). Written step: the branch u*(A) is
      then continuous on [A(5/16), A_d), leaves through u = 1 where y = 1, and
      y is monotone on it, so the first-quadrant critical set is
      (0, arg z_c*] with z_c* the reviewed interior critical value.
      Verdict REGIME_BOUNDARY_CERTIFIED, else OPEN_AFTER_DISCRIMINANT_ANALYSIS.
      (b) per declared point, the T0 test of the transmission verifier: the
      discriminant in tau of H_A(tau) at z(s), as a polynomial in A, and its
      roots in [A(5/16), A(7/16)].
  F2  sharp profile 5/16 | 3/8 | 7/16 (N = 0) at the six points.
  F3  truncated profile t(x) = 3/8 + tanh(x/L)/16 for |x| <= N, asymptotic
      values beyond; (L, N) = (4, 32), (16, 128); s = 1/50, 1/200.

  Per (profile, z): regularity (H squarefree, gcd(H, N) = 1) or
  S_MATRIX_NOT_ESTABLISHED; base roots at radius 2^-256 give
  kappa = max(|lambda|, 1/|lambda|) (upper bound) and the predeclared
  precision p = 256 + 2(2N + 1) ceil(log2 kappa); roots re-certified at radius
  2^-p; Bloch vectors at p bits; flux signs and |F| from the reviewed G_hom;
  interval propagation of the unnormalized interior vectors through
  M_N ... M_{-N-1}, outward rounding to 2^-p after each site; column-scaled
  matching solve with a high-precision preconditioner; |S_rc|^2 =
  |x_rc|^2 |F_r| / |F_c|; S^H S encloses I.
  Verdicts per point: TRANSMISSION_NONZERO_CERTIFIED (enclosure > 0 and width
  <= 1e-6), OPEN_AFTER_TRANSMISSION_ANALYSIS (wider, or a certification step
  failed), S_MATRIX_NOT_ESTABLISHED (not a regular level).
  Line verdict: LEAKAGE_SUPPRESSED_AT_COMPUTED_L / LEAKAGE_NOT_SUPPRESSED /
  MIXED, as defined in the charter; both conditions are printed.

Written steps (not machine-checked) are listed in scripts/README.md.
"""
import hashlib
import importlib.util
import pathlib
import time
from fractions import Fraction as Fr
from math import isqrt

import mpmath as mp
from mpmath import iv
import sympy as sp
from sympy import I, Rational as R

HERE = pathlib.Path(__file__).resolve().parent
SHA_TRANSMISSION = '29ee9f127b2e43dc1a8aabf2cfdffb6e727edf502e9677b823f45b7c27e316ea'
h_tr = hashlib.sha256((HERE / 'verify_dispersive_horizon_transmission.py').read_bytes()).hexdigest()
assert h_tr == SHA_TRANSMISSION, 'imported transmission verifier bytes changed'

spec = importlib.util.spec_from_file_location('transmission', HERE / 'verify_dispersive_horizon_transmission.py')
tr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tr)          # 61 + 53 + 33 reviewed checks
ch, rv = tr.ch, tr.rv
RI, CI = ch.RI, ch.CI
order = ch.order
matvec = ch.matvec
assert len(rv.checks) == 61 and len(ch.checks) == 53 and len(tr.checks) == 33

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


def note(msg):
    print(f'{msg}  [{time.perf_counter() - T0:.1f}s]', flush=True)


ok('H imported transmission verifier has the reviewed SHA256 (checked before import); '
   '61 + 53 + 33 imported checks passed', True)


class NotCertified(Exception):
    pass


dec, ri_str, ci_str = tr.dec, tr.ri_str, tr.ci_str
cmag, contains0, coverlap = tr.cmag, tr.contains0, tr.coverlap
T_INT, T_HOR, T_EXT = R(5, 16), R(3, 8), R(7, 16)
A_INT, A_EXT = T_INT * (2 * T_INT - 1), T_EXT * (2 * T_EXT - 1)


# ----------------------------------------------------------- precision helpers
def fl(x):                          # floor of a Fraction
    return x.numerator // x.denominator


def ce(x):                          # ceiling of a Fraction
    return -((-x.numerator) // x.denominator)


def rnd_RI(x, p):                   # outward rounding to the grid 2^-p
    S = 1 << p
    return RI(Fr(fl(x.lo * S), S), Fr(ce(x.hi * S), S))


def rnd_CI(x, p):
    return CI(rnd_RI(x.re, p), rnd_RI(x.im, p))


def rnd_fr(x, p):                   # nearest point of the grid 2^-p (guesses only)
    S = 1 << p
    return Fr(round(x * S), S)


def sqrt_RI_p(x, p):                # enclosure of sqrt on [lo, hi], grid 2^-p
    assert x.lo >= 0
    S = 4**p
    lo = Fr(isqrt(fl(x.lo * S)), 2**p)
    hi = Fr(isqrt(ce(x.hi * S)) + 1, 2**p)
    return RI(lo, hi)


def raw_fr(raw):                    # exact value of an mpmath raw mpf tuple
    sign, man, exp, _ = raw
    man, exp = int(man), int(exp)
    v = Fr(man << exp) if exp >= 0 else Fr(man, 1 << -exp)
    return -v if sign else v


def mpf_fr(v):
    return raw_fr(mp.mpf(v)._mpf_)


def fr_mp(x):
    return mp.mpf(x.numerator) / x.denominator


def mid_mp(x):                      # CI -> mpc midpoint (guesses only)
    return mp.mpc(fr_mp((x.re.lo + x.re.hi) / 2), fr_mp((x.im.lo + x.im.hi) / 2))


def tanh_RI(x, Lv, p):              # enclosure of tanh(x / Lv), x, Lv integers
    if x == 0:
        return RI(0)
    if x < 0:
        return -tanh_RI(-x, Lv, p)
    iv.prec = p + 64
    E = iv.exp(iv.mpf(2 * x) / Lv)
    elo, ehi = raw_fr(E._mpi_[0]), raw_fr(E._mpi_[1])
    assert 0 < elo <= ehi
    return RI(1 - Fr(2) / (elo + 1), 1 - Fr(2) / (ehi + 1))   # increasing in e^{2y}


def zdata(sv):
    cw = (1 - sv**2) / (1 + sv**2)
    sw = 2 * sv / (1 + sv**2)
    zz = cw + sw * I
    return cw, sw, zz, tr.zCI(zz)


# ================================================================= F1 (a)
u_, A_ = sp.symbols('u_ A_')
gt = 4 * A_ * u_ + 1 - 4 * A_            # f = C gt(u)
gpu = 12 * A_ * u_ + 1 - 4 * A_          # g'(C) = gp(u)
thr = sp.expand(4 * (1 - u_) * gpu**2 - (1 - u_ * gt**2))
ok('F1 thr(u, A) = 4(1-u) gp^2 - (1 - u gt^2) equals the reviewed C3 threshold polynomial '
   'at t = 5/16 and t = 7/16',
   all(sp.expand(thr.subs(A_, tt * (2 * tt - 1)) - ch.thr_poly(tt).as_expr().subs(ch.u, u_)) == 0
       for tt in (T_INT, T_EXT)))
qP, remP = sp.div(sp.Poly(thr, u_), sp.Poly(u_ - 1, u_))
ok('F1 u = 1 is a root of thr for every A (nodes); q = thr / (u - 1)', remP.is_zero)
q = qP.as_expr()
Rr = (2 * u_ * gt**2 - 1) + 4 * (1 - u_) * gt * gpu
yv = sp.expand(u_ * Rr**2)
ok('F1 R(1, A) = 1, so y = u R^2 equals 1 at u = 1 for every A',
   sp.expand(Rr.subs(u_, 1)) == 1)
J = sp.expand(sp.diff(yv, A_) * sp.diff(q, u_) - sp.diff(yv, u_) * sp.diff(q, A_))


def roots_in_A(expr, name):
    P = sp.Poly(sp.expand(expr), A_)
    if P.is_zero:
        note(f'F1 event polynomial {name} vanishes identically')
        return None
    if P.degree() <= 0:
        return 0
    n = P.count_roots(A_INT, A_EXT)
    note(f'F1 event {name}: degree {P.degree()} in A, roots in [A(5/16), A(7/16)]: {n}')
    return n


ev = {
    'q(0, A)': roots_in_A(q.subs(u_, 0), 'q(0, A)'),
    'lc_u q': roots_in_A(sp.Poly(q, u_).LC(), 'lc_u q'),
    'disc_u q': roots_in_A(sp.discriminant(q, u_), 'disc_u q'),
    'res_u(q, J)': roots_in_A(sp.resultant(q, J, u_), 'res_u(q, J)'),
    'q(1, A)': roots_in_A(q.subs(u_, 1), 'q(1, A)'),
}


def q_roots_open01(Av):
    P = sp.Poly(q.subs(A_, Av), u_)
    n = P.count_roots(0, 1)
    n -= (1 if P.eval(0) == 0 else 0) + (1 if P.eval(1) == 0 else 0)
    return n


n_int, n_ext = q_roots_open01(A_INT), q_roots_open01(A_EXT)
note(f'F1 roots of q(., A) in (0, 1): {n_int} at A(5/16), {n_ext} at A(7/16)')
q1P = sp.Poly(q.subs(u_, 1), A_)
simple_structure = (ev['q(0, A)'] == 0 and ev['lc_u q'] == 0 and ev['disc_u q'] == 0
                    and ev['res_u(q, J)'] == 0 and ev['q(1, A)'] == 1
                    and q1P.eval(A_INT) != 0 and q1P.eval(A_EXT) != 0
                    and n_int == 1 and n_ext == 0)
ok(f'F1 event structure computed (simple structure: {simple_structure})', True)

# y* = (Re z_c*)^2 at A(5/16): enclosure from the unique root u* of q in (0, 1)
qi = sp.Poly(q.subs(A_, A_INT), u_)
ivs = [iv_ for iv_, _ in qi.intervals(eps=R(1, 10**80), inf=0, sup=1)]
ivs = [(a, b) for a, b in ivs if a > 0 and b < 1]
ok('F1 exactly one isolating interval of q(., A(5/16)) inside (0, 1)', len(ivs) == 1)
uI = RI(Fr(int(ivs[0][0].p), int(ivs[0][0].q)), Fr(int(ivs[0][1].p), int(ivs[0][1].q)))
r168 = ch.sqrt_RI(RI(168025))
u_rev = (RI(5245) - r168) / 5250
ok('F1 u* agrees with the reviewed C3 value (5245 - sqrt 168025)/5250 (enclosures overlap)',
   uI.lo <= u_rev.hi and u_rev.lo <= uI.hi)
yP = sp.Poly(yv.subs(A_, A_INT), u_)
y_star = RI(0)
for c in yP.all_coeffs():
    y_star = y_star * uI + RI(Fr(int(c.p), int(c.q)))
rz_lo = Fr('0.996006471094483079484232973570')
rz_hi = Fr('0.996006471094483079484232973571')
ok('F1 y* = (Re z_c*)^2 overlaps the square of the reviewed Re z_c* enclosure',
   y_star.lo <= rz_hi**2 and rz_lo**2 <= y_star.hi and y_star.hi < 1)
note(f'F1 y* in {ri_str(y_star, 30)}')
F1_verdict = 'REGIME_BOUNDARY_CERTIFIED' if simple_structure else 'OPEN_AFTER_DISCRIMINANT_ANALYSIS'
if simple_structure:
    note('F1 REGIME_BOUNDARY_CERTIFIED: in the open first quadrant the critical values of the '
         'media t in [5/16, 7/16] fill exactly (0, arg z_c*]; the CONNECTED region there is '
         '(arg z_c*, pi/2) = I (written step, see header)')
else:
    note('F1 OPEN_AFTER_DISCRIMINANT_ANALYSIS: event structure not the simple one (see counts)')

S_I = [R(1, 4), R(1, 2), R(3, 4)]
S_ARC = [R(1, 200), R(1, 50), R(1, 30)]
F1_class = {}
for sv in S_I + S_ARC:
    cw = (1 - sv**2) / (1 + sv**2)
    ys = Fr(int((cw**2).p), int((cw**2).q))
    if ys > y_star.hi:
        F1_class[sv] = 'horizon arc'
    elif ys < y_star.lo:
        F1_class[sv] = 'I'
    else:
        F1_class[sv] = 'undecided'
ok('F1 declared points classified against y*: s in {1/4, 1/2, 3/4} on I, '
   's in {1/200, 1/50, 1/30} on the horizon arc',
   all(F1_class[s] == 'I' for s in S_I) and all(F1_class[s] == 'horizon arc' for s in S_ARC))

# ================================================================= F1 (b)
F1b = {}
for sv in S_I + S_ARC:
    cw, sw, zz, _ = zdata(sv)
    HA = tr.H_of(tr.Asym, cw, sw)
    lc = sp.expand(HA.LC())
    Dsc = sp.Poly(sp.discriminant(HA.as_expr(), tr.tau), tr.Asym)
    nD = Dsc.count_roots(A_INT, A_EXT)
    conn = (lc.is_number and lc != 0 and HA.degree() == 12 and nD == 0
            and Dsc.eval(A_INT) != 0 and Dsc.eval(A_EXT) != 0)
    F1b[sv] = conn
    note(f'F1b s = {sv}: leading coefficient {lc}; discriminant degree {Dsc.degree()} in A, '
         f'roots in [A(5/16), A(7/16)]: {nD} -> {"CONNECTED" if conn else "not certified connected"}')
ok('F1b T0 test at the declared points: CONNECTED at s = 1/4, 1/2, 3/4',
   all(F1b[s] for s in S_I))


# ================================================================= pipeline
Lsym = tr.L


def roots_boxes(AA, zz, p):
    """12 roots of P(., z) in disjoint boxes of half-width 2^-p (Krawczyk)."""
    Pz = sp.Poly(sp.expand(ch.P.subs({ch.lam: Lsym, ch.Aa: AA, ch.z: zz})), Lsym)
    cs = Pz.all_coeffs()
    assert len(cs) == 13 and cs[-1] != 0
    cz = [tr.gauss_to_CI(c) for c in cs]
    dcz = [tr.gauss_to_CI(c) for c in Pz.diff(Lsym).all_coeffs()]
    dps = int(p * 0.30103) + 60
    RAD = Fr(1, 2**p)
    boxes = []
    with mp.workdps(dps):
        cmp_ = [mp.mpc(mp.mpf(int(sp.re(c).p)) / int(sp.re(c).q),
                       mp.mpf(int(sp.im(c).p)) / int(sp.im(c).q)) for c in cs]
        dmp = [cmp_[k] * (12 - k) for k in range(12)]
        try:
            rts = mp.polyroots(cmp_, maxsteps=800, extraprec=2 * dps)
        except mp.NoConvergence:
            raise NotCertified('root guesses did not converge')
        for x in rts:
            for _ in range(60):
                dx = mp.polyval(cmp_, x) / mp.polyval(dmp, x)
                x -= dx
                if abs(dx) < mp.mpf(2)**(-(p + 64)):
                    break
            cr, ci_ = rnd_fr(mpf_fr(x.real), p + 32), rnd_fr(mpf_fr(x.imag), p + 32)
            X = CI(RI(cr - RAD, cr + RAD), RI(ci_ - RAD, ci_ + RAD))
            c = CI(RI(cr), RI(ci_))
            fc = tr.horner(cz, c)
            yinv = 1 / mp.polyval(dmp, x)
            Y = CI(RI(rnd_fr(mpf_fr(yinv.real), p + 32)), RI(rnd_fr(mpf_fr(yinv.imag), p + 32)))
            K = c - Y * fc + (CI(1) - Y * tr.horner(dcz, X)) * (X - c)
            if not (K.re.lo > X.re.lo and K.re.hi < X.re.hi and K.im.lo > X.im.lo and K.im.hi < X.im.hi):
                raise NotCertified(f'Krawczyk inclusion failed at radius 2^-{p}')
            boxes.append(X)
    if len(boxes) != 12 or any(coverlap(boxes[i], boxes[j]) for i in range(12) for j in range(i + 1, 12)):
        raise NotCertified(f'root boxes not 12 pairwise disjoint at radius 2^-{p}')
    return boxes


def ceil_log2_kappa(boxes):
    m = max(max(X.abs2().hi, 1 / X.abs2().lo) for X in boxes)     # kappa^2 upper bound
    e = 0
    while Fr(4)**e < m:
        e += 1
    return e


def coins_t(tI, p):
    pc = sqrt_RI_p(tI, p)
    qc = sqrt_RI_p(RI(1) - tI, p)
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = (pc, qc) if m == 1 else (rnd_RI(RI(2) * tI - 1, p), rnd_RI(RI(-2) * pc * qc, p))
    return cc, ss, pc, qc


def M_site_p(tI, tnI, zI, p):
    cc, ss, _, _ = coins_t(tI, p)
    cn, sn, _, _ = coins_t(tnI, p)
    env = {tr.zT: zI, tr.cPT: CI(cn[6]), tr.sPT: CI(sn[6])}
    for j in range(1, 7):
        env[tr.cTs[j - 1]] = CI(cc[j])
        env[tr.sTs[j - 1]] = CI(ss[j])
    return [[rnd_CI(tr.eval_CI(tr.M_TEMPLATE[i, k], env), p) for k in range(12)] for i in range(12)]


def bloch_vector_p(lamI, zI, tt, p):
    pc, qc = sqrt_RI_p(RI(tt), p), sqrt_RI_p(RI(1 - tt), p)
    Sm = [[CI(1) / lamI, CI(0)], [CI(0), lamI]]
    Cm2, Cm1 = ch.coin_I(-2, pc, qc), ch.coin_I(1, pc, qc)
    mm = ch.matmul
    Wm = mm(Sm, mm(Cm1, mm(Sm, mm(Cm1, mm(Sm, Cm2)))))
    Um = mm([[lamI, CI(0)], [CI(0), lamI]], mm(Wm, Wm))
    v1 = [Um[0][1], zI - Um[0][0]]
    v2 = [zI - Um[1][1], Um[1][0]]
    if (v1[0].abs2() + v1[1].abs2()).pos():
        vv = v1
    elif (v2[0].abs2() + v2[1].abs2()).pos():
        vv = v2
    else:
        raise NotCertified('kernel vector norm not certified positive')
    qv = [vv]
    for m in order[:5]:
        qv.append(matvec(Sm, matvec(ch.coin_I(m, pc, qc), qv[-1])))
    Y = [x[0] for x in qv] + [x[1] / lamI for x in qv]
    return [rnd_CI(y, p + 32) for y in Y]


G_CACHE = {}


def medium_p(tt, zI, zz, cw, sw, p, name):
    H, Nn = tr.HN_at(tt, cw, sw)
    nprop = H.count_roots()
    boxes = roots_boxes(tt * (2 * tt - 1), zz, p)
    inside = [X for X in boxes if X.abs2().hi < 1]
    outside = [X for X in boxes if X.abs2().lo > 1]
    circle = [X for X in boxes if X.abs2().lo <= 1 <= X.abs2().hi]
    if not (len(circle) == nprop and len(inside) == len(outside) == (12 - nprop) // 2):
        raise NotCertified(f'{name}: box classification does not match the Sturm count')
    key = (tt, zz)
    if key not in G_CACHE:
        G_CACHE[key] = tr.G_hom(tt, zI)
    G, _ = G_CACHE[key]
    Mh = M_site_p(RI(tt), RI(tt), zI, p)
    prop, eig_ok = [], True
    for X in circle:
        Y = bloch_vector_p(X, zI, tt, p)
        MY = matvec(Mh, Y)
        eig_ok = eig_ok and all(contains0(MY[i] - X * Y[i]) for i in range(12))
        GY = matvec(G, Y)
        F = sum((Y[i].conj() * GY[i] for i in range(12)), CI(0))
        if not (F.re.pos() or F.re.neg()):
            raise NotCertified(f'{name}: flux sign undecided')
        prop.append(dict(lam=X, Y=Y, sign=1 if F.re.pos() else -1,
                         aF=F.re if F.re.pos() else -F.re))
    ev_s, ev_l = [], []
    for X in inside + outside:
        Y = bloch_vector_p(X, zI, tt, p)
        MY = matvec(Mh, Y)
        eig_ok = eig_ok and all(contains0(MY[i] - X * Y[i]) for i in range(12))
        (ev_s if X.abs2().hi < 1 else ev_l).append(dict(lam=X, Y=Y))
    if not eig_ok:
        raise NotCertified(f'{name}: eigen-residual does not enclose 0')
    Rm = [m for m in prop if m['sign'] > 0]
    Lm = [m for m in prop if m['sign'] < 0]
    note(f'  {name}: p = {p}; propagating {len(prop)} (right {len(Rm)}, left {len(Lm)})')
    for m in prop:
        note(f'    lambda in {ci_str(m["lam"], 12)}, flux sign {m["sign"]:+d}')
    return dict(R=Rm, L=Lm, ev_small=ev_s, ev_large=ev_l, nR=len(Rm), nL=len(Lm))


def solve_hp(A, Bcols, p):
    """A x = b for each b; A n x n interval. Columns scaled by exact powers of 2;
    certified by beta = ||I - R A'||_inf < 1/2 (R from an mpmath inverse at
    precision p + 128 bits, converted exactly) and an interval residual."""
    n = len(A)
    ecol = []
    for k in range(n):
        m = max(cmag(A[i][k]) for i in range(n))
        if m == 0:
            raise NotCertified('zero column in the matching matrix')
        ecol.append(m.numerator.bit_length() - m.denominator.bit_length())
    scale = [Fr(1, 2**e) if e >= 0 else Fr(2**(-e)) for e in ecol]
    As = [[A[i][k] * CI(RI(scale[k])) for k in range(n)] for i in range(n)]
    pr = p + 128
    with mp.workprec(pr):
        Am = mp.matrix([[mid_mp(As[i][k]) for k in range(n)] for i in range(n)])
        try:
            Rf = mp.inverse(Am)
        except ZeroDivisionError:
            raise NotCertified('midpoint matching matrix numerically singular')
        Rq = [[CI(RI(rnd_fr(mpf_fr(Rf[i, k].real), pr)), RI(rnd_fr(mpf_fr(Rf[i, k].imag), pr)))
               for k in range(n)] for i in range(n)]
        RA = ch.matmul(Rq, As)
        beta = max(sum((cmag((CI(1) if i == k else CI(0)) - RA[i][k]) for k in range(n)), Fr(0))
                   for i in range(n))
        if not beta < Fr(1, 2):
            raise NotCertified(f'preconditioned matrix not contractive (beta bound {float(beta):.3g})')
        sols = []
        for b in Bcols:
            bm = mp.matrix([mid_mp(x) for x in b])
            xm = Rf * bm
            for _ in range(2):          # refinement in mpmath (guess only)
                xm = xm + Rf * (bm - Am * xm)
            xt = [CI(RI(rnd_fr(mpf_fr(xm[i].real), pr)), RI(rnd_fr(mpf_fr(xm[i].imag), pr)))
                  for i in range(n)]
            Ax = matvec(As, xt)
            res = matvec(Rq, [b[i] - Ax[i] for i in range(n)])
            err = max(cmag(r) for r in res) / (1 - beta)
            xs = [CI(RI(x.re.lo - err, x.re.hi + err), RI(x.im.lo - err, x.im.hi + err)) for x in xt]
            sols.append([xs[k] * CI(RI(scale[k])) for k in range(n)])
    return sols, beta


def t_profile(x, Lv, N, p):
    if x < -N:
        return RI(T_INT)
    if x > N:
        return RI(T_EXT)
    if x == 0:
        return RI(T_HOR)
    return rnd_RI(RI(T_HOR) + tanh_RI(x, Lv, p) * Fr(1, 16), p)


def run_point(sv, Lv, N, label, arc):
    """Returns (verdict, quantity enclosure or None, info)."""
    cw, sw, zz, zI = zdata(sv)
    for tt in (T_INT, T_EXT):
        H, Nn = tr.HN_at(tt, cw, sw)
        if not (H.degree() == 12 and sp.gcd(H, H.diff(tr.tau)).degree() == 0
                and sp.gcd(H, Nn).degree() == 0):
            note(f'{label}: S_MATRIX_NOT_ESTABLISHED (not a regular level in medium t = {tt})')
            return 'S_MATRIX_NOT_ESTABLISHED', None, {}
    try:
        base = roots_boxes(T_INT * (2 * T_INT - 1), zz, 256) + roots_boxes(T_EXT * (2 * T_EXT - 1), zz, 256)
        e = ceil_log2_kappa(base)
        p = 256 + 2 * (2 * N + 1) * e
        note(f'{label}: ceil(log2 kappa) = {e}; predeclared precision p = {p} bits; N = {N}')
        mi = medium_p(T_INT, zI, zz, cw, sw, p, f'{label} interior t=5/16')
        me = medium_p(T_EXT, zI, zz, cw, sw, p, f'{label} exterior t=7/16')
        exp_counts = (2, 4, 1, 3) if arc else (1, 3, 1, 3)
        ok(f'{label}: channel counts {exp_counts} (interior R/L, exterior R/L; reviewed counts)',
           (mi['nR'], mi['nL'], me['nR'], me['nL']) == exp_counts)
        int_out = mi['L'] + mi['ev_large']
        ext_out = me['R'] + me['ev_small']
        int_in, ext_in = mi['R'], me['L']
        vecs = [m['Y'] for m in int_out] + [m['Y'] for m in int_in]
        ts = {x: t_profile(x, Lv, N, p) for x in range(-N - 1, N + 2)}
        for x in range(-N - 1, N + 1):
            Mx = M_site_p(ts[x], ts[x + 1], zI, p)
            vecs = [[rnd_CI(y, p) for y in matvec(Mx, v)] for v in vecs]
        prop_out = vecs[:len(int_out)]
        prop_in = vecs[len(int_out):]
        note(f'{label}: propagated through {2 * N + 2} sites')
        cols = prop_out + [[-y for y in m['Y']] for m in ext_out]
        if len(cols) != 12:
            raise NotCertified('matching matrix is not 12 x 12')
        A = [[cols[k][i] for k in range(12)] for i in range(12)]
        Bcols = [[-y for y in v] for v in prop_in] + [m['Y'] for m in ext_in]
        sols, beta = solve_hp(A, Bcols, p)
        ok(f'{label}: matching matrix certified invertible (||I - R A D|| <= {dec(beta, 6, True)} < 1/2)', True)
        Fout = [m['aF'] for m in mi['L']] + [m['aF'] for m in me['R']]
        Fin = [m['aF'] for m in int_in] + [m['aF'] for m in ext_in]
        out_rows = list(range(mi['nL'])) + list(range(len(int_out), len(int_out) + me['nR']))
        nI, nO = len(Bcols), len(out_rows)
        absS2 = [[sols[c][r].abs2() * Fout[ri] / Fin[c] for c in range(nI)] for ri, r in enumerate(out_rows)]
        sq_out = [ch.sqrt_RI(f) for f in Fout]
        sq_in = [ch.sqrt_RI(f) for f in Fin]
        S = [[sols[c][r] * CI(sq_out[ri] / sq_in[c]) for c in range(nI)] for ri, r in enumerate(out_rows)]
        SHS = [[sum((S[r][a].conj() * S[r][b] for r in range(nO)), CI(0)) for b in range(nI)]
               for a in range(nI)]
        uni = all(contains0(SHS[a][b] - (CI(1) if a == b else CI(0)))
                  for a in range(nI) for b in range(nI))
        wid = max(max(SHS[a][b].re.width(), SHS[a][b].im.width()) for a in range(nI) for b in range(nI))
        ok(f'{label}: S^H S encloses the identity ({nO} x {nI}; max enclosure width {float(wid):.3g})', uni)
        if not all(cmag(SHS[a][b]) < 2 for a in range(nI) for b in range(nI)):
            raise NotCertified('S^H S enclosure too wide to be informative')
        er = mi['nL']                   # row of the exterior right-mover
        if arc:
            Q = absS2[er][0] + absS2[er][1]
            qname = 'sigma^2'
        else:
            Q = absS2[er][0]
            qname = 'T'
        note(f'{label}: {qname} in {ri_str(Q, 20)} (width {float(Q.width()):.3g})')
        if Q.lo > 0 and Q.width() <= Fr(1, 10**6):
            verdict = 'TRANSMISSION_NONZERO_CERTIFIED'
        else:
            verdict = 'OPEN_AFTER_TRANSMISSION_ANALYSIS'
        note(f'{label}: verdict {verdict}')
        return verdict, Q, dict(p=p, e=e, beta=beta)
    except NotCertified as exc:
        note(f'{label}: OPEN_AFTER_TRANSMISSION_ANALYSIS (certification step failed: {exc})')
        return 'OPEN_AFTER_TRANSMISSION_ANALYSIS', None, {}


# ================================================================= F2
F2 = {}
for sv in S_I + S_ARC:
    arc = sv in S_ARC
    F2[sv] = run_point(sv, None, 0, f'F2 s={sv}', arc)

v12, Q12, _ = F2[R(1, 2)]
v150, Q150, _ = F2[R(1, 50)]
ok('F2 cross-check: at s = 1/2 (z0) the new T enclosure overlaps the reviewed one',
   Q12 is not None and Q12.lo <= tr.T_z0.hi and tr.T_z0.lo <= Q12.hi)
ok('F2 cross-check: at s = 1/50 (z1) the new sigma^2 enclosure overlaps the reviewed one',
   Q150 is not None and Q150.lo <= tr.sig2.hi and tr.sig2.lo <= Q150.hi)

# ================================================================= F3
F3 = {}
for sv in (R(1, 50), R(1, 200)):
    for Lv, N in ((4, 32), (16, 128)):
        F3[(sv, Lv)] = run_point(sv, Lv, N, f'F3 s={sv} L={Lv} N={N}', True)

# ================================================================= summary
print('\nSUMMARY')
print(f'F1: {F1_verdict}; y* = (Re z_c*)^2 in {ri_str(y_star, 30)}')
for sv in S_I + S_ARC:
    print(f'F1 s={sv}: {F1_class[sv]}; T0-type discriminant test: '
          f'{"CONNECTED" if F1b[sv] else "not certified connected"}')
for sv in S_I + S_ARC:
    v, Q, info = F2[sv]
    print(f'F2 s={sv}: {v}' + (f'; {"sigma^2" if sv in S_ARC else "T"} in {ri_str(Q, 20)}' if Q is not None else '')
          + (f'; p = {info["p"]}' if info else ''))
for key, (v, Q, info) in F3.items():
    print(f'F3 s={key[0]} L={key[1]}: {v}' + (f'; sigma^2 in {ri_str(Q, 20)}' if Q is not None else '')
          + (f'; p = {info["p"]}' if info else ''))


def lt(a, b):
    return a.hi < b.lo


decided = all(F3[k][1] is not None and F3[k][0] == 'TRANSMISSION_NONZERO_CERTIFIED' for k in F3) \
    and all(F2[s][1] is not None for s in (R(1, 50), R(1, 200)))
if decided:
    supp = all(lt(F3[(s, 16)][1], F2[s][1]) and lt(F3[(s, 16)][1], F3[(s, 4)][1])
               for s in (R(1, 50), R(1, 200)))
    notsupp = all(F3[(s, 16)][1].lo >= Fr(1, 2) for s in (R(1, 50), R(1, 200)))
    print(f'Line: suppression condition (sigma^2(L=16) < sharp and < sigma^2(L=4) at both points): {supp}')
    print(f'Line: abandonment condition (sigma^2(L=16) >= 1/2 at both points): {notsupp}')
    if supp and not notsupp:
        line = 'LEAKAGE_SUPPRESSED_AT_COMPUTED_L'
    elif notsupp and not supp:
        line = 'LEAKAGE_NOT_SUPPRESSED'
    elif supp and notsupp:
        line = 'BOTH_CONDITIONS_HOLD (charter does not order them; reported, not resolved)'
    else:
        line = 'MIXED'
else:
    line = 'NOT_DECIDABLE (some F2/F3 point is not TRANSMISSION_NONZERO_CERTIFIED)'
print(f'Line verdict candidate: {line}')
ok('summary written', True)
print(f'{len(checks)}/{len(checks)} frequency/finite-L checks PASS '
      f'(after {len(rv.checks)} + {len(ch.checks)} + {len(tr.checks)} imported checks)')
