import AliceLayers.Reindex
import Mathlib.Analysis.Fourier.PoissonSummation

noncomputable section
open scoped FourierTransform
open MeasureTheory
namespace AliceLayers

/-- Compact-wise absolute summability of all integer translates, as required by
Mathlib's one-dimensional Poisson theorem. -/
def PoissonTranslateSummable (f : C(ℝ, ℂ)) : Prop :=
  ∀ K : TopologicalSpace.Compacts ℝ,
    Summable fun n : ℤ => ‖(f.comp (ContinuousMap.addRight n)).restrict K‖

/-- Two successive one-dimensional Poisson formulas. The intermediate function
`g m` must be the first Fourier transform, pointwise. The hypothesis `hcross`
justifies exchanging the two integer sums. No identification with a two-dimensional
Fourier integral is made here. -/
theorem poisson_two_iterated
    (f : ℝ → C(ℝ, ℂ)) (g : ℤ → C(ℝ, ℂ))
    (hg : ∀ m : ℤ, ∀ x : ℝ, g m x = 𝓕 (f x : ℝ → ℂ) (m : ℝ))
    (hftrans : ∀ n : ℤ, PoissonTranslateSummable (f n))
    (hffourier : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (f n : ℝ → ℂ) (m : ℝ))
    (hgtrans : ∀ m : ℤ, PoissonTranslateSummable (g m))
    (hgfourier : ∀ m : ℤ, Summable fun n : ℤ => 𝓕 (g m : ℝ → ℂ) (n : ℝ))
    (hcross : Summable fun p : ℤ × ℤ => g p.2 (p.1 : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, f (n : ℝ) (m : ℝ)) =
      ∑' m : ℤ, ∑' n : ℤ, 𝓕 (g m : ℝ → ℂ) (n : ℝ) := by
  calc
    _ = ∑' n : ℤ, ∑' m : ℤ, g m (n : ℝ) := by
      apply tsum_congr
      intro n
      have h := Real.tsum_eq_tsum_fourier (hftrans n) (hffourier n) 0
      simpa [hg] using h
    _ = ∑' m : ℤ, ∑' n : ℤ, g m (n : ℝ) := by
      exact hcross.tsum_comm.symm
    _ = _ := by
      apply tsum_congr
      intro m
      have h := Real.tsum_eq_tsum_fourier (hgtrans m) (hgfourier m) 0
      simpa using h

/-- A one-dimensional section of the actual compactly supported Ψ integrand. -/
def psiSlice (δ : ℝ) (τ : Tangent) (x : ℝ) : C(ℝ, ℂ) where
  toFun y := psiIntegrand δ τ ![y, x]
  continuous_toFun := by
    apply (psi_integrand_continuous δ τ).comp
    fun_prop

/-- Poisson applied twice to the Ψ profile, conditional on the analytic
hypotheses for its sections and their Fourier transforms. -/
theorem psi_poisson_iterated (δ : ℝ) (τ : Tangent) (g : ℤ → C(ℝ, ℂ))
    (hg : ∀ m : ℤ, ∀ x : ℝ, g m x = 𝓕 (psiSlice δ τ x : ℝ → ℂ) (m : ℝ))
    (hftrans : ∀ n : ℤ, PoissonTranslateSummable (psiSlice δ τ n))
    (hffourier : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ))
    (hgtrans : ∀ m : ℤ, PoissonTranslateSummable (g m))
    (hgfourier : ∀ m : ℤ, Summable fun n : ℤ => 𝓕 (g m : ℝ → ℂ) (n : ℝ))
    (hcross : Summable fun p : ℤ × ℤ => g p.2 (p.1 : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, 𝓕 (g m : ℝ → ℂ) (n : ℝ) := by
  exact poisson_two_iterated (psiSlice δ τ) g hg hftrans hffourier hgtrans hgfourier hcross

/-- Every one-dimensional section has compact support for nonnegative depth. -/
theorem psiSlice_compact (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x : ℝ) :
    HasCompactSupport (psiSlice δ τ x : ℝ → ℂ) := by
  apply HasCompactSupport.of_support_subset_isCompact (isCompact_Icc :
    IsCompact (Set.Icc (-(δ+1)) (δ+1)))
  apply Function.support_subset_iff'.mpr
  intro y hy
  have hout : y < -(δ+1) ∨ δ+1 < y := by
    simp only [Set.mem_Icc, not_and_or, not_le] at hy
    exact hy
  have hs : δ ≤ y^2 := by
    rcases hout with h | h
    · nlinarith [sq_nonneg (δ + 1)]
    · nlinarith [sq_nonneg (δ + 1)]
  apply psi_integrand_vanishes_of_sqNorm_ge
  rw [tangent_sq_sum]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
  nlinarith [sq_nonneg x]

/-- Compact support discharges Mathlib's translate-summability condition. -/
theorem compact_poisson_translates (f : C(ℝ, ℂ))
    (hf : HasCompactSupport (f : ℝ → ℂ)) : PoissonTranslateSummable f := by
  have he : (f : ℝ → ℂ) =ᶠ[Filter.cocompact ℝ] 0 := by
    rw [hasCompactSupport_iff_eventuallyEq, Filter.coclosedCompact_eq_cocompact] at hf
    exact hf
  have hb : Asymptotics.IsBigO (Filter.cocompact ℝ) (f : ℝ → ℂ)
      (fun x : ℝ => |x| ^ (-(2 : ℝ))) := by
    apply Asymptotics.IsBigO.of_bound'
    filter_upwards [he] with x hx
    simpa only [hx, Pi.zero_apply, norm_zero] using
      (norm_nonneg (|x| ^ (-(2 : ℝ))))
  intro K
  exact summable_of_isBigO (Real.summable_abs_int_rpow (by norm_num : (1 : ℝ) < 2))
    ((isBigO_norm_restrict_cocompact f (by norm_num : (0 : ℝ) < 2) hb K).comp_tendsto
      Int.tendsto_coe_cofinite)

theorem psiSlice_translate_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x : ℝ) :
    PoissonTranslateSummable (psiSlice δ τ x) :=
  compact_poisson_translates _ (psiSlice_compact δ hδ τ x)

/-- Concrete Ψ formula with the first translate-summability hypothesis proved. -/
theorem psi_poisson_compact (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (g : ℤ → C(ℝ, ℂ))
    (hg : ∀ m : ℤ, ∀ x : ℝ, g m x = 𝓕 (psiSlice δ τ x : ℝ → ℂ) (m : ℝ))
    (hffourier : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ))
    (hgtrans : ∀ m : ℤ, PoissonTranslateSummable (g m))
    (hgfourier : ∀ m : ℤ, Summable fun n : ℤ => 𝓕 (g m : ℝ → ℂ) (n : ℝ))
    (hcross : Summable fun p : ℤ × ℤ => g p.2 (p.1 : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, 𝓕 (g m : ℝ → ℂ) (n : ℝ) := by
  exact psi_poisson_iterated δ τ g hg (fun n => psiSlice_translate_summable δ hδ τ n)
    hffourier hgtrans hgfourier hcross

end AliceLayers
