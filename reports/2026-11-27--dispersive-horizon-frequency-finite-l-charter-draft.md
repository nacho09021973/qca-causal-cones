# Dispersive-horizon frequency and finite-L gate — DRAFT

2026-11-27. Author: Claude Code (Claude Opus 5.5). **DRAFT, not frozen.** It
is frozen only by a later commit, as `theory/DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md`, after the user answers the questions at the
end. Initial status after freezing: **OPEN**.

## Authorization and budget

- **Drafting.** Task 3 of `reports/2026-11-27--work-plan.md`, under the user
  instruction «continúa con la hoja de ruta» (2026-11-27). The plan states
  that this is a draft only and that the user decides before freezing.
- **Not authorized:** freezing, execution, review, promotion. Each needs a
  separate user decision.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically.
- **Dependency.** The transmission execution
  (`reports/2026-11-26--dispersive-horizon-transmission.md`) is under Astra 6.2
  review (`reports/reviews/2026-11-27-dispersive-horizon-transmission-astra/`).
  This charter should not be frozen before that review is recorded. If the
  review requires repairs to the method (Krawczyk, matching, normalization),
  the method sections below are revised first.

## Known, question, abandonment

**Known** (with source; status as of the draft):

- Channels on I = (arg z_c*, π/2) and below the threshold arc, with flux form
  G_x and unit-flux normalization: `reports/2026-11-26--dispersive-horizon-channels.md`
  with Amendment 1, Astra 6.2 PASS. arg z_c* ≈ 0.0894 (orientation; z_c* is
  certified in a rational box there).
- Sharp profile 5/16 | 3/8 | 7/16, author PRELIMINARY, review pending
  (`reports/2026-11-26--dispersive-horizon-transmission.md`):
  - z₀ = (3+4i)/5: T ∈ [0.995719…, 0.995719…], T0 = CONNECTED (adiabatic
    continuity of a high-k branch);
  - z₁ = (2499+100i)/2501: σ² ∈ [0.960541…, 0.960541…], the two interior
    right-moving doublers feeding the exterior low-k right-mover.
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
  - Product of 2N + 1 transfer matrices. The evanescent modes grow
    exponentially across the window, so the method must control the
    conditioning (Q4).
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

## Questions for the user (to answer before freezing)

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
