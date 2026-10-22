# Revisión independiente de W3–W6 (texto reconstruido)

Fecha: 2026-10-22. Autorización del usuario: «adelante con 2 y 3, autorizado» (revisión independiente de lo PRELIMINARY) y «adelante» (reconstrucción, y después revisión de W3–W6).
Objetivo: comprobar si las derivaciones de W3, W4, W5 (fuente tetrad-conjugada) y W6 son correctas y respetan sus contratos congelados, y si los certificados comprueban lo que los informes dicen.
Resultado esperado: tabla por afirmación (SUPPORTED, SUPPORTED_WEAKER o NOT_SUPPORTED) y veredicto por gate (ACCEPT, ACCEPT_WITH_REPAIRS o REJECT), con reparaciones obligatorias.
Máximo: una ronda sellada y un reintento operativo. Revisor: deepseek (familia distinta de Claude; los textos de 2026-09-30 tienen autoría de agente no identificado y la reconstrucción tipográfica es de Claude).
Cierre: informe y lectura crítica del autor en `verificacion_autor.md`. No promociona nada por sí misma.
Documentos: contratos y informes de W3–W6 reconstruidos (certificado: `check_reconstruction.py`), los cuatro certificados SymPy y la definición CJWW (5.15).
Herramienta: revision-ciega del PATH; ~/herramientas `d32e850`.

---
You are an independent referee in mathematical physics (quantum walks / QCA, lattice fermions, linearized gravity). You receive only the documents below; no web, no other context. Do not assume they are correct. Answer in English or Spanish.

The documents are four consecutive gates (W3, W4, W5-source, W6) of a toy "dynamical geometry" construction coupled to a 3D two-component quantum walk (CJWW Eq. 5.15): for each gate the contract frozen before calculation, the execution report and its exact SymPy certificate. The LaTeX of the contracts and reports was typographically reconstructed after an encoding accident; each carries a note saying so. Judge the mathematics, not the typography.

For each gate:
1. **Contract compliance.** Does the report address every obligation as frozen, without moving the goalposts?
2. **Derivations.** Re-derive the key steps: W3 Heisenberg update of Z under exp(-ig Y⊗A) with A²=A, z'-z, and the O(g²) backreaction δE; W4 SWAP identities, fixed homogeneous product state, the |1,0⟩ propagation and the discrete-curvature witness; W5 the identities for cos(2ηJ), sin(2ηJ) with J²=A, J³=J, the exact z' and its expansion, the variational relation ∂H_m/∂z=gJ and the symbol 2 sin(p·d)σ; W6 ranks 9 and 6, kernel dimension 3 and its identification with linearized frame rotations. Give corrected expressions for any error.
3. **Hidden assumptions.** Flag where a step uses an uncontrolled approximation: semiclassical/mean-field replacement of Z by ⟨Z⟩, "initially uncorrelated" states, the passage from a per-tick unitary to an effective Hamiltonian δH_m=g z J, finite-depth claims for the full step, and whether "tetrad-conjugate stress source" and "curvature propagation" are justified at the stated level.
4. **Certificates.** Say exactly what each script checks and whether that matches the report. Flag anything vacuous, circular or weaker than claimed (for instance, a script asserting a formula it defines rather than deriving it).
5. **Scope.** Is each claim ceiling respected? Anything overclaimed or understated?

Output: one section per gate; a final table (claim / SUPPORTED, SUPPORTED_WEAKER or NOT_SUPPORTED / one-line reason); a verdict per gate: ACCEPT, ACCEPT_WITH_REPAIRS (numbered mandatory repairs) or REJECT. Be specific and brief; single round; state assumptions instead of asking.
---
