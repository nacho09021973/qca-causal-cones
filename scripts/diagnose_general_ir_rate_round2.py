"""Diagnostic run for theory/GENERAL_IR_RATE_ROUND2_DIAGNOSTIC.md.

Sixteen walks (the six of diagnose_general_ir_rate_polyhedra.py and the ten
of diagnose_general_ir_rate_zonotopes.py, both imported read-only; the
latter installs the declared vertex fallback). Regions are placed half-way
between each walk's ballistic region and its causal boundary along n, and
the minimiser of the rate on B - A is found by Newton's method without
assuming it lies on the axis. Floating point; labels are diagnostic, not
certificates or verdicts.

Run from the repository root:
    python3 -B scripts/diagnose_general_ir_rate_round2.py --output reports/<name>.json
"""
import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import diagnose_general_ir_rate_polyhedra as P  # noqa: E402
import diagnose_general_ir_rate_zonotopes as Zs  # noqa: E402  (installs fallback)

T_SMALL = 1e-3


def walk_list():
    rows = [(wid, name, builder, phase) for wid, name, builder, phase in P.WALKS]
    for zid, name, gens, expos in Zs.ROWS:
        rows.append((zid, name, (lambda g=gens, e=expos: Zs.product_walk(g, e)), None))
    return rows


class Rate:
    def __init__(self, sym, basis_np, grid):
        self.sym, self.B, self.grid = sym, basis_np, grid

    def full(self, xi):
        return P.phi_and_maximisers(self.sym, xi, self.B, self.grid)

    def local(self, xi, ks):
        found = [P.refine(self.sym, k, xi, self.B) for k in ks]
        vmax = max(v for _, v in found)
        return vmax, [k for k, v in found if v >= vmax - 1e-9 * max(1, abs(vmax))]

    def grad(self, xi, ks):
        _, kk = self.local(xi, ks)
        return P.grad_xi_logabs(self.sym, kk[0], xi), kk


def rational_direction(x, basis_np):
    """Is x parallel to a dual-lattice vector with small integer coordinates?"""
    r = basis_np.T @ x            # components in the dual basis (up to scale)
    j = int(np.argmax(np.abs(r)))
    q = [Fraction(float(ri / r[j])).limit_denominator(12) for ri in r]
    ok = all(abs(float(qi) * r[j] - ri) < 1e-6 * abs(r[j]) for qi, ri in zip(q, r))
    return bool(ok), [str(qi) for qi in q]


def analyse2(wid, name, builder, target_phase):
    M, zs, gens = builder()
    terms = P.laurent_terms(M, zs)
    basis, steps = P.lattice_data(terms, gens)
    d = len(gens)
    sym = P.Symbol(terms, steps)
    basis_np = np.array([[float(x) for x in b] for b in basis]).T
    out = dict(id=wid, name=name, d=d, s=sym.s,
               lattice_isometric_to_Zd=bool(P.isometric_to_Zd(basis)))
    Zs.FALLBACK.clear()
    V = P.choose_vertex(steps, d, sym)
    out["no_rate_axis"] = bool(Zs.FALLBACK.get("used"))
    Vn = np.array([float(x) for x in V])
    h = float(np.linalg.norm(Vn))
    n = Vn / h
    lam0, Q, A, c, node_def = P.node(sym, d, target_phase)
    out["node"] = dict(c_IR=c, **node_def)
    rate = Rate(sym, basis_np, P.bz_grid(basis_np, d))

    xi0 = T_SMALL * n
    _, ks0 = rate.full(xi0)
    s0 = float(np.dot(n, P.grad_xi_logabs(sym, ks0[0], xi0)))
    out["s0"], out["h"] = s0, h
    out["fast_modes_along_n"] = bool(s0 > c * (1 + 1e-6))
    if s0 >= h:
        out["label"] = "NO_CORONA_ALONG_N"
        return out
    rho = (h - s0) / 4
    target = (s0 + h) / 2
    out["rho"], out["target_speed"] = rho, target

    # on-axis start: n.grad Phi(t n) = target
    lo, hi = T_SMALL, 12.0
    for _ in range(32):
        mid = (lo + hi) / 2
        _, ks = rate.full(mid * n)
        if np.dot(n, P.grad_xi_logabs(sym, ks[0], mid * n)) < target:
            lo = mid
        else:
            hi = mid
    xi = ((lo + hi) / 2) * n
    _, ks = rate.full(xi)

    # Newton for grad Phi(xi) + 2 rho xi/|xi| = V
    def F(x, kk):
        g, kk2 = rate.grad(x, kk)
        return g + 2 * rho * x / np.linalg.norm(x) - Vn, kk2

    res, ks = F(xi, ks)
    for _ in range(25):
        if np.linalg.norm(res) < 1e-9:
            break
        J = np.zeros((d, d))
        hstep = 1e-5
        for b in range(d):
            e = np.eye(d)[b] * hstep
            fp, _ = F(xi + e, ks)
            fm, _ = F(xi - e, ks)
            J[:, b] = (fp - fm) / (2 * hstep)
        try:
            step = -np.linalg.solve(J, res)
        except np.linalg.LinAlgError:
            break
        if np.linalg.norm(step) > 0.2 * np.linalg.norm(xi):
            step *= 0.2 * np.linalg.norm(xi) / np.linalg.norm(step)
        xi = xi + step
        res, ks = F(xi, ks)
    out["newton_residual"] = float(np.linalg.norm(res))
    phi, ks = rate.full(xi)
    vstar = P.grad_xi_logabs(sym, ks[0], xi)
    out["xi_star"] = xi.tolist()
    out["xi_on_axis_defect"] = float(np.linalg.norm(xi / np.linalg.norm(xi) - n))
    out["v_star"] = vstar.tolist()
    out["K_star"] = float(np.dot(xi, vstar) - phi)
    h3, ratios = rational_direction(xi, basis_np)
    out["xi_dual_ratios"] = ratios

    u = xi / np.linalg.norm(xi)
    plane = []
    if h3:
        Bn = basis_np.T @ u
        plane = [basis_np @ np.array(m, float) for m in itertools.product(range(-6, 7), repeat=d)
                 if any(m) and abs(np.dot(Bn, m)) < 1e-7]
    dom = []
    for k in ks:
        lam, e, f, gap = sym.dominant(k, xi)
        g = P.grad_xi_logabs(sym, k, xi)
        hess = np.linalg.eigvalsh(P.hess_kappa_logabs(sym, k, xi))
        trivial = bool(plane) and all(abs(np.exp(1j * np.dot(k, p)) - 1) < 1e-6 for p in plane)
        dom.append(dict(k=k.tolist(), is_zero=bool(np.linalg.norm(k) < 1e-4), trivial_character=trivial,
                        gap_ratio=float(gap), hessian_eigs=hess.tolist(),
                        grad_minus_vstar=float(np.linalg.norm(g - vstar)), e=e, f=f))
    out["dominant_points"] = [{kk: v for kk, v in x.items() if kk not in ("e", "f")} for x in dom]
    zero = [x for x in dom if x["is_zero"]]
    others = [x for x in dom if x["trivial_character"] and not x["is_zero"]]
    hy = {}
    hy["K_star_positive"] = bool(out["K_star"] > 1e-6)
    hy["H2"] = bool(all(x["gap_ratio"] < 1 - 1e-6 for x in dom) and all(max(x["hessian_eigs"]) < -1e-6 for x in dom))
    hy["H3"] = h3
    hy["H4prime"] = bool(zero)
    hy["H8"] = bool(all(x["grad_minus_vstar"] < P.TOL_EQ for x in dom))
    hy["H7"] = bool(rho < (np.pi if d == 3 else 2.405))
    hy["H9"] = "generic" if (h3 and out["xi_on_axis_defect"] < 1e-6) else (None if not h3 else False)
    if zero:
        f0, e0 = zero[0]["f"], zero[0]["e"]
        if others:
            Fo = np.array([x["f"] for x in others]).T
            Fall = np.column_stack([Fo, f0])
            so = np.linalg.svd(Fo / np.linalg.norm(Fo, axis=0), compute_uv=False)
            sa = np.linalg.svd(Fall / np.linalg.norm(Fall, axis=0), compute_uv=False)
            hy["H6_left"] = bool(np.sum(sa > P.TOL_SING) > np.sum(so > P.TOL_SING))
        else:
            hy["H6_left"] = True
        wB = Vn - rho * u
        tails = []
        for col in range(2):
            R, I0, I1 = P.tail(wB, A, c, Q[:, col], d)
            par = abs(np.vdot(e0, R)) / (np.linalg.norm(e0) * np.linalg.norm(R))
            tails.append(dict(chi_index=col, tail_norm=float(np.linalg.norm(R)), cos_angle_e0_tail=float(par)))
        out["tails"] = tails
        hy["H5"] = all(t["tail_norm"] > 1e-8 for t in tails)
        hy["H10_sufficient"] = bool(hy["H6_left"] and all(t["cos_angle_e0_tail"] < 1 - P.TOL_SING for t in tails))
    out["hypotheses"] = hy
    fails = [k for k, v in hy.items() if v is False]
    tags = []
    if not out["lattice_isometric_to_Zd"]:
        tags.append("OUTSIDE_CLASS_LATTICE")
    tags.append("FAILS_" + "_".join(fails) if fails else "HYPOTHESES_HOLD_NUMERICALLY")
    out["label"] = "; ".join(tags)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    results = []
    for wid, name, builder, phase in walk_list():
        r = analyse2(wid, name, builder, phase)
        results.append(r)
        print(f"{wid} {name}: {r['label']}")
        for k in ("s0", "h", "fast_modes_along_n", "K_star", "newton_residual", "xi_on_axis_defect"):
            if k in r:
                print(f"    {k} = {r[k]}")
        if "hypotheses" in r:
            print("    " + ", ".join(f"{k}={v}" for k, v in r["hypotheses"].items()))
            print(f"    dominant points: {len(r['dominant_points'])}, zero dominant: "
                  f"{any(x['is_zero'] for x in r['dominant_points'])}")
        sys.stdout.flush()
    meta = dict(charter="theory/GENERAL_IR_RATE_ROUND2_DIAGNOSTIC.md", script_sha256=P.sha(__file__),
                imported=dict(polyhedra=P.sha(P.__file__), zonotopes=P.sha(Zs.__file__)),
                numpy=np.__version__, sympy=sp.__version__,
                nature="floating-point diagnostic; labels are not certificates or verdicts")
    args.output.write_text(json.dumps(dict(meta=meta, walks=results), indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
