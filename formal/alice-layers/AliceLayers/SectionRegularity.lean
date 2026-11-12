import AliceLayers.Dual
import Mathlib.Analysis.Fourier.FourierTransformDeriv
import Mathlib.Analysis.Calculus.Deriv.Support

noncomputable section
open Filter Asymptotics MeasureTheory
open scoped Topology FourierTransform
namespace AliceLayers

/-- The squared positive part used at the disk boundary. -/
def positiveSquare (z : ℝ) : ℝ := (max z 0)^2

theorem positiveSquare_bound (z : ℝ) : ‖positiveSquare z‖ ≤ ‖z^2‖ := by
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg (sq_nonneg _), abs_of_nonneg (sq_nonneg _)]
  by_cases h : 0 ≤ z
  · rw [positiveSquare, max_eq_left h]
  · rw [positiveSquare, max_eq_right (le_of_not_ge h)]
    simpa using sq_nonneg z

theorem positiveSquare_hasDerivAt_zero : HasDerivAt positiveSquare 0 0 := by
  apply HasDerivAt.of_isLittleO
  have hb : positiveSquare =O[𝓝 0] fun z : ℝ => z^2 :=
    isBigO_of_le _ positiveSquare_bound
  have hl : positiveSquare =o[𝓝 0] fun z : ℝ => z :=
    hb.trans_isLittleO (isLittleO_pow_id (by norm_num : 1 < 2))
  simpa [positiveSquare] using! hl

theorem positiveSquare_hasDerivAt (z : ℝ) :
    HasDerivAt positiveSquare (2 * max z 0) z := by
  rcases lt_trichotomy z 0 with h | h | h
  · have he : positiveSquare =ᶠ[𝓝 z] (fun _ => 0) := by
      filter_upwards [Iio_mem_nhds h] with y hy
      have hy' : y < 0 := hy
      simp [positiveSquare, max_eq_right hy'.le]
    have hd : HasDerivAt (fun _ : ℝ => (0 : ℝ)) (2 * max z 0) z := by
      simpa [max_eq_right h.le] using (hasDerivAt_const z (0 : ℝ))
    exact hd.congr_of_eventuallyEq he
  · subst z
    simpa using positiveSquare_hasDerivAt_zero
  · have he : positiveSquare =ᶠ[𝓝 z] (fun y => y^2) := by
      filter_upwards [Ioi_mem_nhds h] with y hy
      have hy' : 0 < y := hy
      simp [positiveSquare, max_eq_left hy'.le]
    have hd : HasDerivAt (fun y : ℝ => y^2) (2 * max z 0) z := by
      have hd := (hasDerivAt_id z).pow 2
      simp only [id_eq, Nat.cast_ofNat, pow_one, one_mul] at hd
      simpa [max_eq_left h.le, mul_comm, Pi.pow_apply] using! hd
    exact hd.congr_of_eventuallyEq he

/-- Exact derivative of each real cutoff section, including its boundary. -/
theorem section_cutoff_derivative (δ x y : ℝ) :
    HasDerivAt (fun t : ℝ => positiveSquare (δ - t^2 - x^2))
      (-4*y * max (δ-y^2-x^2) 0) y := by
  have hd : HasDerivAt (fun t : ℝ => δ - t^2 - x^2) (-2*y) y := by
    convert! ((hasDerivAt_const y δ).sub ((hasDerivAt_id y).pow 2)).sub
      (hasDerivAt_const y (x^2)) using 1 <;> try (funext t) <;> try (simp [id_eq, Pi.pow_apply, Pi.sub_apply, Function.comp_def]) <;> try ring
    all_goals simp_all [id_eq] <;> ring
  convert! (positiveSquare_hasDerivAt (δ-y^2-x^2)).comp y hd using 1 <;> try (funext t) <;> try (simp [id_eq, Pi.pow_apply, Pi.sub_apply, Function.comp_def]) <;> try ring
  all_goals ring

theorem section_cutoff_derivative_continuous (δ x : ℝ) :
    Continuous (fun y : ℝ => -4*y * max (δ-y^2-x^2) 0) := by
  fun_prop

theorem section_boundary_derivative_zero (δ x y : ℝ) (h : δ = y^2 + x^2) :
    deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2)) y = 0 := by
  rw [(section_cutoff_derivative δ x y).deriv]
  simp [show δ-y^2-x^2 = 0 by linarith]

theorem positiveSquare_differentiable : Differentiable ℝ positiveSquare :=
  fun z => (positiveSquare_hasDerivAt z).differentiableAt

/-- The full complex section, including its oscillatory factor, is C¹. -/
theorem psiSlice_differentiable (δ : ℝ) (τ : Tangent) (x : ℝ) :
    Differentiable ℝ (psiSlice δ τ x : ℝ → ℂ) := by
  have hp : Differentiable ℝ (fun y : ℝ => positiveSquare (δ-y^2-x^2)) := by
    exact positiveSquare_differentiable.comp (by fun_prop)
  have hc : Differentiable ℝ (fun y : ℝ => ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ)) :=
    Complex.ofRealCLM.differentiable.comp hp
  have he : Differentiable ℝ (fun y : ℝ =>
      Complex.exp (Complex.I * ((τ 0 * y + τ 1 * x : ℝ) : ℂ))) := by
    apply Complex.differentiable_exp.comp
    apply Differentiable.const_mul
    apply Complex.ofRealCLM.differentiable.comp
    have hh : Differentiable ℝ (fun y : ℝ => τ 0 * y + τ 1*x) := by
      fun_prop
    exact hh
  convert! hc.mul he using 1
  funext y
  simp [psiSlice, psiIntegrand, positiveSquare, Fin.sum_univ_two,
    show δ - (y^2 + x^2) = δ-y^2-x^2 by ring]

theorem positiveSquare_contDiff_one : ContDiff ℝ 1 positiveSquare := by
  apply contDiff_one_iff_deriv.mpr
  refine ⟨positiveSquare_differentiable, ?_⟩
  have he : deriv positiveSquare = fun z : ℝ => 2 * max z 0 := by
    funext z
    exact (positiveSquare_hasDerivAt z).deriv
  rw [he]
  fun_prop

theorem section_cutoff_contDiff_one (δ x : ℝ) :
    ContDiff ℝ 1 (fun y : ℝ => positiveSquare (δ-y^2-x^2)) := by
  apply positiveSquare_contDiff_one.comp
  fun_prop

theorem psiSlice_contDiff_one (δ : ℝ) (τ : Tangent) (x : ℝ) :
    ContDiff ℝ 1 (psiSlice δ τ x : ℝ → ℂ) := by
  have hc : ContDiff ℝ 1 (fun y : ℝ => ((positiveSquare (δ-y^2-x^2) : ℝ) : ℂ)) :=
    Complex.ofRealCLM.contDiff.comp (section_cutoff_contDiff_one δ x)
  have hr : ContDiff ℝ 1 (fun y : ℝ => τ 0*y + τ 1*x) := by fun_prop
  have he : ContDiff ℝ 1 (fun y : ℝ =>
      Complex.exp (Complex.I * ((τ 0*y + τ 1*x : ℝ) : ℂ))) := by
    exact (contDiff_const.mul (Complex.ofRealCLM.contDiff.comp hr)).cexp
  convert! hc.mul he using 1
  funext y
  simp [psiSlice, psiIntegrand, positiveSquare, Fin.sum_univ_two,
    show δ - (y^2+x^2) = δ-y^2-x^2 by ring]

theorem psiSlice_deriv_integrable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x : ℝ) :
    MeasureTheory.Integrable (deriv (psiSlice δ τ x : ℝ → ℂ)) := by
  apply ((contDiff_one_iff_deriv.mp (psiSlice_contDiff_one δ τ x)).2).integrable_of_hasCompactSupport
  exact (psiSlice_compact δ hδ τ x).deriv

/-- One justified integration by parts in Fourier space. -/
theorem psiSlice_fourier_deriv (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ) :
    𝓕 (deriv (psiSlice δ τ x : ℝ → ℂ)) u =
      (2 * Real.pi * Complex.I * u) * 𝓕 (psiSlice δ τ x : ℝ → ℂ) u := by
  have hi : MeasureTheory.Integrable (psiSlice δ τ x : ℝ → ℂ) :=
    (psiSlice δ τ x).continuous.integrable_of_hasCompactSupport
      (psiSlice_compact δ hδ τ x)
  have hd := Real.fourier_deriv hi (psiSlice_differentiable δ τ x)
    (psiSlice_deriv_integrable δ hδ τ x)
  simpa only [smul_eq_mul] using congrFun hd u

/-- A first-order Fourier bound; it does not by itself imply summability on ℤ. -/
theorem psiSlice_first_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ) :
    ‖(2 * Real.pi * Complex.I * u) * 𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ ≤
      ∫ y : ℝ, ‖deriv (psiSlice δ τ x : ℝ → ℂ) y‖ := by
  rw [← psiSlice_fourier_deriv δ hδ τ x u, Real.fourier_real_eq_integral_exp_smul]
  calc
    _ ≤ ∫ y : ℝ, ‖Complex.exp ((↑(-2 * Real.pi * y * u) : ℂ) * Complex.I) •
        deriv (psiSlice δ τ x : ℝ → ℂ) y‖ := norm_integral_le_integral_norm _
    _ = _ := by
      apply integral_congr_ae
      filter_upwards with y
      simp [smul_eq_mul, Complex.norm_exp, Complex.mul_re]

end AliceLayers
