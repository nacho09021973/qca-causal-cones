# Delayed (3,-2) bridge: partial formal attempt

2026-11-17. Codex/OpenAI. Preregistration 92e5fc8.
Status OPEN_MISSING_BOUND; physical bridge not proved or formalized.

The exact requested physical statement is in the gate: freely evolved
pair modes at t_a=2 floor(27L/2), evolution to t_b=28L, target
V(a(3)/a(-2)), creation order (fast,spectator). No change of frame or
geometry was made. The earlier pair theorems do not instantiate it directly.

A permanent Lean helper in formal/ThirringWindow/Transfer.lean was compiled
using the existing pinned formal/ environment. For any seminormed additive
group and distance-preserving U it proves
||U x-target|| <= eIn+eOut from ||x-y||<=eIn and
||U y-target||<=eOut. This is precisely the transfer step that would apply
to an exact scattering comparison state. The hypotheses are explicit.
It does not construct such a state or prove either physical bound.
Successful output and the first failed build are retained in that directory.
No reviewed verifier changed. No new own axioms or sorry in the source.

Essential open obligation: construct the (3,-2) comparison state over the
whole momentum support and establish both wrong-side bounds in the delayed
frame, including its phase variation and normalization. Reusing two-particle
formulas without this construction would assume the desired bridge. The
Lean helper is insufficient to close that obligation. No physical verdict
PASS is issued and no general F follows.

This attempt stops OPEN_MISSING_BOUND under its contract. A full Lean
formalization additionally needs the physical spaces, operators and integral
construction; none is supplied by the helper. No claim is made that such a
formalization is impossible. No external review or promotion performed.
