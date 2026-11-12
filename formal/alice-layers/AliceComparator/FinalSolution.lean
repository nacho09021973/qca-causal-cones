import AliceComparator.FinalChallenge
import AliceLayers.Assembly

set_option maxHeartbeats 1000000
namespace AliceFinalSolution

theorem FullScalarClaim : AliceFinalChallenge.FullScalarClaim :=
  @AliceLayers.aliceLayersB_proved

theorem ExplicitWitnessesClaim : AliceFinalChallenge.ExplicitWitnessesClaim :=
  @AliceLayers.aliceLayersB_explicit_witnesses

theorem BoundaryPositiveClaim : AliceFinalChallenge.BoundaryPositiveClaim :=
  @AliceLayers.boundaryResource_pos

theorem BoundaryIntegralClaim : AliceFinalChallenge.BoundaryIntegralClaim :=
  @AliceLayers.boundaryResource_eq_paper_integral

theorem PhaseSignClaim : AliceFinalChallenge.PhaseSignClaim :=
  @AliceLayers.normalPhaseError_eq_difference

theorem PhaseUniformClaim : AliceFinalChallenge.PhaseUniformClaim :=
  @AliceLayers.phase_error_uniform_exists

theorem ActiveIndicesClaim : AliceFinalChallenge.ActiveIndicesClaim :=
  @AliceLayers.activeDepthIndices_membership

theorem CompletionSignClaim : AliceFinalChallenge.CompletionSignClaim :=
  @AliceLayers.depthCompletionError_eq_difference

theorem CompletionUniformClaim : AliceFinalChallenge.CompletionUniformClaim :=
  @AliceLayers.completion_error_uniform_exists

theorem NormalizedIdentityClaim : AliceFinalChallenge.NormalizedIdentityClaim :=
  @AliceLayers.normalizedRemainder_identity

theorem NormalizedUniformClaim : AliceFinalChallenge.NormalizedUniformClaim :=
  @AliceLayers.normalized_error_uniform_exists

end AliceFinalSolution
