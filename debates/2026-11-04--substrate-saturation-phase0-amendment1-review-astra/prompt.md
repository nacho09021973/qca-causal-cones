# Revisión independiente (casa OpenAI, gpt-6.1-sol) del borrador de la Enmienda 1 de la fase 0 (fila L4)

Autorización explícita del usuario (2026-11-04), respuesta a «¿a qué casa
lo mando?»: «a chat gtp 6.1 Sol». Autoriza el envío a OpenAI
(`gpt-6.1-sol`, vía `codex exec`, miembro astra); no autoriza aprobar la
enmienda ni promover nada. Autor del borrador: Claude (Anthropic). Base:
cecf75a (local). Herramienta: ce09890. Generación comprobada antes del
envío con una petición trivial («OK»). Una revisión, una ronda. Hashes en
`inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: la auditoría dejó
L4 sin clasificar; el addendum derivó desde CJWW las cláusulas del nodo y
DeepSeek lo dio por bueno dos veces; el usuario pidió una enmienda que
exija clase identificada y derivación revisada. Pregunta: ¿rebaja la regla
algún requisito del contrato congelado, y es correcta su aplicación a L4,
en particular la derivación del sustrato? Cierre: PASS → el usuario decide
si aprueba; REPAIR_REQUIRED → se repara; si la clase o el sustrato no se
sostienen, L4 sigue sin clasificar.

---
Revisa de forma adversarial e independiente el borrador
theory/SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md, escrito por Claude
(Anthropic). Se adjuntan: el contrato congelado de la fase 0, el informe de
la auditoría, el addendum sobre L4, el contrato congelado
C_ACROSS_LATTICES_GATE, el texto extraído de las pp. 16–17 del PDF de
Cedzich, Joye, Werner y Werner (arXiv:2408.02108v1, Ecs. (5.12)–(5.17)) y
extractos literales numerados de CURRENT_STATE, de dos verificadores, del
contrato DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE y de la tabla del
informe c-across-lattices. El borrador no es premisa. Las revisiones
previas de DeepSeek no se adjuntan: juzga desde las fuentes. No tienes
herramientas: no ejecutes ni navegues. No propongas ampliar la
investigación.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. REGLA (Sec. 1). ¿Rebaja algún requisito del contrato congelado (Secs.
   2.2, 2.4, 4, 5), o sólo añade una segunda fuente admisible para el
   nodo? ¿Basta la condición de clase para que «aparecer en una tabla» no
   cuente? ¿Es aceptable una revisión de una sola casa? ¿Es legítima una
   regla escrita después del resultado, tal como la acota la cabecera?
2. CLASE (Sec. 2.1). ¿Declara C_ACROSS_LATTICES_GATE l. 78 con su regla de
   admisión (l. 100–104) una «clase declarada» en el sentido de la Sec. 2.2
   de la fase 0, o sólo una fila? Si no basta, qué cita bastaría.
3. FUENTE Y NODO (Sec. 2.2). Con el texto de las pp. 16–17, ¿están bien
   transcritas (5.12) y (5.15)? Rehaz (i)–(v) para ambas con
   T_a = i ∂_a W(0). Comprueba también el signo de (5.13) frente a la parte
   escalar de (5.12) (verificador l. 81) y di si afecta a algo.
4. SUSTRATO (Sec. 2.4). Rehaz los soportes de Fourier de (5.12) y (5.15) y
   los grupos que generan. ¿Es (5.12) un walk sobre la red BCC y (5.15)
   sobre Z^3? ¿Es correcta la consecuencia para el recuento F3 de la
   auditoría y que la forma (cubo) no cambie? ¿Está bien registrada la
   inconsistencia con DISPERSION_CORRECTIONS (l. 63, 67), sin repararla?
5. EFECTO Y ALCANCE (Secs. 3–4). ¿Es correcto que sólo se reevalúe la
   salida definicional, que DEFINITIONS_CLOSED sólo sea posible si todo lo
   congelado se cumple, que los dos NO_COUNTEREXAMPLE_IN_SOURCE_TABLE, F1 y
   F2 no cambien, y que nada se presente como evidencia para (PH)?

Hasta 1800 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global
PASS, REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
