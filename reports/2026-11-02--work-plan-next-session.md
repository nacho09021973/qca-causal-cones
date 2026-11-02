# Work plan for the next session (other machine)

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit`, content
equal to `main` after PR #16 (`a481f5f`). **Nature:** planning record
written by an AI (Claude) at the user's instruction. It promotes nothing and
authorizes nothing; each item below needs the user's decision, and any
computation needs a charter first.

## 1. Setting up the other machine

Everything needed is on GitHub except what section 1.3 lists.

```sh
git clone git@github.com:nacho09021973/qca-causal-cones.git
cd qca-causal-cones && git checkout research/schur-stability-audit
python3.12 -m venv ~/venvs/qca && ~/venvs/qca/bin/pip install -r scripts/requirements.txt
# sympy==1.14.0, numpy==1.26.4; this machine used Python 3.12.3

git clone git@github.com:nacho09021973/herramientas.git ~/herramientas   # main @ ce09890
git clone git@github.com:nacho09021973/sanedrin.git ~/sanedrin           # main @ 7e011a4
bash ~/sanedrin/instalar.sh        # puts sanedrin on PATH; idempotent
```

Optional: `cd formal && lake exe cache get && lake build` (Lean v4.31.0,
Mathlib rev fabf563).

Smoke test, which needs no new charter: rerun one reviewed verifier from
the repo root, e.g. `python3 -B scripts/verify_l6b_triangular_row_gate.py`.
It should report 64/64 in about a minute.

### 1.1 Uncommitted work in `~/herramientas`

Eight files under `ai_scientist_local/experiments/alice_layers/formalization/`
were modified and not committed on `main @ ce09890`. They are not this
repo's work. They were pushed unchanged to the branch
`wip/alice-layers-2026-11-02` (commit `6b40c1a`, a `git stash create`
snapshot). `main` and the local working tree were not touched. To recover
them: `git -C ~/herramientas checkout wip/alice-layers-2026-11-02 -- ai_scientist_local/experiments/alice_layers`.

### 1.2 Local `main` here was stale

On this machine the local `main` branch pointed at `0ee2564`, 57 commits
behind `origin/main`. A fresh clone does not have that problem.

### 1.3 Not in git (must be recreated or is not needed)

- **Credentials:** `gh auth login`, SSH key, and the API keys or logins
  that `sanedrin` and `revision-ciega` use. Before relying on a house,
  probe its generation endpoint (`CLAUDE.md`, Tools); `sanedrin --listar`
  does not prove a house can generate.
- **Claude Code memory** (`~/.claude/projects/.../memory/`), which is local.
  Its content that matters is already in the repo:
  - the three-questions rule is in `PROJECT_INSTRUCTIONS.md` and `AGENTS.md`;
  - the goal ("how much is c on different substrates") is in
    `reports/2026-11-02--research-lines-known-question-abandonment.md`;
  - the sanedrin fallback ladders and false census readings are in
    `CLAUDE.md`.
- **`biblioteca/`:** git-ignored and absent here too. Primary literature
  lives in `sources/`, with SHA256 recorded. Several papers in the prior-art
  checks were read through alphaXiv text and not saved to `sources/`; the
  reports list them by arXiv id.

## 2. Where things stand (short)

The goal is c across substrates. Source:
`reports/2026-11-02--c-across-substrates-answer.md`, which is PRELIMINARY
and not reviewed.

- In the declared classes the substrate does not fix `c_0`. It fixes the
  bound `c_0 <= r_in(C_micro)`.
- That bound is attained on the line, square, BCC and cubic substrates.
- No declared hexagonal row attains it. The hexagonal class as a whole is
  OPEN (CS Sec. 12).
- No absolute scale is derivable (CS Sec. 8.21).

Novelty candidates:

| Candidate | State |
| --- | --- |
| s=4 family | Dropped by user decision |
| IR-corona theorem | `NOVELTY = OPEN`; strongest candidate |
| Hexagonal ceiling | Not refuted, low weight |

H1 is abandoned by user decision. Dispersion Phase 2 stays deferred, with
no charter.

## 3. Candidate next steps (the user chooses; none is authorized)

Each item states what is known, the question, and the result that would end
it, as the rule requires.

1. **Independent review of the c-across-substrates answer** (needs
   explicit permission to send text to a third party).
   - Known: the answer is built only from promoted results.
   - Question: does it state anything beyond what those results support?
   - Ends the line: a reviewer PASS, after which the answer can be cited;
     or a REPAIR, which gets fixed and closes the item.
2. **Charter M1, the hexagonal supremum.**
   - Known: K4 and K5. Exact Groebner on the 19-point ball did not finish
     in 900 s.
   - Question: does any s=2 walk in `W_hex` reach `c_0 = r_in`?
   - Ends the line: an explicit witness, after which there is nothing
     substrate-specific left; or no exact method finishing within one
     session, giving `OPEN_AFTER_<analysis>` with no numerics.
   - The charter must name the method before any computation.
3. **Finish the IR-corona prior-art check.**
   - Known: `reports/2026-11-02--ir-corona-prior-art-check.md`, conditions
     (a) and (b) not met.
   - Question: do the Pemantle–Wilson–Melczer monograph (2nd ed.), the
     open-Markov-systems paper (doi:10.1007/s11005-026-02086-4), or later
     citations of CRT 2005, Sunada–Tate 2012 or BBBP give the corona
     asymptotics?
   - Ends the line: a source giving them, which drops the candidacy.
4. **Finish the hexagonal-ceiling prior-art check.**
   - Question: do arXiv:1812.02601 or citations of P17, ADMP or JDW state a
     speed bound or a 120° optimum?
   - Ends the line: a source stating one, which drops the candidacy.
5. **Paper decision.** Whether `papers/ir-corona/` is revised to reflect
   the prior-art checks. This is a user decision; there is no computation.

Recommendation, not an authorization: 3 before anything is written for
outside readers, since the corona is the only candidate with weight. If the
goal is the c question itself, 1 settles whether the current answer stands,
and 2 is the only computation whose result changes it.

## 4. Repository closure criterion (user decision, 2026-11-02)

User statement: «si mañana volvemos a fracasar cerramos el repo y lo
borramos». The user asked for "failure" to be fixed here in advance, so it
is not argued afterwards:

- **Close if** step 3 finds the IR-corona asymptotics already published.
  No candidate with weight would then remain: the s=4 family was dropped,
  and the hexagonal ceiling is elementary (Bernstein plus a three-vector
  Gram bound).
- **Close if** the independent review (step 1) finds that the
  c-across-substrates answer states more than its promoted results
  support, and the repair leaves no content of its own.
- **Not a closure:** M1 stopping at `OPEN_AFTER_<analysis>`, which its
  abandonment result anticipates as a stop rather than a failure. A step
  that is simply not done tomorrow is not a closure either.

How to close: archive the GitHub repository (read-only, can be private,
reversible) rather than delete it. Deletion cannot be undone, and it
discards results that stand without novelty: no substrate-fixed `c_0`, the
`r_in` bound, the counterexamples, and the Lean fragment. No agent deletes
or archives anything without the user's explicit confirmation at that
moment.
