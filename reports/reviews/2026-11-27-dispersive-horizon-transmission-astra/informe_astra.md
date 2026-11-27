<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6.2-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-27T07:13:58Z  fin: 2026-11-27T07:17:00Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/theory/DISPERSIVE_HORIZON_TRANSMISSION_GATE.md ; último commit observado: 8eb8be5 ; sha256 de la copia enviada 917920140e2fb29a9dce5db8f8ae53345e6129b70ee9103d43efc4b5a3670117
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transmission.md ; último commit observado: a189db3 ; sha256 de la copia enviada 40adae1e914a53f17c739598ca8e2ed99fad5d3d3e64f3d91eabe9f51ab519cd
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transmission.py ; último commit observado: 0959251 ; sha256 de la copia enviada 29ee9f127b2e43dc1a8aabf2cfdffb6e727edf502e9677b823f45b7c27e316ea
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_channels.py ; último commit observado: a5b9be3 ; sha256 de la copia enviada 08a387355884018d09a35b521e341f6219a235cf462167ea3f16c055e76772dc
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_matrix.py ; último commit observado: d0114b2 ; sha256 de la copia enviada 98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transmission-run-2.txt ; último commit observado: a189db3 ; sha256 de la copia enviada 889cd5cd2b03a39992bbf9c8b3af53b5aab8266fc22f17df78256bd1720c1e12
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transmission-run-1.txt ; último commit observado: 0959251 ; sha256 de la copia enviada 29a6975782bc0b385f2f0399dd4951dd2cccf3ee810263fe339427e1e4feb505
entrada_astra.txt sha256 ed3e401cf3ef2fd274f69c459a35f8e2016184ac62691c9714bc0295f4f02905
respuesta sha256 ee2c25594ac08ebfc0b092aa6af0ab5b36fc0e12cdf535e93bf70df959d036c7
-->

**Veredicto global — REPAIR_REQUIRED.** Los dos `TRANSMISSION_NONZERO_CERTIFIED` se sostienen para el perfil brusco. También se sostiene `T0 = CONNECTED` en \(z_0\). La reparación principal está en la interpretación de \(z_1\). El \(96.05\,\%\) es un peso de la fila de \(S\) y una transmisión máxima para incidencia interior de flujo unitario. Atribuir ese porcentaje del flujo observado a una fuente interior requiere especificar el estado incidente.

He inspeccionado el código y los registros adjuntos. Las implicaciones matemáticas que siguen están derivadas a mano. Los extremos decimales, el grado del discriminante y los recuentos de Sturm se toman de la ejecución 2. La correspondencia de los adjuntos con los bytes y commits del repositorio queda `[UNVERIFIED]` por esta revisión.

### 1. Vector de Bloch y filas de cierre — PASS

Para una raíz \(\lambda\), se tiene \(\lambda\ne0\) y \(P(\lambda,z)=\lambda^5\det(U(\lambda)-zI)=0\). Las dos fórmulas de `bloch_vector` producen vectores del núcleo por la identidad de la adjunta. El código exige que la fórmula elegida tenga norma cuadrada con cota inferior positiva.

Escribamos \(q_j(x)=\lambda^x(a_j,b_j)^T\). Las cinco primeras etapas dan exactamente los \(q_j\) de `bloch_vector`. La sexta satisface \(q_7(x+1)=zq_1(x)\) por la ecuación de Bloch. La variable del verificador de transferencia es, por tanto,
\[
Y_x=\lambda^x(a_1,\ldots,a_6,b_1/\lambda,\ldots,b_6/\lambda)^T.
\]
Estos datos satisfacen las ecuaciones de etapa y cierre cuya solución única es \(Y_{x+1}=M Y_x\). A la vez, \(Y_{x+1}=\lambda Y_x\). Esto prueba las dos filas pendientes, también para los modos evanescentes. Los denominadores de la eliminación son no nulos en el perfil. Este argumento prueba la propiedad de autovector que necesita el empalme. (Docs. 3, `bloch_vector` y S, y 5, T2.)

Las nueve especializaciones son controles exactos de transcripción. El residuo intervalar en cada raíz puede detectar un error si alguna componente excluye cero. La inclusión de cero, por sí sola, admite también un residuo exacto pequeño y no nulo. El informe describe honestamente la sustitución de la ejecución 1. La cabecera del verificador sí debería precisar que la divisibilidad **comprobada por el programa** es muestral. (Docs. 2, «Process deviation», 3, S, y 7, última línea.)

### 2. Raíces por Krawczyk y clasificación — PASS

Sea \(c\) el centro racional de una caja \(X\) e \(y\) el inverso aproximado de \(P'(c)\), convertido en un racional complejo fijo. Para \(F(u)=u-yP(u)\), la integración de \(P'\) sobre el segmento de \(c\) a \(u\) da
\[
F(X)\subseteq c-yP(c)+(1-yP'(X))(X-c)=K.
\]
El código exige las cuatro desigualdades estrictas de \(K\subset\operatorname{int}X\). Así, \(F\) tiene un punto fijo en el rectángulo y, puesto que \(y\ne0\), allí hay una raíz. La unicidad tiene una segunda justificación particularmente sencilla en esta ejecución. Hay doce cajas disjuntas, cada una contiene una raíz y el polinomio tiene grado doce. Esto agota las raíces contando multiplicidades y prueba que todas son simples. Los centros y \(y\) dependen de aproximaciones, pero Horner, los extremos de \(K\) y las comparaciones operan con racionales. El \(10^{-50}\) es el semiancho de cada coordenada. (Doc. 3, `certified_roots`.)

La clasificación de las cajas que tocan el círculo también es válida. Sturm cuenta exactamente las raíces reales de \(H(\tau)\), en biyección con las raíces unitarias mediante \(\tau=\tan(k/2)\), una vez excluido \(k=\pi\) por el grado doce y el coeficiente principal no nulo. Las cajas clasificadas estrictamente dentro o fuera no pueden contener ninguna de esas raíces. Quedan exactamente tantas cajas indecisas como raíces unitarias, con una sola raíz por caja. Así se prueba la igualdad \(|\lambda|=1\). (Docs. 3, `medium_modes`, 4, C2–C4, y 6, líneas R.)

### 3. T0 y continuidad de rama — PASS

\(A'(t)=4t-1>0\) en el intervalo del perfil. Esto justifica usar los valores extremos de \(A\) como límites del recuento del discriminante. El coeficiente principal \(8/5\) tiene una comprobación directa. En \(k=\pi\), \(f=-1\) y \(h=1+\cos\omega_0=8/5\). Por tanto, ninguna raíz se pierde en el punto omitido por la carta de \(\tau\). La ausencia registrada de ceros del discriminante, incluidos los extremos, da \(h_k\ne0\) en cada solución real. (Docs. 3, T0, y 6, T0.)

Esto cubre también las colisiones. Si las dos bandas coincidiesen en \(z_0\) para un \(k\) real, la unitariedad de la matriz \(2\times2\) implicaría \(U(k)=z_0I\). Entonces \(\det(U(k)-z_0I)\) y su primera derivada en \(k\) se anularían allí, en contradicción con la simplicidad. En una banda simple se tiene \(h_\omega\ne0\), y \(v=-h_k/h_\omega\) es continua y no nula sobre la rama. Las raíces reales simples continúan por todo el intervalo sin colisión ni paso por infinito. En consecuencia, hay **un movedor a la derecha para cada \(t\)**, y el de \(k\approx1.231\) termina en el de \(k\approx1.107\). Esta es la continuidad de rama que pide T0.

### 4. T1, estados ligados y recuento de Tarasinski — PASS

El producto \(M_0M_{-1}\) lleva \(Y_{-1}\) a \(Y_1\) e incluye la moneda de \(x=0\). En la cola izquierda decrecen hacia el infinito espacial negativo los modos con \(|\lambda|>1\). En la derecha decrecen los de \(|\lambda|<1\). Sumados a los propagantes salientes, dan siete incógnitas a la izquierda y cinco a la derecha en ambos puntos. Las doce raíces simples y sus autovectores dan bases completas en las colas. Por ello, cualquier estado ligado produciría una solución del empalme homogéneo con amplitudes propagantes nulas. La invertibilidad excluye tal estado en cada uno de los dos \(z\). (Doc. 3, `scatter`.)

Para la matriz de empalme \(A_{\rm m}\), `solve_verified` convierte \(R\) en una matriz racional compleja fija. La cota registrada \(\beta=\|I-RA_{\rm m}\|_\infty\le10^{-6}\) es suficiente por la serie de Neumann. Para cualquier candidato \(\tilde x\),
\[
\|x-\tilde x\|_\infty
\le \frac{\|R(b-A_{\rm m}\tilde x)\|_\infty}{1-\beta}.
\]
El código encierra el residuo usando la matriz y el término independiente intervalares. La calidad de la inversión flotante inicial afecta al éxito del test, pero la desigualdad final se decide racionalmente. (Docs. 3, `solve_verified`, y 6, T1.)

La unitariedad exacta procede del flujo conservado. En cada cola, \((\bar\lambda_i\lambda_j-1)Y_i^HGY_j=0\), de modo que los propagantes distintos son ortogonales para el flujo. Los evanescentes admitidos desaparecen al evaluar el flujo en el infinito correspondiente. Tras normalizar cada propagante por \(|Y^HGY|^{-1/2}\), la conservación da \(\|Sa\|^2=\|a\|^2\) para toda entrada \(a\). Como \(S\) es cuadrada, es unitaria. El encierro \(S^HS\ni I\) es un control de consistencia de esta derivación. (Docs. 3, `medium_modes` y `scatter`, y 4, C1 y C5.)

En \(z_0\), \(t'^Ht'=I_3-r'^Hr'\), con \(r'\) de tamaño \(1\times3\). Su núcleo tiene dimensión al menos dos, lo que da dos combinaciones incidentes exteriores de transmisión perfecta. Además, la norma de la fila exterior da \(\|r'\|^2=1-T\), luego \(\operatorname{tr}(t'^Ht')=2+T\). La prueba del recuento es el argumento de rango. La traza registrada comprueba su consecuencia numérica. (Docs. 3 y 6, T1 en \(z_0\).)

### 5. T2 y T4, transmisión — PASS

Con las filas salientes y las columnas incidentes de `scatter`, los índices del código seleccionan los canales correctos. Los encierros decisivos del registro son los siguientes. (Docs. 3 y 6, T2 y T4.)

| Punto | Cantidad | Encierro registrado |
|---|---|---|
| \(z_0\) | \(|S_0[3,0]|^2=T\) | \([0.99571933684127928475,\ 0.99571933684127928476]\) |
| \(z_1\) | \(|S_1[4,0]|^2\) | \([0.60328032410923785982,\ 0.60328032410923785983]\) |
| \(z_1\) | \(|S_1[4,1]|^2\) | \([0.35726102067870325215,\ 0.35726102067870325216]\) |
| \(z_1\) | \(\sigma^2\) | \([0.96054134478794111197,\ 0.96054134478794111198]\) |

Para dos entradas interiores y una salida exterior, el bloque extraído es la **fila \(1\times2\)** \(B=(t_1,t_2)\). Se tiene \(BB^H=|t_1|^2+|t_2|^2\). El valor singular es \(\sigma=\sqrt{BB^H}\) y el intervalo de la tabla encierra su **cuadrado**. Tomar las raíces positivas de ambos extremos da un encierro exacto de \(\sigma\). Quedan decididas tanto la transmisión no nula del bloque como la de cada entrada por separado.

La coma flotante interviene en la elección de candidatos y precondicionadores. Las cotas que deciden ambos veredictos usan fracciones exactas, encierros de raíces cuadradas por raíz entera y redondeo decimal hacia fuera. El registro proporciona también ambos extremos para cada componente de \(t,t_1,t_2\). Son preferibles a la notación del informe \(t\in\) seguida de un único decimal complejo. (Docs. 3, `dec`, `certified_roots` y `solve_verified`, 4, `sqrt_RI`, y 6, T2 y T4.)

### 6. Interpretación física en \(z_1\) — REPAIR_REQUIRED

Los sentidos de propagación están certificados por el signo del flujo. Los \(k\) aproximados de la tabla concuerdan con \(k=-\arg\lambda\). La pendiente \(8t-3\) establece el cambio de signo de la velocidad infrarroja. Para identificar la hoja de dispersión en las raíces concretas se puede añadir una comprobación escrita a la misma cuasienergía. En \(0<|k|<\pi/2\), sea \(E(k)=\arccos f(k)\). La hoja con esa pendiente se escribe localmente como \(-k+2\,\mathrm{sgn}(k)E(k)\). En las raíces pequeñas de la tabla, sin ambigüedad de \(2\pi\), el signo de \(\sin(\omega_1+k)=\Im(z_1\bar\lambda)\) distingue las dos hojas. Las cajas dan signo positivo en \(k\approx0.080\), negativo en \(k\approx-0.083\) y positivo en \(k\approx-0.027\). Así se identifica el modo exterior y se distingue cuál de los dos modos interiores pequeños pertenece a esa hoja. Las cajas también distinguen los dos incidentes interiores de \(k\) finito. El término «doublers» es una interpretación de esos canales adicionales. T4 certifica sus amplitudes de dispersión y el informe extiende esa certificación a un mecanismo físico. (Docs. 2, T4, 4, C2–C3, 5, T8, y 6, modos en \(z_1\).)

La objeción al porcentaje es independiente de esa identificación. Para incidencia exclusivamente interior con amplitud \(a\) y flujo unitario, el flujo en la salida exterior es \(|Ba|^2\). Tomando \(a=B^H/\sigma\) se obtiene \(\sigma^2\). Tomando \(a\) proporcional a \((t_2,-t_1)^T\) se obtiene **cero** para la misma interfaz y el mismo flujo incidente. Por tanto, el \(96.05\,\%\) tiene dos lecturas precisas: es la transmisión interior máxima hacia esa salida y es la suma de los pesos interiores de su fila. El complemento \(3.95\,\%\) es la suma de los pesos exteriores por unitariedad. Ambos porcentajes describen fracciones del flujo saliente para una mezcla incoherente con igual flujo medio en cada canal incidente. El informe omite esa condición al atribuir el origen del flujo. (Docs. 2, «Interpretation» de T4, y 6, última fila de \(S_1\).)

### 7. Veredictos, alcance y proceso — REPAIR_REQUIRED

Ambos intervalos de transmisión excluyen cero y satisfacen la regla del contrato. En \(z_0\), el informe cumple la cláusula de `CONNECTED` al declarar la continuidad adiabática de la rama. Su significado demostrado es la continuación en la familia de medios homogéneos. El valor certificado de \(T\) corresponde al salto brusco. En \(z_1\), la certificación alcanza la transmisión desde los dos canales interiores hacia el único saliente exterior. Las frases «through the mode that carries the horizon» y «Here it is certified exactly» extienden el referente de *certified* más allá de ese resultado. (Docs. 1, «Verdicts» y «Not claimed», y 2, T2, T4 y «Answer».)

Las exclusiones sobre \(L\) finita, otras \(z\), Hawking y novedad son adecuadas. La interrupción está documentada y el paso escrito del punto 1 cubre la obligación matemática. La sustitución de la prueba simbólica no altera los dos veredictos. Para leer la ejecución importa conservar sus líneas de decisión, porque el programa también puede registrar una salida `OPEN` mediante `ok(..., True)`. En esta ejecución las dos líneas dicen explícitamente `TRANSMISSION_NONZERO_CERTIFIED`. (Docs. 3, ramas finales de T2 y T4, 6 y 7.)

### Objeciones por gravedad y reparación concreta

1. **Principal · Informe T4, «Interpretation».** Sustituir la atribución incondicional del \(96.05\,\%\) por «La transmisión máxima desde una superposición interior de flujo unitario hacia el modo exterior es \(\sigma^2\approx0.96054\)». Si se conservan los porcentajes de procedencia, especificar la preparación incoherente y las ocupaciones iguales.
2. **De alcance · Informe T4 y «Answer».** Dar los canales por medio, signo de flujo y \(k\) aproximado. Añadir el argumento de hoja si se conserva la identificación infrarroja. Presentar «doublers» y la analogía física como interpretación, y referir «certificado» al bloque de dispersión del perfil brusco en \(z_1\).
3. **De precisión documental · Cabecera del verificador S e informe T2/T4.** Indicar en la cabecera las nueve especializaciones y la prueba general escrita. Reproducir los intervalos rectangulares del registro donde se use el signo \(\in\), y distinguir el bloque \(1\times2\), su valor singular \(\sigma\) y la probabilidad \(\sigma^2\).