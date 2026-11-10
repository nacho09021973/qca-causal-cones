# Polyhedral corona: fixed tetrahedral spectral preflight

2026-11-10. User: "empecemos por poliedros de alcance finito", following
the request to test the manuscript's operational claim on other geometries.
One fixed existing walk; no survey or constructor search. Status: OPEN.

## Known, question, abandonment

Known inputs: `reports/2026-11-06--s4-cyclic-realization.md` sections 4--5
and the read-only `scripts/verify_s4_cyclic_realization.py` define the
unitary and tetrahedral coefficients, local cones of speed 1/3, and axial
semitraces. This is source code/model input, not independent proof of a
new operational statement. The CJWW manuscript uses a different cube walk
whose group velocities all lie in the emergent unit ball.

Question: can that crucial global spectral bound be transferred to the
fixed tetrahedral walk? Specifically, is every differentiable eigenphase
gradient bounded in Euclidean norm by c_IR=1/3?

Abandon the direct transfer of the *entirely non-ballistic corona*
interpretation if a simple eigenphase has a directional derivative with
magnitude >1/3. This does not abandon the broader operational question:
it does not prove a signal or no signal for an IR-admissible protocol.

## Frozen model and scope

- d=3, internal dimension 4, one update lasts 1, lengths unchanged.
- Lattice: equal-parity integer triples divided by sqrt(3).
- G_i=sigma_i tensor sigma_i;
  W=I_2 tensor [I_2-i(sigma_x+sigma_y+sigma_z)/sqrt(3)]/sqrt(2).
- U(k)=W product_{i=x,y,z}[cos(k_i/sqrt(3))I_4
  -i sin(k_i/sqrt(3))G_i], fixed xyz order.
- F={(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)}/sqrt(3).
  C_micro=conv F, nodes at k=0 with phases ±pi/4; local speed 1/3.
- D2 and cyclic proper tetrahedral covariance as in the existing model;
  no changed representation, coefficient, node, normalization or parameter.
- All eigenphases of this same rule are included in the global-bound test.
  No irreducibility classification is attempted.

## Bounded execution

Start from the existing axial block formula at k=(sqrt(3)x,0,0),
f_eps(x)=[cos x-eps sin x/sqrt(3)]/sqrt(2), eps=±1.
Re-derive it from the 2x2 blocks and verify both determinants and traces.
Evaluate the local slope at x=0 and the derivative at x=pi/2, a target
chosen in designing this preflight, not a blind discovery prediction.
Check that all four eigenvalues at the target are simple. Cross-check the
derivative using 2 f=lambda+lambda^(-1), rather than only differentiating
arccos. A permanent exact SymPy verifier records these identities.

Outcomes:

- `GLOBAL_IR_BALL_BOUND_REFUTED_BY_AXIAL_WITNESS` if the exact simple-branch
  derivative exceeds 1/3; report only a lower bound on V_grp^max, not its maximum.
- `OPEN_AFTER_AXIAL_PREFLIGHT` otherwise. A finite axial test cannot prove
  the global bound and does not certify another polyhedron.

One analytic preflight and one verifier, no numerical scans, protocol
construction, operational asymptotics, novelty verdict or further models.
The result remains PRELIMINARY until independent review; sending it out
requires separate explicit permission. No automatic promotion.

Commit this charter before execution; record its commit in the report.
The user has authorized beginning the finite-range polyhedral comparison;
this document bounds its first step and does not authorize forty new gates.
