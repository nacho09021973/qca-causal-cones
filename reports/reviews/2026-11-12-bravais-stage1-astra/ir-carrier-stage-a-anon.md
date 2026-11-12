# Infrared carrier dichotomy, Stage A (regime R1)

2026-11-12. Claude (claude-opus-5-5). Charter
`theory/IR_CARRIER_DICHOTOMY_GATE.md` (`36adaa1`, naming addendum
`fd40996`). User instruction «adelante». Author derivation,
**PRELIMINARY, not reviewed**. The hypotheses H6_k, H9_k, H10_k below are
stated here before use and frozen only by draft Amendment 1 to the
carrier charter, which needs the user's approval; until then no verdict
is recorded.

Pre-step record. Known: G1–G3 of the charter and the general-rate Stage 2
derivation (`reports/2026-11-12--general-ir-rate-stage2-leading-term.md`,
"the general derivation" below). Question: in R1, does a dominant
momentum `eta_k != 0` with character trivial on the planes carry the
leading term at the CJWW rate? Stop: outcome (a) if the leading term must
vanish for every protocol.

## 1. Setting

Class and hypotheses of the general derivation, except that zero momentum
is not dominant. `eta_k` is a dominant point (H2) whose character is
trivial on `Lambda_0 = Z^d cap u^perp`. Since `x -> u.x` identifies
`Z^d/Lambda_0` with `Z`, `e^(i eta_k.x) = omega^(u.x)` for lattice `x`,
with `omega = e^(i phi)`, `phi in (-pi, pi]`. Near `eta_k`, by H2 and H8,

    e^(-N Phi_*) lambda_k(eta_k + eta)^N = e^(N(i phi_k + i v_*.eta - eta^T C_k eta/2 + rho_3)),

`C_k` accretive, `phi_k = arg lambda_k(eta_k - i xi_*)`.

## 2. The phases (the only genuinely new step)

**Alice.** For `x` on the plane at depth index `j`,
`u.x = floor(u.x_*) - j = u.x_* - theta^A - j`, so

    e^(i eta_k.(x - x_*)) = alpha_A e^(-i phi (theta^A + j)),
    alpha_A = e^(i phi u.x_*) e^(-i eta_k.x_*).

**Bob.** `u.y = ceil(u.y_*) + j' = u.y_* + theta^B + j'`, so

    e^(-i eta_k.(y - y_*)) = alpha_B e^(-i phi (theta^B + j')),
    alpha_B = e^(-i phi u.y_*) e^(i eta_k.y_*).

**Product of all global factors.** With `y_* - x_* = N v_*`:

    alpha_A alpha_B e^(-i N eta_k.v_*) e^(i N phi_k) e^(i N omega_0)
      = e^(i N psi_k),     psi_k = phi_k + omega_0 - phi u.v_*.

The terms `e^(+-i eta_k.(y_* - x_*))` cancel exactly; what is left is
linear in `N` and independent of the offsets.

Check against the manuscript's point `pi u` (`phi = pi`, `phi_k = pi`,
`omega_0 = 0`, `u.v_* = 3 - sqrt3/2`): `e^(i N psi_k) = e^(i pi sqrt3 N/2)`;
together with the factors `e^(-i pi theta_N)` from each side (absorbed
below into the depth sums) this is manuscript Thm 7.5's cancellation
`e^(-2 pi i theta_N) e^(i pi sqrt3 N/2) = 1`.

## 3. Depth sums with complex decay

The depth factor `e^(-i phi (theta + j))` combines with the tilt weight
`e^(-kappa (theta + j))`. Each side's depth sum is the general one with
`kappa` replaced by `sigma = kappa + i phi`:

    S_sigma(tau; theta) = sum_{j>=0} e^(-sigma (theta + j)) Psi_{(theta+j)/|u|}(tau)
                        = sum_n g^(2 pi n; sigma) e^(2 pi i n theta),
    g^(omega; sigma) = 2 pi^(m/2) |u| (|u|(sigma + i omega))^(-3 - m/2) e^(-|tau|^2 / (4 |u| (sigma + i omega))).

The Laplace transform of the general derivation holds for complex
`p = |u|(sigma + i omega)` with `Re p = |u| kappa > 0`; `S_sigma` is
continuous and 1-periodic in `theta`. The layer estimates of the general
derivation, Sec. 3, are absolute and do not see the unimodular phases.

## 4. Leading term at `eta_k`

As in the general derivation, Sec. 5, with the phases of Sec. 2:

    Z_1^(k) = e^(-K_* N) N^(-5 - d/2) e^(i N psi_k) [ c_k Gamma_k(theta^A_N, theta^B_N) + O(N^(-1/2)) ],
    c_k = phi_partial k_A k_B (2 pi)^(-d) sqrt(2 pi / (C_k)_nn) (R~^dagger M_B e_k)(f_k^dagger M chi),
    Gamma_k = int e^(-zeta^T S_{C_k} zeta / 2) S^A_sigma(sqrt(2 rho_A) zeta; theta^A) S^B_sigma(sqrt(2 rho_B) zeta; theta^B) d^m zeta.

Same power as at zero momentum: `5 + d/2`. The carrier is `eta_k`; the
resource's band near zero momentum enters only through its boundary
values `phi_partial` and `R~`, exactly as at zero momentum.

## 5. Average of the depth factor: where positivity is lost

- Under H9(i) (independent offsets) the average is
  `int W g^A(0; sigma) g^B(0; sigma)`: the product of two non-zero complex
  numbers `(|u| sigma)^(-3-m/2)` and an accretive Gaussian integral
  (`Re(1/sigma) = kappa/|sigma|^2 > 0`). **Non-zero**, though not
  necessarily of positive real part.
- Under H9(ii) (`theta^A = theta^B`, irrational) the average is

      mu_k = sum_n int W g^A(2 pi n; sigma) g^B(-2 pi n; sigma) d^m zeta.

  For real `sigma` the pairs were complex conjugates and every term had
  positive real part; for `phi != 0`, `g(-2 pi n; sigma)` is not the
  conjugate of `g(2 pi n; sigma)` and the terms can cancel. **`mu_k != 0`
  is not implied by anything in force.** It is a finite computation per
  walk; if `mu_k = 0` for every trivial-character dominant point, the
  first-order leading term has zero average and the argument fails
  (candidate for outcome (a)).

## 6. Conclusion, conditional on draft Amendment 1

With H6_k (the left eigenvector `f_k` outside the span of those at the
other trivial-character dominant points), H9_k (H9(i), or H9(ii) with
`mu_k != 0`) and H10_k (`e_k` not a complex multiple of `R~`, so that
`M_B` rotates `c_k`), the argument of the general derivation, Sec. 7,
goes through unchanged: `|Gamma_k| >= |mu_k|/2` on a set of `N` of
positive density, two protocols with `c_k` and `i c_k` see the real and
imaginary parts, bilinearity passes to a basis pair, and

    lim sup (1/N) log delta(N) = -K_*,

carried by `eta_k` at power `5 + d/2`. Outcome (b) of the charter is
**partly** triggered: Secs. 2–4 are a direct adaptation; the loss of
positivity in Sec. 5 is new and needs a hypothesis.

## 7. Limits

Author derivation; nothing reviewed. Limsup form only. H3 is still needed
(R1 is defined through lattice planes). Regime R2 (internal name withheld) is
Stage B and not addressed.

## 8. Addendum after the R1 diagnostic: dependent carriers

The diagnostic (`scripts/diagnose_ir_carrier_r1.py`, run 2; run 1 crashed
on a basis error of the tail helper and is kept) finds, in CJWW (5.12),
Pavia A+ and the cyclic s=4 walk, two trivial-character dominant momenta
each, with `mu != 0` at every one (`|mu| = 2.28` and `0.013` for the two
cube walks, `9.46` for both points of the tetrahedral walk), `e_k` not
parallel to `R~`, but **left and right eigenvectors dependent between the
two points** (they are related by a symmetry of the walk). Isolation
(H6_k(i)) is impossible there.

The argument still closes with a second moment. For a protocol whose
coefficient at the group `G` is `c` (times fixed ratios `a_j`), the
bracket is `h(N) = sum_{j in G} a_j e^(i N psi_j) Gamma_j(theta_N)`. Then

    avg_N |h(N)|^2 = sum_j |a_j|^2 avg |Gamma_j|^2
                   + sum_{i != j} a_i a_j-bar avg[ e^(i N (psi_i - psi_j)) Gamma_i Gamma_j-bar (theta_N) ].

Under H6_k(ii), `(N u.w_A, N (psi_i - psi_j)/(2 pi))` is equidistributed on
`T^2` for each pair (Weyl), and `Gamma_i Gamma_j-bar` is continuous on the
circle, so each cross average tends to `0`; the diagonal averages are at
least `|mu_j|^2 > 0`. Hence `|h(N)|` is bounded below on a set of `N` of
positive density, and rotation (H10_k) and bilinearity finish as in Sec. 6.
In the three walks `psi` differs between the two carriers (`4.4626` vs
`5.8428`; `0.5554` vs `1.0154`), but rational independence is not
checkable in floating point.

Also from run 2: the round-2 tail of the JDW hexagonal walk, computed with
the basis error, is recomputed correctly; H5 and the tail part of H10
still hold (`|R~| = 0.700`, `cos(e_0, R~) = 0.893`), so the round-2 row
stands.

## 9. Verdict (revised after the Grok review)

The first version of this section recorded `PROVED_UNDER_FROZEN_CONTRACT`
for the whole amended block. The Grok review (O1) shows that the case
H6_k(ii) together with H9(i) is not covered by Sec. 8. Revised verdict:

- **`PROVED_UNDER_FROZEN_CONTRACT`** (carrier charter as amended), with
  the repairs of Sec. 10: H6_k(i) with H9(i) or H9(ii); H6_k(ii) with
  H9(ii). Author derivation, PRELIMINARY; repairs not re-reviewed.
- **`OPEN`**: H6_k(ii) with H9(i) (a phase difference commensurate with
  the second offset can make the cross term survive).

No verified R1 example is known. The three diagnostic walks are outside
`Z^d` (diagnostic lattice test; CJWW (5.12) generates the BCC group per
`5213d94`; the s=4 walk lives on the equal-parity lattice of index four),
and even there H6_k(i) fails while H6_k(ii) needs a rational independence
that floating point cannot decide.

## 10. Repairs after the Grok review

**Common rotation of a carrier group (O2).** For Hermitian `M_B`,
`u = M_B R~` ranges over `{u : <R~, u> real}`, and
`R~^dagger M_B e_j = u^dagger e_j`. By H10_k there is `u_0` with
`<R~, u_0> = 0` and `u_0^dagger e_k != 0`; both `u_0` and `-i u_0` are
admissible and multiply the whole vector `(u_0^dagger e_j f_j^dagger v)_j`
by `1` and `i`. The two protocols see `Im` and `Re` of the same bracket.

**From the mean of `|h|^2` to positive density (O3).** Let
`omega = (u.w_A, ((psi_i - psi_j)/(2 pi))_{i<j})` and `X` the closure of
`{N omega}` in the torus; the orbit equidistributes for the Haar measure
of `X`. Pairwise independence makes each two-dimensional projection of
that measure Haar, so each cross term integrates to `0` on `X`, and
`int_X |h|^2 = sum_j |a_j|^2 int |Gamma_j|^2 > 0`. `|h|` is continuous on
`X`, so `{|h| > c}` is a relatively open set of positive measure for small
`c > 0`, hence visited with positive density. The `O(N^(-1/2))` error
inside the bracket does not affect this.

**Rotation before the first-moment bound (O5).** With
`alpha = arg mu_k`, the mean of `Re(e^(-i alpha) Gamma_k)` is `|mu_k|`;
the argument of the general derivation, Sec. 6, then gives
`|Gamma_k| >= |mu_k|/2` on a set of positive density.

**Notes (O6, obligation 3).** `mu_k != 0` is sufficient, not necessary;
for the second moment `int |Gamma_j|^2 > 0` suffices. "Cannot be
separated" in H6_k(ii) is read as: `f_k` is outside the span of the `f_j`
with `j` outside `G`, and each point outside `G` is separable on the left.
