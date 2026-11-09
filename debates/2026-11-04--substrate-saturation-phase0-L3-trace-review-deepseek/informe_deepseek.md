<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 b7dff1d32640570a8d8f7fb5bb43b94e7a642e5c837a8bbf9063dc3634a3d008
inicio: 2026-11-04T07:22:33Z  fin: 2026-11-04T07:36:04Z
documento: /home/ignac/qca-causal-cones/reports/2026-11-03--substrate-saturation-phase0.md ; último commit observado: 2f6160e ; sha256 de la copia enviada 3b88e925ec75a3efb81bb13ba9f07c1d4ca4cd2fef374bc9b9627ee312621676
documento: /home/ignac/qca-causal-cones/theory/SUBSTRATE_SATURATION_PHASE0_GATE.md ; último commit observado: 9bf3019 ; sha256 de la copia enviada 62d198bc961b831f2d67f8e7420b5c61b95c25059fa1814541369af1634ba13f
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/debates/2026-11-04--substrate-saturation-phase0-L3-trace-review-deepseek/extractos.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8bf9c85538a866c6417c2ffe6765ada7d5db628c0a0468a09759e83fd56a98ba
entrada_deepseek.txt sha256 6c4b9b77a0e445038790dee300aee3b6de04da770647eb6b5e0b94c808772a78
respuesta sha256 885cf826cb5600905ddf0be92e78d29eb60ae7b9f3cf783071bbe4dbdc40eda8
-->

He revisado el párrafo citado contra el verificador, el contrato congelado y los extractos. Alcance: no ejecuto nada; solo verifico las atribuciones del párrafo.

## 1. LÍNEAS — PASS

- **l. 147** (`check_zero(f"{name}: Weyl unitarity", matrix * adjoint - IDENTITY)`): atribuida a comprobar `W W^† = I` como identidad de Laurent. Correcto: `laurent_adjoint` sustituye `z_j → 1/z_j` y toma la adjunta matricial; el chequeo es exacto con residuo cero.
- **l. 149** (`check_zero(f"{name}: scalar trace", sp.trace(matrix) - 2 * scalar)`): atribuida a `tr W = 2u`. Correcto; `scalar` es el `u` devuelto por `published_symbol`.
- **l. 158** (`check_zero(f"{name}: zero node", matrix.subs(origin) - IDENTITY)`): atribuida a `W(0)-I=0`. Correcto; `origin` pone todas las z en 1, que corresponde a `k=0`.
- **l. 159–160**: el párrafo dice que el verificador fija `spatial = i ∂W` en el origen. El código literal hace `spatial = [sp.I * spatial_derivative(...).subs(origin)]`. Como `spatial_derivative` es `i z ∂_z / sqrt(d)`, bajo la normalización de `CURRENT_STATE` Sec. 5 (`N_d = {(±1,...,±1)/√d}`, z como fase `e^{ik/√d}`), `spatial_derivative` es precisamente la derivada respecto a la k euclidiana, `∂_k W`. Por tanto `spatial = i ∂_k W(0)`. La atribución es correcta, aunque implícitamente depende de esa normalización.
- **l. 161–162** (`scalar gradient`): atribuida a comprobar `∂u = 0` en el origen. Correcto: deriva `scalar` con `spatial_derivative` y evalúa en `z=1`.
- **l. 164–167** (`Clifford`): atribuida a comprobar `{spatial_a, spatial_b} = 2 δ_ab/d I`. Correcto; la comprobación resta exactamente `2 * expected * I`, con `expected = δ_ab/d`.
- **l. 172–173** (`massless matching`): el párrafo dice que por “massless matching” se obtiene `c_0 = 1/sqrt(d)`. El código no asigna textualmente ese valor, sino que calcula `speed = sqrt(trace(spatial[0]^2)/2)` y comprueba `speed - inradius`. Como `spatial[0]` es `T_1`, esa velocidad es `c_0`; la línea comprueba `c_0 = r_in = 1/√d`. Es una aclaración, no un error.

Conclusión: las líneas citadas hacen lo que el párrafo les atribuye, salvo precisiones de notación.

## 2. COBERTURA DE L3 — PASS

La fila L3 en `c-across-lattices` l. 143 es BCC, `r_in = 1/√3`, `c_0 = 1/√3`, con fuente `CURRENT_STATE Secs. 4, 5 (certified)`. El extracto de `CURRENT_STATE` Sec. 5 define `N_d = {(±1,...,±1)/√d}`, `C_micro = [-1/√d, 1/√d]^d`, `r_in = 1/√d`, y declara los casos d=3 `A+, B+, A-, B-`. El verificador, en `run()`, genera exactamente siete casos: d=1 A; d=2 A, B; d=3 A+, B+, A-, B-. Para d=3, `fourier_support` verifica soporte activo `{(-1,1)}^3` y `hull_geometry` divide por `√3`, dando los mismos vértices `(±1,±1,±1)/√3` que L3.

La identificación no es por un token literal `L3` dentro del verificador, sino documental: la fila L3 cita `CURRENT_STATE` Secs. 4–5, y esa sección declara los símbolos d=3 que el verificador comprueba. Con lo adjuntado, la identificación se sigue de forma suficiente.

## 3. DERIVACIONES — PASS

**(ii) Hermiticidad.** De `W W^† = I` como identidad de Laurent y `W(0)=I`, al derivar en `k=0` respecto a una coordenada `a`:

`∂_a W(0) + ∂_a W^†(0) = 0`.

Sea `T_a = i ∂_a W(0)`. Entonces

`T_a^† = -i ∂_a W^†(0) = -i(-∂_a W(0)) = i ∂_a W(0) = T_a`.

Por tanto `T_a` es hermítica. La convención de signo no cambia esto: si se adoptara `T_a = -i ∂_a W(0)`, también sería hermítica. Un factor real global tampoco rompe la hermiticidad.

El factor `1/√d` de `spatial_derivative` solo es inocuo bajo la normalización correcta ya citada (`z=e^{ik/√d}`). Bajo esa convención, `spatial_derivative = ∂_k`; con eso, `spatial = i ∂_k W`. Si literalmente se usara `z=e^{ik}` sin factor en el exponente, el `1/√d` del código escalaría mal el anticonmutador. No es el caso aquí.

**(iii) Traza nula.** El verificador comprueba `tr W = 2u` y `∂_a u(0)=0`. Entonces:

`tr(T_a) = tr(i ∂_a W(0)) = i ∂_a tr W(0) = 2i ∂_a u(0) = 0`.

El signo o el factor real no afectan a la traza nula.

**(iv) Anticonmutador y `c_0`.** El código comprueba para `spatial_a = i ∂_a W(0)` que

`{spatial_a, spatial_b} = 2 δ_ab/d I`.

Por la definición del contrato, `{T_a,T_b} = 2 c_0^2 δ_ab I`; por tanto `c_0^2 = 1/d`, es decir `c_0 = 1/√d`. La línea 172–173 es la comprobación de masa nula: `speed = sqrt(trace(T_1^2)/2)` y `speed = inradius`. Eso verifica `c_0 = r_in`, no es la única fuente del valor `1/√d`, pero es coherente.

## 4. INCLINACIÓN — PASS

Con (iv), para `A(n)=Σ n_a T_a`:

`T_a^2 = c_0^2 I` y, para `a≠b`, `T_a T_b + T_b T_a = 0`.

Por tanto:

`A(n)^2 = Σ_a n_a^2 T_a^2 + Σ_{a<b} n_a n_b (T_a T_b + T_b T_a) = c_0^2 |n|^2 I`.

La traza nula de (iii) garantiza que `A(n)` sea traza nula, como declara la forma equivalente del contrato. El contrato declara la equivalencia entre el paquete de nodo isotrópico no inclinado y `A(n)^2 = c_0^2 |n|^2 I`. Por tanto, llegar a “zero tilt” mediante esa equivalencia es correcto.

## 5. UNIDADES Y ALCANCE — PASS

El verificador no mezcla unidades: extrae soporte en `{±1}^3`, luego `hull_geometry` lo divide por `√d`, por lo que el paso más largo es 1 y el inradio es `1/√d`. Eso coincide con el contrato `N_d = {(±1,...,±1)/√d}`, `C_micro = [-1/√d,1/√d]^d`.

La regla de una sola fuente por fila se respeta para la pareja `(r_in,c_0)`: L3 toma la pareja de la fila l. 143; el verificador se usa para trazar el certificado de nodo, no para sustituir esa pareja por otra normalización. No hay cruce de unidades.

Finalmente, el párrafo distingue correctamente el Hessian de l. 169–171 del certificado de nodo y no lo usa como tal. Tampoco presenta la traza nula como evidencia a favor de (PH): la usa solo dentro del paquete de nodo admisible.

## Dictamen global

**PASS.**

No encuentro defectos que exijan reparación. Hay dos aclaraciones no bloqueantes:

1. En l. 159–160, la igualdad `spatial = i ∂W` es correcta bajo la convención `z=e^{ik/√d}` de `CURRENT_STATE` Sec. 5; convendría hacer explícita esa dependencia si el párrafo se reutiliza.
2. En l. 172–173, “`c_0=1/sqrt(d)` by massless matching” es una abreviación: esas líneas calculan `c_0` desde `T_1` y comprueban igualdad con `r_in`; el valor `1/√d` ya está fijado por el chequeo de Clifford.

**Reparaciones obligatorias: ninguna.**
