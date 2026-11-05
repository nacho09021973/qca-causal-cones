<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-05T13:10:00Z  fin: 2026-11-05T13:13:43Z
documento: /home/ignac/qca-causal-cones/theory/HEX_TRACE_ALIGNED_ALL_M_GATE.md ; último commit observado: 689fd30 ; sha256 de la copia enviada ca2e1788cdb8793c1cc9c0c60902d131280a0163d27be5af81c034d9fd6c6906
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-aligned-all-m.md ; último commit observado: 1154fad ; sha256 de la copia enviada 432930498ba0abcd9611b856b673c755d9cfc397a6db1855c695349e6fb6c8c9
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_trace_aligned_all_m.py ; último commit observado: 1154fad ; sha256 de la copia enviada f8da0f94f61f4dcd56f4f0ec5086ce96dd440019cfeb20b0ef5f6a3aa19ecdf9
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-aligned-all-m-verifier.txt ; último commit observado: 1154fad ; sha256 de la copia enviada 139ddb03cd93e4f8c665f3730acf215d7a9b5264b4d65f242ec56fbc1856d9d1
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-m3.md ; último commit observado: 6aefa91 ; sha256 de la copia enviada c1115dcd7e269b491d3cb65e339ab6f2fd561cdcf38efe0c92a9a8f4f7a1d4a8
documento: /home/ignac/qca-causal-cones/reports/2026-11-05--hex-trace-scalar-method.md ; último commit observado: ad84207 ; sha256 de la copia enviada 321b53d0dbc234724188b350a1ea050fc79747c5f7e038cdb17cd834b689423b
entrada_astra.txt sha256 12a99514d3ff88fb2b3777f175e1473e4d3022e581e78346ebad9bf726a18efa
respuesta sha256 642adbc37be002dab4529a063c48005713b472af9750588c5ba54877954d180d
-->

**Dictamen global: REPAIR_REQUIRED.** La construcción y la conclusión matemática principal son correctas. Las reparaciones afectan al alcance del verificador, la justificación contractual y dos formulaciones excesivas. Revisión realizada exclusivamente sobre los documentos adjuntos, sin ejecutar código.

**1. REDUCCIÓN Y RECÍPROCO: PASS.**

El recíproco es independiente de la divisibilidad: para todo **h real** e invariante con soporte en \(H_{m-2}\), el producto \(\Delta h\) tiene soporte en \(H_2+H_{m-2}=H_m\), es invariante y se anula en las tres normales. Por tanto, \(f(0)=1\) y las restricciones son los cosenos prescritos. Esto certifica admisibilidad algebraica, **no** la cota global.

La divisibilidad también es correcta para m general. Por ejemplo, la reflexión que fija \(p=0\) es
\[
(p,q)\mapsto(-p,q-p).
\]
Para \(d=f-f_m^0\), diferenciando la invariancia allí resulta \(2d_p=-d_q=0\), porque \(d(0,q)\equiv0\). Así, \(z-1\) divide con multiplicidad dos. Las reflexiones conjugadas producen los otros factores dobles. Son irreducibles distintos en el anillo de Laurent, y su producto coincide con \(\Delta\), salvo una unidad.

Finalmente, aplicando las seis formas lineales que definen el hexágono a
\(\operatorname{Newt}(d)=H_2+\operatorname{Newt}(h)\), cada máximo de \(h\) queda acotado por \(m-2\). No se presupone aquí que su polígono sea hexagonal.

**2. RECTA \(p=2q\): PASS.**

Las identidades se obtienen directamente de \(\cos(2mq)=2\cos^2(mq)-1\) y de las fórmulas de medio ángulo:
\[
f_m^0=T_m^2+T_m-1,\qquad
\Delta=\frac{(1-x)^3(1+x)}4.
\]

La inclusión en \(V_n\) es correcta: el giro de \(120^\circ\) fija el punto indicado módulo períodos y su acción sobre covectores tampoco tiene vectores fijos no nulos. La invariancia fuerza gradiente cero; como \(\sin(2\pi/3)\ne0\), fuerza \(g'(-1/2)=0\).

La dimensión se verifica sin asumir cancelaciones favorables. Para sumas sobre órbitas distintas:

- \((a,0)\) restringe a \(2\cos(2aq)+4\cos(aq)\): coeficiente superior 2.
- Para \(a>1\), \((a,1)\) restringe a
  \(4[\cos((2a+1)q)+\cos((a+2)q)+\cos((a-1)q)]\): coeficiente superior 4.
- Para \(a=1\), la órbita tiene seis puntos y restringe a \(4\cos(3q)+2\): también coeficiente superior 4.

Además, \(\|(a,1)\|_{\rm hex}=a+1\). Los máximos \(0,2,3,\ldots,2n\) proporcionan exactamente \(2n\) restricciones independientes. La condición derivativa es una ecuación lineal no trivial, de modo que \(\dim V_n=2n\).

La equivalencia univariable es exacta. La expansión de \(G(mq)\) es
\[
1-\frac32m^2q^2+\frac38m^4q^4+O(q^6).
\]
Las tres condiciones en cero equivalen a divisibilidad por \((x-1)^3\), y la condición en \(\pi\), por \(x+1\). En \(x=-1/2\), tanto \(\Delta'\) como \((T_m^2+T_m-1)'\) se anulan: para este último, si \(3\mid m\), se anula \(T_m'\); en los demás casos, \(2T_m+1=0\). Por ello, la última condición equivale precisamente a \(g'(-1/2)=0\).

**3. CONSTRUCCIÓN: PASS.**

Se tiene \(K_1<s<K_2\), luego \(0<\lambda<1\). El exceso satisface
\[
E=(K_2^2-s^2)(s^2-K_1^2)>0.
\]
Los dos factores suman \(6(K_1+K_2)\), por lo que
\[
E\le9(K_1+K_2)^2<36(s+3)^2.
\]
Como \(L\ge3\sqrt m\), \(3L^4\ge243m^2\). La diferencia respecto de la última cota es exactamente el polinomio D1b, positivo desde \(m=4\). Así, \(0<1-\alpha<1\), y los tres argumentos de acotación de \(A,H,B\) son válidos.

También
\[
H(q)=1-\frac{L^4q^4}{8}+O(q^6).
\]
Por tanto, \(B''(0)=0\), \(B''''(0)=-3(1-\alpha)L^4\); en el producto desaparece el término cruzado de segundo orden y se obtienen los momentos requeridos.

La condición de grado es correcta. Como comprobación adicional exacta,
\(\sqrt3<17321/10000\) y \(\sqrt{629}<627/25\) dan
\[
Q_{\rm deg}(\sqrt{629})>291/10000>0.
\]
La derivada ya es positiva allí y sigue creciendo.

Las congruencias garantizan \(A(\pi)=(-1)^m\), \(B(\pi)=1\) y las derivadas nulas en \(2\pi/3\). Finalmente, la divisibilidad demostrada en el bloque anterior proporciona un polinomio \(g\) de grado máximo \(2m-4\) perteneciente a \(V_{m-2}\). Existe, por tanto, un levantamiento real e invariante \(h\).

**4. VERIFICADOR: REPAIR_REQUIRED.**

Las veinte comprobaciones y la salida adjunta son coherentes por inspección. La ejecución, el hash y la procedencia temporal permanecen **[UNVERIFIED]** en esta revisión.

Defecto concreto: C2b anuncia **“(a,1) in H_n iff a<=n-1”**, pero su condición únicamente comprueba máximos de frecuencias proyectadas y que se alcanzan. No comprueba pertenencia al soporte. La afirmación matemática es verdadera; el rótulo atribuye al código una comprobación ausente. Se cierra añadiendo la comprobación simbólica correspondiente o retirando esa cláusula del rótulo y atribuyéndola expresamente al argumento analítico.

D3a pasa parcialmente **por construcción**: sustituir la definición de \(\alpha\) en el cuarto momento cancela el exceso automáticamente. Es una comprobación algebraica útil, pero no verifica por sí sola que esa expresión sea la cuarta derivada de \(AB\). D2 sí contrasta esto mediante series, en tres instancias. No encuentro una comprobación vacía que invalide el resultado.

Las exclusiones declaradas —divisibilidad universal, cotas fuera de la recta y resolución global— son correctas. La universalidad depende conjuntamente del razonamiento analítico y D1; no de las tres instancias.

**5. ALCANCE Y CONTRATO: REPAIR_REQUIRED.**

El resultado correcto es **OPEN_AFTER_ALIGNED_ALL_M_ANALYSIS**. Para cada \(m\ge629\), un mismo levantamiento satisface las cotas en todas las rectas de dirección de vértice, por invariancia. Esto impide obtener contradicción utilizando exclusivamente esas restricciones. No acredita compatibilidad global ni incompatibilidad fuera de ellas; \(4\le m\le628\) queda sin decidir.

Hay cuatro defectos documentales:

- **“within the 90-minute budget”**, junto con **“worked out by reasoning […] immediately before the first command”**. El contrato cuenta desde el primer cálculo, también analítico. El inicio registrado no permite certificar ese presupuesto. Debe consignarse el inicio analítico respaldado por registro; si no existe, marcar el cumplimiento temporal **[UNVERIFIED]**. La nota actual reconoce el desfase, pero no lo subsana.
- **“First re-derive the scalar relaxation”** y **“the general reduction and trace bridge must be within its scope”**, del contrato: el informe rederiva la parametrización escalar, pero omite el puente general desde los paseos. Debe incorporarse con sus hipótesis, soporte reflejado, promedio y justificación general de la rigidez normal con grado \(N=m\). La omisión no afecta a la construcción escalar, pero impide declarar cumplimiento íntegro.
- **“cos(sqrt3 t) […] meets them”**. El límite satisface las condiciones locales en cero; las condiciones en \(\pi\) y \(2\pi/3\) se desplazan al infinito al escalar. Debe presentarse como control local, no como segunda derivación de todas las condiciones.
- **“a genuinely two-dimensional measure”**. Utilizar puntos fuera de esas rectas no exige una medida bidimensional: podrían estar en otra recta. Basta eliminar ese paréntesis.

El código adjunto no contiene búsqueda flotante, solver ni barrido de exclusiones por radios; los pequeños rangos son diagnósticos declarados. No se formula una exclusión conjunta para \(m=1,2,3,\ldots\), por lo que no se activa aquí la exigencia de identificar su intersección de clases.

**Reparaciones obligatorias:** corregir C2b, documentar o limitar la afirmación temporal, incorporar el puente contractual y corregir las dos frases sobre el límite y la medida bidimensional. Ninguna exige modificar la construcción ni el resultado OPEN.