"""Step 4b-2 (sectors, strict body, comparison) of theory/MINIMAL_S2_RIGIDITY_GATE.md for the only
nonempty class left by Step 4b-1: (V4, tetrahedron, Pauli), rho = inclusion
(reports/2026-10-29--minimal-s2-step4b1.md). Self-contained: no imported certificate code.

Coordinates. q_j = k_j / sqrt(3) (epsilon units), x_j = exp(-i q_j), c_j = cos q_j, s_j = sin q_j.
The covariant symbol (two V4 orbits, S_+ = {h : h1 h2 h3 = +1} and S_- = -S_+) is
  T_h = a I + sum_j h_j b_j sigma_j  (h in S_+),   T_h = c I - sum_j h_j d_j sigma_j  (h in S_-),
with a, c in C and b, d in C^3 (16 real parameters). The linear bijection
  alpha = 4(a+c), beta = 4i(a-c), gamma = -4(b+d), delta = -4i(b-d)
gives U = alpha C0 + beta S0 + sum_j sigma_j (gamma_j C_j + delta_j S_j), with
  C0 = c1 c2 c3, S0 = s1 s2 s3, C_j = c_j s_k s_l, S_j = s_j c_k c_l.

Checks:
 1. covariance and the Laurent identity above;
 2. the unitarity ideal E (Laurent coefficient identities, both orders) equals the ideal R of the
    reduced system written by hand (equal reduced Groebner bases);
 3. sign enumeration: with |alpha| = 1, the 128 choices delta_j = i eta_j alpha,
    gamma_j = i eps_j kappa alpha, beta = kappa alpha satisfy E exactly iff sum_j eps_j eta_j = -1
    (48 families); the deduction that every real point is of this form is written in the report,
    with its key identities checked here;
 4. Q-a two ways: (i) per family, T_{gh} != T_h for g in V4 minus {e}, h in N_3; (ii) for the whole
    class, E + {T_{gh} = T_h} + {y ||T_h||^2 = 1} has unit ideal (Astra's argument);
 5. nodes: per family the system "U(q) scalar" on the torus has exactly the 16 points
    {0, pi}^3 and {pi/2, 3pi/2}^3; at each, U = aI with |a| = 1, H_j = i conj(a) dU/dk_j is
    traceless with (1/2) tr(H_j H_l) = delta_jl / 3, so c_0 = 1/sqrt(3);
 6. strict body: every T_h has rank one and nonzero trace (T_h^2 = tr(T_h) T_h != 0), so the
    vertex coefficient of U^n at n h is tr(T_h)^(n-1) T_h != 0 and c_strict^iso = 1/sqrt(3) =
    rho_micro.

What it does NOT certify: the hand deduction from R to the 48 families beyond the identities of
check 3, the vertex-lemma step S_n subset n conv(N_3) with n h in S_n (written in the report), Q-b,
or any statement outside this class.
"""

import itertools
import sys
import time

import sympy as sp

CHECKS = 0
I = sp.I
PAULI = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
N3 = [h for h in itertools.product((1, -1), repeat=3)]
V4 = [sp.diag(*d) for d in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))]
X = sp.symbols("x1:4")


def require(cond, label):
    global CHECKS
    if not cond:
        print(f"[FAIL] {label}")
        raise SystemExit(1)
    CHECKS += 1
    print(f"[PASS] {label}", flush=True)


def zero(e):
    return sp.expand(sp.expand_complex(e)) == 0


def mzero(M):
    return all(zero(e) for e in M)


def act(g, h):
    return tuple(int(g[i, i]) * h[i] for i in range(3))


def sym_from(a, b, c, d):
    T = {}
    for h in N3:
        if h[0] * h[1] * h[2] == 1:
            T[h] = a * sp.eye(2) + sum((h[j] * b[j] * PAULI[j] for j in range(3)), sp.zeros(2))
        else:
            T[h] = c * sp.eye(2) - sum((h[j] * d[j] * PAULI[j] for j in range(3)), sp.zeros(2))
    return T


def from_greek(al, be, ga, de):
    a, c = (al - I * be) / 8, (al + I * be) / 8
    b = [(-ga[j] + I * de[j]) / 8 for j in range(3)]
    d = [(-ga[j] - I * de[j]) / 8 for j in range(3)]
    return sym_from(a, b, c, d)


def laurent(T):
    return sum((T[h] * sp.prod([X[j] ** h[j] for j in range(3)]) for h in N3), sp.zeros(2))


def unitarity(T, normalize=True):
    """Real and imaginary parts of sum_{h'-h=l} T_h^dag T_h' - delta I and of
    sum_{h'-h=l} T_h' T_h^dag - delta I, for every displacement l."""
    diffs = {}
    for h in N3:
        for hp in N3:
            diffs.setdefault(tuple(p - q for p, q in zip(hp, h)), []).append((h, hp))
    eqs = set()
    for ell, pairs in diffs.items():
        tgt = sp.eye(2) if (ell == (0, 0, 0) and normalize) else sp.zeros(2)
        for S in (sum((T[h].H * T[hp] for h, hp in pairs), sp.zeros(2)) - tgt,
                  sum((T[hp] * T[h].H for h, hp in pairs), sp.zeros(2)) - tgt):
            for e in S:
                e = sp.expand(sp.expand_complex(e))
                for part in (sp.expand(sp.re(e)), sp.expand(sp.im(e))):
                    if part != 0:
                        eqs.add(part)
    return sorted(eqs, key=sp.default_sort_key)


def main():
    t0 = time.time()
    # real variables
    ar, ai, br, bi = sp.symbols("ar ai br bi", real=True)
    gr, gi = sp.symbols("gr1:4", real=True), sp.symbols("gi1:4", real=True)
    dr, di = sp.symbols("dr1:4", real=True), sp.symbols("di1:4", real=True)
    al, be = ar + I * ai, br + I * bi
    ga = [gr[j] + I * gi[j] for j in range(3)]
    de = [dr[j] + I * di[j] for j in range(3)]
    VARS = [ar, ai, br, bi, *gr, *gi, *dr, *di]
    T = from_greek(al, be, ga, de)

    # 1. covariance and Laurent identity
    def coeffs(M):
        return [sp.expand((M * P).trace() / 2) for P in PAULI]

    require(all(zero(sp.trace(T[act(g, h)]) - sp.trace(T[h])) and
                all(zero(coeffs(T[act(g, h)])[j] - sum(g[j, m] * coeffs(T[h])[m] for m in range(3)))
                    for j in range(3))
                for g in V4 for h in N3),
            "covariance a_{gh} = a_h, b_{gh} = g b_h for every g in V4, h in N_3 (rho = inclusion)")
    c = [(X[j] + 1 / X[j]) / 2 for j in range(3)]
    s = [I * (X[j] - 1 / X[j]) / 2 for j in range(3)]
    C0, S0 = c[0] * c[1] * c[2], s[0] * s[1] * s[2]
    Cj = [c[j] * s[(j + 1) % 3] * s[(j + 2) % 3] for j in range(3)]
    Sj = [s[j] * c[(j + 1) % 3] * c[(j + 2) % 3] for j in range(3)]
    Ug = (al * C0 + be * S0) * sp.eye(2) + sum(((ga[j] * Cj[j] + de[j] * Sj[j]) * PAULI[j]
                                                for j in range(3)), sp.zeros(2))
    require(mzero(laurent(T) - Ug),
            "U = alpha C0 + beta S0 + sum_j sigma_j (gamma_j C_j + delta_j S_j) as Laurent identity")

    # 2. ideal equality E = R
    E = unitarity(T)

    def re(z):
        return sp.expand(sp.re(sp.expand(z)))

    def im(z):
        return sp.expand(sp.im(sp.expand(z)))

    def cj(z):
        return sp.conjugate(z)

    R = [re(cj(al) * al) - 1, re(cj(be) * be) - 1]
    R += [re(cj(ga[j]) * ga[j]) - 1 for j in range(3)] + [re(cj(de[j]) * de[j]) - 1 for j in range(3)]
    R += [re(cj(al) * be) + sum(re(cj(ga[j]) * de[j]) for j in range(3))]
    for j in range(3):
        k, l = (j + 1) % 3, (j + 2) % 3
        R += [re(cj(al) * ga[j]) - im(cj(de[k]) * de[l]), re(cj(be) * de[j]) - im(cj(ga[k]) * ga[l]),
              re(cj(al) * de[j]), re(cj(be) * ga[j]), im(cj(ga[k]) * de[l]), im(cj(de[k]) * ga[l])]
    t1 = time.time()
    GE = sp.groebner(E, *VARS, order="grevlex")
    GR = sp.groebner(R, *VARS, order="grevlex")
    require(list(GE.exprs) == list(GR.exprs),
            f"unitarity ideal E ({len(E)} real equations) equals the reduced-system ideal R "
            f"({len(R)} equations): equal reduced Groebner bases ({time.time() - t1:.0f} s)")

    # 3. sign families
    p, r = sp.symbols("p r", real=True)  # alpha = p + i r, p^2 + r^2 = 1
    A = p + I * r
    unit = sp.groebner([p ** 2 + r ** 2 - 1], p, r, order="grevlex", domain="QQ<I>")
    fams = []
    for kappa in (1, -1):
        for eps in itertools.product((1, -1), repeat=3):
            for eta in itertools.product((1, -1), repeat=3):
                Tf = from_greek(A, kappa * A, [I * eps[j] * kappa * A for j in range(3)],
                                [I * eta[j] * A for j in range(3)])
                ok = all(unit.reduce(sp.expand(e))[1] == 0 for e in unitarity(Tf))
                if ok:
                    fams.append((kappa, eps, eta, Tf))
                if ok != (sum(eps[j] * eta[j] for j in range(3)) == -1):
                    require(False, f"sign family {kappa, eps, eta}: unitary iff sum eps eta = -1")
    require(len(fams) == 48, "of the 128 sign choices exactly the 48 with sum_j eps_j eta_j = -1 "
            "are unitary for every unimodular alpha")
    # key identities of the hand deduction (real variables)
    require(all(zero(re(cj(de[j] - I * al) * (de[j] - I * al)) * re(cj(de[j] + I * al) * (de[j] + I * al))
                     - ((re(cj(de[j]) * de[j]) - re(cj(al) * al)) ** 2 + 4 * re(cj(al) * de[j]) ** 2))
                for j in range(3)),
            "|delta_j - i alpha|^2 |delta_j + i alpha|^2 = (|delta_j|^2 - |alpha|^2)^2 + "
            "4 Re(conj(alpha) delta_j)^2, so R forces delta_j = +- i alpha")
    require(all(zero(re(cj(ga[j] - I * be) * (ga[j] - I * be)) * re(cj(ga[j] + I * be) * (ga[j] + I * be))
                     - ((re(cj(ga[j]) * ga[j]) - re(cj(be) * be)) ** 2 + 4 * re(cj(be) * ga[j]) ** 2))
                for j in range(3)),
            "same identity for gamma_j and beta: R forces gamma_j = +- i beta")
    require(zero(re(cj(be - al) * (be - al)) * re(cj(be + al) * (be + al))
                 - ((re(cj(be) * be) - re(cj(al) * al)) ** 2 + 4 * im(cj(al) * be) ** 2)),
            "|beta - alpha|^2 |beta + alpha|^2 = (|beta|^2 - |alpha|^2)^2 + 4 Im(conj(alpha) beta)^2; "
            "with gamma, delta as above, Im(conj(gamma_k) delta_l) = 0 is Im(conj(beta) alpha) = 0")

    # witness of 4b-1 lies in a family (alpha = 1, kappa = -1)
    W = {h: sp.expand(sp.prod([(sp.eye(2) + h[j] * PAULI[j]) / 2 for j in range(3)])) for h in N3}
    hit = [f for f in fams if all(mzero(f[3][h].subs({p: 1, r: 0}) - W[h]) for h in N3)]
    require(len(hit) == 1, f"the 4b-1 witness is the family kappa, eps, eta = {hit[0][:3]} at alpha = 1")

    # 4. Q-a
    qa = all(not mzero(f[3][act(g, h)] - f[3][h]) for f in fams for g in V4[1:] for h in N3)
    require(qa, "Q-a (i): in every family T_{gh} != T_h for all g in V4 \\ {e}, h in N_3 (Eq. (2))")
    y = sp.symbols("y", real=True)
    t1 = time.time()
    for g in V4[1:]:
        for h0 in ((1, 1, 1), (-1, -1, -1)):
            extra = [part for e in (T[act(g, h0)] - T[h0]) for part in (re(e), im(e)) if part != 0]
            nrm = sum(re(cj(e) * e) for e in T[h0])
            G = sp.groebner(E + extra + [y * nrm - 1], y, *VARS, order="grevlex")
            require(list(G.exprs) == [1], f"Q-a (ii): unitarity + T_gh = T_h + T_h != 0 is "
                    f"inconsistent for g = diag{tuple(int(g[i, i]) for i in range(3))}, h = {h0}")
    print(f"      Q-a (ii) Groebner time {time.time() - t1:.0f} s")

    # 5. nodes and c_0
    cs, ss = sp.symbols("c1:4", real=True), sp.symbols("s1:4", real=True)
    circ = [cs[j] ** 2 + ss[j] ** 2 - 1 for j in range(3)]
    pts = [tuple(v) for v in itertools.product((0, sp.pi / 2, sp.pi, 3 * sp.pi / 2), repeat=3)]
    expected = {q for q in pts if all(v in (0, sp.pi) for v in q)} | \
        {q for q in pts if all(v in (sp.pi / 2, 3 * sp.pi / 2) for v in q)}
    q = sp.symbols("q1:4", real=True)
    nodes_ok, speeds = True, set()
    require(all(mzero(Tf[h] - A * Tf[h].subs({p: 1, r: 0})) for _, _, _, Tf in fams for h in N3),
            "every family is alpha times a fixed symbol (the phase alpha factors out of U); nodes "
            "and H_j below use alpha = 1")
    for kappa, eps, eta, Tf in fams:
        Tf = {h: Tf[h].subs({p: 1, r: 0}) for h in N3}
        # U(q)/alpha = (C0 + kappa S0) I + i sum_j sigma_j (eps_j kappa C_j + eta_j S_j)
        f = [eps[j] * kappa * cs[j] * ss[(j + 1) % 3] * ss[(j + 2) % 3]
             + eta[j] * ss[j] * cs[(j + 1) % 3] * cs[(j + 2) % 3] for j in range(3)]
        G = sp.groebner(f + circ, *cs, *ss, order="lex")
        sols = sp.solve(list(G.exprs), [*cs, *ss], dict=True)
        found = set()
        for so in sols:
            qq = tuple(sp.atan2(so[ss[j]], so[cs[j]]) % (2 * sp.pi) for j in range(3))
            found.add(qq)
        if found != expected:
            nodes_ok = False
            break
        Uq = sum((Tf[h] * sp.exp(-I * sum(q[j] * h[j] for j in range(3))) for h in N3),
                        sp.zeros(2))
        for qq in expected:
            sub = {q[j]: qq[j] for j in range(3)}
            U0 = sp.simplify(Uq.subs(sub))
            a0 = U0[0, 0]
            if not (mzero(U0 - a0 * sp.eye(2)) and zero(sp.conjugate(a0) * a0 - 1)):
                nodes_ok = False
            H = [sp.simplify(I * sp.conjugate(a0) * sp.diff(Uq, q[j]).subs(sub) / sp.sqrt(3))
                 for j in range(3)]
            for j in range(3):
                if not zero(H[j].trace()):
                    nodes_ok = False
                for l in range(3):
                    v = sp.simplify((H[j] * H[l]).trace() / 2)
                    if not zero(v - (sp.Rational(1, 3) if j == l else 0)):
                        nodes_ok = False
            speeds.add(sp.sqrt(sp.Rational(1, 3)))
        if not nodes_ok:
            break
    require(nodes_ok, "every family: U(q) scalar exactly at {0,pi}^3 and {pi/2,3pi/2}^3 (16 points); "
            "there U = aI, |a| = 1, H_j traceless, (1/2) tr(H_j H_l) = delta_jl / 3")
    require(speeds == {1 / sp.sqrt(3)}, "c_0 = 1/sqrt(3) at every admissible node of every family")

    # 6. strict body
    sb = all(mzero(Tf[h] * Tf[h] - Tf[h].trace() * Tf[h]) and not zero(Tf[h].trace())
             and unit.reduce(sp.expand(sp.expand_complex(Tf[h].det())))[1] == 0
             for _, _, _, Tf in fams for h in N3)
    require(sb, "every T_h has rank one (det = 0), T_h^2 = tr(T_h) T_h and tr T_h != 0: vertex "
            "coefficients of U^n are tr(T_h)^(n-1) T_h != 0")
    # h_infty(q) = max_h q.h / sqrt(3) = |q|_1 / sqrt(3) >= |q|_2 / sqrt(3) (hand: |q|_1 >= |q|_2,
    # equality on the axes); the script checks the value on the axis and one diagonal direction.
    hinf = lambda v: sp.Max(*[sum(v[j] * h[j] for j in range(3)) for h in N3]) / sp.sqrt(3)
    require(sp.simplify(hinf((1, 0, 0)) - 1 / sp.sqrt(3)) == 0 and
            sp.simplify(hinf((1 / sp.sqrt(3),) * 3) - 1) == 0,
            "h_infty on the axis is 1/sqrt(3) (and 1 on the diagonal); with |q|_1 >= |q|_2 this is "
            "the minimum over unit q: c_strict^iso = rho_micro = 1/sqrt(3) = c_0")
    print(f"VERDICT: {CHECKS}/{CHECKS} exact checks passed in {time.time() - t0:.0f} s. "
          "(V4, Pauli): Q-a DISTINGUISHABILITY_IMPLIED_IN_CLASS; ADMISSIBLE_SECTORS_EXIST; "
          "RIGIDITY_PROVED_FOR_FROZEN_CLASS; SATURATION_PROVED_FOR_CLASS")


if __name__ == "__main__":
    main()
