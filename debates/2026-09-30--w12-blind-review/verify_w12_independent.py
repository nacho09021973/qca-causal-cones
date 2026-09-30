"""Independent re-derivation of W12 (Claude), not reusing scripts/verify_w12_*.py.

Derivation by hand: at a +I node p_*, sin((p_*+k).d_r) = cos(p_*.d_r) (k.d_r) + O(k^3), and
s_* W_0(p_*+k) = I + O(k), so to first order in g and k
    delta E_* = -2 Z T_* D,   T_* = diag(cos(p_*.d_r)),   D rows d_1=(1,0,0), d_2=(1,1,0), d_3=(1,1,1),
and delta h_* = E_*^T delta E_* + delta E_*^T E_*, with E_* = diag(s2 s3, -s3, 1), s_i = (-1)^{b_i}.
This script checks the first identity against walk2() at each node, then computes dim U and the
universal metric rank with exact rational linear algebra.
Run from the repo root.
"""
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from verify_directional_saturation import walk2, P1, P2, P3, PAULI  # noqa: E402

PS = (P1, P2, P3)
D = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
PLUS = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
z = sp.symbols("z11 z12 z13 z21 z22 z23 z31 z32 z33")
Z = sp.Matrix(3, 3, z)
g = sp.Symbol("g")


def frame(b):
    s = [(-1) ** x for x in b]
    return sp.diag(s[1] * s[2], -s[2], 1)


def T(b):
    return sp.diag(*[sp.cos(sp.pi * sum(bi * di for bi, di in zip(b, D.row(r)))) for r in range(3)])


# Check delta E_* = -2 Z T_* D against the actual deformed symbol, both product orders.
J = sum((Z[a, r] * 2 * sp.sin(sum(PS[i] * D[r, i] for i in range(3))) * PAULI[a]
         for a in range(3) for r in range(3)), sp.zeros(2))
W = walk2()
for b in PLUS:
    shift = {p: sp.pi * bi + p for p, bi in zip(PS, b)}
    for Wg in (W * (sp.eye(2) - sp.I * g * J), (sp.eye(2) - sp.I * g * J) * W):
        M = Wg.subs(shift, simultaneous=True)
        E = sp.zeros(3)
        for i, p in enumerate(PS):
            dM = sp.diff(M, p).subs({q: 0 for q in PS})
            for a in range(3):
                E[a, i] = sp.simplify(sp.trace(dM * PAULI[a]) / (2 * sp.I))
        dE = sp.expand(sp.diff(E, g).subs(g, 0))
        assert sp.simplify(E.subs(g, 0) - frame(b)) == sp.zeros(3), b
        assert sp.simplify(dE - (-2 * Z * T(b) * D)) == sp.zeros(3), b
print("[PASS] delta E_* = -2 Z T_* D at the four +I nodes, both product orders")

comps = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]


def dh(b):
    dE = -2 * Z * T(b) * D
    Eb = frame(b)
    H = Eb.T * dE + dE.T * Eb
    return sp.Matrix([sp.expand(H[i, j]) for i, j in comps])


def lin(vec):
    return sp.Matrix([[sp.diff(v, zz) for zz in z] for v in vec])


h = [dh(b) for b in PLUS]
Phi = sp.Matrix.vstack(*[lin(h[k] - h[0]) for k in (1, 2, 3)])
U = Phi.nullspace()
print(f"[U3] rank Phi = {Phi.rank()}, dim U = {len(U)}")
Ub = sp.Matrix.hstack(*U)
R = lin(h[0]) * Ub
print(f"[U4] universal metric rank = {R.rank()}/6")
common_null = (sp.Matrix.vstack(*[lin(x) for x in h])).nullspace()
print(f"[U5] common frame-rotation dimension (all four +I) = {len(common_null)}")
assert len(U) == 3 and R.rank() == 3 and len(common_null) == 0
print("[PASS] independent derivation reproduces dim U = 3, rank 3/6, no common rotation "
      "-> UNIVERSAL_SUBFAMILY_DEFICIENT")

# Robustness: other metric convention h = E E^T (index placement swapped).
h2 = []
for b in PLUS:
    dE = -2 * Z * T(b) * D
    Eb = frame(b)
    H = Eb * dE.T + dE * Eb.T
    h2.append(sp.Matrix([sp.expand(H[i, j]) for i, j in comps]))
Phi2 = sp.Matrix.vstack(*[lin(h2[k] - h2[0]) for k in (1, 2, 3)])
U2 = Phi2.nullspace()
R2 = lin(h2[0]) * sp.Matrix.hstack(*U2) if U2 else sp.zeros(6, 0)
print(f"[robustness] with h = E E^T (internal-index metric): dim U = {len(U2)}, rank = {R2.rank() if U2 else 0}/6")
