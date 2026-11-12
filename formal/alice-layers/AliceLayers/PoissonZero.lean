import AliceLayers.Poisson

noncomputable section
open scoped FourierTransform
open MeasureTheory
namespace AliceLayers

/-- Zero-frequency one-dimensional Fourier transform uses no 2π factor. -/
theorem fourier_zero_eq_integral (f : ℝ → ℂ) :
    𝓕 f 0 = ∫ x, f x := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  simp

/-- The product-coordinate version of the Ψ integrand is integrable. -/
theorem psi_prod_integrable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    Integrable (fun p : ℝ × ℝ => psiIntegrand δ τ ![p.1, p.2])
      ((volume : Measure ℝ).prod volume) := by
  have hp := (measurePreserving_finTwoArrow (volume : Measure ℝ)).symm MeasurableEquiv.finTwoArrow
  have hi := (hp.integrable_comp_emb MeasurableEquiv.finTwoArrow.symm.measurableEmbedding).2
    (profile_integrability δ hδ τ)
  have he (p : ℝ × ℝ) : (MeasurableEquiv.finTwoArrow.symm p : Tangent) = ![p.1, p.2] := by
    ext i
    fin_cases i <;> rfl
  have heq : (psiIntegrand δ τ ∘ MeasurableEquiv.finTwoArrow.symm) =
      (fun p : ℝ × ℝ => psiIntegrand δ τ ![p.1, p.2]) := by
    funext p
    simp only [Function.comp_apply, he]
  rw [heq] at hi
  exact hi

/-- Fubini identifies the integral of the sections with Ψ. -/
theorem psi_integral_sections (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    (∫ x : ℝ, ∫ y : ℝ, psiIntegrand δ τ ![y, x]) = psi δ τ := by
  let f : ℝ × ℝ → ℂ := fun p => psiIntegrand δ τ ![p.1, p.2]
  have hi : Integrable f ((volume : Measure ℝ).prod volume) := psi_prod_integrable δ hδ τ
  have hp := (measurePreserving_finTwoArrow (volume : Measure ℝ)).symm MeasurableEquiv.finTwoArrow
  have hm := hp.integral_comp MeasurableEquiv.finTwoArrow.symm.measurableEmbedding
    (psiIntegrand δ τ)
  calc
    _ = ∫ p : ℝ × ℝ, f p ∂((volume : Measure ℝ).prod volume) := (integral_prod_symm f hi).symm
    _ = psi δ τ := by
      have he (p : ℝ × ℝ) : (MeasurableEquiv.finTwoArrow.symm p : Tangent) = ![p.1, p.2] := by
        ext i
        fin_cases i <;> rfl
      simpa only [he, f, psi, volume_pi] using hm

/-- Zero mode of the iterated transform is exactly Ψ. -/
theorem psi_iterated_fourier_zero (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (g : C(ℝ, ℂ)) (hg : ∀ x, g x = 𝓕 (psiSlice δ τ x : ℝ → ℂ) 0) :
    𝓕 (g : ℝ → ℂ) 0 = psi δ τ := by
  rw [fourier_zero_eq_integral]
  simp_rw [hg, fourier_zero_eq_integral]
  exact psi_integral_sections δ hδ τ

/-- The iterated Fourier zero mode equals Ψ without an intermediate-function hypothesis. -/
theorem psi_double_fourier_zero (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    𝓕 (fun x : ℝ => 𝓕 (psiSlice δ τ x : ℝ → ℂ) 0) 0 = psi δ τ := by
  rw [fourier_zero_eq_integral]
  simp_rw [fourier_zero_eq_integral]
  exact psi_integral_sections δ hδ τ

/-- Fourier frequencies are measured in cycles: the Ψ phase shifts by -2πw. -/
def shiftedTau (τ : Tangent) (u v : ℝ) : Tangent :=
  ![τ 0 - 2 * Real.pi * u, τ 1 - 2 * Real.pi * v]

theorem psi_fourier_integrand (δ : ℝ) (τ : Tangent) (u v x y : ℝ) :
    Complex.exp ((↑(-2 * Real.pi * x * v) : ℂ) * Complex.I) *
      (Complex.exp ((↑(-2 * Real.pi * y * u) : ℂ) * Complex.I) *
        psiIntegrand δ τ ![y, x]) =
      psiIntegrand δ (shiftedTau τ u v) ![y, x] := by
  simp only [psiIntegrand, shiftedTau, Fin.sum_univ_two, Matrix.cons_val_zero,
    Matrix.cons_val_one]
  push_cast
  calc
    _ = (↑(max (δ - (y^2 + x^2)) 0) ^ 2 : ℂ) *
        ((Complex.exp (-2 * (Real.pi : ℂ) * x * v * Complex.I) *
          Complex.exp (-2 * (Real.pi : ℂ) * y * u * Complex.I)) *
          Complex.exp (Complex.I * ((τ 0 : ℂ) * y + (τ 1 : ℂ) * x))) := by ring
    _ = _ := by
      rw [← Complex.exp_add, ← Complex.exp_add]
      congr 2
      ring

theorem psi_double_fourier (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (u v : ℝ) :
    𝓕 (fun x : ℝ => 𝓕 (psiSlice δ τ x : ℝ → ℂ) u) v =
      psi δ (shiftedTau τ u v) := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  simp_rw [Real.fourier_real_eq_integral_exp_smul]
  simp only [smul_eq_mul, psiSlice, ContinuousMap.coe_mk]
  simp_rw [← integral_const_mul, psi_fourier_integrand]
  exact psi_integral_sections δ hδ (shiftedTau τ u v)

/-- Conditional Poisson formula with every spectral term identified as Ψ. -/
theorem psi_poisson_identified (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (g : ℤ → C(ℝ, ℂ))
    (hg : ∀ m : ℤ, ∀ x : ℝ, g m x = 𝓕 (psiSlice δ τ x : ℝ → ℂ) (m : ℝ))
    (hffourier : ∀ n : ℤ, Summable fun m : ℤ => 𝓕 (psiSlice δ τ n : ℝ → ℂ) (m : ℝ))
    (hgtrans : ∀ m : ℤ, PoissonTranslateSummable (g m))
    (hgfourier : ∀ m : ℤ, Summable fun n : ℤ => 𝓕 (g m : ℝ → ℂ) (n : ℝ))
    (hcross : Summable fun p : ℤ × ℤ => g p.2 (p.1 : ℝ)) :
    (∑' n : ℤ, ∑' m : ℤ, psiIntegrand δ τ ![(m : ℝ), (n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, psi δ (shiftedTau τ (m : ℝ) (n : ℝ)) := by
  rw [psi_poisson_compact δ hδ τ g hg hffourier hgtrans hgfourier hcross]
  apply tsum_congr
  intro m
  apply tsum_congr
  intro n
  have he : (g m : ℝ → ℂ) = fun x => 𝓕 (psiSlice δ τ x : ℝ → ℂ) (m : ℝ) := by
    funext x
    exact hg m x
  rw [he, psi_double_fourier δ hδ τ]

theorem shiftedTau_zero (τ : Tangent) : shiftedTau τ 0 0 = τ := by
  ext i
  fin_cases i <;> simp [shiftedTau]

theorem psi_double_fourier_zero_from_general (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    𝓕 (fun x : ℝ => 𝓕 (psiSlice δ τ x : ℝ → ℂ) 0) 0 = psi δ τ := by
  simpa [shiftedTau_zero] using psi_double_fourier δ hδ τ 0 0

end AliceLayers
