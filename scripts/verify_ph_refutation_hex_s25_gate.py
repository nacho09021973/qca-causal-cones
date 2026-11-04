"""Exact checks for the PH_REFUTATION_HEX_S25 gate (hexagon H25).

Contract: theory/PH_REFUTATION_HEX_S25_GATE.md, preregistered at 6eb50c1.
Run from the repository root:

  python3 -B scripts/verify_ph_refutation_hex_s25_gate.py

Fail-closed, SymPy only, zero tolerance. Imports read-only the reviewed
verify_hex_supremum_gate.py (hexagon, layers) and verify_hex_supremum_b19.py
(linear reductions L1-L3, parametrization, unitarity equations, square
controls); neither is modified.

Stage A on H25 (v = 2 g1 + g2), certified here:
- support: 25 lattice points, 6 vertices, r_in = sqrt3/2 after normalising
  |v| = 1; no lattice point in the interior of an edge; the mirror image
  H25' (v = g1 + 2 g2) is the image of H25 under a lattice reflection;
- layers along the three facet normals lie on the grid delta = r_in / 7;
  singleton intermediate layers (lemma A1 of the M1 Stage A report) force
  their coefficients to vanish;
- these singletons are exactly the 18 points other than the origin and the
  vertices (second route: exact solution of the layer equations; not
  independent of A1); the same holds directly on H25';
- the surviving support {0} U vert(H25) is, after a rotation, the vertex set
  of the minimal-support T2 of the hex-ceiling gate, whose reviewed check
  is rerun unchanged (4/4);
- the square-substrate controls of the M1-B19 verifier, rerun unchanged.
What is not certified here: the analytic steps (facet-line rigidity, lemma
A1, the normal form, and that the T2 proof uses only the geometry of the
seven points), which are in the hex-ceiling and M1 reports and reused.
No nonlinear solver is run.
"""
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_hex_supremum_gate as m1    # reviewed, read-only
import verify_hex_supremum_b19 as b19    # reviewed, read-only

CHECKS = []
R3 = sp.sqrt(3)
G1, G2 = m1.G1, m1.G2
N25 = 7


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" ({detail})" if detail else ""))


def lattice_coords(p, scale):
    """Integer coordinates (a, b) with p * scale = a g1 + b g2."""
    M = sp.Matrix.hstack(G1, G2)
    c = (M.inv() * (p * scale)).applyfunc(sp.nsimplify)
    return tuple(int(x) for x in c) if all(x.is_integer for x in c) else None


def check_support():
    v = 2 * G1 + G2
    pts, verts, normals, r = m1.hexagon(v)
    L = sp.sqrt((v.T * v)[0])
    record("H25: closed hexagon with vertex 2 g1 + g2 has 25 lattice points, 6 vertices, r_in = sqrt3/2",
           len(pts) == 25 and len(verts) == 6 and sp.simplify(r - R3 / 2) == 0, f"{len(pts)} points")
    vidx = [i for i, p in enumerate(pts) if any(m1.same(p, w) for w in verts)]
    record("H25: all six vertices are lattice points of the support", len(vidx) == 6)
    # edges: lattice points on the segment between consecutive vertices
    interior = 0
    for j in range(6):
        a, b = verts[j], verts[(j + 1) % 6]
        for i, p in enumerate(pts):
            if i in vidx:
                continue
            cross = sp.simplify((b - a)[0] * (p - a)[1] - (b - a)[1] * (p - a)[0])
            if cross == 0:
                interior += 1
    record("H25: no lattice point in the interior of an edge", interior == 0)
    # mirror: reflection across the g1 axis composed with lattice map; image hexagon
    pts2, verts2, _, _ = m1.hexagon(G1 + 2 * G2)
    refl = sp.Matrix([[1, 0], [0, -1]])  # reflection y -> -y maps Lambda to Lambda
    img = [(refl * p).applyfunc(sp.simplify) for p in pts]
    in_lattice = all(lattice_coords(q, L) is not None for q in img)
    same_set = len(pts2) == 25 and all(any(m1.same(q, p2) for p2 in pts2) for q in img)
    record("H25': the reflection y -> -y (a symmetry of Lambda) maps H25 onto the hexagon with vertex g1 + 2 g2",
           in_lattice and same_set)
    return pts, verts, normals, r, vidx


def singleton_layers(pts, normals, r):
    forced, table = set(), []
    for n in normals[:3]:
        Ls = m1.layers(pts, n, r, N25)
        if Ls is None:
            return None, None
        sizes = [len(Ls.get(m, [])) for m in range(N25, -N25 - 1, -1)]
        table.append(sizes)
        for m, idx in Ls.items():
            if abs(m) < N25 and len(idx) == 1:
                forced.update(idx)
    return forced, table


def second_route(pts, normals, r, forced):
    """Generic coefficients on all points; the layer equations of facet-line
    rigidity along the three normals, solved exactly, must force A_h = 0 on
    the A1 set. Not independent of A1 (the layer equations contain it)."""
    syms = []

    def gen(k):
        e = sp.symbols(f"a{k}_0:8", real=True)
        syms.extend(e)
        return sp.Matrix([[e[0] + sp.I * e[1], e[2] + sp.I * e[3]], [e[4] + sp.I * e[5], e[6] + sp.I * e[7]]])
    A = [gen(k) for k in range(len(pts))]
    lin = []
    for n in normals[:3]:
        Ls = m1.layers(pts, n, r, N25)
        # explicit radicals: SymPy leaves cos(atan(sqrt3/5) + pi/6) unevaluated,
        # and re()/im() of the projector entries are then not reduced
        n = n.applyfunc(lambda x: sp.radsimp(sp.simplify(sp.expand_trig(x))))
        Pp = (m1.I2 + n[0] * m1.SX + n[1] * m1.SY) / 2
        Pm = (m1.I2 - n[0] * m1.SX - n[1] * m1.SY) / 2
        for lev, idx in Ls.items():
            target = Pp if lev == N25 else Pm if lev == -N25 else sp.zeros(2)
            M = sum((A[i] for i in idx), sp.zeros(2)) - target
            for e in M:
                e = sp.expand(e)
                lin += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    sol = sp.solve(lin, syms, dict=True)
    return len(sol) == 1 and all(m1.hexg.base.is_zero_matrix(A[i].subs(sol[0])) for i in forced)


def main():
    print("== Part 1: support H25 (contract Sec. 2)")
    pts, verts, normals, r, vidx = check_support()
    print("== Part 2: layers and lemma A1 (contract Sec. 3, Stage A)")
    forced, table = singleton_layers(pts, normals, r)
    record("H25: on each of the three facet normals every projection is a multiple of delta = r_in/7",
           forced is not None)
    nsimp = [n.applyfunc(lambda x: sp.radsimp(sp.simplify(sp.expand_trig(x)))) for n in normals[:3]]
    record("H25: the three facet normals are unit vectors (explicit radicals)",
           all(sp.simplify(n[0] ** 2 + n[1] ** 2 - 1) == 0 for n in nsimp), str([list(n) for n in nsimp]))
    for n, sizes in zip(normals[:3], table):
        print(f"  normal {list(n)}: layer sizes from +7 to -7: {sizes}")
    record("H25: the two extreme layers of each normal are the two vertices of an edge",
           all(s[0] == 2 and s[-1] == 2 for s in table))
    origin = [i for i, p in enumerate(pts) if m1.same(p, sp.zeros(2, 1))]
    survivors = [i for i in range(len(pts)) if i not in forced]
    print(f"  A1 forces A_h = 0 at {len(forced)} points; surviving support: {len(survivors)} points")
    for i in survivors:
        tag = "vertex" if i in vidx else "origin" if i in origin else "interior"
        print(f"    {tag}: {list(pts[i])}, |h|^2 = {sp.simplify((pts[i].T * pts[i])[0])}")
    nonvertex = [i for i in range(len(pts)) if i not in vidx and i not in origin]
    record("H25 (A1): singleton intermediate layers cover every point other than the origin and the vertices",
           forced == set(nonvertex) and len(forced) == 18)
    record("H25 (second route, not independent of A1): exact solution of the layer equations on all 25 "
           "points forces A_h = 0 on those 18 points", second_route(pts, normals, r, forced))
    # The same analysis directly on the mirror hexagon H25' (instead of relying on the reflection).
    pts2, verts2, normals2, r2 = m1.hexagon(G1 + 2 * G2)
    forced2, table2 = singleton_layers(pts2, normals2, r2)
    v2 = [i for i, p in enumerate(pts2) if any(m1.same(p, w) for w in verts2)]
    o2 = [i for i, p in enumerate(pts2) if m1.same(p, sp.zeros(2, 1))]
    record("H25' (direct): 25 points, and A1 forces A_h = 0 at every point other than the origin and the vertices",
           len(pts2) == 25 and forced2 is not None
           and forced2 == {i for i in range(25) if i not in v2 and i not in o2})
    print("== Part 3: reduction to the minimal-support configuration of T2")
    ang = sp.atan2(verts[0][1], verts[0][0])
    t2 = [sp.Matrix([sp.cos(sp.pi * k / 3), sp.sin(sp.pi * k / 3)]) for k in range(6)]
    rv = [(m1.rot(-ang) * w).applyfunc(sp.simplify) for w in verts]
    record("H25: rotating the six vertices by -atan(sqrt3/5) gives the T2 vertex set (cos k pi/3, sin k pi/3)",
           all(any(m1.same(p, q) for q in t2) for p in rv))
    ang2 = sp.atan2(verts2[0][1], verts2[0][0])
    rv2 = [(m1.rot(-ang2) * w).applyfunc(sp.simplify) for w in verts2]
    record("H25': rotating its six vertices by minus the angle of its first vertex gives the T2 vertex set",
           all(any(m1.same(p, q) for q in t2) for p in rv2))
    before = len(m1.hexg.CHECKS)
    m1.hexg.check_T2_minimal()
    sub = m1.hexg.CHECKS[before:]
    record("T2-min of the reviewed verify_hex_ceiling_gate.py, rerun unchanged: all its checks pass",
           len(sub) == 4 and all(c[1] for c in sub), f"{sum(c[1] for c in sub)}/{len(sub)}")
    print("== Part 4: controls (reviewed verify_hex_supremum_b19.py, read-only)")
    before = len(b19.CHECKS)
    b19.check_square_control()
    b19.check_pipeline_square_control()
    sub = b19.CHECKS[before:]
    record("CONTROLS of the M1-B19 verifier on the square substrate, rerun unchanged: all pass "
           "(the layer equations, of which A1 is the singleton case, keep the known saturating walk)",
           len(sub) >= 5 and all(c[1] for c in sub), f"{sum(c[1] for c in sub)}/{len(sub)}")
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (PH refutation, H25, Stage A).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
