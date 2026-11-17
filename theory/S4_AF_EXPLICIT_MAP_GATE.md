# S4 family as an Arrighi-Facchini walk: explicit-map attempt

2026-11-17. Author: Claude Code (Claude Opus 5.5). Initial status
**OPEN / NOT EXECUTED**. User «si, push y redacción» (2026-11-17)
authorized drafting; user «autorizo que lo congeles» (2026-11-17)
authorizes freezing by this commit. Execution needs a separate user
authorization. One contract; successor of
`theory/S4_AF_REGROUPING_GATE.md` (verdict OPEN_AFTER_REGROUPING_ATTEMPT,
`b7859d1`).

## Known, question, abandonment

Known (with source):
- Family (`theory/S4_STRICT_CONE_COUNTEREXAMPLE.md`, `1dae941`): at
  theta = pi/4, A(k) = W F_x F_y F_z, F_i = exp(-i q_i Gamma_i) =
  e^{-iq_i} P_i^+ + e^{iq_i} P_i^-, q_i = k_i/sqrt3, W = I ⊗ exp(-i pi
  tau_z/4). In coordinates scaled by sqrt3 each F_i is a coinless
  conditional shift by ±1 along axis i on the two rank-two eigenspaces of
  the involution Gamma_i; the product has the eight corner displacements.
- AF (`sources/1609.00305v2.pdf`, Secs. II and IV; Step 0 of
  `reports/2026-11-17--s4-af-regrouping.md`): a homogeneous paired step
  along axis i acts on the grouped pair phi(x) = psi(x-1) ⊕ psi(x+1),
  x in 2Z, by G^(i) = E^(i)† W^(i) (P' ⊕ P)(E^(i) ⊕ E^(i)) (Eq. (36)), with
  the Hadamard pre-encoding of Eq. (4) inside E^(i); the (3+1) walk is
  prod_i U^(i) with re-encoding between axes; only one parity sublattice
  per axis is coupled (Fig. 1).
- The previous attempt found no separating invariant among strict-body
  shape, band count and node structure modulo global phase and time
  regrouping, and proposed this explicit construction.

Question: within the fixed reading and ansatz below, is there a choice of
s, constant coins W^(i) and encodings E^(i) such that the AF homogeneous
(3+1) walk equals the family, exactly, up to the declared equivalences?

Abandonment of the line (restricted novelty candidacy): an explicit map
verified exactly → the family is a specialization of AF; record it as
prior art and drop the candidacy. A proof that the ansatz cannot work
does NOT establish non-equivalence and does not end the line; it is
recorded with its obstruction.

## Fixed reading of AF (frozen; resolves the three open points of Step 0)

- R1: shifts as in AF Fig. 1 / Eq. (6): W^(i) takes the upper 2s
  components of phi'(x - 2 e_i) and the lower 2s of phi'(x + 2 e_i).
- R2: only one parity sublattice per axis is evolved; the other is a
  decoupled identical copy and is discarded (declared equivalence E7).
- R3: the zeroth-order condition Eq. (16) is not imposed at fixed eps
  (it constrains the eps -> 0 expansion only); W^(i), E^(i) are arbitrary
  constant unitaries, and E^(i) contains the Hadamard pre-encoding of
  Eq. (4) as AF state.

## Declared equivalences

(E1) constant unitary conjugation; (E2) global phase; (E3) orthogonal
lattice relabeling; (E4) cell regrouping by a finite-index sublattice;
(E5) time-step regrouping U -> U^n on either side; (E6) constant isometric
encoding; (E7) reduction to one of several identical decoupled copies;
(E8) uniform rescaling of lattice units (spacing 2 on the AF parity
sublattice ↔ spacing 1). No momentum-dependent maps.

## Ansatz (frozen)

A1. Each family factor F_i is to be realized by one AF paired step G^(i)
(under R1, R2, E8): choose W^(i), E^(i) so that G^(i) restricted to the
retained sublattice acts as a conditional shift by one (rescaled) site on
the eigenspaces of Gamma_i, with s = 2.
A2. The family coin W is to be absorbed into one W^(i) or into the
encodings, so that prod_i G^(i) = W F_x F_y F_z up to E1, E2, E6.
A3. If A1-A2 fail only because the AF time unit is two ticks, the
comparison is made with E5 at n = 2 on the family side (A(k)^2) before
declaring failure.

## Tasks

- T1. Write G^(i) as an explicit symbol on the retained sublattice
  (R1-R3), as a function of W^(i), E^(i), citing equations.
- T2. Solve A1 exactly: characterize all (W^(i), E^(i)) making G^(i) a
  coinless conditional shift on prescribed rank-two eigenspaces; or
  prove none exists, with the obstruction (e.g. the Hadamard
  pre-encoding mixing the two sites of a pair).
- T3. If T2 succeeds, solve A2 (and A3 if needed) exactly.
- T4. If an explicit map results, verify the identity of symbols for
  symbolic a with an exact SymPy verifier committed before running.
Exact algebra only; no numerical search as evidence. Budget: one session.

## Verdicts

- `AF_EQUIVALENT_VIA_ANSATZ`: explicit map, verified exactly (T4).
- `ANSATZ_OBSTRUCTED`: T2 or T3 proves the ansatz impossible under
  R1-R3; obstruction stated. Non-equivalence NOT established.
- `OPEN_AFTER_EXPLICIT_MAP_ATTEMPT`: undecided within budget.
Author results PRELIMINARY until an independent review.

## Not claimed under any verdict

Anything under other readings of AF, other ansätze, or equivalences not
declared; non-equivalence in general; novelty. NOVELTY = OPEN.
