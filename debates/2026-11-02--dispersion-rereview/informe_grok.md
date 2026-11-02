<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 51200fa1c4312f773ba8b67f5b5c78d54a12e3e47bcf4244e8f203e542c71d14
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-02T18:07:20Z  fin: 2026-11-02T18:18:11Z
documento: /home/adnac/qca-causal-cones/theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md ; último commit observado: a7ff5b7 ; sha256 de la copia enviada 6df09e81fae231ebbb00d19de546298559d333d33e965c95a1aa6027842231ea
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices-review.md ; último commit observado: 4a45280 ; sha256 de la copia enviada 483b29e4848d3002fcaaa9fcccdf45c6325a9c213a706eb402b97e5b050880f6
documento: /home/adnac/qca-causal-cones/debates/2026-11-02--dispersion-review-grok/repair.diff ; último commit observado: 4a45280 ; sha256 de la copia enviada 32389d42dcf3b712fa0a81a2e4532f93b2b3164fb100795c00fa102e7b1151fd
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 4a45280 ; sha256 de la copia enviada fe14d132ee6d2308ecabb089d39aecca37f4bfec167e03d97a65f8ccdeb3a877
documento: /home/adnac/qca-causal-cones/scripts/verify_dispersion_corrections_gate.py ; último commit observado: 4a45280 ; sha256 de la copia enviada b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e
entrada_grok.txt sha256 f4976edfcc8a722b2257ce316528adf2d4086ee98e0f9dfcbb7a5d50d5d3fb6d
respuesta sha256 d139b3fe1b3e7494ff767d10fb1cdb21ffb3295336cc1a61463546d0e359ab24
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias.

## R1 — PASS

Con \(0<a<1\), \(|\beta_0|=\sqrt3\,(1-a^2)/(6a)\) y \(|\beta_3|=\sqrt3\,|2a^2-1|/(3a)\). En la esfera, \(|n_1 n_2 n_3|\le 1/(3\sqrt3)\), con igualdad en \(|n_i|=1/\sqrt3\). Por tanto \(\beta\) tiene en todo punto el signo de \(\beta_0\) si y solo si \(|\beta_3|/(3\sqrt3)<|\beta_0|\), es decir \(\beta_3^2/27<\beta_0^2\). Eso equivale a \(|2a^2-1|<(3\sqrt3/2)(1-a^2)\).

Para \(a^2\le 1/2\) la desigualdad es estricta en todo \((0,1/2]\). Para \(a^2\ge 1/2\) queda \(a^2<(2+3\sqrt3)/(4+3\sqrt3)=(19-6\sqrt3)/11\). En el umbral, \(\beta\) se anula en el octante opuesto a \(\beta_0\) y no toma el signo contrario; por encima sí toma ambos signos. El «si y solo si» estricto del informe es el correcto.

El signo de \(\beta_0\) es el del cúmulo en la rama superior (signo superior en \(+\pi/4\), Sec. 1) y se invierte en la rama inferior: \(\phi\) aporta \(\beta_0\) y \(\omega\) aporta \(\beta_3\), de modo que la rama inferior lleva \(-\beta_0+\beta_3 n_1 n_2 n_3\). La frase nueva de la Sec. 3.3 coincide con la tabla y con la Sec. 3.4.

De las formas cerradas,
\[\beta_0^2-\beta_3^2/27=(11a^4-38a^2+23)/(324a^2).\]
El numerador, como cuadrática en \(u=a^2\), tiene discriminante \(432\) y raíces \((19\pm 6\sqrt3)/11\); en \(0<a<1\) solo \(a=\sqrt{(19-6\sqrt3)/11}\). El denominador \(324a^2\) no cambia de signo en \((0,1)\). En \(a=1/2\) el numerador vale \(227/16>0\); en \(a=19/20\) vale \(-373669/160000<0\).

El registro nuevo no compara coeficientes con ese polinomio: toma el hueco calculado, exige una sola raíz del numerador en \((0,1)\), anulación en ese \(a\) y signos \(+1\) y \(-1\) en \(1/2\) y \(19/20\), para los dos cúmulos. Con una sola raíz y esos dos signos, el hueco es positivo exactamente por debajo del umbral. Eso es lo que enuncia la etiqueta.

## R2 — PASS

La tabla deja \(\beta\) de L5a igual a \(+(\sqrt3/3)\,n_1 n_2 n_3\) y el de cada bloque de L5b igual a \(\pm(\sqrt3/3)\,n_1 n_2 n_3\), con el mismo \(\alpha\). Hay un solo bloque que comparte \(\beta\) y \(\alpha\); el otro solo cambia el signo de \(\beta\). La frase nueva dice eso, y el inciso «hasta orden relativo \(t^2\)» queda en L6d con L6f.

El verificador construye `L5b[+i]` y `L5b[-i]`, registra que sus \(\alpha\) coinciden y, en Hf, empareja L5a solo con `L5b[+i]`. L6d y L6f se comparan por igualdad de \(\beta\) y \(\alpha\). La frase coincide con ese listado y con el par que la reparación R2 ya había identificado.

## R3 — PASS

El predicado es `not undecided`, y esa lista se llena. Puede fallar.

En cada fila numérica el signo es el retorno de `P.positive` sobre \(\alpha_0\); si ese retorno es `None`, la fila queda indecisa. En L3s4 (ambos cúmulos) el signo de tabla es `None` en cuanto hay raíz, y la fila solo cuenta como decidida si `alpha0_signs` cubre \((0,1)\): empieza en \(0\), termina en \(1\), los extremos contiguos coinciden y cada signo está en \(\{1,-1\}\). Los cortes salen de las raíces reales del numerador y el registro compañero ya exige que su número iguale la cuenta de Sturm y que no haya polos. Cero, como en L1, cuenta como signo decidido.

## R4 — PASS

El diff añade el umbral de la Sec. 3.3, restringe el par L5a–L5b, sustituye el predicado constante del registro Hd y añade dos registros (uno por cúmulo). El salto \(79\to 81\) coincide con esos dos registros; no he ejecutado el verificador.

No cambia ninguna entrada de la tabla, ningún coeficiente ni los veredictos Hd, He o Hf. El estado sigue siendo `CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN`, con la revisión de las reparaciones pendiente. El umbral entra en el apartado de signo del contrato (Sec. 3, ítem 4); no hay diccionario observacional ni afirmación sobre el universo.

**Reparaciones obligatorias:** ninguna.
