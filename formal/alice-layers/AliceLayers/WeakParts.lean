import AliceLayers.SectionSecond
import Mathlib.MeasureTheory.Integral.DivergenceTheorem
import Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts

noncomputable section
open Filter MeasureTheory Set
open scoped Topology Interval FourierTransform
namespace AliceLayers

/-- Integration by parts when the first factor has a countable exceptional set. -/
theorem integral_mul_deriv_off_countable
    (u v u' v' : ℝ → ℂ) (a b : ℝ) (s : Set ℝ)
    (hs : s.Countable)
    (hu : ContinuousOn u [[a,b]]) (hv : ContinuousOn v [[a,b]])
    (hdu : ∀ x ∈ Ioo (min a b) (max a b) \ s, HasDerivAt u (u' x) x)
    (hdv : ∀ x ∈ Ioo (min a b) (max a b), HasDerivAt v (v' x) x)
    (hiu : IntervalIntegrable u' volume a b) (hiv : IntervalIntegrable v' volume a b) :
    (∫ x in a..b, u x * v' x) = u b * v b - u a * v a - ∫ x in a..b, u' x * v x := by
  have he := integral_eq_of_hasDerivAt_off_countable (fun x => u x * v x)
    (fun x => u' x * v x + u x * v' x) hs (hu.mul hv)
    (fun x hx => (hdu x hx).mul (hdv x hx.1))
    ((hiu.mul_continuousOn hv).add (hiv.continuousOn_mul hu))
  rw [intervalIntegral.integral_add (hiu.mul_continuousOn hv) (hiv.continuousOn_mul hu)] at he
  apply eq_sub_iff_add_eq.mpr
  simpa [add_comm] using he

/-- The second derivative of the real section satisfies integration by parts
against every continuously differentiable complex test factor. -/
theorem cutoff_deriv_integration_by_parts (δ x a b : ℝ) (v v' : ℝ → ℂ)
    (hv : ContinuousOn v [[a,b]])
    (hdv : ∀ y ∈ Ioo (min a b) (max a b), HasDerivAt v (v' y) y)
    (hiv : IntervalIntegrable v' volume a b) :
    (∫ y in a..b, ((-4*y * max (δ-y^2-x^2) 0 : ℝ) : ℂ) * v' y) =
      ((-4*b * max (δ-b^2-x^2) 0 : ℝ) : ℂ) * v b -
      ((-4*a * max (δ-a^2-x^2) 0 : ℝ) : ℂ) * v a -
      ∫ y in a..b, (cutoffSecond δ x y : ℂ) * v y := by
  apply integral_mul_deriv_off_countable _ _ _ _ a b {y | δ-y^2-x^2 = 0}
  · exact (section_boundary_finite δ x).countable
  · exact Complex.continuous_ofReal.comp (section_cutoff_derivative_continuous δ x) |>.continuousOn
  · exact hv
  · intro y hy
    exact (section_second_away δ x y (by simpa using hy.2)).ofReal_comp
  · exact hdv
  · exact (Complex.ofRealCLM.integrable_comp (cutoffSecond_integrable δ x)).intervalIntegrable
  · exact hiv

/-- The relevant exponential has derivative iω times itself. -/
theorem oscillation_hasDerivAt (ω y : ℝ) :
    HasDerivAt (fun t : ℝ => Complex.exp (Complex.I * ((ω*t : ℝ) : ℂ)))
      (Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) * (Complex.I * (ω : ℂ))) y := by
  have hp : HasDerivAt (fun t : ℝ => ω*t) ω y := by
    simpa using! (hasDerivAt_id y).const_mul ω
  have hc := hp.ofReal_comp
  have h := (hc.const_mul Complex.I).cexp
  simpa using! h

/-- The section's phase and a Fourier phase combine by adding frequencies. -/
theorem psiSlice_mul_oscillation (δ : ℝ) (τ : Tangent) (x y ω : ℝ) :
    psiSlice δ τ x y * Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) =
      ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
        Complex.exp (Complex.I * ((τ 1*x : ℝ) : ℂ)) *
        Complex.exp (Complex.I * (((τ 0+ω)*y : ℝ) : ℂ)) := by
  simp only [psiSlice, psiIntegrand, positiveSquare, Fin.sum_univ_two,
    ContinuousMap.coe_mk, Fin.isValue]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
  have h : δ - (y^2+x^2) = δ-y^2-x^2 := by ring
  rw [h]
  simp only [mul_assoc, ← Complex.exp_add]
  congr 2
  push_cast
  ring

/-- The Fourier transform of the full section is the Fourier integral of the
real cutoff at the shifted angular frequency, times its constant phase. -/
theorem psiSlice_fourier_shift (δ : ℝ) (τ : Tangent) (x u : ℝ) :
    𝓕 (psiSlice δ τ x : ℝ → ℂ) u =
      Complex.exp (Complex.I * ((τ 1*x : ℝ) : ℂ)) *
        ∫ y : ℝ, ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
          Complex.exp (Complex.I * (((τ 0-2*Real.pi*u)*y : ℝ) : ℂ)) := by
  rw [Real.fourier_real_eq_integral_exp_smul, ← integral_const_mul]
  apply integral_congr_ae
  filter_upwards with y
  have h := psiSlice_mul_oscillation δ τ x y (-2*Real.pi*u)
  simp only [smul_eq_mul]
  have hphase : ((↑(-2 * Real.pi * y * u) : ℂ) * Complex.I) =
      Complex.I * ((-2 * Real.pi * u * y : ℝ) : ℂ) := by push_cast; ring
  simpa [hphase, sub_eq_add_neg, mul_comm, mul_left_comm, mul_assoc] using h

/-- Second integration by parts for the real cutoff against a Fourier phase. -/
theorem cutoff_oscillation_parts (δ x ω : ℝ) (hδ : 0 ≤ δ) :
    (∫ y in (-(δ+1))..(δ+1),
      ((-4*y * max (δ-y^2-x^2) 0 : ℝ) : ℂ) *
        (Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) * (Complex.I * (ω : ℂ)))) =
      - ∫ y in (-(δ+1))..(δ+1), (cutoffSecond δ x y : ℂ) *
        Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) := by
  let v : ℝ → ℂ := fun y => Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ))
  let v' : ℝ → ℂ := fun y => v y * (Complex.I * (ω : ℂ))
  have hc : Continuous v := by dsimp [v]; fun_prop
  have hc' : Continuous v' := hc.mul continuous_const
  have hi : IntervalIntegrable v' volume (-(δ+1)) (δ+1) := hc'.intervalIntegrable _ _
  have h := cutoff_deriv_integration_by_parts δ x (-(δ+1)) (δ+1) v v'
    hc.continuousOn (fun y _ => oscillation_hasDerivAt ω y) hi
  have hpos : δ - (δ+1)^2 - x^2 ≤ 0 := by nlinarith [sq_nonneg δ, sq_nonneg x]
  have hneg : δ - (-(δ+1))^2 - x^2 ≤ 0 := by nlinarith [sq_nonneg δ, sq_nonneg x]
  have hp : max (δ-(δ+1)^2-x^2) 0 = 0 := max_eq_right hpos
  have hn : max (δ-(-(δ+1))^2-x^2) 0 = 0 := max_eq_right hneg
  simp only [hp, hn, mul_zero, Complex.ofReal_zero, zero_mul, sub_self, zero_sub] at h
  exact h

/-- First integration by parts for the cutoff and the shifted phase. -/
theorem cutoff_first_oscillation_parts (δ x ω : ℝ) (hδ : 0 ≤ δ) :
    (∫ y in (-(δ+1))..(δ+1),
      ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
        (Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) * (Complex.I * (ω : ℂ)))) =
      - ∫ y in (-(δ+1))..(δ+1),
        ((-4*y * max (δ-y^2-x^2) 0 : ℝ) : ℂ) *
          Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) := by
  let a := -(δ+1)
  let b := δ+1
  let f : ℝ → ℂ := fun y => ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ)
  let f' : ℝ → ℂ := fun y => ((-4*y * max (δ-y^2-x^2) 0 : ℝ) : ℂ)
  let v : ℝ → ℂ := fun y => Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ))
  let v' : ℝ → ℂ := fun y => v y * (Complex.I * (ω : ℂ))
  have hf : Continuous f := by
    exact Complex.continuous_ofReal.comp (section_cutoff_contDiff_one δ x).continuous
  have hf' : Continuous f' := Complex.continuous_ofReal.comp (section_cutoff_derivative_continuous δ x)
  have hv : Continuous v := by dsimp [v]; fun_prop
  have hv' : Continuous v' := hv.mul continuous_const
  have h := integral_mul_deriv_off_countable f v f' v' a b ∅ Set.countable_empty
    hf.continuousOn hv.continuousOn
    (fun y _ => (section_cutoff_derivative δ x y).ofReal_comp)
    (fun y _ => oscillation_hasDerivAt ω y)
    (hf'.intervalIntegrable _ _) (hv'.intervalIntegrable _ _)
  have hpos : δ - (δ+1)^2 - x^2 ≤ 0 := by nlinarith [sq_nonneg δ, sq_nonneg x]
  have hneg : δ - (-(δ+1))^2 - x^2 ≤ 0 := by nlinarith [sq_nonneg δ, sq_nonneg x]
  have hp : max (δ-(δ+1)^2-x^2) 0 = 0 := max_eq_right hpos
  have hn : max (δ-(-(δ+1))^2-x^2) 0 = 0 := max_eq_right hneg
  dsimp [a, b, f, f', v, v', positiveSquare] at h
  simp only [hp, hn] at h
  simp only [show (0 : ℝ)^2 = 0 by norm_num, Complex.ofReal_zero,
    zero_mul, sub_self, zero_sub] at h
  simpa only [positiveSquare] using h

/-- Two integrations by parts, with no division by the frequency. -/
theorem cutoff_double_oscillation_parts (δ x ω : ℝ) (hδ : 0 ≤ δ) :
    (∫ y in (-(δ+1))..(δ+1),
      ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
        Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ))) * (Complex.I * (ω : ℂ))^2 =
      ∫ y in (-(δ+1))..(δ+1), (cutoffSecond δ x y : ℂ) *
        Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) := by
  have h1 := cutoff_first_oscillation_parts δ x ω hδ
  have h2 := cutoff_oscillation_parts δ x ω hδ
  simp only [← mul_assoc, intervalIntegral.integral_mul_const] at h1 h2
  simp only [mul_assoc] at h1 h2
  simp only [pow_two] at h1 h2 ⊢
  rw [← mul_assoc, h1, neg_mul, h2, neg_neg]

/-- Compact support lets the full Fourier integral use the same finite interval. -/
theorem cutoff_integral_whole_eq_interval (δ x ω : ℝ) (hδ : 0 ≤ δ) :
    (∫ y : ℝ, ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
      Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ))) =
    ∫ y in (-(δ+1))..(δ+1), ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ) *
      Complex.exp (Complex.I * ((ω*y : ℝ) : ℂ)) := by
  symm
  apply intervalIntegral.integral_eq_integral_of_support_subset
  apply Function.support_subset_iff'.mpr
  intro y hy
  have hout : y ≤ -(δ+1) ∨ δ+1 < y := by
    simpa only [Set.mem_Ioc, not_and_or, not_lt, not_le] using hy
  have hs : δ ≤ y^2 := by
    rcases hout with h | h <;> nlinarith [sq_nonneg (δ+1)]
  have hz : δ-y^2-x^2 ≤ 0 := by nlinarith [sq_nonneg x]
  simp [positiveSquare, max_eq_right hz]

/-- Full section Fourier transform after two integrations by parts. -/
theorem psiSlice_fourier_double_parts (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ) :
    𝓕 (psiSlice δ τ x : ℝ → ℂ) u *
      (Complex.I * ((τ 0-2*Real.pi*u : ℝ) : ℂ))^2 =
    Complex.exp (Complex.I * ((τ 1*x : ℝ) : ℂ)) *
      ∫ y in (-(δ+1))..(δ+1), (cutoffSecond δ x y : ℂ) *
        Complex.exp (Complex.I * (((τ 0-2*Real.pi*u)*y : ℝ) : ℂ)) := by
  rw [psiSlice_fourier_shift, cutoff_integral_whole_eq_interval δ x _ hδ,
    mul_assoc, cutoff_double_oscillation_parts δ x _ hδ]

/-- A second-order weighted bound, including the zero shifted frequency. -/
theorem psiSlice_second_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ) :
    ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ * |τ 0-2*Real.pi*u|^2 ≤
      ∫ y in (-(δ+1))..(δ+1), |cutoffSecond δ x y| := by
  have hab : -(δ+1) ≤ δ+1 := by linarith
  have h := congrArg norm (psiSlice_fourier_double_parts δ hδ τ x u)
  simp only [norm_mul, norm_pow, Complex.norm_I, one_mul, Complex.norm_real,
    Real.norm_eq_abs] at h
  have hc : ‖Complex.exp (Complex.I * ((τ 1*x : ℝ) : ℂ))‖ = 1 := by
    simp [Complex.norm_exp, Complex.mul_re]
  rw [hc, one_mul] at h
  rw [h]
  calc
    _ ≤ ∫ y in (-(δ+1))..(δ+1), ‖(cutoffSecond δ x y : ℂ) *
        Complex.exp (Complex.I * (((τ 0-2*Real.pi*u)*y : ℝ) : ℂ))‖ :=
      intervalIntegral.norm_integral_le_integral_norm hab
    _ = _ := by
      apply intervalIntegral.integral_congr
      intro y hy
      simp [norm_mul, Complex.norm_exp, Complex.mul_re, Real.norm_eq_abs]

/-- Decay away from the resonant frequency, with the exact L¹ constant. -/
theorem psiSlice_second_order_decay (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ)
    (hω : τ 0-2*Real.pi*u ≠ 0) :
    ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ ≤
      (∫ y in (-(δ+1))..(δ+1), |cutoffSecond δ x y|) /
        |τ 0-2*Real.pi*u|^2 := by
  apply (le_div_iff₀ (sq_pos_of_ne_zero (abs_ne_zero.mpr hω))).2
  exact psiSlice_second_order_bound δ hδ τ x u

set_option maxHeartbeats 800000 in
/-- The first spectral sum converges for every integer section. -/
theorem psiSlice_spectral_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x : ℝ) :
    Summable fun m : ℤ => 𝓕 (psiSlice δ τ x : ℝ → ℂ) (m : ℝ) := by
  let c : ℝ := 2 * Real.pi
  have hc : 0 < c := by dsimp [c]; positivity
  have hcn : c ≠ 0 := ne_of_gt hc
  let a : ℝ := -τ 0 / c
  let K : ℝ := ∫ y in (-(δ+1))..(δ+1), |cutoffSecond δ x y|
  have hs : Summable (fun m : ℤ => 1 / |(m : ℝ) + a| ^ (2 : ℝ)) :=
    (Real.summable_one_div_int_add_rpow a 2).2 (by norm_num)
  have hg : Summable (fun m : ℤ => (K / c^2) * (1 / |(m : ℝ) + a|^2)) := by
    simpa only [Real.rpow_ofNat] using hs.mul_left (K / c^2)
  have hinj : Function.Injective (fun m : ℤ => (m : ℝ) + a) := by
    intro i j hij
    exact Int.cast_injective (add_right_cancel hij)
  have hfinite : {m : ℤ | (m : ℝ) + a = 0}.Finite := by
    exact Set.Finite.preimage (hinj.injOn) (Set.finite_singleton 0)
  apply hg.of_norm_bounded_eventually
  filter_upwards [hfinite.compl_mem_cofinite] with m hm
  have hm' : (m : ℝ) + a ≠ 0 := by simpa using hm
  have hw : τ 0 - 2*Real.pi*(m : ℝ) = -c * ((m : ℝ) + a) := by
    dsimp [a, c] at *
    field_simp
    <;> ring
  have hn : τ 0 - 2*Real.pi*(m : ℝ) ≠ 0 := by
    rw [hw]
    exact mul_ne_zero (neg_ne_zero.mpr hcn) hm'
  have hb := psiSlice_second_order_decay δ hδ τ x (m : ℝ) hn
  rw [hw, abs_mul, abs_neg, abs_of_pos hc, mul_pow] at hb
  convert hb using 1 <;> dsimp [K] <;> ring

/-- Poisson on ℤ² with only the second spectral summability condition remaining. -/
theorem psi_poisson_one_summability (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (hsecond : ∀ m : ℤ, Summable fun n : ℤ =>
      𝓕 (psiPartial δ τ (m : ℝ)) (n : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, psi δ (shiftedTau τ (m : ℝ) (n : ℝ)) := by
  apply psi_poisson_two_summability δ hδ τ
  · intro n
    exact psiSlice_spectral_summable δ hδ τ n
  · exact hsecond

/-- Swapping tangent coordinates leaves the two-dimensional integral unchanged. -/
theorem psi_swap_coordinates (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    psi δ ![τ 1, τ 0] = psi δ τ := by
  rw [← psi_integral_sections δ hδ ![τ 1, τ 0], ← psi_integral_sections δ hδ τ]
  have hi := psi_prod_integrable δ hδ τ
  have hf : Integrable (Function.uncurry (fun x y : ℝ => psiIntegrand δ τ ![x,y]))
      ((volume : Measure ℝ).prod volume) := hi
  have hswap := integral_integral_swap hf
  rw [← hswap]
  apply integral_congr_ae
  filter_upwards with x
  apply integral_congr_ae
  filter_upwards with y
  simp only [psiIntegrand, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
  congr 2 <;> push_cast <;> ring

/-- Uniform in both section coordinates, including degenerate sections. -/
theorem cutoffSecond_uniform_bound (δ x y : ℝ) (hδ : 0 ≤ δ) :
    |cutoffSecond δ x y| ≤ 8 * δ := by
  unfold cutoffSecond
  split_ifs with h
  · apply abs_le.mpr
    constructor <;> nlinarith [sq_nonneg x, sq_nonneg y]
  · simpa using (mul_nonneg (by norm_num : (0 : ℝ) ≤ 8) hδ)

/-- An L¹ constant independent of the section and of the phase. -/
theorem cutoffSecond_integral_uniform_bound (δ x : ℝ) (hδ : 0 ≤ δ) :
    (∫ y in (-(δ+1))..(δ+1), |cutoffSecond δ x y|) ≤ 16 * δ * (δ+1) := by
  have hab : -(δ+1) ≤ δ+1 := by linarith
  calc
    _ ≤ ∫ _y in (-(δ+1))..(δ+1), 8 * δ := by
      apply intervalIntegral.integral_mono_on hab
      · exact (cutoffSecond_integrable δ x).abs.intervalIntegrable
      · exact intervalIntegrable_const
      · intro y _
        exact cutoffSecond_uniform_bound δ x y hδ
    _ = _ := by simp; ring

/-- The second-order section estimate now has a constant uniform in x and τ. -/
theorem psiSlice_second_order_uniform_bound (δ : ℝ) (hδ : 0 ≤ δ)
    (τ : Tangent) (x u : ℝ) :
    ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ * |τ 0-2*Real.pi*u|^2 ≤
      16 * δ * (δ+1) :=
  (psiSlice_second_order_bound δ hδ τ x u).trans
    (cutoffSecond_integral_uniform_bound δ x hδ)

/-- The partial transform vanishes also at the left endpoint of the support box. -/
theorem psiPartial_integral_interval (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u : ℝ) :
    (∫ x : ℝ, psiPartial δ τ u x) =
      ∫ x in (-(δ+1))..(δ+1), psiPartial δ τ u x := by
  symm
  apply intervalIntegral.integral_eq_integral_of_support_subset
  apply Function.support_subset_iff'.mpr
  intro x hx
  have hout : x ≤ -(δ+1) ∨ δ+1 < x := by
    simpa only [Set.mem_Ioc, not_and_or, not_lt, not_le] using hx
  have hs : δ ≤ x^2 := by
    rcases hout with h | h <;> nlinarith [sq_nonneg (δ+1)]
  rw [psiPartial_integral]
  apply integral_eq_zero_of_ae
  filter_upwards with y
  have hv : psiIntegrand δ τ ![y,x] = 0 := by
    apply psi_integrand_vanishes_of_sqNorm_ge
    rw [tangent_sq_sum]
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
    nlinarith [sq_nonneg y]
  simp [partialIntegrand, hv]

/-- Integrating the uniform section bound gives a two-dimensional weighted bound.
Fubini is supplied by psi_double_fourier_zero, with verified product integrability. -/
theorem psi_second_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖ * |τ 0|^2 ≤ 32 * δ * (δ+1)^2 := by
  have hab : -(δ+1) ≤ δ+1 := by linarith
  have hc := psiPartial_continuous δ hδ τ 0
  have he : psi δ τ = ∫ x in (-(δ+1))..(δ+1), psiPartial δ τ 0 x := by
    rw [← psi_double_fourier_zero δ hδ τ, fourier_zero_eq_integral]
    exact psiPartial_integral_interval δ hδ τ 0
  rw [he]
  calc
    _ ≤ (∫ x in (-(δ+1))..(δ+1), ‖psiPartial δ τ 0 x‖) * |τ 0|^2 :=
      mul_le_mul_of_nonneg_right (intervalIntegral.norm_integral_le_integral_norm hab)
        (sq_nonneg _)
    _ = ∫ x in (-(δ+1))..(δ+1), ‖psiPartial δ τ 0 x‖ * |τ 0|^2 :=
      (intervalIntegral.integral_mul_const _ _).symm
    _ ≤ ∫ _x in (-(δ+1))..(δ+1), 16 * δ * (δ+1) := by
      apply intervalIntegral.integral_mono_on hab
      · exact (hc.norm.mul continuous_const).intervalIntegrable _ _
      · exact intervalIntegrable_const
      · intro x _
        simpa [psiPartial] using psiSlice_second_order_uniform_bound δ hδ τ x 0
    _ = _ := by simp; ring

/-- The same bound in the other coordinate, using the proved Fubini symmetry. -/
theorem psi_second_coordinate_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖ * |τ 1|^2 ≤ 32 * δ * (δ+1)^2 := by
  have h := psi_second_order_bound δ hδ ![τ 1, τ 0]
  rw [psi_swap_coordinates δ hδ τ] at h
  exact h

set_option maxHeartbeats 800000 in
/-- The second spectral sum converges for every real first frequency. -/
theorem psiPartial_spectral_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u : ℝ) :
    Summable fun n : ℤ => 𝓕 (psiPartial δ τ u) (n : ℝ) := by
  let c : ℝ := 2 * Real.pi
  have hc : 0 < c := by dsimp [c]; positivity
  have hcn : c ≠ 0 := ne_of_gt hc
  let a : ℝ := -τ 1 / c
  let K : ℝ := 32 * δ * (δ+1)^2
  have hs : Summable (fun n : ℤ => 1 / |(n : ℝ) + a| ^ (2 : ℝ)) :=
    (Real.summable_one_div_int_add_rpow a 2).2 (by norm_num)
  have hg : Summable (fun n : ℤ => (K / c^2) * (1 / |(n : ℝ) + a|^2)) := by
    simpa only [Real.rpow_ofNat] using hs.mul_left (K / c^2)
  have hinj : Function.Injective (fun n : ℤ => (n : ℝ) + a) := by
    intro i j hij
    exact Int.cast_injective (add_right_cancel hij)
  have hfinite : {n : ℤ | (n : ℝ) + a = 0}.Finite :=
    Set.Finite.preimage hinj.injOn (Set.finite_singleton 0)
  apply hg.of_norm_bounded_eventually
  filter_upwards [hfinite.compl_mem_cofinite] with n hn
  have hn' : (n : ℝ) + a ≠ 0 := by simpa using hn
  have hw : τ 1 - 2*Real.pi*(n : ℝ) = -c * ((n : ℝ) + a) := by
    dsimp [a, c] at *
    field_simp
    <;> ring
  have hω : τ 1 - 2*Real.pi*(n : ℝ) ≠ 0 := by
    rw [hw]
    exact mul_ne_zero (neg_ne_zero.mpr hcn) hn'
  have hb := psi_second_coordinate_bound δ hδ (shiftedTau τ u (n : ℝ))
  simp only [shiftedTau, Matrix.cons_val_one] at hb
  have hd : ‖psi δ (shiftedTau τ u (n : ℝ))‖ ≤ K / |τ 1-2*Real.pi*(n : ℝ)|^2 :=
    (le_div_iff₀ (sq_pos_of_ne_zero (abs_ne_zero.mpr hω))).2 hb
  rw [psiPartial_fourier δ hδ τ u]
  rw [hw, abs_mul, abs_neg, abs_of_pos hc, mul_pow] at hd
  convert hd using 1 <;> dsimp [K] <;> ring

/-- Poisson on the standard integer lattice with no extra spectral hypotheses. -/
theorem psi_poisson (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, psi δ (shiftedTau τ (m : ℝ) (n : ℝ)) :=
  psi_poisson_one_summability δ hδ τ
    (fun m => psiPartial_spectral_summable δ hδ τ (m : ℝ))

/-- Independent limiting-case check: the zero-depth profile is identically zero. -/
theorem psi_zero_depth (τ : Tangent) : psi 0 τ = 0 := by
  unfold psi
  apply integral_eq_zero_of_ae
  filter_upwards with σ
  apply psi_integrand_vanishes_of_sqNorm_ge
  exact Finset.sum_nonneg (fun i _ => sq_nonneg (σ i))

end AliceLayers
