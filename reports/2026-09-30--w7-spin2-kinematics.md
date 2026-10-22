# W7_SPIN2_KINEMATICS_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W7_SPIN2_KINEMATICS_GATE](../theory/W7_SPIN2_KINEMATICS_GATE.md), frozen at commit `57361ab6f27fb6c08cf38466dfa42906ca296f40`.  
**Certificado exacto:** [verify_w7_spin2_kinematics.py](../scripts/verify_w7_spin2_kinematics.py), added at commit `34d7a5af510ee363fabf4716cf6dc5807bc067fb`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W7_SPIN2_KINEMATICS_GATE =
SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN

PHYSICAL_LINEARIZED_GRAVITON = NOT_ESTABLISHED
```

W6 contains exactly the expected five-component symmetric-traceless tensor
sector at the linearized spatial level. The project has not yet derived the
constraints/gauge structure that would reduce this to the two propagating
polarizations of a physical graviton.

## 1. Exact decomposition of the W6 tetrad perturbation

Define

[
A=E_0^Tdelta E.
]

Every real (3\times3) matrix decomposes uniquely as

[
A=Omega+S,
]

with

[
Omega=\frac12(A-A^T),
qquad
S=\frac12(A+A^T).
]

Then

[
S=\frac{phi}{3}I+Q,
qquad
phi=operatorname{tr}S,
qquad
operatorname{tr}Q=0.
]

The exact dimensions are

[
dimOmega=3,
qquad
dim(phi)=1,
qquad
dim Q=5.
]

Thus

[
9=3+1+5.
]

## 2. Metric visibility

The linearized spatial metric perturbation is

[
delta h=A+A^T=2S.
]

Therefore

[
\boxed{
delta h
=
\frac{2phi}{3}I+2Q.
}
]

The antisymmetric frame sector (Omega) is exactly invisible to
(delta h) at linear order.

This agrees with the three-dimensional kernel already found in W6.

## 3. Spin-2 representation at the kinematic level

Under a global rotation (Rin SO(3)), a spatial rank-two tensor transforms as

[
Qmapsto R Q R^T.
]

The space of real symmetric traceless (3\times3) matrices is
five-dimensional and is the standard spin-2 irreducible representation of
global spatial (SO(3)).

The exact infinitesimal action

[
delta Q=[Omega_R,Q]
]

preserves symmetry and tracelessness.

Therefore W6 contains a genuine **kinematic spin-2 tensor sector** in its
linearized spatial metric variables.

This is a representation-theoretic statement, not yet a local gauge or
particle-content statement.

## 4. Linearized geometry dynamics respects the decomposition

The W4/W6 geometry self-dynamics is applied componentwise and identically to
the geometry control species at the linearized level.

Any scalar linear propagation operator (mathcal K) acting componentwise
commutes with:

- transpose;
- trace;
- symmetric/antisymmetric projection;
- traceless projection.

Therefore the three sectors

[
Omega,qquad
phi,qquad
Q
]

remain closed under the linearized componentwise geometry propagation.

In particular, the five-component (Q) sector is not mixed with the scalar
trace or frame-rotation sector by the declared linearized stiffness update.

## 5. Why this is not yet a graviton

A physical linearized graviton in 3+1 dimensions has two propagating
polarizations after constraints and gauge reduction.

The project has not derived the transverse condition

[
partial_i Q^{ij}=0
]

as a dynamical constraint or gauge choice.

Nor has it derived:

- a local diffeomorphism symmetry;
- Hamiltonian and momentum constraints;
- a local Lorentz/frame gauge symmetry;
- elimination of the scalar trace mode;
- a 3D isotropic smooth gapless propagation law for the (Q) tensor sector.

The W4 spectrum audit established only a 1D sign-staggered repair with a
linear smooth mode. It did not establish an isotropic tensor dispersion

[
omega^2=c_g^2|mathbf k|^2
]

for the five-component (Q) sector.

Thus the reduction

[
5longrightarrow2
]

has not been obtained.

## 6. Scientific status

The current hierarchy is now:

[
\text{generic spatial tetrad}
\rightarrow
\text{generic spatial metric}
\rightarrow
\text{spin-2 kinematic sector}
]

with backreaction, autonomous geometry propagation, and a tetrad-conjugate
matter source available in the broader W4-W6 construction.

What remains missing is the **constraint/gauge structure and tensor
propagation law** that would make the spin-2 sector physical.

## 7. Terminal decision

[
\boxed{
\texttt{SPIN2\_KINEMATIC\_SECTOR\_PASS /
TT\_GAUGE\_CONSTRAINTS\_OPEN}
}
]

is the terminal state.

No emergent-gravity or graviton claim is made beyond this kinematic sector.
