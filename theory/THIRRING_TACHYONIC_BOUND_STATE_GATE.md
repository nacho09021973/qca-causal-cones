# THIRRING TACHYONIC BOUND-STATE GATE

**Date:** 2026-11-18. **Status at charter:** OPEN / NOT EXECUTED.
**Authorization:** user "Hazla", following the proposed one-band, fixed-rule,
quick falsification test. This contract is frozen before its analytic verdict.

## Known and sources

- Fixed one-dimensional Thirring QCA: `U = FJ`, one-particle `W` of
  arXiv:1711.03920v1 Eq. (1), two-particle antisymmetric sector
  `U_2(p)=W_2(p)V_2(chi)`, Eqs. (2)-(4).
- The paper's Lemma 2, Eq. (14), and Proposition 1 give the isolated
  two-particle bound band and distinguish complex relative momentum `k`
  from its unit-modulus time eigenvalue.
- The existing exact certificate
  [verify_thirring_approximate_recovery.py](../scripts/verify_thirring_approximate_recovery.py)
  and its [report](../reports/2026-11-09--thirring-approximate-recovery.md)
  cover the special eigenvector at `p=pi/4`, not a dispersion-wide tachyon
  test. Do not rerun or extend that verifier for this documentary gate.

## Frozen scope and question

Fixed real parameters `mu=3/5`, `nu=4/5`, `chi=pi/2`; the original
`N=2` antisymmetric, translation-invariant, number-conserving Thirring
rule on the infinite one-dimensional lattice. Fiber momentum `p` is
**half** the total momentum; physical center of mass is
`X=(x1+x2)/2`. No external controls, parameter continuation, background
condensate, other code, or change of local rule.

**One question:** does the declared two-body bound band admit a physically
tachyonic signal, in either of two separately stated operational senses?

1. **Temporal-instability candidate:** a normalizable bound fiber mode
   with `|lambda(p)| != 1`, i.e. exponential temporal growth/decay under
   repeated `U_2`. Complex `k` alone does not qualify.
2. **Superluminal-signal candidate:** dependence on an initial local
   perturbation outside the microscopic one-cell-per-update cone, hence
   outside the *free massless nodal* speed `c_0=a/tau` of this same rule.
   A group derivative compared to a finite-mass `c_H` or
   `c_{omega^2}` is not a signaling test.

These two tests deliberately do not exhaust every use of "tachyon" in
field theory. In particular, a tachyonic instability of an effective
field linearized about a nonvacuum many-body background is outside this
`N=2` spectral contract.

## Admission, falsification, stop

- A *positive* candidate must explicitly satisfy at least one of the
  operational definitions, with phase/momentum conventions verified.
  Any apparent `|lambda|>1` or out-of-cone signaling must be checked
  against the assumptions of unitary, finite-range `U_2` before claiming
  anything physical.
- A *negative* result is established in the declared class if the exact
  spectrum is on the unit circle **and** the local rule enforces the strict
  causal support bound for arbitrary two-particle inputs.
  Then stop; no search for new particles or alternative models.
- If either ingredient cannot be checked from the original and the
  existing rule, record OPEN and stop (no numerical substitute).

**Possible verdict:** `NO_TACHYONIC_SIGNAL_IN_DECLARED_N2_RULE`,
only for the two operational tests and frozen model. This is neither a
general no-tachyon theorem nor an exclusion of many-body instability.

## Execution boundary

One exact documentary/analytic check; no fitted dispersion, new script,
simulation, independent review, or status promotion authorized by this
contract. The execution report must cite original equations, show the
support induction explicitly, distinguish `k` from time quasienergy,
and mark the author result PRELIMINARY pending external review.
**NOVELTY = OPEN.**
