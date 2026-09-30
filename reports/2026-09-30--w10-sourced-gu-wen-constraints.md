# W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE](../theory/W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md), frozen at commit \`7109a3ae5d5c3aaf958cf473c0f6a0200413664d\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE =
CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS /
MICROSCOPIC_CJWW_CHARGES_OPEN

C1 = PASS
C2 = PASS
C3 = PASS / SPATIAL ONLY
C4 = OPEN
\`\`\`

W10 does not invent a new graviton sector. It imports the linearized
constraint architecture already available in Gu-Wen and tests whether the
CJWW Weyl matter sector can source it consistently.

## 1. Prior-art architecture

Gu-Wen introduce the time-space and time-time metric variables as Lagrange
multipliers for the vector and scalar constraints. In their continuum
notation the corresponding terms are of the form

\[
2a_{0i}\partial_j\mathcal E^{ij}
+
a_{00}
\left(
\partial^2 a_{ii}
-
\partial_i\partial_j a_{ij}
\right).
\]

They state that, after integrating out the conjugate tensor momentum, the
result is the linearized Einstein action about flat spacetime.

They then discretize the vector and scalar constraints on the cubic lattice
and impose them through energy-penalty terms in a compactified finite local
Hilbert space.

Those facts are treated as prior art, not project results.

## 2. C1 — continuum matter sourcing

Add the linearized matter coupling

\[
S_{\rm int}
=
\frac{\lambda}{2}
\int d^4x\,
h_{\mu\nu}T^{\mu\nu}.
\]

The lapse-like perturbation \(h_{00}\) enters without a propagating kinetic
role at this linearized constraint level. Varying with respect to it gives the
scalar constraint with source proportional to

\[
T^{00}.
\]

Likewise the shift-like variables \(h_{0j}\) multiply the vector constraints,
and variation gives sources proportional to

\[
T^{0j}.
\]

Thus the vacuum Gu-Wen constraints acquire the schematic sourced form

\[
\boxed{
\mathcal C^0_{\rm geom}
=
\lambda T^{00},
}
\]

\[
\boxed{
\mathcal C^j_{\rm geom}
=
\lambda T^{0j}.
}
\]

The precise numerical convention is deliberately left open because the
gravitational normalization has not been derived.

\[
\boxed{\texttt{C1 = PASS}.}
\]

## 3. C2 — continuum consistency

The linearized Einstein tensor satisfies the identity

\[
\partial_\mu G_{\rm lin}^{\mu\nu}=0.
\]

If the sourced field equation is

\[
G_{\rm lin}^{\mu\nu}
=
\lambda T^{\mu\nu},
\]

then consistency requires

\[
\partial_\mu T^{\mu\nu}=0.
\]

The low-energy continuum Weyl field has a conserved stress tensor on its
equations of motion.

Therefore the sourced scalar/vector constraints are compatible with the
evolution equations at the declared continuum order.

Equivalently, the same conservation identity that repaired the W9 gauge
variation supplies the source-consistency condition here.

\[
\boxed{\texttt{C2 = PASS}.}
\]

## 4. C3 — spatial source compatibility with W5/W6

W5/W6 already established the spatial tetrad-conjugate operator family

\[
J^{(a,r)}(p)
=
2\sin(p\cdot d_r)\sigma_a
=
2d_r{}^i p_i\sigma_a+O(|p|^3).
\]

Because the W6 direction matrix is invertible, these span the spatial
structures

\[
\sigma_a p_i
\]

obtained by varying the Weyl Hamiltonian with respect to spatial tetrad
components.

Thus the project already has a microscopic candidate for the **spatial**
stress/tetrad source.

What W10 adds is the requirement that the temporal constraint charges be the
correct

\[
T^{00},\qquad T^{0i},
\]

not endpoint occupation or particle number by relabeling.

\[
\boxed{\texttt{C3 = PASS / SPATIAL ONLY}.}
\]

## 5. C4 — exact microscopic CJWW energy/momentum charges are not available

The frozen CJWW model is a discrete-time unitary/Floquet walk.

Its low-energy logarithm near the Weyl node produces the expected continuum
Weyl Hamiltonian. That is enough to define continuum

\[
T^{00},\qquad T^{0i},\qquad T^{ij}
\]

to the order used in W9-W10.

However, the repository does not currently contain a proved set of strictly
local microscopic Floquet operators

\[
\widehat T^{00}_x,\qquad
\widehat T^{0i}_x
\]

with all of the following:

1. exact or controlled discrete continuity relations;
2. the correct Weyl low-energy limit;
3. a local insertion into Gu-Wen-type constraint projectors/penalties;
4. preservation of exact flat CJWW at zero matter-gravity coupling.

In particular, the local particle-number density is not an acceptable
substitute for energy density.

A Floquet quasienergy is also not automatically a local conserved energy
density.

Therefore:

\[
\boxed{\texttt{C4 = OPEN}.}
\]

## 6. Scientific consequence

The programme no longer has to guess how matter should source the graviton
constraints.

At low energy the bridge is fixed structurally:

\[
\boxed{
T^{00}
\longrightarrow
\text{scalar/Hamiltonian constraint}
}
\]

and

\[
\boxed{
T^{0i}
\longrightarrow
\text{vector/momentum constraints}.
}
\]

Together with W5/W6,

\[
T^{ij}
\longrightarrow
\text{spatial tetrad dynamics}.
\]

So the complete continuum source object is precisely the Weyl stress tensor.

The remaining difficulty is a discrete-time microscopic realization of that
stress tensor inside the CJWW QCA.

## 7. Why this matters for novelty

Gu-Wen already provide the vacuum tensor/graviton constraint structure.
The project-specific unresolved contribution is now sharply isolated:

\[
\boxed{
\text{CJWW Weyl matter}
+
\text{sourced emergent-gravity constraints}
+
\text{reciprocal backreaction}
}
\]

in one local discrete-time construction.

That is a materially narrower and more defensible target than “emergent
gravity from qubits.”

Novelty of the combined bridge remains OPEN pending dedicated literature
review.

## 8. Terminal decision

\[
\boxed{
\texttt{CONTINUUM\_SOURCED\_CONSTRAINT\_BRIDGE\_PASS /
MICROSCOPIC\_CJWW\_CHARGES\_OPEN}
}
\]

is the terminal state.

The next admissible task is not another gravity ansatz. It is a
**CJWW FLOQUET STRESS-TENSOR GATE**: determine whether suitable local
low-energy energy/momentum densities can be derived from the exact walk with
controlled continuity identities.
