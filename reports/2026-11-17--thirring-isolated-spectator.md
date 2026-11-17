# Isolated spectator: analytic corollary

2026-11-17. Codex (OpenAI), PRELIMINARY author proof, not independently
reviewed. Preregistration a9d5ae1. No numerical computation or verifier run.
Verdict: REDUCES_TO_EXISTING_RESULTS, conditional on the promoted pair bridge
in its declared scope. This is not general multipartarticle factorization F.

## 1. Rule and support

sources/1711.03920v1.pdf pp. 1-2 defines the range-one walk W and on-site
occupation interaction. Use the repository phase convention for J; the
argument below is independent of its sign. F_n=wedge^n W and U_n=F_n J_n.
Exterior products use the normalized determinant convention, so orthonormal
modes have unit wedge norm. Creation by a vector v has operator norm ||v||.

If psi in wedge^2 H is supported with both coordinates in A and v is
supported in a disjoint B, then
J_3(psi wedge v)=(J_2 psi) wedge v.
Indeed, expand in occupation basis: all occupied sites of v lie outside A,
so its single occupation creates no double-occupation phase, and every
phase is precisely that of the pair. This also covers pair double occupancy
and arbitrary superpositions. The fixed exterior order introduces no
permutation. Functoriality of exterior powers gives
F_3(psi wedge v)=(F_2 psi) wedge Wv.
Induction therefore proves U_3^t(psi wedge v)=(U_2^t psi) wedge W^t v
whenever A+[-s,s] and B+[-s,s] are disjoint at each intervening time s.
J changes no positions and W increases support by at most one per step.
This is an occupation-basis proof and, separately, a support induction;
no distinguished physical particle or assumed F enters it.

Put R=floor(L/4). The pair support is contained in
A=[-L-R,L+R] and the spectator in B=[-50L-R,-50L+R].
The gap between their enlarged intervals is 49L-2R-2t, at least
(17/2)L at t=20L. Thus separation holds throughout the prescribed window,
including the instants at which J acts. Pair supports may overlap each other.

## 2. Exact code and initial tails

The three momentum intervals have centres mu times 3,1,-2 and half-width
delta. Adjacent centre distances are at least 2mu > 2delta. All intervals
lie in (-0.4,0.4); their pi translates are disjoint from these and each other
on the torus. Translation of position centres changes only phases.
Gamma shifts momentum by pi, so <phi_j,Gamma phi_k>=0, while
<phi_j,phi_k>=delta_jk. Therefore the six modes u_ja=sqrt(2)Pi_a phi_j
are orthonormal. Their eight declared wedges, B, are an exact isometry;
C=F_3^T B is also an isometry.

The initial-time tail estimate of the low-energy report Sec. 4(iii) applies
to each of these three fixed K supports. The K=-2 packet is the flavour
contract's left packet up to translation; K=1,3 are the co-moving packets.
At t=0 no extension of a time-dependent estimate is needed. The normalized
spinor derivatives in scaled coordinates are uniformly bounded on these
fixed compact K sets. The same two integrations by parts with the stated h
give squared tail <= C(delta R)^(-3). Since L>=101, R>=L/5 and
delta L>=mu^(-1/2). Thus each initial norm tail is O(mu^(3/4)).
Q_j commutes with Gamma and ||sqrt(2)Pi_a||<=sqrt(2), so the same bound
holds for both flavours. Write epsilon for the maximum of these six norm
tails. Truncated modes have norm <=1; they need not be orthonormal.

## 3. Transfer without applying the bridge to truncated modes

For one logical column put psi=u_fa wedge u_sb, v=u_ec, and tildes for
spatially truncated modes. Creation contraction and telescoping give
||psi-tilde psi||<=2 epsilon and
||psi wedge v-tilde psi wedge tilde v||<=3 epsilon.
Unitarity, Section 1 and another telescoping estimate then give
||U_3^T(psi wedge v)-(U_2^T psi) wedge W^T v||<=6 epsilon.
No factor T multiplies this error: the truncation is made once at input,
and both comparisons propagate by unitary maps.

Let eta=||U_2^T B_2-F_2^T B_2 V(r_co)||. The promoted co-moving bridge
states eta=O(mu^(1/2))+O(mu^(3/4)); its hypotheses and time are unchanged.
Wedging its column residual with W^T v costs at most eta, since ||v||=1.
The target is exactly C(V tensor I)|abc>. Each of eight residual columns
has norm <=6 epsilon+eta. Cauchy-Schwarz on their coefficients gives
rho:=||U_3^T B-C(V tensor I)||<=sqrt(8)(6 epsilon+eta)->0.
This covers entangled logical inputs as well as basis inputs.

Since C is isometric,
||K-V tensor I||<=rho, and ||E||<=rho.
As a second consistency check, unitarity gives K* K+E* E=I; the obtained
limits satisfy this identity. This check alone would not establish the gate.

## 4. Frames, limitations and closure

The proved frame is identity order (fast,slow,spectator), with no extra
phase. For a decreasing-position convention, initial order is (f,s,e)
and final free-centre order is (s,f,e): the pair order reverses by the
co-moving bridge, and the spectator remains left of the pair by the
support separation plus vanishing tails. Define the spatial output frame
D|abc>=(W^T u_sa) wedge (W^T u_fb) wedge (W^T u_ec).
Then D=-C(P tensor I), exactly by exterior antisymmetry; hence D*U_3^T B
converges to (-P V) tensor I. These are mode frames, not sharp particle
position measurements. No logical-input-dependent phase is removed.

The argument closes using locality and existing packet estimates, with an
explicit elementary support lemma. It introduces no new scattering solution.
It establishes only this isolated spectator geometry, not successive
collisions or simultaneous three-body scattering. F, COEXISTENCE and
NOVELTY remain OPEN. Independent review and promotion have not occurred.
