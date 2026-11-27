# Turning-point asymptotic law for the dispersive horizon — conjecture note

2026-11-27. Author: Claude Code (Claude Opus 5.5), at the user's request
(«enuncia la ley que crees deberíamos demostrar»; «redáctala como nota en
theory/»). Branch `research/dispersive-horizon-channels`.

**Status: CONJECTURE (`OPEN`). Not a charter, not a result.**
- Nothing here authorizes a computation or changes any verdict.
- It is `POST_RESULTS`: it was formulated after the turning-branch results
  and the reading of De Beule et al.
- The formula is prior art (De Beule et al., Sabsovich et al.).
- NOVELTY = OPEN.
- **[A1] Amendment 1 (2026-11-27).** The statement in §3 is repaired after
  Astra 6.2 (web): `reports/2026-11-27--turning-point-conjecture-astra-web-review.md`.
  - φ′(0) > 0 is required, since tanh(s³)/16 met the old hypotheses with
    κ = 0.
  - (C1)–(C3) are written as S-matrix entries, and (C3) excepts both
    channels e and u, removing an internal contradiction with (C1).
  - (C4) is restricted to universality in φ, since γ_h is fixed by the walk.
  - Existence of S for large L is made part of the conjecture.
  - The original statement is kept below as superseded.

## 1. Why a limit law, and not an identity

- The identity T_ret = X(ω, L) = 1/(1 + e^{4πωL}) is **false**, and this is
  certified. At (s, L) = (1/50, 4), T_ret/X = 1.1114, with T_ret certified at
  width 10⁻²⁰.
  - Turning-branch report.
  - `reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt`.
  - The ratio is reproduced in
    `reports/2026-11-27--dispersive-horizon-heuristic-prediction-harness-test.txt`.
- No finite set of computed points establishes a law (CLAUDE.md, hard rules).
  The certified enclosures prove statements at individual points only.
- So the only candidate for a provable law is an asymptotic statement, in a
  declared limit.

## 2. Ingredients (with sources)

- **Model.** The QCA U = L₋W² with local coin parameter t(x), as in
  `theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md`.
- **Dispersion** (reviewed check C2, `scripts/verify_dispersive_horizon_channels.py`
  lines 210–213):

  2f(k)² − 1 = cos(ω + k),  f(k) = A cos 3k + (1 − A) cos k,  A = t(2t − 1),

  with λ = e^{−ik} and z = e^{iω}.
- **Low-k sheet** (checked: `scripts/check_dispersive_horizon_low_k_sheet.py`,
  output `reports/2026-11-27--dispersive-horizon-low-k-sheet-check.txt`,
  commit `9e8cb5a`; exact series plus an independent numerical route):

  ω = v(t)·k + γ(t)·k³ + O(k⁵),  v(t) = 8t − 3,
  γ(t) = 16t(t − 1)(2t − 1)(2t + 1) / (3(4t − 1)).

  - γ(5/16) = 715/256, γ(3/8) = 35/32 and γ(7/16) = 105/256. γ > 0 on
    [5/16, 7/16].
  - The horizon is t_h = 3/8, where v = 0. Since γ > 0, the turning point
    (dω/dk = 0) lies where v < 0, on the interior side.
- **Prior art for the formula** (read in the original:
  `investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`,
  third batch). De Beule, Groenendijk, Meng, Schmidt, arXiv:2106.14595v4.
  - Continuum model, continuous time; linear horizon V = 1 + αz (p. 9).
  - The leading-order result is
    T_{u←w₁,₂} = R_{u←w₂,₁} = 1/(1 + e^{±2πω/α}) (Eq. (55), p. 12).
  - Its stated assumptions are α, |ω| ≪ 1 and |αz| ≪ 1 (Eq. (41)), and
    first order in V′ (p. 8).
  - Here α is the horizon slope of the low-k group velocity (Eq. (11),
    p. 5; Eq. (64), p. 13).
  - Sabsovich et al., arXiv:2106.14553, find the same form numerically on a
    lattice (pp. 3–4).

## 3. Statement

### 3.1 [A1] Repaired statement (current)

**Admissible profiles.**
- φ ∈ C^∞(ℝ) is strictly increasing, with φ(0) = 0 and **φ′(0) > 0**.
- φ tends to ±1/16 with exponentially small error at the respective ends.
- κ = 8φ′(0) > 0.
- The full profile on ℤ is t_L(x) = 3/8 + φ(x/L), with no truncation.
- Uniformity in μ is required for each fixed φ.

**Scattering matrix.** At quasi-energy ω, S_L(ω) is taken between the
asymptotic media t₋ = 5/16 and t₊ = 7/16. "Defined" means two things:
- every incidence admits a physical solution with no growing evanescent
  component at either end;
- its outgoing propagating amplitudes are uniquely determined, possibly
  modulo a localized state.

**Channels**, in unit-flux bases; S_{b,a} has outgoing b and incoming a:
- r: the incoming interior channel with positive velocity and
  −π/2 < k_r < 0 (the turning branch);
- c: the same, with 0 < k_c < π/2 (the continuing branch);
- e: the outgoing exterior channel of the low-k sheet that reaches k = 0 as
  ω ↓ 0;
- u: the outgoing interior channel of that same sheet that reaches k = 0.

**Conjecture (C), [A1].** For every nonempty compact K ⊂ (0, ∞) there is
L₀(φ, K) such that, for all L ≥ L₀ and μ ∈ K:
- at ω = μ/L the channels above and S_L(ω) are defined;
- with X_φ(μ) = 1/(1 + e^{2πμ/κ}), the following limits hold as L → ∞,
  uniformly on K:

| | Conjectured limit |
| --- | --- |
| (C1) | \|S_{e,r}\|² → X_φ(μ) |
| (C2) | \|S_{e,c}\|² → 1 − X_φ(μ) |
| (C3) | \|S_{u,r}\|² → 1 − X_φ(μ), and Σ_{b ∉ {e, u}} \|S_{b,r}\|² → 0 (sum over outgoing propagating channels) |
| (C4) | Two admissible profiles with the same φ′(0) have the same limits (C1)–(C3) |

Remarks:
- If flux unitarity is established (step 1 of §5), the second half of (C3)
  follows from (C1) and the first half.
- **Scope of (C4).** All admissible profiles cross t_h = 3/8 under the same
  rule, so γ_h = γ(3/8) = 35/32 is fixed. (C4) tests universality in φ only.
  - Whether γ_h cancels from the leading-order connection coefficient is a
    question for the inner problem (§5, step 3).
  - A law comparing walks with different γ_h would require declaring the
    family compared.
- For φ = tanh/16 (κ = 1/2), (C1) reads |S_{e,r}|² → 1/(1 + e^{4πωL}) at
  fixed ωL: the heuristic of the turning-branch charter, as a limit.
- No rate of convergence is conjectured.

### 3.2 Original statement (superseded by [A1]; kept for the record)

**Admissible profiles.** t_L(x) = 3/8 + φ(x/L), where φ: ℝ → ℝ:
- is smooth and strictly increasing, with φ(0) = 0;
- has φ(x) → ±1/16 exponentially fast as x → ±∞;
- defines κ = 8φ′(0), the horizon slope of v(t_L(x)) in units of 1/L.
  [A1: defect — κ = 0 was admitted, for example by tanh(s³)/16.]

The profile of the turning-branch charter, φ(y) = tanh(y)/16, has κ = 1/2. It
is truncated at |x| ≤ N = 8L in the computations, which is not covered by
this smooth class (see §6).

**Observables.** At quasi-energy ω, with unit-flux incidence:
- T_ret: from the interior right-mover with −π/2 < k < 0 (the turning
  branch) into the exterior right-mover;
- T_cont: the same, from the interior right-mover with 0 < k < π/2;
- R_u: from the turning branch into the interior left-mover of the low-k
  sheet.

These are the observables of `theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md`,
for the profile t_L.

**Conjecture (C).** Fix μ > 0 and set ω = μ/L. As L → ∞, uniformly for μ in
compact subsets of (0, ∞):

- **(C1)** T_ret(μ/L, L) → X(μ) = 1/(1 + e^{2πμ/κ}).
- **(C2)** T_cont(μ/L, L) → 1 − X(μ), so σ² = T_ret + T_cont → 1.
- **(C3)** R_u(μ/L, L) → 1 − X(μ). Every other entry of the turning-branch
  column of |S|² tends to 0, including the channels with |k| ≈ 2.
  [A1: defect — "every other entry" includes T_ret, which contradicts (C1).]
- **(C4) Universality.** The limits depend on φ only through φ′(0), and they
  do not depend on γ(t_h).
  [A1: defect — γ_h is fixed by the walk, so the second clause is
  ill-posed.]

For φ = tanh/16, (C1) reads T_ret → 1/(1 + e^{4πωL}) at fixed ωL: the
heuristic of the turning-branch charter, as a limit.

No rate of convergence is conjectured.

## 4. Heuristic derivation of the scaling (not a proof)

- **Turning point inside the linear zone.** The local velocity is
  v(x) ≈ κx/L near x = 0. On the sheet ω = vk + γk³, the turning point is
  where v = −3γk². This gives |x_c| ~ L·|ω|^{2/3}, which is L^{1/3} when
  ω = μ/L.
  - So |x_c|/L → 0: the turning point sits in the linear part of the
    profile. This is De Beule's α z_c ≪ 1, which fails at fixed ω.
  - The computed points (s = 1/40, 1/50 at L ≤ 16) are far from this
    regime. A hand estimate, not certified, puts the local velocity at the
    turning point at ≈ 0.3 of the asymptotic 0.5 for s = 1/40.
- **Inner scaling.** With x = L^{1/3}y and k = L^{−1/3}q, the sheet becomes,
  at leading order,

  κ y q + γ_h q³ = μ,  with γ_h = γ(3/8) = 35/32.

  The lattice disappears: this is a continuum problem, third order in
  d/dy, with three local roots in q.
  - For y → −∞ (interior) the three roots are real:
    q ≈ −√(κ|y|/γ_h), q ≈ +√(κ|y|/γ_h) and q ≈ μ/(κy).
  - For y → +∞ (exterior) there is one real root, q ≈ μ/(κy); the other two
    are complex.
- **Mode matching.** The three interior roots are, respectively, the turning
  branch, the continuing branch and the low-k left-mover. This is the
  structure of w₁, w₂ and u in De Beule et al.
  - Hand check at s = 1/50 with t = 5/16, not certified: the root of
    −k/2 + γ(5/16)k³ = ω near zero is k ≈ −0.083. This matches the
    reflected low-k mode of the turning-branch report.
  - The two other roots match only qualitatively (≈ ±0.42 against −0.476
    and +0.596): the cubic truncation is not valid at |k| ~ 0.5 in the
    asymptotic medium.
- **Where e^{2πμ/κ} would come from.** The connection coefficients of the
  inner third-order problem across y = 0, as in De Beule's hypergeometric
  solution. [A1] Whether γ_h drops out of the leading-order connection
  coefficient is a question for this inner problem; it is no longer part of
  (C4).

## 5. Possible proof route (sketch; no guarantee)

1. **Existence of the S matrix** for smooth multi-step profiles with
   distinct asymptotic media. Richard–Suzuki–Tiedra (arXiv:1801.02779,
   Thm 3.3) cover one-step U = SC. The extension to U = L₋W² is
   `[UNVERIFIED]`.
   - [A1] Under the repaired statement, this is the first open obligation.
     It requires S_L(μ/L) and the channel labels r, c, e, u to exist for
     the full profile, for all L ≥ L₀ and μ ∈ K.
   - The channels charter excluded existence and uniqueness of S for the
     tanh profile from every verdict
     (`theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md:194`).
2. **Outer region** (|x| ≫ L^{1/3}). An adiabatic or discrete-WKB theorem
   for the 12 × 12 transfer matrix:
   - the low-k-sheet modes are transported with O(1/L)-type errors;
   - the other sheet, the |k| ≈ 2 channels and the evanescent modes
     decouple, since they are separated in k by O(1).
3. **Inner region.** Exact solution of the third-order continuum problem
   (Laplace or Airy-type integral) and its connection coefficients.
   Classical antecedents are likely and have not been checked
   (`[UNVERIFIED]`).
4. **Matching** of the two regions, with error control, in the
   intermediate zone L^{1/3} ≪ |x| ≪ L.

Steps 2 and 4, done rigorously for a discrete-time QCA, are the hard part.
Lean formalization is not a realistic first target: it needs a proof on paper
first. Mathlib support for discrete WKB and turning-point asymptotics is
`[UNVERIFIED]` and probably absent.

## 6. Status of the evidence (orientation only)

| Item | Data | Bearing |
| --- | --- | --- |
| (C1) at μ ≈ 0.16 | T_ret/X = 1.111 (L = 4), 1.0076 (L = 16) | Compatible with convergence. Two points; the rate is not identified. |
| (C2) | σ² = 0.99945 (s = 1/50, L = 16), 0.98719 (s = 1/200, L = 16) | Compatible with σ² → 1 |
| (C3) | Reflection into the low-k left-mover 0.99681 and 0.86756 at L = 16; \|k\| ≈ 2 channels ~10⁻¹⁶ | Compatible |
| (C4) | No second profile computed | Untested. This is the cheapest falsification route. |

Caveats on these data:
- They come from the truncated profile (N = 8L), at fixed s rather than at
  fixed μ as L grows.
- The heuristic-prediction charter (`35bf83f`) tests X at four new points,
  at fixed ω, not in this limit. Its outcome is neither proof nor disproof
  of (C).

## 7. What would falsify (C), cheaply

- **(C4):** two admissible profiles with the same φ′(0) = 1/16 and the same
  asymptotes ±1/16, for example φ = tanh(y)/16 and φ = erf(√π y/2)/16.
  - An arctan profile has the same φ′(0) but approaches its asymptotes
    algebraically, so it lies outside the class of §3.
  - If T_ret differs between the two at large L and fixed μ, beyond what
    the trend in L allows, (C) fails as stated.
- **(C1):** at fixed μ, a sequence L = 8, 16, 32 whose ρ = T_ret/X moves
  away from 1.

Either test needs a new charter.

## 8. Not claimed

- That (C) is true, or that it is new.
- Any Hawking, thermal or physical-horizon statement. X is a mode-conversion
  probability with a Fermi–Dirac form.
- Anything about the untruncated profile, beyond the conjecture itself.
