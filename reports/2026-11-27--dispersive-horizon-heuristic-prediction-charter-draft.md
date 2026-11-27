# Dispersive-horizon heuristic prediction gate — DRAFT (EXPLORATORY)

2026-11-27. Author: Claude Code (Claude Opus 5.5). **DRAFT, not frozen.**

- It is kept in `reports/` so that committing it does not freeze it. It is
  frozen by a later commit, as
  `theory/DISPERSIVE_HORIZON_HEURISTIC_PREDICTION_GATE.md`, after the user
  answers the questions at the end. Initial status after freezing: **OPEN**.
- **Label: `EXPLORATORY`, prediction test.** The formula was written in the
  turning-branch charter before the computation it is now compared with.
  This charter tests it **out of sample**: every point below is new.

## Authorization and budget

- **Drafting.** User decision, 2026-11-27: «Nuevo contrato para la
  heurística: SÍ, exploratorio … No ejecutaría nada hasta congelarlo».
- **Not authorized:** freezing, execution, review sending and promotion.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically.

## Known, question, abandonment

**Known** (with source):

- **Turning-branch charter, closed** (`T_RET_DECREASING_AT_COMPUTED_L`).
  - Report `reports/2026-11-27--dispersive-horizon-turning-branch.md`,
    Amendment 1; Astra 6.2 REPAIR_REQUIRED (wording only).
  - Certified T_ret:

    | s | sharp | L = 4 | L = 16 |
    | --- | --- | --- | --- |
    | 1/50 | 0.357261 | 0.131279 | 0.00031249 |
    | 1/200 | 0.450200 | 0.373973 | 0.118986 |
- **The heuristic** (turning-branch charter, written before computing):

  X(ω, L) = 1/(1 + e^{2πω/α}), with α = 8 t_L′(0) = 1/(2L), so
  X = 1/(1 + e^{4πωL}), where ω = arg z = 2 atan(s).

  - Comparison output: `reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt`.
  - T_ret/X = 1.111, 0.971, 0.992 and 1.008 at the four finite-L points.
    Orientation only, not a certificate.
- **Prior art.** The form comes from Sabsovich et al. 2106.14553 (checked in
  the original: `investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`).
  Maertens et al. 2204.06583 is related. The user cites a Weyl-semimetal
  paper on "Hawking fragmentation and attenuation"; it has not yet been
  read in the original, so it is `[UNVERIFIED]`. Confirming an approximately
  thermal dependence would not by itself be novel. NOVELTY = OPEN.
- **The identification of α** with the continuous-interpolation slope, and
  of T_ret with the Sabsovich mixing, is not established (Astra, turning-
  branch review, point 7).

**Question.** Without adjustable parameters, does X predict T_ret at
frequencies and widths not yet computed, within a tolerance fixed now? And
does T_ret depend on (ω, L) approximately only through ωL, as X does?

**Abandonment of the heuristic.** If T_ret/X lies outside [1/2, 2] at any
admitted point, the formula does not describe T_ret for this rule beyond the
calibration points. The agreement found so far is then closed as limited to
those points. This is a first-class negative result. Agreement within
tolerance at the declared points does not establish a law.

## Points (all new)

As before: z(s) = (1 − s² + 2is)/(1 + s²), ω = 2 atan(s), truncated profile
t(x) = 3/8 + tanh(x/L)/16 for |x| ≤ N, N = 8L, asymptotic values beyond.

| id | s | L | N | ωL (approx.) | role |
| --- | --- | --- | --- | --- | --- |
| P1 | 1/100 | 4 | 32 | 0.080 | pair A |
| P2 | 1/400 | 16 | 128 | 0.080 | pair A |
| P3 | 1/100 | 8 | 64 | 0.160 | equal ωL to the calibration points (1/50, 4) and (1/200, 16) |
| P4 | 1/50 | 8 | 64 | 0.320 | triple C |
| P5 | 1/100 | 16 | 128 | 0.320 | triple C |
| P6 | 1/25 | 4 | 32 | 0.320 | triple C |
| P7 | 1/25 | 8 | 64 | 0.640 | equal ωL to the calibration point (1/50, 16) |

- **Truncation control.** P5 is repeated with N = 12L = 192 (P5′). The
  relative change |T_ret(P5′)/T_ret(P5) − 1| must be below 10⁻² for the
  truncation to count as controlled at that point.
- s = 1/25 gives ω ≈ 0.080, inside the horizon arc (arg z_c* ≈ 0.0894) but
  close to its upper edge. This is deliberate: it tests the formula near the
  edge of the regime. Each point must be certified regular, or it is
  reported `S_MATRIX_NOT_ESTABLISHED` and not replaced.

## Tolerance and verdicts (fixed before computing)

The ratio ρ = T_ret/X is certified as an interval. X is enclosed with
`mpmath.iv` (atan, exp, outward rounding) and T_ret is the certified
enclosure.

- **Per point:**
  - `WITHIN_TOLERANCE` if ρ ⊂ [0.8, 1.25];
  - `OUTSIDE_REJECTION_BAND` if ρ ∩ [1/2, 2] = ∅;
  - `INTERMEDIATE` otherwise.
- **Scaling** (pairs and triple with equal ωL): for each pair (i, j), the
  ratio ρ_i/ρ_j ⊂ [0.8, 1.25] counts as `SCALING_CONSISTENT`.
- **Line, on closure:**
  - `HEURISTIC_PREDICTS_WITHIN_TOLERANCE`: every admitted point is
    `WITHIN_TOLERANCE`, and the truncation control passes;
  - `HEURISTIC_REJECTED`: some admitted point is `OUTSIDE_REJECTION_BAND`
    (the abandonment condition);
  - `HEURISTIC_PARTIAL`: otherwise, stated point by point.

  The scaling results are reported alongside and do not change the line
  verdict.
- **No re-adjustment.** α, the formula, the tolerance and the points are not
  changed after seeing results. A different formula, for example one with a
  fitted α, would need a new charter and would be labelled
  post-results.

## Method

- **Reuse.** A thin verifier imports
  `scripts/verify_dispersive_horizon_turning_branch.py` read-only, after a
  SHA256 check (`397f72b3…0676`), and calls its `case` function, unchanged,
  for the new tasks.
  - The import re-runs the turning-branch verifier and, through it, the
    frequency/finite-L verifier: about 37 min on the local WSL2 machine.
  - The new cases then run in up to 4 forked processes.
- **Added code:**
  - the interval enclosure of X;
  - the ratio ρ and the per-point verdicts;
  - the scaling comparisons;
  - the truncation control.
- **Precision.** Each case uses the predeclared rule of the reused pipeline,
  p = 256 + 2(2N + 1)⌈log₂κ⌉.
- **Admission.** Exact rational intervals; floating point only for guesses;
  `mpmath.iv` for exp/atan enclosures; verifier committed before its
  recorded run; failed runs retained.
- **Runtime estimate:**
  - three L = 16 cases (about 5–6 min each in the last run);
  - the N = 192 control (larger p and more sites, perhaps 15–25 min);
  - smaller cases.

  On 4 workers, the new part should take about 30 min after the import.

## Not claimed (in any case)

- A law in (ω, L), the limit L → ∞, or a derivation of X from the rule.
- Any Hawking, thermal or physical-horizon statement.
- Anything about the untruncated tanh profile beyond the truncation
  control at P5.
- Novelty (OPEN).

## Questions for the user (before freezing)

- **Q1. Points.** P1–P7 plus the P5′ control, as above. Recommendation: as
  proposed. They cover ωL from 0.08 to 0.64, three equal-ωL comparisons,
  and the upper edge of the arc.
- **Q2. Tolerance.** Accept if ρ ⊂ [0.8, 1.25] at every point; reject if
  ρ ∩ [1/2, 2] = ∅ at any point. Recommendation: as proposed. The band is
  about twice the spread of the calibration ratios (0.97–1.11).
- **Q3. Truncation control.** P5 with N = 12L, threshold 10⁻² relative.
  Recommendation: as proposed.
- **Q4. Review:** Astra 6.2, as before. A second family (for example Grok)
  could be added, since Astra helped choose the observable.
- **Q5. Before freezing:** read the Weyl-semimetal paper the user cited in
  the original, and record it in the prior-art `comprobacion.md`.
  Recommendation: yes, because the prior-art statement in "Known" depends
  on it.
