# Astra review of the dispersive-horizon frequency and finite-L execution

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`. Reviewed at
`e8952e3` (brief committed at `d0ce325`).

**Reviewed snapshot** (SHA256 of the copies sent, from the provenance header
of `informe_astra.md`):

| Document | Last commit | SHA256 |
| --- | --- | --- |
| `theory/DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md` | `204f33b` | `5c834a013d4f46a71777b05554b392c1765382feddb1c7f143cd9d53afd998de` |
| `reports/2026-11-27--dispersive-horizon-frequency-finite-l.md` | `e8952e3` | `4dc314e81bbb194ccb8b67da80a2d1eeceeb61b262c9f8b94ebf5aed6083a00f` |
| `scripts/verify_dispersive_horizon_frequency_finite_l.py` | `00f09c9` | `3d585a541663ad7f51a539d728069d228e6a8473772ccc3ca90bb17a8ef80faa` |
| `scripts/verify_dispersive_horizon_transmission.py` | `0959251` | `29ee9f127b2e43dc1a8aabf2cfdffb6e727edf502e9677b823f45b7c27e316ea` |
| run-1 log | `fdbbe8a` | `6a4041fc9b9a18577a98caa477d9fbc3ef78ce2228989c543912a3e719aa00fe` |
| `reports/2026-11-26--dispersive-horizon-transmission.md` | `c832876` | `15b7732d3c3786661207ac75086ba5ac9a9cad7f8e2214e2dcece4516e551211` |

**Status:** Astra **REPAIR_REQUIRED** (global).
- All ten point verdicts of F2/F3 stand (points 3–5 PASS).
- Repairs concern F1 (a), the physical objection, and the line verdict.
- Not promoted.

## Execution

- **Authorization:** user «autorizo la revision de AStra 6.2» (2026-11-27).
  The model is fixed by the charter (Q5).
- **Model:** `gpt-6.2-astra`, effort high, codex-cli 0.172.0, via
  `ASTRA_MODEL=gpt-6.2-astra revision-ciega astra`. A probe returned "OK"
  beforehand.
- **Run:** 2026-11-27 09:20:23–09:24:07 UTC, status `COMPLETED`, exit 0.
- **Hashes:** input SHA256
  `81134a8d9ceaf7230235f2d26e6d7bcaeb5976fe9c4f2bddb1c9bbf120340bc7`; response
  SHA256 `6e8ce2820271f6ee493ea80e3895a8e2d6449eb2a66e3dd02d2e93457dfda35d`.
- **Raw files:** `reports/reviews/2026-11-27-dispersive-horizon-frequency-finite-l-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** one cross-family agent review (author Claude, reviewer
  OpenAI). It is not human review. Astra could not run code, and it takes
  Sturm counts, intervals and timings from the log.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 F1 (a), method | REPAIR_REQUIRED |
| 2 F1 (a), result | REPAIR_REQUIRED |
| 3 F1 (b) | PASS |
| 4 F2/F3 pipeline | PASS |
| 5 Point results | PASS |
| 6 Physical objection | REPAIR_REQUIRED |
| 7 Line verdict and scope | REPAIR_REQUIRED |
| Global | **REPAIR_REQUIRED** |

## Main findings (summary of the reviewer's text; checked by the author where stated)

1. **F1 (a), method.**
   - The critical-value parametrization is exact for the *real* critical
     locus, provided two things are stated:
     - the collisions: f = 0 forces C = 0, giving z = ±i, and the nodes
       u = 1 give z = ±1;
     - the sign recovery: the right-hand sides of cos(ω+k) and sin(ω+k)
       define one angle.
   - It is not the bivariate discriminant the charter's text names. That
     discriminant also detects complex double roots.
   - Closing F1 literally needs either that curve or a post-results
     amendment accepting the equivalent physical locus.
2. **F1 (a), the resultant root is explained.**
   - With h₀ = 1 + 8A, the reviewer states:
     - q(1, A) = ∂_u thr(1, A) = h₀(1 − 4h₀);
     - y_A(1, A) = 0;
     - y_u(1, A) = 1 − 4h₀.
   - So q(1, A_d) = J(1, A_d) = 0 at A_d = −3/32 = A(3/8). That is the
     single logged root of res_u(q, J).
   - **Author check by hand**, using thr = 4(1−u)gp² − 1 + u gt²,
     gt(1) = 1 and gp(1) = h₀:
     - thr_u(1) = −4h₀² + 1 + 8A = h₀(1 − 4h₀);
     - R_u(1) = 2 + 16A − 4h₀ = −2h₀, so y_u(1) = 1 + 2R_u(1) = 1 − 4h₀;
     - R(1, A) ≡ 1, so y_A(1) = 0;
     - h₀ = 1/4 at A = −3/32.

     Confirmed.
   - Together with the logged counts, this gives a written deduction: the
     first-quadrant critical locus is (0, arg z_c*], equivalently
     0 < s ≤ s*.
   - The run output `OPEN_AFTER_DISCRIMINANT_ANALYSIS` stays as the
     historical result.
   - On the classification PASS, the reviewer agrees that it overreaches.
     The labels turn out to be correct by the deduction above, and by F1 (b)
     point by point.
   - Other "ok(…, True)" checks count steps, not conclusions. So 43/43 is not
     43 affirmative scientific results.
3. **F1 (b)** is PASS. CONNECTED is proved point by point at s = 1/4, 1/2
   and 3/4. On the arc a real event must occur (6 real roots on one side,
   4 on the other, constant degree), with the net loss of one right-mover
   and one left-mover.
4. **F2/F3 pipeline** is PASS. The certification is valid.
   - `iv.exp` is interval floating point inside a certified quantity, as F3
     allows. Its validity rests on mpmath's enclosure guarantee.
   - The product has 2N + 2 transfer matrices (66 and 258), as the
     recurrence requires. The charter's "65 and 257 transfer matrices" is a
     counting error in the text: those are profile sites. The precision
     formula was applied with its frozen 2N + 1.
5. **Point results** are PASS. All ten enclosures decide positivity and
   width; the cross-checks decide overlap.
6. **Physical objection.**
   - **Sector argument** (reviewer): at the three low frequencies
     h(0) = 1 − cos ω > 0, h(π) > 0 and h(±π/2) = −1 ± sin ω ≠ 0, so no
     real root changes k-quadrant as the medium varies. The logged boxes
     give:
     - in 0 < k < π/2: one right-mover inside and one outside;
     - in −π/2 < k < 0: one right-mover and two left-movers inside, one
       left-mover outside.

     Hence the turning point (a fold) is located at k < 0, and **the k > 0
     right-mover continues** to the exterior.
   - The approximation k ≈ ω/(8t − 3) is not uniform near 3/8, where the
     sheet goes as ω = (35/32)k³ + O(k⁵).
   - **But σ² ≥ 1/2 is not forced by unitarity.** At the sharp profile at z₁
     the two branches contribute 0.60328 and 0.35726, which argues against
     a purely single-mode reading.
     - *Author check from the reviewed transmission verifier:* `int_in`
       keeps the printing order of the right-movers, and the first one
       printed at z₁ is λ ≈ 0.8278 − 0.5611i (k ≈ +0.596). So
       |t₁|² ≈ 0.603 belongs to the continuing k > 0 branch, and
       **|t₂|² ≈ 0.357 to the k < 0 branch that meets the turning point.**
       The new verifier may enumerate the two in a different order.
   - Attributing the growth of σ² to adiabatic continuity, deducing
     σ² → 1, or identifying any of these numbers with Sabsovich's mixing
     all remain `[UNVERIFIED]`.
   - For the branch question, the observable is
     |S_{ext R, int R(k<0)}|²: unit-flux incidence on the turning branch
     alone.
7. **Line verdict.**
   - In both F3 points, σ²_sharp < σ²_{L=4} < σ²_{L=16} and
     σ²_{L=16} > 1/2.
   - **The charter therefore requires `LEAKAGE_NOT_SUPPRESSED`** for the
     maximal transmission at s = 1/50 and 1/200, L = 16, N = 128.
   - Withholding it after the conditions are met would retroactively change
     the criterion. Adopting it does not authorize promotion.
   - Suggested wording: «The abandonment threshold is met for the maximal
     transmission at both F3 points. The transmission of the incident branch
     that meets the turning point stays open at finite L.»
   - Running from another session does not affect validity.

## How the repairs are handled

- **Repairs 2–4** (objection with the sector argument, F1 (a) deduction and
  deliverable, counting and `iv.exp` wording) are applied to the execution
  report as editorial Amendment 1, marked [A1]. They are not re-reviewed.
  The verifier is unchanged; the classification defect is already in
  `scripts/README.md`.
- **Repair 1 (adopt the line verdict)** reverses the author's
  "not adopted", which the user had accepted. It is **left to the user's
  decision**. The author agrees with the reviewer: the frozen criterion was
  met, and holding the verdict back would move the goalposts after the
  results. In the meantime the report records both positions.
