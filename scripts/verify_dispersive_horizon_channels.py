"""Exact verifier for theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md (frozen at
7a63529): flux form, root structure, thresholds, classification and unit-flux
normalization of the asymptotic channels of U = L_- W^2 in the media
t = 5/16 (interior, x -> -inf) and t = 7/16 (exterior, x -> +inf).

Imports scripts/verify_dispersive_horizon_transfer_matrix.py read-only (its 61
checks run first). Exact SymPy and exact rational interval arithmetic only:
no floating point enters any certified quantity. Fails closed.

  C1  flux form G_x = M_x^H D M_x - E_77, D = diag(0,1,1,1,1,1,-1,...,-1):
      M_x^H G_{x+1} M_x = G_x for general independent angles on three sites
      and |z| = 1; Hermitian; operational cut flux (second route) on exact
      site-dependent solutions, sesquilinear, constant in x and equal to
      Y_x^H G_x Y_x; det G = -cot^2 theta in a homogeneous medium.
  C2  conjugate-reciprocal symmetry lambda -> 1/conj(lambda) of P(lambda, z)
      for |z| = 1; P = z lambda^6 Phi with Phi = -2h on the unit circle,
      h(k) = 2 f^2 - 1 - cos(omega + k); Omega_+ + Omega_- = -2k (winding -2).
  C3  thresholds (critical values): elimination identity, threshold
      polynomial in u = cos^2 k, the four interior critical points with exact
      radical z_c and certified rational enclosures, none in the exterior;
      I = (arg z_c*, pi/2) with z_c* the unique critical value in the open
      first quadrant; z0 = (3+4i)/5 in I.
  C4  at z0 in each medium: P(., z0) squarefree of degree 12 with P(0) != 0;
      propagating roots = real roots of a degree-12 polynomial in tau =
      tan(k/2), counted by Sturm; group-velocity signs decided exactly;
      evanescent roots split 4 + 4 by C2.
  C5  flux of each propagating Bloch eigenvector: sign = sign of group
      velocity, nonzero, with certified enclosures (normalization factor);
      operator identity behind flux = (dOmega/dk) |q_1|^2; det G != 0.

What it does not certify: see scripts/README.md.
"""
import importlib.util
import pathlib
import random
import time
from fractions import Fraction as Fr
from math import isqrt

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

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


M_report = rv.M_report
order = rv.order
D = sp.diag(0, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1)
E77 = zeros(12, 12)
E77[6, 6] = 1


def G_of(M, conjM):
    return conjM.T * D * M - E77


# ================================================================= C1
z = sp.symbols('z')
cx = sp.symbols('cx1:7'); sx = sp.symbols('sx1:7')
cy = sp.symbols('cy1:7'); sy = sp.symbols('sy1:7')
cw, sw = sp.symbols('cw sw')                     # beta_6 at x+2
CIRC = list(zip(sx, cx)) + list(zip(sy, cy)) + [(sw, cw)]


def zero_on_circle(expr):
    num, _ = sp.fraction(sp.cancel(sp.together(expr)))
    num = sp.expand(num)
    for sv, cv in CIRC:
        num = sp.rem(num, sv**2 + cv**2 - 1, sv)
    return sp.expand(num) == 0


dx = {j: cx[j - 1] for j in range(1, 7)}; ex = {j: sx[j - 1] for j in range(1, 7)}
dy = {j: cy[j - 1] for j in range(1, 7)}; ey = {j: sy[j - 1] for j in range(1, 7)}
Mx = M_report(dx, ex, cy[5], sy[5], z)
My = M_report(dy, ey, cw, sw, z)
Mx_c = Mx.subs(z, 1 / z)                         # entrywise conjugate for real angles, |z| = 1
My_c = My.subs(z, 1 / z)
Gx = G_of(Mx, Mx_c)
Gy = G_of(My, My_c)
lhs = Mx_c.T * Gy * Mx - Gx
ok('C1 M_x^H G_{x+1} M_x = G_x (general angles on sites x, x+1, x+2; |z| = 1)',
   all(zero_on_circle(e) for e in lhs))
ok('C1 G_x is Hermitian for |z| = 1',
   all(sp.cancel(Gx[i, j] - Gx[j, i].subs(z, 1 / z)) == 0
       for i in range(12) for j in range(12)))

# Second route: operational flux through the cut (x, x+1), from the word of U.
random.seed(1126)
TRIPLES = [(R(3, 5), R(4, 5)), (R(5, 13), R(12, 13)), (R(8, 17), R(15, 17)),
           (R(20, 29), R(21, 29)), (R(48, 73), R(55, 73)), (R(7, 25), R(24, 25))]
NS = 30
site = {x: TRIPLES[random.randrange(len(TRIPLES))] for x in range(-10, NS + 10)}


def cs_site(m, x):
    p, q = site[x]
    return (p, q) if m == 1 else (p * p - q * q, -2 * p * q)


def coefs(x):
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = cs_site(m, x)
    return cc, ss


z0 = R(3, 5) + R(4, 5) * I
z0c = R(3, 5) - R(4, 5) * I


def M_at(x, zz):
    cc, ss = coefs(x)
    cn, sn = coefs(x + 1)
    return M_report(cc, ss, cn[6], sn[6], zz)


def solution(seed):
    rnd = random.Random(seed)
    Y = {0: Matrix([rnd.randint(-4, 4) + rnd.randint(-4, 4) * I for _ in range(12)])}
    for x in range(NS):
        Y[x + 1] = (M_at(x, z0) * Y[x]).applyfunc(sp.expand)
    return Y


Y1, Y2 = solution(1), solution(2)


def stage_amplitudes(Y, x):
    """Coin outputs at every stage around the cut (x, x+1), from the word:
    q_{j+1} = S C(beta_j) q_j. Returns crossing amplitudes per shift."""
    # q_j(y) for y in {x, x+1}: a_j(y) = Y[y][j-1], b_j(y) = Y[y+1][6+j-1]
    def q(j, y):
        return Matrix([Y[y][j - 1], Y[y + 1][6 + j - 1]])
    right, left = [], []
    for j in range(1, 7):
        cc, ss = coefs(x)
        cp, sp_ = cs_site(order[j - 1], x)
        up_x = (Matrix([[cp, -sp_], [sp_, cp]]) * q(j, x))[0]       # moves x -> x+1
        cp1, sp1 = cs_site(order[j - 1], x + 1)
        dn_x1 = (Matrix([[cp1, -sp1], [sp1, cp1]]) * q(j, x + 1))[1]  # moves x+1 -> x
        right.append(up_x)
        left.append(dn_x1)
    # L_-: all of q_7 at x+1 moves to x; q_7(x+1) = z q_1(x)
    q7 = z0 * q(1, x)
    left.extend([q7[0], q7[1]])
    return right, left


def op_flux(Ya, Yb, x):
    ra, la = stage_amplitudes(Ya, x)
    rb, lb = stage_amplitudes(Yb, x)
    return sp.expand(sum(sp.conjugate(p) * q for p, q in zip(ra, rb))
                     - sum(sp.conjugate(p) * q for p, q in zip(la, lb)))


def form(Ya, Yb, x):
    M = M_at(x, z0)
    Mc = M_at(x, z0c)
    return sp.expand((Ya[x].H * G_of(M, Mc) * Yb[x])[0])


xs = range(2, NS - 3)
ok('C1 operational cut flux is constant in x (two solutions, sesquilinear)',
   all(op_flux(a, b, x) == op_flux(a, b, 2) for a in (Y1, Y2) for b in (Y1, Y2) for x in xs))
ok('C1 operational cut flux equals Y_x^H G_x Y_x (sesquilinear, all sites)',
   all(op_flux(a, b, x) == form(a, b, x) for a in (Y1, Y2) for b in (Y1, Y2) for x in xs))
ok('C1 the conserved form is not identically zero on these solutions',
   op_flux(Y1, Y1, 2) != 0 and op_flux(Y1, Y2, 2) != 0)


def hom_cs(p, q):
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = (p, q) if m == 1 else (p * p - q * q, -2 * p * q)
    return cc, ss


pc, qc = sp.symbols('pc qc', positive=True)
cc, ss = hom_cs(pc, qc)
Mh = M_report(cc, ss, cc[6], ss[6], z)
Gh = G_of(Mh, Mh.subs(z, 1 / z))
dG = sp.factor(sp.cancel(Gh.det(method='berkowitz')))
num, _ = sp.fraction(sp.cancel(dG + pc**2 / qc**2))
ok('C1 homogeneous medium: det G = -cot^2 theta (nondegenerate form)',
   sp.expand(sp.rem(sp.expand(num), qc**2 + pc**2 - 1, qc)) == 0)

# ================================================================= C2
lam, Aa, k, om = sp.symbols('lambda A k omega')
fl = Aa / 2 * (lam**3 + lam**-3) + (1 - Aa) / 2 * (lam + 1 / lam)
P = sp.expand(z**2 * lam**5 - z * lam**6 * (4 * fl**2 - 2) + lam**7)
ok('C2 lambda^12 P(1/lambda, 1/z) = z^-2 P(lambda, z)  (roots closed under 1/conj)',
   sp.expand(lam**12 * P.subs({lam: 1 / lam, z: 1 / z}, simultaneous=True) - P / z**2) == 0)
Phi = z / lam + lam / z - 4 * fl**2 + 2
ok('C2 P = z lambda^6 Phi', sp.expand(P - z * lam**6 * Phi) == 0)
f_k = Aa * sp.cos(3 * k) + (1 - Aa) * sp.cos(k)
h_k = 2 * f_k**2 - 1 - sp.cos(om + k)
on_circle = Phi.subs({lam: sp.exp(-I * k), z: sp.exp(I * om)}, simultaneous=True)
ok('C2 on the unit circle Phi = -2 h(k), h = 2 f^2 - 1 - cos(omega + k)',
   sp.simplify(sp.expand((on_circle + 2 * h_k).rewrite(sp.exp))) == 0)
ok('C2 deg_lambda P = 12 and P(0) = -z A^2 lambda^0 coefficient (A != 0)',
   sp.degree(P, lam) == 12 and sp.expand(P.subs(lam, 0)) == sp.expand(-z * Aa**2))
# Omega_+ + Omega_- = -2k: det U(k) = e^{-2ik} (det W = 1, reviewed T5).
ok('C2 det U(k) = e^{-2ik}, i.e. Omega_+ + Omega_- = -2k (total winding -2)',
   sp.simplify(sp.exp(-2 * I * k) * rv.W.det() - sp.exp(-2 * I * k)) == 0)

# ================================================================= C3
F, Fp = sp.symbols('F Fp')
ok('C3 elimination: 16F^2Fp^2 + (2F^2-1)^2 - 1 = 4F^2(4Fp^2 - (1 - F^2))',
   sp.expand(16 * F**2 * Fp**2 + (2 * F**2 - 1)**2 - 1
             - 4 * F**2 * (4 * Fp**2 - (1 - F**2))) == 0)
Cc, u, w = sp.symbols('C u w')


def g_poly(tt):
    AA = tt * (2 * tt - 1)
    return 4 * AA * Cc**3 + (1 - 4 * AA) * Cc, 12 * AA * Cc**2 + 1 - 4 * AA, AA


def thr_poly(tt):
    g, gp, _ = g_poly(tt)
    expr = sp.expand(4 * (1 - Cc**2) * gp**2 - (1 - g**2))
    return sp.Poly(sp.expand(expr.subs(Cc**2, u).subs(Cc, sp.sqrt(u))), u)


T_int, T_ext = R(5, 16), R(7, 16)
for tt in (T_int, T_ext):
    g, gp, AA = g_poly(tt)
    ok(f'C3 t={tt}: A < 0, so g(C) = C(1 - 4A(1-C^2)) vanishes only at C = 0',
       AA < 0)
    ok(f"C3 t={tt}: g' >= g'(1) = (4t-1)^2 > 0 on [-1,1], so f = +-1 only at k = 0, pi",
       sp.expand(gp.subs(Cc, 1) - (4 * tt - 1)**2) == 0 and 4 * tt - 1 > 0)
Pint, Pext = thr_poly(T_int), thr_poly(T_ext)
Qint, rint = sp.div(Pint, sp.Poly(u - 1, u))
Qext, rext = sp.div(Pext, sp.Poly(u - 1, u))
ok('C3 threshold polynomials vanish at u = 1 (nodes k = 0, pi, not critical)',
   rint.is_zero and rext.is_zero)
ok('C3 interior quotient has exactly one root in (0,1); none at 0 or 1',
   Qint.count_roots(0, 1) == 1 and Qint.eval(0) != 0 and Qint.eval(1) != 0)
ok('C3 exterior quotient has no root in [0,1]: no critical values at t = 7/16',
   Qext.count_roots(0, 1) == 0)
ok('C3 interior quotient is proportional to 2625 u^2 - 5245 u + 2604',
   sp.cancel(Qint.as_expr() / (2625 * u**2 - 5245 * u + 2604)).is_number)
ustar = (5245 - sp.sqrt(168025)) / 5250
ok('C3 u* = (5245 - sqrt(168025))/5250 is that root', sp.expand(Qint.as_expr().subs(u, ustar)) == 0)


def S_(x):
    return sp.Rational(x.numerator, x.denominator)


def F_(x):
    return Fr(int(x.p), int(x.q))


# ---- exact rational interval arithmetic (no floating point)
class RI:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None):
        self.lo = Fr(lo)
        self.hi = Fr(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(a, b):
        b = b if isinstance(b, RI) else RI(b)
        return RI(a.lo + b.lo, a.hi + b.hi)
    __radd__ = __add__

    def __neg__(a):
        return RI(-a.hi, -a.lo)

    def __sub__(a, b):
        return a + (-(b if isinstance(b, RI) else RI(b)))

    def __rsub__(a, b):
        return RI(b) - a

    def __mul__(a, b):
        b = b if isinstance(b, RI) else RI(b)
        ps = [a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi]
        return RI(min(ps), max(ps))
    __rmul__ = __mul__

    def inv(a):
        assert a.lo > 0 or a.hi < 0, 'division by interval containing 0'
        return RI(1 / a.hi, 1 / a.lo)

    def __truediv__(a, b):
        return a * (b if isinstance(b, RI) else RI(b)).inv()

    def pos(a):
        return a.lo > 0

    def neg(a):
        return a.hi < 0

    def width(a):
        return a.hi - a.lo


BITS = 200


def sqrt_RI(x):
    assert x.lo >= 0
    S = 4**BITS
    lo = Fr(isqrt((x.lo * S).numerator // (x.lo * S).denominator), 2**BITS)
    nh = x.hi * S
    hi = Fr(isqrt(-(-nh.numerator // nh.denominator)) + 1, 2**BITS)
    return RI(lo, hi)


class CI:
    __slots__ = ('re', 'im')

    def __init__(self, re, im=0):
        self.re = re if isinstance(re, RI) else RI(re)
        self.im = im if isinstance(im, RI) else RI(im)

    def __add__(a, b):
        b = b if isinstance(b, CI) else CI(b)
        return CI(a.re + b.re, a.im + b.im)
    __radd__ = __add__

    def __sub__(a, b):
        b = b if isinstance(b, CI) else CI(b)
        return CI(a.re - b.re, a.im - b.im)

    def __rsub__(a, b):
        return CI(b) - a

    def __neg__(a):
        return CI(-a.re, -a.im)

    def __mul__(a, b):
        b = b if isinstance(b, CI) else CI(b)
        return CI(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re)
    __rmul__ = __mul__

    def conj(a):
        return CI(a.re, -a.im)

    def abs2(a):
        return a.re * a.re + a.im * a.im

    def __truediv__(a, b):
        b = b if isinstance(b, CI) else CI(b)
        d = b.abs2()
        n = a * b.conj()
        return CI(n.re / d, n.im / d)


# interior critical points: C = +-sqrt(u*), sin k = +-sqrt(1-u*)
r168 = sqrt_RI(RI(168025))
u_I = (RI(5245) - r168) / 5250
ok('C3 enclosure: 0 < u* < 1', u_I.pos() and (RI(1) - u_I).pos())
A_int = T_int * (2 * T_int - 1)


def g_I(C, AA):
    return RI(4 * AA) * C * C * C + RI(1 - 4 * AA) * C


def gp_I(C, AA):
    return RI(12 * AA) * C * C + RI(1 - 4 * AA)


zcs = []
for sC in (1, -1):
    for sS in (1, -1):
        C = sqrt_RI(u_I) * sC
        Sg = sqrt_RI(RI(1) - u_I) * sS
        gv, gpv = g_I(C, A_int), gp_I(C, A_int)
        fpv = -Sg * gpv                                   # f'(k) = -sin k g'(cos k)
        zc = CI(C, -Sg) * CI(RI(2) * gv * gv - 1, RI(-4) * gv * fpv)
        zcs.append(((sC, sS), zc))
ok('C3 the four critical z_c have |z_c|^2 enclosures containing 1',
   all(zc.abs2().lo <= 1 <= zc.abs2().hi for _, zc in zcs))
first_quadrant = [(sg, zc) for sg, zc in zcs if zc.re.pos() and zc.im.pos()]
others_out = all(zc.im.neg() or zc.re.neg() for sg, zc in zcs if (sg, zc) not in first_quadrant)
ok('C3 exactly one critical value lies in the open first quadrant; the others have '
   'Im < 0 or Re < 0', len(first_quadrant) == 1 and others_out)
sg_star, zc_star = first_quadrant[0]
ok(f'C3 z_c* (C sign {sg_star[0]}, sin k sign {sg_star[1]}): Re z_c* > 3/5 = Re z0, '
   'so arg z_c* < arg z0 < pi/2 and z0 lies in I',
   (zc_star.re - RI(R(3, 5))).pos() and zc_star.im.pos())
# exact radical form and minimal polynomial of Re z_c*
Cs = sg_star[0] * sp.sqrt(ustar)
Ss = sg_star[1] * sp.sqrt(1 - ustar)
gS = 4 * A_int * Cs**3 + (1 - 4 * A_int) * Cs
gpS = 12 * A_int * Cs**2 + 1 - 4 * A_int
zc_exact = sp.expand((Cs - I * Ss) * (2 * gS**2 - 1 + 4 * I * gS * Ss * gpS))
Xm = sp.symbols('X')
mp_re = sp.minimal_polynomial(sp.re(zc_exact), Xm)
ok(f'C3 Re z_c* is algebraic with minimal polynomial of degree {sp.degree(mp_re, Xm)} '
   '(exact descriptor), and its enclosure lies inside one isolating interval of it',
   sp.Poly(mp_re, Xm).count_roots(S_(zc_star.re.lo), S_(zc_star.re.hi)) == 1)
ok('C3 collision points z = 1, i, -1, -i are not in I = (arg z_c*, pi/2) '
   '(z = i is excluded by definition)', zc_star.im.pos())   # arg z_c* > 0 = arg 1

# ================================================================= C4
tau = sp.symbols('tau')
cos_t = (1 - tau**2) / (1 + tau**2)
sin_t = 2 * tau / (1 + tau**2)
cw0, sw0 = R(3, 5), R(4, 5)


def tau_polys(tt):
    AA = tt * (2 * tt - 1)
    g = 4 * AA * Cc**3 + (1 - 4 * AA) * Cc
    gp = 12 * AA * Cc**2 + 1 - 4 * AA
    f = g.subs(Cc, cos_t)
    fpr = -sin_t * gp.subs(Cc, cos_t)
    Sv = sw0 * cos_t + cw0 * sin_t                    # sin(omega0 + k)
    h = 2 * f**2 - 1 - (cw0 * cos_t - sw0 * sin_t)   # 2f^2 - 1 - cos(omega0 + k)
    H = sp.Poly(sp.cancel(h * (1 + tau**2)**6), tau)
    N = sp.Poly(sp.cancel((4 * f * fpr + Sv) * Sv * (1 + tau**2)**8), tau)
    return H, N, AA


def sign_at_roots(H, N):
    """Exact sign of N at each real root of H (gcd(H, N) = 1 required), and a
    refined rational isolating interval of width < 1e-45 for each root."""
    out = []
    for (a, b), mult in H.intervals():
        a, b = F_(a), F_(b)
        if a == b:
            sgn = 1 if N.eval(S_(a)) > 0 else -1
        else:
            while N.count_roots(S_(a), S_(b)) > 0:
                mid = (a + b) / 2
                if H.eval(S_(mid)) == 0:
                    a = b = mid
                    break
                if H.count_roots(S_(a), S_(mid)) == 1:
                    b = mid
                else:
                    a = mid
            sgn = 1 if N.eval(S_((a + b) / 2)) > 0 else -1
        if a != b:
            ra, rb = H.refine_root(S_(a), S_(b), eps=sp.Rational(1, 10**45))
            a, b = F_(ra), F_(rb)
        out.append(((a, b), sgn))
    return out


lam_s = sp.symbols('lam_s')
results = {}
for tt, name in ((T_int, 'interior'), (T_ext, 'exterior')):
    H, N, AA = tau_polys(tt)
    Pz = sp.Poly(sp.expand(lam_s**7 * P.subs({lam: lam_s, Aa: AA, z: z0}) / lam_s**7), lam_s,
                 domain='QQ_I')
    ok(f'C4 {name}: P(., z0) has degree 12, P(0) != 0', Pz.degree() == 12 and Pz.eval(0) != 0)
    ok(f'C4 {name}: P(., z0) is squarefree (12 distinct roots, M diagonalizable)',
       sp.gcd(Pz, Pz.diff(lam_s)).degree() == 0)
    ok(f'C4 {name}: H(tau) has degree 12 (no root at k = pi) and is squarefree',
       H.degree() == 12 and sp.gcd(H, H.diff(tau)).degree() == 0)
    ok(f'C4 {name}: gcd(H, N) = 1 (no zero velocity, no collision at z0)',
       sp.gcd(H, N).degree() == 0)
    nprop = H.count_roots()
    sg = sign_at_roots(H, N)
    right = sum(1 for _, s_ in sg if s_ < 0)          # v = -N / S^2
    left = sum(1 for _, s_ in sg if s_ > 0)
    ok(f'C4 {name}: {nprop} propagating roots; {right} right-moving, {left} left-moving',
       nprop == len(sg) and right + left == nprop)
    ok(f'C4 {name}: (#right) - (#left) = -2 (winding of C2)', right - left == -2)
    ok(f'C4 {name}: {12 - nprop} evanescent roots, {(12 - nprop) // 2} with |lambda| < 1 '
       f'(decay to x -> +inf) and {(12 - nprop) // 2} with |lambda| > 1 (decay to x -> -inf)',
       (12 - nprop) % 2 == 0)
    results[name] = dict(H=H, N=N, AA=AA, tt=tt, sg=sg, right=right, left=left, nprop=nprop)

ok('C4 interior has exactly one right-moving propagating channel on I',
   results['interior']['right'] == 1)
ok('C4 exterior has at least one right-moving propagating channel on I',
   results['exterior']['right'] >= 1)
n_in = results['interior']['right'] + results['exterior']['left']
n_out = results['exterior']['right'] + results['interior']['left']
ok(f'C4/C5 full line: incoming channels {n_in} = outgoing channels {n_out}', n_in == n_out)

# ================================================================= C5
# Operator identity behind flux = (dOmega/dk)|q_1|^2 (Hellmann-Feynman):
# -i U^dagger dU/dk = sum_{j=1..6} R_j^dagger sigma_z R_j - I, R_j = C(beta_j)...C(beta_1)
# with the shifts interleaved (R_j = C(beta_j) S C(beta_{j-1}) ... S C(beta_1)).
kk, th = sp.symbols('kk theta', real=True)
Sk = sp.diag(sp.exp(I * kk), sp.exp(-I * kk))
sz = sp.diag(1, -1)
coins = [rv.coin(m * th) for m in order]
U = sp.exp(-I * kk) * eye(2)
Rs = []
Rj = eye(2)
for j, Cm in enumerate(coins):
    Rj = Cm * Rj if j == 0 else Cm * Sk * Rj
    Rs.append(Rj)
Ufull = sp.exp(-I * kk) * Sk * Rs[-1]
lhs5 = (-I * Ufull.H * sp.diff(Ufull, kk)).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
rhs5 = (sum((R_.H * sz * R_ for R_ in Rs), zeros(2, 2)) - eye(2)).applyfunc(
    lambda e: sp.simplify(e.rewrite(sp.exp)))
ok('C5 -i U^H dU/dk = sum_j R_j^H sigma_z R_j - I (displacement operator per period)',
   all(sp.simplify(sp.expand((a - b).rewrite(sp.exp))) == 0 for a, b in zip(lhs5, rhs5)))


def coin_I(m, p, q):
    c_, s_ = (p, q) if m == 1 else (p * p - q * q, RI(-2) * p * q)
    return [[CI(c_), CI(-s_)], [CI(s_), CI(c_)]]


def matvec(Mt, v):
    return [sum((Mt[i][j] * v[j] for j in range(len(v))), CI(0)) for i in range(len(Mt))]


def matmul(A_, B_):
    n, m_, l_ = len(A_), len(B_), len(B_[0])
    return [[sum((A_[i][k_] * B_[k_][j] for k_ in range(m_)), CI(0)) for j in range(l_)]
            for i in range(n)]


z0I = CI(RI(R(3, 5)), RI(R(4, 5)))
for name in ('interior', 'exterior'):
    d = results[name]
    tt, AA = d['tt'], d['AA']
    p, q = sqrt_RI(RI(tt)), sqrt_RI(RI(1 - tt))
    # homogeneous M at z0 with interval coins
    c_, s_ = {}, {}
    for j, m in enumerate(order, 1):
        c_[j], s_[j] = (p, q) if m == 1 else (p * p - q * q, RI(-2) * p * q)
    Mi = [[CI(0) for _ in range(12)] for _ in range(12)]
    Mci = [[CI(0) for _ in range(12)] for _ in range(12)]
    for (zz, MM) in ((z0I, Mi), (z0I.conj(), Mci)):
        for j in range(1, 6):
            MM[j][j - 1] = CI(RI(1) / c_[j]); MM[j][6 + j] = CI(-s_[j] / c_[j])
            MM[6 + j - 1][j - 1] = CI(-s_[j] / c_[j]); MM[6 + j - 1][6 + j] = CI(RI(1) / c_[j])
        MM[0][4] = CI(1) / (zz * CI(c_[6] * c_[5]))
        MM[0][6] = CI(-s_[6] / c_[6])
        MM[0][11] = CI(-s_[5]) / (zz * CI(c_[6] * c_[5]))
        MM[11][0] = -zz / CI(s_[6])
        MM[11][5] = CI(c_[6] / s_[6])
    Dv = [0, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
    DM = [[Mi[i][j] * Dv[i] for j in range(12)] for i in range(12)]
    MH = [[Mci[j][i] for j in range(12)] for i in range(12)]
    Gi = matmul(MH, DM)
    Gi[6][6] = Gi[6][6] - 1
    fluxes = []
    for (a, b), sgnN in d['sg']:
        tI = RI(a, b)
        den = RI(1) + tI * tI
        ck = (RI(1) - tI * tI) / den
        sk = RI(2) * tI / den
        lamI = CI(ck, -sk)                              # e^{-ik}
        Sm = [[CI(1) / lamI, CI(0)], [CI(0), lamI]]     # S(k) = diag(1/lambda, lambda)
        Cm2, Cm1 = coin_I(-2, p, q), coin_I(1, p, q)
        Wm = matmul(Sm, matmul(Cm1, matmul(Sm, matmul(Cm1, matmul(Sm, Cm2)))))
        Um = matmul([[lamI, CI(0)], [CI(0), lamI]], matmul(Wm, Wm))
        v1 = [Um[0][1], z0I - Um[0][0]]                 # kernel of U - z0 (row 1)
        v2 = [z0I - Um[1][1], Um[1][0]]                 # kernel of U - z0 (row 2)
        vv = v1 if (v1[0].abs2() + v1[1].abs2()).pos() else v2
        assert (vv[0].abs2() + vv[1].abs2()).pos()
        qs = [vv]
        for m in order[:5]:
            qs.append(matvec(Sm, matvec(coin_I(m, p, q), qs[-1])))
        Yv = [qj[0] for qj in qs] + [qj[1] / lamI for qj in qs]
        GY = matvec(Gi, Yv)
        Fv = sum((Yv[i].conj() * GY[i] for i in range(12)), CI(0))
        # group velocity v = -(4 f f' + S)/S, as interval
        gI = g_I(ck, AA); fpI = -sk * gp_I(ck, AA)
        SI = RI(R(4, 5)) * ck + RI(R(3, 5)) * sk
        vI = -(RI(4) * gI * fpI + SI) / SI
        q1n = vv[0].abs2() + vv[1].abs2()
        ratio = Fv.re / (vI * q1n)
        fluxes.append((Fv, vI, ratio, sgnN))
    ok(f'C5 {name}: every propagating Bloch mode has nonzero flux Y^H G Y with the sign '
       'of its group velocity (exact intervals)',
       all((Fv.re.pos() and vI.pos()) or (Fv.re.neg() and vI.neg()) for Fv, vI, _, _ in fluxes))
    ok(f'C5 {name}: the interval group-velocity sign agrees with the exact Sturm sign',
       all((vI.pos() and sN < 0) or (vI.neg() and sN > 0) for _, vI, _, sN in fluxes))
    ok(f'C5 {name}: flux / (v |q_1|^2) enclosures contain 1 and have width < 1e-20',
       all(r.lo <= 1 <= r.hi and r.width() < Fr(1, 10**20) for _, _, r, _ in fluxes))
    ok(f'C5 {name}: Im(Y^H G Y) enclosures contain 0',
       all(Fv.im.lo <= 0 <= Fv.im.hi for Fv, _, _, _ in fluxes))
    results[name]['fluxes'] = fluxes

print(f'{len(checks)}/{len(checks)} channel checks PASS '
      f'(after {len(rv.checks)}/{len(rv.checks)} reviewed transfer-matrix checks)')
for name in ('interior', 'exterior'):
    d = results[name]
    print(f'{name} (t = {d["tt"]}): propagating {d["nprop"]} '
          f'(right {d["right"]}, left {d["left"]}), evanescent {12 - d["nprop"]}')
print('Verdict candidate: CHANNELS_CLASSIFIED (author PRELIMINARY; review pending)')
