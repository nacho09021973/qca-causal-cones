import AliceLayers.WeakParts

noncomputable section
open MeasureTheory
open scoped FourierTransform
namespace AliceLayers

/-- Physical tangential coordinates with positive lattice spacing s. -/
def scaledTangentMap (s : ℝ) : Tangent →ₗ[ℝ] Tangent :=
  s • tangentMap.toLinearMap

theorem tangentMap_det : LinearMap.det tangentMap.toLinearMap = Real.sqrt 3 := by
  rw [← LinearMap.det_toMatrix', Matrix.det_fin_two]
  simp [LinearMap.toMatrix'_apply, tangentMap]
  have h2 : 0 < Real.sqrt 2 := by positivity
  have h6 : 0 < Real.sqrt 6 := by positivity
  have hm : Real.sqrt 2 * Real.sqrt 6 = 2 * Real.sqrt 3 := by
    rw [← Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
    norm_num
    rw [show (12 : ℝ) = 4 * 3 by norm_num, Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 4)]
    norm_num
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  field_simp
  rw [hm]
  nlinarith

theorem scaledTangentMap_det (s : ℝ) :
    LinearMap.det (scaledTangentMap s) = s^2 * Real.sqrt 3 := by
  simp [scaledTangentMap, LinearMap.det_smul, tangentMap_det]

/-- Change of Lebesgue measure in the orthonormal tangent frame, including translation. -/
theorem tangent_integral_transport (s : ℝ) (hs : 0 < s) (b : Tangent)
    (f : Tangent → ℂ) (hf : Continuous f) :
    (∫ p : Tangent, f (b + scaledTangentMap s p)) =
      ((s^2 * Real.sqrt 3)⁻¹ : ℝ) • ∫ q : Tangent, f q := by
  have hd : 0 < s^2 * Real.sqrt 3 := by positivity
  have hm := Measure.map_linearMap_addHaar_eq_smul_addHaar (volume : Measure Tangent)
    (f := scaledTangentMap s) (by rw [scaledTangentMap_det]; exact ne_of_gt hd)
  have hc : Continuous (fun q : Tangent => f (b+q)) := hf.comp (continuous_const.add continuous_id)
  rw [← integral_map_of_stronglyMeasurable (scaledTangentMap s).continuous_of_finiteDimensional.measurable
    hc.stronglyMeasurable, hm, integral_smul_measure]
  rw [integral_add_left_eq_self]
  rw [scaledTangentMap_det, ENNReal.toReal_ofReal (abs_nonneg _),
    abs_of_pos (inv_pos.mpr hd)]

/-- Dual frequency in angular units for the translated, scaled lattice. -/
def tangentShiftedFrequency (τ : Tangent) (s u v : ℝ) : Tangent :=
  fun i => τ i - (2 * Real.pi / s) * dualCoordinate u v i

/-- The positive sign is fixed by the Fourier kernel exp(-2πi w·p). -/
def tangentTranslationPhase (s : ℝ) (b : Tangent) (u v : ℝ) : ℂ :=
  Complex.exp (Complex.I * (((2 * Real.pi / s) *
    (∑ i, dualCoordinate u v i * b i) : ℝ) : ℂ))

theorem tangent_phase_transport (s : ℝ) (hs : s ≠ 0) (b τ p : Tangent) (u v : ℝ) :
    (∑ i, τ i * (b + scaledTangentMap s p) i) - 2*Real.pi*(u*p 0+v*p 1) =
      (2*Real.pi/s) * (∑ i, dualCoordinate u v i*b i) +
        ∑ i, tangentShiftedFrequency τ s u v i * (b + scaledTangentMap s p) i := by
  have he : p = ![p 0,p 1] := by ext i; fin_cases i <;> rfl
  have hp := dual_pairing u v (p 0) (p 1)
  rw [← he] at hp
  have hd : (∑ i, dualCoordinate u v i * (b i + s * tangentMap p i)) =
      (∑ i, dualCoordinate u v i*b i) + s * (u*p 0+v*p 1) := by
    simp only [mul_add, Finset.sum_add_distrib]
    simp_rw [mul_left_comm (dualCoordinate u v _) s, ← Finset.mul_sum]
    rw [hp]
    ring
  simp only [tangentShiftedFrequency, sub_mul, mul_assoc, Finset.sum_sub_distrib,
    ← Finset.mul_sum, scaledTangentMap, LinearMap.smul_apply, Pi.add_apply,
    Pi.smul_apply, smul_eq_mul]
  change (∑ i, τ i * (b i + s * tangentMap p i)) - 2*(Real.pi*(u*p 0+v*p 1)) =
    (2*Real.pi/s) * (∑ i, dualCoordinate u v i*b i) +
    ((∑ i, τ i * (b i + s * tangentMap p i)) -
    (2*Real.pi/s) * (∑ i, dualCoordinate u v i * (b i + s * tangentMap p i)))
  rw [hd]
  field_simp [hs]
  <;> ring

/-- A Fourier coefficient of the actual pullback profile in integer coordinates. -/
def tangentFourierCoefficient (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent)
    (u v : ℝ) : ℂ :=
  ∫ p : Tangent, Complex.exp (Complex.I * ((-2*Real.pi*(u*p 0+v*p 1) : ℝ) : ℂ)) *
    psiIntegrand δ τ (b + scaledTangentMap s p)

theorem tangent_fourier_integrand (δ : ℝ) (τ : Tangent) (s : ℝ) (hs : s ≠ 0)
    (b p : Tangent) (u v : ℝ) :
    Complex.exp (Complex.I * ((-2*Real.pi*(u*p 0+v*p 1) : ℝ) : ℂ)) *
      psiIntegrand δ τ (b + scaledTangentMap s p) =
    tangentTranslationPhase s b u v *
      psiIntegrand δ (tangentShiftedFrequency τ s u v) (b + scaledTangentMap s p) := by
  have hp := tangent_phase_transport s hs b τ p u v
  simp only [psiIntegrand, tangentTranslationPhase]
  have he : Complex.exp (Complex.I * ((-2*Real.pi*(u*p 0+v*p 1) : ℝ) : ℂ)) *
      Complex.exp (Complex.I * ((∑ i, τ i * (b + scaledTangentMap s p) i : ℝ) : ℂ)) =
      Complex.exp (Complex.I * (((2*Real.pi/s) * (∑ i, dualCoordinate u v i*b i) : ℝ) : ℂ)) *
        Complex.exp (Complex.I * ((∑ i, tangentShiftedFrequency τ s u v i *
          (b + scaledTangentMap s p) i : ℝ) : ℂ)) := by
    rw [← Complex.exp_add, ← Complex.exp_add]
    congr 1
    have hc := congrArg (fun t : ℝ => (t : ℂ)) hp
    push_cast at hc ⊢
    linear_combination Complex.I * hc
  calc
    _ = (((max (δ - ∑ i, (b + scaledTangentMap s p) i ^ 2) 0)^2 : ℝ) : ℂ) *
      (Complex.exp (Complex.I * ((-2*Real.pi*(u*p 0+v*p 1) : ℝ) : ℂ)) *
        Complex.exp (Complex.I * ((∑ i, τ i * (b + scaledTangentMap s p) i : ℝ) : ℂ))) := by ring
    _ = _ := by rw [he]; ring

/-- Exact transported coefficient: inverse covolume, positive translation phase,
and a reciprocal-lattice frequency shift. No Poisson claim is used here. -/
theorem tangent_fourier_coefficient (δ : ℝ) (τ : Tangent) (s : ℝ) (hs : 0 < s)
    (b : Tangent) (u v : ℝ) :
    tangentFourierCoefficient δ τ s b u v =
      tangentTranslationPhase s b u v *
        (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
          psi δ (tangentShiftedFrequency τ s u v) := by
  unfold tangentFourierCoefficient
  simp_rw [tangent_fourier_integrand δ τ s (ne_of_gt hs) b _ u v]
  rw [integral_const_mul, tangent_integral_transport s hs b _
    (psi_integrand_continuous δ (tangentShiftedFrequency τ s u v))]
  simp only [psi, Complex.real_smul, mul_assoc]

theorem tangent_translation_phase_zero_frequency (s : ℝ) (b : Tangent) :
    tangentTranslationPhase s b 0 0 = 1 := by
  simp [tangentTranslationPhase, dualCoordinate]

theorem tangent_shifted_frequency_zero (τ : Tangent) (s : ℝ) :
    tangentShiftedFrequency τ s 0 0 = τ := by
  ext i
  fin_cases i <;> simp [tangentShiftedFrequency, dualCoordinate]

/-- The zero mode is independent of the lattice translation. -/
theorem tangent_fourier_zero (δ : ℝ) (τ : Tangent) (s : ℝ) (hs : 0 < s) (b : Tangent) :
    tangentFourierCoefficient δ τ s b 0 0 =
      (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) * psi δ τ := by
  rw [tangent_fourier_coefficient δ τ s hs b 0 0,
    tangent_translation_phase_zero_frequency, tangent_shifted_frequency_zero, one_mul]

/-- Zero translation removes the phase at every frequency. -/
theorem tangent_translation_phase_zero_shift (s u v : ℝ) :
    tangentTranslationPhase s 0 u v = 1 := by
  simp [tangentTranslationPhase]

/-- The actual transported profile is integrable, separately from the integral identity. -/
theorem tangent_profile_integrable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) :
    Integrable (fun p : Tangent => psiIntegrand δ τ (b + scaledTangentMap s p)) := by
  have hd : 0 < s^2 * Real.sqrt 3 := by positivity
  have hm := Measure.map_linearMap_addHaar_eq_smul_addHaar (volume : Measure Tangent)
    (f := scaledTangentMap s) (by rw [scaledTangentMap_det]; exact ne_of_gt hd)
  have hc : Continuous (fun q : Tangent => psiIntegrand δ τ (b+q)) :=
    (psi_integrand_continuous δ τ).comp (continuous_const.add continuous_id)
  have hi : Integrable (fun q : Tangent => psiIntegrand δ τ (b+q)) :=
    (profile_integrability δ hδ τ).comp_add_left b
  have him : Integrable (fun q : Tangent => psiIntegrand δ τ (b+q))
      (Measure.map (scaledTangentMap s) volume) := by
    rw [hm]
    exact hi.smul_measure ENNReal.ofReal_ne_top
  exact (integrable_map_measure hc.aestronglyMeasurable
    (scaledTangentMap s).continuous_of_finiteDimensional.measurable.aemeasurable).1 him

/-- Modulation introduces no hidden integrability hypothesis. -/
theorem tangent_fourier_integrable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (u v : ℝ) :
    Integrable (fun p : Tangent =>
      Complex.exp (Complex.I * ((-2*Real.pi*(u*p 0+v*p 1) : ℝ) : ℂ)) *
        psiIntegrand δ τ (b + scaledTangentMap s p)) := by
  simp_rw [tangent_fourier_integrand δ τ s (ne_of_gt hs) b _ u v]
  exact (tangent_profile_integrable δ hδ (tangentShiftedFrequency τ s u v) s hs b).const_mul _

/-- The shift of the actual k-th layer has a scale-independent phase. -/
theorem tangent_layer_translation_phase (s : ℝ) (hs : s ≠ 0) (k : ℤ) (u v : ℝ) :
    tangentTranslationPhase s (s • layerShift k) u v =
      Complex.exp (Complex.I * ((-2*Real.pi*(k : ℝ)*(u+v)/3 : ℝ) : ℂ)) := by
  unfold tangentTranslationPhase
  congr 2
  have h6 : Real.sqrt 6 ≠ 0 := by positivity
  simp [Fin.sum_univ_two, dualCoordinate, layerShift]
  field_simp [hs]
  <;> ring

/-- Exact zero-mode factor at the paper's normalization q/√(2R). -/
theorem tangent_fourier_zero_scaled (δ : ℝ) (τ : Tangent) (R : ℝ) (hR : 0 < R)
    (k : ℤ) :
    tangentFourierCoefficient δ τ (Real.sqrt (2*R))⁻¹
      ((Real.sqrt (2*R))⁻¹ • layerShift k) 0 0 =
      (((2*R / Real.sqrt 3 : ℝ)) : ℂ) * psi δ τ := by
  have hr : 0 < Real.sqrt (2*R) := by positivity
  rw [tangent_fourier_zero δ τ _ (inv_pos.mpr hr)]
  congr 1
  norm_cast
  rw [inv_pow, Real.sq_sqrt (by positivity : 0 ≤ 2*R)]
  field_simp

theorem scaledTangentMap_det_covolume (s : ℝ) :
    LinearMap.det (scaledTangentMap s) = s^2 * ZLattice.covolume tangentLattice := by
  rw [scaledTangentMap_det, tangent_covolume]

theorem tangent_fourier_no_translation (δ : ℝ) (τ : Tangent) (s : ℝ) (hs : 0 < s)
    (u v : ℝ) :
    tangentFourierCoefficient δ τ s 0 u v =
      (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
        psi δ (tangentShiftedFrequency τ s u v) := by
  rw [tangent_fourier_coefficient δ τ s hs 0 u v,
    tangent_translation_phase_zero_shift, one_mul]

end AliceLayers
