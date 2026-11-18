# Thirring two-body bound band: tachyonic-signal falsification

**Date:** 2026-11-18. **Author verdict:** PRELIMINARY exact analytic
check; not independently reviewed, not promoted. **NOVELTY = OPEN.**

**Contract:** [THIRRING_TACHYONIC_BOUND_STATE_GATE.md](../theory/THIRRING_TACHYONIC_BOUND_STATE_GATE.md),
preregistered and committed at `d7da3c77c21ce797aa285ccf95f57802af3879ad`.
User authorized execution ("Hazla"). Fixed parameters:
`mu=3/5`, `nu=4/5`, `chi=pi/2`; the same antisymmetric
`N=2` Thirring rule `U_2=W_2 V_2(chi)`.

## Primary and in-repository evidence

- Bisio, D'Ariano, Perinotti and Tosini, *The Thirring quantum cellular
  automaton*, [arXiv:1711.03920v1](https://arxiv.org/abs/1711.03920):
  Eq. (1) the one-particle walk, Eq. (2) the on-site two-particle
  interaction, Eqs. (3)-(4) the fiber convention, Lemma 2 the existence
  of the bound eigenvector, Eq. (14) the exceptional bound eigenvector,
  Proposition 1 the two-body spectral decomposition. These equations
  were checked in the original HTML full text during this session.
- Existing [approximate-recovery report](2026-11-09--thirring-approximate-recovery.md)
  and [16/16 exact author checks](2026-11-09--thirring-approximate-recovery.txt)
  already verify the `p=pi/4` exceptional eigenvector `lambda=i`
  at these parameters. Their full-scope theorem is different; the old
  verifier was not rerun, modified, or cited as a test of the whole band.

## Test 1: temporal tachyonic instability

From the primary Eq. (1), for every real one-particle momentum `q`,

```text
W(q) = [[nu exp(iq), -i mu], [-i mu, nu exp(-iq)]]
nu^2 + mu^2 = 1.
```

Direct multiplication gives `W(q)^dagger W(q)=I`: each diagonal
entry is `nu^2+mu^2=1`, and the off-diagonals cancel.
The two-particle free walk is the antisymmetric restriction of
`W tensor W`, hence unitary. Equation (2) adds only the on-site
phase `exp(i chi)`, of modulus one for the fixed real `chi`.
Thus **each fiber `U_2(chi,p)` is unitary**.

For any nonzero normalizable bound fiber eigenvector `f_p`,

```text
U_2(chi,p) f_p = lambda_b(p) f_p
||f_p|| = ||U_2 f_p|| = |lambda_b(p)| ||f_p||
therefore |lambda_b(p)| = 1.
```

This is an exact all-`p` obstruction to `|lambda_b| != 1`.
The complex `k=k_R+i k_I` with `k_I<0` in the paper's bound
solutions produces spatial decay `exp(k_I y)` for `y>0`;
it is **not** temporal amplification. In particular, Eq. (14)'s
`lambda_b(pi/4)=i` is unit-modulus. Therefore the declared
*temporal-instability* candidate fails.

This does not rule out a tachyonic effective field linearized about an
unstable nonvacuum many-body background: such a background and its
linearized dynamics have not been defined or tested.

## Test 2: signal outside the microscopic/free-nodal cone

The original Eq. (1) moves each single-particle component by at most
one site per update (including on-site mass mixing). Equation (2)
multiplies two-particle amplitudes by a local phase without moving
either position. If an initial two-particle amplitude is supported
on `S subset Z x Z`, after one application of `U_2` it is supported
inside `S + {-1,0,1}^2`. Induction gives after `t` updates

```text
support(U_2^t psi) subset S + [-t,t]^2 .
```

For the actual center of mass `X=(x1+x2)/2`, a perturbation of
initially localized amplitudes cannot affect `|Delta X|>t` in lattice
units. The paper uses `p=(p1+p2)/2` and `w=x1+x2`; comparing
a derivative with respect to `p` to a physical center-of-mass speed
without converting `w=2X` would be a coordinate error.

The free **massless nodal limit** of this parameter family has
`c_0=a/tau` as recorded in the README, but it takes `mu -> 0`:
**this is not a low-energy speed established for the frozen
`mu=3/5` interacting rule.** The microscopic one-step displacement
bound is `a/tau` for the frozen rule. Consequently no two-body
signal crosses the **microscopic cone**. This exactly answers the
contract's second *operational* criterion; it does **not** compare
the bound band's group velocity with a physically derived `c_IR`
for the massive interacting dynamics. The charter's shorthand
"of this same rule" for `c_0` is thus only valid as "of the same
parameter family in the massless limit", not at the frozen mass.
Do not identify finite-mass `c_H`, `c_{omega^2}`, and `c_0`.

## Result, restrictions, and stop

Both predeclared candidates fail under the frozen `N=2`, fixed-rule
contract:

- `TEMPORAL_INSTABILITY_CANDIDATE: REJECTED` (unit modulus of exact
  fiber point spectrum).
- `OUT_OF_MICRO_CONE_SIGNAL_CANDIDATE: REJECTED` (strict one-step
  locality and support induction).
- **Author verdict:** `NO_TACHYONIC_SIGNAL_IN_DECLARED_N2_RULE`,
  `PRELIMINARY` pending independent review. This is not a statement
  about superluminal *group derivatives* relative to a separately
  defined slower effective sector, nor a general absence of tachyons
  or nonvacuum many-body instabilities.

The contract's stop condition is triggered. **No simulation, fitted
dispersion, new verifier, new substrate, or parameter search is needed
to answer the frozen question.** All steps above are analytic. No claim
of novelty or publication readiness. Do not update
`state/CURRENT_STATE.md` or `main` without separately authorized
review and promotion.
