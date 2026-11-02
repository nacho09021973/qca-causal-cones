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
