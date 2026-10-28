# AI-Scientist / Claude documentary trial for A.int — 2026-10-28

**Trial outcome: proposal withdrawn; no new calculation charter recommended.**
This is an evaluation of one proposal, not a rejection of Eon, all non-Gaussian
references, AI-Scientist or Claude's ability to help the project.

## Authorization and scope

User instruction, verbatim: "perfecto ahora vamos a probarlo en cd ~/qca-causal-cones".
The inherited trial uses Claude for one proposal and one self-critique. Codex chose
the current A.int reference-state bottleneck from the canonical state and disclosed
that choice before sending. This is a documentary proposal exercise; it does not
charter or execute new scientific calculations. The model question and the two-call
limit were written in the shared driver and template before the first call.

Project base: `3395c1c27426f06f2d073cae806dd289e782c674`, branch
`research/inverse-gravity-design`. The branch was seven commits ahead of its
upstream and contained an untracked DeepSeek addendum-review folder. Both are
preserved. The pending review was not treated as a completed report or altered.

## What actually ran

- Original SakanaAI `generate_ideas`, its two prompt templates and its JSON parser,
  loaded from checkout `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`.
- A QCA-specific documentary template and `revision-ciega opus` transport, authored
  by Codex in `~/herramientas/pruebas/ai_scientist/qca.py` and `qca_task.md`.
  Shared-tool commit: `352f6c8aacaefa57b9aeee415dbecc3f6249f01e`; uncommitted adapter
  bytes and upstream files are identified by SHA-256 in `provenance.json`.
- Two completed calls to requested model `claude-opus-5-5`, default high effort,
  with network access authorized for the trial. First proposal, then self-critique.
  Both original stream JSON files and launcher states are retained.
- No generated code executed, no finite-rotor simulation, no training, no spectrum,
  vacuum, correlator or loop calculation, and no full AI-Scientist paper pipeline.

The complete evidence is in
`../investigaciones/2026-10-28-ai-scientist-eon/`. `initial_proposal.md` and
`withdrawal.md` are readable extractions; original reports and JSON remain unchanged.
`PARSED_UNVERIFIED` in provenance means a JSON record was parsed, not that a viable
candidate survived. Here that record explicitly withdraws the proposal.

## Proposal and author withdrawal

Claude proposed a test of whether the declared Gaussian-tail obstruction could
extend to factorial electric tails, phrased using entire Laurent generating series
of finite exponential type. The proposed result would only exclude a tail class;
it would not select a physical vacuum.

In the second call Claude withdrew it. It recognized that the suggested second
check reused the same analytic machinery and had not established a useful extension
at the stated budget. It offered further indicator-function thresholds and
kicked-rotor sketches, explicitly unchecked. Those sketches are not accepted here
as theorems, obstructions or spectral facts. In particular, their numerical
threshold constants and claimed resonant control are **UNVERIFIED**.

The proposal's relevance and feasibility scores are self-assessments, not evidence.
The self-critique is not independent review. Codex does not adopt every reason
offered by Claude merely because Claude withdrew its own proposal.

## Codex feasibility check

There is a concrete defect before attempting any Eon calculation. The first
proposal defines a fixed-parameter coefficient class by
`abs(c_n) <= C tau^n/n!` on nonnegative indices and claims its equivalence to a
finite-exponential-type class, together with stability under finite shifts up to
constants. The stated fixed-parameter bound does not have that shift stability:

For the defining coefficients `c_n=tau^n/n!`, the shifted coefficients obey
`c_(n-1)/(tau^n/n!) = n/tau` for `n>=1`. There is no uniform constant in n at the
same fixed positive tau. This is a check of the proposal's definition, not a new
QCA theorem. It does not assert that these coefficients already satisfy the full
Gauss-sector constraints or form an Eon stationary state.

The same example illustrates why exponential type and the exact coefficient
envelope cannot be equated at the boundary parameter without qualifications:
multiplying `exp(tau z)` by z preserves its exponential type at infinity but
introduces that unbounded coefficient ratio. A union over larger parameters or a
polynomial allowance may repair the class, but would require changing the proposed
contract and tracing every later bound. No such repair is executed here.

A separate scope check also fails: even a correctly defined larger excluded class
would not supply the missing physical-selection criterion. Both the model prompt
and final proposal acknowledge this limit. The response does not justify treating
this exclusion program as the next effective reference-state construction step.

**Selection decision: do not freeze or execute this proposed calculation.** This
does not establish that a corrected tail-class problem is impossible or useless;
it records why this particular plan is not ready. No claimed analytic threshold
or kicked-rotor theorem is needed for this decision.

## Primary sources and provenance

Before the call, Codex read `biblioteca/INDICE.md` and inspected
`biblioteca/arXiv-2205.03148v4.pdf` pp.6-9 and 28-29. These pages describe opposite
link-end electric fields, integer gauge registers, JW operators and the order
`U=D_M D_E D_F`, including equations (34)-(37). They do not establish the proposed
tail-class result or a physical vacuum. Extraction can garble formulas; unread or
illegible coefficients remain unverified. The exact magnetic exponential and
other assumptions are inherited as declared model specifications, not re-proved.

PDF SHA-256: `c366b8a8482a762c93e534e43d6572323737df4677556b1a764e02a1389d2d02`.
The library already contains the PDF; no paper was added and no catalogue rewritten.
The complete canonical-state snapshot and document hashes are retained; only the
reading guide and A.int section of the state were sent, alongside the listed
contracts, report/addendum and primary excerpts. No unpublished DeepSeek verdict
was supplied or anticipated.

`consolidar_qca.py` in the shared tools extracts readable records, checks both
provider states, checks input hashes against current files, and applies the
project's text-integrity functions to the retained Markdown. The project-wide
tracked-text integrity baseline was `0 problem(s)`. No certificates were changed,
so no scientific verifier sweep is claimed as evidence for this documentary trial.

## Closure

The adapted proposal/reflection transport worked. This one trial did not yield an
execution-ready research plan. No gate, evidence status, prior scientific report
or independently reviewed verifier is modified. The canonical Eon reference-state
problem remains open. No replacement candidate, review round, commit or push is
started by this outcome.
