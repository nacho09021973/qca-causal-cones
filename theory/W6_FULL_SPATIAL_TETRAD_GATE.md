# W6_FULL_SPATIAL_TETRAD_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to

```
W5_SPATIAL_TETRAD_COMPLETENESS_GATE =
RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN
```

The obstruction was rank: three controls gave rank 3 in tetrad space and rank
3 in the six-dimensional spatial-metric tangent space.

## 1. Geometry register enlargement

Retain the three linearly independent CJWW support directions

[
d_1=(1,0,0),qquad
d_2=(1,1,0),qquad
d_3=(1,1,1),
]

with direction matrix

[
D=
egin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix},
qquad det D=1.
]

For each Pauli/tetrad row (a=1,2,3) and direction label (r=1,2,3), attach
one geometry qubit with control

[
z_{ar}=langle Z_{ar}angle.
]

## 2. Matter transport operators

For each pair ((a,r)) and edge (e=(x,x+d_r)), define

[
J_e^{(a,r)}
=
i(|x+d_ranglelangle x|-|xanglelangle x+d_r|)
otimessigma_a.
]

Transport gate:

[
T_e^{(a,r)}(g)
=
e^{-ig Z_{ar,e}otimes J_e^{(a,r)}}.
]

Backreaction kick:

[
R_e^{(a,r)}(eta)
=
e^{-ieta Y_{ar,e}otimes J_e^{(a,r)}}.
]

Geometry-only W4 exchange may be applied separately to each ((a,r)) register
species.

## 3. Principal-symbol target

For a translation-invariant semiclassical geometry background, the
momentum-linear correction should be

[
delta E_a{}^i
=
-2gsum_r z_{ar}D_r{}^i.
]

Writing (Z=(z_{ar})),

[
oxed{
E=E_0-2gZD+O(g^2).
}
]

## 4. Obligations

### F1 — exact flat recovery

At (g=eta=0), matter is exactly CJWW Eq. (5.15).

### F2 — full tetrad rank

The linear map

[
Zmapstodelta E=-2gZD
]

must have rank 9.

### F3 — full spatial-metric rank

For

[
delta h=E_0^Tdelta E+delta E^TE_0,
]

the induced linear map from the nine (z_{ar}) to symmetric metric
perturbations must have rank 6.

### F4 — kernel interpretation

Compute the dimension and form of the kernel of
(delta Emapstodelta h).

If it is the expected three-dimensional antisymmetric frame-rotation
direction at linear order, record that only as a **kinematic frame
redundancy**, not a proved gauge symmetry.

### F5 — reciprocal source

For each (z_{ar}), the W5 variational source must be the corresponding
(J^{(a,r)}), and the noncommuting Y-kick must change (z_{ar}) according to
that source.

### F6 — autonomous geometry propagation

The W4 geometry-only exchange construction must apply independently to all
nine register species without changing the flat (g=0) matter walk.

## 5. Terminal states

1. `W6_FULL_SPATIAL_TETRAD_FAIL`.
2. `W6_FULL_SPATIAL_TETRAD_PASS / SPACETIME_GAUGE_STRUCTURE_OPEN`.
3. `OPEN_AFTER_AUDIT`.

## 6. Claim ceiling

A full-rank spatial tetrad is not yet full 3+1 gravity. Passing W6 does not
supply lapse, shift, time-like tetrad components, diffeomorphism constraints,
local Lorentz gauge symmetry, Einstein dynamics, or gravitational
normalization.
