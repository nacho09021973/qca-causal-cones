# F8 Gu-Wen constraint architecture preflight

Date: 2026-09-30.

## 1. Question

Can the Gu-Wen qubit/spin construction be treated as the next family in the
atlas, and if so what is its admissible status for the CJWW matter-gravity
programme?

This is a source preflight. It does not construct a coupled CJWW/Gu-Wen
model, run a species metric test, or promote W9-W11.

## 2. Primary source read

Primary local PDF:

```text
biblioteca/arXiv-0907.1203.pdf
```

Read pages: p.1-4, p.10-13, p.21-23.

The abstract on p.1 distinguishes two models:

- L-type: controlled semiclassical result; helicity +/-2 modes are the only
  low-energy excitations, with cubic dispersion.
- N-type: intended linear dispersion, but the paper says there is no reliable
  approach and that the result is argued by spin-wave/quantum-freeze methods.

Pp.10-12 give the symmetric tensor field, vector constraint
`partial_i E^ij=0`, scalar constraint `R_ii=0`, the associated gauge
transformations, and the contrast between the local L-type Hamiltonian with
cubic dispersion and the nonlocal/continuum N-type route to linearized
Einstein form.

Pp.12-13 put the constraints on the cubic lattice through compactified
variables and energy penalties, giving a finite local Hilbert space on finite
lattices.

Pp.21-22 repeat the key reliability split: the L-type model remains reliable
with `omega ~ |k|^3`; the N-type lattice model cannot be calculated reliably
and needs numerical support for the linear-dispersion claim.

## 3. Existing in-repo records

The existing prior-art audit records that Gu-Wen already supply the relevant
low-energy helicity +/-2 and emergent linearized diffeomorphism precedent:

```text
reports/2026-09-30--w8-prior-art-gauge-audit.md
```

The W10 report tried to use Gu-Wen as a sourced-constraint bridge, then its
repair addendum downgraded the result:

```text
W10 = OPEN_AFTER_AUDIT
C5 = CONDITIONAL_ON_FULL_W11_LOCAL_SOURCE_MATCH / NOT_MET
```

The repair matters for F8: the continuum source logic is useful, but the local
CJWW stress/source insertion is still not available.

## 4. Kill tests for atlas status

### F8.1 — model separation

Do not merge L and N.

Result: PASS. L supplies the reliable controlled lattice graviton-like sector
with cubic dispersion. N supplies the intended linear dispersion only as a less
controlled proposal.

### F8.2 — direct CJWW matter rule

Does the source give a CJWW matter walk, a two-component Weyl QCA, or an exact
flat CJWW sector?

Result: FAIL. The source is a qubit/spin graviton-sector construction, not a
CJWW matter walk.

### F8.3 — sourced constraint bridge

Can the existing repository records source Gu-Wen-type scalar/vector
constraints with CJWW matter charges?

Result: OPEN. The continuum Weyl stress logic is structurally compatible, but
the required full local CJWW source matching and controlled constraint
identity remain absent after W10/W11 repair.

### F8.4 — novelty boundary

Can the project claim novelty for emergent helicity +/-2 modes or emergent
linearized diffeomorphism gauge structure from local qubits?

Result: FAIL. Gu-Wen is direct prior art for that claim.

## 5. Verdict

```text
F8_GU_WEN_CONSTRAINT_PREFLIGHT =
VACUUM_CONSTRAINT_ARCHITECTURE_PRIOR_ART /
DIRECT_CJWW_SOURCE_BRIDGE_OPEN
```

Evidence level: primary-source preflight plus existing in-repo repair records.
No independent new review.

## 6. Consequence

F8 is valuable as a constraint/gauge architecture and as a claim ceiling. It is
not the next executable metric/universality family until a new contract
specifies all of:

1. which Gu-Wen sector is used, L, N, continuum constrained theory, or another
   controlled low-energy sector;
2. how flat CJWW matter is included;
3. which local CJWW stress/charge operators source scalar/vector constraints;
4. how exact flat CJWW recovery is preserved at zero coupling;
5. what backreaction rule closes the coupled update.

Until then, F8 blocks overclaiming and helps aim the next constructive work.
