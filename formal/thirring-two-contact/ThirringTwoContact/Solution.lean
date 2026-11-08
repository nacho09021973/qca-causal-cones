import ThirringTwoContact.Challenge

set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace ThirringSolution
theorem first_gate : ThirringChallenge.FirstGate := by decide
theorem free_gram : ThirringChallenge.FreeGram := by decide
theorem actual_gram : ThirringChallenge.ActualGram := by decide
theorem second_compression : ThirringChallenge.SecondCompression := by decide
theorem defect_gram : ThirringChallenge.DefectGram := by decide
theorem projector_identity : ThirringChallenge.ProjectorIdentity := by decide
theorem witness_eigenvector : ThirringChallenge.WitnessEigenvector := by decide
theorem strict_column_defect : ThirringChallenge.StrictColumnDefect := by decide
theorem no_wrap : ThirringChallenge.NoWrap := by decide
end ThirringSolution
