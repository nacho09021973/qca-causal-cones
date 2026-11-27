# Astra review of Amendment 2 (dispersive-horizon transfer-matrix audit)

Date: 2026-11-26. Branch: `research/dispersive-horizon-channels`. The reviewed
documents are byte-identical to `b1c6d75`.

**Reviewed snapshot:**

| Document | Commit | SHA256 |
| --- | --- | --- |
| `amendment2.diff` (`git diff 63db34b b1c6d75` of the audit) | — | `e1363940f474ef8cc07d07ea364885613a34c4a1d70776754c2ea0b932fd5030` |
| audit with Amendments 1–2 | `b1c6d75` | `f343b25ba654931811198307deee3846f0289cf2d3a1bd507faeacd6da456e72` |
| Grok's report on Amendment 1 | `b1c6d75` | `4e72f4846ff6ef7a80f07651fa41b83276ef0f5b2a22da4d7e0897dbb434629d` |
| amendment-2 verifier | `b1c6d75` | `b6c68dc431aba0b21425b1e24a3329ffbe560e673250261c234e064d0dcff243` |
| repairs verifier | `63db34b` | `5a315b68b7f48ded51290408a256e2c7485e8edb22a8b0299fbcfc750c99b0e8` |
| reviewed verifier | `d0114b2` | `98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2` |

**Status:** Astra **REPAIR_REQUIRED** (two medium wording/attribution items).
All Amendment 2 figures are confirmed. Repairs applied as Amendment 3. Not
promoted.

## Execution

- **Authorization:** user «astra» (2026-11-26), as a brief separate from the
  channels contract.
- **Probe:** a one-line `codex exec` probe on `gpt-6-astra` returned "OK".
- **Run:** one sealed `revision-ciega astra` run, model `gpt-6-astra`, effort
  high, codex-cli 0.172.0. It ran 2026-11-26 12:07:54–12:12:38 UTC, status
  `COMPLETED`, exit 0.
- **Input:** input SHA256
  `4a767cdf6cb92e4aa42be9d2155bbf72e0428629e1b60aedd230147dfcb9d7e7`.
- **Output:** response SHA256
  `748185c2289586d5ad64e6f43f6513f5b916e713a085da261f227a7c3e5eed08`.
- **Raw files:** `reports/reviews/2026-11-26-dispersive-horizon-amendment2-astra/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.
- **Independence:** this is one cross-family agent review (author Claude,
  reviewer OpenAI). Astra could not run code.

## Verdicts

| Point | Astra |
| --- | --- |
| 1 Twin (−1, −1) at t = 3/8 | PASS |
| 2 Semisimplicity at the endpoints | PASS |
| 3 Cubic coefficient and G3 | PASS (branch choice and remainder are analytic) |
| 4 Edge equation, roots, endpoints | REPAIR_REQUIRED |
| 5(a) Jordan 3 + 1 versus 2 + 2 | PASS (proved by Astra: a chain of length 3) |
| 5(b) Curvature and defect at the interior edge | PASS (proved by Astra: Ω″ > 0, algebraic 2, geometric 1) |
| 6 New verifier | REPAIR_REQUIRED in documentation and scope; assertions correct by inspection |
| 7 Scope and attribution | REPAIR_REQUIRED |
| Global | **REPAIR_REQUIRED** |

## Objections and disposition

1. **Medium. "No root in [0, 1]" at t = 7/16.** The statement is true of the
   quotient, false of P_t, which vanishes at u = 1 for every t. **Upheld.**
   The verifier's assertion tests the quotient; the audit text and the
   amendment-2 docstring did not say so. The audit text and the README are
   repaired [A3]. The docstring is left unchanged, to keep reviewed bytes
   fixed, and its meaning is stated in the audit.
2. **Medium. "Ordinary band extremum" while Ω″ ≠ 0 was [UNVERIFIED];
   attribution to G4.** **Upheld.** Amendment 3 adds Astra's argument,
   checked by hand here:
   - P_t(u(k)) = sin²E · v(v + 2);
   - differentiating at k* gives P_t′(u*) u′(k*) = 2 sin²E Ω₊″;
   - the factor signs give Ω₊″ > 0.

   The verifier certifies the ingredients (B1–B3). The differentiation and
   the multiplicities are marked as written steps. G4 is credited only with
   the factorization and the root count.

Minor, accepted:

- G4 checked divisibility by (u − 1)² but not exactness. Amendment 3 adds J2:
  (u − 1)³ does not divide.
- G3 decides the series equation; the choice and existence of the branch are
  analytic, as Astra notes. This is noted in the audit text.

**What Astra adds, now certified or checked:**

- Jordan 3 + 1 at (±1, ±1), t = 3/8. Certified independently of Astra's chain
  argument, by exact ranks over ℚ(√6, √10): dim ker K^j = 2, 3, 4, 4 (J1).
- Ω₊″(k*) > 0 at the interior edge, a minimum, with algebraic multiplicity 2
  and geometric multiplicity 1. The ingredients are certified (B1–B3); the
  differentiation and multiplicity steps are written, by Astra, and checked
  by hand here.

## Outcome

Amendment 3 is applied. `scripts/verify_dispersive_horizon_transfer_amendment3.py`
passes 10/10 after the 61/61, 8/8 and 39/39 earlier checks, and no earlier
verifier bytes changed. At the user's request («SI, HAZ LA enmienda tres y
pasala a Astra»; «si quieres la envias tambien a Grok»), Amendment 3 goes to
Astra and Grok in two separate sealed briefs.
