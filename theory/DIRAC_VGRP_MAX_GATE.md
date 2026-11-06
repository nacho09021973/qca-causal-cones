# DIRAC_VGRP_MAX — massive group-velocity ceiling, standard Pavia Dirac family, d=3

**Status: DRAFT v3 (2026-11-06), not frozen.** Drafted by Claude Code (Claude Opus 5.5) at the
user's request ("Redacta el borrador del charter en `theory/` para la primera opción: el techo de
velocidad de grupo masivo en una familia concreta de d=3"). Nothing here is authorized for
execution. The charter is frozen only by an explicit user instruction, and that commit becomes
the preregistration commit. This draft records no computation, candidate or theorem.

Drafting history:
- **v1** proposed Stage A (exact) as the certificate and Stage B (floating-point sweep) as a
  diagnostic only. The user accepted this replacement of their original acceptance criterion
  (2026-11-06).
- **v2** records user decisions D1–D6 (Sec. 9). Branch `theory/massive-vgrp-bcc`, from `main`
  at `bce5599`.
- **v2 review.** Blind review by Grok (`grok-4.7`) of v2 at `5ebe10d`: do not freeze, seventeen
  objections G-V-01..17. The author accepted all of them
  ([report and author reading](../debates/2026-11-06--dirac-vgrp-max-charter-review-grok/verificacion_autor.md)).
- **v3** applies G-V-01..17. It fixes the Stage B tolerances (user approval «SI», 2026-11-06)
  and adds the line-abandonment criterion now required by `CLAUDE.md`. Each change is tagged
  `[G-V-NN]` or `[CLAUDE.md]`.

**Initial scientific status: OPEN.**

**Origin.** An AI-written memorandum pasted on 2026-11-06 claimed
`|v_g,max| = c_eff cos m` for "any isotropic massive QCA". The user classified it REJECTED.
The memorandum is **not** a source for this gate. Its formula appears only as hypothesis H1
(Sec. 3), because the one-dimensional analogue is easy to check (Sec. 4, control C0).

**Authority:** [CURRENT_STATE](../state/CURRENT_STATE.md):
- `V_grp^max := sup_{s,k} ||∇_k ω_s(k)||` is defined in Sec. 2 of
  [`THREE_VELOCITIES.md`](THREE_VELOCITIES.md). `V_grp^max` is OPEN in `d >= 2` (CURRENT_STATE,
  dispersion-corrections and L6b entries).
- Standard Weyl/Dirac exact gate: PASS
  (`reports/2026-09-14--weyl-dirac-gate-contract.md`, `scripts/verify_weyl_dirac_gate.py`).
- Exact finite-mass `B*` REJECTED IN STANDARD DIRAC FAMILY: for `0 < m < 1`, `M = arcsin m`,
  `F = M cot M`, `c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`.
- [`THREE_VELOCITIES.md`](THREE_VELOCITIES.md) Sec. 3.2: `C_micro`, `V_grp^max` and `c_IR` are
  never identified with one another.

**Relation to other drafts.** `theory/MASSIVE_RIGIDITY_GATE.md` (DRAFT v2, present only on
branch `research/inverse-gravity-design`, `99c20c6`) asks how `c_H` and `c_{ω^2}` depend on the
symbol across class M4. This gate asks a different question: the *global maximum* of the group
velocity for *one fixed family*. It does not touch `c_H`, `c_{ω^2}` or M4.

## 0. Pre-step check (rule of 2026-11-02)

- **Known.**
  - **Family.** Weyl matrices: eqs. (15)–(17) of arXiv:1601.04832v1, p.6. Dirac coupling:
    `D = [[n W, i m I], [i m I, n W^†]]`, eq. (9) of arXiv:1601.04842v1. Here `0 < m < 1` and
    `n = sqrt(1-m^2)`.
  - **Spectrum.** The phases are `±ω` with `ω = acos(n u)`. The scalar is
    `u = cos q_x cos q_y cos q_z + χ sin q_x sin q_y sin q_z`, `χ = ±1`
    (`scripts/verify_weyl_dirac_gate.py:66-68`).
  - **Units.** The physical wavevector is `k = sqrt(3) q`: each derivative carries a factor
    `1/sqrt(d)` (`scripts/verify_weyl_dirac_gate.py:133-134`). The hops lie in `N_3`, normalized
    to unit length. The verifier certifies `C_micro` as the cube with `r_in = 1/sqrt(3)` and
    maximum support `1`.
  - **Massless node.** At `m = 0` the linear slope of `ω` at the node equals `r_in`. This is
    not a group velocity: `ω` is not differentiable there [G-V-01].
- **Not known in this repo.** `V_grp^max` of this family for any `0 < m < 1`. Where it is
  attained. Whether it lies below, at or above `r_in`.
- **Literature (to do before execution, part of Stage 0).** The Pavia papers may already state
  the group velocity of the massive BCC automaton. Read `sources/1601.04832v1.pdf` and
  arXiv:1601.04842 (not yet in `sources/`) for any statement about `∇ω`, and record the pages
  read. `NOVELTY = OPEN`. Until that check is done, any prior-art status is `[UNVERIFIED]`. This
  covers the 1D formula and Bernstein-type bounds too [G-V-17].
- **Question.** See Sec. 1.
- **Results that end the gate.**
  - The exact value of `V_grp^max` at the declared masses, with its maximizer set, certified as
    in Sec. 4.
  - Or a stop under Sec. 5.
- **Results that abandon the line** [CLAUDE.md]. These are separate from the per-hypothesis
  verdicts of Sec. 7.
  - The Stage 0 literature check finds `V_grp^max` of this family already published exactly.
    The line is then prior art: the gate stops before Stage A with `STOPPED_PRIOR_ART`.
  - All five masses end `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`. The exact route for this family
    is then abandoned. Any continuation needs a new charter with a different method.

## 1. Single question

For the standard Pavia Dirac family in `d = 3` and each declared mass `m`, what is

`V_grp^max(m) := max_{k ∈ BZ} ||∇_k ω(k; m)||`,  `ω = acos(n u(k/sqrt(3)))`,

and where is the maximum attained?

The answer is compared exactly with `r_in(C_micro) = 1/sqrt(3)` and `V_causal^max = 1`.

`c_H` and `c_{ω^2}` are cited as context only. Their closed forms contain `arcsin` of a rational,
so no certified comparison with them is made [G-V-02, G-V-12, G-V-16]. The quantity named `c_IR`
is neither computed nor inferred here.

## 2. Declared class

| Item | Declaration |
| --- | --- |
| Symbols | The four Pavia Dirac symbols built from `A+, B+, A-, B-` (the four cases of `verify_weyl_dirac_gate.py`) |
| Internal dimension | 4 (two Weyl doublets coupled by the on-site mass term) |
| Substrate | BCC, `N_3 = {(±1,±1,±1)/sqrt(3)}`, plus on-site; one complete update per time step `Δt = 1` |
| Mass | Declared rational set `m ∈ {3/5, 4/5, 5/13, 12/13, 8/17}`, with `n` respectively `4/5, 3/5, 12/13, 5/13, 15/17` (decision D1). Rational `n` keeps every coefficient of Sec. 4 in `Q`. It does not by itself guarantee that Stage A finishes within budget; Sec. 5 governs that |
| Brillouin zone | The torus `T^3 = R^3/(2πZ)^3`. Points are classes `q mod 2π`, not representatives in a cube [G-V-03]. No symmetry reduction unless it is proved exactly in Stage 0 |
| Branch | Both phases `±ω`, each of multiplicity 2. Their gradients differ only in sign. Stage 0, step 2 verifies this [G-V-07] |
| Excluded | `m = 0` (ω is not differentiable at the node) and `m = 1` (support collapses to on-site, so ω is constant) |

## 3. Targets and preregistered hypotheses

**Targets.**
- T1. The exact value of `V_grp^max(m)` at each declared mass. Its square is an algebraic number,
  given by a minimal polynomial over `Q` and an isolating interval with rational endpoints.
- T2. The exact set of maximizers in `T^3`, reconstructed as orbits of representatives under the
  symmetries proved in Stage 0, step 5.
- T3. The exact signs of `V_grp^max(m)^2 − 1/3` (comparison with `r_in`) and
  `V_grp^max(m)^2 − 1` (comparison with `V_causal^max`) at each declared mass. Both are signs of
  algebraic numbers [G-V-12].

**Hypotheses**, frozen before any computation. They are tests, not predictions. No outcome is
favoured.
- **H1 (transplanted 1D formula).** `V_grp^max(m)^2 = n^2/3`, that is
  `V_grp^max = n · r_in` (in 1D, `n = cos(arcsin m)`).
- **H2 (strict ceiling).** `V_grp^max(m)^2 < 1/3` at every declared mass.
- **H3 (axis attainment).** Let `A := {q ∈ T^3 : at least two coordinates are ≡ 0 or π (mod 2π)}`.
  H3 states that at each declared mass at least one maximizer lies in `A` (existential, not
  universal) [G-V-14].

The rules that turn per-mass results into hypothesis verdicts are in Sec. 7 [G-V-13].

No hypothesis is a claim about "any isotropic massive QCA". A confirmation at five masses of one
family is recorded as exactly that.

## 4. Method, named before any computation

**Reduction (to be proved exactly in Stage 0, not assumed).** For `0 < m < 1`,
`|u| <= 1` and therefore `|n u| <= n < 1` on the whole torus. Then `1 − n^2 u^2 >= m^2 > 0`, so
`ω` is real-analytic there. Let

`Φ(q) := ||∇_k ω||^2 = (n^2/3) · G / (1 − n^2 u^2)`,  `G := ||∇_q u||^2`.

This `Φ` is the `d = 3` function only. The 1D control uses its own function `Φ₁` [G-V-09]. The
torus is compact and has no boundary. Therefore `V_grp^max(m)^2 = max Φ`, and the maximum is
attained at a critical point of `Φ`.

**Stage 0 — exact preliminaries** (SymPy, no floating point):
1. Check that `published_symbol` and the Dirac block reproduce the spectrum `cos ω = n u`. Reuse
   these helpers read-only from `verify_weyl_dirac_gate.py`. **That file's bytes are not
   changed.**
2. **Branches** [G-V-07]. Prove `D^2 − 2 n u D + I = 0` and `tr D = 4 n u`. Together with
   `sin ω >= m > 0`, these force the eigenvalues `e^{±iω}`, each of multiplicity 2, so the two
   branch gradients differ only in sign.
3. Prove `|u| <= 1`, hence `|n u| <= n < 1`, on the torus for each declared mass, and derive `Φ`
   symbolically.
4. **Control C0 (1D)** [G-V-09]. With `u₁ = cos q` and `Φ₁(q) := n^2 sin^2 q / (1 − n^2 cos^2 q)`
   (1D units, `k = q`), prove `max Φ₁ = n^2`, attained exactly at `q = ±π/2`. If C0 fails, the
   pipeline is wrong and the gate stops.
5. **Symmetries** [G-V-08]. Only signed permutations `S` of `(q_x, q_y, q_z)` are admitted. They
   are orthogonal in `k = sqrt(3) q`, because the scaling is isotropic. For each candidate, verify
   exactly that `Φ∘S = Φ` (not merely that `u` is invariant), or that `S` maps the `Φ` of one
   symbol case (choice of `χ`, transposition) onto the `Φ` of another. Only symmetries proved
   here may reduce later stages. The maximizer set is then reconstructed by orbits.
6. Record the literature check of Sec. 0. If it finds `V_grp^max` of this family already
   published exactly, stop with `STOPPED_PRIOR_ART` (Sec. 0).

**Stage A — exact global maximum** (primary; certifies T1–T3):
- **A1. Rational charts** [G-V-03]. On each circle factor, `t = tan(q/2)` is a diffeomorphism
  from the class of `(−π, π)` onto `R`, and `t' = cot(q/2)` is one from the class of `(0, 2π)`
  onto `R`. The class `q ≡ π` is the point `t' = 0`. The `2^3` chart combinations cover `T^3`.
  Fewer are used only if Stage 0, step 5 proves symmetries that identify them. Implementations
  never evaluate a chart at a representative where it diverges.
- **A2. Critical system.** Since `dt_i/dq_i != 0` in each chart, `∇_q Φ = 0` is equivalent to
  `∇_t Φ = 0`. With `D := 1 − n^2 u^2 > 0` this is
  `D ∂_i G + 2 n^2 u G ∂_i u = 0`, `i = 1, 2, 3`.
  Multiply only by the listed positive factors: powers of `(1 + t_i^2)` and of `(1 + t_i'^2)`.
  These are positive at real points and neither add nor remove real zeros [G-V-04]. The
  coefficients are in `Q` at each declared mass.
- **A3. Solving** [G-V-04, G-V-05].
  - Compute a Gröbner basis over `Q`, or eliminate with resultants. Every real zero obtained by
    elimination is checked exactly in the A2 system before any further use, or the ideal is
    saturated by the cleared factors. A zero that fails is discarded and recorded.
  - **Zero-dimensional ideal:** isolate every real solution exactly, in rational boxes.
  - **Positive-dimensional ideal:** `dΦ = 0` on the whole real critical locus, so `Φ` is
    constant on each connected component of that locus. The verifier must produce one exact
    sample point in each connected real component, with an exact certificate that the sample
    meets every component (for example, the critical points of a generic linear function
    restricted to the locus, or a cylindrical-decomposition sample). It then evaluates `Φ`
    there.
  - If the sampling certificate cannot be completed within budget, that mass stops with
    `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`. Searching for critical points of `Φ` again on the
    component is not a valid step.
- **A4. Comparison.** Evaluate `Φ` at every real critical point as an algebraic number. Determine
  the maximum by exact sign comparison of differences, and the maximizer set.
- **A5 (alternative certificate, if A3 does not finish)** [G-V-06].
  - Upper bound: for a rational `V^2`, a sum-of-squares certificate with rational coefficients
    for the trigonometric polynomial `V^2 (1 − n^2 u^2) − (n^2/3) G >= 0`. This is sufficient but
    not complete: some nonnegative trigonometric polynomials are not sums of squares, and no
    degree bound is promised.
  - Lower bound: an exact witness `q_*` with `Φ(q_*) = V^2`. The witness may only be a real zero
    certified in A3 (even if A3 did not finish), never a point from Stage B.
  - With both, `V_grp^max(m)^2 = V^2 ∈ Q` and the mass is `VGRP_MAX_CERTIFIED`. With only the
    upper bound, the mass is `CEILING_ONLY`. If `V_grp^max(m)^2` is algebraic but not rational,
    A5 can give only a ceiling.

**Stage B — numerical sweep of the Brillouin zone** (diagnostic only, `SUPPORTED`; the user's
acceptance criterion):
- **B1.** A uniform grid on the full torus (representatives `[-π, π)^3`), with no symmetry reduction and no
  assumption of isotropy or continuous spherical symmetry. Grid: `N = 256` points per axis
  (decision D2), for each declared mass and each of the four symbols. It runs only under the
  `--diagnostics` flag of the exact verifier (decision D4). Report the grid maximum of
  `Φ` and its location.
- **B2.** Local refinement (Newton or BFGS from the best 64 grid points). Report every distinct
  local maximum found.
- **B3. Agreement rule, fixed here before any computation** [G-V-10, G-V-11]. Stage B runs
  **after** Stage A, and only for masses that Stage A certified. Write `Φ*` for the certified
  maximum, converted to double precision from its isolating interval (refined to width below
  `1e-15`). Agreement means all three of:
  - (i) the grid maximum is at most `Φ* (1 + 1e-9)`;
  - (ii) the largest refined local maximum lies in `[Φ* (1 − 1e-9), Φ* (1 + 1e-9)]`. This is
    two-sided: it catches a certified maximum that is too low, and also an inflated or spurious
    one that the sweep cannot reproduce;
  - (iii) only when the A3 certificate is zero-dimensional: every refined local maximum lies
    within sup-norm distance `1e-6` in `q` (mod `2π`) of some exact critical point. When the
    certificate comes from positive-dimensional sampling or from A5, (iii) is not applied and
    only (i) and (ii) count.
  - **Role.** Disagreement is a veto: it stops the gate with
    `STOPPED_EXACT_NUMERIC_DISAGREEMENT`. Stage B never certifies a value, never decides a
    hypothesis and cannot rescue a stopped Stage A. A finite scan does not prove a global
    maximum (`CLAUDE.md`, hard rules).

## 5. Stop rules and budget

- **Budget** [G-V-15]. Stage 0, step 5 decides the number of symbol classes, which is at most
  four. Stage A gets 900 s of CPU per declared mass per symbol class, cumulative across runs.
  A5 gets 900 s per mass per class, once, in total. No other time is authorized.
- **Stop with `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`** if neither A3–A4 nor A5 finishes within
  budget for some mass. The masses that did finish are recorded as certified; the rest stay
  OPEN.
- **Stop with `STOPPED_CONTROL_FAILED`** if control C0 fails.
- **Stop with `STOPPED_EXACT_NUMERIC_DISAGREEMENT`** on any disagreement under Sec. 4, B3.
- **Stop with `STOPPED_PRIOR_ART`** under Sec. 0 (Stage 0, step 6).
- **No extensions without a new charter:** no extra masses, no symbolic-in-`n` result
  (decision D3), not the `s = 4` family of `S4_STRICT_CONE_COUNTEREXAMPLE.md` [G-V-15], no other
  substrates, no `d = 2`.

## 6. Exclusions

The following are not computed, claimed or inferred here:
- `c_IR`; and `c_H` or `c_{ω^2}`, which are cited as context without any certified comparison
  [G-V-16];
- signalling, evanescent precursors, saddle-point asymptotics;
- entanglement, the coin Bloch tensor, Wilson masses, fermion doublers;
- any other family or class, and any general QCA law;
- any physical interpretation, and novelty.

The prior-art status of the 1D formula and of Bernstein-type bounds is `[UNVERIFIED]` until the
Stage 0 literature check [G-V-17]. That C0 checks the 1D formula does not make it a cited
source.

## 7. Verdicts

Verdicts per declared mass:
- `VGRP_MAX_CERTIFIED` (exact `V_grp^max(m)^2`, maximizer set, T3 signs);
- `CEILING_ONLY` (A5 rational upper bound `V^2` without a witness);
- `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`.

Verdicts per hypothesis [G-V-13]:
- **At one mass.** A `VGRP_MAX_CERTIFIED` mass decides H1, H2 and H3 at that mass. A
  `CEILING_ONLY` mass with ceiling `V^2` decides only:
  - H2 true at that mass if `V^2 < 1/3`;
  - H1 false at that mass if `V^2 < n^2/3`.
  Otherwise it decides nothing. An OPEN mass decides nothing.
- **Over the five masses,** with this precedence:
  1. `REFUTED_AT_m=<value>` if some mass decides the hypothesis false, even if other masses are
     OPEN;
  2. `CONFIRMED_AT_DECLARED_MASSES` only if all five masses decide it true;
  3. `UNDECIDED` otherwise.

Gate-level verdicts:
- `STOPPED_PRIOR_ART`;
- `STOPPED_CONTROL_FAILED`;
- `STOPPED_EXACT_NUMERIC_DISAGREEMENT`.

A passing script promotes nothing (`CLAUDE.md`, gate cycle step 5).

## 8. Deliverables

1. **Report** `reports/YYYY-MM-DD--dirac-vgrp-max.md`, citing the preregistration commit.
2. **Exact verifier** `scripts/verify_dirac_vgrp_max_gate.py`. It is fail-closed, covers
   Stage 0 and Stage A, and uses no floating point in any certified quantity. Its two exact
   command forms go into `.claude/settings.json`, and an entry goes into `scripts/README.md`
   stating what it does not certify.
3. **Diagnostic sweep** for Stage B, behind the `--diagnostics` flag of the same script
   (decision D4). The default run executes only Stage 0 and Stage A. Diagnostic output is
   labelled `SUPPORTED`, and no exact check reads it.
4. **Independent review** by Grok (decision D5, as amended), recorded with the SHA256 of the
   candidate, the base commit, the real model name that answered, and the `~/herramientas`
   commit used. Grok generation must be probed first (`CLAUDE.md`: `sanedrin --listar` does not
   prove a house can generate). If Grok cannot generate, the user picks the substitute.
5. **Promotion**, if any, in a separate commit to `CURRENT_STATE.md`, by user decision.

## 9. User decisions (2026-11-06)

- **D1. Mass set.** The five declared rational-`n` masses are approved.
- **D2. Stage B grid.** `N = 256` per axis is approved.
- **D3. Symbolic `n`.** Out of scope for this gate. Only the D1 instances are certified.
- **D4. Stage B location.** A `--diagnostics` flag in the exact verifier. The default run is
  exact only.
- **D5. Reviewer.** DeepSeek, for the charter and for the execution. **Amended 2026-11-06:**
  DeepSeek could not generate (account-level `insufficient_balance_error`, request_id
  `1f6a0357-8eb2-4de0-baeb-b72665234588`), so it is marked `ausente`. Following the substitution
  rule then in Sec. 8, item 4, the user chose Grok (`grok-4.7`, generation probed the same day).
- **D7. Stage B tolerances.** Relative `1e-9`, two-sided, as in Sec. 4, B3 (user approval «SI»,
  2026-11-06).
- **D6. Branch.** `theory/massive-vgrp-bcc`, from `main` (`bce5599`), separate from the pending
  local changes on `research/schur-stability-audit`.
