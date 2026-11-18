# THIRRING_BOUND_SCALING_LIMIT_GATE

**2026-11-18. Status at charter: OPEN / NOT EXECUTED.**
User authorization: "Adelante" to the one-step calculation of the full
two-particle bound-band scaling function, after a read-only check of existing
reports. Branch-local research; no automatic promotion.

## Existing knowledge

- Fixed one-dimensional Thirring rule `U=FJ` and two-particle bound
  solution: Bisio et al., arXiv:1711.03920v1, Eqs. (1)-(4), (12),
  Lemma 2, Proposition 1; also sources/1804.08508v1.pdf.
- [Two-particle IR preflight](../reports/2026-11-09--thirring-two-particle-ir.md)
  Sec. 3.2-3.3: with `chi=pi/2`, `nu=sqrt(1-mu^2)`, and
  `P=2p`, the bound band near `p=0` lies at **negative**
  quasienergy `phi=-E` (equivalently eigenvalue `exp(i E)`),
  with `E(0)=M_b=2 asin(mu/sqrt2)>0`. Its local expansion
  `E(p)^2=M_b^2+c_b^2(2p)^2+O(p^4)` has
  `M_b/mu -> sqrt2`, `c_b^2->1`; the full function at
  `P=mu Q` was explicitly **not computed**. Previous checks: 34/34
  exact author tests; Grok required documentary/verdict repairs, which
  were applied but not re-reviewed.
- No new verifier should repeat those checks. Use the original implicit
  bound condition `T_+=0` and its existing reduction:
  `X(z)=sin(omega(z))-nu sin(z)`, `z=p+i kappa`,
  `Re X(z)=Im X(z)`, `k=pi+i kappa`, `kappa<0`.

## One question, quantifiers, and normalization

For **every fixed real Q**, with `mu -> 0+`, `chi=pi/2` fixed,
`P=mu Q` and `p=mu Q/2`, does the *same normalizable
bound-state branch* have a well-defined limit

```text
e(Q) = lim_{mu -> 0+} E_b(mu, p=mu Q/2)/mu ?
D(Q) = e(Q)^2 - Q^2 ?
```

Determine these exact functions, at least pointwise for all fixed
`Q`; uniformity on compact Q-sets is a separate explicit obligation.
A negative `D(Q)` alone would not automatically prove a physical
tachyon; a constant negative invariant and a controlled relativistic
effective description would be needed.

No change of sign of `chi`, no plus-threshold substitution, no scan
of masses, no other band, no new QCA, no many-body background.

## Disclosed pre-charter exploration

Before freezing this file, the author performed unverified hand
algebra: set `z=mu(x+i r)`, `x=Q/2`; the leading equation appears to
admit `x+i r=sinh(u-i pi/4)` with real
`sinh u=Q/sqrt2`, giving candidate `r=-sqrt(Q^2+2)/2`
and `e(Q)=sqrt(Q^2+2)`. This is **PRELIMINARY, not evidence**;
the gate must test the correct branch, the small-mu error, and whether
the implicit root is unique and normalizable. If any check fails, do
not tune the candidate after seeing the result.

## Admission and stopping rules

- Freeze the original `T_+` sign convention, `k_R=pi`,
  `kappa<0`, `phi=-E`, and physical `P=2p`.
- Derive the leading equation from the **original exact** `X`,
  show the root is nondegenerate (implicit-function step) and remains
  `kappa<0` for sufficiently small `mu`. Justify any branch of
  `sqrt(1+z^2)` and the limit of `E`.
- Certify the finite algebraic identities exactly; if code is needed,
  create one versioned verifier *before* running it, reuse existing
  formulas, and state what the verifier cannot certify.
- **Success:** exact closed `e(Q)` and `D(Q)` with declared
  pointwise/uniform scope. If `D(Q)=2>0`, record
  `NO_TACHYONIC_INVARIANT_IN_DECLARED_SCALING`; this is only about
  this band and scaling, not general tachyons.
- **Failure or undecided:** `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`, no
  numerical sweep and no inference from the truncated `O(P^4)` series.

Author result is PRELIMINARY pending independent cross-family review.
No modification to `state/CURRENT_STATE.md` or `main` unless
separately authorized. **NOVELTY = OPEN**.
