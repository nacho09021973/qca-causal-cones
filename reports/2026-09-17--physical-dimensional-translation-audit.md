# PHYSICAL_DIMENSIONAL_TRANSLATION — dimensional audit

**Contract:**
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](../theory/PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md),
frozen at `fca5881` before this audit.

**Verdict: `DIMENSIONAL_MAP_CONDITIONAL`.** A consistent physical-units
dictionary exists, but the checked model fixes neither an absolute lattice
spacing nor an update time. Consequently `3/128` is an exact dimensionless
operational prediction of the declared protocol, not a parameter-free
prediction of a dimensionful magnitude in SI units.

## 1. What the primary sources fix

CJWW define the one-particle Hilbert space as `l2(Z^s) tensor K`, with position
operator `(Q_alpha psi)(x) = x_alpha psi(x)` (Sec. 2.1), integer powers `W^t`
for discrete time, and Fourier convention

`psi_hat(p) = sum_x exp(-i p.x) psi(x)`, `p in [-pi,pi]^s` (Eq. 2.1).

They diagonalize a discrete-time walk as
`W(p) = sum_j exp(-i omega_j(p)) P_j(p)`, explicitly noting that `omega_j` is
defined modulo `2 pi` (Sec. 2.2, Eq. 2.10), and define group velocity as
`partial omega_j / partial p_alpha` (Eq. 2.11). Their (5.15) is a model on the
same dimensionless cubic lattice, with `|grad omega| <= 1` and the same
conical points as the lattice Weyl construction (Sec. 5.4).

Thus CJWW fix a discrete normalization, not a physical cell size or clock
period. No value of either scale is specified in the checked source.

The antecedent Bialynicki-Birula construction makes the dimensional restoration
explicit: lattice sites have `r = (i,j,k) a`, evolution advances by `Delta t`,
and its continuum Weyl matching uses `a = c Delta t` (Sec. II, Eqs. 1--3 and
the product construction preceding Eq. 16). It also writes the one-step
operator as `W(k) = exp(-i H(k) Delta t)` (Eq. 32) and notes the resulting
energy ambiguity by multiples of `2 pi/Delta t`. This supplies the form of the
dictionary, but it does not numerically determine `a` or `Delta t` for nature.

## 2. The dimensional dictionary

Let `a > 0` be the physical coordinate spacing and `tau > 0` one complete
update time. The conventions above give

| Dimensionless quantity | Physical interpretation |
| --- | --- |
| `n in Z^3` | `x = a n` |
| `N` updates | `t = N tau` |
| `p in [-pi,pi]^3` | `k = p/a`, hence `k_i in [-pi/a,pi/a]` |
| eigenphase `omega(p)` | quasienergy `E = hbar omega(p)/tau` modulo `2 pi hbar/tau` |
| `grad_p omega` | velocity `(a/tau) grad_p omega` |

Since the exact low-energy slope of (5.15) is `c_IR = 1` in lattice-step
units, its physical value is

`c_IR^phys = a/tau`.

Identifying this with an observed relativistic speed `c_phys` imposes
`a = c_phys tau`. It calibrates one ratio; it is not a prediction of `a`,
`tau`, or either absolute cutoff scale. The one-parameter family
`(a,tau) = (c_phys tau,tau)` remains.

## 3. Conditional spacetime translation of the frozen protocol

The message is chosen after two common preparation updates and read after one
further update. Therefore, conditionally on `(a,tau)`:

- preparation duration: `2 tau`;
- encoding-to-readout duration: `tau`;
- total initialization-to-readout duration: `3 tau`;
- Bob displacement at every non-corner site: `a(+-1,+-1,0)`;
- Euclidean separation from the encoding site: `L = sqrt(2) a`;
- microscopic coordinate support condition: `||y||_infinity a = a` in one
  update.

If `a/tau = c_phys`, then
`L/(c_phys tau) = sqrt(2) > 1`: the same witness remains outside the emergent
cone and inside the one-step microscopic support after restoring units. This
ratio is scale-free. It does not choose a physical value for `L` or `tau`.

## 4. What `3/128` means, and what it cannot mean

The exact result

`Delta p_B = D(rho_B^(0),rho_B^(1)) = 3/128`

is already physical in the limited operational sense appropriate to the
model: it is a dimensionless difference of outcome probabilities and the
trace distance of the two computed local states. It is invariant under the
restoration of `a`, `tau` and `hbar`. It means that, for the frozen idealized
state, local phase intervention, one-step dynamics and Bob projection, the
two messages change that event probability by `3/128`; equal priors would
give the corresponding single-copy Helstrom success probability
`(1 + 3/128)/2` for this pair.

It is **not** an energy, rate, cross-section, power, dimensional coupling or
probability per unit time. Multiplying or dividing it by `a` or `tau` would
define a new quantity not supplied by the protocol. Turning it into an
experimental count prediction would additionally require a realization map,
repetition rate, preparation and measurement efficiencies, and a noise model;
none is specified here and no such experiment is designed.

## 5. Energy and momentum obstruction

The initial exactly localized lattice state has a flat Fourier amplitude over
the entire Brillouin torus, not support restricted to `|p| << 1`. After two
finite-range updates it remains a finite Laurent polynomial and is still not a
narrow low-energy wave packet. The local encoding operation is likewise not a
low-energy projection.

Therefore the low-energy relation `E approximately hbar c_phys |k|` does not
assign this protocol a unique characteristic energy or momentum. One can state
the cutoff scales conditionally (`|k_i| <= pi/a` and quasienergy periodicity
`2 pi hbar/tau`), but no protocol energy in joules follows without an added
spectral preparation prescription. Adding one would change the frozen
protocol and lies outside this audit.

## 6. Claim ceiling and closure

**Established from the checked sources and exact in-repo conventions:** a
symbolic dimensional map exists; `c_IR^phys = a/tau`; the non-corner geometry
becomes `(L,Delta t) = (sqrt(2)a,tau)`; and `3/128` remains a dimensionless
single-use distinguishability for the idealized protocol.

**Not specified:** `a`, `tau`, an absolute energy/momentum scale, a coupling to
laboratory degrees of freedom, efficiencies, noise, feasibility, or any
identification of the lattice with nature. A Planck choice would be an added
hypothesis, not a consequence of the model.

The audit is therefore **CLOSED** as `DIMENSIONAL_MAP_CONDITIONAL`. Quantitative
physical prediction in SI units remains blocked until an independently
justified absolute scale and a physical realization map are supplied. No
`Delta T = 2` calculation and no experimental design has been performed.
