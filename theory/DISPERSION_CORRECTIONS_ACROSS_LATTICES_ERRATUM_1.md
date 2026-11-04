# DISPERSION_CORRECTIONS_ACROSS_LATTICES — Erratum 1 (row labels L3/L4)

**Date:** 2026-11-04. **Author:** Claude (Anthropic). **Status: DRAFT,
PRELIMINARY**, pending cross-family review and user approval.
**Authorization:** user instruction of 2026-11-04 («haz la 4 y la 3»),
option 3: a dated erratum with a short review. **Base:** `200f221`.

This erratum changes no byte of the frozen contract
(`theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md`, preregistration
`a7ff5b7`), of the report
(`reports/2026-11-02--dispersion-corrections-across-lattices.md`) or of
the reviewed verifier (`scripts/verify_dispersion_corrections_gate.py`,
SHA256 `b7c451e2…`, last change `4a45280`). Nothing is recomputed. It
records what the rows labelled L3 and L4 actually contain and which
promoted statements of `state/CURRENT_STATE.md` Sec. 13 that affects.

## 1. The inconsistency

| Source | Row L3 | Row L4 |
| --- | --- | --- |
| Parent `C_ACROSS_LATTICES_GATE.md` l. 76, 78 | standard battery, BCC `N_3` | CJWW (5.12) **and** (5.15), `Z^3` label, `C_micro = [-1,1]^3` |
| Dispersion contract l. 63, 67 | `walk2()` = CJWW (5.15), «BCC» | `walk1()` = CJWW (5.12), «cube `[-1,1]^3`» |
| Verifier l. 573–576 | `DS.walk2()`, substrate «cubic» | `DS.walk1()`, substrate «cubic» |

`scripts/verify_directional_saturation.py` l. 64–65 and 72–73 confirm
`walk1()` = CJWW (5.12) and `walk2()` = CJWW (5.15).

Substrates under phase-0 Sec. 2.3 (generated translation group plus step
set), from Amendment 1 of the phase-0 gate, Sec. 2 item 4 (hand
derivation, re-derived by gpt-6.1-sol, PASS):

- CJWW (5.12): support `{±1}^3`, generated group BCC.
- CJWW (5.15): generated group `Z^3`.
- Both have `C_micro = [-1,1]^3`.

So the dispersion gate:

- put a CJWW walk, (5.15), in the slot of the parent's standard-battery
  row L3;
- labelled it «BCC», although its generated group is `Z^3`;
- labelled (5.12) «cube», which is right for its hull but not for its
  group, BCC.

The verifier followed the contract as frozen. The defect is in the
contract's row table relative to its parent, not in the execution.

## 2. What stands

- **Per-symbol results.** Every coefficient in the report table (l. 38–50)
  is a result for the symbol the verifier imported. Under the corrected
  labels:
  - the row printed «L3» (`O_h`, `alpha = −sigma2/18`, `alpha_0 = −1/90`)
    is **CJWW (5.15)**;
  - the row printed «L4» (`T_d`, `beta = −(sqrt3/3) n1 n2 n3`, `alpha` as
    L5a) is **CJWW (5.12)**.
- **Findings unaffected by the labels:**
  - which rows have a `beta` term (inversion-free walk group);
  - harmonic content against `G_walk`;
  - Hd (`REFUTED_BY_ROW_L1`; L3s4 range);
  - Hf refuted by L2 = L6e on the square.

## 3. What changes

1. **Coverage.** The parent's row L3 (standard d = 3 battery,
   `verify_weyl_dirac_gate.published_symbol(3, ·, ·)`) has **no dispersion
   entry**; the verifier imports `published_symbol` only for d = 1, 2
   (l. 560, 562). Both computed CJWW rows belong to parent row L4. The
   phrase «the thirteen massless rows of Sec. 11» in CS Sec. 13 overstates
   coverage by one row.
2. **He.** The listing «L3 `K4`» in CS Sec. 13 (l. 2449–2450) is evidence
   for CJWW (5.15), i.e. parent row L4. He is **not checked** for the
   parent's row L3. The verdict `CONFIRMED_IN_DECLARED_ROWS` therefore
   holds for the declared rows except the standard-battery L3.
3. **Hf substrate grouping.** Contract l. 142 and verifier l. 811 compare
   «BCC: L3, L5a, L5b», where «L3» is CJWW (5.15) on `Z^3`. With the
   groups of Sec. 1:
   - the BCC substrate carries L5a, the two Weyl blocks of L5b, and CJWW
     (5.12);
   - (5.15) is the only computed row on `Z^3`.

   From the report table, by hand, not compared by the verifier: CJWW
   (5.12) has `beta = −(sqrt3/3) n1 n2 n3` and `alpha` as L5a, so it has
   the same `(beta, alpha)` as the L5b Weyl block whose `beta` sign is
   opposite to L5a's, through the orders the table records. This is a
   further shared pair on BCC. Report l. 81 and l. 263 («on the … BCC
   substrates the corrections are not all equal») remain true with the
   corrected membership: L5a and (5.12) differ in the sign of `beta`. The
   verdict `REFUTED_BY_ROW_L6e` is unchanged.

## 4. Not done here

- No dispersion entry is computed for the standard-battery L3. That would
  need an authorized computation (user decision).
- Whether CJWW (5.12) or (5.15) coincides with an L3 symbol up to the
  declared symmetries is not checked (as in Amendment 1, Sec. 2 item 4).
- The verifier and the report are not edited. CS Sec. 13 receives a
  dated note only after this erratum is reviewed and approved.
