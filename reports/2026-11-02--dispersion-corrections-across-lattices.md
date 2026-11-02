# Dispersion corrections across lattices — execution

**Date:** 2026-11-02
**Gate:** `DISPERSION_CORRECTIONS_ACROSS_LATTICES`, contract
[`theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md`](../theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md),
preregistration commit `a7ff5b7` (contract SHA256
`6df09e81fae231ebbb00d19de546298559d333d33e965c95a1aa6027842231ea`).
**Parent:** `C_ACROSS_LATTICES` massless table and `L6B_TRIANGULAR_ROW`
(both promoted). No row is recomputed; every symbol is imported read-only
from the script named in contract Sec. 2.
**Verifier:**
[`scripts/verify_dispersion_corrections_gate.py`](../scripts/verify_dispersion_corrections_gate.py),
SHA256 `791f0d80d2790f34b72521c90622fa0056fd629fa1b3ef89addfc2ad664e6c2a`, 79/79 exact checks (Python 3.12.3,
`sympy==1.14.0`, interpreter `/home/adnac/venvs/torch-gpu/bin/python`, as
`scripts/README.md` records for earlier runs; the system `python3` has no
SymPy). Run time about 11 min, dominated by the symmetry test of
L3s4. The imported verifiers are unchanged.
**Status:** `CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN` —
PRELIMINARY, independent review pending. Nothing is promoted by this report.

## 1. Result

Units as in the parent: Cartesian positions divided by the longest step
of one update, one update per time unit (L6b: `V = U^3`, quasienergy
divided by 3). Along a ray `k = t n̂`, `|n̂| = 1`, the upper branch of the
massless node is

`eps_+(t n̂) - eps_0 = c_0 t [1 + beta(n̂) t + alpha(n̂) t^2 + O(t^3)]`.

`alpha_0` is the mean of `alpha` over the unit circle or sphere. In
`d = 2`, `theta` is the angle of `n̂` in the row's Cartesian frame; in
`d = 3`, `K4 = n1^4 + n2^4 + n3^4 - 3/5`, `K6` is the part of
`n1^2 n2^2 n3^2` orthogonal to 1 and `K4` on the sphere, and
`sigma2 = n1^2 n2^2 + n2^2 n3^2 + n3^2 n1^2`.

| Row | Substrate | `c_0` | `G_walk` (exact) | Lowest correction | `beta(n̂)` | `alpha(n̂)` | `alpha_0` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L1 | line | 1 | `{±1}` | none: `omega = |k|` exactly | 0 | 0 | **0** |
| L2 | square | `1/sqrt2` | `D_4` (8) | `alpha`, anisotropic | 0 | `-n1^2 n2^2/12 = -(1 - cos 4θ)/96` | `-1/96` |
| L6e | square | `1/sqrt2` | `D_4` (8) | `alpha`, anisotropic | 0 | identical to L2 | `-1/96` |
| L3 | BCC | `1/sqrt3` | `O_h` (48) | `alpha`, anisotropic | 0 | `-sigma2/18 = -1/90 + K4/36` | `-1/90` |
| L5a | BCC | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `(sqrt3/3) n1 n2 n3` | `-sigma2/18 - n1^2 n2^2 n3^2/6` | `-4/315` |
| L5b (each Weyl block) | BCC | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `±(sqrt3/3) n1 n2 n3` | as L5a | `-4/315` |
| L4 | cube | `1/sqrt3` | 24, `T_d` | `beta`, anisotropic | `-(sqrt3/3) n1 n2 n3` | as L5a | `-4/315` |
| L3s4 (each cluster) | BCC, `s = 4` | `a/sqrt3` | 8 (`D_2` half-turns and the `x <-> z` swap composed with them) | `beta`, isotropic + anisotropic | `±[sqrt3 (1-a^2)/(6a) + sqrt3 (2a^2-1)/(3a) n1 n2 n3]`, upper sign for the cluster at `+pi/4` | non-cubic content (Sec. 3.4) | `2(27a^4 - 34a^2 + 5)/(315 a^2)` |
| L6a | hexagon | `1/2` | `D_3` (6) | `beta`, anisotropic | `-(sqrt15/36) cos 3θ` | `-41/1728 - (5/1728) cos 6θ` | `-41/1728` |
| L6c | hexagon | `3/4` | `D_6` (12) | `alpha`, isotropic | 0 | `-1/512` | `-1/512` |
| L6d | hexagon | `3/4` | `D_6` (12) | `alpha`, isotropic | 0 | `-1/128` | `-1/128` |
| L6f | hexagon | `3/4` | `D_6` (12) | `alpha`, isotropic | 0 | `-1/128` | `-1/128` |
| L6b (each orientation block) | hexagon, `s = 6` | `1/3` | `D_3` (6) | `beta`, anisotropic | `(sqrt15/18) cos 3θ` | `-41/432 - (5/432) cos 6θ` | `-41/432` |

First anisotropy of the isotropic hexagonal rows, at relative order
`t^4` (coefficient of `cos 6θ` in `E_5 / c_0`): L6c `1/184320`, L6d
`1/11520`, L6f `-1/11520`. L6d and L6f therefore agree through relative
order `t^2` and differ at `t^4` by the sign of the `cos 6θ` term, that is,
by a 30° rotation of the anisotropy.

Hypotheses (contract Sec. 4):

- **Hd** (`alpha_0 < 0` in every row): **`REFUTED_BY_ROW_L1`**. L1 has
  `alpha_0 = 0`, because its symbol is `exp(-i k sigma_z)` and the
  dispersion is exactly linear. The refutation is not only the degenerate
  1D row: L3s4 has `alpha_0 > 0` for `0 < a < a*` and `< 0` for
  `a* < a < 1`, with `a* = sqrt3 sqrt(17 - sqrt154) / 9` (exact root,
  Sturm count 1; `a* ≈ 0.412`). Every other row has `alpha_0 < 0`.
- **He** (ceiling rows with `d >= 2` have a nonzero anisotropic
  coefficient in their lowest correction): **`CONFIRMED_IN_DECLARED_ROWS`**.
  L2, L6e: `cos 4θ` at relative order `t^2`. L3: `K4` at `t^2`. L5a, L5b,
  L4: the odd invariant `n1 n2 n3` at relative order `t`. Not decided by
  symmetry: `D_4`, `O_h` and `T_d` allow these terms but do not force
  them.
- **Hf** (no two rows on one substrate share `beta` and `alpha`):
  **`REFUTED_BY_ROW_L6e`**. L2 and L6e have identical `beta`, `alpha`,
  group-velocity coefficients and `t^4` harmonics. Further shared pairs:
  L5a with each Weyl block of L5b, and L6d with L6f through relative order
  `t^2`. Under the weaker reading of Hf's header ("do not all share"),
  the square substrate also refutes it, since it has only these two rows.
  On the hexagon and BCC substrates the corrections are not all equal.

Under the contract's exact procedure, the `C_6` isotropy of Sec. 1 decides
no hypothesis: He concerns rows that reach the ceiling, and no hexagonal
row does.

## 2. Method (contract Sec. 3)

For each row the symbol is expanded exactly as a Taylor polynomial in `k`
to total degree `N` (`N = 6` in `d <= 2`, `N = 4` in `d = 3`). The node
branch is read from the quadratic factor `lambda^2 - s1 lambda + s2` of
the characteristic polynomial that carries the node:

- `s = 2` rows: the whole characteristic polynomial.
- L5b (`s = 4`): `Gamma = dP_X dP_Y dP_Z` commutes with every Fourier
  coefficient and `Gamma^2 = -I`; its two eigenspaces give two `2x2`
  Weyl blocks.
- L6b: the three `2x2` orientation blocks of `V = U^3`, as in the L6b
  verifier.
- L3s4: Hensel lifting of the quadratic factor at the double root
  `exp(∓ i pi/4)` of `A_a(0) = W`. The characteristic polynomial is
  computed from Newton's identities on truncated power traces; the script
  checks this route against the full characteristic polynomial on the
  `4x4` L5b symbol. The parameter is kept symbolic: `a` and
  `b = sqrt(1-a^2)` are independent symbols reduced with `b^2 = 1 - a^2`.
  This keeps the zero test exact, because `sqrt(1-a^2)` is not a rational
  function of `a`.

From `s1`, `s2`: `exp(-2i phi) = s2 / s2(0)` gives the common phase
`phi(k)` of the two node levels, and `cos^2 omega = s1^2/(4 s2)` gives
`omega^2(k)` as a power series with exact homogeneous parts. Then
`eps_± = eps_0 + phi ± omega`. No series is fitted; every coefficient is
an exact algebraic number or, for L3s4, an exact rational function of
`a`. The Taylor coefficients of `arccos(1-v)^2`, `log(1+v)`, `sqrt(1+v)`
and `1/(1+v)` are checked against SymPy's series.

`G_walk` is the set of point-group elements `g` of the substrate with
`charpoly U(g k) = charpoly U(k)` as Laurent identities. In characteristic
0 this equals equality of `tr U^m`, `m = 1..s`, and `tr U(gk)^m` is
`tr U^m` under the monomial substitution `z^h -> z^(Mh)`. The angular
content is read as a trigonometric polynomial in `d = 2` and projected on
`1, K4, K6` in `d = 3` (and `beta` on `1, n1 n2 n3`). A zero residual is
certified wherever `|G_walk| >= 24`.

## 3. Findings per item

### 3.1 Order of the lowest correction

Every node is untilted at linear order, as the parent certified. The
lowest correction has relative order `t` (a `beta` term) exactly in the
rows whose `G_walk` lacks inversion: L5a, L5b, L4 (`T_d`-type, 24
elements), L6a and L6b (`D_3`), and L3s4. In every row whose `G_walk`
contains `k -> -k` (L1, L2, L6e, L3, L6c, L6d, L6f), `omega^2` has no odd
terms through the computed order and the lowest correction is `alpha`.
The draft charter assumed evenness; the frozen contract required it to be
checked, and six of the thirteen rows are not even.

### 3.2 Angular pattern and the walk's group

The harmonic content matches `G_walk` in every row:

- `D_6` rows (L6c, L6d, L6f): `alpha` isotropic and `cos 6θ` first at
  relative order `t^4`, as the degree argument of contract Sec. 1 forces.
- `D_3` rows (L6a, L6b): `cos 3θ` at relative order `t`. The `cos 6θ` in
  `alpha` comes from `beta^2`; the degree-4 part of `omega^2` is
  isotropic (`Q4 = -1/96` for L6a).
- `D_4` rows (L2, L6e): `cos 4θ` at `t^2`.
- `O_h` row (L3): `K4` at `t^2`.
- 24-element cubic rows: `n1 n2 n3` at `t`, then `1, K4, K6` at `t^2`.

The three ADMP/JDW hexagonal walks with `c_0 = 3/4` have the full `D_6`.
ADMP's L6a has only `D_3`, and so has L6b, which realises L6a's dispersion
after three updates.

### 3.3 Sign

- `alpha <= 0` pointwise in L2, L6e, L3, L5a, L5b, L4 (closed forms in
  Sec. 1), vanishing only along the coordinate axes. `alpha < 0` pointwise
  in L6a, L6b (`-46/1728 <= alpha <= -36/1728` for L6a), L6c, L6d, L6f.
- In the rows with `beta != 0`, the lowest correction takes both signs: it
  is odd under `n̂ -> -n̂`. These rows are not "subluminal at short
  wavelength" in every direction even though `alpha_0 < 0`. The phase
  speed of the upper branch exceeds `c_0` near the node where
  `beta(n̂) > 0`, for example along `n1 n2 n3 > 0` in L5a.
- L3s4: `alpha_0` changes sign at `a*` (Sec. 1).

### 3.4 L3s4: a branch-dependent quadratic term

L3s4 is the only row with `phi != 0`. The two levels of each cluster move
together as `phi = ±(1 - a^2) t^2 / 6 + O(t^4)`, with opposite signs for
the clusters at `±pi/4`. This is consistent with second-order repulsion
between the clusters through the intersector coupling `b^2 = 1 - a^2`. It
gives `beta` an isotropic part `±sqrt3 (1-a^2)/(6a)` of opposite sign on
the upper and lower branch of a cluster; `alpha` is the same for both
branches and both clusters. `G_walk` has 8 elements, so `alpha` has
content outside `span(1, K4, K6)`. The verifier prints it; it is not
tabulated further here. At `a = 1` the isotropic part of `beta` vanishes,
and `beta = (sqrt3/3) n1 n2 n3` with `alpha_0 = -4/315`, the values of
L5a.

### 3.5 Group velocity at the node

`|grad eps_+| / c_0 = 1 + 2 beta(n̂) t + O(t^2)`, and `1 + 3 alpha(n̂) t^2
+ O(t^4)` where `beta = 0`. The coefficients through relative order `t^4`
(`d <= 2`) or `t^2` (`d = 3`) are printed per row by the verifier.
`V_grp^max` is `OPEN` for every row in `d >= 2`, as in the parent. For L1,
`omega = |k|` on the whole branch, so its group speed is 1 everywhere;
this follows from the symbol `exp(-i k sigma_z)` and is checked by the
script only through `t^5`.

### 3.6 Scale of validity

L1: the branches meet first at `|k| = pi` (exact). `d >= 2`: `OPEN`. The
exact minimisation of `|k|` on the branch-meeting set was not attempted,
as contract Sec. 3 item 6 allows.

## 4. Cross-checks and second route

- **L1** reproduces the exactly linear 1D massless walk: all corrections
  vanish through `t^5`.
- **Closed forms by hand.** For a symbol with `cos omega = prod_i cos p_i`
  and `p = k / sqrt d`, the expansion `log cos x = -x^2/2 - x^4/12 +
  O(x^6)` gives `omega^2 = |p|^2 - (1/3) sum_{i<j} p_i^2 p_j^2 + O(p^6)`,
  hence `alpha = -sum_{i<j} n_i^2 n_j^2 / (6d)`. This is `-n1^2 n2^2/12`
  for L2 and `-sigma2/18` for L3. For the chiral BCC rows,
  `alpha = (3/2) Q4 - Q3^2/(8 c_0^4)` with `Q4 = -sigma2/27` and
  `Q3 = (2 sqrt3/9) n1 n2 n3` gives `-sigma2/18 - n1^2 n2^2 n3^2/6`. The
  verifier asserts all three forms against its series output.
- **L6b vs L6a.** With each row's normalisation,
  `eps_L6b(k) = eps_L6a(2 R k) / 3` for a 60° rotation `R`. So
  `c_0` scales by `2/3`, `beta` by 2 and `alpha` by 4. All three are
  asserted exactly. The rotation reverses the sign of `cos 3θ`, which is
  why `beta` changes sign between the two rows. The three orientation
  blocks of L6b give identical results.
- **L6c, L6d, L6f:** compared in Sec. 1.
- **L5b:** both Weyl blocks give the same `alpha` and opposite `beta`.
  **L3s4:** both clusters give the same `alpha`.

## 5. Corrections made during the execution

- The first runs used the full characteristic polynomial; for L3s4 with
  symbolic `a` it did not finish in an hour. It was replaced by Newton's
  identities on truncated power traces, cross-checked as stated.
- A rational parametrisation of `a` was tried and abandoned: SymPy merged
  `1 + u^2` with negative powers of `z`. The independent-symbol reduction
  replaced it.
- The first cross-check of L6b against L6a compared `alpha` without the
  scale factor 4. The second route above derived the factor, and the
  check was corrected before any passing run.
- Two per-row assertions assumed that `beta` is purely `n1 n2 n3` and that
  `alpha` is cubic-invariant. Both fail for L3s4, whose group has 8
  elements. They now apply only where `|G_walk| >= 24` and are reported
  descriptively otherwise.

## 6. What this does not claim

- No physical interpretation of `alpha` or `beta`, no observational
  comparison, no statement about our universe (contract Secs. 5, 7).
- Hf's refutation by L2 and L6e is one coincidence on one substrate. It is
  not evidence that the substrate fixes the correction in general; the
  hexagon and BCC substrates carry rows with different corrections.
- The observation that `alpha <= 0` pointwise in every row with
  `d >= 2` except L3s4 is a pattern in the declared list, found after
  solving. It is not a hypothesis of this gate and not a law.
- Not human review. No novelty claim.

## 7. Next step

Independent cross-family review of this report and of the verifier
(SHA256 above), then a separate promotion decision.
