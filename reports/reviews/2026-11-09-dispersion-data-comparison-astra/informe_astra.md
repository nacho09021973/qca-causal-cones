<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.167.0)
inicio: 2026-11-09T13:06:52Z  fin: 2026-11-09T13:10:55Z
documento: /home/ignac/qca-causal-cones/theory/DISPERSION_DATA_COMPARISON_GATE.md ; último commit observado: ad445aa ; sha256 de la copia enviada e43209091f1971d89591b74ceddf3aba5e7c469ff720db17bf3924c35b329d84
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--dispersion-data-comparison.md ; último commit observado: 121f679 ; sha256 de la copia enviada ee4521c070a1e55b97cd78927aba8614e613dc9c79e2ddb84cdb6efd34d52ee5
documento: /home/ignac/qca-causal-cones/scripts/verify_dispersion_data_comparison.py ; último commit observado: 6b0e049 ; sha256 de la copia enviada 02ee804aa0ffec6f57e801b9f7217819c524f85894c23f140d3772b1eeb9a386
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--dispersion-data-comparison.txt ; último commit observado: 121f679 ; sha256 de la copia enviada dca3817a3410b5c7922db5cb2fd8ff942a847fbabba8dcc8ed49f9243dcc2342
documento: /home/ignac/qca-causal-cones/investigaciones/2026-11-09-lorentz-violation-bounds/comprobacion.md ; último commit observado: 2f7664d ; sha256 de la copia enviada 23c68879a7cc58f9b69e32c87ec8a5f003b0a7dba2d0a62ffbeb61d7b478d353
documento: /home/ignac/qca-causal-cones/reports/2026-11-02--dispersion-corrections-across-lattices.md ; último commit observado: 70dd98c ; sha256 de la copia enviada 5aaaea6af9704abb2a1a16613f1ede7fc1639956800e66d2580824484b31bec9
entrada_astra.txt sha256 cfcfa456b81dc521e3acf8df4da7f3047a4e591a7f959931b350d957187df6db
respuesta sha256 e7142ba5a8cc8f1ed969a5f7c84f3a4861c748b4b488a7aad7c61f4d1b79fc8e
-->

**Veredicto: reparación necesaria.** Los factores de emparejamiento y la aritmética principal se sostienen bajo los diccionarios declarados. No se sostiene presentar esos números como cotas generales sobre cada red con orientación desconocida. Hay además errores concretos sobre L3s4 y sobre qué sucede cuando \(\beta\) se anula en una dirección.

He derivado a mano los emparejamientos, los extremos angulares y las comprobaciones que siguen. Del script y del registro sólo he inspeccionado el texto: no he ejecutado código ni comprobado los artículos, los commits o los hashes. La fidelidad a las fuentes originales queda **[UNVERIFIED]**; sí puedo evaluar la coherencia entre los documentos adjuntos. El 9/9 no interviene como prueba.

**El emparejamiento D1 es correcto al orden declarado.** Escribiendo \(u=E\ell/(\hbar c)\), la expansión de energía implica
\[
u=t[1+\beta t+\alpha t^2+\cdots].
\]
Por tanto, \(t=u\) sólo a orden dominante. Esa sustitución basta para las correcciones consideradas: lineal cuando \(\beta\ne0\), cuadrática cuando \(\beta\equiv0\).

Para \(n=1\), LHAASO da
\[
\frac{\delta v}{c}=-s\frac{E}{E_{\rm QG,1}},
\]
mientras la red da \(2\beta E\ell/(\hbar c)\). Luego
\[
\ell_{\max}=\frac{\hbar c}{2|\beta|E_{\rm QG,1}}.
\]
\(\beta<0\) corresponde a \(s=+1\), subluminal; \(\beta>0\), a \(s=-1\), superluminal.

Para \(\beta\equiv0\),
\[
3\alpha\frac{E^2\ell^2}{(\hbar c)^2}
=-s\frac32\frac{E^2}{E_{\rm QG,2}^2},
\qquad
\ell_{\max}=\frac{\hbar c}{\sqrt{2|\alpha|}\,E_{\rm QG,2}}.
\]
Los factores \(2\) y \(3/2\) están bien tratados. Las seis filas exclusivamente cuadráticas tienen \(\alpha<0\) donde no se anula, de modo que corresponde usar \(6.9\times10^{11}\) GeV.

**D2 tampoco contiene un error de factor dos**, tomando la forma SME suministrada como premisa. Denomino \(q_5(\hat n)\) a la combinación angular con unidades \({\rm GeV}^{-1}\), para distinguirla de convenciones donde \(\varsigma_3\) incorpora también la energía:
\[
\frac{\delta v_\pm}{c}=\pm2E|q_5|,
\qquad
\frac{\delta v_\pm}{c}=\pm2|\beta|\frac{E\ell}{\hbar c}.
\]
Así,
\[
|q_5|=\frac{|\beta|\ell}{\hbar c},
\qquad
\ell_{\max}=\frac{K\hbar c}{|\beta|}.
\]
La separación entre velocidades de ambas helicidades sería \(4E|q_5|\); no debe confundirse con la corrección de cada helicidad.

El registro atribuye \(7\times10^{-35}\)–\(2\times10^{-34}\ {\rm GeV}^{-1}\) a **combinaciones direccionales**, que son las cantidades pertinentes. No corresponde sustituirlas por las cotas sobre \(k_{(V)00}^{(5)}\), ni introducir aquí un factor \(\sqrt{4\pi}\). El cociente entre ambos extremos de \(K\) es \(20/7\simeq2.86\). Son límites de fuentes distintas, no un intervalo estadístico de una única medición.

Los extremos angulares se obtienen directamente de la tabla padre:

| Filas | \(\sup|\text{coeficiente}|\) | Ceros del coeficiente |
|---|---:|---|
| L1 | \(0\) | Todas las direcciones |
| L2, L6e | \(1/48\) | Ejes coordenados |
| L3 | \(1/54\) | Ejes coordenados |
| L5a, L5b, L4 | \(1/9\) | Planos coordenados |
| L6a | \(\sqrt{15}/36\) | \(\cos3\theta=0\) |
| L6b | \(\sqrt{15}/18\) | \(\cos3\theta=0\) |
| L6c | \(1/512\) | Ninguno |
| L6d, L6f | \(1/128\) | Ninguno |

En el círculo, \(n_1^2n_2^2\le1/4\), con igualdad en las diagonales. En la esfera,
\[
1-3\sigma_2
=\tfrac12\sum_{i<j}(n_i^2-n_j^2)^2\ge0,
\]
con igualdad cuando \(n_i^2=1/3\). Finalmente, AM–GM da
\[
|n_1n_2n_3|\le\frac1{3\sqrt3},
\]
también alcanzado en las diagonales. Esto demuestra tanto las cotas como su alcanzabilidad, sin depender del script.

Para **L3s4**, defino
\[
B=\frac{\sqrt3(1-a^2)}{6a}>0,\qquad
M=\frac{|2a^2-1|}{9a}.
\]
Para uno de los signos de cluster, el rango de \(\beta\) es \([B-M,B+M]\); para el otro, su opuesto. Por consiguiente,
\[
\boxed{\sup|\beta|=S(a)=B+M},\qquad
\boxed{\inf|\beta|=\max(B-M,0)}.
\]

La cota \(S(a)\ge1/9\) es correcta. Para \(a^2\ge1/2\),
\[
a(S-1/9)
=(1-a)\left[\frac{\sqrt3(1+a)}6-\frac{2a+1}{9}\right]>0
\]
en \(0<a<1\) dentro de ese tramo. Para \(a^2\le1/2\),
\[
\frac{d}{da}\bigl[a(S-1/9)\bigr]
=-\frac{\sqrt3 a}{3}-\frac{4a}{9}-\frac19<0,
\]
y su valor en \(a=1/\sqrt2\) es positivo. De hecho, \(S>1/9\) en todo el intervalo abierto; \(1/9\) se alcanza como límite cuando \(a\to1\).

Pero L3s4 tiene ceros **sólo si**
\[
a^2\ge x_c=\frac{19-6\sqrt3}{11}\simeq0.7825.
\]
Cuando existen, satisfacen
\[
n_1n_2n_3=-\frac{1-a^2}{2(2a^2-1)}.
\]
No son los planos coordenados: en éstos \(|\beta|=B>0\) para cualquier \(0<a<1\).

**La aritmética numérica principal concuerda**, por sustitución manual y redondeo, con las constantes declaradas:

| Filas | \(\ell_{\max}\), D1 | \(\ell_{\max}/\ell_P\) | \(f_{\min}\), Hz |
|---|---:|---:|---:|
| L5a, L5b, L4 | \(8.88\times10^{-36}\) m | \(0.5494\) | \(5.85\times10^{43}\) |
| L6a | \(9.17\times10^{-36}\) m | \(0.5674\) | \(6.54\times10^{43}\) |
| L6b | \(4.59\times10^{-36}\) m | \(0.2837\) | \(1.96\times10^{44}\) |
| L2, L6e | \(1.401\times10^{-27}\) m | \(8.668\times10^7\) | \(3.026\times10^{35}\) |
| L3 | \(1.486\times10^{-27}\) m | \(9.194\times10^7\) | \(3.494\times10^{35}\) |
| L6c | \(4.576\times10^{-27}\) m | \(2.831\times10^8\) | \(8.736\times10^{34}\) |
| L6d, L6f | \(2.288\times10^{-27}\) m | \(1.416\times10^8\) | \(1.747\times10^{35}\) |

Las tres primeras líneas usan el extremo subluminal, más débil. En los extremos superluminales, \(\ell_{\max}\) se divide por \(1.1\) y \(f_{\min}\) se multiplica por \(1.1\). Por ello, los números publicados son una elección conservadora entre signos; no son el mínimo estricto de \(\ell_{\max}\) sobre todas las orientaciones.

Para D2, los intervalos entre el \(K\) más fuerte y el más débil son:

| Filas | \(\ell_{\max}\), m | \(\ell_{\max}/\ell_P\) |
|---|---:|---:|
| L5a, L5b, L4 | \(1.243\)–\(3.552\times10^{-49}\) | \(7.692\times10^{-15}\)–\(2.198\times10^{-14}\) |
| L6a | \(1.284\)–\(3.668\times10^{-49}\) | \(7.944\times10^{-15}\)–\(2.270\times10^{-14}\) |
| L6b | \(6.420\times10^{-50}\)–\(1.834\times10^{-49}\) | \(3.972\times10^{-15}\)–\(1.135\times10^{-14}\) |

También concuerdan. Para L3s4, sustituir \(S(a)\) por \(1/9\) proporciona una envolvente conservadora de la sensibilidad máxima, no su valor exacto.

Las objeciones, por gravedad, son las siguientes.

1. **La conclusión cambia indebidamente de cuantificador — informe §§1, 3 y 4.**

   Una cota calculada donde el coeficiente es máximo no es una cota válida para una orientación desconocida. Para una fuente y una orientación \(R\), D1 depende de
   \[
   |\beta(R^{-1}\hat n_{\rm fuente})|.
   \]
   Si este valor puede anularse, el análisis lineal no proporciona una cota finita uniforme sobre \(R\). Por continuidad, tampoco hay separación uniforme entre clases cerca de esas direcciones.

   La advertencia de §3 no salva afirmaciones posteriores como «las reglas […] necesitan una celda» de media longitud de Planck. Tampoco se ha demostrado que las filas cuadráticas sean reglas donde «nada supera \(c\)»: el padre deja abierta la velocidad de grupo máxima fuera del régimen local.

   **Reparación:** limitar el resultado a una **comparación de sensibilidades en direcciones de coeficiente máximo**, bajo H_gamma, D1/D2 y las hipótesis observacionales de las fuentes. Reescribir §4 con ese alcance. Hi se sostiene con su cuantificador explícito; Hk se sostiene como comparación de límites de orden dominante, no como validación física completa de esos tamaños de celda.

2. **Es falsa la descripción de los ceros de L3s4 — informe §3 y representación de la fila en el script.**

   La afirmación «todas las filas de orden 1 tienen direcciones donde se anula el coeficiente» falla para \(a^2<x_c\). Por ejemplo, en \(a=1/\sqrt2\),
   \[
   \beta=\pm\frac{\sqrt6}{12}
   \]
   es isotrópico y no nulo. Su supremo es aproximadamente \(0.2041\), no \(1/9\).

   Además, en un cluster fijo los extremos positivos y negativos no tienen igual magnitud, y puede existir un solo signo. Las dos columnas calculadas usando el mismo supuesto `sup=1/9` no representan extremos direccionales reales de ese cluster.

   **Reparación:** almacenar y presentar \(S(a)\), \(\max(B-M,0)\), el umbral \(x_c\) y el signo del cluster. Etiquetar los números actuales como envolventes conservadoras. Para una cota D1 exacta, maximizar \(E_{\rm QG,1}^{\rm signo}|\beta|\), respetando los signos realmente disponibles.

3. **La desaparición de \(\beta\) en una dirección no autoriza usar simplemente \(3\alpha\) — informe §3 y padre §3.5.**

   De la expansión adjunta se deriva, para dirección de **vector de onda** fija,
   \[
   \frac{\nabla\varepsilon}{c_0}
   =\hat n(1+2\beta t+3\alpha t^2)
     +t\nabla_S\beta+t^2\nabla_S\alpha+\cdots,
   \]
   y por tanto
   \[
   \boxed{\frac{|\nabla\varepsilon|}{c_0}
   =1+2\beta t+
   \left(3\alpha+\tfrac12|\nabla_S\beta|^2\right)t^2
   +O(t^3)}.
   \]
   El término angular desaparece si \(\beta\equiv0\), pero no necesariamente si sólo \(\beta(\hat n)=0\).

   Hay un contraejemplo directo a la justificación del supuesto retorno al orden cuadrático: para L5a/L5b/L4, en \(n_3=0\),
   \[
   3\alpha=-\frac{n_1^2n_2^2}{6},\qquad
   \tfrac12|\nabla_S\beta|^2=\frac{n_1^2n_2^2}{6}.
   \]
   Se cancelan. En la convención de velocidad usada por el informe, tampoco queda corrección cuadrática allí.

   **Reparación:** retirar la afirmación general de que esas direcciones «vuelven a cotas de orden 2». Distinguir \(\beta\equiv0\) de un cero direccional y precisar dirección del vector de onda frente a dirección de propagación. Este fallo no altera los cálculos principales de las seis filas con \(\beta\equiv0\).

4. **El registro respalda los números transcritos, pero no permite declarar verificadas las fuentes en esta revisión — informe §2 y registro de fuentes.**

   Los cuatro valores ML de LHAASO y el rango direccional de Kostelecký–Mewes coinciden entre contrato, script y registro. No detecto una sustitución accidental de cotas isotrópicas SME por direccionales.

   Hay, sin embargo, una discrepancia interna no explicada: los números atribuidos al abstract de LHAASO equivalen a
   \[
   10E_{\rm Pl}=1.22\times10^{20}\ {\rm GeV},\qquad
   6\times10^{-8}E_{\rm Pl}=7.32\times10^{11}\ {\rm GeV},
   \]
   superiores a los ML usados. Podrían corresponder a otro procedimiento; los adjuntos no lo aclaran. No demuestra que los ML estén mal, pero impide presentarlos como corroborados por esas frases del abstract.

   La aplicación direccional de una ley isotrópica es admisible como transferencia condicional si se mantienen sus restantes hipótesis. No convierte el resultado en un ajuste anisótropo ni permite combinar libremente el \(K\) de una fuente con otras direcciones observadas.

   **Reparación:** atribuir las entradas específicamente a la transcripción de Table I, método ML, y Table III. Mantener explícita la falta de comprobación primaria en esta revisión y las condiciones de transferencia.

5. **El script reproduce la simplificación del informe, pero no completa todas las cantidades contratadas — contrato §4, informe §§3 y 5.**

   Por inspección, las fórmulas y constantes del código concuerdan con el registro. No obstante:

   - `sup=1/9` en L3s4 almacena una cota inferior del supremo como si fuera el supremo.
   - No se calcula el rango angular completo de L3s4.
   - Faltan todas las frecuencias D2.
   - La dependencia conocida de \(c_0\) en \(a\) no justifica dejar sin expresión \(f_{\min}\) para L3s4.

   Por ejemplo, con el extremo D1 conservador,
   \[
   f_{\min}^{\rm cons}(a)
   =\frac{2\sqrt3\,c\,E_{\rm QG,1}^{\rm sub}S(a)}
          {a\,\hbar c}.
   \]
   Para D2,
   \[
   f_{\min}(a,K)=\frac{\sqrt3\,c\,S(a)}{aK\hbar c}.
   \]
   En L5a/L5b/L4, las frecuencias D2 omitidas serían aproximadamente \(1.46\times10^{57}\)–\(4.18\times10^{57}\) Hz.

   Los dos `passed=True` de Hi/Hk son registros deliberados de evaluación, no comprobaciones de que las hipótesis sean verdaderas. Esto está reconocido en el informe; no lo considero un engaño. Los siete restantes tampoco verifican por sí solos signos, ceros, constantes, emparejamientos físicos o fidelidad al padre.

   **Reparación:** representar por separado valores exactos y envolventes, completar las expresiones omitidas y describir el alcance real de las comprobaciones.

6. **Hay imprecisiones menores de presentación — informe §§1 y 2.**

   La comprobación manual
   \[
   \ell/\ell_P=E_{\rm Pl}\,9/(2\times10^{20})
   \]
   debe llevar \(\simeq\): con las constantes declaradas, \(\hbar c/\ell_P\simeq1.22089\times10^{19}\) GeV, mientras \(E_{\rm Pl}\) se redondea a \(1.22\times10^{19}\).

   En Hk, la cota sobre \(\ell\) es **mínima y más restrictiva** en \(\sup|\alpha|\), no «mayor». La separación típica entre \(10^{-27}\) y \(10^{-49}\) m es aproximadamente 22 órdenes, no 21. Y los valores D2 de la tabla resumen son redondeos: no deberían presentarse como desigualdades estrictas más fuertes que los números detallados.

   **Reparación:** corregir esas frases y distinguir límites numéricos de aproximaciones.

**Aceptaría este alcance:** tomando los coeficientes del padre y las cotas bibliográficas transcritas como entradas, los diccionarios declarados producen sensibilidades máximas D1 conservadoras de \(0.284\)–\(0.567\,\ell_P\) para las cinco filas lineales de coeficientes fijos, y una envolvente \(\le0.5494\,\ell_P\) para L3s4. Las seis filas exclusivamente cuadráticas dan \(1.40\)–\(4.58\times10^{-27}\) m en sus direcciones más sensibles. D2 proporciona las sensibilidades de polarización tabuladas, condicionadas adicionalmente al emparejamiento SME.

Eso sostiene Hi y Hk en su lectura de orden dominante y sensibilidad angular declarada. **No sostiene una separación observacional de las redes válida para orientación desconocida, ni la formulación general de §4.**