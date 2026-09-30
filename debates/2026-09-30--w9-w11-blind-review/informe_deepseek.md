<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 574b5f3; lo que sigue a la cabecera es la respuesta sin editar)
modelo: deepseek-v4-pro, esfuerzo: por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
inicio: 2026-09-30T08:25:42Z  fin: 2026-09-30T08:30:47Z
documento: /home/ignac/qca-causal-cones-review-w9w11/reports/2026-09-30--w8-prior-art-gauge-audit.md ; último commit: 44bc411 ; sha256 69d974b43922cf52d25e2ff9e4d8cf220458ade5d4d9ed288d66e654c0e449a5
documento: /home/ignac/qca-causal-cones-review-w9w11/theory/W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md ; último commit: 4a40c12 ; sha256 9d47b58eb1efcffbfebf07802eb207e78bbbe3c3191e36403bd930092441defb
documento: /home/ignac/qca-causal-cones-review-w9w11/reports/2026-09-30--w9-cjww-graviton-matter-bridge.md ; último commit: 8a8b2bf ; sha256 16b1d5fd5df4eec1f902e98697fde56c29fcd40764d02a81077870e995124819
documento: /home/ignac/qca-causal-cones-review-w9w11/scripts/verify_w9_continuum_gauge_bridge.py ; último commit: 5abd536 ; sha256 04597aff363f74dcb9a1569ec9509d1103fa1adccbf6d457582eb62b3fa670ee
documento: /home/ignac/qca-causal-cones-review-w9w11/theory/W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md ; último commit: 7109a3a ; sha256 eeca083f4248d211ab4f61e309640d868c2740a66c5abdee4657aff0039e0f50
documento: /home/ignac/qca-causal-cones-review-w9w11/reports/2026-09-30--w10-sourced-gu-wen-constraints.md ; último commit: f956f68 ; sha256 41c92a424b9d685d2ecfb72438d84ce4e33e4a43b96305c98a064cd4c74dd55a
documento: /home/ignac/qca-causal-cones-review-w9w11/theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md ; último commit: cfdc5c6 ; sha256 81f81078a4601f772a24017f5a829a40102404bc98e4d2ef92dbbbec4db2e9f0
documento: /home/ignac/qca-causal-cones-review-w9w11/reports/2026-09-30--w11-cjww-floquet-stress-tensor.md ; último commit: 83acdfd ; sha256 87e49c81b21b898d250c7a317279074e0fa6c6b24e547f0096e4b800e2dbddd6
documento: /home/ignac/qca-causal-cones-review-w9w11/scripts/verify_w11_ir_stress_source.py ; último commit: 97592a4 ; sha256 db1247dbc3f0afc817ea30e70e003260295e314e82696ec1827fa0cd2fc15516
documento: /home/ignac/qca-causal-cones-review-w9w11/debates/2026-09-30--w9-w11-blind-review/cjww_walk_definition.md ; último commit: sin versionar ; sha256 9ed70fe0ffd964d012a0f9a1013740942a126339ec598b7c1322d8522fc48417
entrada_deepseek.txt sha256 2d3fdc4b737957ee7dd70e4d5e7e75cfb9b863492d520a02308279db5a721a8a
respuesta sha256 914bfa84a4a52d1c7593fe4072503bc0d915e62f948aaec6ff152d9024fb2103
-->

Assumptions: I use the CJWW momentum-space walk exactly as given in Document 10, standard Pauli matrices, Fourier convention appropriate to the scripts, and assume boundary terms vanish in integrations by parts. Prior-art statements are from memory and marked `[UNVERIFIED]`.

---

## 1. What is claimed

**W9** claims:
- The spatial-only coupling \((λ/2)∫h_{ij}T^{ij}\) fails linearized gauge invariance because its variation is proportional to \(∂_t T^{0j}\).
- The full linearized coupling \((λ/2)∫h_{μν}T^{μν}\) is gauge invariant on-shell when \(∂_μT^{μν}=0\).
- W5/W6 spatial currents give a spatial tetrad-conjugate source, but not \(T^{00}\) or \(T^{0i}\).
- Microscopic lapse/shift/stress registers are absent; the result is a continuum bridge, not a microscopic one.

It explicitly does **not** claim microscopic lattice completion, nonlinear GR, a Newton constant, or universal equivalence-principle coupling.

**W10** claims:
- Gu-Wen-type vacuum linearized constraints can be imported.
- Adding \((λ/2)∫h_{μν}T^{μν}\) sources the scalar constraint by \(T^{00}\) and the vector constraint by \(T^{0j}\).
- Conservation of \(G_{\rm lin}^{μν}\) and \(T^{μν}\) makes the sourced continuum equations consistent.
- W5/W6 provide only the spatial source.
- Exact microscopic CJWW energy/momentum charge operators remain open.

It explicitly does **not** claim exact microscopic diffeomorphism symmetry, nonlinear GR, or fixed \(8πG\).

**W11** claims:
- The exact CJWW symbol has \(W_0(p)=I+iσ^aE_{0a}{}^ip_i+O(p^2)\).
- A local centered-difference IR Hamiltonian \(H_{\rm IR}\) reproduces the linear Weyl generator.
- A bond momentum-density surrogate \(\pi_i(x)\) has symbol \(\sin p_i\to p_i\).
- Exact Floquet energy and momentum local tensors remain open.

It explicitly does **not** claim an exact microscopic stress tensor.

---

## 2. Derivations

### W9 B1 — spatial-only coupling

The report’s derivation is correct. For

\[
S_{\rm int}^{\rm spatial}=\frac{\lambda}{2}\int h_{ij}T^{ij},
\qquad
δh_{ij}=∂_iξ_j+∂_jξ_i,
\]

with \(T^{ij}=T^{ji}\),

\[
δS_{\rm int}^{\rm spatial}
=
λ\int T^{ij}∂_iξ_j
=
-λ\int ξ_j∂_iT^{ij}.
\]

Using \(∂_μT^{μj}=0\),

\[
δS_{\rm int}^{\rm spatial}
=
λ\int ξ_j\,∂_tT^{0j},
\]

which does not vanish for general time-dependent \(ξ_j\). This is correct.

### W9 B2 — full linearized coupling

The derivation is also correct:

\[
δS_{\rm int}
=
λ\int T^{μν}∂_μξ_ν
=
-λ\int ξ_ν∂_μT^{μν}
\]

up to boundary terms. Thus on-shell \(∂_μT^{μν}=0\) gives \(δS_{\rm int}=0\). This assumes a symmetric conserved stress tensor, as the gate does.

### W9 B3 / W10 C3 — spatial source span

The low-momentum symbol

\[
J^{(a,r)}(p)=2(d_r·p)σ_a+O(|p|^3)
\]

or equivalently \(2\sin(p·d_r)σ_a\), indeed spans the spatial structures \(σ_a p_i\) if the direction matrix \(D=(d_r{}^i)\) is invertible. The script only checks invertibility of a triangular matrix; if that matrix is the actual W6 direction matrix, the span conclusion follows. This supports only the spatial source, not the full \(T^{ij}\).

### W10 C1–C2

No explicit derivation is given. The report states the standard variational result but does not write a concrete \(S_{\rm grav}^{(2)}\) or show the signs/factors of the sourced Gu-Wen constraints. The consistency argument in C2 is logically correct once the sourced equation is \(G_{\rm lin}^{μν}=λT^{μν}\), because \(∂_μG_{\rm lin}^{μν}=0\) forces \(∂_μT^{μν}=0\).

### W11 F1 — Weyl generator

Using the given \(W(p)\), I find

\[
\left.\frac{∂W}{∂p_1}\right|_{p=0}=iσ_1,\qquad
\left.\frac{∂W}{∂p_2}\right|_{p=0}=-iσ_2,\qquad
\left.\frac{∂W}{∂p_3}\right|_{p=0}=iσ_3.
\]

Thus with \(E_0=\operatorname{diag}(1,-1,1)\),

\[
W_0(p)=I+iσ^aE_{0a}{}^ip_i+O(p^2).
\]

A local log branch gives

\[
H_{\rm eff}(p)=-σ^aE_{0a}{}^ip_i+O(p^2).
\]

This is correct.

### W11 F2 — IR Hamiltonian and momentum symbols

The centered derivative has symbol

\[
\nabla_i \leftrightarrow i\sin p_i.
\]

Therefore

\[
H_{\rm IR}(p)
=
-σ^aE_{0a}{}^i\sin p_i.
\]

Expanding,

\[
H_{\rm IR}(p)
=
-σ^aE_{0a}{}^ip_i+O(p^3).
\]

The bond momentum surrogate

\[
\pi_i(x)
=
-\frac{i}{2}\left(\psi_x^\dagger ψ_{x+e_i}
-\psi_{x+e_i}^\dagger ψ_x\right)
\]

has symbol \(\sin p_i=p_i+O(p_i^3)\). These are correct first-order IR surrogates.

### Claimed mismatch order

The report says

\[
H_{\rm eff}(p)-H_{\rm IR}(p)=O(p^2).
\]

That is true, but weaker than what follows from the given walk. For \(A=σ^aE_{0a}{}^ip_i\),

\[
H_{\rm eff}(p)
=
-A-\frac{p^2}{6}A+O(p^4),
\]

while

\[
H_{\rm IR}(p)
=
-A+\frac16(σ_1p_1^3-σ_2p_2^3+σ_3p_3^3)+O(p^4).
\]

Thus

\[
H_{\rm eff}-H_{\rm IR}
=
-\frac{p^2}{6}A
-\frac16(σ_1p_1^3-σ_2p_2^3+σ_3p_3^3)
+O(p^4),
\]

which is \(O(p^3)\), not merely \(O(p^2)\). The report’s order is not wrong, but it is not sharp.

---

## 3. Verdicts versus evidence

### W9

- **B1 = FAIL**: **SUPPORTED**. The variation calculation is correct.
- **B2 = PASS**: **SUPPORTED**, conditional on a symmetric conserved continuum \(T^{μν}\). That assumption is explicit in the gate.
- **B3 = COMPATIBLE / PARTIAL**: **SUPPORTED**. Evidence supports spatial tetrad-source span only.
- **B4 = OPEN**: **SUPPORTED**. The report correctly records absence of microscopic lapse/shift/stress completion.

### W10

- **C1 = PASS**: **SUPPORTED_WEAKER**. The report only asserts the standard variational result schematically; it does not derive it from an explicit Gu-Wen/linearized-gravity action. The numerical convention is left open.
- **C2 = PASS**: **SUPPORTED**, as a conditional continuum identity. Once the field equation is \(G_{\rm lin}=λT\), conservation consistency is correct.
- **C3 = PASS / SPATIAL ONLY**: **SUPPORTED**. The spatial low-momentum symbol span is supported; it does not establish full \(T^{ij}\).
- **C4 = OPEN**: **SUPPORTED**. The report correctly distinguishes IR/continuum objects from exact microscopic charges.

### W11

- **F1 = PASS**: **SUPPORTED**. The exact first derivatives of \(W(p)\) match the claimed Weyl generator.
- **F2 = PASS**: **SUPPORTED_WEAKER**. The bilinears reproduce first-order symbols, but the report/certificate do not derive the full Weyl stress tensor or the Belinfante/frame symmetrization. “All three continuum source types” is true only at first-order IR level.
- **F3 = OPEN**: **SUPPORTED**. No exact local Floquet Hamiltonian/energy continuity is proved.
- **F4 = OPEN**: **SUPPORTED**. Global crystal momentum does not give a local one-step momentum tensor.

---

## 4. Certificates

### `verify_w9_continuum_gauge_bridge.py`

It checks:
- the algebraic identity

\[
kxT_1+kyT_2+kzT_3=(k_\mu T^\mu_{\text{col}})-ωT_0;
\]

- that substituting the conservation constraint into the spatial divergence yields \(-ωT_0\);
- that substituting the same conservation constraint into the full variation yields zero;
- that a hard-coded triangular matrix has determinant \(1\).

This is weaker than the report’s wording “certifies gauge consistency.” The full on-shell check is essentially a rewrite of the assumed conservation law, not a derivation that the Weyl stress tensor is conserved. The W6 span check only tests invertibility of a hard-coded matrix; it does not verify the actual W6 symbol or the claimed low-momentum current family from data.

### `verify_w11_ir_stress_source.py`

It checks:
- the first derivatives of the imported `walk2()` at \(p=0\), compared with \(iσ_1,-iσ_2,iσ_3\);
- the first derivatives of \(H_{\rm IR}=-\sum σ^aE_{0a}{}^i\sin p_i\), compared with the linear generator;
- that \(∂_p\sin p|_{0}=1\).

This is a genuine first-order check, but it does **not** check:
- the \(O(p^2)\) or \(O(p^3)\) mismatch between \(H_{\rm eff}\) and \(H_{\rm IR}\);
- the derivation of bond bilinears from the real-space definitions;
- Hermiticity, finite-range, or full low-energy operator convergence.

So it supports the first-order IR surrogate claim, not the stronger “IR stress-source certificate” label.

---

## 5. Prior art

All statements here are from memory and `[UNVERIFIED]`.

- **Gu–Wen, arXiv:0907.1203**: I can confirm from memory that such a paper exists and concerns emergent qubit/spin models with gravitational or helicity-\(±2\) structure. The specific L-type/N-type distinction, cubic versus linear dispersion, and the statement that the linear \(ω\sim k\) sector is less controlled are plausible but I cannot confirm exact details. `[UNVERIFIED]`
- **Pretko, PRB 96, 035119 (2017)**: I can confirm from memory that Pretko has a paper on rank-2 U(1) tensor gauge theories and subdimensional particles. The specific traceless vector-charge theory with \(∂_iE^{ij}=ρ^j\), \(E^i{}_i=0\), two gauge polarizations, and cubic dispersion is plausible. `[UNVERIFIED]`
- **Attribution that Gu–Wen explicitly leave combined gravity plus nearly massless fermions as future work**: plausible from memory, but I cannot confirm without the source. `[UNVERIFIED]`
- **Attribution that Gu–Wen discretize the constraints by energy penalties and recover the linearized Einstein action**: plausible, but exact wording and reliability need source verification. `[UNVERIFIED]`

No prior-art attribution here can be treated as established without consulting the original papers.

---

## 6. Missing steps

Before the chain

\[
\text{exact walk} \to \text{Weyl IR} \to \text{IR stress tensor} \to \text{sourced linearized constraints}
\]

could be called established at the stated level, the following are missing:

1. **Explicit continuum Weyl stress tensor**: derive a symmetric conserved \(T^{μν}\) for the chosen frame/sign convention, not assume it.
2. **Explicit linearized gravity variation**: write a concrete Gu-Wen-type or standard linearized \(S_{\rm grav}^{(2)}\), vary \(h_{00},h_{0i},h_{ij}\), and fix all signs and prefactors.
3. **Lattice energy/momentum charges**: construct or disprove existence of finite-range microscopic \(\hat T^{00}_x,\hat T^{0i}_x\) with controlled one-step continuity identities and correct IR limit.
4. **Belinfante/frame symmetrization**: show that the W5/W6 spatial currents and the W11 momentum/energy surrogates assemble into the correct symmetric continuum \(T^{ij},T^{0i},T^{00}\), not merely the same first-order symbols.
5. **Joint coupled model**: build and test a model containing both the Gu-Wen-type geometry sector and the CJWW matter sector with the W11 sources inserted.
6. **Backreaction and reciprocal coupling**: verify that geometry changes the matter principal symbol and matter sources geometry consistently at low energy.
7. **Stability/error bounds**: show the Weyl node, constraints, and source operators survive allowed perturbations and that finite-\(Λ\) errors are controlled.
8. **Coupling normalization**: derive or at least constrain \(λ\); the current gates deliberately avoid fixing \(8πG\).

---

## Final table

| Gate | Sub-verdict | Assessment | Reason |
|---|---|---|---|
| W9 | B1 = FAIL | SUPPORTED | Correct spatial variation; residual \(λ∫ξ_j∂_tT^{0j}\). |
| W9 | B2 = PASS | SUPPORTED | Full coupling vanishes on shell for assumed conserved symmetric \(T^{μν}\). |
| W9 | B3 = COMPATIBLE / PARTIAL | SUPPORTED | W5/W6 span \(σ_ap_i\) only; not full \(T^{ij}\). |
| W9 | B4 = OPEN | SUPPORTED | No microscopic lapse/shift/stress completion shown. |
| W10 | C1 = PASS | SUPPORTED_WEAKER | Only schematic; no explicit action variation or sign fixing. |
| W10 | C2 = PASS | SUPPORTED | Correct conditional consistency from Bianchi identity and conservation. |
| W10 | C3 = PASS / SPATIAL ONLY | SUPPORTED | Spatial symbol span supported; full stress tensor not established. |
| W10 | C4 = OPEN | SUPPORTED | Exact microscopic charges remain absent. |
| W11 | F1 = PASS | SUPPORTED | First derivatives of \(W(p)\) match Weyl generator. |
| W11 | F2 = PASS | SUPPORTED_WEAKER | First-order IR bilinears only; full \(T^{00},T^{0i},T^{ij}\) not derived. |
| W11 | F3 = OPEN | SUPPORTED | No exact local Floquet Hamiltonian/energy tensor. |
| W11 | F4 = OPEN | SUPPORTED | No exact local momentum density/current tensor. |

---

## Overall verdicts

- **W9**: **ACCEPT**. The derivations for B1/B2 are correct, and the terminal state is appropriately limited.
- **W10**: **ACCEPT_WITH_REPAIRS**.
  - Mandatory: derive the sourced constraints from an explicit linearized Gu-Wen-type action, including signs and prefactors.
  - Mandatory: replace the schematic C1 “PASS” with the explicit derivation before treating it as established.
- **W11**: **ACCEPT_WITH_REPAIRS**.
  - Mandatory: augment the certificate to verify real-space bond bilinear symbols and compute the \(H_{\rm eff}-H_{\rm IR}\) mismatch beyond first derivatives.
  - Mandatory: state clearly that the established objects are first-order IR surrogates, not full components of the Weyl stress tensor.
