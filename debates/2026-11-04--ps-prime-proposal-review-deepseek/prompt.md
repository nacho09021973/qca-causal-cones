# Revisión sellada (casa DeepSeek) de la propuesta documental sobre PS′

Autorización explícita del usuario (2026-11-04): «si a las 3», en respuesta a
la oferta de una revisión sellada con DeepSeek o Grok. Se elige DeepSeek
(casa usada en la revisión de L3). Autor del candidato: Codex (OpenAI), con
dos aclaraciones insertadas por Claude (Anthropic). Base: 0d85366 (local).
Herramienta: ce09890. Modelo: deepseek-v4-pro (comprobar generación antes del
envío). Una revisión, una ronda. Hashes en `inputs.sha256`. La revisión de
Claude (`debates/2026-11-04--ps-prime-proposal-review-claude/`) no se adjunta,
para que esta sea ciega.

Comprobación previa. Sabido: la propuesta recomienda no usar el recuento de
generadores reducidos como criterio intrínseco de saturación sin una regla de
presentación, apoyándose en L6e (JDW Eq. (6)). El usuario ha adoptado la
recomendación como decisión del proyecto. Pregunta: ¿se sostienen los hechos y
la lógica de la propuesta frente a un revisor de otra familia? Cierre: PASS →
se registra la adopción con este dictamen; REPAIR_REQUIRED → se repara antes de
registrarla; un fallo de fondo vuelve a dejar la decisión al usuario.

---
Revisa de forma adversarial e independiente el informe
reports/2026-11-04--ps-prime-intrinsic-definition-proposal.md (propuesta
documental, escrita por Codex de OpenAI con dos aclaraciones insertadas por
Claude de Anthropic). Se adjuntan: la propuesta, el contrato congelado de la
fase 0 (theory/SUBSTRATE_SATURATION_PHASE0_GATE.md; PS′ en su Sec. 1, los
cuantificadores en su Sec. 2), la traza documental G1
(reports/2026-11-04--substrate-saturation-phase0-G1-trace.md; L6e en su Sec. 2
y en la tabla de la Sec. 3) y extractos literales del verificador
scripts/verify_c_across_lattices_gate.py y de la fuente primaria JDW
(arXiv:1803.01304v1, p.1 Eq. (1) y p.2 Eq. (6), texto extraído del PDF, con
dos columnas intercaladas). Ni la propuesta ni la traza son premisas. No
tienes herramientas: no ejecutes ni navegues. No propongas ampliar la
investigación ni nuevas filas.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. L6e DESDE LA FUENTE. Con JDW Eq. (1) y Eq. (6) y los vecinos X1..X6 de
   p.2: ¿es la moneda del paso 2 la identidad? ¿Se pueden fusionar los pasos
   2 y 3 sin cambiar el operador completo ni la unidad de tiempo? ¿Son los
   desplazamientos ±(1,0), ±(1/2,1/2), ±(−1/2,1/2) (en unidades de ε) y el
   fusionado ±(0,1), simétrico? ¿Implementan lo mismo las líneas citadas del
   verificador (convención de `jdw_shift`: L se mueve a −read_L)?
2. RECUENTO Y ZONÓTOPOS. ¿Tiene la presentación impresa 3 direcciones
   reducidas y la fusionada 2? ¿Es correcto que el zonótopo impreso tiene
   vértices que faltan en conv F, y que el fusionado coincide con el cuerpo
   de 4 vértices registrado en `EXPECTED_MASSLESS`?
3. CONTRATO. ¿Es cierto que el contrato define PS′ sobre una presentación y
   no afirma que el recuento sea intrínseco al walk? ¿Representa bien la
   propuesta el cuantificador existencial del contrato (Sec. 2, punto 1)?
4. LÓGICA. ¿Se sigue la recomendación (Sec. 4) de lo establecido, sin
   afirmar más: no declara imposible una regla, no emite veredicto sobre PS′
   ni sobre PH? ¿Es correcta la consecuencia condicional de la opción
   «Z(P) = conv F» (Sec. 3), incluida la hipótesis de dimensión plena? ¿Es
   correcto el párrafo sobre G1-a (medios vectores fuera del grupo)?
5. HONESTIDAD DE ESTADO. ¿Declara la propuesta que su criterio es
   retrospectivo y no preregistrado, y deja sin cambio PH, G1 y el estado de
   la fase 0?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global PASS,
REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente.
---
