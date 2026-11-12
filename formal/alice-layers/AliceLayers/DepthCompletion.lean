import AliceLayers.DepthGeometry

noncomputable section
open scoped BigOperators
namespace AliceLayers

theorem unphasedZeroModeSum_eq_index_sum (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) :
    unphasedZeroModeSum N t η =
      ∑ j ∈ activeDepthIndices N, depthTerm t (theta N) (tau N η) j := by
  unfold unphasedZeroModeSum activeDepthIndices
  rw [Finset.sum_image (active_layer_index_injective N hN)]

/-- Small depths are controlled by the vanishing of the profile at depth zero. -/
theorem small_depth_term_envelope (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (θ : ℝ) (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) (j : ℕ)
    (hsmall : (θ+(j : ℝ))/Real.sqrt 3 ≤ 12/(N : ℝ)) :
    ‖depthTerm t θ τ j‖ ≤ (96/(N : ℝ))*weightedDepthEnvelope t j := by
  let δ := (θ+(j : ℝ))/Real.sqrt 3
  have hd : 0 ≤ δ := by dsimp [δ]; positivity
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hdj : δ+1 ≤ (j : ℝ)+2 := by
    have hr : (1 : ℝ) ≤ Real.sqrt 3 := by norm_num
    have h := div_le_self (show 0 ≤ θ+(j : ℝ) by positivity) hr
    change δ ≤ θ+(j : ℝ) at h
    linarith
  have hp : ‖psi δ τ‖ ≤ (96/(N : ℝ))*((j : ℝ)+2)^5 := by
    calc
      _ ≤ 8*δ^2*(δ+1)^2 := psi_uniform_polynomial_bound δ hd τ
      _ = 8*δ*(δ*(δ+1)^2) := by ring
      _ ≤ 8*δ*((δ+1)*(δ+1)^2) := by gcongr; linarith
      _ = 8*δ*(δ+1)^3 := by ring
      _ ≤ 8*(12/(N : ℝ))*((j : ℝ)+2)^3 := by gcongr
      _ ≤ 8*(12/(N : ℝ))*((j : ℝ)+2)^5 := by
        apply mul_le_mul_of_nonneg_left
          (pow_le_pow_right₀ (by have hj : (0 : ℝ) ≤ j := Nat.cast_nonneg j; linarith : (1 : ℝ) ≤ (j : ℝ)+2)
            (by norm_num : 3 ≤ 5))
        positivity
      _ = _ := by ring
  have he : Real.exp (-t*(θ+(j : ℝ))) ≤ Real.exp (-t*(j : ℝ)) := by
    apply Real.exp_le_exp.mpr
    nlinarith
  rw [depthTerm_norm]
  calc
    _ ≤ Real.exp (-t*(j : ℝ))*((96/(N : ℝ))*((j : ℝ)+2)^5) :=
      mul_le_mul he hp (norm_nonneg _) (Real.exp_nonneg _)
    _ = _ := by unfold weightedDepthEnvelope; ring

/-- The already summable first moment bounds all depths beyond N/4. -/
theorem deep_depth_term_envelope (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (θ : ℝ) (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) (j : ℕ)
    (hdeep : (N : ℝ)/4 ≤ (θ+(j : ℝ))/Real.sqrt 3) :
    ‖depthTerm t θ τ j‖ ≤ (32/(N : ℝ))*weightedDepthEnvelope t j := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hm := depthTerm_moment_envelope t ht θ hθ hθ1 τ j
  have hh := mul_nonneg (norm_nonneg (depthTerm t θ τ j)) (sub_nonneg.mpr hdeep)
  have h : ‖depthTerm t θ τ j‖ ≤ (32*weightedDepthEnvelope t j)/(N : ℝ) := by
    apply (le_div_iff₀ hn).2
    nlinarith [norm_nonneg (depthTerm t θ τ j)]
  convert h using 1 <;> ring

/-- All omitted indices are covered, including empty spherical layers and the infinite tail. -/
theorem omitted_depth_term_envelope (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (τ : Tangent) (j : ℕ) (hj : j ∉ activeDepthIndices N) :
    ‖depthTerm t (theta N) τ j‖ ≤ (96/(N : ℝ))*weightedDepthEnvelope t j := by
  have hθ : 0 ≤ theta N := Int.fract_nonneg _
  have hθ1 : theta N ≤ 1 := (Int.fract_lt_one _).le
  rcases omitted_depth_dichotomy N hN j hj with hsmall | hdeep
  · exact small_depth_term_envelope N hN t ht (theta N) hθ hθ1 τ j hsmall
  · have h := deep_depth_term_envelope N hN t ht (theta N) hθ hθ1 τ j hdeep.le
    apply h.trans
    apply mul_le_mul_of_nonneg_right _ (by unfold weightedDepthEnvelope; positivity)
    exact div_le_div_of_nonneg_right (by norm_num : (32 : ℝ) ≤ 96) (Nat.cast_nonneg N)

/-- General subseries bound; the right side uses the full nonnegative envelope. -/
theorem depth_subseries_envelope_bound (t : ℝ) (ht : 0 < t) (θ : ℝ) (τ : Tangent)
    (p : ℕ → Prop) (C : ℝ) (hC : 0 ≤ C)
    (hp : ∀ j, p j → ‖depthTerm t θ τ j‖ ≤ C*weightedDepthEnvelope t j) :
    ‖∑' j : Subtype p, depthTerm t θ τ j‖ ≤ C*∑' j : ℕ, weightedDepthEnvelope t j := by
  have hg := (weightedDepthEnvelope_summable t ht).mul_left C
  have hs : Summable (fun j : Subtype p => depthTerm t θ τ j) :=
    (hg.subtype p).of_norm_bounded (fun j => hp j j.property)
  calc
    _ ≤ ∑' j : Subtype p, ‖depthTerm t θ τ j‖ := norm_tsum_le_tsum_norm hs.norm
    _ ≤ ∑' j : Subtype p, C*weightedDepthEnvelope t j :=
      hs.norm.tsum_le_tsum (fun j => hp j j.property) (hg.subtype p)
    _ ≤ ∑' j : ℕ, C*weightedDepthEnvelope t j :=
      Summable.tsum_subtype_le _ _ (fun j => mul_nonneg hC (by unfold weightedDepthEnvelope; positivity)) hg
    _ = _ := tsum_mul_left

/-- Includes, in particular, every depth outside the finite spherical range. -/
theorem deep_depth_sum_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (θ : ℝ) (hθ : 0 ≤ θ) (hθ1 : θ ≤ 1) (τ : Tangent) :
    ‖∑' j : {j : ℕ // (N : ℝ)/4 ≤ (θ+(j : ℝ))/Real.sqrt 3}, depthTerm t θ τ j‖ ≤
      (32/(N : ℝ))*∑' j : ℕ, weightedDepthEnvelope t j :=
  depth_subseries_envelope_bound t ht θ τ _ _ (by positivity)
    (fun j hj => deep_depth_term_envelope N hN t ht θ hθ hθ1 τ j hj)

theorem shallow_omitted_depth_sum_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (τ : Tangent) :
    ‖∑' j : {j : ℕ // j ∉ activeDepthIndices N ∧
      (theta N+(j : ℝ))/Real.sqrt 3 ≤ (N : ℝ)/4}, depthTerm t (theta N) τ j‖ ≤
      (96/(N : ℝ))*∑' j : ℕ, weightedDepthEnvelope t j :=
  depth_subseries_envelope_bound t ht (theta N) τ _ _ (by positivity)
    (fun j hj => omitted_depth_term_envelope N hN t ht τ j hj.1)

/-- Sign convention: full infinite depth sum minus the unphased active-layer sum. -/
def depthCompletionError (N : ℕ) (t : ℝ) (τ : Tangent) : ℂ :=
  ∑' j : {j : ℕ // j ∉ activeDepthIndices N}, depthTerm t (theta N) τ j

theorem depthCompletionError_summable (N : ℕ) (t : ℝ) (ht : 0 < t) (τ : Tangent) :
    Summable (fun j : {j : ℕ // j ∉ activeDepthIndices N} => depthTerm t (theta N) τ j) :=
  (depthTerm_summable t ht (theta N) (Int.fract_nonneg _) (Int.fract_lt_one _).le τ).subtype _

theorem depthCompletionError_eq_difference (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) :
    depthCompletionError N t (tau N η) = sPlus t (theta N) (tau N η)-unphasedZeroModeSum N t η := by
  have hs := depthTerm_summable t ht (theta N) (Int.fract_nonneg _) (Int.fract_lt_one _).le (tau N η)
  have he := hs.sum_add_tsum_subtype_compl (activeDepthIndices N)
  rw [← unphasedZeroModeSum_eq_index_sum N hN t η] at he
  change unphasedZeroModeSum N t η+depthCompletionError N t (tau N η) = sPlus t (theta N) (tau N η) at he
  exact eq_sub_iff_add_eq.mpr (by simpa only [add_comm] using he)

def depthCompletionConstant (t : ℝ) : ℝ := 96*∑' j : ℕ, weightedDepthEnvelope t j

theorem depthCompletionConstant_nonneg (t : ℝ) : 0 ≤ depthCompletionConstant t := by
  unfold depthCompletionConstant
  apply mul_nonneg (by norm_num)
  exact tsum_nonneg (fun j => by unfold weightedDepthEnvelope; positivity)

theorem depthCompletionError_uniform_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (τ : Tangent) : ‖depthCompletionError N t τ‖ ≤ depthCompletionConstant t/(N : ℝ) := by
  have h := depth_subseries_envelope_bound t ht (theta N) τ
    (fun j => j ∉ activeDepthIndices N) (96/(N : ℝ)) (by positivity)
    (fun j hj => omitted_depth_term_envelope N hN t ht τ j hj)
  calc
    _ ≤ (96/(N : ℝ))*∑' j : ℕ, weightedDepthEnvelope t j := h
    _ = _ := by unfold depthCompletionConstant; ring

theorem critical_depthCompletionError_bound (N : ℕ) (hN : 0 < N) (τ : Tangent) :
    ‖depthCompletionError N criticalTilt τ‖ ≤ depthCompletionConstant criticalTilt/(N : ℝ) :=
  depthCompletionError_uniform_bound N hN criticalTilt criticalTilt_pos τ

theorem depthTerm_zero_shift_index (t : ℝ) (τ : Tangent) : depthTerm t 0 τ 0 = 0 := by
  simp [depthTerm, psi_zero_depth]

/-- The stronger O(1/N) estimate implies the target's O(1/sqrt N) requirement. -/
theorem depthCompletionError_sqrt_bound (N : ℕ) (hN : 1 ≤ N) (t : ℝ) (ht : 0 < t)
    (τ : Tangent) : ‖depthCompletionError N t τ‖ ≤ depthCompletionConstant t/Real.sqrt (N : ℝ) := by
  have hn : 0 < N := lt_of_lt_of_le Nat.zero_lt_one hN
  have hn1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  have hs : Real.sqrt (N : ℝ) ≤ N :=
    Real.sqrt_le_iff.mpr ⟨Nat.cast_nonneg _, by nlinarith⟩
  exact (depthCompletionError_uniform_bound N hn t ht τ).trans
    (div_le_div_of_nonneg_left (depthCompletionConstant_nonneg t) (by positivity) hs)

/-- Exact full-depth expansion: phase error is added and completion error subtracted. -/
theorem amplitude_full_depth_decomposition (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) :
    amplitude N t η = (leadingScale N : ℂ) *
      (sPlus t (theta N) (tau N η)+normalPhaseError N t η-depthCompletionError N t (tau N η)+
        zeroModeDepthError N t η+nonzeroLayerAggregate N t η)+finiteProfileErrorAggregate N t η := by
  rw [amplitude_unphased_zero_decomposition N hN t η,
    depthCompletionError_eq_difference N hN t ht η]
  ring

theorem amplitude_full_depth_error (N : ℕ) (hN : 1 ≤ N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*sPlus criticalTilt (theta N) (tau N η)‖ ≤
      geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ))+dualAmplitudeConstant/(N : ℝ)^4+
        |leadingScale N| * (depthEnvelopeConstant criticalTilt*|normalFrequency η|+
          depthCompletionConstant criticalTilt/(N : ℝ)) := by
  have hn : 0 < N := lt_of_lt_of_le Nat.zero_lt_one hN
  have he : amplitude N criticalTilt η-(leadingScale N : ℂ)*sPlus criticalTilt (theta N) (tau N η) =
      (amplitude N criticalTilt η-(leadingScale N : ℂ)*unphasedZeroModeSum N criticalTilt η)-
        (leadingScale N : ℂ)*depthCompletionError N criticalTilt (tau N η) := by
    rw [depthCompletionError_eq_difference N hn criticalTilt criticalTilt_pos η]
    ring
  rw [he]
  calc
    _ ≤ ‖amplitude N criticalTilt η-(leadingScale N : ℂ)*unphasedZeroModeSum N criticalTilt η‖+
        ‖(leadingScale N : ℂ)*depthCompletionError N criticalTilt (tau N η)‖ := norm_sub_le _ _
    _ ≤ (geometricZeroErrorConstant/((N : ℝ)^3*Real.sqrt (N : ℝ))+dualAmplitudeConstant/(N : ℝ)^4+
        |leadingScale N| * (depthEnvelopeConstant criticalTilt*|normalFrequency η|))+
        |leadingScale N| * (depthCompletionConstant criticalTilt/(N : ℝ)) := by
      apply add_le_add (amplitude_unphased_zero_error N hN η hη)
      rw [norm_mul, Complex.norm_real, Real.norm_eq_abs]
      exact mul_le_mul_of_nonneg_left (critical_depthCompletionError_bound N hn (tau N η)) (abs_nonneg _)
    _ = _ := by ring

end AliceLayers
