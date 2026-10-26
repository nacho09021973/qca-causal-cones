# W3_CURVATURE_DYNAMICS_GATE — execution

> **Typographic reconstruction — 2026-10-26.** Backslashes restored by hand.
> No scientific text changed and no evidence level is promoted. The metric
> expansion and curvature witness were checked manually by two formulations
> in `2026-10-26--w3-curvature-dynamics-reconstruction.md`.
> `scripts/verify_w3_backreacting_tetrad.py` checks the related local rotation
> and declared tetrad, not the curvature. The source factorization retains
> the separable/mean-field scope of the later W3 review.

**Fecha:** 2026-09-30.  
**Contrato:** [W3_CURVATURE_DYNAMICS_GATE](../theory/W3_CURVATURE_DYNAMICS_GATE.md), frozen at commit `3373869966836e0e219a80e54ce9ff208e99ad76`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W3_CURVATURE_DYNAMICS_GATE =
COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL

C1 = PASS
C2 = PASS
C3 = FAIL
C4 = FAIL
```

W3 supplies a matter-backreacting tetrad-like microscopic variable and an
induced coarse metric, but it does not yet supply intrinsic geometry dynamics
or a gravitationally appropriate source.

## 1. C1 — coarse metric

The W3 principal symbol is

\[
H(x,p)\sim \sigma^a E_a{}^i(x)p_i,
\]

with

\[
E=E_0-2gZD+O(g^2),
\qquad
E_0=\operatorname{diag}(1,-1,1),
\]

\[
Z=\operatorname{diag}(z_1,z_2,z_3),
\qquad
D=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

Using the Pauli anticommutator, the leading dispersion is

\[
\omega^2=p_i h^{ij}p_j+\cdots,
\qquad
h^{ij}=\sum_a E_a{}^iE_a{}^j.
\]

Therefore

\[
h=E^TE
=
I-2g(E_0^TZD+D^TZE_0)+O(g^2).
\]

Explicitly,

\[
\boxed{
h^{ij}
=
\delta^{ij}
-2g
\begin{pmatrix}
2z_1&-z_2&z_3\\
-z_2&-2z_2&z_3\\
z_3&z_3&2z_3
\end{pmatrix}
+O(g^2).
}
\]

Thus the state of the link/tetrad variables determines an explicit coarse
spatial metric at the principal-symbol level.

\[
\boxed{\texttt{C1 = PASS}.}
\]

## 2. C2 — kinematically nonzero curvature is possible

Let

\[
q^{ij}=h^{ij}-\delta^{ij}.
\]

To first order, the covariant metric perturbation is
\(k_{ij}=-q_{ij}\). The linearized spatial scalar curvature around Euclidean
space is

\[
R^{(1)}
=
\partial_i\partial_j k_{ij}
-
\partial^2 k_i{}^i
=
-\partial_i\partial_j q^{ij}
+
\partial^2 q_i{}^i.
\]

As an explicit witness, set

\[
z_1=f(x_2),\qquad z_2=z_3=0.
\]

Then

\[
q^{11}=-4g f(x_2),
\qquad
q_i{}^i=-4g f(x_2),
\]

and all other \(q^{ij}\) vanish. Hence

\[
\boxed{
R^{(1)}=-4g f''(x_2).
}
\]

For any smooth \(f\) with nonzero second derivative, the induced coarse
spatial metric has nonzero linearized curvature.

This is a kinematic construction only.

\[
\boxed{\texttt{C2 = PASS}.}
\]

## 3. C3 — no autonomous geometry dynamics

The complete W3 geometry-changing gates are

\[
R_e=e^{-igY_e\otimes A_e},
\qquad
T_e=e^{-igZ_e\otimes J_e}.
\]

Every geometry generator is multiplied by a matter operator.

There is no declared term of the form

\[
U_{\rm geom}
\]

acting nontrivially on neighboring geometry/link registers alone, nor a
plaquette, gradient, stiffness or geometry-geometry coupling.

If the relevant matter factors vanish on an edge/region, then

\[
A_e=0,\qquad J_e=0
\]

on that sector and the corresponding W3 geometry update is the identity.

Thus W3 has **backreaction** but no intrinsic geometric kinetic/stiffness
term. A geometric perturbation has no independent vacuum propagation law in
the declared model.

Indirect mediation through later matter motion is not the geometry-only
dynamics required by the frozen gate.

\[
\boxed{\texttt{C3 = FAIL}.}
\]

## 4. C4 — source is not derived stress-energy

The W3 backreaction equation is

\[
z_e'-z_e
=
-2g\,x_e a_e+O(g^2),
\]

where

\[
a_e=\langle A_e\rangle
\]

is endpoint occupation.

The gate explicitly forbids relabeling this as stress-energy.

No derivation shows that \(a_e\), or the combination \(x_ea_e\), is the
appropriate conserved stress-energy component of the continuum Weyl field.
No discrete conservation identity matching a gravitational source equation is
proved.

Therefore:

\[
\boxed{\texttt{C4 = FAIL}.}
\]

## 5. Scientific interpretation

W3 has reached

\[
\text{matter}
\leftrightarrow
\text{backreacting tetrad}
\longrightarrow
\text{coarse metric}
\]

and spatially varying tetrad configurations can be assigned nonzero coarse
curvature.

But it has **not** reached

\[
\text{curvature with its own dynamics}.
\]

The missing ingredient is now precise: a local geometry-geometry unitary
whose long-wavelength limit supplies spatial stiffness/propagation for the
tetrad field, together with a justified matter source.

## 6. Terminal-state decision

C1-C2 pass, C3-C4 fail. By the frozen stop rule,

\[
\boxed{
\texttt{COARSE\_METRIC\_KINEMATICS\_PASS /
CURVATURE\_DYNAMICS\_FAIL}
}
\]

is the terminal state.

No Einstein-Hilbert coefficient or gravitational-normalization gate is
opened by this result.
