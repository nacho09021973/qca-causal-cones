# W6 resonant carriers: joint leading-signal contract (draft)

2026-11-13. Codex (OpenAI), base `374ff6a`, branch
`research/tetrahedral-support-rigidity-2026-11-09`.
User «hazlo», following the proposed new bounded contract for the joint
contribution of W6's resonant carriers. **DRAFT; NOT FROZEN; NOT EXECUTED.**
No external review sent. This successor does not reopen, amend or erase
the negative outcome of `IR_CARRIER_W6_EXACT_EXAMPLE_GATE.md`.

## 1. Known, question, abandonment

Known, with evidence ceilings:

- The prior report `reports/2026-11-13--w6-exact-carrier-preflight.md`
  records the exact author identity `S(p+q)=-i S(p)`,
  `q=(pi/2)u`, `u=3V`, of order four on the declared reciprocal torus.
  It gives inseparable scalar-shift carrier copies and a phase relation
  incompatible with H6_k(ii). Its 86-check certificate does not replace
  an independent review of the analytic proof. Status PRELIMINARY.
- The prior numerical inventory of two dominant W6 points is incomplete
  if that identity and the declared torus are correct. At least one
  four-point orbit is required; exactly four and completeness of that
  orbit have not been established. Other orbits must not be omitted.
- Carrier Stage A Secs. 8–10 uses rational independence to discard cross
  terms in a second moment. That sufficient method fails for the frozen
  W6 instance. Individual non-zero depth averages do not prove that the
  summed signal survives.
- Active-protocol infrared admissibility is promoted under its separate
  charter, with its recorded review ceiling. It supplies no rate lower
  bound and no non-cancellation theorem.

Question: for the **same fixed W6 instance**, does the complete resonant
sum give a non-zero physical leading signal for at least one active
encoder/non-zero detector pair, at amplitude exponent K_* and power
N^(-13/2), without the false independence assumption?

Abandon this leading-order route if the full leading physical coefficient
is identically zero on the actual phase orbit for every declared pair.
Record cancellation, not a no-go for any signal or for exponential rate
attainment at a different power. Stop OPEN on an unproved inventory,
uncontrolled remainder, failed necessary prerequisite or exhausted budget.
No tuning of the data and no additional asymptotic order under this gate.

## 2. Data frozen by reference for the prospective execution

Use exactly Secs. 2–3 of `IR_CARRIER_W6_EXACT_EXAMPLE_GATE.md` as frozen
at `b8ece32`: the same Laurent matrix, step-generated Bravais lattice,
P node, `chi=P e_1/sqrt(e_1^dagger P e_1)`, resource g, `V=n`,
`t_0=1/1000`, envelope-defined radius r, physical continuum balls,
Hermitian basis, detector projectors and local exponential encoders.
No substituted QR vector or diagnostic radius, alternative nodal sector,
enlarged ambient lattice, changed time step, measurement, ancilla or
subsequence-specific protocol. A witnessing pair is fixed independently
of N; subsequences may establish a limsup for that fixed pair.

The previous gate's arithmetic H6_k(ii) is not assumed. This is a new
joint-sum argument, not an assertion that W6 meets the old hypothesis.
Geometry H1, full spectral dominance/Hessians, rate smoothness, resource
boundary/tail conditions and operational error control must be proved
or explicitly left open. No inference of those facts from a PASS label.

## 3. Separate review of the prior obstruction

Prepare a sealed review brief attaching the old frozen contract, report
and permanent verifier, asking an independent family to check:
the global axial-envelope bound, the conditional H1/symmetry argument,
the true lattice, four-point scalar orbit and phase-branch correction.
One review round, no earlier external verdict used as evidence.

This is a distinct dependency audit, not a request to certify the new
joint-sum theorem before it exists. Transmission requires explicit user
authorization for that assignment. A completed review is not promotion.
If a mandatory mathematical error is found, stop reliance on the affected
identity and record the repair before any new calculation using it.
If execution is separately authorized before the external review is
complete, prior identities must be rederived as author inputs and all
new results stay explicitly provisional; no independence claim is made.

## 4. Prospective execution stages and targets

### A. Complete orbit inventory and exact joint kernel (90 minutes)

First rederive the scalar shift and characterize the equality conditions
for global spectral dominance at the relevant tilt. List every orbit
and its multiplicity on `T_L`; distinguish point copies from additional
eigenvalue branches at a single point. Prove any simplicity, spectral
gap, Hessian and common-gradient condition used in saddle asymptotics.
An axial envelope formula alone is not a full inventory or Hessian proof.

For each orbit, sum all its kernel contributions before taking a modulus,
discarding a cross term or interpreting a numerical depth average. Track
the exact eigenvalue phase, the resource-node phase, the layer character,
both depth offsets and any residue class of N. Recover the real-space
support rule `u.(y-x) == -N (mod 4)` by a second formulation. Check whether
the summed orbit acts as a congruence selector rather than assuming it
cancels or survives. Residue classes partition the existing evolution;
they do not change its one-step rule.

Keep the other ledger obligations visible. If a prerequisite fails,
stop rather than deriving a conditional-looking numeric answer.

### B. Joint non-cancellation on the actual phase orbit (90 minutes)

Aim for a uniform expansion for every fixed declared pair a,

    L_a(N) = exp(-K_* N) N^(-13/2)
                 [C_a(x_N) + epsilon_a(N)],
    delta_a(N)=|L_a(N)|,    sup_a |epsilon_a(N)| -> 0,

where C_a is the **real physical signed coefficient** after summing all
leading carriers. A finite family suffices for uniformity in a.
State an error rate only if proved. This formula is a target, not an
established input of this contract.

Define x_N with all actual phases and offsets needed to represent that
coefficient, including any common phase relative to the resource and
the N residue class. Determine its compact orbit closure X and the
limiting measure there. Do not integrate over a larger independent
torus merely because that makes cross terms disappear. Treat rational,
irrational and finite-component cases according to exact relations;
no assumed irrationality or floating-point non-resonance.

A proposed sufficient target is a proved bound

    integral_X C_a(x)^2 dmu_X(x) > 0

for at least one fixed active/non-zero physical basis pair, together
with continuity, orbit equidistribution and a uniform remainder that
turn it into a positive scaled limsup. All cross terms are retained.
An explicit non-zero witness on X with the necessary continuity and
recurrence control is an alternative route; a grid sample is not.

If a complex bracket h is used instead, proving `integral |h|^2>0`
does not alone prove a measured signal. Prove a common rotation using
the frozen finite matrix spans and pass to a fixed physical basis pair,
or evaluate its real measured component directly. The exponential
encoder signal is not bilinear. Any bilinearity argument applies only
to a justified leading functional; no signed combination of projectors
is silently implemented as a detector.

### C. Operational close (60 minutes, only if A–B close)

Complete the exact geometry/spectral/resource ledger, the regional upper
rate bound and the relation of the non-zero leading coefficient to the
same operational signal without spectral projections. Apply the active
admissibility lemma to the actual witnessing pair. Show explicitly how
the scaled positive limsup and upper bound yield

    limsup (1/N) log delta_a(N) = -K_*.

If A–B give only a conditional joint-sum lemma, record that limited result
and the missing rows; do not call it a certified W6 rate example.

## 5. Budget, provenance and verdicts

Maximum three analytic sessions, 240 minutes total. Stages are sequential;
no new session to rescue a stopped or inconclusive target. Before each
calculation state known inputs, question and abandonment criterion.
All retained computational results require permanent traced scripts
in `scripts/`, committed before execution, exact command entries in
`.claude/settings.json` and scope/limits in `scripts/README.md`.
Fail closed; no floats in certified quantities, no fitted tolerances,
no ephemeral scientific scripts, no modification of reviewed verifiers.
An analytic bound with explicit tail/remainder control may certify an
infinite sum; a finite truncation alone may not.

Report each target separately using `PROVED_UNDER_FROZEN_CONTRACT`,
`COUNTEREXAMPLE_VERIFIED` (explicitly naming the failed condition or
identically cancelled leading term), or
`OPEN_AFTER_W6_RESONANT_ANALYSIS`. Preserve negative outcomes. Any
conditional lemma is labelled with its exact unmet hypotheses.

Full positive closure requires inventory, joint coefficient,
non-cancellation, operational remainder and the full fixed-data ledger.
No novelty claim, interacting-QCA claim, R2 work, fallback to W2/W3,
time blocking, new walk search or automatic higher-order expansion.
External review of a new candidate and promotion are separate user
decisions. The old failed H6 instance remains recorded unchanged.

## 6. Drafting checkpoint

The local literature index and the existing carrier/preflight records
were inspected. No paper claim is inferred from the index and no new
scientific calculation was performed in preparing this draft. The next
authorization must distinguish freezing/execution, the prior-obstruction
review assignment and any later review of the new result.
