# NARROW_BAND_SIGNALING_GATE — ejecución preregistrada

**Veredicto: `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`.**
Razón, en la lista de §10 del contrato: **incompatibilidad del encoder con el
criterio IR**. La stop rule de §7 se activó en el primer control: la fracción
de la diferencia codificada que queda fuera de la banda cumple
`eta_enc(Lambda) -> 1`, no `-> 0`. No se calculó `D_B`.

Ejecución del contrato
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md) en el
orden de su §13. El contrato no se modificó. No hubo commit ni push, y
`state/CURRENT_STATE.md` no se promovió. Certificado exacto:
[`scripts/verify_narrow_band_gate.py`](../scripts/verify_narrow_band_gate.py),
**34/34 comprobaciones exactas**.

Convención de este informe: **[V]** marca una identidad o un límite que el
certificado comprueba con aritmética exacta. **[A]** marca un paso analítico
que se prueba aquí mismo a partir de pasos [V]. No se usó cuadratura,
coma flotante ni malla como evidencia.

## 1. Preflight

| Elemento | Resultado |
| --- | --- |
| `HEAD` | `817050d8e80e6d6e636937b5794d60ff67e6e047` |
| `origin/research/b-infinity-post-s4-gate` | idéntico tras `git fetch` y `git ls-remote`: `BASELINE_MATCH` |
| Commit de "enmienda administrativa del encabezado" | **no existe** en ninguna ref local ni remota (§13.1) |
| Charter | publicado en `817050d`, único commit que lo toca; blob `5ef52c4a…`, sha256 `3d559ced…41ba9`; `git diff` vacío |
| Cambios tracked antes de ejecutar | ninguno |
| Untracked preexistentes | cuatro (`Auditoría De Novedad Matemática.md`, dos `.log` de `debates/`, `scripts/__pycache__/`); **sin tocar**, todo Python con `PYTHONDONTWRITEBYTECODE=1`, mtimes de `__pycache__` intactos (08:45:20) |
| Leídos íntegros | el charter; `reports/2026-09-17--physical-dimensional-translation-audit.md`; `theory/ALICE_LOCAL_PREPARATION_WITNESS.md`; `theory/NONCORNER_SIGNALING_GATE.md`; DP14, BDP17 y BB93 de `biblioteca/`, con sha256 igual a los de §14 del charter |
| Inspeccionados para reutilizar | `walk2`, `laurent`/`is_zero`, `verify_local_preparation`, `verify_noncorner_gate` (en `verify_directional_saturation.py`); `exact_blocks`, `evolve`, `reduced_state` (en `verify_signaling_witness.py`); `scripts/README.md` |

La ejecución se hizo sobre el único HEAD remoto existente. Su contenido
científico es el que fue preregistrado. El encabezado no enmendado se reporta
en §13 y no se corrigió.

## 2. Clase preregistrada (sin reinterpretar)

- Modelo: CAR libre de CJWW (5.15), sector de una partícula, `S = W^dagger`.
  Convención de Fourier de §2 del charter:
  `hat psi(p) = sum_x e^{i p.x} psi(x)`, inversa con signo negativo,
  `dmu = d^3p/(2 pi)^3` sobre `B = [-pi,pi)^3`.
- Nodo único `p = 0`, con `W(0) = I` **[V]**.
  `H_W = p1 sigma1 - p2 sigma2 + p3 sigma3` como término lineal de `W` **[V]**,
  `H_W^2 = |p|^2 I` **[V]** y `c_IR = 1`. Se conservan ambas ramas; no hay
  proyector de helicidad.
- `Pi_Lambda = F^{-1}[1_{|p|<=Lambda} I_2] F`, con `0 < Lambda < pi/4` y
  límite `Lambda -> 0`.
- Envolvente `g(q) = (1-|q|^2)^2 1_{|q|<1}`, con `g(1) = g'(1) = 0` **[V]**.
  `hat phi_Lambda = Z_Lambda^{-1/2} g(p/Lambda) (0,1)^T`, espín `down`, fase
  real.
- Recurso al elegir: `psi_Lambda = S^2 phi_Lambda`, con dos pasos comunes.
- Alice en `A = (T=0, x=0)`: `U_0 = I` o `U_1 = e^{i pi n_0} = I - 2 P_0`, con
  `P_0 = |0><0| (x) I_2`.
- Después: `S^n U_b psi_Lambda`, `n = 0, 1`. Bob en `y_B = (1,1,0)`, con
  `Delta T = 1`.

Sólo `Lambda` varía, y nunca se eligió un valor: todas las afirmaciones son
uniformes en `(0, pi/4)` o asintóticas. Las historias previas a la elección
son idénticas por construcción: ambas son `S^j phi_Lambda`, `j = 0, 1, 2`, y el
bit sólo entra en `T = 0`.

**Carta (§3, §13.1).**

*Lema 1* **[A]**: si `|p| < pi/2`, entonces `c1 c2 c3 >= cos|p|`.

Prueba. La función `h(u) = log cos sqrt(u)` es cóncava en `[0, (pi/2)^2)`,
porque `h''(u) = -(2t - sin 2t)/(8 t^3 cos^2 t)` con `t = sqrt(u)`, y
`2t - sin 2t` vale cero en `0` y tiene derivada `4 sin^2 t >= 0` **[V]**.
La suma `sum_i h(p_i^2)` es entonces cóncava sobre el símplex
`{u_i >= 0, sum u_i = |p|^2}` y alcanza su mínimo en un vértice:
`sum_i h(p_i^2) >= h(|p|^2) + 2 h(0) = log cos|p|`.

Consecuencias en `|p| < pi/4`:

- `tr W/2 = c1 c2 c3 ∈ (cos(pi/4), 1]` **[V]** para la traza. Vale `1` sólo
  en `p = 0`.
- Las eigenfases `±omega`, con `omega = arccos(c1 c2 c3) ∈ [0, pi/4)`, no
  tocan otro nodo (`W = ±I` exige `omega ∈ {0, pi}`) ni el corte del
  logaritmo (`omega = pi`).
- `2 c1^2 c2^2 c3^2 - 1 >= 2cos^2|p| - 1 = cos 2|p| > 0` **[V]** para la
  identidad.

Hay una ruta elemental independiente para `|p| <= 1/sqrt2`:
`cos^2 x >= 1 - x^2` y `prod(1 - a_i) >= 1 - sum a_i` **[V]**. Da
`2 prod c_i^2 - 1 >= 1 - 2|p|^2`, que es `> 0` en `|p| < 1/sqrt2`.

## 3. Control pre-elección (§6)

**(a) Soporte espectral exacto por construcción.** `hat phi_Lambda` tiene
soporte en la bola abierta, y `S^j` y `Pi_Lambda` son operadores de
multiplicación en `p`, así que conmutan. Por tanto

`epsilon_pre(j, Lambda) = 0` exactamente, para `j = 0, 1, 2`.

Normalización: `Z_Lambda = 64 Lambda^3/(3465 pi^2)` **[V]**.

**(b) Error respecto de la dinámica Weyl.**

*Lema 2* **[A]**: `r_W(Lambda) <= R_W(Lambda) := 3 Lambda^2 (1/2 + sqrt(1/2 + 25 Lambda^2/18))`.
En la carta, además, `R_W(Lambda) < 5 Lambda^2` **[V]**, usando
`pi < 22/7` por la integral de Dalzell **[V]**.

Prueba en cuatro pasos:

1. `W - I - i H_W` se descompone por entradas en restos de Taylor **[V]**:
   - diagonal: `(c1 c2 - 1) e^{±i p3} + (e^{±i p3} - 1 ∓ i p3)`;
   - fuera de la diagonal: `∓(c1 - 1) s2 ∓ (s2 - p2) + i(s1 - p1)`.
2. Los restos integrales **[V]** dan `|e^{ix} - 1 - ix| <= x^2/2`,
   `|cos x - 1| <= x^2/2` y `|sin x - x| <= |x|^3/6`. Con
   `|c1 c2 - 1| <= (p1^2 + p2^2)/2` y `|s2| <= |p2|`, cada entrada diagonal
   está acotada por `Lambda^2/2` y cada entrada fuera de la diagonal por
   `5 Lambda^3/6`. La norma de Frobenius da
   `||W - I - i H_W|| <= Lambda^2 sqrt(1/2 + 25 Lambda^2/18)`.
3. `H_W` es hermítico con autovalores `±|p|`, así que
   `||e^{i H_W} - I - i H_W|| <= Lambda^2/2`. Tomando adjuntos,
   `||S - e^{-i H_W}|| = ||W - e^{i H_W}||`.
4. Por telescopio **[V]**,
   `||S^j - e^{-ij H_W}|| <= j ||S - e^{-i H_W}||` para `j <= 3`.

Traslado a estados, sin factores ocultos: `hat phi` tiene soporte en la bola,
así que `||S^j phi - e^{-ij H_W} phi|| <= r_W`. La distancia de traza entre
estados puros satisface `|| |a><a| - |b><b| ||_1 <= 2 ||a - b||`, y la
reducción a cualquier subsistema local es contractiva en norma de traza. Con
esto la preparación queda Weyl-controlada en el sentido de §6, con una
constante explícita (`R_W -> 0`), y no sólo porque su soporte esté dentro de
`Lambda`.

**(c) Aproximaciones.** No hubo ninguna. La única cantidad sin forma cerrada
es `c_down(Lambda)` (§4.2), y está acotada analíticamente por ambos lados.

**Presupuesto absoluto de §6**, incluyendo las etapas posteriores a la
elección (§4.5):

- `epsilon_0(n, Lambda) = 0`;
- `epsilon_1(0, Lambda) = 4 s(1 - kappa)` **[V]**;
- `epsilon_1(1, Lambda) = epsilon_1(0, Lambda)`, porque `[S, Pi_Lambda] = 0`
  y `S` es unitario;
- `epsilon_UV = 4 s(1 - kappa) <= 11 Lambda^3/(35 pi^2)`;
- `epsilon_IR <= 5 Lambda^2 + sqrt(11/35) Lambda^{3/2}/pi -> 0`.

**§6 se cumple, pero es necesario y no suficiente** (§§4–5).

## 4. Codificación: primer candado (§7)

### 4.1 Qué introduce la operación puntual en el espectro

Se tiene `U_1 - I = -2 P_0`. Con la convención de §2,
`(P_0 psi)^(p) = psi(0) = int_B hat psi dmu` para **todo** `p ∈ B`. El núcleo
de `P_0` en momento es la constante `I_2` sobre `B x B`: toma cualquier estado
y devuelve un vector de **densidad espectral plana** en toda la zona de
Brillouin. Por eso `[Pi_Lambda, P_0] != 0`.

*Lema 3* **[A]**: para `v ∈ C^2`, `||Pi_Lambda (delta_0 (x) v)||^2 = kappa(Lambda) ||v||^2`,
con `kappa(Lambda) = Lambda^3/(6 pi^2)` **[V]**. La fracción dentro de la
banda de cualquier vector de un solo sitio es la medida de la bola, que tiende
a `0`.

### 4.2 Amplitud en el sitio de Alice

Sea `c(Lambda) := psi_Lambda(0)`. Por Cayley–Hamilton, `S^2 = 2 f S - I` con
`f = c1 c2 c3` **[V]**, y

`S^2 |down> = ( 2 c1^2 c2 c3 s2 - 2i f s1 ,  (2 c1^2 c2^2 c3^2 - 1) + 2i c1^2 c2^2 c3 s3 )` **[V]**.

La componente superior es suma de un término impar en `p2` y otro impar en
`p1`. La parte imaginaria inferior es impar en `p3`, y la parte real inferior
es par en las tres coordenadas **[V]**. Como `g` es radial y la bola es
simétrica, las partes impares integran cero **[A]**:

`c(Lambda) = (0, c_down)`, con `c_down = Z^{-1/2} int g(p/Lambda) (2 c1^2 c2^2 c3^2 - 1) dmu ∈ R`.

*Lema 4* **[A]**: para `0 < Lambda < pi/4`,
`cos(2 Lambda) A(Lambda) <= c_down(Lambda) <= A(Lambda)`, con
`A = Z^{-1/2} int g dmu = sqrt(3465) Lambda^{3/2}/(210 pi)` **[V]**.

Prueba: sobre el soporte de `g`, el Lema 1 da
`cos 2Lambda <= 2 prod c_i^2 - 1 <= 1`.

Por tanto `s(Lambda) := ||P_0 psi_Lambda||^2 = c_down^2` satisface

`cos^2(2 Lambda) 11 Lambda^3/(140 pi^2) <= s(Lambda) <= 11 Lambda^3/(140 pi^2) < kappa(Lambda)` **[V]** para las constantes,

y, en particular, `0 < s < 1`, `s ~ 11 Lambda^3/(140 pi^2)` y
`s/kappa -> 33/70`.

### 4.3 La diferencia global `Delta_Lambda`

Sean `e := P_0 psi = delta_0 (x) c` y `f := psi - e`, con `e ⊥ f`. Como
`U_1 psi = psi - 2e`,

`Delta_Lambda = |psi - 2e><psi - 2e| - |psi><psi| = -2(|e><f| + |f><e|) = -2(P_0 rho_0 Q_0 + Q_0 rho_0 P_0)`,

`||Delta_Lambda||_1 = 4 sqrt(s(1 - s)) > 0` para todo `Lambda ∈ (0, pi/4)` **[V]**.

**La convención `Delta = 0` de §7 no se activa en ningún punto de la carta.**

### 4.4 Reducción exacta a tres dimensiones

`Pi_Lambda psi = psi`, porque el soporte es exacto. Sean `e_in = Pi e` y
`e_out = (I - Pi) e`. El subespacio `V = span{psi, e_in, e_out}` es invariante
bajo `Pi`. `Delta`, `L = Pi Delta Pi` y `R = Delta - L` tienen rango y soporte
en `V`, y se anulan en `V^⊥`. Sus normas de traza quedan fijadas por los datos
de Gram, que son reales:

`<psi|psi> = 1`, `<psi|e_in> = <Pi psi|e> = <psi|P_0 psi> = s`,
`||e_in||^2 = kappa s` (Lema 3), `||e_out||^2 = (1 - kappa) s`, y los demás
productos valen `0`.

El certificado realiza estos datos en coordenadas ortonormales reales **[V]**.
Con `w := Pi U_1 psi = psi - 2 e_in` y `h := (I - Pi) U_1 psi = -2 e_out`:

- `L = |w><w| - |psi><psi|`;
- `R = |w><h| + |h><w| + |h><h|`.

### 4.5 Normas y cociente

Los tres operadores tienen `det = 0` en `V` y
`e2 = (tr^2 - tr X^2)/2 <= 0`, que valen respectivamente `-4s(1-s)`,
`-4s(kappa - s)` y `-4s(1-kappa)(1 - 4s(1-kappa))` **[V]**. Por eso
`||X||_1 = sqrt(tr^2 - 4 e2)`:

| Cantidad | Valor exacto |
| --- | --- |
| `\|\|Delta_Lambda\|\|_1` | `4 sqrt(s(1-s))` **[V]** |
| `\|\|L\|\|_1 = \|\|Pi Delta Pi\|\|_1` | `4 sqrt(s^2(1-kappa)^2 + s(kappa-s))` **[V]** |
| `\|\|Delta - Pi Delta Pi\|\|_1` | `4 sqrt(s(1-kappa)(1 - 3s(1-kappa)))` **[V]** |
| `eta_enc(Lambda)` | `sqrt( (1-kappa)(1 - 3s(1-kappa)) / (1-s) )` **[V]** |
| fuga absoluta `epsilon_1(0, Lambda)` | `4s(1-kappa) <= 11 Lambda^3/(35 pi^2) -> 0` **[V]** |

### 4.6 Cotas y límite

Para `0 < s <= kappa < 1/3`, los numeradores de `1 - eta^2` y de
`eta^2 - (1-kappa)(1-3kappa)`, que son `kappa - s + 3s(1-kappa)^2` y
`3(1-kappa)(kappa - s(1-kappa)) + s(1-kappa)(1-3kappa)`, son `>= 0` **[V]**.
Por tanto

`(1 - kappa)(1 - 3 kappa) <= eta_enc(Lambda)^2 <= 1`.

En toda la carta, `kappa < pi/384 < 11/1344`, y el suelo es decreciente con
`floor(11/1344) = 1747563/1806336 > 24/25` **[V]**. Queda

**`eta_enc(Lambda) > 2 sqrt(6)/5 ≈ 0.98` para todo `Lambda ∈ (0, pi/4)`**,

y, por compresión entre las dos cotas, **`lim_{Lambda->0} eta_enc(Lambda) = 1`**
**[V]**. En sentido complementario,
`||L||_1/||Delta||_1 <= sqrt(kappa/(1-kappa)) -> 0` **[V]**.

Lectura física. Al estrechar la banda, el recurso se extiende sobre unos
`Lambda^{-3}` sitios, y su amplitud en Alice cae como `Lambda^{3/2}`. La puerta
de un solo sitio escribe el bit en la dirección `e = delta_0 (x) c`, cuyo
espectro es plano: sólo una fracción `kappa ~ Lambda^3` de esa dirección cae
dentro de la banda. `||Delta||_1 ~ (4/pi) sqrt(11/140) Lambda^{3/2}` tiende a
cero, igual que la fuga absoluta, porque toda la intervención se hace pequeña.
Pero la fracción de la diferencia codificada que vive fuera de la banda tiende
a **1**. Es exactamente el escenario que §7 fue diseñado para detectar: pasar
§6 en norma absoluta ocultaría una codificación esencialmente UV.

**Observación estructural, que no amplía el veredicto.** La fórmula de
`eta_enc` sólo usa de la familia congelada dos cosas: `Pi_Lambda psi_Lambda = psi_Lambda`
y `s(Lambda) ∈ (0, 1)`. La cota inferior `(1-kappa)(1-3kappa)` no depende de
`s`. La envolvente, el espín y los dos pasos comunes sólo entran a través de
`s > 0`. No se examinaron otras preparaciones: recursos sin soporte espectral
exacto, puertas no puntuales u otras operaciones locales quedan fuera.

## 5. Stop rule

**§7: FAIL. Declarado antes de cualquier `D_B`.**

La incompatibilidad está demostrada en todo entorno perforado del origen, con
cualquiera de las dos lecturas de la frase: `||Delta_Lambda||_1 > 0` y
`eta_enc > 2 sqrt(6)/5` en **toda** la carta, y el límite vale `1`. Es una
identidad exacta con cota inferior explícita, no una cota débil ni una prueba
fallida. Conforme a §7 y §13.2: no se construyó `Delta(1)`, ni `rho_B`, ni
`D_B`, ni el presupuesto de §8; no se cambiaron la puerta, la familia, el
perfil ni el criterio.

## 6. Propagación

**No procede** (stop rule).

## 7. Bob

**No procede.** No se calcularon `D_B(Lambda)` ni ningún efecto `E_B`. La
re-certificación geométrica de `y_B` y la igualdad de los estados de Bob en
`0^+` tampoco se ejecutaron, porque no intervienen en la obstrucción.

## 8. Límite IR

**Demostrado** (analítico, con certificado exacto):

- `eta_enc(Lambda) -> 1`;
- `||Delta_Lambda||_1 -> 0` como `Lambda^{3/2}`;
- `||L||_1/||Delta||_1 -> 0`;
- `epsilon_pre = 0`, `epsilon_UV -> 0` y `R_W -> 0`.

**No establecido:** nada sobre `D_B(Lambda)`. De las cuatro opciones pedidas
sólo cabe la 4, "no determinado", y no por falta de análisis sino porque la
stop rule lo excluye. Según §10, una prueba de incompatibilidad **no afirma
`D_B = 0`** para el walk. `Lambda -> 0` es un límite espectral de la familia,
con sitio y número de pasos fijos; no equivale a `a, tau -> 0`.

**Evidencia numérica:** ninguna se usó. Como comprobación de cordura efímera,
no retenida y sin papel probatorio, un análogo en un toro finito (`N = 12`, un
único `Lambda = 0.7`, matrices densas en coma flotante) reprodujo las fórmulas
cerradas de §4.5 con error de redondeo del orden de `1e-15`.

## 9. Veredicto

**`NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`**, por incompatibilidad del
encoder con el criterio IR de §7.

Estados en el orden de la tabla de §10:

- las filas 1 y 2 exigen todos los criterios positivos, y el 9.1 queda
  refutado;
- la fila 3 se aplica, porque hay una obstrucción probada para toda la
  familia asintótica;
- la fila 4 queda excluida, porque hay obstrucción y no se trata de cotas
  insuficientes.

Sobre la nomenclatura: el charter nombra la primera fila
`IR_SIGNALING_NONZERO_BUT_VANISHES_AS_LAMBDA_TO_ZERO` y rechaza
expresamente `IN_CONTINUUM_LIMIT` (§10). No afecta a este veredicto.

## 10. Techo de reclamo

- El witness `3/128` pertenece al protocolo ultralocal cerrado y permanece
  **cerrado e inalterado**. Este gate no lo recalculó ni lo usó como objetivo
  (§11 del charter), y sus verificadores pasan sin cambios (§12).
- Este negativo **no refuta** `3/128`,
  `ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED` ni
  `NONCORNER_SIGNALING_CONSTRUCTED`. Lo que establece es que ese mecanismo,
  con una puerta de un solo sitio sobre este recurso de banda estrecha, no
  queda dentro del régimen IR según el criterio preregistrado.
- Un positivo tampoco habría constituido una predicción experimental.
- El negativo **sólo vale para la clase congelada**: nodo `p = 0`, envolvente
  `g`, espín `down`, dos pasos, `U_1 = e^{i pi n_0}` en el origen, `y_B`,
  `Delta T = 1` y el criterio `eta_enc` de §7. No vale bajo otras nociones de
  control IR (§15), ni para puertas extendidas, suavizadas o dependientes de
  `Lambda`, ni para recursos sin soporte espectral exacto.
- No es una imposibilidad general, no afirma `D_B = 0` y no toca la
  microcausalidad del modelo.
- **No se ha fijado escala absoluta.** Se mantiene
  `DIMENSIONAL_MAP_CONDITIONAL`: no hay `a`, `tau`, eV, metros, segundos ni
  escala de Planck. `Lambda -> 0` no es `a, tau -> 0`.
- DP14, BDP17 y BB93 sólo motivaron la expansión Weyl. Todas las constantes
  (`R_W`, `kappa`, `Z_Lambda`, cotas de `s`) se derivaron aquí para CJWW
  (5.15); ninguna propiedad de esos walks se transfirió.

## 11. Cambios de código

| Archivo | Estado | Motivo |
| --- | --- | --- |
| `scripts/verify_narrow_band_gate.py` | **nuevo**, untracked, sha256 `23be80f2…8d4586` | certificado exacto de los pasos 0–2 |
| `reports/2026-09-17--narrow-band-signaling-gate.md` | **nuevo**, untracked | este informe |

Por qué un script nuevo:

1. `scripts/README.md` exige código generador permanente y trazado para todo
   resultado retenido, y la sección IMPLEMENTACIÓN de la instrucción de
   ejecución lo autoriza con justificación.
2. Los helpers `exact_blocks`, `evolve` y `reduced_state` sólo representan
   estados de soporte espacial finito. El paquete de banda estrecha es
   extendido, y §13 del charter prohíbe truncarlo sin control.
3. Añadir un flag a `verify_directional_saturation.py` alteraría los bytes de
   un verificador revisado que respalda witnesses congelados. §13 fija que
   esos verificadores conservan sus bytes.

Se reutilizaron por importación, en sólo lectura, `walk2`, `is_zero`
(`laurent`), `C`, `S`, `PS` y `PAULI`. **No se modificó ningún archivo
tracked**: charter, `CURRENT_STATE.md`, verificadores revisados (sha256
inalterados) y `scripts/README.md`, cuya entrada queda pendiente de una
decisión de congelación.

## 12. Validación

| Comprobación | Resultado |
| --- | --- |
| `python3 scripts/verify_narrow_band_gate.py` | **34/34 exact checks passed**, exit 0 (Python 3.12.3, SymPy 1.14.0) |
| Fallo en cerrado | tres mutaciones del objetivo (coeficiente de `\|\|R\|\|_1`, constante `11/140`, suelo `24/25 -> 49/50`) → `[FAIL]`, exit 1 |
| `verify_directional_saturation.py` | 27/27, exit 0 |
| `… --local-preparation-only` (witness `3/128`) | 21/21 exact, exit 0 |
| `… --noncorner-gate-only` | 20/20 exact, `NONCORNER_SIGNALING_CONSTRUCTED`, exit 0 |
| `verify_signaling_witness.py` | 17/17 exact, exit 0 |
| `verify_weyl_dirac_gate.py` | PASS, 375 exact checks, exit 0 |
| `cert_Aa_s4_counterexample.py` / `review_Aa_s4_exact.py` | `PASS` / `PASS`, exit 0 |
| `git diff --check` (tracked) | vacío; no hay cambios tracked |
| `git diff --no-index --check` sobre los dos archivos nuevos | vacío |
| Untracked preexistentes | intactos |

## 13. Observaciones sobre el charter (reportadas, no reparadas)

1. **Encabezado sin enmendar.** Las líneas 3–7 siguen diciendo "sobre
   `HEAD=11efe1f` y el remoto científico `780ecb0`. Su publicación/versionado y
   su ejecución quedan pendientes". El archivo está publicado en `817050d`, y
   no existe en el remoto el commit de enmienda administrativa que la
   instrucción daba por hecho. No afecta al contenido científico.
2. **Signo de Fourier.** §2 usa `e^{+i p.x}`, opuesto a CJWW (2.1) tal como
   lo cita la auditoría dimensional. Es una convención declarada y coherente
   con `K_t` y con `evolve`. `eta_enc` es invariante bajo `p -> -p`, porque
   `Pi` es radial y el espectro de un vector de un solo sitio es plano, así
   que no influye en el veredicto.
3. **Ambigüedad de "en todo entorno perforado del origen"** (§7). Puede
   leerse como "en cada entorno" o como "uniforme en un entorno". El
   resultado satisface ambas lecturas (cota uniforme en toda la carta y
   límite `1`).
4. **Tensión procedimental.** §13 dice "no se crea un script nuevo salvo
   necesidad demostrada y autorización", mientras `scripts/README.md` exige
   código trazado para todo resultado retenido. Se resolvió con la
   autorización condicionada de la instrucción (§11 de este informe).
5. **El diseño anticipó el resultado sin ser un error.** El control absoluto
   de §6, por sí solo, habría aceptado una codificación esencialmente UV;
   §7 existe precisamente para eso, y aquí fue decisivo.

No se detectó ningún error que invalide el contrato.
