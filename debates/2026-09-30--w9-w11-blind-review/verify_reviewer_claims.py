"""Check the checkable technical claims of the W9-W11 blind reviews (DeepSeek, Opus).

Run from the repo root: python3 debates/2026-09-30--w9-w11-blind-review/verify_reviewer_claims.py
Uses the same CJWW (5.15) walk as the W11 certificate (scripts/verify_directional_saturation.py).
"""
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from verify_directional_saturation import walk2, P1, P2, P3, PAULI  # noqa: E402

PS = (P1, P2, P3)
W = walk2()
t = sp.symbols("t", positive=True)
# Fixed generic directions (symbolic u makes the acos/sqrt series far too slow).
DIRS = [(1, 2, 3), (2, -1, 1), (1, 1, 1)]


def su2_parts(M):
    """M = a0 I + i a.sigma  ->  (a0, a)."""
    a0 = sp.simplify((M[0, 0] + M[1, 1]) / 2)
    a = [sp.simplify(sp.trace(M * s) / (2 * sp.I)) for s in PAULI]
    return a0, a


def sig(v):
    return sum((vi * s for vi, s in zip(v, PAULI)), sp.zeros(2))


def series_t(expr, n):
    return sp.series(expr, t, 0, n).removeO()


# W is in SU(2) along the ray: det = 1.
assert sp.simplify(W.det()) == 1
a0, a = su2_parts(W)
assert sp.simplify(W - (a0 * sp.eye(2) + sp.I * sig(a))) == sp.zeros(2)

# Branch-local H_eff with W = exp(-i H_eff): H_eff = -(theta/sin theta) a.sigma, theta = arccos a0.
E0 = sp.diag(1, -1, 1)


def heff_hir(d):
    ray = {p: t * di for p, di in zip(PS, d)}
    a0r, ar = a0.subs(ray), [x.subs(ray) for x in a]
    s2 = sum(x**2 for x in ar)
    # theta/sin(theta) with sin(theta) = |a|, cos(theta) = a0 (small t branch).
    ratio = series_t(sp.acos(a0r) / sp.sqrt(s2), 4)
    heff = [sp.expand(series_t(-ratio * x, 4)) for x in ar]
    hir = [sp.expand(series_t(-sum(E0[b, i] * sp.sin(PS[i]) for i in range(3)).subs(ray), 4))
           for b in range(3)]
    return heff, hir, ar


# 1. Mismatch H_eff - H_IR: no t^2 term (both reviewers: O(p^3), report says O(p^2)).
for d in DIRS:
    heff, hir, _ = heff_hir(d)
    diff = [sp.expand(h - g) for h, g in zip(heff, hir)]
    assert all(x.coeff(t, 1) == 0 and x.coeff(t, 2) == 0 for x in diff), d
    assert any(sp.nsimplify(x.coeff(t, 3)) != 0 for x in diff), d
print(f"[PASS] H_eff - H_IR = Theta(|p|^3), not only O(|p|^2), along {DIRS} (both reviewers)")

# 1b. Opus counterexample: on the p3 axis W = exp(i p3 sigma3) exactly, so H_eff = -p3 sigma3 exactly.
W3 = W.subs({P1: 0, P2: 0})
assert sp.simplify(W3 - sp.diag(sp.exp(sp.I * P3), sp.exp(-sp.I * P3))) == sp.zeros(2)
print("[PASS] p3 axis: W = exp(i p3 sigma3) exactly (Opus counterexample)")

# 1c. DeepSeek's cubic formula H_eff = -A - (p^2/6) A + O(p^4) is contradicted on the p3 axis.
heff_axis, _, _ = heff_hir((0, 0, 1))
assert [sp.simplify(h) for h in heff_axis] == [0, 0, -t]
print("[CLAIM REFUTED] DeepSeek's -(p^2/6)A cubic term: on the p3 axis H_eff = -p3 sigma3 exactly")

# 2. Nodes: W = +-I at the 8 corners, 4 each; frames at the +I nodes and their det signs.
corners = [(x, y, z) for x in (0, sp.pi) for y in (0, sp.pi) for z in (0, sp.pi)]
plus, minus = [], []
for c in corners:
    Wc = sp.simplify(W.subs(dict(zip(PS, c))))
    if Wc == sp.eye(2):
        plus.append(c)
    elif Wc == -sp.eye(2):
        minus.append(c)
    else:
        raise AssertionError(f"W({c}) is not +-I")
assert len(plus) == 4 and len(minus) == 4
dets = []
for c in plus:
    J = sp.zeros(3)
    for i, p in enumerate(PS):
        dWc = sp.simplify(sp.diff(W, p).subs(dict(zip(PS, c))))
        for b, s in enumerate(PAULI):
            J[b, i] = sp.simplify(sp.trace(dWc * s) / (2 * sp.I))
    dets.append(sp.sign(J.det()))
assert sorted(dets) == [-1, -1, 1, 1]
print(f"[PASS] W=+I at {plus}, W=-I at {minus}; +I-node frame det signs {dets}: net chirality 0 (Opus)")

# 3. H_IR does not commute with W: [H_IR, W] = O(p^4) along a generic ray, nonzero.
Hir_full = -sum((E0[b, i] * sp.sin(PS[i]) * PAULI[b] for b in range(3) for i in range(3)), sp.zeros(2))
for d in DIRS:
    ray = {p: t * di for p, di in zip(PS, d)}
    comm = (Hir_full * W - W * Hir_full).subs(ray)
    entries = [sp.expand(series_t(e, 6)) for e in comm]
    assert all(e.coeff(t, k) == 0 for e in entries for k in range(4)), d
    assert any(sp.nsimplify(e.coeff(t, 4)) != 0 or sp.nsimplify(e.coeff(t, 5)) != 0 for e in entries), d
print("[PASS] [H_IR, W] = O(|p|^4) and nonzero: sum_x H_IR is not conserved by the walk (Opus)")

# 4. K = i(W - W^dagger)/2 = -a.sigma commutes with W and equals H_eff + O(p^3).
K = sp.I * (W - W.H) / 2
assert sp.simplify(K * W - W * K) == sp.zeros(2)
for d in DIRS:
    heff, _, ar = heff_hir(d)
    kr = [sp.expand(series_t(-x, 4)) for x in ar]
    assert all(sp.expand(k - h).coeff(t, 1) == 0 and sp.expand(k - h).coeff(t, 2) == 0
               for k, h in zip(kr, heff)), d
print("[PASS] K = i(U-U^dagger)/2 commutes with W and K - H_eff = O(|p|^3) (Opus)")

# 5. Momentum surrogate: scalar symbol sin p_i * I commutes with W (exactly conserved in total).
for p in PS:
    assert sp.simplify(sp.sin(p) * W - W * sp.sin(p)) == sp.zeros(2)
print("[PASS] sum_x pi_i(x) has scalar symbol sin p_i and commutes with W (Opus, F4)")

print("\nNot checked here: Opus's F3 parity no-go, the Belinfante/q != 0 kernel claims, and all prior-art statements.")
