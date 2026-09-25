# Revisión adversarial: ejecución de NARROW_BAND_SIGNALING_GATE

Fecha: 2026-09-17. **Veredicto de revisión: `PASS_WITH_MANDATORY_REPAIRS`.**
Ninguna reparación cambia el veredicto `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`.

**Limitación de independencia (vinculante para el estado).** Esta revisión la
hizo **la misma sesión y el mismo modelo que ejecutó el gate**. Las revisiones
previas del repositorio las hizo un agente separado que arrancó en frío. Por
tanto esta revisión **no** convierte el resultado en `INDEPENDENTLY_REVIEWED`
ni en `ESTABLISHED` (`PROJECT_INSTRUCTIONS.md` §4).

Mitigación aplicada:

- no se usó `scripts/verify_narrow_band_gate.py` como autoridad;
- el símbolo se volvió a transcribir desde §2 del charter;
- cada fórmula decisiva se rehízo por una ruta distinta de la del informe:
  integrales con la función Beta, fidelidad de estados puros, bloque 2×2,
  una instancia compleja concreta en 4 dimensiones y otra cota de π;
- el certificado se sometió a mutaciones pensadas para localizar huecos.

Archivos revisados: el charter (sha256 `3d559ced…41ba9`), el informe
[`2026-09-17--narrow-band-signaling-gate.md`](2026-09-17--narrow-band-signaling-gate.md)
(sha256 `5d3e7125…445f8e`), el certificado (sha256 `23be80f2…8d4586`),
`walk2()` y `PROJECT_INSTRUCTIONS.md`. No se consultó bibliografía: ninguna
afirmación decisiva depende de DP14, BDP17 ni BB93. No se editó ningún
archivo revisado. No hubo commit, push ni promoción. Todo el Python se ejecutó
con `PYTHONDONTWRITEBYTECODE=1`.

## 1. Preregistro y cadena temporal

| Hecho | Evidencia |
| --- | --- |
| Hash de ejecución | `817050d8e80e6d6e636937b5794d60ff67e6e047` = `HEAD` = `origin/…` = `ls-remote` |
| Charter publicado antes del cálculo | commit 09:52:56 y push 09:53:02 (reflog). Artefactos de cálculo posteriores: texto de los PDFs 09:58, cordura efímera 10:03, script 10:09, informe 10:14 |
| Bytes ejecutados = contrato | `git show 817050d:…` y el archivo de trabajo tienen el mismo sha256; único commit que toca el charter en todas las refs |
| Contenido científico ejecutado = contrato | nodo `p=0`; `Pi_Lambda` con bola cerrada; `g` con soporte abierto; `psi = S^2 phi` con `S = W^dagger`; `U_1 = I - 2P_0`; `n = 0` inmediatamente después de Alice; `eta_enc = \|\|Delta - Pi Delta Pi\|\|_1/\|\|Delta\|\|_1`; convención `Delta = 0`; carta `0 < Lambda < pi/4`. `y_B` y `Delta T` no intervinieron |
| Decisiones posteriores a resultados | ninguna sobre perfil, nodo, Bob, tiempo, encoder o criterio. Sí se añadieron después constantes de cota (`2 sqrt6/5`, `R_W < 5 Lambda^2`) y una observación estructural, pero son artefactos de prueba o de interpretación: el veredicto depende sólo de `lim eta_enc != 0` |
| Cálculo numérico previo | un análogo flotante en un toro (`N = 12`, un único `Lambda = 0.7`) antes del certificado. No fijó ningún parámetro ni se usó como evidencia |

**Inconsistencia del encabezado** (charter, líneas 3–7). Sigue diciendo "sobre
`HEAD=11efe1f` y el remoto científico `780ecb0`… publicación/versionado y
ejecución pendientes", y la enmienda administrativa anunciada no existe en
ninguna ref. **Consecuencia científica: ninguna.** Los §§1–15 ejecutados son
byte a byte el blob publicado antes del cálculo; el encabezado sólo describe
la base de redacción. La consecuencia es administrativa: debe corregirse en un
acto separado y no se reparó aquí. La ejecución lo reportó en lugar de omitirlo.

## 2. Preparación IR (rehecha)

**Normalización**, por una ruta distinta. Se usa
`int_0^1 r^2 (1 - r^2)^n dr = B(3/2, n+1)/2`, que da `1/3`, `8/105` y
`128/3465` para `n = 0, 2, 4`. Desarrollando el polinomio, el caso `n = 4` es
`1/3 - 4/5 + 6/7 - 4/9 + 1/11 = (1155 - 2772 + 2970 - 1540 + 315)/3465 = 128/3465`.
Con `dmu = d^3p/(2pi)^3` y el factor radial `4 pi Lambda^3/(8 pi^3)`:

- `kappa(Lambda) = Lambda^3/(6 pi^2)`;
- `Z_Lambda = 64 Lambda^3/(3465 pi^2)`;
- `int g(p/Lambda) dmu = 4 Lambda^3/(105 pi^2)`;
- `A^2 := (int g)^2/Z = 11 Lambda^3/(140 pi^2)`, con `A^2/kappa = 33/70`.

Las cuatro coinciden.

**`psi_Lambda(0)`.** Multiplicando matrices directamente, sin Cayley–Hamilton,
con `S = W^dagger` transcrito del charter:
`S^2|down> = (2 c1 c2 c3 (c1 s2 - i s1), c1^2 c2^2 (1 + e^{2ip3}) - 1)`.
Esto coincide con el informe.

- La parte real inferior es `2 c1^2 c2^2 c3^2 - 1`. Es la misma para `W^2`,
  así que el signo de la convención de Fourier o de tiempo no altera `s`.
- Las partes impares integran cero contra la `g` radial.
- Por tanto `psi(0) = (0, c_down)`, con
  `c_down = Z^{-1/2} int g(p/Lambda) F dmu` y `F = 2 prod c_i^2 - 1`.

**Positividad.** Para `|p| < pi/2`, `prod cos p_i >= cos|p|`.

Prueba rehecha. `h(u) = log cos sqrt(u)` tiene `h'(u) = -tan t/(2t)` con
`t = sqrt(u)`. Como `(tan t/t)' = (2t - sin 2t)/(2 t^2 cos^2 t) >= 0`, `h'` es
decreciente y `h` es cóncava en `[0, pi^2/4)`. Una función cóncava alcanza su
mínimo sobre el símplex `{u_i >= 0, sum u_i = |p|^2}` en un vértice, lo que da
`sum h(p_i^2) >= h(|p|^2) + 2h(0)`.

Sobre el soporte de `g`, con `|p| < Lambda < pi/4`, esto da
`cos 2Lambda <= cos 2|p| <= F <= 1`. Como `g >= 0`:

`cos(2Lambda) A <= c_down <= A`, luego `cos^2(2Lambda) 11 Lambda^3/(140 pi^2) <= s <= 11 Lambda^3/(140 pi^2)`.

**Confirmado:** `0 < s < kappa < 1` en toda la carta, y la afirmación del
informe `s ~ 11 Lambda^3/(140 pi^2)` es exacta como equivalencia asintótica,
porque el cociente está en `[cos^2 2Lambda, 1]` y tiende a `1`.

**Robustez adversarial.** Ni `c_up = 0` ni la constante `11/140` son
decisivas. Por Cauchy–Schwarz, `s <= kappa` vale para cualquier `psi`
normalizado con soporte en la bola, y la cota de §6 sólo usa `s <= kappa`. La
positividad `s > 0` sólo fija la *razón* declarada y que `eta_enc` esté
definido. Incluso con `s = 0` en algunos `Lambda`, la convención `Delta = 0`
impediría un positivo, y el estado terminal seguiría siendo el mismo.

## 3. Efecto de la puerta puntual

`U_1 psi - U_0 psi = -2 P_0 psi = -2 e`, con `e = delta_0 (x) psi(0)`. Con
`hat e(p) = sum_x e^{ip.x} delta_{x,0} psi(0) = psi(0)` para todo `p`:

| Aspecto | Valor |
| --- | --- |
| Soporte espectral | toda `B`, pues `psi(0) != 0` |
| Amplitud total | `\|\|e\|\|^2 = int_B \|psi(0)\|^2 dmu = s`, con `mu(B) = 1`, Parseval con esta normalización |
| Fracción en `Pi_Lambda` | `\|\|Pi e\|\|^2/\|\|e\|\|^2 = mu({\|p\| <= Lambda}) = kappa`, válida porque la bola está dentro de `B` (`Lambda < pi`) |

**Confirmado:** un vector soportado en un sitio tiene densidad espectral plana
sobre toda la zona de Brillouin. Además, `f = psi - e` no tiene soporte en la
banda: su parte fuera es `-(I - Pi) e`. Todo el contenido fuera de la banda de
las dos ramas procede de `e_out = (I - Pi) e`.

## 4. Norma de la diferencia (ruta distinta)

Para estados puros unitarios, `\|\| |a><a| - |b><b| \|\|_1 = 2 sqrt(1 - |<a|b>|^2)`.
Como `<psi|U_1 psi> = 1 - 2<psi|P_0|psi> = 1 - 2s`, que es real:

`||Delta_Lambda||_1 = 2 sqrt(1 - (1-2s)^2) = 4 sqrt(s(1-s))`. **Confirmado.**

El dominio es `s ∈ [0,1]` (aquí `0 < s < 1`); los signos no importan, porque
el producto escalar entra al cuadrado; la normalización es `||psi|| = 1` por
`Z_Lambda`. Una instancia compleja concreta (`C^4`, `kappa = 9/25`,
`psi = ((3+4i)/13, 12/13, 0, 0)`, `s = 9/169`) da el mismo valor con
autovalores exactos.

## 5. Fuga relativa (ruta distinta)

Sean `w = Pi U_1 psi` y `h = (I - Pi) U_1 psi`. Como `Pi psi = psi`:

- `Pi Delta Pi = |w><w| - |psi><psi|`;
- `R = Delta - Pi Delta Pi = |w><h| + |h><w| + |h><h|`.

Como `w ⊥ h`, `R` en la base ortonormal `(w/a, h/b)` es `[[0, ab],[ab, b^2]]`,
con `a = ||w||` y `b = ||h||`. Sus autovalores tienen producto `-a^2 b^2 < 0`,
luego `||R||_1 = |λ1 - λ2| = b sqrt(b^2 + 4a^2)`.

Datos:

- `b^2 = ||(I-Pi)(psi - 2e)||^2 = 4||e_out||^2 = 4 s (1-kappa)`;
- `a^2 = 1 - b^2`, porque `U_1` es unitario.

Resultado:

`||R||_1 = 4 sqrt(s(1-kappa)(1 - 3s(1-kappa)))`,
`eta_enc = sqrt( (1-kappa)(1 - 3s(1-kappa)) / (1-s) )`. **Confirmado**, también
en la instancia 4-dimensional (`||R||_1` exacto).

`kappa(Lambda) = Lambda^3/(6 pi^2)` es la medida `d^3p/(2pi)^3` de la bola
cerrada `|p|_2 <= Lambda`, es decir, la fracción dentro de la banda de todo
vector de un solo sitio.

**Hipótesis que entran en la fórmula:**

- (H1) `Pi_Lambda psi_Lambda = psi_Lambda` exactamente;
- (H2) `||psi_Lambda|| = 1`;
- (H3) `U_1 = I - 2P_0`, con `P_0` el proyector del sitio `0` y ambos espines;
- (H4) `Lambda < pi`, bola dentro de `B`;
- (H5) `0 < s < 1`, para que el cociente esté definido;
- (H6) evaluación en `n = 0`, sector de una partícula, como fija §7.

`s <= kappa` no es una hipótesis: es consecuencia de (H1)–(H2).

## 6. Cota uniforme y límite (analíticos)

Para `0 < s <= kappa < 1/3`:

- `1 - eta^2 = (kappa - s + 3s(1-kappa)^2)/(1-s) >= 0`;
- `eta^2 >= (1-kappa)(1 - 3s(1-kappa)) >= (1-kappa)(1-3kappa) =: m(kappa)`,
  usando `s(1-kappa) <= kappa` y `0 < 1-s <= 1`.

En la carta, `kappa < kappa(pi/4) = pi/384`. `m` decrece estrictamente en
`[0, 2/3)`. Se comprobó con dos cotas independientes de `pi`:

- `pi < 22/7` (integral de Dalzell): `m(11/1344) = 1747563/1806336 > 24/25`,
  porque `43689075 > 43352064`;
- `pi < 4(1 - 1/3 + 1/5 - 1/7 + 1/9) = 1052/315` (suma parcial alternante de
  Leibniz): `m(263/30240) > 24/25`.

Luego `eta_enc(Lambda)^2 > 24/25`, es decir, **`eta_enc(Lambda) > 2 sqrt6/5`
para todo `Lambda ∈ (0, pi/4)`**. La desigualdad es estricta porque
`kappa < 11/1344` estrictamente.

Límite: `m(kappa(Lambda)) -> 1` y `eta^2 <= 1`, así que por compresión
**`lim_{Lambda->0} eta_enc = 1`**. **Ambas afirmaciones, confirmadas
analíticamente**, sin ningún valor numérico como premisa.

## 7. Fuga absoluta frente a fuga relativa

- `epsilon_UV = max(epsilon_pre = 0, epsilon_0(n) = 0, epsilon_1(n) = 4s(1-kappa)) <= 11 Lambda^3/(35 pi^2) -> 0`.
  Que `epsilon_1(1) = epsilon_1(0)` se sigue de `[S, Pi] = 0` y de la
  unitariedad de `S`.
- `||Delta||_1 = 4 sqrt(s(1-s)) ~ (4/pi) sqrt(11/140) Lambda^{3/2} -> 0`.
- `eta_enc -> 1`.

Las tres se confirman.

**La interpretación del enunciado sólo está justificada con una precisión.**
Aquí "fuera del sector IR" debe entenderse como *fuera del bloque IR–IR
`Pi Delta Pi`*, que es la definición de `eta_enc`. Además, `eta_enc` es un
cociente de normas, no una partición: `||Pi Delta Pi||_1 + ||R||_1 != ||Delta||_1`
en general. Descomponiendo `R` se obtiene exactamente:

- **coherencias IR–UV:** `||w><h| + |h><w||_1^2/||Delta||_1^2 = (1-kappa)(1 - 4s(1-kappa))/(1-s) -> 1`;
- **bloque UV–UV:** `||h><h||_1^2/||Delta||_1^2 = s(1-kappa)^2/(1-s) -> 0`, del orden de `Lambda^3`.

La diferencia codificada es, asintóticamente, **coherencia entre el recurso
dentro de la banda y el impulso de un sitio, que queda fuera de ella**; no es
contenido o población UV. Por eso **"la señal es puramente UV" no está
demostrado**: no se calculó ninguna señal, y lo que sale del bloque IR–IR es
casi todo término cruzado. El informe escribe "vive fuera de la banda" y
"codificación esencialmente UV", y ambas formulaciones deben reparase (R1, R2).

## 8. Stop rule

- Charter §7, líneas 240–242: "Una demostración de incompatibilidad en todo
  entorno perforado del origen cierra negativamente la clase por control IR,
  **sin calcular `D_B`**."
- §13.2: "Si se prueba incompatibilidad asintótica, aplicar la stop rule sin
  evaluar señal ni buscar otra puerta."
- §9.1 exige el control de §7 demostrado en un intervalo completo, y
  `eta_enc -> 0` queda refutado en todos, porque el límite es `1`.

No se trata de una "cota demasiado débil" (línea 242), sino de una identidad
con cota inferior explícita. No calcular `D_B` es **cumplimiento del
preregistro**, no ausencia de análisis.

§10 enumera "incompatibilidad del encoder con el criterio IR" como razón
válida y precisa que "Una prueba de incompatibilidad no afirma `D_B = 0`". El
veredicto **no requiere** `D_B = 0` y no lo afirma.

## 9. Techo de reclamo: inferencias

| # | Inferencia | Clasificación | Justificación |
| --- | --- | --- | --- |
| 1 | `3/128` queda refutado | **INVÁLIDA** | Es otro protocolo: recurso localizado `\|0,down>` en `T=0`, Bob en `(1,1,1)`, cálculo exacto finito. §11 del charter lo excluye; sus verificadores pasan 21/21. Además `3/128` nunca afirmó régimen IR (la auditoría dimensional, §5, ya lo negaba) |
| 2 | Ninguna puerta posible produce señalización IR | **INVÁLIDA** | Sólo se analizó `U_1 = e^{i pi n_0}` en un sitio, bajo el criterio `eta_enc`. §10 fila 3: "No es una imposibilidad general"; §15: otras nociones de control IR y puertas extendidas quedan fuera. Ni siquiera se trataron otras puertas de un solo sitio |
| 3 | La puerta puntual congelada falla el criterio IR relativo | **VÁLIDA** | `eta_enc > 2 sqrt6/5` en toda la carta y `-> 1`, sobre la familia congelada |
| 4 | Cambiar sólo la envolvente podría rescatar esta puerta | **INVÁLIDA como inferencia** | No se sigue del resultado. Para envolventes que mantengan (H1)–(H2), la misma identidad da `eta_enc >= sqrt(m(kappa)) -> 1` (y `psi(0) = 0` elimina la dependencia del bit), así que allí queda excluida. Para envolventes sin soporte espectral exacto, no está decidido. En todo caso sería otro contrato |
| 5 | Ausencia de señalización en el continuo físico | **INVÁLIDA** | No se calculó `D_B` y no se afirma `D_B = 0`. `Lambda -> 0` no es `a, tau -> 0`. Sin escala física (`DIMENSIONAL_MAP_CONDITIONAL`) |
| 6 | Vale únicamente para la clase preregistrada | **VÁLIDA** | Como alcance del veredicto. La identidad de §5 es más general matemáticamente, pero el claim congelable es el de la clase |

## 10. Código

**Correspondencia.** Las fórmulas de los checks 10, 12–13, 20 y 23–34 son las
de §§2–6 de esta revisión.

**Qué prueban realmente los 34 checks.** Los decisivos para el veredicto son
10 (`kappa`), 23–27 (modelo, determinantes, `e2`, `||Delta||`, `||R||`), 30–31
(`eta^2` y cotas) y 33–34 (carta y límite). Los checks 14–19 (`R_W`) no afectan
al veredicto.

Huecos, ninguno invalidante porque cada paso se probó a mano arriba:

- **G1.** El check 1 dice "(817050d blob)" pero compara el sha256 del archivo
  de trabajo con una constante. El vínculo con el blob lo establece el
  preflight de git, no el script.
- **G2.** El check 8 sólo verifica `2cos^2 t - 1 = cos 2t`. El mínimo en un
  vértice del símplex y la monotonía no están certificados; la mutación S03
  (`… or True`) sobrevive.
- **G3.** La cadena de desigualdades de `R_W` (módulos, Frobenius) y la
  constante `25/18` no están certificadas. La mutación S01 (`25/18 -> 1/18`)
  sobrevive con 34/34.
- **G4.** El check 22 sólo comprueba límites; la cota bilateral de `s`
  (desigualdad integral) no está certificada. La mutación S02
  (`cos 2L -> cos 3L`) sobrevive.
- **G5.** El check 21 certifica imparidad, no la anulación de las integrales.
- **G6.** El Lema 3 (espectro plano) y la reducción fiel a `V` son analíticos.
  El modelo usa `.T` (transpuesta), lo cual es correcto sólo porque las
  coordenadas son reales bajo `s <= kappa`.
- **G7.** Los signos (`e2 <= 0`, numeradores `>= 0`) se leen por inspección.
- **G8.** `kappa(pi/4) = pi/384` no está codificado.
- **G9.** El docstring dice que sólo se reutilizan `walk2` y el test de
  Laurent, pero también importa `C`, `S`, `PS` y `PAULI`.

**Mutaciones.** Diez mutaciones mueren con exit 1: hash del charter, `kappa`,
Gram de `e_out`, fórmula de `eta`, entrada de `S^2`, signo de concavidad,
`e2(R)`, `Pi` del modelo, `Z` y cota de `pi` debilitada a `4`. Un
monkeypatch del símbolo (signo de `i s1` en `W12`) muere en el check 2. El
guardia rechaza relaciones no decididas y comparaciones con floats. Las
sondas S01–S03 sobreviven, lo que documenta G2–G4.

**Imports.** `from verify_directional_saturation import …` sólo se lee. Al
importarse, ese módulo registra sus checks sin ejecutarlos, simplifica
`B1`/`B2` e **importa numpy a nivel de módulo** (línea 517), sin usarlo en
este certificado.

**Punto flotante.** Instrumentando `Float.__new__` durante una ejecución
completa se obtienen 4438 construcciones, y **todas devuelven `±oo`**
(centinelas internos de `limit`/`integrate`). No aparece ningún float finito.
No hay literales decimales.

**Regresiones.** Todas con exit 0:

- nuevo certificado 34/34;
- `verify_directional_saturation.py` 27/27, `--local-preparation-only` 21/21,
  `--noncorner-gate-only` 20/20;
- `verify_signaling_witness.py` 17/17;
- Weyl/Dirac, 375 checks;
- los dos scripts S4: PASS.

`git diff --check` vacío. Archivos tracked y `__pycache__` intactos.

**¿Contradijo el script nuevo el charter?** No materialmente. §13 permite un
script nuevo con "necesidad demostrada y autorización de implementación".

- **Necesidad:** el mismo charter (líneas 408–410) prohíbe usar los helpers
  de soporte finito truncando el paquete; los verificadores revisados
  conservan sus bytes (línea 411), y `scripts/README.md` exige código trazado.
- **Autorización:** la cláusula IMPLEMENTACIÓN de la instrucción de ejecución.
- La justificación está documentada en §11 del informe.

Es una desviación de implementación inocua y documentada. El veredicto
descansa en una prueba analítica que esta revisión reprodujo sin el script.

## 11. Veredicto de revisión

### `PASS_WITH_MANDATORY_REPAIRS`

**Errores que cambian el veredicto: ninguno.**

**Reparaciones obligatorias** (texto, alcance o estado; se aplican en el acto
de congelación, no en esta revisión):

- **R1.** Informe, líneas 6 y 256: "fuera de la banda" debe decir "fuera del
  bloque IR–IR `Pi_Lambda Delta_Lambda Pi_Lambda` (definición de `eta_enc`)".
- **R2.** Informe, líneas 258 y 414: "codificación esencialmente UV" debe
  sustituirse por el enunciado preciso de §7 de esta revisión: la parte fuera
  del bloque IR–IR está dominada por coherencias IR–UV; el bloque UV–UV es
  relativamente `O(sqrt s)`. Sin afirmación alguna sobre la señal en Bob.
- **R3.** Informe, línea 334: "ese mecanismo … no queda dentro del régimen IR"
  debe decir "la puerta puntual congelada, sobre la familia congelada, falla
  el criterio relativo de §7", para que no se lea como un juicio sobre el
  protocolo de `3/128`.
- **R4.** Informe, §12: declarar que el lema de la carta, las cotas de `s`, la
  cadena de `R_W`, el espectro plano y la reducción a `V` son **analíticos y no
  están certificados por software** (G2–G6), para que "34/34" no se lea como
  cobertura de esos pasos.
- **R5.** Estado: el resultado no puede congelarse como
  `INDEPENDENTLY_REVIEWED`. Etiqueta máxima:
  `PROOF_COMPLETE / SELF_ADVERSARIAL_REVIEW_PASS_WITH_REPAIRS; INDEPENDENT_REVIEW_PENDING`.

**Recomendadas, no obligatorias:**

- añadir a la observación estructural de §4.6 las hipótesis (H1)–(H6);
- renombrar el check 1 (G1);
- corregir el docstring (G9);
- codificar `kappa(pi/4) = pi/384` (G8);
- corregir el encabezado del charter en un acto administrativo separado.

**Huecos del certificado que no invalidan la demostración:** G1–G9.

### Claim máximo congelable

> En el CAR libre de CJWW (5.15), sector de una partícula, se considera la
> familia preregistrada `psi_Lambda = S^2 phi_Lambda`: nodo `p = 0`, envolvente
> `g(q) = (1-|q|^2)^2_+`, espín `down` y `Pi_Lambda` el proyector espectral sobre
> `|p|_2 <= Lambda`, con `0 < Lambda < pi/4`. La puerta puntual es
> `U_1 = e^{i pi n_0} = I - 2P_0`, aplicada en el origen en `T = 0`.
>
> Entonces `s(Lambda) = ||P_0 psi_Lambda||^2` cumple
> `cos^2(2Lambda) 11 Lambda^3/(140 pi^2) <= s <= 11 Lambda^3/(140 pi^2)`, y la
> diferencia global inmediatamente posterior a la elección cumple
> `||Delta_Lambda||_1 = 4 sqrt(s(1-s)) > 0` y
> `eta_enc(Lambda) = sqrt((1-kappa)(1 - 3s(1-kappa))/(1-s))`, con
> `kappa = Lambda^3/(6 pi^2)`. Por tanto `eta_enc > 2 sqrt6/5` en toda la carta
> y `eta_enc -> 1`.
>
> La fuga absoluta (`epsilon_UV <= 11 Lambda^3/(35 pi^2)`) y `||Delta_Lambda||_1`
> tienden a cero, mientras la fracción, en norma de traza, de `Delta_Lambda`
> fuera del bloque IR–IR tiende a uno, dominada por coherencias IR–UV. Por la
> stop rule de §7 la clase congelada se cierra como
> `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS`, por incompatibilidad del
> encoder con el criterio IR relativo preregistrado.
>
> No se calculó `D_B` ni se afirma nada sobre él (en particular, no se afirma
> `D_B = 0`). No afecta a `3/128` ni a los witnesses previos. No es una
> imposibilidad para otras puertas, preparaciones o nociones de control IR. No
> fija escala física, y `Lambda -> 0` no es un límite continuo `a, tau -> 0`.

## Apéndice: re-derivación exacta (efímera, sin importar `scripts/`)

Se ejecutaron 23 comprobaciones SymPy exactas:

- unitariedad y `det = 1` del símbolo transcrito del charter;
- `S^2|down>` por producto directo, y su independencia de la convención de
  signo;
- `kappa`, `Z`, `int g` y `A^2` por la función Beta;
- concavidad mediante `(tan t/t)'`;
- `||Delta||_1` por fidelidad de estados puros;
- `||R||_1` y `eta^2` por el bloque 2×2;
- la descomposición en coherencias IR–UV y bloque UV–UV;
- la instancia compleja en `C^4` con autovalores exactos;
- `kappa(pi/4) = pi/384` y la cota de Leibniz `pi < 1052/315`, con
  `m > 24/25`;
- el límite del suelo.

Las 23 pasaron. Durante la revisión se corrigieron dos erratas del script de
revisión: un paréntesis y una línea residual con un float de Python. No
afectaban al código revisado.
