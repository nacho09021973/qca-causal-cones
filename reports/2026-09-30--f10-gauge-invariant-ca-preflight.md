# F10 gauge-invariant CA preflight

Date: 2026-09-30.

## 1. Question

Can Arrighi--Costes--Eon gauge-invariant cellular automata be entered as a
new atlas family, and what is their admissible status for the CJWW
matter-geometry programme?

This is a source preflight. It does not construct a QCA, identify a metric
observable, or execute a four-species CJWW test.

## 2. Primary source read

Primary local PDF:

```text
biblioteca/arXiv-2102.06912.pdf
```

Read pages: pp.1-14. The local PDF checksum is:

```text
c44d21281318b1340aa4336c02306a18b2326128452ce6e7d751fc62db721b20
```

## 3. Source facts retained

The abstract on p.1 states that the paper formalizes gauge extension in the
cellular automata setting. It also states two main structural results:

- cellular automata admitting relative gauge extension are exactly the
  globally symmetric, or colour-blind, ones;
- every cellular automaton admits a non-relative gauge extension.

Pp.2-4 define CA, global symmetry, local gauge transformations,
gauge-invariant CA and gauge extension. Definition 2.7 gives the general
gauge-extension condition: an extended CA must simulate the original CA under
the chosen gauge initialization and must commute with local gauge changes.

Pp.5-6 define relative gauge extension. In that case, gauge fields live on
links and record the relative gauge relation between neighbouring cells.

Pp.6-7 prove the relative theorem: a CA has a relative gauge extension with
identity gauge-field evolution exactly when it is globally symmetric.

P.8 proves that every CA admits a gauge extension in the more general,
non-relative sense. In that construction the gauge field is not a link field
of the relative type.

P.9 records universality consequences for gauge-invariant CA. Pp.9-12 give a
reversible example in which the matter field influences the gauge field and
the gauge field influences the matter field. The text also records a limit:
the constructed gauge-extended CA simulates the original CA for one step from
the empty gauge initialization, but the gauge field generally no longer remains
empty afterwards.

The conclusion on p.12 says that finding a relative gauge extension with
similar two-way matter/gauge influence remains open. It also points to the
quantum cellular automaton for one-dimensional QED as a quantum analogue, but
that paper was not read in this preflight and is not used here as evidence.

## 4. Relation to existing in-repo records

The 2026-09-29 model-class selection already used gauge-invariant CA/QCA
constructions only as evidence that matter plus link variables can be coupled
by local/reversible discrete dynamics. It explicitly did not reinterpret those
links as geometry.

F10 makes that separation explicit in the atlas:

- gauge/link variables are a serious discrete architecture;
- gauge/link variables are not automatically metric, tetrad, embedding or
  graph geometry;
- a future constructive family must declare the geometric observable before
  using such links in a gravity gate.

## 5. Kill tests for atlas status

### F10.1 — independent identity

Is this family distinct from QCGD, Gu-Wen and Pretko?

Result: PASS. F10 is about gauge extension of CA rules and link/absolute gauge
fields. QCGD is graph dynamics; Gu-Wen and Pretko are tensor-constraint and
rank-2 gauge architectures.

### F10.2 — local gauge architecture

Does the source provide a formal local gauge-extension framework?

Result: PASS. Definitions 2.7 and 2.8 give general and relative gauge
extension, and the theorems characterize the relative case and existence of
the non-relative case.

### F10.3 — sourcing matter/gauge

Does the source provide a discrete example where matter and gauge fields
influence each other?

Result: PASS for the non-relative reversible CA example on pp.9-12. The
relative analogue remains OPEN in the source conclusion.

### F10.4 — direct CJWW/QCA bridge

Does the source provide an exact two-component CJWW walk, QCA update, Weyl
species, flat CJWW limit, or metric response?

Result: FAIL/ABSENT. The read paper is a CA gauge-extension paper. It is not a
CJWW/QCA geometry construction.

### F10.5 — geometry/gauge separation

Can the link variables be counted as geometry for this project?

Result: FAIL/ABSENT. They are gauge variables unless a new contract defines and
tests a metric or frame observable.

## 6. Verdict

```text
F10_GAUGE_INVARIANT_CA_PREFLIGHT =
GAUGE_EXTENSION_CA_ARCHITECTURE_PRIOR_ART /
DIRECT_CJWW_QCA_BRIDGE_ABSENT
```

Evidence level: primary-source preflight. No independent review.

## 7. Consequence

F10 is useful for future rule design, especially any family that introduces
link variables and wants local matter/gauge feedback. It is not a gravitational
family by itself. The admissible next use would be a new contract that states
which variables are gauge, which are geometry, what observable extracts a
metric or frame, and how the rule reduces to CJWW in a fixed flat sector.
