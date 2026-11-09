# Thirring two-particle low-energy preflight: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: author derivation plus
exact author checks; one sealed cross-family review (Grok) with repairs
applied below, not re-reviewed; no promotion.**

[Sealed Grok review](reviews/2026-11-09-thirring-two-particle-ir-grok/informe_grok.md)
of the text at 3500cbc (grok-4.7, herramientas 97292a9): «reparación necesaria».
No identity, series or limit found false. Accepted objections:

1. The verdict label overreached. With no bound branch in the window, the
   contract makes (R) rest on O2 and O4. O4 is open, so the verdict is now
   `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`.
2. Sec. 5 reintroduced the -2 omega0 branch as part of the answer. Removed.
3. The definition of E(p) was wrong. Corrected.
4. Gamma_1 Gamma_2 and the projector P of 1804.08508 coincide only on the
   physical lattice, not as fibre operators, and the "1/2" was not a
   demonstrated weight. Corrected.

Its point that leaving O4 OPEN is correct is recorded. The original text
is in git at 3500cbc.

Contract [THIRRING_TWO_PARTICLE_IR_PREFLIGHT_GATE.md](../theory/THIRRING_TWO_PARTICLE_IR_PREFLIGHT_GATE.md),
frozen at `6d24fb8` before any code; contract 1 of the 2-contract budget of
the Thirring coexistence line. Verifier committed before its first run at
`5c484d7`; four failed runs retained (Sec. 6); passing run at `68e1a55`.

## 1. Verdict

`OPEN_AFTER_BOUNDED_EXACT_ATTEMPT` (contract Sec. 5; repaired after review).

- O1 holds on all of F: the gate D survives at every mu.
- O2: c_f -> 1 and omega0/mu -> 1.
- O3: inside the frozen window ((+,+) near +2 omega0) there is no bound
  branch at chi = pi/2.
- O4: not decided, because the frozen definition does not separate doubler
  content from doubler transfer (Sec. 4).

By contract Sec. 5, with an empty window the relativistic property (R)
rests on O2 and O4. O4 being open, (R) is not decided.

A bound branch exists at the opposite edge -2 omega0, outside the frozen
window (Sec. 3.2-3.3). It does not enter the verdict or answer (R).

Scope: family F = {chi = pi/2, 0 < mu < 1}, two-fermion sector of the
carriers, rule only. Not composable universality, not an interacting
relativistic QFT limit, nothing outside the two-particle sector.

## 2. O1 and O2

- **O1.** Since J acts before F and the only same-site opposite-component
  pairs of the M=1 code are inputs 01 and 10, U B = F J B = F B D with
  D = diag(1,i,i,1) for every mu (certified for symbolic mu, rational
  parametrization mu = 2s/(1+s^2)). Property (G) holds along F.
- **O2.** omega(q) = acos(nu cos q): omega'(0) = 0, omega''(0) = nu/mu,
  omega^2 = omega0^2 + c_f^2 q^2 + O(q^4) with omega0 = acos(nu) = asin(mu),
  c_f^2 = omega0 nu / mu. Limits omega0/mu -> 1, c_f^2 -> 1. A free pair at
  total momentum P has threshold 2 omega(P/2) = 2 omega0 + omega''(0) P^2/4,
  so its squared threshold is (2 omega0)^2 + c_f^2 P^2 + O(P^4): same c_f.

## 3. O3: the bound branch

Conventions of `sources/1804.08508v1.pdf` (p.3-4): k is the half-relative
momentum, p the half-total momentum, P = 2p, v^s_q = (-i mu, g_s(q)),
g_s(q) = -i(s sin omega(q) + nu sin q). By 1804.08508 p.10 and 1711.03920
Lemma 2 (p.3), a proper eigenvector requires T_+ = 0 or T_- = 0 at complex
k = k_R + i k_I with k_I < 0; for (+,+) eigenphases, k_R is 0 or pi
(1711.03920 Lemma 1).

### 3.1 No bound state at the (+,+) threshold +2 omega0

At p = 0, k = i kappa, chi = pi/2, the numerator of T_+ is
(-i)(1-i)(S - nu sinh kappa), where S = sqrt(1 - nu^2 cosh^2 kappa) >= 0
(certified). It vanishes only if sinh kappa = S/nu >= 0, i.e. k_I >= 0. That
solution is not normalizable. Small p != 0: Lemma 2 gives exactly one bound
state per p (e^{2ip} != i). At p = 0, 1804.08508 p.13 gives the point
spectrum {e^{-2i omega(k~)}, 1}. The bound state identified in 3.2 is
therefore the only one, and it is not at +2 omega0. By continuity in p,
the window has no bound branch near P = 0.

### 3.2 The bound branch at k_R = pi

With g_+(x ± pi) = -g_-(x), the T_+ = 0 condition at k = pi + i kappa
becomes X(p + i kappa) = i conj(X(p + i kappa)), with
X(z) = sin omega(z) - nu sin z. Equivalently Re X = Im X, a single real
equation. At p = 0 it gives sin omega(i kappa) = -nu sinh kappa, hence
cosh 2 kappa = 1/nu^2 with kappa < 0 (normalizable). The eigenphase is
e^{i M_b} with

  cos M_b = nu^2,   M_b = 2 asin(mu/sqrt2),   M_b < 2 omega0.

The eigenvector (1804.08508 Eq.(19), y >= 0, restricted to the
opposite-Gamma pattern) is f_j(y) = 2 u_j lambda^y, with
u = v^{++}_{pi + i kappa} ∝ (1, (1-i)/sqrt2, (1+i)/sqrt2, 1),
lambda = -t, t = e^kappa = (sqrt(2-mu^2) - mu)/(sqrt2 nu) in (0,1), the
factor e^{-i chi} on the up-down component at y = 0, and antisymmetric
extension to y < 0. Certified as a pointwise lattice eigenvector of U = FJ
with eigenvalue (1-mu^2) + i mu sqrt(2-mu^2) at mu = 3/5 and mu = 5/13, on
every target with |x1|, |x2| <= 5.

This covers all sites. For |y| >= 3 every equation involves only y' with
|y'| >= 1 on the same side. The equations there are lambda^y times a fixed
pattern of period 2 in y, so y = 3, 4 settle all of them. y in {0, 1, 2} is
checked directly. y < 0 follows from exchange symmetry, and all w from
translation invariance (p = 0). This argument is written here, not certified.

### 3.3 Curvature and limits

Implicit differentiation of Re X = Im X at p = 0 (z0 = i kappa0, all
quantities exact):

- omega'(z0) = -i and omega''(z0) = 2 sqrt2 C0/mu, with
  C0 = cos omega(z0) = sqrt((1+nu^2)/2);
- kappa''(0) = -F_pp/F_kappa;
- E''(0) = 2 sqrt2 nu^2/(C0 mu), where E(p) = 2 Re omega(p + i kappa(p)) is
  the modulus of the quasienergy, phi = -E, counted from the same zero as
  +2 omega0. Its distance to the -2 omega0 edge is 2 omega0 - E.

Hence

  omega_b^2 = M_b^2 + c_b^2 P^2 + O(P^4),   c_b^2 = M_b nu^2 / (sqrt2 C0 mu).

Limits as mu -> 0: M_b/mu -> sqrt2, c_b^2 -> 1, and
c_b^2 - c_f^2 = -mu^2/3 + O(mu^4). At mu = 3/5: c_b^2 = 0.72989, while
c_f^2 = 0.85800. A floating-point finite difference, labelled illustration,
gives 0.7298921 against the closed form 0.7298921.

Which threshold carries the bound branch depends on the sign of chi.
Complex conjugation maps W(q) to sigma_z W(-q) sigma_z and J(chi) to
J(-chi). So at chi = -pi/2 the same branch, with the same M_b and c_b,
would sit at +2 omega0. This is a written remark, not certified. The
infinite-dimensional eigenvalue-1 space at p = 0 (the (+,-) states, of
quasienergy 0; 1804.08508 p.13) is a single fibre and lies outside the
window.

The limit (R) is established at the level of the rest mass and the P^2
coefficient. The full scaling function omega_b(mu Q)/mu was not computed.

## 4. O4: why it stays OPEN

- Gamma = sigma_z (-1)^x anticommutes with W (certified on the lattice). So
  Gamma_1 Gamma_2 = sigma_z sigma_z (-1)^{x1+x2} commutes with W ⊗ W.
- On the physical lattice (y ≡ w mod 2), the eigenspace Gamma_1 Gamma_2 = -1
  coincides with the component-dependent parity mask of the projector P of
  1804.08508 Eq.(8). As fibre operators in the paper's doubled (y, w)
  representation the two differ: Gamma_1 Gamma_2 carries (-1)^w and shifts
  p by pi, while P fixes the parity of y and conserves p (review objection 3).
- Eq.(18) gives equal coefficients to v^{++}_k and v^{--}_{k-pi}, also
  without interaction. I had called this a weight 1/2; that is not
  demonstrated as an L^2 weight of a wave packet.
- Within P, the scattering eigenvectors of Eq.(18) map P(+,+;k) to
  T_+ P(+,+;-k). For fermions this is a phase on the same momentum pair.
  This is a written argument; no wave-packet proof.
- At low energy, g_+(mu Q)/(-i mu) -> sqrt(1+Q^2) + Q = e^{theta}, with
  rapidity theta = asinh Q (certified). Hence
  T_+ -> (e^{Delta/2} + e^{-i chi} e^{-Delta/2}) / (e^{-Delta/2} + e^{-i chi} e^{Delta/2}),
  which depends only on the rapidity difference Delta. This is a statement
  about real-momentum scattering, not a doubler weight.

The frozen O4 asks for "the outgoing weight carried by the doubler
components", defined by a wave-packet analysis to be stated in the report
before evaluation. Read literally as content, the doubler component is nonzero and present in
the incoming state as well. Read as transfer, the written argument gives
zero. Choosing the reading after having
derived both would be a post-hoc definition. O4 is therefore recorded as not
decided, and the contract wording is flagged as defective.

## 5. What this means for the coexistence question

- Along F, the T=1 gate holds at every point, on lattice-scale states of
  the M=1 code. No statement that it acts on low-energy states.
- Free particles have c_f -> 1.
- The relativistic property (R) of the two-particle sector is not decided:
  the window has no bound branch and O4 is open.
- The -2 omega0 bound branch (M_b/mu -> sqrt2, c_b -> 1 at the level of the
  P^2 coefficient) is outside the frozen window and is not part of (R).
- Open: O4 and its definition, the full scaling function, composable gates,
  many-body behaviour, and gates acting on low-energy states.

Budget: this was contract 1 of 2, closed OPEN; one contract remains
(decision of 2026-11-09).

## 6. Verifier and failed runs

[Script](../scripts/verify_thirring_two_particle_ir.py),
[record](2026-11-09--thirring-two-particle-ir.txt),
[JSON](2026-11-09--thirring-two-particle-ir.json),
[illustration](2026-11-09--thirring-two-particle-ir-illustration.txt):
**34/34 exact checks** (SymPy 1.14.0). Floating point appears only in the
labelled illustration.

Four failed runs are retained, all tool or check-construction errors. No
expectation was changed.

| Run | Commit | Outcome | Cause | Record |
| --- | --- | --- | --- | --- |
| 1 | `5c484d7` | 900 s timeout | radicals with unbounded mu | `-failed-run-1.txt` |
| 2 | `0f81ea6` | SymPy `NotImplementedError` | series of acos near 1 | `-failed-run-2.txt` |
| 3 | `0a48dbd` | the same error | series on the raw expression | `-failed-run-3.txt` |
| 4 | `9510d54` | 29/32 | dependent-basis eigenvector test; double-angle identity not recognised | `-failed-run-4*` |

In run 4, a floating-point inspection showed the eigenvector equation
holding to about 1e-16 before the test was corrected.

Not certified: the uniqueness and continuity argument of 3.1 (from the
sources), the bulk-recurrence extension of 3.2, the chi -> -chi remark, and
everything in Sec. 4 except the two certified identities.
