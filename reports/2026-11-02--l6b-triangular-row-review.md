# L6b triangular row — independent reviews

**Date:** 2026-11-02
**Reviewed candidate:** `reports/2026-11-02--l6b-triangular-row.md` (SHA256
`201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c`) and
`scripts/verify_l6b_triangular_row_gate.py` (SHA256
`c2e91c237b023abde1199f8ef3bea143f49e559da35899c01e049a9ddf3f2441`), at
commit `a19e480`, against the contract `theory/L6B_TRIANGULAR_ROW_GATE.md`
(`b076670`). Also sent: the parent verifier (read-only import) and the ADMP
source as text extracted from the PDF, **without Fig. 1**.
**Tool:** `revision-ciega` (`~/herramientas` `ce09890`), sealed, no tools;
identical input to both houses (input SHA256
`37568e67f30cb8437107f374cfc61ddb53664f7c9040e81d21eae4162c50be3c`).
**Authorization:** user, «adelante» (2026-11-02).

| House | Model | Blocks 1–6 | Global | Mandatory repairs | Record |
| --- | --- | --- | --- | --- | --- |
| Gemini | gemini-4-argon | PASS ×6 | PASS | none | [`debates/2026-11-02--l6b-review-gemini/`](../debates/2026-11-02--l6b-review-gemini/informe_gemini.md) |
| Grok | grok-4.7 | PASS ×6 | PASS | none | [`debates/2026-11-02--l6b-review-grok/`](../debates/2026-11-02--l6b-review-grok/informe_grok.md) |

Both reviewers reconstructed the labelling from the text alone (Fig. 1 was
not in their input), the six admissible assignments, the step set, the node
structure `U(0) = P ⊗ W`, both routes to `c_0 = 1/3`, the limsup argument
for `c_strict^iso = 1/sqrt3`, and the 60° rotation behind the L6a
cross-check. Both judged the change from the identity isometry to the
twelve isometries of the hexagon legitimate, not post hoc. Gemini supplied
the algebraic identity linking routes A and B
(`Q^dagger (i d_k U^3(0)) Q = 3 G_a`).

Non-blocking clarifications (no entry or verdict changes):

- Grok: several checks are weak or structural (`U.rows == 6`, `W^3 = I`,
  the similarity check of Eq. (11)); the content is in `hull`, `nilpotent`,
  `node_speeds` and the external anchors (source coefficient `sqrt3/6`,
  L6a support, agreement of four variants). Agreement of routes A and B
  does not by itself exclude a common scale error; the source coefficient
  does. Equality of characteristic polynomials fixes the dispersion, not an
  operator equivalence or equality of coins; the contract asks for no more.
- Gemini: `ccw_successor` orders three exact angles by `float`; the angles
  are `2π/3` apart, so no ambiguity, but a sign-of-cross-product test
  would be fully symbolic.

Neither is human review. Nothing is promoted by this record; promotion is
a separate user decision (contract Sec. 8).
