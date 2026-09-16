# COUPLING_MAP_OPTIMAL_D — outcome (stop rule applied)

**Contract:** [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md), frozen at `0f7628d`. Contract and the four declared geometries **unchanged**.
**Verifier:** [`verify_directional_saturation.py`](../scripts/verify_directional_saturation.py), 27/27.
**Stop rule applied at the first classifiable result: H1 and H2 classified, H3 and H4 NOT REACHED.**

## 1. Structure

With `P = W^t P_y W^{t†}` and a number-conserving Gaussian local operation of
Alice acting as `R` on the site-0 one-particle space, the difference operator
`Δ = u†Pu − P` has blocks

`Δ₀₀ = R†P₀₀R − P₀₀`, `P₀₀ = K_{0,y}K_{0,y}†` → order `‖K_{0,y}‖²`
`Δ_{0w} = (R†−I)P_{0w}`, `P_{0w} = K_{0,y}K_{w,y}†` → order `‖K_{0,y}‖·‖K_{w,y}‖`

Two different powers of the small kernel. `⟨Δ⟩` picks up `Δ_{0w}` only if the
state carries coherence between site `0` and site `w`.

## 2. The optimal probe

**Alice's optimal operation is the local phase gate `U = exp(iπn₀)`**, i.e.
`R = −I`. Then exactly

`Δ₀₀ = 0` and `Δ_{0w} = −2P_{0w}`.

It **annihilates** the local term and **doubles** the coherence term.

## 3. Results at the declared geometries

| `t` | geometry | `‖K_{0,y}‖` | coherent max | local-only max | gain |
| --- | --- | --- | --- | --- | --- |
| 2 | vertex ray | 6.25e-2 | 9.38e-2 | 3.91e-3 | 24× |
| 3 | vertex ray | 1.56e-2 | 1.17e-2 | 2.44e-4 | 48× |
| 4 | vertex ray | 3.91e-3 | 3.30e-3 | 1.53e-5 | 216× |
| 5 | vertex ray | 9.77e-4 | 5.19e-4 | 9.54e-7 | 544× |
| 2–5 | face-diagonal | — | `Θ(‖K‖)` | **exactly 0** | ∞ |
| 2–5 | nearest off-axis | — | `Θ(‖K‖)` | **exactly 0** | ∞ |
| 2–5 | **axial control** | **0** | **0** | **0** | — |

`coherent/‖K‖ ∈ [0.53, 1.5]` (O(1)); `local/‖K‖² = 1.0000`. The gain grows like
`1/‖K‖`, i.e. exponentially in `t`.

## 4. Classification

**H1 — CONFIRMED, conditionally.** `max D = Θ(‖K_{0,y}‖)`, so the single-particle
kernel is the tight figure of merit — **but only** for states carrying coherence
between Alice's site and a site `w` with `K_{w,y} ≠ 0`. Without it,
`max D = Θ(‖K_{0,y}‖²)`, quadratically worse.

**H2 — CONFIRMED and sharpened.** The required resource is **not occupation at
`A`** but **coherence between `A` and the interior**. A particle sharply
localized at Alice's site is the *worst* case, not the best. Stronger still: at
the face-diagonal and nearest-off-axis geometries `P₀₀` is a multiple of the
identity, so the local term vanishes for **every** operation — there the
coherence is **necessary**, not merely advantageous.

**Axial control passes**: `K_{0,y} = 0` ⟹ `Δ ≡ 0` ⟹ `D = 0` for every state and
every operation, as the contract demanded.

**H3 (Bell protocols not optimal) — NOT REACHED.** The structure hints at it:
the resource that matters is `A`–interior coherence, not `A`–`B` entanglement,
and `B` plays no role in the resource. That is a *hint*, not a result; no Bell
protocol was modelled. Stop rule applied.

**H4 (amplification exponent `p`) — NOT REACHED.** Stop rule applied.

## 5. Declared asymmetry (contract Sec. 6)

PASS required achievability **and** a matching upper bound. Achievability is
solid: an explicit phase gate plus a two-site coherent one-particle state, with
the state aligned to the top singular vectors of `Δ_{0w}`. The upper bound is
**only over number-conserving Gaussian local operations**. Pairing (Bogoliubov)
terms and genuinely non-Gaussian even operations at the site were not covered.
So the gate returns **achievability + a restricted upper bound**, and the map is
recorded as such, not claimed in full.

## 6. Consequence for Sec. 8.11

The transfer that was blocked is now partly unblocked *in principle*: the figure
of merit is `‖K_{0,y}‖ × ‖K_{w,y}‖` with a phase-gate probe on a coherent state.
It remains blocked *in practice* until H3 settles whether a Bell-type protocol
realizes anything like this — which the stop rule left open.
