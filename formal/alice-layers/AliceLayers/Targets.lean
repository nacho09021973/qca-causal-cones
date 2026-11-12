import AliceLayers.Definitions

/-! These are OPEN propositions, not asserted theorems or axioms. -/
noncomputable section
namespace AliceLayers

/-- Scalar Alice part of Layers(b), with uniform constants and an asymptotic N₀.
The Fourier integrals and depth sum have explicit analytic well-definedness obligations.
This def does NOT provide a proof. -/
def AliceLayersB : Prop :=
  ∃ r₀ : ℝ, 0 < r₀ ∧ ∃ C : ℝ, 0 ≤ C ∧ ∃ N₀ : ℕ, 2 ≤ N₀ ∧
    ∀ N : ℕ, N₀ ≤ N → ∀ η : Frequency, frequencyNorm η ≤ r₀ →
      Summable (depthTerm criticalTilt (theta N) (tau N η)) ∧
      ∃ E : ℂ,
        ‖E‖ ≤ C * (Real.rpow (N : ℝ) (-(1 : ℝ)/2) + |normalFrequency η|) ∧
        amplitude N criticalTilt η =
          (leadingScale N : ℂ) * (sPlus criticalTilt (theta N) (tau N η) + E)

/-- Integrability must not be inferred from Bochner integral's default value. OPEN. -/
def ProfileIntegrability : Prop :=
  ∀ δ : ℝ, 0 ≤ δ → ∀ τ : Tangent, MeasureTheory.Integrable (psiIntegrand δ τ)

/-- Exact finite support obligation; proved by Basic.support_faithfulness. -/
def SupportFaithfulness : Prop :=
  ∀ N : ℕ, ∀ x : Lattice, x ∈ aliceSites N ↔ 16 * sqNorm x ≤ (N : ℝ)^2

end AliceLayers
