# PH_REFUTATION_HEX_S25 — frozen contract

**Frozen:** 2026-11-04, before solving. Nothing in Secs. 3–5 has been
computed. Drafted by Claude Code (Claude Opus 5.5) at the user's
instruction of 2026-11-04 («haz la prueba de refutación de PH»).
**Authorization:** user approval of the draft, 2026-11-04, «SI», without
changes. Reports cite the commit that adds this file as the
preregistration commit.
**Parents:** `SUBSTRATE_SATURATION_PHASE0_GATE.md` (`9bf3019`; Sec. 7: «a
test that can fail needs its own contract, with a shape or support not in
the source table»; the user's first choice is the hexagon) and
`HEX_SUPREMUM_GATE.md` (M1; S13, S19 promoted, whole class OPEN, «S25 or any
other extension needs a new charter»). This contract is that charter. It
does not reopen S7, S13, S19 or Stage A of M1.
**Initial scientific status: OPEN.**

## 0. Pre-step check (rule of 2026-11-02)

- **Known.** (PH) [UNVERIFIED] was read off the source table, so phase 0
  cannot refute it (phase-0 Sec. 4). On the hexagonal substrate no walk of
  `W_hex^sym` with `F` in S7, S13 or S19 reaches `r_in` (promoted, CS Secs.
  12, 14). The regular hexagon is inside the phase-0 domain (`s = 2`,
  declared class `W_hex`, admissible node), so an admissible hexagonal
  saturating walk refutes (PH⇒).
- **Question.** Does a walk of `W_hex` whose composite support has as hull
  the next centred lattice hexagon, H25, reach `c_0 = r_in`?
- **Result that ends the test.**
  (a) an exact witness in `W_hex` (explicit product, Sec. 2): (PH⇒) is
  **refuted** under phase-0 Sec. 4, once the witness is reviewed and
  promoted;
  (b) an exact gap proof for H25: `PROVED_FOR_S25`. This is a bounded
  result. It is **not** evidence for (PH) beyond that support and does not
  close the hexagonal class;
  (c) budget exhausted: `OPEN_AFTER_<analysis>`, no numerics in the verdict.
- **Why this can fail.** The support H25 is not in the source table, and its
  outcome is not fixed before computing. Its geometry differs from S13 and
  S19 (Sec. 2), so the earlier proofs do not carry over automatically.

## 1. Single question

> In `W_hex` (`s = 2`, triangular lattice), is there a walk with
> `conv F = H25` and `c_0 = r_in(C_micro)`?

## 2. Class and support

`W_hex` and `W_hex^sym` exactly as in `HEX_CEILING_GATE.md` Sec. 1 and
`HEX_SUPREMUM_GATE.md` Sec. 2. Gap direction: stated for `W_hex^sym`.
Witness direction: must lie in `W_hex` (explicit product
`C_n D_n(k) … C_1 D_1(k)`). A saturating symbol without a product
factorization is reported as `CEILING_ATTAINED_IN_W_HEX_SYM_ONLY` and does
**not** refute (PH): whether `W_hex^sym` is a declared class for phase 0 is
a definitional question for the user, not decided here.

**Support.** Centred regular lattice hexagons are `R^j v`, `v in Lambda`,
`R` the 60° rotation (which preserves `Lambda`). H25: `v = 2 g_1 + g_2`,
`|v| = sqrt7`. An author's inspection count (not a certificate) gives 25
lattice points in the closed hull, against 7, 13, 19 for `v = g_1`,
`g_1 + g_2`, `2 g_1`. The verifier certifies the count and the vertex set
exactly. Facts to be certified, not assumed:

- each edge of H25 contains no lattice point besides its two vertices
  (edge vector `R v − v = −3 g_1 + 2 g_2`, coprime coordinates);
- H25 is not mirror-symmetric under the lattice reflections; its mirror
  image H25′ (`v = g_1 + 2 g_2`) is the other hexagon of the same norm. A
  lattice reflection maps `W_hex` to itself and preserves `c_0` and
  `r_in`, so H25′ is decided with H25; the verifier checks the map on the
  reduced system;
- walks with `F` inside H25 but hull S7, S13 or S19 have `F` inside that
  smaller support (the only centred lattice hexagons inside H25), so they
  are already decided. Only `conv F = H25` is new.

## 3. Method, named before any computation

As M1 (`HEX_SUPREMUM_GATE.md` Sec. 4), restated for H25, whose vertices are
not at angles `k pi/3`: coordinates are rotated so that the normal form
`A(n) = r_in n . sigma` of the hex-ceiling report Sec. 3, Step 2 applies;
the rotation is part of the certified setup.

- **Stage A (by hand, checked by the verifier).** Facet-line rigidity
  (top edge sums to `P_+(n_f)`, bottom edge to `P_-(n_f)`, intermediate
  layers to `0`) and the extreme-face identities
  `E_e E_{−e}^dag = 0`, `E_{−e}^dag E_e = 0`. On H25 each edge polynomial
  has two terms (the two vertices); the consequences are derived in the
  report and checked exactly. If Stage A alone gives a gap for H25, stop
  there with `PROVED_FOR_S25`.
- **Stage B (exact decision).** Unknowns left after Stage A; equations:
  layer equations, node, isotropy, unitarity. Accepted certificates as in
  M1 Sec. 4 (i) or (ii) (`HEX_SUPREMUM_GATE_AMENDMENT_1.md` for (i)),
  checked by the verifier without rerunning a solver. A Gröbner basis over
  `C` other than `{1}` decides nothing. A witness is certified exactly
  (unitarity, composite `F`, hull H25, node, isotropy, `c_0 = r_in`,
  product factorization).
- **Exploratory numerics** in a versioned script labelled exploratory may
  guide the search for a witness or a certificate; no numerical result
  enters a verdict, and no rigidity is inferred from a failed search.
- **Controls.** As in M1: the reductions are run on the square substrate,
  where they must keep the known saturating walk.

## 4. Stop rules and budget

- Budget: at most 3600 s of solver wall time **cumulative for H25** (H25′
  by the reflection), however split; every run recorded with command,
  wall time and exit code. A run cut by the budget is not evidence.
- Stop at the first of: a certified witness (a); a certified gap (b);
  budget exhausted (c).
- Do not widen the class or the support during execution. No support beyond
  H25, no `s > 2`, no other lattice.

## 5. Verdicts

- H25: `CEILING_ATTAINED_BY_EXPLICIT_WALK` (in `W_hex`) /
  `CEILING_ATTAINED_IN_W_HEX_SYM_ONLY` / `PROVED_FOR_S25` /
  `OPEN_AFTER_<analysis>`.
- (PH⇒): `REFUTED_BY_H25_WITNESS` only after review and promotion of a
  `W_hex` witness; otherwise `NOT_REFUTED_ON_H25` (never `CONFIRMED`).
- HX2 of the hex-ceiling gate: `REFUTED_BY_<witness>` or
  `CONFIRMED_FOR_S25`.

## 6. Exclusions

`s > 2`, masses, `V_grp^max`, inhomogeneous or encoded walks, other
lattices or new substrate classes, general QCA laws, claims about our
universe. No novelty claim (Bernstein's inequality and its equality case
are prior art; the hexagonal prior-art check is not finished).

## 7. Deliverables

Report `reports/YYYY-MM-DD--ph-refutation-hex-s25.md`; verifier
`scripts/verify_ph_refutation_hex_s25_gate.py` (fail-closed, exact, checks
certificates; both exact command forms in `.claude/settings.json`); reviewed
verifiers (`verify_hex_ceiling_gate.py`, `verify_hex_supremum_gate.py`,
`verify_hex_supremum_b19.py`) imported read-only; exploratory scripts
versioned and labelled; independent cross-family review with every
imported module attached; promotion as a separate user decision.
