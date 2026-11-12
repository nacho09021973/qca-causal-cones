import AliceComparator.NewChallenge
import AliceLayers.SectionRegularity

namespace AliceNewSolution

theorem positiveSquareDerivative : AliceNewChallenge.PositiveSquareDerivative :=
  @AliceLayers.positiveSquare_hasDerivAt
theorem positiveSquareC1 : AliceNewChallenge.PositiveSquareC1 :=
  @AliceLayers.positiveSquare_contDiff_one
theorem sectionDerivative : AliceNewChallenge.SectionDerivative :=
  @AliceLayers.section_cutoff_derivative
theorem sectionBoundary : AliceNewChallenge.SectionBoundary :=
  @AliceLayers.section_boundary_derivative_zero
theorem psiSliceC1 : AliceNewChallenge.PsiSliceC1 := @AliceLayers.psiSlice_contDiff_one
theorem psiFourierAll : AliceNewChallenge.PsiFourierAll := @AliceLayers.psi_double_fourier
theorem psiFourierBound : AliceNewChallenge.PsiFourierBound := @AliceLayers.psiSlice_first_order_bound

end AliceNewSolution
