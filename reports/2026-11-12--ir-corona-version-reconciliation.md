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

(Sections 1–9 were committed as `9f16b1b`, `aa37be6`, `2525211` and pushed
at the user's instruction; `~/herramientas` as `7d111a1`.)

## 10. Items left open in Sec. 8, done at the user's instruction («haz todo esto»)

Same Claude model as Secs. 1–9. **Still not an independent review.**

### 10.1 Attribution of the shape theorem — corrected

Sources read in the PDF:

- BBBP, `biblioteca/arXiv-0810.5495.pdf` (37 pages). Theorem 4.2, PDF
  p. 24: for the family `S(t)`, amplitude asymptotics uniformly over a
  compact subset of the interior of the feasible region; outside its
  closure, `|a_r| <= C|r|^(-N)` for every `N`; the proof (PDF p. 25)
  adds «Uniform exponential decay of amplitudes for r bounded outside the
  image of the Gauss map follows».
- BGPP, arXiv:0903.2967v2, downloaded 2026-11-12 from arxiv.org, SHA256
  `7176b8dd36ba7aa62a2cf8a926ac633fa2340f7f82717976fc994cc755ca631c`
  (18 pages), stored locally as `biblioteca/arXiv-0903.2967.pdf`
  (git-ignored). PDF p. 3: «Theorem 2.2 (shape theorem [BBBP08,
  Theorem 4.2])», `O(e^(-cn))` uniformly over compact subsets of the
  complement of `G`, under hypothesis (2.7); PDF p. 4: «Theorem 2.3
  (asymptotics in the feasible region)».

So the statement cited is BGPP's formulation, which BGPP attribute to
BBBP Theorem 4.2. The sentence «the shape theorem they prove … [BGPP]»
is replaced, in `.tex` and `.md`, by one that names BGPP as the authors of
the cited formulation and BBBP Theorem 4.2 as its attributed source.

Library catalogue (fixed the same day, user «arréglalo como mejor te
valga»): `scripts/biblioteca_catalog/curated.csv` and `tags.csv` on this
branch were the 2026-09-24 version (13 rows), while the fuller catalogue
(73 rows, four more tags) existed only on `research/inverse-gravity-design`
(`241be89`). Both files are now taken from that branch; its rows are a
superset of this branch's except one row for a duplicate PDF that was
removed there (`3c7a98c`) and is not on disk. Added: the row for
`arXiv-0903.2967.pdf` and the pages read today in the BBBP row. Index
regenerated with `~/herramientas/biblioteca_catalog/build_catalog.py`
(herramientas `7d111a1`): 75 PDFs, 74 tagged. The untagged one,
`Finiteness and Uniqueness of Duality Cascades in Three Dimensions for
Affine Quivers.pdf` (arXiv:2411.09141), is on disk without a catalogue row
and looks unrelated to this repository; left for the user.

### 10.2 October remark on BBBP — verified

`biblioteca/arXiv-0810.5495.pdf`, PDF p. 2: «An explicit description of the
feasible set and explicit formulae for probability amplitudes at specific
points inside and outside of the feasible set may be obtained; however,
these details differ greatly from one instance to another.» PDF p. 4: «No
family of QRW in dimension three or higher has been analyzed to date, for
example, but such an undertaking should be a modest extension of the
present work.» The sentence in the manuscript states this and no more. The
`[UNVERIFIED]` of Sec. 3 item 1 is withdrawn.

### 10.3 Certificates rerun

The four Appendix A certificates were rerun at `2525211`:
53/53, 18/18, 58/58, 27/27, exit 0; outputs byte-identical to the
2026-10-28 record. Stored in `papers/ir-corona/certificados/2026-11-12/`.
Script bytes unchanged since `551addabe28b`.

### 10.4 Poisson remainders and the compactness step — re-derived, no gap found

Author-side re-derivation, PRELIMINARY like everything here.

- **Lemma symbol (e).** For `xi_* = t_* u` all components are non-zero, so
  Lemma specrad gives `rho(S(eta - i xi_*)) < e^(Phi_*)` for every `eta`
  outside `Sigma`. The spectral radius is continuous in `eta` and the
  complement of the eight open balls in the torus is compact, so the
  maximum is `e^(Phi_* - c')` with `c' > 0`. Lemma schur with the uniform
  norm bound `4e^(3t_*)` then gives
  `||S~_N|| <= e^(-c'N)(1 + 4e^(3t_*) N e^(-(Phi_*-c')))`, which is the
  stated `CNe^(-cN)`. Nothing is missing.
- **Reciprocal branch near the eight points.** `e^(-N Phi_*)|lambda|^(-N)
  <= exp(-2N Phi_* + (3/4) N eta^T Q eta)`, which is below
  `exp(-N eta^T Q eta/4)` as soon as `eta^T Q eta <= 2 Phi_*` on the ball;
  this holds for small `r_0`. The November sentence covers it.
- **Layers (b), terms `m != 0`.** `G_delta` is continuous and compactly
  supported, `C^1`, with bounded second derivative jumping across the rim,
  so its third derivative is a finite measure and
  `|G^(k)| <= ||d^3 G||_M |k|^(-3)`; `sum_m |m|^(-3)` converges on a
  two-dimensional lattice, so Poisson summation holds pointwise. With
  `r_0 <= (1/2) min|2 pi m|` the bound `|2 pi m - eta_t| >= pi|m|` is
  uniform in `eta`. Plane translations contribute unit-modulus phases
  only, so the bound is uniform in `theta_N`; depth factors are polynomial
  against `e^(-t_*(theta_N+j))`. Sum over planes `<= CN^(-4)`, relative
  `N^(-3/2)`.
- **Layers (b), term `m = 0`.** Every replacement (variation of `phi_N`,
  `sin` against its argument, `eps_perp` against `delta - |u|^2/2R`,
  `e^(-i eta_n delta) - 1`) is bounded on the integrand in absolute value,
  hence uniformly in `eta_t` and `theta_N`. Remark: on the support
  `|x| - R = O(delta)`, so the variation of `phi_N` is `O(delta/N)`; the
  text's `O(|u_perp|/N + delta/N)` is weaker and sufficient.
- **Completion of the depth series.** Planes with `delta > R/2` and the
  tail `j > sqrt3 R/2` of `S_+` are exponentially small
  (`Psi_delta <= pi delta^3/3`).
- **Layers (d).** The character on `Lambda_0` depends only on the
  tangential projection, so non-triviality is `eta_(0, "# IR-corona manuscript: reconciliation of two divergent versions\n\n2026-11-12. Claude Code (claude-fable-5-2), at the user's instruction\n(«adelante empieza con 1»). **Editorial three-way merge of existing text, not\na proof review, not a promotion.** Status of the reconciled manuscript:\nPRELIMINARY, not re-reviewed as a whole. NOVELTY OPEN. No external\ntransmission, no verifier or Lean bytes changed, no new computation.\n\n## Pre-step record\n\n- Known: `papers/ir-corona/ir-corona.tex` existed in two versions that\n  never met. Verified in this session with `git log` / `git merge-base`.\n- Question: can the two be merged without losing a repair from either\n  side, and does the statement proved in Lean still match the result?\n- Stop: a mathematical contradiction between the two repair sets. None\n  was found; one overlap was resolved by choosing a side (Sec. 3, item 3).\n\n## 1. The two versions\n\nCommon ancestor: `adba394` (2026-09-28).\n\n| Side | Tip | Manuscript commits since the ancestor | Content |\n| --- | --- | --- | --- |\n| October | `research/inverse-gravity-design` at `28c686e` | `cd8ff54`, `f85f429`, `5255823`, `951bbe3`, `59998ac`, `5f77de8` (all 2026-10-28) | Repair of Lemma Layers (b), (d) and the Table 1 caption after the sanedrin; site count in (b) and the `pi u` phases in (c)/Assembly after the Astra review; three DeepSeek minor remarks; DMPT citations; tag `ir-corona-v1` |\n| November | this branch at `269ada5` | `1afc164` (2026-11-03), `76d6b38`, `341950e` (2026-11-10) | Prior-art citations (BGPP, BP3, ACSV manuscript); exposition repairs after the Opus review; narrowed abstract and scope statements; priority sentence removed |\n\nNeither side contained the other's manuscript commits. `main` (`d4f06d0`)\ncarries the November side only up to `1afc164`.\n\nConsequences before this reconciliation: the November text lacked the\nOctober corrections of known defects in Lemma Layers, and the Lean proof of\nthe scalar Alice coefficient in `~/herramientas` (commit `2a7342b`) was\nwritten against the October statement (source SHA256 `2075e840…`, commit\n`08d5981`), which the November text did not contain.\n\n## 2. Method\n\n`git merge-file --diff3` of the November file against the October file\nwith the ancestor as base, for `.tex` and `.md`.\n\nFor the Markdown transcription the two sides had renumbered the reference\nlist differently (October inserted two entries at positions 10–11;\nNovember appended three at 20–22). Before merging, the ancestor and the\nNovember file were renumbered to the merged order (`n >= 10 -> n + 2` in\ncitations and in the list). After the merge the citation numbers were\nlisted and compared with the order of `\\bibitem` in the merged `.tex`\n(24 entries, same order).\n\n## 3. Conflicts and their resolution\n\nFour in `.tex`; the same four plus one reflow conflict in `.md`.\n\n1. **Literature, two-dimensional walks.** Both kept: the November sentence\n   on the shape theorem (BGPP, Thms. 2.2–2.3) followed by the October\n   remark that explicit amplitudes outside the feasible set can be\n   obtained instance by instance. The subject of the October remark is\n   written as «Baryshnikov et al.» so that it is not read as a statement\n   about BGPP. That remark was not re-checked against arXiv:0810.5495 in\n   this session: `[UNVERIFIED]` here, inherited from `5f77de8`.\n2. **Literature, transfer theorems.** Both kept: the October sentence on\n   the DMPT path-sum solutions, then the November sentences on ACSV\n   Thms. 9.5 and 9.12.\n3. **Proof of Lemma Layers, Bob's part of (b), and (c), (d).** The two\n   sides repaired the same gap (the spinor of `r` varies across Bob's\n   region) in different ways. October splits\n   `r(y) = N^{-3/2} R_0(w_*) + rho(y)` and bounds the `rho` term in norm\n   without oscillation. November applies Leibniz to `h_N r~` with a smooth\n   Fourier interpolation of the free tail. **The October argument is\n   kept**: it is the one that went through the sanedrin, the Astra review\n   and the DeepSeek review, and it is the one the row-vector statement of\n   (b) is written for. **The November paragraph is not carried over**; it\n   remains in `341950e`. October's (c) and (d) replace the short ancestor\n   text, which the November side had left unchanged. The two closing\n   November sentences on uniformity in `theta_N` and on the endpoint\n   `delta = 0` are appended after (d).\n4. **Assembly, six non-contributing points.** Both kept: the October\n   sentence (Lemma symbol (b) transfers the Gaussian decay from the ball at\n   0), then the November sentences on the reciprocal eigenvalue branch. The\n   November sentence on the half-period identities says the same as the\n   October one and is not repeated.\n5. **`.md` only, first paragraph of the proof of (b).** November text with\n   the October insertions (`G_delta`, the condition on `r_0`).\n\nOne notation fix outside the conflicts: a November sentence in the proof of\n(b) wrote `G_0` where the October side had renamed the profile `G_delta`\n(DeepSeek remark); changed to `G_delta` in `.tex` and `.md`. One reference\nnumber inside the Markdown list (`[16] -> [18]`, the printed ACSV edition).\n\nEverything else merged without conflict. Checked by listing, for each\nside, the lines it added to the ancestor that are absent from the result:\nOctober, only the lines of items 1 and 4 that were rewritten as above;\nNovember, only the paragraph of item 3, the duplicate sentence of item 4\nand reflowed line ends.\n\n## 4. Checks run\n\n- `pdflatex` twice on the reconciled `.tex`: exit 0, 21 pages, no\n  undefined reference or citation.\n- Lemma Layers, statement: byte-identical to the frozen source of the Lean\n  proof (`runs/run_0/paper.tex`, SHA256 `2075e840…`), by `diff` of the\n  lemma environment.\n- Passages cited in the Lean fidelity table\n  (`FIDELITY_ALICE_LAYERS_B.md`: source lines 403–405, 418–437, 563–568,\n  947–952, 1017–1031, 1076–1085, 1118–1145): no `diff` hunk between the\n  frozen source and the reconciled `.tex` starts in those ranges. The one\n  hunk nearby (source lines 943–944) is the November expansion of the\n  bound on `<r, E a_c>`, a different statement.\n\nNot checked: the mathematics of either repair set; the certificates\n(not rerun); the Lean build (not rerun); the Markdown against the PDF line\nby line.\n\n## 5. Files\n\nReconciled:\n\n- `papers/ir-corona/ir-corona.tex` SHA256\n  `eed30c18a1d7d062e1f065230231073b696b1eaf7098b314f4e91a8548137dd5`\n- `papers/ir-corona/ir-corona.md` SHA256\n  `6602d1f9cf0ef84da34998a5f91ec9d010eb4bae1f49ac64c13c9cb0a943ed23`\n\n(after the read-through edits of Sec. 8; the merge alone gave\n`e62af5d2…` and `ef599e6a…`).\n\nBrought unchanged from `research/inverse-gravity-design` (`28c686e`),\nbecause the reconciled text depends on them and they were absent here:\n\n- `debates/2026-10-28--ir-corona-sanedrin.md`, `.log`, `-request.md`\n- `debates/2026-10-28--ir-corona-repairs-review-astra/` (verdict recorded\n  there: `CERRADA_CON_ARREGLOS`, two mandatory repairs, applied in\n  `f85f429`)\n- `debates/2026-10-28--ir-corona-repairs-review-deepseek/` (verdict\n  recorded there: `CERRADA`, minor remarks applied in `951bbe3`)\n- `papers/ir-corona/certificados/2026-10-28/` (certificate run outputs)\n- `reports/2026-10-28--ir-corona-prior-art-audit.md`\n\n## 6. Review coverage of the reconciled text\n\nNo review covers the reconciled file. The October reviews (sanedrin,\nAstra `gpt` family, DeepSeek) saw the October text without the November\nedits. The Opus review of 2026-11-10 saw the November text without the\nOctober repairs; the repairs applied after it were not re-reviewed. The\nmerge itself was done by a Claude model.\n\n## 7. Open after this step\n\n1. The `Repo` bibitem cites tag `ir-corona-v1`, which points to `59998ac`\n   on the October branch, not to the reconciled text. A new tag is the\n   user's decision; none was created.\n2. (Done in Sec. 8: the Markdown header now names the reconciliation.)\n3. `reports/2026-11-10--ir-corona-readiness.md` and\n   `reports/2026-11-10--ir-corona-opus-repairs.md` record SHA256 values of\n   the November text; they are historical for that text.\n4. Bob's coefficient, the matrix symbol and the assembly are not\n   formalized. (The Lean proof of the scalar Alice coefficient was moved\n   into `formal/alice-layers/` the same day, Sec. 9.)\n5. Whether `research/inverse-gravity-design` should be merged as a branch\n   (it is 271 commits apart from `main` on its own side) was not examined;\n   only the manuscript and its review records were reconciled.\n\n## 8. Read-through of the reconciled text (same day)\n\nUser instruction «revísalo completo». One complete reading of the\nreconciled `.tex` by the same Claude model that merged it. **Not an\nindependent review** (same family as part of the authorship; no second\nfamily, no person). It does not change any status.\n\nRe-derived by hand while reading, no discrepancy found: the fourteen jumps\nand their norms; `det S = 1`, the dispersion and `H_W`; the normalization\n`Z_N` and `c_r`; the separation inequalities; the constants of\nTheorem upper (`9N4^N`, `J`) and the `D_B <= 4T_N` step; the convexity\nargument for `Phi`; Lemma symbol (a), (b); the depth parametrization, the\nparity `(-1)^{j+j'}`, the two phase identities of Layers (c) and their\ncancellation in the assembly; the layer prefactors `16 pi/sqrt3` and\n`32/sqrt3`; `c_g`, `1/720`, `1/48`; the constant `K` and the power\ncount `13/2`; the `rho` bound and the `CN^{-3}` estimate of the October\nproof of (b); the total-variation estimate of the November text, which is\nconsistent with (and sharper in `delta` than) the October bound\n`CN^{-4}(1+delta)^3`.\n\nSecond route for the printed numbers (floating point, inspection only,\nnothing retained, not a certificate): `t_*`, `K_*`, `e^{Phi_*}`, `q_t`,\n`q_n` (also as eigenvalues of a finite-difference Hessian of `Phi`), `P`\n(against a numerical eigenprojector), `I_0`, `I_1`, `K`, `Gamma-bar`,\n`eps_+`, `eps_-` and twelve entries of Table 1 with their relative bounds\nwere recomputed from the definitions in the text; all agree with the\nprinted digits, and the sign margin holds in the twelve cases.\n\nEdits made after the reading, in `.tex` and `.md`, wording only:\n\n1. The sentence that CJWW count two outside-region studies appeared twice\n   in the literature paragraph (once from each side). The second\n   occurrence is removed.\n2. The DMPT sentence is moved after the ACSV sentences, which continue the\n   preceding argument.\n3. In the proof of Layers (b) the two conditions on `r_0` were stated\n   twice (October and November wording). The November duplicate is\n   replaced by a pointer to (d), where the second condition is imposed\n   with its proof of positivity (`d_0 > 0`).\n4. Markdown header: names the reconciliation.\n\nAfter these edits: compiles (21 pages, no undefined reference); the\nstatement of Lemma Layers is still byte-identical to the frozen source of\nthe Lean proof.\n\nLeft for the author, not changed:\n\n- «the shape theorem they prove … [BGPP, Thms. 2.2–2.3]» follows a\n  sentence whose subject is Baryshnikov–Brady–Bressler–Pemantle (BBBP),\n  but cites Bressler–Greenwood–Pemantle–Petkovšek. The attribution should\n  be checked in the two papers.\n- The October remark on BBBP (amplitudes outside the feasible set,\n  extension to dimension three) is unverified in this session.\n- Item 1 of Sec. 7 (tag).\n\nNot covered by the reading: the certificate scripts (not rerun), the\nanalytic remainder estimates beyond the orders checked above (uniformity\nof the Poisson remainders in `eta`, the compactness step of\nLemma symbol (e)), the Markdown line by line, and novelty.\n\n## 9. Lean proof of the scalar Alice coefficient moved into this repository\n\nAt the user's instruction the formalization was moved from\n`~/herramientas` (`2a7342b`) to `formal/alice-layers/`; record in\n`formal/alice-layers/MIGRATION.md`. 997 files copied byte-identical, three\npath edits, full offline verification rerun from the new location:\n`verification/migration_2026-11-12/verification.json`, `success: true`,\n38 modules, proved targets `ProfileIntegrability`, `AliceLayersB`, 57\ncopied definitions equal, Lean source hashes equal to the pre-migration\nrecord `assembly_final01`. Mutation campaigns not rerun. In\n`~/herramientas` the folder is removed from the working tree with a\npointer `MOVED.md` (uncommitted there). Scope unchanged: scalar Alice\ncoefficient only; no external review.\n\nNothing was committed in either repository.\n")` not in
  `2 pi Lambda_0^*`, `d_0 > 0` over six points, and with `r_0 <= d_0/2`
  every frequency including `m = 0` has modulus `>= d_0/2`.
- **Alice's side is also machine-checked.** `AliceLayers.aliceLayersB_proved`
  (`formal/alice-layers/`) proves the scalar statement of (b) with the
  constant fixed before `N` and `eta`, `r_0 = pi/6`, `N_0 = 2`; this is
  below the paper's bound (the shortest vector of `2 pi Lambda_0^*` has
  length `2 pi sqrt(2/3)`, about 5.13). Bob's side and (d) rest on the
  written argument.

Not done: explicit constants; a second-family or human check of these
steps.

### 10.5 Markdown against LaTeX — collated

Both files were normalized (macros expanded, citations and cross
references replaced by placeholders, markup and whitespace removed) and
compared sentence by sentence, then by numeric literal.

- Table 1: the 32 numbers are identical.
- Every decimal literal of the body coincides, apart from theorem and
  section numbers, which the Markdown writes out and the LaTeX generates.
- The 20 written-out statement numbers (Lemma 2.1 … Theorem 7.5,
  Definition 3.1, Table 1) equal the labels of the compiled `.aux`; every
  «Kind N.M» mention in the Markdown is one of them or a remark number,
  except `Lemma 4.1`, which is CJWW's.
- Remaining differences are wording only, in five sentences of the
  November repairs that the Markdown paraphrases (methodology remark,
  profile expansion, endpoint `delta = 0`, `I(u) = log 4`, the ACSV
  sentence). No formula or number differs.

The normalizer was an inspection aid and is not kept; the collation is a
check, not a certificate.

### 10.6 Tag

The `Repo` bibitem (and Markdown reference 19) now cite `ir-corona-v2`.
The annotated tag `ir-corona-v2` is created on the commit that contains
this section. `ir-corona-v1` is left where it was (`59998ac`).

### Files after Sec. 10

- `papers/ir-corona/ir-corona.tex` SHA256 `4fc35d7f6ad260611be55870df6d21663d328eff06d5f0942102c702cd1bc88b`
- `papers/ir-corona/ir-corona.md` SHA256 `7c58fca1fec6b4f49f98ef234dd8dd7484d942ca3c0bdbc153215c0d9a109db7`

Compiles: 21 pages, no undefined reference. Lemma Layers statement still
byte-identical to the frozen source of the Lean proof.
