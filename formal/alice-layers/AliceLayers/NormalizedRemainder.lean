import AliceLayers.DepthCompletion

noncomputable section
open scoped BigOperators
open MeasureTheory
namespace AliceLayers

theorem boundary_sinc_lower (k : ℝ) (hk : k ∈ Set.Icc (0 : ℝ) 1) :
    (3 : ℝ)/4 ≤ Real.sinc (k*(1/4)) := by
  have h := sinc_lipschitz_bound (k*(1/4)) 0
  rw [Real.sinc_zero, sub_zero,
    abs_of_nonneg (mul_nonneg hk.1 (by norm_num : (0 : ℝ) ≤ 1/4))] at h
  have hh := (abs_le.mp h).1
  linarith [hk.2]

theorem boundary_kernel_integral_pos :
    0 < ∫ k in (0 : ℝ)..1, k^2*(1-k^2)^2*Real.sinc (k*(1/4)) := by
  apply intervalIntegral.integral_pos (by norm_num : (0 : ℝ) < 1)
  · exact (by fun_prop : Continuous (fun k : ℝ => k^2*(1-k^2)^2*Real.sinc (k*(1/4)))).continuousOn
  · intro k hk
    have hs := boundary_sinc_lower k ⟨hk.1.le,hk.2⟩
    exact mul_nonneg (mul_nonneg (sq_nonneg _) (sq_nonneg _)) (by linarith)
  · refine ⟨1/2, by norm_num, ?_⟩
    have hs := boundary_sinc_lower (1/2) (by norm_num)
    norm_num only [one_div, inv_pow] at *
    positivity

theorem boundaryResource_pos : 0 < boundaryResource := by
  unfold boundaryResource phi0
  have hc : 0 < cResource := by unfold cResource; positivity
  exact mul_pos (by positivity) boundary_kernel_integral_pos

def scalarLeadingCoefficient : ℝ := (16*Real.pi/Real.sqrt 3)*boundaryResource

theorem scalarLeadingCoefficient_pos : 0 < scalarLeadingCoefficient := by
  unfold scalarLeadingCoefficient
  exact mul_pos (by positivity) boundaryResource_pos

theorem leadingScale_fraction (N : ℕ) (hN : 0 < N) :
    leadingScale N = scalarLeadingCoefficient/((N : ℝ)^2*Real.sqrt (N : ℝ)) := by
  unfold leadingScale scalarLeadingCoefficient
  have he : Real.rpow (N : ℝ) (-(5 : ℝ)/2) = 1/((N : ℝ)^2*Real.sqrt (N : ℝ)) :=
    rpow_neg_five_halves _ (Nat.cast_pos.mpr hN)
  rw [he]
  ring

theorem leadingScale_pos (N : ℕ) (hN : 0 < N) : 0 < leadingScale N := by
  rw [leadingScale_fraction N hN]
  exact div_pos scalarLeadingCoefficient_pos (by positivity)

/-- Explicit normalized residual; its denominator is proved nonzero for N>0. -/
def normalizedRemainder (N : ℕ) (η : Frequency) : ℂ :=
  (amplitude N criticalTilt η-(leadingScale N : ℂ)*sPlus criticalTilt (theta N) (tau N η)) /
    (leadingScale N : ℂ)

/-- Multiplication by the original prefactor reconstructs the exact amplitude. -/
theorem normalizedRemainder_identity (N : ℕ) (hN : 0 < N) (η : Frequency) :
    amplitude N criticalTilt η = (leadingScale N : ℂ)*
      (sPlus criticalTilt (theta N) (tau N η)+normalizedRemainder N η) := by
  have hl : (leadingScale N : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr (ne_of_gt (leadingScale_pos N hN))
  unfold normalizedRemainder
  field_simp
  ring

theorem normalizedRemainder_norm (N : ℕ) (hN : 0 < N) (η : Frequency) :
    ‖normalizedRemainder N η‖ =
      ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*sPlus criticalTilt (theta N) (tau N η)‖ /
        leadingScale N := by
  rw [normalizedRemainder, norm_div, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos (leadingScale_pos N hN)]

/-- Exact power-of-N check for the geometric finite-profile and depth errors. -/
theorem geometric_error_normalization (N : ℕ) (hN : 0 < N) :
    (geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ)))/leadingScale N =
      (geometricZeroErrorConstant/scalarLeadingCoefficient)/(N : ℝ) := by
  have hn : (N : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr hN)
  have hs : Real.sqrt (N : ℝ) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (Nat.cast_pos.mpr hN))
  have hc := ne_of_gt scalarLeadingCoefficient_pos
  rw [leadingScale_fraction N hN]
  field_simp
  <;> ring

/-- The dual error becomes O(N^(-3/2)) after dividing by the leading scale. -/
theorem dual_error_normalization (N : ℕ) (hN : 0 < N) :
    (dualAmplitudeConstant/(N : ℝ)^4)/leadingScale N =
      (dualAmplitudeConstant/scalarLeadingCoefficient)/((N : ℝ)*Real.sqrt (N : ℝ)) := by
  have hn : (N : ℝ) ≠ 0 := ne_of_gt (Nat.cast_pos.mpr hN)
  have hs : Real.sqrt (N : ℝ) ≠ 0 := ne_of_gt (Real.sqrt_pos.mpr (Nat.cast_pos.mpr hN))
  have hc := ne_of_gt scalarLeadingCoefficient_pos
  rw [leadingScale_fraction N hN]
  field_simp
  <;> ring_nf
  <;> simp only [Real.sq_sqrt (Nat.cast_nonneg N)]

def normalizedGeometricConstant : ℝ := |geometricZeroErrorConstant|/scalarLeadingCoefficient
def normalizedDualConstant : ℝ := |dualAmplitudeConstant|/scalarLeadingCoefficient

/-- A finer estimate, retaining the separate powers before weakening to the target. -/
theorem normalizedRemainder_component_bound (N : ℕ) (hN : 1 ≤ N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖normalizedRemainder N η‖ ≤
      normalizedGeometricConstant/(N : ℝ)+normalizedDualConstant/((N : ℝ)*Real.sqrt (N : ℝ))+
        depthEnvelopeConstant criticalTilt*|normalFrequency η|+depthCompletionConstant criticalTilt/(N : ℝ) := by
  have hn : 0 < N := lt_of_lt_of_le Nat.zero_lt_one hN
  have hl := leadingScale_pos N hn
  rw [normalizedRemainder_norm N hn]
  have hb := div_le_div_of_nonneg_right (amplitude_full_depth_error N hN η hη) hl.le
  rw [abs_of_pos hl, add_div, add_div,
    geometric_error_normalization N hn, dual_error_normalization N hn,
    mul_div_cancel_left₀ _ (ne_of_gt hl)] at hb
  apply hb.trans
  unfold normalizedGeometricConstant normalizedDualConstant
  have hg : geometricZeroErrorConstant/scalarLeadingCoefficient ≤
      |geometricZeroErrorConstant|/scalarLeadingCoefficient :=
    div_le_div_of_nonneg_right (le_abs_self _) scalarLeadingCoefficient_pos.le
  have hd : dualAmplitudeConstant/scalarLeadingCoefficient ≤
      |dualAmplitudeConstant|/scalarLeadingCoefficient :=
    div_le_div_of_nonneg_right (le_abs_self _) scalarLeadingCoefficient_pos.le
  have hg' := div_le_div_of_nonneg_right hg (Nat.cast_nonneg N)
  have hd' := div_le_div_of_nonneg_right hd (by positivity : 0 ≤ (N : ℝ)*Real.sqrt (N : ℝ))
  linarith

def normalizedTotalConstant : ℝ :=
  normalizedGeometricConstant+normalizedDualConstant+depthCompletionConstant criticalTilt+
    depthEnvelopeConstant criticalTilt

theorem depthEnvelopeConstant_nonneg (t : ℝ) : 0 ≤ depthEnvelopeConstant t := by
  unfold depthEnvelopeConstant
  apply mul_nonneg (by norm_num)
  exact tsum_nonneg (fun j => by unfold weightedDepthEnvelope; positivity)

theorem normalizedTotalConstant_nonneg : 0 ≤ normalizedTotalConstant := by
  have hg : 0 ≤ normalizedGeometricConstant := div_nonneg (abs_nonneg _) scalarLeadingCoefficient_pos.le
  have hd : 0 ≤ normalizedDualConstant := div_nonneg (abs_nonneg _) scalarLeadingCoefficient_pos.le
  unfold normalizedTotalConstant
  exact add_nonneg (add_nonneg (add_nonneg hg hd) (depthCompletionConstant_nonneg _))
    (depthEnvelopeConstant_nonneg _)

theorem rpow_neg_half_eq_inv_sqrt (x : ℝ) (hx : 0 < x) :
    Real.rpow x (-(1 : ℝ)/2) = 1/Real.sqrt x := by
  have he : Real.rpow x (-((1 : ℝ)/2)) = (Real.rpow x ((1 : ℝ)/2))⁻¹ := Real.rpow_neg hx.le _
  have hh : Real.rpow x ((1 : ℝ)/2) = Real.sqrt x := by
    have hhalf : x ^ ((1 : ℝ)/2) = Real.sqrt x := by
      simpa only [Real.rpow_one] using Real.rpow_div_two_eq_sqrt (1 : ℝ) hx.le
    exact hhalf
  rw [show (-(1 : ℝ)/2) = -((1 : ℝ)/2) by ring, he, hh, one_div]

/-- Exactly the normalized error estimate requested by Targets.AliceLayersB. -/
theorem normalizedRemainder_uniform_bound (N : ℕ) (hN : 1 ≤ N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖normalizedRemainder N η‖ ≤ normalizedTotalConstant *
      (Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|) := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr (lt_of_lt_of_le Nat.zero_lt_one hN)
  have hn1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hs : 0 < Real.sqrt (N : ℝ) := Real.sqrt_pos.mpr hn
  have hsN : Real.sqrt (N : ℝ) ≤ N := Real.sqrt_le_iff.mpr ⟨hn.le, by nlinarith⟩
  have hsNs : Real.sqrt (N : ℝ) ≤ (N : ℝ)*Real.sqrt (N : ℝ) := by nlinarith
  have hg : 0 ≤ normalizedGeometricConstant := div_nonneg (abs_nonneg _) scalarLeadingCoefficient_pos.le
  have hd : 0 ≤ normalizedDualConstant := div_nonneg (abs_nonneg _) scalarLeadingCoefficient_pos.le
  have hc := depthCompletionConstant_nonneg criticalTilt
  have hh := depthEnvelopeConstant_nonneg criticalTilt
  have hgb := div_le_div_of_nonneg_left hg hs hsN
  have hdb := div_le_div_of_nonneg_left hd hs hsNs
  have hcb := div_le_div_of_nonneg_left hc hs hsN
  rw [rpow_neg_half_eq_inv_sqrt _ hn]
  apply (normalizedRemainder_component_bound N hN η hη).trans
  have hab := abs_nonneg (normalFrequency η)
  unfold normalizedTotalConstant
  have ha := mul_nonneg (add_nonneg (add_nonneg hg hd) hc) hab
  have hb := div_nonneg hh hs.le
  simp only [div_eq_mul_inv] at *
  nlinarith

end AliceLayers
