# OBSERVATIONAL_SIGNATURE_SATURATION — draft contract

**Status of this text:** frozen at the commit that introduces it (preregistration), written 2026-11-09 by Claude (Opus 5.5) at
user request («si, redáctalo como contrato»); frozen on «si, congélalo y ejecútalo». Earlier draft text said it would freeze at the
commit that introduces it. Nothing in Secs. 3-4 has been computed.
**Parent:** `DISPERSION_CORRECTIONS_ACROSS_LATTICES` (promoted 2026-11-02,
`CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN`). Its Sec. 5
deferred the observational dictionary to "its own charter and its own user
authorization"; this is that charter.
**Initial scientific status: OPEN.**

## 0. Single question

> In the declared rows, is there an observable difference between a walk
> whose low-energy speed is the largest speed its update allows and one
> whose low-energy speed lies below it? Concretely: does any excitation
> outrun c_0, and what time-of-flight signature (sign, order in energy,
> direction dependence) does each row predict, under the explicit
> hypothesis that the row's massless branch is the photon?

## 1. Known (with sources), the question, and what abandons the line

Known:

- Locality: no signal exceeds the microscopic causal body C_micro; in units
  of one longest step per update, V_causal^max = 1 for every declared row
  (`theory/THREE_VELOCITIES.md` Sec. 4; parent Sec. 1).
- An isotropic low-energy cone fits inside C_micro, so c_0 ≤ r_in
  (`theory/THREE_VELOCITIES.md` Sec. 5). For d ≥ 2 and a polytope C_micro,
  r_in < V_causal^max. Hence c_0 = V_causal^max is possible only in d = 1.
- Parent table (`reports/2026-11-02--dispersion-corrections-across-lattices.md`
  Sec. 1 and Sec. 3.5): exact beta(n̂), alpha(n̂) and the node group-speed
  correction |grad eps|/c_0 = 1 + 2 beta t + ... or 1 + 3 alpha t^2 + ...
  for 13 rows. In L1, omega = |k| exactly. In L5a, L5b, L4, L6a and L6b,
  beta is odd and the lowest correction takes both signs with direction.
  V_grp^max is OPEN for every row with d ≥ 2.
- No absolute scale is derivable (4B, `NO_ABSOLUTE_SCALE_DERIVABLE`);
  ell and tau are free, and only ell/tau is fixed by c.

Two saturation notions, fixed here:

- **S_max**: c_0 = V_causal^max. Among the declared rows only L1 can have it.
- **S_in**: c_0 = r_in (ceiling rows: L1, L2, L6e, L3, L5a, L5b, L4 in the
  parent's list). This is "c is the largest isotropic speed the update
  allows".

Question: see Sec. 0.

Abandonment of this observational route: if, in every declared row, no
excitation is shown to outrun c_0 and the signatures of S_in rows and of
non-ceiling rows do not differ in any of sign, order or direction
dependence, the route is recorded as
`NO_DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS` and abandoned for these rows.

## 2. Rows

Exactly the 13 rows of the parent table, with symbols imported read-only
from the scripts listed in the parent contract Sec. 2. No new walk,
lattice, massive row or interacting model. If a constructor does not return
the symbol in the parent's form, the row is `OPEN (symbol not reusable)`.

## 3. Quantities per row (exact, SymPy, zero tolerance)

1. **Super-c witness.** An exact point k* (algebraic coordinates) on the
   massless branch, with branch analyticity at k* checked, such that
   |grad_k omega(k*)| > c_0 is certified exactly. Search is restricted, and
   declared now, to the symmetry rays of each row (coordinate axes, face
   and body diagonals, and the hexagon's vertex and edge directions) with
   |k| on an exact rational grid fixed in the verifier before running. A
   witness proves V_grp^max > c_0. Failing to find one proves nothing
   (`NO_WITNESS_ON_DECLARED_RAYS`, not "V_grp^max = c_0").
2. **Upper bound, optional.** Where an exact global argument exists (as for
   L1, omega = |k|), V_grp^max = c_0 proved. Otherwise `OPEN`.
3. **Signature class**, from the parent coefficients (imported, not
   recomputed), under hypothesis H_gamma of Sec. 4:
   - order n of the leading correction to the arrival time: n = 1 if beta is
     not identically 0, n = 2 if beta = 0 and alpha is not identically 0,
     none if both vanish;
   - sign: delay only, advance only, or both signs with direction;
   - direction dependence: isotropic or anisotropic, with the harmonic
     (n1 n2 n3, cos 3 theta, cos 4 theta, K4, ...).
   Arrival-time shift in the row's units, for a source at distance D and
   energy E: Delta t / (D/c) = -(group-speed correction) at the wavenumber
   of E. ell enters only through E ell / (hbar c) and stays a free
   parameter. No numerical value of ell.
4. **Discrimination table.** S_max row (L1), S_in rows and non-ceiling rows
   side by side in items 1 and 3.

## 4. Explicit hypotheses

- **H_gamma (dictionary hypothesis, not a result):** the massless branch of
  a row is identified with the photon; c = c_0 ell/tau. Every statement in
  Sec. 3 item 3 is conditional on H_gamma. No claim that our universe is a
  QCA or a simulation (`state/CURRENT_STATE.md` Sec. 8.9(iii) claim ceiling
  stands, except that this conditional dictionary is now authorized).
- **Hg (stated before solving):** every S_in row with d ≥ 2 has a super-c
  witness: even when c is the largest isotropic speed the update allows,
  some excitation outruns it.
- **Hh (stated before solving):** no non-ceiling row has an advance-only
  signature: a walk below the ceiling does not show a purely superluminal
  leading correction.

## 5. Not part of this gate

- Comparison with observational bounds (time-of-flight limits from
  astrophysical sources). This needs primary sources read in the original;
  a literature search with `investigacion-gemini` sends text to third
  parties and requires separate user permission; the comparison needs a
  successor charter.
- Any numerical value or bound on ell or on the clock frequency 1/tau.
- Lorentz-violation model building, detector or source modelling.

## 6. Method, budget, stop rules

- Exact arithmetic; witnesses certified by exact inequality (radicals,
  Sturm sequences if needed). Floating point only in a labelled
  illustration file that feeds no verdict.
- One permanent verifier `scripts/verify_observational_signature_gate.py`,
  committed before its first run; failed runs retained; two exact command
  forms in `.claude/settings.json`. Reviewed verifiers imported read-only.
- Bound: one working session. Stop when every row has items 1, 3 and 4
  filled or `OPEN` with reason. No search beyond the declared rays and grid.

## 7. Verdicts

- Per row: `SUPER_C_WITNESS` / `NO_WITNESS_ON_DECLARED_RAYS` /
  `V_GRP_MAX_EQUALS_C0_PROVED`; signature class or `OPEN`.
- Hg, Hh: `CONFIRMED_IN_DECLARED_ROWS` / `REFUTED_BY_ROW_<Id>` /
  `DECIDED_BY_PARENT_TABLE`.
- Route: `DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS` /
  `NO_DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS` /
  `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`, with the same weight.

All results PRELIMINARY until a cross-family review; no promotion without
separate user decision. Even a discriminating signature says what would
distinguish the hypotheses in these rows; it is not evidence that we live
in either.

## 8. Explored before freezing (declared)

Reading of the parent contract and report (Secs. 1, 3.3, 3.5, 3.6, 5) and of
`theory/THREE_VELOCITIES.md`. The 1D Dirac-walk inequality
nu sin k / sin omega ≤ 1 was noted by hand in conversation. The d ≥ 2
consequence r_in < V_causal^max for polytopes is elementary. No group
velocity off the node, no witness and no signature class has been computed.
