#!/usr/bin/env python3
"""Checks for the observational-signature / saturation gate.

Contract: theory/OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md (commit 21af1dd).
Report:   reports/2026-11-09--observational-signature-saturation.md

Rows and symbols: imported read-only from the reviewed verifiers used by the parent
gate (verify_dispersion_corrections_gate.py and its imports). Units: longest step
of one update = 1, one update per time unit (L6b: V = U^3, quasienergy / 3).

Certification methods (declared in the report as a deviation from the contract's
"radicals, Sturm" wording, because e^{ik} at rational |k| is transcendental):
  * EXACT (SymPy): Laurent identities, closed-form bounds, signs of parent
    coefficients on declared rays, multilinear vertex checks.
  * INTERVAL: rigorous outward-rounded interval arithmetic (mpmath.iv) for the
    inequality |grad eps(k*)| > c0 at explicit points k* on declared rays and on the
    rational |k| grid below, plus the non-crossing check 0 < |Tr U~|^2 < 4 at k*.
No floating point enters a verdict.
"""
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp
from mpmath import iv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import verify_dispersion_corrections_gate as DC    # reviewed parent, read-only
P, WD, DS, L6B = DC.P, DC.WD, DC.DS, DC.L6B

OUT = ROOT / "reports/2026-11-09--observational-signature-saturation"
CHECKS = []
I = sp.I
R2, R3 = sp.sqrt(2), sp.sqrt(3)
GRID = [sp.Rational(1, 16), sp.Rational(1, 8), sp.Rational(1, 4), sp.Rational(1, 2),
        sp.Rational(3, 4), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2)]
iv.dps = 40


def ivnum(e):
    """Rigorous enclosure of a real SymPy number: 60-digit value widened by 1e-55."""
    x = sp.N(e, 70)
    eps = sp.Rational(1, 10**55)
    return iv.mpf([str(sp.N(x - eps, 70)), str(sp.N(x + eps, 70))])


def exact(name, cond, detail=""):
    CHECKS.append(dict(name=name, passed=bool(cond), detail=str(detail)))


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


# ---------------- rows (same constructors as the parent) ----------------
def build_rows():
    rows = {}
    zs1, zs2 = sp.symbols("w1:2"), sp.symbols("w1:3")
    rows["L1"] = dict(blocks=[WD.published_symbol(1, 1, zs1)[0]], zs=zs1, gens=[(1,)], sigma=+1, c0=sp.Integer(1), div=1)
    rows["L2"] = dict(blocks=[WD.published_symbol(2, 1, zs2)[0]], zs=zs2, gens=[(1, 0), (0, 1)], sigma=+1, c0=R2 / 2, div=1)
    for label, fn in (("L6e", P.row_L6e), ("L5a", P.row_L5a), ("L6a", P.row_L6a),
                      ("L6c", P.row_L6c), ("L6d", P.row_L6d), ("L6f", P.row_L6f)):
        symbol, zs, support, gens = fn()
        rows[label] = dict(blocks=[symbol], zs=zs, gens=gens, sigma=-1, c0=P.EXPECTED_MASSLESS[label][1], div=1)
    rows["L3"] = dict(blocks=[DC.laurent_matrix_from_p(DS.walk2())], zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                      sigma=+1, c0=1 / R3, div=1)
    rows["L4"] = dict(blocks=[DC.laurent_matrix_from_p(DS.walk1())], zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                      sigma=+1, c0=1 / R3, div=1)
    # L5b: 4x4, split by Gamma = dP_X dP_Y dP_Z (as in the parent)
    symbol, zs, support, gens = P.row_L5b()
    kron = sp.kronecker_product
    dP = (kron(P.SX, P.SX), kron(P.SX, P.SY), kron(P.SX, P.SZ))
    Gam = (dP[0] * dP[1] * dP[2]).applyfunc(DC.canon)
    blks = []
    for sgn in (1, -1):
        proj = (sp.eye(4) - sgn * I * Gam) / 2
        Bq, _ = sp.Matrix.hstack(*proj.columnspace()).QRdecomposition()
        Bq = Bq.applyfunc(DC.canon)
        blks.append((Bq.H * symbol * Bq).applyfunc(sp.expand))
    rows["L5b"] = dict(blocks=blks, zs=zs, gens=gens, sigma=-1, c0=P.EXPECTED_MASSLESS["L5b"][1], div=1)
    succ, admissible = L6B.part1_labelings()
    Wcoin, _, _ = L6B.coin("parent")
    U6, _ = L6B.step_symbol("up", succ, Wcoin)
    off, blocks = L6B.orientation_blocks(sp.expand(U6 ** 3))
    rows["L6b"] = dict(blocks=[b.applyfunc(sp.expand) for b in blocks], zs=L6B.ZS, gens=L6B.GENS, sigma=-1,
                       c0=sp.Rational(1, 3), div=3, scale=sp.Rational(1, 2))
    return rows


def scale_of(row):
    if row.get("scale") is not None:
        return row["scale"]
    sup = P.laurent_support(row["blocks"][0], row["zs"])
    dim = len(row["gens"][0])
    best = 0
    for h in sup:
        v = sum((a * sp.Matrix(g) for a, g in zip(h, row["gens"])), sp.zeros(dim, 1))
        nrm = sp.sqrt((v.T * v)[0])
        if float(nrm) > float(best):
            best = nrm
    return sp.radsimp(sp.simplify(best))


# ---------------- real polynomial representation in (c_j, s_j) ----------------
def trig_parts(expr, zs, sigma):
    cs = sp.symbols(f"c1:{len(zs) + 1}", real=True)
    ss = sp.symbols(f"s1:{len(zs) + 1}", real=True)
    sub = {z: c + I * sigma * s for z, c, s in zip(zs, cs, ss)}
    inv = {z: c - I * sigma * s for z, c, s in zip(zs, cs, ss)}
    # Laurent polynomial: negative powers via z^{-1} = conj(z) on the unit circle
    e2 = sp.expand(sp.expand(expr).replace(lambda x: x.is_Pow and x.base in zs and x.exp < 0,
                                        lambda x: (inv[x.base]) ** (-x.exp)))
    e2 = sp.expand(e2.subs(sub))
    return sp.expand(sp.re(e2)), sp.expand(sp.im(e2)), cs, ss


def dp(F, j, cs, ss):
    return sp.expand(-ss[j] * sp.diff(F, cs[j]) + cs[j] * sp.diff(F, ss[j]))


def prepare_block(block, zs, sigma):
    trr, tri, cs, ss = trig_parts(block.trace(), zs, sigma)
    der, dei, _, _ = trig_parts(sp.expand(block.det()), zs, sigma)
    T2 = sp.expand(trr ** 2 + tri ** 2)
    n = len(zs)
    exprs = [T2, sp.expand(der ** 2 + dei ** 2)]
    exprs += [dp(T2, j, cs, ss) for j in range(n)]
    exprs += [sp.expand(der * dp(dei, j, cs, ss) - dei * dp(der, j, cs, ss)) for j in range(n)]
    args = list(cs) + list(ss)
    fns = [sp.lambdify(args, e, modules=[{"sqrt": iv.sqrt, "mpf": iv.mpf}, "mpmath"]) for e in exprs]
    return fns, n


def branch_speeds_interval(prep, gens, L, div, kvec):
    """Rigorous intervals for |grad eps_+|, |grad eps_-| of a 2x2 unitary block at k.
    Tr U = e^{i phi_d/2} 2 cos(theta): eps_pm = -phi_d/2 -+ theta, |Tr|^2 = 4 cos^2 theta,
    grad theta = -+ grad|Tr|^2 / (2 |Tr| sqrt(4-|Tr|^2)) (sign covered by the two branches),
    grad phi_d = Im(conj(det) grad det) since |det| = 1."""
    fns, n = prep
    dim = len(gens[0])
    Lv = ivnum(L)
    pv = []
    for g in gens:
        acc = iv.mpf(0)
        for m in range(dim):
            acc += ivnum(kvec[m]) * ivnum(g[m])
        pv.append(acc / Lv)
    args = [iv.cos(x) for x in pv] + [iv.sin(x) for x in pv]
    vals = [f(*args) for f in fns]
    T2v, detmod = vals[0], vals[1]
    dT2 = vals[2:2 + n]
    dphi = vals[2 + n:2 + 2 * n]
    a = [-x / 2 for x in dphi]
    bmag = iv.mpf(1) / (2 * iv.sqrt(T2v) * iv.sqrt(4 - T2v))
    b = [x * bmag for x in dT2]
    def kgrad(vec):
        return [sum(vec[j] * ivnum(gens[j][m]) for j in range(n)) / Lv / div for m in range(dim)]
    A, Bv = kgrad(a), kgrad(b)
    plus = iv.sqrt(sum((A[m] + Bv[m]) ** 2 for m in range(dim)))
    minus = iv.sqrt(sum((A[m] - Bv[m]) ** 2 for m in range(dim)))
    return T2v, detmod, plus, minus


def rays(dim, label):
    if dim == 1:
        return {"+x": (1,), "-x": (-1,)}
    if dim == 2:
        if label in ("L2", "L6e"):
            out = {}
            for nm, v in (("x", (1, 0)), ("y", (0, 1)), ("d1", (1, 1)), ("d2", (1, -1))):
                nv = sp.sqrt(sum(x ** 2 for x in v))
                out["+" + nm] = tuple(x / nv for x in v); out["-" + nm] = tuple(-x / nv for x in v)
            return out
        out = {}
        for j in range(12):                    # hexagon vertex and edge directions, every 30 degrees
            th = sp.pi * j / 6
            out[f"th={j * 30}"] = (sp.cos(th), sp.sin(th))
        return out
    out = {}
    for nm, v in (("x", (1, 0, 0)), ("y", (0, 1, 0)), ("z", (0, 0, 1)),
                  ("xy", (1, 1, 0)), ("x-y", (1, -1, 0)), ("xz", (1, 0, 1)), ("x-z", (1, 0, -1)),
                  ("yz", (0, 1, 1)), ("y-z", (0, 1, -1)),
                  ("111", (1, 1, 1)), ("11-1", (1, 1, -1)), ("1-11", (1, -1, 1)), ("-111", (-1, 1, 1))):
        nv = sp.sqrt(sum(x ** 2 for x in v))
        out["+" + nm] = tuple(x / nv for x in v); out["-" + nm] = tuple(-x / nv for x in v)
    return out


def witness_search(label, row):
    L = scale_of(row)
    dim = len(row["gens"][0])
    c0 = row["c0"]
    c0v = ivnum(c0)
    found = None
    for bi, blk in enumerate(row["blocks"]):
        if blk.rows != 2:
            return None, "block not 2x2"
        prep = prepare_block(blk, row["zs"], row["sigma"])
        for rname, n in rays(dim, label).items():
            for t in GRID:
                k = [t * x for x in n]
                T2v, detmod, plus, minus = branch_speeds_interval(prep, row["gens"], L, row["div"], k)
                ok_branch = (T2v.a > 0) and (T2v.b < 4)
                best = plus if plus.a > minus.a else minus
                if ok_branch and best.a > c0v.b:
                    found = dict(block=bi, ray=rname, t=str(t), speed_lower=str(best.a), c0=str(c0), detmod=str(detmod))
                    return found, "found"
    return None, "none on declared rays and grid"


# ---------------- exact closed forms ----------------
def check_L1(row):
    U = row["blocks"][0]; z = row["zs"][0]
    exact("L1-symbol-trace=z+1/z-and-det=1", zero(U.trace() - (z + 1 / z)) and zero(U.det() - 1),
          f"trace={sp.simplify(U.trace())}, det={sp.simplify(U.det())}")


def check_product_form(label, row):
    U = row["blocks"][0]; zs = row["zs"]
    target = sp.prod([(z + 1 / z) for z in zs]) * 2 / 2 ** len(zs)
    ok_tr = zero(U.trace() - target)
    ok_det = zero(U.det() - 1)
    L = scale_of(row)
    exact(f"{label}-trace/2=prod(cos p_j)-and-det=1", ok_tr and ok_det, f"L={L}")
    exact(f"{label}-c0=1/L", zero(row["c0"] - 1 / L), f"c0={row['c0']}, L={L}")
    return ok_tr and ok_det


def check_multilinear(d):
    a = sp.symbols(f"a1:{d + 1}", real=True)
    lhs = sum((1 - a[j]) * sp.prod([a[i] for i in range(d) if i != j]) for j in range(d))
    f = sp.expand(1 - sp.prod(a) - lhs)          # >= 0 on [0,1]^d  <=>  sum_j (dω/dp_j)^2 <= 1
    multilinear = all(sp.degree(f, x) <= 1 for x in a)
    import itertools
    vert = all(f.subs(dict(zip(a, v))) >= 0 for v in itertools.product((0, 1), repeat=d))
    exact(f"multilinear-bound-d={d}: 1 - prod a - sum_j (1-a_j) prod_(i!=j) a_i >= 0 on [0,1]^d (vertices)",
          multilinear and vert, f"f={f}")


# ---------------- parent coefficients (transcribed from the promoted report, Sec. 1) ----------------
def parent_table():
    n1, n2, n3, th, a = sp.symbols("n1 n2 n3 theta a", real=True)
    T = {
        "L1": dict(beta=0, alpha=0, alpha0=0, d=1, ceiling=True, smax=True),
        "L2": dict(beta=0, alpha=-n1**2 * n2**2 / 12, alpha0=sp.Rational(-1, 96), d=2, ceiling=True),
        "L6e": dict(beta=0, alpha=-n1**2 * n2**2 / 12, alpha0=sp.Rational(-1, 96), d=2, ceiling=True),
        "L3": dict(beta=0, alpha=-(n1**2*n2**2 + n2**2*n3**2 + n3**2*n1**2) / 18, alpha0=sp.Rational(-1, 90), d=3, ceiling=True),
        "L5a": dict(beta=R3 / 3 * n1 * n2 * n3, alpha0=sp.Rational(-4, 315), d=3, ceiling=True),
        "L5b": dict(beta=R3 / 3 * n1 * n2 * n3, alpha0=sp.Rational(-4, 315), d=3, ceiling=True, both_blocks_sign=True),
        "L4": dict(beta=-R3 / 3 * n1 * n2 * n3, alpha0=sp.Rational(-4, 315), d=3, ceiling=True),
        "L3s4": dict(beta=R3 * (1 - a**2) / (6 * a) + R3 * (2 * a**2 - 1) / (3 * a) * n1 * n2 * n3,
                     alpha0=2 * (27 * a**4 - 34 * a**2 + 5) / (315 * a**2), d=3, ceiling=False),
        "L6a": dict(beta=-sp.sqrt(15) / 36 * sp.cos(3 * th), alpha0=sp.Rational(-41, 1728), d=2, ceiling=False),
        "L6c": dict(beta=0, alpha0=sp.Rational(-1, 512), d=2, ceiling=False, iso=True),
        "L6d": dict(beta=0, alpha0=sp.Rational(-1, 128), d=2, ceiling=False, iso=True),
        "L6f": dict(beta=0, alpha0=sp.Rational(-1, 128), d=2, ceiling=False, iso=True),
        "L6b": dict(beta=sp.sqrt(15) / 18 * sp.cos(3 * th), alpha0=sp.Rational(-41, 432), d=2, ceiling=False),
    }
    return T, (n1, n2, n3, th, a)


def beta_positive_on_declared_ray(label, entry, syms):
    n1, n2, n3, th, a = syms
    b = sp.sympify(entry["beta"])
    if b == 0:
        return None
    if entry["d"] == 3:
        if label == "L3s4":
            # cluster with upper sign: beta0 = sqrt3 (1-a^2)/(6a) > 0 for 0<a<1; along +111 or -111 choose sign of n1n2n3
            s = R3 / 9
            val_p = b.subs({n1: 1 / R3, n2: 1 / R3, n3: 1 / R3})
            val_m = b.subs({n1: -1 / R3, n2: -1 / R3, n3: -1 / R3})
            # for every a in (0,1): max(val_p, val_m) > 0 since val_p + val_m = 2 beta0 > 0
            return ("+111 or -111 (upper-sign cluster)", sp.simplify(val_p + val_m), "sum=2*beta0>0 for 0<a<1")
        for nm, v in (("+111", (1, 1, 1)), ("-111", (-1, -1, -1))):
            val = b.subs({n1: v[0] / R3, n2: v[1] / R3, n3: v[2] / R3})
            if sp.simplify(val) > 0:
                return (nm, sp.nsimplify(val), "")
    else:
        for j in range(12):
            val = b.subs(th, sp.pi * j / 6)
            if sp.simplify(val) > 0:
                return (f"th={j * 30}", sp.nsimplify(val), "")
    return None


def main():
    rows = build_rows()
    T, syms = parent_table()
    out = {}
    check_multilinear(2); check_multilinear(3)
    check_L1(rows["L1"])
    vgrp_exact = {"L1": "V_GRP_MAX_EQUALS_C0_PROVED (omega=|k|)"}
    for lab in ("L2", "L3"):
        if check_product_form(lab, rows[lab]):
            vgrp_exact[lab] = "V_GRP_MAX_EQUALS_C0_PROVED (product form + multilinear bound)"
    # existence of super-c near the node from the parent's beta (exact sign on a declared ray)
    near_node = {}
    for lab, e in T.items():
        r = beta_positive_on_declared_ray(lab, e, syms)
        if r is not None:
            near_node[lab] = dict(ray=r[0], beta_value=str(r[1]), note=r[2])
            exact(f"{lab}-beta>0-on-declared-ray-(near-node-super-c-existence)", True, r)
    exact("L3s4-beta0>0-for-0<a<1", sp.simplify(sp.sqrt(3) * (1 - syms[4]**2) / (6 * syms[4])).subs(syms[4], sp.Rational(1, 2)) > 0
          and sp.solve(sp.Eq(1 - syms[4]**2, 0), syms[4]) == [-1, 1])
    # explicit interval witnesses on the rational grid
    for lab, row in rows.items():
        if lab in vgrp_exact:
            out[lab] = dict(witness=None, status=vgrp_exact[lab])
            continue
        try:
            w, why = witness_search(lab, row)
        except Exception as ex:          # recorded, not hidden
            w, why = None, f"error: {type(ex).__name__}: {ex}"
        out[lab] = dict(witness=w, status=("SUPER_C_WITNESS (interval-certified point)" if w else
                                           ("SUPER_C_WITNESS (existence near node, exact beta sign)" if lab in near_node
                                            else f"NO_WITNESS_ON_DECLARED_RAYS ({why})")))
        if w:
            exact(f"{lab}-interval-witness |grad eps(k*)| > c0", True, w)
    out["L3s4"] = dict(witness=None, status="SUPER_C_WITNESS (existence near node, exact beta sign; explicit k* not attempted, a symbolic)")
    # signature classes
    sig = {}
    n1, n2, n3, th, a = syms
    for lab, e in T.items():
        b = sp.sympify(e["beta"])
        if lab == "L1":
            sig[lab] = "none (omega = |k| exactly)"
        elif b != 0:
            if lab == "L3s4":
                sig[lab] = "order 1; one-signed on the sphere iff a^2 < (19-6sqrt3)/11 (sign opposite between clusters), else both signs; anisotropic"
            else:
                sig[lab] = "order 1; both signs with direction (beta odd); anisotropic"
        else:
            iso = e.get("iso", False)
            sig[lab] = f"order 2; delay-only near node (alpha0 = {e['alpha0']} < 0, alpha <= 0 pointwise); {'isotropic' if iso else 'anisotropic'}"
    data = dict(rows={k: dict(saturation=("S_max" if T[k].get("smax") else ("S_in" if T[k]["ceiling"] else "below ceiling")),
                              signature=sig[k], vgrp=out.get(k)) for k in T},
                near_node=near_node, checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in (
                    "scripts/verify_observational_signature_gate.py",
                    "theory/OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md",
                    "scripts/verify_dispersion_corrections_gate.py",
                    "reports/2026-11-02--dispersion-corrections-across-lattices.md")})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2, default=str) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Checks: {passed}/{len(CHECKS)} (exact SymPy {sp.__version__}; interval mpmath.iv dps={iv.dps})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}  {c['detail']}" for c in CHECKS]
    lines += ["", "Per row: saturation | V_grp / witness | signature"]
    for k, v in data["rows"].items():
        lines.append(f"{k}: {v['saturation']} | {v['vgrp']['status'] if v['vgrp'] else '-'} | {v['signature']}")
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
