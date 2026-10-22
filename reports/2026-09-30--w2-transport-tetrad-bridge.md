# W2_TRANSPORT_TETRAD_BRIDGE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W2_TRANSPORT_TETRAD_BRIDGE_GATE](../theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md), frozen at commit `384c0032967fd1164206ca6bed7319db6a84e8e1`.  
**Certificado simbólico:** [verify_w2_transport_tetrad.py](../scripts/verify_w2_transport_tetrad.py), added at commit `6f81a52588cfbd63e76f2a93b666f7ad8119bf4f`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W2_TRANSPORT_TETRAD_BRIDGE_GATE =
W2_DYNAMIC_PRINCIPAL_SYMBOL_PASS / CURVATURE_OPEN

FULL_QCGD_SYNTHESIS = OPEN
EINSTEIN_DYNAMICS = NOT_CLAIMED
GRAVITATIONAL_NORMALIZATION_G1 = NOT_OPENED
```

W2 constructs a reciprocal local matter/link interaction whose semiclassical
link background changes the momentum-linear Weyl principal symbol. This
crosses the obstruction that stopped W1, where the link field generated only
a scalar potential/dephasing term.

## 1. Exact flat baseline

For CJWW Eq. (5.15),

[
W_0(p)=
\begin{pmatrix}
c_1c_2e^{ip_3}&-c_1s_2+i s_1\\
c_1s_2+i s_1&c_1c_2e^{-ip_3}
end{pmatrix}.
]

Direct differentiation at (p=0) gives

[
partial_{p_1}W_0(0)=isigma_1,qquad
partial_{p_2}W_0(0)=-isigma_2,qquad
partial_{p_3}W_0(0)=isigma_3.
]

Hence

[
W_0(p)
=
I+i,sigma^a E_{0,a}{}^i p_i+O(|p|^2),
]

with

[
E_0=
\begin{pmatrix}
1&0&0\\
0&-1&0\\
0&0&1
end{pmatrix}.
]

This is the convention used below. Interpreting (W=e^{-iH}) flips the
overall Hamiltonian-tetrad sign but not any conclusion about deformation.

## 2. Local transport gate

Choose the three certified support directions

[
d_1=(1,0,0),qquad
d_2=(1,1,0),qquad
d_3=(1,1,1).
]

For (e=(x,x+d_a)),

[
J_e^{(a)}
=
i(|x+d_a\ranglelangle x|-|x\ranglelangle x+d_a|)
otimessigma_a.
]

The spatial factor is Hermitian, as is (sigma_a); therefore
(J_e^{(a)}) is Hermitian.

With geometry/link operator

[
B_e=Z_e+X_e,
]

define

[
V_e^{(a)}(g)
=
e^{-ig B_eotimes J_e^{(a)}}.
]

This is exactly unitary for every real (g).

For a fixed (d_a), the parity split of the starting (x_1) gives two
matchings because ((d_a)_1=1). Three direction families therefore require
at most six disjoint-edge layers.

Thus the added interaction is finite-depth and bounded-range independently
of volume.

## 3. W2.1 and W2.2

At (g=0),

[
V_e^{(a)}(0)=I
]

for every edge, so

[
\boxed{
U_{g=0}=I_gotimes U_{\rm CJWW}.
}
]

The added gates act only on one link register and its two matter endpoints,
and can be layered at depth at most six.

Therefore:

```
W2.1 = PASS
W2.2 = PASS for the added interaction
```

No exact finite-depth factorization of the complete CJWW step is supplied by
this gate, so `FULL_QCGD_SYNTHESIS` remains OPEN.

## 4. W2.3 — matter-to-link backreaction

Let an edge start in

[
eta_e=|0\ranglelangle0|.
]

For a matter state (sigma), to first order,

[
\rho_e(g)
=
eta_e
-ig,j_e[B_e,eta_e]
+O(g^2),
]

where

[
j_e=operatorname{tr}(J_e^{(a)}sigma).
]

Because

[
[Z_e,eta_e]=0,qquad
[X_e,eta_e]
e0,
]

the edge-state derivative is proportional to the **matter current**
(j_e).

This response is explicitly nontrivial. Let (|s_a^+\rangle) be the
(+1) eigenvector of (sigma_a), and on the two endpoint positions take

[
|psi_pm\rangle
=
\frac{|x\ranglepm i|x+d_a\rangle}{sqrt2}
otimes|s_a^+\rangle.
]

Then

[
langlepsi_pm|J_e^{(a)}|psi_pm\rangle=pm1.
]

The same initial link state therefore acquires opposite first-order responses
for the two matter currents.

[
\boxed{\texttt{W2.3 = PASS}.}
]

## 5. W2.4 — link-to-matter transport response

For an initial link state (eta_e), tracing the link at first order gives
the matter generator

[
b_e J_e^{(a)},
qquad
b_e=operatorname{tr}(eta_e B_e).
]

For example,

[
langle0|B_e|0\rangle=+1,qquad
langle1|B_e|1\rangle=-1.
]

Thus two link backgrounds differing only by the local edge state induce
opposite first-order hopping/current terms.

This is a transport modification, not an on-site scalar potential.

[
\boxed{\texttt{W2.4 = PASS}.}
]

## 6. W2.5 — exact current symbol and tetrad deformation

For one uniform oriented displacement family (d),

[
sum_x
i(|x+d\ranglelangle x|-|x\ranglelangle x+d|)
]

has Fourier symbol

[
i(e^{-ipcdot d}-e^{ipcdot d})
=
2sin(pcdot d).
]

Therefore a translation-invariant semiclassical link background with family
means (b_a) contributes

[
2b_asin(pcdot d_a)sigma_a
]

to the interaction generator.

To first order in (g),

[
V_g(p)
=
I-i,2gsum_a
b_asin(pcdot d_a)sigma_a+O(g^2).
]

Multiplying the flat CJWW symbol and retaining the terms linear in momentum
and first order in (g),

[
W_g(p)
=
I+i,sigma^a E_a{}^i(g)p_i
+
O(|p|^2,g^2|p|),
]

where

[
\boxed{
E(g)
=
E_0
-
2g,operatorname{diag}(b_1,b_2,b_3)D
}
]

and

[
D=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix},
qquad
det D=1.
]

Explicitly,

[
E(g)=
\begin{pmatrix}
1-2gb_1&0&0\\
-2gb_2&-1-2gb_2&0\\
-2gb_3&-2gb_3&1-2gb_3
end{pmatrix}.
]

This is a genuine momentum-linear principal-symbol deformation.

As a minimal control, set (b_2=b_3=0). Then

[
E(g)=operatorname{diag}(1-2gb_1,-1,1),
]

so the leading Weyl dispersion has

[
omega^2
=
(1-2gb_1)^2p_1^2+p_2^2+p_3^2+cdots.
]

The local characteristic speed in the first direction changes at order (g).

Thus the link background changes the local effective cone rather than merely
adding a quasienergy shift.

[
\boxed{\texttt{W2.5 = PASS}.}
]

Because (det E(0)=-1), the tetrad remains nondegenerate for sufficiently
small (g).

## 7. W2.6 — same coupling supplies backreaction and tetrad response

Sections 4 and 6 use the same operator

[
B_eotimes J_e^{(a)}.
]

Its geometry expectation (b_e) changes matter transport, while its matter
expectation (j_e) changes the geometry/link state.

Therefore reciprocal coupling and principal-symbol deformation are not two
unrelated mechanisms added after the fact.

[
\boxed{\texttt{W2.6 = PASS}.}
]

## 8. What has been achieved

At the declared one-particle causal-unitary level, W2 gives

[
\boxed{
\text{CJWW at }g=0
;longrightarrow;
\text{dynamical link variables}
;longleftrightarrow;
\text{matter currents}
;longrightarrow;
E_a{}^i(G)
}
]

with an explicit geometry-state-dependent Weyl principal symbol.

This is stronger than W1:

- W1 changed finite-time interference support but left the principal symbol
  fixed;
- W2 changes the leading propagation cone itself.

In the limited language of the present gate, the link variables are therefore
**tetrad-like dynamical variables**.

## 9. What is still missing

The result is not yet emergent general relativity.

Missing:

1. a coarse field variable (e_a{}^i(x,t)) defined beyond a prescribed
   product/semi-classical link background;
2. its autonomous long-wavelength equation of motion;
3. a curvature observable/action built from that field;
4. gauge redundancy/local Lorentz or diffeomorphism structure;
5. an Einstein-Hilbert coefficient or (G_{\rm eff});
6. an independently generated curvature scale;
7. a proof that the complete CJWW+link evolution is a QCGD finite-depth
   circuit, rather than the present causal-unitary construction plus a
   finite-depth interaction.

The result also carries **no novelty claim**. Position-dependent local
unitaries producing curved-spacetime Dirac principal symbols are established
prior art in quantum-walk literature. The new project question, if any, is
whether the same microscopic variables can both acquire matter-dependent
dynamics and generate a controlled gravitational continuum equation.

## 10. Terminal-state decision

All W2.1-W2.6 obligations pass at the declared level. Therefore

[
\boxed{
\texttt{W2\_DYNAMIC\_PRINCIPAL\_SYMBOL\_PASS /
CURVATURE\_OPEN}
}
]

is the terminal state.

By the stop rule, no Einstein or gravitational-normalization calculation is
opened here.
