# Independent Grok review: reconciled IR-corona manuscript

User authorization (2026-11-12, «dile a Grok que lo revise»): review by Grok,
a model family different from the one that merged and read the text.
One sealed round via revision-ciega; herramientas 7d111a1.
Document sent: ir-corona-anon.tex in this folder, which is
papers/ir-corona/ir-corona.tex at commit b5cc166 (tag ir-corona-v2) with
five identifying strings replaced (author, address, e-mail, repository name
and URL); nothing else differs (`diff` shows those five lines only). No earlier review, no reconciliation
report and no verdict is attached.

Objective: decide whether the manuscript, as it stands after merging two
separately repaired versions, is mathematically correct and internally
consistent. Expected result: a verdict with located objections.
Maximum rounds: one. Closes with: the written report. No automatic
repair/re-review loop, no promotion.

---
Revisa adversarialmente el manuscrito LaTeX adjunto, completo. No tienes
herramientas, repositorio ni web: trabaja solo con el texto. No presupongas
que sus afirmaciones sean correctas; es un borrador, no una fuente.

Contexto mínimo: el texto resulta de fusionar dos versiones que habían sido
reparadas por separado. Por eso interesa tanto la corrección matemática como
la coherencia interna: definiciones, notación, constantes y pasos de prueba
que puedan haber quedado duplicados, contradictorios o huérfanos.

Afirmaciones que debes juzgar:
A. Teorema «Explicit upper bound»: T_N <= 9 N^4 e^{-JN} y delta <= D_B <= 4 T_N.
B. Teorema «Regional rate»: propiedades de I, minimizador único v_*, la
   forma cerrada de cosh^2 t_*, J < K_* < log 4 y la cota (d).
C. Teorema «Admissibility» y el lema de operaciones de un solo sitio.
D. Teorema «Leading asymptotics»: L = e^{-K_* N} N^{-13/2} (C(theta_N) +
   O(N^{-1/2})) con C dado por (eq:C), y no anulación de C.

Comprueba en particular, rehaciendo las cuentas:
1. Sección 2: saltos, det S = 1, dispersión, identidad (eq:SOS), soporte.
2. Lema de la elipse, lema del radio espectral y lema de potencias; el
   desplazamiento de contorno (eq:tilt) y las constantes de A.
3. Convexidad de Phi, alcance del supremo de Legendre y unicidad de v_*.
4. Lema del símbolo inclinado: (a)–(e), en especial las identidades de
   medio periodo (b), la analiticidad y el desarrollo de lambda(eta) en (d),
   y el paso de compacidad de (e). ¿Está controlada la rama recíproca
   lambda^{-1} en el ensamblaje?
5. Coordenadas por planos: theta_N, paridad (-1)^{j+j'}, perfiles exactos.
6. Lema «Free tail» y la constante R_0(w_*).
7. Lema «Depth sums»: transformada, sumas 1/720 y 1/48, Gamma-barra y
   epsilon_±.
8. Lema «Layers» (a)–(d) y su prueba, que es la parte fusionada:
   - sumación de Poisson en cada plano, cota de los términos m != 0 por la
     variación total de la tercera derivada, y uniformidad en eta y theta_N;
   - prefactores 16 pi/sqrt3 y 32/sqrt3;
   - parte de Bob: descomposición r = N^{-3/2} R_0(w_*) + rho, cota de rho,
     recuento de sitios y definición del vector fila E_B;
   - fases cerca de pi u en (c);
   - (d): condición sobre r_0 y cota C N^{-4}.
   ¿Son compatibles entre sí todos los pasos y las condiciones sobre r_0?
9. Ensamblaje (Teorema T): tres reemplazos y sus costes, cancelación de
   fases cerca de pi u, la constante K, el recuento de la potencia 13/2 y
   el presupuesto de restos.
10. No anulación: ¿basta el margen |l_0|(Gamma-barra - eps_+) > eps_- |l_pi|?
    ¿Son coherentes la Tabla 1 y la tabla de l_0, l_pi del apéndice con las
    definiciones x_0 = R~^dagger M_B P chi, x_pi = R~^dagger M_B P-barra chi?
11. Reducción (eq:Lexp): signos de los cuatro funcionales y la cota
    N^{-17/2} para el término con a_c.
12. Que resumen, introducción, discusión y apéndice no afirmen más de lo
    que prueban los teoremas (alcance de «infrared-admissible», carácter
    puramente asintótico, qué está formalizado en Lean y qué no).

No se pide certificar originalidad ni comprobar la bibliografía contra las
fuentes; sí puedes señalar afirmaciones bibliográficas que el propio texto
haga de forma incoherente.

Salida: dictamen global PASS / REPAIR_REQUIRED / REJECTED y un dictamen por
cada bloque A–D. Cada objeción debe citar sección, lema o ecuación, decir
si es error fatal, reparación necesaria, incoherencia de la fusión o
cuestión de exposición, y dar la derivación o el contraejemplo cuando sea
decisiva. Si no puedes verificar un paso, márcalo NO_VERIFICADO; no lo
conviertas en PASS por plausibilidad ni añadas hipótesis para salvarlo.
Lista aparte lo que sí has rederivado.

Presupuesto: una ronda. Cierre: informe escrito con dictamen y
obligaciones pendientes.
---
