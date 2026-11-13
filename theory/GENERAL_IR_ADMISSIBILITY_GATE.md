# Infrared admissibility of the general-rate protocol family: charter

2026-11-13. Drafted by Codex (OpenAI), resuming Claude's work plan
`reports/2026-11-13--work-plan.md`, Sec. 2.2, at the user's instruction
«continua donde lo dejo claude». Base commit: `cf7eeb4` on
`research/tetrahedral-support-rigidity-2026-11-09`.

**Status: OPEN; FROZEN; Stage A authorized by the user («SI»,
2026-11-13), approving freezing and execution of Stage A.** Stage B,
external review and promotion are not authorized. No amendment to B1
is made here.

## 1. Known, question, abandonment

**Known (documentary baseline, not a new verification of the proofs).**

- The manuscript defines three leakage ratios in Definition 3.1
  (`papers/ir-corona/ir-corona.tex`, label `def:admissible`). Its
  Theorem `thm:admissible` states bounds of order `N^(-1/2)` for its
  specific three-dimensional, two-component protocol. The proof in
  `sec:admissible` uses a discrete multiplier estimate, lower resource
  mass on an interior and an exterior set, and explicit Pauli identities.
  This is an author derivation; its existence is checked here, not its
  validity in a larger class.
- B1 (`GENERAL_IR_RATE_GATE.md`, Amendments 1–6) declares a general
  Hermitian encoder basis and a finite spanning set of detector
  projectors. Bravais Stage 1, Sec. 6.3
  (`reports/2026-11-12--general-ir-rate-bravais-stage1.md`), explicitly
  records that admissibility of that family has not been proved in B1.
- Canonical status remains `state/CURRENT_STATE.md`: no promotion.
  Neither a diagnostic nor a non-zero denominator proves convergence
  of a leakage ratio.
- The local literature index was inspected for quantum walks, large
  deviations and lower bounds. No external theorem is used in this
  draft. Novelty is not a target and remains OPEN.

**Question.** For every fixed walk and protocol family in the amended
B1 class, do the encoder and detector satisfy Definition 3.1 as
`N -> infinity`, first on `Z^d`, then on a fixed Bravais lattice?
Which hypotheses, if any, beyond the existing class are needed?

**Result that ends the line.** A proof for the declared family closes
the gap; a certified failure of convergence for a protocol required by
the claim prevents that unrestricted claim. Failure of a denominator
is recorded separately from failure of convergence. If a new resource,
generator restriction or hypothesis is needed, stop before using it:
propose an amendment rather than repair the class silently. Budget
exhaustion closes execution as `OPEN_AFTER_ADMISSIBILITY_ANALYSIS`.

## 2. Fixed scope and definitions

Inherit B1 Sec. 2 with Amendments 1–6, and the Bravais charter's lattice
replacement. Dimension `d in {2,3}`, finite internal dimension `s >= 2`,
one fixed translation-invariant finite-range free walk. No interaction,
new walk construction, carrier analysis or diagnostic sweep.

Use the existing fixed continuum balls A and B, of positive radii,
intersected with the lattice after dilation by N. Make their inherited
quadratically vanishing profiles explicit before the proof:

    F_N(x) = (1 - |x/N - a|^2/r_A^2)_+^2,
    h_N(x) = (1 - |x/N - b|^2/r_B^2)_+^2.

Resource: the normalized Fourier function `g(Np) chi`, with
`g(q) = (1-|q|^2)_+^2` and a fixed unit vector chi in the declared nodal
space. Encoder `U_M = exp(i pi F_N M/2)` for each member M of the
inherited fixed Hermitian basis. Detector `E = h_N tensor M_B` for
each member of the inherited finite spanning set of projectors.
Do not replace that basis by Pauli matrices or impose `M^2 = I`.

Let Pi and Pi' be the momentum-ball projections of radii `N^(-1)` and
`N^(-1/2)`, respectively, with identity on the internal space; they
are not projections onto a selected eigenphase branch. On a Bravais
lattice use its reciprocal torus and normalized Haar measure, with
Euclidean balls in a neighbourhood of zero for sufficiently large N.

Targets, with the norms and denominators unchanged from Definition 3.1:

    eta_op(X) = ||(I-Pi') X Pi|| / ||X Pi||,
    X = U_M-I or E;
    Delta_M = |U_M phi_N><U_M phi_N| - |phi_N><phi_N|;
    eta_enc(M) = ||Delta_M-Pi' Delta_M Pi'||_1 / ||Delta_M||_1.

An identically zero operation or Delta has an undefined ratio, not a
ratio equal to zero. Record which protocols have defined ratios; do
not omit such a case from a claim quantified over the whole family.
No projection is inserted into the operational signal.

## 3. Targets and proposed route (not established results)

1. **Numerators.** Adapt manuscript Lemma `lem:IR1` to dimension d and
   matrix size s. Then adapt it to a lattice basis, accounting for the
   reciprocal-torus representative and the constants of the fixed
   lattice. Seek `O(N^(-1/2))`, without assuming this rate is optimal.
2. **Operator denominators.** Establish lower bounds uniform in N for
   each fixed non-zero encoder multiplier and detector. Constants may
   depend on the fixed geometry, lattice and finite matrix family.
   A pointwise non-zero value is not such a lower bound.
3. **State denominator.** Establish a positive lower bound for
   `||Delta_M||_1` for each required M, or exhibit the precise failure.
   Check the action on chi explicitly: the Pauli computation in the
   manuscript is not a proof for an arbitrary Hermitian basis.
4. **Combine and audit dependencies.** Determine which of H1–H10 and
   the nodal assumptions actually enter. Do not assume tilted spectral
   hypotheses control these leakage ratios. State the result with its
   actual quantifiers, including whether constants are uniform only in
   N. No uniformity over all lattices, walks or bases is requested.
5. **Second route/check.** Recover the manuscript's `Z^3`, Pauli case
   from the general statement and separately inspect a generator whose
   action on chi vanishes. These are analytic checks, not a walk search.

The desired conclusion is convergence of all defined required ratios;
`O(N^(-1/2))` is a secondary target. A slower proved convergence still
answers the admissibility question positively. A failure of one member
does not by itself refute existence of an admissible pair attaining
the B1 rate: that requires matching admissibility to B1's non-vanishing
argument, and must be stated as a separate remaining obligation.

## 4. Stages, budget and verdicts

- Stage A: one analytic session on `Z^d`, at most 90 minutes, including
  the denominator audit. Stop at a necessary class change.
- Stage B: one analytic session, at most 60 minutes, transferring a
  successful Stage A statement to a fixed Bravais lattice. No claim
  about the unresolved B2 carrier cell. Stage B requires separate
  authorization after the Stage A result is shown.

Per target: `PROVED_UNDER_FROZEN_CONTRACT`,
`COUNTEREXAMPLE_VERIFIED`, or `OPEN_AFTER_ADMISSIBILITY_ANALYSIS`.
Undefined ratios are identified explicitly in the report and limit
its quantifiers; they are not labelled counterexamples to convergence
of a defined ratio. All author results remain PRELIMINARY pending review.

Deliver execution in a dated report, citing the preregistration commit
and recording actual timing. Any computation contributing a retained
result requires a permanent script committed before execution. Do not
modify reviewed verifiers. No numerical search is requested.

After freezing, commit the charter before execution. External review
requires explicit transmission authorization; promotion requires a
separate user decision. A positive result would supply an admissibility
lemma for the declared free-walk protocols, not establish coexistence
in the interacting Thirring QCA or settle novelty.
