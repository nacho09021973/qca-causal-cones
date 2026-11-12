# General infrared operational rate: Stage 2, leading term and non-vanishing

2026-11-12, session 2 of the Stages 1–2 budget. Claude (claude-opus-5-5).
Charter `GENERAL_IR_RATE_GATE.md` (`aa6c5f6`), Amendments 1 (`91be396`)
and 2 (`34f0601`); draft Amendment 3 (this commit). User instruction
«SIGUE». Author derivation, **PRELIMINARY, not reviewed**; no computation.

Pre-step record. Known: Stages 0–1 and the Stage 2 progress record
(`reports/2026-11-12--general-ir-rate-stage2-progress.md`). Question:
prove the leading term at zero momentum (A1) and the non-vanishing (A2)
in the amended class. Stop: any step needing a hypothesis not in force is
recorded as such.

Notation as in the manuscript where it exists. `m = d - 1` (in-plane
dimension). H3: `xi_* = kappa u`, `u` primitive, `kappa > 0`. Planes
`{u.x = k}` are translates of `Lambda_0 = Z^d cap u^perp`, of covolume
`|u|`, with spacing `1/|u|`. Every character trivial on `Lambda_0` has the
form `x -> omega^(u.x)`, `|omega| = 1`, because `Z^d/Lambda_0 = Z` through
`x -> u.x`.

## 1. Geometry

`v_* = w_B - w_A`, where `w_A` maximises `xi_*.w` on `A` and `w_B`
minimises it on `B` (the minimiser of a linear functional on the ball
`B - A` is unique, and Stage 1 shows `v_*` minimises `xi_*.v` there).
Put `x_* = N w_A`, `y_* = N w_B`, `R_A = N rho_A`, `R_B = N rho_B`.

Alice's sites near `x_*`: `x = x_* - delta u^ + u_perp`, with
`|u| delta = theta^A_N + j`, `j >= 0`, `theta^A_N = {N u.w_A}`. Bob's:
`y = y_* + delta' u^ + u'_perp`, `|u| delta' = theta^B_N + j'`,
`theta^B_N = {-N u.w_B}`. Tilt weights `e^(xi_*.(x - x_*)) = e^(-kappa(theta^A + j))`
and `e^(-xi_*.(y - y_*)) = e^(-kappa(theta^B + j'))`. On each plane, exactly,

    F_N = (4/R_A^2) eps^2,   eps = delta - delta^2/(2R_A) - |u_perp|^2/(2R_A),

and the same for `h_N` with `R_B`. (Manuscript: `R = N/4`, `4/R^2 = 64/N^2`.)

## 2. Free tail (generalises manuscript Lemma 7.2)

Let `e^(-i omega_0)` be the nodal eigenvalue at `p = 0`, `H_W` the linear
nodal Hamiltonian on the two-dimensional nodal space `V_0` (isotropic,
untilted, speed `c_IR`), `chi in V_0`. Then, uniformly in `y in Z^d`,

    r~(y) = N^(-d/2) e^(-i N omega_0) [ R_0(y/N) + O(N^(-1)) ],
    R_0(w) = c_r int g(q) e^(-i q.w) e^(-i H_W(q)) chi d^d q.

*Proof.* The resource is supported in `|p| <= 1/N`. The two nodal
eigenvalues are isolated from the other `s - 2` at `p = 0`, so their
spectral projector `Pi(p)` is analytic near `0`; `||(I - Pi(p)) chi|| = O(1/N)`
on the support, which contributes `O(N^(-d/2 - 1))` pointwise (sup norm
bounded by the `L^1` norm of the Fourier transform). On `Pi(p)`,
`S(p) = e^(-i omega_0) e^(-i H(p))` with `H = H_W + O(|p|^2)` (the
remainder bound uses the analyticity of the symbol and of the nodal
projector, and the absence of a constant or tilt term); with
`p = q/N`, Duhamel gives `e^(-i N H(q/N)) = e^(-i H_W(q)) + O(1/N)`, and
`Pi(q/N) = Pi(0) + O(1/N)`. ∎

H5: `R~ := R_0(w_B) != 0`.

## 3. Layer sums at a trivial point (generalises Layers (a)–(c))

For `f_1 = theta phi_N M chi` (`theta = (pi/2) F_N`) and `w = h_N M_B r`,
with `A`, `B` the tilted sums of manuscript Sec. 7.2 and `tau_A = sqrt(2 R_A) eta_t`,
`tau_B = sqrt(2 R_B) eta_t`:

**(a)** `|A_{f_1}(eta)|, ||B_w(eta)|| <= C N^(-5/2)` for all `eta`
(progress record, Sec. 2).

**(b)** For `|eta| <= r_0`,

    A_{f_1}(eta) = N^(-5/2) k_A phi_partial [ S^A(tau_A; theta^A_N) + E_A ] M chi,
    B_w(eta)    = N^(-5/2) k_B e^(i N omega_0) [ R~^dagger M_B S^B(tau_B; theta^B_N) + E_B ],

with `phi_partial = Phi_0(w_A)` (H7),
`k_A = 2 pi (2 rho_A)^(m/2) / (rho_A^2 |u|)`,
`k_B = 4 (2 rho_B)^(m/2) / (rho_B^2 |u|)`,

    S^X(tau; theta) = sum_{j>=0} e^(-kappa(theta + j)) Psi_{(theta+j)/|u|}(tau),
    Psi_delta(tau)  = int_{R^m} (delta - |sigma|^2)_+^2 e^(i tau.sigma) d^m sigma,

and `|E_A|, ||E_B|| <= C (N^(-1/2) + |eta_n|)` uniformly in the offsets.

**(c)** At a trivial dominant point `eta_k` with character `omega_k^(u.x)`,
the same holds with `S^X` replaced by the depth sum weighted by
`omega_k^(-j)` and with global unimodular factors
`e^(-i eta_k.x_*) omega_k^(floor(N u.w_A))` and
`e^(i eta_k.y_*) omega_k^(-ceil(N u.w_B))`. *(The continuous factors
`e^(-+i eta_k.x_*, y_*)` were omitted in the first version; added
2026-11-12 after the second Codex review. Their cancellation against
`e^(-i N eta_k.v_*)` is carrier Stage A, Sec. 2; exposition only.)*

*Proof of (b).* Plane by plane: in-plane Poisson summation over the
translate of `Lambda_0` gives `(1/|u|) int G_delta(y) e^(i eta_t.y) d^m y`
from `m = 0` and terms bounded by `||partial^3 G_delta||_M |2 pi m' - eta_t|^(-3)`,
`m' in Lambda_0^*`, summable for `m <= 2`; with
`r_0 <= (1/2) min |2 pi m'|` the frequencies stay at distance `>= pi |m'|`.
The total variation of the third derivative is
`O(N^(-d/2 - 2)[(delta/R)(R delta)^((m-1)/2) + (delta/R)^(1/2) R^(-1) (R delta)^(m/2)])
= O(N^(-4) delta^(d/2))`, against an `m = 0` term of order
`N^(-5/2) delta^(...)`: relative `O(N^(-3/2))`, uniform at `delta = 0`
(absolute bounds), with polynomial depth factors summable against the
tilt. In the `m = 0` term: `theta` is exact,
`theta = (2 pi / R_A^2) eps^2`; replacing `eps` by `delta - |y|^2/(2R_A)`
costs a relative `O(delta/R_A)`; `phi_N = N^(-d/2) phi_partial (1 + O(N^(-1/2)))`
on the support (it is `O(N^(-1))` when `c_A = 0`); `|e^(-i eta_n delta) - 1| <= |eta_n| delta`.
The substitution `y = sqrt(2 R_A) sigma` gives
`int e^(i eta_t.y)(delta - |y|^2/(2R_A))_+^2 d^m y = (2 R_A)^(m/2) Psi_delta(tau_A)`.
Collecting `N^(-d/2) (2 pi / R_A^2)(1/|u|)(2 R_A)^(m/2) = N^(-5/2) k_A`.
Planes with `delta > R_A/2` and the depth tail are `O(e^(-cN))`. Bob is the
same with `h_N = (4/R_B^2) eps'^2` and Sec. 2, which supplies
`e^(i N omega_0)` (complex conjugate of the tail's phase) and
`R~^dagger M_B`; the variation of `r` across Bob's layer is
`O(N^(-d/2 - 1/2))` and is bounded without oscillation as in manuscript
Layers (b). (c) is the same computation with the character written as
`omega_k^(u.x)`. ∎

Check against the manuscript (`d = 3`, `u = (1,1,1)`, `rho = 1/4`,
`omega_0 = 0`): `N^(-5/2) k_A = N^(-5/2) 16 pi / sqrt3` and
`N^(-5/2) k_B = N^(-5/2) 32 / sqrt3`, as in Layers (b).

## 4. Depth sums (generalises manuscript Lemma 7.3)

`S^X(tau; theta) = sum_n g^_tau(2 pi n) e^(2 pi i n theta)` with

    g^_tau(omega) = 2 pi^(m/2) |u| (|u| s)^(-3 - m/2) e^(-|tau|^2 / (4 |u| s)),   s = kappa + i omega.

*Proof.* `int_0^inf e^(-p delta)(delta - |sigma|^2)_+^2 d delta = 2 e^(-p |sigma|^2)/p^3`
and `int e^(-p|sigma|^2) e^(i tau.sigma) d^m sigma = (pi/p)^(m/2) e^(-|tau|^2/(4p))`;
then `x = |u| delta`. The function `x -> e^(-kappa x) Psi_{x/|u|}(tau) 1_{x>=0}`
is continuous and vanishes at `0`; `|g^| <= C |s|^(-3 - m/2)` is summable;
Poisson summation is exact. ∎ For `d = 3`, `|u| = sqrt3`, `kappa = t_*`
this is `c_g/s^4`, `c_g = 2 pi/(3 sqrt3)`, as in the manuscript.

## 5. Assembly at zero momentum

Near `eta = 0`, with H2, H8 and the progress record Sec. 3.1,
`e^(-N Phi_*) lambda_0(eta)^N e^(-i N eta.v_*) = e^(i N phi_0) e^(-N eta^T C eta / 2 + N rho_3(eta))`,
`C = Q + i Q'` accretive, `|rho_3| <= (1/4) eta^T Q eta` on `|eta| <= r_0`;
the other eigenvalues and `P_0(eta) - P_0` cost as in manuscript Thm 7.5.
The three replacements of that proof (Gaussian for the symbol, leading
forms for the layers, extension to `R^d`) cost `O(N^(-1/2))` relative,
with the same estimates; `|e^(-N eta^T C eta/2)| = e^(-N eta^T Q eta/2)`.
Integrating `eta_n` first (the leading layer forms do not depend on it)
and putting `zeta = sqrt(N) eta_t`:

    Z_1^(0) = e^(-K_* N) N^(-5 - d/2) e^(i N psi) [ c Gamma_0(theta^A_N, theta^B_N) + O(N^(-1/2)) ],

    psi = phi_0 + omega_0,
    c   = phi_partial k_A k_B (2 pi)^(-d) sqrt(2 pi / C_nn) (R~^dagger M_B e_0)(f_0^dagger M chi),
    Gamma_0(theta^A, theta^B) = int_{R^m} e^(-zeta^T S_C zeta / 2)
                                 S^A(sqrt(2 rho_A) zeta; theta^A) S^B(sqrt(2 rho_B) zeta; theta^B) d^m zeta,

with `C_nn = u^.C u^` (positive real part), `S_C` the Schur complement of
`C` on `u^perp` (accretive: inverses and compressions of accretive
matrices are accretive, and `S_C^(-1)` is a compression of `C^(-1)`), and
`P_0 = e_0 f_0^dagger` the rank-one dominant projector (H2). The power
`5 + d/2` is `13/2` for `d = 3`, as in the manuscript; with `d = 3`,
`psi = 0`, `C = Q` real and equal radii this reduces to manuscript
Thm 7.5's zero-momentum term.

The same holds at the other trivial dominant points with their own
`psi_k`, depth factors and coefficients `c_k` proportional to
`(R~^dagger M_B e_k)(f_k^dagger M chi)` (Sec. 3(c)).

## 6. Positive average of the depth factor (uses H9)

`Gamma_0` is continuous on `T^2` (the depth sums are continuous and
1-periodic in the offset, since the summand vanishes at depth `0`) and
bounded by some `M_Gamma`.

- Under H9(i), `(theta^A_N, theta^B_N)` is equidistributed on `T^2`
  (Weyl), so the average over `N` of `Gamma_0` is
  `int e^(-zeta^T S_C zeta/2) g^A(0) g^B(0) d^m zeta`. Both zero modes are
  positive Gaussians in `zeta`; the total quadratic form
  `S_C/2 + (rho_A + rho_B)/(2 |u| kappa) I` is strictly accretive; the
  Gaussian integral of such a form is `pi^(m/2) det^(-1/2)`. *Branch
  (added after review):* its eigenvalues satisfy `|arg lambda_j| < pi/2`,
  so for `m <= 2` the argument of the determinant stays in `(-pi, pi)`;
  along the segment to the Hermitian part the form stays strictly
  accretive, and at the positive-definite end the root is positive, so
  `det^(-1/2)` has positive real part. For `m >= 3` this argument fails;
  `d in {2, 3}` is essential here. So the average `mu` has `Re mu > 0`.
- Under H9(ii), the average is `sum_n int e^(-zeta^T S_C zeta/2) g^A(2 pi n) conj(g^B(2 pi n))`.
  For each `n` the prefactors give `|u s|^(-6 - m) > 0` and the exponent
  has the form `-zeta^T [S_C/2 + (rho_A/s + rho_B/s-bar)/(2|u|) I] zeta`,
  whose added part has real part `(rho_A + rho_B) kappa / (2 |u| |s|^2) > 0`:
  each term has positive real part and the series converges absolutely.
  So `Re mu > 0`.

Hence `Re Gamma_0(theta^A_N, theta^B_N) >= Re mu / 2` on a set of `N` of
lower density at least `Re mu / (2 M_Gamma)`.

## 7. Non-vanishing (A2) and the conclusion

Exact facts: `Z_1` is complex-linear in `M` and real-linear in `M_B`, so
`Im Z_1` is real-bilinear in `(M, M_B)`; `L_N = -2 Im Z_1 + 2 Re Z_2 + Q_N`
with `Z_2`, `Q_N` of lower order (progress record, Sec. 2).

Choose `(M, M_B)` in the real span of the declared family so that the
coefficients `c_k` of every other trivial dominant point vanish (H6:
`f_0` outside the span of the other `f_k`, then `M chi = v` with
`f_k^dagger v = 0`, `f_0^dagger v != 0`, `<chi, v>` real after a phase).
Their contributions are then `O(e^(-K_* N) N^(-5-d/2-1/2))`, and so are
those of the non-trivial dominant points and of the rest of the torus.
For such a protocol

    L_N = -2 e^(-K_* N) N^(-5-d/2) [ Im( e^(i N psi) Gamma_0(theta^A_N, theta^B_N) c ) + O(N^(-1/2)) ].

**What is still needed.** If two such protocols have coefficients `c` and
`i c`, the two brackets are `Im` and `Re` of the same complex number, so
one of them is at least `|Gamma_0| |c| / sqrt2 >= Re mu |c| / (2 sqrt2)` on
a set of positive density; one of the two protocols then has
`limsup e^(K_* N) N^(5 + d/2) |L_N| > 0`, whatever `psi` is. Without that
rotation, `Im(e^(i N psi) Gamma_0 c)` could tend to zero (progress record,
Sec. 3.2), and the condition `psi in pi Z` recommended there is **not
sufficient on its own**, because `Gamma_0` is complex when `Q' != 0`. The
rotation is not implied by the hypotheses in force; it is draft
**Amendment 3 (H10)**. A sufficient form: H6 holds for the left
eigenvectors and `e_0` is not a complex multiple of `R~`; then `M` removes
the other points and `M_B` alone sweeps `R~^dagger M_B e_0` over all of
`C` (for rank-one `K = e_0 R~^dagger`, the real-linear map
`M_B -> tr(M_B K)` on Hermitian matrices is onto `C` unless `e_0` is
parallel to `R~`).

**Conclusion, conditional on Amendment 3.** By bilinearity, if every basis
pair of the declared family had `e^(K_* N) N^(5+d/2) Im Z_1 -> 0`, so
would every protocol in their span. Hence some basis pair `(M_i, M_B,j)`
has `limsup e^(K_* N) N^(5+d/2) delta(N) > 0`; with Stage 1,

    lim sup_{N->inf} (1/N) log delta(N) = -K_*,

which is (T). Amendment 3 was approved by the user the same day. **Stage 2
verdict: `PROVED_UNDER_FROZEN_CONTRACT` (charter as amended by
Amendments 1–3), author derivation, PRELIMINARY, not reviewed.** Line
outcome: none of (a), (b), (c) of the charter.

## 8. K3 against H10

`e_0` is proportional to the second column of manuscript `P`,
`(-(1 + i c_*) alpha / c_*^2, 1 + alpha)`; `R~` to
`(-(1 + i) I_1/sqrt3, I_0 + I_1/sqrt3)` with `I_0, I_1 > 0`. The ratios of
first to second components have arguments `arg(-(1 + i c_*))` and
`arg(-(1 + i))`, equal only if `c_* = 1`; `c_* = cosh t_* > 1`. So `e_0`
is not parallel to `R~`. Left-H6: `S(-i xi_*)` is Hermitian, so
`f_0 = e_0`, and at `pi u` the projector is `P-bar`, so `f_pi = e_0-bar`;
`e_0` is not a complex multiple of a real vector (same argument), so `f_0`
is not in the span of `f_pi`. K3 satisfies H10 by hand derivation.

## 9. Limits

Author derivation by a Claude model; nothing reviewed. Constants not
explicit. Limsup form only; no claim on `liminf`, the prefactor or the
power as a verdict (the power `5 + d/2` is a by-product of the route). No
novelty claim.
