Encargo de revisión ciega de W12 (rama `research/gravitational-normalization-gate`, `5485cb0`).
Lanzado con `revision-ciega <deepseek|opus> <esta carpeta> $(cat documentos.txt)`. Solo se envía el
texto entre las dos líneas `---`.
---
You are an independent referee in mathematical physics (quantum walks / quantum cellular automata,
lattice fermions, linearized gravity). You receive only the documents below; no web access, no
other context. Do not assume the documents are correct.

The documents are: the contract of an earlier gate (W6) that defines nine geometry controls acting
on a 3D two-component quantum walk; the contract of gate W12, frozen before any calculation; the W12
execution report; the W12 SymPy certificate; and the definition of the walk (CJWW Eq. (5.15)).

W12 asks whether the W6 controls induce the same first-order spatial metric perturbation at the
four zero-quasienergy Weyl nodes of the walk (species universality). The report concludes
UNIVERSAL_SUBFAMILY_DEFICIENT, which the contract classifies in advance as a negative result that
closes this line for the W6 control class.

Work in this order:

1. **Setting.** Check that the report follows the frozen contract (common coordinates, ranks on the
   coefficient of g, only the four +I nodes deciding, both product orders).
2. **Derivation.** Check the node frames E_*, the first-order expansion of the control symbol
   2 sin((p_* + k)·d_r) σ_a at each node, the induced δE_* and δh_*. Give the corrected
   expression for any error.
3. **Linear algebra.** Check dim U = 3, the basis of U, the rank 3/6 of the metric map on U, the
   three missing metric relations, and the absence of a common frame-rotation direction. Recompute
   them yourself if you can.
4. **Certificate.** Say what the script actually checks and whether it matches the report. Flag
   anything vacuous, circular or weaker than claimed.
5. **Robustness of the negative conclusion.** Within the contract's rules, could a convention
   choice (metric index placement, sign or ordering conventions, choice of reference node) change
   the verdict? Is comparing δh at the four nodes the right test of species universality at this
   order? Note anything that would make the negative result an artefact.
6. **Scope.** Is the claim ceiling respected? Is anything overclaimed or understated?

Output format: one section per point; a final table (claim / SUPPORTED, SUPPORTED_WEAKER or
NOT_SUPPORTED / one-line reason); a final verdict: ACCEPT, ACCEPT_WITH_REPAIRS (list mandatory
repairs) or REJECT. Be specific and brief; do not praise. Single round: state your assumptions
instead of asking questions.
---
Objetivo: revisión independiente del resultado negativo de W12 (autor Astra/GPT; contrato de
Claude). Resultado esperado: un informe por revisor. Máximo una ronda por revisor (DeepSeek, Opus).
Cierre: ambos informes recibidos o fallo documentado en `<modelo>.log`.
