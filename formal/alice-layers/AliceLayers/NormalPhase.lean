import AliceLayers.DepthEnvelope

noncomputable section
open scoped BigOperators
namespace AliceLayers

theorem active_layer_weight_index (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    theta N+(layerNaturalIndex N k : ℝ) = Real.sqrt 3*(N : ℝ)/4-(k : ℝ) := by
  have hc := congrArg (fun z : ℤ => (z : ℝ)) (active_layer_index_cast N hN k hk)
  push_cast at hc
  have hf := Int.fract_add_floor (Real.sqrt 3*(N : ℝ)/4)
  unfold theta
  linarith

/-- Exact phase and weight, with the geometric depth and natural depth index. -/
theorem geometric_layer_phase_identity (N : ℕ) (hN : 0 < N) (t : ℝ)
    (η : Frequency) (k : ℤ) (hk : k ∈ (aliceSites N).image planeIndex) :
    layerGlobalFactor N t η k * psi (indexedLayerDepth N k) (tau N η) =
      Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ)) *
        depthTerm t (theta N) (tau N η) (layerNaturalIndex N k) := by
  have hw := active_layer_weight_index N hN k hk
  have hp : normalFrequency η*((k : ℝ)/Real.sqrt 3-(N : ℝ)/4) =
      -normalFrequency η*indexedLayerDepth N k := by unfold indexedLayerDepth; ring
  unfold layerGlobalFactor depthTerm
  rw [hp, ← active_layer_index_depth N hN k hk]
  have he : t*((k : ℝ)-Real.sqrt 3*(N : ℝ)/4) =
      -t*(theta N+(layerNaturalIndex N k : ℝ)) := by rw [hw]; ring
  rw [he]
  ring

def unphasedZeroModeSum (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex,
    depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)

def normalPhaseError (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex,
    (Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ))-1) *
      depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)

/-- The sign is fixed by an exact difference of finite sums. -/
theorem normalPhaseError_eq_difference (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) :
    normalPhaseError N t η = geometricZeroModeSum N t η-unphasedZeroModeSum N t η := by
  unfold normalPhaseError geometricZeroModeSum unphasedZeroModeSum
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro k hk
  rw [geometric_layer_phase_identity N hN t η k hk]
  ring

theorem normalPhaseError_zero (N : ℕ) (t : ℝ) (η : Frequency)
    (hη : normalFrequency η = 0) : normalPhaseError N t η = 0 := by
  simp [normalPhaseError, hη]

theorem normal_phase_term_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) (k : ℤ) (hk : k ∈ (aliceSites N).image planeIndex) :
    ‖(Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ))-1) *
      depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)‖ ≤
      (8*|normalFrequency η|)*weightedDepthEnvelope t (layerNaturalIndex N k) := by
  have hd := (active_layer_depth_le_index N hN k hk).1
  have he : ‖Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ))-1‖ ≤
      |normalFrequency η| * indexedLayerDepth N k := by
    have h := Real.norm_exp_I_mul_ofReal_sub_one_le (x := -normalFrequency η*indexedLayerDepth N k)
    simpa only [Real.norm_eq_abs, abs_mul, abs_neg, abs_of_nonneg hd] using h
  have hm := depthMomentTerm_envelope t ht (theta N) (Int.fract_nonneg _)
    (Int.fract_lt_one _).le (tau N η) (layerNaturalIndex N k)
  have hm' : indexedLayerDepth N k * ‖depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)‖ ≤
      8*weightedDepthEnvelope t (layerNaturalIndex N k) := by
    simpa only [depthMomentTerm, norm_mul, Complex.norm_real, Real.norm_eq_abs,
      ← active_layer_index_depth N hN k hk, abs_of_nonneg hd] using hm
  rw [norm_mul]
  calc
    _ ≤ (|normalFrequency η| * indexedLayerDepth N k) *
        ‖depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)‖ :=
      mul_le_mul_of_nonneg_right he (norm_nonneg _)
    _ = |normalFrequency η| * (indexedLayerDepth N k *
        ‖depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)‖) := by ring
    _ ≤ |normalFrequency η| * (8*weightedDepthEnvelope t (layerNaturalIndex N k)) :=
      mul_le_mul_of_nonneg_left hm' (abs_nonneg _)
    _ = _ := by ring

/-- Uniform in N and all frequencies; no small-frequency restriction is needed. -/
theorem normalPhaseError_uniform_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) : ‖normalPhaseError N t η‖ ≤ depthEnvelopeConstant t*|normalFrequency η| := by
  let S := (aliceSites N).image planeIndex
  have hc : 0 ≤ 8*|normalFrequency η| := by positivity
  unfold normalPhaseError
  calc
    _ ≤ ∑ k ∈ S, ‖(Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ))-1) *
        depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)‖ := norm_sum_le _ _
    _ ≤ ∑ k ∈ S, (8*|normalFrequency η|)*weightedDepthEnvelope t (layerNaturalIndex N k) :=
      Finset.sum_le_sum (fun k hk => normal_phase_term_bound N hN t ht η k hk)
    _ = (8*|normalFrequency η|)*∑ j ∈ S.image (layerNaturalIndex N), weightedDepthEnvelope t j := by
      rw [← Finset.mul_sum, Finset.sum_image (active_layer_index_injective N hN)]
    _ ≤ (8*|normalFrequency η|)*∑' j : ℕ, weightedDepthEnvelope t j := by
      apply mul_le_mul_of_nonneg_left _ hc
      exact (weightedDepthEnvelope_summable t ht).sum_le_tsum _
        (fun j _ => by unfold weightedDepthEnvelope; positivity)
    _ = _ := by unfold depthEnvelopeConstant; ring

theorem critical_normalPhaseError_bound (N : ℕ) (hN : 0 < N) (η : Frequency) :
    ‖normalPhaseError N criticalTilt η‖ ≤ depthEnvelopeConstant criticalTilt*|normalFrequency η| :=
  normalPhaseError_uniform_bound N hN criticalTilt criticalTilt_pos η

/-- Reconstructs the original amplitude, now with an unphased finite main sum. -/
theorem amplitude_unphased_zero_decomposition (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) :
    amplitude N t η = (leadingScale N : ℂ) *
      (unphasedZeroModeSum N t η+normalPhaseError N t η+zeroModeDepthError N t η+
        nonzeroLayerAggregate N t η)+finiteProfileErrorAggregate N t η := by
  rw [amplitude_geometric_zero_decomposition N hN t η,
    normalPhaseError_eq_difference N hN t η]
  ring

theorem amplitude_unphased_zero_error (N : ℕ) (hN : 1 ≤ N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*unphasedZeroModeSum N criticalTilt η‖ ≤
      geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ))+dualAmplitudeConstant/(N : ℝ)^4+
        |leadingScale N| * (depthEnvelopeConstant criticalTilt*|normalFrequency η|) := by
  have hn : 0 < N := lt_of_lt_of_le Nat.zero_lt_one hN
  have he : amplitude N criticalTilt η-(leadingScale N : ℂ)*unphasedZeroModeSum N criticalTilt η =
      (amplitude N criticalTilt η-(leadingScale N : ℂ)*geometricZeroModeSum N criticalTilt η)+
        (leadingScale N : ℂ)*normalPhaseError N criticalTilt η := by
    rw [normalPhaseError_eq_difference N hn criticalTilt η]
    ring
  rw [he]
  calc
    _ ≤ ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*geometricZeroModeSum N criticalTilt η‖+
        ‖(leadingScale N : ℂ)*normalPhaseError N criticalTilt η‖ := norm_add_le _ _
    _ ≤ geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ))+dualAmplitudeConstant/(N : ℝ)^4+
        |leadingScale N| * (depthEnvelopeConstant criticalTilt*|normalFrequency η|) := by
      apply add_le_add (amplitude_geometric_zero_error N hN η hη)
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs]
      exact mul_le_mul_of_nonneg_left (critical_normalPhaseError_bound N hn η) (abs_nonneg _)

end AliceLayers
