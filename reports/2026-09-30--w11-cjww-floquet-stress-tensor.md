# W11_CJWW_FLOQUET_STRESS_TENSOR_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W11_CJWW_FLOQUET_STRESS_TENSOR_GATE](../theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md), frozen at commit \`cfdc5c6059a169028b38fa326444286d9703e8e5\`.  
**Certificado exacto:** [verify_w11_ir_stress_source.py](../scripts/verify_w11_ir_stress_source.py), added at commit \`97592a465e40a3769980bcd64623c2c3ac8da3c9\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
W11_CJWW_FLOQUET_STRESS_TENSOR_GATE =
LOW_ENERGY_LOCAL_STRESS_SURROGATE_PASS /
EXACT_FLOQUET_STRESS_OPEN

F1 = PASS
F2 = PASS
F3 = OPEN
F4 = OPEN
\`\`\`

The exact CJWW walk admits finite-range lattice bilinears whose narrow-band
limit reproduces the Weyl energy/momentum source structure needed by W10.
This is sufficient for a controlled low-energy matter-gravity bridge, but not
for an exact microscopic Floquet stress tensor.

## 1. F1 — branch-local Weyl generator

For CJWW Eq. (5.15), exact differentiation at the Weyl node gives

\[
W_0(p)
=
I+i\left(
p_1\sigma_1-p_2\sigma_2+p_3\sigma_3
\right)
+O(|p|^2).
\]

With

\[
E_0=\operatorname{diag}(1,-1,1),
\]

this is

\[
W_0(p)
=
I+i\sigma^aE_{0\,a}{}^ip_i+O(|p|^2).
\]

For a local branch of \(W_0=e^{-iH_{\rm eff}}\),

\[
\boxed{
H_{\rm eff}(p)
=
-\sigma^aE_{0\,a}{}^ip_i
+
O(|p|^2).
}
\]

Thus the low-energy matter generator is the expected Weyl Hamiltonian.

\[
\boxed{\texttt{F1 = PASS}.}
\]

## 2. F2 — finite-range IR energy source

Use the centered lattice derivative

\[
\nabla_i\psi_x
=
\frac{\psi_{x+\hat e_i}-\psi_{x-\hat e_i}}{2}.
\]

Its Fourier symbol is

\[
i\sin p_i.
\]

Define the local IR lattice Hamiltonian

\[
H_{\rm IR}
=
\sum_x
\psi_x^\dagger
\left(
i\sigma^aE_{0\,a}{}^i\nabla_i
\right)
\psi_x.
\]

Equivalently, a Hermitian bond decomposition is

\[
\varepsilon_x^{(i)}
=
\frac{i}{2}
\left[
\psi_x^\dagger M_i\psi_{x+\hat e_i}
-
\psi_{x+\hat e_i}^\dagger M_i\psi_x
\right],
\]

with

\[
M_i=\sigma^aE_{0\,a}{}^i.
\]

The total symbol is

\[
\boxed{
H_{\rm IR}(p)
=
-\sigma^aE_{0\,a}{}^i\sin p_i.
}
\]

Therefore

\[
H_{\rm IR}(p)
=
-\sigma^aE_{0\,a}{}^ip_i
+
O(|p|^3).
\]

Comparing with the branch-local exact Floquet generator,

\[
H_{\rm eff}(p)-H_{\rm IR}(p)
=
O(|p|^2).
\]

For matter supported in a narrow ball \(|p|\le\Lambda\), the generator
mismatch vanishes at least as \(O(\Lambda^2)\) as \(\Lambda\to0\).

This supplies a finite-range local **IR energy-density surrogate**.

## 3. IR momentum density

A local bond momentum-density surrogate is

\[
\pi_i(x)
=
-\frac{i}{2}
\left(
\psi_x^\dagger\psi_{x+\hat e_i}
-
\psi_{x+\hat e_i}^\dagger\psi_x
\right).
\]

Its Fourier symbol is

\[
\sin p_i
=
p_i+O(p_i^3).
\]

Thus it reproduces the continuum momentum density entering \(T^{0i}\) in the
Weyl narrow-band limit.

Together with the W5/W6 spatial tetrad-current operators, the project now has
local lattice representatives for all three continuum source types at IR
level:

\[
T^{00},\qquad
T^{0i},\qquad
T^{ij}.
\]

The precise Belinfante/frame symmetrization remains a continuum-level
identification, not an exact microscopic tensor equality.

\[
\boxed{\texttt{F2 = PASS}.}
\]

## 4. F3 — exact Floquet energy remains open

The exact CJWW object is a one-step unitary \(U_0\), not a continuous-time
Hamiltonian supplied as part of the microscopic definition.

A Floquet logarithm

\[
H_F=i\log U_0
\]

requires a quasienergy branch choice and is not, merely by its existence, a
canonical strictly local Hamiltonian density.

The repository does not currently contain a proof of a finite-range Hermitian
operator \(H_{\rm loc}\) such that

\[
U_0=e^{-iH_{\rm loc}}
\]

together with a strictly local exact energy continuity law.

Therefore the IR bond energy above must not be called the exact microscopic
CJWW energy.

\[
\boxed{\texttt{F3 = OPEN}.}
\]

## 5. F4 — exact microscopic momentum tensor remains open

Exact translation invariance of CJWW implies conservation of Bloch/crystal
momentum globally.

That does not by itself produce a unique strictly local momentum density and
one-step current satisfying a local continuity equation.

The bond operator \(\pi_i(x)\) is therefore certified here only as a
narrow-band representative of the continuum \(T^{0i}\), not as an exact
microscopic Noether density.

\[
\boxed{\texttt{F4 = OPEN}.}
\]

## 6. Consequence for W10

W10 can now be sharpened.

At low energy, the sourced Gu-Wen-type constraints can use finite-range CJWW
matter operators whose symbols converge to

\[
T^{00},\qquad T^{0i},\qquad T^{ij}.
\]

Thus a **low-energy local sourced-constraint bridge** is technically
available in principle.

But an exact all-momentum microscopic Einstein/Gauss constraint sourced by a
canonical CJWW Floquet stress tensor is not established.

The correct hierarchy is therefore

\[
\boxed{
\text{exact CJWW QCA}
\to
\text{controlled Weyl IR}
\to
\text{local IR stress surrogate}
\to
\text{sourced low-energy gravity constraints}.
}
\]

## 7. Scientific status

This is a useful positive result because the Floquet issue does not block the
emergent low-energy programme.

It does block a stronger claim:

\[
\text{“the exact microscopic QCA already carries a canonical local
stress-energy tensor.”}
\]

No such claim is made.

## 8. Terminal decision

\[
\boxed{
\texttt{LOW\_ENERGY\_LOCAL\_STRESS\_SURROGATE\_PASS /
EXACT\_FLOQUET\_STRESS\_OPEN}
}
\]

is the terminal state.

The next serious step is no longer algebraic component counting. It is to
construct one **joint low-energy model** combining:

- a Gu-Wen-type constrained helicity-2 sector;
- the CJWW Weyl matter sector;
- the W11 local IR stress sources;
- reciprocal matter-geometry coupling;

and then test whether its coupled linearized equations reproduce the
Einstein-Weyl system to controlled order.
