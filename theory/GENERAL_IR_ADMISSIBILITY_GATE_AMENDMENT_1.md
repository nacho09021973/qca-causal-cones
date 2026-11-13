# Amendment 1: active encoders and null resource actions

2026-11-13. Author: Codex (OpenAI). **APPROVED by the user
(«aprobado»), accepting the proposed treatment of null encoders and
continuation on active encoders after the Stage A report.** This text
records that approved scope before the continuation is executed.

## Reason and change

The Stage A report exhibits a permitted non-zero Hermitian generator
with `M chi = 0`; its resource state is unchanged and `eta_enc` is
undefined. Keep the original fixed basis, matrices, resource, walk and
profiles. Partition the basis by its action on the fixed resource:

- Active encoders: `M chi != 0`. Prove all three required leakage
  ratios converge, including a positive lower bound on the state
  denominator for sufficiently large N.
- Null encoders: `M chi = 0`. Record their exactly zero operational
  signal; do not assign a value to `eta_enc` or call them admissible
  under Definition 3.1.
- Non-zero detector projectors are the detector targets. Any zero
  projector already in a spanning set stays recorded as a zero signal
  with an undefined operator ratio, rather than an admissible effect.

After proving the active-case lemma, check that the non-vanishing
basis pair in B1 can be selected among active encoders and non-zero
detectors. This is a compatibility check conditional on B1's existing
asymptotic derivation, not a fresh independent verification of B1.

No matrix or protocol is replaced. The admissibility statement is
restricted to active encoders; B1's existence claim is retained only
if compatibility is proved. This amendment governs the admissibility
gate; it does not rewrite the frozen B1 documents or promote B1.

## Authorization, budget and stop

Resume Stage A on `Z^d` for one analytic session of at most 90 minutes.
Deliver a separate report citing this amendment's commit. Stop if an
active encoder has no positive eventual state-denominator bound or if
the B1 compatibility step fails; record the precise open obligation.
Same verdicts and PRELIMINARY evidence level as the original charter.
No new walk search, computation, external transmission or promotion.
Bravais Stage B remains separately unauthorized.
