# Research lines: what is known, the open question, the abandonment result

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit` (equal to
`main` at `ba73dd2`). **Nature of this text:** planning record written by an
AI (Claude) at the user's instruction. It is not a result, promotes nothing
and authorizes nothing; every gate still needs its own charter and the
user's authorization. Judgments about relevance are PRELIMINARY; every
"known" item cites the section of `state/CURRENT_STATE.md` (CS) or the
report it comes from.

## 0. The rule

User instruction, 2026-11-02: before every new experiment, calculation or
code modification, state (1) what is already known, (2) the concrete
question, and (3) the result that would make us abandon the line. Gate
charters already freeze a background (1) and a single question (2); their
verdicts are per hypothesis. What they have not stated is (3) for the
*line*: the outcome after which the line is not worth continuing. From now
on each charter states it (`PROJECT_INSTRUCTIONS.md`, rules for successor
gates; `AGENTS.md`).

## 1. What is known about c (the repo's stated goal)

The user's goal is how much `c` is on different substrates (CS Sec. 11
authorization). Known, at the level stated:

| # | Fact | Level and source |
| --- | --- | --- |
| K1 | `c_0 <= c_strict^iso` in every direction | PROVED_UNDER_FROZEN_CONTRACT, one independent review (CS Sec. 7.2) |
| K2 | `c_strict^iso <= r_in(C_micro)` in general | CS Sec. 4 (B_infty^* paragraph) |
| K3 | `c_0` is not fixed by the substrate: on the BCC step set `N_3` the s=4 family has `c_0 = a/sqrt3` for every `0 < a < 1`; on one hexagonal substrate ADMP and JDW L6d give `c_0/r_in = 1/sqrt3` and `sqrt3/2` | COUNTEREXAMPLE_VERIFIED (CS Sec. 4.1); promoted rows (CS Sec. 11) |
| K4 | `c_0 = r_in` is attained on the line, square and BCC/cubic rows | promoted in declared rows (CS Sec. 11) |
| K5 | Hexagonal substrate: `c_0/r_in <= sqrt3/2` in the `n = 3` antipodal subclass; no minimal-support s=2 walk reaches `r_in`; whole class OPEN | promoted (CS Sec. 12) |
| K6 | `C_infty^strict = C_micro` in every computed row; L6b is the one declared row with `c_strict^iso < r_in` | promoted (CS Sec. 11, L6b) |
| K7 | Massive sectors: `c_H != c_{omega^2}` for `0 < m < 1`; exact finite-mass B* rejected in the standard Dirac family | CS Sec. 4 table |
| K8 | Lowest dispersion correction per row; in the `beta` rows the radial group speed near the node is `c_0 (1 + 2 beta t + ...)`, so it exceeds `c_0` in the directions with `beta > 0` | promoted (CS Sec. 13); report Sec. 3.5 |
| K9 | No absolute value of `c` in physical units is derivable in the frozen flat class | `NO_ABSOLUTE_SCALE_DERIVABLE` (CS Sec. 8.21) |

Consequence for the goal, read off K1–K5 and K9: in the declared classes
`c` is not a number fixed by the substrate. What the substrate fixes is an
upper bound, `c_0 <= r_in(C_micro)`, and the walk decides where below it
`c_0` falls. The residual substrate question that is still well posed is
the supremum of `c_0/r_in` over a stated class of walks on each substrate,
and which walks attain it. It is decided for line, square and BCC (value
1) and open only for the hexagonal substrate beyond the subclasses in K5.

## 2. Lines, open question and abandonment result

| Line | Known | Concrete open question | Result that ends the line |
| --- | --- | --- | --- |
| **M1. Hexagonal supremum** (CS Sec. 12, T2) | K4, K5; exact Groebner on the 19-point ball did not finish in 900 s | Does any s=2 walk in `W_hex` reach `c_0 = r_in`? | (a) An explicit witness reaching `r_in`: then every declared substrate has supremum `r_in`, the per-substrate supremum reduces to the inradius bound (Bernstein, prior art) and the line has nothing substrate-specific left; close it. (b) No exact method finishes within one session: stop at `OPEN_AFTER_<analysis>`, no numerics. A gap proof keeps the line. |
| **M2. `V_grp^max` per row** (CS Sec. 11, 13) | K8: above `c_0` near the node in the `beta` rows; bounded by `V_causal^max` | In each declared row, what is `V_grp^max` exactly, and does it depend on the walk beyond `C_micro`? | If in every row it equals `V_causal^max` or follows from `C_micro` alone, the row-by-row computation adds nothing to the goal; close. |
| **A. IR universality** (CS Sec. 4) | OPEN; K3 shows free species on one substrate do not share `c_0` unless tuned | Is there an in-scope (free, homogeneous) mechanism that forces two species to one `c`? | If every candidate mechanism needs interactions, the question is outside PROJECT_INSTRUCTIONS §1: record it as out of scope, not as open work. |
| **Massive rows** (CS Sec. 11) | K7; isotropic `c_omega2` absent in the new rows; two ADMP sign issues | Is the ADMP massive row's `c_H` / `c_omega2` pair decidable exactly? | Not needed for the stated goal unless the user asks for `c` at finite mass; no work by default. |
| **Physical line / IR corona** (CS Sec. 8, paper) | Closed in its frozen class; K9 | None chartered | Already met for the absolute scale (K9). No new work unless the paper is revised. |
| **H1** (CS Sec. 9) | `B / OPEN_BLOCKED_METHOD` at the L2 stop; flagged as drift by the user on 2026-11-01 | None that serves the goal | Already met: the stop record names a method obstruction. Proposed: record H1 as abandoned, not paused (user decision). |
| **IR attribution** (CS Sec. 10) | C1, C2a–c, C3 PASS in frozen scopes | None chartered | No question that serves the goal; no work by default. |
| **Dispersion Phase 2** (observational) | Deferred; the charter itself expects `NO_COMPARABLE_OBSERVABLE_READ` and needs the photon identification the claim ceiling forbids | — | Met in advance: do not open. |

## 3. Retrospective check of the last two gates

- `L6B_TRIANGULAR_ROW`: question and background stated; no line-level
  abandonment result. It served the goal directly (it decided Hb).
- `DISPERSION_CORRECTIONS_ACROSS_LATTICES`: question and background
  stated; no line-level abandonment result, and its link to the goal is
  indirect (it describes departures from `c_0`, not `c`). Its useful
  output for the goal is K8.

## 4. Recommendation (not an authorization)

If one more step is taken on the goal, M1 is the one whose answer changes
the reading of section 1 either way. Before chartering it, the method
risk recorded in CS Sec. 12 must be addressed in the charter, with (b)
above as its stop. Otherwise the goal as posed is answered in the declared
classes by section 1, and the right move is to write that answer up rather
than open new computations.
