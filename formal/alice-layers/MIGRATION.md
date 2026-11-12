# Migration record — 2026-11-12

This directory was moved here from the auxiliary tools repository, at the
user's instruction (2026-11-12: the tools repository helps the others; work
is not done inside it).

- Origin: `~/herramientas`, commit `2a7342b`, path
  `ai_scientist_local/experiments/alice_layers/formalization/`.
- Copied: the 997 tracked files, byte-identical (SHA256 of every file
  checked against the origin before any edit). `build/` was not copied.
- Edited after the copy, paths only:
  - `build.py`, `verify.py`: `PACKAGES` now `HERE.parent/'.lake/packages'`
    (the Mathlib cache of `formal/`), instead of the absolute path;
  - `verify.py`: the shared `AssertAxioms.lean` is read from
    `~/herramientas/lean/HerramientasLean/AssertAxioms.lean` instead of a
    path relative to the old location;
  - `lakefile.toml`: Mathlib path `../.lake/packages/mathlib`.
- Not edited: every `.lean` file, the comparators, the mutation
  inventories, the generators and all records under `verification/`.

## What the older documents in this directory refer to

They were written in the old location and are kept as written.

- `../runs/run_0/paper.tex` (frozen source, SHA256 `2075e840…c04cc4`) is
  `papers/ir-corona/ir-corona.tex` of this repository at commit `08d5981`
  (branch `research/inverse-gravity-design`). Checked on 2026-11-12:
  `git show 08d5981:papers/ir-corona/ir-corona.tex | sha256sum`.
- Commands that start with
  `ai_scientist_local/experiments/alice_layers/formalization/` are now run
  from this directory: `python3 -I build.py`,
  `python3 -I verify.py --output verification/<new-name>`.
- `runner_sha256` and module hashes in the records made before the
  migration belong to the old `verify.py` and `build.py`.
- The numerical exponent diagnostic and the AI-Scientist trial records of
  the same experiment stay in `~/herramientas` (they depend on that
  controller); they are not part of this formalization.

## Scope, unchanged by the move

The Lean theorem `AliceLayers.aliceLayersB_proved` is the scalar Alice
coefficient of Lemma Layers (b) of the IR-corona manuscript. It does not
cover Bob's coefficient, the matrix symbol, the assembly, the rest of the
lemma or the paper. No external review of the proof or of its fidelity to
the manuscript. See `FIDELITY_ALICE_LAYERS_B.md` and `STATUS.md`.

On 2026-11-12 the manuscript in this branch was reconciled with the
October version
(`reports/2026-11-12--ir-corona-version-reconciliation.md`); the statement
of Lemma Layers there is byte-identical to the frozen source above.

## Verification after the move

See `verification/migration_2026-11-12/verification.json` for the full
compilation from this location. The mutation campaigns were not rerun
after the move.
