# W11_CJWW_FLOQUET_STRESS_TENSOR_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W11_CJWW_FLOQUET_STRESS_TENSOR_GATE](../theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md), frozen at commit \`cfdc5c6059a169028b38fa326444286d9703e8e5\`.  
**Certificado exacto:** [verify_w11_ir_stress_source.py](../scripts/verify_w11_ir_stress_source.py), added at commit \`97592a465e40a3769980bcd64623c2c3ac8da3c9\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

> **SUPERSEDED — see §9.** The block below is historical. Current gate:
> **OPEN_AFTER_AUDIT**. F3 has a scoped one-particle obstruction; the broader
> contract question remains OPEN.

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

## 9. Repair addendum — 2026-09-30 (supersedes the verdict above)

Authorization: the user's handoff after source check `7903713`. Inputs:
[repair list](../debates/2026-09-30--w9-w11-blind-review/reparaciones.md)
and [primary-source check](../investigaciones/2026-09-30-prior-art-walk-graviton/comprobacion.md).
The frozen report at `83acdfd` is preserved above, with an added superseded
banner. **Second-review update (2026-09-30):** both reviewers accept the
node/K/bound calculations and the scoped F3 proof at snapshot `86fe771`;
the review is recorded at `d6e74e6`. This §9 implements items 3, 5–7 of its
[README](../debates/2026-09-30--w9-w11-repair-review/README.md). The gate remains
OPEN; no joint Einstein–Weyl gate is frozen or opened by this review.

### A1 — nodes and species contract

For the actual CJWW (5.15) symbol, write

\[
W=a_0I+i\boldsymbol a\cdot\boldsymbol\sigma,\qquad
 a_0=c_1c_2c_3,\quad
 \boldsymbol a=(s_1,-c_1s_2,c_1c_2s_3),
\]

where here \(c_i=\cos p_i\), \(s_i=\sin p_i\).
Since \(\det W=1\), a degeneracy is \(W=\pm I\). The condition
\(|a_0|=1\) forces every \(|c_i|=1\): the following eight nodes exhaust the
Brillouin torus (coordinates understood modulo \(2\pi\)). Define the frame by

\[
W(p_*+k)=s_*[(1-|k|^2/2)I+i\sigma^a E_{*a}{}^i k_i+O(|k|^3)],\qquad
H_*(k)=i\log[s_*W(p_*+k)]=-\sigma^a E_{*a}{}^ik_i+O(|k|^3).
\]

The Pauli-vector part has no quadratic term. The table uses the normalized
frame of \(s_*W\), including at the π nodes.

| \(p_*/\pi\) | \(s_*\) | \(\operatorname{diag}E_*\) | \(\det E_*\) | Hamiltonian chirality \(\operatorname{sgn}\det(-E_*)\) |
| --- | --- | --- | --- | --- |
| (0,0,0) | +1 | (1,−1,1) | −1 | +1 |
| (1,1,0) | +1 | (−1,−1,1) | +1 | −1 |
| (1,0,1) | +1 | (−1,1,1) | −1 | +1 |
| (0,1,1) | +1 | (1,1,1) | +1 | −1 |
| (0,0,1) | −1 | (−1,1,1) | −1 | +1 |
| (0,1,0) | −1 | (−1,−1,1) | +1 | −1 |
| (1,0,0) | −1 | (1,−1,1) | −1 | +1 |
| (1,1,1) | −1 | (1,1,1) | +1 | −1 |

The review's signs −,+,−,+ refer to \(\det E_*\); with the Hamiltonian
convention \(W=e^{-iH}\), chirality has the opposite sign. Both conventions
have zero net chirality in the four zero-quasienergy species. F1 in §1
applies only near \(p=0\), not to the entire low-quasienergy sector.

**Selected option A1(i): retain all four zero-quasienergy species.** Any
subsequent continuum coupling must use their sum
\(T^{\mu\nu}_{\mathrm{tot}}=\sum_{s_*=+1}T_*^{\mu\nu}\), each with its own
frame, and one common geometry/coupling. This is a required contract, not a
constructed microscopic coupling or a proof of universal coupling. A
single-species truncation is not licensed. The π sector remains explicitly
outside this low-quasienergy contract; its exclusion under coupled dynamics
and all species-dependent source kernels must be checked before a joint PASS.
No suppression of intervalley scattering is inferred from this node table.

### A2 — replace the energy surrogate by K

For the **one-particle free walk** \(U\), set

\[
K=\frac{i}{2}(U-U^\dagger),\qquad K(p)=-\boldsymbol a(p)\cdot\boldsymbol\sigma.
\]

This is Hermitian and exactly conserved: \([K,U]=0\). If
\((U\psi)_x=\sum_r A_r\psi_{x+r}\), then
\(B_r=i(A_r-A_{-r}^\dagger)/2\) are the hopping matrices of K and
\(B_{-r}=B_r^\dagger\). One local Hermitian density is

\[
\varepsilon_x^K=\frac12\sum_r
[\psi_x^\dagger B_r\psi_{x+r}+\psi_{x+r}^\dagger B_r^\dagger\psi_x],
\qquad \sum_x\varepsilon_x^K=\langle\psi,K\psi\rangle.
\]

It has the spatial range of the walk (at most one site per coordinate).
For a freely second-quantized walk the corresponding conserved bilinear is
\(d\Gamma(K)\); taking \(i(\Gamma(U)-\Gamma(U)^\dagger)/2\) instead is not
this local bilinear. No interacting QCA claim is made.

On the union of the four balls \(|k|\le\Lambda\le1/2\) around \(+I\) nodes,
let \(P_\Lambda\) be the band projector. Here \(\cos\theta=\prod_i\cos k_i>0\),
\(\sin^2\theta=1-\prod_i(1-\sin^2k_i)\le|k|^2\), hence
\(0\le\theta\le\arcsin\Lambda\). Spectral calculus gives
\(K=\sin H_{\rm eff}\) on this branch, so

\[
\|(K-H_{\rm eff})P_\Lambda\|
\le\frac{(\arcsin\Lambda)^3}{6},\qquad
\|(U^n-e^{-inK})P_\Lambda\|
\le |n|\frac{(\arcsin\Lambda)^3}{6}.
\]

The second estimate follows by telescoping/Duhamel for the two unitary
propagators. It is useful for \(|n|\Lambda^3\ll1\), and uses invariance of
\(P_\Lambda\) under the free walk. The projector is a restriction on states,
not a claim of finite-range band selection.

K still vanishes at **all eight nodes**. It is not the all-zone quasienergy,
not a positive energy, and not a continuous-time generator of U. Its exact
free conservation does not prove conservation after a geometry coupling.
More precisely, on a local branch about a node of sign s*,
\(U=s_*e^{-iH_*}\), hence \(K=s_*\sin H_*\). At the −I nodes,
\(K=-H_*+O(|k|^3)\): its leading energy sign is opposite to the shifted
Weyl generator. For a fixed spectral direction its sine dependence also
identifies eigenphases θ and π−θ; K cannot resolve that quasienergy ambiguity.
The construction is established here algebraically; no checked primary
literature attribution for this particular energy surrogate is claimed.

The old \(H_{\rm IR}\) in §2 is superseded. Its commutator with W has a
nonzero quartic term. Near p=0 its mismatch with \(H_{\rm eff}\) is cubic,
not merely the loose quadratic bound quoted there. In fact
\(\|K-H_{\rm IR}\|\le\Lambda^3\) on the p=0 ball, from
\(|1-\cos u|\le u^2/2\), so its free dynamical error is bounded by
\(|n|[\Lambda^3+(\arcsin\Lambda)^3/6]\). On the p3 axis both surrogates
are \(-\sin p_3\sigma_3\), while \(H_{\rm eff}=-p_3\sigma_3\); the cubic
coefficient is \(1/6\). This also rejects the review's incorrect universal
cubic formula for \(H_{\rm eff}\) (repair B4).

### A3 / F2 — explicit downgrade of the local-stress claim

F2 now certifies K as an energy **charge** surrogate on the stated band,
the integrated canonical momentum near p=0, and the q=0 spatial
**tetrad-conjugate** structures from W5/W6. It does not certify all local
components of a symmetric Belinfante tensor. No longitudinal Ward identity
is inferred merely from the integrated charges. At another node,
\(\sin(p_{*i}+k_i)=(-1)^{p_{*i}/\pi}k_i+O(k_i^3)\); the original momentum
surrogate is therefore not one common envelope-momentum operator for all
four species without further matching.

The kernels at nonzero momentum transfer, spin improvement, frame
symmetrization and full four-species local source construction remain open.
This chooses the explicit downgrade permitted by A3. It supersedes the
claim in §§3,6 that all three local source types needed by W10 were supplied.

### C3 / F3 — one-particle obstruction with full Z³ translation invariance

Restrict to a **one-particle** generator (or its number-conserving quadratic
second quantization), invariant under **every translation in ℤ³**, with
the original **two-component cell**. For this walk, suppose a periodic
continuous Hermitian 2×2 \(H(p)\) on the connected Brillouin torus obeyed
\(e^{-iH(p)}=W(p)\). Then \(\operatorname{tr}H(p)\in2\pi\mathbb Z\) is
constant, since \(\det W=1\). Also \([H,W]=0\). Approaching any Weyl node
along k=tn and dividing that commutator by t gives
\([H(p_*),\sigma^aE_{*a}{}^in_i]=0\) for every n. The frames in the table
are invertible, so \(H(p_*)=c_*I\). At a +I node this requires
\(c_*\in2\pi\mathbb Z\), hence an even multiple of \(2\pi\) for the
trace. At a −I node it requires \(c_*\in(2\mathbb Z+1)\pi\), hence an odd
multiple. This contradicts constant trace.

Thus no such continuous logarithm exists, in particular none with
absolutely summable translation-invariant hopping matrices (which would
have a continuous symbol). This includes finite range. This proof uses
both kinds of nondegenerate Weyl node; it is not a no-go for all QCA, for
translation-breaking generators, or for time-dependent local circuits.
In particular it does not exclude generators invariant only under a
supercell subgroup, or interacting many-body generators of the second-quantized
update. Discontinuous logarithms are also outside the exclusion. These
cases remain open, so **the broader F3 question in the frozen contract is
not closed**. Both second-round reviewers accept the proof in the stated
one-particle/full-ℤ³ class; their acceptance does not enlarge that class or
establish novelty. Po et al.'s chiral-edge result is not used as evidence.

### C3 / F4 and primary antecedent

The bond operator in §3 has total symbol \(\sin p_i I\), so its integrated
charge is **exactly conserved** by the free walk. The missing step in F4 is
a constructed local one-step current and its relation to the symmetric
stress, not global conservation. Both that current and the q≠0 Belinfante
identification remain open in this certificate.

Arnault–Cedzich, `biblioteca/arXiv-2208.14997.pdf` pp.1–2, construct a
(1+1)D single-particle discrete-time action and a lattice Noether theorem
for **internal** symmetries, including a U(1) charge current. These pages
were re-read for this addendum. This is a relevant antecedent; it is not a
result about gravitational energy-momentum or the CJWW stress tensor.

### Repaired decision and verification scope

```
W11 = OPEN_AFTER_AUDIT
F1 = PASS / FOUR_ZERO_QUASIENERGY_SPECIES
F2 = INTEGRATED_CHARGES_AND_ZERO_TRANSFER_TETRAD_ONLY
F3_CONTRACT = OPEN
F3_SUBRESULT = ONE_PARTICLE_FULL_Z3_CONTINUOUS_LOGARITHM_EXCLUDED
F4 = GLOBAL_BOND_MOMENTUM_CONSERVED / LOCAL_STRESS_OPEN
REVIEW = SCOPED_RESULTS_ACCEPTED / SECOND_ROUND_CLARIFICATIONS_APPLIED
```

The new [certificate](../scripts/verify_w11_ir_stress_source.py) extracts
real-space hoppings from `walk2()`, constructs K and the original bond
operators, checks conservation by both Bloch algebra and real-space
convolution, tabulates eight frames/chiralities, and checks arbitrary-direction
Taylor coefficients with an independent exact-axis case. It does not
construct q≠0 stress kernels. D2 is repaired for these declared checks;
its full-stress part remains open. Node completeness and the identity
\(H_{\rm eff}=-(\arcsin|a|/|a|)a\cdot\sigma\) on the +I branch are
**analytic inputs**, not conclusions proved by the code. At |a|=0 the ratio
is defined by its limit. The script checks exact recentering and frame
derivatives at every node and prints the table; it does not compare each
printed row with an independent expected table (only the +I chirality
multiset is asserted). The analytic band bound and the
continuous-logarithm obstruction are the arguments above, not numerical
inferences from the certificate.
