# Thirring low-energy packet gate: results and closing balance

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: written proof plus exact
author checks; no independent review, no promotion.**

Contract [THIRRING_LOW_ENERGY_PACKET_GATE.md](../theory/THIRRING_LOW_ENERGY_PACKET_GATE.md),
frozen by Codex at `715096f` before execution: contract 2 of 2 of the Thirring
coexistence line. Exact verifier and labelled diagnostic committed before
running at `75b33c3`. First run: one failure, retained (Sec. 6). Passing
exact run at `8b41761`.

## 1. Verdict

`NO_ENTANGLER_IN_DECLARED_PACKET_CODE`: the necessary condition
||E_mu|| -> 0 is disproved. For each logical input,

  lim_{mu -> 0} ||E_mu|ab>||^2 = |T_ab - 1|^2 / 4 =: l_ab,

with exact values

| Input ab | l_ab |
| --- | --- |
| 00 | 1/3 |
| 01, 10 | (sqrt10 + 1)/(2(sqrt10 + 2)) ≈ 0.4031 |
| 11 | 4/9 |

The outgoing doubler content (the contract's Q_D observable) has the same
limits. The logical compression tends to diag((1+T_ab)/2), which is not
unitary.

Scope: this packet code, chi = pi/2, mu -> 0, the rule only. Not a no-go for
the Thirring QCA, for other codes or for other resources (contract, "Neither
excludes Thirring").

## 2. Admission (certified or immediate)

- Envelope: int h^2 = 1 (P1). The A, B momentum bins are disjoint and inside
  0 < |q| < 4 mu for 0 < mu < 1/10 (P7). Hence the four columns are
  orthonormal, B_mu is an isometry, and Q_D B_mu = 0.
- Positive band at q = O(mu); sin omega(mu K)/mu -> sqrt(1+K^2), so
  omega(mu K)/mu -> sqrt(1+K^2) (P5).
- omega'(q) = nu sin q / sin omega > 0 (P5). With |q> = sum e^{-iqx}|x>, the
  stationary phase of e^{-i(qx + omega t)} is at x = -omega'(q) t: positive-band
  positive q moves toward negative x, as the contract states. A modes start
  at +L moving left and B modes at -L moving right, so the packets collide.
- B_out = F^T B_mu keeps band and momenta, so Q_D B_out = 0.

## 3. Structure: only the opposite-Gamma half interacts

- Gamma = sigma_z (-1)^x satisfies Gamma W Gamma = -W (P2), so
  G := Gamma_1 Gamma_2 commutes with F = W ⊗ W.
- Contact configurations (same site, opposite components) have G = -1
  (P4). Hence J is the identity on the G = +1 subspace, and with
  P := (1 - G)/2,

    U (1-P) = F (1-P)   exactly.

- G shifts both momenta by pi and flips both bands (sigma_z v^+_q = v^-_{q+pi},
  P2). So G B_mu has both particles in the negative band within 4 mu of pi
  (P7). Its momentum support is disjoint from that of every column of B_mu.
  Therefore <B_mu, G B_mu> = 0, ||P B_mu|ab>||^2 = 1/2, Q_D G B_mu = G B_mu,
  and F^T G B_mu is orthogonal to the range of B_out.

## 4. The packet/scattering bridge (written proof)

Fix a column and write its two-particle amplitude as
c(q1,q2) = phi_A(q1) phi_B(q2), where phi_A carries e^{iq1 L} and phi_B
carries e^{-iq2 L}. Here q1 = p + k and q2 = p - k, with y = x1 - x2 and
w = x1 + x2.

**(i) Exact eigenfunctions.** For each (q1, q2) in the support, the
interacting P-sector solution is (1711.03920 Eq.(12) / 1804.08508 Eq.(18)):

    f_{q1,q2} = [v^{++} - (-1)^{x1+x2} v^{--}] e^{-i(q1 x1 + q2 x2)}
                - T(q1,q2) [v^{++}_swap - (-1)^{x1+x2} v^{--}_swap] e^{-i(q2 x1 + q1 x2)}

on y ≥ 0, with the phase e^{-i chi} on RL at y = 0 and antisymmetric
extension. It is an exact lattice eigenvector of U with eigenvalue
e^{-i omega(q1)} e^{-i omega(q2)}. There are no evanescent terms. Certified
at two algebraic momentum pairs, one with p = 0 (P3). For chi = 0 the same
form, with T = 1 and no phase, is an exact eigenvector of F (P3). Here
T(q1,q2) = [g_+(q1) + e^{-i chi} g_+(q2)] / [g_+(q2) + e^{-i chi} g_+(q1)],
and |T| = 1.

**(ii) Exact approximate solution.** Let
psi~(t) = (1/sqrt2) ∫∫ c(q1,q2) e^{-it(omega(q1)+omega(q2))} (1/2) f_{q1,q2} dq1 dq2,
with normalized spinors (the swap and doubler partners have the same norm,
P2). Since each f is an exact eigenvector and c is bounded with compact
support, U psi~(t) = psi~(t+1) exactly. psi~(t) lies in l^2 by the tail
bound below. Unitarity gives

    ||U^T P B|ab> - psi~(T)|| = ||P B|ab> - psi~(0)||.

**(iii) Initial error.** By the identity P(plane wave) = (1/2)[v^{++} -
(-1)^{x1+x2} v^{--}] e^{-i(q1 x1 + q2 x2)} (P2), the A⊗B term of P B|ab> on
y ≥ 0 equals the incoming part of psi~(0). The rest of P B|ab> - psi~(0) is
supported where some packet is at least L from its centre:

- the B⊗A term on y ≥ 0, centred at y = -2L;
- the outgoing part of psi~(0), centred at y = -2L;
- the incoming part on y < 0;
- the line y = 0.

One-particle tail bound: integrating by parts twice (h is continuous,
piecewise smooth, with jumps of h' at ±1),

    |packet(x)| ≤ C min(delta^{1/2}, delta^{-3/2} |x - x_c|^{-2}),

so the l^2 mass beyond distance D is at most C (delta D)^{-3}. With D = L
and delta L = mu^{-1/2}, the initial error is O(mu^{3/4}).

**(iv) Time T.** The phase is q x + t omega(q), with derivative
x - x_c + t omega'(q). On the support, omega'(mu K) ≥ 0.55 for both packets
(P5, rational bounds for 0 < mu < 1/10). So the incoming part of psi~(T) has
y-centre at most 2L - 1.10 · 4L = -2.4L. The outgoing part has y-centre at
least +2.4L.

Spreading is T delta max omega'' ≤ 4L mu^{3/2} (C/mu) = O(mu^{-3/2}), much
less than L. Repeating the integration by parts with the extra terms
t omega'' ≤ C T/mu, whose contribution is controlled by
(T/mu) D^{-3} = O(mu^3), shows that the incoming part restricted to y ≥ 0,
and the y = 0 line, are O(mu^{3/4}).

The same holds for the free solution psi~_free (chi = 0, T = 1), with
||F^T P B - psi~_free(T)|| = O(mu^{3/4}).

**(v) Phase variation.** At low energy, g_+(mu Q) = -i mu e^{asinh Q}(1 + O(mu))
(P6). So T is a smooth function of (q1/mu, q2/mu) with denominator bounded
below by c mu, and |grad T| ≤ C/mu on the support. The support has width
O(delta) around the centre (q1c, q2c) = (mu k_a, -mu k_b), so
sup |T - T_c| = O(delta/mu) = O(mu^{1/2}), with T_c := T(q1c, q2c). Hence

    U^T P B|ab> = T_c F^T P B|ab> + O(mu^{1/2}).

**(vi) Assembly.** Using Sec. 3,

    U^T B = F^T (1-P) B + U^T P B
          = F^T B + (T_c - 1) F^T P B + o(1)
          = F^T [ (1+T_c)/2 B - (T_c - 1)/2 G B ] + o(1).

Since F^T G B is orthogonal to B_out and lies in the range of Q_D:

- K_mu -> diag((1+T_ab)/2);
- ||E_mu|ab>||^2 -> |T_ab - 1|^2 / 4;
- ||Q_D U^T B|ab>||^2 has the same limit.

T_c -> T_ab, given by the rapidity form
(e^{theta_a} - i e^{-theta_b}) / (e^{-theta_b} - i e^{theta_a}), with
theta = asinh k (P6). Then l_ab = (cosh Delta - 1)/(2 cosh Delta), with
Delta = asinh k_a + asinh k_b. Since Delta > 0 for this code, l_ab > 0.

Error budget: O(mu^{1/2}) from the phase variation and O(mu^{3/4}) from the
tails. The constants in (iii)-(v) are written, not machine-checked.

## 5. Diagnostic (labelled, decides nothing)

[Diagnostic](2026-11-09--thirring-low-energy-packet-diagnostic.txt): direct
lattice evolution at mu = 1/11 (L = 121, T = 484, box of 1520 sites, packet
norms 0.99989). Measured values against the finite-mu prediction
|T_c - 1|^2/4:

| Input | Leakage | Doubler content | Prediction |
| --- | --- | --- | --- |
| 00 | 0.3312 | 0.3291 | 0.3321 |
| 01 | 0.4015 | 0.3996 | 0.4019 |
| 10 | 0.4015 | 0.3996 | 0.4019 |
| 11 | 0.4434 | 0.4415 | 0.4435 |

This is a second, independent route to the same mechanism. Per the
contract it is not evidence for the asymptotic verdict.

## 6. Verifier and failed run

[Script](../scripts/verify_thirring_low_energy_packet.py),
[record](2026-11-09--thirring-low-energy-packet.txt),
[JSON](2026-11-09--thirring-low-energy-packet.json): **39/39 exact checks**.

Run 1 (`75b33c3`) failed the velocity bound. I had written 0.555; the
certified chain gives about 0.5545. The constant was lowered to 0.55
(closing margin -2.4L instead of about -2.44L), which the argument allows.
Records: `-failed-run-1.{txt,json}`, with a note appended.

Diagnostic script: [diag](../scripts/diag_thirring_low_energy_packet.py).

## 7. Closing balance of the Thirring coexistence line (mandatory)

- **Contract 1** (two-particle low-energy preflight): `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`.
- **Contract 2** (low-energy packets): `NO_ENTANGLER_IN_DECLARED_PACKET_CODE`.
  The opposite-Gamma half of a low-energy pair acquires the scattering
  phase T, which depends only on the rapidity difference. The same-Gamma
  half evolves freely. Their relative phase generates doubler content and
  leakage |T - 1|^2/4 that does not vanish as mu -> 0. This is the momentum
  transfer described in 1804.08508 (abstract), made quantitative for
  packets.
- **Scientific discard:** this packet code only. Not the Thirring model,
  other codes, ancillas, measurement or geometry.
- **Operational:** the two-contract budget is exhausted. By the decision of
  2026-11-09, the Thirring coexistence line stops. The coexistence question
  remains **OPEN**: no exclusion is demonstrated beyond the declared codes.
  There is no automatic third contract.
- **Recorded for whoever resumes:** in this rule, any code whose carriers
  are split between the G = ±1 halves with T ≠ 1 leaks into doublers. A
  code would have to live entirely in one half, or use T = 1 kinematics
  (Delta = 0, no entangling phase). This is a remark, not a theorem.
