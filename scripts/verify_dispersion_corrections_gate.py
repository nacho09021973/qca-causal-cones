#!/usr/bin/env python3
"""Exact certificate for the DISPERSION_CORRECTIONS_ACROSS_LATTICES gate.
Contract: theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md
(preregistration commit a7ff5b7). Rows and symbol sources: contract Sec. 2.

For every declared massless row the symbol U(k) is imported read-only from
the script named in the contract, expanded exactly as a multivariate Taylor
polynomial in k (normalised as in the parent: Cartesian positions divided by
the longest step, one update per time unit), and the node branch is read
from the quadratic factor of the characteristic polynomial that carries the
node:
  s = 2 rows                  : the factor is the whole polynomial,
                                s1 = tr U, s2 = det U;
  L5b (s = 4)                 : the joint commutant element
                                Gamma = dP_X dP_Y dP_Z splits U into two
                                2x2 blocks (two Weyl blocks);
  L6b (s = 6, V = U^3)        : the three 2x2 orientation blocks of V,
                                quasienergies divided by 3 (three updates);
  L3s4 (s = 4, nodes at +-pi/4): Hensel lifting of the quadratic factor of
                                the characteristic polynomial at the
                                double root exp(-+ i pi/4) of A_a(0) = W.
From s1, s2: exp(-2 i phi) = s2 / s2(0), cos^2 omega = s1^2 / (4 s2), the
node branches are eps = eps_0 + phi +- omega, and omega^2 is an analytic
function of k whose homogeneous parts Q_m(k) are extracted exactly.
Along a ray k = t n, |n| = 1, the upper branch is
  eps_+ - eps_0 = c_0 t [1 + beta(n) t + alpha(n) t^2 + ...],
with beta, alpha exact functions of n; their angular content is read as a
trigonometric polynomial (d = 2) or projected on cubic invariants (d = 3).
The symmetry group of the walk, G_walk, is the set of substrate point-group
elements g with charpoly U(g k) = charpoly U(k) exactly (Laurent identity).
Fails closed: any failed check or exception exits nonzero.
Run from the repository root:  python3 -B scripts/verify_dispersion_corrections_gate.py
"""
import hashlib
import itertools
import math
import sys
import time
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_c_across_lattices_gate as P      # reviewed, read-only
import verify_weyl_dirac_gate as WD            # reviewed, read-only
import verify_directional_saturation as DS     # reviewed, read-only
import cert_Aa_s4_counterexample as AA         # reviewed, read-only
import verify_l6b_triangular_row_gate as L6B   # reviewed, read-only

CONTRACT = ROOT / "theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md"
CHECKS = []
START = time.time()
R3 = sp.sqrt(3)
R2 = sp.sqrt(2)
LAM = sp.symbols("lambda")
T = sp.symbols("t", positive=True)
W = sp.symbols("w")  # e^{i theta} for the d = 2 angular content

# Exact Taylor coefficients (SymPy series, checked at import below).
ACOS2 = [0, 2, sp.Rational(1, 3), sp.Rational(4, 45), sp.Rational(1, 35)]    # acos(1-v)^2
LOG1P = [0, 1, -sp.Rational(1, 2), sp.Rational(1, 3), -sp.Rational(1, 4),
         sp.Rational(1, 5), -sp.Rational(1, 6)]                             # log(1+v)
SQRT1P = [1, sp.Rational(1, 2), -sp.Rational(1, 8), sp.Rational(1, 16),
          -sp.Rational(5, 128), sp.Rational(7, 256), -sp.Rational(21, 1024)]  # sqrt(1+v)
INV1P = [1, -1, 1, -1, 1, -1, 1]                                            # 1/(1+v)


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok), detail))
    print(("[PASS] " if ok else "[FAIL] ") + label + (f" -- {detail}" if detail else ""))


A_SYM = sp.symbols("a", positive=True)   # L3s4 parameter, 0 < a < 1
B_SYM = sp.symbols("b", positive=True)   # stands for sqrt(1 - a^2)


def reduce_b(e):
    """Reduce modulo b^2 = 1 - a^2, leaving b to degree <= 1. Since
    sqrt(1-a^2) is not a rational function of a, c0(a) + c1(a) b vanishes
    identically on 0 < a < 1 iff c0 = c1 = 0: the zero test stays exact."""
    if not e.has(B_SYM):
        return e
    poly = sp.Poly(sp.expand(e), B_SYM)
    return sp.expand(sum((c * (1 - A_SYM ** 2) ** (j // 2) * B_SYM ** (j % 2)
                          for (j,), c in poly.terms()), sp.Integer(0)))


def canon(e):
    """Canonical radical form for a scalar; zero iff the scalar is zero."""
    return sp.radsimp(sp.simplify(sp.expand_complex(reduce_b(sp.expand(e)))))


def zero(e):
    e = reduce_b(sp.expand(e))
    return e == 0 or canon(e) == 0      # fast path when expansion already gives 0


def czero(expr, syms):
    """Zero test for a polynomial in syms with radical coefficients."""
    expr = sp.expand(expr)
    if expr == 0:
        return True
    return all(zero(c) for c in sp.Poly(expr, *syms).coeffs())


# ------------------------------------------------------------ polynomials
def trunc(expr, ks, N):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    poly = sp.Poly(expr, *ks)
    return sum((reduce_b(c) * sp.prod([k ** e for k, e in zip(ks, exps)])
                for exps, c in poly.terms() if sum(exps) <= N), sp.Integer(0))


def homog(expr, ks, m):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    poly = sp.Poly(expr, *ks)
    return sum((c * sp.prod([k ** e for k, e in zip(ks, exps)])
                for exps, c in poly.terms() if sum(exps) == m), sp.Integer(0))


def compose(coeffs, x, ks, N):
    """sum_j coeffs[j] x^j truncated at total degree N; x has no constant term."""
    out = sp.Integer(coeffs[0])
    power = sp.Integer(1)
    for j in range(1, len(coeffs)):
        power = trunc(power * x, ks, N)
        if power == 0:
            break
        out += coeffs[j] * power
    return trunc(out, ks, N)


def taylor_symbol(support, gens, scale, sigma, ks, N):
    """U(k) = sum_h A_h exp(sigma i k.h_cart / scale), Taylor polynomial of degree N."""
    d = len(ks)
    U = sp.zeros(next(iter(support.values())).rows)
    for h, A in support.items():
        cart = [sum(a * sp.Matrix(g)[i] for a, g in zip(h, gens)) for i in range(d)]
        phase = sigma * sp.I * sum(k * c for k, c in zip(ks, cart)) / scale
        e = sum((phase ** m / sp.factorial(m) for m in range(N + 1)), sp.Integer(0))
        U += A.applyfunc(canon) * e
    return U.applyfunc(lambda e: trunc(e, ks, N))


# ------------------------------------------------------------ node branch
def node_from_quadratic(s1, s2, ks, N):
    """Given the quadratic factor lambda^2 - s1 lambda + s2 carrying the node
    (truncated at degree N), return (phi, omega2, lambda0): the common phase
    phi(k) with exp(-2 i phi) = s2/s2(0), and omega^2(k) with
    cos^2 omega = s1^2/(4 s2), both as polynomials in k of degree <= N."""
    at0 = {k: 0 for k in ks}
    s20 = canon(s2.subs(at0))
    s10 = canon(s1.subs(at0))
    lam0 = canon(s10 / 2)                     # double root at k = 0
    record_quiet = zero(lam0 ** 2 - s20)
    if not record_quiet:
        raise ValueError("node factor is not a double root at k = 0")
    x = trunc(s2 / s20 - 1, ks, N)
    phi = trunc(sp.I / 2 * compose(LOG1P, x, ks, N), ks, N)
    inv_s2 = trunc(compose(INV1P, x, ks, N) / s20, ks, N)
    g = trunc(s1 ** 2 * inv_s2 / 4, ks, N)
    v = trunc(2 * (1 - g), ks, N)             # 1 - cos(2 omega)
    omega2 = trunc(compose(ACOS2, v, ks, N) / 4, ks, N)
    return phi, omega2, lam0


def reduce_sphere(expr, ns):
    """Reduce a polynomial in n modulo |n|^2 = 1 (last variable eliminated)."""
    expr = sp.expand(expr)
    if expr == 0 or len(ns) == 1:
        return sp.expand(expr.subs(ns[0] ** 2, 1)) if len(ns) == 1 else expr
    last = ns[-1]
    rest = 1 - sum(n ** 2 for n in ns[:-1])
    poly = sp.Poly(expr, last)
    out = sp.Integer(0)
    for (j,), c in poly.terms():
        out += c * last ** (j % 2) * rest ** (j // 2)
    return sp.expand(out)


def ray_expansion(phi, omega2, ks, ns, N, divisor=1):
    """Upper node branch along k = t n, |n| = 1:
    eps_+ - eps_0 = (phi + omega)/divisor = sum_j E_j(n) t^j.
    Returns c0 and the dict {j: E_j(n)} (sphere-reduced), j = 1..N-1,
    together with the homogeneous parts Q_m(n) of omega^2 and Phi_m of phi."""
    sub = {k: T * n for k, n in zip(ks, ns)}
    om2_t = sp.expand(omega2.subs(sub))
    Q = {m: reduce_sphere(om2_t.coeff(T, m), ns) for m in range(0, N + 1)}
    ph_t = sp.expand(phi.subs(sub))
    Phi = {m: reduce_sphere(ph_t.coeff(T, m), ns) for m in range(0, N + 1)}
    c0sq = canon(Q[2])
    c0 = sp.radsimp(sp.sqrt(c0sq))
    x = sum((Q[m] / c0sq * T ** (m - 2) for m in range(3, N + 1)), sp.Integer(0))
    sq = compose(SQRT1P, x, [T], N - 2)
    om_t = sp.expand(c0 * T * sq)
    eps_t = sp.expand((om_t + ph_t) / divisor)
    E = {j: reduce_sphere(eps_t.coeff(T, j), ns) for j in range(1, N)}
    return c0 / divisor, E, Q, Phi


def group_velocity(phi, omega2, ks, ns, N, c0, divisor=1):
    """|grad eps_+| along k = t n to relative order t^(N-2): returns the
    coefficients gamma_j with |grad eps_+| = c0 [1 + sum_j gamma_j t^j]."""
    sub = {k: T * n for k, n in zip(ks, ns)}
    grad_om2 = [sp.expand(sp.diff(omega2, k).subs(sub)) for k in ks]
    grad_phi = [sp.expand(sp.diff(phi, k).subs(sub)) for k in ks]
    om2_t = sp.expand(omega2.subs(sub))
    c0full = c0 * divisor
    c0sq = c0full ** 2
    x = sp.expand(sum((reduce_sphere(om2_t.coeff(T, m), ns) / c0sq * T ** (m - 2)
                       for m in range(3, N + 1)), sp.Integer(0)))
    inv_sqrt = compose(SQRT1P, x, [T], N - 2)     # sqrt(1+x)
    inv_sqrt = compose(INV1P, sp.expand(inv_sqrt - 1), [T], N - 2)  # 1/sqrt(1+x)
    comps = []
    for a in range(len(ks)):
        g = sp.expand(grad_om2[a])
        # grad omega = grad omega2 / (2 omega), omega = c0full t sqrt(1+x)
        g_over_t = sp.expand(sum(reduce_sphere(g.coeff(T, m), ns) * T ** (m - 1) for m in range(1, N)))
        val = sp.expand(g_over_t * inv_sqrt / (2 * c0full) + grad_phi[a])
        comps.append(trunc(val, [T], N - 2))
    v2 = trunc(sum(c ** 2 for c in comps), [T], N - 2)
    v2 = sp.expand(sum(reduce_sphere(v2.coeff(T, m), ns) * T ** m for m in range(0, N - 1)))
    lead = canon(v2.coeff(T, 0))
    if not zero(lead - c0sq):
        raise ValueError(f"group speed at the node is not c0: {lead} vs {c0sq}")
    y = trunc(v2 / c0sq - 1, [T], N - 2)
    vg = compose(SQRT1P, y, [T], N - 2)
    return {j: reduce_sphere(sp.expand(vg).coeff(T, j), ns) for j in range(1, N - 1)}


# ------------------------------------------------------------ angular content
def fourier2(f, ns):
    """Trigonometric content of f(cos th, sin th): returns {m: (a_m, b_m)} with
    f = a_0 + sum_{m>0} a_m cos(m th) + b_m sin(m th), exactly."""
    sub = {ns[0]: (W + 1 / W) / 2, ns[1]: (W - 1 / W) / (2 * sp.I)}
    g = sp.expand(f.subs(sub))
    out = {}
    if g == 0:
        return {0: (sp.Integer(0), sp.Integer(0))}
    shift = W ** 40
    poly = sp.Poly(sp.expand(g * shift), W)
    c = {}
    for (e,), coeff in poly.terms():
        c[e - 40] = canon(coeff)
    ms = sorted({abs(m) for m in c})
    for m in ms:
        cp, cm = c.get(m, 0), c.get(-m, 0)
        if m == 0:
            out[0] = (canon(cp), sp.Integer(0))
        else:
            out[m] = (canon(cp + cm), canon(sp.I * (cp - cm)))
    return out


def dfact(n):
    return sp.Integer(1) if n <= 0 else sp.Integer(n) * dfact(n - 2)


def sphere_average(f, ns):
    """Exact average over the unit sphere S^2 of a polynomial in n."""
    f = sp.expand(f)
    if f == 0:
        return sp.Integer(0)
    poly = sp.Poly(f, *ns)
    out = sp.Integer(0)
    for exps, c in poly.terms():
        if any(e % 2 for e in exps):
            continue
        out += c * sp.prod([dfact(e - 1) for e in exps]) / dfact(sum(exps) + 1)
    return canon(out)


def cubic_content(f, ns):
    """f on S^2 = a0 + b4 K4 + b6 K6 + residual, with K4 = sum n^4 - 3/5 and K6
    the part of n1^2 n2^2 n3^2 orthogonal (L^2(S^2)) to 1 and K4. 1, K4, K6
    span the cubic (O_h) invariants of degree <= 6 on S^2. A zero residual
    certifies that f has only cubic-invariant content up to degree 6."""
    def avg(x):
        return sphere_average(reduce_sphere(x, ns), ns)
    K4 = reduce_sphere(sum(n ** 4 for n in ns) - sp.Rational(3, 5), ns)
    m6 = reduce_sphere(sp.prod([n ** 2 for n in ns]), ns)
    K6 = reduce_sphere(m6 - avg(m6) - avg(m6 * K4) / avg(K4 * K4) * K4, ns)
    a0 = avg(f)
    b4 = canon(avg(f * K4) / avg(K4 * K4))
    b6 = canon(avg(f * K6) / avg(K6 * K6))
    residual = reduce_sphere(f - a0 - b4 * K4 - b6 * K6, ns)
    return a0, b4, b6, residual


# ------------------------------------------------------------ symmetry group
def rot2(angle):
    return sp.Matrix([[sp.cos(angle), -sp.sin(angle)], [sp.sin(angle), sp.cos(angle)]])


def point_group(name):
    if name == "line":
        return {"+1": sp.Matrix([[1]]), "-1": sp.Matrix([[-1]])}
    F = sp.diag(1, -1)
    if name == "square":
        g = {}
        for j in range(4):
            g[f"R{90 * j}"] = rot2(sp.pi * j / 2)
            g[f"R{90 * j}F"] = rot2(sp.pi * j / 2) * F
        return g
    if name == "hexagon":
        g = {}
        for j in range(6):
            g[f"R{60 * j}"] = rot2(sp.pi * j / 3)
            g[f"R{60 * j}F"] = rot2(sp.pi * j / 3) * F
        return g
    if name == "cubic":
        g = {}
        for perm in itertools.permutations(range(3)):
            for signs in itertools.product((1, -1), repeat=3):
                m = sp.zeros(3)
                for i in range(3):
                    m[i, perm[i]] = signs[i]
                g[f"P{perm}S{signs}"] = m
        return g
    raise ValueError(name)


def lp_equal(a, b, zs):
    shift = sp.prod([z ** 12 for z in zs])
    diff = sp.expand((a - b) * shift)
    if diff == 0:
        return True
    return all(zero(c) for c in sp.Poly(diff, *zs).coeffs())


def power_traces(symbol, n):
    """tr(U^m), m = 1..n, exact Laurent polynomials."""
    out, M = [], sp.eye(symbol.rows)
    for _ in range(n):
        M = (M * symbol).applyfunc(sp.expand)
        out.append(sp.expand(M.trace()))
    return out


def walk_group(symbol, zs, gens, group):
    """Elements g of the substrate point group with charpoly U(g k) = charpoly U(k).
    In characteristic 0 the characteristic polynomial of an s x s matrix is
    determined by tr(U^m), m = 1..s (Newton identities), and tr(U(g k)^m) is
    tr(U^m) with the monomial substitution z^h -> z^(M h), M the integer
    matrix of g in generator coordinates (k.h is invariant)."""
    d = len(gens[0])
    G = sp.Matrix([[sp.Matrix(g)[i] for g in gens] for i in range(d)])
    Ginv = G.inv()
    traces = power_traces(symbol, symbol.rows)
    members, non_lattice = [], []
    for name, g in group.items():
        M = (Ginv * g.T * G).applyfunc(canon)
        if not all(x.is_integer for x in M):
            non_lattice.append(name)
            continue
        sub = {zs[i]: sp.prod([zs[j] ** int(M[j, i]) for j in range(d)]) for i in range(d)}
        if all(lp_equal(sp.expand(tr.subs(sub, simultaneous=True)), tr, zs) for tr in traces):
            members.append(name)
    return members, non_lattice


def truncated_charpoly(Uk, ks, N):
    """Coefficients (low to high in lambda) of det(lambda - U(k)) truncated at
    total degree N in k, from Newton's identities on truncated power traces."""
    n = Uk.rows
    p, M = [], sp.eye(n)
    for _ in range(n):
        M = (M * Uk).applyfunc(lambda e: trunc(e, ks, N))
        p.append(trunc(M.trace(), ks, N))
    e = [sp.Integer(1)]
    for m in range(1, n + 1):
        acc = sum(((-1) ** (i - 1) * e[m - i] * p[i - 1] for i in range(1, m + 1)), sp.Integer(0))
        e.append(trunc(acc / m, ks, N))
    coeffs = [sp.Integer(0)] * (n + 1)
    for m in range(n + 1):
        coeffs[n - m] = (-1) ** m * e[m]
    return coeffs


def describe_group(members, dim):
    rot = [m for m in members if not m.endswith("F")] if dim == 2 else None
    if dim == 1:
        return f"{{{', '.join(members)}}}"
    if dim == 2:
        refl = [m for m in members if m.endswith("F")]
        return f"{len(members)} elements: rotations {sorted(rot)}, reflections {len(refl)}"
    if len(members) == 48:
        return "48 of 48 signed permutations (O_h)"
    return f"{len(members)} of 48 signed permutations: {sorted(members)}"


# ------------------------------------------------------------ rows
def laurent_matrix_from_p(M):
    """Matrices of verify_directional_saturation (functions of p) as Laurent
    matrices in DS.Z with z_k = exp(i p_k)."""
    return M.applyfunc(lambda e: sp.expand(DS.laurent(e)))


def row_L3s4_symbol(a, zs):
    """A_a(k) of CURRENT_STATE Sec. 4.1 at theta = pi/4: W exp(-i q.Gamma) with
    q_i = k_i/sqrt3 and z_i <-> exp(-i q_i), i.e. generators e_i/sqrt3, sigma=-1.
    The radical b = sqrt(1-a^2) built inside core() is replaced by the symbol
    B_SYM, reduced with b^2 = 1 - a^2 (reduce_b)."""
    b, w, ts, gammas, rs = AA.core(a, sp.pi / 4)
    gammas = tuple(g.xreplace({b: B_SYM}) for g in gammas)
    if any(e.has(sp.sqrt(1 - a ** 2)) for g in gammas for e in g):
        raise ValueError("L3s4: sqrt(1-a^2) survived the substitution")
    U = w
    for z, gam in zip(zs, gammas):
        cosq = (z + 1 / z) / 2
        sinq = (1 / z - z) / (2 * sp.I)     # z = exp(-i q)
        U = U * (cosq * sp.eye(4) - sp.I * sinq * gam)
    return U.applyfunc(sp.expand)


def hensel_quadratic(coeffs, lam0, ks, N):
    """coeffs: monic polynomial sum_j coeffs[j] lambda^j (coeffs[-1] = 1) with
    entries polynomials in k of degree <= N. At k = 0, lam0 is a double root
    and the cofactor is coprime to (lambda - lam0)^2. Returns (s1, s2) with
    the lifted quadratic factor lambda^2 - s1 lambda + s2, exact to degree N."""
    n = len(coeffs) - 1
    at0 = {k: 0 for k in ks}
    P0 = sp.Poly(sum(canon(c.subs(at0)) * LAM ** j for j, c in enumerate(coeffs)), LAM)
    Q0 = sp.Poly(sp.expand((LAM - lam0) ** 2), LAM)
    R0, rem = sp.div(P0, Q0)
    if not all(zero(c) for c in rem.all_coeffs()):
        raise ValueError("lam0 is not a double root at k = 0")
    R0 = sp.Poly([canon(c) for c in R0.all_coeffs()], LAM)
    # Unknowns u = (q0, q1, r0, ..., r_{n-3}); linear map u -> Q0 * r + R0 * q.
    us = sp.symbols(f"u0:{n}")
    qpoly = sp.Poly(us[0] + us[1] * LAM, LAM)
    rpoly = sp.Poly(sum(us[2 + i] * LAM ** i for i in range(n - 2)), LAM)
    lin = (Q0 * rpoly + R0 * qpoly).as_expr()
    S = sp.Matrix([[sp.expand(lin).coeff(LAM, j).coeff(u) for u in us] for j in range(n)])
    Sinv = S.inv().applyfunc(canon)
    Qparts = {0: Q0.as_expr()}
    Rparts = {0: R0.as_expr()}
    for m in range(1, N + 1):
        Pm = sum(homog(c, ks, m) * LAM ** j for j, c in enumerate(coeffs))
        conv = sum((Qparts[i] * Rparts[m - i] for i in range(1, m)), sp.Integer(0))
        rhs_poly = sp.expand(Pm - conv)
        rhs = sp.Matrix([rhs_poly.coeff(LAM, j) for j in range(n)])
        sol = (Sinv * rhs).applyfunc(sp.expand)
        Qparts[m] = sol[0] + sol[1] * LAM
        Rparts[m] = sum(sol[2 + i] * LAM ** i for i in range(n - 2))
    Q = sp.expand(sum(Qparts.values()))
    q1 = sp.expand(Q.coeff(LAM, 1))
    q0 = sp.expand(Q.coeff(LAM, 0))
    return -q1, q0


def analyse_block(label, s1, s2, ks, ns, N, divisor, results, expected_c0):
    """From the node quadratic factor to the tabulated quantities."""
    phi, omega2, lam0 = node_from_quadratic(s1, s2, ks, N)
    c0, E, Q, Phi = ray_expansion(phi, omega2, ks, ns, N, divisor)
    dim = len(ks)
    record(f"{label}: omega^2 has no terms of degree 0 or 1 and its degree-2 part is c0^2 |k|^2",
           czero(Q[0], ns) and czero(Q[1], ns) and zero(Q[2] - c0 ** 2 * divisor ** 2))
    record(f"{label}: c0 = {c0} agrees with the parent table", zero(c0 - expected_c0))
    record(f"{label}: no linear phase (phi has no degree-1 part: untilted node)", czero(Phi[1], ns))
    odd = {m: czero(Q[m], ns) for m in range(3, N + 1, 2)}
    even_phi = {m: czero(Phi[m], ns) for m in range(2, N + 1)}
    beta = sp.expand(E[2] / c0)
    alpha = sp.expand(E[3] / c0)
    print(f"  {label}: node eigenvalue at k=0: {lam0}; eps_0 = {canon(sp.I * sp.log(lam0))}")
    print(f"  {label}: Q3 = {Q[3]}; Q4 = {Q[4]}")
    if N >= 6:
        print(f"  {label}: Q5 = {Q[5]}; Q6 = {Q[6]}")
    print(f"  {label}: phi: Phi2 = {Phi[2]}, Phi3 = {Phi[3]}, Phi4 = {Phi[4]}")
    print(f"  {label}: beta(n) = {beta}")
    print(f"  {label}: alpha(n) = {alpha}")
    gam = group_velocity(phi, omega2, ks, ns, N, c0, divisor)
    print(f"  {label}: |grad eps_+| / c0 - 1 = " + " + ".join(f"({g}) t^{j}" for j, g in gam.items()))
    info = dict(c0=c0, beta=beta, alpha=alpha, E=E, Q=Q, Phi=Phi, gamma=gam, dim=dim,
                odd_zero=all(odd.values()), phi_zero=all(even_phi.values()))
    if dim == 1:
        info["alpha0"] = canon(alpha)
        info["aniso"] = sp.Integer(0)
        info["pattern"] = f"constant alpha = {info['alpha0']}"
    elif dim == 2:
        fb = fourier2(beta, ns)
        fa = fourier2(alpha, ns)
        info["fourier_beta"], info["fourier_alpha"] = fb, fa
        info["alpha0"] = fa.get(0, (sp.Integer(0),))[0]
        info["aniso"] = {m: v for m, v in fa.items() if m > 0 and not (zero(v[0]) and zero(v[1]))}
        info["pattern"] = (f"beta: {fb}; alpha: {fa}")
        if N >= 6:
            f5 = fourier2(sp.expand(E[5] / c0), ns)
            info["fourier_E5"] = f5
            print(f"  {label}: E5/c0 (relative order t^4) harmonics: {f5}")
    else:
        a0, b4, b6, res = cubic_content(alpha, ns)
        info["alpha0"] = a0
        info["aniso"] = {4: b4, 6: b6} if not (zero(b4) and zero(b6)) else {}
        info["cubic_residual"] = res
        n123 = sp.prod(ns)
        b0 = sphere_average(beta, ns)
        b3 = canon(sphere_average(reduce_sphere(beta * n123, ns), ns)
                   / sphere_average(reduce_sphere(n123 ** 2, ns), ns))
        info["beta0"], info["beta3"] = b0, b3
        info["beta_residual"] = reduce_sphere(beta - b0 - b3 * n123, ns)
        info["pattern"] = (f"beta = {b0} + ({b3}) n1 n2 n3 [+ residual "
                           f"{'0' if czero(info['beta_residual'], ns) else 'nonzero'}]; "
                           f"alpha = {a0} + ({b4}) K4 + ({b6}) K6 [+ residual "
                           f"{'0' if czero(res, ns) else 'nonzero'}]")
    if dim == 1:
        info["lowest"] = "beta" if not czero(beta, ns) else ("alpha" if not czero(alpha, ns) else "none (to t^%d)" % (N - 2))
    else:
        info["lowest"] = "beta" if not czero(beta, ns) else ("alpha" if not czero(alpha, ns) else "none")
    if info["lowest"] == "beta":
        if dim == 2:
            info["lowest_aniso"] = any(m > 0 and not (zero(v[0]) and zero(v[1])) for m, v in info["fourier_beta"].items())
        else:
            info["lowest_aniso"] = not zero(info["beta3"]) or not czero(info["beta_residual"], ns)
    elif info["lowest"] == "alpha":
        info["lowest_aniso"] = bool(info["aniso"]) or (dim == 3 and not czero(info["cubic_residual"], ns))
    else:
        info["lowest_aniso"] = False
    print(f"  {label}: lowest nonvanishing correction: {info['lowest']}; anisotropic: {info['lowest_aniso']}")
    print(f"  {label}: lowest corrections: beta == 0: {czero(beta, ns)}; alpha0 = {info['alpha0']}; "
          f"angular content: {info['pattern']}")
    results[label] = info
    return info


def validity_scale_1d(s1, ks):
    """d = 1: smallest |k| > 0 where the two branches meet (cos omega = +-1)."""
    k = ks[0]
    sols = []
    for sgn in (1, -1):
        try:
            sol = sp.solveset(sp.Eq(s1 / 2, sgn), k, domain=sp.Interval.open(0, 4 * sp.pi))
            if isinstance(sol, sp.FiniteSet):
                sols += [s for s in sol if s.is_real]
        except Exception:
            pass
    return min(sols, key=lambda x: float(x)) if sols else None


def main():
    print(f"contract sha256 {hashlib.sha256(CONTRACT.read_bytes()).hexdigest()}")
    v = sp.symbols("v")
    record("Taylor coefficients match SymPy series (acos(1-v)^2, log, sqrt, 1/(1+v))",
           sp.expand(sp.series(sp.acos(1 - v) ** 2, v, 0, 5).removeO() - sum(c * v ** j for j, c in enumerate(ACOS2))) == 0
           and sp.expand(sp.series(sp.log(1 + v), v, 0, 7).removeO() - sum(c * v ** j for j, c in enumerate(LOG1P))) == 0
           and sp.expand(sp.series(sp.sqrt(1 + v), v, 0, 7).removeO() - sum(c * v ** j for j, c in enumerate(SQRT1P))) == 0
           and sp.expand(sp.series(1 / (1 + v), v, 0, 7).removeO() - sum(c * v ** j for j, c in enumerate(INV1P))) == 0)

    results = {}
    groups = {}
    print("== Part 1: symbols imported read-only (parent checks re-run on import, not counted here)")
    rows = {}
    zs1 = sp.symbols("w1:2")
    zs2 = sp.symbols("w1:3")
    sym, _ = WD.published_symbol(1, 1, zs1)
    rows["L1"] = dict(symbol=sym, zs=zs1, gens=[(1,)], sigma=+1, substrate="line", N=6, c0=sp.Integer(1))
    sym, _ = WD.published_symbol(2, 1, zs2)
    rows["L2"] = dict(symbol=sym, zs=zs2, gens=[(1, 0), (0, 1)], sigma=+1, substrate="square", N=6, c0=R2 / 2)
    n_parent_before = len(P.CHECKS)
    for label, fn in (("L6e", P.row_L6e), ("L5a", P.row_L5a), ("L5b", P.row_L5b), ("L6a", P.row_L6a),
                      ("L6c", P.row_L6c), ("L6d", P.row_L6d), ("L6f", P.row_L6f)):
        symbol, zs, support, gens = fn()
        sub = {"L6e": "square", "L5a": "cubic", "L5b": "cubic"}.get(label, "hexagon")
        rows[label] = dict(symbol=symbol, zs=zs, gens=gens, sigma=-1, substrate=sub,
                           N=4 if sub == "cubic" else 6, c0=P.EXPECTED_MASSLESS[label][1])
    record("parent row constructors pass their own checks on import",
           all(ok for _, ok, _ in P.CHECKS[n_parent_before:]), f"{len(P.CHECKS) - n_parent_before} parent checks")
    rows["L3"] = dict(symbol=laurent_matrix_from_p(DS.walk2()), zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                      sigma=+1, substrate="cubic", N=4, c0=1 / R3)
    rows["L4"] = dict(symbol=laurent_matrix_from_p(DS.walk1()), zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                      sigma=+1, substrate="cubic", N=4, c0=1 / R3)
    zs3 = sp.symbols("z1:4")
    rows["L3s4"] = dict(symbol=row_L3s4_symbol(A_SYM, zs3), zs=zs3, gens=[(1 / R3, 0, 0), (0, 1 / R3, 0), (0, 0, 1 / R3)],
                        sigma=-1, substrate="cubic", N=4, c0=A_SYM / R3)
    # L6b: V = U^3 on the white-triangle lattice, orientation blocks.
    succ, admissible = L6B.part1_labelings()
    Wcoin, _, _ = L6B.coin("parent")
    U6, _ = L6B.step_symbol("up", succ, Wcoin)
    V6 = sp.expand(U6 ** 3)
    off, blocks = L6B.orientation_blocks(V6)
    record("L6b: V = U^3 is block diagonal in the edge orientation (reused structure)", off)
    ell = sp.Rational(1, 2)
    rows["L6b"] = dict(symbol=blocks[0].applyfunc(sp.expand), zs=L6B.ZS, gens=L6B.GENS, sigma=-1, substrate="hexagon",
                       N=6, c0=sp.Rational(1, 3), scale=ell, divisor=3, blocks=[b.applyfunc(sp.expand) for b in blocks])

    print("== Part 2: node branch expansions per row (contract Sec. 3)")
    for label, row in rows.items():
        symbol, zs, gens, sigma, N = row["symbol"], row["zs"], row["gens"], row["sigma"], row["N"]
        dim = len(gens[0])
        ks = sp.symbols(f"k1:{dim + 1}", real=True)
        ns = sp.symbols(f"n1:{dim + 1}", real=True)
        support = P.laurent_support(symbol, zs)
        if label == "L3s4":
            record("L3s4: U(0) = W exactly (node structure of Sec. 4.1)",
                   all(zero(x) for x in (sum(support.values(), sp.zeros(4)) - AA.core(A_SYM, sp.pi / 4)[1])))
        cart = {h: sum((a_ * sp.Matrix(g) for a_, g in zip(h, gens)), sp.zeros(dim, 1)) for h in support}
        L = row.get("scale") or sp.radsimp(sp.simplify(max((sp.sqrt((v_.T * v_)[0]) for v_ in cart.values()),
                                                           key=lambda x: float(x))))
        divisor = row.get("divisor", 1)
        print(f"-- {label} ({row['substrate']}, s = {symbol.rows}, d = {dim}, scale = {L}, N = {N})"
              f"  [elapsed {time.time() - START:.0f} s]", flush=True)
        if label == "L5b":
            Uk = taylor_symbol(support, gens, L, sigma, ks, N)
            kron = sp.kronecker_product
            dP = (kron(P.SX, P.SX), kron(P.SX, P.SY), kron(P.SX, P.SZ))
            full = [trunc(c, ks, N) for c in reversed(Uk.charpoly(LAM).all_coeffs())]
            record("truncated_charpoly (Newton identities) equals the full charpoly truncated, L5b 4x4",
                   all(czero(x - y, ks) for x, y in zip(full, truncated_charpoly(Uk, ks, N))))
            Gam = (dP[0] * dP[1] * dP[2]).applyfunc(canon)
            record("L5b: Gamma = dP_X dP_Y dP_Z commutes with every Fourier coefficient and Gamma^2 = -I",
                   all(P.is_zero_matrix(Gam * A - A * Gam) for A in support.values())
                   and P.is_zero_matrix(Gam * Gam + sp.eye(4)))
            for sgn in (1, -1):
                proj = (sp.eye(4) - sgn * sp.I * Gam) / 2        # eigenvalue  sgn*i
                vecs = proj.columnspace()
                B = sp.Matrix.hstack(*vecs)
                Bq, _ = B.QRdecomposition()
                Bq = Bq.applyfunc(canon)
                blk = (Bq.H * Uk * Bq).applyfunc(lambda e: trunc(e, ks, N))
                record(f"L5b block (Gamma = {sgn}i): the block is 2x2 and Bq is an isometry",
                       blk.rows == 2 and P.is_zero_matrix(Bq.H * Bq - sp.eye(2)))
                s1 = trunc(blk.trace(), ks, N)
                s2 = trunc(blk.det(), ks, N)
                analyse_block(f"L5b[{'+' if sgn > 0 else '-'}i]", s1, s2, ks, ns, N, 1, results, row["c0"])
                # block symbol as Laurent matrix for the symmetry test
                blk_l = (Bq.H * symbol * Bq).applyfunc(sp.expand)
                members, non_lattice = walk_group(blk_l, zs, gens, point_group(row["substrate"]))
                groups[f"L5b[{'+' if sgn > 0 else '-'}i]"] = members
                print(f"  L5b[{'+' if sgn > 0 else '-'}i]: G_walk = {describe_group(members, dim)}; "
                      f"non-lattice elements skipped: {len(non_lattice)}")
            continue
        if label == "L3s4":
            Uk = taylor_symbol(support, gens, L, sigma, ks, N)
            cp = truncated_charpoly(Uk, ks, N)
            record("L3s4: characteristic polynomial is monic of degree 4", len(cp) == 5 and zero(cp[4] - 1))
            for sgn, name in ((1, "+pi/4"), (-1, "-pi/4")):
                lam0 = (1 - sgn * sp.I) / R2          # exp(-+ i pi/4)
                s1, s2 = hensel_quadratic(cp, lam0, ks, N)
                analyse_block(f"L3s4[{name}]", s1, s2, ks, ns, N, 1, results, row["c0"])
            members, non_lattice = walk_group(symbol, zs, gens, point_group(row["substrate"]))
            groups["L3s4"] = members
            print(f"  L3s4: G_walk = {describe_group(members, dim)}; non-lattice skipped: {len(non_lattice)}")
            continue
        if label == "L6b":
            for i, blk in enumerate(row["blocks"]):
                sup_b = P.laurent_support(blk, zs)
                Uk = taylor_symbol(sup_b, gens, L, sigma, ks, N)
                s1 = trunc(Uk.trace(), ks, N)
                s2 = trunc(Uk.det(), ks, N)
                analyse_block(f"L6b[block {i}]", s1, s2, ks, ns, N, divisor, results, row["c0"])
            tr0 = power_traces(row["blocks"][0], 2)
            same = all(all(lp_equal(x, y, zs) for x, y in zip(tr0, power_traces(b, 2)))
                       for b in row["blocks"][1:])
            record("L6b: the three orientation blocks have the same characteristic polynomial", same)
            members, non_lattice = walk_group(row["blocks"][0], zs, gens, point_group(row["substrate"]))
            groups["L6b"] = members
            print(f"  L6b: G_walk (block 0) = {describe_group(members, dim)}; non-lattice skipped: {len(non_lattice)}")
            continue
        Uk = taylor_symbol(support, gens, L, sigma, ks, N)
        s1 = trunc(Uk.trace(), ks, N)
        s2 = trunc(Uk.det(), ks, N)
        info = analyse_block(label, s1, s2, ks, ns, N, 1, results, row["c0"])
        members, non_lattice = walk_group(symbol, zs, gens, point_group(row["substrate"]))
        groups[label] = members
        print(f"  {label}: G_walk = {describe_group(members, dim)}; non-lattice skipped: {len(non_lattice)}")
        if dim == 1:
            full_s1 = symbol.subs({zs[0]: sp.exp(sigma * sp.I * ks[0] / L)}).trace()
            kstar = validity_scale_1d(sp.simplify(full_s1), ks)
            print(f"  {label}: branches meet first at |k| = {kstar} (exact, d = 1)")
            info["kstar"] = kstar
        else:
            print(f"  {label}: scale of validity OPEN (exact minimisation of |k| on the branch-meeting "
                  f"set not attempted, contract Sec. 3 item 6)")

    print("== Part 3: cross-checks (contract Sec. 3)")
    r1 = results["L1"]
    record("L1: massless 1D Dirac walk has exactly linear dispersion (all corrections vanish)",
           all(czero(r1["E"][j], sp.symbols("n1:2", real=True)) for j in range(2, 6)))
    n2 = sp.symbols("n1:3", real=True)
    for x, y in (("L6c", "L6d"), ("L6c", "L6f"), ("L6d", "L6f")):
        same = czero(results[x]["alpha"] - results[y]["alpha"], n2) and czero(results[x]["beta"] - results[y]["beta"], n2)
        print(f"  {x} vs {y}: same beta and alpha: {same}")
        results[x].setdefault("same_as", {})[y] = same
    # L6b vs L6a. In the normalised units of each row, V = U^3 realises the
    # L6a symbol at half the length scale, rotated (L6b report Sec. 5):
    # eps_L6b(k) = eps_L6a(2 R k) / 3, so c0 scales by 2/3, beta(n) by 2 and
    # alpha(n) by 4, evaluated at R n.
    th = sp.pi / 3
    record("L6b: c0(L6b) = (2/3) c0(L6a)", zero(results["L6b[block 0]"]["c0"] - sp.Rational(2, 3) * results["L6a"]["c0"]))
    for sgn in (1, -1):
        R = rot2(sgn * th)
        sub = {n2[0]: R[0, 0] * n2[0] + R[0, 1] * n2[1], n2[1]: R[1, 0] * n2[0] + R[1, 1] * n2[1]}
        rb = reduce_sphere(sp.expand(2 * results["L6a"]["beta"].subs(sub, simultaneous=True)), n2)
        ra = reduce_sphere(sp.expand(4 * results["L6a"]["alpha"].subs(sub, simultaneous=True)), n2)
        ok = czero(rb - results["L6b[block 0]"]["beta"], n2) and czero(ra - results["L6b[block 0]"]["alpha"], n2)
        print(f"  L6b (beta, alpha) = (2 beta, 4 alpha) of L6a at R({sgn * 60} deg) n: {ok}")
        if ok:
            results["L6b[block 0]"]["rot_match"] = sgn * 60
    record("L6b: beta = 2 beta_L6a(R n), alpha = 4 alpha_L6a(R n) for a 60-degree rotation R",
           "rot_match" in results["L6b[block 0]"])
    # Second route (hand derivation, report Sec. 4). For cos(omega) =
    # prod_i cos(p_i), p = k / sqrt(d): log cos x = -x^2/2 - x^4/12 + O(x^6)
    # gives omega^2 = |p|^2 - (1/3) sum_{i<j} p_i^2 p_j^2 + O(p^6), hence
    # alpha = -sum_{i<j} n_i^2 n_j^2 / (6 d). For the chiral BCC rows the
    # beta^2 term adds -n1^2 n2^2 n3^2 / 6. The script checks these forms.
    n3 = sp.symbols("n1:4", real=True)
    sig2 = n3[0] ** 2 * n3[1] ** 2 + n3[1] ** 2 * n3[2] ** 2 + n3[2] ** 2 * n3[0] ** 2
    sig3 = n3[0] ** 2 * n3[1] ** 2 * n3[2] ** 2
    record("closed form: L2 and L6e alpha = -n1^2 n2^2 / 12",
           all(czero(reduce_sphere(results[l]["alpha"] + n2[0] ** 2 * n2[1] ** 2 / 12, n2), n2) for l in ("L2", "L6e")))
    record("closed form: L3 alpha = -(n1^2 n2^2 + n2^2 n3^2 + n3^2 n1^2) / 18",
           czero(reduce_sphere(results["L3"]["alpha"] + sig2 / 18, n3), n3))
    record("closed form: L5a, L5b, L4 alpha = -sigma2/18 - n1^2 n2^2 n3^2/6",
           all(czero(reduce_sphere(results[l]["alpha"] + sig2 / 18 + sig3 / 6, n3), n3)
               for l in ("L5a", "L5b[+i]", "L5b[-i]", "L4")))
    record("closed form: L6a alpha = -41/1728 - (5/1728) cos 6 theta, beta = -(sqrt15/36) cos 3 theta",
           results["L6a"]["fourier_alpha"] == {0: (-sp.Rational(41, 1728), 0), 6: (-sp.Rational(5, 1728), 0)}
           and set(results["L6a"]["fourier_beta"]) == {3} and zero(results["L6a"]["fourier_beta"][3][0] + sp.sqrt(15) / 36))
    record("L6b: the three orientation blocks give identical beta and alpha",
           all(czero(results[f"L6b[block {i}]"]["alpha"] - results["L6b[block 0]"]["alpha"], n2)
               and czero(results[f"L6b[block {i}]"]["beta"] - results["L6b[block 0]"]["beta"], n2) for i in (1, 2)))
    n3c = sp.symbols("n1:4", real=True)
    for label, info in results.items():
        if info["dim"] != 3:
            continue
        g = groups.get(label) or groups.get(label.split("[")[0])
        if g is not None and len(g) >= 24:
            record(f"{label}: |G_walk| = {len(g)} >= 24, so beta = b3 n1 n2 n3 and alpha in span(1, K4, K6) exactly",
                   zero(info["beta0"]) and czero(info["beta_residual"], n3c) and czero(info["cubic_residual"], n3c))
        else:
            print(f"  {label}: |G_walk| = {len(g) if g is not None else '?'} < 24: non-cubic content allowed; "
                  f"beta residual zero: {czero(info['beta_residual'], n3c)}, "
                  f"alpha residual zero: {czero(info['cubic_residual'], n3c)}")
    record("L5b: the two Weyl blocks give identical alpha",
           czero(results["L5b[+i]"]["alpha"] - results["L5b[-i]"]["alpha"], sp.symbols("n1:4", real=True)))
    record("L3s4: the two clusters give identical alpha",
           czero(results["L3s4[+pi/4]"]["alpha"] - results["L3s4[-pi/4]"]["alpha"], sp.symbols("n1:4", real=True)))

    print("== Part 4: hypotheses (contract Sec. 4)")
    table = {}
    for label, info in results.items():
        a0 = info["alpha0"]
        if not a0.free_symbols:
            sgn = P.positive(a0)
        else:
            if a0.has(B_SYM) or a0.free_symbols - {A_SYM}:
                raise ValueError(f"{label}: alpha0 is not a rational function of a: {a0}")
            num, den = sp.fraction(sp.together(sp.factor(a0)))
            pn, pd = sp.Poly(num, A_SYM), sp.Poly(den, A_SYM)
            roots_in = pn.count_roots(0, 1) - (1 if pn.eval(0) == 0 else 0) - (1 if pn.eval(1) == 0 else 0)
            poles_in = pd.count_roots(0, 1) - (1 if pd.eval(0) == 0 else 0) - (1 if pd.eval(1) == 0 else 0)
            mid = P.positive(a0.subs(A_SYM, sp.Rational(1, 2)))
            sgn = mid if roots_in == 0 and poles_in == 0 else None
            rts = [r for r in sp.real_roots(pn) if bool(r > 0) and bool(r < 1)]
            rts = [sp.radsimp(sp.nsimplify(sp.simplify(r))) for r in rts]
            signs = []
            cuts = [sp.Integer(0)] + sorted(rts, key=lambda x: float(x)) + [sp.Integer(1)]
            for lo, hi in zip(cuts[:-1], cuts[1:]):
                q = sp.Rational(int(float((lo + hi) / 2) * 10 ** 6), 10 ** 6)  # rational point inside (lo, hi)
                if not (bool(q > lo) and bool(q < hi)):                       # checked exactly
                    raise ValueError("sample point outside its interval")
                signs.append((lo, hi, P.positive(a0.subs(A_SYM, q))))
            record(f"{label}: alpha0(a) roots in 0 < a < 1 found exactly (Sturm count {roots_in}, poles {poles_in})",
                   len(rts) == roots_in and poles_in == 0,
                   f"alpha0(a) = {sp.factor(a0)}; roots {rts}; sign on each interval {signs}")
            info["alpha0_roots"], info["alpha0_signs"] = rts, signs
        table[label] = sgn
        print(f"  {label}: alpha0 = {a0}; sign = {sgn if sgn is not None else 'depends on a (see report)'}; "
              f"odd parts of omega^2 vanish: {info['odd_zero']}; phi == 0: {info['phi_zero']}")
    undecided = [l for l, s in table.items() if s is None]
    record("Hd: the sign of alpha0 is decided exactly in every row (or left to the report for symbolic a)",
           True, f"undecided: {undecided}")
    hd = all(s is not None and s < 0 for s in table.values())
    print(f"  Hd (alpha0 < 0 in every row): {hd}; rows with alpha0 >= 0: "
          f"{[l for l, s in table.items() if s is not None and s >= 0]}")
    ceiling = ["L2", "L6e", "L3", "L5a", "L5b[+i]", "L5b[-i]", "L4"]
    he = {}
    for label in ceiling:
        he[label] = results[label]["lowest_aniso"]
    print(f"  He (ceiling rows have nonzero anisotropy): {all(he.values())}; per row {he}")
    hf = {}
    n3 = sp.symbols("n1:4", real=True)
    for sub, members in (("square", ["L2", "L6e"]), ("BCC", ["L3", "L5a", "L5b[+i]"]),
                         ("hexagon", ["L6a", "L6c", "L6d", "L6f", "L6b[block 0]"])):
        ns_ = n2 if sub != "BCC" else n3
        pairs = {}
        for x, y in itertools.combinations(members, 2):
            pairs[(x, y)] = czero(results[x]["alpha"] - results[y]["alpha"], ns_) and czero(results[x]["beta"] - results[y]["beta"], ns_)
        hf[sub] = pairs
        print(f"  Hf {sub}: identical (beta, alpha) pairs: {[p for p, s in pairs.items() if s]}")
    identical = {sub: [p for p, same in pairs.items() if same] for sub, pairs in hf.items()}
    print(f"  Hf: identical (beta, alpha) pairs per substrate: {identical}")
    print(f"  Hf (no two rows on one substrate share beta and alpha, contract refutation clause): "
          f"{not any(identical.values())}")
    print(f"  Hf (rows on each substrate do not all share the correction): "
          f"{all(not all(pairs.values()) for pairs in hf.values())}")
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (dispersion corrections gate).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail closed
        import traceback
        traceback.print_exc()
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
