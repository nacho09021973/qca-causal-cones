# General infrared operational rate: Stage 2 progress

2026-11-12. Claude (claude-opus-5-5). Charter `GENERAL_IR_RATE_GATE.md`
(`aa6c5f6`), Amendment 1 (`91be396`), Amendment 2 (`34f0601`). Author
derivation, **PRELIMINARY, not reviewed**; no computation.

Pre-step record. Known: Stage 1 bound, the reduction of non-vanishing
(`reports/2026-11-12--general-ir-rate-stages-0-1.md`). Question: which
parts of the leading-term analysis hold in the amended class with no
further hypothesis, and what remains? Stop: any step that needs a
hypothesis not in force is recorded, not assumed.

## 1. Exact decomposition

With `a = (U_M - I) phi_N`, `r = P_B S^N phi_N`, and `E` supported in `B_N`,

    L_N = 2 Re <r, E P_B S^N a> + <P_B S^N a, E P_B S^N a>.

For Hermitian `M` and `theta = (pi/2) F_N`, `e^(i theta M) - I = i theta M +
R(theta)` with `||R(theta)|| <= theta^2 ||M||^2 / 2`. So
`L_N = -2 Im Z_1 + 2 Re Z_2 + Q_N`, with `Z_j = <r, E P_B S^N f_j>`,
`f_1 = theta phi_N M chi`, `f_2 = R(theta) phi_N chi`.

## 2. Bounds that hold in the amended class

- **Quadratic term.** `|Q_N| <= ||P_B S^N a||^2 <= (2 T_N)^2 <= C N^(2(d+s-1)) e^(-2 K_* N)`
  (Stage 1).
- **Layer sizes.** On the plane at depth `delta` the boundary profile is
  `F_N = O(N^(-2) eps^2)`, `eps <= delta`, the disc has `O((N delta)^((d-1)/2) + 1)`
  sites, and the plane weight is `e^(-t (theta + j))`. Hence, uniformly in
  `eta`, `|A_{f_1}(eta)| <= C N^(-d/2 - 2 + (d-1)/2) = C N^(-5/2)`,
  `|A_{f_2}(eta)| <= C N^(-9/2)`, and `||B_w(eta)|| <= C N^(-5/2)` using the
  pointwise tail `|r| <= C N^(-d/2)`. The exponent `-5/2` does not depend on
  `d`. (For `d = 3` these are manuscript Layers (a) and the `a_c` bound.)
- **Second-order encoder term.** With the exact representation
  (manuscript Eq. (13), valid in any `d`) and
  `int ||S~_N(eta)|| deta <= C N^(-d/2)` (Gaussian near the dominant points
  by H2, `C N^(s-1) e^(-cN)` elsewhere), `|Z_2| <= C e^(-K_* N) N^(-7 - d/2)`.
- **Away from the dominant points.** Their complement contributes
  `O(e^(-K_* N) N^(s-6) e^(-cN))`: compactness and H2 give a spectral
  radius `<= e^(Phi_* - c')` there, and Stage 1 Lemma 1.2 the power bound.
- **Dominant points with non-trivial character.** As in manuscript Layers
  (d): the in-plane Poisson sum has no zero frequency, each frequency is at
  distance `>= d_0/2` from the lattice, and the inverse-cube sum converges
  in in-plane dimension `d - 1 <= 2`. Alice's layer is `O(N^(-4))`, a
  relative `O(N^(-3/2))`.
- **Dominant points with trivial character other than zero.** Their
  contribution vanishes for the protocol chosen by H6 (report of Stages
  0–1, Stage 2(B)).

So, for the protocol chosen by H6, `L_N = -2 Im Z_1^(0) + o(e^(-K_* N) N^(-5-d/2))`,
where `Z_1^(0)` is the contribution of the ball around `eta = 0`.
The order `N^(-5-d/2)` (`13/2` for `d = 3`) is the expected size of
`Z_1^(0)` by the count of manuscript Remark 7.6; it is not claimed here.

## 3. Two things the manuscript's proof does not need and the general case does

1. **Complex Gaussian.** Near `eta = 0`,
   `log lambda_0(eta) = Phi_* + i phi_0 + i v_*.eta - (1/2) eta^T (Q + i Q') eta + O(|eta|^3)`,
   with `Q = Hess_xi log|lambda_0|` positive definite (H2, pluriharmonicity
   of `log|lambda_0|` in `p = eta - i xi`) and a real symmetric `Q'`,
   zero in the manuscript because `S(-i xi)` is Hermitian there. The linear
   coefficient is `v_*` by H8. The integrals stay controlled: `Q + i Q'`
   is accretive, its Schur complement on the plane is accretive (the
   inverse of an accretive matrix is accretive and the Schur complement's
   inverse is a compression of it), and the positivity argument behind H9
   goes through with "positive real part" in place of "positive".
2. **A phase that grows with `N`.** `Z_1^(0)` carries
   `e^(i N psi)`, `psi = phi_0 + omega_0`, where `e^(-i omega_0)` is the
   nodal eigenvalue at `p = 0` (it enters through the free tail `r`) and
   `phi_0 = arg lambda_0(-i xi_*)`. Then

       L_N ≈ -2 e^(-K_* N) N^(-p) Im( e^(i N psi) Gamma_0(theta^A_N, theta^B_N) c ),

   with `c` the coefficient fixed by the protocol. In the manuscript
   `psi = 0` (`S(0) = I` and `S(-i xi_*)` Hermitian with positive dominant
   eigenvalue). In general nothing in force fixes `psi`, and the family
   may not be able to rotate `c`: with `s = 2` and two trivial points (as in
   K3) the choice of `M` that removes the second point leaves `M chi` fixed
   up to a real factor, and if `e_0` is parallel to `R~` every Hermitian
   `M_B` gives a real multiple of the same number. Then `Im` of the bracket
   could tend to zero along every `N`, depending on the joint distribution
   of `N psi / 2 pi` and the depth offsets.

## 4. What remains

- **A1 (analysis).** Leading term of `Z_1^(0)`: generalise manuscript
  Layers (b) and the assembly to the amended class, with the complex
  Gaussian of Sec. 3.1 and H9's averaging. No obstruction found; it is a
  long but direct adaptation.
- **A2 (non-vanishing of the imaginary part).** Needs one more condition,
  for example: `psi in pi Z`; or the family can rotate `c` (true when
  `s >= |D| + 1`, or when `e_0` is not parallel to `R~` in a suitable
  sense); or a joint-equidistribution condition on `(N psi / 2 pi, theta_N)`.
  Any of these is a change of hypotheses and needs an amendment before use.

Budget: Stages 1–2 share two sessions; this is the end of the first.
