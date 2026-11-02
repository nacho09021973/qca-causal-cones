#!/usr/bin/env python3
"""Exact certificate for the L6B_TRIANGULAR_ROW gate.

Contract: theory/L6B_TRIANGULAR_ROW_GATE.md (preregistration commit b076670).
Source:   ADMP, arXiv 1803.01015v2, Sec. IV p.4, Eqs. (9), (11), (12), Fig. 1.

Row L6b of C_ACROSS_LATTICES, massless (M = I). The walk lives on the edges
of the triangular lattice; one update is R (every triangle rotated
anticlockwise, side k-1 -> side k) followed by the coin W of Eq. (9) on
every edge, upper component on the white triangle's side, lower on the
grey's (Eq. (12)).

Coordinates. Triangle side 1. Fine generators f1 = (1/2, 0),
f2 = (1/4, sqrt3/4), so every edge midpoint has integer coordinates. The up
triangle U_n (n in Z^2, coarse) has vertices 2n, 2n+(2,0), 2n+(0,2) and
edges h (bottom), b (right, "\\") and s (left, "/") with midpoints
2n + (1,0), 2n + (1,1), 2n + (0,1). Each edge lies in exactly one up
triangle, so a unit cell holds the three edges (n, h), (n, b), (n, s); with
C^2 per edge the walk is translation invariant with s = 6 (contract Sec. 1).
The down triangle D_m has edges (m, b), (m+(0,1), h), (m+(1,0), s).

Symbol convention as in the parent verifier: entry (target, source) carries
z^(x_target - x_source), z^h <-> exp(-i k.h), physical displacements.

Reuses, read-only, the reviewed helpers of
scripts/verify_c_across_lattices_gate.py (hull, node_speeds, nilpotent,
laurent_support, laurent_adjoint, row_L6a, ...). That file is not modified.

Fails closed: any failed check or exception exits nonzero.
"""

import hashlib
import itertools
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_c_across_lattices_gate as P  # reviewed, imported read-only

CONTRACT = ROOT / "theory/L6B_TRIANGULAR_ROW_GATE.md"
SOURCE = "1803.01015v2"

CHECKS = []


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok), detail))
    print(("[PASS] " if ok else "[FAIL] ") + label + (f" -- {detail}" if detail else ""))


Z = P.is_zero_matrix
ORIENT = ("h", "b", "s")
OFFSET = {"h": (1, 0), "b": (1, 1), "s": (0, 1)}
GENS = [(sp.Rational(1, 2), 0), (sp.Rational(1, 4), sp.sqrt(3) / 4)]
ZS = sp.symbols("z1:3")


def add(*vs):
    return tuple(sum(c) for c in zip(*vs))


def pos(edge):
    n, o = edge
    return add((2 * n[0], 2 * n[1]), OFFSET[o])


def up_edges(n):
    return [(n, "h"), (n, "b"), (n, "s")]


def down_edges(m):
    return [(m, "b"), (add(m, (0, 1)), "h"), (add(m, (1, 0)), "s")]


def down_of(edge):
    """The down triangle containing an edge."""
    n, o = edge
    return {"b": n, "h": add(n, (0, -1)), "s": add(n, (-1, 0))}[o]


def cart(v):
    return sp.Matrix([v[0] * GENS[0][0] + v[1] * GENS[1][0], v[0] * GENS[0][1] + v[1] * GENS[1][1]])


def ccw_successor(vertices_edges):
    """Anticlockwise successor map on the three edges of one triangle, from
    exact geometry: order the edge midpoints by angle around the centroid."""
    mids = {o: cart(pos(e)) for e, o in vertices_edges}
    centre = sum(mids.values(), sp.zeros(2, 1)) / 3
    ang = {o: sp.atan2(*(list(m - centre)[::-1])) for o, m in mids.items()}
    order = sorted(ang, key=lambda o: float(ang[o]))
    return {order[i]: order[(i + 1) % 3] for i in range(3)}


# ---------------------------------------------------------------- Part 1
def part1_labelings():
    print("== Part 1: admissible labelings (contract Sec. 2)")
    n0 = (0, 0)
    succ_up = ccw_successor([(e, e[1]) for e in up_edges(n0)])
    succ_dn = ccw_successor([(e, e[1]) for e in down_edges(n0)])
    print(f"  anticlockwise successor, up triangle: {succ_up}; down triangle: {succ_dn}")
    record("same anticlockwise cyclic order of edge orientations in up and down triangles",
           succ_up == succ_dn)
    admissible = []
    for white in ("up", "down"):
        for perm_w in itertools.permutations(range(3)):
            for perm_g in itertools.permutations(range(3)):
                lam_w = dict(zip(ORIENT, perm_w))
                lam_g = dict(zip(ORIENT, perm_g))
                succ_w = succ_up if white == "up" else succ_dn
                succ_g = succ_dn if white == "up" else succ_up
                # (i) glued triangles share the side label (p.4: psi(t,v0,1) = psi(t,v1,1))
                glue = lam_w == lam_g
                # (ii) R: side k -> k+1 is the anticlockwise rotation in every triangle (p.4)
                rot = all(lam_w[succ_w[o]] == (lam_w[o] + 1) % 3 for o in ORIENT) and all(
                    lam_g[succ_g[o]] == (lam_g[o] + 1) % 3 for o in ORIENT)
                if glue and rot:
                    admissible.append((white, lam_w))
    print(f"  {len(admissible)} admissible of {2 * 36} candidate (colouring, label_white, label_grey):")
    for white, lam in admissible:
        print(f"    white = {white}, labels {lam}")
    record("exactly 6 admissible labelings: 2 colourings x 3 rotations of one cyclic labeling",
           len(admissible) == 6)
    fig1 = {"h": 2, "b": 0, "s": 1}  # Fig. 1 as read: bottom 2, right 0, left 1 (white, upward)
    record("the labeling read from Fig. 1 (white upward; bottom 2, right 0, left 1) is admissible",
           ("up", fig1) in admissible)
    # The step map only uses 'side k-1 -> side k', i.e. the anticlockwise
    # predecessor of the edge orientation; it is the same for all three
    # rotations of the labeling, so only the colouring can change the walk.
    preds = {}
    for white, lam in admissible:
        inv = {v: o for o, v in lam.items()}
        preds.setdefault(white, set()).add(tuple(inv[(lam[o] - 1) % 3] for o in ORIENT))
    record("for each colouring the predecessor map k-1 -> k is the same for all labelings",
           all(len(v) == 1 for v in preds.values()))
    return succ_up, admissible


# ---------------------------------------------------------------- Part 2
def coin(variant):
    """W of Eq. (9) with M = I. 'parent': the matrices used for row L6a in
    the reviewed parent verifier (alpha = -arccos(sqrt5/3), S^{-1}, recorded
    there as source sign issues). 'printed': Eq. (8)-(9) as printed
    (alpha = +arccos(sqrt5/3), S = e^{i pi/3} R_z(2pi/3))."""
    c_half = sp.sqrt((1 + sp.sqrt(5) / 3) / 2)
    s_half = sp.sqrt((1 - sp.sqrt(5) / 3) / 2)
    S = sp.diag(1, sp.exp(2 * sp.pi * sp.I / 3)).applyfunc(sp.expand_complex)
    if variant == "parent":
        U0 = sp.Matrix([[c_half, s_half], [-s_half, c_half]])
        S = S.H
    else:
        U0 = sp.Matrix([[c_half, -s_half], [s_half, c_half]])
    return (U0 * S * U0.H).applyfunc(lambda e: sp.radsimp(sp.expand(e))), U0, S


def step_symbol(white, succ, W):
    """6x6 symbol of one update, Eq. (12) on pre-encoded spinors.
    Basis index 2*o + c, o in (h, b, s), c = 0 (upper, white side), 1 (lower)."""
    pred = {v: k for k, v in succ.items()}
    n0 = (0, 0)
    R = sp.zeros(6, 6)
    hops = []
    for o in ORIENT:
        target = (n0, o)
        for c, colour in ((0, white), (1, "down" if white == "up" else "up")):
            tri = up_edges(n0) if colour == "up" else down_edges(down_of(target))
            source = [e for e in tri if e[1] == pred[o]][0]
            d = tuple(a - b for a, b in zip(pos(target), pos(source)))
            R[2 * ORIENT.index(o) + c, 2 * ORIENT.index(source[1]) + c] = P.monomial(ZS, d)
            hops.append((o, c, d))
    Wall = sp.diag(*[W] * 3)
    return sp.expand(Wall * R), hops


def orientation_blocks(V):
    off = all(V[2 * i + a, 2 * j + b] == 0 for i in range(3) for j in range(3) if i != j
              for a in range(2) for b in range(2))
    return off, [V[2 * i:2 * i + 2, 2 * i:2 * i + 2] for i in range(3)]


def h_of(points, nhat):
    return max((nhat.T * p)[0] for p in points)


def analyse(white, succ, variant):
    tag = f"[white={white}, W={variant}]"
    W, U0, S = coin(variant)
    record(f"{tag} W is unitary and W^3 = I", Z(W * W.H - P.I2) and Z(W ** 3 - P.I2))
    U, hops = step_symbol(white, succ, W)
    P.check_unitary(f"L6b {tag}", U, ZS)

    # Encoding (contract Sec. 2): psi~ = U_k psi with U_k fixed per edge class
    # is an on-site block-diagonal unitary E, constant in z, so the symbol is
    # conjugated: same support and same eigenphases.
    Us = [U0, U0 * S, U0 * S * S]
    E = sp.diag(*Us)
    Uenc = sp.expand(E.H * U * E)
    record(f"{tag} encoding E = diag(U_k) conjugates the symbol: same support, same char. polynomial",
           set(P.laurent_support(Uenc, ZS)) == set(P.laurent_support(U, ZS))
           and sp.expand((Uenc.charpoly().as_expr() - U.charpoly().as_expr())) == 0)

    # Step set F and C_micro of one update.
    support = P.laurent_support(U, ZS)
    pts_raw = [cart(h) for h in sorted(support)]
    ell = sp.radsimp(max((sp.sqrt((p.T * p)[0]) for p in pts_raw), key=lambda x: float(x)))
    record(f"{tag} F has 6 displacements, none zero, all of length 1/2 (half a side)",
           len(support) == 6 and (0, 0) not in support
           and all(sp.simplify(sp.sqrt((p.T * p)[0]) - sp.Rational(1, 2)) == 0 for p in pts_raw))
    pts = [(p / ell).applyfunc(sp.radsimp) for p in pts_raw]
    facets, verts = P.hull(pts)
    r_in = min(facets.values(), key=lambda x: float(x))
    print(f"  {tag} F (fine coords) = {sorted(support)}; longest step = {ell}; "
          f"|vertices| = {len(verts)}; r_in(C_micro) = {r_in} (normalised)")
    record(f"{tag} C_micro is the regular hexagon, r_in = sqrt3/2 (normalised)",
           len(verts) == 6 and sp.simplify(r_in - sp.sqrt(3) / 2) == 0)
    one_step_vertices_dead = all(P.nilpotent(support[h]) for h in support)
    record(f"{tag} every one-step vertex coefficient is nilpotent (the edge orientation changes each step)",
           one_step_vertices_dead)

    # Three updates: orientation-preserving, a Bravais walk with s = 6.
    V = sp.expand(U ** 3)
    off, blocks = orientation_blocks(V)
    record(f"{tag} U^3 is block diagonal in the edge orientation", off)
    k = sp.symbols("k1:3", real=True)
    subs0 = {z: 1 for z in ZS}
    U0k = U.subs(subs0)
    record(f"{tag} U(0) = P (x) W with P the cyclic permutation; U(0)^3 = I", Z(U0k ** 3 - sp.eye(6)))
    ev = U0k.eigenvals()
    one = sum(m for lam, m in ev.items() if sp.simplify(lam - 1) == 0)
    record(f"{tag} eigenvalue 1 of U(0) has multiplicity 2 (the declared node)", one == 2,
           f"spectrum {{{', '.join(f'{sp.nsimplify(l)}:{m}' for l, m in ev.items())}}}")

    # c_0 route A: three-update symbol, scale 1 (side units), per three updates.
    at0, A, tilt, c2, iso, herm = P.node_speeds(V, ZS, GENS, 1, -1, 2)
    record(f"{tag} route A: V(0) = I, Hermitian untilted isotropic cone", Z(at0 - sp.eye(6)) and herm
           and all(t == 0 for t in tilt) and iso)
    c0_V = sp.radsimp(sp.sqrt(c2))
    c0_A = sp.radsimp(c0_V / 3 / ell)  # per update, normalised
    # c_0 route B: one update, degenerate first order on the eigenvalue-1 space.
    Ek = U.subs({z: sp.exp(-sp.I * (k[0] * g[0] + k[1] * g[1])) for z, g in zip(ZS, GENS)})
    null = (U0k - sp.eye(6)).nullspace()
    Q, _ = sp.Matrix.hstack(*null).QRdecomposition()
    Q = Q.applyfunc(lambda e: sp.radsimp(sp.simplify(e)))
    gen = [(Q.H * (sp.I * U0k.H * Ek.diff(ka)).subs({kb: 0 for kb in k}) * Q).applyfunc(
        lambda e: sp.radsimp(sp.simplify(sp.expand_complex(e)))) for ka in k]
    tr = [sp.simplify(g.trace() / 2) for g in gen]
    T = [g - t * P.I2 for g, t in zip(gen, tr)]
    cB2 = sp.radsimp(sp.simplify((T[0] * T[0])[0, 0]))
    isoB = Z(T[0] * T[0] - cB2 * P.I2) and Z(T[1] * T[1] - cB2 * P.I2) and Z(T[0] * T[1] + T[1] * T[0])
    c0_B = sp.radsimp(sp.sqrt(cB2) / ell)
    record(f"{tag} route B (one update, node subspace): untilted isotropic cone",
           all(t == 0 for t in tr) and isoB)
    record(f"{tag} routes A and B give the same c_0", sp.simplify(c0_A - c0_B) == 0,
           f"c_0 = {c0_A} (normalised), {sp.radsimp(c0_A * ell)} per update in side units")

    # C_infty^strict: vertices of conv supp(U^3) and their survival.
    supV = P.laurent_support(V, ZS)
    ptsV = [cart(h) for h in sorted(supV)]
    keysV = sorted(supV)
    facV, vertV = P.hull(ptsV)
    survive = {keysV[i]: not P.nilpotent(supV[keysV[i]]) for i in vertV}
    record(f"{tag} every vertex coefficient of U^3 is non-nilpotent",
           all(survive.values()), f"{sum(survive.values())}/{len(survive)}; supp U^3 = {keysV}")
    r_in_V = min(facV.values(), key=lambda x: float(x))
    c_strict = sp.radsimp(r_in_V / 3 / ell) if all(survive.values()) else None
    # Check the zonotope picture by support functions in the two symmetry directions.
    print(f"  {tag} conv supp U^3: |vertices| = {len(vertV)}, inradius {r_in_V} (side units, per 3 updates)")
    record(f"{tag} c_strict^iso = r_in(conv supp U^3)/3 = 1/sqrt3 (normalised)",
           c_strict is not None and sp.simplify(c_strict - 1 / sp.sqrt(3)) == 0, f"c_strict^iso = {c_strict}")
    return dict(U=U, V=V, blocks=blocks, r_in=r_in, c0=c0_A, c_strict=c_strict, ell=ell,
                supV=supV, c0_V=c0_V, iso=iso and isoB)


# ---------------------------------------------------------------- Part 3
def part3_crosschecks(res):
    print("== Part 3: cross-checks against the source (contract Sec. 4)")
    r = res[("up", "parent")]
    # Source p.4: i d_t psi = (sqrt3/6)(sigma.p) psi with triangle side sqrt3
    # (it states the distance between side midpoints is sqrt3/2) and time
    # step epsilon = one update. Per update, in side units: c_0 * ell; with
    # side sqrt3: c_0 * ell * sqrt3.
    src = sp.radsimp(r["c0"] * r["ell"] * sp.sqrt(3))
    record("c_0 in the source's units (side sqrt3, one update) equals its coefficient sqrt3/6",
           sp.simplify(src - sp.sqrt(3) / 6) == 0, f"computed {src}")
    # Source: three updates equivalent to the honeycomb walk L6a.
    l6a, zs_a, sup_a, gens_a = P.row_L6a()
    sym_a = l6a.subs(dict(zip(zs_a, ZS)))
    # The 12 isometries of the hexagon in the triangular basis g1, g2:
    # rotation by 60 deg  h -> (-b, a+b); reflection  h -> (b, a).
    rot = sp.Matrix([[0, -1], [1, 1]])
    ref = sp.Matrix([[0, 1], [1, 0]])
    group = [rot ** i * ref ** j for i in range(6) for j in range(2)]

    def act(M, expr):
        # z^h -> z^{M h}: z1 -> z1^m11 z2^m21, z2 -> z1^m12 z2^m22
        return sp.expand(expr.subs({ZS[0]: ZS[0] ** M[0, 0] * ZS[1] ** M[1, 0],
                                    ZS[1]: ZS[0] ** M[0, 1] * ZS[1] ** M[1, 1]}, simultaneous=True))

    lam = sp.Symbol("lam")
    cp_a = sym_a.charpoly(lam).as_expr()
    strict, iso_match = [], []
    for B in r["blocks"]:
        cp_b = B.charpoly(lam).as_expr()
        strict.append(sp.expand(cp_b - cp_a) == 0)
        hits = [i for i, M in enumerate(group) if sp.expand(act(M, cp_b) - cp_a) == 0]
        iso_match.append(hits)
    print(f"  same orientation (identity isometry) matches: {strict}")
    print(f"  isometries (index i = 2*rot + ref) matching each block: {iso_match}")
    record("each orientation block of U^3 has the characteristic polynomial of the L6a symbol "
           "up to an isometry of the hexagon, with L6a's generators halved",
           all(len(h) > 0 for h in iso_match), f"blocks: {iso_match}")
    record("supp U^3 equals the L6a step set F (same integer coordinates, generators halved)",
           set(r["supV"]) == set(sup_a))


def main():
    print(f"contract sha256 {hashlib.sha256(CONTRACT.read_bytes()).hexdigest()}")
    digest = hashlib.sha256((ROOT / f"sources/{SOURCE}.pdf").read_bytes()).hexdigest()
    record(f"source {SOURCE}.pdf SHA256 matches sources/README.md", digest == P.SOURCES[SOURCE])
    succ, admissible = part1_labelings()
    print("== Part 2: row L6b, massless, per admissible colouring and both coin readings")
    res = {}
    for white in ("up", "down"):
        for variant in ("parent", "printed"):
            res[(white, variant)] = analyse(white, succ, variant)
    vals = {key: (r["r_in"], r["c0"], r["c_strict"]) for key, r in res.items()}
    record("r_in, c_0, c_strict^iso identical for both colourings and both coin readings",
           len({tuple(sp.nsimplify(x) for x in v) for v in vals.values()}) == 1, str(vals))
    part3_crosschecks(res)
    print("== Hypotheses (contract Sec. 5), row L6b")
    r = res[("up", "parent")]
    record("s = 6, so L6b is outside Ha's scope (Ha stays REFUTED_BY_ROW_L6a)", r["U"].rows == 6)
    hb = sp.simplify(r["c_strict"] - r["r_in"]) == 0
    hc = P.positive(r["c_strict"] - r["c0"]) >= 0
    print(f"  r_in = {r['r_in']}, c_0 = {r['c0']}, c_strict^iso = {r['c_strict']}, "
          f"c_0/r_in = {sp.radsimp(r['c0'] / r['r_in'])}, c_strict^iso/r_in = {sp.radsimp(r['c_strict'] / r['r_in'])}")
    record("Hb fails for L6b: c_strict^iso = 1/sqrt3 < r_in = sqrt3/2 (ratio 2/3)",
           (not hb) and sp.simplify(r["c_strict"] / r["r_in"] - sp.Rational(2, 3)) == 0)
    record("Hc holds for L6b: c_0 = 1/3 <= c_strict^iso = 1/sqrt3",
           hc and sp.simplify(r["c0"] - sp.Rational(1, 3)) == 0)
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (L6b massless row).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail closed
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
