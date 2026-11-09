# DISPERSION_L3_ROW — frozen contract

**Status of this text:** frozen at the commit that introduces it; that
commit is the preregistration commit. Nothing computed before it.
**Authorization:** user instruction of 2026-11-04, «autorizado a L3», in
reply to Erratum 1 of the dispersion gate
(`theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_ERRATUM_1.md`, Sec. 4: «No
dispersion entry is computed for the standard-battery L3. That would need
an authorized computation»). Read by the author as authorizing this
computation; the user may withdraw that reading.
**Parent:** `DISPERSION_CORRECTIONS_ACROSS_LATTICES` (preregistration
`a7ff5b7`, promoted, CS Sec. 13). This contract adds the one parent row of
`C_ACROSS_LATTICES` (l. 76) that the dispersion gate did not compute. It is
a revision of the dispersion gate restricted to that row; nothing else of
the parent is recomputed or changed.
**Initial scientific status: OPEN.**

## 0. Single question

> For the standard d = 3 Weyl battery (row L3 of `C_ACROSS_LATTICES`),
> what is the exact lowest-order correction to the massless dispersion,
> its order, sign and angular pattern, under the parent's definitions?

## 1. Row and symbols

Row L3, `s = 2`, `d = 3`. The four symbols certified by
`scripts/verify_weyl_dirac_gate.py` (`verify_case`, l. 137–149), imported
read-only:

| Case | Symbol |
| --- | --- |
| A+ | `published_symbol(3, +1, z)` |
| B+ | `published_symbol(3, +1, z).T` |
| A− | `published_symbol(3, −1, z)` |
| B− | `published_symbol(3, −1, z).T` |

`z_j = e^{i k_j}` (sign `sigma = +1`, as the parent uses for L1 and L2),
generators the unit vectors, support `{±1}^3`, normalization as the
parent: longest step `sqrt3` → 1, one update per time unit; expected
`c_0 = 1/sqrt3` (CS Sec. 5).

## 2. Quantities and method

Exactly the parent's quantities (parent contract Sec. 3) and method: the
node quadratic factor `lambda^2 − tr U lambda + det U`; `omega^2`, `phi`;
along rays `eps_+ − eps_0 = c_0 t [1 + beta(n) t + alpha(n) t^2 + …]`;
`beta`, `alpha` exact, with cubic projections (`alpha_0`, `K4`, `K6`,
`n1 n2 n3`); `G_walk` among the 48 signed permutations. Taylor degree
`N = 4`, as the parent uses for its d = 3 rows. Scale of validity and
`V_grp^max` are not attempted (OPEN, as in the parent).

The helpers of `scripts/verify_dispersion_corrections_gate.py`
(`taylor_symbol`, `analyse_block`, `walk_group`, `point_group`,
`laurent_matrix_from_p`) and the symbols of
`scripts/verify_weyl_dirac_gate.py` and
`scripts/verify_directional_saturation.py` are imported read-only. No
reviewed byte is changed. New verifier:
`scripts/verify_dispersion_L3_row_gate.py`, fail-closed, exact.

## 3. Hypotheses, stated before solving

Author's reading of the code before computing (recorded so that it is a
prediction, not a fit). For `s = 2` with `det U = 1` the characteristic
polynomial is fixed by `tr U = 2 × scalar`. The scalar of
`published_symbol(3, chi, ·)` is `ccc + chi sss` (`verify_weyl_dirac_gate.py`
l. 68). The half-trace of CJWW (5.12), as transcribed by `walk1()`, is
`ccc + sss` (`verify_directional_saturation.py` l. 81, Amendment 1 of the
phase-0 gate, Sec. 2). Transposition preserves trace and determinant.

- **HL3a.** `det U = 1` and `tr U = 2(ccc + chi sss)` exactly for all
  four cases.
- **HL3b.** A+ and B+ have the same `(beta, alpha)` and `G_walk` as the
  parent's row printed «L4» (CJWW (5.12), `walk1()`), recomputed here with
  the same helpers.
- **HL3c.** A− and B− have `beta` of opposite sign to A+ and the same
  `alpha`, and the same `(beta, alpha)` as L5a.
- **HL3d (parent He for L3).** The lowest nonvanishing correction is
  anisotropic.
- **HL3e (parent Hd for L3).** `alpha_0 < 0`.

## 4. Verdicts

- `L3_DISPERSION_COMPLETE` (all quantities of Sec. 2 except the two OPEN
  ones) or `L3_DISPERSION_OPEN_<reason>`.
- Per hypothesis: `CONFIRMED` / `REFUTED`.
- Consequences for the parent's He and Hf are recorded, not re-decided:
  He coverage of row L3 (Erratum 1, Sec. 3 item 2), and any shared
  `(beta, alpha)` pair on the BCC substrate.

## 5. Stop rules and exclusions

- Stop when the four cases are filled or marked OPEN with reason.
- No numerics, no fitting, no new walk, no change to the parent table.
- No physical interpretation, no claim about our universe, no novelty
  claim.

## 6. Deliverables

- `reports/2026-11-04--dispersion-L3-row.md`.
- `scripts/verify_dispersion_L3_row_gate.py`; its two exact command forms
  in `.claude/settings.json`.
- Cross-family review before any promotion; promotion is a separate user
  decision.
