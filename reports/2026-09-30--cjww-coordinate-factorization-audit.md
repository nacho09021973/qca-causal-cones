# CJWW coordinate-factorization audit

Date: 2026-09-30.

## 1. Question

Can one exact CJWW (5.15) tick on the original two-component cell be written
as a product of three invertible differentiable 2x2 factors, with one factor
depending on each original coordinate?

This is a restricted bridge test for the Arrighi-Facchini paired-QW route. It
does not test grouped cells, ancillas, repeated factors along the same axis,
time blocking, powers of the walk, or coordinate mixing.

## 2. Frozen scope

The audit follows
[`theory/CJWW_SINGLE_COORDINATE_FACTORIZATION_AUDIT.md`](../theory/CJWW_SINGLE_COORDINATE_FACTORIZATION_AUDIT.md),
frozen at `f9dcb46`. The freeze is retrospective with respect to the earlier
directed reading: it verifies a restriction already alleged in
[`reports/2026-09-30--arrighi-facchini-cjww-directed-reading.md`](2026-09-30--arrighi-facchini-cjww-directed-reading.md).
It is not evidence that the theorem was predicted before seeing the negative
direction.

Allowed equivalence: constant on-site conjugation.

Excluded equivalences: supercell, dilation, ancilla, blocking, powers of the
walk, repeated coordinate factors, and momentum-coordinate mixing.

## 3. Primary-source boundary

`biblioteca/1609.00305v2.pdf` was read locally. The relevant point is p.5,
Sec. IV, Eq. 36: the published construction composes directional walks
`U^(i)` to build a global operator. Pp.6-7 discuss implementation by grouping
and encoding. Those implementation freedoms are outside this restricted
certificate.

Therefore this audit may only be cited as:

```text
SINGLE_COORDINATE_FACTORIZATION_EXCLUDED
for one CJWW tick, original C^2 cell, one factor per original coordinate.
```

It must not be cited as a no-go theorem for all paired quantum walks.

## 4. Exact target

The target is `walk2()` from the existing symbolic machinery, with momenta
`p1,p2,p3` and exact matrix

```text
[[ cos(p1) cos(p2) exp(i p3),  -cos(p1) sin(p2) + i sin(p1)],
 [ cos(p1) sin(p2) + i sin(p1),   cos(p1) cos(p2) exp(-i p3)]]
```

The verifier checks exact unitarity and determinant 1 before the
factorization test.

## 5. First certificate

If

```text
W(p1,p2,p3) = A(p_i) B(p_j) C(p_k)
```

with invertible factors, then the left logarithmic derivative of the first
factor in the order,

```text
L_i = (partial_i W) W^-1,
```

depends only on `p_i`. Hence any nonzero cross derivative
`partial_j L_i` at fixed `i != j` excludes `i` as the first coordinate in
the product order.

The permanent verifier finds exact nonzero witnesses at the origin:

```text
partial_2 L_1(0) = [[-i, 0], [0, i]]
partial_1 L_2(0) = [[ i, 0], [0,-i]]
partial_1 L_3(0) = [[ 0, 1], [-1, 0]]
```

Every possible product order has one of axes 1, 2, 3 as first factor, so the
six orders are excluded by this necessary condition. The script also checks a
separated exact point, not only the derivative at the origin.

## 6. Second certificate

At `p1=pi/2`, the whole CJWW tick collapses exactly to

```text
W(pi/2,p2,p3) = i sigma_1.
```

But at the origin the derivatives along `p2` and `p3` are nonzero:

```text
partial_2 W(0) = -i sigma_2
partial_3 W(0) =  i sigma_3
```

In a one-factor-per-coordinate product, fixing `p1` and one of the other
coordinates would force the remaining coordinate factor to be constant; that
contradicts the nonzero variation at `p1=0`.

## 7. Positive control

The same necessary condition is applied to `walk1()`. The verifier confirms
the known product

```text
walk1 = F_1(p1) F_2(p2) F_3(p3)
```

and verifies that its first-axis left logarithmic derivative has no cross
dependence. This guards against a vacuous or over-strong test.

## 8. Constant conjugation

For every constant invertible on-site matrix `S`,

```text
partial_j[(partial_i(S W S^-1))(S W S^-1)^-1]
  = S (partial_j L_i) S^-1.
```

Nonzero witnesses remain nonzero under this transformation. The verifier
checks this covariance explicitly for
`S=(I+i sigma_3)/sqrt(2)`.

## 9. Command

Run from the repository root:

```bash
python3 -B scripts/verify_cjww_coordinate_factorization.py
```

The local run used for this report ended with:

```text
VERDICT: SINGLE_COORDINATE_FACTORIZATION_EXCLUDED
Scope: one factor per original coordinate, one tick, original two-component cell only
Evidence: AUTHOR_SIDE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING
```

## 10. Result

```text
SINGLE_COORDINATE_FACTORIZATION_EXCLUDED
AUTHOR_SIDE_CERTIFICATE / INDEPENDENT_REVIEW_PENDING
```

The result supports the atlas entry F5 as a restricted structural obstruction.
It does not decide whether a grouped Arrighi-Facchini circuit, a repeated-axis
factorization, or a different IR-only objective could be useful under a new
contract.
