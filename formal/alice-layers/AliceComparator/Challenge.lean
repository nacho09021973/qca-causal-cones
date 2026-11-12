import Mathlib

/-!
Readable statements, independent of all project proof modules.
Definitions copied from AliceLayers/Definitions.lean and Targets.lean.
No project structures are imported. Type names below are only local notation.
Pattern: herramientas/lean, source commit 83c04f9.
Coverage: exactly the nine ingredients in CLAIMS.md; no asymptotic theorem.
-/
noncomputable section
open scoped BigOperators
namespace AliceChallenge

local notation "Lattice" => (Fin 3 → ℤ)
local notation "Frequency" => (Fin 3 → ℝ)
local notation "Tangent" => (Fin 2 → ℝ)

def sqNorm (x : Lattice) : ℝ := ∑ i, (x i : ℝ)^2
def normalFrequency (η : Frequency) : ℝ := (∑ i, η i) / Real.sqrt 3
def centerCoordinate (N : ℕ) : ℝ := (N : ℝ) / (4 * Real.sqrt 3)
def phase (N : ℕ) (η : Frequency) (x : Lattice) : ℝ :=
  ∑ i, η i * ((x i : ℝ) - centerCoordinate N)
def uncenteredPhase (η : Frequency) (x : Lattice) : ℝ := ∑ i, η i * (x i : ℝ)
def latticeBox (N : ℕ) : Finset Lattice :=
  Fintype.piFinset fun _ => Finset.Icc (-(N : ℤ)) (N : ℤ)
def aliceSites (N : ℕ) : Finset Lattice :=
  (latticeBox N).filter fun x => 16 * sqNorm x ≤ (N : ℝ)^2
def transverseCoordinates (η : Frequency) : Tangent :=
  ![(η 0-η 1)/Real.sqrt 2, (η 0+η 1-2*η 2)/Real.sqrt 6]
def latticeLayerDepth (N : ℕ) (x : Lattice) : ℝ :=
  (N : ℝ)/4 - (∑ i, (x i : ℝ))/Real.sqrt 3
def latticeLayerRadiusSquared (x : Lattice) : ℝ :=
  ∑ i, transverseCoordinates (fun j => (x j : ℝ)) i ^ 2
def SupportFaithfulness : Prop :=
  ∀ N : ℕ, ∀ x : Lattice, x ∈ aliceSites N ↔ 16 * sqNorm x ≤ (N : ℝ)^2

def PhaseSubCenter : Prop := ∀ (N : ℕ) (η : Frequency) (x : Lattice),
  phase N η x = uncenteredPhase η x - centerCoordinate N * ∑ i, η i
def TransversePhase : Prop := ∀ (N : ℕ) (η : Frequency) (x : Lattice)
  (_h : ∑ i, η i = 0), phase N η x = uncenteredPhase η x
def FinitePhaseBound : Prop := ∀ {ι : Type*} (s : Finset ι) (p w : ι → ℝ),
  ‖∑ x ∈ s, Complex.exp (Complex.I * (p x : ℂ)) * (w x : ℂ)‖ ≤ ∑ x ∈ s, |w x|
def LayerProfileIdentity : Prop := ∀ (n δ q : ℝ) (_hn : n ≠ 0),
  (1 - 16 * ((n/4-δ)^2+q) / n^2)^2 =
    (64/n^2) * (δ - δ^2/(2*(n/4)) - q/(2*(n/4)))^2
def PrefactorIdentity : Prop := ∀ (n φ : ℝ) (_hn : n ≠ 0),
  (1/Real.sqrt 3) * (32*Real.pi/n^2) * (1/(n*Real.sqrt n)) * φ * (n/2) =
    (16*Real.pi/Real.sqrt 3) * φ * (1/(n^2*Real.sqrt n))
def FrameNormIdentity : Prop := ∀ η : Frequency,
  (normalFrequency η)^2 + ∑ i, (transverseCoordinates η i)^2 = ∑ i, η i ^ 2
def SupportFaithfulnessClaim : Prop := SupportFaithfulness
def LayerCoordinateDecomposition : Prop := ∀ (N : ℕ) (x : Lattice),
  sqNorm x = ((N : ℝ)/4 - latticeLayerDepth N x)^2 + latticeLayerRadiusSquared x
def LayerCoordinateDomain : Prop := ∀ (N : ℕ), 0 < N → ∀ x : Lattice,
  x ∈ aliceSites N ↔ 0 ≤ latticeLayerDepth N x ∧
    latticeLayerDepth N x ≤ (N : ℝ)/2 ∧
    latticeLayerRadiusSquared x ≤ latticeLayerDepth N x * ((N : ℝ)/2-latticeLayerDepth N x)

end AliceChallenge
