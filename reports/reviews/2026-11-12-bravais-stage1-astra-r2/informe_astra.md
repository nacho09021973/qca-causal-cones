<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.167.2)
inicio: 2026-11-12T16:28:58Z  fin: 2026-11-12T16:32:43Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-bravais-stage1.md ; último commit observado: 6516892 ; sha256 de la copia enviada 0b48e5b01faa1f3b3f81051ef529c23c6a938e5ddde0e57b865e48859b37678a
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE_AMENDMENT_5.md ; último commit observado: 755f2ba ; sha256 de la copia enviada bfe04c51b388f17c9ec2195de7b28f74eb1c021019e2d576d48df956b3e14c84
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-bravais-stage1-astra-r2/informe_astra_ronda1.md ; último commit observado: sin versionar ; sha256 de la copia enviada 776765124de0da7a4457a7f8cf802744a34f46426cee4091173a82507570448a
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_BRAVAIS_GATE.md ; último commit observado: f301c21 ; sha256 de la copia enviada c3d94d73f6772c426abab829cc624bd3919e64321858ddcc8ae4c5fec918ef12
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE.md ; último commit observado: aa6c5f6 ; sha256 de la copia enviada ce398b36d0d74bfd10c389adad471ed93abbd1e0930d50a6e671faff068d7548
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stages-0-1.md ; último commit observado: 8eb504a ; sha256 de la copia enviada 613cff7db7c81af089a4e2d748f1735ee661683b47ce13f09a10afa740038389
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stage2-progress.md ; último commit observado: bb28f0c ; sha256 de la copia enviada 694ab7c78ac4a6d28a0c2dad8eb2a3cb945bbe6d237f1750da3a8e0f25698224
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stage2-leading-term.md ; último commit observado: 0cdaeac ; sha256 de la copia enviada ace6c7bfbbbebb7f0c42a89c926c2bf637e84c7a655dcb2a040fab05f54e14c0
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-bravais-stage1-astra/ir-carrier-stage-a-anon.md ; último commit observado: 2162420 ; sha256 de la copia enviada 4b926e904341be7dd79e90d4448823923fdfb7a0b70b5e59b189de045b06cf7c
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-general-ir-rate-grok/ir-corona-anon.tex ; último commit observado: 0cdaeac ; sha256 de la copia enviada 70b74038aa81d0ca0982e43209af318c1ee64352a21db5f616968bd9946a28f9
entrada_astra.txt sha256 51734ebd9c69ba9f2bbee42a1d176eea685af4ca4b0b131b9bb18abea414aa58
respuesta sha256 e7fcfb026ff751d0bcf91b5562abd587080cbecf023308ac3150456631bbcd74
-->

**Etapa 1 reparada: PASS, como adaptación relativa de las demostraciones generales indicadas.**

**Enmienda 5: REPAIR_REQUIRED.** La sustitución de la condición sobre la Hessiana es correcta. Falta precisar otro requisito que utilizan las pruebas: que la rama dominante sea **única en módulo en cada punto dominante**. La simplicidad algebraica, por sí sola, no garantiza ese requisito.

Estos dictámenes se basan exclusivamente en los textos adjuntos y en las derivaciones siguientes. El PASS de la adaptación no certifica las demostraciones de partida ni completa la admisibilidad general.

**Las cuatro objeciones de la primera ronda**

| Objeción | Estado | Razón |
|---|---|---|
| 1. Uso algebraico omitido | **RESUELTA** | U15 incorpora correctamente la estructura Laurent-polinómica y §2 utiliza su consecuencia. |
| 2. U6 y zona fundamental | **RESUELTA** | Se especifica la celda de Voronoi centrada en cero y se impone inclusión estricta. |
| 3. Afirmación universal de §6.1 | **RESUELTA** | «En general» y la excepción de las similitudes corrigen el exceso. |
| 4. Alcance del inventario y §7 | **RESUELTA** | Se excluyen expresamente las verificaciones particulares de K3 y se conserva el carácter relativo del corolario y la celda abierta. |

En U15, con \(p=B^{-T}t\), el determinante pertenece al anillo
\(\mathbb C[z_1^{\pm1},\ldots,z_d^{\pm1}]\). La identidad \(PP^\sharp=1\) implica que es una unidad, por tanto un monomio. Además, la segunda demostración es suficiente por sí sola: la identidad \(SS^\sharp=I\), obtenida por unicidad de los coeficientes de Fourier, continúa a los argumentos complejos. Así \(S(p)\) es invertible. Para cada \(\xi\) fijo, la continuidad y compacidad del toro proporcionan finitud de \(\Phi(\xi)\). No se introduce una hipótesis nueva.

En U6, los períodos no nulos tienen longitud mínima \(2\pi\lambda_1(L^*)\). Una bola cerrada de radio \(r<\pi\lambda_1(L^*)\) está estrictamente dentro de la celda de Voronoi y es inyectiva en el toro: la diferencia de dos de sus puntos tiene longitud menor que cualquier período no nulo. Esto verifica la reparación por dos vías. El umbral excluye solamente finitos \(N\) para cada red fija.

La reparación de §6.1 también es exacta: una similitud conserva bolas e isotropía, con las escalas correspondientes; una transformación lineal general no lo hace.

En cuanto al alcance, §6.3 reconoce correctamente que demostrar denominadores no nulos no demuestra admisibilidad. §7 debe leerse junto con esa limitación, como ya exige su formulación de corolario relativo.

**Completitud de U1–U15**

Para los usos de la red en las demostraciones generales de S01, SP, LT y CA adjuntas, **el inventario es completo dentro del alcance declarado**. No encuentro otro ingrediente de \(\mathbb Z^d\) que exija una hipótesis específica de Bravais.

En particular:

- La periodicidad del **integrando completo** en el desplazamiento de contorno está cubierta por U3 y requiere \(y-x\in L\).
- Las traslaciones de las clases de \(\Lambda_0\) en Poisson solo añaden fases unimodulares; están comprendidas en U7–U11.
- La separación de los caracteres no triviales respecto de \(2\pi\Lambda_0^*\) es positiva por discreción; el mínimo sobre los puntos dominantes es positivo por finitud.
- Las elecciones adicionales del radio local —inyectividad del toro, separación entre puntos dominantes y separación de frecuencias— cambian constantes, no hipótesis.
- Los promedios aritméticos usan números reales y caracteres del cociente, sin exigir coordenadas enteras en una base euclídea particular.

Esta conclusión **no incluye** la demostración de admisibilidad del manuscrito ni sus verificaciones particulares de K3. Incluirlas haría falsa la afirmación de completitud. El texto reparado ya las separa.

**Enmienda 5: comprobación matemática**

La identidad de Hessianas está bien utilizada, con una precisión esencial: ambas derivadas corresponden a **la misma rama local**, manteniendo fija la otra variable; no se está derivando el máximo sobre \(\eta\).

Sea
\[
f(p)=\log\lambda(p),\qquad H=(\partial_{p_j}\partial_{p_k}f).
\]
La simplicidad y la no anulación de la eigenvalue permiten escoger localmente esta rama holomorfa. Como \(p=\eta-i\xi\),
\[
\partial_{\eta_j}=\partial_{p_j},\qquad
\partial_{\xi_j}=-i\partial_{p_j}.
\]
Por tanto, entrada por entrada,
\[
\operatorname{Hess}_{\eta}\log|\lambda|=\Re H,\qquad
\operatorname{Hess}_{\xi}\log|\lambda|=-\Re H.
\]
Es una identidad de matrices completas, incluidos los términos mixtos. La equivalencia formulada en H2′ es correcta.

También es correcto que \(Q>0\) implica no degeneración de la Hessiana compleja. Escribiendo
\[
H=-(Q+iQ'),\qquad Q'=Q'^T\in M_d(\mathbb R),
\]
para cualquier \(z\in\mathbb C^d\setminus\{0\}\),
\[
\Re\bigl(z^*(Q+iQ')z\bigr)=z^*Qz>0.
\]
Luego \(Q+iQ'\) no tiene núcleo complejo. La implicación inversa no vale; el germen de la primera ronda demuestra correctamente esa insuficiencia local, aunque no constituye un paseo de la clase.

Los usos señalados quedan así:

| Lugar | Evaluación |
|---|---|
| S01, etapa 0(i) | Correcto para K3, donde se dispone además de la identificación local con \(\Phi\). |
| SP, §3.1 | H2′ proporciona exactamente la positividad que faltaba. El coeficiente lineal necesita además H8 y la dualidad de H1. |
| LT, §5 | H2′ justifica la coercividad gaussiana y el control del resto cúbico. La supresión de las otras ramas necesita además la separación espectral indicada abajo. |
| CA, §§1 y 4 | La misma conclusión en cada portador: H2′ da la parte real positiva de \(C_k\); H8 sigue siendo necesario para identificar la velocidad. |

En particular, si \(|\rho_3(\eta)|\le K|\eta|^3\) y \(q_{\min}>0\) es el menor autovalor de \(Q\), basta reducir el radio hasta \(Kr_0\le q_{\min}/4\). Entonces
\[
|\rho_3(\eta)|\le \tfrac14\eta^TQ\eta.
\]
La accretividad también justifica las inversiones y el complemento de Schur empleados en la integración normal.

**K3 sí satisface H2′, verificable con el manuscrito adjunto.** No hace falta aceptar los valores decimales ni los certificados externos. Para \(c=\cosh t_*>1\) y \(D=\sqrt{c^6-1}>0\), las fórmulas de Lemma 7.1(d) dan
\[
q_t=\frac cD>0,\qquad
q_n=\frac cD\frac{(c^2-1)(c^2+2)}{c^4+c^2+1}>0.
\]
Se recuperan directamente diferenciando
\(\Phi(\xi)=\operatorname{arcosh}(\prod_j\cosh\xi_j)\).
En los ocho puntos de \(\{0,\pi\}^3\), el producto de cosenos cambia únicamente de signo. La rama dominante cambia por un factor constante \(\pm1\), y su logaritmo de módulo conserva la misma Hessiana. El otro autovalor tiene módulo \(e^{-\Phi_*}<e^{\Phi_*}\).

**Objeción nueva decisiva: separación espectral no explicitada**

**Documentos:** enmienda 5, «Change» y «Effect»; contrato general, H2; LT §5; CA §§1 y 4.  
**Tipo:** hipótesis que falta en la lectura literal; exposición si «dominante» pretendía significar estrictamente dominante.

Las pruebas usan una descomposición con una sola rama principal y consideran exponencialmente menores las demás. Pero «a simple dominant eigenvalue» no declara inequívocamente
\[
|\lambda_0|>|\lambda_j|\qquad(j\ne0).
\]
Un autovalor puede ser simple y compartir el módulo máximo con otro autovalor distinto.

La diferencia se comprueba dentro de la estructura de símbolos unitarios de rango finito. A partir del símbolo \(S_0\) de K3, considérese
\[
S_\beta(p)=S_0(p)\oplus e^{i\beta}S_0(p),
\qquad \beta\notin\pi\mathbb Z.
\]
En cada punto dominante aparecen dos autovalores distintos y simples de módulo \(e^{\Phi_*}\). Ambos tienen la misma Hessiana de \(\log|\lambda|\), por tanto satisfacen la condición cuadrática de H2′. Sin embargo, el segundo bloque no es exponencialmente pequeño tras normalizar por \(e^{N\Phi_*}\).

Esto **no es un contraejemplo al teorema operacional completo**. Sí demuestra que simplicidad y H2′ no justifican descartar las otras ramas.

La reparación mínima es declarar:

> En cada punto dominante existe un único autovalor de módulo máximo; es algebraicamente simple y la Hessiana real indicada es negativa definida.

Si esa era la definición pretendida de «dominante», basta explicitarla. Admitir varias ramas de módulo máximo requeriría contabilizarlas en el término principal y revisar las hipótesis de aislamiento y cancelación.

Por ello, «No proof changes» solo es defendible en esta forma:

> No cambia el cálculo gaussiano; se fortalece su hipótesis declarada. Las estimaciones sobre las demás ramas presuponen dominancia estricta.

No se obtiene retroactivamente una demostración bajo H2 literal.

**Otras precisiones y límites del dictamen**

1. **H2′ no identifica en general \(Q\) con \(\operatorname{Hess}\Phi\).**  
   Documento 2, «Reason»; documento 6, etapa 0(i). Tipo: exposición preventiva.

   Si el máximo local se mueve con \(\xi\), para \(H=-Q-iQ'\) la Hessiana de la envolvente local es
   \[
   Q+Q'Q^{-1}Q',
   \]
   no necesariamente \(Q\). Con varios máximos activos, la envolvente puede incluso carecer de segunda derivada. La identificación usada en K3 es válida por su estructura particular. H2′ no sustituye H8; la enmienda no debe sugerirlo.

2. **La frase sobre ACSV sigue excediendo lo establecido.**  
   Documento 6, etapa 0(ii), «ACSV can supply … under H2». Tipo: exposición; reparación necesaria en ese documento de base.

   El propio apartado deja pendientes dominio de Laurent, minimalidad y cancelación del numerador. H2′ no descarga esas obligaciones. La frase debe ser condicional a ellas. Esta observación no invalida la adaptación Bravais ni el cálculo gaussiano directo.

3. **Persisten factores globales omitidos en la formulación abreviada de LT §3(c).**  
   Documento 8, §3(c). Tipo: exposición/reparación de fórmula, heredada.

   Para las sumas centradas en \(x_*,y_*\), los factores completos son
   \[
   e^{-i\eta_k\cdot x_*}\omega_k^{\lfloor Nu\cdot w_A\rfloor},
   \qquad
   e^{i\eta_k\cdot y_*}\omega_k^{-\lceil Nu\cdot w_B\rceil}.
   \]
   LT enumera únicamente las potencias de \(\omega_k\). CA §2 incorpora correctamente los factores continuos y demuestra su cancelación con el kernel. La Etapa 1, §5, utiliza esta versión correcta; no introduce un error de fase nuevo.

4. **Diagnósticos y documentos externos: NO_VERIFICADO.**  
   No están adjuntos los scripts citados por la enmienda. No puedo confirmar que sus columnas implementen exactamente H2′ ni que resulte apropiado conservar sus etiquetas. Tampoco están los textos completos de las enmiendas 1–4 y del contrato de portadores: sus formulaciones contractuales exactas quedan NO_VERIFICADAS. Esto no impide comprobar las identidades y los usos explícitos examinados arriba.

La ronda queda cerrada con **PASS para la adaptación Bravais reparada**, dentro de su alcance relativo, y **REPAIR_REQUIRED para la enmienda 5**, hasta precisar la dominancia estricta y acotar correspondientemente «ninguna prueba cambia».