# DISPERSION_CORRECTIONS_ACROSS_LATTICES — frozen contract

**Status of this text:** frozen at the commit that introduces it; that
commit is the preregistration commit. Authorized by user instruction of
2026-11-02 («haz lo que consideres, estás autorizado») on the draft
revised as recorded in `state/CURRENT_STATE.md` Sec. 13. Nothing computed
before this commit.
**Parent:** `C_ACROSS_LATTICES` (`theory/C_ACROSS_LATTICES_GATE.md`), its
table of massless rows, and `L6B_TRIANGULAR_ROW` for row L6b (promoted
2026-11-02). Those rows are input; none is recomputed.
**Initial scientific status: OPEN.**

## 0. Single question

> For each declared row, how does the propagation speed depart from the
> constant `c_0` as the wavelength approaches the lattice scale: what is
> the exact lowest-order correction to the massless dispersion, its order,
> its sign, and what angular pattern the walk's symmetry imposes on it?

`c_0` is one number per row and says nothing about the shape of the
lattice beyond `r_in`. The first correction is where the substrate's
symmetry, as far as the walk keeps it, becomes visible in the dispersion.
This gate computes that correction exactly and tabulates it; it does not
interpret it physically.

## 1. Background taken as input

- Massless table of `C_ACROSS_LATTICES` (`reports/2026-11-01--c-across-
  lattices.md` Sec. 4) and row L6b (`reports/2026-11-02--l6b-triangular-
  row.md`, promoted 2026-11-02): symbols, nodes, `c_0`, `r_in`,
  `c_strict^iso` per row.
- `c_H` and `c_{omega^2}` are kept distinct for massive rows (PROJECT_
  INSTRUCTIONS §3). This gate is massless only, so a single `omega(k)`.
- The 4B closure (`CURRENT_STATE.md` Sec. 8.21): the model fixes no
  absolute scale; `ell` (lattice step) and `tau` (update time) are free.
  Every quantity here is therefore dimensionless, in units `ell = 1`
  (longest step) and `tau = 1`.
- Claim ceiling of Sec. 8.9(iii) / Sec. 8.21: no claim about our universe.
  No dictionary to observations is part of this gate (Sec. 5).
- Symmetry facts used in Sec. 3, elementary and prior art, stated here so
  that no hypothesis is decided by them unknowingly. A homogeneous
  polynomial of degree `n` in `(k_x, k_y)` invariant under rotation by
  `2 pi / m` is a combination of `|k|^n` and `|k|^(n-jm) Re/Im (k_x + i k_y)^(jm)`,
  `jm <= n`. Hence under `C_6` there is no invariant of odd degree and the
  degree-4 invariant is `|k|^4` alone: the first anisotropic term can only
  appear at degree 6 (`cos 6 theta`, relative order `|k|^4`). Under `C_3`
  alone, `cos 3 theta` is allowed at degree 3 (relative order `|k|`), an
  odd term. Under `C_4`, `cos 4 theta` is allowed at degree 4. Under the
  cubic group, the degree-4 cubic harmonic `k_x^4 + k_y^4 + k_z^4 -
  (3/5)|k|^4` is allowed.

## 2. Rows and the source of each symbol

All rows of the parent massless table with a symbol in a versioned
script, imported read-only (the bytes of a reviewed verifier are not
changed):

| Row | Substrate | Symbol taken from |
| --- | --- | --- |
| L1 | line | `verify_weyl_dirac_gate.published_symbol(1, 1, ·)` |
| L2 | square | `verify_weyl_dirac_gate.published_symbol(2, 1, ·)` |
| L6e | square | `verify_c_across_lattices_gate.row_L6e()` |
| L3 | BCC | `verify_directional_saturation.walk2()` (CJWW (5.15)) |
| L5a | BCC | `verify_c_across_lattices_gate.row_L5a()` |
| L5b | BCC | `verify_c_across_lattices_gate.row_L5b()` |
| L3s4 | BCC, `s = 4` | `cert_Aa_s4_counterexample.core(a, theta)` with `a` symbolic, `0 < a < 1`, at the massless point recorded in `CURRENT_STATE.md` Sec. 4.1 |
| L4 | cube `[-1,1]^3` | `verify_directional_saturation.walk1()` (CJWW (5.12)) |
| L6a | hexagon | `verify_c_across_lattices_gate.row_L6a()` |
| L6c | hexagon | `verify_c_across_lattices_gate.row_L6c()` |
| L6d | hexagon | `verify_c_across_lattices_gate.row_L6d()` |
| L6f | hexagon | `verify_c_across_lattices_gate.row_L6f()` |
| L6b | hexagon, `s = 6` | `verify_l6b_triangular_row_gate.step_symbol(...)` cubed, `V = U^3`, one admissible assignment and one coin reading, as the L6b report fixes them (all six are isometric) |

If a listed constructor turns out not to return the symbol in the form
the parent used, the row is marked `OPEN (symbol not reusable)` with the
reason; no new walk is constructed and no symbol is retranscribed from a
paper inside this gate.

## 3. Quantities per row (exact, SymPy, zero tolerance)

At the massless node of the row (at `k = 0` in every parent row, `U(0) = I`),
with `omega(k)` the quasienergy branch of the node and `k = |k| n̂`:

1. **Expansion.** `omega(k) = c_0 |k| [1 + beta(n̂) |k| + alpha(n̂) |k|^2
   + O(|k|^3)]`, obtained from the exact characteristic polynomial of the
   symbol along the ray `k = |k| n̂` (equivalently from `cos omega` or
   `omega^2` as the row's node structure allows), as functions of the
   direction cosines with radical coefficients. No series fitting. The
   first thing recorded is the **order of the lowest nonvanishing
   correction**: `beta` (relative order `|k|`, possible only if
   `omega(k) != omega(-k)` at the node) or `alpha` (relative order
   `|k|^2`). Evenness `omega(k) = omega(-k)` is checked per row, not
   assumed; the parent's "zero tilt" certifies only the linear term.
2. **Symmetry group of the walk.** For each row, the subgroup `G_walk`
   of the substrate point group under which the node dispersion is
   invariant, decided exactly by equality of characteristic polynomials
   of the symbol at `k` and `g k` (the test the L6b verifier used for the
   twelve isometries of the hexagon). `G_walk` may be smaller than the
   point group of the lattice; the harmonics allowed are those of
   `G_walk`, not of the substrate.
3. **Angular pattern.** Decompose the lowest nonvanishing correction into
   the harmonics allowed by `G_walk` (Sec. 1): `d = 1`: constant;
   `C_4`/`D_4`: `alpha_0 + alpha_4 cos 4 theta`; `C_3`: `beta_3 cos 3 theta`
   at relative order `|k|` (then `alpha` at the next order); `C_6`/`D_6`:
   `alpha_0` isotropic, no anisotropy possible at this order; cubic:
   isotropic part plus the degree-4 cubic harmonic. Record the isotropic
   part and every anisotropic coefficient exactly. For rows whose first
   correction is isotropic by symmetry (`C_6`), also compute the next
   order (relative `|k|^4`) to exhibit the first anisotropic coefficient
   `alpha_6`, if exactly feasible; otherwise record
   `ANISOTROPY_AT_HIGHER_ORDER_OPEN`. That no forbidden harmonic appears is
   a consistency check on the symbol, not a result.
4. **Sign.** For each row: sign of the isotropic coefficient of the lowest
   even correction `alpha_0` (`< 0`: subluminal at short wavelength; `= 0`;
   `> 0`), and whether the full correction changes sign with direction.
5. **Group velocity at the node.** `|grad_k omega|` to the same order, so
   the correction to `c_0` in the group speed, direction by direction;
   and, where exactly certifiable, `V_grp^max` of the node branch
   (otherwise `OPEN`, as in the parent).
6. **Scale of validity.** The smallest `|k|` at which the node branch
   meets another branch or `omega` stops being analytic, if finite and
   exactly computable; else `OPEN`.

Cross-checks: for L1 the result must reproduce the one-dimensional Dirac
walk expansion (`omega = arcsin`-type dispersion); rows that share a
substrate and `c_0` (L6c, L6d, L6f) are compared; L6b's `V` is compared
with L6a up to the 60° isometry already recorded; for every row the
harmonic content found in item 3 must be consistent with `G_walk` found
in item 2.

## 4. Hypotheses, stated before solving

- **Hd.** In every declared row `alpha_0 < 0`: the lattice is subluminal
  at short wavelength.
- **He.** In every row with `d >= 2` and `c_0 = r_in` (rows that reach
  the ceiling: L2, L6e, L3, L5a, L5b, L4 at freeze; L1 excluded because
  no anisotropy exists in `d = 1`), the anisotropic coefficient of the
  lowest nonvanishing correction is nonzero: a walk that reaches the
  ceiling shows the substrate's shape in its first correction. No
  hexagonal row reaches the ceiling, so the `C_6` isotropy of Sec. 1 does
  not decide He.
- **Hf.** Rows on the same substrate (square: L2, L6e; BCC: L3, L5a, L5b;
  hexagonal: L6a, L6c, L6d, L6f, L6b) do not all share the same
  correction function: the correction is walk-dependent, not fixed by the
  substrate. Hf is refuted only if two rows on one substrate have
  identical `beta(n̂)` and `alpha(n̂)`; it is confirmed in a substrate if
  any two differ.

Refuting any of them is a valid outcome. A pattern is a pattern in the
declared list, not a law. A hypothesis decided by the symmetry facts of
Sec. 1 alone is recorded as `DECIDED_BY_SYMMETRY`, not as a computed
result.

## 5. Deferred, not part of this gate

A conditional dictionary (`omega^2 = c^2 k^2 [1 + xi_1 (k ell) + xi_2
(k ell)^2 + ...]`, bounds on `ell` per row from observational bounds on
`xi_1`, `xi_2`) was in the draft and is removed: it is a second question,
it would need the extra hypothesis that a row's massless excitation is
the photon, and the expected close is `NO_COMPARABLE_OBSERVABLE_READ`.
If wanted after Phase 1 is reviewed, it needs its own charter and its own
user authorization; this gate makes no statement about our universe.

## 6. Stop rules

- Stop when every row has items 1–6 filled or `OPEN` with reason.
- No numerics in a certified entry; no series fitting; no new walks or
  lattices; no massive rows; no interacting or inhomogeneous models.
- Reviewed verifiers are imported read-only; their bytes are not changed.
- If a row's series extraction does not finish exactly (SymPy) within one
  session, the row is `OPEN (not extracted)`; no floating-point fallback.

## 7. Exclusions

Same as the parent §7. Additionally: no Lorentz-violation model building
(no DSR, no Horava-type Lagrangians), no detector or source modelling, no
observational comparison, no claim about our universe.

## 8. Verdicts

- `CORRECTIONS_TABLE_COMPLETE` / `CORRECTIONS_TABLE_PARTIAL_<reason>`.
- Per hypothesis: `CONFIRMED_IN_DECLARED_ROWS` / `REFUTED_BY_ROW_<Id>` /
  `DECIDED_BY_SYMMETRY`.

## 9. Deliverables

- `reports/YYYY-MM-DD--dispersion-corrections-across-lattices.md`.
- `scripts/verify_dispersion_corrections_gate.py`, fail-closed, exact,
  importing reviewed symbols read-only; two exact command forms in
  `.claude/settings.json`.
- Independent cross-family review before any promotion; promotion is a
  separate commit updating `state/CURRENT_STATE.md` Sec. 13.
