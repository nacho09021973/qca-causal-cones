---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-24 19:21
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-09-24--two-channel-stability-review-request.md
rondas: 1
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - CLAUDE OPUS — Claude (Anthropic) — claude -p --model claude-opus-5 --effort high (sellado)
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Revisión independiente: estabilidad Schur y reconstrucción a Bob

## Decisión solicitada

Revisar únicamente la cadena matemática
\[
\text{cotas de bloques Schur}\Longrightarrow
\|t_N\|_{L^2}=O_W(1)\Longrightarrow
\|E^{1/2}\mathcal V_cPt_N\|,
\|E^{1/2}\mathcal V_cQt_N\|=O_W(N^{-1}),
\]
y las cotas de piezas que se deducen inmediatamente por Cauchy–Schwarz.
Atacar cuantificadores, constantes, normas y operadores. No revisar T1
completo ni T2/T3; no buscar cancelaciones, coeficientes, dominancia ni
H1c. No proponer Volterra nuevo.

## Enunciados que deben verificarse

1. En el soporte de Alice, `xi_*·(x-x_*) <= 0`; como
   `f=J(U_M-I)phi_N`, `||phi_N||=1` y `U_M` es unitario,
   `||s||=||F H_xi f||<=2`.
2. Para Bob, `R=N/4`, `y_*=Nu-R uhat`, `xi_*=lambda uhat` y
   `sqrt(h_N(y))=(1-|y-Nu|^2/R^2)_+`. Determinar si
   `||E^(1/2)V_c|| = sup_{y in B_N} sqrt(h_N(y)) exp[-xi_*·(y-y_*)]`
   y la cota `<= 8/(e lambda N)` son correctas, incluido el orden
   ajustado `Theta(N^-1)` sobre la red.
3. Con W fijo, verificar que `P,Q` tienen cotas operatoriales
   independientes de N y que se deduce
   `||E^(1/2)V_cP||, ||E^(1/2)V_cQ|| = O_W(N^-1)`.
4. Examinar si las estimaciones Schur (6), en sus normas diferentes
   P=`L2`, Q=`||·||_*`, bastan para que la recurrencia acoplada tenga
   norma de paso `<=1+C'/N` en `||x||_2+||y||_*`, con equivalencia
   uniforme en N, y por iteración `||t_N||_2<=C_W||s||_2`.
   Comprobar el retorno de la norma producto a la norma L2 de `t_N`.
5. Si esos pasos pasan, verificar el traslado al vector actual con el
   factor exacto `e^{-K_*N}` y las cotas superiores
   `|A_cP|,|A_cQ|<=C_W N^-1 e^{-K_*N}` y
   `0<=B_cPP,B_cQQ<=C_W N^-2 e^{-2K_*N}`,
   `|B_cPQ|<=C_W N^-2 e^{-2K_*N}`. Confirmar expresamente que sólo
   son cotas superiores y que las consecuencias de (4) heredan el
   nivel probatorio de Schur, rotulado PRELIMINARY / SIN REVISIÓN
   INDEPENDIENTE.

## Criterio de veredicto

Dar `PASS`, `REPAIR_REQUIRED` o `OPEN` para esta cadena, con la premisa
crítica, el primer paso que falla (si lo hay), la condición exacta que
desactivaría cada objeción y el alcance de cualquier pase. Separar la
cota operatorial geométrica (independiente de la estabilidad Schur) de
la cota sobre el vector `t_N`. No convertir un paso preliminar en un
resultado certificado. No inferir que los términos lineales dominan,
que las cotas son ajustadas, ni que exista término firmado líder.

## Contexto

### Contexto adjunto: reports/2026-09-24--h1c-return-kernel-schur-audit.md
```
# H1c: auditoría de la cota Schur y cierre del contrato operacional

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: el resolvente Volterra de
`reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md`.
`H1c_LOCALIZATION (L') = OPEN`.

**Cierre de sesión, 2026-09-24:** §§1–5 conservan el precheck analítico
previo, preliminar y sin revisión independiente. §6 congela por instrucción
expresa del usuario `TWO_DISTINGUISHABLE_CHANNELS`, con observable primario
`(L_+, L_-)`. H1c-0a está CLOSED; H1c-0b está
FIXED_BY_EXPLICIT_ASSUMPTION. La justificación física concreta sigue OPEN.
Volterra/localización asintótica: PAUSED; la prueba de H1c sigue abierta.
§7 fija el orden de la próxima sesión y no registra su ejecución.

## 1. La suma propuesta no implica la cota de susceptibilidad

Pongamos `R_{m,k}=B_mG_Q(m,k+1)C_k` para `m>k`. La memoria exacta es
\[
(\mathbb M_Nx)_n=
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\Phi_P(n,m+1)R_{m,k}x_k.
\tag{1}
\]
El kernel propuesto
`\widetilde R_{m,k}=\Phi_P(N,m+1)R_{m,k}\Phi_P(k,0)`
es la contribución de **una excursión** al elemento final cuando la
entrada sigue el transporte P libre. No es el kernel de `\mathbb M_N`
sobre secuencias arbitrarias `x_k`: (1) debe evaluarse también en
tiempos intermedios y con todas las posibles entradas `x_k`.

Contraejemplo algebraico: en espacios P y Q escalares, durante N pasos
tomar `A_j=D_j=1` y `B_j=C_j=1/N`, con pesos `w_j=1`. Entonces
`\Phi_P=1`, `G_Q=1`, y para `j>k`,
\[
R_{j,k}=\widetilde R_{j,k}=N^{-2},\qquad
\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|\le N^{-1}.
\tag{2}
\]
Sin embargo, para la secuencia `x_k=1`,
\[
(\mathbb M_Nx)_N
=N^{-2}\sum_{m=0}^{N-1}m
=\frac{N-1}{2N}\longrightarrow\frac12.
\tag{3}
\]
Así, la cota de (2) con `C/N` no implica
`\|\mathbb M_N\|=O(N^{-1})`. El ejemplo refuta sólo esa implicación;
no pretende representar el sector Q del walk inclinado.

Una condición suficiente que sí conserva el transporte temporal es
\[
\boxed{
\mathcal S_N(w):=
\sup_{0\le n\le N}\frac1{w_n}
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\|\Phi_P(n,m+1)R_{m,k}\|w_k
\le\frac{C}{N}.}
\tag{4}
\]
Por la desigualdad triangular, (4) implica
`\chi_N=\|\mathbb M_N\|_{w\to w}\le C/N`. También basta controlar
uniformemente el transporte P ponderado y exigir
`\sup_m w_{m+1}^{-1}\sum_{k<m}\|R_{m,k}\|w_k=O(N^{-2})`.
Con transporte P acotado y pesos unitarios, una suma por columnas
`\sup_k\sum_{m>k}\|R_{m,k}\|=O(N^{-2})` es otra condición suficiente.
El orden `N^{-2}` en estas sumas deja una suma adicional de `O(N)`
tiempos P en (1).
Como caso límite independiente, si `D_j=\rho` con `0<\rho<1`
fijo en el ejemplo escalar, entonces
`R_{j,k}=N^{-2}\rho^{j-k-1}`. La suma en duración es `O(N^{-2})`
por tiempo de origen y (1) es `O(N^{-1})`, como predice (4).

## 2. Cota completa en una norma auxiliar L2

Hay una forma de acotar el retorno **sandwichado** sin exigir una
estimación final para el Green Q desnudo. Se usa una partición
auxiliar que no afirma un Riesz splitting global. Sea W la unión de
vecindades fijas y disjuntas de los ocho saddles. En W, `P(p)` es el
proyector Riesz dominante de rango dos del símbolo libre inclinado;
fuera de W se define `P(p)=0` y `Q(p)=I`. Esta partición es medible y
acotada en `L^2(\mathbb T^3;\mathbb C^4)`; el salto en el borde de W
forma parte de los bloques de la moneda.

Normalicemos por el escalar global `\Lambda=e^{\Phi_*}>1`. El lema
espectral del TeX plano (`papers/ir-corona/ir-corona.tex`,
`lem:specrad` y `lem:symbol(d,e)`) da esa propiedad para S; para
`D=S\oplus S^{-1}` se sigue porque S es unimodular y ambos sumandos
tienen el mismo radio espectral. Por tanto
`\rho(D_\xi(p)/\Lambda)\le1`, con igualdad sólo en los ocho saddles.
En W, el bloque libre Q tiene autovalor
`\lambda(p)^{-1}/\Lambda`, uniformemente dentro del disco unidad.
Fuera de W, `Q=I` y el radio espectral libre es estrictamente menor
que uno por compacidad. En consecuencia existe `\rho_0<1` que
acota el radio espectral de todo el bloque libre Q, aun donde la
matriz exterior sea no normal.

En dimensión finita por fibra, el resolvente de la familia libre en
una circunferencia `\rho_0<\rho_1<1` es uniformemente acotado en
cada uno de los dos compactos (cierres de W y de su exterior).
Por la fórmula de Cauchy,
\[
\|(D_Q^{(0)})^h\|_{L^2\to L^2}
\le C_0\rho_1^h,
\qquad D_Q^{(0)}=Q(D_\xi/\Lambda)Q.
\tag{5}
\]
La norma equivalente
`\|y\|_*:=\sup_{h\ge0}\rho_1^{-h}\|(D_Q^{(0)})^hy\|_2`
satisface `\|D_Q^{(0)}y\|_*\le\rho_1\|y\|_*`.

En la representación de momento, la moneda espacial es convolución,
pero su norma `L^2\to L^2` es la norma del multiplicador en posición:
`\|C_N-I\|\le C/N` para `\vartheta` acotada. Las proyecciones
auxiliares son multiplicadores acotados en momento. Por ello, en
las normas P=`L^2`, Q=`\|\cdot\|_*`, los bloques exactos satisfacen
\[
\|B_j\|,\|C_j\|\le C/N,\quad
\|D_j\|_*\le\rho_1+C/N<\rho_2<1,
\quad\|A_j\|_2\le1+C/N.
\tag{6}
\]
La última desigualdad usa `|\lambda(p)|/\Lambda\le1` en W.
Permite variación uniforme de la moneda entre pasos; no presume
conservación del momento.

De (6) se obtiene directamente para el **retorno completo**
\[
\|R_{m,k}\|_{P\to P}
\le\frac{C}{N^2}\rho_2^{m-k-1},\qquad
\|\Phi_P(n,m+1)\|\le e^C.
\tag{7}
\]
La suma de (4) con `w=1` da
\[
\boxed{\|\mathbb M_N\|_{\ell^\infty_t L^2_p\to
\ell^\infty_t L^2_p}=O(N^{-1}).}
\tag{8}
\]
Esta es una cota preliminar en un espacio auxiliar para el producto
normalizado; la no normalidad exterior queda absorbida en la norma
equivalente de (5). No demuestra la cota física ponderada de `L'`.

## 3. Techo físico de la cota auxiliar

La cota (8) no recupera por sí sola el factor gaussiano tangencial
de los elementos Alice/Bob. `state/CURRENT_STATE.md`, §9.2, sólo
certifica masas absolutas inclinadas `O(N^{-5/2})` para cada extremo.
Usándolas sin información adicional, (8) produciría para la
corrección interna una cota `O(N^{-6})`. La escala líder que se intenta
conservar es `N^{-13/2}`: esa cota gruesa pierde `N^{1/2}` y no prueba
dominancia relativa. Una norma física con envolventes de momento,
fases y endpoints podría recuperar la potencia, pero aún no se ha
fijado ni estimado.

Además, definir `P=0` fuera de W asigna todas las trayectorias
exteriores a Q. Sus entradas/salidas y los saltos entre W y su
exterior siguen presentes en `B,C,D`; (8) no demuestra que la
contribución Q inicial/final al elemento físico sea pequeña.

## 4. Resultado del subgate

- **REFUTADO:** la condición
  `\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|_w\le C/N`
  implica por sí sola `\chi_N=O(N^{-1})`.
- **PRELIMINARY:** la condición correcta es una suma Volterra doble
  como (4), o una suma de retornos `O(N^{-2})` por tiempo bajo
  transporte P controlado.
- **PRELIMINARY:** en `\ell^\infty_t L^2_p`, el splitting auxiliar
  local-en-W / exterior-en-Q y el lema espectral plano dan (8).
- **OPEN:** trasladar (8) a una envolvente física que preserve el
  factor de saddle, y controlar los términos Q de los extremos
  reales de `L'`.

En el precheck de §§1–4 no se ejecutó código numérico ni se modificaron
C2c, el manuscrito o `state/CURRENT_STATE.md`. El cierre documental de §6
sí se resume ahora en el estado canónico, por instrucción del usuario.

## 5. Cortafuegos del elemento físico

Antes del cierre de §6, la prueba propuesta era comparar directamente la primera
corrección `\ell_P(\mathbb M_Nx^{(0)})_N` y los términos con entrada o
salida Q de (8) en el precheck Volterra con el líder `L'_{N,P}`.
La búsqueda en `state/CURRENT_STATE.md`, §9,
`reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md`,
§§8–9, y `reports/2026-09-20--h1-chat-research-log.md`, §§12–13,
no proporciona los extremos físicos de cuatro componentes, el
funcional firmado final ni una cota inferior uniforme para
`|L'_{N,P}|`. El TeX plano, §7.3, fija un elemento de dos componentes;
su embedding en cuatro componentes es un test auxiliar, no una
definición del observable inhomogéneo.

Por ello los cocientes físicos
`\ell_P(\mathbb M_Nx^{(0)})_N/L'_{N,P}` y
`L'_{\mathrm{boundary}-Q}/L'_{N,P}` son **NO EVALUABLES CON EL
CONTRATO ACTUAL**. La cota (8) no se convierte en un PASS de H1c.
Según el cortafuegos de esta línea, se detiene aquí la vía Volterra:
no se introducen nuevas normas, proyectores o resolventes para
suplantar esos datos físicos. Ese diagnóstico describe el contrato anterior.
§6 fija ahora el protocolo por hipótesis explícita; su traducción exacta a
P/Q sigue pendiente y no se obtiene automáticamente de (1)–(8).

## 6. Cierre H1c-0 / decisión explícita de modelo — 2026-09-24

### 6.1 Procedencia y alcance del cierre

La búsqueda local previa al cierre no encontró las etiquetas
`H1C0_UNDERSPECIFIED`, `CONTRACT_VALID`, `PHYSICAL_INTERPRETATION_OPEN`
o `MODEL_CHOICE_REQUIRED` en archivos del repositorio. Se registran aquí
como etapas de la auditoría y decisión de esta sesión, sin atribuirlas
retroactivamente a un commit anterior:

1. `H1C0_UNDERSPECIFIED`: el contrato H1 fijaba propagación y beta,
   pero no el lift operacional del protocolo plano.
2. `CONTRACT_VALID / PHYSICAL_INTERPRETATION_OPEN`: el candidato con
   preparación en el primer bloque y POVM refinado supera las identidades
   de normalización, positividad y recuperación plana, en auditoría interna.
3. `MODEL_CHOICE_REQUIRED`: el repositorio anterior no seleccionaba qué
   significado operacional dar a los bloques.
4. Decisión aceptada y congelada por el usuario:
   **`TWO_DISTINGUISHABLE_CHANNELS`**, como nueva hipótesis de modelo.

El contrato algebraico figura en la
[reconstrucción H1, §1](2026-09-20--h1-inhomogeneous-localization-reconstruction.md),
introducida en `bbc898be6c68cd8594449a7a52988c95b655dff4`. La
[bitácora H1, §§1–2](2026-09-20--h1-chat-research-log.md),
archivada en `3f8ae75f327aa06d23a2e5ee726a81866bcdfe33`, se identifica
como reconstrucción de chat y no certifica la convención gamma original.
Esos textos documentan las identidades del doblado; no derivan la
accesibilidad física de sus dos bloques. La falta de ese diccionario
tampoco demuestra que el doblado se introdujera exclusivamente como
dispositivo auxiliar.

El cierre H1c-0a se limita a la consistencia y definición del contrato
matemático siguiente. No certifica los prechecks de §§1–5, no constituye
revisión independiente y no cierra la localización H1c ni H1.

### 6.2 Espacio, propagación, preparación y encoder

El Hilbert operacional completo de una partícula es
\[
\mathcal H=
\ell^2(\mathbb Z^3)\otimes
\mathbb C^2_{\rm canal}\otimes\mathbb C^2_{\rm espín}.
\]
Para esta extensión candidata, los bloques de
\[
D=S\oplus S^{-1},\qquad
\beta=\sigma_x^{\rm canal}\otimes I_{\rm espín},\qquad
U_N=C_N(x)D,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N}
\]
se interpretan como canales internos distinguibles `+` y `-`. Se conserva
el perfil real y las hipótesis de regularidad del contrato H1 existente.
Beta intercambia los canales y la moneda los mezcla coherentemente.
La interpretación y la capacidad de Bob para resolver el canal son
**supuestos nuevos**, no consecuencias de esas identidades algebraicas.

Se heredan sin cambio el recurso, las regiones, los perfiles y las familias
de encoder/detector de [ir-corona.tex, §3](../papers/ir-corona/ir-corona.tex):
\[
\widehat\phi_N(p)=Z_N^{-1/2}g(Np)|\downarrow\rangle,
\quad \|\phi_N\|=1,\qquad
U_M=e^{i\pi F_N M/2},\qquad E=h_N\otimes M_B,
\quad 0\le E\le I.
\]
Aquí `M` recorre `I, sigma_1, sigma_2, sigma_3` y `M_B` recorre
`I, (I+sigma_j)/2`, como en el protocolo plano.
Con `Jx=(x,0)`, la preparación fijada es
\[
\Phi_N=J\phi_N=\binom{\phi_N}{0}.
\]
El bit `b=0` aplica la identidad; para `b=1` se usa un representante
\[
\mathcal U_M^{(1)}=U_M\oplus U_M,\qquad
\mathcal U_M^{(0)}=I_{\mathcal H}.
\]
La identidad
\[
(U_M\oplus U_M)J=(U_M\oplus I)J=JU_M
\]
registra equivalencia operacional en el instante del encoding bajo esta
preparación. No afirma identidad física de ambos encoders sobre otros
estados o protocolos. Ambos son unitarios y actúan como identidad fuera
de Alice. Para el mismo perfil real, `U_N` es unitario en el Hilbert físico.

Tras encoding y `N` pasos,
\[
\Psi_b=U_N^N\mathcal U_M^{(b)}\Phi_N
=\binom{\psi_b^+}{\psi_b^-},\qquad \|\Psi_b\|=1.
\]
La referencia no codificada de Bob procede de
`Psi_0=U_N^N Phi_N`; depende del walk doblado. No se reemplaza por la
referencia plana al activar la moneda.

### 6.3 POVM y respuesta física primaria

Bob resuelve la etiqueta de canal, por hipótesis de modelo. Su POVM es
\[
F_+=E\oplus0,\qquad F_-=0\oplus E,\qquad
F_\varnothing=I_4-(E\oplus E).
\]
En esta fórmula `I_4` abrevia la identidad completa
`I_{ell^2(Z^3)} tensor I_4`; no se restringe el espacio a la región Bob.
Como `0<=E<=I`, los tres efectos son positivos y suman
`I_{mathcal H}`. El resultado vacío incluye toda ausencia de detección.

Con la dependencia en `N,M,M_B` implícita, se fija como respuesta primaria
\[
\boxed{(L_+,L_-)},\qquad
L_\pm=
\langle\psi_1^\pm,E\psi_1^\pm\rangle
-\langle\psi_0^\pm,E\psi_0^\pm\rangle.
\]
Por normalización de las dos distribuciones de resultados,
\[
L_\varnothing=-L_+-L_-.
\]
Las dos lecturas binarias posibles son coarse-grainings explícitos:
\[
L_{\rm block}=L_+,\qquad L_{\rm incl}=L_++L_-.
\]
La primera cuenta `+` frente a `-` o ausencia de detección; la segunda
cuenta cualquiera de los dos canales frente a ausencia de detección.
Ninguna es el observable primario del contrato. Las respuestas se suman
con signo antes de tomar cualquier valor absoluto. No se seleccionará
posteriormente una lectura porque proporcione mejores potencias.

Los canales pueden mantener coherencia cuántica. Este POVM conserva la
información de sus tres resultados; no reconstruye todas las coherencias
del estado. Tampoco identifica los canales físicos `+/-` con los sectores
espectrales auxiliares `P/Q` de los prechecks.

### 6.4 Control plano exacto y límites

Para `vartheta=0`,
\[
C_N=I,\qquad U_N=D=S\oplus S^{-1},\qquad
U_N^N\binom{x}{0}=\binom{S^Nx}{0}.
\]
Por tanto para ambos bits y todos los pares heredados,
\[
\Psi_b=\binom{S^NU_M^{(b)}\phi_N}{0},\qquad
L_+=L_{\rm plano},\quad L_-=0,\quad
L_{\rm incl}=L_{\rm plano}.
\]
Esta recuperación exacta justifica inicialmente la extensión propuesta.
No se usa comportamiento asintótico favorable para elegirla.

Sigue **OPEN** la justificación de este doubled walk como representación
de un sistema físico concreto. Ningún resultado futuro de esta extensión
se presentará como universal para el protocolo plano original: quedará
condicionado a la hipótesis de dos canales distinguibles accesibles a Bob.

Estado conceptual congelado por instrucción del usuario:

```text
model choice: TWO_DISTINGUISHABLE_CHANNELS
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

H1c y H1 permanecen matemáticamente abiertos. El cierre de contrato no
promueve ninguna cota preliminar. En particular, el `O(N^-6)` de §3
procede de multiplicar cotas absolutas auxiliares; no se ha aislado un
coeficiente `E_6`, ni se ha trasladado esa cota a cada respuesta firmada
del protocolo recién fijado.

## 7. Next session / 2026-09-25

Plan registrado; T1–T3 no se ejecutan en este cierre documental.

### T1 — Lift exacto del observable a P/Q

Partir del POVM de §6 y derivar, sin estimaciones de norma, las expresiones
exactas firmadas de `L_+` y `L_-` dentro de la descomposición P/Q existente.
Determinar si tiene sentido escribir
`L_± = L_{±,P} + L_{±,Q}`. No asumir esa aditividad: si el observable
cuadrático genera términos cruzados, escribir la expansión exacta completa,
incluyendo la referencia de Bob y ambos bits. No confundir canal físico con
proyector de Riesz ni cambiar la partición para obtener el resultado.

### T2 — Identificar qué significa realmente el actual O(N^-6)

Sólo tras cerrar T1, trazar la cota auxiliar
`||mathbb M_N||=O(N^-1)` de (8) y las cotas de extremo hasta cada
contribución firmada de `L_+` y `L_-`. Distinguir cota de norma, término
asintótico real, términos cruzados y posible cancelación firmada.
Comprobar el alcance de las cotas heredadas para la nueva referencia de Bob.
No llamar `E_6` a nada salvo que exista un coeficiente realmente aislado.

### T3 — Test de proyección

Sólo cuando T1 y T2 estén cerrados, comprobar separadamente qué contenido
del techo `O(N^-6)` sobrevive en `L_+`, en `L_-`, se cancela en alguno,
o se cancela únicamente en `L_++L_-`. Toda afirmación de cancelación
requiere contribuciones firmadas identificadas; una cota sola no basta.
Una cancelación en `L_incl` no permite cambiar el observable primario.

### STOP GATE

- Si T1 no produce un observable firmado exacto compatible con la
  descomposición existente, parar.
- Si T2 muestra que `N^-6` sólo es una cota gruesa sin coeficiente
  identificable, no buscar simetrías de un término inexistente.
- No introducir otra técnica analítica hasta cerrar T1–T3. La vía Volterra
  y la localización asintótica permanecen PAUSED durante este cierre.

## 8. Cadena documental archivada

Los siete informes de hoy pertenecen a esta cadena. Se conservan sus
argumentos previos con su alcance y falta de revisión independiente:

- [Conteo de parejas Dyson](2026-09-24--h1c-dyson-pair-audit.md).
- [Cota por inserción Dyson](2026-09-24--h1c-dyson-target-check.md).
- [Descomposición Dyson exacta](2026-09-24--h1c-exact-dyson-decomposition.md).
- [Masa de excursiones: kill-tests](2026-09-24--h1c-excursion-mass-kill-tests.md).
- [Resolvente de excursiones](2026-09-24--h1c-kernel-excursion-resolvent-audit.md).
- [Núcleo de memoria Volterra](2026-09-24--h1c-volterra-memory-kernel-precheck.md).
- Este informe de Schur y cierre operacional.

El cierre añade documentación y el resumen de `state/CURRENT_STATE.md`.
No ejecuta Volterra, nuevos fits, cálculos asintóticos, scripts científicos
ni el plan de mañana. El manuscrito plano y el código no se modifican.
```

### Contexto adjunto: reports/2026-09-24--two-channel-reconstruction-operator-norms.md
```
# Norma de la reconstrucción física P/Q sobre la salida normalizada

Fecha: 2026-09-24. Estado: `BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM`
al nivel **PRELIMINARY**, condicionado al lema de bloques Schur §2.
Alcance: sólo las cuatro normas
`||E^{1/2} V_c P t_N||`, `||E^{1/2} V_c Q t_N||`, `c=+,-`, y su uso
inmediato para acotar las diez piezas por Cauchy–Schwarz. No se cambia
Volterra, no se buscan cancelaciones y no se identifican términos líderes.

Este informe actualiza el resultado de la primera auditoría
`reports/2026-09-24--two-channel-physical-bound-transfer-audit.md`:
el STOP inicial localizó correctamente las normas que faltaban; la
presente estimación, usando la geometría explícita del efecto de Bob y
las cotas de bloques ya escritas, cierra ese hueco como cota superior.

## 1. Norma exacta del operador de reconstrucción

Del contrato en T1, §§2 y (6)–(8),
\[
(\mathcal V_c z)(y)=\mathbf1_{\mathcal B_N}(y)
e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}\pi_c z)(y),
\quad
d_{c,P/Q}=e^{-K_*N}\mathcal V_c(P/Q)t_N.
\]
El efecto del TeX plano, §3 y la definición del perfil Bob, es
\[
E=h_N\otimes M_B,\quad \|M_B\|=1,\quad
h_N(y)=\left(1-\frac{|y-Nu|^2}{R^2}\right)_+^2,
\quad R=N/4,\quad u=(1,1,1).
\]
Además, su representación inclinada fija
\(y_*=Nu-R\widehat u\), \(\widehat u=u/\sqrt3\), y
\(\xi_*=t_*u=\lambda\widehat u\), \(\lambda=\sqrt3t_*>0\).
Estas posiciones están en `papers/ir-corona/ir-corona.tex`, §§3,
exact tilted representation, y en T1 (6)–(8).

Como Fourier y la extracción de un canal tienen norma uno,
\[
\|E^{1/2}\mathcal V_c\|
=m_N:=\sup_{y\in\mathbb Z^3}
\sqrt{h_N(y)}e^{-\xi_*\cdot(y-y_*)}.
\]
Esta igualdad usa que \(M_B\) tiene autovalor máximo uno y que el
dominio permite cualquier función de Fourier L² en el canal elegido.
Para un y dentro de Bob, ponga
\(s=\widehat u\cdot(y-y_*)\) y descomponga
\(y-Nu=(s-R)\widehat u+q\), con \(q\perp\widehat u\). La condición
\(|y-Nu|\le R\) da \(0\le s\le2R\), y
\[
\sqrt{h_N(y)}
=\left(1-\frac{(s-R)^2+|q|^2}{R^2}\right)_+
\le \frac{2s}{R}-\frac{s^2}{R^2}
\le \frac{2s}{R}.
\]
Por ello
\[
0\le m_N\le\sup_{s\ge0}\frac{2s}{R}e^{-\lambda s}
=\frac{2}{e\lambda R}=\frac{8}{e\sqrt3t_*}\,N^{-1}.
\tag{1}
\]
El orden \(N^{-1}\) es ajustado para el operador sin P/Q: elija puntos
de red sobre la diagonal \(y=(m,m,m)\) con
\(s=\sqrt3(m-(y_*)_1)\) en un intervalo fijo positivo, por ejemplo
\([\sqrt3,2\sqrt3]\). Para N grande están dentro de Bob, con \(q=0\),
\(\sqrt{h_N}\ge c/N\), y el factor exponencial es uniformemente
positivo. Así \(m_N=\Theta(N^{-1})\). El factor exponencial de
desinclinación no hace crecer la norma: en la cara enfrentada donde
el peso sería máximo, \(h_N\) se anula; dentro, el peso decae.

Para W admisible y fijo, T1 §2 da
\(C_P(W)=\|P\|_{L^2\to L^2}<\infty\) y
\(C_Q(W)=\|Q\|_{L^2\to L^2}<\infty\), independientes de N. Por (1),
\[
\boxed{\|E^{1/2}\mathcal V_cP\|\le C_P(W)m_N=O_W(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQ\|\le C_Q(W)m_N=O_W(N^{-1}).}
\tag{2}
\]
Vale para ambos canales. No se afirma una cota inferior para ninguna
composición con P o Q.

## 2. Norma del vector normalizado actual

La fuente exacta T1 §1 es
\(s=\mathcal F H_\xi f\), con
\(f=J(U_M-I)\phi_N\), \(\|f\|\le2\), soportada en Alice.
Alice es la bola de radio R centrada en el origen y
\(x_*=R\widehat u\). Para todo x de Alice,
\(\xi_*\cdot(x-x_*)\le0\); luego el multiplicador \(H_\xi\) tiene
norma a lo sumo uno sobre el soporte de f y
\[
\|s\|_2=\|H_\xi f\|_2\le2.
\tag{3}
\]

No hace falta estimar Volterra. Se usan directamente las cotas de
bloques ya establecidas en la auditoría Schur, §2, ecuación (6): en
las normas P=L² y Q=\(\|\cdot\|_*\), uniformemente para N grande,
\[
\|A_j\|\le1+C/N,\quad \|B_j\|,\|C_j\|\le C/N,
\quad \|D_j\|_*\le\rho_2<1.
\]
En la norma producto \(\|x\|_2+\|y\|_*\), la recurrencia T1 (13)
queda acotada por \(1+C'/N\) paso a paso (absorbiendo la contracción
\(\rho_2\) y los dos bloques cruzados \(O(N^{-1})\)). Iterar N pasos
da una constante independiente de N. El dato inicial satisface
\(\|Ps\|+\|Qs\|\le(C_P(W)+C_Q(W))\|s\|\). Por tanto
\[
\boxed{\|t_N\|_2\le C_{\rm stab}(W,\vartheta)\|s\|_2
=O_W(1).}
\tag{4}
\]
Ésta es sólo estabilidad L² del producto ya normalizado, que sale de
las cotas de bloques Schur; no es una nueva cota de memoria ni una
afirmación sobre historias individuales. El informe Schur está rotulado
`PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`, por lo que (4), (5), (6) y
las cotas por pieza que usan t_N heredan ese nivel de evidencia. En
cambio (1) y (2) son cotas operatoriales directas de la definición
geométrica, condicionadas sólo a W fijo y a la acotación P/Q de T1.

De (2) y (4), para c=+ y c=-,
\[
\boxed{\|E^{1/2}\mathcal V_cPt_N\|=O_W(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQt_N\|=O_W(N^{-1}).}
\tag{5}
\]
Al volver a las amplitudes físicas,
\[
\boxed{\|E^{1/2}d_{c,P}\|,
\|E^{1/2}d_{c,Q}\|=O_W(N^{-1}e^{-K_*N}).}
\tag{6}
\]
La fuente de la potencia \(N^{-1}\) es la norma del multiplicador
Bob ponderado en (1), no el antiguo retorno \(\mathbb M_N\) ni una
proyección de saddle. La cota es superior; no hay lower bound ni
asintótica equivalente para los vectores concretos \(t_N\).

## 3. Transferencia inmediata a las diez piezas

La unitariedad física y \(0\le E\le I\) dan
\(\|E^{1/2}r_c\|\le1\). Aplicando Cauchy–Schwarz a las identidades
exactas T1 (10a), sin cambiar los signos de las definiciones:
\[
|A_{cP}|,|A_{cQ}|=O_W(N^{-1}e^{-K_*N}),
\]
\[
0\le B_{cPP},B_{cQQ}=O_W(N^{-2}e^{-2K_*N}),\qquad
|B_{cPQ}|=O_W(N^{-2}e^{-2K_*N}),
\quad c=+,-.
\]
Estas son cotas superiores uniformes en N para W fijo, **condicionales
al lema de estabilidad preliminar Schur §2**; no se promueven a
`ESTABLISHED`. No son \(\sim\), no contienen lower bounds y no
identifican `LEADING_ASYMPTOTIC_TERM`. En particular, el operador bound no atribuye al observable el antiguo
\(O(N^{-6})\), que dependía de otros extremos y otro sandwich.

| TERM | BOUND | SOURCE | ASSUMPTIONS | EXPONENTIAL_SCALE | POWER_OF_N | SIGNED_INFORMATION_RETAINED | LOST_BY_ABSOLUTE_VALUE | STATUS |
|---|---|---|---|---|---|---|---|---|
| `A_{+P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{+Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |

Memoria Q: ambas salidas P contienen entradas/retornos desde Q; la salida
Q contiene Q inicial y las salidas desde P, con historia de retornos en
los \(x_k\) (T1 (14)). La tabla no separa una contribución de
“permanencia P” ni atribuye historias. El mismo bound operatorial cubre
ambos canales porque extracción de canal tiene norma uno; no suma ni
cancela \(L_+\) y \(L_-\).

## 4. Límite de la conclusión

Los términos lineales tienen una envolvente exponencial menos pequeña
que la de los cuadráticos. Eso los hace candidatos naturales si una
lower bound posterior los mantiene en esa escala; la auditoría no prueba
dominancia, porque todos los resultados aquí son cotas superiores y
pueden ser estrictamente no ajustados. No se abre esa pregunta ahora.

```text
PRELIMINARY: BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM
```

No se ejecutaron scripts ni barridos. No se modificó el manuscrito.
No se hizo commit ni push.
```

### Contexto adjunto: reports/2026-09-24--two-channel-t1-exact-signed-pq.md
```
# T1: lift exacto firmado de los dos canales al P/Q inclinado

Fecha: 2026-09-24. Base inspeccionada: `d8ca7b285129b8b29a304e232195e29f20095526`.
Estado: `T1: PASS`.
Review status: `INDEPENDENT_ADVERSARIAL_REVIEW_PASS`.
La revisión reparada de Claude Opus y DeepSeek V4-Pro acepta T1 en el
contrato y el W fijado aquí. El expediente y sus límites están en
`debates/2026-09-24--two-channel-t1-rereview.md`. El primer intento quedó
degradado porque Gemini falló por falta de crédito; no se cuenta como
consenso ni como evidencia a favor o en contra.
El snapshot matemático adjunto a la re-revisión tiene SHA256
`dc076059935d9b814c17f69390f202187768f75dfad30c9d912033c4c6d487ee`.
Después del dictamen se incorporó a este informe la relación local
\(\beta P=Q\beta\), recomendada y derivada en los turnos de revisión.

Los revisores comprobaron de forma separada el signo \(p-i\xi_*\), el
factor exacto \(e^{-K_*N}\), la fórmula de cinco piezas, los adjuntos,
la recurrencia Volterra y el control acoplado. No encontraron error en
las identidades de T1. Opus retiró sus reparaciones obligatorias iniciales
tras verificar la versión reparada; DeepSeek discrepó de su objeción
residual sobre una supuesta independencia necesaria de las etiquetas.
El acuerdo es `T1_PASS` dentro del contrato explícito y para cada W
admisible fijo de §2. El pase no evalúa escalas, uniformidad en W ni
las afirmaciones analíticas preliminares. Los controles (17)–(18) sólo
verifican las identidades de bloques en una fibra; no controlan
\(P(p')Q(p)\) a momentos distintos ni las interfaces con \(W^c\).
Ambos revisores recomiendan dejar ese límite registrado para T2.

La re-revisión fue un sanedrín deliberativo de una ronda, Claude Opus
(Anthropic) y DeepSeek V4-Pro (DeepSeek); el segundo tuvo acceso al turno
de Opus. Es revisión independiente del autor por dos familias, no dos
juicios ciegos ni revisión humana. Commit de la herramienta sanedrín:
`8162508e3bd0e3d05770b4dd544fe7c962d0272c`.
Alcance: T1 de `state/CURRENT_STATE.md`, §9.6, por instrucción del usuario.
No se ejecutan T2 ni T3. No se modifica el estado canónico.

## 1. Definiciones y procedencia

Se usan como definiciones del problema el contrato de dos canales de
`reports/2026-09-24--h1c-return-kernel-schur-audit.md`, §6, y la partición
auxiliar de su §2. Las identidades siguientes se derivan aquí; no se toman
las conclusiones analíticas de los prechecks como premisas probadas.
El índice `biblioteca/INDICE.md` fue inspeccionado; no se utiliza ningún
resultado bibliográfico para esta expansión algebraica.

Sean
\[
Jv=(v,0),\qquad D=S\oplus S^{-1},\qquad
U_N=C_ND,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N},
\quad \beta=\sigma_x\otimes I_2.
\]
Los perfiles, la preparación y los efectos son los de
`papers/ir-corona/ir-corona.tex`, §3. Se fija cualquier entero \(N\ge2\),
cualquiera de los cuatro encoders \(M\) y cualquiera de los cuatro
detectores \(M_B\) del contrato. El perfil real \(\vartheta\) conserva
las hipótesis del contrato H1. El producto interno es antilineal en el
primer argumento. Para \(c\in\{+,-\}\), \(\pi_c\) extrae el canal y
\[
F_c=\pi_c^*E\pi_c,\qquad E=h_N\otimes M_B.
\]
Definimos la referencia física y la perturbación de Alice **completas**:
\[
r=U_N^NJ\phi_N=\Psi_0,\qquad
f=J(U_M-I)\phi_N,\qquad d=U_N^Nf.
\tag{1}
\]
Así \(\Psi_b=r+b d\) para ambos bits \(b=0,1\). No se sustituye
\(r\) por la referencia plana. En particular,
\[
f=J\bigl(c_N\phi_N+i s_N M\phi_N\bigr),\quad
c_N=\cos(\pi F_N/2)-1,\quad s_N=\sin(\pi F_N/2).
\]
No se descarta la parte \(c_N\), ni ninguna contribución cuadrática.
Como \(U_M-I\) está soportado en Alice, \(f\) tiene soporte finito.

La expansión directa del POVM da, sin aproximaciones,
\[
\boxed{L_c=2\operatorname{Re}\langle r,F_cd\rangle
                 +\langle d,F_cd\rangle.}
\tag{2}
\]
Esto ya incluye la sustracción exacta de la probabilidad del bit cero.

## 2. La partición existente y el lift bien definido

Se mantiene la construcción de ventanas del precheck de Schur,
explicitando su cuantificador. Sean \(O_\alpha\) vecindades espectrales
de los ocho saddles \(\alpha\in\Sigma=\{0,\pi\}^3\), en el toro,
en las que existe una rama continua dominante \(\lambda_\alpha\),
con \(|\lambda_\alpha|>1\). Se fija, una vez para T1–T3, una familia
de vecindades abiertas \(W_\alpha\ni\alpha\) con cierres disjuntos
y \(\overline{W_\alpha}\subset O_\alpha\). Se define
\(W=\bigcup_\alpha W_\alpha\), independiente de N, del encoder,
del detector y del perfil de moneda.

Estas vecindades existen directamente para el símbolo explícito del
TeX: en cada saddle \(\tfrac12\operatorname{tr}S\) es
\(\pm\prod_j\cosh(\xi_{*,j})\), de módulo mayor que uno, mientras
\(\det S=1\). Las dos raíces del polinomio característico son
distintas y una tiene módulo mayor que uno. Por continuidad, la
separación persiste en vecindades pequeñas con cierres en ese dominio.
Ésta es la condición de admisibilidad de W usada aquí.

Para cada W así fijado, las identidades siguientes son exactas. Las
piezas se entienden como \(A_{cP}^{(W)},\ldots,B_{cPQ}^{(W)}\), aunque
se suprima el superíndice. No se fija un radio numérico ni se afirma
independencia de las piezas respecto de W: es una descomposición relativa
a un parámetro auxiliar fijo. Toda cota posterior deberá retener esa
dependencia, salvo prueba separada de uniformidad. No se permite elegir
\(W=W_N\) ni reajustarlo para mejorar una pieza.

Si \(p_S(p)\) es el Riesz idempotente de \(S(p-i\xi_*)\)
para la raíz dominante \(\lambda(p)\) en una ventana, entonces
\[
P(p)=
\begin{cases}
\operatorname{diag}(p_S(p),I_2-p_S(p)),&p\in W,\\
0,&p\notin W,
\end{cases}
\qquad Q=I-P.
\tag{3}
\]
En efecto, \(S^{-1}\) tiene autovalor \(\lambda\) en el subespacio
de \(S\) con autovalor \(\lambda^{-1}\). Se entiende (3) como
multiplicadores acotados en \(\mathscr H=L^2(\mathbb T^3;\mathbb C^4)\).
Sólo se usa \(P^2=P\), \(Q^2=Q\), \(P+Q=I\) y \(PQ=QP=0\).
No se presupone \(P^*=P\).

La acotación no requiere un radio efectivo. En cada cierre de ventana,
\[
p_S(p)=\frac{S(p-i\xi_*)-\lambda_\alpha(p)^{-1}I_2}
                    {\lambda_\alpha(p)-\lambda_\alpha(p)^{-1}}.
\tag{3a}
\]
El numerador es continuo y el denominador está separado de cero en
ese compacto. Hay sólo ocho ventanas; fuera de ellas P=0. Por tanto
\(\operatorname*{ess\,sup}_p\|P(p)\|\le C_P(W)<\infty\), y lo
mismo vale para Q=I-P. Los saltos en la frontera no afectan a esta
acotación de multiplicadores L2, y siguen presentes en los bloques.

Estos P/Q son los del símbolo **inclinado**. No son los canales
\(+/-\), ni el corte IR \(\Pi'\) del frente C2/C3. Ambos canales
tienen componentes en P y en Q dentro de las ventanas. El exterior
permanece en Q, con todas sus transiciones.

Hay, sin embargo, una relación entre las transiciones locales y los
canales que conviene dejar a la vista. En W, usando la convención del
contrato \(\beta=\sigma_x\otimes I_2\),
\[
\beta P(p)=Q(p)\beta,\qquad P(p)\beta=\beta Q(p),
\qquad p\in W.
\tag{3b}
\]
Se comprueba por bloques a partir de (3); requiere que W use la misma
ventana para los dos bloques recíprocos, como se ha fijado aquí.
Así, para moneda constante y una fibra individual, una transición
P\(\leftrightarrow\)Q mediante \(\beta\) conmuta los canales
\(+\leftrightarrow-\) a la vez. Fuera de W esta identidad no se afirma:
P=0 y Q=I allí. La identidad de cinco piezas no requiere que esos
mecanismos sean independientes; el control (18) comprueba la recurrencia
con acoplamiento en una fibra, pero no prueba el efecto de \(P(p')Q(p)\)
para \(p'\ne p\) ni los cruces con el exterior de W. Esas cantidades
quedan para el trazado de T2, no se estiman aquí.

Para justificar el lift sin inclinar la preparación de cola espacial
infinita, basta inclinar \(f\). Con la convención de Fourier del TeX,
\[
(\mathcal Fv)(p)=\sum_xe^{ip\cdot x}v(x),\qquad
(\mathcal F^{-1}z)(y)=\int e^{-ip\cdot y}z(p)\,d\mu(p),
\]
sean
\[
(H_\xi v)(x)=e^{\xi_*\cdot(x-x_*)}v(x),\quad
s=\mathcal F H_\xi f,\quad \Lambda=e^{\Phi_*},\quad
T=\Lambda^{-1}\mathcal F H_\xi U_NH_\xi^{-1}\mathcal F^{-1}.
\tag{4}
\]
La conjugación se define primero en vectores de soporte finito.
Como \(U_N\) tiene alcance finito y moneda local acotada, el operador
inclinado así obtenido tiene una extensión acotada en \(\mathscr H\).
La moneda conmuta con \(H_\xi\); el bloque libre es
\(D_\xi(p)=D(p-i\xi_*)\). Por tanto T es precisamente el paso
normalizado del precheck, con sus saltos de momento, no otro propagador.

Para cada \(0\le j\le N\),
\[
t_j=T^js=\Lambda^{-j}\mathcal F H_\xi U_N^jf.
\tag{5}
\]
Esta identidad se comprueba por inducción. Todos los \(U_N^jf\)
tienen soporte finito. No se necesita que \(H_\xi r\) o
\(H_\xi\phi_N\) pertenezcan a \(\ell^2\).

Sean \(B\) la restricción espacial a Bob y
\[
(\mathcal Vz)(y)=\mathbf1_{\mathcal B_N}(y)
 e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}z)(y),\qquad
\mathcal V_c=\pi_c\mathcal V.
\tag{6}
\]
Para cada N fijo esta aplicación está bien definida sobre \(L^2\),
pues Bob tiene soporte finito. Más explícitamente, \(\mathcal V\) es
la composición de la inversa de Fourier unitaria con el multiplicador
\(\mathbf1_{\mathcal B_N}(y)e^{-\xi_*\cdot(y-y_*)}\), cuyo máximo
es finito. Como \(0\le E\le I\) y \(\pi_c\) es acotado,
\(\mathcal H_c=\mathcal V_c^*E\mathcal V_c\) es un operador
acotado, positivo y autoadjunto. Este argumento sólo asegura que
los objetos existen para N fijo; no transfiere cotas asintóticas.
Con los centros y escala ya fijados,
\(y_*-x_*=Nv_*\) y \(K_*=\xi_*\cdot v_*-\Phi_*\), (5) da
\[
Bd=e^{-K_*N}\mathcal Vt_N.
\tag{7}
\]
El factor se obtiene exactamente de
\(\Lambda^Ne^{-\xi_*\cdot(y-x_*)}
=e^{-K_*N}e^{-\xi_*\cdot(y-y_*)}\).
Extraerlo no es una estimación del tamaño de los factores restantes.

Definimos las dos contribuciones de **salida**:
\[
d_{c,P}=e^{-K_*N}\mathcal V_cPt_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_cQt_N,\qquad
B\pi_cd=d_{c,P}+d_{c,Q}.
\tag{8}
\]
Son amplitudes en Bob. No se afirma que desinclinar por separado
P y Q produzca vectores globales en el Hilbert físico. La restricción
en (6) evita exigir esa propiedad, innecesaria para el efecto local.

## 3. Expresión firmada completa para cada canal

Escribiendo \(r_c=B\pi_cr\), las probabilidades de ambos bits son
\[
p_{c,0}=\langle r_c,Er_c\rangle,
\qquad
p_{c,1}=\langle r_c+d_{c,P}+d_{c,Q},
                 E(r_c+d_{c,P}+d_{c,Q})\rangle.
\tag{9}
\]
Al restarlas:
\[
\boxed{\begin{aligned}
L_c={}&2\operatorname{Re}\langle r_c,E d_{c,P}\rangle
      +2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle\\
 &+\langle d_{c,P},E d_{c,P}\rangle
  +\langle d_{c,Q},E d_{c,Q}\rangle
  +2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\quad c=+,-.
\end{aligned}}
\tag{10}
\]
Ésta es la fórmula de T1. No contiene normas ni valores absolutos de
las respuestas. Los dos términos cuadráticos diagonales son reales
y no negativos; los términos de interferencia conservan sus signos.

Por indicación del usuario, se congela el siguiente vocabulario para T2,
con cinco contribuciones por canal:
\[
\begin{aligned}
A_{cP}&=2\operatorname{Re}\langle r_c,E d_{c,P}\rangle,\\
A_{cQ}&=2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle,\\
B_{cPP}&=\langle d_{c,P},E d_{c,P}\rangle,\\
B_{cQQ}&=\langle d_{c,Q},E d_{c,Q}\rangle,\\
B_{cPQ}&=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\end{aligned}
\qquad
\boxed{L_c=A_{cP}+A_{cQ}+B_{cPP}+B_{cQQ}+B_{cPQ}.}
\tag{10a}
\]
Estas etiquetas designan escalares del observable. No son los bloques
de transporte \(A_j,B_j\) de §4 ni nuevos proyectores.

Si se llama
\[
L_{c,A}=2\operatorname{Re}\langle r_c,E d_{c,A}\rangle
              +\langle d_{c,A},E d_{c,A}\rangle\quad(A=P,Q),
\]
entonces la identidad es
\[
L_c=L_{c,P}+L_{c,Q}+L_{c,\mathrm{cross}},\qquad
L_{c,\mathrm{cross}}=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle.
\tag{11}
\]
La aditividad de sólo dos términos requiere que este último escalar
sea cero para los datos considerados; T1 no establece tal anulación.
Repartirlo por convenio entre P y Q no demostraría una separación física.

En la representación auxiliar, sea
\[
\mathcal H_c=\mathcal V_c^*E\mathcal V_c,\qquad
\ell_c(z)=\langle r_c,E\mathcal V_cz\rangle.
\]
La misma fórmula, antes de agrupar términos conjugados, es
\[
\begin{aligned}
L_c={}&e^{-K_*N}\{
\ell_c(Pt_N)+\overline{\ell_c(Pt_N)}
+\ell_c(Qt_N)+\overline{\ell_c(Qt_N)}\}\\
&+e^{-2K_*N}\sum_{A,B\in\{P,Q\}}
  \langle t_N,A^*\mathcal H_c B t_N\rangle.
\end{aligned}
\tag{12}
\]
Aquí \(PQ=0\) no elimina \(P^*\mathcal H_cQ\). El efecto de Bob,
la reconstrucción y los adjuntos permanecen en su lugar. Incluso una
partición ortogonal no permitiría ese paso sin una condición adicional
sobre el efecto. El extremo lineal es exactamente el determinado por
\(w_c=F_cr\), soportado en Bob y dependiente de \(U_N\).

## 4. Compatibilidad con los bloques temporales existentes

No se estima ni se reabre la vía Volterra. Sólo se sustituyen los datos
de (4) en sus identidades finitas. Con \(x_j=Pt_j\), \(y_j=Qt_j\),
\[
A_j=PTP,\quad B_j=PTQ,\quad C_j=QTP,\quad D_j=QTQ,
\]
\[
x_{j+1}=A_jx_j+B_jy_j,\qquad
y_{j+1}=C_jx_j+D_jy_j,\qquad (x_0,y_0)=(Ps,Qs).
\tag{13}
\]
Los subíndices se conservan para coincidir con el precheck; en este
protocolo el paso T es el mismo en todas las capas. Los productos
vacíos son las identidades de los respectivos rangos.

Con \(\Phi_P(j,k)=A_{j-1}\cdots A_k\) y
\(G_Q(j,k)=D_{j-1}\cdots D_k\), la sustitución sucesiva de (13) da
\[
\begin{aligned}
x_N={}&\underbrace{\Phi_P(N,0)Ps}_{\text{trayectoria siempre en P}}\\
 &+\underbrace{\sum_{m=0}^{N-1}
 \Phi_P(N,m+1)B_mG_Q(m,0)Qs}_{f_{Q,N}}\\
 &+\underbrace{\sum_{m=0}^{N-1}\sum_{k=0}^{m-1}
 \Phi_P(N,m+1)B_mG_Q(m,k+1)C_kx_k}_{(\mathbb M_Nx)_N},\\
y_N={}&G_Q(N,0)Qs+
 \sum_{k=0}^{N-1}G_Q(N,k+1)C_kx_k.
\end{aligned}
\tag{14}
\]
Se verifica (14) primero resolviendo la segunda recurrencia de (13),
y sustituyéndola en la primera con su transporte \(\Phi_P\).
Así, los objetos de (8) son exactamente
\[
d_{c,P}=e^{-K_*N}\mathcal V_c x_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_c y_N.
\tag{15}
\]
La contribución que termina en P incluye retornos y entradas desde Q:
no es la contribución que permaneció siempre en P. Esta última es
únicamente el primer sumando de \(x_N\) en (14).

Si \(d_{c,0}\) denota la reconstrucción de ese primer sumando y
\(\delta d_c=d_{c,P}+d_{c,Q}-d_{c,0}\), la respuesta respecto de
esa amplitud, **manteniendo la referencia física r**, satisface
\[
\begin{aligned}
L_{c,0}&=2\operatorname{Re}\langle r_c,E d_{c,0}\rangle
                 +\langle d_{c,0},E d_{c,0}\rangle,\\
L_c-L_{c,0}&=2\operatorname{Re}\langle r_c+d_{c,0},E\delta d_c\rangle
                      +\langle\delta d_c,E\delta d_c\rangle.
\end{aligned}
\tag{16}
\]
Esto identifica el funcional exacto al que entrarían las correcciones
de (14); no les asigna potencia, pequeñez ni dominancia relativa.
Tampoco define una dinámica alternativa para el bit cero.

## 5. Comprobaciones internas por otra formulación y caso límite

**Segunda derivación, mediante la diferencia de estados.** Si
\(v=J\phi_N\), la diferencia inicial es exactamente
\[
\Delta=|v+f\rangle\langle v+f|-|v\rangle\langle v|
=|f\rangle\langle v|+|v\rangle\langle f|+|f\rangle\langle f|.
\]
Al conjugar por \(U_N^N\) y tomar la traza contra \(F_c\), los
dos primeros sumandos dan los términos lineales de (2) y el tercero
da su término cuadrático. Sustituir (8) genera las cuatro parejas
\(PP,PQ,QP,QQ\) de (12), incluidos ambos adjuntos cruzados.
Es la misma identidad obtenida desde las probabilidades (9).

**Control plano.** Si \(\vartheta=0\), T es diagonal por canales,
y también lo son P y Q de (3). Como \(f=J(U_M-I)\phi_N\),
\(r_-=d_{-,P}=d_{-,Q}=0\). Por (10), \(L_-=0\). En el canal
positivo \(r_+=BS^N\phi_N\) y
\(d_{+,P}+d_{+,Q}=BS^N(U_M-I)\phi_N\), por lo que (10) recupera
exactamente \(L_+=L_{\rm plano}\), para los dieciséis pares.
Este control verifica la reconstrucción, sin afirmar que se anule
el cruce P/Q dentro del canal positivo.

**Control acoplado de las recurrencias.** Para N=2 y bloques genéricos,
la multiplicación directa de dos matrices de bloques da
\[
\begin{aligned}
x_2&=A_1A_0x_0+A_1B_0y_0+B_1C_0x_0+B_1D_0y_0,\\
y_2&=C_1A_0x_0+C_1B_0y_0+D_1C_0x_0+D_1D_0y_0.
\end{aligned}
\tag{17}
\]
Por otra vía, (14) da
\(f_{Q,2}=A_1B_0y_0+B_1D_0y_0\),
\((\mathbb M_2x)_2=B_1C_0x_0\) y
\(y_2=D_1D_0y_0+D_1C_0x_0+C_1x_1\), con
\(x_1=A_0x_0+B_0y_0\). Esto reproduce (17) sin suponer que los
acoplamientos se anulen.

Un caso concreto con retorno no nulo es la fibra del saddle p=0,
restringida a un par intercambiado por beta, con moneda constante.
En la base donde \(D_\xi=\operatorname{diag}(\Lambda,\Lambda^{-1})\)
y \(\beta=\sigma_x\), para \(a=\theta/2\),
\[
T=\begin{pmatrix}
\cos a&-i\sin a\,\Lambda^{-2}\\
-i\sin a&\cos a\,\Lambda^{-2}
\end{pmatrix},\qquad P=\operatorname{diag}(1,0).
\tag{18}
\]
Si \(\sin a\ne0\), B y C son no nulos y
\(BC=-\sin^2a\,\Lambda^{-2}\). Para \((x_0,y_0)=(1,0)\),
\[
x_2=\cos^2a-\sin^2a\,\Lambda^{-2},\qquad
y_2=-i\sin a\cos a\,(1+\Lambda^{-2}),
\]
tanto por \(T^2\) como por (17). La diferencia de \(x_2\) respecto
de la trayectoria siempre P es exactamente BC. Es un test algebraico
de fibra; no se identifica un estado de una sola fibra con la preparación
normalizada del protocolo ni se amplía la clase de perfiles físicos.

**Control nulo.** Si en un test se toma \(U_{\rm enc}=I\), entonces
\(f=s=0\) y ambos bits preparan el mismo estado; todos los términos
de (10) son cero para cualquier moneda. No confundirlo con M=I:
el encoder congelado correspondiente es \(e^{i\pi F_N/2}I\ne I\).
Es un control algebraico, no una ampliación de la familia de encoders.

**POVM completo.** La unitariedad física y la normalización de ambos
bits dan \(L_\varnothing=-L_+-L_-\). La suma inclusiva conserva los
términos cruzados de (10) para ambos canales; T1 no demuestra que
se anulen en esa suma. No se infiere \(L_++L_-=0\).

## 6. Resultado y techo

T1 produce un observable firmado exacto compatible con el P/Q existente:
(10), con datos físicos (1), lift (4)–(8) y bloques (13)–(15).
La referencia y los dos bits están incluidos sin imponer una nueva
hipótesis de decaimiento exponencial a la preparación. El STOP por
incompatibilidad algebraica de T1 no se activa en esta derivación.

La derivación y sus controles son internos: no constituyen revisión
independiente ni promoción de un gate canónico. Sigue pendiente T2:
este documento no identifica un coeficiente de orden \(N^{-6}\),
no transfiere cotas de extremos y no demuestra una relación entre
los dos canales. T3 tampoco se ejecuta. H1/H1c, la justificación física,
E0, POWER_13/2_STABILITY, E/AdS y el manuscrito conservan su estado.

No se ha ejecutado código científico ni generado datos numéricos.
La procedencia de las fórmulas nuevas es su derivación explícita en
este archivo; los prechecks aportan la notación y el contrato, no una
certificación de sus estimaciones previas.

## 7. T2: alcance fijado, ejecución pendiente

Orden obligatorio por instrucción del usuario:
T1 → revisión independiente y cierre de sus reparaciones → T2 → T3.
No se ejecuta T2 mientras la versión reparada esté pendiente de revisión.

La pregunta es qué contribución, o sub-contribución identificada, hereda
realmente el techo previo \(O(N^{-6})\). No se asigna de antemano ese
orden a ninguna de las diez piezas de (10a).

T2 deberá producir diez filas, una por cada
\(A_{+P},A_{+Q},B_{+PP},B_{+QQ},B_{+PQ}\) y
\(A_{-P},A_{-Q},B_{-PP},B_{-QQ},B_{-PQ}\), con estos campos:

| Campo | Contenido requerido |
| --- | --- |
| Objeto previo | Fórmula y localización precisa del bloque o extremo que se pretende usar; distinguir pieza completa y sub-contribución. |
| Cota disponible | Enunciado, hipótesis, ámbito, dependencia en W fijo y nivel de revisión; marcar explícitamente cuando no haya transferencia justificada o uniformidad en W. |
| Información perdida | Signos, fases, interferencias o dependencia de la referencia que desaparecieron al tomar normas. |
| Escala resultante | Factores exponenciales y potencias de N, indicando si se trata del observable físico o de una cantidad normalizada; distinguir cota superior y término asintótico identificado. |

El producto \(N^{-5/2}N^{-1}N^{-5/2}=N^{-6}\) sólo proporciona
un recuento de cotas hasta que se identifique el elemento bilineal,
sus extremos físicos y su lugar exacto en (10a). Las cotas heredadas
para extremos planos no se transfieren automáticamente a \(r_c\).
P/Q final tampoco etiqueta el número de excursiones: se conserva (14).

No se introduce ninguna técnica nueva. Si una transferencia no está
justificada por lo ya disponible, se registra esa carencia sin abrir
una nueva vía de estimación. T2 no busca simetrías ni ejecuta T3.

Para cualquier posterior afirmación de cancelación, se mantendrán
separados estos tres niveles:

1. Dentro de una pieza de (10a).
2. Entre piezas de un mismo canal.
3. Entre canales, en \(L_++L_-\).

El tercer nivel no prueba cancelación en ninguno de los dos canales
por separado. El número de piezas que reciban una misma cota tampoco
decide por sí solo si hay una relación estructural.

Si T2 sólo recupera una cota gruesa sin coeficiente identificado, la
conclusión será que \(N^{-6}\) sigue siendo un techo sin término
asintótico aislado. Eso no prueba que un término de ese orden sea
inexistente, ni que su coeficiente sea cero. En ese caso se aplica el
STOP previsto: no buscar simetrías de un coeficiente no identificado.
```

### Contexto adjunto: papers/ir-corona/ir-corona.tex
```
\documentclass[11pt]{amsart}

\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\T}{\mathbb{T}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cK}{\mathcal{K}}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\up}{{\uparrow}}
\newcommand{\dn}{{\downarrow}}
\newcommand{\Cmicro}{C_{\mathrm{micro}}}
\newcommand{\cIR}{c_{\mathrm{IR}}}
\newcommand{\arcosh}{\operatorname{arcosh}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Tr}{\operatorname{Tr}}
\newcommand{\Hess}{\operatorname{Hess}}
\newcommand{\re}{\operatorname{Re}}
\newcommand{\im}{\operatorname{Im}}
\newcommand{\vstar}{v_*}
\newcommand{\xistar}{\xi_*}
\newcommand{\uhat}{\hat u}

\begin{document}

\title[Infrared response outside the emergent light cone]{An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk}

% TODO(author): any AI-assistance disclosure required by the target journal.
\author{Jos\'e Ignacio Mart\'in Gandul}
\address{Independent Researcher, Seville, Spain}
\email{adnacho@gmail.com}

\date{\today}

\begin{abstract}
In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support.  We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region.  All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node.  Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a \emph{corona}.  There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control.  Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector.  All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
produces only a vanishing fraction of its output outside the wider band
$|p|\le N^{-1/2}$.  Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$.  For a concrete
family of sixteen encoder--detector pairs, it has the exact leading
asymptotics
\[
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
\]
Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser.  The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
the sixteen pairs.  The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations.  The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support.  The result is purely asymptotic: the
remainder constants are not explicit, and numerical diagnostics indicate
that the leading term is quantitatively accurate only for $N$ of order
$10^3$ and beyond.
\end{abstract}

\maketitle

\section{Introduction}\label{sec:intro}

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation
\cite{SchumacherWerner,Arrighi,Farrelly}.  After $N$ steps of a finite-range
walk, the propagator vanishes identically outside $N\Cmicro$.  Here
$\Cmicro=\operatorname{conv}F$ is the convex hull of the one-step jumps.
Many such walks have a conical point in their dispersion relation.  Near it,
the long-wavelength dynamics is that of a Weyl or Dirac equation with a
speed of light $\cIR$
\cite{BialynickiBirula,DArianoPerinotti,BDPT,DArianoErbaPerinotti}.

In spatial dimension $d\ge2$ the two causal structures cannot coincide.  The
infrared cone of a Weyl node is a Euclidean ball, and $\Cmicro$ is a
polytope.  Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice.  It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin \cite{BHS}, but that
setting lies outside the scope of this paper.  For a lattice walk, some
velocities are therefore causally allowed but not relativistic.  How much
physics can be sent through them?

Three questions must be kept apart.

\begin{description}
\item[(U) Ultraviolet propagator] Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside $N\Cmicro$?  For
  the walk studied here it does: along the eight vertex rays a single
  lattice path contributes, with amplitude of norm $4^{-N}$
  (Proposition~\ref{prop:geometry}).  One-step Alice/Bob protocols built
  from localized operations turn this into a finite distinguishability
  (for instance $3/128$ after one step for a suitable localized
  preparation, as recorded in~\cite{Repo}).  Such protocols are broadband:
  their operations are not concentrated near the Weyl node.
\item[(I) Infrared operational response] Require the preparation, the
  encoder and the detector to be infrared-admissible, and put Bob outside
  the infrared cone of \emph{every} site of Alice.  Does Bob's
  distinguishability still fail to vanish as the infrared scale goes to
  zero, and at what rate?
\item[(N) Nature] Is there a physical system in which the lattice scale and
  the operations are given rather than engineered?  This question is not
  addressed here.
\end{description}

A non-zero ultraviolet kernel does not answer (I).  Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U).  This paper answers (I), for
one walk and one explicit protocol.

\subsection*{The walk}
We work with the Weyl walk of Cedzich, Joye, Werner and Werner
\cite[Eq.~(5.15)]{CJWW}.  They introduced it as a modification of the
Bialynicki-Birula Weyl automaton \cite[Eq.~(5.12)]{CJWW},
\cite{BialynickiBirula}, with the same conical points and with a
\emph{spherical} propagation region.  For this walk the three velocity sets
are nested as
\begin{equation}\label{eq:three-bodies}
\Gamma\;\subseteq\;B(1)\;\subsetneq\;\Cmicro=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=\cIR=1 .
\end{equation}
Here $B(1)=\overline B(0,1)$ is the closed infrared light cone ($\cIR=1$),
$\Gamma$ is the closed set of group velocities, and $\Cmicro$ is the strict
causal body.  Both statements in \eqref{eq:three-bodies} are exact, and
moreover $\partial B(1)\subseteq\Gamma$ (Proposition~\ref{prop:geometry}).
Numerically, $\Gamma$ fills the ball; this is not proved and not used.
Every ballistic mode, at every energy, therefore respects the emergent light
speed.  Nevertheless, in every non-axial direction $\hat n$ the causal
support extends to $\|\hat n\|_1\in(1,\sqrt3\,]$ times the light speed.
Probability outside $\Gamma$ is exponentially small in $N$ \cite{CJWW}.  The
question is whether it can be \emph{used} under infrared control.

\subsection*{Main results}
Section~\ref{sec:protocol} gives the precise definitions.  In outline,
Alice's region is the lattice ball $\cA_N$ of radius $N/4$ at the origin,
and Bob's region is the lattice ball $\cB_N$ of radius $N/4$ at $N(1,1,1)$.
After $N$ steps, every pair $(x,y)\in\cA_N\times\cB_N$ is separated by more
than $N+N/5$.  Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$.  The resource is a narrow-band packet of
momentum width $\Lambda=1/N$.  Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$.  Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$.  The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish quadratically
on the spheres.

\begin{enumerate}[label=(\roman*)]
\item \emph{Infrared admissibility} (Theorem~\ref{thm:admissible}).  All
  eight operations map the band $|p|\le N^{-1}$ into the band
  $|p|\le N^{-1/2}$, up to relative errors $O(N^{-1/2})$ with explicit
  constants.  Single-site operations fail this criterion maximally
  (Lemma~\ref{lem:point}).
\item \emph{Explicit upper bound} (Theorem~\ref{thm:upper}).  For every
  $N\ge2$, every unitary acting in $\cA_N$, every one-particle state and
  every effect in $\cB_N$, Bob's distinguishability is at most
  $36N^4e^{-JN}$, with $J=(1-\tfrac{\sqrt3}{2})\log2$.  Polynomial infrared
  signalling is excluded.
\item \emph{Regional rate} (Theorem~\ref{thm:rate}).  The kernel between
  the two regions is $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal
  regional value of a Legendre rate function.  Here $I$ is the Legendre
  transform of $\Phi(\xi)=\arcosh(\prod_j\cosh\xi_j)$, and
  $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
  regional velocity set.  Moreover $J<K_*<\log4$.  By (iv), the rate $K_*$
  is attained by an explicit response.
\item \emph{Leading asymptotics} (Theorem~\ref{thm:main}).  For all sixteen
  encoder--detector pairs,
  $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
  The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
  uniformly non-zero, with relative oscillation in $\theta$ at most
  $1.5\times10^{-3}$.
\end{enumerate}

Result (iv) is an asymptotic statement and not a numerical approximation
valid from small $N$.  The constants in its remainder are not explicit, and
neither is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is
guaranteed.  Finite-$N$ diagnostics (Appendix~\ref{app:numerics}) indicate
a relative correction of about $-100/N$, so the leading term is
quantitatively accurate only for $N\gtrsim10^3$.  For the pairs with the
smallest coefficients, the next-order term $N^{-17/2}e^{-K_*N}$ dominates
throughout the diagnostic range $N\le56$ (Remark~\ref{rem:features}).

The coefficient is not a product of local factors.  It arises from the
interference between the \emph{free tail} of the resource at Bob, which is
only polynomially small, and the part of Alice's encoding that reaches Bob,
which is exponentially small.  Two points of the complex-shifted Brillouin
torus contribute, and they enter with different projectors.  The power
$13/2$ is not a count of Gaussian directions.  The two normal directions are
discrete sums over lattice planes of depth $O(1)$, and the common tangential
direction is a flat direction of the exponent that is confined only by the
profiles.

\subsection*{Relation to the literature}
Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical \cite{Konno,GJS,AVWW}: $Q(t)/t$ converges in
distribution to the group velocity distributed by the initial state.
Cedzich, Joye, Werner and Werner \cite{CJWW} proved that the probability of
velocities outside the support of this limit decays exponentially.  They gave
a method for bounding the rate uniformly in the initial state and discussed
the ``fuzziness'' of the emergent light cone in exactly this language.  Our
upper bound (ii) uses their contour-shift idea, supplemented by an elementary
ellipse lemma and a Jordan-safe bound on matrix powers.  Their method bounds
rates; it does not give prefactor-level asymptotics.

Sharp asymptotics with prefactors outside the propagation region are known
in one dimension.  Sunada and Tate \cite{SunadaTate} obtained exact local
asymptotics of transition probabilities, including exponential decay with an
explicit prefactor in the region hidden from the weak limit.  Carteret,
Richmond and Temme \cite{CRT} obtained uniformly convergent asymptotics in
the exponentially decaying regions of coined walks on the line.  These are
the closest precursors of the saddle-point analysis of
Section~\ref{sec:asymptotics}.  In two dimensions, Baryshnikov, Brady,
Bressler and Pemantle \cite{BBBP} analysed quantum walks through multivariate
generating functions and determined the limiting profile in the feasible
region, outside of which the probability is exponentially small.  Analytic
combinatorics in several variables \cite{ACSV} provides general transfer
theorems for multivariate coefficient asymptotics, whose standard sharp
forms assume minimality hypotheses on the critical points.  We do not claim
that these methods cannot reproduce the present result.  We are not aware of
a transfer theorem that yields it directly, and we carry out the
model-specific saddle-point analysis explicitly.

What we add is a \emph{lower} bound, in the strong form of exact leading
asymptotics.  It concerns an \emph{operational} quantity: the
distinguishability produced by a local encoding.  The encoding is spread
over a region of size $O(N)$ and constrained to be infrared-admissible, in
dimension three, and at a point strictly inside the corona.  Upper bounds
alone cannot distinguish an exponentially small response from an exactly
vanishing one.  In the problem studied here that distinction is the
content of the result.  The novelty claim is correspondingly narrow.  To our
knowledge, Theorem~\ref{thm:main} is the first prefactor-level asymptotic,
with a leading coefficient that is oscillatory and certified to be
non-vanishing, for an infrared-controlled operational response in the
strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk.  Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb--Robinson bounds \cite{LiebRobinson,BHV} give exponentially small
leakage outside a linear cone for continuous-time lattice dynamics.  For
quantum walks the strict cone $\Cmicro$ plays that role exactly, and the
question here is the one \emph{inside} it.

\subsection*{Organisation}
Section~\ref{sec:walk} sets up the walk and proves the geometric statements.
Section~\ref{sec:protocol} defines the protocol and infrared admissibility.
Section~\ref{sec:results} states the results.  Sections~\ref{sec:upper}
to~\ref{sec:asymptotics} contain the proofs.  Section~\ref{sec:discussion}
discusses scope and limitations.  Appendix~\ref{app:numerics} lists the
computer-assisted parts and the finite-$N$ diagnostics.

\section{The walk and its three velocity sets}\label{sec:walk}

\subsection{Conventions}
The one-particle Hilbert space is $\mathcal H=\ell^2(\Z^3;\C^2)$ with
internal basis $\up=(1,0)^T$ and $\dn=(0,1)^T$.  We use the Fourier
transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\T^3=[-\pi,\pi)^3$.  We write $c_j=\cos p_j$ and
$s_j=\sin p_j$.  $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of \cite[Eq.~(5.15)]{CJWW} has symbol
\[
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
\]
States evolve by the unitary $S$ with symbol
\begin{equation}\label{eq:symbol}
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\end{equation}
Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\C^3$.  For $p\in\C^3$, $S(p)$ denotes the continuation of
\eqref{eq:symbol}, which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$.  The $N$-step kernel is
\begin{equation}\label{eq:kernel}
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\end{equation}

\begin{lemma}[Jumps]\label{lem:jumps}
The set $F=\{d:S_d\ne0\}$ has fourteen elements: the eight vertices
$(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$, and the two
axial jumps $(\pm1,0,0)$.  Each vertex block is $\frac14$ times a rank-one
diagonal projector; in particular $S_{(1,1,1)}=\frac14|\dn\rangle\langle\dn|$.
The face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.
\end{lemma}

\begin{proof}
This is a direct expansion of \eqref{eq:symbol} in $z_j=e^{ip_j}$.  The
coefficient of $z_1z_2z_3$ comes only from the $(2,2)$ entry
$c_1c_2e^{ip_3}$ and equals $\frac14$.
\end{proof}

\subsection{Dispersion and the infrared node}
Since $\det S=1$ and $\tr S(p)=2c_1c_2c_3$, the eigenvalues of $S(p)$ are
$e^{\mp i\omega(p)}$ with
\begin{equation}\label{eq:dispersion}
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\end{equation}
At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with
\[
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
\]
This is a Weyl Hamiltonian with speed $\cIR=1$.  The same conical structure
occurs at the eight points of $\{0,\pi\}^3$.

\begin{proposition}[Geometry]\label{prop:geometry}
\begin{enumerate}[label=(\alph*)]
\item The causal body is $\Cmicro=\operatorname{conv}F=[-1,1]^3$.  Its
  support function is $h_{\Cmicro}(\hat n)=\|\hat n\|_1$ for unit vectors
  $\hat n$.
\item At every $p$ where $\omega$ is differentiable,
  \begin{equation}\label{eq:SOS}
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \end{equation}
  and hence $|\nabla\omega(p)|\le1$.  At the conical points $\nabla\omega$
  takes every value in the unit sphere.  Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set
  of group velocities.
\item For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector.  In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|\dn\rangle\langle\dn|$.  Hence the $N$-step
  support function equals $N\|\hat n\|_1$ exactly.
\end{enumerate}
\end{proposition}

\begin{proof}
(a) follows from Lemma~\ref{lem:jumps}.  The supremum of $\hat n\cdot x$ over
the cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$.  The identity \eqref{eq:SOS} is a polynomial identity
in $(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion.  Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$.  Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so
$\sum_k\sigma_i(d_k)_i=N$ forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$,
that is, $d_k=\sigma$.  Hence $(S^N)_{N\sigma,0}=S_\sigma^N$.  By Lemma~\ref{lem:jumps},
$S_\sigma=\frac14\Pi_\sigma$, so $S_\sigma^N=4^{-N}\Pi_\sigma$.
\end{proof}

\begin{remark}
The reverse inclusion $B(1)\subseteq\Gamma$, that is, that $\Gamma$ fills
the ball, holds numerically but is not proved and not used.  What is used is
the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le\cIR$, with equality by $\partial B(1)\subseteq\Gamma$.  Consequently the relation
$\sup|v_g|=\cIR$ does \emph{not} imply that the emergent cone coincides with
the causal boundary.  The two coincide only in the six axial directions.
The \emph{corona} is $\Cmicro\setminus B(1)$.  Propagation into $N$ times
the corona is not ballistic, but by (c) it is not forbidden.
\end{remark}

\begin{remark}
For the Bialynicki-Birula walk \cite[Eq.~(5.12)]{CJWW}, $\Gamma$ is contained
in the intersection of three orthogonal cylinders (and numerically equal to
it \cite[Fig.~5]{CJWW}).  It contains group velocities up to
$\sqrt{3/2}>\cIR$, attained at $p=-\frac\pi4(1,1,1)$.  In that walk the corona contains a ballistic sector
faster than the emergent light.  We restrict to \cite[Eq.~(5.15)]{CJWW}
precisely because it has no such sector.
\end{remark}

\section{Protocol and infrared admissibility}\label{sec:protocol}

Fix an integer $N\ge2$.  The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$.  Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write $\Pi=\Pi_{\Lambda_N}$
and $\Pi'=\Pi_{\Lambda'_N}$.  For $N\ge2$ both balls lie in $|p|<\pi/4$,
where $f>0$ and the only conical point is $p=0$.

\subsection{Regions}
Let
\[
\cA_N=\{x\in\Z^3:|x|\le N/4\},\qquad \cB_N=\{y\in\Z^3:|y-N(1,1,1)|\le N/4\},
\]
with Euclidean norms throughout.  For every $x\in\cA_N$ and $y\in\cB_N$,
\begin{equation}\label{eq:separation}
|y-x|-N\ge(\sqrt3-\tfrac32)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge(3-\tfrac{\sqrt3}2)N,\quad u=(1,1,1).
\end{equation}
Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$.  Each region has at most $(N/2+1)^3\le N^3$
sites.

\subsection{Resource, encoder, detector}
Let $g(q)=(1-|q|^2)_+^2$.  The resource is
\[
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,\dn,
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
\]
so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$.  In position space
$\phi_N=\varphi_N\,\dn$ with the real, radial function
\begin{equation}\label{eq:resource}
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\end{equation}
This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in $\cA_N$.  For
$M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the multiplication
operator
\[
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
\]
It acts as the identity outside $\cA_N$.  In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\cB_N$.
For $M_B\in\{I,P_1,P_2,P_3\}$, with $P_j=(I+\sigma_j)/2$, the effect is
\[
E=h_N\otimes M_B,\qquad 0\le E\le I .
\]

\subsection{Signal}
Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$ to
the resource.  After $N$ steps the state is
$\psi_b(N)=S^NU^{(b)}\phi_N$.  The signal is
\begin{equation}\label{eq:signal}
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\end{equation}
where $L_{M,M_B}(N)$ denotes the signed difference.  No spectral projection is
applied to the signal.  Infrared admissibility is a property of the
operations only.  We also consider the trace distance $D_B(N)$ between Bob's
reduced states.  In the free-fermion description, the reduced state of a
one-particle vector $\psi$ on the modes of $\cB_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

\subsection{Infrared admissibility}
\begin{definition}\label{def:admissible}
For a bounded operator $X$ on $\mathcal H$ with $X\Pi\ne0$, set
\[
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
\]
The encoder $U_M$ is \emph{infrared-admissible} if
$\eta_{\mathrm{op}}(U_M-I)\to0$ and
\[
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
\]
as $N\to\infty$, where $\Delta_M\ne0$ is required for $\eta_{\mathrm{enc}}^M$
to be defined.  The effect $E$ is infrared-admissible if
$\eta_{\mathrm{op}}(E)\to0$.
\end{definition}

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem~\ref{thm:admissible}).

In words: acting on anything in the infrared band, an admissible operation
leaves only a vanishing fraction of its output outside the wider band
$\Pi'$.  A strictly local gate cannot do this.

\begin{lemma}[Single-site operations are ultraviolet]\label{lem:point}
If $X\Pi\ne0$ and $\operatorname{ran}X\subseteq\ell^2(\{x_0\};\C^2)$ for a
single site $x_0$, then
$\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.
\end{lemma}

\begin{proof}
For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$.
\end{proof}

This is the reason the encoder is spread over a region of size $O(N)$ with
a smooth profile.  A pointlike phase gate, such as $I-2P_{x_0}$, is
excluded by Lemma~\ref{lem:point}.  The regional operations pass:

\begin{theorem}[Admissibility]\label{thm:admissible}
Let $K_e=\frac\pi2(2+8\sqrt3\pi)$, $K_d=\frac\pi2(1+16\sqrt3)$ and
$m=11/(560\pi^2\,32^3)$.  For all $N\ge32$, all four $M$ and all four
$M_B$,
\[
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
\]
All denominators are non-zero for every $N\ge2$.
\end{theorem}

The constants are conservative.  The proof is in Section~\ref{sec:admissible}.

\section{Results}\label{sec:results}

\begin{theorem}[Explicit upper bound]\label{thm:upper}
Let $N\ge2$ and $T_N=\|P_{\cB_N}S^NP_{\cA_N}\|$.  Then
\[
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
\]
Consequently, for every unitary $U$ acting as the identity outside
$\cA_N\otimes\C^2$, every one-particle state and every effect in $\cB_N$,
\[
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
\]
\end{theorem}

\begin{remark}[Formal verification]
Theorem~\ref{thm:upper} is machine-checked in Lean~4 with Mathlib
(\texttt{formal/} in~\cite{Repo}), for every $N\ge2$ and without
additional axioms.  This covers the kernel bound, the geometry
\eqref{eq:separation}, the counting of lattice points, the operator bound on
$T_N$, and the step $\delta\le4T_N$.  The formal proof bounds the matrix
powers through Cayley--Hamilton and entrywise estimates instead of
Lemma~\ref{lem:schur}, and obtains the sharper constant
$T_N\le4N^4e^{-JN}$.  Both constants are valid; the proof in
Section~\ref{sec:upper} keeps the constant $9$ that the elementary
Lemma~\ref{lem:schur} gives.  The identification of Bob's amplitudes with the
restricted walk, and the second-quantized distance $D_B$, are not
formalized.
\end{remark}

For $\xi\in\R^3$ put $\Phi(\xi)=\arcosh\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$
and define the rate function
\begin{equation}\label{eq:rate}
I(v)=\sup_{\xi\in\R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\end{equation}
Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$.  This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\cA_N,\cB_N$.

\begin{theorem}[Regional rate]\label{thm:rate}
\begin{enumerate}[label=(\alph*)]
\item $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
\item On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$.  The corresponding dual
  tilt is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$.  Moreover
  \[
  K_*:=I(v_*)=3\alpha t_*-\arcosh(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  \]
\item $J<K_*<\log4$.  Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
\item For all $N\ge2$ and all $(x,y)\in\cA_N\times\cB_N$,
  \[
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  \]
  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.
\end{enumerate}
\end{theorem}

The main result identifies the exact leading behaviour of every signal in
the family.  Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

\begin{theorem}[Leading asymptotics]\label{thm:main}
For each of the sixteen pairs $(M,M_B)$ there is a continuous, $1$-periodic,
real function $C_{M,M_B}(\theta)$ such that, as $N\to\infty$,
\[
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
\]
Explicitly,
\begin{equation}\label{eq:C}
C_{M,M_B}(\theta)=\cK\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\end{equation}
with the constants $\cK$, $c_r$, the functions $\Gamma_\pm$ and the numbers
$\ell_0,\ell_\pi$ defined in Section~\ref{sec:asymptotics}.  For every pair,
\[
C_{M,M_B}(\theta)=\overline C_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline C_{M,M_B}\ne0,
\]
with the values in Table~\ref{tab:C}.  Consequently, for every pair,
\[
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\]
and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.
\end{theorem}

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$.  Theorem~\ref{thm:main} therefore does not
assert $\delta_{M,M_B}(N)>0$ at any specified $N$.  It also does not say from
which $N$ on the leading term is numerically accurate
(Section~\ref{sec:discussion}).

\begin{table}[t]
\centering
\small
\begin{tabular}{llrr}
\toprule
$M$ & $M_B$ & $\overline C_{M,M_B}$ & $\sup_\theta|C/\overline C-1|$\\
\midrule
$I$ & $I$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$I$ & $P_1$ & $+1.2072650683$ & $1.09\cdot10^{-3}$\\
$I$ & $P_2$ & $+0.8164098576$ & $1.08\cdot10^{-3}$\\
$I$ & $P_3$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_1$ & $I$ & $-3.7206303938$ & $1.05\cdot10^{-3}$\\
$\sigma_1$ & $P_1$ & $-1.5567800857$ & $1.06\cdot10^{-3}$\\
$\sigma_1$ & $P_2$ & $-2.8203960182$ & $1.02\cdot10^{-3}$\\
$\sigma_1$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $I$ & $-2.9389199724$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $P_1$ & $-0.5846543741$ & $1.02\cdot10^{-3}$\\
$\sigma_2$ & $P_2$ & $-1.7729950974$ & $1.04\cdot10^{-3}$\\
$\sigma_2$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_3$ & $I$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_3$ & $P_1$ & $-1.2072650683$ & $1.09\cdot10^{-3}$\\
$\sigma_3$ & $P_2$ & $-0.8164098576$ & $1.08\cdot10^{-3}$\\
$\sigma_3$ & $P_3$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
\bottomrule
\end{tabular}
\caption{Mean leading coefficients $\overline C_{M,M_B}=\cK c_r\overline\Gamma\ell_0$
and the uniform bound on their relative oscillation in $\theta$.  Values are
certified by interval arithmetic (Appendix~\ref{app:numerics}).}
\label{tab:C}
\end{table}

\begin{corollary}\label{cor:suppressed}
In this protocol the emergent light cone is not operationally sharp for
infrared-admissible operations.  For each pair the response is
non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every $k$.  It is
nevertheless non-zero for all large $N$, with the exact rate $K_*$, the exact
power $13/2$ and an explicit non-vanishing coefficient.
\end{corollary}

\begin{remark}\label{rem:features}
Three features of Table~\ref{tab:C} were not assumed and come out of the
computation.  First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order;
the two encoders differ only at lower orders.  Second, the three Pauli
encoders are not equivalent: with $M_B=I$ they give three different
coefficients.  Third, for $M=\sigma_2$ the two contributing saddles enter with
the same sign for every detector: $\ell_0$ and $\ell_\pi$ of
Appendix~\ref{app:numerics} have the same sign.  Since $\Gamma_+>0$ and
$\Gamma_-\ge0$ (Lemma~\ref{lem:depth}), non-vanishing then follows without
the margin estimate in the proof of Theorem~\ref{thm:main}, so for this
encoder the non-cancellation mechanism is particularly transparent.  The smallest coefficients,
$|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$ with
$M_B\in\{I,P_3\}$.  For these two encoders with $M_B=I$, the diagnostics of
Appendix~\ref{app:numerics} show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.
\end{remark}

\begin{remark}[Methodology]
The protocol (regions, profiles, encoders, detectors, scalings
$\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the encoding angle $\pi/2$) was fixed before
the asymptotic analysis and was not tuned afterwards.  The family of
encoders and detectors is not exhaustive: a general generator
$M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk relating
the directions $\hat n\cdot\sigma$ has been established.
\end{remark}

\section{Proof of the upper bounds}\label{sec:upper}

\subsection{An ellipse lemma}
For $a\ge1$ let
$E_a=\{z\in\C:(\re z)^2/a^2+(\im z)^2/(a^2-1)\le1\}$, where $E_1=[-1,1]$.
These are the confocal ellipses with foci $\pm1$.  The Joukowski map
$\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle $|\lambda|=r\ge1$
onto $\partial E_{(r+r^{-1})/2}$.

\begin{lemma}\label{lem:ellipse}
Let $a,c\ge1$.  If $z\in\partial E_a$ and $w\in E_c$, then $zw\in E_{ac}$;
consequently $E_aE_c\subseteq E_{ac}$.  If moreover $a,c>1$, then
$zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.
\end{lemma}

\begin{proof}
If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and symmetry.  If
$a=1$, then $z\in[-1,1]$ and the same argument applies.  So let $a,c>1$.
Write
$z=a\cos p+i\sqrt{a^2-1}\sin p$ and $w=c\,x+i\sqrt{c^2-1}\,y$ with
$x^2+y^2\le1$.  In the coordinates adapted to $E_{ac}$, the point $zw$
corresponds to $L(x,y)^T$ with
\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]
With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives
\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
\]
Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$.  If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is
interior.  If $u=1$, then $z=\pm a$ and
\[
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
\]
whose second entry is $<1$.  Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$.
\end{proof}

\begin{lemma}\label{lem:specrad}
For $\eta\in\R^3$ and $\xi\in\R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$.  If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.
\end{lemma}

\begin{proof}
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma~\ref{lem:ellipse} applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$.  When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$.  The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$.
If $|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$.  Since the
ellipses are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is
$r\le e^{\Phi(\xi)}$, with strict inequality when $f$ is interior.  On
$\Sigma$, $f=\pm\prod\cosh\xi_j$ is real and equality holds.
\end{proof}

\begin{lemma}[Powers without a gap]\label{lem:schur}
Let $T$ be a $2\times2$ matrix with $\rho(T)\le e^{\varkappa}$ and
$\|T\|\le\beta$.  Then $\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.
\end{lemma}

\begin{proof}
Take a unitary Schur form $T=V\begin{psmallmatrix}\lambda_1&b\\0&\lambda_2\end{psmallmatrix}V^*$,
so $|b|\le\|T\|$.  The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$.  The diagonal part has norm
$\max_j|\lambda_j|^N$.
\end{proof}

\subsection{Proof of Theorem~\ref{thm:upper}}
Since the integrand in \eqref{eq:kernel} is entire and $2\pi$-periodic in
each variable, the contour can be shifted to $p=\eta-i\xi$ for any
$\xi\in\R^3$ without boundary terms:
\begin{equation}\label{eq:tilt}
G_N(d)=e^{-\xi\cdot d}\int_{\T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\end{equation}
Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$.  Lemma~\ref{lem:specrad}
gives
\[
\rho\bigl(S(\eta-itu)\bigr)\le\exp\arcosh(125/64)<4,
\]
because $125/64<17/8=\cosh\log4$.  By Lemma~\ref{lem:jumps},
\[
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
\]
Lemma~\ref{lem:schur}, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$.  With
\eqref{eq:separation},
\[
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
\]
for all $(x,y)\in\cA_N\times\cB_N$.  The Schur test with $|\cA_N|,|\cB_N|\le N^3$
gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$.  Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$.  The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$ on
the one-particle block, together with $-\tr X$ on the vacuum block.  Hence
$D_B=\frac12(|\tr X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
\qed

\subsection{Proof of Theorem~\ref{thm:rate}}
(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$).  The inequality
$\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$, applied twice, gives
$\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.  Since
$\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$.  Finally $I=+\infty$ outside
$\operatorname{conv}F$ by \cite[Lemma~4.1]{CJWW}.  Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with
\[
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
\]
On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$.  It is strictly increasing, since
$3h'(t)=u^T\Hess\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is given by the
formula of Lemma~\ref{lem:symbol}(d) with $c_*$ replaced by $\cosh t>1$.  Since
$\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with $h(t_*)=\alpha$, and
then $\nabla\Phi(\xi_*)=v_*$.  Solving $h(t)=\alpha$ for $\cosh^2t$ gives the
stated closed form.  By the definition of $I$, for every $v$,
\[
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\uhat\cdot v-|v_*|\bigr),
\qquad \uhat=u/\sqrt3 .
\]
On $V_{\mathrm{reg}}$ we have $\uhat\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$.  Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\arcosh(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$.  Along the diagonal,
$3t-\arcosh(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also the exact
vertex rate of Proposition~\ref{prop:geometry}(c).  The numerical values are
enclosed by interval arithmetic.

(d) Apply \eqref{eq:tilt} with $\xi=\xi_*$.  By Lemma~\ref{lem:specrad},
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$.  By
Lemma~\ref{lem:jumps}, $\|S(\eta-i\xi_*)\|\le4e^{3t_*}$.
Lemma~\ref{lem:schur} gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$.  For
$(x,y)\in\cA_N\times\cB_N$, \eqref{eq:separation} and $\xi_*\parallel\uhat$
give $\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and
$N\xi_*\cdot v_*-N\Phi_*=NK_*$.  Numerically $4e^{3t_*-\Phi_*}<9.2$, so
$1+4e^{3t_*-\Phi_*}N\le1+10N$, and the Schur test concludes as before.
\qed

\section{Proof of admissibility}\label{sec:admissible}

\begin{lemma}\label{lem:IR1}
Let $a:\Z^3\to M_2(\C)$ satisfy $\sup\|a\|\le A$ and
$\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$.  Then
\[
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
\]
\end{lemma}

\begin{proof}
Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$.  On the complement of $\Pi'$,
\[
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
\]
using $\sin s\ge2s/\pi$ on $[0,\pi/2]$.  By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$.  For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$.  The
discrete product rule
$D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's inequality give
$(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:admissible}]
\emph{Numerators.}  $|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside
$\cA_N$, and the gradient vanishes on the sphere, so $F_N$ is
$16/N$-Lipschitz on $\Z^3$.  For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$,
because $\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$.  For $E=h_N\otimes M_B$ we get
$A=1$ and $L=16$.  Lemma~\ref{lem:IR1} bounds the numerators by
$K_eN^{-1/2}$ and $K_dN^{-1/2}$.  For $\eta_{\mathrm{enc}}$, write
$v=U_M\phi_N$, $w=\Pi'v$ and $r=v-w=(I-\Pi')a_M\phi_N$.  Since
$\Pi'\phi_N=\phi_N$, $\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$,
whose trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

\emph{Denominators.}  For $|x|\le N$ and $|p|\le N^{-1}$, $\cos(p\cdot x)\ge\frac12$.
Hence $\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$.
Let $N\ge32$, and consider two auxiliary sets.  The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$.  The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$.  Each carries resource
weight at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$.  Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$.  For the detector, test
on the resource translated to $N(1,1,1)$, with internal state a
$+1$ eigenvector of $M_B$.  This test vector lies in $\operatorname{ran}\Pi$,
and it gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle\dn|e^{i\pi F_N(x)M/2}|\dn\rangle$.  This gives $t_x=e^{i\pi F_N/2}$
for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and $e^{-i\pi F_N/2}$ for
$M=\sigma_3$.  Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\re t_x\bar t_y)$.  All terms are non-negative,
and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\re t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$.  Counting both orders
gives $1-|z|^2\ge(2-\sqrt2)m^2$.  For $2\le N<32$ the same argument, with
the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows that the
denominators are non-zero.
\end{proof}

\section{Proof of the leading asymptotics}\label{sec:asymptotics}

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line.  The constants $r_0,c,c_3,c_P$ below are finite
but not made explicit.

\subsection{Reduction to one interference functional}
Let $P_B$ be the restriction to $\cB_N$ (not a spectral projection).  Write
$\widetilde r=S^N\phi_N$ for the free evolution of the resource on all of
$\Z^3$, and put
\[
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N\dn),\qquad
a_\up=P_BS^N(s_N\varphi_N\up),\qquad a_\dn=P_BS^N(s_N\varphi_N\dn).
\]
Since $\sigma_1\dn=\up$, $\sigma_2\dn=-i\up$ and $\sigma_3\dn=-\dn$, Bob's
encoded amplitude $P_B\psi_1$ is $v+ia_\dn$, $v+ia_\up$, $v+a_\up$ or
$v-ia_\dn$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.  Expanding
\eqref{eq:signal} with $E$ supported in $\cB_N$,
\begin{equation}\label{eq:Lexp}
\begin{aligned}
L_{I}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\dn\rangle+Q_I, &
L_{\sigma_3}&=2\re\langle r,Ea_c\rangle+2\im\langle r,Ea_\dn\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\up\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\re\langle r,Ea_c\rangle+2\re\langle r,Ea_\up\rangle+Q_{\sigma_2}.
\end{aligned}
\end{equation}
Each $Q_M$ is a sum of terms quadratic in $(a_c,a_\up,a_\dn)$.  For
example, $Q_I=\langle a_c,Ea_c\rangle+\langle a_\dn,Ea_\dn\rangle-2\im\langle a_c,Ea_\dn\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem~\ref{thm:rate}(d), $a_c,a_\up,a_\dn$ have $\ell^2$-norm at most
$T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$.  The free tail is only polynomially
small (Lemma~\ref{lem:tail}).  The $e^{-K_*N}$ sector therefore consists of
the linear interference terms.  Define, for $\chi\in\{\up,\dn\}$,
\[
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
\]
Theorem~\ref{thm:main} follows from Theorem~\ref{thm:T} below.  The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
because $c_N=\Theta(N^{-4})$ in the relevant layer while $s_N=\Theta(N^{-2})$.

\subsection{Exact tilted representation}
Let $R=N/4$, $x_*=R\uhat$ and $y_*=N u-R\uhat$, so that $y_*-x_*=Nv_*$.  For
$f$ supported in $\cA_N$ and $w$ supported in $\cB_N$, put
\[
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
\]
Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$.  By \eqref{eq:tilt}
with $\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,
\begin{equation}\label{eq:exactrep}
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\end{equation}
This identity is exact: the sums are finite and no poles are crossed.

\subsection{The tilted symbol}\label{ssec:tilted}
\begin{lemma}\label{lem:symbol}
\begin{enumerate}[label=(\alph*)]
\item $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$.  At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,
  \[
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  \]
  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is
  \[
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  \]
\item For all $p\in\C^3$: $S(p+\pi e_1)=-S(p)$, $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
\item The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\Z^3:u_1+u_2+u_3=0\}$ is trivial if and only if
  $\eta_0\in\{0,\pi u\}$.
\item There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and
  \[
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  \]
  Here $Q=\Hess\Phi(\xi_*)=q_t(I-\uhat\uhat^T)+q_n\uhat\uhat^T$ with
  \[
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  \]
\item Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) and (b) are identities between trigonometric polynomials and are checked
by expansion.  (c): $\Lambda_0$ is generated by $e_1-e_2$ and $e_2-e_3$, so
the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$.  (d): the
eigenvalues of $S(\eta-i\xi_*)$ are
$\exp(\pm\arcosh f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$.  Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$.  Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\Hess\Phi(\xi_*)=Q$.  The explicit Hessian is
$\Hess\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$.  The eigenvalues $\lambda^{\pm1}$ are separated
by the gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic.
(e): by Lemma~\ref{lem:specrad} and compactness,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from $\Sigma$.  Conclude with
Lemma~\ref{lem:schur}.
\end{proof}

By (b), near $\pi u$ we have $S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$,
whose Perron projector is $P^T=\overline P$.  The other six points of
$\Sigma$ have the same spectral radius, but by (c) their characters are
non-trivial on the lattice planes $u\cdot x=k$.  This is why only $0$ and
$\pi u$ contribute at leading order (Lemma~\ref{lem:layers}(d)).

\subsection{Lattice-plane coordinates and profiles}
The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a translate
of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.  Write
Alice's sites as $x=x_*-\delta\uhat+u_\perp$ with $u_\perp\perp\uhat$ and
depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$.  Since $u\cdot x\in\Z$,
\[
\sqrt3\,\delta=\theta_N+j,\qquad j\in\Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
\]
Similarly $y=y_*+\delta'\uhat+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$, with
the \emph{same} $\theta_N$.  Then
$\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and $\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$.
Moreover $u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,
\[
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
\]
and therefore
$s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.  The
same holds for $h_N$ with $\delta'$ and $u'_\perp$.  Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

\subsection{The free tail}
\begin{lemma}\label{lem:tail}
Uniformly in $y\in\Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where
\[
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]\dn,
\]
\[
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
\]
At the facing point $w_*=u-\uhat/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\uhat$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in $y\in\cB_N$,
and $r=0$ outside $\cB_N$.
\end{lemma}

\begin{proof}
For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic, and
$H-H_W=O(|p|^2)$.  Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$.  With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$.  The resource enters through $g(Np)$ and is not
truncated.  The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$.  The value of $H_W(\uhat)\dn=(1+i,-1)^T/\sqrt3$ follows
by direct computation.
\end{proof}

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$.  We write
$\varphi_\partial=c_rI_b$.

\subsection{Layer sums}
Let $\Psi_\delta(\tau)=\int_{\R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$.  Define
\[
\cS_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\R^2}e^{-q_t|\tau|^2}\,\cS_\pm(\tau;\theta)^2\,d^2\tau .
\]

\begin{lemma}[Depth sums]\label{lem:depth}
Let $c_g=2\pi/(3\sqrt3)$ and $s_\omega=t_*+i\omega$.  Then
\[
\cS_+=\sum_{n\in\Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\cS_-=\sum_{n\in\Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
\]
Consequently $|\cS_+-\hat g_\tau(0)|\le c_g/720$ and $|\cS_-|\le c_g/48$.
Moreover
\[
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
\]
with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.
\end{lemma}

\begin{proof}
Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$.  So $H'''=2J_0(|\tau|\sqrt\delta)$
and $H(0)=H'(0)=H''(0)=0$.  Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated.  It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\Z)$.  Poisson summation is
therefore exact.  The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$.  The Gaussian integrals are elementary.
\end{proof}

\begin{lemma}[Layers]\label{lem:layers}
Let $\chi\in\{\up,\dn\}$, $f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and
$\tau=\sqrt{N/2}\,\eta_t$, where $\eta=\eta_n\uhat+\eta_t$ with
$\eta_t\perp\uhat$.
\begin{enumerate}[label=(\alph*)]
\item $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
\item For $|\eta|\le r_0$,
  \[
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\cS_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\cS_+(\tau;\theta_N)+\mathcal E_B\bigr],
  \]
  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
\item Near $\pi u$ the same holds with $\cS_-$ in place of $\cS_+$.  The
  alternating sign comes from the parity $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$,
  combined with $S^N\mapsto(-1)^N(S^N)^T$.
\item For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Decompose the sums into lattice planes.  On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$.  The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size $O(N^{-7/2}\delta^2)$.
Planes with $\delta>R/2$ contribute $O(e^{-cN})$.  This gives (a).

For (b), apply Poisson summation on each plane.  The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$.  The
terms $m\ne0$ are bounded by $\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$,
since the profile vanishes quadratically on the rim and its third
derivative is a finite measure.  After the weighted depth sum, they give a
relative error $O(N^{-3/2})$.  In the $m=0$ term, use the profile
expansions, $\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$.  With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,
\[
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
\]
Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$ gives
the prefactor of $\mathfrak A_f$.  For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$, using
Lemma~\ref{lem:tail}, the smoothness of $R_0$ and $M_B^\dagger=M_B$.  (c)
follows from Lemma~\ref{lem:symbol}(b) and the parity identity.  (d): by
Lemma~\ref{lem:symbol}(c), the character is non-trivial on each plane.  The
Poisson sum therefore has no $m=0$ term, and the remaining terms are
$O(N^{-4})$.
\end{proof}

\subsection{Assembly}
\begin{theorem}\label{thm:T}
For $\chi\in\{\up,\dn\}$ and each $M_B$,
\[
\mathcal T_\chi(N)=N^{-13/2}\,\cK\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
\]
where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and
\[
\cK=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
\]
\end{theorem}

\begin{proof}
Insert Lemmas~\ref{lem:symbol} and~\ref{lem:layers} into
\eqref{eq:exactrep}.  Away from the balls $B(\eta_0,r_0)$ the contribution is
$O(Ne^{-cN}N^{-5})$.  The six points of $\Sigma$ with non-trivial
characters give $O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the
Gaussian decay of $\widetilde S_N$.  Near $\eta_0\in\{0,\pi u\}$ we make
three replacements.  First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced
by $e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.  Third,
the integral is extended to $\R^3$, at cost $O(e^{-cNr_0^2})$.  What
remains is
\[
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\R^2}e^{-q_t|\tau|^2}\cS_\pm^2\,d^2\tau .
\]
Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:main}]
By \eqref{eq:Lexp}, the $e^{-K_*N}N^{-13/2}$ sector of $L_{M,M_B}$ is
$\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear functional
$-2\im$ for $M\in\{I,\sigma_1\}$, $+2\im$ for $M=\sigma_3$ and $+2\re$ for
$M=\sigma_2$, and $\chi=\dn$ for $M\in\{I,\sigma_3\}$, $\chi=\up$ for
$M\in\{\sigma_1,\sigma_2\}$.  Since $\cK$, $c_r$ and $\Gamma_\pm$ are real,
Theorem~\ref{thm:T} gives \eqref{eq:C} with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$.  Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in
Appendix~\ref{app:numerics}.

The remainder budget, relative to $N^{-13/2}$, is as follows:
\begin{itemize}
\item $O(N^{-1/2})$ from the cubic term of the exponent, from
  $P(\eta)-P$, from the normal phase, and from the variation of
  $\varphi_N$ and $R_0$ across the layer;
\item $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
\item $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
\item $O(N^{-2})$ from $2\re\langle r,Ea_c\rangle$;
\item exponentially small terms from the region away from $\Sigma$ and from
  the sector $e^{-2K_*N}$.
\end{itemize}
Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$.  For every pair, interval
arithmetic certifies $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$.
Therefore $C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline C-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table~\ref{tab:C}.  Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow.
\end{proof}

\begin{remark}[Counting the power]
The exponent $13/2$ decomposes as follows.  The resource contributes
$\frac32$ at the layer and the free tail $\frac32$ at Bob.  The profiles
$s_N$ and $h_N$ contribute $2+2$.  The two in-plane areas contribute $-2$.
The normal Gaussian contributes $\frac12$, and the tangential rescaling
$d^2\eta_t=(2/N)d^2\tau$ contributes $1$.  The depths $j,j'$ are discrete
sums of size $O(1)$ and contribute no power.  The common tangential
direction $u_\perp+u'_\perp$ is a flat direction of the exponent, because
$\xi_*$ is orthogonal to the planes.  It is confined by the profiles and
produces the area factors, not a Gaussian factor.
\end{remark}

\begin{remark}[Dependence on $\theta_N$]
Since $\sqrt3/4\notin\mathbb Q$, the sequence $\theta_N$ is equidistributed.
$C(\theta_N)$ is therefore quasi-periodic in $N$ and not a constant.  The
oscillation comes from the commensurability of the lattice planes with the
spheres bounding the regions.  It is below $0.15\%$, and it never changes
the sign.
\end{remark}

\section{Discussion}\label{sec:discussion}

\subsection{What the theorem says and does not say}
The theorem is a statement about one walk and one explicitly specified
family of operations.  It shows that the gap between the emergent
relativistic cone and the microscopic causal support is not merely
geometric.  Under an infrared-controlled protocol it carries an
operational response whose asymptotic law is known exactly: rate, power
and coefficient.  It does not claim that $D_B>0$ for every protocol, that
every quantum walk behaves this way, or that every smooth encoder
$M=aI+b\cdot\sigma$ signals.  It is not a violation of the model's
microcausality, since Bob remains inside $N\Cmicro$.  The limit
$N\to\infty$ is an infrared scaling at fixed lattice units, not a continuum
limit $a,\tau\to0$.

The result is asymptotic.  The remainder constants and $N_*$ are finite but
not explicit.  The finite-$N$ diagnostics of Appendix~\ref{app:numerics}
indicate an effective relative correction of about $-100/N$.  The leading
formula is therefore quantitatively reliable only for $N\gtrsim10^3$.  For
$M\in\{I,\sigma_3\}$ with $M_B=I$, whose coefficient is among the smallest,
the $N^{-17/2}$ term dominates over the whole diagnostic range.

\subsection{Physical reading}
Restoring a lattice spacing $a$, the integer $N$ is both the number of
steps and the separation scale in lattice units, so $N\sim\ell/a$ for a
separation $\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors.  The
response is therefore negligible at any separation large compared with the
lattice spacing, and by the preceding subsection the leading formula becomes
accurate only for $N\gtrsim10^3$.  We make no claim about observability, and
regard the result as a statement in the mathematical physics of finite-range
unitary dynamics.
Its interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $\cIR$, and operational influence,
which does not vanish inside the corona even under infrared control.

\subsection{Open problems}
\begin{enumerate}[label=(\arabic*)]
\item General encoders $M=aI+b\cdot\sigma$, and optimisation over
  admissible operations.
\item Other walks, in particular the Bialynicki-Birula walk
  \cite[Eq.~(5.12)]{CJWW}, whose corona contains ballistic modes faster than
  $\cIR$, and the massive Dirac case.
\item Explicit remainder constants and $N_*$, which would make the
  statement effective at finite $N$.
\item Many-particle and second-quantized versions.  The upper bound
  extends to even local unitaries on the full CAR algebra, with prefactor
  $288N^7$ in place of $36N^4$~\cite{Repo}, but no lower bound is available
  there.
\end{enumerate}

\appendix

\section{Computer-assisted parts and diagnostics}\label{app:numerics}

Theorem~\ref{thm:upper}, together with Lemma~\ref{lem:ellipse}, is
formally verified in Lean~4/Mathlib (\texttt{formal/} in~\cite{Repo}).  The
asymptotic results (Theorems~\ref{thm:rate} and~\ref{thm:main}) are not.
The analytic arguments above are complete up to the following verified
computations.  All of them are performed by the certificate scripts listed
in~\cite{Repo}, at the commit given there, with Python~3.12.3, SymPy~1.14.0
and mpmath~1.3.0.  Exact identities use SymPy.  Enclosures use the interval
context \texttt{mpmath.iv} with 50 digits, and only its elementary
operations: the four arithmetic operations, integer powers by repeated
multiplication, $\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$.
No interval quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$
and $I_b$ are enclosed through exact closed forms in $\sin$ and $\cos$,
obtained from the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$,
which are checked symbolically.
\begin{itemize}
\item The symbol identities: Lemma~\ref{lem:jumps}, \eqref{eq:SOS}, and
  Lemma~\ref{lem:symbol}(a)--(b).  Also the ellipse-lemma polynomials,
  $\cosh^3(\log2)=125/64$ and the vertex blocks.
\item Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$,
  $q_t$, $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$, $\cK$,
  $\overline\Gamma$ and $\varepsilon_\pm$.
\item The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table~\ref{tab:C}, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.
\end{itemize}
Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$.  The rows for
$\sigma_3$ are the negatives of the rows for $I$.

{\small
\[
\begin{array}{lll}
\toprule
(M,M_B) & \ell_0 & \ell_\pi\\
\midrule
(I,I),(I,P_3) & -\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2} & +\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}\\[3pt]
(I,P_1) & \frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2} & -\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}\\[3pt]
(I,P_2) & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2} & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}\\[3pt]
(\sigma_1,I) & -\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c} & \frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}\\[3pt]
(\sigma_1,P_1) & -\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2} & \frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_2) & -\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2} & -\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_3),(\sigma_2,P_3) & -\frac{\sqrt3}{3}B(1-\alpha) & -\frac{\sqrt3}{3}B(1-\alpha)\\[3pt]
(\sigma_2,I) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}\\[3pt]
(\sigma_2,P_1) & -\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2} & -\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}\\[3pt]
(\sigma_2,P_2) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}\\
\bottomrule
\end{array}
\]
}

\medskip\noindent\emph{Finite-$N$ diagnostics.}  These are floating-point
and not used in any proof; they use NumPy~1.26.4 and are produced by the
\texttt{--diagnostics} option of the coefficient certificate~\cite{Repo}.  A
floating-point FFT evaluation of the exact discrete convolution formula in
tilted variables (``brute'') was compared with a reference that keeps the
exact lattice geometry but replaces the kernel by its Gaussian form at the
eight points of $\Sigma$.  Their ratio tends to $1$ with deviation of order
$c/N$, $c\in[-0.5,14]$, at $N=24,40,56$.  For $M\in\{I,\sigma_3\}$ and
$M_B=I$, the ratio of the $N^{-17/2}$ piece $2\re\langle r,Ea_c\rangle$ to
the piece $2\im\langle r,Ea_\dn\rangle$ that carries the $N^{-13/2}$ term is
$15.2$, $9.4$ and $6.4$ at $N=24,40,56$.  A semi-analytic evaluation with discrete
planes and exact profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at
$N=10^3$, $10^4$ and $3\cdot10^4$, consistent with a relative correction
$\approx-100/N$.  The free tail agrees with $N^{-3/2}R_0$ to relative
accuracy $2\cdot10^{-6}$ at $N=40$ and $8\cdot10^{-9}$ at $N=640$.

\begin{thebibliography}{99}

\bibitem{AVWW}
A.~Ahlbrecht, H.~Vogts, A.~H.~Werner, R.~F.~Werner,
\emph{Asymptotic evolution of quantum walks with random coin},
arXiv:1009.2019.

\bibitem{Arrighi}
P.~Arrighi,
\emph{An overview of quantum cellular automata},
arXiv:1904.12956.

\bibitem{BBBP}
Y.~Baryshnikov, W.~Brady, A.~Bressler, R.~Pemantle,
\emph{Two-dimensional quantum random walk},
J.\ Stat.\ Phys.\ \textbf{142}, 78--107 (2011), arXiv:0810.5495.

\bibitem{BialynickiBirula}
I.~Bialynicki-Birula,
\emph{Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata},
Phys.\ Rev.\ D \textbf{49}, 6920 (1994), arXiv:hep-th/9304070.

\bibitem{BDPT}
A.~Bisio, G.~M.~D'Ariano, P.~Perinotti, A.~Tosini,
\emph{Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata},
arXiv:1601.04832.

\bibitem{BHS}
L.~Bombelli, J.~Henson, R.~D.~Sorkin,
\emph{Discreteness without symmetry breaking: a theorem},
arXiv:gr-qc/0605006.

\bibitem{BHV}
S.~Bravyi, M.~B.~Hastings, F.~Verstraete,
\emph{Lieb--Robinson bounds and the generation of correlations and topological quantum order},
Phys.\ Rev.\ Lett.\ \textbf{97}, 050401 (2006), arXiv:quant-ph/0603121.

\bibitem{CRT}
H.~A.~Carteret, B.~Richmond, N.~M.~Temme,
\emph{Evanescence in coined quantum walks},
J.\ Phys.\ A: Math.\ Gen.\ \textbf{38}, 8641--8665 (2005), arXiv:quant-ph/0506048.

\bibitem{CJWW}
C.~Cedzich, A.~Joye, A.~H.~Werner, R.~F.~Werner,
\emph{Exponential tail estimates for quantum lattice dynamics},
Ann.\ Henri Poincar\'e \textbf{27}, 2843--2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.

\bibitem{DArianoErbaPerinotti}
G.~M.~D'Ariano, M.~Erba, P.~Perinotti,
\emph{Isotropic quantum walks on lattices and the Weyl equation},
Phys.\ Rev.\ A \textbf{96}, 062101 (2017), arXiv:1708.00826.

\bibitem{DArianoPerinotti}
G.~M.~D'Ariano, P.~Perinotti,
\emph{Derivation of the Dirac equation from principles of information processing},
Phys.\ Rev.\ A \textbf{90}, 062106 (2014), arXiv:1306.1934.

\bibitem{Farrelly}
T.~Farrelly,
\emph{A review of quantum cellular automata},
Quantum \textbf{4}, 368 (2020), arXiv:1904.13318.

\bibitem{GJS}
G.~Grimmett, S.~Janson, P.~F.~Scudo,
\emph{Weak limits for quantum random walks},
Phys.\ Rev.\ E \textbf{69}, 026119 (2004), arXiv:quant-ph/0309135.

\bibitem{Konno}
N.~Konno,
\emph{Quantum random walks in one dimension},
Quantum Inf.\ Process.\ \textbf{1}, 345--354 (2002).

\bibitem{LiebRobinson}
E.~H.~Lieb, D.~W.~Robinson,
\emph{The finite group velocity of quantum spin systems},
Commun.\ Math.\ Phys.\ \textbf{28}, 251--257 (1972).

\bibitem{ACSV}
R.~Pemantle, M.~C.~Wilson, S.~Melczer,
\emph{Analytic Combinatorics in Several Variables}, 2nd ed.,
Cambridge University Press (2024), doi:10.1017/9781108874144.

\bibitem{Repo}
Repository \texttt{nacho09021973/qca-causal-cones},
% TODO(author): replace by an archived release (tag and DOI) before submission.
\url{https://github.com/nacho09021973/qca-causal-cones}, commit
\texttt{551addabe28b} (branch \texttt{research/b-infinity-post-s4-gate}).
Certificates
\texttt{scripts/verify\_scaled\_ir\_gate.py},
\texttt{scripts/verify\_regional\_directional\_asymptotics\_gate.py},
\texttt{scripts/verify\_regional\_laplace\_coefficient\_gate.py},
\texttt{scripts/verify\_directional\_saturation.py}; Lean formalization in
\texttt{formal/}.

\bibitem{SchumacherWerner}
B.~Schumacher, R.~F.~Werner,
\emph{Reversible quantum cellular automata},
arXiv:quant-ph/0405174.

\bibitem{SunadaTate}
T.~Sunada, T.~Tate,
\emph{Asymptotic behavior of quantum walks on the line},
J.\ Funct.\ Anal.\ \textbf{262}, 2608--2645 (2012), arXiv:1108.1878.

\end{thebibliography}

\end{document}
```

### Contexto adjunto: state/CURRENT_STATE.md
```
# CURRENT_STATE

**Date:** 2026-09-24
**Status:** STANDARD WEYL/DIRAC EXACT GATE: PASS; strong `B_infty^*` REJECTED IN DECLARED s=4 CLASS; point-(3) ceiling PROVED UNDER FROZEN CONTRACT, one independent review PASS; flat CJWW (5.15) operational IR-corona result CLOSED in its frozen class; **H1-only extension: TWO_DISTINGUISHABLE_CHANNELS frozen by explicit model assumption** (Sec. 9.6): H1c-0a CLOSED, H1c-0b FIXED_BY_EXPLICIT_ASSUMPTION, primary observable `(L_+, L_-)`; physical realization/justification OPEN; Volterra/asymptotic localization PAUSED. H1-SR proved under frozen beta contract, H1a/H1b proof written/unreviewed, layer absolute-mass bound PASS, G-insertion and final-Q-leakage PASS_IN_LOCAL_WINDOW retain their prior scope; H1c localization and H1 remain unproved/OPEN. Exploratory sequence: T1 `PASS` with independent adversarial review for the frozen model and admissible fixed W; T2 `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`; T3 `STOPPED_NO_SIGNED_TERM`. Physical reconstruction norm audit: `PRELIMINARY: BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM`, conditional on the unreviewed Schur block-stability estimates; the operator norm bound is direct, but vector/piece bounds are not independently reviewed. No `E_6` or dominance claim. See Sec. 9.7. No H1/H1c promotion. E0 and POWER_13/2_STABILITY remain OPEN_AT_STOP; E/AdS remains STOPPED_UNPROVEN. IR spectral-attribution front (Sec. 10.1): C1 PASS, C2a PASS for sigma2/I (one independent agent review), C2b PASS for sigma2/I (B4_PRIME_PASS separately; one independent agent review), C2c structural scope C2C_PASS for the frozen 16-pair scope, C3 conditioning C3_PASS for the frozen four-encoder `M_B=I` scope.

**Branch-local state.** This file is reconciled on
`research/b-infinity-post-s4-gate` only, so that it agrees with all evidence
merged on this branch. It is **not** a canonical promotion: `main` is
unchanged, and promotion requires a separate explicit decision.

**Repository:** `nacho09021973/qca-causal-cones`

**Evidence baseline:** `2c7c2c9433e5817763fbeb8e400580f54a9dbeb0`.
Canonical promotion is recorded in
[`2026-09-14--standard-gate-promotion.md`](../reports/2026-09-14--standard-gate-promotion.md).
**Only point (3), the strict-cone ceiling, is chartered and authorized by
direct user instruction** (Sec. 7.2). The full C gate is not ratified.

**Correction (2026-09-14):** `B*` as a comparison against the one-step
inradius `r_in(C_micro)` is superseded by `B_infty^*`, a comparison against
the strict asymptotic isotropic speed `c_strict^iso`. See
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) and
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0. New baseline-specific certificate: for the
standard Pavia Weyl family in d=3, `C_infty^strict = C_micro` exactly, so
`c_strict^iso = r_in(C_micro) = 1/sqrt(3)`; see
[`2026-09-14--strict-asymptotic-pavia-baseline.md`](../reports/2026-09-14--strict-asymptotic-pavia-baseline.md).
This baseline-specific certificate did not by itself close the gate; the
later s=4 counterexample completed it for the declared s=4 class.

**Integration (2026-09-15, branch-local):** an explicit irreducible `s=4`
family on the same `N_3`, with the same `D2` action, has
`C_infty^strict = C_micro` and `c_strict^iso = 1/sqrt(3)`, but
`c_0(a) = a/sqrt(3)` for every `0 < a < 1`. This is `COUNTEREXAMPLE_VERIFIED`
in the sense of the
[gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) Sec. 5 for the
declared `s=4` class (Sec. 4.1 below). It does not refute the standard Pavia
`s=2` certificate above. Evidence:
[analytic note](../theory/S4_STRICT_CONE_COUNTEREXAMPLE.md) and
[freeze record](../reports/2026-09-15--s4-strict-cone-counterexample-freeze.md)
(`1dae941`), [independent review](../reports/2026-09-15--s4-independent-review.md)
(`aeec462`), [prior-art audit](../reports/2026-09-15--s4-family-prior-art-audit.md)
(`f74018f`). **NOVELTY = OPEN.**

## 1. Purpose

The project asks whether the relativistic propagation speed seen in the low-energy effective theory of a finite-range QCA is determined by the causal geometry of the microscopic substrate.

The original slogan — “`c` is the maximum speed of the substrate” — has been split into precise statements. Its literal strong form does **not** survive generically in finite-range lattice QCA for spatial dimension `d >= 2`.

## 2. Frozen objects

Let the one-step displacement set be `N` (dimensionless lattice displacements unless scale is explicitly restored).

### Microscopic causal body

`C_micro := conv(N)`.

With lattice spacing `a` and time step `Δt`, physical velocities are obtained by the corresponding scale factor.

For a unit vector `n̂`, define the support function

`h_C(n̂) := sup_{v in C_micro} n̂·v`.

Define

`r_in(C_micro) := min_{||n̂||=1} h_C(n̂)`

and

`V_causal^max := max_{||n̂||=1} h_C(n̂)`.

### Spectral propagation

For Bloch eigenphases `exp[-i ω_s(k) Δt]`, define

`V_grp^max := sup_{s,k} ||∇_k ω_s(k)||`.

In one dimension, finite range and unitarity give the classical Bernstein-type bound

`V_grp^max <= r a / Δt`.

In more than one dimension the correct primitive object is directional support, not a single scalar causal speed.

### Relativistic low-energy speed

`c_IR` is the speed parameter of the relativistic effective theory.

- For a gapless branch, it may be read from the linear slope at the relevant low-energy node.
- For a massive relativistic sector, `|∇ω(0)| = 0`, so `c_IR` must be read from the low-energy Hamiltonian/EFT structure, not from the slope at the origin.
- At finite lattice mass, the spatial coefficient of the interpolating Hamiltonian and the coefficient inferred only from the `k^2` term of `ω^2` need not coincide exactly because lattice corrections contribute at the same order.
- In the verified standard Dirac couplings they differ for every `0 < m < 1`.
  Name the extraction `c_H` or `c_{ω^2}`; do not use an unspecified finite-lattice
  `c_IR` as though those coefficients were interchangeable.

## 3. Established status

### 3.1 Bernstein

**Status: CLASSICAL / NOT NOVEL**

Bernstein gives a clean route from finite Fourier/Laurent range to a derivative bound. The scalar equality theory is prior art. It is background, not the main project claim.

### 3.2 Three distinct levels

**Status: FROZEN**

Do not identify:

`C_micro`, `V_grp^max`, and `c_IR`.

### 3.3 Old strong hypotheses

Define:

- `B_max`: `c_IR = V_causal^max`;
- `B_full`: the isotropic IR velocity ball equals `C_micro`;
- `B_touch`: the isotropic IR ball is tangent to `∂C_micro`.

For an isotropic IR ball contained in a convex microscopic causal body,

`c_IR <= r_in(C_micro) = min h_C <= max h_C = V_causal^max`.

If `C_micro` is anisotropic, then `min h_C < max h_C`, hence `B_max` is impossible.

For a finite-range lattice QCA in `d >= 2`, `C_micro` is a polytope. A nondegenerate Euclidean ball is not a polytope, so exact `B_full` is impossible.

`B_touch` is weaker and is equivalent to the candidate equality

`c_IR = r_in(C_micro)`

when the IR cone is isotropic and centered in the same velocity coordinates.

Therefore:

- `B_max`: **REJECTED generically for anisotropic finite-range lattice QCA in d >= 2**;
- `B_full`: **GEOMETRICALLY IMPOSSIBLE for exact isotropic IR ball vs finite polytope in d >= 2**;
- `B_touch`: **NOT equivalent to “c is the maximum substrate speed”**.

## 4. Canonical hypothesis status

### A — IR universality

Why do distinct low-energy species share the same effective relativistic cone/speed?

**Status: OPEN**

### B_infty^* — strict asymptotic matching (supersedes B* / inradius matching)

Candidate:

`c_0 = c_strict^iso`, `c_strict^iso = min_{n̂} h_infty(n̂)`,

with `h_infty` the strict asymptotic support function of
[`CAUSAL_BODY_GEOMETRY.md`](../theory/CAUSAL_BODY_GEOMETRY.md) Sec. 6.
Interpretation: `c` would match the exact long-run isotropic propagation
speed of the same dynamics, not necessarily the inradius of the one-step
body `C_micro` — the two satisfy `c_strict^iso <= r_in(C_micro)` in general,
with equality only where separately certified (see the d=3 row below).

| Claim | Status and scope |
| --- | --- |
| A — IR universality | **OPEN** |
| B_max | **REJECTED** under isotropic containment in an anisotropic causal body, d >= 2 |
| B_full | **REJECTED / GEOMETRICALLY IMPOSSIBLE** for a nondegenerate isotropic ball equaling a finite lattice polytope, d >= 2 |
| Exact finite-mass B* | **REJECTED IN STANDARD DIRAC FAMILY**, for both specified extractions, every 0 < m < 1 (comparison against `r_in(C_micro)`, unaffected by the B_infty^* correction) |
| B*_0 (linear order, `c_0=r_in`) | **VERIFIED FOR STANDARD WEYL FAMILY / GENERALITY OPEN** |
| B*_cont | **VERIFIED FOR STANDARD DIRAC COUPLINGS / GENERALITY OPEN** |
| B_infty^*, d=3 Pavia baseline (`C_infty^strict=C_micro`, full nonlinear order) | **CERTIFIED for the standard Weyl family `A+,B+,A-,B-`** (`s=2`): `c_0 = c_strict^iso = 1/sqrt(3)`; d=1,2 not checked; unaffected by the s=4 result |
| Strong B_infty^* (`c_0 = c_strict^iso` forced by locality, unitarity, homogeneity and D2 covariance at fixed `N_3`) | **REJECTED IN DECLARED s=4 CLASS** — explicit counterexample, Sec. 4.1; false for any class containing that family |
| B_infty^* in the published minimal `s=2` class (P17, including its Eq. (2)) | **NOT REFUTED by the s=4 result; rigidity OPEN as an in-repo claim.** Origin-node inradius matching there is a conditional application of P17's classification plus the standard certificate, not a new theorem. The strict-body certificate is recorded for `A+,B+,A-,B-`; its transfer across all of P17's equivalences is not separately checked |
| B_infty^* for `s=2` without P17 Eq. (2), or with an irreducible internal symmetry representation `R` for `s>2` | **OPEN** |
| Novelty of the s=4 family and its strict-support statement | **OPEN** — no equivalent found in eleven checked primary sources; not a novelty certificate |

The restricted statements are established for the declared cases below.
There is no general rigidity theorem, proof of A, or novelty claim.

### 4.1 Declared s=4 counterexample class

**Status: COUNTEREXAMPLE_VERIFIED for this class; independent review PASS;
NOVELTY = OPEN.**

| Item | Declaration |
| --- | --- |
| Geometry | d=3, `N_3 = {(+/-1,+/-1,+/-1)/sqrt(3)}`, all eight modes active, no on-site coefficient, one complete update per time unit, phase `exp(-i k.h)` |
| Internal space | `s=4 = C^2_sigma (x) C^2_tau`; parameter `0<a<1`, `b=sqrt(1-a^2)` |
| Symbol | `A_a(k) = W exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)`, `q_i=k_i/sqrt(3)`, `W = I (x) exp(-i pi tau_z/4)` |
| Isotropy | D2 half-turns acting on `N_3`; `R_i = sigma_i (x) I_2` — two copies of the Pauli projective class, hence a **reducible** representation; full cubic symmetry not assumed |
| Irreducibility | Dynamics irreducible: scalar joint commutant of all eight Fourier coefficients |
| Gapless sector | `k=0`; two isolated rank-two clusters at quasienergies `+/-theta`, `theta=pi/4`; isotropic, untilted cones measured from each cluster's node |
| Result | `C_infty^strict = C_micro` exactly (all vertex traces nonzero, so no vertex coefficient is nilpotent); `c_strict^iso = 1/sqrt(3)`; `c_0(a) = a/sqrt(3)` |
| Coverage | One particular product ansatz, not a classification of four-component walks |

Scope limits, all retained:

- **Procedure.** The class table above was written at the freeze and review,
  after the construction, not before solving as charter Sec. 2 requires. This
  limits which classes the example speaks to; it does not affect the
  mathematical validity of the certified inequality.
- **Strict means exact support.** Vertex amplitudes may decay exponentially.
  No ballistic, essential or Lieb-Robinson front statement is made.
- **Floquet-shifted nodes.** `A(0) = W` is not a global phase.
- **Family identity only.** For `0<theta<pi/2`,
  `c_0^2 + 2 sin^2(Delta eps/2) g_ii(0) = 1/3`, where `Delta eps = 2 theta`
  and `g` is the projector quantum metric. It comes from the
  intra/inter-sector split `a^2 + b^2 = 1` of the involutions `Gamma_i`.
  Equating `1/3` with `(c_strict^iso)^2` additionally needs vertex survival,
  which is certified at `theta=pi/4`, or, for fixed `a`, on an open
  neighbourhood where all vertex traces remain nonzero. This is not a
  general QCA theorem.
- **Prior art.** Product-of-projector walks (MB18, BM25), four-component Weyl
  mixing (BB94), shifted Floquet Weyl nodes, adjustable continuum velocity,
  and involution block completion (AF16/17) are antecedents and must be
  attributed. Raynal's explicit s=4 Dirac family is excluded as an
  identification. The most useful open equivalence check is AF16/17's
  homogeneous paired-walk specialization.
- **Certificates.** `scripts/cert_Aa_s4_counterexample.py` and
  `scripts/review_Aa_s4_exact.py` both return PASS (SymPy 1.14.0, zero
  tolerance), and `scripts/verify_weyl_dirac_gate.py` still returns PASS
  (375 checks), on this branch.

## 5. Completed standard Weyl/Dirac exact gate

**Status: PASS — 247 exact checks, zero tolerance, specific negative controls.**

Evidence is the committed
[contract](../reports/2026-09-14--weyl-dirac-gate-contract.md),
[analytic derivation](../reports/2026-09-14--weyl-dirac-exact-gate.md),
[verification record](../reports/2026-09-14--weyl-dirac-verification.md), and
[permanent verifier](../scripts/verify_weyl_dirac_gate.py) at `2c7c2c9`.
Source provenance and the published sign/dagger issues are recorded there.
The analytic proof establishes the open mass interval and continuum scaling;
the check count alone is not their justification or a formal proof certificate.

### Declared family and coordinates

The cases are d=1 A; d=2 A, B; d=3 A+, B+, A-, B-, with the standard d=2
on-site rotation parameter fixed to zero. The d=1 Dirac reduction also covers
the minimal two-component blocks. The seven symbols are not seven independent
geometries: transposes/chiralities within a dimension share support, inradius
and linear speed. There are three dimension-specific geometries in this battery.

Use Cartesian Euclidean coordinates dual to unit-length neighbors and one
complete update per time unit:

`N_d = {(+/-1, ..., +/-1)/sqrt(d)}`,

`C_micro = [-1/sqrt(d), 1/sqrt(d)]^d`,

`r_in = 1/sqrt(d)`, `V_causal^max = 1`.

### Massless equality

For d=1,2,3 in this family, at the declared zero node,

`m = 0: c_0 = r_in = 1/sqrt(d)` — **EXACT**.

This is equality of the linear IR coefficient, not exact finite-momentum
relativistic dispersion or a theorem about every admissible symbol.

### Fixed nonzero lattice mass

For `U_k = [[n A_k, i m I], [i m I, n A_k^†]]`,
`0 < m < 1`, `n = sqrt(1-m^2)`, use `U = exp(-i H)` and the logarithm branch
continuous from the identity near the massless zero node. Then

`cos ω_D(k) = n cos θ(k)`, `M = ω_D(0) = arcsin(m)`,

`F(m) = arcsin(m) sqrt(1-m^2) / m = M cot M`, with `0 < F < 1`,

`c_H = r_in F < c_{ω^2} = r_in sqrt(F) < r_in` — **EXACT**.

Exact finite-mass B* is refuted in the standard family under either extraction.
This result is no longer PRELIMINARY.

The quadratic mass-direction Hamiltonian term `b |k|^2 β` reconciles the two
expansions: `b = r_in^2 n (1-F)/(2m)` and
`c_H^2 + 2 M b = c_{ω^2}^2`. Their discrepancy is a lattice correction,
not a failure of the exact spectrum or an inconsistent calculation.

The endpoint m=1 is separate: actual hopping vanishes, active support becomes
`{0}`, and its inradius and spatial coefficients are zero. It is not covered
by the strict inequalities for `0 < m < 1`.

### Small-mass / continuum matching

For each standard coupling in d=1,2,3,

`lim_{m -> 0+} c_H(m) = lim_{m -> 0+} c_{ω^2}(m) = r_in`.

**VERIFIED FOR STANDARD DIRAC COUPLINGS.** Matching is asymptotic in m;
the equality of the limits is established analytically. The joint scaling
of momentum, dimensionless mass, neighbor length and time step is specified
in the report. Its continuum statement is local at fixed rescaled momentum
and mass, not a full propagator convergence theorem on arbitrary states.

## 6. Current scientific interpretation

**Superseded as the active line by Sec. 8 (2026-09-16).** This section records
the `B_infty^*` reading of the project and remains valid where proved, but its
scalar summaries must be read under the scope correction in Sec. 8.6.

The live idea is no longer:

`c = maximum microscopic speed`,

nor, unqualified, `c_massless = r_in(C_micro)`. The corrected comparison is
`B_infty^*`: `c_0 = c_strict^iso`, the exact strict asymptotic isotropic
speed of the same dynamics (Sec. 4). Its strong form is rejected in the
declared s=4 class (update below). `r_in(C_micro)` remains a provable
upper bound (`c_strict^iso <= r_in(C_micro)`), and is known to be exactly
attained — `c_strict^iso = r_in(C_micro)` — for the standard Pavia Weyl
family in d=3, by an explicit vertex non-nilpotency certificate, not merely
by the linear-order Taylor coefficient.

**Update (2026-09-15, branch-local).** Locality, unitarity, homogeneity and
D2 covariance at fixed `N_3` do **not** force `c_0 = c_strict^iso` once the
internal dimension is enlarged. The s=4 family (Sec. 4.1) keeps the whole
strict body, `C_infty^strict = C_micro`, while its Weyl slope varies
continuously below `1/sqrt(3)`. The strict causal body alone therefore does
not fix the Weyl speed. In this family the missing speed is exactly
accounted for by the inter-sector part of the involutions (the family
identity in Sec. 4.1). Whether that is a structural principle or a feature of
this ansatz is **OPEN**.

What remains unknown is which additional hypotheses restore matching: `s=2`
minimality with or without P17 Eq. (2), irreducibility of the internal
symmetry representation, a whole-symbol common cone, or something else.
Whether `c_strict^iso` saturates `r_in(C_micro)` for every admissible symbol
(saturation, charter Sec. 0(ii)) is a separate question and also remains
open.

At finite mass the two natural extraction procedures differ exactly. A common
relativistic coefficient is recovered in the specified continuum limit.
Additional equivalent representatives cannot resolve the open generality issue;
any successor gate must examine structural freedom under fixed causal geometry
and discrete isotropy.

**Update (2026-09-17, branch-local, frozen class of Sec. 8 only).**
`B_infty^*` matching in Sec. 4 is unchanged. What is now closed is the
**operational IR question** on the preregistered CJWW (5.15) protocol of
Secs. 8.16–8.20, not the matching hypothesis. In that class there is an
IR-controlled operational response outside the emergent cone, and it is
not a mere UV-propagator artefact:

`c_IR < v_micro` (already geometric for (5.15)) and
`IR probe → δ_B(N) ≠ 0` for large `N`, with
`δ_{M,M_B}(N) ∼ |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N}`
on the twelve Pauli pairs (Sec. 8.20). The signal is
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. This is theoretical step 3
of the physical line, closed inside the preregistered class. It is not
`D_B > 0` for every QCA, not a claim about nature, and not a further
signalling calculation. The authorized next front is Sec. 8.21.

## 7. GATE STATUS — only point (3) authorized by the user

**MASSLESS INRADIUS RIGIDITY GATE — COUNTEREXAMPLE_VERIFIED IN DECLARED s=4
CLASS (branch-local); s=2 and irreducible-R classes OPEN; point (3) ceiling
investigation separately chartered by direct user instruction.**
(Charter name kept for continuity; its comparison target is corrected, see
[`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md)
Sec. 0.) Where the charter or
[`B_STAR_HYPOTHESIS.md`](../theory/B_STAR_HYPOTHESIS.md) still describe the
gate as having no counterexample, this section overrides them
(`PROJECT_INSTRUCTIONS.md` Sec. 2).

### 7.1 Superseded operative plan

The 2026-09-14 deliberation
([`debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md`](../debates/2026-09-14--1711--siguiente-paso-b-infinito-rigidez-vs-saturacion.md))
predates the s=4 result. It recommended freezing an `s=2` contract on `N_3`,
filtering candidates by non-nilpotent vertices, and escalating to `s>2` only
after exhausting that class. That order was not followed, and its
"rigidity vs saturation" framing cannot continue as written. It is kept as
historical decision material, not as a current plan. Its open point about
whether P17 Eq. (2) is derivable from the charter's identities still matters
for the `s=2` question.

### 7.2 Point (3) — direct user authorization, not a ratification

**Authorization (2026-09-16):** after the incomplete ratification, the user
explicitly instructed: "pues adelante, punto (3)". Accordingly,
`STRICT_CONE_CEILING_N3 = AUTHORIZED_BY_DIRECT_USER_INSTRUCTION` under the
[frozen point-(3) contract](../theory/STRICT_CONE_CEILING_N3_GATE.md).
Its sole target is `c_0 <= c_strict^iso` in all directions, including
degenerate Floquet nodes and eigenvalue collisions in U^n. The contract
was frozen at `4135625` with initial scientific status **OPEN**. No L1,
defect-metric or other C step is authorized by this instruction.

**Point-(3) result (2026-09-16):**
`PROOF_COMPLETE_ONE_INDEPENDENT_ADVERSARIAL_REVIEW_PASS`;
`THEOREM_STATUS = PROVED_UNDER_FROZEN_CONTRACT`. The
[analytic report](../reports/2026-09-16--point-3-strict-cone-ceiling.md)
supplies a matrix-polynomial boundary bound, compression to the original
eigenspace, a direct directional-slope argument, and the exact support
limit. The author's assessment is `PASS_ANALYTIC` under the frozen
contract. The [independent adversarial review](../informe_adversarial_punto_3.md)
at `bd44122`, reviewing `db083af` against `4135625`, records
`ACCEPT_AS_WRITTEN`, with no mandatory repairs. One independent review is
complete; it is not a five-member ratification. The follow-up incorporates
its recommended sign control and expository clarifications without changing
the frozen quantifiers. The bound is proved for the admitted cones and the
exact support of the full symbol on N3, including degenerate Floquet nodes
and collisions of eigenvalues after taking powers. It does not establish a
sector-intrinsic or ballistic bound, or an extension to incommensurable
displacement sets. No numerical search or scientific script was run.
The full C gate is neither ratified nor closed;
L1 remains a manual candidate and the defect identity remains family-only.
The s=4 example refutes equality and is consistent with this ceiling.
**NOVELTY = OPEN.**

The 2026-09-16 ratification attempt is `ABORTED_OR_INCOMPLETE`: Gemini was
absent at launch; the process was interrupted without a final verdict. Three
first-round turns completed — ASTRA `PREFER_A`, CLAUDE OPUS `RATIFY_C`
conditioned on its own amendment (i), CIRO `RATIFY_C` — and ABNER's turn was
sent but never returned. That is neither a closed round nor five-member
ratification, so the status above is unchanged. The partial acta is archived
at [`2026-09-16--ratificacion-gate-completitud-axial-n3.md`](../debates/2026-09-16--ratificacion-gate-completitud-axial-n3.md);
the raw session log stays local and unversioned.

**Candidate from a degraded debate (2026-09-15):**
`GATE_COMPLETITUD_AXIAL_N3 = CANDIDATE_FROM_DEGRADED_DEBATE`, **not
authorized.** In the
[deliberation](../debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.md),
four members proposed `AUTHORIZE_C`. The tool classified the run as
`DEGRADED_NO_CONSENSUS`: ASTRA failed two turns (Codex usage limit) and was
excluded. ASTRA's recorded preference was A, and its objection that C reaches
`c_strict^iso` only through the still unproven bound `c_0 <= c_strict^iso`
was left unanswered. The earlier requirement of five-member ratification
has not been met. The later direct user instruction above authorizes only
point (3) under a separate contract; it does not authorize the full C gate
or convert either incomplete debate into consensus.

Research directions (only the point-(3) ceiling is now frozen):

1. **Surviving bounds.** Which inequalities between `c_0`, `c_strict^iso`
   and `r_in(C_micro)` hold for every admissible symbol? Currently
   `c_strict^iso <= r_in(C_micro)` is established. `c_IR <= r_in(C_micro)`
   is established only under the isotropic-containment premise of Sec. 3.3.
   `c_0 <= c_strict^iso` is proved under the frozen point-(3) assumptions,
   with one independent adversarial review PASS. Thus every admitted cone
   satisfies `0 < c_0 <= c_strict^iso <= 1/sqrt(3)`. Equality and microscopic
   saturation are not consequences of this ceiling.
2. **Restoring hypotheses.** Which explicitly stated extra assumptions (for
   example `s=2` minimality with or without Eq. (2), or an irreducible `R`)
   give `c_0 = c_strict^iso` for a whole declared class?
3. **Intra/inter rule.** Does the s=4 family identity reflect a general
   structure that accounts for the missing speed, or is it specific to this
   ansatz?

Every class must keep the quantifiers of charter Sec. 2 and be declared
**before** solving.

### 7.3 Original gate question (answered for the declared s=4 class)

The original question was whether another admissible massless symbol can have
`0 < c_0 < c_strict^iso` for its own strict asymptotic body, while preserving
the same `N`, `C_micro`, embedding, unitarity, homogeneity and discrete
isotropy as its selected standard baseline. A candidate whose `c_0 < r_in(C_micro)`
only because its own strict body already falls short of `r_in(C_micro)` is not
this counterexample; see the charter's Sec. 0 for the (i)/(ii) split.

**Erratum (2026-09-15).** Earlier wording here attributed such a shortfall to
a nilpotent one-step coefficient. What is established is only this: a
saturation failure `c_strict^iso < r_in(C_micro)` requires at least one
nilpotent vertex coefficient (contrapositive of the vertex lemma). The
converse is not established. A nilpotent vertex removes the exact ray `n.h`
from `S_n`, but it does not by itself determine `c_strict^iso`, which must be
computed. See the charter's erratum.

The [gate charter](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md) requires the
internal dimension, isotropy group/action and representation, node/sector,
and any irreducibility assumptions to be explicit before solving. Do not
silently introduce minimality or weaken the symmetry when interpreting a result.

- One exact admissible counterexample refutes B_infty^* for a class containing
  it (realized for the declared s=4 class, Sec. 4.1).
- A rigidity claim requires an exhaustive analytic argument for an explicitly
  quantified class; failure to find a deformation is not such an argument.
- The absence of a continuous deformation alone does not exclude disconnected
  admissible symbols. A restricted proof leaves wider generality open.
- Prior-art classification assumptions must be checked before any novelty claim.

### Stop rule

Until a successor gate is chartered and closed:

- **NO causal sets**;
- **NO new substrate class**;
- **NO broad model search**;
- **NO anisotropic-QCA detour**;
- **NO change of support, embedding, time normalization or discrete isotropy
  within a declared rigidity comparison**;
- **NO novelty claim for B*, B_infty^* or the s=4 family (NOVELTY = OPEN)**;
- **NO use of a scalar `v_max` without definition**;
- **NO promotion of the s=4 family identity to a general QCA law**;
- **NO reading of `c_strict^iso`, `r_in(C_micro)` or `S_min` as "the microscopic
  speed of the substrate"** (Sec. 8.6);
- **NO new novelty audit, Bernstein-rigidity, paraunitary-classification or
  d=3-theorem line** under the Sec. 8.7 scope decision;
- **NO directional/anisotropic `I(v)` computation** (Sec. 8.8, NOT_AUTHORIZED);
- **NO operational-invisibility or no-signalling claim** from a rate function
  (Sec. 8.8); that question requires its own charter.

A certified falsification within the frozen admissible class is a successful
gate outcome. The s=4 counterexample is such an outcome for its declared
class only. This branch-local reconciliation does not promote anything to
`main`. The only later successor authorization is the point-(3) contract
in Sec. 7.2, by direct user instruction.

## 8. Directional causal saturation — canonical physical interpretation (2026-09-16)

**Evidence commit:** `2494192`.
[Report](../reports/2026-09-16--directional-causal-saturation.md),
[verifier](../scripts/verify_directional_saturation.py) (15/15, fail-closed,
fourteen exact).

The active physical question is: **does `c_IR` coincide with the microscopic
causal boundary of the discrete substrate?** The canonical answer is
**direction-dependent; in general, no.**

### 8.1 Three objects, never identified

For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
Eqs. (5.12) and (5.15):

`B(c_IR) ⊆ Γ ⊆ C_micro`,

- `B(c_IR)`: the emergent isotropic IR light cone;
- `Γ`: the ballistic / group-velocity propagation body;
- `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.

`Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
`conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
be assumed.

### 8.2 The canonical saturation function

For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`

`v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,

and, in the normalization `c_IR = 1`, the canonical directional saturation
function is the **support-function ratio**

`S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.

`S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.

`S_min` is a **descriptive scalar summary only**. The full directional function
`S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.

### 8.3 Walk (5.12)

`B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
`p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
faster than the emergent IR light speed while remaining inside `C_micro`.
`Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.

### 8.4 Walk (5.15) — the clean counterexample

`Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.

This refutes the identification

`sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.

Even when **all ballistic propagation respects `c_IR`**, the substrate permits
causal propagation outside the relativistic ball in non-axial directions.

**Evidence tags, not to be merged.** `sup|∇ω| = c_IR = 1` and
`Γ_2 ⊆ B(1)` are **ESTABLISHED (exact SOS certificate**
`(1-f²) - |∇f|² = s₂²s₃² + s₁²s₂²c₃² + s₁²c₂²s₃²`**)**, and `∂B(1) ⊆ Γ_2` is
exact from the conical point. That `Γ_2` also fills the open ball is
**SUPPORTED (numerical)** only. The counterexample does **not** depend on that
last half: it needs only `sup|v_g| = c_IR`, which is exact.

### 8.5 The gap is not a one-step artefact

At the eight vertex rays a single lattice path contributes, so
`(W^n)_{nσ} = (W_σ)^n`. Each `W_σ` has rank 1 with nonzero trace, hence
`(W_σ)^n = tr(W_σ)^{n-1} W_σ ≠ 0` **for every `n ≥ 1`** (exact). Therefore
`h_infty = h_{C_micro} = ||·||_1` exactly, and the distinction between `Γ` and
`C_micro` is not an artefact of a one-step support bound.

Between `Γ` and `C_micro`, propagation is non-ballistic and may be exponentially
suppressed; it is **not generically causally forbidden**. **No claim is made
that every point of this intermediate region has nonzero amplitude** — what is
proved is the statement about the vertex rays.

### 8.6 Scope correction to earlier scalar summaries

`c_strict^iso` and `r_in(C_micro)` remain mathematically valid summaries where
previously proved (Secs. 4, 6, 7), but **must not be interpreted as "the
microscopic speed of the substrate."** The microscopic causal boundary is
anisotropic and is represented by `C_micro`, equivalently by `h_{C_micro}(n̂)`.

Under (i) finite `F`, (ii) `d ≥ 2` and (iii) an isotropic IR cone, exact
equality `B(c_IR) = C_micro` is impossible, because `C_micro` is a finite
polytope and the IR body a Euclidean ball. This restates `B_full` (Sec. 3.3)
with its hypotheses made explicit; relaxing (i), (ii) or (iii) leaves it open.

### 8.7 Scope decision

The physical relation **emergent relativistic cone vs microscopic causal
body** remains the line. As of 2026-09-17, inside the frozen IR class of
Secs. 8.16–8.20, theoretical step 3 of that line is **closed**: the gap
is not only geometric (`c_IR < v_micro`) but operational
(`IR probe → δ_B(N) ≠ 0` for large `N`, nonperturbatively suppressed;
Sec. 8.20). No further signalling gate is authorized.

The live front is whether that structure can correspond to something in
nature (Sec. 8.21, `NOT_EXECUTED`), not another calculation of `C` and
not yet a laboratory implementation of the walk (fork 4A, identified,
not chartered).

**Not authorized by this result:** further search for mathematical novelty,
Bernstein rigidity, paraunitary classification, or a new dimension-3 theorem.

The previous novelty / Gate-C material is retained as historical project state
and is **not an active prerequisite** for the physical line. Sec. 7 is unchanged
and still governs anything done under the point-(3) contract.

### 8.8 LDP_RADIAL_INTERPRETATION — PASSED, subline CLOSED (2026-09-16)

**Status: `DOCUMENT_EXISTING_RESULT` — PASSED. This subline is CLOSED.**
Contract: [`OPERATIONAL_INVISIBILITY_GATE.md`](../theory/OPERATIONAL_INVISIBILITY_GATE.md).
A first freeze at `a9e611a` chartered the *directional* variant; it was narrowed
by user instruction before any solving and is **SUPERSEDED, UNSOLVED** — nothing
may be cited from it.

For walk (5.15), CJWW's own radial rate function Eq. (5.21),
`R̃(ℓ) = 2 arccosh(cosh(ℓ/2√3)³)`, has exactly the two slopes

`R̃'(0) = 1 = c_IR`   and   `R̃'(∞) = √3 = max_n̂ v_sub(n̂) = v_sub(body diagonal)`,

so by Legendre duality `Ĩ(r) = 0` for `r ≤ 1`, `0 < Ĩ(r) < ∞` for `1 < r < √3`,
and `Ĩ(r) = ∞` for `r > √3`, reproducing CJWW's control value `Ĩ(1.1) ≈ 0.104`.
Three regimes, with boundaries at precisely the two numbers Sec. 8 canonizes:

**ballistic/emergent | causal but exponentially suppressed | causally forbidden**

**ESTABLISHED (exact).** The *value* of (5.21) at CJWW's stated maximizer is
exact; the *location* of that maximizer is their numerical finding, not ours.

**Declared limitations, not to be dropped.**
- `Ĩ` is radial and demonstrably coarse. Since `v_sub(ê_i) = c_IR`, a velocity
  `r ê_i` with `r > 1` is already outside `C_micro`, where the amplitude is
  **exactly zero**, not suppressed. The finite rate `Ĩ` reports for `1 < r < √3`
  is therefore carried by non-axial directions only. The angular structure of
  `I(x)` is **not resolved**.
- Upper bound only; CJWW prove no lower bound.
- It bounds the position distribution of one particle, nothing else.

**Non-implication, explicit.** This does **not** yield an operational-invisibility
or no-signalling theorem. At QCA level an exponentially small tail still lies
inside the exact causal support, so "operationally invisible" may not be
asserted. That question needs resources, distinguishability or channel capacity
defined first, changes problem class, and merits an independent charter.

**NOT_AUTHORIZED:** anisotropic/directional `I(v)`; probability vs signalling.

(For the canonical conclusion of Sec. 8 as a whole, see Sec. 8.9.)

### 8.9 Canonical conclusion — stated at the right logical level

Earlier wording here read "`c_IR` **can** be the boundary of typical macroscopic
propagation without coinciding with the microscopic causal boundary". That is
modal, and too weak: this is not a possibility claim but an **explicit
counterexample**. Corrected, and canonical:

**(i) Existence — PROVED (exact).**

> There exists at least one local, unitary, finite-range model in 3D — the
> one-particle translation-invariant walk of CJWW Eq. (5.15) on `Z^3`, internal
> space `C^2`, jump length 1 — in which **all** ballistic propagation satisfies
> `|v_g| ≤ c_IR`, while the microscopic causal region is **strictly larger**
> than the emergent relativistic cone:
>
> `sup|v_g| = c_IR`  **and**  `B(c_IR) ⊊ C_micro`.

Both halves are exact: `sup|v_g| = c_IR = 1` by the SOS certificate of Sec. 8.4,
and `B(c_IR) ⊊ C_micro = [-1,1]^3` with `v_sub(n̂) = ||n̂||_1` reaching `√3 c_IR`
on the body diagonals, certified at every vertex ray for every `n` (Sec. 8.5),
hence not a one-step artefact. This statement does **not** rest on the
numerically supported half of `Γ_2 = B(1)`.

**(ii) Logical consequence — PROVED in the class studied.**

> `c_IR = sup|v_g|  ⇏  B(c_IR) = C_micro`.
>
> Equivalently: the equality "`c_IR` = microscopic causal limit" is **not a
> necessary consequence of relativistic emergence**.

**(iii) Explicitly NOT established — UNKNOWN.**

> `c_universe < ` the fundamental causal limit of our universe.

No evidence is offered here in either direction. This project makes **no claim
about our universe**; asserting (iii) from (i)-(ii) would be a category error,
since (i) is an existence result inside a declared model class.

### 8.10 SUBSTRATE_CONE_OBSERVABILITY — PASSED, gate CLOSED (2026-09-16)

Contract [`SUBSTRATE_CONE_OBSERVABILITY_GATE.md`](../theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md)
frozen at `d86b018` before solving;
[outcome](../reports/2026-09-16--substrate-cone-observability.md). This lifts
the Sec. 8.8 `NOT_AUTHORIZED` for the signalling question only.

The question was operational: for `ct < L < v_sub(n̂)t`, is `D = 0` or `D > 0`?
It is **undefined** for the one-particle walk, so the gate declared a
free-fermion (CAR) lift. On the one-particle sector `α_t(n_x) = W^t P_x W^{t†}`,
so `[α_t(n_x), n_y]` has `(y,y')` block `(W^t)_{y,x}((W^t)_{y',x})†` and is
nonzero exactly when the single-particle kernel is. **The operational causal
structure of the lift is the strict support of `W^t`** — the object already
certified in Sec. 8.5.

**Answer: `D > 0`, exponentially small, strictly off-axis.** Exactly zero for
`L > v_sub(n̂)t` (H4); nonzero `∝ 4^{-t}` at the vertex rays for
`ct < L < v_sub(n̂)t` (H2); **exactly zero in the six axial directions** for
every `L > ct`, since `v_sub(ê_i) = c` (H3). At `t = 3`, 108 of the 148
populated sites lie strictly outside `B(c)t`, all inside `C_micro t`, none
axial. **ESTABLISHED (exact, Gaussian-integer kernels).**

This is the signature sought: fundamental causality outside the light cone with
no superluminal ballistic propagation, carrying the angular fingerprint
`v_sub(n̂) = ‖n̂‖₁ c`.

**Limits.** Statements are about the lift, not the one-particle walk. A nonzero
commutator means *there exists* an intervention and a state with `D > 0`; no
specific protocol's `D` and no channel capacity were computed. How the
suppression varies across `C_micro \ B(c)` is the anisotropic `I(v)` question,
still `NOT_AUTHORIZED`. No claim about our universe: Sec. 8.9(iii) stands at
UNKNOWN, and a wider cone fully decoupled from accessible observables would be
invisible to any experiment, so no null result can establish exact coincidence.
No experimental or LIV constraint survey is authorized.

### 8.11 EMPIRICAL_SUBSTRATE_CONE_SURVEY — COMPLETE (2026-09-16)

Contract [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md)
frozen at `416dde1`;
[outcome](../reports/2026-09-16--empirical-substrate-cone-survey.md).

**Declared premise (computed before surveying).** With `t` in lattice steps, a
Planck-scale substrate puts this model's own effect at `10^(-8.4e41)` over one
second, against finest-ever bounds of `10^-20` to `10^-30`. The model's effect is
**unobservable in principle**. The survey is therefore model-independent. The
geometric window is by contrast not small: it reaches `√3 ct`, 73% beyond the
light cone.

**Verdict, in three levels.**

| | |
| --- | --- |
| Scalar no-signalling | experimentally tested, to finite precision |
| Directional causal tail of Sec. 8.10 | no specific localized operational test |
| Exact equality `C_fundamental = B(c)` | **not established** by null results |

In contract categories: `DIRECT_CONSTRAINTS_FOUND` for the scalar variable,
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure.

**Missing coupling map — the real obstacle.** `[A(t),B] ≠ 0` gives `∃` a state
and intervention with `D > 0`; it does **not** give that a standard Bell-test
protocol is that intervention. Converting a bound on Bell marginals into a
quantitative bound on the tail needs a coupling/protocol map — which observable
realizes `A`, which realizes `B`, which preparation exploits the commutator.
None exists. The scalar bound therefore constrains the right *kind* of variable
without being convertible into a number about our `D`.

**Withdrawn.** An earlier phrasing used Adenier–Khrennikov to fix the empirical
level at "percent-to-permille". That was an overreach: it is a contested
reanalysis of one dataset, not a universal bound nor a calibrated interval for
`D`. No numerical empirical level is claimed. Likewise "essentially untested" is
replaced by the exact-equality statement above.

**Category error recorded, the survey's main result.** Salart 2008 (`v > 10⁴ c`)
and Bancal 2012 (finite-speed influence ⟹ superluminal signalling) constrain
models where the superluminal influence *explains* the quantum correlations. The
tail of Sec. 8.10 is non-explanatory, so those bounds do **not** apply to it;
using them to "exclude" it would be a category error. LIV/dispersion/threshold
limits are `INDIRECT_ONLY` by contract Sec. 2.1, since Sec. 8 proves
`sup|v_g| = c` is compatible with influence outside `B(c)`. Lieb–Robinson
experiments (Cheneau 2012 and successors) **observe** this structure in
engineered lattices: realizability, not a constraint on nature.

**Consequence, and the firm epistemological point.** No finite sequence of null
results can prove `D = 0` exactly; it can only yield ever smaller upper bounds.
A reproducible positive result outside `B(c)` could falsify the identification
of `c` with the fundamental causal boundary. Sec. 8.9(iii) stands at UNKNOWN.

**Next step if the line continues (not opened).** Not a further theoretical
front, and not a generic FTL search: design the experiment that **maximizes `D`**
for a Sec. 8.10-type tail — which two local operations, which spacelike
separation, which remote observable optimally exploit an exponentially small,
anisotropic causal tail. Only afterwards does it make sense to ask whether an
existing experiment already did this accidentally, and by how much it falls
short. This is the coupling map above, and it is **not chartered**.

### 8.12 COUPLING_MAP_OPTIMAL_D — PARTIAL; exact signalling witness CLOSED (2026-09-16)

Contract [`COUPLING_MAP_GATE.md`](../theory/COUPLING_MAP_GATE.md) frozen at
`0f7628d`: frozen Sections 0–6 unchanged, outcome corrected;
[report](../reports/2026-09-16--coupling-map.md).

**Correction authorized by the user, 2026-09-16.** The former conditional H1
confirmation, universal linear/quadratic scaling and claimed restricted
optimal-D upper bound are withdrawn. The code computed an occupation
witness, not full trace-distance optimization. Four finite times cannot
establish asymptotic scaling; moreover `t = 5` exceeded the frozen `{2,3,4}`.
The historical ratios remain descriptive only. H1 is **OPEN**; H2 establishes
preparation dependence for the specified protocol, not necessity of coherence
for all admissible interventions. **H3 and H4 remain NOT REACHED**.

**Finite existence task: EXISTENCE_WITNESS_PROVED / INDEPENDENTLY_REVIEWED.** The user's
subsequent instruction chartered closure as a theorem/witness, not further
optimization or an experimental study. See
[`COUPLING_MAP_SIGNALING_WITNESS.md`](../theory/COUPLING_MAP_SIGNALING_WITNESS.md).
At `t = 2`, Alice at `0`, Bob at `y = (2,2,2)`, prepare
`(|0,down> + |y,down>)/sqrt(2)` before Alice chooses between `I` and
`exp(i pi n_0)`. Bob measures the even non-vacuum projection at his site.
The exact probabilities are

`p_0 = 121/512`, `p_1 = 169/512`, `Delta p_B = 3/32 > 0`, hence **`D >= 3/32`**.

The theorem fixes the existing CAR/Heisenberg convention, the state,
intervention, measurement and spacetime point. The exact kernel is nonzero
there: Bob is outside the emergent ball and **on the microscopic boundary**.
This proves membership in the exact causal support, not strict interior
membership. Each local site has two modes; the original `N = M = 1`
optimization is not closed. The
[verifier](../scripts/verify_signaling_witness.py) passes **17/17 exact checks**.
The [independent review](../reports/2026-09-16--signaling-witness-independent-review.md)
returns **PASS on the four requested points, no mandatory repairs**: analytic
probabilities, code correspondence, causal location, and the convention
`D = (1/2)||rho_1-rho_0||_1`. It records hashes of the unchanged reviewed
theorem and both scripts. This is one separate agent's independent review,
not external human review, consensus, or a full PASS of the optimal-D gate.

**Claim ceiling, branch-local:**

> In this free-fermion lift, given a state prepared with coherence between
> Alice and Bob's own site before Alice's choice, that local choice changes
> a measurement probability accessible
> to Bob outside the emergent relativistic cone and within the exact
> microscopic causal support. The choices are distinguishable in principle.
> Preparation of this operational channel from resources initially localized
> around Alice, Bob's optimal measurement, a globally optimal protocol and
> experimental feasibility are not established.

**Superseded clause, 2026-09-16.** The requirement of a resource already
distributed before Alice acts is no longer open: Sec. 8.13 exhibits a
*different* channel, in the same model, driven from a particle initially at
Alice alone. That successor does **not** supply a preparation protocol for
*this* channel, whose theorem, review and ceiling above are unchanged.

**Controls and limits.** For an Alice-localized particle the phase gate gives
only a global phase, hence exactly zero signal. Removing spatial coherence
also removes this protocol's signal. At the axial control the exact zero
kernel excludes Alice from the evolved Bob algebra, hence forbids signalling
for any initial state under even local Alice unitaries. By contrast, a zero
occupation witness alone never certifies `D = 0`.

The second coherent arm in this construction is **at Bob's initial site**;
the earlier hint excluding Bob from the resource is withdrawn. No Bell
protocol has been modelled. The finite interference term involves both
`K_0y` and `K_yy` with their internal alignment, not a universal asymptotic
law in one kernel. The empirical transfer of Sec. 8.11 remains unresolved;
the experimental problem is not opened. No claim about our universe follows.

**The original question, split.**

| Question | Answer |
| --- | --- |
| Theoretical: must `c` coincide with the substrate's causal limit? | **No** — (ii), proved |
| Physical: does it coincide in our universe? | **Unknown** — (iii) |

### 8.13 ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED (2026-09-16)

Successor to Sec. 8.12, chartered by direct user instruction as an
**existence question only**: does the signalling channel require a resource
that is already spatially distributed before Alice acts? **It does not.**
See [`ALICE_LOCAL_PREPARATION_WITNESS.md`](../theory/ALICE_LOCAL_PREPARATION_WITNESS.md)
and the [construction report](../reports/2026-09-16--alice-local-preparation.md).

Same unchanged CAR lift of CJWW (5.15), same conventions. At `T = 0` the
resource is exactly one particle, `|0,down>`, with every other mode vacant.
Between `T = 0` and `T = 2` **only the declared free dynamics acts**, equally
for both messages: the prepared state is `chi = S^2|0,down>`, given in closed
form by Cayley-Hamilton (`S^2 = 2fS - I`, `f = cos p1 cos p2 cos p3`), with
38 populated sites, `||chi|| = 1`, `chi(0) = -3 down/4` and
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`. Alice encodes at `A = (2,0)`
with `I` or `exp(i pi n_0)`; Bob measures the even non-vacuum projection at
`B = (3,(1,1,1))`. The exact probabilities are

`p_0 = 49/1024`, `p_1 = 25/1024`, `Delta p_B = 3/128 > 0`, hence **`D >= 3/128`**.

**Causal origin — the load-bearing step.** The bit is exogenous at `T = 2`.
Both conditional histories are *identical operators on the whole Fock space*
for `T = 0, 1, 2^-`, so the mutual information between the bit and any
pre-choice observable is exactly zero and no earlier encoding exists. Bob's
own site is **exactly vacant** at the encoding event (`chi(1,1,1) = 0`).
Comparing cones from `T = 2` is therefore the appropriate operational
reference for communication. From the encoding event,
`|y_B| = sqrt(3) > c_IR Delta T = 1` while `||y_B||_inf = 1` and
`K_1(0,y_B) = diag(0,1/4) != 0`: Bob is outside the emergent cone and on the
**boundary of the exact microscopic causal support**. **No microscopic
causality bound of the model is violated.** It is explicitly *not* claimed
that Bob is outside the emergent cone of the initial event: from `T = 0`,
`sqrt(3) < 3`.

**Claim ceiling, branch-local:**

> A particle initially localized at Alice alone suffices. The ordinary
> microscopic dynamics generates the required spatial coherence before the
> message is chosen. A later local choice by Alice then changes a Bob
> statistic one step afterwards, with Bob outside the emergent causal cone
> of **that encoding event** and within the microscopic causal support.
> This is not a violation of the model's microcausality. Optimality,
> minimal preparation time, experimental feasibility, asymptotics, capacity
> and any claim about our universe are **not** established.

**Evidence.** `verify_directional_saturation.py --local-preparation-only`
passes **21/21 exact checks**; the frozen witness verifier still passes
17/17 and the default suite 27/27, unchanged. The
[independent review](../reports/2026-09-16--alice-local-preparation-independent-review.md)
returns **PASS, no mandatory repairs**, and explicitly covers the item most
exposed to adversarial attack: the closed-form derivation of `S^2|0,down>`
and the identity of the two pre-choice histories. It reconstructs the
prepared state from a separately transcribed symbol, records SHA256 hashes of
every reviewed input, and confirms the script change is one added function
plus a CLI dispatch, with the frozen witness path untouched. This is one
separate agent's independent review — **not** external human review,
multi-member consensus, or ratification.

**Relation to Sec. 8.12.** The hypothesis is strictly weaker (no pre-existing
Alice-Bob coherence) and the geometry differs (one readout step to
`(1,1,1)`, not two to `(2,2,2)`); the signal is smaller, `3/128` against
`3/32`. This does **not** retroactively supply a preparation protocol for the
Sec. 8.12 channel, whose frozen theorem and review keep their exact bytes and
scope. The optimal-D gate stays **PARTIAL**; H1 stays **OPEN**; H3 and H4 stay
**NOT REACHED**. The experimental problem remains unopened, by instruction.

### 8.14 NONCORNER_SIGNALING_CONSTRUCTED / INDEPENDENTLY_REVIEWED (2026-09-17)

Successor to Sec. 8.13, executed under the frozen
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md): the
Alice-local preparation channel is **not** confined to the vertex
`(1,1,1)`. The [corrected execution report](../reports/2026-09-16--noncorner-signaling-gate.md)
and its [independent review](../reports/2026-09-16--noncorner-signaling-gate-independent-review.md)
are frozen together here. The review verdict is **PASS with three mandatory
textual repairs (`MR1`--`MR3`)**, all applied to the report; none changes a
computed quantity or the scientific verdict.

The exact one-step kernel support gives precisely four admissible non-vertex
sites, `y = (+/-1,+/-1,0)`, and the preregistered construction succeeds at
all four. At each site,

`M(y) = diag(-3/256,0) != 0`,
`p_0 = 25/1024`, `p_1 = 49/1024`, and `Delta p_B = 3/128`.

The reduced-state trace distance is exactly `D = 3/128`, so the exhibited
projection saturates the distinguishability bound for each computed pair of
states. This is pairwise measurement optimality only; it is not protocol,
preparation, site or intervention optimality. The result refutes
vertex-exclusivity for this protocol at `Delta T = 1`; it says nothing about
`Delta T = 2`, other vertices, asymptotic scaling, capacity, experimental
feasibility or our universe. No violation of the model's microscopic causal
bound is claimed.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NONCORNER_SIGNALING_CONSTRUCTED /
  INDEPENDENTLY_REVIEWED` in the exact scope above.
- **Software certificate: PASS with six externally verified properties not
  yet encoded as checks.** The run
  `verify_directional_saturation.py --noncorner-gate-only` passes **20/20
  exact checks**, but that count **is not by itself an exhaustive certificate**
  of the six properties listed in the execution report Sec. 8. They were
  independently checked by the reviewer. They remain recorded certification
  debt, not gaps in the scientific result.

The reviewed script is deliberately unchanged after review. Encoding those
six additional checks would alter the reviewed artefact and therefore require
a new review of that file. The earlier frozen contracts and witnesses retain
their bytes and scope; the optimal-D gate remains **PARTIAL** and no
experimental-design gate is opened here.

### 8.15 PHYSICAL_DIMENSIONAL_TRANSLATION — CLOSED / CONDITIONAL (2026-09-17)

Contract
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](../theory/PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md)
frozen at `fca5881` before solving; see the
[dimensional audit](../reports/2026-09-17--physical-dimensional-translation-audit.md).

**Verdict: `DIMENSIONAL_MAP_CONDITIONAL`.** The source conventions support the
symbolic restoration

`x = a n`, `t = N tau`, `k = p/a`,
`E = hbar omega/tau (mod 2 pi hbar/tau)`, and
`v_phys = (a/tau) grad_p omega`.

Hence `c_IR^phys = a/tau`. Identifying it with an observed `c_phys` imposes
`a = c_phys tau`; it does not determine either absolute scale. The model and
checked sources specify no numerical `a` or `tau`, and the earlier Planck-scale
calculation was explicitly conditional, not a scale derivation.

For the frozen non-corner witness, conditionally on `(a,tau)`, the
encoding-to-readout interval is `tau` and Bob is at Euclidean distance
`sqrt(2)a`. If `a/tau = c_phys`, then the scale-free ratio is
`L/(c_phys tau) = sqrt(2)`: outside the emergent cone and inside the exact
one-step microscopic support, exactly as in lattice units.

The value `3/128` acquires **no units**. It remains the exact probability
difference and trace distance for the two idealized local states. It is not an
energy, rate or dimensional coupling. The exactly localized preparation is
broad over the full Brillouin zone, not a low-energy narrow-band state, so no
unique physical energy or momentum can be assigned from the IR dispersion.

**Claim ceiling.** A consistent conditional dictionary is established; a
parameter-free prediction in SI units is not. Absolute cutoff scale, physical
realization/coupling, efficiencies, noise, feasibility and any identification
with nature remain unspecified. No experiment was designed and `Delta T = 2`
was not opened.

### 8.16 NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`NARROW_BAND_SIGNALING_GATE.md`](../theory/NARROW_BAND_SIGNALING_GATE.md)
preregistered at `817050d` before any computation. Three artefacts are frozen
together at `778a44a`, through the provenance chain `5f6d350` -> `f00f64e` ->
`778a44a`:

- the [execution report](../reports/2026-09-17--narrow-band-signaling-gate.md);
- its exact certificate
  [`verify_narrow_band_gate.py`](../scripts/verify_narrow_band_gate.py);
- the [independent review](../reports/2026-09-17--narrow-band-signaling-gate-independent-review.md).

The question was whether the Alice-local signalling mechanism admits an
IR-controlled version with a preestablished narrow-band resource. The frozen
class is:

- node `p = 0`, both Weyl branches;
- `g(q) = (1-|q|^2)^2_+` supported on `|p| <= Lambda`, with
  `0 < Lambda < pi/4`;
- spin `down` and two common steps;
- the point gate `U_1 = exp(i pi n_0)` at the origin;
- Bob at `(1,1,0)`, with `Delta T = 1`.

**Verdict.** The Sec. 7 stop rule fires at the first control, before any signal
in Bob is computed: the point encoder is incompatible with the preregistered
relative IR criterion. Let `kappa = Lambda^3/(6 pi^2)`, the in-band share of
any one-site vector, and `s = ||P_0 psi_Lambda||^2`, with `0 < s <= kappa`. Then

`||Delta_Lambda||_1 = 4 sqrt(s(1-s)) -> 0`,
`eta_enc = ||Delta - Pi Delta Pi||_1/||Delta||_1 = sqrt((1-kappa)(1-3s(1-kappa))/(1-s))`.

So `eta_enc > 2 sqrt(6)/5` on the whole chart and `eta_enc -> 1`, while the
absolute leakage `epsilon_UV = 4s(1-kappa)` also tends to zero. The residual
outside the IR-IR block is dominated by the IR-UV and UV-IR coherences; the
UV-UV block is relatively `O(sqrt s)`. This is **not** a statement that the
encoding, the information or any signal is UV.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: CLOSED.** `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS /
  INDEPENDENTLY_REVIEWED`, in the exact scope below.
- **Review metadata.**
  - Cold independent agent review: PASS, after the mandatory repairs R1-R4 and
    MR1, all textual and all applied.
  - Human review: PASS.
  - No external peer review / no external replication yet.
  - Two earlier same-session adversarial reviews are archived as secondary,
    non-independent records. The self-review contains errors that the
    independent review corrected.
- **Software certificate: PASS, 34/34 exact checks.** The count covers only
  the identities and limits marked [V] in the report. The analytic steps listed
  in report Sec. 12 are not encoded as checks; the independent reviewer
  verified them by hand. They are recorded certification debt, not gaps in the
  result. The certificate imports `verify_directional_saturation.py`, which
  requires numpy, pinned in `scripts/requirements.txt`.

**Claim ceiling.** The result holds only for the frozen class and the Sec. 7
criterion.

- `D_B` was not computed, and `D_B = 0` is not asserted.
- It does not refute `3/128`, either at the vertex or at the non-corner sites.
  The non-corner witness uses the same `y_B = (1,1,0)`, but with an exactly
  localized resource and no IR criterion.
- It is no impossibility result for other encoders (extended, smoothed or
  `Lambda`-dependent gates), for resources without exact spectral support, for
  other notions of IR control, for other QCA, or for the physical continuum.
- `Lambda -> 0` is not `a, tau -> 0`, and no physical scale is set
  (Sec. 8.15).

**Erratum, charter header.** Lines 3-7 of the charter are pre-publication
text. They cite drafting base `HEAD=11efe1f` and scientific remote `780ecb0`,
state `NOT_EXECUTED / OUTCOME_OPEN`, and say that publication and execution
are pending. All of that is superseded: the charter was published at
`817050d`, executed, and frozen at `778a44a` with the status recorded in this
section. The charter deliberately keeps its bytes, for two reasons:

- its sha256 `3d559ced...` is pinned by the frozen certificate (check 1)
  and recorded in the report, the independent review and the freeze
  commits;
- contracts in this repository keep their pre-execution text, as
  `NONCORNER_SIGNALING_GATE.md` does.

The header was never part of the scientific contract (Secs. 1-15), which
is unchanged. `Delta T = 2` and the experimental problem remain unopened.

### 8.17 OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`SCALED_IR_SIGNALING_GATE.md`](../theory/SCALED_IR_SIGNALING_GATE.md)
preregistered at `31b5797` before any computation. Successor of Sec. 8.16,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--scaled-ir-signaling-gate.md);
- its exact certificate
  [`verify_scaled_ir_gate.py`](../scripts/verify_scaled_ir_gate.py);
- the [independent review](../reports/2026-09-17--scaled-ir-signaling-gate-independent-review.md).

The question is the disappearance law of Bob's distinguishability when
regions of size `O(1/Lambda)`, a margin `O(1/Lambda)` outside the emergent
cone of Alice's whole region, and time `O(1/Lambda)` are scaled together
(`N = Delta T = 1/Lambda`, Euclidean balls of radius `N/4`, frozen internal
families). A signal at fixed `Delta T`, or with an `O(1)`-site margin, does
not answer it.

**Verdict.** `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The eight frozen operations are IR-admissible. There is a directional
exponential upper bound, independently re-derived, for every one-particle
state and every unitary supported on `A_N`:

`δ_{M,M_B}(N) ≤ D_B(N) ≤ 36 N^4 exp[-(1 - √3/2)(log 2) N]`, `N ≥ 2`,

with `J = (1 - √3/2) log 2 > 0`. This **excludes**
`IR_RESOLVABLE_SIGNALING_POLYNOMIAL` in the frozen class and **does not
authorize** `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. All sixteen pairs
remain `OPEN_PAIR`: no positive lower bound, no proven vanishing, no
non-vanishing amplitude. `D_B = 0` is not asserted. The independent review
attacks specifically the three load-bearing steps named before promotion
(the geometry-to-kernel derivation of `J`, uniformity of `36 N^4`, and
polynomial exclusion without an existence claim) and returns **PASS**, with
no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with a one-sided quantitative bound.**
  `OPEN_AFTER_SCALED_IR_ANALYSIS / INDEPENDENTLY_REVIEWED`, in the exact
  scope below.
- **Review metadata.**
  - Cold independent agent review: PASS. No mandatory repairs. The three
    recommended drafting clarifications (`D_B = (1/2)||ρ1-ρ0||_1`;
    off-diagonal of the ellipse matrix; Schur diagonal operator-norm) were
    applied to the execution report at freeze. They change no quantity and
    no classification. Execution-report sha256 before/after those phrases:
    `4876ecab…` / `86a086dc…`. The CAR bound (DF) is not part of the frozen
    claim for the sixteen pairs.
  - Human freeze authorization: the 2026-09-17 instruction to freeze this
    status if the cold review passed, then to publish with those
    clarifications and without additional science.
  - No external peer review / no external replication yet.
- **Software certificate: PASS, 53/53 exact checks.** The count covers only
  the identities and limits marked [V] in the execution report. The
  analytic steps for `J`, `T_N`, `(D1)` and the classification were
  re-derived by the independent reviewer; they are not encoded as checks.

**Claim ceiling.** The result holds only for the frozen scaled class
(Euclidean balls, `α = 1/2`, `θ = π/2`, the declared internal families,
CJWW (5.15) in the one-particle sector).

- Any allowed effect in this class is at most `O(N^4 e^{-JN})`. That is a
  one-sided, model-falsifiable bound. It is not a two-sided prediction and
  not an existence result.
- Polynomial IR-resolvable signalling is discarded **in this
  geometry/class**. If a positive signal exists, it is at most
  nonperturbatively small. Existence is not claimed.
- The bound does not refute `3/128`, the vertex or non-corner witnesses, or
  the narrow-band negative (Sec. 8.16).
- `N → ∞` is not `a, τ → 0`. No physical scale is set (Sec. 8.15). An
  `e^{-JN}` law would translate only conditionally to a form
  `e^{-J' λ/a}`, with no numerical prediction.
- The internal families are not exhaustive. `M = a I + b·σ` in general is
  not covered. `I` is `REFERENCE_CONTROL` only.
- No new encoder is authorized. The cancellation analysis of the sixteen
  pairs is Sec. 8.18. The regional exponential rate is Sec. 8.19. The
  remaining bottleneck is the integrated Laplace coefficient
  (Hessian, profiles, spin, interference with the free tail `r`), not
  yet chartered.

`Delta T = 2` and the experimental problem remain unopened.

### 8.18 OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`LOWER_BOUND_NO_CANCELLATION_GATE.md`](../theory/LOWER_BOUND_NO_CANCELLATION_GATE.md)
preregistered at `1717d5e` before any computation. Successor of Sec. 8.17,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--lower-bound-no-cancellation-gate.md);
- its exact certificate
  [`verify_lower_bound_no_cancellation_gate.py`](../scripts/verify_lower_bound_no_cancellation_gate.py);
- the [independent review](../reports/2026-09-17--lower-bound-no-cancellation-independent-review.md).

**Verdict.** `OPEN_AFTER_CANCELLATION_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The unique-path vertex

`(S^N)_{(N,N,N),0} = 4^{-N} |↓⟩⟨↓|`

exists and cannot be promoted to a regional leader (`K = log 4`, kills
`↑`, coherent regional sum). The Euclidean minimum of `|y-x|_2` on the
two balls is unique and lies on both spheres, where the profiles vanish.
That implies neither `A = 0` nor `A ≠ 0`. All sixteen pairs remain
`OPEN_PAIR`. `D_B = 0` is not asserted. The independent review attacks
those three load-bearing claims and returns **PASS**, with one recommended
drafting clarification applied at freeze (execution-report sha256 before /
after: `33691df6…` / `2da09280…`).

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN.** The obstacle is now localized: the
  competition between the propagation exponent and the profile zero at
  the boundary, not a missing trajectory and not a new encoder.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed.
- **Software certificate: PASS, 24/24 exact checks.** Identities only;
  leader, `A` and remainder are analytic and open.

**Claim ceiling.** Same frozen class as Sec. 8.17. No existence, no
vanishing, no `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The regional
rate is Sec. 8.19.

### 8.19 OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md`](../theory/REGIONAL_DIRECTIONAL_ASYMPTOTICS_GATE.md)
preregistered at `08613d0` before any computation. Successor of Sec. 8.18,
without reopening it. Three artefacts are recorded together here:

- the [execution report](../reports/2026-09-17--regional-directional-asymptotics-gate.md);
- its exact certificate
  [`verify_regional_directional_asymptotics_gate.py`](../scripts/verify_regional_directional_asymptotics_gate.py);
- the [independent review](../reports/2026-09-17--regional-directional-asymptotics-independent-review.md).

**Verdict.** `OPEN_AFTER_REGIONAL_SADDLE_ANALYSIS / INDEPENDENTLY_REVIEWED`.
The regional exponential rate is

`K_* = I(v_*)`, `v_* = (1 - 1/(2√3))(1,1,1)`,

with `I(v) = sup_ξ [ξ·v - arcosh(∏_j cosh ξ_j)]`. This is strictly
between `J` and `log 4`. It is the unique minimizer of `I` on the
regional velocity set (supporting tilt `ξ_* ∥ û`). The profile logarithms
are `O(log N)` and shift the saddle by `O(1)` lattice sites; they do
**not** change `K_*`. The coefficient `C` and the power `β` remain
unclassified. All sixteen pairs remain `OPEN_PAIR`. The independent
review attacks the three load-bearing claims (`I(v)` and the dual saddle;
uniqueness of `v_*`; `O(log N)` profiles) and returns **PASS**, with no
mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: OPEN, with the exponential rate identified.**
  `K_* = I(v_*)` is the Legendre envelope of the regional kernel. It is
  the exponential rate of `L` only if some `C` (or `C^{(j)}`) is
  non-vanishing and controlled, which is not claimed.
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze this status if the cold review passed, and not to open a
  coefficient gate before that review.
- **Software certificate: PASS, 18/18 exact checks.** Identities only;
  `C`, `β` and remainder are analytic and open.

**Claim ceiling.** Same frozen class. This section does not claim
existence, vanishing, or `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`.
No new encoder. The complete Laplace coefficient at this unique saddle
is Sec. 8.20.

### 8.20 PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED (2026-09-17)

Contract
[`REGIONAL_LAPLACE_COEFFICIENT_GATE.md`](../theory/REGIONAL_LAPLACE_COEFFICIENT_GATE.md)
preregistered at `6f520ad` before any computation (blob `18d1f65`).
Successor of Sec. 8.19, without reopening it. Three artefacts are
recorded together here:

- the [execution report](../reports/2026-09-17--regional-laplace-coefficient-gate.md);
- its exact certificate
  [`verify_regional_laplace_coefficient_gate.py`](../scripts/verify_regional_laplace_coefficient_gate.py);
- the [independent review](../reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md).

**Verdict.** `PAULI_LEADING_COEFFICIENT_NONVANISHING / INDEPENDENTLY_REVIEWED`.
For all sixteen frozen pairs,

`L_{M,M_B}(N) = e^{-K_* N} N^{-13/2} (C_{M,M_B}(θ_N) + O(N^{-1/2}))`,

with `θ_N = {√3 N/4}` and `β = 13/2`. The complete coefficient is a sum
of the free-tail interference against the encoder layer, over the two
torus saddles `η ∈ {0, π(1,1,1)}` (distinct projectors `P` and `P̄`,
weights `Γ_±`). `C(θ)` is sign-definite and uniformly non-vanishing; the
relative oscillation is bounded by `1.47×10^{-3}`. Quadratic terms are
only bounded, at rate `e^{-2 K_* N}`. The independent review attacks the
seven load-bearing claims (`β`; complete `C` as a sum; uniform
non-vanishing; remainder vs charter `o(1)`; `C(θ)` vs constant `C`;
eight torus points vs frozen `K_*`; terminal state) and returns **PASS**,
with no mandatory repairs.

**Frozen status, keeping evidence levels separate:**

- **Scientific result: PAULI_LEADING_COEFFICIENT_NONVANISHING.** `β = 13/2`
  is identified. All twelve Pauli pairs have `C(θ) ≠ 0` uniformly in `θ`,
  controlled against an `O(N^{-1/2})` remainder. With Secs. 8.17 and 8.19
  this authorizes, for those twelve pairs,
  `δ_{M,M_B}(N) = |C_{M,M_B}(θ_N)| N^{-13/2} e^{-K_* N} (1 + O(N^{-1/2}))`
  and `IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED` for those pairs. The
  four `M = I` pairs are also non-vanishing (`REFERENCE_CONTROL`).
- **Review metadata.** Cold independent agent review: PASS. No mandatory
  repairs. Human freeze authorization: the 2026-09-17 instruction to
  freeze, commit and promote as separate steps if the cold review passed.
- **Software certificate: PASS, 58/58 exact checks.** Identities and
  interval enclosures of closed forms, including uniform sign of
  `C_{M,M_B}(θ)` for all sixteen pairs. Analytic remainder lemmas (`N_*`,
  `C'`) are report `[A]`, not encoded. Finite-`N` diagnostics are
  `SUPPORTED` only.

**Claim ceiling.** Same frozen class. `C = C(θ_N)`, not an `N`-independent
constant. The remainder is asymptotic: `N_*` and `C'` are not explicit;
the leading formula is not quantitatively reliable for `N ≲ 10^3`, and
for `M ∈ {I, σ_3}` the `N^{-17/2}` piece dominates at diagnostic `N`.
No `D_B = 0`, no `δ ≡ 0`. Does not reopen `K_*`, `v_*`, geometry,
encoders, detectors, profiles, node or walk. Does not reopen
Secs. 8.16–8.19, `3/128`, no-corner, or `Delta T = 2`. `N → ∞` is not
`a, τ → 0`. No physical units. No claim of a microcausality violation.
The general family `M = a I + b · σ` is not covered.

The Sec. 8.19 sentence that the spectral-radius maximum is unique at
`η = 0` is false (equality on `{0,π}³`); `K_*` is unchanged and the extra
contributing point `π(1,1,1)` is included in `C`. The Sec. 8.19 files
are not edited.

This is a branch-local promotion only; `main` is unchanged.

**Project-level consequence (direct user instruction, 2026-09-17).**
In this frozen class, theoretical step 3 of the physical line is closed.
There is an operational IR response outside the emergent cone, and it is
not a mere consequence of the UV propagator. For the twelve Pauli pairs
the response is asymptotically non-vanishing and
`IR_SIGNALING_NONPERTURBATIVELY_SUPPRESSED`. The precise claim, not to
be exaggerated, is:

> In the 3D Weyl QCA under study, the difference between the emergent
> relativistic cone and the microscopic causal support is not only a
> geometric possibility: under the preregistered IR-controlled protocol
> it produces an asymptotically non-vanishing operational response,
> albeit nonperturbatively suppressed.

That is a property of the model, with standing outside the repository as
such. It is not a statement about nature, not `D_B > 0` for every QCA,
and not an experimental prediction. No further signalling gate is
authorized. Fork 4A (a physical implementation of the walk that could
test the derived law) is identified and **not chartered**. The authorized
next front is Sec. 8.21.

### 8.21 PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE — AUTHORIZED, NOT_EXECUTED (2026-09-17)

Contract
[`PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md`](../theory/PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE.md)
frozen before any calculation, by direct user instruction (2026-09-17),
with the four closure criteria and first-class negative outcomes
incorporated before execution (this commit; first preregistration
`e9353ad`). Successor of Sec. 8.20, without reopening it. Inherits
Sec. 8.15 (`DIMENSIONAL_MAP_CONDITIONAL`) without reopening the `3/128`
audit. **Not a signalling gate, not a rate gate, not a Laplace-coefficient
gate, not a laboratory-implementation gate (4A).**

**Initial evidence status: `NOT_EXECUTED / OUTCOME_OPEN`.**

Step 3 is **input**, not an object to re-optimize. The gate does **not**
ask whether `δ_{M,M_B}(N) ≠ 0`. It asks whether a physically defensible
identification

`(a, τ, Λ, internal modes, A, B) ↔ (physical magnitudes and operations)`

converts `δ(N) ∼ |C(θ_N)| N^{-13/2} e^{-K_* N}` into a dimensional,
falsifiable prediction.

**Four hard closure criteria, all scored separately:**

1. **Absolute scale.** `a/τ = c` is not enough. External information must
   fix `a` or `τ`, or an additional physically motivated relation must
   appear. `a = ℓ_P` is `ASSUMPTION`, never `DERIVED`.
2. **Physical dictionary.** What the two internal components are, which
   physical operation implements `M = σ_j`, what `M_B` is, and what a
   narrow-band preparation is in the candidate system. A formal relabelling
   is not a dictionary.
3. **Dimensional observable.** From a dimensionless distance/probability
   to something an apparatus records (counts, phase, frequency, energy,
   occupation, correlation, or other), with an explicit SI law.
4. **Detectability.** If substituting physical scales yields
   `δ ∼ e^{-K_* λ/a}` with `λ/a` astronomical, the effect may be real
   and experimentally inaccessible. That is a legitimate closure.

A viable experiment is **not** the success criterion. First-class
negative outcomes: `NO_ABSOLUTE_SCALE_DERIVABLE`,
`PHYSICAL_MAP_CONDITIONAL_ONLY`,
`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`. None of these weakens Sec. 8.20.

Binding separation: model closed ≠ nature established ≠ experiment designed.

**Premises, not reopened:** `K_*`, `β`, `C(θ_N)`, the sixteen pairs, the
conditional dictionary of Sec. 8.15. **Not authorized:** execution of
this gate; fork 4A; a new signalling encoder, detector or geometry;
re-optimizing `K_*` or `C`; treating `N → ∞` as `a, τ → 0`; using a
Planck fiat as `DERIVED`.

**Theory paper (draft, not a gate).** The closed model result is written
as
[`papers/ir-corona-operational-response-draft.md`](../papers/ir-corona-operational-response-draft.md).
It does not wait on 4B. It separates ultraviolet propagator, infrared
operational response, and nature.

**Literature input to 4B, not execution.**
[`2026-09-17--physical-realization-literature-scan.md`](../reports/2026-09-17--physical-realization-literature-scan.md).
Adversarial bibliographic scan only. Three bins:
`ENGINEERED_EMULATOR`, `NATURAL_EFFECTIVE_ANALOG`,
`FUNDAMENTAL_CANDIDATE`. Hard question (natural system, `a` and `τ`
physically fixed, infrared cone strictly narrower than microscopic
support, known observable of that gap): **no** on this pass. Ion-trap
and photonic Dirac automata are 4A antecedents. Pavia/Mlodinow–Brun
are incomplete fundamental candidates (Planck `ASSUMPTION`, different
observables). This scan does **not** assign a 4B terminal state.


## 9. H1-only inhomogeneous reopening — branch-local update (2026-09-20)

**Status (2026-09-24): H1 OPEN; H1c localization unproved, work PAUSED.
The operational contract is fixed in Sec. 9.6; the next gate is T1.**

This update supersedes the older statement that physical-realization / absolute-scale
Sec. 8.21 is the active line. The flat CJWW (5.15) operational IR-corona result
remains closed in its frozen class. The later inhomogeneous/AdS extension is not
reactivated as a whole: only H1 has been reopened.

Full research record:
- [H1 chat research log](../reports/2026-09-20--h1-chat-research-log.md)
- [H1 localization reconstruction and gate ledger](../reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md)
- primary endpoint/layer source: [regional Laplace-coefficient gate](../reports/2026-09-17--regional-laplace-coefficient-gate.md)

### 9.1 Frozen local structure

For
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=e^{-i\vartheta(X)\beta/N},
\]
under the working frozen beta contract
\[
\beta^2=I,\qquad \beta D\beta=D^{-1},
\]
the dominant rank-two Riesz bundle satisfies
\[
\mathcal P\beta\mathcal P=0.
\]

Current statuses:
- \`H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT\`;
- \`H1a = PROOF_WRITTEN / UNREVIEWED\`;
- \`H1b = PROOF_WRITTEN / UNREVIEWED\`;
- \`DERIVATIVE_SELECTION_RULE = PASS\`.

No global torus spectral gap is claimed.

### 9.2 Endpoint absolute-mass gate

The 2026-09-17 primary regional report was rechecked. It uses the complete
endpoint spinors, before spectral projection,
\[
f=s_Nb_N\chi,\qquad w=h_BM_Br,
\]
with
\[
b_N=O(N^{-3/2}),\quad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),\quad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

Accounting for tangential area \(O(N(1+j))\) at normal depth \(j\) and the
exponentially summable tilted normal weight gives
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]

Therefore:
\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

This is a full-spinor absolute bound, not a cancellation or dominant-projection
bound.

**Scope at the 2026-09-24 freeze:** these are the inherited flat endpoint
estimates. Their transfer to the two-channel response and its reference
`U_N^N Phi_N` is not certified here; that trace belongs to T1–T2 in Sec. 9.6.

### 9.3 Local-window insertion and leakage gates

Using the derivative selection rule and the endpoint bounds:
\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

The final complementary-bundle leakage is controlled by the full Bob norm.
The safe dominant correction is the zeroth-order \(Q\beta\mathcal P/N\) term,
giving
\[
|\Delta T_Q|=O(N^{-15/2}),
\]
not the earlier exploratory \(O(N^{-8})\) count. Hence:
\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

These are local-window statements only.

### 9.4 Remaining H1c gate

Literal pathwise H1b is not valid because a spatial path carries individual
hopping matrices \(D_h\), not the full symbol \(D(z)\). Thus:
\[
\texttt{H1c_GLOBAL = UNNECESSARY},
\qquad
\texttt{H1c_LOCALIZED = OPEN}.
\]

The unresolved localization statement recorded before the model freeze is:
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

Work on that asymptotic statement is **PAUSED** by the 2026-09-24 decision.
Sec. 9.6 supersedes the immediate route below with an exact observable gate.

A candidate momentum-space Dyson route has been formulated. Its key local
selection factor is
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)=O(|q|),
\]
and, for \(K_N(q)=N^3\widehat\vartheta(Nq)\),
\[
\int |q||K_N(q)|\,dq
=\frac1N\int |p||\widehat\vartheta(p)|\,dp.
\]
The working regularity assumption for this route is the Fourier-moment
condition
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|\,dp<\infty.
\]

The historical candidate \(n\)-insertion estimate was
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

**This estimate is not proved.** The missing step is uniform control of
non-normal variable-momentum products, including complementary-bundle visits,
transitions among the eight saddle neighborhoods, and regions where the local
Riesz splitting is unavailable. No momentum-conservation assumption may be
smuggled into that proof.

The [2026-09-24 Dyson precheck](../reports/2026-09-24--h1c-dyson-target-check.md)
also challenges this target when `n` counts raw insertions and the fixed
flat embedded endpoints are admitted. That precheck remains preliminary,
without independent review; this freeze does not promote it or transfer
its fixed-endpoint conclusion to the new physical response.

### 9.5 Locks

The H1 reopening does not change:
- \`E0 = OPEN_AT_STOP\`;
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`;
- \`E / AdS = STOPPED_UNPROVEN\`.

No localization or H1 promotion is authorized without proof and review.
The explicit operational model choice in Sec. 9.6 closes a contract only.

### 9.6 H1c-0 close / two-channel operational model — 2026-09-24

Direct user instruction freezes **TWO_DISTINGUISHABLE_CHANNELS** for this
candidate extension. The complete contract, prior diagnostic stages and
seven-report provenance are in the
[Schur audit and operational close, §§6–8](../reports/2026-09-24--h1c-return-kernel-schur-audit.md).

The one-particle space is `ell^2(Z^3) tensor C^2_channel tensor C^2_spin`.
The blocks of `D=S direct-sum S^-1` are assumed to be distinguishable
internal channels; `beta=sigma_x_channel tensor I_spin` exchanges them.
Bob's ability to resolve the channel is part of the new assumption. The
earlier repository did not derive this physical interpretation.

Prepare `Phi_N=(phi_N,0)` and evolve
`Psi_b=U_N^N mathcal U_M^(b) Phi_N=(psi_b^+,psi_b^-)`.
At encoding, `U_M direct-sum U_M` and `U_M direct-sum I` agree on this
preparation; they are not identified as physical operations on other states.
Bob uses `F_+=E direct-sum 0`, `F_-=0 direct-sum E` and
`F_empty=I_H-(E direct-sum E)`. The primary response is `(L_+,L_-)`,
where `L_±=<psi_1^±,E psi_1^±>-<psi_0^±,E psi_0^±>` and
`L_empty=-L_+-L_-`. `L_block=L_+` and `L_incl=L_++L_-` are only
coarse-grainings; signed responses are summed before absolute values.

For `vartheta=0`, `C_N=I` and `U_N^N(x,0)=(S^N x,0)`, so
`(L_+,L_-)=(L_flat,0)` and `L_incl=L_flat` exactly. This flat control
motivates the candidate; favorable asymptotics do not select its detector.
Channels may retain quantum coherence; the three-outcome POVM does not
reconstruct every coherence. Identification with a concrete physical
system remains OPEN. All future extension claims are conditional on this
contract, not universal claims about the original flat protocol. Neither
coarse-graining may later replace the primary observable for better powers.

```text
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

**Exploratory sequence executed by direct user instruction, 2026-09-24:**

1. **T1 — exact signed P/Q lift:** derivation and frozen five-piece
   vocabulary in
   [`two-channel T1 report`](../reports/2026-09-24--two-channel-t1-exact-signed-pq.md).
   Status: `PASS`, reviewed by Claude Opus and DeepSeek V4-Pro in the
   deliberative session
   [`T1 re-review`](../debates/2026-09-24--two-channel-t1-rereview.md).
   This is independent agent review across two model families, not human
   review. The pass is conditional on the explicit two-channel contract and
   a fixed admissible W. It does not certify estimates.
2. **T2 — trace of `O(N^-6)`:**
   [`T2 trace`](../reports/2026-09-24--two-channel-t2-trace.md) locates
   the old bound in the normalized auxiliary bilinear return correction.
   Status: `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`. It is a potential sub-contribution in the terminal-P linear slot
   `A_cP` for the earlier functional, conditional on matching its endpoint.
   No transfer to any of the ten current pieces is proved. The old
   `O(N^-6)` remains a coarse ceiling, not a signed term or coefficient.
3. **T3 — cancellation:** status `STOPPED_NO_SIGNED_TERM`. The frozen stop applies because T2 isolated no
   signed term or coefficient. No cancellation or symmetry search was
   performed; see [`T3 stop`](../reports/2026-09-24--two-channel-t3-stop.md).

These records do not prove H1c or H1, promote preliminary localization
prechecks, or alter C2/C3, E0, POWER_13/2_STABILITY, E/AdS, or the flat
manuscript. Physical realization of the two channels remains OPEN.
### 9.7 Physical reconstruction operator norms — 2026-09-24

The initial endpoint-transfer audit is recorded in
[`physical bound-transfer audit`](../reports/2026-09-24--two-channel-physical-bound-transfer-audit.md)
and its first STOP was superseded by the explicit Bob reconstruction norm
estimate in
[`reconstruction operator norms`](../reports/2026-09-24--two-channel-reconstruction-operator-norms.md).
The vector/piece bounds are PRELIMINARY, conditional on the unreviewed
Schur block-stability lemma in §2. The operator norm bound in (1)–(2)
of the report is direct from the defined Bob geometry and does not use
that lemma. For W fixed, `||E^{1/2} V_c P t_N||` and
`||E^{1/2} V_c Q t_N||` are `O_W(N^-1)` in both channels. Consequently
the ten physical pieces have the upper bounds in the linked report:
linear `O_W(N^-1 e^{-K_*N})`, quadratic `O_W(N^-2 e^{-2K_*N})`.
These are upper bounds only; no signed leading term, matching lower
bound, or dominance result is identified. The old `O(N^-6)` remains
untransferred.

## 10. IR spectral-attribution audit — 2026-09-22

User-authorized exploratory audit and commit/push, documented in the
[full report](../reports/2026-09-22--ir-spectral-attribution-audit.md).
Status: **SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC**.
For the fixed sigma2/I pair, N=24 and N=40 pass the stated empirical precision
criterion. Lpp and R=L-Lpp nearly cancel. At N=40, direct nonperiodic
position evolution agrees with the tilted FFT: field discrepancy normalized
by maximum amplitude 1.62e-15; signal relative discrepancy 5.07e-16.
No asymptotic trend, exclusively UV origin, or rigorous numerical enclosure
is claimed. IR admissibility of operations does not by itself prove
predominance of the PP contribution at the exponentially small signal scale.
The stronger spectral attribution remains OPEN. The Sec. 8.20 flat theorem
retains its scope and status; its full proof is not re-certified here.
H1c, E0, POWER_13/2_STABILITY and E/AdS statuses of Sec. 9 are unchanged.
This records completed authorized diagnostics, not authorization for larger scans.

### 10.1 IR spectral-attribution front C1/C2/C3 — gate ledger (2026-09-22)

Explicit user decision on 2026-09-22 to record the certified C1 and C2a
verdicts here. Branch-local, like the rest of this file; `main` is unchanged.
Subsequent user acceptance on the same date promotes C2b after its independent
review and unblocks C2c as a structural-scope gate, without promoting C2c.
Contracts: [C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md),
[C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
[C2b](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md),
[C2c structural scope](../theory/IR_C2C_STRUCTURAL_SCOPE_GATE.md).
The front is fixed to P=Pi'=1_{|p|<=N^-1/2} (hard cutoff), Q=I-P, and the
signed block observable
Lpp=tr(E S^N P Delta P S^-N). This observable is not the conditioned Lcond
of C3.

| Subgate | Status | Evidence |
| --- | --- | --- |
| C1 leakage | **PASS** | [derivation](../reports/2026-09-22--ir-projection-leakage-and-conditioning.md), [independent review](../reports/2026-09-22--c1-leakage-independent-review.md) |
| C2a transfer, sigma2/I | **PASS** | [derivation](../reports/2026-09-22--c2a-oscillatory-transfer.md), [independent review](../reports/2026-09-22--c2a-independent-review.md) |
| C2b block decomposition, sigma2/I | **PASS** | [candidate](../reports/2026-09-22--c2b-block-decomposition-candidate.md), [independent review](../reports/2026-09-22--c2b-independent-review.md); B4_PRIME_PASS separately |
| C2c structural scope | **PASS — C2C_PASS, scope frozen** | [repaired execution](../reports/2026-09-22--c2c-structural-scope.md), [repaired review criteria](../theory/IR_C2C_REPAIRED_REVIEW_CRITERIA.md), [independent review](../reports/2026-09-23--c2c-independent-review.md); 16 original pairs only |
| C3 conditioning | **PASS — C3_PROOF_WRITTEN_REVIEW_ACCEPTED, scope frozen** | [execution](../reports/2026-09-23--c3-conditioning-execution.md), [DeepSeek/Gemini independent review](../reports/2026-09-23--c3-deepseek-gemini-review.md), commit `191ca20`; four original encoders, `M_B=I` only |
| E/AdS | **FROZEN** (STOPPED_UNPROVEN, Sec. 9.5) | unchanged |

- **C1 result:** q_N = ||Q(U_M-I)phi_N||^2 = D N^-5/2 (1+O(N^-1/2)) with
  D = 1024 pi^2 Phi_0(1/4)^2/5 > 0, for all four encoders. It follows that
  ||Delta - P Delta P||_1 = 2 sqrt(D) N^-5/4 (1+O(N^-1/2)).
- **C2a result (sigma2/I):**
  Lpp = N^-3 [C0 + C1 cos(sqrt(N)/2)] + O(N^-13/4), with C0 > C1 > 0 proved
  analytically (no numerical input). Hence Lpp = Theta(N^-3) and Lpp > 0 for
  all sufficiently large N.
- **Earlier consequence of C2a (arithmetic only):** R = L - Lpp = -Lpp + L
  exactly, and Thm 4.1 gives |L| <= 36 N^4 e^{-JN}. The complement of the PP
  block therefore cancels an algebraic Theta(N^-3) response. This establishes
  the cancellation's existence; it is not the proof of C2b below.
- **C2b result (sigma2/I):** direct block decomposition gives
  Lpp = +N^-3 A_N + O(N^-13/4), Lqq = +N^-3 A_N + O(N^-13/4), and
  Lpq + Lqp = -2 N^-3 A_N + O(N^-13/4), with the same
  A_N = C0 + C1 cos(sqrt(N)/2) >= C0-C1 > 0 as C2a.
  Thus the diagonal leaders are positive and the opposite leader lies in
  the coherences. Lqq >= 0 exactly; positivity of Lpp is asymptotic.
  B4_PRIME_PASS additionally gives Lpq = -N^-3 A_N + O(N^-13/4) and
  Lqp = -N^-3 A_N + O(N^-13/4); exactly, Lqp is the complex conjugate
  of Lpq, not necessarily equal to it at finite N.
- **Autonomous mechanism and bounds:** d_Q = d - d_P follows from Q=I-P
  and linearity. Thm 4.1 applies to the local source a, giving
  ||E^(1/2)(d_Q+d_P)|| <= 2 T_N. For every N>=2,
  |Lqq-Q_N| <= 8 T_N + 4 T_N^2 and
  |Lpq+Lqp+Lin_N+2 Q_N| <= 12 T_N, with T_N <= 9 N^4 exp(-JN).
  Here Q_N denotes the quadratic form <d_P,E d_P>, not the projector Q.
  C2a controls this quadratic form and Lin_N separately. No L-Lpp,
  Thm 4.4, total-signal asymptotics or N=24/40 data establish these blocks.

Caveats that must be retained with the C2a PASS:

1. The error term gains only N^-1/4 over the leading term.
2. The asymptotic regime is reached slowly: the oscillatory gains are powers
   of 1/(gamma sqrt(N)), where gamma = sqrt(3) - 3/2, which is about 1.1 at
   N=24 and 1.5 at N=40. The retained N=24/40 values do not validate or
   refute the sign.
3. The PASS is one independent **agent** review (Claude Opus 5). It is not
   an external human verification or a multi-member ratification.

C2b remains a `POST-DISCOVERY VERIFICATION GATE`: its discovery preceded
its contract. The independent review covers exactly snapshot
`19eb7a383cbb09464e91b64e89f724204e58cccb` and returns C2B_PASS and
B4_PRIME_PASS without required repairs. Review artifact SHA256:
`65bab830c6960f2c661ae47d739d90c1ecf8ae06b5f9923383919f76c2b234d5`.
The reviewer is recorded as **Codex, agent `/root`**, distinct from the
candidate's author, Claude Opus 5. This is one independent agent review,
not external human review, multi-member consensus or documented model
diversity. No additional Astra review has been recorded; such a review
remains an optional additional audit before publication, not a condition
retroactively imposed on this internal PASS.

C2c addressed **structural scope**, starting from the mechanism already
proved for sigma2/I: distinguish algebra and localized compensation from
pair-dependent leading coefficients, classify the sixteen original pairs,
and state the hypotheses and limits of any general hard-cutoff result.
The repaired execution makes the detector/espinor transfer explicit, retains
all band crossings, changes the grouping claim to **at most eight families**,
and restricts §9.2 to scalar indicator cuts with the stated open-set and
finite-support hypotheses. An independent review records
`C2C_PASS` for all five S3 levels on all sixteen original pairs, C1, and
§9.2 within that scope. The exponent `N^-3` remains a property of the frozen
`K=sqrt(N)` protocol, not a general QCA law; `N_0` and remainder constants
remain non-effective, and `NOVELTY=OPEN`.

C3 conditioning is now **C3_PROOF_WRITTEN_REVIEW_ACCEPTED** for the four
original encoders with `M_B=I`, the frozen hard cutoff and the same CJWW
protocol. The accepted result is
`Lcond-LPP = D p_infty N^-5/2 (1+o(1))`, with `D>0` and `p_infty>0`.
The result concerns the postselection increment. The leader and absolute
magnitude of `Lcond`, and comparison with the total signal `L`, remain outside
the C3 contract; no broader detector or QCA claim follows.

The C2c promotion is branch-local and does not alter the C3 result, E/AdS or FR1–FR3.
The repaired report and review retain their own commits and hashes; no
finite-N claim or broader detector/QCA class is added.

C3 is PASS in its frozen scope; E/AdS remains FROZEN. H1c, E0,
POWER_13/2_STABILITY and the Sec. 8.20 flat theorem are unchanged. No new
numerical calculation, scan, manuscript publication, commit or push follows
from this update.
```


## Ronda 1 — CLAUDE OPUS

## Versión más fuerte de la cadena

Para que (4) del informe de normas sea una implicación válida hay que leer (6) del informe Schur con cuatro precisiones que el texto no escribe y que son todas disponibles:

(i) los bloques no son operadores en \(L^2\), sino aplicaciones entre los rangos: \(A:\operatorname{ran}P\to\operatorname{ran}P\) en \(\|\cdot\|_2\), \(D:\operatorname{ran}Q\to\operatorname{ran}Q\) en \(\|\cdot\|_*\), \(B:\operatorname{ran}Q\to\operatorname{ran}P\) en \(\|\cdot\|_*\to\|\cdot\|_2\), \(C:\operatorname{ran}P\to\operatorname{ran}Q\) en \(\|\cdot\|_2\to\|\cdot\|_*\); (ii) la equivalencia **bilateral** \(\|y\|_2\le\|y\|_*\le C_0\|y\|_2\), con \(C_0=C_0(W,\rho_1)\) independiente de N, que se sigue de \(h=0\) y de (5) [INFERENCE, a partir de (5) y de la definición de \(\|\cdot\|_*\) — SOURCE]; (iii) la identidad algebraica fibrada \(D_\xi(p)\restriction_{\operatorname{ran}P(p)}=\lambda(p)\,\mathrm{Id}\); (iv) que del multiplicador acotado \(\widehat C_N-I\), \(\|\widehat C_N-I\|\le C/N\), y de \(P(p)D_\xi(p)Q(p)=0\) fibra a fibra, salen \(\|B\|,\|C\|=O(N^{-1})\) *sin* necesidad de controlar \(P(p')Q(p)\) a momentos distintos (los proyectores son multiplicadores; la no localidad está sólo en la moneda) [INFERENCE].

Con (i)–(iv) el paso en \(\nu(x,y)=\|x\|_2+\|y\|_*\) está acotado por \(\max(\|A\|+\|C\|,\ \|B\|+\|D\|)\le 1+C'/N\), la iteración da \(e^{C'}\), y el retorno \(\|t_N\|_2\le\|x_N\|_2+\|y_N\|_2\le\nu_N\) usa sólo \(\|\cdot\|_2\le\|\cdot\|_*\). El dato inicial es \(\nu_0\le(C_P+C_0C_Q)\|s\|_2\) — con \(C_0\), que la fórmula escrita en §2 del informe de normas omite. Obsérvese además que la contracción \(\rho_2<1\) **no** se usa como contracción en el paso: bastaría \(\|D\|_*\le1+C/N\). \(\rho_1<1\) se usa para *construir* \(\|\cdot\|_*\) y para que \(C_0\) exista; conviene no presentarla como el motor de la estabilidad [INFERENCE].

## Punto más débil y objeción

El eslabón que falla tal como está escrito es la última desigualdad de (6): «\(\|A_j\|_2\le1+C/N\). La última desigualdad usa \(|\lambda(p)|/\Lambda\le1\) en W» [SOURCE]. Esa justificación es un ascenso de radio espectral a norma, exactamente el ascenso que el propio informe declara ilegítimo dos párrafos antes, cuando construye \(\|\cdot\|_*\) porque \(\rho\le\rho_0<1\) no le da la cota de potencias en el sector Q («aun donde la matriz exterior sea no normal», (5)) [SOURCE]. En el sector P se usa \(\rho\le1\) como si fuera \(\|\cdot\|\le1\).

Cuantitativamente: \(A_j=P\widehat C_N\Lambda^{-1}D_\xi P\), y su parte libre es el multiplicador \((\lambda(p)/\Lambda)P(p)\), cuya norma \(L^2\to L^2\) es \(\operatorname{ess\,sup}_{p\in W}\frac{|\lambda(p)|}{\Lambda}\|P(p)\|\ge1\). \(P(p)\) es el idempotente de Riesz, del que T1 dice expresamente «No se presupone \(P^*=P\)» [SOURCE]; \(S(-i\xi)\) es hermítica sólo en \(\eta=0\) (lem:symbol(a)) [SOURCE], luego para \(\eta\ne0\) nada del acta acota \(\|P(\eta)\|\) por 1. Si se lee (6) en la norma en que está escrita, la iteración produce \(\kappa_P(W)^N\) con \(\kappa_P(W)=\operatorname{ess\,sup}_W(|\lambda|/\Lambda)\|P\|\), y cualquier \(\kappa_P>1\) destruye (4): con la cota bruta \(\|t_N\|\le2e^{(3t_*-\Phi_*)N}\), \(3t_*-\Phi_*\approx0.83>0\) [INFERENCE sobre los valores \(t_*=0.7357\ldots\), \(e^{\Phi_*}=3.97314\ldots\), \(\|S(\eta-i\xi_*)\|\le4e^{3t_*}\), todos SOURCE], el enunciado \(\|t_N\|=O(1)\) es precisamente lo que hay que ganar frente a un crecimiento exponencial admisible; no es un detalle de constantes.

Dos observaciones que cierran las salidas fáciles. Primera: **encoger W no arregla nada**. Cerca de un saddle, \(|\lambda(\eta)|/\Lambda=\exp(-\tfrac12\eta^\top Q\eta+O(|\eta|^3))\) (lem:symbol(d)) [SOURCE] y, como el ángulo entre autovectores derecho e izquierdo es \(O(|\eta|)\), \(\|P(\eta)\|=1+a(\eta)+O(|\eta|^3)\) con \(a\) cuadrática y \(\ge0\) [INFERENCE]. Ambos términos son homogéneos de grado 2: el signo de \(a(\eta)-\tfrac12\eta^\top Q\eta\) no cambia al reducir el radio de la ventana. Nadie en el acta ha comparado esas dos formas cuadráticas [ABSENCE: busqué en el informe Schur §2, en T1 §2 y en lem:symbol(d) una cota de \(\|P(\eta)\|\); sólo aparece \(\|P(\eta)-P\|\le c_P|\eta|\), que da \(\|P(\eta)\|\le1+c_P|\eta|\), insuficiente]. No afirmo \(\kappa_P>1\); afirmo que \(\kappa_P\le1\) no está probado y que el texto lo usa. Segunda: **en el sector P no hay sustituto genérico del truco de (5)**. Allí \(\rho=1\) exactamente en los ocho saddles, así que no existe circunferencia \(\rho_1<1\) que encierre el espectro y la fórmula de Cauchy no da nada. La cota tiene que venir de estructura, no de resolvente.

La reparación existe y es de dos líneas. En W, \(\operatorname{ran}P(p)\) es el autoespacio de dimensión dos de \(D_\xi(p)\) para \(\lambda(p)\): en el bloque 1, \(p_SSp_S=\lambda p_S\); en el bloque 2, el rango de \(I_2-p_S\) es el autoespacio de \(\lambda^{-1}\) de \(S\), que es el de \(\lambda\) de \(S^{-1}\) [INFERENCE a partir de (3) y de «\(S^{-1}\) tiene autovalor \(\lambda\) en el subespacio de \(S\) con autovalor \(\lambda^{-1}\)», SOURCE]. Por tanto, **para \(x\in\operatorname{ran}P\)**, \(\Lambda^{-1}D_\xi x=(\lambda/\Lambda)x\) puntualmente, el bloque libre P es multiplicación por un escalar de módulo \(\le1\), y \(\|A_j\restriction_{\operatorname{ran}P}\|_2\le1+C_P\|\widehat C_N-I\|\,\|\Lambda^{-1}D_\xi\|\le1+C/N\) [ORIGINAL en su formulación; los tres ingredientes son SOURCE]. La misma identidad da \(PD_\xi Q=QD_\xi P=0\), es decir, el mecanismo de \(O(N^{-1})\) en los bloques cruzados. Es decir: el hecho que salva (6) es el mismo que la hace no trivial, y no está escrito.

**Condición de concesión.** Retiro la objeción si el informe Schur (a) reformula (6) como cotas de los bloques restringidos a los rangos, con las cuatro normas mixtas explícitas; (b) añade \(\|y\|_2\le\|y\|_*\le C_0\|y\|_2\) con \(C_0\) independiente de N; (c) sustituye «usa \(|\lambda|/\Lambda\le1\)» por la identidad \(D_\xi\restriction_{\operatorname{ran}P}=\lambda\,\mathrm{Id}\) y deduce de ahí la norma; (d) corrige \(\nu_0\) incluyendo \(C_0\). Si en cambio se mantiene la lectura \(L^2\to L^2\) de \(A_j\), entonces (4) exige probar \(\kappa_P(W)\le1\), y sin eso el paso primero que falla es \(\|A_j\|\le1+C/N\), con \(\|t_N\|=O_W(1)\) no establecido.

## Lo que concedo sin condiciones

Los enunciados 1, 2 y 3 pasan, y pasan **sin depender de Schur**. (1): en Alice, \(\hat u\cdot x\le|x|\le R\) da \(\xi_*\cdot(x-x_*)\le0\), \(J\) es isometría, \(\operatorname{supp}(U_M-I)\subset\mathcal A_N\), luego \(\|s\|=\|H_\xi f\|\le\|f\|\le2\) [INFERENCE]. (2): la igualdad \(\|E^{1/2}\mathcal V_c\|=m_N\) es correcta y el testigo es explícito — \(z=\mathcal F(\delta_{y_{\max}}\otimes\chi)\) embebido en el canal \(c\), con \(\chi\) autovector de autovalor 1 de \(M_B\) (los cuatro \(M_B\) son proyectores); el supremo se alcanza porque \(\mathcal B_N\) es finito. La descomposición \(y-Nu=(s-R)\hat u+q\) da \(\sqrt{h_N}\le2s/R-s^2/R^2\le2s/R\) y \(m_N\le2/(e\lambda R)=8/(e\sqrt3t_*)N^{-1}\). El \(\Theta(N^{-1})\) es correcto: el intervalo \(m-(y_*)_1\in[1,2]\) contiene un entero para todo N, allí \(q=0\), \(\sqrt{h_N}\ge c/N\) y \(e^{-\lambda s}\ge e^{-2\sqrt3\lambda}\) [INFERENCE]. (3): \(C_P(W),C_Q(W)<\infty\) por (3a) sobre los ocho cierres compactos, independientes de N porque el símbolo no depende de N; \(\|E^{1/2}\mathcal V_cP\|\le C_Pm_N\) es trivial. Estas cotas son geométricas y no heredan el nivel Schur, como el informe ya dice.

Sobre (5) del informe Schur añado, a favor: la cota uniforme del resolvente no necesita compacidad ni continuidad en \(p\) — en dimensión 4 por fibra, \(\|(z-M)^{-1}\|\le\|\mathrm{adj}(z-M)\|/\prod_i|z-\mu_i|\), acotado uniformemente si \(\|M\|\le C\) y \(\rho(M)\le\rho_0<\rho_1\); el salto en \(\partial W\) es de medida nula e irrelevante para un ess-sup [INFERENCE]. Y \(\rho(Q D_\xi Q)\restriction_{\operatorname{ran}Q}=|\lambda|^{-1}/\Lambda\le1/((1+c)\Lambda)\) en W, con \(\Lambda=3.973\ldots>1\) [INFERENCE].

## Calibración y veredicto

Un límite de alcance que ningún informe cuantifica: aun concedida toda la cadena, \(|A_{cP}|=O_W(N^{-1}e^{-K_*N})\) es \(N^{11/2}\) **mayor** que la única escala líder conocida en la clase plana, \(N^{-13/2}e^{-K_*N}\) (thm:main) [INFERENCE sobre SOURCE]. La cadena por tanto no puede decidir dominancia, cancelación ni no anulación de ninguna de las diez piezas, ni comparar con el techo viejo \(O(N^{-6})\). Sólo son cotas superiores, sin \(\sim\), sin lower bound y sin término firmado líder; suscribo esa autorrestricción del informe.

Veredicto: **REPAIR_REQUIRED**, con reparación disponible y acotada. Premisa crítica: \(\|A_j\|\le1+C/N\) como cota de **norma** (no de radio espectral) del bloque P. Alcance del pase parcial: enunciados 1–3 PASS, incondicional y separable de Schur; enunciado 4 condicionado a (a)–(d); enunciado 5 correcto *dado* 4 y con el factor \(e^{-K_*N}\) exacto (verifiqué \(\Lambda^{-N}e^{\xi_*\cdot(y_*-x_*)}=e^{-K_*N}\)), heredando el rótulo `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.

