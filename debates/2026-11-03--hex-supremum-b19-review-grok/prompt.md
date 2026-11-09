# Revisión independiente (casa Grok) de M1-B19 (soporte de 19 puntos)

Autorización explícita del usuario (2026-11-03): «Autorizo las dos cosas:
push de `6302328` y revisión independiente con Grok y Gemini. No autorizo
todavía ampliar M1 a S25.» Orden fijado por el usuario: push conservando
PRELIMINARY, revisión ciega de Grok y Gemini sobre exactamente los mismos
archivos y versiones, lectura crítica y decisión separada de promoción.
Autoriza el envío externo a xAI (Grok) y a Google (Gemini), encargos
gemelos con entrada idéntica; no autoriza publicación ni promoción. Autor:
Claude (Anthropic). Base: 6302328 (publicado en
`research/schur-stability-audit`). Herramienta: ce09890. Una revisión por
casa, una ronda. Hashes en `inputs.sha256`.

Comprobación previa (regla de los tres puntos). Sabido: rigidez en rectas
normales, T2 de soporte mínimo y la etapa A con S13 (promocionados); M1-B19
da A3, A4, la reducción 56 → 28 → 18 y un certificado de Gram,
PRELIMINARY, verificador 17/17. Pregunta: ¿la cadena hipótesis originales
→ A3/A4 → sistema reducido → certificado es correcta y no elimina
soluciones legítimas? Cierre: PASS en ambas casas → lectura del autor y
decisión de promoción del usuario (con enmienda previa del campo de
coeficientes); REPAIR_REQUIRED → reparar; si una objeción invalida A3, A4,
la reducción o el certificado, S19 vuelve a OPEN y el usuario decide si
usa el presupuesto de solver (3600 s, 0 s consumidos).

---
Revisa de forma adversarial e independiente el informe
2026-11-03--hex-supremum-b19.md (M1-B19 del contrato HEX_SUPREMUM_GATE.md),
escrito por Claude (Anthropic), su verificador verify_hex_supremum_b19.py y
el fichero de multiplicadores hex_s19_certificate.json. Se adjuntan, como
fuentes ya revisadas y promocionadas, el informe y el verificador de la
etapa A (verify_hex_supremum_gate.py, importado por el de B19), y el
informe y el verificador del gate padre (hex-ceiling). El informe no es
premisa: comprueba cada paso. No tienes herramientas: no ejecutes, edites
ni navegues. Si un punto solo puede comprobarse ejecutando código, dilo y
evalúa si el código, tal como está escrito, comprueba lo que dice.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. LEMA A3. ¿Se deduce necesariamente de unitariedad y rigidez, sin
   hipótesis añadidas? Comprueba: que f(z; s) es un polinomio analítico en
   z para todo s real (exponentes r − h·n ≥ 0 y múltiplos de delta), que
   Re g = 0 en el círculo implica g constante imaginaria, que g(1) = 0, y
   que los coeficientes de Fourier de g son exactamente las sumas por capa
   del enunciado. ¿Vale igual el signo −?
2. LEMA A4. ¿Es correcta la derivación de la antihermiticidad de
   K(t) = D(t)^† ∂_e U(t n), la expresión de K_{+−} y conj K_{−+}, y el
   emparejamiento de frecuencias λ' = −λ? ¿Hay frecuencias coincidentes
   que el emparejamiento ignore?
3. NO SE ELIMINAN SOLUCIONES. A3 y A4 son condiciones necesarias; confirma
   que lo son y que el verificador impone exactamente esas identidades
   (linear_system: L1 sumas de capa, L2 = A3, L3 = A4) y no otras más
   fuertes. ¿Basta usar las tres primeras normales de cara (normals[:3]),
   o las opuestas aportarían restricciones distintas? (Usar menos
   restricciones no elimina soluciones; usar de más sí.)
4. REDUCCIÓN A 18 PARÁMETROS. ¿Conservan las transformaciones lineales
   (forma real con z y w = conj z formales, rango y rref exactos sobre
   QQ(sqrt3), parametrización afín P, Q en t) todas las soluciones del
   sistema lineal? ¿Es legítimo tratar w como variable independiente y
   luego volver a la forma real? ¿unitarity_equations codifica las dos
   familias Σ A_{h+d} A_h^† = δ_{d0} I y Σ A_h^† A_{h+d} = δ_{d0} I para todo
   d, sin omitir ninguna?
5. CERTIFICADO DE GRAM. Revisa check_certificate, gram_of,
   ldl_pivots_positive y positive_q3: ¿la comprobación p = (1,t) G (1,t)^T
   es identidad polinómica completa? ¿La eliminación exacta con 19 pivotes
   positivos implica G definida positiva y p > 0 en todo R^18, es decir,
   sobre todas las variables reales restantes? ¿Es exacta la decisión de
   signo de a + b√3? ¿Es correcta la conversión a la forma del contrato
   −1 = Σ (d_j/μ) ℓ_j² + Σ (−c_i/μ) f_i?
6. DESVIACIONES LITERALES DEL CONTRATO. El contrato, Sec. 4 (ii), pide
   «exact rational coefficients» y una comprobación «exactly and quickly»;
   el certificado tiene c_i racionales pero G, d_j y ℓ_j en QQ(sqrt3), y el
   verificador tarda unos 11 minutos. ¿Es la forma usada matemáticamente
   equivalente en validez a la del contrato? ¿Son desviaciones que deben
   declararse con una enmienda explícita antes de promocionar? No se
   modificará retroactivamente el prerregistro.
7. CONTROLES Y ALCANCE. ¿Son pertinentes los controles del cuadrado
   (recordando que no sustituyen la demostración de A3 y A4)? ¿Se
   corresponden los veredictos (M1-B19 PROVED_FOR_S19, HX2
   CONFIRMED_FOR_S19, M1-A OPEN_AFTER_SINGLETON_LAYER_ANALYSIS) con lo
   demostrado, sin extenderse a S25, a soportes mayores ni a s > 2? ¿Dice
   el informe lo que el verificador no certifica?

Hasta 2000 palabras en español. Cada reparación obligatoria debe citar la
frase o la línea afectada, por qué falla y qué la cerraría. Distingue
aclaración de error. Dictamen global y lista de reparaciones obligatorias;
si no hay ninguna, dilo expresamente. No exijas resultados nuevos (S25 no
está en el alcance).
---
