# Promotion of active-protocol infrared admissibility

2026-11-13. User instruction: «push , promocion y posteriormente preparar
el contrato». Branch-local promotion on
`research/tetrahedral-support-rigidity-2026-11-09`; base `76c939a`.

## Promoted statement

`PROVED_UNDER_FROZEN_CONTRACT` under the admissibility charter (`ecc5827`)
and active/null Amendment 1 (`156657e`): for every fixed full-rank
Bravais lattice `L=B Z^d`, `d in {2,3}`, fixed finite internal dimension,
fixed positive-radius physical balls, frozen profiles and resource,
each fixed active Hermitian encoder `M chi != 0` and non-zero orthogonal
detector projector has the three required leakage ratios defined for
sufficiently large N and bounded by `O(N^(-1/2))`. Constants and thresholds
depend on the fixed data and lattice. `Z^d` is included.

Null encoders retain an exactly zero resource perturbation and signal;
their state ratio is undefined. A non-zero null generator still has the
operator-ratio bound. A zero detector has zero signal and an undefined
operator ratio. No uniformity over changing or degenerating data.

## Evidence and ceiling

- Written Stage A proof `bb3592b`; Bravais proof `6ddda97`.
- One sealed independent cross-family review: Claude Opus 5.5, PASS,
  no mandatory repairs, recorded at `fea31b9`. Tool commit
  `7d111a158edda04a469b59f0d380cd69d35bbdea`.
- Optional exposition O1–O8 applied at `76c939a`; not re-reviewed. The
  exact reviewed versions and their hashes remain in the sealed input
  and review header. No reviewed verifier bytes were changed; the
  result is analytic, not computational.

Evidence level: **ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS**. This is a
bounded repository promotion, not human verification or a novelty result.
The review's acceptance of compatibility with B1 is only a conditional
implication: any B1 basis pair with positive scaled limsup has non-zero
signal and is therefore active with a non-zero detector. B1's rate,
existence and Bravais-transfer dependencies are not independently
verified by this review and are not promoted here.

No promotion of the carrier theorem, an exact R1 example, the R2 regime,
the interacting coexistence question, or the separate Bravais rate
corollary. No change to the parent frozen B1 charter or its hypotheses.

## Publication boundary

Publish the current research branch, including its eight pending
admissibility commits and this separate promotion commit. No merge to
main. Checks: scope inspection, `git diff --check`, reviewed-document
provenance retained. Remote SHA equality is checked after the push;
the subsequent R1 draft is kept separate from this publication.
