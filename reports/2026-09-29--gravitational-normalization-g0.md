# GRAVITATIONAL_NORMALIZATION_GATE — G0 execution

> **Typographic reconstruction — 2026-10-26.** Display delimiters restored
> by hand against the frozen operator contract. No scientific text changed.
> G0 failure concerns the prescribed-background H1 model of this record;
> the historical source descriptions were not independently rechecked here.

**Fecha:** 2026-09-29.  
**Contrato:** [GRAVITATIONAL_NORMALIZATION_GATE](../theory/GRAVITATIONAL_NORMALIZATION_GATE.md), frozen at commit `2680d799210731ab2815533e0b9ca9918f15d397`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
GRAVITATIONAL_NORMALIZATION_GATE = BLOCKED_NO_DYNAMICAL_GEOMETRY
G0 = FAIL
G1 = NOT_EXECUTED
G2 = NOT_EXECUTED
G3 = NOT_EXECUTED
```

This is a structural result about the **currently frozen** inhomogeneous/QCA
construction. It is not a no-go theorem for all QCA gravity models.

## 1. Frozen operator actually present in the repository

The inhomogeneous H1 reconstruction fixes

\[
D(z)=S(z)\oplus S(z)^{-1},
\qquad
C_N(X)=\exp[-i\vartheta(X)\beta/N],
\qquad
A_N(X,z)=C_N(X)D(z).
\]

The same front treats `vartheta` as a bounded prescribed profile and studies
how the already-defined matter propagator changes under this inhomogeneous
on-site coin. The E roadmap asks whether the flat corona asymptotics are stable
under that deformation.

There is no additional microscopic Hilbert-space factor or classical state
variable denoted by `g`, `vartheta`, a tetrad, lapse, link geometry, or an
equivalent geometric degree of freedom whose state is updated together with
the matter field.

## 2. G0.1 — geometric degree of freedom in the state/update algebra

**FAIL.**

`vartheta(X)` appears as a coefficient in the externally specified operator
`C_N(X)`. The frozen contract does not promote it to a state variable,
operator-valued field, register, link degree of freedom, or dynamical sector.

A position-dependent coin can encode propagation on a prescribed effective
background. That is not yet a dynamical geometry.

## 3. G0.2 — evolution equation for geometry

**FAIL.**

The update evolves the matter/spinor state through `A_N(X,z)`. No update map

\[
g_t\mapsto g_{t+1}
\]

or

\[
\vartheta_t\mapsto\vartheta_{t+1}
\]

is part of the frozen construction.

The existing H1/H1c machinery studies spectral stability, Riesz projectors,
P/Q transfer and endpoint control for a fixed inhomogeneous profile. None of
those steps supplies a geometry evolution equation.

## 4. G0.3 — backreaction

**FAIL.**

Because no geometric variable is evolved, the frozen model contains no map in
which the matter/information state changes the subsequent geometric profile.
There is therefore no microscopic backreaction channel of the form

\[
\text{matter state}\longrightarrow\text{geometry update}.
\]

The absence of such a channel is stronger than merely saying that Einstein's
equations have not yet been derived: the current state space has no variable
on which such an equation could act.

## 5. Stop-rule application

All three G0 requirements fail. The contract therefore requires immediate
termination as

\[
\boxed{\texttt{BLOCKED\_NO\_DYNAMICAL\_GEOMETRY}}.
\]

G1 (Einstein-Hilbert normalization), G2 (independent curvature/length anchor)
and G3 (non-circular physical identification) are **not executed**.

In particular, it would be invalid to assign the frozen `vartheta(X)` an
Einstein-Hilbert action, a Newton constant or an AdS radius by matching after
the fact. Those would be new model assumptions, not consequences of the
current QCA.

## 6. Relation to the existing E/AdS front

This negative gate does **not** make the E/AdS front meaningless.

E asks whether the already-proved flat corona law is stable when matter
propagates through a specified inhomogeneous deformation. That remains a
well-defined propagation problem.

What G0 establishes is narrower:

\[
\text{stability on a curved/inhomogeneous background}
\;\not\Rightarrow\;
\text{dynamical gravity}.
\]

Thus even a future PASS of H1/E0 would not, by itself, repair
`NO_ABSOLUTE_SCALE_DERIVABLE`.

## 7. External context checked in the preflight

Two external lines clarify the distinction but are not imported into the
frozen model:

1. Arrighi and Facchini, arXiv:1609.00305, construct quantum walks whose
   continuum limit includes the Dirac equation in curved spacetime. Their
   result shows that a metric can be represented by local unitaries; it does
   not add backreaction to the present CJWW/H1 model.
2. Mohamed Sacha, *Quantum Reports* **8**, 33 (2026), introduces a different,
   gauge-coded QCA/QICT framework with an emergent copy-time geometry and
   discusses a microscopic information stiffness associated with
   `G_eff`. The paper itself distinguishes its theorem-level copy-time
   result from model-dependent gravity closure and states that mapping model
   units to SI still requires choosing the microscopic spatial/time scales.

Neither source upgrades the frozen CJWW (5.15)+H1 construction into a
dynamical-gravity model.

## 8. Consequence and next admissible question

The current project now has a sharper separation:

- flat CJWW corona: mathematical result;
- E/H1: propagation stability under an externally specified inhomogeneous
  background;
- absolute-scale gate: no absolute scale derived;
- gravitational-normalization gate: blocked before normalization because the
  current model has no dynamical geometry.

A future successor, if separately authorized, would have to define a
**dynamical geometry model class first**: microscopic geometric degrees of
freedom, their local unitary update, and an explicit matter-to-geometry
backreaction rule. Only after that could an Einstein-Hilbert coefficient or
a curvature anchor be meaningfully audited.

No such successor model is constructed by this report.
