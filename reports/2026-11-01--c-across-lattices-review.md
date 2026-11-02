# Independent reviews of the c-across-lattices execution

Date: 2026-11-01. Branch: `research/schur-stability-audit`.
Reviewed snapshot: base `aab5e7b`; report
`reports/2026-11-01--c-across-lattices.md`, verifier at `cae6e30`
(SHA256 `1da30dab9060c8d97a4452eb07451f7886325f4fd87ce22a27cdd950dfee9645`),
contract preregistered at `30672ba`.
Status: **REPAIR_REQUIRED (Grok) / PASS (Gemini)**. Not promoted.

## Execution

User instruction «si, con ciro y gemini». Two sealed `revision-ciega` runs
in parallel, same request body and same nine documents (contract, report,
verifier, `verify_weyl_dirac_gate.py`, and the PDFs 1803.01015v2,
1803.01304v1, 1802.03910v1, 1312.2852v1, 1708.00826v2). Identical input
SHA256 `c062bab84ef1010241d29895dc4a0e959e03583660d664b8b73162cc25a2944a`.
Neither saw the other. Generation was probed for both beforehand. Tools
commit `ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.

| House | Model, route | Window (UTC) | Exit | Review SHA256 |
| --- | --- | --- | --- | --- |
| ciro (xAI) | grok-4.7, grok CLI 1.0.70 sealed | 22:14:09–22:29:02 | 0 | `ea960b3d5aea845e37e217e5e66dfd6774ed831bed02905abeec7799e1c42001` |
| gemini (Google) | gemini-4-argon, generateContent, thinkingLevel medium, no tools | 22:14:09–22:16:24 | 0 (`STOP`) | `feb54b7cc85625d4445affda3e519b6cf34017e4e77dc380b924d1b557c1fbe5` |

Raw files are in `debates/2026-11-01--c-across-lattices-review/`. The author
is Claude (Anthropic), so both are cross-family. Neither reviewer ran code.

## Verdicts

| Block | Grok | Gemini |
| --- | --- | --- |
| SOURCE_READING | PASS | PASS |
| STEP_SETS | PASS | PASS |
| MASSLESS_SPEEDS | PASS | PASS |
| STRICT_BODY | PASS | PASS |
| MASSIVE | PASS | PASS |
| SCOPE_AND_CODE | **REPAIR_REQUIRED** | PASS |
| Global | **REPAIR_REQUIRED** | PASS, no mandatory repairs |

Both reconstruct independently the step sets and same-substrate
identifications, the massless `c_0` values, the vertex argument and the
massive Gram/curvature conclusions.

## Mandatory repairs (Grok), all accepted by the author

1. **Table values not asserted.** `c_0`, `r_in`, `g_rel`, `K` are printed,
   not checked by `record`; a different value would still exit 0. Repair:
   an exact `record` for every certified table entry.
2. **Report Sec. 2 overclaims.** The continuum-speed agreement does not
   test the `prod_j` order of JDW Eqs. (2), (8): with `W_j(0) = I` the linear
   term is the sum of derivatives, independent of order. The order stays a
   declared convention and may affect `K` and vertex coefficients.
3. **Hb/Hc tokens.** `CONFIRMED_IN_DECLARED_ROWS` while declared row L6b is
   `OPEN` exceeds the frozen vocabulary. Repair: state that Hb and Hc hold
   in every decided row, with L6b OPEN.

## Clarifications (non-blocking)

- Both houses: the identity `i dU U(0)^dag = X_par + (sin theta/theta)
  X_perp` is incomplete; by Duhamel the anticommuting part carries a
  unitary factor, `X_par + (sin theta/theta) X_perp e^{i theta Q}`. The
  computed object is `X_perp e^{i theta Q}`, which is Hermitian,
  anticommutes with `Q` and has the same Gram matrix; no number changes.
  The author confirms this.
- Grok: "two substrates" in 2D flattens the finer translation group of
  L6c (same `C_micro`, different group); the script docstring says Parts
  2–3 are not implemented; the Fourier sign is `k -> -k` relative to
  JDW's plane wave, which does not affect the even quantities tabulated;
  `iso_W` means `K = 0`, not `K` scalar.

## Next step

Repair the verifier and report, then a bounded re-review of the repaired
snapshot. No promotion before that.

## Bounded re-review of the repaired snapshot (2026-11-01)

User instruction «si, autorizado». Repaired snapshot `8d0276e`; request,
diff `aab5e7b..8d0276e` of the verifier and report, and raw outputs in
`debates/2026-11-01--c-across-lattices-rereview/`. Documents: contract,
this review record, the diff, the repaired report and verifier. Same
input to both houses, SHA256
`28f6c9ded4da3a99f308e5c6f5ad7dc48652196bf54b9a40f11235b647f09a27`.
Scope: the three repairs (R1–R3), the clarifications (R4) and regressions
(R5); blocks 1–5 not reopened unless the diff altered them.

| House | Outcome |
| --- | --- |
| gemini (gemini-4-argon) | COMPLETED (`STOP`), 22:33 UTC. **PASS on R1–R5; no mandatory repairs.** Review SHA256 `6672ed508bb20920f8c75003f3c905ea03016331512aa08db7805d87f757f3c0` (file `informe_gemini.md`). |
| ciro (grok-4.7) | **FAILED, ausente**: `API error (status 402 Payment Required): Grok Build usage balance exhausted` (`grok.log`). Account-level failure, so no descent of the Grok model ladder; no verdict. |

Consequence: Grok's three mandatory repairs were applied by the author
and checked by Gemini, not by Grok. The repaired snapshot has one bounded
cross-family re-review PASS (Gemini) on top of the first-round Gemini PASS;
Grok's acceptance of its own repairs is not on record.

## Grok re-review of the repaired snapshot (2026-11-02)

After the Grok account balance was restored, Grok reviewed the repaired
snapshot `8d0276e` with the same bounded request as on 2026-11-01, blind
to the Gemini re-review (it received this record as it stood at
`8d0276e`). Raw files in
`debates/2026-11-02--c-across-lattices-rereview-grok/`; `grok-4.7`,
08:02:29–08:12:10 UTC, exit 0; review SHA256 `a57b20bcb31c32e5cccb8d8b983cab8073b576992a5951468d3a1471794caaf8`. Before sending, the
report and verifier were checked byte-identical to `8d0276e`.

**Verdict: PASS on R1–R5, no mandatory repairs.** Grok's acceptance of its
own three repairs is now on record. One non-blocking observation: the
report's Sec. 9 still names the verifier at `cae6e30`, which the header
identifies as the pre-repair version.
