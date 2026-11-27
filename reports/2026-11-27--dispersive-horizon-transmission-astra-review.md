# Astra review of the dispersive-horizon transmission execution

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`. Reviewed at
`d5a944d` (brief committed at `729e810`).

**Reviewed snapshot** (SHA256 of the copies sent, from the provenance header
of `informe_astra.md`):

| Document | Last commit | SHA256 |
| --- | --- | --- |
| `theory/DISPERSIVE_HORIZON_TRANSMISSION_GATE.md` | `8eb8be5` | `917920140e2fb29a9dce5db8f8ae53345e6129b70ee9103d43efc4b5a3670117` |
| `reports/2026-11-26--dispersive-horizon-transmission.md` | `a189db3` | `40adae1e914a53f17c739598ca8e2ed99fad5d3d3e64f3d91eabe9f51ab519cd` |
| `scripts/verify_dispersive_horizon_transmission.py` | `0959251` | `29ee9f127b2e43dc1a8aabf2cfdffb6e727edf502e9677b823f45b7c27e316ea` |
| `scripts/verify_dispersive_horizon_channels.py` | `a5b9be3` | `08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc` |
| `scripts/verify_dispersive_horizon_transfer_matrix.py` | `d0114b2` | `98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2` |
| run-2 log | `a189db3` | `889cd5cd2b03a39992bbf9c8b3af53b5aab8266fc22f17df78256bd1720c1e12` |
| run-1 log (interrupted) | `0959251` | `29a6975782bc0b385f2f0399dd4951dd2cccf3ee810263fe339427e1e4feb505` |

**Status:** Astra **REPAIR_REQUIRED** (global). Both
`TRANSMISSION_NONZERO_CERTIFIED` verdicts and T0 = CONNECTED stand for the
sharp profile. The repairs concern the physical interpretation at z₁ and the
documentation; they are applied as Amendment 1 of the transmission report
(marked [A1]). The verifier is not changed. Not promoted.

## Execution

- **Authorization:** user «Yes, send» (2026-11-27), in answer to the question
  whether to send the brief; the model is fixed by the charter (Q4).
- **Model:** `gpt-6.2-astra`, effort high, codex-cli 0.172.0, via
  `ASTRA_MODEL=gpt-6.2-astra revision-ciega astra`. A probe returned "OK"
  beforehand.
- **First launch** rejected locally before sending (the brief lacked its
  closing `---`); log kept as `lanzador-intento1-rechazo-local.out`. Nothing
  was sent in that attempt.
- **Run:** 2026-11-27 07:13:58–07:17:00 UTC, status `COMPLETED`, exit 0.
- **Hashes:** input SHA256
  `ed3e401cf3ef2fd274f69c459a35f8e2016184ac62691c9714bc0295f4f02905`; response
  SHA256 `ee2c25594ac08ebfc0b092aa6af0ab5b36fc0e12cdf535e93bf70df959d036c7`.
- **Raw files:** `reports/reviews/2026-11-27-dispersive-horizon-transmission-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** one cross-family agent review (author Claude, reviewer
  OpenAI). Not human review. Astra could not run code; it takes decimal
  endpoints, the discriminant degree and the Sturm counts from the run-2 log,
  and marks the correspondence of the attachments with the repository bytes
  `[UNVERIFIED]`.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 Bloch vector and closure rows | PASS |
| 2 Krawczyk roots and classification | PASS |
| 3 T0 branch continuity | PASS |
| 4 T1 existence, bound states, Tarasinski count | PASS |
| 5 T2 and T4 transmission | PASS |
| 6 Physical interpretation at z₁ | REPAIR_REQUIRED |
| 7 Verdicts, scope, process | REPAIR_REQUIRED |
| Global | **REPAIR_REQUIRED** |

## What Astra derives by hand (summary, not a source)

- **Point 1.** The stage variables of a Bloch solution are
  Y_x = λ^x(a₁,…,a₆, b₁/λ,…,b₆/λ)ᵀ. They satisfy the stage and closure
  equations whose unique solution is Y_{x+1} = M Y_x, and also
  Y_{x+1} = λY_x. This proves closure rows 0 and 11 in general, including for
  evanescent modes. The 9 samples are transcription checks.
- **Point 2.** The Krawczyk inclusion K ⊂ int X gives a root in each box.
  Twelve disjoint boxes for a degree-12 polynomial give all roots, simple.
  The undecided boxes equal the Sturm count, so they are the unit roots.
- **Point 3.** A′(t) = 4t − 1 > 0 on the profile interval; the leading
  coefficient 8/5 is h at k = π. Simplicity excludes band collisions at z₀
  (a collision would force U(k) = z₀I and a double root). Hence there is one
  right-mover for each t, and k ≈ 1.231 continues to k ≈ 1.107.
- **Point 4.** Neumann bound for the verified solve; unitarity from flux
  conservation and flux-orthogonality of distinct propagating modes; the
  Tarasinski count from the rank of the 1 × 3 block r′, with
  tr(t′ᴴt′) = 2 + T.
- **Point 5.** The indices select the right channels. The block is the
  1 × 2 row B = (t₁, t₂); σ² = BBᴴ.

## Objections and how they are handled

1. **Main, T4 "Interpretation".** The 96.05 % is the maximal transmission
   from a unit-flux interior superposition into the exterior low-k mode, and
   the interior weight of that row of S. Incidence ∝ (t₂, −t₁)ᵀ transmits
   zero. "96.05 % of the outgoing flux comes from the doublers" holds only
   for an incoherent preparation with equal flux in every incoming channel.
   **Applied [A1]:** the sentence is replaced, with the incoherent reading
   stated as a condition.
2. **Scope, T4 and "Answer".** List the channels by medium, flux sign and
   approximate k. Add the sheet argument if the infrared identification is
   kept. Present "doublers" and the analogy as interpretation, and limit
   "certified" to the sharp-profile scattering block at z₁. **Applied [A1].**
   The sheet argument was checked by the author by hand from the logged
   boxes (see Amendment 1 of the report). It shows that the interior
   member of the low-k sheet is k ≈ −0.083, not k ≈ −0.027. The original
   table was ambiguous on this.
3. **Documentation.** Say that the verifier checks closure rows at 9 sample
   points, with the general proof written. Reproduce rectangular enclosures
   where "∈" is used. Distinguish B, σ and σ². **Applied [A1]** in the
   report and in `scripts/README.md`. The verifier header is **not** changed:
   its bytes are those reviewed, and the repo rule forbids changing a
   reviewed verifier without a new review. The README and report now carry
   the clarification.

Astra also notes that the program can record an `OPEN` outcome through
`ok(…, True)`, so the decision lines must be read. In run 2 both decision
lines say `TRANSMISSION_NONZERO_CERTIFIED`. Recorded, verifier not changed.

## Outcome

After Amendment 1, the verdicts under the frozen charter are:
- z₀: `TRANSMISSION_NONZERO_CERTIFIED`, T0 = CONNECTED (continuation within
  the family of homogeneous media; T itself is that of the sharp step).
- z₁: `TRANSMISSION_NONZERO_CERTIFIED` for the 1 × 2 block from the two
  interior right-movers to the exterior right-mover.

Amendment 1 is editorial and has **not** been re-reviewed. One reviewing
house (OpenAI). Not promoted. TRANSMISSION remains OPEN outside the two
points; NOVELTY = OPEN.
