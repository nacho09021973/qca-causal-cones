# Independent review of the hexagonal ceiling execution

Date: 2026-11-02. Branch: `research/schur-stability-audit`.
Reviewed snapshot: base `61232d7`; report
`reports/2026-11-01--hex-ceiling.md`, verifier
`scripts/verify_hex_ceiling_gate.py` (24/24), contract preregistered at
`8c56ced`.
Status: **Gemini PASS; Grok REPAIR_REQUIRED (two repairs, applied)**.
Not promoted.

## Execution

User instruction «si, con gemini». One sealed `revision-ciega gemini` run,
model `gemini-4-argon` (generateContent, thinkingLevel medium, no tools),
generation probed beforehand, 2026-11-02 07:09:32–07:11:05 UTC (about 90 s),
finish `STOP`, exit 0. Documents: contract, report, verifier,
`verify_c_across_lattices_gate.py` (imported helpers), and the exploratory
`explore_hex_saturation_support.py`. Input SHA256
`64e38b3b420f0a2d1b697c7a50e125c0bdc46632c9324abd4314f067a9d2feaf`; review
SHA256 `30dd2d1e9c9bf30f001afd848c89a04abcc0a2a77938f45c9565dfa7b4f883cb`. Raw files in `debates/2026-11-02--hex-ceiling-review/`. Tools commit
`ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.

Grok did not participate (account balance exhausted at the last attempt).
This is **one** cross-family agent review (author Claude, reviewer
Google), not two houses and not human review.

## Verdicts

| Block | Gemini |
| --- | --- |
| L0 | PASS |
| T1 | PASS |
| T2_SATURATION_STEP | PASS |
| T2_MINIMAL_CERTIFICATE | PASS |
| SCOPE_AND_CODE | PASS |
| Global | PASS, no mandatory repairs |

Gemini independently reconstructs the grid identity, the T1 algebra
(double-angle cancellation, `c_0^2 = (3/2) l^2 (1-g)`, `g >= -1/2`), the
saturation step (Julia / Bernstein equality, Cauchy–Schwarz, layer sums by
linear independence of characters), the derivation `A_0 = -I/2` by summing
layer equations, the completeness of the unitarity system, the real
infeasibility from the negative discriminant, and the square control. It
finds no tautological check and no scope overreach, and accepts the
exploratory script as correctly labelled.

## Author's notes on the review (not repairs)

- Gemini adds a parenthetical "elementary verification without Julia" in
  block 3. As written it is not valid (it treats `|P|^2 = sum |a_k|^2`
  pointwise). The report does not use it; the saturation step rests on
  Julia's lemma / the Bernstein equality case. It is not counted as an
  independent proof of that step.
- Gemini's chirality note (case `u_y = -y`) is unnecessary: an `SO(3)`
  rotation maps any orthonormal pair to `(x, y)`. The report's reduction
  stands as written.
- The review was short (about 90 s).

## Second house: Grok (2026-11-02)

User instruction «1, esperamos a grok». After the account balance was
restored (probe answered `OK`), one sealed `revision-ciega grok` run,
`grok-4.7`, 08:02:29–08:23:24 UTC, exit 0. Request body and documents
identical to the Gemini run (same input SHA256
`64e38b3b420f0a2d1b697c7a50e125c0bdc46632c9324abd4314f067a9d2feaf`); blind
to the Gemini review. Raw files in
`debates/2026-11-02--hex-ceiling-review-grok/`; review SHA256 `5c2add01e66d3f94a5834cabcad9259f1ea97a9c8d3da4df6e0a5c7a59f2c823`.

| Block | Grok |
| --- | --- |
| L0 | **REPAIR_REQUIRED** |
| T1 | **REPAIR_REQUIRED** |
| T2_SATURATION_STEP | PASS |
| T2_MINIMAL_CERTIFICATE | PASS |
| SCOPE_AND_CODE | **REPAIR_REQUIRED** |
| Global | **REPAIR_REQUIRED**, two mandatory repairs |

Mandatory repairs, both accepted by the author:

1. **R1 (L0).** The verdict `PROVED_IN_REPO` relied on Bernstein's
   inequality named as prior art, without in-repo proof or a cited page,
   against contract Sec. 2. The grid, symmetry and application steps were
   accepted.
2. **R2 (verifier, T1).** The "rank 2 for every theta_0" record tested
   only that a minor is not identically zero. The minor is the constant
   `sqrt3 l^4/2` (author's computation; Grok's value; Gemini's
   parenthetical `-3 sqrt3/8 l^4` is wrong).

Grok also gives an independent proof of the minimal-support certificate
that does not use the Gröbner basis: the diameter mode `v_0 - v_3` forces
`S S^dag = S/2` for the free coefficient, and the three resulting cases
are excluded by the modes `v_1 - v_4` and `v_2 - v_5`; the matrix system is
inconsistent even over `C`. Clarifications (non-blocking): state the
Hermiticity of `A` in L0; name the maximum-modulus step; the hexagon fixes
the denominator `2l`; `xi` is a component, not an angle.

## Repairs applied (2026-11-02)

Report: Lemma B proves the scalar Bernstein inequality in-repo (reduction
to real polynomials, comparison with `cos(N(s - s_0) + beta)`, zero count
`>= 2N + 2` against `<= 2N`); the clarifications are written in. Verifier:
the rank record now asserts the minor equals `sqrt3 l^4/2`; 24/24. A
bounded re-review of the repairs is pending.
