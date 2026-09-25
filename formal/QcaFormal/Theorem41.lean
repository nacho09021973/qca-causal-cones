import Mathlib
import QcaFormal.Kernel

/-!
# Theorem 4.1 of the paper (explicit upper bound)

* `sum_sub_ge`: every pair `x ∈ 𝒜_N`, `y ∈ ℬ_N` has `u·(y-x) ≥ (3 - √3/2) N`.
* `kernel_bound_regions`: `‖G_N(y-x)_{ij}‖ ≤ (33/32) N 2^{-(1-√3/2) N}`, i.e.
  `(33/32) N e^{-JN}` with `J = (1 - √3/2) log 2`.
* `TN_bound`: the block operator `P_ℬ S^N P_𝒜`, acting between the finite
  coordinate spaces of the two regions, has norm `≤ 4 N^4 e^{-JN}`, which
  implies the paper's `T_N ≤ 9 N^4 e^{-JN}`.
* `delta_le_four_T`: the operational step `δ ≤ 4 T`.
-/

noncomputable section

open Finset Complex

namespace QcaFormal

/-- Alice's region `𝒜_N = ℤ³ ∩ B̄(0, N/4)`. -/
def inA (N : ℕ) (x : Z3) : Prop := 16 * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ≤ (N : ℤ) ^ 2

/-- Bob's region `ℬ_N = ℤ³ ∩ B̄(N(1,1,1), N/4)`. -/
def inB (N : ℕ) (y : Z3) : Prop :=
  16 * ((y 0 - N) ^ 2 + (y 1 - N) ^ 2 + (y 2 - N) ^ 2) ≤ (N : ℤ) ^ 2

/-- `a + b + c ≤ √3 N / 4` whenever `16 (a² + b² + c²) ≤ N²`. -/
lemma sum_le_of_ball (a b c N : ℝ) (hN : 0 ≤ N)
    (h : 16 * (a ^ 2 + b ^ 2 + c ^ 2) ≤ N ^ 2) : a + b + c ≤ Real.sqrt 3 * N / 4 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : 0 ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  have hcs : (a + b + c) ^ 2 ≤ 3 * (a ^ 2 + b ^ 2 + c ^ 2) := by
    nlinarith [sq_nonneg (a - b), sq_nonneg (b - c), sq_nonneg (a - c)]
  have hsq : (a + b + c) ^ 2 ≤ (Real.sqrt 3 * N / 4) ^ 2 := by
    rw [div_pow, mul_pow, h3]; nlinarith
  have hpos : 0 ≤ Real.sqrt 3 * N / 4 := by positivity
  exact abs_le_of_sq_le_sq' hsq hpos |>.2

/-- Separation of the two regions along `u = (1,1,1)`. -/
lemma sum_sub_ge (N : ℕ) (x y : Z3) (hx : inA N x) (hy : inB N y) :
    (3 - Real.sqrt 3 / 2) * N ≤ ((y 0 - x 0 + (y 1 - x 1) + (y 2 - x 2) : ℤ) : ℝ) := by
  unfold inA at hx
  unfold inB at hy
  have hx' : 16 * (((x 0 : ℝ)) ^ 2 + ((x 1 : ℝ)) ^ 2 + ((x 2 : ℝ)) ^ 2) ≤ (N : ℝ) ^ 2 := by
    exact_mod_cast hx
  have hy' : 16 * ((((y 0 : ℝ)) - N) ^ 2 + (((y 1 : ℝ)) - N) ^ 2 + (((y 2 : ℝ)) - N) ^ 2)
      ≤ (N : ℝ) ^ 2 := by exact_mod_cast hy
  have hN : (0 : ℝ) ≤ N := Nat.cast_nonneg N
  have ha := sum_le_of_ball _ _ _ _ hN hx'
  have hb := sum_le_of_ball (N - (y 0 : ℝ)) (N - (y 1 : ℝ)) (N - (y 2 : ℝ)) N hN
    (by nlinarith [hy'])
  push_cast
  linarith

/-- Kernel bound between the two regions:
`‖G_N(y - x)_{ij}‖ ≤ (33/32) N 2^{-(1 - √3/2) N}` for `N ≥ 1`. -/
theorem kernel_bound_regions (n : ℕ) (x y : Z3) (hx : inA (n + 1) x) (hy : inB (n + 1) y)
    (i j : Fin 2) :
    ‖kernel (n + 1) (y - x) i j‖
      ≤ 33 / 32 * ((n + 1 : ℕ) : ℝ) * (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * ((n + 1 : ℕ) : ℝ)) := by
  set N : ℕ := n + 1 with hNdef
  have hb := kernel_entry_bound n (y - x) i j
  have hsep := sum_sub_ge N x y hx hy
  set s : ℤ := (y - x) 0 + (y - x) 1 + (y - x) 2 with hs
  have hs' : ((s : ℤ) : ℝ) = ((y 0 - x 0 + (y 1 - x 1) + (y 2 - x 2) : ℤ) : ℝ) := by
    simp [hs, Pi.sub_apply]
  -- 4^N · 2^{-s} = 2^{2N - s} ≤ 2^{-(1-√3/2) N}
  have hpow : (4 : ℝ) ^ N * (2 : ℝ) ^ (-s) ≤ (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * (N : ℝ)) := by
    have h4 : (4 : ℝ) ^ N = (2 : ℝ) ^ ((2 * N : ℕ) : ℝ) := by
      rw [Real.rpow_natCast]; rw [pow_mul]; norm_num
    rw [h4, ← Real.rpow_intCast, ← Real.rpow_add (by norm_num)]
    apply Real.rpow_le_rpow_of_exponent_le (by norm_num)
    push_cast
    rw [hs'] at *
    linarith
  calc ‖kernel N (y - x) i j‖
      ≤ 33 / 32 * (N : ℝ) * 4 ^ N * (2 : ℝ) ^ (-s) := hb
    _ = 33 / 32 * (N : ℝ) * ((4 : ℝ) ^ N * (2 : ℝ) ^ (-s)) := by ring
    _ ≤ 33 / 32 * (N : ℝ) * (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * (N : ℝ)) := by
        gcongr

/-! ### The block operator between the regions -/

instance (N : ℕ) : DecidablePred (inA N) := fun _ => by unfold inA; infer_instance

instance (N : ℕ) : DecidablePred (inB N) := fun _ => by unfold inB; infer_instance

/-- Integer points of `𝒜_N` as a finset. -/
def regA (N : ℕ) : Finset Z3 :=
  (Fintype.piFinset fun _ => Finset.Icc (-(N : ℤ)) N).filter (inA N)

/-- Integer points of `ℬ_N` as a finset. -/
def regB (N : ℕ) : Finset Z3 :=
  (Fintype.piFinset fun _ => Finset.Icc (0 : ℤ) (2 * N)).filter (inB N)

lemma mem_regA {N : ℕ} {x : Z3} : x ∈ regA N ↔ inA N x := by
  unfold regA
  rw [Finset.mem_filter, Fintype.mem_piFinset]
  constructor
  · exact fun h => h.2
  · intro h
    refine ⟨fun j => ?_, h⟩
    unfold inA at h
    rw [Finset.mem_Icc]
    have : x j ^ 2 ≤ (N : ℤ) ^ 2 := by
      fin_cases j <;> simp <;> nlinarith [sq_nonneg (x 0), sq_nonneg (x 1), sq_nonneg (x 2)]
    constructor <;> nlinarith [sq_nonneg (x j - N), sq_nonneg (x j + N)]

lemma mem_regB {N : ℕ} {y : Z3} : y ∈ regB N ↔ inB N y := by
  unfold regB
  rw [Finset.mem_filter, Fintype.mem_piFinset]
  constructor
  · exact fun h => h.2
  · intro h
    refine ⟨fun j => ?_, h⟩
    unfold inB at h
    rw [Finset.mem_Icc]
    have : (y j - N) ^ 2 ≤ (N : ℤ) ^ 2 := by
      fin_cases j <;> simp <;>
        nlinarith [sq_nonneg (y 0 - N), sq_nonneg (y 1 - N), sq_nonneg (y 2 - N)]
    have hb := abs_le_of_sq_le_sq' this (Nat.cast_nonneg N)
    constructor <;> linarith [hb.1, hb.2]

/-- `|x_j| ≤ N/4` coordinatewise on a ball of radius `N/4`, as `4|x_j| ≤ N`. -/
lemma coord_le_of_ball {N : ℕ} {a b c : ℤ} (h : 16 * (a ^ 2 + b ^ 2 + c ^ 2) ≤ (N : ℤ) ^ 2) :
    4 * |a| ≤ N := by
  have hN : (0 : ℤ) ≤ N := Nat.cast_nonneg N
  have ha : 16 * a ^ 2 ≤ (N : ℤ) ^ 2 := by nlinarith [sq_nonneg b, sq_nonneg c]
  have : (4 * |a|) ^ 2 ≤ (N : ℤ) ^ 2 := by rw [mul_pow, sq_abs]; linarith
  nlinarith [abs_nonneg a]

/-- Each region has at most `N^3` lattice points (`N ≥ 2`). -/
lemma card_regA_le (N : ℕ) (hN : 2 ≤ N) : ((regA N).card : ℝ) ≤ (N : ℝ) ^ 3 := by
  have hsub : regA N ⊆ Fintype.piFinset fun _ : Fin 3 => Finset.Icc (-((N : ℤ) / 4)) ((N : ℤ) / 4) := by
    intro x hx
    rw [mem_regA] at hx
    rw [Fintype.mem_piFinset]
    intro j
    rw [Finset.mem_Icc]
    unfold inA at hx
    have hj : 4 * |x j| ≤ N := by
      fin_cases j
      · exact coord_le_of_ball hx
      · exact coord_le_of_ball (a := x 1) (b := x 0) (c := x 2) (by linarith)
      · exact coord_le_of_ball (a := x 2) (b := x 0) (c := x 1) (by linarith)
    have a1 := neg_abs_le (x j)
    have a2 := le_abs_self (x j)
    constructor <;> omega
  have hc := Finset.card_le_card hsub
  rw [Fintype.card_piFinset, Finset.prod_const, Finset.card_univ, Fintype.card_fin,
    Int.card_Icc] at hc
  have hlen : ((N : ℤ) / 4 + 1 - -((N : ℤ) / 4)).toNat ≤ N := by omega
  calc ((regA N).card : ℝ) ≤ (((((N : ℤ) / 4 + 1 - -((N : ℤ) / 4)).toNat) ^ 3 : ℕ) : ℝ) := by
        exact_mod_cast hc
    _ ≤ (N : ℝ) ^ 3 := by push_cast; gcongr

lemma card_regB_le (N : ℕ) (hN : 2 ≤ N) : ((regB N).card : ℝ) ≤ (N : ℝ) ^ 3 := by
  -- translate by `-N(1,1,1)`
  have hinj : Set.InjOn (fun y : Z3 => fun j => y j - (N : ℤ)) (regB N : Set Z3) := by
    intro a _ b _ hab
    funext j
    have := congrFun hab j
    simpa using this
  have himg : (regB N).image (fun y : Z3 => fun j => y j - (N : ℤ)) ⊆ regA N := by
    intro x hx
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.mp hx
    rw [mem_regA]
    rw [mem_regB] at hy
    exact hy
  have := Finset.card_le_card himg
  rw [Finset.card_image_of_injOn hinj] at this
  calc ((regB N).card : ℝ) ≤ (regA N).card := by exact_mod_cast this
    _ ≤ (N : ℝ) ^ 3 := card_regA_le N hN

/-- The operator `P_ℬ S^N P_𝒜`: `(Kψ)(y)_i = ∑_{x ∈ 𝒜} ∑_j G_N(y-x)_{ij} ψ(x)_j`. -/
def Kop (N : ℕ) (ψ : Z3 → Fin 2 → ℂ) (y : Z3) (i : Fin 2) : ℂ :=
  ∑ x ∈ regA N, ∑ j, kernel N (y - x) i j * ψ x j

/-- Squared ℓ² norm over a region. -/
def l2sq (s : Finset Z3) (ψ : Z3 → Fin 2 → ℂ) : ℝ := ∑ x ∈ s, ∑ j, ‖ψ x j‖ ^ 2

/-- Generic Schur/Cauchy–Schwarz bound for a block operator with entries `≤ ε`. -/
lemma block_bound (A B : Finset Z3) (G : Z3 → Z3 → Fin 2 → Fin 2 → ℂ) (ε : ℝ) (hε : 0 ≤ ε)
    (hG : ∀ y ∈ B, ∀ x ∈ A, ∀ i j, ‖G y x i j‖ ≤ ε) (ψ : Z3 → Fin 2 → ℂ) :
    ∑ y ∈ B, ∑ i, ‖∑ x ∈ A, ∑ j, G y x i j * ψ x j‖ ^ 2
      ≤ 4 * (A.card : ℝ) * (B.card : ℝ) * ε ^ 2 * l2sq A ψ := by
  have hrow : ∀ y ∈ B, ∀ i : Fin 2,
      ‖∑ x ∈ A, ∑ j, G y x i j * ψ x j‖ ^ 2 ≤ 2 * (A.card : ℝ) * ε ^ 2 * l2sq A ψ := by
    intro y hy i
    have h1 : ‖∑ x ∈ A, ∑ j, G y x i j * ψ x j‖ ≤ ∑ x ∈ A, ∑ j, ε * ‖ψ x j‖ := by
      refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun x hx => ?_)
      refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun j _ => ?_)
      rw [norm_mul]
      exact mul_le_mul_of_nonneg_right (hG y hy x hx i j) (norm_nonneg _)
    have h2 : (∑ x ∈ A, ∑ j, ε * ‖ψ x j‖) ^ 2
        ≤ ((A ×ˢ (Finset.univ : Finset (Fin 2))).card : ℝ) *
            ∑ p ∈ A ×ˢ (Finset.univ : Finset (Fin 2)), (ε * ‖ψ p.1 p.2‖) ^ 2 := by
      rw [← Finset.sum_product']
      exact sq_sum_le_card_mul_sum_sq
    have h3 : ∑ p ∈ A ×ˢ (Finset.univ : Finset (Fin 2)), (ε * ‖ψ p.1 p.2‖) ^ 2
        = ε ^ 2 * l2sq A ψ := by
      rw [Finset.sum_product, l2sq, Finset.mul_sum]
      apply Finset.sum_congr rfl; intro x _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl; intro j _
      ring
    rw [h3, Finset.card_product, Finset.card_univ, Fintype.card_fin] at h2
    have h0 : 0 ≤ ∑ x ∈ A, ∑ j, ε * ‖ψ x j‖ := by positivity
    calc ‖∑ x ∈ A, ∑ j, G y x i j * ψ x j‖ ^ 2 ≤ (∑ x ∈ A, ∑ j, ε * ‖ψ x j‖) ^ 2 := by
          gcongr
      _ ≤ ((A.card * 2 : ℕ) : ℝ) * (ε ^ 2 * l2sq A ψ) := h2
      _ = 2 * (A.card : ℝ) * ε ^ 2 * l2sq A ψ := by push_cast; ring
  calc ∑ y ∈ B, ∑ i, ‖∑ x ∈ A, ∑ j, G y x i j * ψ x j‖ ^ 2
      ≤ ∑ _y ∈ B, ∑ _i : Fin 2, 2 * (A.card : ℝ) * ε ^ 2 * l2sq A ψ :=
        Finset.sum_le_sum fun y hy => Finset.sum_le_sum fun i _ => hrow y hy i
    _ = 4 * (A.card : ℝ) * (B.card : ℝ) * ε ^ 2 * l2sq A ψ := by
        rw [Finset.sum_const, Finset.sum_const, Finset.card_univ, Fintype.card_fin]
        simp only [nsmul_eq_mul]
        push_cast; ring

/-- **Theorem 4.1, operator form.**  For `N ≥ 2`,
`‖P_ℬ S^N P_𝒜 ψ‖² ≤ (4 N^4 · 2^{-(1-√3/2)N})² ‖ψ‖²` on ℓ²(𝒜_N; ℂ²),
i.e. `T_N ≤ 4 N^4 e^{-JN} ≤ 9 N^4 e^{-JN}`. -/
theorem TN_bound (N : ℕ) (hN : 2 ≤ N) (ψ : Z3 → Fin 2 → ℂ) :
    l2sq (regB N) (Kop N ψ)
      ≤ (4 * (N : ℝ) ^ 4 * (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * (N : ℝ))) ^ 2 *
          l2sq (regA N) ψ := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 1 := ⟨N - 1, by omega⟩
  set E : ℝ := (2 : ℝ) ^ (-(1 - Real.sqrt 3 / 2) * ((n + 1 : ℕ) : ℝ)) with hE
  set ε : ℝ := 33 / 32 * ((n + 1 : ℕ) : ℝ) * E
  have hE0 : 0 ≤ E := by positivity
  have hε : 0 ≤ ε := by positivity
  have hG : ∀ y ∈ regB (n + 1), ∀ x ∈ regA (n + 1), ∀ i j,
      ‖kernel (n + 1) (y - x) i j‖ ≤ ε := by
    intro y hy x hx i j
    exact kernel_bound_regions n x y (mem_regA.mp hx) (mem_regB.mp hy) i j
  have hb := block_bound (regA (n + 1)) (regB (n + 1)) (fun y x => kernel (n + 1) (y - x))
    ε hε hG ψ
  have hA := card_regA_le (n + 1) hN
  have hB := card_regB_le (n + 1) hN
  have hl2 : 0 ≤ l2sq (regA (n + 1)) ψ := by unfold l2sq; positivity
  have hNr : (0 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) := by positivity
  calc l2sq (regB (n + 1)) (Kop (n + 1) ψ)
      ≤ 4 * ((regA (n + 1)).card : ℝ) * ((regB (n + 1)).card : ℝ) * ε ^ 2 *
          l2sq (regA (n + 1)) ψ := hb
    _ ≤ 4 * ((n + 1 : ℕ) : ℝ) ^ 3 * ((n + 1 : ℕ) : ℝ) ^ 3 * ε ^ 2 * l2sq (regA (n + 1)) ψ := by
        gcongr
    _ ≤ (4 * ((n + 1 : ℕ) : ℝ) ^ 4 * E) ^ 2 * l2sq (regA (n + 1)) ψ := by
        apply mul_le_mul_of_nonneg_right _ hl2
        simp only [ε]
        have : (0 : ℝ) ≤ ((n + 1 : ℕ) : ℝ) ^ 8 * E ^ 2 := by positivity
        nlinarith

/-- **Operational step.**  If Bob's two amplitudes differ by at most `2T` and
the effect has norm `≤ 1`, then the signal is at most `4T`. -/
theorem delta_le_four_T {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (Eop : H →L[ℂ] H) (hE : ‖Eop‖ ≤ 1) (v₀ v₁ : H) (h₀ : ‖v₀‖ ≤ 1) (h₁ : ‖v₁‖ ≤ 1)
    {T : ℝ} (hT : ‖v₁ - v₀‖ ≤ 2 * T) :
    ‖(inner ℂ v₁ (Eop v₁)) - inner ℂ v₀ (Eop v₀)‖ ≤ 4 * T := by
  have hsplit : inner ℂ v₁ (Eop v₁) - inner ℂ v₀ (Eop v₀)
      = inner ℂ (v₁ - v₀) (Eop v₁) + inner ℂ v₀ (Eop (v₁ - v₀)) := by
    rw [inner_sub_left, map_sub, inner_sub_right]; ring
  rw [hsplit]
  have hEv : ∀ v : H, ‖Eop v‖ ≤ ‖v‖ := fun v =>
    (Eop.le_opNorm v).trans (by nlinarith [norm_nonneg v])
  have t1 : ‖inner ℂ (v₁ - v₀) (Eop v₁)‖ ≤ 2 * T := by
    calc ‖inner ℂ (v₁ - v₀) (Eop v₁)‖ ≤ ‖v₁ - v₀‖ * ‖Eop v₁‖ := norm_inner_le_norm _ _
      _ ≤ 2 * T * 1 := mul_le_mul hT ((hEv v₁).trans h₁) (norm_nonneg _)
          (by linarith [norm_nonneg (v₁ - v₀)])
      _ = 2 * T := mul_one _
  have t2 : ‖inner ℂ v₀ (Eop (v₁ - v₀))‖ ≤ 2 * T := by
    calc ‖inner ℂ v₀ (Eop (v₁ - v₀))‖ ≤ ‖v₀‖ * ‖Eop (v₁ - v₀)‖ := norm_inner_le_norm _ _
      _ ≤ 1 * (2 * T) := mul_le_mul h₀ ((hEv _).trans hT) (norm_nonneg _) (by norm_num)
      _ = 2 * T := one_mul _
  calc ‖inner ℂ (v₁ - v₀) (Eop v₁) + inner ℂ v₀ (Eop (v₁ - v₀))‖
      ≤ ‖inner ℂ (v₁ - v₀) (Eop v₁)‖ + ‖inner ℂ v₀ (Eop (v₁ - v₀))‖ := norm_add_le _ _
    _ ≤ 4 * T := by linarith

end QcaFormal
