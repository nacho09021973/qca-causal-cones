<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.1-sol, esfuerzo: high, vía: codex exec sellado (codex-cli 0.166.0)
inicio: 2026-11-04T08:41:54Z  fin: 2026-11-04T08:45:16Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-04--substrate-saturation-phase0-G1-trace.md ; último commit observado: cb814b5 ; sha256 de la copia enviada f173971be2f182c57482f555a24b45ec0639487cd4ee7e07861d1f1216f474ec
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: 862b405 ; sha256 de la copia enviada aee9b97aa5841abfaaae487ee765b8a7ea40b45acd9ec83ac8f5a680870041e0
documento: /home/ignac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/cjww_pp16-17.txt ; último commit observado: sin versionar ; sha256 de la copia enviada 68d4b9c97dedcc638ba1f55cc50e888497a3d1ce313d83a85c6ebe3399d70f5e
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-G1-trace-review-astra/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada ce7632dc6469689fa0e35cdd398c6e9a51a4c7bb45bd5e35cb9ba3aa81f60cfb
entrada_astra.txt sha256 b91d9ce3d3631e8750dba71da9ea1b75d75aacbbbd94129a75f0f691f6d8488d
respuesta sha256 5ce72c25fe11c72a3cc8a0dd9a53f2d77e786f0afbd08e6927397eee316ab554
-->

**Dictamen global: REPAIR_REQUIRED.** Hay dos errores obligatorios de corregir: el recuento final de patrones nulos de L6e y la presentación de F2 como condición necesaria. Los cálculos principales y las lagunas G1-a/b/c quedan sustentados por los textos adjuntos. Esta revisión es manual; no acredita nuevas ejecuciones de los verificadores.

**1. LEMAS: PASS.**

El **Lema V** es correcto. Un funcional que expone únicamente el vértice debe satisfacer \(\varphi(a_i)\ne0\): si alguno fuera cero, variar ese segmento produciría otros maximizadores. Cada signo queda entonces forzado por \(\operatorname{sign}\varphi(a_i)\). Esto vale también con generadores paralelos o dependientes.

La consecuencia sobre amplitudes es correcta dentro del contexto, donde \(F\subseteq Z\): un vértice tiene un solo patrón contribuyente, por lo que no puede desaparecer por interferencia entre patrones distintos. Asimismo,
\[
\operatorname{conv}F=Z\iff \operatorname{vert}Z\subseteq F.
\]

El **Lema P** también es correcto para proyectores ortogonales de rango uno. Escribiendo \(Q_i=|v_i\rangle\langle v_i|\),
\[
Q_n\cdots Q_1
=|v_n\rangle\Bigl(\prod_{i=1}^{n-1}\langle v_{i+1}|v_i\rangle\Bigr)\langle v_1|.
\]
Se anula exactamente cuando algún solapamiento consecutivo es cero. Para estados puros de qubit, eso equivale a vectores de Bloch antípodas. No hay que comparar adicionalmente el último factor con el primero.

La fórmula JDW es correcta. De `u2` resulta
\[
R=\begin{pmatrix}i\cos\theta&\sin\theta\\-\sin\theta&-i\cos\theta\end{pmatrix},
\qquad R^\dagger|0\rangle=(-i\cos\theta,\sin\theta)^T.
\]
Por tanto, \(2\Re(\bar\alpha\beta)=0\), \(2\Im(\bar\alpha\beta)=\sin2\theta\) y \(|\alpha|^2-|\beta|^2=\cos2\theta\).

**2. FILAS RESUELTAS: PASS.**

La pertenencia literal y los generadores indicados se sostienen:

- **L1–L3:** `rotation_product` proporciona factores con desplazamientos opuestos por cada coordenada. La transposición invierte el orden de los factores y transpone los proyectores, conservando esta estructura. La igualdad «published vs product» y «active support» son las comprobaciones pertinentes. Son \(2^d\) desplazamientos distintos, todos esquinas. En L1 el eje de Pauli utilizado es \(z\); esto no cambia el único generador espacial.
- **L5a:** el código construye literalmente \(T_xT_yT_z\), con desplazamientos \(\pm e_b\), y compara el soporte calculado con las ocho esquinas.
- **CJWW (5.12):** la ecuación primaria y `walk1` muestran los tres factores. El *jump set* se obtiene de coeficientes Fourier no nulos y se compara con las ocho esquinas. No se necesita la reseña de otro modelo citada por la traza.
- **L6a:** los desplazamientos son \(\pm u_i\). Como \(u_0+u_1+u_2=0\), dos patrones llegan al origen y los otros seis a \(\pm2u_i\). Los vectores de Bloch tienen producto escalar \(1/3\) entre distintos índices; ningún par pertinente es igual ni antípoda. Los ocho patrones son individualmente no nulos.
- **L6d:** los tres factores pueden agruparse como \(S_1\), \(R_1^{-1}S_2R_1\), \(R_2^{-1}S_3R_2\). Sus generadores son los \(N_j\) citados. Los patrones \(\pm(+,-,+)\) coinciden en cero; los otros seis dan \(\pm2N_j\). Los vectores \(m(0),m(\pi/6),m(\pi/3)\) permiten aplicar P.

En L6a y L6d, la traza distingue correctamente dos afirmaciones: cada patrón central es no nulo y su **suma** también lo es. La primera procede de P; la segunda, del soporte afirmado por el código. `EXPECTED_F` no es por sí solo una prueba, pero aquí se compara explícitamente con `laurent_support`, que elimina coeficientes matriciales nulos.

**3. L6e: REPAIR_REQUIRED.**

La derivación principal es correcta. El constructor da
\[
W=U^3S^3U^2S^2U^1S^1,\qquad
U^j=e^{-i(j-2)\pi\sigma_x/4},
\]
por lo que \(U^2=I\) y \(U^3=(U^1)^{-1}\).

Los desplazamientos físicos de L son \(-N_j\), porque `jdw_shift` lee en \(X+N_j\). Para reproducir la tabla de la traza, el signo positivo debe designar R, que se desplaza por \(+N_j\). Con esa convención,
\[
A_s=U^3P_{s_3}P_{s_2}U^1P_{s_1}.
\]
Así, se anulan exactamente los **cuatro** patrones con \(s_2\ne s_3\):

\[
(++-),\ (--+),\ (+-+),\ (-+-).
\]

Los dos primeros llegan a \(\pm(2,-2)\); los otros dos, al origen. Los cuatro restantes son no nulos porque todas las entradas de \(U^1\) son no nulas. Producen exactamente el `EXPECTED_F` de cuatro puntos.

El zonótopo de los tres \(N_j\) tiene los seis vértices citados. El soporte pierde dos vértices y el origen; su envolvente es el cuadrado indicado. No hay cancelación entre dos contribuciones centrales no nulas: ambas contribuciones son individualmente cero.

La fusión también es correcta:
\[
W=U^3(S^3S^2)U^1S^1.
\]
El desplazamiento combinado es \(\pm(N_2+N_3)\). En coordenadas cartesianas, los dos generadores son \((1,0)\) y \((0,1)\). Sus cuatro patrones son no nulos. Por tanto, **los generadores reducidos de estas presentaciones sí difieren**: tres direcciones frente a dos.

**Error exacto:** resumen, G1-c: «**in the printed one, two sign patterns vanish**». Son cuatro, aunque solo dos correspondan a vértices desaparecidos. Lo cierra sustituir esa frase por «four sign patterns vanish: two at the missing vertices and two at zero».

**Aclaración:** explicitar «\(+\) corresponde a R» evita confundir lectura y desplazamiento. No cambia los conjuntos ni la conclusión.

**4. L6c, L6f y CJWW (5.15): PASS, con aclaración de signos.**

En los factores impresos de L6c y L6f, los desplazamientos son efectivamente asimétricos: \(c_j\ne-b_j\). No satisfacen literalmente la cláusula congelada \(\pm a_j\). Esto establece el fallo de esa presentación respecto de la cláusula; no demuestra que sea imposible cualquier otra factorización.

Para **L6f**, con \(b=-N_a,c=-N_b\), los valores de \(a=(b-c)/2\) son correctos. Los centros son
\[
m_1=(0,-1/2),\quad m_2=(1/2,0),\quad m_3=(-1/2,1/2),
\]
y suman cero. Las ocho asignaciones producen siete desplazamientos: cero dos veces y los seis puntos no nulos de `EXPECTED_F`. Los ángulos de Bloch consecutivos difieren en \(2\pi/3\); P confirma que los ocho patrones son individualmente no nulos. La presencia efectiva del origen se obtiene además de la comparación de soportes.

Para **L6c**, los centros son
\[
m_j=-(N_j+N_{j+1})/2,\qquad \sum_jm_j=0.
\]
Los \(a_j=(N_j-N_{j+1})/2\) impresos son válidos si el signo positivo designa **R**. Si se conserva la convención \(b=m+a\) de L6f con \(b\) como desplazamiento L, deben llevar el signo contrario. Es una **aclaración de orientación**, no un error en los generadores reducidos, definidos salvo signo.

Las parejas opuestas se fusionan en tres segmentos de longitud 1, con las direcciones cartesianas indicadas. Sus sumas dan los 19 puntos del hexágono afirmado; los seis vértices tienen patrón único. Los incrementos consecutivos de \(2\theta\) son \(\pi/3\), de modo que los 64 patrones son individualmente no nulos.

Para **CJWW (5.15)**, lo adjuntado contiene una matriz y una transcripción por entradas, ninguna factorización. El soporte de 14 puntos no determina proyectores, monedas ni una presentación producto. Mantener G1-b abierto es correcto; tampoco procede afirmar inexistencia de factorización.

**5. ALCANCE: PASS.**

La traza mantiene explícitamente G1 abierto, `OPEN_AFTER_ROW_SURVEY`, el carácter preliminar y la ausencia de valor confirmatorio. Registra L6e sin emitir un veredicto sobre (PS′), sin trasladarlo a (PH) y sin autorizar fases posteriores. No encuentro factores deducidos de aristas: las direcciones proceden de constructores y las envolventes se calculan después.

**Segundo error obligatorio, transversal: formulación de F2.**

La frase de Sec. 0 «**that identity presupposes every sign pattern has nonzero amplitude**» reproduce una condición necesaria incorrecta para \(\operatorname{conv}F=Z\). El propio Lema V identifica la condición exacta: basta y es necesario conservar todos los vértices.

Como comprobación independiente, dos factores idénticos \(P_+T(a)+P_-T(-a)\) tienen patrones mixtos nulos, pero soporte \(\{\pm2a\}\), cuya envolvente es el zonótopo completo. Para la igualdad del **soporte** con todas las sumas candidatas, además deben considerarse las sumas de amplitudes en desplazamientos coincidentes.

Lo cierra reemplazar aquella frase por una atribución explícitamente corregida: F2 señaló un riesgo real, pero su condición era excesiva; la igualdad de envolventes depende de los patrones de vértice. Esto no altera el diagnóstico de L6e.

**Reparaciones obligatorias:**

1. Cambiar de dos a cuatro los patrones nulos en el resumen de G1-c.
2. Corregir la formulación necesaria de F2, distinguiendo soporte, patrones individuales y envolvente convexa.

No hacen falta nuevos cálculos ni ampliar la investigación para estas reparaciones.