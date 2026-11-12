# Independent Codex review: Bravais-lattice Stage 1

User authorization (2026-11-12, «empezamos con que Codex revise la FAse 1»):
sealed review by GPT-6 Astra (OpenAI, via `codex exec`), a model family
different from the author's (Claude). One round via `revision-ciega astra`;
herramientas `7d111a1`. Generation probed the same day (`codex exec --model
gpt-6-astra`, trivial prompt, answered). Base commit `24e1965`.

Candidate: `reports/2026-11-12--general-ir-rate-bravais-stage1.md`,
SHA256 `922162b8dc695ea1d5843d6b875389f30d89bcd3ff144b2e797d7be9cf894b1c`.
Charter `theory/GENERAL_IR_RATE_BRAVAIS_GATE.md` (frozen `5eb6da9`;
file at base SHA256 `c3d94d73…ef12`, status line updated at `f301c21`).
Context documents: the general-rate charter with Amendments 1–4, its three
stage reports, the carrier charter with Amendment 1 and its Stage A report
(the texts the candidate adapts), and the IR-corona manuscript at tag
`ir-corona-v3` with identifying strings replaced (same anonymised file as
the Grok review, `reports/reviews/2026-11-12-general-ir-rate-grok/ir-corona-anon.tex`,
SHA256 `70b74038…28f9`; `papers/ir-corona/ir-corona.tex` unchanged since
the tag). The carrier charter and the Stage A report are attached as
copies in this folder (`*-anon.md`) with the internal name of regime R2
withheld (two lines, nothing else changed; `diff` against the originals at
`24e1965`). No earlier review is attached.

Objective: decide whether Stage 1 establishes that the general-rate
theorem and the proved part of carrier Stage A hold on an arbitrary Bravais
lattice, with only the stated replacements. Expected result: verdict with
located objections. Maximum rounds: one. Closes with: the written report.
No automatic repair/re-review loop, no promotion.

---
Revisa adversarialmente una adaptación matemática. No tienes herramientas,
repositorio ni web; trabaja solo con los documentos adjuntos. No
presupongas que sean correctos: son borradores de un autor, no fuentes.

Material. El documento a juzgar es el informe
`2026-11-12--general-ir-rate-bravais-stage1.md` («Etapa 1»), que ejecuta
la Etapa 1 del contrato `GENERAL_IR_RATE_BRAVAIS_GATE.md`. Se apoya en dos
resultados previos, adjuntos como contexto:
- B1: contrato `GENERAL_IR_RATE_GATE.md` con enmiendas 1–4 y sus informes
  de etapas 0–1, progreso de la etapa 2 y término principal (escritos para
  paseos en Z^d, d en {2,3});
- B2: contrato `IR_CARRIER_DICHOTOMY_GATE.md` con su enmienda 1 y el
  informe de la etapa A.
Los informes citan un manuscrito previo (`ir-corona-anon.tex`, caso Z^3).

Afirmación a juzgar. Toda utilización de Z^d en las etapas 1–2 de B1 y en
la parte demostrada de B2 es una de las U1–U14 del inventario de la
Etapa 1, y cada una se traslada a una red de Bravais L de R^d, d en {2,3},
con regiones bola euclídea y u vector primitivo de la red dual L* en la
dirección de xi_*, mediante los reemplazos indicados; solo cambian
constantes (Sec. 4) y se excluyen finitos N (U6). Las hipótesis no
cambian. No se juzga aquí si B1 y B2 son correctos en Z^d: tómalos como
base, y si ves un error en ellos anótalo aparte, sin que decida el
dictamen sobre la adaptación.

Comprueba en particular:
1. Completitud del inventario: ¿hay algún paso de B1 o B2 que use Z^d
   (o su toro, su dual, sus planos, la normalización de Fourier, conteos
   de sitios, simetrías de Z^d, coordenadas enteras) y que no figure en
   U1–U14? Si lo hay, ¿se traslada o falla?
2. Sec. 0: u primitivo en L* si y solo si u.L = Z; cada plano corta L en
   una clase de Lambda_0; covol(Lambda_0) = covol(L)|u|; caracteres
   triviales en Lambda_0 de la forma omega^(u.x); criterio de trivialidad
   por la componente en el plano. Comprobaciones con la red triangular y
   la BCC.
3. U6: condición para que la banda g(Np) quepa en una zona,
   N > 1/(pi lambda_1(L*)), y que no afecta a la forma limsup.
4. Sec. 2: lema de convexidad (traslación en T_L), desplazamiento de
   contorno, test de Schur con conteos en L.
5. Sec. 3: cola libre en L; sumas por capas con Poisson en clases de
   Lambda_0 (modo cero 1/(covol(L)|u|), frecuencias no nulas en
   2 pi Lambda_0^*, r_0, suma de inversos al cubo para m <= 2);
   ensamblaje con dmu_L.
6. Sec. 4: Z_N(L), c_r(L), k_A(L), k_B(L), el coeficiente c(L) y la
   cancelación de las potencias de covol(L); la comprobación contra Z^3
   (c_r = sqrt(3465)/(64 pi^2), Z_N = 64/(3465 pi^2 N^3), k_A, k_B).
7. Sec. 5: la parte demostrada de B2 en L (fases, sumas de profundidad
   con sigma complejo, promedios); que la celda abierta sigue abierta.
8. Sec. 6: si las tres observaciones son correctas (no es un cambio de
   coordenadas; elección de red y copias plegadas; la admisibilidad no
   está demostrada en la clase general de B1).
9. Que el informe no afirma más de lo que prueba, y que el veredicto
   (resultado (b), corolario) está justificado.

Salida: dictamen global PASS / REPAIR_REQUIRED / REJECTED para la
adaptación. Cada objeción debe citar documento y sección, decir si es
error fatal, reparación necesaria, hipótesis que falta o cuestión de
exposición, y dar la derivación o el contraejemplo cuando sea decisiva.
Si no puedes verificar un paso, márcalo NO_VERIFICADO; no lo conviertas
en PASS por plausibilidad ni añadas hipótesis para salvarlo. Lista aparte
lo que sí has rederivado. No se pide juzgar la originalidad.

Presupuesto: una ronda. Cierre: informe escrito con dictamen y
obligaciones pendientes.
---
