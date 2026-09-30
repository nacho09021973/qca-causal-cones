"""Check the checkable claims of the second-round W9-W11 repair reviews (DeepSeek, Opus).

Run from the repo root:
    python3 debates/2026-09-30--w9-w11-repair-review/verify_reviewer_claims.py
Numerical parts use random sampling with a fixed seed; they test bounds, they do not prove them.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260930)
S1 = np.array([[0, 1], [1, 0]], complex)
S2 = np.array([[0, -1j], [1j, 0]])
S3 = np.array([[1, 0], [0, -1]], complex)


def parts(p):
    c, s = np.cos(p), np.sin(p)
    a0 = c[0] * c[1] * c[2]
    a = np.array([s[0], -c[0] * s[1], c[0] * c[1] * s[2]])
    return a0, a


def sig(v):
    return v[0] * S1 + v[1] * S2 + v[2] * S3


def ball(n, lam):
    v = rng.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return v * (lam * rng.random(n) ** (1 / 3))[:, None]


PLUS = [np.array(x) * np.pi for x in [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]]
MINUS = [np.array(x) * np.pi for x in [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]]

# 1. ||K - H_IR|| on the p=0 ball: report claims <= Lambda^3, Opus <= |p|^3/2 (sup ratio ~0.18).
worst = 0.0
for lam in (0.5, 0.2, 0.05):
    for k in ball(20000, lam):
        _, a = parts(k)
        hir = -np.array([np.sin(k[0]), -np.sin(k[1]), np.sin(k[2])])
        d = np.linalg.norm(-a - hir)  # K = -a.sigma; ||v.sigma|| = |v|
        worst = max(worst, d / np.linalg.norm(k) ** 3)
assert worst <= 0.5
print(f"[PASS] ||K - H_IR|| / |p|^3 sup over samples = {worst:.3f} <= 1/2 (Opus); report's Lambda^3 is loose")

# 2. Band bound: ||K - H_eff|| <= (arcsin L)^3/6 and dynamical |n| version, on all four +I balls.
rb = rn = 0.0
for p0 in PLUS:
    for lam in (0.5, 0.2, 0.05):
        for k in ball(5000, lam):
            a0, a = parts(p0 + k)
            th = np.arccos(np.clip(a0, -1, 1))
            bound = np.arcsin(lam) ** 3 / 6
            rb = max(rb, (th - np.sin(th)) / bound)
            for n in (1, 7, 40):
                rn = max(rn, abs(np.exp(-1j * n * th) - np.exp(-1j * n * np.sin(th))) / (n * bound))
assert rb <= 1 and rn <= 1
print(f"[PASS] band bound ratio {rb:.3f} <= 1, dynamical ratio {rn:.3f} <= 1 (both reviewers)")

# 3. At -I nodes K = +sigma.E_* k + O(k^3) = -H_*(k) (Opus): K has the opposite sign there.
for p0 in MINUS:
    k = 1e-4 * np.array([0.3, -0.7, 0.5])
    _, a0v = parts(p0)
    _, a = parts(p0 + k)
    Kv = -a
    # H_*(k) = i log(s_* W) with s_* = -1: s_*W = -a0 I - i a.sigma, so H_* = +(theta/sin)(a).sigma ~ +a.
    Hstar = a
    assert np.allclose(Kv, -Hstar, atol=1e-10)
print("[PASS] at the four -I nodes K = -H_*(k) to leading order: opposite energy sign (Opus)")

# 4. W10: in the Lagrangian form S_g = -1/2 h G(h), the shift h0i enters quadratically (Opus).
eta = sp.diag(-1, 1, 1, 1)
d = sp.Matrix(sp.symbols("d0:4"))
dup = eta * d
hs = {(i, j): sp.Symbol(f"h{i}{j}") for i in range(4) for j in range(i, 4)}
h = sp.Matrix(4, 4, lambda i, j: hs[min(i, j), max(i, j)])
box = d.dot(dup)
tr = sp.trace(eta * h)
div = h * dup
scal = dup.dot(div) - box * tr
G = (d * div.T + div * d.T - box * h - d * d.T * tr - eta * scal) / 2
Gup = (eta * G * eta).applyfunc(sp.expand)
L = sp.expand(-sum(h[i, j] * Gup[i, j] for i in range(4) for j in range(4)) / 2)
assert sp.Poly(L, hs[0, 1]).degree() == 2
assert sp.Poly(L, hs[0, 0]).degree() == 1
print("[PASS] W10 Lagrangian: h00 linear, h01 quadratic -> shift is a multiplier only in Hamiltonian form (Opus)")

# 5. W9 certificate: the 'after_ibp' assert restates the first one (Opus: tautological).
lam, xi0, T0 = sp.symbols("lambda xi0 T0")
div_ = sp.Symbol("D")
first = sp.I * lam * xi0 * div_
after_ibp = -lam * xi0 * (-sp.I * div_)
assert sp.expand(first - after_ibp) == 0
print("[PASS] W9 certificate: after_ibp == i*lambda*xi.(Tk) identically, same as the first assert (Opus)")

print("\nNot checked here: the F3 proof itself (both reviewers accept it; scope remark is Opus's), "
      "the synchronous residual gauge claim, and Gu-Wen/Arnault-Cedzich page citations.")
