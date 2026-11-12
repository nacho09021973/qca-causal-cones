import AliceLayers.NormalPhase

noncomputable section
open scoped BigOperators
namespace AliceLayers

/-- Integer plane corresponding to every natural depth index, including inactive ones. -/
def depthPlaneIndex (N j : ℕ) : ℤ := ⌊Real.sqrt 3*(N : ℝ)/4⌋-(j : ℤ)

def activeDepthIndices (N : ℕ) : Finset ℕ :=
  ((aliceSites N).image planeIndex).image (layerNaturalIndex N)

theorem depthPlaneIndex_naturalIndex (N j : ℕ) :
    layerNaturalIndex N (depthPlaneIndex N j) = j := by
  simp [layerNaturalIndex, depthPlaneIndex]

theorem active_depthPlaneIndex (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∈ (aliceSites N).image planeIndex) :
    depthPlaneIndex N (layerNaturalIndex N k) = k := by
  unfold depthPlaneIndex
  rw [active_layer_index_cast N hN k hk]
  ring

theorem activeDepthIndices_membership (N : ℕ) (hN : 0 < N) (j : ℕ) :
    j ∈ activeDepthIndices N ↔ depthPlaneIndex N j ∈ (aliceSites N).image planeIndex := by
  constructor
  · intro hj
    obtain ⟨k,hk,rfl⟩ := Finset.mem_image.mp hj
    simpa only [active_depthPlaneIndex N hN k hk] using hk
  · intro hj
    exact Finset.mem_image.mpr ⟨depthPlaneIndex N j, hj, depthPlaneIndex_naturalIndex N j⟩

theorem depthPlaneIndex_depth (N j : ℕ) :
    indexedLayerDepth N (depthPlaneIndex N j) = (theta N+(j : ℝ))/Real.sqrt 3 := by
  have hf := Int.fract_add_floor (Real.sqrt 3*(N : ℝ)/4)
  have hs : Real.sqrt 3 ≠ 0 := by positivity
  unfold indexedLayerDepth depthPlaneIndex theta
  push_cast
  apply (eq_div_iff hs).2
  field_simp
  have hf' : Int.fract ((N : ℝ)*Real.sqrt 3/4) +
      (⌊(N : ℝ)*Real.sqrt 3/4⌋ : ℝ) = (N : ℝ)*Real.sqrt 3/4 := by
    simpa only [mul_comm (Real.sqrt 3) (N : ℝ)] using hf
  nlinarith [hf']

/-- A concrete integer point in every plane; no assertion of spherical membership. -/
def nearAxisPoint (k : ℤ) : Lattice := layerPoint k (k/3) (k/3)

theorem nearAxisPoint_plane (k : ℤ) : planeIndex (nearAxisPoint k) = k :=
  planeIndex_layerPoint k (k/3) (k/3)

theorem nearAxisPoint_radius_identity (k : ℤ) :
    latticeLayerRadiusSquared (nearAxisPoint k) =
      (2 : ℝ)/3*((k : ℝ)-3*((k/3 : ℤ) : ℝ))^2 := by
  norm_num [nearAxisPoint, latticeLayerRadiusSquared, transverseCoordinates,
    layerPoint, Fin.sum_univ_two, Matrix.cons_val_two, div_pow, Real.sq_sqrt]
  ring

theorem nearAxisPoint_radius_bound (k : ℤ) :
    latticeLayerRadiusSquared (nearAxisPoint k) ≤ 3 := by
  have hr0 : 0 ≤ k-3*(k/3) := by omega
  have hr2 : k-3*(k/3) ≤ 2 := by omega
  have h0 : (0 : ℝ) ≤ (k : ℝ)-3*((k/3 : ℤ) : ℝ) := by exact_mod_cast hr0
  have h2 : (k : ℝ)-3*((k/3 : ℤ) : ℝ) ≤ 2 := by exact_mod_cast hr2
  rw [nearAxisPoint_radius_identity]
  nlinarith

/-- If a plane is inactive inside the geometric depth range, its disk radius is small. -/
theorem inactive_layer_radius_lt (N : ℕ) (hN : 0 < N) (k : ℤ)
    (hk : k ∉ (aliceSites N).image planeIndex)
    (hd : 0 ≤ indexedLayerDepth N k) (hdN : indexedLayerDepth N k ≤ (N : ℝ)/2) :
    indexedLayerDepth N k*((N : ℝ)/2-indexedLayerDepth N k) < 3 := by
  by_contra hh
  have hr : 3 ≤ indexedLayerDepth N k*((N : ℝ)/2-indexedLayerDepth N k) := le_of_not_gt hh
  have hp : latticeLayerDepth N (nearAxisPoint k) = indexedLayerDepth N k := by
    simp [nearAxisPoint, indexedLayerDepth_point]
  have hx : nearAxisPoint k ∈ aliceSites N :=
    (lattice_layer_domain N hN _).2 (by
      rw [hp]
      exact ⟨hd, hdN, (nearAxisPoint_radius_bound k).trans hr⟩)
  exact hk (Finset.mem_image.mpr ⟨nearAxisPoint k, hx, nearAxisPoint_plane k⟩)

/-- Every omitted depth is either within 12/N of the top or deeper than N/4.
The second alternative includes all depths past the lower spherical boundary. -/
theorem omitted_depth_dichotomy (N : ℕ) (hN : 0 < N) (j : ℕ)
    (hj : j ∉ activeDepthIndices N) :
    (theta N+(j : ℝ))/Real.sqrt 3 ≤ 12/(N : ℝ) ∨
      (N : ℝ)/4 < (theta N+(j : ℝ))/Real.sqrt 3 := by
  let δ := (theta N+(j : ℝ))/Real.sqrt 3
  have hθ : 0 ≤ theta N := Int.fract_nonneg _
  have hd : 0 ≤ δ := by dsimp [δ]; positivity
  have hn : (0 : ℝ) < N := Nat.cast_pos.mpr hN
  by_cases hh : (N : ℝ)/4 < δ
  · exact Or.inr hh
  · left
    have hsmall : δ ≤ (N : ℝ)/4 := le_of_not_gt hh
    have hk : depthPlaneIndex N j ∉ (aliceSites N).image planeIndex :=
      fun hk => hj ((activeDepthIndices_membership N hN j).2 hk)
    have hr := inactive_layer_radius_lt N hN (depthPlaneIndex N j) hk
      (by rw [depthPlaneIndex_depth]; exact hd)
      (by rw [depthPlaneIndex_depth]; dsimp [δ] at hsmall; linarith)
    rw [depthPlaneIndex_depth] at hr
    change δ*((N : ℝ)/2-δ) < 3 at hr
    change δ ≤ 12/(N : ℝ)
    apply (le_div_iff₀ hn).2
    nlinarith [mul_nonneg hd (sub_nonneg.mpr hsmall)]

end AliceLayers
