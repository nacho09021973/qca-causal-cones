<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 73be113fc136f9626cb95ae89ce47a1fdf09ae7bdd96ac2c5c4c67a5a411c682
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-03T12:15:06Z  fin: 2026-11-03T12:25:57Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--hex-supremum.md ; último commit observado: 8abca3c ; sha256 de la copia enviada 8a4c4eece8cda613d9945e8aa106729620e31c958c1c43941c70d781d0db26b5
documento: /home/ignac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_supremum_gate.py ; último commit observado: 8abca3c ; sha256 de la copia enviada ef4b0114124d16937ced9a600a65b229c6fd968ab417d8493d1297806bf46a55
documento: /home/ignac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_ceiling_gate.py ; último commit observado: bb4fcdb ; sha256 de la copia enviada 8f3b7a10ecee91c515429640b794da91e2c0e273176f5bbbd62e56a0f3b43d72
documento: /home/ignac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
entrada_grok.txt sha256 b1ef01f64fc78e3b902c98bd5669c3d5b0d18b870e2f6e9675025e0f3d53b408
respuesta sha256 f1ad217753b9d660c7a8db5bb48ca967d46ae7ddd074ff8d6f2c25f955deeaac
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias.

La cadena de S13 cierra: la rigidez de cara da sumas de capa nulas sobre la malla uniforme; en S13 esas capas de un solo punto son exactamente el anillo interior; el soporte que queda es el de T2 tras un giro conjunto de −30°, y T2 no usa la factorización ni la red. A2 es correcto y no interviene. Los veredictos no salen de ese alcance. No he ejecutado el verificador: la geometría y las implicaciones se rehacen aquí a mano; el certificado de T2 (base de Gröbner y discriminante) se toma del gate padre ya promocionado, que esta revisión no reabre.

## 1. Lema A1 — PASS

La rigidez (informe padre, Sec. 3, Paso 1) da la identidad de operadores
`U(t n_f) = e^{-i r t} P₊ + e^{i r t} P₋`, no solo un símbolo escalar: el caso de igualdad fija `⟨x, U x⟩` en cada autovector de `A(n_f)`, y Cauchy–Schwarz más `|Ux|=1` suben eso a `Ux` igual a la fase; con espectro `{±c₀}` se obtiene el operador.

Esa identidad implica sumas de capa nulas sin hipótesis extra sobre qué puntos de `F` están ocupados. Hace falta, y está en L0 del padre, lo siguiente. Si la arista es un vector de red `d`, entonces `h · n_f = m δ` con `δ = √3/(2|d|)` y `m ∈ ℤ` para todo `h ∈ Λ`. Los vértices están en `F` (son extremos de `conv F`), así que `r = h_C(n_f) = N δ` con `N` entero, no un nivel intermedio de la malla. Los coeficientes de Fourier de `U(t n_f)` son las sumas de las matrices `A_h` de cada nivel `m`, y por unicidad coinciden con `P₊`, `P₋` y ceros. Un nivel intermedio con un solo punto de `C ∩ Λ` tiene un solo sumando posible (`F ⊂ C`), luego esa matriz es cero, esté o no en `F`.

En S13 el giro de 60° entre vértices `g₁+g₂ = (1,1)` y `(-1,2)` tiene `d` de coordenadas enteras coprimas, `|d|=√3` sin normalizar, `δ = 1/2`, `r = 3/2`, `N = 3`. Tras `|v|=1`, `δ = r/3`. No queda hueco de soporte.

Aclaración, no error: el párrafo de A1 no reescribe la malla; cita el Paso 1, como autoriza el contrato. En S19, `d = 2(g₂−g₁)` tiene `gcd = 2`, así que el `δ` formal de L0 es la mitad del paso realmente ocupado y el grado ocupado es `N = 2`, no 4. Las capas ocupadas siguen siendo cinco; no aparecen singletons fantasma. El informe acierta al usar `N = 2`.

## 2. Geometría de S13 — PASS

Con `|h|² = a² + ab + b²`, el hexágono cerrado de vértice `g₁+g₂` (`|v|² = 3`) es exactamente `{|h|² ≤ 3}`: 1 origen, 6 puntos de norma 1 y 6 de norma 3. Son 13. No hay más puntos de red, porque `C` está en el disco de radio `|v|`. S7 (`≤ 1`) y S19 (`≤ 4`) dan 7 y 19 por el mismo conteo; en S19 los de norma `√3` caen en el centro de las aristas.

Normal at 60°, `n = (1/2, √3/2)`, nivel entero `m = a+2b` (extremo `±3`):

| m | puntos | tamaño |
|---|--------|--------|
| 3 | dos vértices | 2 |
| 2 | `(0,1)` | 1, anillo |
| 1 | dos del anillo | 2 |
| 0 | origen y dos vértices | 3 |
| −1 | dos del anillo | 2 |
| −2 | `(0,−1)` | 1, anillo |
| −3 | dos vértices | 2 |

Los otros dos normales (120° y 180°) recorren el anillo por la simetría de 60°. Esos seis singletons son los seis vecinos y ningún otro punto. A1 los anula todos y queda `F ⊂ {0} ∪ vértices`. Las aristas solo contienen sus dos vértices, así que no sobra un punto de arista.

La segunda vía es correcta y más débil de lo que parece: las ecuaciones de capa incluyen ya `A_h = 0` en cada singleton, con blanco 0, sin usar `P₊`. El `solve` lineal del verificador, si termina en una sola solución y esas matrices quedan a cero, solo reencuentra ese subsistema. No es una geometría distinta; es la misma, en álgebra. El código agrupa por `n·p / (r/3)`, exige niveles `−3..3` enteros, toma tres normales a 60° (no los tres opuestos) y pone `P₊ = (I + n·σ)/2` solo en los extremos. Eso es lo que tiene que comprobar. No puedo afirmar el 12/12: no lo he ejecutado. La enumeración de arriba no depende de esa ejecución.

En S19, el mismo nivel `a+b` sobre la arista entre `2g₁` y `2g₂` da tamaños 3, 4, 5, 4, 3. Ningún intermedio es singleton. El informe lo dice bien.

## 3. Aplicabilidad de T2 — PASS

El contrato separa las direcciones: una cota en `W_hex^sym` solo puede usar unitariedad, `F`, nodo e isotropía. `check_T2_minimal` hace eso (sumas de capa, `UU†` y `U†U` sobre los siete puntos, sin producto moneda–desplazamiento y sin `G1`, `G2`). Vale para la clase ampliada y por tanto para `W_hex`.

Los vértices de S13, ya con `|v|=1`, están en `π/6 + kπ/3`. El giro `R_{−π/6}` los lleva a `(cos kπ/3, sin kπ/3)`. Los normales, que iban a `π/3 + kπ/3`, caen en `π/6`, `π/2`, `5π/6`, que es la configuración escrita en T2. El verificador comprueba ese giro concreto; no una semejanza genérica.

La forma normal se conserva. Si `A(n) = r n·σ` y `V` es la rotación de Bloch en torno a `z` del mismo ángulo, `U_new(k) = V† U(R_{−θ}^T k) V` mueve el soporte con `R_θ`, mantiene `U(0)` escalar, la unitariedad, el patrón de ceros y `A_new(n) = r n·σ`. Las diferencias `h−h'` se giran en bloque, así que las ecuaciones de T2 se transportan por una conjugación invertible común a todos los coeficientes. El discriminante negativo no hay que rehacerlo.

Aclaración, no error: la frase «encodes the vertices abstractly» (`check_T2_minimal`, líneas 166–238) significa que esos vértices están escritos como geometría, no como puntos de `Λ`. El checker no cuantifica sobre semejanzas. Aquí no hace falta: el giro de −30° está comprobado aparte y cae exactamente sobre ese juego de coordenadas. La cita de líneas cuadra con el arranque de la función.

## 4. Lema A2 — PASS

El coeficiente de `UU†` en el desplazamiento `2v ≠ 0` es `∑_{h−h'=2v} A_h A_{h'}^†`, y análogo el de `U†U` en el orden `A_{h'}^† A_h`. Ambos son cero por unitariedad.

Unicidad: `h−h'=2v` con `h,h' ∈ C` y `C=−C` pone a `h` y a `−h'` en `C` con punto medio `v`. Un punto extremo no es punto medio de dos puntos de `C` salvo el caso trivial, luego `h=v` y `h'=−v`. La misma conclusión sale del soporte: `(h−h')·v = 2|v|²` y `x·v ≤ |v|²` en `C`, con igualdad solo en `v` (el cono normal de un vértice del hexágono es abierto y el máximo se alcanza en un único punto). Hacen falta las dos cosas que el informe nombra: simetría central y extremalidad. Vale para todo hexágono regular centrado, y de hecho para todo convexo centralmente simétrico en un punto extremo. Si `v` o `−v` no están en `F`, el producto es cero igual.

A2 no se usa en S13. No está en el verificador; el contrato pide el Paso 2 demostrado en el informe, y el informe solo demuestra este caso de vértices opuestos, no las identidades de arista completas. Para el veredicto de S13 es indiferente. No pido que se cierren esas identidades: S19 está fuera de alcance.

## 5. Alcance y niveles — PASS

Lo demostrado es: si `c₀ = r_in` y `F ⊂ S13` con el casco hexagonal regular, el anillo interior se anula, el resto cae en T2 y no hay solución. Eso es `M1-B13 = PROVED_FOR_S13` en `W_hex^sym` y por tanto en `W_hex`, y `HX2 = CONFIRMED_FOR_S13`. S7 queda cubierto por el T2 padre, como ya dice el contrato; no es una extensión. No se afirma supremo cuantitativo en S13, solo la desigualdad estricta.

`M1-A = OPEN_AFTER_SINGLETON_LAYER_ANALYSIS` es una de las tres salidas permitidas: A1 y A2 no dan cota para toda la clase ni una forma normal general. `HX2` en general sigue `OPEN`. S19 se describe y se deja sin empezar; `s > 2` y hexágonos mayores están en la Sec. 6 como no establecidos. La línea M1 no se cierra ni se declara conservada, que es lo que el contrato pide para un soporte acotado.

El informe no atribuye al verificador la rigidez, la forma normal ni el carácter libre de red de T2. El propio verificador lo excluye en su cabecera. A2 queda solo en el texto. Las etiquetas `PROVED_FOR_S13` y `CONFIRMED_FOR_S13` no exceden esa división.

## Aclaraciones que no obligan a corregir

- A1 hereda `r = Nδ` del L0 citado; leído aparte, el «so» del párrafo es corto, pero el paso es válido.
- La segunda vía no es independiente de la geometría de los singletons; la confirma.
- «Abstractamente» no quiere decir «para toda semejanza».
- El `solve` lineal y el relanzamiento de `check_T2_minimal` recalculan álgebra exacta ya identificada; no son una búsqueda numérica ni un certificado de S19.

**Reparaciones obligatorias: ninguna.**
