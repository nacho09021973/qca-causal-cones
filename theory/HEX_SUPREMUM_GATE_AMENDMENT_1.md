# HEX_SUPREMUM (M1) — Amendment 1 (post-execution, M1-B19)

**Status: APPROVED, 2026-11-03** («apruebo la enmienda, haz commit y aplica
las correcciones»), without changes to the draft. Drafted by Claude Code
(Claude Opus 5.5) on 2026-11-03 at the user's instruction («redacta la
enmienda»). Approval of the amendment is not promotion of M1-B19.
**Amends:** [`HEX_SUPREMUM_GATE.md`](HEX_SUPREMUM_GATE.md), preregistration
commit `86573ca`. **The frozen file is not edited.** This amendment is a
separate document; where it applies, it prevails over the frozen text, and
only there.
**Disclosure: it is written after the result.** M1-B19 was executed
(`6302328`, pushed) and reviewed by Grok (`f80c075`, REPAIR_REQUIRED, one
mandatory repair: this amendment). The user had flagged the same deviation
before the review («Debe declararse y resolverse mediante una enmienda
explícita antes de promocionar; nunca modificar retroactivamente el
prerregistro»). Because it is post hoc, it may only **name and declare**
what was done; it does not lower any requirement on what has to be proved,
and it does not change any verdict name.

## 0. Pre-step check

- **Known.** The verifier `scripts/verify_hex_supremum_b19.py` (SHA-256
  `244bb106…`, 17/17, two runs: 10 min 44 s and 10 min 52 s) checks: 730
  rational multipliers `c_i`; `p = sum c_i f_i`, expanded exactly; the
  polynomial identity `p = (1,t) G (1,t)^T`; 19 positive pivots of `G`,
  exact in `QQ(sqrt3)`. The report (`reports/2026-11-03--hex-supremum-b19.md`,
  Sec. 3) and the docstring of `check_certificate` call this «the
  contract's form (Sec. 4 (ii))». Grok (`informe_grok.md`, point 6): it is
  not the literal form (ii), which requires rational coefficients and the
  expansion of both sides of `-1 = sum q_j^2 + sum h_i f_i`; the
  implication itself is valid (points 4–5 PASS).
- **Question.** Which accepted form of Sec. 4 does the B19 certificate meet,
  and which literal clauses does it not meet?
- **What would sink this amendment.** If the certificate met neither form
  of Sec. 4 without relaxing what has to be proved (for example, if `p` were
  not in the ideal, or its positivity were not certified over all real
  variables), an amendment could not repair it: M1-B19 would be
  `OPEN_AFTER_<analysis>`.

## 1. Classification of the B19 certificate: Sec. 4 (i)

The frozen Sec. 4 (i) accepts «a polynomial `p` in the ideal, given with
explicit exact cofactors `p = sum_i h_i f_i`, whose absence of real zeros is
itself certified exactly (e.g. ... a sum-of-squares-plus-positive-constant
representation of `p`)». For M1-B19 the certificate is assessed under (i),
with exactly these components, all checked by the verifier:

1. **Ideal element.** `p = sum_i c_i f_i`, with the `f_i` the 730 distinct
   real quadratics of the reduced S19 system (Sec. 2 of the report) and
   constant cofactors `c_i` rational, read from
   `scripts/data/hex_s19_certificate.json` (SHA-256 `548988f7…`); the file's
   length must equal the number of equations.
2. **Gram identity.** `G` is the symmetric `19 x 19` matrix of `p` in the
   basis `(1, t_1, ..., t_18)`; `p - (1,t) G (1,t)^T` expands exactly to `0`.
3. **No real zeros.** Exact Gaussian elimination of `G` without pivoting
   over `QQ(sqrt3)`, every pivot of the form `a + b sqrt3` with `a, b`
   rational and its sign decided exactly. All 19 pivots positive implies
   `G` positive definite (Sylvester), hence `p(t) > 0` for every
   `t in R^18`. Since every `f_i` vanishes at a solution, there is none.

This is the "sum-of-squares-plus-positive-constant" case named in (i):
with `0 < mu <= 1/(G^{-1})_00`, `p = mu + sum_j d_j l_j^2`, `d_j >= 0`. The
verifier does not build `mu`, `L`, `D`; it certifies `G > 0`, which implies
that representation exists. The identity `-1 = sum (d_j/mu) l_j^2 + sum
(-c_i/mu) f_i` in the report is a corollary and **is not claimed as a
form (ii) certificate**.

## 2. Declared deviations from the literal frozen text

| Frozen clause | What B19 does | Declaration |
| --- | --- | --- |
| Sec. 4 (ii): «exact rational coefficients», both sides expanded | Not used as (ii); see Sec. 1 | B19 does not claim form (ii) |
| Sec. 4 (i): field not stated | `c_i` in `QQ`; `G`, pivots in `QQ(sqrt3)` | Accepted: the system's own coefficients lie in `QQ(sqrt3)` (normal form `A(n) = r_in n.sigma`, `r_in = sqrt3/2`, hexagon geometry); exact arithmetic in that field |
| Sec. 4: «checked exactly and quickly ... without rerunning a solver» | Exact; no solver rerun; about 11 min wall time | Declared. «Quickly» is not met literally; accepted for B19 |
| Sec. 5: 3600 s of «solver wall time» per support | Gröbner / nonlinear exact solver on S19: 0 s. Exploratory numerics (labelled, no verdict): 558 s least squares, 2 x 368 s SLSQP | Declared. Even counted as solver time, 1294 s < 3600 s |
| Sec. 8: report `reports/YYYY-MM-DD--hex-supremum.md`, verifier `scripts/verify_hex_supremum_gate.py` | B19 in a separate report `2026-11-03--hex-supremum-b19.md` and verifier `verify_hex_supremum_b19.py`, which imports the reviewed `verify_hex_supremum_gate.py` read-only | Declared. Keeps the reviewed verifier's bytes unchanged |

## 3. What this amendment does not change

- The question, the classes `W_hex` and `W_hex^sym`, the supports, the
  stop rules, the exclusions (Sec. 6) and the verdict names (Sec. 7).
- The rule that no numerical result enters a verdict.
- The requirement of independent cross-family review and a separate
  promotion. The user asked for two houses; Gemini has not reported
  (402, no credits). This amendment does not replace that review.
- Anything beyond S19. S25 is not authorized.
- The bytes of `verify_hex_supremum_b19.py`: its docstring's mention of
  «contract Sec. 4 (ii)» is superseded by this amendment, not edited
  (editing would require a new review of the file).

## 4. Consequential text repairs (report only, after approval)

In `reports/2026-11-03--hex-supremum-b19.md`:

- Sec. 3: replace «In the contract's form (Sec. 4 (ii))» by the
  classification of Sec. 1 above, citing this amendment.
- Sec. 1, after the proofs: «A3 and A4 are consequences of unitarity,
  rigidity and the normal form `A(v) = r v.sigma` (hex-ceiling report
  Sec. 3, Step 2)» (Grok, point 1).
- Sec. 2, Controls: state that the counts «13-parameter family», «298
  reduced equations» and S7's «1 free parameter» are printed output, not
  checks (Grok, point 7).
- Header: cite this amendment and the Grok review.
