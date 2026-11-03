"""EXPLORATORY search, not a certificate. M1-B19 of HEX_SUPREMUM (contract
theory/HEX_SUPREMUM_GATE.md, preregistered at 86573ca, Sec. 4: numerics may
guide the search for a certificate; only the exact check in
verify_hex_supremum_b19.py can enter a verdict).

Question it guides: is there a real linear combination p = sum_i lam_i f_i of
the reduced S19 equations f_i (18 real parameters t, quadratic) whose unique
Gram matrix G in the basis (1, t) is positive definite? Then p >= c > 0 on
R^18 while p = 0 on any solution: the system has no real solution, with a
certificate -1 = sum q_j^2 + sum h_i f_i, h_i constant (contract Sec. 4 (ii)).

Method: G(mu) = sum_k mu_k G_k over a basis of the span of the f_i (computed
in floating point here only to find a candidate); maximise lambda_min(G(mu))
subject to trace G(mu) = 1 with SLSQP from several starts. Output: the best
lambda_min and the candidate mu written to an .npy file for the exact step.

  python -B scripts/explore_hex_s19_certificate.py <out.npy> [n_starts]
"""
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import explore_hex_s19_reduced as ex  # read-only


def gram_of(poly, t):
    """Unique symmetric Gram matrix of a quadratic polynomial in basis (1, t)."""
    n = len(t)
    G = sp.zeros(n + 1)
    for mon, c in sp.Poly(poly, *t).terms():
        nz = [i for i, p in enumerate(mon) if p]
        if not nz:
            G[0, 0] += c
        elif len(nz) == 1 and mon[nz[0]] == 1:
            G[0, nz[0] + 1] += c / 2
            G[nz[0] + 1, 0] += c / 2
        elif len(nz) == 1:
            G[nz[0] + 1, nz[0] + 1] += c
        else:
            i, j = nz
            G[i + 1, j + 1] += c / 2
            G[j + 1, i + 1] += c / 2
    return G


def main():
    out = sys.argv[1]
    n_starts = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    t0 = time.time()
    t, eqs = ex.build()
    Gs = np.array([np.array(gram_of(e, t).evalf(), dtype=float) for e in eqs])
    flat = Gs.reshape(len(eqs), -1)
    U, S, Vt = np.linalg.svd(flat, full_matrices=False)
    k = int((S > 1e-9 * S[0]).sum())
    basis = Vt[:k].reshape(k, *Gs.shape[1:])
    basis = 0.5 * (basis + basis.transpose(0, 2, 1))
    tr = np.array([np.trace(B) for B in basis])
    print(f"built {len(eqs)} equations, span dim {k}, {time.time() - t0:.1f} s")

    def G(mu):
        return np.tensordot(mu, basis, axes=1)

    def f(mu):
        w, V = np.linalg.eigh(G(mu))
        v = V[:, 0]
        return -w[0], -np.array([v @ B @ v for B in basis])

    rng = np.random.default_rng(0)
    best = (-np.inf, None)
    for s in range(n_starts):
        mu0 = rng.normal(size=k)
        mu0 /= mu0 @ tr if abs(mu0 @ tr) > 1e-6 else 1.0
        res = minimize(f, mu0, jac=True, method="SLSQP",
                       constraints=[{"type": "eq", "fun": lambda m: m @ tr - 1, "jac": lambda m: tr}],
                       options={"maxiter": 2000, "ftol": 1e-14})
        lam = -f(res.x)[0]
        if lam > best[0]:
            best = (lam, res.x)
        print(f"start {s}: lambda_min = {lam:.6e}")
    lam, mu = best
    lam_combo = U[:, :k] @ np.diag(1 / S[:k]) @ mu  # coefficients on the equations
    np.save(out, lam_combo)
    # rational rounding of the candidate, for the exact check in the verifier
    import json
    from fractions import Fraction
    scale = 1 / np.max(np.abs(lam_combo))
    rat = [str(Fraction(float(c * scale)).limit_denominator(10 ** 9)) for c in lam_combo]
    Path(out).with_suffix(".json").write_text(json.dumps(
        {"note": "EXPLORATORY candidate multipliers (rational) for the S19 equations, "
                 "in the order of unitarity_equations(); checked exactly in verify_hex_supremum_b19.py",
         "n_equations": len(eqs), "multipliers": rat}, indent=0))
    print(f"best lambda_min = {lam:.6e} (positive suggests a certificate); total {time.time() - t0:.1f} s")


if __name__ == "__main__":
    main()
