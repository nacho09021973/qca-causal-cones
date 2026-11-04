# Substrate saturation, phase 0 — definitional audit

**Date:** 2026-11-03. **Branch:** `research/schur-stability-audit`.
**Contract:** [`SUBSTRATE_SATURATION_PHASE0_GATE.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE.md),
preregistration commit `9bf3019`; registered in CS Sec. 15 (`6851d92`).
**Authorization to execute:** user instruction, 2026-11-03 («EJECUTAMOS
FASE 0»).
**Author:** Claude Code (Claude Opus 5.5). Documentary only: no verifier
run, written or edited; no walk built; no numerics.
**Nature:** a definitional audit with **no confirmatory value** (contract
Sec. 0). **Status: PRELIMINARY.**
**Review:** Grok (`grok-4.7`), REPAIR_REQUIRED, five mandatory repairs, all
applied in this revision (`debates/2026-11-03--substrate-saturation-phase0-exec-review-grok/`;
reviewed snapshot `informe_fase0_snapshot.md`). Repair 1 changes the
definitional outcome from `DEFINITIONS_CLOSED` to `OPEN_AFTER_ROW_SURVEY`
(L4). While applying it the author found that L3, like L4, is a recorded
row not covered by the c-across-lattices certificate; its node is traced
to the Weyl/Dirac gate (Sec. 2). Second Grok round
(`debates/2026-11-03--substrate-saturation-phase0-exec-review2-grok/`):
REPAIR_REQUIRED, two repairs (L3 trace rewritten clause by clause; L4 not
counted in the domain), both applied here; this revision is not
re-reviewed.
**Update 2026-11-04 (L3 only).** DeepSeek (`deepseek-v4-pro`) reviewed the
L3 node trace of Sec. 2: PASS on all five points, no mandatory repairs
(`debates/2026-11-04--substrate-saturation-phase0-L3-trace-review-deepseek/`,
`97dfe44`; reviewed sha256 `3b88e925…`). By the user's decision of
2026-11-04, L3 counts as a witness in this audit, in that role only; its two
non-blocking clarifications are added to the trace. This changes no outcome:
the BCC substrate already had the witness L5a. It does not close phase 0 and
does not change its evidential value.

**Pre-step check.** Known: the contract fixes (PH), its domain (`s = 2`,
`d <= 3`, admissible models), one source per row, three separate fields,
and the outcomes. Question: is (PH) defined without ambiguity on the
promoted rows, and is there an exact counterexample among them? Ends this
formulation: one exact counterexample (contract Sec. 4).

## 1. Rows considered (contract Sec. 3.1)

Promoted rows with `d <= 3` and an exact `c_0` or an exact class statement.
Primary row source: the massless table of
[`reports/2026-11-01--c-across-lattices.md`](2026-11-01--c-across-lattices.md)
(l. 140–152; promoted in the declared rows, CS Sec. 11), in units of
longest step 1, one update per time unit. Composite step sets from the same
report, Sec. 3 (l. 106–113), and for L2–L3 the vertices from CS l. 486–488
(`N_d = {(±1,...,±1)/sqrt(d)}`, `C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`).
The pair `(r_in, c_0)` of every row is taken from the massless table only. Every computed row of that table carries the
certificate «Hermitian linear generators, zero tilt, an isotropic untilted
cone (`{T_a, T_b} = 2 c_0^2 delta_ab`), the exact facets and vertices of
`C_micro`» (report l. 154–156).

**Outside the domain (`s != 2`), recorded only:**

| Row | `s` | Source | Note |
| --- | --- | --- | --- |
| L5b (BCC) | 4 | c-across-lattices l. 145 | saturates; cannot confirm or refute (PH) |
| L3s4 (BCC) | 4 | c-across-lattices l. 146; CS Sec. 4.1 | `c_0 = a/sqrt3 < r_in` |
| L6b (triangular) | 6 | L6b report l. 24, l. 70–71; CS l. 97–99, l. 111 (current numbering; the frozen contract's l. 88–94, l. 106 refer to the file at `9bf3019`) | the parent table (l. 152) still lists `s = 2`, OPEN, not encoded; not amended |

## 2. Row table, `s = 2` (contract Secs. 3.2–3.3; L4 tabulated, domain membership not established)

Shapes are read from the certified vertices of `C_micro` in the units
above. "Hypercube" means up to scale and isometry; "parallelepiped" means a
Minkowski sum of `d` independent segments. "Zonotope directions" are the
edge directions of `C_micro` (every polytope listed here is a zonotope;
its generators are read from its edges, not from the walk's factor
structure — see Sec. 4, finding F2).

| Row | Substrate (group, `N`) | `C_micro` vertices | Hypercube | Parallelepiped | Zonotope directions | `r_in` | `c_0` | Single source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | line, `N = {±1}` | `±1` | yes (segment) | yes | 1 | 1 | 1 | c-across-lattices l. 140 |
| L2 | square, `N_2` | `(±1,±1)/sqrt2` | yes (square) | yes | 2, orthogonal | `1/sqrt2` | `1/sqrt2` | pair: l. 141 only (vertices: CS l. 486–488) |
| L6e | square, same as L2 (l. 111) | `(±1,±1)/sqrt2` | yes | yes | 2, orthogonal | `1/sqrt2` | `1/sqrt2` | l. 142 |
| L3 | BCC, `N_3` | `(±1,±1,±1)/sqrt3` | yes (cube) | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | pair: l. 143 only (vertices: CS l. 486–488) |
| L5a | BCC, same as L3 (l. 106) | `(±1,±1,±1)/sqrt3` | yes | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | l. 144 |
| L4 | cube (CJWW (5.12), (5.15)) | cube of longest step 1 (label `[-1,1]^3` is in CS Sec. 8 units; not combined with the rescaled radius) | yes | yes | 3, orthogonal | `1/sqrt3` | `1/sqrt3` | l. 147 only (CS Sec. 8 pair not crossed) |
| L6a | triangular lattice, `F = {0} ∪ {±2u_i}` (l. 108) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `1/2` | l. 148 |
| L6d | identical to L6a (l. 110) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 150 |
| L6f | triangular lattice, hexagon of radius `sqrt3` rotated 30° (l. 112) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 151 |
| L6c | finer triangular group, 19-point hexagonal ball (l. 109) | regular hexagon | no | no | 3, at 120° | `sqrt3/2` | `3/4` | l. 149 |

**Three fields per row, kept apart (contract Sec. 3.3).**

| Row | (a) this walk | (b) promoted class statement, with its scope | (c) substrate, existential |
| --- | --- | --- | --- |
| L1 | `c_0 = r_in` | — | yes: L1 |
| L2, L6e | `c_0 = r_in` | — | yes: L2, L6e |
| L3, L5a | `c_0 = r_in` | — | yes: L5a and L3 (L3's node trace reviewed 2026-11-04) |
| L4 | `c_0 = r_in` (pair from l. 147); node not established in the frozen sense | — | unresolved: L4 is the only tabulated walk on its substrate and is flagged |
| L6a | `c_0 < r_in` (`c_0/r_in = 1/sqrt3`) | T1: `sup c_0/r_in = sqrt3/2` on the `n = 3` antipodal subclass only (hex-ceiling report l. 125, CS Sec. 12); L6a is in it, `g = 1/3` (l. 138–139). T2: no s=2 walk with `F within {0} U vert(H)` reaches `r_in` (CS Sec. 12; contains L6a, L6d, L6f, hex-ceiling l. 153–156). M1-B13, M1-B19: no s=2 walk in `W_hex^sym` with `F` within S13 or S19 reaches `r_in` (CS Sec. 14), qualitative gaps. Whole hexagonal class OPEN. | no promoted saturating walk; **not** "no walk saturates" |
| L6d, L6f | `c_0 < r_in` (`c_0/r_in = sqrt3/2`) | as for L6a (L6d at the T1 maximum, `g = -1/2`) | as for L6a |
| L6c | `c_0 < r_in` (`c_0/r_in = sqrt3/2`) | not in the minimal-support subclass (hex-ceiling l. 156–157); its 19-point support is S19, covered by M1-B19 in `W_hex^sym` (B19 report Sec. 3) | as for L6a, on its own (finer) substrate |

**Definition check (contract Sec. 3.4).** The c-across-lattices report
separates computed from recorded rows (l. 235: Ha «Holds in L1, L2, L5a,
L6e and the recorded L3, L4»). Rows L1, L2, L6e, L5a, L6a, L6c, L6d and
L6f are computed there and carry its certificate of the isotropic untilted
node (l. 154–156). **L3 is recorded, not computed**, so that certificate
does not cover it either. Its node is traced instead, clause by clause, to
checks of the standard Weyl/Dirac gate (CS Sec. 5, PASS, l. 462–464;
verifier `scripts/verify_weyl_dirac_gate.py`, applied to all seven
standard symbols, including the d=3 symbols of L3). The scalar Hessian
check («Hessian», verifier l. 169–171) is **not** the node certificate and
is not used. Correspondence with contract Sec. 2.4:
(i) `U(0)` scalar: «zero node», `W(0) − I = 0` (verifier l. 158);
(ii) Hermitian linear term: the verifier sets `spatial = i ∂W` at the
origin (l. 159–160) and checks unitarity `W W^† = I` as a Laurent identity
(l. 147); differentiating it at `k = 0`, where `W = I`, gives
`∂W + ∂W^† = 0`, so `i ∂W` is Hermitian (a one-line derivation by the
author from the checked identity, not itself a verifier check);
[clarification, 2026-11-04 review: `spatial_derivative` is
`i z ∂_z / sqrt(d)` (verifier l. 133–134), which equals `∂_k` under the phase
`z_j = e^{i k_j / sqrt(d)}`; that phase follows from `N_d = {±1}^d / sqrt(d)`
(CS l. 486), since the monomial `z^n` is the displacement `n / sqrt(d)`. The
opposite sign convention flips the sign of every `T_a` and affects neither
Hermiticity, tracelessness nor the anticommutator];
(iii) traceless: «scalar trace» `tr W = 2u` (l. 149) and «scalar gradient»
`∂u = 0` at the origin (l. 161–162), so `tr(i ∂W) = 0`;
(iv) `{T_a, T_b} = 2 c_0^2 delta_ab`: «Clifford» checks
`{spatial_a, spatial_b} = 2 (delta_ab/d) I` (l. 164–167), with
`c_0 = 1/sqrt(d)` [clarification, 2026-11-04 review: the value `c_0^2 = 1/d`
is fixed by the Clifford check; «massless matching» (l. 172–173) computes
`c_0` from `T_1` and checks `c_0 = r_in`]; also exact-gate
report l. 131–138 (`H_W = (1/sqrt d) sum_j Sigma_j k_j + O(|k|^2)`,
`{Sigma_i, Sigma_j} = 2 delta_ij I`);
(v) zero tilt: the word is not used in the Weyl/Dirac dossier. It is
reached only through the equivalent form the contract itself declares,
`A(n)^2 = c_0^2 |n|^2 I` with `A(n) = n_a T_a` traceless, which is the
polarization of (iv) together with (iii).
**Status of L3's node: traced by this correspondence; reviewed by DeepSeek on
2026-11-04, PASS, no repairs (header); L3 counts as a witness by the user's
decision of that date.** Text as of 2026-11-03, kept: «pending review»
(steps (ii) and (v) are elementary derivations by the author from checked
identities; the user checked both derivations on 2026-11-03 and found them
correct under the stated hypotheses, without inspecting the verifier lines
or the full correspondence, so the status is unchanged). Until that is reviewed, L3 is not used as a witness; the BCC
witness is L5a» (superseded 2026-11-04 as stated above). L5a is a computed row under the certificate of l. 154–156. **L4 is flagged, unresolved:** it is re-tabulated, not
computed, in that report (l. 147, «CURRENT_STATE Sec. 8»), so the
certificate does not cover it, and the promoted passages read here (CS
Sec. 8.1–8.2, l. 762–789) state an emergent isotropic IR cone `B(c_IR)`
(l. 769) and the support-function ratio `S(n̂) = h_{B(c_IR)}/h_{C_micro} =
1/||n̂||_1` (l. 780–787, in CS Sec. 8 units), which is geometry of `B`, not
the algebraic node condition of contract Sec. 2.4 (`U(0)` scalar,
traceless Hermitian linear term, `{T_a, T_b} = 2 c_0^2 delta_ab`, zero
tilt). Whether L4 is admissible in the frozen sense is therefore not
established from the promoted data used here. **L4 is unclassified, not
shown to be outside the domain:** it is neither `OUTSIDE_DEFINITIONS` nor
an admissible row; the uncertainty is kept as such. (An earlier draft of this
report read that ratio as "no tilt"; Grok's review showed that inference
is not the frozen certificate, and it is withdrawn.)

## 3. Counterexample check (contract Sec. 4)

- **Against (PH⇒)** — a non-hypercube substrate in the domain with a
  promoted walk at `c_0 = r_in`: none. The only non-hypercube shape is the
  regular hexagon (L6a, L6c, L6d, L6f), and every promoted hexagonal walk
  has `c_0 < r_in`.
- **Against (PH⇐)** — a hypercube substrate in the domain on which a
  promoted exact result shows that no admissible walk saturates: none.
  The line, square and BCC substrates each have a promoted admissible walk
  with `c_0 = r_in` (L1; L2 and L6e; L5a). On the L4 cube substrate the only tabulated walk is
  flagged (Sec. 2), so that substrate has no established witness; a
  flagged node is not a promoted result that no walk saturates, so it is
  not a counterexample either.

## 4. Audit findings

- **F1 (contract Sec. 3.5).** The table contains no parallelepiped that is
  not a hypercube, and no non-hypercube body with a promoted saturating
  walk. It therefore cannot separate (PH) from (PS′), nor from any other
  predicate that agrees on segments, squares, cubes and the regular
  hexagon (for example "fewer than `d+1` zonotope directions", or "the
  facet normals come in `d` orthogonal pairs"). The shapes present are
  three hypercubes (segment, square, cube) and one non-hypercube (the
  regular hexagon).
- **F2 (on (PS′), recorded, no verdict).** The contract's identity
  `conv F = sum_i [-a_i, a_i]` presupposes that every sign pattern
  `sum_i ε_i a_i` of the partial shifts appears in `F` with nonzero
  amplitude. That is not recorded per row in the promoted data (the factor
  structure is tabulated only for the `n = 3` antipodal subclass, T1), and
  it can fail if a coin entry vanishes. The "zonotope directions" column
  above is read from the edges of `C_micro`, which are certified; whether
  they coincide with the factor shifts of each walk is not established
  here. (PS′) as written therefore needs that hypothesis made explicit
  before any test.
- **F3 (substrate counts; updated in Sec. 7.3 to six substrates).** Grouped by shape and translation group, the
  rows with a traced node give four substrates in the domain (line; square,
  L2 = L6e; BCC, L5a and L3 (L3 reviewed 2026-11-04); hexagon on the triangular lattice,
  L6a = L6d, with L6f the same shape up to rotation and scale) plus the
  finer-group hexagon of L6c. The cube substrate of L4 is tabulated with
  domain membership not established (Sec. 2) and is not counted. By shape,
  among domain rows: segment, square, cube (BCC) and hexagon.

## 5. Outcomes (contract Sec. 5)

**Re-assessed 2026-11-04 under Amendment 1: see Sec. 7** (outcome
`OPEN_AFTER_ROW_SURVEY` kept; L4 gap resolved; gap G1 named). Text of
2026-11-03 follows.

**Definitional outcome: `OPEN_AFTER_ROW_SURVEY`.** Gap: the admissibility
of L4 (isotropic untilted node in the sense of contract Sec. 2.4) is not
established from the promoted data used here (Sec. 2). L3's node is traced through the Weyl/Dirac gate by the correspondence of
Sec. 2, reviewed 2026-11-04 (PASS); this does not touch the gap, which is L4. Every tabulated `s = 2` row, L4 included, has one
traced source for the pair `(r_in, c_0)` in the units of contract
Sec. 2.4; the rows counted in the domain are those with a traced node (L4
is not among them); the zonotope-direction field is read from the
certified vertices, with the caveat of F2.

**Counterexample check:** the outcomes are (PH⇐)
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE` and (PH⇒)
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`; they are not independent evidence for
(PH), because the statement was read off this table (three hypercube
shapes, one regular hexagon, no parallelepiped that is not a hypercube,
F1); they are never `CONFIRMED`; and, like every outcome of this gate,
they authorize no later phase.

## 6. What this does not establish

No evidence for (PH) or (PS′); no statement about parallelepipeds that are
not hypercubes, about hexagonal walks beyond the promoted results, about
`s != 2` or `d > 3`; no uniform gap; no physical explanation of the
predicate; no novelty claim.

## 7. Re-assessment of the definitional outcome under Amendment 1 (2026-11-04)

**Authorization:** user instruction, 2026-11-04 («haz la revaluación
conforme a la Enmienda 1 aprobada. Comprueba cada condición congelada de
cierre y deja su trazabilidad en el informe»). **Amendment:**
[`SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md),
approved `5213d94` (review: gpt-6.1-sol, PASS, `1d17a2d`). Author: Claude
Code (Claude Opus 5.5). Documentary only: no verifier run, written or
edited. Per Amendment 1 Sec. 3, only the definitional outcome is
re-assessed, with the amendment as the sole change; Secs. 1–6 above are
kept as written on 2026-11-03 (with the L3 annotation of `6aa42f9`).

### 7.1 L4 under Amendment 1

The five conditions of Amendment 1 Sec. 1, as applied there in Sec. 2 and
reviewed: (1) class: C_ACROSS_LATTICES_GATE l. 78 with its admission rule
l. 100–104, the two printed walks CJWW (5.12), (5.15); (2) primary source:
PDF p. 16 (5.12), p. 17 (5.15), transcription checked literally (DeepSeek,
`801c3f2`; gpt-6.1-sol, point 3); (3) review: DeepSeek PASS twice, the
current addendum text being the second record (sha256 `b8b9ed87…`), and
gpt-6.1-sol re-derivation PASS; (4) substrate: (5.12) generates the BCC
group, (5.15) generates `Z^3` (Amendment 1 Sec. 2.4, re-derived by
gpt-6.1-sol); (5) pair `(1/sqrt3, 1/sqrt3)` from c-across-lattices l. 147
only. **L4 is admissible under Amendment 1 (reviewed primary-source
derivation), not «certified».** Fields of Sec. 3.3 for L4: (a) `c_0 = r_in`
for both walks; (b) none; (c) yes for the `Z^3` substrate (witness
(5.15)) and yes again for BCC ((5.12), besides L5a and L3).

### 7.2 Frozen closing conditions (contract Sec. 5, `DEFINITIONS_CLOSED`)

| # | Condition (frozen text) | Status after Amendment 1 | Trace |
| --- | --- | --- | --- |
| C1 | every row in the domain has a single traced source in the units of Sec. 2.4 | **met** | Sec. 2 table, «Single source» column: c-across-lattices l. 140–151; L4 l. 147 only, CS Sec. 8 pair not crossed |
| C2 | domain membership of each row (admissible node, frozen Secs. 2.2, 2.4) | **met** | L1, L2, L6e, L5a, L6a, L6c, L6d, L6f: certificate c-across-lattices l. 154–156; L3: trace to the Weyl/Dirac gate (CS Sec. 5, PASS), reviewed (DeepSeek, `97dfe44`); L4: Sec. 7.1 |
| C3a | Sec. 3.2 fields: vertices of `C_micro`, hypercube, parallelepiped, `r_in`, `c_0` | **met** | Sec. 2 table, vertices from c-across-lattices Sec. 3 (l. 106–113) and CS l. 486–488 |
| C3b | Sec. 3.2 field: «for product-class rows, the reduced generators (for (PS′))» | **not met** | see gap G1 below |
| C3c | Sec. 3.3: three separate fields per row | **met** | Sec. 2 «Three fields» table, L3 updated `6aa42f9`, L4 in Sec. 7.1 |
| C4 | all fields «filled from promoted exact data» | met for C3a and C3c, with the L4 node from the Amendment 1 source; not for C3b | as above |
| C5 | «the `OUTSIDE_DEFINITIONS` list is explicit» | **met here**: `OUTSIDE_DEFINITIONS = ∅` | every `s = 2` row now has an admissible node (C2); rows with `s != 2` (L5b, L3s4, L6b) are outside the domain (Sec. 1 table), which is a different category. The 2026-11-03 text did not state the list; it is stated here |

**Gap G1 (C3b), present in the 2026-11-03 audit and not counted there.**
Frozen Sec. 3.2 and the last paragraph of frozen Sec. 1 require phase 0 to
record, for product-class rows, the reduced generators: the partial-shift
vectors `a_i` of the factors, up to sign and positive scale, parallel ones
merged. The Sec. 2 table records instead a «Zonotope directions» column
read from the edges of `C_micro`, and finding F2 states that «whether they
coincide with the factor shifts of each walk is not established here». The
edges of `conv F` equal the reduced generators only if `conv F` is the full
zonotope `sum_i [-a_i, a_i]`, which is the hypothesis of F2. Nor does the
audit record which rows belong to the product class (CJWW (5.15), for
instance, is printed as a matrix, not as a product of partial shifts). So
the field is filled by a proxy whose identity with the frozen quantity is
not established. The 2026-11-03 Sec. 5 named only L4 as the gap; that was
an omission by the author, found now while checking each condition.

**What would close G1 (not done here; needs the user's decision and a
review):** a documentary trace, per `s = 2` row, of (i) product-class
membership and the factor shift vectors, read from the reviewed
constructors that build each symbol as a product (e.g.
`verify_weyl_dirac_gate.py` `rotation_product`, l. 80–88, factors along the
coordinate axes; `verify_c_across_lattices_gate.py` `row_L5a`, l. 167–189,
`T_b` shifting by `±e_b`; `row_L6a`, l. 227–299, translations by `±u_i`),
and (ii) whether every sign pattern appears in the certified support `F`.
For CJWW (5.12) both are already in the reviewed record (three factors with
shifts `±e_a`; all eight corner amplitudes nonzero, gpt-6.1-sol point 4).

### 7.3 F3 updated: six substrates by group and support

Grouped by translation group and composite step set (frozen Sec. 2.3),
source coordinates, shape in brackets:

1. **Line** [segment]: group `Z`, `F = {±1}`. L1.
2. **Square, diagonal steps** [square]: `F = {(±1,±1)}`, group
   `{x ∈ Z^2 : x_1 ≡ x_2 (mod 2)}`. L2 (CS l. 486), L6e (c-across-lattices
   l. 111).
3. **BCC** [cube]: `F = {±1}^3`, group
   `{x ∈ Z^3 : x_1 ≡ x_2 ≡ x_3 (mod 2)}`. L3 (CS l. 486), L5a
   (c-across-lattices l. 106), CJWW (5.12) of L4 (Amendment 1 Sec. 2.4).
4. **Simple cubic** [cube]: `F = {±1}^3 ∪ {(±1,±1,0)} ∪ {(±1,0,0)}` (signs
   independent), group `Z^3`. CJWW (5.15) of L4 (Amendment 1 Sec. 2.4).
   New in this count.
5. **Hexagon on the triangular lattice** [regular hexagon]:
   `F = {0} ∪ {±2u_i}`, step spacing equal to the hull radius. L6a = L6d
   (c-across-lattices l. 108, 110); L6f, a hexagon of radius `sqrt3` rotated
   30° (l. 112), the same shape and group up to rotation and scale.
6. **Hexagon over the finer triangular group** [regular hexagon]: the
   19-point hexagonal ball of radius 2, group of index 1 instead of 4 in
   the generator lattice (l. 109). L6c.

The 2026-11-03 count was five (items 1, 2, 3, 5, 6). Item 4 is added and
item 3 gains a walk. **Shapes unchanged:** segment, square, cube,
hexagon; F1 unchanged (no parallelepiped that is not a hypercube, no
non-hypercube body with a saturating walk).

### 7.4 Outcomes after re-assessment

**Definitional outcome: `OPEN_AFTER_ROW_SURVEY`, kept.** Remaining gap:
**G1**, the reduced generators of product-class rows (and the list of
those rows), frozen Sec. 3.2. The L4 gap of 2026-11-03 is **resolved** by
Amendment 1. No other gap was found against conditions C1–C5.

**Counterexample check, unchanged:** (PH⇐) and (PH⇒)
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE`. The new `Z^3` witness is on a
hypercube substrate and saturates, so it is consistent with (PH⇐) and is
not a counterexample; it is not independent evidence for (PH), because
(PH) was read off this table and the table still has three hypercube
shapes, one regular hexagon and no parallelepiped that is not a hypercube.
Never `CONFIRMED`. No outcome authorizes a later phase. F2 unchanged.
