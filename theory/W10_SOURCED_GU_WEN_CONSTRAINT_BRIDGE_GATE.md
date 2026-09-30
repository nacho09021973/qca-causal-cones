# W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** \`AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## 0. Prior-art import boundary

Gu-Wen already supply the vacuum linearized-gravity constraint architecture:

- spatial symmetric tensor geometry;
- vector constraint of the form \(\partial_i\mathcal E^{ij}=0\);
- scalar curvature constraint;
- \(a_{0i}\) and \(a_{00}\) as Lagrange multipliers;
- recovery of the linearized Einstein action in the continuum;
- lattice realization of the constraints through energy-penalty terms after
  compactification/discretization.

These ingredients are prior art and are not reconstructed as project novelty.

## 1. Single project-specific question

Can the low-energy CJWW Weyl matter sector enter the Gu-Wen-type linearized
gravity constraints as a consistent source?

The continuum target is schematically

\[
\mathcal C^j
=
\partial_i\mathcal E^{ij}
-\lambda\,T^{0j}
=0
\]

and

\[
\mathcal C^0
=
\mathcal R^{(1)}
-\lambda\,T^{00}
=0,
\]

where \(\mathcal R^{(1)}\) denotes the linearized scalar-curvature constraint
in the chosen convention and \(\lambda\) is an unfixed coupling.

No normalization to \(8\pi G\) is assumed.

## 2. C1 — continuum variational sourcing

Starting from

\[
S_{\rm grav}^{(2)}
+
\frac{\lambda}{2}\int h_{\mu\nu}T^{\mu\nu},
\]

variation with respect to lapse-like \(h_{00}\) and shift-like \(h_{0j}\)
must produce sourced scalar and vector constraints proportional to
\(T^{00}\) and \(T^{0j}\), respectively.

## 3. C2 — constraint consistency

Use:

\[
\partial_\mu G_{\rm lin}^{\mu\nu}=0
\]

and

\[
\partial_\mu T^{\mu\nu}=0
\]

to verify that the sourced continuum equations are mutually consistent.

This is a low-energy continuum statement only.

## 4. C3 — spatial source match

Check compatibility with W5/W6:

- spatial tetrad variation gives the lattice current family
  \(J^{(a,r)}\);
- in the Weyl continuum, those span the spatial
  \(\sigma_a p_i\) structures entering the tetrad stress.

The gate must distinguish this already-supported spatial source from the new
constraint charges \(T^{00}\) and \(T^{0j}\).

## 5. C4 — microscopic CJWW charge operators

A microscopic PASS requires explicit local lattice/Floquet operators
\(\widehat T^{00}_x\) and \(\widehat T^{0j}_x\) such that:

1. their low-energy limit is the Weyl energy and momentum density;
2. they obey a controlled discrete continuity/constraint identity to the
   required order;
3. they can be inserted into local Gu-Wen-type constraint penalties or
   projectors without destroying exact flat CJWW recovery when
   \(\lambda=0\).

A particle-number density is not accepted as \(T^{00}\) merely because it is
local.

## 6. C5 — low-energy constrained subspace

If exact microscopic charges are unavailable but controlled low-energy
operators exist, record the weaker state

\`CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS /
MICROSCOPIC_CJWW_CHARGES_OPEN\`.

Do not require exact microscopic diffeomorphism symmetry if the constraints
and Ward identities emerge in a controlled low-energy sector.

## 7. Terminal states

1. \`SOURCED_CONSTRAINT_BRIDGE_FAIL\`.
2. \`CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS /
   MICROSCOPIC_CJWW_CHARGES_OPEN\`.
3. \`MICROSCOPIC_SOURCED_CONSTRAINT_BRIDGE_PASS\`.
4. \`OPEN_AFTER_AUDIT\`.

## 8. Claim ceiling

Passing the continuum gate does not establish nonlinear GR, a unique Newton
constant, universal equivalence-principle coupling beyond the tested Weyl
sector, or an absolute scale.
