# Dispersion corrections: row L3 (standard d = 3 Weyl battery)

**Date:** 2026-11-04. **Author:** Claude (Anthropic). **Contract:**
[`DISPERSION_L3_ROW_GATE.md`](../theory/DISPERSION_L3_ROW_GATE.md),
preregistration `d3868fa`. **Verifier:**
`scripts/verify_dispersion_L3_row_gate.py`, SHA256 `1beb8fd9…` (full hash in
the commit that adds this report), 34/34 exact checks, `python3 -B`, sympy
1.14.0. **Status: PRELIMINARY**, not independently reviewed, not promoted.

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

**Second route.** HL3b and HL3c also follow without the expansion. For
`s = 2` with `det U = 1` the characteristic polynomial is fixed by `tr U`.
`tr U` equals `2(ccc + sss)` for A+, B+ and for CJWW (5.12)
(`verify_directional_saturation.py` l. 81). `chi = −1` is `k -> −k` of
`chi = +1`, which flips `beta` (odd order) and keeps `alpha` (even). The
expansion agrees with this.

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
  pairs: L3 A± with CJWW (5.12) and with L5a (and the L5b blocks, through
  the parent's table). Hf was already `REFUTED_BY_ROW_L6e`; this adds
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
- No promotion. CS Sec. 13 is not changed by this report; a note would
  follow review and a user decision, together with Erratum 1.
