# Observational signature of saturation: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact and interval
author checks plus written arguments; no independent review, no promotion.**

Contract [OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md](../theory/OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md),
frozen at `21af1dd`. Verifier committed before its first run at `658845a`.
First run passed 19/19.

## 1. Answer

In the 13 declared rows, under the dictionary hypothesis H_gamma (the
massless branch is the photon), these are the findings:

1. **"c is the largest isotropic speed the update allows" (S_in) does not
   imply that nothing outruns c.** Among the ceiling rows with d ≥ 2:
   - L2 and L3 have V_grp^max = c_0, exactly proved: nothing exceeds c.
   - L5a, L5b and L4 have certified super-c excitations.
   - Hg is `REFUTED_BY_ROW_L2` (and by L3).
2. **Observing that nothing exceeds c does not show that c is at the
   ceiling.** Below-ceiling rows show the same "delay-only, no witness"
   behaviour (L6c, L6d, L6f: no witness on the declared rays, delay-only
   near the node). Rows below the ceiling also show super-c (L6a, L6b,
   L3s4).
3. **The discrimination that does exist is partial:**
   - The only S_max row (L1, d = 1) has no correction at all
     (omega = |k|). Every d ≥ 2 row has one. So "no dispersion whatsoever"
     singles out exact saturation of the clock, which is possible only
     in d = 1.
   - An advance-only signature (superluminal in every direction at first
     order) appears only below the ceiling: L3s4, one cluster, for
     a^2 < (19 - 6 sqrt3)/11. Hh is `REFUTED_BY_ROW_L3s4`, decided by the
     parent table. No ceiling row shows it.

Route verdict: `DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS`, partial in
exactly the sense of item 3. The contract's abandonment condition (no
super-c anywhere and no difference in signatures) is not met. The
discrimination is one-directional and does not separate S_in from
below-ceiling in general.

## 2. Per row

| Row | d | Saturation | Excitation faster than c_0? | Signature under H_gamma (from the parent table) |
| --- | --- | --- | --- | --- |
| L1 | 1 | S_max | no, V_grp^max = c_0 proved (omega = abs(k)) | none |
| L2 | 2 | S_in | no, V_grp^max = c_0 proved | order 2, delay-only near node, anisotropic |
| L6e | 2 | S_in | no witness on declared rays | order 2, delay-only, anisotropic |
| L3 | 3 | S_in | no, V_grp^max = c_0 proved | order 2, delay-only, anisotropic |
| L5a | 3 | S_in | yes: interval-certified point (+111, abs(k) = 1/16) | order 1, both signs with direction |
| L5b | 3 | S_in | yes: interval-certified point | order 1, both signs |
| L4 | 3 | S_in | yes: interval-certified point (-111) | order 1, both signs |
| L3s4 | 3 | below | yes: existence near node (exact sign of beta); explicit k* not attempted (a symbolic) | order 1; one-signed iff a^2 < (19 - 6 sqrt3)/11, else both |
| L6a | 2 | below | yes: interval-certified point (theta = 60°) | order 1, both signs |
| L6b | 2 | below | yes: interval-certified point (theta = 0°) | order 1, both signs |
| L6c, L6d, L6f | 2 | below | no witness on declared rays | order 2, delay-only, isotropic |

"No witness on declared rays" is not a proof that V_grp^max = c_0
(contract Sec. 3, item 1).

## 3. Arguments

- **L1.** Tr U = z + 1/z and det U = 1 (exact), so cos omega = cos k and
  omega = |k| on the branch. Group speed is 1 = c_0 everywhere.
- **L2, L3.** Exact identities: Tr U / 2 = prod_j cos p_j, det U = 1, and
  c_0 = 1/L, with p_j = k_j/L and L = sqrt d. Then
  omega = arccos(prod cos p_j) and, with a_j = cos^2 p_j,

    L^2 |grad_k omega|^2 = sum_j (1 - a_j) prod_{i≠j} a_i / (1 - prod a_i).

  This is at most 1 iff f(a) = 1 - prod a - sum_j (1 - a_j) prod_{i≠j} a_i ≥ 0
  on [0,1]^d. f is multilinear, so its minimum is attained at a vertex.
  All vertex values are ≥ 0 (certified for d = 2, 3). Hence
  |grad omega| ≤ 1/L = c_0, with equality along the axes, so
  V_grp^max = c_0.
- **Rows with beta not identically 0.** The parent's exact expansion gives
  |grad eps_+|/c_0 ≥ 1 + 2 beta(n̂) t + O(t^2) along k = t n̂, with the
  radial derivative as a lower bound. beta is positive on a declared ray
  (exact):

  | Row | Ray | beta |
  | --- | --- | --- |
  | L5a, L5b | +111 | 1/9 |
  | L4 | -111 | 1/9 |
  | L6a | theta = 60° | sqrt15/36 |
  | L6b | theta = 0° | sqrt15/18 |
  | L3s4, upper-sign cluster | +111 or -111 | the two values sum to 2 beta0 > 0 for all 0 < a < 1 |

  So super-c holds for small t. For the 2x2 rows an explicit point on the
  rational grid is also certified by rigorous interval arithmetic. The
  certified lower bounds match c_0(1 + 2 beta t) at t = 1/16 to the
  expected order; for example L5a gives 0.5852 against 0.5854.
- **Signatures** are read from the promoted parent table (Sec. 1 and
  Sec. 3.3 of `reports/2026-11-02--dispersion-corrections-across-lattices.md`),
  transcribed into the script, not recomputed.

## 4. Deviation and limits

- **Contract defect.** The contract asked for k* with algebraic coordinates
  on a rational |k| grid, certified "by exact inequality (radicals,
  Sturm)". At rational |k|, e^{ik} is transcendental, so these
  requirements cannot all hold. The explicit witnesses are certified with
  outward-rounded interval arithmetic (mpmath.iv, 40 digits, irrational
  inputs enclosed within ±1e-55). Existence of super-c for every beta row
  also follows from exact signs alone.
- **Search.** Only the declared rays and grid were searched. No row was
  searched beyond them.
- **V_grp^max** remains OPEN for L6e, L6c, L6d and L6f.
- **Signatures** are leading-order and near the node only. Their range of
  validity is OPEN, as in the parent.
- **Scope.** No comparison with observational bounds (contract Sec. 5), no
  value of ell or of the clock frequency, and no claim that our universe
  is a QCA or a simulation.

## 5. What this says about "c is the clock, therefore it cannot be exceeded"

In these models, two statements are independent:

- c being the largest isotropic speed the update allows;
- c being unbeatable.

Some walks at that ceiling still let excitations outrun c (L5a, L5b, L4).
Some walks below it do not show any excitation faster than c on the
declared rays (L6c, L6d, L6f). Only exact saturation of the clock, which
for an isotropic c is possible only in one dimension, comes with no
dispersion at all. An observation that nothing outruns c would therefore
not, by itself, identify c with the clock in this class.

## 6. Verifier

[Script](../scripts/verify_observational_signature_gate.py),
[record](2026-11-09--observational-signature-saturation.txt),
[JSON](2026-11-09--observational-signature-saturation.json): 19/19.
Reviewed verifiers were imported read-only.
