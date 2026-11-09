# Revisión independiente (casa Grok), ronda 2: ejecución de la fase 0 (SUBSTRATE_SATURATION)

Autorización explícita del usuario (2026-11-03): «Elijo la opción (a):
segunda revisión de Grok, con los documentos de la puerta Weyl/Dirac»,
limitada a tres comprobaciones (L3, L4, integridad de las reparaciones),
con veredictos PASS, REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y referencias
exactas. No autoriza commit ni promoción. Autoriza el envío externo a xAI
(Grok). Autor: Claude (Anthropic). Base: 6851d92 (publicado) más el informe
revisado sin commit (hash en `inputs.sha256`; copia en
`informe_fase0_rev_snapshot.md`). Contrato congelado en 9bf3019.
Herramienta: ce09890. Una revisión, una ronda.

Comprobación previa (regla de los tres puntos). Sabido: la ronda 1 dio
REPAIR_REQUIRED (cinco reparaciones, aplicadas); el veredicto definicional
bajó a OPEN_AFTER_ROW_SURVEY por L4; al aplicar la reparación el autor
encontró que L3 también es fila registrada y trazó su nodo a la puerta
Weyl/Dirac. Pregunta: ¿satisface ese certificado existente la definición
congelada de nodo, y están bien aplicadas las reparaciones? Cierre: el
usuario decide; si L3 no satisface la definición, quedan dos filas abiertas
antes que una equivalencia no demostrada.

---
Revisa de forma adversarial e independiente el informe revisado
2026-11-03--substrate-saturation-phase0.md, escrito por Claude (Anthropic),
contra su contrato congelado SUBSTRATE_SATURATION_PHASE0_GATE.md. Se
adjuntan: un extracto literal de state/CURRENT_STATE.md con numeración
original (incluye la Sec. 5, puerta Weyl/Dirac, y la Sec. 8), tu informe
de la ronda 1 y la lectura del autor, el informe c-across-lattices, el
contrato, la derivación analítica, el registro de verificación y el
verificador de la puerta Weyl/Dirac, y el informe hex-ceiling. El informe
no es premisa. No tienes herramientas: no ejecutes, edites ni navegues. No
propongas cálculos ni ampliar la investigación.

Tres comprobaciones, cada una con veredicto PASS / REPAIR_REQUIRED /
INSUFFICIENT_EVIDENCE:

1. L3. ¿Implica el PASS de la puerta Weyl/Dirac (comprobación congelada:
   derivadas primeras y hessiana del símbolo escalar en cero, isotropía
   incluidas entradas mixtas; `∇u(0)=0`; `c_0 = r_in = 1/sqrt(d)`)
   exactamente la condición congelada de nodo de la Sec. 2.4 del contrato
   (`U(0)` escalar; término lineal hermítico sin traza con
   `{T_a, T_b} = 2 c_0^2 delta_ab`; inclinación nula)? Establece la
   correspondencia matemática término a término con lo que dicen los
   documentos y el verificador adjuntos, o di dónde falla o qué falta. No
   basta con que las condiciones parezcan compatibles. Si los documentos no
   permiten decidirlo, INSUFFICIENT_EVIDENCE.
2. L4. ¿Está correctamente justificado, por insuficiencia documental, que
   L4 queda sin clasificar (ni admisible ni OUTSIDE_DEFINITIONS)? ¿Se
   conserva esa incertidumbre sin convertirla en exclusión del dominio ni
   en apoyo? No intentes resolver L4.
3. INTEGRIDAD. ¿Están aplicadas las cinco reparaciones de la ronda 1 (L4,
   fuente única de L2/L3, citas de L6b, cita de L6c, frase única del
   veredicto)? ¿Depende alguna conclusión del informe revisado de una
   inferencia no certificada? Con L4 sin resolver, ¿es correcto que el
   veredicto definicional siga siendo OPEN_AFTER_ROW_SURVEY aunque L3
   pase?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global y
lista de reparaciones obligatorias; si no hay ninguna, dilo expresamente.
---
