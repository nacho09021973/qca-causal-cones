# Fixed tetrahedral walk: one infrared operational protocol

2026-11-10. User: "estudiemos la señal bajo un protocolo infrarrojo".
Status OPEN; this user instruction authorizes the bounded execution below.

## Known, question and abandonment

Known: the preceding tetrahedral spectral preflight exhibits a simple
branch with directional speed 1/sqrt(5)>c_IR=1/3. This neither proves a
protocol nor transfers the CJWW signal asymptotic. The resource/encoder/
effect admissibility definition is the one in `ir-corona.tex` section 3.
Question: is the fixed protocol below IR-admissible, and what can be
established about its signal outside the local IR cone?
Stop a positive-signal proof if admissibility or a non-cancellation bound
cannot be justified. Report OPEN with the missing bound. A finite-N
floating-point nonzero value is not an asymptotic or exact nonzero proof.

## Fixed model, conventions and geometry

Same lattice L, internal dimension four and fixed U(k) as
`POLYHEDRAL_CORONA_TETRA_PREFLIGHT_GATE.md`; no coefficient, representation,
node or parameter change. Both nodal subspaces are present in the rule.
Fourier convention here: hat psi(k)=sum_{x in L} exp(-ik.x)psi(x);
inverse measure is vol(L)/(2pi)^3 dk. The symbol with exp(-ik.h/sqrt(3))
then implements shifts +h/sqrt(3). Primitive-cell volume is 4/(3sqrt(3)).
The momentum cell is defined by primitive phases in [-pi,pi)^3, for
primitive lattice vectors (-1,1,1),(1,-1,1),(1,1,-1), each /sqrt(3).

v=(-1,-1,-1)/sqrt(3); b_N=(3N/4)v. Radius R_N=N/32 for both regions:
A_N=L intersect ball(0,R_N), B_N=L intersect ball(b_N,R_N).
All x,y obey |y-x|>=11N/16>N/3. The ball of relative velocities has
centre (3/4)v and radius 1/16, inside the tetrahedron (nearest face
distance 1/12). Thus the experiment is outside the local IR cone and
within its convex microscopic envelope. This is not a strict-support proof.

## Resource, operations and observable

Lambda=N^-1, Lambda'=N^-1/2. Use the exact normalised resource
hat phi_N(k)=Z_N^-1/2 (1-N^2|k|^2)_+^2 chi for sufficiently large N,
Z_N=vol(L)*64/(3465 pi^2 N^3).
chi=|up> tensor eta_+, where (n.sigma)eta_+=eta_+,
n=(1,1,1)/sqrt(3), eta_+=(sqrt((1+1/sqrt(3))/2),
exp(i pi/4)sqrt((1-1/sqrt(3))/2)).

F_N(x)=(1-|x|^2/R_N^2)_+^2; h_N(y)=F_N(y-b_N).
M=sigma_y tensor I_2, encoder V_N=exp(i pi F_N M/2), effect E_N=h_N I_4.
No spectral projection in the measured signal:

    L_N=<U^N V_N phi_N,E_N U^N V_N phi_N>
         -<U^N phi_N,E_N U^N phi_N>,   delta_N=|L_N|.

Admissibility requires all three relative ratios in manuscript Definition
3.1 and nonzero denominators, including Delta_N!=0. It is not enough to
show an absolute leakage goes to zero. No exclusivity of spectral origin.

## Stages and outcomes

1. Analytic geometry, resource normalisation, operator leakage via lattice
   finite differences, and lower bounds on the denominators. Obtain
   vanishing relative leakage or name the gap. No diagnostic can close it.
2. Fixed finite-N diagnostic N=8,16,24,32 only, no fit or parameter search.
   Evolve the compact encoded difference by the four exact coefficient
   formulas on a nonperiodic grid large enough for all N steps. Obtain the
   unrestricted reference by quadrature over its exact compact momentum
   support. Use two fixed cubature orders 8 and 12. Evaluate the stable
   interference-plus-square expression for L_N. Check difference-state
   norm preservation, no wraparound and quadrature sensitivity; fail on
   nonfinite data or relative norm error >1e-10. Finite floating-point
   samples remain diagnostic even if they agree.
3. Seek an analytic non-cancellation argument for this fixed protocol.
   If unavailable in this session, retain `OPEN_AFTER_IR_PROTOCOL_ANALYSIS`
   with the precise missing estimate, not a claim of proven signal.

Allowed alternatives: `IR_ADMISSIBILITY_NOT_ESTABLISHED`,
`PROTOCOL_ZERO_SIGNAL_PROVED`, or `IR_SIGNAL_PROVED_IN_DECLARED_PROTOCOL`
only with an actual nonzero proof. No assumed N^-13/2 power or exponential
rate. No change of profiles, detector, input, geometry or M to rescue zeros.

One analytic pass and one diagnostic script with retained data/provenance.
No new polyhedron, numerical sweep, independent external review or
promotion. New code stays in scripts; reviewed verifiers stay byte-identical.
Commit the charter before execution. All new results remain PRELIMINARY
until independent review and a separate promotion decision.
