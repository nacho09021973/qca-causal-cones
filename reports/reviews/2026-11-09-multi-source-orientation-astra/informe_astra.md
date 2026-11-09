<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.167.0)
inicio: 2026-11-09T13:32:58Z  fin: 2026-11-09T13:39:23Z
documento: /home/ignac/qca-causal-cones/theory/MULTI_SOURCE_ORIENTATION_GATE.md ; último commit observado: dd9ab5c ; sha256 de la copia enviada 3c8239b39d034d89efc8e65a9b61f3e1530c3cc519261876e8b93eb4e15c71e2
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--multi-source-orientation.md ; último commit observado: 630bd6e ; sha256 de la copia enviada bfef9cc733ebe30def44b81e81ce7c9e3d6b6e3fc8a3db107f148044ac7d690e
documento: /home/ignac/qca-causal-cones/scripts/verify_multi_source_orientation.py ; último commit observado: 2464e1a ; sha256 de la copia enviada fb277dff228ca8dedaf44dfdc2e44d19b30a15ddbdc60e28a0684f7a3e4c92c1
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--multi-source-orientation.txt ; último commit observado: 630bd6e ; sha256 de la copia enviada fc850af7390c4ea9d364af737862f9662b69db4236816b4b7ebf4dfa57e24123
documento: /home/ignac/qca-causal-cones/investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md ; último commit observado: 3a0ad92 ; sha256 de la copia enviada f474cef10cf6c1304650eddb432afe2c8e68721bd3a596fe42addbf0e83ac2d0
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--dispersion-data-comparison.md ; último commit observado: 81cac4e ; sha256 de la copia enviada 160e0574983c713a89523e79caa6ea31bff7d764d0180feebc22abf57c39439c
entrada_astra.txt sha256 aa198a0e28a3e63e245ca812641a7a83ab82418c511c0707feacad734ee4f742
respuesta sha256 72925f5a14f08bc321c0a24535f70a8bbd22840b9f10d19d69cb75f7ff684511
-->

**Veredicto: reparación necesaria.** La cancelación algebraica y la construcción geométrica se sostienen para direcciones del **vector de onda**, hasta orden 2. Su traslado a las direcciones observadas de propagación tiene un hueco sustancial. El resultado D2 sigue siendo **OPEN**. Los umbrales de L3s4 se sostienen como criterios suficientes, condicionados a los coeficientes y diccionarios suministrados, pero la tabla atribuye demasiado a su incumplimiento.

He derivado a mano las identidades siguientes e inspeccionado el script y el registro. No he ejecutado código ni comprobado las fuentes originales, los commits o las dispersiones completas. El recuento 4/5 no interviene en el veredicto.

**Cancelación y escape geométrico.** Sea
\[
\varepsilon=c_0 k[1+\beta(n)t+\alpha(n)t^2+O(t^3)],
\qquad t=k\ell,\quad |n|=1.
\]
Entonces
\[
\frac{\nabla_k\varepsilon}{c_0}
=n(1+2\beta t+3\alpha t^2)
+t\nabla_S\beta+t^2\nabla_S\alpha+O(t^3),
\]
y, por ortogonalidad entre las partes radial y tangencial,
\[
\frac{|\nabla_k\varepsilon|}{c_0}
=1+2\beta t+
\left(3\alpha+\frac12|\nabla_S\beta|^2\right)t^2+O(t^3).
\]
La identidad del informe es correcta.

Con los coeficientes del script,
\[
\beta=\pm\frac{n_1n_2n_3}{\sqrt3},\qquad
\alpha=-\frac{\sigma_2}{18}-\frac{n_1^2n_2^2n_3^2}{6}.
\]
En \(n_3=0\),
\[
\nabla_S\beta=\pm(0,0,n_1n_2/\sqrt3),\quad
|\nabla_S\beta|^2=\frac{n_1^2n_2^2}{3},\quad
3\alpha=-\frac{n_1^2n_2^2}{6}.
\]
La cancelación es exacta. Las permutaciones de coordenadas y el cambio global de signo de \(\beta\) la preservan. También incluye los ejes.

La construcción para tres direcciones admite todos los casos degenerados. Elíjase un normal \(e_3\) perpendicular a las dos primeras; si son paralelas o antiparalelas, cualquier normal perpendicular a su recta sirve. Para la tercera dirección \(w\):

- si \(w\not\parallel e_3\), tómese \(e_1\parallel e_3\times w\);
- si \(w\parallel e_3\), cualquier \(e_1\perp e_3\) sirve.

Completando una base orientada, las dos primeras tienen tercera coordenada cero y la tercera tiene primera coordenada cero.

Además, puede completarse a mano el argumento de que el máximo **genérico** es tres. Entre cuatro direcciones asignadas a tres planos debe haber una pareja en un mismo plano. Su normal queda fijado. Las otras dos deben satisfacer una condición adicional: o sus proyecciones sobre ese plano son ortogonales, si ocupan los otros dos planos, o el normal del plano que ambas generan es perpendicular al primero. Son condiciones algebraicas excepcionales; una cuádrupla genérica no las satisface. Esto no decide la cuádrupla concreta de GRBs.

Nada de ello demuestra cancelación a todos los órdenes. «Exacta» califica aquí la identidad del coeficiente de orden 2, no la dispersión completa.

Las objeciones, ordenadas por gravedad, son las siguientes.

1. **Dirección de onda frente a dirección de propagación: afecta a §§1–3 y al escape D1.**

   El propio cálculo muestra el problema. En \(n_3=0\), la velocidad tiene componente normal
   \[
   v_3/c_0=\pm t\,n_1n_2/\sqrt3+O(t^2).
   \]
   Por tanto, colocar el vector de onda en el plano no coloca, en general, el rayo en ese plano.

   Sea \(r=v/|v|\) la dirección de propagación. A primer orden,
   \[
   r=n+t\nabla_S\beta(n)+O(t^2),\qquad
   n=r-t\nabla_S\beta(r)+O(t^2).
   \]
   Sustituyendo en la expansión de la rapidez a dirección de propagación fija:
   \[
   \frac{|v|}{c_0}
   =1+2\beta(r)t+
   \left(3\alpha(r)-\frac32|\nabla_S\beta(r)|^2\right)t^2
   +O(t^3).
   \]
   En \(r_3=0\), resulta
   \[
   \frac{|v|}{c_0}
   =1-\frac23r_1^2r_2^2t^2+O(t^3).
   \]
   **La cancelación desaparece**, salvo en los ejes. Cambiar de \(t\) a energía no modifica este coeficiente en el plano, porque allí el término lineal se anula.

   Para direcciones de propagación, anular simultáneamente los órdenes 1 y 2 exige entonces ejes coordenados. Dos direcciones arbitrarias no pueden convertirse simultáneamente en ejes: deben ser paralelas o perpendiculares. Las posiciones suministradas dan, mediante el producto escalar esférico, un producto aproximado de \(0.44\), incompatible con ambas posibilidades.

   **Reparación:** distinguir explícitamente los dos enunciados. El escape geométrico demostrado corresponde a vectores de onda. No sostiene por sí solo `ESCAPES_ALL_SOURCES` hasta orden 2 para fuentes observadas. Si el diccionario identifica artificialmente ambas direcciones, debe declararse esa hipótesis y limitarse a ella la conclusión. Esta objeción tampoco demuestra exclusión bajo H_min: una corrección cuadrática residual puede ser demasiado pequeña para excluir.

2. **Incumplir el criterio de L3s4 no demuestra “no excluida”: §1, tabla, y §2.**

   Escribiendo \(f(a)=B-M\), una fuente proporciona
   \[
   \sup_R\frac{\ell_{\max}(R)}{\ell_P}
   =\frac{E'_P}{2E_{\rm QG,1}f(a)},\qquad
   E'_P=\hbar c/\ell_P.
   \]
   Por tanto,
   \[
   f(a)>\frac{E'_P}{E_{\rm QG,1}}
   \]
   es el criterio de exclusión robusta para toda orientación **con esa fuente sola**. Si falla, varias fuentes todavía podrían proporcionar una exclusión conjunta. Tampoco implica que todas las orientaciones estén permitidas.

   Hay además errores de clasificación por redondeo:

   - Entre \(0.7731\) y la raíz indicada \(0.7731485185\), ambos clusters todavía satisfacen el criterio D1.
   - Entre \(0.7826\) y \(0.7826218041\), el superior todavía lo satisface.
   - La tabla deja sin clasificar correctamente bajo D2 el intervalo amplio desde \(a=0.7826\) hasta aproximadamente \(a=0.88460\). La franja próxima a \(a^2=x_c\) no está en la fila \(0.7731\leq a<0.7826\).

   **Reparación:** usar las raíces definidas por ecuaciones como fronteras; presentar sus decimales como aproximaciones. Sustituir «not excluded» por «este criterio uniforme de una fuente no decide», salvo que exista otro argumento. Organizar D2 mediante su propia frontera \(a_{\rm D2}\).

3. **El diagnóstico de muestreo no respalda la explicación ofrecida del fallo D2: §2, parte B.**

   Está correctamente identificado como muestreo sin veredicto. Sin embargo, comparar \(0.009915\) con una variación «de hasta aproximadamente \(0.02\)» no aporta evidencia de escape dentro de las cajas angulares reales.

   Puede obtenerse a mano una cota más estrecha. Para \(p(n)=n_1n_2n_3\),
   \[
   |\nabla_Sp|\leq|\nabla p|
   =\sqrt{\sigma_2}\leq1/\sqrt3.
   \]
   Una variación \(|\Delta\theta|,|\Delta\phi|\leq0.5^\circ\) admite un camino esférico de longitud como máximo \(\sqrt2\,\pi/360\). Por ello, para cualquier rotación,
   \[
   |\Delta p|
   \leq\frac{\pi}{360}\sqrt{\frac23}
   \approx0.00713.
   \]
   Aceptando el registro del muestreo, **ninguna de las orientaciones muestreadas puede convertirse en escape exacto mediante esas variaciones angulares**: en cada una queda alguna fuente con \(|p|\gtrsim0.00279\).

   Esto no excluye otras orientaciones: el mínimo muestreado es una estimación superior del mínimo global, nunca una cota inferior.

   **Reparación:** conservar el diagnóstico, pero retirar esa justificación de plausibilidad. La causa científica del cierre fallido no está determinada: puede intervenir la geometría, la sobreestimación intervalar o el presupuesto.

4. **La rama y poda tiene una lógica conservadora correcta, pero no constituye una implementación certificada: contrato §2 y script B.**

   El umbral es correcto:
   \[
   \ell_{\max}<\ell_P/2
   \iff |\beta_i|>2E'_P K_i
   \iff |p_i|>\delta_i=2\sqrt3\,E'_P K_i.
   \]

   Para cada caja de orientaciones, el código poda si encuentra una fuente que viola el umbral para todas las posiciones encerradas y todas las orientaciones de la caja. Esto es suficiente para
   \[
   \forall R\;\forall(s_1,\ldots,s_4)\;\exists i:
   |p(R^Ts_i)|>\delta_i.
   \]
   Las cajas cartesianas de `source_box` agrandan los conjuntos angulares y pierden correlaciones, lo que dificulta la poda, pero no introduce por sí mismo una falsa exclusión.

   Dos límites deben quedar claros:

   - Los ±0.5° representan una **hipótesis de redondeo al entero más próximo**, no una incertidumbre astrométrica demostrada por el mero formato de la tabla.
   - El margen de error de libm y el tratamiento de constantes no están certificados. El script podría devolver `CERTIFIED` sin satisfacer las garantías exigidas por el contrato.

   **Reparación:** describir el resultado como intento intervalar condicionado, sin certificación. El resultado actual **OPEN es correcto**: no confirma ni refuta Hm2 y no demuestra ausencia de una cota menos fuerte.

5. **La asignación de signos a los clusters no se verifica en los documentos aportados: §2 C.**

   La aritmética de los umbrales es correcta **si** el cluster superior tiene \(\beta>0\) y el inferior \(\beta<0\) cuando \(B>M\). Pero el script introduce esas asociaciones como cadenas de texto; no las deriva. Los adjuntos tampoco incluyen las fórmulas espectrales de ambas ramas que permitan comprobar qué significa «superior».

   **Reparación:** incluir las expresiones de \(\beta\) de ambos clusters y su convención de rama. Hasta entonces, la correspondencia entre nombre del cluster y signo queda `[UNVERIFIED]`; los umbrales por signo sí se sostienen.

6. **Hay discrepancias menores entre script, registro e informe: §5 y partes B–C.**

   - La función de diagnóstico anuncia en su documentación \(\max_i|p_i|/\delta_i\), pero calcula \(\max_i|p_i|\). El informe y el registro describen correctamente lo calculado.
   - `boxes_processed` suma el último lote **antes** de comprobar el presupuesto y salir. Los 4 721 034 no son todos cajas evaluadas; incluyen el lote que provoca la salida.
   - El PASS C comprueba solamente que aparece una raíz admisible por cluster. No comprueba directamente la desigualdad en todo el intervalo, los signos espectrales, el umbral D2 o L3.
   - El script no calcula la cota de L3, aunque su cabecera la incluye entre las tareas de C.

   **Reparación:** ajustar documentación, nombres de contadores y atribución de verificaciones. Las derivaciones escritas pueden justificar resultados que el script no comprueba, pero deben identificarse como tales.

**Derivación de los umbrales de L3s4.** Aceptando la estructura angular suministrada, el término variable recorre \([-M,M]\): el producto \(n_1n_2n_3\) alcanza ambos extremos \(\pm1/(3\sqrt3)\), por AM–GM. De ahí
\[
\inf|\beta|=\max(B-M,0).
\]
Para \(a^2<x_c\), la positividad uniforme elimina cualquier dependencia de la orientación de una fuente.

La función relevante es
\[
f(a)=
\begin{cases}
\displaystyle\frac{\sqrt3/6-1/9}{a}
+\left(\frac29-\frac{\sqrt3}{6}\right)a,
& a^2\leq\frac12,\\[6pt]
\displaystyle\frac{C}{a}-Da,
& a^2\geq\frac12,
\end{cases}
\]
donde
\[
C=\frac{\sqrt3}{6}+\frac19,\qquad
D=\frac{\sqrt3}{6}+\frac29.
\]
Ambas ramas son estrictamente decrecientes. Además,
\[
f(1/\sqrt2)=\frac{\sqrt6}{12}\approx0.204124,\qquad
f(\sqrt{x_c})=0,\qquad
x_c=\frac CD=\frac{19-6\sqrt3}{11}.
\]
Esto demuestra, sin depender del PASS C, la unicidad de las raíces y el lado de la desigualdad.

Para cualquier umbral \(q<0.204124\), la raíz pertinente es
\[
a(q)=\frac{\sqrt{q^2+4DC}-q}{2D}.
\]
Con los valores suministrados,
\[
q_{\rm super}\approx0.110990,\qquad
q_{\rm sub}\approx0.122089.
\]
Las raíces registradas \(0.7826218041\) y \(0.7731485185\) son compatibles con estas ecuaciones; no he reproducido sus diez decimales mediante ejecución. El intervalo conservador \(0<a<0.7731\) sí queda cubierto para ambos signos, condicionado a los valores observacionales declarados.

Bajo D2,
\[
q_2=2E'_P(7\times10^{-35})\approx1.70925\times10^{-15}.
\]
El alcance exacto del criterio es
\[
0<a<a(q_2),
\]
no simplemente \(a^2<x_c\). La anchura excluida del argumento junto al extremo satisface
\[
x_c-a(q_2)^2
=\frac{\sqrt{x_c}}{D}\,q_2+O(q_2^2)
\approx2.96\times10^{-15}.
\]
Es una franja pequeña pero de anchura positiva. La expresión «casi todo» debe entenderse informalmente; no significa «salvo un conjunto de medida cero». Para localizarla hay que usar la expresión exacta de \(x_c\), no su decimal redondeado.

**L3 y sección 3.** El argumento de compatibilidad D1 de L3 es correcto dentro del orden considerado. Con \(x_i=n_i^2\), \(\sum x_i=1\),
\[
\sigma_2\leq\frac13,\qquad |\alpha|\leq\frac1{54}.
\]
Por tanto,
\[
\ell_{\max}(R)\geq
\frac{\sqrt{27}\,\hbar c}{6.9\times10^{11}\ {\rm GeV}}
\approx9.2\times10^7\ell_P.
\]
La segunda fuente tiene menor sensibilidad cuadrática según los datos adjuntos; combinar ambas no reduce la cota por debajo de ese mínimo. Existe, para cada orientación y cada \(\lambda\in[1/2,2]\), un intervalo de longitudes compatible con H_min y D1. Eso no significa que toda longitud admitida por H_min esté permitida.

En cambio, «nada supera \(c\)» es una afirmación global sobre la dispersión: no se deduce de \(\alpha\leq0\). El padre remite a una demostración no adjunta; aquí queda `[UNVERIFIED]`.

La sección 3 puede conservar la exclusión **de la subfamilia** L3s4 indicada y la compatibilidad D1 de L3. Debe corregir el escape de las fuentes observadas y evitar presentar estos resultados como una selección general entre reglas con o sin excitaciones superlumínicas.

**Alcance que aceptaría:** cancelación hasta orden 2 y escape de tres direcciones de onda; D2 de L5a/L5b/L4 **OPEN**; exclusión uniforme de L3s4 bajo las hipótesis declaradas y las desigualdades exactas anteriores, dejando condicionada la identificación de clusters; compatibilidad de L3 con H_min bajo D1 al orden analizado. No aceptaría escape físico de tiempo de vuelo hasta orden 2 sin resolver la distinción onda–rayo, cancelación a todos los órdenes, ni conclusiones de permiso obtenidas únicamente porque falla un criterio suficiente de exclusión.