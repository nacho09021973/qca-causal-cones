"""Exact checks for the HEX_CEILING gate (L0 lattice-grid step and T1).

Contract: theory/HEX_CEILING_GATE.md, preregistered at 8c56ced.
Run from the repository root:

  python -B scripts/verify_hex_ceiling_gate.py

Fail-closed, SymPy only, zero tolerance. Reuses read-only helpers of the
reviewed verify_c_across_lattices_gate.py (laurent_support, hull,
node_speeds, nilpotent, is_zero_matrix); that file is not modified and its
own check list is not used.

What is certified here:
- L0, grid step: for a lattice edge direction d of a triangular-lattice
  polygon, h . Rot90(d) is an integer multiple of sqrt3/2 for every lattice
  vector h, so the frequencies along a facet normal lie on a uniform grid
  (the remaining step, the classical scalar Bernstein inequality, is prior
  art and is applied in the report, not here).
- T1 algebra, symbolic in the pairwise overlaps g_ij = t_i . t_j and the
  orientation theta0: the traceless part of sum_ij g_ij a_i a_j^T vanishes
  iff g_12 = g_13 = g_23; then c0_raw^2 = (3/2) l^2 (1 - g); the Gram matrix
  is PSD iff -1/2 <= g <= 1; hence c0/r_in <= sqrt3/2 with equality iff
  g = -1/2.
- An explicit T1 walk with g = -1/2 (coplanar Bloch vectors at 120 deg),
  built as a symbol and certified exactly: unitarity, F = {0, +-2 a_j},
  regular hexagonal hull, node, isotropy, c0 = 3/4, c0/r_in = sqrt3/2;
  and the ADMP overlaps g = 1/3 giving c0 = 1/2.
What is not certified here: the reduction of a general n = 3 antipodal
walk to the product form, the hull argument for all g, and the Bernstein
step; these are in the report.
"""
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_c_across_lattices_gate as base  # reviewed, read-only

CHECKS = []
SX, SY, SZ, I2 = base.SX, base.SY, base.SZ, base.I2
R3 = sp.sqrt(3)
G1 = sp.Matrix([1, 0])
G2 = sp.Matrix([sp.Rational(1, 2), R3 / 2])


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    print(("[PASS] " if ok else "[FAIL] ") + label + (f" -- {detail}" if detail else ""))


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def check_L0_grid():
    p, q, a, b = sp.symbols("p q a b", integer=True)
    d = p * G1 + q * G2
    h = a * G1 + b * G2
    rot = sp.Matrix([-d[1], d[0]])
    value = sp.expand((h.T * rot)[0])
    record("L0: h . Rot90(d) = (sqrt3/2)(b p - a q) for lattice h = a g1 + b g2, d = p g1 + q g2",
           sp.simplify(value - R3 / 2 * (b * p - a * q)) == 0)


def check_T1_algebra():
    th, ell = sp.symbols("theta0 ell", positive=True)
    g12, g13, g23, g = sp.symbols("g12 g13 g23 g", real=True)
    a = [ell * sp.Matrix([sp.cos(th + 2 * sp.pi * j / 3), sp.sin(th + 2 * sp.pi * j / 3)]) for j in range(3)]
    G = sp.Matrix([[1, g12, g13], [g12, 1, g23], [g13, g23, 1]])
    M = sp.zeros(2, 2)
    for i in range(3):
        for j in range(3):
            M += G[i, j] * a[i] * a[j].T
    M = M.applyfunc(lambda e: sp.simplify(sp.expand_trig(e)))
    traceless = M - M.trace() / 2 * sp.eye(2)
    eqs = [sp.simplify(traceless[0, 0]), sp.simplify(traceless[0, 1])]
    # linear in (g12, g13, g23); solve for all theta0
    jac = sp.Matrix([[sp.diff(e, x) for x in (g12, g13, g23)] for e in eqs]).applyfunc(sp.simplify)
    const = [sp.simplify(e.subs({g12: 0, g13: 0, g23: 0})) for e in eqs]
    record("T1: traceless part is linear homogeneous in (g12, g13, g23)", all(c == 0 for c in const))
    record("T1: its 2x3 coefficient matrix has rank 2 for every theta0",
           sp.simplify(jac[:, :2].det()) != 0 or sp.simplify(jac[:, 1:].det()) != 0)
    null = jac * sp.Matrix([1, 1, 1])
    record("T1: null space is spanned by (1,1,1): isotropy iff g12 = g13 = g23",
           all(sp.simplify(e) == 0 for e in null))
    Mg = M.subs({g12: g, g13: g, g23: g}).applyfunc(sp.simplify)
    record("T1: at equal overlaps, sum g_ij a_i a_j^T = (3/2) l^2 (1 - g) I",
           all(sp.simplify(e) == 0 for e in (Mg - sp.Rational(3, 2) * ell ** 2 * (1 - g) * sp.eye(2))))
    Gg = G.subs({g12: g, g13: g, g23: g})
    eig = Gg.eigenvals()
    record("T1: Gram eigenvalues are 1 + 2g (once) and 1 - g (twice): PSD iff -1/2 <= g <= 1",
           eig == {1 + 2 * g: 1, 1 - g: 2})
    c0_raw = sp.sqrt(sp.Rational(3, 2) * (1 - g)) * ell
    c0 = c0_raw / (2 * ell)          # longest step 2*ell
    r_in = R3 / 2
    ratio = sp.simplify(c0 / r_in)
    record("T1: c0/r_in = sqrt(1 - g)/sqrt2, maximal at g = -1/2 with value sqrt3/2",
           sp.simplify(ratio - sp.sqrt(1 - g) / sp.sqrt(2)) == 0 and sp.simplify(ratio.subs(g, -sp.Rational(1, 2)) - R3 / 2) == 0)
    record("T1: sqrt3/2 < 1 (the ceiling is not reached in T1)", bool(R3 / 2 < 1))
    record("T1: ADMP overlaps g = 1/3 give c0 = 1/2; g = -1/2 gives c0 = 3/4",
           sp.simplify(c0.subs(g, sp.Rational(1, 3)) - sp.Rational(1, 2)) == 0
           and sp.simplify(c0.subs(g, -sp.Rational(1, 2)) - sp.Rational(3, 4)) == 0)


def t1_walk(tvecs):
    """U(k) = prod_{j=3..1} exp(-i (k.a_j) tau_j), a_j = u_0, u_1, u_2 (unit,
    120 deg), tau_j = t_j . sigma, as a Laurent symbol in z = exp(-i k.g)."""
    zs = sp.symbols("z1:3")
    u = [(1, 0), (-1, 1), (0, -1)]          # u_0, u_1, u_2 in (g1, g2)
    factors = []
    for (tx, ty, tz), uj in zip(tvecs, u):
        tau = tx * SX + ty * SY + tz * SZ
        plus, minus = (I2 + tau) / 2, (I2 - tau) / 2
        factors.append(base.monomial(zs, uj) * plus + base.monomial(zs, base.neg(uj)) * minus)
    return sp.expand(factors[2] * factors[1] * factors[0]), zs


def check_witness():
    tv = [(sp.cos(2 * sp.pi * j / 3), sp.sin(2 * sp.pi * j / 3), 0) for j in range(3)]
    tv = [tuple(sp.nsimplify(x) for x in t) for t in tv]
    overlaps = [sum(a * b for a, b in zip(tv[i], tv[j])) for i, j in ((0, 1), (0, 2), (1, 2))]
    record("witness: Bloch vectors are unit, coplanar, pairwise overlap -1/2",
           all(sp.simplify(sum(x ** 2 for x in t) - 1) == 0 for t in tv)
           and all(sp.simplify(o + sp.Rational(1, 2)) == 0 for o in overlaps))
    symbol, zs = t1_walk(tv)
    adj = base.laurent_adjoint(symbol, zs)
    record("witness: symbol is unitary", base.is_zero_matrix(sp.expand(symbol * adj) - I2))
    support = base.laurent_support(symbol, zs)
    expected = {(-2, 0), (-2, 2), (0, -2), (0, 0), (0, 2), (2, -2), (2, 0)}
    record("witness: composite F = {0, +-2 u_j} (zero coefficient tolerated only at 0)",
           set(support) - {(0, 0)} == expected - {(0, 0)})
    gens = [(1, 0), (sp.Rational(1, 2), R3 / 2)]
    keys = sorted(h for h in support)
    cart = {h: (h[0] * G1 + h[1] * G2) for h in keys}
    L = 2
    pts = [(cart[h] / L).applyfunc(sp.radsimp) for h in keys]
    facets, verts = base.hull(pts)
    r_in = min(facets.values(), key=lambda x: float(x))
    record("witness: hull is the regular hexagon (6 vertices, 6 facets, r_in = sqrt3/2)",
           len(verts) == 6 and len(facets) == 6 and sp.simplify(r_in - R3 / 2) == 0)
    record("witness: every vertex coefficient is non-nilpotent",
           all(not base.nilpotent(support[keys[i]]) for i in verts))
    at0, A, tilt, c2, iso, herm = base.node_speeds(symbol, zs, gens, L, -1, 2)
    c0 = sp.radsimp(sp.sqrt(c2))
    record("witness: U(0) = I, Hermitian untilted isotropic cone",
           base.is_zero_matrix(at0 - I2) and herm and all(t == 0 for t in tilt) and iso)
    record("witness: c0 = 3/4 and c0/r_in = sqrt3/2", c0 == sp.Rational(3, 4)
           and sp.simplify(c0 / r_in - R3 / 2) == 0)


def check_admp():
    xi = sp.sqrt(5) / 3
    tv = [(sp.Rational(2, 3), 0, xi), (-sp.Rational(1, 3), R3 / 3, xi), (-sp.Rational(1, 3), -R3 / 3, xi)]
    overlaps = [sp.simplify(sum(a * b for a, b in zip(tv[i], tv[j]))) for i, j in ((0, 1), (0, 2), (1, 2))]
    record("ADMP: tau_i of Eq. (5) have equal pairwise overlaps g = 1/3", overlaps == [sp.Rational(1, 3)] * 3)
    symbol, zs = t1_walk(tv)
    _, _, _, c2, iso, _ = base.node_speeds(symbol, zs, [(1, 0), (sp.Rational(1, 2), R3 / 2)], 2, -1, 2)
    record("ADMP: product-form symbol gives isotropic c0 = 1/2 (matches Sec. 11 row L6a)",
           iso and sp.radsimp(sp.sqrt(c2)) == sp.Rational(1, 2))


def check_T2_minimal():
    """Minimal-support subclass: F within {0} U vert(H), any s = 2 walk (no
    product form assumed). WLOG (Bloch rotation, joint spatial/Bloch
    rotation, scale): vertices v_k = (cos k pi/3, sin k pi/3), the isotropic
    linear term A(n) = r n.sigma with n in the xy Bloch plane. Saturation
    c_0 = r_in forces, along each facet normal n, U(t n) = e^{-irt} P_+ +
    e^{irt} P_- (report, Bernstein equality / Julia), i.e. layer sums:
    top edge -> P_+(n), bottom edge -> P_-(n), middle layer -> 0."""
    v = [sp.Matrix([sp.cos(sp.pi * k / 3), sp.sin(sp.pi * k / 3)]) for k in range(6)]
    normals = [sp.Matrix([sp.cos(a), sp.sin(a)]) for a in (sp.pi / 6, sp.pi / 2, 5 * sp.pi / 6)]
    layers = []
    for n in normals:
        proj = [sp.nsimplify((vk.T * n)[0]) for vk in v]
        top = [k for k in range(6) if proj[k] == R3 / 2]
        bot = [k for k in range(6) if proj[k] == -R3 / 2]
        mid = [k for k in range(6) if proj[k] == 0]
        layers.append((top, bot, mid))
    record("T2-min: along each facet normal the layers are {top edge, middle (2 vertices + 0), bottom edge}",
           all(len(t) == 2 and len(b) == 2 and len(m) == 2 for t, b, m in layers)
           and [l[0] for l in layers] == [[0, 1], [1, 2], [2, 3]])

    def proj(n, sign):
        return (I2 + sign * (n[0] * SX + n[1] * SY)) / 2
    Pp = [proj(n, 1).applyfunc(sp.nsimplify) for n in normals]
    Pm = [proj(n, -1).applyfunc(sp.nsimplify) for n in normals]
    # generic unknown coefficients for the 6 vertices and the origin
    syms = []
    def gen(name):
        e = sp.symbols(f"{name}_0:8", real=True)
        syms.extend(e)
        return sp.Matrix([[e[0] + sp.I * e[1], e[2] + sp.I * e[3]], [e[4] + sp.I * e[5], e[6] + sp.I * e[7]]])
    X = [gen(f"X{k}") for k in range(6)]
    Z = gen("Z")
    lin = []
    for (top, bot, mid), Pt, Pb in zip(layers, Pp, Pm):
        for M in (X[top[0]] + X[top[1]] - Pt, X[bot[0]] + X[bot[1]] - Pb, X[mid[0]] + X[mid[1]] + Z):
            for e in M:
                e = sp.expand(e)
                lin += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    x0 = syms[:8]
    sol = sp.solve(lin, [s_ for s_ in syms if s_ not in x0], dict=True)
    record("T2-min: layer equations are consistent, with the X0 coefficient free", len(sol) == 1)
    sol = sol[0]
    Zs = Z.subs(sol)
    record("T2-min: layer equations force A_0 = -I/2", base.is_zero_matrix(Zs + I2 / 2))
    Xs = [Xk.subs(sol) for Xk in X]
    pts = [(v[k], Xs[k]) for k in range(6)] + [(sp.zeros(2, 1), Zs)]
    eqs = set()
    blocks = {}
    for h1, A1 in pts:
        for h2, A2 in pts:
            d = tuple(sp.nsimplify(c) for c in (h1 - h2))
            blocks.setdefault(d, [sp.zeros(2), sp.zeros(2)])
            blocks[d][0] += A1 * A2.H
            blocks[d][1] += A2.H * A1
    for d, (m1, m2) in blocks.items():
        target = I2 if all(c == 0 for c in d) else sp.zeros(2)
        for M in (m1 - target, m2 - target):
            for e in M:
                e = sp.expand(e)
                for part in (sp.expand(sp.re(e)), sp.expand(sp.im(e))):
                    if part != 0:
                        eqs.add(part)
    G = sp.groebner(list(eqs), *x0, order="lex")
    uni = [g for g in G.exprs if g.free_symbols == {x0[6]} and sp.degree(g, x0[6]) == 2]
    ok = False
    if uni:
        a2, a1, a0 = sp.Poly(uni[0], x0[6]).all_coeffs()
        disc = sp.simplify(a1 ** 2 - 4 * a2 * a0)
        ok = bool(disc < 0)
        print(f"  T2-min: Groebner element {uni[0]} = 0, discriminant {disc}")
    record("T2-min: unitarity + saturation imply a real quadratic with negative discriminant "
           "(no real solution): the ceiling is not attained with F in {0} U vert(H)", ok)


def check_T2_square_control():
    """Positive control for the saturation method: the square substrate
    F within {0} U {(+-1,+-1)}, facet normals x and y, A(n) = r n.sigma.
    The same layer + unitarity system must be consistent, and the known
    saturating walk exp(-i k_x sigma_x) exp(-i k_y sigma_y) must solve it."""
    verts = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    syms = []
    def gen(name):
        e = sp.symbols(f"{name}_0:8", real=True)
        syms.extend(e)
        return sp.Matrix([[e[0] + sp.I * e[1], e[2] + sp.I * e[3]], [e[4] + sp.I * e[5], e[6] + sp.I * e[7]]])
    X = {v: gen(f"Y{i}") for i, v in enumerate(verts)}
    Z = gen("W")
    Px, Pxm = (I2 + SX) / 2, (I2 - SX) / 2
    Py, Pym = (I2 + SY) / 2, (I2 - SY) / 2
    lin = []
    for M in (X[(1, 1)] + X[(1, -1)] - Px, X[(-1, 1)] + X[(-1, -1)] - Pxm,
              X[(1, 1)] + X[(-1, 1)] - Py, X[(1, -1)] + X[(-1, -1)] - Pym, Z):
        for e in M:
            e = sp.expand(e)
            lin += [sp.expand(sp.re(e)), sp.expand(sp.im(e))]
    free = syms[:8]
    sol = sp.solve(lin, [s_ for s_ in syms if s_ not in free], dict=True)[0]
    pts = [(sp.Matrix(v), X[v].subs(sol)) for v in verts] + [(sp.zeros(2, 1), Z.subs(sol))]
    eqs = set()
    blocks = {}
    for h1, A1 in pts:
        for h2, A2 in pts:
            d = tuple(h1 - h2)
            blocks.setdefault(d, [sp.zeros(2), sp.zeros(2)])
            blocks[d][0] += A1 * A2.H
            blocks[d][1] += A2.H * A1
    for d, (m1, m2) in blocks.items():
        target = I2 if all(c == 0 for c in d) else sp.zeros(2)
        for M in (m1 - target, m2 - target):
            for e in M:
                e = sp.expand(e)
                for part in (sp.expand(sp.re(e)), sp.expand(sp.im(e))):
                    if part != 0:
                        eqs.add(part)
    G = sp.groebner(list(eqs), *free, order="lex")
    record("CONTROL square: saturation system is consistent (Groebner basis != {1})", list(G.exprs) != [1])
    # known walk: (cos kx - i sin kx sx)(cos ky - i sin ky sy), coefficient of shift (a,b)
    # with z^h <-> exp(-i k.h): factor = z_x P_x^+ + z_x^{-1} P_x^-, same for y
    known = Px * Py  # coefficient at (1,1) = P_x^+ P_y^+
    vals = dict(zip(free, [sp.re(known[0, 0]), sp.im(known[0, 0]), sp.re(known[0, 1]), sp.im(known[0, 1]),
                           sp.re(known[1, 0]), sp.im(known[1, 0]), sp.re(known[1, 1]), sp.im(known[1, 1])]))
    record("CONTROL square: the saturating walk exp(-ik_x s_x) exp(-ik_y s_y) solves it",
           all(sp.simplify(e.subs(vals)) == 0 for e in eqs))


def main():
    print("== L0 grid step")
    check_L0_grid()
    print("== T1 algebra")
    check_T1_algebra()
    print("== T1 witness at g = -1/2")
    check_witness()
    print("== T1 consistency with ADMP")
    check_admp()
    print("== T2, minimal-support subclass F in {0} U vert(H)")
    check_T2_minimal()
    print("== positive control on the square substrate")
    check_T2_square_control()
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (L0 grid step, T1, T2 minimal support).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
