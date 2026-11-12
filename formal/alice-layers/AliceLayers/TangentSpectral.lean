import AliceLayers.TangentTransport

noncomputable section
open MeasureTheory Filter
open scoped FourierTransform Topology
namespace AliceLayers

/-- An orthogonal frame aligned with the first tangential basis vector. -/
def sectionRotation (q : Tangent) : Tangent :=
  ![(q 0 + Real.sqrt 3*q 1)/2, (-Real.sqrt 3*q 0+q 1)/2]

theorem sectionRotation_norm (q : Tangent) :
    (∑ i, sectionRotation q i ^ 2) = ∑ i, q i ^ 2 := by
  have h3 : (Real.sqrt 3)^2 = 3 := Real.sq_sqrt (by norm_num)
  simp only [sectionRotation, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
  ring_nf
  rw [h3]
  ring

theorem sectionRotation_pairing (τ q : Tangent) :
    (∑ i, sectionRotation τ i * sectionRotation q i) = ∑ i, τ i*q i := by
  simp only [sectionRotation, Fin.sum_univ_two, Matrix.cons_val_zero, Matrix.cons_val_one]
  ring_nf
  rw [Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 3)]
  ring

theorem psi_integrand_rotation (δ : ℝ) (τ q : Tangent) :
    psiIntegrand δ (sectionRotation τ) (sectionRotation q) = psiIntegrand δ τ q := by
  simp only [psiIntegrand, sectionRotation_norm, sectionRotation_pairing]

theorem sectionRotation_affine (s : ℝ) (b : Tangent) (y x : ℝ) :
    sectionRotation (b + scaledTangentMap s ![y,x]) =
      ![s*Real.sqrt 2*y + (sectionRotation b 0+s*Real.sqrt 2*x/2),
        sectionRotation b 1+s*Real.sqrt 6*x/2] := by
  have h2 : (Real.sqrt 2)^2 = 2 := Real.sq_sqrt (by norm_num)
  have h3 : (Real.sqrt 3)^2 = 3 := Real.sq_sqrt (by norm_num)
  have h6 : (Real.sqrt 6)^2 = 6 := Real.sq_sqrt (by norm_num)
  have h23 : Real.sqrt 2 * Real.sqrt 3 = Real.sqrt 6 := by
    rw [← Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]; norm_num
  have hn2 : Real.sqrt 2 ≠ 0 := by positivity
  have hn6 : Real.sqrt 6 ≠ 0 := by positivity
  ext i
  fin_cases i <;> simp [sectionRotation, scaledTangentMap, tangentMap]
  all_goals rw [← h23]
  all_goals field_simp
  all_goals ring_nf
  all_goals simp [h2,h3]
  all_goals ring

/-- The full elliptical section, reduced exactly to an affine circular section. -/
theorem tangent_section_reduction (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent) (x y : ℝ) :
    psiIntegrand δ τ (b + scaledTangentMap s ![y,x]) =
      psiSlice δ (sectionRotation τ) (sectionRotation b 1+s*Real.sqrt 6*x/2)
        (s*Real.sqrt 2*y+(sectionRotation b 0+s*Real.sqrt 2*x/2)) := by
  rw [← psi_integrand_rotation δ τ, sectionRotation_affine]
  rfl

/-- Fourier norm under a real affine reparametrization; the translation has unit norm. -/
theorem fourier_affine_norm (f : ℝ → ℂ) (A : ℝ) (hA : 0 < A) (d u : ℝ) :
    ‖𝓕 (fun y : ℝ => f (A*y+d)) u‖ = A⁻¹ * ‖𝓕 f (u/A)‖ := by
  have hAn : A ≠ 0 := ne_of_gt hA
  let g : ℝ → ℂ := fun z =>
    Complex.exp (Complex.I * ((-2*Real.pi*(u/A)*z : ℝ) : ℂ)) * f z
  let c : ℂ := Complex.exp (Complex.I * ((2*Real.pi*(u/A)*d : ℝ) : ℂ))
  have hc : ‖c‖ = 1 := by simp [c, Complex.norm_exp, Complex.mul_re]
  have he (y : ℝ) :
      Complex.exp ((↑(-2*Real.pi*y*u) : ℂ)*Complex.I) * f (A*y+d) = c * g (A*y+d) := by
    dsimp [c,g]
    rw [← mul_assoc, ← Complex.exp_add]
    congr 2
    push_cast
    field_simp [hAn]
    <;> ring
  rw [Real.fourier_real_eq_integral_exp_smul]
  simp only [smul_eq_mul]
  simp_rw [he]
  rw [integral_const_mul]
  have hi : (∫ y : ℝ, g (A*y+d)) = (A⁻¹ : ℝ) • ∫ z : ℝ, g z := by
    rw [Measure.integral_comp_mul_left (fun z : ℝ => g (z+d)) A, integral_add_right_eq_self]
    rw [abs_of_pos (inv_pos.mpr hA)]
  rw [hi, norm_mul, hc, one_mul, norm_smul, Real.norm_eq_abs, abs_of_pos (inv_pos.mpr hA)]
  congr 1
  rw [Real.fourier_real_eq_integral_exp_smul]
  congr 1
  apply integral_congr_ae
  filter_upwards with z
  simp only [g, smul_eq_mul]
  congr 2
  push_cast
  ring

/-- A reusable integer p-series comparison, allowing one finite resonant exception. -/
theorem summable_of_shifted_square_bound (f : ℤ → ℂ) (K c t : ℝ) (hc : 0 < c)
    (hb : ∀ n : ℤ, ‖f n‖ * |t-c*(n : ℝ)|^2 ≤ K) : Summable f := by
  let a : ℝ := -t/c
  have hcn : c ≠ 0 := ne_of_gt hc
  have hs : Summable (fun n : ℤ => 1 / |(n : ℝ)+a|^(2 : ℝ)) :=
    (Real.summable_one_div_int_add_rpow a 2).2 (by norm_num)
  have hg : Summable (fun n : ℤ => (K/c^2)*(1/|(n : ℝ)+a|^2)) := by
    simpa only [Real.rpow_ofNat] using hs.mul_left (K/c^2)
  have hinj : Function.Injective (fun n : ℤ => (n : ℝ)+a) := by
    intro i j hij
    exact Int.cast_injective (add_right_cancel hij)
  have hf : {n : ℤ | (n : ℝ)+a=0}.Finite :=
    Set.Finite.preimage hinj.injOn (Set.finite_singleton 0)
  apply hg.of_norm_bounded_eventually
  filter_upwards [hf.compl_mem_cofinite] with n hn
  have hn' : (n : ℝ)+a ≠ 0 := by simpa using hn
  have hw : t-c*(n : ℝ) = -c*((n : ℝ)+a) := by dsimp [a]; field_simp; ring
  have hω : t-c*(n : ℝ) ≠ 0 := by rw [hw]; exact mul_ne_zero (neg_ne_zero.mpr hcn) hn'
  have hd := (le_div_iff₀ (sq_pos_of_ne_zero (abs_ne_zero.mpr hω))).2 (hb n)
  rw [hw, abs_mul, abs_neg, abs_of_pos hc, mul_pow] at hd
  simpa only [div_eq_mul_inv, mul_inv_rev, one_mul, mul_one, mul_comm, mul_left_comm, mul_assoc] using hd

/-- Section of the genuine affine pullback in integer coordinates. -/
def tangentSlice (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent) (x : ℝ) : C(ℝ,ℂ) where
  toFun y := psiIntegrand δ τ (b + scaledTangentMap s ![y,x])
  continuous_toFun := (psi_integrand_continuous δ τ).comp
    (continuous_const.add ((scaledTangentMap s).continuous_of_finiteDimensional.comp (by fun_prop)))

/-- First spectral bound, including resonance, obtained from the circular section. -/
theorem tangentSlice_second_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (x u : ℝ) :
    ‖𝓕 (tangentSlice δ τ s b x : ℝ → ℂ) u‖ *
      |s*Real.sqrt 2*sectionRotation τ 0-2*Real.pi*u|^2 ≤
        (s*Real.sqrt 2) * (16*δ*(δ+1)) := by
  let A : ℝ := s*Real.sqrt 2
  have hA : 0 < A := by dsimp [A]; positivity
  let d : ℝ := sectionRotation b 0+s*Real.sqrt 2*x/2
  let X : ℝ := sectionRotation b 1+s*Real.sqrt 6*x/2
  have he : (tangentSlice δ τ s b x : ℝ → ℂ) =
      fun y => psiSlice δ (sectionRotation τ) X (A*y+d) := by
    funext y
    exact tangent_section_reduction δ τ s b x y
  rw [he, fourier_affine_norm _ A hA d u]
  have hb := psiSlice_second_order_uniform_bound δ hδ (sectionRotation τ) X (u/A)
  have hw : A*sectionRotation τ 0-2*Real.pi*u =
      A*(sectionRotation τ 0-2*Real.pi*(u/A)) := by field_simp
  change A⁻¹ * _ * |A*sectionRotation τ 0-2*Real.pi*u|^2 ≤ A * _
  rw [hw, abs_mul, abs_of_pos hA, mul_pow]
  calc
    _ = A * (‖𝓕 (psiSlice δ (sectionRotation τ) X : ℝ → ℂ) (u/A)‖ *
      |sectionRotation τ 0-2*Real.pi*(u/A)|^2) := by field_simp
    _ ≤ _ := mul_le_mul_of_nonneg_left hb hA.le

theorem tangentSlice_spectral_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (x : ℝ) :
    Summable fun m : ℤ => 𝓕 (tangentSlice δ τ s b x : ℝ → ℂ) (m : ℝ) := by
  apply summable_of_shifted_square_bound _ ((s*Real.sqrt 2)*(16*δ*(δ+1)))
    (2*Real.pi) (s*Real.sqrt 2*sectionRotation τ 0) (by positivity)
  intro m
  exact tangentSlice_second_order_bound δ hδ τ s hs b x m

/-- Every row of the transported dual coefficients is absolutely summable. -/
theorem tangentCoefficient_spectral_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (u : ℝ) :
    Summable fun n : ℤ => tangentFourierCoefficient δ τ s b u (n : ℝ) := by
  let J : ℝ := (s^2 * Real.sqrt 3)⁻¹
  have hJ : 0 < J := by dsimp [J]; positivity
  let c : ℝ := (2*Real.pi/s)*Real.sqrt 6/6
  have hc : 0 < c := by dsimp [c]; positivity
  apply summable_of_shifted_square_bound _ (J*(32*δ*(δ+1)^2)) c (τ 1-c*u) hc
  intro n
  have hphase : ‖tangentTranslationPhase s b u (n : ℝ)‖ = 1 := by
    simp [tangentTranslationPhase, Complex.norm_exp, Complex.mul_re]
  have hfreq : tangentShiftedFrequency τ s u (n : ℝ) 1 = τ 1-c*u-c*(n : ℝ) := by
    simp [tangentShiftedFrequency, dualCoordinate, c]
    ring
  have hb := psi_second_coordinate_bound δ hδ (tangentShiftedFrequency τ s u (n : ℝ))
  rw [hfreq] at hb
  rw [tangent_fourier_coefficient δ τ s hs b u (n : ℝ), norm_mul, norm_mul,
    hphase, one_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hJ]
  change J * _ * _ ≤ _
  simpa only [mul_assoc] using mul_le_mul_of_nonneg_left hb hJ.le

/-- Fubini in the two real coordinates, with integrability as an explicit premise. -/
theorem integral_finTwo_sections (f : Tangent → ℂ) (hf : Integrable f) :
    (∫ x : ℝ, ∫ y : ℝ, f ![y,x]) = ∫ p : Tangent, f p := by
  have hp := (measurePreserving_finTwoArrow (volume : Measure ℝ)).symm MeasurableEquiv.finTwoArrow
  have hi := (hp.integrable_comp_emb MeasurableEquiv.finTwoArrow.symm.measurableEmbedding).2 hf
  have he (p : ℝ × ℝ) : (MeasurableEquiv.finTwoArrow.symm p : Tangent) = ![p.1,p.2] := by
    ext i
    fin_cases i <;> rfl
  have hm := hp.integral_comp MeasurableEquiv.finTwoArrow.symm.measurableEmbedding f
  have heq : f ∘ MeasurableEquiv.finTwoArrow.symm =
      (fun p : ℝ × ℝ => f ![p.1,p.2]) := by
    funext p
    simp only [Function.comp_apply, he]
  rw [heq] at hi
  have hi' : Integrable (fun p : ℝ × ℝ => f ![p.1,p.2])
      ((volume : Measure ℝ).prod volume) := hi
  calc
    _ = ∫ p : ℝ × ℝ, f ![p.1,p.2] ∂((volume : Measure ℝ).prod volume) :=
      (integral_prod_symm _ hi').symm
    _ = _ := by simpa only [he, volume_pi] using hm

def tangentPartial (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent) (u x : ℝ) : ℂ :=
  𝓕 (tangentSlice δ τ s b x : ℝ → ℂ) u

/-- The iterated Fourier transform is the transported coefficient, by integrable Fubini. -/
theorem tangentPartial_fourier (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (u v : ℝ) :
    𝓕 (tangentPartial δ τ s b u) v = tangentFourierCoefficient δ τ s b u v := by
  rw [Real.fourier_real_eq_integral_exp_smul]
  simp only [tangentPartial, Real.fourier_real_eq_integral_exp_smul, smul_eq_mul,
    tangentSlice, ContinuousMap.coe_mk]
  simp_rw [← integral_const_mul]
  have he (x y : ℝ) :
      Complex.exp ((↑(-2*Real.pi*x*v) : ℂ)*Complex.I) *
        (Complex.exp ((↑(-2*Real.pi*y*u) : ℂ)*Complex.I) *
          psiIntegrand δ τ (b + scaledTangentMap s ![y,x])) =
      Complex.exp (Complex.I * ((-2*Real.pi*(u*y+v*x) : ℝ) : ℂ)) *
        psiIntegrand δ τ (b + scaledTangentMap s ![y,x]) := by
    rw [← mul_assoc, ← Complex.exp_add]
    congr 2
    push_cast
    ring
  simp_rw [he]
  exact integral_finTwo_sections _ (tangent_fourier_integrable δ hδ τ s hs b u v)

/-- The precise second spectral condition required by iterated Poisson. -/
theorem tangentPartial_spectral_summable (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) (u : ℝ) :
    Summable fun n : ℤ => 𝓕 (tangentPartial δ τ s b u) (n : ℝ) := by
  simp_rw [tangentPartial_fourier δ hδ τ s hs b u]
  exact tangentCoefficient_spectral_summable δ hδ τ s hs b u

def tangentProfile (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent) (p : Tangent) : ℂ :=
  psiIntegrand δ τ (b + scaledTangentMap s p)

theorem tangentProfile_continuous (δ : ℝ) (τ : Tangent) (s : ℝ) (b : Tangent) :
    Continuous (tangentProfile δ τ s b) :=
  (psi_integrand_continuous δ τ).comp
    (continuous_const.add (scaledTangentMap s).continuous_of_finiteDimensional)

theorem tangentProfile_compact (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) : HasCompactSupport (tangentProfile δ τ s b) := by
  let e : Tangent ≃ₗ[ℝ] Tangent := tangentMap.trans (LinearEquiv.smulOfNeZero ℝ Tangent s (ne_of_gt hs))
  let H : Tangent ≃ₜ Tangent := e.toContinuousLinearEquiv.toHomeomorph |>.trans (Homeomorph.addLeft b)
  exact (psi_integrand_hasCompactSupport δ hδ τ).comp_homeomorph H

/-- Compact support supplies a common box for both coordinate projections. -/
theorem compact_finTwo_support_box (f : Tangent → ℂ) (hf : HasCompactSupport f) :
    ∃ B : ℝ, ∀ x y : ℝ,
      (y ∉ Set.Icc (-B) B ∨ x ∉ Set.Icc (-B) B) → f ![y,x] = 0 := by
  obtain ⟨B,hB⟩ := hf.isBounded.exists_norm_le
  refine ⟨B, ?_⟩
  intro x y hout
  by_contra hn
  have hp : ![y,x] ∈ tsupport f := subset_tsupport f (by simpa using hn)
  have hnorm := hB _ hp
  have h0 : |y| ≤ B := by
    simpa only [Real.norm_eq_abs, Matrix.cons_val_zero] using
      (norm_le_pi_norm (![y,x] : Tangent) 0).trans hnorm
  have h1 : |x| ≤ B := by
    simpa only [Real.norm_eq_abs, Matrix.cons_val_one, Matrix.cons_val_zero] using
      (norm_le_pi_norm (![y,x] : Tangent) 1).trans hnorm
  rcases hout with hy | hx
  · exact hy (abs_le.mp h0)
  · exact hx (abs_le.mp h1)

/-- Conditions remaining after the two spectral bounds are supplied by compactness. -/
theorem tangent_poisson (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) :
    (∑' n : ℤ, ∑' m : ℤ, tangentProfile δ τ s b ![(m : ℝ),(n : ℝ)]) =
      ∑' m : ℤ, ∑' n : ℤ, tangentFourierCoefficient δ τ s b (m : ℝ) (n : ℝ) := by
  let f := tangentProfile δ τ s b
  obtain ⟨B,hB⟩ := compact_finTwo_support_box f (tangentProfile_compact δ hδ τ s hs b)
  let P : ℝ → ℝ → ℝ → ℂ := fun u x y =>
    Complex.exp ((↑(-2*Real.pi*y*u) : ℂ)*Complex.I) * f ![y,x]
  have hPc (u : ℝ) : Continuous (Function.uncurry (P u)) := by
    apply Continuous.mul
    · fun_prop
    · exact (tangentProfile_continuous δ τ s b).comp (by fun_prop)
  have hPi (u x : ℝ) : tangentPartial δ τ s b u x = ∫ y, P u x y := by
    rw [tangentPartial, Real.fourier_real_eq_integral_exp_smul]
    rfl
  have hPy (u x y : ℝ) (hy : y ∉ Set.Icc (-B) B) : P u x y = 0 := by
    simp only [P, hB x y (Or.inl hy), mul_zero]
  have hPx (u x y : ℝ) (hx : x ∉ Set.Icc (-B) B) : P u x y = 0 := by
    simp only [P, hB x y (Or.inr hx), mul_zero]
  have hcont (u : ℝ) : Continuous (tangentPartial δ τ s b u) := by
    rw [show tangentPartial δ τ s b u = fun x => ∫ y, P u x y by funext x; exact hPi u x]
    apply continuousOn_univ.mp
    apply continuousOn_integral_of_compact_support (μ := volume)
      (k := Set.Icc (-B) B) isCompact_Icc
    · exact (hPc u).continuousOn
    · intro x y _ hy
      exact hPy u x y hy
  have hvanish (u x : ℝ) (hx : x ∉ Set.Icc (-B) B) : tangentPartial δ τ s b u x = 0 := by
    rw [hPi]
    apply integral_eq_zero_of_ae
    filter_upwards with y
    exact hPx u x y hx
  have hcompact (u : ℝ) : HasCompactSupport (tangentPartial δ τ s b u) := by
    apply HasCompactSupport.of_support_subset_isCompact (isCompact_Icc : IsCompact (Set.Icc (-B) B))
    exact Function.support_subset_iff'.mpr (fun x hx => hvanish u x hx)
  let g : ℤ → C(ℝ,ℂ) := fun m => ⟨tangentPartial δ τ s b (m : ℝ), hcont m⟩
  have hfinite : {n : ℤ | ∃ u : ℝ, tangentPartial δ τ s b u n ≠ 0}.Finite := by
    apply (tendsto_cofinite_cocompact_iff.mp Int.tendsto_coe_cofinite
      (Set.Icc (-B) B) isCompact_Icc).subset
    intro n hn
    obtain ⟨u,hu⟩ := hn
    by_contra hx
    exact hu (hvanish u n hx)
  have hcross : Summable fun p : ℤ × ℤ => g p.2 (p.1 : ℝ) := by
    apply Summable.of_norm
    apply (summable_prod_of_nonneg (fun _ => norm_nonneg _)).2
    constructor
    · intro n
      exact (tangentSlice_spectral_summable δ hδ τ s hs b n).norm
    · apply summable_of_hasFiniteSupport
      apply hfinite.subset
      intro n hn
      by_contra hx
      simp only [Set.mem_setOf_eq] at hx
      push Not at hx
      apply hn
      simp only [g, ContinuousMap.coe_mk, hx, norm_zero, tsum_zero]
  have he := poisson_two_iterated (tangentSlice δ τ s b) g (fun _ _ => rfl)
    (fun n => compact_poisson_translates _ (by
      apply HasCompactSupport.of_support_subset_isCompact (isCompact_Icc : IsCompact (Set.Icc (-B) B))
      exact Function.support_subset_iff'.mpr (fun y hy => hB n y (Or.inl hy))))
    (fun n => tangentSlice_spectral_summable δ hδ τ s hs b n)
    (fun m => compact_poisson_translates _ (hcompact m))
    (fun m => tangentPartial_spectral_summable δ hδ τ s hs b m) hcross
  simpa only [tangentSlice, tangentProfile, ContinuousMap.coe_mk, g,
    tangentPartial_fourier δ hδ τ s hs b] using he

/-- Poisson with every Jacobian, reciprocal frequency and translation phase exposed. -/
theorem tangent_poisson_identified (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (b : Tangent) :
    (∑' n : ℤ, ∑' m : ℤ, tangentProfile δ τ s b ![(m : ℝ),(n : ℝ)]) =
      (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
        ∑' m : ℤ, ∑' n : ℤ, tangentTranslationPhase s b (m : ℝ) (n : ℝ) *
          psi δ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ)) := by
  rw [tangent_poisson δ hδ τ s hs b]
  have he (m n : ℤ) : tangentFourierCoefficient δ τ s b (m : ℝ) (n : ℝ) =
      (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
        (tangentTranslationPhase s b (m : ℝ) (n : ℝ) *
          psi δ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ))) := by
    rw [tangent_fourier_coefficient δ τ s hs b]
    ring
  simp_rw [he, tsum_mul_left]

/-- The principal profile on the actual k-th layer, including its translation phase. -/
theorem tangent_layer_poisson (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent)
    (s : ℝ) (hs : 0 < s) (k : ℤ) :
    (∑' n : ℤ, ∑' m : ℤ,
      psiIntegrand δ τ (s • (layerShift k + tangentMap ![(m : ℝ),(n : ℝ)]))) =
      (((s^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
        ∑' m : ℤ, ∑' n : ℤ,
          Complex.exp (Complex.I * ((-2*Real.pi*(k : ℝ)*((m : ℝ)+(n : ℝ))/3 : ℝ) : ℂ)) *
            psi δ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ)) := by
  have h := tangent_poisson_identified δ hδ τ s hs (s • layerShift k)
  simp only [tangent_layer_translation_phase s (ne_of_gt hs), tangentProfile,
    scaledTangentMap, LinearMap.smul_apply, smul_add] at h ⊢
  exact h

/-- A separate degenerate-depth check for the full transported spatial profile. -/
theorem tangentProfile_zero_depth (τ : Tangent) (s : ℝ) (b p : Tangent) :
    tangentProfile 0 τ s b p = 0 := by
  apply psi_integrand_vanishes_of_sqNorm_ge
  exact Finset.sum_nonneg (fun i _ => sq_nonneg _)

end AliceLayers
