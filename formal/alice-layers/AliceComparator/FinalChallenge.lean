import Mathlib

/-!
Final scalar comparator. Imports no project modules or project structures.
Definitions copied verbatim from the manifest final_comparator_sources.json.
Claim selection: block 5 of ORDEN_TRABAJO_2026-11-11.md, not all auxiliary lemmas.
Source herramientas: 8da0e09231ca9d7d6b6d5ea8861df3777be5ab18 plus local blocks 4 and 5.
This file can be read independently of all implementation proof modules.
-/
noncomputable section
open scoped BigOperators
open MeasureTheory
namespace AliceFinalChallenge

local notation "Lattice" => (Fin 3 → ℤ)
local notation "Frequency" => (Fin 3 → ℝ)
local notation "Tangent" => (Fin 2 → ℝ)

def sqNorm (x : Lattice) : ℝ := ∑ i, (x i : ℝ)^2

def frequencyNorm (η : Frequency) : ℝ := Real.sqrt (∑ i, η i ^ 2)

def planeIndex (x : Lattice) : ℤ := ∑ i, x i

def normalFrequency (η : Frequency) : ℝ := (∑ i, η i) / Real.sqrt 3

def centerCoordinate (N : ℕ) : ℝ := (N : ℝ) / (4 * Real.sqrt 3)

def phase (N : ℕ) (η : Frequency) (x : Lattice) : ℝ :=
  ∑ i, η i * ((x i : ℝ) - centerCoordinate N)

def latticeBox (N : ℕ) : Finset Lattice :=
  Fintype.piFinset fun _ => Finset.Icc (-(N : ℤ)) (N : ℤ)

def aliceSites (N : ℕ) : Finset Lattice :=
  (latticeBox N).filter fun x => 16 * sqNorm x ≤ (N : ℝ)^2

def cutoff (N : ℕ) (x : Lattice) : ℝ := max (1 - 16 * sqNorm x / (N : ℝ)^2) 0

def profileF (N : ℕ) (x : Lattice) : ℝ := (cutoff N x)^2

def profileS (N : ℕ) (x : Lattice) : ℝ := Real.sin (Real.pi / 2 * profileF N x)

def cResource : ℝ := Real.sqrt 3465 / (64 * Real.pi^2)

def phi0 (ρ : ℝ) : ℝ :=
  4 * Real.pi * cResource * ∫ k in (0 : ℝ)..1,
    k^2 * (1-k^2)^2 * Real.sinc (k*ρ)

def resource (N : ℕ) (x : Lattice) : ℝ :=
  Real.rpow (N : ℝ) (-(3 : ℝ)/2) * phi0 (Real.sqrt (sqNorm x) / (N : ℝ))

def boundaryResource : ℝ := phi0 (1/4)

def alpha : ℝ := 1 - 1 / (2 * Real.sqrt 3)

def criticalCoshSquared : ℝ :=
  alpha * (alpha + Real.sqrt (4-3*alpha^2)) / (2*(1-alpha^2))

def criticalTilt : ℝ :=
  Real.log (Real.sqrt criticalCoshSquared + Real.sqrt (criticalCoshSquared-1))

def tiltWeight (N : ℕ) (t : ℝ) (x : Lattice) : ℝ :=
  Real.exp (t * ((planeIndex x : ℝ) - Real.sqrt 3 * (N : ℝ)/4))

def amplitude (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ x ∈ aliceSites N,
    Complex.exp (Complex.I * (phase N η x : ℂ)) *
      ((tiltWeight N t x * profileS N x * resource N x : ℝ) : ℂ)

def theta (N : ℕ) : ℝ := Int.fract (Real.sqrt 3 * (N : ℝ)/4)

def transverseCoordinates (η : Frequency) : Tangent :=
  ![(η 0-η 1)/Real.sqrt 2, (η 0+η 1-2*η 2)/Real.sqrt 6]

def tau (N : ℕ) (η : Frequency) : Tangent :=
  fun i => Real.sqrt ((N : ℝ)/2) * transverseCoordinates η i

def psiIntegrand (δ : ℝ) (τ σ : Tangent) : ℂ :=
  (((max (δ - ∑ i, σ i ^ 2) 0)^2 : ℝ) : ℂ) *
    Complex.exp (Complex.I * ((∑ i, τ i * σ i : ℝ) : ℂ))

def psi (δ : ℝ) (τ : Tangent) : ℂ := ∫ σ : Tangent, psiIntegrand δ τ σ

def depthTerm (t θ : ℝ) (τ : Tangent) (j : ℕ) : ℂ :=
  ((Real.exp (-t * (θ + (j : ℝ))) : ℝ) : ℂ) * psi ((θ + (j : ℝ))/Real.sqrt 3) τ

def sPlus (t θ : ℝ) (τ : Tangent) : ℂ := ∑' j : ℕ, depthTerm t θ τ j

def leadingScale (N : ℕ) : ℝ :=
  Real.rpow (N : ℝ) (-(5 : ℝ)/2) * (16*Real.pi/Real.sqrt 3) * boundaryResource

def indexedLayerDepth (N : ℕ) (k : ℤ) : ℝ := (N : ℝ)/4-(k : ℝ)/Real.sqrt 3

def layerGlobalFactor (N : ℕ) (t : ℝ) (η : Frequency) (k : ℤ) : ℂ :=
  Complex.exp (Complex.I * ((normalFrequency η * ((k : ℝ)/Real.sqrt 3-(N : ℝ)/4) : ℝ) : ℂ)) *
    ((Real.exp (t*((k : ℝ)-Real.sqrt 3*(N : ℝ)/4)) : ℝ) : ℂ)

def layerNaturalIndex (N : ℕ) (k : ℤ) : ℕ := (⌊Real.sqrt 3*(N : ℝ)/4⌋-k).toNat

def geometricZeroModeSum (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex, layerGlobalFactor N t η k * psi (indexedLayerDepth N k) (tau N η)

def unphasedZeroModeSum (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex,
    depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)

def normalPhaseError (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ k ∈ (aliceSites N).image planeIndex,
    (Complex.exp (Complex.I * ((-normalFrequency η*indexedLayerDepth N k : ℝ) : ℂ))-1) *
      depthTerm t (theta N) (tau N η) (layerNaturalIndex N k)

def depthPlaneIndex (N j : ℕ) : ℤ := ⌊Real.sqrt 3*(N : ℝ)/4⌋-(j : ℤ)

def activeDepthIndices (N : ℕ) : Finset ℕ :=
  ((aliceSites N).image planeIndex).image (layerNaturalIndex N)

def depthCompletionError (N : ℕ) (t : ℝ) (τ : Tangent) : ℂ :=
  ∑' j : {j : ℕ // j ∉ activeDepthIndices N}, depthTerm t (theta N) τ j

def normalizedRemainder (N : ℕ) (η : Frequency) : ℂ :=
  (amplitude N criticalTilt η-(leadingScale N : ℂ)*sPlus criticalTilt (theta N) (tau N η)) /
    (leadingScale N : ℂ)

def AliceLayersB : Prop :=
  ∃ r₀ : ℝ, 0 < r₀ ∧ ∃ C : ℝ, 0 ≤ C ∧ ∃ N₀ : ℕ, 2 ≤ N₀ ∧
    ∀ N : ℕ, N₀ ≤ N → ∀ η : Frequency, frequencyNorm η ≤ r₀ →
      Summable (depthTerm criticalTilt (theta N) (tau N η)) ∧
      ∃ E : ℂ,
        ‖E‖ ≤ C * (Real.rpow (N : ℝ) (-(1 : ℝ)/2) + |normalFrequency η|) ∧
        amplitude N criticalTilt η =
          (leadingScale N : ℂ) * (sPlus criticalTilt (theta N) (tau N η) + E)

def FullScalarClaim : Prop :=
  AliceLayersB

def ExplicitWitnessesClaim : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 2 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 →
      Summable (depthTerm criticalTilt (theta N) (tau N η)) ∧
      ∃ E : ℂ, ‖E‖ ≤ C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|) ∧
        amplitude N criticalTilt η = (leadingScale N : ℂ)*(sPlus criticalTilt (theta N) (tau N η)+E)

def BoundaryPositiveClaim : Prop :=
  0 < boundaryResource

def BoundaryIntegralClaim : Prop :=
  boundaryResource = cResource*(16*Real.pi*
      ∫ k in (0 : ℝ)..1, k*(1-k^2)^2*Real.sin (k/4))

def PhaseSignClaim : Prop :=
  ∀ N : ℕ, 0 < N → ∀ t : ℝ, ∀ η : Frequency,
      normalPhaseError N t η = geometricZeroModeSum N t η-unphasedZeroModeSum N t η

def PhaseUniformClaim : Prop :=
  ∀ t : ℝ, 0 < t →
      ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ η : Frequency,
        ‖normalPhaseError N t η‖ ≤ C*|normalFrequency η|

def ActiveIndicesClaim : Prop :=
  ∀ N : ℕ, 0 < N → ∀ j : ℕ,
      j ∈ activeDepthIndices N ↔ depthPlaneIndex N j ∈ (aliceSites N).image planeIndex

def CompletionSignClaim : Prop :=
  ∀ N : ℕ, 0 < N → ∀ t : ℝ, 0 < t → ∀ η : Frequency,
      depthCompletionError N t (tau N η) = sPlus t (theta N) (tau N η)-unphasedZeroModeSum N t η

def CompletionUniformClaim : Prop :=
  ∀ t : ℝ, 0 < t →
      ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ τ : Tangent,
        ‖depthCompletionError N t τ‖ ≤ C/(N : ℝ)

def NormalizedIdentityClaim : Prop :=
  ∀ N : ℕ, 0 < N → ∀ η : Frequency,
      amplitude N criticalTilt η = (leadingScale N : ℂ)*
        (sPlus criticalTilt (theta N) (tau N η)+normalizedRemainder N η)

def NormalizedUniformClaim : Prop :=
  ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 1 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 → ‖normalizedRemainder N η‖ ≤
        C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|)

end AliceFinalChallenge
