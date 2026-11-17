#!/usr/bin/env python3
"""S4 family as a homogeneous Arrighi-Facchini (AF) walk: explicit map.

Contract: theory/S4_AF_EXPLICIT_MAP_GATE.md, frozen at fcb6f50 (reading
R1-R3, equivalences E1-E8, ansatz A1-A3). Source: arXiv:1609.00305v2,
Eqs. (3)-(6), (16), (36).

Conventions (fixed here, all within R1-R3):
  psi in C^4 = C^2_sigma ⊗ C^2_tau; AF split psi = psi_+ ⊕ psi_- with
  psi_+ = components (0,1), psi_- = (2,3) (s = 2).
  Pair vector v = psi(x-1) ⊕ psi(x+1) in C^8 (pair index ⊗ internal).
  AF coordinates phi = (u, d, u', d') with (u, u') = H(psi_+(x+1),
  psi_+(x-1)) and (d, d') = H(psi_-(x+1), psi_-(x-1)), H Hadamard (Eq. (4)).
  Encoding E^(i): v -> encoded coordinates (contains the Hadamard, R3).
  P, P': C^8 -> C^4 select the unprimed (u,d) / primed (u',d') blocks.
  Grouped symbol of one homogeneous paired step (Eqs. (5)-(6)), with the
  node shift x -> x ∓ 2 carried by e^{∓ip} (p conjugate to the node index):
      G(p) = E† W' ( e^{-ip} J' + e^{ip} J ) E,   J' = [P'; 0], J = [0; P].

Checks (exact SymPy, a symbolic in (0,1), b = sqrt(1-a^2)):
  M1  J' = Pi Q', J = Pi Q with Pi = J' + J a permutation, Pi = X
      (= sigma_x ⊗ I_4, block swap), Q' + Q = I.
  M2  For each axis i, an explicit unitary E_i (built from exact
      eigenvectors of Gamma_i) with E_i† Q' E_i = I_2 ⊗ P_i^+.
  M3  With W'_i = E_i C_i E_i† Pi†, G_i(p) = C_i (I_2 ⊗ F_i(p)),
      F_i(p) = e^{-ip} P_i^+ + e^{ip} P_i^-: the paired step is pair-
      diagonal, i.e. on the psi lattice each site moves by ∓2 cells along
      axis i on the eigenspaces of Gamma_i (both parity sublattices
      evolve identically; E7 keeps one copy).
  M4  Composition: with C_x = W ⊗ I_2 and C_y = C_z = I, the psi-level
      symbol W F_x(2k_x) F_y(2k_y) F_z(2k_z) equals the family symbol
      A(k') with q_i = k'_i/sqrt3 = 2k_i (E8 rescaling), identically.
  M5  (Remark, not part of the verdict) Zeroth-order structure Eq. (16)
      in AF's phi coordinates: H C H† = I_4 ⊕ U holds for C = I (U = I) and
      fails for C = W ⊗ I_2 (unprimed block equals W ≠ I).
Fails closed on any failed check or exception.

Run 1 (2026-11-17, db25f3d) hit the 580 s timeout with no output (symbolic
eigenvects with square roots; buffered prints); retained in
reports/2026-11-17--s4-af-explicit-map-run1.txt. Eigenvectors are now
closed-form half-angle vectors on a rational parametrization; no
expectation changed.
Run 2 (0da360c): 30/31; M3 for axis x (C = W ⊗ I) reported FAIL because
simplify did not reduce exp(±i pi/4) products; retained in
reports/2026-11-17--s4-af-explicit-map-run2.txt. The zero test now applies
expand_complex before simplify (all checks); no expectation changed.
Run 3 (c8867fb): M1-M3 all PASS, then the 580 s timeout during the old M4
(expand_complex on the full product of exponentials); retained in
reports/2026-11-17--s4-af-explicit-map-run3.txt. M4 is now the per-factor
identity that makes the two ordered products equal; no expectation
changed.
"""
import sys

import sympy as sp
from sympy.physics.quantum import TensorProduct as TP

# Rational parametrization: c = cos(phi/2), s = sin(phi/2) with cos(phi) = a,
# c = (1-t^2)/(1+t^2), s = 2t/(1+t^2), t in (0,1); a = c^2 - s^2, b = 2cs.
# All identities below are polynomial in t, hence hold for every t in (0,1),
# which contains every a in (0,1) (and b = 2cs > 0).
tt = sp.symbols("t", positive=True)
c_ = (1 - tt**2) / (1 + tt**2)
s_ = 2 * tt / (1 + tt**2)
a = sp.simplify(c_**2 - s_**2)
b = sp.simplify(2 * c_ * s_)
p = sp.symbols("p", real=True)
k = sp.symbols("k_x k_y k_z", real=True)
I2, I4, I8 = sp.eye(2), sp.eye(4), sp.eye(8)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = {"x": sx, "y": sy, "z": sz}
T = {"x": b * sx + a * sz, "y": b * sy + a * sz, "z": -b * sx + a * sz}
G = {i: TP(SIG[i], T[i]) for i in "xyz"}
Pp = {i: (I4 + G[i]) / 2 for i in "xyz"}
Pm = {i: (I4 - G[i]) / 2 for i in "xyz"}
W = TP(I2, sp.diag(sp.exp(-sp.I * sp.pi / 4), sp.exp(sp.I * sp.pi / 4)))

checks = []


def ok(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)


def z(M):
    M = M.applyfunc(lambda e: sp.simplify(sp.expand_complex(sp.expand(e))))
    return M == sp.zeros(*M.shape)


# --- AF coordinates on the pair space -------------------------------------
# v index: (pair r in {0: x-1, 1: x+1}) * 4 + internal c
def vidx(r, c):
    return 4 * r + c


h = 1 / sp.sqrt(2)
Had = sp.zeros(8)  # v -> phi = (u0,u1,d0,d1,u'0,u'1,d'0,d'1)
for comp in range(2):          # component inside psi_+ / psi_-
    for blk, base in ((0, 0), (1, 2)):   # blk 0: psi_+ -> (u,u'); 1: psi_- -> (d,d')
        c = base + comp
        row_un = 2 * blk + comp          # u or d position
        row_pr = 4 + 2 * blk + comp      # u' or d' position
        # (u, u') = H (psi(x+1), psi(x-1))
        Had[row_un, vidx(1, c)] += h
        Had[row_un, vidx(0, c)] += h
        Had[row_pr, vidx(1, c)] += h
        Had[row_pr, vidx(0, c)] += -h
Pun = sp.zeros(4, 8)
Ppr = sp.zeros(4, 8)
for j in range(4):
    Pun[j, j] = 1
    Ppr[j, 4 + j] = 1
Jp = sp.Matrix.vstack(Ppr, sp.zeros(4, 8))
J = sp.Matrix.vstack(sp.zeros(4, 8), Pun)
Qp = sp.diag(0, 0, 0, 0, 1, 1, 1, 1)
Q = I8 - Qp
Pi = Jp + J
X = TP(sx, I4)

try:
    ok("Had unitary", z(Had * Had.H - I8))
    ok("M1 J' = Pi Q'", z(Jp - Pi * Qp))
    ok("M1 J = Pi Q", z(J - Pi * Q))
    ok("M1 Pi permutation and Pi = X (block swap)", z(Pi * Pi.T - I8) and z(Pi - X))

    for i in "xyz":
        # closed-form eigenvectors (half-angle), checked below
        sq = 1 / sp.sqrt(2)
        sv = {"x": (sp.Matrix([sq, sq]), sp.Matrix([sq, -sq])),
              "y": (sp.Matrix([sq, sp.I * sq]), sp.Matrix([sq, -sp.I * sq])),
              "z": (sp.Matrix([1, 0]), sp.Matrix([0, 1]))}[i]
        tv = {"x": (sp.Matrix([c_, s_]), sp.Matrix([-s_, c_])),
              "y": (sp.Matrix([c_, sp.I * s_]), sp.Matrix([sp.I * s_, c_])),
              "z": (sp.Matrix([c_, -s_]), sp.Matrix([s_, c_]))}[i]
        ok(f"M2 sigma_{i} eigenvectors", z(SIG[i] * sv[0] - sv[0]) and z(SIG[i] * sv[1] + sv[1]))
        ok(f"M2 T_{i} eigenvectors", z(T[i] * tv[0] - tv[0]) and z(T[i] * tv[1] + tv[1]))
        plus = [TP(sv[0], tv[0]), TP(sv[1], tv[1])]
        minus = [TP(sv[0], tv[1]), TP(sv[1], tv[0])]
        ok(f"M2 Gamma_{i}: two +1 and two -1 eigenvectors", len(plus) == 2 and len(minus) == 2)
        Vi = sp.Matrix.hstack(*(minus + plus))  # columns: -1, -1, +1, +1
        ok(f"M2 eigenbasis of Gamma_{i} unitary", z(Vi.H * Vi - I4))
        # On pair space: columns ordered so that the +1 eigenvectors of both
        # pair slots map to the primed coordinates 4..7.
        cols = []
        for vec in minus:
            for r in range(2):
                cols.append(TP(I2[:, r], vec))
        for vec in plus:
            for r in range(2):
                cols.append(TP(I2[:, r], vec))
        B = sp.Matrix.hstack(*cols)           # B e_j = basis vector j
        E = B.H                               # E: v -> encoded coordinates
        ok(f"M2 E_{i} unitary", z(E * E.H - I8))
        ok(f"M2 E_{i}† Q' E_{i} = I_2 ⊗ P_{i}^+", z(E.H * Qp * E - TP(I2, Pp[i])))
        Ci = TP(I2, W) if i == "x" else I8
        Wpi = E * Ci * E.H * Pi.H
        ok(f"M3 W'_{i} unitary", z(Wpi * Wpi.H - I8))
        Gp = E.H * Wpi * (sp.exp(-sp.I * p) * Jp + sp.exp(sp.I * p) * J) * E
        Fi = sp.exp(-sp.I * p) * Pp[i] + sp.exp(sp.I * p) * Pm[i]
        ok(f"M3 G_{i}(p) = C_{i} (I_2 ⊗ F_{i}(p))", z(Gp - Ci * TP(I2, Fi)))

    # M4 composition on the psi lattice, E8: q_i = 2 k_i. The AF symbol is
    # W F_x(2k_x) F_y(2k_y) F_z(2k_z) with F_i(q) = e^{-iq} P_i^+ + e^{iq} P_i^-;
    # the family symbol is W prod_i exp(-i q_i Gamma_i). Both are the same
    # ordered product once F_i(q) = cos(q) I - i sin(q) Gamma_i is shown for
    # a symbolic q, which is checked per axis.
    qq = sp.symbols("q", real=True)
    for i in "xyz":
        Fq = sp.exp(-sp.I * qq) * Pp[i] + sp.exp(sp.I * qq) * Pm[i]
        ok(f"M4 F_{i}(q) = cos q I - i sin q Gamma_{i} (factor of A at q_i = 2 k_i)",
           z((Fq - (sp.cos(qq) * I4 - sp.I * sp.sin(qq) * G[i])).applyfunc(
               lambda e: e.rewrite(sp.exp))))

    # M5 remark on Eq. (16)
    def zeroth(C):
        return Had * C * Had.H
    Z1 = zeroth(I8)
    ok("M5 remark: C = I gives I_4 ⊕ U with U = I", z(Z1 - I8))
    Zw = zeroth(TP(I2, W))
    ok("M5 remark: C = W ⊗ I_2 has unprimed block W ≠ I (Eq. (16) fails)",
       z(Zw[:4, 4:]) and not z(Zw[:4, :4] - I4))
except Exception as exc:
    print("FAIL exception:", repr(exc))
    sys.exit(1)

n_fail = sum(1 for _, c in checks if not c)
print(f"{len(checks) - n_fail}/{len(checks)} checks passed")
sys.exit(1 if n_fail else 0)
