<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 cb818a0acfc0675274a5d2356879ecd678c8d48ffe4c91a7a71042979dbf0222
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T12:02:21Z  fin: 2026-10-29T12:18:13Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step00.md ; último commit observado: 3bcf7b6 ; sha256 de la copia enviada 3f1b9e4bdc3b0fad1934b07b225627146c2ae143c07149e4dfcbd231faec49d3
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step00.py ; último commit observado: 3bcf7b6 ; sha256 de la copia enviada a2abbe32a98ac005f3cc8c90bdc1aac37a97b436d41559cea942c719f253b4d7
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-step00-review-grok/informe_grok.md ; último commit observado: 3bcf7b6 ; sha256 de la copia enviada f0118b7103347901104f284732bc04e3c81ad88d1a591b465f17c82a84a686a2
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
entrada_grok.txt sha256 70efcaff2c6dad94fe36d10a2bbde67df89fe94e9b261e47194a07bff723ae3d
respuesta sha256 51afffef28741b5aaae6fbd14a56246d8ea7dedcead5aa48cedfa5489999a471
-->

La identificación de la clase vaciada con `E` queda hecha y no la estropea que `sigma` sea antihomomorfismo. La prueba de 2-generación, tal como está escrita, no es completa. Los `require` de 5/3/3/6/4 y de los cinco supervivientes son correctos, y son caracteres de un representante fijo.

Supuestos: no ejecuté el script; el código se lee como argumento. No está `verify_irreducible_isotropy_step01.py`, así que no recomprobé las matrices de Pavia. La traza de una rotación de ángulo θ en `SO(3)` es `1+2cos θ`. Una involución de `SO(3)` es la identidad (traza 3) o un giro de 180° (traza −1). En dimensión 3, traza 3 ocurre solo en la identidad.

| Ítem | Veredicto |
| --- | --- |
| G-S0-01 | Reparado en lo que bloqueaba: la clase de `O` con núcleo el `V4` axial es la de `E`, y es la vaciada. El antihomomorfismo no cambia núcleo, imagen ni puntos fijos. «Puntos fijos − 1» es el carácter de la irrep 2-dimensional, no el de `ρ: O → SO(3)`. En `D4` las dos multiplicidades valen 1; no son la misma función. |
| G-S0-02 | Los enunciados son verdaderos. La prueba escrita no es completa: la exclusión de `C2³` es circular y el caso de orden 8 no se prueba. |
| G-S0-03 | Correcto. Los `require` fijan 5, 3, 3, 6, 4 y exactamente esos cinco supervivientes. La nota de caracteres, no de órbitas de tuplas, es correcta. |

## 1. G-S0-01

Basta con el núcleo. `E`, la irrep lineal 2-dimensional de `O ≅ S4`, factoriza por `O/V4 ≅ S3` y el núcleo proyectivo es exactamente el `V4` axial: en `S3` el carácter de la irrep estándar vale 2, 0 y −1 en la identidad, las transposiciones y los 3-ciclos, y solo la identidad es escalar. El certificado hace eso por álgebra lineal, no por el carácter. Con la base `u1=(1,−1,0)`, `u2=(0,1,−1)` del plano de suma cero, `P` actúa por la permutación de ejes y se comprueba si `Puk = λ uk` para el mismo `λ ∈ {±1}`. Eso es `±I` en el plano. Como `P` conserva el plano, el criterio es necesario y suficiente. Solo la permutación identidad lo cumple: `−I` en el plano exigiría carácter de permutación `−1`, imposible. Por tanto `ker E = {M : sigma(M) = id}`.

Ese conjunto es el `V4` axial. `sigma(M)[i]` es la columna no nula de la fila `i`, así que `sigma(M) = (0,1,2)` significa matriz diagonal. Dentro de `O` (determinante 1) eso es `{I, diag(1,−1,−1), diag(−1,1,−1), diag(−1,−1,1)}`. El `require` lo iguala al `V4` del código y comprueba que la imagen tiene 6 elementos. Orden: `|O|/4 = 6`.

La identidad de antihomomorfismo es correcta y el código la recorre. Si `k = sigma(A)[i]` es el único índice con `A[i][k] ≠ 0`, el único `j` con `(AB)[i][j] ≠ 0` es `j = sigma(B)[k]`. Luego `sigma(AB) = sigma(B) ∘ sigma(A)`. No afecta a la identificación:

- `sigma(M) = id` si y solo si `sigma(M)^{−1} = id`, mismo núcleo;
- invertir recorre todo `S3`, misma imagen;
- una permutación y su inversa tienen los mismos puntos fijos;
- `π(sigma(M))` es escalar si y solo si `π(sigma(M)^{−1})` lo es.

`g ↦ π(sigma(g)^{−1})` es el homomorfismo; el código lo dice. El informe dice solo «composed with». Para el núcleo da igual.

Hay una sola clase de `O` con ese núcleo, y el carácter tridimensional queda forzado, así que es la de `E`. Los normales de `S4` son `1`, el `V4` de las dobles transposiciones, `A4` y `S4`. Un núcleo de orden 4 tiene que ser ese `V4`, no un `V4` no normal. Traza según el orden: 3, −1, 0, 1 para órdenes 1, 2, 3, 4. Con núcleo exactamente el `V4`:

- los cuatro elementos del `V4` van a la identidad, traza 3;
- un 3-ciclo no puede ir a la identidad ni a un orden 2, luego traza 0 (hay 8);
- una transposición, orden 2 y fuera del núcleo, traza −1;
- un 4-ciclo cumple `ρ(g)² = ρ(g²) = I` porque `g²` es una doble transposición, y `ρ(g) ≠ I`, luego orden 2 y traza −1 (6+6 = 12).

Ese es el carácter de la clase de imagen de orden 6. El `require` de unicidad mira los núcleos de los cuatro caracteres de `O` y exige que solo uno sea el `V4` axial. El vaciado es el de `emptying_shift(V4)`, ya comprobado: cualquier núcleo que contenga a ese `V4` hereda el desplazamiento. Con esto la fila de `E` en `O` queda identificada con la clase vaciada.

La fórmula del carácter no es la traza de `ρ`. El código pone

`chiE(M) = #{i : sigma(M)[i] = i} − 1`

y suma eso sobre `D4`. Es el carácter de la irrep 2-dimensional: `χ_perm − 1`. En la identidad vale 2, no 3. No es una traza de `SO(3)` salvo en la identidad del grupo: un giro no trivial tiene traza 3, −1, 0 o 1, nunca 2.

En el `D4` geométrico generado por `r: (x,y,z) ↦ (−y, x, z)` y `s: (x,y,z) ↦ (x, −y, −z)`, el cociente `D4/V4` tiene orden 2. Cuatro elementos caen en el `V4` y cuatro fuera.

| Elementos | `χ` 2-dimensional | traza de `ρ_E` |
| --- | --- | --- |
| 4 del `V4` | 2 | 3 |
| 4 de fuera | 0 | −1 |
| Suma | 8 | 8 |
| Multiplicidad | 1 | 1 |

El `require` `triv_mult == 1` pasa, y la multiplicidad trivial de `ρ_E` restringida a `D4` es realmente 1. No es lo que la suma calcula. Para `r` concreto, `sigma(r) = (1,0,2)`, un punto fijo, así que la fórmula da 0; la traza de la matriz es 1; la traza de `ρ_E(r)` es −1, porque la imagen en `S3` es una transposición y el giro correspondiente es de 180°. Tres valores distintos.

El acuerdo es particular de este subgrupo. En un `C3 = ⟨3-ciclo⟩` la irrep 2-dimensional tiene carácter `2, −1, −1`, multiplicidad `(2−1−1)/3 = 0`. El `ρ_E` manda el generador a un giro de 120°, carácter `3, 0, 0`, multiplicidad `3/3 = 1`. La misma fórmula ya no es la multiplicidad de `ρ`.

`ρ_E` restringida a `D4` es `1 ⊕ α ⊕ α`, con `α` el signo de `D4/V4`: traza `3` en el `V4` y `−1` fuera, de modo que al restar la trivial queda `2α`. Se puede escribir `1 ⊕ χ` con `χ = α ⊕ α`. La irrep 2-dimensional restringida es `1 ⊕ α`. Las dos lecturas de «`1 ⊕ χ`» son verdaderas y tienen multiplicidad trivial 1. El certificado prueba la segunda. El vaciado de la restricción no usa esa suma: usa `V4 ≤ D4` y `emptying_shift(V4)`.

`Q8` no se toca. El enunciado A2 del charter dice que en `2O` el núcleo es la preimagen `Q8`. El certificado no construye el recubrimiento doble. La celda de la tabla no afirma `Q8`; el rótulo «A2 verificado» es más ancho que el cálculo. El vaciado no depende de esa frase.

## 2. G-S0-02

La distinción por órdenes es el argumento correcto, y cada igualdad que se afirma es verdadera. Como prueba, el texto no cierra.

Faltan los órdenes. Por Lagrange, un subgrupo de `S4` tiene orden 1, 2, 3, 4, 6, 8, 12 o 24. El informe no lo dice; el reparto de casos sí los cubre todos. El código cierra pares ordenados de `O`, incluidos `(a,a)`. En un grupo finito el monoide generado es el subgrupo, porque `g^{−1} = g^{n−1}` si `g^n = 1`. Eso tampoco está escrito y hace falta para que `closure` sea exhaustivo.

Órdenes 1 a 4. Cíclico o `C2×C2`, ambos generados por a lo más dos elementos. Correcto. La frase que excluye `C2³` no es una prueba: «no hay `C2³` porque un 2-subgrupo abeliano elemental máximo tiene orden 4» repite el enunciado.

La exclusión sí sale por involuciones. Las involuciones de `S4` son transposiciones y dobles transposiciones. La clase de las transposiciones tiene 6 elementos, luego el centralizador de `(12)` tiene orden `24/6 = 4` y es `{1, (12), (34), (12)(34)}`. Cualquier 2-subgrupo abeliano elemental que contenga una transposición tiene orden ≤ 4. Si no contiene ninguna, solo quedan las tres dobles transposiciones, y junto con la identidad forman el `V4` normal, orden 4. No hay un quinto elemento. Por tanto no hay `C2³`.

Orden 6. No hay elemento de orden 6: los tipos de ciclo son 1, transposición (orden 2), doble transposición (orden 2), 3-ciclo (orden 3) y 4-ciclo (orden 4). Un grupo de orden 6 es `C6` o `S3`. Sin elemento de orden 6 es `S3`, y `S3 = ⟨(12),(13)⟩` porque `(12)(13)(12) = (23)`. El paso es correcto; el informe no escribe los tipos de ciclo ni por qué solo hay dos grupos de orden 6.

Orden 8. «Todo grupo de orden 8 salvo `C2³` es 2-generado» es verdadero y no está probado. Los cinco grupos son `C8 = ⟨x⟩`, `C4×C2 = ⟨(a,0),(0,b)⟩`, `D4 = ⟨r,s⟩`, `Q8 = ⟨i,j⟩` y `C2³`, el único que necesita tres generadores. Sin esa lista, o sin el argumento de Frattini (`d(G) ≥ 3` y `|G| = 8` fuerzan `G ≅ C2³`), la frase no prueba nada. Encadenada con la exclusión circular de `C2³`, el caso de orden 8 queda sin justificación. Hay un atajo que el informe tampoco da: todo subgrupo de orden 8 es un 2-Sylow, los tres son conjugados y uno es el diedral `⟨r, s⟩`.

Orden 12. Índice 2 implica normal, y el único subgrupo de índice 2 es el núcleo del signo, `A4`. Hasta ahí, bien, aunque la unicidad no se escribe. «Luego `A4 = ⟨(123),(124)⟩`» no se sigue del índice: la generación es otra afirmación, y no se demuestra. El cálculo que falta: conjugando, `(123)(124)(123)^{−1} = (234)`. Conjugando otra vez se obtienen `(243)`, `(134)`, `(142)` y `(143)`. Con los inversos están los ocho 3-ciclos, y generan `A4`.

Orden 24. `S4 = ⟨(12),(1234)⟩` es verdadero y no se deduce en el texto. Con `b = (1234)` y `a = (12)`, `bab^{−1} = (23)`, `b(23)b^{−1} = (34)`, y `(12),(23),(34)` generan `S4`.

El `require` de 30 subgrupos sigue siendo un contraste, no una prueba. El censo `1+9+4+4+3+4+3+1+1` cuadra con lo de arriba y no tapa el hueco.

## 3. G-S0-03

Los dos `require` fijan lo que la ronda 1 solo veía impreso. Las claves salen de las tres clases de P y las dos de F, y no colisionan. Recuento a mano, por caracteres del representante, no por ejecutar el bucle.

`V4 = {1,a,b,c}`. El núcleo es un subgrupo y la traza de cada no identidad es 3 o −1. Cinco caracteres: el trivial `(3,3,3,3)`; tres de núcleo de orden 2, según cuál elemento conserve traza 3; el fiel `(3,−1,−1,−1)`, multiplicidad `(3−1−1−1)/4 = 0`. El superviviente es ese fiel, irreducible.

`T ≅ A4`. Normales: `1`, `V4`, `A4`. Tres cocientes y tres caracteres: trivial; núcleo `V4` e imagen `C3` (los cuatro del `V4` a traza 3, los ocho 3-ciclos a traza 0); fiel (los tres orden 2 a traza −1, los orden 3 a traza 0), multiplicidad 0. Superviviente: fiel, irreducible, imagen de orden 12.

`C4 = ⟨r⟩`. La imagen de `r` es la identidad, un 180° o un 90°. Tres caracteres, y los tres fijan un eje: multiplicidades 3, 1 y 1. El fiel es el de 90°, `|ker| = 1`, `|imagen| = 4`, reducible. Es el tercer superviviente del `require`.

`D4 = ⟨r,s | r⁴ = s² = 1, srs^{−1} = r^{−1}⟩`. Seis caracteres, ya separados por `(χ(r), χ(r²), χ(s), χ(rs))`:

- trivial, `(3,3,3,3)`;
- núcleo `⟨r⟩`, imagen `C2`, `(3,3,−1,−1)`;
- núcleo `⟨r²,s⟩`, `(−1,3,3,−1)`;
- núcleo `⟨r²,rs⟩`, `(−1,3,−1,3)`;
- núcleo `⟨r²⟩`, imagen `V4`, `(−1,3,−1,−1)`;
- fiel, imagen `D4`, `(1,−1,−1,−1)`, multiplicidad 0.

No hay un séptimo: si `r` va a un orden 4, `s` no puede ir a la identidad, porque tiene que invertir `r` por conjugación, y toda involución no trivial de `SO(3)` tiene traza −1. El único de núcleo trivial es el fiel. Los otros cinco tienen un desplazamiento que los vacía. Para el núcleo no axial `{1, r², rs, r³s}`, con `rs: (x,y,z) ↦ (y, x, −z)`, las órbitas sobre `N3` tienen tamaño 4 y el desplazamiento `(2,2,0)` mete sus dos pares dentro de órbitas: `(−1,−1,1) → (1,1,1)` y `(−1,−1,−1) → (1,1,−1)`. El superviviente de `D4` es solo el fiel, irreducible, imagen de orden 8.

`O`. Cuatro normales, cuatro caracteres forzados por órdenes: trivial; núcleo `A4` e imagen `C2`; núcleo el `V4` e imagen de orden 6; fiel, traza 3 solo en la identidad, multiplicidad 0. Imagen fiel de orden 24. Los tres de núcleo no trivial contienen al `V4` axial o son transitivos, y el lema los vacía.

Eso es exactamente la lista del segundo `require`: un superviviente por grupo, núcleo proyectivo trivial, y reducible solo el `C4` de la cara.

La nota es correcta. `len(reps)` cuenta tuplas de trazas de un `G` fijo. No son órbitas de `(G,S,R)`. En `(V4, tetraedro)` los tres núcleos de orden 2 son tres caracteres, y `T` los funde en una sola órbita: `(123)` conjuga `(12)(34)` a `(14)(23)` y esta a `(13)(24)`. El fiel no se funde con nadie. Los supervivientes no cambian. «A single tuple» en el informe sobra una palabra: es una órbita de tres tuplas, no una tupla.

## 4. Errores nuevos, y lo que no excede

El párrafo de `SO(3)` no reintroduce la clasificación general como hipótesis del recuento. La lista de trazas por orden es correcta, y un cociente de un subgrupo de `S4` no puede tener orden divisible por 5 ni por 60. La frase «enumerar homomorfismos hacia `O` es exhaustivo» sigue apoyada en que cada imagen de esos tipos es conjugada dentro de `O`. Eso es verdad y sigue sin demostrarse en el informe; no es una afirmación falsa, y es la misma hipótesis que ya usaba el resto de la enumeración. Citar el desglose de la ronda 1 no sustituye a tenerlo escrito, pero no altera los números: ahora están exigidos por el certificado.

Errores nuevos:

1. Carácter de `E` en la restricción a `D4`. Certificado, asignación `chiE` y el `require` «G-S0-01 / A7»; informe, fila A2/A7, «`1 ⊕ χ`». Gravedad media. No borra la identificación ni el vaciado. La función sumada es `χ(E_2) = puntos fijos − 1`. La traza de `ρ_E` es otra: en `r` valen 0 y −1, como arriba. En `D4` las sumas coinciden (8 y 8) porque las diferencias `+1` en el `V4` y `−1` fuera se cancelan. En un `C3` dan multiplicidades 0 y 1. El `require` no calcula la multiplicidad de la clase tridimensional.

2. «Form a single tuple». Informe, fila de representaciones. Gravedad baja. Son tres caracteres y una órbita bajo `T`. El `require` no hereda esa frase: cuenta 5 caracteres.

3. El rótulo A2 incluye, en el charter, la preimagen `Q8` en `2O`. Informe, fila A2/A7. Gravedad baja. No está calculada. La celda misma solo afirma lo que el certificado hace sobre `O`.

No veo otro exceso. El lema del núcleo, A3 y A8 no cambian, y al releerlos el desplazamiento `(2,2,2)` sigue teniendo el único par `((−1,−1,−1),(1,1,1))`, cada `2h` el único par `(−h,h)`, y Cayley–Hamilton en 2×2 es la identidad que el certificado pide. `T2s` y `O2s` siguen marcados como anticipación no verificada. El techo se afirma solo donde el grupo contiene al `V4` axial y se niega en la cara. El control positivo de Pavia sigue fuera de estos documentos.

## Veredicto global

**No promocionable.** La clase vaciada de imagen de orden 6 es la de `E`, los recuentos 5/3/3/6/4 y los cinco fieles están fijados, y el antihomomorfismo no abre otro núcleo. La condición de parada del Paso 0′ pide una prueba escrita de exhaustividad, y la de 2-generación sigue sin probar que no hay `C2³` ni que todo grupo de orden 8 distinto de `C2³` es 2-generado. A eso se añade que el test de «`1 ⊕ χ`» suma el carácter 2-dimensional, no la traza de `ρ`.
