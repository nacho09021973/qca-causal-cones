# Astra review of the dispersive-horizon turning-branch execution

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`. Reviewed at
`75c7e30` (brief committed at `bac572e`).

**Reviewed snapshot** (SHA256 of the copies sent, from the provenance header
of `informe_astra.md`):

| Document | SHA256 |
| --- | --- |
| `theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md` | `0117754239c2afbcea4e08739ec7b35ae0efca12529e66f7a78706848e33ee0f` |
| `reports/2026-11-27--dispersive-horizon-turning-branch.md` | `43d278468bef902fe4529ff614fc8783975a526fe8ebf6a89685f69f13ac4423` |
| `scripts/verify_dispersive_horizon_turning_branch.py` | `397f72b3a9293fe1784dfb9e3d4da8a616f215999c3c97adee006d7d880e0676` |
| `scripts/verify_dispersive_horizon_frequency_finite_l.py` | `3d585a541663ad7f51a539d728069d228e6a8473772ccc3ca90bb17a8ef80faa` |
| run-1 log | `797cdda126fce0c5134d4b93bc5890e1830a8b80d2f3e699911db753e3452c1e` |
| `scripts/compare_turning_branch_heuristic.py` | `c122bc97a8ad15088164e8590fee2f393e8d7667c31e2441f9e19db244cbdae6` |
| heuristic output | `6a028e1c44b53cd808335fe66aade5f5b968cb694f9dc1dc6dc9aaec15f8ce84` |

**Status:** Astra **REPAIR_REQUIRED**, limited to the execution report.
- The six `TRANSMISSION_NONZERO_CERTIFIED` verdicts stand.
- The four strict comparisons justify `T_RET_DECREASING_AT_COMPUTED_L` at
  closure.
- No repair requires re-running.
- Not promoted.

## Execution

- **Authorization:** user «autorizo la revisión de Astra 6.2» (2026-11-27).
  The model is fixed by the charter (Q4).
- **Model:** `gpt-6.2-astra`, effort high, via
  `ASTRA_MODEL=gpt-6.2-astra revision-ciega astra`. A probe returned "OK"
  beforehand.
- **Run:** 2026-11-27 10:49:33–10:51:59 UTC, status `COMPLETED`, exit 0.
- **Hashes:** input SHA256
  `a44b9ec22a3be634f88623c5204640657ada3cfec04085a32b83df525fe8ea3d`; response
  SHA256 `057438e2242fec830573337da2690ad50315d303d76f9422c92dbe92f2867cd8`.
- **Raw files:** `reports/reviews/2026-11-27-dispersive-horizon-turning-branch-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** one cross-family agent review (author Claude, reviewer
  OpenAI). It is not human review.
  - The reviewer had also proposed this observable in the previous round,
    so it is not independent of the question's design.
  - Commit chronology, run uniqueness and real file hashes are
    `[UNVERIFIED]` for the reviewer.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 Branch identification (R1) | PASS |
| 2 Column and unitarity (R2) | PASS |
| 3 Cross-checks (R3) | PASS |
| 4 Parallelism | PASS |
| 5 Verdicts | PASS; no contractual reason to withhold the line candidate |
| 6 Reflected flux | PASS; sheet assignment at s = 1/200 justified by hand |
| 7 Heuristic comparison | REPAIR_REQUIRED |
| 8 Scope | REPAIR_REQUIRED |
| Global | **REPAIR_REQUIRED** (wording only) |

## Main findings (summary; not a source)

- **R1.** The box sign selects k ∈ (−π/2, 0) among modes whose flux is
  already certified positive. Column indices and right-hand sides follow
  the same list, so the selection does not depend on enumeration order.
  The old and new logs print the two right-movers in opposite order at z₁,
  which is a visible check.
- **R3.**
  - The σ² cross-check alone would not detect a branch swap, since the sum
    is symmetric in the two branches.
  - The sharp-z₁ check does detect it: T_ret overlaps the reviewed |t₂|²
    and is disjoint from 0.60328.
  - So the attribution of |t₂|² to k < 0 is confirmed.
- **Parallelism.**
  - Pool.map preserves the input order.
  - `G_CACHE` and the precision contexts are per process.
  - The statement "all checks are made in the parent" is inexact. Repaired.
- **Reflected flux.** "Larger |k|" must be restricted to −π/2 < k < 0. The
  sheet assignment at s = 1/200 is justified by hand, using the sign of
  Im(z λ̄).
- **Heuristic.**
  - No circularity was found.
  - (1/50, 4) and (1/200, 16) have almost the same ωL but different
    ratios, so the agreement is not imposed.
  - "Finite-L corrections are visible" overreads the data; the data show
    deviations from X. Repaired.
  - Identifying α stays `[UNVERIFIED]`.
- **Scope.** "T_cont → 1" is an unnecessary asymptotic reading. It is
  replaced by the finite comparison of increments.

## How the repairs are handled

- All four repairs are applied to the execution report as Amendment 1
  ([A1]). They are not re-reviewed.
- The comparison script is **not** edited. Its docstring overstates the
  SHA256 handling, but changing it would decouple the file from the run
  whose output is kept. The report and `scripts/README.md` record the
  discrepancy.
- The verifier is unchanged.
- The line verdict `T_RET_DECREASING_AT_COMPUTED_L` is recorded under the
  frozen charter, with the closure balance in the report.
