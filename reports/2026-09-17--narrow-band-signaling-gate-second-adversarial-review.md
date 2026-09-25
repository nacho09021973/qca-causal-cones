# Segunda revisión adversarial: ejecución de NARROW_BAND_SIGNALING_GATE

Fecha: 2026-09-17 (10:41 en adelante).
**Veredicto de revisión: `PASS_WITH_MANDATORY_REPAIRS`.**
**Estado congelable: `PARTIAL_REVIEW_PASS_WITH_REPAIRS / INDEPENDENT_REVIEW_PENDING`.**

**Declaración de contexto (vinculante para §15).** La pidieron como revisión
independiente, pero **no se hizo desde un contexto independiente**: la hizo la
misma sesión que ejecutó el gate y escribió la self-review, con conocimiento
previo de ambas. Se aplicó la regla de trabajo pedida: primero las
derivaciones propias desde el charter, el walk, la preparación y la puerta, por
rutas distintas de las del informe y de la self-review; después la auditoría
del certificado; y al final, como evidencia secundaria, la self-review. Esa
disciplina mitiga el sesgo, pero **no autoriza** la etiqueta
`INDEPENDENTLY_REVIEWED`.

No se modificó ningún archivo revisado. No hubo commit, push ni promoción.
Todo el Python se ejecutó con `PYTHONDONTWRITEBYTECODE=1`, en scripts efímeros
del scratchpad que no importan de `scripts/` salvo en la auditoría del
certificado.

## Preflight

| Elemento | Resultado |
| --- | --- |
| Repo | `github.com/nacho09021973/qca-causal-cones` |
| Rama | `research/b-infinity-post-s4-gate` |
| `HEAD` | `817050d8e80e6d6e636937b5794d60ff67e6e047` |
| `origin/research/b-infinity-post-s4-gate` | `817050d8e80e6d6e636937b5794d60ff67e6e047`, también en `ls-remote` tras `fetch` |
| Tracked | sin cambios; `git diff --check` vacío |
| Untracked | 4 preexistentes y 3 nuevos (informe, certificado, self-review); `__pycache__` intacto (08:45:20) |
| Commit que publicó el charter | `817050d`, 09:52:56; push 09:53:02 (reflog); único commit que toca el archivo en todas las refs |
| Bytes del charter | `git show 817050d:…` = archivo de trabajo = sha256 `3d559ced…41ba9` |

**Secuencia temporal** (commit y reflog para el charter; tiempos de
nacimiento del sistema de archivos para los untracked, que no son
criptográficos):

1. Charter publicado: 09:52:56 (push 09:53:02).
2. Ejecución: cordura efímera 10:03, certificado 10:09 (modificado 10:12),
   informe 10:14:08.
3. Self-review: 10:28:52.
4. **Reparaciones textuales: NO EXISTEN.** El informe no ha cambiado desde su
   creación (birth = modify = 10:14:08; sha256 `5d3e7125…`) y conserva las
   frases de R1–R3.
5. Esta revisión: 10:41 en adelante.

La secuencia pedida (charter → ejecución → reparaciones → revisión) **se rompe
en el paso 4**.

**Encabezado del charter** (líneas 3–7). Sigue diciendo `HEAD=11efe1f`,
remoto `780ecb0` y "publicación/versionado y ejecución pendientes"; no hay
enmienda en ninguna ref. **No altera el contrato científico:** §§1–15 son el
blob publicado antes de cualquier cálculo, y el encabezado sólo describe la
base de redacción. Es un defecto administrativo.

## 1. Clase congelada

Leída en el charter (§§2–5):

- CJWW (5.15), una partícula, `S = W^dagger`, con la convención de Fourier
  `hat psi = sum e^{ip.x} psi`, `dmu = d^3p/(2pi)^3` y `mu(B) = 1`;
- nodo `p = 0`, con `Pi_Lambda = 1_{|p|<=Lambda} (x) I_2`: ambas componentes
  internas y ambas ramas, sin proyector de helicidad;
- `g(q) = (1-|q|^2)^2 1_{|q|<1}`, espín `down`, `psi_Lambda = S^2 phi_Lambda`;
- `U_0 = I`, `U_1 = e^{i pi n_0} = I - 2P_0`, con `P_0 = |0><0| (x) I_2`;
- Bob en `y_B = (1,1,0)`, `Delta T = 1`, dominio `0 < Lambda < pi/4`.

El informe reproduce exactamente estos parámetros. Ninguna elección de perfil,
nodo, Bob, tiempo, encoder o criterio es posterior a los resultados. Lo único
añadido después son constantes de cota y comentarios, y ninguno cambia el
criterio.

## 2. Normalización y peso en Alice

**Ruta de rebanadas** (distinta de la Beta de la self-review y de la radial del
certificado):

`int_{|q|<1} (1-|q|^2)^n d^3q = int_{-1}^{1} dz int_0^{sqrt(1-z^2)} 2 pi rho (1 - z^2 - rho^2)^n drho = (pi/(n+1)) int_{-1}^{1} (1-z^2)^{n+1} dz`.

Con el jacobiano `Lambda^3/(2pi)^3`, que es la normalización de Parseval:

- `kappa = Lambda^3/(6 pi^2)`;
- `Z = 64 Lambda^3/(3465 pi^2)`;
- `(int g)^2/Z = 11 Lambda^3/(140 pi^2)`.

**Confirmado.** Revisé factores `2pi`, volumen, cambio de variable (`p =
Lambda q`) y degeneración de espín: `P_0` incluye ambos espines y `s` suma
ambas componentes.

**Amplitud en el sitio.** Por producto directo de matrices,
`S^2|down> = (2 c1c2c3 (c1 s2 - i s1), c1^2 c2^2 (1 + e^{2ip3}) - 1)`.

- La parte real de la componente superior es impar en `p2` y la imaginaria es
  impar en `p1`. La parte imaginaria de la inferior es impar en `p3`.
- La `g` radial anula las partes impares, así que `psi(0) = (0, c_down)`, con
  `c_down = Z^{-1/2} int g F dmu` y `F = 2 prod c_i^2 - 1`.
- La parte par es la misma con `W^2`, así que la convención de rama o de signo
  no altera `s`.

**Positividad, con una prueba distinta de la del informe** (producto de
Weierstrass): `cos x = prod_k (1 - 4x^2/((2k-1)^2 pi^2))`. Para `|p| < pi/2`,
cada factor `a_{k,i} = 4p_i^2/((2k-1)^2 pi^2)` está en `[0,1)` y cumple
`sum_i a_{k,i} < 1`. De `prod_i (1 - a_{k,i}) >= 1 - sum_i a_{k,i} > 0`,
multiplicando sobre `k` (productos absolutamente convergentes):

`prod_i cos p_i >= cos|p|`.

Sobre el soporte de `g` esto da `cos 2Lambda <= F <= 1`, luego

`cos^2(2Lambda) 11 Lambda^3/(140 pi^2) <= s <= 11 Lambda^3/(140 pi^2)`

y `s ~ 11 Lambda^3/(140 pi^2)`. **Confirmado.**

**Independencia de estas constantes.** El veredicto no usa `11/140` ni
`c_up = 0`. Sólo necesita `0 < s`, que aquí está probado, y `s <= kappa`, que
es Cauchy–Schwarz: `|psi(0)|^2 = |int_ball hat psi|^2 <= kappa`.

## 3. Efecto del encoder

`U_1 psi - psi = -2 P_0 psi = -2e`, con `e = delta_0 (x) psi(0)`: soporte
espacial en un único sitio, y `hat e(p) = psi(0)` **constante** en toda `B`.
Hay que separar tres cosas:

| Aspecto | Valor |
| --- | --- |
| Espectro | plano, con valor constante `psi(0)` |
| Peso total | `\|\|e\|\|^2 = s` |
| Bloque IR de `e` | `\|\|Pi e\|\|^2 = kappa s` |
| Bloque UV de `e` | `\|\|(I-Pi) e\|\|^2 = (1-kappa) s` |

La coherencia IR–UV no es una propiedad de `e`, sino de `Delta` (§§5 y 7). En
cuanto al resto del estado, `f = psi - e` tiene fuera de la banda exactamente
`-(I - Pi) e`, porque `psi` está en la banda.

## 4. `||Delta_Lambda||_1`

- **Subespacio bidimensional** `span{psi, U_1 psi}` con solapamiento real
  `gamma = <psi|U_1 psi> = 1 - 2s`: `Delta` tiene traza `0` y determinante
  `-(1 - gamma^2)`, así que `||Delta||_1 = 2 sqrt(1 - gamma^2)`.
- Sustituyendo, `||Delta||_1 = 4 sqrt(s(1-s))`. **Confirmado** para
  `0 <= s <= 1`, dominio activo `0 < s < 1`.
- **Convención `Delta = 0`:** sólo ocurriría con `s ∈ {0, 1}`. Aquí
  `0 < s <= 11 Lambda^3/(140 pi^2) < 1`, así que nunca se activa.

## 5. Proyección IR

Sean `w = Pi U_1 psi` y `h = (I - Pi) U_1 psi = -2(I - Pi) e`. Como
`Pi psi = psi`:

- `Pi Delta Pi = |w><w| - |psi><psi|`;
- `R = |w><h| + |h><w| + |h><h|`.

Con `a = ||w||`, `b = ||h||`, `b^2 = 4s(1-kappa)` y `a^2 = 1 - b^2`, se tiene
`||R||_1 = b sqrt(b^2 + 4a^2) = 4 sqrt(s(1-kappa)(1 - 3s(1-kappa)))`, y
`eta_enc^2 = (1-kappa)(1 - 3s(1-kappa))/(1-s)`. **Confirmado.**

**Segunda vía: un caso exacto de 8 dimensiones.** Posición `C^4` y espín
`C^2`, `Pi = diag(1,1,0,0) (x) I_2`, `P_0 = |delta><delta| (x) I_2` con
`delta = (3/5, 0, 4/5, 0)`, y `psi = e1 (x) (3/10, 4i/10) + e2 (x) (1/2, (1+i)/2)`,
que tiene **ambas componentes de espín en el sitio**, `s = 9/100` y
`kappa = 9/25`. Los autovalores exactos dan `||Delta||_1 = 3 sqrt(91)/25` y
`eta^2 = 33088/56875`, ambos iguales a la fórmula.

**Hipótesis de la fórmula:**

- (H1) `Pi_Lambda psi = psi` exacto;
- (H2) `||psi|| = 1`;
- (H3) `U_1 = I - 2P_0`, con `P_0` el proyector de un solo sitio (con
  degeneración de espín);
- (H4) `||Pi (delta_0 (x) v)||^2 = kappa ||v||^2`, que es espectro plano con
  la bola dentro de `B` (`Lambda < pi`);
- (H5) `0 < s < 1`;
- (H6) evaluación en `n = 0`, sector de una partícula.

`s <= kappa` se deduce de (H1)–(H2) y no es una hipótesis. Con `[S, Pi] = 0`
y `S` unitario, el mismo cociente vale también para `Delta(1)`, así que el
veredicto no depende de a qué `n` se refiera §7.

## 6. Cota global

**Prueba más simple que la del informe.**

- `eta^2 - (1 - 4kappa) = [(3kappa - 2s) + s kappa(2 - 3kappa)]/(1-s) > 0`
  para `0 < s <= kappa < 2/3`, luego `eta^2 > 1 - 4kappa`.
- `kappa` crece con `Lambda`, y `kappa(pi/4) = pi/384`.
- Basta **`pi < 2 sqrt3`** (semiperímetro del hexágono regular circunscrito):
  `1 - 4kappa > 1 - 2sqrt3/96 > 24/25`, porque `sqrt3 < 48/25`.

Por tanto **`eta_enc > 2 sqrt6/5` en todo `0 < Lambda < pi/4`, con
desigualdad estricta**, porque las desigualdades `Lambda < pi/4` y
`eta^2 > 1 - 4kappa` son estrictas. Sirve cualquier cota `pi < 3.84`.

Las cotas auxiliares del informe (`s <= kappa`, concavidad y `pi < 22/7` por
Dalzell) también son correctas, pero no son necesarias.

## 7. Límite IR y lectura permitida

- `s <= kappa -> 0`.
- `||Delta||_1 <= 4 sqrt(kappa) -> 0`.
- `epsilon_UV = 4s(1-kappa) <= 4kappa -> 0`.
- `1 - 4kappa < eta^2 <= 1`; la cota superior se sigue de
  `1 - eta^2 = (kappa - s + 3s(1-kappa)^2)/(1-s) >= 0`.

Por tanto **`lim eta_enc = 1`, demostrado**, sin usar `11/140`.

**Descomposición de `R`**, exacta tanto simbólicamente como en el caso de 8
dimensiones:

| Bloque | `\|\|·\|\|_1 / \|\|Delta\|\|_1` | Límite |
| --- | --- | --- |
| IR–UV, `Pi R (I-Pi) = \|w><h\|` | `(1/2) sqrt((1-kappa)(1-4s(1-kappa))/(1-s))` | `1/2` |
| UV–IR, `(I-Pi) R Pi = \|h><w\|` | igual | `1/2` |
| UV–UV, `\|h><h\|` | `(1-kappa) sqrt(s/(1-s))` | `0` |

**Dominan conjuntamente las coherencias IR–UV y UV–IR.**

- **Afirmación permitida:** establecida tal como está formulada.
- **"La señal es puramente UV":** no establecida. No se calculó señal alguna.
- **"La codificación es esencialmente UV":** refutada como descripción de
  `R`. El bloque UV–UV es relativamente despreciable.
- **"Toda la información vive en modos UV":** no establecida.

## 8. Carta y error Weyl

- **Otros nodos:** `W = ±I` exige `s1 = 0` y `c1 s2 = 0`, y dentro de la carta
  eso fuerza `p = 0`. Es un argumento directo, sin lema.
- **Logaritmo:** `cos omega = c1c2c3 >= cos|p| > cos(pi/4)` (Weierstrass), así
  que `omega < pi/4`, lejos del corte en `pi`, con rama continua y `H(0) = 0`.
- **`r_W <= R_W < 5 Lambda^2`:** cadena analítica correcta (descomposición,
  restos de Taylor, Frobenius, cota espectral, telescopio). Por software sólo
  están certificadas las identidades y la desigualdad racional final. Las
  constantes `25/18` y el prefactor `3` son manuales, y hay mutaciones que
  sobreviven (§12).
- **Irrelevante para la stop rule:** el fallo de §7 no usa `R_W`.

## 9. Stop rule

§7, literal: "Una demostración de incompatibilidad en todo entorno perforado
del origen cierra negativamente la clase por control IR, **sin calcular
`D_B`**. Una cota demasiado débil o un intento de prueba fallido deja el
resultado abierto."

El resultado es una identidad exacta con `eta_enc > 2 sqrt6/5` en toda la
carta y límite `1`: es incompatibilidad, no una cota débil. §10 da como razón
válida "incompatibilidad del encoder con el criterio IR", y la fila 3 exige
"obstrucción probada a los criterios positivos para esta familia asintótica".

- **¿Era correcto NO calcular `D_B(Lambda)`?** **Sí.** §7 (líneas 240–241) y
  §13.2 obligan a detenerse.
- **¿El negativo requiere `D_B = 0`?** **No.** §10: "Una prueba de
  incompatibilidad no afirma `D_B=0` para el walk."

## 10. Alcance

| # | Afirmación | Clasificación |
| --- | --- | --- |
| 1 | `3/128` queda invalidado | `NOT_SUPPORTED`: otro protocolo; charter §11 y §10 fila 3; su verificador pasa 21/21 |
| 2 | Ningún encoder produce señalización IR | `NOT_SUPPORTED`: sólo se analizó `I - 2P_0` bajo `eta_enc` |
| 3 | El encoder puntual congelado no satisface el criterio relativo | `SUPPORTED` |
| 4 | Cambiar sólo el perfil, manteniendo soporte espectral exacto, rescata necesariamente el encoder | `NOT_SUPPORTED`: con (H1)–(H6) la misma identidad da `eta^2 > 1 - 4kappa`, y si `psi(0) = 0` no hay diferencia codificada. Además sería otro contrato |
| 5 | Las coherencias IR–UV dominan el residuo relativo cuando `Lambda -> 0` | `SUPPORTED`, entendiendo IR–UV y UV–IR conjuntamente, para la diferencia global de una partícula en `n = 0` |
| 6 | No hay señalización en el límite continuo físico | `NOT_SUPPORTED`: no hay `D_B`, `Lambda -> 0` no es `a, tau -> 0`, no hay escala |
| 7 | Vale sólo para la clase preregistrada | `SUPPORTED` |
| 8 | Toda intervención estrictamente local falla en cualquier QCA | `NOT_SUPPORTED` |

## 11. Reparaciones R1–R4: **no aplicadas**

El informe revisado (sha256 `5d3e7125…`, sin cambios desde 10:14:08) conserva
versiones equivalentes de los claims prohibidos:

| Reparación | Estado | Evidencia en el informe |
| --- | --- | --- |
| R1 | **pendiente** | l. 5–7 "fuera de la banda … `eta_enc -> 1`"; l. 256 "vive fuera de la banda" |
| R2 | **pendiente** | l. 258 y l. 414 "codificación esencialmente UV" |
| R3 | **pendiente** | l. 334–336 "ese mecanismo … no queda dentro del régimen IR" |
| R4 | **pendiente, parcial** | la convención [V]/[A] existe, pero: l. 17 define [A] como "a partir de pasos [V]", lo cual es falso para los Lemas 1, 3 y 4 y para la reducción a `V`; l. 246–248 marcan [V] el límite por compresión y una desigualdad; l. 291 dice "con certificado exacto"; §12 no lista los pasos sin cobertura |

## 12. Certificado software (secundario)

- **Ejecución:** 34/34 y exit 0, con SymPy 1.14.0 exacto.
- **Correspondencia fórmula ↔ código:** correcta en los checks decisivos: 10,
  23–27, 30–31 y 33–34.
- **Punto flotante:** `main()` no crea ningún `Float` finito. **Corrección a
  la self-review:** al importar `verify_directional_saturation`, `sp.simplify`
  (línea 84) carga `sympy.physics.units`, que crea **17** `Float` finitos
  (constantes físicas de la librería). No entran en ninguna expresión del
  certificado.
- **Imports:** la dependencia transitiva de **numpy** (línea 517) hace fallar
  el import si numpy no está instalado, y `scripts/requirements.txt` sólo
  declara `sympy`. Con un `is_zero` vacuo y un símbolo erróneo, el certificado
  aún falla (check 3); con un símbolo erróneo y el `is_zero` real falla en el
  check 2.
- **Mutaciones nuevas:** mueren 10 de 10:
  - convención `S = W`;
  - `(2pi)^2` en lugar de `(2pi)^3`;
  - puerta no unitaria;
  - intercambio de `e_in` y `e_out`;
  - exponente 3 en `g`;
  - umbral `97/100`;
  - signo de `e2(L)`;
  - suelo `(1-k)(1-5k)`;
  - signo del término lineal;
  - `R = L`.

**Huecos:**

| Hueco | Sonda (sobrevive con 34/34) | Clasificación |
| --- | --- | --- |
| Constante `25/18` y prefactor `3` de `R_W` | sí / sí | `SOFTWARE_ONLY_GAP`, irrelevante para la stop rule |
| Cotas de `s` (Lema 4) | sí | `SOFTWARE_ONLY_GAP`, reprobado aquí; el veredicto sólo usa `s > 0` y `s <= kappa` |
| Lema de la carta (Lema 1) | sí | `SOFTWARE_ONLY_GAP`, reprobado aquí con Weierstrass |
| Ruta elemental (identidad trivial) | sí | `SOFTWARE_ONLY_GAP`, redundante |
| Espectro plano y reducción fiel a `V` | no codificable en el script | `SOFTWARE_ONLY_GAP`, reprobado en el caso de 8 dimensiones |
| Signos `e2 <= 0` y numeradores `>= 0` | por inspección | `SOFTWARE_ONLY_GAP` |
| **Mitad superior `eta <= 1` del sándwich** (no señalado por la self-review) | sí | `SOFTWARE_ONLY_GAP`; sólo afecta a "límite = 1", no a `eta ↛ 0` |
| **Vínculo `k_chart` ↔ `kappa(pi/4) = pi/384`** (no señalado por la self-review) | sí (`/385` sobrevive) | `SOFTWARE_ONLY_GAP` |
| Paridad ⇒ integrales nulas | sí | `SOFTWARE_ONLY_GAP` |
| numpy no declarado | — | `SOFTWARE_ONLY_GAP` (reproducibilidad, preexistente) |

`PROOF_GAP`: ninguno encontrado. `VERDICT_THREATENING_GAP`: ninguno.

**Regresiones**, todas con exit 0:

- nuevo certificado 34/34;
- `verify_directional_saturation.py` 27/27, `--local-preparation-only` 21/21,
  `--noncorner-gate-only` 20/20;
- `verify_signaling_witness.py` 17/17;
- Weyl/Dirac, 375 checks;
- los dos scripts S4: PASS.

## 13. Script nuevo frente al charter

§13 dice: "No se crea un script nuevo salvo necesidad demostrada y
autorización de implementación". Es una prohibición condicional.

- **Necesidad:** el propio charter excluye los helpers de soporte finito para
  este paquete y protege los bytes de los verificadores revisados, y
  `scripts/README.md` exige código trazado.
- **Autorización:** la documenta el informe (§11). Fuera de ese informe no
  consta en el repo.
- **Efecto:** el veredicto descansa en una prueba analítica reproducida aquí
  sin el script.

**`DOCUMENTED_IMPLEMENTATION_DEVIATION_WITHOUT_SCIENTIFIC_EFFECT`.**

## 14. Veredicto

### `PASS_WITH_MANDATORY_REPAIRS`

No puede ser `PASS`, porque las reparaciones obligatorias no están
incorporadas. No es `FAIL`, porque todas las inferencias centrales están
demostradas. **Ningún cambio afecta al resultado.** Cambios exactos necesarios:

1. **(R1)** Línea 5–7: "la fracción de la diferencia codificada que queda fuera
   de la banda" debe decir "la fracción, en norma de traza, de la diferencia
   codificada que queda fuera del bloque `Pi_Lambda Delta Pi_Lambda`". Línea
   256: sustituir por "el cociente
   `eta_enc = ||Delta - Pi Delta Pi||_1/||Delta||_1` tiende a 1".
2. **(R2)** Líneas 257–258: "pasar §6 en norma absoluta ocultaría una
   codificación esencialmente UV" debe decir "la fuga absoluta de §6 tiende a
   cero aunque la diferencia codificada no quede asintóticamente en el bloque
   IR–IR; el residuo está dominado por coherencias IR–UV y UV–IR y el bloque
   UV–UV es relativamente `O(sqrt s)`". Línea 414: "habría aceptado una
   codificación esencialmente UV" debe decir "habría aceptado una diferencia
   codificada que no queda asintóticamente en el bloque IR–IR".
3. **(R3)** Líneas 334–336: sustituir por "Lo que establece es que la puerta
   puntual congelada, aplicada a la familia narrow-band congelada, falla el
   criterio relativo de §7; no dice nada sobre el protocolo ultralocal de
   `3/128`".
4. **(R4)** Cuatro cambios:
   - línea 17: definir [A] como "paso analítico probado en este informe y no
     certificado por software";
   - líneas 246–248: marcar [A] la compresión y la desigualdad, y [V] sólo el
     límite del suelo y la identidad del cociente;
   - línea 291: "Demostrado analíticamente; el certificado cubre sólo las
     identidades [V]";
   - en §12, añadir la lista de pasos sin cobertura de software y las
     mutaciones que sobreviven: los Lemas 1, 3 y 4, la reducción a `V`, la
     cadena y las constantes de `R_W`, los signos, `eta <= 1` y
     `kappa(pi/4)`.
5. **(Estado)** No usar `INDEPENDENTLY_REVIEWED` (§15).
6. **(Self-review, si se conserva en el registro)** Corregir su §10: "ningún
   float finito" vale para `main()`; el import crea 17 `Float` de
   `sympy.physics.units`, ajenos al cálculo.

**Recomendadas:**

- enunciar en §4.6 del informe las hipótesis (H1)–(H6);
- cambiar la línea 143, "§6 se cumple", por "los controles absolutos de §6
  (`epsilon_UV -> 0`, `R_W -> 0`) se cumplen";
- declarar numpy en la entrada del README o en los requisitos;
- renombrar el check 1;
- opcionalmente, sustituir la cadena Dalzell/concavidad por la cota
  `eta^2 > 1 - 4kappa` con `pi < 2 sqrt3`;
- corregir el encabezado del charter en un acto administrativo separado.

## 15. Estado congelable

**`PARTIAL_REVIEW_PASS_WITH_REPAIRS / INDEPENDENT_REVIEW_PENDING`.**

`NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED`
**no está autorizado**, por dos razones:

- esta revisión no se hizo desde un contexto independiente;
- las reparaciones obligatorias no están incorporadas.

La etiqueta sólo sería legítima tras una revisión en un contexto nuevo, sin
acceso a esta sesión, que reconstruya las partes decisivas, y con R1–R4 ya
aplicadas.
