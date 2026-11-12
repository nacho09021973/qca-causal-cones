# General infrared rate on Bravais lattices: Stage 1 (written adaptation)

2026-11-12. Claude (claude-opus-5-5). Charter
`theory/GENERAL_IR_RATE_BRAVAIS_GATE.md`, preregistration commit `5eb6da9`
(frozen unchanged on the user's instruction «comienza por la fase 1»).
Author derivation, **PRELIMINARY, not reviewed**. No computation, no
verifier, no external transmission.

Pre-step record. Known: B1–B4 of the charter; the texts gone through are
`reports/2026-11-12--general-ir-rate-stages-0-1.md` ("S01"),
`reports/2026-11-12--general-ir-rate-stage2-progress.md` ("SP"),
`reports/2026-11-12--general-ir-rate-stage2-leading-term.md` ("LT") and
`reports/2026-11-12--ir-carrier-stage-a.md` ("CA"), all as they stand at
`5eb6da9` (Grok repairs included). Question: does every use of `Z^d` in
them transfer to a Bravais lattice `L` by the replacements of charter
Sec. 1? Stop: outcome (a) at the first step that does not.

## 0. Setting on `L`

`L = B Z^d`, `B` invertible real `d x d`, `covol(L) = |det B|`. Dual
lattice `L* = {k : k.x in Z for all x in L} = B^(-T) Z^d`. Walk on
`l^2(L; C^s)`, `(S psi)(y) = sum_{a in F} S_a psi(y - a)`, `F subset L`
finite. Fourier convention of the manuscript:
`psi^(p) = sum_{x in L} e^(i p.x) psi(x)`, periodic under `2 pi L*`;
Brillouin zone `T_L = R^d / 2 pi L*`, of volume `(2 pi)^d / covol(L)`;
normalised measure

    dmu_L = covol(L) d^d p / (2 pi)^d,     psi(x) = int_{T_L} e^(-i p.x) psi^(p) dmu_L(p),

with Parseval `sum_x |psi(x)|^2 = int |psi^|^2 dmu_L`. Kernel
`G_N(a) = int_{T_L} e^(-i p.a) S(p)^N dmu_L(p)`. The symbol is a finite sum
of `e^(i p.a)`, `a in L`, hence entire in `p in C^d` and `2 pi L*`-periodic.

**Primitive normal.** For `u in L*`, `u.L` is a subgroup `g Z` of `Z`; if
`g > 1` then `u/g in L*`. So `u` primitive in `L*` iff `u.L = Z`. H3 on `L`:
`xi_* = kappa u`, `kappa > 0`, `u` primitive in `L*`. Then:

- every plane `{u.x = k}`, `k in Z`, meets `L`, and its trace is a coset
  of `Lambda_0 = L cap u^perp` (rank `m = d - 1`);
- `L/Lambda_0 = Z` through `x -> u.x`, so a character of `L` trivial on
  `Lambda_0` is `x -> omega^(u.x)`, `|omega| = 1`;
- plane spacing `1/|u|`; `covol(L) = covol(Lambda_0) / |u|`, i.e.
  `covol(Lambda_0) = covol(L) |u|` (a fundamental cell of `L` is a cell
  of `Lambda_0` times one spacing);
- `e^(i eta.x)` is trivial on `Lambda_0` iff the in-plane component
  `eta_t` lies in `2 pi Lambda_0^*`, with `Lambda_0^*` the dual of
  `Lambda_0` inside `u^perp`.

*Second-way check of the covolume (rule 4).* Triangular lattice,
`b_1 = (1, 0)`, `b_2 = (1/2, sqrt3/2)`, `covol = sqrt3/2`,
`B^(-T) = [[1, 0], [-1/sqrt3, 2/sqrt3]]`. With `k = (1, 0)`,
`u = (1, -1/sqrt3)`, `|u| = 2/sqrt3`; `u.b_1 = 1`, `u.b_2 = 0`, so
`Lambda_0 = Z b_2`, covolume `1 = (sqrt3/2)(2/sqrt3)`; spacing `sqrt3/2`,
the distance from `b_1` to the line `R b_2`. BCC lattice (integer points
with three coordinates of equal parity), `covol = 4`, `u = (1,1,1)`:
`u.(1,1,1) = 3`, `u.(2,0,0) = 2`, so `u.L = Z` and `u` is primitive in
`L*` (while `u/2` is not in `L*`). Directly,
`Lambda_0 = 2 (Z^3 cap u^perp)` (odd points cannot sum to zero), covolume
`4 sqrt3 = covol(L) |u|`. Both agree with the formula.

## 1. Inventory of uses of `Z^d`

Every use found in S01, SP, LT, CA, with the replacement on `L`. "Exact"
means the step goes through with the same words; "constant" means only a
numerical factor changes (Sec. 4).

| # | Use | Where | On `L` | Status |
|---|---|---|---|---|
| U1 | torus `T^d`, measure `d^d p/(2 pi)^d` | S01 notation; LT Sec. 5; SP Sec. 2 | `T_L`, `dmu_L` | constant |
| U2 | real translation `eta -> eta + b e` unitary on `L^2(T^d)` | S01 Lemma 1.1 | `T_L` is a quotient of `R^d`; same | exact |
| U3 | contour shift `p -> p - i xi` (manuscript Eq. (11)) | S01 Thm 1.3 | symbol entire and `2 pi L*`-periodic | exact |
| U4 | site counts `|A_N|, |B_N| <= C N^d` | S01 Thm 1.3; SP Sec. 2 | `|N A cap L| <= vol(N A + V_L)/covol(L)`, `V_L` a Voronoi cell | constant |
| U5 | resource normalisation `Z_N`, `c_r` | LT Sec. 2 (`R_0`), Amendment 2 (`Phi_0`) | Parseval with `dmu_L` | constant |
| U6 | resource band inside the zone | LT Sec. 2 | `g(N p)` supported in `|p| <= 1/N`; inside one zone iff `N > 1/(pi lambda_1(L*))` | finitely many `N` excluded |
| U7 | `u` primitive integer, planes `{u.x = k}` | LT Sec. 1; CA Sec. 2 | `u` primitive in `L*`, `u.L = Z` | exact |
| U8 | `Z^d/Lambda_0 = Z`, characters `omega^(u.x)` | LT preamble, Sec. 3(c); CA Sec. 1 | Sec. 0 | exact |
| U9 | every depth index `j >= 0` is a non-empty plane; `u.x = floor(u.x_*) - j` | LT Sec. 1; CA Sec. 2 | `u.L = Z` | exact |
| U10 | in-plane Poisson summation, zero mode `1/covol(Lambda_0) = 1/|u|` | LT Sec. 3(b) | `1/(covol(L) |u|)` | constant |
| U11 | non-zero in-plane frequencies `2 pi m'`, `m' in Lambda_0^*`; `r_0`; inverse-cube sum in `m <= 2` | LT Sec. 3(b); SP Sec. 2 (non-trivial characters) | same with `Lambda_0^*` of `L` | exact (new `r_0`) |
| U12 | disc site count `O((N delta)^(m/2) + 1)` on a plane | SP Sec. 2 | cosets of `Lambda_0` | constant |
| U13 | depth offsets `theta^A_N = {N u.w_A}`, `theta^B_N = {-N u.w_B}`; H9 | LT Secs. 1, 6; CA Secs. 5, 8, 10 | same formulas with `u in L*` | exact |
| U14 | compactness of the torus (away from dominant points) | SP Sec. 2 | `T_L` compact | exact |

U2, U3, U6, U11, U12 and U14 are uses not listed in charter B3. None
fails. U6 is the only new condition, and it removes finitely many `N`,
which the limsup form of (T) does not see.

Steps that do not use the lattice at all and are therefore unchanged:
S01 Lemma 1.2 (Schur form), the Fenchel–Young step and the Schur test of
Thm 1.3 (apart from U4); the free-tail expansion of LT Sec. 2 apart from
U5–U6 (the node is a statement about `S(p)` near `p = 0` in Euclidean
momentum); the depth-sum Laplace/Poisson formula of LT Sec. 4 (it involves
only `|u|` and `kappa`); the Gaussian assembly of LT Sec. 5 apart from U1;
the averaging arguments of LT Sec. 6 and CA Secs. 5, 8, 10 (Weyl
equidistribution of `N u.w_A`, `N u.w_B`, `N (psi_i - psi_j)/2 pi`); the
bilinearity and rotation arguments of LT Sec. 7 and CA Secs. 6, 10.

## 2. B1 Stage 1 on `L`

Lemma 1.1: the multiplication operator by `S(. - i xi)` on
`L^2(T_L, dmu_L; C^s)`; conjugation by the translation by `b e` (U2) gives
`||F(a + ib)|| = ||F(a)||`; the subharmonicity argument is unchanged.
Lemma 1.2: no lattice. Thm 1.3: the contour shift (U3) and Lemma 1.2 give
`||G_N(y - x)|| <= C N^(s-1) e^(N Phi(xi_*) - xi_*.(y - x))` for
`x, y in L`; the convexity step uses `(y - x)/N in B - A`, which holds for
any points of `N A`, `N B`; the Schur test with U4. Hence, under H1 and
`0 < K_* < inf`,

    delta <= D_B <= 4 T_N <= C_L N^(d+s-1) e^(-K_* N),

with `C_L` depending on `L` through U4 only. The power is unchanged.

## 3. B1 Stage 2 on `L`

LT Sec. 1 (geometry): `w_A`, `w_B`, `v_*` do not involve the lattice;
depth parametrisation by U7, U9; tilt weights
`e^(xi_*.(x - x_*)) = e^(-kappa(theta^A + j))` because `xi_*.x = kappa u.x`
with `u.x in Z`. The exact formula for `F_N` on each plane is Euclidean.

LT Sec. 2 (free tail): `r(y) = int_{T_L} e^(-i p.y) S(p)^N phi^_N(p) dmu_L`.
For `N > 1/(pi lambda_1(L*))` (U6) the band is one ball in one zone, and
substituting `p = q/N` gives

    r~(y) = N^(-d/2) e^(-i N omega_0) [ R_0(y/N) + O(N^(-1)) ],    R_0 with c_r(L) of Sec. 4,

uniformly in `y in L`; the remainder bounds (spectral projector,
`O(|p|^2)` remainder, Duhamel, sup norm by the `L^1(dmu_L)` norm) are
unchanged.

LT Sec. 3 (layers): the only lattice inputs are U10–U12. (a): the absolute
bound `N^(-5/2)` is unchanged (it counts sites per plane with U12 and
uses the pointwise tail). (b): the zero mode of the in-plane Poisson sum
carries `1/(covol(L) |u|)`; the remainder bound
`||partial^3 G_delta||_M |2 pi m' - eta_t|^(-3)` is summed over
`m' in Lambda_0^*` (convergent for `m <= 2`) with
`r_0 <= (1/2) min_{m' != 0} |2 pi m'|`. The rest of the computation
(exact `theta`, replacement of `eps`, `phi_N = N^(-d/2) phi_partial (1 + O(N^(-1/2)))`,
the substitution `y = sqrt(2 R_A) sigma`) does not see the lattice. (c):
characters `omega_k^(u.x)` by U8.

LT Sec. 4 (depth sums): unchanged; `x = |u| delta` with `|u|` the length
of the primitive vector of `L*`.

LT Sec. 5 (assembly): the integral over the ball around `eta = 0`
carries `dmu_L = covol(L) d^d eta/(2 pi)^d` instead of `d^d eta/(2 pi)^d`.
The Gaussian replacements and their `O(N^(-1/2))` costs are unchanged.
The power `5 + d/2` is unchanged.

LT Sec. 6 (positive average): no lattice beyond U13. The branch argument
for `det^(-1/2)` depends on `m <= 2`, which is unchanged.

LT Sec. 7 (non-vanishing): no lattice. SP Sec. 2: the second-order
encoder term uses `int ||S~_N(eta)|| dmu_L <= C N^(-d/2)` (constant
change); the non-trivial-character bound uses U11 and needs
`eta_t notin 2 pi Lambda_0^*`, which is exactly non-triviality on
`Lambda_0` (Sec. 0); the off-dominant bound uses U14.

## 4. Constants

Write `||g||_2^2 = int_{R^d} g(q)^2 d^d q`.

- `Z_N(L) = covol(L) N^(-d) (2 pi)^(-d) ||g||_2^2`, from
  `||phi_N||^2 = Z_N^(-1) int g(N p)^2 dmu_L = 1`.
- `c_r(L) = covol(L)^(1/2) (2 pi)^(-d/2) ||g||_2^(-1)`, from
  `phi_N(x) = Z_N^(-1/2) covol(L) (2 pi)^(-d) N^(-d) int g(q) e^(-i q.x/N) d^d q`.
  Hence `Phi_0`, `phi_partial = Phi_0(w_A)` and `R_0`, `R~` scale as
  `covol(L)^(1/2)`; the conditions H5 and H7 (non-vanishing) and the
  sufficient radial-positivity forms of H7 do not change.
- `k_A(L) = 2 pi (2 rho_A)^(m/2) / (rho_A^2 covol(L) |u|)`,
  `k_B(L) = 4 (2 rho_B)^(m/2) / (rho_B^2 covol(L) |u|)`.
- Leading coefficient at a trivial dominant point (`eta = 0` or `eta_k`):

      c(L) = phi_partial k_A k_B covol(L) (2 pi)^(-d) sqrt(2 pi / C_nn) (R~^dagger M_B e) (f^dagger M chi).

  Counting powers of `covol(L)`: `1/2` (`phi_partial`) `+ 1/2` (`R~`)
  `- 2` (`k_A k_B`) `+ 1` (`dmu_L`) `= 0`. So `c(L)` is the `Z^d` formula
  with `|u|` the length of the primitive vector of `L*`: the explicit
  covolume factors cancel.

**Check against `Z^3` (charter Stage 1).** `covol = 1`, `L* = Z^3`,
`u = (1,1,1)` primitive with `|u| = sqrt3`: `dmu_L = d^3 p/(2 pi)^3`,
`c_r(Z^3) = (2 pi)^(-3/2) (512 pi/3465)^(-1/2) = sqrt(3465)/(64 pi^2)`
(with `||g||_2^2 = 4 pi int_0^1 (1 - r^2)^4 r^2 dr = 512 pi/3465`),
which is manuscript Eq. (7); `Z_N = 64/(3465 pi^2 N^3)`, manuscript
Sec. 3.3; `k_A = 16 pi/sqrt3`, `k_B = 32/sqrt3` at `rho = 1/4`, as in LT
Sec. 3 and manuscript Layers (b).

## 5. B2 (proved part) on `L`

CA Sec. 1: U8. CA Sec. 2: `u.x = floor(u.x_*) - j` and
`u.y = ceil(u.y_*) + j'` need only `u.L = Z` (U9); the cancellation of
`e^(+-i eta_k.(y_* - x_*))` against `e^(-i N eta_k.v_*)` is an identity
in `R^d`, so `psi_k = phi_k + omega_0 - phi u.v_*` is unchanged. CA
Sec. 3: depth sums with `sigma = kappa + i phi`, no lattice. CA Sec. 4:
`c_k(L)` as in Sec. 4 above. CA Secs. 5, 8, 10: averages and
equidistribution in `N u.w_A`, `N u.w_B`, `N (psi_i - psi_j)/2 pi`, with
`u in L*` (U13); no other lattice input. Hypotheses H6_k, H9_k, H10_k of
carrier Amendment 1 are read with `u` primitive in `L*` and characters
trivial on `Lambda_0 = L cap u^perp`. The proved cells stay proved under
the same hypotheses; the cell H6_k(ii) with H9(i) stays `OPEN`.

## 6. Observations outside the question (no verdict)

1. **Not a relabelling.** Writing `L = B Z^d` turns a walk on `L` into a
   walk on `Z^d`, but Euclidean balls become ellipsoids and an isotropic
   node becomes anisotropic, both outside B1's class. The enlarged class
   is therefore not obtained from B1 by a change of coordinates; it is
   obtained by repeating the proof, which uses the lattice only through
   U1–U14.
2. **Choice of lattice.** If the steps of a walk generate a proper
   sublattice `L' subset L`, the symbol on `T_L` is periodic under
   `2 pi L'*`, so every dominant point comes with copies carrying the same
   eigenvectors. Where such a copy has a character trivial on
   `L cap u^perp`, H6 (or H6_k(i)) fails automatically on `L`. On `L'`
   the walk is a different operator (one coset), with a different
   primitive `u`, `Lambda_0`, characters and offsets. Which reading
   applies to a diagnostic row is a Stage 2 question, not decided here.
3. **Admissibility.** B1's class requires admissibility in the sense of
   manuscript Definition 3.1, but S01, SP and LT contain no proof that the
   protocol family is admissible for a general walk of the class (a
   `grep -i admissib` over them finds only the non-vanishing of the
   denominators, S01 Stage 2). This gap is inherited unchanged on `L`; it
   does not involve the lattice and is not addressed by this charter.

## 7. Verdict

Every use of `Z^d` in B1 Stages 1–2 and in the proved part of B2 is one of
U1–U14; each transfers to a Bravais lattice of `R^d`, `d in {2, 3}`, by
the charter's replacements, with U6 excluding finitely many `N`. No new
analytic step and no change of hypotheses was needed.

**Stage 1: `PROVED_UNDER_FROZEN_CONTRACT` (charter `5eb6da9`); line
outcome (b), corollary.** Author derivation, PRELIMINARY, not reviewed.
The corollary inherits the status of what it transfers: B1 Stages 1–2
PASS in one sealed Grok review with repairs not re-reviewed; B2's proved
cells after one Grok review with REPAIR_REQUIRED and repairs not
re-reviewed; B2's `OPEN` cell stays open. Constants: Sec. 4.

Not done: Stage 2 (diagnostic consequence) is not authorized; the sealed
cross-family review proposed in charter Sec. 4 has not been requested. No
novelty claim.
