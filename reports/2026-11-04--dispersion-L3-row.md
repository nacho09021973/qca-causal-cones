# Dispersion corrections: row L3 (standard d = 3 Weyl battery)

**Date:** 2026-11-04. **Author:** Claude (Anthropic). **Contract:**
[`DISPERSION_L3_ROW_GATE.md`](../theory/DISPERSION_L3_ROW_GATE.md),
preregistration `d3868fa`. **Verifier:**
`scripts/verify_dispersion_L3_row_gate.py`, SHA256 `89b33e700aedb7ae19bb80e00f45d8452f6a550ba7c836c5d3c246f070adae10`,
35/35 exact checks, `python3 -B`, sympy 1.14.0; prints the row verdict
**`L3_DISPERSION_COMPLETE`** (contract Sec. 4). **Status: PROMOTED** by
user decision, 2026-11-05 («adelante»), for these four declared cases;
HL3a–e CONFIRMED. One cross-family reviewing house (OpenAI), not two.
Previous status: PRELIMINARY, not promoted.

**Re-review:** gpt-6.1-sol PASS, no mandatory repairs (`f3b9b10`;
`debates/2026-11-04--dispersion-L3-row-rereview-astra/informe_astra.md`).
Static review; no verifier execution by the reviewer. It supersedes
«not re-reviewed» in the historical first-review paragraph below.

**Review.** gpt-6.1-sol (OpenAI), on the version `1beb8fd9…` (34 checks) at
base `b9b0e58`:
`debates/2026-11-04--dispersion-L3-row-review-astra/`, **REPAIR_REQUIRED**,
three repairs. It re-derived `beta`, `alpha`, `alpha_0` and `G_walk` by
hand and found no error in the coefficients. Repairs applied in this
version, not re-reviewed:
1. the checks of the constructor `row_L5a` now enter the evaluated record,
   and the hypothesis verdicts print «NOT CERTIFIED» if any prerequisite
   check fails (an undecidable sign prints «UNDECIDED»);
2. the script now prints the contract's row verdict;
3. the «second route» of Sec. 3 is restricted to what it proves.

Contract wording, recorded not edited (frozen): «nothing else of the parent
is recomputed or changed» means that the parent table is not changed; two
parent rows, CJWW (5.12) and L5a, are recomputed here only as comparison
controls.

## 1. Why this row

Erratum 1 of the dispersion gate
(`theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_ERRATUM_1.md`, DeepSeek PASS)
found that the parent's row L3 (standard battery, `C_ACROSS_LATTICES` l. 76)
had no dispersion entry. The row printed «L3» in the dispersion report is
CJWW (5.15). The user authorized this computation («autorizado a L3").

## 2. Result

All four cases have `c_0 = 1/sqrt3`, no linear phase, and support `{±1}^3`
(BCC group). Coefficients in the parent's normalization (ray
`k = t n`, `eps_+ − eps_0 = c_0 t [1 + beta t + alpha t^2 + …]`):

| Case | `G_walk` | Lowest correction | `beta(n̂)` | `alpha(n̂)` | `alpha_0` |
| --- | --- | --- | --- | --- | --- |
| A+, B+ | 24, `T_d` (same 24 elements as L5a and CJWW (5.12)) | `beta`, anisotropic | `−(sqrt3/3) n1 n2 n3` | `−4/315 + (7/198) K4 − (1/6) K6` | `−4/315` |
| A−, B− | 24, same set | `beta`, anisotropic | `+(sqrt3/3) n1 n2 n3` | same | `−4/315` |

Residuals of both cubic projections are zero. The `alpha` expression is the
same as the parent's L5a and «L4» entries (`−sigma2/18 − n1^2 n2^2 n3^2/6`,
report l. 44); here it is printed as its projection on `1, K4, K6`.

## 3. Hypotheses (contract Sec. 3)

- **HL3a CONFIRMED.** `det U = 1` and `tr U = 2(ccc + chi sss)` exactly
  for all four cases (asserted checks).
- **HL3b CONFIRMED.** A+ and B+ have the same `(beta, alpha)` and the same
  `G_walk` as CJWW (5.12) (parent row printed «L4»), recomputed in the same
  run with the parent's setup. The recomputed (5.12) reproduces the
  parent's table: `beta = −(sqrt3/3) n1 n2 n3`, `alpha_0 = −4/315`.
- **HL3c CONFIRMED.** A− and B− have the opposite `beta` and the same
  `alpha` as A+, and the same `(beta, alpha)` as L5a (recomputed, matching
  the parent's table: `beta = +(sqrt3/3) n1 n2 n3`).
- **HL3d CONFIRMED.** The lowest correction is anisotropic in all four
  cases.
- **HL3e CONFIRMED.** `alpha_0 = −4/315 < 0` in all four cases.

**Second route (restricted after review, repair 3).** For `s = 2` with
`det U = 1` the characteristic polynomial is fixed by `tr U`. `tr U` equals
`2(ccc + sss)` for A+, B+ and for CJWW (5.12)
(`verify_directional_saturation.py` l. 81), which gives HL3b without the
expansion. The trace for `chi = −1` is the trace for `chi = +1` at `−k`
(an identity of traces, not of matrices), which flips `beta` (odd order)
and keeps `alpha` (even): the first half of HL3c. The comparison of A−/B−
with L5a rests on the expansion only; no trace identity for the L5a symbol
(with `sigma = −1`) is derived here.

These hypotheses were written after the author read the code, before the
run. They are predictions from an exact identity, not independent evidence
about walks in general.

## 4. Consequences for the parent (recorded, not re-decided)

- **Rows with a `beta` term.** The parent's list «L5a, L5b, L4 with
  `T_d`; L6a, L6b with `D_3`; L3s4» (CS Sec. 13) gains the standard L3.
  The parent's statement «`alpha` elsewhere» covered the row printed «L3»,
  which is CJWW (5.15).
- **He.** The coverage gap recorded by Erratum 1, Sec. 3 item 2, is filled:
  the standard L3 (a ceiling row) has a nonzero anisotropic lowest
  coefficient. He holds in all declared ceiling rows of the parent plus L3.
- **Hd.** Unchanged (`alpha_0 < 0` here).
- **Hf.** On the BCC substrate there are further shared `(beta, alpha)`
  pairs: A+/B+ with CJWW (5.12), A−/B− with L5a, and each sign with the
  L5b block of the same `beta` sign (the last through the parent's table). Hf was already `REFUTED_BY_ROW_L6e`; this adds
  coincidences on BCC, which the parent read as «not all equal»: that
  still holds, since `beta` takes both signs.
- **CJWW (5.12).** Same dispersion through relative order `t^2` and same
  `G_walk` as L3 A+/B+. Whether (5.12) equals an L3 symbol up to the
  declared symmetries is still not checked; equal characteristic
  polynomials do not imply equal symbols.

## 5. Not established

- `V_grp^max` and the scale of validity: OPEN, as in the parent.
- Terms beyond relative order `t^2`.
- Any physical reading of `alpha`, `beta`.
- At execution: no promotion; a CS Sec. 13 note required review and a
  user decision together with Erratum 1. Superseded by the dated promotion
  above and the corresponding CS Sec. 13 entry; exclusions unchanged.
