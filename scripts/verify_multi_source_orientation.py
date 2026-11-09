#!/usr/bin/env python3
"""Multi-source orientation gate (contract theory/MULTI_SOURCE_ORIENTATION_GATE.md, commit dd9ab5c).

Report: reports/2026-11-09--multi-source-orientation.md

Parts:
 A. EXACT (SymPy): on the coordinate plane n3 = 0 the order-2 group-speed coefficient
    3 alpha + |grad_S beta|^2 / 2 vanishes for L5a/L5b/L4 (beta = +-(sqrt3/3) n1 n2 n3,
    alpha = -sigma2/18 - n1^2 n2^2 n3^2/6); and the radial/tangential expansion identity.
 B. D2 branch-and-bound over SO(3) (ZYZ Euler boxes) with float interval arithmetic,
    outward rounding by np.nextafter, Lipschitz trig enclosures with an added 1e-15 slack for
    libm error, and source-direction boxes of +-0.5 deg (Kostelecky-Mewes positions are
    integer degrees). Goal: certify that for every orientation some source i has
    |n1 n2 n3 (R^T s_i)| > delta_i, delta_i = 2 E_Pl' K_i sqrt3 (EXCLUDED_ROBUST threshold).
    Declared limits: libm error slack is assumed, not proved; constants enter as floats.
 C. Decimal (mpmath): L3s4 orientation-independent D1/D2 thresholds on a (quadratic roots),
    L3 D1 orientation-independent lower bound (inherits the parent sensitivity).
"""
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-09--multi-source-orientation"
CHECKS = []
mp.mp.dps = 30
HBARC = mp.mpf("1.973269804e-16")
LP = mp.mpf("1.616255e-35")
EPLP = HBARC / LP                                   # hbar c / ell_P in GeV (~1.22089e19)
EQG1 = {"sub": mp.mpf("1.0e20"), "super": mp.mpf("1.1e20")}
KM = [  # (name, codeclination deg, RA deg, K GeV^-1)
    ("GRB 041219A", 27, 6, 2e-34), ("GRB 100826A", 112, 279, 7e-35),
    ("GRB 110301A", 61, 229, 2e-34), ("GRB 110721A", 129, 333, 1e-34)]
POS_UNC_DEG = 0.5
SLACK = 1e-15
MAX_BOXES = 4_000_000
MIN_WIDTH = 1e-7


def exact(name, cond, detail=""):
    CHECKS.append(dict(name=name, passed=bool(cond), detail=str(detail)))


# ---------------- A ----------------
def part_A():
    n1, n2, n3, t = sp.symbols("n1 n2 n3 t", real=True)
    beta = sp.sqrt(3) / 3 * n1 * n2 * n3
    alpha = -(n1**2 * n2**2 + n2**2 * n3**2 + n3**2 * n1**2) / 18 - n1**2 * n2**2 * n3**2 / 6
    grad = sp.Matrix([sp.diff(beta, v) for v in (n1, n2, n3)])
    nvec = sp.Matrix([n1, n2, n3])
    radial = (nvec.T * grad)[0]                     # = 3 beta (Euler, homogeneous degree 3)
    exact("A: n.grad(beta) = 3 beta (homogeneity), so on beta = 0 grad beta is tangential",
          sp.simplify(radial - 3 * beta) == 0)
    on_plane = {n3: 0}
    gS2 = sum(g**2 for g in grad).subs(on_plane)    # tangential = full gradient where beta = 0
    coef2 = sp.simplify((3 * alpha + gS2 / 2).subs(on_plane))
    exact("A: on n3 = 0, 3 alpha + |grad_S beta|^2/2 = 0 (L5a/L5b/L4; same for -beta)", coef2 == 0, coef2)
    # expansion identity: |grad eps|/c0 = 1 + 2 b t + (3 a + |gS b|^2/2) t^2 + O(t^3)
    b, a, g = sp.symbols("b a g", real=True)
    expr = sp.sqrt((1 + 2 * b * t + 3 * a * t**2)**2 + t**2 * g**2)
    ser = sp.series(expr, t, 0, 3).removeO()
    exact("A: sqrt((1+2bt+3at^2)^2 + g^2 t^2) = 1 + 2bt + (3a + g^2/2) t^2 + O(t^3)",
          sp.expand(ser - (1 + 2 * b * t + (3 * a + g**2 / 2) * t**2)) == 0)


# ---------------- B: interval arithmetic ----------------
def dn(x):
    return np.nextafter(x, -np.inf)


def up(x):
    return np.nextafter(x, np.inf)


def iadd(a, b):
    return dn(a[0] + b[0]), up(a[1] + b[1])


def imul(a, b):
    p = np.stack([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]])
    return dn(p.min(0)), up(p.max(0))


def ineg(a):
    return -a[1], -a[0]


def isin(lo, hi):
    c = 0.5 * (lo + hi); w = 0.5 * (hi - lo)
    s = np.sin(c)
    return np.maximum(dn(s - w - SLACK), -1.0), np.minimum(up(s + w + SLACK), 1.0)


def icos(lo, hi):
    c = 0.5 * (lo + hi); w = 0.5 * (hi - lo)
    s = np.cos(c)
    return np.maximum(dn(s - w - SLACK), -1.0), np.minimum(up(s + w + SLACK), 1.0)


def rot_z_T(v, c, s):
    """apply Rz(angle)^T = Rz(-angle) to vector intervals v=(x,y,z): x' = c x + s y, y' = -s x + c y."""
    x, y, z = v
    return iadd(imul(c, x), imul(s, y)), iadd(imul(ineg(s), x), imul(c, y)), z


def rot_y_T(v, c, s):
    """Ry(angle)^T: x' = c x - s z, z' = s x + c z."""
    x, y, z = v
    return iadd(imul(c, x), imul(ineg(s), z)), y, iadd(imul(s, x), imul(c, z))


def source_box(theta_deg, phi_deg):
    """Enclosure of s = (sin th cos ph, sin th sin ph, cos th) over th, ph in +-0.5 deg (Lipschitz 1 per angle)."""
    th = math.radians(theta_deg); ph = math.radians(phi_deg)
    r = math.radians(POS_UNC_DEG) * 2 + SLACK      # |ds_j| <= |dth| + |dph|
    c = [math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th)]
    return [(np.float64(dn(x - r)), np.float64(up(x + r))) for x in c]


def part_B():
    deltas = [float(2 * EPLP * mp.mpf(K) * mp.sqrt(3)) * (1 + 1e-9) for _, _, _, K in KM]
    srcs = [source_box(th, ph) for _, th, ph, _ in KM]
    lo = np.array([[0.0, 0.0, 0.0]]); hi = np.array([[2 * math.pi, math.pi, 2 * math.pi]])
    # split initial domain into a coarse grid
    g = 8
    A = np.linspace(0, 2 * math.pi, g + 1); B = np.linspace(0, math.pi, g + 1); C = np.linspace(0, 2 * math.pi, g + 1)
    ii = np.array([(i, j, k) for i in range(g) for j in range(g) for k in range(g)])
    lo = np.stack([A[ii[:, 0]], B[ii[:, 1]], C[ii[:, 2]]], 1)
    hi = np.stack([A[ii[:, 0] + 1], B[ii[:, 1] + 1], C[ii[:, 2] + 1]], 1)
    processed = 0
    level = 0
    status = "CERTIFIED"
    witness = None
    while len(lo):
        level += 1
        processed += len(lo)
        if processed > MAX_BOXES:
            status = "OPEN (box budget exceeded)"; break
        ca, sa = icos(lo[:, 0], hi[:, 0]), isin(lo[:, 0], hi[:, 0])
        cb, sb = icos(lo[:, 1], hi[:, 1]), isin(lo[:, 1], hi[:, 1])
        cg, sg = icos(lo[:, 2], hi[:, 2]), isin(lo[:, 2], hi[:, 2])
        alive = np.ones(len(lo), bool)
        for (sx, sy, sz), d in zip(srcs, deltas):
            n = len(lo)
            v = ((np.full(n, sx[0]), np.full(n, sx[1])), (np.full(n, sy[0]), np.full(n, sy[1])),
                 (np.full(n, sz[0]), np.full(n, sz[1])))
            # n = R^T s with R = Rz(a) Ry(b) Rz(g): R^T = Rz(g)^T Ry(b)^T Rz(a)^T
            v = rot_z_T(v, ca, sa); v = rot_y_T(v, cb, sb); v = rot_z_T(v, cg, sg)
            p = imul(imul(v[0], v[1]), v[2])
            excluded_here = (p[0] > d) | (p[1] < -d)
            alive &= ~excluded_here
        lo, hi = lo[alive], hi[alive]
        if not len(lo):
            break
        w = hi - lo
        if w.max() < MIN_WIDTH:
            status = "OPEN (min width reached; candidate escape region)"
            witness = dict(lo=lo[0].tolist(), hi=hi[0].tolist(), count=int(len(lo))); break
        k = np.argmax(w, axis=1)
        mid = lo[np.arange(len(lo)), k] + 0.5 * w[np.arange(len(lo)), k]
        lo2 = lo.copy(); hi2 = hi.copy()
        hi1 = hi.copy(); hi1[np.arange(len(lo)), k] = mid
        lo2[np.arange(len(lo)), k] = mid
        lo = np.concatenate([lo, lo2]); hi = np.concatenate([hi1, hi2])
    return dict(status=status, boxes_processed=int(processed), levels=level, deltas=deltas, witness=witness)


def part_B_diagnostic(nsamp=20000):
    """Non-verdict diagnostic: sampled upper estimate of min_R max_i |p_i|/delta_i (floats)."""
    rng = np.random.default_rng(12345)
    q = rng.normal(size=(nsamp, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
    w, x, y, z = q.T
    R = np.stack([np.stack([1 - 2 * (y*y + z*z), 2 * (x*y - z*w), 2 * (x*z + y*w)], -1),
                  np.stack([2 * (x*y + z*w), 1 - 2 * (x*x + z*z), 2 * (y*z - x*w)], -1),
                  np.stack([2 * (x*z - y*w), 2 * (y*z + x*w), 1 - 2 * (x*x + y*y)], -1)], 1)
    best = np.inf
    vals = []
    for (_, th, ph, K) in KM:
        t, p = math.radians(th), math.radians(ph)
        s = np.array([math.sin(t) * math.cos(p), math.sin(t) * math.sin(p), math.cos(t)])
        n = np.einsum("nji,j->ni", R, s)
        vals.append(np.abs(n.prod(1)))
    m = np.max(np.stack(vals), 0)
    return float(m.min())


# ---------------- C ----------------
def part_C():
    out = {}
    s3 = mp.sqrt(3)
    xc = (19 - 6 * s3) / 11
    for cluster, E in (("upper (beta>0, superluminal)", EQG1["super"]), ("lower (beta<0, subluminal)", EQG1["sub"])):
        thr = EPLP / E                          # D1 EXCLUDED_ROBUST iff B-M > thr
        roots = []
        # case a^2 <= 1/2: sqrt3(1-a^2)/6 - (1-2a^2)/9 = thr a  ->  a^2(2/9 - sqrt3/6) - thr a + (sqrt3/6 - 1/9) = 0
        A1, B1, C1 = (mp.mpf(2) / 9 - s3 / 6), -thr, (s3 / 6 - mp.mpf(1) / 9)
        # case a^2 >= 1/2: sqrt3(1-a^2)/6 - (2a^2-1)/9 = thr a -> a^2(-sqrt3/6 - 2/9) - thr a + (sqrt3/6 + 1/9) = 0
        A2, B2, C2 = (-s3 / 6 - mp.mpf(2) / 9), -thr, (s3 / 6 + mp.mpf(1) / 9)
        for (Aq, Bq, Cq, lo_, hi_) in ((A1, B1, C1, 0, 1 / mp.sqrt(2)), (A2, B2, C2, 1 / mp.sqrt(2), mp.sqrt(xc))):
            disc = Bq**2 - 4 * Aq * Cq
            if disc >= 0:
                for r in ((-Bq + mp.sqrt(disc)) / (2 * Aq), (-Bq - mp.sqrt(disc)) / (2 * Aq)):
                    if lo_ < r < hi_:
                        roots.append(r)
        f = lambda a: (s3 * (1 - a**2) / 6 - abs(2 * a**2 - 1) / 9) / a
        out[cluster] = dict(threshold=mp.nstr(thr, 8), roots=[mp.nstr(r, 10) for r in roots],
                            f_at_1_over_sqrt2=mp.nstr(f(1 / mp.sqrt(2)), 8), f_near_xc=mp.nstr(f(mp.sqrt(xc) * (1 - mp.mpf("1e-6"))), 6))
    d2_thr = 2 * mp.mpf("7e-35") * EPLP
    out["D2 threshold on B-M (strongest K, any single source)"] = mp.nstr(d2_thr, 6)
    out["x_c"] = mp.nstr(xc, 10)
    exact("C: L3s4 B-M > D1 threshold holds for a in (0, root) per cluster (single root inside (0, sqrt x_c))",
          all(len(v["roots"]) == 1 for k, v in out.items() if isinstance(v, dict)), out)
    return out


def main():
    part_A()
    b = part_B()
    exact("B: D2 branch-and-bound: every orientation has some KM source with |n1n2n3| > delta_i "
          "(interval method; libm slack assumed)", b["status"] == "CERTIFIED", b)
    diag = part_B_diagnostic()
    c = part_C()
    data = dict(B=b, B_diagnostic_sampled_min_max_abs_p=diag, C=c, checks=CHECKS,
                sources_D1=dict(GRB_090510="RA 333.55271 Dec -26.58266 (GCN 9339)",
                                GRB_221009A="RA 288.2643 Dec +19.7712 (GCN 32632; GCN 32635 identification)"),
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (
                    "scripts/verify_multi_source_orientation.py", "theory/MULTI_SOURCE_ORIENTATION_GATE.md",
                    "investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md")})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2, default=str) + "\n")
    passed = sum(x["passed"] for x in CHECKS)
    lines = [f"Checks: {passed}/{len(CHECKS)}"] + [f"{'PASS' if x['passed'] else 'FAIL'} {x['name']}  {x['detail']}" for x in CHECKS]
    lines += ["", f"DIAGNOSTIC (sampled, float, no verdict): min over sampled R of max_i |n1n2n3| = {diag:.4g}"]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
