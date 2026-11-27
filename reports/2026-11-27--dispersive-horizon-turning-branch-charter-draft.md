# Dispersive-horizon turning-branch transmission gate — DRAFT (POST_RESULTS_EXPLORATORY)

2026-11-27. Author: Claude Code (Claude Opus 5.5). **DRAFT, not frozen.**

- It is kept in `reports/` so that committing it does not freeze it. It is
  frozen by a later commit, as
  `theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md`, after the user answers
  the questions at the end. Initial status after freezing: **OPEN**.
- **Label: `POST_RESULTS_EXPLORATORY`.** The question was formulated after
  seeing the frequency/finite-L results and their review. Nothing in it can
  retroactively change the verdicts of that charter.

## Authorization and budget

- **Drafting.** User decision, 2026-11-27: «mi decisión es SÍ a las dos
  propuestas … autorizo, como siguiente paso de investigación, preparar el
  nuevo contrato exploratorio».
- **Not authorized:** freezing, execution, review sending and promotion.
  Each needs a separate user decision.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically.

## Known, question, abandonment

**Known** (with source):

- **Frequency/finite-L charter, closed.**
  - Report `reports/2026-11-27--dispersive-horizon-frequency-finite-l.md`,
    with Amendments 1 and 2; Astra 6.2 REPAIR_REQUIRED.
  - `LEAKAGE_NOT_SUPPRESSED` adopted for σ² at s = 1/50 and 1/200,
    L = 16, N = 128 (user decision).
  - σ² values:

    | s | sharp | L = 4 | L = 16 |
    | --- | --- | --- | --- |
    | 1/50 | 0.96054 | 0.97545 | 0.99945 |
    | 1/200 | 0.95918 | 0.96466 | 0.98719 |
- **Sector argument** (Astra, written; checked against logged boxes, not
  machine-checked).
  - At the arc frequencies no real root changes k-quadrant as t varies over
    [5/16, 7/16].
  - The interior right-mover with 0 < k < π/2 continues into the exterior
    right-mover.
  - The interior right-mover with −π/2 < k < 0 meets a fold (turning point)
    in some intermediate medium.
- **Turning branch, sharp profile, z₁.**
  - In the reviewed transmission verifier, the incident columns follow the
    printing order of the right-movers (author check).
  - The k ≈ −0.476 branch transmits |t₂|² ≈ 0.35726 into the exterior
    right-mover; the continuing k ≈ +0.596 branch transmits ≈ 0.60328.
  - These are reviewed enclosures; the branch attribution is the author's
    reading of the code.
- **σ² = T_ret + T_cont.** σ² is the maximal transmission over unit-flux
  interior superpositions, and it equals the sum of the two column weights
  (transmission report, Amendment 1).

**Author heuristic, not computed, `[UNVERIFIED]`.** If the Sabsovich mixing
1/(1 + e^{2πω/α}), with α = 1/(2L), described T_ret, one would get:
- ≈ 0.12 at s = 1/200, L = 16;
- ≈ 3·10⁻⁴ at s = 1/50, L = 16.

That identification is not established. The heuristic is written down only
so that the result can contradict it, and no verdict depends on it.

**Question.** For the incident interior right-mover in the sector
−π/2 < k < 0, which meets the turning point, what is its transmission into
the exterior right-mover,

  T_ret(s, profile) = |S_{ext R, int R(k<0)}|²,

with unit-flux incidence and all other incoming amplitudes zero? Does it
decrease from the sharp profile to L = 4 and to L = 16 while σ² increases?

**Abandonment of the line.** If T_ret does **not** decrease, that is
T_ret(L = 16) ≥ T_ret(sharp) at both points, the rule's turning point does
not act as a barrier for the incident turning branch at the computed L. That
closes the confinement question negatively for this rule, at these points
and profiles. It is a first-class result. A decrease at two L values does
not establish a law in L.

## Tasks

- **R1. Branch identification (certified).**
  - In each interior medium box set, exactly one right-mover has
    Re λ > 0 and Im λ > 0 (k ∈ (−π/2, 0), the turning branch).
  - Exactly one right-mover has Re λ > 0 and Im λ < 0 (k ∈ (0, π/2), the
    continuing branch).
  - Each sign is decided by the interval box. If the identification is not
    certified, the point is `OPEN_AFTER_TRANSMISSION_ANALYSIS`.
  - Columns are identified by this sector, never by enumeration order.
- **R2. Turning-branch column.** At s = 1/50 and 1/200, for the sharp profile
  (N = 0), L = 4 (N = 32) and L = 16 (N = 128):
  - the full column of |S|² for incidence on the turning branch: interior
    left-movers, exterior right-mover; its sum encloses 1 (consistency);
  - T_ret is the decided quantity;
  - T_cont = |S_{ext R, int R(k>0)}|² is reported too.
- **R3. Consistency with the closed charter.** T_ret + T_cont must overlap
  the σ² enclosure of the same (s, profile) computed by the imported
  frequency/finite-L verifier. At sharp z₁, the T_ret enclosure must overlap
  the reviewed |t₂|² enclosure.

## Method

- **Reuse.** A thin new verifier imports
  `scripts/verify_dispersive_horizon_frequency_finite_l.py` read-only, after
  a SHA256 check (`3d585a54…80faa`). Its pipeline is reviewed (Astra
  point 4 PASS) and its bytes must not change.
  - Its `run_point` returns σ² only and not the S matrix, so the entry cannot
    be "extracted" without new code.
  - The new verifier reuses its helpers (`roots_boxes`, `medium_p`,
    `M_site_p`, `t_profile`, `solve_hp`, the precision rule) unchanged, and
    adds only the branch identification and the per-column output.
- **Runtime.** Importing re-runs the full frequency/finite-L verifier
  (about 70 min, including its own F3). The new part repeats the six
  (s, profile) solves, about 15 min.
- **Precision.** The same predeclared rule,
  p = 256 + 2(2N + 1)⌈log₂κ⌉. Not tuned after seeing results.
- **Admission.** As in the frequency/finite-L charter:
  - exact rational intervals;
  - floating point only for guesses;
  - `mpmath.iv.exp` for the tanh enclosure;
  - verifier committed before its recorded run; failed runs retained.

## Verdicts

- **Per (s, profile):**
  - `TRANSMISSION_NONZERO_CERTIFIED` (T_ret enclosure > 0 and width
    ≤ 10⁻⁶);
  - `TRANSMISSION_ZERO_PROVED` (exact zero, with a structural reason);
  - `OPEN_AFTER_TRANSMISSION_ANALYSIS`;
  - `S_MATRIX_NOT_ESTABLISHED`.
- **Line, on closure** (comparisons decided by disjoint enclosures):
  - `T_RET_DECREASING_AT_COMPUTED_L`: T_ret(sharp) > T_ret(L = 4) >
    T_ret(L = 16) at both points;
  - `T_RET_NOT_DECREASING`: T_ret(L = 16) ≥ T_ret(sharp) at both points
    (the abandonment condition);
  - `MIXED`: otherwise, stated point by point.

## Not claimed (in any case)

- Any functional law in L or ω, or the limit L → ∞.
- That T_ret is the Sabsovich mixing, or any Hawking, thermal or
  physical-horizon statement.
- Anything about the untruncated tanh profile, or at other s or L.
- Any change to the verdicts of the closed frequency/finite-L charter.
- Novelty (OPEN).

## Questions for the user (before freezing)

- **Q1. Points and profiles.** s = 1/50 and 1/200; sharp, L = 4 (N = 32),
  L = 16 (N = 128), as in the closed charter. Recommendation: as proposed,
  with no new points, to stay comparable.
- **Q2. Output.** The full column for the turning branch, plus T_cont, as
  reported data, with only T_ret decided. Recommendation: yes. The column
  shows where the reflected flux goes (which interior left-movers), and
  that costs nothing extra.
- **Q3. Line thresholds.** As written: strict decrease at both points, or
  T_ret(L = 16) ≥ T_ret(sharp) at both points as the abandonment
  condition. Recommendation: as written. An alternative is to add an
  absolute threshold (for example T_ret(L = 16) < 0.1) for "barrier".
- **Q4. Review** after execution: model(s). Proposal: Astra 6.2, as before.
