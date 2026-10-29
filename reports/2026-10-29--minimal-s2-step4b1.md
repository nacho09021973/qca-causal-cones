# Minimal s=2 rigidity gate: Step 4b-1, exact class derivation — 2026-10-29

## Provenance

- **Charter:** [`MINIMAL_S2_RIGIDITY_GATE.md`](../theory/MINIMAL_S2_RIGIDITY_GATE.md),
  preregistration commit `785565c`.
- **Starting point:** stage (a), reviewed by Grok and promoted in `b67ea83`. It leaves five classes
  with a faithful projective action.
- **Authorization:** stage 4b-1 in `cfdc4a8` ("Autorizo 4b-1"). The user raised the budget from
  1 hour to 3 hours.
- **Timing:** started 13:06 UTC. The certificate passed at 13:13 UTC.
- **Certificate:** `scripts/verify_minimal_s2_step4b1.py`. The first version (`38f462c`,
  SHA-256 `5f91feaeece0d36a…`, 16/16) was reviewed by Astra
  ([review](../debates/2026-10-29--minimal-s2-step4b1-review-astra/informe_astra.md)). This
  repaired version (SHA-256 `5b0122f11df6f88d…`) runs 17/17 exact checks in about 110 s, Python
  3.12.3, SymPy 1.14.0. The repairs A-4B1-01..06 are listed at the end.
- **Full sweep:** 49/49 verifiers pass ([record](2026-10-29--minimal-s2-step4b1-run_all.tsv)),
  rerun after the repairs ([record](2026-10-29--minimal-s2-step4b1-repairs-run_all.tsv)).
- **Evidence level:** **PRELIMINARY**. First round of review (Astra) accepted the per-class
  results and requested six repairs, applied here; second round pending.

## Result

| Class (stage (a)) | Real parameters | Outcome |
| --- | --- | --- |
| `(O)`, family F | 4 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(T, tetrahedron)`, family P | 8 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(D4)`, family F | 8 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(C4, face)`, family P | 16 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(V4, tetrahedron, Pauli)`, family P | 16 | `UNITARY_SYMBOLS_EXIST`. The ideal is not `(1)` (79 s). The explicit witness `U(q) = e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}` is a real point, checked in the certificate itself; the Pavia symbol of chirality 1 is a secondary control |

**Consequence.** In the frozen families (d=3, `N_3` without on-site term, `s=2`, proper cube
rotations, Eq. (2) not assumed), the only nonempty isotropy class is
`(V4, tetrahedron, Pauli)`: family P, `G = V4` (the three axial half-turns), `S_+` a tetrahedron,
`ρ` conjugate to the inclusion. Its group and representation coincide with P17's. The class is
not "P17 minus Eq. (2)" (charter, family P row, A-R1-03): it is the restriction to proper cube
rotations and an oriented four-generator presentation.
- The `C4` face class, the one where the general ceiling was not certified, is empty. Within the
  `C4` class the outcome `COUNTEREXAMPLE_VERIFIED_ABOVE` therefore has no object. In the
  surviving class it is still open: it depends on which nodes an admissible transport reaches
  (Step 4b-2).
- The `T` and `O` results match the step-01 `T2s`/`O2s` controls, which that certificate
  certifies.

**Not decided here:**
- the dimension and components of the `(V4, Pauli)` class;
- whether every member satisfies Eq. (2) (Q-a);
- nodes, `c_0`, `c_strict^iso` (Step 4b-2, not authorized);
- Q-b (Step 4a, not authorized).

## Method

**Parametrization.**
- For a faithful class, `ρ: G → SO(3)` is conjugate to the inclusion. A constant basis change
  `W` absorbs the conjugation and preserves unitarity, so emptiness or existence for
  `ρ` = inclusion holds for the whole class.
- Write `T_h = a_h I + b_h·σ` with `a_h ∈ C` and `b_h ∈ C^3`. Conjugation by the spin-1/2 lift
  of `g` acts as `b ↦ g b`, `a ↦ a`, with `g` an integer signed permutation matrix. Covariance is
  `a_{gh} = a_h`, `b_{gh} = g b_h`. All group arithmetic is with integers.

**Two constructions of the covariant space, with shared infrastructure.**
- (i) Per orbit: the base coefficient is restricted to the fixed space of its stabilizer, and
  the orbit is filled by covariance. Well-definedness is checked.
- (ii) All eight `T_h` are free and covariance is imposed as linear equations for every
  `(g, h)`, then solved.

Both use the same group action (`S0.act`), the same `matvec`, the same Pauli basis and the same
unitarity generator. They can detect an error in the stabilizer/orbit filling of (i), but not an
error in that shared code.
- In the four empty classes both give the same number of real parameters and the unit ideal.
- In `(V4, Pauli)` construction (ii) is only compared by the number of real parameters (16). Its
  Groebner basis is not computed. Equal dimension does not prove that the two subspaces are
  equal.

**Unitarity.** The 27 coefficient identities, split into real and imaginary parts, use the
reviewed step-01 generator. The reduced Groebner basis is exact (grevlex). A basis equal to `[1]`
means no complex solution, and hence no real solution.

**Existence.** An ideal other than `(1)` is not taken as existence. The real point is the
explicit witness proposed in the Astra review:
`U(q) = e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}`, that is
`T_{(x,y,z)} = P_x^x P_y^y P_z^z` with `P_j^{±1} = (I ± σ_j)/2`. The certificate checks, without
the imported unitarity generator or Groebner code (it still uses `S0.act` and `sym_zero`):
- all eight `T_h` are nonzero;
- Laurent unitarity in both orders, `Σ_{h'−h=ℓ} T_h^† T_{h'} = δ_{ℓ0} I` and
  `Σ_{h'−h=ℓ} T_{h'} T_h^† = δ_{ℓ0} I`, for every displacement `ℓ`;
- covariance `a_{gh} = a_h`, `b_{gh} = g b_h` for every `g ∈ V4` and `h ∈ N_3`.

The reviewed Pavia symbol of chirality 1
passes the same covariance check as a secondary control; its unitarity comes from
`verify_irreducible_isotropy_step01.py`.

**DEP19 (A30), audit only.** It was read, but not used for any outcome.
- It is the general `s=2` BCC family only modulo relabelling of the generators, the PT map
  `A ↦ A^†`, basis change and the swap 2↔3. Several steps rest on "it is easy to see".
- (A30) keeps a free unitary `V`. DEP19's Eq. (14) is the normalization `Σ_h A_h = I_s`, not an
  isotropy condition, and (A32) does not by itself impose the Pauli covariance.
- Using (A30) as a cross-check of the `(V4, Pauli)` class remains to be done.

## Scope and limits

- **Frozen families only.** The emptiness results need all eight `T_h != 0` only through the
  frozen class definition; the unit ideal holds without that condition.
- **What `UNITARY_SYMBOLS_EXIST` covers.** It certifies one real point. It says nothing about the
  rest of the class, about Eq. (2) or about speeds.
- **Ceiling.** The surviving class contains the axial `D2`, so the general ceiling
  `c_0 <= c_strict^iso` applies there, at nodes reachable by an admissible transport.
- **No novelty claim.** The group and representation of `(V4, Pauli)` are P17's.

## Repairs after the Astra review (A-4B1-01..06)

| ID | Repair |
| --- | --- |
| A-4B1-01 (dependencies not attached) | Existence no longer rests on `S1`: the explicit witness is checked inside the certificate. `S1` is still used for the unitarity generator and Groebner call, and is attached to the second round. |
| A-4B1-02 (no Groebner for `V4` in construction (ii)) | Text corrected: only the parameter count is compared there. |
| A-4B1-03 (shared infrastructure) | Constructions described as sharing infrastructure, with what they can and cannot detect. |
| A-4B1-04 (identification with P17) | Class named exactly; coincidence of group and representation with P17 only. |
| A-4B1-05 (`..._ABOVE`) | Restricted to the `C4` class. |
| A-4B1-06 (DEP19 Eq. (14)) | Corrected: (14) is the normalization `Σ_h A_h = I_s`. |

Second round (Grok, [review](../debates/2026-10-29--minimal-s2-step4b1-review-grok/informe_grok.md)):
all six repairs resolved and the five per-class conclusions confirmed by direct proofs. Its two
new objections are closed in the text: A-4B1-R2-01 by removing the uncertified sentence on
negative controls; A-4B1-R2-02 by qualifying "no imported code" (the certificate's own label
keeps that wording; it means no imported unitarity or Groebner code) and by not calling the
step-01 `T2s`/`O2s` controls anticipations. The certificate bytes are unchanged since the review.
Grok also notes that the witness is Pavia chirality `−1` in the convention of
`verify_weyl_dirac_gate.py`; chirality `1`, the secondary control, is a different point.

Not adopted as a result here: Astra's argument that every active unitary symbol of the
`(V4, Pauli)` class satisfies Eq. (2). It is an anticipation for Q-a, decided in Step 4b-2 with a
certificate.
