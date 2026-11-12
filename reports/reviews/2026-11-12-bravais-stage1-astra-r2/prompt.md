# Codex re-review: repaired Bravais Stage 1 and Amendment 5

User authorization (2026-11-12, «adelante», answering the proposal to send
the repaired Stage 1 and Amendment 5 back to Codex): second sealed round by
GPT-6 Astra (OpenAI, `codex exec`), a family different from the author's.
`revision-ciega astra`; herramientas `7d111a1`. Base commit `755f2ba`.

Candidates:
- `reports/2026-11-12--general-ir-rate-bravais-stage1.md`, SHA256
  `0b48e5b01faa1f3b3f81051ef529c23c6a938e5ddde0e57b865e48859b37678a`
  (repairs at `6516892`);
- `theory/GENERAL_IR_RATE_GATE_AMENDMENT_5.md`, SHA256
  `bfe04c51b388f17c9ec2195de7b28f74eb1c021019e2d576d48df956b3e14c84`
  (approved at `755f2ba`).

Attached also: the first-round report (copy `informe_astra_ronda1.md` here, with the provenance header removed because it contains local paths; reviewer text unchanged,
the objections to check), the Bravais charter, the general-rate charter,
the three B1 stage reports, the anonymised carrier Stage A copy from the
first round and the anonymised manuscript. The author's reading of the
first round is not attached.

Objective: decide whether the repairs answer the four objections and
whether Amendment 5 correctly repairs H2 without changing any proof.
Expected result: verdict with located objections. Maximum rounds: one.
Closes with: the written report. No automatic loop, no promotion.

---
Revisa adversarialmente, en segunda ronda, unas reparaciones. No tienes
herramientas, repositorio ni web; trabaja solo con los documentos
adjuntos. No presupongas que sean correctos.

En la primera ronda (documento `informe_astra_ronda1.md`, adjunto) un revisor dio
REPAIR_REQUIRED al informe `2026-11-12--general-ir-rate-bravais-stage1.md`
(«Etapa 1») con cuatro objeciones, y señaló aparte que la hipótesis H2 del
contrato `GENERAL_IR_RATE_GATE.md` no da, tal como está escrita, la
positividad de `Q = Hess_xi log|lambda_0|` que usan las pruebas. El autor
ha reparado la Etapa 1 (sección final «Repairs after the Codex review») y
ha escrito la enmienda `GENERAL_IR_RATE_GATE_AMENDMENT_5.md` (H2′).

Juzga:
1. Si cada una de las cuatro objeciones queda resuelta por el texto actual
   de la Etapa 1 (U15; U6 con la celda de Voronoi; §6.1; alcance del
   inventario y §7), y si las reparaciones introducen algún error nuevo o
   afirman algo que no se prueba.
2. Si el inventario U1–U15 es ahora completo para las demostraciones
   generales de los documentos adjuntos.
3. Enmienda 5: si H2′ es la hipótesis que usan realmente las pruebas
   (etapa 0(i), §3.1 del progreso de la etapa 2, §5 del término
   principal, §§1 y 4 de la etapa A de portadores); si la identidad
   `Hess_xi log|lambda| = -Hess_eta log|lambda|` por pluriarmonicidad está
   bien usada; si `Q > 0` implica la no degeneración de la Hessiana
   compleja; si es cierto que ninguna prueba cambia; si el caso del
   manuscrito cumple H2′; y si queda algún otro uso de H2 que necesite
   algo distinto.
4. Que nada afirme más de lo que prueba.

Salida: dictamen PASS / REPAIR_REQUIRED / REJECTED para la Etapa 1
reparada y, por separado, para la enmienda 5. Para cada objeción de la
primera ronda: RESUELTA / NO_RESUELTA / PARCIAL, con la razón. Objeciones
nuevas con documento y sección, tipo (error fatal, reparación necesaria,
hipótesis que falta, exposición) y derivación cuando sea decisiva. Si no
puedes verificar un paso, márcalo NO_VERIFICADO.

Presupuesto: una ronda. Cierre: informe escrito con dictamen.
---
