# Substrate saturation, phase 0 — addendum on row L4 (CJWW (5.12), (5.15))

**Date:** 2026-11-03. **Branch:** `research/schur-stability-audit`.
**Addendum to:** [`2026-11-03--substrate-saturation-phase0.md`](2026-11-03--substrate-saturation-phase0.md)
(committed at `2f6160e`), under the contract
[`SUBSTRATE_SATURATION_PHASE0_GATE.md`](../theory/SUBSTRATE_SATURATION_PHASE0_GATE.md)
(`9bf3019`).
**Authorization:** user instructions, 2026-11-03 («vamos con L4, lee CJWW
(5.12) y (5.15)»; «adelante con (a), el addendum»).
**Author:** Claude Code (Claude Opus 5.5).
**Status: PRELIMINARY, not independently reviewed. This addendum does not
change any outcome of the audit.** The audit keeps `OPEN_AFTER_ROW_SURVEY`,
L4 stays unclassified there, and the two
`NO_COUNTEREXAMPLE_IN_SOURCE_TABLE` outcomes are unchanged. The contract
says phase 0 is documentary and that a flagged row is flagged «without
resolving» (Sec. 3.4); resolving L4 inside the audit would need an
amendment of the contract with independent review of the derivation
below (option (b) offered to the user), and preferably an exact verifier
(option (c), a computation needing its own charter). Neither is done here.

**Pre-step check.** Known: L4's pair `(r_in, c_0) = (1/sqrt3, 1/sqrt3)` is
traced to the c-across-lattices table (l. 147); its node is not established
in the frozen sense, because the promoted passages (CS Sec. 8.1–8.2) state
only an emergent isotropic IR cone. Question: do CJWW Eqs. (5.12) and
(5.15), as printed, contain what the frozen node condition (contract
Sec. 2.4) requires? Ends this line: if the source cannot decide it, or
shows the contrary, L4 stays unclassified and that is recorded.

## 1. What the source prints

Source: Cedzich, Joye, Werner, Werner, *Exponential tail estimates for
quantum lattice dynamics*, `sources/2408.02108v1.pdf`, Sec. 5.4, PDF
pp. 17–18 (printed pp. 16–17). Read in the PDF text in this session.

- Eq. (5.12), the «"Weyl equation" model» of Bialynicki-Birula, with
  `K = C^2`: `W(p_1, p_2, p_3) = e^{i p_1 σ_1} e^{i p_2 σ_2} e^{i p_3 σ_3}`.
  The text states «conical singularities at `p = 0`» and at the points with
  `p_i ∈ πZ`, and Eq. (5.14) `ω(p_∨ + p)^2 = (p_1^2 + p_1^2 + p_1^2) + O(p^3)`
  (printed with `p_1` three times; the intended `p_1^2 + p_2^2 + p_3^2` is
  an evident typographical error, recorded, not repaired).
- Eq. (5.15), «on the same lattice and also with `K = C^2`, and with exactly
  the same conical points»:
  `W = [[cos p_1 cos p_2 e^{i p_3}, −cos p_1 sin p_2 + i sin p_1],
  [cos p_1 sin p_2 + i sin p_1, cos p_1 cos p_2 e^{−i p_3}]]`,
  Eq. (5.16) `ω(p) = arccos(cos p_1 cos p_2 cos p_3)`, and the statement
  that the analytic continuation of `W` «is still a 2×2-matrix with
  determinant 1».

## 2. What follows from the printed formulas

Elementary derivations by the author, by hand, **not checked by any
script**. Convention as in the Weyl/Dirac verifier: `T_a := i ∂_{p_a} W`
at `p = 0`. (The overall sign of `T_a` depends on the momentum sign
convention and does not affect any clause below.)

**(5.12).**
(i) `W(0) = I`, scalar.
(ii)–(iii) Each factor is `cos p_a + i sin p_a σ_a`, so `∂_a W(0) = i σ_a`
and `T_a = −σ_a`: Hermitian and traceless.
(iv) `{T_a, T_b} = 2 δ_ab I`, hence `c_0 = 1` in CJWW units (unit lattice
spacing, one update per time unit), consistent with Eq. (5.14).
(v) Traceless plus (iv) gives `A(n)^2 = |n|^2 I` for `A(n) = n_a T_a`, the
equivalent form of the untilted condition declared in contract Sec. 2.4.

**(5.15).**
Unitarity for real `p` (checked by hand): the rows have norm
`cos^2 p_1 cos^2 p_2 + cos^2 p_1 sin^2 p_2 + sin^2 p_1 = 1` and are
orthogonal.
(i) `W(0) = I`.
(ii)–(iii) `∂_1 W(0) = i σ_1`, `∂_2 W(0) = −i σ_2`, `∂_3 W(0) = i σ_3`, so
`T = (−σ_1, σ_2, −σ_3)`: Hermitian and traceless.
(iv) The three anticommute and square to `I`: `{T_a, T_b} = 2 δ_ab I`,
`c_0 = 1`.
(v) As for (5.12), `A(n)^2 = |n|^2 I`.

**Support and units.** In both walks the composite support contains
`(±1, ±1, ±1)` (for (5.12), the product of three factors each with steps
`±e_a`; for (5.15), the diagonal entries `cos p_1 cos p_2 e^{±i p_3}`), so
`C_micro = [−1, 1]^3`, `r_in = 1`, as in CS Sec. 8.2 (l. 780). Hence
`c_0 = r_in` in CJWW units; rescaled to longest step 1 (divide by `sqrt3`)
this is `(1/sqrt3, 1/sqrt3)`, the pair of the c-across-lattices table
l. 147. The pair itself is still taken from that single source; the
rescaling is stated only to show consistency.

## 3. Reading

**Provisional, `[UNVERIFIED]`:** from the primary source, both CJWW walks
satisfy the clauses (i)–(v) of the frozen node condition and saturate
(`c_0 = r_in`). If this derivation were independently reviewed and adopted
by an amendment, L4 would be an admissible row and the cube substrate of L4
would have an established witness.

What this addendum does **not** do: it does not classify L4 in the audit,
does not change `OPEN_AFTER_ROW_SURVEY` to `DEFINITIONS_CLOSED`, does not
add a witness to Sec. 3 of the audit, and gives no evidence for (PH). Even
if adopted, the cube shape already has the BCC witness L5a; L4 would add a
second substrate (group) with the same shape, not a new shape, and would
not change F1 (the table still contains no parallelepiped that is not a
hypercube).

## 4. Open after this addendum

- Independent review of the derivation in Sec. 2 (needs user permission to
  send).
- Option (b), an amendment allowing a flagged row to be resolved from the
  primary source, and option (c), an exact verifier: not authorized.
- L3's node trace remains pending review, as recorded in the audit.
