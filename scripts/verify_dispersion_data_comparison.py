#!/usr/bin/env python3
"""Dispersion data comparison (contract theory/DISPERSION_DATA_COMPARISON_GATE.md, commit ad445aa).

Report: reports/2026-11-09--dispersion-data-comparison.md

Exact (SymPy): suprema/zeros of the parent coefficients over the unit sphere or circle
(AM-GM identities), and a lower bound sup|beta| >= 1/9 for L3s4 valid for every 0<a<1.
Decimal (mpmath, 30 digits): physical constants and the derived ell_max, f_min under the
frozen dictionaries D1 and D2, using only the verified bounds of
investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md.
Everything is conditional on H_gamma and D1/D2 (contract Sec. 3).
"""
import hashlib
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--dispersion-data-comparison"
CHECKS = []
mp.mp.dps = 30

HBARC = mp.mpf("1.973269804e-16")      # GeV m
LP = mp.mpf("1.616255e-35")            # m
EPL = mp.mpf("1.22e19")                # GeV (LHAASO value)
C = mp.mpf(299792458)                  # m/s
EQG1 = {"sub": mp.mpf("1.0e20"), "super": mp.mpf("1.1e20")}
EQG2 = {"sub": mp.mpf("6.9e11"), "super": mp.mpf("7.0e11")}
K5 = {"strongest": mp.mpf("7e-35"), "weakest": mp.mpf("2e-34")}   # GeV^-1


def exact(name, cond, detail=""):
    CHECKS.append(dict(name=name, passed=bool(cond), detail=str(detail)))


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


def am_gm_checks():
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    # circle: n1^2 + n2^2 = 1  =>  1/4 - n1^2 n2^2 = (n1^2 - n2^2)^2 / 4
    exact("circle: 1/4 - n1^2 n2^2 = (n1^2-n2^2)^2/4 when n1^2+n2^2=1",
          zero(((n1**2 + n2**2)**2 / 4 - n1**2 * n2**2) - (n1**2 - n2**2)**2 / 4))
    # sphere: (sum n^2)^2 - 3 sigma2 = 1/2 sum (n_i^2 - n_j^2)^2
    s2 = n1**2 * n2**2 + n2**2 * n3**2 + n3**2 * n1**2
    exact("sphere: (sum n^2)^2 - 3 sigma2 = (1/2) sum (n_i^2-n_j^2)^2 >= 0, so sigma2 <= 1/3",
          zero((n1**2 + n2**2 + n3**2)**2 - 3 * s2 - ((n1**2 - n2**2)**2 + (n2**2 - n3**2)**2 + (n3**2 - n1**2)**2) / 2))
    # |n1 n2 n3| <= 3^{-3/2} (AM-GM on n_i^2), attained on body diagonals
    v = 1 / sp.sqrt(3)
    exact("sphere: n1 n2 n3 at body diagonal = 3^{-3/2} (AM-GM bound attained)", zero(v**3 - 3**sp.Rational(-3, 2)))


def l3s4_bound():
    a = sp.symbols("a", positive=True)
    B0 = sp.sqrt(3) * (1 - a**2) / (6 * a)
    B3abs_hi = (2 * a**2 - 1) / (3 * a) * sp.sqrt(3)   # a^2 >= 1/2
    B3abs_lo = (1 - 2 * a**2) / (3 * a) * sp.sqrt(3)   # a^2 <= 1/2
    sup_hi = B0 + B3abs_hi / (3 * sp.sqrt(3))
    sup_lo = B0 + B3abs_lo / (3 * sp.sqrt(3))
    # a in [1/sqrt2, 1): a (sup - 1/9) = (1-a) [sqrt3 (1+a)/6 - (2a+1)/9]
    g_hi = sp.expand(a * (sup_hi - sp.Rational(1, 9)))
    exact("L3s4: a(sup|beta| - 1/9) = (1-a)[sqrt3(1+a)/6 - (2a+1)/9] for a^2>=1/2",
          zero(g_hi - (1 - a) * (sp.sqrt(3) * (1 + a) / 6 - (2 * a + 1) / 9)))
    br = sp.sqrt(3) * (1 + a) / 6 - (2 * a + 1) / 9
    exact("L3s4: bracket linear increasing (slope sqrt3/6 - 2/9 > 0) and positive at a = 1/sqrt2",
          bool(sp.sqrt(3) / 6 - sp.Rational(2, 9) > 0) and bool(br.subs(a, 1 / sp.sqrt(2)) > 0))
    g_lo = sp.expand(a * (sup_lo - sp.Rational(1, 9)))
    dg = sp.diff(g_lo, a)
    exact("L3s4: for a^2<=1/2, a(sup|beta|-1/9) is decreasing in a and positive at a = 1/sqrt2",
          zero(dg - (-sp.sqrt(3) * a / 3 - 4 * a / 9 - sp.Rational(1, 9))) and bool(g_lo.subs(a, 1 / sp.sqrt(2)) > 0))
    return sp.simplify(sup_hi), sp.simplify(sup_lo)


ROWS = {
    # label: (order, sup|coef| exact, has_zero_directions, sign info, c0)
    "L1": (None, None, None, "none", 1),
    "L2": (2, sp.Rational(1, 48), True, "delay (alpha<=0)", 1 / sp.sqrt(2)),
    "L6e": (2, sp.Rational(1, 48), True, "delay", 1 / sp.sqrt(2)),
    "L3": (2, sp.Rational(1, 54), True, "delay", 1 / sp.sqrt(3)),
    "L6c": (2, sp.Rational(1, 512), False, "delay, isotropic", sp.Rational(3, 4)),
    "L6d": (2, sp.Rational(1, 128), False, "delay, isotropic", sp.Rational(3, 4)),
    "L6f": (2, sp.Rational(1, 128), False, "delay, isotropic", sp.Rational(3, 4)),
    "L5a": (1, sp.Rational(1, 9), True, "both signs", 1 / sp.sqrt(3)),
    "L5b": (1, sp.Rational(1, 9), True, "both signs; two Weyl blocks with opposite beta", 1 / sp.sqrt(3)),
    "L4": (1, sp.Rational(1, 9), True, "both signs", 1 / sp.sqrt(3)),
    "L6a": (1, sp.sqrt(15) / 36, True, "both signs", sp.Rational(1, 2)),
    "L6b": (1, sp.sqrt(15) / 18, True, "both signs", sp.Rational(1, 3)),
    "L3s4": (1, sp.Rational(1, 9), "a-dependent", "a-dependent (sup|beta| >= 1/9 for all a)", None),
}


def num(e):
    return mp.mpf(str(sp.N(e, 40)))


def main():
    am_gm_checks()
    sup_hi, sup_lo = l3s4_bound()
    exact("sups used: L2/L6e 1/48 = (1/4)/12; L3 1/54 = (1/3)/18; beta rows 1/9 = (sqrt3/3)(3^{-3/2})",
          zero(sp.Rational(1, 4) / 12 - sp.Rational(1, 48)) and zero(sp.Rational(1, 3) / 18 - sp.Rational(1, 54))
          and zero(sp.sqrt(3) / 3 * 3**sp.Rational(-3, 2) - sp.Rational(1, 9)))
    table = {}
    for lab, (n, sup, zeros, sign, c0) in ROWS.items():
        row = dict(order=n, sup=str(sup), zero_directions=str(zeros), sign=sign)
        if n is None:
            row["D1"] = "UNCONSTRAINED_AT_ALL_ORDERS (omega = |k|)"
        elif n == 2:
            s = num(sup)
            ell = HBARC / (mp.sqrt(2 * s) * EQG2["sub"])
            row["D1"] = dict(ell_max_m=mp.nstr(ell, 4), ell_over_lP=mp.nstr(ell / LP, 4),
                             f_min_Hz=mp.nstr(C / (num(c0) * ell), 4))
        else:
            s = num(sup)
            ell_sub = HBARC / (2 * s * EQG1["sub"])
            ell_sup = HBARC / (2 * s * EQG1["super"])
            row["D1"] = dict(ell_max_m_delay_dir=mp.nstr(ell_sub, 4), ell_max_m_advance_dir=mp.nstr(ell_sup, 4),
                             ell_over_lP_max=mp.nstr(max(ell_sub, ell_sup) / LP, 4))
            row["D2"] = {k: dict(ell_max_m=mp.nstr(Kv * HBARC / s, 4), ell_over_lP=mp.nstr(Kv * HBARC / s / LP, 4))
                         for k, Kv in K5.items()}
            if c0 is not None:
                row["D1"]["f_min_Hz"] = mp.nstr(C / (num(c0) * max(ell_sub, ell_sup)), 4)
            else:
                row["D1"]["note"] = "L3s4: bound uses sup|beta| >= 1/9 (all a); c_0 = a/sqrt3 a-dependent, f_min not given"
        table[lab] = row
    # hypotheses
    order1 = [k for k, v in ROWS.items() if v[0] == 1]
    order2 = [k for k, v in ROWS.items() if v[0] == 2]
    hi = all(mp.mpf(table[k]["D1"]["ell_over_lP_max"]) < 1 for k in order1)
    hk = all(mp.mpf(table[k]["D1"]["ell_over_lP"]) > 1e6 for k in order2)
    exact("Hi-evaluated (recorded, either outcome allowed): order-1 rows need ell_max < ell_P at most sensitive direction (D1)", True,
          {k: table[k]["D1"]["ell_over_lP_max"] for k in order1} | {"Hi": hi})
    exact("Hk-evaluated (recorded, either outcome allowed): order-2 rows allow ell_max > 1e6 ell_P at sup|alpha|", True,
          {k: table[k]["D1"]["ell_over_lP"] for k in order2} | {"Hk": hk})
    data = dict(dictionary="H_gamma with D1/D2 (contract Sec. 3)", constants=dict(hbarc_GeV_m=str(HBARC), l_P_m=str(LP),
                E_Pl_GeV=str(EPL), c=str(C), E_QG1=str(EQG1), E_QG2=str(EQG2), K5=str(K5)),
                L3s4_sup_beta=dict(a2_ge_half=str(sup_hi), a2_le_half=str(sup_lo)), rows=table, Hi=hi, Hk=hk,
                checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (
                    "scripts/verify_dispersion_data_comparison.py", "theory/DISPERSION_DATA_COMPARISON_GATE.md",
                    "investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md")})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2, default=str) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Checks: {passed}/{len(CHECKS)} (SymPy {sp.__version__}; mpmath {mp.__version__}, 30 digits for constants)."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}  {c['detail']}" for c in CHECKS]
    lines += ["", "Per row (conditional on H_gamma; D1 non-birefringent, D2 birefringent):"]
    for k, v in table.items():
        lines.append(f"{k}: order={v['order']} sup={v['sup']} zeros={v['zero_directions']} | D1 {v['D1']}"
                     + (f" | D2 {v['D2']}" if 'D2' in v else ""))
    lines.append(f"Hi={hi}  Hk={hk}")
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
