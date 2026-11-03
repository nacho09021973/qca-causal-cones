# s=3 isotropic rigidity gate: Step 0, determinant parity lemma — 2026-10-29

## Provenance

- **Charter:** [`S3_ISOTROPIC_RIGIDITY_GATE.md`](../theory/S3_ISOTROPIC_RIGIDITY_GATE.md),
  preregistration commit `58ea188`, Step 0 (points 1–5), anticipation B5.
- **Authorization:** stage (a), Step 0 only, "si a ambas" (2026-10-29), recorded in
  `CURRENT_STATE` in `e582939`. Budget 1 hour.
- **Timing:** started 18:09 UTC; certificate passed at 18:10 UTC.
- **Certificate:** `scripts/verify_s3_parity_step0.py`, SHA-256 `78f5ace96ce02023…`. 14/14 exact checks,
  about 5 s, Python 3.12.3, SymPy 1.14.0. It imports the stage (a) group helpers of
  `verify_minimal_s2_step00.py` and `published_symbol` of `verify_weyl_dirac_gate.py`, read-only.
- **Full sweep:** 51 verifiers, 0 failed, run 2026-11-03 ([record](2026-10-29--s3-parity-step0-run_all.tsv)).
- **Evidence level:** **PRELIMINARY**. Author-side computation, not yet reviewed.

## Result

In families P and F (`(V4, tetrahedron)`, `(T, tetrahedron)`, `(C4, face)`; `D4`, `O`), with
`s = 3`, support `N_3` and no on-site term, **every class is `EMPTY_CLASS`, for every projective
unitary `R`**. Union outcome: `S3_VACUOUS_IN_DECLARED_FAMILIES`, reached at Step 0. Steps 0′, 0″,
1 and 2 have no object.

The proof does not use active support (`T_h != 0`), Eq. (2), irreducibility, or any property of
`R` other than unitarity.

## Proof

Labels: `N_3 = {ε/√3 : ε ∈ {±1}^3}`; Fourier exponents are written in `ε` units, and
`U(k) = Σ_h e^{-ik·h} T_h`.

**Lemma 1 (parity).** For any `3 × 3` symbol supported on `N_3`, every monomial of `det U` has
all three exponents odd. Each term of the Leibniz expansion is a product of three entries, each a
combination of the monomials `e^{-ik·h}`, `h ∈ N_3`; its exponent is `ε^1 + ε^2 + ε^3`, and each
coordinate is a sum of three odd integers, hence odd (`±1` or `±3`). In particular the constant
monomial never occurs, for any coefficients. The certificate expands `det U` for a generic symbol
(72 symbolic entries) and finds exactly the 64 exponents `{±1, ±3}^3`.

**Lemma 2 (unimodular Laurent polynomials).** If a Laurent polynomial `f` satisfies `|f| = 1` on
the real torus, then `f` is a single monomial. Proof: on the torus `\bar f(k) = f^*(k)`, the
Laurent polynomial with conjugated coefficients and negated exponents, so `f f^* = 1` as Laurent
polynomials. Order exponents lexicographically; this order is compatible with addition. Let `a`
and `b` be the largest and smallest exponents of `f`. The exponent `a − b` of `f f^*` arises only
from the pair `(a, b)`: if `e − e' = a − b` with `e ≤ a` and `e' ≥ b`, then `e = a` and `e' = b`.
Its coefficient `c_a \bar c_b` is nonzero, so `a − b = 0`, and `f` has one monomial. The
certificate checks the uniqueness of the extremal pair on the support of Lemma 1. This is the
general form of A3 of the minimal charter; its stage (a) certified only the `s = 1` case.

**Lemma 3 (invariance).** If `U` is unitary, `det U` is unimodular, hence `det U = ζ e^{-ik·m}`
with `m` odd (Lemmas 1 and 2). Covariance `U(gk) = R_g U(k) R_g^†`, with `R` linear or projective,
gives `det U(gk) = det U(k)`, so `e^{-ik·g^T m} = e^{-ik·m}` for all `k`, that is `g^T m = m` for
every `g ∈ G`: `m` lies in the common fixed space of `G`.

**Common fixed spaces** (exact nullspaces in the certificate):
- `V4`, `T`, `D4`, `O`: `{0}`. Each contains the axial `V4`.
- `(C4, face)`: the rotation axis, here spanned by `(0, 1, 0)`; every vector has two zero
  coordinates.

Neither meets the odd coset. So no unitary covariant symbol exists in any of the five classes.

Element-wise control (charter repair G-S3-R2-01): a 3-fold rotation alone fixes the odd vector
`(1, 1, −1)` (for the element found). The decision uses the common fixed space of the whole group.

## Controls

- **Negative:** at `s = 2` and `s = 4` the same expansion, on an exact integer instance, has only
  even exponents and a nonzero constant coefficient (6 and −507). The parity obstruction does not
  fire where unitary symbols exist.
- **Positive:** the 4b-1 witness `e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}` (Pavia chirality −1)
  and both published Pavia symbols have `det U = 1`.

## Scope and limits

- Families P and F only, `s = 3`, `N_3`, no on-site term. Nothing about other groups, supports
  (an on-site term adds the even exponent `0` and breaks Lemma 1), reflections, antiunitaries or
  other `s`.
- The argument extends verbatim to every odd `s` on `N_3` without on-site term under these
  groups. The charter (Sec. 0) leaves that statement to a separate charter; it is not claimed here.
- This does not say which internal dimension is the smallest non-rigid one in general.
- T3 and O3, already `EMPTY_CLASS`, are consistent with this result; it does not depend on their
  certificate.
- **Novelty: OPEN.** The literature step of the charter has not been done.
