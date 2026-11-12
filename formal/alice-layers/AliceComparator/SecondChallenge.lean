import Mathlib

noncomputable section
open MeasureTheory
namespace AliceSecondChallenge

def positiveSquare (z : ℝ) : ℝ := (max z 0)^2

def cutoffSecond (δ x y : ℝ) : ℝ :=
  if 0 < δ-y^2-x^2 then 12*y^2 - 4*(δ-x^2) else 0

def SecondDerivativeAE : Prop := ∀ δ x : ℝ,
    (fun y => deriv (deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2))) y) =ᵐ[volume]
      cutoffSecond δ x

def SecondDerivativeIntegrable : Prop := ∀ δ x : ℝ,
    Integrable (deriv (deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2))))

end AliceSecondChallenge
