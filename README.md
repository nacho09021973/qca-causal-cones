# qca-causal-cones

Finite-range quantum cellular automata, microscopic causal bodies, Bernstein bounds, and the emergence of relativistic propagation speeds.

## Project question

The project asks whether a relativistic low-energy propagation speed can be derived from the causal geometry of an underlying finite-range QCA, while keeping distinct three objects that must not be conflated:

1. the microscopic causal body `C_micro`, fixed by locality;
2. the spectral group-velocity envelope `V_grp^max`, fixed by the bands of a specific automaton;
3. the relativistic low-energy speed `c_IR`, fixed by the effective field theory.

The original strong identification `c_IR = maximum microscopic substrate speed` does **not** survive generically in finite-range lattice QCAs for spatial dimension `d >= 2`. Comparison with the one-step inradius was replaced by `B_infty^*`, which compares the massless speed `c_0` with the strict asymptotic isotropic speed `c_strict^iso` of the same dynamics. Its strong form has an explicit counterexample in a declared four-component class. The open question is which additional structural hypotheses, if any, restore the equality.

## Setup on another computer

See the [portability guide](docs/PORTABILIDAD.md) for Python dependencies,
verification, and restoring the git-ignored local library.

## Canonical state

Read [`state/CURRENT_STATE.md`](state/CURRENT_STATE.md) before doing new work. It is the single source of truth for project status, gates, rejected claims, and the next allowed calculation.

## Current reading order — 2026-09-28

1. [State and synchronization summary](state/CURRENT_STATE.md#reading-guide-and-synchronization--2026-09-28):
   accepted scopes, preliminary work, paused fronts, and missing local commits.
2. [Flat CJWW manuscript](papers/ir-corona/ir-corona.tex): the model result.
3. [Independent-use discrimination cost](reports/2026-09-28--iid-message-discrimination-cost.md):
   supplied preliminary derivation, independent review pending.
4. [Existing 4B execution](reports/2026-09-25--physical-realization-absolute-scale-gate.md):
   negative absolute-scale result, with its recorded evidence limitations.

The immediate task is synchronization and review before further research.
The new report does not establish a universal operational boundary at c.

## Literature library

`biblioteca/` (git-ignored) holds the local PDFs. **Before investigating any question, read
`biblioteca/INDICE.md`** (one line per PDF, with subject tags;
`grep -i <topic|keyword> biblioteca/INDICE.md`) and check whether a paper can help. The index
locates papers, it proves nothing: read the PDF and cite `file.pdf p.N`, otherwise mark the claim
`[UNVERIFIED]`. Tags marked `proposed` were written by an AI. Regenerate the index with
`python3 ~/herramientas/biblioteca_catalog/build_catalog.py --repo .` after editing
`scripts/biblioteca_catalog/curated.csv`.

## Method rule

No result is promoted from exploratory to canonical merely because it fits the current narrative. Every claimed identity must be checked against the exact QCA geometry, exact unitary spectrum, and the appropriate low-energy expansion.

## Verified standard Weyl/Dirac gate

The [execution contract](reports/2026-09-14--weyl-dirac-gate-contract.md),
[exact derivation](reports/2026-09-14--weyl-dirac-exact-gate.md), and
[reproducible verification](reports/2026-09-14--weyl-dirac-verification.md)
cover the seven declared standard symbols in d=1,2,3 and their Dirac couplings.
**STANDARD WEYL/DIRAC EXACT GATE: PASS.** The evidence baseline is `2c7c2c9`;
the [promotion record](reports/2026-09-14--standard-gate-promotion.md) explains
the canonical status change. The original reports retain their historical
pre-promotion wording and provenance.

Massless and continuum inradius matching are verified for the declared
standard family; exact finite-mass matching is rejected for both `c_H` and
`c_{ω^2}`. Generality and inter-species universality remain open. The seven
symbols share three dimension-specific geometries.

## Status after the s=4 counterexample

The records below originated on `research/b-infinity-post-s4-gate` and are
present in the September 28 remote main baseline. Their scientific scope
and evidence levels remain those recorded in `state/CURRENT_STATE.md`.

The [MASSLESS INRADIUS RIGIDITY GATE](theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
is historical. It was completed by an explicit
[s=4 strict-cone counterexample](theory/S4_STRICT_CONE_COUNTEREXAMPLE.md)
with an [independent review](reports/2026-09-15--s4-independent-review.md)
and a [prior-art audit](reports/2026-09-15--s4-family-prior-art-audit.md).

- Strong `B_infty^*` is **REJECTED IN THE DECLARED s=4 CLASS**.
- The standard Pavia `s=2`, d=3 equality `c_0 = c_strict^iso = 1/sqrt(3)`
  remains **CERTIFIED** and is not affected.
- Rigidity in the published minimal `s=2` class, and in stronger classes with
  additional representation assumptions, remains **OPEN**.
- **NOVELTY remains OPEN.**
- This is the historical s=4 summary. Later authorizations and stops are
  recorded in [`state/CURRENT_STATE.md`](state/CURRENT_STATE.md), Sections 8–10.
  Use its reading guide before continuing; this documentation update opens
  no new scientific gate.
