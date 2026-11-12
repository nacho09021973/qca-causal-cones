import AliceComparator.Solution
import AliceComparator.AssertAxioms

/-- info: 9 theorems use only propext, Classical.choice, Quot.sound -/
#guard_msgs in
#assert_standard_axioms
  AliceSolution.phase_sub_center AliceSolution.transverse_phase AliceSolution.finite_phase_bound
  AliceSolution.layer_profile_identity AliceSolution.prefactor_identity
  AliceSolution.frame_norm_identity AliceSolution.support_faithfulness
  AliceSolution.lattice_layer_decomposition AliceSolution.lattice_layer_domain
