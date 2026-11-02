# L6b triangular row — execution

**Date:** 2026-11-02
**Gate:** `L6B_TRIANGULAR_ROW`, contract
[`theory/L6B_TRIANGULAR_ROW_GATE.md`](../theory/L6B_TRIANGULAR_ROW_GATE.md),
preregistration commit `b076670` (contract SHA256
`28081b0cd8536bceeb732c6740a07b53239ed8d32a678e52d8177b0b60259829`).
**Parent:** `C_ACROSS_LATTICES`, row L6b.
**Source:** ADMP `sources/1803.01015v2.pdf` (SHA256 checked against
`sources/README.md`), Sec. IV p.4, Eqs. (9), (11), (12), Fig. 1; read on
2026-11-02.
**Verifier:**
[`scripts/verify_l6b_triangular_row_gate.py`](../scripts/verify_l6b_triangular_row_gate.py),
64/64 exact checks (Python 3.12.3, `sympy==1.14.0`, run from the repo root
with `python -B`). It imports the reviewed parent verifier read-only; that
file is unchanged.
**Status:** `L6B_PARTIAL_VGRP_OPEN` — PRELIMINARY, independent review
pending. Nothing is promoted by this report.

## 1. Result

| Quantity (normalised: longest one-update step = 1) | L6b, massless |
| --- | --- |
| internal dimension `s` (translation-invariant form) | **6** (three edges per unit cell, `C^2` each) |
| step set `F` of one update | 6 vectors of length 1/2 side, at 60° spacing; `0 ∉ F` |
| `C_micro` | regular hexagon, `r_in = sqrt3/2`, `V_causal^max = 1` |
| `c_0` (isotropic, untilted) | **1/3** |
| `c_strict^iso` | **1/sqrt3** |
| `c_0 / r_in` | `2 sqrt3 / 9` |
| `c_strict^iso / r_in` | **2/3** |
| `S_min = c_0 / V_causal^max`, `S_max = c_0 / r_in` | `1/3`, `2 sqrt3/9` |
| `V_grp^max` | `OPEN` (not certified) |
| `c_0` in source units (side `sqrt3`, one update) | `sqrt3/6`, equal to the source's coefficient |

Hypotheses of the parent gate, for this row (contract Sec. 5):

- **Ha:** `s = 6`, so L6b is outside Ha's scope. Ha stays
  `REFUTED_BY_ROW_L6a`.
- **Hb:** **fails**: `c_strict^iso = 1/sqrt3 < r_in = sqrt3/2`. Parent Hb
  becomes `REFUTED_BY_ROW_L6b`.
- **Hc:** holds: `c_0 = 1/3 <= 1/sqrt3`. With L6b decided, parent Hc holds
  in every declared row: `CONFIRMED_IN_DECLARED_ROWS`.

All entries are identical for the two admissible colourings and for both
readings of the coin (Sec. 3).

## 2. Encoding (contract Sec. 2)

The parent verifier left L6b unencoded because the labelling seemed fixed
only by Fig. 1. The text fixes it. Two statements on p.4 suffice:
(i) glued triangles share the side label ("triangle `v0` (white) and `v1`
(grey) are glued along their `k = 1` side, then `psi(t,v0,1) =
psi(t,v1,1)`"); (ii) `R` sends side `k` to side `k+1` anticlockwise in
every triangle. The verifier computes the anticlockwise successor of edge
orientations from exact midpoints: it is `h -> b -> s -> h` in both up and
down triangles. Enumerating all 72 candidates (2 colourings × 6 white
labelings × 6 grey labelings), exactly 6 satisfy (i)–(ii): two colourings
times the three rotations of one cyclic labeling. The labeling read from
Fig. 1 (white upward; bottom 2, right 0, left 1) is one of them. The update
uses only "side `k-1` -> side `k`", i.e. the anticlockwise predecessor,
which is the same for the three rotations; so at most the colouring can
change the walk, and it does not change any entry.

The encodings `U_k` of Eq. (11) form an on-site block-diagonal unitary
constant in quasimomentum; the verifier checks that it leaves the support
and the characteristic polynomial unchanged, then works with Eq. (12).

**Internal dimension.** Each edge lies in exactly one up triangle, and no
translation maps up triangles onto down ones, so the unit cell holds the
three edges of one up triangle. The parent table's `s = 2` counts the
`C^2` per edge, not per unit cell. Recorded, not repaired in the parent.

## 3. Coin

`W = U_0 S U_0^dagger` (Eq. (9), `M = I`). The parent verifier recorded two
source sign issues for L6a (Eq. (8) holds for `alpha = -arccos(sqrt5/3)`;
the printed `S` orders the `tau_i` backwards) and used the corrected
matrices. Following parent §6, both are run here: the parent's corrected
`W` and the `W` as printed. Both are unitary with `W^3 = I`, and every
entry of Sec. 1 is the same for both.

## 4. Derivation of the entries

**`F`, `C_micro`.** In an up triangle the anticlockwise moves between side
midpoints point at 60°, 180°, 300°; in a down triangle at 240°, 0°, 120°.
The move out of an edge on the grey side is minus the move on the white
side. So `F` is six vectors of length 1/2 (side units) and `C_micro` the
regular hexagon, `r_in = sqrt3/2` normalised.

**Node.** `U(0) = P ⊗ W` with `P` the cyclic permutation of the three
edge orientations, so `U(0)^3 = I`. Its spectrum is `{1, e^{±2πi/3}}`, each
with multiplicity 2; the eigenvalue-1 pair is the declared node.

**`c_0`, two routes.** (A) `V = U^3` is block diagonal in edge orientation,
hence a walk on the white-triangle Bravais lattice with `V(0) = I`; the
parent's `node_speeds` gives a Hermitian, untilted, isotropic cone with
`c_0(V) = 1/2` side per three updates. The node branch of `U` has
quasienergy `omega = Omega/3`, so per update `c_0 = 1/6` side, `1/3`
normalised. (B) First-order degenerate perturbation of `U` itself on the
eigenvalue-1 space: generator `Q^dagger (i U(0)^dagger dU/dk) Q`,
untilted, isotropic, same `c_0`. Both routes agree exactly.

**`c_strict^iso`.** Every one-step vertex coefficient is nilpotent: the
edge orientation advances at every update, so the same move cannot be
repeated. With `h_infty(n̂) = limsup_n (1/n) max_{x in S_n} n̂·x`
(`theory/B_STAR_HYPOTHESIS.md`, from `CAUSAL_BODY_GEOMETRY.md` Sec. 6):
`supp U^3 = {0, ±2w_o}`, a hexagon of radius 1 side, and all six vertex
coefficients of `U^3` are non-nilpotent. For `V = U^3`, a translation-
invariant walk, the coefficient of `V^m` at `m v` for a vertex `v` is
`M_v^m`, nonzero; and `supp U^n` lies within a bounded distance of
`supp U^{3⌊n/3⌋}`. Hence `h_infty = h_{conv supp U^3} / 3`, inradius
`sqrt3/6` side per update, `1/sqrt3` normalised. The asymptotic body is
the hexagon `(1/3) sum_o [-w_o, w_o]`, with the same orientation as
`C_micro` (vertices at multiples of 60°) and scaled by 2/3.

## 5. Cross-checks against the source (contract Sec. 4)

- **Coefficient.** The source states `i d_t psi = (sqrt3/6)(p·sigma) psi`
  per update `epsilon`, with side-midpoint distance `sqrt3/2`, i.e. side
  `sqrt3`. The computed `c_0` in those units is `sqrt3/6`. Agrees.
- **Equivalence with L6a.** `supp U^3` equals L6a's `F` in the same
  integer coordinates (generators halved). Each orientation block of `U^3`
  has the characteristic polynomial of the L6a symbol **up to an isometry
  of the hexagon**, not in the same orientation: the first run of the
  verifier tested the identity isometry only and that check failed (all
  three blocks). Re-derived: L6b's three moves from edge `h` are at 60°,
  180°, 300°, L6a's partial shifts at 0°, 120°, 240°. The repaired check
  tries all 12 isometries; the matching ones are the rotations by 60°,
  180°, 300° and three reflections, for every block. So three L6b updates
  realise the L6a dispersion at half the length scale, rotated 60°.

## 6. What this does not claim

- No statement about the ADMP massive row (still `OPEN` under the parent),
  about `V_grp^max`, or about any other row.
- Hb's failure is one row of a declared list, caused by a walk whose
  translation cell carries three edge orientations visited cyclically. It
  is not a general QCA law, and it does not contradict
  `c_strict^iso <= r_in`, which it satisfies.
- No novelty claim. Not human review.

## 7. Next step

Independent cross-family review of this report and of the verifier
(SHA256 `c2e91c237b023abde1199f8ef3bea143f49e559da35899c01e049a9ddf3f2441`
at the run recorded here), then a separate promotion decision.
