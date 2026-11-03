# How much is c on different substrates: the answer in the declared classes

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit`.
**Nature of this text:** synthesis, written by Claude Code (Claude Opus
5.5) at the user's instruction («redacta la respuesta»), of results
already promoted in `state/CURRENT_STATE.md` (CS). No new computation was
run and no verifier was touched. Every statement cites the promoted
section or report it comes from and keeps that result's scope. The text
itself has had no independent review: **PRELIMINARY as a synthesis**;
the results it collects keep their own levels.

**Repairs (2026-11-03).** Grok REPAIR_REQUIRED, ten mandatory repairs
([review](../debates/2026-11-03--c-answer-review-grok/informe_grok.md),
[author reading](../debates/2026-11-03--c-answer-review-grok/verificacion_autor.md)),
all applied; R6 and R8 as citation repairs (the content is in the promoted
gates' execution reports, which the review did not receive). No value
changed. Still PRELIMINARY as a synthesis.

**Pre-step check (PROJECT_INSTRUCTIONS, rule of 2026-11-02).** Known: the
promoted results of CS Secs. 4, 7.2, 8.21, 11, 12, 13 and the L6b row.
Question: what does the repo establish about the value of `c` per
substrate within its declared classes? Abandonment: any statement that
cannot be traced to a promoted section with its scope is dropped; if the
answer needed a new computation, the text stops there.

## 0. Answer

1. **The substrate does not fix `c`.** On one substrate, different walks
   have different `c_0`: on the BCC step set the four-component family
   L3s4 has `c_0 = a/sqrt3` for every `0 < a < 1`, a continuum of values;
   on one hexagonal substrate (the identical substrate of ADMP L6a and JDW
   L6d, CS Sec. 11) the two declared walks have `c_0 = 1/2` and `3/4`
   (units: longest step 1, one update per time unit). The row L6b
   (`s = 6`, a different step set) has `c_0 = 1/3`.
2. **The substrate fixes a ceiling.** `c_strict^iso <= r_in(C_micro)` in
   general, and `c_0 <= c_strict^iso` (proved for the admitted cones and
   the exact support of the full symbol on `N_3`, CS Sec. 7.2; confirmed
   row by row in every other declared row). So `c_0 <=
   r_in(C_micro)` in every declared row: the inradius of the one-step
   causal body bounds the relativistic speed.
3. **Whether the ceiling is reached depends on the substrate and the
   walk.** On the line, square, standard BCC and cube substrates, some
   declared walks reach it (`c_0 = r_in`); on the same BCC step set L3s4
   does not (`c_0 = a/sqrt3 < 1/sqrt3`, CS Sec. 4.1). On the hexagonal
   substrate none of the five declared walks does; in the class of
   three-step antipodal walks the exact supremum is `c_0/r_in = sqrt3/2`,
   and no `s = 2` walk with `F within {0} U vert(H)` reaches `r_in`
   (CS Sec. 12). The rest of `W_hex` is OPEN; nothing is stated for
   `s > 2`.
4. **No absolute value.** The repo derives no value of `c` in physical
   units: in the frozen flat class the absolute scale is
   `NO_ABSOLUTE_SCALE_DERIVABLE`. Every number here is in lattice units.

This is a statement about declared rows and classes, not a QCA law.

## 1. Table per substrate (massless node at `k = 0`)

Units: longest one-update step 1, one update per time unit, so
`V_causal^max = 1` in every row. All values exact.

| Substrate | Rows | `r_in` | `c_0` | `c_0 / r_in` | `c_strict^iso` | Source |
| --- | --- | --- | --- | --- | --- | --- |
| line | L1 | 1 | 1 | 1 | 1 | CS Secs. 5, 11 |
| square | L2, L6e | `1/sqrt2` | `1/sqrt2` | 1 | `1/sqrt2` | CS Secs. 5, 11 |
| BCC (`N_3`) | L3, L5a, L5b | `1/sqrt3` | `1/sqrt3` | 1 | `1/sqrt3` | CS Secs. 4, 5, 11 |
| BCC (`N_3`) | L3s4 (s=4) | `1/sqrt3` | `a/sqrt3`, `0<a<1` | `a` | `1/sqrt3` | CS Sec. 4.1 |
| cube (`C_micro = [-1,1]^3` in CS Sec. 8 units, `r_in = 1`; rescaled here to longest step 1) | L4 | `1/sqrt3` | `1/sqrt3` | 1 | `1/sqrt3` | CS Secs. 8, 11 |
| hexagon (triangular lattice) | L6a (ADMP) | `sqrt3/2` | `1/2` | `1/sqrt3` | `sqrt3/2` | CS Sec. 11; hex-ceiling report T1 |
| hexagon | L6c, L6d, L6f (JDW) | `sqrt3/2` | `3/4` | `sqrt3/2` | `sqrt3/2` | CS Sec. 11; hex-ceiling report T1 |
| hexagon | L6b (ADMP, s=6) | `sqrt3/2` | `1/3` | `2 sqrt3/9` | `1/sqrt3` | L6b row (promoted) |

Readings, each limited to these rows:

- `c_strict^iso = r_in` in every row except L6b, where every one-step
  vertex coefficient is nilpotent and the long-run body is smaller
  (`c_strict^iso / r_in = 2/3`). So `r_in` does not force
  `c_strict^iso = r_in` (row L6b). No source places L6b on the step set of
  L6a/L6d, so this is not a statement that one substrate leaves
  `c_strict^iso` free.
- L6a and L6d sit on the identical substrate (same translation group and
  step set) and differ in `c_0`. Internal dimension `s = 2` does not
  restore uniqueness.
- The directional ratio `S(n̂) = c_0 / h_{C_micro}(n̂)` equals 1 in some
  direction only in the rows with `c_0 = r_in`.
- Different substrates can share `c_0`. L3s4 at `a = sqrt3/2` has
  `c_0 = 1/2`, the value of L6a on the hexagonal substrate. This is
  immediate from the L3s4 continuum (every `c_0` in `(0, 1/sqrt3)` is
  attained on BCC) and is a statement in the units of this table (longest
  step 1, one update per time unit; the `N_3` steps have unit length). In
  units of `r_in` the two rows differ (`sqrt3/2` against `1/sqrt3`). It
  shows that a common `c_0` across substrates is possible by choice of
  coin parameters, not that anything forces it: IR universality (A) stays
  OPEN.
- In the hexagonal subclass the internal parameter enters through
  `c_0,raw^2 = (3/2) l^2 (1 - g)`, i.e. through the overlaps `g_ij`
  weighted by the step products `a_i . a_j` (`= -l^2/2` for `i != j`).
  Pairwise anticommuting coin operators (`g = 0`) give `c_0/r_in =
  1/sqrt2`, not the maximum; the maximum `sqrt3/2` is at `g = -1/2`,
  where the Bloch vectors reproduce the 120° geometry of the steps and
  the operators do not anticommute. What matters is the joint structure
  of step vectors and internal overlaps, not anticommutation alone
  (`reports/2026-11-01--hex-ceiling.md`, T1). Read off that subclass only.

## 2. The ceiling and its scope

- `c_strict^iso <= r_in(C_micro)`: established (CS Sec. 7.2, research
  direction 1; CS Sec. 4).
- `c_0 <= c_strict^iso`: `PROVED_UNDER_FROZEN_CONTRACT` with one
  independent review, for the admitted cones and the exact support of the
  full symbol on `N_3`, including degenerate Floquet nodes and eigenvalue
  collisions after taking powers (CS Sec. 7.2); not for incommensurable
  displacement sets. Outside `N_3` it is
  `CONFIRMED_IN_DECLARED_ROWS` (Hc, CS Sec. 11 and the L6b row), not
  proved.
- Equality `c_0 = c_strict^iso` is not forced: the strong `B_infty^*` is
  `REJECTED IN THE DECLARED s=4 CLASS` (L3s4).
- On the hexagonal substrate: `c_0 <= r_in` on `W_hex` is
  `PROVED_IN_REPO` (classical Bernstein, prior art); the supremum
  `sqrt3/2` is `GAP_PROVED_IN_CLASS` for the `n = 3` antipodal subclass,
  attained iff the coin axes are coplanar at 120°; no `s = 2` walk with
  `F within {0} U vert(H)` reaches the ceiling, `PROVED_FOR_MINIMAL_SUPPORT`;
  the rest of `W_hex` is `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS` (CS Sec. 12).
  Nothing is stated for `s > 2`.

## 3. Away from the node and at finite mass

- **Dispersion** (CS Sec. 13; the group-speed sentence is from the
  promoted gate's execution report,
  `reports/2026-11-02--dispersion-corrections-across-lattices.md`
  Sec. 3.5). Writing `omega = c_0 |k| [1 + beta |k| +
  alpha |k|^2 + ...]`: the lowest correction is the odd term `beta`
  exactly in the rows whose walk group lacks inversion (L5a, L5b, L4, L6a,
  L6b, L3s4), and `alpha` elsewhere. In the `beta` rows the group speed
  near the node, `|grad eps_+| = c_0 (1 + 2 beta |k| + ...)`, exceeds `c_0` in the
  directions where `beta > 0`; so `c_0` is not the largest group speed of
  those walks. L1 is exactly linear. `alpha_0 < 0` in every other row
  except L3s4 for `0 < a < a* = sqrt3 sqrt(17 - sqrt154)/9`. `V_grp^max` itself is OPEN.
- **Finite mass** (CS Secs. 4, 5, 11; the row-by-row readings are from
  the promoted table's execution report,
  `reports/2026-11-01--c-across-lattices.md` Sec. 5). `c_H` and
  `c_{omega^2}` differ for `0 < m < 1` in the standard Dirac family, where
  `c_H < c_{omega^2} < r_in`. In the rows where the
  mass is a separate coin (L5b, L6c, L6d, L6f), `c_H = c_0 theta / sin
  theta > c_0` (a Hamiltonian coefficient, not a propagation speed), and
  `omega^2` has no isotropic quadratic coefficient at finite mass; in L6e
  the linear term itself becomes anisotropic. The ADMP massive row is
  OPEN.

## 4. What this does not establish

- No QCA law, rigidity or classification: the rows are a declared finite
  list from the repo's own constructions and five primary sources
  (`reports/2026-11-01--c-across-lattices.md`).
- Not that the hexagonal substrate cannot reach the ceiling; only the
  `n = 3` antipodal subclass and the `s = 2` minimal-support results of
  CS Sec. 12. Nothing for `s > 2`.
- Not that every declared BCC walk reaches the ceiling: L3s4 does not.
- No closure of `NOVELTY = OPEN` for the hexagonal ceiling.
- No value of `c` in physical units, no statement about our universe, no
  identification of any row's excitation with the photon.
- No IR universality (question A stays OPEN): the table shows that free
  walks on one substrate do not share `c_0` unless chosen to.
- No novelty: Bernstein's inequality and the sources' constructions are
  prior art.

## 5. What is still open, none of it chartered

- Hexagonal supremum in the rest of `W_hex` (CS Sec. 12, T2).
- `V_grp^max` per row; IR universality (A); the ADMP massive row.
