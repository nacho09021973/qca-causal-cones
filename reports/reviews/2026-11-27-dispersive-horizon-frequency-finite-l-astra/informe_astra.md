<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.2-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-27T09:20:23Z  fin: 2026-11-27T09:24:07Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/theory/DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md ; último commit observado: 204f33b ; sha256 de la copia enviada 5c834a013d4f46a71777b05554b392c1765382feddb1c7f143cd9d53afd998de
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-27--dispersive-horizon-frequency-finite-l.md ; último commit observado: e8952e3 ; sha256 de la copia enviada 4dc314e81bbb194ccb8b67da80a2d1eeceeb61b262c9f8b94ebf5aed6083a00f
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/scripts/verify_dispersive_horizon_frequency_finite_l.py ; último commit observado: 00f09c9 ; sha256 de la copia enviada 3d585a541663ad7f51a539d728069d228e6a8473772ccc3ca90bb17a8ef80faa
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/scripts/verify_dispersive_horizon_transmission.py ; último commit observado: 0959251 ; sha256 de la copia enviada 29ee9f127b2e43dc1a8aabf2cfdffb6e727edf502e9677b823f45b7c27e316ea
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-27--dispersive-horizon-frequency-finite-l-run-1.txt ; último commit observado: fdbbe8a ; sha256 de la copia enviada 6a4041fc9b9a18577a98caa477d9fbc3ef78ce2228989c543912a3e719aa00fe
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-26--dispersive-horizon-transmission.md ; último commit observado: c832876 ; sha256 de la copia enviada 15b7732d3c3786661207ac75086ba5ac9a9cad7f8e2214e2dcece4516e551211
entrada_astra.txt sha256 81134a8d9ceaf7230235f2d26e6d7bcaeb5976fe9c4f2bddb1c9bbf120340bc7
respuesta sha256 6e8ce2820271f6ee493ea80e3895a8e2d6449eb2a66e3dd02d2e93457dfda35d
-->

**Veredicto global — REPAIR_REQUIRED.** Los diez veredictos puntuales de F2/F3 se sostienen. Al cerrar el contrato corresponde adoptar `LEAKAGE_NOT_SUPPRESSED` para la transmisión máxima \(\sigma^2\) en los dos puntos de F3. La objeción física sí identifica una limitación de ese observable. Además, los adjuntos permiten resolver a mano dos cuestiones que el informe deja abiertas: la raíz del resultante se explica en \(u=1\), y los recuentos por sectores de \(k\) distinguen la rama que continúa de la que encuentra el retorno. Ninguna de esas dos deducciones demuestra un límite adiabático para la dispersión.

He inspeccionado el código y el registro suministrados. Los recuentos de Sturm, las inclusiones intervalares y los tiempos de ejecución que cito proceden de ese registro. Las derivaciones algebraicas y los argumentos de continuidad que siguen son manuales. No he ejecutado código, calculado transmisiones nuevas ni realizado un seguimiento numérico de ramas.

| Punto | Veredicto | Resultado |
|---|---|---|
| 1. F1(a), método | REPAIR_REQUIRED | La parametrización describe el lugar crítico real si se añaden las colisiones y se restituyen los signos. Falta distinguir ese entregable del discriminante algebraico completo pedido. |
| 2. F1(a), resultado | REPAIR_REQUIRED | `OPEN_AFTER_DISCRIMINANT_ANALYSIS` es la salida correcta del programa. La objeción del resultante se resuelve por una identidad en el extremo. El `PASS` de clasificación tiene un alcance excesivo. |
| 3. F1(b) | PASS | `CONNECTED` queda probado individualmente en los tres puntos altos. En cada punto bajo hay un valor singular intermedio con pérdida de dos raíces reales. |
| 4. F2/F3, tubería | PASS | La certificación es válida con la aritmética intervalar declarada. El producto contiene 66 o 258 matrices, tal como exige la recurrencia. |
| 5. Resultados puntuales | PASS | Los seis encierros bruscos y los cuatro truncados deciden positividad y anchura. Los dos cotejos deciden solapamiento. |
| 6. Objeción física | REPAIR_REQUIRED | Se puede justificar la geometría de las ramas. La causa del valor alto de \(\sigma^2\), la mezcla por rama a \(L\) finita y el límite adiabático siguen `[UNVERIFIED]`. |
| 7. Línea y alcance | REPAIR_REQUIRED | El resultado operacional de la línea está decidido. La reserva física corresponde a la interpretación y al diseño de otro observable. |

### 1. F1(a). Qué curva describe la parametrización

Sea \(C=\cos k\), \(u=C^2\), \(b=1-4A+4Au\), \(d=1-4A+12Au\). Entonces \(f=Cb\) y \(f'=-\sin k\,d\). Una raíz real múltiple satisface \(h=h_k=0\), de donde

\[
\cos(\omega+k)=2f^2-1,\qquad \sin(\omega+k)=-4ff'.
\]

Al sumar cuadrados se obtiene \(4f^2[4f'^2-(1-f^2)]=0\). Si \(f\ne0\), la segunda condición da precisamente `thr = 0`. También vale el recíproco: para un \(k\) real que la cumple, los dos miembros derechos definen el coseno y el seno de **un mismo ángulo**. Así se recupera \(z\) sin introducir soluciones por el cuadrado. En particular,

\[
\Re z=(2f^2-1)C-4ff'\sin k
     =C\bigl[2ub^2-1+4(1-u)bd\bigr]=C R.
\]

En \(u=1\), \(R=1\). Para \(q=0\), \(q_u\ne0\), la derivación implícita da \(dy/dA=(y_Aq_u-y_uq_A)/q_u\). Por tanto, el \(J\) del código es correcto para \(y=uR^2\).

Hay dos casos que deben figurar en la equivalencia. En toda la franja \(b>0\) y \(d\ge 1+8A=(4t-1)^2>0\). Así, \(f=0\) exige \(C=0\) y da las colisiones \(z=\pm i\). Los nodos \(u=1\) dan \(z=\pm1\), incluido \(k=\pi\), que requiere atender al punto en el infinito de la carta \(\tau\). Para \(0<u<1\), los cambios \(k\mapsto-k\) y \(k\mapsto k+\pi\) recuperan la conjugación y el cambio \(z\mapsto-z\). Esas simetrías justifican el uso de \(y\) en el primer cuadrante.

**Juicio contractual.** Es un método exacto admisible para obtener la proyección de «valor crítico o colisión» **real**. El discriminante literal \(\operatorname{disc}_\tau H\) también detecta raíces múltiples complejas, y su tratamiento proyectivo exige controlar el grado. El verificador calcula especializaciones en seis frecuencias y no entrega ese discriminante como curva bivariada. Si se conserva el `OPEN`, basta declarar qué parte del encargo se ejecutó. Para cerrar F1 como cumplimiento literal, corresponde aportar la curva pedida o aceptar explícitamente, mediante enmienda identificada como posterior, la caracterización equivalente del lugar físico. No hace falta enmendar F2/F3. (Docs. 1, F1; 3, `thr`, `Rr`, `J`; 4, `H_of`.)

### 2. F1(a). La raíz del resultante se identifica a mano

Hay una comprobación decisiva que el informe omite. Escribiendo \(h_0=1+8A\), la evaluación de las fórmulas del verificador da

\[
q(1,A)=\partial_u\mathrm{thr}(1,A)=h_0(1-4h_0),\qquad
y_A(1,A)=0,\qquad y_u(1,A)=1-4h_0.
\]

La última igualdad se obtiene de \(R(1,A)=1\) y \(R_u(1,A)=-2h_0\). Por tanto, para \(A_d=-3/32=A(3/8)\), se cumplen simultáneamente \(q(1,A_d)=J(1,A_d)=0\). **Ese valor ya explica la única raíz real del resultante registrada en la franja.** No queda otro valor de \(A\) en el que buscar un extremo interior.

Hay que excluir todavía una raíz física adicional en ese mismo \(A_d\). Los recuentos registrados lo permiten. El coeficiente líder y \(\operatorname{disc}_u q\) no se anulan, ninguna raíz cruza \(u=0\) y el único evento en \(u=1\) es \(A_d\). Hay una raíz en \((0,1)\) en el extremo interior de la franja y cero en el exterior. Por continuidad de raíces simples, la raíz física llega a \(u=1\) en \(A_d\). Cualquier otra raíz en \((0,1)\) en \(A_d\) persistiría inmediatamente a su derecha, contradiciendo el recuento cero. En la rama física abierta \(J\ne0\), luego \(y\) es monótona entre \(y_*\) y 1.

Así, **como deducción escrita apoyada en los recuentos del log**, el lugar crítico en el primer cuadrante abierto es \(0<\omega\le\arg z_{c*}\), o \(0<s\le s_*\), con

\[
s_*=\sqrt{\frac{1-\sqrt{y_*}}{1+\sqrt{y_*}}}.
\]

Aquí \(y_*=u_*R(u_*,A_{\rm int})^2\), con el \(u_*\) algebraico aislado en F1. Los demás cuadrantes se obtienen por las simetrías anteriores, añadiendo las cuatro colisiones. Esta deducción puede incorporarse como tal, conservando `OPEN_AFTER_DISCRIMINANT_ANALYSIS` como salida histórica de la ejecución.

La lectura del defecto de clasificación necesita un matiz. La comparación con \(y_*\) **sí** sitúa las frecuencias respecto del arco definido por el umbral del medio interior y del intervalo ya denominado \(I\). El salto injustificado en el programa consiste en presentar esa comparación como clasificación frente a **todos los medios intermedios** después de fallar `simple_structure`. Las etiquetas resultan correctas por la derivación anterior y tienen apoyo puntual independiente en F1(b). El `PASS` por sí solo no aporta esa prueba.

También `ok('event structure computed', True)` y `ok('summary written', True)` cuentan ejecución de pasos. El `ok` final de F1(b) sólo exige los tres `CONNECTED` altos; los tres recuentos bajos se **imprimen**. Por eso «43/43» no equivale a 43 conclusiones científicas afirmativas. Los recuentos impresos y las líneas individuales de decisión siguen siendo utilizables. (Docs. 3 y 5, F1 y `SUMMARY`.)

### 3. F1(b). Qué prueba el discriminante punto a punto

En \(s=1/4,1/2,3/4\), el grado en \(\tau\) permanece en 12, el coeficiente líder es constante no nulo y el discriminante carece de ceros en toda la franja. Ninguna raíz real puede desaparecer, encontrarse con otra o pasar por el infinito. Las colisiones de hojas están fuera de esas frecuencias. Una raíz propagante simple conserva el signo de velocidad y en cada extremo hay un único movedor a la derecha. Esto basta para `CONNECTED` en cada punto. Se trata de continuidad en la **familia de medios homogéneos**. El valor de transmisión del perfil brusco lo decide F2 por separado.

En cada uno de \(s=1/200,1/50,1/30\), un cero del discriminante por sí solo podría corresponder a raíces complejas. Aquí hay además seis raíces reales en un extremo y cuatro en el otro, con grado constante y extremos regulares. Por consiguiente, en el único \(A\) singular tiene que ocurrir un evento real. La pérdida neta es de un movedor a la derecha y uno a la izquierda. La frase del registro «not certified connected» es correcta para el test global de regularidad; es compatible con que **una rama concreta sí continúe**. (Docs. 3 y 5, F1(b) y recuentos F2.)

### 4. F2/F3. Certificación numérica y sitios de emparejamiento

- **Raíces y precisión.** Los centros y las inversas aproximadas se convierten en racionales antes de evaluar la inclusión estricta de Krawczyk. Doce cajas disjuntas con existencia, para un polinomio de grado doce, agotan las raíces. El número de cajas compatibles con \(|\lambda|=1\) concuerda con el recuento real independiente de \(H\). Con las cajas base de radio \(2^{-256}\), el código acota \(\kappa^2\) mediante \(\max_X\{\sup|X|^2,1/\inf|X|^2\}\) y compara con \(4^e\) usando racionales. El registro da \(e=3\), de donde salen exactamente \(p=262,646,1798\). La regla fija un presupuesto de precisión. La certificación efectiva procede de las inclusiones y del residuo obtenidos con ese presupuesto.
- **Perfil y vectores.** Sí interviene **coma flotante intervalar en una cantidad certificada**: `iv.exp` proporciona los extremos dirigidos para \(E=\exp(2x/L)\), tal como autoriza expresamente F3. `raw_fr` recupera el valor diádico de cada extremo finito. La función \(1-2/(1+E)\) es creciente, y la imparidad cubre \(x<0\). La validez depende de la garantía de encierro de `mpmath.iv.exp` en la versión declarada. Las raíces cuadradas usan `isqrt`, y los redondeos de cajas usan suelo y techo racionales. La coma flotante ordinaria suministra aproximaciones o cifras de presentación. Los vectores de Bloch se construyen con las cajas a la precisión elegida y se redondean a \(p+32\) antes de la propagación. La identidad general del vector procede de las ecuaciones de etapas y de su solución única. Que un residuo intervalar contenga cero es un control de consistencia.
- **Sitios.** La última transferencia homogénea izquierda entrega \(Y_{-N-1}\). Como \(M_x\) usa también la sexta moneda en \(x+1\), hay que incluir \(M_{-N-1}\). El producto termina en \(M_N\) y entrega \(Y_{N+1}\), donde se empareja con los modos exteriores. Son \(2N+2\) factores, frente a \(2N+1\) sitios de perfil. Para \(N=0\) se recupera \(M_0M_{-1}\). La mención contractual a «65 y 257 transfer matrices» es un error de conteo del texto; el producto explícito, el código y el registro coinciden. La fórmula congelada de \(p\) se aplicó con su \(2N+1\) original.
- **Resolución y flujo.** Para \(A'=AD\), con \(D\) diagonal diádica invertible, \(\beta=\|I-RA'\|_\infty<1/2\) implica invertibilidad y
  \[
  \|x'-\tilde x'\|_\infty
  \le \frac{\|R(b-A'\tilde x')\|_\infty}{1-\beta},\qquad x=Dx'.
  \]
  El código acota los módulos complejos por \(|\Re|+|\Im|\) y encierra el residuo después de racionalizar el precondicionador. Esto justifica el uso de una inversa aproximada a \(p+128\). Un coeficiente \(x_{rc}\) entre vectores sin normalizar transmite la fracción \(|x_{rc}|^2|F_r|/|F_c|\), precisamente el cociente implementado. La unitariedad exacta se apoya en conservación de flujo y en el emparejamiento invertible; \(S^HS\ni I\) comprueba su consistencia numérica. (Docs. 3, `roots_boxes` a `run_point`; 4, `scatter`; 5, C1 y F2/F3; 6, Amendment 1.)

### 5. Qué deciden los diez encierros

En los seis puntos bruscos y en los cuatro truncados, el predicado que asigna `TRANSMISSION_NONZERO_CERTIFIED` usa directamente \(Q_{\rm lo}>0\) y \(\operatorname{anchura}(Q)\le10^{-6}\), con racionales. Los diez resultados lo satisfacen. Las anchuras de orden \(10^{-57}\) corresponden a las cajas internas; las parejas de decimales impresas, redondeadas hacia fuera a 20 posiciones, son encierros más anchos. **Incluso esas parejas impresas** bastan para decidir positividad, el umbral de abandono y las ordenaciones usadas en el veredicto de línea.

Los cotejos de \(z_0,z_1\) comprueban intersección no vacía de los respectivos encierros. Son controles de regresión con código y dependencias compartidos. El resultado en el arco es positividad del bloque de transmisión hacia la única salida exterior. Para un canal incidente individual hace falta su columna. (Docs. 3, `run_point` y `F2 cross-check`; 5, `SUMMARY`.)

### 6. Objeción física. Qué rama continúa y qué mide la fila

**La geometría admite una conclusión más fuerte que la del informe.** Para las tres frecuencias bajas, \(h(0)=1-\cos\omega>0\), \(h(\pi)=1+\cos\omega>0\) y \(h(\pm\pi/2)=-1\pm\sin\omega\ne0\). Una raíz real no puede cambiar de cuadrante de \(k\) al variar el medio. Las cajas registradas, con \(k=-\arg\lambda\), dan este recuento en los dos sectores centrales:

| Sector | Interior | Exterior |
|---|---|---|
| \(0<k<\pi/2\) | Un movedor a la derecha | Un movedor a la derecha |
| \(-\pi/2<k<0\) | Un movedor a la derecha y dos a la izquierda | Un movedor a la izquierda |

El segundo sector exige un evento real. En el \(A\) del evento hay un solo \(u\) crítico físico, por los recuentos de \(q\) del punto 2. Para ese \(u\), los cuatro signos de \(C,\sin k\) dan valores de \(z\) relacionados por conjugación y cambio de signo, distintos fuera de los ejes. A la frecuencia dada sólo uno es crítico. **El evento queda localizado en \(k<0\); el movedor a la derecha de \(k>0\) continúa hasta el exterior.** La simplicidad de \(q\) en \(0<u<1\), donde \(du/dk\ne0\), da un cero simple de la condición de velocidad en la hoja crítica. Además, \(\partial_A h=4f\,\partial_A f\ne0\) allí. Se trata de un pliegue ordinario. En \(z_1\), la pareja negativa que se encuentra tiene \(\sin(\omega+k)<0\); el movedor de \(k\simeq-0.027\) tiene el signo opuesto y queda fuera de la pareja. Este argumento usa sectores, signos y recuentos ya suministrados.

La aproximación \(k\simeq\omega/(8t-3)\) es local para \(t\) fijo con pendiente no nula. Pierde validez uniforme cerca de \(3/8\). Precisamente en \(t=3/8\), la expansión de la hoja de pendiente nula se obtiene de \(f=A\cos3k+(1-A)\cos k\) y da \(\omega=(35/32)k^3+O(k^5)\). Esto explica por qué la inversión lineal falla. A frecuencia positiva fija, \(h(0)>0\) excluye \(k=0\) en todo el perfil. La continuidad del modo positivo hasta el interior se justifica por el argumento de sectores anterior.

**La dispersión contiene otra información.** Para la fila exterior escrita como \((B,r')\), con \(B=(t_1,t_2)\), Cauchy–Schwarz y la unitariedad dan

\[
\sigma^2=\max_{\|a\|=1}|Ba|^2
        =|t_1|^2+|t_2|^2
        =1-\|r'\|^2 .
\]

Una incidencia proporcional a \(B^H\) alcanza el máximo y una proporcional a \((t_2,-t_1)^T\) transmite cero. La unitariedad permite que el peso de la fila se reparta de muchas maneras entre las dos columnas interiores y las tres exteriores. **No impone \(\sigma^2\ge1/2\).** Ese umbral se supera como resultado de la dispersión calculada. En el perfil brusco de \(z_1\) ya consta un dato contra una lectura puramente monomodal: las dos ramas aportan aproximadamente \(0.60328\) y \(0.35726\). Para F3 sólo se registra su suma. Además, en \(z_1\) los dos verificadores enumeran los movedores interiores en orden inverso. Cualquier comparación por rama debe usar la caja de \(\lambda\) o el sector de \(k\) como identificador.

Por tanto, \(\sigma^2\) es adecuada para la pregunta congelada de **cuánto puede escapar una preparación interior óptima**. Para la pregunta de cuánto escapa al preparar **la rama que encuentra el retorno**, el observable es \(|S_{\mathrm{ext,R},\,\mathrm{int,R}(k<0)}|^2\), con incidencia de flujo unidad y las demás entradas vacías. Si se pregunta por conversión a una rama reflejada concreta, también hay que especificar la fila de salida interior. La continuidad geométrica de la otra rama apoya la hipótesis adiabática. Atribuirle el crecimiento de \(\sigma^2\), deducir \(\sigma^2\to1\), o identificar una de estas probabilidades con la fórmula de Sabsovich sigue `[UNVERIFIED]`. La comparación numérica sólo contradice la heurística **si se identifica su observable con \(\sigma^2\)**. (Docs. 2, «Main objection» y F3; 5, cajas F2/F3 y bloque T4 importado; 6, T4 [A1].)

### 7. Veredicto de línea, alcance y procedencia

En ambos puntos predeclarados de F3 los encierros dan estrictamente
\[
\sigma^2_{\rm brusco}<\sigma^2_{L=4}<\sigma^2_{L=16},
\qquad \sigma^2_{L=16}>\tfrac12 .
\]
La supresión es falsa y el abandono operacional es verdadero. **Al cierre corresponde `LEAKAGE_NOT_SUPPRESSED`**, para \(s=1/50,1/200\), \(L=16\), \(N=128\), con el observable máximo convenido. Esperar la revisión antes de cerrar era razonable. Retener el veredicto después de comprobar esas condiciones cambiaría retrospectivamente el criterio. Adoptarlo tampoco constituye autorización para promover el resultado.

«Not claimed» es adecuado para el límite en \(L\), la tanh sin truncar, otras frecuencias, una interpretación térmica o de horizonte físico, la novedad y la conversión de una incidencia específica en F3. Debe corregirse su primer inciso si deja sin registrar el abandono definido por el contrato. Una redacción de cierre suficiente sería: **«Se cumple el umbral de abandono para la transmisión máxima en los dos puntos F3. La transmisión de la rama incidente que encuentra el retorno queda abierta a \(L\) finita».**

Lanzar la ejecución desde otra sesión con un encargo escrito no afecta a las implicaciones matemáticas. El informe declara autorización y el registro identifica versión, commit, hash, entorno, horas y código de salida. La autorización original, los bytes del repositorio, el orden de commits y la unicidad de la ejecución no son autenticables de manera independiente con los adjuntos. (Docs. 1, «Verdicts» y «Not claimed»; 2, «Process»; 5, cabecera y cierre.)

### Reparaciones por gravedad

1. **Alta — Informe, «Line verdict» y «Not claimed».** Adoptar el veredicto operacional con sus dos frecuencias, perfil, \(L,N\) y preparación óptima. Conservar la objeción a la interpretación por rama. Incluir esta distinción en el balance de cierre exigido por el contrato.
2. **Alta — Informe, «Main objection» y «Author heuristic … contradicted».** Incorporar el argumento de sectores. Limitar la atribución adiabática a hipótesis y explicitar qué observable se comparó. Cualquier evaluación nueva de mezcla por rama debe declararse posterior a los resultados e identificar los canales físicamente.
3. **Media — F1(a), entregable y clasificación.** Conservar la salida histórica `OPEN`, añadir la identidad en \(A_d\) y distinguir el lugar crítico real del discriminante bivariado literal. En una revisión del verificador, condicionar las etiquetas globales a la prueba de proyección y comprobar explícitamente los tres recuentos bajos de F1(b).
4. **Menor — Contrato F3 y descripción de la certificación.** Corregir «65 y 257 matrices» por «65 y 257 sitios de perfil, 66 y 258 transferencias». Identificar `iv.exp` como operación de coma flotante **intervalar** de la que depende el certificado. Ninguna de estas correcciones cambia un encierro.