# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A physics/mathematics research repository, not a software product. Its output is
frozen contracts, derivations, exact verification certificates, reports and
independent reviews about finite-range quantum cellular automata (QCA), their
microscopic causal geometry and the relativistic speed of the low-energy limit.
Most work is textual; code exists only to certify claims.

Because it is a research repo, **process discipline is the load-bearing part**.
A plausible-sounding result written without its contract, its traced code and its
review is a regression here, even if it is correct.

## Read before doing anything

In this order:

1. `PROJECT_INSTRUCTIONS.md` — scope, mandatory distinctions, evidence levels,
   method, novelty discipline, current gate.
2. `state/CURRENT_STATE.md` — **single source of truth** for status, gates, what
   is authorized. If any other file (including this one, `README.md`, a gate
   charter or a report) contradicts it, `CURRENT_STATE.md` wins.
3. `AGENTS.md` — the shared entry point for every AI agent, plus
   `~/herramientas/REGLAS.md`, the cross-repo rules that also apply here.

Before investigating any question, check the literature index:
`grep -i <topic> biblioteca/INDICE.md`. `biblioteca/` is git-ignored and local;
the index only *locates* papers, it proves nothing — read the PDF and cite
`file.pdf p.N`, otherwise tag the claim `[UNVERIFIED]`. Tags marked `proposed`
were written by an AI. Never hand-edit `INDICE.md`; edit
`scripts/biblioteca_catalog/curated.csv` (versioned, with `tags.csv`) and
regenerate with `python3 ~/herramientas/biblioteca_catalog/build_catalog.py --repo .`.
Verified 2026-10-28: `biblioteca/` (with `INDICE.md`) and the generator are both
present on this machine. On a fresh checkout they may not be; `docs/PORTABILIDAD.md`
explains how to restore them. If either is missing, ask the user rather than
inventing a path, and fall back to `sources/` (versioned PDFs with recorded
SHA256) as primary literature.

## Commands

No build system, no test suite, no linter. The verifier scripts *are* the tests.

```sh
pip install -r scripts/requirements.txt          # Python 3.12, sympy==1.14.0, numpy==1.26.4

python3 -B scripts/verify_weyl_dirac_gate.py     # run any verifier from the repo ROOT
python3 -B scripts/verify_<gate>_gate.py         # one gate == one script == one report
```

Every verifier **fails closed**: any failed check or exception exits nonzero.
There is no per-test selection flag; a script is the unit. `scripts/README.md`
documents, per script, which report and gate contract it certifies, how many
checks it runs, and — important — *what it does not certify* (analytic steps
verified by hand in the independent review). Do not cite a script as evidence for
more than its README says it covers.

`verify_weyl_dirac_gate.py --output <path>` writes its record only if all checks
pass. `--diagnostics` output on the Laplace-coefficient verifier is `SUPPORTED`
only and must never feed a terminal state.

Lean 4 formalization of Theorem 4.1 of `papers/ir-corona/ir-corona.tex`:

```sh
cd formal && lake exe cache get && lake build   # Lean v4.31.0 + Mathlib rev fabf563, no sorry
```

`formal/README.md` maps each Lean theorem to its paper statement and lists what
is deliberately *not* formalized (Thm 4.2/4.3, admissibility, `D_B`).

`.claude/settings.json` allowlists each verifier as an **exact** command (both
`python3 scripts/X.py` and `python3 -B scripts/X.py`), never a `python3` wildcard.
When you add a new verifier, add its two exact forms there.

## Layout

| Path | Role |
| --- | --- |
| `state/CURRENT_STATE.md` | canonical status; ~1800 lines, sectioned by front (Sec. 7 gates, Sec. 8 physical line, Sec. 9 H1, Sec. 10 IR attribution) |
| `theory/*_GATE.md` | **frozen contracts**, written and committed *before* the work they authorize |
| `theory/` (other) | derivations and counterexamples (`S4_STRICT_CONE_COUNTEREXAMPLE.md`, `THREE_VELOCITIES.md`, …) |
| `reports/YYYY-MM-DD--slug.md` | executions, verification records, independent reviews, promotions |
| `scripts/verify_*.py` | exact SymPy certificates, one per gate |
| `formal/` | Lean 4 + Mathlib machine-checked fragment |
| `papers/ir-corona/` | the paper (`.tex` is authoritative) |
| `debates/YYYY-MM-DD--slug.md` (+ `.log`) | cross-family adversarial debates (`sanedrin`), in Spanish |
| `comite/` | `/comite` role anchors and `config.toml` for this repo; output to `reports/comite/` |
| `sources/` | primary PDFs, with `README.md` recording SHA256 and which equations were actually read |

Language: scientific artifacts (`theory/`, `reports/`, `state/`, `papers/`) are in
English; `AGENTS.md`, `comite/` and `debates/` are in Spanish. Follow the
convention of the directory you are writing into. Commit messages are short
English imperatives ("Record Grok authentication failure…", "Charter C3 conditioning gate").

## The gate cycle

This is the repo's core workflow. Skipping a step invalidates the result.

1. **Charter** — write `theory/<NAME>_GATE.md` freezing the question,
   quantifiers (internal dimension, group/action, representation, node/sector,
   irreducibility/minimality), admission criteria, stop rules and success/failure
   verdicts, with initial evidence status `OPEN`. Commit it. Reports cite this
   *preregistration commit hash*.
2. **Authorize** — only the user charters a gate. `CURRENT_STATE.md` records what
   is authorized; everything else is unchartered and must not be computed.
3. **Execute** — derivation in `reports/`, plus a permanent traced verifier in
   `scripts/` if any computation is involved.
4. **Review** — independent adversarial review by a model of a *different family*
   (`sanedrin`) or a person, recorded as its own report with the SHA256 of the
   reviewed candidate and the base commit.
5. **Promote** — a separate explicit commit updates `CURRENT_STATE.md`. Nothing is
   promoted automatically by a passing script.

Verdicts are named states, not prose: `PASS`, `COUNTEREXAMPLE_VERIFIED`,
`OPEN_AFTER_<analysis>`, `STOPPED_NO_SIGNED_TERM`, `PROVED_UNDER_FROZEN_CONTRACT`,
`REJECTED IN THE DECLARED <class> CLASS`. Reuse the existing vocabulary.

Work here is **branch-local by default**. `CURRENT_STATE.md` is reconciled on the
research branch, not on `main`; promotion to `main` is a separate user decision.
Note which branch a status belongs to before citing it.

## Hard rules

Integrity (since 2026-10-22; see `reports/2026-10-22--escape-corruption-audit.md`):

- Before committing text: `python3 -B scripts/text_integrity.py --check` must report
  nothing new (the existing list is the manual-reconstruction queue).
- Before committing certificates: `python3 -B scripts/run_all_verifiers.py --output <tsv>`
  must pass in full. Use `certificate_utils.assert_sym_equal` for symbolic identities,
  never structural `==` on simplified expressions.
- Never route LaTeX through an escape-interpreting layer (JSON, non-raw Python strings,
  APIs) without running `--check` afterwards: this is how the W-series lost its formulas.

Scientific:

- **Never write `v_max` unqualified.** Keep `C_micro`, `V_causal^max`,
  `V_grp^max` and `c_IR` distinct. For `d >= 2`, `C_micro` is a convex body, not
  a scalar speed.
- For massive sectors do not identify `c_IR` with `|∇ω(0)|`, and do not treat
  `c_H` and `c_{ω^2}` as interchangeable — they differ for every `0 < m < 1`.
- Tag every nontrivial claim: `ESTABLISHED` / `SUPPORTED` / `PRELIMINARY` /
  `OPEN` / `REJECTED`. Never promote `PRELIMINARY` because it fits the narrative.
- Exact algebra and geometry before numerics. No fitted tolerances, no floating
  point in a certified quantity.
- No rigidity from a failed search, a finite scan or local isolation. No family
  identity promoted to a general QCA law without a separate proof.
- Scope (revised 2026-10-28, `PROJECT_INSTRUCTIONS.md` §1): finite-range,
  translation-invariant QCA on periodic lattices in d ≤ 3, free or interacting.
  Other lattices, neighbourhoods and internal structures are in scope, each with
  its own charter. Anisotropic substrates only as controls of a stated hypothesis.
  Out of scope without a successor charter: causal sets, random lattices, quantum
  gravity, and model searches without a frozen class and hypothesis.
- Bernstein's inequality and its equality theory are prior art. `NOVELTY = OPEN`.
- Negative results are first-class outcomes.

Code and git:

- No ephemeral scripts. Any code producing a retained result must be versioned in
  `scripts/`. Short manual inspection (`grep`, `sed -n`, `wc`, `git diff`) is exempt.
- **Do not change the bytes of an independently reviewed verifier** without a new
  review of that file. Reuse reviewed helpers read-only (as the later gate
  certificates import `walk2()`, `PAULI`, `exact_blocks` from
  `verify_directional_saturation.py`).
- `git add` named files only. Never `git add -A` or `git add .` — the user works
  in this repo too.
- When a result leans on `~/herramientas` or `~/sanedrin`, record the tool commit
  (`git -C ~/herramientas rev-parse --short HEAD`).

Epistemic (from `~/herramientas/REGLAS.md`):

- Nothing is stated as fact without verification *in this session* — a command,
  `file:line`, a commit, or a primary source. Otherwise `[UNVERIFIED]`.
- **No autophagy.** AI-generated text is not a source, and a model reviewing
  another of the same family is not independent verification.
- On an error, re-derive from scratch; a longer explanation of the same answer
  does not fix it.
- Dry style. If a sentence impresses more than it proves, rewrite it.
- Stay on the user's objective, not on the momentum of the previous step. A "yes"
  to one step does not change the goal.

## Tools

- `/comite` — expert committee, engine in `~/herramientas/skills/comite`, roles in
  `comite/config.toml`, anchors in `comite/roles/`, output to `reports/comite/`.
  Its guardrails encode `PROJECT_INSTRUCTIONS.md` §§1-7. Use for "what do I do
  now?" — direction, scope, readiness. All members are Claude.
- `sanedrin` (on PATH via `~/.local/bin/sanedrin` → `~/sanedrin/sanedrin`;
  installed 2026-09-26 with `bash ~/sanedrin/instalar.sh`, idempotent, rerun it
  if the symlink goes missing) — adversarial debate across model families. Use
  for "is this true?" before promoting or publishing. It sees only what is
  attached with `-c`. Output to `debates/`. See `~/sanedrin/README.md`.
  Check the census first: `sanedrin --listar`. On 2026-10-28 all five houses
  (`opus`, `astra`, `ciro`, `abner`, `gemini`) report `ok`. The census only checks
  that a key or CLI is present, not that a call succeeds. Last real calls:
  DeepSeek completed a review on 2026-10-26, Grok on 2026-10-28, and the latest
  Gemini API attempt (2026-10-27) failed on DNS before reaching the provider.
  For single sealed reviews outside a debate, `revision-ciega <astra|opus|deepseek|grok|gemini>
  <folder> <docs>...` takes `prompt.md` from the folder. Read a first `ausente` for
  `ciro` with suspicion: the check is `timeout 15 grok models`, and a cold
  `grok` can exceed it; rerun before recording the house as unavailable. Record a
  genuine failure rather than substituting a same-family review.
- Neither authorizes anything; the user decides.
