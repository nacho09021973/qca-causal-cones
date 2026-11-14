# Revisión independiente: brecha uniforme en S13 (adenda candidata a M1-B13)

Autorización del usuario (2026-11-14): «Solicitar una revisión independiente
de la prueba de compacidad de S13, comprobando también que la clase
admisible no sea vacía». Casa y permiso de envío (2026-11-14, respuesta
explícita del usuario): Grok, una ronda; autoriza el envío a xAI, no
publicación ni promoción. Autor: Claude (Anthropic); el Lema 2 lo formuló
el usuario con un asistente externo y lo comprobó el autor. Base: 7cadad6.
Herramienta: ~/herramientas 2a7342b.

Objetivo: decidir si el candidato demuestra, en la clase X_13, que
sup c_0/r_in < 1 y que X_13 no es vacía. Resultado esperado: dictamen por
bloque PASS / REPAIR_REQUIRED / OPEN. Rondas: una por casa. Cierre: PASS →
incorporar el resultado al informe de S13 como adenda PRELIMINARY revisada,
sin contrato nuevo, y promoción solo por decisión del usuario;
REPAIR_REQUIRED → reparar y, si el usuario lo decide, re-revisión acotada;
una objeción que invalide el Lema 1 o el Lema 2 → el resultado queda OPEN.
No autoriza cálculos de eps_13 ni S19.

---
Revisa de forma adversarial e independiente el documento candidato.md
(adenda candidata al informe 2026-11-03--hex-supremum.md), escrito por
Claude (Anthropic) salvo la prueba del Lema 2, formulada por el usuario.
Se adjuntan como fuentes ya revisadas y promocionadas el informe de S13, el
informe del gate padre hex-ceiling (con el Lema B, Bernstein, y la
subclase T1) y los dos contratos. El candidato no es premisa: comprueba
cada paso. No tienes herramientas: no ejecutes, edites ni navegues.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. CLASE. ¿X_13 coincide con lo que M1-B13 cubre (W_hex^sym, F dentro de
   S13, envolvente igual al hexágono de S13)? ¿Es constante el
   denominador r_in en X_13?
2. LEMA 1 (compacidad). ¿Son cerradas todas las condiciones de Y
   (unitariedad, U(0) escalar con la fase, nodo sin traza, isotropía
   escrita como A(e1)^2 = A(e2)^2 = c^2 I y anticonmutación)? ¿Es correcta
   la acotación por la identidad de orden cero de U^dag U = I? ¿Son
   exactamente c_0 > 0 y los seis coeficientes de vértice no nulos las
   condiciones abiertas, sin ninguna otra condición de la clase que no sea
   cerrada (en particular la regularidad hexagonal de la envolvente)?
   ¿Es continuo el cociente?
3. LEMA 2 (pérdida de vértice). Comprueba las proyecciones
   {-1, -1/2, 0, 1/2} de S13 sin un vértice, las frecuencias
   {-3, -1, 1, 3} de P(t) = e^{-it} W(4t), la aplicación del Lema B
   elemento a elemento, la derivada P'(0) = -i(I + 4H), la hermiticidad
   de H y su espectro {±c_0}, y la conclusión c_0 <= 1/2. ¿Vale en un
   punto del cierre que no está en la clase?
4. TEOREMA. ¿Es exhaustiva la división en tres casos del maximizador?
   ¿Pertenece a X_13 todo punto del cierre con c_0 > 0 y los seis
   vértices no nulos, aunque falten puntos del anillo interior?
5. NO VACUIDAD. ¿El paseo de T1 con b_j = 2a_j situados en vértices
   alternos de S13 es un polinomio de Laurent unitario sobre la red, con
   F = {0} ∪ vértices de S13, nodo e isotropía, y cociente sqrt3/2? ¿Es
   correcta la salvedad de que está en W_hex^sym y no necesariamente en
   W_hex?
6. ALCANCE. ¿Afirma el candidato solo una brecha cualitativa en S13, con
   0 < eps_13 <= 1 - sqrt3/2, sin extenderse a S19, soportes mayores,
   s > 2, ni a que el sustrato fije c_0? ¿Es correcta la observación de
   la Sec. 5 sobre hexágonos mayores, o la presenta con más fuerza de la
   demostrada?

Hasta 1500 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente. No exijas resultados nuevos (ni un valor de
eps_13 ni S19).
---
