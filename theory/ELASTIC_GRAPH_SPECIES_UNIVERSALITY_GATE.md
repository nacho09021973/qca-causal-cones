# ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** \`AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED\`
("congelada, vamos a intentarlo", 2026-09-30).  
**Rama:** \`research/gravitational-normalization-gate\`.

## 0. Contractual reopening basis

W12 closed the gravity line for the **W6/CJWW control class** after
\`UNIVERSAL_SUBFAMILY_DEFICIENT\`. Its frozen consequence permits reopening
only for a **new control family with an independent physical justification
written before calculation**.

This gate is not a repair of W6.

Independent motivation predates W12 in-repo:

- \`DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE\` (2026-09-29) identifies graph/link
  degrees of freedom as the candidate geometry class and explicitly
  distinguishes them from a spectator internal register.
- D'Ariano–Perinotti derive homogeneous QCA kinematics on Cayley graphs.
- Arrighi–Martiel treat the graph itself as the evolving quantum-geometric
  object.
- Cortijo–Zubkov (cubic Weyl tight binding with elastic deformation) derive
  both an emergent gauge field and an anisotropic Fermi-velocity/vierbein
  field from a single deformation of the lattice/hoppings. The geometry and
  gauge sectors are distinct.

The physical design principle frozen here is therefore:

> geometry is a single deformation of the spatial support/embedding shared by
> all matter components; internal Pauli/valley-selective terms are not used to
> define the metric.

This motivation is independent of the numerical/rank failure of W12.

## 1. Frozen matter sector

Matter remains the exact one-particle CJWW Eq. (5.15) walk on
\[
\mathcal H_m=\ell^2(\mathbb Z^3)\otimes\mathbb C^2.
\]

The decisive low-quasienergy species are exactly the four W11/W12 \`+I\`
nodes
\[
p_*\in\{(0,0,0),(\pi,\pi,0),(\pi,0,\pi),(0,\pi,\pi)\}.
\]

Their flat linear frames \(E_*\) are inherited from the reviewed W11/W12
node table. All species are compared in **common physical lattice
coordinates**. No species-dependent spatial relabelling or reflection is
allowed.

## 2. New geometric control family

Let
\[
\Lambda=I+\varepsilon L,\qquad \Lambda\in GL^+(3,\mathbb R),
\]
with \(\varepsilon\) formal and \(L\) an arbitrary real \(3\times3\) matrix.

The physical embedding of lattice sites is
\[
X_\Lambda(n)=a\,\Lambda n.
\]

Every abstract CJWW displacement \(h\in\mathbb Z^3\) is realized by the
physical edge vector
\[
\ell_h(\Lambda)=a\,\Lambda h.
\]

The internal CJWW transition block attached to the abstract hop \(h\) is
**unchanged** in this first gate. Thus:

- no \(z_{ar}\);
- no Pauli-selective transport control;
- no valley-dependent control;
- no extra gauge/axial term is inserted by hand.

The abstract one-step unitary is still exactly \(U_0\), while the relation
between common physical momentum \(q\) and dimensionless lattice momentum is
\[
p=a\,\Lambda^T q.
\]

Hence the homogeneous embedded-graph symbol is, by definition of this class,
\[
W_\Lambda(q)=W_0(a\,\Lambda^T q).
\]

This preserves exact unitarity because it is the same CJWW walk represented
on one affinely deformed physical embedding.

### Scope warning

This is the **minimal common-geometry subclass**. It does not yet include the
strain-induced change of hopping amplitudes studied in tight-binding
semimetals. Therefore a positive result here establishes only a
species-universal **embedded-graph principal metric**, not a nontrivial
elastic response of the CJWW gate matrices.

That distinction is part of the frozen contract.

## 3. Geometry versus gauge

For any later extension, the low-energy symbol must be decomposed into:

1. tetrad/principal-symbol terms, which define the metric;
2. connection/internal terms;
3. vector or axial gauge terms, possibly valley dependent.

Only item 1 enters the species-metric universality test.

A valley-dependent gauge field does not count as metric non-universality.
A valley-dependent \(g^{ij}\) does.

No such extra terms are present in the minimal family of §2.

## 4. Obligations

### E0 — exact flat recovery
At \(\Lambda=I\),
\[
W_\Lambda(q)=W_0(aq).
\]

### E1 — node transport under common embedding
For each decisive flat node \(p_*\), define its physical reciprocal-space
location
\[
q_*(\Lambda)=a^{-1}\Lambda^{-T}p_*.
\]

Expand at common physical momentum
\[
q=q_*(\Lambda)+\kappa.
\]

Derive the frame \(E_*^{(\Lambda)}\) from
\[
s_*W_\Lambda(q)
=
I+i\sigma^a E_{*a}^{(\Lambda)\,i}\kappa_i
+O(|\kappa|^2).
\]

### E2 — species metric kill test
Compute
\[
h_*^{(\Lambda)}
=
(E_*^{(\Lambda)})^T E_*^{(\Lambda)}
\]
for all four \`+I\` species in the same physical coordinates.

The necessary PASS condition is
\[
h_{*1}^{(\Lambda)}
=
h_{*2}^{(\Lambda)}
=
h_{*3}^{(\Lambda)}
=
h_{*4}^{(\Lambda)}
\]
to first order in \(\varepsilon\), for arbitrary \(L\).

### E3 — metric span
For the symmetric strain
\[
u=\frac12(L+L^T),
\]
compute the rank of
\[
u\mapsto \delta h.
\]

A full geometric family at this kinematic level requires rank 6.

The antisymmetric part of \(L\) may act as a rigid frame rotation and must be
reported separately; it does not count toward metric rank.

### E4 — coordinate/embedding ceiling
If E1–E3 pass solely because the abstract unitary is unchanged and the common
embedding pushes momentum covariantly, record
\[
\texttt{KINEMATIC\_COMMON\_EMBEDDING\_UNIVERSAL}
\]
rather than a claim of dynamical gravity.

No curvature, backreaction or hopping-response conclusion follows.

### E5 — no W6 rescue
Whatever the outcome, W12 remains the negative result for the W6/CJWW
Pauli-selective control class. This gate neither modifies nor reinterprets
\[
\dim\mathcal U=3,\qquad \operatorname{rank}=3/6.
\]

## 5. Terminal states

Apply in order:

1. \`ELASTIC_GRAPH_CLASS_INCONSISTENT\` — the frozen common-embedding family
   is not well-defined/unitary under its own contract.
2. \`SPECIES_METRIC_NON_UNIVERSAL\` — E2 fails.
3. \`SPECIES_METRIC_UNIVERSAL_RANK_DEFICIENT\` — E2 passes, E3 rank < 6.
4. \`KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / ELASTIC_HOPPING_RESPONSE_OPEN\` —
   E2 passes and E3 has rank 6, but the result is only the common-embedding
   kinematics of §2.
5. \`OPEN_AFTER_AUDIT\`.

## 6. Stop rule

If terminal state 4 is reached, stop.

Do **not** immediately re-run W3–W11 and do not call the gravity line reopened
in full. A separate successor would first have to freeze a physically
motivated, unitary rule for strain-dependent CJWW hopping amplitudes or a
genuine dynamical-graph update, and repeat the four-species metric kill test.

No such rule may be chosen after seeing this gate's result merely to rescue a
failure.

## 7. Claim ceiling

This gate concerns only:

- one-particle CJWW (5.15);
- homogeneous affine common embedding;
- first-order species metric universality;
- rank of the induced spatial metric family.

It makes no claim about strain-induced hopping renormalization, gauge fields,
backreaction, curvature, spin 2, constraints, Einstein dynamics, \(G_{\rm eff}\),
AdS, absolute scale, or nature.
