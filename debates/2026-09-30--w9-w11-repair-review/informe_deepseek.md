<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ b817ac0; lo que sigue a la cabecera es la respuesta sin editar)
modelo: deepseek-v4-pro, esfuerzo: por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
inicio: 2026-09-30T10:14:43Z  fin: 2026-09-30T10:21:49Z
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
entrada_deepseek.txt sha256 af7094b69bedb8e56200418628cb4981171cd65d065634c3fead1036714740e4
respuesta sha256 a762773a02fc4c7a1d21a01598c0959c18e74c6b2bef83ce0c01c09dd0973bcc
-->

Assumption: the certificates import a `walk2()` exactly matching the CJWW Eq. (5.15) shown in Document 10, and SymPy simplifications are reliable.

## 1. What is now claimed

**W9**  
Current claim is narrow:
- \(B1\): spatial-only coupling is not invariant under arbitrary time-dependent spatial gauge transformations; it is compatible only with static residual gauge.
- \(B2\): the full linearized coupling obeys the on-shell continuum identity \(\delta S_{\rm int}=-\lambda\int \xi_\nu \partial_\mu T^{\mu\nu}\), at \(O(\lambda)\), for an already symmetric conserved test stress.
- \(B3\): only zero-transfer spatial tetrad-source compatibility.
- \(B4\): microscopic lapse/shift/constraint/current completion is open.
- Explicitly not claimed: a constructed CJWW local stress tensor, reciprocal microscopic coupling, off-shell Einstein–Weyl action, local-Lorentz Ward identity, or W6 rank result.

**W10**  
Current state is \(OPEN\_AFTER\_AUDIT\):
- \(C1\): explicit continuum action convention and sourced constraints.
- \(C2\): flat test-source consistency at \(O(\lambda)\) only.
- \(C3\): zero-transfer spatial tetrad source partial.
- \(C4\): microscopic CJWW charges open.
- \(C5\): not met.
- Explicitly not claimed: microscopic Floquet stress, Gu–Wen L-model dynamics, coupled closure, Newton constant.

**W11**  
Current state is \(OPEN\_AFTER\_AUDIT\):
- \(F1\): four zero-quasienergy species near \(+I\) nodes.
- \(F2\): integrated charge surrogates and zero-transfer tetrad structures only.
- \(F3\): no continuous periodic translation-invariant Hermitian logarithm.
- \(F4\): global bond momentum conserved; local stress open.
- Explicitly not claimed: full Belinfante stress, \(q\neq 0\) kernels, interacting conservation, exact microscopic Floquet stress.

## 2. W11 node table

The table is correct.

For \(p_i=\pi b_i\), set \(s_i=(-1)^{b_i}\). From
\[
W=a_0I+i\sigma\cdot a,\qquad
a_0=c_1c_2c_3,\quad a=(s_1,-c_1s_2,c_1c_2s_3),
\]
the condition \(W=\pm I\) is \(a=0\) and \(a_0=\pm1\). Since \(\det W=1\), this requires all \(\sin p_i=0\), hence \(p_i\in\{0,\pi\}\), giving exactly eight nodes.

The frame is
\[
E_*=\operatorname{diag}(s_2s_3,\,-s_3,\,1),
\]
with \(s_*=\prod_i s_i\). This reproduces every row of the table. The chirality column is
\[
\operatorname{sgn}\det(-E_*)=-\operatorname{sgn}\det E_*,
\]
and the four \(+I\) rows have chiralities \(2\times(+1),2\times(-1)\), so net chirality zero. No error found.

## 3. W11 energy charge \(K=i(U-U^\dagger)/2\)

Supported.

- \(K=-\sigma\cdot a\) is Hermitian and \([K,U]=0\) since both are built from the same \(\sigma\cdot a\).
- Real-space hoppings \(B_r=i(A_r-A_{-r}^\dagger)/2\) satisfy \(B_{-r}=B_r^\dagger\), and the stated density sums to \(\langle\psi,K\psi\rangle\). Range is at most one site per coordinate.
- On the four \(+I\) balls, \(a_0=\prod_i\cos k_i>0\). With \(\cos\theta=a_0\),
  \[
  K=-\sin\theta\,(a\cdot\sigma)/|a|,\qquad H_{\rm eff}=-\theta\,(a\cdot\sigma)/|a|,
  \]
  so \(K=\sin H_{\rm eff}\).
- The inequality
  \[
  \sin^2\theta=1-\prod_i(1-\sin^2 k_i)\le \sum_i\sin^2 k_i\le |k|^2
  \]
  is valid for the stated range. Hence \(\theta\le\arcsin\Lambda\), and
  \[
  \|(K-H_{\rm eff})P_\Lambda\|=\|\theta-\sin\theta\|\le \frac{(\arcsin\Lambda)^3}{6}.
  \]
  The dynamical bound follows by Duhamel/telescoping, with factor \(|n|\). No correction needed.
- \(\|K-H_{\rm IR}\|\le\Lambda^3\) is also valid. For \(R^2=|p|^2\le\Lambda^2\), the vector coefficient components of \(K-H_{\rm IR}\) are bounded by \(R^3/2\), giving norm \(\le R^3/\sqrt2\le\Lambda^3\). The p3-axis cubic coefficient \(1/6\) is correct.

## 4. W11 F3 obstruction

The proof is valid.

- From \(\det W=1\), any continuous Hermitian logarithm \(H(p)\) with \(e^{-iH}=W\) has \(e^{-i\operatorname{tr}H}=1\), so \(\operatorname{tr}H\in2\pi\mathbb Z\) is constant on the connected torus.
- \([H,W]=0\).
- Near a node, \((W(p_*+tn)-s_*I)/t\to i s_*\sigma\cdot E_*n\). Even if \(H\) is only continuous, passing the divided commutator to the limit gives \([H(p_*),\sigma\cdot E_*n]=0\) for every \(n\). Since \(E_*\) is invertible, \(H(p_*)=c_*I\).
- At a \(+I\) node, \(c_*\in2\pi\mathbb Z\), so \(\operatorname{tr}H=2c_*\) is an even multiple of \(2\pi\). At a \(-I\) node, \(c_*\in(2\mathbb Z+1)\pi\), so \(\operatorname{tr}H\) is an odd multiple of \(2\pi\). Contradiction.

The stated scope is correct: this rules out continuous translation-invariant Hermitian logarithms, including finite-range hopping logarithms, but not general QCAs, translation-breaking generators, or time-dependent circuits.

## 5. W10

The explicit continuum calculation is supported.

- The signature, trace convention, \(G_{\mu\nu}^{\rm lin}\) formula, and
  \[
  S_g=-\frac12\int h_{\mu\nu}G^{\mu\nu},\qquad
  S_{\rm int}=\frac{\lambda}{2}\int h_{\mu\nu}T^{\mu\nu}
  \]
  are internally consistent.
- The certificate checks all ten variations, including the off-diagonal multiplicity factor \(2\). The resulting equations are
  \[
  G^{\mu\nu}=\frac{\lambda}{2}T^{\mu\nu}.
  \]
- The lapse/shift factors are correct: diagonal \(h_{00}\) gives one factor, off-diagonal \(h_{0i}\) gives two in the variation. Thus \(C^\nu=2G^{0\nu}\) gives the reported scalar/vector constraints.
- The component formulas for \(C^0\) and \(C^i\) match the certificate.
- The new \(OPEN\_AFTER\_AUDIT\) state is consistent: the continuum fixed-source calculation passes, but the microscopic/reciprocal completion does not.

## 6. W9

The repaired certificate supports the narrow W9 claim.

- It constructs symmetric \(h,T\), uses \(\delta h_{\mu\nu}=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu\), checks the \(1/2\) coupling factor, and verifies the full gauge variation.
- The spatial variation is correctly split into a conserved-shell temporal residual:
  \[
  \delta S_{\rm spatial}
  =
  -\lambda\int (\partial_t\xi_j)T^{0j},
  \]
  which vanishes for static \(\xi_j\). The certificate checks this without dividing by a momentum component.
- It does not derive stress conservation and does not check W6 rank or microscopic source matching.
- The remaining PASS is stated at the right scope: an algebraic on-shell \(O(\lambda)\) continuum identity, not a constructed CJWW bridge.

## 7. Certificates

**W9 certificate**  
Checks: symmetric \(h,T\), full and spatial gauge variation, factor \(1/2\), and static residual case. It takes stress conservation as input. Matches the addendum. The “after integration by parts” check is mostly an algebraic sign/factor consistency check, not an independent derivation, but it is not vacuous.

**W10 certificate**  
Checks: linearized Einstein operator, Bianchi identity \(\partial_\mu G^{\mu\nu}=0\), gauge identity \(G(\partial\xi)=0\), all ten variations with correct multiplicity, scalar/vector constraint formulas, and a TT wave-operator limit. Matches the report. It does not check source conservation in a coupled QCA or Gu–Wen lattice dynamics.

**W11 certificate**  
Checks: exact SU(2) decomposition, unitarity/det, K hoppings, Hermiticity, range, \([K,U]=0\) by Bloch algebra and real-space convolution, eight nodes/frames/chiralities, old momentum charge conservation, old \(H_{\rm IR}\) quartic commutator, arbitrary-direction jets, and the p3-axis cubic coefficient. It does not construct \(q\neq0\) stress kernels or interacting constraint identities. The node completeness is only asserted in a comment, but it follows elementarily from \(a_0^2+|a|^2=1\), and I verified it.

## 8. Consistency of the downgrades

The downgrades are consistent.

- W9’s continuum on-shell identity does not depend on an unknown microscopic stress tensor; the addendum explicitly conditions only the CJWW application on W11.
- W10’s \(C2\) is limited to a flat test source at \(O(\lambda)\) and does not rely on the missing full W11 local source.
- W11’s \(F1/F3\) and K bounds are free-walk statements; \(F2\) is explicitly downgraded to integrated charges and zero-transfer tetrad structures.
- No remaining PASS requires a quantity marked open in the same report.

The only mild presentation issue is W9’s retained terminal label `CONTINUUM_GRAVITON_MATTER_BRIDGE_PASS / MICROSCOPIC_SPACETIME_COMPLETION_OPEN`; without the addendum qualifier it overstates the result.

## Final table

| Gate | Claim | Status | Reason |
|---|---:|---|---|
| W9 | Conditional on-shell continuum gauge identity; static residual compatible; microscopic completion open | SUPPORTED_WEAKER | Certificate supports the algebra, but it is only a continuum on-shell identity, not the named bridge PASS. |
| W10 | \(OPEN\_AFTER\_AUDIT\); explicit continuum constraints and \(O(\lambda)\) flat test-source consistency | SUPPORTED | Continuum action, factors, constraints, and Bianchi/gauge identities check out; microscopic completion remains open. |
| W11 | \(OPEN\_AFTER\_AUDIT\); node table, K charge bounds, no continuous translation-invariant logarithm; \(F2\) downgraded | SUPPORTED | Node/frame/chirality table, K bounds, and no-go proof are valid; full local stress/interacting conservation remains open. |

## Final verdicts

- **W9:** ACCEPT_WITH_REPAIRS  
  Mandatory repair: replace the main terminal label with one that states the actual scope, e.g.  
  `ON_SHELL_CONTINUUM_IDENTITY_PASS / MICROSCOPIC_SPACETIME_COMPLETION_OPEN`, and make the downgraded B1/B2/B3 labels primary.

- **W10:** ACCEPT  
  Accept as a correctly downgraded \(OPEN\_AFTER\_AUDIT\) report.

- **W11:** ACCEPT  
  Accept as a correctly downgraded \(OPEN\_AFTER\_AUDIT\) report.
