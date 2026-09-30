# W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE](../theory/W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md), frozen at commit \`4a40c12c83801d5bdfdd7fc1c3638bb6308005e0\`.  
**Certificado simbólico:** [verify_w9_continuum_gauge_bridge.py](../scripts/verify_w9_continuum_gauge_bridge.py), added at commit \`5abd53673cef98c2ec0f0349db70f57fad869939\`.  
**Prior-art correction:** [w8-prior-art-gauge-audit.md](./2026-09-30--w8-prior-art-gauge-audit.md), commit \`44bc411ab72b121302c42cfe8a0afc5fd4613c01\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE =
CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS /
MICROSCOPIC_SPACETIME_COMPLETION_OPEN

B1 SPATIAL_ONLY = FAIL
B2 FULL_LINEARIZED_CONTINUUM = PASS
B3 W5/W6 SPATIAL_TETRAD_SOURCE = COMPATIBLE / PARTIAL
B4 MICROSCOPIC LAPSE_SHIFT_STRESS = OPEN
\`\`\`

W9 changes the target of the gravity programme. Prior art already supplies
microscopic/qubit helicity-2 sectors. The project-specific bridge is the
coupling of the explicit CJWW Weyl-limit matter sector to such geometry with
reciprocal sourcing.

## 1. Prior-art boundary

Gu and Wen (arXiv:0907.1203; Nucl. Phys. B 863 (2012) 90-129) construct local
qubit/spin models with emergent low-energy linearized diffeomorphism gauge
structure and helicity +/-2 modes. Their controlled L-type model has cubic
dispersion; their N-type model is argued, with weaker control, to admit a
linear dispersion.

Their paper explicitly treats combining gravity with nearly massless fermions
as a future objective, rather than establishing that combined matter-gravity
model.

Pretko's rank-2 tensor U(1) gauge theories also already contain vector Gauss
laws and known polarization counting. In particular, the traceless
vector-charge theory has two gauge polarizations but cubic dispersion.

Accordingly, no novelty is claimed for “qubits -> spin 2”, “rank-2 Gauss law”
or the W8 five-to-two kinematic counting.

## 2. B1 — spatial-only coupling fails gauge consistency

The current W6 geometry controls only the spatial metric/tetrad sector.

Consider

\[
S_{\rm int}^{\rm spatial}
=
\frac{\lambda}{2}
\int d^4x\,h_{ij}T^{ij}.
\]

For symmetric \(T^{ij}\), under

\[
\delta h_{ij}=\partial_i\xi_j+\partial_j\xi_i,
\]

\[
\delta S_{\rm int}^{\rm spatial}
=
\lambda\int d^4x\,T^{ij}\partial_i\xi_j.
\]

After integration by parts,

\[
\delta S_{\rm int}^{\rm spatial}
=
-\lambda\int d^4x\,\xi_j\partial_iT^{ij}
\]

up to a boundary term.

Relativistic stress conservation gives

\[
\partial_\mu T^{\mu j}=0,
\]

hence

\[
\partial_iT^{ij}
=
-\partial_tT^{0j}.
\]

Therefore

\[
\boxed{
\delta S_{\rm int}^{\rm spatial}
=
\lambda\int d^4x\,\xi_j\partial_tT^{0j}
}
\]

in general, and does not vanish for arbitrary time-dependent gauge
transformations.

Thus the spatial W6/W8 bridge is incomplete as a linearized
diffeomorphism-gauge coupling.

\[
\boxed{\texttt{B1 = FAIL}.}
\]

This is a structural result, not a failed parameter choice.

## 3. B2 — full linearized matter-gravity coupling works

Introduce the missing time-time and time-space metric components:

\[
h_{00},\qquad h_{0i}.
\]

Use the full linearized coupling

\[
S_{\rm int}
=
\frac{\lambda}{2}
\int d^4x\,
h_{\mu\nu}T^{\mu\nu}.
\]

Under

\[
\delta h_{\mu\nu}
=
\partial_\mu\xi_\nu+\partial_\nu\xi_\mu,
\]

symmetry of \(T^{\mu\nu}\) gives

\[
\delta S_{\rm int}
=
\lambda\int d^4x\,
T^{\mu\nu}\partial_\mu\xi_\nu.
\]

Integrating by parts,

\[
\delta S_{\rm int}
=
-\lambda\int d^4x\,
\xi_\nu\partial_\mu T^{\mu\nu}
\]

up to a boundary term.

For the continuum Weyl field, on its equations of motion,

\[
\partial_\mu T^{\mu\nu}=0.
\]

Hence

\[
\boxed{\delta S_{\rm int}=0}
\]

to the declared linearized/on-shell order.

\[
\boxed{\texttt{B2 = PASS}.}
\]

This establishes continuum compatibility, not a microscopic lattice
construction.

## 4. B3 — relation to W5/W6 spatial source

The W5/W6 edge-current family has low-momentum symbol

\[
J^{(a,r)}(p)
=
2(d_r\cdot p)\sigma_a+O(|p|^3).
\]

Since the W6 direction matrix is invertible, linear combinations of these
operators span all spatial structures

\[
\sigma_a p_i.
\]

Those are precisely the structures obtained by varying the Weyl Hamiltonian
with respect to spatial tetrad coefficients.

Therefore W5/W6 already provide a lattice representative of the **spatial
tetrad-conjugate source**.

However, the symmetric metric stress tensor requires the appropriate
symmetrization/frame treatment, and the current construction does not supply
the temporal source components

\[
T^{00},\qquad T^{0i}.
\]

Thus:

\[
\boxed{
\texttt{B3 = SPATIAL SOURCE COMPATIBLE / PARTIAL}.
}
\]

## 5. B4 — microscopic spacetime completion is absent

The frozen CJWW/W6-W8 construction has:

- a preferred discrete update time;
- nine spatial tetrad controls;
- spatial current/tetrad source operators;
- geometry-only spatial stiffness.

It does **not** yet have microscopic variables or constraint registers
corresponding to:

\[
h_{00},\qquad h_{0i}.
\]

It also lacks a complete discrete local conserved object already proved to
flow to the full symmetric Weyl

\[
T^{\mu\nu}.
\]

In particular, a Floquet unitary has quasienergy but does not automatically
supply the local time-translation Noether structure needed to identify an
exact microscopic \(T^{00}\).

Therefore the continuum gauge completion cannot yet be lifted back to the
microscopic QCA.

\[
\boxed{\texttt{B4 = OPEN}.}
\]

## 6. Scientific interpretation

The current programme has now separated two problems that had been conflated:

### Gravity-sector problem

How to obtain a stable two-polarization helicity-2 low-energy sector.

This has substantial prior art, including Gu-Wen and rank-2 tensor gauge
models. The project need not rediscover it.

### Matter-gravity bridge problem

How to couple the explicit CJWW Weyl matter sector to that geometry so that:

\[
\text{geometry}\to\text{Weyl principal symbol}
\]

and

\[
\text{Weyl stress}\to\text{geometry}
\]

are the same variational coupling and respect the low-energy gauge
constraints.

W9 shows that the spatial part of that bridge is already compatible with the
W5/W6 construction, but full gauge consistency forces temporal completion.

## 7. Minimal successor

The next successor should not add more spatial tensor fields.

It should construct the missing ADM-like linearized variables:

\[
\text{lapse-like }n\sim h_{00},
\qquad
\text{shift-like }n_i\sim h_{0i},
\]

and determine whether they can appear as microscopic constraint variables
rather than extra propagating modes.

The target low-energy coupling is then

\[
\frac{\lambda}{2}
\left(
h_{00}T^{00}
+2h_{0i}T^{0i}
+h_{ij}T^{ij}
\right).
\]

Only after a discrete/low-energy conservation law is derived should the
project attempt a full Gauss/diffeomorphism constraint algebra.

## 8. Terminal decision

\[
\boxed{
\texttt{CONTINUUM\_GRAVITON\_MATTER\_BRIDGE\_PASS /
MICROSCOPIC\_SPACETIME\_COMPLETION\_OPEN}
}
\]

is the terminal state.

No nonlinear Einstein, equivalence-principle, \(G_{\rm eff}\), AdS or
absolute-scale claim follows.

## 9. Repair addendum — 2026-09-30

This addendum responds to A3, B5–B6, C1–C2 and D1 of the
[blind-review repair list](../debates/2026-09-30--w9-w11-blind-review/reparaciones.md),
imported through `7903713`. The frozen report above is retained.
Evidence: **PRELIMINARY / REPAIRED_VERSION_NOT_INDEPENDENTLY_REVIEWED**.

**B1 / C1.** The computed variation is an obstruction to invariance under
arbitrary time-dependent spatial gauge transformations of the truncated
coupling. On the free conserved-stress shell and with vanishing boundary
terms, it is also
\(-\lambda\int(\partial_t\xi_j)T^{0j}\), which vanishes for static spatial
parameters. It does not disprove a gauge-fixed formulation with residual
gauge freedom. The missing requirements are the temporal constraint equations
and their matter sources. The revised label is
`SPATIAL_TRUNCATION_NOT_FULL_GAUGE_INVARIANT / STATIC_RESIDUAL_COMPATIBLE`.

**B2 / B5–B6.** This is the continuum algebraic identity
\(\delta S_{\rm int}=-\lambda\int\xi_\nu\partial_\mu T^{\mu\nu}\), for an
already symmetric conserved stress, on the free matter shell, at O(λ).
It is not CJWW-specific and does not derive the transformation of ψ,
an off-shell matter symmetry, or a local-Lorentz Ward identity. Passing
from a tetrad source to a symmetric metric stress is an additional input;
W6's antisymmetric frame directions alone do not establish local Lorentz
gauge redundancy. No complete off-shell Einstein–Weyl action is claimed.
The revised label is `ON_SHELL_CONTINUUM_IDENTITY / O(lambda)`.

CJWW's use of this identity depends on the repaired W11 F1, including its
four-species contract. The original p=0 expansion describes only one of
those species. The continuum target sums the four stresses; their full
microscopic nonzero-transfer kernels have not been matched.

**B3 / A3.** Keep only `ZERO_TRANSFER_SPATIAL_TETRAD_SOURCE / PARTIAL`.
The current symbols span tetrad-conjugate structures at p=0; they do not
establish the local symmetric Belinfante tensor at q≠0. In particular,
no spin-improvement formula from a review is adopted without derivation.

**B4 / C2.** The missing microscopic objects are local **constraint
operators containing matter charges**, with a controlled penalty/projection
and low-energy Ward identity. Lapse and shift may be Lagrange multipliers;
separate microscopic registers for them are not a requirement. This
supersedes the wording of §§5,7. B4 remains OPEN.

**D1.** The updated [checker](../scripts/verify_w9_continuum_gauge_bridge.py)
constructs the symmetric h,T coupling and its variation with ξ explicitly,
checks the 1/2 factor and Fourier integration by parts, and checks the static
residual case without division by any momentum component. Its output is
labelled an algebraic consistency check. It takes stress conservation as an
input and makes no W6 rank claim; the original W6 certificate remains the
source for that separate rank calculation.

The terminal label `CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS /
MICROSCOPIC_SPACETIME_COMPLETION_OPEN` is retained **only for this conditional
on-shell continuum statement**, not for a constructed CJWW local stress
or reciprocal coupling. W10/W11's repaired OPEN states govern readiness
for any joint successor.
