import AliceLayers.Targets
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

noncomputable section
open scoped BigOperators

namespace AliceLayers

theorem tangent_sq_sum (σ : Tangent) :
    (∑ i, σ i ^ 2) = σ 0 ^ 2 + σ 1 ^ 2 := by
  simp [Fin.sum_univ_two]

theorem psi_integrand_vanishes_of_sqNorm_ge (δ : ℝ) (τ σ : Tangent)
    (hσ : δ ≤ ∑ i, σ i ^ 2) : psiIntegrand δ τ σ = 0 := by
  simp only [psiIntegrand]
  rw [tangent_sq_sum] at hσ ⊢
  have hpos : max (δ - (σ 0 ^ 2 + σ 1 ^ 2)) 0 = 0 := by
    rw [max_eq_right]
    linarith
  simp [hpos]

theorem psi_integrand_hasCompactSupport (δ : ℝ) (hδ : 0 ≤ δ) (τ : Tangent) :
    HasCompactSupport (psiIntegrand δ τ) := by
  let box : Set Tangent := Set.pi Set.univ fun _ => Set.Icc (-(δ + 1)) (δ + 1)
  have hbox : IsCompact box := by
    exact isCompact_univ_pi fun _ => isCompact_Icc
  apply HasCompactSupport.of_support_subset_isCompact hbox
  apply Function.support_subset_iff'.mpr
  intro σ hσ
  have hout : ∃ i, σ i ∉ Set.Icc (-(δ + 1)) (δ + 1) := by
    by_contra hn
    push Not at hn
    apply hσ
    intro i _
    exact hn i
  obtain ⟨i, hi⟩ := hout
  have hi' : σ i < -(δ + 1) ∨ δ + 1 < σ i := by
    simp only [Set.mem_Icc, not_and_or, not_le] at hi
    exact hi
  have hcoord : δ ≤ (σ i)^2 := by
    rcases hi' with hneg | hpos
    · have : δ + 1 < -σ i := by linarith
      nlinarith [sq_nonneg (δ + 1)]
    · nlinarith [sq_nonneg (δ + 1)]
  have hsum : (σ i)^2 ≤ ∑ j, σ j ^ 2 :=
    Finset.single_le_sum (fun j _ => sq_nonneg (σ j)) (Finset.mem_univ i)
  exact psi_integrand_vanishes_of_sqNorm_ge δ τ σ (le_trans hcoord hsum)

theorem psi_integrand_continuous (δ : ℝ) (τ : Tangent) :
    Continuous (psiIntegrand δ τ) := by
  change Continuous (fun σ : Tangent =>
    (((max (δ - ∑ i, σ i ^ 2) 0)^2 : ℝ) : ℂ) *
      Complex.exp (Complex.I * ((∑ i, τ i * σ i : ℝ) : ℂ)))
  fun_prop

theorem profile_integrability : ProfileIntegrability := by
  intro δ hδ τ
  exact (psi_integrand_continuous δ τ).integrable_of_hasCompactSupport
    (psi_integrand_hasCompactSupport δ hδ τ)

theorem phi0_kernel_intervalIntegrable (ρ : ℝ) :
    IntervalIntegrable (fun k : ℝ => k^2 * (1-k^2)^2 * Real.sinc (k*ρ))
      MeasureTheory.volume 0 1 := by
  letI : MeasureTheory.IsLocallyFiniteMeasure
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := Real.locallyFinite_volume
  have hc : Continuous (fun k : ℝ => k^2 * (1-k^2)^2 * Real.sinc (k*ρ)) := by
    fun_prop
  exact hc.intervalIntegrable (μ := MeasureTheory.volume) 0 1

theorem phi0_continuous : Continuous phi0 := by
  unfold phi0
  fun_prop

theorem rpow_neg_five_halves (x : ℝ) (hx : 0 < x) :
    x ^ (-(5 : ℝ)/2) = 1 / (x^2 * Real.sqrt x) := by
  have hpow : Real.sqrt x ^ 5 = x^2 * Real.sqrt x := by
    calc
      Real.sqrt x ^ 5 = (Real.sqrt x * Real.sqrt x)^2 * Real.sqrt x := by ring
      _ = x^2 * Real.sqrt x := by rw [Real.mul_self_sqrt hx.le]
  calc
    x ^ (-(5 : ℝ)/2) = (x ^ ((5 : ℝ)/2))⁻¹ := by
      rw [show (-(5 : ℝ)/2) = -(5/2 : ℝ) by ring]
      exact Real.rpow_neg hx.le ((5 : ℝ)/2)
    _ = (Real.sqrt x ^ 5)⁻¹ := by
      have hs := Real.rpow_div_two_eq_sqrt (5 : ℝ) hx.le
      have hs' : x ^ ((5 : ℝ)/2) = Real.sqrt x ^ (5 : ℕ) := by
        calc
          x ^ ((5 : ℝ)/2) = Real.sqrt x ^ (5 : ℝ) := hs
          _ = Real.sqrt x ^ (5 : ℕ) := Real.rpow_natCast _ _
      exact congrArg Inv.inv hs'
    _ = 1 / (x^2 * Real.sqrt x) := by rw [hpow]; simp [div_eq_mul_inv]

theorem rpow_neg_three_halves (x : ℝ) (hx : 0 < x) :
    x ^ (-(3 : ℝ)/2) = 1 / (x * Real.sqrt x) := by
  have hpow : Real.sqrt x ^ 3 = x * Real.sqrt x := by
    calc
      Real.sqrt x ^ 3 = (Real.sqrt x * Real.sqrt x) * Real.sqrt x := by ring
      _ = x * Real.sqrt x := by rw [Real.mul_self_sqrt hx.le]
  calc
    x ^ (-(3 : ℝ)/2) = (x ^ ((3 : ℝ)/2))⁻¹ := by
      rw [show (-(3 : ℝ)/2) = -(3/2 : ℝ) by ring]
      exact Real.rpow_neg hx.le ((3 : ℝ)/2)
    _ = (Real.sqrt x ^ 3)⁻¹ := by
      have hs := Real.rpow_div_two_eq_sqrt (3 : ℝ) hx.le
      have hs' : x ^ ((3 : ℝ)/2) = Real.sqrt x ^ (3 : ℕ) := by
        calc
          x ^ ((3 : ℝ)/2) = Real.sqrt x ^ (3 : ℝ) := hs
          _ = Real.sqrt x ^ (3 : ℕ) := Real.rpow_natCast _ _
      exact congrArg Inv.inv hs'
    _ = 1 / (x * Real.sqrt x) := by rw [hpow]; simp [div_eq_mul_inv]

theorem prefactor_rpow_identity (n φ : ℝ) (hn : 0 < n) :
    (1/Real.sqrt 3) * (32*Real.pi/n^2) * Real.rpow n (-(3 : ℝ)/2) * φ * (n/2) =
      (16*Real.pi/Real.sqrt 3) * φ * Real.rpow n (-(5 : ℝ)/2) := by
  change (1/Real.sqrt 3) * (32*Real.pi/n^2) * n ^ (-(3 : ℝ)/2) * φ * (n/2) =
      (16*Real.pi/Real.sqrt 3) * φ * n ^ (-(5 : ℝ)/2)
  rw [rpow_neg_three_halves n hn, rpow_neg_five_halves n hn]
  field_simp
  ring

theorem phase_sub_center (N : ℕ) (η : Frequency) (x : Lattice) :
    phase N η x = uncenteredPhase η x - centerCoordinate N * ∑ i, η i := by
  simp only [phase, uncenteredPhase, Fin.sum_univ_three]
  ring

theorem transverse_phase (N : ℕ) (η : Frequency) (x : Lattice)
    (h : ∑ i, η i = 0) : phase N η x = uncenteredPhase η x := by
  rw [phase_sub_center, h, mul_zero, sub_zero]

theorem finite_phase_bound {ι : Type*} (s : Finset ι) (p w : ι → ℝ) :
    ‖∑ x ∈ s, Complex.exp (Complex.I * (p x : ℂ)) * (w x : ℂ)‖ ≤
      ∑ x ∈ s, |w x| := by
  calc
    _ ≤ ∑ x ∈ s, ‖Complex.exp (Complex.I * (p x : ℂ)) * (w x : ℂ)‖ := norm_sum_le _ _
    _ = _ := by simp [Complex.norm_exp, Complex.mul_re, Complex.norm_real]

/-- Algebraic profile identity before applying the positive part; geometric domain is separate. -/
theorem layer_profile_identity (n δ q : ℝ) (hn : n ≠ 0) :
    (1 - 16 * ((n/4-δ)^2+q) / n^2)^2 =
      (64/n^2) * (δ - δ^2/(2*(n/4)) - q/(2*(n/4)))^2 := by
  field_simp
  ring

/-- Inside the sphere, layer depth and tangential squared radius have this exact domain. -/
theorem layer_ball_domain (n δ q : ℝ) (hn : 0 < n) (hq : 0 ≤ q) :
    16 * ((n/4-δ)^2+q) ≤ n^2 ↔
      0 ≤ δ ∧ δ ≤ n/2 ∧ q ≤ δ*(n/2-δ) := by
  constructor
  · intro h
    constructor
    · nlinarith [sq_nonneg (n/4-δ)]
    constructor
    · nlinarith [sq_nonneg (n/4-δ)]
    · nlinarith [sq_nonneg (n/4-δ)]
  · rintro ⟨hδ0, hδn, hqδ⟩
    nlinarith [sq_nonneg (n/4-δ)]

theorem layer_cutoff_profile (n δ q : ℝ) (hn : 0 < n) (hq : 0 ≤ q)
    (hdom : 0 ≤ δ ∧ δ ≤ n/2 ∧ q ≤ δ*(n/2-δ)) :
    (max (1 - 16*((n/4-δ)^2+q)/n^2) 0)^2 =
      (64/n^2) * (δ - δ^2/(2*(n/4)) - q/(2*(n/4)))^2 := by
  have hball := (layer_ball_domain n δ q hn hq).2 hdom
  have hden : 0 < n^2 := sq_pos_of_pos hn
  have hbase : 0 ≤ 1 - 16*((n/4-δ)^2+q)/n^2 := by
    rw [sub_nonneg]
    exact (div_le_one hden).2 hball
  rw [max_eq_left hbase, layer_profile_identity n δ q hn.ne']

/-- Exact coefficient collection in the paper, in reciprocal/sqrt notation.
Identifying these powers with rpow is a separate bridge, not assumed here. -/
theorem prefactor_identity (n φ : ℝ) (hn : n ≠ 0) :
    (1/Real.sqrt 3) * (32*Real.pi/n^2) * (1/(n*Real.sqrt n)) * φ * (n/2) =
      (16*Real.pi/Real.sqrt 3) * φ * (1/(n^2*Real.sqrt n)) := by
  field_simp
  ring

theorem frame_norm_identity (η : Frequency) :
    (normalFrequency η)^2 + ∑ i, (transverseCoordinates η i)^2 = ∑ i, η i ^ 2 := by
  norm_num [normalFrequency, transverseCoordinates, Fin.sum_univ_two, Fin.sum_univ_three,
    div_pow, Real.sq_sqrt]
  ring

theorem lattice_layer_decomposition (N : ℕ) (x : Lattice) :
    sqNorm x = ((N : ℝ)/4 - latticeLayerDepth N x)^2 +
      latticeLayerRadiusSquared x := by
  have hframe := frame_norm_identity (fun i => (x i : ℝ))
  have hnormal : (N : ℝ)/4 - latticeLayerDepth N x =
      normalFrequency (fun i => (x i : ℝ)) := by
    simp [latticeLayerDepth, normalFrequency]
  calc
    sqNorm x = (normalFrequency (fun i => (x i : ℝ)))^2 +
        latticeLayerRadiusSquared x := by
      simpa [sqNorm, latticeLayerRadiusSquared] using hframe.symm
    _ = _ := by rw [← hnormal]

/-- The bounded finite enumeration is exactly the whole Euclidean ball, including N=0. -/
theorem support_faithfulness : SupportFaithfulness := by
  intro N x
  simp only [aliceSites, Finset.mem_filter, latticeBox, Fintype.mem_piFinset, Finset.mem_Icc]
  constructor
  · exact fun h => h.2
  · intro h
    refine ⟨?_, h⟩
    intro i
    have hi : (x i : ℝ)^2 ≤ sqNorm x := by
      exact Finset.single_le_sum (fun j _ => sq_nonneg (x j : ℝ)) (Finset.mem_univ i)
    have hb : -(N : ℝ) ≤ (x i : ℝ) ∧ (x i : ℝ) ≤ (N : ℝ) :=
      abs_le_of_sq_le_sq' (by nlinarith [sq_nonneg (x i : ℝ)]) (Nat.cast_nonneg N)
    exact_mod_cast hb

theorem lattice_layer_domain (N : ℕ) (hN : 0 < N) (x : Lattice) :
    x ∈ aliceSites N ↔
      0 ≤ latticeLayerDepth N x ∧
      latticeLayerDepth N x ≤ (N : ℝ)/2 ∧
      latticeLayerRadiusSquared x ≤
        latticeLayerDepth N x * ((N : ℝ)/2 - latticeLayerDepth N x) := by
  rw [support_faithfulness N x, lattice_layer_decomposition]
  exact layer_ball_domain (N : ℝ) (latticeLayerDepth N x)
    (latticeLayerRadiusSquared x) (Nat.cast_pos.mpr hN)
    (Finset.sum_nonneg fun _ _ => sq_nonneg _)

end AliceLayers

namespace AliceLayers

/-- Integer coordinates on the plane with coordinate sum k. -/
def layerPoint (k a b : ℤ) : Lattice := ![a, b, k-a-b]

theorem planeIndex_layerPoint (k a b : ℤ) : planeIndex (layerPoint k a b) = k := by
  simp [planeIndex, layerPoint, Fin.sum_univ_three]

theorem layerPoint_coordinates (x : Lattice) :
    layerPoint (planeIndex x) (x 0) (x 1) = x := by
  funext i
  fin_cases i <;> simp [layerPoint, planeIndex, Fin.sum_univ_three] <;> ring

theorem layerPoint_injective (k : ℤ) : Function.Injective (fun p : ℤ × ℤ => layerPoint k p.1 p.2) := by
  intro p q h
  apply Prod.ext
  · simpa [layerPoint] using congrFun h 0
  · simpa [layerPoint] using congrFun h 1

/-- Gram determinant of the integer basis (1,0,-1), (0,1,-1). -/
theorem tangent_basis_gram : (2 : ℝ) * 2 - 1 * 1 = 3 := by norm_num

theorem tangent_basis_area : Real.sqrt ((2 : ℝ) * 2 - 1 * 1) = Real.sqrt 3 := by
  norm_num

/-- Exact regrouping of the finite amplitude into fibers of the integer plane index. -/
theorem amplitude_by_planes (N : ℕ) (t : ℝ) (η : Frequency) :
    amplitude N t η =
      ∑ k ∈ (aliceSites N).image planeIndex,
        ∑ x ∈ (aliceSites N).filter (fun x => planeIndex x = k),
          Complex.exp (Complex.I * (phase N η x : ℂ)) *
            ((tiltWeight N t x * profileS N x * resource N x : ℝ) : ℂ) := by
  classical
  unfold amplitude
  symm
  exact Finset.sum_fiberwise_of_maps_to (fun x hx => Finset.mem_image_of_mem planeIndex hx) _

end AliceLayers

namespace AliceLayers

def tangentBasis₁ : Lattice := ![1, 0, -1]
def tangentBasis₂ : Lattice := ![0, 1, -1]

theorem tangent_basis_indices : planeIndex tangentBasis₁ = 0 ∧ planeIndex tangentBasis₂ = 0 := by
  norm_num [planeIndex, tangentBasis₁, tangentBasis₂, Fin.sum_univ_three, Matrix.cons_val, Matrix.cons_val_two, Matrix.vecHead, Matrix.vecTail]

theorem tangent_basis_gram_entries :
    (∑ i, (tangentBasis₁ i : ℝ)^2) = 2 ∧
    (∑ i, (tangentBasis₂ i : ℝ)^2) = 2 ∧
    (∑ i, (tangentBasis₁ i : ℝ) * (tangentBasis₂ i : ℝ)) = 1 := by
  norm_num [tangentBasis₁, tangentBasis₂, Fin.sum_univ_three, Matrix.cons_val, Matrix.cons_val_two, Matrix.vecHead, Matrix.vecTail]

theorem layer_depth_from_index (N : ℕ) (x : Lattice) :
    latticeLayerDepth N x =
      (Real.sqrt 3 * (N : ℝ)/4 - (planeIndex x : ℝ)) / Real.sqrt 3 := by
  have h : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  have hn : Real.sqrt 3 ≠ 0 := by positivity
  simp only [latticeLayerDepth, planeIndex, Fin.sum_univ_three, Int.cast_add]
  field_simp

theorem layer_depth_from_theta (N : ℕ) (x : Lattice) :
    latticeLayerDepth N x =
      (theta N + ((⌊Real.sqrt 3 * (N : ℝ)/4⌋ - planeIndex x : ℤ) : ℝ)) /
        Real.sqrt 3 := by
  rw [layer_depth_from_index]
  have h := Int.fract_add_floor (Real.sqrt 3 * (N : ℝ)/4)
  simp only [theta, Int.cast_sub]
  congr 1
  linarith

end AliceLayers

namespace AliceLayers

theorem site_index_le_floor (N : ℕ) (hN : 0 < N) (x : Lattice)
    (hx : x ∈ aliceSites N) :
    planeIndex x ≤ ⌊Real.sqrt 3 * (N : ℝ)/4⌋ := by
  apply Int.le_floor.mpr
  have hd := ((lattice_layer_domain N hN x).1 hx).1
  rw [layer_depth_from_index] at hd
  have hs : 0 < Real.sqrt 3 := by positivity
  have hh : 0 ≤ Real.sqrt 3 * (N : ℝ)/4 - (planeIndex x : ℝ) := by simpa using (le_div_iff₀ hs).1 hd
  linarith

theorem site_depth_natural (N : ℕ) (hN : 0 < N) (x : Lattice)
    (hx : x ∈ aliceSites N) :
    ∃ j : ℕ, latticeLayerDepth N x = (theta N + (j : ℝ)) / Real.sqrt 3 := by
  let z : ℤ := ⌊Real.sqrt 3 * (N : ℝ)/4⌋ - planeIndex x
  have hz : 0 ≤ z := sub_nonneg.mpr (site_index_le_floor N hN x hx)
  refine ⟨z.toNat, ?_⟩
  rw [layer_depth_from_theta]
  have hc : ((z.toNat : ℕ) : ℤ) = z := Int.toNat_of_nonneg hz
  exact congrArg (fun y : ℝ => (theta N + y) / Real.sqrt 3) (by exact_mod_cast hc.symm)

end AliceLayers
