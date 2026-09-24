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
