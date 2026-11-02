# Dispersion corrections across lattices — independent reviews

**Date:** 2026-11-02
**Reviewed candidate:** `reports/2026-11-02--dispersion-corrections-across-lattices.md`
(SHA256 `6f0f9394c73b13dd62e3f1034cbeec187824c91c54a26c180d03dbabca45203e`)
and `scripts/verify_dispersion_corrections_gate.py` (SHA256
`791f0d80d2790f34b72521c90622fa0056fd629fa1b3ef89addfc2ad664e6c2a`), at
commit `9557aa9`, against the contract
`theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md` (`a7ff5b7`). Also
sent, read-only: the five scripts the verifier imports symbols from
(`verify_c_across_lattices_gate.py`, `verify_weyl_dirac_gate.py`,
`verify_directional_saturation.py`, `cert_Aa_s4_counterexample.py`,
`verify_l6b_triangular_row_gate.py`). Not sent: `.claude/settings.json`.
**Tool:** `revision-ciega` (`~/herramientas` `ce09890`), sealed, no tools;
identical input to both houses (input SHA256
`5859cd5784e9882225d85484b267e203fbde162f70e6e344a6b7d17579714843`).
**Authorization:** user, «adelante» (2026-11-02). One round.

| House | Model | 1 SERIES | 2 BLOCKS | 3 SYMMETRY | 4 VALUES | 5 HYPOTHESES | 6 SCOPE_AND_CODE | Global | Mandatory repairs | Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini | gemini-4-argon | PASS | PASS | PASS | PASS | PASS | PASS | PASS | none | [`debates/2026-11-02--dispersion-review-gemini/`](../debates/2026-11-02--dispersion-review-gemini/informe_gemini.md) |
| Grok | grok-4.7 | PASS | PASS | PASS | REPAIR_REQUIRED | PASS | REPAIR_REQUIRED | REPAIR_REQUIRED | three | [`debates/2026-11-02--dispersion-review-grok/`](../debates/2026-11-02--dispersion-review-grok/informe_grok.md) |

Both reviewers reconstructed by their own route the series method, the
`L5b` splitting by `Gamma`, the exactness of the zero test with
`b^2 = 1 - a^2`, the power-trace definition of `G_walk`, the degree
argument of contract Sec. 1, and the closed forms for L2, L3, the chiral
BCC rows and L6a. Both confirm the L6b/L6a relation (`c_0` by 2/3, `beta`
by 2, `alpha` by 4, 60° rotation), the root `a*` of L3s4, and the three
hypothesis verdicts against the contract text. Gemini also rederived
`alpha = -1/128` for L6d; its derivation corrects a sign midway. Grok
derived `phi = ±(1-a^2) t^2/6` for L3s4 by a Schur complement between the
clusters, and did not rederive L6c, L6d, L6f, the `t^4` harmonics or the
eight elements of L3s4's group.

Grok's mandatory repairs, each checked here before acceptance:

- **R1 (report Sec. 3.3).** The sentence saying that every row with
  `beta != 0` has an odd lowest correction taking both signs is false for
  L3s4. There `beta = beta_0 + beta_3 n1 n2 n3` with
  `beta_0 = ±sqrt3 (1-a^2)/(6a) != 0`. Since `|n1 n2 n3| <= 1/(3 sqrt3)`,
  `beta` keeps the sign of `beta_0` iff
  `|2a^2 - 1| < (3 sqrt3/2)(1 - a^2)`, that is `a^2 < (19 - 6 sqrt3)/11`.
  Checked: correct. **Accepted.**
- **R2 (report Sec. 1).** "L5a with each Weyl block of L5b" is false: the
  two blocks have opposite `beta`, and the verifier lists only the pair
  with the `+i` block. **Accepted.**
- **R3 (verifier, Part 4).** The record "Hd: the sign of alpha0 is decided
  exactly in every row" has the constant predicate `True`. Gemini made the
  same observation as a non-blocking clarification. **Accepted.**

Non-blocking clarifications: the values of L6c, L6d, L6f and the orders
of `G_walk` are printed, not recorded (Grok; it asks not to hard-code
them); `omega = c_0 |k|` is not analytic at `k = 0`, the ray expansion is
(Grok); the `float` calls only order roots and pick a rational sample
point whose position is then checked exactly (Gemini).

**Repairs applied (2026-11-02).** R1 and R2 in the report (Secs. 3.3, 1,
listed in its Sec. 5); R3 in the verifier, which also gains an exact check
of the R1 threshold (`beta0^2 - beta3^2/27 = (11a^4 - 38a^2 + 23)/(324a^2)`,
single root `a^2 = (19 - 6 sqrt3)/11` in `0 < a < 1`). Verifier SHA256
`b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e`, 81/81; its output differs from the reviewed run only in those
three records and the count. Diff:
[`repair.diff`](../debates/2026-11-02--dispersion-review-grok/repair.diff).
No value, table entry or verdict changed.

Neither review is human review. Nothing is promoted by this record. The
verifier's bytes changed, so the repairs need their own review before
promotion.

## Bounded re-review of the repairs (2026-11-02)

**Authorization:** user, «adelante» (2026-11-02). One round per house,
1800 s. **Input:** the contract, this record (as of `4a45280`), the repair
diff, and the repaired report and verifier (SHA256
`b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e`);
identical to both houses (input SHA256
`f4976edfcc8a722b2257ce316528adf2d4086ee98e0f9dfcbb7a5d50d5d3fb6d`).
Snapshot reviewed `9557aa9`, repaired `4a45280`. Tool `ce09890`.

| House | Model | R1 β sign in L3s4 | R2 L5a/L5b sentence | R3 Hd record | R4 regressions | Global | Mandatory repairs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini | gemini-4-argon | PASS | PASS | PASS | PASS | PASS | none |
| Grok | grok-4.7 | PASS | PASS | PASS | PASS | PASS | none |

Record: [`debates/2026-11-02--dispersion-rereview/`](../debates/2026-11-02--dispersion-rereview/).
Both rederived `beta0^2 - beta3^2/27 = (11a^4 - 38a^2 + 23)/(324a^2)` and
the single threshold `a^2 = (19 - 6 sqrt3)/11` in `0 < a < 1`. Both
confirm that the new records can fail and certify what their labels
state, and that the diff changes no value or verdict. Grok checked the
sample values at `a = 1/2` and `a = 19/20` and noted that `beta` vanishes
on the diagonals at the threshold, so the strict "iff" is the right
statement. Grok's acceptance of its own three repairs is now on record.

Status after re-review: **PRELIMINARY, INDEPENDENT_REVIEW_PASS_TWO_HOUSES,
PROMOTION_PENDING (user decision).** Not human review. Nothing promoted.
