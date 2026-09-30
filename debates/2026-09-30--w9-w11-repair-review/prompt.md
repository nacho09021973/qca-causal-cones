Encargo de revisión ciega, segunda ronda: reparaciones de W9–W11 (rama
`research/gravitational-normalization-gate`, `86fe771`). Lanzado con
`revision-ciega <deepseek|opus> <esta carpeta> $(cat documentos.txt)`. Solo se envía el texto entre
las dos líneas `---`. Revisión desde cero: el revisor no recibe los informes de la primera ronda.
---
You are an independent referee in mathematical physics (quantum walks / quantum cellular automata,
linearized gravity). You receive only the documents below; no web access, no other context. Do not
assume the documents are correct.

The documents are three research "gates" (W9, W10, W11): for each, a contract frozen before the
work and an execution report. Each report has an original part and a later "Repair addendum"
(Section 9 or similar) written after an earlier review; the addendum states that it supersedes the
original verdict. Three SymPy certificate scripts and the definition of the underlying 3D
two-component quantum walk (CJWW Eq. (5.15)) are attached.

Focus on the repair addenda and the current certificates. Work in this order:

1. **What is now claimed.** For W9, W10 and W11, state the current verdict and what each explicitly
   does not claim.
2. **W11 node table.** Check that the eight points p_i in {0, pi} are exactly the points where
   W = +-I, and check each frame E_* and chirality sign in the table.
3. **W11 energy charge K = i(U - U^dagger)/2.** Check: hermiticity and [K, U] = 0; the real-space
   hopping matrices and the local density; the band bound ||(K - H_eff) P_Lambda|| <= (arcsin
   Lambda)^3 / 6, including the claims sin^2(theta) <= |k|^2 and K = sin(H_eff) on the branch; the
   dynamical bound ||(U^n - e^{-inK}) P_Lambda|| <= |n| (arcsin Lambda)^3 / 6; and the bound
   ||K - H_IR|| <= Lambda^3. Give a counterexample or a corrected constant for any error.
4. **W11 F3 obstruction.** Check the proof that no continuous periodic Hermitian H(p) with
   e^{-iH(p)} = W(p) exists (constant trace in 2 pi Z; H(p_*) scalar at each node; parity
   mismatch between +I and -I nodes). Is every step valid? Is the stated scope (continuous,
   translation-invariant logarithms; not all QCAs) correct?
5. **W10.** Check the explicit quadratic action, signature and normalization, and the claimed
   relation G^{mu nu} = lambda T^{mu nu} / 2 with the lapse/shift factors, against the W10
   certificate. Is the new verdict OPEN_AFTER_AUDIT consistent with the evidence?
6. **W9.** Check the repaired certificate (explicit h, xi, symmetric T, factor 1/2, integration by
   parts, static residual gauge) and whether the remaining PASS is stated at the right scope.
7. **Certificates.** For each script, say what it actually checks and whether that matches what
   the report says. Flag anything vacuous, circular or weaker than claimed.
8. **Consistency of the downgrades.** Does any remaining PASS rely on something the same report
   marks as open? Is anything overclaimed or, conversely, understated?

Output format: one section per point; a final table (gate / claim / SUPPORTED, SUPPORTED_WEAKER or
NOT_SUPPORTED / one-line reason); a final verdict per gate: ACCEPT, ACCEPT_WITH_REPAIRS (list
mandatory repairs) or REJECT. Be specific and brief; do not praise. Single round: state your
assumptions instead of asking questions.
---
Objetivo: revisión independiente de las reparaciones de W9–W11 (autor Astra/GPT), sobre todo la
prueba de F3 y las cotas de K, que el autor marca como no revisadas.
Resultado esperado: un informe por revisor. Máximo una ronda por revisor (DeepSeek, Opus).
Cierre: ambos informes recibidos o fallo documentado en `<modelo>.log`.
