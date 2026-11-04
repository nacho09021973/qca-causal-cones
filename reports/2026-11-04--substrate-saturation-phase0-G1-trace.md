# Substrate saturation, phase 0 — documentary trace for gap G1 (reduced generators)

**Date:** 2026-11-04. **Branch:** `research/schur-stability-audit`.
**Base:** `4747b23` (local).
**Gap traced:** G1 of the audit re-assessment
([`2026-11-03--substrate-saturation-phase0.md`](2026-11-03--substrate-saturation-phase0.md),
Sec. 7.2, `862b405`): frozen Sec. 3.2 of
[`SUBSTRATE_SATURATION_PHASE0_GATE.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE.md)
(`9bf3019`) requires, for product-class rows, the reduced generators.
**Authorization:** user instruction, 2026-11-04 («haz la traza documental
de G1, acotada a las filas de la auditoría y usando los constructores y
fuentes ya revisados ... No deduzcas los factores a partir de las aristas
del cuerpo. Si alguna fila no puede resolverse documentalmente, deja la
laguna explícita ... sin ejecutar ni modificar verificadores»).
**Author:** Claude Code (Claude Opus 5.5). **Documentary only:** no verifier
run, written or edited. Factors are read from the constructor code and the
source equations, never from the edges of `C_micro`. Supports are taken
from set assertions already in the verifiers (cited per row). Statements
marked **[hand]** are elementary derivations by the author, not checked by
any script.
**Review:** gpt-6.1-sol (OpenAI), REPAIR_REQUIRED, two mandatory repairs
(L6e count in the summary; F2 stated as a necessary condition), both
applied in this revision with three clarifications, by the user's decision
of 2026-11-04 («SI»); `debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/`
(`8d70e58`, reviewed text `cb814b5`). This revision is not re-reviewed.
**Status: PRELIMINARY.** The audit stays
`OPEN_AFTER_ROW_SURVEY`, PRELIMINARY, with no confirmatory value.

## 0. Pre-step check

- **Known.** Frozen definition (contract Sec. 1, «Zonotope reading»): a
  walk in the product class is «a product of `n` coin–partial-shift
  factors, each partial shift moving by `±a_i`»; then
  `F = {sum_i ε_i a_i}` and `C_micro` is the zonotope `sum_i [-a_i, a_i]`;
  reduced generators are the `a_i` «up to sign and positive scale, parallel
  ones merged». Audit F2 said that identity presupposes every sign pattern
  has nonzero amplitude. **Corrected (repair 2):** that condition is
  sufficient, not necessary. Three things must be kept apart: the
  individual pattern amplitudes, the support `F` (where coincident
  patterns add), and the convex hull. By Lemma V (Sec. 1), `conv F = Z`
  iff every vertex of `Z` is in `F`; non-vertex patterns may vanish without
  changing the hull (e.g. two identical factors `P_+ T(a) + P_- T(−a)`:
  the mixed patterns vanish, `F = {±2a}`, `conv F = Z`). Equality of `F`
  with the full set of candidate sums needs, in addition, the summed
  amplitudes at coincident displacements.
- **Question.** For each `s = 2` row of the audit: is it in the product
  class (cited), what are its factor shifts and reduced generators, and do
  the sign patterns have nonzero amplitude in the certified support?
- **What ends it.** Every row resolved closes G1; any row that cannot be
  resolved from the record leaves G1 open with that row named.

## 1. Two facts used throughout [hand]

**Lemma V (vertex patterns are unique).** If every `a_i ≠ 0`, each vertex
`v` of `Z = sum_i [-a_i, a_i]` is the sum of exactly one sign pattern.
Proof: `v` uniquely maximizes some linear functional `φ` with
`φ(a_i) ≠ 0` for all `i`; any pattern summing to `v` also maximizes `φ`,
which forces `ε_i = sign φ(a_i)`. Hence coincident displacements (several
patterns, one point) occur only at non-vertices, and the amplitude at a
vertex is the amplitude of a single pattern: it is nonzero **iff** the
vertex is in the certified support. In particular `conv F = Z` iff every
vertex of `Z` is in `F`.

**Lemma P (pattern amplitudes, rank-one projectors).** If factor `i` is
`sum_{s=±} Q_i^s T(s a_i)` with `Q_i^±` rank-one projectors on `C^2`
(Bloch vectors `±q_i`), the amplitude of pattern `(s_1, …, s_n)` is
`Q_n^{s_n} … Q_1^{s_1}`, nonzero iff no consecutive pair
`s_i q_i`, `s_{i+1} q_{i+1}` is antipodal; for `s_i = s_{i+1}` this means
`q_{i+1} ≠ −q_i`, for `s_i ≠ s_{i+1}` it means `q_{i+1} ≠ q_i`. For the
conjugated JDW factors `R^{-1} S R` with `R = U(0, π/2, 0, θ)` (JDW Eq. (1),
`verify_c_across_lattices_gate.py` l. 92–97), the projector of the L
component is onto `R^† |0⟩ = (−i cos θ, sin θ)`, Bloch vector
`m(θ) = (0, sin 2θ, cos 2θ)`.

## 2. Row-by-row trace

Coordinates are the generator coordinates of each constructor; Cartesian
values are given where directions are compared.

### L1, L2, L3 (standard battery)

- **Product class: yes, literal.** `verify_weyl_dirac_gate.py`
  `rotation_product` (l. 80–88): one factor per axis,
  `z_a P_a^+ + z_a^{-1} P_a^-`, `P_a^± = (I ∓ sign σ_a)/2`; the check
  «published vs product» (l. 145) makes the published symbol equal to this
  product for all seven cases (CS Sec. 5, PASS). B cases: transpose of the
  product, again a product of axis factors (`σ_y^T = −σ_y`). L1, L2 use
  `published_symbol(d, 1, ·)` (`verify_c_across_lattices_gate.py` l. 504).
- **Factor shifts:** `±e_a`, `a = 1..d` (scaled by `1/sqrt d` in the
  normalized units). **Reduced generators:** `d` orthogonal directions of
  equal length.
- **Patterns:** `2^d`, all with distinct displacements (the corners). The
  certified support is exactly the corners («active support», l. 150–152).
  So every pattern has nonzero amplitude, and `conv F = Z`.
  [hand, Lemma P] consistent: Bloch vectors along orthogonal axes are
  never antipodal.

### L5a (Farrelly–Short, axis product)

- **Product class: yes, literal.** `row_L5a` (l. 167–189):
  `T_b = z^{e_b} (I+σ_b)/2 + z^{-e_b} (I−σ_b)/2`, product `T_x T_y T_z`.
- **Factor shifts:** `±e_b`. **Reduced generators:** 3 orthogonal.
- **Patterns:** 8, distinct displacements; the support is asserted equal to
  `{±1}^3` (l. 187–188). All nonzero; `conv F = Z`.

### L4, walk CJWW (5.12)

- **Product class: yes, literal.** Source PDF p. 16:
  `W = e^{i p_1 σ_1} e^{i p_2 σ_2} e^{i p_3 σ_3}`, each factor
  `sum_ε e^{i ε p_a} (I + ε σ_a)/2`; constructor
  `verify_directional_saturation.py` `walk1` (l. 64–69).
- **Factor shifts:** `±e_a`. **Reduced generators:** 3 orthogonal.
- **Patterns:** 8, distinct; support asserted exactly the 8 cube vertices
  (`verify_directional_saturation.py` l. 136–140; verifier promoted, CS
  l. 754–755). All nonzero;
  `conv F = Z`.

### L4, walk CJWW (5.15) — **not resolved**

- **Product class: not established.** The source prints `W` as a `2×2`
  matrix (PDF p. 17), not as a product of coin–partial-shift factors, and
  the constructor `walk2` (l. 72–78) transcribes it entry by entry. No
  factorization is in the reviewed record. Its support is asserted to have
  14 vectors containing the 8 vertices (l. 142–147), but factors may not be
  inferred from it (user rule). **Gap G1-b.**

### L6e (JDW isosceles, three-step)

- **Product class: yes, literal, in the printed presentation.** `row_L6e`
  (l. 352–364): `W^0 = W^3 W^2 W^1`, `W^j = U^j S^j`,
  `U^j = U(0, 0, −π/2, (j−2) π/4)`, `S^j` reads L at `N_j` and R at
  `N_{j+3} = −N_j` (ISO table, l. 348), so each partial shift moves by
  `±N_j`.
- **Factor shifts:** `N_1 = (1,−1)`, `N_2 = (1,0)`, `N_3 = (0,1)` (ISO
  coordinates); Cartesian (generators l. 349) `(1,0)`, `(1/2,1/2)`,
  `(−1/2,1/2)`. **Reduced generators: 3 directions** in `d = 2`
  (`N_1 − N_2 + N_3 = 0`).
- **Patterns [hand]** (`+` designates the R component, which moves by
  `+N_j`; L moves by `−N_j`, since `jdw_shift` reads L at `X + N_j`):
  `(+,+,+) → (2,0)`, `(+,+,−) → (2,−2)`,
  `(+,−,+) → (0,0)`, `(+,−,−) → (0,−2)` and negatives (ISO). The zonotope
  of the three generators is a hexagon with vertices `±(2,0)`, `±(2,−2)`,
  `±(0,2)` (ISO). The asserted support is
  `{(−2,0), (0,−2), (0,2), (2,0)}` (l. 70, asserted l. 684): the vertices
  `±(2,−2)` and the point `0` are **absent**. By Lemma V the patterns
  `±(+,+,−)` have zero amplitude. [hand] Cause: `U^2 = U(0,0,−π/2,0) = I`,
  so `P_{s_3} U^2 P_{s_2} = 0` when `s_2 ≠ s_3`; the four patterns with
  `s_2 ≠ s_3` vanish individually (including the two at `0`), the four
  with `s_2 = s_3` do not (`U^1` has both entries nonzero).
- **Consequence:** in the printed presentation `conv F` (a square) is not
  the zonotope (a hexagon): the vertex condition (corrected F2, Sec. 0) **fails** for L6e. [hand]
  Because `U^2 = I`, factors 2 and 3 combine into one partial shift by
  `±(N_2 + N_3) = ±(1,1)` (ISO) = `±(0,1)` (Cartesian); in that
  presentation there are 2 orthogonal reduced generators, all 4 patterns
  are nonzero, and `conv F = Z`. **The reduced generators of L6e therefore
  depend on the presentation (3 or 2).** Which presentation the frozen
  definition intends is not documentary. **Gap G1-c.**

### L6a (ADMP honeycomb, Eq. (7)/(10))

- **Product class: yes, literal.** `row_L6a` (l. 227–299):
  `prod_i sum_s Π_i^s T(s u_i)`, `Π_i^±` eigenprojectors of `τ_i`.
- **Factor shifts:** `u = (1,0), (−1,1), (0,−1)` (TRI); Cartesian
  `(1,0)`, `(−1/2, √3/2)`, `(−1/2, −√3/2)`. **Reduced generators:** 3
  directions at 120°.
- **Patterns [hand]:** `u_0 + u_1 + u_2 = 0`, so `±(+,+,+) → 0` (two
  coincident patterns, interior) and the other six give the hexagon
  vertices `±2u_i`. Asserted support (l. 67, l. 684) contains the six
  vertices and `0`: by Lemma V all six vertex patterns are nonzero;
  `conv F = Z`. At `0` the support shows only that the sum of the two
  patterns is nonzero. [hand, Lemma P] individually nonzero: the Bloch
  vectors of `τ_0, τ_1, τ_2` (l. 235–237) are distinct and pairwise not
  antipodal.

### L6d (JDW equilateral, three-step)

- **Product class: yes, literal.** `row_L6d` (l. 332–345):
  `R~2^{-1} S~3 R~2 R~1^{-1} S~2 R~1 S~1`, `U_j = 1`; `S~j` reads L at
  `N_j`, R at `N_{j+3} = −N_j` (TRI table, l. 308).
- **Factor shifts:** `N_1 = (1,0)`, `N_2 = (0,1)`, `N_3 = (−1,1)` (TRI);
  Cartesian `(1,0)`, `(1/2, √3/2)`, `(−1/2, √3/2)`. **Reduced
  generators:** 3 directions at 60°.
- **Patterns [hand]:** `N_1 − N_2 + N_3 = 0`, so `±(+,−,+) → 0` (two
  coincident, interior); the other six give `±2N_j`. Asserted support
  (l. 69) contains them: vertices nonzero, `conv F = Z`. [hand, Lemma P]
  Bloch vectors `m(0), m(π/6), m(π/3)`, consecutive ones neither equal nor
  antipodal: all 8 patterns individually nonzero.

### L6f (JDW honeycomb, three-step) — **partial shifts not of the form ±a**

- **Product of coin–partial-shift factors: yes.** `row_L6f` (l. 370–385):
  `W_j = U_j^{-1} S_j U_j`; `S_1` reads `(N_1, N_2)`, `S_2` `(N_2, N_3)`,
  `S_3` `(N_3, N_1)` with `HEX = (1,0), (−1,1), (0,−1)` (l. 367). Each
  partial shift moves L by `b_j = −N_a` and R by `c_j = −N_b` with
  `c_j ≠ −b_j`. **The literal clause «each partial shift moving by `±a_i`»
  is not met** by the printed presentation; this does not show that no
  other factorization exists.
- **Affine reading [hand], recorded only:** `b_j = m_j + a_j`,
  `c_j = m_j − a_j` with `a_j = (b_j − c_j)/2`: `a = (−1, 1/2), (1/2, −1),
  (1/2, 1/2)` (TRI), Cartesian `(−3/4, √3/4)`, `(0, −√3/2)`, `(3/4, √3/4)`,
  three directions at 60°; `sum_j m_j = 0`, so `F = {sum ε_j a_j}` holds
  exactly. Patterns: `±(+,+,+) → 0` (two, interior), six vertices
  `(−1,−1), (−1,2), (−2,1)` and negatives, equal to the asserted support
  (l. 71): vertices nonzero, `conv F = Z`. [hand, Lemma P] `m(π/6),
  m(π/2), m(5π/6)`: all 8 patterns individually nonzero.
- **Gap G1-a:** whether a product with asymmetric partial shifts belongs to
  the frozen product class is a definitional decision, not documentary.

### L6c (JDW equilateral, six-step) — **partial shifts not of the form ±a**

- **Product of coin–partial-shift factors: yes.** `row_L6c` (l. 312–329):
  `prod_j R_j^{-1} S_j R_j`, `S_j` reads L at `N_j`, R at `N_{j+1}`;
  `c_j ≠ −b_j`. **Literal clause not met** by the printed presentation;
  this does not show that no other factorization exists.
- **Affine reading [hand], recorded only** (orientation: `+` designates
  R; with `b_j` the L displacement and `b_j = m_j + a_j` as for L6f, the
  `a_j` below carry the opposite sign, which does not change the reduced
  generators, defined up to sign): `a_j = (N_j − N_{j+1})/2`:
  `(1,−1)/2, (1,0)/2, (0,1)/2` and their negatives (`a_{j+3} = −a_j`);
  `sum_j m_j = −sum_j N_j = 0`. **Reduced generators** (parallel merged):
  3 directions at 60°, Cartesian `(1,0)`, `(1/2, ±√3/2)`, each of merged
  length 1. 64 patterns onto the 19 points of the asserted support (l. 68):
  many coincident displacements at non-vertices; the six hexagon vertices
  of radius 2 are single patterns (Lemma V) and are in the support:
  `conv F = Z`. [hand, Lemma P] consecutive `2θ_j` differ by `π/3`: all 64
  patterns individually nonzero.
- **Gap G1-a** as for L6f.

## 3. Summary

| Row | Product class (literal) | Factor shifts / reduced generators | Vertex patterns in certified support | Coincident displacements |
| --- | --- | --- | --- | --- |
| L1, L2, L3 | yes (`rotation_product`, l. 145) | `±e_a`; `d` orthogonal | all | none |
| L5a | yes (l. 167–189) | `±e_b`; 3 orthogonal | all | none |
| L4 (5.12) | yes (p. 16; `walk1`) | `±e_a`; 3 orthogonal | all | none |
| L4 (5.15) | **not established** (G1-b) | — | — | — |
| L6e | yes, printed presentation | 3 directions (printed) or 2 orthogonal (factors 2–3 merged, `U^2 = I`) — **G1-c** | **no** for the printed presentation (`±(2,−2)` absent); yes for the merged one | `0`, two patterns, both zero |
| L6a | yes (l. 227–299) | `u_i`; 3 at 120° | all | `0`, two patterns |
| L6d | yes (l. 332–345) | `N_j`; 3 at 60° | all | `0`, two patterns |
| L6f | **no**: asymmetric partial shifts (G1-a) | affine: 3 at 60° | all (affine) | `0`, two patterns |
| L6c | **no**: asymmetric partial shifts (G1-a) | affine: 3 at 60°, merged pairs | all (affine) | 64 patterns on 19 points |

**Outcome of the trace: G1 is not closed.** Resolved documentarily: L1,
L2, L3, L5a, L4-(5.12), L6a, L6d. Open, named:

- **G1-a** (L6c, L6f): asymmetric partial shifts; product-class membership
  needs a definitional decision (the affine reading makes the frozen
  formula `F = {sum ε_i a_i}` hold exactly, since `sum m_j = 0`).
- **G1-b** (L4-(5.15)): no factorization in the source or in the reviewed
  constructor.
- **G1-c** (L6e): the reduced generators depend on the presentation; in
  the printed one, four sign patterns vanish (two at the missing vertices
  `±(2,−2)` and two at `0`) and `conv F` is not the zonotope.

**Finding recorded, no verdict (frozen Sec. 1: phase 0 gives no verdict on
(PS′)).** L6e is literally in the product class in its printed
presentation, has three reduced generators in `d = 2`, and saturates
(`c_0 = r_in`, c-across-lattices l. 142). (PS′) as written («the ceiling is
attained iff the generators reduce to `d` independent directions») would
need either the vertex condition (corrected F2) or a rule fixing the presentation to apply
to it. This is a concrete instance of the corrected F2 (vertex patterns vanish); it bears on (PS′) only, not on
(PH), and is not evidence for or against either.

The audit's definitional outcome stays **`OPEN_AFTER_ROW_SURVEY`**,
PRELIMINARY, with no confirmatory value; the counterexample outcomes are
unchanged. This trace is not promoted and authorizes nothing; external
review is the user's decision.
