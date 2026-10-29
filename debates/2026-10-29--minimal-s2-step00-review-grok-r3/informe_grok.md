<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 cfeeed0f26d3cd1c4153d32d02bde73c0f981168278059c52d2c0914ae85358a
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T12:46:19Z  fin: 2026-10-29T13:04:30Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step00.md ; último commit observado: ebebca7 ; sha256 de la copia enviada 1c04715d08c427e8d676748db92a2593a2273375a50b939933551931785f44ae
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step00.py ; último commit observado: ebebca7 ; sha256 de la copia enviada adeb8afc4d4be5ed8d692f47727882e688991a36e7e5739a3eeb1bd053bbec5b
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-step00-review-grok-r2/informe_grok.md ; último commit observado: ebebca7 ; sha256 de la copia enviada 1b109a44189d16c36b21fb2fad571ae9f8a9b63088c149689c7ee2e7a2921681
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
entrada_grok.txt sha256 c12dbeb0cdb57c4446cdb67feea3f1d621fd5146a0de0c26d05593d8d6e94aff
respuesta sha256 4caf6c8426726352ab57729d509eb5badc5af5668cd8ad13c2beae19d4e06f7e
-->

La prueba por órdenes cierra, y el certificado usa la traza tridimensional enumerada, no el carácter bidimensional. Las tres objeciones abiertas de la ronda 2 quedan resueltas. No queda objeción obligatoria.

Supuestos de esta ronda: no ejecuté el script; el código se lee como argumento. No están `verify_irreducible_isotropy_step01.py` ni `certificate_utils.py`, así que no recomprobé las matrices de Pavia ni si `assert_sym_equal` incrementa el contador. Los SHA-256, el 23/23 y los 48/48 son declaración del autor. Uso como hechos estándar el teorema de Lagrange, la conjugación de subgrupos de Sylow y que un grupo de orden 6 es `C6` o `S3`. La traza de un giro de ángulo θ en `SO(3)` es `1+2cos θ`: orden 1, 2, 3, 4 da traza 3, −1, 0, 1. Traza 3 solo en la identidad. Conjugación: `στσ^{-1}` sustituye cada entrada por su imagen bajo `σ`.

| Punto de la ronda 2 | Veredicto |
| --- | --- |
| G-S0-02, 2-generación de los subgrupos de `S4` | Resuelto. La prueba escrita es completa y correcta. |
| Traza de `ρ_E` en `D4` y fórmula del orden de `sigma` | Resuelto. Se usa la traza enumerada; la fórmula y `1⊕α⊕α` son correctos. |
| «Single tuple» | Resuelto. Ahora es una órbita de tres tuplas. |
| `Q8` y la fila A2/A7 | Resuelto. `Q8` se declara no calculado en la misma celda. |
| G-S0-01, identificación del núcleo, y G-S0-03, recuentos | No reabiertos. Siguen como en la ronda 2. |

## 1. Prueba por órdenes

La prueba ya no es circular. Por Lagrange los órdenes posibles son 1, 2, 3, 4, 6, 8, 12 y 24, y el texto los reparte todos. Las involuciones de `S4` son las 6 transposiciones y las 3 dobles transposiciones.

**No hay `C2³`.** La clase de las transposiciones tiene 6 elementos, luego `|C((12))| = 24/6 = 4`. Esos cuatro elementos conmutan con `(12)` y son distintos: `{1, (12), (34), (12)(34)}`. Un 2-subgrupo abeliano elemental que contenga una transposición es abeliano, así que cae dentro del centralizador de esa transposición y tiene orden ≤ 4. Uno sin transposiciones solo puede usar la identidad y las tres dobles transposiciones `(12)(34)`, `(13)(24)`, `(14)(23)`. El producto de dos distintas es la tercera, así que ese conjunto es el `V4` normal y tiene orden 4. No hay un quinto elemento. No hay `C2³`.

**Órdenes 1–4.** Cíclicos, o de orden 4 y por tanto `C4` o `C2×C2`. Los dos últimos son 2-generados. `C2³` tiene orden 8 y ya está excluido.

**Orden 6.** No hay elemento de orden 6: los tipos son 1, transposición, doble transposición, 3-ciclo y 4-ciclo. No es `C6`, luego es `S3`. Y `S3` es 2-generado: `(12)(13)(12) = (23)`, así que `⟨(12),(13)⟩` contiene las tres transposiciones. Ser 2-generado pasa al isomorfismo, de modo que vale para cualquier subgrupo de orden 6, no solo para ese de soporte `{1,2,3}`. La frase del texto iguala todos a ese subgrupo concreto; la propiedad que se usa no depende de eso.

**Orden 8.** Un subgrupo de orden 8 es un 2-Sylow. Los 2-Sylow son conjugados, y el conjugado de un grupo 2-generado es 2-generado. Falta solo un testigo diedral dentro de `S4`. El texto da la presentación y no las permutaciones; el testigo es el de esa presentación:

- `r = (1234)`, orden 4; `⟨r⟩ = {1, (1234), (13)(24), (1432)}`.
- `s = (24)`, orden 2, fuera de `⟨r⟩`.
- `srs = (s(1) s(2) s(3) s(4)) = (1432) = r^{-1}`.

Los ocho productos `r^i` y `r^i s` son distintos, así que `|⟨r,s⟩| = 8`. Ese es un 2-Sylow, generado por dos elementos, y todos los demás son conjugados a él. La exclusión de `C2³` no hace falta para este paso.

La alternativa «de los cinco grupos de orden 8 solo `C2³` no es 2-generado» es verdadera y sigue sin demostrarse. No carga la prueba: la carga la lleva el argumento de Sylow.

**Orden 12.** Índice 2 implica normal. Es el único: un subgrupo de índice 2 contiene todo elemento de orden impar, luego los ocho 3-ciclos; esos generan `A4`, y los dos subgrupos tienen orden 12. La generación que el texto afirma se comprueba dentro de `⟨(123),(124)⟩`:

- `(123)(124)(123)^{-1} = (234)`.
- `(132)(124)(132)^{-1} = (314) = (134)`.
- Con los inversos, que son cuadrados, están `(123)`, `(132)`, `(124)`, `(142)`, `(234)`, `(243)`, `(134)`, `(143)`. Son los ocho.

Y `(132)(134)`, aplicado de derecha a izquierda, es `(12)(34)`. Las dobles transposiciones salen igual, así que el subgrupo es `A4`. «Further conjugations» no lista los ocho, pero el primero es correcto y el resto es el mismo cálculo con `(123)^{-1}`.

**Orden 24.** Con `b = (1234)` y `a = (12)`: `bab^{-1} = (23)` y `b(23)b^{-1} = (34)`. Luego `(23)(12)(23) = (13)`, `(34)(13)(34) = (14)` y `(34)(23)(34) = (24)`. Las seis transposiciones generan `S4`, luego `S4 = ⟨(12),(1234)⟩`.

**Monoide.** `closure` multiplica a la derecha por los generadores, así que construye el monoide. En un grupo finito, si `g^n = 1` entonces `g^{-1} = g^{n-1}`, y eso vale para cualquier palabra, no solo para los generadores. El monoide es un subgrupo. Recorrer `O×O` incluye `(g,g)` y `(g,1)`, así que salen también los cíclicos. Como todo subgrupo es 2-generado, salen todos. El `require` de 30 subgrupos sigue siendo contraste, no prueba, y el texto lo dice.

El censo `1+9+4+4+3+4+3+1+1` (trivial, nueve de orden 2, cuatro `C3`, cuatro `C2×C2`, tres `C4`, cuatro `S3`, tres `D4`, `A4`, `S4`) suma 30 y no contiene un `C2³`. Cuadra con la prueba; no la sustituye.

## 2. Traza de `ρ_E` y orden de `sigma`

El certificado ya no suma «puntos fijos − 1». `rhoE` es el homomorfismo de la enumeración cuyo núcleo es el `V4` axial:

```python
rhoE = [phi for phi in reps_O if frozenset(g for g in O if phi[g] == I3) == V4][0]
```

`reps_O` sale de `homs_into_O`, y `trace(rhoE[g])` es la traza de una matriz de `O ⊂ SO(3)`. Esa traza se compara, para todo `g ∈ O`, con la tabla `{1: 3, 2: -1, 3: 0}`, y la suma sobre `D4` usa esas mismas trazas. Las dos comprobaciones piden lo que la ronda 2 pedía.

La fórmula del orden es correcta en `S3`. `sigma(M)` es la permutación de ejes, y la imagen tiene 6 elementos. En tres letras: la identidad es `(0,1,2)`; un elemento sin puntos fijos es un 3-ciclo; cualquier otro no identidad fija un punto y es una transposición. No hay doble transposición. Los seis casos caen bien: `(0,1,2)` orden 1; `(1,0,2)`, `(2,1,0)`, `(0,2,1)` orden 2; `(1,2,0)`, `(2,0,1)` orden 3. La identidad se descarta antes del test de derivación, así que no se le asigna orden 3. El orden de `sigma(g)` y el de `sigma(g)^{-1}` coinciden, de modo que el antihomomorfismo no cambia la tabla.

Por qué la igualdad de trazas es identidad, no un accidente del `require`. `sigma` y `rhoE` tienen ambos núcleo el `V4` axial, así que el orden de `sigma(g)`, el orden de `gV4` en `O/V4 ≅ S3` y el orden de la matriz `rhoE(g)` son el mismo. Un giro de ese orden tiene traza 3, −1 o 0. Cualquier automorfismo de `S3` conserva órdenes, así que no hay otro carácter.

En `D4` el cociente por el `V4` axial tiene orden 2, porque `|D4| = 8` y `|V4| = 4`, y el `V4` axial es normal en `O`, luego está en todos los 2-Sylow. La imagen en `S3` tiene orden 2: no hay 3-ciclos. Cuatro elementos van a la identidad y cuatro a una transposición.

| Cosete | Número | `tr ρ_E` |
| --- | --- | --- |
| `V4` | 4 | 3 |
| fuera | 4 | −1 |

Suma `12 + (−4) = 8`. Multiplicidad trivial `8/8 = 1`. Con `α` el signo de `D4/V4` (`α = 1` en el `V4`, `α = −1` fuera),

`⟨χ, α⟩ = (1/8)(4·3·1 + 4·(−1)·(−1)) = 16/8 = 2`.

Luego `χ = 1+2α`, que es el carácter de `1⊕α⊕α`. El `require` de la suma no deja otro reparto: sobre el `V4` la traza ya es 3, y cuatro valores en `{−1, 0}` solo suman −4 si los cuatro valen −1. El rótulo `1⊕α⊕α` no excede al certificado.

El carácter bidimensional sigue siendo otra función. En el `V4` vale 2, no 3; fuera de él, en este `D4`, vale 0, no −1. Las sumas coinciden (`8 = 8`) y las funciones no. En un `C3` las multiplicidades son `(2−1−1)/3 = 0` y `(3+0+0)/3 = 1`. El inciso del informe sobre `C3` es correcto, y se refiere a las sumas.

## 3. Órbita, `Q8` y la fila A2/A7

Las tres correcciones de redacción son correctas y bastan.

Los tres caracteres de `V4` con núcleo de orden 2 son tres caracteres del representante fijo. `(123)` los funde: `(12)(34) ↦ (23)(14) = (14)(23)`, y `(14)(23) ↦ (24)(31) = (13)(24)`. Son tres núcleos y una sola órbita bajo `T ≅ A4`, que fija el tetraedro y normaliza al `V4`. El texto dice ahora «a single orbit (of three tuples)». El recuento 5 sigue siendo de caracteres, no de órbitas de tuplas. Las dos frases conviven y no se contradicen. Los supervivientes no se mueven: el fiel no entra en esa órbita.

La celda A2/A7 dice en la misma frase que la preimagen `Q8` de `V4` en `2O` no se calcula. El `VERIFIED` queda limitado a lo que el certificado hace sobre `O`: núcleo proyectivo el `V4` axial, única clase de `O` con ese núcleo, restricción a `D4` igual a `1⊕α⊕α` y vaciada porque el núcleo contiene al `V4` axial. Eso es A7 y la mitad de A2 que vive en `O`. La mitad `Q8` del enunciado A2 del charter queda fuera, dicha en la celda y no solo en un comentario del código.

## 4. Errores nuevos

No veo ningún error matemático nuevo, ni una afirmación de vacío, de recuento o de descomposición que el argumento no cubra.

Hay un resto de redacción, de gravedad baja, en Provenance, al final del párrafo de la segunda reparación. La frase del barrido completo aparece dos veces, con ficheros distintos: `2026-10-29--minimal-s2-step00-repair2-run_all.tsv` y `2026-10-29--minimal-s2-step00-repair-run_all.tsv`. La segunda es el registro de la reparación anterior. No toca la prueba. No recompuse ninguno de los dos.

Sigue en el mismo estado que dejó la ronda 2, y no lo reabro: «enumerar homomorfismos hacia `O` es exhaustivo» porque cada imagen de esos tipos es conjugada a un subgrupo de `O`. Es verdadero para cocientes de subgrupos de `S4` (ninguno tiene orden divisible por 5 ni por 60) y el desglose por caracteres sigue estando en la ronda 2, no reescrito aquí. Los números 5, 3, 3, 6 y 4 están exigidos por el certificado y el desglose de aquella ronda no cambia.

## Veredicto global

**Sin objeción obligatoria abierta.** El bloqueo de la ronda 2 queda levantado: la 2-generación está probada por órdenes, y la comprobación sobre `D4` suma la traza de `ρ_E: O → SO(3)` tomada de la enumeración. No ejecuté el certificado, así que el 23/23 y el SHA-256 `adeb8afc4d4be5ed…` siguen siendo una declaración del autor, no una comprobación de esta ronda.
