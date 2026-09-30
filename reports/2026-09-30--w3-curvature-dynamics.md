# W3_CURVATURE_DYNAMICS_GATE — execution

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

[
H(x,p)sim sigma^a E_a{}^i(x)p_i,
]

with

[
E=E_0-2gZD+O(g^2),
qquad
E_0=operatorname{diag}(1,-1,1),
]

[
Z=operatorname{diag}(z_1,z_2,z_3),
qquad
D=
egin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix}.
]

Using the Pauli anticommutator, the leading dispersion is

[
omega^2=p_i h^{ij}p_j+cdots,
qquad
h^{ij}=sum_a E_a{}^iE_a{}^j.
]

Therefore

[
h=E^TE
=
I-2g(E_0^TZD+D^TZE_0)+O(g^2).
]

Explicitly,

[
oxed{
h^{ij}
=
delta^{ij}
-2g
egin{pmatrix}
2z_1&-z_2&z_3\\
-z_2&-2z_2&z_3\\
z_3&z_3&2z_3
end{pmatrix}
+O(g^2).
}
]

Thus the state of the link/tetrad variables determines an explicit coarse
spatial metric at the principal-symbol level.

[
oxed{	exttt{C1 = PASS}.}
]

## 2. C2 — kinematically nonzero curvature is possible

Let

[
q^{ij}=h^{ij}-delta^{ij}.
]

To first order, the covariant metric perturbation is
(k_{ij}=-q_{ij}). The linearized spatial scalar curvature around Euclidean
space is

[
R^{(1)}
=
partial_ipartial_j k_{ij}
-
partial^2 k_i{}^i
=
-partial_ipartial_j q^{ij}
+
partial^2 q_i{}^i.
]

As an explicit witness, set

[
z_1=f(x_2),qquad z_2=z_3=0.
]

Then

[
q^{11}=-4g f(x_2),
qquad
q_i{}^i=-4g f(x_2),
]

and all other (q^{ij}) vanish. Hence

[
oxed{
R^{(1)}=-4g f''(x_2).
}
]

For any smooth (f) with nonzero second derivative, the induced coarse
spatial metric has nonzero linearized curvature.

This is a kinematic construction only.

[
oxed{	exttt{C2 = PASS}.}
]

## 3. C3 — no autonomous geometry dynamics

The complete W3 geometry-changing gates are

[
R_e=e^{-igY_eotimes A_e},
qquad
T_e=e^{-igZ_eotimes J_e}.
]

Every geometry generator is multiplied by a matter operator.

There is no declared term of the form

[
U_{m geom}
]

acting nontrivially on neighboring geometry/link registers alone, nor a
plaquette, gradient, stiffness or geometry-geometry coupling.

If the relevant matter factors vanish on an edge/region, then

[
A_e=0,qquad J_e=0
]

on that sector and the corresponding W3 geometry update is the identity.

Thus W3 has **backreaction** but no intrinsic geometric kinetic/stiffness
term. A geometric perturbation has no independent vacuum propagation law in
the declared model.

Indirect mediation through later matter motion is not the geometry-only
dynamics required by the frozen gate.

[
oxed{	exttt{C3 = FAIL}.}
]

## 4. C4 — source is not derived stress-energy

The W3 backreaction equation is

[
z_e'-z_e
=
-2g,x_e a_e+O(g^2),
]

where

[
a_e=langle A_eangle
]

is endpoint occupation.

The gate explicitly forbids relabeling this as stress-energy.

No derivation shows that (a_e), or the combination (x_ea_e), is the
appropriate conserved stress-energy component of the continuum Weyl field.
No discrete conservation identity matching a gravitational source equation is
proved.

Therefore:

[
oxed{	exttt{C4 = FAIL}.}
]

## 5. Scientific interpretation

W3 has reached

[
	ext{matter}
leftrightarrow
	ext{backreacting tetrad}
longrightarrow
	ext{coarse metric}
]

and spatially varying tetrad configurations can be assigned nonzero coarse
curvature.

But it has **not** reached

[
	ext{curvature with its own dynamics}.
]

The missing ingredient is now precise: a local geometry-geometry unitary
whose long-wavelength limit supplies spatial stiffness/propagation for the
tetrad field, together with a justified matter source.

## 6. Terminal-state decision

C1-C2 pass, C3-C4 fail. By the frozen stop rule,

[
oxed{
	exttt{COARSE\_METRIC\_KINEMATICS\_PASS /
CURVATURE\_DYNAMICS\_FAIL}
}
]

is the terminal state.

No Einstein-Hilbert coefficient or gravitational-normalization gate is
opened by this result.
