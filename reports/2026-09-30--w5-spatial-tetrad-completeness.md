# W5_SPATIAL_TETRAD_COMPLETENESS_GATE — execution

> **Typographic reconstruction — 2026-10-26.** Backslashes restored by hand
> against `scripts/verify_w5_spatial_tetrad_rank.py`. No scientific text changed.
> The ranks are generic symbolic ranks, valid for g nonzero; both are zero
> at g=0. Independent-entry and image-relation checks are recorded in
> `2026-10-26--w5-spatial-tetrad-reconstruction.md`. This is a first-order
> three-control result, not a gauge construction or an independent review.
> The later W3 mean-field and W4 spectrum qualifications remain applicable
> to the historical proof-of-principle language below.

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

\[
\delta E
=
-2g\,\operatorname{diag}(z_1,z_2,z_3)D,
\]

with

\[
D=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

The three derivative matrices

\[
\frac{\partial\delta E}{\partial z_a}
\]

are linearly independent because the rows of \(D\) are nonzero and occupy
different tetrad rows.

Therefore the map

\[
(z_1,z_2,z_3)\mapsto\delta E
\]

has exact rank

\[
\boxed{3}.
\]

A general real \(3\times3\) spatial tetrad perturbation has nine components
before any internal-frame redundancy.

\[
\boxed{\texttt{T1 = RANK 3 OF 9}.}
\]

## 2. Metric tangent-space rank

At first order,

\[
\delta h
=
E_0^T\delta E+\delta E^TE_0.
\]

Using the W3 convention,

\[
\delta h
=
-2g
\begin{pmatrix}
2z_1&-z_2&z_3\\
-z_2&-2z_2&z_3\\
z_3&z_3&2z_3
\end{pmatrix}.
\]

The coefficient matrices of \(z_1,z_2,z_3\) are linearly independent, so the
map into the six-dimensional space of symmetric \(3\times3\) matrices has
exact rank

\[
\boxed{3}.
\]

Hence the current model reaches only a three-dimensional linear subspace of
the six-dimensional spatial-metric tangent space.

\[
\boxed{\texttt{T2 = RANK 3 OF 6}.}
\]

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

\[
\boxed{\texttt{T3 = GAUGE COMPLETION OPEN}.}
\]

## 4. Temporal completion is also absent

The model controls only the spatial Weyl coefficient matrix \(E_a{}^i\).

No independent dynamical variables or proved gauge conditions supply:

- a lapse/time-leg;
- shift/mixed components;
- a full \(3+1\) tetrad;
- the corresponding constraint sector.

The fixed discrete update time supplies a preferred foliation, but a preferred
foliation is not a derivation of an admissible GR gauge fixing.

\[
\boxed{\texttt{T4 = TEMPORAL COMPLETION OPEN}.}
\]

## 5. Consequence

The current chain

\[
\text{matter}
\leftrightarrow
z_a
\rightarrow
E_a{}^i
\rightarrow
h^{ij}
\]

remains mathematically valid inside its restricted three-field image.

The W3 backreaction, W4 autonomous geometry propagation and W5
tetrad-conjugate source therefore remain useful proof-of-principle results.

What fails is the stronger interpretation that the present three fields form
a generic spatial gravitational configuration.

## 6. Minimal repair indicated by the rank calculation

A natural successor is to replace the three controls \(z_a\) by nine local
controls

\[
z_{ar},\qquad a,r=1,2,3,
\]

where \(r\) labels three linearly independent displacement/current directions.

If

\[
\delta E_a{}^i
=
-2g\sum_r z_{ar}D_r{}^i
\]

and the \(3\times3\) direction matrix \(D\) is invertible, then for each
tetrad row \(a\) the three \(z_{ar}\) span all three spatial directions.

The resulting linear map from nine \(z_{ar}\) to nine tetrad components is
then potentially full rank.

That extension is not constructed in this report.

## 7. Terminal decision

\[
\boxed{
\texttt{RESTRICTED\_SPATIAL\_METRIC\_SUBMANIFOLD /
GAUGE\_COMPLETION\_OPEN}
}
\]

is the terminal state.

No claim about generic GR geometry follows from W3-W5 without a successor
that resolves this rank and temporal-completion obstruction.
