# ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE](../theory/ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md), frozen at commit \`25d81383a0821ee1c8e2f5a196d1611c4da4ecf3\`.  
**Certificado:** [verify_elastic_graph_species_universality.py](../scripts/verify_elastic_graph_species_universality.py), added at commit \`103a2c45ada5dec2e167f875482a2fe6ce1f447d\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE =
KINEMATIC_COMMON_EMBEDDING_UNIVERSAL /
ELASTIC_HOPPING_RESPONSE_OPEN

E0 = PASS
E1 = PASS
E2 = PASS EXACTLY
E3 = PASS, METRIC RANK 6/6
E4 = ACTIVE CLAIM CEILING
W12/W6 NEGATIVE RESULT = UNCHANGED
\`\`\`

The new common-geometry class passes the four-species metric kill test for the
minimal homogeneous affine embedding. The pass is exact at the linear
principal-symbol level in species momentum and, as a metric identity, exact
in the affine matrix \(\Lambda\).

It does **not** yet establish a nontrivial elastic response of the CJWW
transition blocks.

## 1. Frozen deformation

The abstract CJWW walk is unchanged. The physical embedding is

\[
X_\Lambda(n)=a\,\Lambda n,
\qquad
\Lambda=I+\varepsilon L\in GL^+(3,\mathbb R).
\]

Every abstract displacement \(h\) is represented by the same common physical
edge vector

\[
\ell_h=a\,\Lambda h
\]

for every internal component and every Weyl species.

The common physical reciprocal momentum \(q\) enters the exact flat symbol as

\[
\boxed{
W_\Lambda(q)=W_0(a\Lambda^Tq).
}
\]

No \(z_{ar}\), Pauli-selective control, valley-dependent metric control,
vector gauge field or axial gauge field is inserted.

Because the abstract one-step operator remains \(U_0\), exact unitarity and
the CJWW local transition algebra are retained.

## 2. E0 — flat recovery

At

\[
\Lambda=I,
\]

\[
W_\Lambda(q)=W_0(aq).
\]

Thus, in the original dimensionless lattice momentum \(p=aq\), the walk is
exactly CJWW Eq. (5.15).

\[
\boxed{\texttt{E0 = PASS}.}
\]

## 3. E1 — the four nodes in common physical coordinates

Let \(p_*\) be any of the four decisive W11/W12 \(+I\) nodes.

Its physical reciprocal-space location under the common embedding is

\[
\boxed{
q_*(\Lambda)=a^{-1}\Lambda^{-T}p_*.
}
\]

Now write

\[
q=q_*(\Lambda)+\kappa.
\]

Then

\[
a\Lambda^Tq
=
p_*+a\Lambda^T\kappa.
\]

The reviewed flat CJWW expansion is

\[
s_*W_0(p_*+\delta p)
=
I+i\sigma^a E_{*a}{}^i\delta p_i
+O(|\delta p|^2),
\]

with

\[
E_*^TE_*=I
\]

at every decisive \(+I\) node.

Substituting

\[
\delta p=a\Lambda^T\kappa
\]

gives

\[
s_*W_\Lambda(q_*+\kappa)
=
I+i\sigma^a
\left(aE_*\Lambda^T\right)_a{}^j
\kappa_j
+O(|\kappa|^2).
\]

Therefore the deformed physical frame is

\[
\boxed{
E_*^{(\Lambda)}=aE_*\Lambda^T.
}
\]

The same \(\Lambda\) acts at every species. No species-dependent coordinate
map is used.

\[
\boxed{\texttt{E1 = PASS}.}
\]

## 4. E2 — exact four-species metric universality

The physical spatial metric seen by species \(*\) is

\[
h_*^{(\Lambda)}
=
(E_*^{(\Lambda)})^TE_*^{(\Lambda)}.
\]

Using the previous result,

\[
h_*^{(\Lambda)}
=
a^2\Lambda E_*^TE_*\Lambda^T.
\]

But all four decisive flat species satisfy

\[
E_*^TE_*=I.
\]

Hence

\[
\boxed{
h_*^{(\Lambda)}
=
a^2\Lambda\Lambda^T
}
\]

for **every** one of the four \(+I\) species.

Thus

\[
\boxed{
h_{*1}^{(\Lambda)}
=
h_{*2}^{(\Lambda)}
=
h_{*3}^{(\Lambda)}
=
h_{*4}^{(\Lambda)}
}
\]

exactly within the frozen homogeneous affine common-embedding class.

The W12 sign flips in the individual frames remain present in \(E_*\), but
they cancel in the metric because they are orthogonal frame flips rather than
species-dependent geometry in this class.

\[
\boxed{\texttt{E2 = PASS EXACTLY}.}
\]

## 5. E3 — full spatial metric rank

Write

\[
\Lambda=I+\varepsilon L.
\]

Then

\[
\frac{h^{(\Lambda)}}{a^2}
=
(I+\varepsilon L)(I+\varepsilon L^T)
\]

and therefore

\[
\boxed{
\frac{\delta h}{a^2}
=
\varepsilon(L+L^T)+O(\varepsilon^2).
}
\]

If

\[
u=\frac12(L+L^T)
\]

is the symmetric strain,

\[
\boxed{
\delta h=2a^2\varepsilon u.
}
\]

The map from the six independent components of \(u\) to the six independent
components of \(\delta h\) has exact rank

\[
\boxed{6/6}.
\]

The three-dimensional tangent kernel in the full nine-dimensional distortion
space consists precisely of antisymmetric \(L\), i.e. infinitesimal rigid
rotations. They do not contribute to the metric at first order.

\[
\boxed{\texttt{E3 = PASS}.}
\]

## 6. Why this does not overturn W12

W12 studied a different microscopic class:

\[
W_g(p)
=
W_0(p)\left(
I-ig\sum_{a,r}z_{ar}J^{(a,r)}(p)
\right)+O(g^2),
\]

with nine Pauli-selective transport controls on a fixed graph.

That class remains

\[
\boxed{
\texttt{UNIVERSAL_SUBFAMILY_DEFICIENT}
}
\]

with

\[
\dim\mathcal U=3,
\qquad
\operatorname{rank}(\delta h|_{\mathcal U})=3/6.
\]

Nothing in the present result modifies that calculation.

The new result instead says that if geometry is represented by **one common
affine deformation of the spatial support itself**, the metric is
species-universal by the common action on physical momentum.

## 7. E4 — mandatory interpretation ceiling

The pass has an important limitation.

The abstract CJWW unitary and all internal hopping matrices were deliberately
left unchanged. Only their common physical embedding was affinely deformed.

Consequently the result is, in the language frozen before calculation,

\[
\boxed{
\texttt{KINEMATIC\_COMMON\_EMBEDDING\_UNIVERSAL}
}
\]

and not yet

\[
\texttt{DYNAMICAL\_ELASTIC\_CJWW\_GEOMETRY}.
\]

For a constant \(\Lambda\), the metric is flat and a global affine coordinate
change can remove it. The result is still useful as a species-universality
test: the four valleys respond to the same spatial geometry. But it does not
show that CJWW transition amplitudes themselves react physically to strain,
nor that an inhomogeneous deformation produces curvature.

Cortijo–Zubkov provide independent precedent for the next physical layer:
elastic deformation of a cubic Weyl tight-binding model modifies hopping
parameters and produces both an anisotropic Fermi velocity/vierbein and an
emergent gauge field. That published mechanism is not silently imported into
CJWW here.

## 8. Consequence under the frozen stop rule

Because E2 passes and E3 has rank six, the terminal state is

\[
\boxed{
\texttt{KINEMATIC\_COMMON\_EMBEDDING\_UNIVERSAL /
ELASTIC\_HOPPING\_RESPONSE\_OPEN}.
}
\]

The W12 contractual prerequisite for considering a physically distinct class
has been satisfied and that class survives its first species-universality
kill test.

However, the gravity programme is **not reopened in full** by this gate.
Before any backreaction/spin-2/constraint work, a separate successor must
freeze a physically motivated **unitary CJWW hopping-response or
dynamical-graph rule** and repeat the four-species metric kill test.

No such successor is authorized or executed by this report.

## 9. Evidence level

\`\`\`
EVIDENCE =
AUTHOR_DERIVATION / EXACT_SYMBOLIC_CERTIFICATE /
INDEPENDENT_REVIEW_PENDING
\`\`\`

No novelty claim is made.
