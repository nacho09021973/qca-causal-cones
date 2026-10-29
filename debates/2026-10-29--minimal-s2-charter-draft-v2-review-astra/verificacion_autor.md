# Lectura crítica del autor — revisión Astra, ronda 2 (borrador v2 del charter s=2)

Fecha: 2026-10-29. Autor de esta lectura: Claude, autor del borrador. **No es una revisión
independiente.** La revisión independiente es la de Astra (gpt-6-astra, familia OpenAI).

## Ejecución

- Un intento, `COMPLETED`, de 10:32:52Z a 10:40:02Z.
- Antes del envío, `sha256sum -c inputs.sha256` dio OK.
- Siete documentos enviados: el borrador v2 (`e117d2e`, `6c7594a9…`), el informe de la ronda 1,
  tres charters predecesores (incluida la cota general), la auditoría de fuentes y el PDF de P17.
- Herramienta: `revision_ciega.sh` @ `a32e189`.
- Autorización del usuario: «si, segunda ronda y los commit pendientes».

## Veredicto del revisor

`NOT_READY`:

- Ocho reparaciones de la ronda 1 quedan resueltas: 02, 04, 05, 08, 09, 12, 13 y 14.
- 01, 03, 06 y 07 quedan resueltas para la familia P, con ajustes pendientes en F.
- 10 y 11 quedan parciales.

Seis lagunas nuevas, A-R2-01 a 06. Ningún error nuevo en la identidad tangencial, en A2 con
`Q8`, en la normalización ni en las leyes de transporte.

## Contraste

**A-R2-03 (hipótesis D2 de la cota general).** Se acepta y es la más importante. Comprobado en
`theory/STRICT_CONE_CEILING_N3_GATE.md:34`: la clase de la cota exige covarianza bajo el `D2`
de medias vueltas cartesianas. La clase P con `C4` sobre una cara no contiene ese `D2`, así que
la cota no la cubre automáticamente. El revisor también da la condición para mover un nodo sin
perder la covarianza: `g^{-1}k_star − k_star ∈ Λ^*`. Basta comprobarla para el `D2`.

**A-R2-04 (contraejemplo solo con `c_0 < c_strict^iso`).** Se acepta. Donde la cota no está
certificada (por ejemplo, en la clase `C4`), la salida debe admitir `c_0 ≠ c_strict^iso` en
cualquiera de los dos sentidos.

**Familia F.** Se acepta el cálculo del revisor, comprobado a mano.
- Un subgrupo transitivo sobre ocho vértices tiene orden 8 o 24. Por tanto F se reduce a `D4`
  (un 2-Sylow, transitivo y regular) y a `O`, salvo conjugación.
- Con `R` escalar sobre un subgrupo transitivo, los ocho `T_h` son iguales a una misma `A`.
  - El desplazamiento `(2,2,2)` tiene un solo par, que da `A^†A = 0`.
  - El desplazamiento cero da `8A^†A = I`.
  - Las dos identidades se contradicen: la clase es vacía.
- `E` bajo `O` o `D4` es escalar sobre `V4`, que no es transitivo sobre los ocho vértices.
  Basta A1 en el tetraedro.

**A-R2-02 (solapamiento P/F).** Se acepta. Todo símbolo de F, restringido a `V4`, está en una
clase P. Dos efectos:
- F no amplía la unión de símbolos de P; solo declara simetrías más fuertes.
- Un mismo símbolo en varias filas no es evidencia adicional.

**A-R2-01, 05 y 06.** Se aceptan como lagunas de definición:
- A-R2-01: tuplas de F sin `S_±`, y dominio de la Eq. (2) en F (`h ∈ N_3`).
- A-R2-05: las salidas sobre sectores admisibles se deciden en 4b-2, no en 4b-1. Además hay que
  fijar si Q-a cuantifica sobre símbolos unitarios o sobre símbolos con cono admisible.
- A-R2-06: separar la rigidez universal del fallo de saturación existencial o universal.

**Aportaciones técnicas del revisor que sirven para la v3:**
- Codificar el soporte activo con `y·∏ d_h − 1 = 0`.
- Usar como certificado de vacío real la forma `−1 = Σ a_i f_i + Σ b_j^2`.
- Formular la admisibilidad del nodo con `H_j = i ā ∂_j U(k_star)`, `tr H_j = 0` y
  `½ tr(H_j H_l) = c_0^2 δ_jl`.
- Rango uno sin Eq. (2): el desplazamiento `2h` tiene un solo par antipodal. No
  nilpotencia equivale a `tr T_h ≠ 0`.

Todo esto es derivación del revisor `[UNVERIFIED]` hasta que un certificado lo compruebe.

## Conclusión del autor

- La v2 resolvió los errores de la ronda 1. Las seis lagunas nuevas son de cuantificación y de
  alcance, no errores matemáticos.
- La más seria es A-R2-03: la cota general no cubre la clase `C4`.
- Hace falta una v3. Dos opciones de diseño necesitan decisión del usuario:
  - si la clase `C4` (cara) se mantiene, con contraejemplo en ambos sentidos;
  - si Q-a cuantifica sobre símbolos unitarios o sobre símbolos con cono admisible.
- Nada de esto autoriza congelar ni calcular.
