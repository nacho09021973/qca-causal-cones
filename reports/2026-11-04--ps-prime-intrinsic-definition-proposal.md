# PS′: documentary proposal on presentation dependence

Date: 2026-11-04. Base: `13432ab9f85f2b5d46c5e55b8ef2f2c749393628`.
Author: Codex (OpenAI). Status: **PROPOSAL / PRELIMINARY**.
Authorization: the user's instruction to write a bounded documentary
proposal about PS′ and its stopping criterion.

Revision note: translated into English to follow `CLAUDE.md`, Layout,
and revised after the read-through supplied in the conversation. That
read-through reported no factual or citation errors and requested three
changes: disclose the retrospective stopping criterion, distinguish a
possible intrinsic extension from the contract's presentation-based
wording, and follow the directory's language convention. It was not a
sealed blind review. This revised text has not been independently reviewed.
Second revision (2026-11-04): Claude's review
(`debates/2026-11-04--ps-prime-proposal-review-claude/revision.md`, PASS,
not blind) asked for two non-blocking clarifications, A1 and A2; the user
approved applying them, and Claude inserted them (Sec. 1, Sec. 3).

This is not an approved amendment. It does not change the frozen contract,
close G1, issue the PS′ verdict excluded by phase 0, or update
`state/CURRENT_STATE.md` Sec. 15. No verifier is run or modified. The
logical consequences below are the author's reasoning, not promoted results.

## 0. Known facts, question and retrospective stopping rationale

**Known, with sources.** `theory/SUBSTRATE_SATURATION_PHASE0_GATE.md`,
Sec. 1, states PS′ using the generators of a product presentation whose
partial shifts move by `±a_i`. It does not select a presentation or
quantify over factorizations. In particular, it does not assert that this
count is intrinsic to the complete walk. Sec. 2.1 gives saturation an
existential quantifier over walks on a substrate.
`reports/2026-11-04--substrate-saturation-phase0-G1-trace.md`, Secs. 2–3,
records presentation dependence in L6e and leaves G1-a, G1-b and G1-c open.
`state/CURRENT_STATE.md`, Sec. 15, retains
`PRELIMINARY / OPEN_AFTER_ROW_SURVEY`, with no confirmatory value.

**Concrete question.** What additional definition would be needed to
extend the presentation-based generator count into an intrinsic criterion
for the complete walk? This is a possible extension of the frozen wording,
not a correction of an intrinsic-invariance claim made by the contract.

**Retrospective stopping rationale, not preregistration.** This document
was written knowing the L6e example. The following condition describes
why the proposed unqualified intrinsic use should stop; it is not a
prediction, a test passed, or independent evidence: if two presentations
of the same walk give different truth values to “exactly `d` independent
reduced directions”, that predicate cannot be assigned to the walk
without an additional rule. Reconsideration would require an explicit
rule justified without using saturation to select presentations, with
its domain and invariance obligations stated.

This bounded documentary task stops if it supplies no such justified rule;
it does not initiate a search for exceptions or factorizations to preserve
the proposed interpretation. This rationale does not abandon PH or every
possible intrinsic conjecture. “No justified rule is available here” does
not mean “no such rule can exist”.

## 1. Local evidence and two checks of the same identity

The original drafting consulted `biblioteca/INDICE.md` by author, topic
and identifier. It did not locate JDW `1803.01304` there; this is not a
claim of bibliographic absence. The original is registered in
`sources/README.md` and available as `sources/1803.01304v1.pdf`. Pages 1–2
were read: the coin parametrization in Eq. (1), and the isosceles shifts
and three-step product in Eq. (6). The zonotope theorems cited indirectly
by the contract have not been read and are not used here.

In Eq. (6), the second-step coin has angle zero; Eq. (1) then gives the
identity. The second and third shifts act diagonally in the same L/R
basis, so they can be combined without changing the complete operator or
the duration assigned to one update. This rewrites the same product; it
does not change the time normalization.

The second check reads the repository constructor in
`scripts/verify_c_across_lattices_gate.py`: `u2` (lines 92–97),
`jdw_shift` (303–305), `ISO` and `ISO_GENS` (348–349), and `row_L6e`
(352–364). It implements that same identity intermediate coin and that
same L/R basis for the shifts. This checks agreement between the primary
source and the code; it is neither independent review nor a new execution
of the support or speed certificate.

The G1 trace, Sec. 2, L6e entry, already records both presentations:

| Presentation of the same update | Reduced directions | Factor zonotope versus `conv F` |
| --- | --- | --- |
| Three printed steps | Three in dimension two | Different: two candidate vertices are absent |
| Second and third shifts combined | Two orthogonal directions | Equal, as recorded in the trace |

The recorded Cartesian shift vectors are `(1,0)`, `(1/2,1/2)` and
`(-1/2,1/2)`; the last two combine to `(0,1)`. The combined shift moves
L by `-(0,1)` and R by `+(0,1)`, so it is symmetric, `±a` with
`a = (0,1)`; this is what places the two-factor presentation in the
product class of contract Sec. 1 (clarification A1). Operator equality follows
from the identity coin and the shifts conditioned in the same basis,
not from inferring factors from the body's edges. Support and saturation
values are taken from the existing record, not recertified here. In
particular, L6e's normalized pair is recorded in `EXPECTED_MASSLESS` of
the same script, lines 74–80.

**Documentary consequence:** an arbitrary presentation's count cannot
simply be assigned to the complete walk. L6e exhibits this distinction
without needing its speed value. This identifies an obstacle to the
proposed intrinsic extension, not a scientific phase-0 verdict on PS′.

## 2. Two quantifiers requiring separate decisions

Write `P` for a presentation, `r(P)` for its number of reduced directions,
and `W` for the complete walk.

1. **Presentations of one walk.** “For every presentation `P` of `W`”,
   “there exists a presentation `P` of `W`”, and “for a selected
   presentation `P_0(W)`” are different conditions. The example separates
   the count of a presentation from the complete operator. Choosing one
   of these quantifiers would add a definition; none is adopted here.
2. **Walks on one substrate.** Existence of a saturating walk in a
   substrate's declared class is different from saying that each walk
   with a particular factorization saturates. Contract Sec. 2.1 uses the
   first reading for saturation. A future formulation must say whether
   the generator test applies to the saturating witness, to every walk
   on the substrate, or to the existence of some walk. It must not
   silently replace the substrate-level statement with a per-walk one.

## 3. Options and their outstanding obligations

| Option | What it defines | Outstanding obligation / reason not to adopt it here |
| --- | --- | --- |
| Printed presentation | A property of the published construction | Traceable but presentation-dependent, not intrinsic to `W` |
| Combine compatible factors until no further combination is possible | A reduction of a presentation | Complete rules and invariance under different reduction sequences are missing; L6e supplies only one concrete reduction |
| Some presentation has `d` independent reduced directions | A logical property of `W`, once the permitted presentations are fixed | The permitted set must be defined; an existence witness does not decide nonexistence in other rows |
| Minimum direction count over permitted presentations | A candidate intrinsic property, if the domain is defined and nonempty | No minimum has been established for the rows; this is a new definition, not an editorial repair |
| Admit only presentations whose zonotope equals `conv F` | An explicit geometric restriction | The vertex condition does not show that such a presentation exists for each walk; membership and factorization remain unresolved |

A rule cannot be justified by making the saturating rows have `d`
directions and the other rows not. Its selection must be stated and
assessed without consulting `c_0 = r_in`.

The last option uses the corrected F2 but has a precise limit. Conditional
on `Z(P) = conv F`, and on the generators spanning `R^d` (a
full-dimensional body, which holds in every row of the record;
clarification A2), the geometric statement in contract Sec. 1 makes
“exactly `d` independent reduced directions” equivalent to the common body
being a parallelepiped. The truth value of that predicate is then fixed
by the body, even without a canonical factorization. This is a conditional
consequence of the stated geometric criterion, not proof that suitable
presentations exist or a theorem about saturation. Under this restriction,
a PS′ reformulation would use a body predicate involving parallelepipeds;
PH uses hypercubes. Those predicates remain distinct. The walk/substrate
quantifiers in Sec. 2 would still need to be fixed before stating a new
biconditional.

The domain also matters for G1-a. Centering asymmetric shifts may introduce
half-vectors that are not translations of the original group at an
intermediate step. Zero total center displacement over the complete update
does not by itself admit those factors as operators on the original
space. A rule must specify the permitted group and space for intermediate
steps. No such extension is adopted here.

## 4. Bounded recommendation and end of this task

**Recommendation, pending the user's decision:** do not extend the
presentation-based generator count to an intrinsic saturation criterion
without an explicit presentation rule. This concerns a proposed extension;
it does not withdraw or correct an intrinsic claim made by the frozen
contract. Keeping counts attached to their specified presentations remains
legitimate documentary work.

The discrepancy used in the retrospective rationale of Sec. 0 is already
in the L6e record. This document provides no additional rule justified for
the whole domain and stops here. That is a description of the current
obstruction, not a preregistered test outcome or a proof that no intrinsic
rule can exist. No amendment is proposed to fit L6e. The existential and
vertex-restricted readings remain options, not adopted rules or tested
hypotheses. Adoption of this recommendation as a project decision belongs
to the user; no abandonment is recorded as already approved.

- **G1-c:** the presentation ambiguity is explained but not closed under
  the frozen contract.
- **G1-a:** the domain decision concerning asymmetric shifts and their
  intermediate operators remains open.
- **G1-b:** no factorization is documented; none is sought here.
- **PH:** formulation and status unchanged; this document does not prove,
  refute or support it.
- **Phase 0:** remains `PRELIMINARY / OPEN_AFTER_ROW_SURVEY`, with no
  confirmatory value and no promotion.

Work performed: documentary reading and revision of this proposal. No
scripts are created, no automated calculations are run, no material is
sent to third parties, and no subsequent phase is authorized.
