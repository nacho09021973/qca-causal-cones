# COUPLING_MAP_OPTIMAL_D — corrected outcome and exact witness

**Contract:** [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md), frozen at
`0f7628d`. The original optimization contract is **PARTIAL / NOT CLOSED**.
The separate finite existence task is **CLOSED WITH AN EXACT WITNESS**; see
[`COUPLING_MAP_SIGNALING_WITNESS.md`](../theory/COUPLING_MAP_SIGNALING_WITNESS.md).

**Correction, 2026-09-16.** The original report identified an occupation
witness with the full trace-distance optimization and inferred asymptotic
scaling from four times. Those conclusions are withdrawn. The user's accepted
claim ceiling is existence of distinguishability in the declared CAR lift,
without optimality or experimental feasibility.

## 1. Exact construction

At `t = 2`, with Alice at `0` and Bob at `y = (2,2,2)`, prepare

`psi = (|0,down> + |y,down>)/sqrt(2)`.

Alice chooses `I` or `exp(i pi n_0)`. Under the already declared convention
`alpha_t(n_y) = dGamma(W^t P_y W^{t dagger})`, states evolve by
`W^{t dagger}`. Bob measures the even local non-vacuum projection `E_y`.
Exact kernel blocks give

`K_2(0,y) = diag(0,1/16)`, `K_2(y,y) = -3 I/4`,

`p_0 = 121/512`, `p_1 = 169/512`, **`Delta p_B = 3/32 > 0`**.

Because `0 <= E_y <= I`, **`D(rho_B^(0),rho_B^(1)) >= 3/32`**. The
construction proves this lower bound; it does not optimize `D`. Total
occupation equals this projection on the prepared one-particle sector, but
has norm two on the full two-mode Fock space, so the effect normalization is
explicit in the theorem.

Bob is outside the emergent ball (`|y| = 2 sqrt(3) > 2`) and **on** the
microscopic boundary, with a nonzero exact kernel. This proves membership in
the causal support, not strict interior membership. The coherent preparation
must exist before Alice's choice. In this example its second arm is at Bob's
site, so no conclusion excluding Alice-Bob coherence or Bell resources follows.
This distributed preparation is a hypothesis of the theorem: the witness
does not establish creation of the operational channel from resources
initially localized around Alice.

Verifier: `python3 scripts/verify_signaling_witness.py` — **17/17 exact checks**.
It checks both evolved states, the full local reduced density matrices, the
probabilities, the interference identity and the controls.

**Status: EXISTENCE_WITNESS_PROVED / INDEPENDENTLY_REVIEWED.** The
[independent review](2026-09-16--signaling-witness-independent-review.md) gives
PASS on the four requested points, with no mandatory repairs. It records
the frozen input hashes and checks the analytic probabilities, correspondence
with the code, causal location, and the trace-distance convention. This is
one separate agent's review, not external human review or consensus. The
reviewed theorem and both scripts are unchanged after review.

The updated legacy verifier `python3 scripts/verify_directional_saturation.py`
also passes **27/27 checks**. Its finite occupation diagnostics are now tagged
SUPPORTED and make no optimality or asymptotic claim.

## 2. Which earlier algebra survives

For `P = W^t P_y W^{t dagger}` and a number-conserving Gaussian intervention
acting as `R` at Alice, the occupation difference operator has blocks

`Delta_00 = R^dagger P_00 R - P_00`, `P_00 = K_0y K_0y^dagger`,

`Delta_0w = (R^dagger-I) P_0w`, `P_0w = K_0y K_wy^dagger`.

For the phase choice `R = -I`, `Delta_00 = 0` and
`Delta_0w = -2 P_0w`. These identities survive. They certify a mechanism,
not an optimum over all interventions and all Bob measurements, even within
the number-conserving Gaussian class.

A particle entirely at Alice acquires only a global phase under this gate,
so its signal is **exactly zero**. A quadratic occupation response can arise
from other local internal rotations; it is not the response of this phase
gate on that preparation. Removing coherence from the specified two-site
preparation also eliminates the signal of this protocol.

If `P_00` is scalar, the occupation response of an Alice-localized particle
vanishes for every such internal rotation. This does **not** prove equality
of all Bob reduced states: an internal-state measurement might distinguish
them. Similarly, a nonzero occupation witness proves `D > 0` but neither
determines `D` nor gives its optimal measurement.

The axial zero has a stronger cause: `K_0y = 0` removes Alice from the support
of the evolved Bob algebra. Even local Alice unitaries cannot signal there,
for any initial state. This is not an inference from a vanishing occupation
response alone.

## 3. Historical finite table — descriptive values only

These are the previously reported vertex values. The coherent column is
`max_w 2 ||K_0y K_wy^dagger||`, an occupation-witness construction with
suitable internal vectors, not the global maximum of `D`. The local column
came from sampled internal unitaries and its displayed precision does not
constitute an exact maximization certificate.

| `t` | kernel norm | coherent occupation construction | sampled local occupation response | reported ratio |
| --- | --- | --- | --- | --- |
| 2 | 6.25e-2 | 9.38e-2 | 3.91e-3 | 24x |
| 3 | 1.56e-2 | 1.17e-2 | 2.44e-4 | 48x |
| 4 | 3.91e-3 | 3.30e-3 | 1.53e-5 | 216x |
| 5 (outside frozen times) | 9.77e-4 | 5.19e-4 | 9.54e-7 | 544x |

The old code evaluated `t = 5` despite the frozen list `{2,3,4}`. This is
recorded as a scope deviation, not retroactively authorized evidence. Active
legacy checks now use the frozen times only. The new exact certificate uses
only `t = 2`. The numbers above support no universal `Theta(||K||)` or
`Theta(||K||^2)` law, exponential gain theorem or matching upper bound on `D`.
Both kernel arms and their internal alignment matter.

## 4. Corrected status and remaining limits

- **Existence of signalling:** established by the exact finite witness above.
- **H1, optimal-D kernel scaling:** the previous conditional confirmation is
  withdrawn; the requested optimization and asymptotic claim remain OPEN.
- **H2:** preparation dependence is established for the explicit phase
  protocol, including the vacuum, localized and dephased zero controls.
  Necessity of coherence for every admissible protocol is not established.
- **H3 and H4:** NOT REACHED. No Bell protocol, resource-amplification law or
  experimental coupling map has been supplied.
- **Optimality:** no matching upper bound on the full `D` optimization is
  certified here, including in the restricted Gaussian class. Pairing and
  non-Gaussian operations remain outside the calculation.

The theorem concerns the declared free-fermion lift, not the one-particle walk
without its local observable algebras. It makes no claim about our universe,
experimental feasibility, large-time rates or channel capacity. Establishing
this finite witness does not close the original optimal-D gate or open the
experimental problem.
