# PH refutation test on hexagon H25

**Date:** 2026-11-04. **Branch:** `research/schur-stability-audit`.
**Contract:** [`PH_REFUTATION_HEX_S25_GATE.md`](../theory/PH_REFUTATION_HEX_S25_GATE.md),
preregistration commit `6eb50c1` (user approval «SI»).
**Author:** Claude Code (Claude Opus 5.5). **Verifier:**
`scripts/verify_ph_refutation_hex_s25_gate.py`, 14/14, SHA-256
`ddf853866d1e249b9de3689030e85d4477bfe310a6bf0b0cc7a22b3f8567e10e`, about
30 s. It imports read-only `verify_hex_supremum_gate.py` (SHA-256
`ef4b0114…`), `verify_hex_supremum_b19.py` (`244bb106…`) and, through them,
`verify_hex_ceiling_gate.py` (`8f3b7a10…`). These are the hashes recorded
in the M1 reports, so the files are unchanged.
**Solver budget used:** 0 s of 3600 s (no nonlinear solver, no numerics).
**Status: PRELIMINARY**, not independently reviewed, not promoted.

**Pre-step check.** Known: no walk of `W_hex^sym` with `F` in S7, S13 or
S19 reaches `r_in` (promoted). Question: does a walk with `conv F = H25`?
Abandonment: if Stage A forced nothing beyond the layer sums, H25 would go to
Stage B within the budget.

## 1. Support (verifier, Part 1)

H25 is the closed regular hexagon with vertex `v = 2 g_1 + g_2`. After
normalising `|v| = 1` it has 25 lattice points, 6 vertices and
`r_in = sqrt3/2`. No lattice point lies in the interior of an edge. The
reflection `y -> −y`, a symmetry of `Lambda`, maps it onto H25′ (vertex
`g_1 + 2 g_2`). H25′ is also checked directly below, so the reflection
argument is not needed.

## 2. Stage A: lemma A1 decides H25 (verifier, Part 2)

The facet normals have explicit radicals, for example
`(sqrt21/7, 2 sqrt7/7)`. Along each of the three normals the projections of
the 25 points lie on the grid `delta = r_in/7`, levels −7..7. Layer sizes,
top to bottom, are the same on every normal:

`2, 1, 1, 2, 1, 2, 2, 3, 2, 2, 1, 2, 1, 1, 2`

The extreme layers are the two vertices of an edge. Each normal has six
singleton intermediate layers. By lemma A1 of the M1 Stage A report (from
facet-line rigidity: every intermediate layer sums to 0), each singleton
coefficient vanishes. Over the three normals the singletons are exactly
the 18 points other than the origin and the six vertices.

Second route (rule 4), not independent of A1: with generic coefficients on
all 25 points, the exact solution of the full layer equations on the three
normals forces those 18 coefficients to 0. The same singleton analysis run
directly on H25′ gives the same result.

So saturation forces `F within {0} U vert(H25)`.

## 3. Reduction to T2 (verifier, Part 3)

Rotating space by `−atan(sqrt3/5)` maps the six vertices of H25 onto
`(cos k pi/3, sin k pi/3)`, the vertex set of the minimal-support T2 of the
hex-ceiling gate; the same holds for H25′ with its own angle. As in the M1
Stage A report (Sec. 3), the space rotation is done jointly with a Bloch
rotation about `z`, so the normal form `A(n) = r n.sigma` is kept. The T2
proof uses only the geometry of the seven points, unitarity, the node and
isotropy, and the lattice never enters. Its reviewed check is rerun
unchanged and passes 4/4: the layer equations force `A_0 = −I/2`, and
unitarity then gives a real quadratic with discriminant `−1/12`, so there
is no real solution.

**Controls (Part 4).** The square-substrate controls of the M1-B19 verifier,
rerun unchanged, pass 5/5: the layer equations, of which A1 is the
singleton case, keep the known saturating square walk. A1 itself has no
nontrivial instance on the square substrate (no singleton layer arises
there), so this control tests the layer equations, not the singleton step
as such.

## 4. Verdicts (contract Sec. 5)

- **H25: `PROVED_FOR_S25`.** No `s = 2` walk with `conv F = H25` or
  `conv F = H25′` (in `W_hex^sym`, hence in `W_hex`) reaches
  `c_0 = r_in`. The gap is qualitative; no bound below `r_in` is claimed.
- **(PH⇒): `NOT_REFUTED_ON_H25`.** Never `CONFIRMED`.
- **HX2: `CONFIRMED_FOR_S25`** (with S7, S13, S19).

## 5. What this does and does not show

- The test could have failed. H25 was not in the source table, and nothing
  fixed the outcome before computing. It ended at Stage A through the same
  mechanism as S13 (singleton layers leaving the T2 configuration), not
  through a new argument.
- **Bounded result.** Only H25 and H25′. The hexagonal class stays OPEN.
  Per the contract this is not evidence for (PH) beyond H25, and it closes
  nothing in phase 0.
- **Pattern noted, not claimed.** S13 and H25 reduce to T2 by A1; S19 does
  not (layers 3, 4, 5, 4, 3). Whether A1 decides every hexagon whose edges
  have no interior lattice point is not examined here (no extension beyond
  H25 is authorized).
- No novelty claim. A1 is a direct use of the Bernstein equality case
  (prior art). The hexagonal prior-art check is not finished.

## 6. Next step

Independent cross-family review, with every imported module attached, then a
separate promotion (user decision).
