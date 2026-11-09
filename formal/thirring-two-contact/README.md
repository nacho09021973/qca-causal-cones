# Exact two-contact Thirring certificate (Lean core)

Lean `v4.31.0`; no Mathlib, external packages, floats or scientific axioms.
This subproject does not modify the existing Mathlib project in `formal/`.

```sh
cd formal/thirring-two-contact
lake build
```

Read [Challenge.lean](ThirringTwoContact/Challenge.lean) for all definitions
and statements, then [Solution.lean](ThirringTwoContact/Solution.lean) and
[Axioms.lean](ThirringTwoContact/Axioms.lean). Nine closed finite identities
are checked by kernel reduction (`decide`, not `native_decide`). Eight
theorems use no axioms; the eigenvector statement uses only `propext`.
Changing a proof to `sorry` fails the guarded axiom output.

The physical parameters are fixed: mu=3/5, nu=4/5, contact phase i.
Each free two-particle step is represented by Gaussian-integer numerators
with denominator 25. The initial logical supports are positions {2,3}
on an eight-site ring, two steps of range one: no boundary wrapping occurs.

The formal results include the exact first gate, free and actual Grams,
the second compressed matrix, its strict Gram deficit, the projector
identity, an eigenvector and a nonzero witness column deficit. Thus a
wrong sign, wrong compressed coefficient or fake proof is detectable.

Coverage precision: `FirstGate` checks the four basis columns; its extension
to arbitrary complex inputs uses linearity in the written modelling bridge.
`NoWrap` checks final support on the ring, not every intermediate path.
The separate two-step locality argument establishes absence of periodic
wrapping. See the [statement audit](../../reports/2026-11-08--thirring-lean-statement-audit.md),
which includes a clean rebuild without changing any Lean source.

The identification with the opposite-Gamma sector of fermionic Fock
space, the generic formula in arbitrary real mass/coupling and the norm
interpretation of the Gram deficit are explained in the
[scientific report](../../reports/2026-11-08--thirring-two-contacts.md).
They are not claimed as fully formalized here. No claim of universal
computation or a relativistic continuum limit is encoded.

Negative controls use the shared `lean-mutar` from PATH; no tool is copied:

```sh
lean-mutar formal/thirring-two-contact formal/thirring-two-contact/mutaciones.toml \
  --salida reports/2026-11-08--thirring-two-contact-lean-mutations.json
```

Run that command from the repository root. The output path must be fresh;
the recorded run rejects 3/3 mutations and restores clean compilation.
Tool provenance: herramientas `ce09890`.
