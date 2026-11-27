# Dispersive-horizon heuristic prediction: execution (POST_RESULTS_EXPLORATORY)

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`.

| Item | Reference |
| --- | --- |
| Charter | `theory/DISPERSIVE_HORIZON_HEURISTIC_PREDICTION_GATE.md`, frozen at `35bf83f` (approved draft `714b7dc`; user «si») |
| Verifier | `scripts/verify_dispersive_horizon_heuristic_prediction.py`. First committed at `8453304` before any run. Fixed at `832f76e` (import harness) and `89f41ab` (π check). Final SHA256 `a98bbd6f…86c9`. |
| Harness test | `scripts/test_heuristic_prediction_harness.py` (`13d83a9`), output `reports/2026-11-27--dispersive-horizon-heuristic-prediction-harness-test.txt`. It computes no transmission. |
| Run 1 (failed) | `…-run-1.txt`, SHA256 `748915b4…c6ee`, commit `858d1e7`. Verifier `767655a3…57e0`. |
| Run 2 (failed) | `…-run-2.txt`, SHA256 `dfb36829…4cef`, commit `b319814`. Verifier `24d652d7…fc89`. |
| Run 3 (recorded) | `…-run-3.txt`, SHA256 `5793662a…b34d`, commit `face673`. Verifier `a98bbd6f…86c9`, at HEAD `13d83a9`. 12:54:42–13:36:48 UTC. 34/34 new checks after 61 + 53 + 33 + 43 + 38 imported. Exit 0. |
| Environment | Local WSL2, 4 cores, Python 3.12.3, SymPy 1.14.0, NumPy 1.26.4, mpmath 1.3.0 |
| Authorization | Writing the verifier: «1 autorizado». Run: «autorizo la ejecucion». Run 2: «si». Run 3 and harness test: «si, con la prueba previa». This report: «si, haz commit y redacta el informe». |

**Author verdicts (PRELIMINARY; independent review pending; not promoted).**
- Q1–Q4: all `WITHIN_TOLERANCE`.
- Truncation control: `TRUNCATION_CONTROLLED`.
- B: `SCALING_CONSISTENT`.
- Line candidate: **`HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS`**.

POST_RESULTS_EXPLORATORY. NOVELTY = OPEN.

## Deviation from the charter (§10): three runs

The charter allows one rerun after a failure that is unrelated to the
computation. Two runs failed. Neither produced any value at a new point, and
both logs are retained.

- **Run 1.** `PicklingError` while the *imported* turning-branch verifier
  ran its own pool. The wrapper loaded that module with
  `spec_from_file_location` but did not register it in `sys.modules`.
  - The crash happened inside the import (run-1 log, lines 431–453),
    before R0, X or any new case.
  - Fix at `832f76e`: register the module before executing it.
  - Run 2 was the single rerun the charter allows.
- **Run 2.** The full import passed, including the reproduction of the six
  calibration cases. R0 then passed at all four values of s.
  - The run then failed at a sanity check of the π enclosure. The check
    wrongly required the truncated decimal 3.14159265358979323846264, which
    lies below π, to lie inside a 2^−300-wide enclosure of π.
  - The enclosure itself was correct (checked by inspection).
  - No new transmission was computed: the run-2 log has no Q-point
    transmission line.
  - Fix at `89f41ab`.
- **Run 3** goes beyond the charter's allowance. It was run on an explicit
  user decision, preceded by a harness test the user requested.
  - The harness test executes the verifier's own post-import code. That code
    is extracted with `ast` from the bytes committed at `89f41ab`, minus 21
    listed nodes, and run on the real X enclosures, the real calibration
    T_ret and synthetic values.
  - It exercises every verdict branch, and reproduces the calibration ratios
    1.1114, 0.97121, 0.99219 and 1.0076.
- **No transmission at a new point was seen before run 3.** The prediction
  table, the bands and the points were not changed after any failure. Only
  the import harness and a sanity check were changed.

## Results

T_ret = |S_{e,r}|²: unit-flux incidence on the turning branch r, which R1
certifies by box sign (k ∈ (−π/2, 0)), into the exterior right-mover. The
truncated tanh profile has N = 8L. X = 1/(1 + e^{4πωL}) with ω = 2 atan(s) is
enclosed exactly (rational intervals). ρ = T_ret/X.

| id | s | L | N | ωL | X | T_ret (certified) | ρ | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 | 1/80 | 8 | 64 | 0.19999 | 0.0749419114 | 0.0790715159 | 1.055104072 | `WITHIN_TOLERANCE` |
| Q2 | 1/40 | 8 | 64 | 0.39992 | 0.0065254311 | 0.0067700657 | 1.037489411 | `WITHIN_TOLERANCE` |
| Q3 | 1/80 | 16 | 128 | 0.39998 | 0.0065203439 | 0.0067200662 | 1.030630652 | `WITHIN_TOLERANCE` |
| Q4 | 1/40 | 16 | 128 | 0.79983 | 4.31405994·10⁻⁵ | 3.72796371·10⁻⁵ | 0.864142772 | `WITHIN_TOLERANCE` |

- The printed enclosures of T_ret have width ≤ 10⁻²⁴, and those of ρ
  ≤ 10⁻¹².
- The relative-width criterion (10⁻⁶) is met at every point.
- **B (equal ωL):** r = ρ(Q2)/ρ(Q3) ∈ [1.006654914866, 1.006654914867], so
  `SCALING_CONSISTENT` (band [1/1.1, 1.1]). For comparison, the calibration
  pair at widths 4 and 16 gave 1.103.
- **Truncation control (Q4′, N = 192):** T_ret(N = 192)/T_ret(N = 128)
  ∈ [1.000010044965, 1.000010044966], so `TRUNCATION_CONTROLLED`
  (threshold 10⁻³).

**Certified checks in every case** (run-3 log):
- R0: one real fold in [A(5/16), A(7/16)] at s = 1/80 and 1/40, reproduced
  at 1/50 and 1/200;
- channel counts (2, 4, 1, 3);
- R1 branch identification by box sign;
- matching matrix certified invertible (‖I − RAD‖ ≤ 10⁻⁶);
- S^H S ∋ I;
- the turning-branch column sums to an enclosure of 1;
- X agrees with the frozen prediction table.

**Level-1 reproduction.** The import re-certified the six calibration T_ret
of the turning-branch run, digit for digit: for example (1/50, 16)
0.00031248888433704610. The calibration ratios are re-obtained as certified
intervals:

| s | L | ρ |
| --- | --- | --- |
| 1/50 | 4 | 1.1114026144 |
| 1/50 | 16 | 0.9712078899 |
| 1/200 | 4 | 0.9921878143 |
| 1/200 | 16 | 1.0075516797 |

## Reported data (orientation; no verdict depends on it)

| id | κ_eff = ln(1/T_ret − 1)/(4πωL) | sign of ln ρ | T_cont | σ² = T_ret + T_cont |
| --- | --- | --- | --- | --- |
| Q1 | 0.97688 | + | 0.907254 | 0.986326 |
| Q2 | 0.99263 | + | 0.989350 | 0.996120 |
| Q3 | 0.99396 | + | 0.990369 | 0.997089 |
| Q4 | 1.01453 | − | 0.999786 | 0.999824 |

- T_ret(L = 16) < T_ret(L = 8) at both s, by disjoint enclosures.
- **Where the rest of the turning-branch flux goes.** From the printed
  columns:

  | id | low-k left-mover u | other k < 0 left-mover | \|k\| ≈ 2 channels |
  | --- | --- | --- | --- |
  | Q1 | 0.906573 | 0.014355 | ~10⁻¹⁵ |
  | Q2 | 0.984478 | 0.008752 | ~10⁻¹⁶ |
  | Q3 | 0.987363 | 0.005917 | ~10⁻¹⁶ |
  | Q4 | 0.998246 | 0.001717 | ~10⁻¹⁶ |

  - Hand check, not certified: k = −arg λ of the "other" mode
    (≈ −0.0333 at s = 1/40, ≈ −0.0167 at s = 1/80) matches
    k ≈ −ω/(8t − 1) at t = 5/16. That is the low-k left-mover of the
    *other* sheet of the dispersion.
  - At fixed ωL ≈ 0.40 its weight falls from 0.00875 (L = 8) to 0.00592
    (L = 16).
  - This bears on the conjecture note (Amendment 2). It does not bear on
    this charter's verdicts.

## Reading (interpretation, not certified)

- The formula, fixed before computing, has no free parameter. It predicts
  T_ret within 14 % at four new points, over three decades of T_ret
  (8·10⁻² to 4·10⁻⁵), including ωL = 0.80, beyond the calibrated range.
- The largest deviation is at Q4, the highest ω. In exponent terms
  (κ_eff = 1.0145) it is 1.5 %.
- This is the direction expected if the turning point lies outside the
  linear zone of the profile at high ω. That cause is `[UNVERIFIED]`: the
  turning-point-location argument in the conjecture note is a hand
  estimate.
- B: at equal ωL, widths 8 and 16 agree to 0.7 %. This is compatible with
  dependence mainly through ωL at this pair. It is one pair only.

## Not claimed

- Level C: any law T_ret = F(ωL), or T_ret = X, or the limit L → ∞.
- That α = 1/(2L) is the α of De Beule et al. or Sabsovich et al.
  - The *definition* is consistent: the horizon slope of the low-k group
    velocity, with v = 8t − 3 checked at `9e8cb5a`.
  - Their derivation is for a continuum, continuous-time model. Its
    applicability to this QCA is not established.
- Any Hawking, thermal or physical-horizon statement.
- Anything about the untruncated profile beyond the Q4′ control.
- Any change to the closed turning-branch or frequency/finite-L verdicts.
- Novelty: OPEN. The formula and the mechanism are prior art.

## Independence

- **Level 1 (reproduction):** done by the import.
- **Level 2 (prospective prediction):** formula, points and bands were frozen
  at `35bf83f` before any new transmission was computed. That is what this
  charter tests.
- **Level 3 (independence of design and review): limited.**
  - The author is Claude.
  - Astra 6.2 helped choose the observable.
  - The bands were informed by the calibration ratios.

## Closure balance (charter §10)

| Item | Outcome |
| --- | --- |
| Level-1 reproduction (import) | Six calibration T_ret re-certified, digit for digit |
| R0 regime and counts, per point | Certified at s = 1/80 and 1/40; counts (2, 4, 1, 3) in all five cases |
| Q1–Q4: T_ret, X, ρ, κ_eff, verdict | Table above; all `WITHIN_TOLERANCE` |
| B | r = 1.00665, `SCALING_CONSISTENT` |
| Q4′ truncation control | 1.00001, `TRUNCATION_CONTROLLED` |
| Line verdict | **`HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS`** (author candidate) |
| Runs | Three. Runs 1 and 2 failed before any new point; run 3 is on a user decision beyond §10. Deviation recorded above. |
| Review(s) | Pending: Astra 6.2 and Grok (charter §9) |
| Bibliographic question | Partly answered. De Beule et al. 2106.14595 read. The α definition is consistent; applicability to the QCA is open (`comprobacion.md`, third and fourth batches). |
| Promotion | None. NOVELTY = OPEN. |

## Next steps (each needs user authorization)

1. Independent review by Astra 6.2 and Grok (charter §9). Each sending
   needs a go-ahead and a generation probe.
2. After review: closure, and merging into `main` or promotion as the user
   decides.
3. Optional, new charter: the cheap falsification tests listed in
   `theory/DISPERSIVE_HORIZON_TURNING_POINT_CONJECTURE.md` §7:
   - a second profile at equal φ′(0);
   - a sequence in L at fixed μ.

   The second would also track the cross-sheet leak.
