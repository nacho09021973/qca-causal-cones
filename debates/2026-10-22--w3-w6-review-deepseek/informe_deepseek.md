<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ d32e8507c32aefc0acd0721a000eeeb2a261d824; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 9b4a1d94214494e23afece076b33e017e142a7c79f1b026be0dcea2a1a9b1557; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, max_tokens=por defecto de la API, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 2cc4f4d859b187c8cbbd2180f8ca42254f7f9ae653857aea0237104431bce31b
inicio: 2026-10-22T08:31:02Z  fin: 2026-10-22T08:39:43Z
documento: /home/ignac/qca-causal-cones/theory/W3_BACKREACTING_TETRAD_FLOQUET_GATE.md ; último commit observado: d576fda ; sha256 de la copia enviada 7bb0cb7d9d04d6e22ffa9fc740f535beabfc40815cd822c214a72d2636992f41
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w3-backreacting-tetrad.md ; último commit observado: 2b982f2 ; sha256 de la copia enviada 72639112fbebf897a33c83b4ff65bc01e52ce5904db818cb45ff4389063fac35
documento: /home/ignac/qca-causal-cones/scripts/verify_w3_backreacting_tetrad.py ; último commit observado: f1f54c9 ; sha256 de la copia enviada 33859d49d2d4d7466a28fdde9c1623bc3400ba010bade3d26ec70ff6d1806d2b
documento: /home/ignac/qca-causal-cones/theory/W4_GEOMETRY_STIFFNESS_GATE.md ; último commit observado: d2eea01 ; sha256 de la copia enviada 56c28a52714f749f52049777f0a97e3e3ccceb77326f3c39b313289cd29d529d
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w4-geometry-stiffness.md ; último commit observado: d2eea01 ; sha256 de la copia enviada 8c7f70ea346c38cf40a6c9926240821415f00ea6453369254bf22de8ba0f62b6
documento: /home/ignac/qca-causal-cones/scripts/verify_w4_geometry_stiffness.py ; último commit observado: 3099bd5 ; sha256 de la copia enviada e83a7ed3d4c4a3e09baf3692ba504b11f4e49b579ba741ea8f4c1ae61fa836fb
documento: /home/ignac/qca-causal-cones/theory/W5_TETRAD_CONJUGATE_SOURCE_GATE.md ; último commit observado: 607e2ab ; sha256 de la copia enviada 749365ef8a8053a43bda2953a429c6182a77376f3fa0f2cc8099cc9d0e6681de
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w5-tetrad-conjugate-source.md ; último commit observado: 607e2ab ; sha256 de la copia enviada 4fcb92f5197c71739311e2d89a90152cbe02f5bea9bb2a3be5eeef94f0fd50db
documento: /home/ignac/qca-causal-cones/scripts/verify_w5_tetrad_source.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 347e38bdc45a511c6f03a219d10b5fa0ad8f906073e08e42ca76860e2eb6cb98
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/theory/W6_FULL_SPATIAL_TETRAD_GATE.md ; último commit observado: 32387b0 ; sha256 de la copia enviada 012afa5fe56697680087d6ce21dc6eb388a303da0798551626d5cf1fcfeb0216
documento: /home/ignac/qca-causal-cones/reports/2026-09-30--w6-full-spatial-tetrad.md ; último commit observado: 32387b0 ; sha256 de la copia enviada 9e7400e62eb10f6bf5cc4b80e44d98bca37d46dfa8a7b6e250e388210152de89
documento: /home/ignac/qca-causal-cones/scripts/verify_w6_full_spatial_tetrad.py ; último commit observado: 1137a14 ; sha256 de la copia enviada 1de52a5ca8fcd13514c2140be9765251e2a28d5796c15b3c9847edebd62f1b35
documento: /home/ignac/qca-causal-cones/debates/2026-09-30--w12-blind-review/cjww_walk_definition.md ; último commit observado: 4b0797d ; sha256 de la copia enviada 9ed70fe0ffd964d012a0f9a1013740942a126339ec598b7c1322d8522fc48417
entrada_deepseek.txt sha256 1524ba64400b7f5111eb98a0179bf86650fae634a7bc74547bbcb27869089163
respuesta sha256 32d6b9eb0e67fcf22e8b0345f770398f36b1050a71eff84a41081f11da5f3570
-->

Assumption: I use the Pauli and QW conventions in the documents. I treat the cited W2 tetrad-symbol result and the earlier W3 coarse-metric kinematics result as external prior results only where explicitly stated; if those are not granted, the affected items weaken further, as noted.

---

## W3: Backreacting tetrad Floquet gate

### 1. Contract compliance
The report addresses W3.1–W3.6 as frozen. It does not move the goalposts: the Einstein/source ceiling is respected.

### 2. Derivations
- Since \(A_e^2=A_e\), the Heisenberg update splits into \(A_e=0\) and \(A_e=1\). On the \(A_e=1\) sector,
  \[
  e^{igY}Z e^{-igY}=Z\cos 2g-X\sin 2g,
  \]
  so
  \[
  R_e^\dagger(Z\otimes I)R_e
  =
  Z\otimes(I-A_e)
  +
  \bigl(Z\cos2g-X\sin2g\bigr)\otimes A_e.
  \]
  This is correct.
- For an initially uncorrelated state,
  \[
  z'_e=z_e+a_e[(\cos2g-1)z_e-\sin2g\,x_e],
  \]
  hence
  \[
  z'_e-z_e=-2g\,x_ea_e+O(g^2).
  \]
  Correct.
- The tetrad-control formula
  \[
  E(z)=E_0-2g\operatorname{diag}(z_1,z_2,z_3)D+O(g^2)
  \]
  is consistent with the current symbol
  \[
  J_a(p)=2\sin(p\cdot d_a)\sigma_a=2d_a^i p_i\sigma_a+O(|p|^3)
  \]
  under the semiclassical replacement \(Z_e\mapsto z_e\). The algebraic backreaction
  \[
  \delta E_{\rm back}=4g^2\operatorname{diag}(x_1a_1,x_2a_2,x_3a_3)D+O(g^3)
  \]
  follows.
- No algebraic sign error found.

### 3. Hidden assumptions
- \(z_e=\langle Z_e\rangle\) is inserted into \(T_e\), i.e. a mean-field/semiclassical replacement. It is not exact beyond leading order or beyond uncorrelated backgrounds.
- The \(Z\)-update is derived only for initially uncorrelated states. After \(R_e\), geometry and matter are entangled; re-inserting \(z'\) into \(E(z')\) for the next transport step is another mean-field assumption.
- The finite-depth bound is only for the added W3 interaction, not for the frozen CJWW \(U_0\).
- The exact number “twelve layers” is inherited from W2 and not independently checked here.

### 4. Certificate
The script checks:
- the exact \(Y\)-rotation of \(Z\) on the occupied sector;
- the derivative of the declared \(z'-z\) formula;
- \(D\) invertibility and the declared \(E(z)\) formula at \(g=0\);
- the algebraic \(O(g^2)\) backreaction.

It does **not** derive \(E(z)\) from the Fourier symbol of \(J\) or from \(T_e=e^{-igZ\otimes J}\). That part is asserted, not derived. Thus the certificate for W3.3 is weaker than the report suggests.

### 5. Scope
The “no Einstein claim” ceiling is respected.

### Verdict: ACCEPT_WITH_REPAIRS

Mandatory repairs:
1. Explicitly label W3.3 as semiclassical/mean-field and leading-order only.
2. Strengthen the certificate so that \(E(z)=E_0-2g\operatorname{diag}(z_a)D\) is derived from \(J_a(p)\), not merely asserted.
3. State that W3.5 re-uses \(z'\) as a classical background despite post-\(R_e\) entanglement.

---

## W4: Geometry stiffness gate

### 1. Contract compliance
W4.1–W4.6 are addressed. However W4.5 depends on an external W3 coarse-curvature formula not present in the supplied W3 materials.

### 2. Derivations
- The SWAP identity
  \[
  S_{ef}=\frac12(I+X_eX_f+Y_eY_f+Z_eZ_f)
  \]
  is correct.
- Therefore
  \[
  K_{ef}(\kappa)=e^{-i\kappa(I-S_{ef})}
  =\exp(-i\kappa)\bigl[\cos\kappa\,I+i\sin\kappa\,S_{ef}\bigr].
  \]
- Every identical two-qubit product state \(|n,n\rangle\) satisfies \(S|n,n\rangle=|n,n\rangle\), so \(K_\kappa|n,n\rangle=|n,n\rangle\). Correct.
- For \(|1,0\rangle\),
  \[
  K|1,0\rangle
  =
  e^{-i\kappa}\left(\cos\kappa\,|1,0\rangle+i\sin\kappa\,|0,1\rangle\right),
  \]
  giving
  \[
  \langle Z_e\rangle=-\cos2\kappa,\qquad \langle Z_f\rangle=\cos2\kappa.
  \]
  Correct.
- Repeated finite-speed propagation follows from the brickwork locality of partial swaps.
- W4.5: if the cited linearized curvature formula
  \[
  R^{(1)}=-4g\,\partial_2^2z_1
  \]
  is accepted, then a moving \(Z\)-defect changes the discrete second-difference curvature witness. But that formula is not derived or checked in the supplied W3/W4 documents.

### 3. Hidden assumptions
- W4.5 is a kinematic/linearized coarse-field statement, not a curvature wave equation.
- The curvature propagation is really defect/texture propagation under partial SWAPs.
- The finite-depth statement concerns the geometry-only addition \(K_\kappa\), not the full step including CJWW \(U_0\).

### 4. Certificate
The script checks:
- SWAP is Hermitian/unitary and equal to the Pauli expression;
- the generator of \(K(\kappa)\);
- identical product states are fixed;
- the \(|1,0\rangle\) propagation and \(\langle Z_e\rangle,\langle Z_f\rangle\);
- full transfer at \(\kappa=\pi/2\).

It does **not** check W4.5’s coarse-curvature formula or the finite-depth brickwork bound.

### 5. Scope
The report mostly respects the ceiling, but “coarse-curvature propagation” is justified only conditionally on the external W3 curvature kinematics result.

### Verdict: ACCEPT_WITH_REPAIRS

Mandatory repairs:
1. Include or certify the W3 coarse-curvature formula \(R^{(1)}=-4g\partial_2^2z_1\) in the W4 record.
2. Reword W4.5 as “linearized kinematic curvature witness transport,” not autonomous curvature dynamics.
3. Clarify that finite-depth is only for \(K_\kappa\), not for the full CJWW-containing step.

---

## W5: Tetrad-conjugate source gate

### 1. Contract compliance
S1–S4 are addressed; S5 is explicitly left open. The contract’s “no full stress-energy tensor” ceiling is respected.

### 2. Derivations
- On its support,
  \[
  J_e^2=A_e,\qquad J_e^3=J_e.
  \]
  Hence
  \[
  \cos(2\eta J)=I+(\cos2\eta-1)A_e,
  \qquad
  \sin(2\eta J)=\sin2\eta\,J_e.
  \]
  Correct.
- The Heisenberg transformation
  \[
  R_e^{(T)\dagger}Z_eR_e^{(T)}
  =
  Z_e\cos(2\eta J_e)-X_e\sin(2\eta J_e)
  \]
  is correct.
- For initially uncorrelated states,
  \[
  z_e'=z_e[1+(\cos2\eta-1)a_e]-x_e\sin2\eta\,j_e,
  \]
  and
  \[
  z_e'-z_e=-2\eta x_ej_e-2\eta^2 z_ea_e+O(\eta^3).
  \]
  Correct.
- The Fourier symbol
  \[
  J_a(p)=2\sin(p\cdot d_a)\sigma_a
  =
  2d_a^i p_i\sigma_a+O(|p|^3)
  \]
  is correct.

### 3. Hidden assumptions
- \(\delta H_m=g z_e J_e\) is the leading-order effective generator after replacing \(Z_e\) by \(\langle Z_e\rangle\). It is not the full Floquet Hamiltonian.
- The variational relation
  \[
  \frac{\partial H_m}{\partial z_e}=gJ_e
  \]
  is therefore perturbative/semiclassical, not exact at finite \(g\).
- The \(z'\) result is again first-step and initially uncorrelated only; no closed equation for later times is derived.
- S4 correctly refuses to call \(J_e\) a full \(T_{\mu\nu}\).

### 4. Certificate
The script checks:
- \(J^2=I\) on the two-site support;
- the Pauli rotation sign on \(J=\pm1\) sectors;
- the derivative of the declared \(z'-z\) formula;
- the one-dimensional current symbol \(2\sin q\) and its derivative.

It does **not** check:
- the full three-direction current symbol with all Pauli rows;
- the actual variational statement \(\partial H_m/\partial z=gJ\);
- the relation to the tetrad symbol beyond a one-dimensional check.

### 5. Scope
The report’s terminology “tetrad-conjugate stress source” is within its stated ceiling. “S5 = OPEN” is appropriate.

### Verdict: ACCEPT_WITH_REPAIRS

Mandatory repairs:
1. State plainly that \(\delta H_m=gzJ\) and \(\partial H_m/\partial z=gJ\) are leading-order semiclassical effective relations.
2. Add certificate checks for the variational derivative and for the full \(J_a(p)\) with \(a=1,2,3\), not only one scalar \(q\).
3. Clarify that the reciprocity is first-step/mean-field and not a closed dynamical equation after entanglement.

---

## W6: Full spatial tetrad gate

### 1. Contract compliance
F1–F6 are addressed. F2–F4 are directly proved; F1, F5, F6 are supported by construction/analogy from W4/W5 but not independently certified by the script.

### 2. Derivations
- \(D\) is invertible, so
  \[
  Z\mapsto \delta E=-2gZD
  \]
  has rank \(9\). Correct.
- The linearized spatial metric
  \[
  \delta h=E_0^T\delta E+\delta E^T E_0
  \]
  is \(B+B^T\) with \(B=E_0^T\delta E\). Since every symmetric \(3\times3\) matrix is \(B+B^T\) for some \(B\), the image has dimension \(6\). Correct.
- The kernel is
  \[
  B+B^T=0
  \iff
  B \text{ antisymmetric},
  \]
  so \(\dim\ker=3\). Equivalently,
  \[
  \delta E=\Omega E_0,\qquad \Omega^T=-\Omega.
  \]
  This is the expected linearized internal frame rotation. Correct.
- F1 holds by construction at \(g=\eta=0\), with \(K_\kappa\) acting only on geometry.
- F5 and F6 are componentwise specializations of W5 and W4.

### 3. Hidden assumptions
- The rank and kernel statements are linearized around flat \(E_0\).
- The kernel is a kinematic frame redundancy; the report correctly does not claim a proved local gauge symmetry.
- The existence of finite layering for all nine controls is plausible by bounded-degree local graph edge coloring, but the report gives only a sketch: “finitely many species labels” alone is not a rigorous schedule.
- F5/F6 are analogical; the script does not verify them.

### 4. Certificate
The script checks:
- rank of \(Z\to\delta E\) is \(9\);
- rank of \(Z\to\delta h\) is \(6\);
- kernel dimension is \(3\);
- the kernel is generated by antisymmetric frame directions.

It does **not** check:
- F1 exact CJWW recovery;
- F5 reciprocal source update;
- F6 autonomous propagation for all nine species.

### 5. Scope
The ceiling is respected: full spatial tetrad is not claimed to be full 3+1 gravity.

### Verdict: ACCEPT_WITH_REPAIRS

Mandatory repairs:
1. Certify or explicitly derive F1, F5, F6 rather than relying only on analogy.
2. Provide an explicit finite-depth coloring/level schedule for the nine-species overlapping gates.
3. Keep the strong label “kinematic frame redundancy” and avoid any suggestion that a gauge symmetry has been established.

---

## Final status table

| Claim | Status | Reason |
|---|---:|---|
| W3.1 exact CJWW recovery at \(g=0\) | SUPPORTED | All added gates become identity. |
| W3.2 local unitarity/finite interaction depth | SUPPORTED_WEAKER | Unitarity exact; depth bound inherited from W2, not independently certified. |
| W3.3 tetrad control \(E(z)\) | SUPPORTED_WEAKER | Consistent with current symbol but relies on mean-field \(Z\mapsto z\) and W2 transfer. |
| W3.4 matter changes \(z\) | SUPPORTED | Exact first-step formula for initially uncorrelated state. |
| W3.5 reciprocal closure | SUPPORTED_WEAKER | Algebra correct; uses mean-field reinsertion after entanglement. |
| W3.6 no false Einstein claim | SUPPORTED | Ceiling respected. |
| W4.1 unitarity/depth of \(K_\kappa\) | SUPPORTED_WEAKER | Unitarity exact; depth sketch not a rigorous schedule. |
| W4.2 homogeneous background fixed | SUPPORTED | Symmetric product state exactly fixed. |
| W4.3 local autonomous propagation | SUPPORTED | Exact \(|1,0\rangle\) computation. |
| W4.4 repeated finite-speed propagation | SUPPORTED | Locality and partial swaps give finite speed/spread. |
| W4.5 curvature linkage | SUPPORTED_WEAKER | Depends on external W3 curvature formula; not rechecked here. |
| W4.6 source remains separate | SUPPORTED | No stress-energy source claimed. |
| W5 S1 exact unitarity | SUPPORTED | Hermitian generator. |
| W5 S2 source changes tetrad control | SUPPORTED | Exact first-step formula with leading \(j_e\) term. |
| W5 S3 variational reciprocity | SUPPORTED_WEAKER | Only for leading-order semiclassical \(H_m\). |
| W5 S4 Weyl symbol/source interpretation | SUPPORTED | Symbol formula correct; “tetrad-conjugate” ceiling respected. |
| W5 S5 conservation/stress-energy open | SUPPORTED | Explicitly left OPEN. |
| W6 F1 exact flat recovery | SUPPORTED | By construction; not script-checked. |
| W6 F2 full tetrad rank 9 | SUPPORTED | \(D\) invertible; certificate checks rank. |
| W6 F3 full spatial metric rank 6 | SUPPORTED | Surjectivity onto symmetric matrices. |
| W6 F4 kernel dimension 3/frame rotations | SUPPORTED | Kernel is antisymmetric frame subspace. |
| W6 F5 reciprocal componentwise source | SUPPORTED_WEAKER | Follows from W5 analog but not independently certified. |
| W6 F6 autonomous propagation for nine species | SUPPORTED_WEAKER | Follows from W4 analog but not independently certified. |

### Gate verdicts
- **W3: ACCEPT_WITH_REPAIRS** — core formulas correct; mean-field/certification gaps remain.
- **W4: ACCEPT_WITH_REPAIRS** — local propagation exact; curvature-linkage claim is external and under-certified.
- **W5: ACCEPT_WITH_REPAIRS** — source repair is mathematically sound at leading order; effective-Hamiltonian language must be explicitly limited.
- **W6: ACCEPT_WITH_REPAIRS** — rank/kernel results are exact and well certified; F1/F5/F6 need explicit certification and a real finite-depth schedule.
