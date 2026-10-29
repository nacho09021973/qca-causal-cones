<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 b6b718c6230917396beea9eb60ee05a6e2ea1a9c773b162f2e3606db9013fb11
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-29T17:44:24Z  fin: 2026-10-29T17:57:15Z
documento: /home/ignac/qca-causal-cones/theory/S3_ISOTROPIC_RIGIDITY_GATE.md ; último commit observado: 2308e75 ; sha256 de la copia enviada c65cba87d4847358a12d981aa526acd2d6309f13508381419c147bf6ae247146
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--s3-charter-draft-review-grok/informe_grok.md ; último commit observado: 2308e75 ; sha256 de la copia enviada ce40f40548a005f4394e1a388995873c1bdca06b0464ca209d4d9e7d0f6c7a49
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--s3-charter-draft-review-grok/verificacion_autor.md ; último commit observado: 2308e75 ; sha256 de la copia enviada 96eb0f00a541a013c35a92d43dd61ddc362c85b5cce0d327ec336d33adac04d0
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step4b1.py ; último commit observado: 4646be5 ; sha256 de la copia enviada 5b0122f11df6f88d01cea7c88a45a07680606c8b78fbd4df2146dab08dfe0b33
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/theory/STRICT_CONE_CEILING_N3_GATE.md ; último commit observado: 4135625 ; sha256 de la copia enviada aadaafb37d3e311fba39028699815f818322b02f9163661d1f96f30671b97827
documento: /home/ignac/qca-causal-cones/state/CURRENT_STATE.md ; último commit observado: ea3f401 ; sha256 de la copia enviada bcc1bbf8eccf483d252d10fdae8c02076254015bcf15122f1dee0748c4f11884
entrada_grok.txt sha256 f8895634561ab9b952a9b9b77f370425bf76c8a9d46573be9678427ea2f9aa05
respuesta sha256 eee77962ca671d40a1845e496b6b603d76a5043273708de09643884cd586d5a7
-->

**Veredicto: NOT_READY.** No se congela. El rechazo de G-S3-06 es correcto y el lema de paridad está bien enunciado; lo que impide congelar es que la tabla de la unión no parte los casos y que el punto 3 del certificado admite una lectura falsa.

Supuestos de esta ronda. No ejecuté el script del Documento 4: el soporte del testigo sale de la identidad algebraica de abajo y de leer `witness_symbol` y `laurent_unitary`. No rehíce los multiplicadores de Schur, ni la prueba de A3, ni los hashes `014753e`, `ea3f401` y `5424771`. A3 se toma como el hecho general ya marcado VERIFIED en el Documento 7 («un polinomio de Laurent unimodular en el toro es un monomio»), no como el corolario de `s=1`. Los vértices de `N3` en ese script son etiquetas de `{±1}^3`: las claves de los proyectores son `±1` y el código indexa `h[i]`. `V4 ≤ T, D4, O` y los ejes ternarios de `T` y `O` se usan como en el charter `s=2` ya congelado. La ecuación (2) es el predicado que glosa el Documento 5. El Documento 3 no es evidencia.

## Reparaciones

| Id | Estado | Qué queda |
| --- | --- | --- |
| G-S3-01 | Resuelta | B5 ya no es una reducción de variables. El vacío, si el certificado cierra, es el desenlace y cae en el paso 0. |
| G-S3-02 | Resuelta | Hay una codificación por rango y no se usan las identidades de traza de 4b-2. Objeción nueva sobre el espectador y la palabra «pendiente». |
| G-S3-03 | Resuelta | Equivalencia proyectiva, producto por un carácter, colisiones escritas, `C4` sin antiunitarias, cuentas de la etapa (a) no reutilizadas. |
| G-S3-04 | Resuelta | B4 dice que no vacía la clase; el paso 0″ lo trata como restricción, no como cierre. |
| G-S3-05 | Resuelta | Un vacío de P y F ya no se lee como «la dimensión no rígida mínima es 4». `s=2` está como ESTABLISHED en el Documento 7, no como PRELIMINARY. |
| G-S3-06 | Rechazo correcto | El cargo de la ronda 1 era falso. El control de v2, aun así, es el adecuado. |
| G-S3-07 | Resuelta | Techo por tupla, transporte de nodo, salvedad de `C4`, conflicto antes que cualquier otro desenlace. |
| G-S3-08 | Parcial | Están el cierre en el paso 0, la casilla sin sector y la mezcla vacío/rigidez. La tabla no es una partición. |
| G-S3-09 | Resuelta | El Documento 7 promociona T3/O3/O4 a ESTABLISHED tras Gemini y Grok. v2 no sube el estado por su cuenta y deja la cabecera del otro charter como PRELIMINARY. |
| G-S3-10 | Resuelta | Q-a3 con `D_𝒞`, paso 2 sobre todo el conjunto real, literatura solo para novedad y «clasificación», exponente de la clase, traza no heredada en rango 2. |

## 1. G-S3-06

El rechazo se sostiene. Cada factor solo tiene frecuencias `±1`, y el producto tiene soporte exactamente en `{±1}^3`.

La identidad, con `P_j^{(±1)} = (I ± σ_j)/2`, es

\[
e^{-iq\sigma_j}=\cos q\,I-i\sin q\,\sigma_j=e^{-iq}P_j^{(+1)}+e^{iq}P_j^{(-1)}.
\]

`cos q` y `sin q` no aportan modo cero: su media en el toro es cero. El producto de los tres factores es

\[
\sum_{\varepsilon\in\{\pm1\}^3}e^{-i(q_x\varepsilon_x+q_y\varepsilon_y+q_z\varepsilon_z)}\,P_x^{(\varepsilon_x)}P_y^{(\varepsilon_y)}P_z^{(\varepsilon_z)}.
\]

Son ocho modos, no los 27 de `{-1,0,1}^3`. Una cancelación puede borrar alguno de esos ocho; no puede crear un noveno. El término on-site sería la frecuencia `(0,0,0)`, que no está.

Ese error de la ronda 1 venía de leer la serie de Taylor `I - iqσ + …` como si el `I` fuera un modo de Fourier. No lo es.

El Documento 4 construye precisamente esos ocho coeficientes (`T_(x,y,z) = P_x^x P_y^y P_z^z` sobre `N3`) y comprueba que ninguno es nulo, que las identidades de Laurent `U^†U = I` y `UU^† = I` cierran para todo desplazamiento `h'-h` con `h,h'∈N3`, y que el símbolo es covariante. No hace falta ejecutar el script para el soporte: la fórmula ya lo da, y el script no añade modos fuera de `N3`.

En estas unidades, `{±1}^3` es la etiqueta `ε` de `N_3`. El testigo está en la geometría congelada. Según el Documento 7 es la quiralidad de Pavia `−1`; la quiralidad `+1` aparece en el mismo script como control secundario (`require(ch == 1)`), no como otro soporte. No rederivé el signo de la quiralidad: no está en los adjuntos y no afecta al soporte.

Sustituir el control positivo por los símbolos de Pavia no contradice el rechazo: es el mismo objeto, y `det = 1` en el producto de exponenciales porque cada Pauli tiene traza cero.

## 2. Lema de paridad

B5 está bien enunciado. Cada sumando de `det U` es un producto de tres entradas, luego una frecuencia `ε¹+ε²+ε³` con `ε^j∈{±1}^3`. Cada coordenada es suma de tres impares, así que vale `±1` o `±3`, nunca `0`. El modo cero no está en el soporte, idénticamente, con o sin cancelaciones y con o sin covarianza. `|det U|=1` y A3 dejan un solo monomio; la covarianza, también si `R` es proyectiva, da `det U(gk)=det U(k)` porque `det(RUR^†)=det U` para `R` unitaria. De ahí `g^T m=m` para todo `g∈G`: dos vectores de red distintos definen caracteres distintos en el toro, así que no hay cociente por un periodo no nulo.

El único vector fijo por todo `V4` es `0`, que no está en el coseto impar. `T`, `D4` y `O` contienen esa `V4`. El `C4` de cara solo fija su eje, y todo vector axial tiene dos coordenadas nulas. Ninguna frecuencia del determinante es invariante. Si el certificado cierra, las cinco clases son `EMPTY_CLASS` para toda `R` proyectiva unitaria. El argumento usa `s` impar y la ausencia de término on-site; las dos cosas están en la geometría congelada.

El plan 1–5 es suficiente para esa prueba, leído con la prosa de B5. El punto 1 (expansión genérica y paridad) da el modo cero idénticamente nulo. El punto 2 reutiliza el hecho general de A3, no el vacío de `s=1`. El punto 3 tiene que ser el de los invariantes comunes del grupo entero. Los puntos 4 y 5 no sustituyen a 1–3; comprueban que el método no dispara en las dimensiones donde hay símbolos.

Los controles apuntan bien. El negativo: en `s=2` y `s=4` la misma cuenta no prohíbe la frecuencia cero (suma de un número par de impares), y un símbolo unitario en `N_3` sin término on-site existe en ambas, según el Documento 7. Si el script dijera que el modo cero falta también ahí, el script estaría mal. El positivo: los Pavia de `s=2` cumplen `det U` constante. En el producto de exponenciales eso es `det U=1`. Si el certificado devolviera un monomio no constante, o el símbolo no es el certificado o se está aplicando mal A3. Llamar «negativo» al caso en que la obstrucción no debe disparar es coherente.

La lectura que no vale está en el punto 3 de la sección 3: «los vectores fijos de `g^T`». Un giro de orden 3 de `T` o de `O` fija la diagonal `(1,1,1)`, y `(1,1,1)` es impar y es suma de tres vértices. Eso no salva a la clase: `(1,1,1)` no es fijo por todo el grupo, porque `V4` no lo fija. Un certificado elemento a elemento refutaría B5 en falso y abriría los pasos 1 y 2 sin objeto. Tiene que calcular el intersección de los espacios fijos.

## 3. Sectores y conflicto

Las dos codificaciones son las del techo, no las de 4b-2.

Para `r=2`, un autovalor aislado de multiplicidad 2 y las dos ramas de la compresión a la imagen de `P` iguales a `±c_0` en toda dirección, sin tilt, es la fila «Selected cone»: en rango 2, «incluir `+c_0` y `-c_0`» obliga a que esas sean las dos ramas. El espectador queda fuera de `P` porque su autovalor en el nodo es distinto. Para `r=3`, `U(k_⋆)=aI` es forzoso, y «incluir `±c_0`» más una tercera pendiente registrada y no contada como cono es «Selected cone» junto con «Other slopes». Puede ser nula. No usar `tr H_j=0` ni `½ tr(H_j H_l)=c_0^2 δ_{jl}` es correcto: esas identidades expulsarían una tercera pendiente no nula que el techo admite.

La cláusula de conflicto también es la del Documento 5, puesta en la sección 1 y no solo heredada. Donde B6 cubre la tupla, la única dirección de contraejemplo es `c_0 < c_strict^{iso}`. Un testigo por encima, dentro de la tupla cubierta, es conflicto y se revisa antes que cualquier otro desenlace. Fuera del techo (`C4` como clase, o un nodo cuyo transporte `g^{-1}k_⋆-k_⋆∈Λ^*` falla para algún `g∈D2`) las dos direcciones siguen admitidas, y el testigo por encima tiene que comprobar por su cuenta que no cumple las hipótesis del techo. La salvedad de un símbolo de `C4` que además sea covariante bajo `D2` está escrita.

La frase de más es «su pendiente no es `c_0`». El Documento 6 aísla autovalores en el nodo, no pendientes. Un espectador con la misma pendiente y otra cuasienergía sigue dentro del techo y aquí dejaría de ser admisible. Además, «pendientes `+c_0|q|` y `-c_0|q|`» no es lo que dice el techo: el techo dice pendientes `±c_0`, es decir fases `ω_⋆±c_0|q|+o(|q|)`. Escrito así, un certificado puede exigir que la derivada valga `c_0|q|`.

## 4. Tabla de la unión

Cubre el cierre en el paso 0, el caso «hay símbolos y ningún sector» y la mezcla de clases vacías, sin sector y rígidas. No parte el conjunto de situaciones.

| Situación | Qué casa dispara | Qué falla |
| --- | --- | --- |
| Todas las clases `EMPTY_CLASS` | `S3_VACUOUS`, también en el paso 0 | Nada |
| Todas decididas, alguna con símbolos, ninguna con sector | `S3_NO_ADMISSIBLE_SECTOR` | Nada |
| Todas decididas, cada una vacía, sin sector o rígida, y alguna rígida | `S3_RIGID` | Nada |
| Alguna con contraejemplo verificado y las demás decididas | `S3_COUNTEREXAMPLE` | Nada |
| Contraejemplo en un rango e igualdad en el otro | La unión es el contraejemplo; la regla de lectura pide registrar los dos rangos | No borra el rango que no falla, pero solo en la ficha de la clase |
| Una clase con contraejemplo y otra sin decidir | Las dos filas, contraejemplo y `OPEN` | Sin prioridad |
| Una clase con símbolos y sin sector, y otra abierta en el paso 1 | `OPEN` y, leído sobre lo ya registrado, también «ninguna tiene sector» | Sin la cláusula «todas decididas» |
| `c_0 > c_strict^{iso}` dentro de una tupla cubierta | Ninguna fila | El conflicto está en la sección 1 y no en la sección 5 |

`S3_VACUOUS` (toda clase `EMPTY_CLASS`) y el `VACUOUS` de la fila rígida (el desenlace por clase del charter mínimo: vacía o sin sector) no son la misma palabra. No se solapan como etiquetas, pero se pueden copiar mal.

La saturación queda fuera de la tabla. Eso es correcto: la sección 1 la separa de la pregunta principal.

La fila rígida sí recoge lo que pedía G-S3-08: vacío de símbolos, ausencia de sector y rigidez pueden convivir, con al menos una clase rígida, sin caer en `OPEN`. El contraejemplo de una clase no necesita una etiqueta compuesta: la pregunta principal es universal, así que un solo contraejemplo decide la unión, y las reglas heredadas conservan el desenlace de las otras clases.

## 5. Alcance

Ninguna frase nueva decide más de lo que este charter puede decidir. La sección 0 dice que un vacío de estas familias no dice cuál es la dimensión interna no rígida mínima en `N_3`. La sección 5 lo repite como techo, junto con `s≠3`, otros soportes, término on-site, reflexiones, antiunitarias, masas, interacciones, universalidad, escala y naturaleza. `v_max` no se escribe solo. La literatura condiciona la novedad y la palabra «clasificación», no el cierre dentro de P y F.

La nota «fuera de este charter» no afirma el resultado para `s` impar. Dice que el mismo argumento, si es correcto, valdría para todo `s` impar en `N_3` sin término on-site bajo estos grupos, y que esa afirmación necesita otro charter. El certificado del paso 0 sigue siendo solo de `s=3`, con controles en `s=2` y `s=4`. No hay que promover esa frase a un enunciado: la cuenta de paridad con `s` factores impares es inmediata, pero este borrador no la decide.

`s=2` rígido en su única clase declarada no vacía, y `s=4` no rígido en la suya, coinciden con el Documento 7. T3 y O3 se reutilizan como vacío ya promocionado; la cabecera desactualizada del otro charter se cita y no se enmienda.

## Objeciones nuevas

**G-S3-R2-01. Redacción que puede desviar el certificado.** Sección 3, paso 0, punto 3 («los vectores fijos de `g^T`»). El invariante que hay que vaciar es el común a todo `G`. En `T` y en `O` un elemento de orden 3 fija `(1,1,1)`, que es impar. B5, en la sección 0, ya lo dice bien: `V4` solo fija `0`, y el eje de `C4` no está en el coseto. El punto 3 tiene que repetir ese cuantificador.

**G-S3-R2-02. Laguna.** Sección 5, tabla de la unión. No es una partición. `OPEN` convive con `S3_COUNTEREXAMPLE` si otra clase sigue sin decidir, y puede convivir con `S3_NO_ADMISSIBLE_SECTOR` si «ninguna tiene sector» se lee sobre lo ya certificado. Esas dos filas necesitan «toda clase decidida», y el contraejemplo tiene que ganar a `OPEN`. El conflicto `c_0 > c_strict^{iso}` dentro de una tupla cubierta no tiene fila ni remisión en la sección 5; la sección 1 lo deja fuera de «contraejemplo», pero la tabla no dice qué etiqueta usar mientras se revisa. En la fila rígida, `VACUOUS` es el desenlace por clase del charter mínimo, no `S3_VACUOUS`.

**G-S3-R2-03. Laguna.** Sección 1, codificación `r=2`, «su pendiente no es `c_0`», y «pendientes `+c_0|q|` y `-c_0|q|`» en los dos rangos. El Documento 6 no exige que el espectador tenga otra pendiente: lo deja fuera del cono porque no está en `P`. La frase estrecha la admisión y, a la vez, el borrador dice que las codificaciones siguen las filas del techo. La pendiente que hay que escribir es `±c_0`, con fase `ω_⋆±c_0|q|+o(|q|)`, no `±c_0|q|`. Esta frase venía de la reparación de la ronda 1; contra el Documento 6 sobra.

**G-S3-R2-04. Redacción.** Sección 0, B1, «Step 0 checks the multiplier exponent». Ese chequeo está en el paso 0′, y 0′ solo existe si el paso 0 no cierra. En el certificado de paridad no hay multiplicadores de Schur.
