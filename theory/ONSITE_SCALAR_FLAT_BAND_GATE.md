# Scalar on-site term on N3 ∪ {0}: flat-band lemma

2026-11-19. Author: Claude Code (Claude Opus 5.5). Initial status
**OPEN / NOT EXECUTED**. The user chose option 1 («1», 2026-11-19) of the
proposal "contrato mínimo, un verificador exacto de dos o tres comprobaciones
en `scripts/` y una revisión de otra familia". That choice authorizes this
contract, its freezing by this commit and the execution of Sec. 3. The
sealed external review needs a separate confirmation of the reviewer before
any text is sent. The repository pause (`cff4bd9`) is lifted for this
contract only.

## Known, question, abandonment

Known (read in this session, with source):
- T3/O3/O4 are `EMPTY_CLASS` on `N_3` without an on-site term, under the
  rotation groups `T` and `O` with irreducible `R`
  (`theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`, preregistration
  `d112bb0`, promoted `5424771` on `research/inverse-gravity-design`; read
  with `git show 28c686e:<path>`; reconciled on this branch at `0f20d4e`).
  That report lists "other supports (on-site terms)" as not covered.
- Under `D2` no projective irreducible `R` with `s>2` exists (same
  charter, Sec. 0).
- The point-(3) ceiling `0 < c_0 <= c_strict^iso <= 1/sqrt3` concerns
  symbols with support `N_3` (`theory/STRICT_CONE_CEILING_N3_GATE.md`).

Question: on the support `S = N_3 ∪ {0}`, with a scalar on-site coefficient
`T_0 = λ I`, can a unitary symbol have any dispersion at all, and hence an
isotropic Weyl cone with `c_0 > 0`?

Abandonment: if any exact check of Sec. 3 fails, or the review finds a
contributing pair to the identity of Sec. 2(b) that the derivation omits,
the lemma is withdrawn and the on-site variant returns to OPEN. No partial
version is kept.

## 1. Frozen declaration

| Item | Declaration |
| --- | --- |
| Geometry | d=3; `N_3 = {(±1,±1,±1)/sqrt3}`; support `S = N_3 ∪ {0}`; all eight displacements active (`T_h ≠ 0` for every `h` in `N_3`); one complete update per time unit; `U(k) = T_0 + sum_{h in N_3} e^{-i k.h} T_h` on `C^s`, any finite `s >= 1` |
| On-site term | `T_0 = λ I` with `λ` in `C`. Global phase equivalence sets `λ >= 0`; it shifts quasienergies uniformly and leaves every group velocity unchanged |
| Route to the scalar | For any group `G` of linear maps of `R^3` that fixes `0` and acts with covariance `T_{gh} = R_g T_h R_g^dagger`, `T_0` commutes with every `R_g`. If `R` is irreducible (linear or projective), Schur's lemma gives `T_0 = λ I`. This covers T3, O3 and O4 with an on-site term. Schur's lemma and the irreducibility certified by the predecessor are cited, not recertified |
| Not covered | Non-scalar `T_0` (reducible `R`, or no symmetry); other supports; d ≠ 3 |

## 2. Claim under test (hand derivation before freezing, PRELIMINARY)

(a) `λ = 0` is the predecessor class, empty for T3/O3/O4. `λ = 1` forces
every `T_h = 0` by the `ℓ = 0` identity, contradicting full activity. So
`0 < λ < 1` in any nontrivial case.

(b) Differences of two elements of `N_3` have coordinates in
`{0, ±2}/sqrt3`; elements of `N_3` have coordinates `±1/sqrt3`. Hence for
`ℓ = h` in `N_3` the only pairs `(h_1, h_2)` in `S × S` with
`h_2 - h_1 = ℓ` are `(0, h)` and `(-h, 0)`, and the unitarity identity
`sum_{h_2-h_1=ℓ} T_{h_1}^dagger T_{h_2} = δ_{ℓ0} I` reads
`λ T_h + λ T_{-h}^dagger = 0`, i.e. `T_{-h} = -T_h^dagger`.

(c) With `V(k) = sum_h e^{-ik.h} T_h`, (b) gives `V^dagger = -V`, so
`U + U^dagger = 2λ I`. For unitary `U` this gives
`U^2 - 2λ U + I = U (U + U^dagger - 2λ I) = 0`. Every eigenvalue of `U(k)`
is a root of `z^2 - 2λ z + 1`, i.e. `e^{± i arccos λ}`, for every `k`.

(d) Conclusion: every symbol of the declared class, if one exists, has
flat quasienergy bands. Its group velocity vanishes identically and it has
no isotropic cone with `c_0 > 0`. Existence of a symbol in the class is
neither claimed nor needed.

## 3. Execution (authorized)

One permanent verifier `scripts/verify_onsite_scalar_flat_band.py`, exact
SymPy, fail-closed, run from the repository root:

1. Support combinatorics: `N_3 ∩ (N_3 - N_3) = ∅`; for each `ℓ` in `N_3`
   the contributing pairs in `S × S` are exactly `{(0,ℓ), (-ℓ,0)}`; for
   `ℓ` in `(N_3 - N_3) \ {0}` no pair involves `0`.
2. Mutation control: adding one extra displacement that creates a third
   pair for some `ℓ` in `N_3` is detected by check 1.
3. Symbolic anti-Hermiticity: with independent noncommutative `s × s`
   matrix symbols for the four `±` pairs and real `k`,
   `V + V^dagger = 0` after imposing `T_{-h} = -T_h^dagger`.
4. Polynomial identity: `U^2 - 2λU + I - U(U + U^dagger - 2λI) = I - U U^dagger`
   as a noncommutative identity, and the roots of `z^2 - 2λz + 1` have
   modulus 1 and do not depend on `k` for `0 < λ < 1`.

Report `reports/2026-11-19--onsite-scalar-flat-band.md`.

## 4. Outcomes

| Outcome | Meaning |
| --- | --- |
| `PROVED_UNDER_FROZEN_CONTRACT` | Sec. 2 holds: no symbol of the declared class has a cone with `c_0 > 0`; for T3/O3/O4 with on-site term the matching question has no object |
| `COUNTEREXAMPLE_VERIFIED` | An exact unitary symbol of the declared class with non-constant spectrum |
| `OPEN_AFTER_LEMMA_CHECK` | A check fails or the review finds a gap; the variant stays OPEN |

Ceilings: nothing about non-scalar on-site terms, reducible `R`, other
supports, interactions or nature. Novelty not assessed (`NOVELTY = OPEN`);
the lemma is elementary and may be known.

## 5. Review

The outcome stays PRELIMINARY until a sealed review by a model of a
different family (`revision-ciega`), citing the SHA-256 of the report and
verifier and the base commit. Promotion to `CURRENT_STATE.md` is a
separate commit.
