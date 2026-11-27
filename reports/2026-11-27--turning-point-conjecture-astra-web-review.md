# Astra 6.2 (web) on the turning-point conjecture: statement repair

Date: 2026-11-27. Branch: `research/dispersive-horizon-channels`. Reviewed
note: `theory/DISPERSIVE_HORIZON_TURNING_POINT_CONJECTURE.md` at `73fc0b8`.

**Outcome:** Astra's verdict is `STATEMENT_REPAIRED_THEN_PARTIAL`.
- Three defects of the statement are found. Claude checked each of them in
  this session, and all three hold.
- The repaired statement is adopted as Amendment 1 of the note.
- No proof step (existence of S, outer region, inner region, matching) was
  attempted.
- The conjecture stays `OPEN`.

## Provenance

- **Route.** User: «es de Astra 6.2 por la web», 2026-11-27. It did **not**
  go through `revision-ciega`, so there is no sealed header, input SHA256, or
  model and effort record.
- **Prompt.** The prompt Claude gave the user is in
  `reports/reviews/2026-11-27-turning-point-conjecture-astra-web/prompt.md`.
  Whether it was sent verbatim, and with which attachments, is `[UNVERIFIED]`.
- **Response.** The verbatim text is in `informe_astra.md`, in the same
  folder.
- **Independence.**
  - This is a cross-family agent (OpenAI against Claude), not a human.
  - Astra proposed the observable T_ret in an earlier round.
  - Its text is not a source. Each claim below was re-derived or checked by
    Claude.

## Findings and checks

| # | Astra's claim | Claude's check | Status |
| --- | --- | --- | --- |
| 1 | φ(s) = tanh(s³)/16 meets the written hypotheses but has φ′(0) = 0, so X is undefined. Under x = L^{1/3}y, k = L^{−1/3}q the velocity term vanishes, so the inner problem changes. | φ′ = 3s² sech²(s³)/16 ≥ 0, zero only at s = 0, so φ is strictly increasing. The tail 1/16 − φ = 1/(8(e^{2s³} + 1)) ≤ e^{−2s}/8 for s ≥ 1. With φ ~ s³/16, the rescaled velocity term is O(L^{−4/3}). | Holds. Fix: require φ′(0) > 0. |
| 2 | (C3) must except both outgoing channels e and u. | The note's (C3) said that every entry other than R_u tends to 0, and that includes S_{e,r}, whose limit by (C1) is X > 0. The note was internally inconsistent. | Holds |
| 3 | (C4) «does not depend on γ(t_h)» is not meaningful within the fixed walk: all profiles cross t_h = 3/8, so γ_h = 35/32 is fixed. Whether γ_h cancels is a question for the inner problem. | γ(3/8) = 35/32 for this rule (`9e8cb5a`). Varying φ cannot vary γ_h. | Holds |
| 4 | The previous charter excluded existence and uniqueness of S («line 194»). | `theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md:194`: «existence or uniqueness of the scattering matrix for the tanh profile» is outside every verdict. | Correct |

Two precisions are also adopted:
- S defined modulo a localized state;
- channel labels e and u fixed by the low-k sheet that reaches k = 0 as
  ω ↓ 0.

## Disposition

- Amendment 1 is applied to the note and marked `[A1]`.
- The repaired statement is now the conjecture. Steps 2–5 of the proof route
  remain open.
- Not promoted. No verdict anywhere changes.
