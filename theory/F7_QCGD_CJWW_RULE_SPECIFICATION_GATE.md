# F7_QCGD_CJWW_RULE_SPECIFICATION_GATE

**Fecha:** 2026-09-30.
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.
**Rama:** `research/gravitational-normalization-gate`.

## 0. Scope

Successor to the family-atlas F7 preflight:

```text
BRIDGE_QUANTIFIERS_OPEN / EXPLICIT_CJWW_RULE_NOT_SPECIFIED
```

This gate does not derive gravity, compute a metric response, reopen W3-W11,
or promote QCGD to an explicit CJWW bridge. Its only task is to decide whether
there is a concrete, frozen, local unitary rule in the QCGD/dynamical-graph
family that is eligible for the later four-species metric test.

The gate is a specification gate. A negative or open result is useful if it
prevents running metric tests on an undefined family.

## 1. Prior records that constrain this gate

The class-selection record
[`DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md`](DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md)
selected a bounded-degree QCGD-type class but stopped at:

```text
VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED
```

The strong pure-background bridge audit records:

```text
STRONG_EXACT_BRIDGE_IMPOSSIBLE
```

for a fixed pure geometry background and an exact CJWW reduced matter channel
for every matter input at nonzero backreaction. Therefore this gate uses the
conservative W1 escape route: exact CJWW is required at `g=0`; at `g != 0`
the reduced matter channel may be perturbed.

The W1 link-register bridge proves algebraic compatibility of reversible
local backreaction with exact CJWW recovery at zero coupling, but it leaves:

```text
GEOMETRIC_INTERPRETATION = OPEN
FULL_QCGD_SYNTHESIS = OPEN
```

Therefore W1 is an allowed input only as a mechanism, not as an already
accepted geometry rule.

## 2. Frozen target

The flat target remains one-particle CJWW Eq. (5.15) on the original
two-component matter cell over Z3, with the four +I species used in W12.

The admissible rule must specify:

1. the graph/geometry Hilbert space;
2. the matter Hilbert space and how the C2 CJWW cell is embedded;
3. the background graph sector `G0`;
4. whether the calculation is on infinite Z3, finite boxes with a stated
   thermodynamic/local limit, or another explicitly justified sector;
5. the complete one-step unitary `U_F7(g)`;
6. the local decomposition or QCGD causality radius;
7. the geometry observables that are allowed to define metric response;
8. the equivalence relation by which the `g=0` matter step equals CJWW.

No item may be filled in after seeing a metric-universality calculation.

## 3. Eligibility tests

### Q0 — rule specified

There must be a single mathematical definition of `U_F7(g)`, not a prose
description of a possible graph update.

### Q1 — unitarity

`U_F7(g)` must be exactly unitary for the stated Hilbert space and boundary
conditions.

### Q2 — causal/localizable

The rule must be QCGD-causal or given by a bounded-depth bounded-radius local
circuit. If a finite box is used, the bound must be independent of the box
size away from boundary conventions.

### Q3 — exact flat CJWW recovery

At `g=0` and background `G0`, the induced matter update must be exactly CJWW
Eq. (5.15), or locally unitarily equivalent by a specified on-site/unit-cell
equivalence. IR agreement is not enough.

### Q4 — nontrivial geometry-to-matter response

For `g != 0`, at least two admissible local geometry states near `G0` must
induce different reduced matter channels to first nonzero order.

### Q5 — nontrivial matter-to-geometry response

For `g != 0`, at least two admissible matter states with the same initial
geometry state must induce different local geometry observables to first
nonzero order.

### Q6 — geometry interpretation

The observables used in Q4-Q5 must be adjacency, distance, port, embedding,
or another declared graph-geometric object. A spectator link qubit, gauge
field, phase register, or interaction-strength register does not count as
geometry unless the contract gives an operational metric/causal meaning.

### Q7 — no strong-channel contradiction

The rule must not require the exact CJWW reduced matter channel for every
matter input at `g != 0` while also claiming information-bearing
matter-to-geometry backreaction from one pure background. That combination is
already excluded.

## 4. What counts as success

The strongest success state is:

```text
EXPLICIT_F7_RULE_ELIGIBLE_FOR_METRIC_TEST
```

It means only that a rule exists for the next species/universality test. It
does not imply a metric PASS, curvature, Einstein dynamics, stress-energy
source, Newton constant, or novelty.

If Q0-Q5 pass but Q6 remains open, the terminal state is:

```text
LINK_BACKREACTION_RULE_ELIGIBLE / GEOMETRIC_INTERPRETATION_OPEN
```

That state permits algebraic backreaction work but not a claim of dynamical
geometry.

## 5. Terminal states

Apply in order:

1. `NO_RULE_SPECIFIED`.
2. `RULE_NONUNITARY_OR_NONLOCAL`.
3. `FLAT_CJWW_RECOVERY_FAIL`.
4. `NO_NONTRIVIAL_BACKREACTION`.
5. `GEOMETRIC_INTERPRETATION_OPEN`.
6. `LINK_BACKREACTION_RULE_ELIGIBLE / GEOMETRIC_INTERPRETATION_OPEN`.
7. `EXPLICIT_F7_RULE_ELIGIBLE_FOR_METRIC_TEST`.
8. `OPEN_AFTER_AUDIT`.

## 6. Stop rule

If Q0 fails, stop. Do not invent an edge flip, port update, stress law,
Hamiltonian, or metric observable inside the execution report.

If only a W1-style link-register rule is available, record it under Q6 and
do not call it geometry until the operational metric/causal meaning is
specified.

If the rule passes this gate, the next gate must freeze the four-species
metric observable before calculation.
