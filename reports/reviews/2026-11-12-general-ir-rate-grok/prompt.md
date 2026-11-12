# Independent Grok review: general infrared operational rate

User authorization (2026-11-12, «Aprobar y mandar a Grok»): sealed review
by Grok, a model family different from the author's (Claude). One round
via revision-ciega; herramientas 7d111a1. Base commit 65e1ec4.
Documents: charter, Amendments 1–3, the three stage reports, and the
IR-corona manuscript at tag ir-corona-v3 with five identifying strings
replaced (ir-corona-anon.tex here). No earlier review is attached.

Objective: decide whether the Stage 1 and Stage 2 proofs establish the
amended statement (T). Expected result: verdict with located objections.
Maximum rounds: one. Closes with: the written report. No automatic
repair/re-review loop, no promotion.

---
Revisa adversarialmente una prueba matemática. No tienes herramientas,
repositorio ni web; trabaja solo con los documentos adjuntos. No
presupongas que sean correctos: son borradores de un autor, no fuentes.

Material: un contrato congelado (GENERAL_IR_RATE_GATE.md) con tres
enmiendas, tres informes de ejecución (etapas 0–1; progreso de la etapa 2;
término principal y no anulación) y un manuscrito previo (ir-corona-anon.tex)
cuyo caso particular (un paseo de Weyl en Z^3) se generaliza. Los informes
citan lemas y ecuaciones de ese manuscrito.

Afirmación a juzgar. En la clase del contrato (d en {2,3}, paseo unitario
de alcance finito en Z^d ⊗ C^s con nodo isótropo en p=0, regiones bola,
protocolo de la familia declarada) y bajo H1–H3, H4′, H5–H10:
  (Etapa 1) delta(N) <= C N^(d+s-1) e^(-K_* N) para toda operación;
  (Etapa 2) para algún par (M, M_B) de la familia,
            limsup (1/N) log delta(N) = -K_*.

Comprueba en particular:
1. Etapa 1: convexidad de Phi por el argumento de subarmonicidad/tres
   líneas; el lema de potencias con forma de Schur; la igualdad de
   Fenchel–Young y la condición de primer orden en B−A; el test de Schur.
2. Que las hipótesis H1–H10 son coherentes entre sí, que cada una se usa
   donde se dice y que ninguna paso de la prueba usa una hipótesis no
   declarada. ¿Falta alguna condición? ¿Sobra alguna?
3. Lema de cola libre general: proyector espectral del par nodal,
   Duhamel, uniformidad.
4. Sumas por capas generales (d−1 = 1 o 2): Poisson en el plano,
   variación total de la tercera derivada, constantes k_A y k_B,
   uniformidad en los desfases; comprobación contra el caso d=3.
5. Sumas de profundidad: la transformada g^ y su comprobación contra el
   caso d=3.
6. Ensamblaje con gaussiana compleja C = Q + iQ': acretividad del
   complemento de Schur, integración en eta_n, potencia 5 + d/2.
7. Promedio positivo del factor de profundidad bajo H9 (i) y (ii):
   equidistribución, signo de la parte real de cada término, continuidad
   y periodicidad en el desfase, paso a densidad positiva.
8. No anulación: eliminación de los otros puntos triviales (H6), rotación
   del coeficiente (H10), argumento de bilinealidad para pasar de una
   combinación lineal a un par de la familia, y que la fase e^(iN psi) no
   estropea el argumento.
9. Que el caso del manuscrito cumple H1–H10 según se afirma (sección 8 del
   último informe).
10. Que los informes no afirman más de lo que prueban.

Salida: dictamen global PASS / REPAIR_REQUIRED / REJECTED para la etapa 1
y para la etapa 2 por separado. Cada objeción debe citar documento y
sección, decir si es error fatal, reparación necesaria, hipótesis que
falta o cuestión de exposición, y dar la derivación o el contraejemplo
cuando sea decisiva. Si no puedes verificar un paso, márcalo NO_VERIFICADO;
no lo conviertas en PASS por plausibilidad ni añadas hipótesis para
salvarlo. Lista aparte lo que sí has rederivado. No se pide juzgar la
originalidad.

Presupuesto: una ronda. Cierre: informe escrito con dictamen y
obligaciones pendientes.
---
