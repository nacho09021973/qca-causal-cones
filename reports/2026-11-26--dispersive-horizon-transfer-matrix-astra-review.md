# Astra review of the dispersive-horizon transfer matrix and its audit

Date: 2026-11-26. Branch: `review/dispersive-horizon-transfer-audit`.

**Reviewed snapshot** (base `d0114b2`):

| Document | Commit | SHA256 |
| --- | --- | --- |
| (A) author derivation `reports/2026-11-26--dispersive-horizon-three-step-transfer.md` | `8e5b540` | `7e372669d0155b26c26b50e464c33a4c7d6612dcf2d5e791b01d57cda90d63b6` |
| (B) audit `reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md`, pre-amendment | `d0114b2` | `9591e16e97347e660a7f4ba48156be7af66f79af3116e8d1e48abb700ec4d0d0` |
| (C) verifier `scripts/verify_dispersive_horizon_transfer_matrix.py` | `d0114b2` | `98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2` |

**Status:** Astra **REPAIR_REQUIRED** on the audit (B). PASS on sections 1–5,
which include the matrix of (A). Repairs applied as Amendment 1 of (B). Not
promoted.

## Execution

- **Authorization:** user instruction «que la haga AStra».
- **Probe:** generation was checked beforehand with a one-line `codex exec`
  probe on `gpt-6-astra`, which returned "OK", exit 0.
- **Run:** one sealed `revision-ciega astra` run, model `gpt-6-astra`, effort
  high, via `codex exec` (codex-cli 0.172.0). It ran 2026-11-26
  10:42:22–10:46:41 UTC, status `COMPLETED`, exit 0.
- **Input:** the brief plus (A), (B) and (C). The brief told Astra to derive
  the matrix from the operator of (A) before reading (B) or (C). Input SHA256
  `36549e24553fcdf0510327da4942f64a30f0810af4d14f7e06735bb84701af96`.
- **Output:** response SHA256
  `3bc70484eea6e7ddfdfc59cd17f6528ce7a0980fbf489ff85feb8a0d450c9e85`.
- **Raw files:** `reports/reviews/2026-11-26-dispersive-horizon-transfer-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.

**Independence.**

- This is **one** cross-family agent review: the auditor is Claude, the
  reviewer is OpenAI. It is not human review and not a multi-house debate.
- The model family that wrote (A) is not recorded, so independence for (A)
  holds only if (A) was not written with GPT.
- Astra could not run code. The 61/61 execution of (C) is `[UNVERIFIED]` in
  its report and rests only on this repository's own runs.

## Verdicts

| Section | Astra |
| --- | --- |
| 1 Conventions and stationary closure | PASS |
| 2 Twelve rows, four blocks, 144 entries, equivalence, no spurious solutions | PASS |
| 3 Determinant cot θ_x / cot θ_{x+1} | PASS |
| 4 Dispersion and multiplicities as published in (A) | PASS |
| 5 Support, denominators, velocities, branch continuity | PASS |
| 6 Accuracy of the audit's claims | REPAIR_REQUIRED |
| Reported execution of (C) | UNVERIFIED |
| Global | **REPAIR_REQUIRED** |

Astra's answer to the closing question: the published M_x(z) can be used
mathematically to study stationary transmission through the tanh profile, for
any L > 0 and |z| = 1. It found no wrong entry, no missing determinant factor
and no spurious solutions.

Astra independently re-derives:

- the stage relations and both closures, with the coefficients at x+1;
- the twelve rows and the four blocks;
- the two-way equivalence;
- the determinant, by the same pair-block and 12-cycle argument as (B);
- tr W/2 = A cos 3k + (1−A) cos k from the explicit product, with the
  coefficients c²d = A and −s²d + 2csr = 1 − A;
- the normalised characteristic identity;
- the support bound and its extreme paths;
- the velocities and the continuity of the branch.

## Objections and disposition

The objections were checked here before acting, not accepted as given.

1. **The audit's general claim about roots at points of zero velocity.**
   **Upheld.**
   - (B) said that band edges give double roots. At the horizon, t = 3/8 and
     z = 1, Astra derives Ω₊ ~ k³ and a quadruple root λ = 1.
   - Exact check: algebraic multiplicity 4 and geometric multiplicity 2 at
     t = 3/8; multiplicity 2 at t = 5/16 and t = 7/16 (repairs verifier R2,
     R3).
   - Repaired in (B) [A1].
   - This matters for the channel analysis at the horizon, which is still
     OPEN.

2. **T3 site count.** **Upheld.**
   - T3 compares 21 interior sites (6..26), not 22 (repairs verifier R1).
   - The 22 was copied from an earlier scratchpad check built differently.
   - The verifier's own threshold (at least 20) is unaffected.
   - Repaired in (B) [A1].

3. **"For all θ".** **Upheld (wording).** It now reads "for all admissible θ,
   z ≠ 0" [A1].

Astra's minor remarks, accepted with no change needed:

- the check on the auxiliary b₆(x+1) is a consistency check, not a second
  proof of the equivalence;
- the check that A < 0 at the endpoints relies on the written argument
  A = t(2t−1) < 0 for 0 < t < 1/2;
- the check labelled "E′(π/2)" decides −f′(π/2) = 1 − 4A.

(B) already stated all three.

## What Astra adds beyond (B), not verified here

These come from Astra's own derivations and are `[UNVERIFIED]` until checked
separately:

- (λ + i)² semisimplicity at z = i on the **whole** profile interval. The
  argument: both slopes at k = π/2 are nonzero because A < 0. (C) certifies
  only the three profile values.
- The coefficient Ω₊ = (35/32)k³ + O(k⁵) at t = 3/8. The multiplicity it
  implies is certified; the coefficient is not.
- A written compactness argument for ω* and k₊(t): a uniform positive slope
  on a strip [π/2 − δ, π/2], then the implicit function theorem.

## Outcome

The matrix of (A) passes one cross-family review. The audit (B) is repaired
by Amendment 1, and the repairs are certified by
`scripts/verify_dispersive_horizon_transfer_repairs.py`, 8/8 after the 61/61
reviewed checks. The reviewed verifier's bytes are unchanged.

The brief allowed one round, so no re-review of Amendment 1 was run.
`state/CURRENT_STATE.md` and `README.md` are unchanged. Promotion is a
separate decision for the user. TRANSMISSION remains OPEN.
