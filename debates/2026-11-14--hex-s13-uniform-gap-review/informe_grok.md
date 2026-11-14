<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 7daae462d5871c2270abf8d53a894af9a776f245a7368c774098d2b1156fc83b
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-14T07:04:49Z  fin: 2026-11-14T07:17:18Z
documento: /home/adnac/qca-causal-cones/debates/2026-11-14--hex-s13-uniform-gap-review/candidato.md ; último commit observado: sin versionar ; sha256 de la copia enviada 282f3024294d86179f57c3d62b82b1557eea8841b7795fd8297b598ad39df042
documento: /home/adnac/qca-causal-cones/reports/2026-11-03--hex-supremum.md ; último commit observado: 677bec0 ; sha256 de la copia enviada 177d94d3e6991fb45fddadad218dd05c4ce7c0011419c481a2c94c5acccf0c88
documento: /home/adnac/qca-causal-cones/reports/2026-11-01--hex-ceiling.md ; último commit observado: bb4fcdb ; sha256 de la copia enviada fbbf6c822db13a1eec6bdcecc1f9dafa5e9fbf7835524bd871f1781c956b2dbc
documento: /home/adnac/qca-causal-cones/theory/HEX_SUPREMUM_GATE.md ; último commit observado: 86573ca ; sha256 de la copia enviada cf272f3daf8715049289268e7e9330b3b1e064625a011118d2198583895b77bc
documento: /home/adnac/qca-causal-cones/theory/HEX_CEILING_GATE.md ; último commit observado: 8c56ced ; sha256 de la copia enviada 8f8223e6cd651e4120d65a2c29fef87e32a3a00309c5811a148289cb236af9a0
entrada_grok.txt sha256 51ad53cb2e98e5f78c0aaf8e7d4f5cb53b7caa969891cd41a5d8fb64764506a4
respuesta sha256 bf4366138ff0b3fd04667821417fce90f6c28e99ec5837f80052a0128b0410bf
-->

**Dictamen global: PASS.** Las seis piezas cierran. No hay reparaciones obligatorias.

## 1. CLASE — PASS

`X_13` es el conjunto que cubre M1-B13. El informe promocionado afirma que ningún paseo de `W_hex^sym` con `F ⊆ S13` alcanza `c_0 = r_in`. En esa clase la envolvente es un hexágono regular centrado, el vector más largo tiene longitud 1 y los únicos puntos de S13 a distancia 1 son sus seis vértices. Con uno de menos la envolvente deja de ser ese hexágono; con los seis, `conv F = conv S13` aunque falten el origen o el anillo interior. Esa es la definición de `X_13` (s=2, Laurent unitario, nodo escalar, cono isótropo sin traza, `c_0 > 0`). El denominador es constante: `|vértice| = 1` fija `r_in(conv S13) = √3/2` en todo `X_13`.

## 2. LEMA 1 — PASS

Todas las condiciones de `Y` son cerradas. La unitariedad equivale a las identidades de coeficientes de `U U^† = I`; en matrices 2×2 eso equivale a `U^† U = I`. `U(0)` escalar es lineal en los `A_h`; junto con la unitariedad, el escalar tiene módulo 1, así que la fase queda fijada por `e^{iφ} U(0) = I` y `e^{iφ}` es continuo sobre `Y`. El término lineal `A(n) = i d/dt[e^{iφ} U(t n)]_{t=0}` coincide con el del gate. Sin traza en una base, y por linealidad en todo `n`.

La isotropía escrita con `A(e_1)^2 = A(e_2)^2 = c^2 I` y `{A(e_1), A(e_2)} = 0` equivale a `A(n)^2 = c^2 |n|^2 I` para todo `n` cuando `e_1, e_2` es la base ortonormal: al desarrollar `A(x e_1 + y e_2)^2` el anticonmutador es el término cruzado y se anula precisamente si `e_1 · e_2 = 0`. Son igualdades polinómicas en los coeficientes, en `e^{iφ}` y en `c`, con `c ≥ 0` cerrado. La traza nula es lineal. La identidad de orden cero de `U^† U = I` es `∑_h A_h^† A_h = I`, luego `‖A_h‖ ≤ 1`. En dimensión finita, `Y` es cerrado y acotado, así compacto.

Dentro de S13 no hay otra condición abierta. La regularidad hexagonal de la envolvente queda implicada por los seis vértices no nulos: no hay puntos de red en las aristas, y el anillo interior no cambia `conv`. `X_13 = Y ∩ {c_0 > 0} ∩ {A_v ≠ 0 en los seis vértices}`. `c_0^2 = (1/2) tr A(e_1)^2` vale sobre `Y` y es no negativo; `c_0` es su raíz continua y `ρ = c_0 / (√3/2)` es continuo. El máximo en la clausura compacta se alcanza.

Aclaración, no error: «por bilinealidad» es la polarización del cuadrado. Conviene nombrar que `e_1, e_2` es base ortonormal. La equivalencia, tal como está escrita, es cierta en esa lectura.

## 3. LEMA 2 — PASS

Geometría, con `v` el vértice en ángulo `π/6`. Los otros cinco vértices proyectan en `{-1, -1/2, 1/2}`. El anillo, radio `1/√3` y ángulos `±30°, ±90°, ±150°` respecto de `v̂`, proyecta en `{1/2, 0, -1/2}` porque `(1/√3) cos 30° = 1/2`. El origen da `0`. El conjunto es `{-1, -1/2, 0, 1/2}`; el valor `+1` es solo `v`. Más coeficientes nulos solo quitan frecuencias.

`W(0) = I` y `H = i W'(0) = A(v̂)`. Derivar `W W^† = I` da `W'(0)` antihermítica, luego `H` hermítica. Por (c), `H` tiene traza nula y `H^2 = c_0^2 I`, así espectro `{±c_0}` (raíces simples si `c_0 > 0`, y la traza separa los dos signos).

`W(4t)` tiene frecuencias `4p` con `p` en ese conjunto, es decir `{-4, -2, 0, 2}`. `P(t) = e^{-it} W(4t)` las desplaza a `m = 4p+1 ∈ {-3, -1, 1, 3}`. Grado ≤ 3, convención `e^{-imt}` la del Lema B. Para `‖x‖ = ‖z‖ = 1`, el escalar `⟨z, P(t) x⟩` tiene módulo ≤ 1, luego `|⟨z, P'(0) x⟩| ≤ 3` y `‖P'(0)‖ ≤ 3`. La derivada es `P'(0) = -i I + 4 W'(0) = -i(I + 4H)`, porque `W'(0) = -i H`. De ahí `‖I + 4H‖ ≤ 3`. El autovalor `1 + 4c_0` cumple `1 + 4c_0 ≤ 3`, así `c_0 ≤ 1/2` y `ρ ≤ (1/2)/(√3/2) = 1/√3`.

Vale en un punto de la clausura fuera de la clase. El enunciado pide solo `y ∈ Y` y un vértice nulo. La clausura está en `Y`, así que siguen la unitariedad, el nodo y la isotropía. No usa que `conv F` sea hexagonal. El grado sigue ≤ 3 si faltan más puntos.

## 4. TEOREMA — PASS

La división es exhaustiva y excluyente sobre la clausura: `c_0 > 0` y los seis vértices no nulos; `c_0 = 0`; o `c_0 > 0` y algún vértice nulo. En el primer caso el punto está en `X_13`, aunque falten coeficientes del anillo interior o el origen: el soporte exacto sigue teniendo envolvente `conv S13`. M1-B13 da `ρ < 1` ahí. En el segundo, `ρ = 0`. En el tercero, el Lema 2 da `ρ ≤ 1/√3 < 1`. El máximo se alcanza en un punto `y`, luego `sup_{X_13} ρ = ρ(y) = 1 - ε_13 < 1`. Eso es cota uniforme `ρ ≤ 1 - ε_13` en `X_13`, alcanzada o solo en la clausura.

## 5. NO VACUIDAD — PASS

Con `a_1 + a_2 + a_3 = 0`, las ocho combinaciones de signos `σ_1 a_1 + σ_2 a_2 + σ_3 a_3`, `σ_j = ±1`, caen en `{0, ±2a_j}`: las dos de signos iguales dan 0, y `a_1 - a_2 - a_3 = 2a_1`, etc. El producto de exponenciales es unitario, `U(0) = I`, y el cono isótropo con vectores de Bloch coplanares a 120° tiene cociente `√3/2`, ya certificado en T1; el cociente no depende de la escala.

Tres vértices alternos de S13, a 120°, suman cero y son vectores de red (rotación de 120° del retículo). Con `b_j = 2a_j` igual a esos vértices, `F = {0} ∪ vert(S13)`, `conv F = conv S13` y los seis coeficientes de vértice son no nilpotentes, como en el certificado de T1. Nodo e isotropía se conservan, y `ρ = √3/2`. Por tanto `√3/2 ≤ 1 - ε_13 < 1`.

La salvedad es correcta: `a_j = b_j/2` no está en `Λ` (mitad de `g_1 + g_2`), así que esta factorización no es la forma producto de `W_hex`. El símbolo sí es de Laurent sobre `Λ`. Que `X_13 ∩ W_hex` sea no vacío queda sin decidir.

## 6. ALCANCE — PASS

Solo hay brecha cualitativa en S13: `0 < ε_13 ≤ 1 - √3/2`, sin valor de `ε_13`. Nada para S19, S25, soportes mayores ni `s > 2`, y nada que haga al sustrato fijar `c_0`.

La observación sobre hexágonos mayores está en su sitio. Quitar un vértice de S13 sustituye las dos aristas incidentes por la cuerda entre los vértices vecinos, a distancia `1/2` del origen, por debajo de `√3/2`; el Lema 2 recupera esa cota. En un hexágono mayor la cuerda entre los puntos de arista más próximos al vértice, a fracción `t` de la arista, está a distancia `R(1 - t/2)`. Eso baja el inradio centrado solo si `t > 2 - √3`. Si hay un punto de red con `t` menor, el inradio no cambia. El «may» es correcto, y el límite queda con envolvente no regular, fuera de `W_hex^sym`, donde L0, T2 y M1-B13 no dan `ρ < 1`. No se afirma nada sobre S19.

## Aclaraciones que no reparan

- Nombrar la base ortonormal y decir polarización en vez de bilinealidad.
- La continuidad de `ρ` usa la raíz de un polinomio no negativo.
- La Sec. 5 resume el Lema 2 como caída del inradio; el lema prueba `c_0 ≤ 1/2`, igual al inradio centrado de `conv(S13 \ {v})`.

Ninguna de esas frases es falsa ni deja un paso sin cerrar. No hay reparaciones obligatorias.
