<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T19:13:00Z  fin: 2026-11-14T19:14:45Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-matchgate-a5.md ; último commit observado: 3fa82c8 ; sha256 de la copia enviada 6575d2363f68733fbbd2a572ce3d2af8cef25d35bfa316fbc57307b27fc10e22
documento: /home/adnac/qca-causal-cones/theory/THIRRING_MATCHGATE_A5_GATE.md ; último commit observado: 915e55f ; sha256 de la copia enviada 2d8f2731513828110b0a0345de8547244a6aa703da3ac10b2dc3e424d48884de
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_matchgate_a5.py ; último commit observado: eae7876 ; sha256 de la copia enviada 8a5de947de8627d81f641ef7cbe1c21be599dae5c59ff99c06597cea50f0cb1a
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-matchgate-a5.txt ; último commit observado: 3fa82c8 ; sha256 de la copia enviada b1af88b87131f9779e0e2be24962214651fbc18022a5dc64e39ac6e9dae217fc
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-comoving-packet.md ; último commit observado: 4e192ca ; sha256 de la copia enviada f016490209ccebdb23cbc3faba35987415ad26b744313755b4151d1b86ea1020
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_comoving_packet.py ; último commit observado: 2685635 ; sha256 de la copia enviada a72db65cf837921d2448315babce39ff93d9ac8077ab9f226abf77f039a9ac55
documento: /home/adnac/qca-causal-cones/sources/valiant-stoc2001.pdf ; último commit observado: a1cfd20 ; sha256 de la copia enviada ff54395f2a04bcffcb8f483bca409d9328aceed2545312d7a35479beb9958572
documento: /home/adnac/qca-causal-cones/sources/quant-ph-0108010v2.pdf ; último commit observado: 7fa79e7 ; sha256 de la copia enviada 71a6c85976f3697a24eb6c32219e6322915f4e2684cd772b25f4f67c3edb271a
documento: /home/adnac/qca-causal-cones/sources/0804.4050v2.pdf ; último commit observado: 7fa79e7 ; sha256 de la copia enviada 5f6ea3d7cf51f6e1981cd9139743161ca3847f59627c6b278c3e6ed2e52d497a
entrada_astra.txt sha256 414c08486ef7f7317c2caaa3706ad5c1b6acbc4d967caac13d391938a9f323db
respuesta sha256 192a3878dfa8f6fdb4125287049f533838da60e7afb66582d812c4f0f0d46300
-->

**Dictamen global: REPAIR_REQUIRED.** La reducción algebraica a matchgates es correcta bajo F. Las reparaciones afectan al dominio de \(W_{ab}\), las hipótesis computacionales, la conclusión sobre universalidad, una afirmación fuera del acoplamiento estudiado y las páginas citadas. No cuestiono F como premisa.

Revisión realizada únicamente sobre los textos suministrados, por lectura y derivación matemática. No he ejecutado los verificadores ni comprobado commits, hashes o imágenes de los PDF; esas comprobaciones quedan **[UNVERIFIED]** en esta revisión.

**1. Formalización de F: REPAIR_REQUIRED, por el dominio declarado.**

Sobre el sector lógico con exactamente un fermión por paquete, \(W_{ab}\) es una representación fiel de la acción por pares con espectadores. En efecto,
\[
c_{by}c_{ax}c^\dagger_{ax}c^\dagger_{by}|0\rangle=|0\rangle,
\]
y la recreación devuelve el orden \(a,b\). Por tanto, sus coeficientes son los de \(V\), sin transposición ni intercambio de columnas.

La elección de \(a\) como paquete inicialmente a mayor coordenada coincide con el contrato y con el informe co-móvil, §4. También respeta el marco libre \(B_{\rm out}\): no añade otra evolución de sabor. Esto representa F; no la prueba ni introduce una interacción adicional con espectadores.

**R1 — aclaración obligatoria de dominio.** Frase: «acts on the fermionic Fock space as the even operator … identity on all other occupations».

La fórmula anula, por ejemplo, el vacío y los estados sin ocupación en alguno de los dos paquetes; no es una puerta unitaria sobre todo Fock. Tampoco especifica una extensión física fuera del código. Se cierra indicando que se utiliza **su restricción al sector de una ocupación por paquete**, donde actúa como identidad sobre los factores espectadores. No hace falta definir ni asumir una extensión unitaria fuera de ese sector.

**2. Signo fermiónico: PASS.**

Con las convenciones declaradas, la acción entre registros ordenados por posición es \(-Pv\). Tras aplicar \(W\), la cadena sigue escrita como \(c^\dagger_a c^\dagger_b\); la base final utiliza \(c^\dagger_b c^\dagger_a\). El intercambio aporta \(-1\) para AA, AB, BA y BB: incluso cuando coinciden los sabores, los modos de paquete son distintos.

Los espectadores no cambian ese signo. Cada monomio de \(W\) contiene cuatro operadores del par y conmuta con cualquier creador de un modo espectador: atravesarlo produce \((-1)^4=1\). Esto prueba el resultado para cualquier número de espectadores, más allá de los tres paquetes del ensayo.

El código implementa correctamente:

- el signo Jordan–Wigner mediante la ocupación de modos anteriores;
- la actuación de derecha a izquierda en `W`;
- la cadena de creación mediante el recorrido invertido de `string`;
- la comparación entre bases inicial y final en `register_map`.

Un \(v\) con 16 símbolos independientes es suficiente para esta identidad lineal: no necesita unitariedad ni conservación de sabor. S3 comprueba un sector limitado, pero el argumento de paridad anterior establece la extensión pertinente. El signo acumulado es global porque la secuencia de cruces está fijada y no depende del sabor.

**3. Adyacencia y coincidencias: PASS, con una precisión sobre la resolución.**

El argumento de continuidad es correcto si «estaba entre ellos» significa en un intervalo inmediatamente anterior a \(t_*\). Una coincidencia exclusivamente doble no puede involucrar posiciones no adyacentes.

Con velocidades distintas, una coincidencia múltiple invierte el bloque: cerca de ella,
\[
x_p(t)-x_q(t)=-(v_p-v_q)(t-t_*).
\]
Una resolución cinemática usa transposiciones adyacentes y cada par una sola vez.

S4 respeta los pares, parámetros y orden temporal. También puede comprobarse algebraicamente sin invocar el recuento 26/26. Escribiendo \(\alpha(t)=ic_t\), \(\beta(t)=b_t\),
\[
c_{xy}=\frac{c_x+c_y}{1+c_xc_y},\qquad
b_{xy}=\frac{b_xb_y}{1+c_xc_y},
\]
se obtienen las igualdades de las dos secuencias en el sector de una excitación; la complementación cubre el de dos. Los sectores restantes son escalares.

Para \(k\ge4\), **cada resolución especificada** sigue siendo simulable, aunque no se haya demostrado unicidad. Esto no permite simular una elección desconocida o no computable de resolución. La distinción del informe es válida en ese sentido. Además, S4 y la conmutación de cruces disjuntos proporcionan las relaciones necesarias para demostrar independencia entre descomposiciones reducidas; esa ampliación no es necesaria para simular un circuito dado.

**4. Clase de puerta: PASS.**

Poniendo \(c=(r^2-1)/(r^2+1)\), se tiene \(\beta^2+c^2=1\). Así,
\[
A=-I_2,\qquad B=-(\beta I_2+icX)
\]
son unitarios y ambos tienen determinante uno. El signo de \(\alpha\) coincide con el repositorio.

En Valiant, p. 118, la primera identidad es precisamente \(\det A=\det B\); las otras cuatro se anulan por el patrón de paridad. Junto con los ocho ceros y \(B(4,4)=-1\), esto satisface la Proposición 3. Las posibles pérdidas de signos del texto extraído en las cuatro identidades triviales no afectan a esta conclusión.

La correspondencia de convenciones merece explicitarse, pero **no produce un error en esta familia**:

- Valiant coloca entradas en filas y salidas en columnas; frente a la convención del verificador corresponde transponer.
- La lectura complementada de p. 120 corresponde a complementar ambos bits de entrada y salida.
- Aquí \(G^T=G\) y \((X\otimes X)G(X\otimes X)=G\). Intercambiar simultáneamente los dos índices centrales tampoco cambia \(G\).

Por tanto, la matriz carácter adecuada es efectivamente la misma matriz numérica. Comprobar solo los índices centrales no explica todo este puente; añadirlo sería una aclaración recomendable.

La segunda vía también es correcta:
\[
PV=e^{\,i\theta(XX+YY)/2}.
\]
El signo positivo sigue de \(\sin\theta=c\). Con la matriz explícita `sm` del código, la identidad Jordan–Wigner es correcta; para posiciones adyacentes las cadenas anteriores se cancelan. Estos fermiones del registro lógico no deben identificarse con los modos físicos \(c_{pf}\).

**5. Hipótesis de los teoremas: REPAIR_REQUIRED.**

Contraste de las siete filas:

1. **Adyacencia:** satisfecha. Valiant, Main Theorem (b), está en **p. 120**, no 119; T–D, pp. 3–4; J–M, p. 2.
2. **Patrón y realización:** satisfechos, Valiant, Proposición 3, p. 118.
3. **Bloques unitarios:** satisfechos, T–D, pp. 3–4; J–M, ecuación (1), p. 2.
4. **Entrada:** correcta: base computacional para Valiant/T–D; producto general para J–M.
5. **Salida:** T–D, p. 4, establece explícitamente probabilidades de asignaciones de cualquier subconjunto y muestreo. J–M, pp. 2–3, solo garantiza aquí una línea y \(\langle Z_k\rangle\). En Valiant, Theorem 4 está en **p. 120** y Measurement Theorem en **p. 121**.
6. **Adaptatividad:** no se necesita. T–D admite una extensión concreta, con mediciones completas de ocupación y sin reutilizar modos medidos (§V, p. 16); no adaptatividad arbitraria.
7. **Tamaño y uniformidad:** solo está demostrado el número cuadrático de puertas.

**R2 — error de hipótesis y precisión.** Frases: «Poly-size, uniform family … met» y «precision handling is that of the cited theorems».

El número de cruces no demuestra uniformidad. F no prescribe representaciones finitas de \(K_p,x_p(0)\), su generación, ni el coste de ordenar tiempos y resolver empates. Que los \(r\) sean algebraicos para \(K\) racionales tampoco basta para afirmar evaluación exacta en tiempo polinómico de bits.

Se cierra especificando una descripción clásica eficiente de la arquitectura: tamaño de entrada, generación uniforme, cálculo de parámetros y orden de cruces —incluidos empates— y coste en bits. Debe distinguirse evaluación algebraica ideal de aproximación: probabilidades con error aditivo declarado y muestreo con error declarado, por ejemplo en distancia de variación total. Para estados producto generales también se necesita acceso eficiente a sus amplitudes.

«Probabilidades de cualquier subconjunto» significa **una asignación consultada**, no imprimir una tabla de \(2^k\) probabilidades.

**R3 — error documental.** Las referencias «Main Theorem … p. 119», «Thm 4, p. 119» y «Measurement Theorem, p. 120» deben corregirse a **120, 120 y 121**, respectivamente.

La inferencia a \(P\) de J–M, p. 3, es legítima una vez asegurada uniformidad, para aceptación mediante una línea con brecha acotada: basta aproximar su probabilidad con error menor que \(1/6\). No se deduce automáticamente para cualquier predicado clásico sobre muchas salidas.

**6. Alcance: REPAIR_REQUIRED.**

La separación entre verificaciones algebraicas, argumentos escritos y F está bien planteada. No afirma demostrar F ni un no-go general de Thirring.

**R4 — exceso en la conclusión.** Frases: «Hence … do not give universal quantum computation» y «excluded as a route to universality».

La simulabilidad eficiente, por sí sola, no demuestra una separación incondicional respecto de computación cuántica universal. J–M, pp. 3 y 16, distingue expresamente esta cuestión. Se cierra afirmando simulabilidad y pertenencia a \(P\) bajo las condiciones anteriores; una universalidad eficiente implicaría \(P=BQP\). Si se pretende imposibilidad algebraica de implementar unitarias arbitrarias, debe darse un argumento estructural separado.

**R5 — error literal fuera del acoplamiento estudiado.** Frase: «For chi != pi/2 and r != 1, P V is not a matchgate».

El resultado adjunto es módulo \(\pi\): \(\chi=3\pi/2\) también satisface la condición. Se cierra escribiendo \(\chi\not\equiv\pi/2\pmod\pi\), donde la familia esté definida, o suprimiendo esa afirmación.

Las reparaciones obligatorias son **R1–R5**. F permanece asumida; el signo \(-1\), la adyacencia y la identificación de la puerta como matchgate no requieren corrección algebraica.