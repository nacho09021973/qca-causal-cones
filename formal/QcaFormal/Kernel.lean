import Mathlib
import QcaFormal.Symbol

/-!
# Exact coefficient extraction and the tilted kernel bound

The kernel `G_N(d)` is a Laurent coefficient.  A Laurent polynomial supported
in the box `|d_j| ≤ r` is recovered exactly from its values at the
`(2r+1)`-th roots of unity (a finite discrete Fourier transform), so no
integrals are needed.  Evaluating at the tilted points `2 ζ^k` gives
`‖G_N(d)_{ij}‖ ≤ 2^{-(d₀+d₁+d₂)} · sup_{|w|=1} ‖(T(2w)^N)_{ij}‖`.
-/

noncomputable section

open AddMonoidAlgebra Finset Complex

namespace QcaFormal

/-! ### Supports -/

/-- `p` is supported in the box `max_j |d_j| ≤ r`. -/
def InBox (r : ℕ) (p : Lau) : Prop := ∀ d ∈ p.support, ∀ j, |d j| ≤ (r : ℤ)

lemma InBox.mono {r s : ℕ} (h : r ≤ s) {p : Lau} (hp : InBox r p) : InBox s p :=
  fun d hd j => (hp d hd j).trans (by exact_mod_cast h)

lemma InBox.add {r : ℕ} {p q : Lau} (hp : InBox r p) (hq : InBox r q) : InBox r (p + q) := by
  intro d hd j
  rcases Finset.mem_union.mp (Finsupp.support_add hd) with h | h
  · exact hp d h j
  · exact hq d h j

lemma InBox.neg {r : ℕ} {p : Lau} (hp : InBox r p) : InBox r (-p) := by
  intro d hd j
  apply hp d _ j
  rw [Finsupp.mem_support_iff] at hd ⊢
  intro h0
  apply hd
  have : (-p) d = -(p d) := rfl
  rw [this, h0, neg_zero]

lemma InBox.sub {r : ℕ} {p q : Lau} (hp : InBox r p) (hq : InBox r q) : InBox r (p - q) := by
  rw [sub_eq_add_neg]; exact hp.add hq.neg

lemma InBox.smul {r : ℕ} (c : ℂ) {p : Lau} (hp : InBox r p) : InBox r (c • p) :=
  fun d hd j => hp d (Finsupp.support_smul hd) j

lemma InBox.mul {r s : ℕ} {p q : Lau} (hp : InBox r p) (hq : InBox s q) :
    InBox (r + s) (p * q) := by
  intro d hd j
  obtain ⟨a, ha, b, hb, rfl⟩ := Finset.mem_add.mp (AddMonoidAlgebra.support_mul p q hd)
  have h1 := hp a ha j
  have h2 := hq b hb j
  simp only [Pi.add_apply]
  push_cast
  calc |a j + b j| ≤ |a j| + |b j| := abs_add_le _ _
    _ ≤ r + s := add_le_add h1 h2

lemma InBox.sum {r : ℕ} {ι : Type*} (s : Finset ι) (f : ι → Lau)
    (h : ∀ i ∈ s, InBox r (f i)) : InBox r (∑ i ∈ s, f i) := by
  classical
  intro d hd j
  obtain ⟨i, hi, hdi⟩ := Finset.mem_biUnion.mp (Finsupp.support_finsetSum hd)
  exact h i hi d hdi j

lemma inBox_zero (r : ℕ) : InBox r (0 : Lau) := by
  intro d hd
  change d ∈ (0 : Z3 →₀ ℂ).support at hd
  simp at hd

lemma inBox_X {r : ℕ} (d : Z3) (h : ∀ j, |d j| ≤ (r : ℤ)) : InBox r (X d) := by
  intro d' hd' j
  have : d' = d := by
    unfold X at hd'
    exact Finset.mem_singleton.mp (Finsupp.support_single_subset hd')
  rw [this]; exact h j

lemma inBox_one : InBox 0 (1 : Lau) := by
  rw [AddMonoidAlgebra.one_def]
  exact inBox_X 0 (by simp)

lemma abs_ej_le (j k : Fin 3) : |ej j k| ≤ ((1 : ℕ) : ℤ) := by
  unfold ej
  rw [Pi.single_apply]
  split_ifs <;> simp

lemma inBox_cL (j : Fin 3) : InBox 1 (cL j) := by
  unfold cL
  exact ((inBox_X _ (abs_ej_le j)).add (inBox_X _ (fun k => by
    rw [Pi.neg_apply, abs_neg]; exact abs_ej_le j k))).smul _

lemma inBox_sL (j : Fin 3) : InBox 1 (sL j) := by
  unfold sL
  exact ((inBox_X _ (abs_ej_le j)).sub (inBox_X _ (fun k => by
    rw [Pi.neg_apply, abs_neg]; exact abs_ej_le j k))).smul _

lemma inBox_Xej (j : Fin 3) : InBox 1 (X (ej j)) := inBox_X _ (abs_ej_le j)

lemma inBox_Xnegej (j : Fin 3) : InBox 1 (X (-ej j)) :=
  inBox_X _ (fun k => by rw [Pi.neg_apply, abs_neg]; exact abs_ej_le j k)

lemma inBox_Ssym (i j : Fin 2) : InBox 3 (Ssym i j) := by
  have cc : InBox 3 (cL 0 * cL 1 * X (-ej 2)) := ((inBox_cL 0).mul (inBox_cL 1)).mul (inBox_Xnegej 2)
  have cc' : InBox 3 (cL 0 * cL 1 * X (ej 2)) := ((inBox_cL 0).mul (inBox_cL 1)).mul (inBox_Xej 2)
  have cs : InBox 3 (cL 0 * sL 1) := ((inBox_cL 0).mul (inBox_sL 1)).mono (by norm_num)
  have is0 : InBox 3 (I • sL 0) := ((inBox_sL 0).smul I).mono (by norm_num)
  fin_cases i <;> fin_cases j
  · exact cc
  · exact cs.sub is0
  · exact cs.neg.sub is0
  · exact cc'

lemma inBox_pow (n : ℕ) (i j : Fin 2) : InBox (3 * n) ((Ssym ^ n) i j) := by
  induction n generalizing i j with
  | zero =>
    rw [pow_zero, Matrix.one_apply]
    split_ifs
    · exact inBox_one
    · exact inBox_zero _
  | succ n ih =>
    rw [pow_succ', Matrix.mul_apply]
    apply InBox.sum
    intro k _
    have := (inBox_Ssym i k).mul (ih k j)
    rwa [show 3 + 3 * n = 3 * (n + 1) by ring] at this

/-! ### Roots of unity -/

/-- `ζ_M = exp(2πi/M)`. -/
def zeta (M : ℕ) : ℂ := Complex.exp (2 * Real.pi * I / M)

lemma zeta_prim {M : ℕ} (hM : M ≠ 0) : IsPrimitiveRoot (zeta M) M :=
  Complex.isPrimitiveRoot_exp M hM

lemma zeta_ne_zero (M : ℕ) : zeta M ≠ 0 := Complex.exp_ne_zero _

lemma norm_zeta (M : ℕ) : ‖zeta M‖ = 1 := by
  unfold zeta
  rw [Complex.norm_exp]
  simp

lemma norm_zeta_zpow (M : ℕ) (m : ℤ) : ‖zeta M ^ m‖ = 1 := by
  rw [norm_zpow, norm_zeta, one_zpow]

/-- Orthogonality of the characters of `ℤ / M`. -/
lemma sum_zeta_zpow {M : ℕ} (hM : 1 < M) (m : ℤ) (hm : |m| < M) :
    ∑ k : Fin M, zeta M ^ ((k : ℤ) * m) = if m = 0 then (M : ℂ) else 0 := by
  have hprim := zeta_prim (M := M) (by omega)
  have hz := zeta_ne_zero M
  have hterm : ∀ k : ℕ, zeta M ^ ((k : ℤ) * m) = (zeta M ^ m) ^ k := by
    intro k
    rw [mul_comm, zpow_mul, zpow_natCast]
  rw [Fin.sum_univ_eq_sum_range (fun k => zeta M ^ ((k : ℤ) * m)) M]
  simp_rw [hterm]
  split_ifs with h0
  · subst h0; simp
  · have hne : zeta M ^ m ≠ 1 := by
      intro h1
      rw [hprim.zpow_eq_one_iff_dvd] at h1
      obtain ⟨c, hc⟩ := h1
      have hc0 : c ≠ 0 := by rintro rfl; simp at hc; exact h0 hc
      have : (M : ℤ) ≤ |m| := by
        rw [hc, abs_mul]
        have : (1 : ℤ) ≤ |c| := Int.one_le_abs hc0
        have hM0 : (0 : ℤ) ≤ |(M : ℤ)| := abs_nonneg _
        calc (M : ℤ) = |(M : ℤ)| * 1 := by simp
          _ ≤ |(M : ℤ)| * |c| := by gcongr
      omega
    rw [geom_sum_eq hne]
    have : (zeta M ^ m) ^ M = 1 := by
      rw [← zpow_natCast, ← zpow_mul, mul_comm, zpow_mul, zpow_natCast, hprim.pow_eq_one,
        one_zpow]
    rw [this, sub_self, zero_div]

/-- The unit `ζ_M^k`. -/
def zetaPt (M : ℕ) (k : Fin 3 → Fin M) : Fin 3 → ℂˣ :=
  fun j => (Units.mk0 (zeta M) (zeta_ne_zero M)) ^ ((k j : ℕ))

lemma zetaPt_val (M : ℕ) (k : Fin 3 → Fin M) (j : Fin 3) :
    ((zetaPt M k j : ℂˣ) : ℂ) = zeta M ^ ((k j : ℕ)) := by
  simp [zetaPt]

lemma norm_zetaPt (M : ℕ) (k : Fin 3 → Fin M) (j : Fin 3) : ‖((zetaPt M k j : ℂˣ) : ℂ)‖ = 1 := by
  rw [zetaPt_val, norm_pow, norm_zeta, one_pow]

/-- Evaluation at a tilted root-of-unity point, expanded. -/
lemma evalAt_tilt_zeta (M : ℕ) (k : Fin 3 → Fin M) (p : Lau) :
    evalAt (tilt (zetaPt M k)) p
      = ∑ d ∈ p.support, p d * ((2 : ℂ) ^ (d 0 + d 1 + d 2) *
          ∏ j, zeta M ^ ((k j : ℤ) * d j)) := by
  rw [evalAt_apply]
  apply Finset.sum_congr rfl
  intro d _
  congr 1
  rw [Fin.prod_univ_three, Fin.prod_univ_three]
  simp only [tilt_val, zetaPt_val]
  have h2 : (2 : ℂ) ≠ 0 := two_ne_zero
  have hz := zeta_ne_zero M
  simp only [mul_zpow, ← zpow_natCast, ← zpow_mul, zpow_add₀ h2]
  ring

/-- Exact inversion: a box-supported Laurent polynomial from its tilted
root-of-unity values. -/
theorem dft_coeff (p : Lau) (r : ℕ) (hr : 0 < r) (hp : InBox r p) (d : Z3)
    (hd : ∀ j, |d j| ≤ (r : ℤ)) :
    ∑ k : Fin 3 → Fin (2 * r + 1),
        (∏ j, zeta (2 * r + 1) ^ (-((k j : ℤ) * d j))) * evalAt (tilt (zetaPt (2 * r + 1) k)) p
      = ((2 * r + 1 : ℕ) : ℂ) ^ 3 * ((2 : ℂ) ^ (d 0 + d 1 + d 2) * p d) := by
  set M := 2 * r + 1 with hMdef
  have hM : 1 < M := by omega
  have hz := zeta_ne_zero M
  simp_rw [evalAt_tilt_zeta, Finset.mul_sum]
  rw [Finset.sum_comm]
  -- for each `d'` in the support, the inner sum over `k` is a product of 1D sums
  have inner : ∀ d' ∈ p.support,
      ∑ k : Fin 3 → Fin M, (∏ j, zeta M ^ (-((k j : ℤ) * d j))) *
          (p d' * ((2 : ℂ) ^ (d' 0 + d' 1 + d' 2) * ∏ j, zeta M ^ ((k j : ℤ) * d' j)))
        = p d' * (2 : ℂ) ^ (d' 0 + d' 1 + d' 2) *
            ∏ j, (if d' j - d j = 0 then (M : ℂ) else 0) := by
    intro d' hd'
    have hrew : ∀ k : Fin 3 → Fin M, (∏ j, zeta M ^ (-((k j : ℤ) * d j))) *
          (p d' * ((2 : ℂ) ^ (d' 0 + d' 1 + d' 2) * ∏ j, zeta M ^ ((k j : ℤ) * d' j)))
        = p d' * (2 : ℂ) ^ (d' 0 + d' 1 + d' 2) *
            ∏ j, zeta M ^ ((k j : ℤ) * (d' j - d j)) := by
      intro k
      have : ∏ j, zeta M ^ ((k j : ℤ) * (d' j - d j))
          = (∏ j, zeta M ^ (-((k j : ℤ) * d j))) * ∏ j, zeta M ^ ((k j : ℤ) * d' j) := by
        rw [← Finset.prod_mul_distrib]
        apply Finset.prod_congr rfl
        intro j _
        rw [← zpow_add₀ hz]
        congr 1
        ring
      rw [this]
      ring
    simp_rw [hrew]
    rw [← Finset.mul_sum]
    congr 1
    rw [← Fintype.prod_sum (fun j (kj : Fin M) => zeta M ^ ((kj : ℤ) * (d' j - d j)))]
    apply Finset.prod_congr rfl
    intro j _
    apply sum_zeta_zpow hM
    have h1 := hp d' hd' j
    have h2 := hd j
    rw [abs_le] at h1 h2
    rw [abs_lt]
    have hMz : ((M : ℕ) : ℤ) = 2 * (r : ℤ) + 1 := by rw [hMdef]; push_cast; ring
    rw [hMz]
    constructor <;> omega
  rw [Finset.sum_congr rfl inner]
  -- only `d' = d` survives
  have hprod : ∀ d' : Z3, (∏ j, (if d' j - d j = 0 then (M : ℂ) else 0))
      = if d' = d then (M : ℂ) ^ 3 else 0 := by
    intro d'
    by_cases h : d' = d
    · subst h; simp
    · rw [if_neg h]
      obtain ⟨j, hj⟩ : ∃ j, d' j ≠ d j := by
        by_contra hc; push Not at hc; exact h (funext hc)
      apply Finset.prod_eq_zero (Finset.mem_univ j)
      rw [if_neg (sub_ne_zero.mpr hj)]
  simp_rw [hprod, mul_ite, mul_zero]
  rw [Finset.sum_ite_eq']
  split_ifs with hmem
  · ring
  · rw [Finsupp.notMem_support_iff.mp hmem]; ring

/-- Tilted kernel bound: `‖G_{n+1}(d)_{ij}‖ ≤ (33/32)(n+1)4^{n+1} · 2^{-(d₀+d₁+d₂)}`. -/
theorem kernel_entry_bound (n : ℕ) (d : Z3) (i j : Fin 2) :
    ‖kernel (n + 1) d i j‖
      ≤ 33 / 32 * ((n + 1 : ℕ) : ℝ) * 4 ^ (n + 1) * (2 : ℝ) ^ (-(d 0 + d 1 + d 2)) := by
  set p := (Ssym ^ (n + 1)) i j with hp
  set B : ℝ := 33 / 32 * ((n + 1 : ℕ) : ℝ) * 4 ^ (n + 1) with hB
  have hBnn : 0 ≤ B := by positivity
  have hbox := inBox_pow (n + 1) i j
  unfold kernel
  rw [← hp]
  by_cases hd : ∀ j, |d j| ≤ ((3 * (n + 1) : ℕ) : ℤ)
  · set r := 3 * (n + 1)
    set M := 2 * r + 1
    have key := dft_coeff p r (by positivity) hbox d hd
    have hpt : ∀ k : Fin 3 → Fin M,
        ‖(∏ j, zeta M ^ (-((k j : ℤ) * d j))) * evalAt (tilt (zetaPt M k)) p‖ ≤ B := by
      intro k
      rw [norm_mul, norm_prod]
      simp_rw [norm_zeta_zpow]
      rw [Finset.prod_const_one, one_mul, hp, Tz_pow_apply]
      exact norm_Tz_tilt_pow_le (zetaPt M k) (norm_zetaPt M k) n i j
    have hsum := norm_sum_le (Finset.univ : Finset (Fin 3 → Fin M))
      (fun k => (∏ j, zeta M ^ (-((k j : ℤ) * d j))) * evalAt (tilt (zetaPt M k)) p)
    rw [key] at hsum
    have hcard : (∑ _k : Fin 3 → Fin M, B) = (M : ℝ) ^ 3 * B := by
      rw [Finset.sum_const, Finset.card_univ, Fintype.card_fun, Fintype.card_fin,
        Fintype.card_fin, nsmul_eq_mul]
      push_cast; ring
    have hle := hsum.trans ((Finset.sum_le_sum fun k _ => hpt k).trans_eq hcard)
    rw [norm_mul, norm_mul, norm_pow, Complex.norm_natCast, norm_zpow, Complex.norm_two] at hle
    have hM3 : (0 : ℝ) < (M : ℝ) ^ 3 := by positivity
    have h2 : (0 : ℝ) < (2 : ℝ) ^ (d 0 + d 1 + d 2) := zpow_pos (by norm_num) _
    have : (2 : ℝ) ^ (d 0 + d 1 + d 2) * ‖p d‖ ≤ B := by
      have := le_of_mul_le_mul_left (by linarith [hle] : (M : ℝ) ^ 3 *
        ((2 : ℝ) ^ (d 0 + d 1 + d 2) * ‖p d‖) ≤ (M : ℝ) ^ 3 * B) hM3
      exact this
    rw [zpow_neg, ← div_eq_mul_inv, le_div_iff₀ h2]
    linarith
  · -- outside the box the coefficient vanishes
    have : p d = 0 := by
      by_contra hne
      exact hd (hbox d (Finsupp.mem_support_iff.mpr hne))
    rw [this, norm_zero]
    positivity

end QcaFormal
