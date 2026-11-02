<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 477d4b55b03eb58f33018e92ce34d6e742541bb5d81f521999691b6d02916860
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-02T13:24:14Z  fin: 2026-11-02T13:38:22Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-02--l6b-triangular-row.md ; último commit observado: a19e480 ; sha256 de la copia enviada 201a62e186976639dc351da55355820b8327dff971e0badd53a58ed9835afe4c
documento: /home/adnac/qca-causal-cones/scripts/verify_l6b_triangular_row_gate.py ; último commit observado: a19e480 ; sha256 de la copia enviada c2e91c237b023abde1199f8ef3bea143f49e559da35899c01e049a9ddf3f2441
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: 8d0276e ; sha256 de la copia enviada b91253117e141b972add6640834363fe34cbbc1d321fd00fbe01d22b7875eadb
documento: /home/adnac/qca-causal-cones/theory/L6B_TRIANGULAR_ROW_GATE.md ; último commit observado: b076670 ; sha256 de la copia enviada 28081b0cd8536bceeb732c6740a07b53239ed8d32a678e52d8177b0b60259829
documento: /home/adnac/qca-causal-cones/sources/1803.01015v2.pdf ; último commit observado: 30672ba ; sha256 de la copia enviada 1d1de6058787437bb712448af11dd6b57d83f73fbe6cb7e6dffd242a45f8a570
entrada_grok.txt sha256 37568e67f30cb8437107f374cfc61ddb53664f7c9040e81d21eae4162c50be3c
respuesta sha256 a60eff5b15aa8f09d2fc72ba029c136710bfdceb5448d2781366233a7a392b2a
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias. No reejecuté el verificador y no confirmo el recuento 64/64: el dictamen sale de la p. 4 de ADMP, de la geometría reconstruida y del texto del código.

## 1. ENCODING — PASS

El texto fija la clase admisible, no un etiquetado único. Dos frases bastan, sin la Figura 1.

Pegado con la misma etiqueta. El ejemplo («v0 blanco y v1 gris pegados por el lado k=1, luego ψ(t,v0,1)=ψ(t,v1,1)») usa el mismo índice, y la Eq. (12) escribe el predecesor del vecino como e(v,k) en el lado k−1, el mismo número k. La etiqueta es de la arista, no de cada triángulo por separado.

R antihoraria y k→k+1. «El componente del lado k salta al lado k+1 mod 3» y el ejemplo Rψ=(ψ(k−1))_{k=2,0,1} dicen lo mismo: el valor nuevo en k viene de k−1. Antihorario está fijado por la orientación del plano.

Geometría. Con lado 1, f1=(1/2,0), f2=(1/4,√3/4), el triángulo arriba de vértices (0,0), (1,0), (1/2,√3/2) tiene puntos medios h=(1/2,0), b=(3/4,√3/4), s=(1/4,√3/4). Respecto del centroide (1/2,√3/6) los ángulos son −90°, 30°, 150°, así que el sucesor antihorario es h→b→s→h. El triángulo de abajo que comparte b tiene vértices (1,0), (1/2,√3/2), (3/2,√3/2); sus puntos medios, ordenados, dan el mismo ciclo. `down_of` y `down_edges` describen ese triángulo. El teorema de la paralela media da saltos de longitud 1/2: desde h, (1/4,√3/4) a 60°, (−1/2,0) a 180° y (1/4,−√3/4) a 300°. Rotar el triángulo 180° manda esos vectores a sus opuestos, 0°, 120°, 240°. F tiene seis vectores y 0∉F.

72 y 6. Hay 2 coloraciones × 3! × 3!. Con el mismo ciclo en ambos colores, la etiqueta crece +1 antihorario solo si λ(h)=a, λ(b)=a+1, λ(s)=a+2 (mod 3): tres rotaciones por coloración. La lectura declarada de la Figura 1, h:2, b:0, s:1, es el caso a=2. Sin la figura esa lectura queda sin auditar; no selecciona, porque las tres rotaciones comparten el predecesor geométrico s→h, h→b, b→s. La Eq. (12) solo usa ese predecesor. El símbolo depende a lo sumo de la coloración, y el código construye las dos.

Eq. (11). Uk actúa en el sitio, constante en z. Para cualquier E invertible constante y diagonal por orientaciones, E†UE tiene el mismo polinomio característico por semejanza, y el mismo soporte: cada bloque entre orientaciones se multiplica por invertibles y los monomios distintos no se mezclan. El `record` de la codificación, con E=diag(U0,U0 S,U0 S²) en el orden (h,b,s), es ese hecho lineal; no puede fallar y no distingue el alineamiento de la Figura 1. La dinámica certificada es la Eq. (12), que ya está en espinores precodificados. Aclaración, no fallo.

## 2. INTERNAL_DIMENSION — PASS

Cada arista pertenece a un solo triángulo arriba, y ninguna traslación que conserve el coloreado manda orientaciones distintas entre sí: las traslaciones conservan la dirección de la arista. La celda tiene tres aristas × C², así que s=6. El s=2 de la tabla padre cuenta el C² de una arista. Ha solo cuantifica filas con s=2, de modo que L6b queda fuera de su alcance y Ha sigue REFUTED_BY_ROW_L6a, como fija el §5 del contrato. El `record` `U.rows==6` repite el tamaño construido en `zeros(6)`; el contenido está en la geometría, no en esa línea.

## 3. C0 — PASS

Normalización. El paso más largo es 1/2 lado. En las unidades de la fuente la distancia entre puntos medios es √3/2, luego el lado es √3.

Nodo. Con M=I, W=U0 S U0† y S³=I implican W³=I en las dos lecturas. U(0)=P⊗W con P el 3-ciclo de orientaciones, así que U(0)³=I. La lectura del padre tiene autovalores de W iguales a 1 y e^{−2πi/3}; la impresa, 1 y e^{2πi/3}. En ambos casos los productos con {1,e^{±2πi/3}} dan ese conjunto con multiplicidad 2. El par de autovalor 1 es el nodo de la p. 4.

Ruta A. Cada paso avanza la orientación, así que U³ es diagonal por bloques 2×2 y V(0)=I. `node_speeds` sobre ese símbolo, con U(0)=I, es el cono de las seis bandas plegadas a cuasienergía 0. En la rama del nodo, Ω=3ω, luego c0(U)=c0(V)/3. El desarrollo de la fuente,

T(0,3ε)ψ = ψ − (√3/2) ε (σ·∂)ψ + O(ε²),

junto con T(0,3ε)=ψ+3ε ∂t ψ, da i∂t ψ = (√3/6)(p·σ)ψ. Por tanto c0(V)=1/2 lado por cada tres actualizaciones, 1/6 lado por actualización y, al dividir por el paso 1/2, c0=1/3. En lado √3: (1/6)·√3=√3/6. La línea `src = c0*ell*sqrt(3)` es exactamente esa conversión; el `ell` se cancela y el chequeo contrasta c0(V) con la fuente.

Ruta B. En el autoespacio de autovalor 1, U(0) actúa como I, el hueco hasta e^{±2πi/3} es finito y el término lineal no se mezcla con las otras bandas. Si U(k)≈U(0)(I−i k·X), entonces X=i U(0)† ∂k U. Comprimir con la Q ortonormal del núcleo es la perturbación degenerada de primer orden. El cono isotrópico sin tilt de esa 2×2, dividido por `ell`, es c0 por actualización. Las dos rutas usan el mismo símbolo y métricas distintas (V frente al núcleo de U); coinciden si la rama ω=Ω/3 está bien extraída. No detectan solas un error común de escala: eso lo cierra el coeficiente de la fuente.

Las dos W están bien transcritas. Padre: U0=[[c,s],[−s,c]] y S†, el par que el propio padre necesita para la Eq. (8) y el orden de los τi. Impresa: U0=Ry(+arccos√(5/3)) y S=diag(1,e^{2πi/3}), que es e^{iπ/3} Rz(2π/3). Ejecutar ambas y no reparar el signo cumple el §6. Que las cuatro combinaciones den las mismas entradas es una salida del verificador; la construcción, no esa igualdad numérica, es lo que queda revisado.

## 4. C_STRICT — PASS

No hay hueco. La nilpotencia de un paso y la cota de U³ hacen trabajos distintos.

Un paso. La orientación cambia siempre, así que el mismo desplazamiento no se compone consigo: el coeficiente M cumple M²=0. Los seis puntos de F son vértices del hexágono regular. Por eso h∞ es estrictamente más pequeño que la función soporte de Cmicro, y Hb puede fallar. El test de un paso del padre devolvería OPEN; el contrato deja OPEN solo lo indecidible.

Tres pasos. Para un vértice v de un hexágono regular la recta de soporte radial toca solo ese vértice: los vecinos tienen proyección 1/2. La única escritura de m v como suma de m puntos del soporte es v+…+v, así que el coeficiente de V^m en m v es Mv^m. `nilpotent` comprueba M^6=0 en matrices 6×6, equivalente a nilpotencia. Si no es nilpotente, Mv^m≠0 para todo m y el vértice sobrevive. Eso da h(conv supp U³) como función soporte de la caminata V.

Pegado a U. Con n=3m+r y r<3, supp U^n ⊂ supp U^r + supp V^m, a distancia acotada independiente de m. Esa inclusión acota por arriba: limsup (1/n) h(Sn) ≤ h(conv supp U³)/3. A lo largo de n=3m el vértice se alcanza, así que el límite vale exactamente eso. Por tanto

h∞(n̂) = h_{conv supp U³}(n̂) / 3.

El soporte entero de L6a, leído con los generadores a mitad, es el hexágono de radio 1 (lado) y vértices en múltiplos de 60°: (2,0), (0,2), (2,−2) y sus opuestos tienen longitud 2 con los generadores de L6a y longitud 1 con los de L6b. Inradio √3/2 por cada tres actualizaciones, √3/6 por actualización, y al normalizar por 1/2 queda 1/√3. Cmicro tiene radio de vértice 1 ya normalizado; el cuerpo asintótico tiene radio (1/3)/(1/2)=2/3 y la misma orientación, así que c_strict^iso / r_in = 2/3. La nilpotencia de un paso no entra en esta igualdad; explica 1/√3 < √3/2.

## 5. CROSSCHECK_L6A — PASS

El cambio es legítimo. El contrato pide comparar sustrato y c0, no la identidad matricial en un marco fijado por el código. Los saltos de L6b desde h van a 60°, 180° y 300°; los ui de la Eq. (4) van a 0°, 120° y 240°. El desfase de 60° es el teorema de la paralela media, anterior al fallo de la primera ejecución. Probar las 12 isometrías es recorrer el grupo diedral, no buscar un modelo: la rotación de 60° en la base entera es [[0,−1],[1,1]], que es la `rot` del código, y `z^h → z^{Mh}` está bien suscrito. El conjunto soporte puede coincidir con el F de L6a, como comprueba `set(supV)==set(sup_a)`, mientras los coeficientes solo coinciden tras rotar, porque el hexágono es invariante y la asignación de amplitudes no.

La igualdad de polinomios característicos, en bloques 2×2 unitarios, iguala las cuasienergías como funciones del cuasimomento entero después de la isometría. Eso fija la dispersión y, por isotropía, c0. No da un entrelazador independiente de k ni la igualdad de las monedas. El contrato no lo pide. La escala queda aparte: mismos enteros con generadores a la mitad, que el informe declara.

## 6. SCOPE_AND_CODE — PASS

El veredicto L6B_PARTIAL_VGRP_OPEN es el del §6: hay codificación admisible, las entradas 1–5 quedan llenas y V_grp^max sigue OPEN. La fila masiva no se toca. Ha no cambia de estatus. Hb falla en todas las asignaciones admisibles, 1/√3 < √3/2, así que pasa a REFUTED_BY_ROW_L6b sin necesitar la Figura 1. Hc, 1/3 ≤ 1/√3, queda afirmada en esta fila; el §5 ata la frase CONFIRMED a que ambas valgan, pero el libro es por hipótesis, el informe se marca preliminar y no promociona. No es un exceso.

Chequeos débiles, que no cargan la tabla: `U.rows==6`; W³=I, que es S³=I; y el polinomio característico bajo la conjugación constante de la Eq. (11). Los valores salen de `hull`, `nilpotent` y `node_speeds` sobre el símbolo, contrastados con √3/6, con el soporte de L6a y entre las cuatro variantes. El padre se importa y no se reescribe: el `SOURCE_GAPS["L6b"]` adjunto sigue diciendo que la fila no está codificada.

## Reparaciones obligatorias

Ninguna. Aclaraciones ya incorporadas arriba, que no cambian entradas ni veredicto: la Eq. (11) no fija un solo etiquetado; su chequeo de espectro es semejanza; `U.rows==6` no demuestra la celda; el acuerdo de las rutas A y B no sustituye el coeficiente de la fuente; el polinomio característico no es equivalencia de operadores.
