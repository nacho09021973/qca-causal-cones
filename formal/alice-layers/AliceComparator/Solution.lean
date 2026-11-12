import AliceComparator.Challenge
import AliceLayers.Basic

namespace AliceSolution
theorem phase_sub_center : AliceChallenge.PhaseSubCenter := @AliceLayers.phase_sub_center
theorem transverse_phase : AliceChallenge.TransversePhase := @AliceLayers.transverse_phase
theorem finite_phase_bound : AliceChallenge.FinitePhaseBound := @AliceLayers.finite_phase_bound
theorem layer_profile_identity : AliceChallenge.LayerProfileIdentity := @AliceLayers.layer_profile_identity
theorem prefactor_identity : AliceChallenge.PrefactorIdentity := @AliceLayers.prefactor_identity
theorem frame_norm_identity : AliceChallenge.FrameNormIdentity := @AliceLayers.frame_norm_identity
theorem support_faithfulness : AliceChallenge.SupportFaithfulnessClaim := @AliceLayers.support_faithfulness
theorem lattice_layer_decomposition : AliceChallenge.LayerCoordinateDecomposition :=
  @AliceLayers.lattice_layer_decomposition
theorem lattice_layer_domain : AliceChallenge.LayerCoordinateDomain :=
  @AliceLayers.lattice_layer_domain
end AliceSolution
