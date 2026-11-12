# General infrared rate: hypotheses on sixteen walks

2026-11-12. Claude (claude-opus-5-5). Charters
`theory/GENERAL_IR_RATE_POLYHEDRA_DIAGNOSTIC.md` (`af44458`) and
`theory/GENERAL_IR_RATE_ZONOTOPES_DIAGNOSTIC.md` (`ee429de`). Scripts
`scripts/diagnose_general_ir_rate_polyhedra.py` (`9009bde`, tooling fix
`dce71db`) and `scripts/diagnose_general_ir_rate_zonotopes.py` (`ee429de`).
Outputs: `reports/2026-11-12--general-ir-rate-{polyhedra,zonotopes}.json`
and `-stdout.txt`; the failed first six-walk run is kept as
`...-polyhedra-attempt1-stdout.txt` (crash on W6, singular Newton step).
**Floating-point diagnostic. No label is a certificate, a proof that a
hypothesis fails, or a verdict on the theorem.** Nothing reviewed.

## 1. Table

`c_IR`: cone speed at `k = 0`. `slope(0+)`: `d/dt Phi(t n)` at small `t`,
the extent of the zero set of the rate along `n` (so it exceeds `c_IR`
exactly when the walk has ballistic modes faster than `c_IR` in that
direction). `|v_*|`: distance of `B - A` from the origin under the region
rule. Units of each script.

| Id | Body | `Z^d`? | `c_IR` | slope(0+) | `|v_*|` | `K_*` | Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | cube (CJWW 5.15), control | yes | 1 | 1 | 1.232 | 0.19052 | all hypotheses hold |
| W4 | square (Weyl) | yes | 1 | 1 | 1.006 | 0.00087 | all hypotheses hold |
| W2 | cube, BCC (CJWW 5.12) | no | 1 | 1.2247 | 1.232 | 0.0013 | H4′ fails |
| W3 | cube, BCC (Pavia A+) | no | 1 | 1.2247 | 1.232 | 0.0013 | H4′ fails |
| W6 | tetrahedron (s=4) | no | 0.333 | 0.805 | 0.711 | 0 | ballistic corona |
| W5 | hexagon (JDW L6d) | no | 1.5 | 1.5 | 1.423 | 0 | Bob inside the IR cone |
| Z3 | regular hexagon | no | 1.5 | 1.5 | 1.423 | 0 | Bob inside the IR cone |
| Z1 | octagon | yes | 2.414 | 2.414 | 2.249 | 0 | inside the IR cone; no rate axis |
| Z2 | octagon (long axes) | yes | 3.414 | 3.414 | 3.181 | 0 | inside the IR cone; no rate axis |
| Z4 | dodecagon | no | 4.098 | 4.098 | 3.764 | 0 | inside the IR cone; no rate axis |
| Z5 | octagon, other order | yes | 2.414 | 2.414 | 2.249 | 0 | inside the IR cone; no rate axis |
| Z6 | rhombic dodecahedron | no | 2.309 | 2.309 | 2.845 | 0.155 | H4′ fails; no rate axis |
| Z7 | truncated octahedron | yes | 2.828 | 3.029 | 3.181 | 0.037 | H4′, H8 fail; no rate axis |
| Z8 | axes + diagonals | no | 3.309 | 3.779 | 3.696 | 0 | ballistic corona; no rate axis |
| Z9 | great rhombicuboctahedron | no | 3.828 | 4.306 | 4.208 | 0 | ballistic corona; no rate axis |
| Z10 | hexagonal prism | no | 1.5 | 1.525 | 1.778 | 0.089 | H4′, H8 fail; no rate axis |

All sixteen nodes are untilted and isotropic to machine precision. H3, H7
and H9 hold exactly in every row where they were evaluated.

## 2. What the rows show (descriptive, these sixteen walks only)

1. **The hypotheses hold in two walks**: the manuscript's (W1) and the
   square Weyl walk (W4), the second a new case inside the declared class.
   Both have no ballistic mode faster than `c_IR` along the chosen axis
   (`slope(0+) = c_IR`) and zero momentum is a dominant point.
2. **Faster-than-`c_IR` ballistic modes are common.** They appear along
   the chosen axis in W2, W3, W6, Z7, Z8, Z9, Z10. In every such row either
   Bob's region is reached ballistically (`K_* = 0`: W6, Z8, Z9) or the
   tail just outside the ballistic region is controlled by those fast
   modes and zero momentum is not dominant (H4′ fails: W2, W3, Z7, Z10).
   In those rows the theorem does not apply. The rows do not show whether
   the operational rate is then strictly larger than `K_*`; that would
   need a separate proof.
3. **The absence of fast modes is not enough.** Z6 has `slope(0+) = c_IR`
   and `K_* > 0`, yet zero momentum is not dominant (four dominant points,
   none with trivial character). This row has no rate axis (below), so its
   dual point may not be the true one; the observation is weak.
4. **The body's shape does not decide the outcome.** The same cube gives
   all hypotheses (W1) or a failure of H4′ (W2, W3), depending on the
   walk; Z1 and Z5 (same octagon, other factor order) give identical
   numbers here, but only because both regions fall inside the IR cone.
   What matters in these rows is the walk's ballistic region relative to
   `c_IR`, not `conv F`.

## 3. Limits of this run (design faults declared)

- **Region rule.** The rule copied from the manuscript (`|v_*| = 0.711 |V|`)
  places Bob inside the IR cone whenever `c_IR > 0.711 |V|`: W5 and all
  five 2D zonotopes (Z1–Z5). Those rows test nothing about the corona. A
  rule scaled to `c_IR` would be needed; changing it after seeing the
  output is not allowed by the charters, so it needs a new decision.
- **No rate axis.** For the product walks the factor order breaks the
  symmetry of the rate about the chosen vertex (the declared fallback was
  used in Z1, Z2, Z4–Z10). The run then assumes `v_*` on the axis, which
  may be false; `K_*` and the dominant-point structure in those rows are
  for the on-axis dual point and may not be those of the true minimiser.
- Lattices: only W1, W4, Z1, Z2, Z5, Z7 live on a lattice isometric to
  `Z^d`; the rest are outside the declared class regardless of outcome.
- Floating point, grid plus local refinement; a dominant point missed by
  the grid would change H2, H4′, H8.

## 4. A label to check elsewhere in the repository

W3 (Pavia Weyl `A+`, `published_symbol(3, +1)` of
`scripts/verify_weyl_dirac_gate.py`) has the same dispersion as CJWW (5.12)
(`cos omega = c1c2c3 + s1s2s3` in both scripts) and therefore ballistic
modes up to `sqrt(3/2) c_IR` along the body diagonals. The 2026-11-09
observational-signature entry says «L2, L3 have `V_grp^max = c_0`
exactly». If «L3» there is the standard Pavia walk, that sentence is
contradicted by this; if it uses the dispersion gate's labels (where,
per Erratum 1, the row printed L3 is CJWW (5.15)), it is consistent. Not
resolved here.

## 5. What would make the next run informative

A region rule tied to the walk (Bob's nearest velocity at a fixed ratio
above `max(c_IR, slope(0+))` along the axis), and product orders chosen
symmetric (or the minimiser found numerically off the axis). Both are
changes of design and need a new charter.
