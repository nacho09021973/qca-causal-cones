<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 574b5f3; lo que sigue a la cabecera es la respuesta sin editar)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.285 (Claude Code))
inicio: 2026-09-30T08:25:42Z  fin: 2026-09-30T08:33:08Z
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
entrada_opus.txt sha256 2d3fdc4b737957ee7dd70e4d5e7e75cfb9b863492d520a02308279db5a721a8a
respuesta sha256 fbebf38321a73f914ee3ceaf27380bc221213ab8fcb9e4f77749e30a20049501
-->

# Referee report: W9, W10, W11 (CJWW Weyl walk to linearized gravity bridge)

**Assumptions.**
- Document 10 correctly transcribes `walk2()`, and `walk2()` correctly transcribes CJWW Eq. (5.15). I cannot check the second part.
- The W5/W6 symbols quoted in W9 and W10 are taken as given. They are not reproduced in the documents.
- Bilinears ψ†…ψ are read as second-quantized free-fermion operators, with Γ(U) implementing the walk.
- Index conventions: x⁰ = t, and ∂_μT^{μν} = ∂_tT^{0ν} + ∂_iT^{iν} in any signature.
- Commit hashes and freeze order cannot be verified. All six documents carry the same date.

---

## 1. What is claimed

**W9 claims:**
- (B1) The spatial-only coupling ½λ∫h_{ij}T^{ij} is not invariant under time-dependent spatial linearized diffeomorphisms.
- (B2) The full ½λ∫h_{μν}T^{μν} is invariant, up to boundary terms, when ∂_μT^{μν} = 0.
- (B3) The W5/W6 lattice currents span the first-order spatial tetrad-conjugate structures σ_a p_i.
- (B4) The QCA has no microscopic lapse/shift variables and no microscopic T^{μν}.

**W9 does not claim:** a microscopic construction, a unique lattice T^{μν}, Einstein dynamics, G, nonlinear diffeomorphism invariance, or the equivalence principle beyond linear order.

**W10 claims:**
- (C1) Adding ½λ h T to a Gu–Wen-type linearized action yields scalar and vector constraints sourced by T^{00} and T^{0j}.
- (C2) These are consistent by the linearized Bianchi identity plus ∂T = 0.
- (C3) The spatial source is covered by W5/W6.
- (C4) Microscopic T̂^{00} and T̂^{0j} are open.

**W10 does not claim:** normalization to 8πG, nonlinear GR, the equivalence principle, or microscopic charges.

**W11 claims:**
- (F1) At p = 0 the exact walk has W = I + iσ^aE_{0a}{}^i p_i + O(p²), so H_eff = −σEp + O(p²).
- (F2) Finite-range bond bilinears have symbols that reproduce T^{00}, T^{0i} and, via W5/W6, T^{ij} in the narrow-band limit.
- (F3, F4) An exact local Floquet energy and an exact local momentum density are open.

**W11 does not claim:** an exact microscopic energy, the gravitational coupling, or the equivalence principle outside the Weyl sector.

---

## 2. Derivations

### W9 B1

These steps are correct:
- δS = λ∫T^{ij}∂_iξ_j
- after integration by parts, δS = −λ∫ξ_j∂_iT^{ij}
- ∂_iT^{ij} = −∂_tT^{0j}, so δS = λ∫ξ_j∂_tT^{0j}

A second integration by parts in t gives δS = −λ∫(∂_tξ_j)T^{0j}. So the variation vanishes exactly for ∂_tξ_j = 0.

The "FAIL" is therefore tautological. Setting h_{0μ} = 0 is a gauge choice (δh_{0j} = ∂_tξ_j), and its residual group is the time-independent ξ_j. In that gauge the truncation is consistent, provided the h_{0μ} equations (the constraints) are imposed separately as Gauss laws. B1 shows that the constraints are missing. It does not show that lapse/shift fields are needed. See B4.

### W9 B2

The derivation is correct, including the factor: symmetric T turns ½·2 into 1. It is the textbook Fierz–Pauli / Noether statement, with two caveats:
- The variation vanishes only on the matter equations of motion. Invariance of S_m + S_int at O(λ) needs an O(λ) transformation of ψ, which is not stated.
- Fermions couple to tetrads. Reducing to h_{μν}T^{μν} with symmetric T needs local Lorentz invariance to remove the antisymmetric tetrad part, which is not stated.

The W9 §2 action gives H = +σ·p. W11 gives H_eff = −σ^aE_{0a}{}^i p_i = σ·(Rp) with R = diag(−1, 1, −1) ∈ SO(3). These have the same chirality, so the two are consistent "up to frame".

### W9 B3

Given the quoted symbol, the span argument is correct: the 9 operators σ_a(d_r·p) span all σ_a p_i iff D is invertible. However:
- σ_a p_i is the canonical, frame-indexed tetrad-conjugate symbol. It is not symmetric T^{ij}.
- Only the zero-transfer (q = 0) symbol is addressed.

### W10 C1

The structure is correct: h_{00} and h_{0i} are non-dynamical in Fierz–Pauli, and their equations of motion are the Hamiltonian and momentum constraints.

The factors are not free conventions. With the Gu–Wen terms as quoted, a₀₀(∂²a_ii − ∂_i∂_ja_ij) + 2a_{0i}∂_jE^{ij}, the matter term gives:
- (λ/2)T^{00} for the scalar equation
- λT^{0i} for the vector equation, which becomes ∂_jE^{ij} ∝ (λ/2)T^{0i} after dividing by 2

Signs also depend on the signature (T^{0i} versus T_{0}{}^{i}). Writing both constraints as "= λT" with independently normalized C⁰ and C^j hides a relative coefficient that gauge invariance (B2) fixes. It must be derived, because C2 depends on it.

### W10 C2

The necessity argument is correct: Bianchi plus G_lin = λT implies ∂T = 0.

Sufficiency (constraint propagation) holds only for test matter on flat space at O(λ). Once geometry acts back on matter, which is the reciprocity the programme requires, matter obeys ∇_μT^{μν} = 0 on the perturbed metric. Then ∂_μT^{μν} = O(λhT), and the linearized sourced system is inconsistent at O(λ²) (the Deser / Gupta bootstrap problem).

C2 also assumes Einstein dynamics G_lin. According to W8 and W9, Gu–Wen's controlled L-type sector has ω ∝ k³, which is not linearized Einstein dynamics.

### W11 F1

I checked this by hand and it is correct:
- ∂₁W|₀ = iσ₁, ∂₂W|₀ = −iσ₂, ∂₃W|₀ = iσ₃.
- The sign of H_eff is consistent with W = e^{−iH_eff}.

**The mismatch order is wrong in the pessimistic direction.** Write W ∈ SU(2) as W = a₀ + i a·σ, with:
- a₀ = c₁c₂cos p₃ = 1 − |p|²/2 + O(p⁴)
- a = (s₁, −c₁s₂, c₁c₂s₃) = (p₁, −p₂, p₃) + O(p³)

Then W = e^{iA} + O(p³) with A = p₁σ₁ − p₂σ₂ + p₃σ₃, so H_eff = −A + O(|p|³). There is no O(p²) term.

**Counterexample to the "O(p²)" mismatch.** On the p₃ axis, W = e^{ip₃σ₃} exactly, so H_eff = −p₃σ₃ while H_IR = −sin p₃ σ₃. The mismatch is −(p₃³/6)σ₃ + O(p⁵).

The correct statement is: absolute mismatch Θ(Λ³), relative mismatch O(Λ²). The report's "O(Λ²)" is true but not sharp.

**Missing node analysis.** W(p) = ±I at all eight points p_i ∈ {0, π}:
- W = +I at (0,0,0), (π,π,0), (π,0,π), (0,π,π).
- W = −I at the other four (the π-nodes).

The linearized frames M, where W ≈ I + iMq, at the four quasienergy-0 nodes are:
- (0,0,0): diag(1, −1, 1)
- (π,π,0): diag(−1, −1, 1)
- (π,0,π): diag(−1, 1, 1)
- (0,π,π): diag(1, 1, 1)

Their det-signs are −, +, −, +, so the net chirality is zero. The low-quasienergy sector of the walk is therefore four Weyl species, not one. "The low-energy matter generator is the expected Weyl Hamiltonian" holds only after restricting to a neighborhood of p = 0.

### W11 F2, energy density

The algebra is correct:
- The bond term ε^{(i)} is Hermitian.
- Its total symbol is (i/2)M_i(e^{ip_i} − e^{−ip_i}) = −M_i sin p_i.
- It matches the definition ψ†(iM∇)ψ.

At transfer q (not computed in the report), the kernel is −M_i e^{−iq_i/2} sin(p_i + q_i/2). This is the midpoint-symmetrized density, which equals Belinfante T^{00} on shell at leading order. So T^{00} is acceptable at first order in (p, q).

Two defects:

- **Doublers.** H_IR vanishes at all eight corners. At the π-nodes it assigns energy 0 to walk states of quasienergy π. At (π,π,0) its frame is diag(−1, 1, 1) (det −1), while the walk's frame there has det +1: opposite chirality. H_IR is a surrogate only after a band projection, and that projection is non-local.
- **Not conserved.** [H_IR(p), W(p)] = 2i(b × a)·σ with b = −(s₁, −s₂, s₃). This is O(p⁴), not zero, so ΣH_IR drifts under the exact walk.

A better local candidate is K := i(U − U†)/2 = sin(H_F):
- It is finite-range and Hermitian.
- It commutes with U exactly.
- Its symbol is −(s₁σ₁ − c₁s₂σ₂ + c₁c₂s₃σ₃) = H_eff + O(p³).

### W11 F2, momentum density

The total symbol of π_i is sin p_i, which is correct. But π_i is the canonical density. The Weyl Belinfante density is

T^{0i} = P^i_can + ½(∇ × S)^i, with S = ψ†σψ/2.

At transfer q the curl term is O(q). In a narrow band, p and q are both O(Λ), so the curl term is the same order as the canonical term. π_i reproduces only:
- the integrated momentum, and
- the longitudinal part ∂_iT^{0i}.

It does not reproduce the transverse part, which sources gravitomagnetism and spin–rotation coupling. It is also not symmetric, and h_{0i} coupling needs T^{0i} = T^{i0}.

---

## 3. Verdicts against evidence

**W9**
- **B1:** Correct, but it is a statement about a gauge truncation (see §2).
- **B2:** Correct as a continuum first-order result. It is not CJWW-specific: the Weyl IR of CJWW is assumed in W9 §2 ("schematically") and established only later, in W11 F1, at a single node.
- **B3:** Rests on unverified W5/W6 symbols. It covers only the q = 0 canonical tetrad structures, and the report itself defers symmetrization.
- **B4:** The OPEN status is correct, but it contradicts W8 §3 and the Gu–Wen architecture imported in W10. There, a₀₀ and a₀ᵢ are Lagrange multipliers, and the microscopic requirement is local constraint operators with matter charges, enforced by penalty or projection, not lapse/shift registers.

**W10**
- **Terminal state and C5.** By the W10 contract, the weaker terminal state needs "controlled low-energy operators exist". W10 C4 has none; they appear only in W11. The terminal state was recorded before its own condition held.
- **C1:** Schematic. The relative scalar-to-vector normalization is left open, yet C2 depends on it.
- **C2:** Relies on G_lin dynamics, which the audit attributes only to the less-controlled N-type sector. It also silently assumes no backreaction.
- **C3:** Same limitations as B3.
- **C4:** Correct.

**W11**
- **F1:** Correct. It needs the three repairs noted in §2 (mismatch order, node count, band restriction).
- **F2:**
  - The energy part meets the contract's low bar, at q = 0 and for a narrow band.
  - "Local lattice representatives for all three source types" is not supported. T^{0i} is canonical, not Belinfante. T^{ij} comes from W5/W6, is tetrad-conjugate, and its symmetrization is marked "continuum-level identification", i.e. open.
  - The PASS thus rests on items the same report calls open.
- **F3:** OPEN understates the situation. See §6, item 5.
- **F4:** OPEN is factually "not constructed", but the reasoning is wrong. Σ_x π_i(x) has scalar symbol sin p_i·I, which commutes with W(p), so it is exactly conserved by Γ(U). Because U has finite range, the difference U†π(x)U − π(x) is local and has zero total, so an exact one-step local continuity equation with a local current exists. The real obstruction is canonical versus Belinfante, not conservation.

---

## 4. Certificates

### `verify_w9_continuum_gauge_bridge.py`
- **Check 1** is the polynomial identity spatial_div = conservation − ωT⁰. It is tautological.
- **Check 2** substitutes the conservation law and recovers −ωT⁰. It is tautological, and it divides by k_z, so k_z = 0 is excluded.
- **Check 3** substitutes the conservation law into itself and gets 0. It is circular.
- None of the checks involve h, ξ, the symmetry of T, the ½ → 1 factor, or integration by parts.
- **The det D = 1 check** confirms a hard-coded matrix is invertible. It does not link D to W6 and does not check the J^{(a,r)} symbol.

**Net:** it certifies nothing beyond linear algebra that is obvious by inspection. The report's label "symbolic certificate" overstates it.

### `verify_w11_ir_stress_source.py`
- **The F1 derivative check is genuine:** it differentiates the imported `walk2`. It does not assert W(0) = I, although that holds by inspection.
- **The H_IR check hard-codes the symbol** −σE sin p rather than building it from the bond operators, then checks d(sin)/dp|₀ = 1. It is circular with respect to the lattice construction.
- **The momentum check** asserts cos 0 = 1. It is vacuous.
- **Not checked at all:**
  - the mismatch order between H_eff and H_IR
  - kernels at q ≠ 0
  - conservation
  - the other nodes
  - symmetrization

**Net:** "exact IR stress-source certificate" should read "first-order zero-transfer symbol check at p = 0".

---

## 5. Prior art (all [UNVERIFIED])

**Plausible or consistent with memory:**
- Gu–Wen, *Emergence of helicity ±2 modes (gravitons) from qubit models*, arXiv:0907.1203. I also recall publication in Nucl. Phys. B around 2012, but I cannot confirm the volume or pages.
- Cubic dispersion in their better-controlled model is consistent with my memory.
- Linearized gravity written with a₀ᵢ and a₀₀ as Lagrange multipliers, with constraints imposed by energy penalties, is plausible.
- Pretko, *Generalized Electromagnetism of Subdimensional Particles: A Spin Liquid Story*, PRB 96, 035119 (2017), treats scalar and vector charge theories and their traceless versions.
- For the traceless vector-charge theory, 6 − 1 − 3 = 2 gapless modes, and cubic dispersion via a Cotton-type magnetic tensor, both match memory.

**Cannot confirm:**
- The "L-type / N-type" labels.
- The "spin-wave / quantum-freeze" characterization.
- The claim that Gu–Wen explicitly defer "gravity + nearly massless fermions" as future work.
- The exact form of the a₀₀ term.

**Doubtful:**
- W10 §0 credits Gu–Wen with "recovery of the linearized Einstein action" and then uses G_lin in C2. That appears true, if at all, only of the continuum starting point or the less-controlled linear-dispersion sector. Their controlled lattice sector (k³) is not linearized Einstein dynamics, per the project's own W8 summary.

**Missing prior art to audit:**
- C. Xu, rank-2 "soft graviton" lattice models (≈2006)
- Xu–Hořava, emergent Lifshitz gravity (≈2010)
- Rasmussen–You–Xu (≈2016)
- Quantum walks in curved spacetime: Arrighi–Facchini–Forets, Di Molfetta–Debbasch
- Arnault–Debbasch, *Quantum walks and gravitational waves* (≈2017), which is directly relevant to the W9/W10 "combined bridge" novelty question
- The Weinberg–Witten theorem, which any emergent graviton coupled to a conserved covariant T must evade

---

## 6. Missing steps

1. **External transcription check** of `walk2` against CJWW Eq. (5.15).
2. **Multi-node IR.** The IR theory has four quasienergy-0 Weyl nodes with net chirality zero, plus four π-nodes. Either couple gravity to all species, or prove that smooth geometry (|q| ≪ π) suppresses inter-node scattering to a stated order.
3. **Dynamical IR control.** Give a bound on the gap between the walk and Weyl evolution for narrow-band states. The error is O(tΛ³), not just a symbol match.
4. **Stress kernels at nonzero transfer q.** Derive T^{μν}(p, p+q) to first order in (p, q), matching the symmetric Belinfante tensor. This includes the spin-curl term in T^{0i} and the removal of the antisymmetric tetrad part in T^{ij}.
5. **Conservation and the F3 question.**
   - Use exactly conserved local densities: K = i(U − U†)/2 for energy, and sin P_i for momentum. Derive their local currents explicitly.
   - F3 as posed has a no-go for translation-invariant generators. Suppose H(p) is continuous with e^{−iH(p)} = W(p). Then tr H is constant in 2πℤ. At a Weyl node the eigenprojectors of W are direction-dependent, so H must be scalar there: H = 2πa·I at the 0-nodes and H = (2c+1)π·I at the π-nodes. That gives trace 4πa = 2π(2c+1), a parity contradiction. So no translation-invariant generator with summable hopping exists, and every branch of i log U has non-summable tails.
6. **Vacuum and normal ordering.** A Floquet unitary has no ground state. Define the reference state and the renormalized T^{00}, and address positivity.
7. **Geometry-dependent walk W[e, h₀₀, h₀ᵢ]** whose IR operator is the curved-space Weyl operator. The sources must be the variational derivatives of this same walk. The W11 surrogates are defined independently of any coupling, so reciprocity is not established.
8. **Derived constraint normalization.** Derive the relative scalar/vector normalization and signs, and the operator-level Ward identity k_μT^{μν}(q) = 0 to the stated order.
9. **Order of validity with backreaction.** Either restrict explicitly to O(λ) test matter, or include the gravitational self-stress, because consistency fails at O(λ²).
10. **Choice of graviton sector.** Specify the sector (the controlled k³ sector, or the linear-dispersion sector with weaker control) and redo C2 with its actual dynamics.
11. **Lattice constraint algebra with matter charges.** Show that the sourced local constraints close among themselves and commute with the Floquet step to the stated order, given that the charges are only approximately conserved.
12. **Exact CJWW recovery at λ = 0** in the coupled model.

---

## Summary table

| Gate | Sub-verdict | Assessment | Reason |
|---|---|---|---|
| W9 | B1 = FAIL | SUPPORTED | Correct; it shows the constraints are missing in the h₀μ = 0 truncation, and residual invariance holds for ∂_tξ = 0. |
| W9 | B2 = PASS | SUPPORTED_WEAKER | Textbook result; on shell, O(λ), needs an O(λ) matter transformation; not CJWW-specific. |
| W9 | B3 = COMPATIBLE/PARTIAL | SUPPORTED_WEAKER | Only q = 0 first-order canonical tetrad symbols, imported and unverified. |
| W9 | B4 = OPEN | SUPPORTED | True, but mis-framed: needs constraint operators, not lapse/shift registers. |
| W10 | C1 = PASS | SUPPORTED_WEAKER | Structure right; relative scalar/vector normalization and sign not derived. |
| W10 | C2 = PASS | SUPPORTED_WEAKER | Only O(λ) test matter with assumed Einstein dynamics; fails at O(λ²) with backreaction. |
| W10 | C3 = PASS/SPATIAL | SUPPORTED_WEAKER | Same as B3. |
| W10 | C4 = OPEN | SUPPORTED | No microscopic charges were available at W10 time. |
| W11 | F1 = PASS | SUPPORTED | Expansion verified; true mismatch is O(p³); one of four IR nodes. |
| W11 | F2 = PASS | SUPPORTED_WEAKER | T⁰⁰ OK narrow-band but not conserved and doubled; T⁰ⁱ canonical only; Tⁱʲ by reference. |
| W11 | F3 = OPEN | SUPPORTED | Understated: no translation-invariant continuous generator exists (parity no-go). |
| W11 | F4 = OPEN | SUPPORTED | Understated in the other direction: π_i is exactly conserved; the obstruction is Belinfante. |

## Overall verdicts

**W9: ACCEPT_WITH_REPAIRS.** Mandatory repairs:
- (a) Recast B1 as the missing constraints of the h₀μ = 0 gauge.
- (b) State B2 as a textbook on-shell O(λ) result, with the matter transformation and local-Lorentz step.
- (c) Restrict B3 to q = 0 canonical symbols.
- (d) Reframe B4 as needing local sourced constraint operators, not lapse/shift registers.
- (e) Relabel the certificate as a tautology check, and link D to W6.
- (f) Flag that the Weyl IR was assumed here.

**W10: ACCEPT_WITH_REPAIRS.** Mandatory repairs:
- (a) Derive the relative scalar/vector source coefficients and signs.
- (b) Restrict C2 explicitly to O(λ) without backreaction.
- (c) State which Gu–Wen sector supplies G_lin, and at what level of control.
- (d) Make the terminal state conditional on W11, per C5.
- (e) Apply the same C3 restriction as B3.

**W11: ACCEPT_WITH_REPAIRS.** Mandatory repairs:
- (a) Correct the mismatch order to Θ(Λ³) absolute.
- (b) Report the four 0-nodes and four π-nodes, and the doublers and chirality mismatch of H_IR.
- (c) Downgrade the T⁰ⁱ and Tⁱʲ claims to integrated charges and longitudinal parts, or supply q ≠ 0 Belinfante kernels.
- (d) Replace H_IR with the exactly conserved K = i(U − U†)/2, or bound its non-conservation.
- (e) Update F3 with the no-go, and F4 with the exact conservation of π_i.
- (f) Rewrite the certificate to build the symbols from the bond operators and to test q ≠ 0, conservation, and the H_eff − H_IR order.
