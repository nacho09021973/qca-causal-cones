# Handoff to another local PC — 2026-11-13

User requested publication of every updated local branch to GitHub.
Repository: `https://github.com/nacho09021973/qca-causal-cones.git`.
The current research branch is
`research/tetrahedral-support-rigidity-2026-11-09`.

## Resume

```sh
git clone https://github.com/nacho09021973/qca-causal-cones.git
cd qca-causal-cones
git switch research/tetrahedral-support-rigidity-2026-11-09
```

A normal clone fetches remote-tracking refs for all published branches;
it does not check all of them out. List them with `git branch -r`, then
use `git switch <branch>` to work on another one. In an existing clone,
fetch first (`git fetch origin --prune`), inspect the working tree, and
fast-forward the selected branch only after preserving local edits.
No force reset is required for this handoff.

Read `PROJECT_INSTRUCTIONS.md`, `state/CURRENT_STATE.md` and the applicable
shared rules before resuming scientific work. The canonical state is
branch-local; this publication does not merge research into main.

## Scientific checkpoint

- Active-protocol admissibility was promoted in its bounded scope at
  `46114c0`, with one independent Claude review and later exposition edits
  explicitly not re-reviewed. The B1 rate link remains conditional.
- W6 exact-example preflight stopped at `374ff6a`: a scalar-shift carrier
  symmetry gives a phase dependence incompatible with the old H6_k(ii).
  86 exact algebra checks passed. The analytic result is PRELIMINARY,
  unreviewed and unpromoted; not a no-go for physical signal or rate.
- `theory/W6_RESONANT_CARRIER_GATE.md` is the successor **DRAFT**.
  It preserves the same walk, geometry and resource and targets the
  complete joint signal with resonant cross terms. It is not frozen or
  executed. The prior obstruction review and a review of any new result
  are distinct assignments. No external review has been sent for it.

## Branch and worktree scope

At the initial live comparison, all 15 local branches matched same-named
GitHub heads. The pending resonant draft and its state entry are included
in this handoff commit on the current research branch. All local heads
are pushed and compared again with `git ls-remote --heads origin` after
the commit; completion is reported only after that comparison.

The two additional worktrees, `.worktrees/massive-vgrp-bcc` and
`.worktrees/transfer-causal-dynamic-ir`, had clean tracked/untracked
status. Their branches are published; a clone does not recreate the
local worktree directories automatically. They are optional working
layouts, not additional unpublished projects.

## Files and environment outside a GitHub clone

The live ignored-directory inventory contains `biblioteca/`,
`formal/.lake/`, `formal/alice-layers/build/`, `scripts/__pycache__/` and
the local `.worktrees/` layouts. They are not uploaded by pushing branches.
In particular the local literature library needs a separate copy if it
is required on the other PC. Do not infer a complete library from the
versioned `sources/` directory. Build caches can be recreated as needed.
Shared tools under `~/herramientas` and credentials are outside this repo.

The Python requirements file fixes `sympy==1.14.0` and `numpy==1.26.4`.
The last exact W6 verifier run used Python 3.12.3. Install dependencies
in a suitable environment on the new PC; no fresh-machine installation
has been tested during this handoff.
