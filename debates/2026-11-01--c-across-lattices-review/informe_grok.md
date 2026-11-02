<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 4253a67d69d18a63d2d07fb19228e7854b71055e429ba9d04221d8bd2a1c3e3f
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-01T22:14:09Z  fin: 2026-11-01T22:29:02Z
documento: /home/adnac/qca-causal-cones/theory/C_ACROSS_LATTICES_GATE.md ; último commit observado: 30672ba ; sha256 de la copia enviada b58deeec91184fbf976a6cb857c8e935ec7d4a4e52d6608a62768452759e34e3
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--c-across-lattices.md ; último commit observado: aab5e7b ; sha256 de la copia enviada 429c35518299fb369180abec9df4056bf59de8e2c99719f533b3628349bfa3fe
documento: /home/adnac/qca-causal-cones/scripts/verify_c_across_lattices_gate.py ; último commit observado: cae6e30 ; sha256 de la copia enviada 1da30dab9060c8d97a4452eb07451f7886325f4fd87ce22a27cdd950dfee9645
documento: /home/adnac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/adnac/qca-causal-cones/sources/1803.01015v2.pdf ; último commit observado: 30672ba ; sha256 de la copia enviada 1d1de6058787437bb712448af11dd6b57d83f73fbe6cb7e6dffd242a45f8a570
documento: /home/adnac/qca-causal-cones/sources/1803.01304v1.pdf ; último commit observado: 30672ba ; sha256 de la copia enviada 9fa0ea34763b4dd01fe2c38d699ecf5358b98b6b1582381f95330c84eb90ff90
documento: /home/adnac/qca-causal-cones/sources/1802.03910v1.pdf ; último commit observado: f74018f ; sha256 de la copia enviada ecbca6d8dea9c5b79c5d692f45443a6e1e8cbb6a99a381326af7b4294981c9b8
documento: /home/adnac/qca-causal-cones/sources/1312.2852v1.pdf ; último commit observado: f74018f ; sha256 de la copia enviada a6babd4fdb67f84a24dc1b00fe3a8a484c0511c8da8d209eec14a352624fc95a
documento: /home/adnac/qca-causal-cones/sources/1708.00826v2.pdf ; último commit observado: f74018f ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_grok.txt sha256 c062bab84ef1010241d29895dc4a0e959e03583660d664b8b73162cc25a2944a
respuesta sha256 18065027a9932c521558a760a66f0330150ffb7e9b4ebf80631bd62fba5472d1
-->

**Dictamen global: `REPAIR_REQUIRED`.** No ejecuté el verificador y no confirmo el recuento 103/103. Las identificaciones de sustrato, los `c_0` sin masa que se reconstruyen desde las fuentes y el argumento de vértices aguantan. Bloquean la promoción tres cosas: la tabla exacta no está cerrada por asertos que fallen el proceso, la frase que presenta la velocidad continua como test del orden `Π` es falsa, y los tokens de Hb y Hc cubren una fila declarada que sigue `OPEN`.

## 1. SOURCE_READING — `PASS`

Los símbolos codificados siguen a las ecuaciones, con las dos ambigüedades que el propio informe declara.

**Fase.** Desplazar la amplitud en `h` lleva `e^{-i k·h}`. En JDW, `(SΨ)(X)=ψ(N(X))` con `N=X+v` toma el valor en `X+v`, así que el caminante se desplaza `h=-v`. Farrelly–Short escribe `S_q=exp(-i(q·P)a)` para el salto `|n⟩→|n+q⟩`: el código de L5a (`z^{+e}` en el proyector up) coincide con eso. Respecto de la onda plana de JDW, `exp i(ωt-k·X)`, el mismo muestreo da `e^{-i k·v}` y el código da `e^{+i k·v}`: es `k→-k`. Los escalares certificados (`U(0)`, conos cuadráticos, Hessiana) son pares. No cambia la tabla.

**Orden.** En los productos escritos, el índice menor actúa primero. JDW (4) termina en `U_1 S̃_1` a la derecha; el código de L6d es `R̃_2^{-1} S̃_3 R̃_2 R̃_1^{-1} S̃_2 R̃_1 S̃_1`. JDW (6) es `Ŵ_3 Ŵ_2 Ŵ_1`; el bucle `j=1,2,3` acumula por la izquierda y deja `U^1 S^1` a la derecha. ADMP fig. 1 mueve primero `u_0`: `factors[2]*factors[1]*factors[0]`. MB (23) y FS (20) dejan el eje `Z` a la derecha: `T[0]*T[1]*T[2]`. Para `Π_{j=1}^{6}` y `Π_{j=1}^{3}` de JDW (2) y (8) el código usa el mismo criterio (`W_6…W_1`, `W_3 W_2 W_1`). El producto matemático usual `Π_{j=1}^n W_j=W_1…W_n` haría actuar primero al índice mayor. La elección queda alineada con (4) y (6), no con esa lectura de `Π`. Como cada factor libre cumple `W_j(0)=I`,
\[
i\partial_k(W_n\cdots W_1)\big|_{0}=\sum_j i\partial_k W_j\big|_{0},
\]
el cono lineal no depende del orden. La velocidad continua `c=1` no certifica el orden; sí pueden depender de él `F` si hay cancelaciones, la nilpotencia de `A_v` y la matriz `K`.

**`U(α,ξ,ζ,θ)`.** La matriz de JDW (1) está copiada literal. `U(0,0,-π/2,φ)=e^{-iφ σ_x}`. Con `Δt=3ε/2`, el ángulo `3ε m/2` es el hueco en `k=0` porque `W_0(0)=I`. En L6e, `θ_j=(j-2)π/4` da `U_3 U_1=I` en `k=0`; sustituir el ángulo de `Û^1` por `-π/4+m` da `U(0)=e^{-im σ_x}`.

**Vecinos.** Con `g_1=(1,0)`, `g_2=(1/2,√3/2)`, los `X_1…X_6` de JDW p. 2 caen en `TRI`. L6c lee `(N_j,N_{j+1})` con `N_7=N_1`. L6d lee `(N_j,N_{j+3})`. El isósceles con `g_1=(1/2,1/2)`, `g_2=(-1/2,1/2)` reproduce `X_1=(ε,0),…,X_6`. L6f lee `(N_1,N_2)`, `(N_2,N_3)`, `(N_3,N_1)` sobre `u_0,u_1,u_2`.

**Clifford (L5b).** `ΔP=(σ_x⊗σ_x, σ_x⊗σ_y, σ_x⊗σ_z)`, `Q=σ_z⊗I` son involuciones que anticonmutan, representación irreducible en `C^4` como piden MB (25)–(27). El coin va a la derecha, `e^{-iθ Q}`, como en (23). `P^±=(I±ΔP)/2` con el salto `+1` en `P^+`. Cualquier otra representación irreducible da el mismo cono.

**`τ_i` y los dos signos (ADMP).** Con `ξ=√5/3`,
\[
τ_0=\tfrac23 σ_x+ξ σ_z,\quad
τ_1=-\tfrac13 σ_x+\tfrac{√3}{3}σ_y+ξ σ_z,\quad
τ_2=-\tfrac13 σ_x-\tfrac{√3}{3}σ_y+ξ σ_z
\]
es (5), y `∑ τ_i=√5 σ_z`. El vector de Bloch de `τ_0` es `(2/3,0,√5/3)`. La rotación de Bloch que lo lleva a `σ_z` es `-arccos(√5/3)`, no el `+arccos` impreso en (8). `S=e^{iπ/3} R_z(2π/3)=diag(1,e^{2π i/3})` cumple `S^3=I`, pero `S^† τ_0 S` gira `-2π/3` y cae en `τ_2`, no en `τ_1`. Con `S^{-1}` el orden `(τ_0,τ_1,τ_2)` cuadra, y el símbolo primario sale de los proyectores de (5), no de `S` impreso. El conjunto `{±2u_i}` no cambia. El informe lo registra; no lo repara en silencio. El contrato, §6, pide exactamente eso.

**Exclusiones.** Arrighi–Facchini queda fuera por el contrato (encoding previo, coins que dependen de la posición, `F` no comparable). L6b no está excluida: está `OPEN`. La eq. (12) define la dinámica con `e(v,k)` y la incidencia blanco/gris solo en la Fig. 1; el texto no fija los vectores de los puntos medios. `OPEN` con esa razón es una parada válida (§6). No verifiqué la equivalencia con L6a en tres pasos; el informe tampoco, y lo dice.

## 2. STEP_SETS — `PASS`

Reconstrucción, con `ε=1`.

- **L5a, L5b.** Tres saltos condicionales `±e_i`. Las ocho sumas son `{±1}^3`, el vecindario BCC de L3. El orden no altera el conjunto.
- **L6a.** `u_0+u_1+u_2=0`, luego `∑_{i=0}^2 ε_i u_i ∈ {0}∪{±2u_i}`. Hexágono de radio 2. En la base `(u_0,g_2)` esos vectores generan el subgrupo de índice 4.
- **L6d.** `X_4=-X_1`, `X_5=-X_2`, `X_6=-X_3`, así que cada `S̃_j` aporta `±X_j` con `X_1,X_2,X_3` a 60°. Las ocho sumas son exactamente `{0}∪{±2u_i}`. Mismo `F` y mismo grupo que L6a. Cada vértice es un solo camino: que el coeficiente no se anule es el chequeo de nilpotencia, no la geometría del conjunto admisible.
- **L6e.** `N_{j+3}=-N_j` y `C_2=I`, `C_1=(I+iσ_x)/√2`, `C_3=(I-iσ_x)/√2`. El coeficiente del ramo `(ε_1,ε_2,ε_3)` lleva `P_{ε_3} P_{ε_2}`, nulo si `ε_2≠ε_3`. Sobreviven cuatro sumas: `(±1,±1)`, todas de longitud `√2`, con matriz no nula (`⟨e_1|C_3|e⟩≠0` y por tanto `M^2≠0`). Tras dividir por `√2` es `N_2` de L2. Mismo sustrato, rotación incluida.
- **L6f.** Los ocho ramos de `(S_1,S_2,S_3)` dan `{0}` y el hexágono de radio `√3` con vértice en `(0,√3)`, girado 30° respecto de L6a. El cociente paso de red / radio del casco es 1, como en L6a: mismo sustrato a rotación y escala.
- **L6c.** El casco de la bola hexagonal de radio 2 en la red triangular tiene `3·2·3+1=19` puntos y el mismo hexágono de radio 2. El grupo fino (espaciado 1 frente a 2) no es el de L6a ni siquiera a escala: ese cociente es invariante (1/2 frente a 1). La tabla lo dice; el párrafo que habla de «dos sustratos» en 2D aplana mal esa distinción (aclaración, no un `F` mal calculado).

Ningún walk homogéneo de estas fuentes vive en una red de Bravais hexagonal: el panal no es un grupo, y `⟨F⟩` es triangular.

## 3. MASSLESS_SPEEDS — `PASS`

Normalización del contrato: un update, paso más largo = 1, luego `V_causal^max=1`.

**L6a, derivado sin el informe.** `T_i=e^{-i k·u_i} P_i^++e^{i k·u_i} P_i^-`, `P_i^+-P_i^-=τ_i`. En `k=0` cada factor es `I`, el producto es `I`, y
\[
i\partial_{k_a} U(0)=\sum_i u_i^a τ_i.
\]
La condición (C2) dice `∑_i (u_i·p) τ_i = p_x σ_x+p_y σ_y`. Generador sin traza (tilt nulo), cono isótropo de velocidad 1 en unidades de la fuente (`|u_i|=1`). El paso más largo mide 2, así que `c_0=1/2`. El inradio del hexágono regular de radio 1 es `√3/2`. Cociente `1/√3≠1`.

**JDW, por la escala que la fuente fija al escribir la Dirac con `c=1`.** `c_0=Δt/L`: L6c y L6d, `Δt=3/2`, `L=2`, `c_0=3/4`; L6f, `Δt=3√3/4`, `L=√3`, `c_0=3/4`; L6e, `Δt=1`, `L=√2`, `c_0=1/√2`. En todos, `U(0)=I` porque cada salto parcial es `I` y los `R^{-1} R` cancelan. `r_in`: hexágono normalizado `√3/2`; cuadrado de L6e/L2, distancia al lado `x=1/√2`, luego `r_in=1/√2`. El cubo `[-1,1]^3` de L4, normalizado por el vértice `√3`, da `r_in=1/√3` y convierte el `c_IR=1` del contrato en `c_0=1/√3`. BCC `{±1}^3` igual: `r_in=1/√3`.

`S(n̂)=c_0/h_C(n̂)`. Tras la normalización, `max h_C=1` y `min h_C=r_in`, así que `S_min=c_0` y `S_max=c_0/r_in`. Solo si `c_0=r_in` hay una dirección con `S=1`. No rederivé las autofases fuera del nodo `k=0` (ahí son 0). `V_grp^max` queda `OPEN`, como permite el contrato si no hay certificado exacto.

## 4. STRICT_BODY — `PASS`

Si `v` es vértice de `conv F` y `v∈F`, la única escritura de `nv` como suma de `n` vectores de `F` es `v+…+v`. El coeficiente en `U^n` es `A_v^n`. En dimensión finita, `A` no nilpotente equivale a tener un autovalor `λ≠0`, luego `A^n≠0` para todo `n`, y también a que alguna traza `tr(A^n)` no se anule (las sumas de potencias fijan el polinomio característico). Por tanto `C_∞^strict=C_micro` y `c_strict^iso=r_in` en toda fila donde eso se decide. `nilpotent` como `A^{s}=0` es el criterio correcto. L4 reutiliza el registro del contrato (§1: no recomputar filas ya hechas). En L6e el argumento cierra a mano: los cuatro vértices tienen `M^2≠0`.

## 5. MASSIVE — `PASS`

La identidad escrita no es la de operadores. Con `U=e^{-iH}`, `H(0)=θ Q`, `X=dH` y `Y=i(dU)U^†`,
\[
Y=\int_0^1 e^{-iuθ Q} X e^{iuθ Q}\,du.
\]
En bloques de `Q`, `Y_par=X_par` y `⟨+|Y|-⟩=e^{-iθ}(sinθ/θ)⟨+|X|-⟩`. No es el factor real `sinθ/θ`. El código forma `B=Y_par+(θ/sinθ) Y_perp`. Si `X_par=0`, los elementos de matriz dan `B=X e^{iθ Q}` y, como `X` anticonmuta con `Q`,
\[
\{B_a,B_b\}=\{X_a,X_b\}.
\]
La gramiana de `c_H` es la buena precisamente cuando el chequeo `X_par=0` pasa. El control 1D `[[cosθ\, e^{-ik}, i sinθ],[i sinθ, cosθ\, e^{ik}]]` con `Q=-σ_x` reproduce `c_H=c_0 θ cot θ`: es el bloque mínimo del gate Weyl/Dirac (`n=cos M`, `F=M cot M`).

Si el coin de masa multiplica por la izquierda a un hopping con `W(0)=I` y generadores que anticonmutan con `Q`, la conjugación `U_m T U_m^†` conserva la gramiana sin masa y el factor `θ/sinθ` sale solo. Eso cubre L5b, L6c, L6d y L6f: `c_H=c_0 θ/sinθ>c_0` para `θ∈(0,π)`. En L5b, `c_0=r_in`, así que `c_H` supera `r_in`. No contradice ninguna cota de propagación: `c_H` es coeficiente del logaritmo, no velocidad de soporte. En la familia estándar el hopping va con `cos M` y `c_H=c_0 M cot M<c_0`. Las dos lecturas conviven.

`G=(U+U^†)/2` es `cosθ\, I` en `k=0`. Si el gradiente se anula y la degeneración es el espacio entero, las curvaturas son los autovalores de la Hessiana, sin proyección extra. De `cos ω=cosθ-(sinθ/(2θ)) c^2|k|^2` sale
\[
\partial_a\partial_b\cosω=-(sinθ/θ)\,c^2\,δ_{ab},
\]
y la descomposición `Hess=-c_0^2 cosθ\, I+sinθ\, K` da, si `K=0`, `c_{ω^2}=c_0√(θ cot θ)`. Las `K` impresas no son múltiplos de `I` (diagonales distintas en L6c y L6f; fuera de diagonal en L6d y L6e): ahí no hay `c_{ω^2}` isótropo. No rederivé las fracciones `-5√3/32`, `√3/16`, etc. L6e, con la masa dentro de `U^1`, puede hacer anisótropa la parte lineal; el informe no le aplica `c_H=c_0 θ/sinθ`. La masa ADMP, `U(0)=∏_i e^{-iμ τ_i}`, no entra en esa factorización: `OPEN` es honesto. El flag `iso_W` del código significa `K≡0`, no «`K` escalar»; un `K=λ I` con `λ≠0` sería isótropo con otro valor. No es el caso de las matrices que el informe transcribe.

## 6. SCOPE_AND_CODE — `REPAIR_REQUIRED`

Ha está refutada por L6a: `s=2`, nodo en `k=0`, `c_0/r_in=1/√3`. También fallan L6c, L6d y L6f (`√3/2`). Una fila `OPEN` no salva un universal ya contradicho. El token `REFUTED_BY_ROW_L6a` es el del contrato.

Hb y Hc no. `CONFIRMED_IN_DECLARED_ROWS` significa toda fila declarada. L6b es declarada y está `OPEN`. El paréntesis del informe lo dice y el token lo desmiente. En las filas decididas el argumento de vértices da `c_strict^iso=r_in` y, con `c_0≤r_in`, Hc. L3s4 cumple Hc con `c_0=a/√3<r_in` y no entra en Ha (`s=4`).

El veredicto de tabla `TABLE_PARTIAL_…` es el correcto: L6b, la masa ADMP y `V_grp^max` abiertos, sin fila nueva.

**Chequeos que no prueban lo que parecen.** En `part2`, `c_strict` se asigna a `r_in` si los vértices sobreviven; el diccionario Hb solo mira `c_strict is not None`. Hc sí compara `c_0` con ese valor, pero solo en las filas que `analyse` visita (no L3, L4, L3s4). Los valores de la tabla —`c_0`, `r_in`, `g_rel=I`, las `K`— se imprimen. No hay `record` que falle si `c_0` de L6a no es `1/2` o si `g_rel[0,0]≠1`. El contrato §9 pide un verificador fail-closed de las cantidades exactas. Salir con código 0 no certifica la tabla transcrita. La cabecera del `.py` dice además que las partes 2 y 3 no están implementadas; el fichero sí las contiene.

No hay ley general, rigidez ni novedad en el informe. Bernstein queda como arte previo. La frase «ningún walk hexagonal declarado llega al techo» no dice que el sustrato no pueda llegar. P17 por fila queda `OPEN`; el contrato lo pedía como ítem de ejecución y la parada con razón es admisible. No exijo cerrarlo aquí.

## Reparaciones obligatorias

1. **Verificador, `part2`/`part3` (los `print` de `c0`, `r_in`, `g_rel`, `K`) y tablas §§4–5 del informe.** Esos números no están en `record`. Un cono isótropo con otro `c_0`, o una gramiana proporcional a `I` pero no igual a `(c_0 θ/sinθ)^2 I`, deja el proceso en éxito. Cierra la objeción un `record` exacto, tolerancia cero, de cada entrada certificada de la tabla (incluidas `g_rel-I=0` en L5b, L6c, L6d, L6f, la gramiana de L6e y las `K` impresas).

2. **Informe §2, frase que atribuye a `c=1` un test del orden.** Falla porque, si `W_j(0)=I`, el término lineal es la suma de las derivadas y no ve el orden de `Π` en JDW (2) y (8). Ese orden sigue siendo convención declarada y puede mover `K` y algún `A_v`. Cierra sustituir la frase y dejar el §7 como lo que es: acuerdo con la velocidad continua, no prueba del orden. No hace falta calcular el orden opuesto para cumplir el contrato; sí hace falta no presentarlo como testeado.

3. **Informe §6, tokens de Hb y Hc.** `CONFIRMED_IN_DECLARED_ROWS` con L6b `OPEN` excede el vocabulario congelado. Cierra retirar el token y escribir que Hb y Hc valen en las filas decididas, con L6b `OPEN`.

## Aclaraciones que no son fallo matemático

El signo de Fourier frente a la onda plana de JDW es `k→-k` y no mueve la tabla. La identidad `Y=X_par+(sinθ/θ)X_perp` es incompleta; la gramiana queda bien cuando `X_par=0`, que es el chequeo que el código exige. «Dos sustratos» en 2D borra el grupo fino de L6c: misma forma de `C_micro`, grupo distinto (cociente espaciado/radio igual a 1/2, invariante de escala). El docstring inicial del verificador está atrasado respecto del código. Ninguna de estas cuatro, por sí sola, cambia un número de la tabla.
