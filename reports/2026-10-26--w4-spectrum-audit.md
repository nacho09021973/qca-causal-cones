# W4: auditoría del espectro completo, las unidades y el observable

Fecha: 2026-10-26. Autor: Codex. Base de trabajo: `800cafd8cd6b119a8ac69219e64a915d38a92d2a`.
Autorización directa: auditar W4, convertir las comprobaciones manuales en
verificaciones permanentes y preparar después una revisión independiente.
Estado: `AUTHOR_CHECKED / INDEPENDENT_REVIEW_PREPARED_NOT_SENT`.

## 1. Alcance y resultado

Se audita exclusivamente la reducción 1D de un defecto sobre el vacío
polarizado, con la puerta original `K(kappa)=exp[-i kappa (I-SWAP)]` y dos
matchings sucesivos. El segundo matching tiene el mismo ángulo o el inverso;
este último sigue siendo un control, no un reemplazo del modelo canónico.

La conclusión histórica `SMOOTH_MODE_GAPPED / STAGGERED_GAPLESS_ONLY` no
describe el espectro completo referido al vacío fijo. El paso original tiene
una rama que vale cero en k=0 y es cuadrática para kappa fijo en (0, pi/2).
El control de ángulos opuestos tiene un cruce lineal en k=0. La pendiente
`|sin(kappa)|` usa celdas de dos registros y pasos completos de dos capas.
En registros vecinos por paso completo es `2|sin(kappa)|`.

El espectro es de amplitudes. Por sí solo no prueba una onda lineal del
control z=<Z>, ni una onda del métrico. La regla microscópica de Z depende
también de coherencias. La descripción actual de este gate queda como
`OPEN_AFTER_AUDIT`, con estas comprobaciones locales PASS y la interpretación
corregida pendiente de revisión independiente. W1–W12 sigue CLOSED_BY_CONTRACT.

Se consultó `biblioteca/INDICE.md` antes de trabajar. Esta auditoría no usa
papers como prueba ni hace afirmaciones de novedad: deriva las identidades
desde las puertas del contrato y conserva todo el código que las verifica.
El informe previo de reconstrucción localiza los errores; no es evidencia
independiente del cálculo nuevo.

## 2. Convenciones y fase respecto al vacío

Sea A_m el registro 2m y B_m el 2m+1. El primer matching une A_m con B_m;
el segundo une B_m con A_(m+1). Se usa psi_(A/B,m)=exp(ikm) u_(A/B) y el
paso U=K_odd K_even. Un autovalor se escribe exp(-i epsilon); epsilon se
entiende módulo 2pi, con la rama local indicada en cada expansión.

Con c=cos(kappa), s=sin(kappa), las matrices sin fase son

\[
A=\begin{pmatrix}c&is\\is&c\end{pmatrix},\qquad
B_\sigma=\begin{pmatrix}c&\sigma is e^{-ik}\\
\sigma is e^{ik}&c\end{pmatrix},\qquad \sigma=\pm1.
\]

En el par vacío, K|00>=|00>. En el subespacio de un defecto del enlace,
K=e^(-i kappa) A. Cada matching contiene un único enlace ocupado en el
sector de un defecto; todos los otros enlaces son pares vacíos fijos. Así,

\[
U_{\sigma,\mathrm{full}}(k)
=e^{-i(1+\sigma)\kappa}B_\sigma A,\qquad
\frac12\operatorname{tr}(B_\sigma A)=c^2-\sigma s^2\cos k.
\]

El determinante de B_sigma A es uno; el del paso completo es
exp[-2i(1+sigma)kappa]. La fase retirada es común dentro del sector de un
defecto, pero no al vacío. Retirarla no cambia velocidades de grupo,
degeneraciones entre bandas ni expectativas de Z dentro del sector. Sí
cambia qué autovalor coincide con el del vacío. No se infiere que Z sea un
detector de esa fase relativa: Z no conecta ambos sectores.

El certificado simbólico comprueba el generador, la unitariedad, el vacío,
la restricción de la puerta de dos qubits, las trazas y los determinantes.
Como segunda vía, el certificado de observables construye el circuito
completo de 2^L estados desde permutaciones de bits, y sólo después lo
proyecta al sector de un defecto y a los momentos de Bloch. No fabrica ese
circuito desde el símbolo que se pretende comprobar.

## 3. Ramas y excepciones

### Mismo signo

En k=0, el vector simétrico (1,1) tiene autovalor 1 del paso completo; el
antisimétrico tiene exp(-4i kappa). Además, el estado uniforme de un defecto
es invariante bajo cada SWAP y, por tanto, bajo cada K. Es una segunda prueba
del cero uniforme que no depende del cálculo de la traza. En cadena infinita
es un modo de Bloch generalizado; en cada anillo finito es normalizable.

Para kappa fijo en (0,pi/2), sea omega_+(0)=2 kappa y
cos omega_+=c²-s² cos k. La rama relativa al vacío es

\[
\epsilon_{\rm unif}(k)=2\kappa-\omega_+(k)
=\frac{\tan\kappa}{4}k^2+O(k^4).
\]

La prueba usa F(epsilon,k)=cos(2kappa-epsilon)-(c²-s² cos k).
En (0,0), F_epsilon=sin(2kappa) no se anula, F_k=0 y F_kk=-s².
El teorema de función implícita da una rama analítica, única localmente y
par en k, con epsilon''(0)=s²/sin(2kappa)=tan(kappa)/2. El código verifica
estas identidades y contrasta el coeficiente sustituyendo
lambda=1-i tan(kappa) k²/4 en el polinomio característico completo hasta
orden dos. El resto O(k^4) usa la paridad y analiticidad recién indicadas;
no se obtiene de una extrapolación de anillos pequeños.

En k=pi, el paso completo es exp(-2i kappa) I: el cruce está centrado en
epsilon=2kappa módulo 2pi, no en cero respecto al vacío para este intervalo.
Cada rama se separa del centro con pendiente de magnitud |s|; la separación
entre las dos ramas es 2|s||q|+O(|q|³), igual que en el símbolo sin fase.
Conviene distinguir «cruce entre bandas» de «excitación de cuasienergía
cero respecto al vacío».

### Ángulos opuestos

Las fases se cancelan, U_-(0)=I y

\[
\sin^2\frac{\omega_-(k)}2=s^2\sin^2\frac{k}2,\qquad
\omega_-(k)=2\arcsin\bigl(|s|\,|\sin(k/2)|\bigr)
=|s|\,|k|+O(|k|^3).
\]

Esta es la rama no negativa próxima a cero; los autovalores son exp(±i omega_-).
Para derivar las pendientes se usa la rama con signo 2 asin(v sin(k/2)),
v=|s| en [0,1]. Sus términos primero y cúbico son v k y
v(v²-1) k³/24. Se necesita s distinto de cero para una pendiente no nula.

### Extremos

En kappa=0 y pi ambas construcciones son identidad. En kappa=pi/2, K es
SWAP tanto para el ángulo positivo como para el negativo, y ambos pasos son
diag(exp(-ik),exp(ik)). Hay ramas lineales en ese extremo: la expansión
cuadrática para kappa fijo en el intervalo abierto no es uniforme al acercarse
a pi/2. No se extrapola a ese punto. Todos estos límites se verifican exactamente.

## 4. Unidades y comprobación por transporte

Si a es la distancia entre registros y tau el tiempo del paso completo,
la longitud de celda es 2a, k=2a p y la frecuencia física es epsilon/tau.
Por la regla de la cadena,

\[
v_{\rm grp}=\frac{2a}{\tau}\frac{d\epsilon}{dk},\qquad
|v_{\rm IR,control}|=\frac{2a}{\tau}|\sin\kappa|.
\]

La última expresión es la pendiente del cruce del control 1D, no una igualdad
general entre velocidad IR, velocidad máxima de grupo y soporte causal.
En el caso SWAP se sigue exactamente A_m a A_(m+1) y B_m a B_(m-1): son
dos registros por paso de dos capas. Se comprueban los desplazamientos
orientados en anillos L=4,6; L=6 distingue +2 de -2 módulo L. Si se asigna
un tiempo a cada capa, tau es dos veces ese tiempo; no se mezcla con un paso.

## 5. Observable Z: qué se deriva y qué falta

En vacío más un defecto, Z_n es diagonal: -1 si el defecto está en n y +1
en los demás estados, incluido el vacío. Para un vector b no nulo de ese
subespacio,

\[
\langle Z_n\rangle=1-2\frac{|b_n|^2}{\|b\|^2},
\]

donde b_n es la amplitud del defecto en n y la norma incluye el vacío.
En el sector de un defecto normalizado se reduce a 1-2|psi_n|². La identidad
se verifica con amplitudes simbólicas arbitrarias, proyectando los Z físicos.
Una onda de Bloch pura tiene densidad constante de celda a celda, aunque sus
dos subredes puedan tener densidades diferentes. El momento de las amplitudes
no se convierte automáticamente en un momento de la expectativa de Z.

Contraejemplo retenido: en L=4, psi_n=(-1)^floor(n/2)/2 tiene k=pi por celda
y Z_n=1/2 en todos los registros. En kappa=pi/4 es un autoestado del paso
completo para ambos controles (autovalores -i e i respectivamente). Su Z
es uniforme y estacionario. El estado uniforme psi_n=1/2 es ortogonal y
produce el mismo Z. Queda refutada la inferencia «fase k=pi implica Z alternante».

Para (|vac>+epsilon|psi>)/sqrt(1+epsilon²), con psi normalizado, el cambio
de Z empieza en epsilon²; la derivada primera en cero se anula. La misma
identidad vale después de cualquier número de pasos, porque el vacío se fija
y el sector de un defecto se conserva. El código verifica la identidad
general y un paso explícito. No es un no-go para otros fondos, observables
transversales, mezclas de densidad pequeña o sectores con varios defectos.

Además, los estados de enlace (1,i)/sqrt(2) y (1,-i)/sqrt(2) tienen las
mismas densidades iniciales y dan Z opuestos tras K(pi/4). En la base
computacional restringida a los estados 1 y 2, se usa el Z del registro 1,
diag(1,-1), y se obtienen -1 y +1. El contraejemplo también se comprueba
para el paso completo de dos capas en L=4: ambos perfiles iniciales son
(0,0,1,1), mientras los finales son (1,0,0,1) y (0,1,1,0). Esto impide
deducir una actualización cerrada de Z para estados arbitrarios sólo desde
el perfil inicial de Z.
No niega el transporte de densidades ni el testigo discreto de curvatura
W4 previamente acotado; tampoco establece una ecuación de onda del métrico.

## 6. Verificaciones permanentes y reproducibilidad

| Artefacto | Comprobación | Límite |
| --- | --- | --- |
| `scripts/verify_w4_long_wavelength_spectrum.py` | 7 bloques: puerta, símbolos completos, nodos, rama cuadrática, control lineal, extremos, unidades | Argumentos de rama y resto analítico explicitados arriba; no espectro 3D |
| `scripts/verify_w4_spectrum_observables.py` | 6 bloques: dos anillos, identidad Z, contraejemplo k=pi, respuesta cuadrática y falta de cierre de densidad | 12 circuitos exactos: L=4,6; kappa=0,pi/4,pi/2; dos signos; todos los momentos permitidos en cada anillo |

Los anillos son una segunda formulación y controles finitos, no revisión
independiente ni prueba por extrapolación. No hay coma flotante ni ajuste.
Las entradas algebraicas de las matrices finitas se expanden exactamente
antes de usar `assert_sym_equal`, evitando falsas negativas del normalizador
trigonométrico sobre productos complejos no expandidos. No se cambió el helper
compartido ni se omitieron controles de unitariedad.

Comandos desde la raíz:

```sh
python3 -B scripts/verify_w4_long_wavelength_spectrum.py
python3 -B scripts/verify_w4_spectrum_observables.py
python3 -B scripts/run_all_verifiers.py --output reports/2026-10-26--w4-audit-verifier-sweep.tsv
sha256sum -c reports/2026-10-26--w4-audit-verifier-inputs.sha256
python3 -B scripts/text_integrity.py --check
git diff --check
```

Resultado local final: **43 verificadores, cero fallos**; los dos certificados
de esta auditoría pasan sus 13 bloques. Las huellas de los scripts coinciden
con el manifiesto. El barrido y el manifiesto de entradas se conservan junto
a este informe. El HEAD del barrido identifica la base; el manifiesto identifica los bytes de
los certificados ejecutados y el helper, incluidos los cambios sobre esa base.
La reconstrucción y la revisión anteriores de W4 no revisaron estos bytes
ni esta interpretación del espectro completo.

## 7. Expediente independiente preparado

En `debates/2026-10-26--w4-spectrum-review-deepseek/` quedan el encargo, el
manifiesto y la entrada sellada para DeepSeek, familia distinta de la del
autor. Se prepara con `revision-ciega` del PATH en modo
`REVISION_SOLO_ENTRADA=1`: no se envía texto ni se ejecuta al revisor.
Herramienta inspeccionada: `~/herramientas` en
`d32e8507c32aefc0acd0721a000eeeb2a261d824`.

El encargo fija una ronda, pide atacar las hipótesis y fórmulas, exige
rederivaciones y separa el juicio matemático del significado físico. Termina
con ACCEPT, ACCEPT_WITH_REPAIRS o REJECT/INCONCLUSIVE y una lista numerada de
objeciones; una respuesta truncada o con llamadas simuladas no cuenta como
informe. Una futura respuesta debe contrastarse localmente antes de cambiar
evidencia o estado. Preparar el paquete no equivale a haber recibido revisión.
