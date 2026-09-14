# Canonical promotion of the standard Weyl/Dirac gate

Date: 2026-09-14.
Evidence commit: `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.

## Reason for the status change

The initial freeze marked the massive derivation PRELIMINARY and required a
normalization-controlled standard Weyl/Dirac battery. The evidence commit now
contains that battery's contract, source review, analytic derivation, permanent
verifier and provenance record. The record reports 247 exact checks with zero
tolerance and the missing-dagger, reversed-phase-sign and omitted-mass-correction
negative controls. The analytic report supplies the mass-interval inequality
and the specified continuum limit; they are not inferred from the check count.

The user explicitly requested promotion of these restricted conclusions and
replacement of the next gate with a massless fixed-geometry rigidity test.
This is the reason-recording canonical update required by PROJECT_INSTRUCTIONS.

## Promoted conclusions only

- STANDARD WEYL/DIRAC EXACT GATE: PASS for the seven declared symbols and
  their standard Dirac couplings in d=1,2,3.
- At m=0: `c_0 = r_in = 1/sqrt(d)` in the frozen coordinates.
- For every `0 < m < 1`, with `F = arcsin(m) sqrt(1-m^2)/m`,
  `c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`.
- Exact finite-mass B* is REJECTED in that standard Dirac family under either
  specified extraction. The result is no longer preliminary.
- B*_0 is VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN.
- Both small-mass limits equal r_in: B*_cont is VERIFIED FOR STANDARD DIRAC
  COUPLINGS / GENERALITY OPEN, with the local continuum scope of the report.
- A remains OPEN; the established, qualified B_max and B_full rejections and
  Bernstein CLASSICAL / NOT NOVEL status remain unchanged.

The seven symbols share three dimension-specific geometries. This update
does not promote their enumeration to seven independent tests of generality,
an exhaustive classification, a formal proof certificate, or a novelty claim.
The m=1 support-collapse endpoint remains separate from the strict interval.

At finite mass, c_H and c_{ω^2} must be distinguished; the quadratic
mass-direction term accounts for their difference. No unspecified finite-lattice
c_IR replaces the two named extractions.

## Historical evidence and current authority

The initial-freeze report, old execution contract, exact-gate report,
verification record, source PDF and verifier remain unchanged from `2c7c2c9`.
Their pre-promotion wording describes their historical status. The live
authority is now [CURRENT_STATE](../state/CURRENT_STATE.md), which cites them
as evidence and this record as the promotion decision. Keeping them unchanged
preserves their original provenance hashes and check semantics.

Before promotion, the verifier was rerun without rewriting the stored record:

```sh
python3 scripts/verify_weyl_dirac_gate.py | cmp - reports/2026-09-14--weyl-dirac-verification.md
```

The comparison exited zero: the stored 247-check record reproduced byte for
byte. This command reuses the permanent scientific code and creates no temporary result.
Document checks also cover whitespace, control characters, internal links,
and the absence of changes to the frozen scientific evidence.

## Only next front

[MASSLESS INRADIUS RIGIDITY GATE](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
is OPEN. It fixes the baseline neighborhood, causal body, normalization,
unitarity, homogeneity and discrete isotropy. Its first task is an explicit
admissible-class contract, including internal dimension, representation and
gapless-sector quantifiers, before solving for new structural coefficients.

This promotion supplies the charter only. It records no new model search,
counterexample or rigidity theorem and authorizes no anisotropic detour or
new substrate class.
