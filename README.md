# qca-causal-cones

Finite-range quantum cellular automata (QCA): can one substrate, with one
fixed update rule, both compute universally and look relativistic at low
energy?

## Project question

Does a single finite-range QCA, evolving under one fixed local rule, admit
**both**

1. **universal quantum computation**: an encoding of qubits in its states
   such that the rule itself, with no external control of its free or
   interacting parts, implements an entangling gate set that composes into
   a universal set, with preparation and readout stated explicitly; and
2. **a relativistic low-energy regime of the same rule**: an effective
   propagation speed `c_IR` for its low-energy excitations, with the
   interacting dynamics, not only free envelopes, controlled?

The question is stated per code, per resource set (ancillas, measurement,
geometry) and per parameter choice. A negative answer for one code is not a
no-go for the substrate. The working model is the Thirring QCA
(`sources/1711.03920v1.pdf`, `sources/1804.08508v1.pdf`): a one-dimensional
Dirac walk with an on-site two-fermion phase, `U = F J`.

Two distinctions are kept throughout:

- `C_micro` (causal body fixed by locality), `V_grp^max` (group-velocity
  envelope) and `c_IR` (low-energy speed) are different objects
  ([`theory/THREE_VELOCITIES.md`](theory/THREE_VELOCITIES.md)); never write
  `v_max` unqualified.
- `c_IR` has units of length per time and an update frequency has units of
  inverse time. Comparing them needs a spatial scale, a time scale and the
  relevant dimensionless coefficient.

## Why the question changed

The repository started with a narrower question: can `c_IR` be derived from
the causal geometry of the substrate alone? The answer found is that, in
general, it cannot (summary below). The coexistence question above is more
concrete: it names the operations that must be shown, and each can be
proved or excluded for a declared code.

## Status of the coexistence question

Single source of truth: [`state/CURRENT_STATE.md`](state/CURRENT_STATE.md).
Roadmap: [`state/ROADMAP_2026-11-09.md`](state/ROADMAP_2026-11-09.md).
All entries below are for the declared code, rule and parameters only.

| Result | Report | Status |
| --- | --- | --- |
| Massless two-node code: a full crossing is an exact entangling gate and completed crossings compose; trajectory parities forbid a universal unitary set in this code | [two-node](reports/2026-11-08--thirring-two-node.md) | PRELIMINARY; Grok review with author repairs; Claude objections O1–O9 open |
| Massive code: bounded-duration entangling gates closed for the declared code and frame | [massive preflight](reports/2026-11-08--thirring-massive-preflight.md) | PRELIMINARY |
| M=1 microscopic code: one step is an exact maximally entangling gate `diag(1,i,i,1)` | [growing time](reports/2026-11-08--thirring-growing-time.md) | PRELIMINARY |
| A second consecutive contact leaks (worst leakage 288/625); finite identities checked in Lean | [two contacts](reports/2026-11-08--thirring-two-contacts.md) | PRELIMINARY |
| No exact recovery of the code at any later time `T >= 2` | [exact recovery](reports/2026-11-08--thirring-exact-recovery.md) | PRELIMINARY; Claude review «se sostiene» |
| No approximate recovery at growing times: a two-particle bound state keeps leakage of input 00 above `c > 0` | [approximate recovery](reports/2026-11-09--thirring-approximate-recovery.md) | **PROMOTED** 2026-11-09 (Grok review) |
| Vacuum one-particle sector of a density-collision QCA is exactly free at every coupling | [vacuum sector](reports/2026-11-06--interaction-vacuum-sector.md) | PRELIMINARY |
| Low-energy band-packet code: no entangler (positive leakage into the doubler-partner sector) | [low-energy packet](reports/2026-11-09--thirring-low-energy-packet.md) | **PROMOTED** 2026-11-14 (Astra review and re-review) |
| Flavour-packet code, opposite-moving packets: leakage-free entangling exchange gate `V = 1 ⊕ [[iy, x], [x, iy]] ⊕ 1`, `x = (√10 − 2)/6`, under `U^2` | [flavour packet](reports/2026-11-14--thirring-flavour-packet.md) | **PROMOTED** 2026-11-14 (Grok review) |
| Same-direction (overtaking) flavour packets act by the same family `V(r)`, `r = e^{Δθ}`; `V(r)` satisfies Yang–Baxter, `P V` the braid relation | [co-moving packet](reports/2026-11-14--thirring-comoving-packet.md) | **PROMOTED** 2026-11-14 (Astra review and re-review; owner review) |
| Under the premise F (multi-packet factorization), crossings at `χ = π/2` are nearest-neighbour matchgates `−P V(r)`: classically simulable with product flavour inputs and flavour readout | [A5 matchgates](reports/2026-11-14--thirring-matchgate-a5.md) | **PROMOTED** 2026-11-14, conditional on F (Astra review, two re-reviews; owner review) |

Read together: the fixed rule produces an exact entangling gate once, but in
the microscopic codes tested it neither keeps the code closed under
repeated contacts nor yields a universal set. In the flavour-packet code,
low-energy packets crossing in either direction act by one leakage-free
entangling family `V(r)`; under F, at `χ = π/2`, these crossings are
classically simulable matchgates, so crossings alone in that code and
with those resources are not a route to universality (an efficient
universal construction would imply BQP ⊆ P). Free nodal envelopes have
`c_IR = a/tau`. No interacting relativistic limit has been established.
Open: F itself, `χ ≢ π/2 (mod π)`, other codes, ancillas or measurement,
composition with controlled error, and the low-energy regime of the
interacting rule.

## Results inherited from the original question

- **Standard Weyl/Dirac gate: PASS** (d=1,2,3; seven standard symbols).
  Massless and continuum inradius matching hold; exact finite-mass matching
  fails for both `c_H` and `c_{ω^2}`.
  [Promotion record](reports/2026-09-14--standard-gate-promotion.md).
- **Strong `B_infty^*` rejected in the declared s=4 class**
  ([counterexample](theory/S4_STRICT_CONE_COUNTEREXAMPLE.md)); the Pavia
  s=2, d=3 equality `c_0 = c_strict^iso = 1/sqrt(3)` remains certified.
- **s=4 tetrahedral shift** (promoted 2026-11-09):
  [any U(4) coin](reports/2026-11-06--s4-general-coin-viability.md) gives
  `c = 1/3` for an untilted isotropic node at `k=0`, and an
  [explicit cyclic-symmetric realization](reports/2026-11-06--s4-cyclic-realization.md)
  has two such cones.
- Paper on the IR corona: [`papers/ir-corona/ir-corona.tex`](papers/ir-corona/ir-corona.tex),
  with its Theorem 4.1 formalized in Lean 4 ([`formal/`](formal/README.md)).
- Bernstein's inequality and its equality theory are prior art.
  **NOVELTY remains OPEN** for every result in this repository.

## How to work here

Read `CLAUDE.md`, `PROJECT_INSTRUCTIONS.md` and `state/CURRENT_STATE.md`
first. Every result follows the cycle: frozen contract in `theory/`,
execution in `reports/` with a permanent verifier in `scripts/`, independent
cross-family review, and a separate promotion commit. No result is promoted
because it fits the narrative.

```sh
pip install -r scripts/requirements.txt          # Python 3.12, sympy==1.14.0, numpy==1.26.4
python3 -B scripts/verify_<gate>.py              # run from the repo root; fails closed
cd formal && lake exe cache get && lake build   # Lean fragment
```

[`scripts/README.md`](scripts/README.md) states what each verifier certifies
and what it does not.

## Literature library

`biblioteca/` (git-ignored) holds the local PDFs. Before investigating a
question, read `biblioteca/INDICE.md`
(`grep -i <topic> biblioteca/INDICE.md`). The index locates papers and proves
nothing: read the PDF and cite `file.pdf p.N`, otherwise mark the claim
`[UNVERIFIED]`. Tags marked `proposed` were written by an AI. Regenerate with
`python3 ~/herramientas/biblioteca_catalog/build_catalog.py --repo .` after
editing `scripts/biblioteca_catalog/curated.csv`. `sources/` holds versioned
primary PDFs with recorded SHA256.
