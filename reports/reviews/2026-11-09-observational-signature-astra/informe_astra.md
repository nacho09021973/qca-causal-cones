<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.167.0)
inicio: 2026-11-09T12:35:19Z  fin: 2026-11-09T12:41:54Z
documento: /home/ignac/qca-causal-cones/theory/OBSERVATIONAL_SIGNATURE_SATURATION_GATE.md ; último commit observado: 21af1dd ; sha256 de la copia enviada 9cd7a1ee04aa89071bf5ba3f5dfabcec221cfef9fb039793d2d4529e067f3d84
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--observational-signature-saturation.md ; último commit observado: f9a638e ; sha256 de la copia enviada e611079728cb6e918d30670498417365574c42fd0fcc651131c00517e0ccd1c7
documento: /home/ignac/qca-causal-cones/scripts/verify_observational_signature_gate.py ; último commit observado: 658845a ; sha256 de la copia enviada 785a6b1dfca7934716c2944a80706dbabe1977a5be6ab0a4fc60f1089aacd31a
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--observational-signature-saturation.txt ; último commit observado: f9a638e ; sha256 de la copia enviada f9fcf445bfbe0d63cbdeaea5820aa0dbb9b7c00b93e2dd47ba0158664fad029f
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 70dd98c ; sha256 de la copia enviada 5aaaea6af9704abb2a1a16613f1ede7fc1639956800e66d2580824484b31bec9
documento: /home/ignac/qca-causal-cones/theory/THREE_VELOCITIES.md ; último commit observado: 95f423f ; sha256 de la copia enviada bf1a746c557408d1ab5249210fba0566502677ab302e1068886f39b31d32ba41
entrada_astra.txt sha256 fb07907c5f3182124f135039547d5e94e0377e4518985c956903f11320ec124c
respuesta sha256 6b62dde6d36d6da4a257c446b44117fb918e9392128bdae9bb9c337831ba57d7
-->

**Veredicto: reparación necesaria.** La cota de L2/L3 y la existencia local de excitaciones super‑\(c_0\) se sostienen matemáticamente a partir de las identidades y coeficientes declarados. La independencia afirmada en la sección 5 no está demostrada. Además, la certificación por intervalos tiene un hueco en el tratamiento de las constantes, y la clasificación de L3s4 necesita dos correcciones.

Esta es una revisión manual de los adjuntos. No he ejecutado el script. Las identidades de los símbolos importados y los resultados numéricos del registro quedan **[UNVERIFIED] como resultados de ejecución independiente**: sus constructores no están adjuntos. Sí puedo comprobar las consecuencias matemáticas de esas identidades y la lógica del código mostrado. El 19/19 no sustituye esas comprobaciones.

Las derivaciones críticas son las siguientes.

1. **L2/L3: la prueba global es correcta, condicionada a las identidades del símbolo.**

   Para un unitario \(2\times2\) con
   \[
   \det U=1,\qquad \operatorname{Tr}U=2C,\qquad
   C=\prod_j\cos p_j,
   \]
   el polinomio característico es
   \[
   \lambda^2-2C\lambda+1.
   \]
   Sus eigenvalores son \(e^{\pm i\omega}\), con
   \[
   \omega=\arccos C.
   \]
   Esto comprueba la reducción espectral; que los símbolos concretos de L2/L3 satisfagan esas identidades sólo consta aquí en el script y su registro.

   Si \(p_j=k_j/L\), donde \(C^2\ne1\),
   \[
   \partial_{k_j}\omega=
   \frac{\sin p_j\prod_{i\ne j}\cos p_i}
        {L\sqrt{1-C^2}}.
   \]
   Por tanto, tomando \(a_j=\cos^2p_j\),
   \[
   L^2\|\nabla_k\omega\|^2=
   \frac{\sum_j(1-a_j)\prod_{i\ne j}a_i}
        {1-\prod_j a_j}.
   \]
   La fórmula del informe es correcta.

   También lo es la cota multilineal. En un vértice de \([0,1]^d\), sea \(m\) el número de coordenadas nulas. Para
   \[
   f=1-\prod_j a_j-\sum_j(1-a_j)\prod_{i\ne j}a_i
   \]
   se obtiene \(f=0\) si \(m=0\) o \(m=1\), y \(f=1\) si \(m\ge2\). Una función multiafín es una combinación convexa de sus valores en los vértices: luego \(f\ge0\).

   Hay una segunda comprobación directa: interpretando \(a_j\) como probabilidades de éxitos independientes, \(f\) es la probabilidad de tener al menos dos fallos. En particular,
   \[
   f_2=(1-a_1)(1-a_2),
   \]
   y
   \[
   f_3=(1-a_1)(1-a_2)
      +(1-a_3)\bigl[(1-a_1)a_2+a_1(1-a_2)\bigr].
   \]
   Ambos son manifiestamente no negativos.

   Finalmente,
   \[
   C=1-\frac{|k|^2}{2L^2}+O(|k|^4)
   \quad\Longrightarrow\quad
   \omega=\frac{|k|}{L}+O(|k|^3),
   \]
   de modo que \(c_0=1/L\). Sobre un eje, fuera de los cruces, la velocidad alcanza exactamente \(1/L\). Las dos ramas tienen la misma norma del gradiente. Así,
   \[
   V_{\rm grp}^{\max}=c_0.
   \]

   Los puntos donde \(C^2=1\) requieren excluir el gradiente no definido o considerar límites; no invalidan el supremo. Análogamente, en L1, \(\omega=|k|\) corresponde a la zona principal: globalmente hay plegamiento de cuasienergía, aunque la rapidez de las ramas regulares sigue siendo uno.

2. **El signo positivo de \(\beta\) sí demuestra existencia local, pero no un punto de la rejilla finita.**

   Para una rama analítica a lo largo del rayo, con \(t>0\),
   \[
   \varepsilon_+(t\hat n)-\varepsilon_0
   =c_0\bigl[t+\beta(\hat n)t^2+\alpha(\hat n)t^3+O(t^4)\bigr],
   \]
   se puede derivar:
   \[
   \hat n\cdot\nabla\varepsilon_+
   =c_0\bigl[1+2\beta(\hat n)t+3\alpha(\hat n)t^2+O(t^3)\bigr].
   \]
   Como
   \[
   \|\nabla\varepsilon_+\|
   \ge \hat n\cdot\nabla\varepsilon_+,
   \]
   si \(\beta(\hat n)>0\), existe un intervalo \(0<t<\delta\) donde la rapidez supera \(c_0\).

   La analiticidad importa: no basta con derivar formalmente un resto \(O(t^4)\) sin regularidad. Aquí se justifica para un símbolo unitario analítico restringido a un rayo: puede elegirse un logaritmo hermítico local y, para \(c_0>0\), la separación lineal de las dos ramas permite una elección analítica unilateral. Para L3s4, los dos conglomerados tienen eigenvalores distintos en el nodo, y el mismo argumento vale para cada \(a\) fijo con \(0<a<1\). No proporciona un radio uniforme en \(a\).

   Las sustituciones de los rayos dan efectivamente:
   \[
   \beta_{\mathrm{L5a,L5b}}(+111)=\frac19,\qquad
   \beta_{\mathrm{L4}}(-111)=\frac19,
   \]
   \[
   \beta_{\mathrm{L6a}}(60^\circ)=\frac{\sqrt{15}}{36},
   \qquad
   \beta_{\mathrm{L6b}}(0^\circ)=\frac{\sqrt{15}}{18}.
   \]
   En L5b se entiende el bloque con el signo correspondiente.

   Para el signo superior de L3s4,
   \[
   \beta(+111)+\beta(-111)
   =\frac{\sqrt3(1-a^2)}{3a}>0.
   \]
   Al menos uno de esos rayos tiene \(\beta>0\), para todo \(0<a<1\). Esta demostración es suficiente para la existencia local super‑\(c_0\).

   **No demuestra que alguno de los ocho radios de `GRID` esté dentro de ese intervalo.** La existencia local y el testigo contractual en la rejilla son resultados distintos.

3. **La fórmula de velocidades del bloque \(2\times2\) es correcta como pareja no ordenada.**

   Escribamos
   \[
   d=\det U=e^{i\phi_d},\qquad
   \lambda_\pm=e^{i\phi_d/2}e^{\pm i\theta}.
   \]
   Con la convención \(\lambda=e^{-i\varepsilon}\),
   \[
   \varepsilon_\pm=-\frac{\phi_d}{2}\mp\theta
   \quad\bmod 2\pi.
   \]
   Si \(T=|\operatorname{Tr}U|^2\), entonces
   \[
   T=4\cos^2\theta,\qquad
   \nabla T=-8\cos\theta\sin\theta\,\nabla\theta.
   \]
   Por ello, para \(0<T<4\), las dos velocidades forman el conjunto
   \[
   \left\{
   -\frac12\nabla\phi_d
   \ \pm\
   \frac{\nabla T}{2\sqrt T\sqrt{4-T}}
   \right\}.
   \]
   El signo perdido al usar \(T\) sólo intercambia las ramas. No hay un factor dos incorrecto en el script.

   Además,
   \[
   \nabla\phi_d=
   \frac{\operatorname{Im}(\bar d\,\nabla d)}{|d|^2}.
   \]
   El código puede omitir el denominador porque presupone unitariedad exacta, de donde \(|d|=1\). La conversión desde las fases \(p_j\) a \(k\), y la división entre tres para L6b, coinciden con las convenciones declaradas.

   La condición \(T<4\) excluye una degeneración dentro del bloque. \(T>0\) evita la singularidad de esta representación mediante el módulo cuadrado de la traza; \(T=0\) no es en sí un cruce de eigenvalores.

   El chequeo mostrado establece regularidad **en el punto evaluado**. Que el bloque sea unitario, invariante y contenga las dos ramas del nodo depende de los constructores y descomposiciones importados. El informe padre lo describe, pero el script nuevo no vuelve a comprobarlo. Tampoco identifica cuál de `plus` y `minus` es la rama superior: para demostrar existencia en cualquiera de las dos basta, pero debe conservarse esa distinción.

4. **L3s4 refuta Hh en el sentido de una rama seleccionada, con dos excepciones de clasificación.**

   Poniendo \(x=a^2\),
   \[
   \beta=B_0+B_3n_1n_2n_3,\qquad
   B_0=\frac{\sqrt3(1-x)}{6a},\quad
   B_3=\frac{\sqrt3(2x-1)}{3a}.
   \]
   Puesto que
   \[
   |n_1n_2n_3|\le\frac1{3\sqrt3},
   \]
   resulta
   \[
   \min_{\hat n}\beta
   =\frac{\sqrt3(1-x)}{6a}-\frac{|2x-1|}{9a}.
   \]
   La positividad estricta equivale a
   \[
   3\sqrt3(1-x)>2|2x-1|,
   \]
   que, para \(0<x<1\), da exactamente
   \[
   x<x_c=\frac{19-6\sqrt3}{11}.
   \]

   Por tanto, la rama superior del conglomerado de signo positivo tiene avance a primer orden en todas las direcciones para \(a^2<x_c\). Esto refuta Hh bajo la lectura del contrato que asigna la firma a esa rama. No significa que todas las ramas de L3s4 tengan avance: el conglomerado opuesto tiene el signo contrario.

   Las correcciones necesarias son:

   - En \(a^2=x_c\), \(\beta\ge0\), con ceros en ciertas diagonales. **No toma ambos signos.** En esas direcciones nulas, el comportamiento siguiente requiere términos superiores.
   - En \(a^2=1/2\), \(B_3=0\) y
     \[
     \beta=\frac{\sqrt6}{12}.
     \]
     La corrección principal es **isótropa**. La etiqueta incondicional «anisotropic» del script es incorrecta para ese parámetro.

   Para las demás filas, orden y signos se leen correctamente de las fórmulas adjuntas: \(\alpha\le0\) en L2/L6e/L3; \(\alpha<0\), constante, en L6c/L6d/L6f; y \(\beta\) cambia de signo en las filas impares indicadas. «Orden 1» u «orden 2» describe el primer coeficiente no idénticamente nulo sobre la esfera: no asegura ese mismo orden sobre sus direcciones de anulación.

Las objeciones, ordenadas por gravedad, son estas.

1. **La independencia de la sección 5 y la afirmación 1.2 no están demostradas.**

   Sean
   \[
   A:\ c_0=r_{\rm in},
   \qquad
   B:\ V_{\rm grp}^{\max}=c_0.
   \]
   Los resultados declarados proporcionan:

   | Caso | Filas |
   |---|---|
   | \(A\land B\) | L2, L3 |
   | \(A\land\neg B\) | L5a, L5b, L4 |
   | \(\neg A\land\neg B\) | L6a, L6b, L3s4 |
   | \(\neg A\land B\) | Ninguna demostrada |

   Se demuestra que \(A\) **no implica** \(B\). No se demuestra que \(B\) no implique \(A\). Los resultados negativos de una búsqueda finita en L6c/L6d/L6f no rellenan la última casilla.

   **Reparación:** sustituir «son independientes» por «alcanzar el techo isótropo no garantiza que ninguna excitación supere \(c_0\); la implicación inversa queda abierta». La afirmación 1.2 debe limitarse a la coincidencia de firmas de retraso y de resultados negativos de búsqueda.

   Hay una conclusión distinta que sí se sostiene: la insuperabilidad espectral no implica \(S_{\max}\). L2/L3 ya son ejemplos, pues \(V_{\rm grp}^{\max}=c_0<1=V_{\rm causal}^{\max}\), según las normalizaciones declaradas. Esto permite conservar una conclusión limitada sobre «identificar \(c\) con el reloj», distinguiéndola de \(S_{\rm in}\).

2. **La certificación rigurosa por intervalos no queda cerrada —informe §4; `ivnum`, `scale_of`, `prepare_block`.**

   `ivnum` evalúa con `sp.N(e,70)` y ensancha el resultado en \(10^{-55}\). Eso no incluye una demostración de que
   \[
   |e-\operatorname{N}(e,70)|<10^{-55}.
   \]
   Para las constantes pequeñas y radicales esperables, el margen parece holgado; pero «70 cifras solicitadas» no es una cota de error certificada. El redondeo exterior posterior de `iv.mpf` encierra los extremos decimales suministrados, no demuestra por sí mismo que éstos encierren el número exacto.

   Por otro lado, `scale_of` usa `float(nrm)` para seleccionar la normalización. Por tanto, la frase **«No floating point enters a verdict» es literalmente falsa**: esas comparaciones influyen en \(L\) y, con ello, en las velocidades. No he encontrado evidencia de que hayan elegido mal en estas filas; el defecto es de garantía y descripción.

   La asociación de `sqrt` y `mpf` con operaciones de intervalos es adecuada. Sin los símbolos importados y las funciones generadas no puedo comprobar que todas las constantes y operaciones restantes queden cubiertas.

   **Reparación:** proporcionar encerramientos certificados de las constantes exactas y elegir \(L\) mediante comparaciones exactas. Explicitar también dónde se garantiza la unitariedad de los bloques; `detmod` se registra, pero no se exige. Hasta entonces, aceptaría esos números como resultados reportados compatibles con la prueba local, no como certificados rigurosos auditados.

   Este hueco **no elimina** la existencia super‑\(c_0\) obtenida mediante \(\beta>0\).

3. **El diagnóstico de imposibilidad contractual es demasiado fuerte —informe §4; contrato §§3 y 6.**

   Un \(k_*\) de coordenadas algebraicas y radio racional es perfectamente coherente. Que sus exponenciales sean trascendentes impide tratarlas en general como radicales algebraicos; **no impide demostrar desigualdades exactas sobre ellas**. Por ejemplo, pueden encerrarse mediante series con restos acotados y extremos racionales.

   La desviación real es utilizar aritmética de punto flotante con redondeo dirigido para alimentar el veredicto, cuando el contrato reservaba el punto flotante a ilustraciones.

   **Reparación:** describirlo como una modificación del método, no como incompatibilidad matemática de los requisitos. Los intervalos son científicamente aceptables si sus garantías están completas, pero no constituyen cumplimiento literal del contrato congelado.

   Además, L3s4 debe distinguir `SUPER_C_EXISTENCE_NEAR_NODE` de un testigo contractual: no se ha dado el punto exigido ni se ha demostrado que pertenezca a la rejilla finita.

4. **La firma de L3s4 necesita corregir la frontera y el parámetro isótropo —informe §§1–2; `main`; registro; padre §3.3.**

   Son errores algebraicos concretos, derivados arriba: «else both signs» falla en \(a^2=x_c\), y «anisotropic» falla para la corrección principal en \(a^2=1/2\).

   **Reparación:** separar \(a^2<x_c\), \(a^2=x_c\) y \(a^2>x_c\), y registrar la isotropía principal en \(a^2=1/2\). Hh sigue refutada para el intervalo estricto, identificando la rama elegida bajo \(H_\gamma\).

5. **El significado físico de “techo” necesita respetar THREE_VELOCITIES §5.**

   El contrato define \(S_{\rm in}\) mediante el cuerpo causal de **un paso**. El documento adjunto advierte expresamente que éste proporciona una cota geométrica y que no debe identificarse automáticamente con la propagación asintótica realizable.

   **Reparación:** usar «techo geométrico isótropo del cuerpo de un paso». Una fila con \(c_0<r_{\rm in}\) no queda demostrada, sólo por eso, por debajo de su propio techo dinámico asintótico. Esta precisión no altera las comparaciones algebraicas con \(c_0\), pero limita su interpretación.

6. **El script respalda menos afirmaciones de las que puede sugerir el 19/19 —informe §6.**

   Por inspección:

   - Las firmas y el umbral de L3s4 se transcriben o codifican como texto; no se verifican en esta ejecución.
   - Los chequeos de existencia local verifican signos, no regularidad analítica ni pertenencia a la rejilla.
   - Las etiquetas de éxito de los intervalos dependen de la ruta numérica antes discutida.
   - Una excepción en la búsqueda puede terminar etiquetada como `NO_WITNESS_ON_DECLARED_RAYS`; debería ser `OPEN (evaluation failed)`. No consta que ocurriera en el registro adjunto.

   No todas las llamadas con predicado `True` son vacías: varias sólo se alcanzan después de una condición efectiva. Pero el recuento mezcla resultados calculados, consecuencias matemáticas y etiquetas; no son diecinueve pruebas independientes de todo el informe.

   **Reparación:** ajustar las etiquetas a lo efectivamente comprobado y separar las firmas heredadas de las verificaciones nuevas. La promoción del padre también queda **[UNVERIFIED]**: el documento adjunto todavía dice `PROMOTION_PENDING`, aunque una decisión posterior podría explicar la discrepancia.

Una precisión adicional afecta al diccionario de llegada. Si \(v=c_0(1+\delta)\), entonces
\[
\frac{\Delta T}{D/c}=\frac1{1+\delta}-1
=-\delta+O(\delta^2).
\]
La igualdad con menos la corrección de velocidad es de **orden principal**, no exacta. Así entendida, los signos y órdenes utilizados son correctos. Para L3s4, además, la energía de la excitación debe medirse respecto a \(\varepsilon_0\), como en la expansión padre.

**El alcance que aceptaría** es el siguiente: dadas las identidades espectrales y los coeficientes declarados, L2/L3 satisfacen exactamente \(V_{\rm grp}^{\max}=c_0\), Hg queda refutada, y las seis filas con \(\beta\) indicada tienen excitaciones super‑\(c_0\) suficientemente cerca del nodo. Hh queda refutada para la rama especificada de L3s4 y \(a^2<x_c\).

También aceptaría `DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS` como conclusión **parcial, condicional a \(H_\gamma\) y restringida a las filas y ramas declaradas**, tras corregir L3s4. La justificación son las diferencias concretas de firmas, no simplemente que no se cumpla la condición de abandono. No aceptaría todavía los puntos como certificados rigurosos independientes, el cumplimiento literal del contrato, ni la independencia entre \(S_{\rm in}\) e insuperabilidad.