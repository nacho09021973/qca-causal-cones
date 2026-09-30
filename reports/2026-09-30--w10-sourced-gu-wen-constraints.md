# W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE](../theory/W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md), frozen at commit \`7109a3ae5d5c3aaf958cf473c0f6a0200413664d\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

> **SUPERSEDED — see §9.** The block below is historical. Current gate:
> **OPEN_AFTER_AUDIT**; C5 is not met by the available integrated charges.

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

## 9. Repair addendum — 2026-09-30 (supersedes the terminal decision)

Inputs: [blind-review repairs](../debates/2026-09-30--w9-w11-blind-review/reparaciones.md)
and [source check at 7903713](../investigaciones/2026-09-30-prior-art-walk-graviton/comprobacion.md).
The report at `f956f68` and its frozen contract are not rewritten.
**Second-review update (2026-09-30):** the review at `d6e74e6` covers snapshot
`86fe771`: DeepSeek ACCEPT; Opus ACCEPT_WITH_REPAIRS. This §9 implements
items 3–4 and 9 of the
[review README](../debates/2026-09-30--w9-w11-repair-review/README.md).
The continuum calculation is supported by that review; the local-source
and backreaction questions remain OPEN.

### A4 — correct the premature terminal state

W10's terminal PASS was recorded at `f956f68`, before W11's contract
`cfdc5c6`. C5 requires controlled low-energy source operators; the continuum
identity alone did not meet that requirement at that time. The former
terminal decision is therefore superseded, not retrospectively justified
by the later W11 report.

Reevaluation after A2 and the explicit A3 downgrade: W11 now supplies a
finite-range exactly conserved free energy charge K with a controlled
narrow-band error. It still does not supply the full local Belinfante
stress at nonzero transfer, the four-species source matching, or a sourced
constraint/Ward identity. Hence the conditions of C5 have not been shown
for the intended local matter–geometry bridge. The authoritative state is

```
W10 = OPEN_AFTER_AUDIT
C1 = PASS / EXPLICIT_CONTINUUM_CONVENTION_BELOW
C2 = PASS / FLAT_TEST_SOURCE_AT_O(lambda)_ONLY
C3 = ZERO_TRANSFER_SPATIAL_TETRAD_SOURCE / PARTIAL
C4 = OPEN
C5 = CONDITIONAL_ON_FULL_W11_LOCAL_SOURCE_MATCH / NOT_MET
```

Restoring the former weak PASS requires the missing W11 source matching
and a controlled constraint identity in an explicitly specified low-energy
sector. An exact microscopic Floquet stress remains a separate stronger
condition. Neither is inferred from conservation of a global charge.

### B1 — fixed quadratic action, signs and relative coefficients

Fix signature \(\eta=\operatorname{diag}(-1,1,1,1)\), lower-index symmetric
perturbation \(h_{\mu\nu}\), and compact support or boundary conditions
that remove surface terms. Indices are raised with η. Put
\(h=\eta^{\mu\nu}h_{\mu\nu}\), \(\Box=\eta^{\mu\nu}\partial_\mu\partial_\nu\).
The following choice fixes the gravitational field normalization for this
continuum calculation; it does not derive a Newton constant:

\[
S_g^{(2)}=-\frac12\int h_{\mu\nu}G_{\rm lin}^{\mu\nu}(h),\qquad
S_{\rm int}=\frac\lambda2\int h_{\mu\nu}T_{(0)}^{\mu\nu},
\]

\[
G^{\rm lin}_{\mu\nu}=\frac12\left[
\partial_\mu\partial^\rho h_{\rho\nu}
+\partial_\nu\partial^\rho h_{\rho\mu}
-\Box h_{\mu\nu}-\partial_\mu\partial_\nu h
-\eta_{\mu\nu}(\partial^\rho\partial^\sigma h_{\rho\sigma}-\Box h)
\right].
\]

Here \(T_{(0)}\) is symmetric and independent of h in the variation.
The operator is formally self-adjoint (two integrations by parts). Thus
\(\delta S_g=-\int\delta h_{\mu\nu}G_{\rm lin}^{\mu\nu}\) and

\[
G_{\rm lin}^{\mu\nu}=\frac\lambda2 T_{(0)}^{\mu\nu}.
\]

For independent components, the lapse variation is
\(-G^{00}+\lambda T_{(0)}^{00}/2=0\), while the shift variation is
\(-2G^{0i}+\lambda T_{(0)}^{0i}=0\). Diagonal spatial components have
multiplicity one; off-diagonal spatial components have multiplicity two.
There are no independent adjustable scalar/vector source normalizations.
The shift is a Lagrange multiplier **in the Hamiltonian formulation**, after
the Legendre transform introduces the spatial canonical momenta. In the
quadratic Lagrangian displayed here, h00 is linear while h0i enters
quadratically (through spatial derivatives). There is no shift time-kinetic
term, but that does not make the shift a linear Lagrangian multiplier.
This qualifies the historical multiplier wording in §§1–2; Gu–Wen's
first-order canonical form and the h-only Lagrangian must be distinguished.
Equivalently, define \(\mathcal C^\nu_{\rm geom}=2G^{0\nu}_{\rm lin}\):

\[
\mathcal C^0_{\rm geom}=\partial_i\partial_jh_{ij}-\Delta h_{jj}
=\lambda T_{(0)}^{00},
\]

\[
\mathcal C^i_{\rm geom}=-\partial_j\dot h_{ij}
+\partial_i\dot h_{jj}+\Delta h_{0i}
-\partial_i\partial_jh_{0j}
=\lambda T_{(0)}^{0i}.
\]

These explicit definitions replace the schematic independent normalizations
in §2. Their numerical mapping to Gu–Wen's canonical variables and J,g is
not asserted. The coefficient λ in the former §3 equation must be replaced
by λ/2 in this action convention (or renamed consistently everywhere).

### B2–B3 — continuum target and perturbative ceiling

C2 uses **the constrained continuum Einstein target**, not the controlled
Gu–Wen lattice L model. Gu–Wen, `biblioteca/arXiv-0907.1203.pdf` p.12,
eq.(37), introduce the multipliers and state the continuum Einstein-action
result. Their p.1 distinguishes the controlled L model with cubic dispersion
from the less controlled linear-dispersion N proposal. Both pages were
re-read in this session. The L model cannot be substituted for this action:
its cubic modes do not obey the TT wave equation derived here. No sourced
L-model dynamics or controlled lattice realization of this continuum target
is established by W10.

The Bianchi identity gives compatibility with a prescribed **free flat-space**
\(T_{(0)}\) satisfying \(\partial_\mu T_{(0)}^{\mu\nu}=0\). For the CJWW
application the required tensor is the total of **all four** zero-quasienergy
species, \(T_{(0)}^{\mu\nu}=\sum_{s_*=+1}T_{*,(0)}^{\mu\nu}\), in their
respective frames. Its full local microscopic matching has not been
constructed: this is an input to C2, not a new W11 output. In a coupling
expansion at fixed weak h, if matter responds as
\(T=T_{(0)}+\lambda T_{(1)}+\cdots\), the source \(\lambda T/2\) acquires
O(λ²) terms. The free identity alone does not control their divergence.
Reciprocal backreaction needs the corresponding higher-order matter and
gravity identities/self-couplings; they are not included here. Thus C2 is
restricted to test-source consistency at O(λ), not a coupled closure test.
No unverified Gupta/Deser attribution is needed for this restriction.

The new [certificate](../scripts/verify_w10_linearized_constraints.py)
checks all ten variations, the scalar/vector component formulas, Bianchi
and gauge identities for arbitrary formal momentum, and the independent
TT limit \(G_{12}=(\partial_t^2-\partial_3^2)h_{12}/2\). This verifies the
chosen continuum calculation, not source conservation in a coupled QCA.

### Prior-art and closure boundary

The source audit through `7903713` locates no counterexample to a CJWW-like
matter–graviton construction with reciprocal backreaction among the checked
papers. That is a bounded search result, not a novelty proof. The outstanding
source checks listed there remain outstanding; no proposed catalog tag is
promoted by this repair.

A1/A2/A4 are repaired; A3 takes the permitted downgrade, B1 fixes the continuum
convention, and B2/B3 restrict C2 to the actual continuum/test-source result.
A joint Einstein–Weyl gate is **not ready to freeze** from these results.
