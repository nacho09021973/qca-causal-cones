# IR-corona manuscript: bounded readiness audit

2026-11-10. Codex. **Documentary audit, not an independent proof review or
novelty verdict.** User authorized documentation consolidation followed by
the manuscript. Base cb40b4f13305d383c01d6aae241d77d585eba14e on
research/tetrahedral-support-rigidity-2026-11-09. No external transmission.

## Scope and version

Known: the manuscript states an asymptotic operational response for one
walk and a fixed protocol. Its components have historical reviews and
certificates; only part of the upper-bound argument is formalized.
Question: what remains to obtain a specialist assessment of this manuscript?
Stop: a versioned inventory and bounded review brief, or a documented
blocking objection. This audit does not reproduce the whole proof, certify
the bibliography, or open a new calculation.

Authoritative file: `papers/ir-corona/ir-corona.tex`; Markdown is a
transcription. Last manuscript commit before this audit: 1afc164 (prior-art
citations). Initial SHA256:

- TeX: d332cd178594eefba2b8d358ba5fcc15167fbf0528bb74586ff19484d4a5420a
- Markdown: 8845a6b41d3596a265c64e1d36f2e7d82b33b079ccc3132e1e71eeddaef7164c

After the two wording repairs below:

- TeX: 5274dda038ffe08c8d3d9bad8be58e7576070ee548d1dfd53299390629e5d579
- Markdown: 4fdec258464fa499854200cf27b3989aac5eacdfb5ced4c1bd2b1dfc2d6daef0

## Claim and evidence map

| Claim | Existing evidence inspected | Limits / reviewer obligation |
| --- | --- | --- |
| Explicit upper bound (Theorem 4.1) | `formal/README.md`; scaled-IR review of 2026-09-17; manuscript formal-verification remark | Lean covers kernel, geometry, counting, operator bound and an abstract signal inequality. Protocol identification and second-quantized D_B are not formalized. No Lean rebuild in this audit. |
| Regional rate | `reports/2026-09-17--regional-directional-asymptotics-independent-review.md` records PASS for its bounded claims | This review explicitly left the coefficient open; it cannot certify the later full asymptotic by itself. |
| Leading power and non-vanishing coefficient | `reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md` records PASS; `scripts/README.md` states certificate coverage | Certificate checks exact identities and interval coefficients; it does not certify analytic remainder lemmas or an explicit N_*. |
| Operational scope | Current leading-asymptotics theorem and restriction after it; commit 3a44725 | Sixteen algebraic pairs, twelve Pauli pairs for the operational claim; four identity-encoder reference controls. |
| Infrared interpretation | Definition of admissibility and Theorem 3.3; CURRENT_STATE Sec. 10.1 | Vanishing relative leakage is not a proof that an exponentially small signal is carried entirely by the infrared block. The later spectral decomposition records leading cancellations. The reviewer must keep these meanings separate. |
| Novelty | `reports/2026-11-02--ir-corona-prior-art-check.md`, including its November 3 continuation; manuscript literature section | Historical targeted author audit, unreviewed. Its later sections supersede its initial unread-source list. No new literature search or validation of its negative conclusions here. NOVELTY OPEN. |
| Full manuscript review | Commit e37ad09 records changes after a pre-publication review | A commit message is not the review itself. No standalone complete report for that review was located in the targeted reports/debates search. No claim that the current whole manuscript is independently accepted. |

The four certificate scripts cited in the manuscript and the original
corona Lean files have no tracked changes from its cited baseline
551addabe28b to the audit base. The `formal/` diff consists of the unrelated
Thirring subproject. Thus the old citation is not automatically a wrong
certificate version, but it is not the current manuscript snapshot.

## Two bounded repairs

1. Introduction: the cube's support function h(n)=||n||_1 was described
   ambiguously as its extent in that direction. It is the maximum
   projection; the extent along a ray is 1/||n||_infinity. Both are now
   stated. Direct check: maximizing n.x over |x_i|<=1 gives sum |n_i|;
   imposing |r n_i|<=1 gives r<=1/max |n_i|. For n=(2,1,0)/sqrt(5),
   these give 3/sqrt(5) and sqrt(5)/2, so they cannot be interchanged.
   Axial and diagonal cases agree and alone would not catch the wording.
   This repairs interpretation, not the support-function proposition.
2. Appendix A: replaced the unqualified claim that Theorem 4.1 is
   formalized with the exact component scope already stated in its remark
   and `formal/README.md`. No Lean or certificate bytes were changed.

Both repairs are synchronized in TeX and Markdown. They have not received
independent review. The theorem statements and priority wording are unchanged.

## Readiness decision

The manuscript is a concrete candidate for **specialist assessment**, not
certified ready for publication. No fatal proof error was established in
this bounded audit; absence of such a finding is not a proof endorsement.

Before submission, distinguish these obligations:

- Obtain an assessment of the current full proof, especially uniformity
  in theta_N, Poisson layer remainders, the two contributing saddles and
  the transition from the interference functional to the observable.
- Obtain a separate judgment on substantive novelty, using original
  papers rather than the repository's literature audit as authority.
- Reconcile the phrase "infrared-controlled" with the admissibility
  definition and the later cancellation results. Do not silently turn
  admissibility into exclusive infrared spectral origin.
- Produce a reproducibility snapshot for delivery: exact manuscript and
  certificate versions, archived release if submitting, and a fresh
  execution record if requested. Historical PASS is not a run today.
- Finish typesetting and visual inspection. Compilation succeeds, but
  overfull boxes remain. The source also has author TODOs for a release/DOI
  and target-journal AI-assistance disclosure. These are submission tasks,
  not reasons to withhold a clearly labelled review draft.

## Concrete specialist brief — prepared, not sent

**Objective:** decide mathematical correctness and substantive contribution
of the fixed three-dimensional CJWW protocol, separately.

**Primary input:** the TeX/compiled PDF identified above; certificate scripts
listed in its Repo reference; `formal/README.md`. Historical reviews and
the prior-art audit are secondary context, explicitly labelled as such.
The original cited papers are required for any priority conclusion.

**Questions:**

1. Does the proof establish the stated uniform asymptotic with a
   non-vanishing coefficient for all sixteen pairs, with the operational
   conclusion restricted to the twelve Pauli pairs?
2. Are the layer/Poisson remainder estimates sufficient, including
   uniformity as theta_N approaches an endpoint, and is the inference
   delta(N)>0 for sufficiently large N justified?
3. Is the operational interpretation valid under the exact infrared
   admissibility definition, without assuming spectral dominance?
4. Does an existing theorem yield this weighted operational asymptotic
   directly? If yes, identify it and verify its hypotheses. If not,
   identify the substantive additional step and assess its significance.

**Expected output:** separate correctness and originality assessments;
each objection must cite the equation/lemma and say whether it is fatal,
repairable, or a limitation. A negative literature search alone is not
an originality verdict. **Budget:** one initial round. **Closure:** the
written assessment and an explicit list of unresolved obligations; no
automatic repair/review loop or new model. Human recipient not selected.
External transmission requires a separate explicit user instruction.

## Checks performed

TeX compiled with pdfLaTeX (TeX Live 2023); output has 18 pages. Auxiliary
build files are in `/tmp/qca-ir-corona-readiness/`, not scientific evidence.
The compilation checks typesetting only. No scientific verifier, diagnostic
sweep or Lean build was run. `git diff --check` passed. No commit or push
was made as part of this task.
