# IR-corona: checks and repairs after the Opus review

2026-11-10. Codex. User authorized checking and repairing the objections.
Status: PRELIMINARY repairs, not independently re-reviewed; NOVELTY OPEN.

## Scope and stopping condition

Known: the sealed Opus review in
`reviews/2026-11-10-ir-corona-readiness-r4/informe_opus.md` accepts the
argument in substance but requests repairs. Question: which objections
survive checking the authoritative TeX, its definitions and primary sources?
Stop if a fatal proof defect is established; do not hide it in editorial
changes. This task does not promote evidence or authorize a new external round.

The review completed with Claude Opus 5.5, tools commit 97292a9. Its checks
were documentary, not executions of certificates or Lean. Earlier three
attempts failed with EAI_AGAIN; they are not reviews. The successful review
was run outside the network sandbox. Its unaltered report remains intact.

## Objection disposition

| Item | Check and action | Remaining limit |
| --- | --- | --- |
| C-1 | Confirmed truncated sentence. Replaced the fourth-order Poisson detour by an absolute layer bound: Alice N^(-9/2), Bob N^(-5/2), spectral integral N^(-3/2), hence N^(-17/2). The first exponent also follows from resource N^(-3/2), fourth-order profile N^(-4) and planar area O(N). | Analytic repair requires re-review. |
| C-2 | Non-trivial characters must stay separated from the reciprocal lattice throughout their neighbourhoods. Added this finite positive separation to the choice of r_0. Specified the delta <= R/2 truncation, exact-depth Taylor error and uniformly summable depth moments. At zero depth the profile vanishes; no inverse depth enters. | This is a clarification of absolute bounds, not a new explicit remainder constant. |
| C-3 | Confirmed missing upper bound for I(u). The exact vertex amplitude 4^(-N), compared against every fixed tilted polynomial-times-exponential bound, forces xi.u-Phi(xi) <= log 4. Diagonal tilts give the reverse inequality. Added both directions. | No new numerical calculation. |
| C-4 | Confirmed wrong phase expansion at f=-1. There omega=pi-|q|+O(|q|^2), and the gradient has the opposite sign. Both signs still sweep the sphere. | Geometry conclusion unchanged. |
| C-5 | Existing statement already says remainder constants and N_* are not explicit and diagnostics give no exact-signal threshold. Retained that limitation. | Effective threshold and optional sharper remainder remain OPEN. No diagnostic extrapolation adopted. |
| C-6 | Confirmed the sigma_3/I sign relation follows from the exact signal expansion and subleading cosine term. Reworded its attribution. | No new discovery claim. |
| C-7 | Taylor expansion of the fixed bounded Hermitian generator gives a real-linear leading coefficient in a,b; quadratic terms have the repaired C-1 layer bound. Added the formula and changed the open problem to optimisation/subleading responses at zeros. | No general-generator admissibility theorem is asserted. The review's numerical cross-product example was not adopted. |
| C-8 | Removed the unpublished hard-cutoff cancellation assertion and its internal state-file citation from the manuscript. | No claim that the projected IR block alone equals the signal. |
| C-9 | Explicit constants establish asymptotic admissibility; they are not an effective signal-detection or accuracy threshold. | The review's numerical threshold estimates were not independently certified and are not imported. |
| C-10 | Distinguished pointwise O(N^(-3/2)) free amplitude from its O(1) regional norm upper bound on O(N^3) sites. | No N-independent exact regional norm or positive lower bound is inferred from this estimate. |
| I-1, I-3 | Abstract/discussion now formulate existence for operations satisfying the declared admissibility definition. Admissibility and the asymptotic proof are separate statements. | No exclusive IR spectral origin is claimed. |
| I-2 | Confirmed the logical scale mismatch: polynomial leakage control alone cannot bound errors relative to an exponentially small signal. Stated this limit explicitly. | The proposed UV perturbation estimate is labelled heuristic in the review and remains UNVERIFIED; it is not a new theorem here. |
| O-1 | Read the general smooth-point theorems in the original ACSV PDF, not just its walk examples; corrected the literature discussion. | Full hypothesis matching for the matrix space-time generating function and numerator cancellations remains OPEN. |
| O-2--O-4 | Replaced the priority sentence by a description of the weighted operational sum, two torus contributions and pair-specific non-vanishing. | No absence-of-prior-art inference or novelty verdict. |

The null generator example in C-7 needs an important qualification:
M=I+sigma_3 annihilates the down spinor, so its response is exactly zero.
But Definition 3.1 explicitly requires Delta_M != 0 to define encoder
admissibility. It is therefore not an admissible counterexample to the
corollary. The manuscript now says this. The review's broader phrase
"admissible generators" is not accepted on this example alone.

The I encoder is a non-trivial local phase operation. Its designation as
a reference comparison is a presentation convention, not a null control;
this is now explicit.

## Primary-source check for O-1

Source: Pemantle, Wilson, Melczer, *Analytic Combinatorics in Several
Variables*, Expanded Second Edition manuscript,
https://ACSVproject.com/PemantleWilsonMelczer23.pdf.
Downloaded PDF: `/tmp/ir-corona-acsv.pdf`, SHA256
`b9529cd711e4bdc547da8ebbb15ee31fdbd57edb05467b5f479e4182e3f5c02b`.
Printed page numbers below refer to that PDF, not the printed 2024 edition.

- pp. 264--265, Theorem 9.5: ratio of coprime polynomials with a convergent
  Laurent expansion; smooth minimal nondegenerate contributing points;
  uniformity on compact direction sets; finitely minimal case sums the
  smoothly varying local contributions.
- pp. 266--267, Theorem 9.12: the minimal-point version requires a finite
  set of smooth nondegenerate contributing critical points on the torus,
  again with uniformity over the declared compact direction set.
- p. 274, Theorem 9.25: under finite criticality and minimality the local
  contributions sum, with an exponentially smaller remainder.

Thus neither Laurent expansions nor directional uniformity exclude the
kernel from these theorems. The natural candidate is the matrix resolvent
(I-w S(z))^(-1), entry by entry. A full application must identify the
chosen Laurent expansion's convergence component, the contributing points
and possible entrywise numerator cancellations. This task records those
obligations instead of declaring them discharged. These fixed-function
transfer statements by themselves do not perform the manuscript's
N-dependent weighted operational sum. This observation is not a novelty proof.

## Validation and delivery

TeX is authoritative; the Markdown transcription has corresponding repairs.
pdfLaTeX compilation passed (20 pages, TeX Live 2023); repeated to settle
references, with no remaining undefined-reference or rerun warnings.
Overfull boxes remain; no visual-layout approval is claimed.
`git diff --check` passed. No reviewed verifier or Lean file was changed;
none was rerun, and no numerical value from the review was promoted.
The repaired manuscript still requires independent re-review. No commit,
push, submission or evidence promotion is part of this task.
