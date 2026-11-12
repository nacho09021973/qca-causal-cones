import AliceLayers.RemainderBounds

noncomputable section
open MeasureTheory Set Filter
open scoped FourierTransform Topology Interval
namespace AliceLayers

/-- The second-derivative integral can be restricted to the actual circular section.
The polynomial has nonzero boundary values; equality is only almost everywhere. -/
theorem cutoffSecond_integral_inner (δ x ω : ℝ) (ha : 0 < δ-x^2) :
    (∫ y : ℝ, (cutoffSecond δ x y : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) =
    ∫ y in (-Real.sqrt (δ-x^2))..Real.sqrt (δ-x^2),
      ((12*y^2-4*(δ-x^2) : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ)) := by
  let r := Real.sqrt (δ-x^2)
  have hr : 0 < r := Real.sqrt_pos.mpr ha
  have hrs : r^2 = δ-x^2 := Real.sq_sqrt ha.le
  have hs : Function.support (fun y : ℝ => (cutoffSecond δ x y : ℂ)*
      Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) ⊆ Ioc (-r) r := by
    apply Function.support_subset_iff'.mpr
    intro y hy
    have hout : y ≤ -r ∨ r < y := by simpa only [mem_Ioc, not_and_or, not_lt, not_le] using hy
    have hq : δ-y^2-x^2 ≤ 0 := by rcases hout with h | h <;> nlinarith
    simp [cutoffSecond,not_lt.mpr hq]
  rw [← intervalIntegral.integral_eq_integral_of_support_subset hs]
  apply intervalIntegral.integral_congr_ae
  have hane : ∀ᵐ y : ℝ, y ≠ r := by
    rw [ae_iff]
    simpa using (measure_singleton r : (volume : Measure ℝ) {r} = 0)
  filter_upwards [hane] with y hy
  intro hmem
  have hm : y ∈ Ioc (-r) r := by simpa only [uIoc_of_le (by linarith : -r ≤ r)] using hmem
  have hy' : y < r := lt_of_le_of_ne hm.2 hy
  have hp := mul_pos (show 0 < r-y by linarith) (show 0 < r+y by linarith [hm.1])
  have hin : 0 < δ-y^2-x^2 := by nlinarith
  simp [cutoffSecond,hin]

theorem cutoffSecond_integral_outer (δ x ω : ℝ) (hδ : 0 ≤ δ) :
    (∫ y : ℝ, (cutoffSecond δ x y : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) =
      ∫ y in (-(δ+1))..(δ+1),
        (cutoffSecond δ x y : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ)) := by
  symm
  apply intervalIntegral.integral_eq_integral_of_support_subset
  apply Function.support_subset_iff'.mpr
  intro y hy
  have hout : y ≤ -(δ+1) ∨ δ+1 < y := by
    simpa only [mem_Ioc, not_and_or, not_lt, not_le] using hy
  have hq : δ-y^2-x^2 ≤ 0 := by rcases hout with h | h <;> nlinarith [sq_nonneg δ,sq_nonneg x]
  simp [cutoffSecond,not_lt.mpr hq]

/-- Third integration by parts on the interior polynomial, retaining both boundary terms. -/
theorem polynomial_third_parts (a ω : ℝ) (ha : 0 < a) :
    (∫ y in (-Real.sqrt a)..Real.sqrt a,
      ((12*y^2-4*a : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) *
        (Complex.I*(ω : ℂ)) =
      (8*a : ℝ) * Complex.exp (Complex.I*((ω*Real.sqrt a : ℝ) : ℂ)) -
        (8*a : ℝ) * Complex.exp (Complex.I*((ω*(-Real.sqrt a) : ℝ) : ℂ)) -
          ∫ y in (-Real.sqrt a)..Real.sqrt a,
            ((24*y : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ)) := by
  let p : ℝ → ℂ := fun y => ((12*y^2-4*a : ℝ) : ℂ)
  let p' : ℝ → ℂ := fun y => ((24*y : ℝ) : ℂ)
  let v : ℝ → ℂ := fun y => Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))
  let v' : ℝ → ℂ := fun y => v y*(Complex.I*(ω : ℂ))
  have hp : Continuous p := by dsimp [p]; fun_prop
  have hp' : Continuous p' := by dsimp [p']; fun_prop
  have hv : Continuous v := by dsimp [v]; fun_prop
  have hv' : Continuous v' := hv.mul continuous_const
  have hd (y : ℝ) : HasDerivAt p (p' y) y := by
    have h : HasDerivAt (fun t : ℝ => 12*t^2-4*a) (24*y) y := by
      convert! (((hasDerivAt_id y).pow 2).const_mul 12).sub_const (4*a) using 1
      all_goals simp only [id_eq]
      all_goals ring
    exact h.ofReal_comp
  have he := integral_mul_deriv_off_countable p v p' v' (-Real.sqrt a) (Real.sqrt a)
    ∅ countable_empty hp.continuousOn hv.continuousOn (fun y _ => hd y)
    (fun y _ => oscillation_hasDerivAt ω y) (hp'.intervalIntegrable _ _) (hv'.intervalIntegrable _ _)
  have hr : (Real.sqrt a)^2=a := Real.sq_sqrt ha.le
  dsimp [p,p',v,v'] at he
  simp only [neg_sq,hr,show 12*a-4*a=8*a by ring] at he
  simpa only [← mul_assoc, intervalIntegral.integral_mul_const] using he

/-- Variation bound for the section's second derivative, including its jumps. -/
theorem polynomial_third_bound (a ω : ℝ) (ha : 0 < a) :
    ‖(∫ y in (-Real.sqrt a)..Real.sqrt a,
      ((12*y^2-4*a : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) *
        (Complex.I*(ω : ℂ))‖ ≤ 64*a := by
  have hr : 0 ≤ Real.sqrt a := Real.sqrt_nonneg _
  have hrs : (Real.sqrt a)^2=a := Real.sq_sqrt ha.le
  have hphase (y : ℝ) : ‖Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))‖=1 := by
    simp [Complex.norm_exp,Complex.mul_re]
  have hi : ‖∫ y in (-Real.sqrt a)..Real.sqrt a,
      ((24*y : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))‖ ≤ 48*a := by
    have h := intervalIntegral.norm_integral_le_of_norm_le_const
      (a := -Real.sqrt a) (b := Real.sqrt a) (C := 24*Real.sqrt a)
      (f := fun y : ℝ => ((24*y : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ)))
      (fun y hy => by
        have hm : -Real.sqrt a < y ∧ y ≤ Real.sqrt a := by
          simpa only [uIoc_of_le (by linarith : -Real.sqrt a ≤ Real.sqrt a),mem_Ioc] using hy
        rw [norm_mul,hphase, mul_one,Complex.norm_real,Real.norm_eq_abs,abs_mul,abs_of_pos (by norm_num : (0:ℝ)<24)]
        exact mul_le_mul_of_nonneg_left (abs_le.mpr ⟨hm.1.le,hm.2⟩) (by norm_num))
    have he : (24*Real.sqrt a)*|Real.sqrt a-(-Real.sqrt a)|=48*a := by
      rw [abs_of_nonneg (by linarith)]
      nlinarith [hrs]
    rwa [he] at h
  rw [polynomial_third_parts a ω ha]
  calc
    _ ≤ ‖(8*a : ℝ)*Complex.exp (Complex.I*((ω*Real.sqrt a : ℝ) : ℂ)) -
        (8*a : ℝ)*Complex.exp (Complex.I*((ω*(-Real.sqrt a) : ℝ) : ℂ))‖ +
          ‖∫ y in (-Real.sqrt a)..Real.sqrt a,
            ((24*y : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))‖ := norm_sub_le _ _
    _ ≤ (‖(8*a : ℝ)*Complex.exp (Complex.I*((ω*Real.sqrt a : ℝ) : ℂ))‖ +
        ‖(8*a : ℝ)*Complex.exp (Complex.I*((ω*(-Real.sqrt a) : ℝ) : ℂ))‖) + 48*a :=
      add_le_add (norm_sub_le _ _) hi
    _ = _ := by
      simp only [norm_mul,hphase,Complex.norm_real,Real.norm_eq_abs,
        abs_of_pos (by norm_num : (0 : ℝ)<8),abs_of_pos ha,mul_one]
      ring

/-- Uniform third-order section bound. The frequency may be zero; no division is used. -/
theorem psiSlice_third_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) (x u : ℝ) :
    ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ * |τ 0-2*Real.pi*u|^3 ≤ 64*δ := by
  by_cases ha : 0 < δ-x^2
  · let ω := τ 0-2*Real.pi*u
    let J : ℂ := ∫ y in (-Real.sqrt (δ-x^2))..Real.sqrt (δ-x^2),
      ((12*y^2-4*(δ-x^2) : ℝ) : ℂ)*Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))
    let c := Complex.exp (Complex.I*((τ 1*x : ℝ) : ℂ))
    have hc : ‖c‖=1 := by simp [c,Complex.norm_exp,Complex.mul_re]
    have he : (∫ y in (-(δ+1))..(δ+1), (cutoffSecond δ x y : ℂ)*
        Complex.exp (Complex.I*((ω*y : ℝ) : ℂ))) = J :=
      (cutoffSecond_integral_outer δ x ω hδ).symm.trans (cutoffSecond_integral_inner δ x ω ha)
    have h := psiSlice_fourier_double_parts δ hδ τ x u
    change 𝓕 (psiSlice δ τ x : ℝ → ℂ) u*(Complex.I*(ω : ℂ))^2 = c * _ at h
    rw [he] at h
    have ht := congrArg (fun z : ℂ => z*(Complex.I*(ω : ℂ))) h
    have hh : ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖*|ω|^3 = ‖J*(Complex.I*(ω : ℂ))‖ := by
      calc
        _ = ‖(𝓕 (psiSlice δ τ x : ℝ → ℂ) u*(Complex.I*(ω : ℂ))^2)*(Complex.I*(ω : ℂ))‖ := by
          simp only [norm_mul,norm_pow,Complex.norm_I,one_mul,Complex.norm_real,Real.norm_eq_abs]
          ring
        _ = ‖(c*J)*(Complex.I*(ω : ℂ))‖ := congrArg norm ht
        _ = _ := by rw [mul_assoc,norm_mul,hc,one_mul]
    change ‖𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖*|ω|^3 ≤ _
    rw [hh]
    exact (polynomial_third_bound (δ-x^2) ω ha).trans (by nlinarith [sq_nonneg x])
  · have hz : (psiSlice δ τ x : ℝ → ℂ) = 0 := by
      funext y
      apply psi_integrand_vanishes_of_sqNorm_ge
      simp only [Fin.sum_univ_two,Matrix.cons_val_zero,Matrix.cons_val_one]
      nlinarith [sq_nonneg y]
    rw [hz]
    rw [Real.fourier_real_eq_integral_exp_smul]
    simp only [Pi.zero_apply,smul_zero,integral_zero,norm_zero,zero_mul]
    positivity

/-- Integrating the section bound yields a cubic Fourier bound in the first coordinate. -/
theorem psi_third_order_first_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖*|τ 0|^3 ≤ 128*δ*(δ+1) := by
  have hab : -(δ+1) ≤ δ+1 := by linarith
  have hc := psiPartial_continuous δ hδ τ 0
  have he : psi δ τ = ∫ x in (-(δ+1))..(δ+1), psiPartial δ τ 0 x := by
    rw [← psi_double_fourier_zero δ hδ τ,fourier_zero_eq_integral]
    exact psiPartial_integral_interval δ hδ τ 0
  rw [he]
  calc
    _ ≤ (∫ x in (-(δ+1))..(δ+1), ‖psiPartial δ τ 0 x‖)*|τ 0|^3 :=
      mul_le_mul_of_nonneg_right (intervalIntegral.norm_integral_le_integral_norm hab) (by positivity)
    _ = ∫ x in (-(δ+1))..(δ+1), ‖psiPartial δ τ 0 x‖*|τ 0|^3 :=
      (intervalIntegral.integral_mul_const _ _).symm
    _ ≤ ∫ _x in (-(δ+1))..(δ+1), 64*δ := by
      apply intervalIntegral.integral_mono_on hab
      · exact (hc.norm.mul continuous_const).intervalIntegrable _ _
      · exact intervalIntegrable_const
      · intro x _
        simpa only [psiPartial,mul_zero,sub_zero] using psiSlice_third_order_bound δ hδ τ x 0
    _ = _ := by simp; ring

theorem psi_third_order_second_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖*|τ 1|^3 ≤ 128*δ*(δ+1) := by
  have h := psi_third_order_first_bound δ hδ ![τ 1,τ 0]
  rw [psi_swap_coordinates δ hδ τ] at h
  exact h

def tangentL1 (τ : Tangent) : ℝ := |τ 0|+|τ 1|

/-- Cubic two-dimensional decay, in the l¹ norm of angular frequency. -/
theorem psi_third_order_bound (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    ‖psi δ τ‖*(tangentL1 τ)^3 ≤ 1024*δ*(δ+1) := by
  have h0 := psi_third_order_first_bound δ hδ τ
  have h1 := psi_third_order_second_bound δ hδ τ
  have hpoly : (|τ 0|+|τ 1|)^3 ≤ 4*(|τ 0|^3+|τ 1|^3) := by
    nlinarith [mul_nonneg (sq_nonneg (|τ 0|-|τ 1|)) (add_nonneg (abs_nonneg (τ 0)) (abs_nonneg (τ 1)))]
  have hm := mul_le_mul_of_nonneg_left hpoly (norm_nonneg (psi δ τ))
  unfold tangentL1
  nlinarith

theorem dual_reconstruction (m n : ℝ) :
    m = dualCoordinate m n 0/Real.sqrt 2+3*dualCoordinate m n 1/Real.sqrt 6 ∧
    n = -dualCoordinate m n 0/Real.sqrt 2+3*dualCoordinate m n 1/Real.sqrt 6 := by
  have h2 : Real.sqrt 2 ≠ 0 := by positivity
  have h6 : Real.sqrt 6 ≠ 0 := by positivity
  constructor <;> simp [dualCoordinate] <;> field_simp <;> ring

/-- A uniform equivalence bound for reciprocal-lattice coordinates. -/
theorem dual_l1_lower (m n : ℝ) : |m|+|n| ≤ 3*tangentL1 (dualCoordinate m n) := by
  have h2 : 0 < Real.sqrt 2 := by positivity
  have h6 : 0 < Real.sqrt 6 := by positivity
  have hr2 : 1 ≤ Real.sqrt 2 := by norm_num
  have hr6 : 2 ≤ Real.sqrt 6 := (Real.le_sqrt (by norm_num) (by norm_num)).2 (by norm_num)
  have hc2 : (1 : ℝ)/Real.sqrt 2 ≤ 3/2 := (div_le_iff₀ h2).2 (by linarith)
  have hc6 : (3 : ℝ)/Real.sqrt 6 ≤ 3/2 := (div_le_iff₀ h6).2 (by linarith)
  let d := dualCoordinate m n
  have hm : |m| ≤ |d 0|/Real.sqrt 2+3*|d 1|/Real.sqrt 6 := by
    rw [(dual_reconstruction m n).1]
    have h := abs_add_le (d 0/Real.sqrt 2) (3*d 1/Real.sqrt 6)
    simpa only [abs_div,abs_mul,abs_of_pos h2,abs_of_pos h6,abs_of_pos (by norm_num : (0:ℝ)<3)] using h
  have hn : |n| ≤ |d 0|/Real.sqrt 2+3*|d 1|/Real.sqrt 6 := by
    rw [(dual_reconstruction m n).2]
    have h := abs_add_le (-d 0/Real.sqrt 2) (3*d 1/Real.sqrt 6)
    simpa only [abs_div,abs_neg,abs_mul,abs_of_pos h2,abs_of_pos h6,abs_of_pos (by norm_num : (0:ℝ)<3)] using h
  calc
    _ ≤ 2*(|d 0|/Real.sqrt 2+3*|d 1|/Real.sqrt 6) := by linarith
    _ = 2*((1/Real.sqrt 2)*|d 0|+(3/Real.sqrt 6)*|d 1|) := by ring
    _ ≤ 2*((3/2)*|d 0|+(3/2)*|d 1|) := by gcongr
    _ = _ := by unfold tangentL1; dsimp [d]; ring

theorem integer_pair_l1_ge_one (m n : ℤ) (hp : (m,n) ≠ (0,0)) :
    (1 : ℝ) ≤ |(m : ℝ)|+|(n : ℝ)| := by
  have hi : (1 : ℤ) ≤ |m|+|n| := by
    have hm : 0 ≤ |m| := abs_nonneg _
    have hn : 0 ≤ |n| := abs_nonneg _
    by_contra h
    have hz : |m|=0 ∧ |n|=0 := by omega
    exact hp (Prod.ext (abs_eq_zero.mp hz.1) (abs_eq_zero.mp hz.2))
  exact_mod_cast hi

/-- Nonzero reciprocal modes remain separated from the small-frequency ball. -/
theorem dual_shift_separation (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (m n : ℤ) (hp : (m,n) ≠ (0,0)) :
    (Real.pi/(3*s))*(|(m : ℝ)|+|(n : ℝ)|) ≤
      tangentL1 (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ)) := by
  let c : ℝ := 2*Real.pi/s
  have hc : 0 < c := by dsimp [c]; positivity
  have h0 := abs_sub_le (c*dualCoordinate (m : ℝ) (n : ℝ) 0) (τ 0) 0
  have h1 := abs_sub_le (c*dualCoordinate (m : ℝ) (n : ℝ) 1) (τ 1) 0
  simp only [sub_zero,abs_mul,abs_of_pos hc] at h0 h1
  rw [abs_sub_comm (c*dualCoordinate (m : ℝ) (n : ℝ) 0) (τ 0)] at h0
  rw [abs_sub_comm (c*dualCoordinate (m : ℝ) (n : ℝ) 1) (τ 1)] at h1
  have hd := dual_l1_lower (m : ℝ) (n : ℝ)
  have hr := integer_pair_l1_ge_one m n hp
  have hsmall : tangentL1 τ ≤ c/6 := by convert hτ using 1 <;> dsimp [c] <;> ring
  have htri : c*tangentL1 (dualCoordinate (m : ℝ) (n : ℝ)) ≤
      tangentL1 τ+tangentL1 (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ)) := by
    unfold tangentL1 tangentShiftedFrequency
    dsimp [c] at *
    linarith
  have hmul := mul_le_mul_of_nonneg_left hd hc.le
  have hmulr := mul_le_mul_of_nonneg_left hr hc.le
  have he : Real.pi/(3*s)=c/6 := by dsimp [c]; ring
  rw [he]
  nlinarith

/-- Pointwise summable-order majorant for every nonzero dual mode. -/
theorem psi_nonzero_dual_bound (δ : ℝ) (hδ : 0 ≤ δ) (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (m n : ℤ) (hp : (m,n) ≠ (0,0)) :
    ‖psi δ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ))‖ ≤
      (27648*δ*(δ+1)*s^3/Real.pi^3) *
        (1/(|(m : ℝ)|+|(n : ℝ)|)^3) := by
  let r : ℝ := |(m : ℝ)|+|(n : ℝ)|
  have hr : 0 < r := lt_of_lt_of_le (by norm_num) (integer_pair_l1_ge_one m n hp)
  have hsep := dual_shift_separation s hs τ hτ m n hp
  have hbase : 0 < (Real.pi/(3*s))*r := by positivity
  have hb := psi_third_order_bound δ hδ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ))
  have hpow := pow_le_pow_left₀ hbase.le hsep 3
  have hm := (mul_le_mul_of_nonneg_left hpow (norm_nonneg _)).trans hb
  have hdiv := (le_div_iff₀ (pow_pos hbase 3)).2 hm
  calc
    _ ≤ 1024*δ*(δ+1)/((Real.pi/(3*s))*r)^3 := hdiv
    _ = _ := by dsimp [r]; field_simp <;> ring

def integerL1CubicKernel (p : ℤ × ℤ) : ℝ := 1/(|(p.1 : ℝ)|+|(p.2 : ℝ)|)^3
def standardIntegerLattice : Submodule ℤ Tangent :=
  Submodule.span ℤ (Set.range (Pi.basisFun ℝ (Fin 2)))

theorem integerPair_mem_standard (p : ℤ × ℤ) :
    (![(p.1 : ℝ),(p.2 : ℝ)] : Tangent) ∈ standardIntegerLattice := by
  change _ ∈ Submodule.span ℤ (Set.range (Pi.basisFun ℝ (Fin 2)))
  rw [(Pi.basisFun ℝ (Fin 2)).mem_span_iff_repr_mem ℤ]
  intro i
  fin_cases i
  · exact ⟨p.1,rfl⟩
  · exact ⟨p.2,rfl⟩

def integerPairInLattice (p : ℤ × ℤ) : standardIntegerLattice :=
  ⟨![(p.1 : ℝ),(p.2 : ℝ)],integerPair_mem_standard p⟩

theorem integerPairInLattice_injective : Function.Injective integerPairInLattice := by
  intro p q h
  have he := congrArg (fun z : standardIntegerLattice => (z : Tangent)) h
  apply Prod.ext
  · exact Int.cast_injective (congrArg (fun z : Tangent => z 0) he)
  · exact Int.cast_injective (congrArg (fun z : Tangent => z 1) he)

/-- Cubic inverse frequency is absolutely summable on the two-dimensional integer lattice. -/
theorem integerL1CubicKernel_summable : Summable integerL1CubicKernel := by
  letI : DiscreteTopology standardIntegerLattice := ZSpan.discreteTopology_pi_basisFun
  letI : IsZLattice ℝ standardIntegerLattice := by
    change IsZLattice ℝ (Submodule.span ℤ (Set.range (Pi.basisFun ℝ (Fin 2))))
    infer_instance
  have hrank : Module.finrank ℤ standardIntegerLattice = 2 := by
    rw [ZLattice.rank ℝ standardIntegerLattice]
    simp
  have hs := ZLattice.summable_norm_rpow standardIntegerLattice (-3 : ℝ)
    (by rw [hrank]; norm_num)
  have hm := hs.comp_injective integerPairInLattice_injective
  apply hm.of_norm_bounded_eventually
  filter_upwards [(Set.finite_singleton ((0,0) : ℤ × ℤ)).compl_mem_cofinite] with p hp
  have hp' : p ≠ (0,0) := by simpa using hp
  let v : Tangent := ![(p.1 : ℝ),(p.2 : ℝ)]
  have hv : v ≠ 0 := by
    intro h
    have h0 := congrArg (fun z : Tangent => z 0) h
    have h1 := congrArg (fun z : Tangent => z 1) h
    have hz0 : p.1=0 := by simpa only [v,Matrix.cons_val_zero,Pi.zero_apply,Int.cast_eq_zero] using h0
    have hz1 : p.2=0 := by simpa only [v,Matrix.cons_val_one,Matrix.cons_val_zero,Pi.zero_apply,Int.cast_eq_zero] using h1
    exact hp' (Prod.ext hz0 hz1)
  have hn : 0 < ‖v‖ := norm_pos_iff.mpr hv
  have hle : ‖v‖ ≤ |(p.1 : ℝ)|+|(p.2 : ℝ)| := by
    apply (pi_norm_le_iff_of_nonneg (by positivity)).2
    intro i
    fin_cases i <;> simp [v,Real.norm_eq_abs]
  change ‖integerL1CubicKernel p‖ ≤ ‖v‖^(-3 : ℝ)
  have he : ‖v‖^(-3 : ℝ) = 1/‖v‖^3 := by
    rw [Real.rpow_neg (norm_nonneg _)]
    simp only [Real.rpow_ofNat,one_div]
  rw [he,Real.norm_eq_abs,abs_of_nonneg (by unfold integerL1CubicKernel; positivity)]
  exact one_div_le_one_div_of_le (pow_pos hn 3) (pow_le_pow_left₀ hn.le hle 3)

def dualCubicConstant : ℝ := ∑' p : ℤ × ℤ, integerL1CubicKernel p
def nonzeroDualTerm (δ : ℝ) (τ : Tangent) (s : ℝ) (k : ℤ) (p : ℤ × ℤ) : ℂ :=
  if p=(0,0) then 0 else
    Complex.exp (Complex.I*((-2*Real.pi*(k : ℝ)*((p.1 : ℝ)+(p.2 : ℝ))/3 : ℝ) : ℂ)) *
      psi δ (tangentShiftedFrequency τ s (p.1 : ℝ) (p.2 : ℝ))
def nonzeroDualSum (δ : ℝ) (τ : Tangent) (s : ℝ) (k : ℤ) : ℂ :=
  ∑' p : ℤ × ℤ, nonzeroDualTerm δ τ s k p

theorem nonzeroDualTerm_bound (δ : ℝ) (hδ : 0 ≤ δ) (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (k : ℤ) (p : ℤ × ℤ) :
    ‖nonzeroDualTerm δ τ s k p‖ ≤
      (27648*δ*(δ+1)*s^3/Real.pi^3)*integerL1CubicKernel p := by
  unfold nonzeroDualTerm
  split_ifs with hp
  · simp only [norm_zero]
    unfold integerL1CubicKernel
    positivity
  · have hphase : ‖Complex.exp (Complex.I*((-2*Real.pi*(k : ℝ)*((p.1 : ℝ)+(p.2 : ℝ))/3 : ℝ) : ℂ))‖=1 := by
      simp [Complex.norm_exp,Complex.mul_re]
    rw [norm_mul,hphase,one_mul]
    exact psi_nonzero_dual_bound δ hδ s hs τ hτ p.1 p.2 hp

theorem nonzeroDualTerm_summable (δ : ℝ) (hδ : 0 ≤ δ) (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (k : ℤ) : Summable (nonzeroDualTerm δ τ s k) := by
  apply (integerL1CubicKernel_summable.mul_left (27648*δ*(δ+1)*s^3/Real.pi^3)).of_norm_bounded
  intro p
  exact nonzeroDualTerm_bound δ hδ s hs τ hτ k p

/-- The complete nonzero dual sum has a uniform O(s³) bound, not merely a bound per mode. -/
theorem nonzeroDualSum_bound (δ : ℝ) (hδ : 0 ≤ δ) (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (k : ℤ) :
    ‖nonzeroDualSum δ τ s k‖ ≤
      (27648*δ*(δ+1)*s^3/Real.pi^3)*dualCubicConstant := by
  have ht := nonzeroDualTerm_summable δ hδ s hs τ hτ k
  have hm := integerL1CubicKernel_summable.mul_left (27648*δ*(δ+1)*s^3/Real.pi^3)
  unfold nonzeroDualSum
  calc
    _ ≤ ∑' p : ℤ × ℤ, ‖nonzeroDualTerm δ τ s k p‖ := norm_tsum_le_tsum_norm ht.norm
    _ ≤ ∑' p : ℤ × ℤ, (27648*δ*(δ+1)*s^3/Real.pi^3)*integerL1CubicKernel p :=
      ht.norm.tsum_le_tsum (nonzeroDualTerm_bound δ hδ s hs τ hτ k) hm
    _ = _ := by rw [tsum_mul_left]; rfl

theorem transverse_l1_bound (η : Frequency) : tangentL1 (transverseCoordinates η) ≤ 2*frequencyNorm η := by
  have hf := frame_norm_identity η
  rw [Fin.sum_univ_two] at hf
  have h0 : |transverseCoordinates η 0| ≤ frequencyNorm η := by
    apply Real.abs_le_sqrt
    nlinarith [sq_nonneg (normalFrequency η),sq_nonneg (transverseCoordinates η 1)]
  have h1 : |transverseCoordinates η 1| ≤ frequencyNorm η := by
    apply Real.abs_le_sqrt
    nlinarith [sq_nonneg (normalFrequency η),sq_nonneg (transverseCoordinates η 0)]
  unfold tangentL1
  linarith

theorem tau_small_frequency (N : ℕ) (hN : 0 < N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) : tangentL1 (tau N η) ≤ Real.pi/(3*layerScale N) := by
  have hr : 0 < Real.sqrt ((N : ℝ)/2) := by positivity
  have he : tangentL1 (tau N η) = Real.sqrt ((N : ℝ)/2)*tangentL1 (transverseCoordinates η) := by
    simp only [tangentL1,tau,abs_mul,abs_of_pos hr]
    ring
  rw [he]
  have hb := (transverse_l1_bound η).trans (by linarith : 2*frequencyNorm η ≤ Real.pi/3)
  have h := mul_le_mul_of_nonneg_left hb hr.le
  calc
    _ ≤ Real.sqrt ((N : ℝ)/2)*(Real.pi/3) := h
    _ = _ := by unfold layerScale; field_simp

theorem dualCubicConstant_nonneg : 0 ≤ dualCubicConstant := by
  exact tsum_nonneg (fun p => by unfold integerL1CubicKernel; positivity)

/-- The joint absolutely convergent series equals the iterated series used in Poisson. -/
theorem iterated_dual_zero_split (δ : ℝ) (hδ : 0 ≤ δ) (s : ℝ) (hs : 0 < s) (τ : Tangent)
    (hτ : tangentL1 τ ≤ Real.pi/(3*s)) (k : ℤ) :
    (∑' m : ℤ, ∑' n : ℤ,
      Complex.exp (Complex.I*((-2*Real.pi*(k : ℝ)*((m : ℝ)+(n : ℝ))/3 : ℝ) : ℂ)) *
        psi δ (tangentShiftedFrequency τ s (m : ℝ) (n : ℝ))) =
      psi δ τ+nonzeroDualSum δ τ s k := by
  let F : ℤ × ℤ → ℂ := fun p =>
    Complex.exp (Complex.I*((-2*Real.pi*(k : ℝ)*((p.1 : ℝ)+(p.2 : ℝ))/3 : ℝ) : ℂ)) *
      psi δ (tangentShiftedFrequency τ s (p.1 : ℝ) (p.2 : ℝ))
  let Z : ℤ × ℤ → ℂ := fun p => if p=(0,0) then psi δ τ else 0
  have hZ : Summable Z := summable_of_ne_finset_zero (s := {(0,0)}) (by
    intro p hp
    simp only [Finset.mem_singleton] at hp
    simp [Z,hp])
  have hT := nonzeroDualTerm_summable δ hδ s hs τ hτ k
  have he : F = fun p => Z p+nonzeroDualTerm δ τ s k p := by
    funext p
    by_cases hp : p=(0,0)
    · subst p
      simp [F,Z,nonzeroDualTerm,tangent_shifted_frequency_zero]
    · simp [F,Z,nonzeroDualTerm,hp]
  have hF : Summable F := by rw [he]; exact hZ.add hT
  change (∑' m : ℤ, ∑' n : ℤ, F (m,n)) = _
  rw [← hF.tsum_prod,he,hZ.tsum_add hT]
  simp [Z,nonzeroDualSum]

theorem layerDualSum_zero_split (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) (η : Frequency) (hη : frequencyNorm η ≤ Real.pi/6) :
    layerDualSum N k (tau N η) = psi (effectiveLayerDepth N k) (tau N η) +
      nonzeroDualSum (effectiveLayerDepth N k) (tau N η) (layerScale N) k :=
  iterated_dual_zero_split _ (effectiveLayerDepth_of_active_layer N hN k hk) _
    (layerScale_pos N hN) _ (tau_small_frequency N hN η hη) k

theorem layerScale_cube_bound (N : ℕ) (hN : 0 < N) :
    (layerScale N)^3 ≤ 8/((N : ℝ)*Real.sqrt (N : ℝ)) := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hs : 0 < Real.sqrt (N : ℝ) := Real.sqrt_pos.mpr hn
  have hr : Real.sqrt (N : ℝ)/2 ≤ Real.sqrt ((N : ℝ)/2) := by
    apply Real.le_sqrt_of_sq_le
    rw [div_pow,Real.sq_sqrt hn.le]
    nlinarith
  have hi := one_div_le_one_div_of_le (show 0 < Real.sqrt (N : ℝ)/2 by positivity) hr
  have hb : layerScale N ≤ 2/Real.sqrt (N : ℝ) := by
    simpa only [layerScale,one_div,inv_div,inv_inv] using hi
  have hp := pow_le_pow_left₀ (layerScale_pos N hN).le hb 3
  calc
    _ ≤ (2/Real.sqrt (N : ℝ))^3 := hp
    _ = _ := by
      have he : Real.sqrt (N : ℝ)^3 = (N : ℝ)*Real.sqrt (N : ℝ) := by
        rw [pow_succ,Real.sq_sqrt hn.le]
      rw [div_pow,he]
      norm_num

def dualErrorConstant : ℝ := 221184*dualCubicConstant/Real.pi^3

theorem layer_nonzero_dual_bound (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) (η : Frequency) (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η)‖ ≤
      dualErrorConstant*indexedLayerDepth N k*(indexedLayerDepth N k+1)/
        ((N : ℝ)*Real.sqrt (N : ℝ)) := by
  rw [layerDualSum_zero_split N hN k hk η hη,add_sub_cancel_left]
  have hd := effectiveLayerDepth_of_active_layer N hN k hk
  have he : effectiveLayerDepth N k ≤ indexedLayerDepth N k := by
    unfold effectiveLayerDepth
    have hh : 0 ≤ 2*(indexedLayerDepth N k)^2/(N : ℝ) := by positivity
    linarith
  have hδ := hd.trans he
  have h := nonzeroDualSum_bound _ hd _ (layerScale_pos N hN) _ (tau_small_frequency N hN η hη) k
  have hC := dualCubicConstant_nonneg
  have hsp : 0 ≤ (layerScale N)^3 := pow_nonneg (layerScale_pos N hN).le 3
  apply h.trans
  calc
    _ ≤ (27648*indexedLayerDepth N k*(indexedLayerDepth N k+1)*(8/((N : ℝ)*Real.sqrt (N : ℝ)))/Real.pi^3)*dualCubicConstant := by
      gcongr
      all_goals first | exact hsp | positivity | exact he | exact layerScale_cube_bound N hN
    _ = _ := by unfold dualErrorConstant; ring

def dualErrorTiltConstant (t : ℝ) : ℝ := dualErrorConstant*∑' j : ℕ, weightedDepthEnvelope t j

theorem dualErrorConstant_nonneg : 0 ≤ dualErrorConstant := by
  unfold dualErrorConstant
  have hc := dualCubicConstant_nonneg
  positivity

/-- All nonzero dual contributions, summed over every active layer, uniformly in the small ball. -/
theorem weighted_nonzero_dual_bound (N : ℕ) (hN : 0 < N) (t : ℝ) (ht : 0 < t)
    (η : Frequency) (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k *
      (layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))‖ ≤
        dualErrorTiltConstant t/((N : ℝ)*Real.sqrt (N : ℝ)) := by
  let S := (aliceSites N).image planeIndex
  let D : ℝ := (N : ℝ)*Real.sqrt (N : ℝ)
  have hD : 0 < D := by dsimp [D]; positivity
  have hC := dualErrorConstant_nonneg
  have henv (j : ℕ) : 0 ≤ weightedDepthEnvelope t j := by unfold weightedDepthEnvelope; positivity
  have hpoint (k : ℤ) (hk : k ∈ S) :
      ‖layerGlobalFactor N t η k*(layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))‖ ≤
        (dualErrorConstant/D)*weightedDepthEnvelope t (layerNaturalIndex N k) := by
    have hd := active_layer_depth_le_index N hN k hk
    let a : ℝ := (layerNaturalIndex N k : ℝ)+2
    have ha : 1 ≤ a := by
      have hh : 0 ≤ (layerNaturalIndex N k : ℝ) := Nat.cast_nonneg _
      dsimp [a]
      linarith
    have hbase : indexedLayerDepth N k+1 ≤ a := by dsimp [a]; linarith [hd.2]
    have hsq := pow_le_pow_left₀ (show 0 ≤ indexedLayerDepth N k+1 by linarith [hd.1]) hbase 2
    have hp : indexedLayerDepth N k*(indexedLayerDepth N k+1) ≤ a^5 := by
      have h2 : indexedLayerDepth N k*(indexedLayerDepth N k+1) ≤ a^2 := by nlinarith
      exact h2.trans (pow_le_pow_right₀ ha (by decide : 2 ≤ 5))
    have hpoly : dualErrorConstant*indexedLayerDepth N k*(indexedLayerDepth N k+1) ≤ dualErrorConstant*a^5 := by
      simpa only [mul_assoc] using mul_le_mul_of_nonneg_left hp hC
    rw [norm_mul]
    calc
      _ ≤ Real.exp (-t*(layerNaturalIndex N k : ℝ))*(dualErrorConstant*a^5/D) := by
        exact mul_le_mul (layerGlobalFactor_norm_bound N hN t ht η k hk)
          ((layer_nonzero_dual_bound N hN k hk η hη).trans ((div_le_div_iff_of_pos_right hD).2 hpoly))
          (norm_nonneg _) (Real.exp_nonneg _)
      _ = _ := by dsimp [weightedDepthEnvelope,a]; ring
  calc
    _ ≤ ∑ k ∈ S, ‖layerGlobalFactor N t η k*
        (layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))‖ := norm_sum_le _ _
    _ ≤ ∑ k ∈ S, (dualErrorConstant/D)*weightedDepthEnvelope t (layerNaturalIndex N k) := Finset.sum_le_sum hpoint
    _ = (dualErrorConstant/D)*∑ k ∈ S, weightedDepthEnvelope t (layerNaturalIndex N k) := by rw [Finset.mul_sum]
    _ = (dualErrorConstant/D)*∑ j ∈ S.image (layerNaturalIndex N), weightedDepthEnvelope t j := by
      rw [Finset.sum_image (active_layer_index_injective N hN)]
    _ ≤ (dualErrorConstant/D)*∑' j : ℕ, weightedDepthEnvelope t j := by
      exact mul_le_mul_of_nonneg_left
        ((weightedDepthEnvelope_summable t ht).sum_le_tsum _ (fun j _ => henv j)) (div_nonneg hC hD.le)
    _ = _ := by unfold dualErrorTiltConstant; dsimp [D]; ring

theorem critical_weighted_nonzero_dual_bound (N : ℕ) (hN : 0 < N)
    (η : Frequency) (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N criticalTilt η k *
      (layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))‖ ≤
        dualErrorTiltConstant criticalTilt/((N : ℝ)*Real.sqrt (N : ℝ)) :=
  weighted_nonzero_dual_bound N hN criticalTilt criticalTilt_pos η hη

def dualAmplitudeConstant : ℝ := |(16*Real.pi/Real.sqrt 3)*boundaryResource| * dualErrorTiltConstant criticalTilt

/-- The nonzero dual part of the original amplitude is uniformly O(N^(-4)). -/
theorem dual_amplitude_uniform_bound (N : ℕ) (hN : 0 < N) (η : Frequency)
    (hη : frequencyNorm η ≤ Real.pi/6) :
    ‖(leadingScale N : ℂ)*∑ k ∈ (aliceSites N).image planeIndex,
      layerGlobalFactor N criticalTilt η k *
        (layerDualSum N k (tau N η)-psi (effectiveLayerDepth N k) (tau N η))‖ ≤
      dualAmplitudeConstant/(N : ℝ)^4 := by
  have hn : (0 : ℝ)<N := Nat.cast_pos.mpr hN
  have hr : 0 < Real.sqrt (N : ℝ) := Real.sqrt_pos.mpr hn
  have he : Real.rpow (N : ℝ) (-(5 : ℝ)/2) = 1/((N : ℝ)^2*Real.sqrt (N : ℝ)) :=
    rpow_neg_five_halves _ hn
  have hlead : ‖(leadingScale N : ℂ)‖ =
      (1/((N : ℝ)^2*Real.sqrt (N : ℝ)))*|(16*Real.pi/Real.sqrt 3)*boundaryResource| := by
    rw [Complex.norm_real,Real.norm_eq_abs]
    unfold leadingScale
    rw [he,mul_assoc,abs_mul,abs_of_pos (by positivity : 0 < 1/((N : ℝ)^2*Real.sqrt (N : ℝ)))]
  rw [norm_mul,hlead]
  calc
    _ ≤ ((1/((N : ℝ)^2*Real.sqrt (N : ℝ)))*|(16*Real.pi/Real.sqrt 3)*boundaryResource|)*
      (dualErrorTiltConstant criticalTilt/((N : ℝ)*Real.sqrt (N : ℝ))) :=
      mul_le_mul_of_nonneg_left (critical_weighted_nonzero_dual_bound N hN η hη) (by positivity)
    _ = _ := by
      unfold dualAmplitudeConstant
      have hrs : Real.sqrt (N : ℝ)^2=(N : ℝ) := Real.sq_sqrt hn.le
      field_simp
      ring_nf
      rw [hrs]
      ring

end AliceLayers
