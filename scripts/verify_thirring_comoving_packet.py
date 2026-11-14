#!/usr/bin/env python3
"""Exact checks for the Thirring co-moving packet gate.

Contract: theory/THIRRING_COMOVING_PACKET_GATE.md (frozen at dca5ebc).
Report:   reports/2026-11-14--thirring-comoving-packet.md

Conventions and helpers imported read-only from
scripts/verify_thirring_low_energy_packet.py (contract 2: onepart,
eigenfunction, F_op, J_op, BASIS, iszero) and
scripts/verify_thirring_flavour_packet.py (eigenfunction_pm, check_F1,
check_F3_F4). Neither file is modified; their SHA256 are recorded.
In those helpers Z = I means chi = pi/2 (the phase applied is conj(Z) = -i).

Certified (exact SymPy):
  E1  (+,+) four-plane-wave function of contract 2 is an exact lattice
      eigenvector of U at a co-moving algebraic pair, both momenta positive
      and distinct (e^{iq1} = (4+3i)/5, e^{iq2} = (12+5i)/13), mu = 3/5,
      chi = pi/2 and chi = 0 (T = 1 there); |T| = 1.
  E2  (+,-) four-plane-wave function of the flavour gate, same pair with the
      second momentum shifted by pi (e^{iq2'} = -(12+5i)/13): exact
      eigenvector, chi = pi/2 and chi = 0; |T_-| = 1.
  R   reused checks re-run: F1 (g_-(q+pi) = -g_+(q)) and F3/F4 (code algebra
      and form of V given the two sector limits; label-agnostic finite model).
  M   supports for 0 < mu < 1/10, delta = mu^(3/2): slow in mu[1-m, 1+m],
      fast in mu[3-m, 3+m], m = sqrt(mu): positive, inside (0, 4mu),
      disjoint; pi-shifted copies disjoint.
  V   velocities: omega'(q)^2 = nu^2 s/(mu^2 + nu^2 s), s = sin^2 q, increasing
      in s; rational bounds omega'^2 >= 87/100 on the fast support,
      omega'^2 <= 16/25 on the slow support, so v_f - v_s >= 13/100; at
      T = 20L the incoming y-centre is <= -3L/5 and the outgoing >= +3L/5.
  C   limiting gate at chi = pi/2: T_+ = (a_f + z a_s)/(a_s + z a_f),
      T_- = (a_f - z a_s)/(z a_f - a_s), a_f = sqrt10 + 3, a_s = sqrt2 + 1;
      (T_+ + T_-)/2 = alpha(r_co), (T_+ - T_-)/2 = beta(r_co) with
      r_co = a_f/a_s; unitary; beta != 0; concurrence of V|AB> > 0.
  A1  alpha(r) = z(r^2-1)/(z^2 r^2-1), beta(r) = r(z^2-1)/(z^2 r^2-1) from T_+-
      with r = a1/a2 (symbolic).
  A2  Delta = (1 + alpha^2 - beta^2)/(2 alpha) = (z^2+1)/(2z), independent of
      r; 1 + alpha^2 - beta^2 = (z^2+1)(r^2-1)/(z^2 r^2-1).
  A3  V_12(x) V_13(xy) V_23(y) = V_23(y) V_13(xy) V_12(x) on (C^2)^(x3), all
      64 entries, symbolic in x, y, z; and at z = -i.
  A4  Rcheck = P V: Rcheck_12(x) Rcheck_23(xy) Rcheck_12(y) =
      Rcheck_23(y) Rcheck_12(xy) Rcheck_23(x), symbolic and at z = -i.
  A5  diagnostic only: matchgate determinants (det of the {00,11} block vs
      det of the {01,10} block) for V, P V and fSWAP V, symbolic in z and
      at z = -i. Results are recorded, not asserted, except the algebraic
      identities used to state them.

Not certified (written proof in the report): the packet/scattering bridge
in the co-moving geometry, the U^2 admission argument for K = 1, 3, and the
verdict. Part A says nothing about physical three-packet factorization or
about graded versus ungraded tensor structure.
"""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-14--thirring-comoving-packet"


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c2 = _load("c2", "scripts/verify_thirring_low_energy_packet.py")
fl = _load("fl", "scripts/verify_thirring_flavour_packet.py")
F_op, J_op, BASIS, iszero = c2.F_op, c2.J_op, c2.BASIS, c2.iszero
I = sp.I
CHECKS = []
DIAG = {}


def exact(name, cond):
    CHECKS.append(dict(name=name, passed=bool(cond)))


def ccancel(x):
    return sp.cancel(sp.expand(x))


# ---------------- E1 / E2 ----------------
def eig_check(tag, builder, z1, z2):
    MU, NU = sp.Rational(3, 5), sp.Rational(4, 5)
    out = {}
    for chi_tag, Z in (("chi=pi/2", I), ("chi=0", sp.Integer(1))):
        psi, lam, T = builder(z1, z2, MU, NU, Z)
        Upsi = F_op(J_op(psi, Z), MU, NU)
        ok, nonzero = True, False
        for x1 in range(-3, 4):
            for x2 in range(-3, 4):
                for a1, a2 in BASIS:
                    ok &= iszero(Upsi(x1, a1, x2, a2) - lam * psi(x1, a1, x2, a2))
                    nonzero |= not iszero(psi(x1, a1, x2, a2))
        exact(f"{tag}-{chi_tag}-eigenfunction", ok and nonzero)
        exact(f"{tag}-{chi_tag}-|T|=1", iszero(sp.Abs(T)**2 - 1))
        if Z == 1:
            exact(f"{tag}-chi=0-T=1", iszero(T - 1))
        out[chi_tag] = str(sp.nsimplify(sp.simplify(T)))
    return out


def check_E():
    z1 = (4 + 3 * I) / 5          # q1 ~ 0.6435 > 0 (fast, particle 1)
    z2 = (12 + 5 * I) / 13        # q2 ~ 0.3948 > 0 (slow), q2 != q1
    exact("E-pair-co-moving(Im z1>0, Im z2>0, z1!=z2)",
          sp.im(z1) > 0 and sp.im(z2) > 0 and not iszero(z1 - z2))
    r1 = eig_check("E1-(+,+)", c2.eigenfunction, z1, z2)
    r2 = eig_check("E2-(+,-)", fl.eigenfunction_pm, z1, -z2)
    return {"(+,+)": r1, "(+,-)": r2}


# ---------------- R (reused, read-only) ----------------
def check_R():
    n0 = len(fl.CHECKS)
    fl.check_F1()
    fl.check_F3_F4(sp.Symbol("Tp"), sp.Symbol("Tm"))
    for c in fl.CHECKS[n0:]:
        exact("R-reused-" + c["name"], c["passed"])


# ---------------- M ----------------
def check_M():
    m = sp.symbols("m", positive=True)
    mb = 1 / sp.sqrt(10)
    conds = {"slow-positive(1-m>0)": 1 - m,
             "fast-inside-4mu(4-(3+m)>0)": 4 - (3 + m),
             "disjoint((3-m)-(1+m)>0)": (3 - m) - (1 + m)}
    for k, f in conds.items():
        exact(f"M-{k}", bool(f.subs(m, mb) > 0) and sp.diff(f, m) < 0)
    exact("M-pi-shift-disjoint(8mu<pi)", bool(8 * sp.Rational(1, 10) < sp.pi))


# ---------------- V ----------------
def check_V():
    q, mu = sp.symbols("q mu", positive=True)
    s = sp.symbols("s", positive=True)
    nu2 = 1 - mu**2
    lhs = nu2 * sp.sin(q)**2 / (1 - nu2 * sp.cos(q)**2)
    rhs = (nu2 * s / (mu**2 + nu2 * s)).subs(s, sp.sin(q)**2)
    exact("V-omega'^2=nu^2 s/(mu^2+nu^2 s)",
          iszero(sp.simplify((lhs - rhs).rewrite(sp.cos))))
    exact("V-increasing-in-s",
          iszero(sp.diff(nu2 * s / (mu**2 + nu2 * s), s) - mu**2 * nu2 / (mu**2 + nu2 * s)**2))
    mb = sp.Rational(317, 1000)
    exact("V-1/sqrt10<317/1000", mb**2 > sp.Rational(1, 10))
    mu_max = sp.Rational(1, 10)
    Kf_min, Kf_max = 3 - mb, 3 + mb
    Ks_max = 1 + mb
    # fast: sin q >= q(1 - q^2/6), q = mu K, K >= Kf_min, mu K <= mu_max Kf_max, nu^2 >= 99/100
    rho_f = sp.Rational(99, 100) * (Kf_min * (1 - (mu_max * Kf_max)**2 / 6))**2
    vf2 = rho_f / (1 + rho_f)
    exact("V-fast-omega'^2>=87/100", vf2 >= sp.Rational(87, 100))
    # slow: nu^2 s <= mu^2 K^2, x/(mu^2+x) increasing => omega'^2 <= K^2/(1+K^2)
    vs2 = Ks_max**2 / (1 + Ks_max**2)
    exact("V-slow-omega'^2<=16/25", vs2 <= sp.Rational(16, 25))
    exact("V-sqrt(87/100)>93/100", sp.Rational(93, 100)**2 < sp.Rational(87, 100))
    dv = sp.Rational(93, 100) - sp.Rational(4, 5)
    exact("V-v_f-v_s>=13/100", dv == sp.Rational(13, 100))
    exact("V-incoming-y-centre<=2L-20L*dv=-3L/5", 2 - 20 * dv == -sp.Rational(3, 5))
    exact("V-outgoing-y-centre>=-2L+20L*dv=+3L/5", -2 + 20 * dv == sp.Rational(3, 5))
    vf_lim = sp.Rational(3) / sp.sqrt(10)
    vs_lim = 1 / sp.sqrt(2)
    exact("V-limit-v_f-v_s>24/100", bool(vf_lim - vs_lim > sp.Rational(24, 100)))
    DIAG["velocity_bounds"] = dict(fast_omega_sq_lower=str(vf2), fast_float=float(sp.sqrt(vf2)),
                                   slow_omega_sq_upper=str(vs2), slow_float=float(sp.sqrt(vs2)),
                                   limit_dv=float(sp.N(vf_lim - vs_lim, 20)))


# ---------------- family ----------------
def alpha_beta(r, z):
    return z * (r**2 - 1) / (z**2 * r**2 - 1), r * (z**2 - 1) / (z**2 * r**2 - 1)


def Vmat(r, z):
    al, be = alpha_beta(r, z)
    return sp.Matrix([[1, 0, 0, 0], [0, al, be, 0], [0, be, al, 0], [0, 0, 0, 1]])


SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
FSWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]])
I2 = sp.eye(2)


def kron(A, B):
    return sp.kronecker_product(A, B)


def is_zero_matrix(M):
    return all(ccancel(e) == 0 for e in M)


# ---------------- C ----------------
def check_C():
    af = sp.sqrt(10) + 3          # a(3) = sqrt(1+9) + 3
    as_ = sp.sqrt(2) + 1          # a(1)
    z = -I
    Tp = (af + z * as_) / (as_ + z * af)
    Tm = (af - z * as_) / (z * af - as_)
    r = af / as_
    al, be = alpha_beta(r, z)
    exact("C-(T++T-)/2=alpha(r_co)", iszero((Tp + Tm) / 2 - al))
    exact("C-(T+-T-)/2=beta(r_co)", iszero((Tp - Tm) / 2 - be))
    exact("C-|T+|=|T-|=1", iszero(sp.Abs(Tp)**2 - 1) and iszero(sp.Abs(Tm)**2 - 1))
    exact("C-alpha=i(r^2-1)/(r^2+1)", iszero(al - I * (r**2 - 1) / (r**2 + 1)))
    exact("C-beta=2r/(1+r^2)", iszero(be - 2 * r / (1 + r**2)))
    exact("C-unitary(|al|^2+|be|^2=1, al conj(be)+be conj(al)=0)",
          iszero(sp.Abs(al)**2 + sp.Abs(be)**2 - 1)
          and iszero(al * sp.conjugate(be) + be * sp.conjugate(al)))
    exact("C-beta>0", bool(sp.N(be, 30) > 0))
    conc = 2 * sp.Abs(al) * sp.Abs(be)
    exact("C-concurrence(V|AB>)>0", bool(sp.N(conc, 30) > 0))
    DIAG["limit"] = dict(r_co=str(sp.radsimp(r)), r_co_float=float(sp.N(r, 20)),
                         alpha=str(sp.radsimp(al)), alpha_float_im=float(sp.N(sp.im(al), 20)),
                         beta=str(sp.radsimp(be)), beta_float=float(sp.N(be, 20)),
                         concurrence_float=float(sp.N(conc, 20)))


# ---------------- A ----------------
def check_A():
    a1, a2, r, x, y = sp.symbols("a1 a2 r x y", positive=True)
    z = sp.symbols("z")
    Tp = (a1 + z * a2) / (a2 + z * a1)
    Tm = (a1 - z * a2) / (z * a1 - a2)
    al, be = alpha_beta(a1 / a2, z)
    exact("A1-alpha=(T++T-)/2", ccancel((Tp + Tm) / 2 - al) == 0)
    exact("A1-beta=(T+-T-)/2", ccancel((Tp - Tm) / 2 - be) == 0)
    al, be = alpha_beta(r, z)
    exact("A2-Delta=(z^2+1)/(2z)", ccancel((1 + al**2 - be**2) / (2 * al) - (z**2 + 1) / (2 * z)) == 0)
    exact("A2-1+al^2-be^2=(z^2+1)(r^2-1)/(z^2r^2-1)",
          ccancel(1 + al**2 - be**2 - (z**2 + 1) * (r**2 - 1) / (z**2 * r**2 - 1)) == 0)

    P23 = kron(I2, SWAP)

    def R12(t, zz):
        return kron(Vmat(t, zz), I2)

    def R23(t, zz):
        return kron(I2, Vmat(t, zz))

    def R13(t, zz):
        return P23 * R12(t, zz) * P23

    def C12(t, zz):
        return kron(SWAP * Vmat(t, zz), I2)

    def C23(t, zz):
        return kron(I2, SWAP * Vmat(t, zz))

    res = {}
    for ztag, zz in (("symbolic", z), ("z=-i", -I)):
        yb = R12(x, zz) * R13(x * y, zz) * R23(y, zz) - R23(y, zz) * R13(x * y, zz) * R12(x, zz)
        ok3 = is_zero_matrix(yb)
        br = C12(x, zz) * C23(x * y, zz) * C12(y, zz) - C23(y, zz) * C12(x * y, zz) * C23(x, zz)
        ok4 = is_zero_matrix(br)
        exact(f"A3-YBE-R-form-{ztag}", ok3)
        exact(f"A4-braid-Rcheck=PV-{ztag}", ok4)
        res[ztag] = dict(A3=ok3, A4=ok4)

    # A5 diagnostic: matchgate determinants
    def dets(M):
        A = sp.Matrix([[M[0, 0], M[0, 3]], [M[3, 0], M[3, 3]]])
        B = sp.Matrix([[M[1, 1], M[1, 2]], [M[2, 1], M[2, 2]]])
        return ccancel(A.det()), ccancel(B.det())

    diag = {}
    for name, M in (("V", Vmat(r, z)), ("PV", SWAP * Vmat(r, z)), ("fSWAP V", FSWAP * Vmat(r, z))):
        dA, dB = dets(M)
        dA0, dB0 = ccancel(dA.subs(z, -I)), ccancel(dB.subs(z, -I))
        diag[name] = dict(detA=str(dA), detB=str(sp.factor(dB)),
                          detA_at_z=str(dA0), detB_at_z_minus_i=str(dB0),
                          equal_at_z_minus_i=bool(ccancel(dA0 - dB0) == 0))
    dA, dB = dets(SWAP * Vmat(r, z))
    exact("A5-identity-detA(PV)=1", ccancel(dA - 1) == 0)
    exact("A5-identity-detB(PV)=1-(z^2+1)(r^2-1)/(z^2r^2-1)",
          ccancel(dB - 1 + (z**2 + 1) * (r**2 - 1) / (z**2 * r**2 - 1)) == 0)
    DIAG["A5_matchgate_determinants"] = diag
    DIAG["A3_A4"] = res


def main():
    eig = check_E()
    check_R()
    check_M()
    check_V()
    check_C()
    check_A()
    paths = ("scripts/verify_thirring_comoving_packet.py",
             "scripts/verify_thirring_low_energy_packet.py",
             "scripts/verify_thirring_flavour_packet.py",
             "theory/THIRRING_COMOVING_PACKET_GATE.md", "sources/1711.03920v1.pdf")
    data = dict(T_at_check_points=eig, diagnostics=DIAG, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2, default=str) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    lim = DIAG["limit"]
    lines += ["", f"r_co = {lim['r_co']} ~ {lim['r_co_float']:.6f}",
              f"alpha = {lim['alpha']} ~ i*{lim['alpha_float_im']:.6f}",
              f"beta = {lim['beta']} ~ {lim['beta_float']:.6f}; concurrence ~ {lim['concurrence_float']:.6f}",
              "A5 diagnostic (decides nothing):"]
    for k, v in DIAG["A5_matchgate_determinants"].items():
        lines.append(f"  {k}: detA = {v['detA']}, detB = {v['detB']}; at z=-i: "
                     f"detA = {v['detA_at_z']}, detB = {v['detB_at_z_minus_i']}, equal = {v['equal_at_z_minus_i']}")
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
