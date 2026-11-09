# Revisión sellada (casa xAI, grok-4.7) de la prueba de no saturación en el hexágono H25

Autorización explícita del usuario (2026-11-05): «pide la revisión sellada a
Grok para S25». Autoriza el envío a xAI (`grok-4.7`, vía `revision-ciega
grok`); no autoriza promover. Autor del resultado: Claude Code (Claude Opus
5.5). Base: `da49c00` (pushed). Herramienta: `~/herramientas` `ce09890`.
Generación de `grok-4.7` comprobada antes del envío (respuesta «OK»).
Una revisión, una ronda inicial y como máximo una re-revisión acotada de
reparaciones obligatorias. Hashes en `inputs.sha256`; los 13 documentos del
expediente del 2026-11-04 tienen los mismos hashes que entonces. Se adjuntan
todos los módulos que importa el verificador, directa o transitivamente, y el
chequeo geométrico suplementario `verify_hex_s25_review.py` (autor Codex) con
su salida. No se adjuntan revisiones ni dictámenes previos (intento Astra sin
dictamen; revisión local de Codex): la revisión es ciega respecto a ellos.

Comprobación previa. Sabido: contrato congelado 6eb50c1 antes de calcular;
verificador 14/14, 0 s de solver; resultado del autor PROVED_FOR_S25 por el
lema A1 (capas unitarias) y reducción a T2. Pregunta: ¿es correcta la cadena
completa y no afirma más de lo que prueba? Cierre: PASS → el usuario decide
promover; REPAIR_REQUIRED → se repara y, como mucho, una re-revisión; un
fallo de fondo devuelve el soporte H25 a OPEN. Un `tool_call_as_text` o un
fallo operativo no es revisión.

---
Revisa de forma adversarial e independiente la prueba de no saturación en el
hexágono H25, escrita por Claude (Anthropic): contrato
theory/PH_REFUTATION_HEX_S25_GATE.md, verificador
scripts/verify_ph_refutation_hex_s25_gate.py, informe
reports/2026-11-04--ph-refutation-hex-s25.md y la salida completa del
verificador. Se adjuntan los módulos importados (verify_hex_supremum_gate.py,
verify_hex_supremum_b19.py, verify_hex_ceiling_gate.py,
verify_c_across_lattices_gate.py), el informe de la etapa A de M1 (lema A1;
argumento de que T2 no depende de la red), el informe hex-ceiling (rigidez en
la recta de faceta, forma normal, T2), los contratos HEX_CEILING_GATE
(clase W_hex), HEX_SUPREMUM_GATE y el de la fase 0 (dominio de PH y
criterio de contraejemplo). Se adjunta también un chequeo geométrico
suplementario en aritmética entera, scripts/verify_hex_s25_review.py, escrito
por otro modelo (Codex, OpenAI), con su salida; tampoco es premisa. Nada de lo
escrito por Claude ni por Codex es premisa: rederiva. No tienes herramientas:
no ejecutes ni navegues y no afirmes haber ejecutado código. No propongas
ampliar la investigación ni otros soportes.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. SOPORTE. ¿Certifica el verificador que H25 (vértice 2 g1 + g2) tiene 25
   puntos, 6 vértices, ningún punto de red interior a una arista, y que H25′
   es su imagen por una simetría de la red? ¿Es correcto que los únicos
   hexágonos de red centrados dentro de H25 son S7, S13, S19, de modo que
   sólo conv F = H25 (o H25′) es nuevo? ¿Qué verificador comprueba cada una
   de estas afirmaciones, y queda alguna exigida por el contrato sin
   comprobar?
2. CAPAS Y LEMA A1. ¿Es correcta la rejilla δ = r_in/7 y la tabla de tamaños
   de capa? ¿Se sigue de la rigidez que cada capa intermedia suma 0 y, por
   tanto, que un coeficiente en capa unitaria es 0? ¿Cubren las capas
   unitarias exactamente los 18 puntos que no son origen ni vértice? ¿Es
   correcta la segunda vía (resolución exacta de las ecuaciones de capa) y su
   declaración de no independencia? ¿Afecta la simplificación de las
   normales (radicales explícitos) a la Parte 2?
3. REDUCCIÓN A T2. ¿Es lícito trasladar T2 a {0} ∪ vert(H25) mediante el
   giro espacial conjunto con un giro de Bloch alrededor de z que conserva
   A(n) = r n.σ? ¿Usa T2 sólo la geometría de los siete puntos, la
   unitariedad, el nodo y la isotropía (lee check_T2_minimal)? ¿Cubre T2
   cualquier walk s = 2 con F ⊆ {0} ∪ vert(H), sin forma de producto?
4. CONTROLES. ¿Son pertinentes los controles del cuadrado de M1-B19 y
   describe bien el informe su límite (A1 no tiene caso no trivial en el
   cuadrado)?
5. DICTÁMENES Y ALCANCE. ¿Son correctos PROVED_FOR_S25 (en W_hex^sym, luego
   en W_hex), NOT_REFUTED_ON_H25 y CONFIRMED_FOR_S25? ¿Respeta el informe que
   no es evidencia para (PH) fuera de H25 y que el patrón S13/H25 no se
   afirma? ¿Hay algún walk con conv F = H25 que el argumento no cubra?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente.
---
