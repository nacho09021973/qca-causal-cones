"""Exact checks for the HEX_SUPREMUM (M1) gate, Stage A and M1-B13.

Contract: theory/HEX_SUPREMUM_GATE.md, preregistered at 86573ca.
Run from the repository root:

  python -B scripts/verify_hex_supremum_gate.py

Fail-closed, SymPy only, zero tolerance. Imports read-only the reviewed
verify_hex_ceiling_gate.py (its check_T2_minimal is rerun unchanged and its
own check list is read); that file is not modified.

What is certified here:
- Supports: the closed regular lattice hexagons with vertex v = g1, g1+g2,
  2 g1 contain exactly 7, 13, 19 lattice points (S7, S13, S19).
- Layer structure along the three facet normals, after normalising the
  longest vector to 1: every projection is an integer multiple of
  delta = r_in / N; in S13 (N = 3) the layers +-2 delta are singletons and
  together they are the six inner-ring points; in S19 (N = 2) no layer
  strictly between the extremes is a singleton.
- Second route for S13: generic coefficients on all 13 points, the layer
  equations of facet-line saturation (top edge -> P_+(n), bottom edge ->
  P_-(n), each intermediate layer -> 0) solved exactly force every
  inner-ring coefficient to vanish.
- The surviving S13 support {0} U vert is similar (rotation by -30 deg,
  scale) to the configuration of check_T2_minimal, which is rerun here.
What is not certified here: facet-line rigidity itself (Bernstein equality /
Julia, hex-ceiling report Sec. 3, Step 1, prior art), the normal form
A(n) = r n.sigma (Step 2), and the argument that the T2 proof is
lattice-free (it uses only the geometry of the 7 points); these are in the
report.
"""
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_hex_ceiling_gate as hexg  # reviewed, read-only

CHECKS = []
SX, SY, I2 = hexg.SX, hexg.SY, hexg.I2
R3 = sp.sqrt(3)
G1, G2 = hexg.G1, hexg.G2


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))


def rot(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a)], [sp.sin(a), sp.cos(a)]])


def hexagon(v):
    """Lattice points of the closed regular hexagon with vertices R^j v,
    normalised so that |v| = 1. Returns (points, vertices, normals, r_in)."""
    L = sp.sqrt((v.T * v)[0])
    verts = [rot(sp.pi * j / 3) * v for j in range(6)]
    ang = sp.atan2(v[1], v[0])
    normals = [rot(ang + sp.pi / 6 + sp.pi * j / 3) * G1 for j in range(6)]
    r = sp.simplify(L * R3 / 2)
    pts = []
    for a in range(-5, 6):
        for b in range(-5, 6):
            h = a * G1 + b * G2
            if all(sp.simplify((h.T * n)[0] - r) <= 0 for n in normals):
                pts.append(h)
    s = 1 / L
    return ([(p * s).applyfunc(sp.simplify) for p in pts],
            [(w * s).applyfunc(sp.simplify) for w in verts],
            [n.applyfunc(sp.simplify) for n in normals], sp.simplify(r * s))


def layers(pts, n, r, N):
    delta = r / N
    out = {}
    for i, p in enumerate(pts):
        q = sp.nsimplify(sp.simplify((p.T * n)[0] / delta))
        if not q.is_integer:
            return None
        out.setdefault(int(q), []).append(i)
    return out


def same(p, q):
    return all(sp.simplify(x - y) == 0 for x, y in zip(p, q))


def check_supports():
    res = {}
    for name, v, count in (("S7", G1, 7), ("S13", G1 + G2, 13), ("S19", 2 * G1, 19)):
        pts, verts, normals, r = hexagon(v)
        res[name] = (pts, verts, normals, r)
        record(f"{name}: closed hexagon with vertex {list(v)} has {count} lattice points, r_in = sqrt3/2",
               len(pts) == count and sp.simplify(r - R3 / 2) == 0, f"{len(pts)} points")
    return res


def check_S13(pts, verts, normals, r):
    N = 3
    inner = [i for i, p in enumerate(pts) if sp.simplify((p.T * p)[0] - sp.Rational(1, 3)) == 0]
    vidx = [i for i, p in enumerate(pts) if any(same(p, w) for w in verts)]
    origin = [i for i, p in enumerate(pts) if same(p, sp.zeros(2, 1))]
    record("S13: 1 origin + 6 inner-ring points (|h| = 1/sqrt3) + 6 vertices",
           len(origin) == 1 and len(inner) == 6 and len(vidx) == 6)
    forced = set()
    ok_grid, ok_single = True, True
    lay3 = []
    for n in normals[:3]:
        L = layers(pts, n, r, N)
        if L is None or set(L) != set(range(-N, N + 1)):
            ok_grid = False
            continue
        lay3.append((n, L))
        for lev in (2, -2):
            if len(L[lev]) != 1 or L[lev][0] not in inner:
                ok_single = False
            forced.update(L[lev])
        if sorted(len(L[k]) for k in (N, -N)) != [2, 2]:
            ok_single = False
    record("S13: along each facet normal all projections lie on the grid delta = r_in/3, levels -3..3", ok_grid)
    record("S13: layers +-2 delta are singletons of inner-ring points; edges have 2 points", ok_single)
    record("S13: the six singleton layers are exactly the inner ring (each such coefficient must vanish)",
           forced == set(inner))

    # Second route: generic coefficients, layer equations, exact linear solve.
    syms = []

    def gen(k):
        e = sp.symbols(f"a{k}_0:8", real=True)
        syms.extend(e)
        return sp.Matrix([[e[0] + sp.I * e[1], e[2] + sp.I * e[3]], [e[4] + sp.I * e[5], e[6] + sp.I * e[7]]])
    A = [gen(k) for k in range(len(pts))]
    lin = []
    for n, L in lay3:
        Pp = (I2 + n[0] * SX + n[1] * SY) / 2
        Pm = (I2 - n[0] * SX - n[1] * SY) / 2
        for lev, idx in L.items():
            target = Pp if lev == N else Pm if lev == -N else sp.zeros(2)
            M = sum((A[i] for i in idx), sp.zeros(2)) - target
            for e in M:
                e = sp.expand(e)
                lin += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    sol = sp.solve(lin, syms, dict=True)
    ok = len(sol) == 1 and all(hexg.base.is_zero_matrix(A[i].subs(sol[0])) for i in inner)
    record("S13 (second route): exact solution of the layer equations forces every inner-ring coefficient to 0", ok)

    # The surviving support {0} U vert is similar to the T2 configuration.
    t2 = [sp.Matrix([sp.cos(sp.pi * k / 3), sp.sin(sp.pi * k / 3)]) for k in range(6)]
    rv = [(rot(-sp.pi / 6) * w).applyfunc(sp.simplify) for w in verts]
    record("S13: rotating the six vertices by -30 deg gives the T2 vertex set (cos k pi/3, sin k pi/3)",
           all(any(same(p, q) for q in t2) for p in rv))


def check_S19(pts, verts, normals, r):
    N = 2
    sizes, ok_grid, singleton = [], True, False
    for n in normals[:3]:
        L = layers(pts, n, r, N)
        if L is None or set(L) != set(range(-N, N + 1)):
            ok_grid = False
            continue
        sizes.append([len(L[k]) for k in range(N, -N - 1, -1)])
        singleton |= any(len(L[k]) == 1 for k in range(-N + 1, N))
    record("S19: along each facet normal all projections lie on the grid delta = r_in/2, levels -2..2", ok_grid)
    record("S19: layer sizes (top..bottom) are 3,4,5,4,3 on each normal; no intermediate singleton",
           ok_grid and all(s == [3, 4, 5, 4, 3] for s in sizes) and not singleton, str(sizes))


def check_T2_rerun():
    before = len(hexg.CHECKS)
    hexg.check_T2_minimal()
    sub = hexg.CHECKS[before:]
    record("T2-min of the reviewed verifier, rerun unchanged: all its checks pass",
           len(sub) == 4 and all(c[1] for c in sub), f"{sum(c[1] for c in sub)}/{len(sub)}")


def main():
    print("== supports")
    res = check_supports()
    print("== S13: singleton layers")
    check_S13(*res["S13"])
    print("== S19: layer structure")
    check_S19(*res["S19"])
    print("== T2 minimal support (reviewed verifier, read-only)")
    check_T2_rerun()
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (M1 Stage A, M1-B13).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
