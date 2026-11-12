# Which momenta carry the infrared operational signal: charter

2026-11-12. User choice «Dicotomía de portadores» after the second
general-rate diagnostic. Drafted and frozen by Claude (claude-opus-5-5)
under that choice. **Status: OPEN; frozen; Stage A authorized within the
budget of Sec. 6.** No external transmission, no promotion.

## 1. Known, question, abandonment

Known.

- G1. General rate (charter `GENERAL_IR_RATE_GATE.md` with Amendments
  1–4): under H1–H3, H4′, H5–H10 the CJWW amplitude rate `K_*` is attained,
  in limsup form, by a protocol of the family, with the leading term at
  zero momentum and power `5 + d/2`. Stage 1 (upper bound for every
  operation) needs only H1 and `0 < K_* < inf`. Stages 1–2 PASS in one
  sealed Grok review; PRELIMINARY.
- G2. Second diagnostic (`reports/2026-11-12--general-ir-rate-round2.md`):
  in all seven walks with ballistic modes faster than `c_IR` along Bob's
  direction, zero momentum is not dominant at `xi_*`. In three of them
  (CJWW (5.12), Pavia A+, cyclic s=4) the dominant momenta have characters
  trivial on the lattice planes orthogonal to `xi_*`; in the rhombic
  dodecahedron walk (no fast modes, zero not dominant) they are non-trivial;
  in four product walks H3 fails and the characters were not evaluated.
  Floating-point diagnostic.
- G3. In the proof of G1 (manuscript Layers (c)–(d) and their
  generalisation), a dominant point with trivial character contributes at
  the same layer order as zero momentum, with phases `omega^j` on the depth
  index; a non-trivial character loses a relative `N^(-3/2)` per side
  through in-plane Poisson summation (the profiles' rims).

**Question.** When zero momentum is not dominant, is the CJWW rate still
attained by an infrared-admissible protocol of the family, and which
momenta carry the leading term? Two regimes are separated in advance:

- **R1 (commensurate carriers).** Some dominant momentum `eta_k != 0` has a
  character trivial on the planes. Expected: (T) holds with power
  `5 + d/2`, the leading term carried by `eta_k` at full layer strength;
  infrared admissibility of the operations does not select zero momentum.
- **R2 (rim carriers).** Every dominant momentum has a non-trivial
  character. Expected: (T) holds with a smaller power, the leading term
  carried by the profiles' rims and depending on their order of vanishing.

**Result that ends the line.**

- (a) In R1, a walk satisfying the declared hypotheses for which the
  leading term vanishes for every protocol of the family (for example by an
  identically vanishing average of the complex depth factor): then the
  rate is not attained at that order and the line becomes a different
  question (a rate gap), to be chartered separately.
- (b) The R1 statement is a direct corollary of G1's proof with no new
  step: recorded as such; Stage A closes as a corollary.
- (c) Budget exhausted: `OPEN_AFTER_<analysis>`.

## 2. Class and hypotheses

The class of G1 as amended (Amendment 4 included). Hypotheses H1–H3, H5,
H7, H8 as in G1; H2 at the dominant set `D`, which does not contain zero.
For R1, the analogues of H6, H9 and H10 at a chosen trivial-character
point `eta_k`, to be stated in Stage A **before** they are used and frozen
by amendment. No hypothesis is added after a step needs it without an
amendment approved by the user.

## 3. Stages

- **Stage A (R1).** (i) Depth sums with phase `omega = e^(i phi)`:
  `S_omega(theta) = sum_j omega^j g(theta + j) = e^(-i phi theta) sum_n g^(2 pi n - phi) e^(2 pi i n theta)`.
  (ii) Global phases from the characters at `x_*`, `y_*` and from
  `e^(-i N eta_k.v_*)`, the eigenvalue phase and the free tail. (iii)
  Average over `N` of the leading bracket; condition for a positive
  density of `N` with the bracket bounded away from zero. (iv) Bilinearity
  to a basis pair. Check the outcome against W2/W3/W6 numerically only as
  a diagnostic.
- **Stage B (R2, not authorized by this charter).** Exact leading rim term
  and its dependence on the profile's vanishing order. Needs its own
  decision.

## 4. Verdicts

Per stage: `PROVED_UNDER_FROZEN_CONTRACT` / `COUNTEREXAMPLE_VERIFIED` /
`OPEN_AFTER_<analysis>` / `REDUCED_TO_PRIOR_ART_<source>`. Line: (a), (b),
(c). Floating point never enters a verdict.

## 5. What a positive outcome would and would not say

Would say: in R1 walks, the exponential operational influence outside the
emergent cone is carried, at the CJWW rate, by momenta far from the
infrared node, even for infrared-admissible operations; "infrared
admissible" then does not mean "infrared carried". Would not say anything
about R2, about walks where H3 fails, about nature, or about novelty.

## 6. Budget and stop rules

Stage A: one session. No new walk constructions or searches. No change of
class or protocol after freezing; amendments recorded before use. No
external review without a separate user instruction.

## Naming addendum (2026-11-12)

User instruction: regime R2 is called the **Nacho Martín regime** in the
project's internal documents. Naming only; the frozen content above is
unchanged.

