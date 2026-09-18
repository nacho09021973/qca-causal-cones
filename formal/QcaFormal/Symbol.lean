import Mathlib
import QcaFormal.Ellipse
import QcaFormal.Chebyshev

/-!
# The symbol of the walk and its tilted evaluations

`R = ℂ[ℤ³]` is the ring of Laurent polynomials in three variables, with
`X d ↔ e^{i p·d}`.  `Ssym` is the symbol `S(p)` of eq. (2) of the paper, i.e.
the inverse of the Cedzich–Joye–Werner–Werner symbol (5.15).  The `N`-step
kernel `G_N(d)` is the coefficient of `X d` in `Ssym ^ N` (convolution power
of the jump blocks).

`evalAt z` evaluates at `z ∈ (ℂˣ)³`; the tilted points of the paper are
`z = 2 w` with `|w_j| = 1` (tilt `t = log 2` along `u = (1,1,1)`).
-/

noncomputable section

open AddMonoidAlgebra Finset Complex

namespace QcaFormal

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

/-! ### Evaluation characters -/

/-- The character `d ↦ ∏_j z_j^{d_j}`. -/
def chi (z : Fin 3 → ℂˣ) : Multiplicative Z3 →* ℂ where
  toFun d := ∏ j, ((z j : ℂ)) ^ (Multiplicative.toAdd d j)
  map_one' := by simp
  map_mul' a b := by
    simp only [toAdd_mul, Pi.add_apply]
    rw [← Finset.prod_mul_distrib]
    apply Finset.prod_congr rfl
    intro j _
    exact zpow_add₀ (Units.ne_zero _) _ _

/-- Evaluation of a Laurent polynomial at `z`. -/
def evalAt (z : Fin 3 → ℂˣ) : Lau →ₐ[ℂ] ℂ := AddMonoidAlgebra.lift ℂ ℂ Z3 (chi z)

lemma evalAt_apply (z : Fin 3 → ℂˣ) (p : Lau) :
    evalAt z p = ∑ d ∈ p.support, p d * ∏ j, ((z j : ℂ)) ^ (d j) := by
  unfold evalAt
  rw [AddMonoidAlgebra.lift_apply, Finsupp.sum]
  apply Finset.sum_congr rfl
  intro d _
  simp [chi, smul_eq_mul]

lemma evalAt_X (z : Fin 3 → ℂˣ) (d : Z3) : evalAt z (X d) = ∏ j, ((z j : ℂ)) ^ (d j) := by
  unfold evalAt X
  rw [AddMonoidAlgebra.lift_single]
  simp [chi]

lemma evalAt_X_ej (z : Fin 3 → ℂˣ) (j : Fin 3) : evalAt z (X (ej j)) = z j := by
  rw [evalAt_X]
  fin_cases j <;> simp [ej, Pi.single_apply]

lemma evalAt_X_neg_ej (z : Fin 3 → ℂˣ) (j : Fin 3) :
    evalAt z (X (-ej j)) = ((z j : ℂ))⁻¹ := by
  rw [evalAt_X]
  fin_cases j <;> simp [ej, Pi.single_apply]

/-- `cos` evaluated: `C_j = (z_j + z_j⁻¹)/2`. -/
def Cz (z : Fin 3 → ℂˣ) (j : Fin 3) : ℂ := (1 / 2 : ℂ) * ((z j : ℂ) + ((z j : ℂ))⁻¹)

/-- `sin` evaluated: `(z_j - z_j⁻¹)/(2i)`. -/
def Sz (z : Fin 3 → ℂˣ) (j : Fin 3) : ℂ := (1 / (2 * I)) * ((z j : ℂ) - ((z j : ℂ))⁻¹)

lemma evalAt_cL (z : Fin 3 → ℂˣ) (j : Fin 3) : evalAt z (cL j) = Cz z j := by
  simp [cL, Cz, map_add, evalAt_X_ej, evalAt_X_neg_ej]
  ring

lemma evalAt_sL (z : Fin 3 → ℂˣ) (j : Fin 3) : evalAt z (sL j) = Sz z j := by
  simp [sL, Sz, map_sub, evalAt_X_ej, evalAt_X_neg_ej]

/-- The evaluated symbol. -/
def Tz (z : Fin 3 → ℂˣ) : Matrix (Fin 2) (Fin 2) ℂ := (evalAt z).toRingHom.mapMatrix Ssym

lemma Tz_eq (z : Fin 3 → ℂˣ) :
    Tz z = !![Cz z 0 * Cz z 1 * ((z 2 : ℂ))⁻¹, Cz z 0 * Sz z 1 - I * Sz z 0;
              -(Cz z 0 * Sz z 1) - I * Sz z 0, Cz z 0 * Cz z 1 * (z 2 : ℂ)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Tz, Ssym, RingHom.mapMatrix_apply, Matrix.map_apply, evalAt_cL, evalAt_sL,
      evalAt_X_ej, evalAt_X_neg_ej, map_mul, map_sub, map_neg]

lemma Tz_pow_apply (z : Fin 3 → ℂˣ) (N : ℕ) (i j : Fin 2) :
    evalAt z ((Ssym ^ N) i j) = (Tz z ^ N) i j := by
  unfold Tz
  rw [← map_pow]
  simp [RingHom.mapMatrix_apply, Matrix.map_apply]

/-! ### Algebraic facts at any point -/

lemma Cz_sq_add_Sz_sq (z : Fin 3 → ℂˣ) (j : Fin 3) : Cz z j ^ 2 + Sz z j ^ 2 = 1 := by
  unfold Cz Sz
  have hz : (z j : ℂ) ≠ 0 := Units.ne_zero _
  field_simp
  ring_nf
  rw [Complex.I_sq]
  ring

lemma det_Tz (z : Fin 3 → ℂˣ) : (Tz z).det = 1 := by
  rw [Tz_eq, Matrix.det_fin_two_of]
  have h0 := Cz_sq_add_Sz_sq z 0
  have h1 := Cz_sq_add_Sz_sq z 1
  have hz : (z 2 : ℂ) ≠ 0 := Units.ne_zero _
  have hI : I ^ 2 = -1 := Complex.I_sq
  field_simp
  linear_combination (Cz z 0) ^ 2 * h1 + h0 - (Sz z 0) ^ 2 * hI

lemma trace_Tz (z : Fin 3 → ℂˣ) :
    (Tz z).trace = 2 * (Cz z 0 * Cz z 1 * Cz z 2) := by
  rw [Tz_eq, Matrix.trace_fin_two_of]
  unfold Cz
  have hz : (z 2 : ℂ) ≠ 0 := Units.ne_zero _
  field_simp
  ring

/-! ### Tilted points `z = 2 w`, `|w_j| = 1` -/

/-- The tilted point `2 w`. -/
def tilt (w : Fin 3 → ℂˣ) : Fin 3 → ℂˣ := fun j => (Units.mk0 (2 : ℂ) two_ne_zero) * w j

lemma tilt_val (w : Fin 3 → ℂˣ) (j : Fin 3) : ((tilt w j : ℂˣ) : ℂ) = 2 * (w j : ℂ) := by
  simp [tilt]

section Unit

variable (w : Fin 3 → ℂˣ) (hw : ∀ j, ‖(w j : ℂ)‖ = 1)
include hw

lemma inv_of_unit (j : Fin 3) : ((w j : ℂ))⁻¹ = starRingEnd ℂ (w j : ℂ) := by
  have h := hw j
  rw [Complex.inv_def, ← Complex.sq_norm, h]
  simp

lemma Cz_tilt (j : Fin 3) :
    Cz (tilt w) j = ⟨5 / 4 * (w j : ℂ).re, 3 / 4 * (w j : ℂ).im⟩ := by
  unfold Cz
  rw [tilt_val, mul_inv, inv_of_unit w hw j]
  apply Complex.ext <;> simp <;> ring

lemma gauge_Cz_tilt (j : Fin 3) : gauge (25 / 16) (Cz (tilt w) j) = 1 := by
  rw [Cz_tilt w hw j]
  unfold gauge
  have h : (w j : ℂ).re ^ 2 + (w j : ℂ).im ^ 2 = 1 := by
    have h1 := Complex.normSq_eq_norm_sq (w j : ℂ)
    rw [hw j, Complex.normSq_apply] at h1
    nlinarith [h1]
  simp only
  field_simp
  nlinarith [h]

lemma norm_Cz_tilt_le (j : Fin 3) : ‖Cz (tilt w) j‖ ≤ 5 / 4 := by
  unfold Cz
  rw [tilt_val, norm_mul, mul_inv]
  calc ‖(1 / 2 : ℂ)‖ * ‖2 * (w j : ℂ) + 2⁻¹ * ((w j : ℂ))⁻¹‖
      ≤ ‖(1 / 2 : ℂ)‖ * (‖2 * (w j : ℂ)‖ + ‖2⁻¹ * ((w j : ℂ))⁻¹‖) := by
        gcongr; exact norm_add_le _ _
    _ = 5 / 4 := by
        simp [norm_inv, hw j]
        norm_num

lemma norm_Sz_tilt_le (j : Fin 3) : ‖Sz (tilt w) j‖ ≤ 5 / 4 := by
  unfold Sz
  rw [tilt_val, norm_mul, mul_inv]
  calc ‖1 / (2 * I)‖ * ‖2 * (w j : ℂ) - 2⁻¹ * ((w j : ℂ))⁻¹‖
      ≤ ‖1 / (2 * I)‖ * (‖2 * (w j : ℂ)‖ + ‖2⁻¹ * ((w j : ℂ))⁻¹‖) := by
        gcongr; exact norm_sub_le _ _
    _ = 5 / 4 := by
        simp [norm_inv, hw j]
        norm_num

lemma norm_Tz_tilt_le (i k : Fin 2) : ‖Tz (tilt w) i k‖ ≤ 25 / 8 := by
  have c0 := norm_Cz_tilt_le w hw 0
  have c1 := norm_Cz_tilt_le w hw 1
  have s0 := norm_Sz_tilt_le w hw 0
  have s1 := norm_Sz_tilt_le w hw 1
  have n2 : ‖((tilt w 2 : ℂˣ) : ℂ)‖ = 2 := by rw [tilt_val]; simp [hw 2]
  have n2i : ‖(((tilt w 2 : ℂˣ) : ℂ))⁻¹‖ = 1 / 2 := by rw [norm_inv, n2]; norm_num
  have hC0 := norm_nonneg (Cz (tilt w) 0)
  have hC1 := norm_nonneg (Cz (tilt w) 1)
  have hS1 := norm_nonneg (Sz (tilt w) 1)
  have hCC : ‖Cz (tilt w) 0‖ * ‖Cz (tilt w) 1‖ ≤ 25 / 16 := by nlinarith
  have hCS : ‖Cz (tilt w) 0‖ * ‖Sz (tilt w) 1‖ ≤ 25 / 16 := by nlinarith
  rw [Tz_eq]
  fin_cases i <;> fin_cases k <;> simp only [Matrix.of_apply, Matrix.cons_val',
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one,
    Fin.zero_eta, Fin.mk_one, Fin.isValue]
  · rw [norm_mul, norm_mul, n2i]; nlinarith
  · calc ‖Cz (tilt w) 0 * Sz (tilt w) 1 - I * Sz (tilt w) 0‖
        ≤ ‖Cz (tilt w) 0 * Sz (tilt w) 1‖ + ‖I * Sz (tilt w) 0‖ := norm_sub_le _ _
      _ ≤ 25 / 8 := by rw [norm_mul, norm_mul, Complex.norm_I]; nlinarith
  · calc ‖-(Cz (tilt w) 0 * Sz (tilt w) 1) - I * Sz (tilt w) 0‖
        ≤ ‖-(Cz (tilt w) 0 * Sz (tilt w) 1)‖ + ‖I * Sz (tilt w) 0‖ := norm_sub_le _ _
      _ ≤ 25 / 8 := by rw [norm_neg, norm_mul, norm_mul, Complex.norm_I]; nlinarith
  · rw [norm_mul, norm_mul, n2]; nlinarith

/-- `f = C_0 C_1 C_2 ∈ E_{17/8}` at every tilted point. -/
lemma gauge_f_tilt :
    gauge (289 / 64) (Cz (tilt w) 0 * Cz (tilt w) 1 * Cz (tilt w) 2) ≤ 1 := by
  have g0 := gauge_Cz_tilt w hw 0
  have g1 := gauge_Cz_tilt w hw 1
  have g2 := gauge_Cz_tilt w hw 2
  have h01 := gauge_mul_le (A := 25 / 16) (C := 25 / 16) (by norm_num) (by norm_num)
    (Cz (tilt w) 0) (Cz (tilt w) 1)
  have h012 := gauge_mul_le (A := 25 / 16 * (25 / 16)) (C := 25 / 16) (by norm_num) (by norm_num)
    (Cz (tilt w) 0 * Cz (tilt w) 1) (Cz (tilt w) 2)
  rw [g0, g1] at h01
  rw [g2] at h012
  have hnest := gauge_anti (A := 25 / 16 * (25 / 16) * (25 / 16)) (B := 289 / 64)
    (by norm_num) (by norm_num) (Cz (tilt w) 0 * Cz (tilt w) 1 * Cz (tilt w) 2)
  nlinarith

/-- Pointwise power bound: `|(T(2w)^N)_{ij}| ≤ (33/32) N 4^N` for `N ≥ 1`. -/
lemma norm_Tz_tilt_pow_le (n : ℕ) (i k : Fin 2) :
    ‖(Tz (tilt w) ^ (n + 1)) i k‖ ≤ 33 / 32 * ((n + 1 : ℕ) : ℝ) * 4 ^ (n + 1) := by
  -- the two eigenvalues `l, m` with `l m = 1`, `l + m = tr`
  set f := Cz (tilt w) 0 * Cz (tilt w) 1 * Cz (tilt w) 2 with hf
  obtain ⟨r, hr⟩ := IsAlgClosed.exists_pow_nat_eq ((2 * f) ^ 2 - 4) (n := 2) (by norm_num)
  set l := (2 * f + r) / 2
  set m := (2 * f - r) / 2
  have hlm : l * m = 1 := by
    simp only [l, m]
    linear_combination (-(1 : ℂ) / 4) * hr
  have hsum : l + m = 2 * f := by simp only [l, m]; ring
  have htr : (Tz (tilt w)).trace = l + m := by rw [trace_Tz, hsum]
  have hg : gauge (289 / 64) ((l + m) / 2) ≤ 1 := by
    rw [hsum, show 2 * f / 2 = f by ring]; exact gauge_f_tilt w hw
  have hl : ‖l‖ ≤ 4 := norm_le_four_of_gauge hlm hg
  have hm : ‖m‖ ≤ 4 := norm_le_four_of_gauge (l := m) (m := l) (by rw [mul_comm]; exact hlm)
    (by rw [add_comm]; exact hg)
  have hb := norm_pow_entry_le (Tz (tilt w)) hlm htr (det_Tz _) hl hm
    (norm_Tz_tilt_le w hw) n i k
  calc ‖(Tz (tilt w) ^ (n + 1)) i k‖ ≤ (n + 1) * 4 ^ n * (25 / 8) + n * 4 ^ n := hb
    _ ≤ 33 / 32 * ((n + 1 : ℕ) : ℝ) * 4 ^ (n + 1) := by
        push_cast
        rw [pow_succ]
        have h4 : (0 : ℝ) ≤ 4 ^ n := by positivity
        nlinarith

end Unit

end QcaFormal
