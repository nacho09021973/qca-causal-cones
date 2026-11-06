# DIRAC_VGRP_MAX — massive group-velocity ceiling, standard Pavia Dirac family, d=3

**Status: DRAFT v2 (2026-11-06), not frozen.** Drafted by Claude Code (Claude Opus 5.5) at the
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
  - **Massless node.** The massless group speed at the node equals `r_in`.
- **Not known in this repo.** `V_grp^max` of this family for any `0 < m < 1`. Where it is
  attained. Whether it lies below, at or above `r_in`.
- **Literature (to do before execution, part of Stage 0).** The Pavia papers may already state
  the group velocity of the massive BCC automaton. Read `sources/1601.04832v1.pdf` and
  arXiv:1601.04842 (not yet in `sources/`) for any statement about `∇ω`, and record the pages
  read. `NOVELTY = OPEN`. Until that check is done, any prior-art status is `[UNVERIFIED]`.
- **Question.** See Sec. 1.
- **Results that end the gate.**
  - The exact value of `V_grp^max` at the declared masses, with its maximizer set, certified as
    in Sec. 4.
  - Or a stop under Sec. 5.

## 1. Single question

For the standard Pavia Dirac family in `d = 3` and each declared mass `m`, what is

`V_grp^max(m) := max_{k ∈ BZ} ||∇_k ω(k; m)||`,  `ω = acos(n u(k/sqrt(3)))`,

and where is the maximum attained?

The answer is compared with:
- `r_in(C_micro) = 1/sqrt(3)`;
- `V_causal^max = 1`;
- the cited values of `c_H` and `c_{ω^2}`.

These are comparisons only. The quantity named `c_IR` is neither computed nor inferred here.

## 2. Declared class

| Item | Declaration |
| --- | --- |
| Symbols | The four Pavia Dirac symbols built from `A+, B+, A-, B-` (the four cases of `verify_weyl_dirac_gate.py`) |
| Internal dimension | 4 (two Weyl doublets coupled by the on-site mass term) |
| Substrate | BCC, `N_3 = {(±1,±1,±1)/sqrt(3)}`, plus on-site; one complete update per time step `Δt = 1` |
| Mass | Declared rational set `m ∈ {3/5, 4/5, 5/13, 12/13, 8/17}`, with `n` respectively `4/5, 3/5, 12/13, 5/13, 15/17` (decision D1). Rational `n` keeps every coefficient of Sec. 4 in `Q`. It does not by itself guarantee that Stage A finishes within budget; Sec. 5 governs that |
| Brillouin zone | The full torus `q ∈ [-π, π)^3`. No symmetry reduction unless it is proved exactly in Stage 0 |
| Branch | Both phases `±ω`. Their gradients differ only in sign, and Stage 0 must verify this, not assume it |
| Excluded | `m = 0` (ω is not differentiable at the node) and `m = 1` (support collapses to on-site, so ω is constant) |

## 3. Targets and preregistered hypotheses

**Targets.**
- T1. The exact value of `V_grp^max(m)` at each declared mass. Its square is an algebraic number,
  given by a minimal polynomial over `Q` and an isolating interval with rational endpoints.
- T2. The exact set of maximizers in `q`, up to the symmetries proved in Stage 0.
- T3. The exact sign of `V_grp^max(m) − r_in`, `V_grp^max(m) − c_H(m)` and
  `V_grp^max(m) − c_{ω^2}(m)` at each declared mass.

**Hypotheses**, frozen before any computation. They are tests, not predictions. No outcome is
favoured.
- **H1 (transplanted 1D formula).** `V_grp^max(m) = n · r_in = n/sqrt(3)` (in 1D, `n = cos(arcsin m)`).
  - CONFIRMED_AT_DECLARED_MASSES only if it holds exactly at all five masses.
  - REFUTED_AT_m=… on the first exact counterexample.
- **H2 (strict ceiling).** `V_grp^max(m) < r_in` at every declared mass.
- **H3 (axis attainment).** The maximum is attained on a coordinate axis of `q`.

No hypothesis is a claim about "any isotropic massive QCA". A confirmation at five masses of one
family is recorded as exactly that.

## 4. Method, named before any computation

**Reduction (to be proved exactly in Stage 0, not assumed).** For `0 < m < 1`, `|n u| <= n < 1`
on the whole torus, so `ω` is real-analytic there. Let

`Φ(q) := ||∇_k ω||^2 = (n^2/3) · ||∇_q u||^2 / (1 − n^2 u^2)`.

The torus is compact and has no boundary. Therefore `V_grp^max(m)^2 = max Φ`, and the maximum is
attained at a critical point of `Φ`.

**Stage 0 — exact preliminaries** (SymPy, no floating point):
1. Check that `published_symbol` and the Dirac block reproduce the spectrum `cos ω = n u`. Reuse
   these helpers read-only from `verify_weyl_dirac_gate.py`. **That file's bytes are not
   changed.**
2. Prove `|n u| < 1` on the torus for each declared mass, and derive `Φ` symbolically.
3. **Control C0 (1D):** with `u = cos q`, prove that `max Φ = n^2` (normalized `r_in = 1`),
   attained at `q = ±π/2`. If C0 fails, the pipeline is wrong and the gate stops.
4. Determine exactly which signed permutations of `(q_x, q_y, q_z)`, combined with the choice of
   `χ` and with transposition, leave `u` invariant or map one case to another. Only symmetries
   proved here may reduce later stages.
5. Record the literature check of Sec. 0.

**Stage A — exact global maximum** (primary; certifies T1–T3):
- **A1. Rational charts.** Use `t_i = tan(q_i/2)`. A second chart `t_i' = cot(q_i/2)` covers
  `q_i = π`. Every chart combination is enumerated: `2^3` charts, or fewer if Stage 0 proves
  symmetries that identify them.
- **A2. Critical system.** In each chart, `∇Φ = 0` is equivalent, after clearing positive
  denominators, to the polynomial system
  `(1 − n^2 u^2) ∂_i G + 2 n^2 u G ∂_i u = 0`, where `G = ||∇_q u||^2`. Its coefficients are in
  `Q` at each declared mass.
- **A3. Zero-dimensionality.** Compute a Gröbner basis over `Q` or use resultants. If the ideal
  is zero-dimensional, isolate its real solutions exactly, with rational isolating boxes. If it
  is positive-dimensional, restrict `Φ` exactly to each component and repeat on that component.
  A component that cannot be handled exactly triggers the stop in Sec. 5.
- **A4. Comparison.** Evaluate `Φ` at every real critical point as an algebraic number. Determine
  the maximum by exact sign comparison of differences, and the maximizer set.
- **A5 (alternative certificate, if A3 does not finish).**
  - Upper bound: a sum-of-squares certificate with rational coefficients for the trigonometric
    polynomial `V^2 (1 − n^2 u^2) − (n^2/3) G >= 0`.
  - Lower bound: an exact witness `q_*` with `Φ(q_*) = V^2`.
  - Both are required. An upper bound alone gives only a ceiling, recorded as such.

**Stage B — numerical sweep of the Brillouin zone** (diagnostic only, `SUPPORTED`; the user's
acceptance criterion):
- **B1.** A uniform grid on the full torus `[-π, π)^3`, with no symmetry reduction and no
  assumption of isotropy or continuous spherical symmetry. Grid: `N = 256` points per axis
  (decision D2), for each declared mass and each of the four symbols. It runs only under the
  `--diagnostics` flag of the exact verifier (decision D4). Report the grid maximum of
  `Φ` and its location.
- **B2.** Local refinement (Newton or BFGS from the best 64 grid points). Report every distinct
  local maximum found.
- **B3. Role.** Stage B runs **after** Stage A. It is a cross-check: the grid maximum must not
  exceed the exact maximum, beyond a rounding allowance declared in the script before it runs.
  Every refined local maximum must lie in an isolating box of an exact critical point from A3.
  - Any disagreement triggers the stop `STOPPED_EXACT_NUMERIC_DISAGREEMENT`.
  - Stage B never certifies a value, never feeds a terminal verdict, and cannot rescue a stopped
    Stage A. A finite scan proves no global maximum (`CLAUDE.md`, hard rules).

## 5. Stop rules and budget

- **Budget.** Stage A gets 900 s of CPU per declared mass per symbol class, cumulative across
  runs. Stage 0 step 4 decides how many symbol classes there are. The A5 alternative gets one
  additional budget of the same size.
- **Stop with `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`** if neither A3–A4 nor A5 finishes within
  budget for some mass. The masses that did finish are recorded as certified; the rest stay
  OPEN.
- **Stop with `STOPPED_CONTROL_FAILED`** if control C0 fails.
- **Stop with `STOPPED_EXACT_NUMERIC_DISAGREEMENT`** on any disagreement under Sec. 4, B3.
- **No extensions without a new charter:** no extra masses, no symbolic-in-`n` result
  (decision D3), no `s = 4`, no other substrates, no `d = 2`.

## 6. Exclusions

The following are not computed, claimed or inferred here:
- `c_IR`, `c_H` or `c_{ω^2}`, which are only cited;
- signalling, evanescent precursors, saddle-point asymptotics;
- entanglement, the coin Bloch tensor, Wilson masses, fermion doublers;
- any other family or class, and any general QCA law;
- any physical interpretation, and novelty.

The 1D formula and Bernstein-type bounds are prior art.

## 7. Verdicts

Verdicts per declared mass:
- `VGRP_MAX_CERTIFIED` (exact value, maximizer set, T3 signs);
- `OPEN_AFTER_CRITICAL_POINT_ANALYSIS`;
- `CEILING_ONLY` (A5 upper bound without a witness).

Verdicts per hypothesis:
- H1, H2 and H3 each get `CONFIRMED_AT_DECLARED_MASSES` or `REFUTED_AT_m=<value>`;
- `UNDECIDED` where some mass is OPEN.

Gate-level verdicts:
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
4. **Independent review** by Grok (decision D5, as amended), recorded with the SHA256 of the candidate,
   the base commit, the real model name that answered, and the `~/herramientas` commit used.
   DeepSeek generation must be probed first (`CLAUDE.md`: `sanedrin --listar` does not prove a
   house can generate). If DeepSeek cannot generate, the user picks the substitute.
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
  rule of Sec. 8, item 4, the user chose Grok (`grok-4.7`, generation probed the same day).
- **D6. Branch.** `theory/massive-vgrp-bcc`, from `main` (`bce5599`), separate from the pending
  local changes on `research/schur-stability-audit`.
