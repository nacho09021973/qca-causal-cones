# General infrared rate on Bravais lattices: draft charter

2026-11-12. Drafted by Claude (claude-opus-5-5) after the user agreed to
generalise to other classes, Bravais lattices first («ok»). **Status:
DRAFT, not frozen; nothing authorized to be computed until the user
freezes it.**

## 1. Known, question, abandonment

Known.

- B1. General rate (`GENERAL_IR_RATE_GATE.md` with Amendments 1–4):
  Stages 1–2 PASS in one sealed Grok review (repairs applied, not
  re-reviewed), for walks on `Z^d`, `d in {2, 3}`.
- B2. Carrier dichotomy, Stage A (`IR_CARRIER_DICHOTOMY_GATE.md` with
  Amendment 1): `PROVED_UNDER_FROZEN_CONTRACT` for H6_k(i) with either H9
  and for H6_k(ii) with H9(ii), `OPEN` for H6_k(ii) with H9(i), after one
  Grok review with REPAIR_REQUIRED and repairs not re-reviewed.
- B3. Where the proofs use `Z^d` (read in the two derivations): the planes
  `{u.x = k}` as translates of `Lambda_0 = Z^d cap u^perp`, its covolume
  `|u|`, the plane spacing `1/|u|`, the identification `Z^d/Lambda_0 = Z`
  through `x -> u.x`, the Brillouin zone `T^d` with measure `d^d p/(2pi)^d`,
  the resource normalisation, and the site counts `|A_N|, |B_N| <= C N^d`.
- B4. Diagnostics: the two hexagonal walks satisfy every hypothesis but
  live on the triangular lattice; the three R1 walks live on BCC-type
  lattices (`reports/2026-11-12--general-ir-rate-round2.md`,
  `reports/2026-11-12--ir-carrier-stage-a.md`).

**Question.** Do the general-rate theorem (B1) and the proved part of
Stage A (B2) hold, with the same hypotheses, for walks on an arbitrary
Bravais lattice `L` of `R^d`, `d in {2, 3}`, with Euclidean balls as
regions, once `u` is taken as the primitive vector of the dual lattice
`L*` along `xi_*`?

Expected replacements: `u.x in Z` for `x in L` and `u.L = Z`;
`Lambda_0 = L cap u^perp` with covolume `covol(L) |u|`; spacing `1/|u|`;
characters trivial on `Lambda_0` of the form `omega^(u.x)`; Brillouin zone
of `L` with measure `covol(L) d^d p/(2pi)^d`; factors of `covol(L)` in the
resource normalisation, the free tail and the layer constants `k_A`, `k_B`.

**Result that ends the line.**

- (a) A step of B1 or B2 that uses `Z^d` beyond the items of B3 and fails
  for a Bravais lattice: recorded with the failing step; the line stops
  there.
- (b) Everything transfers by the replacements above with no new step:
  recorded as a corollary (expected outcome).
- (c) Budget exhausted: `OPEN_AFTER_<analysis>`.

## 2. Class

As in B1 (with Amendment 4) and B2, with `Z^d` replaced by a Bravais
lattice `L` (a discrete subgroup of `R^d` of rank `d`), steps in `L`,
Euclidean balls `N A`, `N B` intersected with `L`. Same protocol family,
same hypotheses, with H3 read as «`xi_*` parallel to a vector of `L*`».
Nothing else changes; the open cell of B2 stays open.

## 3. Stages

- **Stage 1 (written adaptation).** Go through Stages 1–2 of B1 and the
  proved part of B2 line by line, list every use of B3, apply the
  replacements, and recompute the constants; check them against the
  `Z^3` case (`covol = 1`, `u = (1,1,1)`).
- **Stage 2 (diagnostic consequence, no new computation).** Restate which
  rows of the existing diagnostics fall inside the enlarged class and what
  their hypothesis columns then say. No new run unless a row needs a
  quantity that was not computed; that would need a separate decision.

## 4. Verdicts, budget, stop rules

Verdicts as in B1. Stage 1: one session. No change of hypotheses; if a
replacement needs one, it is an amendment approved before use. A sealed
cross-family review of the adaptation is proposed after Stage 1, subject
to the user's instruction. No promotion.
