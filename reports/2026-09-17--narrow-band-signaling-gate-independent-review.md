# Revisión independiente: NARROW_BAND_SIGNALING_GATE

**Fecha:** 2026-09-17. **Rama:** `research/b-infinity-post-s4-gate`.

**Veredicto de revisión: `PASS_WITH_MANDATORY_REPAIRS`.** Hay una reparación
obligatoria, **MR1**, de texto de alcance (informe, líneas 358–361). No cambia
ninguna cantidad ni el veredicto científico.

**Veredicto científico revisado:** `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`,
por incompatibilidad del encoder con el criterio IR de §7. **Correcto.**

**Estado congelable hoy:** `PARTIAL_REVIEW_PASS_WITH_REPAIRS / INDEPENDENT_REVIEW_PENDING`
(ver §14).

## 0. Independencia y convenciones de evidencia

**Contexto.** Esta revisión se hizo desde un contexto nuevo, **sin acceso a la
conversación** que ejecutó el gate, lo reparó y escribió las dos revisiones
previas. Sólo se leyeron archivos. Esas dos revisiones se trataron como
objetos que auditar, no como autoridad.

Límite de ciego. El mensaje de encargo ya enunciaba las fórmulas objetivo
(`kappa`, `Z`, `s`, `||Delta||_1`, `eta_enc`). Mi derivación es propia, pero no
ciega a los valores reclamados.

**Orden seguido:**

1. charter íntegro;
2. `walk2()` y convenciones de `verify_directional_saturation.py` (líneas 1–85);
3. `PROJECT_INSTRUCTIONS.md`;
4. derivación a mano y script exacto propio;
5. **sólo después**, informe (pre y post reparación), certificado y revisiones previas.

No se consultaron los PDFs de `biblioteca/`: ninguna inferencia del veredicto
depende de ellos. Sí se verificaron sus sha256 contra §14 del charter
(coinciden).

**Etiquetas de evidencia usadas en este informe:**

| Etiqueta | Significado |
| --- | --- |
| **[M]** | demostrado a mano en esta revisión |
| **[C]** | comprobado con código SymPy exacto propio: `scratchpad/independent-review/own_derivation.py`, 27/27, sin importar nada de `scripts/`; efímero, fuera del repo |
| **[X]** | ejecutado u observado: comandos git, ejecución de scripts, instrumentación, mutaciones sobre copias |
| **[L]** | sólo leído, no verificado independientemente |

El código propio es apoyo de revisión, no evidencia retenida del resultado
(`scripts/README.md`, l. 82–84). El resultado descansa en la prueba analítica.

**Entradas revisadas (sha256):**

| Archivo | sha256 |
| --- | --- |
| `theory/NARROW_BAND_SIGNALING_GATE.md` | `3d559cedefa0b6c25bd0af7ef13a993e2b71e1a8f7f97ae4f29f988147541ba9` |
| `reports/2026-09-17--narrow-band-signaling-gate.md` (reparado) | `06828d5c49eb160ffbc3fbda83bcddff18d7672faacda24e249409a80fe9600d` |
| copia pre-reparación (scratchpad) | `5d3e7125f5dcae1ec445e3a0ac6dafc70636da89e1c411ca34111ab6a5445f8e` |
| `scripts/verify_narrow_band_gate.py` | `23be80f2dad55313eb7f0fc88a9dd4429666af3fb2172b10f17ac0951b8d4586` |
| self-review | `69d600a2642304584e8fc912e3c0dba972516ac4fc9bfbc891671d3abecc4927` |
| segunda revisión | `d3a24a4a7830ee4c3dfd55312d0b66e209d4008997e68f1dc2f3fbeef8922316` |
| `scripts/verify_directional_saturation.py` | `1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596` |
| `scripts/verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |

## 1. Integridad del preregistro

### 1.1 Preflight [X]

| Elemento | Resultado |
| --- | --- |
| `HEAD` | `817050d8e80e6d6e636937b5794d60ff67e6e047` |
| `origin/research/b-infinity-post-s4-gate` | `817050d8e80e6d6e636937b5794d60ff67e6e047`; `git ls-remote` (sólo lectura, sin `fetch`) da el mismo hash |
| Tracked | sin cambios (`git diff` y `git diff --cached` vacíos), antes y después de esta revisión |
| Untracked preexistentes | `Auditoría De Novedad Matemática.md`, dos `.log` de `debates/`, `scripts/__pycache__/` (mtimes 08:45:20, intactos) |
| Untracked del gate | informe, certificado, self-review y segunda revisión; más este informe |
| Commit que publicó el charter | `817050d`, 2026-09-17 09:52:56, padre `11efe1f`; push registrado en reflog de `origin/...` a las 09:53:02 |
| Commits que tocan el charter | `git log --all` devuelve sólo `817050d` |
| Bytes | `git show 817050d:…` = archivo de trabajo = sha256 `3d559ced…`; blob `5ef52c4a…` |
| Commit de reparaciones R1–R4 | **no existe**; ni el informe ni el certificado han estado nunca en ninguna ref |

### 1.2 Cronología

Sólo el charter tiene ancla git. El resto son tiempos del sistema de
archivos [X], que no son criptográficos:

| Evento | Hora |
| --- | --- |
| charter: commit / push | 09:52:56 / 09:53:02 |
| certificado: birth / modify | 10:09:08 / 10:12:21 |
| informe pre-reparación: mtime | 10:14:08 (conservado en la copia; la copia nació a las 11:03:55) |
| self-review | 10:28:52 |
| segunda revisión | 10:47:31 |
| informe reparado: birth = modify | 11:05:12 |

El archivo del informe se reescribió como inodo nuevo, así que el repo ya no
conserva el tiempo de nacimiento original (10:14). Esa fecha sobrevive sólo en
el mtime de la copia del scratchpad y en el texto de la segunda revisión.

### 1.3 Clase ejecutada = clase congelada [M/L]

Comparé el informe con el charter elemento por elemento:

- CJWW (5.15), una partícula, `S = W^dagger`;
- Fourier `e^{+ip.x}` con `dmu = d^3p/(2pi)^3`;
- nodo `p = 0`;
- `Pi_Lambda` con bola cerrada, ambas componentes;
- `g = (1-|q|^2)^2 1_{|q|<1}`, espín `down`, fase real;
- `psi = S^2 phi`;
- `U_1 = e^{i pi n_0} = I - 2P_0` en el origen, `n = 0, 1`;
- Bob `(1,1,0)`, `Delta T = 1`;
- carta `0 < Lambda < pi/4`;
- criterio `eta_enc -> 0` y convención `Delta = 0`.

Todo coincide. Ni el perfil, ni el nodo, ni el encoder, ni Bob, ni los tiempos,
ni el proyector, ni los criterios IR cambiaron después de ver resultados.

Lo único fijado después del cálculo son constantes de cota: `2 sqrt6/5` y
`R_W < 5 Lambda^2`. Son artefactos de la prueba y el criterio no depende de
ellas: el criterio es `eta_enc -> 0`, y la refutación sólo necesita que
`eta_enc` no tienda a `0`.

La cordura flotante en toro (`N = 12`, `Lambda = 0.7`), declarada en el
informe §8, fue previa al certificado. No fijó ningún parámetro ni aporta
evidencia.

### 1.4 Reparaciones R1–R4 frente a la ejecución [X]

Ambos hashes verificados: pre-reparación `5d3e7125…` y reparado `06828d5c…`.
El `diff -u` completo muestra sólo:

- (a) cambios de etiqueta `[V]` → `[V]` + `[A]`;
- (b) sustitución de las frases de R1 y R2;
- (c) nuevo texto de R3;
- (d) párrafo "Estructura del residuo [A]";
- (e) "Cobertura real" y "Hechos del entorno" en §12;
- (f) §14, registro de reparaciones.

**Ninguna fórmula, cantidad, parámetro, regla, criterio ni veredicto cambió.**
Las reparaciones son posteriores a la ejecución (11:05 > 10:14) y a ambas
revisiones (10:28, 10:47). Tocan sólo alcance, redacción y certificación, con
una excepción de contenido factual en R3 (§10, MR1).

### 1.5 Encabezado del charter (líneas 3–7)

Dice "sobre `HEAD=11efe1f` y el remoto científico `780ecb0`… publicación y
ejecución pendientes" y `NOT_EXECUTED / OUTCOME_OPEN`. Era exacto al redactar:
`11efe1f` es el padre de `817050d`, y el remoto estaba en `780ecb0` hasta el
push. Quedó desactualizado tras publicar y ejecutar.

**Decisión independiente:** no altera el contrato científico. §§1–15 son byte a
byte el blob empujado antes de cualquier artefacto de cálculo, y el encabezado
no define cantidades, reglas ni estados terminales. Es un defecto
administrativo que debe corregirse en un acto separado, nunca en la
congelación de este resultado.

### 1.6 ¿Limita la ausencia de commit lo que puedo certificar?

**Sí, en la cronología; no en el contenido.**

Certifico:

- el **contenido** de bytes exactos identificados por hash: informe
  `06828d5c…` y certificado `23be80f2…`;
- que el diff pre→post no altera la matemática;
- que el charter ejecutado está anclado en git y en el remoto antes de los
  artefactos.

No puedo certificar criptográficamente:

- el orden temporal ejecución → revisiones → reparaciones;
- que no existieran otras versiones intermedias.

Esto descansa en mtimes y en el texto de las revisiones. La copia
pre-reparación vive sólo en un scratchpad efímero.

Que no hubo cálculo antes de las 09:52 tampoco es demostrable
criptográficamente por nadie: descansa en §15 del charter y en la cronología
del sistema de archivos. Es la misma situación que en gates anteriores.

**Consecuencia para congelar:** el commit de congelación debe incluir
exactamente los bytes revisados, más el diff de MR1, y registrar los hashes
`5d3e7125…` (pre), `06828d5c…` (revisado) y el hash final tras MR1.

## 2. Reconstrucción matemática independiente

**Plancherel [M].** Con `hat psi(p) = sum_x e^{ip.x} psi(x)` y
`psi(x) = int_B e^{-ip.x} hat psi dmu`, `dmu = d^3p/(2pi)^3`:

`int_B |hat psi|^2 dmu = sum_{x,y} psi(x) conj psi(y) int_B e^{ip.(x-y)} dmu = sum_x |psi(x)|^2`.

La medida está forzada por la convención; no hay libertad de un `2pi`.
`Pi_Lambda` y `S` son multiplicadores de Fourier y conmutan.

**Símbolo del estado [M].** Un operador con núcleo `k(x-z)` actúa con símbolo
`sum_d k(d) e^{ip.d}`. Así, `W` tiene símbolo `W(p)` y su adjunto tiene
`W(p)^dagger`. Por tanto `S(p) = W(p)^dagger`, como fija §2.

**`kappa` [M][C].**

`kappa = mu({|p| <= Lambda}) = (4 pi Lambda^3/3)/(8 pi^3) = Lambda^3/(6 pi^2)`.

Verificado. La bola está dentro de `B` porque `Lambda < pi/4 < pi`.

**`Z` [M][C].**

`Z = Lambda^3/(8pi^3) * 4pi * int_0^1 (1-r^2)^4 r^2 dr`, con
`int_0^1 (1-r^2)^4 r^2 dr = 1/3 - 4/5 + 6/7 - 4/9 + 1/11 = 128/3465`.

Luego `Z = 64 Lambda^3/(3465 pi^2)`. **Verificado.** Análogamente,
`int g(p/Lambda) dmu = (Lambda^3/(2pi^2)) * 8/105 = 4 Lambda^3/(105 pi^2)` [M][C].

**`psi_Lambda(0)` [M][C].** `S` está en SU(2) y `tr S = 2 c1 c2 c3 =: 2f`
es real, así que `S^2 = 2fS - I`. La segunda columna de `S` es
`(c1 s2 - i s1, c1 c2 e^{ip3})`, luego

`S^2 e_down = (2f(c1 s2 - i s1), 2f c1 c2 e^{ip3} - 1)`.

`g(p/Lambda)` es invariante bajo cada reflexión `p_i -> -p_i`, así que integra
la parte par en las tres reflexiones:

- componente superior: `0`;
- componente inferior: `2 c1^2 c2^2 c3^2 - 1`.

Promedié la expresión simbólica sobre los 8 signos [C]. Por tanto

`psi(0) = Z^{-1/2} int g(p/Lambda) F dmu * e_down`, con `F = 2 prod cos^2 p_i - 1`.

La misma parte par sale con `W^2` en lugar de `S^2`, y con espín `up` [C]:
`s` no depende de la convención de signo, de estado/núcleo ni del espín.

**`s(Lambda)` [M][C].** A mano: `F = 1 - 2|p|^2 + O(p^4)`, así que
`s ~ (4Lambda^3/(105pi^2))^2 / (64Lambda^3/(3465pi^2)) = 11 Lambda^3/(140 pi^2)`.
**Verificado.**

En código obtuve además una forma cerrada exacta. Se escribe
`prod cos^2 = (1/8) sum_T prod_{i in T} cos 2p_i`; el promedio sobre signos
reduce cada término a la transformada radial
`G(k) = 4pi int g r^2 sin(kr)/(kr) dr` en `k = 0, 2, 2sqrt2, 2sqrt3`. SymPy da

`s = (33 Lambda^3 - 44 Lambda^5)/(420 pi^2) + O(Lambda^6)` [C].

Como control ilustrativo, no probatorio, esa forma cerrada coincide con
cuadratura 3D directa en `Lambda = 0.6`, con diferencia `9e-14` y
`s/kappa = 0.283`.

**`0 < s <= kappa` en toda la carta.**

- **`s <= kappa`** [M], por Cauchy–Schwarz y sin usar `g`. Como
  `Pi psi = psi` (soporte exacto), para `v` unitario
  `|<delta_0 (x) v|psi>| = |<Pi(delta_0 (x) v)|psi>| <= ||Pi(delta_0 (x) v)|| = sqrt(kappa)`.
  Vale para **cualquier** `psi` normalizado en `ran Pi_Lambda`.
- **`s > 0`** [M]. Sea `h(t) = 2 log cos sqrt t`. Entonces
  `h'(t) = -tan(sqrt t)/sqrt t` y `(tan u/u)' = (2u - sin 2u)/(2u^2 cos^2 u) > 0`
  [C para las identidades], así que `h` es cóncava en `[0, (pi/2)^2)`.
  - El mínimo de `sum h(p_i^2)` sobre el símplex `sum p_i^2 = |p|^2` está en
    un vértice. Luego `prod cos^2 p_i >= cos^2|p|` y
    `F >= cos 2|p| > 0` si `|p| < pi/4`.
  - Como `g >= 0` y no es idénticamente nula, `int gF > 0`.
  - Ruta alternativa para un entorno del origen: `F >= 1 - 2|p|^2 > 0` si
    `|p| < 1/sqrt2`.

Con `F <= 1` se obtienen también
`cos^2(2Lambda) 11Lambda^3/(140pi^2) <= s <= 11Lambda^3/(140pi^2)` y
`s/kappa -> 33/70` [M].

**Factores revisados sin encontrar error:**

- `2pi`: forzado por Plancherel;
- volumen: `4pi/3`;
- espín: `P_0` incluye ambos modos, y `psi(0)` es puramente `down`;
- normalización por `Z`;
- signo de Fourier: irrelevante para `s` y para `kappa`.

## 3. Encoder puntual [M]

En el sector de una partícula, `n_0 = P_0 = |0><0| (x) I_2`, luego
`U_1 = e^{i pi P_0} = I - 2P_0` y `U_1 - I = -2P_0`.

La elección de Alice introduce el vector diferencia
`U_1 psi - U_0 psi = -2a`, con `a := P_0 psi = delta_0 (x) psi(0)`:

| Propiedad de `a` | Valor |
| --- | --- |
| Soporte espacial | un único sitio, el origen |
| Transformada | `hat a(p) = psi(0)`, **constante** sobre toda `B` |
| Peso total | `||a||^2 = s` |
| Peso en el sector proyectado | `||Pi a||^2 = kappa s` (medida de la bola) |
| Peso fuera de él | `||(I-Pi)a||^2 = (1-kappa) s` |

**Descomposición por bloques** antes de hablar de "UV":

- `psi_0 = psi` está entero en `ran Pi`, así que `rho_0` es un bloque
  puramente `Pi…Pi`.
- `psi_1 = w + u`, con `w := Pi psi_1 = psi - 2 Pi a` y
  `u := (I-Pi) psi_1 = -2(I-Pi)a`.
- Todo el contenido de `psi_1` fuera de `ran Pi` procede de la componente
  fuera de banda del vector de un sitio `a`.
- `[Pi, P_0] != 0`, porque `a` tiene espectro plano.

## 4. Norma de la diferencia [M][C]

Sea `b := (I - P_0) psi`, con `a ⊥ b`, `||a||^2 = s` y `||b||^2 = 1-s`.
Entonces `psi_0 = a + b` y `psi_1 = b - a`, así que

`Delta = |psi_1><psi_1| - |psi_0><psi_0| = -2(|a><b| + |b><a|)`.

En la base ortonormal `(a/sqrt s, b/sqrt(1-s))` del subespacio generado por
ambos estados puros:

`Delta = [[0, -2c], [-2c, 0]]`, con `c = sqrt(s(1-s))`.

Los autovalores son `±2c`, luego **`||Delta||_1 = 4 sqrt(s(1-s))`.
Verificado.** La fidelidad da lo mismo: `<psi_0|psi_1> = 1 - 2s` y
`2 sqrt(1 - (1-2s)^2) = 4 sqrt(s(1-s))`.

Como `0 < s <= kappa < 1`, `Delta != 0` en toda la carta: la convención
`Delta = 0` de §7 no se activa.

## 5. Criterio relativo [M][C]

Como `rho_0 = Pi rho_0 Pi`, se tiene
`R := Delta - Pi Delta Pi = rho_1 - Pi rho_1 Pi = |w><u| + |u><w| + |u><u|`,
con `w ⊥ u`. Normas:

- `beta^2 := ||u||^2 = 4(1-kappa)s`;
- `alpha^2 := ||w||^2 = 1 - beta^2 = 1 - 4s(1-kappa)`.

Comprobación directa: `<psi|Pi a> = <Pi psi|a> = s` y `||Pi a||^2 = kappa s`.

En la base `(w/alpha, u/beta)`:

`R = [[0, alpha beta], [alpha beta, beta^2]]`, con `det = -alpha^2 beta^2 < 0`,

así que

`||R||_1 = lambda_+ - lambda_- = beta sqrt(beta^2 + 4alpha^2) = 4 sqrt((1-kappa)s(1 - 3s(1-kappa)))`.

Dividiendo por `||Delta||_1`:

**`eta_enc = sqrt((1-kappa)[1 - 3s(1-kappa)]/(1-s))`. Verificado**, no por
repetición: por la ruta de `rho_1 - Pi rho_1 Pi`. El modelo exacto 3×3 [C]
sobre `span{psi, Pi a, (I-Pi)a}` reproduce los datos de Gram, `det = 0`,
segundo invariante `<= 0` y `||·||_1^2 = tr^2 - 4 e2` para `Delta`, `R` y `L`.

Complemento:
`||L||_1 = ||Pi Delta Pi||_1 = 4 sqrt(s kappa (1 - 2s + s kappa))`
[M][C]. Es algebraicamente igual a la expresión del informe,
`4 sqrt(s^2(1-kappa)^2 + s(kappa - s))`.

**Hipótesis necesarias (todas verificadas para la clase):**

| # | Hipótesis |
| --- | --- |
| H1 | `Pi_Lambda psi = psi` exactamente: `g` con soporte en `|q| < 1` y `S` multiplicador |
| H2 | `||psi|| = 1`, por `Z` y unitariedad de `S` |
| H3 | `U_1 = I - 2P_0`, con `P_0` proyector del sitio con ambos modos |
| H4 | `||Pi(delta_0 (x) v)||^2 = kappa ||v||^2`: bola dentro de `B` y medida de Plancherel |
| H5 | `0 < s < 1`, para que el cociente esté definido |
| H6 | estados puros de una partícula en `n = 0`, como fija §7 |

`s <= kappa` no es una hipótesis: se sigue de H1, H2 y H4. Sólo se necesita
para la fórmula de `L` y para la cota de §6. Para `n = 1`, `[S, Pi] = 0` y la
invariancia unitaria de la norma de traza dan el mismo `eta`. No hace falta,
porque `n = 0` ya falla.

## 6. Cota uniforme [M][C]

Identidad:

`eta^2 - (1 - 4kappa) = [3kappa - 2s + s kappa(2 - 3kappa)]/(1-s)`.

Para `0 < s <= kappa <= 2/3` el numerador es `>= kappa > 0`, luego
`eta^2 > 1 - 4kappa`.

En la carta, `kappa` crece con `Lambda`, así que
`kappa < kappa(pi/4) = pi/384` y `1 - 4kappa > 1 - pi/96`.

Además, `1 - pi/96 > 24/25` si y sólo si `pi < 3.84`, lo que vale por ejemplo
con `pi < 22/7`. Por tanto **`eta_enc(Lambda) > 2 sqrt6/5` para todo
`0 < Lambda < pi/4`, con desigualdad estricta.** Sin muestreo.

**Basta `s <= kappa`** (de hecho `s <= 3kappa/2`) **más `kappa <= 2/3` y
`pi < 3.84`.** `s > 0` sólo hace falta para que `eta` esté definido.

La ruta del informe también es correcta [M]:

- numeradores `(1-kappa)(3kappa - 2s) >= 0` y `kappa - s + 3s(1-kappa)^2 >= 0`;
- suelo `(1-kappa)(1-3kappa)`;
- `pi/384 < 11/1344` por `pi < 22/7`;
- `1747563/1806336 > 24/25`.

## 7. Límite [M][C]

Como `0 < s <= kappa -> 0` y `eta^2` es continua en `(s,kappa) = (0,0)` con
valor 1:

| Cantidad | Comportamiento |
| --- | --- |
| `eta_enc` | `-> 1` |
| `s` | `-> 0` |
| `||Delta||_1` | `<= 4 sqrt(kappa) -> 0`, con `||Delta||_1 ~ (4/pi) sqrt(11/140) Lambda^{3/2}` |
| `epsilon_UV` | `= max(epsilon_pre = 0, epsilon_0 = 0, epsilon_1(0) = epsilon_1(1) = 4s(1-kappa)) <= 4kappa -> 0` |
| `||R||_1` | `-> 0` |

**Bloques de `R`** (`I` = `ran Pi`, `U` = `ran(I-Pi)`):

| Bloque | Operador | `\|\|·\|\|_1` |
| --- | --- | --- |
| IR–IR | `Pi R Pi` | `0` exactamente [C] |
| IR–UV | `\|w><u\|` | `alpha beta` |
| UV–IR | `\|u><w\|` | `alpha beta` |
| IR–UV + UV–IR conjunto | `R_off` | `2 alpha beta` [C] |
| UV–UV | `\|u><u\|` | `beta^2 = 4(1-kappa)s` [C] |

Cocientes:

- `||R_off||_1/||R||_1 = 2alpha/sqrt(beta^2 + 4alpha^2) -> 1`;
- `||R_UU||_1/||R||_1 = beta/sqrt(beta^2 + 4alpha^2) ~ sqrt(11/140) Lambda^{3/2}/pi -> 0`;
- además `||L||_1/||Delta||_1 <= sqrt(kappa) -> 0`.

**Formulación propuesta:** *"La diferencia codificada se hace pequeña en norma
absoluta, mientras que la fracción medida por el criterio relativo del charter
que queda fuera del bloque `Pi_Lambda Delta_Lambda Pi_Lambda` tiende a uno; el
residuo dominante corresponde a coherencias IR–UV/UV–IR."*
**Justificada exactamente**, con una precisión: "fracción" designa el cociente
`eta_enc` de normas de traza, que no es una partición, porque
`||L||_1 + ||R||_1 >= ||Delta||_1` por la desigualdad triangular.

**No autorizadas:**

- "codificación esencialmente UV";
- "señal puramente UV";
- "toda la información está en UV".

El residuo dominante es coherencia cruzada con la componente dentro de la
banda `w` (≈ `psi`), y el bloque UV–UV es relativamente despreciable. Como
descripción de `R`, "esencialmente UV" está refutada. Sobre señal o
información no se calculó nada.

## 8. Stop rule

**Texto literal del charter:**

- §7, l. 236–242: "**Primera prueba de ejecución:** examinar analíticamente
  §§6–7 antes de evaluar cualquier señal en Bob. […] Una demostración de
  incompatibilidad en todo entorno perforado del origen cierra negativamente
  la clase por control IR, sin calcular `D_B`. Una cota demasiado débil o un
  intento de prueba fallido deja el resultado abierto."
- §13.2, l. 396–398: "Si se prueba incompatibilidad asintótica, aplicar la
  stop rule sin evaluar señal ni buscar otra puerta."
- §10, l. 334–338: "Se indicará su razón: […] incompatibilidad del encoder con
  el criterio IR […]. Una prueba de incompatibilidad no afirma `D_B=0` para el
  walk."

**Respuestas:**

1. **¿Era correcto no calcular `D_B`?** **Sí.** Hay una identidad exacta con
   cota inferior uniforme: `Delta != 0` y `eta > 2 sqrt6/5` en toda
   `(0, pi/4)`, luego `eta_enc -> 0` es falso en cada entorno perforado, con
   cualquier lectura. No es una "cota débil". §7 y §13.2 obligan a parar.
2. **¿El negativo necesita `D_B = 0`?** **No.** §10, l. 338, lo excluye
   expresamente, y §5, l. 149, añade que la ocupación nula no lo certifica.
3. **¿Se sigue ya del fallo del encoder bajo la clase congelada?** **Sí.**
   - §9.1 exige "control de §§6–7 demostrado" para cualquier estado positivo;
     su refutación excluye las filas 1 y 2 de §10.
   - Hay obstrucción probada para toda la familia asintótica, que es la
     fila 3.
   - La fila 4 exige "no hay construcción ni obstrucción suficiente", así
     que no se aplica.
   - Aunque `s` se anulara en algún `Lambda`, la convención `Delta = 0`
     impediría un positivo.

## 9. Alcance

| | Afirmación | Clasificación | Motivo |
| --- | --- | --- | --- |
| A | El witness exacto `3/128` queda refutado | **NOT_SUPPORTED** | Otro recurso y ningún criterio IR; charter §11. Sus verificadores siguen pasando (§11) |
| B | El encoder puntual congelado falla el criterio IR relativo | **SUPPORTED** | §§5–6 |
| C | Ningún encoder posible produce señalización IR | **NOT_SUPPORTED** | Sólo `I - 2P_0` en un sitio bajo `eta_enc`; §10 fila 3 y §15 |
| D | Cambiar sólo la envolvente, manteniendo la clase espectral exacta, rescata necesariamente la puerta | **NOT_SUPPORTED** | Además, la identidad de §5 lo contradice para toda `psi` en `ran Pi_Lambda`: `eta^2 > 1 - 4kappa` si `P_0 psi != 0`, y `Delta = 0` si `P_0 psi = 0`. Esta observación de revisión no forma parte del claim congelable. Envolventes sin soporte espectral exacto: no decidido |
| E | Las coherencias IR–UV/UV–IR dominan el residuo relativo cuando `Lambda -> 0` | **SUPPORTED** | Conjuntamente, para la diferencia global de una partícula en `n = 0`, en norma de traza (§7) |
| F | No hay señalización en el límite continuo físico `a, tau -> 0` | **NOT_SUPPORTED** | No se calculó `D_B`; `Lambda -> 0` no es `a, tau -> 0`; `DIMENSIONAL_MAP_CONDITIONAL` |
| G | El resultado sólo vale para la clase preregistrada | **SUPPORTED** | Como alcance del claim congelable. La identidad matemática es más general (ver D), pero promoverlo requeriría otro contrato |
| H | Toda intervención estrictamente local falla en cualquier QCA | **NOT_SUPPORTED** | Ni siquiera se trataron otras puertas locales en este walk |

## 10. Auditoría de R1–R4 en el informe reparado (`06828d5c…`)

### R1 — incorporada

Líneas 5–7: "la fracción, en norma de traza, de la diferencia codificada que
queda fuera del bloque `Pi_Lambda Delta_Lambda Pi_Lambda` cumple
`eta_enc(Lambda) -> 1`". También líneas 265–268 y 466–468. `grep` no
encuentra "fuera de la banda" salvo en el registro de §14 (l. 480).

### R2 — incorporada

No queda "esencialmente UV", "essentially UV", "puramente UV" ni "toda la
información". Las únicas apariciones de "UV" son `epsilon_UV` y los nombres de
bloques (l. 146, 271–278, 318, 482–484). El párrafo nuevo "Estructura del
residuo [A]" (l. 270–279) es correcto: sus dos cocientes coinciden con §7 de
esta revisión. La negativa explícita de las l. 277–279 es adecuada.

### R3 — incorporada con un error factual nuevo → **MR1 obligatoria**

Líneas 354–361. La separación general es correcta. Pero la frase de las
**l. 358–361**,

> "No dice nada sobre el protocolo ultralocal de `3/128`, que usa otro recurso
> (`|0,down>` localizado en `T = 0`), otra lectura (Bob en `(1,1,1)`) y no está
> sometido a ningún criterio IR."

es **factualmente incorrecta o incompleta**. El valor `3/128` está congelado
para **dos** witnesses del mismo protocolo ultralocal:

| Witness | Referencia | Bob |
| --- | --- | --- |
| vértice | `CURRENT_STATE.md` §8.13 | `(1,1,1)` |
| no-corner | `CURRENT_STATE.md` §8.14; `NONCORNER_SIGNALING_GATE.md` l. 48–51 | `(±1,±1,0)` |

El no-corner usa **el mismo sitio `y_B = (1,1,0)`** que este gate, el mismo
`Delta T = 1`, los mismos dos pasos comunes y la misma puerta. La auditoría
dimensional (§8.15) trata precisamente ese witness. Por tanto la separación
**no** descansa en la lectura de Bob, sino en:

- (i) el recurso;
- (ii) la ausencia de criterio IR.

Además, "`T = 0`" usa el reloj de aquellos protocolos. En el reloj de este
informe, `T = 0` es la elección, y el estado ultralocal ahí es
`chi = S^2|0,down>`, no `|0,down>`.

El error no estaba en la redacción de R3 propuesta por la segunda revisión
(l. 367–370). Procede de la tabla de la self-review (l. 236). Es una
afirmación nueva introducida por la reparación.

### R4 — incorporada sustancialmente

Contrasté cada `[V]` con los checks del certificado:

- l. 48–54, 74, 86, 91, 102, 108, 113, 116, 125, 143, 162, 169–175, 182, 199,
  218, 226–228, tabla l. 233–237, l. 243, 250, 255, 257;
- todos corresponden a identidades o límites efectivamente comprobados;
- las desigualdades, signos, compresión, Lema 3, reducción a `V` y cotas de
  `s` están marcadas `[A]` (l. 17–23, 106–109, 116, 126, 201–202, 212, 229,
  237, 244, 248, 254–257, 312–313);
- la lista de cobertura de §12 (l. 418–433) es correcta;
- "Hechos del entorno" (l. 435–443) lo verifiqué: §11.

Omisiones menores, **no obligatorias**, porque no están mal etiquetadas sino
sin etiqueta:

- `Pi psi = psi`, `epsilon_pre = 0` y `epsilon_1(1) = epsilon_1(0)` por
  `[S, Pi] = 0` (l. 96–100, 144–145);
- `epsilon_UV <= …` y `epsilon_IR <= …` (l. 146–147);
- `s/kappa -> 33/70` (l. 192);
- que los símbolos `s`, `kappa` del modelo 3×3 sólo están vinculados
  nominalmente a `s(Lambda)` y `kappa(Lambda)`: mis mutaciones M12 y M13
  sobreviven (§11). En parte ya queda cubierto por "Lema 3 y reducción
  fiel a `V`".

"Propiedades verificadas externamente": el informe declara la cordura en toro
como no probatoria (l. 326–329). Las verificaciones de las revisiones no se
citan en §12. Puede añadirse en el acto de congelación.

### ¿Introdujeron las reparaciones afirmaciones nuevas no demostradas?

| Adición | Estado |
| --- | --- |
| Estructura del residuo | demostrada |
| §12 | verificado |
| §14, cronología | consistente con los mtimes |
| paréntesis de R3 | **incorrecto (MR1)** |

### Observaciones preexistentes, no introducidas por R1–R4, recomendadas

1. **l. 281–286, "Observación estructural".** "La cota inferior
   `(1-kappa)(1-3kappa)` no depende de `s`" y "la envolvente, el espín y los
   dos pasos […] sólo entran a través de `s > 0`" son ciertas. Pero su validez
   exige `s <= 3kappa/2`, y el informe sólo lo obtiene vía el Lema 4, que es
   específico de `g`. Falta la línea de Cauchy–Schwarz de §2 de esta revisión.
   `PROOF_GAP` menor, fuera del claim.
2. **l. 259–260, "unos `Lambda^{-3}` sitios".** Es heurístico. Lo demostrable
   es "al menos `1/kappa = 6pi^2 Lambda^{-3}` sitios", porque
   `sup_x |psi(x)|^2 <= kappa` por Cauchy–Schwarz. `PROOF_GAP` interpretativo,
   fuera del claim.
3. **l. 5 "fracción".** Preferible "cociente `eta_enc`", porque no es una
   partición. La propia self-review (l. 200–201) lo advierte. No obligatorio:
   la frase lo liga a `eta_enc`.

## 11. Certificado software

Inspeccionado sólo tras terminar la derivación propia.

**Ejecución [X].** `python3 scripts/verify_narrow_band_gate.py`: **34/34**,
exit 0 (Python 3.12.3, SymPy 1.14.0).

**Correspondencia código ↔ fórmulas [X].**

| Checks | Contenido |
| --- | --- |
| 10 | `kappa` |
| 12–13 | `Z`, `int g`, `11/140 < 1/6` |
| 20–21 | `S^2 e_down` y paridades |
| 23 | Gram |
| 24–25 | `det`, `e2` |
| 26–28 | `\|\|Delta\|\|`, `\|\|R\|\|`, `\|\|L\|\|` |
| 29 | `epsilon_1` |
| 30 | `eta^2` |
| 31 | numeradores |
| 32 | cociente de `L` |
| 33 | suelo en `11/1344` |
| 34 | límite del suelo |

Todos coinciden con mis fórmulas.

- `verify()` sólo acepta `True` o `sp.true`, así que una relación no decidida
  falla.
- El modelo usa `.T` en lugar de `.H`, lo cual es correcto porque las
  coordenadas son reales bajo `s <= kappa`.
- Check 1: el mensaje dice "(817050d blob)", pero compara el sha256 del
  archivo de trabajo. El vínculo con el blob lo establecí por git (§1).

**`Float` [X].** Instrumenté `Float.__new__` contando sólo instancias finitas,
y registré los locales de `main()` al retornar:

- **17 `Float` finitos durante el import** de `verify_directional_saturation`
  (`sympy.physics.units`, por ejemplo `365.259636`);
- **0 durante `main()`**;
- **ningún átomo `Float`** en los 54 locales de `main()` ni en `C`, `S`, `PS`,
  `PAULI` ni `walk2()`.

No participan en ninguna cantidad científica. Confirma el informe §12 y
**refuta** la self-review (l. 288–291: "No aparece ningún float finito").

**numpy [X].** `verify_directional_saturation.py:517` hace `import numpy` a
nivel de módulo, y `scripts/requirements.txt` sólo declara `sympy==1.14.0`.
Con numpy bloqueado, el certificado aborta con `ImportError` antes del primer
check: falla cerrado por excepción, no da un falso PASS.

**Mutaciones [X].** 16 copias en el scratchpad, con `ROOT` apuntando al repo;
el archivo del repo no se tocó.

| Id | Mutación | Resultado |
| --- | --- | --- |
| M0 | sin mutar | 34/34 |
| M1 | coeficiente de `\|\|R\|\|_1`, `3 -> 4` | FAIL |
| M2 | `11/140 -> 11/141` | FAIL |
| M3 | umbral `24/25 -> 49/50` | FAIL |
| M4 | medida `(2pi)^3 -> (2pi)^2` | FAIL |
| M5 | `S = W^dagger -> W` | FAIL |
| M6 | espín `down -> up` | FAIL |
| M7 | `Pi = diag(1,0,0)` | FAIL |
| M8 | `eta^2` sin `1/(1-s)` | FAIL |
| M14 | hash del charter | FAIL |
| M15 | Gram `s -> 2s` | FAIL |
| M16 | `L = Pi Delta` | FAIL |
| **M9** | `k_chart = (22/7)/3840` | **sobrevive 34/34** |
| **M10** | prefactor de `R_W`, `3 -> 1` | **sobrevive** |
| **M11** | cota de `s`, `cos 2L -> cos 7L` | **sobrevive** |
| **M12** | `floor.subs(k, kappa/7)` | **sobrevive** |
| **M13** | `11/140 < 1/6 -> < 1` | **sobrevive** |

**Clasificación de huecos:**

| Hueco | Sonda | Clasificación |
| --- | --- | --- |
| Constante y cadena de `R_W` (`3`, `25/18`, Frobenius, telescopio) | M10 | `SOFTWARE_ONLY_GAP`. Rehecho a mano [M]: cota diagonal `\|p\|^2/2`, fuera de la diagonal `5Lambda^3/6`, `R_W < 5Lambda^2` con `pi < 22/7`. Irrelevante para la stop rule |
| Cotas bilaterales de `s` (Lema 4) | M11, M13 | `SOFTWARE_ONLY_GAP`. El veredicto sólo usa `0 < s <= kappa`, demostrado [M] por Cauchy–Schwarz y concavidad |
| Lema de la carta (mínimo en un vértice; sin otros nodos; rama del logaritmo) | — | `SOFTWARE_ONLY_GAP`. Demostrado [M]; `W = ±I` en la carta fuerza `s1 = 0`, `c1 s2 = 0` y `p = 0` |
| Reducción a `V` y Lema 3 (vínculo nominal de `s`, `k` con `s(Lambda)`, `kappa(Lambda)`) | M12 | `SOFTWARE_ONLY_GAP`. Demostrado [M] |
| Sándwich `eta <= 1` | — | `SOFTWARE_ONLY_GAP`. Demostrado [M]; sólo afecta a "límite = 1", no a `eta ↛ 0` |
| Vínculo `k_chart` ↔ `kappa(pi/4) = pi/384` | M9 | `SOFTWARE_ONLY_GAP`. Trivial [M] |
| Paridad ⇒ integrales nulas; signos `e2 <= 0` y numeradores `>= 0` | — | `SOFTWARE_ONLY_GAP`. Demostrado [M] |
| numpy transitivo no declarado | bloqueo | `SOFTWARE_ONLY_GAP` (reproducibilidad) |
| 17 `Float` de librería al importar | sonda | `SOFTWARE_ONLY_GAP` (ninguno en cantidades) |
| Mensaje del check 1 y docstring (importa también `C`, `S`, `PS`, `PAULI`) | — | `SOFTWARE_ONLY_GAP` (cosmético) |
| "Observación estructural" sin Cauchy–Schwarz; "`Lambda^{-3}` sitios" | — | `PROOF_GAP` menor, en texto interpretativo fuera del claim |
| — | — | **`VERDICT_THREATENING_GAP`: ninguno** |

**Regresiones congeladas [X]**, todas con exit 0 y
`PYTHONDONTWRITEBYTECODE=1`:

| Script | Resultado |
| --- | --- |
| `verify_directional_saturation.py` | 27/27 |
| `… --local-preparation-only` | 21/21 |
| `… --noncorner-gate-only` | 20/20, `NONCORNER_SIGNALING_CONSTRUCTED` |
| `verify_signaling_witness.py` | 17/17 |

`verify_weyl_dirac_gate.py` y los scripts S4 no fueron re-ejecutados por mí
[L].

Antes y después de todo lo anterior tomé una instantánea: `git status`, mtimes
de `__pycache__`, sha256 de `scripts/*.py`, charter, informes del gate y
`CURRENT_STATE.md`. **Idénticas.** Sin cambios tracked.

## 12. Script nuevo

Charter §13, l. 406–411, literal:

> "Los helpers existentes del símbolo y de la reducción local pueden servir
> posteriormente; los helpers para estados de soporte espacial finito no
> pueden usarse truncando sin control este paquete extendido. No se crea un
> script nuevo salvo necesidad demostrada y autorización de implementación.
> Los verifiers previamente revisados conservan sus bytes en esta fase."

**Clasificación: `DOCUMENTED_IMPLEMENTATION_DEVIATION_WITHOUT_SCIENTIFIC_EFFECT`.**

- **Necesidad: demostrada.**
  - `scripts/README.md`, l. 82–84, exige código permanente y trazado, y
    prohíbe que scripts efímeros aporten evidencia.
  - Los helpers de soporte finito no pueden truncar el paquete.
  - Los verificadores revisados conservan sus bytes: lo comprobé por
    `git hash-object`.
  - La reutilización es sólo por import de lectura.
- **Autorización:** el informe (§11) la atribuye a una instrucción de
  ejecución que no está en el repo. Desde un contexto independiente **no
  puedo verificarla**. Debe confirmarla el usuario en el acto de congelación.
- **Efecto científico: ninguno.** El veredicto descansa en una prueba
  analítica que reconstruí sin el script.

## 13. Veredicto

### `PASS_WITH_MANDATORY_REPAIRS`

**Por qué no FAIL.** Todas las inferencias necesarias para activar la stop
rule y para el veredicto están demostradas, y las reconstruí
independientemente:

- `0 < s <= kappa`;
- `||Delta||_1 = 4 sqrt(s(1-s)) > 0`;
- la fórmula de `eta_enc`;
- `eta_enc > 2 sqrt6/5` en toda la carta;
- el límite `1`;
- la aplicación literal de §§7, 9 y 10.

**Por qué no PASS.** R3 contiene una afirmación factual incorrecta introducida
por la reparación, en el texto de techo de reclamo que se congelaría.

**MR1 (obligatoria).** En `reports/2026-09-17--narrow-band-signaling-gate.md`,
**líneas 358–361**, sustituir

> "No dice nada sobre el
>   protocolo ultralocal de `3/128`, que usa otro recurso (`|0,down>` localizado
>   en `T = 0`), otra lectura (Bob en `(1,1,1)`) y no está sometido a ningún
>   criterio IR."

por un texto equivalente a:

> "No dice nada sobre el protocolo ultralocal de `3/128`, ni en su witness de
> vértice (Bob en `(1,1,1)`) ni en el no-corner (Bob en `(±1,±1,0)`). Ese
> protocolo comparte con este gate los dos pasos comunes, la puerta `U_1` en
> el origen y `Delta T = 1` y, en el caso no-corner, el propio sitio
> `y_B = (1,1,0)`. Difiere en el recurso: `|0,down>` exactamente localizado
> antes de los dos pasos, es decir `chi = S^2|0,down>` en el instante de la
> elección, con espectro sobre toda la zona de Brillouin, en lugar de
> `phi_Lambda` de banda estrecha. Además, no está sometido a ningún criterio
> IR."

MR1 se verifica con un diff limitado a ese párrafo y sin tocar otras líneas.
Conviene reflejar el cambio en §14 del informe.

**Recomendadas, no obligatorias:**

- las tres observaciones del final de §10;
- las omisiones menores de R4;
- renombrar el check 1 y corregir el docstring;
- declarar numpy;
- corregir el encabezado del charter en un acto separado;
- anotar en la self-review archivada su error sobre los `Float` y su tabla
  §9, fila 1.

### Discrepancias con los artefactos previos

1. **Self-review, l. 236, e informe reparado, l. 358–361:** omiten el witness
   no-corner de `3/128`, que tiene el mismo `y_B = (1,1,0)`. La segunda
   revisión no lo detectó. Da lugar a MR1.
2. **Self-review, l. 288–291:** "ningún float finito". Hay 17 al importar. La
   segunda revisión y el informe reparado ya lo corrigen; lo confirmo.
3. **Segunda revisión, l. 321:** "`PROOF_GAP`: ninguno". Hay dos menores, en
   texto interpretativo fuera del claim (§10). No amenazan el veredicto.
4. **Informe, l. 81:** "`tr W/2` … [V]". El certificado verifica `tr S/2`. Es
   equivalente porque la traza es real. Cosmético.
5. **Segunda revisión, l. 3–5 y 267–277:** "reparaciones no aplicadas". Era
   cierto a las 10:47; ahora están aplicadas, salvo el defecto de MR1.

No encontré discrepancias en ninguna cantidad: `kappa`, `Z`, `s`,
`||Delta||_1`, `||R||_1`, `||L||_1`, `eta_enc`, cotas y límites coinciden en
los tres artefactos y en mi derivación.

## 14. Estado congelable

**Sin PASS no autorizo `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED`.**
Se conserva `PARTIAL_REVIEW_PASS_WITH_REPAIRS / INDEPENDENT_REVIEW_PENDING`.

Precisión. La matemática central ya ha recibido una revisión independiente,
**esta**, que la acepta. Lo pendiente es exclusivamente MR1.

El precedente del proyecto es §8.14: `PASS` con reparaciones textuales
aplicadas, congelado como `INDEPENDENTLY_REVIEWED`. Aplicada MR1, y verificado
por diff que ningún otro byte cambia respecto de `06828d5c…`, esta revisión
respaldaría la promoción sin nueva derivación. La decisión y esa verificación
corresponden al usuario.

**Declaraciones explícitas:**

- **Independencia:** revisión realizada desde un contexto independiente, sin
  acceso a la sesión que ejecutó, reparó y escribió las revisiones previas.
  El encargo contenía las fórmulas objetivo (§0).
- **Falta de commit:** no limita la validez matemática, que es verificable
  sobre los bytes identificados por hash. **Sí limita** la cronología
  certificable de ejecución → revisiones → reparaciones: sólo hay mtimes, el
  inodo del informe se recreó a las 11:05:12, y la versión previa existe sólo
  en un scratchpad.
- **Lo congelable** es el contenido de los hashes citados más el diff de MR1.
  El commit de congelación debe registrar `5d3e7125…`, `06828d5c…`, el hash
  posterior a MR1 y `23be80f2…` del certificado.
