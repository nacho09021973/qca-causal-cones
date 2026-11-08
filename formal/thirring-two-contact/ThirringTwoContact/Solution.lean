import ThirringTwoContact.Challenge

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace ThirringSolution
theorem first_gate : ThirringChallenge.FirstGate := by unfold ThirringChallenge.FirstGate; decide
theorem free_gram : ThirringChallenge.FreeGram := by unfold ThirringChallenge.FreeGram; decide
theorem actual_gram : ThirringChallenge.ActualGram := by unfold ThirringChallenge.ActualGram; decide
theorem second_compression : ThirringChallenge.SecondCompression := by unfold ThirringChallenge.SecondCompression; decide
theorem defect_gram : ThirringChallenge.DefectGram := by unfold ThirringChallenge.DefectGram; decide
theorem projector_identity : ThirringChallenge.ProjectorIdentity := by unfold ThirringChallenge.ProjectorIdentity; decide
theorem witness_eigenvector : ThirringChallenge.WitnessEigenvector := by unfold ThirringChallenge.WitnessEigenvector; decide
theorem strict_column_defect : ThirringChallenge.StrictColumnDefect := by unfold ThirringChallenge.StrictColumnDefect; decide
theorem no_wrap : ThirringChallenge.NoWrap := by unfold ThirringChallenge.NoWrap; decide
end ThirringSolution
