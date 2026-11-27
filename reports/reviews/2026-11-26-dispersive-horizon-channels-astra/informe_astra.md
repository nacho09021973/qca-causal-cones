<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.2-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-26T15:36:18Z  fin: 2026-11-26T15:40:50Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md ; último commit observado: 7a63529 ; sha256 de la copia enviada 8ad65212fdc99dd3367ceb073183fd51ba046fe0ea9f09671c361be64b7c3b37
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-channels.md ; último commit observado: 4ff574c ; sha256 de la copia enviada 71109df6c24ceb1368b6e367f06d449d6f4630e7e90a460f3771ade62fa45114
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_channels.py ; último commit observado: a5b9be3 ; sha256 de la copia enviada 08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_matrix.py ; último commit observado: d0114b2 ; sha256 de la copia enviada 98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-channels-run.txt ; último commit observado: 4ff574c ; sha256 de la copia enviada cff1082b90dd3ef6f8e28b02a249f2437cb2a467de03d2f5f1de39bdf7fcaaa8
entrada_astra.txt sha256 570802b6f6103aaf698955a18991eeeddc9e72048b663e2bad8f62c18f32c54f
respuesta sha256 8e981bcb795c88468d950e1cdc84a01fd5452d22ff74aae22b679f749339ef8e
-->

**Veredicto global: REPAIR_REQUIRED.** La ventana congelada es \(I=(\arg z_c^*,\pi/2)\). En toda ella hay, en cada medio, un propagante hacia la derecha, tres hacia la izquierda y cuatro evanescentes en cada sentido de decaimiento. La forma de flujo y la normalización por velocidad son correctas. Ninguna regla de parada se activa.

La reparación afecta al cierre del contrato. C2 pedía el recuento entre umbrales y el informe sólo lo da en \(I\). C4 y C5 pedían resultados por raíz y el registro conserva agregados. En particular, el informe llama «certificado» al intervalo de normalización de cada modo, pero ni el informe ni el registro dan sus extremos.

| Punto | Veredicto | Resultado |
|---|---|---|
| 1. C1, flujo | PASS | La forma representa la corriente del corte. La identidad general y el determinante son correctos. |
| 2. C2, raíces | REPAIR_REQUIRED | Simetría, reducción y enrollamiento correctos. Falta una parte del recuento exigido. |
| 3. C3, umbrales | REPAIR_REQUIRED | Valores críticos, cuártica y ventana correctos. Faltan los recintos racionales que el contrato pide entregar. |
| 4. C4, clasificación | REPAIR_REQUIRED | Recuento, signos y constancia correctos. Falta identificar individualmente los evanescentes en \(z_0\). |
| 5. C5, normalización | REPAIR_REQUIRED | Identidad exacta y apareamiento correctos. Falta registrar los factores por raíz. |
| 6. Verificador | REPAIR_REQUIRED | La aritmética inspeccionada es exacta. Algunos resultados impresos tienen una condición de aceptación más débil que el resultado publicado. |
| 7. Veredicto y alcance | REPAIR_REQUIRED | Se satisface el criterio físico de canales. Quedan entregables explícitos para cerrar C1–C5. |

He revisado únicamente los cinco textos suministrados. Distingo las derivaciones manuales de los resultados que leo en el código y en el registro. La ejecución independiente, la correspondencia con los commits y los hashes de los archivos son **[UNVERIFIED]**.

### 1. C1 | La corriente a través del corte

En la etapa \(j\), cruzan hacia la derecha \(a_{j+1}(x+1)\) y hacia la izquierda \(b_{j+1}(x)\). El desplazamiento final \(L_-\) resta \(\|q_7(x+1)\|^2\). Al sumar las seis etapas y sustituir \(q_7(y+1)=zq_1(y)\), con \(|z|=1\), obtengo
\[
J_x=\sum_{j=2}^6|a_j(x+1)|^2
       -\sum_{j=1}^6|b_j(x)|^2-|b_1(x-1)|^2
    =Y_{x+1}^\dagger D Y_{x+1}-Y_x^\dagger E_{77}Y_x.
\]
Esto fija tanto el cero inicial de \(D\) como el índice 7 y el signo de \(E_{77}\). La conservación local de población durante el periodo da \(J_{x+1}=J_x\). La polarización da la identidad sesquilineal.

Por inspección, `zero_on_circle` comprueba las 144 entradas de la identidad. Usa \(z^{-1}\) para la conjugación, elimina denominadores en el dominio admisible de \(M\) y reduce por polinomios mónicos en variables \(s_j\) distintas. Los dos pasos de transferencia comparten correctamente los coeficientes del sitio \(x+1\). En \(x+2\) sólo interviene la sexta moneda. El contraste operativo comprueba las cuatro parejas de dos soluciones exactas en todos los cortes del rango `xs`. Es un buen contraste del signo y de los índices. La generalidad procede de la identidad simbólica y de la derivación del corte. La segunda vía homogénea que exige el contrato se completa en C5.

También se puede obtener el determinante a mano. La unitariedad de las cinco primeras monedas permite reescribir
\[
J_x=\sum_{j=1}^5|a_j(x)|^2-\sum_{j=1}^6|b_j(x-1)|^2
       -\left|\frac{c_6(x)a_6(x)-za_1(x)}{s_6(x)}\right|^2 .
\]
El cambio que sustituye \(a_6\) por la última expresión dentro del módulo tiene determinante de módulo \(|\cot\beta_6(x)|\). La forma diagonal resultante tiene cinco signos positivos y siete negativos. Por tanto \(\det G_x=-\cot^2\beta_6(x)\), incluso con perfil variable. Esto da \(-5/11\) y \(-7/9\) en los límites y satisface directamente la relación con \(|\det M_x|^2\).

### 2. C2 | Simetría, enrollamiento y recuento que falta

Como \(f_\lambda=f_{1/\lambda}\), la sustitución en \(P\) da \(\lambda^{12}P(1/\lambda,1/z)=z^{-2}P(\lambda,z)\). Los coeficientes de la expresión en \((\lambda,z)\) son reales. Con \(\bar z=1/z\), la involución a \(z\) fijo es \(\lambda\mapsto1/\bar\lambda\), con multiplicidades. Al dividir por \(z\lambda^6\) aparece \(z/\lambda+\lambda/z-4f^2+2=-2h(k)\). Ninguno de los factores eliminados se anula en el círculo.

Cada moneda y cada \(S(k)\) tienen determinante uno. Así, \(\det U(k)=e^{-2ik}(\det W)^2=e^{-2ik}\). En un nivel regular, el número orientado de preimágenes de cada fase es su grado. La suma de esos grados es el grado del producto de las fases, igual a \(-2\). Esto justifica el signo para la convención \(\lambda=e^{-ik}\). El paso de grado a recuento es una demostración escrita.

**El recuento omitido en el informe sí cambia fuera de \(I\).** Escribiendo \(\delta=\arg z_c^*\) y \(d_\pi(\omega)=\operatorname{dist}(\omega,\pi\mathbb Z)\), obtengo la siguiente tabla para niveles regulares, separando los cruces exactos.

| Medio y región | Propagantes | Derecha | Izquierda |
|---|---:|---:|---:|
| Interior, \(0<d_\pi(\omega)<\delta\) | 6 | 2 | 4 |
| Interior, \(d_\pi(\omega)>\delta\) | 4 | 1 | 3 |
| Exterior, en todos los arcos regulares | 4 | 1 | 3 |

Para verificar el cambio de dos, en \(-\pi/2<k<0\) la rama \(-k-2E(k)\) interior tiene pendiente positiva en el extremo izquierdo y negativa al llegar a \(0\). C3 da exactamente un punto estacionario en ese tramo de esa rama. Es el máximo de valor \(\delta\). Al bajar de \(\delta\) aparecen dos raíces con velocidades opuestas. La conjugación y el cambio \(k\mapsto k+\pi\) dan los otros tres pliegues. Los cruces con dos pendientes no nulas conservan el recuento a ambos lados. En el exterior no hay pliegues. El recuento de partida de cuatro tiene además la comprobación manual del punto 4.

### 3. C3 | Umbrales, cuártica y ventana

Se tiene \(h_\omega=\sin(\omega+k)\) y \(h_k=4ff'+\sin(\omega+k)\). Si \(h_\omega\ne0\), la condición \(h=h_k=0\) da
\[
4f'^2=1-f^2,\qquad
z_c=e^{-ik}(2f^2-1-4iff').
\]
Recíprocamente, con \(0<|f|<1\), esa expresión tiene módulo uno y da \(h=h_k=0\). Esto último establece la igualdad de módulo que el test de intervalos sólo comprueba por compatibilidad.

Si \(h_\omega=0\), entonces \(f=0,\pm1\). La monotonía de \(g\) sitúa los cruces en \(k=0,\pi,\pm\pi/2\). Las pendientes de las ramas locales son \(-1\pm2(4t-1)\) en los dos primeros y \(-1\pm2(1-4A)\) en los otros dos, como pares sin ordenar. Ninguna se anula en los medios límite. La distinción entre cruce y valor crítico es correcta.

Al quitar el factor \(u-1\), obtengo, salvo constantes, \(2625u^2-5245u+2604\) en el interior y \(343u^2-1211u+1012\) en el exterior. El segundo decrece en \([0,1]\) y vale \(144\) en \(1\). En el primero sólo la raíz con el signo menos del radical cae en \((0,1)\). Esto confirma por otra vía el resultado de Sturm.

Se pueden dar **recintos racionales explícitos** sin reproducir la aritmética de 200 bits. Sea \(d=1-u^*\). Entonces \(2625d^2-5d-16=0\) y \(78/1000<d<80/1000\). Para \(C=+\sqrt{1-d}\), esto da \(959/1000<C<961/1000\), \(99/100<g(C)<1\) y \(17/100<g'(C)<7/40\). Con \(S=\sin k\),
\[
\Re z_c=C(2g^2-1)+4dg g',\qquad
\Im z_c=S\bigl(4Cgg'-(2g^2-1)\bigr).
\]
Para \(S=-\sqrt d\) resulta el recinto
\[
(\Re z_c^*,\Im z_c^*)\ \in\ (9/10,1)\ \times\ (1/20,1/8).
\]
Los otros tres recintos se obtienen por conjugación y por cambio global de signo. Esto separa los cuatro valores, identifica el único del primer cuadrante y prueba \(\Re z_c^*>3/5\).

Para contrastar la **cuártica impresa**, la reducción módulo \(2625d^2-5d-16\) da
\[
\Re z_c^*=\sqrt{1-d}\,\frac{64368+9195d}{62720}.
\]
Eliminando \(d\), la parte primitiva del resultante es
\[
316240512000000000X^4-664624285099139500X^2
 +348107462168643891 .
\]
El grado cuatro también se justifica a mano. Para la raíz conjugada \(d'\in(-1/10,0)\), el valor conjugado de \(X^2\) excede uno, luego \(X^2\) tiene grado dos. Su norma racional es \(124/125\) por un cuadrado racional no nulo, pues \((1-d)(1-d')=124/125\). Así \(X^2\) tampoco es un cuadrado en ese cuerpo cuadrático. El código calcula el polinomio mínimo y cuenta una raíz en el recinto de la parte real. El registro imprime el grado, pero omite los coeficientes y los extremos del recinto.

Por tanto \(0<\delta<\arg z_0<\pi/2\), y la componente que llega a \(\pi/2\) desde abajo es exactamente \((\delta,\pi/2)\). La glosa de \(C_t\) cambia el conjunto de puntos que se llamarían umbrales si se incluyen todos los cruces. Ambas lecturas dan la misma componente congelada.

### 4. C4 | Cuatro raíces propagantes y sus signos

En \(z_0\), los dos tests de libertad de cuadrados son pertinentes. El de \(P\) da doce autovalores distintos y el de \(H\) da raíces simples en la carta real. El coeficiente de \(\tau^{12}\) de \(H\) es \(h(\pi)=8/5\), lo que verifica directamente el punto omitido por \(\tan(k/2)\). En una raíz real,
\[
\operatorname{sign}v=-\operatorname{sign}N,\qquad
N=(4ff'+h_\omega)h_\omega(1+\tau^2)^8 .
\]
El gcd excluye tanto el numerador nulo como \(h_\omega=0\). El aislamiento de una raíz de \(H\) en un intervalo libre de ceros de \(N\) permite evaluar el signo en un racional interior. El registro da cuatro raíces reales en cada medio.

Hay una comprobación manual independiente del total. Para \(\omega=\pi/2\), poniendo \(s=\sin k\) y \(B=-4A\),
\[
h=(1-s)\,[\,2(1+s)(1+Bs^2)^2-1\,].
\]
El corchete tiene un solo cero en \((-1,0)\). Su derivada tiene el signo de \(1+B(5s^2+4s)>0\), y para \(s\ge0\) el corchete es positivo. Ese cero produce dos raíces simples en \(k\). El punto \(s=1\) aporta dos ramas con pendientes no nulas que persisten al bajar ligeramente de \(\pi/2\). Hay por tanto cuatro raíces cerca de ese extremo. En \(I\), C3 excluye todo cero múltiple sobre el círculo. La continuación local de los ceros simples, la compacidad del círculo y la continuidad de la velocidad dan la constancia alegada.

También se pueden identificar **los signos por raíz en \(z_0\)**. En los cinco puntos \(k=-\pi,-\pi/2,0,\pi/2,\pi\), los signos de \(h\) son \(+,-,+,-,+\). Hay una raíz en cada intervalo consecutivo. Para resolver el signo de \(h_\omega\) en el segundo y el cuarto basta observar que \(h(-\omega_0)<0\) y \(h(\pi-\omega_0)>0\). En orden creciente de \(k\), los signos de \(v\) son así **\(-,-,+,-\)** en ambos medios.

Las ocho raíces restantes se agrupan en cuatro pares recíprocos conjugados. Para la órbita \(\lambda^xY\), las cuatro interiores decaen al avanzar hacia \(+\infty\) y las exteriores hacia \(-\infty\). Se obtiene \(1-3=-2\), y hay cuatro canales entrantes y cuatro salientes. La constancia en \(I\) comprende estos recuentos con multiplicidad. La prueba de simplicidad de **todas** las raíces, incluidas las evanescentes, se hizo en \(z_0\).

### 5. C5 | Flujo exacto y normalización

Sea \(R_jq_1=C_jq_j\), con los desplazamientos intercalados como en el código. En un modo de Bloch propagante las traslaciones conservan el módulo de cada amplitud. La corriente del corte queda
\[
F=\sum_j q_1^\dagger R_j^\dagger\sigma_zR_jq_1-\|q_1\|^2 .
\]
Al derivar el producto de factores de \(U\), cada \(S\) contribuye \(-iS^\dagger S'=\sigma_z\) conjugado por el producto precedente. El factor escalar \(e^{-ik}\) contribuye \(-I\). Por tanto
\[
-iU^\dagger U'=\sum_jR_j^\dagger\sigma_zR_j-I,\qquad
F=\Omega'\|q_1\|^2 .
\]
La última igualdad se obtiene derivando \(Uq_1=e^{i\Omega}q_1\) en una rama simple. Fija exactamente el factor de proporcionalidad y su signo.

Por inspección, el código selecciona un vector no nulo del núcleo, reconstruye las seis etapas y usa \(b_j/\lambda\) en la mitad inferior de \(Y\), conforme a la definición de transferencia. `refine_root` recibe precisión racional \(10^{-45}\). Para cada raíz, el registro atestigua signo estricto de \(\Re F\), concordancia con el signo de Sturm, \(0\in\Im F\) y \(1\) en el intervalo de \(\Re F/(v\|q_1\|^2)\) de anchura inferior a \(10^{-20}\). La realidad y la igualdad exactas se siguen de las identidades anteriores. El vector unitario por flujo es \(Y/\sqrt{|F|}\). El intervalo de \(F\) permite acotar ese factor, pero sus extremos por modo no quedaron en el registro.

Para dos autovectores de transferencia, C1 da \((1-\bar\mu\nu)Y_\mu^\dagger GY_\nu=0\). En \(z_0\), la base de doce autovectores y la no degeneración de \(G\) obligan a que el emparejamiento con el único compañero \(1/\bar\mu\) sea no nulo. Cada evanescente tiene autoflujo cero.

### 6. Verificador | Qué acredita el 53/53

La inspección de `RI` y `CI` muestra operaciones de inclusión racionales. Los cuatro productos de extremos acotan una multiplicación real. La inversión comprueba que el intervalo excluya cero. Un producto intervalar de un intervalo por sí mismo puede ensanchar la cota de un cuadrado, pero conserva la inclusión. En `sqrt_RI`, con escala \(2^{200}\), el `isqrt` del extremo inferior redondeado hacia abajo da una cota inferior segura. El `isqrt` del superior redondeado hacia arriba, más una unidad, da una cota superior segura, también para cuadrados perfectos. La coma flotante visible mide tiempos. Los datos espectrales inspeccionados usan racionales, enteros o expresiones simbólicas exactas.

El registro suministrado contiene los 53 `PASS` y los recuentos publicados. Hay tres límites concretos a su interpretación.

- **Recuentos dinámicos.** La línea que anuncia «4, 1, 3» comprueba que dos formas de contar concuerdan y que los signos suman el total. La de «4 + 4» comprueba paridad y usa la simetría de C2. Son conclusiones válidas para los valores impresos. Como control de regresión de la tabla exterior, el programa también aceptaría, por ejemplo, dos derechas y cuatro izquierdas si los demás cálculos fueran coherentes. La igualdad de dimensiones entrante y saliente tampoco distingue ese caso.
- **Predicados parciales.** Que un intervalo contenga \(1\) o \(0\) prueba compatibilidad. Las igualdades exactas correspondientes tienen las demostraciones de C3 y C5. La exclusión de todos los cruces de \(I\) usa además su localización previa. El test del polinomio mínimo aísla una raíz del polinomio calculado, pero no compara sus coeficientes con los transcritos al informe.
- **Procedencia.** El documento 3 carga el documento 4 para ejecutarlo y no contiene una escritura sobre su fuente `.py`. `M_report` sí se reutiliza. `hom_cs` se vuelve a definir localmente y la matriz homogénea intervalar de C5 se transcribe a mano. Sus entradas coinciden por inspección con `M_report` homogénea. La identidad byte por byte con el archivo del commit auditado sigue **[UNVERIFIED]**. El hash de cabecera identifica al verificador de canales.

### 7. Cierre y objeciones por gravedad

1. **Mayor — contrato C2 e informe «Not claimed».** Falta el recuento por arcos regulares fuera de \(I\). La exclusión global de «anything at quasienergies outside I» contradice esa tarea y también la determinación global de umbrales de C3. **Reparación:** incorporar la tabla del punto 2 y acotar esa exclusión a los resultados que el contrato reserva a \(I\). Las exclusiones sobre transmisión, dispersión, Jost, interpretación física y originalidad son adecuadas.
2. **Mayor — entregables C3–C5.** Los recintos críticos, los identificadores de los ocho evanescentes de cada medio y los factores individuales de normalización no aparecen en la salida conservada. **Reparación:** emitir recintos racionales para los cuatro \(z_c\), identificar los cuatro evanescentes interiores de cada medio por cajas aislantes en \(z_0\) y referir sus cuatro compañeros por reciprocidad. Para cada propagante, registrar el intervalo de \(\tau\), el signo, el vector inicial elegido y un intervalo de \(F\) o de \(1/\sqrt{|F|}\). La recurrencia de etapas ya especifica las doce componentes del vector normalizado.
3. **Media — verificador C3/C4 y procedencia.** **Reparación:** comparar el polinomio mínimo primitivo y la tabla de ambos medios con los valores que se publican, conservando aparte el criterio contractual «al menos uno» para el exterior. Adjuntar la identificación por hash del archivo importado frente a la versión auditada.
4. **De proceso — «Authorization and process».** La ejecución de desarrollo anterior al commit incumplió literalmente el orden congelado. La ejecución registrada posterior permite sostener las comprobaciones sobre la versión identificada en el registro, con la limitación de procedencia ya indicada. La desviación no invalida las identidades ni cambia la ventana fijada de antemano. **Reparación:** conservar la desviación en el balance y hacer la próxima ejecución registrada de las correcciones después de su commit.

El candidato `CHANNELS_CLASSIFIED` satisface las condiciones de existencia y unicidad de canales. Para el cierre documental actual, la cláusula «otherwise, with the open obligation stated» del contrato corresponde a **`OPEN_AFTER_CHANNEL_ANALYSIS`**, con las obligaciones concretas de los puntos 1 y 2.