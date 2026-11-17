import Mathlib.Analysis.Normed.Group.Basic

/- Conditional transfer of a physical evolution through an exact comparison
solution. This does NOT construct the scattering solution or prove its tails. -/
namespace ThirringWindow

 theorem transfer_bound {E : Type*} [SeminormedAddCommGroup E]
    (U : E → E) (x y target : E) (eIn eOut : ℝ)
    (preserve : ∀ a b, ‖U a - U b‖ = ‖a - b‖)
    (initial : ‖x - y‖ ≤ eIn)
    (final : ‖U y - target‖ ≤ eOut) :
    ‖U x - target‖ ≤ eIn + eOut := by
  calc
    ‖U x - target‖ ≤ ‖U x - U y‖ + ‖U y - target‖ := by
      have h : U x - target = (U x - U y) + (U y - target) := by abel
      rw [h]
      exact norm_add_le _ _
    _ = ‖x - y‖ + ‖U y - target‖ := by rw [preserve]
    _ ≤ eIn + eOut := add_le_add initial final

#print axioms transfer_bound
end ThirringWindow
