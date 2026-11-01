# Hexagonal ceiling — execution report (L0 and T1)

Date: 2026-11-01. Branch: `research/schur-stability-audit`.
Contract: [`HEX_CEILING_GATE.md`](../theory/HEX_CEILING_GATE.md),
preregistered at `8c56ced`.
Verifier: [`scripts/verify_hex_ceiling_gate.py`](../scripts/verify_hex_ceiling_gate.py),
18/18 exact checks (Python 3.12.3, `sympy==1.14.0`).
Author: Claude Code (Claude Opus 5.5), at the user's direction.

**Status: PARTIAL EXECUTION — L0 `PROVED_IN_REPO` (using the classical
scalar Bernstein inequality, prior art); T1 `GAP_PROVED_IN_CLASS` with
supremum `sqrt3/2`, attained; T2 not started.** Evidence **PRELIMINARY**
(no independent review). Not promoted.

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
`N` with `|p| <= 1` (U unitary). The classical Bernstein inequality (prior
art) gives `|p'(0)| <= N`, i.e. `|<y, dU/dt(0) x>| <= N delta = h_C(n_f)`
along `n_f`. Taking the supremum over `x, y`,
`||A(n_f)|| <= h_C(n_f) = r_in`, where `A(n) = i dU(t n)/dt (0)`. For
`s = 2` with a traceless isotropic cone, `A(n_f)^2 = c_0^2 I`, so
`||A(n_f)|| = c_0`. Therefore **`c_0 <= r_in` for every walk in `W_hex`**.

Scope: the Bernstein inequality is used, not reproved; the in-repo content
is the grid reduction and the application. Only the facet normal is
needed, since `r_in = min h_C` is attained there.

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
the traceless part of `M` is linear in `(g_12, g_13, g_23)` with a rank-2
coefficient matrix whose kernel is `(1,1,1)`. Geometrically, the three
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

i.e. iff the three Bloch vectors are coplanar at mutual 120°. This bound
uses only the node and isotropy; the hexagon condition only restricts the
set further.

**Attainment.** The verifier builds the walk with
`t_j = (cos 2pi j/3, sin 2pi j/3, 0)` and certifies exactly: unitary
symbol, `F = {0, ±2 u_j}`, regular hexagonal hull (6 vertices, 6 facets,
`r_in = sqrt3/2`), every vertex coefficient non-nilpotent, `U(0) = I`,
untilted isotropic cone, `c_0 = 3/4`, `c_0/r_in = sqrt3/2`.

**Explains the previous table.** ADMP's `tau_i` (Eq. (5)) have `g = 1/3`,
giving `c_0 = 1/2` (verifier, reproducing row L6a of Sec. 11). JDW L6d has
`c_0 = 3/4`, the maximum, which corresponds to `g = -1/2`. The ADMP–JDW
difference on the same substrate is the difference in the overlap of the
three coin axes: ADMP's axes are tilted out of a common plane by
`xi = sqrt5/3`, which costs speed.

**Verdicts.** T1 `GAP_PROVED_IN_CLASS`: `sup c_0/r_in = sqrt3/2`,
attained exactly at coplanar 120° Bloch vectors. HX1
`CONFIRMED_IN_CLASS` (T1 subclass). HX0 `CONFIRMED_IN_CLASS` (L0, all of
`W_hex`).

## 3. Not established

- T2 (all of `W_hex`: more factors, skew partial shifts, other step
  lengths) is not started. HX2 is OPEN. The T1 result does not extend to
  T2 by itself.
- Nothing for `s > 2`, other lattices, masses.
- No novelty claim: Bernstein is prior art; the T1 computation is
  elementary.

## 4. Next step

T2, under the same contract. Then independent cross-family review and a
separate promotion.
