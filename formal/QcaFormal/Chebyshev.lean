import Mathlib

/-!
# Powers of a unimodular 2×2 matrix without a spectral gap

For `T` with `det T = 1` and `tr T = l + m`, `l * m = 1`, Cayley–Hamilton gives
`T^(n+1) = h n • T - hPrev n • 1` with `h n = ∑_{j ≤ n} l^j m^(n-j)`.
If `‖l‖, ‖m‖ ≤ 4` then `‖h n‖ ≤ (n+1) 4^n`.  No division by `l - m` occurs,
so coincident eigenvalues (Jordan blocks) are covered.
-/

noncomputable section

open Matrix Finset

namespace QcaFormal

/-- Complete homogeneous symmetric polynomial `h_n(l, m)`. -/
def hsym (l m : ℂ) (n : ℕ) : ℂ := ∑ j ∈ range (n + 1), l ^ j * m ^ (n - j)

/-- `h_{n-1}`, with `h_{-1} = 0`. -/
def hPrev (l m : ℂ) : ℕ → ℂ
  | 0 => 0
  | n + 1 => hsym l m n

lemma hsym_zero (l m : ℂ) : hsym l m 0 = 1 := by simp [hsym]

lemma hsym_succ (l m : ℂ) (n : ℕ) : hsym l m (n + 1) = l ^ (n + 1) + m * hsym l m n := by
  unfold hsym
  rw [sum_range_succ, Nat.sub_self, pow_zero, mul_one, add_comm, mul_sum]
  congr 1
  apply sum_congr rfl
  intro j hj
  have hj' : j ≤ n := Nat.lt_succ_iff.mp (mem_range.mp hj)
  rw [show n + 1 - j = (n - j) + 1 by omega, pow_succ]
  ring

lemma hsym_rec (l m : ℂ) (hlm : l * m = 1) (n : ℕ) :
    hsym l m (n + 1) = (l + m) * hsym l m n - hPrev l m n := by
  cases n with
  | zero => simp [hsym, hPrev, sum_range_succ]; ring
  | succ k =>
    simp only [hPrev]
    rw [hsym_succ l m (k + 1), hsym_succ l m k]
    have : l * (m * hsym l m k) = hsym l m k := by rw [← mul_assoc, hlm, one_mul]
    linear_combination (-(1 : ℂ)) * this

lemma norm_hsym_le {l m : ℂ} (hl : ‖l‖ ≤ 4) (hm : ‖m‖ ≤ 4) (n : ℕ) :
    ‖hsym l m n‖ ≤ (n + 1) * 4 ^ n := by
  unfold hsym
  calc ‖∑ j ∈ range (n + 1), l ^ j * m ^ (n - j)‖
      ≤ ∑ j ∈ range (n + 1), ‖l ^ j * m ^ (n - j)‖ := norm_sum_le _ _
    _ ≤ ∑ j ∈ range (n + 1), (4 : ℝ) ^ n := by
        apply sum_le_sum
        intro j hj
        have hj' : j ≤ n := Nat.lt_succ_iff.mp (mem_range.mp hj)
        rw [norm_mul, norm_pow, norm_pow]
        calc ‖l‖ ^ j * ‖m‖ ^ (n - j) ≤ 4 ^ j * 4 ^ (n - j) := by
              apply mul_le_mul (pow_le_pow_left₀ (norm_nonneg _) hl _)
                (pow_le_pow_left₀ (norm_nonneg _) hm _) (by positivity) (by positivity)
          _ = 4 ^ n := by rw [← pow_add, Nat.add_sub_cancel' hj']
    _ = (n + 1) * 4 ^ n := by rw [sum_const, card_range, nsmul_eq_mul]; push_cast; ring

lemma norm_hPrev_le {l m : ℂ} (hl : ‖l‖ ≤ 4) (hm : ‖m‖ ≤ 4) (n : ℕ) :
    ‖hPrev l m n‖ ≤ n * 4 ^ n := by
  cases n with
  | zero => simp [hPrev]
  | succ k =>
    simp only [hPrev]
    calc ‖hsym l m k‖ ≤ (k + 1) * 4 ^ k := norm_hsym_le hl hm k
      _ ≤ ((k + 1 : ℕ) : ℝ) * 4 ^ (k + 1) := by
        push_cast
        have : (4 : ℝ) ^ k ≤ 4 ^ (k + 1) := pow_le_pow_right₀ (by norm_num) (Nat.le_succ k)
        have hk : (0 : ℝ) ≤ k + 1 := by positivity
        nlinarith

/-- Cayley–Hamilton for 2×2 matrices. -/
lemma cayley_hamilton_two (T : Matrix (Fin 2) (Fin 2) ℂ) :
    T * T = T.trace • T - T.det • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.det_fin_two] <;> ring

/-- Power formula for a unimodular 2×2 matrix. -/
lemma pow_succ_eq (T : Matrix (Fin 2) (Fin 2) ℂ) {l m : ℂ} (hlm : l * m = 1)
    (htr : T.trace = l + m) (hdet : T.det = 1) (n : ℕ) :
    T ^ (n + 1) = hsym l m n • T - hPrev l m n • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  induction n with
  | zero => simp [hsym, hPrev]
  | succ k ih =>
    rw [pow_succ', ih, Matrix.mul_sub, Matrix.mul_smul, Matrix.mul_smul, Matrix.mul_one,
      cayley_hamilton_two, htr, hdet, hsym_rec l m hlm k]
    simp only [hPrev, one_smul, smul_sub, sub_smul, smul_smul]
    abel_nf
    module

/-- Entrywise bound on the powers. -/
lemma norm_pow_entry_le (T : Matrix (Fin 2) (Fin 2) ℂ) {l m : ℂ} (hlm : l * m = 1)
    (htr : T.trace = l + m) (hdet : T.det = 1) (hl : ‖l‖ ≤ 4) (hm : ‖m‖ ≤ 4)
    {B : ℝ} (hB : ∀ i j, ‖T i j‖ ≤ B) (n : ℕ) (i j : Fin 2) :
    ‖(T ^ (n + 1)) i j‖ ≤ (n + 1) * 4 ^ n * B + n * 4 ^ n := by
  rw [pow_succ_eq T hlm htr hdet n]
  simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
  have h1 : ‖hsym l m n * T i j‖ ≤ (n + 1) * 4 ^ n * B := by
    rw [norm_mul]
    exact mul_le_mul (norm_hsym_le hl hm n) (hB i j) (norm_nonneg _) (by positivity)
  have h2 : ‖hPrev l m n * (1 : Matrix (Fin 2) (Fin 2) ℂ) i j‖ ≤ n * 4 ^ n := by
    rw [norm_mul]
    have : ‖(1 : Matrix (Fin 2) (Fin 2) ℂ) i j‖ ≤ 1 := by
      rw [Matrix.one_apply]; split_ifs <;> simp
    calc ‖hPrev l m n‖ * ‖(1 : Matrix (Fin 2) (Fin 2) ℂ) i j‖ ≤ (n * 4 ^ n) * 1 :=
          mul_le_mul (norm_hPrev_le hl hm n) this (norm_nonneg _) (by positivity)
      _ = n * 4 ^ n := mul_one _
  calc ‖hsym l m n * T i j - hPrev l m n * (1 : Matrix (Fin 2) (Fin 2) ℂ) i j‖
      ≤ ‖hsym l m n * T i j‖ + ‖hPrev l m n * (1 : Matrix (Fin 2) (Fin 2) ℂ) i j‖ :=
        norm_sub_le _ _
    _ ≤ (n + 1) * 4 ^ n * B + n * 4 ^ n := add_le_add h1 h2

end QcaFormal
