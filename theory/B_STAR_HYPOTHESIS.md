# B_STAR_HYPOTHESIS

## 1. Motivation

The original strong thesis identified the relativistic low-energy speed with the maximum microscopic speed of the substrate. That thesis fails generically for anisotropic finite-range lattice QCAs in spatial dimension `d >= 2`.

A weaker geometric candidate was proposed next:

`B*: c_IR = r_in(C_micro)`,

with `r_in(C_micro)` the inradius of the *one-step* microscopic causal body `C_micro = conv(N)`.

## 2. Correction (2026-09-14): `B*` is superseded by `B_infty^*`

`r_in(C_micro)` is a fact about a single update. It is not automatically the
speed actually reachable by strict ballistic propagation after arbitrarily
many updates: whether a one-step displacement `h` remains reachable at `n.h`
for every `n` depends on whether the Fourier coefficient of `U^n` there stays
nonzero, which `N` alone does not determine. Calling the relevant scalar an
"inradius" also silently assumes the strict asymptotic body is centered at
`v = 0`; a pure one-step shift already shows this can fail (Sec. 3 below).

The corrected object, defined precisely in
[`CAUSAL_BODY_GEOMETRY.md`](CAUSAL_BODY_GEOMETRY.md) Sec. 6, is: for
`S_n = {x : the Fourier coefficient of U^n at x is nonzero}`,

`h_infty(n̂) = limsup_{n->infty} (1/n) max_{x in S_n} n̂.x`,

`c_strict^iso = min_{||n̂||=1} h_infty(n̂)`, origin fixed at `v = 0`.

**The corrected hypothesis is:**

`B_infty^*: c_0 = c_strict^iso`,

for the declared gapless sector, in the same embedding/time convention used
to define `c_0`. This replaces `B*` as stated against `r_in(C_micro)`; the
old formulation is kept below only as history and as a special case.

**Status (2026-09-15, branch-local):** the strong form, where locality,
unitarity, homogeneity and discrete isotropy alone force `B_infty^*`, is
**REJECTED IN THE DECLARED s=4 CLASS**
([`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md)).
The standard Pavia `s=2`, d=3 equality (Sec. 6) remains **CERTIFIED** and is
not affected. Rigidity in the published minimal `s=2` class, and in stronger
classes with additional representation assumptions, remains **OPEN**.
**NOVELTY remains OPEN.** No successor scientific gate is currently
chartered; see the [canonical state](../state/CURRENT_STATE.md) Sec. 7.

General relation: `c_strict^iso <= r_in(C_micro)` always (trivial inclusion
`S_n/n subseteq C_micro`), so the old `B*` and the new `B_infty^*` coincide
exactly where a *separate* argument certifies `c_strict^iso = r_in(C_micro)`
for the case at hand — established so far only for the standard Pavia Weyl
family in d=3 (Sec. 4). Nowhere else in this repository is that equality
assumed.

## 3. Sanity check on the definition: pure shift

For `U` a pure shift by `h_0 != 0` (one-element support `N = {h_0}`),
`S_n = {n h_0}` exactly, so `h_infty(n̂) = n̂.h_0` and
`min_{n̂} h_infty(n̂) = -||h_0|| < 0`. There is no bidirectional isotropic
cone centered at `v = 0` here; `c_strict^iso` correctly reports a negative
value rather than being forced into a meaningless "inradius" of a
single-point body. No QCA in this repository's battery has singleton
one-step support; this is a check on the definition, not a claim about any
case here.

## 4. What `B_infty^*` does and does not say

`B_infty^*` does **not** say that `c_IR` equals the fastest microscopic direction.

`B_infty^*` does **not** say that the IR cone equals the entire one-step microscopic causal body `C_micro` in general — only that `c_0` matches the *strict asymptotic* isotropic speed of the same symbol, whatever that is.

`B_infty^*` does **not**, by itself, say `c_strict^iso = r_in(C_micro)`; that is a separate, case-by-case geometric fact (`CAUSAL_BODY_GEOMETRY.md` Sec. 6) which happens to hold exactly in the certified Pavia baseline below.

## 5. Current evidence

**STANDARD WEYL/DIRAC EXACT GATE: PASS.** The derivation, verifier, contract
and provenance at `2c7c2c9` establish `c_0 = r_in = 1/sqrt(d)` for the
declared standard massless family in d=1,2,3, in unit-neighbor and unit-time
coordinates. See the [canonical state](../state/CURRENT_STATE.md) and
[promotion record](../reports/2026-09-14--standard-gate-promotion.md). This is
the *linearized* IR slope versus the *one-step* inradius; Sec. 6 below adds
the exact, nonlinear certificate that closes the gap to `c_strict^iso` for d=3.

The seven symbols include transpose/chirality partners sharing geometry and
linear speed. They cover three dimension-specific geometries, not seven
independent tests of generality. No theorem for a general class follows.

## 6. Pavia d=3 baseline: `C_infty^strict = C_micro` exactly (2026-09-14)

For the standard d=3 Weyl symbols and their transposes (`A+, B+, A-, B-`),
every one-step corner `h` of `C_micro = [-1/sqrt(3), 1/sqrt(3)]^3` has a
Fourier coefficient `A_h` satisfying the exact identity `A_h^2 = alpha_h A_h`
with `alpha_h in {(1-i)/4, (1+i)/4}`, `alpha_h != 0` (rank-one, not
nilpotent). By the vertex/convexity lemma of
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md),
this gives `n.h in S_n` for every vertex `h` and every `n >= 1`, hence

`conv(S_n/n) = C_micro` for every `n >= 1`, so `C_infty^strict = C_micro`,

and therefore, in this baseline only,

`c_strict^iso = r_in(C_micro) = 1/sqrt(3) = c_0` — **EXACT, certified by
375 zero-tolerance checks** (`scripts/verify_weyl_dirac_gate.py`, addendum
`verify_vertex_idempotency`; record:
[`2026-09-14--vertex-idempotency-verification.md`](../reports/2026-09-14--vertex-idempotency-verification.md)).

This certificate is **BASELINE-SPECIFIC**. It answers Sec. 1.1's "when does
`c_strict^iso = r_in(C_micro)`" question for this one family in d=3; it says
nothing about d=1, d=2 (not checked here), and nothing about whether *any
other* admissible massless symbol sharing the same `N_3` also has this
property — an admissible symbol only needs `T_h != 0`, not non-nilpotent
powers, so a different symbol's `C_infty^strict` could in principle be a
strict subset of `C_micro`. See Sec. 9 for how this interacts with the
rigidity gate.

## 7. Massive warning

For the standard Dirac couplings and every `0 < m < 1`, define
`F = arcsin(m) sqrt(1-m^2)/m`. The exact result is

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in`, with `0 < F < 1`.

This is an established result for the declared family, no longer preliminary.
The quadratic mass-direction Hamiltonian correction accounts for the exact
discrepancy between the two extraction procedures.

Therefore the unrestricted statement

`c_IR(m) = r_in(C_micro) for all m`

is **REJECTED IN THE STANDARD DIRAC FAMILY** under either specified
finite-mass extraction. At m=1 the active support collapses; treat that endpoint
separately rather than extending the strict inequalities to it.

The restricted forms are:

### B*_0 — massless matching

`c_0 = r_in(C_micro)`.

**VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN.** For d=3 this is now
also known to equal `c_strict^iso` exactly (Sec. 6): the standard d=3 family
is the one case where `B*_0` and `B_infty^*` are certified identical, not
just linearly coincident. For d=1, d=2 only the linear-order statement
`c_0 = r_in` is established; the full `C_infty^strict = C_micro` computation
was not performed there and is not claimed.

### B*_cont — continuum/small-mass matching

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in(C_micro)`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN.** The continuum
scaling and local convergence scope are fixed in the exact-gate report. This
statement is about the one-step `r_in(C_micro)` at the level of the massive
extractions `c_H`, `c_{ω^2}`; it is unaffected by the `B_infty^*` correction,
which concerns the massless/gapless sector's asymptotic body.

These are logically distinct. In the declared standard family, continuum
matching holds while exact finite-mass matching fails.

## 8. Required mechanism

A successful explanation must do more than fit a known coefficient. It must explain why, once the microscopic neighbor geometry and normalization are fixed, the EFT selects the inradius rather than a smaller isotropic speed.

A candidate derivation should identify which assumptions are essential among:

- locality;
- unitarity;
- homogeneity;
- discrete isotropy;
- minimal internal dimension;
- analyticity / smooth low-energy branch structure;
- massless versus massive sector.

## 9. Falsifiers

`B_infty^*` is falsified for a symbol by an exact, nonzero, isotropic
massless coefficient `c_0` strictly below that *same symbol's own*
`c_strict^iso`. A symbol whose `c_0 < r_in(C_micro)` only because its own
`c_strict^iso` is already below `r_in(C_micro)` is **not** by itself a
falsifier of `B_infty^*`. (Erratum 2026-09-15: such a shortfall requires a
nilpotent vertex coefficient, Sec. 6, but vertex nilpotency does not by itself
imply it; see the gate charter's erratum.) Such a symbol
would falsify only the old, superseded `B*_0` statement against
`r_in(C_micro)`. Distinguish these two before claiming a counterexample.

This falsifier has been realized. The explicit s=4 family of
[`S4_STRICT_CONE_COUNTEREXAMPLE.md`](S4_STRICT_CONE_COUNTEREXAMPLE.md) has
`C_infty^strict = C_micro`, `c_strict^iso = 1/sqrt(3)` and
`c_0 = a/sqrt(3)` for `0 < a < 1`. It keeps `N_3`, the D2 action (with the
reducible representation `sigma_i (x) I_2`) and irreducible dynamics. It was
judged under the now historical
[MASSLESS INRADIUS RIGIDITY GATE](MASSLESS_INRADIUS_RIGIDITY_GATE.md), which
is no longer an active front. Any successor gate must still retain the
selected standard neighborhood, causal body, normalization, unitarity,
homogeneity and discrete isotropy, and freeze the internal dimension,
symmetry representation and massless sector before solving.

An exhaustive proof for one fixed class is a class-specific rigidity result;
a failed search or a test of equivalent representatives is not. Added
minimality or irreducibility assumptions must remain explicit in the conclusion.

B*_cont is falsified if a valid massive family has a small-mass/continuum limit whose relativistic speed does not approach the microscopic inradius.

A failure is scientifically useful: it identifies which extra structural principle, if any, is missing.
