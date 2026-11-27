# Grok review of Amendment 1 (dispersive-horizon transfer-matrix audit)

Date: 2026-11-26. Branch: `review/dispersive-horizon-transfer-audit`.

**Reviewed snapshot** (base `63db34b`):

| Document | Commit | SHA256 |
| --- | --- | --- |
| `amendment1.diff` (`git diff d0114b2 63db34b` of the audit) | — | `f5e3387cd2b4c6df56dba70066d70669f340016c991cb9eedfd2a547d280fe34` |
| audit with Amendment 1 | `63db34b` | `838cc16f09872206e00ea27173d9f0ed078297dfabc465c63da8b14824ce6c3b` |
| Astra's report | `63db34b` | `49f77a0054bed8abf7821cb4693896c1c2e01398de4a54239c57bd2506315da9` |
| repairs verifier | `63db34b` | `5a315b68b7f48ded51290408a256e2c7485e8edb22a8b0299fbcfc750c99b0e8` |
| reviewed verifier | `d0114b2` | `98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2` |

**Status:** Grok **REPAIR_REQUIRED** on Amendment 1. Every figure in
Amendment 1 is confirmed; the repairs concern attribution and completeness.
Repairs applied as Amendment 2. Not promoted.

## Execution

- **Authorization:** user instruction «pide a Grok que revise la enmienda 1».
- **Probe:** generation was checked beforehand with a one-line `grok --model
  grok-4.7 -p` probe, which returned "OK", exit 0.
- **Run:** one sealed `revision-ciega grok` run, model `grok-4.7`, CLI default
  effort, sealed as Sanedrín's CIRO member (grok 1.0.34). It ran 2026-11-26
  10:54:01–11:10:13 UTC, status `COMPLETED`, exit 0, with 0 attempted tool
  calls.
- **Input:** input SHA256
  `4d372a14676d6e78d4936b5da27f2dd388e55eee52b26f99659d137b962f2ff0`.
- **Output:** response SHA256
  `0ac67e3da1c5de983cf658ea6459915e08b295017f518ab4272668eb21c4de03`.
- **Raw files:** `reports/reviews/2026-11-26-dispersive-horizon-amendment1-grok/`.
- **Tools commit:** `4a4fccaecc259da07956a30c50ea620f7e21ebd9`.

**Independence.** Amendment 1 was written by Claude and reviewed by xAI. This
is one cross-family agent review, not human review. Grok could not run code,
so the reported executions are `[UNVERIFIED]` in its report.

## Verdicts

| Point | Grok |
| --- | --- |
| 1 Multiplicity at zero velocity (4/2 at t = 3/8; 2 at the endpoints) | PASS |
| 2 Wording on zero group velocity, completeness | REPAIR_REQUIRED |
| 3 T3 count (21 sites) | PASS |
| 4 "Admissible θ, z ≠ 0" | PASS |
| 5 Repairs verifier decides what it says | PASS (execution UNVERIFIED) |
| 6 Scope of Amendment 1 and of the Astra record | REPAIR_REQUIRED |
| Global | **REPAIR_REQUIRED** |

**What Grok derives by hand:**

- the series f = 1 − k²/8 − (13/48)k⁴ at t = 3/8, giving β = 35/64 and
  Ω₊ = (35/32)k³ + O(k⁵), so Astra's coefficient is correct;
- the transfer of contact order 3 + 1 to the characteristic polynomial;
- the geometric multiplicity 2 from U(0) = I and the bijection;
- the 21-site count;
- the admissible domain;
- a line-by-line inspection of the repairs verifier. It found no false-PASS
  path: the multiplicity loop fails closed, nonzero_alg(0) is false, and
  importing the reviewed verifier does not mask failures.

## Objections and disposition

Each was checked exactly before acting. The inspection reproduced every
number below, and Amendment 2 now certifies them.

1. **High. Attribution.** Amendment 1 attributed "Ω₊ ~ k³" and the vanishing
   velocity to R2/R3, which certify only multiplicities. **Upheld.**
   - The attribution is fixed.
   - The k³ coefficient is now certified (amendment-2 verifier G3).
   - The vanishing infrared velocity is T8 of the reviewed verifier.
2. **High. Twin degeneracy.** At t = 3/8, (z, λ) = (−1, −1) also has algebraic
   multiplicity 4 and geometric multiplicity 2. **Upheld** (G1). Added to the
   audit [A2].
3. **Medium. Endpoints and ordinary band edge.** **Upheld** (G2, G4); added
   [A2].
   - At t = 5/16 and t = 7/16, the roots at (±1, ±1) are semisimple, with
     algebraic and geometric multiplicity both 2. R3 had certified only the
     algebraic multiplicity.
   - At t = 5/16, the outgoing branch has an ordinary zero-velocity point in
     (0, π/2), from 2625w² + 5w − 16 = 0 with discriminant 168025. At
     t = 7/16 there is none.

## Not verified here

- Grok's statement that the Jordan partition at the horizon is 3 + 1.
- That the t = 5/16 band edge gives a non-semisimple double root, which needs
  Ω″ ≠ 0 there.

Both are marked `[UNVERIFIED]` in the audit.

## Outcome

Amendment 2 is applied and certified by
`scripts/verify_dispersive_horizon_transfer_amendment2.py`, 39/39 after the
61/61 reviewed and 8/8 repair checks. The earlier verifiers' bytes are
unchanged.

The brief allowed one round, so Amendment 2 has not been reviewed.
`state/CURRENT_STATE.md` and `README.md` are unchanged. TRANSMISSION remains
OPEN.
