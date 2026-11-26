# Astra review of the dispersive-horizon channels execution (C1–C5)

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`. Reviewed at
base `526823f`.

**Reviewed snapshot:**

| Document | Commit | SHA256 |
| --- | --- | --- |
| channels charter `theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md` | `7a63529` | `8ad65212fdc99dd3367ceb073183fd51ba046fe0ea9f09671c361be64b7c3b37` |
| channels report `reports/2026-11-26--dispersive-horizon-channels.md` | `4ff574c` | `71109df6c24ceb1368b6e367f06d449d6f4630e7e90a460f3771ade62fa45114` |
| channels verifier `scripts/verify_dispersive_horizon_channels.py` | `a5b9be3` | `08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc` |
| reviewed matrix verifier `scripts/verify_dispersive_horizon_transfer_matrix.py` | `d0114b2` | `98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2` |
| run log `reports/2026-11-26--dispersive-horizon-channels-run.txt` | `4ff574c` | `cff1082b90dd3ef6f8e28b02a249f2437cb2a467de03d2f5f1de39bdf7fcaaa8` |

**Status:** Astra **REPAIR_REQUIRED**. No mathematical claim of the report is
refuted. The objections concern deliverables the charter requires and the
report does not give. Repairs go to Amendment 1 of the channels report. Not
promoted.

## Execution

- **Authorization:** user «autorizo solo Astra», then «quiero la version 6.2»
  (2026-11-26).
- **Model:** `gpt-6.2-astra`, effort high, codex-cli 0.172.0, via
  `ASTRA_MODEL=gpt-6.2-astra revision-ciega astra`. A one-line probe returned
  "OK" beforehand. The name `gpt-6.2` without suffix is refused by the account.
- **Interrupted first attempt.** A first send used the tool default
  `gpt-6-astra`. It was stopped within seconds, when the user asked for 6.2,
  and returned no response. The same input had already been sent. Its files
  are kept in `intento-interrumpido-gpt-6-astra/`.
- **Run:** 2026-11-26 15:36:18–15:40:50 UTC, status `COMPLETED`, exit 0.
- **Hashes:** input SHA256
  `570802b6f6103aaf698955a18991eeeddc9e72048b663e2bad8f62c18f32c54f`, identical
  to the interrupted attempt. Response SHA256
  `8e981bcb795c88468d950e1cdc84a01fd5452d22ff74aae22b679f749339ef8e`.
- **Raw files:** `reports/reviews/2026-11-26-dispersive-horizon-channels-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** one cross-family agent review (author Claude, reviewer
  OpenAI). It is not human review. Astra could not run code and marks the
  executions and byte identities `[UNVERIFIED]`.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 C1 flux form | PASS |
| 2 C2 root structure | REPAIR_REQUIRED (count between thresholds missing) |
| 3 C3 thresholds and window | REPAIR_REQUIRED (rational enclosures not delivered) |
| 4 C4 classification on I | REPAIR_REQUIRED (evanescent roots not identified individually) |
| 5 C5 normalization | REPAIR_REQUIRED (per-root factors not recorded) |
| 6 Verifier | REPAIR_REQUIRED (some acceptance conditions weaker than the published result) |
| 7 Verdict and scope | REPAIR_REQUIRED; as delivered, the charter gives `OPEN_AFTER_CHANNEL_ANALYSIS` |
| Global | **REPAIR_REQUIRED** |

## What Astra confirms by hand

- **C1.** The cut current derived from the stage shifts and L₋ fixes D, the
  index 7 and the sign of E₇₇.
- **det G_x = −cot²β₆(x), varying profile.** Astra gives a hand proof of
  this, where the report had it as an unchecked author remark: rewrite the
  cut flux with the last term |(c₆a₆ − za₁)/s₆|², then count signature
  (5, 7) and the change of variables.
- **C2.** The symmetry, the reduction Φ = −2h, and winding −2 from
  det U(k) = e^{−2ik}.
- **C3.**
  - Critical values versus collision points; local slopes at the collision
    points are −1 ± 2(4t − 1) and −1 ± 2(1 − 4A), all nonzero.
  - Quotients 2625u² − 5245u + 2604 (interior) and 343u² − 1211u + 1012
    (exterior).
  - A coarse rational box Re z_c* ∈ (9/10, 1), Im z_c* ∈ (1/20, 1/8).
  - The quartic for Re z_c*, recomputed by a resultant, with degree 4 argued
    by hand.
- **C4.**
  - At ω = π/2, h = (1 − s)[2(1 + s)(1 + Bs²)² − 1], s = sin k, B = −4A,
    giving four simple roots by hand.
  - At z₀ the signs of v, in increasing k, are −, −, +, − in both media.
- **C5.** −iU^H U′ = Σ R_j^H σ_z R_j − I, and F = Ω′‖q₁‖² exactly. The
  evanescent pairing is correct.
- **Verifier.** RI, CI and `sqrt_RI` are correct inclusions, and no floating
  point enters a certified quantity.

## Objections and disposition

Each objection was checked against the frozen charter
(`theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md`, C2–C5 and Verdicts) before
being accepted.

1. **Major. C2 count between thresholds; "Not claimed" outside I.** The
   charter asks to "count the roots on the unit circle as a function of ω
   between thresholds". The report counts only on I, and its "Not claimed:
   anything at quasienergies outside I" contradicts that task. Astra's table
   (`[UNVERIFIED]` until certified):
   - interior, 0 < dist(ω, πℤ) < arg z_c*: 6 propagating roots (2 right, 4 left);
   - interior elsewhere: 4 (1 right, 3 left);
   - exterior on every regular arc: 4 (1 right, 3 left).

   **Upheld.** To be certified in Amendment 1 at exact points on each side
   of every threshold and collision point.
2. **Major. C3–C5 deliverables.** The charter asks for "certified rational
   enclosures" (C3), "every root λ" with its type (C4), and "the eigenvector
   … normalized" for each propagating root (C5). The run log keeps only the
   aggregate counts. **Upheld.** Amendment 1 is to emit:
   - rational boxes for the four z_c;
   - isolating boxes for the eight evanescent roots in each medium, with the
     side of the unit circle;
   - for each propagating root, the τ interval, the sign, the kernel vector
     chosen, and enclosures of F, 1/√|F| and the normalized vector.
3. **Medium. Verifier acceptance conditions and provenance.**
   - The count check tests internal consistency, not the published values:
     it would accept 2 right and 4 left.
   - The minimal polynomial is not compared with the printed coefficients.
   - There is no hash check of the imported reviewed verifier.

   **Upheld.** Amendment 1 asserts the published values and checks the
   SHA256 of both imported files.
4. **Process.** The development run before the commit is a literal deviation
   from the charter. It does not invalidate the identities or the window,
   which was fixed in advance. **Upheld as stated.** The Amendment 1
   verifier is committed before its recorded run.

## Outcome

As delivered at `526823f`, the channels execution stands at
`OPEN_AFTER_CHANNEL_ANALYSIS`, with the open obligations in objections 1–2.
The author candidate `CHANNELS_CLASSIFIED` waits on Amendment 1 and its
review. Existence and uniqueness of the incident channel on I are not
disputed. TRANSMISSION = OPEN. Nothing is promoted.
