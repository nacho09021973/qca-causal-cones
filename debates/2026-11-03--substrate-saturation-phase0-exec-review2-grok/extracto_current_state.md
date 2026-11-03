# Extracto literal de state/CURRENT_STATE.md en el commit 6851d92 (numeración original de líneas a la izquierda; el fichero no ha cambiado desde entonces)

## Líneas 85,112
```
   85  a charter. Chartered the same day by user instruction («haz lo que
   86  consideres, estás autorizado»); executed on «si»
   87  ([report](../reports/2026-11-02--dispersion-corrections-across-lattices.md),
   88  verifier 81/81 after repairs, SHA256 `b7c451e2…`);
   89  [reviews](../reports/2026-11-02--dispersion-corrections-across-lattices-review.md).
   90  Previous status: PRELIMINARY, INDEPENDENT_REVIEW_PASS_TWO_HOUSES,
   91  PROMOTION_PENDING. Sec. 11, L6b and Sec. 12 stay promoted as below.
   92  
   93  **Gate promoted — 2026-11-02:** by user instruction («haz lo que
   94  consideres, estás autorizado», after the two PASS reviews were reported
   95  with `PROMOTION_PENDING`), `L6B_TRIANGULAR_ROW`
   96  ([`theory/L6B_TRIANGULAR_ROW_GATE.md`](../theory/L6B_TRIANGULAR_ROW_GATE.md)),
   97  a revision of `C_ACROSS_LATTICES` restricted to row L6b, is promoted on
   98  `research/schur-stability-audit` in its frozen scope: row L6b
   99  `L6B_PARTIAL_VGRP_OPEN` with `s = 6`, `r_in = sqrt3/2`, `c_0 = 1/3`,
  100  `c_strict^iso = 1/sqrt3`; parent Hb `REFUTED_BY_ROW_L6b` (first declared
  101  row where `c_strict^iso < r_in`), Hc `CONFIRMED_IN_DECLARED_ROWS`, Ha
  102  unchanged. Evidence: two houses, Gemini and Grok, PASS on all six blocks,
  103  no repairs; Grok did not rerun the verifier. Not human review. One row
  104  of a declared list, no general QCA law, no novelty; ADMP massive row and
  105  `V_grp^max` stay OPEN. Chartered the same day by direct user instruction
  106  («vamos con L6b»; «sí, apruébalo y empieza»). Massless row only; it
  107  decides parent Hb/Hc only. The parent
  108  verifier is not modified. **Executed 2026-11-02**
  109  ([report](../reports/2026-11-02--l6b-triangular-row.md), verifier 64/64):
  110  `L6B_PARTIAL_VGRP_OPEN`. The text fixes the labelling (6 admissible, all
  111  equivalent); `s = 6`, not the parent's `s = 2`; `r_in = sqrt3/2`,
  112  `c_0 = 1/3`, `c_strict^iso = 1/sqrt3` (normalised), identical for both
```

## Líneas 455,500
```
  455    identification. The most useful open equivalence check is AF16/17's
  456    homogeneous paired-walk specialization.
  457  - **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  458    `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  459    tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  460    (375 checks), on this branch.
  461  
  462  ## 5. Completed standard Weyl/Dirac exact gate
  463  
  464  **Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**
  465  
  466  Evidence is the committed
  467  [contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
  468  [analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
  469  [verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
  470  [permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
  471  Source provenance and the published sign/dagger issues are recorded there.
  472  The analytic proof establishes the open mass interval and continuum scaling;
  473  the check count alone is not their justification or a formal proof certificate.
  474  
  475  ### Declared family and coordinates
  476  
  477  The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
  478  on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
  479  the minimal two-component blocks. The seven symbols are not seven independent
  480  geometries: transposes/chiralities within a dimension share support, inradius
  481  and linear speed. There are three dimension-specific geometries in this battery.
  482  
  483  Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
  484  complete update per time unit:
  485  
  486  `N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,
  487  
  488  `C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,
  489  
  490  `r_in = 1/sqrt(d)`, `V_causal^max = 1`.
  491  
  492  ### Massless equality
  493  
  494  For d=1,2,3 in this family, at the declared zero node,
  495  
  496  `m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.
  497  
  498  This is equality of the linear IR coefficient, not exact finite-momentum
  499  relativistic dispersion or a theorem about every admissible symbol.
  500  
```

## Líneas 762,812
```
  762  ### 8.1 Three objects, never identified
  763  
  764  For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
  765  Eqs. (5.12) and (5.15):
  766  
  767  `B(c_IR) ⊆ Γ ⊆ C_micro`,
  768  
  769  - `B(c_IR)`: the emergent isotropic IR light cone;
  770  - `Γ`: the ballistic / group-velocity propagation body;
  771  - `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.
  772  
  773  `Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
  774  `conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
  775  two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
  776  be assumed.
  777  
  778  ### 8.2 The canonical saturation function
  779  
  780  For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`
  781  
  782  `v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,
  783  
  784  and, in the normalization `c_IR = 1`, the canonical directional saturation
  785  function is the **support-function ratio**
  786  
  787  `S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.
  788  
  789  `S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
  790  non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.
  791  
  792  `S_min` is a **descriptive scalar summary only**. The full directional function
  793  `S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
  794  is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.
  795  
  796  ### 8.3 Walk (5.12)
  797  
  798  `B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
  799  `p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
  800  faster than the emergent IR light speed while remaining inside `C_micro`.
  801  `Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.
  802  
  803  ### 8.4 Walk (5.15) — the clean counterexample
  804  
  805  `Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.
  806  
  807  This refutes the identification
  808  
  809  `sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.
  810  
  811  Even when **all ballistic propagation respects `c_IR`**, the substrate permits
  812  causal propagation outside the relativistic ball in non-axial directions.
```

## Líneas 2318,2340
```
 2318  ## 11. c across QCA lattices and neighbourhoods — chartered 2026-11-01
 2319  
 2320  Contract: [`C_ACROSS_LATTICES_GATE.md`](../theory/C_ACROSS_LATTICES_GATE.md),
 2321  frozen before solving. Authorization: direct user instruction, 2026-11-01,
 2322  redirecting the project to comparing `c` across substrates within the QCA
 2323  scope (PROJECT_INSTRUCTIONS §1); no new substrate class is opened.
 2324  
 2325  Execution (2026-11-01): [report](../reports/2026-11-01--c-across-lattices.md),
 2326  verifier `scripts/verify_c_across_lattices_gate.py` (reviewed at
 2327  `cae6e30`, 103/103; repaired, 135/135 with every table value asserted).
 2328  [Reviews](../reports/2026-11-01--c-across-lattices-review.md): Grok
 2329  REPAIR_REQUIRED (three repairs, applied), Gemini PASS. Status:
 2330  **TABLE_PARTIAL_L6B_UNENCODED_ADMP_MASS_VGRP_OPEN — PROMOTED IN THE
 2331  DECLARED ROWS (2026-11-01, user instruction «1»).** Repaired; bounded
 2332  re-review Gemini PASS (R1–R5); Grok, ausente on 2026-11-01 (402), reviewed
 2333  the repaired snapshot on 2026-11-02: PASS on R1–R5, no mandatory repairs.
 2334  Grok's acceptance of its own three repairs is now on record. Previous
 2335  status: PRELIMINARY, PROMOTION_PENDING. In the declared rows: square,
 2336  BCC/cubic and line substrates have `c_0 = r_in`; the hexagonal substrate
 2337  has `c_0 / r_in = 1/sqrt3` (ADMP) or `sqrt3/2` (JDW), with ADMP and JDW
 2338  L6d on the identical substrate; `C_infty^strict = C_micro` in every
 2339  computed row. Ha `REFUTED_BY_ROW_L6a`. **Row L6b decided and promoted 2026-11-02**
 2340  ([`L6B_TRIANGULAR_ROW`](../theory/L6B_TRIANGULAR_ROW_GATE.md),
```

