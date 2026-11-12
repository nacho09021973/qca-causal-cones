# IR-corona manuscript: reconciliation of two divergent versions

2026-11-12. Claude Code (claude-fable-5-2), at the user's instruction
(«adelante empieza con 1»). **Editorial three-way merge of existing text, not
a proof review, not a promotion.** Status of the reconciled manuscript:
PRELIMINARY, not re-reviewed as a whole. NOVELTY OPEN. No external
transmission, no verifier or Lean bytes changed, no new computation.

## Pre-step record

- Known: `papers/ir-corona/ir-corona.tex` existed in two versions that
  never met. Verified in this session with `git log` / `git merge-base`.
- Question: can the two be merged without losing a repair from either
  side, and does the statement proved in Lean still match the result?
- Stop: a mathematical contradiction between the two repair sets. None
  was found; one overlap was resolved by choosing a side (Sec. 3, item 3).

## 1. The two versions

Common ancestor: `adba394` (2026-09-28).

| Side | Tip | Manuscript commits since the ancestor | Content |
| --- | --- | --- | --- |
| October | `research/inverse-gravity-design` at `28c686e` | `cd8ff54`, `f85f429`, `5255823`, `951bbe3`, `59998ac`, `5f77de8` (all 2026-10-28) | Repair of Lemma Layers (b), (d) and the Table 1 caption after the sanedrin; site count in (b) and the `pi u` phases in (c)/Assembly after the Astra review; three DeepSeek minor remarks; DMPT citations; tag `ir-corona-v1` |
| November | this branch at `269ada5` | `1afc164` (2026-11-03), `76d6b38`, `341950e` (2026-11-10) | Prior-art citations (BGPP, BP3, ACSV manuscript); exposition repairs after the Opus review; narrowed abstract and scope statements; priority sentence removed |

Neither side contained the other's manuscript commits. `main` (`d4f06d0`)
carries the November side only up to `1afc164`.

Consequences before this reconciliation: the November text lacked the
October corrections of known defects in Lemma Layers, and the Lean proof of
the scalar Alice coefficient in `~/herramientas` (commit `2a7342b`) was
written against the October statement (source SHA256 `2075e840…`, commit
`08d5981`), which the November text did not contain.

## 2. Method

`git merge-file --diff3` of the November file against the October file
with the ancestor as base, for `.tex` and `.md`.

For the Markdown transcription the two sides had renumbered the reference
list differently (October inserted two entries at positions 10–11;
November appended three at 20–22). Before merging, the ancestor and the
November file were renumbered to the merged order (`n >= 10 -> n + 2` in
citations and in the list). After the merge the citation numbers were
listed and compared with the order of `\bibitem` in the merged `.tex`
(24 entries, same order).

## 3. Conflicts and their resolution

Four in `.tex`; the same four plus one reflow conflict in `.md`.

1. **Literature, two-dimensional walks.** Both kept: the November sentence
   on the shape theorem (BGPP, Thms. 2.2–2.3) followed by the October
   remark that explicit amplitudes outside the feasible set can be
   obtained instance by instance. The subject of the October remark is
   written as «Baryshnikov et al.» so that it is not read as a statement
   about BGPP. That remark was not re-checked against arXiv:0810.5495 in
   this session: `[UNVERIFIED]` here, inherited from `5f77de8`.
2. **Literature, transfer theorems.** Both kept: the October sentence on
   the DMPT path-sum solutions, then the November sentences on ACSV
   Thms. 9.5 and 9.12.
3. **Proof of Lemma Layers, Bob's part of (b), and (c), (d).** The two
   sides repaired the same gap (the spinor of `r` varies across Bob's
   region) in different ways. October splits
   `r(y) = N^{-3/2} R_0(w_*) + rho(y)` and bounds the `rho` term in norm
   without oscillation. November applies Leibniz to `h_N r~` with a smooth
   Fourier interpolation of the free tail. **The October argument is
   kept**: it is the one that went through the sanedrin, the Astra review
   and the DeepSeek review, and it is the one the row-vector statement of
   (b) is written for. **The November paragraph is not carried over**; it
   remains in `341950e`. October's (c) and (d) replace the short ancestor
   text, which the November side had left unchanged. The two closing
   November sentences on uniformity in `theta_N` and on the endpoint
   `delta = 0` are appended after (d).
4. **Assembly, six non-contributing points.** Both kept: the October
   sentence (Lemma symbol (b) transfers the Gaussian decay from the ball at
   0), then the November sentences on the reciprocal eigenvalue branch. The
   November sentence on the half-period identities says the same as the
   October one and is not repeated.
5. **`.md` only, first paragraph of the proof of (b).** November text with
   the October insertions (`G_delta`, the condition on `r_0`).

One notation fix outside the conflicts: a November sentence in the proof of
(b) wrote `G_0` where the October side had renamed the profile `G_delta`
(DeepSeek remark); changed to `G_delta` in `.tex` and `.md`. One reference
number inside the Markdown list (`[16] -> [18]`, the printed ACSV edition).

Everything else merged without conflict. Checked by listing, for each
side, the lines it added to the ancestor that are absent from the result:
October, only the lines of items 1 and 4 that were rewritten as above;
November, only the paragraph of item 3, the duplicate sentence of item 4
and reflowed line ends.

## 4. Checks run

- `pdflatex` twice on the reconciled `.tex`: exit 0, 21 pages, no
  undefined reference or citation.
- Lemma Layers, statement: byte-identical to the frozen source of the Lean
  proof (`runs/run_0/paper.tex`, SHA256 `2075e840…`), by `diff` of the
  lemma environment.
- Passages cited in the Lean fidelity table
  (`FIDELITY_ALICE_LAYERS_B.md`: source lines 403–405, 418–437, 563–568,
  947–952, 1017–1031, 1076–1085, 1118–1145): no `diff` hunk between the
  frozen source and the reconciled `.tex` starts in those ranges. The one
  hunk nearby (source lines 943–944) is the November expansion of the
  bound on `<r, E a_c>`, a different statement.

Not checked: the mathematics of either repair set; the certificates
(not rerun); the Lean build (not rerun); the Markdown against the PDF line
by line.

## 5. Files

Reconciled:

- `papers/ir-corona/ir-corona.tex` SHA256
  `eed30c18a1d7d062e1f065230231073b696b1eaf7098b314f4e91a8548137dd5`
- `papers/ir-corona/ir-corona.md` SHA256
  `6602d1f9cf0ef84da34998a5f91ec9d010eb4bae1f49ac64c13c9cb0a943ed23`

(after the read-through edits of Sec. 8; the merge alone gave
`e62af5d2…` and `ef599e6a…`).

Brought unchanged from `research/inverse-gravity-design` (`28c686e`),
because the reconciled text depends on them and they were absent here:

- `debates/2026-10-28--ir-corona-sanedrin.md`, `.log`, `-request.md`
- `debates/2026-10-28--ir-corona-repairs-review-astra/` (verdict recorded
  there: `CERRADA_CON_ARREGLOS`, two mandatory repairs, applied in
  `f85f429`)
- `debates/2026-10-28--ir-corona-repairs-review-deepseek/` (verdict
  recorded there: `CERRADA`, minor remarks applied in `951bbe3`)
- `papers/ir-corona/certificados/2026-10-28/` (certificate run outputs)
- `reports/2026-10-28--ir-corona-prior-art-audit.md`

## 6. Review coverage of the reconciled text

No review covers the reconciled file. The October reviews (sanedrin,
Astra `gpt` family, DeepSeek) saw the October text without the November
edits. The Opus review of 2026-11-10 saw the November text without the
October repairs; the repairs applied after it were not re-reviewed. The
merge itself was done by a Claude model.

## 7. Open after this step

1. The `Repo` bibitem cites tag `ir-corona-v1`, which points to `59998ac`
   on the October branch, not to the reconciled text. A new tag is the
   user's decision; none was created.
2. (Done in Sec. 8: the Markdown header now names the reconciliation.)
3. `reports/2026-11-10--ir-corona-readiness.md` and
   `reports/2026-11-10--ir-corona-opus-repairs.md` record SHA256 values of
   the November text; they are historical for that text.
4. Bob's coefficient, the matrix symbol and the assembly are not
   formalized. (The Lean proof of the scalar Alice coefficient was moved
   into `formal/alice-layers/` the same day, Sec. 9.)
5. Whether `research/inverse-gravity-design` should be merged as a branch
   (it is 271 commits apart from `main` on its own side) was not examined;
   only the manuscript and its review records were reconciled.

## 8. Read-through of the reconciled text (same day)

User instruction «revísalo completo». One complete reading of the
reconciled `.tex` by the same Claude model that merged it. **Not an
independent review** (same family as part of the authorship; no second
family, no person). It does not change any status.

Re-derived by hand while reading, no discrepancy found: the fourteen jumps
and their norms; `det S = 1`, the dispersion and `H_W`; the normalization
`Z_N` and `c_r`; the separation inequalities; the constants of
Theorem upper (`9N4^N`, `J`) and the `D_B <= 4T_N` step; the convexity
argument for `Phi`; Lemma symbol (a), (b); the depth parametrization, the
parity `(-1)^{j+j'}`, the two phase identities of Layers (c) and their
cancellation in the assembly; the layer prefactors `16 pi/sqrt3` and
`32/sqrt3`; `c_g`, `1/720`, `1/48`; the constant `K` and the power
count `13/2`; the `rho` bound and the `CN^{-3}` estimate of the October
proof of (b); the total-variation estimate of the November text, which is
consistent with (and sharper in `delta` than) the October bound
`CN^{-4}(1+delta)^3`.

Second route for the printed numbers (floating point, inspection only,
nothing retained, not a certificate): `t_*`, `K_*`, `e^{Phi_*}`, `q_t`,
`q_n` (also as eigenvalues of a finite-difference Hessian of `Phi`), `P`
(against a numerical eigenprojector), `I_0`, `I_1`, `K`, `Gamma-bar`,
`eps_+`, `eps_-` and twelve entries of Table 1 with their relative bounds
were recomputed from the definitions in the text; all agree with the
printed digits, and the sign margin holds in the twelve cases.

Edits made after the reading, in `.tex` and `.md`, wording only:

1. The sentence that CJWW count two outside-region studies appeared twice
   in the literature paragraph (once from each side). The second
   occurrence is removed.
2. The DMPT sentence is moved after the ACSV sentences, which continue the
   preceding argument.
3. In the proof of Layers (b) the two conditions on `r_0` were stated
   twice (October and November wording). The November duplicate is
   replaced by a pointer to (d), where the second condition is imposed
   with its proof of positivity (`d_0 > 0`).
4. Markdown header: names the reconciliation.

After these edits: compiles (21 pages, no undefined reference); the
statement of Lemma Layers is still byte-identical to the frozen source of
the Lean proof.

Left for the author, not changed:

- «the shape theorem they prove … [BGPP, Thms. 2.2–2.3]» follows a
  sentence whose subject is Baryshnikov–Brady–Bressler–Pemantle (BBBP),
  but cites Bressler–Greenwood–Pemantle–Petkovšek. The attribution should
  be checked in the two papers.
- The October remark on BBBP (amplitudes outside the feasible set,
  extension to dimension three) is unverified in this session.
- Item 1 of Sec. 7 (tag).

Not covered by the reading: the certificate scripts (not rerun), the
analytic remainder estimates beyond the orders checked above (uniformity
of the Poisson remainders in `eta`, the compactness step of
Lemma symbol (e)), the Markdown line by line, and novelty.

## 9. Lean proof of the scalar Alice coefficient moved into this repository

At the user's instruction the formalization was moved from
`~/herramientas` (`2a7342b`) to `formal/alice-layers/`; record in
`formal/alice-layers/MIGRATION.md`. 997 files copied byte-identical, three
path edits, full offline verification rerun from the new location:
`verification/migration_2026-11-12/verification.json`, `success: true`,
38 modules, proved targets `ProfileIntegrability`, `AliceLayersB`, 57
copied definitions equal, Lean source hashes equal to the pre-migration
record `assembly_final01`. Mutation campaigns not rerun. In
`~/herramientas` the folder is removed from the working tree with a
pointer `MOVED.md` (uncommitted there). Scope unchanged: scalar Alice
coefficient only; no external review.

Nothing was committed in either repository.
