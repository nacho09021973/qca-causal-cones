<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.2-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-27T10:49:33Z  fin: 2026-11-27T10:51:59Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md ; último commit observado: 08e0703 ; sha256 de la copia enviada 0117754239c2afbcea4e08739ec7b35ae0efca12529e66f7a78706848e33ee0f
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-27--dispersive-horizon-turning-branch.md ; último commit observado: 75c7e30 ; sha256 de la copia enviada 43d278468bef902fe4529ff614fc8783975a526fe8ebf6a89685f69f13ac4423
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/scripts/verify_dispersive_horizon_turning_branch.py ; último commit observado: b0bb720 ; sha256 de la copia enviada 397f72b3a9293fe1784dfb9e3d4da8a616f215999c3c97adee006d7d880e0676
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/scripts/verify_dispersive_horizon_frequency_finite_l.py ; último commit observado: 00f09c9 ; sha256 de la copia enviada 3d585a541663ad7f51a539d728069d228e6a8473772ccc3ca90bb17a8ef80faa
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-27--dispersive-horizon-turning-branch-run-1.txt ; último commit observado: b22fb05 ; sha256 de la copia enviada 797cdda126fce0c5134d4b93bc5890e1830a8b80d2f3e699911db753e3452c1e
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/scripts/compare_turning_branch_heuristic.py ; último commit observado: 71488b0 ; sha256 de la copia enviada c122bc97a8ad15088164e8590fee2f393e8d7667c31e2441f9e19db244cbdae6
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon/reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt ; último commit observado: 75c7e30 ; sha256 de la copia enviada 6a028e1c44b53cd808335fe66aade5f5b968cb694f9dc1dc6dc9aaec15f8ce84
entrada_astra.txt sha256 a44b9ec22a3be634f88623c5204640657ada3cfec04085a32b83df525fe8ea3d
respuesta sha256 057438e2242fec830573337da2690ad50315d303d76f9422c92dbe92f2867cd8
-->

**Veredicto global: `REPAIR_REQUIRED`, limitado al informe de ejecución.** Los seis casos satisfacen `TRANSMISSION_NONZERO_CERTIFIED`. Las cuatro comparaciones estrictas exigidas por el contrato justifican adoptar `T_RET_DECREASING_AT_COMPUTED_L` en el balance de cierre. Las reparaciones afectan a la interpretación de la heurística y a la descripción de lo comprobado. Ninguna requiere repetir la ejecución.

He contrastado el código, el registro y las tablas suministradas. Las derivaciones de sector, normalización, hoja y pendiente que siguen son manuales. La cronología de los commits, la unicidad de la ejecución y los hashes reales de los archivos quedan `[UNVERIFIED]` por esta revisión documental.

### 1. Identificación de rama (R1) — `PASS`

Para los modos propagantes, \(\lambda=e^{-ik}\). Por tanto, \(\Re\lambda>0,\Im\lambda>0\) equivale a \(-\pi/2<k<0\), y cambiar el signo de la parte imaginaria selecciona \(0<k<\pi/2\). `sector` exige que **toda la caja** satisfaga las desigualdades estrictas. Se aplica a `mi['R']`, donde el flujo ya ha sido certificado positivo. Este filtro es esencial porque también hay modos de flujo negativo en el primer cuadrante de \(\lambda\).

El argumento de sectores concuerda con el registro. En la ecuación registrada \(h=2f^2-1-\cos(\omega+k)=0\), las fronteras \(k=0,\pi\) dan \(1-\cos\omega\) y \(1+\cos\omega\), y \(k=\pm\pi/2\) da \(-1\pm\sin\omega\). Ninguna se anula a estas frecuencias, para ningún medio del perfil. El sector \(-\pi/2<k<0\) pasa de un movedor derecho y dos izquierdos interiores a un solo izquierdo exterior. El derecho exterior está en \(0<k<\pi/2\). Esto concuerda con la pérdida del par en el pliegue del argumento escrito del contrato. R1 certifica la selección del modo en el medio interior. El registro mantiene abierta la afirmación global de F1 sobre la frontera de regímenes.

`secs.index('neg')` y `secs.index('pos')` se evalúan después de exigir exactamente una aparición de cada signo. `prop_in` y los primeros miembros derechos de `Bcols` conservan el orden de esa misma `mi['R']`. Al permutar los modos se permutan conjuntamente los índices y las columnas. Hay incluso un control visible en \(z_1\): el registro antiguo imprime primero el derecho de \(k>0\), mientras que el nuevo imprime primero el de \(k<0\).

### 2. Columna y unitariedad (R2) — `PASS`

Cada miembro derecho interior impone amplitud uno en un solo modo incidente y cero en los demás. Si \(x_{rc}\) es la amplitud saliente obtenida con los vectores de Bloch sin normalizar, la fracción de flujo para incidencia unitaria es

\[
|S_{rc}|^2=|x_{rc}|^2\,\frac{|F_r|}{|F_c|}.
\]

Es la expresión de `absS2`. `out_rows` toma las cuatro filas propagantes interiores, salta las evanescentes interiores y toma el único derecho exterior. Por eso su índice en `absS2` es `er = mi['nL'] = 4`, aunque en la solución completa su posición sea `len(int_out)`. La distinción entre ambos índices es correcta.

La suma usa las cinco entradas de `c_ret`. Por otra vía algebraica, el código construye \(S\) con \(\sqrt{|F_r|/|F_c|}\) y comprueba que cada caja de \((S^\dagger S)_{ab}\) contiene \(\delta_{ab}\). Ambas son comprobaciones de consistencia por inclusión. La identidad exacta requiere el argumento de conservación del flujo. Sólo `T_ret` recibe un veredicto por positividad y anchura. `T_cont` queda como dato, conforme a Q2.

### 3. Cotejos (R3) — `PASS`

El bloque de transmisión interior–exterior tiene una sola fila, \((a,b)\). Por Cauchy–Schwarz, el máximo de \(|au_1+bu_2|^2\) sobre entradas de norma uno es \(|a|^2+|b|^2\). Así se obtiene \(\sigma^2=T_{\rm ret}+T_{\rm cont}\).

El primer cotejo selecciona correctamente `F2[sv]` o `F3[(sv,Lv)]` y compara por solapamiento de extremos. Tiene valor como control de correspondencia de casos y de extracción. Comparte los auxiliares, el ensamblaje y la normalización con el cálculo importado. Además, la suma es invariante bajo intercambio de las dos etiquetas, de modo que ese cotejo por sí solo **no detectaría una inversión de ramas**.

El cotejo brusco en \(z_1\) sí discrimina esa inversión. La caja seleccionada por signo da \(0.35726102067870325215\ldots\), solapa `tr.S1[4][1].abs2()` y es disjunta del \(0.60328032410923785982\ldots\) de la otra columna. El orden invertido de impresión proporciona la segunda comprobación de la atribución. Queda confirmada la asociación de \(|t_2|^2\) con \(k<0\) en ese caso, aun compartiendo ambos cálculos el modelo de transferencia.

### 4. Paralelismo — `PASS`

`Pool.map` devuelve los resultados en orden de entrada. `zip(tasks, results)` conserva, por tanto, la asociación de cada caso aunque termine antes otro trabajador. Tras `fork`, cada proceso conserva su copia de `G_CACHE` y de los contextos de precisión. La caché visible usa la clave `(tt, zz)`, los cálculos de aproximaciones fijan su precisión y `tanh_RI` fija `iv.prec` antes de evaluar la exponencial. En el código suministrado no aparece una dependencia del reparto que altere el veredicto.

La frase «todas las comprobaciones se hacen en el padre» es inexacta. El trabajador comprueba, entre otras cosas, la identificación R1 y la contracción del precondicionador, y calcula el booleano de unitariedad. El padre recibe extremos racionales, estados, booleanos y etiquetas. Su `ok(..., True)` de R1 registra una condición ya exigida en el hijo. `NotCertified` vuelve como estado abierto, la falta de regularidad como `S_MATRIX_NOT_ESTABLISHED`, y una excepción ordinaria inesperada se propaga desde `map`. Un estado abierto puede acabar con código de salida cero, por lo que importan los estados del resumen.

Las marcas de los `PASS` del padre son aceptables. El registro muestra **154.0, 154.1 y 155.5 s** después de reunir los resultados. Los mensajes intermedios de los hijos usan el reloj de `fr.note`, iniciado antes. La diferencia de relojes explica también que aparezca un `done` a 546.5 s antes de un `PASS` a 154.0 s.

### 5. Veredictos — `PASS`

Los seis límites inferiores son positivos, incluido el menor, \(0.00031248888433704610\). Los extremos decimales impresos de cada \(T_{\rm ret}\) distan \(10^{-20}\), suficiente por sí solo para el umbral \(10^{-6}\). Como comprobación manual de la decisión del código, estos intervalos **ensanchados** a partir del registro todavía separan todos los casos:

| \(s\) | Brusco | \(L=4\) | \(L=16\) |
|---|---:|---:|---:|
| \(1/50\) | [0.357, 0.358] | [0.131, 0.132] | [0.00031, 0.00032] |
| \(1/200\) | [0.450, 0.451] | [0.373, 0.375] | [0.118, 0.120] |

En ambas filas, el extremo inferior de cada intervalo supera el extremo superior del siguiente. La condición de abandono es falsa en ambas. **No hay motivo contractual para retener el candidato al cierre.** Q3 acordó precisamente estas comparaciones, sin umbral absoluto de barrera. El balance de cierre corresponde todavía al proceso previsto por el contrato.

### 6. Destino del flujo reflejado — `PASS`

La descripción correcta es «el de mayor \(|k|\) **entre los dos modos izquierdos con \(-\pi/2<k<0\)**». Hay además un izquierdo con \(k<-\pi/2\), rotulado `[None]`, cuyo \(|k|\) es mayor. Dentro del sector relevante, \(|k|=\arctan(\Im\lambda/\Re\lambda)\). Las cajas con parte imaginaria \(0.083036\ldots\) y \(0.020043\ldots\) identifican inequívocamente las filas dominantes. En \(L=4,16\) sus pesos respectivos son \(0.84645,0.99681\) para \(1/50\), y \(0.60427,0.86756\) para \(1/200\). Incluso en el caso menos concentrado, \(0.60427\) sobre un flujo reflejado de aproximadamente \(1-0.37397\) supera el 96 %.

**La asignación de hoja también se puede justificar a mano para \(1/200\).** En este sector \(0<f(k)<1\). Con \(E=\arccos f\), las dos elecciones de \(\omega+k\) son \(\pm2E\) módulo \(2\pi\), distinguibles por el signo de

\[
\sin(\omega+k)=\Im(z\bar\lambda)
=\sin\omega\,\Re\lambda-\cos\omega\,\Im\lambda .
\]

Para la fila dominante de \(1/200\), \(\Im\lambda/\Re\lambda>0.020\), mientras que \(\tan\omega=2s/(1-s^2)<0.011\). El signo es negativo. Para la otra fila cercana al origen, el cociente es menor que \(0.007\) y el signo es positivo. En \(1/50\) se obtiene la misma separación comparando los cocientes de las dos cajas con \(\tan\omega\simeq0.0400\). En ambos casos la fila dominante pertenece a \(\omega=-k-2E\), cuya pendiente en \(k\to0^-\) es \(-1+2(4t-1)\). Esto extiende la identificación de la hoja de bajo \(k\) mediante un argumento escrito. El verificador nuevo no ejecutó ese test de hoja.

### 7. Comparación heurística — `REPAIR_REQUIRED`

La pendiente está bien calculada para la **interpolación continua** del perfil muestreado. De \(v_{\rm IR}=8t-3\) y \(t_L(x)=3/8+\tanh(x/L)/16\) se deduce

\[
v_{\rm IR}(0)=0,\qquad |v'_{\rm IR}(0)|=8t'_L(0)=\frac1{2L}.
\]

La identificación de esa derivada con el parámetro físico \(\alpha\) de la fórmula citada sigue `[UNVERIFIED]`. Tampoco es una diferencia finita exacta de la red. Con \(\omega=2\arctan s\), la sustitución en el exponente sí da \(4\pi\omega L\).

No encuentro circularidad numérica. El cálculo de \(S\) selecciona la incidencia por signo y resuelve el matching sin usar \(X\). La unitariedad y la suma \(\sigma^2\) permiten múltiples repartos entre las dos columnas. Los cocientes del informe concuerdan con la salida orientativa, que usa el extremo inferior impreso de \(T_{\rm ret}\). Su alcance es menor de lo que sugieren cuatro filas: \((1/50,4)\) y \((1/200,16)\) tienen casi el mismo \(\omega L\), con \(X=0.11812038\) y \(0.11809421\), pero dan cocientes \(1.1114\) y \(1.0076\). Es una diferencia informativa precisamente porque la coincidencia no viene impuesta.

La frase que requiere reparación es «Finite-L corrections … are visible». Se ven **desviaciones respecto de \(X\)**. Las cuatro observaciones no identifican su causa. El script imprime el SHA256 y el valor impreso concuerda con la referencia abreviada del informe. Su docstring promete una comparación automática que el código no hace.

### 8. Alcance — `REPAIR_REQUIRED`

«Not claimed» delimita adecuadamente los veredictos a los dos valores de \(s\), los tres perfiles y el observable declarado. En «Reading», `T_cont → 1` introduce una lectura asintótica innecesaria. La afirmación que sí sostienen las cajas es que, en cada paso entre los perfiles calculados, **el aumento de \(T_{\rm cont}\) supera el descenso de \(T_{\rm ret}\)**, de modo que crece su suma. La mayor supresión a la frecuencia más alta también se observa en estos datos. Su interpretación como mecanismo de barrera sigue siendo una hipótesis. La atribución bibliográfica exacta del mecanismo y de la fórmula queda `[UNVERIFIED]` con los documentos adjuntos.

### Objeciones por gravedad y reparación concreta

1. **Interpretación física — «Comparison» y «Reading».** Sustituir «se ven correcciones de \(L\) finita» por «se observan desviaciones respecto de \(X\) en los cuatro casos». Sustituir la flecha al límite por la comparación finita de incrementos. Son las dos correcciones relevantes para el cierre científico.
2. **Precisión declarada — «Results».** Cambiar «width below \(10^{-20}\) as printed» por «anchura impresa \(10^{-20}\)». El registro nuevo no imprime las anchuras racionales individuales de \(T_{\rm ret}\). El orden \(10^{-57}\) sí aparece para cantidades del cálculo importado. Basta conservar la cota impresa para justificar todos los veredictos.
3. **Trazabilidad — «Process» y docstring del comparador.** Describir qué valida el trabajador y qué decide el padre. Indicar que las marcas se agrupan tras `map`. En el comparador, cambiar «after a SHA256 check» por «prints the SHA256 of the input log» para describir fielmente la versión ejecutada.
4. **Identificación de filas — «Where the rest … goes».** Especificar el intervalo \(-\pi/2<k<0\) al hablar de «mayor \(|k|\)». Si se incorpora la atribución de hoja en \(1/200\), identificarla como la derivación manual del punto 6.