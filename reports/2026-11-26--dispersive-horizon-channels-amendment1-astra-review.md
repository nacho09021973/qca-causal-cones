# Astra review of Amendment 1 of the dispersive-horizon channels report

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`. Reviewed at
`6d45537`.

**Reviewed snapshot:**

| Document | Commit | SHA256 |
| --- | --- | --- |
| `amendment1.diff` (`git diff 526823f 6d45537` of the channels report) | — | `2f8ca47e70f0a5490b1fd202a67ebcfe5d56cd32e9e16a50e70dab28a210232c` |
| channels report with Amendment 1 | `6d45537` | `5b41e20462cde535b191a463f4ecfc1fd009142fb65af1b0c3d465145adcddca` |
| Astra's report on the channels execution | `49ebac2` | `43fbf0abe27e3cd0a24538c1fe7e83e3e1205df3fd14c3bb371d0a2544e08ece` |
| Amendment 1 verifier | `ea3067a` | `37aacbb5a3680fa3de3c74660b2fccfcd507e7b04c7f91b1b2b105c3416ebdd6` |
| channels verifier | `a5b9be3` | `08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc` |
| Amendment 1 run log | `6d45537` | `7c3bbe83ae9e6b23452cdc6fa7bdde984faedf28311e96e88f58369521c581fb` |

**Status:** Astra **PASS** (global). `CHANNELS_CLASSIFIED` follows under the
frozen charter. The editorial corrections are applied below; the verifiers
are not changed. Not promoted.

## Execution

- **Authorization:** user «permiso concedido» (2026-11-26).
- **Model:** `gpt-6.2-astra`, effort high, codex-cli 0.172.0, via
  `ASTRA_MODEL=gpt-6.2-astra revision-ciega astra`. A probe returned "OK"
  beforehand.
- **Run:** 2026-11-26 16:34:32–16:37:32 UTC, status `COMPLETED`, exit 0.
- **Hashes:** input SHA256
  `965c89148d6c700fdac2e031237d91b5d48a1f2a7624c85abd33033e6ab7fe3d`; response
  SHA256 `8297e37abec9a9f69cd798e5d47ac47e7e12d8ee5db16cea7ae2e9d079844b0d`.
- **Raw files:**
  `reports/reviews/2026-11-26-dispersive-horizon-channels-amendment1-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** one cross-family agent review (author Claude, reviewer
  OpenAI, the same house and model as the previous round). It is not human
  review. Astra could not run code and marks the execution, the git bytes,
  the commit precedence and the single-run claim `[UNVERIFIED]`.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 C2 count between thresholds | PASS |
| 2 C3–C5 deliverables | PASS |
| 3 Published values and provenance | PASS |
| 4 det G_x with varying profile | PASS |
| 5 Text coherence | REPAIR_REQUIRED (editorial) |
| 6 Closure | PASS: `CHANNELS_CLASSIFIED` |
| Global | **PASS** |

## What Astra checks by hand

- **C2.** The position of p₁: Im p₁ = 100/2501 < 1/20 < Im z_c*. The arc
  permutation under conjugation and negation, and the per-arc constancy,
  with side counts across collision points.
- **C3.** The z_c* enclosure in the report matches the (1, −1) row of Z digit
  by digit.
- **C4.**
  - The assignment logic: each box holds one root of N, and excluding 0 for
    one factor assigns the root to the other.
  - Sturm forces the four circle roots into the remaining boxes.
  - **Independent check of the factor assignment.** The λ¹¹ coefficient of
    P(·, z₀) is zero, so the twelve roots sum to zero. The imaginary parts of
    the logged evanescent pairs cancel those of the propagating roots, and no
    alternative assignment compatible with reciprocity comes within 0.03.
- **C5.** N^H G N = F/|F| = sign v exactly. The interval check is a
  consistency check, and `same_F` compares with C5 re-run in the same
  import.
- **det G_x.** Congruence: det G_x = |det T|²(−1)⁷ = −cot²β₆(x).

## Residual objections and disposition

Each was checked against the report and the run log before acting.

1. **Minor. Precision wording in C5 [A1].** The printed τ intervals have width
   10⁻²⁰; 10⁻⁴⁵ is the internal tolerance. The 10⁻¹⁰ bound applies to
   Re N^H G N. The table values are 6 significant digits. **Upheld and
   applied:**
   - "refined internally to tolerance 10⁻⁴⁵, printed outward-rounded to 20
     decimals";
   - the real and imaginary parts are stated separately;
   - "6 significant digits";
   - F is compared with "the C5 computation re-run in the same import".
2. **Minor. Verifier predicates.**
   - `to_CI` applies `nsimplify` to coefficients already in ℚ(i), without
     checking equality with the original.
   - The V quotient test `.is_number` would also accept the constant 0.

   **Upheld, not applied to code.** Changing the verifier would change bytes
   under review. Astra states that neither weakness changes the recorded
   assignments or quotient, and its hand check of the root sum confirms the
   assignment independently. Recorded here as known limits of verifier
   `ea3067a`.
3. **Wording. C2 table and C4 mirror pairing.** **Upheld and applied:**
   - the C2 table is stated "at regular levels only";
   - in C4, "the enclosure of its image under 1/λ̄ meets exactly one outside
     box; by the C2 symmetry, that box contains the partner root".

H compares the hashes after `exec_module`. A mismatch would still make the
amendment verifier fail, but only after the imported file had run. Astra
accepts this as sufficient for the recorded run. It is noted here.

## Outcome

The channels execution with Amendment 1 passes review. Under the frozen
charter the verdict is **`CHANNELS_CLASSIFIED`**. Reviewed by one house
(OpenAI, two rounds); not promoted.

On I = (arg z_c*, π/2) each medium has 4 propagating channels (1 right, 3
left) and 4 + 4 evanescent ones, with a certified flux form and unit-flux
normalized modes. The full-line problem has 4 incoming and 4 outgoing
channels. The incident and transmitted right-moving channels are each
unique on I. They are not unique in the interior near ω ≡ 0 (mod π).

TRANSMISSION = OPEN; NOVELTY = OPEN. Promotion, a transmission charter and a
merge to `main` are separate user decisions.
