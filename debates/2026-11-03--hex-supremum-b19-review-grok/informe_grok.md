<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 af8b13459acd3ed6802a74624f64d2615035950e4a4e9844652698dd02f80325
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T15:46:07Z  fin: 2026-11-03T15:57:48Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum-b19.md ; último commit observado: 6302328 ; sha256 de la copia enviada 92a6107f6e83b52effbd3b08823031270c77a10b7975dddd357cafd355aea95f
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_b19.py ; último commit observado: 6302328 ; sha256 de la copia enviada 244bb1065a7a0f76edc890637e289bda94b8477b3a1488792185e7e7c07cbb7a
documento: /home/ignac/qca-causal-cones/scripts/data/hex_s19_certificate.json ; último commit observado: 6302328 ; sha256 de la copia enviada 548988f768346eea02d0b58c89bc78bc60dd7a16ede01180525895181f3fd497
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum.md ; último commit observado: 677bec0 ; sha256 de la copia enviada 177d94d3e6991fb45fddadad218dd05c4ce7c0011419c481a2c94c5acccf0c88
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_gate.py ; último commit observado: 8abca3c ; sha256 de la copia enviada ef4b0114124d16937ced9a600a65b229c6fd968ab417d8493d1297806bf46a55
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
entrada_grok.txt sha256 55928596ec4ae876b7bf7e33fbff99603c3d5fd01461acc051cb68bc10451cc7
respuesta sha256 9cf1a842898ef558d57277eb501d48b2d55ff6d74c4aff50ae71cd46fb14056d
-->

**Dictamen global: REPAIR_REQUIRED.** La infeasibilidad real en S19 está bien encadenada (A3 y A4 necesarias, reducción lineal completa, Gram definida positiva implica \(p>0\) en todo \(\mathbb{R}^{18}\)). No se promociona todavía: el certificado no es la forma literal congelada en la Sec. 4 (ii) del contrato, y el prerregistro no se reescribe. Hay una sola reparación obligatoria (enmienda previa). No he ejecutado nada: los conteos 56/28/18/730, los 19 pivotes y el 17/17 solo puede confirmarlos una corrida; el código, tal como está escrito, sí comprueba esas afirmaciones de forma fail-closed.

### 1. Lema A3 — PASS, con aclaración

No se deduce de unitariedad y rigidez solas. Con la forma normal ya en vigor, \(A(v)=r\,v\cdot\sigma\), sí.

- Para \(s\) real fijo, \(f(z;s)=e^{irt}\langle x_+,U(tn+se)x_+\rangle\) es polinomio en \(z=e^{i\delta t}\): \(h\cdot n=m\delta\), \(|m|\le N\), \(r=N\delta\), luego el exponente \(r-h\cdot n=(N-m)\delta\) es múltiplo entero no negativo de \(\delta\). El factor \(e^{-is\,h\cdot e}\) solo entra en el coeficiente.
- \(|f|\le 1\) en la circunferencia por unitariedad, y \(f(\cdot;0)\equiv 1\) por la rigidez. Entonces \(f=1+sg+O(s^2)\) y \(|f|^2=1+2s\,\mathrm{Re}\,g+O(s^2)\le 1\) para ambos signos de \(s\), así que \(\mathrm{Re}\,g=0\) en el círculo. Un polinomio analítico con parte real nula en el círculo solo tiene modo de Fourier constante, y ese modo es imaginario puro: \(g\) es constante imaginaria. (Sin analiticidad solo sale \(\mathrm{Re}\,g=0\); el paréntesis del informe sobre la diagonal de \(K\) es correcto.)
- Los coeficientes de Fourier, agrupados por capa (mismo \(h\cdot n\), misma potencia de \(z\)), son exactamente \(-i\sum_{h\in\lambda}(h\cdot e)\langle x_+,A_h x_+\rangle\). El factor \(-i\) no afecta al enunciado.
- \(g(1)=-i\langle x_+,A(e)x_+\rangle=-ir(e\cdot n)=0\) usa \(\langle\sigma\rangle_{x_+}=n\) y \(A(e)=r\,e\cdot\sigma\). Eso es la forma normal isótropa, no la rigidez. Sin ella, \(g\) puede ser una constante imaginaria no nula y el momento de la capa extrema no se anula; las capas intermedias sí mueren por la constancia sola. En esta clase la forma normal es hipótesis previa (nodo, isotropía, marco de Bloch), no un supuesto nuevo de A3, y L1 ya implica \(A(n)=r\,n\cdot\sigma\) en las tres normales y, por linealidad, en toda dirección.
- El signo \(-\) vale igual: el prefactor es \(e^{-irt}\), las potencias de \(w=\bar z=e^{-i\delta t}\) son no negativas, y \(\langle x_-,\sigma x_-\rangle=-n\) da otra vez \(g(1)=0\).

Aclaración, no error de la identidad: la frase «consequences of unitarity and rigidity; they are not new assumptions» omite la forma normal. Conviene reescribirla; no cambia las ecuaciones que impone el verificador.

### 2. Lema A4 — PASS

La derivación es correcta y el emparejamiento no ignora frecuencias coincidentes.

De \(U^\dagger U=I\), al derivar en la dirección \(e\) sobre la recta de faceta, \(K=D^\dagger\partial_e U\) cumple \(K^\dagger=-K\). En la entrada fuera de diagonal eso es \(K_{+-}+\overline{K_{-+}}=0\). Con \(\partial_e U=-i\sum(h\cdot e)A_h e^{-ith\cdot n}\) salen exactamente las expresiones del informe:
\(K_{+-}=-i\sum(h\cdot e)\langle x_+,A_h x_-\rangle e^{it(r-h\cdot n)}\) y
\(\overline{K_{-+}}=i\sum(h\cdot e)\overline{\langle x_-,A_h x_+\rangle}\,e^{it(r+h\cdot n)}\).
Igualar la frecuencia \(r-\lambda=r+\lambda'\) da \(\lambda'=-\lambda\) de manera única, y los factores \(-i\) e \(+i\) producen la igualdad tal como está escrita, sin un signo de menos escondido. Cada frecuencia aparece una vez por cada lado; \(\lambda=0\) se empareja consigo misma y no se omite. La identidad de \(-\lambda\) es otra componente de Fourier de la misma antihermiticidad, no un conjugado redundante ni una restricción más fuerte.

El código hace lo mismo: `(xm.T*Abar*xp.conjugate())` es \(\overline{\langle x_-,A x_+\rangle}\) con \(w=\bar z\) formal. El control del cuadrado usa el conjugado directo sobre matrices numéricas; el de la tubería 3×3 usa el camino `Abar`. No los he corrido.

### 3. No se eliminan soluciones — PASS

A3 y A4 son necesarias en \(W_{hex}^{sym}\) bajo saturación y forma normal. El sistema lineal es exactamente L1 (sumas de capa: arista superior \(\to P_+\), inferior \(\to P_-\), intermedias \(\to 0\)), L2 (A3 para \(x_\pm\)) y L3 (A4). No están A2 ni las caras casi extremas.

`normals[:3]` basta. Son tres direcciones a 60°, no opuestas. La normal \(-n\) tiene \(e'=-e\), capas cambiadas de signo y \(x_+'=x_-\), \(x_-'=x_+\): A3 se repite y A4(\(-n\)) es el conjugado de A4(\(n\)), ya incluido al partir en real e imaginaria. Las opuestas no aportan restricciones distintas. Usar las seis no eliminaría soluciones; usar tres no deja fuera ninguna consecuencia lineal de A3/A4.

Menos restricciones no fabrican infeasibilidad. El riesgo sería una ecuación lineal de más: no la hay.

### 4. Reducción a 18 parámetros — PASS

La parametrización conserva todas las soluciones reales del sistema lineal. Tratar \(w\) como símbolo formal y volver a la forma real es legítimo: no se resuelve \((z,w)\) como variables complejas independientes. `real_form` sustituye \(z=x+iy\), \(w=x-iy\) y separa partes. Los coeficientes `[cr+dr, -ci+di]` y `[ci+di, cr-dr]` coinciden con \(\mathrm{Re},\mathrm{Im}\) de \(c(x+iy)+d(x-iy)\). El rango y el `rref` son exactos sobre \(\mathbb{Q}(\sqrt{3})\) (`DomainMatrix`, `extension=True`); si el aumentado tiene el mismo rango, toda solución real es un único \(t\) real, y \(P+iQ\) recorre esa familia afín.

`unitarity_equations` codifica las dos familias para todo \(d=h_i-h_j\): \(A_i A_j^\dagger\) da \(\sum_h A_{h+d}A_h^\dagger\) y \(A_j^\dagger A_i\) da \(\sum_h A_h^\dagger A_{h+d}\), con blanco \(I\) solo en \(d=0\), partes real e imaginaria, descartando ceros. No falta ningún \(d\) de soporte (fuera del soporte el coeficiente es cero). Los productos de afines son de grado \(\le 2\).

Que los libres sean 56, 28 y 18, y que haya 730 cuadráticas distintas, solo lo certifica ejecutar el verificador. El código sí lo exige (`free1==56`, `free2==28`, `len(t)==18`, `len(eqs)==730`) y aborta si el rango no coincide con el aumentado.

### 5. Certificado de Gram — PASS en la implicación; la corrida no está repetida aquí

- `sp.expand((v^T G v)-p)==0` con \(v=(1,t)\) es la identidad polinómica completa, no un muestreo. `gram_of` reparte bien constante, lineal (\(c/2\)), cuadrado diagonal y producto cruzado; si se equivocara, esa igualdad fallaría.
- Eliminación gaussiana sin pivoteo: en una matriz real simétrica los menores principales de cabeza son el producto de los pivotes, y es definida positiva si y solo si todos los pivotes son \(>0\) (Sylvester; en una definida positiva ningún menor de cabeza se anula, así que no hace falta permutar). Diecinueve pivotes positivos de la Gram \(19\times 19\) dan \(G>0\) sobre las 18 variables y la constante. Como la primera coordenada de \((1,t)\) es 1, \(p(t)>0\) para todo \(t\in\mathbb{R}^{18}\). En una solución \(p=\sum c_i f_i=0\). Contradicción. Basta una subfamilia de ecuaciones necesarias.
- `positive_q3` decide bien el signo real de \(a+b\sqrt{3}\): ambos cuadrantes no negativos, \(a^2>3b^2\) si \(a>0>b\), \(3b^2>a^2\) si \(b>0>a\), y falso si \(a+b\sqrt{3}\le 0\). Cero no cuenta como positivo. El fallo si el elemento no está en \(\mathbb{Q}(\sqrt{3})\) cierra por el lado seguro.
- La conversión algebraica es correcta como existencia: si \(0<\mu\le 1/(G^{-1})_{00}\), entonces \(G-\mu e_0 e_0^T=LDL^T\) con \(D\ge 0\) y coeficientes en \(\mathbb{Q}(\sqrt{3})\) (LDL no saca raíces de los pivotes), y
  \(-1=\sum_j(d_j/\mu)\ell_j^2+\sum_i(-c_i/\mu)f_i\).
  El verificador no construye \(\mu\), \(L\) ni \(D\): comprueba \(G>0\), que es lo que hace existir esa escritura y, más directamente, lo que prueba \(p>0\).

No he comprobado que los pivotes de este JSON sean positivos. Si la corrida fail-closed pasó, el teorema de infeasibilidad queda demostrado; el diseño del chequeo es el correcto.

### 6. Desviaciones literales del contrato — REPAIR_REQUIRED

La validez matemática es equivalente: \(p=\sum c_i f_i\) con \(c_i\) racionales explícitos y \(p>0\) en todo \(\mathbb{R}^{18}\) es un certificado exacto de que el sistema real no tiene solución, del tipo de la Sec. 4 (i) (polinomio en el ideal sin ceros reales). No es la forma (ii) tal como se congeló.

La Sec. 4 (ii) pide una identidad \(-1=\sum q_j^2+\sum h_i f_i\) «with exact rational coefficients» y que el verificador «expand[a] both sides». El informe dice, en la Sec. 3: «In the contract's form (Sec. 4 (ii)): … exact coefficients in \(\mathbb{Q}(\sqrt{3})\)». El docstring de `check_certificate` abre con «contract Sec. 4 (ii)» y admite que solo comprueba \(G>0\). Tres desvíos: cuerpo \(\mathbb{Q}(\sqrt{3})\) en \(G\), \(d_j\) y \(\ell_j\) (los \(c_i\) sí son racionales); no se expanden los dos lados de \(-1=\cdots\); el chequeo tarda unos 11 minutos, no «quickly». Lo de «rápido» iba contra relanzar un solver: aquí no hay solver (0 s de los 3600), pero la palabra del contrato no se cumple al pie de la letra. Los numeradores exploratorios no entran en el veredicto; cualquier \(c_i\) que deje \(G>0\) sirve, y el orden se autoverifica.

Esto debe declararse con una enmienda explícita, posterior al congelado, antes de promocionar. No se toca el prerregistro.

### 7. Controles y alcance — PASS, con aclaraciones

Los controles del cuadrado son pertinentes y el informe no los presenta como prueba de A3/A4: el paseo que satura cumple L1–L3, y en el soporte 3×3 (con interior, como S19) sigue dentro de la familia y anula las unitariedades reducidas. Eso detectaría una restricción lineal espuria o un signo mal puesto en `real_form` / `Abar`. No sustituye los lemas.

Los veredictos no se salen de lo demostrado. `PROVED_FOR_S19` es solo el hueco cualitativo en \(F\) dentro de S19, en \(W_{hex}^{sym}\) y por tanto en \(W_{hex}\), forma normal incluida, sin cota bajo \(r_{in}\). Incluye el soporte de JDW L6c porque ese soporte está dentro de S19, no porque se haya reconstruido el paseo. HX2 `CONFIRMED_FOR_S19`, y S7/S13 por T2 y por la etapa A ya promocionada, no por este certificado. M1-A sigue abierto para la clase: A1–A4 valen para todo soporte y no dan el hueco global. No hay nada para S25, soportes mayores ni \(s>2\). El nombre `OPEN_AFTER_SINGLETON_LAYER_ANALYSIS` se quedó corto (el análisis ya pasó de las capas singleton); el texto de la Sec. 5 no sobrereclama.

El informe sí dice dos cosas que el verificador no bloquea. «On S7, L1+L2+L3 leave 1 free parameter» y, en el control 3×3, «13-parameter family» y «298» ecuaciones: el código imprime esas cifras, pero el `record` de S7 es `True` incondicional y los otros dos solo exigen pertenencia y anulación, no el número. El rango flotante 56 está bien marcado como guía, sin veredicto. La identidad \(-1=\cdots\) está escrita como corolario, no como chequeo ejecutado.

### Reparación obligatoria

Una sola. En el informe, Sec. 3, la frase «In the contract's form (Sec. 4 (ii)): for \(0<\mu\le 1/(G^{-1})_{00}\), … exact coefficients in \(\mathbb{Q}(\sqrt{3})\)», y en el docstring de `check_certificate` la atribución a «contract Sec. 4 (ii)» con la afirmación de que comprobar \(G>0\) es esa forma.

Por qué falla: la Sec. 4 congelada solo acepta las formas nombradas; la (ii) exige coeficientes racionales y la expansión de los dos lados. Aquí \(G\), los pivotes y las formas lineales viven en \(\mathbb{Q}(\sqrt{3})\), y el verificador no construye ni expande la identidad \(-1=\sum(d_j/\mu)\ell_j^2+\sum(-c_i/\mu)f_i\). Dar por cumplida la (ii) promocionaría fuera del texto congelado. La prueba \(p>0\Rightarrow\) no hay solución real no queda invalidada.

Qué la cierra: una enmienda nueva, sin editar el prerregistro, que autorice para M1-B19 exactamente lo que el verificador hace: \(c_i\in\mathbb{Q}\), \(p=\sum c_i f_i\), identidad polinómica \(p=(1,t)G(1,t)^T\) y 19 pivotes \(>0\) en \(\mathbb{Q}(\sqrt{3})\), como certificado de la Sec. 4 (i) de que \(p\) no tiene ceros reales; y que esa comprobación sustituye la expansión literal de la (ii) y la restricción a \(\mathbb{Q}\). Ajustar esas dos frases para que no digan que la (ii) ya se verificó. No hace falta ningún resultado nuevo: S25 queda fuera.
