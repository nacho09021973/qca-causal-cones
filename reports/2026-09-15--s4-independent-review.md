# S4 counterexample: independent mathematical review

**Date:** 2026-09-15

**Reviewed commit:** `1dae941e8df7f20203aacba9d5fa8f8ad9692bac`

**Verdict:** minimal counterexample survives independent review, for every
`0<a<1` at `theta=pi/4`. Branch-local correctness finding only.

**Canonical promotion:** not performed. Prior-art/novelty gate remains separate.

## 1. Scope and provenance

The reviewed objects are the three files added by the reviewed commit:
the [analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md), its
[original certificate](../scripts/cert_Aa_s4_counterexample.py), and the
[freeze record](2026-09-15--s4-strict-cone-counterexample-freeze.md).
The review reconstructs the algebra without importing the original verifier.

The comparison fixes one full product update per time unit and the physical
Fourier displacement `h=(sx,sy,sz)/sqrt(3)`, with phase `exp(-i k.h)`.
The parameter `a` is a dimensionless mixing parameter, not lattice spacing.
The internal dimension is four, `R_i=sigma_i tensor I_2`, and the selected
node is `k=0`, with two isolated rank-two clusters at quasienergies `+theta`
and `-theta`. The linear cones are measured relative to each cluster's node.
The positive BCC generating set can be taken as the four sign triples of
parity `+1`; coordinate half-turns act transitively on that set. Their
negatives form the other orbit. Full cubic rotational symmetry is not assumed.

This is a particular product ansatz, not a classification of four-component
walks. Irreducibility means absence of a common constant reducing subspace
of all Fourier coefficients. It does not prohibit a momentum-dependent
spectral decomposition, which would not in general preserve finite range.

Remote references checked during review:

- `origin/main`: `5845eda92d7a5ee07c2e8eb26183eb5b2770cf79`;
- research branch: `1dae941e8df7f20203aacba9d5fa8f8ad9692bac`.

Thus the reported remote delta is correct: one commit, three new files.
Local `main` is instead `95f423ff483fdb1897ce6ee2cd11e7a350e7b5e6`, containing
the later correction to `B_infty*`. Local main and the research branch are
each one commit ahead of their common ancestor `5845eda`. Integrating them
must preserve that correction. No merge, rebase or canonical edit was made.

## 2. Frozen independent checks and results

Before running the new script, its checks were fixed to:

1. both Fourier coefficient unitarity identities, at all 27 displacement differences;
2. D2 covariance, coefficient sums and signed first moments;
3. the vertex-trace formula with symbolic parameters;
4. both projected Weyl blocks;
5. Hermiticity, idempotency and commutation differential equations for the projector;
6. all nine components of the projector metric and the weighted sum rule.

Acceptance requires exact zero residuals. The new script uses explicit
exceptions on failure. Its polynomial reductions impose only
`a^2+b^2=1` and `c^2+d^2=1`, where `c=cos(theta)` and `d=sin(theta)`.
No fitted tolerance or parameter sampling is used. Projector equations are
multiplied by `d`; their interpretation requires `d != 0`.

The original certificate was run successfully in the working branch and
again in a fresh local clone at the exact reviewed commit, with a clean
worktree. The fresh checkout was `/tmp/qca-s4-review-84FouN`; it is not a
required input for future runs. Both runs used SymPy 1.14.0 and returned:

```text
S4_STRICT_CONE_COUNTEREXAMPLE_CERTIFICATE: PASS
a_panel=1/5,2/5,1/2,1/sqrt(2),4/5,99/100
theta_panel=pi/6,pi/4,pi/3 at a=1/2
backend=sympy_exact
tolerance=0
```

Reproduce the independent symbolic checks from the repository root:

```sh
python3 scripts/review_Aa_s4_exact.py
```

Observed output:

```text
both_fourier_unitarity_identities: PASS (27 differences each)
covariance_moments_and_all_parameter_trace: PASS
both_weyl_blocks_projector_equations_and_full_metric: PASS
S4_INDEPENDENT_SYMBOLIC_REVIEW: PASS
matrix_or_scalar_identities=117
sympy=1.14.0; tolerance=0; parameter_sampling=none
```

The original script supplies exact spot checks. The independent script
checks parameter identities. Neither check count alone proves the interval
inequality, infinite-time support statement or irreducibility: those
arguments are given below.

## 3. Vertex trace and survival for every a

Terms with one or two distinct Pauli factors have zero Pauli trace. In the
triple term, `sigma_x sigma_y sigma_z=i I_2`. Direct multiplicity algebra gives

\[
\operatorname{Tr}(T_xT_yT_z)=4iab^2,\qquad
\operatorname{Tr}(\tau_zT_xT_yT_z)=2a.
\]

Consequently, with `p=sx sy sz`,

\[
\operatorname{Tr}A_h=\frac12\left[c+p\,a(d-2b^2c)\right].
\]

At `theta=pi/4`, the trace is `sqrt(2)/4 [1+p a(2a^2-1)]`.
For `0<a<1`, both `a<1` and `|2a^2-1|<1`, so every trace is strictly
positive. Each coefficient is therefore nonzero and non-nilpotent.
In particular, no positive power of any vertex coefficient can vanish.

At displacement `n h`, every coordinate already attains its maximum or
minimum possible sum, so every step must equal `h`. Its coefficient is
exactly `A_h^n`; there is no second word with which it could cancel.
The upper support bound and all eight surviving vertices give

\[
\operatorname{conv}(S_n/n)=[-1/\sqrt3,1/\sqrt3]^3\quad(n\ge1).
\]

This proves the asserted strict asymptotic body, including its inradius
`1/sqrt(3)`. It does not use a finite iteration test or a lower bound on
amplitude norms.

## 4. Irreducibility independently checked

Summing coefficients with and without signs recovers `W` and `W Gamma_i`.
Any common commuting matrix therefore commutes with `W` and `Gamma_i`.
For `sin(theta) != 0`, write it as `diag(X_+,X_-)` in the tau-z decomposition.

The diagonal blocks of `[X,Gamma_x]=0` give
`[X_+,sigma_x]=[X_-,sigma_x]=0`, since `a != 0`.
The off-diagonal block gives `X_+ sigma_x=sigma_x X_-`, since `b != 0`.
Using the two preceding commutation equations yields `X_+=X_-`.
The diagonal blocks for `Gamma_y` then force the common matrix to commute
also with `sigma_y`. Expanding in the Pauli basis proves it is scalar.
There is no exceptional value inside `0<a<1`.

This establishes the scalar joint commutant and rules out a constant direct
sum decomposition. It also rules out a common invariant subspace: such a
subspace would be invariant under every unitary `A(k)`, hence reducing in
finite dimension, and Fourier uniqueness would make its orthogonal
projector commute with every coefficient.

**Necessary distinction:** the representation `R_i=sigma_i tensor I_2`
itself is reducible, with two copies of the Pauli projective representation.
The dynamics is irreducible. This result cannot refute a theorem that
explicitly requires an irreducible internal symmetry representation.

## 5. Weyl cones and metric normalization

Inside the two tau-z doublets, the projected generators are `+a sigma_i`
and `-a sigma_i`, respectively. Degenerate first-order perturbation at
the isolated eigenvalues of `W` therefore gives

\[
H_{\mathrm{eff},+}=\theta I_2+\frac a{\sqrt3}\,k\cdot\sigma+O(|k|^2),
\qquad
H_{\mathrm{eff},-}=-\theta I_2-\frac a{\sqrt3}\,k\cdot\sigma+O(|k|^2).
\]

Since `(k dot sigma)^2=|k|^2 I_2`, both cones are untilted and isotropic in
all directions, with speed `a/sqrt(3)`. Their quasienergy origins are
distinct. These are local expansions for fixed separated clusters, not
a uniform limit through `theta=0`.

Differentiating `[A,P]=0` at the node fixes the off-block derivative

\[
K_i:=Q(\partial_iP)P
=\frac{e^{i\theta}}{2\sqrt3\sin\theta}\,Q\Gamma_iP.
\]

Hermiticity and the derivative of `P^2=P` give `partial_i P=K_i+K_i^dagger`.
The lower multiplicity matrix elements of `T_i` are `b`, `ib`, `-b`.
Using `Tr(sigma_i sigma_j)=2 delta_ij` gives

\[
g_{ij}=\frac12\operatorname{Tr}[(\partial_iP)(\partial_jP)]
=\operatorname{Re}\operatorname{Tr}(K_i^\dagger K_j)
=\frac{b^2}{6\sin^2\theta}\delta_{ij}.
\]

The factor two from the rank-two sector is essential. The full tensor,
not only its diagonal, is checked by the independent script.

One can also see the origin of the sum rule without assigning a new
physical meaning to the terms. At the node set `J_i=i A^dagger partial_i A
=Gamma_i/sqrt(3)`. Then

\[
\frac12\operatorname{Tr}(P J_i^2 P)
=\frac12\operatorname{Tr}[(P J_i P)^2]
+\frac12\operatorname{Tr}(P J_i Q J_i P)
=\frac{a^2}{3}+\frac{b^2}{3}=\frac13.
\]

The second term equals `2 sin^2(theta) g_ii`. Thus the weighted identity
to `1/3` follows exactly from this family's involutions and projections.
Equality of that number to the strict-cone speed squared additionally
uses the vertex-survival proof; it is not a consequence of the projector
decomposition alone.

## 6. Domain clarification and outstanding gates

**Scope clarification for Sec. 8 of the analytic note:** the metric formula
and its weighted identity to `1/3` hold for `0<a<1`, `0<theta<pi/2`.
The final equality to `(c_strict^iso)^2` should explicitly inherit Sec. 5's
certified domain: `theta=pi/4`, or, for each fixed `a`, an open neighborhood
of that angle where all vertex traces remain nonzero. A sufficient explicit
condition within `0<theta<pi/2` is

\[
a\left|\sin\theta-2(1-a^2)\cos\theta\right|<\cos\theta.
\]

This review does not extend the strict-cone conclusion to all theta or
claim that it fails when this sufficient trace condition fails. Section 5
already disclaims a global all-theta result; repeating the domain next to
the boxed equation prevents an overreading. This precision issue does not
invalidate the original `theta=pi/4` counterexample.

Prior-art status is **not independently closed by this review**. The
existing source audit distinguishes classification assumptions, but this
review has not checked a direct equivalence or non-equivalence with Raynal's
s=4 construction. Neither correctness nor a difference in hypotheses proves
novelty. No new literature search was performed.

The surviving minimal claim is therefore:

> At fixed normalized BCC neighborhood, fixed D2 action and fixed doubled
> Pauli projective representation, the explicitly defined four-component
> irreducible family at theta=pi/4 has a constant strict causal body and
> a continuously variable, positive Weyl speed strictly below its inradius.

The result concerns exact support of the full walk and local Floquet Weyl
sectors. It neither refutes the minimal s=2 classification nor proves a
ballistic-front statement, IR universality, or a general causal-budget law.
Canonical integration and prior-art assessment remain separate actions.
