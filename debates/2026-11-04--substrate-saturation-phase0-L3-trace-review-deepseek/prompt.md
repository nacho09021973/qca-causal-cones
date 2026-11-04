# Revisión independiente (casa DeepSeek) de la traza del nodo de la fila L3 en la auditoría de la fase 0

Autorización explícita del usuario (2026-11-04, respuesta a la pregunta de
envío): «DeepSeek». Autoriza el envío a DeepSeek; no autoriza promoción. Autor: Claude
(Anthropic). Base: 78eb306 (local). Herramienta: ce09890. Modelo:
deepseek-v4-pro (comprobar generación con una petición trivial antes del
envío). Una revisión, una ronda. Hashes en `inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: la auditoría
(2f6160e) traza el nodo isótropo sin inclinación de L3 cláusula a cláusula
hasta comprobaciones del verificador `scripts/verify_weyl_dirac_gate.py`
(l. 147, 149, 158–167, 172–173); el usuario comprobó las derivaciones (ii) y
(v), no las líneas del verificador. Pregunta: ¿confirma un revisor de otra
familia, con esas líneas y la Sec. 2.4 congelada, la correspondencia
completa? Cierre: PASS → L3 puede usarse como testigo (decisión del usuario,
sin promoción automática); REPAIR_REQUIRED → se repara; un fallo de fondo
deja L3 pendiente.

---
Revisa de forma adversarial e independiente un único párrafo del informe
reports/2026-11-03--substrate-saturation-phase0.md, escrito por Claude
(Anthropic): la «Definition check (contract Sec. 3.4)», l. 86–118, que traza
el nodo de la fila L3 (walk de Weyl en la red BCC, d = 3) hasta
comprobaciones del verificador exacto scripts/verify_weyl_dirac_gate.py. Se
adjuntan: el informe completo, el contrato congelado de la fase 0
(theory/SUBSTRATE_SATURATION_PHASE0_GATE.md; la condición de nodo está en su
Sec. 2.4), el verificador completo y extractos literales numerados de
state/CURRENT_STATE.md (Sec. 5), del informe c-across-lattices (tabla de
filas, l. 143 para L3) y del informe del gate exacto de Weyl/Dirac (l.
131–138). El informe no es premisa. No tienes herramientas: no ejecutes ni
navegues. No propongas ampliar la investigación.

Dictámenes separados PASS / REPAIR_REQUIRED / INSUFFICIENT_EVIDENCE:
1. LÍNEAS. ¿Hace cada línea citada del verificador (147, 149, 158, 159–160,
   161–162, 164–167, 172–173) lo que el párrafo le atribuye? Lee
   `published_symbol`, `spatial_derivative` y `verify_case`.
2. COBERTURA DE L3. ¿Son los símbolos d = 3 que comprueba el verificador
   (A±, B±) los walks de la fila L3? Usa la tabla del informe
   c-across-lattices (l. 143, fuente «CURRENT_STATE Secs. 4, 5») y el
   extracto de CURRENT_STATE. Si la identificación no se sigue de lo
   adjuntado, dilo.
3. DERIVACIONES. Rehaz (ii): de W W^† = I como identidad de Laurent y W(0)
   = I, ¿se sigue que i ∂W(0) es hermítica? Ten en cuenta que
   `spatial_derivative` usa i z ∂_z / sqrt(d) con z = e^{±ik}: ¿afecta la
   convención de signo o el factor a la hermiticidad, a la traza nula o al
   anticonmutador? Rehaz (iii) y (iv) y la identificación c_0 = 1/sqrt(d)
   por «massless matching».
4. INCLINACIÓN. ¿Es correcto llegar a (v) sólo mediante la forma
   equivalente A(n)^2 = c_0^2 |n|^2 I que declara el contrato? ¿Implican
   (iii) y (iv) esa forma, y declara el contrato la equivalencia de modo
   que baste?
5. UNIDADES Y ALCANCE. ¿Son coherentes las unidades del verificador
   (vértices {±1}^3, inradio 1/sqrt3, paso más largo 1) con la regla de
   una sola fuente por fila de la Sec. 2.4 del contrato? ¿Respeta el
   párrafo que el «Hessian» (l. 169–171) no es el certificado del nodo, y
   no presenta la traza como evidencia para (PH)?

Hasta 1500 palabras en español. Cada defecto: frase o línea exacta, por qué
falla y qué lo cerraría. Distingue aclaración de error. Dictamen global
PASS, REPAIR_REQUIRED o INSUFFICIENT_EVIDENCE y lista de reparaciones
obligatorias; si no hay ninguna, dilo expresamente.
---
