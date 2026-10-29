# Minimal s=2 rigidity gate: Step 4b-1, exact class derivation — 2026-10-29

## Provenance

- **Charter:** [`MINIMAL_S2_RIGIDITY_GATE.md`](../theory/MINIMAL_S2_RIGIDITY_GATE.md),
  preregistration commit `785565c`.
- **Starting point:** stage (a), reviewed by Grok and promoted in `b67ea83`. It leaves five classes
  with a faithful projective action.
- **Authorization:** stage 4b-1 in `cfdc4a8` ("Autorizo 4b-1"). The user raised the budget from
  1 hour to 3 hours.
- **Timing:** started 13:06 UTC. The certificate passed at 13:13 UTC.
- **Certificate:** `scripts/verify_minimal_s2_step4b1.py`, SHA-256 `5f91feaeece0d36a…`. 16/16
  exact checks, about 110 s, Python 3.12.3, SymPy 1.14.0.
- **Full sweep:** 49/49 verifiers pass ([record](2026-10-29--minimal-s2-step4b1-run_all.tsv)).
- **Evidence level:** **PRELIMINARY**. Author-side computation, not yet reviewed.

## Result

| Class (stage (a)) | Real parameters | Outcome |
| --- | --- | --- |
| `(O)`, family F | 4 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(T, tetrahedron)`, family P | 8 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(D4)`, family F | 8 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(C4, face)`, family P | 16 | `EMPTY_CLASS`: unit ideal, by both constructions |
| `(V4, tetrahedron, Pauli)`, family P | 16 | `UNITARY_SYMBOLS_EXIST`. The ideal is not `(1)` (78 s), and the Pavia symbol of chirality 1 is a certified real point, covariant with `ρ` = inclusion |

**Consequence.** In the frozen families (d=3, `N_3` without on-site term, `s=2`, proper cube
rotations, no Eq. (2)), the only nonempty isotropy class is `(V4, tetrahedron, Pauli)`. That is
P17's isotropy setting without its Eq. (2).
- The `C4` face class, the one where the general ceiling was not certified, is empty. The
  outcome `COUNTEREXAMPLE_VERIFIED_ABOVE` therefore has no object.
- The `T` and `O` results match the step-01 `T2s`/`O2s` controls, which were anticipations
  there.

**Not decided here:**
- the dimension and components of the `(V4, Pauli)` class;
- whether every member satisfies Eq. (2) (Q-a);
- nodes, `c_0`, `c_strict^iso` (Step 4b-2, not authorized);
- Q-b (Step 4a, not authorized).

## Method

**Parametrization.**
- For a faithful class, `ρ: G → SO(3)` is conjugate to the inclusion. A constant basis change
  `W` absorbs the conjugation and preserves unitarity, so emptiness or existence for
  `ρ` = inclusion holds for the whole class.
- Write `T_h = a_h I + b_h·σ` with `a_h ∈ C` and `b_h ∈ C^3`. Conjugation by the spin-1/2 lift
  of `g` acts as `b ↦ g b`, `a ↦ a`, with `g` an integer signed permutation matrix. Covariance is
  `a_{gh} = a_h`, `b_{gh} = g b_h`. All group arithmetic is with integers.

**Two independent constructions of the same system (robustness check).**
- (i) Per orbit: the base coefficient is restricted to the fixed space of its stabilizer, and
  the orbit is filled by covariance. Well-definedness is checked.
- (ii) All eight `T_h` are free and covariance is imposed as linear equations for every
  `(g, h)`, then solved.

Both give the same number of real parameters and the same Groebner outcome in every class.

**Unitarity.** The 27 coefficient identities, split into real and imaginary parts, use the
reviewed step-01 generator. The reduced Groebner basis is exact (grevlex). A basis equal to `[1]`
means no complex solution, and hence no real solution.

**Existence.** An ideal other than `(1)` is not taken as existence. The real point is the
reviewed Pavia symbol. Its `I` and `σ` coefficients are checked to satisfy
`a_{gh} = a_h`, `b_{gh} = g b_h` exactly for every `g ∈ V4` and every `h ∈ N_3`. Its
unitarity was checked in the earlier certificates.

**DEP19 (A30), audit only.** It was read, but not used for any outcome.
- It is the general `s=2` BCC family only modulo relabelling of the generators, the PT map
  `A ↦ A^†`, basis change and the swap 2↔3. Several steps rest on "it is easy to see".
- (A30) keeps a free unitary `V`. (A32) already imposes DEP19's isotropy condition (14).
- Using (A30) as a cross-check of the `(V4, Pauli)` class remains to be done.

## Scope and limits

- **Frozen families only.** The emptiness results need all eight `T_h != 0` only through the
  frozen class definition; the unit ideal holds without that condition.
- **What `UNITARY_SYMBOLS_EXIST` covers.** It certifies one real point. It says nothing about the
  rest of the class, about Eq. (2) or about speeds.
- **Ceiling.** The surviving class contains the axial `D2`, so the general ceiling
  `c_0 <= c_strict^iso` applies there, at nodes reachable by an admissible transport.
- **No novelty claim.** The `(V4, Pauli)` setting is P17's.
