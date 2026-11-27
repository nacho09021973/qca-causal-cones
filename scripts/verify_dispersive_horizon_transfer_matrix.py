"""Exact audit verifier for the 12x12 spatial transfer matrix of
reports/2026-11-26--dispersive-horizon-three-step-transfer.md (commit 8e5b540).

Operator under audit:  U = L_- W^2,  W = S C(theta) S C(theta) S C(-2 theta),
C(b) = exp(-i b sigma_y), S|x,up> = |x+1,up>, S|x,dn> = |x-1,dn>,
L_-|x,s> = |x-1,s>; each coin acts with the coin angle of the site where the
excitation sits at that stage.

Exact SymPy only (no floating point, no fitted tolerances). Fails closed: any
failed check raises and the process exits nonzero. Groups:

  T1  conventions: C(b) = exp(-i b sigma_y); coin order read off W's word
  T2  independent elimination of the raw stage + closure equations (general
      independent angles, reduced modulo c^2+s^2=1) vs the report's blocks
      P, Q, R, H, entry by entry (144 entries); uniqueness of the solution;
      consistency of the auxiliary unknown b_6(x+1) with row 12 of M_{x+1};
      two negative controls (sign flip; closure coefficients at x not x+1)
  T3  second route: iterate the report's M with site-dependent rational coins,
      rebuild psi, apply U from its definition, check U psi = z psi exactly
  T4  det M_x = cot beta_6(x) / cot beta_6(x+1), general angles, z-free
  T5  homogeneous symbol: tr W / 2 = A cos 3k + (1-A) cos k, det W = 1,
      charpoly(M_hom) * (-z A^2) = boxed lambda-polynomial (degree 12), for
      symbolic theta and at three rational points
  T6  Floquet degeneracy (z, lambda) = (i, -i) at t = 5/16, 3/8, 7/16:
      W(pi/2)^2 = -I, two explicit independent eigenvectors of M,
      algebraic multiplicity exactly 2 (so semisimple)
  T7  microscopic support [-7, 5] with nonzero extreme coefficients
      (site-dependent rational coins)
  T8  denominators, IR/UV velocities, and 0 <= f < 1 on (0, pi/2]

What it does NOT certify: see scripts/README.md.
"""
import random
import sys
import time

import sympy as sp
from sympy import I, Matrix, Rational as R, cos, sin, eye, zeros

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


def zero(label, value):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    def z0(x):
        x = sp.expand(x)
        return sp.simplify(x) == 0 or sp.simplify(sp.expand(x.rewrite(sp.exp))) == 0
    ok(label, all(z0(x) for x in entries))


XMP = sp.symbols('X_minpoly')


def nonzero_alg(x):
    """Exact nonzero test for an algebraic number: minimal polynomial is not X."""
    return sp.minimal_polynomial(sp.expand(x), XMP) != XMP


def E(i, j):
    m = zeros(6, 6)
    m[i - 1, j - 1] = 1
    return m


def M_report(c, s, cp, sp_, z):
    """Blocks P, Q, R, H transcribed verbatim from report Sec. 6.
    c[j], s[j] (j = 1..6) at site x; cp, sp_ = c_6, s_6 at site x+1."""
    P = sum((E(j + 1, j) / c[j] for j in range(1, 6)), zeros(6, 6)) \
        + E(1, 5) / (z * cp * c[5])
    Q = -sum((s[j] / c[j] * E(j + 1, j + 1) for j in range(1, 6)), zeros(6, 6)) \
        - sp_ / cp * E(1, 1) - s[5] / (z * cp * c[5]) * E(1, 6)
    Rb = -sum((s[j] / c[j] * E(j, j) for j in range(1, 6)), zeros(6, 6)) \
        - z / s[6] * E(6, 1) + c[6] / s[6] * E(6, 6)
    H = sum((E(j, j + 1) / c[j] for j in range(1, 6)), zeros(6, 6))
    return Matrix(sp.BlockMatrix([[P, Q], [Rb, H]]))


SY = Matrix([[0, -I], [I, 0]])


def coin(b):
    return Matrix([[cos(b), -sin(b)], [sin(b), cos(b)]])


# ---------------------------------------------------------------- T1
b = sp.symbols('b', real=True)
zero('T1 C(b) = exp(-i b sigma_y)', (-I * b * SY).exp().applyfunc(lambda e: e.rewrite(cos)) - coin(b))
# W's word, written left to right exactly as in the report; applied right to left.
W_WORD = ['S', ('C', 1), 'S', ('C', 1), 'S', ('C', -2)]   # ('C', m): angle m*theta
order = [f[1] for f in reversed(W_WORD) if f != 'S'] * 2
ok('T1 coin order of W^2 is (-2,1,1,-2,1,1) theta', order == [-2, 1, 1, -2, 1, 1])
ok('T1 W^2 has six conditional shifts', [f for f in reversed(W_WORD)].count('S') * 2 == 6)

# ---------------------------------------------------------------- T2
# General independent angles: free symbols c_j, s_j (j = 1..6, site x) and
# cP, sP (beta_6 at site x+1). Identities are decided exactly by clearing
# denominators and reducing the numerator modulo c^2 + s^2 - 1 (division in s).
cs_ = sp.symbols('c1:7')
ss_ = sp.symbols('s1:7')
cP, sP, z = sp.symbols('cP sP z')
c = {j: cs_[j - 1] for j in range(1, 7)}
s = {j: ss_[j - 1] for j in range(1, 7)}
CIRCLE = list(zip(ss_, cs_)) + [(sP, cP)]


def is_zero_on_circle(expr):
    num, _ = sp.fraction(sp.cancel(sp.together(expr)))
    num = sp.expand(num)
    for sv, cv in CIRCLE:
        num = sp.rem(num, sv**2 + cv**2 - 1, sv)
    return sp.expand(num) == 0


a0 = sp.symbols('a0_1:7')      # a_j(x)
bm = sp.symbols('bm_1:7')      # b_j(x-1)
a1 = sp.symbols('a1_1:7')      # a_j(x+1)   (unknown)
b0 = sp.symbols('b0_1:7')      # b_j(x)     (unknown)
b6n = sp.symbols('b6_next')    # b_6(x+1)   (auxiliary unknown)
# Raw stage relations: (S C q)(y) = ((C q)_up(y-1), (C q)_dn(y+1)).
#   a_{j+1}(x+1) = c_j(x) a_j(x) - s_j(x) b_j(x)
#   b_{j+1}(x-1) = s_j(x) a_j(x) + c_j(x) b_j(x)
eqs = []
for j in range(1, 6):
    eqs.append(a1[j] - (c[j] * a0[j - 1] - s[j] * b0[j - 1]))
    eqs.append(bm[j] - (s[j] * a0[j - 1] + c[j] * b0[j - 1]))
# Closure q_7(y+1) = z q_1(y): stage 6 at site x (up), and at site x+1 (up, dn).
eqs.append(z * a0[0] - (c[6] * a0[5] - s[6] * b0[5]))           # a_7(x+1) = z a_1(x)
eqs.append(z * a1[0] - (cP * a1[5] - sP * b6n))                 # a_7(x+2) = z a_1(x+1)
eqs.append(z * bm[0] - (sP * a1[5] + cP * b6n))                 # b_7(x)   = z b_1(x-1)
unknowns = list(a1) + list(b0) + [b6n]
ok('T2 13 equations in 13 unknowns', len(eqs) == 13 and len(unknowns) == 13)
Asys, bsys = sp.linear_eq_to_matrix(eqs, unknowns)
detA = sp.factor(Asys.det(method='berkowitz'))
# Unique solution iff c_1..c_5(x), c_6(x+1), s_6(x), z are all nonzero.
ok('T2 stage system det = -c1 c2 c3 c4 c5 c6(x+1) s6(x) z (unique solution)',
   sp.expand(detA + c[1] * c[2] * c[3] * c[4] * c[5] * cP * s[6] * z) == 0)
solv = Asys.LUsolve(bsys)
sol = {v: sp.cancel(solv[n]) for n, v in enumerate(unknowns)}
Yx = Matrix(list(a0) + list(bm))
Ynext = Matrix([sol[v] for v in list(a1) + list(b0)])
M_ind = Ynext.jacobian(Yx)
zero('T2 solution is linear homogeneous in Y_x', Ynext - M_ind * Yx)
M_rep = M_report(c, s, cP, sP, z)
names = 'PQRH'
for bi, (r0, c0) in enumerate([(0, 0), (0, 6), (6, 0), (6, 6)]):
    blk = M_ind[r0:r0 + 6, c0:c0 + 6] - M_rep[r0:r0 + 6, c0:c0 + 6]
    ok(f'T2 block {names[bi]}: 36 entries agree with independent elimination',
       all(is_zero_on_circle(x) for x in blk))
# Negative controls: the same test must reject (a) one flipped sign in Q and
# (b) the closure coefficients evaluated at x instead of x+1.
M_bad = M_rep.copy()
M_bad[0, 6] = -M_bad[0, 6]
ok('T2 negative control: sign flip in Q[1,1] is detected',
   not all(is_zero_on_circle(x) for x in (M_ind - M_bad)))
M_bad = M_report(c, s, c[6], s[6], z)
ok('T2 negative control: c_6(x), s_6(x) in place of c_6(x+1), s_6(x+1) is detected',
   not all(is_zero_on_circle(x) for x in (M_ind - M_bad)))
nnz = sum(1 for x in M_rep if sp.cancel(x) != 0)
ok('T2 report M has 25 structurally nonzero entries (P 6, Q 7, R 7, H 5)', nnz == 25)
# Forward direction: the auxiliary b_6(x+1) equals row 12 of M_{x+1}, so the
# recurrence on consecutive sites reproduces every stage + closure equation.
ok('T2 b_6(x+1) from stage system equals row 12 of M_{x+1}',
   is_zero_on_circle(sol[b6n] - (cP * sol[a1[5]] - z * sol[a1[0]]) / sP))

# ---------------------------------------------------------------- T3
random.seed(20261126)
TRIPLES = [(R(3, 5), R(4, 5)), (R(5, 13), R(12, 13)), (R(8, 17), R(15, 17)),
           (R(7, 25), R(24, 25)), (R(20, 29), R(21, 29)), (R(4, 5), R(3, 5)),
           (R(12, 13), R(5, 13)), (R(48, 73), R(55, 73))]
NS = 34
site = {x: TRIPLES[random.randrange(len(TRIPLES))] for x in range(-12, NS + 12)}


def coin_cs(m, x):
    """cos, sin of m*theta_x for m in {1, -2} with rational cos/sin theta."""
    p, q = site[x]
    if m == 1:
        return p, q
    if m == -2:
        return p * p - q * q, -2 * p * q
    raise ValueError(m)


def apply_word(word, psi):
    """Apply a word of 'S', ('C', m), 'L' (right to left) to psi: {x: (up, dn)}.
    Sites whose value is not determined by the window are dropped."""
    for f in reversed(word):
        new = {}
        if f == 'S':
            for x in psi:
                if x - 1 in psi and x + 1 in psi:
                    new[x] = (psi[x - 1][0], psi[x + 1][1])
        elif f == 'L':
            for x in psi:
                if x + 1 in psi:
                    new[x] = psi[x + 1]
        else:
            for x, (up_, dn_) in psi.items():
                cc, ss = coin_cs(f[1], x)
                new[x] = (cc * up_ - ss * dn_, ss * up_ + cc * dn_)
        psi = new
    return psi


U_WORD = ['L'] + W_WORD + W_WORD
zr = R(3, 5) + R(4, 5) * I


def site_cs(x):
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = coin_cs(m, x)
    return cc, ss


Y = {0: Matrix([random.randint(-5, 5) + random.randint(-5, 5) * I for _ in range(12)])}
for x in range(NS):
    cc, ss = site_cs(x)
    cn, sn = site_cs(x + 1)
    Y[x + 1] = (M_report(cc, ss, cn[6], sn[6], zr) * Y[x]).applyfunc(sp.expand)
psi = {x: (Y[x][0], Y[x + 1][6]) for x in range(NS)}
Upsi = apply_word(U_WORD, psi)
interior = [x for x in Upsi if x in psi]
ok('T3 at least 20 interior sites', len(interior) >= 20)
ok('T3 U psi = z psi exactly at every interior site (site-dependent coins)',
   all(sp.expand(Upsi[x][k] - zr * psi[x][k]) == 0 for x in interior for k in (0, 1)))
# Same psi also reproduces the intermediate stage vectors stored in Y:
q = dict(psi)
stage_ok = True
ncmp = 0
for j in range(1, 6):
    q = apply_word(['S', ('C', order[j - 1])], q)
    for x in q:
        if 0 <= x < NS and x - 1 >= 0:
            stage_ok &= sp.expand(q[x][0] - Y[x][j]) == 0          # a_{j+1}(x)
            stage_ok &= sp.expand(q[x][1] - Y[x + 1][6 + j]) == 0  # b_{j+1}(x)
            ncmp += 2
ok(f'T3 rebuilt stage vectors q_2..q_6 equal the components of Y ({ncmp} comparisons)',
   stage_ok and ncmp >= 100)

# ---------------------------------------------------------------- T4
d = sp.factor(M_rep.det(method='berkowitz'))
ok('T4 det M_x = cot beta_6(x) / cot beta_6(x+1), general angles',
   is_zero_on_circle(d - (c[6] / s[6]) / (cP / sP)))
zero('T4 det M_x independent of z', sp.diff(d, z))
th0, th1 = sp.symbols('theta0 theta1', positive=True)
zero('T4 with beta_6 = theta: cot(theta_x)/cot(theta_{x+1})',
     (cos(th0) / sin(th0)) / (cos(th1) / sin(th1)) - sp.cot(th0) / sp.cot(th1))

# ---------------------------------------------------------------- T5
k, th = sp.symbols('k theta', real=True)
Sk = sp.diag(sp.exp(I * k), sp.exp(-I * k))     # symbol on e^{-ikx}
W = Sk * coin(th) * Sk * coin(th) * Sk * coin(-2 * th)
t = cos(th)**2
A = t * (2 * t - 1)
f = A * cos(3 * k) + (1 - A) * cos(k)
zero('T5 tr W / 2 = A cos 3k + (1-A) cos k',
     (sp.expand_complex(W.trace() / 2) - f).rewrite(sp.exp))
zero('T5 det W = 1', W.det() - 1)
lam = sp.symbols('lambda')


def hom_cs(p, qq):
    cc, ss = {}, {}
    for j, m in enumerate(order, 1):
        cc[j], ss[j] = (p, qq) if m == 1 else (p * p - qq * qq, -2 * p * qq)
    return cc, ss


def boxed(AA):
    fl = AA / 2 * (lam**3 + lam**-3) + (1 - AA) / 2 * (lam + 1 / lam)
    return sp.expand(z**2 * lam**5 - z * lam**6 * (4 * fl**2 - 2) + lam**7)


for p, qq in [(R(3, 5), R(4, 5)), (R(48, 73), R(55, 73)), (R(8, 17), R(15, 17))]:
    tt = p * p
    AA = tt * (2 * tt - 1)
    cc, ss = hom_cs(p, qq)
    Mh = M_report(cc, ss, cc[6], ss[6], z)
    cpoly = sp.expand((lam * eye(12) - Mh).det(method='berkowitz'))
    Pb = boxed(AA)
    zero(f'T5 t={tt}: charpoly(M_hom) * (-z A^2) = boxed polynomial',
         sp.expand(cpoly * (-z * AA**2)) - Pb)
    ok(f'T5 t={tt}: boxed polynomial has degree 12, nonzero constant term',
       sp.degree(Pb, lam) == 12 and sp.expand(Pb.subs(lam, 0)) != 0)

# General theta: cos theta = pc, sin theta = qc symbolic, reduced modulo pc^2+qc^2-1.
pc, qc = sp.symbols('pc qc')
cc, ss = hom_cs(pc, qc)
Mh = M_report(cc, ss, cc[6], ss[6], z)
cpoly = sp.together((lam * eye(12) - Mh).det(method='berkowitz'))
AAg = pc**2 * (2 * pc**2 - 1)
num, _ = sp.fraction(sp.cancel(sp.together(cpoly * (-z * AAg**2) - boxed(AAg))))
num = sp.rem(sp.expand(num), qc**2 + pc**2 - 1, qc)
ok('T5 general theta: charpoly(M_hom) * (-z A^2) = boxed polynomial', sp.expand(num) == 0)

# ---------------------------------------------------------------- T6
Wpi2 = W.subs(k, sp.pi / 2)
zero('T6 W(pi/2)^2 = -I for all theta', Wpi2 * Wpi2 + eye(2))
PROFILE = [R(5, 16), R(3, 8), R(7, 16)]
for tt in PROFILE:
    p, qq = sp.sqrt(tt), sp.sqrt(1 - tt)
    cc, ss = hom_cs(p, qq)
    Mh = M_report(cc, ss, cc[6], ss[6], I)
    L0 = -I
    vecs = []
    for v in (Matrix([1, 0]), Matrix([0, 1])):
        qs = [v]
        S_pi2 = sp.diag(I, -I)                      # S(k) at k = pi/2
        for m in order[:5]:
            cm, sm = (p, qq) if m == 1 else (p * p - qq * qq, -2 * p * qq)
            qs.append(S_pi2 * Matrix([[cm, -sm], [sm, cm]]) * qs[-1])
        Yv = Matrix([qj[0] for qj in qs] + [qj[1] / L0 for qj in qs])
        vecs.append(Yv.applyfunc(sp.radsimp))
        zero(f'T6 t={tt}: Bloch vector e{len(vecs)} is an eigenvector of M (z=i, lambda=-i)',
             (Mh * Yv - L0 * Yv).applyfunc(sp.radsimp))
    rank2 = Matrix.hstack(*vecs)
    ok(f'T6 t={tt}: the two eigenvectors are independent',
       any(nonzero_alg(rank2[i, 0] * rank2[j, 1] - rank2[j, 0] * rank2[i, 1])
           for i in range(12) for j in range(i + 1, 12)))
    cpoly = sp.Poly(sp.expand((lam * eye(12) - Mh).det(method='berkowitz')), lam)
    cpoly = sp.Poly([sp.radsimp(co) for co in cpoly.all_coeffs()], lam)
    r2 = cpoly.rem(sp.Poly((lam + I)**2, lam))
    r3 = cpoly.rem(sp.Poly((lam + I)**3, lam))
    ok(f'T6 t={tt}: (lambda+i)^2 divides charpoly',
       all(sp.radsimp(co) == 0 for co in r2.all_coeffs()))
    ok(f'T6 t={tt}: (lambda+i)^3 does not divide charpoly (multiplicity exactly 2)',
       any(nonzero_alg(co) for co in r3.all_coeffs()))

# ---------------------------------------------------------------- T7
x0 = 10
window = range(x0 - 20, x0 + 21)   # wide enough that trimming never reaches [x0-7, x0+5]
for comp, name in ((0, 'up'), (1, 'dn')):
    delta = {x: ((1, 0) if comp == 0 else (0, 1)) if x == x0 else (0, 0) for x in window}
    out = apply_word(U_WORD, delta)
    supp = [x for x, (p_, q_) in out.items() if p_ != 0 or q_ != 0]
    ok(f'T7 U delta_{name}: computed window covers [x0-9, x0+7]',
       all(x in out for x in range(x0 - 9, x0 + 8)))
    ok(f'T7 U delta_{name}: support inside [x0-7, x0+5]',
       min(supp) >= x0 - 7 and max(supp) <= x0 + 5)
    if comp == 0:
        ok('T7 U delta_up: nonzero up amplitude at x0+5', out[x0 + 5][0] != 0)
    else:
        ok('T7 U delta_dn: nonzero dn amplitude at x0-7', out[x0 - 7][1] != 0)

# ---------------------------------------------------------------- T8
tl, th_ = R(5, 16), R(7, 16)
ok('T8 profile: 2t-1 in [-3/8,-1/8] (cos 2theta != 0), 0<t<1 (sin, cos theta != 0)',
   2 * tl - 1 == R(-3, 8) and 2 * th_ - 1 == R(-1, 8) and 0 < tl and th_ < 1)
ts = sp.symbols('t', positive=True)
As = ts * (2 * ts - 1)
zero('T8 1 + 8A = (4t-1)^2', 1 + 8 * As - (4 * ts - 1)**2)
# IR: f = 1 - (1+8A) k^2/2 + O(k^4); slope of E is |4t-1| = 4t-1 for t > 1/4.
fk = As * cos(3 * k) + (1 - As) * cos(k)
zero('T8 f(k) = 1 - (1+8A) k^2/2 + O(k^4)',
     sp.series(fk, k, 0, 4).removeO() - (1 - (1 + 8 * As) * k**2 / 2))
vIR = {tt: -1 + 2 * (4 * tt - 1) for tt in PROFILE}
ok('T8 v_IR,out = 8t-3 = -1/2, 0, 1/2',
   [vIR[tt] for tt in PROFILE] == [R(-1, 2), 0, R(1, 2)])
# UV at k = pi/2: f = 0, E = pi/2, E' = -f'/sin E = 1 - 4A, v = -1 + 2E' = 1 - 8A.
zero('T8 f(pi/2) = 0', fk.subs(k, sp.pi / 2))
zero("T8 E'(pi/2) = 1 - 4A", -sp.diff(fk, k).subs(k, sp.pi / 2) - (1 - 4 * As))
vUV = [1 - 8 * As.subs(ts, tt) for tt in PROFILE]
ok('T8 v_UV,out(pi/2) = 31/16, 7/4, 23/16', vUV == [R(31, 16), R(7, 4), R(23, 16)])
# 0 <= f < 1 on (0, pi/2]: with C = cos k in [0,1), f = g(C) = 4A C^3 + (1-4A) C,
# g(0)=0, g(1)=1, g'(C) = 12A C^2 + 1 - 4A, decreasing in C^2 because A < 0,
# so g' >= g'(1) = 1 + 8A = (4t-1)^2 > 0 on [0,1].
Cs = sp.symbols('C')
zero('T8 f = 4A cos^3 k + (1-4A) cos k',
     sp.expand_trig(fk) - (4 * As * cos(k)**3 + (1 - 4 * As) * cos(k)))
Aint = [As.subs(ts, tt) for tt in (tl, th_)]
ok('T8 A < 0 on the profile (A = t(2t-1), both endpoints negative, t<1/2)',
   all(a_ < 0 for a_ in Aint))
# g'(1) = 1 + 8A = (4t-1)^2 (checked above) and 4t - 1 >= 4*5/16 - 1 = 1/4 > 0.
ok("T8 g'(1) = (4t-1)^2 > 0 on the whole profile (4t-1 >= 1/4)", 4 * tl - 1 == R(1, 4))
# A = t(2t-1) < 0 for every t in (0, 1/2), hence on the whole profile.

print(f'{len(checks)}/{len(checks)} exact checks PASS')
print('Verdict: TRANSFER_MATRIX_PASS (algebraic scope; author-side audit, '
      'cross-family independence not established)')

