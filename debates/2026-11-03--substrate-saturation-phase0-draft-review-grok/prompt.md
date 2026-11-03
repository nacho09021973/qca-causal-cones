# Revisión independiente (casa Grok) del borrador de carta SUBSTRATE_SATURATION, fase 0

Autorización explícita del usuario (2026-11-03): «que lo revise grok», sobre
el borrador `theory/SUBSTRATE_SATURATION_PHASE0_GATE.md`, redactado a su
instrucción («Autorizo redactar la carta de la fase 0, pero no congelarla ni
ejecutar todavía ninguna comprobación»). Autoriza el envío externo a xAI
(Grok); no autoriza congelar, ejecutar ni promocionar. Autor: Claude
(Anthropic). Base: 1afc164 (publicado) más el borrador sin commit (hash en
`inputs.sha256`). Herramienta: ce09890. Una revisión, una ronda.

Comprobación previa (regla de los tres puntos). Sabido: el borrador
incorpora las cuatro precisiones del usuario (cuantificadores, dominio,
normalización, criterio de fracaso) y la distinción hueco puntual/uniforme.
Pregunta: ¿está bien planteada la carta, de modo que su veredicto no pueda
leerse como más de lo que prueba? Cierre: PASS → el usuario decide si la
congela; REPAIR_REQUIRED → se repara el borrador y el usuario decide; si la
conjetura resulta mal definida en su forma actual, se reformula antes de
congelar.

---
Revisa de forma adversarial e independiente el borrador de contrato
SUBSTRATE_SATURATION_PHASE0_GATE.md, escrito por Claude (Anthropic). Se
adjuntan como contexto, ya revisados y promocionados, la síntesis sobre c
en distintos sustratos, el informe c-across-lattices con la tabla de filas,
su contrato y el contrato M1 del hexágono. El borrador no es premisa: es el
objeto de la revisión. No tienes herramientas: no ejecutes, edites ni
navegues. La fase 0 es solo documental: no pidas cálculos.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. CONJETURA. ¿Está bien definida (PS) «el techo c_0 = r_in(C_micro) se
   alcanza si y solo si C_micro es un paralelotopo» con s = 2, d ≤ 3? ¿Es
   «paralelotopo» la noción geométrica adecuada, o lo es otra (zonotopo,
   cubo/cuadrado regular, simetría bajo la isotropía exigida)? En
   particular: ¿tiene sentido PS⇐ para paralelotopos sin la simetría que
   exige un cono isótropo en el nodo (por ejemplo un rombo de 60° en d = 2)?
   ¿Hay ya en los documentos adjuntos un dato que la contradiga?
2. CUANTIFICADORES Y DOMINIO. ¿Están bien separados el existencial
   (existe un walk que satura) y el universal (ninguno satura)? ¿Está bien
   excluido todo lo que tiene s ≠ 2? ¿«Sustrato» queda definido sin
   ambigüedad (grupo de traslaciones y N compuesto)?
3. NORMALIZACIÓN. ¿Garantizan las definiciones congeladas (C_micro =
   conv N, r_in = min h_C, c_0 del cono isótropo sin inclinación, unidades
   de paso más largo 1) que todas las filas se comparan igual? ¿Falta algo
   (por ejemplo, el tratamiento del cero en N, o filas cuya c_0 viene de
   otro contrato con otra normalización, como L4 reescalado)?
4. CRITERIO DE FRACASO Y VEREDICTOS. ¿Es correcto que un solo
   contraejemplo exacto refute, que NOT_REFUTED_IN_EXISTING_ROWS sea el
   máximo, y que OUTSIDE_DEFINITIONS no cuente ni a favor ni en contra?
   ¿Distingue bien la carta hueco puntual y hueco uniforme?
5. UTILIDAD Y SESGO. Con cuatro sustratos paralelotopo y uno no
   paralelotopo, elegidos antes para otras preguntas, ¿qué información
   real puede dar la fase 0? ¿Hay riesgo de leer un NOT_REFUTED como
   apoyo? ¿Qué cambiarías para que la fase 0 pueda fallar de verdad?

Hasta 1500 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente.
---
