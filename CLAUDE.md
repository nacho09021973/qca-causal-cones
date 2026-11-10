# CLAUDE.md

Single instruction file for every AI agent working in this repository: Claude
Code reads it directly, Codex through `project_doc_fallback_filenames =
["CLAUDE.md"]` in its `config.toml`, and Grok. There is no `AGENTS.md` here on
purpose: with both files Grok would load both (`~/herramientas/README.md`).

## What this repository is

A physics/mathematics research repository, not a software product. Its output is
frozen contracts, derivations, exact verification certificates, reports and
independent reviews about finite-range quantum cellular automata (QCA).

Project question (since 2026-11-09, `README.md`): does one finite-range QCA,
under one fixed rule, admit both universal quantum computation and a
relativistic low-energy regime of the same rule? Claims are per code,
resources and parameters; working model the Thirring QCA, `U = F J`. The
original question — the relativistic speed from microscopic causal geometry —
and its results are kept as inherited lines (`PROJECT_INSTRUCTIONS.md` §1).
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
3. `~/herramientas/REGLAS.md` — the cross-repo rules, which also apply here.

Before every experiment, computation or code change, write down three things:
what is already known (with its source), the concrete question to be answered,
and which result would force abandoning that line. Each charter records the
third point for the line, separately from its per-hypothesis verdicts.

Before investigating any question, check the literature index:
`grep -i <topic> biblioteca/INDICE.md`. `biblioteca/` is git-ignored and local;
the index only *locates* papers, it proves nothing — read the PDF and cite
`file.pdf p.N`, otherwise tag the claim `[UNVERIFIED]`. Tags marked `proposed`
were written by an AI. Never hand-edit `INDICE.md`; edit
`scripts/biblioteca_catalog/curated.csv` (versioned, with `tags.csv`) and
regenerate with `python3 ~/herramientas/biblioteca_catalog/build_catalog.py
--repo .`. Verified 2026-11-06: `biblioteca/INDICE.md` and the generator both
exist on this machine (on 2026-09-26 neither did). If either is missing in a
checkout, ask the user rather than inventing a path; `sources/` (versioned PDFs
with recorded SHA256) is the primary literature that is always present.

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
English; `comite/` and `debates/` are in Spanish. Follow the
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
- Do not broaden scope: no causal sets, random lattices, quantum gravity, new
  substrate classes, or anisotropic detours, absent a new charter. Interacting
  QCA are in scope for the coexistence question, one declared model, code and
  resource set per charter.
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
  **`sanedrin --listar` checks logins and credential presence; no check of it
  proves a house can generate.** Probe the generating endpoint before relying on
  one: `claude -p --model`, `codex exec -m`, `grok --model … -p`, or Gemini's
  `:generateContent`. Four false readings were verified on 2026-09-26 —
  `abner` `ok` on a placeholder key (its check is `-n "$DEEPSEEK_API_KEY"` plus
  DNS); `astra` `ok` while the ChatGPT account was over its usage limit (that
  check self-labels "cuota no verificada"); `gemini` `ok` while every *pro*
  model returned `limit: 0` (its check is an authenticated metadata `GET`, which
  passes regardless); and `ciro` `ausente` because a cold `timeout 15 grok
  models` overran, so rerun a single `ausente` before believing it.

  Generation verified on 2026-09-26: `opus` (`claude-opus-5`, and
  `claude-sonnet-5` / `claude-haiku-4-5-20251001` below it; `claude-fable-5`
  needs credits), `ciro` (`grok-4.7` / `4.6` / `4.5`) and `gemini`
  (`gemini-3.8-flash`; the seat is pinned there because the *pro* family has no
  free-tier quota, so it is weaker than the pro the design assumes — name the
  real model in any report it feeds). `astra` could **not** generate: every
  model its account admits — `gpt-6-astra`, `gpt-5.6-terra`, `gpt-5.6-sol`,
  `gpt-5.6-luna` — returned the same account-level usage limit, and
  `gpt-6-pro` / `gpt-6` / `gpt-5.4-mini` are refused outright. So three houses,
  not four, which still satisfies the cross-family requirement.

  When a house fails, descend that provider's own ladder rather than dropping
  the seat — but only for a *per-model* failure (400/404, or a `limit: 0` on
  that model). An *account-level* failure is identical across the family, so
  descending wastes calls: mark the house `ausente`. Record whatever actually
  answered; never downgrade a seat silently.
- `revision-ciega <astra|opus|deepseek> <folder> <document>...` — sealed blind
  review of one or more documents (e.g. a report or `state/CURRENT_STATE.md`) by
  a single model; the brief (`prompt.md`) and the report go in `reports/` or
  `debates/`, next to what was reviewed. `opus` does not count as independent
  review of text written with Claude.
- `investigacion-gemini investigaciones/<YYYY-MM-DD>-<slug> [prompt_abierto.md]`
  — research brief to Gemini with Google search. It locates, it does not prove:
  every citation is read in the original and logged in that folder's
  `comprobacion.md`.
- `comprobar-objeciones <objeciones.csv> <document.tex|.md>` — objection register
  with status and checked commit; warns about sections changed since the check.
- These three live in `~/herramientas` (see `~/herramientas/README.md` and
  `MAPA.md`). `revision-ciega`, `investigacion-gemini` and `sanedrin` send text to
  third parties: only with the user's explicit permission.
- In Codex, run authorized external reviews outside the network sandbox
  (`sandbox_permissions: require_escalated`). On 2026-11-10 three sandboxed
  Opus calls failed with DNS `EAI_AGAIN`; the same sealed CLI options worked
  outside it. This execution requirement does not replace permission to send.
  On failure, inspect the provider JSON (`opus.json`), including the final
  `result` and `api_retry` events: `missing_or_failed_result` in the summary
  can conceal the concrete connection error. Do not repeat an unchanged call
  after a DNS failure; correct network access first.
- Neither the committee nor the sanedrin authorizes anything; the user decides.
