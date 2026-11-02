# Revisión independiente del gate DISPERSION_CORRECTIONS_ACROSS_LATTICES

Autorización explícita del usuario: «adelante» (2026-11-02), en respuesta a
la petición de lanzar la revisión cruzada con Gemini y Grok. Autoriza este
envío externo; no autoriza publicación ni promoción.
Autor: Claude Code (Claude Fable 5.1 y Claude Opus 5.5, Anthropic). Revisor: gemini vía
revision-ciega. Base: 9557aa9. Una revisión. Herramienta: ~/herramientas
ce09890. Se cierra con el informe del revisor.

---
Revisa de forma adversarial e independiente la ejecución del gate
DISPERSION_CORRECTIONS_ACROSS_LATTICES: el informe
2026-11-02--dispersion-corrections-across-lattices.md y el verificador
verify_dispersion_corrections_gate.py, escritos por Claude (Anthropic),
contra el contrato congelado DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md
adjunto. El verificador importa sin modificarlos los símbolos de las filas
desde cinco scripts revisados antes, que también se adjuntan:
verify_c_across_lattices_gate.py, verify_weyl_dirac_gate.py,
verify_directional_saturation.py, cert_Aa_s4_counterexample.py y
verify_l6b_triangular_row_gate.py. Reconstruye las afirmaciones; el informe
no es premisa. No tienes herramientas: no ejecutes, edites ni navegues; el
código se lee como texto y no confirmes el recuento 79/79.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:
1. SERIES: ¿es correcto el método? Factor cuadrático del nodo
   λ² − s1 λ + s2; fase común φ con exp(−2iφ) = s2/s2(0); ω² a partir de
   cos²ω = s1²/(4 s2) y arccos(1−v)²; ramas ε = ε0 + φ ± ω; composición de
   series truncadas (log, sqrt, 1/(1+v)); reducción a la esfera
   |n| = 1. ¿Bastan los grados N = 6 (d ≤ 2) y N = 4 (d = 3) para los
   órdenes relativos que se tabulan? ¿Es correcta la velocidad de grupo?
2. BLOCKS: separación de L5b por Γ = dP_X dP_Y dP_Z (conmuta con todos los
   coeficientes, Γ² = −I); bloques de orientación de V = U³ en L6b con
   escala 1/2 y divisor 3; en L3s4, levantamiento de Hensel del factor
   cuadrático en la raíz doble exp(∓iπ/4), polinomio característico por
   identidades de Newton sobre trazas truncadas, y a, b = √(1−a²) como
   símbolos independientes reducidos con b² = 1 − a². ¿Es exacto el test
   de cero? ¿Es correcta la lectura de φ ≠ 0 en L3s4 como desplazamiento
   común de los dos niveles?
3. SYMMETRY: G_walk como los elementos g del grupo puntual con
   charpoly U(gk) = charpoly U(k), comprobado por igualdad de tr U^m,
   m = 1..s, bajo la sustitución de monomios z^h → z^(Mh). ¿Es la noción
   adecuada para decidir qué armónicos permite el contrato? ¿Son correctos
   los grupos tabulados (D_4, O_h, T_d de 24, D_3, D_6, el de 8 elementos
   de L3s4)? ¿Es correcto el argumento de grado de la Sec. 1 del contrato
   (C_6 sin anisotropía antes de |k|⁴; C_3 con cos 3θ a orden |k|)?
4. VALUES: reconstruye por una vía propia al menos L2, L3 y L6c o L6d, y
   comprueba las formas cerradas del informe (α = −Σ n_i²n_j²/(6d) para
   cos ω = Π cos p_i; −σ2/18 − n1²n2²n3²/6 en las filas BCC quirales;
   L6a con β = −(√15/36) cos 3θ y α = −41/1728 − (5/1728) cos 6θ). ¿Es
   correcta la relación L6b/L6a (c_0 por 2/3, β por 2, α por 4, rotación
   de 60°)? Raíz a* de α_0 en L3s4.
5. HYPOTHESES: veredictos Hd REFUTED_BY_ROW_L1 (y L3s4 para a < a*), He
   CONFIRMED_IN_DECLARED_ROWS, Hf REFUTED_BY_ROW_L6e, contra el texto
   exacto del contrato §4. ¿Cuenta un término impar n1 n2 n3 como
   «coeficiente anisótropo de la corrección más baja» para He? ¿Es la
   lectura de Hf la del contrato? ¿Algún veredicto está decidido solo por
   simetría y debería ser DECIDED_BY_SYMMETRY?
6. SCOPE_AND_CODE: veredicto CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN;
   ¿checks tautológicos o que codifican el resultado esperado?; las
   hipótesis se imprimen pero no se afirman, ¿es correcto?; correcciones
   hechas durante la ejecución (Sec. 5 del informe), ¿legítimas o ajuste a
   posteriori?; ¿se excede el contrato o se omite algo que pide?

Hasta 2400 palabras en español, con ecuaciones y contraargumentos precisos.
Cada reparación obligatoria debe identificar la ecuación o línea afectada,
qué falla y qué cerraría la objeción. Distingue aclaración de fallo
matemático. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente. No exijas resultados que el contrato no pide.
---
