import AliceLayers.Basic
import Mathlib.Algebra.Module.ZLattice.Covolume

noncomputable section
open scoped BigOperators
open MeasureTheory Module
namespace AliceLayers

/-- Coordinates in the orthonormal tangential frame of (a,b,-a-b). -/
def tangentMap : Tangent ≃ₗ[ℝ] Tangent where
  toFun p := ![(p 0 - p 1) / Real.sqrt 2, 3 * (p 0 + p 1) / Real.sqrt 6]
  invFun q := ![Real.sqrt 2 * q 0 / 2 + Real.sqrt 6 * q 1 / 6,
    -Real.sqrt 2 * q 0 / 2 + Real.sqrt 6 * q 1 / 6]
  map_add' x y := by ext i; fin_cases i <;> simp <;> ring
  map_smul' c x := by ext i; fin_cases i <;> simp <;> ring
  left_inv p := by
    have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
    have h6 : Real.sqrt 6 * Real.sqrt 6 = 6 := Real.mul_self_sqrt (by norm_num)
    have hn2 : Real.sqrt 2 ≠ 0 := by positivity
    have hn6 : Real.sqrt 6 ≠ 0 := by positivity
    ext i; fin_cases i <;> simp <;> field_simp <;> nlinarith
  right_inv p := by
    have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
    have h6 : Real.sqrt 6 * Real.sqrt 6 = 6 := Real.mul_self_sqrt (by norm_num)
    have hn2 : Real.sqrt 2 ≠ 0 := by positivity
    have hn6 : Real.sqrt 6 ≠ 0 := by positivity
    ext i; fin_cases i <;> simp <;> field_simp <;> nlinarith

def tangentRealBasis : Basis (Fin 2) ℝ Tangent := (Pi.basisFun ℝ (Fin 2)).map tangentMap

def tangentLattice : Submodule ℤ Tangent := Submodule.span ℤ (Set.range tangentRealBasis)

theorem tangent_covolume : ZLattice.covolume tangentLattice = Real.sqrt 3 := by
  change ZLattice.covolume (Submodule.span ℤ (Set.range tangentRealBasis)) = _
  rw [ZLattice.covolume_eq_measure_fundamentalDomain (Submodule.span ℤ (Set.range tangentRealBasis)) volume
    (ZSpan.isAddFundamentalDomain tangentRealBasis volume), ZSpan.volume_real_fundamentalDomain]
  rw [Matrix.det_fin_two]
  simp [tangentRealBasis, tangentMap, Pi.basisFun_apply, Matrix.of_apply]
  have h2 : 0 < Real.sqrt 2 := by positivity
  have h6 : 0 < Real.sqrt 6 := by positivity
  have h3 : 0 < Real.sqrt 3 := by positivity
  have hmul : Real.sqrt 2 * Real.sqrt 6 = 2 * Real.sqrt 3 := by
    rw [← Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 2)]
    norm_num
    rw [show (12 : ℝ) = 4 * 3 by norm_num, Real.sqrt_mul (by norm_num : (0 : ℝ) ≤ 4)]
    norm_num
  have he : (Real.sqrt 2)⁻¹ * (3 / Real.sqrt 6) -
      3 / Real.sqrt 6 * (-1 / Real.sqrt 2) = 6 / (Real.sqrt 2 * Real.sqrt 6) := by
    field_simp
    <;> ring
  rw [he, abs_of_pos (by positivity), hmul]
  have hsq : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  field_simp
  nlinarith

end AliceLayers

namespace AliceLayers

theorem tangentMap_layerPoint (a b : ℤ) :
    tangentMap ![(a : ℝ), (b : ℝ)] =
      transverseCoordinates (fun i => (layerPoint 0 a b i : ℝ)) := by
  ext i
  fin_cases i <;> simp [tangentMap, transverseCoordinates, layerPoint, Matrix.cons_val_two,
    Matrix.vecHead, Matrix.vecTail] <;> ring

theorem tangentLattice_iff (q : Tangent) :
    q ∈ tangentLattice ↔ ∃ a b : ℤ, q = tangentMap ![(a : ℝ), (b : ℝ)] := by
  change q ∈ Submodule.span ℤ (Set.range tangentRealBasis) ↔ _
  rw [tangentRealBasis.mem_span_iff_repr_mem ℤ q]
  simp only [tangentRealBasis, Basis.map_repr, LinearEquiv.trans_apply, Pi.basisFun_repr,
    Set.mem_range]
  constructor
  · intro h
    obtain ⟨a, ha⟩ := h 0
    obtain ⟨b, hb⟩ := h 1
    refine ⟨a, b, ?_⟩
    apply tangentMap.symm.injective
    simp only [LinearEquiv.symm_apply_apply]
    ext i
    fin_cases i <;> simp_all
  · rintro ⟨a, b, rfl⟩ i
    fin_cases i <;> simp

end AliceLayers

namespace AliceLayers

theorem tangentLattice_is_integer_plane (q : Tangent) :
    q ∈ tangentLattice ↔ ∃ x : Lattice, planeIndex x = 0 ∧
      q = transverseCoordinates (fun i => (x i : ℝ)) := by
  rw [tangentLattice_iff]
  constructor
  · rintro ⟨a, b, rfl⟩
    exact ⟨layerPoint 0 a b, planeIndex_layerPoint 0 a b, tangentMap_layerPoint a b⟩
  · rintro ⟨x, hx, hq⟩
    refine ⟨x 0, x 1, ?_⟩
    rw [tangentMap_layerPoint, ← hx, layerPoint_coordinates]
    exact hq

end AliceLayers

namespace AliceLayers

/-- The chosen transverse coordinates preserve the Euclidean norm on the plane. -/
theorem tangent_coordinates_preserve_norm (x : Lattice) (hx : planeIndex x = 0) :
    latticeLayerRadiusSquared x = sqNorm x := by
  have hn : normalFrequency (fun i => (x i : ℝ)) = 0 := by
    simp [normalFrequency, planeIndex, Fin.sum_univ_three] at hx ⊢
    exact_mod_cast hx
  have hf := frame_norm_identity (fun i => (x i : ℝ))
  simpa [hn, latticeLayerRadiusSquared, sqNorm] using hf

end AliceLayers

namespace AliceLayers

theorem transverse_plane_norm (v : Frequency) (hv : ∑ i, v i = 0) :
    (∑ i, (transverseCoordinates v i)^2) = ∑ i, v i ^ 2 := by
  have hn : normalFrequency v = 0 := by simp [normalFrequency, hv]
  simpa [hn] using frame_norm_identity v

end AliceLayers
