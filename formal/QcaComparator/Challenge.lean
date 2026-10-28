import Mathlib

/-!
# Challenge: the statement of Theorem 4.1, apart from its proof

This file is the only one a reviewer needs to read to know what the Lean
development claims.  It imports Mathlib and nothing from `QcaFormal`: every
definition used by the statements is restated here, so the claim does not rest
on trusting definitions buried in the proof files.  `QcaComparator.Solution`
proves these `Prop`s from the `QcaFormal` theorems; the copies below must be
definitionally equal to the originals, otherwise `Solution` does not compile.

Pattern taken from `Comparator/Challenge.lean` of AxiomMath/CFSG (commit
`69cb972`), adapted to Lean v4.31.0 without the external `comparator` tool:
statements are `Prop` definitions instead of `sorry` theorems, and the axiom
check is `QcaComparator.Axioms`.
-/

noncomputable section

open AddMonoidAlgebra Finset Complex

namespace QcaChallenge

abbrev Z3 := Fin 3 → ℤ
abbrev Lau := AddMonoidAlgebra ℂ Z3

/-- Monomial `e^{i p·d}`. -/
def X (d : Z3) : Lau := single d 1

/-- Unit vector `e_j`. -/
def ej (j : Fin 3) : Z3 := Pi.single j 1

/-- `cos p_j`. -/
def cL (j : Fin 3) : Lau := (1 / 2 : ℂ) • (X (ej j) + X (-ej j))

/-- `sin p_j`. -/
def sL (j : Fin 3) : Lau := (1 / (2 * I) : ℂ) • (X (ej j) - X (-ej j))

/-- The symbol `S(p)` of eq. (2) (indices `0,1,2` for the paper's `1,2,3`). -/
def Ssym : Matrix (Fin 2) (Fin 2) Lau :=
  !![cL 0 * cL 1 * X (-ej 2), cL 0 * sL 1 - I • sL 0;
     -(cL 0 * sL 1) - I • sL 0, cL 0 * cL 1 * X (ej 2)]

/-- The `N`-step kernel `G_N(d) = (S^N)_{y,x}` with `d = y - x`. -/
def kernel (N : ℕ) (d : Z3) : Matrix (Fin 2) (Fin 2) ℂ := fun i j => (Ssym ^ N) i j d

/-- Alice's region `𝒜_N = ℤ³ ∩ B̄(0, N/4)`. -/
def inA (N : ℕ) (x : Z3) : Prop := 16 * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ≤ (N : ℤ) ^ 2

/-- Bob's region `ℬ_N = ℤ³ ∩ B̄(N(1,1,1), N/4)`. -/
def inB (N : ℕ) (y : Z3) : Prop :=
  16 * ((y 0 - N) ^ 2 + (y 1 - N) ^ 2 + (y 2 - N) ^ 2) ≤ (N : ℤ) ^ 2

instance (N : ℕ) : DecidablePred (inA N) := fun _ => by unfold inA; infer_instance

instance (N : ℕ) : DecidablePred (inB N) := fun _ => by unfold inB; infer_instance

/-- Integer points of `𝒜_N` as a finset. -/
def regA (N : ℕ) : Finset Z3 :=
  (Fintype.piFinset fun _ => Finset.Icc (-(N : ℤ)) N).filter (inA N)

/-- Integer points of `ℬ_N` as a finset. -/
def regB (N : ℕ) : Finset Z3 :=
  (Fintype.piFinset fun _ => Finset.Icc (0 : ℤ) (2 * N)).filter (inB N)

/-- The operator `P_ℬ S^N P_𝒜`: `(Kψ)(y)_i = ∑_{x ∈ 𝒜} ∑_j G_N(y-x)_{ij} ψ(x)_j`. -/
def Kop (N : ℕ) (ψ : Z3 → Fin 2 → ℂ) (y : Z3) (i : Fin 2) : ℂ :=
  ∑ x ∈ regA N, ∑ j, kernel N (y - x) i j * ψ x j

/-- Squared ℓ² norm over a region. -/
def l2sq (s : Finset Z3) (ψ : Z3 → Fin 2 → ℂ) : ℝ := ∑ x ∈ s, ∑ j, ‖ψ x j‖ ^ 2

/-- **Theorem 4.1, operator form.**  For `N ≥ 2`,
`‖P_ℬ S^N P_𝒜 ψ‖² ≤ (4 N^4 · 2^{-(1-√3/2)N})² ‖ψ‖²` on ℓ²(𝒜_N; ℂ²). -/
def TNBound : Prop :=
  ∀ (N : ℕ), 2 ≤ N → ∀ (ψ : Z3 → Fin 2 → ℂ),
    l2sq (regB N) (Kop N ψ)
      ≤ (4 * (N : ℝ) ^ 4 * (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * (N : ℝ))) ^ 2 *
          l2sq (regA N) ψ

/-- **Operational step.**  If Bob's two amplitudes differ by at most `2T` and
the effect has norm `≤ 1`, then the signal is at most `4T`. -/
def DeltaLeFourT : Prop :=
  ∀ (H : Type) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (Eop : H →L[ℂ] H), ‖Eop‖ ≤ 1 → ∀ (v₀ v₁ : H), ‖v₀‖ ≤ 1 → ‖v₁‖ ≤ 1 →
    ∀ (T : ℝ), ‖v₁ - v₀‖ ≤ 2 * T →
      ‖(inner ℂ v₁ (Eop v₁)) - inner ℂ v₀ (Eop v₀)‖ ≤ 4 * T

end QcaChallenge
