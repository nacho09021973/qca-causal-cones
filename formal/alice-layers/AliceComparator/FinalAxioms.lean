import AliceComparator.FinalSolution
import AliceComparator.AssertAxioms

/-- info: 11 theorems use only propext, Classical.choice, Quot.sound -/
#guard_msgs in
#assert_standard_axioms
  AliceFinalSolution.FullScalarClaim
  AliceFinalSolution.ExplicitWitnessesClaim
  AliceFinalSolution.BoundaryPositiveClaim
  AliceFinalSolution.BoundaryIntegralClaim
  AliceFinalSolution.PhaseSignClaim
  AliceFinalSolution.PhaseUniformClaim
  AliceFinalSolution.ActiveIndicesClaim
  AliceFinalSolution.CompletionSignClaim
  AliceFinalSolution.CompletionUniformClaim
  AliceFinalSolution.NormalizedIdentityClaim
  AliceFinalSolution.NormalizedUniformClaim
