<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ b817ac0; lo que sigue a la cabecera es la respuesta sin editar)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.285 (Claude Code))
inicio: 2026-09-30T10:14:43Z  fin: 2026-09-30T10:20:55Z
documento: /home/ignac/qca-causal-cones/theory/W9_CJWW_GRAVITON_MATTER_BRIDGE_GATE.md ; último commit: 4a40c12 ; sha256 9d47b58eb1efcffbfebf07802eb207e78bbbe3c3191e36403bd930092441defb
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w9-cjww-graviton-matter-bridge.md ; último commit: 86fe771 ; sha256 990717104b029683fa4585c31e3c21bb920155706328bbb6d49f13914e026ec4
documento: /home/ignac/qca-causal-cones/scripts/verify_w9_continuum_gauge_bridge.py ; último commit: 86fe771 ; sha256 4291df6f93c1b5b78675c8ac79723e2478c913157b0598de6d7e6b4104b31798
documento: /home/ignac/qca-causal-cones/theory/W10_SOURCED_GU_WEN_CONSTRAINT_BRIDGE_GATE.md ; último commit: 7109a3a ; sha256 eeca083f4248d211ab4f61e309640d868c2740a66c5abdee4657aff0039e0f50
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w10-sourced-gu-wen-constraints.md ; último commit: 86fe771 ; sha256 9bb8c92026a5165a5a9d48962ff45c8510454393c21bcf10893fa023a20c5cf7
documento: /home/ignac/qca-causal-cones/scripts/verify_w10_linearized_constraints.py ; último commit: 86fe771 ; sha256 ae12afd75048c307ba819e9c005f2a93ff19c5c470223315597289d28f54dc28
documento: /home/ignac/qca-causal-cones/theory/W11_CJWW_FLOQUET_STRESS_TENSOR_GATE.md ; último commit: cfdc5c6 ; sha256 81f81078a4601f772a24017f5a829a40102404bc98e4d2ef92dbbbec4db2e9f0
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w11-cjww-floquet-stress-tensor.md ; último commit: 86fe771 ; sha256 dc63553d1467c149fdb48c3559561df4544eb5cb963c8d2ad06707c8f8372982
documento: /home/ignac/qca-causal-cones/scripts/verify_w11_ir_stress_source.py ; último commit: 86fe771 ; sha256 cf52ab1c9119f2dbfb2076b562fbfaabaf348c02ce1476d57d9eb1c09a451a24
documento: /home/ignac/qca-causal-cones/debates/2026-09-30--w9-w11-repair-review/cjww_walk_definition.md ; último commit: sin versionar ; sha256 9ed70fe0ffd964d012a0f9a1013740942a126339ec598b7c1322d8522fc48417
entrada_opus.txt sha256 af7094b69bedb8e56200418628cb4981171cd65d065634c3fead1036714740e4
respuesta sha256 01f64f2e6df3fa8c17baf7142928deaf2403efe978aec155e8e1d7c2b6d97e3c
-->

# Referee report: W9, W10, W11 repair addenda

**Assumptions.** I take the transcribed `walk2()` symbol (Doc 10) as the CJWW (5.15) walk. I assume the unprovided helpers `laurent`, `Z` and `PAULI` do what their names suggest. W5/W6 claims (invertible direction matrix, J^{(a,r)} symbols) are taken as given. I did not verify the Gu–Wen and Arnault–Cedzich page citations.

I re-derived everything below by hand. I also ran the two self-contained certificates' logic and an independent numerical check of the W11 table and bounds: random sampling on the four +I balls at Λ ∈ {0.5, 0.2, 0.05}, with n ∈ {1, 7, 40}.

---

## 1. What is now claimed

**W9**
- **Current verdict:** `CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS / MICROSCOPIC_SPACETIME_COMPLETION_OPEN`, retained only for the identity δS_int = −λ∫ξ_ν∂_μT^{μν}. This holds for an assumed symmetric, conserved T, on the free shell, at O(λ).
- **Sub-verdicts:** B1 = `SPATIAL_TRUNCATION_NOT_FULL_GAUGE_INVARIANT / STATIC_RESIDUAL_COMPATIBLE`; B3 = `ZERO_TRANSFER…/PARTIAL`; B4 = OPEN.
- **Not claimed:**
  - a CJWW-specific identity, or a CJWW local stress;
  - reciprocal coupling;
  - the matter transformation law, off-shell symmetry, or local-Lorentz Ward identity;
  - the tetrad → symmetric-stress step;
  - a q≠0 Belinfante tensor;
  - four-species kernel matching;
  - an off-shell Einstein–Weyl action.

**W10**
- **Current verdict:** `OPEN_AFTER_AUDIT`. C1 PASS (explicit convention). C2 PASS for a flat test source at O(λ) only. C3 zero-transfer/partial. C4 OPEN. C5 NOT_MET.
- **Not claimed:**
  - any mapping to Gu–Wen canonical variables or J, g;
  - sourced L-model dynamics or a lattice realization;
  - O(λ²) or backreaction consistency;
  - a Newton constant;
  - novelty;
  - readiness of a joint gate.

**W11**
- **Current verdict:** `OPEN_AFTER_AUDIT`. F1 PASS with four zero-quasienergy species. F2 covers integrated charges and zero-transfer tetrad only. F3 is an author proof that no continuous translation-invariant logarithm exists. F4 has a globally conserved bond momentum; local stress is OPEN.
- **Not claimed about K:** that it is the quasienergy, a positive energy, the generator of U, or conserved after coupling.
- **Not claimed about the stress:**
  - q≠0 kernels, spin improvement, or the Belinfante tensor;
  - a local one-step current;
  - a common envelope momentum across species;
  - π-sector exclusion under coupling;
  - any interacting-QCA statement;
  - a no-go for all QCAs.

## 2. W11 node table

- **Decomposition.** W = a₀I + i a·σ with a₀ = c₁c₂c₃ and a = (s₁, −c₁s₂, c₁c₂s₃). This is verified entrywise, and |a|² + a₀² = 1.
- **Completeness.** Since det W = 1, W is degenerate iff a = 0, iff |a₀| = 1. That forces |c_i| = 1 for all i, i.e. p_i ∈ {0, π}. At those points s_i = 0, so W = s_*I with s_* = (−1)^{b₁+b₂+b₃}. The eight nodes are exactly W = ±I. ✔
- **Frames.** Write σ_i = (−1)^{b_i}. Then s_*W(p_*+k) = a₀(k)I + i(σ₂σ₃a₁, σ₃a₂, a₃)(k)·σ, which gives **E_* = diag(σ₂σ₃, −σ₃, 1)**.
  - All eight rows of diag E_*, det E_* and sgn det(−E_*) match the table. I checked by hand and numerically.
  - The +I chiralities are (+,−,+,−), with net zero. The −I nodes also net to zero.
  - The Pauli part is odd in k, so it has no quadratic term. ✔
  - The review's (−,+,−,+) is det E_* in the same node order. ✔
- **Unstated but relevant:** every E_* is diagonal ±1, so E_*E_*ᵀ = I. All species therefore see the same flat metric, which is consistent with "one common geometry" at λ = 0.

## 3. W11 energy charge K

- **Hermiticity and commutation.** K = i(U−U†)/2 is Hermitian, and [K,U] = 0 because U is normal. K(p) = i(W−W†)/2 = −a·σ. ✔
- **Hopping matrices.**
  - With the convention (Uψ)_x = Σ_r A_rψ_{x+r}, U† has hoppings A_{−r}†. Hence B_r = i(A_r − A_{−r}†)/2 and B_{−r} = B_r†. ✔
  - Explicitly, from K = −s₁σ₁ + c₁s₂σ₂ − c₁c₂s₃σ₃:
    - B_{±e₁} = ±(i/2)σ₁;
    - B_{(ε₁,ε₂,0)} = −(iε₂/4)σ₂;
    - B_{(ε₁,ε₂,ε₃)} = (iε₃/8)σ₃.
  - That is 14 displacements with range ≤ 1 per coordinate, including body diagonals. ✔
- **Local density.** ε_x^K is Hermitian, and Σ_x ε_x^K = ⟨ψ,Kψ⟩. The second term reindexes to ⟨ψ,Kψ⟩ using B_{−s}† = B_s. ✔
- **dΓ remark.** Correct: Γ(U)dΓ(K)Γ(U)† = dΓ(K).
- **Band bound.**
  - At +I nodes a₀(p_*+k) = Πcos k_i. For Λ ≤ 1/2 this is positive, so θ ∈ [0, π/2).
  - sin²θ = 1 − Π(1 − sin²k_i) ≤ Σsin²k_i ≤ |k|², by the union bound. Hence θ ≤ arcsin Λ. ✔
  - On this branch H_eff = −θ n·σ, so sin H_eff = −sinθ n·σ = −a·σ = K. ✔
  - The difference in each band is θ − sinθ ≤ θ³/6. The bound is valid, with tight form arcsinΛ − Λ. The numerical sup of the ratio is 0.96–0.99.
- **Dynamical bound.** U = e^{−iH_eff} commutes with K on each fibre, so |e^{−inθ} − e^{−in sinθ}| ≤ |n|(θ − sinθ). P_Λ is a momentum projector and is U-invariant. ✔ Numerical ratio ≤ 0.99.
- **‖K − H_IR‖ ≤ Λ³.**
  - K − H_IR = −(0, (1−c₁)s₂, (c₁c₂−1)s₃)·σ.
  - Using 1−c₁ ≤ p₁²/2 and 1−c₁c₂ ≤ (p₁²+p₂²)/2, the norm is ≤ |p|³/2. The claim is true but loose by at least a factor of 2; numerically the sup of the ratio is ≈ 0.18.
  - The derived H_IR dynamical bound is valid on the p=0 ball only.
- **Axis check.** Both K and H_IR equal −sin p₃σ₃, versus H_eff = −p₃σ₃, giving coefficient 1/6. ✔
- **Unstated fact.** At the −I nodes, K = +σ·E_*k + O(k³) = −H_*(k). K assigns π-species the opposite energy sign, and it is two-to-one in θ ↔ π−θ. This strengthens the stated need to exclude the π sector.

**No errors found.** The only constant that could be improved is Λ³ → Λ³/2.

## 4. W11 F3 obstruction

The steps:
1. tr H ∈ 2πℤ and is constant, since det W = 1, H is continuous, and the torus is connected. ✔
2. [H,W] = 0. ✔
3. Along k = tn: [H(p_*+tn), s_*(itσ·E_*n + O(t²))] = 0. Divide by t and use boundedness and continuity of H to get [H(p_*), σ·E_*n] = 0 for all n. With E_* invertible, H(p_*) = c_*I. ✔
4. At +I nodes c_* ∈ 2πℤ, so tr ∈ 4πℤ. At −I nodes c_* ∈ π + 2πℤ, so tr ∈ 2π(2ℤ+1). Contradiction. ✔

Step 3 is essential. Without scalarity, a −I node allows eigenvalues such as (π, 3π), whose trace 4π is compatible with a +I node.

**Scope is correct but incomplete. Mandatory clarifications:**
- The statement is **one-particle (quadratic)**. It does not exclude an interacting many-body local H with Γ(U) = e^{−iH}.
- "Translation-invariant" must mean the full ℤ³ with the given 2-component cell. Supercell-invariant generators fold π-nodes to 0 and are not covered. This is formally covered by "translation-breaking", but should be said explicitly.
- Discontinuous translation-invariant logarithms exist (e.g. the principal branch). The no-go is specifically about continuous symbols.

Hence the contract's F3 question (any strictly local H_loc) is not closed. The label is accurate but must carry "one-particle".

## 5. W10

**Linearized Einstein tensor.** G_lin matches R⁽¹⁾_{μν} − ½ηR⁽¹⁾.

**Action and normalization.**
- S_g = −½∫hG has the same sign as (1/2κ)∫√−g R at κ = ½ with g = η + h.
- The TT Lagrangian I computed is −½h₁₂(∂_t² − ∂₃²)h₁₂, i.e. +½ḣ₁₂² − ½(∂₃h₁₂)². The kinetic sign is healthy.
- The Newtonian check h₀₀ = h_ii = −2Φ gives 2G⁰⁰ = 4ΔΦ, which is attractive for λ > 0.

**Field equations.**
- G^{μν} = λT^{μν}/2 is correct.
- Lapse: −G⁰⁰ + λT⁰⁰/2. Shift, with weight 2: −2G^{0i} + λT^{0i}. ✔
- I derived C⁰ = 2G⁰⁰ and C^i = 2G^{0i} = −2G_{0i} independently; they match the stated formulas. ✔

**Wording defect.** h₀₀ enters the Lagrangian linearly, but **h₀ᵢ enters quadratically** (checked: degree 2 in h₀₁), and C^i contains h₀ᵢ. The shift is a Lagrange multiplier only in Hamiltonian form, i.e. after the Legendre transform to ∂_jπ^{ij}. The original C1 text and W9's "lapse and shift may be Lagrange multipliers" need that qualifier.

**Verdict consistency.** OPEN_AFTER_AUDIT is consistent with the evidence.
- C5 needs controlled local source operators for the intended bridge.
- W11 supplies only an integrated energy charge, and marks four-species matching, q≠0 kernels and continuity currents as open.
- The A4 argument (a PASS recorded before W11's contract existed) is correct. The downgrade is not understated.

**Scope note on C2.** C2 applies to any conserved symmetric T_(0). For CJWW it must be the four-species total, which is not constructed. The label says "test source", which is acceptable.

## 6. W9

**Algebra.**
- δS = (λ/2)·2i·Σk_iξ_jT_{ij} = iλξ·(Tk). The factor ½ cancels by symmetry of T. ✔
- The spatial/temporal split is correct.
- The on-shell form −λ∫(∂_tξ_j)T^{0j} is correct, given vanishing temporal boundary terms. For static ξ, those boundary terms are ∫d³x ξ_j[T^{0j}]_{t_i}^{t_f}, which is nonzero for on-shell fields. The statement is therefore "invariant up to a temporal boundary term", which is acceptable but should be said.

**Understatement.**
- The truncated coupling equals the full coupling in the gauge h₀μ = 0.
- Its residual group is {ξ₀(x), ξ_i = f_i(x) − t∂_iξ₀}.
- For ξ_i = −t∂_iξ₀, the variation is λ∫∂_jξ₀T^{0j} = λ∫ξ₀∂_tT⁰⁰, which is again a boundary term.
- So the entire synchronous residual group is compatible, not only static ξ_j. "STATIC_RESIDUAL_COMPATIBLE" undersells this. The report correctly says the missing content is the temporal constraints.

**Scope of the PASS.** The retained PASS is stated at the right scope *in prose*: a conditional on-shell continuum identity, not CJWW-specific. The **label** is not, because "CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS" reads as the contract's question.
- Contract condition 3 (reciprocity) is explicitly disclaimed.
- The CJWW application depends on W11 four-species source matching, which W11 marks open.

## 7. Certificates

**W9 script**
- **Assert 1** (variation = iλξ·Tk): genuine, but trivial.
- **Assert 2** ("Fourier integration by parts"): **tautological.** after_ibp = −λξ·(−iTk) is the same expression as assert 1; I verified this symbolically. The IBP content lives only in the comment's sign convention.
- **Assert 3** (spatial = split): genuine. It is an index split that uses no conservation.
- **Assert 4** (`residual.subs(k0,0)==0`): **vacuous.** The residual is defined by hand as ∝ k₀. The on-shell step (spatial − residual = iλΣξ_j(Tk)_j) is never asserted.
- The report's "checks … Fourier integration by parts … static residual case" overstates what the script does. It is an algebraic restatement, which the output label half-admits.

**W10 script**
- Checks the Bianchi identity and gauge invariance of G_lin for arbitrary formal momenta.
- Checks all ten variations with weights 1 and 2.
- Checks the C⁰ and C^i formulas and the TT wave operator.
- The use of commuting symbols for the self-adjointness check is valid, since the operator has even order.
- This matches the report.
- Not checked: kinetic-energy sign and conservation of T. The latter is correctly declared as an input.

**W11 script**
- Checks:
  - unitarity and det = 1;
  - the SU(2) decomposition;
  - the K symbol, hermiticity and [K,W] = 0;
  - real-space U†U = I and U†KU = K;
  - 14 hoppings and range 1;
  - exact recentering identities and first derivatives at all eight nodes;
  - multiset of +I chiralities;
  - conservation of π_i;
  - the H_IR symbol;
  - jets;
  - the axis case.
- E_* is defined by formula but then verified against ∂W. **Not circular.** Matches the report.
- **Weaker than it may appear:**
  - Node completeness is only a comment (the analytic argument is trivial).
  - The H_eff series is input as −(arcsin|a|/|a|)a, not derived from W. The report's "K − H_eff = O(p³)" rests on that identity.
  - The table is printed, not asserted row-by-row; only the multiset is asserted. It does match, per §2.
  - The quartic-commutator check uses one direction v = (1,2,3), which is sufficient for "nonzero".
  - The ε_x^K sum rule, the band bounds, the ‖K − H_IR‖ bound and F3 are not checked. The report says these are analytic.
  - The script depends on an unprovided module.

## 8. Consistency of the downgrades

**Overclaims**
- **W9 terminal label.** It retains PASS wording although reciprocity is disclaimed and CJWW use depends on W11-open items. The substance is correctly scoped; the label is not.
- **W9 D1 certificate description.** It overstates two asserts that are tautological or vacuous (§7).
- **Frozen verdict blocks.** In all three reports the top-of-file blocks still show the superseded PASS states with no banner. A reader of the header gets the wrong state.
- **Shift as multiplier.** Called a Lagrange multiplier without the Hamiltonian-form qualifier.

**Understatements (not errors)**
- W9's residual gauge is larger than "static".
- ‖K − H_IR‖ ≤ Λ³/2.
- The common metric E_*E_*ᵀ = I is not noted.

**Dependence check.** No remaining sub-PASS depends on anything its own report marks open. W10 C1/C2 and W11 F1 are self-contained continuum or symbol statements. W9's terminal PASS depends on nothing open *only because* it is decoupled from CJWW, which is why the label must say so.

---

## Summary table

| Gate | Claim | Status | Reason |
|---|---|---|---|
| W9 | B1: spatial truncation not fully gauge invariant | SUPPORTED | Residual λ∫ξ_j∂_tT^{0j} ≠ 0 for general ξ(t) |
| W9 | B1: static residual compatible | SUPPORTED_WEAKER than truth | Full synchronous residual group compatible, up to temporal boundary terms |
| W9 | B2: on-shell O(λ) continuum identity | SUPPORTED | Standard; T symmetric and conserved is an input |
| W9 | Terminal `CONTINUUM_…_BRIDGE_PASS` | SUPPORTED_WEAKER | Only a generic conditional identity; reciprocity and CJWW matching open |
| W9 | Certificate checks IBP and static residual | NOT_SUPPORTED | Those asserts are tautological or vacuous |
| W10 | Quadratic action, signature, normalization | SUPPORTED | Verified; healthy TT sign; Newtonian limit attractive |
| W10 | G^{μν} = λT^{μν}/2, lapse/shift factors | SUPPORTED | Weights 1/2 and C⁰, C^i formulas re-derived |
| W10 | C2 test-source consistency at O(λ) | SUPPORTED | Bianchi identity plus conserved T_(0) (input) |
| W10 | Shift as Lagrange multiplier | SUPPORTED_WEAKER | Quadratic in the Lagrangian; multiplier only in Hamiltonian form |
| W10 | OPEN_AFTER_AUDIT | SUPPORTED | C5 not met by an integrated charge |
| W11 | Eight nodes = {W = ±I} | SUPPORTED | \|a₀\| = 1 forces p_i ∈ {0, π} |
| W11 | Frame/chirality table | SUPPORTED | E_* = diag(σ₂σ₃, −σ₃, 1); all rows match |
| W11 | K Hermitian, [K,U] = 0, hoppings, density | SUPPORTED | Verified; 14 hoppings, range 1 |
| W11 | Band bound (arcsinΛ)³/6, sin²θ ≤ \|k\|², K = sin H_eff | SUPPORTED | Valid; tight form arcsinΛ − Λ |
| W11 | Dynamical bound \|n\|(arcsinΛ)³/6 | SUPPORTED | Commuting fibrewise; numerical ratio ≤ 0.99 |
| W11 | ‖K − H_IR‖ ≤ Λ³ | SUPPORTED (loose) | Actually ≤ Λ³/2 (numerically ≈ 0.18Λ³) |
| W11 | F3 no continuous logarithm | SUPPORTED | All steps valid; scalarity at nodes essential |
| W11 | F3 scope | SUPPORTED_WEAKER | Must state: one-particle, full-ℤ³ with 2-site cell; many-body/supercell not excluded |
| W11 | Certificate scope as described | SUPPORTED | Matches; H_eff series and node completeness are inputs |

## Final verdicts

**W9: ACCEPT_WITH_REPAIRS**
1. Relabel the terminal state so the qualifier is part of the label (e.g. `CONDITIONAL_ON_SHELL_CONTINUUM_IDENTITY / CJWW_BRIDGE_OPEN`), or use `OPEN_AFTER_AUDIT` with B2 as a sub-result.
2. Add a "superseded — see §9" banner at the verdict block.
3. In the certificate, either replace the IBP and `subs(k0,0)` asserts with a genuine assertion (spatial = iλΣ_jξ_j(Tk)_j + residual), or describe them as convention restatements.
4. State the B1 temporal boundary term, and either widen the residual claim to the synchronous residual group or write "at least static".
5. Qualify "lapse and shift may be Lagrange multipliers" as Hamiltonian-form.

**W10: ACCEPT_WITH_REPAIRS**
1. Add a superseded banner at the top verdict block.
2. Qualify the shift-as-multiplier language (h₀ᵢ is quadratic in S_g⁽²⁾).
3. State that T_(0) in C2 must be the total four-species symmetric conserved stress, which is not constructed.

**W11: ACCEPT_WITH_REPAIRS**
1. Add a superseded banner at the top verdict block.
2. Restrict the F3 label and text to one-particle (quadratic) generators with full-ℤ³ invariance on the 2-component cell. State that interacting and supercell generators remain open, so contract F3 is not closed.
3. Record that K ≈ −H_* at the −I nodes and is two-to-one in θ ↔ π−θ.
4. In the certificate description, state that node completeness and the H_eff = −(arcsin|a|/|a|)a series are analytic inputs, and that the table is printed rather than asserted per row.
5. Optional: tighten ‖K − H_IR‖ ≤ Λ³/2.
