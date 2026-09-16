# SUBSTRATE_CONE_OBSERVABILITY — outcome

**Contract:** [`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](../theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md), frozen at `d86b018` before solving.
**Verifier:** [`scripts/verify_directional_saturation.py`](../scripts/verify_directional_saturation.py), 23/23 fail-closed.
**Result: H1–H4 all CONFIRMED. `D > 0`, exponentially small, and strictly off-axis.**

## 1. The lift makes the question well posed, and then trivializes it

For the free-fermion lift declared in the contract, on the one-particle sector
the Bogoliubov automorphism gives `α_t(n_x) = W^t P_x W^{t†}`. Hence for `y' ≠ y`

`[α_t(n_x), n_y]` has `(y,y')` block `= (W^t)_{y,x} ((W^t)_{y',x})†`,

so the commutator is nonzero exactly when the single-particle kernel
`(W^t)_{y,x}` is (given `W^t` populates at least two sites, true for `t ≥ 1`).
**H1 CONFIRMED, analytically.** The operational causal structure of the lift is
therefore the strict support of `W^t` — the object already certified in
`CURRENT_STATE.md` Sec. 8.5. No Lieb–Robinson machinery is needed.

Kernels computed in exact Gaussian integers (`4·W_x ∈ M_2(Z[i])`).

## 2. The answer

| | | |
| --- | --- | --- |
| `L > v_sub(n̂) t` | commutator **exactly 0** | outside `C_micro`; H4 |
| `ct < L < v_sub(n̂) t`, off-axis | commutator **≠ 0**, `∝ 4^{-t}` at the vertex rays | H2 |
| `L > ct`, **on-axis** | commutator **exactly 0** | `v_sub(ê_i) = c`; H3 |

At `t = 3` the strict support has 148 sites, of which **108 lie strictly outside
the emergent light cone** `B(c)t`, every one of them inside `C_micro t` and
**none of them axial**. The effect is not a measure-zero artefact and it is not
isotropic.

So, for the frozen question `ct < L < v_sub(n̂)t`:

> `D > 0`, exponentially small in `t`, and possible only in non-axial directions.

This is the signature the contract asked for: **fundamental causality outside the
light cone with no superluminal ballistic propagation**, carrying the angular
fingerprint `v_sub(n̂) = ‖n̂‖₁ c` of the substrate.

## 3. What this does and does not say

- **Scope of the object.** Every statement is about the **free-fermion lift** of
  CJWW (5.15), not about the one-particle walk, for which these quantities are
  undefined (contract Sec. 1).
- **Commutator vs protocol.** A nonzero commutator means the algebras fail to
  commute, hence *there exists* an intervention and a state with `D > 0`. A
  specific protocol's `D`, and any channel capacity, were **not** computed.
- **Rate, not just sign.** `4^{-t}` is the vertex-ray magnitude. How the
  suppression varies over `C_micro \ B(c)` is the anisotropic `I(v)` question,
  which remains **NOT_AUTHORIZED**.
- **Upper-bound discipline.** Nothing here upgrades CJWW's one-sided bounds.
- **Our universe.** No claim. `CURRENT_STATE.md` Sec. 8.9(iii) stands at UNKNOWN,
  and the falsifiability asymmetry of contract Sec. 4 stands: a wider cone fully
  decoupled from accessible observables would be invisible to any experiment, so
  no null result can establish exact coincidence.
- **No data survey.** LIV dispersion bounds, threshold processes and sidereal
  searches remain out of scope pending a further charter.
