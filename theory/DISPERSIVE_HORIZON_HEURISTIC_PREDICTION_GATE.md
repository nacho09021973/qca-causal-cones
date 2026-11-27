# Dispersive-horizon heuristic prediction gate (POST_RESULTS_EXPLORATORY)

2026-11-27. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.

- Frozen by the commit that moves this file here from
  `reports/2026-11-27--dispersive-horizon-heuristic-prediction-charter-draft.md`
  (approved draft committed at `714b7dc`), on branch
  `research/dispersive-horizon-channels`, before any new computation.
- **Supersedes** the earlier draft (`4c70757`, points P1–P7 plus a control),
  which was never frozen. This charter adopts the minimal four-point design
  the user proposed on 2026-11-27, plus one truncation control.
- **Freezing.** User decision, 2026-11-27: «si». This approves the design and
  thresholds exactly as written below, with no modification:
  - Q1–Q4 with N = 8L, plus the control Q4′;
  - the A bands [0.8, 1.25] and [1/2, 2];
  - the B bands [1/1.1, 1.1] and [0.8, 1.25];
  - relative width 10⁻⁶;
  - truncation thresholds 10⁻³ and 10⁻²;
  - review by Astra 6.2 plus Grok.
- Below, "draft", "would" and "proposed" refer to this frozen text.
- **Label: `POST_RESULTS_EXPLORATORY`.**
  - The observable T_ret was chosen after the σ² results of the
    frequency/finite-L charter.
  - The formula X was chosen with knowledge of the prior-art form.
  - X was written into the turning-branch charter (`08e0703`) before T_ret
    was computed, but the four calibration ratios below are now known.
  - The new points are a prospective prediction test. They do not turn the
    earlier exploration into independent confirmation.

## 0. Authorization and budget

- **Drafting.** User decision, 2026-11-27: «Nuevo contrato para la
  heurística: SÍ, exploratorio … No ejecutaría nada hasta congelarlo». The
  four-point brief of the same day restates the design.
- **Freezing:** authorized («si», 2026-11-27; see header).
- **Not authorized:** writing the verifier, execution, review sending,
  promotion and merging. Each needs a separate user decision.
- **Budget:** one contract. A balance is mandatory on closure. No further
  contract follows automatically, whatever the outcome.

## 1. Known (with sources)

- **Turning-branch charter, closed** with `T_RET_DECREASING_AT_COMPUTED_L`.
  - Charter `theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md` (`08e0703`).
  - Report `reports/2026-11-27--dispersive-horizon-turning-branch.md`, with
    run 1 at `b22fb05`.
  - Six cases, each `TRANSMISSION_NONZERO_CERTIFIED`. Certified T_ret:

    | s | sharp | L = 4 (N = 32) | L = 16 (N = 128) |
    | --- | --- | --- | --- |
    | 1/50 | 0.357261 | 0.131279 | 0.00031249 |
    | 1/200 | 0.450200 | 0.373973 | 0.118986 |
- **Review status.** Astra 6.2 (`gpt-6.2-astra`) returned REPAIR_REQUIRED,
  for wording only
  (`reports/2026-11-27--dispersive-horizon-turning-branch-astra-review.md`).
  - Points 1–6 are PASS: R1, the column and unitarity, R3, parallelism,
    the verdicts and the reflected flux.
  - Amendment 1 is applied and has not had a second review.
  - Nothing is promoted. NOVELTY = OPEN.
- **Calibration ratios** (orientation, not certified).
  - Source: `reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt`,
    produced by `scripts/compare_turning_branch_heuristic.py` at `71488b0`.
  - The X values were re-evaluated in this session with mpmath at 30
    digits and agree.

    | s | L | ωL | X | T_ret / X | ln(T_ret/X) |
    | --- | --- | --- | --- | --- | --- |
    | 1/50 | 4 | 0.15998 | 0.118120 | 1.1114 | +0.106 |
    | 1/50 | 16 | 0.63991 | 3.2175·10⁻⁴ | 0.9712 | −0.029 |
    | 1/200 | 4 | 0.04000 | 0.376918 | 0.9922 | −0.008 |
    | 1/200 | 16 | 0.15999 | 0.118094 | 1.0076 | +0.008 |

  - These four points are **excluded** from every verdict of this contract.
  - (1/50, 4) and (1/200, 16) have nearly equal ωL. Their ratios differ by
    a factor of 1.103, so the deviations from X are not imposed by
    construction (Astra, point 7).
- **What the earlier calculations already answer**, so these are not
  repeated:
  - branch identification by box sign;
  - the column and unitarity;
  - σ² = T_ret + T_cont;
  - the attribution of the sharp-z₁ |t₂|² to k < 0;
  - the decrease of T_ret from sharp to L = 16 at two frequencies.

  What they do **not** answer is any value of T_ret at s ∉ {1/50, 1/200}
  or L ∉ {4, 16}.
- **Regime.**
  - Arc boundary. The written deduction after review puts the
    first-quadrant critical locus at (0, arg z_c*], with
    arg z_c* = arccos(0.996006471…) ≈ 0.089400 (re-evaluated in this
    session). Source: frequency/finite-L report, F1 (a) closure row; the
    run verdict for F1 (a) itself was `OPEN_AFTER_DISCRIMINANT_ANALYSIS`.
  - Known defect. The y*-classification check of the frequency verifier is
    not valid as a region label (`scripts/README.md`, "Known defect"). The
    per-point F1 (b) discriminant test is the usable regime check. It
    found one discriminant root in [A(5/16), A(7/16)] at s = 1/200, 1/50
    and 1/30 (run-1 log, lines 216–218).
  - Sector argument (Astra, written; frequency/finite-L review, point 6).
    h(0) = 1 − cos ω > 0, h(π) > 0 and h(±π/2) = −1 ± sin ω ≠ 0, so no
    real root changes k-quadrant as t varies. These inequalities hold for
    every 0 < ω < π/2. The root counts per quadrant were read from logged
    boxes only at the computed points.
- **Prior art** (`investigaciones/2026-11-26-dispersive-horizon-prior-art/comprobacion.md`).
  - Sabsovich, Wunderlich, Fleurov, Pikulin, Ilan, Meng, «Hawking
    fragmentation and Hawking attenuation in Weyl semimetals»,
    arXiv:2106.14553v3. It was read in the original, pp. 3–4, Eqs. (8)–(9):
    - a numerical S matrix of a lattice horizon with a tanh profile;
    - mixing with doublers with probability X = 1/(1 + e^{2πω/α_t}).
  - This is the "Weyl-semimetal paper" that the earlier draft (Q5) listed
    as unread. That listing was wrong.
  - Their ref. [74], an analytic derivation of the S matrix, has **not**
    been read.
  - Maertens et al. 2204.06583 is related and was not read in detail.
  - The Fermi–Dirac-type form and the lattice-doubler mechanism are prior
    art. NOVELTY = OPEN.

## 2. Physical question (single)

Does X(ω, L) = 1/(1 + e^{4πωL}), with no parameter fitted to the new results,
predict the transmission T_ret of the incident interior right-mover with
−π/2 < k < 0 into the exterior right-mover?

- Observable: T_ret = |S_{ext R, int R(k<0)}|², with unit-flux incidence on
  that branch and all other incoming amplitudes zero.
- The branch is identified by its certified λ box: Re λ > 0 and Im λ > 0,
  with k = −arg λ. It is never identified by enumeration order.
- ω = arg z = 2 arctan s exactly. α = 8 t_L′(0) = 1/(2L) is the slope of
  the continuous interpolation t(x) = 3/8 + tanh(x/L)/16 at x = 0. So
  2πω/α = 4πωL.

**Three levels, kept distinct:**

- **A. Numerical agreement** within a declared tolerance at the declared
  points. Tested here.
- **B. Compatibility with ωL scaling**, at one pair with equal ωL. Tested
  here, as compatibility only.
- **C. A functional law** T_ret = F(ωL), or T_ret = X. **Not tested and
  not obtainable** from four observations, whatever they show.

**Abandonment of the heuristic.** If ρ = T_ret/X lies certifiably outside
[1/2, 2] at any admitted point, X does not describe T_ret for this rule
beyond the calibration points. The calibration agreement is then closed as
local to those points. This is a first-class negative result.

## 3. Hypothesis and predictions (fixed before any new computation)

- **H_A.** For every admitted new point, ρ = T_ret/X ∈ [0.8, 1.25].
- **H_B.** T_ret(1/40, 8)/T_ret(1/80, 16) agrees with
  X(1/40, 8)/X(1/80, 16) = 1.00078 within the band in §6.

**Prediction table.**
- The values were evaluated with mpmath at 30 digits, as a manual
  inspection command run in this session:
  `python3 -c "import mpmath as mp; mp.mp.dps=30; …"`, with
  ω = 2·atan(1/q) and X = 1/(1 + exp(4π ω L)).
- They are orientation values. The binding prediction is the formula
  itself, enclosed with interval arithmetic by the verifier (§5).

| id | s | L | N = 8L | ω = 2 arctan s | ωL | 4πωL | X (prediction) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 | 1/80 | 8 | 64 | 0.0249986980 | 0.199990 | 2.51314 | 0.0749419 |
| Q2 | 1/40 | 8 | 64 | 0.0499895872 | 0.399917 | 5.02550 | 0.00652543 |
| Q3 | 1/80 | 16 | 128 | 0.0249986980 | 0.399979 | 5.02629 | 0.00652034 |
| Q4 | 1/40 | 16 | 128 | 0.0499895872 | 0.799833 | 10.05100 | 4.31406·10⁻⁵ |
| Q4′ (control) | 1/40 | 16 | 192 | as Q4 | as Q4 | as Q4 | as Q4 |

z(s) = (1 − s² + 2is)/(1 + s²) is exact and rational. At s = 1/40,
z = (1599 + 80i)/1601. At s = 1/80, z = (6399 + 160i)/6401.

## 4. Points and profiles

**Design check, done before accepting the user's proposal** (inspection only,
no transmission computed):

1. **Regime.** ω(1/40) ≈ 0.0500 and ω(1/80) ≈ 0.0250 both lie in
   (0, arg z_c*) ≈ (0, 0.0894). Both are interior to the s-range
   [1/200, 1/30] already scanned on the arc, so they are far from its edge.
   This placement rests on the written arc-boundary deduction. Per point it
   is re-certified at run time by R0 (§5), not assumed.
2. **Channels.** The expected counts are (2, 4, 1, 3), as at all three
   computed arc points. They are certified per case. A mismatch makes the
   point `REGIME_NOT_CERTIFIED`, and the point is **not** replaced.
3. **Frequencies.** Two new ω values, at ratio 2. Two widths, L = 8 (new)
   and L = 16.
4. **Equal ωL pair.** Q2 and Q3 have ωL = 0.39992 and 0.39998. X differs
   between them by 0.08 %. This tests B at widths 8 and 16, whereas the
   calibration pair was at widths 4 and 16.
5. **Range.**
   - ωL spans 0.20–0.80.
   - Q4 (ωL ≈ 0.80, X ≈ 4·10⁻⁵) extrapolates beyond the calibration range
     (maximum ωL 0.64). It is the strictest point: see the exponent
     equivalence in §6.
6. **Cost.** It is dominated by the mandatory import (§8). The four new
   cases add a few minutes on 4 workers.

**Result of the check:** no problem found, and no point substituted. The
only addition is the truncation control Q4′, justified in §5. The user may
drop it.

**Profile.** t(x) = 3/8 + tanh(x/L)/16 for |x| ≤ N, t = 5/16 for x < −N,
t = 7/16 for x > N, and t(0) = 3/8 exactly. This is `t_profile` of the
frequency verifier, unchanged, with N = 8L.
- Every certified statement is about **this truncated profile**, not about
  the untruncated tanh.
- At |x| = N = 8L the profile jumps by
  (1/16)(1 − tanh 8) = (1/8)/(e^{16} + 1) ≈ 1.4·10⁻⁸.
- Its effect on T_ret is not estimated analytically here; Q4′ measures it.

## 5. Method (reuse first)

**Reuse.** A thin new verifier would check SHA256 and import read-only
`scripts/verify_dispersive_horizon_turning_branch.py`
(`397f72b3a9293fe1784dfb9e3d4da8a616f215999c3c97adee006d7d880e0676`,
reviewed). It would call that file's module-level `case((s, L, N, label))`
unchanged, once per new case.
- `case` takes s, L and N as arguments. It already contains:
  - regularity at t = 5/16 and 7/16;
  - the predeclared precision p = 256 + 2(2N + 1)⌈log₂κ⌉;
  - certified root boxes, flux normalization and R1 by box sign;
  - interval propagation with outward rounding;
  - the certified invertibility of the matching matrix (‖I − RAD‖ < 1/2);
  - S^H S ∋ I, the column sum and the T_ret and T_cont enclosures.
- So **no existing script needs to change**, and no new dependency is
  needed (SymPy, mpmath `iv` and NumPy are already in use).
- Importing it re-runs the turning-branch verifier, and through it the
  frequency/finite-L, transmission, channels and transfer verifiers. That
  is **level-1 reproduction** of all six calibration cases, including the
  sharp-z₁ |t₂|² check that detects a branch swap. It costs time, not
  extra code.

**New code needed** (described here, not implemented):

- **R0, regime per new s.**
  - The F1 (b)-type test: the discriminant in τ of H_A(τ) at z(s), as a
    polynomial in A, has exactly one root in [A(5/16), A(7/16)] and is
    nonzero at both ends.
  - It reuses `tr.H_of`, `tr.Asym` and `sp.discriminant`. It is a few
    lines that reproduce the inline F1 (b) loop of the frequency verifier,
    which is not a callable function.
  - The y* classification is **not** used (known defect).
- **Channel-count handling.** The turning-branch parent asserts the counts
  and would abort. The new wrapper records a mismatch as
  `REGIME_NOT_CERTIFIED` for that point instead.
- **Relative width.** `case`'s verdict uses absolute width ≤ 10⁻⁶, which
  is not enough at Q4 (T_ret ~ 4·10⁻⁵). The wrapper requires
  width(T_ret) ≤ 10⁻⁶ · T_ret.lo.
- **Enclosure of X.** mpmath `iv` with outward rounding, at precision
  ≥ 128 bits: ω = 2 atan(1/q), then X = 1/(1 + exp(4πωL)). It is converted
  to a rational interval like the existing `tanh_RI`.
- **ρ = T_ret/X as a rational interval**, with the per-point verdicts, the
  pair ratio for B, the control comparison for Q4′, and the line verdict.
- **Parallel execution.**
  - The same pattern as the turning-branch verifier: `fork`, up to 4
    workers, longest first, and `Pool.map` so that the order is preserved.
  - Workers return rational endpoints. The parent makes every PASS check
    and decides every verdict.

**Consistency checks per new case.**
- R1 is certified.
- Counts are (2, 4, 1, 3).
- The matching matrix is certified invertible.
- S^H S ∋ I.
- The turning-branch column sums to an enclosure of 1.

Also reported: T_cont, σ² = T_ret + T_cont, and the full turning-branch
column.

**What is not repeated, and why.** The R3 overlap of T_ret + T_cont with an
imported σ² is **not applicable** at the new points: no reviewed σ² exists
there. Recomputing σ² with `run_point` would run the same code path, and
Astra noted that this sum cannot detect a branch swap. The swap protection
is R1 by box sign, plus the imported sharp-z₁ check.

**Truncation control (Q4′).**
- Q4 is repeated with N = 12L = 192, using the same predeclared precision
  rule (p = 2566 if ⌈log₂κ⌉ = 3, as at every computed arc point; the value
  is not tuned).
- Q4 is chosen because it is the most suppressed point, so the most
  sensitive to a relative error.
- Verdicts:
  - `TRUNCATION_CONTROLLED` if |T_ret(Q4′)/T_ret(Q4) − 1| ≤ 10⁻³
    (certified);
  - `TRUNCATION_SENSITIVE` if it is certifiably > 10⁻²;
  - `TRUNCATION_UNDECIDED` otherwise.
- The control never turns a statement about the truncated profile into
  one about tanh. It only says whether N = 8L is already saturated at that
  point.
- The A and B verdicts are always made at N = 8L.

**Admission.**
- Exact rational intervals throughout.
- Floating point only for guesses and preconditioners.
- `mpmath.iv` only for exp, atan and π enclosures.
- The verifier is committed before its single recorded run. Failed runs
  are retained. No development runs on the new points, only `py_compile`.

## 6. Quantitative criteria (fixed before computing)

**Per point (Q1–Q4)**, evaluated in this order:

1. `REGIME_NOT_CERTIFIED`: R0 or the channel counts fail.
2. `S_MATRIX_NOT_ESTABLISHED`: the level is not regular.
3. `OPEN_AFTER_TRANSMISSION_ANALYSIS`: a certification step fails, or the
   relative width of T_ret exceeds 10⁻⁶, or the ρ enclosure meets two
   bands.
4. Otherwise, with ρ certified:
   - `WITHIN_TOLERANCE` if ρ ⊂ [0.8, 1.25];
   - `OUTSIDE_REJECTION_BAND` if ρ ∩ [1/2, 2] = ∅;
   - `INTERMEDIATE` otherwise.

**Justification of the bands.**
- Both bands are symmetric in ln ρ.
- The tolerance |ln ρ| ≤ ln 1.25 = 0.223 is about twice the largest
  calibration deviation (0.106).
- The rejection threshold |ln ρ| > ln 2 = 0.693 is about 6.5 times that
  deviation.
- The bands are fixed from the calibration spread, not from the new
  results.

**Equivalent exponent tolerance.** If T_ret = 1/(1 + e^{κ·4πωL}), then
ρ ≈ e^{−(κ−1)·4πωL} when X ≪ 1. A tolerance of 0.223 in ln ρ therefore
allows |κ − 1| up to about:

| id | 4πωL | allowed \|κ − 1\| (tolerance) | allowed \|κ − 1\| (rejection) |
| --- | --- | --- | --- |
| Q1 | 2.51 | ≈ 9 % | ≈ 28 % |
| Q2, Q3 | 5.03 | ≈ 4.4 % | ≈ 14 % |
| Q4 | 10.05 | ≈ 2.2 % | ≈ 6.9 % |

So the same band is a much stricter test of the exponent at Q4 than at Q1.
- κ_eff = ln(1/T_ret − 1) / (4πωL) is **reported** at each point as data,
  and decides nothing.
- For reference, κ_eff at calibration (1/50, 16) is ≈ 1.004.

**B. Equal ωL pair (Q2, Q3)**, with r = ρ(Q2)/ρ(Q3) certified:
- `SCALING_CONSISTENT` if r ⊂ [1/1.1, 1.1];
- `SCALING_VIOLATED` if r ∩ [0.8, 1.25] = ∅;
- `SCALING_UNDECIDED` otherwise, or if either point is not certified.

Justification:
- The calibration pair, at widths 4 and 16, gave r = 1.103, just outside
  the consistency band.
- So the band asks the new pair, at widths 8 and 16, to do at least
  slightly better. Whether finite-L deviations shrink with L is
  `[UNVERIFIED]`, and the band does not presume it.
- B is reported alongside the line verdict and does not change it.
- `SCALING_CONSISTENT` is compatibility with ωL scaling at one pair, not a
  demonstration of it.

**Line verdict, on closure:**
- `HEURISTIC_REJECTED_AT_DECLARED_POINTS`: at least one point is
  `OUTSIDE_REJECTION_BAND`. This is the abandonment condition, and it
  applies whatever the other points show.
- `HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS`: all four points are
  `WITHIN_TOLERANCE`.
- `HEURISTIC_PARTIAL`: all four are certified, none is outside the
  rejection band, and at least one is `INTERMEDIATE`. Stated point by
  point.
- `OPEN_AFTER_PREDICTION_TEST`: no point is outside the rejection band,
  and at least one point is `REGIME_NOT_CERTIFIED`,
  `S_MATRIX_NOT_ESTABLISHED` or `OPEN_AFTER_TRANSMISSION_ANALYSIS`.

**Reported, not decided:**
- the sign pattern of ln ρ across the four points, to look for a
  systematic deviation;
- the monotonicity T_ret(L = 16) < T_ret(L = 8) at each s;
- T_cont, σ², and the turning-branch column.

**No re-adjustment.** After any new transmission is seen, none of the
following may change: α, the formula, ω (no frequency shift), L, N, the
points, the bands, or the order of the verdict rules. A different formula,
such as one with fitted α or κ, needs a new charter labelled post-results.
Points are not replaced. A point that fails keeps its non-decided state.

## 7. Limitations

**Mathematical:**
- All statements hold for the truncated profile at N = 8L (plus Q4′).
  Nothing is claimed about the untruncated tanh or about L → ∞.
- Four points cannot establish level C, the dependence on ωL alone, or the
  functional form. One pair tests B once.
- R0 is per point. It does not certify the regime between points.
- That the k < 0 right-mover is the branch that **meets** the fold at the
  new s rests on the written sector argument. Its inequalities are
  ω-generic, but the per-quadrant root counts would be read from boxes at
  the new points: certified by R1 for the interior medium, not machine
  checked for the intermediate media.

**Physical and interpretive:**
- Identifying α = 1/(2L), the continuous-interpolation slope, with
  Sabsovich's α_t is `[UNVERIFIED]`. So is identifying T_ret with their
  mixing probability.
- Agreement under A does not establish either identification. Rejection
  does not refute Sabsovich et al., since their setting is a different
  model.
- Nothing about Hawking emission, thermality, a physical horizon, or a
  temperature is claimed, whatever the outcome.

**Pending bibliographic question** (it does not block freezing and does not
change X after freezing). Check in the original, citing pages:
- under which hypotheses the Sabsovich mixing X (2106.14553, Eqs. (8)–(9))
  can be identified with an S-matrix element of the form T_ret: which
  incident and outgoing channels, what flux normalization, and a
  continuous-time or discrete-time model;
- how α_t is defined there, and when α = 1/(2L) is the right choice for a
  discrete-time lattice profile;
- their ref. [74] (analytic S matrix) and Maertens et al. 2204.06583.

Results are logged in the prior-art `comprobacion.md`.

## 8. Computational budget (estimate)

These are estimates, with timings scaled from the turning-branch run 1
(WSL2, 4 cores).

| Item | Estimate |
| --- | --- |
| Mandatory import: turning-branch verifier plus its chain, single-threaded until its own pool | ≈ 35–37 min (run 1: 09:49:54–10:27:11 UTC overall) |
| Q3, Q4 (N = 128, p = 1798 if ⌈log₂κ⌉ = 3) | ≈ 150 s each in a worker (run 1: 393 s → 546 s) |
| Q1, Q2 (N = 64, p = 1030) | ≈ 30–60 s each |
| Q4′ (N = 192, p = 2566) | ≈ 5–10 min in a worker (≈ 1.5× the sites and ≈ 1.4× the bits) |
| R0 (two discriminants, degree 28 in A) | < 1 min |
| **Total wall time** | **≈ 45–50 min** on 4 workers |

Memory is not expected to be a constraint, as in run 1.

## 9. Planned independent review

**Independence, three levels:**
1. **Reproduction.** The six calibration cases are re-run by the import,
   so they are reproduced automatically.
2. **Prediction.** The formula and thresholds are frozen before the new
   points are computed. This is the contribution of this contract.
3. **Independence of design and review.** It is limited:
   - the author is Claude;
   - Astra 6.2 helped choose the observable;
   - the bands are informed by the calibration ratios.

**Proposed review** after execution, each sending needing a go-ahead:
- Astra 6.2 (`gpt-6.2-astra`) for continuity.
- A second family, Grok (`ciro`), because Astra took part in the design.
  Probe generation before sending.
- Human review is not available unless the user provides it.

Both reviews receive the frozen charter, the verifier, the run log and the
report, with their SHA256 values and the base commit. Neither review
authorizes promotion.

## 10. Closure conditions and mandatory balance

The contract closes when one recorded run has finished, its report is
written, and the review(s) are recorded and any repairs are applied, or
when the user stops it. A failed run is retained and counts as the run,
unless it fails for an infrastructure reason unrelated to the computation;
then one rerun is allowed, and both logs are kept.

Balance table, to be filled on closure:

| Item | Outcome |
| --- | --- |
| Level-1 reproduction (import) | |
| R0 regime, counts, per point | |
| Q1–Q4: T_ret, X, ρ, κ_eff, verdict | |
| B: r, verdict | |
| Q4′ truncation control | |
| Line verdict | |
| Review(s) | |
| Bibliographic question | open / answered (with pages) |
| Promotion | none without separate user decision; NOVELTY = OPEN |

## Not claimed (in any case)

- A law in (ω, L), dependence on ωL alone, the limit L → ∞, or a
  derivation of X from the rule.
- That T_ret is the Sabsovich mixing, or that α = 1/(2L) is their α_t.
- Any Hawking, thermal, temperature or physical-horizon statement.
- Anything about the untruncated tanh profile, or at points other than
  Q1–Q4 (and Q4′).
- Any change to the closed turning-branch or frequency/finite-L verdicts.
- Novelty (OPEN).

## Recommendation (author)

**Worth freezing as written, at low cost, with a narrow scope.**

- **For:**
  - Every number is new. The formula has no free parameter, and the bands
    are fixed from the calibration spread.
  - Q4 is a strict test of the exponent (|κ − 1| ≲ 2 % for acceptance),
    so agreement is not easy to obtain by accident.
  - Both outcomes are informative, and rejection is a first-class result.
  - It needs no change to reviewed code and adds about 10 min of
    computation beyond the mandatory import.
- **Against, or limits:**
  - Even full agreement gives only A at four points and B at one pair. It
    gives no law, no identification with Sabsovich et al., and nothing
    physical.
  - The line is peripheral to the repository question, the coexistence of
    universal computation and a relativistic regime in one QCA. Its value
    is to close the heuristic question honestly, not to advance that
    question.
- **Optional, and not part of this design:** the bibliographic check of §7
  could be done before freezing. It would not change X, which is already
  declared, but it would sharpen what agreement means.

**User decision, resolved 2026-11-27 («si»):** the design and its thresholds
are approved unchanged:
- points Q1–Q4 with N = 8L, plus the control Q4′;
- the bands [0.8, 1.25] and [1/2, 2];
- the B band [1/1.1, 1.1] / [0.8, 1.25];
- the relative width 10⁻⁶;
- the truncation thresholds 10⁻³ / 10⁻²;
- review by Astra 6.2 plus Grok.

The charter is frozen by the commit that moves it to `theory/`.
