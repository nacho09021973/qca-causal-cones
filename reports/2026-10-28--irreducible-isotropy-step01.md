# Irreducible isotropy matching gate: Steps 0–1 — 2026-10-28

Charter: [`IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md`](../theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md)
(preregistration commit `d112bb0`; Steps 0–1 authorized in `43fd00e`, user: "si, autorizo los
pasos 0-1"). Certificate: `scripts/verify_irreducible_isotropy_step01.py`
(SHA-256 `d414b446d476c646…`), 31/31 exact checks, 518 s, Python 3.12.3, SymPy 1.14.0.
Full verifier sweep before commit: 47/47 pass at `43fd00e` plus this certificate
([record](2026-10-28--irreducible-isotropy-step01-run_all.tsv)). Evidence level: **PRELIMINARY**. These are author-side computations; independent review is
pending, as the charter (Sec. 6) requires.

## Result

| Class | Group, internal dimension, irreducible `R` | Outcome |
|---|---|---|
| T3 | `T`, `s = 3`, spin 1 | `EMPTY_CLASS` |
| O3 | `O`, `s = 3`, spin 1 (equivalently T1 or T2) | `EMPTY_CLASS` |
| O4 | `O`, `s = 4`, spin 3/2 (G3/2) | `EMPTY_CLASS` |
| Control B | s=4 family `A_a` against `O`/spin 3/2 | `S4_FAMILY_OUTSIDE_O4` (for every `a`, since O4 is empty) |

In all three classes, no unitary symbol `U(k) = sum_{h in N_3} e^{-ik.h} T_h` (all eight cube
vertices, no on-site term) is covariant, `T_{gh} = R_g T_h R_g^dagger`, with the stated
irreducible `R`. The same holds for the `s = 2` spin-1/2 controls under `T` and under `O`.
The hypothesis "an irreducible internal representation restores `c_0 = c_strict^iso`" is
therefore **vacuous** in these classes: there is no admissible symbol to which it applies.
It is not refuted, and it is not confirmed. Steps 2–3 of the charter have no object.

## Step 0

1. **Sources.** P17 (D'Ariano–Erba–Perinotti, arXiv:1708.00826v2, local
   `biblioteca/1708.00826v2.pdf`, SHA-256 `dc4107946e601364…`), Definition 1 (arXiv PDF p.2):
   the isotropy group `L` permutes `S_+` transitively, with a projective unitary
   representation on `C^s`; irreducibility is not required. The classification is restricted
   to `s = 2` ("From now on we will restrict to s = 2", p.4). The question of the charter is
   not answered there. The repo's earlier audit records P17's d=3 projective image as the Pauli
   group {I, iσX, iσY, iσZ}, a `D2` image
   ([source audit](2026-09-14--massless-rigidity-source-audit.md), P17 Prop. 4).
2. **Character tables** (certificate). `2T` (order 24) and `2O` (order 48) are generated
   exactly in SU(2), and their maps onto `T` and `O` are checked homomorphisms. The 7 and 8
   listed characters are orthonormal and complete. Irreducible dimensions:
   `2T`: 1, 1, 1, 2, 2, 2, 3; `2O`: 1, 1, 2, 2, 2, 3, 3, 4. Irreducible representations of
   equal dimension differ by a one-dimensional character. Conjugation sees `R` only up to that
   scalar, so spin 1/2, 1 and 3/2 cover every irreducible `R` of dimension 2, 3 and 4. `O`
   is transitive on `N_3`; `T` and `D2` have two orbits of size 4.
3. **Control A** (certificate). Both published Pavia d=3 Weyl symbols (both chiralities):
   - the half-turns of `D2` have nonzero intertwiners (σz, σx);
   - the 3-fold rotation about (1,1,1) and the 4-fold rotation about z have only the zero
     intertwiner.

   So the Pavia symbols are `D2`-isotropic and not `T`- or `O`-isotropic, consistent with
   P17's Pauli image.
4. **Control B** (certificate). The s=4 family `A_a` (θ = π/4) has only the zero
   intertwiner for the 3-fold rotation, for generic `a`. For special values of `a` the
   conclusion follows from O4 being empty, because `A_a` is unitary with full `N_3`
   support.

## Step 1: method and controls

For each class:

- one coefficient per orbit (`T_{h0}`, plus `T_{-h0}` for `T`) is restricted to the commutant
  of `R` on the vertex stabilizer (order 3, lifted to order 6);
- the other vertices follow by covariance, and the certificate checks that this is
  independent of the coset representative;
- the coefficient unitarity identities `sum_{h'-h=ℓ} T_h^dagger T_{h'} = δ_{ℓ0} I` for all 27
  differences `ℓ` are split into real and imaginary parts;
- SymPy's exact Groebner basis (grevlex, rational arithmetic) is computed.

A basis equal to [1] means the system has no solution, even over C.

Controls in the certificate:

- the equation generator vanishes identically on the s=4 family and on both Pavia symbols;
- without the normalization `sum T^dagger T = I`, every class system is homogeneous, so the
  unit ideal comes from the normalization alone;
- **positive control:** the same pipeline with `D2` (lifted to Q8), spin 1/2 and two free
  orbit coefficients gives a non-unit ideal. That class contains the Pavia symbols.

Exploration before the certificate (scratch, not retained as evidence): a 200-start
least-squares search on the T3 system stayed bounded away from zero. It is mentioned only
because it led to the certificate. It is not cited as a result.

## Scope and limits

- Only the frozen classes: d=3, support exactly `N_3` with no on-site term, rotation groups
  `T` or `O` (no reflections or antiunitaries), covariance by conjugation as in P17
  Definition 1, irreducible `R` of dimension 2–4.
- Since `2T` and `2O` have no irreducible representation of dimension above 4, every
  irreducible-`R` class with `s ≥ 2` under `T` or `O` on `N_3` is covered by T3, O3, O4 and
  the two `s = 2` controls. The `s = 1` case (scalar walks, which P17 cites as trivial) is not
  certified here. `[UNVERIFIED]`
- Not covered: reducible `R` under `T`/`O`; other groups; other supports (on-site terms,
  larger neighbourhoods); `D2`-isotropic classes, where the s=4 counterexample lives.
- No statement about Steps 2–3 (slopes, strict bodies). They have no object in these
  classes.

## Consequence for the question

With the cubic-vertex geometry, isotropy under the full tetrahedral or octahedral rotation
group with an irreducible internal representation is incompatible with unitarity. The
`B_infty^*` question stays where it was. The repo's established cases (Pavia `s = 2`, the s=4
counterexample) are all `D2`-isotropic with reducible or `D2`-irreducible `R`. The live
rows are now `s = 2` without P17 Eq. (2), and representation conditions formulated for `D2`,
or for `T`/`O` with reducible `R`. Either would need its own charter.
