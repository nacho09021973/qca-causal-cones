Encargo de revisión ciega de W9–W11 (rama `research/gravitational-normalization-gate`,
`41d0e0d`). Lanzado con `revision-ciega <deepseek|opus> <esta carpeta> <documentos>` (ver
`README.md` de esta carpeta). Solo se envía el texto entre las dos líneas `---`.
---
You are an independent referee in mathematical physics (quantum walks / quantum cellular automata,
linearized gravity, lattice gauge theory). You receive only the documents below. You have no web
access and no other context. Do not assume the documents are correct.

The documents are a sequence of three "gates" (W9, W10, W11) of a research project. Each gate has a
contract, frozen before the work, and an execution report with a verdict. There is also a
prior-art audit and two SymPy certificate scripts. Context: the frozen matter model is a 3D
two-component discrete-time quantum walk (CJWW Eq. (5.15)); its definition is attached.

Work in this order:

1. **What is claimed.** Before judging, state in your own words what each of W9, W10 and W11
   claims to establish, and what it explicitly says it does not establish.
2. **Derivations.** Check each derivation step by step: signs, factors, index placement,
   integrations by parts, the use of the conservation law, the Fourier symbols, the first-order
   expansion of W(p) at p = 0 and the resulting effective Hamiltonian, and the claimed order of
   the mismatch between H_eff and H_IR. For each error, give a concrete counterexample or the
   corrected expression.
3. **Verdicts versus evidence.** For each sub-verdict (W9 B1–B4, W10 C1–C4, W11 F1–F4), say whether
   the evidence in the report supports it as stated, supports only a weaker statement (give it),
   or does not support it. Check especially whether a verdict marked PASS relies on something
   the same report marks as open, assumed or schematic.
4. **Certificates.** For each script, say what it actually checks and whether that is what the
   report says it certifies. Point out any check that is vacuous, circular or weaker than claimed.
5. **Prior art.** The documents attribute specific results to Gu and Wen (arXiv:0907.1203) and to
   Pretko. You cannot consult them. Say which attributions you can confirm from memory, which you
   cannot, and which look doubtful. Mark everything from memory as [UNVERIFIED].
6. **Missing steps.** List the steps that are missing before the chain
   "exact walk -> Weyl IR -> IR stress tensor -> sourced linearized constraints" could be
   called established at the stated level.

Output format:
- One section per point above.
- A final table: gate / sub-verdict / your assessment (SUPPORTED, SUPPORTED_WEAKER,
  NOT_SUPPORTED) / reason in one line.
- A final overall verdict per gate: ACCEPT, ACCEPT_WITH_REPAIRS (list the mandatory repairs) or
  REJECT.

Be specific and brief. Do not praise. If something is correct, say so in one line and move on.
This is a single round: do not ask questions back; state your assumptions instead.
---
Objetivo: revisión independiente (familias distintas del autor, GPT/Astra) de W9–W11.
Resultado esperado: un informe por revisor con veredicto por puerta y reparaciones.
Máximo: una ronda por revisor (DeepSeek, Opus). Cierre: ambos informes recibidos, o fallo
documentado en `<modelo>.log`. Opus es Claude: independiente del autor, no de Claude Code.
