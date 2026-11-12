import AliceLayers.DualDecay

noncomputable section
open scoped BigOperators
namespace AliceLayers

def depthErrorTiltConstant (t : ℝ) : ℝ := 16*∑' j : ℕ, weightedDepthEnvelope t j

theorem depthErrorTiltConstant_nonneg (t : ℝ) : 0 ≤ depthErrorTiltConstant t := by
  unfold depthErrorTiltConstant
  apply mul_nonneg (by norm_num)
  exact tsum_nonneg (fun j => by unfold weightedDepthEnvelope; positivity)

/-- A common summable envelope for the geometric depth error at every active layer. -/
theorem active_depth_error_polynomial (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    (indexedLayerDepth N k)^3*(indexedLayerDepth N k+1)^2 ≤
      ((layerNaturalIndex N k : ℝ)+2)^5 := by
  have hd := active_layer_depth_le_index N hN k hk
  have hbase : indexedLayerDepth N k+1 ≤ (layerNaturalIndex N k : ℝ)+2 := by linarith [hd.2]
  have hp := pow_le_pow_left₀ (show 0 ≤ indexedLayerDepth N k+1 by linarith [hd.1]) hbase 5
  have h3 := pow_le_pow_left₀ hd.1 (show indexedLayerDepth N k ≤ indexedLayerDepth N k+1 by linarith) 3
  calc
    _ ≤ (indexedLayerDepth N k+1)^3*(indexedLayerDepth N k+1)^2 :=
      mul_le_mul_of_nonneg_right h3 (sq_nonneg _)
    _ = (indexedLayerDepth N k+1)^5 := by ring
    _ ≤ _ := hp

def zeroModeDepthError (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k *
    (psi (effectiveLayerDepth N k) (tau N η)-psi (indexedLayerDepth N k) (tau N η))

/-- The depth replacement is O(1/N), after summing all active layers, for every frequency. -/
theorem zeroModeDepthError_uniform_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) : ‖zeroModeDepthError N t η‖ ≤ depthErrorTiltConstant t/(N : ℝ) := by
  let S := (aliceSites N).image planeIndex
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hpoint (k : ℤ) (hk : k ∈ S) :
      ‖layerGlobalFactor N t η k *
        (psi (effectiveLayerDepth N k) (tau N η)-psi (indexedLayerDepth N k) (tau N η))‖ ≤
      ((16 : ℝ)/(N : ℝ))*weightedDepthEnvelope t (layerNaturalIndex N k) := by
    have hp := mul_le_mul_of_nonneg_left (active_depth_error_polynomial N hN k hk) (by norm_num : (0:ℝ) ≤ 16)
    have hb : ‖psi (effectiveLayerDepth N k) (tau N η)-psi (indexedLayerDepth N k) (tau N η)‖ ≤
        16*((layerNaturalIndex N k : ℝ)+2)^5/(N : ℝ) := by
      rw [norm_sub_rev]
      exact (psi_effective_depth_error N hN k hk (tau N η)).trans
        ((div_le_div_iff_of_pos_right hn).2 (by simpa only [mul_assoc] using hp))
    rw [norm_mul]
    calc
      _ ≤ Real.exp (-t*(layerNaturalIndex N k : ℝ))*(16*((layerNaturalIndex N k : ℝ)+2)^5/(N : ℝ)) :=
        mul_le_mul (layerGlobalFactor_norm_bound N hN t ht η k hk) hb (norm_nonneg _) (Real.exp_nonneg _)
      _ = _ := by unfold weightedDepthEnvelope; ring
  unfold zeroModeDepthError
  calc
    _ ≤ ∑ k ∈ S, ‖layerGlobalFactor N t η k *
        (psi (effectiveLayerDepth N k) (tau N η)-psi (indexedLayerDepth N k) (tau N η))‖ := norm_sum_le _ _
    _ ≤ ∑ k ∈ S, ((16 : ℝ)/(N : ℝ))*weightedDepthEnvelope t (layerNaturalIndex N k) := Finset.sum_le_sum hpoint
    _ = ((16 : ℝ)/(N : ℝ))*∑ k ∈ S, weightedDepthEnvelope t (layerNaturalIndex N k) := by rw [Finset.mul_sum]
    _ = ((16 : ℝ)/(N : ℝ))*∑ j ∈ S.image (layerNaturalIndex N), weightedDepthEnvelope t j := by
      rw [Finset.sum_image (active_layer_index_injective N hN)]
    _ ≤ ((16 : ℝ)/(N : ℝ))*∑' j : ℕ, weightedDepthEnvelope t j := by
      exact mul_le_mul_of_nonneg_left ((weightedDepthEnvelope_summable t ht).sum_le_tsum _
        (fun j _ => by unfold weightedDepthEnvelope; positivity)) (by positivity)
    _ = _ := by unfold depthErrorTiltConstant; ring

theorem critical_zeroModeDepthError_bound (N : ℕ) (hN : 0 < N) (η : Frequency) :
    ‖zeroModeDepthError N criticalTilt η‖ ≤ depthErrorTiltConstant criticalTilt/(N : ℝ) :=
  zeroModeDepthError_uniform_bound N hN criticalTilt criticalTilt_pos η

def depthAmplitudeConstant : ℝ :=
  |(16*Real.pi/Real.sqrt 3)*boundaryResource| * depthErrorTiltConstant criticalTilt

/-- The contribution of the depth replacement to the original amplitude is O(N^(-7/2)). -/
theorem zeroModeDepth_amplitude_bound (N : ℕ) (hN : 0 < N) (η : Frequency) :
    ‖(leadingScale N : ℂ)*zeroModeDepthError N criticalTilt η‖ ≤
      depthAmplitudeConstant/((N : ℝ)^3*Real.sqrt (N : ℝ)) := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have he : Real.rpow (N : ℝ) (-(5 : ℝ)/2) = 1/((N : ℝ)^2*Real.sqrt (N : ℝ)) :=
    rpow_neg_five_halves _ hn
  have hlead : ‖(leadingScale N : ℂ)‖ =
      (1/((N : ℝ)^2*Real.sqrt (N : ℝ)))*|(16*Real.pi/Real.sqrt 3)*boundaryResource| := by
    rw [Complex.norm_real,Real.norm_eq_abs]
    unfold leadingScale
    rw [he,mul_assoc,abs_mul,abs_of_pos (by positivity : 0 < 1/((N : ℝ)^2*Real.sqrt (N : ℝ)))]
  rw [norm_mul,hlead]
  calc
    _ ≤ ((1/((N : ℝ)^2*Real.sqrt (N : ℝ)))*|(16*Real.pi/Real.sqrt 3)*boundaryResource|)*
      (depthErrorTiltConstant criticalTilt/(N : ℝ)) :=
      mul_le_mul_of_nonneg_left (critical_zeroModeDepthError_bound N hN η) (by positivity)
    _ = _ := by unfold depthAmplitudeConstant; ring

def geometricZeroModeSum (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k * psi (indexedLayerDepth N k) (tau N η)
def effectiveZeroModeSum (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k * psi (effectiveLayerDepth N k) (tau N η)

/-- Fixes the sign of the correction independently of the norm estimate. -/
theorem zeroModeDepthError_eq_difference (N : ℕ) (t : ℝ) (η : Frequency) :
    zeroModeDepthError N t η = effectiveZeroModeSum N t η-geometricZeroModeSum N t η := by
  unfold zeroModeDepthError effectiveZeroModeSum geometricZeroModeSum
  simp only [mul_sub,Finset.sum_sub_distrib]

def nonzeroLayerAggregate (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k *
    (layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))
def finiteProfileErrorAggregate (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k * finiteLayerError N k (tau N η)

/-- Exact original amplitude after replacing the effective depth in the zero mode. -/
theorem amplitude_geometric_zero_decomposition (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) :
    amplitude N t η = (leadingScale N : ℂ)*
      (geometricZeroModeSum N t η+zeroModeDepthError N t η+nonzeroLayerAggregate N t η) +
        finiteProfileErrorAggregate N t η := by
  rw [amplitude_finite_profile_poisson N hN]
  unfold geometricZeroModeSum zeroModeDepthError nonzeroLayerAggregate finiteProfileErrorAggregate
  conv_rhs =>
    rw [mul_add,mul_add,Finset.mul_sum,Finset.mul_sum,Finset.mul_sum,
      ← Finset.sum_add_distrib,← Finset.sum_add_distrib,← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro k hk
  ring

def geometricZeroErrorConstant : ℝ := finiteErrorTiltConstant criticalTilt+depthAmplitudeConstant

/-- Combined finite-profile, dual and zero-mode-depth errors; normal phase and missing layers remain. -/
theorem amplitude_geometric_zero_error (N : ℕ) (hN : 0 < N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*geometricZeroModeSum N criticalTilt η‖ ≤
      geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ))+dualAmplitudeConstant/(N : ℝ)^4 := by
  have he : amplitude N criticalTilt η-(leadingScale N : ℂ)*geometricZeroModeSum N criticalTilt η =
      finiteProfileErrorAggregate N criticalTilt η +
        (leadingScale N : ℂ)*zeroModeDepthError N criticalTilt η +
          (leadingScale N : ℂ)*nonzeroLayerAggregate N criticalTilt η := by
    rw [amplitude_geometric_zero_decomposition N hN]
    ring
  rw [he]
  calc
    _ ≤ (‖finiteProfileErrorAggregate N criticalTilt η‖+
      ‖(leadingScale N : ℂ)*zeroModeDepthError N criticalTilt η‖) +
        ‖(leadingScale N : ℂ)*nonzeroLayerAggregate N criticalTilt η‖ :=
      (norm_add_le _ _).trans (add_le_add (norm_add_le _ _) (le_refl _))
    _ ≤ (finiteErrorTiltConstant criticalTilt/((N : ℝ)^3*Real.sqrt (N : ℝ))+
      depthAmplitudeConstant/((N : ℝ)^3*Real.sqrt (N : ℝ)))+dualAmplitudeConstant/(N : ℝ)^4 :=
      add_le_add (add_le_add (critical_weighted_finiteLayerError_bound N hN η)
        (zeroModeDepth_amplitude_bound N hN η)) (dual_amplitude_uniform_bound N hN η hη)
    _ = _ := by unfold geometricZeroErrorConstant; ring

end AliceLayers
