import AliceLayers.TangentSpectral

noncomputable section
open MeasureTheory
open scoped BigOperators
namespace AliceLayers

def indexedLayerDepth (N : ℕ) (k : ℤ) : ℝ := (N : ℝ)/4-(k : ℝ)/Real.sqrt 3
def effectiveLayerDepth (N : ℕ) (k : ℤ) : ℝ :=
  indexedLayerDepth N k - 2*(indexedLayerDepth N k)^2/(N : ℝ)
def layerScale (N : ℕ) : ℝ := (Real.sqrt ((N : ℝ)/2))⁻¹
def normalizedLayerPosition (N : ℕ) (k : ℤ) (p : Tangent) : Tangent :=
  layerScale N • (layerShift k + tangentMap p)

theorem layerScale_pos (N : ℕ) (hN : 0 < N) : 0 < layerScale N := by
  unfold layerScale
  positivity

theorem indexedLayerDepth_point (N : ℕ) (k a b : ℤ) :
    latticeLayerDepth N (layerPoint k a b) = indexedLayerDepth N k := by
  rw [layer_depth_from_index, planeIndex_layerPoint]
  have h3 : Real.sqrt 3 ≠ 0 := by positivity
  unfold indexedLayerDepth
  field_simp

theorem normalizedLayerPosition_sq (N : ℕ) (hN : 0 < N) (k : ℤ) (p : Tangent) :
    (∑ i, normalizedLayerPosition N k p i ^ 2) =
      2 * (∑ i, (layerShift k + tangentMap p) i ^ 2) / (N : ℝ) := by
  have hroot : (Real.sqrt ((N : ℝ)/2))^2 = (N : ℝ)/2 := Real.sq_sqrt (by positivity)
  simp only [normalizedLayerPosition, Pi.smul_apply, smul_eq_mul, mul_pow, ← Finset.mul_sum,
    layerScale, inv_pow, hroot]
  field_simp

/-- Exact positive-part identity, before any sine or resource approximation. -/
theorem finite_cutoff_algebra (n δ q : ℝ) (hn : 0 < n) :
    (max (1-16*((n/4-δ)^2+q)/n^2) 0)^2 =
      (64/n^2) * positiveSquare (δ-2*δ^2/n-2*q/n) := by
  have hc : 0 < 8/n := by positivity
  have he : 1-16*((n/4-δ)^2+q)/n^2 = (8/n)*(δ-2*δ^2/n-2*q/n) := by
    field_simp
    <;> ring
  rw [he]
  by_cases h : 0 ≤ δ-2*δ^2/n-2*q/n
  · rw [max_eq_left (mul_nonneg hc.le h), positiveSquare, max_eq_left h]
    field_simp
    <;> ring
  · have hh : δ-2*δ^2/n-2*q/n ≤ 0 := le_of_not_ge h
    rw [max_eq_right (mul_nonpos_of_nonneg_of_nonpos hc.le hh), positiveSquare, max_eq_right hh]
    simp

/-- Exact finite profile on every lattice point of a plane, including outside the ball. -/
theorem finite_profileF_identity (N : ℕ) (hN : 0 < N) (k a b : ℤ) :
    profileF N (layerPoint k a b) = (64/(N : ℝ)^2) *
      positiveSquare (effectiveLayerDepth N k -
        ∑ i, normalizedLayerPosition N k ![(a : ℝ),(b : ℝ)] i ^ 2) := by
  rw [profileF, cutoff, lattice_layer_decomposition, indexedLayerDepth_point]
  rw [finite_cutoff_algebra _ _ _ (Nat.cast_pos.mpr hN)]
  rw [normalizedLayerPosition_sq N hN]
  simp only [effectiveLayerDepth, latticeLayerRadiusSquared, layer_transverse_coordinates]

theorem finite_profileS_identity (N : ℕ) (hN : 0 < N) (k a b : ℤ) :
    profileS N (layerPoint k a b) = Real.sin ((32*Real.pi/(N : ℝ)^2) *
      positiveSquare (effectiveLayerDepth N k -
        ∑ i, normalizedLayerPosition N k ![(a : ℝ),(b : ℝ)] i ^ 2)) := by
  rw [profileS, finite_profileF_identity N hN]
  congr 1
  ring

theorem effectiveLayerDepth_nonneg (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hδ : 0 ≤ indexedLayerDepth N k) (hu : indexedLayerDepth N k ≤ (N : ℝ)/2) :
    0 ≤ effectiveLayerDepth N k := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  unfold effectiveLayerDepth
  apply sub_nonneg.mpr
  apply (div_le_iff₀ hn).2
  nlinarith

/-- No unsupported principal-profile tail is introduced outside the finite original support. -/
theorem effective_profile_vanishes (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ)
    (hp : p ∉ layerCoordinates N k) (τ : Tangent) :
    psiIntegrand (effectiveLayerDepth N k) τ
      (normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)]) = 0 := by
  have hx : layerPoint k p.1 p.2 ∉ aliceSites N := by
    simpa only [layerCoordinates_membership] using hp
  have hs : (N : ℝ)^2 < 16*sqNorm (layerPoint k p.1 p.2) := by
    exact lt_of_not_ge (fun h => hx ((support_faithfulness N _).2 h))
  have hden : (0 : ℝ) < (N : ℝ)^2 := by positivity
  have hcut : cutoff N (layerPoint k p.1 p.2) = 0 := by
    unfold cutoff
    apply max_eq_right
    have ht := (one_lt_div hden).2 hs
    linarith
  have hf : profileF N (layerPoint k p.1 p.2) = 0 := by simp [profileF,hcut]
  rw [finite_profileF_identity N hN] at hf
  have hc : (64/(N : ℝ)^2) ≠ 0 := by positivity
  have hz := (mul_eq_zero.mp hf).resolve_left hc
  change (((positiveSquare _) : ℝ) : ℂ) * _ = 0
  rw [hz, Complex.ofReal_zero, zero_mul]

/-- The leading sine argument, with its exact normalization. -/
def layerPolynomial (N : ℕ) (k : ℤ) (p : ℤ × ℤ) : ℝ :=
  positiveSquare (effectiveLayerDepth N k -
    ∑ i, normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)] i ^ 2)
def profileLinearArgument (N : ℕ) (x : Lattice) : ℝ := Real.pi/2 * profileF N x
def boundaryResourceScale (N : ℕ) : ℝ := Real.rpow (N : ℝ) (-(3 : ℝ)/2) * boundaryResource
def principalLayerCoefficient (N : ℕ) : ℝ := (32*Real.pi/(N : ℝ)^2) * boundaryResourceScale N
def sineProfileError (N : ℕ) (x : Lattice) : ℝ :=
  (Real.sin (profileLinearArgument N x)-profileLinearArgument N x)*resource N x
def radialResourceError (N : ℕ) (x : Lattice) : ℝ :=
  profileLinearArgument N x * (resource N x-boundaryResourceScale N)

theorem finite_linear_argument (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ) :
    profileLinearArgument N (layerPoint k p.1 p.2) =
      (32*Real.pi/(N : ℝ)^2)*layerPolynomial N k p := by
  rw [profileLinearArgument, finite_profileF_identity N hN]
  unfold layerPolynomial
  ring

/-- Explicit pointwise error split; no error estimate is asserted by this identity. -/
theorem finite_profile_error_split (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ) :
    profileS N (layerPoint k p.1 p.2) * resource N (layerPoint k p.1 p.2) =
      principalLayerCoefficient N * layerPolynomial N k p +
        sineProfileError N (layerPoint k p.1 p.2) +
          radialResourceError N (layerPoint k p.1 p.2) := by
  simp only [profileS, sineProfileError, radialResourceError, profileLinearArgument]
  have he := finite_linear_argument N hN k p
  unfold profileLinearArgument at he
  rw [he]
  unfold principalLayerCoefficient
  ring

/-- The effective principal profile extends from the exact finite support without a tail. -/
theorem finite_effective_sum_eq_tsum (N : ℕ) (hN : 0 < N) (k : ℤ) (τ : Tangent) :
    (∑ p ∈ layerCoordinates N k, psiIntegrand (effectiveLayerDepth N k) τ
      (normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)])) =
    ∑' n : ℤ, ∑' m : ℤ, psiIntegrand (effectiveLayerDepth N k) τ
      (normalizedLayerPosition N k ![(m : ℝ),(n : ℝ)]) := by
  let f : ℤ × ℤ → ℂ := fun p => psiIntegrand (effectiveLayerDepth N k) τ
    (normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)])
  have hv : ∀ p ∉ layerCoordinates N k, f p = 0 :=
    fun p hp => effective_profile_vanishes N hN k p hp τ
  have hs : Summable f := summable_of_ne_finset_zero hv
  have ht : (∑' p : ℤ × ℤ, f p) = ∑ p ∈ layerCoordinates N k, f p := tsum_eq_sum hv
  change (∑ p ∈ layerCoordinates N k, f p) = ∑' n : ℤ, ∑' m : ℤ, f (m,n)
  rw [← ht, hs.tsum_prod]
  exact hs.tsum_comm.symm

/-- Poisson now applies to the exact finite squared-cutoff profile at effective depth. -/
theorem finite_effective_poisson (N : ℕ) (hN : 0 < N) (k : ℤ) (τ : Tangent)
    (hd : 0 ≤ effectiveLayerDepth N k) :
    (∑ p ∈ layerCoordinates N k, psiIntegrand (effectiveLayerDepth N k) τ
      (normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)])) =
      ((((layerScale N)^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) *
        ∑' m : ℤ, ∑' n : ℤ,
          Complex.exp (Complex.I * ((-2*Real.pi*(k : ℝ)*((m : ℝ)+(n : ℝ))/3 : ℝ) : ℂ)) *
            psi (effectiveLayerDepth N k)
              (tangentShiftedFrequency τ (layerScale N) (m : ℝ) (n : ℝ)) := by
  rw [finite_effective_sum_eq_tsum N hN]
  exact tangent_layer_poisson _ hd τ _ (layerScale_pos N hN) k

def layerDualSum (N : ℕ) (k : ℤ) (τ : Tangent) : ℂ :=
  ∑' m : ℤ, ∑' n : ℤ,
    Complex.exp (Complex.I * ((-2*Real.pi*(k : ℝ)*((m : ℝ)+(n : ℝ))/3 : ℝ) : ℂ)) *
      psi (effectiveLayerDepth N k)
        (tangentShiftedFrequency τ (layerScale N) (m : ℝ) (n : ℝ))
def layerTransversePhase (N : ℕ) (k : ℤ) (τ : Tangent) (p : ℤ × ℤ) : ℂ :=
  Complex.exp (Complex.I * ((∑ i, τ i * normalizedLayerPosition N k
    ![(p.1 : ℝ),(p.2 : ℝ)] i : ℝ) : ℂ))
def originalLayerTransverseSum (N : ℕ) (k : ℤ) (τ : Tangent) : ℂ :=
  ∑ p ∈ layerCoordinates N k, layerTransversePhase N k τ p *
    ((profileS N (layerPoint k p.1 p.2) * resource N (layerPoint k p.1 p.2) : ℝ) : ℂ)
def finiteLayerError (N : ℕ) (k : ℤ) (τ : Tangent) : ℂ :=
  ∑ p ∈ layerCoordinates N k, layerTransversePhase N k τ p *
    ((sineProfileError N (layerPoint k p.1 p.2) + radialResourceError N (layerPoint k p.1 p.2) : ℝ) : ℂ)

/-- Exact connection to the original sine/resource profile, with an explicit finite error. -/
theorem original_layer_poisson_with_error (N : ℕ) (hN : 0 < N) (k : ℤ) (τ : Tangent)
    (hd : 0 ≤ effectiveLayerDepth N k) :
    originalLayerTransverseSum N k τ =
      (principalLayerCoefficient N : ℂ) *
        ((((layerScale N)^2 * Real.sqrt 3)⁻¹ : ℝ) : ℂ) * layerDualSum N k τ +
          finiteLayerError N k τ := by
  have he : originalLayerTransverseSum N k τ =
      (principalLayerCoefficient N : ℂ) *
        (∑ p ∈ layerCoordinates N k, psiIntegrand (effectiveLayerDepth N k) τ
          (normalizedLayerPosition N k ![(p.1 : ℝ),(p.2 : ℝ)])) + finiteLayerError N k τ := by
    unfold originalLayerTransverseSum finiteLayerError
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro p hp
    rw [finite_profile_error_split N hN k p]
    simp only [psiIntegrand, layerPolynomial, positiveSquare, layerTransversePhase]
    push_cast
    ring
  rw [he, finite_effective_poisson N hN k τ hd]
  simp only [layerDualSum, mul_assoc]

theorem normalized_layer_phase (N : ℕ) (hN : 0 < N) (k : ℤ) (η : Frequency) (p : Tangent) :
    (∑ i, tau N η i * normalizedLayerPosition N k p i) =
      ∑ i, transverseCoordinates η i * (layerShift k + tangentMap p) i := by
  have hr : Real.sqrt ((N : ℝ)/2) ≠ 0 := by positivity
  apply Finset.sum_congr rfl
  intro i hi
  simp only [tau, normalizedLayerPosition, layerScale, Pi.smul_apply, smul_eq_mul]
  field_simp

theorem effectiveLayerDepth_of_active_layer (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) : 0 ≤ effectiveLayerDepth N k := by
  obtain ⟨x,hx,hk⟩ := Finset.mem_image.mp hk
  have hdom := (lattice_layer_domain N hN x).1 hx
  have he : latticeLayerDepth N x = indexedLayerDepth N k := by
    rw [← hk, ← layerPoint_coordinates x, indexedLayerDepth_point, planeIndex_layerPoint]
  rw [he] at hdom
  exact effectiveLayerDepth_nonneg N hN k hdom.1 hdom.2.1

/-- The exact finite-layer prefactor is the same leadingScale used by AliceLayersB. -/
theorem principalLayer_prefactor (N : ℕ) (hN : 0 < N) :
    principalLayerCoefficient N * ((layerScale N)^2 * Real.sqrt 3)⁻¹ = leadingScale N := by
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  have hj : ((layerScale N)^2 * Real.sqrt 3)⁻¹ = ((N : ℝ)/2)/Real.sqrt 3 := by
    unfold layerScale
    rw [inv_pow, Real.sq_sqrt (by positivity : 0 ≤ (N : ℝ)/2)]
    field_simp
  rw [hj]
  unfold principalLayerCoefficient boundaryResourceScale leadingScale
  have he := prefactor_rpow_identity (N : ℝ) boundaryResource hn
  convert he using 1 <;> ring

theorem original_layer_poisson_leading (N : ℕ) (hN : 0 < N) (k : ℤ) (τ : Tangent)
    (hd : 0 ≤ effectiveLayerDepth N k) :
    originalLayerTransverseSum N k τ =
      (leadingScale N : ℂ) * layerDualSum N k τ + finiteLayerError N k τ := by
  have he := original_layer_poisson_with_error N hN k τ hd
  rw [← Complex.ofReal_mul, principalLayer_prefactor N hN] at he
  exact he

def layerGlobalFactor (N : ℕ) (t : ℝ) (η : Frequency) (k : ℤ) : ℂ :=
  Complex.exp (Complex.I * ((normalFrequency η * ((k : ℝ)/Real.sqrt 3-(N : ℝ)/4) : ℝ) : ℂ)) *
    ((Real.exp (t*((k : ℝ)-Real.sqrt 3*(N : ℝ)/4)) : ℝ) : ℂ)

theorem original_layer_factor (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) (k : ℤ) :
    (∑ p ∈ layerCoordinates N k,
      Complex.exp (Complex.I * (phase N η (layerPoint k p.1 p.2) : ℂ)) *
        ((tiltWeight N t (layerPoint k p.1 p.2) * profileS N (layerPoint k p.1 p.2) *
          resource N (layerPoint k p.1 p.2) : ℝ) : ℂ)) =
      layerGlobalFactor N t η k * originalLayerTransverseSum N k (tau N η) := by
  unfold originalLayerTransverseSum
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p hp
  rw [layer_phase_coordinates, ← normalized_layer_phase N hN k η]
  simp only [layerGlobalFactor, layerTransversePhase, tiltWeight, planeIndex_layerPoint,
    Complex.ofReal_mul, Complex.ofReal_add, mul_add, Complex.exp_add]
  ring

/-- Exact original amplitude linked to the dual-layer identity, with explicit finite errors.
The effective depth has NOT yet been replaced by the asymptotic depth. -/
theorem amplitude_finite_profile_poisson (N : ℕ) (hN : 0 < N) (t : ℝ) (η : Frequency) :
    amplitude N t η =
      ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k *
        ((leadingScale N : ℂ) * layerDualSum N k (tau N η) + finiteLayerError N k (tau N η)) := by
  rw [amplitude_reindexed]
  apply Finset.sum_congr rfl
  intro k hk
  rw [original_layer_factor N hN, original_layer_poisson_leading N hN k (tau N η)
    (effectiveLayerDepth_of_active_layer N hN k hk)]

end AliceLayers
