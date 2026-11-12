import AliceLayers.Covolume

noncomputable section
open scoped BigOperators
namespace AliceLayers

/-- Exact finite coordinate set of the k-th layer. -/
def layerCoordinates (N : ℕ) (k : ℤ) : Finset (ℤ × ℤ) :=
  ((aliceSites N).filter (fun x => planeIndex x = k)).image (fun x => (x 0, x 1))

def layerShift (k : ℤ) : Tangent := ![0, -2 * (k : ℝ) / Real.sqrt 6]

theorem layer_transverse_coordinates (k a b : ℤ) :
    transverseCoordinates (fun i => (layerPoint k a b i : ℝ)) =
      layerShift k + tangentMap ![(a : ℝ), (b : ℝ)] := by
  ext i
  fin_cases i <;> simp [transverseCoordinates, layerPoint, layerShift, tangentMap,
    Matrix.cons_val_two, Matrix.vecHead, Matrix.vecTail] <;> ring

theorem layerCoordinates_membership (N : ℕ) (k : ℤ) (p : ℤ × ℤ) :
    p ∈ layerCoordinates N k ↔ layerPoint k p.1 p.2 ∈ aliceSites N := by
  classical
  constructor
  · intro h
    obtain ⟨x, hx, hp⟩ := Finset.mem_image.mp h
    have hi := (Finset.mem_filter.mp hx).2
    have hs := (Finset.mem_filter.mp hx).1
    have hpoint := layerPoint_coordinates x
    rw [hi] at hpoint
    cases p with
    | mk a b =>
      have h0 : x 0 = a := congrArg Prod.fst hp
      have h1 : x 1 = b := congrArg Prod.snd hp
      rw [h0, h1] at hpoint
      rw [hpoint]
      exact hs
  · intro h
    apply Finset.mem_image.mpr
    refine ⟨layerPoint k p.1 p.2, Finset.mem_filter.mpr ⟨h, planeIndex_layerPoint _ _ _⟩, ?_⟩
    cases p
    simp [layerPoint]

theorem layer_fiber_image (N : ℕ) (k : ℤ) :
    (layerCoordinates N k).image (fun p => layerPoint k p.1 p.2) =
      (aliceSites N).filter (fun x => planeIndex x = k) := by
  classical
  ext x
  constructor
  · intro h
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp h
    exact Finset.mem_filter.mpr ⟨(layerCoordinates_membership N k p).1 hp,
      planeIndex_layerPoint _ _ _⟩
  · intro hx
    have hi := (Finset.mem_filter.mp hx).2
    refine Finset.mem_image.mpr ⟨(x 0, x 1), ?_, ?_⟩
    · apply (layerCoordinates_membership N k _).2
      rw [← hi, layerPoint_coordinates]
      exact (Finset.mem_filter.mp hx).1
    · rw [← hi, layerPoint_coordinates]

theorem layer_sum_reindexed (N : ℕ) (k : ℤ) (f : Lattice → ℂ) :
    (∑ x ∈ (aliceSites N).filter (fun x => planeIndex x = k), f x) =
      ∑ p ∈ layerCoordinates N k, f (layerPoint k p.1 p.2) := by
  classical
  rw [← layer_fiber_image N k]
  exact Finset.sum_image (fun _ _ _ _ h => layerPoint_injective k h)

theorem amplitude_reindexed (N : ℕ) (t : ℝ) (η : Frequency) :
    amplitude N t η =
      ∑ k ∈ (aliceSites N).image planeIndex,
        ∑ p ∈ layerCoordinates N k,
          Complex.exp (Complex.I * (phase N η (layerPoint k p.1 p.2) : ℂ)) *
            ((tiltWeight N t (layerPoint k p.1 p.2) * profileS N (layerPoint k p.1 p.2) *
              resource N (layerPoint k p.1 p.2) : ℝ) : ℂ) := by
  rw [amplitude_by_planes]
  apply Finset.sum_congr rfl
  intro k hk
  exact layer_sum_reindexed N k _

/-- The original centered phase splits into normal and tangent coordinates. -/
theorem layer_phase_coordinates (N : ℕ) (η : Frequency) (k a b : ℤ) :
    phase N η (layerPoint k a b) =
      normalFrequency η * ((k : ℝ) / Real.sqrt 3 - (N : ℝ)/4) +
      ∑ i, transverseCoordinates η i *
        (layerShift k + tangentMap ![(a : ℝ), (b : ℝ)]) i := by
  rw [← layer_transverse_coordinates]
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  have h6 : Real.sqrt 6 * Real.sqrt 6 = 6 := Real.mul_self_sqrt (by norm_num)
  have hn2 : Real.sqrt 2 ≠ 0 := by positivity
  have hn3 : Real.sqrt 3 ≠ 0 := by positivity
  have hn6 : Real.sqrt 6 ≠ 0 := by positivity
  simp [phase, centerCoordinate, normalFrequency, transverseCoordinates, layerPoint,
    Fin.sum_univ_two, Fin.sum_univ_three, Matrix.cons_val_two, Matrix.vecHead, Matrix.vecTail]
  field_simp
  simp only [Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2),
    Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 3), Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 6)]
  ring_nf
  rw [Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 3)]
  ring

/-- The tangential image of each integer layer is a translate of the same lattice. -/
theorem layer_is_lattice_translate (k : ℤ) (q : Tangent) :
    (∃ x : Lattice, planeIndex x = k ∧
      q = transverseCoordinates (fun i => (x i : ℝ))) ↔
      q - layerShift k ∈ tangentLattice := by
  rw [tangentLattice_iff]
  constructor
  · rintro ⟨x, hx, hq⟩
    refine ⟨x 0, x 1, ?_⟩
    have he : layerPoint k (x 0) (x 1) = x := by
      rw [← hx, layerPoint_coordinates]
    rw [← he] at hq
    rw [layer_transverse_coordinates] at hq
    rw [hq]
    abel
  · rintro ⟨a, b, h⟩
    refine ⟨layerPoint k a b, planeIndex_layerPoint _ _ _, ?_⟩
    rw [layer_transverse_coordinates]
    have hq := sub_eq_iff_eq_add.mp h
    simpa [add_comm] using hq

/-- Support in coordinate space is the exact spherical layer domain. -/
theorem layerCoordinates_domain (N : ℕ) (hN : 0 < N) (k : ℤ) (p : ℤ × ℤ) :
    p ∈ layerCoordinates N k ↔
      let δ := (Real.sqrt 3 * (N : ℝ)/4 - (k : ℝ)) / Real.sqrt 3
      let q := layerShift k + tangentMap ![(p.1 : ℝ), (p.2 : ℝ)]
      0 ≤ δ ∧ δ ≤ (N : ℝ)/2 ∧ (∑ i, q i ^ 2) ≤ δ * ((N : ℝ)/2 - δ) := by
  rw [layerCoordinates_membership, lattice_layer_domain N hN]
  simp only [layer_depth_from_index, planeIndex_layerPoint, latticeLayerRadiusSquared,
    layer_transverse_coordinates]

/-- Exact original amplitude with the normal and transverse phase exposed. -/
theorem amplitude_reindexed_phase (N : ℕ) (t : ℝ) (η : Frequency) :
    amplitude N t η =
      ∑ k ∈ (aliceSites N).image planeIndex,
        ∑ p ∈ layerCoordinates N k,
          Complex.exp (Complex.I * ((normalFrequency η *
            ((k : ℝ) / Real.sqrt 3 - (N : ℝ)/4) +
            ∑ i, transverseCoordinates η i *
              (layerShift k + tangentMap ![(p.1 : ℝ), (p.2 : ℝ)]) i : ℝ) : ℂ)) *
            ((tiltWeight N t (layerPoint k p.1 p.2) * profileS N (layerPoint k p.1 p.2) *
              resource N (layerPoint k p.1 p.2) : ℝ) : ℂ) := by
  rw [amplitude_reindexed]
  simp_rw [layer_phase_coordinates]

end AliceLayers
