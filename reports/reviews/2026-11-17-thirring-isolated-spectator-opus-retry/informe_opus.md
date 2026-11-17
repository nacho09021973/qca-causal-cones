<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.322 (Claude Code))
opus.json sha256 b72d5166ebaf9bafe175489f33b60152dd61d0b072b75992e2fded01f79be88b
inicio: 2026-11-17T07:38:39Z  fin: 2026-11-17T07:42:47Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-17--thirring-isolated-spectator.md ; último commit observado: 8d02630 ; sha256 de la copia enviada 519acf05033347626c8ca4f7b138b890f323421cf0714123dcf6fd18e7051934
documento: /home/ignac/qca-causal-cones/theory/THIRRING_ISOLATED_SPECTATOR_GATE.md ; último commit observado: a9d5ae1 ; sha256 de la copia enviada 5c959b560953e1db9a4d2ba2a340b7c3f28ea5237df915e35d236676bcb1be7a
documento: /home/ignac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.md ; último commit observado: e6bcef1 ; sha256 de la copia enviada 6d5359d70f16c654326de2fa828408880a21251e075a9dfcef7c3335f7276962
documento: /home/ignac/qca-causal-cones/reports/2026-11-14--thirring-flavour-packet.md ; último commit observado: 918f7f4 ; sha256 de la copia enviada 39e595ce17ac1e5f2f0ad6fa3821f5e413e44ed2a0126aa39c4674e58eb8118e
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.md ; último commit observado: 55f2b43 ; sha256 de la copia enviada d5d21b221fc3c70d15dfb6c57cbc40372a51a40c2bda59b14eb7c974546d2f2f
documento: /home/ignac/qca-causal-cones/theory/THIRRING_FLAVOUR_PACKET_GATE.md ; último commit observado: d0c59cb ; sha256 de la copia enviada df61430f415eddc5e3186e19bfcd61f5fa15a33299c61a4d9880409f58a22231
documento: /home/ignac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_opus.txt sha256 8c0d8457746150487da65e5942b1a03e70deb1f96723c6172f93bd9b051b6557
respuesta sha256 758a817bf75822ace9eaa36e60f08ae99a16cfeec85c813304ee3c04fcb6d246
-->

# Adversarial review: isolated-spectator corollary (2026-11-17)

**Scope.** One round, written analysis only. Nothing was executed. I re-derived every step of Document 1 from the rule in Document 7, using the supplied reports only where Document 1 cites them. I did not count review or promotion labels as evidence.

---

## A. Re-derivation of the new claims

### A1. On-site rule and the exact decoupling lemma (Doc 1 §1): correct

- **Phase operator.** J = exp(iχ Σ_x n↑(x)n↓(x)) is diagonal in the occupation basis. Each site holds at most two fermions, so in first quantization J_N multiplies a configuration by e^{iχ·#(doubly occupied sites)}.
- **Phase count.** Take ψ with both coordinates in A and v supported in B, with A ∩ B = ∅. In every configuration of ψ∧v the third particle sits on a site no pair particle occupies, so the count equals the pair's count.
  - This includes pair configurations where both pair particles are on one site with opposite components (phase e^{iχ}).
  - Same-site, same-component configurations are excluded by antisymmetry.
  - J is permutation-symmetric, so it commutes with antisymmetrization. A fixed wedge order gives only an overall sign, which J does not see.
  - Hence J₃(ψ∧v) = (J₂ψ)∧v.
- **Free step.** W^{⊗3} commutes with the antisymmetrizer, so F₃(ψ∧v) = (F₂ψ)∧Wv.
- **Locality.** W in Doc 7 has entries νT_x^{±1} and −iμ, so it has range one. J moves nothing. Therefore U₂^sψ has both coordinates in A+[−s,s], and W^s v lies in B+[−s,s].
- **Induction.** The induction needs disjointness only at s = 0,…,T−1, the instants just before each J acts. Document 1 states "each intervening time", which covers this.
- **Geometry.**
  - A+[−t,t] = [−L−R−t, L+R+t] and B+[−t,t] = [−50L−R−t, −50L+R+t].
  - The gap is 49L−2R−2t. At t = 20L this is 9L−2R ≥ 17L/2, since R ≤ L/4.
  - Positive throughout. ✔
- **Spectator motion.** The spectator (K = −2, positive band) moves toward +x at about 0.894. The pair moves toward −x. So isolation here is genuinely a light-cone statement within T, not diverging motion.

No factorization hypothesis enters. The lemma is a pure locality identity.

### A2. Exact code isometry (Doc 1 §2): correct

- **Momentum supports.** The intervals [Kμ−δ, Kμ+δ] for K = 3, 1, −2 are separated by 2μ and 3μ. Both exceed 2δ = 2μ^{3/2}.
- **Range.** All supports lie in |q| ≤ 0.3 + μ^{3/2} < 0.4. Their π-translates lie at distance > π − 0.8 from all of them.
- **Inner products.** Γ is on-site and shifts momentum by π. Therefore:
  - ⟨φ_j, Γφ_k⟩ = 0 and ⟨φ_j, φ_k⟩ = δ_jk.
  - ⟨Π_aφ_j, Π_bφ_k⟩ = ¼δ_jk(1 + s_a s_b) = ½δ_jkδ_ab.
  - So the six u_ja are orthonormal.
- **Isometry.** Each wedge takes exactly one mode per packet label j. Two wedges share a mode set only if their (a,b,c) coincide. So B is an isometry, and C = F₃^T B is an isometry because F₃ is unitary. ✔

### A3. Initial tails (Doc 1 §2): correct

I checked the t = 0 case directly rather than relying on the cited estimate.

- **Envelope.** h = (√15/4)(1−t²) vanishes at ±1, and h′ jumps there. Two integrations by parts give |φ(x)| ≲ δ^{1/2}(1 + δ|x − x_c|)^{−2}.
- **Spinor derivatives.** In scaled variables (δ/μ)^j = μ^{j/2}, which is bounded. The positive-band spinor has |N₊|² = μ² + |g₊|² ≥ μ², so it is smooth in K = q/μ for every K, including K = −2. No degeneracy enters at t = 0.
- **Squared tail.** The mass beyond R is ≲ (δR)^{−3}.
  - L ≥ 101 gives R = ⌊L/4⌋ ≥ L/5.
  - δL ≥ μ^{−1/2}.
  - So (δR)^{−3} ≤ 125·C·μ^{3/2}.
- **Norm tail.** ε = O(μ^{3/4}), uniform over the three compact K sets.
- **Flavour.** The cutoff Q_j commutes with Γ, so the flavour projection costs at most √2.
- **Truncated modes.** They have norm ≤ 1 and are not renormalized, as the contract requires. ✔

### A4. Transfer to original packets (Doc 1 §3): correct, no time accumulation

- **Creation bound.** With the normalized determinant convention, ψ∧v = c†(v)ψ up to sign, so ‖ψ∧v‖ ≤ ‖ψ‖‖v‖.
- **Input truncation.**
  - ‖ψ−ψ̃‖ ≤ ε + ‖Qu_f‖ε ≤ 2ε.
  - ‖ψ∧v − ψ̃∧ṽ‖ ≤ 2ε + ‖ψ̃‖ε ≤ 3ε.
- **Evolution comparison.** I split the difference into three terms:
  - U₃^T(ψ∧v − ψ̃∧ṽ): at most 3ε.
  - U₃^T(ψ̃∧ṽ) − (U₂^Tψ̃)∧W^Tṽ: exactly 0 by A1. The supports of ψ̃ and ṽ satisfy the hypotheses.
  - (U₂^Tψ̃)∧W^Tṽ − (U₂^Tψ)∧W^Tv: at most 2ε + ε by unitarity.
  - The total is 6ε. The truncation is applied once, at t = 0, and both comparisons are unitary, so there is no factor of T. ✔
- **Pair bridge on original packets only.** η is applied to U₂^T B₂|ab⟩ with the untruncated original modes. The truncated pair ψ̃ enters only the exact lemma. ✔
- **Target.** (F₂^T B₂V|ab⟩)∧W^T u_ec = Σ V_{a′b′,ab} F₃^T(u_fa′∧u_sb′∧u_ec) = C(V⊗I)|abc⟩. The order is (f,s,e) on both sides, so there is no sign. ✔
- **Operator norm.** Each column residual is ≤ 6ε + η. For an arbitrary x ∈ ℂ⁸, including entangled inputs, Σ|x_i|r_i ≤ ‖x‖√8·max r_i. So ρ ≤ √8(6ε + η). ✔
- **Compression and leakage.**
  - ‖K − V⊗I‖ = ‖C*(U^TB − C(V⊗I))‖ ≤ ρ.
  - E = (I−CC*)(U^TB − C(V⊗I)), because (I−CC*)C = 0, so ‖E‖ ≤ ρ. ✔
- **Consistency.** V_co is unitary: α is imaginary, β is real and |α|² + β² = 1. Hence K*K + E*E = I is consistent, and Document 1 correctly calls this check non-probative.

### A5. Output frames and signs (Doc 1 §4): correct

- **Free centres at T = 20L.**
  - Fast: L − v_f T ≈ −18L.
  - Slow: −L − v_s T ≈ −15L.
  - Spectator: −50L + v_e T ≈ −32L.
  - Decreasing-position order is therefore (s,f,e), against the initial order (f,s,e).
- **Sign of D.** D|abc⟩ = W^Tu_sa ∧ W^Tu_fb ∧ W^Tu_ec = −C|bac⟩, so D = −C(P⊗I).
- **Limit in the spatial frame.** D*U^TB = −(P⊗I)K → −(PV)⊗I. This matches Document 3's "PV up to a common sign". ✔
- **Flavour labels.** T is even and WΠ_A = Π_BW, so the frame modes carry the declared flavour labels. Document 1 does not say this explicitly; see O2.

### A6. Circularity and scope

- **No circular use of factorization F.** The only "F" in the proof is F_n = ∧ⁿW, the free walk. The three-body statement is derived, not assumed.
- **No overreach.** Document 1 claims no successive or simultaneous scattering, no general F, and no novelty. COEXISTENCE and NOVELTY are left OPEN. This is consistent with the contract.

---

## B. Inherited assumptions versus new claims

| Item | Status |
|---|---|
| Decoupling lemma, geometry, isometry of B and C, 6ε transfer, √8 assembly, K/E bounds, frame signs | **New, proved here**; re-derived above |
| Initial-time tail bound ε = O(μ^{3/4}) | Cited from Doc 5 §4(iii); **independently checkable at t = 0** and verified above |
| η = O(μ^{1/2}) + O(μ^{3/4}) at T = 20L, no extra phase | **Inherited hypothesis H_pair**. Its chain is: Doc 3 §3 (written co-moving adaptation) → Doc 4 §4 ((+,−) adaptation) → Doc 5 §4 (contract-2 bridge). It is not re-derived here and not assessed in this review. |

---

## C. Mandatory objection

**M1 — The provenance of the sole inherited hypothesis is stated by a label the supplied material does not support.**

- Document 1's verdict line and §3 condition the result on "the promoted pair bridge". The supplied Document 3 header says "**no promotion**".
- Document 2 asserts that CURRENT_STATE records a promotion, but CURRENT_STATE is not supplied. Document 3's own §1 still says "The adaptation is not reviewed", which conflicts with its header.
- The corollary's logical form ("if H_pair then the bound") is unaffected. But the verdict line is the record of what the result rests on.

Required repair, either of:

1. Cite the specific CURRENT_STATE entry or commit that records the promotion. **or**
2. Replace "promoted pair bridge" with an explicit hypothesis: H_pair: ‖U₂^T B₂ − F₂^T B₂V(r_co)‖ = O(μ^{1/2}) + O(μ^{3/4}) at T = 20L, as written in Doc 3 §3, resting on Doc 4 §4 and Doc 5 §4. Add a one-line table, like §B above, separating proved from inherited items.

No mathematical repair is required.

---

## D. Optional improvements

- **O1.** Rename the free evolution, for example to W_n = ∧ⁿW. Then "no assumed F" in §1 unambiguously means factorization, and readers cannot confuse it with F₃, which the proof uses throughout.
- **O2.** State explicitly two facts the proof currently leaves implicit:
  - Separation is needed only for s = 0,…,T−1.
  - T = 20L is even, so the C and D frame modes satisfy W^T u_ja = √2 Π_a W^T φ_j, and the flavour labels survive.
- **O3.** Reword the frame justification in §4.
  - The (f,s) reversal of *frame* centres follows from free group velocities. Doc 3 §3(iv) gives a free-centre difference ≤ −3L/5. The interacting bridge is not needed for this.
  - The spectator ordering follows from the light cone of the truncated free modes: [−70L−R, −30L+R] versus [−21L−R, 21L+R].
- **O4.** Write the explicit constant chain: ε ≤ √2·5^{3/2}·C^{1/2}·μ^{3/4}, with C the t = 0 constant for h. Also note that the spectator moves *toward* the pair, so isolation is by light cone within T.
- **O5.** Fix the typo "multipartarticle" in the header.

---

## Verdict

**REPAIR_REQUIRED** (single mandatory item, M1: provenance wording only).

Every new claim survives adversarial re-derivation:

- the exact on-site decoupling;
- the light-cone geometry with margin ≥ 17L/2;
- the exact isometry of B and C;
- the t = 0 tail bound;
- the T-independent 6ε transfer;
- the √8(6ε + η) operator-norm bound, uniform over arbitrary entangled inputs;
- the compression and leakage bounds;
- both frame signs, including D*U^TB → −(PV)⊗I.

The pair theorem is applied only to original packets, and factorization F is not used circularly. Once M1 is applied, the correct classification is **REDUCES_TO_EXISTING_RESULTS**, conditional on H_pair as explicitly stated. It does not establish general F, successive or simultaneous three-body scattering, or novelty. This review is closed; no further round is proposed.
