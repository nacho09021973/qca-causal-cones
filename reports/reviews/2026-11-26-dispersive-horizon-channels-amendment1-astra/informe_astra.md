<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.2-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-26T16:34:32Z  fin: 2026-11-26T16:37:32Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-channels-amendment1-astra/amendment1.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 2f8ca47e70f0a5490b1fd202a67ebcfe5d56cd32e9e16a50e70dab28a210232c
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-channels.md ; último commit observado: 6d45537 ; sha256 de la copia enviada 5b41e20462cde535b191a463f4ecfc1fd009142fb65af1b0c3d465145adcddca
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-channels-astra/informe_astra.md ; último commit observado: 49ebac2 ; sha256 de la copia enviada 43fbf0abe27e3cd0a24538c1fe7e83e3e1205df3fd14c3bb371d0a2544e08ece
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_channels_amendment1.py ; último commit observado: ea3067a ; sha256 de la copia enviada 37aacbb5a3680fa3de3c74660b2fccfcd507e7b04c7f91b1b2b105c3416ebdd6
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_channels.py ; último commit observado: a5b9be3 ; sha256 de la copia enviada 08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-channels-amendment1-run.txt ; último commit observado: 6d45537 ; sha256 de la copia enviada 7c3bbe83ae9e6b23452cdc6fa7bdde984faedf28311e96e88f58369521c581fb
entrada_astra.txt sha256 965c89148d6c700fdac2e031237d91b5d48a1f2a7624c85abd33033e6ab7fe3d
respuesta sha256 8297e37abec9a9f69cd798e5d47ac47e7e12d8ee5db16cea7ae2e9d079844b0d
-->

**Veredicto global — PASS.** Con las exigencias del contrato citadas en el documento 3, procede `CHANNELS_CLASSIFIED`. La enmienda entrega el recuento por arcos, los cuatro recintos críticos, la identificación de las doce raíces de cada medio en \(z_0\) y los ocho vectores propagantes normalizados. En toda la ventana \(I\) hay exactamente un canal hacia la derecha en cada medio. Queda una corrección menor en la descripción de las precisiones, sin obligación contractual abierta que justifique `OPEN_AFTER_CHANNEL_ANALYSIS`.

| Punto | Veredicto | Resultado |
|---|---|---|
| 1. C2, recuento entre umbrales | PASS | K verifica dieciséis muestras regulares. La continuación de raíces y el análisis local de los cruces justifican el recuento en los arcos abiertos. |
| 2. Entregables C3–C5 | PASS | Z entrega los cuatro recintos. E identifica los evanescentes y los propagantes. N registra las doce componentes de cada modo normalizado. |
| 3. Valores publicados y procedencia | PASS | V fija los valores solicitados y H compara ambos hashes completos. Hay límites concretos a lo que comprueban algunos predicados. |
| 4. Determinante con perfil variable | PASS | La atribución de la prueba es correcta y G se presenta como contraste exacto en seis sitios. |
| 5. Coherencia del texto | REPAIR_REQUIRED | Corrección editorial. Los números de las tablas concuerdan con el registro. La anchura publicada del intervalo de \(\tau\) confunde precisión interna e impresa. |
| 6. Condición de cierre | PASS | \(z_0\in I\), C1–C5 completos y se satisfacen ambos requisitos sobre los canales hacia la derecha. |

He inspeccionado el código y el registro suministrados. Las derivaciones siguientes son manuales. De la ejecución consta en el documento 6 el resultado 61/61, 53/53 y 63/63, con salida 0. La reproducción independiente, los bytes en Git, la anterioridad efectiva del commit y el carácter único de la ejecución quedan **[UNVERIFIED]**.

### 1. Los ocho arcos y sus extremos

La parametrización racional con \(s=1/50\) da exactamente \(p_1=(2499+100i)/2501\) y \(\arg p_1=2\arctan(1/50)\). Hay una comprobación sencilla de su posición. Ambos puntos están en el primer cuadrante del círculo y
\[
0<\Im p_1=\frac{100}{2501}<\frac1{20}<\Im z_c^*.
\]
Por tanto \(0<\arg p_1<\delta\). A su vez, \(\Re z_c^*>9/10>3/5=\Re z_0\) da \(\delta<\arg z_0<\pi/2\). En la fórmula de \(z_c\), cambiar \(S=\sin k\) por \(-S\) conjuga el valor. Cambiar \((C,S)\) por \((-C,-S)\) lo niega, por la imparidad de \(g\) y la paridad de \(g'\). Estas operaciones preservan también los cuatro puntos de colisión. Las imágenes de los dos puntos elegidos ocupan exactamente un arco cada una. K hace el cálculo en los ocho, en ambos medios.

El grado 12 de \(H\) cubre el punto omitido por la carta \(\tau=\tan(k/2)\), pues su coeficiente principal es \(h(\pi)\ne0\). La libertad de cuadrados asegura raíces simples. En cada raíz real, el polinomio de signo de K tiene el signo de \(h_kh_\omega\), de modo que \(\operatorname{sign}v=-\operatorname{sign}N\). El gcd excluye los ceros que impedirían esa decisión. K contrasta las ternas completas, además de la diferencia derecha menos izquierda. En el interior obtiene \((6,2,4)\) cerca de \(\pi\mathbb Z\) y \((4,1,3)\) en los otros cuatro arcos. En el exterior obtiene \((4,1,3)\) en los ocho.

La extensión al arco entero es una prueba escrita. Por C3, dentro del arco cada raíz sobre el círculo tiene \(h_kh_\omega\ne0\). La función implícita la continúa con velocidad de signo constante. La compacidad del círculo en \(k\) impide la aparición de otras raíces sin pasar por una múltiple. En los cruces, al desarrollar \(\cos(\omega+k)=2f^2-1\), las dos pendientes locales son \(-1\pm2(4t-1)\) en \(z=\pm1\) y \(-1\pm2(1-4A)\) en \(z=\pm i\). Ninguna se anula en los dos medios. Cada rama persiste a ambos lados con su signo. Esto justifica comparar los **recuentos laterales** incluso donde las dos ramas comparten un mismo \(\lambda\) en el nivel exacto. En los pliegues interiores, la diferencia entre ternas adyacentes es una raíz de cada signo.

«Not claimed» deja espacio para el recuento orientado fuera de \(I\) y reserva la clasificación modal individual a la ventana. Conviene hacer explícito en la tabla que sus filas corresponden a niveles regulares, pues la desigualdad \(d_\pi>\delta\), leída sola, incluye \(z=\pm i\).

### 2. Recintos, asignación de raíces y normalización

**C3 — PASS.** El documento 5 evalúa el radical de \(u^*\), las dos elecciones de \(C\) y las dos de \(S\) mediante intervalos racionales. `dec` aplica suelo al extremo inferior y techo al superior, incluidos los extremos negativos. El recinto de \(z_c^*\) del informe coincide dígito por dígito con la fila \((1,-1)\) de Z. Los otros tres se obtienen cambiando los signos e invirtiendo los extremos de cada intervalo negado. Quedan separados por cuadrantes. La pertenencia exacta al círculo también se deduce a mano de \(4f'^2=1-f^2\), pues \((2f^2-1)^2+16f^2f'^2=1\).

**C4 — PASS.** Los factores son conjugados en sus coeficientes. Su producto racional es libre de cuadrados, tiene grado 24 y el aislamiento da 24 cajas. Cada caja contiene una raíz del producto. Por tanto, si Horner intervalar excluye cero para un factor, la raíz pertenece al otro. Que la evaluación del otro contenga cero es compatible con esa conclusión. La prueba de existencia procede del aislamiento previo. El código rechaza las dos situaciones ambiguas, tanto si ambas evaluaciones contienen cero como si ambas lo excluyen.

Las desigualdades estrictas de `abs2` certifican cuatro raíces dentro y cuatro fuera. Para las cuatro restantes, \(1\in|\lambda|^2\) por sí solo permitiría falsos positivos. Aquí Sturm ya da cuatro raíces distintas exactamente sobre el círculo, con
\[
\lambda=\frac{1-\tau^2-2i\tau}{1+\tau^2}.
\]
Necesariamente ocupan las cuatro cajas restantes. El cruce uno a uno de recintos identifica cuál corresponde a cada \(\tau\). Del mismo modo, la simetría de C2 garantiza la existencia de la raíz \(1/\bar\lambda\) en una caja exterior. Al encontrar una sola intersección posible se identifica esa caja. Se prueba así dónde cae **la raíz imagen**. El predicado `coverlap` no acredita la inclusión geométrica de toda la caja transformada en la caja exterior.

Hay además un contraste manual de la asignación al factor, pertinente por el uso de `nsimplify` en `to_CI`. El coeficiente de \(\lambda^{11}\) de \(P(\lambda,z_0)\) es cero, de modo que las doce raíces suman cero. Fijados los cuatro propagantes por \(\tau\), las sumas de las partes imaginarias de cada pareja evanescente identificada en el registro son, aproximadamente,
\[
\begin{aligned}
\text{interior}&:\quad 0.598347,\;-0.386787,\;-0.171064,\;0.636915,\\
\text{exterior}&:\quad 0.840535,\;-0.560914,\;-0.249074,\;0.762727.
\end{aligned}
\]
En cada medio cancelan la suma imaginaria de los propagantes a la precisión mostrada. La otra elección de factor para una pareja conjuga ambos miembros y cambia el signo de su contribución. En ninguna fila hay un subconjunto no vacío cuya suma diste de cero menos de \(0.03\). El margen supera ampliamente el redondeo. Así se distingue también a mano la asignación publicada de todas las alternativas compatibles con la reciprocidad.

**C5 — PASS.** Para cada uno de los ocho modos, el registro conserva \(\tau\), el signo, la elección de fila 1, \(F\), \(1/\sqrt{|F|}\) y las doce componentes complejas en el orden \(a_1,\ldots,a_6,b_1/\lambda,\ldots,b_6/\lambda\). La fila determina el vector inicial por la fórmula publicada. Como \(G\) es hermítica y C5 establece \(F\ne0\) con el signo de \(v\), la definición \(N=Y/\sqrt{|F|}\) da exactamente
\[
N^\dagger G N=F/|F|=\operatorname{sign}v.
\]
La evaluación intervalar de N comprueba que la parte real contiene ese signo con anchura inferior a \(10^{-10}\) y que la parte imaginaria contiene cero. Esa es una comprobación correcta de consistencia. `same_F` compara los cuatro extremos con el cálculo de C5 **reejecutado en la misma importación**. El registro histórico de 53 comprobaciones carecía de esos extremos.

### 3. Verificador y procedencia

V compara literalmente \((4,1,3)\) en ambos medios, conserva por separado el criterio contractual exterior \(\#\mathrm{derecha}\ge1\), coteja la cuártica primitiva completa y exige inclusión estricta en el recinto grueso. Los ocho evanescentes se siguen del grado 12 y E comprueba explícitamente el reparto \(4+4\).

H lee ambos archivos antes de importar y compara los SHA256 completos con los valores de referencia que figuran en la cabecera del documento 3. Las comparaciones se ejecutan **después** de `exec_module`. Una discrepancia impide que A1 termine satisfactoriamente, aunque para entonces el archivo ya se ha ejecutado. Esto satisface la identificación pedida para la ejecución registrada. El hash propio de A1 y el commit constan en la cabecera del registro.

### 4. Determinante con perfil variable

La reducción escrita sustituye \(a_6\) por \((c_6a_6-za_1)/s_6\) en las coordenadas de la forma. Si \(T\) denota ese cambio, \(|\det T|=|c_6/s_6|\). La forma diagonal resultante tiene cinco entradas positivas y siete negativas. Por congruencia, en el dominio de la transferencia,
\[
\det G_x=|\det T|^2(-1)^7=-\cot^2\beta_6(x).
\]
El informe atribuye expresamente la derivación a la revisión anterior. G calcula por separado el determinante con las monedas racionales del perfil en \(x=0,\ldots,5\). La generalidad procede de la congruencia y el registro documenta los seis contrastes.

### 5. Objeciones residuales, por gravedad

1. **Menor, C5 [A1], «Inputs» y «Checks».** El primer \(\tau\) impreso, por ejemplo, tiene extremos que terminan en `60639` y `60638`, con anchura \(10^{-20}\). La precisión \(10^{-45}\) corresponde al refinamiento interno. Corregir la frase a «intervalo refinado internamente con tolerancia \(10^{-45}\) e impreso con redondeo exterior a 20 decimales». Especificar también que la cota \(10^{-10}\) se aplica a la parte real de \(N^\dagger G N\). Los \(F\) y \(1/\sqrt{|F|}\) de la tabla son aproximaciones a seis cifras significativas. Sus redondeos concuerdan con el registro, al igual que los evanescentes a tres decimales y los \(k\) orientativos obtenidos de \(2\arctan\tau\).
2. **Menor, verificador E y V.** En E, `to_CI` aplica `nsimplify` a coeficientes que ya pertenecen a \(\mathbb Q(i)\), sin comprobar igualdad con el coeficiente original. Extraer directamente las partes racionales exactas elimina esa dependencia y hace explícita la premisa de Horner. En V, `.is_number` por sí solo admite el cociente constante cero. Exigir un racional no nulo expresa exactamente la proporcionalidad anunciada. Ninguna de estas debilidades cambia las asignaciones ni el cociente del caso registrado.
3. **De redacción, C2 y C4.** Añadir «para niveles regulares» a la tabla C2 y sustituir en C4 «la caja se transforma en una caja exterior» por «el recinto de la imagen intersecta una única caja exterior, que contiene la raíz compañera». Ambas formulaciones reflejan exactamente lo demostrado.

**Cierre contractual.** La ventana congelada es \(I=(\delta,\pi/2)\) y contiene \(z_0\). En cada medio hay en toda ella cuatro propagantes, uno hacia la derecha y tres hacia la izquierda. Los entregables individuales exigidos en \(z_0\) están en el registro. Las correcciones anteriores afectan a la descripción de la precisión y de los predicados, y permiten mantener `CHANNELS_CLASSIFIED`.