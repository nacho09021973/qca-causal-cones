import AliceLayers.PoissonZero

noncomputable section
open scoped FourierTransform
open MeasureTheory
namespace AliceLayers

/-- The first Fourier transform of each horizontal section. -/
def psiPartial (δ : ℝ) (τ : Tangent) (u x : ℝ) : ℂ :=
  𝓕 (psiSlice δ τ x : ℝ → ℂ) u

def partialIntegrand (δ : ℝ) (τ : Tangent) (u x y : ℝ) : ℂ :=
  Complex.exp ((↑(-2 * Real.pi * y * u) : ℂ) * Complex.I) *
    psiIntegrand δ τ ![y, x]

theorem partial_integrand_continuous (δ : ℝ) (τ : Tangent) (u : ℝ) :
    Continuous (Function.uncurry (partialIntegrand δ τ u)) := by
  unfold partialIntegrand
  apply Continuous.mul
  · fun_prop
  · exact (psi_integrand_continuous δ τ).comp (by fun_prop)

theorem partial_integrand_y_vanish (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (u x y : ℝ) (hy : y ∉ Set.Icc (-(δ+1)) (δ+1)) :
    partialIntegrand δ τ u x y = 0 := by
  have hout : y < -(δ+1) ∨ δ+1 < y := by
    simp only [Set.mem_Icc, not_and_or, not_le] at hy
    exact hy
  have hs : δ ≤ y^2 := by
    rcases hout with h | h <;> nlinarith [sq_nonneg (δ + 1)]
  have hv : psiIntegrand δ τ ![y, x] = 0 := by
    apply psi_integrand_vanishes_of_sqNorm_ge
    rw [tangent_sq_sum]
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
    nlinarith [sq_nonneg x]
  simp [partialIntegrand, hv]

theorem partial_integrand_x_vanish (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (u x y : ℝ) (hx : x ∉ Set.Icc (-(δ+1)) (δ+1)) :
    partialIntegrand δ τ u x y = 0 := by
  have hout : x < -(δ+1) ∨ δ+1 < x := by
    simp only [Set.mem_Icc, not_and_or, not_le] at hx
    exact hx
  have hs : δ ≤ x^2 := by
    rcases hout with h | h <;> nlinarith [sq_nonneg (δ + 1)]
  have hv : psiIntegrand δ τ ![y, x] = 0 := by
    apply psi_integrand_vanishes_of_sqNorm_ge
    rw [tangent_sq_sum]
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
    nlinarith [sq_nonneg y]
  simp [partialIntegrand, hv]

theorem psiPartial_integral (δ : ℝ) (τ : Tangent) (u x : ℝ) :
    psiPartial δ τ u x = ∫ y, partialIntegrand δ τ u x y := by
  rw [psiPartial, Real.fourier_real_eq_integral_exp_smul]
  rfl

theorem psiPartial_continuous (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u : ℝ) :
    Continuous (psiPartial δ τ u) := by
  rw [show psiPartial δ τ u = fun x => ∫ y, partialIntegrand δ τ u x y by
    funext x; exact psiPartial_integral δ τ u x]
  apply continuousOn_univ.mp
  apply continuousOn_integral_of_compact_support (μ := volume)
    (k := Set.Icc (-(δ+1)) (δ+1)) isCompact_Icc
  · exact (partial_integrand_continuous δ τ u).continuousOn
  · intro x y hx hy
    exact partial_integrand_y_vanish δ hδ τ u x y hy

theorem psiPartial_compact (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u : ℝ) :
    HasCompactSupport (psiPartial δ τ u) := by
  apply HasCompactSupport.of_support_subset_isCompact (isCompact_Icc :
    IsCompact (Set.Icc (-(δ+1)) (δ+1)))
  apply Function.support_subset_iff'.mpr
  intro x hx
  rw [psiPartial_integral]
  have he : (fun y => partialIntegrand δ τ u x y) = 0 := by
    funext y
    exact partial_integrand_x_vanish δ hδ τ u x y hx
  rw [he]
  simp

def psiPartialMap (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (m : ℤ) : C(ℝ, ℂ) :=
  ⟨psiPartial δ τ m, psiPartial_continuous δ hδ τ m⟩

theorem psiPartial_translate_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (m : ℤ) :
    PoissonTranslateSummable (psiPartialMap δ hδ τ m) :=
  compact_poisson_translates _ (psiPartial_compact δ hδ τ m)

/-- Only finitely many integer x-sections can be nonzero. -/
theorem psiPartial_integer_support_finite (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    {n : ℤ | ∃ u : ℝ, psiPartial δ τ u n ≠ 0}.Finite := by
  apply (tendsto_cofinite_cocompact_iff.mp Int.tendsto_coe_cofinite
    (Set.Icc (-(δ+1)) (δ+1)) isCompact_Icc).subset
  intro n hn
  simp only [Set.mem_preimage, Set.mem_setOf_eq] at hn ⊢
  obtain ⟨u, hu⟩ := hn
  by_contra h
  apply hu
  rw [psiPartial_integral]
  have he : (fun y => partialIntegrand δ τ u n y) = 0 := by
    funext y
    exact partial_integrand_x_vanish δ hδ τ u n y h
  rw [he]
  simp

theorem psiPartial_cross_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (hs : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ)) :
    Summable fun p : ℤ × ℤ => psiPartial δ τ (p.2 : ℝ) (p.1 : ℝ) := by
  apply Summable.of_norm
  apply (summable_prod_of_nonneg (fun _ => norm_nonneg _)).2
  constructor
  · intro n
    exact (hs n).norm
  · apply summable_of_hasFiniteSupport
    apply (psiPartial_integer_support_finite δ hδ τ).subset
    intro n hn
    simp only [Function.mem_support, Set.mem_setOf_eq] at hn ⊢
    by_contra h
    push Not at h
    apply hn
    simp only [h, norm_zero, tsum_zero]

/-- The Ψ Poisson identity needs only the two frequency-summability hypotheses. -/
theorem psi_poisson_two_summability (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (hfirst : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ))
    (hsecond : ∀ m : ℤ, Summable fun n : ℤ =>
      𝓕 (psiPartial δ τ (m : ℝ)) (n : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, psi δ (shiftedTau τ (m : ℝ) (n : ℝ)) := by
  apply psi_poisson_identified δ hδ τ (psiPartialMap δ hδ τ)
  · intro m x
    rfl
  · exact hfirst
  · exact psiPartial_translate_summable δ hδ τ
  · exact hsecond
  · exact psiPartial_cross_summable δ hδ τ hfirst

theorem psiPartial_fourier (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u v : ℝ) :
    𝓕 (psiPartial δ τ u) v = psi δ (shiftedTau τ u v) :=
  psi_double_fourier δ hδ τ u v

/-- The remaining second condition is exactly summability of sampled Ψ values. -/
theorem psi_poisson_spectral_condition (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (hfirst : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ))
    (hspectral : ∀ m : ℤ, Summable fun n : ℤ =>
      psi δ (shiftedTau τ (m : ℝ) (n : ℝ))) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, psi δ (shiftedTau τ (m : ℝ) (n : ℝ)) := by
  apply psi_poisson_two_summability δ hδ τ hfirst
  intro m
  simpa only [psiPartial_fourier δ hδ τ] using hspectral m

end AliceLayers
