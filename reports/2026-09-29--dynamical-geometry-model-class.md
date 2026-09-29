# DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE — execution

**Fecha:** 2026-09-29.  
**Contrato:** [DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE](../theory/DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md), frozen at commit `abfa341a30cd71ae2b6e130b387808a85f3b5a06`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE =
VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED
```

The viable class is a **bounded-degree Quantum Causal Graph Dynamics
(QCGD)-type model with joint local matter/graph unitaries and a required
fixed-background CJWW sector**. This is a model-class specification, not an
explicit theory and not a published theorem that gravity emerges.

## 1. Candidate A — Quantum Causal Graph Dynamics

Primary source:

P. Arrighi and S. Martiel, *Quantum causal graph dynamics*,
Phys. Rev. D 96, 024026 (2017), arXiv:1607.06700.

The source supplies the cleanest kinematic base for the successor:

- discrete time;
- global unitary causal evolution;
- quantum systems on graph nodes;
- the graph itself belongs to the evolving quantum state and may be in a
  superposition of graphs;
- causal unitaries admit a finite-depth local-unitary decomposition.

Therefore, at the level of model class:

```
M1 unitary discrete update: PASS
M2 causal/localizable: PASS
M3 genuine graph dynamics allowed: PASS
```

QCGD does **not** choose a particular matter-to-geometry backreaction law or
an Einstein-Hilbert continuum limit. M4-M6 are not supplied automatically by
the formalism.

## 2. Candidate B — evolving-graph Bose-Hubbard model

Primary source:

A. Hamma, F. Markopoulou, S. Lloyd, F. Caravelli, S. Severini and
K. Markstrom, *A quantum Bose-Hubbard model with an evolving graph as a toy
model for emergent spacetime*, Phys. Rev. D 81, 104032 (2010),
arXiv:0911.5075.

This model supplies the missing physical precedent for backreaction:

- link/adjacency variables are quantum degrees of freedom;
- matter hopping is conditioned by link state;
- an exchange term converts matter quanta into an edge and the inverse
  process converts an edge into matter quanta;
- matter and graph degrees become entangled.

Thus it explicitly realizes the two logical directions required by M4 and M5:
geometry affects matter propagation, and matter affects the graph.

However, it is Hamiltonian/continuous-time toy-model dynamics on an evolving
interaction graph, not the discrete-time frozen CJWW QCA. It is therefore
**precedent for the coupling mechanism**, not the successor model itself.

## 3. Supporting architecture — local link fields in cellular automata/QCA

Two additional sources show that local link variables coupled to matter are
compatible with reversible/local discrete dynamics:

- P. Arrighi, M. Costes, N. Eon, *Universal gauge-invariant cellular
  automata*, MFCS 2021, arXiv:2102.06912: gauge fields may live on links and
  mediate interactions while reversibility is preserved.
- K. Sellapillay, P. Arrighi, G. Di Molfetta, *A discrete relativistic
  spacetime formalism for 1+1-QED with continuum limits*, Sci. Rep. 12, 2198
  (2022): a QCA circuit of unitary gates couples fermionic matter to a U(1)
  gauge field on links and has the expected QED/Dirac continuum limits.

These are **not geometric models**. A gauge link is not a distance, adjacency
or metric variable. They are used only as evidence that the local
matter-plus-link architecture is technically compatible with unitary QCA
evolution.

## 4. Minimal viable successor class

The selected class is therefore:

[
oxed{
	ext{bounded-degree QCGD}
+
	ext{joint local graph/matter gates}
+
	ext{fixed CJWW background sector}
}
]

with fixed vertex number at the first stage.

This class preserves the architectural commitments that matter to the present
project:

1. discrete-time unitarity;
2. bounded-speed causality;
3. finite-depth localizability;
4. geometry as a quantum variable;
5. possible bidirectional matter/geometry coupling.

No vertex creation/destruction is required for the first bridge.

## 5. The unresolved hard condition — M6

No checked source provides an explicit local gate set satisfying simultaneously:

- a dynamical bounded-degree graph sector;
- nontrivial matter-to-graph backreaction;
- graph-dependent matter propagation;
- and an invariant regular-background sector whose exact one-step matter
  symbol is CJWW Eq. (5.15), or is locally unitarily equivalent to it.

Therefore:

```
M4 backreaction: EXISTS AS PRIOR-ART MECHANISM, NOT YET IN CJWW BRIDGE
M5 geometry affects matter: EXISTS AS PRIOR-ART MECHANISM
M6 exact fixed-background CJWW sector: OPEN / NOT CONSTRUCTED
M7 bounded local complexity: COMPATIBLE AS A CLASS RESTRICTION
```

A failed literature search is not used as a novelty claim.

## 6. Stop-rule application

The charter forbids inventing an edge-flip rule inside this gate.

Accordingly the terminal state is

[
oxed{
	exttt{VIABLE\_MODEL\_CLASS\_IDENTIFIED /
EXPLICIT\_BRIDGE\_NOT\_CONSTRUCTED}
}
]

and not `EXPLICIT_DG_QCA_BRIDGE_CONSTRUCTED`.

## 7. Consequence for the research programme

The next mathematical object is now precise.

One would need a local unitary rule `U_DG` acting jointly on bounded-degree
graph/link variables and the two-component matter field such that:

1. on a frozen regular graph state (|G_0\rangle), the matter update is
   exactly CJWW (5.15);
2. off (|G_0\rangle), local graph variables alter the matter walk;
3. local matter state can alter graph variables reversibly;
4. the total update remains causal and finite-depth;
5. (|G_0\rangle) is not destroyed merely by the vacuum/background matter
   sector.

Constructing or proving impossible such a rule is a **separate successor
gate**. Only after it exists would it make sense to reopen
`GRAVITATIONAL_NORMALIZATION_GATE` at G0 and ask for G1.

No claim about Einstein dynamics, Newton's constant, AdS/CFT, absolute scale
or nature follows from this class-selection result.
