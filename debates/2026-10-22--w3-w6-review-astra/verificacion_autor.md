# Lectura crítica del autor (Claude Opus 5.5), 2026-10-22 — revisión de W3–W6

Revisiones selladas sobre el texto reconstruido:
- Astra (`informe_astra.md`)
- DeepSeek (`../2026-10-22--w3-w6-review-deepseek/informe_deepseek.md`)

Las dos dan **ACCEPT_WITH_REPAIRS en W3, W4, W5-source y W6**. Ninguna encuentra errores en las identidades exactas: actualización de Z, álgebra de SWAP, cálculo funcional de J y rangos 9/6/3. Coinciden de forma independiente en los alcances y en los certificados.

| Punto | Revisor | Comprobación del autor | Decisión |
|---|---|---|---|
| W3: δE_back = 4g² diag(x_a a_a)D es solo la contribución de campo medio; a O(g²) las correlaciones creadas por R_e contribuyen al mismo orden | Astra (NOT_SUPPORTED como coeficiente completo), DeepSeek | Correcto: el informe reutiliza z′ como fondo clásico tras un paso que entrelaza | aceptada: se etiqueta como campo medio |
| W3/W5: δH_m = g z J y ∂H_m/∂z = gJ son relaciones semiclásicas de primer orden (generador del paso de transporte en un fondo), no un Hamiltoniano efectivo completo | ambos | Correcto: proceden de sustituir Z por ⟨Z⟩ en e^{−igZ⊗J} | aceptada |
| W4: R^{(1)} = −4g ∂₂²z₁ se cita de W3 sin estar en el registro; W4.5 es transporte de un testigo discreto de curvatura, no dinámica de curvatura con límite controlado | ambos | Correcto; la reconstrucción ya lo anotaba como cita no comprobada | aceptada |
| W4: el argumento genérico de amplitudes (κ arbitrario) no controla interferencias; el testigo de SWAP completo (κ = π/2) sí vale | Astra | Correcto | aceptada: la prueba se restringe al testigo |
| W4: profundidad finita solo para K_κ, no para el paso completo con CJWW | DeepSeek | Coherente con W3 («no full finite-depth synthesis claim for U_0») | aceptada |
| W6: U_{0,0} = I_g⊗U_CJWW es falsa como identidad del paso completo si κ ≠ 0 (queda K_κ); la recuperación de la materia libre exige η = 0 | Astra (NOT_SUPPORTED), DeepSeek | Correcto; F1 del contrato pide solo que la materia sea CJWW, lo cual sí vale | aceptada: se corrige la identidad mostrada |
| W6: falta un calendario explícito de coloración para los nueve tipos; F1, F5 y F6 se apoyan en analogía con W4/W5 y no están certificados | ambos | Correcto: el informe afirma que existe sin darlo | aceptada como obligación pendiente |
| Certificados: comprueban fórmulas que ellos mismos definen (p. ej. E(z) en W3) en lugar de derivarlas del símbolo J_a(p); W5 comprueba un solo q escalar | ambos | Correcto; lo confirma la lectura de los cuatro scripts | aceptada como obligación pendiente |

**Consecuencia para la evidencia:** W3, W4, W5-source y W6 pasan de PRELIMINARY a **REVIEWED_ACCEPT_WITH_REPAIRS** (dos revisiones independientes), con los alcances reducidos de la tabla:
- W3: retroacción de campo medio.
- W4: transporte del testigo discreto.
- W5: relación variacional semiclásica direccional.
- W6: rango y núcleo exactos para g ≠ 0; recuperación de la materia, no del paso completo.

Las reparaciones de texto se aplican como adendas en los informes. Siguen pendientes:
- certificados que deriven lo que hoy solo comprueban: E(z) desde J_a(p), ∂H/∂z, el símbolo J_a(p) para a = 1, 2, 3, y F1/F5/F6 de W6;
- el calendario de profundidad finita de W6.

La línea W1–W12 sigue CLOSED_BY_CONTRACT; esta revisión no la reabre.
