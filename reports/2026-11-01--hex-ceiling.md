# Hexagonal ceiling — execution report (L0 and T1)

Date: 2026-11-01. Branch: `research/schur-stability-audit`.
Contract: [`HEX_CEILING_GATE.md`](../theory/HEX_CEILING_GATE.md),
preregistered at `8c56ced`.
Verifier: [`scripts/verify_hex_ceiling_gate.py`](../scripts/verify_hex_ceiling_gate.py),
24/24 exact checks (Python 3.12.3, `sympy==1.14.0`); repaired 2026-11-02
after review (see the repair note below).
Author: Claude Code (Claude Opus 5.5), at the user's direction.

**Status: PARTIAL EXECUTION — L0 `PROVED_IN_REPO` (Bernstein's inequality
proved in Lemma B); T1 `GAP_PROVED_IN_CLASS` with
supremum `sqrt3/2`, attained; T2 `PROVED_FOR_MINIMAL_SUPPORT`
(`F within {0} U vert(H)`, any s=2 walk, no product form assumed); T2 in
general `OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS`. Execution stopped here; ready
for independent review.** Evidence **PRELIMINARY**. Not promoted.

**Repair note (2026-11-02).** [Reviews](2026-11-02--hex-ceiling-review.md):
Gemini PASS; Grok REPAIR_REQUIRED with two mandatory repairs, both
accepted. (R1) L0 was labelled `PROVED_IN_REPO` while Bernstein's
inequality was only named as prior art, against contract Sec. 2; Lemma B
now proves it in-repo. (R2) The verifier's "rank 2 for every theta_0"
check only tested that a minor is not identically zero; it now asserts the
minor equals the `theta_0`-free constant `sqrt3 l^4/2`. Clarifications:
Hermiticity of `A` in L0; the maximum-modulus step in T2; the hexagon
fixes the denominator `2l`; `xi` is a Bloch component.

## 1. L0 — the ceiling `c_0 <= r_in` on `W_hex`

Let `U` be in `W_hex`. Multiplying by the scalar `e^{i phi}` does not change
the support, so take `U(0) = I`. Let `n_f` be the unit outward normal of a
facet of the regular hexagon `C = conv F`, with edge vector `d in Lambda`
(edges join lattice vertices). For a lattice vector `h = a g_1 + b g_2` and
`d = p g_1 + q g_2`,

`h . Rot90(d) = (sqrt3/2)(b p - a q)`   (verifier, check L0),

so `h . n_f = m_h delta` with `m_h in Z` and `delta = sqrt3/(2|d|)`. The
extreme values of `h . n_f` over `F` are `±h_C(n_f)` (central symmetry of
the hexagon) and are attained at vertices, which lie in `F`; hence
`h_C(n_f) = N delta` for an integer `N` and every `m_h` satisfies
`|m_h| <= N`.

For unit vectors `x, y in C^2` set `p(s) = <y, U(s n_f / delta) x>`. Then
`p(s) = sum_{|m|<=N} c_m e^{-i m s}` is a trigonometric polynomial of degree
`N` with `|p| <= 1` (U unitary). Bernstein's inequality (Lemma B below,
proved here) gives `|p'(0)| <= N`, i.e. `|<y, dU/dt(0) x>| <= N delta =
h_C(n_f)` along `n_f`. Taking the supremum over `x, y`,
`||A(n_f)|| <= h_C(n_f) = r_in`, where `A(n) = i dU(t n)/dt (0)`. `A(n_f)` is
Hermitian: differentiating `U U^dag = I` at `t = 0`, where `U = I`, shows
`dU/dt(0)` is anti-Hermitian. With `s = 2` and a traceless isotropic cone,
`A(n_f)^2 = c_0^2 I`, so the Hermitian `A(n_f)` has spectrum `{±c_0}` and
`||A(n_f)|| = c_0` (without Hermiticity, `M^2 = c_0^2 I` would not fix the
norm). Therefore **`c_0 <= r_in` for every walk in `W_hex`**. Only the
facet normal is needed, since `r_in = min h_C` is attained there.

**Lemma B (Bernstein, proved in-repo; repair R1 of the 2026-11-02 Grok
review).** If `p(s) = sum_{|m|<=N} c_m e^{-ims}` and `|p| <= 1` on `R`, then
`|p'(s_0)| <= N` for every `s_0`.

*Reduction to real polynomials.* Fix `s_0` and choose `alpha` with
`e^{i alpha} p'(s_0) = |p'(s_0)|`. `R(s) = Re(e^{i alpha} p(s))` is a real
trigonometric polynomial of degree `<= N`, `|R| <= 1`, and
`R'(s_0) = Re(e^{i alpha} p'(s_0)) = |p'(s_0)|`. So it suffices to show
`R'(s_0) <= N` for real `R`.

*Real case.* Suppose `R'(s_0) > N`. Choose `0 < eps < 1` so small that
`R_eps = (1 - eps) R` still has `R_eps'(s_0) > N`; then `|R_eps| < 1`
everywhere. Pick `beta in (-pi, 0)` with `cos beta = R_eps(s_0)` (possible
since `|R_eps(s_0)| < 1`) and set `C(s) = cos(N(s - s_0) + beta)`. Then
`C(s_0) = R_eps(s_0)` and `C'(s_0) = -N sin beta in (0, N]`, so
`D = C - R_eps` has `D(s_0) = 0`, `D'(s_0) < 0`; in particular `D` is not
identically zero. On one period `C` reaches `±1` alternately at `2N`
points `t_1 < ... < t_2N`, and there `|R_eps| < 1` gives
`sign D(t_j) = sign C(t_j)`, alternating. Hence `D` has a zero in each of
the `2N` open arcs between consecutive `t_j`. The point `s_0` is not a
`t_j` (`D(s_0) = 0 != D(t_j)`), so it lies in one arc `(t_j, t_{j+1})`, on
which `C` is monotone; `C'(s_0) > 0` makes it increasing, so
`C(t_j) = -1`, `C(t_{j+1}) = +1`, i.e. `D(t_j) < 0 < D(t_{j+1})`. Since `D`
falls through zero at `s_0` (`D'(s_0) < 0`), `D > 0` just left of `s_0` and
`D < 0` just right of it: there is a further zero in `(t_j, s_0)` and one in
`(s_0, t_{j+1})`. That arc holds at least three zeros, so `D` has at least
`2N + 2` zeros per period. But `e^{iNs} D(s)` is an algebraic polynomial of
degree `<= 2N` in `z = e^{is}`, so a nonzero `D` has at most `2N` zeros per
period. Contradiction; hence `R'(s_0) <= N`. Applying this to `R(-s)` gives
`R'(s_0) >= -N`. `square`

This is the classical argument (prior art; no novelty claimed); it is
written out so that L0 closes in-repo as the contract (Sec. 2) requires.

## 2. T1 — the `n = 3` antipodal subclass

**Reduction (analytic).** With `D_j(k) = diag(e^{-ik.a_j}, e^{ik.a_j}) =
e^{-i (k.a_j) sigma_z}` and `G_j = C_{j-1} ... C_1` (`G_1 = I`),

`C_3 D_3 C_2 D_2 C_1 D_1 = (C_3 C_2 C_1) * prod_{j=3..1} G_j^dag D_j G_j`.

The node condition makes `C_3 C_2 C_1` scalar, so up to a phase
`U(k) = prod_{j=3..1} exp(-i (k.a_j) tau_j)`, `tau_j = G_j^dag sigma_z G_j
= t_j . sigma` with unit Bloch vectors `t_j` (free up to one global
rotation). The `a_j` are three lattice vectors of equal length `l` at
120°, `a_1 + a_2 + a_3 = 0`.

**Linear term.** `A(k) = sum_j (k.a_j) tau_j = (sum_j t_j (a_j . k)) . sigma`,
independent of the factor order. Its square is
`k^T M k I` with `M = sum_ij g_ij a_i a_j^T`, `g_ij = t_i . t_j`.

**Isotropy forces equal overlaps** (verifier, symbolic in `theta_0`):
the traceless part of `M` is linear in `(g_12, g_13, g_23)` with a
coefficient matrix whose `2x2` minors are `±sqrt3 l^4/2`, independent of
`theta_0` (verifier), hence rank 2 for every `theta_0`, with kernel
`(1,1,1)`. Geometrically, the three
pair terms are double-angle vectors at `2 theta_0`, `2 theta_0 + 2pi/3`,
`2 theta_0 + 4pi/3`, which cancel only with equal weights. With
`g_ij = g`: `M = (3/2) l^2 (1 - g) I`, so `c_0,raw^2 = (3/2) l^2 (1 - g)`.

**Range of `g`.** The Gram matrix of three unit vectors with equal
overlaps has eigenvalues `1 + 2g` and `1 - g` (twice); it is realisable iff
`-1/2 <= g <= 1`.

**Normalisation.** `F` is contained in `{0, ±2 a_j}`; the hexagon condition
puts all six `±2 a_j` in `F`, so the longest step is `2l` and
`c_0 = c_0,raw/(2l)`, `r_in = sqrt3/2`. Hence

`c_0 / r_in = sqrt(1 - g) / sqrt2 <= sqrt3/2`, equality iff `g = -1/2`,

i.e. iff the three Bloch vectors are coplanar at mutual 120°. The
hexagon condition enters only through the denominator: it puts the six
`±2 a_j` in `F` and so fixes the longest step at `2l`. It does not change
the supremum, since `g = -1/2` is realised with all six vertices present.

**Attainment.** The verifier builds the walk with
`t_j = (cos 2pi j/3, sin 2pi j/3, 0)` and certifies exactly: unitary
symbol, `F = {0, ±2 u_j}`, regular hexagonal hull (6 vertices, 6 facets,
`r_in = sqrt3/2`), every vertex coefficient non-nilpotent, `U(0) = I`,
untilted isotropic cone, `c_0 = 3/4`, `c_0/r_in = sqrt3/2`.

**Explains the previous table.** ADMP's `tau_i` (Eq. (5)) have `g = 1/3`,
giving `c_0 = 1/2` (verifier, reproducing row L6a of Sec. 11). JDW L6d has
`c_0 = 3/4`, the maximum, which corresponds to `g = -1/2`. The ADMP–JDW
difference on the same substrate is the difference in the overlap of the
three coin axes: ADMP's axes share the Bloch `z`-component
`xi = sqrt5/3` (they are not coplanar through the origin), which raises
`g` to `1/3` and costs speed.

**Verdicts.** T1 `GAP_PROVED_IN_CLASS`: `sup c_0/r_in = sqrt3/2`,
attained exactly at coplanar 120° Bloch vectors. HX1
`CONFIRMED_IN_CLASS` (T1 subclass). HX0 `CONFIRMED_IN_CLASS` (L0, all of
`W_hex`).

## 3. T2 — minimal-support subclass (2026-11-02)

Subclass: walks in `W_hex` whose composite support satisfies
`F within {0} U vert(H)` (origin plus the six hull vertices). No product
form is assumed: the argument uses only `F`, unitarity, the node and
isotropy. It contains T1, ADMP L6a, JDW L6d and L6f (Sec. 11); it does not
contain JDW L6c (19 points).

**Step 1: saturation along a facet normal is rigid.** Suppose
`c_0 = r_in`. Let `n_f` be a facet normal and `x` a unit eigenvector of
`A(n_f)` with eigenvalue `+c_0`. With the notation of Sec. 1,
`p(s) = <x, U(s n_f/delta) x>` has `|p| <= 1`, `p(0) = 1` and
`p'(0) = -i N`. Then `P(z) = z^N p` (with `z = e^{is}`) is an analytic
polynomial with `|P| = |p| <= 1` on the unit circle, hence `|P| <= 1` on
the closed disc by the maximum-modulus principle, `P(1) = 1` and
`P'(1) = 0`.
By Julia's lemma (classical; a non-constant `P` with `|P| <= 1` and a
boundary fixed point has angular derivative `P'(1) > 0`) `P` is constant,
so `p(s) = e^{-iNs}`; equivalently this is the equality case of
Bernstein's inequality, listed as prior art in PROJECT_INSTRUCTIONS §6.
By Cauchy–Schwarz `U(t n_f) x = e^{-i r_in t} x` for all `t`, and likewise
for the `-c_0` eigenvector. Hence along every facet-normal line
`U(t n_f) = e^{-i r_in t} P_+(n_f) + e^{i r_in t} P_-(n_f)`: only the two
extreme layers of `F` survive in that direction. In coefficients: the sum
of `A_h` over the top edge is `P_+(n_f)`, over the bottom edge
`P_-(n_f)`, and over every intermediate layer `0`.
Citation status: Julia's lemma and the Bernstein equality case are
classical; no primary source for them is in `sources/` (page
[UNVERIFIED]).

**Step 2: normal form.** By a Bloch rotation, a joint rotation of space
and Bloch sphere about `z`, and scale, take `vert(H) = {(cos k pi/3,
sin k pi/3)}` and `A(n) = r_in n . sigma` with `n` in the `xy` Bloch plane.
The three facet normals are at 30°, 90°, 150°.

**Step 3: certificate (verifier).** Along each facet normal the layers
are top edge (2 vertices), middle layer (2 vertices and `0`), bottom edge.
The nine layer equations are consistent, leave the coefficient `X_0` of
one vertex free, and force `A_0 = -I/2`. Imposing
`sum_h A_{h+d} A_h^dag = delta_{d0} I` and `sum_h A_h^dag A_{h+d} =
delta_{d0} I` for all `d`, the lex Gröbner basis of the real equations
contains `x^2 - x/2 + 1/12` in one real coordinate of `X_0`; its
discriminant is `-1/12 < 0`. No real solution exists.

**Positive control.** The same procedure on the square substrate
(`F within {0} U {(±1,±1)}`, facet normals `x`, `y`) gives a consistent
system, and the saturating walk `e^{-ik_x sigma_x} e^{-ik_y sigma_y}`
solves it (verifier).

**Verdict.** T2 `PROVED_FOR_MINIMAL_SUPPORT`: no s=2 walk on the
hexagonal substrate with `F within {0} U vert(H)` reaches `c_0 = r_in`.
HX2 holds in this subclass; HX2 in general is OPEN. No supremum is
claimed for this subclass beyond T1's `sqrt3/2`, which it contains; the
gap here is qualitative (`<`), not a bound.

## 4. Attempt beyond minimal support (inconclusive)

The same reduction for the radius-2 hexagonal ball (19 points: origin,
inner ring, edge midpoints, vertices; contains JDW L6c) leaves 56 free real
parameters after the layer equations and 730 quadratic unitarity
equations. A grevlex Gröbner basis over the complex field did not finish
within the agreed 900 s cap (exit 124). Even a finished basis other than
`{1}` would not decide real solvability (the minimal case is consistent
over `C`; its contradiction is real). The attempt is recorded in the
exploratory script `scripts/explore_hex_saturation_support.py`; it is not
evidence for any verdict. Per the contract's stop rule, T2 is recorded as
`OPEN_AFTER_MINIMAL_SUPPORT_ANALYSIS`.

## 5. Not established

- T2 for supports with further lattice points (edge-interior or interior
  points, e.g. JDW L6c). HX2 is OPEN there. The minimal-support result does
  not extend by itself, and the failed computation is not evidence either
  way.
- Nothing for `s > 2`, other lattices, masses.
- No novelty claim: Bernstein is prior art; the T1 computation is
  elementary.

## 6. Next step

Independent cross-family review of L0, T1 and the minimal-support T2, then
a separate promotion. Extending T2 needs a new approach (e.g. a structural
argument on edge polynomials, or real-algebraic certificates) and is not
in progress. Then independent cross-family review and a
separate promotion.
