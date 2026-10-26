# EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE — execution

> **Typographic reconstruction — 2026-10-26.** Backslashes restored by hand
> against the self-contained purity and linearity proof below. No scientific
> text changed. A second operator proof, the infinite-dimensional continuity
> step and quantifier controls are recorded in
> `2026-10-26--cjww-exact-bridge-reconstruction.md`. No dedicated executable
> certificate or new independent review is claimed.

**Fecha:** 2026-09-29.  
**Contrato:** [EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE](../theory/EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md), frozen at commit `b8655ceefce70b3ec30df2372211a3565757df34`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE =
STRONG_EXACT_BRIDGE_IMPOSSIBLE
```

The obstruction is algebraic and occurs before locality, graph degree,
finite-depth synthesis or continuum limits enter.

## 1. Setup

Let

\[
V:\mathcal H_m\to \mathcal H_g\otimes\mathcal H_m
\]

be the isometry induced by the joint unitary from the fixed pure geometry
background:

\[
V|\psi\rangle=
U_{DG}(|G_0\rangle\otimes|\psi\rangle).
\]

Assume B1: for every matter density matrix \(\rho\),

\[
\operatorname{tr}_g(V\rho V^\dagger)
=
U\rho U^\dagger,
\qquad U=U_{\rm CJWW}.
\]

Define

\[
\widetilde V=(I_g\otimes U^\dagger)V.
\]

Then

\[
\operatorname{tr}_g(\widetilde V\rho\widetilde V^\dagger)=\rho
\]

for every \(\rho\). It is therefore enough to prove the statement for the
identity matter channel.

## 2. Pure-state factorization

Take any pure matter state \(|\psi\rangle\). The reduced matter state of

\[
|\Psi_\psi\rangle=\widetilde V|\psi\rangle
\]

is \(|\psi\rangle\langle\psi|\), which is pure.

A bipartite pure state has a pure reduced state iff its Schmidt rank is one.
Hence there is a normalized geometry vector \(|\gamma_\psi\rangle\) such that

\[
\widetilde V|\psi\rangle
=
|\gamma_\psi\rangle\otimes|\psi\rangle.
\]

At this point the geometry vector could still appear to depend on
\(|\psi\rangle\). Linearity removes that possibility.

## 3. Linearity forces one geometry state

Choose an orthonormal matter basis \(\{|i\rangle\}\). For each basis state,

\[
\widetilde V|i\rangle
=
|\gamma_i\rangle\otimes|i\rangle.
\]

Now apply the same statement to

\[
|+\rangle=\frac{|i\rangle+|j\rangle}{\sqrt2}.
\]

Linearity gives

\[
\widetilde V|+\rangle
=
\frac{|\gamma_i\rangle\otimes|i\rangle+
      |\gamma_j\rangle\otimes|j\rangle}{\sqrt2}.
\]

But the reduced matter state must be exactly

\[
|+\rangle\langle+|.
\]

Tracing out geometry gives an off-diagonal coefficient

\[
\frac12\langle\gamma_j|\gamma_i\rangle |i\rangle\langle j|+\mathrm{h.c.}
\]

which equals the required coefficient \(1/2\) only if

\[
\langle\gamma_j|\gamma_i\rangle=1.
\]

For normalized vectors this implies

\[
|\gamma_i\rangle=|\gamma_j\rangle.
\]

As \(i,j\) were arbitrary, one fixed normalized vector
\(|\Gamma\rangle\) satisfies

\[
\widetilde V|\psi\rangle
=
|\Gamma\rangle\otimes|\psi\rangle
\]

for every \(|\psi\rangle\). Undoing the \(U^\dagger\) conjugation,

\[
\boxed{
V|\psi\rangle
=
|\Gamma\rangle\otimes U_{\rm CJWW}|\psi\rangle.
}
\]

## 4. Complementary geometry channel

Therefore, for every matter density matrix \(\rho\),

\[
\operatorname{tr}_m(V\rho V^\dagger)
=
|\Gamma\rangle\langle\Gamma|.
\]

The final geometry state is independent of the matter input.

Thus B1 implies the negation of B2.

\[
\boxed{
\text{exact CJWW reduced unitary for all matter states}
\Longrightarrow
\text{no information-bearing matter-to-geometry backreaction}.
}
\]

No QCGD construction, local gate decomposition or graph rewrite can evade this
while retaining B1 exactly, because the contradiction already holds for an
arbitrary global unitary dilation.

## 5. Terminal-state decision

B1 and B2 are incompatible, so

\[
\boxed{\texttt{STRONG_EXACT_BRIDGE_IMPOSSIBLE}}.
\]

This is a theorem under the frozen pure-background and exact-channel
quantifiers. It is not based on a failed model search.

## 6. Scope and escape routes

The theorem does **not** rule out dynamical-geometry QCA.

It shows that backreaction necessarily disturbs the exact CJWW matter channel
if the geometry initially occupies one fixed pure background state and the
statement is required for every matter input.

Consequently any viable successor must weaken B1. The already-declared
possibilities are:

- W1: exact CJWW only at zero backreaction coupling, with controlled
  corrections for nonzero coupling;
- W2: exact CJWW only on a restricted reference/vacuum matter sector;
- W3: approximate/semi-classical CJWW after tracing over sharply peaked
  geometry;
- W4: a relational subsystem notion in which the two-component CJWW field is
  not the complete matter factor.

The most conservative successor for this project is W1: require

\[
U_{\rm matter}(g=0)=U_{\rm CJWW}
\]

exactly and quantify the first nontrivial joint matter/geometry correction as
\(g\to0\). That does not contradict the theorem because for \(g\ne0\) the
reduced matter channel is no longer required to be exactly unitary CJWW.

No W1 construction is made in this report.

## 7. External context

The result is consistent with the standard quantum-information principle
usually summarized as “no information without disturbance”. The present proof
is self-contained and uses only purity, Schmidt rank and linearity; no external
theorem is required for the project result.
