# Explicit signalling witness in the declared CAR lift

## Scope fixed before evaluation — 2026-09-16

Authorized by the user's instruction to close the signalling result as a
theorem/witness before considering an experiment. This is a finite existence
certificate, not a reopening of the optimal-D or experimental gates.

- Model: the existing free-fermion CAR lift of CJWW (5.15), unchanged;
  `c_IR = 1`, `C_micro = [-1,1]^3`.
- Convention: `K_t(x,z) = (W^t)_{x,z}`, with Laurent block at displacement
  `x-z`; `alpha_t(n_z) = dGamma(W^t P_z W^{t dagger})`. Thus the
  corresponding one-particle Schrodinger evolution is `W^{t dagger}`.
- Alice: site `0`, two internal modes; choices `U_0 = I` and
  `U_1 = exp(i pi n_0)`, applied at time zero.
- Time and Bob: `t = 2`, `y = (2,2,2)`, the existing vertex geometry.
- Preparation, identical before either choice: exactly one particle in
  `psi = (|0,down> + |y,down>)/sqrt(2)`, with all other modes vacant;
  `down = (0,1)^T`. Preparation is assumed available before the choice.
- Bob's measurement: the local even projection `E_y` onto non-vacuum at
  site `y`. On the one-particle sector this equals total occupation `n_y`.
- Target: an exact strictly positive difference between the two probabilities
  of `E_y`, hence a lower bound on trace distance, without optimizing it.
- Controls: the same phase gate on an Alice-localized particle; removal of
  the preparation's spatial coherence; and the existing axial point
  `(3,0,0)` at `t = 2`.
- Method: exact Laurent coefficients and rational matrix arithmetic; no
  parameter search, asymptotic inference, new dynamics or resource scaling.

The vertex is **on** the microscopic boundary, not in its strict interior.
The witness must state membership of the exact causal support, not the strict
inequality `L < v_sub t`. Alice and Bob each have two local fermionic modes;
this does not establish the original gate's `N = M = 1` optimization claim.

Status before evaluation: **PENDING EXACT CERTIFICATE**.

## Theorem — exact finite existence witness

**Resource hypothesis and conclusion boundary.** Before Alice chooses her
operation, the prescribed state already has spatial coherence between Alice
and **Bob's own site**. This pre-existing distributed preparation is a
hypothesis of the theorem. The conclusion is that Alice's subsequent local
choice changes Bob's measurement probability. It does **not** establish that
this operational channel can be created starting from resources initially
localized around Alice; no such preparation protocol is provided.

Under precisely the preparation, dynamics and measurement above, the two
choices give

\[
p_0=\frac{121}{512},\qquad p_1=\frac{169}{512},\qquad
\Delta p_B=|p_1-p_0|=\frac{3}{32}>0.
\]

Writing `rho_B^(b)` for the local two-mode Fock state after choice `b` and
two time steps, this implies

\[
D(\rho_B^{(0)},\rho_B^{(1)})
=\tfrac12\|\rho_B^{(1)}-\rho_B^{(0)}\|_1
\ \geq\ \Delta p_B=\frac{3}{32}>0.
\]

This is a lower bound obtained with a specified measurement, not an
optimization over measurements, preparations or interventions.

### Proof

Let `|x,s>` denote a one-particle site/internal basis state. Equivalently, on
Fock space the common preparation is

\[
|\Psi\rangle=
\frac{a^\dagger_{0,\downarrow}+a^\dagger_{y,\downarrow}}{\sqrt2}
|\Omega\rangle.
\]

It has fixed particle number one. Its density operator respects fermion
parity superselection. The gate `exp(i pi n_0)` is local, even, unitary and
number conserving; in the local basis `(vacuum, up, down, up-down)` it is
`diag(1,-1,-1,1)`. There is no postselection. The state is the same before
either freely selected intervention, and the two post-choice vectors are

\[
|\psi_b\rangle=
\frac{(-1)^b|0,\downarrow\rangle+|y,\downarrow\rangle}{\sqrt2}.
\]

Using the declared Heisenberg convention, the Bob amplitude after evolution
by `W^{2 dagger}` is

\[
v_b=\frac{(-1)^b K_2(0,y)^\dagger\downarrow
                    +K_2(y,y)^\dagger\downarrow}{\sqrt2}.
\]

The exact Laurent coefficients of the existing symbol give

\[
K_2(0,y)=\begin{pmatrix}0&0\\0&1/16\end{pmatrix},\qquad
K_2(y,y)=-\frac34 I_2.
\]

These coefficients also follow directly from the symbol. Its entries are
`a = cos(p1) cos(p2) exp(i p3)`, `d = cos(p1) cos(p2) exp(-i p3)`,
`b = -cos(p1) sin(p2) + i sin(p1)`, and
`c = cos(p1) sin(p2) + i sin(p1)`. In `W^2`, only `d^2` contributes to the
coefficient at `(-2,-2,-2)`, giving `1/16` in the down-down entry.
The constant coefficient of `bc = -cos(p1)^2 sin(p2)^2 - sin(p1)^2` is
`-1/4 - 1/2 = -3/4`. The other diagonal terms have nonzero `p3` exponent,
and the off-diagonal terms have `p3` exponent `+1` or `-1`, so there are
no further constant contributions.

Consequently

\[
v_0=-\frac{11}{16\sqrt2}\downarrow,\qquad
v_1=-\frac{13}{16\sqrt2}\downarrow.
\]

Bob measures `E_y = I - |vacuum_y><vacuum_y|`, an even local projection
with `0 <= E_y <= I`. In the sector used here its event probability is
`p_b = ||v_b||^2`, yielding the fractions above. More explicitly,

\[
\rho_B^{(b)}=(1-p_b)|\mathrm{vac}\rangle\langle\mathrm{vac}|
                         +v_bv_b^\dagger,
\]

where the second term lies in Bob's one-particle internal subspace and the
two-particle block is zero. The variational bound for trace distance,
`|Tr(E (rho_1-rho_0))| <= D` for any effect `0 <= E <= I`, proves the
stated lower bound. No claim of measurement optimality is needed.

**Normalization matters.** Total occupation `n_y` has norm two on the full
two-mode local Fock space. It agrees with `E_y` on these states, but is not
itself a norm-one effect on arbitrary states. The bound above uses `E_y`.

### Spacetime location and controls

Here `|y| = 2 sqrt(3) > c_IR t = 2`. The nonzero block `K_2(0,y)` places Bob
in the exact causal support of the dynamics; `y` is a vertex of
`t C_micro = [-2,2]^3`. This is outside the emergent cone and **on the
microscopic boundary**, not strictly inside that boundary.

- For a particle entirely at Alice, `U_1|0,down> = -|0,down>` is a global
  phase: the two full density matrices coincide before and after evolution.
  The vacuum is also invariant under both the phase gate and the dynamics.
- Replacing the coherent preparation by the equal mixture of `|0,down>` and
  `|y,down>` also gives identical full density matrices under the two choices.
  Coherence is necessary for this particular phase protocol; this says
  nothing about every other admissible intervention.
- At the declared axial control `y_ax = (3,0,0)`,
  `K_2(0,y_ax) = 0` exactly. Bob's evolved local generators have no component
  at Alice, so an even unitary at Alice commutes with the evolved Bob algebra.
  Hence `D = 0` for any initial state and either local unitary choice there.
  The verifier also checks equality of the full axial reduced states for
  this preparation.

### What this closes, and what remains open

**Final status: EXACT SIGNALING WITNESS ESTABLISHED.** The algebraic proof is
backed by [the exact verifier](../scripts/verify_signaling_witness.py), which
passes 17/17 checks using rational and symbolic arithmetic. This is not an
independent review or a full PASS of the original optimal-D contract.

Canonical claim, for this branch:

> In the declared free-fermion lift, given a state prepared with spatial
> coherence between Alice and Bob's own site before Alice's choice, that local
> choice changes a measurement probability
> accessible to Bob outside the emergent relativistic causal cone and within
> the exact microscopic causal support. Thus the two choices are
> distinguishable in principle. This does not establish Bob's optimal
> measurement, a globally optimal protocol, preparation of the operational
> channel from resources initially localized around Alice, or experimental
> feasibility.

The two arms in this certificate start at Alice and **at Bob's site**. Thus
the earlier suggestion that Bob plays no role in the required resource is
not a conclusion of this construction. No Bell protocol is modelled.
Preparation of this spatially extended state must precede Alice's choice;
its preparation cost and any possible laboratory realization are unanalysed.

The exact interference contribution is
`-2 Re(down^dagger K_2(0,y) K_2(y,y)^dagger down) = 3/32`.
This is a finite, geometry-specific value, not an asymptotic scaling theorem
in either kernel. No large-time exponent, channel capacity, multi-mode
amplification, physical speed beyond the model's causal support, or claim
about our universe follows. The experimental problem remains unopened.
