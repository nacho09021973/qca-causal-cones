# Thirring low-energy packet gate

2026-11-09. Author: Codex (OpenAI). User authorization: «hazlo», responding
 to the proposal to use the final contract for a gate on low-energy packets.
Contract 2 of 2. Initial status OPEN. Freeze this document before execution.

## Known, question, abandonment

The canonical state records contract 1 as OPEN_AFTER_BOUNDED_EXACT_ATTEMPT;
its repaired proof has not been re-reviewed. The microscopic T=1 gate is
not a gate on low-energy packets. No relativistic interacting regime or
universality is established by that record.
Primary definitions read this session: sources/1804.08508v1.pdf pp.3-4,
Eqs.(1)-(6), W(q), positive-band eigenvector, U=FJ and physical antisymmetry.
Question: does the following fixed packet code implement a nonvanishing
entangling unitary with vanishing error under autonomous U?
Abandon this construction if a positive asymptotic error is proved or its
only limiting logical action is nonentangling. Neither excludes Thirring.

## Frozen construction

Infinite physical lattice, two fermions, chi=pi/2, nu=sqrt(1-mu^2),
0<mu<1/10, limit mu down to zero. No ancillary particles, intermediate
measurements, postselection, external F or J control, or parameter changes
during evolution. Ideal preparation and final readout in the declared modes.

Use the Fourier convention |q>=(2pi)^(-1/2) sum_x exp(-iqx)|x> and the
normalized v_q^+ of Eq.(3). Let h(t)=sqrt(15)/4 (1-t^2) for |t|<=1 and
zero otherwise (normalization must be checked during execution).
Set delta=mu^(3/2), L=ceil(mu^(-2)), T=4L.
For a=0,1 set k_a=1+a. The two A modes have momentum centers +mu k_a,
the two B modes -mu k_a, each with scalar envelope
 delta^(-1/2) h((q-q_center)/delta).
Translate the A modes to x=+L and B modes to x=-L by multiplying their
Fourier amplitudes by exp(i q L) and exp(-i q L), respectively.
With this Fourier convention positive-band positive q moves toward negative
x. Verify this sign before using any collision argument; a mismatch is a
construction failure, not permission to swap definitions after results.

The four logical columns B_mu|ab> are A_a wedge B_b, with A first in the
creation order. Disjoint momentum supports should give an exact isometry;
this is an admission check, not an assumption to repair after calculation.
Output frame is B_out=F^T B_mu, specified before execution; it is a
comparison/readout frame, not a physically applied inverse evolution.
No other packet, momentum center, time schedule or frame is admissible.

## Observables and success

K_mu=B_out^* U^T B_mu; leakage operator
E_mu=(I-B_out B_out^*) U^T B_mu.
All norms below are operator norms, uniform over logical inputs.
Success requires a fixed unitary V on C^2 tensor C^2 and phases alpha_mu
such that ||K_mu-exp(i alpha_mu)V|| -> 0 and ||E_mu|| -> 0, with V mapping
at least one product vector to an entangled vector. Give an explicit
witness and a strictly positive limiting entanglement measure; a nonzero
phase alone is insufficient. Local changes of basis cannot be chosen
post hoc to remove error.

Low-energy admission: show the incoming modes are in the positive band
at q=O(mu), and derive the free scaling omega(mu K)/mu on their support.
This does not settle the interacting relativistic property (R).
For a physical doubler observable define D_mu as the one-particle projector
onto negative band and periodic distance(q,pi)<4mu. On the antisymmetric
two-particle space define Q_D=I-(I-D_mu) tensor (I-D_mu).
Measure outgoing content ||Q_D U^T B_mu||^2, verifying Q_D B_mu=0 exactly.
Thus any final doubler content is generated from a doubler-free input;
no generalized-eigenvector coefficient is interpreted as packet probability.
Vanishing total leakage already controls this channel if Q_D B_out=0.
This is a new frozen observable, not a retroactive resolution of old O4.

## Method, verdicts, budget

Exact analytic packet/scattering analysis first. Prove the bridge from any
stationary scattering formula to these normalized finite-time physical
packets, including antisymmetry, phases, tails and uniform error estimates.
A plane-wave phase without that bridge cannot yield success or exclusion.
No finite scan or numerical fit decides an asymptotic claim.
Any computation needs a permanent verifier committed before execution,
recorded failures, and exact command entries in .claude/settings.json.
Do not modify a reviewed verifier. Written analytic steps must be identified
separately from machine checks.

Verdicts: LOW_ENERGY_PACKET_ENTANGLER_IN_DECLARED_CODE (all success
conditions proved); NO_ENTANGLER_IN_DECLARED_PACKET_CODE (a necessary
condition disproved); OPEN_AFTER_BOUNDED_EXACT_ATTEMPT (otherwise).
All are author PRELIMINARY pending independent review. Even success is
neither composability nor universality nor a full relativistic QFT limit.

Execution bound: one working session, one construction, no parameter or
packet search. Stop when a verdict is proved or when the bounded analysis
cannot close a required estimate. Record the exact open obligation.
Mandatory balance after closure: contract 1 remains OPEN; no automatic third
contract, no budget reset for partial positives. Overall coexistence stays
OPEN unless actually proved. External review requires separate permission;
no promotion or merge is authorized by this charter.

## Before freezing

Read canonical status, previous contract and repaired report, and the primary
pages named above. No new packet evolution, scattering evaluation or
numerical experiment has been performed. Packet choices above are a design
proposal frozen for this attempt, not an optimized or validated construction.
