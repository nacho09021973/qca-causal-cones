"""HEX_TRACE_ALIGNED_ALL_M: exact checks for the all-m analysis.

Contract: theory/HEX_TRACE_ALIGNED_ALL_M_GATE.md (preregistration 689fd30).
Report:   reports/2026-11-05--hex-trace-aligned-all-m.md
Run from the repo root:  python3 -B scripts/verify_hex_trace_aligned_all_m.py

What it checks (exact SymPy / integer arithmetic, no floating point in any
certified quantity, fail-closed):
  A. general-m interpolant f0 and residual factor Delta (symbolic m);
  B. the vertex-direction slice p=2q: f0 = T_m^2+T_m-1, Delta=(1-x)^3(1+x)/4;
  C. the slice image of D6-invariant residuals h (support H_{m-2}):
     C1 K-point constraint g'(-1/2)=0 (symmetry), C2 triangular top
     frequencies {0,2,3,...,2n} for symbolic orbit parameter a, C3 exact
     rank diagnostics for m=3..8 (consistency only, not a universal proof),
     C4 m=3 control (image span{1, 4x^2+4x-2});
  D. slice-route closure: for every m>=629 an explicit slice polynomial
     F=A*B, bounded by 1 by construction, meets every slice condition.
     D1 symbolic inequalities for all m>=629, D2 explicit instances
     m=629, 630, 1000 (Taylor to q^4, F(pi), F'(2pi/3), lambda, alpha, degree),
     D3 closed-form moments (algebraic, partly by construction; D2 is the
     independent Taylor test), negative control, m=3 consistency.

What it does NOT certify: the universal divisibility (R) of the general
reduction (analytic, report Sec. 2), boundedness of any candidate off the
slice, or any statement about the all-m question itself, which stays OPEN.
"""
from math import isqrt

import sympy as sp

p, q, x, m, a, y = sp.symbols('p q x m a y', real=True)
CHECKS = []


def check(label, cond):
    ok = bool(cond)
    CHECKS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zero(e):
    return sp.simplify(sp.expand(sp.expand_trig(e)).rewrite(sp.exp)) == 0


# ---------------- A. interpolant and residual factor -------------------
f0 = (sp.cos(m*p) + sp.cos(m*q) + sp.cos(m*(p - q)) - 1) / 2
check('A1 f0 = cos(mq) on p=0, cos(mp) on q=0 and on p=q (symbolic m)',
      zero(f0.subs(p, 0) - sp.cos(m*q)) and zero(f0.subs(q, 0) - sp.cos(m*p))
      and zero(f0.subs(q, p) - sp.cos(m*p)) and f0.subs({p: 0, q: 0}) == 1)

Delta = sp.sin(p/2)**2 * sp.sin(q/2)**2 * sp.sin((p - q)/2)**2
z, w = sp.symbols('z w')
DeltaL = -(z - 1)**2 * (w - 1)**2 * (z - w)**2 / (64 * z**2 * w**2)
num = sp.Poly(sp.expand((z - 1)**2 * (w - 1)**2 * (z - w)**2), z, w)
supp = {(i - 2, j - 2): c for (i, j), c in num.terms()}   # divide by z^2 w^2
hexn = lambda i, j: max(abs(i), abs(j), abs(i + j))
verts2 = {(2, 0), (0, 2), (-2, 2), (-2, 0), (0, -2), (2, -2)}
check('A2 Delta Laurent support inside H_2, six vertices present (Newton polygon H_2)',
      all(hexn(i, j) <= 2 for (i, j) in supp) and verts2 <= set(supp)
      and all(-supp[v] / 64 == sp.Rational(-1, 64) for v in verts2))
check('A3 Delta and its gradient vanish on p=0, q=0, p=q',
      all(zero(e) for e in [Delta.subs(p, 0), sp.diff(Delta, p).subs(p, 0),
                            Delta.subs(q, 0), sp.diff(Delta, q).subs(q, 0),
                            Delta.subs(q, p), (sp.diff(Delta, p) + sp.diff(Delta, q)).subs(q, p),
                            sp.diff(Delta, p).subs(q, p)]))
check('A4 Laurent form of Delta equals the trigonometric form',
      zero(DeltaL.subs({z: sp.exp(sp.I*p), w: sp.exp(sp.I*q)}) - Delta))

# ---------------- B. vertex-direction slice p=2q -----------------------
F0q = sp.cos(m*q)**2 + sp.cos(m*q) - 1
check('B1 f0(2q,q) = cos(mq)^2 + cos(mq) - 1 (symbolic m)',
      zero(f0.subs(p, 2*q) - F0q))
Dslice = sp.expand_trig(Delta.subs(p, 2*q))
Dx = (1 - x)**3 * (1 + x) / 4
check('B2 Delta(2q,q) = (1-x)^3 (1+x)/4 with x = cos q',
      zero(Dslice - Dx.subs(x, sp.cos(q))))

# ---------------- C. slice image of invariant residuals ----------------
# rotation by 60 degrees on frequencies (i,j)->(-j,i+j); dual on (p,q): (p,q)->(p-q,p)
rotk = lambda P: (P[0] - P[1], P[0])
kstar = (4*sp.pi/3, 2*sp.pi/3)
r2 = rotk(rotk(kstar))
check('C1a 120-degree rotation fixes the slice point q=2pi/3, i.e. (4pi/3,2pi/3), mod 2pi',
      all(sp.simplify((r2[i] - kstar[i]) / (2*sp.pi)).is_integer for i in range(2)))
dDx = sp.diff(Dx, x).subs(x, sp.Rational(-1, 2))
k = sp.symbols('k', integer=True, nonnegative=True)
dF0 = sp.diff(F0q, q)
okres = True
for rres in range(3):
    val = sp.simplify(dF0.subs(m, 3*k + rres).subs(q, 2*sp.pi/3))
    okres &= zero(val)
check('C1b Delta\'(-1/2)=0, Delta(-1/2)!=0, and d/dq f0(2q,q)=0 at q=2pi/3 for m=0,1,2 mod 3',
      dDx == 0 and Dx.subs(x, sp.Rational(-1, 2)) != 0 and okres)


def rot(P):
    return (-P[1], P[0] + P[1])


def orbit(P):
    out = set()
    for _ in range(6):
        out.add(P)
        out.add((P[1], P[0]))          # reflection (i,j)->(j,i)
        P = rot(P)
    return out


def sym_orbit(i0, j0):
    pts, P = [], (i0, j0)
    for _ in range(6):
        pts += [P, (P[1], P[0])]
        P = (-P[1], P[0] + P[1])
    return pts


def tops_ok(i0, j0, top, amin):
    """2i+j over the symbolic orbit is <= top for a>=amin (linear in a)."""
    for (i, j) in sym_orbit(i0, j0):
        d = sp.expand(top - (2*i + j))
        if not (d.subs(a, amin) >= 0 and sp.diff(d, a) >= 0):
            return False
    return True


check('C2a orbit of (a,0), a>=1: slice frequencies <= 2a, attained',
      tops_ok(a, 0, 2*a, 1) and any(sp.expand(2*i + j - 2*a) == 0 for i, j in sym_orbit(a, 0)))
check('C2b orbit of (a,1), a>=1: slice frequencies <= 2a+1, attained',
      tops_ok(a, 1, 2*a + 1, 1) and any(sp.expand(2*i + j - 2*a - 1) == 0 for i, j in sym_orbit(a, 1)))
ap = sp.symbols('ap', positive=True)            # ap = a - 1 >= 0 handled via a = ap + 1 > 1 and a = 1
hex_a1 = sp.Max(sp.Abs(ap + 1), 1, sp.Abs(ap + 2))
check('C2c hex norm of (a,1) is a+1 for a>=1, so (a,1) in H_n iff a<=n-1 (Review R1)',
      sp.simplify(hex_a1 - (ap + 2)) == 0 and hexn(1, 1) == 2)


def slice_image(n):
    """Coefficient vectors (in cos(jq), j=0..2n) of slice restrictions of orbit sums in H_n."""
    pts = [(i, j) for i in range(-n, n + 1) for j in range(-n, n + 1) if hexn(i, j) <= n]
    seen, rows = set(), []
    for P in pts:
        o = frozenset(orbit(P))
        if o in seen:
            continue
        seen.add(o)
        v = [0] * (2*n + 1)
        for (i, j) in o:
            v[abs(2*i + j)] += 1
        rows.append(v)
    return sp.Matrix(rows)


def cheb_to_x(vec):
    return sp.expand(sum(c * sp.chebyshevt(j, x) for j, c in enumerate(vec)))


okrank, okcon = True, True
for mm in range(3, 9):
    n = mm - 2
    M = slice_image(n)
    okrank &= (M.rank() == 2*n)
    for r in range(M.rows):
        g = cheb_to_x(list(M.row(r)))
        okcon &= (sp.diff(g, x).subs(x, sp.Rational(-1, 2)) == 0)
check('C3 diagnostics m=3..8: slice image has rank 2(m-2) and every element has g\'(-1/2)=0',
      okrank and okcon)
M3 = slice_image(1)
coef = lambda g: [sp.Poly(g, x).coeff_monomial(x**e) for e in range(3)]
rows3 = [coef(cheb_to_x(list(M3.row(r)))) for r in range(M3.rows)]
check('C4 m=3 control: slice image spanned by 1 and 4x^2+4x-2 (the promoted m=3 form)',
      sp.Matrix(rows3).rank() == 2
      and sp.Matrix(rows3 + [[1, 0, 0], [-2, 4, 4]]).rank() == 2)

# ---------------- D. slice-route closure for m>=629 ---------------------
S3 = sp.sqrt(3)
# D1: for m>=629 with L=6*ceil(sqrt(m)/2), K2<sqrt3 m+6:
#   degree  sqrt3*m + 6 + 2L <= 2m   follows from (2-sqrt3) y^2 - 6 y - 18 >= 0, y = sqrt(m)
#   deficit 3L^4 >= 243 m^2 >= excess  follows from 135 m^2 - 216 sqrt3 m - 324 >= 0
Qdeg = (2 - S3)*y**2 - 6*y - 18
vertex = sp.Rational(3, 1) / (2 - S3)
check('D1a (2-sqrt3)y^2-6y-18 > 0 at y=sqrt(629), and y=sqrt(629) beyond the vertex (increasing)',
      sp.simplify(Qdeg.subs(y, sp.sqrt(629))) > 0 and sp.sqrt(629) > vertex)
Qexc = 135*m**2 - 216*S3*m - 324
check('D1b 135m^2-216sqrt3 m-324 > 0 for m>=4 (positive at 4, increasing beyond vertex)',
      sp.simplify(Qexc.subs(m, 4)) > 0 and 4 > 216*S3/270)


def construction(mm):
    c = 0 if mm % 2 == 0 else 3
    t = 3*mm*mm
    K1 = isqrt(t)
    while K1 % 6 != c or K1*K1 >= t:
        K1 -= 1
    K2 = K1 + 6
    tt = 1
    while 4*tt*tt < mm:          # tt = ceil(sqrt(m)/2), exact
        tt += 1
    L = 6*tt
    s2 = sp.Integer(t)
    lam = (K2**2 - s2) / (K2**2 - K1**2)
    Mq = lam*K1**4 + (1 - lam)*K2**4
    one_minus_alpha = (Mq - s2**2) / (3*sp.Integer(L)**4)
    alpha = 1 - one_minus_alpha
    H = 1 - sp.Rational(1, 2)*(1 - sp.cos(L*q))**2
    A = lam*sp.cos(K1*q) + (1 - lam)*sp.cos(K2*q)
    B = alpha + (1 - alpha)*H
    return dict(K1=K1, K2=K2, L=L, lam=lam, alpha=alpha, A=A, B=B)


for mm in (629, 630, 1000):
    C = construction(mm)
    F = C['A'] * C['B']
    F0 = sp.cos(mm*q)**2 + sp.cos(mm*q) - 1
    ser = sp.series(F - F0, q, 0, 6).removeO()
    ok = (sp.simplify(ser) == 0
          and 0 <= C['lam'] <= 1 and 0 <= C['alpha'] <= 1
          and C['K2'] + 2*C['L'] <= 2*mm
          and C['K1'] % 3 == 0 and C['K1'] % 2 == mm % 2 and C['L'] % 6 == 0
          and sp.simplify(F.subs(q, sp.pi) - (-1)**mm) == 0
          and sp.simplify(sp.diff(F, q).subs(q, 2*sp.pi/3)) == 0)
    check(f"D2 m={mm}: K1={C['K1']}, K2={C['K2']}, L={C['L']}; F-F0=O(q^6), F(pi)=(-1)^m, "
          f"F'(2pi/3)=0, lambda,alpha in [0,1], degree K2+2L<=2m", ok)

# D3: second route (closed-form moments, no series) and a negative control.
okm = True
for mm in (629, 630, 1000):
    C = construction(mm)
    K1, K2, L, lam, alpha = C['K1'], C['K2'], C['L'], C['lam'], C['alpha']
    mu2 = lam*K1**2 + (1 - lam)*K2**2
    mu4 = lam*K1**4 + (1 - lam)*K2**4 - 3*(1 - alpha)*sp.Integer(L)**4
    okm &= sp.simplify(mu2 - 3*mm**2) == 0 and sp.simplify(mu4 - 9*mm**4) == 0
check('D3a closed-form moments (algebraic; cancels by the definition of alpha, so it is '
      'not an independent test of the q^4 Taylor coefficient: D2 is) mu2 = 3m^2, mu4 = 9m^4', okm)
C = construction(629)
Fbad = C['A']                                    # drop the B factor (alpha=1)
F0b = sp.cos(629*q)**2 + sp.cos(629*q) - 1
check('D3b negative control: without B the q^4 condition fails (excess > 0)',
      sp.simplify(sp.series(Fbad - F0b, q, 0, 6).removeO()) != 0)
mm = 3
check('D3c m=3: construction degree bound fails (K2+2L>2m), consistent with SCALAR_INFEASIBLE_M3',
      construction(mm)['K2'] + 2*construction(mm)['L'] > 2*mm)

print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
raise SystemExit(0 if all(CHECKS) else 1)
