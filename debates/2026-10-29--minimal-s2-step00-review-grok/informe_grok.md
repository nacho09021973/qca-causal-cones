<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 3c635acb1aae335df9ffdb8bb9d71b53dc61013efd53c946886e79315431fc4f
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T11:25:53Z  fin: 2026-10-29T11:46:55Z
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step00.md ; último commit observado: dc4a6f7 ; sha256 de la copia enviada f10fcfb39802a35eb79452724a4dcfdee90f89405257f2440aead7f9bb9240e8
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step00.py ; último commit observado: dc4a6f7 ; sha256 de la copia enviada d6bf4189357f62faaacbbb64b294045d6b96da29725748f20198fdd3b8713b98
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
entrada_grok.txt sha256 60db54bf3681d0de9b7eff053186b603bd89096236114fa77a1e30c72b8dbcb2
respuesta sha256 d7e5e729a0340347dbdc91a011f69ad8f5049e59ce661198c54ad879adeeef92
-->

El argumento matemático de la etapa (a) es correcto en la enumeración, en los recuentos y en el lema. No es promocionable tal cual: el informe marca como verificado un enunciado que el certificado no comprueba.

Supuestos de esta lectura: no ejecuté el script; juzgo el código como argumento. No está adjunto `verify_irreducible_isotropy_step01.py`, así que no recompuse las matrices de Pavia. La traza de una rotación de ángulo θ en SO(3) es 1+2cos θ. Una involución de SO(3) es la identidad (traza 3) o un giro de 180° (traza −1).

## 1. Exhaustividad del Paso 0′

**Veredicto: correcto.** Cerrar todos los pares basta, los 16 `S_+` y las tres clases de P son los que dice el informe, y F es `{D4, O}`. La identificación salvo conjugación está bien implementada. La prueba escrita de la 2-generación no está en el informe.

`O` son las 24 matrices monomiales de signo con determinante 1: hay 3!·2³ = 48 matrices monomiales de signo y la mitad tiene determinante 1. El `V4` axial es el conjunto diagonal, `{diag(1,1,1), diag(1,−1,−1), diag(−1,1,−1), diag(−1,−1,1)}`, orden 4. El código construye exactamente eso.

Cerrar pares da todos los subgrupos si y solo si todo subgrupo es a lo más 2-generado. Eso es verdad, y no depende del «30 conocido»:

- Orden divisor de 24. Los grupos de orden 1, 2, 3 o 4 son cíclicos o `C2×C2`, ambos ≤2-generados. No hay `C2³` en `S4`: un 2-subgrupo abeliano elemental máximo tiene orden 4 (tres involuciones que conmutan: o tres doble transposiciones, o dos transposiciones disjuntas y su producto).
- Orden 6: no hay elemento de orden 6, luego es `S3 = ⟨(12),(13)⟩`.
- Orden 8: todos los grupos de orden 8 salvo `C2³` son ≤2-generados, y `C2³` no entra.
- Orden 12: índice 2, luego normal, y el único es `A4`. `⟨(123),(124)⟩` ya da `(234)` por conjugación y los 3-ciclos generan `A4`.
- Orden 24: `S4 = ⟨(12),(1234)⟩`.

El código recorre pares ordenados con repetición, así que también genera los cíclicos vía `⟨a,a⟩`. En un grupo finito el monoide generado coincide con el subgrupo porque el inverso es una potencia. El `require` de 30 encaja con el censo clásico (1 + 9 + 4 + 4 + 3 + 4 + 3 + 1 + 1), pero ese número es un contraste, no la prueba.

Los 16 `S_+` salen de elegir un vértice en cada una de las 4 parejas antipodales. El criterio del código no se solapa:

- Producto de coordenadas constante: solo los dos tetraedros regulares. En cada pareja antipodal los dos vértices tienen productos opuestos (tres signos), así que hay exactamente una elección con todos los productos +1 y una con todos −1.
- Una coordenada constante: cada valor fijo de una coordenada determina 4 vértices, y ese conjunto es una cara. Hay 6.
- Los 8 restantes son «vértice más sus tres vecinos». La suma de sus vectores es el doble del vértice distinguido, así que no son ni cara ni tetraedro.

Pares transitivos. Si `G` actúa transitivamente sobre 4 puntos, 4 divide a `|G|`.

- Tetraedro. Quien preserva un tetraedro preserva el otro, porque son complementarios. El estabilizador es el único subgrupo de índice 2, `T ≅ A4`, orden 12, y contiene al `V4` axial. Los subgrupos de `A4` son el trivial, tres `C2`, cuatro `C3`, un `V4` y `A4`. Solo `V4` y `A4` son transitivos en los 4 vértices: un 3-ciclo fija un vértice. No hay `C4` dentro de `T`. Luego, salvo conjugación, solo `(V4, tetraedro)` y `(T, tetraedro)`. `T` es normal y algún giro de 90° cambia un tetraedro por el otro, así que las dos elecciones de tetraedro son una sola clase.
- Cara. `O` es transitivo en las 6 caras, luego el estabilizador tiene orden 4: es el `C4` del eje de la cara, y es transitivo en sus 4 vértices. Su único subgrupo propio no trivial es el giro de 180°, con dos órbitas de tamaño 2. Ese `C4` contiene un solo giro axial de 180°, no el `V4` entero. Una sola clase.
- Vértice + tres vecinos. El estabilizador fija el vértice distinguido (preserva la suma), luego coincide con el estabilizador del vértice, que es un `C3` de orden 3. Ningún subgrupo puede ser transitivo.

El filtro del código es el de la definición: `G` estabiliza `S_+`, una sola órbita, y se descarta el par si algún `g ∈ O` lleva `(G,S)` a un representante ya guardado. `conj` es `gHg^{-1}` y la acción sobre `S` es la lineal. Para la cara, exige además que el grupo sea cíclico de orden 4. El descriptor que se afirma, `[(4, cara, False), (4, tetraedro, True), (12, tetraedro, True)]`, separa las tres clases.

Familia F. Transitivo sobre 8 vértices implica que 8 divide a `|G|`, luego `|G| ∈ {8, 24}`. `O` es transitivo. Un subgrupo de orden 8 es el generado por el giro de 90° alrededor de `z`, `(x,y,z) ↦ (−y,x,z)`, y el giro de 180° alrededor de `x`, `(x,y,z) ↦ (x,−y,−z)`: es el grupo diedral de orden 8 (`s` tiene orden 2 y `srs^{-1} = r^{-1}`), contiene al `V4` axial, y la órbita de `(1,1,1)` ya tiene los 8 vértices. Hay tres Sylow y son conjugados, así que una sola clase. `T` tiene orden 12, no divisible por 8. F = `{D4, O}`, ambos con el `V4` axial.

## 2. Representaciones

**Veredicto: correcto.** La identificación con homomorfismos `G → PU(2) ≅ SO(3)` salvo conjugación es correcta, enumerar hacia este `O` y clasificar por el carácter tridimensional es exhaustivo para estos cinco grupos, el criterio de reducibilidad es correcto, y los recuentos son 5, 3, 3, 6 y 4.

Una representación proyectiva unitaria de dimensión 2 es un homomorfismo a `PU(2)`. La equivalencia `R'_g = c_g W R_g W^†` es exactamente un cambio de levantamiento por fases seguido de conjugación en `PU(2)`. Como `PU(2) ≅ SO(3)`, eso es conjugación en `SO(3)`. La covarianza `T_{gh} = R_g T_h R_g^†` solo depende de la clase en `PU(2)`. El núcleo proyectivo es `{g : R_g escalar} = ker ρ`. Correcto.

Reducible equivale a que, tras equivalencia, todos los `R_g` preserven una recta, es decir a que `ρ(G)` fije un eje y sea conjugado a un subgrupo de `SO(2)`. En dimensión 3 impar, dos representaciones ortogonales con el mismo carácter son conjugadas por alguna matriz de `O(3)`: el promedio usual da un entrelazador invertible, y su descomposición polar sigue entrelazando. Si ese entrelazador `M` tiene determinante −1, `−M` tiene determinante 1 y conjuga igual, porque los signos se cancelan. Multiplicidad trivial ≥ 1 significa un vector fijo, es decir un eje fijo. En `SO(3)` esa multiplicidad solo puede ser 0, 1 o 3: el único elemento que fija un plano punto a punto es la identidad. El criterio del código, `sum(χ)/|G| ≥ 1`, es el correcto.

La apelación a la clasificación de todos los subgrupos finitos de `SO(3)` sobra para estos dominios, aunque la frase del informe es verdadera y está marcada como no rederivada. Las imágenes posibles son cocientes del dominio, y la traza queda fijada por el orden del elemento: 3, −1, 0 o 1 según orden 1, 2, 3 o 4. No hace falta el grupo icosaédrico ni los cíclicos de orden ≥ 5: no son cocientes de subgrupos de `O`. El censo por caracteres:

- `V4 = {1,a,b,c}`. Cada no identidad va a la identidad o a un 180°. Cinco caracteres: el trivial `(3,3,3,3)`; tres de núcleo orden 2, según qué elemento conserve traza 3; y el fiel, tres trazas −1. El fiel tiene multiplicidad `(3−1−1−1)/4 = 0`. Total 5.
- `T ≅ A4`. Cocientes: 1, `C3`, `A4`. El de núcleo `V4` manda los cuatro elementos de `V4` a traza 3 y los ocho 3-ciclos a traza 0. El fiel manda los tres orden 2 a traza −1 y los orden 3 a traza 0. Total 3.
- `C4 = ⟨r⟩`. Imagen de `r`: identidad; 180° (entonces `χ(r)=χ(r³)=−1`, `χ(r²)=3`); o giro de 90° (`χ(r)=χ(r³)=1`, `χ(r²)=−1`). Los tres tienen multiplicidad 1: toda imagen cíclica en `SO(3)` fija un eje. Total 3, todos reducibles. El superviviente fiel es reducible, como dice el informe.
- `D4 = ⟨r,s | r⁴=s²=1, srs=r⁻¹⟩`. Seis caracteres, separados ya por `(χ(r), χ(r²), χ(s), χ(rs))`:
  - trivial: `(3,3,3,3)`;
  - núcleo `⟨r⟩`, imagen `C2`: `(3,3,−1,−1)`;
  - núcleo `⟨r²,s⟩`: `(−1,3,3,−1)`;
  - núcleo `⟨r²,rs⟩`: `(−1,3,−1,3)`;
  - núcleo `⟨r²⟩`, imagen `V4`: `(−1,3,−1,−1)`, multiplicidad 0;
  - fiel, imagen `D4`: `(1,−1,−1,−1)`, multiplicidad 0.
  No hay un séptimo: si `r` va a un orden 4, `s` no puede ir a la identidad, y ningún elemento fuera de `{1}` va a la identidad. Total 6.
- `O ≅ S4`. Normales: 1, `V4`, `A4`, `S4`. Cuatro cocientes y cuatro caracteres forzados por órdenes: trivial; núcleo `A4` e imagen `C2` (pares traza 3, impares traza −1); núcleo el `V4` axial e imagen `S3` de orden 6 (el `V4` a traza 3, los ocho 3-ciclos a traza 0, las seis transposiciones y los seis 4-ciclos a traza −1); fiel, traza 3 solo en la identidad. Total 4.

En cada grupo hay un único carácter con núcleo trivial. El normalizador no funde esos fieles con nadie.

Matiz que el informe no escribe. Esos números cuentan caracteres de un representante concreto, que es lo que pide la equivalencia proyectiva de la sección 2. No son todavía órbitas de la tupla `(G,S,R)`. En `V4` los tres núcleos de orden 2 son tres caracteres distintos, pero `V4` es normal en `O` y `T` preserva el tetraedro y permuta los tres ejes, así que son una sola clase de tupla. Pasan de 5 caracteres a 3 tuplas. No toca a los supervivientes: el fiel es único en los dos censos, y las otras tuplas se vacían igual. En `D4` el normalizador dentro de `O` es el propio `D4` (hay tres Sylow), y los dos núcleos `⟨r²,s⟩` y `⟨r²,rs⟩` no son conjugados dentro de `D4`; el 6 no se funde. En `C4`, `T` y `O` los tipos tienen núcleos de distinta forma y tampoco se funden.

El código no hace `require` de 5, 3, 3, 6 ni 4: los imprime. El «16/16» no los bloquea. El algoritmo que los calcula es, eso sí, el correcto: recorre imágenes de un sistema generador y acepta la asignación solo cuando respeta todos los productos por generadores.

## 3. Lema del núcleo

**Veredicto: correcto, y `emptying_shift` lo implementa.** El informe no transcribe los pares; los dos certificados de abajo son los que el `require` deja cerrados, reconstruidos a mano.

Si `g ∈ ker ρ`, entonces `R_g` es escalar unitario y `T_{gh} = R_g T_h R_g^† = T_h`. `T` es constante en las órbitas de `K`, no solo proyectivamente.

La unitaridad de `U(k) = Σ_h e^{−ik·h} T_h` dice que, para `ℓ ≠ 0`, `Σ T_h^† T_{h+ℓ} = 0`, sumando sobre los `h` con `h` y `h+ℓ` ambos en `N_3`. Si cada par cae dentro de una órbita, cada sumando es `T_h^† T_h`, semidefinido positivo. Una suma de semidefinidos positivos nula obliga a que cada uno sea nulo: la traza es suma de trazas no negativas. Luego esos `T_h` son cero, contra la soporte de ocho coeficientes. Basta un solo par. Vale para cualquier dimensión interna. El código busca exactamente eso: diferencias no nulas de `N_3`, pares con ambos extremos en `N_3`, y exige que todos compartan órbita. `act(I3, ·)` es la identidad; no altera el par.

Dos certificados.

Núcleo el `V4` axial. Órbitas: los dos tetraedros. El giro de 180° en `x` manda `(1,1,1)` a `(1,−1,−1)` y `(−1,1,−1)` a `(−1,−1,1)`; son los cuatro productos +1. El otro tetraedro es la otra órbita. El primer desplazamiento, en orden lexicográfico, que no falla es `(−2,−2,0)`. El anterior, `(−2,−2,−2)`, une `(1,1,1)` con `(−1,−1,−1)`, tetraedros distintos, y se rechaza. Para `(−2,−2,0)` solo hay dos pares:

- `(1,1,1) → (−1,−1,1)`, ambos de producto +1;
- `(1,1,−1) → (−1,−1,−1)`, ambos de producto −1.

Si `A` y `B` son los dos valores, la identidad queda `A^†A + B^†B = 0`, luego `A = B = 0`. Es el tipo `(0,2,2)` del charter, con signos y ejes permutados. El mismo desplazamiento vacía cualquier núcleo que contenga a este `V4`, en particular el `C2` axial, el `T` entero y la clase de `O` con imagen de orden 6.

Núcleo un `C4` de cara. Para la cara `x = +1`, el `C4` es el giro alrededor de `x` y sus órbitas son las dos caras `x = ±1`. Cualquier desplazamiento que vacíe tiene que cumplir `ℓ_x = 0`: si `ℓ_x ≠ 0`, los dos extremos están en caras opuestas, órbitas distintas. El `require` de tangencia es consecuencia de las órbitas, no un ajuste del representante, y da igual cuál de las seis caras elija la iteración del conjunto. El normal `(2,0,0)` no vacía: produce términos cruzados `B^†A`, como dice la corrección del charter. Un desplazamiento que sí vacía es `(0,−2,−2)`, con pares

- `(1,1,1) → (1,−1,−1)`,
- `(−1,1,1) → (−1,−1,−1)`.

Otra vez `A^†A + B^†B = 0`.

El contraste con el control negativo es el mismo grupo geométrico y otro núcleo: si `K = {1}`, las órbitas son puntos y ningún `ℓ ≠ 0` cae dentro de una órbita. `emptying_shift` devuelve `None`. No es un accidente del orden de búsqueda.

## 4. A3 y A8

**Veredicto: correcto.**

El desplazamiento `(2,2,2)` solo admite `h_i = −1` en las tres coordenadas, luego un único par, `((-1,−1,−1),(1,1,1))`. En `s = 1` el coeficiente de Fourier es el escalar `T_{(-1,-1,-1)}^* T_{(1,1,1)} = 0`, así que uno de los dos es cero. No es el mismo modo que el de desplazamiento nulo: el vector físico `(2,2,2)/√3` es un vector no nulo de la red, y `e^{−ik·δ}` no es la función constante. Con ocho coeficientes no nulos la clase `s = 1` está vacía. El argumento no necesita la forma «un Laurent unimodular es un monomio»; la implica para este soporte.

Para cada `h ∈ N_3`, el desplazamiento `2h` fuerza `a = −h` y `b = h` coordenada a coordenada. Un solo par antipodal, y la identidad es `T_{−h}^† T_h = 0`. Con matrices 2×2 no nulas, la imagen de `T_h` cae en el núcleo de `T_{−h}^†`, de dimensión `2 − rango(T_{−h})`. Luego `rango(T_h) + rango(T_{−h}) ≤ 2`. Los dos rangos son al menos 1, luego los dos valen 1. En particular el determinante es 0.

Cayley–Hamilton en 2×2 es `T² − (tr T) T + (det T) I = 0`. Con determinante 0 queda `T² = (tr T) T`, y por inducción `T^n = (tr T)^{n−1} T`. Si la traza no es cero y `T ≠ 0`, ninguna potencia se anula. Si la traza es cero, `T² = 0`. Para estos coeficientes de rango uno, no nilpotente equivale a `tr T_h ≠ 0`. La identidad polinómica sí está comprobada de forma simbólica en el certificado; el paso del rango y el determinante está solo en prosa, y es el que acaba de hacerse.

## 5. Controles

**Veredicto: el negativo es informativo; el positivo tiene el papel correcto, pero su contenido simbólico no se puede recomprobar con estos documentos.**

El negativo comprueba que `(V4, tetraedro)` con núcleo trivial queda fuera de la lista de vaciados, y el `require` exige que aparezca exactamente una vez. Es el contraste justo: el mismo `V4` con núcleo el grupo entero se vacía por `(−2,−2,0)`, y con núcleo trivial no. Cazaría un error que aplicara el lema al grupo en vez de al núcleo, o que declarara vacío todo carácter. No demuestra que la clase de Pauli tenga símbolos unitarios. El informe no dice eso: dice que el lema no la vacía y la manda al paso 4b. Esa lectura es la correcta.

El positivo recorre las dos quiralidades, reindexa el monomio de `published_symbol` y exige las identidades de unitaridad con los ocho `T_h` distintos de cero. El diseño responde al pedido del charter. La extracción está en `S1.WD.published_symbol` y `S1.unitarity_equations`, que no vienen en este paquete. El signo `T2[−v]` tampoco se puede contrastar aquí. Aunque esa inversión estuviera al revés, `h ↦ −h` conserva la unitaridad y el soporte lleno, así que el control seguiría siendo un ejemplo de símbolo unitario con ocho coeficientes; lo que no puedo afirmar es que las matrices sean las de Pavia.

## 6. Alcance

**Veredicto: hay un exceso, la fila de `E`. La clasificación de subgrupos finitos de `SO(3)` y los controles `T2s`/`O2s` no se presentan como más de lo que son.**

La dependencia de la clasificación está declarada en el método, con la marca de no rederivada, y repetida en el alcance. Para los cinco grupos concretos no queda nada condicional: el desglose por órdenes y trazas de la sección 2 cierra los recuentos sin ese teorema. Conviene sustituir la cita por ese desglose; no hace falta retirar ningún número.

Los controles `T2s` y `O2s` están leídos como el charter pide. El informe dice que coinciden, como clases proyectivas, con dos supervivientes, que allí dieron ideales de Gröbner triviales, y a continuación que eran controles, que el charter no permite usarlos, y que aquí son anticipaciones sin verificar. No los convierte en vaciado ni en existencia.

El exceso está en `E`. El certificado no construye la representación `E` de `2O`, no calcula su carácter y no menciona `Q8`. El `require` correspondiente solo comprueba que `emptying_shift` del `V4` axial devuelve un desplazamiento de tipo `(0,2,2)`. Eso demuestra: toda clase cuyo núcleo contiene al `V4` axial se vacía, y en particular la única clase de `O` con núcleo de orden 4 e imagen de orden 6. No demuestra el enunciado A2, que es precisamente que la representación llamada `E` tiene ese núcleo. A7, además, pedía la fila propia de la restricción a `D4`, `E|D4 ≃ 1 ⊕ χ`, y el informe no la separa. El párrafo «What this changes» da por cerrada, con ese argumento, la fila abierta de `E` en el estado del repositorio. El vaciado de la clase de imagen de orden 6 está certificado; el nombre `E` y el cierre de esa fila, no.

El resto del informe no se sale. No habla de `c_0`, del cono estricto, de Q-a ni de Q-b. El techo se afirma solo para los grupos que contienen al `D2` axial, se niega para la cara `C4`, y el transporte de nodos se deja sin examinar. La reducción a cinco supervivientes fieles es lo que el lema da, no una existencia. `A4` se verifica como par geométrico. `A3`, `A5`, `A6` y `A8` tienen el contenido que el certificado comprueba.

## Veredicto global

**No promocionable.** No hay un cálculo falso en los 30 subgrupos, en las tres clases de P, en F, en los recuentos 5, 3, 3, 6 y 4, en el lema ni en A3/A8. La etiqueta `VERIFIED` de A2/A7, y la consecuencia que se saca para la fila de `E`, van más allá del certificado.

## Reparaciones

**G-S0-01. Laguna. Bloquea la promoción.** Informe, tabla de resultados, fila A2/A7; párrafo «What this changes»; texto del `require` que dice «e.g. E of 2O» en el certificado. El script vacía la clase de `O` con núcleo el `V4` axial e imagen de orden 6. No identifica esa clase con la irrep lineal `E` de `2O`, ni escribe `E` restringida a `D4`. Hay que dejar `VERIFIED` solo el vaciado de esa clase y tratar la identificación A2 como heredada, no recomputada, salvo que se añada el carácter o las matrices. Mientras tanto, la fila de `E` no se cierra.

**G-S0-02. Laguna. Bloquea la condición de parada de exhaustividad del Paso 0′, no el resultado.** Informe, sección Method, párrafo del grupo; comentario inicial del certificado. «Todo subgrupo de `S4` es a lo más 2-generado» y «30 es el número conocido» se afirman sin prueba. El cierre por pares es exhaustivo solo con ese lema. Hay que incorporar la distinción por órdenes de la sección 1. El censo no cambia.

**G-S0-03. Redacción. No bloquea.** Informe, fila de representaciones; bucle que imprime `len(reps)` sin `require`. Los cinco recuentos y la lista de supervivientes no están entre las 16 comprobaciones que el informe cuenta. Conviene fijarlos con `require` y decir que son caracteres de un representante fijo: en `(V4, tetraedro)` los tres núcleos de orden 2 son una sola tupla bajo el estabilizador del tetraedro. Los supervivientes fieles no cambian.
