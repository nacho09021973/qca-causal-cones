# Two successive Thirring collisions — draft proposal

2026-11-17. Author: Codex (OpenAI).
DRAFT / NOT FROZEN / NOT EXECUTED. NOVELTY = OPEN.
User «adelante con el borrador» authorizes drafting only. This document
neither opens an executable gate nor authorizes a geometry search.

## Known, question and abandonment

The branch-local promotion in state/CURRENT_STATE.md at d375551 records
REDUCES_TO_EXISTING_RESULTS for one isolated spectator. The proof is
reports/2026-11-17--thirring-isolated-spectator.md, including its explicit
inherited pair hypothesis H_pair and the Opus provenance repair. Its
frozen geometry has K=(3,1,-2), centres (L,-L,-50L), T=20L.
It does not provide a second collision window.

The co-moving report of 2026-11-14 Sec. 3 covers the fixed K=(3,1)
pair. The flavour report of that date Secs. 4-5 covers K=(1,-2).
Neither report is an arbitrary-centre, arbitrary-time scattering theorem.
The massless two-node code and the fixed-mass two-contact code have
different hypotheses and cannot discharge the present obligations.
The literature index was consulted; no new prior-art claim is made.

Question: can two temporally separated physical collisions in one fixed
three-packet preparation be shown to implement an ordered product of the
available pair gates with operator-norm error and leakage tending to zero?

Abandon the proposed construction if its fixed geometry cannot supply the
required isolated windows, or if persistent leakage or a different limiting
map is proved. A missing theorem yields OPEN_MISSING_BOUND, not a no-go.
Do not change geometry or parameters after a failure. No claim of novelty.

## Admission before an executable contract

No complete geometry is selected or certified in this draft. Selecting one
is a separate, bounded analytic design task requiring authorization.
The executable contract must freeze all of the following before proof:

- Three momentum centres K_j, initial centres x_j(mu), the inherited h,
  delta=mu^(3/2), L=ceil(mu^(-2)), chi=pi/2 and the same U=FJ.
- Even integer window boundaries 0=t_0<t_1<t_2=T; if gaps are needed,
  their endpoints and free-propagation obligations must also be frozen.
- Exactly two prescribed crossings, their order and participating pairs;
  no additional crossing before T and no simultaneous three-body encounter.
- Spatial cutoff radii and the causal-separation inequalities in each window.
- Which existing pair theorem covers each window, with an explicit mapping
  of packets, frames, centres and times. Translation covariance alone does
  not supply a change of separation or duration. Free evolution to a later
  window gives dispersed modes, not automatically the original packet shape.

A possible starting inventory is K=(3,1,-2), inherited from the isolated
spectator, but it is not a frozen choice. In that inventory only the
(3,1) and (1,-2) pair bridges are currently identified above; the (3,-2)
pair is not admitted by analogy. Do not extrapolate the existing isolated
spectator geometry into a later encounter without checking the full schedule.
If no geometry can be justified with the available estimates in the bounded
design attempt, stop with the exact additional pair-bound obligation.

## Fixed logical formulation required in the successor

H is the one-particle space; W is the free one-particle walk and
W_n=wedge^n W. Reserve the symbol F for the open factorization premise
when discussing computational consequences; the microscopic rule remains U=FJ
in the repository's original notation.

Define normalized flavour modes u_ja=sqrt(2)Pi_a phi_j and an identity-ordered
isometry B_0|abc>=u_1a wedge u_2b wedge u_3c. Prove its isometry.
Define B_j=W_3^(t_j)B_0 before evaluating the physical evolution.
No reset, inverse free operation, fresh preparation, adaptive measurement,
ancilla or coupling change is permitted between windows.

The successor must explicitly define unitary logical gates G_1,G_2, including
rapidities, pair orientation, embedding and phases. Its window targets are

    ||U_3^(t_j-t_(j-1)) B_(j-1) - B_j G_j||_op <= e_j(mu),
    e_j(mu) -> 0, j=1,2.

These estimates must hold for every logical input, including entangled ones.
The second estimate concerns the freely evolved frame B_1; it must not be
inferred merely from the existence of a two-particle gate at time zero.
The final target is B_2 G_2 G_1. The physical state at t_1 is only close to
B_1 G_1; no projection or renormalization is physically performed there.
Compression and leakage use the orthogonal projector B_2 B_2*.
Position-ordered frames, if used, require explicit input/output permutations
and exterior signs for each window; no phase dependent on logical input may
be discarded. Identity order is the primary formulation.

## Proof obligations

1. Prove the fixed schedule and spectator separation for each window using
   the microscopic range, including any intervening free interval.
2. Establish spatial tails of the freely evolved modes at each cutoff time,
   uniformly up to the frozen final horizon; the initial-time estimate alone
   is insufficient. Keep unnormalized cutoffs as proof auxiliaries.
3. Apply the occupation-basis decoupling lemma window by window, retaining
   antisymmetry. Check every new application against its support hypotheses.
4. Supply each original-packet pair estimate in the actual window frame;
   do not apply a momentum-supported bridge to spatially truncated modes.
5. Transfer the cutoffs with uniform bounds and state the logical norm
   assembly explicitly. Derive the final error from the two window estimates
   and unitarity; account separately for any free gaps.
6. Bound final compression error and leakage. Independently check frame signs
   and verify that removing the second window recovers the admitted first
   collision. No numerical fit substitutes for these steps.

## Closure, budget and authorization

Design-stage outcomes: READY_FOR_FROZEN_CONTRACT or OPEN_MISSING_BOUND.
A frozen successor may use PASS_TWO_SUCCESSIVE_COLLISIONS,
FAIL_IN_DECLARED_GEOMETRY or OPEN_MISSING_BOUND, with all author results
PRELIMINARY until independent review. A positive result concerns only its
fixed sequence; general F, universality, interacting QFT and novelty stay OPEN.

Proposed design budget, not yet authorized: one analytic pass, at most
90 minutes, no parameter sweep, simulation or verifier. Close at a complete
reviewable geometry or the first essential unsupported estimate. The design
must be recorded as design work, not retrospectively preregistered proof.
Execution would require a fully specified contract committed before execution
and explicit user authorization. External review, promotion and publication
remain separate. This draft authorizes none of them.

## Selected design — 2026-11-17

User «fija la geometria que creas compatible» authorizes this analytic design
selection, not freezing or proof execution. This section supersedes the
unselected-geometry paragraphs above. All remaining proof obligations apply.

Keep exactly the isolated-spectator preparation: K=(3,1,-2), centres
(L,-L,-50L), h and delta unchanged. Use windows [0,20L] and [27L,28L],
with a proposed free gap [20L,27L]. These integer boundaries are even:
replace the latter two by 2 floor(27L/2) and 28L, respectively.
Cutoff radius at each window start is floor(L/4).
Final horizon is 28L. Identity order is (f,s,e).

The following is design-stage algebra of limiting free centres, not a
finite-mu or physical-scattering certificate. Put a=3/sqrt(10),
b=1/sqrt(2), c=2/sqrt(5). In units x/L and t/L the free centres are
1-a t, -1-b t, -50+c t. Their crossing times are exactly

    t_fs=2/(a-b), t_fe=51/(a+c), t_se=49/(b+c).

They obey 8<t_fs<9, 27<t_fe<28, 30<t_se<31.
These bounds follow, for example, from
948/1000<a<949/1000, 707/1000<b<708/1000,
894/1000<c<895/1000, verified by squaring positive rational endpoints.
Thus the proposed sequence is (f,s), then (f,e), with no third free-centre
crossing before the final horizon. It cannot be (f,s), then (s,e): the
(f,e) crossing intervenes. The second pair is a new obligation.

At scaled time 27 the slow centre is to the right of the fast by
-2+27(a-b)>4.48, and to the right of the spectator by
49-27(b+c)>5.71. Hence cutoffs of radius L/4 around all three free centres
leave the spectator slow packet separated from the active-pair hull for
one further unit of scaled time even after range-one expansion: the
limiting lower margin is > (4.48-0.5-2)L. Rounding the starting time
changes positions and the duration by O(1), harmless only after a proved
small-mu admission bound. The first window is the promoted isolated
spectator geometry exactly. This calculation does not certify the free gap.

The gates proposed in identity order are G_1=V_fs(a(3)/a(1)) and
G_2=V_fe(a(3)/a(-2)), with a(K)=sqrt(1+K^2)+K; the second expression is
a hypothesis, not an established pair theorem. Target G_2 G_1.

Admission remains OPEN_MISSING_BOUND until the following are supplied:
(1) the (3,-2) pair bridge in the freely evolved input frame at the second
window, with its shorter duration; (2) negligible interaction during the
gap, including pair tails after the first collision; (3) uniform finite-mu
localization and cone margins at the second cutoff. These require explicit
new analytic work and cannot be imported from the original two pair gates.
No claim of compatibility with all existing theorem hypotheses is made.
Stop design here; do not search alternative centres to avoid these obligations.
