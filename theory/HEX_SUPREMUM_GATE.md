# HEX_SUPREMUM (M1) — frozen contract

**Frozen:** 2026-11-03, before solving. Nothing in Secs. 3–5 has been
computed. Drafted by Claude Code (Claude Opus 5.5) at the user's
instruction («vamos con la carta M1»).
**Authorization:** user approval of the draft, 2026-11-03, «APROBACIÓN CON
ENMIENDAS», with three amendments incorporated before freezing: (1) the
solver budget is cumulative per support, not per run (Sec. 5); (2) the
sum-of-squares certificate has the explicit form of Sec. 4, and the
no-real-zero alternative needs its own certificate; (3) a witness answers
the saturation question only, without a broader claim about the substrate
(Sec. 0). Approval covers the preregistration and Stage A as first work,
with no confirmatory numerics.
Reports cite the commit that adds this file as the preregistration commit.
**Initial scientific status: OPEN.**
**Parent:** `HEX_CEILING_GATE.md` (T2 general `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS`,
CURRENT_STATE Sec. 12). This gate continues T2 only; it does not reopen L0,
T1 or the minimal-support T2.

## 0. Pre-step check (rule of 2026-11-02)

- **Known.** K4 (`c_0 = r_in` attained on line, square, BCC/cubic rows) and
  K5 (hexagon: L0 `c_0 <= r_in` on `W_hex`; T1 `sup = sqrt3/2` in the
  `n = 3` antipodal subclass; no s=2 walk with `F within {0} U vert(H)`
  reaches `r_in`). Saturation along a facet normal is rigid (hex-ceiling
  report Sec. 3, Step 1). A grevlex Gröbner basis over `C` for the 19-point
  ball did not finish in 900 s, and would not have decided real
  solvability anyway (hex-ceiling report Sec. 4).
- **Question.** Does any s=2 walk in `W_hex` reach `c_0 = r_in`?
- **Result that ends the line** (research-lines report, M1):
  (a) an explicit witness in `W_hex` with `c_0 = r_in`, certified exactly:
  the saturation question is answered affirmatively for `s = 2` and the
  line M1 closes. This shows only that the hexagonal substrate admits
  saturation in `W_hex`; it does not by itself show that no other
  property of `c` specific to the hexagonal substrate remains;
  (b) no exact method of Sec. 4 finishes within the session budget of
  Sec. 5: stop at `OPEN_AFTER_<analysis>`, no numerics.
  A gap proof for the whole class keeps the line (it is the only outcome
  that makes the hexagon substrate-specific). A gap proof for a bounded
  support only is recorded as such and does not close the line either way.

## 1. Single question

> On the hexagonal substrate, is there a two-component walk of the class
> `W_hex` with `c_0 = r_in(C_micro)`, i.e. a walk whose support is not of
> minimal type and which saturates the ceiling?

## 2. Declared class

`W_hex` exactly as in `HEX_CEILING_GATE.md` Sec. 1 (triangular lattice
`Lambda`, `s = 2`, product of coin–partial-shift factors, `C_micro = conv F`
a regular hexagon from the exact composite support, scalar `U(0)`,
traceless isotropic linear term, longest vector of `F` of length 1).

Two readings of the class are kept apart:

- **Gap direction.** A proof that `c_0 < r_in` may use only unitarity, `F`,
  the node and isotropy (as the minimal-support T2 did). It then holds for
  the larger class `W_hex^sym` of all s=2 unitary Laurent polynomials with
  those properties, which contains `W_hex`; it is stated for `W_hex^sym`.
- **Witness direction.** A witness must lie in `W_hex`: it is given as an
  explicit product `C_n D_n(k) ... C_1 D_1(k)`. A saturating symbol found
  without a product factorization is reported as a witness in `W_hex^sym`
  only, which does not meet result (a); in two dimensions factorization is
  not automatic [UNVERIFIED as a general statement; not used].

**Supports.** Regular lattice hexagons centred at the origin have vertices
`R^j v`, `v in Lambda`, `R` the 60° rotation. Ordered by the number of
lattice points of the closed hull (to be certified by the verifier, not
assumed):

- `S7`: `v = g_1` — 7 points; every walk is of minimal type (done in T2).
- `S13`: `v = g_1 + g_2` — origin, inner ring of six unit vectors, six
  vertices: 13 points. Smallest support not covered by T2.
- `S19`: `v = 2 g_1` — the radius-2 ball (contains JDW L6c, `c_0/r_in =
  sqrt3/2`).
- larger hexagons: covered only by a structural argument (Sec. 4, Stage A).

## 3. Targets

- **M1-A (structural).** Necessary conditions for saturation valid for
  every support, from facet-line rigidity and the extreme-face unitarity
  identities (Sec. 4). Either a gap proof for `W_hex^sym`, or a reduced
  normal form with fewer unknowns for Stage B.
- **M1-B13.** On `S13`: gap proof (`c_0 < r_in` for every walk with
  `F within S13`) or an explicit witness.
- **M1-B19.** On `S19`: same, only after M1-B13 has a verdict.

## 4. Method, named before any computation

**Stage A — structural reduction (by hand, checked by the verifier).**

1. Facet-line rigidity (hex-ceiling report Sec. 3, Step 1, reused): along
   each of the three facet-normal lines the top edge sums to `P_+(n_f)`,
   the bottom edge to `P_-(n_f)`, every intermediate layer to `0`.
2. Extreme-face identities. The Newton polytope of `U U^dag` lies in
   `C - C = 2C`. For each edge `e` of `C` with outward normal `n_e`, the
   coefficients of `U U^dag` and `U^dag U` on the face of `2C` in direction
   `n_e` vanish (except at `0`, not on the face). With `E_e(x)` the edge
   polynomial of the top edge and `E_{-e}(x)` that of the opposite edge,
   this gives `E_e(x) E_{-e}(x)^dag = 0` and `E_{-e}(x)^dag E_e(x) = 0` as
   one-variable Laurent identities, together with `E_e(1) = P_+(n_e)`,
   `E_{-e}(1) = P_-(n_e)` from step 1.
3. Use 1–2 (and, if needed, the next-to-extreme faces) to restrict the
   edge coefficients to rank-one forms and eliminate unknowns, before any
   solver is run. Step 2 is a standard fact about Laurent polynomials
   (product of extreme coefficients); its use here is stated and proved in
   the report, not cited.

**Stage B — exact decision on a bounded support (`S13`, then `S19`).**

- Unknowns: the coefficients left after Stage A and the normal form of the
  hex-ceiling report Sec. 3, Step 2 (`A(n) = r_in n . sigma`, vertices at
  `k pi/3`).
- Equations: layer equations, node and isotropy, and unitarity
  `sum_h A_{h+d} A_h^dag = delta_{d0} I`, `sum_h A_h^dag A_{h+d} = delta_{d0} I`.
- **Infeasibility certificate (gap).** Accepted forms only, each checked
  exactly and quickly by the verifier without rerunning a solver:
  (i) a polynomial `p` in the ideal, given with explicit exact cofactors
  `p = sum_i h_i f_i`, whose absence of real zeros is itself certified
  exactly (e.g. a univariate polynomial with negative discriminant, as in
  T2, or a sum-of-squares-plus-positive-constant representation of `p`);
  or (ii) for the real system `f_1 = ... = f_m = 0`, an identity
  `-1 = sum_j q_j(x)^2 + sum_i h_i(x) f_i(x)` with exact rational
  coefficients, the verifier expanding both sides and checking equality. A Gröbner basis over `C`
  different from `{1}` decides nothing about real solvability and is not a
  verdict.
- **Witness.** Closed form, certified exactly: unitarity, composite `F`,
  regular hexagonal hull, node, isotropy, `c_0 = r_in`, and the product
  factorization (Sec. 2).
- Exploratory numerics (a versioned script labelled exploratory) may guide
  the search for a witness or for the certificate. **No numerical result,
  scan, optimisation or failed search enters a verdict**, and no rigidity
  is inferred from one.

## 5. Stop rules and budget

- Order: Stage A, then M1-B13, then M1-B19. Do not start the next stage
  before the previous has a verdict or a recorded stop.
- Budget: one working session, and at most 3600 s of solver wall time
  **cumulative per support** (`S13`, `S19`), however it is split across
  runs; every run is recorded with its command, wall time and exit code.
  A run cut by the budget is inconclusive and is not evidence.
- Stop at the first of: a witness meeting Sec. 4 (result (a); then M1
  closes, with the limited reading of Sec. 0); a gap proof for `W_hex^sym` (line kept); budget exhausted
  (result (b), `OPEN_AFTER_<analysis>` naming the stages done).
- Do not widen the class during execution; restricted results stay
  restricted.

## 6. Exclusions

`s > 2`, other lattices, masses, `V_grp^max`, inhomogeneous or encoded
walks, new substrate classes, general QCA laws, claims about our universe.
No novelty claim: Bernstein's inequality and its equality case are prior
art; the hexagonal-ceiling prior-art check (plan step 4) is not finished.

## 7. Verdicts

- M1-A: `GAP_PROVED_IN_CLASS` (for `W_hex^sym`), `REDUCED_TO_<normal form>`,
  or `OPEN_AFTER_<analysis>`.
- M1-B13, M1-B19: `PROVED_FOR_<support>` (gap on that support),
  `CEILING_ATTAINED_BY_EXPLICIT_WALK` (in `W_hex`) /
  `CEILING_ATTAINED_IN_W_HEX_SYM_ONLY`, or `OPEN_AFTER_<analysis>`.
- HX2 (from the parent gate): `CONFIRMED_IN_CLASS` / `REFUTED_BY_<witness>` /
  `OPEN`, and `CONFIRMED_FOR_<support>` for a bounded result.

## 8. Deliverables

Report `reports/YYYY-MM-DD--hex-supremum.md`; verifier
`scripts/verify_hex_supremum_gate.py` (fail-closed, exact, checks
certificates rather than rerunning solvers; both exact command forms added
to `.claude/settings.json`); exploratory scripts, if any, versioned and
labelled; independent cross-family review; then a separate promotion.
Reviewed verifiers (`verify_hex_ceiling_gate.py`) are imported read-only,
never edited.
