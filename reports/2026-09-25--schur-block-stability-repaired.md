# Estabilidad L² del producto normalizado: reparación de Schur §2 con E5 explícito

Fecha: 2026-09-25. Estado: `SCHUR_STABILITY_PASS` (revisión independiente
documentada, §5) para la conclusión de §1 y nada más.
Alcance: **sólo** la cota uniforme de `||t_j||_2`, `0<=j<=N`, con `W`
admisible fijo y `vartheta` real acotado. No cubre Schur (7)–(8), ni
`||M_N|| = O_W(N^-1)`, ni las cotas de las diez piezas físicas, ni H1/H1c.
Revisión: ver §5. Las consecuencias físicas que usan `t_N` (informe de
normas (5)–(6), piezas) conservan su propio nivel; este `PASS` no las
promueve.

## 1. Enunciado

Con las definiciones de T1 §§1–2 y (13) (`T = C^_N L`, `L = D_xi/Lambda`,
`t_j = T^j s`, `x_j = P t_j`, `y_j = Q t_j`), fijados `W` admisible y
`Theta < infinito`:

> Para cada `W` admisible fijo y cada `Theta < infinito` existe `C(W,Theta)`
> tal que, para todo `N>=2`, todo perfil real
> `vartheta` con `||vartheta||_inf <= Theta`, todo encoder `M` y todo
> `0<=j<=N`, `||t_j||_2 <= C(W,Theta) ||s||_2 <= 2 C(W,Theta)`.

No hay uniformidad en `W` (ver §4, cierre): el cuantificador sobre `W` va
delante. La dependencia es `O_{W,Theta}(1)`, no `O_W(1)`: la constante contiene
`e^kappa` con `kappa = Theta (C_P + C_0 C_Q)`. `C_P, C_Q, K_D, C_0, rho_0,
rho_1` dependen de `W` y del símbolo, no de `N`, `j`, `M` ni `vartheta`.

## 2. Datos y constantes

- (E3) `C^_N = F C_N F^-1`, `C_N(x) = exp(-i vartheta(x/N) beta / N)`,
  `beta` hermítica e involutiva. Como `|e^{-i a}-1| <= |a|`,
  `E := C^_N - I` cumple `||E||_{2->2} <= Theta/N`. La moneda conmuta con
  `H_xi` (ambas son multiplicaciones en posición), y `F` es unitaria.
- (E4) `C_P = ess sup ||P(p)||`, `C_Q = ess sup ||Q(p)||` (T1 (3a)),
  `K_D = sup_p ||D_xi(p)|| / Lambda` (símbolo continuo en el toro).
  Normas de fibra: euclídea en `C^4`; la norma de un multiplicador en
  `L^2(T^3; C^4, dmu)` es el supremo esencial de la norma de fibra.
- (E1) En `W`, `D_xi = diag(S_xi, S_xi^-1)` y `P = diag(p_S, I-p_S)`;
  por (3a) y `det S_xi = 1`,
  `D_xi P = lambda P`, `D_xi Q = lambda^-1 Q`, con `|lambda| > 1`.
  Fuera de `W`, `P = 0`, `Q = I`. Luego `P D_xi Q = 0 = Q D_xi P`
  en casi todo punto, y `D_xi Q = Q D_xi Q`.
- (E2) `m(p) = lambda(p)/Lambda` en `W`, `m = 0` fuera. `lem:specrad`
  (TeX) da `rho(S(eta - i xi_*)) <= Lambda`; `lambda` es la raíz de
  módulo mayor, así que `|m| <= 1`. Es una cota **escalar**: no se usa
  como cota de la norma de ninguna matriz.
- `M(p) = Q(p) D_xi(p) Q(p) / Lambda`, multiplicador en momento.
  `||M(p)|| <= K_M := max(1,C_Q)^2 K_D`.

## 3. E5 ejecutado: norma `||.||_*`

**Separación espectral uniforme.**

- En `W`: de `D_xi Q = lambda^-1 Q` y `Q^2 = Q`, `M(p) = (lambda Lambda)^-1 Q(p)`,
  `M^h = (lambda Lambda)^-h Q`. Espectro contenido en
  `{0, (lambda Lambda)^-1}` y, como `|lambda| > 1` y `Lambda = e^{Phi_*} > 1`,
  `rho(M(p)) <= Lambda^-1 < 1`. No hace falta continuidad de la familia
  partida `p -> M(p)` a través de `partial W`. La compacidad que sí se
  usa dentro de `W` es la de los cierres `closure(W_alpha)` subset `O_alpha`,
  a través de `C_P` (T1 (3a)), y por tanto de `C_Q <= 1 + C_P` y `K_M`:
  la admisibilidad de `W` se paga ahí.
- Fuera de `W`: `M = D_xi/Lambda` y `rho(D_xi) = rho(S_xi)` (mismo
  espectro, `det S = 1`). `K = T^3 \ W` es compacto (W abierto) y no
  contiene ningún punto de `Sigma`, y `xi_* = t_* (1,1,1)` tiene todas
  las componentes no nulas: por `lem:specrad`, `rho(D_xi/Lambda) < 1` en
  cada punto de `K`. El símbolo es continuo y `rho` es continuo sobre
  matrices `4x4`, luego `r_ext := max_K rho(D_xi/Lambda) < 1`.
- `rho_0 := max{Lambda^-1, r_ext} < 1`, y `rho(M(p)) <= rho_0` para casi
  todo `p`. La frontera `partial W` pertenece a `W^c = K`
  (T1 §2, `W` abierto), de modo que queda cubierta por el caso exterior.
  No se usa que tenga medida nula.

**Resolvente sin diagonalizabilidad.** Se fija por convención
`rho_1 := (1 + rho_0)/2`, con lo que `C_0` y `C(W,Theta)` son funciones
bien definidas de `W`.
Para `|z| = rho_1`: `|det(zI - M)| >= (rho_1 - rho_0)^4`, y, para
matrices `4x4`, `||adj(A)|| <= ||A||^3` (los valores singulares de
`adj(A)` son productos de tres valores singulares de `A`). Con
`||zI - M|| <= rho_1 + K_M`,
`||(zI-M(p))^-1|| <= R := (rho_1+K_M)^3 / (rho_1-rho_0)^4`.
Sin número de condición ni base propia.

**Cauchy.** `M^h = (2 pi i)^-1 ∮_{|z|=rho_1} z^h (zI-M)^-1 dz`, luego
`||M(p)^h|| <= R rho_1^{h+1}` y, con `C_0 := max{1, R rho_1}`,
`||M^h||_{2->2} <= C_0 rho_1^h`.

**Norma.** Para `y in ran Q`, `||y||_* := sup_{h>=0} rho_1^-h ||M^h y||_2`.
Entonces `||y||_2 <= ||y||_* <= C_0 ||y||_2` y
`||M y||_* <= rho_1 ||y||_*` (desplazar el índice `h`).

## 4. Bloques, recurrencia y dato inicial

Como `T = (I+E) L`, `L x = m x in ran P` para `x in ran P`
y `L y = M y in ran Q` para `y in ran Q` (E1):

| Bloque | Identidad | Cota |
|---|---|---|
| `A_j` en `ran P` | `A_j x = m x + P E m x` | `||A_j x||_2 <= (1 + C_P Theta/N) ||x||_2` |
| `B_j`, `ran Q -> ran P` | `B_j y = P E M y` (porque `P D_xi Q = 0`) | `||B_j y||_2 <= rho_1 C_P Theta/N ||y||_*` |
| `C_j`, `ran P -> ran Q` | `C_j x = Q E m x` (porque `Q m x = 0`) | `||C_j x||_* <= C_0 C_Q Theta/N ||x||_2` |
| `D_j` en `ran Q` | `D_j y = M y + Q E M y` | `||D_j y||_* <= rho_1 (1 + C_0 C_Q Theta/N) ||y||_*` |

En `B_j`, `D_j` se usó `||M y||_2 <= ||M y||_* <= rho_1 ||y||_*`. Los
productos `P(p') Q(p)` con `p' != p` no se anulan: viven dentro de `E`
y se pagan con `||E|| <= Theta/N`. La identidad de `A_j` exige el orden
`T = C^_N L` (moneda después del bloque libre) de T1 (4).

Con `nu_j := ||x_j||_2 + ||y_j||_*`, de T1 (13),
`nu_{j+1} <= (1 + (a+c)/N) ||x_j||_2 + (rho_1 + rho_1 (a+c)/N) ||y_j||_*`,
con `a = C_P Theta`, `c = C_0 C_Q Theta`. Como `rho_1 < 1`, ambos
coeficientes son `<= 1 + kappa/N`, `kappa = a + c`, **para todo `N`** (no
se requiere `N >= N_0`; `rho_1 < 1` sólo se usa para que el coeficiente
de `||y_j||_*` no exceda `1`, y `rho_1 <= 1` bastaría aquí). Por tanto
`nu_j <= (1+kappa/N)^j nu_0 <= e^kappa nu_0` para `0 <= j <= N`.

**Dato inicial.** `s = F H_xi f`, `f = J(U_M - I) phi_N`, `||f|| <= 2`
(T1 (1)). En el soporte de Alice, `xi_* . (x - x_*) = sqrt(3) t_* (u^ . x - R) <= 0`
(`x_* = R u^`, `xi_* = sqrt(3) t_* u^`, `|x| <= R`), luego `||H_xi f|| <= ||f||` y
`||s||_2 <= 2`. `nu_0 <= (C_P + C_0 C_Q) ||s||_2`. Como
`t_j = x_j + y_j` y `||y||_2 <= ||y||_*`:

`||t_j||_2 <= nu_j <= e^kappa (C_P + C_0 C_Q) ||s||_2`, `kappa = Theta (C_P + C_0 C_Q)`.

Esto es el enunciado de §1 con `C(W,Theta) = (C_P+C_0 C_Q) e^{Theta (C_P+C_0 C_Q)}`.

**Formulación por norma equivalente (segunda vía).** Sobre todo `L^2`,
`nu(t) := ||P t||_2 + ||Q t||_*` cumple `||t||_2 <= nu(t) <= (C_P + C_0 C_Q) ||t||_2`,
y la tabla anterior afirma `||T||_{nu -> nu} <= 1 + kappa/N`; de ahí
`||T^j s||_2 <= (1+kappa/N)^j nu(s) <= e^kappa (C_P+C_0 C_Q) ||s||_2`, la
misma constante sin manejar la recurrencia acoplada. Se prueba
`sup_{j<=N} ||T^j|| < infinito`, no `||T^j|| -> 0`: el sector P no decae,
porque `m(0) = 1` en los saddles (`|m| <= 1` es exactamente lo que impide
crecimiento; una cota `rho(S) <= Lambda(1+eps)` con `eps` fijo daría
`e^{eps N}`).

**Controles.**
- `Theta = 0`: `E = 0`, `T = L`, `t_j = m^j x_0 + M^j y_0` y
  `||t_j||_2 <= ||x_0||_2 + C_0 rho_1^j ||y_0||_2 <= (C_P + C_0 C_Q) ||s||_2`,
  que coincide con la fórmula (y con `C_P + C_Q` no cerraría).
- Fibra de T1 (18) (saddle `p=0`, moneda constante, `a = theta/2`,
  `P = diag(1,0)`, `m = 1`, `L = diag(1, Lambda^-2)`,
  `I + E = [[cos a, -i sin a], [-i sin a, cos a]]`): la tabla da
  `A = cos a`, `B = -i sin a Lambda^-2`, `C = -i sin a`, `D = cos a Lambda^-2`,
  las cuatro entradas de `T` en (18). Es un contraste en una sola fibra:
  no dice nada sobre `P(p') Q(p)` con `p' != p` ni sobre las interfaces con
  `W^c`, que la cota `||E||_{2->2} <= Theta/N` paga globalmente.

**Sobre `W`.** `r_ext = max_K rho(D_xi/Lambda)` tiende a `1` al encoger `W`
(`K` se acerca a `Sigma`), y `C_P` crece al dilatar `W` hacia
`partial O_alpha` (el denominador `lambda - lambda^-1` en (3a) se degrada).
No hay uniformidad en `W` recuperable de esta prueba; cualquier uso con
`W = W_N` queda fuera de este enunciado.

## 5. Las tres reparaciones y la procedencia

Reparaciones incorporadas (las tres pedidas por el sanedrín):

1. Schur §2, (6): `||A_j|| <= 1 + C/N` es una cota **sobre `ran P`**, no sobre
   `L^2` entero (allí el bloque libre es `m P` con `||P||` posiblemente `> 1`).
   La premisa original `rho <= 1 + C/N => ||.|| <= 1 + C/N` se abandona.
2. Schur §2, antes de (5): el resolvente se controla por adjunta/determinante
   con dos ramas (`W` puntual, `K` compacto), no por continuidad de la
   familia partida.
3. `two-channel-reconstruction-operator-norms.md` §2: `nu_0` lleva
   `C_P + C_0 C_Q`, no `C_P + C_Q`.

Correcciones en los informes fuente: ver los avisos `[corregido 2026-09-25]`
en Schur §2 y en el informe de normas. Tras la revisión focalizada de §5 se
aplicaron además: `rho_1` fijado por convención, símbolo `lambda` del dato
inicial sustituido por `sqrt(3) t_*`, frase sobre compacidad recalibrada,
control de fibra T1 (18), cuantificador sobre `W` explícito.

Procedencia de las revisiones (herramientas: `~/herramientas` 18028a9,
`~/sanedrin` 8162508):

| Acta | Miembros (orden) | Resultado |
|---|---|---|
| `debates/2026-09-24--two-channel-stability-review.md` | Opus, ABNER | Opus `REPAIR_REQUIRED`; el turno de ABNER no llegó |
| `debates/2026-09-25--schur-repair-deepseek-review.md` | ABNER, Opus | ambos `PASS_WITH_REPAIRS`; ABNER: E5 no ejecutado, conclusión abierta hasta que conste E5 o la vía Dyson |
| `debates/2026-09-25--schur-repair-astra-review.md` | Astra (GPT), Ciro (Grok) | ambos `PASS_WITH_REPAIRS`; Astra ejecuta E5, Ciro la suscribe |
| `debates/2026-09-25--schur-e5-abner-check.md` | ABNER, Opus | ABNER `PASS` (E5 ejecutado; su objeción original queda cerrada), Opus `PASS`; sólo cuenta ABNER como independiente. Reparaciones menores (fijar `rho_1`, renombrar `lambda`, frase de compacidad, control T1 (18)) aplicadas arriba |

La vía Dyson de Opus (`||T^N|| <= C_1 e^{C_1 K_D Theta}`, con
`C_1 = sup_a ||T_0^a||`) no se usa aquí y sigue sin reproducir por otro
revisor.

## 6. Límites

- Esta nota es una derivación por escrito; no incluye comprobación
  numérica. Las identidades de bloque sólo se han contrastado en la fibra de
  T1 (18); `[UNVERIFIED]` numéricamente fuera de ella.
- La revisión cubrió exclusivamente §1–§4 (ABNER lo declara así); no cubrió
  interfaces con `W^c` en piezas físicas, ni Schur (7)–(8).
- Se usan como fuente `lem:specrad`, `lem:symbol` del TeX y T1 §§1–2, (3a),
  (4), (13) sin reabrirlos.
- No implica `||M_N|| = O_W(N^-1)` ni ninguna cota física; ninguna
  transferencia a los extremos físicos ni a `A_cP`, `A_cQ`.
