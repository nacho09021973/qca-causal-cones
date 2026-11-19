# Scalar on-site term on N3 ∪ {0}: flat-band lemma — execution

**Date:** 2026-11-19. **Author:** Claude Code (Claude Opus 5.5).
**Contract:** [`ONSITE_SCALAR_FLAT_BAND_GATE.md`](../theory/ONSITE_SCALAR_FLAT_BAND_GATE.md),
preregistration commit `b2ffcdc`.
**Author verdict:** `PROVED_UNDER_FROZEN_CONTRACT` — **PRELIMINARY**, pending the
different-family review of contract Sec. 5. Not promoted.

## 1. Result

In d=3, on the support `S = N_3 ∪ {0}` with `N_3 = (±1,±1,±1)/sqrt3`, every
unitary symbol `U(k) = λ I + sum_{h in N_3} e^{-ik.h} T_h` with all eight `T_h`
nonzero has flat quasienergy bands: its eigenvalues lie in
`{e^{+i arccos λ}, e^{-i arccos λ}}` for every `k`. It therefore has no
isotropic cone with `c_0 > 0`. Existence of such a symbol is not claimed.

Since any irreducible internal representation of a group fixing the origin
forces a scalar on-site term (Schur), this applies to T3, O3 and O4 with an
on-site term. There the matching question `c_0 = c_strict^iso` has no object,
whether or not the class is empty.

## 2. Proof

1. **Scalar on-site.** Given in the frozen declaration; route by Schur for
   irreducible `R`. A global phase sets `λ >= 0`. `λ = 0` is the predecessor
   class (no on-site term), empty for T3/O3/O4. The `ℓ = 0` identity
   `λ^2 I + sum_h T_h^dagger T_h = I` gives `λ <= 1`, and `λ = 1` forces
   `tr sum_h T_h^dagger T_h = 0`, i.e. every `T_h = 0`. So `0 < λ < 1`.
2. **Vertex identities.** Coordinates of differences within `N_3` lie in
   `{0, ±2}/sqrt3`; those of `N_3` are `±1/sqrt3`. So the unitarity identity
   at `ℓ = h ∈ N_3` has exactly the pairs `(0,h)` and `(-h,0)`:
   `λ T_h + λ T_{-h}^dagger = 0`, hence `T_{-h} = -T_h^dagger` (checks 1–6).
   The identities at `ℓ ∈ (N_3 - N_3) \ {0}` do not involve `λ` and are those
   of the predecessor; they are not needed here.
3. **Anti-Hermitian part.** `V^dagger = sum_h e^{ik.h} T_h^dagger
   = -sum_h e^{ik.h} T_{-h} = -V`, so `U + U^dagger = 2λ I` (checks 8 and 10;
   wrong-sign negative control 9).
4. **Quadratic relation.** `U^2 - 2λU + I = U(U + U^dagger - 2λ I) + (I - U U^dagger) = 0`
   (check 11). Every eigenvalue is a root of `z^2 - 2λz + 1`, namely
   `λ ± i sqrt(1-λ^2)`, of modulus 1 and independent of `k` (checks 12–14).
   No continuity argument is needed.

A second route to step 4, by hand: `U^dagger U = (λ - V)(λ + V) = λ^2 - V^2 = I`
gives `V^2 = -(1-λ^2) I`, so `-iV` is Hermitian with eigenvalues
`±sqrt(1-λ^2)`, the same spectrum.

## 3. Certificate

`scripts/verify_onsite_scalar_flat_band.py`, SHA-256
`644b5181ecea1e53431b1c9b268c25cbbe9e48a71a52661ee5f496e2121fd035`.
Python 3.12.3, SymPy 1.14.0. Run from the repository root on 2026-11-19:
`14/14 checks passed`, exit code 0, under 1 s.

Not certified by the script: Schur's lemma and the irreducibility of the
T3/O3/O4 representations (cited from the predecessor, certified there); the
extension of the `s = 2, 3` matrix check to all `s` (argued in
`scripts/README.md`: each entry of `V + V^dagger` involves only two entries
of each `T_h`).

## 4. Scope and limits

- Only scalar `T_0`. A non-scalar on-site term (reducible `R`, or no
  symmetry) is not covered; there step 2 gives `T_0^dagger T_h + T_{-h}^dagger T_0 = 0`,
  which does not force flatness by this argument.
- Only `N_3 ∪ {0}`. The disjointness of step 2 is specific to this support;
  the mutation control shows how one extra displacement breaks it.
- Says nothing about interactions, other dimensions or nature.
- `NOVELTY = OPEN`; the lemma is elementary and may be known. No literature
  search was made.

## 5. Next step

Contract Sec. 5: sealed review by a model of a different family
(`revision-ciega`), citing this report's SHA-256, the verifier's SHA-256 and
the base commit. Sending needs the user's confirmation of the reviewer.
