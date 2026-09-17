# Revisión independiente: SCALED_IR_SIGNALING_GATE

**Fecha:** 2026-09-17. **Rama:** `research/b-infinity-post-s4-gate`.

**Veredicto de revisión: `PASS`.** No hay reparación obligatoria de cantidades
ni de clasificación. Hay aclaraciones recomendadas de redacción, ninguna de
las cuales cambia `J`, el prefactor `36 N^4` ni el estado terminal.

**Veredicto científico revisado:** `OPEN_AFTER_SCALED_IR_ANALYSIS`.
**Correcto.**

**Estado congelable hoy:**
`OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.

Resultado cuantitativo central, rederivado en esta revisión:

\[
\delta_{M,M_B}(N)\le D_B(N)\le 36 N^4
\exp\!\left[
-\left(1-\frac{\sqrt3}{2}\right)(\log 2)\,N
\right],
\qquad N\ge 2,
\]

en el sector de una partícula de la clase congelada. Esto **excluye**
`IR_RESOLVABLE_SIGNALING_POLYNOMIAL` y **no autoriza**
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. No se afirma
\(\delta_B(N)>0\).

## 0. Independencia y convenciones de evidencia

**Contexto.** Revisión en contexto frío del resultado ya escrito. El mensaje
de encargo enunciaba las fórmulas objetivo (`J`, `36 N^4`, la exclusión
polinómica y el estado `OPEN_AFTER_SCALED_IR_ANALYSIS`). La derivación es
propia; no es ciega a los valores reclamados.

**Orden seguido:**

1. charter íntegro `theory/SCALED_IR_SIGNALING_GATE.md`;
2. `walk2()`, `laurent`, `PAULI` y `exact_blocks` (sólo para contrastar
   convenciones, después de transcribir el símbolo a mano);
3. `PROJECT_INSTRUCTIONS.md` y el criterio de `D_B` del charter
   narrow-band;
4. derivación a mano de geometría, contorno, elipses, Schur, `T_N` y `D_B`;
5. script exacto propio, **sin importar** `scripts/`
   (`/tmp/scaled_ir_own_derivation.py`, `/tmp/scaled_ir_blocks.py`);
6. **sólo después**, informe de ejecución, certificado y `CURRENT_STATE`.

No se consultaron PDFs de `biblioteca/`. DP14, BDP17 y BB93 no se usan.

**Etiquetas:**

| Etiqueta | Significado |
| --- | --- |
| **[M]** | demostrado a mano en esta revisión |
| **[C]** | SymPy exacto propio, sin importar el certificado del gate |
| **[X]** | ejecutado u observado (git, sha256, suite del certificado) |
| **[L]** | leído; no rederivado al mismo profundidad |

El código propio es apoyo de revisión, no evidencia retenida.

**Entradas revisadas (sha256) [X]:**

| Archivo | sha256 |
| --- | --- |
| `theory/SCALED_IR_SIGNALING_GATE.md` | `325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c` |
| `reports/2026-09-17--scaled-ir-signaling-gate.md` | `4876ecab8ed6a7000aa2d2b991ad4bbb12a3f29538d2a7be910fb9c5476b7f31` |
| `scripts/verify_scaled_ir_gate.py` | `b8c6b56ea114b7cf135c73d344dc7a4911d43d7cba8cef609ea3dcfee415763c` |
| `state/CURRENT_STATE.md` (sin el resultado; no modificado por la ejecución) | `7cb84de881b4a03b751842ef4f46a1bf10f54a1c6fd468c6029cfa5acf791098` |
| `theory/NARROW_BAND_SIGNALING_GATE.md` (definición heredada de `D_B`) | `3d559cedefa0b6c25bd0af7ef13a993e2b71e1a8f7f97ae4f29f988147541ba9` |

## 1. Integridad del preregistro [X]

| Elemento | Resultado |
| --- | --- |
| `HEAD` | `31b5797119a9aad03b11c5ee00db99e0d96ed9e4` |
| `origin/research/b-infinity-post-s4-gate` | el mismo hash |
| Tracked | sin cambios (`git diff` y `git diff --cached` vacíos) |
| Charter | único archivo de `31b5797`; blob = working tree = sha256 `325fd416…` |
| Informe y certificado | untracked; no hay commit de ejecución |
| `CURRENT_STATE.md` | no menciona aún este gate; hash idéntico al declarado en el preflight del informe |

La clase ejecutada coincide con la congelada: CJWW (5.15), una partícula,
`S = adj W`, Fourier `e^{+ip·x}`, bolas euclídeas de radio `N/4`,
`Delta T = N`, `Lambda = 1/N`, `Lambda' = N^{-1/2}`, familias internas
`{I,σ1,σ2,σ3}` y `{I,(I+σj)/2}`, perfiles `(1-16|·|^2/N^2)^2_+`, `theta=π/2`.
Ningún parámetro de geometría, encoder, detector o carta se cambió después
de ver un número.

## 2. Ataque 1 — de la geometría regional a `J>0`

### 2.1 Geometría de las regiones completas [M]

Con `u=(1,1,1)`, `x\in A_N`, `y\in B_N`:

\[
u\cdot x\le |u|_2\,|x|_2\le \frac{\sqrt3}{4}N,
\qquad
u\cdot y\ge 3N-\frac{\sqrt3}{4}N,
\]

luego

\[
u\cdot(y-x)\ge\Bigl(3-\frac{\sqrt3}{2}\Bigr)N. \tag{G}
\]

La red está contenida en las bolas continuas cerradas, así que el mínimo
discreto no puede ser peor. El margen euclídeo
`|y-x|_2-N\ge(\sqrt3-3/2)N>N/5` se usa para la admisibilidad causal del
contrato, **no** para el exponente: la tasa sale del tilt `u·(y-x)`, no de
una LDP radial. `3>(17/10)^2` es exacto [C].

### 2.2 Convención de Fourier y signo del contorno [M]

Con `hat psi(p)=\sum_x e^{ip·x}psi(x)` y `S(p)=\sum_d S_d e^{ip·d}`,

\[
(S^N)_{y,x}=\int S(p)^N e^{-ip·(y-x)}\,d\mu,
\qquad d\mu=\frac{d^3p}{(2\pi)^3}.
\]

El integrando es un polinomio trigonométrico entero, periódico, sin polos.
Desplazar el 3-toro real a `p\mapsto p-itu`, `t=\log 2`, no cruza
singularidades. El factor es `e^{-t\,u·(y-x)}`. El signo es el que decae
cuando `y-x` apunta hacia `(N,N,N)`. Un desplazamiento opuesto **invalidaría**
la cota; el informe usa el signo correcto.

### 2.3 Producto de elipses [M]/[C]

`cos(p_j-it)` recorre exactamente la frontera de
`E_{\cosh t}=E_{5/4}`. El lema `E_a E_c\subset E_{ac}` se rederivó
construyendo la matriz real `L` de la multiplicación, **incluyendo el
término extra-diagonal** de `I-L^\top L`, que el informe no escribe.

Para las cuatro combinaciones de signos de `(\cos p,\sin p)` [C]:

- `(I-L^\top L)_{11}` y `(I-L^\top L)_{22}` coinciden con las fórmulas
  del informe;
- el determinante coincide con la fórmula del informe;
- `(I-L^\top L)_{12}\ne 0` si `0<u<1`.

En `2\times 2` simétrica, `g_{11}\ge 0` y `\det\ge 0` bastan para
`I-L^\top L\ge 0` (criterio de Sylvester). El extra-diagonal queda
absorbido en el determinante que el informe sí usa. Los tres polinomios
son no negativos para `A,C>1`, `0\le u\le 1`. Los interiores de `E_a` son
contracciones radiales; `E_{ac}` es estrellado en el origen. Aplicado dos
veces: `f(p-itu)\in E_{125/64}` uniformemente en el toro real.

El certificado **no construye** `L`; comprueba identidades entre
expresiones. Esa inclusión queda certificada por esta revisión, no por
`53/53`.

### 2.4 Radio espectral y potencia [M]/[C]

`det S\equiv 1` como identidad de polinomio [C], también fuera del toro
real. Autovalores `λ,λ^{-1}`, `f=(λ+λ^{-1})/2`. Joukowski: `f\in E_a` sii
el radio espectral es `\le a+\sqrt{a^2-1}`. Con `a=125/64<17/8=\cosh(\log 4)`
se tiene `ρ(S(p-itu))<4`, incluso en colisiones `f=\pm 1`. No se elige rama
global ni se divide por un gap.

Suma de normas de los catorce bloques de `S` [C]: ocho vértices de norma
`1/4`, cuatro `(±1,±1,0)` de norma `1/4`, dos axiales `(±1,0,0)` de norma
`1/2`; total `4`. Luego `\|S(p-itu)\|\le 4 e^{3t}=32`. En forma de Schur,
`|b|\le 32` y `|λ_j|<4`.

\[
T^N=\mathrm{diag}(λ_1^N,λ_2^N)+(\mathrm{off})\,|e_1\rangle\langle e_2|,
\]
\[
\|T^N\|_2\le \max(|λ_1^N|,|λ_2^N|)+|\mathrm{off}|
\le 4^N+32 N 4^{N-1}\le 9N\,4^N\qquad(N\ge 1).
\]

La cadena (P) del informe es correcta: la norma de la diagonal es el
máximo, no la suma de las dos entradas. (Una lectura de Frobenius con tres
términos da `(8N+2)4^N`, que también es `\le 9N 4^N` para `N\ge 2`; no hace
falta.) El factor `N` es de Jordan; no se divide por separación de
autovalores.

### 2.5 Exponente [M]/[C]

\[
\|(S^N)_{y,x}\|\le 9N\,4^N\exp\bigl[-t\,u\cdot(y-x)\bigr].
\]

Con (G) y `t=\log 2`, `4^N=e^{N\log 4}`,

\[
-t\Bigl(3-\frac{\sqrt3}{2}\Bigr)+\log 4
=\log 2\cdot\Bigl(-1+\frac{\sqrt3}{2}\Bigr)
=-\Bigl(1-\frac{\sqrt3}{2}\Bigr)\log 2.
\]

Identidad `expo+J=0` [C]. `J>0` porque `√3<2` (`3<4`) y `log 2>0`.
`J` es una **tasa inferior de una upper bound**, no `I(v)` ni una
equivalencia asintótica. Vale en todo `(B_N-A_N)/N` porque se usó el
mínimo del tilt.

**Ataque 1: PASS.** El paso geometría regional → kernel está cerrado.

## 3. Ataque 2 — el prefactor `36 N^4` y la uniformidad

### 3.1 De kernels a `T_N` [M]

Cada región está en un cubo de lado `N/2`: a lo sumo
`(N/2+1)^3\le N^3` sitios para `N\ge 2` (igualdad en `N=2`). Cauchy–Schwarz
en `ℓ^2(Z^3,C^2)`, con la norma `2\times 2` ya dentro de `\|K_{yx}\|`,

\[
T_N:=\|P_{B_N}S^N P_{A_N}\|\le N^3\cdot 9N\,e^{-JN}=9N^4 e^{-JN}.
\]

No hay factor extra por los dos modos internos. El `N^4` es `N` de Jordan
por `N^3` de sitios. La cota usa el **peor** par de sitios (mínimo tilt);
los demás decaen al menos igual de rápido. Pares microscópicamente fuera
de `[-N,N]^3` tienen kernel cero y no empeoran la cota.

### 3.2 De `T_N` a `D_B` [M]

El modelo del charter está en el **sector de una partícula**. Para cualquier
puro normalizado y cualquier unitario que sea la identidad fuera de Alice,

\[
\|v_1-v_0\|=\|P_B S^N(U_1-I)\psi\|\le 2 T_N,
\]

porque `(U_1-I)psi` vive en `A_N`. El recurso **no** tiene que estar
soportado en Alice.

Estados reducidos de Fock en los modos de Bob:

\[
\rho_b=(1-\|v_b\|^2)|\mathrm{vac}\rangle\langle\mathrm{vac}|+|v_b\rangle\langle v_b|.
\]

Convención, heredada del charter narrow-band l. 16 y compatible con
`D_B\ge\delta` del charter escalado: `D_B=\tfrac12\|\rho_1-\rho_0\|_1`.
Con `X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|` y `α=-\mathrm{tr}\,X`
en el bloque de vacío,

\[
D_B=\tfrac12\bigl(|α|+\|X\|_1\bigr)\le\|X\|_1
\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le 4 T_N\le 36 N^4 e^{-JN}.
\]

`|Tr E(ρ_1-ρ_0)|\le D_B` para `0\le E\le I`. La cadena (D1) del informe
es correcta **bajo esta convención de `1/2`**, que el informe comprime en
la frase del bloque de vacío. Si alguien leyera `D_B=\|ρ_1-ρ_0\|_1` sin
`1/2`, el prefactor pasaría a `72` y la forma `C N^4 e^{-JN}` **no
cambiaría**; la exclusión polinómica tampoco.

Convexidad de la distancia de traza extiende (D1) a mixtos de una
partícula. Los dieciséis pares del protocolo viven en este sector. La cota
(DF) CAR del informe **no se usa** para clasificarlos y **no se certifica**
aquí; el charter §2 ya restringe a una partícula.

### 3.3 Uniformidad sobre regiones y pares [M]

- La constante `36=4\times 9` no depende de `M` ni de `M_B`:
  `\|U_M-I\|\le 2` para toda la familia, y `D_B` acota los cuatro
  detectores de cada encoder.
- Vale para todo `N\ge 2`. Cuando el lado derecho supera `1`, se usa
  además `D_B\le 1`; el informe toma `U_N=\min(1,36 N^4 e^{-JN})`.
- No se afirma que `36` ni el `N^4` sean óptimos. El volumen euclídeo es
  `O(N^3)` con constante menor que la del cubo; eso sólo afloja el
  prefactor, no la tasa.

**Ataque 2: PASS.** `36 N^4` domina uniformemente las regiones congeladas
y los dieciséis pares. No es una cota por par seleccionada a posteriori.

## 4. Ataque 3 — exclusión polinómica sin existencia

### 4.1 Lo que el charter permite asignar [M]

Orden de §7, sin solapes:

1. `NO_IR_ADMISSIBLE_ENCODER_IN_FROZEN_FAMILY` — no: las tres Pauli y el
   control pasan el criterio IR del informe (reconstrucción [L]/[M] de
   (IR1) y denominadores; no se encontró obstrucción que active la stop
   rule; profundidad menor que §§2–3).
2. `NO_SIGNALING_IN_SCALED_IR_CLASS` — no: exige `D_B=0` exacto, no una
   cota.
3. `IR_RESOLVABLE_SIGNALING_POLYNOMIAL` — exige un par Pauli admisible con
   `δ(N)\ge c N^{-p}` para todo `N\ge N_*`.
4. `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` — exige lower bound
   exponencial o asintótica de amplitud no nula, **y** upper exponencial.
5. `OPEN_AFTER_SCALED_IR_ANALYSIS` — resto.

Regla explícita del charter: una upper bound con `J>0` **excluye** (3) y
**no autoriza** (4).

### 4.2 Por qué (3) queda excluida [M]

Para cada uno de los dieciséis pares, `δ_{M,M_B}(N)\le D_B(N)\le 36 N^4 e^{-JN}`.
Si existiera `c>0`, `p` y `N_*` con `δ(N)\ge c N^{-p}` para todo `N\ge N_*`,
entonces `c N^{-p}\le C N^q e^{-JN}` para todo `N` grande, absurdo. La
señal evaluada es la física, **sin** proyección espectral, como exige el
charter §5. Una cota sobre un bloque `Π'ΔΠ'` no se usó para esta
exclusión.

Esto descarta la **ley** polinómica resoluble en la clase congelada. No
descarta que, a `N` moderado, `36 N^4 e^{-JN}` aún sea `>1` y no sea
informativa numéricamente.

### 4.3 Por qué no hay afirmación de existencia [M]

`O(N^4 e^{-JN})` incluye `0`. La tabla del informe marca los dieciséis
pares `OPEN_PAIR`, lower bound trivial `0`, signo no decidido. No hay
asintótica `A(N)\ne 0`. El control `I` no se usa como testigo positivo.
Identidades (L) y (F) son funcionales exactos; un término cuadrático
positivo no fija el signo de `L`. El rayo de vértice no nulo no se
promueve a lower bound de región. Nada de eso se contradice.

El informe **no** asigna `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
No usa «puramente de red» ni «invisible a cualquier expansión en
`Lambda`» como claim. Eso está reservado por el charter al estado (4).

**Ataque 3: PASS.** La exclusión de (3) es correcta y no introduce
existencia.

## 5. Clasificación y techo de reclamo [M]

Único estado terminal: `OPEN_AFTER_SCALED_IR_ANALYSIS`. Coincide con la
regla explícita. Constantes de upper bound registradas: `C=36`, `q=4`,
`C_2=J=(1-√3/2)log 2`. No hay `C_1`, `c`, `p`, `N_*` de una lower bound
inexistente.

Techo, aceptado:

- sólo la clase congelada (familias internas no exhaustivas, geometría
  euclídea, `α=1/2`, `θ=π/2`, este walk);
- no reabre `3/128`, no-corner, ni el negativo narrow-band;
- `N\to\infty` no es `a,τ\to 0`; `DIMENSIONAL_MAP_CONDITIONAL` intacto;
- no hay predicción en eV, metros ni segundos;
- no se afirma violación de microcausalidad;
- no se abre `Delta T=2` ni un encoder nuevo.

La lectura autorizada es: **cualquier efecto de la clase está acotado por**
`O(N^4 e^{-JN})`. Eso ya es una predicción unilateral falsable del modelo
implementado. La magnitud real (incluido cero) sigue abierta.

## 6. Certificado software [X]

`python3 -B scripts/verify_scaled_ir_gate.py`: **53/53**, exit 0
(Python 3.12.3). El sha256 coincide con el declarado en el informe.

El recuento cubre identidades y límites marcados `[V]`: hash del charter,
margen `3>(17/10)^2`, bloques de vértice y recurrencia, `S=adj W`,
normalización radial, identidades de Pauli, límites puntuales del sanity,
identidades racionales **entre las expresiones** del lema de elipses,
`cosh(log 2)=5/4`, `125/64<17/8`, suma de normas `=4`, `3<4` para `J>0`,
y los dieciséis funcionales (F) **sin** afirmación de no nulidad.

**No cubre** (y el informe lo declara): Plancherel/Minkowski, (IR1) y
denominadores, el paso menores → contracción de elipses, el argumento de
contorno, Schur, `T_N`, (D1), ni las conclusiones asintóticas. Esos pasos
se rederivaron aquí para `J`, `36 N^4` y la clasificación. `53/53` no
sustituye esta revisión.

Helpers revisados: bytes intactos según el manifiesto del informe
(`git hash-object` no se repitió sobre cada uno; el working tree tracked
está limpio y esos archivos no aparecen en `git status`).

## 7. Aclaraciones recomendadas, no obligatorias

Ninguna cambia una cantidad ni el veredicto.

1. **Convención `D_B=\tfrac12\|ρ_1-ρ_0\|_1`.** Escribirla explícitamente en
   (D1). Está heredada del charter anterior y es la que hace `D_B\le\|X\|_1`
   con prefactor `36`.
2. **`(I-L^\top L)_{12}\ne 0`.** Una línea evita que un lector crea que la
   matriz es diagonal. El determinante ya cubre el criterio PSD.
3. **Justificación de (P):** `\mathrm{diag}` tiene norma de operador igual
   al máximo de `|λ_j|^N`.
4. **(DF)** es extra al sector de una partícula. No debe citarse como
   parte del claim congelado de los dieciséis pares.
5. El certificado podría, en un acto futuro separado, construir `L` en
   lugar de sólo relacionar expresiones. Eso cambiaría bytes y exigiría
   nueva revisión de ese archivo; **no** se hace aquí.

## 8. Qué esta revisión no cierra

- Lower bound, no cancelación, ni `δ>0` para ningún par.
- Nulidad exacta `D_B=0`.
- Tasa óptima `I(v)` fuera de esta geometría.
- Admisibilidad IR al mismo detalle que `J` (reconstruida, sin error
  bloqueante encontrado; no es el ataque pedido).
- Cota CAR (DF).
- Extensión a `M=aI+b·σ` general, a otros QCA, o al continuo físico.
- Novedad bibliográfica.
- Revisión humana externa ni replicación externa.

El cuello de botella científico siguiente, si se congela este resultado,
es específicamente la lower bound / no cancelación de los dieciséis pares.
No un encoder nuevo.

## 9. Veredicto

### `PASS`

Los tres puntos delicados sobreviven un ataque adversarial independiente:

| Punto | Resultado |
| --- | --- |
| Geometría regional → cota del kernel y `J>0` | **PASS** |
| Prefactor `36 N^4` uniforme en regiones y pares | **PASS** |
| Exclusión de `IR_RESOLVABLE_SIGNALING_POLYNOMIAL` sin existencia | **PASS** |

El estado terminal `OPEN_AFTER_SCALED_IR_ANALYSIS` es el único compatible
con lo demostrado. Congelar

`OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`

con la cota central de §0 está autorizado por esta revisión. No abre
ciencia nueva.
