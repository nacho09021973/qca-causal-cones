#!/usr/bin/env python3
"""Exact checks for the approximate-recovery obstruction of the M=1 Thirring code.

Contract: theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md (commit 61a8215).
Report:   reports/2026-11-09--thirring-approximate-recovery.md

Certifies, with exact SymPy arithmetic in Q(i, sqrt2):
  1. The compact two-particle vector of 1711.03920v1 Eq.(14), as a plane wave
     psi(w,y)=exp(-i p w) f(y), w=x1+x2, y=x1-x2, p=pi/4, satisfies
     U psi = i psi pointwise for U=F J (phase first), mu=3/5, nu=4/5, z=i.
     U commutes with the diagonal translation by one site, under which psi
     picks up the phase exp(-2ip); hence checking every target with w in
     {0,1} (all y) proves the identity on the whole lattice. A larger window
     is checked anyway.
  2. f is antisymmetric under particle exchange.
  3. Isolation: single-particle W(q) has trace 2 nu cos q and det 1, and
     cos^2(p+k)+cos^2(p-k)=1+cos2p cos2k. The written case analysis reduces
     exp(-i(s w(p+k)+r w(p-k)))=i to nu^2(1+cos2p cos2k)=1, impossible at
     p=pi/4 because nu^2 != 1.
  4. Fiber overlaps of the four logical code vectors with f at p=pi/4.

Does NOT certify: the analytic-continuation (Riesz projection) step, the
Riemann-Lebesgue step, absolute continuity of the free fiber spectrum, or the
case analysis behind check 3. Those are written in the report.
No time evolution, no floating point in any certified quantity.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--thirring-approximate-recovery"
CHECKS = []

I = sp.I
MU, NU, Z = sp.Rational(3, 5), sp.Rational(4, 5), sp.I
P0 = sp.pi / 4
R, L = 0, 1  # component index: R == up, L == down (1711.03920v1 p.1 convention)


def exact(name, condition):
    CHECKS.append(dict(name=name, passed=bool(condition)))


def simp(x):
    return sp.nsimplify(sp.simplify(sp.expand_complex(x)))


def iszero(x):
    return sp.simplify(sp.expand_complex(x)) == 0


# ---------- the claimed bound state, 1711.03920v1 p.4 Eq.(14), "+" case ----------
# basis order (a1 a2) = (up up, up down, down up, down down)
BASIS = [(R, R), (R, L), (L, R), (L, L)]
EP = sp.exp(I * P0)
F_REL = {
    1: [-I * EP, 0, 0, 0],
    0: [0, MU / NU, -MU / NU, 0],
    -1: [I * EP, 0, 0, 0],
}


def psi(x1, a1, x2, a2):
    """Plane-wave amplitude exp(-i p0 w) f_{a1 a2}(y)."""
    y, w = x1 - x2, x1 + x2
    if y not in F_REL:
        return sp.Integer(0)
    return sp.exp(-I * P0 * w) * F_REL[y][BASIS.index((a1, a2))]


def J(amp):
    def out(x1, a1, x2, a2):
        v = amp(x1, a1, x2, a2)
        return Z * v if (x1 == x2 and a1 != a2) else v
    return out


def W_preimages(x, a):
    """(coefficient, source site, source component) with (W phi)(x,a)=sum c phi(src)."""
    if a == R:
        return ((NU, x - 1, R), (-I * MU, x, L))
    return ((-I * MU, x, R), (NU, x + 1, L))


def F(amp):
    def out(x1, a1, x2, a2):
        s = 0
        for c1, y1, b1 in W_preimages(x1, a1):
            for c2, y2, b2 in W_preimages(x2, a2):
                s += c1 * c2 * amp(y1, b1, y2, b2)
        return s
    return out


def check_eigenvector():
    U_psi = F(J(psi))
    ok_all, ok_core = True, True
    for x1 in range(-6, 7):
        for x2 in range(-6, 7):
            for a1, a2 in BASIS:
                good = iszero(U_psi(x1, a1, x2, a2) - I * psi(x1, a1, x2, a2))
                ok_all &= good
                if x1 + x2 in (0, 1):
                    ok_core &= good
    exact("eq14-eigenvector-all-targets-w-in-{0,1}", ok_core)
    exact("eq14-eigenvector-window-|x|<=6", ok_all)
    exact("eigenvalue-equals-exp(2ip0)-equals-z", iszero(sp.exp(2 * I * P0) - Z))
    exact("diagonal-translation-phase-exp(-2ip0)",
          all(iszero(psi(x1 + 1, a1, x2 + 1, a2) - sp.exp(-2 * I * P0) * psi(x1, a1, x2, a2))
              for x1 in range(-3, 4) for x2 in range(-3, 4) for a1, a2 in BASIS))


def check_antisymmetry():
    swap = [0, 2, 1, 3]
    exact("f-antisymmetric-E f(-y)=-f(y)",
          all(iszero(F_REL[-y][swap[j]] + F_REL[y][j]) for y in (-1, 0, 1) for j in range(4)))


def check_isolation():
    q, p, k = sp.symbols("q p k", real=True)
    Wq = sp.Matrix([[NU * sp.exp(I * q), -I * MU], [-I * MU, NU * sp.exp(-I * q)]])
    exact("W(q)-det-1", iszero(Wq.det() - 1))
    exact("W(q)-trace-2nu-cos-q", iszero(sp.expand_complex(Wq.trace()) - 2 * NU * sp.cos(q)))
    ident = sp.cos(p + k) ** 2 + sp.cos(p - k) ** 2 - 1 - sp.cos(2 * p) * sp.cos(2 * k)
    exact("cos-square-sum-identity", sp.simplify(sp.expand_trig(ident)) == 0)
    exact("cos2p-zero-at-p0", sp.cos(2 * P0) == 0)
    exact("nu-squared-not-one", NU ** 2 != 1)


def code_vectors():
    """Logical inputs ab: A in mode a of (R@0, L@1), B in mode b of (R@1, L@0)."""
    A = [(0, R), (1, L)]
    Bm = [(1, R), (0, L)]
    vecs = {}
    for a in range(2):
        for b in range(2):
            (xa, ca), (xb, cb) = A[a], Bm[b]
            vecs[f"{a}{b}"] = {(xa, ca, xb, cb): 1 / sp.sqrt(2), (xb, cb, xa, ca): -1 / sp.sqrt(2)}
    return vecs


def check_overlaps():
    norm_f = sum(sp.Abs(c) ** 2 for y in F_REL for c in F_REL[y])
    norm_f = simp(norm_f)
    exact("norm-f-squared-25/8", norm_f == sp.Rational(25, 8))
    res = {}
    for name, v in code_vectors().items():
        # fiber component b_p(y)=sum_w exp(i p w) v(w,y); <f,b_p> = sum conj(psi) v
        ov = simp(sum(sp.conjugate(psi(*key)) * c for key, c in v.items()))
        res[name] = ov
    exact("overlap-00-equals-minus-i-sqrt2", iszero(res["00"] + I * sp.sqrt(2)))
    # Run 1 (dd4e547) wrongly expected zero for 01 and 10: those inputs are
    # on-site opposite-component pairs and meet f(0). Corrected after that run;
    # the failed record is kept as ...-failed-run-1.{txt,json}. Not used for the verdict.
    exact("overlap-01-equals-3sqrt2/4", iszero(res["01"] - 3 * sp.sqrt(2) / 4))
    exact("overlap-10-equals-minus-3i-sqrt2/4", iszero(res["10"] + 3 * I * sp.sqrt(2) / 4))
    exact("overlap-11-zero", iszero(res["11"]))
    weight = simp(sp.Abs(res["00"]) ** 2 / norm_f)
    exact("fiber-weight-00-at-p0-equals-16/25", weight == sp.Rational(16, 25))
    return {k: str(v) for k, v in res.items()}, str(norm_f), str(weight)


def main():
    check_eigenvector()
    check_antisymmetry()
    check_isolation()
    overlaps, norm_f, weight = check_overlaps()
    paths = ("scripts/verify_thirring_approximate_recovery.py",
             "theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md",
             "sources/1711.03920v1.pdf")
    data = dict(parameters=dict(mu="3/5", nu="4/5", z="i", p0="pi/4", M=1),
                overlaps_with_f=overlaps, norm_f_squared=norm_f,
                fiber_weight_00_at_p0=weight, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__}).",
             f"Overlaps <f, code_ab>: {overlaps}; ||f||^2={norm_f}; fiber weight of 00 at p0: {weight}"]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
