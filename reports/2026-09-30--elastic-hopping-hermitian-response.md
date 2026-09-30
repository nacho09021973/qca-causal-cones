# ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE](../theory/ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md), frozen at commit \`1cda245e20acc111a856fa4296f77359be714bd2\`.  
**Certificado simbólico:** [verify_elastic_hopping_hermitian_response.py](../scripts/verify_elastic_hopping_hermitian_response.py), added at commit \`060c481702b81ae8a5008b03c0bb426d40b07921\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE =
HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY

HH0 = PASS
HH1 = PASS
HH2 = PASS
HH3 = PASS
HH4 = PASS
HH5 = PASS, RANK 6/6
HH6 = HOPPING METRIC CONTRIBUTION ZERO
HH7 = RESPECTED
\`\`\`

The orientation-independent Hermitian successor is mathematically consistent
and preserves four-species metric universality. However, its new
strain-dependent hopping generator contributes **no first-order correction to
the principal spatial frame** at any of the four decisive \(+I\) nodes after
the scalar quasienergy phase is removed.

The entire universal rank-six metric response remains the common affine
embedding already established by the predecessor gate.

## 1. Frozen response

The exact flat walk is

\[
W_0(p)=\sum_{h\in F}e^{ip\cdot h}W_h
\]

on the certified 14-vector support \(F\).

For symmetric strain \(u\),

\[
\rho_h(u)=\frac{h^Tuh}{h^Th}
\]

satisfies

\[
\rho_{-h}=\rho_h.
\]

The full-support bond-weighted symbol is

\[
R_u(p)
=
\sum_{h\in F}
\rho_h(u)e^{ip\cdot h}W_h,
\]

and the generator is

\[
\boxed{
K_u(p)=\frac12\left(R_u(p)+R_u(p)^\dagger\right).
}
\]

The exact unitary family is

\[
W_{\varepsilon,u}(q)
=
e^{-i\varepsilon K_u(p)}W_0(p),
\qquad
p=a(I+\varepsilon u)^Tq.
\]

## 2. HH0–HH2 — consistency

The full 14-vector support is used directly; no orientation set \(F_+\)
appears.

Because \(\rho_{-h}=\rho_h\) and the Hermitian part is taken only after the
full directed sum,

\[
K_u(p)^\dagger=K_u(p)
\]

identically.

Thus for real \(\varepsilon\),

\[
e^{-i\varepsilon K_u(p)}
\]

is unitary, and multiplying the exact unitary CJWW symbol preserves exact
unitarity.

At \(\varepsilon=0\),

\[
W_{\varepsilon,u}(q)=W_0(aq).
\]

Therefore

\[
\boxed{\texttt{HH0,HH1,HH2 = PASS}.}
\]

## 3. HH3 — node/gauge decomposition

At every decisive \(+I\) node

\[
p_*\in
\{(0,0,0),(\pi,\pi,0),(\pi,0,\pi),(0,\pi,\pi)\},
\]

the exact first-order generator evaluates to

\[
\boxed{
K_u(p_*)
=
\frac{\operatorname{tr}u}{3}I.
}
\]

Its traceless Pauli part vanishes:

\[
\operatorname{tr}\!\left[K_u(p_*)\sigma_a\right]=0.
\]

Therefore the new hopping generator produces no first-order node displacement,

\[
\boxed{\delta q_*=0},
\]

and no axial/vector gauge shift at the node.

The only constant effect is the common scalar quasienergy phase

\[
\alpha_*=\frac{\operatorname{tr}u}{3}.
\]

After factoring

\[
e^{-i\varepsilon\alpha_*},
\]

there is no remaining constant term.

Hence

\[
\boxed{\texttt{HH3 = PASS}.}
\]

## 4. Hopping contribution to the principal frame

Write, to first order,

\[
e^{-i\varepsilon K_u(p)}W_0(p)
=
W_0(p)
-
i\varepsilon K_u(p)W_0(p)
+
O(\varepsilon^2).
\]

After removing the scalar phase at \(p_*\), differentiate with respect to
species momentum.

The exact Pauli projection gives, at every decisive node,

\[
\boxed{
\delta E_*^{\rm hop}=0.
}
\]

The identity-linear/tilt term also vanishes at this order.

Thus the orientation-independent Hermitian hopping response does not modify
the Weyl principal spatial frame to \(O(\varepsilon k)\).

This is stronger than metric universality: the new hopping term supplies no
metric perturbation at all at the retained order.

## 5. HH4 — four-species metric universality

The common physical embedding contributes

\[
p=a(I+\varepsilon u)^Tq.
\]

For each flat species frame \(E_*\),

\[
E_*^TE_*=I.
\]

Since the hopping correction vanishes,

\[
E_*^{(\varepsilon,u)}
=
aE_*(I+\varepsilon u)
+
O(\varepsilon^2).
\]

Therefore

\[
h_*=
(E_*^{(\varepsilon,u)})^TE_*^{(\varepsilon,u)}
\]

gives

\[
\frac{h_*}{a^2}
=
I+2\varepsilon u+O(\varepsilon^2)
\]

at every one of the four \(+I\) nodes.

Hence

\[
\boxed{
\delta h_{*1}
=
\delta h_{*2}
=
\delta h_{*3}
=
\delta h_{*4}
=
2a^2u.
}
\]

Thus

\[
\boxed{\texttt{HH4 = PASS}.}
\]

## 6. HH5 — metric rank

The map

\[
u\mapsto\delta h=2a^2u
\]

is an isomorphism on \(\mathrm{Sym}(3)\).

Therefore

\[
\boxed{
\operatorname{rank}=6/6.
}
\]

Hence

\[
\boxed{\texttt{HH5 = PASS}.}
\]

## 7. HH6 — decomposition of the response

The universal response splits as

\[
\delta h
=
\delta h^{\rm embedding}
+
\delta h^{\rm hopping}.
\]

The exact calculation gives

\[
\boxed{
\delta h^{\rm embedding}=2a^2u,
}
\]

and

\[
\boxed{
\delta h^{\rm hopping}=0
}
\]

to the frozen first order.

Therefore the positive universality/rank result contains **no new nontrivial
elastic metric response of the CJWW hopping matrices**.

The Hermitian symmetrization repairs the predecessor's orientation ambiguity,
but at this order it also removes the desired principal-symbol response.

According to the predeclared terminal-state ordering, the correct state is

\[
\boxed{
\texttt{HERMITIAN\_ELASTIC\_METRIC\_UNIVERSAL\_EMBEDDING\_ONLY}.
}
\]

It is not
\`HERMITIAN_ELASTIC_METRIC_UNIVERSAL_NONTRIVIAL\`.

## 8. Interpretation

Three facts are now separated.

### A. W6 Pauli-selective controls

Remain negative:

\[
\texttt{UNIVERSAL_SUBFAMILY_DEFICIENT}.
\]

### B. Common affine graph embedding

Remains positive:

\[
h_*^{(\Lambda)}
=
a^2\Lambda\Lambda^T
\]

for all four species, with rank \(6/6\).

### C. First orientation-independent unitary strain response

Is well-defined and species-universal, but contributes only a common scalar
phase at the nodes and zero principal-frame correction at first order.

Thus the project has **not yet constructed a physical elastic renormalization
of the CJWW hopping dynamics that produces a nontrivial universal metric**.

## 9. Stop rule

The frozen contract requires stopping at the first applicable terminal state.

Therefore no alternative Hermitian prescription, gate ordering, coefficient,
bond functional, strain subset or internal rotation is tried here.

No W3–W11 gravity machinery is reopened.

A further response family would require a new independent physical
justification and a separately frozen contract; it may not be selected merely
because the present Hermitian prescription has zero metric response.

## 10. Evidence

\`\`\`
EVIDENCE =
EXACT SYMBOLIC FIRST-ORDER DERIVATION /
AUTHOR-SIDE CERTIFICATE /
INDEPENDENT REVIEW PENDING
\`\`\`

No novelty, gravity or nature claim is made.
