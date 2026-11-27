# Dispersive-horizon frequency and finite-L gate

2026-11-27. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Frozen by the commit that moves this file here from
`reports/2026-11-27--dispersive-horizon-frequency-finite-l-charter-draft.md`
(draft committed at `f5a68d3`), on branch
`research/dispersive-horizon-channels`, before any execution.

## Authorization and budget

- **Drafting.** Task 3 of `reports/2026-11-27--work-plan.md`, under the user
  instruction «continúa con la hoja de ruta» (2026-11-27).
- **Freezing.** User decisions, 2026-11-27: «Q1 b, Q2 y Q3 como propones,
  Q4 a, Q5 Astra 6.2». See "User decisions" below.
- **Not authorized:** execution and promotion. Each needs a separate user
  decision. The review model is fixed (Q5), but sending still needs the
  user's go-ahead.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically.
- **Dependency, resolved.** The Astra 6.2 review of the transmission execution
  is recorded (`reports/2026-11-27--dispersive-horizon-transmission-astra-review.md`).
  Points 1–5 (Krawczyk, matching, normalization, unitarity) are PASS, so the
  method below is unchanged. The repairs concerned interpretation only. The
  F2/F3 reports must use the repaired reading: σ² is the *maximal*
  transmission over unit-flux interior superpositions, and "doublers" is an
  interpretation.

## Known, question, abandonment

**Known** (with source; status at freezing):

- Channels on I = (arg z_c*, π/2) and below the threshold arc, with flux form
  G_x and unit-flux normalization: `reports/2026-11-26--dispersive-horizon-channels.md`
  with Amendment 1, Astra 6.2 PASS. arg z_c* ≈ 0.0894 (orientation; z_c* is
  certified in a rational box there).
- Sharp profile 5/16 | 3/8 | 7/16 (`reports/2026-11-26--dispersive-horizon-transmission.md`;
  Astra 6.2: certified numbers PASS, interpretation repaired in editorial
  Amendment 1, not re-reviewed, not promoted):
  - z₀ = (3+4i)/5: T ∈ [0.995719…, 0.995719…], T0 = CONNECTED (adiabatic
    continuity of a high-k branch);
  - z₁ = (2499+100i)/2501: σ² ∈ [0.960541…, 0.960541…], the maximal
    transmission from a unit-flux superposition of the two interior
    right-movers into the exterior right-mover on the low-k sheet.
- Low-k velocity (author remark, transmission charter):
  v(k → 0) = −1 + 2(4t − 1), zero at t = 3/8.
- Prior art, checked in the originals
  (`investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`):
  Sabsovich et al. 2106.14553 report a doubler-mixing probability
  1/(1 + e^{2πω/α}) for a smooth lattice horizon; Maertens–Bultinck–Van
  Acoleyen 2204.06583 report partial transmission and leakage.

**Author heuristic, not computed, `[UNVERIFIED]`.** If the Sabsovich form
applied here with α = |dv/dx| at the horizon, then for t_L(x) = 3/8 +
tanh(x/L)/16 one gets α = 8 t_L′(0) = 1/(2L) and an exponent 2πω/α = 4πωL.
At ω = arg z₁ ≈ 0.04 this is ≈ 0.5 L, so mixing would be ≈ 0.12 at L = 4 and
≈ 3·10⁻⁴ at L = 16. The identification of their mixing probability with σ²
here, and of α with this derivative, is not established. It is written down
only so that the result can contradict it.

**Question.** For this rule:
1. In (t, ω), where exactly is the incident interior right-mover connected
   to the exterior right-mover without a turning point (the CONNECTED
   regime), and where is the horizon arc?
2. For the sharp profile, how do T(ω) and σ²(ω) behave at a few exact points
   in each regime? Is there a visible separation between a high-energy
   regime (CONNECTED, T ≈ 1) and a low-energy one (doubler leakage)? This is
   the user's "two regimes" idea of 2026-11-26.
3. For truncated tanh profiles at one or two finite L, is the low-energy
   leakage σ² smaller than in the sharp limit, and does it decrease from the
   smaller to the larger L?

**Abandonment of the line.** If σ² at the horizon-arc points stays O(1)
(declared threshold: σ² ≥ 1/2 at every horizon-arc point, at the largest L
computed), the "horizon" of this rule is not a barrier in any computed
regime. That closes the "escape across the horizon" question negatively for
this rule and profile family, as a first-class result. The converse
(suppression at two L values) does not establish an exponential law.

## Tasks

- **F1. Regime boundary (exact).** With A = t(2t − 1) and z = e^{iω}:
  - the discriminant in τ = tan(k/2) of H_{A,ω}, as an exact curve in (A, ω)
    (or in (A, s) with z = (1 − s² + 2is)/(1 + s²), which keeps everything
    rational);
  - its intersection with the strip A ∈ [A(5/16), A(7/16)] = [−15/128, −7/128];
  - output: the set of s for which some intermediate medium has a critical
    value or collision at z, as a finite union of intervals with exact
    (algebraic) endpoints. Inside its complement the T0 argument gives
    CONNECTED.
- **F2. Sharp profile, frequency scan.** T(s) on I and σ²(s) on the horizon
  arc, at predeclared exact points (Q2). Same method as the transmission
  verifier: Krawczyk roots, flux normalization, verified matching solve,
  S^H S ∋ I. Each point is regular (certified), or it is reported as
  `S_MATRIX_NOT_ESTABLISHED` and not replaced.
- **F3. Finite L, truncated profile.** t(x) = t_L(x) for |x| ≤ N and the
  asymptotic values 5/16, 7/16 beyond, at the L and N of Q3, at z₁ and one
  more horizon-arc point.
  - The intermediate t_L(x) are irrational. Coins at those sites enter as
    rational interval enclosures of cos θ, sin θ; the asymptotic media remain
    exact rationals, so roots and modes are those already certified.
  - Points: z₁ (s = 1/50) and s = 1/200. [Fixed at freezing: the draft
    said "z₁ and one more horizon-arc point" without naming it. s = 1/200
    is the lowest-energy point of Q2. There the author heuristic predicts
    the weakest suppression, about 0.12 at L = 16, so it separates the
    outcomes best.]
  - N = 32 for L = 4 and N = 128 for L = 16, giving 65 and 257 transfer
    matrices.
  - **Method (Q4 = a).** Interval product of the transfer matrices
    M_N ⋯ M_{−N−1}, applied to the certified asymptotic mode vectors.
    - Rational interval arithmetic. After each matrix product the endpoints
      are rounded outward to the dyadic grid 2⁻ᵖ.
    - Predeclared precision: p = 256 + 2(2N + 1)⌈log₂ κ⌉, where κ is the
      upper bound, over the certified root boxes of both media at that z,
      of max(|λ|, 1/|λ|).
    - Enclosures of tanh(x/L) and of cos θ = √t, sin θ = √(1 − t) at the
      same p: mpmath `iv` (outward rounding), converted to rationals
      outward. Square roots by integer square root, as in the reviewed
      verifiers.
    - Matching, solve, S^H S ∋ I and σ² as in F2.
  - **Fallback.** If any certified enclosure of T or σ² is wider than 10⁻⁶,
    or the matching matrix cannot be certified invertible, that point is
    reported `OPEN_AFTER_TRANSMISSION_ANALYSIS`. Switching to method (b)
    (Redheffer composition) then needs a written amendment and user
    authorization. The precision is not tuned after seeing results.
  - Results are stated for the truncated profile at that N. No statement on
    the untruncated tanh unless a tail bound is in scope (Q3).

## Admission criteria

- Exact algebra, or rational interval arithmetic, for every certified number.
  Floating point only for guesses and preconditioners, labelled as such.
- A permanent verifier in `scripts/`, committed before its recorded run.
  Failed and interrupted runs are retained. The reviewed verifiers are
  imported read-only with SHA256 checks. Krawczyk replaces root isolation.
- Every claim at a named profile, L, N and z. No extrapolation in L or z
  without proof. No fitted curve through the computed points.

## Verdicts

- F1: `REGIME_BOUNDARY_CERTIFIED` (exact intervals), or
  `OPEN_AFTER_DISCRIMINANT_ANALYSIS`.
- F2, F3, per (profile, L, N, z): `TRANSMISSION_NONZERO_CERTIFIED` with the
  enclosure, `TRANSMISSION_ZERO_PROVED`, `S_MATRIX_NOT_ESTABLISHED`, or
  `OPEN_AFTER_TRANSMISSION_ANALYSIS` (as in the transmission charter).
- Line level, on closure:
  - `LEAKAGE_SUPPRESSED_AT_COMPUTED_L`: σ² at the largest L is below the
    sharp value and decreases from the smaller L to the larger at every
    computed horizon-arc point;
  - `LEAKAGE_NOT_SUPPRESSED`: the abandonment threshold above is met;
  - `MIXED`: otherwise, stated point by point.

## Not claimed (in any case)

- An exponential (or any functional) law in L or ω from finitely many points.
- Anything about the untruncated tanh profile without a tail bound.
- A Hawking, thermal or physical-horizon statement.
- Novelty (OPEN).

## User decisions (2026-11-27)

«Q1 b, Q2 y Q3 como propones, Q4 a, Q5 Astra 6.2»:
- **Q1 = (b):** F1 + F2 + F3.
- **Q2:** on I, s = 1/4, 1/2, 3/4; on the horizon arc, s = 1/200, 1/50,
  1/30. Each point is certified regular in both media or reported
  `S_MATRIX_NOT_ESTABLISHED`, and not replaced.
- **Q3:** L = 4 and L = 16, N = 8L, no tail bound. Results are stated for
  the truncated profile.
- **Q4 = (a):** interval transfer-matrix product with the predeclared
  precision of F3. Fallback to (b) only by amendment.
- **Q5:** independent review by Astra 6.2 (`gpt-6.2-astra`).

## Original questions as posed

- **Q1. Scope.** (a) F1 + F2 only (exact, sharp profile; no new
  conditioning risk). (b) F1 + F2 + F3. Recommendation: (b), because F3 is
  the only part that bears on whether the horizon suppresses leakage; (a) is
  a fallback if F3's runtime or conditioning is unacceptable.
- **Q2. Points.** With z = (1 − s² + 2is)/(1 + s²) (z₀ is s = 1/2, z₁ is
  s = 1/50; arg z_c* ≈ 0.0894 corresponds to s ≈ 0.0447):
  - on I: s = 1/4, 1/2, 3/4;
  - on the horizon arc: s = 1/200, 1/50, 1/30.
  Proposal; each must be certified regular in both media.
- **Q3. Finite L.** L = 4 and L = 16, truncation N = 8L (tail jump about
  2e⁻¹⁶/16 ≈ 10⁻⁸ in t). Rigorous tail bound: no (results stated for the
  truncated profile). Recommendation: as proposed.
- **Q4. Method for F3.** (a) Interval transfer-matrix product at high
  precision (simple; conditioning grows like the evanescent ratio to the
  power 2N). (b) Layer-by-layer composition of scattering matrices
  (Redheffer star product), which avoids exponential growth but needs mode
  splitting at each intermediate t. Recommendation: (a) with precision
  chosen from a predeclared rule, falling back to (b) by a new amendment if
  the enclosure width exceeds 10⁻⁶.
- **Q5. Review** after execution: model(s).
