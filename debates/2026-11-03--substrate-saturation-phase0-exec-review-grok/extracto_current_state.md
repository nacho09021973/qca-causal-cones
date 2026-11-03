# Extracto literal de state/CURRENT_STATE.md en el commit 6851d92 (numeración original de líneas a la izquierda)

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

## Líneas 484,500
```
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

## Líneas 2318,2400
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
 2341  [report](../reports/2026-11-02--l6b-triangular-row.md),
 2342  [reviews](../reports/2026-11-02--l6b-triangular-row-review.md)): `s = 6`,
 2343  `r_in = sqrt3/2`, `c_0 = 1/3`, `c_strict^iso = 1/sqrt3`, so Hb
 2344  `REFUTED_BY_ROW_L6b` and Hc `CONFIRMED_IN_DECLARED_ROWS`. The table
 2345  status name `..._L6B_UNENCODED_...` above is historical: L6b is now
 2346  encoded in its own gate, the parent verifier unchanged.
 2347  At finite mass, `c_H = c_0 theta/sin theta` where isotropic and no
 2348  computed new row has an isotropic `c_omega2` (anisotropy `O(sin theta)`).
 2349  Two ADMP sign issues are recorded. Not promoted; no general law.
 2350  
 2351  Charter summary: thirteen declared rows: six
 2352  already established (L1–L3, L3s4, L4 in part) are re-tabulated with their
 2353  existing tags; seven new rows from primary sources read on 2026-11-01
 2354  (L5a Farrelly–Short, L5b Mlodinow–Brun on BCC; L6a–L6b ADMP, L6c–L6f JDW
 2355  on two-dimensional lattices). Arrighi–Facchini is excluded with its
 2356  recorded reason. Substrates are declared by the translation group and
 2357  composite step set of each equation, not by the papers' lattice labels.
 2358  Hypotheses Ha (`c_0 = r_in` in declared s=2 rows), Hb (`c_strict^iso =
 2359  r_in`) and Hc (no row with `c_0 > c_strict^iso`) are OPEN. Execution:
 2360  report plus `scripts/verify_c_across_lattices_gate.py`, then independent
 2361  cross-family review, then a separate promotion. No rigidity or general
 2362  QCA law may be drawn from the table.
 2363  
 2364  ## 12. Hexagonal ceiling — chartered 2026-11-01
 2365  
 2366  Contract: [`HEX_CEILING_GATE.md`](../theory/HEX_CEILING_GATE.md), frozen
 2367  before solving. Authorization: direct user instruction, 2026-11-01, after
 2368  the promoted Sec. 11 table showed no declared hexagonal walk reaching
 2369  `c_0 = r_in`.
 2370  
 2371  Execution (2026-11-01, partial): [report](../reports/2026-11-01--hex-ceiling.md),
 2372  verifier `scripts/verify_hex_ceiling_gate.py` (18/18). L0
 2373  `PROVED_IN_REPO` (with classical Bernstein, prior art): `c_0 <= r_in` on
 2374  `W_hex`. T1 `GAP_PROVED_IN_CLASS`: in the `n = 3` antipodal subclass,
 2375  `c_0/r_in = sqrt(1-g)/sqrt2 <= sqrt3/2`, attained iff the coin axes are
 2376  coplanar at 120° (ADMP `g = 1/3`, JDW L6d `g = -1/2`). T2
 2377  `PROVED_FOR_MINIMAL_SUPPORT` (2026-11-02): no s=2 walk with
 2378  `F within {0} U vert(H)` reaches the ceiling (saturation forces exact
 2379  two-layer restrictions on the facet-normal lines; the resulting
 2380  polynomial system has no real solution; square-substrate positive
 2381  control passes); verifier 24/24. T2 in general
 2382  `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS` (19-point ball: Groebner over C did
 2383  not finish in 900 s; inconclusive, recorded as exploratory). **Promoted
 2384  2026-11-02 (user instruction «si, promuévelo») in the frozen scope stated
 2385  at the top of this file.** Execution
 2386  stopped. [Reviews](../reports/2026-11-02--hex-ceiling-review.md): Gemini
 2387  PASS on all five blocks; Grok REPAIR_REQUIRED (R1: Bernstein used without
 2388  in-repo proof; R2: weak rank predicate), both repaired 2026-11-02 (Lemma B
 2389  in the report; exact minor in the verifier, 24/24). Bounded re-review
 2390  of the repairs: Grok PASS and Gemini PASS on R1–R4, identical input.
 2391  Previous status: PRELIMINARY, PROMOTION_PENDING.
 2392  
 2393  Charter: class `W_hex`: translation-
 2394  invariant `s = 2` walks on the triangular lattice, one update a product
 2395  of `n` coin–partial-shift factors, regular hexagonal `C_micro` from the
 2396  exact composite support, massless node at `k = 0` with isotropic untilted
 2397  cone. Targets: L0 (`c_0 <= r_in`, to be proved or cited, not assumed),
 2398  T1 (`n = 3` antipodal subclass: exact supremum), T2 (whole class: gap
 2399  proof or explicit witness). Hypotheses HX0–HX2 OPEN. No verdict from
 2400  numerics or failed search; restricted results stay restricted.
```

## Líneas 2450,2600
```
 2450  `K4`; L5a, L5b, L4 `n1 n2 n3`). Hf `REFUTED_BY_ROW_L6e` (L2 and L6e
 2451  identical; also L5a = the `+i` Weyl block of L5b, and L6d = L6f through
 2452  `|k|^2`). Scale of
 2453  validity OPEN in `d >= 2`; `V_grp^max` OPEN. No physical interpretation.
 2454  
 2455  ## 14. Hexagonal supremum (M1) — chartered 2026-11-03
 2456  
 2457  Contract: [`HEX_SUPREMUM_GATE.md`](../theory/HEX_SUPREMUM_GATE.md),
 2458  frozen before solving, preregistration commit `86573ca`. Authorization:
 2459  user approval of the draft, 2026-11-03 («APROBACIÓN CON ENMIENDAS»), with
 2460  three amendments incorporated before freezing (cumulative solver budget of
 2461  3600 s per support; explicit form of the real infeasibility certificate,
 2462  `-1 = sum q_j^2 + sum h_i f_i` with exact rational coefficients, or an
 2463  ideal element with certified absence of real zeros; a witness answers the
 2464  saturation question only). Continues T2 of Sec. 12 only; L0, T1 and the
 2465  minimal-support T2 are not reopened.
 2466  
 2467  Question: does any `s = 2` walk in `W_hex` reach `c_0 = r_in`? Method,
 2468  named before computation: Stage A structural reduction (facet-line
 2469  rigidity plus extreme-face unitarity identities), then exact decision on
 2470  the 13-point support `S13` (`v = g_1 + g_2`), then `S19` only after `S13`
 2471  has a verdict. Gap proofs from unitarity, support, node and isotropy are
 2472  stated for `W_hex^sym`; a witness must be given in product form to lie in
 2473  `W_hex`. Exploratory numerics only to guide, never in a verdict; no
 2474  confirmatory numerics. Budget: one session. Ends the line: a factorized
 2475  witness (M1 closes, limited reading), or budget exhausted
 2476  (`OPEN_AFTER_<analysis>`, not a repo closure, plan Sec. 4); a gap proof
 2477  for `W_hex^sym` keeps the line. Status before execution: OPEN; authorized.
 2478  
 2479  Execution (2026-11-03, partial): [report](../reports/2026-11-03--hex-supremum.md),
 2480  verifier `scripts/verify_hex_supremum_gate.py` (12/12), 0 s solver.
 2481  Lemma A1 (singleton intermediate layer along a facet normal forces its
 2482  coefficient to 0) and A2 (`A_v A_{-v}^dag = 0` at opposite vertices).
 2483  M1-A `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS`. M1-B13 `PROVED_FOR_S13`: in
 2484  S13 the singleton layers are the inner ring, which vanishes, leaving the
 2485  minimal support excluded by T2 (Sec. 12), in `W_hex^sym`. HX2
 2486  `CONFIRMED_FOR_S13`. S19 (layers 3,4,5,4,3) not reduced by A1; M1-B19 not
 2487  started. [Reviews](../debates/2026-11-03--hex-supremum-stageA-review-grok/verificacion_autor.md):
 2488  Grok PASS, Gemini PASS, no repairs. **Promoted 2026-11-03 (user
 2489  instruction «PROMOCIÓN AUTORIZADA»):** M1-B13 `PROVED_FOR_S13`, HX2
 2490  `CONFIRMED_FOR_S13`, M1-A `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS`. Scope: S13
 2491  only, in `W_hex^sym` (hence `W_hex`); qualitative gap, no uniform
 2492  separation from `r_in`, whole class OPEN. The 12/12 verifier run is the
 2493  author's session, not the reviewers'. Previous status: PRELIMINARY,
 2494  INDEPENDENT_REVIEW_PASS_TWO_HOUSES, PROMOTION_PENDING. M1-B19 authorized
 2495  the same day, structural reduction first, solver budget 3600 s
 2496  cumulative.
 2497  
 2498  M1-B19 execution (2026-11-03): [report](../reports/2026-11-03--hex-supremum-b19.md),
 2499  verifier `scripts/verify_hex_supremum_b19.py` (17/17), certificate data
 2500  `scripts/data/hex_s19_certificate.json`. Two further linear consequences
 2501  of saturation, A3 (first moments along the edge, per layer) and A4
 2502  (off-diagonal first-order unitarity on the facet line), reduce S19 from 56
 2503  to 18 free real parameters; controls on the square substrate keep the
 2504  known saturating walk. The 730 remaining unitarity quadratics admit a
 2505  rational combination with positive-definite Gram matrix (exact, over
 2506  `QQ(sqrt3)`): no real solution. M1-B19 `PROVED_FOR_S19` (in `W_hex^sym`;
 2507  includes the support of JDW L6c), HX2 `CONFIRMED_FOR_S19`. No nonlinear
 2508  solver run (0 s of 3600 s); exploratory numerics only guided the
 2509  certificate. Whole class OPEN; larger hexagons not in the contract's
 2510  stages. Status: **PRELIMINARY, not independently reviewed.**
 2511  
 2512  M1-B19 review and amendment (2026-11-03): `6302328` pushed by user
 2513  authorization (push and Grok + Gemini review; S25 not authorized). Grok
 2514  (`grok-4.7`): REPAIR_REQUIRED, points on A3, A4, solution preservation,
 2515  the 18-parameter reduction and the certificate's implication PASS; one
 2516  mandatory repair: the report claimed contract form Sec. 4 (ii), which the
 2517  certificate does not meet literally (record `f80c075`). Gemini: no report,
 2518  `402` prepayment credits depleted (four attempts, account-level).
 2519  [Amendment 1](../theory/HEX_SUPREMUM_GATE_AMENDMENT_1.md) (`208e1b1`,
 2520  approved by the user, post-execution, frozen file untouched): the
 2521  certificate is assessed under Sec. 4 (i); field `QQ(sqrt3)`, ~11 min check
 2522  time, exploratory numerics (1294 s) and separate report/verifier declared.
 2523  Report repaired accordingly (verifier bytes unchanged). Second review: the
 2524  user personally, OK, on the version at `88d28dd`
 2525  ([record](../debates/2026-11-03--hex-supremum-b19-review-usuario/registro.md),
 2526  `59f2ea2`; no written list of points checked). **Promoted 2026-11-03 (user
 2527  instruction «sí, promociona S19 y haz push»):** M1-B19 `PROVED_FOR_S19`,
 2528  HX2 `CONFIRMED_FOR_S19`, M1-A stays `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS`.
 2529  Scope: S19 only, in `W_hex^sym` (hence `W_hex`); qualitative gap, no
 2530  uniform separation from `r_in`; certificate under contract Sec. 4 (i) per
 2531  Amendment 1. The 17/17 verifier runs are the author's, not the reviewers'
 2532  (Grok could not execute). M1 status: both bounded stages (S13, S19) end
 2533  with a gap, no witness; result (a) of Sec. 0 not met, no gap proof for the
 2534  class; whole class OPEN. No further stage is in the contract; S25 or any
 2535  other extension needs a new charter (not authorized). Previous status:
 2536  PRELIMINARY; one of two requested reviews; promotion not authorized.
 2537  
 2538  ## 15. Substrate saturation, phase 0 — chartered 2026-11-03
 2539  
 2540  Contract: [`SUBSTRATE_SATURATION_PHASE0_GATE.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE.md),
 2541  frozen before execution, preregistration commit `9bf3019`, by user
 2542  instruction («congela la revisión 3»). Drafting authorized 2026-11-03
 2543  («Autorizo redactar la carta de la fase 0, pero no congelarla ni ejecutar
 2544  todavía ninguna comprobación»), with the user's four precisions
 2545  (existential quantifier, domain `s = 2`, `d <= 3`, single normalization,
 2546  one exact counterexample refutes). Two Grok rounds:
 2547  [round 1](../debates/2026-11-03--substrate-saturation-phase0-draft-review-grok/informe_grok.md)
 2548  REPAIR_REQUIRED (six repairs, all accepted by the user, who chose the
 2549  predicate "hypercube up to scale and isometry" and turned phase 0 into a
 2550  definitional audit);
 2551  [round 2](../debates/2026-11-03--substrate-saturation-phase0-rev2-review-grok/informe_grok.md)
 2552  REPAIR_REQUIRED (one repair, L6b traceability, plus five clarifications,
 2553  all applied). Domain, logic and independence PASS in round 2: the
 2554  isotropic-untilted-node condition is defined on the linear term, not on
 2555  the shape of `C_micro`; the hexagonal rows are inside the domain, so a
 2556  saturating admissible `s = 2` hexagonal walk would refute (PH⇒).
 2557  
 2558  Statement under audit: **(PH) [UNVERIFIED]**, for `s = 2`, `d <= 3`,
 2559  admissible models only: the ceiling `c_0 = r_in(C_micro)` is attained by
 2560  some admissible walk on a substrate iff `C_micro` is a hypercube up to
 2561  scale and isometry. A geometric classification suggested by the promoted
 2562  rows, not a physical explanation. The zonotope reading (PS′) is kept
 2563  `[UNVERIFIED]` and is not equivalent to (PH). Method: documentary only, no
 2564  computation. Outcomes: `DEFINITIONS_CLOSED` (the statement is defined well
 2565  enough to be tested for refutation, nothing more) or
 2566  `OPEN_AFTER_ROW_SURVEY`; per direction `REFUTED_BY_ROW_<row>` or
 2567  `NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`, the latter never evidence for (PH)
 2568  and never `CONFIRMED`. No outcome authorizes a later phase; a test that
 2569  can fail (the hexagon, user's first choice) needs its own contract.
 2570  Status: **OPEN; frozen; execution not authorized; nothing done.**
```

