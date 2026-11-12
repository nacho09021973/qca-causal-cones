import AliceLayers.ZeroModeDepth

noncomputable section
open scoped BigOperators
open MeasureTheory
namespace AliceLayers

/-- Direct integral check: oscillations do not change the pointwise norm. -/
theorem psiIntegrand_norm_eq_profile (δ : ℝ) (τ σ : Tangent) :
    ‖psiIntegrand δ τ σ‖ = (max (δ-∑ i, σ i^2) 0)^2 := by
  have he : ‖Complex.exp (Complex.I * ((∑ i, τ i*σ i : ℝ) : ℂ))‖ = 1 := by
    simp [Complex.norm_exp, Complex.mul_re]
  rw [psiIntegrand, norm_mul, he, mul_one, Complex.norm_real, Real.norm_eq_abs]
  exact abs_of_nonneg (sq_nonneg _)

/-- A second route to a uniform bound, by direct integration of the real profile. -/
theorem psi_norm_le_profile_integral (δ : ℝ) (τ : Tangent) :
    ‖psi δ τ‖ ≤ ∫ σ : Tangent, (max (δ-∑ i, σ i^2) 0)^2 := by
  have h := norm_integral_le_integral_norm (μ := volume) (f := psiIntegrand δ τ)
  simpa only [psi, psiIntegrand_norm_eq_profile] using h

theorem psi_zero_frequency_eq_profile_integral (δ : ℝ) :
    psi δ (0 : Tangent) =
      ((∫ σ : Tangent, (max (δ-∑ i, σ i^2) 0)^2 : ℝ) : ℂ) := by
  unfold psi
  simp only [psiIntegrand, Pi.zero_apply, zero_mul, Finset.sum_const_zero,
    Complex.ofReal_zero, mul_zero, Complex.exp_zero, mul_one]
  exact integral_ofReal

/-- A polynomial bound valid at every real Fourier frequency. -/
theorem psi_uniform_polynomial_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖ ≤ 8*δ^2*(δ+1)^2 := by
  have h := psi_depth_uniform_bound δ 0 (by norm_num) hδ τ
  simpa only [psi_zero_depth, sub_zero, mul_zero] using
    (show ‖psi δ τ-psi 0 τ‖ ≤ 8*δ^2*(δ+1)^2 from by
      calc
        _ ≤ 8*δ*(δ+1)^2*(δ-0) := h
        _ = _ := by ring)

/-- Both the profile and its first depth moment fit a degree-five envelope. -/
theorem psi_depth_moment_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    (1+δ)*‖psi δ τ‖ ≤ 8*(δ+1)^5 := by
  have hp := pow_le_pow_left₀ hδ (show δ ≤ δ+1 by linarith) 2
  calc
    _ ≤ (1+δ)*(8*δ^2*(δ+1)^2) :=
      mul_le_mul_of_nonneg_left (psi_uniform_polynomial_bound δ hδ τ) (by linarith)
    _ ≤ (1+δ)*(8*(δ+1)^2*(δ+1)^2) := by gcongr
    _ = _ := by ring

theorem depthTerm_norm (t θ : ℝ) (τ : Tangent) (j : ℕ) :
    ‖depthTerm t θ τ j‖ = Real.exp (-t*(θ+(j : ℝ))) *
      ‖psi ((θ+(j : ℝ))/Real.sqrt 3) τ‖ := by
  unfold depthTerm
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]

/-- Uniform in theta in [0,1] and in all Fourier frequencies; includes the depth moment. -/
theorem depthTerm_moment_envelope (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) (j : ℕ) :
    (1+(θ+(j : ℝ))/Real.sqrt 3)*‖depthTerm t θ τ j‖ ≤
      8*weightedDepthEnvelope t j := by
  let δ := (θ+(j : ℝ))/Real.sqrt 3
  have hd : 0 ≤ δ := by dsimp [δ]; positivity
  have hroot : (1 : ℝ) ≤ Real.sqrt 3 := by norm_num
  have hdj : δ+1 ≤ (j : ℝ)+2 := by
    have hh : δ ≤ θ+(j : ℝ) := div_le_self (by positivity) hroot
    linarith
  have he : Real.exp (-t*(θ+(j : ℝ))) ≤ Real.exp (-t*(j : ℝ)) := by
    apply Real.exp_le_exp.mpr
    nlinarith
  rw [depthTerm_norm]
  calc
    _ = Real.exp (-t*(θ+(j : ℝ))) * ((1+δ)*‖psi δ τ‖) := by dsimp [δ]; ring
    _ ≤ Real.exp (-t*(j : ℝ)) * (8*(δ+1)^5) :=
      mul_le_mul he (psi_depth_moment_bound δ hd τ) (by positivity) (Real.exp_nonneg _)
    _ ≤ Real.exp (-t*(j : ℝ)) * (8*((j : ℝ)+2)^5) := by gcongr
    _ = _ := by unfold weightedDepthEnvelope; ring

theorem depthTerm_envelope (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) (j : ℕ) :
    ‖depthTerm t θ τ j‖ ≤ 8*weightedDepthEnvelope t j := by
  have hd : 0 ≤ (θ+(j : ℝ))/Real.sqrt 3 := by positivity
  have h := depthTerm_moment_envelope t ht θ hθ hθ1 τ j
  nlinarith [norm_nonneg (depthTerm t θ τ j)]

def depthMomentTerm (t θ : ℝ) (τ : Tangent) (j : ℕ) : ℂ :=
  (((θ+(j : ℝ))/Real.sqrt 3 : ℝ) : ℂ) * depthTerm t θ τ j

theorem depthMomentTerm_envelope (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) (j : ℕ) :
    ‖depthMomentTerm t θ τ j‖ ≤ 8*weightedDepthEnvelope t j := by
  have hd : 0 ≤ (θ+(j : ℝ))/Real.sqrt 3 := by positivity
  have h := depthTerm_moment_envelope t ht θ hθ hθ1 τ j
  simp only [depthMomentTerm, norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hd]
  nlinarith [norm_nonneg (depthTerm t θ τ j)]

theorem depthTerm_summable (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) : Summable (depthTerm t θ τ) :=
  ((weightedDepthEnvelope_summable t ht).mul_left 8).of_norm_bounded
    (depthTerm_envelope t ht θ hθ hθ1 τ)

theorem depthMomentTerm_summable (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) : Summable (depthMomentTerm t θ τ) :=
  ((weightedDepthEnvelope_summable t ht).mul_left 8).of_norm_bounded
    (depthMomentTerm_envelope t ht θ hθ hθ1 τ)

def depthEnvelopeConstant (t : ℝ) : ℝ := 8*∑' j : ℕ, weightedDepthEnvelope t j

theorem sPlus_uniform_bound (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) :
    ‖sPlus t θ τ‖ ≤ depthEnvelopeConstant t := by
  have hs := depthTerm_summable t ht θ hθ hθ1 τ
  calc
    _ ≤ ∑' j : ℕ, ‖depthTerm t θ τ j‖ := norm_tsum_le_tsum_norm hs.norm
    _ ≤ ∑' j : ℕ, 8*weightedDepthEnvelope t j :=
      hs.norm.tsum_le_tsum (depthTerm_envelope t ht θ hθ hθ1 τ)
        ((weightedDepthEnvelope_summable t ht).mul_left 8)
    _ = _ := by rw [tsum_mul_left]; rfl

theorem depthMoment_uniform_bound (t : ℝ) (ht : 0 < t) (θ : ℝ)
    (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) :
    ∑' j : ℕ, ‖depthMomentTerm t θ τ j‖ ≤ depthEnvelopeConstant t := by
  have hs := depthMomentTerm_summable t ht θ hθ hθ1 τ
  calc
    _ ≤ ∑' j : ℕ, 8*weightedDepthEnvelope t j :=
      hs.norm.tsum_le_tsum (depthMomentTerm_envelope t ht θ hθ hθ1 τ)
        ((weightedDepthEnvelope_summable t ht).mul_left 8)
    _ = _ := by rw [tsum_mul_left]; rfl

theorem critical_depthTerm_summable (N : ℕ) (τ : Tangent) :
    Summable (depthTerm criticalTilt (theta N) τ) :=
  depthTerm_summable criticalTilt criticalTilt_pos (theta N)
    (Int.fract_nonneg _) (Int.fract_lt_one _).le τ

end AliceLayers
