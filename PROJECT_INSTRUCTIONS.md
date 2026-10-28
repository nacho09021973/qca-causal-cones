# PROJECT_INSTRUCTIONS

## 1. Scope

This repository studies finite-range quantum cellular automata (QCA), their microscopic causal geometry, spectral propagation speeds, and relativistic low-energy limits.

The central scientific question is not whether locality gives a finite propagation bound; that is background. The live questions are:

- **A — IR universality:** why different low-energy species would share one relativistic causal cone;
- **B_infty^* — strict asymptotic matching:** under which explicitly stated structural hypotheses the massless relativistic speed `c_0` equals the strict asymptotic isotropic speed `c_strict^iso` of the same dynamics. This supersedes B* against the one-step inradius. The strong form, where locality, unitarity, homogeneity and discrete isotropy alone force the equality, is **REJECTED IN THE DECLARED s=4 CLASS**; see `state/CURRENT_STATE.md`.

**Scope (revised 2026-10-28, user instruction).** The substrate is a finite-range, translation-invariant QCA on a periodic lattice in d ≤ 3: one-particle or many-particle, free or interacting. Within that class, varying the lattice, the neighbourhood (including on-site terms) and the internal structure is in scope, because the question is which properties of the substrate fix `c`. Each variation still needs its own frozen charter. Anisotropic substrates are admitted only as controls of a stated hypothesis, never as a line of their own. Out of scope unless a successor charter explicitly opens it: substrates without translation invariance (causal sets, random lattices), quantum gravity, and model searches not tied to a frozen class and a stated hypothesis.

The previous rule ("do not broaden the project to causal sets, random lattices, interacting QCA, quantum gravity, or other substrate classes") dates from the opening of the project. It is replaced because the question now requires comparing substrates. Interacting QCA were already chartered on 2026-10-08.

## 2. Canonical authority

`state/CURRENT_STATE.md` is the single source of truth for project status.

If another file conflicts with it, `CURRENT_STATE.md` wins until explicitly revised by a new commit that records the reason.

## 3. Mandatory distinctions

Never use `v_max` without qualification. Keep distinct:

- `C_micro`: microscopic causal body fixed by locality;
- `V_causal^max`: maximum directional support of `C_micro`;
- `V_grp^max`: maximum group velocity actually realized by a QCA spectrum;
- `c_IR`: relativistic speed parameter of the low-energy effective theory.

For finite-range lattice QCA in more than one spatial dimension, treat `C_micro` as a convex body, not as a scalar speed.

## 4. Evidence levels

Every nontrivial claim must be tagged mentally as one of:

- **ESTABLISHED:** proved in-repo or directly supported by a checked primary source;
- **SUPPORTED:** consistent with checked examples but not established generally;
- **PRELIMINARY:** derivation or calculation not yet independently rechecked;
- **OPEN:** live conjecture/question;
- **REJECTED:** contradicted by proof, geometry, or explicit counterexample.

Do not promote PRELIMINARY to ESTABLISHED because it supports the narrative.

## 5. Method

Prefer exact algebra and geometry before numerical fitting.

For any candidate equality involving propagation speeds:

1. define the microscopic neighborhood and its normalization;
2. compute `C_micro = conv(N)` with physical scale restored only after the dimensionless geometry is clear;
3. compute its support function and inradius;
4. compute the exact Bloch unitary and eigenphases;
5. derive the appropriate low-energy Hamiltonian or dispersion expansion;
6. compare quantities only after checking that their definitions match.

For massive sectors, do not identify `c_IR` with `|∇ω(0)|`. At finite lattice mass, also do not assume that the coefficient extracted from `ω^2` is automatically identical to the coefficient of the linear spatial term in the interpolating Hamiltonian; lattice corrections can spoil that equivalence.

The standard Dirac battery establishes that these coefficients differ for
`0 < m < 1`. Use `c_H` and `c_{ω^2}` explicitly; identify them with a common
relativistic speed only in a specified limit or after an independent proof.

## 6. Novelty discipline

The scalar/trigonometric Bernstein derivative bound and its classical equality theory are prior art. Do not claim them as novel.

Potential novelty, if any, must lie in QCA-specific structural statements, causal-body geometry, exact matching/non-matching results, or new classification theorems that survive prior-art search.

## 7. Current gate

**Branch-local successor authorization (2026-10-08).** Direct user instruction
opens inverse design on `research/inverse-gravity-design`, governed by
`theory/INVERSE_GRAVITY_DESIGN_CHARTER.md` and the newest entry of
`state/CURRENT_STATE.md`. Within that charter, fixed-lattice interacting QCA
construction and collective geometry are allowed; exact CJWW recovery is not
required. Historical statements below that only point (3) is authorized do
not prohibit this separately authorized line. All prior evidence levels, closures and paused fronts retain their scope.
The opening authorizes investigation, not a gravity or novelty result.

The **STANDARD WEYL/DIRAC EXACT GATE is PASS** for its declared cases, on the
evidence committed at `2c7c2c9`. This does not establish generality or lift all
scope restrictions.

The **MASSLESS INRADIUS RIGIDITY GATE** (`theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md`)
is **HISTORICAL / COMPLETED BY COUNTEREXAMPLE FOR THE DECLARED s=4 CLASS**
(`theory/S4_STRICT_CONE_COUNTEREXAMPLE.md`, independently reviewed). It is
no longer the sole authorized next front.

- Strong `B_infty^*` is **REJECTED IN THE DECLARED s=4 CLASS**.
- The standard Pavia `s=2`, d=3 equality `c_0 = c_strict^iso = 1/sqrt(3)`
  remains **CERTIFIED** and is not affected.
- Rigidity in the published minimal `s=2` class, and in stronger classes with
  additional representation assumptions, remains **OPEN**.
- **NOVELTY remains OPEN.**
- **Only point (3), the strict-cone ceiling, is now chartered by direct user
  instruction (2026-09-16).** See `theory/STRICT_CONE_CEILING_N3_GATE.md`
  and `CURRENT_STATE.md` Sec. 7.2. The incomplete ratification remains
  incomplete; the full C gate, L1 and the metric-defect steps are not
  authorized. Other successor questions remain unchartered.
- Point (3) is **PROVED UNDER ITS FROZEN CONTRACT**, with evidence level
  `PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`: the review at
  `bd44122` accepts the proof at `db083af` without mandatory repairs.
  This records one independent review of the ceiling, not a five-member
  ratification, a full C PASS, a matching theorem, or a novelty result.

Rules that carry over to any successor gate:

- Before solving, freeze internal dimension, group/action and representation,
  node/sector and any irreducibility or minimality assumption. Every rigidity
  conclusion must retain these quantifiers.
- Vary admissible structural coefficients, not just transpose/chirality
  representatives with the same geometry and linear speed.
- Do not infer rigidity from a failed search, a finite scan or local isolation.
- Do not promote a family identity (such as the s=4 projector-metric rule) to
  a general QCA law without a separate proof.
- Stay within the scope of Sec. 1. Anisotropic substrates only as controls of a stated
  hypothesis. No model search without a frozen class and a stated hypothesis.
- Check primary classification assumptions before claiming a new rigidity theorem.

Negative results are valid project outcomes.

**Current physical-line navigation (2026-09-28).** Use the dated reading
guide in `state/CURRENT_STATE.md` and the detailed records in Sections 8–10.
The previous September 17 paragraph naming 4B as NOT_EXECUTED is historical:
Section 8.21 now records September 25 execution authorization, the negative
result and its limited review, and a later 4A authorization without a contract.
H1 remains OPEN and paused under the L2 stop record. The September 28 iid
discrimination-cost report is PRELIMINARY, pending independent review.
This documentation checkpoint does not change the point-(3) / Gate C
authorization, promote scientific evidence, or authorize new calculations.
