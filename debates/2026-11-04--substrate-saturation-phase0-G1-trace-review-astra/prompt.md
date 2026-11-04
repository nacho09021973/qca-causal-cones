# Revisión independiente (casa OpenAI, gpt-6.1-sol) de la traza documental de la laguna G1 de la fase 0

Autorización explícita del usuario (2026-11-04), respuesta a la propuesta
de casa: «aceptado gtp 6.1. Sol». Autoriza el envío a OpenAI
(`gpt-6.1-sol`, vía `codex exec`, miembro astra); no autoriza cerrar G1,
cambiar la salida de la auditoría ni promover nada. Autor de la traza:
Claude (Anthropic). Base: cb814b5 (local). Herramienta: ce09890.
Generación comprobada antes del envío con una petición trivial («OK»). Una
revisión, una ronda. Hashes en `inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: la revaluación
(862b405) nombró G1 (generadores reducidos de las filas de clase producto);
la traza (cb814b5) resuelve siete filas y deja G1-a, G1-b y G1-c abiertas.
Pregunta: ¿son correctas la lectura de los constructores, los dos lemas, el
cálculo de patrones por fila y la clasificación de las lagunas? Cierre:
PASS → el usuario decide sobre G1-a/G1-c; REPAIR_REQUIRED → se repara; un
error en una fila resuelta la devuelve a laguna.

---
Revisa de forma adversarial e independiente la traza
reports/2026-11-04--substrate-saturation-phase0-G1-trace.md, escrita por
Claude (Anthropic). Se adjuntan: el contrato congelado de la fase 0 (la
clase producto y los generadores reducidos están en su Sec. 1, «Zonotope
reading», y en la Sec. 3.2), el informe de la auditoría (Sec. 7 nombra G1;
F2 está en la Sec. 4), los verificadores completos
scripts/verify_c_across_lattices_gate.py y scripts/verify_weyl_dirac_gate.py,
el texto de las pp. 16–17 del PDF de CJWW (arXiv:2408.02108v1) y extractos
numerados de scripts/verify_directional_saturation.py, del informe
c-across-lattices y de CURRENT_STATE. La traza no es premisa. No tienes
herramientas: no ejecutes ni navegues. No propongas ampliar la
investigación.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. LEMAS (Sec. 1). ¿Son correctos el Lema V (cada vértice del zonótopo
   procede de un único patrón si todo a_i ≠ 0) y el Lema P (amplitud nula
   de un patrón con proyectores de rango uno sii hay un par consecutivo
   antípoda)? ¿Es correcta m(θ) = (0, sin 2θ, cos 2θ) para R = U(0, π/2,
   0, θ) con la U de JDW (verificador l. 92–97)?
2. FILAS RESUELTAS. Para L1–L3, L5a, CJWW (5.12), L6a y L6d: ¿pertenecen
   literalmente a la clase producto según el código citado? ¿Son correctos
   los desplazamientos de los factores, los generadores reducidos, la
   asignación de patrones a desplazamientos y el uso de los soportes
   afirmados (EXPECTED_F, «active support», jump set)? ¿Se distinguen bien
   patrones y desplazamientos coincidentes?
3. L6e (G1-c). Rehaz: factores, U^2 = U(0,0,−π/2,0) = I, qué patrones se
   anulan y por qué, el zonótopo de tres generadores frente al soporte
   afirmado, y la presentación fusionada de dos factores. ¿Es correcto
   concluir que los generadores reducidos dependen de la presentación?
4. L6c, L6f (G1-a) y CJWW (5.15) (G1-b). ¿Es correcto que sus desplazamientos
   parciales no son de la forma ±a (c_j ≠ −b_j)? ¿Es correcta la lectura
   afín (a_j, m_j, suma de m_j = 0, coincidencia con EXPECTED_F)? ¿Es
   correcto que (5.15) no tiene factorización en lo adjuntado y que no puede
   deducirse del soporte?
5. ALCANCE. ¿Respeta la traza que G1 no se cierra, que la auditoría sigue
   OPEN_AFTER_ROW_SURVEY sin valor confirmatorio, y que el hallazgo sobre
   L6e se registra sin veredicto sobre (PS′) ni efecto sobre (PH)? ¿Se ha
   deducido algún factor de las aristas del cuerpo?

Hasta 1800 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global
PASS, REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
