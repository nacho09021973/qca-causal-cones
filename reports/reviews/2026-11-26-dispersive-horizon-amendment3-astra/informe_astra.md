<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-26T12:35:48Z  fin: 2026-11-26T12:38:37Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment3-astra/amendment3.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 046354617c56f64a6e0313c4d2f2f05e2f0e842e024f29675853bd98dc5a0540
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md ; último commit observado: f9dce97 ; sha256 de la copia enviada dc35f5e00d3356325aa0447b70df53effe81cef37ca6037263cd4fc2daaa6e90
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment2-astra/informe_astra.md ; último commit observado: f9dce97 ; sha256 de la copia enviada ee109fe4932f4964d067a2914cd730cb700ca24da6ab16cdd3565dbee8db5a87
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_amendment3.py ; último commit observado: f9dce97 ; sha256 de la copia enviada 535dec08c127a0db0cdbebb6ae7fa8ed1b876e42a42e495f02cbcd97f3067e27
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_amendment2.py ; último commit observado: b1c6d75 ; sha256 de la copia enviada b6c68dc431aba0b21425b1e24a3329ffbe560e673250261c234e064d0dcff243
entrada_astra.txt sha256 36896ad0f60fa80427bfdaab440c4ee82ece3c024670a0759b67f358b7168d78
respuesta sha256 a7282289ae2bfd7ab381f70e28d11ca94ef4c56fd18f5d4fb1aef6c75ec2862b
-->

**Veredicto global: PASS**, en el alcance matemático de la Enmienda 3. No encuentro un fallo que exija reparación. Las conclusiones nuevas se sostienen mediante derivación manual y el código adjunto comprueba los ingredientes que declara, con las precisiones siguientes.

No he ejecutado código. Quedan **[UNVERIFIED]** la ejecución efectiva, los resultados impresos, la identidad histórica de los bytes y el contenido de los archivos no adjuntos. Tomo la identidad característica y la correspondencia de Bloch anteriormente revisadas como premisas del alcance solicitado; no reabro las 144 entradas. El informe de Astra no se utiliza como fuente probatoria.

| Punto | Veredicto |
|---|---|
| 1. Jordan \(3+1\), nulidades y cuerpo algebraico | **PASS** |
| 2. Contacto exacto \((u-1)^2\), J2 | **PASS** |
| 3. Curvatura y Jordan del borde interior | **PASS** |
| 4. Cociente y extremo en \(t=7/16\) | **PASS** |
| 5. Diez comprobaciones del verificador | **PASS**, por inspección, con la limitación del recuento indicada abajo |
| 6. Alcance y atribución | **PASS** |

**1. Las nulidades determinan inequívocamente \(3+1\).**

Sea \(d_j=\dim\ker K^j\), con \(d_0=0\). Para la parte nilpotente asociada a \(\lambda_0\), el número de bloques de tamaño al menos \(j\) es
\[
b_j=d_j-d_{j-1}.
\]
La sucesión propuesta da
\[
(b_1,b_2,b_3,b_4)=(2,1,1,0).
\]
Hay dos bloques, exactamente uno alcanza tamaño dos y ese mismo alcanza tamaño tres; ninguno alcanza tamaño cuatro. Por tanto, la partición es **\(3+1\)**. La estabilización \(d_3=d_4\) excluye bloques mayores: no hace falta conocer por separado la multiplicidad algebraica para esta deducción.

La elección del cuerpo es correcta. En el horizonte,
\[
p=\frac{\sqrt6}{4},\qquad q=\frac{\sqrt{10}}4,\qquad
p^2-q^2=-\frac14,\qquad -2pq=-\frac{\sqrt{15}}4.
\]
Como
\[
\sqrt{15}=\frac{\sqrt6\sqrt{10}}2,
\]
los coeficientes de las monedas y sus combinaciones racionales pertenecen a
\[
F=\mathbb Q(\sqrt6,\sqrt{10}).
\]
Los denominadores pertinentes son no nulos. Los productos y los inversos no requieren ampliar el cuerpo.

Otra descripción concreta es
\[
\alpha=\sqrt6+\sqrt{10},\qquad \alpha^4-32\alpha^2+16=0,
\]
con
\[
\sqrt6=\frac{\alpha-4/\alpha}{2},\qquad
\sqrt{10}=\frac{\alpha+4/\alpha}{2}.
\]
Esto confirma que ambas raíces, incluidos sus productos, admiten representación exacta en un único cuerpo algebraico.

Por inspección, `R`, `sqrt` y `radsimp` no introducen aproximaciones numéricas. `convert_to(K_field)` exige convertir las entradas al dominio declarado; no es una conversión a coma flotante ni un cálculo de rango por tolerancia. Una conversión imposible abortaría, sin quedar capturada. Una vez realizada, las operaciones de `DomainMatrix` son operaciones exactas en ese cuerpo. Además, extender escala de \(F\) a \(\mathbb C\) conserva el rango, pues conserva la anulación o no anulación de los menores.

Esto valida **el método**. No certifica aquí su ejecución concreta ni permite inspeccionar la implementación ausente de `rv.M_report`.

Hay también una comprobación manual de la partición. Expandiendo directamente
\[
f(k)=-\frac3{32}\cos3k+\frac{35}{32}\cos k
\]
se obtiene
\[
f(k)=1-\frac{k^2}{8}-\frac{13}{48}k^4+O(k^6).
\]
La rama analítica con pendiente positiva satisface
\[
E(k)=\frac{k}{2}+\frac{35}{64}k^3+O(k^5),
\]
y, por tanto,
\[
\Omega_+(k)=\frac{35}{32}k^3+O(k^5),\qquad
\Omega_-(k)=-2k+O(k^3).
\]
La rama analítica puede construirse mediante
\[
E(k)=2\arcsin\!\left(k\sqrt{\frac{1-f(k)}{2k^2}}\right).
\]
Así, el determinante estacionario tiene orden exactamente cuatro en \(k\), y también en \(\lambda-1\).

Para obtener el tamaño del bloque, no basta ese orden. La matriz analítica \((W(k)-I)/k\) tiene en cero autovalores distintos \(\pm i/2\), de modo que admite autovectores analíticos locales. En la rama cúbica, poniendo \(h=\lambda-1\), existe un vector de Bloch analítico no nulo tal que
\[
z(h)=1+O(h^3),\qquad M(z(h))Y(h)=(1+h)Y(h).
\]
Al desarrollar \(Y=Y_0+hY_1+h^2Y_2+\cdots\), resulta
\[
KY_0=0,\qquad KY_1=Y_0,\qquad KY_2=Y_1.
\]
Existe una cadena de longitud tres. En el nodo, \(U(0)=I\), por lo que los dos espinores independientes dan geométrica dos mediante la correspondencia de Bloch. Algebraica cuatro, geométrica dos y una cadena de longitud tres fuerzan \(3+1\).

Finalmente,
\[
W(k+\pi)=-W(k),\qquad U(k+\pi)=-U(k)
\]
traslada el argumento a \((-1,-1)\). Esta vía manual reproduce las nulidades esperadas sin calcular rangos.

**2. J2 sí decide que el contacto es exactamente doble.**

La expansión del polinomio definido en el código da
\[
P_{3/8}(u)=\frac{105}{64}(u-1)^2(4-3u).
\]
En consecuencia,
\[
\left.\frac{P_{3/8}(u)}{(u-1)^2}\right|_{u=1}
=\frac{105}{64}\ne0.
\]
Equivalentemente, el resto al dividir por \((u-1)^3\) es
\[
\frac{105}{64}(u-1)^2\ne0.
\]

J2 comprueba ambas cosas: divisibilidad por el cuadrado y no divisibilidad por el cubo, además de la evaluación no nula del cociente. La última condición es redundante, pero correcta. Aquí los coeficientes son racionales exactos: no hay ambigüedad de reconocimiento de cero.

La conexión con el contacto cúbico requiere además el argumento analítico, no solo divisibilidad polinómica. Se comprueba que
\[
u-1=-k^2+O(k^4),\qquad \sin^2E=\frac{k^2}{4}+O(k^4).
\]
Usando la identidad de B1 y la rama \(v(0)=0\),
\[
P_{3/8}(u(k))=\frac{105}{64}k^4+O(k^6)
\quad\Longrightarrow\quad
v(k)=\frac{105}{32}k^2+O(k^4).
\]
Integrando se recupera \(\Omega_+=(35/32)k^3+O(k^5)\). Es consistente con la expansión anterior.

**3. El borde interior es un mínimo no degenerado con un bloque de Jordan dos.**

En \(0<k<\pi/2\), con \(C=\cos k\),
\[
E'=\frac{\sin k\,g'(C)}{\sin E}.
\]
Por ello,
\[
\begin{aligned}
P_t(u(k))
&=4\sin^2k\,g'(C)^2-\sin^2E\\
&=\sin^2E(4E'^2-1)
=\sin^2E\,v(v+2).
\end{aligned}
\]
Esta identidad usa \(\sin E\ne0\), condición que debe mantenerse al interpretar la cancelación formal de B1.

Al derivar y evaluar en \(v(k_*)=0\), desaparece el término que contiene la derivada de \(\sin^2E\):
\[
P_t'(u_*)u'(k_*)=2\sin^2E(k_*)v'(k_*)
=2\sin^2E(k_*)\Omega_+''(k_*).
\]
El factor dos es correcto.

Para \(t=5/16\), la expansión directa da
\[
P_{5/16}(u)=\frac3{1024}(1-u)
\left[2625(u-1)^2+5(u-1)-16\right].
\]
Escribiendo \(D=\sqrt{168025}\), la raíz interior es
\[
u_*=\frac{5245-D}{5250}.
\]
La comparación entera utilizada por B2 es suficiente:
\[
0<168025<5245^2=27\,510\,025
\]
implica \(0<D<5245\), luego \(u_*>0\). Además,
\[
5245-D<5245<5250,
\]
de donde \(u_*<1\).

En esa raíz, la derivada del cuadrático es
\[
5250(u_*-1)+5=-D.
\]
Como el cuadrático se anula,
\[
P_{5/16}'(u_*)=-\frac3{1024}(1-u_*)D<0.
\]
También
\[
u'(k_*)=-\sin2k_*<0.
\]

La positividad necesaria de \(\sin E\) se obtiene sin evaluar funciones trascendentes:
\[
A=-\frac{15}{128},\qquad g(0)=0,\qquad g(1)=1,
\]
y
\[
g'(C)-g'(1)=12A(C^2-1)\ge0,\qquad g'(1)=\frac1{16}>0.
\]
Así, \(g\) es estrictamente creciente en \([0,1]\). Puesto que \(C_*=\sqrt{u_*}\in(0,1)\),
\[
0<g(C_*)<1,\qquad 0<E(k_*)<\frac\pi2.
\]
Por tanto,
\[
\boxed{\Omega_+''(k_*)>0}.
\]

La banda es simple porque
\[
e^{2iE(k_*)}\ne e^{-2iE(k_*)}.
\]
Para \(z_*=e^{i\Omega_+(k_*)}\), el factor de la banda saliente tiene un cero exactamente cuadrático en \(k-k_*\); el de la otra banda no se anula. Como
\[
\frac{d\lambda}{dk}=-i\lambda_*\ne0,
\]
el orden en \(\lambda-\lambda_*\) también es dos. La identidad característica conserva ese orden, y la correspondencia de Bloch identifica el núcleo con el núcleo unidimensional de la moneda. Resultan algebraica dos, geométrica uno y **un bloque de Jordan de tamaño dos**.

La separación de alcance es correcta: B1–B3 comprueban identidades y datos algebraicos; la diferenciación, los argumentos de intervalo y el paso a multiplicidades son deducciones escritas. La enmienda ya identifica expresamente como escritos los pasos finales.

**4. La redacción de \(t=7/16\) está reparada.**

Se obtiene
\[
P_{7/16}(u)=\frac5{1024}(1-u)
\left[343w^2-525w+144\right],\qquad w=u-1.
\]
En \(u\in[0,1]\), tenemos \(w\in[-1,0]\). El corchete es estrictamente positivo: sus dos primeros términos son no negativos y el constante es positivo. Por ello,
\[
\frac{P_{7/16}(u)}{u-1}
=-\frac5{1024}\left[343w^2-525w+144\right]
\]
no tiene raíces en \([0,1]\).

Aquí «cociente» significa el **cociente polinómico**, definido también en \(u=1\), no la expresión racional sin prolongar.

El propio \(P\) sí se anula en \(u=1\). Ese cero no decide la velocidad, pues allí la ecuación cuadrada se reduce a \(0=0\). Las pendientes
\[
8t-3=\frac12,\qquad 1-8t=-\frac52
\]
son no nulas y resuelven correctamente el extremo. La aclaración sobre la cabecera histórica de A2 también identifica correctamente qué objeto comprobaba G4.

**5. Inspección de las diez comprobaciones y posibles falsos positivos.**

El recuento estático es
\[
4\text{ de J1}+1\text{ de J2}+2\text{ de B1}
+2\text{ de B2}+1\text{ de B3}=10.
\]
No son diez verificaciones independientes: por ejemplo, la segunda comprobación J1 de cada nodo reformula las mismas nulidades. Eso no invalida ninguna conclusión.

Los límites relevantes son:

- **J1:** la conversión y el rango son exactos; no se captura una excepción para transformarla en éxito.
- **J2:** los restos y la evaluación del cociente deciden el orden exacto.
- **B1:** certifica identidades algebraicas. La identificación de `Ep2` con \(E'^2\) procede de derivar \(\cos E=f\), y la interpretación exige \(\sin E\ne0\). El texto suministra esas condiciones.
- **B2:** la comparación entera basta para estos valores concretos. No comprueba por separado `P516(ustar) == 0`; esa identificación se deduce de la fórmula cuadrática y de la factorización previamente comprobada. No queda una laguna matemática.
- **B3:** comprueba los extremos, \(A<0\), el valor \(g'(1)\) y la identidad que demuestra la cota de la derivada. La monotonía y su consecuencia sobre \(E\) son inferencias escritas válidas.
- **Importaciones:** una excepción no capturada abortaría la ejecución. Que efectivamente hayan pasado los módulos anteriores sigue **[UNVERIFIED]** aquí.

La aserción final merece una precisión: **comprueba los recuentos anteriores \(39,8,61\), pero no comprueba `len(checks) == 10`**. El mensaje `n/n` tampoco impone un número esperado y se imprime antes de esa aserción final.

Esto limita la protección frente a una futura eliminación accidental de comprobaciones; **no constituye un falso positivo en las diez comprobaciones presentes**, cuyo número se verifica inspeccionando el código. Añadir `len(checks) == 10` y colocar el resumen después de la aserción sería una mejora opcional, no una reparación matemática necesaria.

**6. Alcance, atribución y objeciones.**

La Enmienda 3 corrige las dos atribuciones sustantivas: distingue el cociente de \(P_t\) y aporta el argumento que faltaba para afirmar curvatura no nula y estructura de Jordan.

Las referencias a B2 y B3 deben entenderse como certificación de sus ingredientes algebraicos junto con las inferencias escritas expuestas. No son cálculos automáticos de curvatura ni del núcleo de la moneda. La advertencia explícita sobre los pasos escritos evita atribuirles esas operaciones.

Retirar las marcas matemáticas **[UNVERIFIED]** de \(3+1\) y del borde no degenerado está justificado: ambos resultados tienen argumentos reproducibles con el material adjunto. No depende de aceptar la coincidencia entre modelos.

**No hay objeciones que exijan reparación dentro del alcance solicitado.** La única mejora opcional identificada está en el resumen y la aserción final de recuentos del documento 4. Las afirmaciones históricas sobre ejecuciones y bytes permanecen **[UNVERIFIED] en esta revisión**, sin que ello invalide las derivaciones matemáticas anteriores.