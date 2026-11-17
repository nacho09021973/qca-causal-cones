# Isolated spectator gate

2026-11-17. Author: Codex (OpenAI). OPEN; frozen by the preregistration commit.
User authorization: «adelante con el siguiente trabajo», following the bounded
proposal to prove physical decoupling, check the fixed geometry and assemble
truncation and two-particle errors. No external review or promotion authorized.

Known: CURRENT_STATE records the promoted co-moving two-packet result;
reports/2026-11-09--thirring-low-energy-packet.md Sec. 4(iii) gives tails;
reports/2026-11-14--thirring-comoving-packet.md Sec. 3 gives the pair bridge.
Primary rule: sources/1711.03920v1.pdf pp. 1-2, range-one free walk and
on-site number-preserving interaction. Keep the repository coupling convention.
Question: does a causally isolated spectator preserve this pair gate uniformly?
Abandon this construction on a demonstrated failure of its fixed code or
geometry, or nonvanishing limiting error; do not change parameters to repair it.
If an indispensable estimate cannot be established, stop OPEN_MISSING_BOUND.

Fixed construction: infinite line, U=FJ, chi=pi/2, 0<mu<1/10,
nu=sqrt(1-mu^2), delta=mu^(3/2), L=ceil(mu^(-2)), T=20L.
Use exactly the normalized h, positive-band spinors, Gamma and flavour
projectors of THIRRING_FLAVOUR_PACKET_GATE.md. Momentum centres K=(3,1,-2),
position centres (L,-L,-50L). Logical order (fast,slow,spectator).
B|abc>=(sqrt(2)Pi_a phi_f) wedge (sqrt(2)Pi_b phi_s) wedge
(sqrt(2)Pi_c phi_e). Prove isometry. Output C=(wedge^3 W)^T B.
K=C* U^T B; E=(I-CC*)U^T B. Target V(r_co) tensor I, no adjustable phases.
Spatial ordering, if discussed, must declare both frames before comparison.

Auxiliary spatial cutoffs have radius floor(L/4); do not normalize them.
Prove exact separated-support decoupling, then transfer to original packets.
Prove an operator-norm bound on U^T B-C(V tensor I), hence compression and
leakage. Use analytic arguments, no numerical experiments or new scripts.
One bounded proof attempt; stop on closure or an unresolved essential bound.
Verdicts: REDUCES_TO_EXISTING_RESULTS (proved corollary),
PASS_ISOLATED_SPECTATOR (requires additional proved input),
FAIL_ISOLATED_SPECTATOR (counterexample), OPEN_MISSING_BOUND.
All author results PRELIMINARY pending independent review.
No general F, successive collisions, universality, interacting QFT or novelty
claim. NOVELTY=OPEN; COEXISTENCE=OPEN.
