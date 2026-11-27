# Dispersive-horizon frequency and finite L: execution of F1–F3

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`.

| Item | Reference |
| --- | --- |
| Charter | `theory/DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md`, frozen at `204f33b` |
| Verifier | `scripts/verify_dispersive_horizon_frequency_finite_l.py`, SHA256 `3d585a54…80faa`, commit `00f09c9` (before its run) |
| Run 1 (recorded, only run) | `reports/2026-11-27--dispersive-horizon-frequency-finite-l-run-1.txt`, SHA256 `6a4041fc…00fe`, commit `fdbbe8a` |
| Run details | 43/43 new checks after 61 + 53 + 33 imported; exit 0; 07:53–09:01 UTC (imported checks about 49 min, new part about 14 min); Python 3.12.3, SymPy 1.14.0, NumPy 1.26.4, mpmath 1.3.0 |
| Run environment | A cloud Claude Code session, launched with a written brief; the user authorized the run there. No development runs: only `py_compile` before the commit. |

**Author verdicts (PRELIMINARY; independent review pending; not promoted).**
- F1 (a): `OPEN_AFTER_DISCRIMINANT_ANALYSIS`.
- F1 (b): CONNECTED at s = 1/4, 1/2, 3/4; not certified connected on the arc.
- F2 and F3: `TRANSMISSION_NONZERO_CERTIFIED` at all 6 + 4 points.
- Line verdict candidate printed by the verifier: `LEAKAGE_NOT_SUPPRESSED`.

**The line verdict is not adopted.** The main objection below argues that
σ², the quantity the charter's line verdicts and abandonment threshold are
written in, probably measures adiabatic branch continuity and not escape
across the horizon. If so, the abandonment condition is met for a trivial
reason. The charter is not changed after seeing the results. The objection
goes to review, and any new measure needs an amendment or a new charter,
marked as post-results.

NOVELTY = OPEN.

## Main objection: what σ² measures (author, after seeing the results; `[UNVERIFIED]`)

- **σ² grows with L towards 1.**
  - s = 1/50: 0.9605 sharp, 0.9754 at L = 4, 0.99945 at L = 16.
  - s = 1/200: 0.9592 sharp, 0.9647 at L = 4, 0.9872 at L = 16.

  This is the opposite of suppression.
- **Expected if one branch continues adiabatically.** σ² is the *maximal*
  transmission from a unit-flux superposition of the two interior
  right-movers into the single exterior right-mover (transmission report,
  Amendment 1). Suppose that, at fixed ω on the arc, one interior
  right-mover continues without a turning point, as t goes from 5/16 to
  7/16, into the exterior right-mover. Then σ² → 1 as L → ∞, for the same
  reason that T ≈ 1 at z₀: adiabatic continuity, not horizon crossing.
- **Consistent with F1 (b).** On the arc, the discriminant has one root in
  the A range. Some intermediate medium therefore has a double real root,
  which would be the turning point of the *other* interior right-mover,
  where it meets a left-mover and the count of propagating roots drops
  from 6 to 4.
- **Consistent with the low-k sheet** (author remark). At fixed ω ≠ 0 the
  exterior low-k right-mover sits at k ≈ ω/(8t − 3). As t decreases towards
  3/8, that k grows: the mode does not stop, it moves to finite k. That
  suggests the exterior "horizon" mode continues into one of the interior
  finite-k right-movers (the "doublers"). The velocity sign change at
  k → 0 is a statement at ω → 0, not at fixed ω.
- **Consequence.** The charter's abandonment threshold (σ² ≥ 1/2 at L = 16)
  and its line verdicts are written in σ². If the reading above is right,
  `LEAKAGE_NOT_SUPPRESSED` says nothing about the horizon. The
  horizon-relevant quantity would be the mode conversion at the turning
  point of the reflected branch. The Sabsovich exponent quoted in the
  charter refers to that mixing, not to σ².
- **Not verified:**
  - which interior right-mover continues (the log prints σ² only, not
    |t₁|² and |t₂|² separately);
  - that the F1 (b) discriminant root is the turning point of the other
    branch;
  - the root tracking in t at fixed ω.

  Each needs computation, hence an amendment or a new charter.

## F1. Regime boundary

**(a) Critical-value branch: `OPEN_AFTER_DISCRIMINANT_ANALYSIS`.**

- **Method.** The contract's text asks for the discriminant of H_{A,ω} as
  a curve. The verifier instead follows the critical-value branch: the
  reviewed C3 condition 4f′² = 1 − f², written in u = cos²k. The set it
  targets is the one the charter defines ("critical value or collision at
  z"). This is a method choice to be judged by the review.
- **Checks passed:**
  - thr(u, A) agrees with the reviewed C3 polynomial at t = 5/16 and 7/16;
  - u = 1 is a root for every A, so q = thr/(u − 1);
  - R(1, A) = 1, so y = 1 at u = 1;
  - u* agrees with the reviewed (5245 − √168025)/5250;
  - y* = (Re z_c*)² ∈ [0.992028890462085358141533820605, …606], which
    overlaps the square of the reviewed Re z_c* box.
- **Events over A ∈ [A(5/16), A(7/16)]:**
  - q(0, A), lc_u q and disc_u q have no root;
  - q(1, A) has exactly 1 root;
  - q has 1 root in (0, 1) at A(5/16) and none at A(7/16);
  - **res_u(q, J), of degree 26, has 1 root.**
- **Why OPEN.** The resultant root means either a stationary point of y
  along the branch, or a common root of q and J at complex or out-of-range
  u. The verifier does not separate the two cases, so the "simple
  structure" premise fails. The first-quadrant critical set is not
  certified to be (0, arg z_c*].
- **Verifier defect.** The check "declared points classified against y*"
  prints PASS. That comparison of y_s with y* is correct as arithmetic. But
  it gives region membership ("I" / "horizon arc") only under the simple
  structure, which failed. Those labels from F1 (a) are therefore **not**
  justified. The verifier is not changed; this is recorded here and in
  `scripts/README.md`.

**(b) Per-point discriminant test** (the T0 test of the reviewed
transmission verifier).
- At s = 1/4, 1/2, 3/4 the discriminant (degree 28 in A) has no root in
  range, so the point is **CONNECTED**.
- At s = 1/200, 1/50, 1/30 it has **1** root in range, so the point is not
  certified connected.

So each I point is certified CONNECTED individually, independently of
F1 (a).

## F2. Sharp profile 5/16 | 3/8 | 7/16

Precision p = 262 bits at every point (⌈log₂κ⌉ = 3). Each point has the
reviewed channel counts. Each has a matching matrix certified invertible,
with ‖I − RAD‖ ≤ 10⁻⁶, and S^H S ∋ I. Enclosure widths are about 10⁻⁵⁷.

| s | region (F1 b) | quantity | enclosure |
| --- | --- | --- | --- |
| 1/4 | I, CONNECTED | T | [0.99164648646525974543, …544] |
| 1/2 (z₀) | I, CONNECTED | T | [0.99571933684127928475, …476] |
| 3/4 | I, CONNECTED | T | [0.99663415347988300948, …949] |
| 1/200 | arc | σ² | [0.95917694282960613905, …906] |
| 1/50 (z₁) | arc | σ² | [0.96054134478794111197, …198] |
| 1/30 | arc | σ² | [0.96378334428854538181, …182] |

**Cross-checks.** At s = 1/2 and 1/50 the new pipeline reproduces the
reviewed enclosures (the overlap checks pass, and the decimals agree). This
pipeline uses higher-precision roots, normalization at the end, and a
column-scaled solve.

All six points are `TRANSMISSION_NONZERO_CERTIFIED`.

## F3. Truncated tanh profile

| s | L | N | p | σ² enclosure |
| --- | --- | --- | --- | --- |
| 1/50 | 4 | 32 | 646 | [0.97544889891764051019, …020] |
| 1/50 | 16 | 128 | 1798 | [0.99945176479917278358, …359] |
| 1/200 | 4 | 32 | 646 | [0.96466201721825333719, …720] |
| 1/200 | 16 | 128 | 1798 | [0.98718684047838943299, …300] |

- Every case has the reviewed channel counts. Every matching matrix is
  certified invertible, S^H S ∋ I, and widths are about 2·10⁻⁵⁷.
- The predeclared precision was sufficient, so the fallback to Redheffer
  composition was not needed.
- All four cases are `TRANSMISSION_NONZERO_CERTIFIED`.
- The results are stated for the truncated profile at that N; there is no
  tail bound.

**Author heuristic of the charter, contradicted.** The charter predicted
mixing ≈ 0.12 at s = 1/200, L = 16, and ≈ 3·10⁻⁴ at s = 1/50, L = 16. The
observed σ² goes the other way (0.987 and 0.9995). The main objection gives
the probable reason: σ² is not that mixing.

## Line verdict as computed

- Suppression condition (σ²(L = 16) below both the sharp value and
  σ²(L = 4), at both points): **False**.
- Abandonment condition (σ²(L = 16) ≥ 1/2 at both points): **True**.
- Candidate printed: `LEAKAGE_NOT_SUPPRESSED`. **Not adopted** until the
  main objection is reviewed (see above).

## What is certified, what is written, what is interpretation

- **Certified** (verifier, exact intervals):
  - the F1 event counts and y*;
  - the F1 (b) discriminant counts;
  - all T and σ² enclosures;
  - invertibility of the matching matrices and S^H S ∋ I;
  - the cross-checks with the reviewed z₀ and z₁ values.
- **Written, not machine-checked:**
  - unitarity in general (from flux conservation);
  - that the critical-value parametrization covers all real double roots,
    with the collisions ±1, ±i from the reviewed C3;
  - the F1 (a) step from the events to the critical set (moot, since F1 (a)
    is OPEN).
- **Interpretation, not verified:** the main objection, and the
  identification of "doublers" and of the "horizon mode".

## Process

- Verifier committed (`00f09c9`) before its only run. The run was launched
  from a cloud session with the brief given in this conversation, and the
  log was committed there (`fdbbe8a`).
- The precision rule, the points and the thresholds were not changed.
- Method choice in F1 (a): the critical-value branch instead of a
  bivariate discriminant. Declared above.

## Not claimed

- That the line is abandoned. The candidate verdict rests on σ², and that
  quantity is under objection.
- Any functional law in L or ω from these points.
- Anything about the untruncated tanh profile, or at other z or L.
- A Hawking, thermal or physical-horizon statement.
- Novelty: OPEN.

## Next steps (each needs user authorization)

1. Independent review by Astra 6.2 (fixed by the charter, Q5). The brief
   should ask explicitly about the main objection, the F1 (a) method
   choice, and the classification defect.
2. Depending on the review: an amendment or a new charter for branch
   tracking at fixed ω and for the amplitude on the reflected branch (the
   turning-point mixing), marked as post-results.
