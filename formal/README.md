# Lean formalization of Theorem 4.1 (explicit upper bound)

Lean 4 (`v4.31.0`) + Mathlib (`v4.31.0`, rev `fabf563`).  Machine-checks the
**non-asymptotic** part of `papers/ir-corona/ir-corona.tex`: the explicit
bound of Theorem 4.1, for every `N ≥ 2`.  No `sorry`; the main theorems
depend only on the standard axioms `propext`, `Classical.choice`, `Quot.sound`
(`#print axioms`).

## Build

```sh
cd formal
lake exe cache get   # prebuilt Mathlib
lake build
```

## What is proved

| Lean | Paper | Statement |
| --- | --- | --- |
| `Ssym`, `kernel` (`Symbol.lean`) | eq. (2), (3) | the symbol `S(p)` as a 2×2 matrix of Laurent polynomials; `G_N(d)` = coefficient of `e^{ip·d}` in `S^N` |
| `gauge_mul_le` (`Ellipse.lean`) | Lemma 5.1 | `E_a E_c ⊆ E_{ac}` for confocal ellipses, in gauge form, for all `a, c > 1` |
| `norm_le_four_of_gauge` | Lemma 5.2 (use) | if `l m = 1` and `(l+m)/2 ∈ E_{17/8}` then `‖l‖ ≤ 4` |
| `pow_succ_eq`, `norm_pow_entry_le` (`Chebyshev.lean`) | Lemma 5.3 (replaced) | `T^{n+1} = h_n T − h_{n−1} I` for unimodular 2×2 `T`, with no spectral gap needed |
| `det_Tz`, `trace_Tz`, `norm_Tz_tilt_pow_le` | proof of Thm 4.1 | at every tilted point `z = 2w`, `‖w_j‖ = 1`: `det = 1`, `f ∈ E_{17/8}`, `‖(T^N)_{ij}‖ ≤ (33/32) N 4^N` |
| `dft_coeff` (`Kernel.lean`) | eq. (11), contour shift | exact recovery of a box-supported Laurent coefficient from its values at `2ζ^k`, with `ζ` a root of unity (a finite DFT; no integrals) |
| `kernel_entry_bound` | proof of Thm 4.1 | `‖G_N(d)_{ij}‖ ≤ (33/32) N 4^N 2^{-(d₀+d₁+d₂)}` for all `d` |
| `sum_sub_ge` (`Theorem41.lean`) | eq. (6) | `u·(y−x) ≥ (3 − √3/2) N` on `𝒜_N × ℬ_N` |
| `kernel_bound_regions` | Thm 4.1 | `‖G_N(y−x)_{ij}‖ ≤ (33/32) N e^{−JN}`, `J = (1 − √3/2) log 2` |
| `card_regA_le`, `card_regB_le` | §3.1 | each region has at most `N³` sites (`N ≥ 2`) |
| `TN_bound` | Thm 4.1 | `‖P_ℬ S^N P_𝒜 ψ‖ ≤ 4 N⁴ e^{−JN} ‖ψ‖`, i.e. `T_N ≤ 4N⁴e^{−JN}` (stronger than the paper's `9N⁴e^{−JN}`) |
| `delta_le_four_T` | Thm 4.1 | `|⟨v₁,Ev₁⟩ − ⟨v₀,Ev₀⟩| ≤ 4T` when `‖v_b‖ ≤ 1`, `‖E‖ ≤ 1`, `‖v₁−v₀‖ ≤ 2T` |

The Lean proof of the power bound differs from the paper: it uses
Cayley–Hamilton with the complete homogeneous polynomials `h_n(λ, λ⁻¹)` and
entrywise bounds, instead of a Schur form and `Σ‖S_d‖ = 4`.  This yields the
sharper constant `4` in place of `9`.

## What is not formalized

* The identification `v₁ − v₀ = P_ℬ S^N P_𝒜 (U − I)ψ` with `‖(U − I)ψ‖ ≤ 2`, and
  the second-quantized trace distance `D_B`.  Both are one-line modelling
  steps; only the one-particle signal `δ` is covered through
  `delta_le_four_T`.
* Theorem 4.3 (the rate `K_*`, its uniqueness, and `J < K_* < log 4`),
  Theorem 3.3 (admissibility) and Theorem 4.4 (the leading asymptotics).
  Mathlib lacks the multidimensional Laplace method, lattice Poisson
  summation and analytic perturbation theory that Theorem 4.3 needs.
  Those parts rely on the paper's proofs, the scoped review records and the
  certificate scripts.

## Found while formalizing

The paper's Lemma 2.1 listed the axial jumps as `(0,0,±1)`; they are
`(±1,0,0)` (from `−i s₁` in the off-diagonal entries).  This is corrected in
the paper; nothing downstream depended on it.
