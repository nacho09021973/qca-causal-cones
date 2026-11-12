import AliceComparator.NewSolution
import AliceComparator.AssertAxioms

/-- info: 7 theorems use only propext, Classical.choice, Quot.sound -/
#guard_msgs in
#assert_standard_axioms
  AliceNewSolution.positiveSquareDerivative AliceNewSolution.positiveSquareC1
  AliceNewSolution.sectionDerivative AliceNewSolution.sectionBoundary AliceNewSolution.psiSliceC1
  AliceNewSolution.psiFourierAll AliceNewSolution.psiFourierBound
