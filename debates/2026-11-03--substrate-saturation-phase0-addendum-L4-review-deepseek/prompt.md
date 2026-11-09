# Revisión independiente (casa DeepSeek) del addendum de la fase 0 sobre la fila L4

Autorización explícita del usuario (2026-11-03): «haz commit del addendum y
mándalo a revisar con Deep». Autoriza el envío externo a DeepSeek; no
autoriza promoción ni cambios en la auditoría. Autor: Claude (Anthropic).
Base: 3e20c70 (local). Herramienta: ce09890. Modelo: deepseek-v4-pro
(generación comprobada con una petición trivial antes del envío). Una
revisión, una ronda. Hashes en `inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: la auditoría dejó
L4 sin clasificar porque su nodo no estaba trazado en el sentido congelado;
el addendum lee CJWW (5.12) y (5.15) y deriva a mano las cláusulas del
nodo. Pregunta: ¿son correctas esas derivaciones y la lectura de la
fuente, y respeta el addendum que no cambia las salidas de la auditoría?
Cierre: PASS → el usuario decide si enmienda la carta para resolver L4;
REPAIR_REQUIRED → se repara; si una derivación falla, L4 sigue sin
clasificar.

---
Revisa de forma adversarial e independiente el addendum
2026-11-03--substrate-saturation-phase0-addendum-L4.md, escrito por Claude
(Anthropic). Se adjuntan: el contrato congelado de la fase 0, el informe de
la auditoría al que se añade, el texto extraído de las páginas 17–18 del PDF
de Cedzich, Joye, Werner y Werner (arXiv:2408.02108v1, Sec. 5.4, con las
Ecs. (5.12)–(5.17)) y un extracto literal de state/CURRENT_STATE.md
(Sec. 8) con su numeración. El addendum no es premisa. No tienes
herramientas: no ejecutes ni navegues. No propongas ampliar la
investigación.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. FUENTE. ¿Transcribe el addendum correctamente (5.12), (5.14), (5.15) y
   (5.16) y lo que dice el texto (puntos cónicos, determinante 1)? ¿Es
   correcta la lectura de (5.14) como errata tipográfica?
2. DERIVACIONES. Rehaz a mano, para (5.12) y para (5.15): W(0); las
   derivadas ∂_a W(0); T_a = i ∂_a W(0); hermiticidad, traza nula y
   {T_a, T_b} = 2 c_0^2 δ_ab con c_0 = 1; la unitariedad de (5.15) para p
   real. Señala cualquier error de signo o de factor y si afecta a alguna
   cláusula.
3. CORRESPONDENCIA CON EL CONTRATO. ¿Cubren las cláusulas (i)–(v) del
   addendum exactamente la condición congelada de nodo isótropo sin
   inclinación de la Sec. 2.4 del contrato, incluida la forma equivalente
   A(n)^2 = c_0^2 |n|^2 I? ¿Falta alguna hipótesis (por ejemplo, que el
   nodo sin masa en k = 0 sea el que se usa, o la convención de signo del
   momento)?
4. SOPORTE Y UNIDADES. ¿Contiene el soporte compuesto (±1, ±1, ±1) en
   ambos walks, de modo que C_micro = [−1, 1]^3 y r_in = 1? ¿Es correcto
   el reescalado a paso más largo 1 y que el par siga tomándose de una sola
   fuente (l. 147 del informe c-across-lattices, citado en la auditoría)?
5. ALCANCE. ¿Deja el addendum intactas las salidas de la auditoría
   (OPEN_AFTER_ROW_SURVEY, L4 sin clasificar, los dos
   NO_COUNTEREXAMPLE_IN_SOURCE_TABLE), sin presentarse como evidencia para
   (PH) ni como resolución de L4?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global
PASS, REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
