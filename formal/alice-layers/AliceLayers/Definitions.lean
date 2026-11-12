import Mathlib

/-! Exact scalar definitions from the frozen ir-corona.tex.
Definitions are not proofs of integrability, summability, or asymptotics.
-/
noncomputable section
open scoped BigOperators
open MeasureTheory

namespace AliceLayers

abbrev Lattice := Fin 3 → ℤ
abbrev Frequency := Fin 3 → ℝ
abbrev Tangent := Fin 2 → ℝ

def sqNorm (x : Lattice) : ℝ := ∑ i, (x i : ℝ)^2
def frequencyNorm (η : Frequency) : ℝ := Real.sqrt (∑ i, η i ^ 2)
def planeIndex (x : Lattice) : ℤ := ∑ i, x i
def normalFrequency (η : Frequency) : ℝ := (∑ i, η i) / Real.sqrt 3
def centerCoordinate (N : ℕ) : ℝ := (N : ℝ) / (4 * Real.sqrt 3)
def phase (N : ℕ) (η : Frequency) (x : Lattice) : ℝ :=
  ∑ i, η i * ((x i : ℝ) - centerCoordinate N)
def uncenteredPhase (η : Frequency) (x : Lattice) : ℝ := ∑ i, η i * (x i : ℝ)

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
def diagnosticTilt : ℝ := (7357528144 : ℝ) / 10000000000

def tiltWeight (N : ℕ) (t : ℝ) (x : Lattice) : ℝ :=
  Real.exp (t * ((planeIndex x : ℝ) - Real.sqrt 3 * (N : ℝ)/4))
def amplitude (N : ℕ) (t : ℝ) (η : Frequency) : ℂ :=
  ∑ x ∈ aliceSites N,
    Complex.exp (Complex.I * (phase N η x : ℂ)) *
      ((tiltWeight N t x * profileS N x * resource N x : ℝ) : ℂ)

def theta (N : ℕ) : ℝ := Int.fract (Real.sqrt 3 * (N : ℝ)/4)
def transverseCoordinates (η : Frequency) : Tangent :=
  ![(η 0-η 1)/Real.sqrt 2, (η 0+η 1-2*η 2)/Real.sqrt 6]
def latticeLayerDepth (N : ℕ) (x : Lattice) : ℝ :=
  (N : ℝ)/4 - (∑ i, (x i : ℝ))/Real.sqrt 3
def latticeLayerRadiusSquared (x : Lattice) : ℝ :=
  ∑ i, transverseCoordinates (fun j => (x j : ℝ)) i ^ 2
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

end AliceLayers
