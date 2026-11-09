# Observational signature of saturation: results

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: exact checks plus
written arguments; one sealed cross-family review (GPT-6 Astra) with
repairs applied, not re-reviewed; no promotion.**

Contract [OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md](../theory/OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md),
frozen at `21af1dd`. Verifier committed before its first run at `658845a`;
first run reported 19/19 (Sec. 6 qualifies this count).

[Sealed Astra review](reviews/2026-11-09-observational-signature-astra/informe_astra.md)
of the text at f9a638e (herramientas 97292a9): «reparación necesaria».
Each repair below was checked by the author before adopting it; the
original text is in git at f9a638e.

1. The claimed independence of "ceiling" and "unbeatable" (old Sec. 5 and
   item 1.2) was not demonstrated. Only one implication is refuted.
2. The interval certificates are not audited rigorous certificates: `ivnum`
   has no certified error bound, and `scale_of` compares floats. The
   statement that no floating point enters a verdict was false.
3. The "contract impossibility" diagnosis was too strong. It is a change of
   method.
4. L3s4 classification corrected: at a^2 = x_c, beta ≥ 0 with zeros; at
   a^2 = 1/2 the leading correction is isotropic.
5. "Ceiling" means the one-step geometric isotropic ceiling, not the
   asymptotic dynamical one.
6. The check count is qualified. The arrival-time formula holds at leading
   order only.

## 1. Answer

In the 13 declared rows, conditional on H_gamma (the massless branch is the
photon), with "ceiling" meaning the one-step geometric isotropic ceiling
c_0 = r_in:

1. **Being at the ceiling does not guarantee that nothing outruns c.**
   - L2 and L3 are at the ceiling and have V_grp^max = c_0, proved exactly.
   - L5a, L5b and L4 are at the ceiling and have excitations faster than
     c_0 close enough to the node. This follows from the exact sign of
     beta on a declared ray.
   - Hg is `REFUTED_BY_ROW_L2` (and by L3).
2. **The converse is OPEN.** Whether "nothing outruns c" implies being at
   the ceiling is not decided. No below-ceiling row is proved to have
   V_grp^max = c_0. L6c, L6d and L6f only have no witness on the declared
   rays, which is a finite search, not a proof.
3. **Spectral unbeatability does not imply exact saturation of the clock.**
   In L2 and L3, V_grp^max = c_0 < 1 = V_causal^max.
4. **Partial discrimination, conditional on H_gamma and on the declared rows
   and branches:**
   - The only S_max row (L1, d = 1) has no dispersion correction at all.
     Every d ≥ 2 row has one.
   - An advance-only first-order signature occurs for the upper-sign
     cluster of L3s4 when a^2 < x_c = (19 - 6 sqrt3)/11, a row below the
     ceiling. No ceiling row shows it. Hh is `REFUTED_BY_ROW_L3s4`, for
     that branch and that interval.

Route verdict: `DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS`, partial in the
sense of item 4. It is justified by these concrete differences in
signature, not merely by the abandonment condition failing.

## 2. Per row

| Row | d | Saturation (one-step) | Excitation faster than c_0? | Signature under H_gamma |
| --- | --- | --- | --- | --- |
| L1 | 1 | S_max | no: V_grp^max = c_0 (omega = abs(k) on regular branches) | none |
| L2 | 2 | S_in | no: V_grp^max = c_0 proved | order 2, delay-only near node, anisotropic |
| L6e | 2 | S_in | no witness on declared rays | order 2, delay-only, anisotropic |
| L3 | 3 | S_in | no: V_grp^max = c_0 proved | order 2, delay-only, anisotropic |
| L5a | 3 | S_in | yes near node (beta = 1/9 on +111) | order 1, both signs |
| L5b | 3 | S_in | yes near node (block with the matching sign) | order 1, both signs |
| L4 | 3 | S_in | yes near node (beta = 1/9 on -111) | order 1, both signs |
| L3s4 | 3 | below | yes near node, upper-sign cluster, every fixed 0 < a < 1 (no radius uniform in a) | see below |
| L6a | 2 | below | yes near node (theta = 60°) | order 1, both signs |
| L6b | 2 | below | yes near node (theta = 0°) | order 1, both signs |
| L6c, L6d, L6f | 2 | below | no witness on declared rays | order 2, delay-only, isotropic |

L3s4 signature, upper-sign cluster, with beta = B_0 + B_3 n1 n2 n3,
B_0 = sqrt3 (1-a^2)/(6a), B_3 = sqrt3 (2a^2 - 1)/(3a), and
min over n̂ of beta = B_0 - |2a^2 - 1|/(9a):

| Parameter | Leading correction |
| --- | --- |
| a^2 < x_c | beta > 0 on the whole sphere: advance-only at first order |
| a^2 = 1/2 (inside this interval) | isotropic, beta = sqrt6/12 |
| a^2 = x_c | beta ≥ 0, with zeros on certain diagonals; the next order decides there |
| a^2 > x_c | both signs |

The opposite cluster has the opposite sign.

"Order 1" or "order 2" names the first coefficient that is not identically
zero on the sphere. It does not cover the directions where that
coefficient vanishes.

## 3. Arguments

- **L1.** Tr U = z + 1/z and det U = 1, so omega = |k| on the principal
  zone. The regular branches have speed 1 = c_0.
- **L2, L3.** With Tr U = 2 prod cos p_j, det U = 1, p_j = k_j/L and
  c_0 = 1/L (identities checked in the script),

    L^2 |grad omega|^2 = sum_j (1 - a_j) prod_{i≠j} a_i / (1 - prod a_i),

  with a_j = cos^2 p_j. The function
  f = 1 - prod a - sum_j (1 - a_j) prod_{i≠j} a_i is multi-affine. It
  equals 0 at vertices with at most one zero coordinate and 1 otherwise,
  so f ≥ 0. An independent reading (from the review): f is the probability
  of at least two failures among independent trials with success
  probabilities a_j. Equality along the axes gives V_grp^max = c_0. Points
  with C^2 = 1 are excluded from the supremum; they do not change it.
- **Beta rows.** On a branch analytic along the ray (one-sided analytic
  choice, justified for a unitary analytic symbol with c_0 > 0),
  n̂·grad eps_+ = c_0 [1 + 2 beta(n̂) t + O(t^2)] ≤ |grad eps_+|.
  So beta(n̂) > 0 gives speed above c_0 for 0 < t < delta. This is
  existence near the node, not a point on the finite grid.
- **Signatures** are transcribed from the parent table into the script,
  not recomputed. The parent gate is promoted in CURRENT_STATE (entry
  "Gate promoted — 2026-11-02"). The parent report's own header still reads
  `PROMOTION_PENDING`, written before that promotion.
- **Arrival time.** If v = c_0 (1 + delta), then
  Delta T/(D/c) = 1/(1 + delta) - 1 = -delta + O(delta^2). The signs and
  orders above are leading-order statements. For L3s4, energy is measured
  from eps_0.

## 4. Method change and limits

- The contract asked for exact certification of k* by radicals or Sturm
  sequences. I used directed-rounding interval arithmetic (mpmath.iv), a
  change of method, not something forced by the contract (repair 3). Exact
  certification over the transcendental exponentials, with series and
  bounded remainders, was possible and was not done.
- The interval points are not audited rigorous certificates (repair 2): the
  enclosures of the irrational constants rely on a 70-digit evaluation
  without a certified error bound, L is chosen by float comparison, and
  block unitarity (detmod) is recorded but not required. They are reported
  values consistent with the near-node expansion; for example L5a gives
  0.5852 against c_0 (1 + 2 beta t) = 0.5854 at t = 1/16. They do not carry
  the verdict. Existence near the node rests on the exact beta signs.
- V_grp^max remains OPEN for L6e, L6c, L6d and L6f.
- The signatures are leading-order and near the node; their range of
  validity is OPEN.
- Scope: no comparison with observational bounds, no value of ell or of the
  clock frequency, and no claim that our universe is a QCA or a simulation.

## 5. What this says about "c is the clock, therefore it cannot be exceeded"

In these models:

- Being at the largest isotropic speed the one-step update allows does not
  guarantee that c is unbeatable (L5a, L5b, L4).
- c being unbeatable does not require exact saturation of the clock (L2,
  L3, with c_0 < V_causal^max).
- Whether "unbeatable" forces being at the isotropic ceiling is OPEN in the
  declared rows.

Only exact saturation of the clock, possible for an isotropic c only in one
dimension, comes with no dispersion correction at all.

## 6. Verifier

[Script](../scripts/verify_observational_signature_gate.py),
[record](2026-11-09--observational-signature-saturation.txt),
[JSON](2026-11-09--observational-signature-saturation.json): 19/19 lines
PASS (repair 6). The count mixes three kinds of entries:

- computed exact identities (L1, L2, L3, multilinear vertices);
- exact signs of transcribed coefficients;
- interval labels, not audited (Sec. 4).

The signature classes and the L3s4 threshold are transcribed text, not
checks. A search exception would have been labelled
`NO_WITNESS_ON_DECLARED_RAYS` instead of `OPEN (evaluation failed)`; none
occurred in this run. Reviewed verifiers were imported read-only.
