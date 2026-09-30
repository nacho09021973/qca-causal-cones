"""Check Opus's additional claims in the W12 blind review (DeepSeek adds none beyond the report).

Uses the hand-derived first-order formula delta E_* = -2 Z T_* D, which
verify_w12_independent.py checks against walk2() at the +I nodes; here it is also checked at the
-I nodes before use. Run from the repo root.
"""
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from verify_directional_saturation import walk2, P1, P2, P3, PAULI  # noqa: E402

PS = (P1, P2, P3)
D = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
PLUS = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
MINUS = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
z = sp.symbols("z11 z12 z13 z21 z22 z23 z31 z32 z33")
Z = sp.Matrix(3, 3, z)
g = sp.Symbol("g")
comps = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def frame(b):
    s = [(-1) ** x for x in b]
    return sp.diag(s[1] * s[2], -s[2], 1)


def T(b):
    return sp.diag(*[sp.cos(sp.pi * sum(bi * di for bi, di in zip(b, D.row(r)))) for r in range(3)])


def dh(b):
    dE = -2 * Z * T(b) * D
    H = frame(b).T * dE + dE.T * frame(b)
    return sp.Matrix([sp.expand(H[i, j]) for i, j in comps])


def lin(v):
    return sp.Matrix([[sp.diff(x, zz) for zz in z] for x in v])


# 0. The formula also holds at the -I nodes (with s_* = -1 normalization).
J = sum((Z[a, r] * 2 * sp.sin(sum(PS[i] * D[r, i] for i in range(3))) * PAULI[a]
         for a in range(3) for r in range(3)), sp.zeros(2))
for b in MINUS:
    M = (-(walk2() * (sp.eye(2) - sp.I * g * J))).subs({p: sp.pi * bi + p for p, bi in zip(PS, b)},
                                                      simultaneous=True)
    E = sp.zeros(3)
    for i, p in enumerate(PS):
        dM = sp.diff(M, p).subs({q: 0 for q in PS})
        for a in range(3):
            E[a, i] = sp.simplify(sp.trace(dM * PAULI[a]) / (2 * sp.I))
    assert sp.simplify(E.subs(g, 0) - frame(b)) == sp.zeros(3), b
    assert sp.simplify(sp.expand(sp.diff(E, g).subs(g, 0)) + 2 * Z * T(b) * D) == sp.zeros(3), b
print("[PASS] delta E_* = -2 Z T_* D also at the four -I nodes")

# 1. On U = diag(z11,z22,z33): delta h at -I nodes = - delta h at +I nodes; 8-node test NON_UNIVERSAL.
diagsub = {x: 0 for x in z if str(x) not in ("z11", "z22", "z33")}
hp = dh(PLUS[0]).subs(diagsub)
for b in MINUS:
    assert sp.expand(dh(b).subs(diagsub) + hp) == sp.zeros(6, 1), b
allnodes = PLUS + MINUS
Phi8 = sp.Matrix.vstack(*[lin(dh(b) - dh(PLUS[0])) for b in allnodes[1:]])
U8 = Phi8.nullspace()
r8 = (lin(dh(PLUS[0])) * sp.Matrix.hstack(*U8)).rank() if U8 else 0
print(f"[PASS] on U, delta h(-I) = -delta h(+I); 8-node test: dim U8 = {len(U8)}, metric rank {r8}")
assert r8 == 0

# 2. Each +I node alone has metric rank 6, and node-dependent 3-dim rotation kernels.
kers = []
for b in PLUS:
    L = lin(dh(b))
    assert L.rank() == 6
    kers.append(sp.Matrix.hstack(*L.nullspace()))
same = all(sp.Matrix.hstack(kers[0], k).rank() == 3 for k in kers[1:])
assert not same
print("[PASS] per-node metric rank 6 at each +I node; per-node rotation kernels are node-dependent")

# 3. Gauge reading: symbol of the three missing relations applied to h = d_i xi_j + d_j xi_i.
q = sp.symbols("q1 q2 q3")
xi = sp.symbols("x1 x2 x3")
hq = sp.Matrix(3, 3, lambda i, j: q[i] * xi[j] + q[j] * xi[i])
rel = [hq[0, 1] - hq[1, 1] / 2, hq[0, 2] - hq[2, 2] / 2, hq[1, 2] - hq[2, 2] / 2]
Mq = sp.Matrix([[sp.diff(r, x) for x in xi] for r in rel])
det = sp.factor(Mq.det())
print(f"[INFO] gauge-condition symbol det = {det}")
target = -q[2] * (2 * q[0] * q[1] - q[0] * q[2] - q[1] ** 2)
print(f"[{'PASS' if sp.expand(det - target) == 0 else 'DIFFERS'}] Opus's determinant "
      f"-q3(2 q1 q2 - q1 q3 - q2^2) (up to the overall normalisation of the relations)")
