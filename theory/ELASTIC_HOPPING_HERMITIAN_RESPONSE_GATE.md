# ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** \`AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED\`
("Hay que congelar", 2026-09-30).  
**Rama:** \`research/gravitational-normalization-gate\`.

## 0. Input and reason for successor

The predecessor

\`\`\`
ELASTIC_HOPPING_UNITARY_RESPONSE_GATE =
UNITARY_ELASTIC_RESPONSE_INCONSISTENT
\`\`\`

failed before any four-species calculation because its generator depended on
an arbitrary orientation set \(F_+\). Exact CJWW Fourier blocks do not satisfy

\[
W_{-h}=W_h^\dagger,
\]

so choosing \(h\) or \(-h\) as representative of an undirected bond changed
the microscopic response.

This successor removes that arbitrary choice **before any species calculation**
by summing over the full directed CJWW support and taking the Hermitian part.

No coefficient or tensor structure below is chosen from a four-species
universality result; that result has not yet been computed for this family.

## 1. Frozen flat CJWW data

Use the exact Fourier decomposition of CJWW Eq. (5.15),

\[
W_0(p)
=
\sum_{h\in F}
e^{ip\cdot h}W_h,
\]

where the support \(F\subset\mathbb Z^3\) is the already certified 14-vector
set.

All \(W_h\) are inherited exactly from the flat walk.

No new Pauli-selective matrices, valley labels or species-dependent
coefficients are introduced.

## 2. Common elastic control

Use one real symmetric strain tensor

\[
u=u^T\in\mathrm{Sym}(3).
\]

For each nonzero support displacement \(h\in F\), define the scalar
bond-length response

\[
\rho_h(u)
=
\frac{h^Tuh}{h^Th}.
\]

Because

\[
\rho_{-h}(u)=\rho_h(u),
\]

the strain control is orientation blind.

The same \(u\) is used for all four decisive \(+I\) Weyl species.

## 3. Orientation-independent bond-weighted symbol

Define

\[
R_u(p)
=
\sum_{h\in F}
\rho_h(u)e^{ip\cdot h}W_h.
\]

No half-support \(F_+\) appears.

Define the Hermitian elastic generator

\[
\boxed{
K_u(p)
=
\frac12\left(
R_u(p)+R_u(p)^\dagger
\right).
}
\]

Then

\[
K_u(p)^\dagger=K_u(p)
\]

identically for real \(p\) and real symmetric \(u\).

The generator is fixed entirely by:

1. the exact CJWW blocks \(W_h\);
2. the common geometric scalar \(\rho_h(u)\);
3. Hermitian symmetrization.

No orientation convention remains.

## 4. Common embedding and exact unitary response

Retain the common physical embedding used by the predecessor successful
kinematic gate,

\[
X_\varepsilon(n)
=
a(I+\varepsilon u)n.
\]

Thus common physical momentum \(q\) enters the abstract CJWW symbol through

\[
p
=
a(I+\varepsilon u)^Tq.
\]

The deformed symbol is frozen as

\[
\boxed{
W_{\varepsilon,u}(q)
=
e^{-i\varepsilon K_u(p)}
W_0(p),
\qquad
p=a(I+\varepsilon u)^Tq.
}
\]

For real \(\varepsilon\), the prefactor is unitary because \(K_u\) is
Hermitian, so \(W_{\varepsilon,u}\) is exactly unitary.

At \(\varepsilon=0\),

\[
W_{\varepsilon,u}(q)
=
W_0(aq),
\]

independently of \(u\).

The overall elastic material coefficient is absorbed into \(\varepsilon\)
and is not tunable after execution.

## 5. Scope of the response rule

This is a **minimal orientation-independent unitary elastic-response ansatz**.

It is motivated by the standard elastic tight-binding rule that a bond
responds to its longitudinal strain \( \hat h^T u\hat h \), but it is not
claimed to be uniquely derived from microscopic CJWW dynamics.

The full exponential can enlarge strict one-step Fourier support beyond the
original 14 hops at nonzero \(\varepsilon\). Therefore the claim is a
finite-range-generator / exactly unitary Floquet response, not literal scalar
rescaling of the fourteen flat transition matrices.

## 6. Geometry versus gauge decomposition

For each decisive flat \(+I\) node \(p_*\), compare species in common physical
coordinates.

The flat physical node is

\[
q_*^{(0)}=a^{-1}p_*.
\]

At first order in strain, allow a species-dependent node displacement

\[
q_*
=
q_*^{(0)}
+
\varepsilon\,\delta q_*.
\]

A momentum-independent traceless Pauli term that can be removed by
\(\delta q_*\) is classified as vector/axial gauge structure, not metric.

A residual identity term is a quasienergy/scalar shift and does not enter the
metric.

After recentering,

\[
q=q_*+\kappa,
\]

extract the linear principal frame from

\[
s_*W_{\varepsilon,u}(q)
=
e^{-i\varepsilon\alpha_*}
\left[
I
+
i\sigma^a
E_{*a}^{(\varepsilon,u)\,i}
\kappa_i
+
O(|\kappa|^2,\varepsilon^2)
\right].
\]

Only

\[
h_*=
(E_*^{(\varepsilon,u)})^T
E_*^{(\varepsilon,u)}
\]

enters the species-metric test.

## 7. Obligations

### HH0 — exact flat recovery

At \(\varepsilon=0\),

\[
W_{\varepsilon,u}(q)=W_0(aq).
\]

### HH1 — orientation independence and Hermiticity

Prove symbolically that:

\[
\rho_{-h}=\rho_h,
\]

the definition contains the entire support \(F\), and

\[
K_u(p)^\dagger=K_u(p).
\]

No arbitrary orientation set may enter the certificate.

### HH2 — exact unitarity

For real \(\varepsilon\),

\[
W_{\varepsilon,u}^\dagger
W_{\varepsilon,u}
=
I.
\]

### HH3 — node/gauge decomposition

At each of the four decisive \(+I\) nodes:

1. derive the \(O(\varepsilon)\) constant perturbation;
2. separate identity/quasienergy shift;
3. solve the traceless constant term as a node displacement
   \(\delta q_*\), if possible;
4. fail closed if an uncancellable traceless constant term remains.

### HH4 — four-species metric kill test

For arbitrary symmetric \(u\), compute the first-order metric perturbations

\[
\delta h_{*1}(u),\ldots,\delta h_{*4}(u)
\]

in common physical coordinates.

Necessary PASS condition:

\[
\boxed{
\delta h_{*1}
=
\delta h_{*2}
=
\delta h_{*3}
=
\delta h_{*4}
}
\]

as linear maps on the six independent components of \(u\).

No species-dependent coordinate redefinition is allowed.

### HH5 — universal metric rank

If HH4 passes, compute the rank of

\[
u\mapsto\delta h(u).
\]

A full spatial metric response requires rank \(6\).

### HH6 — decomposition of universal response

If HH4 passes, separate the common metric response into:

1. the already-known common-embedding contribution;
2. the new hopping-response contribution generated by \(K_u\).

Report whether the hopping term contributes nontrivially to the common metric
or only to node shifts/gauge/scalar terms.

A PASS based solely on the embedding term must be stated as such.

### HH7 — no rescue

After execution begins, do not change:

- the Hermitian-part prescription;
- the bond scalar \(\rho_h\);
- the order \(e^{-i\varepsilon K_u}W_0\);
- the common embedding;
- any coefficient;
- the set of species;
- the common-coordinate convention.

If universality fails, the gate fails.

## 8. Terminal states

Apply in order:

1. \`HERMITIAN_ELASTIC_RESPONSE_INCONSISTENT\`.
2. \`NODE_GAUGE_DECOMPOSITION_FAIL\`.
3. \`HERMITIAN_ELASTIC_METRIC_NON_UNIVERSAL\`.
4. \`HERMITIAN_ELASTIC_METRIC_UNIVERSAL_RANK_DEFICIENT\`.
5. \`HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY\`.
6. \`HERMITIAN_ELASTIC_METRIC_UNIVERSAL_NONTRIVIAL /
   DYNAMICAL_STRAIN_OPEN\`.
7. \`OPEN_AFTER_AUDIT\`.

State 5 applies if rank 6 universality survives but the new hopping generator
adds no nontrivial universal metric deformation beyond the common embedding.

State 6 requires both rank 6 universality and a nonzero universal
hopping-induced metric contribution.

## 9. Stop rule

At the first applicable terminal state, stop.

In particular:

- do not tune the ansatz if HH3/HH4 fails;
- do not move to backreaction, spin-2 or constraints after a positive result;
- a positive result authorizes only a separately chartered
  dynamical-strain/backreaction successor.

W6/W12 remain unchanged for their Pauli-selective fixed-graph control class.

## 10. Claim ceiling

This gate tests one orientation-independent, exactly unitary,
strain-dependent CJWW Floquet response.

It does not establish:

- uniqueness or microscopic derivation of the response;
- phonon or graph dynamics;
- curvature;
- emergent gravity;
- universal coupling beyond the four tested species;
- spin-2 dynamics;
- Einstein constraints;
- \(G_{\rm eff}\), AdS, absolute scale, or nature.
