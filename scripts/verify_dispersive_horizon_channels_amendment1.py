"""Exact checks for Amendment 1 of reports/2026-11-26--dispersive-horizon-channels.md,
after the Astra (gpt-6.2-astra) review
(reports/2026-11-26--dispersive-horizon-channels-astra-review.md).

Imports scripts/verify_dispersive_horizon_channels.py read-only (which imports
the reviewed transfer-matrix verifier read-only); the import runs their
61 + 53 checks first and aborts on any failure. No earlier verifier's bytes are
changed. Exact SymPy and exact rational interval arithmetic only; floating
point appears only in timings. Fails closed.

  H   provenance: SHA256 of both imported verifiers equals the reviewed values.
  V   published values: counts (4 propagating, 1 right, 3 left, 8 evanescent)
      in both media at z0; exterior threshold quotient proportional to
      343u^2 - 1211u + 1012; the primitive minimal polynomial of Re z_c* equals
      the printed one; z_c* lies in the box (9/10, 1) x (1/20, 1/8).
  Z   C3 deliverable: rational enclosures of the four interior critical values
      (printed), and the exact symmetry of the critical set under conjugation
      and negation.
  K   C2 deliverable: root count on the unit circle between thresholds, at one
      exact rational point in each of the eight arcs cut by the four interior
      critical values and the four collision points z = 1, i, -1, -i, in both
      media; regularity at every point; nonzero branch slopes at the
      collision points.
  E   C4 deliverable: every root lambda of P(., z0) in each medium, by
      isolating rational boxes: 4 on the circle (matched one-to-one with the
      Sturm roots, signs of v in increasing k), 4 with |lambda| < 1, 4 with
      |lambda| > 1, each inside root paired with exactly one outside box by
      lambda -> 1/conj(lambda).
  N   C5 deliverable: for each propagating root, the tau interval, the sign,
      the kernel row used, enclosures of F = Y^H G Y and of 1/sqrt|F|, and of
      the twelve components of the normalized vector N = Y/sqrt|F|, with
      N^H G N enclosing sign(v).
  G   det G_x = -cot^2 beta_6(x) for a varying profile, exactly, on rational
      site-dependent coins (spot check of Astra's written proof).

Written steps (not machine-checked) are listed in scripts/README.md.
"""
import hashlib
import importlib.util
import pathlib
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy import I, Rational as R

HERE = pathlib.Path(__file__).resolve().parent
SHA_MATRIX = '98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2'
SHA_CHANNELS = '08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc'


def sha(name):
    return hashlib.sha256((HERE / name).read_bytes()).hexdigest()


# Hashes are read before the import executes the files.
h_matrix = sha('verify_dispersive_horizon_transfer_matrix.py')
h_channels = sha('verify_dispersive_horizon_channels.py')

spec = importlib.util.spec_from_file_location(
    'channels', HERE / 'verify_dispersive_horizon_channels.py')
ch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ch)          # runs 61 reviewed + 53 channel checks
rv = ch.rv
RI, CI, sqrt_RI = ch.RI, ch.CI, ch.sqrt_RI

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


def dec(x, d, up):
    """Outward-rounded decimal string of the rational x at d digits."""
    x = Fr(x)
    n = x * 10**d
    m = -((-n.numerator) // n.denominator) if up else n.numerator // n.denominator
    sgn = '-' if m < 0 else ''
    m = abs(m)
    s = str(m).rjust(d + 1, '0')
    return f'{sgn}{s[:-d]}.{s[-d:]}'


def ri_str(x, d=15):
    return f'[{dec(x.lo, d, False)}, {dec(x.hi, d, True)}]'


def ci_str(x, d=15):
    return f'{ri_str(x.re, d)} + i {ri_str(x.im, d)}'


def overlap(a, b):
    return a.lo <= b.hi and b.lo <= a.hi


def coverlap(a, b):
    return overlap(a.re, b.re) and overlap(a.im, b.im)


# ================================================================= H
ok(f'H imported transfer-matrix verifier SHA256 = {SHA_MATRIX[:12]}... (reviewed, d0114b2)',
   h_matrix == SHA_MATRIX)
ok(f'H imported channels verifier SHA256 = {SHA_CHANNELS[:12]}... (reviewed a5b9be3)',
   h_channels == SHA_CHANNELS)

# ================================================================= V
for name in ('interior', 'exterior'):
    d = ch.results[name]
    ok(f'V {name} at z0: 4 propagating (1 right, 3 left), 8 evanescent (published values)',
       d['nprop'] == 4 and d['right'] == 1 and d['left'] == 3)
u = ch.u
ok('V exterior threshold quotient is proportional to 343u^2 - 1211u + 1012',
   sp.cancel(ch.Qext.as_expr() / (343 * u**2 - 1211 * u + 1012)).is_number)
X = ch.Xm
published = sp.Poly(316240512000000000 * X**4 - 664624285099139500 * X**2
                    + 348107462168643891, X)
mp = sp.Poly(ch.mp_re, X)
mp_prim = mp.primitive()[1]
if mp_prim.LC() < 0:
    mp_prim = -mp_prim
ok('V primitive minimal polynomial of Re z_c* equals the printed quartic',
   mp_prim == published)
zs = ch.zc_star
ok('V z_c* lies in the rational box (9/10, 1) x (1/20, 1/8)',
   zs.re.lo > Fr(9, 10) and zs.re.hi < 1 and zs.im.lo > Fr(1, 20) and zs.im.hi < Fr(1, 8))

# ================================================================= Z
print('Z certified rational enclosures of the four interior critical values '
      '(C sign, sin k sign):')
for sg, zc in ch.zcs:
    print(f'    {sg}: z_c in {ci_str(zc, 30)}')
Cs_, Ss_, gs_, gps_ = sp.symbols('Cs Ss gs gps', real=True)


def zc_formula(Cv, Sv, gv, gpv):        # g odd in C, g' even in C
    return sp.expand((Cv - I * Sv) * (2 * gv**2 - 1 + 4 * I * gv * Sv * gpv))


base = zc_formula(Cs_, Ss_, gs_, gps_)
ok('Z critical set is closed under z -> conj z (S -> -S) and z -> -z (C, S -> -C, -S)',
   sp.expand(zc_formula(Cs_, -Ss_, gs_, gps_) - sp.conjugate(base)) == 0
   and sp.expand(zc_formula(-Cs_, -Ss_, -gs_, gps_) + base) == 0)
ok('Z the four enclosures are pairwise disjoint and match {z*, conj z*, -z*, -conj z*}',
   all(not coverlap(a, b) for i_, (_, a) in enumerate(ch.zcs) for (_, b) in ch.zcs[i_ + 1:])
   and all(any(coverlap(zc, img) for _, zc in ch.zcs)
           for img in (zs, zs.conj(), -zs, -zs.conj())))

# ================================================================= K
Cc, tau = ch.Cc, ch.tau
cos_t, sin_t = ch.cos_t, ch.sin_t


def tau_polys_at(tt, cw, sw):
    AA = tt * (2 * tt - 1)
    g = 4 * AA * Cc**3 + (1 - 4 * AA) * Cc
    gp = 12 * AA * Cc**2 + 1 - 4 * AA
    f = g.subs(Cc, cos_t)
    fpr = -sin_t * gp.subs(Cc, cos_t)
    Sv = sw * cos_t + cw * sin_t                      # sin(omega + k)
    h = 2 * f**2 - 1 - (cw * cos_t - sw * sin_t)      # 2f^2 - 1 - cos(omega + k)
    H = sp.Poly(sp.cancel(h * (1 + tau**2)**6), tau)
    N = sp.Poly(sp.cancel((4 * f * fpr + Sv) * Sv * (1 + tau**2)**8), tau)
    return H, N


s1 = R(1, 50)
p1 = ((1 - s1**2) / (1 + s1**2), 2 * s1 / (1 + s1**2))      # arg p1 = 2 atan(1/50)
ok('K p1 = ((1-s^2) + 2si)/(1+s^2), s = 1/50, lies in the open arc (0, arg z_c*)',
   p1[0] > 0 and p1[1] > 0
   and (RI(p1[1]) * zs.re - zs.im * RI(p1[0])).neg())
c0, s0 = R(3, 5), R(4, 5)
# The eight arcs of S^1 cut by {1, z*, i, -conj z*, -1, -z*, -i, conj z*};
# conjugation and negation permute the arcs and fix both cut sets (Z).
arcs = [
    ('(0, d)', p1, True), ('(d, pi/2)', (c0, s0), False),
    ('(pi/2, pi-d)', (-c0, s0), False), ('(pi-d, pi)', (-p1[0], p1[1]), True),
    ('(pi, pi+d)', (-p1[0], -p1[1]), True), ('(pi+d, 3pi/2)', (-c0, -s0), False),
    ('(3pi/2, 2pi-d)', (c0, -s0), False), ('(2pi-d, 2pi)', (p1[0], -p1[1]), True),
]
print('K root count on the unit circle between thresholds (d = arg z_c*):')
table = {}
for tt, name in ((ch.T_int, 'interior'), (ch.T_ext, 'exterior')):
    for label, (cw, sw), near in arcs:
        assert cw**2 + sw**2 == 1
        H, N = tau_polys_at(tt, cw, sw)
        regular = (H.degree() == 12 and sp.gcd(H, H.diff(tau)).degree() == 0
                   and sp.gcd(H, N).degree() == 0)
        sg = ch.sign_at_roots(H, N) if regular else []
        right = sum(1 for _, s_ in sg if s_ < 0)
        left = sum(1 for _, s_ in sg if s_ > 0)
        table[(name, label)] = (len(sg), right, left)
        print(f'    {name:8s} arc {label:15s} z = ({cw}, {sw}): '
              f'propagating {len(sg)} (right {right}, left {left})')
        ok(f'K {name} arc {label}: regular point (deg H = 12, H squarefree, gcd(H, N) = 1), '
           f'right - left = -2', regular and right - left == -2)
for label, _, near in arcs:
    exp_int = (6, 2, 4) if near else (4, 1, 3)
    ok(f'K interior arc {label}: propagating/right/left = {exp_int}',
       table[('interior', label)] == exp_int)
    ok(f'K exterior arc {label}: propagating/right/left = (4, 1, 3)',
       table[('exterior', label)] == (4, 1, 3))
for tt, name in ((ch.T_int, 'interior'), (ch.T_ext, 'exterior')):
    AA = tt * (2 * tt - 1)
    slopes = [-1 + 2 * (4 * tt - 1), -1 - 2 * (4 * tt - 1),
              -1 + 2 * (1 - 4 * AA), -1 - 2 * (1 - 4 * AA)]
    ok(f'K {name}: branch slopes -1 +- 2(4t-1) (z = +-1) and -1 +- 2(1-4A) (z = +-i) '
       f'are nonzero: {slopes}', all(s_ != 0 for s_ in slopes))

# ================================================================= E
L = sp.symbols('L')


def horner_CI(coeffs, x):
    acc = CI(0)
    for c in coeffs:
        acc = acc * x + c
    return acc


def to_CI(c):
    c = sp.nsimplify(c)
    re_, im_ = sp.re(c), sp.im(c)
    return CI(RI(Fr(int(re_.p), int(re_.q))), RI(Fr(int(im_.p), int(im_.q))))


evan = {}
for tt, name in ((ch.T_int, 'interior'), (ch.T_ext, 'exterior')):
    AA = tt * (2 * tt - 1)
    Pz = sp.Poly(sp.expand(ch.P.subs({ch.lam: L, ch.Aa: AA, ch.z: ch.z0})), L, domain='QQ_I')
    Pzc = sp.Poly(sp.expand(ch.P.subs({ch.lam: L, ch.Aa: AA, ch.z: ch.z0c})), L, domain='QQ_I')
    ok(f'E {name}: gcd(P(., z0), P(., conj z0)) = 1', sp.gcd(Pz, Pzc).degree() == 0)
    Nq = sp.Poly(sp.expand(Pz.as_expr() * Pzc.as_expr()), L)
    ok(f'E {name}: N = P(., z0) P(., conj z0) has rational coefficients, degree 24, squarefree',
       Nq.domain == sp.QQ and Nq.degree() == 24 and sp.gcd(Nq, Nq.diff(L)).degree() == 0)
    reals, cplx = Nq.intervals(all=True, eps=R(1, 10**25))
    boxes = []
    for (a, b), m in reals:
        boxes.append(CI(RI(Fr(int(a.p), int(a.q)), Fr(int(b.p), int(b.q))), RI(0)))
    for (lo, hi), m in cplx:
        rlo, ilo, rhi, ihi = sp.re(lo), sp.im(lo), sp.re(hi), sp.im(hi)
        boxes.append(CI(RI(Fr(int(rlo.p), int(rlo.q)), Fr(int(rhi.p), int(rhi.q))),
                        RI(Fr(int(ilo.p), int(ilo.q)), Fr(int(ihi.p), int(ihi.q)))))
    ok(f'E {name}: 24 isolating rational boxes for the roots of N', len(boxes) == 24)
    cz = [to_CI(c) for c in Pz.all_coeffs()]
    czc = [to_CI(c) for c in Pzc.all_coeffs()]
    own, undecided_owner = [], 0
    for bx in boxes:
        vz, vzc = horner_CI(cz, bx), horner_CI(czc, bx)
        zero_z = vz.re.lo <= 0 <= vz.re.hi and vz.im.lo <= 0 <= vz.im.hi
        zero_zc = vzc.re.lo <= 0 <= vzc.re.hi and vzc.im.lo <= 0 <= vzc.im.hi
        if zero_z and not zero_zc:
            own.append(bx)
        elif zero_z == zero_zc:
            undecided_owner += 1
    ok(f'E {name}: each box is assigned to exactly one factor; 12 belong to P(., z0)',
       undecided_owner == 0 and len(own) == 12)
    inside = [bx for bx in own if bx.abs2().hi < 1]
    outside = [bx for bx in own if bx.abs2().lo > 1]
    circle = [bx for bx in own if bx.abs2().lo <= 1 <= bx.abs2().hi]
    sturm_boxes = []
    for (a, b), sN in ch.results[name]['sg']:
        tI = RI(a, b)
        den = RI(1) + tI * tI
        sturm_boxes.append((CI((RI(1) - tI * tI) / den, -(RI(2) * tI / den)), sN))
    match = [[i_ for i_, (sb, _) in enumerate(sturm_boxes) if coverlap(bx, sb)] for bx in circle]
    ok(f'E {name}: 4 roots with |lambda| < 1, 4 with |lambda| > 1, 4 on the circle matched '
       'one-to-one with the 4 Sturm roots',
       len(inside) == 4 and len(outside) == 4 and len(circle) == 4
       and sorted(m_[0] for m_ in match if len(m_) == 1) == [0, 1, 2, 3])
    mirror_ok = True
    for bx in inside:
        img = bx / bx.abs2()                       # 1/conj(lambda) = lambda/|lambda|^2
        hits = [ob for ob in outside if coverlap(img, ob)]
        mirror_ok = mirror_ok and len(hits) == 1
    ok(f'E {name}: each |lambda| < 1 box maps under 1/conj into exactly one |lambda| > 1 box',
       mirror_ok)
    vsigns = [-sN for _, sN in ch.results[name]['sg']]          # sign v = -sign N
    ok(f'E {name}: signs of v at the propagating roots in increasing k: {vsigns} = [-, -, +, -]',
       vsigns == [-1, -1, 1, -1])
    print(f'E {name}: roots of P(., z0) (lambda = e^(-ik); Y ~ lambda^x):')
    for bx in inside:
        print(f'    |lambda| < 1 (decays as x -> +inf): {ci_str(bx, 12)}')
    for bx in outside:
        print(f'    |lambda| > 1 (decays as x -> -inf): {ci_str(bx, 12)}')
    for bx in circle:
        print(f'    |lambda| = 1 (propagating):         {ci_str(bx, 12)}')
    evan[name] = (inside, outside, circle)

# ================================================================= N
order = ch.order
Dv = [0, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1]
coin_I, matvec, matmul = ch.coin_I, ch.matvec, ch.matmul
z0I = ch.z0I
for name in ('interior', 'exterior'):
    d = ch.results[name]
    tt, AA = d['tt'], d['AA']
    p, q = sqrt_RI(RI(tt)), sqrt_RI(RI(1 - tt))
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
    DM = [[Mi[i][j] * Dv[i] for j in range(12)] for i in range(12)]
    MH = [[Mci[j][i] for j in range(12)] for i in range(12)]
    Gi = matmul(MH, DM)
    Gi[6][6] = Gi[6][6] - 1
    print(f'N {name} (t = {tt}): unit-flux propagating modes at z0')
    same_F, normed = True, True
    for idx, ((a, b), sgnN) in enumerate(d['sg']):
        tI = RI(a, b)
        den = RI(1) + tI * tI
        ck = (RI(1) - tI * tI) / den
        sk = RI(2) * tI / den
        lamI = CI(ck, -sk)
        Sm = [[CI(1) / lamI, CI(0)], [CI(0), lamI]]
        Cm2, Cm1 = coin_I(-2, p, q), coin_I(1, p, q)
        Wm = matmul(Sm, matmul(Cm1, matmul(Sm, matmul(Cm1, matmul(Sm, Cm2)))))
        Um = matmul([[lamI, CI(0)], [CI(0), lamI]], matmul(Wm, Wm))
        v1 = [Um[0][1], z0I - Um[0][0]]
        v2 = [z0I - Um[1][1], Um[1][0]]
        row = 1 if (v1[0].abs2() + v1[1].abs2()).pos() else 2
        vv = v1 if row == 1 else v2
        qs = [vv]
        for m in order[:5]:
            qs.append(matvec(Sm, matvec(coin_I(m, p, q), qs[-1])))
        Yv = [qj[0] for qj in qs] + [qj[1] / lamI for qj in qs]
        GY = matvec(Gi, Yv)
        Fv = sum((Yv[i].conj() * GY[i] for i in range(12)), CI(0))
        Fref = d['fluxes'][idx][0]
        same_F = same_F and (Fv.re.lo, Fv.re.hi, Fv.im.lo, Fv.im.hi) == (
            Fref.re.lo, Fref.re.hi, Fref.im.lo, Fref.im.hi)
        absF = Fv.re if Fv.re.pos() else -Fv.re
        nf = sqrt_RI(absF).inv()
        Nv = [y * CI(nf) for y in Yv]
        GN = matvec(Gi, Nv)
        NGN = sum((Nv[i].conj() * GN[i] for i in range(12)), CI(0))
        sv = -sgnN
        normed = normed and (NGN.re.lo <= sv <= NGN.re.hi and NGN.re.width() < Fr(1, 10**10)
                             and NGN.im.lo <= 0 <= NGN.im.hi)
        print(f'  mode {idx + 1}: tau in {ri_str(tI, 20)}, sign v = {"+" if sv > 0 else "-"}, '
              f'kernel row {row} of U(k) - z0')
        print(f'    F = Y^H G Y in {ri_str(Fv.re, 20)} (Im in {ri_str(Fv.im, 20)})')
        print(f'    1/sqrt|F| in {ri_str(nf, 20)}')
        for i in range(12):
            lab = f'a{i + 1}' if i < 6 else f'b{i - 5}/lambda'
            print(f'    N[{lab:9s}] in {ci_str(Nv[i], 12)}')
    ok(f'N {name}: the recomputed F enclosures equal those of the reviewed C5 run',
       same_F)
    ok(f'N {name}: every normalized vector has N^H G N enclosing sign(v) (width < 1e-10) '
       'and Im enclosing 0', normed)

# ================================================================= G
z0, z0c = ch.z0, ch.z0c
gdet = True
for x in range(0, 6):
    Gx = ch.G_of(ch.M_at(x, z0), ch.M_at(x, z0c))
    cb, sb = ch.cs_site(order[5], x)
    dG = sp.expand(Gx.det(method='bareiss'))
    gdet = gdet and sp.simplify(dG + (cb / sb)**2) == 0
ok('G varying rational profile: det G_x = -cot^2 beta_6(x) at x = 0..5 (exact)', gdet)

print(f'{len(checks)}/{len(checks)} amendment-1 checks PASS '
      f'(after {len(rv.checks)} reviewed and {len(ch.checks)} channel checks)')
assert len(rv.checks) == 61 and len(ch.checks) == 53
