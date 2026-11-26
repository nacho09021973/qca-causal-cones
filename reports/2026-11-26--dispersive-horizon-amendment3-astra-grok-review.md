# Astra and Grok reviews of Amendment 3 (dispersive-horizon transfer-matrix audit)

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`.

**Reviewed snapshot** (base `f9dce97`; identical input for both reviewers,
input SHA256 `36896ad0f60fa80427bfdaab440c4ee82ece3c024670a0759b67f358b7168d78`):

| Document | Commit | SHA256 |
| --- | --- | --- |
| `amendment3.diff` (`git diff b1c6d75 f9dce97` of the audit) | — | `046354617c56f64a6e0313c4d2f2f05e2f0e842e024f29675853bd98dc5a0540` |
| audit with Amendments 1–3 | `f9dce97` | `dc35f5e00d3356325aa0447b70df53effe81cef37ca6037263cd4fc2daaa6e90` |
| Astra's report on Amendment 2 | `f9dce97` | `ee109fe4932f4964d067a2914cd730cb700ca24da6ab16cdd3565dbee8db5a87` |
| amendment-3 verifier | `f9dce97` | `535dec08c127a0db0cdbebb6ae7fa8ed1b876e42a42e495f02cbcd97f3067e27` |
| amendment-2 verifier | `b1c6d75` | `b6c68dc431aba0b21425b1e24a3329ffbe560e673250261c234e064d0dcff243` |

**Status:** **Astra PASS; Grok PASS.** No repair required. Not promoted.

## Execution

- **Authorization:** user «SI, HAZ LA enmienda tres y pasala a Astra» and «si
  quieres la envias tambien a Grok y asi tenemos dos opiniones».
- **Probe:** generation of both houses was checked beforehand with one-line
  prompts, which returned "OK".
- **Runs:** both sealed `revision-ciega` runs used the same brief and the same
  documents, each in its own folder. Both ran in parallel and returned
  `COMPLETED`, exit 0.

| House | Model | Time (UTC) | Response SHA256 | Raw files |
| --- | --- | --- | --- | --- |
| OpenAI | `gpt-6-astra`, effort high, codex-cli 0.172.0 | 12:35:48–12:38:37 | `a7282289ae2bfd7ab381f70e28d11ca94ef4c56fd18f5d4fb1aef6c75ec2862b` | `reports/reviews/2026-11-26-dispersive-horizon-amendment3-astra/` |
| xAI | `grok-4.7`, CLI default, grok 1.0.34, 0 attempted tool calls | 12:35:48–12:54:29 | `5539a7325c3766c6fba3b4dd555098bfb26ae9a3255a72bda43a790a613a3ede` | `reports/reviews/2026-11-26-dispersive-horizon-amendment3-grok/` |

**Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.

**Independence.**

- These are two cross-family agent reviews, from two houses, of text written
  by Claude. They are not human review.
- Neither reviewer could run code. Both mark the executions and historical
  byte identities `[UNVERIFIED]`.
- Astra's previous report was attached to both as the objections being
  answered, and labelled as not a source.

## Verdicts

| Point | Astra | Grok |
| --- | --- | --- |
| 1 Jordan 3 + 1; exact rank over ℚ(√6, √10) | PASS | PASS |
| 2 Exact (u − 1)² contact (J2) | PASS | PASS |
| 3 Interior edge: identity, derivative, signs, Ω₊″ > 0, Jordan 2 | PASS | PASS |
| 4 t = 7/16 wording (quotient; endpoint u = 1) | PASS | PASS |
| 5 The 10 checks | PASS (with an optional count improvement) | PASS |
| 6 Scope and attribution | PASS | PASS |
| Global | **PASS** | **PASS** |

**What both reviewers do by hand:**

- Both derive the partition 3 + 1 a second way, without ranks: W′(0) has
  distinct eigenvalues ±i/2 at t = 3/8, which gives an analytic eigenvector
  of the cubic branch and a Jordan chain of length 3. Together with algebraic
  multiplicity 4 and geometric multiplicity 2, this forces 3 + 1. The twin
  follows from W(k + π) = −W(k).
- Both check that ℚ(√6, √10) contains all entries, since √15 = √6√10/2.
- Both check the factorization P_{3/8} = (105/64)(u − 1)²(4 − 3u).
- Both check P_{5/16}′(u*) = −(3/1024)(1 − u*)√168025, the integer bound
  168025 < 5245², the sign chain giving Ω₊″(k*) > 0, and the multiplicities
  at the interior edge (algebraic 2, geometric 1, one Jordan block of size 2).
- Both check P_{7/16} = (5/1024)(1 − u)(343w² − 525w + 144) and the absence
  of roots of the quotient in [0, 1].
- Grok also checks the numerical value of W′(0): its σ_z and σ_x
  coefficients are −1/8 and √15/8.

**Optional point, raised by both, not applied.** The final assertion of the
amendment-3 verifier fixes the earlier counts (61, 8, 39) but not
`len(checks) == 10`, and the `n/n` summary prints before that assertion. Both
reviewers state that this is not a false positive, since the ten checks are
present by inspection. It is left as is, to keep the reviewed bytes fixed.

## Outcome

Amendment 3 passes two cross-family reviews. The audit chain of the 12×12
matrix now reads:

- original audit: Astra PASS on the matrix;
- Amendment 1: Grok REPAIR_REQUIRED, repaired in Amendment 2;
- Amendment 2: Astra REPAIR_REQUIRED, repaired in Amendment 3;
- Amendment 3: Astra PASS and Grok PASS.

In the audit's scope, no `[UNVERIFIED]` mathematical point remains except the
compactness step for ω* and k₊(t), which is Astra's written argument from the
first review.

`state/CURRENT_STATE.md` is updated branch-locally. Nothing is promoted.
TRANSMISSION remains OPEN.
