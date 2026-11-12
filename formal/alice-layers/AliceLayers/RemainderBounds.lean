import AliceLayers.FiniteProfile

noncomputable section
open MeasureTheory
open scoped BigOperators
namespace AliceLayers

/-- Integral representation valid also at the removable singularity. -/
theorem sinc_integral_cos (x : ℝ) : Real.sinc x = ∫ t in (0 : ℝ)..1, Real.cos (t*x) := by
  by_cases hx : x=0
  · simp [hx]
  rw [intervalIntegral.integral_comp_mul_right Real.cos hx, integral_cos]
  simp [Real.sinc_of_ne_zero hx, div_eq_mul_inv, mul_comm]

/-- A global Lipschitz bound; no lower bound away from zero is needed. -/
theorem sinc_lipschitz_bound (x y : ℝ) : |Real.sinc x-Real.sinc y| ≤ |x-y| := by
  rw [sinc_integral_cos, sinc_integral_cos, ← intervalIntegral.integral_sub
    ((by fun_prop : Continuous (fun t : ℝ => Real.cos (t*x))).intervalIntegrable _ _)
    ((by fun_prop : Continuous (fun t : ℝ => Real.cos (t*y))).intervalIntegrable _ _)]
  have h := intervalIntegral.norm_integral_le_of_norm_le_const
    (a := (0 : ℝ)) (b := 1) (C := |x-y|) (f := fun t => Real.cos (t*x)-Real.cos (t*y))
    (fun t ht => by
      have hti : t ∈ Set.Ioc (0 : ℝ) 1 := by simpa using ht
      have ht' : 0 ≤ t ∧ t ≤ 1 := ⟨hti.1.le,hti.2⟩
      rw [Real.norm_eq_abs]
      calc
        _ ≤ |t*x-t*y| := Real.abs_cos_sub_cos_le _ _
        _ = t*|x-y| := by rw [← mul_sub, abs_mul, abs_of_nonneg ht'.1]
        _ ≤ |x-y| := mul_le_of_le_one_left (abs_nonneg _) ht'.2)
  simpa only [Real.norm_eq_abs, sub_zero, abs_one, mul_one] using h

def resourceBound : ℝ := 4*Real.pi*|cResource|

theorem resourceBound_nonneg : 0 ≤ resourceBound := by unfold resourceBound; positivity

theorem phi0_weight_bound (k : ℝ) (hk : k ∈ Set.Icc (0 : ℝ) 1) :
    0 ≤ k^2*(1-k^2)^2 ∧ k^2*(1-k^2)^2 ≤ 1 := by
  have hk2 : 0 ≤ k^2 ∧ k^2 ≤ 1 := ⟨sq_nonneg k, by nlinarith [hk.1,hk.2]⟩
  constructor
  · positivity
  · have hh : (1-k^2)^2 ≤ 1 := by nlinarith [sq_nonneg (1-k^2)]
    exact (mul_le_mul_of_nonneg_left hh hk2.1).trans (by simpa using hk2.2)

/-- Uniform in the radial argument, with a fixed explicit constant. -/
theorem phi0_uniform_bound (ρ : ℝ) : |phi0 ρ| ≤ resourceBound := by
  have hi : ‖∫ k in (0 : ℝ)..1, k^2*(1-k^2)^2*Real.sinc (k*ρ)‖ ≤ 1 := by
    have h := intervalIntegral.norm_integral_le_of_norm_le_const
      (a := (0 : ℝ)) (b := 1) (C := (1 : ℝ))
      (f := fun k : ℝ => k^2*(1-k^2)^2*Real.sinc (k*ρ)) (fun k hk => by
        have hki : k ∈ Set.Ioc (0 : ℝ) 1 := by simpa using hk
        have hk' : k ∈ Set.Icc (0 : ℝ) 1 := ⟨hki.1.le,hki.2⟩
        have hw := phi0_weight_bound k hk'
        rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg hw.1]
        exact (mul_le_mul_of_nonneg_left (Real.abs_sinc_le_one _) hw.1).trans (by simpa using hw.2))
    simpa using h
  unfold phi0 resourceBound
  rw [abs_mul, abs_mul, abs_of_pos (by positivity : (0 : ℝ)<4*Real.pi)]
  exact mul_le_of_le_one_right (by positivity) (by simpa only [Real.norm_eq_abs] using hi)

/-- A global radial Lipschitz constant, independent of N and of the layer. -/
theorem phi0_lipschitz_bound (ρ σ : ℝ) : |phi0 ρ-phi0 σ| ≤ resourceBound*|ρ-σ| := by
  have hi : ‖∫ k in (0 : ℝ)..1,
      k^2*(1-k^2)^2*(Real.sinc (k*ρ)-Real.sinc (k*σ))‖ ≤ |ρ-σ| := by
    have h := intervalIntegral.norm_integral_le_of_norm_le_const
      (a := (0 : ℝ)) (b := 1) (C := |ρ-σ|)
      (f := fun k : ℝ => k^2*(1-k^2)^2*(Real.sinc (k*ρ)-Real.sinc (k*σ))) (fun k hk => by
        have hki : k ∈ Set.Ioc (0 : ℝ) 1 := by simpa using hk
        have hk' : k ∈ Set.Icc (0 : ℝ) 1 := ⟨hki.1.le,hki.2⟩
        have hw := phi0_weight_bound k hk'
        rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg hw.1]
        calc
          _ ≤ (k^2*(1-k^2)^2)*|k*ρ-k*σ| := mul_le_mul_of_nonneg_left (sinc_lipschitz_bound _ _) hw.1
          _ = (k^2*(1-k^2)^2)*k*|ρ-σ| := by rw [← mul_sub, abs_mul, abs_of_nonneg hk'.1]; ring
          _ ≤ |ρ-σ| := mul_le_of_le_one_left (abs_nonneg _) (by nlinarith [hw.2,hk'.2]))
    simpa using h
  unfold phi0
  rw [← mul_sub, ← intervalIntegral.integral_sub
    (phi0_kernel_intervalIntegrable ρ) (phi0_kernel_intervalIntegrable σ)]
  have he : (fun k : ℝ => k^2*(1-k^2)^2*Real.sinc (k*ρ)-k^2*(1-k^2)^2*Real.sinc (k*σ)) =
      (fun k => k^2*(1-k^2)^2*(Real.sinc (k*ρ)-Real.sinc (k*σ))) := by funext k; ring
  rw [he, abs_mul]
  have hc : |4*Real.pi*cResource| = resourceBound := by
    simp [resourceBound, abs_mul, abs_of_pos Real.pi_pos]
  rw [hc]
  exact mul_le_mul_of_nonneg_left (by simpa only [Real.norm_eq_abs] using hi) resourceBound_nonneg

/-- A global quadratic sine remainder suffices for the finite-profile error. -/
theorem sine_remainder_quadratic (z : ℝ) (hz : 0 ≤ z) : |Real.sin z-z| ≤ z^2/2 := by
  have he : (∫ t in (0 : ℝ)..z, Real.cos t-1) = Real.sin z-z := by
    rw [intervalIntegral.integral_sub (Real.continuous_cos.intervalIntegrable _ _)
      (continuous_const.intervalIntegrable _ _), integral_cos]
    simp
  rw [← he]
  calc
    _ ≤ ∫ t in (0 : ℝ)..z, |Real.cos t-1| := by
      simpa only [Real.norm_eq_abs] using
        (intervalIntegral.norm_integral_le_integral_norm (f := fun t : ℝ => Real.cos t-1) hz)
    _ ≤ ∫ t in (0 : ℝ)..z, t := by
      apply intervalIntegral.integral_mono_on hz
      · exact ((Real.continuous_cos.sub continuous_const).abs).intervalIntegrable _ _
      · exact continuous_id.intervalIntegrable _ _
      · intro t ht
        have h := Real.abs_cos_sub_cos_le t 0
        simpa [abs_of_nonneg ht.1] using h
    _ = _ := by simp

/-- Radial distance to the spherical boundary is controlled by the layer depth. -/
theorem radial_boundary_distance (N : ℕ) (hN : 0 < N) (x : Lattice) (hx : x ∈ aliceSites N) :
    |Real.sqrt (sqNorm x)/(N : ℝ)-1/4| ≤ latticeLayerDepth N x/(N : ℝ) := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hq : 0 ≤ sqNorm x := Finset.sum_nonneg (fun _ _ => sq_nonneg _)
  have hu := (support_faithfulness N x).1 hx
  have hr : Real.sqrt (sqNorm x) ≤ (N : ℝ)/4 := by
    apply (Real.sqrt_le_left (by positivity : (0 : ℝ) ≤ (N : ℝ)/4)).2
    nlinarith
  have hl : (N : ℝ)/4-latticeLayerDepth N x ≤ Real.sqrt (sqNorm x) := by
    apply Real.le_sqrt_of_sq_le
    rw [lattice_layer_decomposition]
    exact le_add_of_nonneg_right (Finset.sum_nonneg (fun _ _ => sq_nonneg _))
  have hh : Real.sqrt (sqNorm x)/(N : ℝ) ≤ (1 : ℝ)/4 := by
    apply (div_le_iff₀ hn).2
    linarith
  rw [abs_of_nonpos (sub_nonpos.mpr hh)]
  apply (le_div_iff₀ hn).2
  field_simp
  nlinarith

theorem resource_uniform_bound (N : ℕ) (x : Lattice) :
    |resource N x| ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2)*resourceBound := by
  have hr : 0 ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2) := Real.rpow_nonneg (Nat.cast_nonneg N) _
  unfold resource
  rw [abs_mul, abs_of_nonneg hr]
  exact mul_le_mul_of_nonneg_left (phi0_uniform_bound _) hr

theorem resource_boundary_error_bound (N : ℕ) (hN : 0 < N) (x : Lattice) (hx : x ∈ aliceSites N) :
    |resource N x-boundaryResourceScale N| ≤
      Real.rpow (N : ℝ) (-(3 : ℝ)/2)*resourceBound*(latticeLayerDepth N x/(N : ℝ)) := by
  have hr : 0 ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2) := Real.rpow_nonneg (Nat.cast_nonneg N) _
  unfold resource boundaryResourceScale boundaryResource
  rw [← mul_sub, abs_mul, abs_of_nonneg hr]
  calc
    _ ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2)*(resourceBound*|Real.sqrt (sqNorm x)/(N : ℝ)-1/4|) :=
      mul_le_mul_of_nonneg_left (phi0_lipschitz_bound _ _) hr
    _ ≤ _ := by
      simpa only [mul_assoc] using mul_le_mul_of_nonneg_left (radial_boundary_distance N hN x hx)
        (mul_nonneg hr resourceBound_nonneg)

def layerArgumentBound (N : ℕ) (k : ℤ) : ℝ :=
  (32*Real.pi/(N : ℝ)^2)*(indexedLayerDepth N k)^2

theorem layer_argument_bound (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ)
    (hp : p ∈ layerCoordinates N k) :
    0 ≤ profileLinearArgument N (layerPoint k p.1 p.2) ∧
      profileLinearArgument N (layerPoint k p.1 p.2) ≤ layerArgumentBound N k := by
  have hx := (layerCoordinates_membership N k p).1 hp
  have hd : 0 ≤ indexedLayerDepth N k := by
    simpa only [indexedLayerDepth_point] using ((lattice_layer_domain N hN _).1 hx).1
  have he : effectiveLayerDepth N k ≤ indexedLayerDepth N k := by
    unfold effectiveLayerDepth
    have h : 0 ≤ 2*(indexedLayerDepth N k)^2/(N : ℝ) := by positivity
    linarith
  have hq : 0 ≤ ∑ i, normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)] i ^ 2 :=
    Finset.sum_nonneg (fun _ _ => sq_nonneg _)
  have hm : max (effectiveLayerDepth N k-
      ∑ i, normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)] i ^ 2) 0 ≤ indexedLayerDepth N k :=
    max_le (by linarith) hd
  rw [finite_linear_argument N hN]
  constructor
  · unfold layerPolynomial positiveSquare
    positivity
  · unfold layerArgumentBound layerPolynomial positiveSquare
    apply mul_le_mul_of_nonneg_left _ (by positivity)
    exact (sq_le_sq₀ (le_max_right _ _) hd).2 hm

def pointwiseSineErrorBound (N : ℕ) (k : ℤ) : ℝ :=
  (layerArgumentBound N k)^2/2 * (Real.rpow (N : ℝ) (-(3 : ℝ)/2)*resourceBound)
def pointwiseRadialErrorBound (N : ℕ) (k : ℤ) : ℝ :=
  layerArgumentBound N k *
    (Real.rpow (N : ℝ) (-(3 : ℝ)/2)*resourceBound*(indexedLayerDepth N k/(N : ℝ)))

theorem sineProfileError_bound (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ)
    (hp : p ∈ layerCoordinates N k) :
    |sineProfileError N (layerPoint k p.1 p.2)| ≤ pointwiseSineErrorBound N k := by
  have hz := layer_argument_bound N hN k p hp
  unfold sineProfileError pointwiseSineErrorBound
  rw [abs_mul]
  apply mul_le_mul
  · exact (sine_remainder_quadratic _ hz.1).trans (by nlinarith [sq_le_sq₀ hz.1 (hz.1.trans hz.2) |>.2 hz.2])
  · exact resource_uniform_bound N _
  · exact abs_nonneg _
  · positivity

theorem radialResourceError_bound (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ)
    (hp : p ∈ layerCoordinates N k) :
    |radialResourceError N (layerPoint k p.1 p.2)| ≤ pointwiseRadialErrorBound N k := by
  have hz := layer_argument_bound N hN k p hp
  unfold radialResourceError pointwiseRadialErrorBound
  rw [abs_mul, abs_of_nonneg hz.1]
  apply mul_le_mul hz.2
  · simpa only [indexedLayerDepth_point] using
      resource_boundary_error_bound N hN _ ((layerCoordinates_membership N k p).1 hp)
  · exact abs_nonneg _
  · exact hz.1.trans hz.2

/-- Uniform in all tangential frequencies and all points in the finite layer. -/
theorem finiteLayerError_uniform_bound (N : ℕ) (hN : 0 < N) (k : ℤ) (τ : Tangent) :
    ‖finiteLayerError N k τ‖ ≤ (layerCoordinates N k).card *
      (pointwiseSineErrorBound N k+pointwiseRadialErrorBound N k) := by
  unfold finiteLayerError
  calc
    _ ≤ ∑ p ∈ layerCoordinates N k, ‖layerTransversePhase N k τ p *
      ((sineProfileError N (layerPoint k p.1 p.2)+radialResourceError N (layerPoint k p.1 p.2) : ℝ) : ℂ)‖ :=
      norm_sum_le _ _
    _ ≤ ∑ _p ∈ layerCoordinates N k, (pointwiseSineErrorBound N k+pointwiseRadialErrorBound N k) := by
      apply Finset.sum_le_sum
      intro p hp
      simp only [layerTransversePhase, norm_mul, Complex.norm_exp, Complex.mul_re,
        Complex.I_re, Complex.ofReal_im, mul_zero, zero_mul, Complex.I_im, sub_self,
        Real.exp_zero, one_mul, Complex.norm_real, Real.norm_eq_abs]
      exact (abs_add_le _ _).trans (add_le_add (sineProfileError_bound N hN k p hp)
        (radialResourceError_bound N hN k p hp))
    _ = _ := by simp [mul_add]

/-- A depth modulus for the squared positive part, including the moving boundary. -/
theorem positiveSquare_depth_bound (δ d q : ℝ) (hd : 0 ≤ d) (hδ : d ≤ δ) (hq : 0 ≤ q) :
    |positiveSquare (δ-q)-positiveSquare (d-q)| ≤ 2*δ*(δ-d) := by
  let A := max (δ-q) 0
  let B := max (d-q) 0
  have hA : 0 ≤ A := le_max_right _ _
  have hB : 0 ≤ B := le_max_right _ _
  have huA : A ≤ δ := max_le (by linarith) (hd.trans hδ)
  have huB : B ≤ δ := (max_le (by linarith : d-q ≤ d) hd).trans hδ
  have hdiff : |A-B| ≤ δ-d := by
    have h := abs_max_sub_max_le_abs (δ-q) (d-q) 0
    simpa only [sub_sub_sub_cancel_right, abs_of_nonneg (sub_nonneg.mpr hδ)] using h
  have hsum : |A+B| ≤ 2*δ := by rw [abs_of_nonneg (by linarith)]; linarith
  change |A^2-B^2| ≤ _
  rw [show A^2-B^2=(A-B)*(A+B) by ring, abs_mul]
  have h := mul_le_mul hdiff hsum (abs_nonneg _) (sub_nonneg.mpr hδ)
  nlinarith

theorem psiIntegrand_depth_bound (δ d : ℝ) (hd : 0 ≤ d) (hδ : d ≤ δ) (τ σ : Tangent) :
    ‖psiIntegrand δ τ σ-psiIntegrand d τ σ‖ ≤ 2*δ*(δ-d) := by
  have he : ‖Complex.exp (Complex.I * ((∑ i, τ i*σ i : ℝ) : ℂ))‖ = 1 := by
    simp [Complex.norm_exp, Complex.mul_re]
  change ‖((positiveSquare (δ-∑ i, σ i^2) : ℝ) : ℂ) * _ -
    ((positiveSquare (d-∑ i, σ i^2) : ℝ) : ℂ) * _‖ ≤ _
  rw [← sub_mul, ← Complex.ofReal_sub, norm_mul, he, mul_one, Complex.norm_real, Real.norm_eq_abs]
  exact positiveSquare_depth_bound δ d _ hd hδ (Finset.sum_nonneg (fun _ _ => sq_nonneg _))

def depthBox (δ : ℝ) : Set Tangent :=
  Set.Icc (fun _ => -(δ+1)) (fun _ => δ+1)

theorem psiIntegrand_vanish_outside_depthBox (δ d : ℝ) (hδ : 0 ≤ δ) (hd : d ≤ δ)
    (τ σ : Tangent) (hσ : σ ∉ depthBox δ) : psiIntegrand d τ σ = 0 := by
  have hout : ∃ i, σ i ∉ Set.Icc (-(δ+1)) (δ+1) := by
    by_contra h
    push Not at h
    exact hσ ⟨fun i => (h i).1, fun i => (h i).2⟩
  obtain ⟨i,hi⟩ := hout
  have hi' : σ i < -(δ+1) ∨ δ+1 < σ i := by simpa only [Set.mem_Icc, not_and_or, not_le] using hi
  have hs : δ ≤ (σ i)^2 := by rcases hi' with h | h <;> nlinarith [sq_nonneg (δ+1)]
  apply psi_integrand_vanishes_of_sqNorm_ge
  exact hd.trans (hs.trans (Finset.single_le_sum (fun j _ => sq_nonneg (σ j)) (Finset.mem_univ i)))

/-- Uniform in all Fourier frequencies: only the depth parameters enter the constant. -/
theorem psi_depth_uniform_bound (δ d : ℝ) (hd : 0 ≤ d) (hδ : d ≤ δ) (τ : Tangent) :
    ‖psi δ τ-psi d τ‖ ≤ 8*δ*(δ+1)^2*(δ-d) := by
  have hδ0 : 0 ≤ δ := hd.trans hδ
  rw [psi, psi, ← integral_sub (profile_integrability δ hδ0 τ) (profile_integrability d hd τ)]
  have he : (∫ σ in depthBox δ, psiIntegrand δ τ σ-psiIntegrand d τ σ) =
      ∫ σ, psiIntegrand δ τ σ-psiIntegrand d τ σ := by
    apply setIntegral_eq_integral_of_forall_compl_eq_zero
    intro σ hσ
    rw [psiIntegrand_vanish_outside_depthBox δ δ hδ0 le_rfl τ σ hσ,
      psiIntegrand_vanish_outside_depthBox δ d hδ0 hδ τ σ hσ, sub_self]
  rw [← he]
  have hm : (volume : Measure Tangent).real (depthBox δ) = 4*(δ+1)^2 := by
    rw [Measure.real, depthBox, Real.volume_Icc_pi_toReal (by intro i; dsimp; linarith)]
    simp
    ring
  calc
    _ ≤ (2*δ*(δ-d)) * (volume : Measure Tangent).real (depthBox δ) :=
      norm_setIntegral_le_of_norm_le_const isCompact_Icc.measure_lt_top
        (fun σ _ => psiIntegrand_depth_bound δ d hd hδ τ σ)
    _ = _ := by rw [hm]; ring

theorem psi_effective_depth_error (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) (τ : Tangent) :
    ‖psi (indexedLayerDepth N k) τ-psi (effectiveLayerDepth N k) τ‖ ≤
      16*(indexedLayerDepth N k)^3*(indexedLayerDepth N k+1)^2/(N : ℝ) := by
  have hd := effectiveLayerDepth_of_active_layer N hN k hk
  have hh : effectiveLayerDepth N k ≤ indexedLayerDepth N k := by
    unfold effectiveLayerDepth
    have h : 0 ≤ 2*(indexedLayerDepth N k)^2/(N : ℝ) := by positivity
    linarith
  have h := psi_depth_uniform_bound _ _ hd hh τ
  convert h using 1
  unfold effectiveLayerDepth
  ring

/-- Elementary count of integer points in a centered square, uniform in its center. -/
theorem integer_square_card_bound (S : Finset (ℤ × ℤ)) (c r : ℝ) (hr : 0 ≤ r)
    (hS : ∀ p ∈ S, |(p.1 : ℝ)-c| ≤ r ∧ |(p.2 : ℝ)-c| ≤ r) :
    (S.card : ℝ) ≤ 8*(r^2+1) := by
  let a : ℤ := ⌊c-r⌋
  let b : ℤ := ⌊c+r⌋
  let I : Finset ℤ := Finset.Icc a b
  have hab : a ≤ b := Int.floor_mono (by linarith)
  have hsub : S ⊆ I.product I := by
    intro p hp
    have h := hS p hp
    have h0 := abs_le.mp h.1
    have h1 := abs_le.mp h.2
    apply Finset.mem_product.mpr
    constructor
    · apply Finset.mem_Icc.mpr
      constructor
      · exact_mod_cast (Int.floor_le (c-r)).trans (by linarith : c-r ≤ (p.1 : ℝ))
      · exact Int.le_floor.mpr (by linarith)
    · apply Finset.mem_Icc.mpr
      constructor
      · exact_mod_cast (Int.floor_le (c-r)).trans (by linarith : c-r ≤ (p.2 : ℝ))
      · exact Int.le_floor.mpr (by linarith)
  have hI : (I.card : ℝ) = (b : ℝ)+1-(a : ℝ) := by
    exact_mod_cast Int.card_Icc_of_le a b (show a ≤ b+1 by omega)
  have hlen : (I.card : ℝ) ≤ 2*r+2 := by
    rw [hI]
    have ha := Int.lt_floor_add_one (c-r)
    have hb := Int.floor_le (c+r)
    dsimp [a,b] at *
    linarith
  have hcard : (S.card : ℝ) ≤ (I.card : ℝ)^2 := by
    have h := Finset.card_le_card hsub
    simp only [Finset.product_eq_sprod, Finset.card_product] at h
    exact_mod_cast (by simpa only [pow_two] using h : S.card ≤ I.card^2)
  have hsquare : (I.card : ℝ)^2 ≤ (2*r+2)^2 :=
    (sq_le_sq₀ (Nat.cast_nonneg _) (by positivity)).2 hlen
  nlinarith [sq_nonneg (r-1)]

theorem layer_centered_radius_identity (k : ℤ) (p : ℤ × ℤ) :
    (∑ i, (layerShift k + tangentMap ![(p.1 : ℝ),(p.2 : ℝ)]) i ^ 2) =
      ((p.1 : ℝ)-(k : ℝ)/3)^2 + ((p.2 : ℝ)-(k : ℝ)/3)^2 +
        (2*(k : ℝ)/3-(p.1 : ℝ)-(p.2 : ℝ))^2 := by
  have he : (layerShift k + tangentMap ![(p.1 : ℝ),(p.2 : ℝ)]) 1 =
      (-2*(k : ℝ)+3*((p.1 : ℝ)+(p.2 : ℝ)))/Real.sqrt 6 := by
    simp [layerShift,tangentMap]
    ring
  rw [Fin.sum_univ_two, he]
  norm_num [layerShift,tangentMap,div_pow,Real.sq_sqrt]
  ring

/-- Uniform layer count: tangent coordinates are centered at k/3, not at the origin. -/
theorem layerCoordinates_card_bound (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hδ : 0 ≤ indexedLayerDepth N k) :
    ((layerCoordinates N k).card : ℝ) ≤ 8*((N : ℝ)*indexedLayerDepth N k+1) := by
  let δ := indexedLayerDepth N k
  have hnδ : 0 ≤ (N : ℝ)*δ := by positivity
  have h := integer_square_card_bound (layerCoordinates N k) ((k : ℝ)/3)
    (Real.sqrt ((N : ℝ)*δ)) (Real.sqrt_nonneg _) (by
      intro p hp
      have hdom := (lattice_layer_domain N hN _).1 ((layerCoordinates_membership N k p).1 hp)
      rw [indexedLayerDepth_point] at hdom
      have hq := hdom.2.2
      simp only [latticeLayerRadiusSquared, layer_transverse_coordinates] at hq
      rw [layer_centered_radius_identity] at hq
      have ha : ((p.1 : ℝ)-(k : ℝ)/3)^2 ≤ (N : ℝ)*δ := by
        nlinarith [sq_nonneg ((p.2 : ℝ)-(k : ℝ)/3),
          sq_nonneg (2*(k : ℝ)/3-(p.1 : ℝ)-(p.2 : ℝ)), sq_nonneg δ]
      have hb : ((p.2 : ℝ)-(k : ℝ)/3)^2 ≤ (N : ℝ)*δ := by
        nlinarith [sq_nonneg ((p.1 : ℝ)-(k : ℝ)/3),
          sq_nonneg (2*(k : ℝ)/3-(p.1 : ℝ)-(p.2 : ℝ)), sq_nonneg δ]
      exact ⟨Real.abs_le_sqrt ha,Real.abs_le_sqrt hb⟩)
  simpa only [Real.sq_sqrt hnδ] using h

/-- The frequency-uniform error bound with the geometric point count substituted. -/
theorem finiteLayerError_polynomial_bound (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hδ : 0 ≤ indexedLayerDepth N k) (τ : Tangent) :
    ‖finiteLayerError N k τ‖ ≤ 8*((N : ℝ)*indexedLayerDepth N k+1)*
      (pointwiseSineErrorBound N k+pointwiseRadialErrorBound N k) := by
  apply (finiteLayerError_uniform_bound N hN k τ).trans
  apply mul_le_mul_of_nonneg_right (layerCoordinates_card_bound N hN k hδ)
  unfold pointwiseSineErrorBound pointwiseRadialErrorBound layerArgumentBound
  have hc := resourceBound_nonneg
  have hr : 0 ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2) := Real.rpow_nonneg (Nat.cast_nonneg N) _
  positivity

def finiteErrorPolynomial (δ : ℝ) : ℝ :=
  8*(δ+1)*resourceBound*((32*Real.pi)^2*δ^4/2+32*Real.pi*δ^3)

/-- Uniform in N≥1 and all frequencies, with an explicit polynomial in the layer depth.
This is an absolute N^(-7/2) bound on the sine/resource errors of one layer. -/
theorem finiteLayerError_uniform_decay (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hδ : 0 ≤ indexedLayerDepth N k) (τ : Tangent) :
    ‖finiteLayerError N k τ‖ ≤
      finiteErrorPolynomial (indexedLayerDepth N k) / ((N : ℝ)^3*Real.sqrt (N : ℝ)) := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hn1 : (1 : ℝ) ≤ N := by exact_mod_cast hN
  let δ := indexedLayerDepth N k
  have hE : 0 ≤ pointwiseSineErrorBound N k+pointwiseRadialErrorBound N k := by
    unfold pointwiseSineErrorBound pointwiseRadialErrorBound layerArgumentBound
    have hc := resourceBound_nonneg
    have hr : 0 ≤ Real.rpow (N : ℝ) (-(3 : ℝ)/2) := Real.rpow_nonneg (Nat.cast_nonneg N) _
    positivity
  have hc : ((layerCoordinates N k).card : ℝ) ≤ 8*(N : ℝ)*(δ+1) :=
    (layerCoordinates_card_bound N hN k hδ).trans (by dsimp [δ]; nlinarith)
  have h := (finiteLayerError_uniform_bound N hN k τ).trans (mul_le_mul_of_nonneg_right hc hE)
  let A := (32*Real.pi)^2*δ^4/2
  let B := 32*Real.pi*δ^3
  have hA : 0 ≤ A := by dsimp [A]; positivity
  have hdiv : A/(N : ℝ) ≤ A := div_le_self hA hn1
  have he : 8*(N : ℝ)*(δ+1)*(pointwiseSineErrorBound N k+pointwiseRadialErrorBound N k) =
      (8*(δ+1)*resourceBound)*(A/(N : ℝ)+B) / ((N : ℝ)^3*Real.sqrt (N : ℝ)) := by
    unfold pointwiseSineErrorBound pointwiseRadialErrorBound layerArgumentBound
    have hr : Real.rpow (N : ℝ) (-(3 : ℝ)/2) = 1/((N : ℝ)*Real.sqrt (N : ℝ)) :=
      rpow_neg_three_halves _ hn
    rw [hr]
    dsimp [A,B,δ]
    field_simp
  rw [he] at h
  apply h.trans
  change _ ≤ (8*(δ+1)*resourceBound)*(A+B)/_
  apply div_le_div_of_nonneg_right _ (by positivity)
  apply mul_le_mul_of_nonneg_left (add_le_add hdiv (le_refl B))
  have hc := resourceBound_nonneg
  have hd : 0 ≤ δ := hδ
  positivity

def finiteErrorConstant : ℝ := 8*resourceBound*((32*Real.pi)^2/2+32*Real.pi)

theorem finiteErrorPolynomial_bound (δ : ℝ) (hδ : 0 ≤ δ) :
    finiteErrorPolynomial δ ≤ finiteErrorConstant*(δ+1)^5 := by
  have hc := resourceBound_nonneg
  have h4 : δ^4 ≤ (δ+1)^4 := by gcongr; linarith
  have h3 : δ^3 ≤ (δ+1)^4 := by
    calc
      _ ≤ (δ+1)^3 := by gcongr; linarith
      _ ≤ _ := by nlinarith [mul_nonneg hδ (pow_nonneg (by linarith : 0 ≤ δ+1) 3)]
  unfold finiteErrorPolynomial finiteErrorConstant
  calc
    _ ≤ 8*(δ+1)*resourceBound*((32*Real.pi)^2*(δ+1)^4/2+32*Real.pi*(δ+1)^4) := by gcongr
    _ = _ := by ring

def layerNaturalIndex (N : ℕ) (k : ℤ) : ℕ := (⌊Real.sqrt 3*(N : ℝ)/4⌋-k).toNat

theorem active_layer_index_cast (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    (layerNaturalIndex N k : ℤ) = ⌊Real.sqrt 3*(N : ℝ)/4⌋-k := by
  obtain ⟨x,hx,rfl⟩ := Finset.mem_image.mp hk
  exact Int.toNat_of_nonneg (sub_nonneg.mpr (site_index_le_floor N hN x hx))

theorem active_layer_index_depth (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    indexedLayerDepth N k = (theta N+(layerNaturalIndex N k : ℝ))/Real.sqrt 3 := by
  have hc := congrArg (fun z : ℤ => (z : ℝ)) (active_layer_index_cast N hN k hk)
  push_cast at hc
  rw [hc]
  have hf := Int.fract_add_floor (Real.sqrt 3*(N : ℝ)/4)
  have hs : Real.sqrt 3 ≠ 0 := by positivity
  unfold indexedLayerDepth theta
  field_simp
  have hf' : Int.fract ((N : ℝ)*Real.sqrt 3/4) +
      (⌊(N : ℝ)*Real.sqrt 3/4⌋ : ℝ) = (N : ℝ)*Real.sqrt 3/4 := by
    simpa only [mul_comm (Real.sqrt 3) (N : ℝ)] using hf
  nlinarith [hf']

theorem active_layer_index_injective (N : ℕ) (hN : 0 < N) :
    Set.InjOn (layerNaturalIndex N) ((aliceSites N).image planeIndex : Set ℤ) := by
  intro i hi j hj hij
  have he := congrArg (fun n : ℕ => (n : ℤ)) hij
  rw [active_layer_index_cast N hN i hi, active_layer_index_cast N hN j hj] at he
  omega

theorem active_layer_depth_le_index (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    0 ≤ indexedLayerDepth N k ∧ indexedLayerDepth N k ≤ (layerNaturalIndex N k : ℝ)+1 := by
  rw [active_layer_index_depth N hN k hk]
  have ht0 : 0 ≤ theta N := Int.fract_nonneg _
  have ht1 : theta N < 1 := Int.fract_lt_one _
  have hs : (1 : ℝ) ≤ Real.sqrt 3 := by norm_num
  constructor
  · positivity
  · exact (div_le_self (by positivity) hs).trans (by linarith)

def weightedDepthEnvelope (t : ℝ) (j : ℕ) : ℝ := ((j : ℝ)+2)^5*Real.exp (-t*(j : ℝ))

theorem weightedDepthEnvelope_summable (t : ℝ) (ht : 0 < t) : Summable (weightedDepthEnvelope t) := by
  have hs := (Real.summable_pow_mul_exp_neg_nat_mul 5 ht).comp_injective
    (fun i j h => Nat.add_right_cancel h : Function.Injective (fun n : ℕ => n+2))
  have hm := hs.mul_left (Real.exp (2*t))
  have he : weightedDepthEnvelope t = fun j : ℕ => Real.exp (2*t) *
      (((j+2 : ℕ) : ℝ)^5 * Real.exp (-t*((j+2 : ℕ) : ℝ))) := by
    funext j
    simp only [weightedDepthEnvelope, Nat.cast_add, Nat.cast_ofNat]
    symm
    calc
      _ = ((j : ℝ)+2)^5*(Real.exp (2*t)*Real.exp (-t*((j : ℝ)+2))) := by ring
      _ = _ := by rw [← Real.exp_add]; congr 2 <;> ring
  rw [he]
  exact hm

def finiteErrorTiltConstant (t : ℝ) : ℝ := finiteErrorConstant * ∑' j : ℕ, weightedDepthEnvelope t j

theorem layerGlobalFactor_norm_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) (k : ℤ) (hk : k ∈ (aliceSites N).image planeIndex) :
    ‖layerGlobalFactor N t η k‖ ≤ Real.exp (-t*(layerNaturalIndex N k : ℝ)) := by
  have hphase : ‖Complex.exp (Complex.I * ((normalFrequency η*
      ((k : ℝ)/Real.sqrt 3-(N : ℝ)/4) : ℝ) : ℂ))‖ = 1 := by
    simp [Complex.norm_exp,Complex.mul_re]
  rw [layerGlobalFactor, norm_mul, hphase, one_mul, Complex.norm_real,
    Real.norm_eq_abs, abs_of_pos (Real.exp_pos _)]
  apply Real.exp_le_exp.mpr
  have hc := congrArg (fun z : ℤ => (z : ℝ)) (active_layer_index_cast N hN k hk)
  push_cast at hc
  have hf := Int.fract_add_floor (Real.sqrt 3*(N : ℝ)/4)
  have ht0 : 0 ≤ theta N := Int.fract_nonneg _
  unfold theta at ht0
  nlinarith

/-- The sum of all finite sine/resource errors is uniformly O(N^(-7/2)) for each fixed t>0. -/
theorem weighted_finiteLayerError_uniform_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) :
    ‖∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k *
      finiteLayerError N k (tau N η)‖ ≤
        finiteErrorTiltConstant t / ((N : ℝ)^3*Real.sqrt (N : ℝ)) := by
  let S := (aliceSites N).image planeIndex
  let D : ℝ := (N : ℝ)^3*Real.sqrt (N : ℝ)
  have hD : 0 < D := by dsimp [D]; positivity
  have hC : 0 ≤ finiteErrorConstant := by unfold finiteErrorConstant; have hc := resourceBound_nonneg; positivity
  have henv (j : ℕ) : 0 ≤ weightedDepthEnvelope t j := by unfold weightedDepthEnvelope; positivity
  have hpoint (k : ℤ) (hk : k ∈ S) :
      ‖layerGlobalFactor N t η k * finiteLayerError N k (tau N η)‖ ≤
        (finiteErrorConstant/D)*weightedDepthEnvelope t (layerNaturalIndex N k) := by
    have hd := active_layer_depth_le_index N hN k hk
    have hbase : indexedLayerDepth N k+1 ≤ (layerNaturalIndex N k : ℝ)+2 := by linarith [hd.2]
    have hpow : (indexedLayerDepth N k+1)^5 ≤ ((layerNaturalIndex N k : ℝ)+2)^5 :=
      pow_le_pow_left₀ (by linarith [hd.1]) hbase 5
    have hpoly := (finiteErrorPolynomial_bound _ hd.1).trans
      (mul_le_mul_of_nonneg_left hpow hC)
    rw [norm_mul]
    calc
      _ ≤ Real.exp (-t*(layerNaturalIndex N k : ℝ)) *
          (finiteErrorConstant*((layerNaturalIndex N k : ℝ)+2)^5/D) := by
        apply mul_le_mul (layerGlobalFactor_norm_bound N hN t ht η k hk)
          ((finiteLayerError_uniform_decay N hN k hd.1 (tau N η)).trans
            ((div_le_div_iff_of_pos_right hD).2 hpoly)) (norm_nonneg _) (Real.exp_nonneg _)
      _ = _ := by unfold weightedDepthEnvelope; ring
  calc
    _ ≤ ∑ k ∈ S, ‖layerGlobalFactor N t η k * finiteLayerError N k (tau N η)‖ := norm_sum_le _ _
    _ ≤ ∑ k ∈ S, (finiteErrorConstant/D)*weightedDepthEnvelope t (layerNaturalIndex N k) :=
      Finset.sum_le_sum hpoint
    _ = (finiteErrorConstant/D)*∑ k ∈ S, weightedDepthEnvelope t (layerNaturalIndex N k) := by rw [Finset.mul_sum]
    _ = (finiteErrorConstant/D)*∑ j ∈ S.image (layerNaturalIndex N), weightedDepthEnvelope t j := by
      rw [Finset.sum_image (active_layer_index_injective N hN)]
    _ ≤ (finiteErrorConstant/D)*∑' j : ℕ, weightedDepthEnvelope t j := by
      apply mul_le_mul_of_nonneg_left
        ((weightedDepthEnvelope_summable t ht).sum_le_tsum _ (fun j _ => henv j)) (div_nonneg hC hD.le)
    _ = _ := by unfold finiteErrorTiltConstant; dsimp [D]; ring

theorem alpha_bounds : (2 : ℝ)/3 < alpha ∧ alpha < 1 := by
  have hs : 0 < Real.sqrt 3 := by positivity
  have hsq : (Real.sqrt 3)^2 = 3 := Real.sq_sqrt (by norm_num)
  have hr : (3 : ℝ)/2 < Real.sqrt 3 := by nlinarith
  have hi : (1 : ℝ)/(2*Real.sqrt 3) < 1/3 := by
    apply (div_lt_iff₀ (by positivity : 0 < 2*Real.sqrt 3)).2
    linarith
  have hp : (0 : ℝ) < 1/(2*Real.sqrt 3) := by positivity
  unfold alpha
  constructor <;> linarith

theorem criticalCoshSquared_gt_one : 1 < criticalCoshSquared := by
  have ha := alpha_bounds
  have ha0 : 0 < alpha := by linarith
  have ha2 : alpha^2 < 1 := by nlinarith
  have hden : 0 < 2*(1-alpha^2) := by linarith
  have hs : 1 ≤ Real.sqrt (4-3*alpha^2) := Real.one_le_sqrt.mpr (by nlinarith)
  unfold criticalCoshSquared
  apply (one_lt_div hden).2
  nlinarith [mul_pos (by linarith : 0 < 3*alpha-2) (by linarith : 0 < alpha+1),
    mul_nonneg ha0.le (sub_nonneg.mpr hs)]

theorem criticalTilt_pos : 0 < criticalTilt := by
  unfold criticalTilt
  apply Real.log_pos
  have hs : 1 < Real.sqrt criticalCoshSquared :=
    (Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)).2 (by simpa using criticalCoshSquared_gt_one)
  linarith [Real.sqrt_nonneg (criticalCoshSquared-1)]

theorem critical_weighted_finiteLayerError_bound (N : ℕ) (hN : 0 < N) (η : Frequency) :
    ‖∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N criticalTilt η k *
      finiteLayerError N k (tau N η)‖ ≤
        finiteErrorTiltConstant criticalTilt / ((N : ℝ)^3*Real.sqrt (N : ℝ)) :=
  weighted_finiteLayerError_uniform_bound N hN criticalTilt criticalTilt_pos η

end AliceLayers
