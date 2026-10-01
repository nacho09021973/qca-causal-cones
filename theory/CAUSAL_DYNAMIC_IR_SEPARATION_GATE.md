# Causal, dynamic and infrared separation gate

**Initial status:** `OPEN / CONTRACT_ONLY / NO_EXECUTION_AUTHORIZED`
**Date:** 2026-10-01
**Branch:** `transfer/causal-dynamic-ir-gate`

This charter imports a methodological distinction from the causal-fidelity
audit without importing causal-set or Schwarzschild claims. It is a scope gate
for future QCA successors.

## 1. Mandatory observables

Keep the following objects distinct:

- `C_micro`: the finite-range microscopic causal body fixed by locality;
- `V_causal^max`: its directional support bound;
- `V_grp^max`: the maximum group velocity realized by the declared QCA spectrum;
- `c_IR`: the speed parameter of the declared low-energy effective theory;
- `D_dyn`: a response or geometry change produced by an explicit state update.

`C_micro` and the first three quantities are not a dynamical geometry. A
coarse metric or tetrad extracted from a state-dependent symbol is not yet a
backreacting geometry. A result must say which of these objects it addresses.

## 2. Frozen common baseline

Before any successor calculation, freeze:

- lattice/support and its dimensionless normalization;
- internal dimension, representation, species/nodes and momentum sector;
- the unperturbed unitary and time-step convention;
- the state space and admissible geometry states;
- the source, perturbation, detector and observable;
- the scale and order of limits;
- exact PASS, FAIL and STOP rules.

The hidden embedding may score a declared observable only when the contract
allows it. It may not select, tune or interpret the observable.

## 3. One-variable ablation matrix

For a proposed elastic or dynamic-graph successor, use this minimum matrix:

| Row | Support | Unitary/rule | Geometry state | Purpose |
|---|---|---|---|---|
| A | frozen | baseline | flat/reference | reproduce the control |
| B | frozen | candidate rule | flat/reference | isolate rule algebra and unitarity |
| C | frozen | candidate rule | one frozen deformation | test the intended response |
| D | frozen | candidate rule | admissible control deformation | test species universality |
| E | frozen | candidate rule | time-dependent geometry, only if chartered | test genuine geometry dynamics |

Rows may not change support, species, normalization and rule simultaneously.
If Row B fails unitarity or is orientation-dependent, stop before any metric or
four-species calculation. If Row C changes only a common embedding while the
unitary remains unchanged, label the result `KINEMATIC_EMBEDDING_ONLY`.

## 4. Gate sequence

### Q0 — rule completeness

Specify the full local update `U(g)`, including every orientation, inverse,
ancilla and geometry-state transition. A family name or a representation
theorem is not a rule.

### Q1 — exact local validity

Certify locality, unitarity, symmetry/conservation assumptions and the frozen
support. The verifier must fail closed. No metric test runs after a Q1 failure.

### Q2 — kinematic/dynamic separation

Show separately whether the candidate changes only the embedding/symbol or
whether it changes a state-dependent local update. Record `D_dyn = OPEN` when
there is no explicit response kernel or geometry-state evolution.

### Q3 — species and metric response

Only after Q0–Q2, run the declared multi-species response test. A rank or
universality result is scoped to the frozen controls and is not a gravity
claim. Missing directions, common kernels and gauge relations must be reported.

### Q4 — infrared comparison

Compare `V_grp^max` and `c_IR` only after their definitions and limits match.
For massive sectors, do not identify `c_IR` with `|∇ω(0)|` or with the
coefficient extracted from `ω²` without an independent proof.

## 5. Verdict vocabulary and ceilings

Use named states:

- `NO_RULE_SPECIFIED`;
- `UNITARY_RULE_INCONSISTENT`;
- `KINEMATIC_EMBEDDING_ONLY`;
- `DYNAMIC_RESPONSE_OPEN`;
- `UNIVERSAL_SUBFAMILY_DEFICIENT`;
- `OPEN_AFTER_AUDIT`;
- `PASS_UNDER_FROZEN_CONTRACT`.

None of these states establishes Einstein dynamics, a universal gravitational
source, a natural substrate, or a general QCA theorem. The existing W12
closure and its scope remain unchanged. A successor may not rescue a failed
rule by changing orientation conventions, species, support or controls after
the result is known.

## 6. Evidence and reopening

The charter is contract-only. Execution requires a separate user authorization
and a permanent verifier in `scripts/`, a report in `reports/`, and an explicit
state update after review. Any retained result must record the charter commit,
verifier commit and claim ceiling.

Reopening a stopped row requires a dated addendum naming the exact failed
obligation and the physically motivated replacement. It does not reopen W9–W12
automatically.
