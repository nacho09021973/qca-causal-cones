# DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE

**Fecha:** 2026-09-29.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Scope

Successor to
`GRAVITATIONAL_NORMALIZATION_GATE = BLOCKED_NO_DYNAMICAL_GEOMETRY`.

This gate does **not** derive gravity, choose a Hamiltonian, calculate an
Einstein-Hilbert coefficient, reopen E/H1, or modify the flat corona theorem.

Its only task is to identify the smallest defensible dynamical model class in
which a later gravitational-normalization calculation could even be posed.

## 1. Single question

Is there a published or minimally extended QCA-like model class that can
simultaneously satisfy:

1. discrete-time unitary evolution;
2. exact causal locality / finite-depth localizability;
3. quantum dynamical geometry rather than a prescribed background;
4. matter-to-geometry backreaction;
5. a fixed-geometry sector capable, in principle, of reproducing the frozen
   CJWW (5.15) matter walk?

The gate selects a **class**, not a particular theory of nature.

## 2. Literature candidates frozen by preflight

### A. Quantum Causal Graph Dynamics (QCGD)

Arrighi and Martiel, Phys. Rev. D 96, 024026 (2017),
arXiv:1607.06700.

Established by the source:

- graph carries quantum systems at its nodes;
- global evolution is discrete-time, unitary and causal;
- the graph itself is part of the evolving quantum state and may be in
  superposition;
- the dynamics admits a finite-depth local-unitary decomposition.

The framework supplies dynamical quantum geometry and QCA-compatible
kinematics. It does not, by itself, select a particular matter/graph
backreaction rule or an Einstein-Hilbert continuum limit.

### B. Evolving-graph Bose-Hubbard model

Hamma, Markopoulou, Lloyd, Caravelli, Severini and Markstrom,
Phys. Rev. D 81, 104032 (2010), arXiv:0911.5075.

Established by the source:

- graph links are quantum degrees of freedom;
- matter hopping depends on the link state;
- exchange terms convert matter quanta into links and links into matter
  quanta;
- matter and geometry become entangled.

This is an explicit precedent for bidirectional matter/geometry coupling.
It is Hamiltonian/continuous-time toy-model dynamics, not the frozen
discrete-time finite-range CJWW walk.

### C. Gauge-coded QCA / copy-time geometry

Mohamed Sacha, Quantum Reports 8, 33 (2026).

The strictly local QCA/copy-time part is relevant background. Its gravity
closure is explicitly downstream and model-dependent; it is not imported as
a proved microscopic gravitational normalization for the present project.

## 3. Required successor class

Call a candidate class `DG-QCA` (dynamical-geometry QCA) for this gate only.
The label creates no new theory.

A member must have a Hilbert space containing both

[
mathcal H_{\rm geom}otimesmathcal H_{\rm matter},
]

where (mathcal H_{\rm geom}) resolves local adjacency/link variables.

One complete update `U` must satisfy:

### M1 — unitary discrete update
[
U^dagger U=UU^dagger=I.
]

### M2 — causal/localizable
`U` is a QCGD-type causal dynamics admitting a bounded-depth product of
bounded-radius local unitaries.

### M3 — genuine geometry update
At least one local geometric observable `G_e` is not conserved identically:
[
U^dagger G_e U
e G_e
]
for some admissible state/edge.

### M4 — backreaction
The geometry update must depend on matter. A sufficient operational witness is
two matter states (\rho_m,\rho'_m) with the same initial geometry state such
that after one or finitely many updates some local geometric expectation
differs:
[
operatorname{tr}[G_e U(\rho_gotimes\rho_m)U^dagger]

e
operatorname{tr}[G_e U(\rho_gotimes\rho'_m)U^dagger].
]

### M5 — geometry affects matter
Conversely, two admissible local graph configurations must induce different
matter evolution. This prevents a spectator geometry register.

### M6 — fixed-background CJWW sector
There must exist a translation-invariant graph/background sector (mathcal G_0)
and a matter subspace on which the induced one-step matter symbol is exactly,
or by an explicitly proved local unitary equivalence, CJWW Eq. (5.15).

No approximate continuum matching counts for M6.

### M7 — bounded local complexity
For the first construction, vertex number is fixed and local graph degree is
uniformly bounded. Vertex creation/destruction is excluded until a separate
gate is authorized.

This deliberately avoids importing the harder size-varying graph problem.

## 4. What counts as a model-class solution

The gate may close positively without constructing a specific `U` if the
literature supplies a formalism broad enough for M1-M5 and no theorem blocks
M6. In that case the result is only:

`VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED`.

A stronger result
`EXPLICIT_DG_QCA_BRIDGE_CONSTRUCTED`
requires an actual local gate set or exact update satisfying M1-M7.

## 5. Terminal states

Apply in order:

1. `NO_QCA_COMPATIBLE_DYNAMICAL_GEOMETRY_CLASS`.
2. `VIABLE_KINEMATIC_CLASS_NO_BACKREACTION`.
3. `VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED`.
4. `EXPLICIT_DG_QCA_BRIDGE_CONSTRUCTED`.
5. `OPEN_AFTER_AUDIT`.

No state above implies Einstein dynamics, AdS/CFT, a Newton constant,
an absolute lattice scale, or nature.

## 6. Stop rule

At this gate do not invent coupling constants, fit continuum gravity, or choose
a particular edge-flip rule merely because one can write one down.

If the class is viable but an explicit CJWW-preserving backreaction rule is
not already established, stop at
`VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED`.

A construction is a separate successor gate.
