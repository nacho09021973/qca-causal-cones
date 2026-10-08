#!/usr/bin/env python3
"""Exact countercontrols: stationarity defect is not ensemble-distance error.

Contract: theory/INVERSE_GRAVITY_B0_ACCESS_GATE.md.
Auxiliary two-level family; no computation of the spatial QCA state B.
"""

import sympy as sp


def main():
    for n in (2, 4, 8, 16):
        phase = (sp.Integer(n)**2 + sp.I) / (sp.Integer(n)**2 - sp.I)
        assert sp.simplify(phase * sp.conjugate(phase)) == 1 and phase != 1
        f = sp.simplify(sum(phase**j for j in range(n)) / n)
        error_squared = sp.simplify(f * sp.conjugate(f))
        defect_squared = sp.simplify((phase - 1) * (sp.conjugate(phase) - 1) * error_squared)
        assert error_squared >= sp.Rational(1, 4)
        assert defect_squared <= sp.Rational(4, n**4)
        print(f"PASS auxiliary N={n}: ensemble distance >=1/2, stationarity defect <=2/N^2 (exact)")
    print("VERDICT: STATIONARITY_DEFECT_NOT_AN_ENSEMBLE_ERROR_BOUND")
    print("Scope: auxiliary family only; B-state convergence of fixed QCA NOT_TESTED.")


if __name__ == "__main__":
    main()
