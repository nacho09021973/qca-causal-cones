"""Diagnostic run for theory/GENERAL_IR_RATE_ZONOTOPES_DIAGNOSTIC.md.

Ten product walks S(k) = prod_j exp(i (k.a_j) n_j.sigma), n_j = a_j/|a_j|,
whose causal bodies are zonotopes in d = 2, 3. Reuses, read-only, the
functions of scripts/diagnose_general_ir_rate_polyhedra.py (author's script,
unreviewed); replaces only the walk list and adds the declared fallback of
the vertex chooser. Floating point; labels are diagnostic, not certificates
or verdicts.

Run from the repository root:
    python3 -B scripts/diagnose_general_ir_rate_zonotopes.py --output reports/<name>.json
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import diagnose_general_ir_rate_polyhedra as P  # noqa: E402

PAULI = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]
R3 = sp.sqrt(3)
TRI = [sp.Matrix([1, 0]), sp.Matrix([sp.Rational(1, 2), R3 / 2])]
HEXP = [sp.Matrix([1, 0, 0]), sp.Matrix([sp.Rational(1, 2), R3 / 2, 0]),
        sp.Matrix([0, 0, sp.Rational(3, 2)])]


def identity_gens(d):
    return [sp.eye(d)[:, i] for i in range(d)]


# (id, description, generators, list of integer exponent vectors of a_j)
ROWS = [
    ("Z1", "octagon (1,0),(0,1),(1,1),(1,-1)", identity_gens(2),
     [(1, 0), (0, 1), (1, 1), (1, -1)]),
    ("Z2", "octagon (2,0),(0,2),(1,1),(1,-1)", identity_gens(2),
     [(2, 0), (0, 2), (1, 1), (1, -1)]),
    ("Z3", "regular hexagon", TRI, [(1, 0), (0, 1), (-1, 1)]),
    ("Z4", "dodecagon, triangular lattice", TRI,
     [(1, 0), (0, 1), (-1, 1), (-1, 2), (1, 1), (2, -1)]),
    ("Z5", "octagon of Z1, other factor order", identity_gens(2),
     [(1, 1), (1, 0), (1, -1), (0, 1)]),
    ("Z6", "rhombic dodecahedron", identity_gens(3),
     [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]),
    ("Z7", "truncated octahedron", identity_gens(3),
     [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]),
    ("Z8", "axes + body diagonals", identity_gens(3),
     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]),
    ("Z9", "great rhombicuboctahedron", identity_gens(3),
     [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1),
      (0, 1, 1), (0, 1, -1)]),
    ("Z10", "hexagonal prism", HEXP, [(1, 0, 0), (0, 1, 0), (-1, 1, 0), (0, 0, 1)]),
]


def product_walk(gens, expos):
    d = len(gens)
    zs = sp.symbols(f"w1:{d + 1}")
    G = sp.Matrix.hstack(*gens)
    M = sp.eye(2)
    for m in expos:
        a = G * sp.Matrix(m)
        nvec = list(a / sp.sqrt(a.dot(a))) + [0] * (3 - d)
        Gam = sum((c * s for c, s in zip(nvec, PAULI)), sp.zeros(2))
        mono = sp.Mul(*[z ** k for z, k in zip(zs, m)])
        M = M * ((sp.eye(2) + Gam) / 2 * mono + (sp.eye(2) - Gam) / 2 / mono)
    return M.applyfunc(sp.expand), zs, gens


FALLBACK = {}
_original_choose = P.choose_vertex


def choose_with_fallback(steps, d, sym):
    try:
        return _original_choose(steps, d, sym)
    except RuntimeError:
        FALLBACK["used"] = True
        pts = list(steps.values())
        norms = [float(sp.sqrt(v.dot(v))) for v in pts]
        return pts[int(np.argmax(norms))]


P.choose_vertex = choose_with_fallback


def frame_isotropy(gens, expos):
    G = np.array([[float(x) for x in g] for g in gens]).T
    S = sum(np.outer(G @ np.array(m, float), G @ np.array(m, float))
            / np.linalg.norm(G @ np.array(m, float)) for m in expos)
    return float(np.max(np.abs(S - np.trace(S) / len(S) * np.eye(len(S)))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    results = []
    for zid, name, gens, expos in ROWS:
        FALLBACK.clear()
        r = P.analyse(zid, name, lambda g=gens, e=expos: product_walk(g, e), None)
        r["frame_isotropy_defect"] = frame_isotropy(gens, expos)
        if FALLBACK.get("used"):
            r["label"] = "NO_RATE_AXIS; " + r["label"]
        results.append(r)
        print(f"{zid} {name}: {r['label']}")
        for k in ("K_star", "t_star", "lattice_isometric_to_Zd", "frame_isotropy_defect"):
            if k in r:
                print(f"    {k} = {r[k]}")
        if "node" in r:
            print(f"    c_IR = {r['node']['c_IR']}")
        if "hypotheses" in r:
            print("    " + ", ".join(f"{k}={v}" for k, v in r["hypotheses"].items()))
            print(f"    dominant points: {len(r['dominant_points'])}")
    meta = dict(charter="theory/GENERAL_IR_RATE_ZONOTOPES_DIAGNOSTIC.md",
                script_sha256=P.sha(__file__), parent_script_sha256=P.sha(P.__file__),
                numpy=np.__version__, sympy=sp.__version__,
                nature="floating-point diagnostic; labels are not certificates or verdicts")
    args.output.write_text(json.dumps(dict(meta=meta, walks=results), indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
