<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ b817ac0; lo que sigue a la cabecera es la respuesta sin editar)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.285 (Claude Code))
inicio: 2026-09-30T10:37:30Z  fin: 2026-09-30T10:42:06Z
documento: /home/ignac/qca-causal-cones/theory/W6_FULL_SPATIAL_TETRAD_GATE.md ; último commit: 318fff2 ; sha256 b5eef47f0377dfaa9fc6a7439fcb757f2a70f338f0062b97a174301bb22c1ceb
documento: /home/ignac/qca-causal-cones/theory/W12_FOUR_SPECIES_METRIC_UNIVERSALITY_GATE.md ; último commit: 2ff88b2 ; sha256 24fc0f507bfa82d6054293814da9c883a1fbcdd09f7c1204b2a789c6ecb66474
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w12-four-species-metric-universality.md ; último commit: 5485cb0 ; sha256 efc00217914112c324e4b919df6b3dddb8b535b151b0bf6dbd50756d5695b324
documento: /home/ignac/qca-causal-cones/scripts/verify_w12_four_species_metric_universality.py ; último commit: 5485cb0 ; sha256 dc17823a267a0085ec10f030e6e1bade738fbf91c95a3e119bf009fbbdbbcc73
documento: /home/ignac/qca-causal-cones/debates/2026-09-30--w12-blind-review/cjww_walk_definition.md ; último commit: sin versionar ; sha256 9ed70fe0ffd964d012a0f9a1013740942a126339ec598b7c1322d8522fc48417
entrada_opus.txt sha256 59dd88997890c404fb34c7a6cae04ef2daa86d49d1945a51cfd7e8dd664e09aa
respuesta sha256 4128eed4883b043a1560868e827ca7f80c3961d06d61d1d7b13f2149c251f1dc
-->

**Assumptions.** The imported `walk2()` equals Document 5. The SHA256 and commit hashes are taken as given; I cannot check them. I did not run the certificate, because `verify_directional_saturation.py` is not available to me. I also started an independent SymPy check in a scratch shell, but it returned no output I could read. Every recomputation below was therefore done by hand from Document 5.

---

## 1. Setting

The report follows the frozen contract on all four points:
- **Common coordinates:** δh_* uses lattice k_i at every node, with no species-dependent reflection.
- **Ranks on the coefficient of g:** Φ and the U4 map are Jacobians of δh/g with respect to the nine z_ar.
- **Only +I nodes decide:** Φ uses the four even-parity nodes only.
- **Both product orders:** both are computed.

One compliance gap: §2 of the contract says the −I nodes are "computed and reported". The report gives only their frames (U1 table). It gives no δE or δh for them. This matters; see §5.

## 2. Derivation

In Pauli form, W = c₁c₂c₃ I + i(s₁σ₁ − c₁s₂σ₂ + c₁c₂s₃σ₃). At p_* = πb this gives W = σ₁σ₂σ₃ I, so s_* = (−1)^{Σb}.

Linearizing, s_* W(p_*+k) = I + iσ^a E_a^i k_i with E_* = diag(s_*σ₁, −s_*σ₁σ₂, 1) = diag(σ₂σ₃, −σ₃, 1). This is correct, and so is every row of the 8-node table, including the τ columns. There is no identity (tilt) term at O(k), because ∂c₁c₂c₃ vanishes at the nodes.

For the control symbol, sin((p_*+k)·d_r) = cos(πb·d_r) sin(k·d_r) = τ_r (d_r·k) + O(k³). This is correct.

J(p_*) = 0, so the node does not move and there is no quasienergy shift at O(g). The O(gk) term is s_*·s_*(−igJ), which has no identity part. So:

  δE_*/g = −2 Z diag(τ_*) D, with D having rows d_r, and
  δh_*/g = −2(ε_* Z T_* D + Dᵀ T_* Zᵀ ε_*), where ε_* = E_*.

Both expressions in the report are correct. Two remarks:
- s_* = +1 at every +I node, so the s_* normalization cannot matter for the verdict.
- The product-order agreement is structurally guaranteed at O(gk), because W₀(p_*) is a scalar and J(p_*) = 0. It is a real check but carries no information.

**No errors found in the derivation.**

## 3. Linear algebra (recomputed)

Everything depends on the sign pattern S^*_{ar} = ε_a τ_r. Writing rows as a = 1, 2, 3:

| node | ε | τ | S (rows a) |
|---|---|---|---|
| (0,0,0) | (1,−1,1) | (+,+,+) | (+++), (−−−), (+++) |
| (1,1,0) | (−1,−1,1) | (−,+,+) | (+−−), (+−−), (−++) |
| (1,0,1) | (−1,1,1) | (−,−,+) | (++−), (−−+), (−−+) |
| (0,1,1) | (1,1,1) | (+,−,+) | (+−+), (+−+), (+−+) |

The diagonal of S is (+,−,+) at all four nodes, so diagonal Z is universal.

The universality condition is: (ΔS∘Z)D is antisymmetric. Its six component equations are:

- X₁₁+X₁₂+X₁₃ = 0
- X₂₂+X₂₃ = 0
- X₃₃ = 0
- X₁₂+X₁₃+X₂₁+X₂₂+X₂₃ = 0
- X₁₃+X₃₁+X₃₂+X₃₃ = 0
- X₂₃+X₃₂+X₃₃ = 0

Applying them to each pair against the reference node:
- **B−A** gives z₁₂ = −z₁₃, z₂₁ = 0, z₃₁ = −z₁₃.
- **C−A** gives z₁₃ = z₂₃ = z₃₁ = z₃₂ = 0.
- Together these force z₁₂ = 0.
- **D−A** adds nothing.

Result: 𝒰 = span{e₁₁, e₂₂, e₃₃}, dim 𝒰 = 3, rank Φ = 6. **Confirmed.**

On 𝒰, with Z = diag(a,b,c):
- ε_A Z D has rows (a,0,0), (−b,−b,0), (c,c,c).
- This gives δh/g = [[−4a, 2b, −2c], [2b, 4b, −2c], [−2c, −2c, −4c]]. **Confirmed.**
- The rank is 3, and the restricted 6×3 matrix matches the report.

The left null space (RREF) of that 6×3 map gives exactly the three stated relations: h₁₂ = ½h₂₂, h₁₃ = ½h₃₃, h₂₃ = ½h₃₃. **Confirmed.** This relation basis is not unique; only the image subspace is canonical.

Common kernel over the four +I nodes: it lies inside 𝒰, and the map on 𝒰 is injective, so the kernel is 0. **Confirmed.**

Facts the report omits:
- Each node's own metric map has rank 6, so W6 F3 holds node by node. The deficiency comes entirely from universality.
- Each node has a 3-dimensional frame-rotation kernel, {ε_* A D⁻¹ T_* : A antisymmetric}. These kernels are node-dependent. So the W6 F4 "kinematic frame redundancy" is not species-common.

## 4. Certificate

**Genuine checks:**
- U1: W(p_*) = s_*I is checked, and E_* is derived from the walk and compared with the closed form.
- U2: δE is compared with the independently computed formula −2Z diag(τ)D, at all eight nodes.
- U3/U4: exact integer ranks, nullspaces and annihilators.
- The verdict is computed by branching on the result, not hard-coded.

**Vacuous, weak or missing:**
- **U6 is tautological.** W·(I − 0·iJ) = W holds for any J. The script never checks that J(p) = 2sin(p·d_r)σ_a is the Fourier symbol of the real-space J_e under walk2's convention.
  - A global sign error would not change the verdict (it flips δh → −δh everywhere).
  - It is still unverified, so the report's "PASS … U6" overstates what was checked.
- **U5 post-asserts are vacuous.** After `assert not rotation_basis`, the next two asserts loop over an empty list or multiply 24×0 matrices. Only the emptiness assert has content.
- **Unasserted assumptions:**
  - J(p_*) = 0, i.e. no O(g) node shift.
  - Zero identity/tilt components of ∂W and of the O(gk) term; `extract_delta_e` projects onto σ_a only.
  - Both hold here, but the extraction formula silently depends on them.
- **Product-order check:** a real check, but structurally guaranteed (see §2).
- **Hard-coded expectations:** `expected_U` and the restricted matrix make the script a regression test for a known answer. That is acceptable because the values are computed first, not assumed.
- **"PASS for U1–U6":** the script prints [PASS] only for U6, U1 and U2. U3–U5 are printed values guarded by asserts. The report should state this distinction.
- **−I nodes:** δh is computed for them but never printed or reported.

## 5. Robustness of the negative conclusion

None of the convention choices changes the verdict:
- **Metric index placement:** δg_ij = −δh^{ij} at h = I. Kernels, ranks and relations are unchanged.
- **Global signs:** the Fourier or J sign, and k → −k, flip δh globally or not at all.
- **Species-dependent internal SU(2) relabelling:** E → RE and δE → RδE leave δh invariant.
- **s_* normalization:** s_* = +1 at all +I nodes.
- **Reference node:** ker Φ is the set where all four δh_* agree, so any reference gives the same 𝒰 and the same restriction.
- **D as rows vs columns:** fixed by the derivation. Transposing would be an error, not a convention.

Common coordinates are physically mandatory, not a convention. Moving between nodes is multiplication by (−1)^{b·x}, which is not a coordinate map, and every species lives in the same position space.

Including the −I nodes makes the result more negative, not less. On 𝒰 the diagonal sign pattern flips to (−,+,−) at every −I node, so δh_{−I} = −δh_{+I}. The universal space would be {0}, giving `NON_UNIVERSAL`.

**Is comparing δh the right test?** At O(k) the dispersion is ω² = kᵀh_*k, so equal δh_* is necessary for species universality. Failing it is sufficient for the non-universality result.

**Caveat on the reading of "rank 3/6"** (this is outside the contract):
- A constant δh is a pure linear coordinate change. The rank-6 requirement is therefore a proxy.
- If Z(x) varies slowly and the continuum limit is diffeomorphism-covariant, then the physical question is whether the three missing relations can be reached as a gauge condition.
- The linearized symbol of that condition, acting on ξ, has determinant −q₃(2q₁q₂ − q₁q₃ − q₂²).
  - This is nonzero for generic q, so the family is gauge-complete for generic wavevectors.
  - It fails on q₃ = 0 and on a cone; for example, x₃-independent perturbations generically cannot be reached.
- So even a gauge-aware criterion would not obviously turn the result positive, but the deficit is much smaller than "3 of 6 metric components".
- This caveat does not change the verdict under the contract, and the contract forbids after-the-fact rescue. It does affect how the negative result may be cited.

## 6. Scope

The claim ceiling is respected: first order in g and k, one-particle, W6 controls only, −I sector excluded, no dynamics, status PRELIMINARY.

**Overclaimed:**
- "PASS … U6" (tautological check).
- "exact comparison passes at all eight nodes" presented as evidence, when it is structurally guaranteed.
- Implying that three metric components are physically unreachable. That is true only for the constant (gauge-trivial) tangent space.

**Understated or omitted:**
- The −I δh results (required by the contract).
- The per-node rank of 6.
- The node-dependent per-node rotation kernels.
- That including −I would give `NON_UNIVERSAL`.

---

| Claim | Status | Reason |
|---|---|---|
| Node frames E_* and s_* (U1) | SUPPORTED | Rederived from the Pauli form of Document 5; all 8 rows match |
| δE_*/g = −2Z diag(τ_*)D (U2) | SUPPORTED | Follows from J(p_*) = 0, W₀(p_*) = s_*I, and the sin expansion |
| Product orders agree at O(gk) | SUPPORTED_WEAKER | True, but structurally guaranteed; not an informative test |
| U6 flat recovery | SUPPORTED_WEAKER | The certificate check is tautological; the real-space symbol convention is unchecked (verdict-neutral) |
| rank Φ = 6, 𝒰 = span{e₁₁, e₂₂, e₃₃} (U3) | SUPPORTED | Recomputed by hand from the sign table |
| rank(metric\|𝒰) = 3/6 and the three relations (U4) | SUPPORTED | Recomputed; the relations are a valid (non-unique) basis |
| No common frame-rotation direction (U5) | SUPPORTED | Common kernel lies in 𝒰, where the map is injective; the certificate's extra asserts are vacuous |
| −I nodes computed and reported | NOT_SUPPORTED | Only frames reported; δh_{−I} = −δh_{+I} on 𝒰 is omitted |
| Verdict `UNIVERSAL_SUBFAMILY_DEFICIENT` | SUPPORTED | Invariant under every convention the contract allows; including −I makes it stronger |
| "Closes the line" as a physical no-go | SUPPORTED_WEAKER | Contract-valid, but rank on constant δh ignores diffeomorphism counting; the gauge symbol is only non-elliptic |

**Verdict: ACCEPT_WITH_REPAIRS**

Mandatory repairs:
1. Report the −I δE and δh as the contract requires, including δh_{−I} = −δh_{+I} on 𝒰 and the fact that an 8-node test would give `NON_UNIVERSAL`.
2. Relabel U6 as "by construction". Alternatively, add a check that the real-space J_e has symbol 2sin(p·d_r)σ_a under walk2's Fourier convention, noting that the sign is verdict-neutral.
3. Add asserts that J(p_*) = 0 and that the identity/tilt components vanish at O(k) and O(gk). Remove or annotate the vacuous U5 asserts.
4. Change "PASS for U1–U6" to state which obligations are asserted and which are only printed. Describe the product-order agreement as structurally guaranteed.
5. Add a scope sentence: the rank deficiency concerns the constant, gauge-trivial metric tangent space. As a gauge condition, the three relations have a symbol vanishing only on q₃ = 0 and a cone. The negative result is a contract outcome, not a proof that the universal controls miss three physical metric degrees of freedom.
6. State that each node's own metric map has rank 6 and that the per-node rotation kernels are node-dependent. This makes clear that the deficiency comes from universality alone and that W6 F4's redundancy is not species-common.
