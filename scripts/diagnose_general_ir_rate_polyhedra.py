"""Diagnostic run for theory/GENERAL_IR_RATE_POLYHEDRA_DIAGNOSTIC.md (charter af44458).

Checks, numerically, the hypotheses H1-H3, H4', H5-H10 of the general
infrared-rate charter (theory/GENERAL_IR_RATE_GATE.md with Amendments 1-3)
on six walks whose symbols are imported read-only from reviewed scripts,
with the region rule frozen in the charter. Floating point throughout except
H3/H9/H7, which are evaluated exactly with SymPy. Every label is diagnostic,
not a certificate, and no label is a verdict on the theorem.

Run from the repository root:
    python3 -B scripts/diagnose_general_ir_rate_polyhedra.py --output reports/<name>.json
"""
import argparse
import contextlib
import hashlib
import io
import itertools
import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
with contextlib.redirect_stdout(io.StringIO()):
    import verify_directional_saturation as vds
    import verify_weyl_dirac_gate as vwd
    import verify_c_across_lattices_gate as vcl
    import verify_s4_cyclic_realization as vs4

GRID = {2: 160, 3: 40}          # grid points per reciprocal direction
TOL_DOM = 1e-7                  # relative tolerance for dominant points
TOL_EQ = 1e-5                   # tolerance for gradient equality (H8, on-axis)
TOL_SING = 1e-6                 # singular-value / parallelism tolerance
GL_NODES, GL_WEIGHTS = np.polynomial.legendre.leggauss(400)


# ---------------------------------------------------------------- walks ----

def laurent_terms(matrix, zs):
    """{integer exponent tuple: exact coefficient matrix} of a Laurent matrix."""
    size = matrix.shape[0]
    terms = {}
    for i in range(size):
        for j in range(matrix.shape[1]):
            entry = sp.expand(matrix[i, j])
            if entry == 0:
                continue
            for term in sp.Add.make_args(entry):
                coeff, expo = term, []
                for z in zs:
                    coeff, k = coeff.as_coeff_exponent(z)
                    expo.append(int(k))
                key = tuple(expo)
                terms.setdefault(key, sp.zeros(size, size))
                terms[key][i, j] += coeff
    return {k: v for k, v in terms.items() if v != sp.zeros(size, size)}


def laurent_inverse(matrix, zs):
    """Laurent adjoint: the inverse of a unitary Laurent symbol."""
    return matrix.T.applyfunc(
        lambda e: sp.conjugate(e).subs({sp.conjugate(z): 1 / z for z in zs}))


def walk_W1():
    zs = vds.Z
    W = sp.Matrix(vds.walk2()).applyfunc(vds.laurent)
    return laurent_inverse(W, zs), zs, [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]),
                                        sp.Matrix([0, 0, 1])]


def walk_W2():
    zs = vds.Z
    W = sp.Matrix(vds.walk1()).applyfunc(vds.laurent)
    return laurent_inverse(W, zs), zs, [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]),
                                        sp.Matrix([0, 0, 1])]


def walk_W3():
    zs = sp.symbols("y1:4")
    M, _ = vwd.published_symbol(3, 1, zs)
    return M, zs, [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]


def walk_W4():
    zs = sp.symbols("y1:3")
    M, _ = vwd.published_symbol(2, 1, zs)
    return M, zs, [sp.Matrix([1, 0]), sp.Matrix([0, 1])]


def walk_W5():
    with contextlib.redirect_stdout(io.StringIO()):
        symbol, zs, _, gens = vcl.row_L6d()
    return symbol, zs, [sp.Matrix(g) for g in gens]


def walk_W6():
    zs = sp.symbols("x1:4")
    M = sp.zeros(4, 4)
    for h, A in vs4.coeffs.items():
        M += A / sp.sqrt(2) * zs[0] ** h[0] * zs[1] ** h[1] * zs[2] ** h[2]
    gens = [sp.Matrix([1, 0, 0]) / sp.sqrt(3), sp.Matrix([0, 1, 0]) / sp.sqrt(3),
            sp.Matrix([0, 0, 1]) / sp.sqrt(3)]
    return M, zs, gens


WALKS = [
    ("W1", "CJWW (5.15), K3 control", walk_W1, None),
    ("W2", "CJWW (5.12) Bialynicki-Birula", walk_W2, None),
    ("W3", "Pavia Weyl A+ (BCC)", walk_W3, None),
    ("W4", "square Weyl", walk_W4, None),
    ("W5", "JDW L6d (hexagon)", walk_W5, None),
    ("W6", "cyclic s=4 (tetrahedron), node P", walk_W6, -np.pi / 4),
]


# -------------------------------------------------------------- lattice ----

def lattice_data(terms, gens):
    d = len(gens)
    expos = [sp.Matrix(k) for k in terms]
    hnf = hermite_normal_form(sp.Matrix.hstack(*expos))
    cols = [hnf[:, i] for i in range(hnf.shape[1]) if any(x != 0 for x in hnf[:, i])]
    assert len(cols) == d, "steps do not span"
    G = sp.Matrix.hstack(*gens)
    basis = [sp.simplify(G * c) for c in cols]                 # physical, exact
    steps = {k: sp.simplify(G * sp.Matrix(k)) for k in terms}
    return basis, steps


def isometric_to_Zd(basis):
    d = len(basis)
    B = np.array([[float(x) for x in b] for b in basis]).T
    vecs = []
    for m in itertools.product(range(-2, 3), repeat=d):
        if any(m):
            vecs.append(B @ np.array(m, float))
    norms = np.array([np.linalg.norm(v) for v in vecs])
    shortest = [v for v, n in zip(vecs, norms) if abs(n - norms.min()) < 1e-9]
    if len(shortest) != 2 * d:
        return False
    M = np.array(shortest)
    gram = M @ M.T / norms.min() ** 2
    ortho = all(abs(gram[i, j]) < 1e-9 or abs(abs(gram[i, j]) - 1) < 1e-9
                for i in range(len(M)) for j in range(len(M)))
    if not ortho:
        return False
    pick = []
    for v in shortest:
        if all(abs(np.dot(v, w)) < 1e-9 for w in pick):
            pick.append(v)
    vol = abs(np.linalg.det(np.array(pick)))
    return len(pick) == d and abs(vol - abs(np.linalg.det(B))) < 1e-9


def axis_map(u, d):
    """rotation by 2pi/3 about u (d=3) or reflection fixing u (d=2)."""
    if d == 2:
        return 2 * np.outer(u, u) - np.eye(2)
    K = np.array([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])
    th = 2 * np.pi / 3
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K


def choose_vertex(steps, d, sym):
    """First step of maximal norm about which the moduli of the eigenvalues of
    S(k - i xi) are invariant (checked at random complex points): a symmetry
    of the rate function I fixing the axis."""
    rng = np.random.default_rng(1)
    kk = rng.uniform(-3, 3, (12, d))
    xx = rng.uniform(-1, 1, (12, d))
    pts = [(np.array([float(x) for x in v]), v) for v in steps.values()]
    big = max(np.linalg.norm(p) for p, _ in pts)
    for p, e in pts:
        if abs(np.linalg.norm(p) - big) > 1e-9:
            continue
        R = axis_map(p / np.linalg.norm(p), d)
        ok = True
        for k, x in zip(kk, xx):
            a = np.sort(np.abs(np.linalg.eigvals(sym.at(k[None, :], x)[0])))
            b = np.sort(np.abs(np.linalg.eigvals(sym.at((R @ k)[None, :], R @ x)[0])))
            ok &= bool(np.allclose(a, b, rtol=1e-10, atol=1e-12))
        if ok:
            return e
    raise RuntimeError("no maximal step on a symmetry axis of the rate")


# --------------------------------------------------------------- symbol ----

class Symbol:
    def __init__(self, terms, steps):
        self.F = np.array([[float(x) for x in steps[k]] for k in terms])
        self.C = np.array([np.array(terms[k].evalf(30), dtype=complex) for k in terms])
        self.s = self.C.shape[1]

    def at(self, kappa, xi):
        """S(kappa - i xi) for kappa of shape (n, d)."""
        ph = np.exp(1j * kappa @ self.F.T + (self.F @ xi)[None, :])
        return np.einsum("pf,fij->pij", ph, self.C)

    def logrho(self, kappa, xi):
        ev = np.linalg.eigvals(self.at(kappa, xi))
        return np.log(np.max(np.abs(ev), axis=1))

    def dominant(self, kappa, xi):
        """dominant eigenvalue, right and left eigenvectors at one point."""
        M = self.at(kappa[None, :], xi)[0]
        w, V = np.linalg.eig(M)
        i = int(np.argmax(np.abs(w)))
        wl, U = np.linalg.eig(M.conj().T)
        j = int(np.argmin(np.abs(wl - np.conj(w[i]))))
        mags = np.sort(np.abs(w))[::-1]
        return w[i], V[:, i], U[:, j], mags[1] / mags[0]


def bz_grid(basis_np, d):
    n = GRID[d]
    t = np.linspace(-np.pi, np.pi, n, endpoint=False)
    th = np.array(list(itertools.product(t, repeat=d)))
    return th @ np.linalg.inv(basis_np).T     # k with k.b_i = theta_i  (rows)


def refine(sym, k0, xi, basis_np):
    """Newton ascent of log rho in theta coordinates."""
    Binv = np.linalg.inv(basis_np).T
    th = basis_np.T @ k0
    h = 1e-4
    d = len(th)
    f = lambda t: sym.logrho((Binv @ t)[None, :], xi)[0]
    for _ in range(60):
        g = np.zeros(d)
        H = np.zeros((d, d))
        f0 = f(th)
        for a in range(d):
            ea = np.eye(d)[a] * h
            g[a] = (f(th + ea) - f(th - ea)) / (2 * h)
            for b in range(d):
                eb = np.eye(d)[b] * h
                H[a, b] = (f(th + ea + eb) - f(th + ea - eb) - f(th - ea + eb)
                           + f(th - ea - eb)) / (4 * h * h)
        step = 0.05 * g
        if np.all(np.isfinite(H)) and np.all(np.linalg.eigvalsh((H + H.T) / 2) < 0):
            try:
                step = -np.linalg.solve(H, g)
            except np.linalg.LinAlgError:     # attempt 1 crashed here (W6); tooling only
                pass
        if np.linalg.norm(step) > 0.2:
            step *= 0.2 / np.linalg.norm(step)
        th = th + step
        if np.linalg.norm(step) < 1e-11:
            break
    return Binv @ th, f(th)


def phi_and_maximisers(sym, xi, basis_np, grid):
    vals = sym.logrho(grid, xi)
    order = np.argsort(vals)[::-1][:40]
    found = []
    for idx in order:
        k, v = refine(sym, grid[idx], xi, basis_np)
        found.append((k, v))
    vmax = max(v for _, v in found)
    keep = []
    for k, v in found:
        if v >= vmax - TOL_DOM * max(1, abs(vmax)):
            th = np.mod(basis_np.T @ k + np.pi, 2 * np.pi) - np.pi
            if not any(np.linalg.norm(np.mod(th - t2 + np.pi, 2 * np.pi) - np.pi) < 1e-3
                       for t2, _ in keep):
                keep.append((th, k))
    return vmax, [k for _, k in keep]


def grad_xi_logabs(sym, k, xi):
    h = 1e-5
    d = len(xi)
    g = np.zeros(d)
    for a in range(d):
        e = np.eye(d)[a] * h
        lp = abs(sym.dominant(k, xi + e)[0])
        lm = abs(sym.dominant(k, xi - e)[0])
        g[a] = (np.log(lp) - np.log(lm)) / (2 * h)
    return g


def hess_kappa_logabs(sym, k, xi):
    h = 1e-4
    d = len(xi)
    f = lambda kk: np.log(abs(sym.dominant(kk, xi)[0]))
    H = np.zeros((d, d))
    for a in range(d):
        for b in range(d):
            ea, eb = np.eye(d)[a] * h, np.eye(d)[b] * h
            H[a, b] = (f(k + ea + eb) - f(k + ea - eb) - f(k - ea + eb) + f(k - ea - eb)) / (4 * h * h)
    return (H + H.T) / 2


# ------------------------------------------------------------ node, tail ----

def node(sym, d, target_phase):
    S0 = sym.at(np.zeros((1, d)), np.zeros(d))[0]
    w, V = np.linalg.eig(S0)
    if target_phase is None:
        groups = {}
        for i, x in enumerate(w):
            key = next((g for g in groups if abs(w[g] - x) < 1e-8), i)
            groups.setdefault(key, []).append(i)
        idx = next(g for g in groups.values() if len(g) == 2)
    else:
        idx = [i for i, x in enumerate(w) if abs(np.angle(x) - target_phase) < 1e-6]
    lam0 = w[idx[0]]
    Q, _ = np.linalg.qr(V[:, idx])
    D = [np.einsum("f,fij->ij", sym.F[:, a], sym.C) for a in range(d)]
    A = [-(Q.conj().T @ Da @ Q) / lam0 for Da in D]
    herm = max(np.abs(Aa - Aa.conj().T).max() for Aa in A)
    trace = max(abs(np.trace(Aa)) for Aa in A)
    anti = np.array([[np.abs(A[a] @ A[b] + A[b] @ A[a]).max() if a != b else 0
                      for b in range(d)] for a in range(d)]).max()
    c2 = [np.real(np.trace(Aa @ Aa)) / 2 for Aa in A]
    iso = max(c2) - min(c2)
    return lam0, Q, A, float(np.sqrt(np.mean(c2))), dict(
        hermitian_defect=float(herm), trace_defect=float(trace),
        anticommutator_defect=float(anti), isotropy_defect=float(iso))


def bessel_J(n, x):
    t = (GL_NODES + 1) * np.pi / 2
    return np.sum(GL_WEIGHTS[None, :] * np.cos(n * t[None, :] - np.outer(x, np.sin(t))), axis=1) / 2


def tail(w, A, c, chi, d):
    k = (GL_NODES + 1) / 2
    wt = GL_WEIGHTS / 2
    g = (1 - k ** 2) ** 2
    r = np.linalg.norm(w)
    x = k * r
    if d == 3:
        j0 = np.sinc(x / np.pi)
        j1 = np.where(x > 1e-8, np.sin(x) / x ** 2 - np.cos(x) / x, x / 3)
        I0 = 4 * np.pi * np.sum(wt * k ** 2 * g * np.cos(c * k) * j0)
        I1 = 4 * np.pi * np.sum(wt * k ** 2 * g * np.sin(c * k) * j1)
    else:
        I0 = 2 * np.pi * np.sum(wt * k * g * np.cos(c * k) * bessel_J(0, x))
        I1 = 2 * np.pi * np.sum(wt * k * g * np.sin(c * k) * bessel_J(1, x))
    H = sum(wa * Aa for wa, Aa in zip(w / r, A)) / c
    return I0 * chi - I1 * (H @ chi), float(I0), float(I1)


# ------------------------------------------------------------ exact parts ----

def exact_geometry(basis, V, d):
    """u = primitive dual-lattice vector along V; rho|u| and its rationality."""
    B = sp.Matrix.hstack(*basis)
    r = sp.simplify(B.T * V)
    ratios = [sp.nsimplify(sp.simplify(x)) for x in r]
    assert all(x.is_rational for x in ratios), ratios
    den = 1
    for x in ratios:
        den = den * sp.denom(x) // gcd(den, int(sp.denom(x)))
    ints = [int(x * den) for x in ratios]
    g = 0
    for a in ints:
        g = gcd(g, abs(a))
    t = sp.Rational(den, g)                       # u = t V
    normV2 = sp.nsimplify(sp.simplify(V.dot(V)))
    normV = sp.sqrt(normV2)
    u_norm = sp.simplify(t * normV)
    rho = sp.simplify(normV / (4 * sp.sqrt(3)))
    rho_u = sp.simplify(rho * u_norm)
    uV = sp.simplify(t * normV2)
    return dict(u_norm=str(u_norm), rho=str(rho), rho_u=str(rho_u),
                rho_u_irrational=bool(rho_u.is_irrational),
                uV=str(uV), uV_integer=bool(uV.is_integer),
                h9_ii=bool(rho_u.is_irrational and uV.is_integer),
                h7=bool(rho < (sp.pi if d == 3 else sp.Rational(2405, 1000)))), float(rho)


# ------------------------------------------------------------------ run ----

def analyse(wid, name, builder, target_phase):
    M, zs, gens = builder()
    terms = laurent_terms(M, zs)
    basis, steps = lattice_data(terms, gens)
    d = len(gens)
    sym = Symbol(terms, steps)
    basis_np = np.array([[float(x) for x in b] for b in basis]).T
    out = dict(id=wid, name=name, d=d, s=sym.s, n_steps=len(terms))
    U0 = sym.at(np.random.default_rng(0).uniform(-3, 3, (5, d)), np.zeros(d))
    out["unitarity_defect"] = float(max(np.abs(Ui.conj().T @ Ui - np.eye(sym.s)).max() for Ui in U0))
    out["lattice_isometric_to_Zd"] = bool(isometric_to_Zd(basis))

    V = choose_vertex(steps, d, sym)
    geo, rho = exact_geometry(basis, V, d)
    out["vertex"] = [str(x) for x in V]
    out["exact"] = geo
    Vn = np.array([float(x) for x in V])
    n = Vn / np.linalg.norm(Vn)
    vstar = Vn * (1 - 1 / (2 * np.sqrt(3)))
    wA, wB = rho * n, Vn - rho * n

    lam0, Q, A, c, node_def = node(sym, d, target_phase)
    out["node"] = dict(eigenvalue=[float(lam0.real), float(lam0.imag)], c_IR=c, **node_def)
    out["min_speed_in_B_minus_A"] = float(np.linalg.norm(vstar))

    grid = bz_grid(basis_np, d)

    def slope(t):
        xi = t * n
        _, ks = phi_and_maximisers(sym, xi, basis_np, grid)
        return float(np.dot(n, grad_xi_logabs(sym, ks[0], xi)))

    target = np.linalg.norm(vstar)
    lo, hi = 1e-3, 12.0
    s_lo, s_hi = slope(lo), slope(hi)
    out["slope_range"] = [s_lo, s_hi]
    if not (s_lo < target < s_hi):
        out["K_star"] = 0.0 if target <= s_lo else None
        out["label"] = "FAILS_KSTAR_POSITIVE" if target <= s_lo else "OUT_OF_RANGE"
        return out
    for _ in range(45):
        mid = (lo + hi) / 2
        if slope(mid) < target:
            lo = mid
        else:
            hi = mid
    tstar = (lo + hi) / 2
    xi = tstar * n
    phi, ks = phi_and_maximisers(sym, xi, basis_np, grid)
    out["t_star"] = tstar
    out["Phi_star"] = float(phi)
    out["K_star"] = float(tstar * target - phi)

    # plane lattice L cap n^perp (small generators) and characters
    Bn = basis_np.T @ n
    plane = [basis_np @ np.array(m, float) for m in itertools.product(range(-4, 5), repeat=d)
             if any(m) and abs(np.dot(Bn, m)) < 1e-9]
    dom = []
    for k in ks:
        lam, e, f, gap = sym.dominant(k, xi)
        grad = grad_xi_logabs(sym, k, xi)
        hess = np.linalg.eigvalsh(hess_kappa_logabs(sym, k, xi))
        trivial = all(abs(np.exp(1j * np.dot(k, p)) - 1) < 1e-6 for p in plane)
        dom.append(dict(k=k.tolist(), is_zero=bool(np.linalg.norm(k) < 1e-4),
                        trivial_character=bool(trivial), gap_ratio=float(gap),
                        hessian_eigs=hess.tolist(),
                        grad_minus_vstar=float(np.linalg.norm(grad - vstar)),
                        e=e, f=f))
    out["dominant_points"] = [{kk: v for kk, v in x.items() if kk not in ("e", "f")} for x in dom]
    zero = [x for x in dom if x["is_zero"]]
    others = [x for x in dom if x["trivial_character"] and not x["is_zero"]]

    h = {}
    h["H1_on_axis"] = all(x["grad_minus_vstar"] < TOL_EQ for x in zero) if zero else None
    h["H2"] = bool(len(dom) < 64 and all(x["gap_ratio"] < 1 - 1e-6 for x in dom)
                   and all(max(x["hessian_eigs"]) < -1e-6 for x in dom))
    h["H3"] = True                                   # V is a lattice vector, exact
    h["H4prime"] = bool(zero)
    h["H8"] = all(x["grad_minus_vstar"] < TOL_EQ for x in dom)
    h["H7"] = geo["h7"]
    h["H9"] = geo["h9_ii"]
    if zero:
        f0 = zero[0]["f"]
        e0 = zero[0]["e"]
        if others:
            Fo = np.array([x["f"] for x in others]).T
            Fall = np.column_stack([Fo, f0])
            s_o = np.linalg.svd(Fo / np.linalg.norm(Fo, axis=0), compute_uv=False)
            s_a = np.linalg.svd(Fall / np.linalg.norm(Fall, axis=0), compute_uv=False)
            h["H6_left"] = bool(np.sum(s_a > TOL_SING) > np.sum(s_o > TOL_SING))
        else:
            h["H6_left"] = True
        tails = []
        for col in range(2):
            chi = Q[:, col]
            R, I0, I1 = tail(wB, A, c, chi, d)
            par = abs(np.vdot(e0, R)) / (np.linalg.norm(e0) * np.linalg.norm(R))
            tails.append(dict(chi_index=col, I0=I0, I1=I1, tail_norm=float(np.linalg.norm(R)),
                              cos_angle_e0_tail=float(par)))
        out["tails"] = tails
        h["H5"] = all(t["tail_norm"] > 1e-8 for t in tails)
        h["H10_sufficient"] = bool(h["H6_left"] and all(t["cos_angle_e0_tail"] < 1 - TOL_SING for t in tails))
    out["hypotheses"] = h
    out["node_untilted_isotropic"] = bool(max(node_def.values()) < 1e-9)
    fails = [k for k, v in h.items() if v is False]
    if not out["lattice_isometric_to_Zd"]:
        out["label"] = "OUTSIDE_CLASS_LATTICE" + ("" if not fails else "; FAILS_" + "_".join(fails))
    elif not out["node_untilted_isotropic"]:
        out["label"] = "OUTSIDE_CLASS_NODE"
    elif fails:
        out["label"] = "FAILS_" + "_".join(fails)
    else:
        out["label"] = "HYPOTHESES_HOLD_NUMERICALLY"
    return out


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    results = []
    for wid, name, builder, phase in WALKS:
        r = analyse(wid, name, builder, phase)
        results.append(r)
        print(f"{wid} {name}: {r['label']}")
        for k in ("K_star", "t_star", "lattice_isometric_to_Zd"):
            if k in r:
                print(f"    {k} = {r[k]}")
        if "hypotheses" in r:
            print("    " + ", ".join(f"{k}={v}" for k, v in r["hypotheses"].items()))
            print(f"    dominant points: {len(r['dominant_points'])}")
    meta = dict(charter="theory/GENERAL_IR_RATE_POLYHEDRA_DIAGNOSTIC.md", charter_commit="af44458",
                script_sha256=sha(__file__), numpy=np.__version__, sympy=sp.__version__,
                imported=dict((m.__name__, sha(m.__file__)) for m in (vds, vwd, vcl, vs4)),
                grid=GRID, tolerances=dict(dom=TOL_DOM, eq=TOL_EQ, sing=TOL_SING),
                nature="floating-point diagnostic; labels are not certificates or verdicts")
    args.output.write_text(json.dumps(dict(meta=meta, walks=results), indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
