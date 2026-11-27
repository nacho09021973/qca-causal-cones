# Dispersive-horizon turning-branch transmission: execution (POST_RESULTS_EXPLORATORY)

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`.

| Item | Reference |
| --- | --- |
| Charter | `theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md`, frozen at `08e0703` |
| Verifier | `scripts/verify_dispersive_horizon_turning_branch.py`, SHA256 `397f72b3…0676`, commit `b0bb720` (before its run) |
| Run 1 (recorded, only run) | `reports/2026-11-27--dispersive-horizon-turning-branch-run-1.txt`, SHA256 `797cdda1…2c1e`, commit `b22fb05` |
| Run details | 38/38 new checks after 61 + 53 + 33 + 43 imported. Exit 0. 09:49:54–10:27:11 UTC: the imported run took about 35 min, single-threaded; the six cases took about 2.5 min in 4 forked processes. Local WSL2, 4 cores, Python 3.12.3, SymPy 1.14.0, NumPy 1.26.4, mpmath 1.3.0. |
| Authorization | Writing: user «si, recuerda que lo ejecutara Claude Code, y que si es posible habria que montarlo para que usara los 4 hilos disponibles». Run: «lanzalo aqui». |

**Author verdicts (PRELIMINARY; independent review pending; not promoted).**
- All six cases: `TRANSMISSION_NONZERO_CERTIFIED`.
- Line candidate: **`T_RET_DECREASING_AT_COMPUTED_L`**.
- The abandonment condition, T_ret(L = 16) ≥ T_ret(sharp) at both points,
  is **not** met.

POST_RESULTS_EXPLORATORY. NOVELTY = OPEN.

## Results

T_ret = |S_{ext R, int R(k<0)}|² is the transmission of the interior
right-mover in the sector −π/2 < k < 0, the branch that meets the turning
point. Incidence has unit flux. Each enclosure has width below 10⁻²⁰ as
printed; the internal width is about 10⁻⁵⁷.

| s | profile | T_ret | T_cont = \|S_{ext R, int R(k>0)}\|² | p |
| --- | --- | --- | --- | --- |
| 1/50 | sharp | [0.35726102067870325215, …216] | [0.60328032410923785982, …983] | 262 |
| 1/50 | L = 4 | [0.13127930001691567909, …910] | [0.84416959890072483109, …110] | 646 |
| 1/50 | L = 16 | [0.00031248888433704610, …611] | [0.99913927591483573748, …749] | 1798 |
| 1/200 | sharp | [0.45019985749482620215, …216] | [0.50897708533477993690, …691] | 262 |
| 1/200 | L = 4 | [0.37397340891991448117, …118] | [0.59068860829833885602, …603] | 646 |
| 1/200 | L = 16 | [0.11898601934473758136, …137] | [0.86820082113365185162, …163] | 1798 |

**Line.** T_ret(sharp) > T_ret(L = 4) > T_ret(L = 16) strictly, at both
points, decided by disjoint enclosures. So the candidate is
`T_RET_DECREASING_AT_COMPUTED_L`.

**Certified checks in every case:**
- **R1.** The turning branch is identified by the sign of its λ box:
  - λ ≈ 0.8889 + 0.4580i at s = 1/50;
  - λ ≈ 0.8641 + 0.5032i at s = 1/200.

  The continuing branch is the other right-mover, with Im λ < 0.
- **Channel counts** (2, 4, 1, 3), the reviewed ones.
- **Matching matrix** certified invertible.
- **Unitarity:** S^H S ∋ I, and the turning-branch column sums to an
  enclosure of 1.
- **R3:**
  - T_ret + T_cont overlaps the σ² of the same case, which the imported
    frequency/finite-L verifier recomputed in the same run;
  - at sharp z₁ (s = 1/50), T_ret overlaps the reviewed
    |t₂|² = 0.35726102067870325215… of the transmission verifier.

  So the earlier attribution of |t₂|² to the k < 0 branch is now confirmed
  by box sign, not only by enumeration order.

**Where the rest of the turning-branch flux goes** (column of |S|², reported
data). At finite L almost all of it is reflected into the interior
left-mover in the k < 0 sector with the larger |k|:
- k ≈ −0.083 at s = 1/50;
- k ≈ −0.020 at s = 1/200.

| s | profile | that left-mover | other k < 0 left-mover | two \|k\| ≈ 2 left-movers |
| --- | --- | --- | --- | --- |
| 1/50 | sharp | 0.6054 | 0.0341 | 0.0029, 0.0003 |
| 1/50 | L = 16 | 0.99681 | 0.00288 | ~10⁻¹⁶ |
| 1/200 | sharp | 0.5212 | 0.0250 | 0.0033, 0.0004 |
| 1/200 | L = 16 | 0.86756 | 0.01345 | ~10⁻¹⁷ |

The transmission reviewers already placed the k ≈ −0.083 mode at s = 1/50
on the low-k sheet: transmission report, Amendment 1, sheet argument. Its
counterpart at s = 1/200 has not been checked the same way.

## Reading (interpretation, not certified)

- At the computed points, σ² grows with L because T_cont → 1, while the
  turning-branch transmission T_ret falls.
  - At s = 1/50 it falls by three orders of magnitude, from 0.357 to
    3·10⁻⁴.
  - At s = 1/200 it falls by a factor of about 4, from 0.450 to 0.119.
- This is the separation that the frequency/finite-L review asked for: σ²
  conflated the continuing branch with the turning branch.
- The suppression is stronger at the higher of the two frequencies. That is
  the direction expected if the turning point acts as a frequency-dependent
  barrier. Two frequencies do not establish a law.

## Comparison with the charter heuristic (orientation; `[UNVERIFIED]`)

The charter wrote down, before computing, X = 1/(1 + e^{2πω/α}) with
α = 1/(2L), that is X = 1/(1 + e^{4πωL}). This is the Sabsovich et al. form
with the author's identification α = |dv/dx| at the horizon. Script
`scripts/compare_turning_branch_heuristic.py` (commit `71488b0`); output in
`reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt`;
mpmath at 40 digits, no fitting.

| s | L | X (heuristic) | T_ret | T_ret / X |
| --- | --- | --- | --- | --- |
| 1/50 | 4 | 0.11812 | 0.13128 | 1.111 |
| 1/50 | 16 | 0.00032175 | 0.00031249 | 0.971 |
| 1/200 | 4 | 0.37692 | 0.37397 | 0.992 |
| 1/200 | 16 | 0.11809 | 0.11899 | 1.008 |

- The ratio lies between 0.97 and 1.11 at four points, over three decades of
  T_ret.
- **This is not claimed as a law or as a derivation.**
  - Four points with two L values cannot test the functional form.
  - The identification of α with 8 t_L′(0) = 1/(2L), and of T_ret with
    Sabsovich's mixing probability, is not established.
  - The heuristic has no free parameter here, but it was chosen with
    knowledge of the prior-art formula.
  - Finite-L corrections (the L = 4 points) are visible.
- It does make a specific, falsifiable prediction for other (ω, L). Testing
  it would need a new charter.
- The script docstring says the log is read "after a SHA256 check". The
  script prints the SHA256 but does not compare it with a fixed value. The
  printed value matches the committed log.

## Process

- The verifier was committed (`b0bb720`) before its only run. No
  development runs; only `py_compile`.
- The comparison script was committed (`71488b0`) before its run, and its
  output is kept.
- **Parallelism.** After the mandatory single-threaded import, the six cases
  run in 4 forked processes. All checks are made in the parent from
  returned plain Fractions, so the results do not depend on scheduling.
  - As a consequence, the six cases' PASS lines carry the same timestamp
    (about 154 s): they are printed after the pool returns.
- The `fork` start method requires Linux or WSL. It does not run on native
  Windows.
- Floating point appears only in guesses and preconditioners; `mpmath.iv.exp`
  supplies the tanh enclosure; and the comparison table is orientation, not
  certified.

## Not claimed

- Any functional law in L or ω, or the limit L → ∞.
- That T_ret equals the Sabsovich mixing, or any Hawking, thermal or
  physical-horizon statement.
- Anything about the untruncated tanh profile, or at other s or L.
- Any change to the closed frequency/finite-L verdicts, including
  `LEAKAGE_NOT_SUPPRESSED` for σ².
- Novelty: OPEN. The suppression mechanism and the formula are prior art.

## Next steps (each needs user authorization)

1. Independent review by Astra 6.2 (fixed by the charter, Q4).
2. After review, a closure balance. Whether to test the heuristic at other
   (ω, L) is a separate decision, and would need a new charter.
