# Revisión independiente del gate L6B_TRIANGULAR_ROW

Autorización explícita del usuario: «adelante» (2026-11-02), en respuesta a
la petición de lanzar la revisión cruzada con Grok y Gemini. Autoriza este
envío externo; no autoriza publicación ni promoción.
Autor: Claude Code (Claude Opus 5.5, Anthropic). Revisor: gemini vía
revision-ciega. Base: a19e480. Una revisión. Herramienta: ~/herramientas
ce09890. Se cierra con el informe del revisor.

---
Revisa de forma adversarial e independiente la ejecución del gate
L6B_TRIANGULAR_ROW: el informe 2026-11-02--l6b-triangular-row.md y el
verificador verify_l6b_triangular_row_gate.py (que importa sin
modificarlas funciones de verify_c_across_lattices_gate.py, adjunto),
escritos por Claude (Anthropic), contra el contrato congelado
L6B_TRIANGULAR_ROW_GATE.md adjunto. Se adjunta la fuente primaria ADMP
(arXiv 1803.01015v2) como texto extraído del PDF; la Figura 1 no se
conserva en la extracción. Reconstruye las afirmaciones; el informe no es
premisa. No tienes herramientas: no ejecutes, edites ni navegues; el
código se lee como texto y no confirmes el recuento 64/64.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. ENCODING: ¿fija el texto de la p.4 el etiquetado sin la Figura 1? Comprueba
   las dos premisas (lados pegados comparten etiqueta; R antihoraria k→k+1),
   la enumeración de 72 candidatos y las 6 admisibles, que la dinámica
   (Eq. (12)) solo use el predecesor k-1→k, la geometría (triángulos
   arriba/abajo, aristas h, b, s, down_of, down_edges) y que la
   codificación U_k de la Eq. (11) no cambie soporte ni espectro.
2. INTERNAL_DIMENSION: ¿es s = 6 la dimensión interna correcta de la forma
   invariante por traslaciones, frente al s = 2 de la tabla padre? ¿Cambia
   eso el alcance de Ha?
3. C0: nodo (U(0) = P⊗W, U(0)^3 = I, autovalor 1 doble), ruta A (U^3
   diagonal por bloques de orientación, c_0(V)=1/2, ω = Ω/3) y ruta B
   (perturbación degenerada de primer orden de U en el autoespacio 1).
   ¿Son correctas y de verdad independientes? Normalización por el paso
   más largo (1/2 lado). Coincidencia con el coeficiente √3/6 de la fuente
   (lado √3 por la distancia √3/2 entre puntos medios).
4. C_STRICT: argumento h_infty = h_{conv supp U^3}/3 a partir de la
   definición limsup, nilpotencia de los vértices de un paso, supervivencia
   de los seis vértices de U^3, y la cota por la distancia acotada entre
   supp U^n y supp U^{3⌊n/3⌋}. ¿Hay hueco?
5. CROSSCHECK_L6A: equivalencia de tres pasos con L6a solo módulo una
   isometría del hexágono. La primera ejecución probó solo la identidad y
   falló; la comprobación se cambió para probar las 12 isometrías. ¿Es un
   cambio legítimo o un ajuste a posteriori? ¿Prueba algo la igualdad de
   polinomios característicos?
6. SCOPE_AND_CODE: veredicto L6B_PARTIAL_VGRP_OPEN; Hb REFUTED_BY_ROW_L6b,
   Hc CONFIRMED_IN_DECLARED_ROWS, Ha sin cambio; ¿checks tautológicos o que
   codifican el resultado esperado?; ¿las dos lecturas de la moneda W están
   bien construidas?; ¿se excede el contrato?

Hasta 2400 palabras en español, con ecuaciones y contraargumentos precisos.
Cada reparación obligatoria debe identificar la ecuación o línea afectada,
qué falla y qué cerraría la objeción. Distingue aclaración de fallo
matemático. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente. No exijas resultados que el contrato no pide.
---
