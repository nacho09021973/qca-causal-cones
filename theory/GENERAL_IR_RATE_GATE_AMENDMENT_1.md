# Amendment 1 to the general infrared operational rate charter

2026-11-12. Drafted by Claude (claude-opus-5-5) after Stage 0–1 and the
Stage 2 reduction (`reports/2026-11-12--general-ir-rate-stages-0-1.md`,
Stage 2). **Status: APPROVED by the user 2026-11-12 (choice «Aprobar la enmienda»);
in force from this commit.** The
frozen charter `GENERAL_IR_RATE_GATE.md` (`aa6c5f6`) is not edited.

## Reason

The reduction of non-vanishing to linear algebra found two situations that
H1–H5 do not exclude and in which the leading term can vanish for every
protocol of the family: linearly dependent dominant eigenvectors at
several trivial points, and a depth factor that is not positive at points
other than `eta = 0`. Written after the reduction, and declared so.

## Changes

- **H4 is replaced by H4′:** `eta = 0` is one of the dominant points of H2
  (its character is trivial on every lattice plane).
- **H6 is added (independence):** the right or the left dominant
  eigenvector at `eta = 0` is not in the complex span of the corresponding
  eigenvectors at the other dominant points with trivial character.
  Automatic when `eta = 0` is the only such point.

Nothing else changes: class, protocol family, stages, budget, verdicts,
stop rules and the result that ends the line. K3 satisfies H4′ and H6
(report, Stage 0(i) and Stage 2). A walk satisfying H1–H5 but not H4′ or
H6 is outside the amended class; whether (T) holds there is Stage 3.

## Effect on what a positive outcome would say

The amended statement is narrower: it covers walks whose tilted symbol is
dominated at zero momentum. Dropping H4′ or H6 is a separate question.
