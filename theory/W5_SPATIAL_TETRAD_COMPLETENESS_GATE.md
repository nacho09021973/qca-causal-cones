# W5_SPATIAL_TETRAD_COMPLETENESS_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Current toy geometry after W3-W5 uses three scalar link controls
`z_a(x)`, one for each declared transport family.

The induced principal symbol is

[
H(x,p)sim sigma^a E_a{}^i(z,x)p_i,
]

with

[
E(z)=E_0-2g,mathrm{diag}(z_1,z_2,z_3)D+O(g^2),
]

[
E_0=operatorname{diag}(1,-1,1),
qquad
D=
egin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix}.
]

## 1. Single question

Is the current three-field W3-W5 geometry rich enough to represent a generic
small spatial tetrad/metric perturbation, or only a restricted submanifold?

## 2. T1 — tetrad tangent-space rank

The linearized tetrad perturbation is

[
delta E
=
-2g,mathrm{diag}(z_1,z_2,z_3)D.
]

Compute the dimension of the image of the linear map

[
(z_1,z_2,z_3)mapsto delta E.
]

A generic real spatial tetrad has nine components before internal frame
rotations.

## 3. T2 — metric tangent-space rank

The spatial metric is

[
h=E^TE.
]

At linear order,

[
delta h
=
E_0^Tdelta E+delta E^T E_0.
]

Compute the dimension of the image in the six-dimensional vector space of
symmetric (3	imes3) matrices.

## 4. T3 — gauge-completion escape

A rank-deficient metric image does not by itself exclude a valid gauge-fixed
gravity sector. Such an escape counts only if the project has independently
derived:

- a gauge symmetry identifying the missing directions as redundant; and
- the corresponding constraints/gauge conditions.

Absent that derivation, do not reinterpret missing components as gauge.

## 5. T4 — temporal completion

The current principal symbol supplies only spatial tetrad coefficients
(E_a{}^i). Record whether lapse/time-leg and shift/mixed spacetime tetrad
components have been constructed or justified as a controlled gauge fixing.

## 6. Terminal states

1. `SPATIAL_TETRAD_GENERIC_PASS`.
2. `RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN`.
3. `OPEN_AFTER_AUDIT`.

## 7. Stop rule

If the current model spans only a restricted metric submanifold and no gauge
reduction is proved, stop. A successor may enlarge the geometry register, but
must do so in a separately frozen model.
