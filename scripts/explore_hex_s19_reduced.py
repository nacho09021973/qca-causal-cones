"""EXPLORATORY, not a certificate. M1-B19 of HEX_SUPREMUM (contract
theory/HEX_SUPREMUM_GATE.md, preregistered at 86573ca, Sec. 4: numerics may
guide the search for a witness or a certificate; no numerical result enters a
verdict).

Builds the reduced S19 saturation system of verify_hex_supremum_b19.py (18
real parameters after the exact linear reductions L1 + L2 + L3; 730 real
quadratic unitarity equations) and minimises the sum of squares from random
starts with scipy least_squares. It only says where to look: a residual near
0 suggests looking for an exact witness; a minimum bounded away from 0 in
every run suggests looking for an exact infeasibility certificate.

  python -B scripts/explore_hex_s19_reduced.py [n_starts] [seed]

Runs (recorded by hand below, wall time included):
- see the report reports/2026-11-03--hex-supremum.md, Sec. on M1-B19.
"""
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_hex_supremum_b19 as b  # read-only


def build():
    pts, verts, normals, r = b.m1.hexagon(2 * b.m1.G1)
    zs, ws, A, Abar = b.unknowns(len(pts))
    e3 = b.linear_system(pts, normals[:3], r, 2, A, moments=True, Abar=Abar)
    t, P, Q = b.parametrize(e3, zs, ws)
    eqs = b.unitarity_equations(pts, P, Q)
    return t, eqs


def main():
    n_starts = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    t0 = time.time()
    t, eqs = build()
    F = sp.lambdify([t], sp.Matrix(eqs), "numpy")
    J = sp.lambdify([t], sp.Matrix(eqs).jacobian(t), "numpy")
    print(f"built: {len(t)} params, {len(eqs)} equations, {time.time() - t0:.1f} s")
    rng = np.random.default_rng(seed)
    best = []
    for k in range(n_starts):
        x0 = rng.normal(scale=0.5, size=len(t))
        res = least_squares(lambda x: np.asarray(F(x), float).ravel(), x0,
                            jac=lambda x: np.asarray(J(x), float), xtol=1e-15, ftol=1e-15, gtol=1e-15,
                            max_nfev=2000)
        best.append((float(np.sum(res.fun ** 2)), res.x))
    best.sort(key=lambda p: p[0])
    vals = [v for v, _ in best]
    print(f"starts {n_starts}, seed {seed}, total {time.time() - t0:.1f} s")
    print("smallest sums of squares:", ", ".join(f"{v:.3e}" for v in vals[:10]))
    print("quantiles (0, 0.1, 0.5):", ", ".join(f"{np.quantile(vals, q):.3e}" for q in (0, 0.1, 0.5)))
    print("best point:", np.array2string(best[0][1], precision=6, max_line_width=200))


if __name__ == "__main__":
    main()
