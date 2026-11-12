# General infrared rate: second hypothesis diagnostic (walk-adapted regions)

2026-11-12. User: «si a las tres», approving the proposal to repeat the
diagnostic with a region rule adapted to each walk. Drafted and frozen by
Claude (claude-opus-5-5). **Status: OPEN; frozen; one diagnostic run
authorized.** Diagnostic only: floating point, no verdict on the theorem,
no promotion, no external transmission.

## Known, question, abandonment

Known: the sixteen-walk report (`reports/2026-11-12--general-ir-rate-sixteen-walks.md`)
and its two declared design faults (regions inside the IR cone; minimiser
assumed on an axis). The general theorem: charter `GENERAL_IR_RATE_GATE.md`
with Amendments 1–4, Stages 1–2 PASS in one sealed Grok review.

Question: with regions placed in the non-ballistic corona of each walk and
the true minimiser, which hypotheses hold, and in particular, does
zero momentum stay dominant (H4′) when the walk has ballistic modes faster
than `c_IR` along the direction of Bob?

No abandonment criterion: one run. A failed hypothesis is not a
counterexample to (T) or to anything else.

## Walks

The same sixteen walks (W1–W6, Z1–Z10), same constructors, same vertex `V`
and direction `n = V/|V|` as in the first runs (including the declared
fallback when no rate axis exists).

## Region rule (fixed before computing)

`s_0 = d/dt Phi(t n)` at `t = 10^-3` (extent along `n` of the zero set of
the rate; `s_0 > c_IR` exactly when there are faster ballistic modes along
`n`). `h = n.V = |V|`. If `s_0 >= h`: label `NO_CORONA_ALONG_N`, stop the
row. Otherwise Alice is the ball of radius `rho = (h - s_0)/4` at the
origin and Bob the ball of the same radius at `V`; the nearest point of
`B - A` along `n` is then at `(s_0 + h)/2`, half-way between the ballistic
region and the causal boundary.

## True minimiser

`xi_*` solves `grad Phi(xi) + 2 rho xi/|xi| = V` (the minimiser of `I` on
the ball `B - A` lies on its boundary with inward normal along `xi_*`),
by Newton's method started on the axis; `v_* = grad Phi(xi_*)`,
`K_* = xi_*.v_* - Phi(xi_*)`. The residual is reported. `H3` is then
checked numerically: `xi_*` parallel to a dual-lattice vector with
components of modulus at most 12 (tolerance `10^-6`). `H9` holds exactly
when `xi_* || n` (then `theta^A_N = theta^B_N`) provided `rho |u|` is
irrational, which is not checked for the numerical `rho` and is reported as
generic. All other hypotheses as in the first runs, at the true `xi_*`.

## Execution

`scripts/diagnose_general_ir_rate_round2.py`, committed before its
recorded run; imports the two first-run scripts read-only. Output JSON and
stdout in `reports/`.
