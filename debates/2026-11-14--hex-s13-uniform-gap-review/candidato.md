# S13: from non-attainment to a uniform gap (candidate addendum)

**Date:** 2026-11-14. **Branch:** `research/schur-stability-audit`, base
`7cadad6`. **Nature:** candidate addendum to
`reports/2026-11-03--hex-supremum.md` (M1-B13), for independent review
before any incorporation. No new contract, no computation, no script.
**Status: PRELIMINARY, unreviewed.** No novelty claim.

**Provenance.** Compactness argument and non-emptiness: Claude Code (Claude
Opus 5.5), 2026-11-14. The proof of Lemma 2 below, which uses only Lemma B
of `reports/2026-11-01--hex-ceiling.md`, was formulated by the user (with an
external assistant) and rechecked step by step by the author; it replaces
the author's first version (a one-sided Bernstein bound obtained by a phase
shift), which is not used.

## 0. Class

Notation of the S13 report: triangular lattice `Lambda`, S13 the closed
regular lattice hexagon with vertex `g_1 + g_2` (13 points), normalised so
that `|vertex| = 1`, hence `r_in(conv S13) = sqrt3/2`.
`U(k) = sum_{h in F} A_h e^{-ik.h}`, `A_h in M_2(C)`.

`X_13` := the walks of `W_hex^sym` (HEX_SUPREMUM_GATE.md, "Gap direction":
s=2 unitary Laurent polynomials with `U(0) = e^{-i phi} I`, traceless
isotropic linear term `A(n)^2 = c_0^2 |n|^2 I` with `c_0 > 0`, and
`C_micro = conv F` a regular hexagon from the exact composite support `F`)
with `F within S13` and `conv F = conv S13`, i.e. all six vertex
coefficients nonzero. On `X_13` the denominator `r_in(C_micro) = sqrt3/2`
is constant.

M1-B13 (`PROVED_FOR_S13`, promoted): no walk of `X_13` has
`c_0 = r_in`.

**Claim.** There is `eps_13 > 0` with `c_0 / r_in <= 1 - eps_13` on all of
`X_13`; moreover `eps_13 <= 1 - sqrt3/2`. No value of `eps_13` is given.

## 1. Lemma 1 (compact closure, continuous ratio)

Let `Y` be the set of tuples `(A_h)_{h in S13}` satisfying: (a) `U(k)`
unitary for all `k`; (b) `U(0)` scalar; (c) the linear term
`A(n) = i d/dt [e^{i phi} U(t n)]_{t=0}` traceless with
`A(e_1)^2 = A(e_2)^2 = c^2 I` for some real `c >= 0` and
`A(e_1) A(e_2) + A(e_2) A(e_1) = 0`.

- (a) is the family of polynomial identities `sum_{h-h'=d} A_h A_{h'}^dag
  = delta_{d,0} I` and likewise for `U^dag U`: closed.
- (b), (c) are polynomial equalities in the coefficients and in
  `e^{i phi}` (on the unit circle): closed. (c) is equivalent to
  `A(n)^2 = c^2 |n|^2 I` for all `n` by bilinearity.
- Boundedness: the `d = 0` identity of `U^dag U = I` gives
  `sum_h A_h^dag A_h = I`, so `||A_h|| <= 1`.

Hence `Y` is compact. `X_13 = Y cap {c_0 > 0} cap {A_v != 0 for the six
vertices v}`; both extra conditions are open, so `closure(X_13) within Y`
is compact. `c_0^2 = (1/2) tr A(e_1)^2` is a polynomial, so
`rho := c_0 / (sqrt3/2)` is continuous on `Y` and attains its maximum on
`closure(X_13)` at some `y`.

## 2. Lemma 2 (vertex loss forces `c_0 <= 1/2`)

Let `y in Y` with `A_v(y) = 0` for some vertex `v` of S13. Let
`hat v = v/|v|`. The projections `h . hat v` of the points of
`S13 \ {v}` are exactly `{-1, -1/2, 0, 1/2}` (the other vertices give
`±1/2, -1/2, -1`; the inner ring, at radius `1/sqrt3` and angles `±30°,
±90°, ±150°` from `hat v`, gives `1/2, 0, -1/2`; the origin `0`). Further
missing points only remove frequencies.

Set `W(t) = e^{i phi} U(t hat v)`, so `W(0) = I`, and `H = i W'(0)`.
Differentiating `W W^dag = I` at `0` shows `H` Hermitian; by (c), `H`
is traceless with `H^2 = c_0^2 I`, so its spectrum is `{±c_0}`.

Let `P(t) = e^{-it} W(4t)`. Its frequencies (as `e^{-imt}`) are
`m = 4p + 1` with `p in {-1, -1/2, 0, 1/2}`, i.e. `m in {-3, -1, 1, 3}`,
so `P` is a trigonometric polynomial of degree `<= 3`, unitary for every
`t`. For unit `x, z in C^2`, `<z, P(t) x>` has modulus `<= 1`; Lemma B of
the hex-ceiling report (Bernstein, proved in-repo) gives
`|<z, P'(0) x>| <= 3`, hence `||P'(0)|| <= 3`. Now
`P'(0) = -i W(0) + 4 W'(0) = -i (I + 4H)`, so `||I + 4H|| <= 3`. The
eigenvalue `1 + 4 c_0` gives `c_0 <= 1/2`. Therefore
`rho(y) <= (1/2)/(sqrt3/2) = 1/sqrt3`.

## 3. Theorem (uniform gap on `X_13`)

Let `y` maximise `rho` on `closure(X_13)`. Exactly one of:

1. `y in X_13`: `rho(y) < 1` by M1-B13.
2. `c_0(y) = 0`: `rho(y) = 0`.
3. `c_0(y) > 0` and some vertex coefficient of `y` vanishes:
   `rho(y) <= 1/sqrt3` by Lemma 2.

(Points of the closure with all six vertex coefficients nonzero and
`c_0 > 0` are in `X_13`: the exact support then has hull `conv S13`,
whatever inner-ring coefficients vanish.) In every case `rho(y) < 1`, so
`sup_{X_13} rho = rho(y) =: 1 - eps_13 < 1`.

## 4. Non-emptiness and an upper bound for `eps_13`

The T1 attainment walk of the hex-ceiling report (Sec. 2) is
`U(k) = prod_j exp(-i (k.a_j) tau_j)` with coplanar Bloch vectors at 120°,
certified there with `F = {0, ±2 a_j}`, regular hexagonal hull, every
vertex coefficient non-nilpotent, `U(0) = I`, isotropic untilted cone,
`c_0/r_in = sqrt3/2`. Its symbol depends on `k` only through
`e^{-ik.h}`, `h in F`. Choosing `b_j = 2 a_j` to be three alternate
vertices of S13 (lattice vectors at 120°, `b_1 + b_2 + b_3 = 0`) gives a
unitary Laurent polynomial on `Lambda` with `F = {0} U vert(S13)`,
`conv F = conv S13`, node and isotropy unchanged: a point of `X_13` with
`rho = sqrt3/2`. Hence `sqrt3/2 <= 1 - eps_13 < 1`.

The `a_j = b_j/2` are not lattice vectors, so this point is in
`W_hex^sym`; whether `X_13 cap W_hex` (product form with lattice partial
shifts) is nonempty is not established here.

## 5. Scope

- Qualitative gap only: compactness gives no value of `eps_13`; the only
  bounds are `0 < eps_13 <= 1 - sqrt3/2`.
- S13 only. The argument uses that removing a vertex of S13 drops the
  inradius (Lemma 2). For larger hexagons with lattice points inside the
  edges, removing a vertex may leave the inradius unchanged, and the
  limit then has a non-regular hull outside `W_hex^sym`, where no existing
  result applies. Nothing is claimed for S19, S25 or larger, nor for
  `s > 2`.
- No statement that the substrate fixes `c_0`.
