"""Certificate for reports/2026-09-17--regional-laplace-coefficient-gate.md.

Scope: REGIONAL_LAPLACE_COEFFICIENT_GATE only. Default run: exact SymPy
identities plus rigorous mpmath interval enclosures of closed forms. It does
not formalize the analytic remainder lemmas (report [A]); it certifies the
algebra, the closed forms and the sign/margin of the sixteen complete leading
coefficients C_{M,M_B}(theta).

    python3 -B scripts/verify_regional_laplace_coefficient_gate.py
    python3 -B scripts/verify_regional_laplace_coefficient_gate.py --diagnostics

--diagnostics runs finite-N float64 numerics (numpy). They are SUPPORTED
diagnostics only: never counted as checks, never used for beta, C or state.
Frozen helpers are imported read-only.
"""

import hashlib
from pathlib import Path
import sys

import sympy as sp
from mpmath import iv, mp

from verify_directional_saturation import PS, PAULI, is_zero, walk2

ROOT = Path(__file__).resolve().parents[1]
CHARTER_SHA = "234f94a73bf0af1160e528c854774af256254cba0aa4f0d6afb09c9336de878d"
REGIONAL_CHARTER_SHA = "3a5fe8d4b22c26d017994eb849ea4e896b6e9a5230758f5c678c135c8e38977d"
REGIONAL_CERT_SHA = "e8a9df88d1ae1aa3b2dcf51b5c1050b23be79ca452a69220d65dbab4ed98eb4f"
CHECKS = 0
iv.dps = 50


def require(condition, label):
    global CHECKS
    if condition is not True and condition is not sp.true:
        raise AssertionError(label)
    CHECKS += 1
    print(f"[PASS] {label}")


def sha(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def ivev(e, env):
    """Rigorous interval evaluation of a real SymPy expression."""
    if e in env:
        return env[e]
    if e.is_Integer:
        return iv.mpf(int(e))
    if e.is_Rational:
        return iv.mpf(int(e.p)) / iv.mpf(int(e.q))
    if e == sp.pi:
        return iv.pi
    if e.is_Add:
        out = iv.mpf(0)
        for a in e.args:
            out = out + ivev(a, env)
        return out
    if e.is_Mul:
        out = iv.mpf(1)
        for a in e.args:
            out = out * ivev(a, env)
        return out
    if e.is_Pow:
        b, x = e.args
        if x.is_Integer:
            base = ivev(b, env)
            n = int(x)
            out = iv.mpf(1)
            for _ in range(abs(n)):
                out = out * base
            return out if n >= 0 else 1 / out
        if x == sp.Rational(1, 2):
            return iv.sqrt(ivev(b, env))
        if x == -sp.Rational(1, 2):
            return 1 / iv.sqrt(ivev(b, env))
        return iv.exp(ivev(x, env) * iv.log(ivev(b, env)))
    fn = {sp.sin: iv.sin, sp.cos: iv.cos, sp.exp: iv.exp, sp.log: iv.log}
    if e.func in fn:
        return fn[e.func](ivev(e.args[0], env))
    raise TypeError(f"no interval rule for {e!r}")


def fmt(x):
    return f"[{mp.nstr(mp.mpf(x.a.a), 12)}, {mp.nstr(mp.mpf(x.b.b), 12)}]"


def positive(x):
    return x.a > 0


def negative(x):
    return x.b < 0


def main():
    I2 = sp.eye(2)
    s1, s2, s3 = PAULI
    up, dn = sp.Matrix([1, 0]), sp.Matrix([0, 1])

    # ------------------------------------------------------------------ 0
    require(sha("theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md") == CHARTER_SHA,
            "frozen Laplace-coefficient charter SHA256 (git blob 18d1f65)")
    require(sha("theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md") == REGIONAL_CHARTER_SHA
            and sha("scripts/verify_regional_directional_asymptotics_gate.py") == REGIONAL_CERT_SHA,
            "inherited Sec. 8.19 charter and certificate bytes unchanged")

    # ------------------------------------------------------------------ 1 tilted symbol
    W = walk2()
    xi = sp.symbols("xi1 xi2 xi3", real=True)
    S = W.subs({PS[j]: -sp.I * xi[j] for j in range(3)}).adjugate()
    S = S.applyfunc(lambda z: sp.expand(z.rewrite(sp.exp)))
    herm = (S - S.H).applyfunc(lambda z: sp.simplify(z))
    require(herm == sp.zeros(2, 2), "S(-i xi) is Hermitian for every real xi")
    require(sp.simplify(sp.det(S) - 1) == 0, "det S(-i xi) = 1")

    pi = sp.pi
    def shifted(v):
        return W.subs({PS[j]: PS[j] + v[j] * pi for j in range(3)}, simultaneous=True)
    Wt = W.T
    rel = [((1, 0, 0), -W, "W(p+pi e1) = -W(p)"),
           ((0, 0, 1), -s3 * W * s3, "W(p+pi e3) = -s3 W(p) s3"),
           ((0, 1, 0), -s3 * Wt * s3, "W(p+pi e2) = -s3 W(p)^T s3"),
           ((0, 1, 1), Wt, "W(p+pi(e2+e3)) = W(p)^T"),
           ((1, 1, 1), -Wt, "W(p+pi(1,1,1)) = -W(p)^T")]
    for v, target, label in rel:
        D = shifted(v) - target
        require(all(is_zero(D[i, j]) for i in range(2) for j in range(2)),
                label + " (Laurent identity, valid for complex p)")

    basis = [(1, -1, 0), (0, 1, -1)]
    nontriv = []
    for e in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]:
        odd = any(sum(e[i] * v[i] for i in range(3)) % 2 for v in basis)
        nontriv.append((e, odd))
    require(all(odd == (e not in ((0, 0, 0), (1, 1, 1))) for e, odd in nontriv),
            "half-period characters are trivial on the planes x1+x2+x3=k only for eta0 in {0, pi(1,1,1)}")

    # ------------------------------------------------------------------ 2 dual point and Perron data
    C, Sh = sp.symbols("C S", positive=True)
    al = sp.symbols("alpha", positive=True)
    red = {Sh**2: C**2 - 1}
    vsq = (C**3 * (Sh / C))**2 / (C**6 - 1)
    require(sp.simplify(vsq.subs(red) - C**4 / (C**4 + C**2 + 1)) == 0,
            "dual relation on xi=t(1,1,1): alpha^2 = C^4/(C^4+C^2+1), C=cosh t")
    alpha = 1 - 1 / (2 * sp.sqrt(3))
    C2 = alpha * (alpha + sp.sqrt(4 - 3 * alpha**2)) / (2 * (1 - alpha**2))
    require(sp.simplify(sp.expand((1 - alpha**2) * C2**2 - alpha**2 * C2 - alpha**2)) == 0,
            "C*^2 = alpha(alpha+sqrt(4-3alpha^2))/(2(1-alpha^2)) solves (1-a^2)C^4 - a^2 C^2 - a^2 = 0")

    a_, d_, b1, b2 = sp.symbols("a d b1 b2", real=True)
    Dl = sp.sqrt(((a_ - d_) / 2)**2 + b1**2 + b2**2)
    M = sp.Matrix([[a_, b1 + sp.I * b2], [b1 - sp.I * b2, d_]])
    Pg = (I2 + (M - (a_ + d_) / 2 * I2) / Dl) / 2
    require((Pg * Pg - Pg).applyfunc(sp.simplify) == sp.zeros(2, 2)
            and (M * Pg - ((a_ + d_) / 2 + Dl) * Pg).applyfunc(sp.simplify) == sp.zeros(2, 2),
            "Hermitian 2x2: P=(I+(M-m)/Delta)/2 is the top spectral projector")
    ep, em = C + Sh, C - Sh                       # e^{t}, e^{-t}
    Sstar = sp.Matrix([[C**2 * em, -(1 + sp.I * C) * Sh], [-(1 - sp.I * C) * Sh, C**2 * ep]])
    require((Sstar.subs({C: sp.cosh(sp.Symbol('t')), Sh: sp.sinh(sp.Symbol('t'))})
             - S.subs({xi[0]: sp.Symbol('t'), xi[1]: sp.Symbol('t'), xi[2]: sp.Symbol('t')}))
            .applyfunc(lambda z: sp.simplify(z.rewrite(sp.exp))) == sp.zeros(2, 2),
            "S(-i t(1,1,1)) = [[C^2 e^-t, -(1+iC)S], [-(1-iC)S, C^2 e^t]]")
    Delta2 = sp.expand(((Sstar[0, 0] - Sstar[1, 1]) / 2)**2 + (1 + C**2) * Sh**2)
    require(sp.expand(Delta2 - Sh**2 * (C**4 + C**2 + 1)).subs(red) == 0
            and sp.expand((Sstar[0, 0] + Sstar[1, 1]) / 2 - C**3).subs(red) == 0
            and sp.expand(C**6 - 1 - (C**2 - 1) * (C**4 + C**2 + 1)) == 0,
            "Delta = S sqrt(C^4+C^2+1) = sqrt(C^6-1), tr/2 = C^3: top eigenvalue e^{phi*}")
    Wq = sp.sqrt(C**4 + C**2 + 1)
    P11 = (1 + ((Sstar[0, 0] - Sstar[1, 1]) / 2) / (Sh * Wq)) / 2
    P12 = Sstar[0, 1] / (2 * Sh * Wq)
    alphaC = C**2 / Wq
    require(sp.simplify(sp.expand(P11).subs(red) - (1 - alphaC) / 2) == 0
            and sp.simplify(P12 + (1 + sp.I * C) * alphaC / (2 * C**2)) == 0,
            "Perron projector P = (1/2)[[1-alpha, -(1+iC)alpha/C^2], [-(1-iC)alpha/C^2, 1+alpha]]")

    Pi_, Dd, T1, T2 = sp.symbols("Pi D T1 T2", positive=True)
    # H_ij = d_j (Pi T_i / D) with d_j Pi = Pi T_j, d_j T_i = delta_ij (1-T_i^2), d_j D = Pi^2 T_j / D
    H_off = (Pi_ * T2 * T1) / Dd - Pi_ * T1 * (Pi_**2 * T2 / Dd) / Dd**2
    H_diag = (Pi_ * T1 * T1 + Pi_ * (1 - T1**2)) / Dd - Pi_ * T1 * (Pi_**2 * T1 / Dd) / Dd**2
    rel_D = {Dd**2: Pi_**2 - 1}
    require(sp.expand(sp.expand(H_off * Dd**3).subs(rel_D) + Pi_ * T1 * T2) == 0
            and sp.expand(sp.expand(H_diag * Dd**3).subs(rel_D)
                          - (Pi_ * (1 - T1**2) * (Pi_**2 - 1) - Pi_ * T1**2)) == 0,
            "Hess phi = (Pi/D) sech^2 delta_ij - (Pi/D^3) tanh_i tanh_j, phi = arccosh(Pi)")
    Dstar = Sh * Wq
    qt = (C**3 / Dstar) / C**2
    qn = qt - 3 * C**3 * (Sh / C)**2 / Dstar**3
    qn_closed = (C / Dstar) * (C**4 + C**2 - 2) / (C**4 + C**2 + 1)
    require(sp.simplify(sp.expand((qn - qn_closed) * Dstar**3).subs(red)) == 0
            and sp.factor(C**4 + C**2 - 2) == (C - 1) * (C + 1) * (C**2 + 2),
            "q_t = C/D*, q_n = (C/D*)(C^2-1)(C^2+2)/(C^4+C^2+1) > 0: Hessian nondegenerate")

    p = sp.symbols("p1 p2 p3")
    f = sp.cos(p[0]) * sp.cos(p[1]) * sp.cos(p[2])
    fx = sp.cosh(xi[0]) * sp.cosh(xi[1]) * sp.cosh(xi[2])
    require(all(sp.simplify(sp.diff(f, p[j]).subs({p[k]: -sp.I * xi[k] for k in range(3)})
                            - sp.I * sp.diff(fx, xi[j])) == 0 for j in range(3)),
            "holomorphy: d_p f(-i xi) = i d_xi f, hence d_eta omega = i v*, d_eta^2 omega = -Hess phi")

    # ------------------------------------------------------------------ 3 free tail (Weyl limit)
    eps = sp.symbols("epsilon")
    Sfull = W.adjugate()
    lin = Sfull.subs({PS[j]: eps * PS[j] for j in range(3)}).applyfunc(
        lambda z: sp.series(z, eps, 0, 2).removeO())
    HW = PS[0] * s1 - PS[1] * s2 + PS[2] * s3
    require((lin - (I2 - sp.I * eps * HW)).applyfunc(sp.simplify) == sp.zeros(2, 2),
            "S(p) = I - i H_W(p) + O(p^2), H_W = p1 s1 - p2 s2 + p3 s3")
    require((HW * HW - (PS[0]**2 + PS[1]**2 + PS[2]**2) * I2).applyfunc(sp.expand) == sp.zeros(2, 2),
            "H_W^2 = |p|^2 I, so e^{-iH_W(q)} = cos|q| - i sin|q| H_W(q)/|q|")
    uhat = [1 / sp.sqrt(3)] * 3
    n_u = uhat[0] * s1 - uhat[1] * s2 + uhat[2] * s3
    require((n_u * dn - sp.Matrix([1 + sp.I, -1]) / sp.sqrt(3)).applyfunc(sp.simplify) == sp.zeros(2, 1),
            "H_W(u_hat) down = (1+i, -1)/sqrt(3)")
    x, c = sp.symbols("x c", positive=True)
    j0 = sp.sin(x) / x
    j1 = sp.sin(x) / x**2 - sp.cos(x) / x
    ang0 = 2 * pi * sp.integrate(sp.exp(-sp.I * x * c), (c, -1, 1))
    ang1 = 2 * pi * sp.integrate(c * sp.exp(-sp.I * x * c), (c, -1, 1))
    require(sp.simplify((ang0 - 4 * pi * j0).rewrite(sp.exp)) == 0
            and sp.simplify((ang1 + 4 * pi * sp.I * j1).rewrite(sp.exp)) == 0,
            "angular integrals: 4 pi j0 and -4 pi i j1 w_hat (plane-wave l=0,1)")
    rho = sp.sqrt(3) - sp.Rational(1, 4)
    require(sp.simplify(sp.diff(sp.sin(x) - x * sp.cos(x), x) - x * sp.sin(x)) == 0
            and bool(rho < 3) and bool(sp.Integer(1) < sp.pi / 2),
            "rho* = sqrt3-1/4 < pi: j0(k rho*), j1(k rho*), cos k, sin k > 0 on (0,1], so A,B > 0")

    w = sp.symbols("omega", positive=True)
    k = sp.symbols("k", real=True)
    def Sm(m, om):
        return -sp.cos(om) / om + (m * Cm(m - 1, om) / om if m else 1 / om)
    def Cm(m, om):
        return sp.sin(om) / om - (m * Sm(m - 1, om) / om if m else 0)
    require(all(sp.simplify(sp.integrate(k**m * sp.sin(w * k), (k, 0, 1)) - Sm(m, w)) == 0
                and sp.simplify(sp.integrate(k**m * sp.cos(w * k), (k, 0, 1)) - Cm(m, w)) == 0
                for m in range(6)),
            "moment recursions int_0^1 k^m {sin,cos}(omega k) dk, m <= 5")
    def Qs(om):
        return Sm(1, om) - 2 * Sm(3, om) + Sm(5, om)
    def Qc(om):
        return Cm(0, om) - 2 * Cm(2, om) + Cm(4, om)
    A_cf = (2 * pi / rho) * (Qs(rho + 1) + Qs(rho - 1))
    B_cf = (2 * pi / rho**2) * (Qc(rho - 1) - Qc(rho + 1)) - (2 * pi / rho) * (Qs(rho + 1) - Qs(rho - 1))
    Ib_cf = 16 * pi * Qs(sp.Rational(1, 4))
    kk = sp.symbols("kk", positive=True)
    require(sp.simplify(sp.expand_trig(sp.cos(kk) * sp.sin(kk * rho) - (sp.sin((rho + 1) * kk) + sp.sin((rho - 1) * kk)) / 2)) == 0
            and sp.simplify(sp.expand_trig(sp.sin(kk) * sp.sin(kk * rho) - (sp.cos((rho - 1) * kk) - sp.cos((rho + 1) * kk)) / 2)) == 0
            and sp.simplify(sp.expand_trig(sp.sin(kk) * sp.cos(kk * rho) - (sp.sin((rho + 1) * kk) - sp.sin((rho - 1) * kk)) / 2)) == 0,
            "product-to-sum reductions for A(rho*), B(rho*), b-profile integral")

    # ------------------------------------------------------------------ 4 discrete layer: Laplace/Poisson
    tau, dl, s, pp = sp.symbols("tau delta s p", positive=True)
    Hint = sp.Integral((dl - s)**2 * sp.besselj(0, tau * sp.sqrt(s)), (s, 0, dl))
    H3 = sp.diff(Hint, dl, 3).doit()
    require(sp.simplify(H3 - 2 * sp.besselj(0, tau * sp.sqrt(dl))) == 0,
            "H(delta)=int_0^delta (delta-s)^2 J0(tau sqrt s) ds has H''' = 2 J0(tau sqrt delta), H(0)=H'(0)=H''(0)=0")
    n = sp.symbols("n", integer=True, nonnegative=True)
    require(sp.simplify(sp.laplace_transform(s**n, s, pp, noconds=True) - sp.factorial(n) / pp**(n + 1)) == 0
            and sp.simplify(sp.summation((-tau**2 / 4)**n * sp.factorial(n) / (sp.factorial(n)**2 * pp**(n + 1)), (n, 0, sp.oo))
                            - sp.exp(-tau**2 / (4 * pp)) / pp) == 0,
            "L[J0(tau sqrt s)](p) = exp(-tau^2/4p)/p (termwise), so L[H](p) = 2 exp(-tau^2/4p)/p^4")
    cg = sp.pi * sp.sqrt(3) * 2 / (sp.sqrt(3)**4)
    require(sp.simplify(cg - 2 * sp.pi / (3 * sp.sqrt(3))) == 0,
            "depth x = sqrt3 delta: ghat(omega) = c_g exp(-tau^2/(4 sqrt3 s)) / s^4, s = t*+i omega, c_g = 2pi/(3sqrt3)")
    sig = sp.symbols("sigma", positive=True)
    require(sp.simplify(2 * pi * sp.integrate((dl - sig**2)**2 * sig, (sig, 0, sp.sqrt(dl))) - pi * dl**3 / 3) == 0
            and sp.simplify(sp.laplace_transform(pi * (s**3 / 3), s, pp, noconds=True) - 2 * pi / pp**4) == 0,
            "tau=0 consistency: Psi_delta(0) = pi delta^3/3 and its Laplace transform 2pi/p^4")
    require(sp.simplify(2 * sp.zeta(4) / (2 * pi)**4 - sp.Rational(1, 720)) == 0
            and sp.simplify(2 * (1 - sp.Rational(1, 16)) * sp.zeta(4) / pi**4 - sp.Rational(1, 48)) == 0,
            "Poisson tails: sum_{n!=0} (2 pi n)^-4 = 1/720; sum_n (pi(2n+1))^-4 = 1/48")
    qsym, aa = sp.symbols("q a", positive=True)
    require(sp.simplify(2 * pi * sp.integrate(tau * sp.exp(-aa * tau**2), (tau, 0, sp.oo)) - pi / aa) == 0,
            "Gaussian: int_{R^2} exp(-a|tau|^2) = pi/a (Gamma-bar, epsilon_+-, epsilon_- closed forms)")

    # ------------------------------------------------------------------ 5 prefactor bookkeeping and beta
    Bhat, qn_s = sp.symbols("Bhat q_n", positive=True)
    K_build = (16 * pi / sp.sqrt(3)) * (32 / sp.sqrt(3)) * sp.sqrt(2 * pi / qn_s) * 2 / (2 * pi)**3 * Bhat
    require(sp.simplify(K_build - sp.Rational(128, 3) / pi**2 * sp.sqrt(2 * pi / qn_s) * Bhat) == 0,
            "prefactor K = (128/(3 pi^2)) sqrt(2pi/q_n) Bhat from A-layer 16pi/sqrt3, B-layer 32/sqrt3, 2/N, (2pi)^-3")
    beta_terms = [-sp.Rational(3, 2), -sp.Rational(3, 2), -2, -2, 1, 1, -sp.Rational(1, 2), -1]
    require(sum(beta_terms) == -sp.Rational(13, 2) and sum(beta_terms) - 2 == -sp.Rational(17, 2),
            "power count: b_N, r, s_N, h_B, two in-plane areas, eta_n Gaussian, eta_t scale -> beta = 13/2; c_N-term 17/2")
    Nn, m_, j_, jj = sp.symbols("N m j jj", integer=True)
    require(sp.simplify(((Nn + (3 * Nn - 2 * m_ + j_ + jj)) - (j_ + jj)) / 2 - (2 * Nn - m_)) == 0,
            "parity: (-1)^{N + k_y - k_x} = (-1)^{j+j'} with k_y-k_x = 3N - 2 floor(sqrt3 R) + j + j'")

    # ------------------------------------------------------------------ 6 interval enclosures
    ivA = iv.mpf(1) - 1 / (2 * iv.sqrt(3))
    ivC2 = ivA * (ivA + iv.sqrt(4 - 3 * ivA**2)) / (2 * (1 - ivA**2))
    ivC = iv.sqrt(ivC2)
    ivS = iv.sqrt(ivC2 - 1)
    ivt = iv.log(ivC + ivS)
    ivD = iv.sqrt(ivC**6 - 1)
    ivphi = iv.log(ivC**3 + ivD)
    ivK = 3 * ivA * ivt - ivphi
    ivJ = (1 - iv.sqrt(3) / 2) * iv.log(2)
    require(positive(ivC2 - 1) and positive(ivK - ivJ) and positive(iv.log(4) - ivK),
            f"K* = 3 alpha t* - arccosh(C*^3) in {fmt(ivK)}, t* in {fmt(ivt)}; J < K* < log 4 (consistency with Sec. 8.19)")
    ivqt = ivC / ivD
    ivqn = ivqt * (ivC2 - 1) * (ivC2 + 2) / (ivC2**2 + ivC2 + 1)
    require(positive(ivqn) and positive(ivqt),
            f"q_n in {fmt(ivqn)}, q_t in {fmt(ivqt)}; det Q = q_n q_t^2 > 0")
    env = {al: ivA, C: ivC}
    ivAv = ivev(sp.expand(A_cf), {})
    ivBv = ivev(sp.expand(B_cf), {})
    ivIb = ivev(sp.expand(Ib_cf), {})
    require(positive(ivAv) and positive(ivBv) and positive(ivIb),
            f"A(rho*) in {fmt(ivAv)}, B(rho*) in {fmt(ivBv)}, I_b in {fmt(ivIb)} (all > 0)")
    ivcr = iv.sqrt(3465) / (64 * iv.pi**2)
    ivBhat = ivcr * ivIb
    ivcg = 2 * iv.pi / (3 * iv.sqrt(3))
    ivGbar = ivcg**2 / ivt**8 * iv.pi / (ivqt + 1 / (2 * iv.sqrt(3) * ivt))
    ivS0int = ivcg / ivt**4 * iv.pi / (ivqt + 1 / (4 * iv.sqrt(3) * ivt))
    iveplus = 2 * (ivcg / 720) * ivS0int + (ivcg / 720)**2 * iv.pi / ivqt
    ivemin = (ivcg / 48)**2 * iv.pi / ivqt
    require(positive(ivGbar - iveplus) and negative(iveplus / ivGbar - iv.mpf("0.0011"))
            and negative(ivemin / ivGbar - iv.mpf("0.00006")),
            f"Gamma-bar in {fmt(ivGbar)}; |Gamma_+(theta)-Gamma-bar| <= eps_+ (eps_+/Gamma-bar < 1.1e-3); 0 <= Gamma_- <= eps_- (< 6e-5 Gamma-bar)")
    ivKpref = 128 / (3 * iv.pi**2) * iv.sqrt(2 * iv.pi / ivqn) * ivBhat
    require(positive(ivKpref), f"K in {fmt(ivKpref)} > 0, c_r in {fmt(ivcr)}")

    # ------------------------------------------------------------------ 7 sixteen pairs
    Asym, Bsym = sp.symbols("A B", positive=True)
    Csym = sp.symbols("C", positive=True)
    Pm = sp.Rational(1, 2) * sp.Matrix([[1 - al, -(1 + sp.I * Csym) * al / Csym**2],
                                        [-(1 - sp.I * Csym) * al / Csym**2, 1 + al]])
    R0 = sp.Matrix([-(Bsym / sp.sqrt(3)) * (1 + sp.I), Asym + Bsym / sp.sqrt(3)])   # times c_r > 0
    MBs = {"I": I2, "P1": (I2 + s1) / 2, "P2": (I2 + s2) / 2, "P3": (I2 + s3) / 2}
    enc = {"I": (dn, lambda z: -2 * sp.im(z)), "s1": (up, lambda z: -2 * sp.im(z)),
           "s2": (up, lambda z: 2 * sp.re(z)), "s3": (dn, lambda z: 2 * sp.im(z))}
    env = {al: ivA, Csym: ivC, Asym: ivAv, Bsym: ivBv}
    ells = {}
    for e_name, (chi, ell) in enc.items():
        for mb, Mb in MBs.items():
            l0 = sp.expand(ell(sp.expand((R0.H * Mb * Pm * chi)[0])))
            lp = sp.expand(ell(sp.expand((R0.H * Mb * Pm.conjugate() * chi)[0])))
            ells[(e_name, mb)] = (l0, lp)
            i0, ip = ivev(l0, env), ivev(lp, env)
            margin = abs(i0).a * (ivGbar - iveplus).a - (ivemin * abs(ip)).b
            Cbar = ivKpref * ivcr * ivGbar * i0
            osc = (iveplus * abs(i0) + ivemin * abs(ip)) / (ivGbar * abs(i0))
            require(margin > 0 and (positive(i0) or negative(i0)),
                    f"C({e_name},{mb})(theta) sign-definite for all theta: C-bar in {fmt(Cbar)}, "
                    f"|C(theta)/C-bar - 1| <= {mp.nstr(mp.mpf(osc.b.b), 4)}")
    require(all(sp.simplify(ells[("s3", mb)][0] + ells[("I", mb)][0]) == 0
                and sp.simplify(ells[("s3", mb)][1] + ells[("I", mb)][1]) == 0 for mb in MBs),
            "leading coefficients satisfy C(sigma3,M_B) = -C(I,M_B) exactly (r x d interference)")
    require(all(sp.simplify(ells[("I", mb)][0] - ells[("I", "I")][0]) == 0 for mb in ("P3",))
            and sp.simplify(ells[("I", "I")][0] + sp.sqrt(3) * Bsym * al * (Csym - 1) / (3 * Csym**2)) == 0,
            "C(I,I) = C(I,P3) proportional to -B alpha (C-1)/C^2: vanishes only if B=0 or C=1 (neither)")

    print(f"{CHECKS}/{CHECKS} exact checks passed. The analytic remainder O(N^-1/2) "
          "and the saddle-point lemmas are report [A], not encoded here.")
    return 0


# ---------------------------------------------------------------------- diagnostics (SUPPORTED only)
def diagnostics():
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    alpha = 1 - 1 / (2 * np.sqrt(3))
    C2 = alpha * (alpha + np.sqrt(4 - 3 * alpha**2)) / (2 * (1 - alpha**2))
    C = np.sqrt(C2); Sh = np.sqrt(C2 - 1); ts = np.log(C + Sh)
    Dst = np.sqrt(C**6 - 1); phi = np.log(C**3 + Dst)
    qt = C / Dst; qn = qt * (C2 - 1) * (C2 + 2) / (C2**2 + C2 + 1)
    P = 0.5 * np.array([[1 - alpha, -(1 + 1j * C) * alpha / C2], [-(1 - 1j * C) * alpha / C2, 1 + alpha]])
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
    I2 = np.eye(2)
    MB = {"I": I2, "P1": (I2 + s1) / 2, "P2": (I2 + s2) / 2, "P3": (I2 + s3) / 2}
    g = lambda q: (1 - q**2)**2
    kq, wk = leggauss(80); kq = 0.5 * (kq + 1); wk = 0.5 * wk
    rho = np.sqrt(3) - 0.25
    A = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.cos(kq) * np.sinc(kq * rho / np.pi))
    B = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.sin(kq) * (np.sin(kq * rho) / (kq * rho)**2 - np.cos(kq * rho) / (kq * rho)))
    cr = np.sqrt(3465) / (64 * np.pi**2)
    Bhat = cr * 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.sinc(kq / 4 / np.pi))
    nvec = np.array([[1, 1 + 1j], [1 - 1j, -1]]) / np.sqrt(3)
    R0 = cr * (A * np.array([0, 1]) - B * (nvec @ np.array([0, 1])))
    Kpref = 128 / (3 * np.pi**2) * np.sqrt(2 * np.pi / qn) * Bhat
    cg = 2 * np.pi / (3 * np.sqrt(3))
    tgrid = np.linspace(0, 12, 6001)
    uh = np.ones(3) / np.sqrt(3)

    def gammas(theta, nf=60):
        nn = np.arange(-nf, nf + 1)
        sp_ = ts + 2j * np.pi * nn; sm_ = ts + 1j * np.pi * (2 * nn + 1)
        Sp = (cg * np.exp(-tgrid[:, None]**2 / (4 * np.sqrt(3) * sp_)) / sp_**4 * np.exp(2j * np.pi * nn * theta)).sum(1).real
        Sm = (cg * np.exp(-tgrid[:, None]**2 / (4 * np.sqrt(3) * sm_)) / sm_**4 * np.exp(1j * np.pi * (2 * nn + 1) * theta)).sum(1).real
        wq = 2 * np.pi * tgrid * np.exp(-qt * tgrid**2)
        return np.trapz(wq * Sp**2, tgrid), np.trapz(wq * Sm**2, tgrid)

    def bN(N, r2):
        return np.sqrt(3465) * np.pi / 8 * N**-1.5 / (2 * np.pi)**3 * 4 * np.pi * (wk * kq**2 * g(kq)) @ np.sinc(np.outer(kq, np.sqrt(r2) / N) / np.pi)

    def tilted_SN(N, L):
        m = np.fft.fftfreq(L) * L
        eta = -2 * np.pi * m / L - 1j * ts
        c = np.cos(eta); s = np.sin(eta); e = np.exp(1j * eta)
        c1, c2, sn1, sn2, e3 = c[:, None, None], c[None, :, None], s[:, None, None], s[None, :, None], e[None, None, :]
        f = (c1 * c2) * c[None, None, :]
        sc = np.exp(-phi)
        Um2 = np.zeros((L, L, L), complex); Um1 = np.full((L, L, L), sc, complex)
        for _ in range(N - 1):
            tmp = 2 * sc * f * Um1; tmp -= sc * sc * Um2
            Um2, Um1 = Um1, tmp
        W11 = (c1 * c2) * e3; W22 = (c1 * c2) / e3; W12 = -c1 * sn2 + 1j * sn1; W21 = c1 * sn2 + 1j * sn1
        return Um1 * W22 - sc * Um2, -Um1 * W12, -Um1 * W21, Um1 * W11 - sc * Um2

    def r_tail(N, Y, nr=24, nth=28, nph=56):
        x, wx = leggauss(nr); kr = 0.5 * (x + 1); wkr = 0.5 * wx
        ct, wct = leggauss(nth); ph = 2 * np.pi * np.arange(nph) / nph
        KQ, CT, PH = np.meshgrid(kr, ct, ph, indexing="ij")
        WQ = ((wkr[:, None, None] * wct[None, :, None]) * (2 * np.pi / nph) * KQ**2 * g(KQ)).reshape(-1)
        st = np.sqrt(1 - CT**2)
        Q = np.stack([KQ * st * np.cos(PH), KQ * st * np.sin(PH), KQ * CT], -1).reshape(-1, 3)
        pq = Q / N; c = np.cos(pq); sn = np.sin(pq); e3 = np.exp(1j * pq[:, 2])
        f = c[:, 0] * c[:, 1] * c[:, 2]
        Um2 = np.zeros_like(f); Um1 = np.ones_like(f)
        for _ in range(N - 1):
            Um2, Um1 = Um1, 2 * f * Um1 - Um2
        W11 = c[:, 0] * c[:, 1] * e3; W12 = -c[:, 0] * sn[:, 1] + 1j * sn[:, 0]
        Md = np.stack([-Um1 * W12, Um1 * W11 - Um2], 0) * WQ
        out = np.zeros((Y.shape[0], 2), complex)
        for i0 in range(0, Y.shape[0], 512):
            out[i0:i0 + 512] = np.exp(-1j * (Y[i0:i0 + 512] @ Q.T) / N) @ Md.T
        return out * np.sqrt(3465) * np.pi / 8 * N**-1.5 / (2 * np.pi)**3

    PROJ = [((0, 0, 0), +1, P), ((1, 0, 0), -1, P), ((0, 0, 1), -1, s3 @ P @ s3), ((1, 0, 1), +1, s3 @ P @ s3),
            ((0, 1, 0), -1, s3 @ P.T @ s3), ((1, 1, 0), +1, s3 @ P.T @ s3), ((0, 1, 1), +1, P.T), ((1, 1, 1), -1, P.T)]
    print("[SUPPORTED diagnostics] float64; not checks; not used for beta, C or the terminal state")
    for N in (40, 640):
        yv = np.round(N * np.ones(3) - (N / 4) * uh)
        w_ = yv / N; rw = np.linalg.norm(w_); wh = w_ / rw
        Aw = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.cos(kq) * np.sinc(kq * rw / np.pi))
        Bw = 4 * np.pi * np.sum(wk * kq**2 * g(kq) * np.sin(kq) * (np.sin(kq * rw) / (kq * rw)**2 - np.cos(kq * rw) / (kq * rw)))
        Hw = wh[0] * s1 - wh[1] * s2 + wh[2] * s3
        R0w = cr * (Aw * np.array([0, 1]) - Bw * (Hw @ np.array([0, 1])))
        rq = r_tail(N, yv.astype(int)[None, :], nr=32, nth=40, nph=80)[0] * N**1.5
        print(f"  free tail N={N}: |N^(3/2) r(y) - R0(y/N)| / |R0| = {np.abs(rq - R0w).max() / np.abs(R0w).max():.2e}")
    for N in (24, 40, 56):
        R = N / 4; L = 2 * (N + int(np.ceil(R))) + 3
        SN = tilted_SN(N, L)
        rg = np.arange(-int(np.ceil(R)), int(np.ceil(R)) + 1)
        X = np.array(np.meshgrid(rg, rg, rg, indexing="ij")).reshape(3, -1).T
        r2 = (X**2).sum(1); X = X[16 * r2 < N * N]; r2 = r2[16 * r2 < N * N]
        F = (1 - 16 * r2 / N**2)**2
        amp = np.exp(ts * X.sum(1) - ts * np.sqrt(3) * R) * np.sin(np.pi * F / 2) * bN(N, r2)
        Y = X + N; wB = np.exp(-ts * Y.sum(1) + ts * (3 * N - np.sqrt(3) * R)) * F
        src = np.zeros((L, L, L), complex); src[X[:, 0] % L, X[:, 1] % L, X[:, 2] % L] = amp
        hf = np.fft.fftn(src)
        fld = {"d": np.stack([np.fft.ifftn(SN[1] * hf), np.fft.ifftn(SN[3] * hf)], -1)[Y[:, 0] % L, Y[:, 1] % L, Y[:, 2] % L],
               "b": np.stack([np.fft.ifftn(SN[0] * hf), np.fft.ifftn(SN[2] * hf)], -1)[Y[:, 0] % L, Y[:, 1] % L, Y[:, 2] % L]}
        cN = -2 * np.sin(np.pi * F / 4)**2
        amp_a = np.exp(ts * X.sum(1) - ts * np.sqrt(3) * R) * cN * bN(N, r2)
        src = np.zeros((L, L, L), complex); src[X[:, 0] % L, X[:, 1] % L, X[:, 2] % L] = amp_a
        hfa = np.fft.fftn(src)
        fld["a"] = np.stack([np.fft.ifftn(SN[1] * hfa), np.fft.ifftn(SN[3] * hfa)], -1)[Y[:, 0] % L, Y[:, 1] % L, Y[:, 2] % L]
        keep = wB * np.abs(fld["d"]).sum(1) > 1e-13 * (wB * np.abs(fld["d"]).sum(1)).max()
        Yk, wkB = Y[keep], wB[keep]
        rY = r_tail(N, Yk)
        ak = amp > 1e-13 * amp.max(); Xa, aa = X[ak], amp[ak]
        ref = {"d": np.zeros((Yk.shape[0], 2), complex), "b": np.zeros((Yk.shape[0], 2), complex)}
        pref = (2 * np.pi * N)**-1.5 / np.sqrt(qn * qt * qt)
        for i0 in range(0, Yk.shape[0], 64):
            Dd = Yk[i0:i0 + 64, None, :] - Xa[None, :, :]
            Dl = Dd - N * alpha
            dn_ = Dl @ uh
            G = pref * np.exp(-(dn_**2 / qn + ((Dl**2).sum(-1) - dn_**2) / qt) / (2 * N)) * aa
            Kt = np.zeros(Dd.shape[:2] + (2, 2), complex)
            for e0, epsn, Pi in PROJ:
                Kt += (G * (-1.0)**((Dd * np.array(e0)).sum(-1)) * epsn**N)[..., None, None] * Pi
            ref["d"][i0:i0 + 64] = Kt[..., :, 1].sum(1); ref["b"][i0:i0 + 64] = Kt[..., :, 0].sum(1)
        theta = (np.sqrt(3) * R) % 1
        gp, gm = gammas(theta)
        inner = {nm: np.sum(wkB * np.einsum("yi,yi->y", rY.conj(), fld[nm][keep])) for nm in ("a", "d", "b")}
        print(f"  N={N:3d} M_B=I, e^(K*N)-scaled: |2Re<r,Ea>| / |2Im<r,Ed>| = {abs(inner['a'].real) / abs(inner['d'].imag):.3f};"
              f"  |2Re<r,Ea>| / |2Re<r,Eb>| = {abs(inner['a'].real) / abs(inner['b'].real):.3f}")
        for name, chi in (("d", np.array([0, 1])), ("b", np.array([1, 0]))):
            for mb, Mb in MB.items():
                num = np.sum(wkB * np.einsum("yi,ij,yj->y", rY.conj(), Mb, fld[name][keep]))
                rf = np.sum(wkB * np.einsum("yi,ij,yj->y", rY.conj(), Mb, ref[name]))
                lead = Kpref * (gp * (R0.conj() @ Mb @ P @ chi) + gm * (R0.conj() @ Mb @ P.conj() @ chi)) * N**-6.5
                print(f"  N={N:3d} {name} {mb:2s} brute/ref = {num / rf:.5f}   ref/lead = {rf / lead:.5f}")
    nodes = 256
    th_ = 2 * np.pi * np.arange(nodes) / nodes
    J0 = lambda z: np.cos(np.multiply.outer(z, np.sin(th_))).mean(-1)
    xg, wg = leggauss(400)
    for N in (1000, 10000, 30000):
        R = N / 4; theta = (np.sqrt(3) * R) % 1
        tau = np.linspace(0, 12, 1201)[1:] / np.sqrt(N); dtau = tau[1] - tau[0]
        Gh = 2 * np.pi * N * qt * np.exp(-N * qt * tau**2 / 2)
        hats = []
        for j in range(60):
            d = (theta + j) / np.sqrt(3)
            if d <= 0:
                hats.append(None); continue
            rr = np.sqrt(2 * R * d - d * d); gq = 0.5 * rr * (xg + 1); wq = 0.5 * rr * wg
            r2 = (R - d)**2 + gq**2; F = (1 - 16 * r2 / N**2)**2
            Jm = J0(np.outer(tau, gq))
            hats.append((d, 2 * np.pi * (Jm * (np.sin(np.pi * F / 2) * bN(N, r2) * gq * wq)).sum(1),
                         2 * np.pi * (Jm * (F * gq * wq)).sum(1)))
        tot = 0.0
        for hA in hats:
            for hB in hats:
                if hA is None or hB is None:
                    continue
                ds = hA[0] + hB[0]
                tot += np.exp(-np.sqrt(3) * ts * ds - ds**2 / (2 * N * qn)) * np.sum(hA[1] * hB[2] * Gh * tau) * dtau / (2 * np.pi)
        semi = tot * (2 * np.pi * N)**-1.5 / np.sqrt(qn * qt * qt) / 3 * N**-1.5
        gp, _ = gammas(theta)
        print(f"  semi-continuum N={N:6d}: semi/lead = {semi / (Kpref * gp * N**-6.5):.5f}")


if __name__ == "__main__":
    try:
        rc = main()
        if "--diagnostics" in sys.argv[1:]:
            diagnostics()
        sys.exit(rc)
    except Exception as exc:
        print(f"[FAIL] {exc!r}")
        sys.exit(1)
