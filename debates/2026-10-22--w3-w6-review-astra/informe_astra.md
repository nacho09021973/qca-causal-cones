<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ d32e8507c32aefc0acd0721a000eeeb2a261d824; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 9b4a1d94214494e23afece076b33e017e142a7c79f1b026be0dcea2a1a9b1557; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.163.0)
inicio: 2026-10-22T08:31:02Z  fin: 2026-10-22T08:35:54Z
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
entrada_astra.txt sha256 1524ba64400b7f5111eb98a0179bf86650fae634a7bc74547bbcb27869089163
respuesta sha256 d7e32e599828e454e9ed19ac51be303007c1e6cedbbc30501d0ac0b818a589ea
-->

I assess the supplied formulas and code by inspection and independent algebra; I have not executed the certificates. Historical commits, reconstruction fidelity and reported execution results are **[UNVERIFIED]**.

## W3 — Backreacting tetrad control

**Compliance.** W3.1, W3.2 and W3.4 are established. W3.3 holds as a first-order background reduction. W3.5 establishes a contribution obtained by updating the mean control, but does not establish the complete quantum matter evolution at order \(g^2\). W3.6 and the exclusion of Einstein dynamics are respected.

**Derivation.** Since \(A^2=A\),
\[
R=I\otimes(I-A)+(\cos g\,I-i\sin g\,Y)\otimes A.
\]
Using \([Y,Z]=2iX\),
\[
R^\dagger ZR
=Z\otimes(I-A)+(Z\cos2g-X\sin2g)\otimes A.
\]
Consequently, for a product input,
\[
\Delta z=a[(\cos2g-1)z-\sin2g\,x]
=-2gxa-2g^2za+O(g^3).
\]
The sign and leading term in the report are correct. For a correlated input, the exact replacement is
\[
\Delta z=(\cos2g-1)\langle Z\otimes A\rangle
-\sin2g\langle X\otimes A\rangle.
\]
Thus the product formula cannot automatically be iterated. Also, \(T^\dagger ZT=Z\), so the subsequent transport gate preserves the updated expectation exactly.

The supplied walk gives
\[
W(p)=I+i(p_1\sigma_1-p_2\sigma_2+p_3\sigma_3)+O(p^2),
\]
confirming \(E_0=\operatorname{diag}(1,-1,1)\) under \(H=-\sigma^aE_a{}^ip_i\). With the Fourier convention used in W5, the current correction gives
\[
E=E_0-2g\,\operatorname{diag}(z_a)D+O(g^2).
\]
Substituting \(\Delta z_a=-2gx_aa_a+O(g^2)\) into its **displayed linear term** gives
\[
\boxed{\Delta E_{\mathrm{mean}}
=4g^2\operatorname{diag}(x_aa_a)D+O(g^3).}
\]

However, an unspecified \(O(g^2)\) remainder does not by itself justify an \(O(g^3)\) remainder in the difference. That conclusion requires a smooth, state-independent background expansion whose remainder changes only through \(\Delta z=O(g)\).

More seriously, the kick creates correlations at precisely the relevant order. For the product input \(\rho_g\otimes\rho_m\),
\[
\operatorname{Tr}_g(ZR\rho R^\dagger)
=z\rho_m-gx\{A,\rho_m\}+O(g^2).
\]
For the declared \(y=0\) input, this generally differs from \(z'\rho_m'\) already at \(O(g)\). The following transport therefore receives correlation corrections at \(O(g^2)\), the same order as the claimed backreaction coefficient.

**Certificate.** It checks the occupied-sector rotation, differentiates an assumed expectation formula, verifies \(\det D=1\), and performs the substitution producing \(4g^2\). Its “transport tetrad” check only defines \(E\) and checks \(E(0)=E_0\); it does **not** derive the transport symbol. It does not check a reduced quantum channel, the remainder estimate or layering.

The twelve interaction layers are defensible: all three directions have first component one, so parity of the starting \(x_1\) supplies two matchings per family, with separate kick and transport layers. This is not a finite-depth synthesis of \(U_0\), as the report correctly acknowledges.

**Verdict: ACCEPT_WITH_REPAIRS.**

1. Label \(\Delta E_{\rm back}\) as the induced **mean-field contribution**, not the complete order-\(g^2\) reduced matter principal symbol.
2. State the factorization and remainder assumptions needed for repeated reciprocal closure; otherwise leave that stronger closure open.
3. Correct the certificate’s description of what it verifies.

## W4 — Autonomous geometry dynamics

**Compliance.** W4.1–W4.3 are established. W4.4 has a valid full-SWAP witness, although its generic-amplitude argument is incomplete. W4.5 supports a lattice curvature diagnostic; the supplied sharp defect does not itself establish a controlled coarse-field limit. W4.6 and the gravitational claim ceiling are respected.

**Derivation.** The identities
\[
S=\tfrac12(I+XX+YY+ZZ),\qquad
K=e^{-i\kappa}(\cos\kappa\,I+i\sin\kappa\,S)
\]
follow from \(S^2=I\). Every identical pure product pair is symmetric, so \(K|n,n\rangle=|n,n\rangle\) exactly. The homogeneous product is therefore fixed by every layer.

For the defect,
\[
K|1,0\rangle=e^{-i\kappa}
(\cos\kappa|1,0\rangle+i\sin\kappa|0,1\rangle),
\]
giving
\[
\langle Z_e\rangle=-\cos2\kappa,\qquad
\langle Z_f\rangle=\cos2\kappa.
\]
At \(\kappa=\pi/2\), \(K=S\) exactly. At \(\kappa\in\pi\mathbb Z\), \(K=I\); propagation must exclude these values.

Six nearest-neighbor matching layers give a strict support bound of six geometry bonds per tick. For a specified schedule with even bonds followed by odd bonds, a full-SWAP defect initially on an even site advances two sites per two-layer cycle. This proves arbitrarily long propagation. Merely exhibiting nonzero factors along paths does not prove nonzero summed amplitudes: interference must be addressed for the broader partial-SWAP assertion.

**Curvature convention and witness.** The cone supplies the **contravariant** spatial metric
\[
h^{ij}=(E^TE)^{ij}.
\]
For \(z_1=f(x_2)\), its perturbation is \(q^{11}=-4gf\). The corresponding covariant perturbation is \(k_{11}=+4gf\), hence
\[
R^{(1)}=\partial_i\partial_jk_{ij}-\partial^2k_{ii}
=-4gf''.
\]
The reported sign is correct with this convention. If \(E^TE\) were instead called the covariant metric, the sign would reverse.

Writing \(c=\cos2\kappa\), the defect calculation gives
\[
\Delta_2z_0=1+3c,\qquad \Delta_2z_1=1-3c.
\]
Initially these are \(4,-2\); at full SWAP they become \(-2,4\), and the entire second-difference pattern translates. This is a correct lattice witness.

Two qualifications matter:

- The formula \(f(x_2)\) describes a plane-invariant texture, not an arbitrary isolated three-dimensional link defect. Replication in the transverse directions supplies the stated geometry.
- A one-link discontinuity is not slowly varying. It proves transport of a discrete diagnostic. A smooth, long-wavelength texture or an explicit smoothing prescription is needed for a controlled coarse-curvature statement.

Moreover, partial SWAP generally creates correlations, so \(z_e\) alone does not obey a closed autonomous evolution law. The **geometry subsystem** evolves autonomously. “Vacuum” here means the geometry-only evolution with matter interactions omitted; a zero-particle sector has not been supplied.

**Certificate.** It checks SWAP algebra, the derivative of the proposed \(K\) at zero, symmetry of identical product pairs, two-site expectations and complete transfer. A derivative at zero alone does not certify the full exponential, though the already checked \(S^2=I\) proves it analytically. The script does not check repeated propagation, curvature or coarse graining.

**Verdict: ACCEPT_WITH_REPAIRS.**

1. Specify the repeated matching schedule and either restrict the propagation proof to its full-SWAP witness or supply an interference-aware proof.
2. State the inverse-metric convention and distinguish the discrete witness from controlled coarse curvature.
3. Replace “autonomous propagation law” for \(z\) by autonomous geometry evolution unless a closure is derived.

## W5-source — Tetrad-conjugate source

**Compliance.** S1 and S2 hold exactly under the stated input condition. S3 and S4 hold for the transport generator and its long-wavelength interpretation, with qualifications about “Hamiltonian” and “stress.” The terminal state correctly leaves stress-energy conservation open.

**Derivation.** On the endpoint subspace, the position current is a Pauli \(Y\); outside it, it vanishes. Thus
\[
J^2=A,\qquad J^3=J,\qquad \operatorname{spec}J\subset\{-1,0,1\}.
\]
Functional calculus gives
\[
\cos(2\eta J)=I+(\cos2\eta-1)A,\qquad
\sin(2\eta J)=\sin2\eta\,J.
\]
Therefore
\[
R^\dagger ZR
=Z\otimes[I+(\cos2\eta-1)A]-X\otimes\sin2\eta\,J,
\]
and for a product input,
\[
\boxed{\Delta z
=-2\eta xj-2\eta^2za+\frac43\eta^3xj+O(\eta^4).}
\]
The report is correct. For correlated inputs, replace \(za\) and \(xj\) by \(\langle ZA\rangle\) and \(\langle XJ\rangle\). A nonzero linear response requires \(xj\ne0\).

For the classical-background transport substep,
\[
H_{\rm kick}=gzJ,\qquad \partial_zH_{\rm kick}=gJ
\]
in units where its duration is one. For \(\psi(x)=e^{ip\cdot x}u\), the forward translation acts by \(e^{-ip\cdot d}\), so
\[
J_a(p)=i(e^{-ip\cdot d_a}-e^{ip\cdot d_a})\sigma_a
=2\sin(p\cdot d_a)\sigma_a
=2d_a{}^ip_i\sigma_a+O(|p|^3).
\]
The sign and factor two are correct. Independently, the chain rule gives
\[
\frac{\partial H}{\partial E_a{}^i}=-\sigma^ap_i,\qquad
\frac{\partial E_a{}^i}{\partial z_a}=-2gD_a{}^i,
\]
recovering the same directional source.

**Hidden assumptions and scope.** The generator of an inserted kick is not generally the additive correction to the logarithm of the full Floquet step. With \(U=e^{-igV}e^{-iH_0}\), commutator corrections can already be first order in \(g\). For a homogeneous long-wavelength reduction here, \(V(p)\) and \(H_0(p)\) are both \(O(p)\), so their first commutator is \(O(gp^2)\): the stated principal-symbol relation survives at order \(gp\). This does not justify the same assertion for a general inhomogeneous effective Hamiltonian.

“Tetrad-conjugate stress source” is defensible only as a qualified name for this directional variational operator. No action-based stress tensor, conserved local stress, or variational derivation of the geometry evolution follows. The independent parameters \(g,\eta\) and the imposed \(Y\)-kick establish matching operators, not a gravitational field equation. The kick also contributes a matter generator \(\eta\langle Y\rangle J\); its absence requires the declared initial \(y=0\) condition and need not persist.

**Certificate.** It checks \(J^2=I\) on the endpoint sector for one Pauli choice, rotations for eigenvalues \(\pm1\), the slope of an assigned expectation formula, and the Fourier identity and slope. The zero sector is handled by reasoning, not explicitly tested. It does not check the variational reduction, the quadratic expectation term, or stress interpretation. The imported `PAULI` implementation is absent, so standalone execution is **[UNVERIFIED]**. The supplied equality helper addresses expression normalization, not these evidential gaps.

**Verdict: ACCEPT_WITH_REPAIRS.**

1. Identify \(gzJ\) explicitly as the background transport-kick generator; qualify its extension to a full effective Hamiltonian.
2. Limit reciprocity and “stress source” to the demonstrated directional variational relation.
3. State the factorization and \(y=0\) restrictions and narrow the certificate’s concluding claim.

## W6 — Full spatial tetrad rank

**Compliance.** F2–F4 are proved for nonzero \(g\). F5 inherits W5’s qualifications. F1’s matter-recovery statement holds, but its displayed full-unitary identity omits retained geometry dynamics. F6 needs an explicit distinction between turning off transport and turning off all matter–geometry coupling.

**Derivation.** For \(g\ne0\),
\[
\delta E=-2gZD,\qquad
Z=-\frac1{2g}\delta E\,D^{-1}.
\]
Thus the tetrad map has rank nine. At \(g=0\), this map has rank zero.

Since \(E_0^TE_0=I\), every symmetric target \(S\) is obtained by choosing
\[
\delta E=\tfrac12E_0S,
\]
which gives \(\delta h=S\). Hence the metric map has rank six.

Writing \(A=E_0^T\delta E\), its kernel satisfies
\[
A+A^T=0,\qquad \delta E=E_0A.
\]
There are three independent antisymmetric components. With
\[
\Omega=E_0AE_0,
\]
one has \(\Omega^T=-\Omega\) and \(\delta E=\Omega E_0\). This is exactly the tangent to internal spatial frame rotations. In control coordinates,
\[
Z_{\ker}=-\frac1{2g}E_0AD^{-1}.
\]
The interpretation as a metric-map redundancy, rather than a microscopic gauge symmetry, is correct.

The full-rank conclusion is local: physical controls satisfy \(|z_{ar}|\le1\). An interior background permits all sufficiently small variations; it does not permit arbitrary finite tetrads at fixed \(g\). Rank also says nothing about dynamically reachable states or physical mode counts.

**Recovery correction.** If W4 exchange is retained,
\[
\boxed{U_{g=0,\eta=0;\kappa}=K_\kappa\otimes U_0,}
\]
not \(I_g\otimes U_0\), unless \(K_\kappa=I\). Matter nevertheless evolves exactly by \(U_0\). Furthermore, \(g=0\) alone does not recover the free matter walk when \(\eta\ne0\): the source kick still couples matter and geometry. Taken literally, F6’s “flat \(g=0\)” wording needs this correction.

Finite interaction depth remains straightforward: serialize the nine matter-coupled species, each with two matchings and two substeps, giving at most 36 interaction layers. Geometry exchange needs six additional layers with species parallelized. None of this synthesizes \(U_0\).

**Certificate.** This is a substantive rank certificate: it computes the two Jacobian ranks, nullity, and the rotation parametrization. Its explicit nonzero assumption on \(g\) is essential. It does not derive the principal-symbol map or check F1, F5, F6, physical control constraints or gauge invariance.

**Verdict: ACCEPT_WITH_REPAIRS.**

1. State \(g\ne0\), an interior control background, and infinitesimal scope.
2. Correct the full recovery identity and require \(\eta=0\) for free matter recovery.
3. Carry forward W5’s reduction assumptions; distinguish rank completeness from dynamics and gauge symmetry.

## Final assessment

| Claim | Status | Reason |
|---|---|---|
| W3 exact \(Z\) update | SUPPORTED | Projector decomposition and Pauli algebra give the stated formula. |
| W3 first-order background tetrad | SUPPORTED | Follows from the supplied walk and summed current symbol. |
| W3 complete \(O(g^2)\) quantum backreaction coefficient | NOT_SUPPORTED | Correlations contribute at the same order; the certificate checks substitution only. |
| W3 induced mean-field backreaction | SUPPORTED_WEAKER | Correct coefficient under an explicitly maintained background reduction. |
| W4 local exchange and homogeneous fixed state | SUPPORTED | Exact SWAP algebra. |
| W4 unbounded-distance, finite-speed transport | SUPPORTED | A scheduled full-SWAP brickwork provides a witness. |
| W4 coarse-curvature propagation | SUPPORTED_WEAKER | Discrete diagnostic transport is proved; controlled coarse graining is absent. |
| W5 exact current-driven \(Z\) response | SUPPORTED | Functional calculus gives the stated product-input update. |
| W5 tetrad-conjugate source | SUPPORTED_WEAKER | Valid for the transport generator and directional continuum variation. |
| W5 conserved stress-energy source | NOT_SUPPORTED | No required conservation or symmetry identity; correctly left open. |
| W6 ranks \(9,6\) and three rotation directions | SUPPORTED | Exact linear algebra for nonzero \(g\). |
| W6 displayed full-unitary flat recovery | NOT_SUPPORTED | Retained exchange leaves \(K_\kappa\), while nonzero \(\eta\) still couples matter. |
| Full-step finite-depth QCA synthesis or gravity | NOT_SUPPORTED | The supplied results establish neither; their main claim ceilings correctly exclude them. |