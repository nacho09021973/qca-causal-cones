import AliceLayers.SectionRegularity

noncomputable section
open Filter MeasureTheory
open scoped Topology
namespace AliceLayers

/-- Classical second derivative away from the circular boundary. -/
def cutoffSecond (δ x y : ℝ) : ℝ :=
  if 0 < δ-y^2-x^2 then 12*y^2 - 4*(δ-x^2) else 0

theorem section_second_inside (δ x y : ℝ) (h : 0 < δ-y^2-x^2) :
    HasDerivAt (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0)
      (12*y^2 - 4*(δ-x^2)) y := by
  have hc : Continuous (fun t : ℝ => δ-t^2-x^2) := by fun_prop
  have hn : ∀ᶠ t : ℝ in 𝓝 y, 0 < δ-t^2-x^2 :=
    (isOpen_lt continuous_const hc).mem_nhds h
  have he : (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0) =ᶠ[𝓝 y]
      (fun t : ℝ => -4*t * (δ-t^2-x^2)) := by
    filter_upwards [hn] with t ht
    simp [max_eq_left ht.le]
  have hd : HasDerivAt (fun t : ℝ => -4*t * (δ-t^2-x^2))
      (12*y^2 - 4*(δ-x^2)) y := by
    convert! (((hasDerivAt_const y (-4 : ℝ)).mul (hasDerivAt_id y)).mul
      (((hasDerivAt_const y δ).sub ((hasDerivAt_id y).pow 2)).sub
        (hasDerivAt_const y (x^2)))) using 1
    all_goals try (funext t)
    all_goals simp_all [id_eq, Pi.pow_apply, Pi.sub_apply] <;> ring
  exact hd.congr_of_eventuallyEq he

theorem section_second_outside (δ x y : ℝ) (h : δ-y^2-x^2 < 0) :
    HasDerivAt (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0) 0 y := by
  have hc : Continuous (fun t : ℝ => δ-t^2-x^2) := by fun_prop
  have hn : ∀ᶠ t : ℝ in 𝓝 y, δ-t^2-x^2 < 0 :=
    (isOpen_lt hc continuous_const).mem_nhds h
  have he : (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0) =ᶠ[𝓝 y]
      (fun _ : ℝ => (0 : ℝ)) := by
    filter_upwards [hn] with t ht
    simp [max_eq_right ht.le]
  exact (hasDerivAt_const y (0 : ℝ)).congr_of_eventuallyEq he

theorem section_second_away (δ x y : ℝ) (h : δ-y^2-x^2 ≠ 0) :
    HasDerivAt (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0)
      (cutoffSecond δ x y) y := by
  rcases lt_or_gt_of_ne h with hn | hp
  · simpa [cutoffSecond, not_lt.mpr hn.le] using section_second_outside δ x y hn
  · simpa [cutoffSecond, hp] using section_second_inside δ x y hp

theorem section_boundary_finite (δ x : ℝ) : {y : ℝ | δ-y^2-x^2 = 0}.Finite := by
  apply ((Set.finite_singleton (Real.sqrt (δ-x^2))).union
    (Set.finite_singleton (-Real.sqrt (δ-x^2)))).subset
  intro y hy
  have hsq : y^2 = δ-x^2 := by simp only [Set.mem_setOf_eq] at hy; linarith
  have hnon : 0 ≤ δ-x^2 := by rw [← hsq]; positivity
  have hroot : (Real.sqrt (δ-x^2))^2 = δ-x^2 := Real.sq_sqrt hnon
  have he : y = Real.sqrt (δ-x^2) ∨ y = -Real.sqrt (δ-x^2) :=
    sq_eq_sq_iff_eq_or_eq_neg.mp (hsq.trans hroot.symm)
  simpa [or_comm] using he

theorem section_second_ae (δ x : ℝ) :
    ∀ᵐ y : ℝ, HasDerivAt (fun t : ℝ => -4*t * max (δ-t^2-x^2) 0)
      (cutoffSecond δ x y) y := by
  have hzero : volume {y : ℝ | δ-y^2-x^2 = 0} = 0 :=
    (section_boundary_finite δ x).measure_zero volume
  have hae : ∀ᵐ y : ℝ, y ∉ {y : ℝ | δ-y^2-x^2 = 0} := by
    rw [ae_iff]
    simpa using hzero
  filter_upwards [hae] with y hy
  apply section_second_away
  simpa using hy

/-- The piecewise second derivative is Lebesgue integrable, even at degenerate slices. -/
theorem cutoffSecond_integrable (δ x : ℝ) : Integrable (cutoffSecond δ x) := by
  let s : Set ℝ := {y | 0 < δ-y^2-x^2}
  let p : ℝ → ℝ := fun y => 12*y^2 - 4*(δ-x^2)
  have hc : Continuous p := by dsimp [p]; fun_prop
  have hq : Continuous (fun y : ℝ => δ-y^2-x^2) := by fun_prop
  have hm : MeasurableSet s := (isOpen_lt continuous_const hq).measurableSet
  have hs : s ⊆ Set.Icc (-(|δ|+1)) (|δ|+1) := by
    intro y hy
    have hy' : 0 < δ-y^2-x^2 := hy
    have hd : δ ≤ |δ| := le_abs_self δ
    have ha : 0 ≤ |δ| := abs_nonneg δ
    constructor <;> nlinarith [sq_nonneg (|δ|+1), sq_nonneg x]
  have hp : IntegrableOn p s :=
    (hc.continuousOn.integrableOn_compact (isCompact_Icc :
      IsCompact (Set.Icc (-(|δ|+1)) (|δ|+1)))).mono_set hs
  have hi : Integrable (s.indicator p) := hp.integrable_indicator hm
  convert hi using 1
  funext y
  by_cases hy : y ∈ s <;> simp [cutoffSecond, s, p, hy, Set.indicator]

/-- The classical second derivative agrees almost everywhere with the integrable
piecewise expression; no pointwise assertion is made at the rim. -/
theorem section_second_deriv_ae (δ x : ℝ) :
    (fun y => deriv (deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2))) y) =ᵐ[volume]
      cutoffSecond δ x := by
  have he : deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2)) =
      fun t => -4*t * max (δ-t^2-x^2) 0 := by
    funext t
    exact (section_cutoff_derivative δ x t).deriv
  rw [he]
  filter_upwards [section_second_ae δ x] with y hy
  exact hy.deriv

theorem section_second_deriv_integrable (δ x : ℝ) :
    Integrable (deriv (deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2)))) := by
  exact (cutoffSecond_integrable δ x).congr (section_second_deriv_ae δ x).symm

end AliceLayers
