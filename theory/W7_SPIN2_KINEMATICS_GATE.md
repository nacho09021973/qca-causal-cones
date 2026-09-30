# W7_SPIN2_KINEMATICS_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W6_FULL_SPATIAL_TETRAD_PASS / SPACETIME_GAUGE_STRUCTURE_OPEN
```

At linear order, define

[
A:=E_0^Tdelta E.
]

Then

[
delta h=A+A^T.
]

## 1. Single question

Does the W6 perturbation space contain the correct **kinematic spin-2 tensor
sector**, and what remains before it can be interpreted as a physical
graviton?

## 2. K1 — irreducible matrix decomposition

Decompose

[
A=Omega+S,
qquad
Omega=rac12(A-A^T),
qquad
S=rac12(A+A^T).
]

Then decompose

[
S=rac{phi}{3}I+Q,
qquad
phi=operatorname{tr}S,
qquad
operatorname{tr}Q=0.
]

Count dimensions.

## 3. K2 — metric visibility

Show

[
delta h=2S
=
rac{2phi}{3}I+2Q
]

and that the antisymmetric (Omega) sector is exactly invisible to the
metric at linear order.

## 4. K3 — global rotation representation

Under a global spatial/internal frame rotation (Rin SO(3)), test the
linearized transformation

[
Qmapsto R Q R^T.
]

Record the symmetric-traceless five-dimensional sector as the standard
spin-2 representation only at the kinematic/global level.

Do not infer local Lorentz gauge symmetry.

## 5. K4 — linearized dynamics closure

If the geometry self-dynamics acts identically and componentwise on all nine
W6 control species, determine whether the linearized subspaces

- antisymmetric frame sector;
- trace scalar;
- symmetric traceless tensor

remain invariant.

## 6. K5 — physical graviton test

A physical 3+1 linearized graviton requires, at minimum, a transverse-traceless
two-polarization sector after constraints/gauge reduction.

Check whether the project has derived:

[
partial_i Q^{ij}=0,
qquad
operatorname{tr}Q=0
]

as dynamical constraints/gauge conditions and whether only two propagating
polarizations remain.

## 7. Terminal states

1. `NO_SPIN2_SECTOR`.
2. `SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN`.
3. `PHYSICAL_LINEARIZED_GRAVITON_PASS`.
4. `OPEN_AFTER_AUDIT`.

## 8. Claim ceiling

A five-component symmetric-traceless tensor sector is not by itself a
graviton. No claim of emergent GR is allowed unless the constraint/gauge and
propagation tests reduce it to the correct physical mode content.
