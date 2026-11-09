#!/usr/bin/env python3
"""Exact checks for the Thirring two-particle low-energy preflight.

Contract: theory/THIRRING_TWO_PARTICLE_IR_PREFLIGHT_GATE.md (commit 6d24fb8).
Report:   reports/2026-11-09--thirring-two-particle-ir.md

Family F: chi = pi/2 (z = i), mu in (0,1), nu = sqrt(1-mu^2). Conventions as in
1804.08508v1 Eq.(1)-(5): W(q)=[[nu e^{iq}, -i mu],[-i mu, nu e^{-iq}]], interaction
before F, basis (up up, up down, down up, down down) = (RR, RL, LR, LL).

Certified (exact SymPy, no floating point):
  O1  U B = F B D, D = diag(1,i,i,1), for symbolic mu on the M=1 code (window).
  O2  free branch: omega0 = acos(nu), omega''(0) = nu/mu, c_f^2 = omega0*nu/mu,
      limits omega0/mu -> 1 and c_f^2 -> 1 as mu -> 0.
  O3a at p=0 the k_R = pi solution of T_+ = 0 gives a normalizable eigenvector
      (checked pointwise on the lattice at mu = 3/5 and mu = 5/13) with eigenvalue
      e^{i M_b}, cos M_b = nu^2, decay factor |lambda| < 1.
  O3b the Gamma_0 solution of T_+ = 0 at p=0 has k_I > 0 (not normalizable).
  O3c implicit differentiation of the bound condition at p=0 (symbolic mu):
      c_b^2 = M_b nu^2 / (sqrt2 C0 mu), C0 = sqrt((1+nu^2)/2); limits
      M_b/mu -> sqrt2 and c_b^2 -> 1; series of c_b^2 - c_f^2.
  O4  Gamma W Gamma = -W (Gamma = sigma_z (-1)^x) on a window, and the low-energy
      limit of g_+(mu Q)/(-i mu) = sqrt(1+Q^2) + Q (rapidity form of T_+).

Not certified (written in the report): the case analysis that the bound branch is
unique and continuous near p=0 (taken from 1711.03920 Lemma 2 / 1804.08508 p.10,13),
the bulk-recurrence argument that the windowed eigenvector check extends to all
sites, and any wave-packet statement for O4.

A separately labelled floating-point illustration (finite-difference check of
c_b at mu=3/5) is written to ...-illustration.txt and feeds no verdict.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--thirring-two-particle-ir"
CHECKS = []
I = sp.I
R, L = 0, 1
BASIS = [(R, R), (R, L), (L, R), (L, L)]
Z = sp.I  # e^{i chi}, chi = pi/2


def exact(name, cond):
    CHECKS.append(dict(name=name, passed=bool(cond)))


def iszero(x):
    x = sp.expand(sp.expand_complex(x))
    if x == 0:
        return True
    return sp.simplify(sp.radsimp(x)) == 0


# ---------------- lattice machinery (first-quantized two-fermion amplitudes) ----------------
def W_pre(x, a, MU, NU):
    """(coef, src site, src comp) with (W phi)(x,a) = sum c phi(src). R moves right."""
    if a == R:
        return ((NU, x - 1, R), (-I * MU, x, L))
    return ((-I * MU, x, R), (NU, x + 1, L))


def F_op(amp, MU, NU):
    def out(x1, a1, x2, a2):
        s = 0
        for c1, y1, b1 in W_pre(x1, a1, MU, NU):
            for c2, y2, b2 in W_pre(x2, a2, MU, NU):
                s += c1 * c2 * amp(y1, b1, y2, b2)
        return s
    return out


def J_op(amp):
    def out(x1, a1, x2, a2):
        v = amp(x1, a1, x2, a2)
        return Z * v if (x1 == x2 and a1 != a2) else v
    return out


# ---------------- O1 ----------------
def check_O1():
    mu = sp.symbols("mu", positive=True)
    nu = sp.sqrt(1 - mu**2)
    A = [(0, R), (1, L)]
    Bm = [(1, R), (0, L)]
    D = [1, Z, Z, 1]
    ok = True
    for j, (a, b) in enumerate([(0, 0), (0, 1), (1, 0), (1, 1)]):
        (xa, ca), (xb, cb) = A[a], Bm[b]
        vec = {(xa, ca, xb, cb): 1, (xb, cb, xa, ca): -1}
        amp = lambda x1, a1, x2, a2, vec=vec: vec.get((x1, a1, x2, a2), 0)
        UB = F_op(J_op(amp), mu, nu)
        FB = F_op(amp, mu, nu)
        for x1 in range(-2, 4):
            for x2 in range(-2, 4):
                for a1, a2 in BASIS:
                    ok &= iszero(UB(x1, a1, x2, a2) - D[j] * FB(x1, a1, x2, a2))
    exact("O1-first-step-gate-D-for-symbolic-mu", ok)


# ---------------- O2 ----------------
def check_O2():
    mu, q = sp.symbols("mu q", positive=True)
    nu = sp.sqrt(1 - mu**2)
    om = sp.acos(nu * sp.cos(q))
    d2 = sp.simplify(sp.diff(om, q, 2).subs(q, 0))
    exact("O2-omega''(0)=nu/mu", iszero(d2 - nu / mu))
    exact("O2-omega'(0)=0", iszero(sp.diff(om, q).subs(q, 0)))
    om0 = sp.acos(nu)
    cf2 = om0 * nu / mu
    ser = sp.series(om**2, q, 0, 4).removeO()
    exact("O2-omega^2-q^2-coefficient=c_f^2", iszero(ser.coeff(q, 2) - cf2))
    exact("O2-limit-omega0/mu=1", sp.limit(om0 / mu, mu, 0, "+") == 1)
    exact("O2-limit-c_f^2=1", sp.limit(cf2, mu, 0, "+") == 1)
    return cf2, mu


# ---------------- O3 ----------------
def bound_vector(MU):
    """p=0, k~ = pi + i kappa, cosh(2 kappa)=1/nu^2, kappa<0. Returns f(y) and lambda_b."""
    NU = sp.sqrt(1 - MU**2)
    r = (1 - MU * sp.sqrt(2 - MU**2)) / NU**2          # t^2, t = e^{kappa}
    t = sp.sqrt(r)
    lam = -t                                            # e^{-i k~}
    # v^{++}_{k~} components, from g_+(pi+i kappa)=-i mu (1+i)/sqrt2, g_+(-pi-i kappa)=-i mu (1-i)/sqrt2
    gpk = -I * MU * (1 + I) / sp.sqrt(2)
    gmk = -I * MU * (1 - I) / sp.sqrt(2)
    a, b, c, d = -MU**2, -I * MU * gmk, -I * MU * gpk, gpk * gmk
    def f(y, comp):
        if y >= 0:
            if comp in (0, 3):
                if y % 2 == 1:
                    return 2 * (a if comp == 0 else d) * lam**y
                return 0
            if y % 2 == 0:
                val = 2 * (b if comp == 1 else c) * lam**y
                if comp == 1 and y == 0:
                    val = val / Z                          # e^{-i chi} on component 2 at y=0
                return val
            return 0
        swap = {0: 0, 1: 2, 2: 1, 3: 3}
        return -f(-y, swap[comp])
    lam_b = (1 - MU**2) + I * MU * sp.sqrt(2 - MU**2)    # e^{i M_b}, cos M_b = nu^2
    return f, lam_b, r, (a, b, c, d), (gpk, gmk), NU


def check_O3_eigenvector(MU, tag):
    f, lam_b, r, (a, b, c, d), (gpk, gmk), NU = bound_vector(MU)
    exact(f"O3a-{tag}-decay-0<t^2<1", bool(0 < r < 1))
    exact(f"O3a-{tag}-T+numerator-zero", iszero(gpk + sp.conjugate(Z) * gmk))
    exact(f"O3a-{tag}-|lambda_b|=1", iszero(sp.Abs(lam_b)**2 - 1))
    exact(f"O3a-{tag}-cos-M_b=nu^2", iszero(sp.re(lam_b) - NU**2))
    psi = lambda x1, a1, x2, a2: f(x1 - x2, BASIS.index((a1, a2)))
    Upsi = F_op(J_op(psi), MU, NU)
    ok, nonzero = True, False
    for x1 in range(-5, 6):
        for x2 in range(-5, 6):
            for a1, a2 in BASIS:
                ok &= iszero(Upsi(x1, a1, x2, a2) - lam_b * psi(x1, a1, x2, a2))
                nonzero |= not iszero(psi(x1, a1, x2, a2))
    exact(f"O3a-{tag}-lattice-eigenvector-window-|x|<=5", ok and nonzero)
    return dict(mu=str(MU), t_squared=str(sp.nsimplify(r)), lambda_b=str(lam_b))


def check_O3b():
    kap = sp.symbols("kappa", real=True)
    nu = sp.symbols("nu", positive=True)
    S = sp.sqrt(1 - nu**2 * sp.cosh(kap)**2)
    sh = sp.sinh(kap)
    gp = -I * (S + I * nu * sh)       # g_+(i kappa)
    gm = -I * (S - I * nu * sh)       # g_+(-i kappa)
    num = sp.expand(gp + sp.conjugate(Z) * gm)
    target = sp.expand((-I) * (1 - I) * (S - nu * sh))
    exact("O3b-Gamma0-T+numerator=(-i)(1-i)(S-nu sinh kappa)", iszero(num - target))
    # S >= 0, so S = nu sinh(kappa) forces kappa >= 0: k_I = kappa > 0, not normalizable.


def check_O3c(cf2, mu):
    nu = sp.sqrt(1 - mu**2)
    C0 = sp.sqrt((1 + nu**2) / 2)
    S0 = mu / sp.sqrt(2)                                  # sin omega(z0)
    sh0 = -mu / (sp.sqrt(2) * nu)                         # sinh kappa0
    ch0 = C0 / nu                                         # cosh kappa0
    exact("O3c-cosh^2-sinh^2=1", iszero(ch0**2 - sh0**2 - 1))
    exact("O3c-bound-condition-S0=-nu*sinh", iszero(S0 + nu * sh0))
    exact("O3c-C0^2+S0^2=1", iszero(C0**2 + S0**2 - 1))
    sinz, cosz = I * sh0, ch0
    w1 = nu * sinz / S0                                    # omega'(z0)
    w2 = (nu * cosz * S0 - nu * sinz * C0 * w1) / S0**2    # omega''(z0)
    X1 = C0 * w1 - nu * cosz                               # X'(z0)
    X2 = -S0 * w1**2 + C0 * w2 + nu * sinz                 # X''(z0)
    Fk = sp.re(sp.expand((1 + I) * I * X1))
    Fpp = sp.re(sp.expand((1 + I) * X2))
    Fp = sp.re(sp.expand((1 + I) * X1))
    exact("O3c-omega'(z0)=-i", iszero(w1 + I))
    exact("O3c-F_p(0)=0", iszero(Fp))
    kpp = -Fpp / Fk
    Epp = 2 * sp.re(sp.expand(w2 + I * w1 * kpp))
    exact("O3c-E''(0)=2sqrt2 nu^2/(C0 mu)", iszero(Epp - 2 * sp.sqrt(2) * nu**2 / (C0 * mu)))
    Mb = sp.acos(nu**2)
    cb2 = Mb * Epp / 4                                     # omega_b^2 = M_b^2 + c_b^2 P^2, P = 2p
    exact("O3c-c_b^2-closed-form", iszero(cb2 - Mb * nu**2 / (sp.sqrt(2) * C0 * mu)))
    exact("O3c-M_b-below-threshold-cos(M_b)>cos(2 omega0)", iszero(sp.cos(2 * sp.acos(nu)) - (2 * nu**2 - 1)))
    exact("O3c-limit-M_b/mu=sqrt2", sp.simplify(sp.limit(Mb / mu, mu, 0, "+") - sp.sqrt(2)) == 0)
    lim_cb2 = sp.limit(cb2, mu, 0, "+")
    exact("O3c-limit-c_b^2=1", sp.simplify(lim_cb2 - 1) == 0)
    diff_ser = sp.series(cb2 - cf2, mu, 0, 4).removeO()
    exact("O3c-c_b^2-c_f^2=-mu^2/3+O(mu^4)", iszero(sp.expand(diff_ser) + mu**2 / 3))
    return dict(c_b2=str(sp.simplify(cb2)), c_f2=str(cf2), cb2_minus_cf2_series=str(sp.expand(diff_ser)),
                M_b="acos(nu^2)"), (Mb, cb2, nu)


# ---------------- O4 ----------------
def check_O4():
    mu = sp.symbols("mu", positive=True)
    nu = sp.sqrt(1 - mu**2)
    # Gamma = sigma_z (-1)^x ; check Gamma W Gamma = -W on single-particle amplitudes
    ok = True
    gam = lambda x, a: (1 if a == R else -1) * (1 if x % 2 == 0 else -1)
    for x in range(-3, 4):
        for a in (R, L):
            for xs in range(-4, 5):
                for b in (R, L):
                    w = sum(c for c, ys, bs in W_pre(x, a, mu, nu) if ys == xs and bs == b)
                    ok &= iszero(gam(x, a) * w * gam(xs, b) + w)
    exact("O4-Gamma-W-Gamma=-W", ok)
    Q = sp.symbols("Q", real=True)
    q = mu * Q
    gplus = -I * (sp.sqrt(1 - nu**2 * sp.cos(q)**2) + nu * sp.sin(q))
    lim = sp.limit(gplus / (-I * mu), mu, 0, "+")
    exact("O4-g+(mu Q)/(-i mu)->sqrt(1+Q^2)+Q", iszero(lim - (sp.sqrt(1 + Q**2) + Q)))


def illustration(Mb_cb2):
    """Floating-point, labelled; feeds no verdict."""
    import mpmath as mp
    mp.mp.dps = 40
    mu = mp.mpf(3) / 5
    nu = mp.sqrt(1 - mu**2)
    def X(p, k):
        z = p + 1j * k
        om = mp.acos(nu * mp.cos(z))
        return mp.sin(om) - nu * mp.sin(z)
    def cond(k, p):
        x = X(p, k)
        return mp.re(x) - mp.im(x)
    def E(p):
        k0 = -mp.acosh(1 / nu**2) / 2
        k = mp.findroot(lambda kk: cond(kk, p), k0)
        return 2 * mp.re(mp.acos(nu * mp.cos(p + 1j * k)))
    h = mp.mpf("1e-4")
    E0, Eh = E(0), E(h)
    Epp_fd = 2 * (Eh - E0) / h**2
    cb2_fd = E0 * Epp_fd / 4
    Mb, cb2, nusym = Mb_cb2
    musym = list(cb2.free_symbols)[0]
    cb2_exact = sp.N(cb2.subs(musym, sp.Rational(3, 5)), 30)
    lines = ["ILLUSTRATION (floating point, mpmath 40 digits); feeds no verdict.",
             f"mu=3/5: E(0)={mp.nstr(E0, 20)}  acos(nu^2)={mp.nstr(mp.acos(nu**2), 20)}",
             f"finite-difference c_b^2 (h=1e-4) = {mp.nstr(cb2_fd, 15)}",
             f"closed-form c_b^2 = {cb2_exact}",
             f"c_f^2 = {mp.nstr(mp.asin(mu) * nu / mu, 15)}"]
    (ROOT / "reports/2026-11-09--thirring-two-particle-ir-illustration.txt").write_text("\n".join(lines) + "\n")
    return lines


def main():
    check_O1()
    cf2, mu = check_O2()
    pts = [check_O3_eigenvector(sp.Rational(3, 5), "mu=3/5"),
           check_O3_eigenvector(sp.Rational(5, 13), "mu=5/13")]
    check_O3b()
    o3c, Mb_cb2 = check_O3c(cf2, mu)
    check_O4()
    ill = illustration(Mb_cb2)
    paths = ("scripts/verify_thirring_two_particle_ir.py",
             "theory/THIRRING_TWO_PARTICLE_IR_PREFLIGHT_GATE.md",
             "sources/1711.03920v1.pdf", "sources/1804.08508v1.pdf")
    data = dict(family="chi=pi/2, mu in (0,1)", bound_points=pts, O3c=o3c, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    lines += ["", *ill]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
