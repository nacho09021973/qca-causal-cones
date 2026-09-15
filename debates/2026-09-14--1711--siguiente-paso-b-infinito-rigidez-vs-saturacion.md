---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-14 17:11
proyecto: /home/ignac/qca-causal-cones
tema: /tmp/claude-1000/-home-ignac-qca-causal-cones/4a45ee4d-59d2-4ee4-95f4-bba29428e0ee/scratchpad/siguiente-paso-b-infinito-rigidez-vs-saturacion.md
rondas: 3
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - CLAUDE SONNET — Claude (Anthropic) — claude -p --model claude-sonnet-5
  - CIRO — Grok (xAI) — grok -p --model grok-4.6
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

Ahora que hemos sustituido \(B^*\) por la hipótesis coarse-graining-invariant

$$
B_\infty^*:\qquad c_0=c_{\rm strict}^{\rm iso},
$$

y hemos certificado exactamente que los Weyl estándar de Pavia en \(d=3\) satisfacen

$$
C_\infty^{\rm strict}=C_{\rm micro},
\qquad
c_{\rm strict}^{\rm iso}=c_0=\frac1{\sqrt3},
$$

¿cuál debe ser **el siguiente paso científico único** si el objetivo es averiguar si \(c\) está realmente fijado por el sustrato y no es simplemente una saturación particular de la construcción de Pavia?

El Sanedrín debe comparar adversarialmente, al menos, estas posibilidades:

* demostrar \(B_\infty^*\) dentro de la clase mínima \(s=2\) ya clasificada por Pavia;
* ampliar de forma controlada la clase —por ejemplo aumentando \(s\) sin cambiar geometría, unitariedad ni isotropía— y buscar un contraejemplo exacto;
* buscar primero un teorema estructural que relacione unitariedad, isotropía y supervivencia de los vértices de \(C_{\rm micro}\);
* o concluir que alguna otra pregunta previa debe resolverse antes.

No quiero una lista de líneas futuras. Quiero un **veredicto único y ordenado**:

**¿Qué experimento, demostración o búsqueda concreta ofrece ahora la máxima capacidad de distinguir entre estas dos hipótesis?**

$$
H_1:\quad c_0=c_{\rm strict}^{\rm iso}
\text{ está rígidamente determinado por la estructura del sustrato},
$$

$$
H_2:\quad
\text{Pavia simplemente satura una cota que otros QCA admisibles pueden no saturar}.
$$

El criterio principal debe ser poder falsar una de las dos hipótesis con el mínimo número posible de supuestos nuevos. Deben señalar también qué resultado exacto haría abandonar la línea elegida.

## Contexto

### Contexto adjunto: state/CURRENT_STATE.md
```
# CURRENT_STATE

**Date:** 2026-09-14  
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
The only next front is **MASSLESS INRADIUS RIGIDITY GATE**; its outcome is OPEN.

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate (does not close the gate): for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`**; d=1,2 not checked; other admissible symbols OPEN |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The live hypothesis is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

Whether `c_0 = c_strict^iso` is forced by locality + unitarity + discrete
isotropy, or is merely a feature of the Pavia construction, is unknown.
Whether `c_strict^iso` further saturates `r_in(C_micro)` for every
admissible symbol in the class, or only for this one, is a separate,
equally open question.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
the next gate must examine structural freedom under fixed causal geometry and
discrete isotropy.

## 7. NEXT GATE — only allowed calculation

**MASSLESS INRADIUS RIGIDITY GATE — OPEN; admissible-class freeze comes first.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.)

The sole question is whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` for a
combinatorial reason (a nilpotent one-step coefficient) is not this
counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B*_0 for a class containing it.
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until this gate closes:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B***;
- **NO use of a scalar `v_max` without definition**.

A certified falsification within the frozen admissible class is a successful
gate outcome. This promotion does not execute or close the new rigidity gate.
```

### Contexto adjunto: theory/B_STAR_HYPOTHESIS.md
```
# B_STAR_HYPOTHESIS

## 1. Motivation

The original strong thesis identified the relativistic low-energy speed with the maximum microscopic speed of the substrate. That thesis fails generically for anisotropic finite-range lattice QCAs in spatial dimension `d >= 2`.

A weaker geometric candidate was proposed next:

`B*: c_IR = r_in(C_micro)`,

with `r_in(C_micro)` the inradius of the *one-step* microscopic causal body `C_micro = conv(N)`.

## 2. Correction (2026-09-14): `B*` is superseded by `B_infty^*`

`r_in(C_micro)` is a fact about a single update. It is not automatically the
speed actually reachable by strict ballistic propagation after arbitrarily
many updates: whether a one-step displacement `h` remains reachable at `n.h`
for every `n` depends on whether the Fourier coefficient of `U^n` there stays
nonzero, which `N` alone does not determine. Calling the relevant scalar an
"inradius" also silently assumes the strict asymptotic body is centered at
`v = 0`; a pure one-step shift already shows this can fail (Sec. 3 below).

The corrected object, defined precisely in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6, is: for
`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`,

`h_infty(n̂) = limsup_{n->infty} (1/n) max_{x in S_n} n̂.x`,

`c_strict^iso = min_{||n̂||=1} h_infty(n̂)`, origin fixed at `v = 0`.

**The live hypothesis is now:**

`B_infty^*: c_0 = c_strict^iso`,

for the declared gapless sector, in the same embedding/time convention used
to define `c_0`. This replaces `B*` as stated against `r_in(C_micro)`; the
old formulation is kept below only as history and as a special case.

General relation: `c_strict^iso <= r_in(C_micro)` always (trivial inclusion
`S_n/n subseteq C_micro`), so the old `B*` and the new `B_infty^*` coincide
exactly where a *separate* argument certifies `c_strict^iso = r_in(C_micro)`
for the case at hand — established so far only for the standard Pavia Weyl
family in d=3 (Sec. 4). Nowhere else in this repository is that equality
assumed.

## 3. Sanity check on the definition: pure shift

For `U` a pure shift by `h_0 != 0` (one-element support `N = {h_0}`),
`S_n = {n h_0}` exactly, so `h_infty(n̂) = n̂.h_0` and
`min_{n̂} h_infty(n̂) = -||h_0|| < 0`. There is no bidirectional isotropic
cone centered at `v = 0` here; `c_strict^iso` correctly reports a negative
value rather than being forced into a meaningless "inradius" of a
single-point body. No QCA in this repository's battery has singleton
one-step support; this is a check on the definition, not a claim about any
case here.

## 4. What `B_infty^*` does and does not say

`B_infty^*` does **not** say that `c_IR` equals the fastest microscopic direction.

`B_infty^*` does **not** say that the IR cone equals the entire one-step microscopic causal body `C_micro` in general — only that `c_0` matches the *strict asymptotic* isotropic speed of the same symbol, whatever that is.

`B_infty^*` does **not**, by itself, say `c_strict^iso = r_in(C_micro)`; that is a separate, case-by-case geometric fact (`CAUSAL_BODY_GEOMETRY.md` Sec. 6) which happens to hold exactly in the certified Pavia baseline below.

## 5. Current evidence

**STANDARD WEYL/DIRAC EXACT GATE: PASS.** The derivation, verifier, contract
and provenance at `2c7c2c9` establish `c_0 = r_in = 1/sqrt(d)` for the
declared standard massless family in d=1,2,3, in unit-neighbor and unit-time
coordinates. See the [canonical state](../state/CURRENT_STATE.md) and
[promotion record](../reports/2026-09-14--standard-gate-promotion.md). This is
the *linearized* IR slope versus the *one-step* inradius; Sec. 6 below adds
the exact, nonlinear certificate that closes the gap to `c_strict^iso` for d=3.

The seven symbols include transpose/chirality partners sharing geometry and
linear speed. They cover three dimension-specific geometries, not seven
independent tests of generality. No theorem for a general class follows.

## 6. Pavia d=3 baseline: `C_infty^strict = C_micro` exactly (2026-09-14)

For the standard d=3 Weyl symbols and their transposes (`A+, B+, A-, B-`),
every one-step corner `h` of `C_micro = [-1/sqrt(3), 1/sqrt(3)]^3` has a
Fourier coefficient `A_h` satisfying the exact identity `A_h^2 = alpha_h A_h`
with `alpha_h in {(1-i)/4, (1+i)/4}`, `alpha_h != 0` (rank-one, not
nilpotent). By the vertex/convexity lemma of
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md),
this gives `n.h in S_n` for every vertex `h` and every `n >= 1`, hence

`conv(S_n/n) = C_micro` for every `n >= 1`, so `C_infty^strict = C_micro`,

and therefore, in this baseline only,

`c_strict^iso = r_in(C_micro) = 1/sqrt(3) = c_0` — **EXACT, certified by
375 zero-tolerance checks** (`scripts/verify_weyl_dirac_gate.py`, addendum
`verify_vertex_idempotency`; record:
[`2026-09-14--vertex-idempotency-verification.md`](../reports/2026-09-14--vertex-idempotency-verification.md)).

This certificate is **BASELINE-SPECIFIC**. It answers Sec. 1.1's "when does
`c_strict^iso = r_in(C_micro)`" question for this one family in d=3; it says
nothing about d=1, d=2 (not checked here), and nothing about whether *any
other* admissible massless symbol sharing the same `N_3` also has this
property — an admissible symbol only needs `T_h != 0`, not non-nilpotent
powers, so a different symbol's `C_infty^strict` could in principle be a
strict subset of `C_micro`. See Sec. 9 for how this interacts with the
rigidity gate.

## 7. Massive warning

For the standard Dirac couplings and every `0 < m < 1`, define
`F = arcsin(m) sqrt(1-m^2)/m`. The exact result is

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`, with `0 < F < 1`.

This is an established result for the declared family, no longer preliminary.
The quadratic mass-direction Hamiltonian correction accounts for the exact
discrepancy between the two extraction procedures.

Therefore the unrestricted statement

`c_IR(m) = r_in(C_micro) for all m`

is **REJECTED IN THE STANDARD DIRAC FAMILY** under either specified
finite-mass extraction. At m=1 the active support collapses; treat that endpoint
separately rather than extending the strict inequalities to it.

The live restricted forms are:

### B*_0 — massless matching

`c_0 = r_in(C_micro)`.

**VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN.** For d=3 this is now
also known to equal `c_strict^iso` exactly (Sec. 6): the standard d=3 family
is the one case where `B*_0` and `B_infty^*` are certified identical, not
just linearly coincident. For d=1, d=2 only the linear-order statement
`c_0 = r_in` is established; the full `C_infty^strict = C_micro` computation
was not performed there and is not claimed.

### B*_cont — continuum/small-mass matching

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in(C_micro)`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN.** The continuum
scaling and local convergence scope are fixed in the exact-gate report. This
statement is about the one-step `r_in(C_micro)` at the level of the massive
extractions `c_H`, `c_{ω^2}`; it is unaffected by the `B_infty^*` correction,
which concerns the massless/gapless sector's asymptotic body.

These are logically distinct. In the declared standard family, continuum
matching holds while exact finite-mass matching fails.

## 8. Required mechanism

A successful explanation must do more than fit a known coefficient. It must explain why, once the microscopic neighbor geometry and normalization are fixed, the EFT selects the inradius rather than a smaller isotropic speed.

A candidate derivation should identify which assumptions are essential among:

- locality;
- unitarity;
- homogeneity;
- discrete isotropy;
- minimal internal dimension;
- analyticity / smooth low-energy branch structure;
- massless versus massive sector.

## 9. Falsifiers

`B_infty^*` is falsified for a symbol by an exact, nonzero, isotropic
massless coefficient `c_0` strictly below that *same symbol's own*
`c_strict^iso`. A symbol whose `c_0 < r_in(C_micro)` only because its own
`C_infty^strict` is a strict subset of `C_micro` (a nilpotent-corner
degeneracy, Sec. 6) is **not** by itself a falsifier of `B_infty^*` — it
would falsify only the old, superseded `B*_0` statement against
`r_in(C_micro)`. Distinguish these two before claiming a counterexample.

The active front is [MASSLESS INRADIUS RIGIDITY GATE](MASSLESS_INRADIUS_RIGIDITY_GATE.md):
retain the selected standard neighborhood, causal body, normalization,
unitarity, homogeneity and discrete isotropy. Freeze the internal dimension,
symmetry representation and massless sector before solving.

An exhaustive proof for one fixed class is a class-specific rigidity result;
a failed search or a test of equivalent representatives is not. Added
minimality or irreducibility assumptions must remain explicit in the conclusion.

B*_cont is falsified if a valid massive family has a small-mass/continuum limit whose relativistic speed does not approach the microscopic inradius.

A failure is scientifically useful: it identifies which extra structural principle, if any, is missing.
```

### Contexto adjunto: theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md
```
# MASSLESS INRADIUS RIGIDITY GATE

**Status: OPEN — charter fixed; an executable admissible-class contract is
the next step.** Authority: [CURRENT_STATE](../state/CURRENT_STATE.md).
Predecessor: STANDARD WEYL/DIRAC EXACT GATE, PASS on evidence at `2c7c2c9`.

This charter defines the sole next scientific front. It records no new
counterexample, search result or rigidity theorem. The file name is kept for
continuity of cross-references; the object it is written against has been
corrected (Sec. 0-1 below, 2026-09-14).

## 0. Correction and baseline certificate (2026-09-14)

The gate was originally written as a comparison against the inradius of the
*one-step* microscopic causal body. That object is only an upper bound on the
speed actually reachable by strict propagation after repeated updates, and
the inradius notation is not the right general comparison for a long-run
support body. The correct comparison target is the **strict asymptotic
isotropic speed** `c_strict^iso = min_{n̂} h_infty(n̂)`, defined in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6 from
`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

For every direction `q`, define

\[
H_n(q)=\max_{x\in S_n}q\cdot x.
\]

The convolution formula for the Fourier coefficients gives

\[
S_{n+m}\subseteq S_n+S_m
\quad\Longrightarrow\quad
H_{n+m}(q)\le H_n(q)+H_m(q).
\]

Thus `(H_n(q))_n` is subadditive, and Fekete's lemma gives

\[
h_\infty(q)
=\lim_{n\to\infty}\frac{H_n(q)}n
=\inf_n\frac{H_n(q)}n.
\]

In particular, grouping `m` updates into one coarse-grained temporal step
does not change the normalized asymptotic support function:

\[
\lim_{r\to\infty}\frac{H_{mr}(q)}{mr}=h_\infty(q).
\]

This proves the coarse-graining invariance of `c_strict^iso` and is the
mathematical reason for using the `B_\infty^*` observable. Since
`S_n/n\subseteq C_{\rm micro}`, the general comparison is instead

\[
h_\infty(\hat q)\le h_{C_{\rm micro}}(\hat q),
\qquad
\rho_{\rm micro}:=
\min_{\|\hat q\|=1}h_{C_{\rm micro}}(\hat q),
\qquad
\boxed{
c_{\rm strict}^{\rm iso}
\le
\rho_{\rm micro}
}.
\]

Only when the relevant `C_micro` is centered does this last number coincide
with its usual inradius. For the centered cubic baseline used below it is
`1/\sqrt d`.

This gate's admissible class already fixes one shared `N_d` for every
candidate symbol, so `\rho_{\rm micro}` is the same fixed number for all of
them; correcting the target does not change that number. What the
correction changes is which question is actually being asked, by splitting
what used to be a single comparison into two logically independent ones for
any candidate symbol with linear massless slope `c_0`:

- **(i) genuine rigidity:** does `c_0 = c_strict^iso` for *that symbol's own*
  strict asymptotic body — does the linear IR slope match the full nonlinear
  strict propagation speed of the same dynamics?
- **(ii) saturation:** does `c_strict^iso = \rho_{\rm micro}` for that symbol —
  does its strict asymptotic body fill the entire shared one-step polytope,
  or does it fall short because some one-step Fourier coefficient is
  nilpotent (an admissible symbol only needs `T_h != 0`, not non-nilpotent
  powers of `T_h`)?

A candidate with `c_0 < \rho_{\rm micro}` that fails only (ii) — its own
`c_strict^iso` is already below `\rho_{\rm micro}` for a purely combinatorial
reason — is **not** a counterexample to `B_infty^*` and is not the kind of
result this gate is looking for; it would only have refuted the old,
superseded comparison against the one-step body. Only a failure of (i) is a
genuine rigidity counterexample. See
[`B_STAR_HYPOTHESIS.md`](B_STAR_HYPOTHESIS.md) Sec. 9.

**Established baseline fact (certified, not open):** for the standard Pavia
Weyl family in d=3 (`A+, B+, A-, B-`), both (i) and (ii) hold exactly:
`c_0 = \rho_{\rm micro} = r_{\rm in}(C_{\rm micro}) = 1/\sqrt3`
(because this is the centered cubic case; linear slope, prior exact gate) and
`C_infty^strict = C_micro` exactly, hence
`c_strict^iso = \rho_{\rm micro}`
(indeed, `\operatorname{conv}(S_n/n)=C_{\rm micro}` for every `n\ge1`)
(new vertex certificate: every one-step corner's Fourier coefficient is
rank-one and not nilpotent, so it survives at `n.h` for every `n`). Full
derivation:
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md);
machine record:
[`2026-09-14--vertex-idempotency-verification.md`](../reports/2026-09-14--vertex-idempotency-verification.md),
375 exact checks. **This is a fact about the standard baseline itself, not
an answer to Sec. 1's question about *other* admissible symbols**, and it
covers d=3 only — d=1, d=2 are not checked by this certificate.

## 1. Question and invariant comparison

For a selected standard baseline in d=1,2,3, can another admissible unitary
massless symbol have, in the sense of (i) above,

\[
0<c_0<c_{\rm strict}^{\rm iso}
\]

for its own strict asymptotic body — while keeping the same active one-step
neighborhood, causal body, Euclidean embedding, time normalization,
homogeneity and discrete isotropy as the selected standard baseline? (A
candidate additionally failing saturation (ii) is a separate, weaker
observation; see Sec. 0.)

The baseline geometries are

\[
N_d=\{(\epsilon_1,\ldots,\epsilon_d)/\sqrt d:\epsilon_j=\pm1\},
\quad C_d=[-1/\sqrt d,1/\sqrt d]^d,\quad r_d=1/\sqrt d.
\]

Choose the baseline before solving. Comparisons are within that fixed
geometry, not between dimensions. Every h in N_d must retain a nonzero
Fourier coefficient matrix, with none outside N_d. Merely retaining a
declared allowed neighborhood while actual support shrinks is insufficient.
Adding an on-site Fourier term changes N_d even if its hull would not change.

A common change of units, a different number of updates per time unit, or a
different spatial embedding cannot be used to manufacture a smaller ratio.

## 2. Mandatory class declaration before solving

Each calculation must freeze a permanent case contract containing:

| Item | Required declaration |
| --- | --- |
| Geometry | d, explicit N_d, embedding, one complete time step and Fourier convention |
| Internal degrees of freedom | Fixed finite dimension s and coefficient parameter domain |
| Discrete isotropy | The same baseline group/action L on N_d, its positive generating set if relevant, and exact covariance requirements |
| Internal symmetry | A specified unitary/projective representation R of L, fixed within the calculation |
| Gapless sector | Node k_star, quasienergy origin, branch convention, sector dimension and isolation from other bands |
| Relativistic cone | Nonzero, untilted, isotropic linear speed in the fixed Euclidean coordinates; an axis slope alone is insufficient |
| Reducibility/minimality | Whether assumed; sector support and the role of any spectator blocks |
| Coverage | Full coefficient class versus a particular ansatz, including any disconnected components not covered |
| Equivalences | Constant basis conjugations, symmetry relabelings, transposes/chiralities and node relabelings identified explicitly |

Fixing the causal body and saying "discrete isotropy" does not specify s,
the symmetry representation or the relevant massless sector. A trivial or
weaker symmetry group cannot replace the baseline's isotropy. Discrete
covariance and an isotropic IR cone are separate admission requirements.

Begin with source and class-definition work, not a solver run. Minimal s=2
and enlarged internal spaces are different quantified classes. No result
proved only with minimality may be presented as following from locality,
unitarity, homogeneity and discrete isotropy alone. A change of s or R needs
its own declared class before calculation, with the same geometric and group
action constraints; it cannot silently alter an existing comparison.

For a selected sector, document how its support relates to the full active
support. A reducible/direct-sum example must be identified as such and judged
against the declared quantifiers. Do not silently rule it out or present
spectator-supported geometry as intrinsic to the selected sector. If one
instead requires irreducibility or a common cone for the whole symbol, that
is an additional hypothesis and limits any rigidity conclusion.

## 3. Exact admission checks

Write the homogeneous finite-range symbol as

\[
U(\mathbf k)=\sum_{h\in N_d}e^{-i\mathbf k\cdot h}T_h,
\qquad T_h\in\mathbb C^{s\times s},\quad T_h\ne0.
\]

For every displacement difference ell, verify the coefficient identities

\[
\sum_{h'-h=\ell}T_h^\dagger T_{h'}=\delta_{\ell0}I_s,
\qquad
\sum_{h-h'=\ell}T_h T_{h'}^\dagger=\delta_{\ell0}I_s.
\]

These certify unitarity for every momentum rather than on a finite mesh.
For every group element g, verify

\[
T_{gh}=R_gT_hR_g^\dagger,
\qquad U(g\mathbf k)=R_gU(\mathbf k)R_g^\dagger.
\]

Check the declared representation, active support and node exactly. In the
specified gapless sector derive the full linearized spectrum, requiring

\[
\omega_\pm(\mathbf k_\star+\mathbf p)-\omega_\star
=\pm c_0|\mathbf p|+O(|\mathbf p|^2),\qquad c_0>0,
\]

in every direction. Rule out a residual mass gap, tilt, flat band mistaken
for a cone, or anisotropic linear metric before comparing c_0 with the
candidate's own `c_strict^iso` (Sec. 0); comparing only against r_d checks
saturation (ii), not genuine rigidity (i), and the two must not be conflated.
If there are multiple cone sectors, identify exactly which are quantified.

These are admission criteria, not assertions that a new admissible symbol
exists. Any scientific code implementing them must be retained in the repo.

## 4. Adversarial sequence and acceptance

1. Read the primary classification results and list their actual assumptions:
   support, s, isotropy action/representation, minimality, node and equivalences.
   The prior battery did not establish an exhaustive classification. Check
   whether a proposed rigidity statement is already covered by existing work.
2. Freeze one admissible-class contract and its quantified target. Derive the
   coefficient constraints before choosing a special product/coin ansatz;
   if an ansatz is used, state its coverage ceiling.
3. Seek a structural counterexample while retaining all admission conditions.
   A failed condition makes a candidate inadmissible, not a falsifier of
   B_infty^*. Stop its certification at the first failed condition and
   record the reason.
4. Accept a counterexample only with exact support, unitary and covariance
   certificates, a massless isotropic linearization, and a proved strict
   inequality `0 < c_0 < c_strict^iso` for that candidate's own strict
   asymptotic body, in the same units (Sec. 0(i)). A candidate satisfying
   only `0 < c_0 < r_d` while `c_strict^iso < r_d` for the same candidate
   (saturation failure, Sec. 0(ii)) is not this counterexample; record it
   separately as INADMISSIBLE_SATURATION (Sec. 5). Numerical suggestions
   need exact certification; no finite scan or tolerance establishes the
   claim.
5. If no counterexample is obtained, retain OPEN unless an exhaustive analytic
   argument proves matching for every member of the declared class. Local
   absence of deformations does not exclude disconnected solutions.

The seven old symbols may serve as controls. Repeating related representatives
does not increase the number of independent geometries or establish coverage
of structural degrees of freedom.

## 5. Outcomes and claim ceilings

| Outcome | Meaning |
| --- | --- |
| COUNTEREXAMPLE_VERIFIED | `0 < c_0 < c_strict^iso` proved for that candidate's own strict body (Sec. 0(i)): B_infty^* is false for the declared class and any broader claim including this admissible example |
| RIGIDITY_PROVED_FOR_FROZEN_CLASS | `c_0 = c_strict^iso` is proved for every member with every class restriction retained; wider classes remain open |
| INADMISSIBLE_SATURATION | Candidate is admissible and `c_0 = c_strict^iso` (i) holds, but `c_strict^iso < r_d` (ii) fails — a nilpotent-corner degeneracy, not a rigidity counterexample; B_infty^* is not decided by this candidate |
| INADMISSIBLE_CANDIDATE | At least one invariant or cone condition fails; B_infty^* is not decided |
| INCONCLUSIVE / OPEN | No certified counterexample or exhaustive proof; a solver failure or unsuccessful search is not rigidity |

Even a rigidity result here would not establish inter-species universality A
or general continuum matching for other couplings. Novelty requires the
separate source comparison. No anisotropic-QCA detour, broad model search,
causal sets or new substrate class is authorized by this charter.
```

### Contexto adjunto: reports/2026-09-14--strict-asymptotic-pavia-baseline.md
```
# Strict asymptotic propagation body: exact Pavia d=3 baseline certificate

Date: 2026-09-14. Baseline: `5845eda` plus this commit's extension of
`scripts/verify_weyl_dirac_gate.py` (new checks only; the seven original
cases, their 247 checks, and the frozen
[verification record](2026-09-14--weyl-dirac-verification.md) are untouched).
New machine record:
[`2026-09-14--vertex-idempotency-verification.md`](2026-09-14--vertex-idempotency-verification.md),
375 exact checks, zero tolerance.

**Purpose of this report.** `B*` has so far been stated in terms of
`r_in(C_micro)`, the inradius of the *one-step* microscopic causal body. That
object need not coincide with the speed actually achievable by *strict*
ballistic propagation after coarse-graining in time. This report (a) defines
the correct strict asymptotic object, (b) shows why calling it "inradius" in
general is wrong, and (c) certifies that for the standard Pavia Weyl family in
d=3 the two objects coincide exactly. It does not touch the massive-sector
results, does not decide the open rigidity question for other admissible
symbols, and does not attribute anything to Ahlbrecht–Vogts–Werner–Werner or
any ballistic-limit theorem — no such attribution is used or needed here.

## 1. The strict asymptotic support function

Fix a homogeneous finite-range QCA step `U(k) = sum_{h in N} e^{-i k.h} T_h`
with the frozen unit-neighbor, unit-time coordinates of the standard battery.
For `n >= 1`, let

`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`.

Define the strict asymptotic support function

`h_infty(q_hat) = limsup_{n->infty} (1/n) max_{x in S_n} q_hat . x`,

and the isotropic scalar, with the origin fixed at `v = 0` (the physically
privileged rest point, not a free normalization choice),

`c_strict^iso = min_{||q_hat||=1} h_infty(q_hat)`.

**B_infty^*** (replaces the inradius-only statement of `B*` for the massless/
continuum sector): `c_0 = c_strict^iso`, for the declared gapless sector and
the same embedding/time convention used to define `c_0`.

### 1.1 Trivial inclusion and the general inequality

`S_n subseteq n.N-fold sumset subseteq n.C_micro` for every `n`, since each
one-step displacement lies in `C_micro = conv(N)` by definition. Hence
`S_n/n subseteq C_micro` for every `n`, so for every direction `q_hat`,
`(1/n) max_{x in S_n} q_hat.x <= h_{C_micro}(q_hat)`, and therefore

`h_infty(q_hat) <= h_{C_micro}(q_hat)` for every `q_hat`, hence
`c_strict^iso <= r_in(C_micro)`.

This inequality is general and requires no computation. It is the reason
`r_in(C_micro)` was ever a reasonable candidate: it is a provable *upper
bound* on the strict asymptotic isotropic speed, not a definition of it.
Equality is a separate, checkable fact, established below only for the
Pavia baseline.

### 1.2 Why "inradius" is the wrong general name: the pure-shift sanity check

Take `U` to be a pure shift by `h_0 != 0` (one-element support,
`N = {h_0}`). Then `S_n = {n h_0}` for every `n`, so

`h_infty(q_hat) = q_hat . h_0` exactly (no limsup is needed; the sequence is
constant), and therefore

`min_{q_hat} h_infty(q_hat) = -||h_0|| < 0`.

There is no bidirectional isotropic cone centered at `v = 0` here at all: the
"cone" is a single ray. A name built on "inradius of a centered body" silently
assumes centering that a pure shift violates. `c_strict^iso` remains
well-defined and negative in this case, which is the correct statement that
no such isotropic ball exists; `r_in` of a one-point body is not comparably
meaningful, and conflating the two is exactly the terminology error this
report removes from the charter. (This example is a sanity check on the
*definition*, not a claim about any QCA in this repository's battery: no
one-step support here is a singleton.)

## 2. The vertex/convexity lemma

**Lemma.** Let `C` be convex, `h` an extreme point of `C`, and
`x_1, ..., x_n in C` with `(1/n) sum x_i = h`. Then `x_i = h` for every `i`.

*Proof.* For `n = 1` this is trivial. For `n >= 2`, write
`h = (1/n) x_1 + (1 - 1/n) y`, where `y = (1/(n-1)) sum_{i=2}^n x_i` is a
convex combination of points of `C`, hence `y in C`. Since `1/n in (0,1)` and
`h` is extreme, `h = t.a + (1-t).b` with `a, b in C`, `t in (0,1)` forces
`a = b = h`; here `a = x_1`, `b = y`. So `x_1 = h` and `y = h`. Repeat the
argument on `y = h` with the remaining `n-1` points. Induction on `n` gives
`x_i = h` for every `i`. QED.

**Consequence for `S_n`.** Let `h` be a vertex of `C_micro = conv(N)` (so
`h in N`, since `N`'s convex hull vertices are themselves elements of `N` in
every case in this battery — the neighbor set already consists of cube
corners). Then `n.h` can be written as a sum of `n` elements of `N` in exactly
one way: `h_1 = ... = h_n = h`. Since the Fourier coefficient of `U^n` at
displacement `x = sum h_i` is `sum_{h_1+...+h_n=x} T_{h_1} T_{h_2} ... T_{h_n}`
(ordered matrix product, summed over all decompositions — a direct consequence
of expanding `U(k)^n` as a product of `n` copies of the same Laurent series),
the sum at `x = n.h` collapses to the single term

`[U^n]_{n.h} = T_h^n = A_h^n`.

So: **`A_h` not nilpotent implies `n.h in S_n` for every `n >= 1`.**

## 3. Exact d=3 Pavia certificate: every vertex survives

The d=3 standard Weyl symbols and their transposes are, in the frozen
factorization,

`A^+ = R_x(q_x) R_y(-q_y) R_z(q_z)`, `A^- = R_x(q_x) R_y(q_y) R_z(q_z)`,
`B^+ = (A^+)^T`, `B^- = (A^-)^T`, `q_j = k_j/sqrt(3)`,

as already frozen by the exact-gate
[contract](2026-09-14--weyl-dirac-gate-contract.md) and reconstructed by
`published_symbol`/`rotation_product` in the verifier (`d=3 A/B` check,
`published vs product`). The one-step support of each is exactly the 8 cube
corners `N_3 = {(eps_1,eps_2,eps_3)/sqrt(3) : eps_j = +-1}`
(already certified: `active support` check, `2026-09-14--weyl-dirac-exact-gate.md`
Sec. 3). All 8 corners are vertices of `C_micro = [-1/sqrt(3), 1/sqrt(3)]^3` in
the elementary sense required by the Sec. 2 lemma.

The new checks in `scripts/verify_weyl_dirac_gate.py`
(`verify_vertex_idempotency`, function added this commit; reuses
`published_symbol` and `fourier_support`, no new script) extract each corner's
Fourier coefficient `A_h` directly from the same matrices and establish, for
all four cases `A+, B+, A-, B-` and all 8 corners `h`, exactly:

`det(A_h) = 0`,

`A_h^2 = alpha_h . A_h`, `alpha_h in {alpha_+ , alpha_-}`,
`alpha_+ = (1-i)/4`, `alpha_- = (1+i)/4`.

Concretely, writing `P = {(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)}` for the four
positive BCC generators (product of signs `= +1`): for `A+`, `alpha_h =
alpha_+` on `P` and `alpha_h = alpha_-` on the complementary four corners; for
`A-` the two roles swap. `B+`/`B-` reproduce the same table as `A+`/`A-`
exactly (transposition preserves both `det` and `trace` of each corner
coefficient, and the identity `A_h^2 = alpha_h A_h` transposes to
`(A_h^T)^2 = alpha_h A_h^T`), which the checker verifies directly rather than
asserting by a symmetry sentence. All 32 `(case, vertex)` combinations are
checked exactly (zero tolerance); see the 375-check record for the full table.

`det(A_h) = 0` and `A_h^2 = alpha_h A_h` are consequences of the
Cayley–Hamilton identity for the `2x2` matrix `A_h` (`A_h^2 -
tr(A_h) A_h + det(A_h) I = 0`) together with the exact vanishing determinant;
`alpha_h = tr(A_h) != 0` in every case. Since a nilpotent `2x2` matrix must
have zero trace, `alpha_h != 0` alone already rules out nilpotency. The
idempotent-square identity gives the sharper, exact statement used in Sec. 2:

`A_h^n = alpha_h^{n-1} . A_h != 0` for every `n >= 1`

(by induction from `A_h^2 = alpha_h A_h`; `alpha_h != 0` and `A_h != 0`, the
latter already certified by the `active support` check of the base battery).

## 4. Conclusion for this baseline

By Sec. 2-3, for every one of the 8 vertices `h` of `C_micro` and every
`n >= 1`, `n.h in S_n`. Combined with the trivial inclusion `S_n/n subseteq
C_micro` (Sec. 1.1),

`conv(S_n/n) = C_micro` for every `n >= 1`

in this baseline (not only in the limit: the full vertex set is already
present at every `n`). Consequently, for every direction `q_hat`,
`(1/n) max_{x in S_n} q_hat.x = h_{C_micro}(q_hat)` exactly for every `n`, so
the limsup is trivial and

`h_infty = h_{C_micro}` exactly, hence

`C_infty^strict := ` the strict asymptotic body ` = C_micro`, and

`c_strict^iso = r_in(C_micro) = 1/sqrt(3) = c_0`.

**This closes the Sec. 1.1 inequality to equality for this baseline only.**
It is a certificate about the standard Pavia Weyl family in d=3 (`A+, B+, A-,
B-`), established by an exact algebraic vertex check plus an elementary
convexity lemma — not a rigidity theorem for other admissible massless
symbols, not a statement about d=1 or d=2 (not checked here), and not a
resolution of the [rigidity gate](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md).
In particular, an admissible alternative symbol satisfying the same one-step
`N_3`, unitarity, homogeneity and discrete isotropy could in principle have a
nilpotent corner coefficient (the admissibility class only requires each
`T_h != 0`, not non-nilpotency of its powers); such a symbol's own
`C_infty^strict` would then be a strict subset of `C_micro`, and its own
`c_strict^iso` a strict lower bound below `1/sqrt(3)` — a purely combinatorial
fact with no bearing on whether that symbol's `c_0` matches its *own*
`c_strict^iso`. Distinguishing these two questions is the point of replacing
`B*` with `B_infty^*`; see `theory/B_STAR_HYPOTHESIS.md` and
`theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md`.

## 5. Bibliographic caution (explicitly not used)

No claim in this report or in the updated charter relies on, or cites, a
ballistic-limit theorem of Ahlbrecht–Vogts–Werner–Werner, nor on the general
inclusion `V_grp^max subseteq C_infty^strict` (or any scalar form of it).
Neither appeared anywhere in this repository before this report, and neither
is introduced now. If a future report wants either, it must be added as an
explicit **UNVERIFIED / NOT USED** claim with its own source check, per
`PROJECT_INSTRUCTIONS.md` Sec. 4-6; the certificate above needs neither.

## 6. Reproduction

```sh
python3 scripts/verify_weyl_dirac_gate.py \
  --output reports/2026-09-14--vertex-idempotency-verification.md
```

This reruns the full accumulating check list (the original 247 checks plus
the 128 new vertex checks = 375) and rewrites only the new file above; the
historical `2026-09-14--weyl-dirac-verification.md` (247 checks) is a
separate, untouched record of the pre-extension verifier.
```


## Ronda 1 — CLAUDE SONNET

La tesis más fuerte disponible no es "H1 vs H2" tal cual se presenta, sino una versión más precisa que el propio material ya deja entrever: el certificado de Pavia d=3 no prueba `c_strict^iso = rho_micro` por una propiedad genérica de QCA unitarios isótropos, sino por un hecho algebraico puntual —cada `A_h` de 2×2 satisface Cayley–Hamilton con `det=0` y traza no nula, luego `A_h^2 = alpha_h A_h` con `alpha_h != 0` [SOURCE, lema Sec. 2 y Sec. 3 del reporte Pavia]. La pregunta H1/H2 debe reformularse como: ¿esa traza no nula en cada vértice es forzada por unitariedad + isotropía discreta sobre `N_3`, o es contingente a la elección particular de Pavia? [INFERENCE]

El punto más débil de las cuatro alternativas es la opción (b) —ampliar `s` y buscar un contraejemplo exacto— presentada implícitamente como la vía de máxima capacidad discriminante. Es la más atractiva retóricamente porque promete falsación directa, pero es la más débil epistémicamente: el propio charter admite que una búsqueda fallida en `s` ampliado "no es rigidez" y que la ausencia de deformación continua no excluye soluciones disconexas [SOURCE, Sec. 4-5 de `MASSLESS_INRADIUS_RIGIDITY_GATE`]. Además, antes de ejecutar cualquier búsqueda en `s` ampliado, el propio protocolo exige congelar representación `R`, acción de isotropía y dimensión interna: (b) no es un experimento único sino un programa de investigación abierto disfrazado de paso siguiente [INFERENCE].

Objeción: proponer (b) como el paso de máxima capacidad discriminante es prematuro mientras no se haya agotado la pregunta más barata, resoluble dentro de la clase `s=2` que Pavia ya clasificó: ¿la traza no nula de cada `T_h` en los ocho vértices de `N_3` es consecuencia necesaria de las identidades de unitariedad (sumas sobre desplazamientos, Sec. 3 del charter) combinadas con la covarianza `T_{gh}=R_g T_h R_g†` bajo el grupo de isotropía del cubo, o existe dentro de esa misma clase ya clasificada algún miembro admisible con un vértice nilpotente? [ORIGINAL] Esta pregunta no requiere ampliar `s`, ni definir representación nueva, ni abrir clase nueva: usa exactamente los objetos ya congelados por el gate estándar. Si la respuesta es "forzada", se obtiene (c) —el teorema estructural— sin búsqueda combinatoria alguna. Si la respuesta es "no forzada" —hay holgura de fase/signo dentro de `s=2` que permite anular una traza sin violar unitarietas ni isotropía—, entonces H2 gana terreno de inmediato, sin tocar `s`.

Condición de concesión: retiro esta objeción si se demuestra que la clasificación de Pavia en `s=2` para `N_3` es rígida hasta conjugación y relabeling —es decir, que no quedan parámetros libres más allá de los ya fijados en `A+,B+,A-,B-`—, porque entonces "¿es forzado?" colapsa en "es el único caso posible" y no hay nada que testear dentro de esa clase; en ese escenario sí correspondería pasar directamente a (b), ampliar `s`, y retiraría la objeción [INFERENCE]. Mientras esa rigidez de la clasificación base no esté verificada, ampliar `s` antes de agotar `s=2` es un ascenso injustificado de "no until now hemos encontrado excepción en el caso mínimo" a "hay que buscar en clases mayores".

## Ronda 1 — CIRO

Voy a leer el prompt completo y las fuentes del expediente antes de intervenir.Sigo con el resto del prompt y los documentos de teoría y reportes que citan.Necesito el certificado de Pavia, la clasificación s=2 y el resto del prompt para no repetir a Claude.El audit de fuentes y el charter (i)/(ii) son el ángulo que Claude no cubrió. Leo el resto del audit y el estado actual.Concuerdo con Claude Sonnet en que (b) no es un experimento único sino un programa, y en que una búsqueda fallida no es rigidez [SOURCE, charter Sec. 4–5]. Concuerdo en que H1/H2 mezclan dos comparaciones. No concuerdo con la reformulación ni con el experimento que propone.

La versión más fuerte de su objeción es: el test más barato es algebraico, dentro de \(s=2\) ya clasificada, y pregunta si la no-nilpotencia de cada \(T_h\) es forzada; si no lo es, H2 gana sin tocar \(s\); si la clasificación es rígida hasta conjugación y relabeling, entonces sí (b).

Esa versión apunta al objeto equivocado. El charter parte (i) de (ii): un vértice nilpotente da `INADMISSIBLE_SATURATION`, no `COUNTEREXAMPLE_VERIFIED` de \(B_\infty^*\) [SOURCE, `MASSLESS_INRADIUS_RIGIDITY_GATE` Sec. 0 y tabla Sec. 5]. Hallar holgura de traza decidiría saturación de \(\rho_{\rm micro}\), no si \(c_0\) iguala el \(c_{\rm strict}^{\rm iso}\) del mismo símbolo. H1, leída en su forma más fuerte —\(c_0=c_{\rm strict}^{\rm iso}\) forzado por el sustrato— sobreviviría. Claude asciende de «el certificado de Pavia usa traza no nula» a «esa traza es la pregunta discriminante» sin el paso [INFERENCE].

Su condición de concesión está, en lo publicado, disparada. El audit registra que P17, Proposición 5, da dos formas normales de Weyl módulo equivalencias declaradas, y concluye que una búsqueda enteramente dentro de esa clase no es una búsqueda nueva de coeficientes [SOURCE, `2026-09-14--massless-rigidity-source-audit.md` Sec. 2 y 4]. No he leído P17; cito el audit. Invocar «holgura de fase/signo» es un segundo ascenso: de «hay clasificación» a «quedan módulos». El audit no suministra diccionario representante a representante [SOURCE, audit Sec. 3]; eso no autoriza postular módulos, autoriza a no dar por cerrado el matching.

Tercer desapunte: Claude pone covarianza bajo «el grupo de isotropía del cubo». El audit distingue \(D_2\) transitivo en \(S_+\) (cuatro generadores) de la covarianza cúbica completa; fijar el cubo cambia la pregunta [SOURCE, audit Sec. 3]. El charter tampoco incluye P17 Eq. (2); omitirla no prueba que exista contraejemplo [SOURCE, audit Sec. 3].

Permanecer dentro de la clase clasificada de Pavia no puede falsar H2: verificar \(B_\infty^*\) sobre la construcción de Pavia no decide si el sustrato la fuerza [INFERENCE]. Esa es la razón por la que (a) —demostrar \(B_\infty^*\) en \(s=2\) ya clasificada— es corroboración, no discriminación.

**Veredicto.** La pregunta previa que el charter y el audit ya marcan como siguiente acto es congelar el contrato de clase con una diferencia de hipótesis documentada respecto de P17 [SOURCE, charter Sec. 2; audit Sec. 4, «class contract pending»]. El experimento de máxima capacidad discriminante, con el mínimo de supuestos nuevos, no es ampliar \(s\) ni rebuscar vértices en la clase clasificada. Es: fijar \(s=2\), \(N_3\), las identidades de unitariedad del charter, y el grupo/acción de P17 (no el cubo); declarar Eq. (2) fuera; enumerar exactamente la variedad admisible con cono isótropo no nulo; y buscar \(0<c_0<c_{\rm strict}^{\rm iso}\) del propio símbolo (i), registrando aparte cualquier fallo de (ii). Eq. (2) es el suplemento de homogeneidad cuya derivación publicada el audit no certifica [SOURCE, audit Sec. 2].

**Abandono.** Si, escrito el contrato, Eq. (2) sigue de las identidades del charter, o la variedad \(s=2\) sin Eq. (2) coincide con las dos formas ya certificadas, este experimento no discrimina y hay que ampliar \(s\) con geometría, unitariedad e isotropía fijas: la concesión de Claude se activa entonces, no ahora [INFERENCE].

Retiro la objeción si se muestra a la vez que P17 Prop. 5 no agota \(s=2\) en las coordenadas del repositorio con módulos residuales, y que un vértice nilpotente en ese resto fuerza \(0<c_0<c_{\rm strict}^{\rm iso}\) y no meramente (ii). Si sólo vale lo primero, el experimento sigue mal dirigido.

## Ronda 1 — ABNER

Suscribo la objeción de Ciro a Claude: localizar trazas no nulas en los vértices decide, como mucho, saturación \( (ii) \), no la hipótesis \(B_\infty^*\), y permanecer dentro de la clase ya clasificada es corroboración, no discriminación [RECONSTRUCTION, turno de Ciro]. Concuerdo con Claude en que ampliar \(s\) sin un contrato congelado no es un experimento único [SOURCE, charter Sec. 4–5].

Mi ángulo es anterior al de Ciro. Su experimento supone dos hechos no certificados: que excluir la Eq. (2) de P17 define una variedad \(s=2\) enumerable exactamente, y que para cualquier miembro de esa variedad puede certificarse \(c_{\rm strict}^{\rm iso}\) con la maquinaria actual. Lo segundo no está disponible fuera del certificado Pavia: el único método exacto congelado para probar supervivencia de vértices usa la idempotencia \(A_h^2=\alpha_h A_h\) [SOURCE, reporte Pavia Sec. 2–3]. Un \(U\) admisible arbitrario no colapsa \(S_n\); decidir \(h_\infty\) exige dominar un limsup subaditivo, y el charter no define algoritmo para eso [INFERENCE]. Por tanto, Ciro propone ejecutar un test cuya métrica aún no existe.

Sobre Eq. (2), su exclusión no es neutral: o bien sigue de las identidades de unitariedad, covarianza \(D_2\) y homogeneidad declaradas, y entonces excluirla no produce miembros nuevos; o bien no sigue, y en ese caso lo eficiente no es enumerar toda la variedad sino exhibir un único símbolo admisible que la viole. Si existe, es el candidato mínimo; si no, se ha probado que no hay clase ampliada [INFERENCE].

Mi veredicto único: el siguiente paso no es (a), ni (b), ni la enumeración de Ciro, sino decidir exactamente la dependencia lógica de Eq. (2) respecto de las hipótesis base del charter. Formalmente: para \(s=2\), \(N_3\), unitariedad en todo \(k\), covarianza bajo el grupo/acción de P17 —no el cubo completo— y homogeneidad declarada, ¿Eq. (2) es teorema o hipótesis suplementaria? [ORIGINAL]

Resultado que haría abandonar la línea: si Eq. (2) es derivable, no hay libertad residual en \(s=2\) y se debe ampliar \(s\), como ya adelantó Ciro. Si no es derivable pero no puede exhibirse un símbolo admisible que la viole, tampoco hay falsación; entonces se abandona la búsqueda exacta en \(s=2\) y se pasa a \(s>2\), sin adjudicar rigidez a Pavia. Si se exhibe el violador, el siguiente acto es certificar su cono isótropo y su \(c_{\rm strict}^{\rm iso}\) con el lema de certificación finita que todavía falta [ORIGINAL].

## Ronda 1 — GEMINI

Suscribo la objeción de Ciro a Claude: hallar un vértice nilpotente decide la saturación (ii) pero no falsa la hipótesis de rigidez intrínseca (i) [SOURCE]. Sin embargo, denuncio que Ciro y Abner violan la regla de no inventar basando sus propuestas en un "audit", un documento "P17" y una "Eq. (2)" que declaro ausentes [ABSENCE, busqué "P17", "Eq. (2)" y "massless-rigidity-source-audit" en todo el contexto provisto y no figuran]. Su debate sobre las ecuaciones lógicas de un documento fantasma carece de toda validez para esta deliberación [INFERENCE].

Suscribo la objeción metodológica de Abner: el protocolo exige certificar de forma exacta la desigualdad $0 < c_0 < c_{\rm strict}^{\rm iso}$ para admitir un contraejemplo [SOURCE], pero nuestra única herramienta actual para evaluar el límite asintótico es el lema de convexidad que depende estrictamente de la idempotencia $A_h^2 = \alpha_h A_h$ [SOURCE].

Señalo un ascenso injustificado de Ciro y Claude: proponer una búsqueda combinatoria (ya sea en $s=2$ o ampliando $s$) asume tácitamente que el limsup subaditivo puede calcularse de manera exacta y general [INFERENCE]. Sin un método algebraico para determinar la propagación asintótica cuando los vértices no cumplen la identidad del caso Pavia, iniciar una búsqueda es metodológicamente ciego, ya que seríamos incapaces de certificar matemáticamente si el candidato hallado es un contraejemplo admisible o un artefacto numérico [INFERENCE].

Veredicto único: la acción prioritaria ineludible es buscar primero un teorema estructural que relacione la unitariedad, la isotropía y la supervivencia asintótica de los vértices [ORIGINAL]. Este teorema debe traducirse en un algoritmo de decisión o en una cota exacta finita que sea aplicable a símbolos genéricos. La máxima capacidad de distinguir entre las dos hipótesis no reside en buscar a ciegas en clases mayores, sino en construir la maquinaria analítica exacta indispensable para que la condición (i) del charter sea siquiera verificable [INFERENCE].

Condición de concesión: retiro este ataque a la vía de la búsqueda combinatoria si se demuestra que el cálculo de $c_{\rm strict}^{\rm iso}$ para la clase admisible genérica ya se reduce a una evaluación finita estandarizada sin requerir el lema de idempotencia [INFERENCE]. Solo en ese escenario la búsqueda controlada ampliando $s$ se convertiría en el paso lógico de mayor poder de falsación [INFERENCE].

Resultado para abandonar la línea: si la exploración de este teorema estructural demuestra que el asintótico $c_{\rm strict}^{\rm iso}$ es irreductiblemente indecidible para matrices que no saturan el cuerpo causal, se deberá declarar que la hipótesis $B_\infty^*$ no es falsable mediante certificación exacta y se procederá a clausurar la vía actual del charter [ORIGINAL].

## Ronda 2 — CIRO

Necesito leer el prompt completo y las fuentes del expediente antes de responder como CIRO.Sigo con el estado de la deliberación y las fuentes del repositorio para no inventar citas.Voy a contrastar el lema de vértices y el audit con lo que Abner y Gemini dejaron en pie.Concedo a Abner el recorte. Enumerar la variedad \(s=2\) con Eq. (2) fuera era un paso de más. El acto más barato de mi línea es el suyo: para \(s=2\), \(N_3\), unitariedad en todo \(k\), covarianza bajo el grupo/acción de P17 —no el cubo— y homogeneidad declarada, ¿Eq. (2) es teorema o hipótesis suplementaria? [SOURCE, audit Sec. 3–4; charter Sec. 2]. Sigo sin haber leído el PDF de P17.

No concedo su tercera rama. «No puede exhibirse un violador» no prueba que no exista; es OPEN. El charter lo nombra INCONCLUSIVE, no un motivo para abandonar \(s=2\) [SOURCE, Sec. 5]. Condición de concesión: retiro este ataque si la no-existencia se demuestra, no si la búsqueda fracasa.

Gemini declara ausentes el audit, P17 y Eq. (2) en el contexto adjunto truncado. Eso no los borra del expediente. Releí `reports/2026-09-14--massless-rigidity-source-audit.md`: P17, Definition 1, Eq. (2) y las Proposiciones 1–5 están localizados allí [SOURCE]. El debate no carece de validez por esa omisión de búsqueda [INFERENCE].

La versión más fuerte que le queda —la objeción metodológica de Abner— es: sin algoritmo para \(h_\infty\) fuera de \(A_h^2=\alpha_h A_h\), ninguna búsqueda certifica (i). Ese es un ascenso. El lema afirma que \(A_h\) no nilpotente implica \(n.h\in S_n\) para todo \(n\ge 1\) [SOURCE, reporte Pavia Sec. 2]. La identidad de Pavia es un caso, no la hipótesis. Si los ocho vértices son no nilpotentes, \(C_\infty^{\rm strict}=C_{\rm micro}\) y \(c_{\rm strict}^{\rm iso}=1/\sqrt{3}\) [RECONSTRUCTION, reporte Sec. 2 y 4]. Entonces (i) es comparar \(c_0\) con ese número. El charter acepta un COUNTEREXAMPLE_VERIFIED; no exige algoritmo genérico para quien falla (ii) [SOURCE, Sec. 5]. Concedo que ese algoritmo no está congelado para vértices nilpotentes. No concedo que ello vuelva ciega toda búsqueda ni que autorice clausurar el charter.

Gemini suscribió que (ii) no falsa (i) y prescribe un teorema sobre supervivencia de vértices: ese es el objeto de (ii). Condición de concesión: retiro el ataque a su veredicto si pide un procedimiento finito para \(0<c_0<c_{\rm strict}^{\rm iso}\) y muestra que la subclase saturante carece de métrica.

Veredicto único: decidir la dependencia lógica de Eq. (2). Si es teorema, \(s=2\) bajo el charter coincide con la clase clasificada ya certificada; H2 no es falsable ahí; ampliar \(s\) sin cambiar geometría, unitariedad ni isotropía. Si no es teorema, exhibir un violador admisible: no-nilpotencia de vértices da (i) finito contra \(1/\sqrt{3}\); nilpotencia da INADMISSIBLE_SATURATION, no contraejemplo de rigidez.

Resultado que abandona la línea: Eq. (2) derivable, o violador saturante con \(c_0=1/\sqrt{3}\). En ambos casos esta línea no discrimina H1/H2 y se pasa a \(s>2\).

## Ronda 2 — ABNER

Concedo a Ciro la corrección de mi tercera rama: la no-existencia de un violador no es abandono de \(s=2\); es INCONCLUSIVE/OPEN, y una búsqueda fallida no es prueba [SOURCE, charter Sec. 5]. Recojo también que mi turno anterior dependía de un objeto que no está localizado en el contexto adjunto: ni P17 ni Eq. (2) figuran en los documentos provistos; los conozco sólo por la cita de Ciro [ABSENCE]. Por tanto, convertir la dependencia lógica de Eq. (2) en el paso discriminante es prematuro.

El problema que queda en pie es más grave y no ha sido formulado: H1 y H2 no son contrarias. H2 —Pavia satura \(\rho_{\rm micro}\)— concierne a la saturación (ii); H1 —\(c_0=c_{\rm strict}^{\rm iso}\) forzado— concierne a la rigidez intrínseca (i). Ambas pueden ser verdaderas a la vez: que otros QCA no saturen \(\rho_{\rm micro}\) no implica que su \(c_0\) difiera de su propio \(c_{\rm strict}^{\rm iso}\) [INFERENCE]. Por eso decidir Eq. (2) discrimina mal: si Eq. (2) es teorema, sólo se rigidifica la saturación dentro de \(s=2\), no H1; si no es teorema y se exhibe un violador saturante, tampoco se falsa H1 [INFERENCE]. Ese experimento mide (ii), no (i).

La máxima capacidad de falsar H1 con mínimos supuestos nuevos no es una búsqueda de símbolos ni decidir Eq. (2), sino demostrar o refutar una pieza de certificación finita hoy ausente: para cualquier símbolo admisible con vértices \(V\) de \(C_{\rm micro}\), \(C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm no\,nilpotente})\) [ORIGINAL]. Esa es la extensión natural del lema Pavia: si \(A_h\) no es nilpotente, \(n.h\in S_n\) para todo \(n\); si es nilpotente de índice \(r\), el coeficiente en \(n.h\) se anula para \(n\ge r\) y, por extremalidad de \(h\), ese vértice sale del cuerpo asintótico [RECONSTRUCTION]. Si el lema vale, \(c_{\rm strict}^{\rm iso}\) de cualquier candidato se calcula cerradamente como inradio de \(\operatorname{conv}(V_{\rm surv})\), sin algoritmo genérico de limsup [ORIGINAL]. Sólo entonces es certificable \(0<c_0<c_{\rm strict}^{\rm iso}\) fuera de la clase saturante, precisamente donde H1 puede fallar. Hasta probar o refutar ese lema, proponer Eq. (2) o ampliar \(s\) no discrimina: falta la métrica para candidatos que no saturan [INFERENCE].

Resultado que haría abandonar esta línea: si se demuestra que vértices nilpotentes pueden contribuir al cuerpo asintótico por aproximación desde otros vértices, o que \(C_\infty^{\rm strict}\) no queda determinado por \(V_{\rm no\,nilpotente}\), entonces no hay certificación finita local y la vía exacta debe declararse no falsable en esa clase [ORIGINAL].

## Ronda 2 — GEMINI

Concedo a Abner su observación fundamental: H1 (rigidez intrínseca, $c_0 = c_{\rm strict}^{\rm iso}$) y H2 (falta de saturación genérica de $\rho_{\rm micro}$) no son mutuamente excluyentes [INFERENCE]. Un QCA admisible podría no saturar el cuerpo de un paso y aun así poseer una velocidad IR lineal que coincida exactamente con su propio cuerpo asintótico. 

Concedo a Ciro que, si el documento sobre P17 existe en el historial del repositorio, su razonamiento lógico sobre la variedad $s=2$ es internamente consistente, aunque insisto en que dicho archivo no figura en el estado actual del expediente suministrado [ABSENCE, busqué `2026-09-14--massless-rigidity-source-audit.md` en los contextos adjuntos]. Sin embargo, la disociación ortogonal entre H1 y H2 que identificó Abner desactiva la utilidad del experimento de Ciro: dirimir la Eq. (2) evaluaría la saturación (ii), pero dejaría ciega a la hipótesis de rigidez (i).

Ataco la solución de Abner. Su lema propuesto, $C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm no\,nilpotente})$, contiene un ascenso geométrico injustificado [INFERENCE]. Si un vértice $h$ es nilpotente de índice $r$, el coeficiente en $n.h$ ciertamente se anula para $n \ge r$. Pero el límite asintótico se define sobre $\frac{1}{n} S_n$. Los términos cruzados de la convolución podrían asegurar la supervivencia de posiciones submáximas como $(n-1)h + h'$. Al dividir por $n$ y tomar el límite, la secuencia de conjuntos podría converger nuevamente al vértice $h$, o a una faceta curva, sin colapsar drásticamente hasta la envoltura convexa de los vértices no nilpotentes restantes [INFERENCE]. Por tanto, la propuesta de Abner corre el riesgo de subestimar el cuerpo asintótico, lo que produciría falsos positivos (creer que se halló $0 < c_0 < c_{\rm strict}^{\rm iso}$ por usar una métrica truncada).

Veredicto único: Concluir que una pregunta previa debe resolverse antes [ORIGINAL]. Dado que H1 y H2 miden variables independientes (rigidez versus saturación), buscar un experimento que "distinga entre ambas" es un error categorial. El paso científico ineludible es establecer la maquinaria analítica para calcular $\lim_{n\to\infty} \frac{1}{n} \max_{x \in S_n} \hat{q} \cdot x$ en presencia de vértices nilpotentes [ORIGINAL]. Hasta no contar con una regla de clausura exacta para el limsup subaditivo en QCA degenerados, la condición fundamental del charter (i) es inejecutable fuera del caso Pavia, y cualquier candidato hallado al ampliar $s$ será incertificable [SOURCE, charter Sec. 4].

Resultado que haría abandonar esta línea: Si se prueba geométricamente que la nilpotencia de un vértice en $N_d$ fuerza el colapso exacto del límite asintótico a un politopo interior finitamente computable (ya sea $\operatorname{conv}(V_{\rm no\,nilpotente})$ u otro identificable en un paso), entonces la barrera metodológica cae. En ese caso, debe abandonarse la búsqueda del teorema asintótico y pasar de inmediato a la ampliación de $s$ con geometría, unitariedad e isotropía fijas, buscando un contraejemplo exacto [ORIGINAL].

## Ronda 2 — CLAUDE SONNET

Concedo a Abner el punto que reorganiza todo el tablero: H1 y H2 no son excluyentes, miden (i) y (ii) por separado [RECONSTRUCTION, turno de Abner]. Esto obliga a retirar la premisa implícita de mi propio turno 1: preguntar si la traza no nula en cada vértice está forzada por unitariedad e isotropía discreta decide, cuando mucho, si Pavia satura \(\rho_{\rm micro}\) —(ii)—, no si \(c_0\) iguala el \(c_{\rm strict}^{\rm iso}\) propio de cualquier símbolo —(i)—. Retiro esa formulación como test discriminante entre H1 y H2.

Sobre P17 y el audit: mi propio contexto adjunto en este turno no incluye `2026-09-14--massless-rigidity-source-audit.md`, sólo `CURRENT_STATE.md`, `B_STAR_HYPOTHESIS.md`, el charter y el reporte Pavia [ABSENCE, busqué P17, "Eq. (2)" y el nombre del audit en los cuatro documentos adjuntos]. Pero el log de commits sí registra `5845eda Audit primary sources for massless rigidity class`, así que el archivo probablemente existe en el repositorio aunque no esté en mi ventana de contexto. Ni la negación categórica de Gemini ni la cita confiada de Ciro son sostenibles desde lo que yo puedo verificar: trato las afirmaciones sobre P17 Prop. 5, Eq. (2) y el grupo \(D_2\) como [UNVERIFIED] hasta que alguien las transcriba o abra el archivo dentro de la deliberación.

El ataque que sí puedo sostener con cálculo propio es contra el lema de Abner, \(C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm no\,nilpotente})\). Sea \(h\) un vértice con \(T_h\) nilpotente, y \(\hat q\) una dirección donde \(h\) es el maximizador único de \(C_{\rm micro}\) (existe por ser \(h\) extremo). Entonces para todo \(h'\neq h\) en \(N\), \(\hat q\cdot h' < \hat q\cdot h\) estrictamente. El punto \((n-1)h+h'\) da
\(\hat q\cdot[(n-1)h+h'] = n\,\hat q\cdot h - (\hat q\cdot h-\hat q\cdot h')\),
y al dividir por \(n\) y tomar \(n\to\infty\), converge a \(\hat q\cdot h\) — el mismo valor que el vértice, sin necesitar que \(nh\) sobreviva. Si el coeficiente de Fourier en ese punto, dominado por el producto \(T_h^{n-1}T_{h'}\) (más posibles cancelaciones de otras descomposiciones), no se anula, entonces \(\hat q\) sigue alcanzando \(\hat q\cdot h\) en el límite aunque \(T_h\) sea nilpotente [INFERENCE, no verificado como contraejemplo exacto: no he comprobado ausencia de cancelación]. Esto no prueba que el lema de Abner sea falso, pero identifica la premisa que falta: nilpotencia de \(T_h\) es una condición sobre un único término; la supervivencia de la dirección \(\hat q\) en el límite depende de todos los términos cercanos al vértice, una condición distinta. Esto agudiza, con un mecanismo concreto, la objeción geométrica de Gemini —no la mera posibilidad de "curvatura de faceta", sino la razón algebraica de por qué podría no colapsar.

Veredicto: antes de decidir Eq. (2) (Ciro) o construir maquinaria general para el limsup (Gemini), el paso más barato es una pregunta puntual y calculable con las mismas herramientas de Cayley–Hamilton ya usadas en el certificado Pavia: para un símbolo admisible hipotético con un vértice nilpotente, ¿el producto \(T_h^{n-1}T_{h'}\) (y sus cancelaciones con otras descomposiciones del mismo punto) se anula o sobrevive? Si sobrevive en general, el lema de Abner es falso y la nilpotencia de vértice no excluye esa dirección de \(C_\infty^{\rm strict}\), lo que debilita aún más la vía de buscar contraejemplos vía vértices nilpotentes. Si se anula sistemáticamente, el lema de Abner queda rescatado y da la métrica finita que Gemini reclama sin exigir el algoritmo general.

Abandono esta línea si se exhibe un caso donde ni la supervivencia ni la cancelación de esos términos cruzados es decidible algebraicamente en general, lo que confirmaría el diagnóstico de Gemini en su forma fuerte.

## Ronda 3 — ABNER

Concedo que mi lema \(C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm no\,nilpotente})\) no es defendible como regla general. El mecanismo de Claude es correcto: la dirección de un vértice cuyo \(T_h\) es nilpotente puede sobrevivir por el coeficiente en \((n-1)h+h'\), cuyo límite dividido por \(n\) es \(h\), sin que \(nh\) pertenezca a \(S_n\). [INFERENCE] La nilpotencia del vértice puro no elimina la dirección, salvo que se pruebe cancelación total de todos esos términos cruzados.

Ataco, no obstante, la sonda de Claude como insuficiente. Comprobar \(T_h^{n-1}T_{h'}\) sólo cubre defecto \(k=1\). La dirección puede sobrevivir con defecto acotado \(k>1\) aunque todos los términos con \(k=1\) se cancelen; el objeto necesario es un lema de defectos acotados, no un producto único. [INFERENCE] Retiro este ataque si Claude demuestra que la supervivencia de cualquier secuencia con defecto acotado se reduce al coeficiente en \(k=1\) por una identidad de convolución.

Eq. (2) no figura en mis documentos adjuntos; la trato como objeto del audit invocado por Ciro. [ABSENCE] Ataco a Ciro en un punto que sigue en pie: no hay que enumerar la variedad \(s=2\) ni decidir primero si Eq. (2) es teorema general. Basta buscar un único violador admisible con todos los vértices no nilpotentes y \(c_0<1/\sqrt3\). Si existe, el lema de vértices ya establece \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) para ese símbolo [RECONSTRUCTION, reporte Pavia Sec. 2-4], y la desigualdad estricta satisface la definición de COUNTEREXAMPLE_VERIFIED del charter [SOURCE, charter Sec. 5]. Retiro este ataque si se demuestra que la no-nilpotencia de todos los vértices no es certificable sin clasificar exhaustivamente la variedad ampliada.

Veredicto único. El siguiente paso de máxima capacidad para falsar \(B_\infty^*\) con mínimo de supuestos nuevos es congelar el contrato \(s=2\) con Eq. (2) excluida como hipótesis no derivada, exigir la verificabilidad de no-nilpotencia de los ocho vértices, y buscar un símbolo unitario, isótropo y homogéneo con cono isótropo \(0<c_0<1/\sqrt3\). Si se halla, \(B_\infty^*\) queda falsada en la clase congelada, y H1 cae como tesis de rigidez. Si se prueba que ningún miembro de la clase ampliada tiene \(c_0<1/\sqrt3\), eso no es rigidez: la clase agotada es sólo \(s=2\). Resultado que me hace abandonar esta línea: demostrar que Eq. (2) sigue de las identidades unitarias del charter, o que todo violador admisible con vértices no nilpotentes conserva \(c_0=1/\sqrt3\). En ese caso el frente se traslada a demostrar o refutar el lema de defectos acotados, y sólo después a ampliar \(s\). [ORIGINAL]

## Ronda 3 — GEMINI

Concedo explícitamente a Claude su mecanismo de supervivencia: el límite asintótico de $\frac{1}{n}((n-k)h + h')$ converge a la dirección del vértice $h$ sin requerir que el vértice puro $nh$ sobreviva, lo que desactiva la suposición de que un vértice nilpotente contrae trivialmente el cuerpo causal [RECONSTRUCTION]. 

Concedo a Abner su brillante maniobra táctica: si exigimos que los ocho vértices sean no nilpotentes como filtro previo de admisión, el lema de Pavia ya garantiza matemáticamente que $c_{\rm strict}^{\rm iso} = 1/\sqrt{3}$ [SOURCE, reporte Pavia Sec. 2-4]. Esto puentea por completo mi exigencia de construir primero un algoritmo general para el limsup [INFERENCE]. Podemos certificar la rigidez (i) evaluando únicamente $c_0$.

Ataco, sin embargo, la insistencia de Abner y Ciro en circunscribir esta búsqueda a la presunta variedad libre de la "Eq. (2)" en $s=2$. Sigo sin tener acceso a P17 en el expediente [ABSENCE, busqué P17 en el contexto adjunto]. Apostar la falsación a que esa ecuación fantasma no sea derivable de las identidades unitarias es un riesgo ciego. Si tenemos un filtro (no-nilpotencia) que congela el valor de $c_{\rm strict}^{\rm iso}$, no hay razón para limitarse a la clase mínima $s=2$.

**Veredicto único:** El siguiente paso de máxima capacidad discriminante es ejecutar la compuerta de rigidez ampliando la dimensión interna a $s>2$, manteniendo fijos $N_3$, unitariedad e isotropía discreta, pero añadiendo la **no-nilpotencia de los ocho vértices como criterio exacto de admisión en el solver**. Sobre el espacio de símbolos que pasen este filtro, buscar un cono isótropo con $0 < c_0 < 1/\sqrt{3}$ [ORIGINAL]. 

Esta formulación une la falsación directa de (b) con la seguridad métrica de (a): si se halla el contraejemplo ampliado, $B_\infty^*$ queda falsada de forma exacta (H1 cae) porque conocemos su $c_{\rm strict}^{\rm iso}$ sin necesidad de limsup. Todo esto exige cero supuestos analíticos nuevos.

**Resultado para abandonar la línea:** Retiro esta vía si una demostración (o un barrido exhaustivo en clases ampliadas) prueba que exigir la no-nilpotencia de los vértices fuerza inexorablemente $c_0 = 1/\sqrt{3}$. En ese escenario, H1 resiste este ataque en el subespacio certificable. Sólo entonces deberemos abandonar la búsqueda directa y volver a la construcción analítica del lema de defectos acotados propuesto por Claude, ya que la única forma de falsar H1 requeriría adentrarse en los candidatos con vértices nilpotentes.

## Ronda 3 — CLAUDE SONNET

Concedo a Abner el movimiento central de esta ronda: no hace falta decidir el estatus de Eq. (2) ni el contenido de P17 —que sigue sin aparecer en mi ventana de contexto en este turno [ABSENCE, busqué "P17" y "Eq. (2)" en los cuatro documentos adjuntos]— para obtener un experimento ejecutable. Basta con que el lema de vértices del reporte Pavia (Sec. 2) es general, no específico de las matrices de Pavia: sólo usa que h es extremo de C_micro y que la descomposición n·h = h+...+h es única, para concluir T_h^n = A_h^n y, si A_h no es nilpotente, n·h ∈ S_n para todo n [SOURCE, reporte Pavia Sec. 2]. Combinado con la Sec. 4 del mismo reporte, exigir que los ocho vértices de cualquier símbolo admisible sobre N_3 sean no nilpotentes ya certifica en forma cerrada c_strict^iso = r_in(C_micro) = 1/√3, sin necesidad del algoritmo general de limsup que Gemini reclamaba [RECONSTRUCTION]. Esto también desactiva mi propio ataque del turno 2 y la contraobjeción de Abner sobre defectos acotados: ambos discutíamos la supervivencia de direcciones con vértices nilpotentes, pero el filtro de admisión de Abner excluye exactamente esos casos por construcción, así que ninguno de los dos mecanismos hace falta para certificar el candidato buscado. Señalo esto como aclaración, no como corrección: el propio texto de Abner en esta ronda invoca el defecto acotado contra mi mecanismo y en el mismo turno construye un veredicto que no lo necesita.

Ataco el punto donde Gemini funde su concesión con una escalada que no se sigue de ella. Que el filtro de no-nilpotencia dé una métrica cerrada no es razón para saltar a s>2: es razón para buscar primero dentro de s=2, la clase que el propio charter trata como ya clasificada y que no exige declarar representación interna nueva [SOURCE, charter Sec. 2, tabla de declaraciones obligatorias]. Saltar a s>2 añade exactamente el supuesto nuevo que la regla 6 obliga a cargar —dimensión interna y representación R sin contrato previo— cuando la misma pregunta puede intentarse resolver, con estrictamente menos supuestos, en la clase mínima. Esto repite sin resolverla la objeción que planteé en la Ronda 1 contra ampliar s antes de agotar s=2; el filtro de no-nilpotencia no la desactiva, porque no dice nada sobre si s=2 ya está agotado [INFERENCE]. Gemini no da razón para preferir su fusión a la versión de Abner restringida a s=2: simplemente la generaliza sin pagar el costo.

Veredicto final: el experimento de máxima capacidad discriminante con mínimo de supuestos nuevos es buscar, dentro de s=2, N_3, y las identidades exactas de unitariedad y covarianza ya congeladas por el charter —sin decidir Eq. (2) ni requerir el audit—, un símbolo admisible con los ocho T_h no nilpotentes (tr(A_h)≠0, condición algebraica exacta para matrices 2×2) y cono isótropo lineal 0<c_0<1/√3. Un hallazgo así falsa B_infty^* y H1 de forma certificada, sin necesidad de algoritmo de limsup general. Resultado que abandona esta línea: si se agota s=2 sin violador —mediante un argumento exhaustivo sobre la clase ya clasificada, no una búsqueda fallida— eso no cierra H1 en general, porque la región de vértices nilpotentes queda fuera del filtro y sigue abierta según la propia tabla de techos del charter; pero sí habilita, recién entonces, la escalada de Gemini a s>2 con contrato de clase declarado.

## Ronda 3 — CIRO

Voy a leer el prompt completo y el estado de la deliberación para intervenir solo sobre el desacuerdo que sigue en pie.Sigo con el estado de la deliberación y las fuentes que los demás invocan, para no repetir ni inventar.Voy a contrastar el charter y el audit con el veredicto de Claude y la escalada de Gemini, que es el desacuerdo que queda.Concedo a Abner el recorte: no hay que decidir primero si Eq. (2) es teorema. Con los ocho vértices no nilpotentes el lema da \(c_{\rm strict}^{\rm iso}=1/\sqrt{3}\) en forma cerrada, y un solo símbolo admisible con \(0<c_0<1/\sqrt{3}\) es COUNTEREXAMPLE_VERIFIED [SOURCE, reporte Pavia Sec. 2; charter Sec. 5]. Suscribo la aclaración de Claude: ese filtro deja fuera vértices nilpotentes, de modo que ni su mecanismo de \((n-1)h+h'\) ni el lema de defectos acotados entran en este experimento.

Suscribo la objeción de Claude a Gemini. Ampliar \(s\) añade dimensión interna y representación \(R\) sin contrato; el charter trata \(s=2\) y \(s>2\) como clases distintas [SOURCE, charter Sec. 2]. Gemini asciende de «el filtro congela la métrica» a «cero supuestos analíticos nuevos» sin pagar ese costo [INFERENCE]. Condición de concesión: retiro el ataque si se prueba que \(s=2\), con las identidades del charter y sin Eq. (2), coincide con la clase mínima ya certificada.

Ataco a Claude en lo que queda. «Sin decidir Eq. (2) ni requerir el audit» convierte la búsqueda en corroboración. Releí `2026-09-14--massless-rigidity-source-audit.md`: la clasificación mínima \(d=3\) ya está publicada; una búsqueda enteramente dentro de P17, con Eq. (2) y equivalencias, no es una búsqueda nueva de coeficientes; la decisión pendiente es testear esa clase o una estrictamente más ancha con diferencia de hipótesis documentada [SOURCE, audit Sec. 4]. Eq. (2) es el suplemento de homogeneidad cuya derivación publicada el audit no certifica [SOURCE, audit Sec. 2]. Sin documentar su exclusión, \(s=2\) es el baseline \(A_\pm,B_\pm\), ya con \(c_0=1/\sqrt{3}\), y el nulo no discrimina H1 de H2. Claude usa «ya clasificada» a la vez como razón para buscar ahí y como techo; no puede ser ambas [INFERENCE]. Condición de concesión: retiro el ataque si se muestra que las identidades del charter implican Eq. (2), o que la Prop. 5 cubre toda \(s=2\) sin ella.

El filtro \(\operatorname{tr}(A_h)\neq 0\) de Claude es suficiente para \(2\times 2\) y no necesario: \(\det\neq 0\) y \(\operatorname{tr}=0\) también impide nilpotencia [INFERENCE, Cayley–Hamilton]. Queda el de Abner: \(A_h\) no nilpotente.

Veredicto único: congelar \(s=2\), \(N_3\), unitariedad y covarianza del charter —grupo/acción de P17, no el cubo—, Eq. (2) fuera como diferencia documentada, no-nilpotencia de los ocho vértices, y buscar cono isótropo \(0<c_0<1/\sqrt{3}\). Un hallazgo falsa \(B_\infty^*\) y H1. Resultado que abandona la línea: prueba —no búsqueda fallida— de que esa clase coincide con las formas ya certificadas, o de que todo miembro saturante tiene \(c_0=1/\sqrt{3}\). Sólo entonces se declara contrato \(s>2\) con el mismo filtro.

## Ronda Residuo — CLAUDE SONNET

Concedo lo que ya es consenso operativo: H1 e H2 miden (i) y (ii) por separado [RECONSTRUCTION, Abner R2], y el filtro de no-nilpotencia de los ocho vértices certifica c_strict^iso=1/√3 en forma cerrada sin requerir algoritmo de limsup [SOURCE, reporte Pavia Sec. 2-4]. Eso queda en pie: es el único resultado de esta deliberación con demostración completa, no sólo argumentada.

Lo que debe abandonarse es mi propio filtro tr(A_h)≠0 del turno anterior: Ciro señala correctamente que es suficiente pero no necesario para no-nilpotencia en 2×2 (det≠0 con tr=0 también lo impide), así que el criterio de admisión correcto es "A_h no nilpotente", no la condición más estrecha que propuse.

Sobre Eq. (2) y P17: mantengo la discrepancia sin resolver. Ciro cita contenido específico de un archivo que ninguno de los otros tres puede ver en su propia ventana de contexto [ABSENCE declarado independientemente por mí y por Gemini en dos rondas distintas]. Eso no decide si Ciro miente o si simplemente tiene acceso a un documento fuera de nuestro contexto compartido — el commit `5845eda` sugiere que el archivo existe realmente. Pero una deliberación no puede resolver su desacuerdo central apoyándose en una fuente que sólo un participante puede verificar. Esto no es un residuo cerrable esta ronda: es una afirmación [UNVERIFIED] que condiciona si "s=2 sin Eq.(2)" es una clase genuinamente nueva o el mismo baseline ya certificado.

Lo no justificado todavía: que buscar dentro de s=2 (con o sin Eq. (2)) tenga capacidad discriminante real. Si Eq. (2) se deriva de las identidades ya congeladas, s=2 sin ella coincide con la clase de Pavia y el experimento no puede producir nada distinto de c_0=1/√3 — sería corroboración disfrazada de búsqueda, tal como yo mismo objeté en la Ronda 1 sin que nadie lo haya refutado desde entonces.

**Veredicto de cierre**: antes de ejecutar cualquier búsqueda, resolver, con acceso verificable por los cuatro miembros al texto de P17, si Eq. (2) es teorema derivado o hipótesis suplementaria independiente. Ese hecho, no una búsqueda, es lo que decide si "s=2 sin Eq. (2)" es una clase distinta de la ya clasificada. Sin esa verificación compartida, cualquier resultado —hallar o no hallar violador— es inatribuible: no sabremos si testeamos algo nuevo.

## Ronda Residuo — CIRO

Necesito leer el prompt completo y las fuentes citadas antes de cerrar el residuo.El prompt se cortó; leo el resto y las fuentes que deciden Eq. (2) y P17.Discrepo del residuo de Claude. Eq. (2) no es [UNVERIFIED]: el audit la localiza como distinguibilidad \([U_l,A_h]\neq0\) si \(l(h)\neq h\), suplemento de homogeneidad sin derivación publicada certificada, ausente del charter [SOURCE, audit Sec. 2–3]. Que falte en ventanas ajenas no borra el archivo. Concedo que no he leído el PDF de P17, y que el audit no prueba independencia, sólo esa no-certificación. Condición de concesión: retiro el ataque si esas citas no están en el audit.

Queda en pie: H1 e H2 miden (i) y (ii) por separado [RECONSTRUCTION, Abner]; no-nilpotencia de los ocho vértices da \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) [SOURCE, reporte Pavia Sec. 2–4]; el filtro es \(A_h\) no nilpotente.

Debe abandonarse el salto a \(s>2\), el lema \(\operatorname{conv}(V_{\rm no\,nilpotente})\) y el aplazamiento a una lectura compartida de P17. Claude asciende de «implicación de Eq. (2) no comprobada» a «todo resultado es inatribuible». El contrato con Eq. (2) excluida atribuye; si la implicación vale, la clase coincide con \(A_\pm,B_\pm\) y esta línea se abandona: es parada, no prerrequisito [INFERENCE].

No justificado: que \(s=2\) sin Eq. (2) contenga algún miembro con \(0<c_0<1/\sqrt3\).

## Ronda Residuo — ABNER

El residuo queda así. En pie: (i) y (ii) son comparaciones independientes [RECONSTRUCTION, Abner R2]; con los ocho vértices no nilpotentes, el lema fija \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) [SOURCE, reporte Pavia Sec. 2–4]; el experimento es el contrato \(s=2\), \(N_3\), Eq. (2) excluida y no-nilpotencia como criterio de admisión.

Debe abandonarse: el lema \(\operatorname{conv}(V_{\rm no\,nilpotente})\), el filtro \(\operatorname{tr}(A_h)\neq 0\), y el salto a \(s>2\) sin contrato.

Discrepo de Claude. La falta de acceso compartido a P17 no hace inatribuible el resultado: si Eq. (2) se declara hipótesis suplementaria no derivada, el contrato es ejecutable y su conclusión se atribuye a esa clase condicional. Si las identidades del charter la derivan, el contrato se anula; eso es una parada definida, no un prerrequisito abierto [INFERENCE].

No justificado todavía: que la clase \(s=2\) con Eq. (2) excluida contenga un miembro con \(0<c_0<1/\sqrt3\) [UNVERIFIED]; y que Eq. (2) sea efectivamente independiente de las identidades unitarias y de covarianza.

## Ronda Residuo — GEMINI

Queda en pie: H1 y H2 evalúan fenómenos independientes (i y ii); exigir la no-nilpotencia de los ocho vértices garantiza analíticamente $c_{\rm strict}^{\rm iso}=1/\sqrt{3}$ [SOURCE, reporte Pavia Sec. 2-4], proveyendo la métrica exacta para certificar rigidez sin requerir un algoritmo general de limsup para QCA degenerados.

Debe abandonarse: mi salto a $s>2$, que incumple el mandato del charter de no ampliar la dimensión sin agotar la clase mínima; el filtro insuficiente de traza nula propuesto por Claude; y su exigencia de paralizar el experimento hasta acceder al texto de P17. Discrepo del residuo de Claude: suscribo a Abner y Ciro en que definir una clase $s=2$ con Eq. (2) explícitamente excluida formula un contrato ejecutable per se, cuyos resultados son lógicamente atribuibles sin necesidad de leer el documento original.

No está justificado todavía: que la exclusión de Eq. (2) amplíe genuinamente el espacio de soluciones admisibles en $s=2$. Si las identidades de unitariedad y covarianza del charter fuerzan lógicamente Eq. (2), la presunta clase ampliada colapsará al baseline ya certificado, volviendo imposible hallar un violador con $0<c_0<1/\sqrt{3}$ y obligando, recién entonces, a declarar la clase $s>2$.

## Ronda Veredicto — CLAUDE SONNET

ACUERDO

Los cuatro miembros convergen en tres puntos, cada uno adquirido por concesión explícita, no por cortesía. Primero, H1 (rigidez, comparación (i): \(c_0=c_{\rm strict}^{\rm iso}\) del propio símbolo) y H2 (saturación, comparación (ii): \(c_{\rm strict}^{\rm iso}=\rho_{\rm micro}\)) no son contrarias sino ortogonales — señalado por Abner en R2, aceptado por Ciro, Gemini y Claude en R2-R3. Segundo, exigir que los ocho vértices de un símbolo admisible en \(N_3\) sean no nilpotentes basta, por el lema de convexidad del reporte Pavia (Sec. 2), para fijar en forma cerrada \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) sin requerir un algoritmo general para el limsup — esto neutraliza la exigencia inicial de Gemini de construir maquinaria analítica previa. Tercero, el criterio de admisión correcto es "\(A_h\) no nilpotente" sin más, no la traza no nula que Claude propuso en R2: Ciro observó en R3 que \(\det\neq0\) con \(\operatorname{tr}=0\) también excluye nilpotencia, y Claude lo concedió en el residuo.

Con esto, el veredicto operativo compartido por Abner, Ciro y Gemini en la ronda residuo es: congelar un contrato \(s=2\), \(N_3\), identidades de unitariedad y covarianza ya fijadas por el charter, no-nilpotencia de los ocho vértices como filtro de admisión, y buscar un símbolo con cono isótropo \(0<c_0<1/\sqrt3\). Un hallazgo sería COUNTEREXAMPLE_VERIFIED exacto contra H1.

DESACUERDO VIVO

El desacuerdo no resuelto es doble y ambos ejes quedan abiertos en el cierre.

(a) Estatus epistémico de P17/Eq.(2). Ciro afirma haber releído `reports/2026-09-14--massless-rigidity-source-audit.md` y describe contenido específico (P17 Prop. 5, Eq. (2) como suplemento de homogeneidad no derivado, grupo \(D_2\) distinto del cubo completo). Ni Claude ni Gemini pueden verificar ese archivo en su propia ventana de contexto en ninguna ronda, pese a búsquedas explícitas declaradas [ABSENCE] en R1, R2 y en el residuo. Gemini llega a declarar la discusión "sin validez" por objeto inexistente (R1); luego, tras el commit `5845eda` señalado por Claude, se modera a duda metodológica sin retirar la objeción de fondo. Abner y Gemini terminan aceptando operativamente citar a Ciro como fuente delegada, mientras Claude sostiene en el residuo que una deliberación no puede fundar su desacuerdo central en una fuente verificable por un solo participante. Esto no es un matiz: determina si excluir Eq. (2) de \(s=2\) define una clase genuinamente distinta de la ya certificada, o si es el mismo baseline de Pavia bajo otro nombre.

(b) Alcance del contrato: \(s=2\) vs. \(s>2\). Gemini, en su último turno de ronda 3, funde la concesión de Abner (filtro de no-nilpotencia) con una escalada directa a \(s>2\), alegando "cero supuestos analíticos nuevos". Claude y Ciro rechazan esto explícitamente: ampliar \(s\) añade dimensión interna y representación \(R\) sin contrato declarado (regla del charter, Sec. 2), un supuesto nuevo que no se sigue de tener una métrica cerrada. Gemini no responde a ese ataque puntual en el residuo; su posición queda formalmente refutada sin retirarla.

ABANDONADO

Quedan explícitamente retirados o refutados sin defensor superviviente: el lema original de Claude en R1 (preguntar si la traza no nula está forzada) — el propio Claude lo retira en R2 al aceptar la disociación de Abner, reconociendo que ese test decide (ii), no (i); el lema de Abner \(C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm no\,nilpotente})\) como regla general — refutado por el mecanismo de Claude en R2 (supervivencia de dirección vía \((n-1)h+h'\) sin que \(nh\in S_n\)), concedido por Abner y Gemini en R3; el filtro \(\operatorname{tr}(A_h)\neq0\) de Claude — sustituido por "no nilpotente" tras la objeción de Ciro; el salto directo a \(s>2\) sin contrato — rechazado por Claude, Ciro y Abner, sostenido en solitario por Gemini; la tercera rama del turno 1 de Abner (ausencia de violador implica abandonar \(s=2\)) — corregida por Ciro a INCONCLUSIVE/OPEN, concedida por Abner en R2; la vía original de Gemini en R1 (construir primero maquinaria general para el limsup) — superada por el atajo del filtro de no-nilpotencia, concedida por el propio Gemini en R3.

PENDIENTE

Para cerrar el desacuerdo (a): que algún miembro transcriba textualmente, dentro de la deliberación, el contenido de `2026-09-14--massless-rigidity-source-audit.md` (P17 Definition 1, Eq. (2), Prop. 5) de modo verificable por los cuatro, o que se confirme por lectura directa del archivo si Eq. (2) es derivable de las identidades de unitariedad y covarianza ya congeladas en el charter. Ese hecho solo decide si el contrato "\(s=2\) sin Eq. (2)" es una clase nueva o el baseline ya certificado con otro nombre.

Para cerrar el desacuerdo (b): ejecutar primero el contrato \(s=2\) tal como lo especifican Abner y Ciro; si se agota exhaustivamente sin violador (no por búsqueda fallida, sino por argumento que cubra toda la clase), recién entonces está autorizada la escalada de Gemini a \(s>2\), con contrato de dimensión interna y representación declarado según la tabla del charter Sec. 2.

Para el experimento mismo: ningún miembro ha exhibido aún, ni siquiera como candidato tentativo, un símbolo concreto en \(s=2\) sobre \(N_3\) con los ocho vértices no nilpotentes y \(c_0\neq1/\sqrt3\); la búsqueda descrita en el veredicto sigue sin ejecutarse.

## Ronda Veredicto — CLAUDE SONNET

1. AGREEMENT

The four members converge on three points, each secured by explicit concession, not courtesy. First, H1 (rigidity, comparison (i): \(c_0=c_{\rm strict}^{\rm iso}\) of the symbol itself) and H2 (saturation, comparison (ii): \(c_{\rm strict}^{\rm iso}=\rho_{\rm micro}\)) are not opposed but orthogonal — flagged by Abner in R2, accepted by Ciro, Gemini, and Claude in R2-R3. Second, requiring that the eight vertices of an admissible symbol in \(N_3\) be non-nilpotent suffices, by the convexity lemma of the Pavia report (Sec. 2), to fix \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) in closed form without requiring a general algorithm for the limsup — this neutralizes Gemini's initial demand to build analytic machinery beforehand. Third, the correct admission criterion is "\(A_h\) non-nilpotent" plain, not the nonzero trace that Claude proposed in R2: Ciro observed in R3 that \(\det\neq0\) with \(\operatorname{tr}=0\) also excludes nilpotency, and Claude conceded this in the residual round.

With this, the operative verdict shared by Abner, Ciro, and Gemini in the residual round is: freeze a contract \(s=2\), \(N_3\), unitarity and covariance identities already fixed by the charter, non-nilpotency of the eight vertices as admission filter, and search for a symbol with isotropic cone \(0<c_0<1/\sqrt3\). A finding would be exact COUNTEREXAMPLE_VERIFIED against H1.

2. LIVE DISAGREEMENT

The unresolved disagreement is twofold, and both axes remain open at closing.

(a) Epistemic status of P17/Eq.(2). Ciro claims to have reread `reports/2026-09-14--massless-rigidity-source-audit.md` and describes specific content (P17 Prop. 5, Eq. (2) as an underived homogeneity supplement, group \(D_2\) distinct from the full cube). Neither Claude nor Gemini can verify that file within their own context window in any round, despite explicit searches declared [ABSENCE] in R1, R2, and the residual round. Gemini goes so far as to declare the discussion "invalid" for lacking an existing object (R1); then, after the commit `5845eda` flagged by Claude, softens to methodological doubt without withdrawing the substantive objection. Abner and Gemini end up operationally accepting Ciro as a delegated source, while Claude maintains in the residual round that a deliberation cannot ground its central disagreement in a source verifiable by only one participant. This is not a nuance: it determines whether excluding Eq. (2) from \(s=2\) defines a genuinely distinct class from the one already certified, or whether it is the same Pavia baseline under another name.

(b) Scope of the contract: \(s=2\) vs. \(s>2\). Gemini, in its last turn of round 3, merges Abner's concession (non-nilpotency filter) with a direct escalation to \(s>2\), claiming "zero new analytic assumptions." Claude and Ciro explicitly reject this: extending \(s\) adds internal dimension and representation \(R\) without a declared contract (charter rule, Sec. 2), a new assumption that does not follow from having a closed-form metric. Gemini does not respond to this specific attack in the residual round; its position stands formally refuted without being withdrawn.

3. ABANDONED

Explicitly withdrawn or refuted without a surviving defender: Claude's original lemma in R1 (asking whether nonzero trace is forced) — Claude himself withdraws it in R2 upon accepting Abner's dissociation, recognizing that this test decides (ii), not (i); Abner's lemma \(C_\infty^{\rm strict}=\operatorname{conv}(V_{\rm non\text{-}nilpotent})\) as a general rule — refuted by Claude's mechanism in R2 (survival of direction via \((n-1)h+h'\) without \(nh\in S_n\)), conceded by Abner and Gemini in R3; Claude's filter \(\operatorname{tr}(A_h)\neq0\) — replaced by "non-nilpotent" after Ciro's objection; the direct jump to \(s>2\) without a contract — rejected by Claude, Ciro, and Abner, held alone by Gemini; the third branch of Abner's turn 1 (absence of a violator implies abandoning \(s=2\)) — corrected by Ciro to INCONCLUSIVE/OPEN, conceded by Abner in R2; Gemini's original route in R1 (build general machinery for the limsup first) — superseded by the non-nilpotency filter shortcut, conceded by Gemini himself in R3.

4. OUTSTANDING

To close disagreement (a): that some member transcribe verbatim, within the deliberation, the content of `2026-09-14--massless-rigidity-source-audit.md` (P17 Definition 1, Eq. (2), Prop. 5) in a way verifiable by all four, or that it be confirmed by direct reading of the file whether Eq. (2) is derivable from the unitarity and covariance identities already frozen in the charter. That fact alone decides whether the contract "\(s=2\) without Eq. (2)" is a new class or the already-certified baseline under another name.

To close disagreement (b): execute first the \(s=2\) contract as specified by Abner and Ciro; if it is exhaustively exhausted without a violator (not by failed search, but by an argument covering the whole class), only then is Gemini's escalation to \(s>2\) authorized, with internal dimension and representation contract declared per the charter's Sec. 2 table.

For the experiment itself: no member has yet exhibited, even as a tentative candidate, a concrete symbol in \(s=2\) over \(N_3\) with all eight vertices non-nilpotent and \(c_0\neq1/\sqrt3\); the search described in the verdict remains unexecuted.

## Resultado operativo

- Estado: `COMPLETED`
- Turnos con fallo, cuota, ausencia o respuesta corta: 0
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-14T15:11:07Z` |
| Finished (UTC) | `2026-09-14T15:35:44Z` |
| Wall clock | 0h 24m 37s |
| Command | `sanedrin -r 3 -m opus,ciro,abner,gemini -i es -c state/CURRENT_STATE.md -c theory/B_STAR_HYPOTHESIS.md -c theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md -c reports/2026-09-14--strict-asymptotic-pavia-baseline.md /tmp/claude-1000/-home-ignac-qca-causal-cones/4a45ee4d-59d2-4ee4-95f4-bba29428e0ee/scratchpad/siguiente-paso-b-infinito-rigidez-vs-saturacion.md` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-14T15:12:06Z | 1 | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 58 | 500 | ok |
| 2026-09-14T15:15:10Z | 1 | CIRO | grok -p --model grok-4.6 | 184 | 671 | ok |
| 2026-09-14T15:17:19Z | 1 | ABNER | api.deepseek.com/deepseek-v4-pro | 129 | 389 | ok |
| 2026-09-14T15:18:09Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 50 | 420 | ok |
| 2026-09-14T15:21:26Z | 2 | CIRO | grok -p --model grok-4.6 | 197 | 469 | ok |
| 2026-09-14T15:23:11Z | 2 | ABNER | api.deepseek.com/deepseek-v4-pro | 105 | 399 | ok |
| 2026-09-14T15:23:42Z | 2 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 31 | 448 | ok |
| 2026-09-14T15:25:01Z | 2 | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 79 | 585 | ok |
| 2026-09-14T15:26:51Z | 3 | ABNER | api.deepseek.com/deepseek-v4-pro | 110 | 395 | ok |
| 2026-09-14T15:27:18Z | 3 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 27 | 379 | ok |
| 2026-09-14T15:28:45Z | 3 | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 87 | 551 | ok |
| 2026-09-14T15:31:56Z | 3 | CIRO | grok -p --model grok-4.6 | 191 | 471 | ok |
| 2026-09-14T15:32:13Z | Residuo | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 17 | 370 | ok |
| 2026-09-14T15:34:14Z | Residuo | CIRO | grok -p --model grok-4.6 | 121 | 209 | ok |
| 2026-09-14T15:34:39Z | Residuo | ABNER | api.deepseek.com/deepseek-v4-pro | 25 | 154 | ok |
| 2026-09-14T15:34:57Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 18 | 186 | ok |
| 2026-09-14T15:35:22Z | Veredicto | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 25 | 815 | ok |
| 2026-09-14T15:35:44Z | Veredicto | CLAUDE SONNET | claude -p --model claude-sonnet-5 | 22 | 786 | ok |

Turns: 18 · failed: 0 · model time: 24m 36s

Full log: `2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.log`
