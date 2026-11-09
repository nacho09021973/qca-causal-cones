# Coexistence question: quantifier order and line-abandonment options

2026-11-09. Draft by Claude (Opus 5.5) at user request, following committee
brief `reports/comite/comite_decision_002_rumbo-tras-cierre-aproximado-thirring.md`
(§7, R2). Options drafted for a user decision; **the decision taken on
2026-11-09 is recorded in the last section** and in `state/CURRENT_STATE.md`.
Nothing here is chartered or computed.

Question being made falsifiable (`README.md`, `PROJECT_INSTRUCTIONS.md` §1):
one finite-range QCA, one fixed rule, both universal quantum computation and a
relativistic low-energy regime of the same rule.

Known facts used below (with source; anything else is marked):

- Only gate resource so far: T=1, D=diag(1,z,z,1) on the M=1 code at
  mu=3/5, z=i (`reports/2026-11-08--thirring-growing-time.md`). Whether D
  survives for other mu is `[UNVERIFIED]`.
- At mu=3/5 the free gap omega(0)=arcsin(3/5) is O(1) in lattice units
  (committee arithmetic from cos omega = nu cos q, `[UNVERIFIED]` by script).
- The vacuum one-particle sector of a density-collision QCA is exactly free
  (`reports/2026-11-06--interaction-vacuum-sector.md`): a "relativistic regime"
  read in a sector the interaction never touches is cheap.

## Q1. Parameters

- **Q1-A. Same fixed point.** Code and relativistic regime at the same
  (mu, chi). Strictest. At mu=3/5 there may be no relativistic window at all.
- **Q1-B. Declared family.** A family (mu, chi) in F, frozen before any
  calculation; the regime is read as a limit inside F (e.g. mu -> 0), and the
  gate resource must be shown at the parameter points where it is used,
  along the same family. No point of F chosen after seeing results.
- **Q1-C. Separate choices.** Code at one point, regime at another. Answers
  a different question (two rules), so it is excluded by "the same rule".

Recommendation: **Q1-B**, with the family and the limit written into the
contract before computing.

## Q2. Sector

- **Q2-A. Same carriers.** The low-energy regime must be that of the
  excitations that carry the code (same particle-number sector, interaction
  active there).
- **Q2-B. Any sector.** Any sector of the rule may supply the regime.

Recommendation: **Q2-A**. Q2-B can be satisfied trivially by a free sector.

## Q3. Output frames and times

- **Q3-A.** Output frame and times defined before the calculation,
  independent of the logical input, and not using the full evolution to
  guarantee recovery by construction. A frame built from the free part of
  the rule, such as F^T B, is admitted; a comoving frame U^T B is excluded,
  because it makes recovery tautological.
- **Q3-B.** Frames may be adapted per code after inspection.

Recommendation: **Q3-A**.

## Q4. Resources

- **Q4-A.** The rule only (current contracts): ideal preparation and readout
  in declared modes, no ancillas, measurement or feed-forward.
- **Q4-B.** A resource ladder frozen in advance (e.g. A: rule only;
  B: + independent ancillas; C: + intermediate measurement without
  feed-forward), each rung its own contract. Adaptive feed-forward counts as
  external control and stays excluded.

Recommendation: **Q4-A** for the next contract; Q4-B only by a separate
decision.

## Q5. What abandons the Thirring coexistence line

Not a single closed code (that is never a no-go). Options:

- **Q5-A. Regime first.** If a contract shows that, in the declared family,
  the two-particle sector of the interacting rule has no relativistic
  low-energy regime (no common c_{omega^2} or c_H for the relevant branches,
  or an IR-to-doubler coupling that is not suppressed in the limit), the
  Thirring model is abandoned as working model for coexistence. Codes are
  not explored further in that family.
- **Q5-B. Budget.** Stop after a fixed number of contracts or sessions
  without a positive gate or regime result, recorded as OPEN, not as a no-go.
- **Q5-C. Both.** Q5-A as the scientific criterion, Q5-B as a hard stop.

Recommendation: **Q5-C**, with the budget chosen by the user.

Every contract must also carry an OPEN verdict with the same weight as the
positive and negative ones, and state what was explored before freezing.

## Q6. Evidence level of the three results promoted on 2026-11-09

"Promoted" is not a level of `PROJECT_INSTRUCTIONS.md` §4.

- **Q6-A. ESTABLISHED, in frozen scope.** §4: "proved in-repo"; each has a
  written proof, exact checks of its algebraic steps and one cross-family
  review. Analytic steps are not machine-checked.
- **Q6-B. SUPPORTED.** Keeps them below ESTABLISHED until a second review
  or a formal check.

Recommendation: **Q6-A**, with "frozen scope, one cross-family review" kept
next to the label.

## Decision recorded 2026-11-09

User decision (text supplied by the user, adopting the recommendations with
three corrections and a budget). Binding on every coexistence contract:

- **Q1-B, corrected.** Coexistence must hold at the same points of the
  declared family. Each contract states which property is preserved when
  the limit is taken. Computation at one point and a relativistic regime at
  another does not suffice.
- **Q2-A** kept: the regime is that of the code's carriers.
- **Q3-A, corrected** as written above: frames and times defined in
  advance, independent of the logical input, without using the full
  evolution to guarantee recovery by construction (F^T B is admitted).
- **Q4-A** kept: rule only for the next contract.
- **Q5, corrected.** Two distinct closures:
  - *Scientific discard*: a demonstrated negative result discards the
    declared family and sector only. It does not exclude the Thirring model
    as a whole.
  - *Operational stop*: budget of **two further contracts**, with a
    mandatory closure and a balance after the second. A partial positive
    result does not reset the count. If the objective is not reached, stop
    with status OPEN, unless an exclusion has been demonstrated within the
    declared scope.
- **Q6-A** kept: the three results promoted on 2026-11-09 carry the level
  ESTABLISHED in their frozen scope, one cross-family review each. The
  canonical state already records the promotions and their limits; this
  labelling is not a new review of the proofs.
