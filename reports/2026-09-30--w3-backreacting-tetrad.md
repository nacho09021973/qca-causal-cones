# W3_BACKREACTING_TETRAD_FLOQUET_GATE — execution

> **Typographic reconstruction — 2026-10-22.** The text recorded on 2026-09-30
> (commit `ebf9142`) lost its LaTeX backslashes through an escape layer
> (`reports/2026-10-22--escape-corruption-audit.md`). The delimiters and commands
> have been restored by hand. `scripts/check_reconstruction.py` certifies that
> only backslashes were added. The formulas were checked against
> `scripts/verify_w3_backreacting_tetrad.py`, which passes. No result or scope
> statement has changed.

**Fecha:** 2026-09-30.  
**Contrato:** [W3_BACKREACTING_TETRAD_FLOQUET_GATE](../theory/W3_BACKREACTING_TETRAD_FLOQUET_GATE.md), frozen at commit `5dc5fda054355f1b1db3bbc7e6c91e8e841273f4`.  
**Certificado simbólico:** [verify_w3_backreacting_tetrad.py](../scripts/verify_w3_backreacting_tetrad.py), added at commit `f1f54c973f05e610c309e4f5f3925cb3fafce953`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W3_BACKREACTING_TETRAD_FLOQUET_GATE =
W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN

FULL_QCGD_SYNTHESIS = OPEN
EINSTEIN_DYNAMICS = NOT_CLAIMED
GRAVITATIONAL_NORMALIZATION_G1 = NOT_OPENED
```

W3 repairs the exact conservation defect found in W2 by separating the
geometry operator that controls transport from a noncommuting geometry
operator that receives the matter kick.

## 1. Exact local substeps

For edge \(e=(x,x+d_a)\),

\[
J_e^{(a)}
=
i(|x+d_a\rangle\langle x|-|x\rangle\langle x+d_a|)
\otimes\sigma_a
\]

and

\[
A_e=(|x\rangle\langle x|+|x+d_a\rangle\langle x+d_a|)
\otimes I_2.
\]

The two local gates are

\[
R_e(g)=e^{-igY_e\otimes A_e},
\qquad
T_e(g)=e^{-igZ_e\otimes J_e^{(a)}}.
\]

Both generators are Hermitian, hence both gates are exactly unitary for every
real \(g\).

The complete interaction uses the same three direction families and parity
matchings as W2. Executing all kick layers and transport layers requires at
most twelve disjoint-edge layers, independent of volume.

At \(g=0\),

\[
R_e(0)=T_e(0)=I,
\]

so

\[
\boxed{
U_{g=0}=I_g\otimes U_{\rm CJWW}.
}
\]

Thus W3.1 and W3.2 pass for the added interaction.

## 2. Tetrad control by Z

The transport substep depends on \(Z_e\).

For a slowly varying/separable edge background with family means

\[
z_a=\langle Z_e\rangle,
\]

the W2 current-symbol calculation transfers directly:

\[
E(z)
=
E_0
-
2g\,\operatorname{diag}(z_1,z_2,z_3)D
+
O(g^2),
\]

with

\[
E_0=\operatorname{diag}(1,-1,1),
\qquad
D=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

Since \(\det D=1\), the \(Z\)-field changes the momentum-linear Weyl
principal symbol and local characteristic cone.

\[
\boxed{\texttt{W3.3 = PASS}.}
\]

## 3. Matter changes the actual tetrad-control observable

The backreaction kick uses \(Y_e\), which does not commute with \(Z_e\).

Because \(A_e^2=A_e\), the Heisenberg evolution of \(Z_e\) is exact:

\[
R_e^\dagger(Z_e\otimes I)R_e
=
Z_e\otimes(I-A_e)
+
\left(
Z_e\cos2g-X_e\sin2g
\right)\otimes A_e.
\]

For an initially uncorrelated edge/matter state, define

\[
x_e=\langle X_e\rangle,\qquad
z_e=\langle Z_e\rangle,\qquad
a_e=\langle A_e\rangle.
\]

Then

\[
\boxed{
z_e'
=
z_e+
a_e\left[
(\cos2g-1)z_e-\sin2g\,x_e
\right].
}
\]

Hence

\[
\boxed{
z_e'-z_e
=
-2g\,x_e a_e+O(g^2).
}
\]

With the frozen reference geometry Bloch vector

\[
(x_0,y_0,z_0)=(\sin\theta,0,\cos\theta),
\qquad0<\theta<\pi/2,
\]

both \(x_0\) and \(z_0\) are nonzero.

Different matter endpoint occupations \(a_e\) therefore produce different
first-order changes in the same \(z_e\) that controls transport.

The subsequent transport gate commutes with \(Z_e\), so it does not undo this
change.

\[
\boxed{\texttt{W3.4 = PASS}.}
\]

## 4. Explicit matter-to-tetrad backreaction

Insert the updated \(z_a'\) into the principal-symbol coefficient:

\[
E(z')
=
E_0-2g\,\operatorname{diag}(z_1',z_2',z_3')D+O(g^2).
\]

Using

\[
\delta z_a=-2g\,x_a a_a+O(g^2),
\]

the matter-dependent contribution to the next transport coefficient is

\[
\boxed{
\delta E_{\rm back}
=
4g^2
\operatorname{diag}(x_1a_1,x_2a_2,x_3a_3)D
+
O(g^3).
}
\]

Thus the matter state changes the local Weyl tetrad/principal symbol.

The ordering is physically transparent:

\[
\text{matter density}
\overset{R}{\longrightarrow}
z_e
\overset{T}{\longrightarrow}
E_a{}^i
\overset{}{\longrightarrow}
\text{matter cone}.
\]

This is the reciprocal closure that W2 lacked.

\[
\boxed{\texttt{W3.5 = PASS}.}
\]

## 5. Perturbative orders

For the declared reference background:

- baseline geometry-controlled cone deformation is \(O(g z_0)\);
- matter changes the geometric control \(z_e\) at \(O(g)\);
- matter-induced change of the principal symbol is \(O(g^2)\).

There is no contradiction with the earlier exact-channel no-go: at nonzero
coupling the reduced matter evolution is not required to remain exactly
CJWW.

## 6. What W3 establishes

Within the declared one-particle causal-unitary model,

\[
\boxed{
\text{matter}
\longrightarrow
\text{local link control }z_e
\longrightarrow
\text{Weyl tetrad }E_a{}^i
\longrightarrow
\text{local characteristic cone}
}
\]

and the reverse influence is present because the cone controls subsequent
matter propagation.

This is the first gate in the project where the **same coarse variable that
controls the principal symbol is explicitly changed by matter**.

It is therefore legitimate, within this restricted construction, to call
\(z_e\) a **backreacting tetrad-like microscopic variable**.

## 7. Mandatory limitations

W3 is still a toy dynamical-geometry model, not emergent general relativity.

In particular:

- the backreaction source \(a_e\) is endpoint occupation, not a derived
  stress-energy tensor;
- no continuum coarse field \(e_a{}^i(x,t)\) has yet been rigorously derived;
- no connection, torsion or curvature tensor has been constructed;
- no local Lorentz or diffeomorphism gauge symmetry is established;
- no Einstein-Hilbert action or Einstein equation is derived;
- no \(G_{\rm eff}\), cosmological constant, AdS radius or absolute scale is
  determined;
- full QCGD finite-depth synthesis of the frozen CJWW baseline remains OPEN.

## 8. Relation to prior art

Quantum-walk literature already establishes that local-unitary fields can
encode curved-spacetime Dirac principal symbols. The present project does not
claim novelty for that fact.

The additional internal question answered here is narrower: can a microscopic
link degree both control the Weyl principal symbol and be changed by the
matter sector in one local unitary Floquet construction? W3 supplies an
explicit perturbative yes within its toy-model scope.

No novelty claim is made pending dedicated prior-art review.

## 9. Terminal-state decision

All frozen W3.1-W3.5 obligations pass. Therefore

\[
\boxed{
\texttt{W3\_BACKREACTING\_TETRAD\_PASS /
CURVATURE\_DYNAMICS\_OPEN}
}
\]

is the terminal state.

The next admissible layer is to define and test a coarse geometric field and
a curvature/dynamics observable. Gravitational-normalization G1 remains
closed until that separate gate passes.
