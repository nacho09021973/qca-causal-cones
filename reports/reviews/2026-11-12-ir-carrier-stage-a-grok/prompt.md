# Independent Grok review: carrier dichotomy, Stage A

User authorization (2026-11-12, «Aprobar y mandar a Grok»): sealed review
by Grok, a model family different from the author's. One round via
revision-ciega; herramientas 7d111a1. Base commit 58885d4. Documents in
this folder are copies of the repository files with one internal personal
name removed (naming only); the manuscript copy is the anonymised
ir-corona-v3 used in the previous review. No earlier review is attached.

Objective: decide whether Stage A establishes the R1 statement under the
amended charter. Expected result: verdict with located objections. Maximum
rounds: one. Closes with: the written report. No promotion.

---
Revisa adversarialmente una prueba matemática. No tienes herramientas,
repositorio ni web; trabaja solo con los documentos adjuntos. No
presupongas que sean correctos.

Material: un contrato congelado (IR_CARRIER_DICHOTOMY_GATE.md) con una
enmienda; el informe de la etapa A; la derivación general de la que la
etapa A es una adaptación (general-ir-rate-stage2-leading-term.md, ya
revisada una vez por separado); la salida de un diagnóstico numérico; y el
manuscrito de partida (ir-corona-anon.tex), cuyos lemas se citan.

Afirmación a juzgar (régimen R1): cuando el momento cero no es dominante
pero un momento dominante eta_k != 0 tiene carácter trivial sobre los
planos de red ortogonales a xi_*, bajo H1–H3, H5, H7, H8, H2 en el
conjunto dominante y H6_k, H9_k, H10_k de la enmienda, algún par de la
familia cumple limsup (1/N) log delta(N) = -K_*, con término principal
transportado por eta_k y potencia 5 + d/2.

Comprueba en particular:
1. La reducción de todas las fases globales a e^(iN psi_k) (sección 2),
   incluida la cancelación de e^(+-i eta_k.(y_*-x_*)), y la comprobación
   contra el punto pi u del manuscrito.
2. Que las sumas de profundidad con decaimiento complejo kappa + i phi
   (sección 3) están bien definidas, son 1-periódicas y que la fórmula de
   Poisson y la transformada siguen valiendo.
3. Que el término principal (sección 4) hereda de la derivación general
   las cotas de error sin cambios.
4. La pérdida de positividad del promedio bajo H9(ii) (sección 5) y que la
   condición mu_k != 0 es la correcta; bajo H9(i), que el promedio no se
   anula.
5. El argumento de segundo momento para portadores inseparables (sección
   8): equidistribución conjunta, desaparición de los términos cruzados,
   paso a densidad positiva, y que la rotación (H10_k) y la bilinealidad
   cierran.
6. Coherencia de la enmienda con lo que la prueba usa; si falta o sobra
   alguna condición.
7. Que los informes no afirman más de lo que prueban (en particular sobre
   el diagnóstico numérico y sobre la ausencia de ejemplos en Z^d).

Salida: dictamen PASS / REPAIR_REQUIRED / REJECTED. Cada objeción debe
citar documento y sección, decir si es error fatal, reparación necesaria,
hipótesis que falta o exposición, y dar la derivación o el contraejemplo
cuando sea decisiva. Marca NO_VERIFICADO lo que no puedas comprobar; no lo
conviertas en PASS por plausibilidad. Lista aparte lo rederivado. No se
pide juzgar originalidad.

Presupuesto: una ronda. Cierre: informe escrito con dictamen y
obligaciones pendientes.
---
