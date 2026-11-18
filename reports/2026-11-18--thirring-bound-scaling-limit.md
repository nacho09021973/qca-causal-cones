# Thirring bound-state correlated scaling limit

2026-11-18. **PRELIMINARY author result; no independent cross-family
review; no promotion.** This closes only the calculation specified by
[THIRRING_BOUND_SCALING_LIMIT_GATE](../theory/THIRRING_BOUND_SCALING_LIMIT_GATE.md).

## Question and exact result

For the two-fermion bound band of the one-dimensional Thirring QCA
at fixed interaction `chi=pi/2`, let
`nu=sqrt(1-mu^2)`, physical total momentum `P=2p=mu Q`,
and `mu -> 0+`, with `Q` real and fixed. Retain the
**negative** quasienergy branch `phi=-E_b` (`E_b>0)),
`k=pi+i kappa`, `kappa<0`. Then

```text
lim_{mu->0+} E_b(mu, P=mu Q)/mu = e(Q) = sqrt(Q^2+2),
D(Q) := e(Q)^2-Q^2 = 2 > 0.
lim_{mu->0+} kappa(mu, Q)/mu = -sqrt(Q^2+2)/2 < 0.
```

The convergence of the binding root and energy is **uniform for Q
in every fixed compact real interval**, but no uniform statement is
claimed over the entire unbounded Q-axis.

**Gate verdict:** `NO_TACHYONIC_INVARIANT_IN_DECLARED_SCALING`.
This is an effective two-particle dispersion statement, not a universal
no-tachyon theorem, nor a proof of a relativistic many-body continuum
limit.

## Derivation from the original bound equation

Use the existing exact reduction of `T_+=0`
([two-particle IR report](2026-11-09--thirring-two-particle-ir.md),
Sec. 3.2; original Bisio et al. 1711.03920v1, Lemma 2):

```text
X(z) = sin(omega(z)) - nu sin(z),
omega(z) = acos(nu cos(z)),
z = p+i kappa,
F = Re X - Im X = 0,
k=pi+i kappa, kappa<0.
```

Set `x=Q/2`, `kappa=mu*r`, and `z=mu*zeta`, with
`zeta=x+i*r`. On a complex neighborhood where the square-root
branch is fixed,

```text
1-nu^2 cos^2(mu*zeta) = mu^2 (1+zeta^2+O(mu^2)),
nu sin(mu*zeta) = mu (zeta+O(mu^2)),
X(mu*zeta)/mu = sqrt(1+zeta^2)-zeta+O(mu^2).
```

The principal square root is the one with positive real part near
the following candidate. Define

```text
a = sqrt(Q^2+2)/2 > 0,  x=Q/2,  r0=-a,
zeta0=x-i*a,  w0=a-i*x.
```

Because `a^2-x^2=1/2`,

```text
w0^2 = 1+zeta0^2,
Re(w0)=a>0,
sqrt(1+zeta0^2)-zeta0 = (a-x)(1+i).
```

Thus `Re X0=Im X0` holds exactly. The choice is physical:
`a>|x|` implies `r0=-a<0`, so the relative-coordinate
amplitude decays as `exp(kappa*|y|)`. The square-root argument
`w0^2` is nonzero and lies in a neighborhood admitting the stated
analytic branch.

The limiting root is simple. With `F0(r)=Re X0(x+i*r)-Im X0(x+i*r)`,
differentiation gives

```text
dX0/dr = -i X0/w0,
F0'(r0) = 2*a*(a-x)/(a^2+x^2) > 0.
```

The functions above extend smoothly in `mu^2` near zero after
dividing `X` by `mu`. The implicit-function theorem therefore
produces a continued real root `r(mu,Q)=r0+O(mu^2)` for sufficiently
small positive `mu`, with `kappa=mu*r<0`. The uniqueness of the
normalizable bound solution for `p != 0` is inherited from the
existing Lemma 2 argument; at `p=0` it matches the already established
explicit bound root. Hence this continuation is the same bound band,
not an extra formal solution. On each compact Q-set the selected
analytic branches and positive derivative admit uniform bounds, so
the estimates and convergence are uniform there.

For the relevant negative-quasienergy band the previous report gives
`E_b=2 Re omega(p+i kappa)`. Since
`omega(mu*zeta)/mu -> sqrt(1+zeta^2)` on this branch,

```text
E_b(mu,mu Q)/mu -> 2 Re(w0) = 2a = sqrt(Q^2+2).
D(Q) = (2a)^2-Q^2 = 2.
```

At `Q=0`, this agrees with the prior exact
`M_b=2 asin(mu/sqrt2)` and `M_b/mu->sqrt2`.
It is also compatible with the previous `c_b^2->1`.
Those local checks alone did **not** imply the present full function.

## Verification, limits of verification, status

Verifier [`scripts/verify_thirring_bound_scaling.py`](../scripts/verify_thirring_bound_scaling.py)
was **committed before its first execution**, SHA
`0664f013a596311ee3085962e9a1d1d80df9ad81`.
Executed once under Python 3, SymPy 1.14.0: **9/9 exact
symbolic identities PASS**, with no floating-point values or scans.
Checks: leading Taylor coefficients (2), square-root/saddle algebra (4),
implicit derivative (1), invariant and rest energy (2).
The verifier contains no numerical approximation and writes no files.

Not mechanically certified: correctness of the cited exact `T_+`
reduction; identification with the original normalizable eigenvector;
use of Lemma 2; selection of analytic roots and the
implicit-function/compact-uniform argument. Those steps are written
above and require independent cross-family review before any
promotion. The original 2026-11-09 report has repaired but not
re-reviewed scope objections, so it remains PRELIMINARY.

No conclusion about finite `mu` at arbitrary momenta,
other interaction phases, other bands, one-particle tachyonic
excitations, interactions in many-particle sectors, or a universal
continuum limit. No changes to `main` or
`state/CURRENT_STATE.md`. **NOVELTY=OPEN.**
