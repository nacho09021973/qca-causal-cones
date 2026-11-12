import AliceLayers.NormalizedRemainder

noncomputable section
open scoped BigOperators
open MeasureTheory
namespace AliceLayers

/-- Fixed witnesses: the original scalar statement holds on pi/6 for every N>=2. -/
theorem aliceLayersB_explicit_witnesses :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 2 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 →
      Summable (depthTerm criticalTilt (theta N) (tau N η)) ∧
      ∃ E : ℂ, ‖E‖ ≤ C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|) ∧
        amplitude N criticalTilt η = (leadingScale N : ℂ)*(sPlus criticalTilt (theta N) (tau N η)+E) := by
  refine ⟨normalizedTotalConstant, normalizedTotalConstant_nonneg, ?_⟩
  intro N hN η hη
  have hn : 1 ≤ N := by omega
  exact ⟨critical_depthTerm_summable N (tau N η), normalizedRemainder N η,
    normalizedRemainder_uniform_bound N hn η hη,
    normalizedRemainder_identity N (by omega) η⟩

/-- The exact proposition in Targets.lean, with no additional hypotheses. -/
theorem aliceLayersB_proved : AliceLayersB := by
  obtain ⟨C,hC,hall⟩ := aliceLayersB_explicit_witnesses
  exact ⟨Real.pi/6, by positivity, C, hC, 2, le_rfl, hall⟩

/-- Existential form exposes uniformity without exporting an implementation constant. -/
theorem phase_error_uniform_exists (t : ℝ) (ht : 0 < t) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ η : Frequency,
      ‖normalPhaseError N t η‖ ≤ C*|normalFrequency η| :=
  ⟨depthEnvelopeConstant t, depthEnvelopeConstant_nonneg t,
    fun N hN η => normalPhaseError_uniform_bound N hN t ht η⟩

theorem completion_error_uniform_exists (t : ℝ) (ht : 0 < t) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ τ : Tangent,
      ‖depthCompletionError N t τ‖ ≤ C/(N : ℝ) :=
  ⟨depthCompletionConstant t, depthCompletionConstant_nonneg t,
    fun N hN τ => depthCompletionError_uniform_bound N hN t ht τ⟩

theorem normalized_error_uniform_exists :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 1 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 → ‖normalizedRemainder N η‖ ≤
        C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|) :=
  ⟨normalizedTotalConstant, normalizedTotalConstant_nonneg,
    fun N hN η hη => normalizedRemainder_uniform_bound N hN η hη⟩

/-- Algebraic correspondence with the boundary integral printed in the frozen paper. -/
theorem boundaryResource_eq_paper_integral :
    boundaryResource = cResource*(16*Real.pi*
      ∫ k in (0 : ℝ)..1, k*(1-k^2)^2*Real.sin (k/4)) := by
  have hi : (∫ k in (0 : ℝ)..1, k^2*(1-k^2)^2*Real.sinc (k*(1/4))) =
      4*∫ k in (0 : ℝ)..1, k*(1-k^2)^2*Real.sin (k/4) := by
    rw [← intervalIntegral.integral_const_mul]
    apply intervalIntegral.integral_congr
    intro k _
    change k^2*(1-k^2)^2*Real.sinc (k*(1/4)) = 4*(k*(1-k^2)^2*Real.sin (k/4))
    by_cases hk : k=0
    · simp [hk]
    · rw [Real.sinc_of_ne_zero (mul_ne_zero hk (by norm_num : (1/4 : ℝ) ≠ 0))]
      have he : k*(1/4 : ℝ) = k/4 := by ring
      rw [he]
      field_simp
      <;> ring
  unfold boundaryResource phi0
  rw [hi]
  ring

end AliceLayers
