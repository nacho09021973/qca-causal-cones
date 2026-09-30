# W5_SPATIAL_TETRAD_COMPLETENESS_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W5_SPATIAL_TETRAD_COMPLETENESS_GATE](../theory/W5_SPATIAL_TETRAD_COMPLETENESS_GATE.md), frozen at commit `d6dfad60a887036047fd2e4ded8d984df2b28844`.  
**Certificado exacto:** [verify_w5_spatial_tetrad_rank.py](../scripts/verify_w5_spatial_tetrad_rank.py), added at commit `322a6fe516f96398fc8cea401e125c7da22393ee`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W5_SPATIAL_TETRAD_COMPLETENESS_GATE =
RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN
```

The current three-field W3-W5 construction is a valid restricted
backreacting-metric toy model, but it does not span a generic spatial tetrad
or metric perturbation.

## 1. Tetrad tangent-space rank

The linearized tetrad perturbation is

[
delta E
=
-2g,operatorname{diag}(z_1,z_2,z_3)D,
]

with

[
D=
egin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
end{pmatrix}.
]

The three derivative matrices

[
rac{partialdelta E}{partial z_a}
]

are linearly independent because the rows of (D) are nonzero and occupy
different tetrad rows.

Therefore the map

[
(z_1,z_2,z_3)mapstodelta E
]

has exact rank

[
oxed{3}.
]

A general real (3	imes3) spatial tetrad perturbation has nine components
before any internal-frame redundancy.

[
oxed{	exttt{T1 = RANK 3 OF 9}.}
]

## 2. Metric tangent-space rank

At first order,

[
delta h
=
E_0^Tdelta E+delta E^TE_0.
]

Using the W3 convention,

[
delta h
=
-2g
egin{pmatrix}
2z_1&-z_2&z_3\\
-z_2&-2z_2&z_3\\
z_3&z_3&2z_3
end{pmatrix}.
]

The coefficient matrices of (z_1,z_2,z_3) are linearly independent, so the
map into the six-dimensional space of symmetric (3	imes3) matrices has
exact rank

[
oxed{3}.
]

Hence the current model reaches only a three-dimensional linear subspace of
the six-dimensional spatial-metric tangent space.

[
oxed{	exttt{T2 = RANK 3 OF 6}.}
]

## 3. Gauge-completion escape is not available yet

In canonical/general-relativistic language, a reduction from six spatial
metric components to fewer functions may be legitimate after constraints and
gauge conditions are derived.

That is not the present situation.

The project has not derived:

- spatial diffeomorphism gauge symmetry;
- local Lorentz/frame gauge symmetry;
- Hamiltonian/momentum constraints;
- a gauge condition whose reduced configuration space is exactly the
  three-dimensional W3-W5 image.

Therefore the missing metric directions cannot be reclassified as gauge by
fiat.

[
oxed{	exttt{T3 = GAUGE COMPLETION OPEN}.}
]

## 4. Temporal completion is also absent

The model controls only the spatial Weyl coefficient matrix (E_a{}^i).

No independent dynamical variables or proved gauge conditions supply:

- a lapse/time-leg;
- shift/mixed components;
- a full (3+1) tetrad;
- the corresponding constraint sector.

The fixed discrete update time supplies a preferred foliation, but a preferred
foliation is not a derivation of an admissible GR gauge fixing.

[
oxed{	exttt{T4 = TEMPORAL COMPLETION OPEN}.}
]

## 5. Consequence

The current chain

[
	ext{matter}
leftrightarrow
z_a
ightarrow
E_a{}^i
ightarrow
h^{ij}
]

remains mathematically valid inside its restricted three-field image.

The W3 backreaction, W4 autonomous geometry propagation and W5
tetrad-conjugate source therefore remain useful proof-of-principle results.

What fails is the stronger interpretation that the present three fields form
a generic spatial gravitational configuration.

## 6. Minimal repair indicated by the rank calculation

A natural successor is to replace the three controls (z_a) by nine local
controls

[
z_{ar},qquad a,r=1,2,3,
]

where (r) labels three linearly independent displacement/current directions.

If

[
delta E_a{}^i
=
-2gsum_r z_{ar}D_r{}^i
]

and the (3	imes3) direction matrix (D) is invertible, then for each
tetrad row (a) the three (z_{ar}) span all three spatial directions.

The resulting linear map from nine (z_{ar}) to nine tetrad components is
then potentially full rank.

That extension is not constructed in this report.

## 7. Terminal decision

[
oxed{
	exttt{RESTRICTED\_SPATIAL\_METRIC\_SUBMANIFOLD /
GAUGE\_COMPLETION\_OPEN}
}
]

is the terminal state.

No claim about generic GR geometry follows from W3-W5 without a successor
that resolves this rank and temporal-completion obstruction.
