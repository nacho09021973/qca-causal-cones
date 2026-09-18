import Mathlib

/-!
# Confocal ellipses and the Joukowski bound

`gauge A z = (re z)^2 / A + (im z)^2 / (A - 1)` is the squared gauge of the
filled ellipse `E_a` with foci `±1` and semi-major axis `a = √A`.

* `gauge_mul_le`: `gauge (A*C) (z*w) ≤ gauge A z * gauge C w`.  This is the
  product lemma `E_a E_c ⊆ E_{ac}` of the paper (Lemma 5.1), in gauge form.
* `norm_le_four_of_gauge`: if `l * m = 1` and `(l+m)/2` lies in `E_{17/8}`,
  then `‖l‖ ≤ 4`.
-/

noncomputable section

open Complex

namespace QcaFormal

/-- Squared gauge of the confocal ellipse with parameter `A = a^2`. -/
def gauge (A : ℝ) (z : ℂ) : ℝ := z.re ^ 2 / A + z.im ^ 2 / (A - 1)

lemma gauge_nonneg {A : ℝ} (hA : 1 < A) (z : ℂ) : 0 ≤ gauge A z := by
  unfold gauge
  have h1 : 0 < A - 1 := by linarith
  have h0 : 0 < A := by linarith
  positivity

/-- Product lemma for confocal ellipses, in gauge form. -/
lemma gauge_mul_le {A C : ℝ} (hA : 1 < A) (hC : 1 < C) (z w : ℂ) :
    gauge (A * C) (z * w) ≤ gauge A z * gauge C w := by
  unfold gauge
  simp only [Complex.mul_re, Complex.mul_im]
  set x1 := z.re
  set y1 := z.im
  set x2 := w.re
  set y2 := w.im
  have hA0 : 0 < A := by linarith
  have hA1 : 0 < A - 1 := by linarith
  have hC0 : 0 < C := by linarith
  have hC1 : 0 < C - 1 := by linarith
  have hAC : 0 < A * C := by positivity
  have hAC1 : 0 < A * C - 1 := by nlinarith
  -- coefficients of the difference, a quadratic form in (x1*y2, y1*x2) plus a square
  set α : ℝ := (A - 1) / (A * (C - 1) * (A * C - 1)) with hα
  set β : ℝ := (C - 1) / ((A - 1) * C * (A * C - 1)) with hβ
  set γ : ℝ := (A + C - 1) / ((A - 1) * (C - 1) * (A * C)) with hγ
  set κ : ℝ := 1 / (A * C * (A * C - 1)) with hκ
  have key :
      (x1 ^ 2 / A + y1 ^ 2 / (A - 1)) * (x2 ^ 2 / C + y2 ^ 2 / (C - 1))
        - ((x1 * x2 - y1 * y2) ^ 2 / (A * C) + (x1 * y2 + y1 * x2) ^ 2 / (A * C - 1))
      = α * (x1 * y2) ^ 2 + β * (y1 * x2) ^ 2 - 2 * κ * (x1 * y2) * (y1 * x2)
        + γ * (y1 * y2) ^ 2 := by
    rw [hα, hβ, hγ, hκ]
    field_simp
    ring
  have hαpos : 0 < α := by rw [hα]; positivity
  have hγnn : 0 ≤ γ := by
    rw [hγ]
    have : 0 < A + C - 1 := by linarith
    positivity
  -- α β - κ^2 = 1 / (A^2 C^2 (AC-1)) > 0
  have hdisc : α * β - κ ^ 2 = 1 / (A ^ 2 * C ^ 2 * (A * C - 1)) := by
    rw [hα, hβ, hκ]
    field_simp
  have hdpos : 0 < α * β - κ ^ 2 := by rw [hdisc]; positivity
  set P1 := x1 * y2
  set P2 := y1 * x2
  have hq : 0 ≤ α * P1 ^ 2 + β * P2 ^ 2 - 2 * κ * P1 * P2 := by
    have h1 : α * (α * P1 ^ 2 + β * P2 ^ 2 - 2 * κ * P1 * P2)
        = (α * P1 - κ * P2) ^ 2 + (α * β - κ ^ 2) * P2 ^ 2 := by ring
    have h2 : 0 ≤ (α * P1 - κ * P2) ^ 2 + (α * β - κ ^ 2) * P2 ^ 2 := by
      have := sq_nonneg (α * P1 - κ * P2)
      have := mul_nonneg hdpos.le (sq_nonneg P2)
      linarith
    rw [← h1] at h2
    exact nonneg_of_mul_nonneg_right (by linarith) hαpos
  have hrest : 0 ≤ γ * (y1 * y2) ^ 2 := mul_nonneg hγnn (sq_nonneg _)
  linarith [key]

/-- Larger confocal ellipses contain smaller ones. -/
lemma gauge_anti {A B : ℝ} (hA : 1 < A) (hAB : A ≤ B) (z : ℂ) :
    gauge B z ≤ gauge A z := by
  unfold gauge
  have hA0 : 0 < A := by linarith
  have hA1 : 0 < A - 1 := by linarith
  have h1 : z.re ^ 2 / B ≤ z.re ^ 2 / A :=
    div_le_div_of_nonneg_left (sq_nonneg _) hA0 hAB
  have h2 : z.im ^ 2 / (B - 1) ≤ z.im ^ 2 / (A - 1) :=
    div_le_div_of_nonneg_left (sq_nonneg _) hA1 (by linarith)
  linarith

/-- Joukowski bound: if `l * m = 1` and `(l + m)/2 ∈ E_{17/8}` then `‖l‖ ≤ 4`. -/
lemma norm_le_four_of_gauge {l m : ℂ} (hlm : l * m = 1)
    (hg : gauge (289 / 64) ((l + m) / 2) ≤ 1) : ‖l‖ ≤ 4 := by
  by_contra hcon
  push Not at hcon
  have hl0 : l ≠ 0 := by
    intro h
    rw [h, zero_mul] at hlm
    exact zero_ne_one hlm
  have hm : m = l⁻¹ := by
    field_simp
    rw [mul_comm]; exact hlm
  set X := l.re
  set Y := l.im
  set s := Complex.normSq l with hs
  have hsXY : s = X ^ 2 + Y ^ 2 := by
    rw [hs, Complex.normSq_apply]; ring
  have hs16 : 16 < s := by
    have h1 : (4 : ℝ) ^ 2 < ‖l‖ ^ 2 := by
      exact pow_lt_pow_left₀ hcon (by norm_num) (by norm_num)
    rw [← Complex.normSq_eq_norm_sq] at h1
    norm_num at h1
    exact h1
  have hspos : 0 < s := by linarith
  have hre : ((l + m) / 2).re = X * (1 + 1 / s) / 2 := by
    rw [hm]
    simp [Complex.add_re, Complex.inv_re, hs]
    ring
  have him : ((l + m) / 2).im = Y * (1 - 1 / s) / 2 := by
    rw [hm]
    simp [Complex.add_im, Complex.inv_im, hs]
    ring
  unfold gauge at hg
  rw [hre, him] at hg
  -- key polynomial facts: 16 (s+1)^2 > 289 s and 16 (s-1)^2 > 225 s for s > 16
  have k1 : 289 * s < 16 * (s + 1) ^ 2 := by nlinarith
  have k2 : 225 * s < 16 * (s - 1) ^ 2 := by nlinarith
  have hXY : 0 < X ^ 2 + Y ^ 2 := by linarith
  -- rewrite the gauge after clearing denominators
  have expand :
      (X * (1 + 1 / s) / 2) ^ 2 / (289 / 64) + (Y * (1 - 1 / s) / 2) ^ 2 / (289 / 64 - 1)
        = (16 * X ^ 2 * (s + 1) ^ 2 / 289 + 16 * Y ^ 2 * (s - 1) ^ 2 / 225) / s ^ 2 := by
    field_simp
    ring
  rw [expand, div_le_one (by positivity)] at hg
  have hX : X ^ 2 * s ≤ 16 * X ^ 2 * (s + 1) ^ 2 / 289 := by
    rw [le_div_iff₀ (by norm_num)]
    nlinarith [sq_nonneg X]
  have hY : Y ^ 2 * s ≤ 16 * Y ^ 2 * (s - 1) ^ 2 / 225 := by
    rw [le_div_iff₀ (by norm_num)]
    nlinarith [sq_nonneg Y]
  -- strictness: at least one of X, Y is nonzero
  have hstrict : s ^ 2 < 16 * X ^ 2 * (s + 1) ^ 2 / 289 + 16 * Y ^ 2 * (s - 1) ^ 2 / 225 := by
    rcases lt_or_eq_of_le (sq_nonneg X) with hx | hx
    · have hX' : X ^ 2 * s < 16 * X ^ 2 * (s + 1) ^ 2 / 289 := by
        rw [lt_div_iff₀ (by norm_num)]
        nlinarith
      nlinarith
    · have hy : 0 < Y ^ 2 := by linarith
      have hY' : Y ^ 2 * s < 16 * Y ^ 2 * (s - 1) ^ 2 / 225 := by
        rw [lt_div_iff₀ (by norm_num)]
        nlinarith
      nlinarith
  linarith

end QcaFormal
