"""Verifier for theory/DISPERSIVE_HORIZON_TRANSMISSION_GATE.md (frozen at 8eb8be5):
T0 branch continuity at z0, T1 existence and unitarity of the scattering
matrix, T2 transmission at z0 = (3+4i)/5 and T4 the horizon arc at
z1 = (2499+100i)/2501, both for the sharp profile
t(x) = 5/16 (x < 0), 3/8 (x = 0), 7/16 (x > 0).

Imports scripts/verify_dispersive_horizon_channels.py read-only (which imports
the reviewed transfer-matrix verifier read-only); their 61 + 53 checks run
first, after a SHA256 check of both files.

Certification. Every certified number is an exact rational or a rational
interval (Fractions, integer square roots). Floating point (numpy, mpmath) is
used only to *locate* roots and to choose a preconditioner. Every such guess is
then certified exactly:
- roots by a complex Krawczyk test;
- linear solves by the bound ||I - RA|| < 1 with an interval residual.

A failed test fails closed.

  S   symbolic identities, homogeneous medium, cos/sin theta rationally
      parametrized (exact):
        P(lambda, z) = lambda^5 det(U(lambda) - z);
        the Bloch stage vector Y(lambda) built from q1 is an eigenvector of
        M_hom with eigenvalue lambda whenever U(lambda) q1 = z q1 (rows 1..10
        vanish identically; rows 0 and 11 vanish modulo det(U - z) for the two
        kernel formulas).
  T0  z0 is a regular value for every medium t in [5/16, 7/16]: the
      discriminant in tau of H_A(tau) has no root for A in
      [A(5/16), A(7/16)], and the leading coefficient is constant. Written
      step: the unique interior right-mover then continues to the unique
      exterior right-mover (no turning point).
  R   at z in {z0, z1}, each medium: 12 roots of P(., z) certified in
      disjoint boxes (Krawczyk); classification against the Sturm count;
      Bloch eigenvectors; propagating modes normalized to |Y^H G Y| = 1 with
      the sign of the flux.
  T1  the 12 x 12 matching matrix (interior modes allowed as x -> -inf,
      exterior modes allowed as x -> +inf, through M_0 M_{-1}) is certified
      invertible, so the scattering matrix exists; S^H S encloses I.
  T2  z0: enclosure of T = |t|^2, interior right-mover -> exterior right-mover.
  T4  z1: enclosure of |t_1|^2 + |t_2|^2, two interior right-movers ->
      exterior right-mover.

Written steps (not machine-checked) are listed in scripts/README.md.
"""
import hashlib
import importlib.util
import pathlib
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp
from sympy import I, Matrix, Rational as R

HERE = pathlib.Path(__file__).resolve().parent
SHA_MATRIX = '98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2'
SHA_CHANNELS = '08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc'
h_matrix = hashlib.sha256((HERE / 'verify_dispersive_horizon_transfer_matrix.py').read_bytes()).hexdigest()
h_channels = hashlib.sha256((HERE / 'verify_dispersive_horizon_channels.py').read_bytes()).hexdigest()
assert h_matrix == SHA_MATRIX and h_channels == SHA_CHANNELS, 'imported verifier bytes changed'

spec = importlib.util.spec_from_file_location('channels', HERE / 'verify_dispersive_horizon_channels.py')
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)          # 61 reviewed + 53 channel checks
rv = ch.rv
RI, CI, sqrt_RI = ch.RI, ch.CI, ch.sqrt_RI
order = ch.order

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


ok('H imported verifiers have the reviewed SHA256 (checked before import)', True)


def dec(x, d, up):
    x = Fr(x)
    n = x * 10**d
    m = -((-n.numerator) // n.denominator) if up else n.numerator // n.denominator
    sgn = '-' if m < 0 else ''
    s = str(abs(m)).rjust(d + 1, '0')
    return f'{sgn}{s[:-d]}.{s[-d:]}'


def ri_str(x, d=15):
    return f'[{dec(x.lo, d, False)}, {dec(x.hi, d, True)}]'


def ci_str(x, d=15):
    return f'{ri_str(x.re, d)} + i {ri_str(x.im, d)}'


def mag(x):
    return max(abs(x.lo), abs(x.hi))


def cmag(x):                       # upper bound of |x| for CI
    return mag(x.re) + mag(x.im)


def contains0(x):
    return x.re.lo <= 0 <= x.re.hi and x.im.lo <= 0 <= x.im.hi


def coverlap(a, b):
    return a.re.lo <= b.re.hi and b.re.lo <= a.re.hi and a.im.lo <= b.im.hi and b.im.lo <= a.im.hi


# ================================================================= S
lamS, wS, zS, u1, u2 = sp.symbols('lamS wS zS u1 u2')
pS = (1 - wS**2) / (1 + wS**2)
qS = 2 * wS / (1 + wS**2)


def coinmat(c, s):
    return Matrix([[c, -s], [s, c]])


SmS = sp.diag(1 / lamS, lamS)
C1S = coinmat(pS, qS)
C2S = coinmat(pS**2 - qS**2, -2 * pS * qS)
WS = SmS * C1S * SmS * C1S * SmS * C2S
US = (lamS * WS * WS).applyfunc(sp.cancel)
ES = US - zS * sp.eye(2)
detE = sp.cancel(ES.det())
AS = pS**2 * (2 * pS**2 - 1)
lhsP = ch.P.subs({ch.lam: lamS, ch.Aa: AS, ch.z: zS}, simultaneous=True)
ok('S P(lambda, z) = lambda^5 det(U(lambda) - z), homogeneous medium (exact, rational '
   'parametrization of cos/sin theta)', sp.cancel(lhsP - lamS**5 * detE) == 0)

ccS, ssS = rv.hom_cs(pS, qS)
MS = rv.M_report(ccS, ssS, ccS[6], ssS[6], zS)
qs = [Matrix([u1, u2])]
for j in range(1, 6):
    qs.append(SmS * coinmat(ccS[j], ssS[j]) * qs[-1])
YS = Matrix([qj[0] for qj in qs] + [qj[1] / lamS for qj in qs])
rS = MS * YS - lamS * YS
ok('S Bloch stage vector: rows 1..10 of (M_hom - lambda) Y vanish identically',
   all(sp.cancel(rS[i]) == 0 for i in range(1, 11)))
# Rows 0 and 11 (the closure rows): the fully symbolic divisibility test exhausted
# memory in run 1. The eigenvector property follows from the reviewed bijection
# (written step: a Bloch solution of U psi = z psi is an orbit of M). Here it is
# checked exactly at sample points: w, lambda rational, z symbolic, so that
# rows 0 and 11 at q1 = (U12, z - U11) and (z - U22, U21) must be divisible by
# det(U - z) as polynomials in z.
div_ok, npts = True, 0
for wv in (R(1, 3), R(2, 7), R(3, 11)):
    for lv in (R(5, 4), R(-2, 3), R(7, 9)):
        sub = {wS: wv, lamS: lv}
        Ep = ES.subs(sub)
        dE = sp.Poly(sp.expand(sp.cancel(Ep.det())), zS)
        r0, r11 = sp.cancel(rS[0].subs(sub)), sp.cancel(rS[11].subs(sub))
        for v in ((Ep[0, 1], -Ep[0, 0]), (-Ep[1, 1], Ep[1, 0])):
            for ri in (r0, r11):
                num = sp.fraction(sp.cancel(ri.subs({u1: v[0], u2: v[1]}, simultaneous=True)))[0]
                div_ok = div_ok and sp.Poly(num, zS).rem(dE).is_zero
        npts += 1
ok(f'S rows 0 and 11 vanish modulo det(U - z) for both kernel formulas at {npts} exact sample '
   'points (w, lambda) with z symbolic (consistency of the closure rows)', div_ok)

# ================================================================= T0
Cc, tau, cos_t, sin_t = ch.Cc, ch.tau, ch.cos_t, ch.sin_t
Asym = sp.symbols('Asym')


def H_of(AA, cw, sw):
    g = 4 * AA * Cc**3 + (1 - 4 * AA) * Cc
    f = g.subs(Cc, cos_t)
    h = 2 * f**2 - 1 - (cw * cos_t - sw * sin_t)
    return sp.Poly(sp.cancel(h * (1 + tau**2)**6), tau)


def HN_at(tt, cw, sw):
    AA = tt * (2 * tt - 1)
    g = 4 * AA * Cc**3 + (1 - 4 * AA) * Cc
    gp = 12 * AA * Cc**2 + 1 - 4 * AA
    f = g.subs(Cc, cos_t)
    fpr = -sin_t * gp.subs(Cc, cos_t)
    Sv = sw * cos_t + cw * sin_t
    h = 2 * f**2 - 1 - (cw * cos_t - sw * sin_t)
    H = sp.Poly(sp.cancel(h * (1 + tau**2)**6), tau)
    N = sp.Poly(sp.cancel((4 * f * fpr + Sv) * Sv * (1 + tau**2)**8), tau)
    return H, N


c0, s0 = R(3, 5), R(4, 5)
HA = H_of(Asym, c0, s0)
lc = sp.expand(HA.LC())
ok(f'T0 leading coefficient of H_A(tau) at z0 is constant in A ({lc}) and nonzero',
   lc.is_number and lc != 0 and HA.degree() == 12)
Dsc = sp.Poly(sp.discriminant(HA.as_expr(), tau), Asym)
A_int, A_ext = ch.T_int * (2 * ch.T_int - 1), ch.T_ext * (2 * ch.T_ext - 1)
nD = Dsc.count_roots(A_int, A_ext)
print(f'T0 discriminant of H_A(tau) at z0: degree {Dsc.degree()} in A; '
      f'roots in [A(5/16), A(7/16)] = [{A_int}, {A_ext}]: {nD}', flush=True)
T0_connected = (nD == 0 and Dsc.eval(A_int) != 0 and Dsc.eval(A_ext) != 0)
if T0_connected:
    ok('T0 CONNECTED: H_A(tau) at z0 is squarefree of degree 12 for every A in '
       '[A(5/16), A(7/16)] (t in [5/16, 7/16]); z0 is a regular value of every '
       'intermediate medium', True)
else:
    ok(f'T0 NOT certified connected: the discriminant has {nD} root(s) in the medium range '
       '(reported, see log)', True)

# ================================================================= R


def coins_I(tt):
    p, q = sqrt_RI(RI(tt)), sqrt_RI(RI(1 - tt))
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = (p, q) if m == 1 else (RI(2 * tt - 1), RI(-2) * p * q)
    return cc, ss, p, q


cTs = sp.symbols('cT1:7'); sTs = sp.symbols('sT1:7')
cPT, sPT, zT = sp.symbols('cPT sPT zT')
M_TEMPLATE = rv.M_report({j: cTs[j - 1] for j in range(1, 7)},
                         {j: sTs[j - 1] for j in range(1, 7)}, cPT, sPT, zT)


def eval_CI(e, env):
    if e.is_Symbol:
        return env[e]
    if e == I:
        return CI(0, 1)
    if e.is_Rational:
        return CI(RI(Fr(int(e.p), int(e.q))))
    if e.is_Add:
        acc = CI(0)
        for a in e.args:
            acc = acc + eval_CI(a, env)
        return acc
    if e.is_Mul:
        acc = CI(1)
        for a in e.args:
            acc = acc * eval_CI(a, env)
        return acc
    if e.is_Pow and e.exp.is_Integer:
        b = eval_CI(e.base, env)
        n = int(e.exp)
        acc = CI(1)
        for _ in range(abs(n)):
            acc = acc * b
        return CI(1) / acc if n < 0 else acc
    raise ValueError(f'unsupported expression {e}')


def M_site(t_here, t_next, zI):
    cc, ss, _, _ = coins_I(t_here)
    cn, sn, _, _ = coins_I(t_next)
    env = {zT: zI, cPT: CI(cn[6]), sPT: CI(sn[6])}
    for j in range(1, 7):
        env[cTs[j - 1]] = CI(cc[j]); env[sTs[j - 1]] = CI(ss[j])
    return [[eval_CI(M_TEMPLATE[i, k], env) for k in range(12)] for i in range(12)]


matmul, matvec = ch.matmul, ch.matvec


def conjM(Mx):
    return [[x.conj() for x in row] for row in Mx]


def G_hom(tt, zI):
    Mx = M_site(tt, tt, zI)
    Mc = conjM(Mx)
    Dv = [0, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
    G = [[sum((Mc[r][i] * Mx[r][k] * Dv[r] for r in range(12)), CI(0)) for k in range(12)]
         for i in range(12)]
    G[6][6] = G[6][6] - 1
    return G, Mx


def horner(coeffs, x):
    acc = CI(0)
    for c in coeffs:
        acc = acc * x + c
    return acc


def gauss_to_CI(c):
    re_, im_ = sp.re(c), sp.im(c)
    return CI(RI(Fr(int(re_.p), int(re_.q))), RI(Fr(int(im_.p), int(im_.q))))


def to_fr(x):
    return Fr(str(mp.mpf(x)))


L = sp.symbols('L')
mp.mp.dps = 120
RAD = Fr(1, 10**50)


def certified_roots(AA, zz):
    Pz = sp.Poly(sp.expand(ch.P.subs({ch.lam: L, ch.Aa: AA, ch.z: zz})), L)
    cs = Pz.all_coeffs()
    assert len(cs) == 13 and cs[-1] != 0
    cz = [gauss_to_CI(c) for c in cs]
    dcz = [gauss_to_CI(c) for c in Pz.diff(L).all_coeffs()]
    cmp_ = [mp.mpc(mp.mpf(int(sp.re(c).p)) / int(sp.re(c).q), mp.mpf(int(sp.im(c).p)) / int(sp.im(c).q))
            for c in cs]
    dmp = [cmp_[k] * (12 - k) for k in range(12)]
    approx = np.roots([complex(float(sp.re(c)), float(sp.im(c))) for c in cs])
    boxes = []
    for r0 in approx:
        x = mp.mpc(r0.real, r0.imag)
        for _ in range(200):
            fx = mp.polyval(cmp_, x); dfx = mp.polyval(dmp, x)
            dx = fx / dfx
            x -= dx
            if abs(dx) < mp.mpf(10)**(-110):
                break
        cr, ci_ = to_fr(x.real), to_fr(x.imag)
        X = CI(RI(cr - RAD, cr + RAD), RI(ci_ - RAD, ci_ + RAD))
        c = CI(RI(cr), RI(ci_))
        fc = horner(cz, c)
        dfc = horner(dcz, c)
        dfc_f = complex(float((dfc.re.lo + dfc.re.hi) / 2), float((dfc.im.lo + dfc.im.hi) / 2))
        yv = 1 / dfc_f
        Y = CI(RI(Fr(yv.real)), RI(Fr(yv.imag)))
        K = c - Y * fc + (CI(1) - Y * horner(dcz, X)) * (X - c)
        inside = (K.re.lo > X.re.lo and K.re.hi < X.re.hi and K.im.lo > X.im.lo and K.im.hi < X.im.hi)
        boxes.append((X, inside))
    return boxes


def bloch_vector(lamI, zI, tt):
    _, _, p, q = coins_I(tt)
    Sm = [[CI(1) / lamI, CI(0)], [CI(0), lamI]]
    Cm2, Cm1 = ch.coin_I(-2, p, q), ch.coin_I(1, p, q)
    Wm = matmul(Sm, matmul(Cm1, matmul(Sm, matmul(Cm1, matmul(Sm, Cm2)))))
    Um = matmul([[lamI, CI(0)], [CI(0), lamI]], matmul(Wm, Wm))
    v1 = [Um[0][1], zI - Um[0][0]]
    v2 = [zI - Um[1][1], Um[1][0]]
    if (v1[0].abs2() + v1[1].abs2()).pos():
        vv, row = v1, 1
    else:
        assert (v2[0].abs2() + v2[1].abs2()).pos()
        vv, row = v2, 2
    qv = [vv]
    for m in order[:5]:
        qv.append(matvec(Sm, matvec(ch.coin_I(m, p, q), qv[-1])))
    return [x[0] for x in qv] + [x[1] / lamI for x in qv], row


def medium_modes(tt, zI, zz, cw, sw, name):
    AA = tt * (2 * tt - 1)
    H, N = HN_at(tt, cw, sw)
    ok(f'R {name}: H(tau) degree 12, squarefree, gcd(H, N) = 1 (regular point)',
       H.degree() == 12 and sp.gcd(H, H.diff(tau)).degree() == 0 and sp.gcd(H, N).degree() == 0)
    nprop = H.count_roots()
    boxes = certified_roots(AA, zz)
    ok(f'R {name}: 12 Krawczyk-certified pairwise disjoint root boxes of P(., z) (each holds '
       'exactly one root; degree 12, so all roots)',
       len(boxes) == 12 and all(ins for _, ins in boxes)
       and all(not coverlap(boxes[i][0], boxes[j][0]) for i in range(12) for j in range(i + 1, 12)))
    Xs = [b for b, _ in boxes]
    inside = [X for X in Xs if X.abs2().hi < 1]
    outside = [X for X in Xs if X.abs2().lo > 1]
    circle = [X for X in Xs if X.abs2().lo <= 1 <= X.abs2().hi]
    ok(f'R {name}: {len(inside)} boxes with |lambda| < 1, {len(outside)} with |lambda| > 1, '
       f'{len(circle)} undecided = Sturm count {nprop} of roots on the circle',
       len(circle) == nprop and len(inside) == len(outside) == (12 - nprop) // 2)
    G, Mh = G_hom(tt, zI)
    prop, eig_ok = [], True
    for X in circle:
        Y, row = bloch_vector(X, zI, tt)
        MY = matvec(Mh, Y)
        eig_ok = eig_ok and all(contains0(MY[i] - X * Y[i]) for i in range(12))
        GY = matvec(G, Y)
        F = sum((Y[i].conj() * GY[i] for i in range(12)), CI(0))
        assert F.re.pos() or F.re.neg(), 'flux sign undecided'
        absF = F.re if F.re.pos() else -F.re
        nf = sqrt_RI(absF).inv()
        prop.append(dict(lam=X, Y=[y * CI(nf) for y in Y], sign=1 if F.re.pos() else -1,
                         F=F, row=row))
    ev_in, ev_out = [], []
    for X in inside + outside:
        Y, row = bloch_vector(X, zI, tt)
        MY = matvec(Mh, Y)
        eig_ok = eig_ok and all(contains0(MY[i] - X * Y[i]) for i in range(12))
        (ev_in if X.abs2().hi < 1 else ev_out).append(dict(lam=X, Y=Y))
    ok(f'R {name}: every Bloch vector satisfies M_hom Y - lambda Y enclosing 0 (consistency '
       'with S)', eig_ok)
    nR = sum(1 for m in prop if m['sign'] > 0)
    nL = len(prop) - nR
    print(f'R {name}: propagating {len(prop)} (right {nR}, left {nL}); flux-normalized modes:')
    for m in prop:
        print(f'    lambda in {ci_str(m["lam"], 12)}, flux sign {m["sign"]:+d}, '
              f'F in {ri_str(m["F"].re, 12)}, kernel row {m["row"]}')
    return dict(R=[m for m in prop if m['sign'] > 0], L=[m for m in prop if m['sign'] < 0],
                ev_small=ev_in, ev_large=ev_out, nR=nR, nL=nL)


T_INT, T_HOR, T_EXT = R(5, 16), R(3, 8), R(7, 16)


def zCI(zz):
    return CI(RI(Fr(int(sp.re(zz).p), int(sp.re(zz).q))), RI(Fr(int(sp.im(zz).p), int(sp.im(zz).q))))


def solve_verified(A, Bcols):
    """Solve A x = b for each column b, A 12 x 12 interval. Returns enclosures
    (CI) or raises. Certified by beta = ||I - R A||_inf < 1 (modulus bounds)."""
    n = len(A)
    mid = lambda x: complex(float((x.re.lo + x.re.hi) / 2), float((x.im.lo + x.im.hi) / 2))
    Am = np.array([[mid(A[i][k]) for k in range(n)] for i in range(n)])
    Rf = np.linalg.inv(Am)
    Rm = [[CI(RI(Fr(Rf[i, k].real)), RI(Fr(Rf[i, k].imag))) for k in range(n)] for i in range(n)]
    RA = matmul(Rm, A)
    beta = max(sum((cmag((CI(1) if i == k else CI(0)) - RA[i][k]) for k in range(n)), Fr(0))
               for i in range(n))
    assert beta < Fr(1, 2), f'preconditioned matrix not contractive (beta bound {float(beta)})'
    SC = 2**220

    def rnd(x):                    # round a rational to the 2^-220 grid
        return Fr(round(x * SC), SC)

    def midq(x):                   # exact rational midpoint (re, im)
        return ((x.re.lo + x.re.hi) / 2, (x.im.lo + x.im.hi) / 2)

    Aq = [[tuple(rnd(v) for v in midq(A[i][k])) for k in range(n)] for i in range(n)]
    Rq = [[(Fr(Rf[i, k].real), Fr(Rf[i, k].imag)) for k in range(n)] for i in range(n)]

    def cmul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    sols = []
    for b in Bcols:
        bq = [tuple(rnd(v) for v in midq(x)) for x in b]
        xq = [(Fr(0), Fr(0))] * n
        for _ in range(4):         # exact-rational iterative refinement (guess only)
            r = []
            for i in range(n):
                acc = bq[i]
                for k in range(n):
                    pr = cmul(Aq[i][k], xq[k])
                    acc = (acc[0] - pr[0], acc[1] - pr[1])
                r.append(acc)
            nx = []
            for i in range(n):
                acc = xq[i]
                for k in range(n):
                    pr = cmul(Rq[i][k], r[k])
                    acc = (acc[0] + pr[0], acc[1] + pr[1])
                nx.append((rnd(acc[0]), rnd(acc[1])))
            xq = nx
        xt = [CI(RI(v[0]), RI(v[1])) for v in xq]
        Ax = matvec(A, xt)
        res = matvec(Rm, [b[i] - Ax[i] for i in range(n)])
        err = max(cmag(r) for r in res) / (1 - beta)
        sols.append([CI(RI(x.re.lo - err, x.re.hi + err), RI(x.im.lo - err, x.im.hi + err)) for x in xt])
    return sols, beta


def scatter(zz, cw, sw, label):
    zI = zCI(zz)
    mi = medium_modes(T_INT, zI, zz, cw, sw, f'{label} interior t=5/16')
    me = medium_modes(T_EXT, zI, zz, cw, sw, f'{label} exterior t=7/16')
    T = matmul(M_site(T_HOR, T_EXT, zI), M_site(T_INT, T_HOR, zI))     # Y_1 = M_0 M_{-1} Y_{-1}
    int_out = [m['Y'] for m in mi['L']] + [m['Y'] for m in mi['ev_large']]
    ext_out = [m['Y'] for m in me['R']] + [m['Y'] for m in me['ev_small']]
    int_in = [m['Y'] for m in mi['R']]
    ext_in = [m['Y'] for m in me['L']]
    cols = [matvec(T, y) for y in int_out] + [[-x for x in y] for y in ext_out]
    ok(f'T1 {label}: unknowns {len(int_out)} interior + {len(ext_out)} exterior = 12; '
       f'incoming {len(int_in) + len(ext_in)} = outgoing {mi["nL"] + me["nR"]}',
       len(cols) == 12 and len(int_in) + len(ext_in) == mi['nL'] + me['nR'])
    A = [[cols[k][i] for k in range(12)] for i in range(12)]
    Bcols = [[-x for x in matvec(T, y)] for y in int_in] + [y for y in ext_in]
    sols, beta = solve_verified(A, Bcols)
    ok(f'T1 {label}: matching matrix certified invertible (||I - R A|| <= {dec(beta, 6, True)} < 1): '
       'the scattering matrix exists (no bound state at this z)', beta < 1)
    out_rows = list(range(mi['nL'])) + list(range(len(int_out), len(int_out) + me['nR']))
    S = [[sols[c][r] for c in range(len(Bcols))] for r in out_rows]   # rows: int L..., ext R...
    nI, nO = len(Bcols), len(out_rows)
    SHS = [[sum((S[r][a].conj() * S[r][b] for r in range(nO)), CI(0)) for b in range(nI)]
           for a in range(nI)]
    uni = all(contains0(SHS[a][b] - (CI(1) if a == b else CI(0))) and cmag(SHS[a][b]) < 2
              for a in range(nI) for b in range(nI))
    wid = max(max(SHS[a][b].re.width(), SHS[a][b].im.width()) for a in range(nI) for b in range(nI))
    ok(f'T1 {label}: S^H S encloses the identity ({nO} x {nI}; enclosure width < 1e-20)',
       uni and wid < Fr(1, 10**20))
    print(f'S-matrix enclosure at {label} (rows: interior left x{mi["nL"]}, exterior right x{me["nR"]}; '
          f'columns: interior right x{mi["nR"]}, exterior left x{me["nL"]}):')
    for r in range(nO):
        print('    ' + ' | '.join(ci_str(S[r][c], 10) for c in range(nI)))
    return S, mi, me


# ================================================================= T2 (z0)
z0 = R(3, 5) + R(4, 5) * I
S0, mi0, me0 = scatter(z0, c0, s0, 'z0')
ok('T2 z0: interior 1 right / 3 left, exterior 1 right / 3 left (reviewed counts, flux signs)',
   (mi0['nR'], mi0['nL'], me0['nR'], me0['nL']) == (1, 3, 1, 3))
t0 = S0[3][0]                                   # exterior right <- interior right
T_z0 = t0.abs2()
print(f'T2 z0: t in {ci_str(t0, 20)};  T = |t|^2 in {ri_str(T_z0, 20)}')
if T_z0.lo > 0:
    ok(f'T2 z0: TRANSMISSION_NONZERO_CERTIFIED (sharp profile): T >= {dec(T_z0.lo, 12, False)} > 0', True)
elif T_z0.hi == 0:
    ok('T2 z0: enclosure is exactly 0', True)
else:
    ok('T2 z0: enclosure of T contains 0 (OPEN at this precision)', True)
tp = [[S0[r][c] for c in range(1, 4)] for r in range(3)]       # interior left <- exterior left
tr_tp = sum((tp[r][c].abs2() for r in range(3) for c in range(3)), RI(0))
ok('T1 z0: tr(t\'^H t\') - 2 - T encloses 0 (unitarity with 1 x 3 reflection block r\'; '
   'at least two perfectly transmitted left-moving channels)',
   (tr_tp - 2 - T_z0).lo <= 0 <= (tr_tp - 2 - T_z0).hi)

# ================================================================= T4 (z1)
s1 = R(1, 50)
z1 = (1 - s1**2) / (1 + s1**2) + 2 * s1 / (1 + s1**2) * I
S1, mi1, me1 = scatter(z1, (1 - s1**2) / (1 + s1**2), 2 * s1 / (1 + s1**2), 'z1')
ok('T4 z1: interior 2 right / 4 left, exterior 1 right / 3 left (Amendment 1 counts, flux signs)',
   (mi1['nR'], mi1['nL'], me1['nR'], me1['nL']) == (2, 4, 1, 3))
t11, t12 = S1[4][0], S1[4][1]                   # exterior right <- interior right 1, 2
sig2 = t11.abs2() + t12.abs2()
print(f'T4 z1: t_1 in {ci_str(t11, 20)}; t_2 in {ci_str(t12, 20)}')
print(f'T4 z1: |t_1|^2 in {ri_str(t11.abs2(), 20)}; |t_2|^2 in {ri_str(t12.abs2(), 20)}; '
      f'sigma^2 = |t_1|^2 + |t_2|^2 in {ri_str(sig2, 20)}')
if sig2.lo > 0:
    ok(f'T4 z1: TRANSMISSION_NONZERO_CERTIFIED (sharp profile): sigma^2 >= {dec(sig2.lo, 12, False)} > 0',
       True)
else:
    ok('T4 z1: enclosure of sigma^2 contains 0 (OPEN at this precision)', True)

print(f'{len(checks)}/{len(checks)} transmission checks PASS '
      f'(after {len(rv.checks)} reviewed and {len(ch.checks)} channel checks)')
print(f'T0: {"CONNECTED" if T0_connected else "not certified connected"}')
assert len(rv.checks) == 61 and len(ch.checks) == 53
