"""Exact checks for the C_ACROSS_LATTICES gate.

Contract: theory/C_ACROSS_LATTICES_GATE.md, preregistered at 30672ba.
Run from the repository root:

  python -B scripts/verify_c_across_lattices_gate.py

Fail-closed: any failed check or exception exits nonzero. SymPy only, zero
tolerance, no sampling or fitting.

Part 1 (this revision): for each new row (L5a, L5b, L6a, L6c-L6f) build the
exact Bloch symbol of one complete update from the source equations, check
unitarity and the source's stated algebraic identities, and extract the
composite step set F and the translation group it generates. Row L6b is
reported as not encoded (see SOURCE_GAPS). Later parts (C_micro geometry,
c_0, c_strict^iso, masses) are not yet implemented here.

Conventions (frozen in the contract, Sec. 2):
- moving amplitude by displacement h carries the phase exp(-i k.h); an
  operator that reads the value at X+v therefore moves amplitude by -v;
- in every product the factor with the smallest index acts first;
- lattice vectors are written as integer combinations of two (or three)
  generators g; the Laurent variable z_i stands for exp(-i k.g_i).
"""
import hashlib
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "theory/C_ACROSS_LATTICES_GATE.md"
SOURCES = {
    "1312.2852v1": None,
    "1802.03910v1": None,
    "1803.01015v2": "1d1de6058787437bb712448af11dd6b57d83f73fbe6cb7e6dffd242a45f8a570",
    "1803.01304v1": "9fa0ea34763b4dd01fe2c38d699ecf5358b98b6b1582381f95330c84eb90ff90",
}

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PROJ_L = sp.Matrix([[1, 0], [0, 0]])
PROJ_R = sp.Matrix([[0, 0], [0, 1]])

CHECKS = []
SOURCE_GAPS = {
    "L6b": "ADMP Eq. (12) p.4 places spinors on triangle edges with a "
           "white/grey triangulation whose geometry is fixed only by Fig. 1, "
           "not by the text; the edge-midpoint lattice and the routing "
           "e(v,k) cannot be encoded exactly from the equations. The source "
           "states equivalence with L6a over three updates; not verified.",
}


def record(label, ok, detail=""):
    CHECKS.append((label, bool(ok), detail))
    print(("[PASS] " if ok else "[FAIL] ") + label + (f" -- {detail}" if detail else ""))


def is_zero_matrix(matrix):
    return all(sp.simplify(sp.radsimp(sp.expand(entry))) == 0 for entry in matrix)


def u2(alpha, xi, zeta, theta):
    """JDW Eq. (1), 1803.01304v1 p.1."""
    return sp.exp(sp.I * alpha) * sp.Matrix([
        [sp.exp(sp.I * xi) * sp.cos(theta), sp.exp(sp.I * zeta) * sp.sin(theta)],
        [-sp.exp(-sp.I * zeta) * sp.sin(theta), sp.exp(-sp.I * xi) * sp.cos(theta)],
    ])


def monomial(zs, displacement):
    return sp.prod([z ** int(a) for z, a in zip(zs, displacement)])


def neg(v):
    return tuple(-a for a in v)


def laurent_adjoint(matrix, zs):
    """Adjoint on the unit torus: conjugate coefficients, z -> 1/z."""
    sub = {sp.conjugate(z): 1 / z for z in zs}
    return matrix.applyfunc(lambda e: sp.conjugate(sp.expand(e)).subs(sub)).T


def laurent_support(matrix, zs, bound=8):
    """Displacements h (integer generator coordinates) with nonzero
    coefficient matrix, for a symbol written with z^h <-> exp(-i k.h)."""
    shift = sp.prod([z ** bound for z in zs])
    coefficients = {}
    for r in range(matrix.rows):
        for c in range(matrix.cols):
            expr = sp.expand(shift * matrix[r, c])
            if expr == 0:
                continue
            poly = sp.Poly(expr, *zs)
            for powers, coeff in poly.terms():
                h = tuple(p - bound for p in powers)
                coefficients.setdefault(h, sp.zeros(matrix.rows, matrix.cols))
                coefficients[h][r, c] += coeff
    return {h: m for h, m in coefficients.items() if not is_zero_matrix(m)}


def check_unitary(label, symbol, zs):
    product = sp.expand(symbol * laurent_adjoint(symbol, zs))
    record(f"{label}: symbol is unitary (U U^dagger = I on |z|=1)",
           is_zero_matrix(product - sp.eye(symbol.rows)))


def lattice_index(vectors):
    """|det| of the integer lattice spanned by integer vectors in Z^d,
    relative to the generator lattice (1 = they generate all of it)."""
    d = len(vectors[0])
    m = sp.Matrix(vectors).T
    hnf_rank = m.rank()
    if hnf_rank < d:
        return 0
    from sympy.matrices.normalforms import smith_normal_form
    snf = smith_normal_form(m, domain=sp.ZZ)
    return sp.prod([abs(snf[i, i]) for i in range(d)])


def report_row(label, support, generators):
    cart = {h: sum((a * sp.Matrix(g) for a, g in zip(h, generators)),
                   sp.zeros(len(generators[0]), 1)) for h in support}
    lengths = {h: sp.sqrt(sum(x ** 2 for x in v)) for h, v in cart.items()}
    longest = max(lengths.values(), key=lambda x: float(x))
    nonzero = [h for h in support if any(h)]
    index = lattice_index(nonzero) if nonzero else 0
    print(f"  {label}: |F| = {len(support)}, contains 0: {tuple([0]*len(generators)) in support}")
    for h in sorted(support):
        v = cart[h]
        print(f"    h={h}  cart={tuple(sp.nsimplify(x) for x in v)}  |h|={sp.nsimplify(lengths[h])}")
    print(f"    longest |h| = {sp.nsimplify(longest)}; index of <F> in generator lattice = {index}")
    return cart, longest, index


# ---------------------------------------------------------------- L5a
def row_L5a():
    """Farrelly-Short 1312.2852v1 Eqs. (20)-(21) p.4-5:
    U_D = T_x T_y T_z, T_b = S_b |up_b><up_b| + S_b^dagger |down_b><down_b|,
    S_b shifts by +1 along b. 'U_D = T_x T_y T_z' as an operator product
    means T_z acts first."""
    zs = sp.symbols("z1:4")
    paulis = (SX, SY, SZ)
    T = []
    for b in range(3):
        up = (I2 + paulis[b]) / 2
        down = (I2 - paulis[b]) / 2
        e = [0, 0, 0]
        e[b] = 1
        T.append(monomial(zs, e) * up + monomial(zs, neg(e)) * down)
    symbol = sp.expand(T[0] * T[1] * T[2])
    check_unitary("L5a", symbol, zs)
    support = laurent_support(symbol, zs)
    gens = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    report_row("L5a", support, gens)
    expected = {(a, b, c) for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)}
    record("L5a: composite step set is {+-1}^3 (BCC, as the source remarks)",
           set(support) == expected)
    return symbol, zs, support, gens


# ---------------------------------------------------------------- L5b
def row_L5b():
    """Mlodinow-Brun 1802.03910v1 Eq. (23) p.5, massless (theta = 0):
    U = (S_X P_X^+ + S_X^dag P_X^-)(S_Y ...)(S_Z ...), with
    Delta P_i = P_i^+ - P_i^- mutually anticommuting involutions and a coin
    Q anticommuting with all three (Eqs. (25)-(27) p.6, p.7), so the four
    generate the irreducible complex Clifford representation on C^4. A
    concrete choice is fixed here; Q is used only to check that choice."""
    zs = sp.symbols("z1:4")
    kron = sp.kronecker_product
    dP = (kron(SX, SX), kron(SX, SY), kron(SX, SZ))
    Q = kron(SZ, I2)
    gens4 = list(dP) + [Q]
    ok = all(is_zero_matrix(g * g - sp.eye(4)) for g in gens4) and all(
        is_zero_matrix(gens4[i] * gens4[j] + gens4[j] * gens4[i])
        for i in range(4) for j in range(i + 1, 4))
    record("L5b: Delta P_X,Y,Z and Q are mutually anticommuting involutions on C^4", ok)
    T = []
    for b in range(3):
        e = [0, 0, 0]
        e[b] = 1
        plus = (sp.eye(4) + dP[b]) / 2
        minus = (sp.eye(4) - dP[b]) / 2
        T.append(monomial(zs, e) * plus + monomial(zs, neg(e)) * minus)
    symbol = sp.expand(T[0] * T[1] * T[2])
    check_unitary("L5b", symbol, zs)
    support = laurent_support(symbol, zs)
    gens = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    report_row("L5b", support, gens)
    expected = {(a, b, c) for a in (-1, 1) for b in (-1, 1) for c in (-1, 1)}
    record("L5b: composite step set is {+-1}^3 (BCC)", set(support) == expected)
    return symbol, zs, support, gens


# ---------------------------------------------------------------- L6a
def row_L6a():
    """ADMP 1803.01015v2 p.3, massless: Eq. (7) with M = I,
    prod_{i=0}^{2} U_i^dag T_i U_i = prod_i sum_s Pi_i^s T(i, s eps),
    Pi_i^s the eigenprojectors of tau_i (Eq. (5)), T(i, s eps) the
    translation by s u_i (u_i Eq. (4)). Factor i = 0 acts first, as in
    Eq. (10). Lattice coordinates: g1 = u_0 = (1,0), g2 = (1/2, sqrt3/2),
    so u_0 -> (1,0), u_1 -> (-1,1), u_2 -> (0,-1)."""
    xi = sp.sqrt(5) / 3
    tau = [sp.Rational(2, 3) * SX + xi * SZ,
           -sp.Rational(1, 3) * SX + sp.sqrt(3) / 3 * SY + xi * SZ,
           -sp.Rational(1, 3) * SX - sp.sqrt(3) / 3 * SY + xi * SZ]
    record("L6a: tau_i are involutions (Eq. (5) C1)",
           all(is_zero_matrix(t * t - I2) for t in tau))
    px, py = sp.symbols("p_x p_y", real=True)
    pis = [sp.cos(2 * sp.pi * i / 3) * px + sp.sin(2 * sp.pi * i / 3) * py for i in range(3)]
    record("L6a: sum_i tau_i pi_i = p_x sigma_x + p_y sigma_y (C2)",
           is_zero_matrix(sum((t * p for t, p in zip(tau, pis)), sp.zeros(2)) - px * SX - py * SY))
    record("L6a: sum_i tau_i = sqrt5 sigma_z (Eq. (5))",
           is_zero_matrix(tau[0] + tau[1] + tau[2] - sp.sqrt(5) * SZ))
    zs = sp.symbols("z1:3")
    u = [(1, 0), (-1, 1), (0, -1)]
    factors = []
    for i in range(3):
        plus = (I2 + tau[i]) / 2
        minus = (I2 - tau[i]) / 2
        factors.append(monomial(zs, u[i]) * plus + monomial(zs, neg(u[i])) * minus)
    symbol = sp.expand(factors[2] * factors[1] * factors[0])
    check_unitary("L6a", symbol, zs)

    # Encoded form Eq. (10): W T2 W T1 W T0 with W = U0 S U0^dag (M = I),
    # U0 = R_y(alpha) = exp(-i alpha sigma_y/2), S = e^{i pi/3} R_z(2pi/3).
    S = (sp.exp(sp.I * sp.pi / 3) * sp.diag(sp.exp(-sp.I * sp.pi / 3), sp.exp(sp.I * sp.pi / 3))
         ).applyfunc(lambda e: sp.expand_complex(sp.expand(e)))  # radicals: diag(1, e^{2 pi i/3})
    record("L6a: S cubes to the identity (p.3)", is_zero_matrix(S ** 3 - I2))
    signs = {}
    # Half-angle radicals of alpha = sign*arccos(sqrt5/3), so that every
    # entry is a real radical and .H simplifies exactly.
    c_half = sp.sqrt((1 + sp.sqrt(5) / 3) / 2)
    s_half = sp.sqrt((1 - sp.sqrt(5) / 3) / 2)

    def ry(sign):
        return sp.Matrix([[c_half, -sign * s_half], [sign * s_half, c_half]])

    for sign in (1, -1):
        U0 = ry(sign)
        signs[sign] = is_zero_matrix(U0 * tau[0] * U0.H - SZ)
    print(f"  L6a: sigma_z = R_y(alpha) tau_0 R_y(alpha)^dag holds for "
          f"alpha=+arccos(sqrt5/3): {signs[1]}, alpha=-arccos(sqrt5/3): {signs[-1]}")
    record("L6a: SOURCE SIGN ISSUE recorded: Eq. (8) holds for alpha = -arccos(sqrt5/3) "
           "only, not the printed +arccos(sqrt5/3)", (not signs[1]) and signs[-1])
    U0 = ry(1 if signs[1] else -1)
    printed = [U0, U0 * S, U0 * S * S]
    printed_ok = all(is_zero_matrix(Ui.H * SZ * Ui - t) for Ui, t in zip(printed, tau))
    swapped = is_zero_matrix(printed[1].H * SZ * printed[1] - tau[2])
    print(f"  L6a: with the printed S, U_i^dag sigma_z U_i = tau_i: {printed_ok}; "
          f"U_0 S gives tau_2 instead: {swapped}")
    record("L6a: SOURCE SIGN ISSUE recorded: printed S orders the tau_i backwards",
           (not printed_ok) and swapped)
    S = S.H  # use S^{-1}; Eq. (5) with C1-C2 is the primary definition
    Us = [U0, U0 * S, U0 * S * S]
    record("L6a: with S^{-1}, tau_i = U_i^dag sigma_z U_i for i = 0, 1, 2",
           all(is_zero_matrix(Ui.H * SZ * Ui - t) for Ui, t in zip(Us, tau)))
    W = U0 * S * U0.H
    Tp = [monomial(zs, ui) * PROJ_L + monomial(zs, neg(ui)) * PROJ_R for ui in u]
    encoded = sp.expand(W * Tp[2] * W * Tp[1] * W * Tp[0])
    # Eq. (7) -> (10): U_{i+1} U_i^dag = W and U_2^dag = U_0^dag W (S^3 = I),
    # hence prod_i U_i^dag T_i U_i = U_0^dag (W T2 W T1 W T0) U_0.
    record("L6a: Eq. (7) symbol = U_0^dag (Eq. (10) symbol) U_0 exactly",
           is_zero_matrix(sp.expand(U0 * symbol * U0.H) - encoded))
    support = laurent_support(symbol, zs)
    gens = [(1, 0), (sp.Rational(1, 2), sp.sqrt(3) / 2)]
    report_row("L6a", support, gens)
    return symbol, zs, support, gens


# ---------------------------------------------------------------- JDW
def jdw_shift(zs, read_L, read_R):
    """(S Psi)(X) = (psi^L(X+read_L), psi^R(X+read_R)): L moves by -read_L."""
    return monomial(zs, neg(read_L)) * PROJ_L + monomial(zs, neg(read_R)) * PROJ_R


TRI = [None, (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]  # X1..X6, g1=(1,0), g2=(1/2,sqrt3/2)
TRI_GENS = [(1, 0), (sp.Rational(1, 2), sp.sqrt(3) / 2)]


def row_L6c():
    """JDW 1803.01304v1 Eq. (2) p.2: W0 = prod_{j=1}^{6} W_j,
    W_j = R_j^{-1} U_j S_j R_j, U_j = 1, R_j = U(0, pi/2, 0, pi/12+(j-1)pi/6),
    R_j^{-1} = U(0, -pi/2, 0, -pi/12-(j-1)pi/6); S_j reads L at N_j, R at
    N_{j+1}. W_1 acts first."""
    zs = sp.symbols("z1:3")
    symbol = sp.eye(2)
    for j in range(1, 7):
        R = u2(0, sp.pi / 2, 0, sp.pi / 12 + (j - 1) * sp.pi / 6)
        Rinv = u2(0, -sp.pi / 2, 0, -sp.pi / 12 - (j - 1) * sp.pi / 6)
        if j == 1:
            record("L6c: R_j^{-1} as printed is the inverse of R_j", is_zero_matrix(Rinv * R - I2))
        Sj = jdw_shift(zs, TRI[j], TRI[j % 6 + 1])
        symbol = sp.expand(Rinv * Sj * R * symbol)
    check_unitary("L6c", symbol, zs)
    support = laurent_support(symbol, zs)
    report_row("L6c", support, TRI_GENS)
    return symbol, zs, support, TRI_GENS


def row_L6d():
    """JDW Eq. (4) p.2: W~0 = R~2^{-1} U3 S~3 R~2 R~1^{-1} U2 S~2 R~1 U1 S~1,
    R~j = U(0, pi/2, 0, j pi/6), U_j = 1, S~j reads L at N_j, R at N_{j+3}."""
    zs = sp.symbols("z1:3")
    Rt = {j: u2(0, sp.pi / 2, 0, j * sp.pi / 6) for j in (1, 2)}
    Rti = {j: u2(0, -sp.pi / 2, 0, -j * sp.pi / 6) for j in (1, 2)}
    record("L6d: R~j^{-1} as printed are the inverses",
           all(is_zero_matrix(Rti[j] * Rt[j] - I2) for j in (1, 2)))
    St = {j: jdw_shift(zs, TRI[j], TRI[j + 3]) for j in (1, 2, 3)}
    symbol = sp.expand(Rti[2] * St[3] * Rt[2] * Rti[1] * St[2] * Rt[1] * St[1])
    check_unitary("L6d", symbol, zs)
    support = laurent_support(symbol, zs)
    report_row("L6d", support, TRI_GENS)
    return symbol, zs, support, TRI_GENS


ISO = [None, (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]  # g1=(1/2,1/2), g2=(-1/2,1/2)
ISO_GENS = [(sp.Rational(1, 2), sp.Rational(1, 2)), (-sp.Rational(1, 2), sp.Rational(1, 2))]


def row_L6e():
    """JDW Eq. (6) p.2: W^0 = W^3 W^2 W^1, W^j = U^j S^j,
    U^j = U(0, 0, -pi/2, (j-2) pi/4), S^j reads L at N_j, R at N_{j+3};
    isosceles neighbours X1..X6 of p.2."""
    zs = sp.symbols("z1:3")
    symbol = sp.eye(2)
    for j in (1, 2, 3):
        Uj = u2(0, 0, -sp.pi / 2, (j - 2) * sp.pi / 4)
        symbol = sp.expand(Uj * jdw_shift(zs, ISO[j], ISO[j + 3]) * symbol)
    check_unitary("L6e", symbol, zs)
    support = laurent_support(symbol, zs)
    report_row("L6e", support, ISO_GENS)
    return symbol, zs, support, ISO_GENS


HEX = [None, (1, 0), (-1, 1), (0, -1)]  # X1..X3 of p.2 in TRI generators


def row_L6f():
    """JDW Eqs. (7)-(8) p.2: W0 = prod_{j=1}^{3} W_j, W_j = U_j^{-1} S_j U_j,
    U_j = U(0, pi/2, 0, pi/6+(j-1)pi/3); S_1 reads (N1,N2), S_2 (N2,N3),
    S_3 (N3,N1). W_1 acts first."""
    zs = sp.symbols("z1:3")
    reads = {1: (1, 2), 2: (2, 3), 3: (3, 1)}
    symbol = sp.eye(2)
    for j in (1, 2, 3):
        Uj = u2(0, sp.pi / 2, 0, sp.pi / 6 + (j - 1) * sp.pi / 3)
        Uji = u2(0, -sp.pi / 2, 0, -sp.pi / 6 - (j - 1) * sp.pi / 3)
        a, b = reads[j]
        symbol = sp.expand(Uji * jdw_shift(zs, HEX[a], HEX[b]) * Uj * symbol)
    check_unitary("L6f", symbol, zs)
    support = laurent_support(symbol, zs)
    report_row("L6f", support, TRI_GENS)
    return symbol, zs, support, TRI_GENS



# ================================================================ Part 2
# Massless geometry and speeds at the declared node k = 0.
#
# Normalisation (contract Sec. 2): Cartesian positions divided by the longest
# |h| in F, one complete update per time unit. U(k) is obtained from the
# Laurent symbol by z_j = exp(sigma * i * k.g_j / L), sigma = -1 for the
# symbols built above (z <-> exp(-i k.g)) and +1 for the published standard
# symbols (z = exp(i k)). Signs of nonzero algebraic numbers are decided by
# SymPy's exact relational evaluation on radicals; zero tests are symbolic.

def positive(x):
    v = sp.radsimp(sp.simplify(x))
    if v == 0:
        return 0
    return 1 if bool(v > 0) else -1


def hull(points):
    """Facets (unit outward normal, distance) and vertex set of conv(points),
    for points spanning R^d with the origin in the interior."""
    import itertools
    d = points[0].rows
    facets = {}
    for combo in itertools.combinations(range(len(points)), d):
        base = points[combo[0]]
        if d == 1:
            normal = sp.Matrix([1])
        else:
            diff = sp.Matrix([list((points[i] - base).T) for i in combo[1:]])
            ns = diff.nullspace()
            if len(ns) != 1:
                continue
            normal = ns[0]
        offset = (normal.T * base)[0]
        if offset == 0 or positive(offset) == 0:
            continue
        if positive(offset) < 0:
            normal, offset = -normal, -offset
        if all(positive(offset - (normal.T * q)[0]) >= 0 for q in points):
            norm = sp.sqrt((normal.T * normal)[0])
            unit = (normal / norm).applyfunc(lambda e: sp.radsimp(sp.simplify(e)))
            facets[tuple(unit)] = sp.radsimp(sp.simplify(offset / norm))
    verts = []
    for idx, q in enumerate(points):
        on = [sp.Matrix(n) for n, dist in facets.items()
              if positive((sp.Matrix(n).T * q)[0] - dist) == 0]
        if on and sp.Matrix.hstack(*on).rank() == d:
            verts.append(idx)
    return facets, verts


def node_speeds(symbol, zs, gens, scale, sigma, dim):
    k = sp.symbols(f"k1:{dim + 1}", real=True)
    subs = {}
    for z, g in zip(zs, gens):
        phase = sum((k[a] * g[a] for a in range(dim)), 0) / scale
        subs[z] = sp.exp(sigma * sp.I * phase)
    U = symbol.subs(subs)
    at0 = U.subs({ka: 0 for ka in k}).applyfunc(lambda e: sp.radsimp(sp.simplify(e)))
    s_dim = symbol.rows
    A = [(sp.I * U.diff(ka)).subs({kb: 0 for kb in k}).applyfunc(
        lambda e: sp.radsimp(sp.simplify(sp.expand_complex(e)))) for ka in k]
    tilt = [sp.simplify(Ai.trace() / s_dim) for Ai in A]
    T = [Ai - t * sp.eye(s_dim) for Ai, t in zip(A, tilt)]
    c2 = sp.radsimp(sp.simplify((T[0] * T[0])[0, 0]))
    iso = all(is_zero_matrix(T[a] * T[a] - c2 * sp.eye(s_dim)) for a in range(dim)) and all(
        is_zero_matrix(T[a] * T[b] + T[b] * T[a]) for a in range(dim) for b in range(a + 1, dim))
    herm = all(is_zero_matrix(Ai - Ai.H) for Ai in A)
    return at0, A, tilt, c2, iso, herm


def nilpotent(m):
    return is_zero_matrix(m ** m.rows)


def analyse(label, symbol, zs, support, gens, sigma, results):
    dim = len(gens[0])
    cart = {h: sum((a * sp.Matrix(g) for a, g in zip(h, gens)), sp.zeros(dim, 1)) for h in support}
    L = max((sp.sqrt((v.T * v)[0]) for v in cart.values()), key=lambda x: float(x))
    L = sp.radsimp(sp.simplify(L))
    keys = sorted(support)
    pts = [(cart[h] / L).applyfunc(sp.radsimp) for h in keys]
    facets, verts = hull(pts)
    r_in = min(facets.values(), key=lambda x: float(x))
    at0, A, tilt, c2, iso, herm = node_speeds(symbol, zs, gens, L, sigma, dim)
    record(f"{label}: U(0) = I (node at k = 0, all quasienergies 0)", is_zero_matrix(at0 - sp.eye(symbol.rows)))
    record(f"{label}: linear generators i dU/dk_a(0) are Hermitian", herm)
    record(f"{label}: no tilt at the node (trace parts vanish)", all(t == 0 for t in tilt))
    record(f"{label}: isotropic untilted cone, {{T_a, T_b}} = 2 c0^2 delta_ab", iso)
    c0 = sp.radsimp(sp.sqrt(c2))
    survive = {keys[i]: not nilpotent(support[keys[i]]) for i in verts}
    all_survive = all(survive.values())
    record(f"{label}: every vertex coefficient is non-nilpotent (C_infty^strict = C_micro)",
           all_survive, f"{sum(survive.values())}/{len(survive)} vertices survive")
    c_strict = r_in if all_survive else None
    ratio = sp.radsimp(sp.simplify(c0 / r_in))
    print(f"  {label}: L = {L}; |vertices| = {len(verts)}; |facets| = {len(facets)}; "
          f"r_in = {r_in}; V_causal^max = 1; c0 = {c0}; c0/r_in = {ratio}; "
          f"c_strict^iso = {c_strict if c_strict is not None else 'OPEN'}; "
          f"S_min = c0/V_causal^max = {c0}; S_max = c0/r_in = {ratio}; "
          f"c0 in source units (per update, |h| as in source) = {sp.radsimp(c0 * L)}")
    results[label] = dict(s=symbol.rows, d=dim, r_in=r_in, c0=c0, ratio=ratio,
                          c_strict=c_strict, iso=iso, nverts=len(verts))
    return results[label]


def part2(rows):
    import verify_weyl_dirac_gate as wd  # reviewed helper, imported read-only
    results = {}
    print("== Part 2: standard rows L1, L2 (recomputed only for C_infty^strict)")
    for label, dim in (("L1", 1), ("L2", 2)):
        zs = sp.symbols(f"w1:{dim + 1}")
        symbol, _ = wd.published_symbol(dim, 1, zs)
        support = wd.fourier_support(symbol, zs)
        gens = [tuple(1 if a == b else 0 for b in range(dim)) for a in range(dim)]
        analyse(label, symbol, zs, support, gens, +1, results)
    print("== Part 2: new rows")
    for label, (symbol, zs, support, gens) in rows.items():
        analyse(label, symbol, zs, support, gens, -1, results)
    # Hypotheses (contract Sec. 5), on the rows computed here.
    s2 = [l for l, r in results.items() if r["s"] == 2]
    ha = {l: results[l]["ratio"] == 1 for l in s2}
    hb = {l: results[l]["c_strict"] is not None for l in results}
    hc = {l: (results[l]["c_strict"] is None) or positive(results[l]["c_strict"] - results[l]["c0"]) >= 0
          for l in results}
    print(f"  Ha (c0 = r_in, s=2 rows): {ha}")
    print(f"  Hb (c_strict^iso = r_in): {hb}")
    print(f"  Hc (c0 <= c_strict^iso where decided): {hc}")
    record("Hc holds in every row where c_strict^iso is decided", all(hc.values()))
    return results


def main():
    print(f"contract sha256 {hashlib.sha256(CONTRACT.read_bytes()).hexdigest()}")
    for name, expected in SOURCES.items():
        digest = hashlib.sha256((ROOT / f"sources/{name}.pdf").read_bytes()).hexdigest()
        if expected is not None:
            record(f"source {name}.pdf SHA256 matches sources/README.md", digest == expected)
        else:
            print(f"  source {name}.pdf sha256 {digest}")
    rows = {}
    for label, fn in [("L5a", row_L5a), ("L5b", row_L5b), ("L6a", row_L6a),
                      ("L6c", row_L6c), ("L6d", row_L6d), ("L6e", row_L6e), ("L6f", row_L6f)]:
        print(f"== {label}")
        rows[label] = fn()
    for label, reason in SOURCE_GAPS.items():
        print(f"== {label}: NOT ENCODED -- {reason}")
    sys.path.insert(0, str(ROOT / "scripts"))
    part2(rows)
    failed = [c for c in CHECKS if not c[1]]
    print(f"{len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed (Parts 1-2).")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail closed
        print(f"[FAIL] exception: {exc!r}")
        sys.exit(1)
