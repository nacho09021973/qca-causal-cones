# HEX_SUPREMUM (M1): Stage A and the 13-point support

**Date:** 2026-11-03. **Branch:** `research/schur-stability-audit`.
**Contract:** [`HEX_SUPREMUM_GATE.md`](../theory/HEX_SUPREMUM_GATE.md),
preregistration commit `86573ca`; authorization CURRENT_STATE Sec. 14
(`762ecdb`), user instruction «adelante» for Stage A.
**Author:** Claude Code (Claude Opus 5.5). **Verifier:**
`scripts/verify_hex_supremum_gate.py`, 12/12, SHA-256 `ef4b0114…`; imports
read-only the reviewed `verify_hex_ceiling_gate.py` (SHA-256 `8f3b7a10…`,
unchanged). **Solver budget used:** 0 s on S13 (no solver run); 0 s on
S19 (not started). No numerics. **Status: PRELIMINARY,
INDEPENDENT_REVIEW_PASS_TWO_HOUSES; promoted 2026-11-03 for S13 (CURRENT_STATE
Sec. 14).**

**Review (2026-11-03).** Grok PASS and Gemini PASS on all five blocks, no
mandatory repair, identical input (this report at SHA-256 `8a4c4eec…`,
before this paragraph)
([Grok](../debates/2026-11-03--hex-supremum-stageA-review-grok/informe_grok.md),
[Gemini](../debates/2026-11-03--hex-supremum-stageA-review-gemini/informe_gemini.md),
[author reading](../debates/2026-11-03--hex-supremum-stageA-review-grok/verificacion_autor.md)).
Accepted clarification (Grok): the "second route" of Sec. 3 is not an
independent derivation; the layer equations already contain `A_h = 0` on
each singleton, so the exact solve confirms the same geometry in algebra.
The body below is unchanged.

**Pre-step check.** Known: facet-line rigidity and the minimal-support T2
(hex-ceiling report Sec. 3, CURRENT_STATE Sec. 12). Question: what do the
saturation conditions force before any solver, and does that decide S13?
Abandonment: if Stage A forced nothing beyond the layer sums, S13 would go
to an exact solver within the per-support budget.

## 1. Stage A: two consequences of saturation valid for every support

Notation of the hex-ceiling report: `U(k) = sum_{h in F} A_h e^{-ik.h}`,
`C = conv F` a regular hexagon, `|vertex| = 1`, `r = r_in = sqrt3/2`,
normal form `A(n) = r n.sigma` (Step 2 there). Suppose `c_0 = r_in`.

**Lemma A1 (singleton layer).** Let `n_f` be a facet normal and `delta`
the spacing of the projections of `Lambda` onto `n_f` (they lie on a
uniform grid, L0 of the parent gate). If a layer strictly between the two
extreme ones contains exactly one point `h` of `C cap Lambda`, then
`A_h = 0`.

*Proof.* By facet-line rigidity (hex-ceiling report Sec. 3, Step 1:
Bernstein equality / Julia, prior art), `U(t n_f) = e^{-irt} P_+(n_f) +
e^{irt} P_-(n_f)`, so the sum of `A_h` over each intermediate layer is 0.
A layer with one point gives `A_h = 0`. ∎

**Lemma A2 (opposite vertices).** For every vertex `v` of `C`,
`A_v A_{-v}^dag = 0` and `A_{-v}^dag A_v = 0`.

*Proof.* The coefficient of `U U^dag` at displacement `2v` is
`sum_{h - h' = 2v} A_h A_{h'}^dag`. Since `C` is centrally symmetric,
`h - h' = 2v` with `h, h' in C` means `(h + (-h'))/2 = v` with both in `C`;
`v` is extreme, so `h = v`, `h' = -v`. The coefficient must vanish
(`2v != 0`); likewise for `U^dag U`. ∎

A2 is recorded for later stages; it is not used for S13. Neither lemma
alone gives a gap proof for `W_hex^sym`.

## 2. Supports (verifier)

Closed regular lattice hexagons with vertex `v`, in increasing size:
`S7` (`v = g_1`, 7 points), `S13` (`v = g_1 + g_2`, 13 points), `S19`
(`v = 2 g_1`, 19 points). After normalising `|v| = 1`, S13 consists of the
origin, an inner ring of six points with `|h| = 1/sqrt3` at angles
`k pi/3`, and six vertices at `pi/6 + k pi/3`.

## 3. M1-B13: the 13-point support reduces to minimal support

Facet normals of S13 point at angles `k pi/3`, i.e. through the
inner-ring points. Along each, the projections lie on the grid
`delta = r/3` with levels `-3..3`; the layers are, top to bottom: two
vertices; **one inner-ring point**; two inner-ring points; origin and two
vertices; two inner-ring points; **one inner-ring point**; two vertices
(verifier). By A1 the two singleton layers force their coefficients to 0.
The three normals cover all six inner-ring points, so every inner-ring
coefficient vanishes and `F within {0} U vert(H)`.

Second route (rule 4): with generic coefficients on all 13 points, the
exact solution of the full set of layer equations along the three normals
forces every inner-ring coefficient to 0 (verifier). Both routes agree.

The surviving support is the configuration of the minimal-support T2 up
to a similarity: rotating space by `-30°` (jointly with the Bloch sphere
about `z`, which keeps `A(n) = r n.sigma`) maps the six vertices to
`(cos k pi/3, sin k pi/3)` (verifier). The T2 proof uses only the geometry
of the seven points, unitarity, the node and isotropy: its layer
equations and its set of differences `h - h'` are invariant under
similarity, and the lattice never enters (`verify_hex_ceiling_gate.py`,
`check_T2_minimal`, lines 166-238, which encodes the vertices abstractly).
The T2 check is rerun read-only and passes (4/4).

**Verdict.** M1-B13 `PROVED_FOR_S13`: no s=2 walk with `F within S13`
(in `W_hex^sym`, hence in `W_hex`) reaches `c_0 = r_in`. HX2
`CONFIRMED_FOR_S13` (and for S7 by T2). No supremum is claimed on S13
beyond what T1 gives; the gap is qualitative.

## 4. S19 is not reduced by A1

In S19 the facet-normal layers have sizes 3, 4, 5, 4, 3 on every normal
(verifier): no intermediate singleton, so A1 forces only the layer sums,
as in the 900 s attempt of the parent gate. S19 contains JDW L6c
(`c_0/r_in = sqrt3/2`). Lemma A2 and the edge identities of the contract
(Sec. 4, Stage A, step 2) are the remaining structural input before any
solver.

## 5. Verdicts so far

- M1-A: `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS` for the whole class (A1, A2
  proved; no gap proof for `W_hex^sym`, no normal form for general
  supports).
- M1-B13: `PROVED_FOR_S13`.
- M1-B19: not started. Per the contract it may now start (S13 has a
  verdict), with at most 3600 s of cumulative solver time.
- HX2: `CONFIRMED_FOR_S13`; OPEN in general.

## 6. Not established

- Nothing for S19 or larger hexagons; nothing for `s > 2`.
- The line M1 is neither closed nor kept by this: S13 is a bounded support.
- No novelty claim: A1 is a direct use of the Bernstein equality case
  (prior art); A2 is the standard extreme-coefficient argument.

## 7. Next step

M1-B19 (user decision on when), then independent cross-family review and
a separate promotion.
