"""Exact structural reduction for M1-B19 of the HEX_SUPREMUM gate (S19).

Contract: theory/HEX_SUPREMUM_GATE.md, preregistered at 86573ca; M1-B19
authorized 2026-11-03 («Autorizar M1-B19 ... empezando exclusivamente por la
reducción estructural»). Run from the repository root:

  python -B scripts/verify_hex_supremum_b19.py

Fail-closed, SymPy only, zero tolerance, no solver of the nonlinear system
(this is Stage A-type reduction, not a budgeted solver run). Imports
read-only the reviewed verify_hex_supremum_gate.py (hexagon, layers) and,
through it, verify_hex_ceiling_gate.py; neither is modified.

What is computed and certified here, for walks with F within S19 (19 points)
and the normal form A(n) = r n.sigma:
- L1, layer equations of facet-line rigidity on the three facet normals:
  56 free real parameters left (as in the parent gate's 900 s attempt).
- L2, first-moment equations (lemma A3 of the report): for each facet
  normal n, edge direction e = Rot90(n), each layer m, and x_+/- the
  +-eigenvectors of n.sigma: sum_{h in layer} (h.e) <x, A_h x> = 0.
  28 free parameters left.
- L3, off-diagonal first-order unitarity on the facet line (lemma A4):
  sum_{h in m} (h.e) <x+, A_h x-> = sum_{h in -m} (h.e) conj<x-, A_h x+>.
  18 free parameters left; L1 + L2 + L3 consistent.
- Controls: the saturating square walk satisfies L1, L2, L3; the whole
  pipeline on the 3x3 square support keeps that walk and all its reduced
  unitarity equations vanish there; unitarity_equations is 0 on a unitary
  walk and nonzero on a perturbed one.
- The reduced S19 system (18 parameters, 730 quadratic equations) and an
  exact real infeasibility certificate: rational multipliers c_i from
  scripts/data/hex_s19_certificate.json (found by the exploratory
  explore_hex_s19_certificate.py), p = sum c_i f_i, Gram matrix of p in the
  basis (1, t) positive definite over QQ(sqrt3) by exact elimination (all
  19 pivots > 0). Hence p > 0 on R^18 and no real solution exists.
- S7 with L1 + L2 + L3 (informational; consistent, 1 free parameter).
What is not certified here: the analytic proofs of rigidity, A3 and A4 and
the normal form (report). Runtime about 11 minutes (the exact certificate
expansion dominates).
"""
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_hex_supremum_gate as m1  # reviewed, read-only

CHECKS = []
SX, SY, I2 = m1.SX, m1.SY, m1.I2
R3 = sp.sqrt(3)


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))


def eigvecs(n):
    """Unit +- eigenvectors of n.sigma for n in the xy plane at angle a."""
    a = sp.atan2(n[1], n[0])
    xp = sp.Matrix([1, sp.exp(sp.I * a)]) / sp.sqrt(2)
    xm = sp.Matrix([1, -sp.exp(sp.I * a)]) / sp.sqrt(2)
    return xp.applyfunc(sp.simplify), xm.applyfunc(sp.simplify)


def unknowns(npts):
    """Complex unknowns z (4 per point) and formal symbols w standing for
    conj(z); equations are linear in (z, w) and split into real form in
    (Re z, Im z) afterwards."""
    zs, ws, A, Abar = [], [], [], []
    for k in range(npts):
        z = sp.symbols(f"z{k}_0:4")
        w = sp.symbols(f"w{k}_0:4")
        zs.extend(z)
        ws.extend(w)
        A.append(sp.Matrix([[z[0], z[1]], [z[2], z[3]]]))
        Abar.append(sp.Matrix([[w[0], w[1]], [w[2], w[3]]]))
    return zs, ws, A, Abar


def linear_system(pts, normals, r, N, A, moments, Abar=None):
    """Linear equations (expressions == 0) in z and, for L3, w = conj(z)."""
    eqs = []
    for n in normals:
        L = m1.layers(pts, n, r, N)
        Pp = (I2 + n[0] * SX + n[1] * SY) / 2
        Pm = (I2 - n[0] * SX - n[1] * SY) / 2
        e = sp.Matrix([-n[1], n[0]])
        xp, xm = eigvecs(n)
        for lev, idx in L.items():
            target = Pp if lev == N else Pm if lev == -N else sp.zeros(2)
            M = sum((A[i] for i in idx), sp.zeros(2)) - target
            eqs += [sp.expand(x) for x in M]
            if moments:
                for x in (xp, xm):
                    s_ = sum((sp.nsimplify((pts[i].T * e)[0]) * (x.H * A[i] * x)[0] for i in idx), 0)
                    eqs.append(sp.expand(s_))
            if Abar is not None:
                # L3: off-diagonal anti-Hermiticity of D^dag d_e U on the line:
                # sum_{h in lev} (h.e) <x+, A_h x-> = sum_{h in -lev} (h.e) conj<x-, A_h x+>
                lhs = sum((sp.nsimplify((pts[i].T * e)[0]) * (xp.H * A[i] * xm)[0] for i in idx), 0)
                rhs = sum((sp.nsimplify((pts[i].T * e)[0]) * (xm.T * Abar[i] * xp.conjugate())[0]
                           for i in L.get(-lev, [])), 0)
                eqs.append(sp.expand(lhs - rhs))
    return [q for q in eqs if q != 0]


def real_form(eqs, zs, ws):
    """System C z + D conj(z) = b  ->  real system in (Re z, Im z)."""
    n = len(zs)
    CD, b = sp.linear_eq_to_matrix(eqs, list(zs) + list(ws))
    rows = []
    for i in range(CD.rows):
        re_row, im_row = [], []
        for j in range(n):
            c, d = sp.expand(CD[i, j]), sp.expand(CD[i, n + j])
            cr, ci = sp.expand(sp.re(c)), sp.expand(sp.im(c))
            dr, di = sp.expand(sp.re(d)), sp.expand(sp.im(d))
            re_row += [cr + dr, -ci + di]
            im_row += [ci + di, cr - dr]
        br, bi = sp.expand(sp.re(b[i])), sp.expand(sp.im(b[i]))
        rows += [re_row + [br], im_row + [bi]]
    return rows


def rank_and_free(eqs, zs, ws):
    rows = real_form(eqs, zs, ws)
    nv = 2 * len(zs)
    full = DomainMatrix.from_list_sympy(len(rows), nv + 1, rows, extension=True)
    coef = DomainMatrix.from_list_sympy(len(rows), nv, [r_[:nv] for r_ in rows], extension=True)
    rk, rka = coef.rank(), full.rank()
    return rk, nv - rk, rka


def parametrize(eqs, zs, ws, tname="t"):
    """Solve the real linear system exactly over QQ<sqrt3>; return the real
    and imaginary parts (P, Q) of each A_h as 2x2 matrices of affine forms in
    the free real parameters t."""
    rows = real_form(eqs, zs, ws)
    nv = 2 * len(zs)
    full = DomainMatrix.from_list_sympy(len(rows), nv + 1, rows, extension=True)
    R, pivots = full.rref()
    R = R.to_Matrix()
    free = [j for j in range(nv) if j not in pivots]
    t = sp.symbols(f"{tname}0:{len(free)}", real=True)
    val = {}
    for j, tj in zip(free, t):
        val[j] = tj
    for row, j in enumerate(pivots):
        val[j] = sp.expand(R[row, nv] - sum(R[row, f] * val[f] for f in free))
    P, Q = [], []
    for k in range(len(zs) // 4):
        P.append(sp.Matrix(2, 2, [val[2 * (4 * k + m)] for m in range(4)]))
        Q.append(sp.Matrix(2, 2, [val[2 * (4 * k + m) + 1] for m in range(4)]))
    return t, P, Q


def unitarity_equations(pts, P, Q):
    """Real polynomial equations of sum_{h-h'=d} A_h A_h'^dag = delta I and
    sum_{h-h'=d} A_h'^dag A_h = delta I, with A = P + iQ."""
    blocks = {}
    for i, hi in enumerate(pts):
        for j, hj in enumerate(pts):
            d = tuple(sp.nsimplify(c) for c in (hi - hj))
            b = blocks.setdefault(d, [sp.zeros(2) for _ in range(4)])
            # A_i A_j^dag = (P_i P_j^T + Q_i Q_j^T) + i (Q_i P_j^T - P_i Q_j^T)
            b[0] += P[i] * P[j].T + Q[i] * Q[j].T
            b[1] += Q[i] * P[j].T - P[i] * Q[j].T
            # A_j^dag A_i = (P_j^T P_i + Q_j^T Q_i) + i (P_j^T Q_i - Q_j^T P_i)
            b[2] += P[j].T * P[i] + Q[j].T * Q[i]
            b[3] += P[j].T * Q[i] - Q[j].T * P[i]
    eqs = set()
    for d, (re1, im1, re2, im2) in blocks.items():
        target = I2 if all(c == 0 for c in d) else sp.zeros(2)
        for M in (re1 - target, im1, re2 - target, im2):
            for e in M:
                e = sp.expand(e)
                if e != 0:
                    eqs.add(e)
    return sorted(eqs, key=sp.default_sort_key)


def gram_of(poly, t):
    """Unique symmetric Gram matrix of a quadratic polynomial in the basis (1, t)."""
    n = len(t)
    G = sp.zeros(n + 1)
    for mon, c in sp.Poly(poly, *t).terms():
        nz = [i for i, p_ in enumerate(mon) if p_]
        if not nz:
            G[0, 0] += c
        elif len(nz) == 1 and mon[nz[0]] == 1:
            G[0, nz[0] + 1] += c / 2
            G[nz[0] + 1, 0] += c / 2
        elif len(nz) == 1:
            G[nz[0] + 1, nz[0] + 1] += c
        else:
            i, j = nz
            G[i + 1, j + 1] += c / 2
            G[j + 1, i + 1] += c / 2
    return G


def positive_q3(x):
    """Exact sign test for x = a + b sqrt3, a, b rational."""
    x = sp.expand(x)
    b_ = x.coeff(R3)
    a_ = sp.expand(x - b_ * R3)
    if not (a_.is_Rational and b_.is_Rational):
        raise ValueError(f"not in Q(sqrt3): {x}")
    if a_ >= 0 and b_ >= 0:
        return a_ > 0 or b_ > 0
    if a_ > 0 and b_ < 0:
        return a_ ** 2 > 3 * b_ ** 2
    if a_ < 0 and b_ > 0:
        return 3 * b_ ** 2 > a_ ** 2
    return False


def ldl_pivots_positive(G):
    """Gaussian elimination without pivoting over QQ<sqrt3>; a real symmetric
    matrix is positive definite iff every pivot is positive (Sylvester)."""
    dm = DomainMatrix.from_list_sympy(G.rows, G.cols, G.tolist(), extension=True)
    K = dm.domain
    a = [list(row) for row in dm.to_list()]
    n = len(a)
    pivots = []
    for k in range(n):
        pk = a[k][k]
        if not positive_q3(K.to_sympy(pk)):
            return False, k, K.to_sympy(pk)
        pivots.append(pk)
        for i in range(k + 1, n):
            f = a[i][k] / pk
            if f != K.zero:
                for j in range(k, n):
                    a[i][j] = a[i][j] - f * a[k][j]
    return True, n, None


def check_certificate(t, eqs, path):
    """Exact real infeasibility certificate (contract Sec. 4 (ii) with
    constant multipliers): p = sum_i c_i f_i with rational c_i read from
    `path`; if the Gram matrix G of p in the basis (1, t) is positive
    definite then p(t) = (1,t) G (1,t)^T > 0 for every real t, while every
    f_i vanishes at a solution. In contract form: for 0 < mu <= 1/(G^-1)_00,
    G - mu e0 e0^T is PSD, = L D L^T with D >= 0, so p = mu + sum_j d_j l_j^2
    and -1 = sum_j (d_j/mu) l_j^2 + sum_i (-c_i/mu) f_i, a weighted sum of
    squares with exact coefficients. The verifier checks G > 0 exactly, which
    is what makes such a representation exist."""
    import json
    from fractions import Fraction
    data = json.loads(Path(path).read_text())
    c = [sp.Rational(Fraction(x).numerator, Fraction(x).denominator) for x in data["multipliers"]]
    record("certificate file matches the equation list", data["n_equations"] == len(eqs) == len(c))
    p = sp.expand(sum((ci * fi for ci, fi in zip(c, eqs) if ci != 0), sp.Integer(0)))
    G = gram_of(p, t)
    v = sp.Matrix([1] + list(t))
    record("p equals (1,t) G (1,t)^T exactly", sp.expand((v.T * G * v)[0] - p) == 0)
    ok, k, piv = ldl_pivots_positive(G)
    record("CERTIFICATE: the Gram matrix of p = sum c_i f_i is positive definite over QQ(sqrt3) "
           "(all 19 pivots > 0): p > 0 on R^18, so the reduced S19 system has no real solution",
           ok, "all pivots positive" if ok else f"pivot {k} not positive: {piv}")


def check_square_control():
    """Square substrate: U = exp(-ik_x s_x) exp(-ik_y s_y) has coefficients
    A_(hx,hy) = X_hx Y_hy at e^{-ik.h}, X_+-1 = (I +- s_x)/2,
    Y_+-1 = (I +- s_y)/2; it saturates c_0 = r_in = 1 with A(n) = n.sigma.
    Facet normals x, y. The walk must satisfy the layer sums and the
    first-moment equations (A3)."""
    X = {1: (I2 + SX) / 2, -1: (I2 - SX) / 2}
    Y = {1: (I2 + SY) / 2, -1: (I2 - SY) / 2}
    pts = [sp.Matrix([a, b]) for a in (1, -1) for b in (1, -1)]
    A = [X[a] * Y[b] for a in (1, -1) for b in (1, -1)]
    ok_sum = sp.simplify(sum(A, sp.zeros(2)) - I2) == sp.zeros(2)
    ok = True
    for n in (sp.Matrix([1, 0]), sp.Matrix([0, 1])):
        e = sp.Matrix([-n[1], n[0]])
        xp, xm = eigvecs(n)
        Pp = (I2 + n[0] * SX + n[1] * SY) / 2
        levels = {}
        for i, p in enumerate(pts):
            levels.setdefault((p.T * n)[0], []).append(i)
        ok = ok and sp.simplify(sum((A[i] for i in levels[1]), sp.zeros(2)) - Pp) == sp.zeros(2)
        for lev, idx in levels.items():
            for x in (xp, xm):
                s_ = sp.simplify(sum(((pts[i].T * e)[0] * (x.H * A[i] * x)[0] for i in idx), 0))
                ok = ok and s_ == 0
            lhs = sum(((pts[i].T * e)[0] * (xp.H * A[i] * xm)[0] for i in idx), 0)
            rhs = sum(((pts[i].T * e)[0] * sp.conjugate((xm.H * A[i] * xp)[0]) for i in levels.get(-lev, [])), 0)
            ok = ok and sp.simplify(lhs - rhs) == 0
    record("CONTROL square: the saturating walk satisfies the layer sums, A3 (L2) and the off-diagonal L3",
           ok_sum and ok)
    P = [Ak.applyfunc(sp.re) for Ak in A]
    Q = [Ak.applyfunc(sp.im) for Ak in A]
    record("CONTROL square: unitarity_equations of the unitary square walk are all identically 0",
           unitarity_equations(pts, P, Q) == [])
    P[0] = P[0] + sp.Rational(1, 7) * I2
    record("CONTROL square: a perturbed (non-unitary) coefficient is detected by unitarity_equations",
           unitarity_equations(pts, P, Q) != [])


def check_pipeline_square_control():
    """Positive control of the whole reduction pipeline (L1 + L2 + L3,
    parametrize, unitarity_equations) on the 3x3 square support, which, like
    S19, has interior and edge-interior points: the known saturating walk
    exp(-ik_x s_x) exp(-ik_y s_y) must lie in the parametrized family and
    satisfy every reduced equation."""
    pts = [sp.Matrix([a, b_]) for a in (-1, 0, 1) for b_ in (-1, 0, 1)]
    normals = [sp.Matrix([1, 0]), sp.Matrix([0, 1])]
    zs, ws, A, Abar = unknowns(len(pts))
    e3 = linear_system(pts, normals, sp.Integer(1), 1, A, moments=True, Abar=Abar)
    t, P, Q = parametrize(e3, zs, ws, tname="u")
    X = {1: (I2 + SX) / 2, -1: (I2 - SX) / 2}
    Y = {1: (I2 + SY) / 2, -1: (I2 - SY) / 2}
    walk = [X[int(p_[0])] * Y[int(p_[1])] if p_[0] != 0 and p_[1] != 0 else sp.zeros(2) for p_ in pts]
    match = []
    for k in range(len(pts)):
        match += list(P[k] - walk[k].applyfunc(sp.re)) + list(Q[k] - walk[k].applyfunc(sp.im))
    match = [sp.expand(m) for m in match if sp.expand(m) != 0]
    sol = sp.solve(match, t, dict=True) if match else [{}]
    ok = len(sol) >= 1 and all(sp.expand(m.subs(sol[0])) == 0 for m in match)
    record("CONTROL pipeline (3x3 square): the saturating walk lies in the L1+L2+L3 parametrized family",
           ok, f"{len(t)} free parameters")
    if ok:
        eqs = unitarity_equations(pts, P, Q)
        val = {ti: sol[0].get(ti, 0) for ti in t}
        record("CONTROL pipeline (3x3 square): it satisfies every reduced unitarity equation",
               all(sp.expand(e.subs(val)) == 0 for e in eqs), f"{len(eqs)} equations")


def main():
    pts, verts, normals, r = m1.hexagon(2 * m1.G1)
    N = 2
    normals = normals[:3]
    record("S19: 19 points, r_in = sqrt3/2, three facet normals", len(pts) == 19 and sp.simplify(r - R3 / 2) == 0)
    zs, ws, A, Abar = unknowns(len(pts))
    e1 = linear_system(pts, normals, r, N, A, moments=False)
    rk1, free1, rka1 = rank_and_free(e1, zs, ws)
    print(f"  L1 (layer sums): rank {rk1}, free real parameters {free1} of {2 * len(zs)}")
    record("L1 consistent", rka1 == rk1)
    record("L1 leaves 56 free real parameters, as in the parent gate's attempt (hex-ceiling report Sec. 4)",
           free1 == 56)
    e2 = linear_system(pts, normals, r, N, A, moments=True)
    rk2, free2, rka2 = rank_and_free(e2, zs, ws)
    print(f"  L1 + L2 (with first moments): rank {rk2}, free real parameters {free2}")
    record("L1 + L2 consistent (rank of augmented matrix equals rank)", rka2 == rk2)
    record("L2 adds independent linear constraints beyond L1", rk2 > rk1, f"{rk2 - rk1} added")
    record("L1 + L2 leave 28 free real parameters", free2 == 28)
    e3 = linear_system(pts, normals, r, N, A, moments=True, Abar=Abar)
    rk3, free3, rka3 = rank_and_free(e3, zs, ws)
    print(f"  L1 + L2 + L3 (with off-diagonal first order): rank {rk3}, free real parameters {free3}")
    record("L1 + L2 + L3 consistent", rka3 == rk3, f"rank {rk3}, augmented {rka3}")
    check_square_control()
    check_pipeline_square_control()
    print("== S19 reduced system and exact certificate")
    t, P, Q = parametrize(e3, zs, ws)
    eqs = unitarity_equations(pts, P, Q)
    record("reduced S19 system: 18 real parameters, 730 distinct quadratic equations",
           len(t) == 18 and len(eqs) == 730)
    check_certificate(t, eqs, ROOT / "scripts" / "data" / "hex_s19_certificate.json")
    print("== S7 (minimal support, second route to T2)")
    p7, v7, n7, r7 = m1.hexagon(m1.G1)
    z7, w7, A7, B7 = unknowns(len(p7))
    e7 = linear_system(p7, n7[:3], r7, 1, A7, moments=True, Abar=B7)
    rk7, free7, rka7 = rank_and_free(e7, z7, w7)
    print(f"  S7 with L1 + L2 + L3: rank {rk7}, augmented {rka7}, free real parameters {free7}")
    record("S7: L1 + L2 + L3 computed (informational; T2 decides S7)", True,
           "inconsistent" if rka7 > rk7 else f"consistent, {free7} free")
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (M1-B19 structural reduction).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
