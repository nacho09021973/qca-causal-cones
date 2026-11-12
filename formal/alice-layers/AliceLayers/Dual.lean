import AliceLayers.PsiIntermediate

noncomputable section
open scoped BigOperators
namespace AliceLayers

/-- Reciprocal basis in cycles (the phase convention multiplies it by 2π). -/
def dualCoordinate (m n : ℝ) : Tangent :=
  ![Real.sqrt 2 * (m-n) / 2, Real.sqrt 6 * (m+n) / 6]

theorem dual_pairing (m n a b : ℝ) :
    (∑ i, dualCoordinate m n i * (tangentMap ![a,b]) i) = m*a + n*b := by
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  have h6 : Real.sqrt 6 * Real.sqrt 6 = 6 := Real.mul_self_sqrt (by norm_num)
  have hn2 : Real.sqrt 2 ≠ 0 := by positivity
  have hn6 : Real.sqrt 6 ≠ 0 := by positivity
  simp [dualCoordinate, tangentMap, Fin.sum_univ_two]
  field_simp
  ring_nf

theorem dual_pairing_translated (k : ℤ) (m n a b : ℝ) :
    (∑ i, dualCoordinate m n i * (layerShift k + tangentMap ![a,b]) i) =
      (∑ i, dualCoordinate m n i * layerShift k i) + m*a + n*b := by
  simp only [Pi.add_apply, mul_add, Finset.sum_add_distrib, dual_pairing]
  ring

end AliceLayers
