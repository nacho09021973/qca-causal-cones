# CURRENT_STATE

> **Typographic reconstruction — 2026-10-26.** The remaining historical
> formulas were restored against their already reconstructed reports. No
> historical status or criterion changed. Lost CR-derived newlines in rho,
> right and rm are explicitly checked with the opt-in reconstruction flag
> against `8dd9080`; this is separate from new dated progress entries.
> The authorized document reconstruction is complete: the integrity checker
> reports zero problems. The former review-transcript warning was a valid
> Python-list bracket inside fenced code, now covered by regression tests.
> User authorization "1 y despues 2" next covers strengthening W3–W6
> certificates, without reopening W1–W12 or promoting scientific evidence.

## Current reading guide — 2026-10-28

Branch `research/inverse-gravity-design`. Documentary summary of the dated entries
below and of the canonical sections; it changes no status. Where it disagrees
with a dated entry, the dated entry wins.

| Front | Status | Where |
| --- | --- | --- |
| Central question (c and the substrate) | Standard Weyl/Dirac gate PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS; minimal `s=2` rigidity and species universality OPEN; irreducible-isotropy charter OPEN, Steps 0–1 authorized (2026-10-28); NOVELTY OPEN | Sections 4–7; entry of 2026-10-28 |
| Flat CJWW corona | CLOSED in its frozen class; manuscript and Lean Thm 4.1; proof of Thm 4.3 repaired after sanedrin, repairs REVIEWED (Astra, DeepSeek); not submitted | Section 8.20; `papers/ir-corona/`; entry of 2026-10-28 |
| Spectral attribution C1–C3 | PASS in their frozen scopes | Section 10.1 |
| Independent-use discrimination cost | REVIEWED_PASS_WITH_REPAIRS (2026-10-22); repaired version REVIEWED_PASS (2026-10-28); corona premises not reviewed; no operational frontier at c | Entry of 2026-10-22 and its addendum |
| 4B absolute scale | `NO_ABSOLUTE_SCALE_DERIVABLE` closed in the frozen class; Sept 28 commits reconciled (`94071db`) | Reconciliation entry of 2026-10-22 |
| H1 / inhomogeneous | OPEN and paused; L2 `B / OPEN_BLOCKED_METHOD` | Section 9.7 |
| Integrity | Documentary reconstruction complete; `text_integrity --check` reports zero problems | Entries of 2026-10-22 and 2026-10-26 |
| W1–W12 gravity line | CLOSED_BY_CONTRACT. W3–W6 REVIEWED_ACCEPT_WITH_REPAIRS (reduced scope); strengthened W3/W5/W6 certificates NEW_INDEPENDENT_REVIEW_PENDING; W1, W2, W7 and the CJWW bridges reconstructed, independent review pending | Entries of 2026-10-22 and 2026-10-26 |
| W4 long-wavelength spectrum | OPEN_AFTER_AUDIT; DeepSeek ACCEPT_WITH_REPAIRS; author repairs not re-reviewed | Entry of 2026-10-26 |
| Inverse-gravity successor (IG-S0 to IG-S2) | `BOUNDED_TRANSFER_ATTEMPT_STOPPED_OPEN`; direct transfer paused | Entries of 2026-10-08 and 2026-10-10 |
| A.int, interaction-renormalized species speed | OPEN sub-question of A; no calculation contract; Eon v4 reference-state work in progress | Section 4, A — IR universality |

## Irreducible isotropy matching charter — 2026-10-28

User instruction: "prepara la carta para la hipótesis 3". Charter
[`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`](../theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md),
status `OPEN`. **Steps 0–1 authorized** by the user on 2026-10-28 ("si, autorizo los pasos
0-1"). Steps 2–3 are not authorized. It asks whether an irreducible
internal representation forces `c_0 = c_strict^iso` (B_infty^* rigidity (i)) in d=3 with the
cubic `N_3`. `D2` admits no irreducible `R` with `s > 2`, because it is abelian. The charter
therefore declares three separate classes:

- T3: tetrahedral group, `s = 3`;
- O3: cube rotation group, `s = 3`;
- O4: cube rotation group, `s = 4`, spinorial.

Its first decisive test is whether the known s=4 family is `O`-covariant with the
irreducible 4-dimensional `R`. No computation has been run. The group-orbit facts in its
Sec. 0 come from an inspection command; the irreducible dimensions are to be verified in
Step 0.

## ir-corona manuscript: sanedrin, repairs and two reviews — 2026-10-28

Direct user instructions: "lanza el sanedrín con el paper de la corona", "hazlo todo
en orden", "revision ciega con codex", "si que lo revise Deep", "el push y el
current_state". Documentary entry. It changes no gate and no frozen claim.

- **Sanedrin** (Astra, Ciro, Abner, Gemini; 2 rounds; Opus excluded as the
  manuscript's family): `DEGRADED_NO_CONSENSUS` (Gemini round 1 `MAX_TOKENS`); all
  four verdicts `ENVIABLE_CON_REPARACIONES`
  ([record](../debates/2026-10-28--ir-corona-sanedrin.md); tools: herramientas
  `0c150e8`, sanedrin `7e011a4`). Three mandatory repairs: Lemma Layers(b) wrote
  Bob's correction as a scalar times a fixed row, which is false because R_0 rotates;
  Layers(d) claimed "no m=0 term", which is false: that term sits at a shifted
  non-zero frequency; Table 1 called the reference coefficient `C-bar` a mean.
- **Certificates of Appendix A** re-run at `929fd44`, identical to the cited
  `551addabe28b`: 53/53, 18/18, 58/58, 27/27
  ([record](../papers/ir-corona/certificados/2026-10-28/README.md)).
- **Repairs** (`cd8ff54`): a norm-bounded residual row `E_B`, propagated with norms
  through Assembly; a bound on all shifted frequencies with
  `||d^3 G_delta||_M <= C N^-4 (1+delta)^3`, summable in depth; Table 1 caption
  "Reference coefficients".
- **Review 1**, Astra (sealed, `revision-ciega`): `CERRADA_CON_ARREGLOS`. Two
  fixes were applied in `f85f429`: the site count `O(1+N delta')`, and the global phase
  `e^{-i pi theta_N}` near `pi u` with its cancellation in Assembly (a defect older
  than the repairs) ([author reading](../debates/2026-10-28--ir-corona-repairs-review-astra/verificacion_autor.md)).
- **Review 2**, DeepSeek (sealed; herramientas `83c04f9`, third attempt;
  earlier attempts archived): `CERRADA`, no mandatory repairs. Its two minor remarks
  and the undefined `G_0` were applied in `951bbe3`
  ([author reading](../debates/2026-10-28--ir-corona-repairs-review-deepseek/verificacion_autor.md)).

Status of the manuscript proof of Thm 4.3: `REPAIRED; REPAIRS_REVIEWED`. The
statements of Theorems 4.1–4.4, `K_*`, the exponent 13/2 and Table 1 values are
unchanged. Open before submission: the short author lines of `f85f429`/`951bbe3`
are unreviewed; bibliographic priority: `NO_ANTICIPATION_FOUND / NOVELTY OPEN`, with three
[UNVERIFIED] items ([prior-art audit](../reports/2026-10-28--ir-corona-prior-art-audit.md)); the `Repo`
bibitem now cites the tag `ir-corona-v1` (user decision "Solo el tag por ahora");
the DOI is pending because the repository is private. The manuscript is not submitted;
submission is a separate user decision.

## W4 full-spectrum audit and review preparation — 2026-10-26

Direct user instruction authorizes this focused audit and preparation of an
independent review. Current W4 long-wavelength interpretation:

```
W4_LONG_WAVELENGTH_SPECTRUM = OPEN_AFTER_AUDIT
LOCAL_ALGEBRA_AND_OBSERVABLE_CHECKS = PASS
EVIDENCE = AUTHOR_CHECKED / INDEPENDENT_REVIEW_ACCEPT_WITH_REPAIRS / AUTHOR_REPAIRS_CHECKED
```

The [audit](../reports/2026-10-26--w4-spectrum-audit.md) supersedes the physical
reading of the historical SMOOTH_MODE_GAPPED / STAGGERED_GAPLESS_ONLY label.
The full same-sign step fixes the uniform one-defect state and has
epsilon(k)=tan(kappa) k²/4+O(k^4) for fixed 0<kappa<pi/2. The zone-edge
crossing is centered at 2kappa modulo 2pi relative to the fixed vacuum.
The opposite-sign control has a linear node at zero with slope |sin(kappa)|
in two-register cells per complete two-layer step: 2|sin(kappa)| registers
per step. The full-SWAP endpoint is checked separately.

The strengthened spectrum certificate and new observable certificate turn
the earlier manual checks into permanent exact checks, with a second
real-space construction on L=4,6 qubit rings. A cell-pi eigenstate can have
uniform stationary Z. Around the polarized vacuum, a coherent small defect
changes Z only at second order in its amplitude; equal initial Z profiles
can have different next Z because coherences matter. These facts do not
establish a linear metric wave or rule out other backgrounds/observables.

All 43 verifiers pass in the retained
[sweep](../reports/2026-10-26--w4-audit-verifier-sweep.tsv); the adjacent
SHA256 manifest identifies the exact executed certificate bytes above the
recorded base HEAD. The new W4 checks use exact arithmetic, not fitted spectra.

The [review package](../debates/2026-10-26--w4-spectrum-review-deepseek/README.md)
was sent to a different model family in one bounded round. The completed
DeepSeek report returns ACCEPT_WITH_REPAIRS. Its five objections were checked
and addressed locally in the [repair record](../reports/2026-10-27--w4-review-objections.md);
the reviewer has not checked the subsequent changes. Completion does not
promote evidence.
The prior
W4 stiffness review does not cover this corrected spectrum interpretation.
No model replacement, evidence promotion, new 3D/tensor calculation or
reopening of W1–W12: it remains CLOSED_BY_CONTRACT.

## Authorized options 1 and 2 completed locally — 2026-10-26

Direct user authorization "1 y despues 2": documentary reconstruction is
complete, with zero problems from `text_integrity.py --check` and six guard
regression tests passing. See the
[reconstruction closure](../reports/2026-10-26--document-reconstruction-closure.md).

The W3/W5/W6 certificate implementation obligations from October 22 are now
`IMPLEMENTED_AUTHOR_CHECKED / NEW_INDEPENDENT_REVIEW_PENDING`:

- W3 derives E from the edge-current Fourier transform and the CJWW transport
  first jet. The O(g²) feedback remains mean-field, not the correlated result.
- W5 checks all three current families, the zero eigenspace, exact local kick
  and derivative of the leading transport generator with respect to each z.
- W6 derives all nine variations and supplies F1/F5/F6 local witnesses plus a
  conservative 90-layer schedule for the added interaction. Exact matter
  recovery requires g=eta=0, leaving K_geometry tensor U_CJWW. The schedule
  is an admissible explicit witness, not a unique historical ordering or full
  CJWW circuit synthesis. Matching proof uses parity; L=4,6 coverage controls
  and omitted-layer/source-on negative controls pass.

The [implementation record](../reports/2026-10-26--w3-w6-certificate-strengthening.md)
states the hypotheses and exclusions. All 42 verifiers pass in the
[sweep](../reports/2026-10-26--strengthened-verifier-sweep.tsv); its baseline
HEAD plus the linked SHA256 manifest identify the executed code. These modified
certificate bytes do not inherit the earlier independent review. No scientific
evidence promotion, source-conservation proof, metric-wave/gauge claim or new
model authorization. The W4 spectrum qualifications remain; W1–W12 stays
CLOSED_BY_CONTRACT. Options 1 and 2 require no remaining implementation work
within their stated local-verification scope.

## Exact CJWW dynamic-graph bridge reconstruction — 2026-10-26

User continuation "adelante" to documentary block h. The bridge contract
and report pass reconstruction against `2d144d9`. The self-contained proof
was checked manually by purity/linearity and by channel operators, including
the separable-Hilbert-space continuity step and quantifier controls in the
[local record](../reports/2026-10-26--cjww-exact-bridge-reconstruction.md).
No dedicated executable certificate was found or claimed for this lemma.
Text-integrity warnings decrease from 119 to 65; no code changed.
`STRONG_EXACT_BRIDGE_IMPOSSIBLE` retains the fixed pure background, exact
unitary matter channel for every input and simultaneous information-bearing
backreaction quantifiers. It does not forbid input-independent geometry
evolution or all dynamical-geometry models. No new independent review,
evidence promotion or successor execution. W1–W12 stays CLOSED_BY_CONTRACT.
Next documentary block: G0 normalization and dynamical model-class selection.

## W7 spin-2 kinematics reconstruction — 2026-10-26

User continuation "ADELANTE" to documentary block g. The W7 contract and
report pass reconstruction against `2d144d9`; the kinematics certificate
passes its four check blocks. Basis, kernel and representation arguments
were contrasted manually in the
[local record](../reports/2026-10-26--w7-spin2-reconstruction.md).
The `9 = 3 + 1 + 5` decomposition is a matrix-representation result, not a
proof of microscopic continuous SO(3) symmetry or local gauge invariance.
Section 4 dynamics closure is conditional on a common componentwise linear
operator; the certificate does not derive a closed microscopic expectation
equation. No TT constraint or physical graviton is established.
Text-integrity warnings decrease from 165 to 119. No code was changed;
there is no new independent review or evidence promotion. The state remains
`SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN`; W1–W12 stays
CLOSED_BY_CONTRACT. Next documentary block: exact CJWW dynamic-graph bridge.

## W5 spatial-tetrad completeness reconstruction — 2026-10-26

User continuation "ADELANTE" to documentary block f. The spatial-tetrad
completeness contract and report pass reconstruction against `2d144d9`;
`verify_w5_spatial_tetrad_rank.py` passes both checks. The ranks 3/9 and 3/6
require nonzero g; both maps have rank zero at g=0. Independent-entry minors
and three image relations were checked manually in the
[local record](../reports/2026-10-26--w5-spatial-tetrad-reconstruction.md).
Global text-integrity warnings decrease from 211 to 165. No code changes,
new independent review, gauge construction or evidence promotion.
`RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN` retains its
first-order scope. This is not the W5 tetrad-source gate; the W3 mean-field
and W4 spectrum qualifications remain in force. W1–W12 stays CLOSED_BY_CONTRACT.
The next documentary block is W7 spin-2 kinematics reconstruction.

## W4 spectrum reconstruction and interpretation limits — 2026-10-26

User continuation "adelante" to documentary block e. Both W4 spectrum texts
pass reconstruction checks against `2d144d9`; the spectrum and stiffness
certificates pass. Text-integrity warnings decrease from 249 to 211; no code
changed. The [local record](../reports/2026-10-26--w4-spectrum-reconstruction.md)
documents additional manual checks and material qualifications:

- The spectrum certificate removes `exp(-2i kappa)` from the same-sign
  one-defect sector while the full gate fixes the vacuum. Restoring that
  phase gives a zero-quasienergy uniform branch at k=0, quadratic for fixed
  `0 < kappa < pi/2`. Historical `SMOOTH_MODE_GAPPED` applies to the
  rephased matrix, not an absence of a zero branch of the full gate.
- `|sin(kappa)|` is a slope in two-site cells per two-layer step; it is
  `2|sin(kappa)|` in neighboring-register units for unit register spacing.
- A defect-amplitude Bloch phase does not itself determine an alternating
  Z expectation or a propagating metric mode. That observable map remains open.

These qualifications govern the historical W4 spectrum table and execution
record below. `W4_REPAIR_AVAILABLE_SMOOTH_GAPLESS` retains only the recorded
phase-stripped algebra and 1D control, without independent review of this
corrected interpretation, model replacement or evidence promotion. W1–W12
stays CLOSED_BY_CONTRACT. The next text-reconstruction block is W5 spatial
tetrad completeness; no further calculation is executed in this block.

## W3 curvature/dynamics typographic reconstruction — 2026-10-26

User continuation "adelante" to block d of the October 22 work sheet. The
curvature/dynamics contract and report pass reconstruction checks against
`2d144d9`; the related W3 backreaction certificate passes its four checks.
The metric expansion and curvature witness `R^(1) = -4g f''(x2)` were checked
manually by two formulations, with scope and provenance in the
[local record](../reports/2026-10-26--w3-curvature-dynamics-reconstruction.md).
The certificate itself does not compute curvature or derive E from the walk.
Global text-integrity warnings decrease from 301 to 249; no code changed.
The source retains separable/mean-field qualifications. C1/C2 PASS and
C3/C4 FAIL remain `COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL`;
no evidence promotion or reopening of W1–W12. The next documentary block
is W4 long-wavelength spectrum reconstruction.

## W1 coarse-metric typographic reconstruction — 2026-10-26

The coarse-metric contract and report also pass reconstruction checks against
`2d144d9`, completing block c of the October 22 work sheet. Across the four
documents, global text-integrity warnings decrease from 411 to 301. The
[local record](../reports/2026-10-26--w1-coarse-metric-reconstruction.md)
flags a missing factor g in the historical H_g display, preserved rather
than silently repaired, and limits the eigenphase argument to the frozen
local symbol or homogeneous background. The related geometricity certificate
passes; the metric argument was checked manually, without independent review.
`W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION` retains that scope.
No scientific evidence promotion, code changes or reopening of W1–W12.
The next documentary block is W3 curvature/dynamics reconstruction.

## W1 geometricity typographic reconstruction — 2026-10-26

User continuation "adelante" to the geometricity/coarse-metric documentary
block. The geometricity contract and report pass reconstruction checks against
`2d144d9`; `verify_w1_geometricity.py` passes its five checks. The
[local record](../reports/2026-10-26--w1-geometricity-reconstruction.md) traces
manual checks, a specified initial spin witness and the outer-boundary argument.
Only backslashes were restored outside provenance headers; no code changed.
The operational PASS retains `FINITE_TIME_EXACT_SUPPORT_ONLY`, without metric
or Einstein interpretation. W1–W12 stays CLOSED_BY_CONTRACT.

## W1 perturbative-bridge typographic reconstruction — 2026-10-26

User continuation "commit y push y continúa" after W2. The W1 perturbative
bridge contract and report have restored LaTeX; both reconstruction checks
pass against `2d144d9`. The related geometricity certificate passes, but does
not certify the full reduced-channel derivation. Manual operator and exact
environment-overlap checks are recorded in the
[local verification record](../reports/2026-10-26--w1-typographic-reconstruction.md),
including qualifications on nonzero-coupling recurrences and finite-box size.
Global text-integrity warnings decrease from 499 to 411, with none in these
two reconstructed documents. No code or scientific status changes.
W1–W12 stays CLOSED_BY_CONTRACT; the later W1 scalar-potential/no-metric
conclusion stands. W1 geometricity/coarse-metric text reconstruction remains
the next documentary block.

## W2 typographic reconstruction — 2026-10-26

Direct user continuation "adelante" to the bounded W2 reconstruction.
The transport contract and both W2 reports now have restored LaTeX;
`scripts/check_reconstruction.py` passes for all three against `2d144d9`.
The W2 certificate passes. The global text-integrity check decreases from
611 to 499 warnings, with none in these three documents; the remaining
reconstruction queue is still open. No certificate code was changed.
[Local verification record](../reports/2026-10-26--w2-typographic-reconstruction.md).

No scientific status changes: `W2_PRINCIPAL_SYMBOL_CONTROL = PASS` and
`W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL`. The later conservation
audit supersedes the original dynamical-tetrad interpretation. W1–W12 stays
CLOSED_BY_CONTRACT. This block does not execute W1 reconstruction or open
a successor model.

## Independent review of W3–W6 — 2026-10-22

Sealed reviews of the reconstructed W3, W4, W5 (tetrad-conjugate source) and W6
records by Astra and DeepSeek: **ACCEPT_WITH_REPAIRS for all four gates** from both.
No error was found in the exact identities. The author checked and accepted the
repairs ([verification](../debates/2026-10-22--w3-w6-review-astra/verificacion_autor.md));
they are appended to each report. Evidence moves from PRELIMINARY to
`REVIEWED_ACCEPT_WITH_REPAIRS`, with reduced scope:
- **W3:** backreaction is mean-field only.
- **W4:** transport of a discrete curvature witness via the full-SWAP case.
- **W5:** semiclassical directional variational relation.
- **W6:** exact ranks for g≠0. The displayed full-step flat identity is
  corrected to K_kappa⊗U_CJWW; matter recovery needs eta=0.

Pending obligations: certificates that derive E(z) from J_a(p), dH/dz, J_a(p) for
a=1,2,3, and W6 F1/F5/F6; an explicit W6 finite-depth schedule. W1–W12 remains
CLOSED_BY_CONTRACT and is not reopened.

## Reconstruction progress — 2026-10-22

User continuation "adelante". The W3, W4, W5 (tetrad-conjugate source) and W6
contracts and reports have been typographically reconstructed (8 documents).
`scripts/check_reconstruction.py` certifies that each differs from the logged
mechanical repair `2d144d9` only by restored backslashes. The formulas were
checked against the four certificates, which pass. Lost `\ne` and `\nu`
newlines were restored where found. One edit (W4 report) was applied with an
inline snippet; the commit diff and the checker record its full effect.
`text_integrity.py --check` still lists 26 documents for manual
reconstruction. The W3–W6 independent review has been launched on the
reconstructed text. No scientific status changes.

## Integrity audit: corrupted LaTeX and non-executing certificates — 2026-10-22

While preparing the authorized W3–W6 independent review, two defects were found.
The user instructed: "es un proyecto a largo plazo, no se trata de poner parches".
[Audit report](../reports/2026-10-22--escape-corruption-audit.md).

- **Certificates.** `verify_w2_transport_tetrad.py` and `verify_w5_tetrad_source.py`
  could not pass under pinned SymPy 1.14.0 since they were added (structural `==`).
  The identities are true; both are fixed via `certificate_utils.assert_sym_equal`.
  All 42 verifiers pass (`reports/2026-10-22--verifier-sweep-after-fix.tsv`).
- **Documents.** 36 tracked documents from 2026-09-20/30 (W1–W7 reports and frozen
  contracts, CJWW bridges, G0/model class, part of this file) went through a
  JSON-style escape layer. Escape sequences became control characters; other
  backslashes were stripped without trace. A logged mechanical repair restored 578
  certain cases. The rest needs **manual reconstruction**, and until then the math
  of those documents is not reviewable.
- **Evidence impact.** No scientific status changes. The W12 blind reviewers
  received the corrupted W6 contract. W1–W7 PRELIMINARY results are not sent to
  independent review until their text is reconstructed. 29 of the 42 verifiers lack
  a `scripts/README.md` entry stating their scope.
- **Prevention.** `scripts/text_integrity.py --check` and
  `scripts/run_all_verifiers.py` are now mandatory before commits (AGENTS.md,
  CLAUDE.md).
- **Next, in order:** reconstruct the corrupted documents (W3–W6 first, each
  formula checked against its certificate; ambiguities marked, not guessed); add the
  missing README scopes; then the W3–W6 independent review.

## Reconciliation of the September 28 local commits — 2026-10-22

User continuation "adelante". The commits `16c4f0f` and `13d398a`, once described
as unavailable, exist locally and on `origin/main`. They are not ancestors of
this branch: the merge base is `a19c647`. `16c4f0f` adds the
[September 28 4B report](../reports/2026-09-28--physical-realization-absolute-scale-gate.md),
now imported unchanged as a historical record. `13d398a` records on main a
direct user decision of 2026-09-28 closing 4B as `NO_ABSOLUTE_SCALE_DERIVABLE`
for the frozen flat CJWW (5.15) class.

Reconciliation:
- **Outcome:** concordant with the September 25 execution (same terminal state,
  same class).
- **Authorization chronology:** the September 28 report states that only
  contract freezing was authorized. It was written on `a19c647`, which lacks the
  September 25 record of execution authorization ("Pues vamos con el 8.21",
  2026-09-25 14:54 UTC; Sec. 8.21). The September 25 record stands.
- **Closure:** the September 28 user decision is recorded as the terminal closure
  of 4B in its frozen class. It does not raise the evidence level of the analysis
  (Sept 25: PRELIMINARY / partial external review).

This resolves the "4B chronology correction" and the reconciliation part of
"Next step before new research" in the reading guide. No gate is reopened or
promoted, and main is not merged into this branch.

## Independent review of the iid discrimination-cost report — 2026-10-22

Direct user instruction "adelante con 2 y 3, autorizado" (consolidate before new
research; external review authorized). Sealed reviews of the
[September 28 report](../reports/2026-09-28--iid-message-discrimination-cost.md):
Astra `PASS_WITH_REPAIRS` (three mandatory repairs), Gemini `PASS`. The author
checked the three repairs and accepted all of them:
- an upper bound on C was asserted without a premise; it is replaced by the
  derived polynomial bound `|C| <= 8 N^{19/2}(1+10N)`;
- "only if polynomial" per-copy cost is false as a necessary condition;
  subexponential is sufficient;
- (8)-(10) are restricted to one-particle-sector unitaries.

They are applied as a dated addendum
([verification](../debates/2026-10-22--iid-discrimination-cost-review-astra/verificacion_autor.md)).
Central result unchanged: `R_eps = Theta(delta_N^-2)` for the sixteen frozen pairs,
and the one-particle necessary bound (10). Inherited corona premises were out of
scope. Status: `REVIEWED_PASS_WITH_REPAIRS`, with the repaired version not
re-reviewed. This supersedes "PRELIMINARY, independent review pending" in the
reading-guide row. The reconciliation of the unavailable local commits (`13d398a`,
`16c4f0f`) remains undone. No gate is promoted, and no operational frontier at c
is claimed. Same-day documentary commit: the 2026-10-08 elastic atlas audit.

**Addendum re-review — 2026-10-28.** Direct user instruction "sigamos con la
revisión del coste de discriminación", then "Re-revisar el addendum". Sealed
single-round review of the repaired report (sha256 `9838662a…`, last commit
`262ce03`) by Grok (grok-4.7), a house that did not take part in the
2026-10-22 round: `PASS`, no mandatory repairs
([review and author reading](../debates/2026-10-28--iid-discrimination-cost-addendum-review-grok/verificacion_autor.md)).
The author re-derived R1 independently from `ir-corona.tex` (D_B >= delta at
l.462; the rate bound at l.576) and it agrees. Non-mandatory notes: the polynomial
bound on C is sufficient, not necessary (log|C| = o(N) suffices); the report header
still reads "without independent review" and is superseded by its addendum.
Status: `REVIEWED_PASS_WITH_REPAIRS; repaired version REVIEWED_PASS`. Inherited
corona premises remain outside all three reviews. No gate is promoted, and no
operational frontier at c is claimed. Correction (2026-10-28): the sentence above
in the 2026-10-22 entry saying the reconciliation of `13d398a`/`16c4f0f` "remains
undone" was superseded the same day by the reconciliation section above (`94071db`).

## IG-S2 bounded mixed-cost transfer attempt — 2026-10-10

Direct user instruction "Intentalo"; the existing sufficiency contract's
dated continuation was frozen at `2a9c1b9` before derivation.
The [dated report continuation](../reports/2026-10-08--ig-s2-mixed-test-sufficiency.md#7-bounded-mixed-cost-transfer-attempt--2026-10-10)
derives the exact ground-energy block identity
`F=X† M^+ X+R`, with `R>=0`, including singular M and complete
ground-space degeneracy. PSD gives a lower bound, not the required upper
bound; the remainder is uncontrolled. Two global qutrit charge differences
also exclude full-operator reconstruction of the fixed curvature pair
from the neutral mixed-generator algebra, even after products and
translations. Its full-trace residual is bounded away from zero.
This is NOT a lower bound in the true ground state, and the charges are
not asserted to be symmetries of the full H_N.

`BOUNDED_TRANSFER_ATTEMPT_STOPPED_OPEN`; no upper numerator or Rayleigh
bound obtained. The full frozen ground-test family and N-type spectrum
are not refuted. Results are author-side analytic only; no new scientific
script, numerical execution, independent review or scientific promotion.
The recommendation is to pause this direct transfer route until a concrete
ground-sensitive estimate is available. No further test hierarchy is opened;
`TENSOR_SPECTRAL_GATE_OPEN` and earlier closed/paused fronts are unchanged.

## IG-S2 mixed-test sufficiency audit — 2026-10-08

User continuation; [contract](../theory/INVERSE_GRAVITY_MIXED_TEST_SUFFICIENCY_GATE.md)
frozen at `cb25f19`, permanent auxiliary code at `b6ed04b` before execution.
The [author-side analysis](../reports/2026-10-08--ig-s2-mixed-test-sufficiency.md)
exhibits tau: maximally mixed diagonal registers and zero-momentum faces.
It passes all curvature-angle polynomial ground inequalities and the fixed
mixed stationarity tests, but has constant curvature numerator
`J*diag(36,99/2)`. This refutes sufficiency of that specified relaxation,
not all tests in the full common commutant or the true-ground estimate.
A genuine two-operator ground-cost PSD condition for `{P_i,S_i P_i}`
excludes tau: its matrix determinant is `-U2^2/4`, with an explicit coherent
cost `-U2^2/(150 J)`. Exact auxiliary controls passed; no independent review.
No bound relating the admitted mixed-cost matrix to the true-ground tensor
numerator is established. `TENSOR_SPECTRAL_GATE_OPEN`; no promotion.

## IG-S2 mixed local stationarity test — 2026-10-08

User-authorized mixed-test obligation, [contract](../theory/INVERSE_GRAVITY_MIXED_GROUND_TEST_GATE.md)
frozen at `c15bde3` and permanent auxiliary code at `47ddd26` before execution.
The [author-side proof](../reports/2026-10-08--ig-s2-mixed-ground-test.md)
fixes P_i=1_{Lxx(i)=0} and Y_i=i(P_i S_i^dagger-S_i P_i).
Its full-H_N stationarity residual in the zero-momentum product state is
exactly -3 U2: the scalar penalty connects the selected configurations;
diagonal terms and H_g cannot supply that transition. Thus this local mixed
test excludes the false positive admitted by curvature-only ground tests.
The proof also gives a local trace-norm distinction from every true ground
density, with its explicit local-commutator norm dependence.
`MIXED_STATIONARITY_TEST_ANALYTIC_PASS_AUTHOR_SIDE`; exact auxiliary
[controls](../reports/2026-10-08--ig-s2-mixed-ground-test-certificate.txt) passed.
Stationarity is necessary, not sufficient, for ground-state admission.
No curvature-cost, Gram or spectral bound is obtained; no independent review
or scientific promotion. `TENSOR_SPECTRAL_GATE_OPEN`.

## IG-S2 restricted ground-cost certificates — 2026-10-08

User-authorized continuation of the true-ground cost obligation, with
[contract](../theory/INVERSE_GRAVITY_GROUND_COST_CERTIFICATE_GATE.md)
frozen at `db2e5f6`. The author-side
[analysis](../reports/2026-10-08--ig-s2-ground-cost-certificate-obstruction.md)
gives an exact local positive-certificate principle without knowing E0.
No actual small-cost certificate is obtained.
Ground tests confined to the common commutant of H_U and H_g admit the
momentum-zero product state, whose curvature cost remains positive and
volume independent. Such tests cannot certify a vanishing upper cost,
even if all supports and coherent combinations within that algebra are used.
Individual unitary-cost tests also cannot certify a strictly positive lower
cost by this positive-certificate form, by the full-trace obstruction.
These are restrictions on certificate classes, not on the true N-type spectrum.
The unchanged curvature verifier was rerun successfully; no new scientific
script, optimization or independent review was performed.
`RESTRICTED_GROUND_CERTIFICATE_CLASS_FAIL / NTYPE_GROUND_COST_OPEN`.
The next local-test obligation is an explicit mixed angle/momentum variation
outside that commutant which excludes the product-state false positive.
The zeroth-moment O(L^-4) condition belongs to a stronger sufficient route;
it is not necessary for the spectral target at the sampled momentum alone.

## IG-S2 true-ground-space sum-rule audit — 2026-10-08

The user instructed continuation using the true full-H_N ground space.
[Contract](../theory/INVERSE_GRAVITY_GROUND_SPACE_SUM_RULE_GATE.md) frozen at
`f57b0e6`, permanent auxiliary code at `1bfa5a7` before execution.
The [report](../reports/2026-10-08--ig-s2-true-ground-sum-rules.md)
derives `D=2F` in the canonical real ground density and reduces the axial
numerator to five finite-range local ground-expectation matrices.
Quartic polynomial cancellation is characterized by coefficient ratios
`(1,-4,6,-4,1)`; quantitative finite-size moment rates are stated separately.
No actual N-type ground moment has been evaluated or bounded.

The zeroth moment is the true-ground-space energy cost of the p=0 probes.
Stationarity implies positivity, not its vanishing. The immediate missing
quantity is its L-uniform finite-size bound.
An auxiliary three-level example refutes inference of two physical excited
states from rank two of a ground-averaged Gram alone.
The [local certificate](../reports/2026-10-08--ig-s2-true-ground-sum-rule-certificate.txt)
passed with exit 0; it is not a N-type vacuum calculation or independent review.
`NTYPE_GROUND_MOMENTS_UNKNOWN / TENSOR_SPECTRAL_GATE_OPEN`.

## IG-S2 constraint-preserving curvature probes — 2026-10-08

The user accepted the bounded R-operator route to test exact constraint
preservation, axial TT tangent content and derivative factors.
The [contract](../theory/INVERSE_GRAVITY_CURVATURE_PROBE_GATE.md) was frozen at
`6ef247d` and the permanent local code at `63ca29d` before execution.
The [report](../reports/2026-10-08--ig-s2-curvature-probe-preflight.md)
records `CONSTRAINT_PRESERVING_PROBE_PASS_AUTHOR_SIDE /
AXIAL_TANGENT_TENSOR_SYMBOL_PASS_AUTHOR_SIDE` for a fixed R_xx/R_yy/R_xy
compact pair. Each probe commutes with every S/V and hence H_U; H_g also
commutes, so the full double commutator reduces exactly to H_J.

The axial tangent multiplier is `4 sin(p/2)^2`, of order p^2.
A product-state witness with double-commutator expectation
`J*diag(207/4,54)` refutes a state-independent p^4 operator-norm bound.
The [exact certificate](../reports/2026-10-08--ig-s2-curvature-probe-certificate.txt)
passed with exit 0. Its fixed-torus checks are auxiliary to the analytic
all-volume identities, not a spectral extrapolation.
`GROUND_STATE_CORRELATION_AND_TENSOR_SPECTRUM_OPEN`:
the formal derivative multiplier is not an exact replacement of compact
operators. No true-vacuum Gram/energy estimate or helicity mode count is
established, and no scientific promotion or independent review is recorded.

## IG-S2 method-three author-side preflight — 2026-10-08

Direct user instruction "ok, primero el metodo tres" selects the commutator
route. The [contract](../theory/INVERSE_GRAVITY_SMA_TENSOR_PREFLIGHT_GATE.md)
was frozen at `737e2a6`, with permanent local code at `d402af8` before
execution. The [report](../reports/2026-10-08--ig-s2-method-three-commutator.md)
derives the exact full-H_N double commutator for a fixed compact sine-probe
pair on q=3 even tori. Its true-ground expectation obeys
`0<=F<=D<=(216 U1+36 J) I_2` uniformly in volume.
Exact local controls passed with exit 0 and SymPy 1.14.0; the
[certificate](../reports/2026-10-08--ig-s2-method-three-certificate.txt)
checks local identities and witness coefficients, not a many-body spectrum.

A product-state witness refutes a state-independent O(p^2) operator bound
for this pair. The alternate route is
`SPECTRAL_UPPER_BOUND_CONDITIONAL_ON_GRAM`: a true-ground-space-subtracted
Gram bound `G(p_L)>=g_* L/(2pi) I_2` would suffice. That bound and physical
tensor admission remain OPEN. The probes have TT tangent motivation but
carry microscopic constraint charge. Six finite-order staggered Z symmetries
and local variance sum rules do not alone imply the missing divergence.
No independent review, spectral promotion, rest-sector separation, QCA
energy–tick bridge or Einstein result is obtained.

## IG-S2 documentary continuation and corrections — 2026-10-08

On `research/inverse-gravity-design`, the user requested the N-type ground-energy
preflight, fixed the projected q=3 reference at `801bc0e`, and then requested
five references or five methods. The
[five-method report](../reports/2026-10-08--ig-s2-five-ground-energy-methods.md)
formulates local positive certificates, residual bounds, matrix commutator
bounds, thermal trace bounds and exact block elimination.
Status: `METHODS_FORMULATED / NTYPE_SPECTRAL_UPPER_BOUND_OPEN`.
Their finite-dimensional implications are author-side derivations; the
N-type quantitative hypotheses have not been established or independently
reviewed. This is a documentary checkpoint, not a spectral promotion.

The proof published at `edf54ff` misread H_J's trace cosine. The
[corrected refutation](../reports/2026-10-08--inverse-gravity-ground-reference-refutation.md)
retains that provenance and rederives the same non-eigenstate conclusion for
the fixed q=3 reference and positive J. The initial audit's assertion that
every variational route requires separately knowing E_0 is also corrected:
ground-state commutator identities can cancel E_0, subject to correlation
and complete-ground-space orthogonality bounds. The five-method formulation
itself opened no microscopic probe pair; the later direct selection of M3
is recorded above. All gravity and energy–tick obligations remain OPEN.

## Branch-local inverse-gravity successor — 2026-10-08

Direct user instruction authorizes opening the independent research line on
`research/inverse-gravity-design`, based on `0a4606c`. Its
[charter](../theory/INVERSE_GRAVITY_DESIGN_CHARTER.md) fixes a 3+1-dimensional
Einstein-gravity target and an initial fixed-lattice, finite-local-dimension,
strictly causal unitary QCA envelope. Interacting many-body construction is
allowed within this separately chartered line. Exact CJWW recovery is not a
requirement; no earlier gate is reopened.

Status: `CHARTER_OPEN / CONTROL_TICK_SPECIFIED / IR_UNDEFINED`.
Current authorized continuation: the user accepted the recommendation to
design the state/IR mechanism before another tick. The
[IG-S0 state-first contract](../theory/INVERSE_GRAVITY_STATE_FIRST_GATE.md)
opens a separately specified architecture preflight within this branch.
Priority: jointly construct a strictly local tick and a conserved local
energy with a controlled correlated ground reference; the relation between
energy and tick phases is a separate admission condition. The previous
control tick and A/B outcomes below retain their scope.
The contract/code were frozen at `9bd3003`; a symbolic-generator comparison
was repaired at `2dad9c4`, retaining the failed attempt. Exact auxiliary
controls then passed with exit 0. The
[IG-S0 report](../reports/2026-10-08--inverse-gravity-state-first.md) records
`STATE_FIRST_PREFLIGHT_COMPLETE_AUTHOR_SIDE` and
`STATE_FIRST_CONSTRUCTION_OPEN / NO_NEW_RULE_SPECIFIED`.
It derives the full-rank reduced-state obstruction to nontrivial gatewise
vacuum preservation, distinguishes a frustration-free Hamiltonian gap bound
from QCA phases, and excludes positive linear gapless bands in a fixed-size
analytic positive one-particle symbol. Each statement retains its hypotheses;
none is a general QCA/gravity no-go. The next construction must supply a
concrete `(K,U)` and controlled ground reference before its spectrum.
R1 is not passed. No external review is opened.

The user then authorized a concrete energy/tick construction. The
[IG-S1 dressed-parent contract](../theory/INVERSE_GRAVITY_DRESSED_PARENT_GATE.md)
and code were frozen at `67fd3b1`, then executed exactly with exit 0:
`DRESSED_PARENT_ALGEBRA_PASS_AUTHOR_SIDE`. A commuting physical projector
parent K_0 is conjugated by the fixed T circuit D, with circuit-defined
`U_E=D F D†`, `K_E=D K_0 D†`. Conservation, inverse and finite-volume ground
projector are explicit. The
[result](../reports/2026-10-08--inverse-gravity-dressed-parent.md) closes this
recipe as `DRESSED_COMMUTING_PARENT_REJECTED_FOR_GAPLESS_PROPAGATING_TARGET`:
`2<=gap(K_E|physical)<=16` uniformly in admitted volume, and physical
observable influence has radius <=4 cells for every integer time because
`U_E^n=D F^n D†`. This is not a general no-go for conserved-energy QCA.
Finite-volume stabilizer access does not establish a thermodynamic state
limit; the low-energy bridge is empty of excitations below energy 2.
`CRITICAL_CONSERVED_ENERGY_CONSTRUCTION_OPEN`. No parameters are rescued;
R1/R3/R4 and Einstein remain OPEN, without independent review.

Direct instruction «haz la consulta a grok» authorizes a bounded external
consultation, superseding prior no-review authorization statements only for
this assignment. Its [record](../debates/2026-10-08--inverse-gravity-grok-consult/README.md)
is `FAILED_NO_COMPLETED_RESPONSE`: initial CLI connection error and an
approved retry outside the restricted environment that timed out after 600 s.
Both exact inputs have identical hashes; all provider/state artifacts are
retained. No completed report, reviewer verdict or recommendation exists.
Scientific evidence levels and the IG-S1 closure are unchanged.

Direct instruction «prueba con deep» authorizes the same sealed assignment
to DeepSeek. Its [record](../debates/2026-10-08--inverse-gravity-deepseek-consult/README.md)
is `CONSULTATION_COMPLETED`: after retaining an initial DNS failure, the
approved retry returned `deepseek-v4-pro`, exit 0 and `finish_reason=stop`.
The exact input hash matches Grok's. DeepSeek accepts the scoped IG-S1
conservation, ground reference, gap interval and all-time support argument;
this is one completed external consultation, not an independent code run
or a gravity result. Its two formulation requests were already explicit
in the submitted report. The [author assessment](../debates/2026-10-08--inverse-gravity-deepseek-consult/verificacion_autor.md)
records that proposed A/B mechanisms lack concrete operators and gap closure;
a decreasing gap lower bound or moving fixed-cost defects is insufficient.
`CRITICAL_CONSERVED_ENERGY_CONSTRUCTION_OPEN` remains unchanged. No new model,
contract relaxation or further external round is opened by this consultation.

Direct instruction «prueba con codex» authorizes the same sealed input via
`revision-ciega astra` / `codex exec`, requested `gpt-6-astra`, effort high.
Its [record](../debates/2026-10-08--inverse-gravity-codex-consult/README.md)
is `FAILED_NO_COMPLETED_RESPONSE`: initial read-only filesystem startup
failure and an approved retry outside the sandbox timing out after 600 s.
Input hash matches Grok/DeepSeek, without DeepSeek's answer being attached.
No reviewer verdict or scientific recommendation exists. Same-family Codex
would not count as independent verification even if completed. DeepSeek
remains the only completed consultation; all scientific statuses are unchanged.

The [IG1b local-gate contract](../theory/INVERSE_GRAVITY_LOCAL_GATE_GATE.md)
and certificate were frozen at `601463b`, then executed with exact arithmetic
and exit 0: `LOCAL_CONSTRAINT_PRESERVING_NONSCALAR_GATE_PASS_AUTHOR_SIDE`.
Gu–Wen Rzz / T_x^x give a local physical Weyl pair in the q=3 constrained
sector. A non-scalar unitary gate at theta=pi/3 is certified; its three cyclic
families define a control tick, inverse, fixed-depth implementation and
author-side strict range bound <=3 cells per tick. Reference rho_L=P/Tr(P)
is stationary on the finite torus, not an energy vacuum.
See [IG1b result](../reports/2026-10-08--inverse-gravity-local-gate.md).
The [IG1c full-tick contract](../theory/INVERSE_GRAVITY_FULL_TICK_DYNAMICS_GATE.md)
and permanent code were frozen at `10ddcf6`, then executed with exact
arithmetic and exit 0. Result:
`FULL_TICK_ONE_STEP_PHYSICAL_INFLUENCE_PASS_AUTHOR_SIDE`.
For fixed physical words O/B with initially disjoint support,
`||[U^dag O U,B] psi0||=2` in the constrained sector. This proves the
full tick is non-scalar there and creates spatial physical influence in one
step. Both stencil incidences and an independent cube-vertex formulation agree.
See [IG1c report](../reports/2026-10-08--inverse-gravity-full-tick-dynamics.md).
No sustained propagation, asymptotic speed, mode count or dispersion is proved.
The [IG1d IR-reference filter](../theory/INVERSE_GRAVITY_IR_REFERENCE_GATE.md)
and algebra controls were frozen at `dd40dee`, then executed exactly with exit 0.
Result: `TRACIAL_REFERENCE_RESPONSE_NULL / TERMWISE_VACUUM_INCOMPATIBLE`.
The general trace proof gives zero mean response to all sector-preserving
unitary sources in rho_L=P/Tr(P), at every time and finite admitted volume.
This does not invalidate the nonzero physical commutator of IG1c. The physical
Weyl pair also excludes a common W=1 state minimizing each auxiliary -A_W term.
See [IG1d report](../reports/2026-10-08--inverse-gravity-ir-reference.md).
The user authorized selecting at least two state options with B as fallback.
The [IG1e A/B contract](../theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md), frozen
with algebra controls at `2bee605`, prioritizes A: constrained Gibbs of the
fixed local auxiliary H_A, conditional on exact `[U,H_A]|H_P=0`.
B is the Cesaro average under the same frozen tick of the fixed beta=1 Gibbs
seed; finite-volume stationarity is proved, but local response/IR control is not.
The [selection report](../reports/2026-10-08--inverse-gravity-ir-options-ab.md)
records exact qutrit controls with exit 0; these do not test the spatial A/B states.
The [A0 physical conservation contract](../theory/INVERSE_GRAVITY_A0_CONSERVATION_GATE.md)
and permanent code were frozen at `bc2da80`, then executed exactly with exit 0.
Result: `A0_FAIL_NONCONSERVED_PHYSICAL_PARENT`. On the fixed physical psi0,
`Delta <H_A>/L^3=43046720/14348907>0`: each conjugated R has expectation
3^-16, established using rank-16 charge independence over F3 for its affected
T gates. This rejects A's frozen conserved-Gibbs route, not all correlated states.
See [A0 result and B0 access audit](../reports/2026-10-08--inverse-gravity-a0-and-b0.md).
B0 is activated with the same beta=1 seed and tick: finite-volume stationarity
is proved, and an exact dual reduction to local observables is written.
Controlled seed expectations and time-average convergence remain absent;
the 2/M stationarity defect is not an error bound to the stationary ensemble.
The [bounded B0 access audit](../reports/2026-10-08--inverse-gravity-b0-access-audit.md),
under its [contract](../theory/INVERSE_GRAVITY_B0_ACCESS_GATE.md) frozen at
`04f0207`, closes the attempted local-average route as `B0_METHOD_NOT_CLOSED`.
Exact auxiliary controls and a general proof show that a small stationarity
defect alone is not ensemble-distance control; they do not simulate B or
prove heating/failure of the frozen QCA. Certified seed expectations and
observable-specific convergence remain missing.
`B=OPEN_BY_CONTROL_LIMITATION`, B1/B2/B3 NOT_EXECUTED;
`IR_SELECTION_OPEN_AFTER_AB`. This bounded A/B attempt is closed; a concrete
new controlled method or a separately chartered architecture is required
before further IR claims. No gate, angle, beta, weight or target is adjusted.
No gravitational dispersion is calculated; IG1 remains incomplete for R1.
No independent review is recorded.

Historical IG1a checkpoint:
Branch-local continuation: [IG1a constraint preflight](../theory/INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md)
frozen with its permanent certificate at `1798644`, then executed with exit 0
(SymPy 1.14.0, exact arithmetic). Result:
`FINITE_CONSTRAINT_ALGEBRA_PASS_AUTHOR_SIDE`, reproduced from Gu–Wen scalar/vector
clock constraints with six qutrits per cell. Both Laurent and independently
entered real-space overlap formulations pass. This certifies only commuting
constraints, not a QCA tick, an IR sector or physical modes.
The [mechanism report](../reports/2026-10-08--inverse-gravity-constraint-mechanism.md)
excludes constraint-only phase kicks as nontrivial dynamics in S=V=1 and
records why Hamiltonian penalties/N-model linear dispersion cannot be
transferred automatically to a Floquet QCA. Its then-open local-gate question
is addressed by IG1b above, without supplying the still-missing IR control.
The [initial primary-source/obstruction audit](../reports/2026-10-08--inverse-gravity-ig0.md)
records `IG0 = ARCHITECTURE_UNDERSPECIFIED`, with local tensor collective
sectors prioritized for specification, not proved viable. That initial
no-rule status is superseded only by the IG1b control tick above. A justified
IR state/sector is still required before a two-polarization/dispersion calculation.
Shared matter/geometry cones, conserved source and nonlinear closure remain OPEN.

This authorization supersedes historical blanket restrictions on new substrate
work only within the new charter. W1–W12 stays CLOSED_BY_CONTRACT in W6/CJWW;
F2/F4 evidence remains PRELIMINARY; H1 remains OPEN and paused; no Einstein
dynamics, novelty, physical scale or independent-review claim is promoted.
No third-party review or publication is authorized by this opening.

## Authoritative W9–W11 repair update — 2026-09-30

This update supersedes the W9–W11 summaries and Sections 29–31 below where
they conflict. The user authorized applying both rounds of blind-review
repairs, after source check `7903713` and second review `d6e74e6`. Both review
branches were incorporated by fast-forward into
`research/gravitational-normalization-gate`.

| Front | Current status | Evidence and limit |
| --- | --- | --- |
| W9 | **`OPEN_AFTER_AUDIT`**; B2 `ON_SHELL_CONTINUUM_IDENTITY_PASS` | Conditional symmetric/conserved continuum stress identity on the free matter shell at O(λ); the CJWW bridge and reciprocal completion remain open |
| W10 | **`OPEN_AFTER_AUDIT`** | Former C5 PASS was premature; explicit continuum action/constraint coefficients now checked, but full W11 local source matching and controlled constraint identity remain absent |
| W11 | **`OPEN_AFTER_AUDIT`** | Four zero-quasienergy species plus four π nodes; K is a finite-range exactly conserved free charge with O(Λ³) branch-local energy error; nonzero-transfer Belinfante source and local continuity current remain open |
| W11 F3 | **Contract OPEN**; `ONE_PARTICLE_FULL_Z3_CONTINUOUS_LOGARITHM_EXCLUDED` | Scoped proof accepted by both second-round reviewers: one particle, every ℤ³ translation, original two-component cell; interacting many-body and supercell generators are outside the proof |
| W12 four-species metric universality | **`UNIVERSAL_SUBFAMILY_DEFICIENT` — REVIEWED** (DeepSeek ACCEPT; Opus ACCEPT_WITH_REPAIRS, presentation only) | `dim(U)=3`, metric rank `3/6` on constant δh, no common rotation; with the −I nodes it would be `NON_UNIVERSAL`. Cite as a contract outcome on constant controls: read as a gauge condition, the missing relations fail only on `q₃=0` and a cone ([review](../debates/2026-09-30--w12-blind-review/README.md)) |
| Gravity line (W1–W12, W6/CJWW control class) | **CLOSED_BY_CONTRACT (W12 §4), 2026-09-30** | Direct user decision («cierra la línea como dice el contrato»). Negative result for this control class; no joint Einstein–Weyl gate will be opened. Reopening requires a new control family with an independent physical justification written before any calculation; after-the-fact rescue is not allowed |
| Elastic/common-graph successor class | **KINEMATIC_COMMON_EMBEDDING_UNIVERSAL / ELASTIC_HOPPING_RESPONSE_OPEN — PRELIMINARY** | Contract frozen only after independent graph/elastic motivation was written; four +I species see exactly (h_*=a^2\Lambda\Lambda^T), metric rank 6/6. This is common-embedding kinematics only; it does not reopen W3–W11 or supply strain-dependent CJWW hopping dynamics | [2026-09-30 elastic-graph report](../reports/2026-09-30--elastic-graph-species-universality.md) |
| Unitary elastic hopping-response attempt | **UNITARY_ELASTIC_RESPONSE_INCONSISTENT** | Frozen bond generator depends on arbitrary orientation set `F_+` because exact CJWW blocks do not satisfy `W_-h=W_h^†`; four-species metric test was not executed | [2026-09-30 elastic-hopping report](../reports/2026-09-30--elastic-hopping-unitary-response.md) |
| Orientation-independent Hermitian elastic successor | **HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY — PRELIMINARY** | HH0–HH5 pass; all four +I species have the same rank-6 metric response, but the new hopping generator contributes zero to the principal spatial frame at first order after removal of the common scalar phase. Entire metric response is inherited from the common embedding | [2026-09-30 Hermitian elastic report](../reports/2026-09-30--elastic-hopping-hermitian-response.md) |
| Arrighi-Facchini paired-QW restricted CJWW bridge | **SINGLE_COORDINATE_FACTORIZATION_EXCLUDED — PRELIMINARY** | Author-side exact certificate excludes one CJWW tick on the original C² cell as three invertible differentiable factors, one per original coordinate, up to constant on-site conjugation. Does not exclude grouped, ancilla, blocked or repeated-axis paired-QW constructions | [2026-09-30 CJWW factorization audit](../reports/2026-09-30--cjww-coordinate-factorization-audit.md) |
| QCGD next-family preflight and specification gate | **NO_RULE_SPECIFIED** after `BRIDGE_QUANTIFIERS_OPEN / EXPLICIT_CJWW_RULE_NOT_SPECIFIED` | Primary-source preflight finds finite labelled graphs and a representation theorem for vertex-preserving causal unitaries. The new F7 specification gate audits QCGD, the strong bridge no-go and W1, and stops at Q0: no complete `U_F7(g)` with geometric observables is specified yet. Next admissible step is constructive rule specification, not a metric test | [family atlas preflight](../docs/family_atlas/NEXT_FAMILY_PREFLIGHT.md), [F7 rule-spec report](../reports/2026-09-30--f7-qcgd-rule-specification.md) |
| Gu-Wen constraint architecture family | **VACUUM_CONSTRAINT_ARCHITECTURE_PRIOR_ART / DIRECT_CJWW_SOURCE_BRIDGE_OPEN** | Primary-source F8 preflight: Gu-Wen supplies a prior-art tensor constraint/helicity +/-2 architecture; controlled L model has cubic dispersion, N/linear route is less controlled, and no local CJWW stress/source bridge is specified. W10 remains `OPEN_AFTER_AUDIT` | [F8 preflight](../reports/2026-09-30--f8-gu-wen-constraint-preflight.md), [F8 atlas card](../docs/family_atlas/families/F8_gu_wen_constraints.md) |
| Pretko rank-2 tensor gauge family | **RANK2_GAUSS_LAW_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT** | Primary-source F9 preflight: Pretko supplies rank-2 tensor Gauss-law/fracton architectures and prior art for tensor-gauge mode counting. The read sources do not provide a CJWW/QW rule, local CJWW source matching, reciprocal backreaction or exact QCA update | [F9 preflight](../reports/2026-09-30--f9-pretko-tensor-gauge-preflight.md), [F9 atlas card](../docs/family_atlas/families/F9_pretko_tensor_gauge.md) |
| Gauge-invariant CA family | **GAUGE_EXTENSION_CA_ARCHITECTURE_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT** | Primary-source F10 preflight: Arrighi--Costes--Eon supply gauge-extension CA architecture, relative link fields and a reversible non-relative matter/gauge feedback example. The source does not provide CJWW/QCA geometry, metric response or four-species test | [F10 preflight](../reports/2026-09-30--f10-gauge-invariant-ca-preflight.md), [F10 atlas card](../docs/family_atlas/families/F10_gauge_invariant_ca.md) |
| Arnault–Cedzich discrete-time lattice gauge family (documentary addition, 2026-10-01) | **DISCRETE_TIME_U1_ACTION_CURRENT_PRIOR_ART / DIRECT_CJWW_GEOMETRY_BRIDGE_ABSENT** | Bounded primary-source F11 reading: (1+1)D matter action, internal U(1) charge current and classical gauge sourcing; no quantized joint matter/gauge update, constructed (3+1)D matter action or direct CJWW metric bridge. No scientific gate is opened or promoted | [F11 preflight](../reports/2026-10-01--f11-arnault-cedzich-lattice-gauge-preflight.md), [F11 atlas card](../docs/family_atlas/families/F11_arnault_cedzich_lattice_gauge.md) |
| Bisio–D’Ariano–Perinotti light QCA family (documentary addition, 2026-10-01) | **PUBLISHED_3D_WEYL_QCA_MAXWELL_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F12 reading: explicit Weyl QCA on BCC `Z^3`, composite Maxwell bilinears and `k`-dependent dispersion; fixed frame, no variable metric, stress/source or four-species test. No scientific gate is opened or promoted | [F12 preflight](../reports/2026-10-01--f12-bisio-dariano-perinotti-light-preflight.md), [F12 atlas card](../docs/family_atlas/families/F12_bisio_dariano_perinotti_light.md) |
| Farrelly–Short discrete causal particle family (documentary addition, 2026-10-01) | **PUBLISHED_CAUSAL_SINGLE_PARTICLE_WALK_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F13 reading: finite-support translationally invariant particle, internal-2 Weyl limit, internal-3 rotational but non-Lorentzian example; no CJWW rule, metric response or four-species test. No scientific gate is opened or promoted | [F13 preflight](../reports/2026-10-01--f13-farrelly-short-discrete-spacetime-preflight.md), [F13 atlas card](../docs/family_atlas/families/F13_farrelly_short_discrete_spacetime.md) |
| D’Ariano–Erba–Perinotti isotropic QW family (documentary addition, 2026-10-01) | **PUBLISHED_ISOTROPIC_CAYLEY_QW_CLASSIFICATION / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F14 reading: complete `s=2`, `d=1,2,3` isotropic Cayley-QW classification; unique BCC graph and two Weyl walks in d=3; no variable metric, CJWW controls or four-species test. No scientific gate is opened or promoted | [F14 preflight](../reports/2026-10-01--f14-isotropic-qw-classification-preflight.md), [F14 atlas card](../docs/family_atlas/families/F14_isotropic_qw_classification.md) |
| D’Ariano–Perinotti information-principles QCA family (documentary addition, 2026-10-01) | **INFORMATION_AXIOM_DERIVED_WEYL_DIRAC_QCA_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F15 reading: informational QCA axioms, emergent Cayley-graph space, minimal BCC Weyl automata and local Weyl–Dirac coupling; no variable metric, CJWW controls or four-species test. No scientific gate is opened or promoted | [F15 preflight](../reports/2026-10-01--f15-information-principles-dirac-preflight.md), [F15 atlas card](../docs/family_atlas/families/F15_information_principles_dirac.md) |
| Białynicki-Birula cubic QCA family (documentary addition, 2026-10-01) | **PUBLISHED_CUBIC_QCA_WEYL_DIRAC_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F16 reading: explicit local reversible Weyl/Dirac QCA on cubic/BCC lattice; no variable metric or CJWW species test. No scientific gate is opened or promoted | [F16 preflight](../reports/2026-10-01--f16-bialynicki-birula-qca-preflight.md), [F16 atlas card](../docs/family_atlas/families/F16_bialynicki_birula_qca.md) |
| Bisio–D’Ariano–Perinotti nonlinear Weyl symmetry family (documentary addition, 2026-10-01) | **NONLINEAR_POINCARE_SYMMETRY_PRIOR_ART / DIRECT_CJWW_METRIC_BRIDGE_ABSENT** | Bounded primary-source F17 reading: BCC Weyl walk and nonlinear Poincare/dilation realization in momentum space; no dynamic metric or CJWW species test. No scientific gate is opened or promoted | [F17 preflight](../reports/2026-10-01--f17-weyl-walk-lorentz-preflight.md), [F17 atlas card](../docs/family_atlas/families/F17_weyl_walk_lorentz.md) |
| Fracton emergent-gravity family (documentary addition, 2026-10-01) | **FRACTON_TENSOR_GRAVITY_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT** | Bounded primary-source F18 reading: rank-2 tensor gauge model with restricted mobility and emergent graviton; no CJWW rule or QCA update. No scientific gate is opened or promoted | [F18 preflight](../reports/2026-10-01--f18-fracton-emergent-gravity-preflight.md), [F18 atlas card](../docs/family_atlas/families/F18_fracton_emergent_gravity.md) |
| Barceló et al. emergent-gauge mechanism family (documentary addition, 2026-10-01) | **EFFECTIVE_GAUGE_EMERGENCE_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT** | Bounded primary-source F19 reading: effective emergence of gauge symmetries and linear diffeomorphisms; no microscopic CJWW rule. No scientific gate is opened or promoted | [F19 preflight](../reports/2026-10-01--f19-emergent-gauge-gravity-mechanism-preflight.md), [F19 atlas card](../docs/family_atlas/families/F19_emergent_gauge_gravity_mechanism.md) |
| Xu–Hořava algebraic Bose liquid family (documentary addition, 2026-10-01) | **LATTICE_BOSE_LIQUID_LIFSHITZ_GRAVITY_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT** | Bounded primary-source F20 reading: FCC boson model with emergent Lifshitz gravity phases and IR gauge constraint; rigid lattice, no CJWW rule. No scientific gate is opened or promoted | [F20 preflight](../reports/2026-10-01--f20-lifshitz-bose-liquid-preflight.md), [F20 atlas card](../docs/family_atlas/families/F20_lifshitz_bose_liquid.md) |

**Atlas relacional — 2026-10-01.** F1–F20 tienen ahora un mapa tipado en
[`docs/family_atlas/RELATIONS.md`](../docs/family_atlas/RELATIONS.md) y una
tabla estructurada en [`relations.csv`](../docs/family_atlas/relations.csv).
Esta capa es documental: no cambia resultados, no transfiere gates y no abre
ningún puente CJWW que las fichas no hayan demostrado.

La guía operativa para usar el atlas en los frentes del proyecto está en
[`PROJECT_NAVIGATION.md`](../docs/family_atlas/PROJECT_NAVIGATION.md). Es una
guía de selección y claim ceiling; no autoriza cálculos ni modifica el cierre
contractual de W12.

La edición pedagógica del atlas está en
[`student_edition/README.md`](../docs/family_atlas/student_edition/README.md);
es una capa explicativa y no modifica la evidencia canónica.

**Review provenance:** the first review covered `41d0e0d`. The
[second review](../debates/2026-09-30--w9-w11-repair-review/README.md) at
`d6e74e6` covers `86fe771`: DeepSeek gives W9 ACCEPT_WITH_REPAIRS and W10/W11
ACCEPT; Opus gives ACCEPT_WITH_REPAIRS for all three. Both accept the
node/K/bound calculations and the scoped F3 proof. Their remaining scope
and presentation repairs are now applied; the revised W9 checker is a local
author-side validation, not a third independent review. No full gate or
novelty claim is promoted. A1/A2/A4 are applied. A3 uses the
explicit downgrade permitted by the repair list. B1 fixes one continuum
normalization; B2/B3 restrict the Einstein calculation to a flat test source
at O(λ), not the Gu–Wen L lattice model. B4–B6 and C1–C3 are addressed in
the dated addenda. D1 now checks the actual gauge-coupling algebra; D2
constructs real-space charge operators but leaves q≠0 local stress open.
The second-round clarifications also distinguish the Hamiltonian shift
multiplier from quadratic shift dependence in the Lagrangian, require the
four-species total T_(0) in W10, and record K's opposite leading energy sign
at the −I nodes. The old verdict blocks now carry superseded banners.

W12 is separately authorized by the frozen contract at `2ff88b2` and has now
been executed. The [report](../reports/2026-09-30--w12-four-species-metric-universality.md)
records `UNIVERSAL_SUBFAMILY_DEFICIENT` at first order for the declared W6
controls. This remains PRELIMINARY pending the blind review required by W12;
the contract was not modified. This is a negative result within that control
class, not a general no-gravity result.

Records: [W9 addendum](../reports/2026-09-30--w9-cjww-graviton-matter-bridge.md#9-repair-addendum--2026-09-30),
[W10 addendum](../reports/2026-09-30--w10-sourced-gu-wen-constraints.md#9-repair-addendum--2026-09-30-supersedes-the-terminal-decision),
[W11 addendum](../reports/2026-09-30--w11-cjww-floquet-stress-tensor.md#9-repair-addendum--2026-09-30-supersedes-the-verdict-above).
The [primary-source audit](../investigaciones/2026-09-30-prior-art-walk-graviton/comprobacion.md)
remains the bounded prior-art record: novelty OPEN, pending sources still
pending, catalog tags still proposed. No earlier scientific gate is reopened.

**Contractually permitted successor, 2026-09-30.** After the W12 closure, the
user explicitly froze a physically distinct common-graph/elastic family only
after its independent motivation had been written: geometry is one deformation
of the spatial support shared by all matter, rather than W6 Pauli-selective
controls on a fixed graph. The frozen contract is
[`ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md`](../theory/ELASTIC_GRAPH_SPECIES_UNIVERSALITY_GATE.md)
at `25d8138`.

For the minimal homogeneous affine embedding
`X_Lambda(n)=a Lambda n`, with the abstract CJWW hopping blocks unchanged,
the exact principal frame at every decisive +I species is
`E_*^(Lambda)=a E_* Lambda^T`. Since the reviewed flat nodes all satisfy
`E_*^T E_*=I`, every species sees exactly
`h_*^(Lambda)=a^2 Lambda Lambda^T`. The first-order metric map is
`delta h/a^2=L+L^T`, with symmetric-strain rank 6/6 and a three-dimensional
antisymmetric rotation kernel.

Terminal state:
```
KINEMATIC_COMMON_EMBEDDING_UNIVERSAL /
ELASTIC_HOPPING_RESPONSE_OPEN
```

This survives the first four-species kill test but is deliberately not a full
reopening of the gravity programme. The pass is kinematic because the abstract
CJWW unitary and its transition blocks are unchanged. A further successor
would need a separately frozen, physically motivated **unitary
strain-dependent hopping rule or dynamical-graph rule** and must repeat the
four-species metric test before any backreaction/spin-2/constraint work. W12
remains unchanged for the W6/CJWW control class. Evidence is
`AUTHOR_DERIVATION / EXACT_SYMBOLIC_CERTIFICATE /
INDEPENDENT_REVIEW_PENDING`.

**First unitary hopping-response successor, 2026-09-30.** The separately
frozen [`ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md`](../theory/ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md)
at `15bc76b` fails before any four-species calculation. Its bond generator
used one representative from each opposite pair and assumed that adding the
adjoint removed the orientation convention. Exact CJWW blocks do not satisfy
`W_-h=W_h^dagger`; for the isotropic control at `p=0`, the choices
`h1=+1` and `h1=-1` give different generators,
`[[1,1],[1,1]]` and `[[1,-1],[-1,1]]`.

Terminal state:
```
UNITARY_ELASTIC_RESPONSE_INCONSISTENT
FOUR_SPECIES_KILL_TEST = NOT_EXECUTED
```

The failure is at model definition, not at species universality. The
common-embedding predecessor remains valid, and W12 remains unchanged.
An orientation-independent Hermitian-part construction from the full
bond-weighted symbol is noted only as a possible separately chartered
successor; it was not substituted or executed after the failure.

## Reading guide and synchronization — 2026-09-28

> Historical snapshot. Several rows below (W3–W6, W4 spectrum, discrimination
> cost, local-versus-remote evidence) were overtaken by later dated entries.
> Use the current reading guide of 2026-10-28 at the top of this file.

This branch was created from the documentation-only checkpoint of 2026-09-28.
That checkpoint's inventory remains unchanged below. On 2026-09-29 the user
directly authorized a separately chartered successor,
`GRAVITATIONAL_NORMALIZATION_GATE`; its G0 stop result is recorded in the
2026-09-29 addendum at the end of this file. No earlier scientific gate is
reopened or promoted by that successor.

| Front | Recorded status and scope | Where to resume |
| --- | --- | --- |
| Central question: c and the substrate | Strong matching rejected in the declared s=4 class; standard Pavia equality retained; additional matching hypotheses and species universality OPEN | Sections 4–7 |
| Flat CJWW corona | CLOSED in the frozen model/protocol; this is not evidence of a natural substrate | Section 8.20; [authoritative manuscript](../papers/ir-corona/ir-corona.tex) |
| Spectral attribution | C2c PASS for the sixteen frozen pairs; C3 PASS for four encoders with M_B=I, limited to the conditioning correction | Section 10.1 |
| Physical realization / absolute scale (4B) | Existing September 25 execution records NO_ABSOLUTE_SCALE_DERIVABLE with PRELIMINARY / PARTIAL_EXTERNAL_REVIEW evidence and a scoped September 26 review | Section 8.21; [existing execution](../reports/2026-09-25--physical-realization-absolute-scale-gate.md) |
| Gravitational normalization successor | **BLOCKED_NO_DYNAMICAL_GEOMETRY** at G0 on the frozen CJWW/H1 model; G1-G3 not executed | [2026-09-29 G0 report](../reports/2026-09-29--gravitational-normalization-g0.md) |
| Dynamical-geometry model class | **VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED**; QCGD-type bounded-degree class selected | [2026-09-29 class-selection report](../reports/2026-09-29--dynamical-geometry-model-class.md) |
| Exact CJWW dynamic-graph bridge | **STRONG_EXACT_BRIDGE_IMPOSSIBLE** for one fixed pure geometry background and exact reduced CJWW dynamics for every matter state; backreaction then cannot carry matter information | [2026-09-29 no-go proof](../reports/2026-09-29--explicit-cjww-dynamic-graph-bridge.md) |
| W1 perturbative link bridge | **W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN**; exact CJWW at g=0, matter-dependent link response O(g), regular-background matter correction begins at O(g^2) | [2026-09-29 W1 report](../reports/2026-09-29--w1-perturbative-backreaction-bridge.md) |
| W1 geometricity | **W1_OPERATIONAL_GEOMETRY_PASS**, scope **FINITE_TIME_EXACT_SUPPORT_ONLY**; two link states give different exact 2-step matter support, while one-step adjacency and outer causal body remain unchanged | [2026-09-29 geometricity report](../reports/2026-09-29--w1-geometricity.md) |
| W1 coarse metric | **W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION**; link backgrounds add scalar potential/dephasing but do not alter the Weyl principal symbol, one-step neighborhood or outer causal body | [2026-09-29 coarse-metric report](../reports/2026-09-29--w1-coarse-metric.md) |
| W2 transport/tetrad bridge | **PRINCIPAL_SYMBOL_CONTROL PASS, but W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL** after exact audit; different link backgrounds change (E_a{}^i), but the controlling observable <Z+X> is conserved by the declared coupling | [2026-09-30 audit](../reports/2026-09-30--w2-tetrad-backreaction-audit.md) |
| W3 backreacting tetrad | **W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN — PRELIMINARY, independent review pending**; noncommuting Y-kick changes <Z_e>, and the same <Z_e> controls the momentum-linear Weyl tetrad in the transport substep | [2026-09-30 W3 report](../reports/2026-09-30--w3-backreacting-tetrad.md) |
| W3 coarse curvature/dynamics | **COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL**; W3 induces an explicit coarse metric and can have nonzero kinematic curvature, but has no geometry-only stiffness/propagation term and no derived stress-energy source | [2026-09-30 curvature report](../reports/2026-09-30--w3-curvature-dynamics.md) |
| W4 geometry stiffness | **W4_AUTONOMOUS_GEOMETRY_DYNAMICS_PASS / GRAVITATIONAL_SOURCE_OPEN — PRELIMINARY, independent review pending**; partial-SWAP geometry-only brickwork preserves the homogeneous background and transports the tetrad-control variable and coarse curvature information in vacuum | [2026-09-30 W4 report](../reports/2026-09-30--w4-geometry-stiffness.md) |
| W4 long-wavelength spectrum | **OPEN_AFTER_AUDIT / AUTHOR_CHECKED; independent review prepared, not sent**. Full same-sign step has a quadratic zero branch for fixed 0<kappa<pi/2; opposite-sign control is linear in 1D. Velocity slope uses two-register cells; no linear Z/metric wave follows from the amplitude spectrum. | [2026-10-26 full-spectrum audit](../reports/2026-10-26--w4-spectrum-audit.md) |
| W5 tetrad-conjugate source | **W5_TETRAD_CONJUGATE_SOURCE_PASS / STRESS_ENERGY_CONSERVATION_OPEN — PRELIMINARY, independent review pending**; the source is the same current operator variationally conjugate to the spatial tetrad, but a conserved full stress-energy tensor/Ward identity is not derived | [2026-09-30 W5 report](../reports/2026-09-30--w5-tetrad-conjugate-source.md) |
| W5 tetrad completeness audit | **RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN** for the original three-field model; exact rank 3 of 9 in tetrad space and 3 of 6 in metric space | [2026-09-30 rank audit](../reports/2026-09-30--w5-spatial-tetrad-completeness.md) |
| W6 full spatial tetrad | **W6_FULL_SPATIAL_TETRAD_PASS / SPACETIME_GAUGE_STRUCTURE_OPEN — PRELIMINARY, independent review pending**; nine controls span all 9 spatial tetrad and all 6 metric perturbations, with a 3D metric kernel equal to infinitesimal frame rotations | [2026-09-30 W6 report](../reports/2026-09-30--w6-full-spatial-tetrad.md) |
| W7 spin-2 kinematics | **SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN — PRELIMINARY, independent review pending**; spatial tetrad perturbations decompose as frame rotations (3) + trace scalar (1) + symmetric-traceless spin-2 tensor (5), but no 5→2 TT reduction is derived | [2026-09-30 W7 report](../reports/2026-09-30--w7-spin2-kinematics.md) |
| W8 TT gauge completion | **TT_GAUGE_REDUCTION_KINEMATIC_PASS / MICROSCOPIC_GAUGE_EMBEDDING_OPEN — PRELIMINARY, independent review pending**; a traceless vector gauge orbit has rank 3 at nonzero momentum and reduces the 5-component spin-2 tensor to plus/cross, but W6 does not realize this redundancy microscopically | [2026-09-30 W8 report](../reports/2026-09-30--w8-tt-gauge-completion.md) |
| W8 prior-art correction | Gu-Wen already provide emergent helicity ±2 and low-energy linearized diffeomorphism gauge structure from qubit/spin models; Pretko rank-2 theories already include the relevant 5→2 tensor-gauge structure. Novelty target pivots to the CJWW matter-gravity bridge | [2026-09-30 prior-art audit](../reports/2026-09-30--w8-prior-art-gauge-audit.md) |
| W9 CJWW-graviton matter bridge | **OPEN_AFTER_AUDIT**; only the conditional on-shell continuum identity passes; see the authoritative repair update above | [2026-09-30 W9 report, §9](../reports/2026-09-30--w9-cjww-graviton-matter-bridge.md) |
| W10 sourced Gu-Wen constraints | **OPEN_AFTER_AUDIT**; continuum test-source result only; full local four-species source and backreaction open | [2026-09-30 W10 report, §9](../reports/2026-09-30--w10-sourced-gu-wen-constraints.md) |
| W11 CJWW Floquet stress | **OPEN_AFTER_AUDIT**; integrated free charges and scoped one-particle F3 obstruction accepted; local Belinfante stress and contract F3 open | [2026-09-30 W11 report, §9](../reports/2026-09-30--w11-cjww-floquet-stress-tensor.md) |
| Engineered implementation (4A) | User authorization recorded, separate contract still missing | Section 8.21 addendum; no implementation opened here |
| H1 / inhomogeneous extension | OPEN and paused; L2 B / OPEN_BLOCKED_METHOD is a method limitation, not a refutation | Section 9.7, later repair and L2 addenda |
| E0 / power stability / E–AdS | OPEN_AT_STOP / OPEN_AT_STOP / STOPPED_UNPROVEN | Existing Section 9 records; no reopening |
| Independent-use discrimination cost | REVIEWED_PASS_WITH_REPAIRS (Astra; Gemini PASS, 2026-10-22); repaired version REVIEWED_PASS (Grok, 2026-10-28); inherited corona premises not reviewed: fixed-detector Theta(delta_N^-2); uniform one-particle lower bound Omega(N^-4 exp(K_* N)) for independent uses in the same regions | [September 28 supplied report](../reports/2026-09-28--iid-message-discrimination-cost.md) |

**Local versus remote evidence.** At this checkpoint, the remote
`claude/endpoint-transfer-partial` points to `a19c6478`, 25 commits behind
the main baseline. The report's declared local baseline `13d398a` and the
user-reported `16c4f0f` could not be retrieved from GitHub. Their absence
from this remote does not invalidate local work, but they are not verified
remote evidence. The distinct local September 28 4B report has not been
imported because its full text is unavailable in this session.

**4B chronology correction.** The September 25 report and Section 8.21 already
record execution authorization and the negative result. The recent account
that only contract freezing had been authorized must not overwrite that
existing record on the basis of the different, unavailable September 28
report. Reconcile the local history against these records when it is synced;
no new 4B closure or evidence-level promotion is performed here.

**Next step before new research.** Superseded: both items are done. The local
commits were reconciled on 2026-10-22 (`94071db`), and the discrimination-cost
report was reviewed on 2026-10-22, with its repairs re-reviewed on 2026-10-28;
its inherited sixteen-pair asymptotic was outside those reviews. See the current
reading guide at the top of this file. A universal operational boundary at c, viable
communication inside it, other geometries, correlated uses, and stability
under perturbations remain unproved and are not opened by this checkpoint.

**Date:** 2026-09-24
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS; point-(3) ceiling PROVED UNDER FROZEN CONTRACT, one independent review PASS; flat CJWW (5.15) operational IR-corona result CLOSED in its frozen class; **H1-only extension: TWO_DISTINGUISHABLE_CHANNELS frozen by explicit model assumption** (Sec. 9.6): H1c-0a CLOSED, H1c-0b FIXED_BY_EXPLICIT_ASSUMPTION, primary observable `(L_+, L_-)`; physical realization/justification OPEN; Volterra/asymptotic localization PAUSED. H1-SR proved under frozen beta contract, H1a/H1b proof written/unreviewed, layer absolute-mass bound PASS, G-insertion and final-Q-leakage PASS_IN_LOCAL_WINDOW retain their prior scope; H1c localization and H1 remain unproved/OPEN. Exploratory sequence: T1 `PASS` with independent adversarial review for the frozen model and admissible fixed W; T2 `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`; T3 `STOPPED_NO_SIGNED_TERM`. Physical reconstruction norm audit: `PRELIMINARY: BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM`, the operator norm bound is direct; the L^2 stability `||t_j||_2 = O_{W,Theta}(1)` (Sec. 9.7) was repaired and has `SCHUR_STABILITY_PASS` with independent review (DeepSeek, GPT/Grok), scope `||t_j||_2` only; the vector/piece bounds that use it remain PRELIMINARY (not expressly reviewed). Physical transfer of the flat endpoints (Sec. 9.7 addendum): `ENDPOINT_TRANSFER_PARTIAL — PRELIMINARY` (Alice `O(N^-3)` transfers; no `O(N^-3)` for Bob at `vartheta != 0`; gaps L1/L2/L3; `PASS_WITH_REPAIRS`, repaired version not re-reviewed). No `E_6` or dominance claim. L2 stop gate: `B / OPEN_BLOCKED_METHOD` (PRELIMINARY decision audit; partial external review + source bounds reproduced by Claude; B structural to norm-based method, not evidence against H1; H1 OPEN and paused). The present physical stay-remainder bounds do not reach `o(N^-13/2 e^{-K_*N})` without the still-open H1c localization machinery; this is a method obstruction, not an H1 refutation. See Sec. 9.7. No H1/H1c promotion. E0 and POWER_13/2_STABILITY remain OPEN_AT_STOP; E/AdS remains STOPPED_UNPROVEN. IR spectral-attribution front (Sec. 10.1): C1 PASS, C2a PASS for sigma2/I (one independent agent review), C2b PASS for sigma2/I (B4_PRIME_PASS separately; one independent agent review), C2c structural scope C2C_PASS for the frozen 16-pair scope, C3 conditioning C3_PASS for the frozen four-encoder `M_B=I` scope.

**Historical branch provenance.** The earlier reconciliation originated on
`research/b-infinity-post-s4-gate`. These records are now present in the remote
main baseline named above; the former statement that main was unchanged is
obsolete. Repository integration does not by itself promote an evidence level.
This checkpoint records inventory and provenance only.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**Only point (3), the strict-cone ceiling, is chartered and authorized by
direct user instruction** (Sec. 7.2). The full C gate is not ratified.

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

Sub-question A.int (imported 2026-10-26, AI-formulated, unreviewed): with
equal free IR speeds, does interaction in a Δt = Δx QCA shift `c^(i)` per
species at O(g²) (Collins mechanism), and does any QCA symmetry forbid it?
Status **OPEN / PRIMARY_SOURCE_PREFLIGHT_COMPLETE** (2026-10-27).
The [primary-source preflight](../reports/2026-10-27--interaction-speed-primary-preflight.md)
distinguishes EFT operator admissibility from a computed QCA loop shift.
The checked covariance papers do not establish interacting 3+1 protection;
this does not prove its absence. Number-preserving Thirring has exactly free
one-particle evolution over the empty vacuum, so that sector is not a witness
of the proposed radiative effect. QCA-specific loop matching and Q3 remain
open; no calculation contract was opened.
User-authorized step 1 (2026-10-27), the
[Eon v4 feasibility audit](../reports/2026-10-27--eon-v4-interaction-speed-feasibility.md),
is complete: `REFERENCE_AND_OBSERVABLE_OPEN / NOT_READY_FOR_ONE_LOOP`.
The physical half-filled Gauss sector is identified, but a stationary vacuum,
charged dressing/boundaries, a controlled weak-coupling expansion and the
free fermion/photon speed calibration remain unestablished. This is not a
rejection of Eon's model.
The user then authorized specification and checking of one reference.
The [fixed specification](../theory/A_INT_EON_REFERENCE_CHECK.md) and
[exact reference check](../reports/2026-10-27--eon-reference-state-check.md)
give `GAUSS_PASS / OCCUPATION_REFERENCE_STATIONARITY_FAIL / STOP_THIS_CANDIDATE`.
For the declared product with modes 2,3 filled and integer E=0, the full-step
occupation witness changes by `2 sin²(m epsilon)` per site. A separate
massless full-step magnetic bound rejects it in a declared small-angle
interval. L=3,4 finite controls and two exact local mass constructions pass;
the analytic proof states the L>=3 scope. Evidence is author-checked, with
independent review pending. No alternative vacuum, loop calculation or
evidence promotion; the model itself is not rejected and A.int stays open.
After a user-supplied reply, an
[author-side audit](../reports/2026-10-27--eon-received-answer-audit.md)
finds its failure explanation compatible but its vacuum shortcuts insufficient.
Fixed E=0 requires sharp local number, not only mean two: a negative-band
Slater control on a four-site free directional slice is stationary freely
but has local number variance one and fails the proposed Gauss sector.
A two-mode counterexample also shows that principal-log minimization can
select a different state from the known additive-energy vacuum. These are
bounded algebra controls, not a construction or simulation of the interacting
3D gauge vacuum. No replacement candidate, independent-review promotion or
loop execution is recorded.
The subsequent user instruction "hazlo" authorizes a new explicit
matter/gauge reference attempt. The
[fixed projected-Gaussian specification](../theory/A_INT_EON_PROJECTED_GAUSSIAN_REFERENCE.md)
and [construction/check](../reports/2026-10-27--eon-projected-gaussian-reference.md)
give `EXPLICIT_NORMALIZABLE_GAUSS_STATE_CONSTRUCTED /
GAUSSIAN_TAIL_STATIONARITY_FAIL`. A Gauss-projected auxiliary Dirac Slater
with electric heat-kernel weights has exact Gauss, finite norm and finite
electric expectation. Its preparation criterion is an explicit auxiliary
choice, not a conserved energy derived from U. An author-written Fourier/
Jensen argument excludes stationary pure states with these Gaussian electric
tails for the declared finite-volume, untruncated, exact-exponential magnetic
step with nonzero angle. Ingredient checks are executable; the analytic
argument still needs independent review. This does not exclude other tails
or all Eon vacua. The requested physical vacuum has NOT been obtained;
no correlator, speed, loop or evidence-promotion gate is opened.
Independent review, 2026-10-28 (user: "mandale a DeepSeek"): the Gemini attempt
of 2026-10-27 never completed (DNS), so the same sealed brief went to DeepSeek
(deepseek-v4-pro, one round) on the bytes committed in `5dbd843`. Verdict:
`ACCEPT_WITH_REPAIRS`, with construction ACCEPT, scope ACCEPT and obstruction proof
ACCEPT_WITH_REPAIRS; no fatal error
([review and author reading](../debates/2026-10-28--eon-gaussian-review-deepseek/verificacion_autor.md)).
The author rejects G-R1-01/06 as errors, since the reviewer swapped the series f
(of phi) and g (of psi). G-R1-04 is accepted with content: Eon's V operators carry
JW/rishon strings (PDF p.7). They are diagonally equivalent to pure shifts because
they commute, but plaquette monomials may then carry ±1 signs, so the report's
`a=4` is not guaranteed. `a≢0` still follows from four distinct monomials at L>=3.
The repairs were applied as a dated addendum to the report on 2026-10-28 and
have not been re-reviewed. Repair 4 rests on an author argument that DeepSeek
has not seen. Status: `REVIEWED_ACCEPT_WITH_REPAIRS; repaired version not re-reviewed`.
No vacuum, correlator, speed or loop is opened.
See the
[imported question](../reports/2026-10-26--interaction-renormalized-species-speed.md).
No gate opened or promoted.

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

**Superseded as the active line by Sec. 8 (2026-09-16).** This section records
the `B_infty^*` reading of the project and remains valid where proved, but its
scalar summaries must be read under the scope correction in Sec. 8.6.

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

**Update (2026-09-17, branch-local, frozen class of Sec. 8 only).**
`B_infty^*` matching in Sec. 4 is unchanged. What is now closed is the
**operational IR question** on the preregistered CJWW (5.15) protocol of
Secs. 8.16–8.20, not the matching hypothesis. In that class there is an
IR-controlled operational response outside the emergent cone, and it is
not a mere UV-propagator artefact:

`c_IR < v_micro` (already geometric for (5.15)) and
`IR probe → δ_B(N) ≠ 0` for large `N`, with
`δ_{M,M_B}(N) ∼ |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N}`
on the twelve Pauli pairs (Sec. 8.20). The signal is
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. This is theoretical step 3
of the physical line, closed inside the preregistered class. It is not
`D_B > 0` for every QCA, not a claim about nature, and not a further
signalling calculation. Sec. 8.21 has now been executed with terminal state `NO_ABSOLUTE_SCALE_DERIVABLE` (preliminary; partial external review + Claude review 2026-09-26, see Sec. 8.21).

## 7. GATE STATUS — only point (3) authorized by the user

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; point (3) ceiling
investigation separately chartered by direct user instruction.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Point (3) — direct user authorization, not a ratification

**Authorization (2026-09-16):** after the incomplete ratification, the user
explicitly instructed: "pues adelante, punto (3)". Accordingly,
`STRICT_CONE_CEILING_N3 = AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` under the
[frozen point-(3) contract](../theory/STRICT_CONE_CEILING_N3_GATE.md).
Its sole target is `c_0 <= c_strict^iso` in all directions, including
degenerate Floquet nodes and eigenvalue collisions in U^n. The contract
was frozen at `4135625` with initial scientific status **OPEN**. No L1,
defect-metric or other C step is authorized by this instruction.

**Point-(3) result (2026-09-16):**
`PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`;
`THEOREM_STATUS = PROVED_UNDER_FROZEN_CONTRACT`. The
[analytic report](../reports/2026-09-16--point-3-strict-cone-ceiling.md)
supplies a matrix-polynomial boundary bound, compression to the original
eigenspace, a direct directional-slope argument, and the exact support
limit. The author's assessment is `PASS_ANALYTIC` under the frozen
contract. The [independent adversarial review](../informe_adversarial_punto_3.md)
at `bd44122`, reviewing `db083af` against `4135625`, records
`ACCEPT_AS_WRITTEN`, with no mandatory repairs. One independent review is
complete; it is not a five-member ratification. The follow-up incorporates
its recommended sign control and expository clarifications without changing
the frozen quantifiers. The bound is proved for the admitted cones and the
exact support of the full symbol on N3, including degenerate Floquet nodes
and collisions of eigenvalues after taking powers. It does not establish a
sector-intrinsic or ballistic bound, or an extension to incommensurable
displacement sets. No numerical search or scientific script was run.
The full C gate is neither ratified nor closed;
L1 remains a manual candidate and the defect identity remains family-only.
The s=4 example refutes equality and is consistent with this ceiling.
**NOVELTY = OPEN.**

The 2026-09-16 ratification attempt is `ABORTED_OR_INCOMPLETE`: Gemini was
absent at launch; the process was interrupted without a final verdict. Three
first-round turns completed — ASTRA `PREFER_A`, CLAUDE OPUS `RATIFY_C`
conditioned on its own amendment (i), CIRO `RATIFY_C` — and ABNER's turn was
sent but never returned. That is neither a closed round nor five-member
ratification, so the status above is unchanged. The partial acta is archived
at [`2026-09-16--ratificacion-gate-completitud-axial-n3.md`](../debates/2026-09-16--ratificacion-gate-completitud-axial-n3.md);
the raw session log stays local and unversioned.

**Candidate from a degraded debate (2026-09-15):**
`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE`, **not
authorized.** In the
[deliberation](../debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.md),
four members proposed `AUTHORIZE_C`. The tool classified the run as
`DEGRADED_NO_CONSENSUS`: ASTRA failed two turns (Codex usage limit) and was
excluded. ASTRA's recorded preference was A, and its objection that C reaches
`c_strict^iso` only through the still unproven bound `c_0 <= c_strict^iso`
was left unanswered. The earlier requirement of five-member ratification
has not been met. The later direct user instruction above authorizes only
point (3) under a separate contract; it does not authorize the full C gate
or convert either incomplete debate into consensus.

Research directions (only the point-(3) ceiling is now frozen):

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is proved under the frozen point-(3) assumptions,
   with one independent adversarial review PASS. Thus every admitted cone
   satisfies `0 < c_0 <= c_strict^iso <= 1/sqrt(3)`. Equality and microscopic
   saturation are not consequences of this ceiling.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` is not
this counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

**Erratum (2026-09-15).** Earlier wording here attributed such a shortfall to
a nilpotent one-step coefficient. What is established is only this: a
saturation failure `c_strict^iso < r_in(C_micro)` requires at least one
nilpotent vertex coefficient (contrapositive of the vertex lemma). The
converse is not established. A nilpotent vertex removes the exact ray `n.h`
from `S_n`, but it does not by itself determine `c_strict^iso`, which must be
computed. See the charter's erratum.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**;
- **NO reading of `c_strict^iso`, `r_in(C_micro)` or `S_min` as "the microscopic
  speed of the substrate"** (Sec. 8.6);
- **NO new novelty audit, Bernstein-rigidity, paraunitary-classification or
  d=3-theorem line** under the Sec. 8.7 scope decision;
- **NO directional/anisotropic `I(v)` computation** (Sec. 8.8, NOT_AUTHORIZED);
- **NO operational-invisibility or no-signalling claim** from a rate function
  (Sec. 8.8); that question requires its own charter.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main`. The only later successor authorization is the point-(3) contract
in Sec. 7.2, by direct user instruction.

## 8. Directional causal saturation — canonical physical interpretation (2026-09-16)

**Evidence commit:** `2494192`.
[Report](../reports/2026-09-16--directional-causal-saturation.md),
[verifier](../scripts/verify_directional_saturation.py) (15/15, fail-closed,
fourteen exact).

The active physical question is: **does `c_IR` coincide with the microscopic
causal boundary of the discrete substrate?** The canonical answer is
**direction-dependent; in general, no.**

### 8.1 Three objects, never identified

For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
Eqs. (5.12) and (5.15):

`B(c_IR) ⊆ Γ ⊆ C_micro`,

- `B(c_IR)`: the emergent isotropic IR light cone;
- `Γ`: the ballistic / group-velocity propagation body;
- `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.

`Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
`conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
be assumed.

### 8.2 The canonical saturation function

For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`

`v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,

and, in the normalization `c_IR = 1`, the canonical directional saturation
function is the **support-function ratio**

`S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.

`S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.

`S_min` is a **descriptive scalar summary only**. The full directional function
`S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.

### 8.3 Walk (5.12)

`B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
`p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
faster than the emergent IR light speed while remaining inside `C_micro`.
`Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.

### 8.4 Walk (5.15) — the clean counterexample

`Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.

This refutes the identification

`sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.

Even when **all ballistic propagation respects `c_IR`**, the substrate permits
causal propagation outside the relativistic ball in non-axial directions.

**Evidence tags, not to be merged.** `sup|∇ω| = c_IR = 1` and
`Γ_2 ⊆ B(1)` are **ESTABLISHED (exact SOS certificate**
`(1-f²) - |∇f|² = s₂²s₃² + s₁²s₂²c₃² + s₁²c₂²s₃²`**)**, and `∂B(1) ⊆ Γ_2` is
exact from the conical point. That `Γ_2` also fills the open ball is
**SUPPORTED (numerical)** only. The counterexample does **not** depend on that
last half: it needs only `sup|v_g| = c_IR`, which is exact.

### 8.5 The gap is not a one-step artefact

At the eight vertex rays a single lattice path contributes, so
`(W^n)_{nσ} = (W_σ)^n`. Each `W_σ` has rank 1 with nonzero trace, hence
`(W_σ)^n = tr(W_σ)^{n-1} W_σ ≠ 0` **for every `n ≥ 1`** (exact). Therefore
`h_infty = h_{C_micro} = ||·||_1` exactly, and the distinction between `Γ` and
`C_micro` is not an artefact of a one-step support bound.

Between `Γ` and `C_micro`, propagation is non-ballistic and may be exponentially
suppressed; it is **not generically causally forbidden**. **No claim is made
that every point of this intermediate region has nonzero amplitude** — what is
proved is the statement about the vertex rays.

### 8.6 Scope correction to earlier scalar summaries

`c_strict^iso` and `r_in(C_micro)` remain mathematically valid summaries where
previously proved (Secs. 4, 6, 7), but **must not be interpreted as "the
microscopic speed of the substrate."** The microscopic causal boundary is
anisotropic and is represented by `C_micro`, equivalently by `h_{C_micro}(n̂)`.

Under (i) finite `F`, (ii) `d ≥ 2` and (iii) an isotropic IR cone, exact
equality `B(c_IR) = C_micro` is impossible, because `C_micro` is a finite
polytope and the IR body a Euclidean ball. This restates `B_full` (Sec. 3.3)
with its hypotheses made explicit; relaxing (i), (ii) or (iii) leaves it open.

### 8.7 Scope decision

The physical relation **emergent relativistic cone vs microscopic causal
body** remains the line. As of 2026-09-17, inside the frozen IR class of
Secs. 8.16–8.20, theoretical step 3 of that line is **closed**: the gap
is not only geometric (`c_IR < v_micro`) but operational
(`IR probe → δ_B(N) ≠ 0` for large `N`, nonperturbatively suppressed;
Sec. 8.20). No further signalling gate is authorized.

The live front is whether that structure can correspond to something in
nature (Sec. 8.21, `NOT_EXECUTED`), not another calculation of `C` and
not yet a laboratory implementation of the walk (fork 4A, identified,
not chartered).

**Not authorized by this result:** further search for mathematical novelty,
Bernstein rigidity, paraunitary classification, or a new dimension-3 theorem.

The previous novelty / Gate-C material is retained as historical project state
and is **not an active prerequisite** for the physical line. Sec. 7 is unchanged
and still governs anything done under the point-(3) contract.

### 8.8 LDP_RADIAL_INTERPRETATION — PASSED, subline CLOSED (2026-09-16)

**Status: `DOCUMENT_EXISTING_RESULT` — PASSED. This subline is CLOSED.**
Contract: [`OPERATIONAL_INVISIBILITY_GATE.md`](../theory/OPERATIONAL_INVISIBILITY_GATE.md).
A first freeze at `a9e611a` chartered the *directional* variant; it was narrowed
by user instruction before any solving and is **SUPERSEDED, UNSOLVED** — nothing
may be cited from it.

For walk (5.15), CJWW's own radial rate function Eq. (5.21),
`R̃(ℓ) = 2 arccosh(cosh(ℓ/2√3)³)`, has exactly the two slopes

`R̃'(0) = 1 = c_IR`   and   `R̃'(∞) = √3 = max_n̂ v_sub(n̂) = v_sub(body diagonal)`,

so by Legendre duality `Ĩ(r) = 0` for `r ≤ 1`, `0 < Ĩ(r) < ∞` for `1 < r < √3`,
and `Ĩ(r) = ∞` for `r > √3`, reproducing CJWW's control value `Ĩ(1.1) ≈ 0.104`.
Three regimes, with boundaries at precisely the two numbers Sec. 8 canonizes:

**ballistic/emergent | causal but exponentially suppressed | causally forbidden**

**ESTABLISHED (exact).** The *value* of (5.21) at CJWW's stated maximizer is
exact; the *location* of that maximizer is their numerical finding, not ours.

**Declared limitations, not to be dropped.**
- `Ĩ` is radial and demonstrably coarse. Since `v_sub(ê_i) = c_IR`, a velocity
  `r ê_i` with `r > 1` is already outside `C_micro`, where the amplitude is
  **exactly zero**, not suppressed. The finite rate `Ĩ` reports for `1 < r < √3`
  is therefore carried by non-axial directions only. The angular structure of
  `I(x)` is **not resolved**.
- Upper bound only; CJWW prove no lower bound.
- It bounds the position distribution of one particle, nothing else.

**Non-implication, explicit.** This does **not** yield an operational-invisibility
or no-signalling theorem. At QCA level an exponentially small tail still lies
inside the exact causal support, so "operationally invisible" may not be
asserted. That question needs resources, distinguishability or channel capacity
defined first, changes problem class, and merits an independent charter.

**NOT_AUTHORIZED:** anisotropic/directional `I(v)`; probability vs signalling.

(For the canonical conclusion of Sec. 8 as a whole, see Sec. 8.9.)

### 8.9 Canonical conclusion — stated at the right logical level

Earlier wording here read "`c_IR` **can** be the boundary of typical macroscopic
propagation without coinciding with the microscopic causal boundary". That is
modal, and too weak: this is not a possibility claim but an **explicit
counterexample**. Corrected, and canonical:

**(i) Existence — PROVED (exact).**

> There exists at least one local, unitary, finite-range model in 3D — the
> one-particle translation-invariant walk of CJWW Eq. (5.15) on `Z^3`, internal
> space `C^2`, jump length 1 — in which **all** ballistic propagation satisfies
> `|v_g| ≤ c_IR`, while the microscopic causal region is **strictly larger**
> than the emergent relativistic cone:
>
> `sup|v_g| = c_IR`  **and**  `B(c_IR) ⊊ C_micro`.

Both halves are exact: `sup|v_g| = c_IR = 1` by the SOS certificate of Sec. 8.4,
and `B(c_IR) ⊊ C_micro = [-1,1]^3` with `v_sub(n̂) = ||n̂||_1` reaching `√3 c_IR`
on the body diagonals, certified at every vertex ray for every `n` (Sec. 8.5),
hence not a one-step artefact. This statement does **not** rest on the
numerically supported half of `Γ_2 = B(1)`.

**(ii) Logical consequence — PROVED in the class studied.**

> `c_IR = sup|v_g|  ⇏  B(c_IR) = C_micro`.
>
> Equivalently: the equality "`c_IR` = microscopic causal limit" is **not a
> necessary consequence of relativistic emergence**.

**(iii) Explicitly NOT established — UNKNOWN.**

> `c_universe < ` the fundamental causal limit of our universe.

No evidence is offered here in either direction. This project makes **no claim
about our universe**; asserting (iii) from (i)-(ii) would be a category error,
since (i) is an existence result inside a declared model class.

### 8.10 SUBSTRATE_CONE_OBSERVABILITY — PASSED, gate CLOSED (2026-09-16)

Contract [`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](../theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md)
frozen at `d86b018` before solving;
[outcome](../reports/2026-09-16--substrate-cone-observability.md). This lifts
the Sec. 8.8 `NOT_AUTHORIZED` for the signalling question only.

The question was operational: for `ct < L < v_sub(n̂)t`, is `D = 0` or `D > 0`?
It is **undefined** for the one-particle walk, so the gate declared a
free-fermion (CAR) lift. On the one-particle sector `α_t(n_x) = W^t P_x W^{t†}`,
so `[α_t(n_x), n_y]` has `(y,y')` block `(W^t)_{y,x}((W^t)_{y',x})†` and is
nonzero exactly when the single-particle kernel is. **The operational causal
structure of the lift is the strict support of `W^t`** — the object already
certified in Sec. 8.5.

**Answer: `D > 0`, exponentially small, strictly off-axis.** Exactly zero for
`L > v_sub(n̂)t` (H4); nonzero `∝ 4^{-t}` at the vertex rays for
`ct < L < v_sub(n̂)t` (H2); **exactly zero in the six axial directions** for
every `L > ct`, since `v_sub(ê_i) = c` (H3). At `t = 3`, 108 of the 148
populated sites lie strictly outside `B(c)t`, all inside `C_micro t`, none
axial. **ESTABLISHED (exact, Gaussian-integer kernels).**

This is the signature sought: fundamental causality outside the light cone with
no superluminal ballistic propagation, carrying the angular fingerprint
`v_sub(n̂) = ‖n̂‖₁ c`.

**Limits.** Statements are about the lift, not the one-particle walk. A nonzero
commutator means *there exists* an intervention and a state with `D > 0`; no
specific protocol's `D` and no channel capacity were computed. How the
suppression varies across `C_micro \ B(c)` is the anisotropic `I(v)` question,
still `NOT_AUTHORIZED`. No claim about our universe: Sec. 8.9(iii) stands at
UNKNOWN, and a wider cone fully decoupled from accessible observables would be
invisible to any experiment, so no null result can establish exact coincidence.
No experimental or LIV constraint survey is authorized.

### 8.11 EMPIRICAL_SUBSTRATE_CONE_SURVEY — COMPLETE (2026-09-16)

Contract [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md)
frozen at `416dde1`;
[outcome](../reports/2026-09-16--empirical-substrate-cone-survey.md).

**Declared premise (computed before surveying).** With `t` in lattice steps, a
Planck-scale substrate puts this model's own effect at `10^(-8.4e41)` over one
second, against finest-ever bounds of `10^-20` to `10^-30`. The model's effect is
**unobservable in principle**. The survey is therefore model-independent. The
geometric window is by contrast not small: it reaches `√3 ct`, 73% beyond the
light cone.

**Verdict, in three levels.**

| | |
| --- | --- |
| Scalar no-signalling | experimentally tested, to finite precision |
| Directional causal tail of Sec. 8.10 | no specific localized operational test |
| Exact equality `C_fundamental = B(c)` | **not established** by null results |

In contract categories: `DIRECT_CONSTRAINTS_FOUND` for the scalar variable,
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure.

**Missing coupling map — the real obstacle.** `[A(t),B] ≠ 0` gives `∃` a state
and intervention with `D > 0`; it does **not** give that a standard Bell-test
protocol is that intervention. Converting a bound on Bell marginals into a
quantitative bound on the tail needs a coupling/protocol map — which observable
realizes `A`, which realizes `B`, which preparation exploits the commutator.
None exists. The scalar bound therefore constrains the right *kind* of variable
without being convertible into a number about our `D`.

**Withdrawn.** An earlier phrasing used Adenier–Khrennikov to fix the empirical
level at "percent-to-permille". That was an overreach: it is a contested
reanalysis of one dataset, not a universal bound nor a calibrated interval for
`D`. No numerical empirical level is claimed. Likewise "essentially untested" is
replaced by the exact-equality statement above.

**Category error recorded, the survey's main result.** Salart 2008 (`v > 10⁴ c`)
and Bancal 2012 (finite-speed influence ⟹ superluminal signalling) constrain
models where the superluminal influence *explains* the quantum correlations. The
tail of Sec. 8.10 is non-explanatory, so those bounds do **not** apply to it;
using them to "exclude" it would be a category error. LIV/dispersion/threshold
limits are `INDIRECT_ONLY` by contract Sec. 2.1, since Sec. 8 proves
`sup|v_g| = c` is compatible with influence outside `B(c)`. Lieb–Robinson
experiments (Cheneau 2012 and successors) **observe** this structure in
engineered lattices: realizability, not a constraint on nature.

**Consequence, and the firm epistemological point.** No finite sequence of null
results can prove `D = 0` exactly; it can only yield ever smaller upper bounds.
A reproducible positive result outside `B(c)` could falsify the identification
of `c` with the fundamental causal boundary. Sec. 8.9(iii) stands at UNKNOWN.

**Next step if the line continues (not opened).** Not a further theoretical
front, and not a generic FTL search: design the experiment that **maximizes `D`**
for a Sec. 8.10-type tail — which two local operations, which spacelike
separation, which remote observable optimally exploit an exponentially small,
anisotropic causal tail. Only afterwards does it make sense to ask whether an
existing experiment already did this accidentally, and by how much it falls
short. This is the coupling map above, and it is **not chartered**.

### 8.12 COUPLING_MAP_OPTIMAL_D — PARTIAL; exact signalling witness CLOSED (2026-09-16)

Contract [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md) frozen at
`0f7628d`: frozen Sections 0–6 unchanged, outcome corrected;
[report](../reports/2026-09-16--coupling-map.md).

**Correction authorized by the user, 2026-09-16.** The former conditional H1
confirmation, universal linear/quadratic scaling and claimed restricted
optimal-D upper bound are withdrawn. The code computed an occupation
witness, not full trace-distance optimization. Four finite times cannot
establish asymptotic scaling; moreover `t = 5` exceeded the frozen `{2,3,4}`.
The historical ratios remain descriptive only. H1 is **OPEN**; H2 establishes
preparation dependence for the specified protocol, not necessity of coherence
for all admissible interventions. **H3 and H4 remain NOT REACHED**.

**Finite existence task: EXISTENCE_WITNESS_PROVED / INDEPENDENTLY_REVIEWED.** The user's
subsequent instruction chartered closure as a theorem/witness, not further
optimization or an experimental study. See
[`COUPLING_MAP_SIGNALING_WITNESS.md`](../theory/COUPLING_MAP_SIGNALING_WITNESS.md).
At `t = 2`, Alice at `0`, Bob at `y = (2,2,2)`, prepare
`(|0,down> + |y,down>)/sqrt(2)` before Alice chooses between `I` and
`exp(i pi n_0)`. Bob measures the even non-vacuum projection at his site.
The exact probabilities are

`p_0 = 121/512`, `p_1 = 169/512`, `Delta p_B = 3/32 > 0`, hence **`D >= 3/32`**.

The theorem fixes the existing CAR/Heisenberg convention, the state,
intervention, measurement and spacetime point. The exact kernel is nonzero
there: Bob is outside the emergent ball and **on the microscopic boundary**.
This proves membership in the exact causal support, not strict interior
membership. Each local site has two modes; the original `N = M = 1`
optimization is not closed. The
[verifier](../scripts/verify_signaling_witness.py) passes **17/17 exact checks**.
The [independent review](../reports/2026-09-16--signaling-witness-independent-review.md)
returns **PASS on the four requested points, no mandatory repairs**: analytic
probabilities, code correspondence, causal location, and the convention
`D = (1/2)||rho_1-rho_0||_1`. It records hashes of the unchanged reviewed
theorem and both scripts. This is one separate agent's independent review,
not external human review, consensus, or a full PASS of the optimal-D gate.

**Claim ceiling, branch-local:**

> In this free-fermion lift, given a state prepared with coherence between
> Alice and Bob's own site before Alice's choice, that local choice changes
> a measurement probability accessible
> to Bob outside the emergent relativistic cone and within the exact
> microscopic causal support. The choices are distinguishable in principle.
> Preparation of this operational channel from resources initially localized
> around Alice, Bob's optimal measurement, a globally optimal protocol and
> experimental feasibility are not established.

**Superseded clause, 2026-09-16.** The requirement of a resource already
distributed before Alice acts is no longer open: Sec. 8.13 exhibits a
*different* channel, in the same model, driven from a particle initially at
Alice alone. That successor does **not** supply a preparation protocol for
*this* channel, whose theorem, review and ceiling above are unchanged.

**Controls and limits.** For an Alice-localized particle the phase gate gives
only a global phase, hence exactly zero signal. Removing spatial coherence
also removes this protocol's signal. At the axial control the exact zero
kernel excludes Alice from the evolved Bob algebra, hence forbids signalling
for any initial state under even local Alice unitaries. By contrast, a zero
occupation witness alone never certifies `D = 0`.

The second coherent arm in this construction is **at Bob's initial site**;
the earlier hint excluding Bob from the resource is withdrawn. No Bell
protocol has been modelled. The finite interference term involves both
`K_0y` and `K_yy` with their internal alignment, not a universal asymptotic
law in one kernel. The empirical transfer of Sec. 8.11 remains unresolved;
the experimental problem is not opened. No claim about our universe follows.

**The original question, split.**

| Question | Answer |
| --- | --- |
| Theoretical: must `c` coincide with the substrate's causal limit? | **No** — (ii), proved |
| Physical: does it coincide in our universe? | **Unknown** — (iii) |

### 8.13 ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED (2026-09-16)

Successor to Sec. 8.12, chartered by direct user instruction as an
**existence question only**: does the signalling channel require a resource
that is already spatially distributed before Alice acts? **It does not.**
See [`ALICE_LOCAL_PREPARATION_WITNESS.md`](../theory/ALICE_LOCAL_PREPARATION_WITNESS.md)
and the [construction report](../reports/2026-09-16--alice-local-preparation.md).

Same unchanged CAR lift of CJWW (5.15), same conventions. At `T = 0` the
resource is exactly one particle, `|0,down>`, with every other mode vacant.
Between `T = 0` and `T = 2` **only the declared free dynamics acts**, equally
for both messages: the prepared state is `chi = S^2|0,down>`, given in closed
form by Cayley-Hamilton (`S^2 = 2fS - I`, `f = cos p1 cos p2 cos p3`), with
38 populated sites, `||chi|| = 1`, `chi(0) = -3 down/4` and
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`. Alice encodes at `A = (2,0)`
with `I` or `exp(i pi n_0)`; Bob measures the even non-vacuum projection at
`B = (3,(1,1,1))`. The exact probabilities are

`p_0 = 49/1024`, `p_1 = 25/1024`, `Delta p_B = 3/128 > 0`, hence **`D >= 3/128`**.

**Causal origin — the load-bearing step.** The bit is exogenous at `T = 2`.
Both conditional histories are *identical operators on the whole Fock space*
for `T = 0, 1, 2^-`, so the mutual information between the bit and any
pre-choice observable is exactly zero and no earlier encoding exists. Bob's
own site is **exactly vacant** at the encoding event (`chi(1,1,1) = 0`).
Comparing cones from `T = 2` is therefore the appropriate operational
reference for communication. From the encoding event,
`|y_B| = sqrt(3) > c_IR Delta T = 1` while `||y_B||_inf = 1` and
`K_1(0,y_B) = diag(0,1/4) != 0`: Bob is outside the emergent cone and on the
**boundary of the exact microscopic causal support**. **No microscopic
causality bound of the model is violated.** It is explicitly *not* claimed
that Bob is outside the emergent cone of the initial event: from `T = 0`,
`sqrt(3) < 3`.

**Claim ceiling, branch-local:**

> A particle initially localized at Alice alone suffices. The ordinary
> microscopic dynamics generates the required spatial coherence before the
> message is chosen. A later local choice by Alice then changes a Bob
> statistic one step afterwards, with Bob outside the emergent causal cone
> of **that encoding event** and within the microscopic causal support.
> This is not a violation of the model's microcausality. Optimality,
> minimal preparation time, experimental feasibility, asymptotics, capacity
> and any claim about our universe are **not** established.

**Evidence.** `verify_directional_saturation.py --local-preparation-only`
passes **21/21 exact checks**; the frozen witness verifier still passes
17/17 and the default suite 27/27, unchanged. The
[independent review](../reports/2026-09-16--alice-local-preparation-independent-review.md)
returns **PASS, no mandatory repairs**, and explicitly covers the item most
exposed to adversarial attack: the closed-form derivation of `S^2|0,down>`
and the identity of the two pre-choice histories. It reconstructs the
prepared state from a separately transcribed symbol, records SHA256 hashes of
every reviewed input, and confirms the script change is one added function
plus a CLI dispatch, with the frozen witness path untouched. This is one
separate agent's independent review — **not** external human review,
multi-member consensus, or ratification.

**Relation to Sec. 8.12.** The hypothesis is strictly weaker (no pre-existing
Alice-Bob coherence) and the geometry differs (one readout step to
`(1,1,1)`, not two to `(2,2,2)`); the signal is smaller, `3/128` against
`3/32`. This does **not** retroactively supply a preparation protocol for the
Sec. 8.12 channel, whose frozen theorem and review keep their exact bytes and
scope. The optimal-D gate stays **PARTIAL**; H1 stays **OPEN**; H3 and H4 stay
**NOT REACHED**. The experimental problem remains unopened, by instruction.

### 8.14 NONCORNER_SIGNALING_CONSTRUCTED / INDEPENDENTLY_REVIEWED (2026-09-17)

Successor to Sec. 8.13, executed under the frozen
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md): the
Alice-local preparation channel is **not** confined to the vertex
`(1,1,1)`. The [corrected execution report](../reports/2026-09-16--noncorner-signaling-gate.md)
and its [independent review](../reports/2026-09-16--noncorner-signaling-gate-independent-review.md)
are frozen together here. The review verdict is **PASS with three mandatory
textual repairs (`MR1`--`MR3`)**, all applied to the report; none changes a
computed quantity or the scientific verdict.

The exact one-step kernel support gives precisely four admissible non-vertex
sites, `y = (+/-1,+/-1,0)`, and the preregistered construction succeeds at
all four. At each site,

`M(y) = diag(-3/256,0) != 0`,
`p_0 = 25/1024`, `p_1 = 49/1024`, and `Delta p_B = 3/128`.

The reduced-state trace distance is exactly `D = 3/128`, so the exhibited
projection saturates the distinguishability bound for each computed pair of
states. This is pairwise measurement optimality only; it is not protocol,
preparation, site or intervention optimality. The result refutes
vertex-exclusivity for this protocol at `Delta T = 1`; it says nothing about
`Delta T = 2`, other vertices, asymptotic scaling, capacity, experimental
feasibility or our universe. No violation of the model's microscopic causal
bound is claimed.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NONCORNER_SIGNALING_CONSTRUCTED /
  INDEPENDENTLY_REVIEWED` in the exact scope above.
- **Software certificate: PASS with six externally verified properties not
  yet encoded as checks.** The run
  `verify_directional_saturation.py --noncorner-gate-only` passes **20/20
  exact checks**, but that count **is not by itself an exhaustive certificate**
  of the six properties listed in the execution report Sec. 8. They were
  independently checked by the reviewer. They remain recorded certification
  debt, not gaps in the scientific result.

The reviewed script is deliberately unchanged after review. Encoding those
six additional checks would alter the reviewed artefact and therefore require
a new review of that file. The earlier frozen contracts and witnesses retain
their bytes and scope; the optimal-D gate remains **PARTIAL** and no
experimental-design gate is opened here.

### 8.15 PHYSICAL_DIMENSIONAL_TRANSLATION — CLOSED / CONDITIONAL (2026-09-17)

Contract
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](../theory/PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md)
frozen at `fca5881` before solving; see the
[dimensional audit](../reports/2026-09-17--physical-dimensional-translation-audit.md).

**Verdict: `DIMENSIONAL_MAP_CONDITIONAL`.** The source conventions support the
symbolic restoration

`x = a n`, `t = N tau`, `k = p/a`,
`E = hbar omega/tau (mod 2 pi hbar/tau)`, and
`v_phys = (a/tau) grad_p omega`.

Hence `c_IR^phys = a/tau`. Identifying it with an observed `c_phys` imposes
`a = c_phys tau`; it does not determine either absolute scale. The model and
checked sources specify no numerical `a` or `tau`, and the earlier Planck-scale
calculation was explicitly conditional, not a scale derivation.

For the frozen non-corner witness, conditionally on `(a,tau)`, the
encoding-to-readout interval is `tau` and Bob is at Euclidean distance
`sqrt(2)a`. If `a/tau = c_phys`, then the scale-free ratio is
`L/(c_phys tau) = sqrt(2)`: outside the emergent cone and inside the exact
one-step microscopic support, exactly as in lattice units.

The value `3/128` acquires **no units**. It remains the exact probability
difference and trace distance for the two idealized local states. It is not an
energy, rate or dimensional coupling. The exactly localized preparation is
broad over the full Brillouin zone, not a low-energy narrow-band state, so no
unique physical energy or momentum can be assigned from the IR dispersion.

**Claim ceiling.** A consistent conditional dictionary is established; a
parameter-free prediction in SI units is not. Absolute cutoff scale, physical
realization/coupling, efficiencies, noise, feasibility and any identification
with nature remain unspecified. No experiment was designed and `Delta T = 2`
was not opened.

### 8.16 NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md)
preregistered at `817050d` before any computation. Three artefacts are frozen
together at `778a44a`, through the provenance chain `5f6d350` -> `f00f64e` ->
`778a44a`:

- the [execution report](../reports/2026-09-17--narrow-band-signaling-gate.md);
- its exact certificate
  [`verify_narrow_band_gate.py`](../scripts/verify_narrow_band_gate.py);
- the [independent review](../reports/2026-09-17--narrow-band-signaling-gate-independent-review.md).

The question was whether the Alice-local signalling mechanism admits an
IR-controlled version with a preestablished narrow-band resource. The frozen
class is:

- node `p = 0`, both Weyl branches;
- `g(q) = (1-|q|^2)^2_+` supported on `|p| <= Lambda`, with
  `0 < Lambda < pi/4`;
- spin `down` and two common steps;
- the point gate `U_1 = exp(i pi n_0)` at the origin;
- Bob at `(1,1,0)`, with `Delta T = 1`.

**Verdict.** The Sec. 7 stop rule fires at the first control, before any signal
in Bob is computed: the point encoder is incompatible with the preregistered
relative IR criterion. Let `kappa = Lambda^3/(6 pi^2)`, the in-band share of
any one-site vector, and `s = ||P_0 psi_Lambda||^2`, with `0 < s <= kappa`. Then

`||Delta_Lambda||_1 = 4 sqrt(s(1-s)) -> 0`,
`eta_enc = ||Delta - Pi Delta Pi||_1/||Delta||_1 = sqrt((1-kappa)(1-3s(1-kappa))/(1-s))`.

So `eta_enc > 2 sqrt(6)/5` on the whole chart and `eta_enc -> 1`, while the
absolute leakage `epsilon_UV = 4s(1-kappa)` also tends to zero. The residual
outside the IR-IR block is dominated by the IR-UV and UV-IR coherences; the
UV-UV block is relatively `O(sqrt s)`. This is **not** a statement that the
encoding, the information or any signal is UV.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS /
  INDEPENDENTLY_REVIEWED`, in the exact scope below.
- **Review metadata.**
  - Cold independent agent review: PASS, after the mandatory repairs R1-R4 and
    MR1, all textual and all applied.
  - Human review: PASS.
  - No external peer review / no external replication yet.
  - Two earlier same-session adversarial reviews are archived as secondary,
    non-independent records. The self-review contains errors that the
    independent review corrected.
- **Software certificate: PASS, 34/34 exact checks.** The count covers only
  the identities and limits marked [V] in the report. The analytic steps listed
  in report Sec. 12 are not encoded as checks; the independent reviewer
  verified them by hand. They are recorded certification debt, not gaps in the
  result. The certificate imports `verify_directional_saturation.py`, which
  requires numpy, pinned in `scripts/requirements.txt`.

**Claim ceiling.** The result holds only for the frozen class and the Sec. 7
criterion.

- `D_B` was not computed, and `D_B = 0` is not asserted.
- It does not refute `3/128`, either at the vertex or at the non-corner sites.
  The non-corner witness uses the same `y_B = (1,1,0)`, but with an exactly
  localized resource and no IR criterion.
- It is no impossibility result for other encoders (extended, smoothed or
  `Lambda`-dependent gates), for resources without exact spectral support, for
  other notions of IR control, for other QCA, or for the physical continuum.
- `Lambda -> 0` is not `a, tau -> 0`, and no physical scale is set
  (Sec. 8.15).

**Erratum, charter header.** Lines 3-7 of the charter are pre-publication
text. They cite drafting base `HEAD=11efe1f` and scientific remote `780ecb0`,
state `NOT_EXECUTED / OUTCOME_OPEN`, and say that publication and execution
are pending. All of that is superseded: the charter was published at
`817050d`, executed, and frozen at `778a44a` with the status recorded in this
section. The charter deliberately keeps its bytes, for two reasons:

- its sha256 `3d559ced...` is pinned by the frozen certificate (check 1)
  and recorded in the report, the independent review and the freeze
  commits;
- contracts in this repository keep their pre-execution text, as
  `NONCORNER_SIGNALING_GATE.md` does.

The header was never part of the scientific contract (Secs. 1-15), which
is unchanged. `Delta T = 2` and the experimental problem remain unopened.

### 8.17 OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`SCALED_IR_SIGNALING_GATE.md`](../theory/SCALED_IR_SIGNALING_GATE.md)
preregistered at `31b5797` before any computation. Successor of Sec. 8.16,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--scaled-ir-signaling-gate.md);
- its exact certificate
  [`verify_scaled_ir_gate.py`](../scripts/verify_scaled_ir_gate.py);
- the [independent review](../reports/2026-09-17--scaled-ir-signaling-gate-independent-review.md).

The question is the disappearance law of Bob's distinguishability when
regions of size `O(1/Lambda)`, a margin `O(1/Lambda)` outside the emergent
cone of Alice's whole region, and time `O(1/Lambda)` are scaled together
(`N = Delta T = 1/Lambda`, Euclidean balls of radius `N/4`, frozen internal
families). A signal at fixed `Delta T`, or with an `O(1)`-site margin, does
not answer it.

**Verdict.** `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The eight frozen operations are IR-admissible. There is a directional
exponential upper bound, independently re-derived, for every one-particle
state and every unitary supported on `A_N`:

`δ_{M,M_B}(N) ≤ D_B(N) ≤ 36 N^4 exp[-(1 - √3/2)(log 2) N]`, `N ≥ 2`,

with `J = (1 - √3/2) log 2 > 0`. This **excludes**
`IR_RESOLVABLE_SIGNALING_POLYNOMIAL` in the frozen class and **does not
authorize** `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. All sixteen pairs
remain `OPEN_PAIR`: no positive lower bound, no proven vanishing, no
non-vanishing amplitude. `D_B = 0` is not asserted. The independent review
attacks specifically the three load-bearing steps named before promotion
(the geometry-to-kernel derivation of `J`, uniformity of `36 N^4`, and
polynomial exclusion without an existence claim) and returns **PASS**, with
no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with a one-sided quantitative bound.**
  `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`, in the exact
  scope below.
- **Review metadata.**
  - Cold independent agent review: PASS. No mandatory repairs. The three
    recommended drafting clarifications (`D_B = (1/2)||ρ1-ρ0||_1`;
    off-diagonal of the ellipse matrix; Schur diagonal operator-norm) were
    applied to the execution report at freeze. They change no quantity and
    no classification. Execution-report sha256 before/after those phrases:
    `4876ecab…` / `86a086dc…`. The CAR bound (DF) is not part of the frozen
    claim for the sixteen pairs.
  - Human freeze authorization: the 2026-09-17 instruction to freeze this
    status if the cold review passed, then to publish with those
    clarifications and without additional science.
  - No external peer review / no external replication yet.
- **Software certificate: PASS, 53/53 exact checks.** The count covers only
  the identities and limits marked [V] in the execution report. The
  analytic steps for `J`, `T_N`, `(D1)` and the classification were
  re-derived by the independent reviewer; they are not encoded as checks.

**Claim ceiling.** The result holds only for the frozen scaled class
(Euclidean balls, `α = 1/2`, `θ = π/2`, the declared internal families,
CJWW (5.15) in the one-particle sector).

- Any allowed effect in this class is at most `O(N^4 e^{-JN})`. That is a
  one-sided, model-falsifiable bound. It is not a two-sided prediction and
  not an existence result.
- Polynomial IR-resolvable signalling is discarded **in this
  geometry/class**. If a positive signal exists, it is at most
  nonperturbatively small. Existence is not claimed.
- The bound does not refute `3/128`, the vertex or non-corner witnesses, or
  the narrow-band negative (Sec. 8.16).
- `N → ∞` is not `a, τ → 0`. No physical scale is set (Sec. 8.15). An
  `e^{-JN}` law would translate only conditionally to a form
  `e^{-J' λ/a}`, with no numerical prediction.
- The internal families are not exhaustive. `M = a I + b·σ` in general is
  not covered. `I` is `REFERENCE_CONTROL` only.
- No new encoder is authorized. The cancellation analysis of the sixteen
  pairs is Sec. 8.18. The regional exponential rate is Sec. 8.19. The
  remaining bottleneck is the integrated Laplace coefficient
  (Hessian, profiles, spin, interference with the free tail `r`), not
  yet chartered.

`Delta T = 2` and the experimental problem remain unopened.

### 8.18 OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`LOWER_BOUND_NO_CANCELLATION_GATE.md`](../theory/LOWER_BOUND_NO_CANCELLATION_GATE.md)
preregistered at `1717d5e` before any computation. Successor of Sec. 8.17,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--lower-bound-no-cancellation-gate.md);
- its exact certificate
  [`verify_lower_bound_no_cancellation_gate.py`](../scripts/verify_lower_bound_no_cancellation_gate.py);
- the [independent review](../reports/2026-09-17--lower-bound-no-cancellation-independent-review.md).

**Verdict.** `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The unique-path vertex

`(S^N)_{(N,N,N),0} = 4^{-N} |↓⟩⟨↓|`

exists and cannot be promoted to a regional leader (`K = log 4`, kills
`↑`, coherent regional sum). The Euclidean minimum of `|y-x|_2` on the
two balls is unique and lies on both spheres, where the profiles vanish.
That implies neither `A = 0` nor `A ≠ 0`. All sixteen pairs remain
`OPEN_PAIR`. `D_B = 0` is not asserted. The independent review attacks
those three load-bearing claims and returns **PASS**, with one recommended
drafting clarification applied at freeze (execution-report sha256 before /
after: `33691df6…` / `2da09280…`).

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN.** The obstacle is now localized: the
  competition between the propagation exponent and the profile zero at
  the boundary, not a missing trajectory and not a new encoder.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed.
- **Software certificate: PASS, 24/24 exact checks.** Identities only;
  leader, `A` and remainder are analytic and open.

**Claim ceiling.** Same frozen class as Sec. 8.17. No existence, no
vanishing, no `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The regional
rate is Sec. 8.19.

### 8.19 OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`](../theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md)
preregistered at `08613d0` before any computation. Successor of Sec. 8.18,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--regional-directional-asymptotics-gate.md);
- its exact certificate
  [`verify_regional_directional_asymptotics_gate.py`](../scripts/verify_regional_directional_asymptotics_gate.py);
- the [independent review](../reports/2026-09-17--regional-directional-asymptotics-independent-review.md).

**Verdict.** `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The regional exponential rate is

`K_* = I(v_*)`, `v_* = (1 - 1/(2√3))(1,1,1)`,

with `I(v) = sup_ξ [ξ·v - arcosh(∏_j cosh ξ_j)]`. This is strictly
between `J` and `log 4`. It is the unique minimizer of `I` on the
regional velocity set (supporting tilt `ξ_* ∥ û`). The profile logarithms
are `O(log N)` and shift the saddle by `O(1)` lattice sites; they do
**not** change `K_*`. The coefficient `C` and the power `β` remain
unclassified. All sixteen pairs remain `OPEN_PAIR`. The independent
review attacks the three load-bearing claims (`I(v)` and the dual saddle;
uniqueness of `v_*`; `O(log N)` profiles) and returns **PASS**, with no
mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with the exponential rate identified.**
  `K_* = I(v_*)` is the Legendre envelope of the regional kernel. It is
  the exponential rate of `L` only if some `C` (or `C^{(j)}`) is
  non-vanishing and controlled, which is not claimed.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed, and not to open a
  coefficient gate before that review.
- **Software certificate: PASS, 18/18 exact checks.** Identities only;
  `C`, `β` and remainder are analytic and open.

**Claim ceiling.** Same frozen class. This section does not claim
existence, vanishing, or `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
No new encoder. The complete Laplace coefficient at this unique saddle
is Sec. 8.20.

### 8.20 PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_LAPLACE_COEFFICIENT_GATE.md`](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md)
preregistered at `6f520ad` before any computation (blob `18d1f65`).
Successor of Sec. 8.19, without reopening it. Three artefacts are
recorded together here:

- the [execution report](../reports/2026-09-17--regional-laplace-coefficient-gate.md);
- its exact certificate
  [`verify_regional_laplace_coefficient_gate.py`](../scripts/verify_regional_laplace_coefficient_gate.py);
- the [independent review](../reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md).

**Verdict.** `PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.
For all sixteen frozen pairs,

`L_{M,M_B}(N) = e^{-K_* N} N^{-13/2} (C_{M,M_B}(θ_N) + O(N^{-1/2}))`,

with `θ_N = {√3 N/4}` and `β = 13/2`. The complete coefficient is a sum
of the free-tail interference against the encoder layer, over the two
torus saddles `η ∈ {0, π(1,1,1)}` (distinct projectors `P` and `P̄`,
weights `Γ_±`). `C(θ)` is sign-definite and uniformly non-vanishing; the
relative oscillation is bounded by `1.47×10^{-3}`. Quadratic terms are
only bounded, at rate `e^{-2 K_* N}`. The independent review attacks the
seven load-bearing claims (`β`; complete `C` as a sum; uniform
non-vanishing; remainder vs charter `o(1)`; `C(θ)` vs constant `C`;
eight torus points vs frozen `K_*`; terminal state) and returns **PASS**,
with no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: PAULI_LEADING_COEFFICIENT_NONVANISHING.** `β = 13/2`
  is identified. All twelve Pauli pairs have `C(θ) ≠ 0` uniformly in `θ`,
  controlled against an `O(N^{-1/2})` remainder. With Secs. 8.17 and 8.19
  this authorizes, for those twelve pairs,
  `δ_{M,M_B}(N) = |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N} (1 + O(N^{-1/2}))`
  and `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` for those pairs. The
  four `M = I` pairs are also non-vanishing (`REFERENCE_CONTROL`).
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze, commit and promote as separate steps if the cold review passed.
- **Software certificate: PASS, 58/58 exact checks.** Identities and
  interval enclosures of closed forms, including uniform sign of
  `C_{M,M_B}(θ)` for all sixteen pairs. Analytic remainder lemmas (`N_*`,
  `C'`) are report `[A]`, not encoded. Finite-`N` diagnostics are
  `SUPPORTED` only.

**Claim ceiling.** Same frozen class. `C = C(θ_N)`, not an `N`-independent
constant. The remainder is asymptotic: `N_*` and `C'` are not explicit;
the leading formula is not quantitatively reliable for `N ≲ 10^3`, and
for `M ∈ {I, σ_3}` the `N^{-17/2}` piece dominates at diagnostic `N`.
No `D_B = 0`, no `δ ≡ 0`. Does not reopen `K_*`, `v_*`, geometry,
encoders, detectors, profiles, node or walk. Does not reopen
Secs. 8.16–8.19, `3/128`, no-corner, or `Delta T = 2`. `N → ∞` is not
`a, τ → 0`. No physical units. No claim of a microcausality violation.
The general family `M = a I + b · σ` is not covered.

The Sec. 8.19 sentence that the spectral-radius maximum is unique at
`η = 0` is false (equality on `{0,π}³`); `K_*` is unchanged and the extra
contributing point `π(1,1,1)` is included in `C`. The Sec. 8.19 files
are not edited.

This is a branch-local promotion only; `main` is unchanged.

**Project-level consequence (direct user instruction, 2026-09-17).**
In this frozen class, theoretical step 3 of the physical line is closed.
There is an operational IR response outside the emergent cone, and it is
not a mere consequence of the UV propagator. For the twelve Pauli pairs
the response is asymptotically non-vanishing and
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The precise claim, not to
be exaggerated, is:

> In the 3D Weyl QCA under study, the difference between the emergent
> relativistic cone and the microscopic causal support is not only a
> geometric possibility: under the preregistered IR-controlled protocol
> it produces an asymptotically non-vanishing operational response,
> albeit nonperturbatively suppressed.

That is a property of the model, with standing outside the repository as
such. It is not a statement about nature, not `D_B > 0` for every QCA,
and not an experimental prediction. No further signalling gate is
authorized. Fork 4A (a physical implementation of the walk that could
test the derived law) is identified and **not chartered**. The authorized
next front is Sec. 8.21.

### 8.21 PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — AUTHORIZED (2026-09-17); EXECUTED (2026-09-25)

`EXECUTION_AUTHORIZED_BY_DIRECT_USER_INSTRUCTION — 2026-09-25` («Pues vamos con el 8.21», 14:54 UTC). The status `NOT_EXECUTED` and the clause “Not authorized: execution of this gate” were correct as of 2026-09-17 and are superseded by that instruction.

Contract
[`PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md`](../theory/PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md)
frozen before any calculation, by direct user instruction (2026-09-17),
with the four closure criteria and first-class negative outcomes
incorporated before execution (this commit; first preregistration
`e9353ad`). Successor of Sec. 8.20, without reopening it. Inherits
Sec. 8.15 (`DIMENSIONAL_MAP_CONDITIONAL`) without reopening the `3/128`
audit. **Not a signalling gate, not a rate gate, not a Laplace-coefficient
gate, not a laboratory-implementation gate (4A).**

**Execution 2026-09-25:** `NO_ABSOLUTE_SCALE_DERIVABLE`.
Evidence: `EXECUTED / PRELIMINARY / PARTIAL_EXTERNAL_REVIEW`.
[Execution report](../reports/2026-09-25--physical-realization-absolute-scale-gate.md).
The frozen model fixes only `a/tau=c`; the targeted literature recheck supplies
engineered simulators and external bounds on lattice spacing, but no absolute
scale or natural physical dictionary for the complete Sec. 8.20 CJWW protocol.
A conditional SI restoration is possible, with centre separation
`L_c=sqrt(3) a N` and
`delta(L_c;a) ~ |C({L_c/(4a)})|(L_c/(sqrt(3)a))^-13/2 exp[-(K_*/sqrt(3))L_c/a]`,
but `a` remains undetermined. The terminal state is not
`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`: no defensible physical map exists first.
The Planck substitution is retained only as a diagnostic ASSUMPTION. 4A was
not chartered at execution time (see addendum below: now authorized, still
without contract) and Sec. 8.20 is unchanged.
**Review 2026-09-26 (Claude):** dimensional restoration, criterion scoring,
terminal state and Planck diagnostic arithmetic verified; terminal state
correct (report Sec. 11). Not an exhaustive literature audit.

**4A authorization addendum — 2026-09-25.**
`4A = AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` by the user's later message
«Pues lo autorizo» (2026-09-25, 15:35:40 UTC). This supersedes the
`not chartered` status prospectively from that instruction only; the
2026-09-17 statements remain historically correct. Authorization does not
constitute a 4A design, execution, physical realization, or claim about
nature. A separate 4A contract is still required before scientific work.

Step 3 is **input**, not an object to re-optimize. The gate does **not**
ask whether `δ_{M,M_B}(N) ≠ 0`. It asks whether a physically defensible
identification

`(a, τ, Λ, internal modes, A, B) ↔ (physical magnitudes and operations)`

converts `δ(N) ∼ |C(θ_N)| N^{-13/2} e^{-K_* N}` into a dimensional,
falsifiable prediction.

**Four hard closure criteria, all scored separately:**

1. **Absolute scale.** `a/τ = c` is not enough. External information must
   fix `a` or `τ`, or an additional physically motivated relation must
   appear. `a = ℓ_P` is `ASSUMPTION`, never `DERIVED`.
2. **Physical dictionary.** What the two internal components are, which
   physical operation implements `M = σ_j`, what `M_B` is, and what a
   narrow-band preparation is in the candidate system. A formal relabelling
   is not a dictionary.
3. **Dimensional observable.** From a dimensionless distance/probability
   to something an apparatus records (counts, phase, frequency, energy,
   occupation, correlation, or other), with an explicit SI law.
4. **Detectability.** If substituting physical scales yields
   `δ ∼ e^{-K_* λ/a}` with `λ/a` astronomical, the effect may be real
   and experimentally inaccessible. That is a legitimate closure.

A viable experiment is **not** the success criterion. First-class
negative outcomes: `NO_ABSOLUTE_SCALE_DERIVABLE`,
`PHYSICAL_MAP_CONDITIONAL_ONLY`,
`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`. None of these weakens Sec. 8.20.

Binding separation: model closed ≠ nature established ≠ experiment designed.

**Premises, not reopened:** `K_*`, `β`, `C(θ_N)`, the sixteen pairs, the
conditional dictionary of Sec. 8.15. **Not authorized (as of 2026-09-17):** execution of
this gate (superseded 2026-09-25, see above); fork 4A; a new signalling encoder, detector or geometry;
re-optimizing `K_*` or `C`; treating `N → ∞` as `a, τ → 0`; using a
Planck fiat as `DERIVED`.

**Theory paper (draft, not a gate).** The closed model result is written
as
[`papers/ir-corona-operational-response-draft.md`](../papers/ir-corona-operational-response-draft.md).
It does not wait on 4B. It separates ultraviolet propagator, infrared
operational response, and nature.

**Literature input to 4B, not execution.**
[`2026-09-17--physical-realization-literature-scan.md`](../reports/2026-09-17--physical-realization-literature-scan.md).
Adversarial bibliographic scan only. Three bins:
`ENGINEERED_EMULATOR`, `NATURAL_EFFECTIVE_ANALOG`,
`FUNDAMENTAL_CANDIDATE`. Hard question (natural system, `a` and `τ`
physically fixed, infrared cone strictly narrower than microscopic
support, known observable of that gap): **no** on this pass. Ion-trap
and photonic Dirac automata are 4A antecedents. Pavia/Mlodinow–Brun
are incomplete fundamental candidates (Planck `ASSUMPTION`, different
observables). This scan does **not** assign a 4B terminal state.


## 9. H1-only inhomogeneous reopening — branch-local update (2026-09-20)

**Status (2026-09-25): H1 OPEN; the Schur / physical-endpoint bridge is
written but awaits independent review in Sec. 9.7. The operational contract is fixed
in Sec. 9.6. The full H1c localization claim is not closed.**

This update supersedes the older statement that physical-realization / absolute-scale
Sec. 8.21 is the active line. The flat CJWW (5.15) operational IR-corona result
remains closed in its frozen class. The later inhomogeneous/AdS extension is not
reactivated as a whole: only H1 has been reopened.

Full research record:
- [H1 chat research log](../reports/2026-09-20--h1-chat-research-log.md)
- [H1 localization reconstruction and gate ledger](../reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md)
- primary endpoint/layer source: [regional Laplace-coefficient gate](../reports/2026-09-17--regional-laplace-coefficient-gate.md)

### 9.1 Frozen local structure

For
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=e^{-i\vartheta(X)\beta/N},
\]
under the working frozen beta contract
\[
\beta^2=I,\qquad \beta D\beta=D^{-1},
\]
the dominant rank-two Riesz bundle satisfies
\[
\mathcal P\beta\mathcal P=0.
\]

Current statuses:
- \`H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT\`;
- \`H1a = PROOF_WRITTEN / UNREVIEWED\`;
- \`H1b = PROOF_WRITTEN / UNREVIEWED\`;
- \`DERIVATIVE_SELECTION_RULE = PASS\`.

No global torus spectral gap is claimed.

### 9.2 Endpoint absolute-mass gate

The 2026-09-17 primary regional report was rechecked. It uses the complete
endpoint spinors, before spectral projection,
\[
f=s_Nb_N\chi,\qquad w=h_BM_Br,
\]
with
\[
b_N=O(N^{-3/2}),\quad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),\quad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

Accounting for tangential area \(O(N(1+j))\) at normal depth \(j\) and the
exponentially summable tilted normal weight gives
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]

Therefore:
\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

This is a full-spinor absolute bound, not a cancellation or dominant-projection
bound.

**Scope at the 2026-09-24 freeze:** these are the inherited flat endpoint
estimates. Their transfer to the two-channel response and its reference
`U_N^N Phi_N` is not certified here; that trace belongs to T1–T2 in Sec. 9.6.

**Addendum 2026-09-25 — tilted ℓ² norms of the flat endpoints.**
[`flat-endpoint-l2-n3`](../reports/2026-09-25--flat-endpoint-l2-n3.md)
derives, directly from the exact TeX profiles and without the ℓ¹ masses above,
\(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), with explicit
constants, in the P-component of the norm used by Schur (8). Status:
`FLAT_ENDPOINT_L2_N3_PASS — PRELIMINARY`. It was reviewed in one sanedrín
round, `PASS_WITH_REPAIRS`, with the repairs applied; DeepSeek is the only
reviewer outside the author's family. Scope: inherited flat endpoints only.
Nothing is transferred to the two-channel contract or to `r_c`. The count
`N^-3 · N^-1 · N^-3` is not installed in any signed piece, and its margin
against the known `e^{-K_*N}N^{-7}` remainder of the flat leader is `N^0`.
**This is not `N^-7 PROVED`.**

### 9.3 Local-window insertion and leakage gates

Using the derivative selection rule and the endpoint bounds:
\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

The final complementary-bundle leakage is controlled by the full Bob norm.
The safe dominant correction is the zeroth-order \(Q\beta\mathcal P/N\) term,
giving
\[
|\Delta T_Q|=O(N^{-15/2}),
\]
not the earlier exploratory \(O(N^{-8})\) count. Hence:
\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

These are local-window statements only.

### 9.4 Remaining H1c gate

Literal pathwise H1b is not valid because a spatial path carries individual
hopping matrices \(D_h\), not the full symbol \(D(z)\). Thus:
\[
\texttt{H1c_GLOBAL = UNNECESSARY},
\qquad
\texttt{H1c_LOCALIZED = OPEN}.
\]

The unresolved localization statement recorded before the model freeze is:
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

Work on that asymptotic statement is **PAUSED** by the 2026-09-24 decision.
Sec. 9.6 supersedes the immediate route below with an exact observable gate.

A candidate momentum-space Dyson route has been formulated. Its key local
selection factor is
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)=O(|q|),
\]
and, for \(K_N(q)=N^3\widehat\vartheta(Nq)\),
\[
\int |q||K_N(q)|\,dq
=\frac1N\int |p||\widehat\vartheta(p)|\,dp.
\]
The working regularity assumption for this route is the Fourier-moment
condition
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|\,dp<\infty.
\]

The historical candidate \(n\)-insertion estimate was
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

**This estimate is not proved.** The missing step is uniform control of
non-normal variable-momentum products, including complementary-bundle visits,
transitions among the eight saddle neighborhoods, and regions where the local
Riesz splitting is unavailable. No momentum-conservation assumption may be
smuggled into that proof.

The [2026-09-24 Dyson precheck](../reports/2026-09-24--h1c-dyson-target-check.md)
also challenges this target when `n` counts raw insertions and the fixed
flat embedded endpoints are admitted. That precheck remains preliminary,
without independent review; this freeze does not promote it or transfer
its fixed-endpoint conclusion to the new physical response.

### 9.5 Locks

The H1 reopening does not change:
- \`E0 = OPEN_AT_STOP\`;
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`;
- \`E / AdS = STOPPED_UNPROVEN\`.

No localization or H1 promotion is authorized without proof and review.
The explicit operational model choice in Sec. 9.6 closes a contract only.

### 9.6 H1c-0 close / two-channel operational model — 2026-09-24

Direct user instruction freezes **TWO_DISTINGUISHABLE_CHANNELS** for this
candidate extension. The complete contract, prior diagnostic stages and
seven-report provenance are in the
[Schur audit and operational close, §§6–8](../reports/2026-09-24--h1c-return-kernel-schur-audit.md).

The one-particle space is `ell^2(Z^3) tensor C^2_channel tensor C^2_spin`.
The blocks of `D=S direct-sum S^-1` are assumed to be distinguishable
internal channels; `beta=sigma_x_channel tensor I_spin` exchanges them.
Bob's ability to resolve the channel is part of the new assumption. The
earlier repository did not derive this physical interpretation.

Prepare `Phi_N=(phi_N,0)` and evolve
`Psi_b=U_N^N mathcal U_M^(b) Phi_N=(psi_b^+,psi_b^-)`.
At encoding, `U_M direct-sum U_M` and `U_M direct-sum I` agree on this
preparation; they are not identified as physical operations on other states.
Bob uses `F_+=E direct-sum 0`, `F_-=0 direct-sum E` and
`F_empty=I_H-(E direct-sum E)`. The primary response is `(L_+,L_-)`,
where `L_±=<psi_1^±,E psi_1^±>-<psi_0^±,E psi_0^±>` and
`L_empty=-L_+-L_-`. `L_block=L_+` and `L_incl=L_++L_-` are only
coarse-grainings; signed responses are summed before absolute values.

For `vartheta=0`, `C_N=I` and `U_N^N(x,0)=(S^N x,0)`, so
`(L_+,L_-)=(L_flat,0)` and `L_incl=L_flat` exactly. This flat control
motivates the candidate; favorable asymptotics do not select its detector.
Channels may retain quantum coherence; the three-outcome POVM does not
reconstruct every coherence. Identification with a concrete physical
system remains OPEN. All future extension claims are conditional on this
contract, not universal claims about the original flat protocol. Neither
coarse-graining may later replace the primary observable for better powers.

```text
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

**Exploratory sequence executed by direct user instruction, 2026-09-24:**

1. **T1 — exact signed P/Q lift:** derivation and frozen five-piece
   vocabulary in
   [`two-channel T1 report`](../reports/2026-09-24--two-channel-t1-exact-signed-pq.md).
   Status: `PASS`, reviewed by Claude Opus and DeepSeek V4-Pro in the
   deliberative session
   [`T1 re-review`](../debates/2026-09-24--two-channel-t1-rereview.md).
   This is independent agent review across two model families, not human
   review. The pass is conditional on the explicit two-channel contract and
   a fixed admissible W. It does not certify estimates.
2. **T2 — trace of `O(N^-6)`:**
   [`T2 trace`](../reports/2026-09-24--two-channel-t2-trace.md) locates
   the old bound in the normalized auxiliary bilinear return correction.
   Status: `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`. It is a potential sub-contribution in the terminal-P linear slot
   `A_cP` for the earlier functional, conditional on matching its endpoint.
   No transfer to any of the ten current pieces is proved. The old
   `O(N^-6)` remains a coarse ceiling, not a signed term or coefficient.
3. **T3 — cancellation:** status `STOPPED_NO_SIGNED_TERM`. The frozen stop applies because T2 isolated no
   signed term or coefficient. No cancellation or symmetry search was
   performed; see [`T3 stop`](../reports/2026-09-24--two-channel-t3-stop.md).

These records do not prove H1c or H1, promote preliminary localization
prechecks, or alter C2/C3, E0, POWER_13/2_STABILITY, E/AdS, or the flat
manuscript. Physical realization of the two channels remains OPEN.
The next candidate question is whether bounds for all ten signed pieces
can be derived from the physical endpoints \((r_c,d_{c,P},d_{c,Q})\).
It was not executed or opened at that freeze. The later direct user
instruction and its narrowly scoped continuation are recorded in Sec. 9.7.

### Historical Schur / endpoint proposal — 2026-09-24 (superseded in part)

The following proposal is retained for provenance. Its claimed physical Bob
endpoint and resulting N^-7 estimates are not current accepted results: use
the subsequent Section 9.7 repairs and L2 stop addendum. The later Schur PASS
covers the stated stability norm only.

Direct user instruction: repair the bottleneck and continue, with an explicit
follow-up requiring a line-by-line check that both endpoints belong to the
current two-channel protocol. This authorizes the estimate audit and the
linear-piece reduction below; it does not assert a nonzero leading coefficient.

Status: **PROOF_WRITTEN / INDEPENDENT_REVIEW_PENDING**. The
[candidate proof and endpoint trace](../reports/2026-09-24--schur-stability-physical-transfer.md)
retains the exact T1 definitions and fixed W. It distinguishes bounded real
profiles (B) from the additional Fourier-moment hypothesis of Sec. 9.4 (F).
The latter is not implied by boundedness or merely C1 regularity.
Two external review executions timed out without a mathematical verdict;
the [execution record](../reports/2026-09-25--schur-physical-bridge-review-status.md)
records both failures. Neither is a pass, rejection or consensus. No review
process remains running.

The candidate establishes under B the full double Schur sum O_W(N^-1),
uniform stability of the normalized product, and the reconstruction norm
Theta(N^-1). Under F it proposes the stronger full propagator estimate
||T^N - R^N|| = O_W(N^-1), where R = D_xi/Lambda. The complete physical
Alice source s = Fourier H_xi J(U_M-I)phi_N and the actual Bob dual endpoint
v_c = V_c^* E B pi_c U_N^N J phi_N both have L2 norm O(N^-3).
The Bob estimate is derived from the real, inhomogeneous doubled evolution
in Fourier L1, not inherited from the flat reference.

Their product yields an absolute O_W(N^-7 exp(-K_*N)) linear error.
The signed continuation keeps the current reference r_+:

- A_+P = 2 Re <r_+, E S^N(U_M-I)phi_N> + O_W(N^-7 exp(-K_*N)).
- A_+Q, A_-P, A_-Q = O_W(N^-7 exp(-K_*N)).
- The sum of quadratic pieces in either channel is nonnegative and
  O_W(N^-8 exp(-2K_*N)); there are three such pieces per channel.

These are candidate estimates pending review. N^-7 is smaller than the
flat benchmark N^-13/2, but no lower bound for the current signed functional
is supplied. Its sign, coefficient and nonvanishing remain OPEN. This is
a proposed repair of the missing bridge, not a novelty claim, not transfer
of the flat Bob spinor, and not closure of H1/H1c, E0,
POWER_13/2_STABILITY or E/AdS. T3's earlier cancellation stop is not converted
into a cancellation result.
### 9.7 Physical reconstruction operator norms — 2026-09-24

The initial endpoint-transfer audit is recorded in
[`physical bound-transfer audit`](../reports/2026-09-24--two-channel-physical-bound-transfer-audit.md)
and its first STOP was superseded by the explicit Bob reconstruction norm
estimate in
[`reconstruction operator norms`](../reports/2026-09-24--two-channel-reconstruction-operator-norms.md).
The vector/piece bounds are PRELIMINARY (not expressly reviewed); they use
the L^2 stability `||t_N||_2` of the Schur block lemma, now repaired and
reviewed (below). The operator norm bound in (1)–(2)
of the report is direct from the defined Bob geometry and does not use
that lemma. For W fixed and `||vartheta||_inf <= Theta`,
`||E^{1/2} V_c P t_N||` and
`||E^{1/2} V_c Q t_N||` are `O_{W,Theta}(N^-1)` in both channels. Consequently
the ten physical pieces have the upper bounds in the linked report:
linear `O_{W,Theta}(N^-1 e^{-K_*N})`, quadratic `O_{W,Theta}(N^-2 e^{-2K_*N})`.
These are upper bounds only; no signed leading term, matching lower
bound, or dominance result is identified. The old `O(N^-6)` remains
untransferred.

Review: `debates/2026-09-24--two-channel-stability-review.md` (Opus +
DeepSeek, one round) gave `REPAIR_REQUIRED`. Critical premise:
`||A_j|| <= 1 + C/N` as a **norm** bound (not spectral radius) of the P
block, not yet repaired. Statements 1-3 PASS; 4 conditional on (a)-(d); 5
correct given 4. Bounds remain PRELIMINARY.

**Addendum 2026-09-25 — Schur block stability repaired.**
[`schur block stability repaired`](../reports/2026-09-25--schur-block-stability-repaired.md)
replaces the defective premise by identities on `ran P` (`A_j x = m x +
P(C^_N - I) m x`, `m = lambda/Lambda` scalar, `|m| <= 1`), mixed norms
`||.||_2` on P and `||.||_*` on Q, and an explicit E5 (uniform spectral
separation in `W` and `T^3 \ W`, resolvent by adjugate/determinant without
diagonalizability, Cauchy bound `||M^h|| <= C_0 rho_1^h`). Result: for each
fixed admissible W and `Theta < inf`, `sup_{0<=j<=N} ||t_j||_2 <=
(C_P + C_0 C_Q) e^{Theta (C_P + C_0 C_Q)} ||s||_2`, i.e.
`O_{W,Theta}(1)`, not `O_W(1)`; no uniformity in W. Status:
`SCHUR_STABILITY_PASS`, scope `||t_j||_2` only. Reviews (all sealed sanedrin
records in `debates/`): `2026-09-25--schur-repair-deepseek-review.md` (ABNER
`PASS_WITH_REPAIRS`, E5 then unwritten), `2026-09-25--schur-repair-astra-review.md`
(Astra GPT, Ciro Grok, `PASS_WITH_REPAIRS`, E5 executed),
`2026-09-25--schur-e5-abner-check.md` (ABNER DeepSeek `PASS`; its E5 objection
closed; the repairs it listed applied in the note). Opus takes part in two
records but does not count as independent. Not covered: Schur (7)-(8),
`||M_N|| = O_W(N^-1)`, the ten physical pieces, H1/H1c, W-uniformity,
interfaces with `W^c` in physical pieces. The Dyson route proposed by Opus
is unused and unreproduced. Not a numerical check beyond one fibre (T1 (18)).

**Addendum 2026-09-25 — physical transfer of the flat endpoints to `A_{cP}`, `A_{cQ}`.**
[`physical linear endpoint transfer gate`](../reports/2026-09-25--physical-linear-endpoint-transfer-gate.md).
Status: `ENDPOINT_TRANSFER_PARTIAL — PRELIMINARY`.
`INDEPENDENT_REVIEW: PASS_WITH_REPAIRS; repaired version not re-reviewed.`
Stable conclusions, with dependence on `(W, Theta)` in every power:
- **Alice transfers `O(N^-3)`:** exact `f^{T1} = J[c_N b_N down + eps_M s_N b_N chi_M]`
  (`|eps_M| = 1`), `||s||_2 = ||f^{T1}||_{l2_tilt}` by Parseval, remainder
  `O(N^-5)`; with the linearity of the Schur PASS, `||t_j||_2 = O_{W,Theta}(N^-3)`.
  The `N^-3` power inherits the `PRELIMINARY` status of the flat-endpoint note.
- **Bob: no `O(N^-3)` is proved for `vartheta != 0`.** Exact representation
  `<r_c, E V_c z> = <F w~_c, pi_c z>` with `w_c^fis = E r_c` and `w~_c` its tilted
  version; for `vartheta = 0`, `w_+^fis = w_N`, `w_-^fis = 0`. Available bound
  `||E V_c|| <= C_B N^-2`, `C_B = 256/(3 e^2 t_*^2)`; `||E delta r|| <= C_B Theta N^-2`.
  The inverse-Duhamel route gives only `N^-3/2` on that term, worse than
  `C_B Theta N^-2`; improving it needs uniform band conservation of `U_N^k J phi_N`
  (`H1c_LOCALIZATION`, OPEN).
- **`A_{+P}` at `vartheta = 0` contains the flat leader**, so the literal target
  "each linear term subdominant to `N^-13/2 e^{-K_* N}`" is unattainable for it;
  `A_{+Q} = O(rho_1^N e^{-K_* N})` and `A_{-P} = A_{-Q} = 0` there.
- Upper bounds only: `A_{cP} = O_{W,Theta}(N^-5 e^{-K_* N})`,
  `A_{cQ} = O_{W,Theta}(N^-6 e^{-K_* N})` (`N^-5` with the Schur PASS alone; the
  extra `N^-1` uses sums of the class L3). They do not prove subdominance.
- **Remaining gaps:** L1 (layer control of `r_c` for a non-translation-invariant coin,
  constants `C(W,Theta)`), L2 (the `vartheta`-dependent remainder of the terminal-P
  `stay` term, `o(N^-13/2 e^{-K_* N})`, both endpoints varying), L3 (independent review
  of the Schur (7)-(8)-type sums, including `sum_k G_Q(N,k+1) C_k x_k`).
Reviews (sealed sanedrin records in `debates/`): `2026-09-25--physical-transfer-astra-review.md`
(Astra GPT `REPAIR_REQUIRED`, Ciro Grok `PASS_WITH_REPAIRS`; Astra's residue and
verdict turns failed by `QUOTA`, so Astra did not confirm the repaired version);
`2026-09-25--physical-transfer-abner-review.md` (ABNER DeepSeek and Opus,
`PASS_WITH_REPAIRS` on the repaired version; the repairs were applied afterwards and
not re-reviewed; Opus does not count as independent). No substantive step of the
derivation was refuted. **No conclusion on signal survival, dominance or a signed
leading term; `N^-3 . N^-1 . N^-3 = N^-7` is not a theorem.** Which of L1/L2/L3
to attack first is not decided here. H1/H1c, the manuscript and the observable are
unchanged.


**Addendum 2026-09-25 — L2 A/B/C stop gate.**
[`H1/L2 A-B-C stop gate`](../reports/2026-09-25--h1-l2-abc-stop-gate.md).
Status: `L2_GATE = B / OPEN_BLOCKED_METHOD`;
`EVIDENCE = PRELIMINARY_DECISION_AUDIT / PARTIAL_EXTERNAL_REVIEW + SOURCE_BOUNDS_REPRODUCED`.
The object is the `vartheta`-dependent physical `stay` sub-remainder inside
the terminal-P contribution, not the full terminal-P output and not full
`A_{+P}`. T1 (14) gives `x_N=x^stay+f_{Q,N}+(M_Nx)_N`; the latter two
terminal-P pieces are separate L3 material. The exact `stay` subtraction
varies both endpoints. Available
bounds leave the two displayed pieces at
`O_{W,Theta}(N^-5 e^{-K_*N})` and
`O_{W,Theta}(N^-6 e^{-K_*N})`, above the flat leader scale
`N^-13/2 e^{-K_*N}`. The existing local-window and fixed-endpoint
homogeneous Dyson estimates do not transfer that control to the physical
inhomogeneous remainder. Under the precommitted stop rule this is outcome B. The report does not
claim that `H1c_LOCALIZATION`-class Gaussian-localization/phase transport is
the only route to A.
**Structural character of B.** B is structural for the present norm-based
method: the same norm estimates already bound the flat leading `stay`
contribution only at `O(N^-6 e^{-K_*N})`, missing the `N^-13/2` scale. Thus B
diagnoses a limitation of the method, not evidence against H1.
**Review 2026-09-26 (Claude, external to the author's family):** both bounds
reproduced from their sources, B validated; H1 not reviewed or closed (report
§8). By user decision H1 stays OPEN and work on it is paused; neither
`H1c_LOCALIZATION` nor any other route is opened. B is a method
obstruction, **not** a refutation: H1 remains OPEN; no admissible
counterexample/lower bound (C), signal-survival or dominance claim is made.
No `PP[vartheta]/PP[0]` sweep was run. L1 and L3 are not opened as rescue
routes. The closed flat result is unchanged.

## 10. IR spectral-attribution audit — 2026-09-22

User-authorized exploratory audit and commit/push, documented in the
[full report](../reports/2026-09-22--ir-spectral-attribution-audit.md).
Status: **SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC**.
For the fixed sigma2/I pair, N=24 and N=40 pass the stated empirical precision
criterion. Lpp and R=L-Lpp nearly cancel. At N=40, direct nonperiodic
position evolution agrees with the tilted FFT: field discrepancy normalized
by maximum amplitude 1.62e-15; signal relative discrepancy 5.07e-16.
No asymptotic trend, exclusively UV origin, or rigorous numerical enclosure
is claimed. IR admissibility of operations does not by itself prove
predominance of the PP contribution at the exponentially small signal scale.
The stronger spectral attribution remains OPEN. The Sec. 8.20 flat theorem
retains its scope and status; its full proof is not re-certified here.
H1c, E0, POWER_13/2_STABILITY and E/AdS statuses of Sec. 9 are unchanged.
This records completed authorized diagnostics, not authorization for larger scans.

### 10.1 IR spectral-attribution front C1/C2/C3 — gate ledger (2026-09-22)

Explicit user decision on 2026-09-22 to record the certified C1 and C2a
verdicts here. Branch-local, like the rest of this file; `main` is unchanged.
Subsequent user acceptance on the same date promotes C2b after its independent
review and unblocks C2c as a structural-scope gate, without promoting C2c.
Contracts: [C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md),
[C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
[C2b](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
[C2c structural scope](../theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md).
The front is fixed to P=Pi'=1_{|p|<=N^-1/2} (hard cutoff), Q=I-P, and the
signed block observable
Lpp=tr(E S^N P Delta P S^-N). This observable is not the conditioned Lcond
of C3.

| Subgate | Status | Evidence |
| --- | --- | --- |
| C1 leakage | **PASS** | [derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md), [independent review](../reports/2026-09-22--c1-leakage-independent-review.md) |
| C2a transfer, sigma2/I | **PASS** | [derivation](../reports/2026-09-22--c2a-oscillatory-transfer.md), [independent review](../reports/2026-09-22--c2a-independent-review.md) |
| C2b block decomposition, sigma2/I | **PASS** | [candidate](../reports/2026-09-22--c2b-block-decomposition-candidate.md), [independent review](../reports/2026-09-22--c2b-independent-review.md); B4_PRIME_PASS separately |
| C2c structural scope | **PASS — C2C_PASS, scope frozen** | [repaired execution](../reports/2026-09-22--c2c-structural-scope.md), [repaired review criteria](../theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md), [independent review](../reports/2026-09-23--c2c-independent-review.md); 16 original pairs only |
| C3 conditioning | **PASS — C3_PROOF_WRITTEN_REVIEW_ACCEPTED, scope frozen** | [execution](../reports/2026-09-23--c3-conditioning-execution.md), [DeepSeek/Gemini independent review](../reports/2026-09-23--c3-deepseek-gemini-review.md), commit `191ca20`; four original encoders, `M_B=I` only |
| E/AdS | **FROZEN** (STOPPED_UNPROVEN, Sec. 9.5) | unchanged |

- **C1 result:** q_N = ||Q(U_M-I)phi_N||^2 = D N^-5/2 (1+O(N^-1/2)) with
  D = 1024 pi^2 Phi_0(1/4)^2/5 > 0, for all four encoders. It follows that
  ||Delta - P Delta P||_1 = 2 sqrt(D) N^-5/4 (1+O(N^-1/2)).
- **C2a result (sigma2/I):**
  Lpp = N^-3 [C0 + C1 cos(sqrt(N)/2)] + O(N^-13/4), with C0 > C1 > 0 proved
  analytically (no numerical input). Hence Lpp = Theta(N^-3) and Lpp > 0 for
  all sufficiently large N.
- **Earlier consequence of C2a (arithmetic only):** R = L - Lpp = -Lpp + L
  exactly, and Thm 4.1 gives |L| <= 36 N^4 e^{-JN}. The complement of the PP
  block therefore cancels an algebraic Theta(N^-3) response. This establishes
  the cancellation's existence; it is not the proof of C2b below.
- **C2b result (sigma2/I):** direct block decomposition gives
  Lpp = +N^-3 A_N + O(N^-13/4), Lqq = +N^-3 A_N + O(N^-13/4), and
  Lpq + Lqp = -2 N^-3 A_N + O(N^-13/4), with the same
  A_N = C0 + C1 cos(sqrt(N)/2) >= C0-C1 > 0 as C2a.
  Thus the diagonal leaders are positive and the opposite leader lies in
  the coherences. Lqq >= 0 exactly; positivity of Lpp is asymptotic.
  B4_PRIME_PASS additionally gives Lpq = -N^-3 A_N + O(N^-13/4) and
  Lqp = -N^-3 A_N + O(N^-13/4); exactly, Lqp is the complex conjugate
  of Lpq, not necessarily equal to it at finite N.
- **Autonomous mechanism and bounds:** d_Q = d - d_P follows from Q=I-P
  and linearity. Thm 4.1 applies to the local source a, giving
  ||E^(1/2)(d_Q+d_P)|| <= 2 T_N. For every N>=2,
  |Lqq-Q_N| <= 8 T_N + 4 T_N^2 and
  |Lpq+Lqp+Lin_N+2 Q_N| <= 12 T_N, with T_N <= 9 N^4 exp(-JN).
  Here Q_N denotes the quadratic form <d_P,E d_P>, not the projector Q.
  C2a controls this quadratic form and Lin_N separately. No L-Lpp,
  Thm 4.4, total-signal asymptotics or N=24/40 data establish these blocks.

Caveats that must be retained with the C2a PASS:

1. The error term gains only N^-1/4 over the leading term.
2. The asymptotic regime is reached slowly: the oscillatory gains are powers
   of 1/(gamma sqrt(N)), where gamma = sqrt(3) - 3/2, which is about 1.1 at
   N=24 and 1.5 at N=40. The retained N=24/40 values do not validate or
   refute the sign.
3. The PASS is one independent **agent** review (Claude Opus 5). It is not
   an external human verification or a multi-member ratification.

C2b remains a `POST-DISCOVERY VERIFICATION GATE`: its discovery preceded
its contract. The independent review covers exactly snapshot
`19eb7a383cbb09464e91b64e89f724204e58cccb` and returns C2B_PASS and
B4_PRIME_PASS without required repairs. Review artifact SHA256:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.
The reviewer is recorded as **Codex, agent `/root`**, distinct from the
candidate's author, Claude Opus 5. This is one independent agent review,
not external human review, multi-member consensus or documented model
diversity. No additional Astra review has been recorded; such a review
remains an optional additional audit before publication, not a condition
retroactively imposed on this internal PASS.

C2c addressed **structural scope**, starting from the mechanism already
proved for sigma2/I: distinguish algebra and localized compensation from
pair-dependent leading coefficients, classify the sixteen original pairs,
and state the hypotheses and limits of any general hard-cutoff result.
The repaired execution makes the detector/espinor transfer explicit, retains
all band crossings, changes the grouping claim to **at most eight families**,
and restricts §9.2 to scalar indicator cuts with the stated open-set and
finite-support hypotheses. An independent review records
`C2C_PASS` for all five S3 levels on all sixteen original pairs, C1, and
§9.2 within that scope. The exponent `N^-3` remains a property of the frozen
`K=sqrt(N)` protocol, not a general QCA law; `N_0` and remainder constants
remain non-effective, and `NOVELTY=OPEN`.

C3 conditioning is now **C3_PROOF_WRITTEN_REVIEW_ACCEPTED** for the four
original encoders with `M_B=I`, the frozen hard cutoff and the same CJWW
protocol. The accepted result is
`Lcond-LPP = D p_infty N^-5/2 (1+o(1))`, with `D>0` and `p_infty>0`.
The result concerns the postselection increment. The leader and absolute
magnitude of `Lcond`, and comparison with the total signal `L`, remain outside
the C3 contract; no broader detector or QCA claim follows.

The C2c promotion is branch-local and does not alter the C3 result, E/AdS or FR1–FR3.
The repaired report and review retain their own commits and hashes; no
finite-N claim or broader detector/QCA class is added.

C3 is PASS in its frozen scope; E/AdS remains FROZEN. H1c, E0,
POWER_13/2_STABILITY and the Sec. 8.20 flat theorem are unchanged. No new
numerical calculation, scan, manuscript publication, commit or push follows
from this update.


## 11. Gravitational-normalization successor — 2026-09-29

**Authorization:** direct user instruction on 2026-09-29. This is a separately
chartered quantum-gravity successor, satisfying the scope rule in
`PROJECT_INSTRUCTIONS.md`.

**Contract:** [`GRAVITATIONAL_NORMALIZATION_GATE.md`](../theory/GRAVITATIONAL_NORMALIZATION_GATE.md),
frozen at commit `2680d799210731ab2815533e0b9ca9918f15d397`.

**Execution:** [G0 report](../reports/2026-09-29--gravitational-normalization-g0.md),
commit `f9f20746ccf44e62c440565455679eb4fd384a7d`.

Status:

```
GRAVITATIONAL_NORMALIZATION_GATE = BLOCKED_NO_DYNAMICAL_GEOMETRY
G0 = FAIL
G1 = NOT_EXECUTED
G2 = NOT_EXECUTED
G3 = NOT_EXECUTED
```

Reason: the frozen inhomogeneous operator
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=\exp[-i\vartheta(X)\beta/N],\qquad
A_N(X,z)=C_N(X)D(z)
\]
treats `vartheta(X)` as an externally specified profile. The frozen state
space contains no geometric degree of freedom that is evolved by the update,
and there is no matter-to-geometry backreaction rule. Therefore the stop rule
forbids assigning this model an Einstein-Hilbert normalization, Newton
constant or dynamically selected AdS radius.

This does **not** refute or reopen E/H1. E remains a propagation-stability
question on a prescribed inhomogeneous background and retains
`STOPPED_UNPROVEN`. A future successor would first need a separately
chartered dynamical-geometry model class: microscopic geometry degrees of
freedom, their local update and explicit backreaction. No such model is
constructed or authorized by this result.


## 12. Dynamical-geometry model-class successor — 2026-09-29

**Authorization:** direct user instruction to continue after the G0 stop.

**Contract:** [`DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md`](../theory/DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md),
frozen at commit `abfa341a30cd71ae2b6e130b387808a85f3b5a06`.

**Execution:** [model-class selection report](../reports/2026-09-29--dynamical-geometry-model-class.md),
commit `c08394e720e2c06bd91543a81aa2dbd4ac0b12c5`.

Status:

```
DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE =
VIABLE_MODEL_CLASS_IDENTIFIED / EXPLICIT_BRIDGE_NOT_CONSTRUCTED
```

Selected minimal successor class: bounded-degree Quantum Causal Graph
Dynamics-type kinematics with joint local matter/graph unitary gates and a
required fixed-background sector reproducing CJWW Eq. (5.15).

Evidence roles are separated:

- Arrighi--Martiel QCGD supplies discrete-time unitary causal graph dynamics
  and finite-depth localizability at the class level;
- Hamma et al. evolving-graph Bose--Hubbard supplies an explicit prior-art
  mechanism for bidirectional matter/graph coupling, but not in the CJWW
  discrete-time QCA;
- gauge-invariant CA/QCA constructions show that matter plus link variables
  can be coupled by reversible/local discrete dynamics, but gauge links are
  not reinterpreted as geometry.

The unresolved hard condition is M6: no explicit local gate set has yet been
constructed that has nontrivial graph backreaction while reducing **exactly**
to CJWW (5.15) on a regular fixed-background sector.

No edge-flip rule is invented in this gate. Construction or impossibility of
the explicit bridge requires a separate successor. The gravitational
normalization gate remains blocked until such a bridge passes its own G0
requirements.


## 13. Exact CJWW / dynamic-graph bridge no-go — 2026-09-29

**Contract:** [`EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md`](../theory/EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md),
frozen at commit `b8655ceefce70b3ec30df2372211a3565757df34`.

**Execution:** [no-go proof](../reports/2026-09-29--explicit-cjww-dynamic-graph-bridge.md),
commit `ef38144d2dec51819b91d84aeee8eb218e7aa86a`.

Status:

```
EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE =
STRONG_EXACT_BRIDGE_IMPOSSIBLE
```

For one fixed pure geometry background `|G0>`, assume the reduced matter
channel is exactly `U_CJWW rho U_CJWW^dag` for every matter state. The
joint output for every pure matter input must then factorize, and linearity
forces the geometry factor to be independent of the matter input. Therefore
the complementary geometry channel is constant and cannot encode
matter-dependent backreaction.

This obstruction is algebraic and precedes locality or QCGD gate synthesis.
It does not rule out dynamical-geometry QCA. It rules out only the strong
combination of exact CJWW reduced dynamics for every matter input and
simultaneous information-bearing backreaction on the same fixed pure
background.

The conservative escape route is W1: exact CJWW at zero backreaction coupling
and controlled matter-channel corrections at nonzero coupling. W1 is not
opened or constructed by this record.


## 14. W1 perturbative link-backreaction bridge — 2026-09-29

**Contract:** [`W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md`](../theory/W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md),
frozen at commit `2631e31369a9598da044d00e37cbb54d7100cab6`.

**Execution:** [W1 report](../reports/2026-09-29--w1-perturbative-backreaction-bridge.md),
commit `c3ff835e0ee5a72c9e64f3557820a55cad8fde40`.

Status:

```
W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE =
W1_CAUSAL_UNITARY_BRIDGE_PASS / FULL_QCGD_SYNTHESIS_OPEN
GEOMETRIC_INTERPRETATION = OPEN
GRAVITATIONAL_NORMALIZATION_G0 = NOT_REOPENED
```

Construction: one qubit on each undirected edge of the fourteen-jump CJWW
support graph, with local endpoint projector
`A_e = (|x><x|+|y><y|) tensor I_2` and edge gate
`V_e(g)=exp[-ig(Z_e+X_e) tensor A_e]`.

The seven undirected displacement classes all have a representative with
first coordinate +1. Splitting each class by the parity of the starting
`x_1` gives fourteen matching layers, so the added interaction is
finite-depth and bounded-range.

On the regular product background all edge qubits are `|0>`.
Matter changes each edge state at first order according to its endpoint
occupation. Conversely, changing one edge background from `|0>` to
`|1>` changes the first-order matter generator by `2 A_e`.

Because every site is incident to exactly fourteen support edges,
`sum_e A_e = 14 I` on the one-particle matter Hilbert space. Therefore the
regular-background first-order reduced matter correction is only a global
phase and vanishes on density matrices. The first nonzero correction is

\[
\Phi_g(\rho)=U_0\rho U_0^\dagger+
g^2\sum_e\left(A_e\sigma A_e-\frac12\{A_e,\sigma\}\right)+O(g^3),
\quad \sigma=U_0\rho U_0^\dagger.
\]

Thus link backreaction is `O(g)` while regular-background matter disturbance
begins at `O(g^2)`, consistent with the exact-bridge no-go.

This is **not yet dynamical geometry**: the edge qubit has not been proved to
change adjacency, causal distance or a metric observable. The G0
gravitational-normalization block therefore remains in force. A separately
chartered geometricity test would be required before G0 can be reconsidered.


## 15. W1 operational geometricity — 2026-09-29

**Contract:** [`W1_GEOMETRICITY_GATE.md`](../theory/W1_GEOMETRICITY_GATE.md),
frozen at commit `4c2abd64628f0f9d23e8c7d6371f8d790a4fc86f`.

**Exact certificate:** [`verify_w1_geometricity.py`](../scripts/verify_w1_geometricity.py),
added at commit `4a745f2878c8d973dfe8c627f1bf1131da376b3e`.

**Execution:** [W1 geometricity report](../reports/2026-09-29--w1-geometricity.md),
commit `bf8935c54ff71d837a1e50e15dfdf6fc4215db22`.

Status:

```
W1_GEOMETRICITY_GATE = W1_OPERATIONAL_GEOMETRY_PASS
SCOPE = FINITE_TIME_EXACT_SUPPORT_ONLY
ONE_STEP_ADJACENCY = UNCHANGED
OUTER_CAUSAL_BODY = UNCHANGED
METRIC / EINSTEIN INTERPRETATION = NOT ESTABLISHED
```

Exact witness: flat CJWW has eight nonzero two-step path contributions from
0 to `(0,0,1)` whose matrix sum vanishes exactly. On the product
`|0>_e` link background, the first derivative in `g` has a nonzero
component tied uniquely to the edge
`{(1,1,1),(2,1,1)}`, lifting that zero. On the product eigenstate of
`Z+X` with eigenvalue `+sqrt(2)`, every site sees the same fourteen-edge
phase and the exact CJWW cancellation is preserved. Hence the link-register
state changes exact finite-time matter support.

The pass is deliberately narrow. The elementary fourteen-jump neighborhood,
the graph distance generated by those jumps and the outer cube
`[-1,1]^3` are unchanged. The effect may be understood as
path/interference-sensitive operational geometry; it is not yet a derived
metric, tetrad, curvature or Einstein dynamics.

For the W1 successor model, the specific old G0 obstruction
`NO_DYNAMICAL_GEOMETRY` is no longer the right description: W1 has an
evolving link register, reciprocal matter/link coupling and an operational
support witness. Nevertheless G1 is **not** opened here because no coarse
metric/curvature observable has yet been derived.


## 16. W1 coarse-metric test — 2026-09-29

**Contract:** [`W1_COARSE_METRIC_GATE.md`](../theory/W1_COARSE_METRIC_GATE.md),
frozen at commit `a0a769b35b1c4e8e57241713a6cbd423038fb507`.

**Execution:** [coarse-metric report](../reports/2026-09-29--w1-coarse-metric.md),
commit `d1a93bab9e1922c1cc8243976479d90d32c8ed84`.

Status:

```
W1_COARSE_METRIC_GATE =
W1_SCALAR_POTENTIAL_ONLY / NO_METRIC_DEFORMATION
```

For a separable link background, the first-order matter generator is
`sum_e b_e A_e = sum_x v(x)|x><x| tensor I_2`: a scalar on-site potential.
For link eigen-backgrounds this is exact,
`W_g(x,p)=exp[-ig v(x)] W_0(p)`, so the momentum derivative and local
group-velocity/characteristic cone are unchanged. Non-eigenstate backgrounds
produce the previously derived dephasing-type reduced correction and can lift
finite-time interference zeros, but that is not a principal-symbol/tetrad
deformation.

The W1 operational-geometricity PASS of Sec. 15 therefore remains valid only
at the finite-time exact-support level. It does not supply a coarse metric.
The gravitational-normalization programme remains blocked before G1 for this
coupling. A successor would have to couple geometry to the hopping/coin
matrices themselves so that a geometry-dependent
`sigma^a e_a^i(x) p_i` term appears. No such new coupling is constructed
here.


## 17. W2 transport / tetrad-like bridge — 2026-09-30

**Contract:** [`W2_TRANSPORT_TETRAD_BRIDGE_GATE.md`](../theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md),
frozen at commit `384c0032967fd1164206ca6bed7319db6a84e8e1`.

**Symbolic certificate:** [`verify_w2_transport_tetrad.py`](../scripts/verify_w2_transport_tetrad.py),
added at commit `6f81a52588cfbd63e76f2a93b666f7ad8119bf4f`.

**Execution:** [W2 report](../reports/2026-09-30--w2-transport-tetrad-bridge.md),
commit `57ebe0f0ccb5c65065a1232ddbe02e93f9bb8aaf`.

Status:

```
W2_TRANSPORT_TETRAD_BRIDGE_GATE =
W2_DYNAMIC_PRINCIPAL_SYMBOL_PASS / CURVATURE_OPEN
FULL_QCGD_SYNTHESIS = OPEN
EINSTEIN_DYNAMICS = NOT_CLAIMED
GRAVITATIONAL_NORMALIZATION_G1 = NOT_OPENED
```

W2 replaces the W1 endpoint-occupation coupling by Hermitian local current
operators on three linearly independent displacement families
`d1=(1,0,0)`, `d2=(1,1,0)`, `d3=(1,1,1)`. The local gate is
`exp[-ig (Z_e+X_e) tensor J_e^(a)]`, with
`J_e^(a)=i(|x+d_a><x|-|x><x+d_a|) tensor sigma_a`.
The added interaction is exactly unitary and admits six matching layers.

At `g=0` the matter walk is exactly CJWW (5.15). Matter current changes the
link state at first order, and the link expectation changes the matter
transport generator at first order.

For a translation-invariant semiclassical link background with family means
`b_a=<Z+X>`, the momentum-linear CJWW coefficient matrix changes from
`E0=diag(1,-1,1)` to

\[
E(g)=E_0-2g\,\mathrm{diag}(b_1,b_2,b_3)
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

The direction matrix has determinant one. In particular, with only `b1`
nonzero, the leading dispersion becomes
`omega^2=(1-2gb1)^2 p1^2+p2^2+p3^2+cdots`, so the local characteristic
cone changes at order `g`.

This crosses the W1 metric-level obstruction: the link variables now control
the Weyl principal symbol itself and can be called **tetrad-like dynamical
variables** within this narrow perturbative model.

No curvature tensor/action, local Lorentz/diffeomorphism structure,
Einstein equation, `G_eff`, AdS radius or absolute scale is derived.
Curvature/dynamics is the next open layer; gravitational normalization G1
remains unopened.


## 18. W2 tetrad-backreaction correction — 2026-09-30

**Audit contract:** [`W2_TETRAD_BACKREACTION_AUDIT.md`](../theory/W2_TETRAD_BACKREACTION_AUDIT.md),
frozen at commit `1fc383fd62607ab118f3d6305c8e445ca10caab9`.

**Execution:** [audit report](../reports/2026-09-30--w2-tetrad-backreaction-audit.md),
commit `16ca6302ed4132f822df1cc48cf0ffaafb2788f5`.

Corrected state:

```
W2_PRINCIPAL_SYMBOL_CONTROL = PASS
W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL
```

Reason: W2 uses `H_e=B_e tensor J_e` with `B_e=Z_e+X_e`, while the
principal-symbol coefficient is `b_e=<B_e>`. Exactly
`[H_e,B_e tensor I]=0`, hence `<B_e>` is conserved for every joint state
and every coupling. The link density matrix can still change in components
orthogonal to `B_e`, but matter cannot change the variable that controls the
W2 tetrad deformation.

Therefore the phrase "dynamical tetrad-like variable" in the original W2
execution is superseded. W2 is a **link-controlled principal-symbol
deformation**, not yet a backreacting tetrad. A repair must use noncommuting
geometry operators so that matter can change the next-step transport control.


## 18. W2 tetrad-backreaction correction — 2026-09-30

**Audit contract:** [`W2_TETRAD_BACKREACTION_AUDIT.md`](../theory/W2_TETRAD_BACKREACTION_AUDIT.md),
frozen at commit `1fc383fd62607ab118f3d6305c8e445ca10caab9`.

**Execution:** [audit report](../reports/2026-09-30--w2-tetrad-backreaction-audit.md),
commit `16ca6302ed4132f822df1cc48cf0ffaafb2788f5`.

Corrected state:

```
W2_PRINCIPAL_SYMBOL_CONTROL = PASS
W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL
```

W2 uses `H_e=B_e tensor J_e` with `B_e=Z_e+X_e`, while the
principal-symbol coefficient is `b_e=<B_e>`. Exactly
`[H_e,B_e tensor I]=0`, hence `<B_e>` is conserved. The link density
matrix can change in components orthogonal to `B_e`, but matter cannot
change the variable that controls the W2 tetrad deformation.

## 19. W3 backreacting tetrad — 2026-09-30

**Contract:** [`W3_BACKREACTING_TETRAD_FLOQUET_GATE.md`](../theory/W3_BACKREACTING_TETRAD_FLOQUET_GATE.md),
frozen at commit `5dc5fda054355f1b1db3bbc7e6c91e8e841273f4`.

**Certificate:** [`verify_w3_backreacting_tetrad.py`](../scripts/verify_w3_backreacting_tetrad.py),
added at commit `f1f54c973f05e610c309e4f5f3925cb3fafce953`.

**Execution:** [W3 report](../reports/2026-09-30--w3-backreacting-tetrad.md),
commit `ebf9142880945ee243eef22acc5cf5f4554697b4`.

Status:

```
W3_BACKREACTING_TETRAD_FLOQUET_GATE =
W3_BACKREACTING_TETRAD_PASS / CURVATURE_DYNAMICS_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
FULL_QCGD_SYNTHESIS = OPEN
EINSTEIN_DYNAMICS = NOT_CLAIMED
GRAVITATIONAL_NORMALIZATION_G1 = NOT_OPENED
```

W3 separates roles on each link:
`R_e=exp[-ig Y_e tensor A_e]` gives a matter-dependent geometry kick, while
`T_e=exp[-ig Z_e tensor J_e]` makes `z_e=<Z_e>` control the current/hopping
term and hence the Weyl principal symbol.

For an initially uncorrelated edge/matter state,

\[
z_e' =
z_e+a_e[(\cos2g-1)z_e-\sin2g\,x_e],
\]

so

\[
z_e'-z_e=-2g\,x_e a_e+O(g^2).
\]

The transport tetrad is
`E(z)=E0-2g diag(z_1,z_2,z_3)D+O(g^2)`, hence the matter-dependent
backreaction on the principal symbol is

\[
\delta E_{\rm back}
=
4g^2\operatorname{diag}(x_1a_1,x_2a_2,x_3a_3)D+O(g^3).
\]

Thus the same microscopic variable `z_e` that controls the local
characteristic cone is changed by matter. This is the first project gate to
supply an explicit backreacting tetrad-like microscopic variable.

The source is endpoint occupation rather than a derived stress tensor, and no
coarse curvature, Einstein equation, gauge symmetry, `G_eff`, AdS scale or
absolute scale is established. Curvature/dynamics is the next open layer.


## 20. W3 coarse metric and curvature-dynamics audit — 2026-09-30

**Contract:** [`W3_CURVATURE_DYNAMICS_GATE.md`](../theory/W3_CURVATURE_DYNAMICS_GATE.md),
frozen at commit `3373869966836e0e219a80e54ce9ff208e99ad76`.

**Execution:** [curvature-dynamics report](../reports/2026-09-30--w3-curvature-dynamics.md),
commit `600122063633ca0f99e452e1e7439c8ecc93e70d`.

Status:

```
W3_CURVATURE_DYNAMICS_GATE =
COARSE_METRIC_KINEMATICS_PASS / CURVATURE_DYNAMICS_FAIL
C1 = PASS
C2 = PASS
C3 = FAIL
C4 = FAIL
```

The W3 principal symbol defines the coarse spatial metric
`h^{ij}=sum_a E_a^i E_a^j`. To first order,

\[
h^{ij}
=
\delta^{ij}
-2g
\begin{pmatrix}
2z_1&-z_2&z_3\\
-z_2&-2z_2&z_3\\
z_3&z_3&2z_3
\end{pmatrix}
+O(g^2).
\]

Spatial textures of `z_a(x)` can therefore carry nonzero kinematic
curvature; e.g. `z_1=f(x_2)`, `z_2=z_3=0` gives the linearized spatial
scalar curvature `R^(1)=-4g f''(x_2)`.

However, every W3 geometry-changing generator is multiplied by a matter
operator. There is no geometry-only neighbor/plaquette/stiffness term, so
geometric perturbations have no autonomous vacuum propagation law in the
declared model. The source `a_e=<A_e>` is endpoint occupation and has not
been derived as continuum stress-energy. Hence curvature kinematics passes,
but gravity-like curvature dynamics does not.


## 21. W4 autonomous geometry dynamics — 2026-09-30

**Contract:** [`W4_GEOMETRY_STIFFNESS_GATE.md`](../theory/W4_GEOMETRY_STIFFNESS_GATE.md),
frozen at commit `d4bcadf9e41ead03d3004607a48d46c1db5e6291`.

**Certificate:** [`verify_w4_geometry_stiffness.py`](../scripts/verify_w4_geometry_stiffness.py),
added at commit `3099bd5d06ea4395292489889f7324f79f48d405`.

**Execution:** [W4 report](../reports/2026-09-30--w4-geometry-stiffness.md),
commit `6b7c29643d26ac75b5d43ce0cd6bb95c0b5dc5d4`.

Status:

```
W4_GEOMETRY_STIFFNESS_GATE =
W4_AUTONOMOUS_GEOMETRY_DYNAMICS_PASS / GRAVITATIONAL_SOURCE_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

W4 adds a geometry-only exchange brickwork
`K_ef(kappa)=exp[-i kappa(I-SWAP_ef)]` between neighboring parallel link
registers. The homogeneous W3 geometry product state is exactly fixed because
every identical pair is symmetric under SWAP. A local defect in the
tetrad-control observable `z_e=<Z_e>` spreads autonomously in vacuum; for
`|1,0>`, the pair evolves to
`cos(kappa)|1,0>+i sin(kappa)|0,1>` up to a global phase.

Because W3 already maps spatial `z_a(x)` textures to the coarse metric and
linearized curvature, W4 makes that coarse curvature information evolve under
a geometry-only local unitary. This repairs the specific W3 C3 obstruction.

The W3 source obstruction remains: endpoint occupation has not been derived
as stress-energy. No Einstein equation, spin-2 mode, gauge symmetry,
Einstein-Hilbert action, `G_eff`, AdS scale or absolute scale is established.


## 22. W5 tetrad-conjugate source — 2026-09-30

**Contract:** [`W5_TETRAD_CONJUGATE_SOURCE_GATE.md`](../theory/W5_TETRAD_CONJUGATE_SOURCE_GATE.md),
frozen at commit `5a1e51286804c60f26aee8ccb3d07b4d1f8859f7`.

**Certificate:** [`verify_w5_tetrad_source.py`](../scripts/verify_w5_tetrad_source.py),
added at commit `bd91e1ae0ffd4e006b83b8ff7816cbaf6fcb5db9`.

**Execution:** [W5 report](../reports/2026-09-30--w5-tetrad-conjugate-source.md),
commit `d6fd2109a0960da3049063a6a2af99aa05141d7f`.

Status:

```
W5_TETRAD_CONJUGATE_SOURCE_GATE =
W5_TETRAD_CONJUGATE_SOURCE_PASS / STRESS_ENERGY_CONSERVATION_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

W5 replaces the W3 endpoint-occupation source with the same local current
operator `J_e^(a)` that is variationally conjugate to the tetrad-control
variable in the matter transport Hamiltonian. The repaired geometry kick is
`R_e^T(eta)=exp[-i eta Y_e tensor J_e]`.

Exactly,

\[
z_e'
=
z_e[1+(\cos2\eta-1)a_e]
-
x_e\sin2\eta\,j_e,
\]

so the leading source is
`z_e'-z_e=-2 eta x_e <J_e>+O(eta^2)`.

The current family has symbol
`J_a(p)=2 sin(p.d_a) sigma_a
=2 d_a^i p_i sigma_a+O(|p|^3)`, which is the directional lattice
representative of the operator obtained by varying the Weyl Hamiltonian with
respect to the spatial tetrad coefficient.

This justifies the narrow label **tetrad-conjugate stress source**. It does
not yet justify identifying `J_e` with the full conserved
`T_{mu nu}`: no discrete diffeomorphism/local-Lorentz Ward identity, full
spacetime tetrad, or local energy continuity law has been derived.


## 23. W5 spatial-tetrad completeness audit — 2026-09-30

The original three-field W3-W5 map has exact rank 3 in the nine-dimensional
spatial-tetrad tangent space and rank 3 in the six-dimensional spatial-metric
tangent space. No derived gauge symmetry justifies treating the missing
directions as redundant.

Contract: `d6dfad60a887036047fd2e4ded8d984df2b28844`.
Certificate: `322a6fe516f96398fc8cea401e125c7da22393ee`.
Report: `23672d2b2c4650180985a2c56d24532cf772182d`.

Status:

```
RESTRICTED_SPATIAL_METRIC_SUBMANIFOLD / GAUGE_COMPLETION_OPEN
```

## 24. W6 full spatial tetrad — 2026-09-30

**Contract:** [`W6_FULL_SPATIAL_TETRAD_GATE.md`](../theory/W6_FULL_SPATIAL_TETRAD_GATE.md),
frozen at commit `318fff219c1b84db3c3515699a3905a42626dbb6`.

**Certificate:** [`verify_w6_full_spatial_tetrad.py`](../scripts/verify_w6_full_spatial_tetrad.py),
added at commit `1137a14ec11d335895d356b87c7189de0cbcde00`.

**Execution:** [W6 report](../reports/2026-09-30--w6-full-spatial-tetrad.md),
commit `156e00fdabf1a00c1a5b491695f9a6d736b6b949`.

Status:

```
W6_FULL_SPATIAL_TETRAD_GATE =
W6_FULL_SPATIAL_TETRAD_PASS / SPACETIME_GAUGE_STRUCTURE_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

W6 replaces the three scalar controls by nine `z_{ar}`. With the invertible
direction matrix `D`, the map
`delta E=-2g Z D` has exact rank 9. The induced spatial metric map
`delta h=E0^T delta E + delta E^T E0` has exact rank 6. Its
three-dimensional kernel consists of infinitesimal internal frame rotations:
`delta E=Omega E0` with `Omega^T=-Omega`.

Each of the nine controls keeps the W5 tetrad-conjugate source and can inherit
the W4 geometry-only propagation. The spatial rank obstruction is therefore
repaired at the perturbative toy-model level.

Still absent: temporal tetrad/lapse/shift completion, a proved local frame
gauge symmetry, diffeomorphism constraints, full conserved stress-energy,
massless spin-2 mode and Einstein dynamics.


## 25. W4 long-wavelength spectrum audit — 2026-09-30

> Historical execution below. The October 26 full-spectrum audit above
> supersedes the physical reading of SMOOTH_MODE_GAPPED and the zone-edge
> zero: those statements use a rephased one-defect matrix. Current status is
> OPEN_AFTER_AUDIT, with corrected local checks and independent review pending.

**Contract:** [`W4_LONG_WAVELENGTH_SPECTRUM_GATE.md`](../theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md),
frozen at commit `89d53c15b15cc75948bbcaded26f1110127164e9`.

**Certificate:** [`verify_w4_long_wavelength_spectrum.py`](../scripts/verify_w4_long_wavelength_spectrum.py),
added at commit `6d22b365e71d619803425c4ca93b2d045abc8b42`.

**Execution:** [spectrum report](../reports/2026-09-30--w4-long-wavelength-spectrum.md),
commit `66e29d084c74b6e4643bf1d849f1b8098c8fff6a`.

Status:

```
W4_LONG_WAVELENGTH_SPECTRUM_GATE =
W4_REPAIR_AVAILABLE_SMOOTH_GAPLESS
DECLARED_W4 = SMOOTH_MODE_GAPPED / STAGGERED_GAPLESS_ONLY
```

For the original same-sign two-layer partial-SWAP brickwork,
`cos omega = cos^2(kappa)-sin^2(kappa) cos k`; the smooth point `k=0`
is generically gapped and the linear node lies at `k=pi`.
Using the inverse angle on the second matching instead gives
`cos omega = cos^2(kappa)+sin^2(kappa) cos k`, hence
`omega=|sin(kappa)||k|+O(|k|^3)` near `k=0`.
This is only a 1D repair witness; 3D isotropic tensor propagation remains open.


## 26. W7 spin-2 kinematics — 2026-09-30

**Contract:** [`W7_SPIN2_KINEMATICS_GATE.md`](../theory/W7_SPIN2_KINEMATICS_GATE.md),
frozen at commit `57361ab6f27fb6c08cf38466dfa42906ca296f40`.

**Certificate:** [`verify_w7_spin2_kinematics.py`](../scripts/verify_w7_spin2_kinematics.py),
added at commit `34d7a5af510ee363fabf4716cf6dc5807bc067fb`.

**Execution:** [W7 report](../reports/2026-09-30--w7-spin2-kinematics.md),
commit `0c68dcb93e0399df526bd9d55a277e0a4e023cc5`.

Status:

```
W7_SPIN2_KINEMATICS_GATE =
SPIN2_KINEMATIC_SECTOR_PASS / TT_GAUGE_CONSTRAINTS_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

Writing `A=E0^T delta E`, the nine spatial tetrad perturbations decompose
exactly into antisymmetric frame directions (3), one trace scalar and a
five-dimensional symmetric-traceless tensor `Q`. The metric sees only
trace + `Q`, and the five-dimensional `Q` space is the standard global
SO(3) spin-2 representation.

Componentwise identical linear geometry propagation preserves these sectors.
However no local diffeomorphism/constraint structure has been derived to
impose transversality or eliminate the scalar mode, and no 3D isotropic
smooth-gapless tensor dispersion has been established. The physical
two-polarization graviton is therefore still OPEN.


## 27. W8 TT gauge-completion audit — 2026-09-30

**Contract:** [`W8_TT_GAUGE_COMPLETION_GATE.md`](../theory/W8_TT_GAUGE_COMPLETION_GATE.md),
frozen at commit `223d9f41665efb0e3dd6684403eeeac3109e54d1`.

**Certificate:** [`verify_w8_tt_gauge_reduction.py`](../scripts/verify_w8_tt_gauge_reduction.py),
added at commit `7be4a0a341156e371f9f6cae505b931a6373c0f1`.

**Execution:** [W8 report](../reports/2026-09-30--w8-tt-gauge-completion.md),
commit `5612284befab40ff1d664d02e0702aa88b834e86`.

Status:

```
W8_TT_GAUGE_COMPLETION_GATE =
TT_GAUGE_REDUCTION_KINEMATIC_PASS / MICROSCOPIC_GAUGE_EMBEDDING_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

For nonzero momentum, the traceless-projected vector transformation
`delta Q_ij = partial_i xi_j + partial_j xi_i
-(2/3)delta_ij partial.k xi` has rank 3 inside the five-dimensional
symmetric-traceless tensor space. For `k || z`, one can set
`Q_xz=Q_yz=Q_zz=0`, leaving exactly
`Q_xx=-Q_yy` and `Q_xy`: the plus/cross pair.

This establishes only the kinematic gauge reduction. W6 does not contain an
exact local generator/Gauss constraint identifying gauge-related tensor
configurations; such configurations generally give different matter
principal symbols. The physical graviton therefore remains OPEN.


## 28. W8 prior-art correction — 2026-09-30

Gu-Wen already establish local qubit/spin models with emergent low-energy
linearized diffeomorphism gauge structure and helicity +/-2 modes. Pretko
rank-2 tensor gauge theories already contain vector Gauss laws and, in the
traceless vector-charge case, a two-polarization gauge sector. Therefore W7/W8
mode counting is not a novelty claim.

The W8 requirement is also corrected methodologically: an emergence programme
need not realize the target diffeomorphism gauge symmetry exactly at the
microscopic lattice level. A controlled low-energy constraint subspace and
effective Ward identity can suffice.

Report commit: `44bc411ab72b121302c42cfe8a0afc5fd4613c01`.

## 29. W9 CJWW / graviton-matter bridge — 2026-09-30

> Historical record, superseded by the authoritative repair update above
> and W9 report §9. Current W9: **OPEN_AFTER_AUDIT**.

**Contract:** [`W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md`](../theory/W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md),
frozen at commit `4a40c12c83801d5bdfdd7fc1c3638bb6308005e0`.

**Certificate:** [`verify_w9_continuum_gauge_bridge.py`](../scripts/verify_w9_continuum_gauge_bridge.py),
added at commit `5abd53673cef98c2ec0f0349db70f57fad869939`.

**Execution:** [W9 report](../reports/2026-09-30--w9-cjww-graviton-matter-bridge.md),
commit `8a8b2bf38e8bb7832153f5d8ce3bfaafb5130229`.

Status:

```
W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE =
CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS /
MICROSCOPIC_SPACETIME_COMPLETION_OPEN

B1 SPATIAL_ONLY = FAIL
B2 FULL_LINEARIZED_CONTINUUM = PASS
B3 W5/W6 SPATIAL_TETRAD_SOURCE = COMPATIBLE / PARTIAL
B4 MICROSCOPIC LAPSE_SHIFT_STRESS = OPEN
```

The spatial coupling `h_ij T^ij` is not gauge complete because stress
conservation gives `partial_i T^ij = -partial_t T^0j` rather than zero.
Adding `h_00 T^00 + 2 h_0i T^0i` restores the full linearized coupling
`h_mu_nu T^mu_nu/2`, whose gauge variation vanishes on
`partial_mu T^mu_nu=0`.

Thus the W5/W6 spatial source is compatible with the spatial part of the
continuum Weyl stress coupling, but the microscopic QCA still lacks
lapse/shift constraint variables and a proved full local lattice
stress-energy object.


## 30. W10 sourced Gu-Wen constraints — 2026-09-30

> Historical record, superseded by the authoritative repair update above
> and W10 report §9. Current W10: **OPEN_AFTER_AUDIT**.

**Contract:** [`W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md`](../theory/W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md),
frozen at commit `7109a3ae5d5c3aaf958cf473c0f6a0200413664d`.

**Execution:** [W10 report](../reports/2026-09-30--w10-sourced-gu-wen-constraints.md),
commit `f956f68b339d97ee207793d9402cb3cd9492f567`.

Status:

```
W10 =
CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS /
MICROSCOPIC_CJWW_CHARGES_OPEN
```

Gu-Wen already supply the vacuum scalar/vector constraint architecture,
including lapse/shift as Lagrange multipliers and a lattice energy-penalty
implementation. The project-specific continuum bridge sources those
constraints with Weyl `T^{00}` and `T^{0i}`; consistency follows from the
linearized Bianchi identity together with `partial_mu T^{mu nu}=0`.

The microscopic CJWW model still lacks proved local exact Floquet operators
for those charges.

## 31. W11 low-energy CJWW stress source — 2026-09-30

> Historical record, superseded by the authoritative repair update above
> and W11 report §9. Current W11: **OPEN_AFTER_AUDIT**; contract F3 remains open.

**Contract:** [`W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md`](../theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md),
frozen at commit `cfdc5c6059a169028b38fa326444286d9703e8e5`.

**Certificate:** [`verify_w11_ir_stress_source.py`](../scripts/verify_w11_ir_stress_source.py),
added at commit `97592a465e40a3769980bcd64623c2c3ac8da3c9`.

**Execution:** [W11 report](../reports/2026-09-30--w11-cjww-floquet-stress-tensor.md),
commit `83acdfd6031cdb14be6c6477d09d18cc172950a7`.

Status:

```
W11 =
LOW_ENERGY_LOCAL_STRESS_SURROGATE_PASS /
EXACT_FLOQUET_STRESS_OPEN
EVIDENCE = PRELIMINARY / INDEPENDENT_REVIEW_PENDING
```

Centered finite differences give a finite-range IR Hamiltonian with symbol
`-sigma^a E0_a^i sin p_i`, matching the branch-local CJWW Weyl generator to
first order. Local bond momentum densities likewise have symbol `sin p_i`
and reproduce `T^{0i}` in the narrow-band limit. Together with W5/W6 spatial
currents this supplies low-energy lattice representatives for all continuum
stress components needed by W10.

No canonical strictly local all-momentum Floquet stress tensor or exact
one-step local energy/momentum continuity law is claimed.


## 33. Orientation-independent Hermitian elastic successor — frozen 2026-09-30

**Contract:** [`ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md`](../theory/ELASTIC_HOPPING_HERMITIAN_RESPONSE_GATE.md),
frozen at commit `1cda245e20acc111a856fa4296f77359be714bd2`.

Status:

```
AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED
```

The successor removes the arbitrary half-support orientation that killed the
previous elastic-response attempt. It uses the full 14-hop weighted symbol

\[
R_u(p)=\sum_{h\in F}\rho_h(u)e^{ip\cdot h}W_h,
\qquad
\rho_h(u)=\frac{h^Tuh}{h^Th},
\]

and the Hermitian generator

\[
K_u(p)=\frac12(R_u(p)+R_u(p)^\dagger).
\]

The exact unitary response is frozen as
`W_{eps,u}(q)=exp[-i eps K_u(p)] W_0(p)`,
with the same common affine embedding and common physical coordinates used by
the predecessor elastic-graph gate.

No node/gauge decomposition, four-species metric comparison, metric-rank
calculation or coefficient adjustment has been performed after freezing.

**Execution result.** The exact symbolic first-order calculation was then
performed without changing the frozen prescription. At every decisive +I
node,

\[
K_u(p_*)=\frac{\operatorname{tr}u}{3}I.
\]

Thus there is no traceless constant term and no first-order node displacement;
only a common scalar quasienergy phase remains. After removing that phase, the
hopping-induced principal-frame correction vanishes exactly,

\[
\delta E_*^{\rm hop}=0.
\]

The common embedding still gives

\[
\delta h_*=2a^2u
\]

for all four species, with rank 6/6. Therefore the terminal state is

```
HERMITIAN_ELASTIC_METRIC_UNIVERSAL_EMBEDDING_ONLY
```

not a nontrivial elastic metric response. The stop rule applies: no alternate
ordering, coefficient, bond functional or internal rotation is tried here.
W3–W11 remain closed and W12 remains unchanged. Evidence is
`EXACT SYMBOLIC FIRST-ORDER DERIVATION / AUTHOR-SIDE CERTIFICATE /
INDEPENDENT REVIEW PENDING`.

Execution report: [2026-09-30 Hermitian elastic response](../reports/2026-09-30--elastic-hopping-hermitian-response.md),
commit `5de01a895582b61aa9baaee8b39006d6bdcf28a6`.
