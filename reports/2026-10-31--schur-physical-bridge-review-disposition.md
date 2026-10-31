# Schur physical bridge: independent review and disposition

Date: 2026-10-31. Branch: `research/schur-stability-audit`.
Base commit: `b934bc3d10fd855f27214a70c28519c98bf3c1db`.
Status: `INDEPENDENT_REVIEW_COMPLETED / CLARIFICATIONS_APPLIED_NOT_REREVIEWED`.
No global PASS or canonical promotion is recorded.

The continuation addresses only the pending review of the existing candidate.
H1 remains OPEN and paused; localization, a signed nonzero leader and AdS
are not opened or certified.

## Execution and frozen sources

The prior execution record documents the user's explicit request for Grok,
then Gemini if unavailable. The current instruction was to continue.
The bounded request allowed one Grok execution and one Gemini fallback.
Both used `revision-ciega` from herramientas commit
`ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.

Grok's execution was interrupted by the Codex server restart. The recovered
JSON contains 1773 events, no final result/error/done event and no text event.
The previous execution session was no longer available. No mathematical
verdict is attributed to Grok; partial provider output is not evidence.

Gemini completed normally, model returned `gemini-4-argon`, finish `STOP`,
2026-10-31 17:32:51–17:34:19 UTC. See the unedited
[review](../debates/2026-10-31--schur-physical-bridge-review/informe_gemini.md)
and [operational state](../debates/2026-10-31--schur-physical-bridge-review/estado_gemini.json).
One Google-family agent reviewed an OpenAI-authored candidate; this is not
human review or multi-member consensus. `COMPLETED` describes execution only.

The exact submitted document is the assembled frozen September dossier,
SHA256 `2c805293f8d3fbe6afb536fc7d6d09a0ef53b245856aaed4936faa134b591fb6`.
The wrapper's complete input has SHA256
`c4085e2a74e6496184bf1c05efc4ec56a6abf419c69af93db56ac6e1c13221a8`.
Before the clarifications, the current candidate had SHA256
`472c18154104530b15123c67e62d456f5b18a44bec79f4eeac1b4ae4b77e4534`;
its text and T1 match their embedded versions, ignoring outer whitespace.
The dossier's manuscript predates changes to the presentation of the twelve
Pauli pairs and four reference controls. The review covers the frozen text,
not a fresh certification of the current manuscript.

## Verdict and mathematical disposition

| Requested block | Gemini verdict |
| --- | --- |
| SCHUR_STABILITY | PASS |
| PHYSICAL_ENDPOINTS | PASS |
| PROPAGATOR_ERROR | PASS |
| SIGNED_REDUCTION | REPAIR_REQUIRED |
| CLAIM_CEILING | PASS |

Gemini accepts the current physical Alice and Bob endpoints and the absolute
bridge error. Its requested repair concerns absorbing the free terminal-Q
contribution when replacing the projected free functional by the full one.
The review is retained without editing, including its errors.

**Author disposition, not a second independent review:** the stated objection
that no N-independent constant bounds `rho^N` by `C_W/N` is false for fixed
`0<rho(W)<1`. With `a=-log(rho)>0`, differentiation gives
`d(x exp(-a x))/dx = exp(-a x)(1-a x)`, hence

\[
\sup_{N\ge2}N\rho^N\le\sup_{x\ge0}xe^{-ax}
=1/(ea)<\infty.
\]

A second elementary bound follows from positivity of the geometric series:
`N rho^N <= sum_{n>=1} n rho^n = rho/(1-rho)^2`.
Both constants are independent of N and may depend on W, as the candidate
already permits. No uniformity as W varies or shrinks is asserted.

The exact free reconstruction identity splits the full functional into
`2 exp(-K_*N) Re<v_+, R_P^N P s>` and its Q counterpart. The latter obeys
`C_(W,profile) N^-6 rho(W)^N exp(-K_*N)`, therefore
`O_(W,profile)(N^-7 exp(-K_*N))`. The original conclusion does not fail for
the reason alleged. Nevertheless the candidate now displays this identity,
the separate Q error, and the explicit absorption constant at (15) and
before (21). These are clarifications, with no change of hypotheses or powers.
The changed version has not been independently re-reviewed.

**Further review error:** in its Schur discussion Gemini writes the interior
subdominant modulus as at most `Lambda^-2`. This does not follow from
`|lambda(p)|<=Lambda`: inversion reverses the inequality. The sufficient
bound retained by the candidate is instead
`1/(Lambda inf_(p in closure W)|lambda(p)|)<1`, under T1's fixed admissible
window with `inf|lambda|>1`. This review sentence must not be used as a lemma.
Neither this correction nor the absorption calculation certifies the entire
proof afresh. The reported per-block verdicts remain those of the reviewer.

## Scope and checks

The original dossier, raw provider responses and unedited Gemini report are
preserved. The source manuscript, T1, observable and canonical gate ledger
are unchanged. No new numerical scan, external literature claim, publication,
commit or push is made. The local library index is absent in this checkout;
this task reviews the supplied frozen proof rather than adding literature.
Validation is the explicit absorption calculation above and `git diff --check`;
no scientific verifier was changed or rerun for these textual clarifications.
