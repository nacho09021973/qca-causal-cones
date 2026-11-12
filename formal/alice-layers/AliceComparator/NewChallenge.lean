import Mathlib

/-! Independent statements for selected recent results. Copied definitions are
checked by verify.py. The local continuity lemma only constructs a ContinuousMap;
it does not assert any claim being compared. -/
noncomputable section
open scoped BigOperators FourierTransform
open MeasureTheory
namespace AliceNewChallenge

abbrev Tangent := Fin 2 → ℝ

def psiIntegrand (δ : ℝ) (τ σ : Tangent) : ℂ :=
  (((max (δ - ∑ i, σ i ^ 2) 0)^2 : ℝ) : ℂ) *
    Complex.exp (Complex.I * ((∑ i, τ i * σ i : ℝ) : ℂ))
def psi (δ : ℝ) (τ : Tangent) : ℂ := ∫ σ : Tangent, psiIntegrand δ τ σ

theorem psi_integrand_continuous (δ : ℝ) (τ : Tangent) :
    Continuous (psiIntegrand δ τ) := by
  unfold psiIntegrand
  fun_prop

def psiSlice (δ : ℝ) (τ : Tangent) (x : ℝ) : C(ℝ, ℂ) where
  toFun y := psiIntegrand δ τ ![y, x]
  continuous_toFun := by
    apply (psi_integrand_continuous δ τ).comp
    fun_prop

def shiftedTau (τ : Tangent) (u v : ℝ) : Tangent :=
  ![τ 0 - 2 * Real.pi * u, τ 1 - 2 * Real.pi * v]

def positiveSquare (z : ℝ) : ℝ := (max z 0)^2

def PositiveSquareDerivative : Prop := ∀ z : ℝ,
    HasDerivAt positiveSquare (2 * max z 0) z
def PositiveSquareC1 : Prop := ContDiff ℝ 1 positiveSquare
def SectionDerivative : Prop := ∀ δ x y : ℝ,
    HasDerivAt (fun t : ℝ => positiveSquare (δ - t^2 - x^2))
      (-4*y * max (δ-y^2-x^2) 0) y
def SectionBoundary : Prop := ∀ δ x y : ℝ, δ = y^2 + x^2 →
    deriv (fun t : ℝ => positiveSquare (δ-t^2-x^2)) y = 0
def PsiSliceC1 : Prop := ∀ (δ : ℝ) (τ : Tangent) (x : ℝ),
    ContDiff ℝ 1 (psiSlice δ τ x : ℝ → ℂ)
def PsiFourierAll : Prop := ∀ (δ : ℝ), 0 ≤ δ → ∀ (τ : Tangent) (u v : ℝ),
    𝓕 (fun x : ℝ => 𝓕 (psiSlice δ τ x : ℝ → ℂ) u) v = psi δ (shiftedTau τ u v)
def PsiFourierBound : Prop := ∀ (δ : ℝ), 0 ≤ δ → ∀ (τ : Tangent) (x u : ℝ),
    ‖(2 * Real.pi * Complex.I * u) * 𝓕 (psiSlice δ τ x : ℝ → ℂ) u‖ ≤
      ∫ y : ℝ, ‖deriv (psiSlice δ τ x : ℝ → ℂ) y‖

end AliceNewChallenge
