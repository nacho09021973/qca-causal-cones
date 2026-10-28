import QcaComparator.Challenge
import QcaFormal.Theorem41

/-!
# Solution: the `QcaFormal` theorems prove the challenge statements

Each proof is the corresponding `QcaFormal` theorem applied as is; it type-checks
only because the definitions restated in `QcaComparator.Challenge` unfold to
the same terms as those in `QcaFormal`.
-/

namespace QcaComparator

theorem tn_bound : QcaChallenge.TNBound :=
  fun N hN ψ => QcaFormal.TN_bound N hN ψ

theorem delta_le_four_T : QcaChallenge.DeltaLeFourT :=
  fun _ _ _ Eop hE v₀ v₁ h₀ h₁ _ hT => QcaFormal.delta_le_four_T Eop hE v₀ v₁ h₀ h₁ hT

end QcaComparator
