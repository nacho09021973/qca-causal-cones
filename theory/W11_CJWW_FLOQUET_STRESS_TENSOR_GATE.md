# W11_CJWW_FLOQUET_STRESS_TENSOR_GATE

**Fecha:** 2026-09-30.  
**Estado al congelar:** \`AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## 0. Input

Successor to

\`\`\`
W10 =
CONTINUUM_SOURCED_CONSTRAINT_BRIDGE_PASS /
MICROSCOPIC_CJWW_CHARGES_OPEN
\`\`\`

The missing objects are local matter sources corresponding to
\(T^{00}\) and \(T^{0i}\).

## 1. Single question

Does the exact CJWW discrete-time walk admit a controlled local
energy-momentum source suitable for the W10 constraints?

The gate distinguishes:

1. **IR/local surrogate:** a local lattice bilinear whose narrow-band limit is
   the Weyl stress tensor;
2. **exact Floquet stress:** a canonical strictly local microscopic
   \(T^{\mu\nu}\) obeying exact one-step continuity identities.

These are not conflated.

## 2. F1 — effective Weyl generator

From the exact CJWW symbol, derive

\[
W_0(p)
=
I+i\sigma^aE_{0\,a}{}^ip_i+O(|p|^2)
\]

and therefore a branch-local effective Hamiltonian

\[
H_{\rm eff}(p)
=
-\sigma^aE_{0\,a}{}^ip_i+O(|p|^2).
\]

## 3. F2 — local IR lattice surrogate

Choose symmetric finite differences

\[
\nabla_i\psi_x
=
\frac{\psi_{x+\hat e_i}-\psi_{x-\hat e_i}}{2}.
\]

Define a local first-derivative Weyl Hamiltonian density using the frozen
\(E_0\), and construct the corresponding standard continuum-limit bilinears
for energy and momentum density.

PASS requires only:

- finite spatial range;
- correct Weyl symbols through first order in \(p\);
- a controlled statement that errors vanish in the narrow-band
  \(p\to0\) limit.

## 4. F3 — exact Floquet energy test

Determine whether the repository has an exact strictly local Hermitian
generator \(H_{\rm loc}\) with

\[
U_0=e^{-iH_{\rm loc}}
\]

and a proved local energy continuity law.

Do not infer one merely from a branch of

\[
H_F=i\log U_0.
\]

## 5. F4 — exact microscopic momentum test

Translation invariance gives conserved crystal momentum globally. Determine
whether a strictly local momentum density/current satisfying an exact
one-step continuity equation has been constructed.

Global Bloch momentum conservation is not automatically such a local tensor.

## 6. F5 — W10 source level

If F1-F2 pass but F3-F4 remain open, authorize only a low-energy sourced
constraint bridge:

\`LOW_ENERGY_LOCAL_STRESS_SURROGATE_PASS /
EXACT_FLOQUET_STRESS_OPEN\`.

This can support a controlled continuum-emergence programme but not an exact
microscopic Einstein constraint.

## 7. Terminal states

1. \`NO_LOCAL_STRESS_SOURCE\`.
2. \`LOW_ENERGY_LOCAL_STRESS_SURROGATE_PASS /
   EXACT_FLOQUET_STRESS_OPEN\`.
3. \`EXACT_CJWW_FLOQUET_STRESS_PASS\`.
4. \`OPEN_AFTER_AUDIT\`.

## 8. Claim ceiling

A low-energy stress surrogate does not define an exact microscopic energy,
does not fix the gravitational coupling, and does not establish universal
equivalence-principle coupling outside the Weyl sector.
