#!/usr/bin/env python3
"""Exact certificate for the DISPERSION_L3_ROW gate.
Contract: theory/DISPERSION_L3_ROW_GATE.md (preregistration commit d3868fa).

Adds row L3 of C_ACROSS_LATTICES (standard d = 3 Weyl battery: cases A+, B+,
A-, B- of verify_weyl_dirac_gate.verify_case) to the dispersion corrections
table, with the parent's helpers imported read-only from
scripts/verify_dispersion_corrections_gate.py (no reviewed byte changed).
For comparison (hypotheses HL3b, HL3c) the parent's rows printed "L4"
(CJWW (5.12), walk1()) and L5a are recomputed here with the parent's own row
setup (verify_dispersion_corrections_gate.py l. 565-576).
Fails closed: any failed check or exception exits nonzero.
Run from the repository root:  python3 -B scripts/verify_dispersion_L3_row_gate.py
"""
import sys
import time
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_dispersion_corrections_gate as D   # reviewed, read-only
import verify_c_across_lattices_gate as P        # reviewed, read-only
import verify_weyl_dirac_gate as WD              # reviewed, read-only
import verify_directional_saturation as DS       # reviewed, read-only

R3 = sp.sqrt(3)
START = time.time()
N = 4                                            # parent's degree for d = 3 rows
GENS3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
KS = sp.symbols("k1:4", real=True)
NS = sp.symbols("n1:4", real=True)


def analyse(label, symbol, zs, gens, sigma, results, groups):
    """The parent's generic s = 2 branch (Part 2), applied to one symbol."""
    support = P.laurent_support(symbol, zs)
    cart = {h: sum((a * sp.Matrix(g) for a, g in zip(h, gens)), sp.zeros(3, 1)) for h in support}
    L = sp.radsimp(sp.simplify(max((sp.sqrt((v.T * v)[0]) for v in cart.values()), key=lambda x: float(x))))
    print(f"-- {label} (s = {symbol.rows}, d = 3, scale = {L}, N = {N})  [elapsed {time.time() - START:.0f} s]",
          flush=True)
    Uk = D.taylor_symbol(support, gens, L, sigma, KS, N)
    s1 = D.trunc(Uk.trace(), KS, N)
    s2 = D.trunc(Uk.det(), KS, N)
    D.analyse_block(label, s1, s2, KS, NS, N, 1, results, 1 / R3)
    members, non_lattice = D.walk_group(symbol, zs, gens, D.point_group("cubic"))
    groups[label] = members
    print(f"  {label}: G_walk = {D.describe_group(members, 3)}; non-lattice skipped: {len(non_lattice)}")
    return support


def same_pair(x, y, results):
    return (D.czero(results[x]["beta"] - results[y]["beta"], NS)
            and D.czero(results[x]["alpha"] - results[y]["alpha"], NS))


def main():
    results, groups = {}, {}
    zs = sp.symbols("w1:4")
    cases = {}
    print("== Part 1: row L3 symbols imported read-only (contract Sec. 1)")
    for chi in (1, -1):
        sym, scalar = WD.published_symbol(3, chi, zs)
        s = "+" if chi == 1 else "-"
        cases[f"L3 A{s}"] = (sym, scalar)
        cases[f"L3 B{s}"] = (sym.T, scalar)
    C = [(z + 1 / z) / 2 for z in zs]
    S = [(z - 1 / z) / (2 * sp.I) for z in zs]
    for label, (sym, scalar) in cases.items():
        chi = 1 if "+" in label else -1
        D.record(f"{label}: unitary as a Laurent matrix",
                 P.is_zero_matrix(sym * P.laurent_adjoint(sym, zs) - sp.eye(2)))
        # HL3a
        D.record(f"{label}: det U = 1 (Laurent identity)", sp.expand(sp.together(sym.det() - 1)) == 0)
        D.record(f"{label}: tr U = 2 (ccc + chi sss), chi = {chi} (HL3a)",
                 sp.expand(sp.together(sym.trace() - 2 * (C[0] * C[1] * C[2] + chi * S[0] * S[1] * S[2]))) == 0)
        sup = P.laurent_support(sym, zs)
        D.record(f"{label}: Fourier support is {{+-1}}^3", set(sup) == {(a, b, c) for a in (1, -1)
                                                                       for b in (1, -1) for c in (1, -1)})

    print("== Part 2: node branch expansions (contract Sec. 2)")
    for label, (sym, _) in cases.items():
        analyse(label, sym, zs, GENS3, +1, results, groups)
    # Comparison rows with the parent's own setup (l. 565-576).
    analyse("parent L4 = CJWW (5.12)", D.laurent_matrix_from_p(DS.walk1()), DS.Z, GENS3, +1, results, groups)
    n_parent_before = len(P.CHECKS)
    symbol, zsa, _, gens_a = P.row_L5a()
    D.record("parent row constructor row_L5a passes its own checks (as the parent requires)",
             all(ok for _, ok, _ in P.CHECKS[n_parent_before:]), f"{len(P.CHECKS) - n_parent_before} constructor checks")
    analyse("parent L5a", symbol, zsa, gens_a, -1, results, groups)

    # Prerequisites: every asserted check so far (repair 1 of the gpt-6.1-sol review).
    prereq_failed = [c for c in D.CHECKS if not c[1]]
    certified = not prereq_failed

    def verdict(ok):
        if not certified:
            return "NOT CERTIFIED (failed prerequisite checks)"
        if ok is None:
            return "UNDECIDED"
        return "CONFIRMED" if ok else "REFUTED"

    print("== Part 3: hypotheses (contract Sec. 3)")
    hb = all(same_pair(x, "parent L4 = CJWW (5.12)", results) and groups[x] == groups["parent L4 = CJWW (5.12)"]
             for x in ("L3 A+", "L3 B+"))
    print(f"  HL3b (A+, B+ share (beta, alpha) and G_walk with CJWW (5.12)): {verdict(hb)}")
    hc_sign = all(D.czero(results[x]["beta"] + results["L3 A+"]["beta"], NS)
                  and D.czero(results[x]["alpha"] - results["L3 A+"]["alpha"], NS) for x in ("L3 A-", "L3 B-"))
    hc_l5a = all(same_pair(x, "parent L5a", results) for x in ("L3 A-", "L3 B-"))
    hc = hc_sign and hc_l5a
    print(f"  HL3c (A-, B-: beta opposite to A+, same alpha: {hc_sign}; same (beta, alpha) as L5a: {hc_l5a}): "
          f"{verdict(hc)}")
    hd = all(results[x]["lowest_aniso"] for x in cases)
    print(f"  HL3d (lowest correction anisotropic in all four cases): {verdict(hd)}")
    signs = [results[x]["alpha0"].is_negative for x in cases]
    he = None if any(v is None for v in signs) else all(signs)
    print(f"  HL3e (alpha_0 < 0 in all four cases): {verdict(he)}; "
          f"alpha_0 = {[results[x]['alpha0'] for x in cases]}")
    for x in cases:
        r = results[x]
        print(f"  {x}: lowest = {r['lowest']}; beta = {r['beta0']} + ({r['beta3']}) n1 n2 n3; "
              f"{r['pattern'].split('; ')[1]}")
    # Contract Sec. 4 verdict (repair 2): every quantity of Sec. 2 except the two OPEN ones.
    missing = [x for x in cases
               if any(results[x].get(key) is None for key in ("beta", "alpha", "alpha0", "lowest"))
               or x not in groups
               or not D.czero(results[x]["beta_residual"], NS) or not D.czero(results[x]["cubic_residual"], NS)]
    if not certified:
        row_verdict = "L3_DISPERSION_OPEN_FAILED_CHECKS"
    elif missing:
        row_verdict = "L3_DISPERSION_OPEN_QUANTITIES_MISSING_" + "_".join(m.replace(" ", "") for m in missing)
    else:
        row_verdict = "L3_DISPERSION_COMPLETE"
    print(f"  Row verdict (contract Sec. 4): {row_verdict} "
          f"(V_grp^max and scale of validity OPEN, as the contract states)")
    failed = [c for c in D.CHECKS if not c[1]]
    print(f"{len(D.CHECKS) - len(failed)}/{len(D.CHECKS)} checks passed (dispersion L3 row gate; "
          f"includes the parent's per-row checks of the comparison rows).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
