# SCALED_IR_SIGNALING_GATE — ejecución del contrato publicado

Registro de ejecución, 2026-09-17. Evaluación del autor; sin revisión
independiente ni promoción canónica. [A] identifica pruebas analíticas;
[V] identifica exclusivamente identidades comprobadas por el certificado.
El orden de ejecución es geometría/carta, admisibilidad, upper bound,
análisis de los dieciséis pares, clasificación.

**Resultado: `OPEN_AFTER_SCALED_IR_ANALYSIS`.** Admisibilidad IR demostrada
para las ocho operaciones; upper bound direccional exponencial demostrada;
positividad o nulidad de las dieciséis señales no resuelta. Certificado
auxiliar: **53/53 identidades**, sin cobertura software de la prueba completa.

## 1. Preflight

- Repositorio: `nacho09021973/qca-causal-cones`.
- Rama: `research/b-infinity-post-s4-gate`.
- `HEAD`, `refs/remotes/origin/research/b-infinity-post-s4-gate` y consulta
  efectiva `git ls-remote origin refs/heads/research/b-infinity-post-s4-gate`:
  `31b5797119a9aad03b11c5ee00db99e0d96ed9e4`, idénticos al baseline exigido.
  La consulta remota se repitió fuera del sandbox tras un fallo DNS.
- SHA256 de `theory/SCALED_IR_SIGNALING_GATE.md`:
  `325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c`.
- Ningún cambio tracked inicial, ni staged ni unstaged.
- Cuatro entradas untracked preexistentes, preservadas:
  `Auditoría De Novedad Matemática.md`,
  `debates/2026-09-15--1100--siguiente-gate-b-infinito-post-s4.log`,
  `debates/2026-09-16--ratificacion-gate-completitud-axial-n3.log`,
  `scripts/__pycache__/` (dos `.pyc`). Todo Python se ejecuta con `-B`.
- SHA256 inicial de `state/CURRENT_STATE.md`:
  `7cb84de881b4a03b751842ef4f46a1bf10f54a1c6fd468c6029cfa5acf791098`.

Leídos íntegramente antes del cálculo: el charter escalado, el charter
narrow-band, `CURRENT_STATE`, `OPERATIONAL_INVISIBILITY_GATE`,
`COUPLING_MAP_SIGNALING_WITNESS`, `ALICE_LOCAL_PREPARATION_WITNESS`,
`NONCORNER_SIGNALING_GATE`, el informe de ejecución narrow-band y los scripts
`verify_directional_saturation.py`, `verify_signaling_witness.py`,
`verify_narrow_band_gate.py`, `verify_weyl_dirac_gate.py`; además las reglas
del proyecto y `scripts/README.md`. Las referencias bibliográficas a otros
walks son motivación solamente; no se transfieren sus propiedades.

La lógica terminal se reconstruyó antes de calcular, en el orden de §7:
ninguna Pauli admisible; obstrucción exacta de toda la familia incluido `I`;
lower bound polinómica de una Pauli; lower bound exponencial/asintótica no
nula y upper exponencial de una Pauli; en cualquier otro caso `OPEN`.
Una cota débil de admisibilidad no activa el primer estado. El control `I`
nunca establece por sí solo un estado positivo.

## 2. Geometría [A]

Se conservan exactamente `N` entero, `N>=2`, `Lambda=1/N`,
`Lambda'=1/sqrt(N)`, `Delta T=N`, y las bolas **euclídeas**

\[
A_N=\mathbb Z^3\cap\overline B_2(0,N/4),\qquad
B_N=\mathbb Z^3\cap\overline B_2(N(1,1,1),N/4).
\]

Para **cada** par `x` en Alice, `y` en Bob, la desigualdad triangular da

\[
|y-x|_2-N\ge(\sqrt3-3/2)N>N/5.
\]

La última desigualdad es exacta: `3>(17/10)^2`. También
`dist(A_N,B_N)-N <= (sqrt3-1)N`, tomando los centros, que son sitios de red.
Por tanto el margen es `Theta(N)`, en particular `O(N)`. Los centros sólo
se usan para esta cota superior; la separación inferior cubre las regiones
completas. Con `u=(1,1,1)` se obtiene asimismo

\[
u\cdot(y-x)\ge(3-\sqrt3/2)N. \tag{G}
\]

Los bloques de Laurent heredados son
`W_(1,1,1)=diag(1/4,0)` y `W_(-1,-1,-1)=diag(0,1/4)`.
Para llegar a un vértice en `N` pasos cada paso debe ser ese mismo vértice:

\[
K_N((N,N,N),0)=4^{-N}\operatorname{diag}(1,0)\ne0,
\quad (S^N)_{(N,N,N),0}=4^{-N}\operatorname{diag}(0,1)\ne0.
\]

Así se certifica tanto el candidato literal del charter como el sentido de
propagación de estados. Ese par pertenece a las dos regiones y al soporte
exacto microscópico, en su frontera. No se afirma que todos los pares sean
microscópicamente accesibles: algunos desplazamientos quedan fuera de
`[-N,N]^3` y tienen kernel exactamente cero.

## 3. Carta y dominio analítico [A]

Se usa el símbolo literal `walk2()`, con `S(p)=W(p)^{-1}` y
`f(p)=tr S(p)/2=cos(p1)cos(p2)cos(p3)`, `det S=1`.
La inversión, y no la conjugación antiholomorfa, define la continuación
compleja. Tanto `W` como `S=adj W` son polinomios trigonométricos enteros.

En el toro real las colisiones de eigenvalores exigen `f=+1` o `f=-1`;
esto ocurre sólo cuando cada coordenada está en `pi Z`, módulo `2pi`.
En la bola `|p|<pi/4` sólo queda el nodo `p=0`, donde `W=I`.
Todos los cosenos son positivos y `0<f<=1`; por tanto no hay eigenvalor
`-1` ni corte del logaritmo principal. Las dos bandas se conservan; los
proyectores individuales pueden ser singulares en el nodo, pero el
logaritmo matricial es regular allí. `1/sqrt(N)<=1/sqrt2<pi/4` para `N>=2`
(basta `pi>3>2sqrt2`), así que ambas bandas del contrato están en la carta.

La expansión directa es `W=I+iH_W+O(|p|^2)`,
`H_W=p1 sigma1-p2 sigma2+p3 sigma3`, `H_W^2=|p|^2 I`.
La continuación de potencias usará el símbolo entero en el tubo entre el
toro real y su desplazamiento complejo, sin exigir una rama global de
`arccos(f)`. Las colisiones complejas `f^2=1` no son polos de `S^N`;
deben tratarse sin dividir por la separación de eigenvalores.

La normalización, por integración radial exacta, es

\[
Z_N=\frac{64}{3465\pi^2 N^3},\qquad
\int g(Np)d\mu=\frac4{105\pi^2N^3},\qquad
|\phi_N(0)|^2=\frac{11}{140\pi^2N^3}.
\]

**Geometría y carta: PASS.** No se detecta aquí una inconsistencia que
active la parada. La carta local no se usa como sustituto del control del
toro complejo completo requerido para una upper bound de propagación.

## 4. Admisibilidad IR [A]

Escribimos `F_N(x)=(1-16|x|^2/N^2)^2_+` y
`a_M(x)=exp(i pi F_N(x) M/2)-I`. Cada `M` es una involución hermítica.
El perfil extendido por cero es globalmente Lipschitz, con constante
`16/N`: dentro de la bola, `|grad F_N|=64|x|(1-16|x|^2/N^2)/N^2<=16/N`,
y la derivada se anula en la frontera. En consecuencia
`||a_M||_infty<=2`, `Lip(a_M)<=8pi/N`. Para `h_B M_B`, las constantes son
`1` y `16/N`, ya que los cuatro `M_B` tienen norma uno.

### 4.1 Cotas de operador, uniformes en toda la banda de entrada

Sea `D_j xi(x)=xi(x+e_j)-xi(x)`. Por Plancherel y
`sin(t)>=2t/pi` para `0<=t<=pi/2`,

\[
\|(I-\Pi')\xi\|\le\frac{\pi}{2\Lambda'}
 \Big(\sum_j\|D_j\xi\|^2\Big)^{1/2}.
\]

Si `Pi psi=psi`, entonces `||D psi||<=Lambda ||psi||`. La regla de
producto discreta y Minkowski dan, para un multiplicador de norma `A`
y constante Lipschitz `L/N`,

\[
\|(I-\Pi')a\Pi\|\le\frac\pi2(A+\sqrt3 L)N^{-1/2}.
\tag{IR1}
\]

Definimos las constantes explícitas

\[
K_e=\frac\pi2(2+8\sqrt3\pi),\qquad
K_d=\frac\pi2(1+16\sqrt3).
\]

Esta prueba controla las operaciones completas sobre cualquier vector en
la banda de entrada; no descompone ni proyecta la señal de Bob.

### 4.2 Denominadores no nulos y uniformemente separados de cero

La componente escalar real `b_N` de `phi_N=b_N down` satisface, para
`|x|<=N`,

\[
b_N(x)=Z_N^{-1/2}\int g(Np)\cos(p\cdot x)d\mu
\ge\tfrac12\sqrt{11/(140\pi^2)}\,N^{-3/2}.
\]

Se usó `cos t>=1-t^2/2>=1/2` para `|t|<=1`. Para `N>=32`, tomamos
únicamente como conjuntos auxiliares de prueba, sin cambiar las regiones:

- `Q_in={|x_j|<=N/32}`: al menos `(N/32)^3` sitios,
  `F_N >= (61/64)^2 > 1/2`.
- `Q_out={N/2<=x1<=5N/8, 0<=x2,x3<=N/8}`: al menos `(N/16)^3`
  sitios, `F_N=0`, `|x|<N`.

Ambos tienen probabilidad al menos

\[
m=\frac{11}{560\pi^2\,32^3}>0.
\]

En `Q_in`, `theta F_N` pertenece a `[pi/4,pi/2]`. Por tanto, para las
cuatro `M`, `a_M^*a_M=2(1-cos(theta F_N))I` y

\[
\|a_M\Pi\|\ge b_e:=\sqrt{(2-\sqrt2)m}>0.
\]

Para el detector, se puede probar la norma de operador sobre el mismo
paquete **trasladado** al centro de Bob, con un autovector de eigenvalor
uno de `M_B`. Es sólo un vector de prueba para la norma, no un cambio del
recurso físico. Su soporte espectral sigue en `Pi`. Así

\[
\|(h_B\otimes M_B)\Pi\|\ge b_d:=\sqrt m/2>0.
\]

Con `w_x=|b_N(x)|^2`, `t_x=<down|U_M(x)|down>` y `z=sum_x w_x t_x`,
se tiene `|t_x|<=1`. Para un punto de `Q_in` y otro de `Q_out`,
`Re(t_x conjugate(t_y))=cos(theta F_N(x))<=1/sqrt2`. Para todos los
otros pares, esa parte real es como máximo uno. Sumando las dos
orientaciones de esos pares se obtiene

\[
1-|z|^2\ge(2-\sqrt2)m^2,\qquad
\|\Delta_M\|_1=2\sqrt{1-|z|^2}\ge d_e:=2m\sqrt{2-\sqrt2}>0.
\tag{IR2}
\]

Esto cubre separadamente `t_x=e^{i theta F_N}` para `I`,
`t_x=cos(theta F_N)` para `sigma1,sigma2`, y
`t_x=e^{-i theta F_N}` para `sigma3`; no invoca simetría del protocolo.
Para los finitos `2<=N<32`, el origen tiene peso positivo y fase distinta
de cero y hay un punto exterior de peso positivo con `|x|<=N`; por ejemplo
`x=(floor(N/4)+1,0,0)`. El mismo argumento prueba denominadores no nulos,
sin necesitar las constantes uniformes anteriores.

### 4.3 Norma de traza y tabla completa

Para `v=U_M phi_N`, `w=Pi' v`, `r=v-w`, se tiene
`Delta_M-Pi' Delta_M Pi'=|v><v|-|w><w|`, porque `Pi' phi_N=phi_N`.
La identidad `|v><v|-|w><w|=|r><v|+|w><r|` da norma de traza `<=2||r||`.
Por (IR1), `||r||<=K_e/sqrt N`, de donde, para `N>=32`,

| Operación | Cota relativa explícita | Límite | Admisibilidad |
| --- | --- | --- | --- |
| Encoder `I` (`REFERENCE_CONTROL`) | `eta_op<=K_e/(b_e sqrt N)`; `eta_enc<=2K_e/(d_e sqrt N)` | ambos 0 | PASS |
| Encoder `sigma1` | mismas dos cotas, demostradas con `M^2=I` | ambos 0 | PASS |
| Encoder `sigma2` | mismas dos cotas, demostradas con `M^2=I` | ambos 0 | PASS |
| Encoder `sigma3` | mismas dos cotas; actúa como fase sobre `down` al elegir | ambos 0 | PASS |
| Detector `I` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma1)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma2)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |
| Detector `(I+sigma3)/2` | `eta_read<=K_d/(b_d sqrt N)` | 0 | PASS |

Las constantes son conservadoras, no ajustadas numéricamente. Las cotas
son asintóticas explícitas y no aseguran un pequeño error para `N=2`.
La tabla cubre las familias congeladas y no todos los generadores internos
ni todos los efectos locales posibles.

### 4.4 Sanity check puntual

Sea `kappa'=1/(6pi^2 N^(3/2))`, medida de la bola de radio `Lambda'`.
Para cualquier vector de un sitio, la fracción de norma cuadrada dentro
de `Pi'` es exactamente `kappa'`. Por tanto, con entrada `Pi`,

\[
\eta_{enc,op}^{point}=\eta_{read}^{point}=\sqrt{1-\kappa'}\longrightarrow1.
\]

Para la puerta `I-2P_0`, la reducción de Gram del gate anterior se aplica
con `Pi'` porque `Pi' psi=psi`. Con `s=||P_0 psi||^2`,

\[
\eta_{enc}^{point\,2}=
\frac{(1-\kappa')[1-3s(1-\kappa')]}{1-s}\longrightarrow1.
\]

Vale para el recurso actual (`s=11/(140pi^2 N^3)`) y para el recurso
puntual anterior `psi=S^2 phi_N`: por su prueba congelada,
`cos^2(2/N) 11/(140pi^2N^3)<=s<=11/(140pi^2N^3)`. En ambos casos
`0<s<=kappa'`, con denominador positivo. Así, el sanity check prueba
literalmente la persistencia del negativo puntual con las dos escalas.

## 5. Stop rule

**Admisibilidad: PASS. Sanity check: PASS. Stop rule: NO ACTIVADA.**
Las tres Pauli y el control pasan. Se continúa con los dieciséis pares.
No se ha evaluado aún señal alguna para obtener este resultado.

## 6. Upper bound geométrica: derivación direccional [A]

Esta prueba es independiente de los encoders, detectores y recurso
concretos. No usa la LDP radial ni su maximización numérica.

### 6.1 Lema de producto de elipses

Para `a>1` escribimos
`E_a={z: (Re z)^2/a^2+(Im z)^2/(a^2-1)<=1}`. Entonces

\[
E_a E_c\subset E_{ac},\qquad a,c>1. \tag{E}
\]

Prueba explícita. Basta fijar un punto de la frontera del primer factor,
`z=a cos p+i sqrt(a^2-1) sin p`; los puntos interiores son contracciones
radiales de éstos. Multiplicar por `z` y pasar de coordenadas unitarias de
`E_c` a las de `E_ac` da la matriz real

\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\
\sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]

Sean `A=a^2`, `C=c^2`, `u=cos^2 p`. Las identidades exactas [V] son

\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},
\]
\[
(I-L^TL)_{22}=(1-u)\frac{A+C-1}{AC}
 +u\frac{A-1}{AC-1},
\]
\[
\det(I-L^TL)=
\frac{(C-1)(1-u)[A-1+C(1-u)]}{AC(AC-1)}.
\]

Son no negativos para `A,C>1`, `0<=u<=1`; luego `I-L^TL>=0`.
Esto prueba (E), incluida la frontera por continuidad. La implicación de
los menores a positividad y la inclusión geométrica son [A], no checks.

### 6.2 Espectro complejo y colisiones

Se fija el desplazamiento de contorno `t=log 2`, en la dirección
`u=(1,1,1)`. Cada `cos(p_j-it)` pertenece a `E_cosh(t)`; (E) aplicado dos
veces prueba uniformemente en **todo** el toro real

\[
f(p-it u)\in E_{\cosh^3 t}=E_{125/64}.
\]

Para una matriz unimodular, los eigenvalores `lambda,lambda^-1` satisfacen
`(lambda+lambda^-1)/2=f`. Si `|lambda|=r>=1`, la imagen es una elipse
de semieje mayor `(r+r^-1)/2`. Las elipses están anidadas, por lo que

\[
\rho(S(p-it u))\le e^{\kappa},\qquad
\kappa=\operatorname{arcosh}(125/64)<\log4,
\]

pues `125/64 < 17/8=cosh(log4)`. No se selecciona una rama global de
eigenvalores. Esto cubre también `f=+1,-1` y cualquier nodo del toro.

Los catorce bloques de `S` tienen suma de normas `4` [V]: ocho vértices
de norma `1/4`, cuatro desplazamientos `(+-1,+-1,0)` de norma `1/4` y
dos axiales de norma `1/2`. Como `|u·d|<=3`,

\[
\|S(p-it u)\|\le4e^{3t}=32.
\]

En la forma de Schur unitaria `T=[[lambda1,b],[0,lambda2]]`, `|b|<=32` y
`|lambda_j|<=4`. La entrada superior de `T^N` es
`b sum_(j=0)^(N-1) lambda1^j lambda2^(N-1-j)`, también para eigenvalores
coincidentes. Por tanto

\[
\|S(p-it u)^N\|\le4^N+32N4^{N-1}\le9N4^N. \tag{P}
\]

Se ha controlado el posible factor de Jordan sin dividir por un gap.

### 6.3 Contorno y norma entre las regiones completas

Con Fourier inversa `e^{-ip·d}`, se desplaza **hacia abajo**,
`p -> p-it u`. El factor se convierte en `e^{-t u·d}`. La periodicidad y
el carácter entero cancelan las caras laterales del contorno. (P) da

\[
\|(S^N)_{y,x}\|\le9N\exp[-t\,u\cdot(y-x)+N\log4].
\]

Usando (G), para todos los pares de las regiones congeladas,

\[
\|(S^N)_{y,x}\|\le9N e^{-JN},\qquad
\boxed{J=(1-\sqrt3/2)\log2>0}. \tag{J}
\]

`J` es una tasa inferior certificada para el exponente de una **upper
bound**, no una tasa óptima ni una equivalencia asintótica. La desigualdad
es direccional: se derivó con la proyección sobre `u` y sirve en todo
`(B_N-A_N)/N`. No afirma resolver `I(v)` en otras geometrías.

Cada región tiene a lo sumo `(N/2+1)^3<=N^3` sitios (`N>=2`). La cota de
Schur por bloques, o Cauchy–Schwarz para la suma de normas, da

\[
T_N:=\|P_{B_N}S^NP_{A_N}\|\le9N^4e^{-JN}. \tag{T}
\]

### 6.4 De propagación a distinguibilidad operacional

En el sector de una partícula, para cualquier estado puro normalizado y
cualquier unitario que actúe como identidad fuera de Alice,
`||v1-v0||<=2T_N`, con `v_b=P_B S^N U_b psi`.
El estado reducido completo es
`(1-||v_b||^2)|vac><vac|+|v_b><v_b|`, incluidos todos los modos de Bob.
Como `||v_b||<=1`,

\[
D_B\le\||v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|\|_1
\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|
\le4T_N\le36N^4e^{-JN}. \tag{D1}
\]

La primera desigualdad incluye el bloque de vacío: su contribución es
`|tr X|`, acotada por `||X||_1`. Convexidad extiende (D1) a cualquier
estado mixto de una partícula. Todo efecto físico de Bob satisface
`delta<=D_B`; esto incluye exactamente los cuatro del charter.

Para no dejar ambigua la frase «toda operación unitaria, todo estado» de
§6, también se obtiene una cota uniforme en el CAR completo para unitarios
**pares** locales de Alice, sin restringir a Gaussianos ni a una partícula:

\[
D_B\le32|B_N|T_N\le288N^7e^{-JN}. \tag{DF}
\]

Prueba. El subespacio de los `d_B=2|B_N|` modos de Bob evolucionados hacia
atrás es `L=(S^N)^* ran P_B`; su proyección a Alice tiene norma `T_N`.
Si `T_N<1/2`, proyectar `L` en `A^perp` y ortonormalizar produce `L'`
de la misma dimensión. Sus ángulos principales con `L` son como máximo
`arcsin T_N<=2T_N` (los valores singulares de la proyección a `A^perp`
son `sqrt(1-s_j^2)`, `s_j<=T_N`). La rotación canónica `V` que lleva
`L` a `L'` actúa en dimensión a lo sumo `2d_B`, con fases `+-theta_j`.
Su segunda cuantización cumple
`||Gamma(V)-I||<=sum 2theta_j<=4d_B T_N` por
`|e^{i alpha}-1|<=|alpha|` para cada suma de fases ocupadas.
Todo efecto `E` en el álgebra de `L` queda a distancia de norma
`<=2||Gamma(V)-I||` de un efecto `E'` en `L'`. Este último conmuta con
todo unitario par de Alice, pues `L'` es ortogonal a sus modos. Luego
`||U^* E U-E||<=2||E-E'||<=16d_B T_N=32|B_N|T_N`.
Tomar el supremo sobre efectos prueba (DF), para cualquier estado.
Si `T_N>=1/2`, la misma cota se cumple trivialmente por `D_B<=1`.
Se trata de una cota adicional para los cuantificadores de la obligación;
no amplía las familias ni los recursos evaluados por el gate.

Para los dieciséis pares se usará la cota más fuerte (D1), junto con
`delta<=1`: `U_N=min(1,36N^4 exp(-JN))`. Queda excluida una lower bound
polinómica positiva. **No se ha demostrado positividad de ninguna señal.**

## 7. Análisis de los dieciséis pares: lower bounds y cancelaciones [A]

### 7.1 Reducción exacta de la señal física, sin proyección espectral

Definimos, sólo como abreviaturas de amplitudes del protocolo,

\[
c_N(x)=\cos(\pi F_N(x)/2)-1,\qquad
s_N(x)=\sin(\pi F_N(x)/2),\qquad \phi_N(x)=b_N(x)\downarrow,
\]
\[
r=P_B S^N\phi_N,\quad a=P_B S^N(c_N b_N\downarrow),\quad
b=P_B S^N(s_N b_N\uparrow),\quad d=P_B S^N(s_N b_N\downarrow),
\qquad v=r+a.
\]

`P_B` aquí restringe a los sitios del aparato físico; **no** es `Pi` ni
`Pi'`. Todas las convoluciones son exactas: por ejemplo,

\[
a(y)=\sum_{x\in A_N}(S^N)_{y,x}c_N(x)b_N(x)\downarrow,
\qquad
r(y)=\int e^{-ip\cdot y}S(p)^N\widehat\phi_N(p)d\mu.
\]

La primera suma es finita por soporte exacto del encoder. La segunda
integral representa el recurso completo, sin truncar su cola espacial.
También se puede escribir como suma finita sobre los desplazamientos del
kernel de `S^N`, evaluando `b_N(y-d)` por su integral exacta. No se ha
sustituido el recurso por uno de soporte espacial finito.

Las cuatro amplitudes de Bob codificadas son, por acción explícita de cada
Pauli sobre `down` [V],

| Encoder | Amplitud física codificada en Bob |
| --- | --- |
| `I` | `v+i d` |
| `sigma1` | `v+i b` |
| `sigma2` | `v+b` |
| `sigma3` | `v-i d` |

Esto no supone equivalencia entre direcciones. Para un detector concreto
`E=h_B M_B` y `H_E=<v,E v>-<r,E r>`, se obtienen las identidades
de respuestas **con signo**

\[
L_{I,E}=H_E+\langle d,Ed\rangle-2\operatorname{Im}\langle v,Ed\rangle,
\quad
L_{3,E}=H_E+\langle d,Ed\rangle+2\operatorname{Im}\langle v,Ed\rangle,
\]
\[
L_{1,E}=H_E+\langle b,Eb\rangle-2\operatorname{Im}\langle v,Eb\rangle,
\quad
L_{2,E}=H_E+\langle b,Eb\rangle+2\operatorname{Re}\langle v,Eb\rangle.
\tag{L}
\]

Siempre `delta_(M,M_B)=|L_(M,E)|`. En particular, un término cuadrático
positivo en (L) **no** prueba positividad de la respuesta completa: puede
cancelarse con `H_E` o con la interferencia.

Para mostrar los cuatro detectores de cada encoder sin omitir componentes,
sea la matriz interna hermítica

\[
R_M=\sum_{y\in B_N}h_B(y)
 [\psi_1^M(y)\psi_1^M(y)^*-r(y)r(y)^*]
 =\begin{pmatrix}\alpha_M&z_M\\\bar z_M&\beta_M\end{pmatrix}.
\]

Con datos de la **misma** pareja física de estados, las cuatro respuestas
son exactamente [V]

\[
\begin{split}
F_0(R_M)&=\alpha_M+\beta_M,\\
F_1(R_M)&=(\alpha_M+\beta_M)/2+\operatorname{Re}z_M,\\
F_2(R_M)&=(\alpha_M+\beta_M)/2-\operatorname{Im}z_M,\\
F_3(R_M)&=\alpha_M.
\end{split} \tag{F}
\]

Así los detectores Pauli no han sido sustituidos por ocupación total.
La matriz `R_M` es suficiente para estos cuatro efectos, pero no contiene
todas las coherencias entre sitios del estado reducido de Bob: ni siquiera
probar `R_M=0` bastaría por sí solo para concluir `D_B=0`.

### 7.2 Intentos de cerrar una lower bound y obligación que queda abierta

Se examinaron las siguientes vías sobre (L), para cada una de sus cuatro
columnas de detector (F):

1. **Extraer el rayo de vértice.** El término del kernel de §2 es no nulo,
   pero las amplitudes son sumas coherentes de todos los sitios de Alice,
   y (L) incluye la interferencia con `r`. No hay una desigualdad inferior
   que sobreviva al reemplazo de estas sumas por un término. La prueba de
   camino único para un bloque no se extiende a la señal de región.
2. **Usar positividad del efecto.** Da `delta>=0` y positividad de los
   términos cuadrados, pero no signo de su diferencia con el estado de
   referencia. (L) expone explícitamente los términos que faltaría dominar.
   En `I` y `sigma3`, cambiar el signo de la fase cambia un término de
   interferencia; no certifica ni igualdad ni no nulidad de sus respuestas.
   En `sigma1` y `sigma2` se requieren, respectivamente, las partes
   imaginaria y real de un solapamiento distinto. No se identifica ninguna
   de ellas mediante una simetría no probada del protocolo.
3. **Saddle del contorno de §6.** El lema de elipses controla un supremo de
   norma; no identifica el término dominante de las sumas con `c_N,s_N,h_B`
   ni su fase relativa a `r`. Los perfiles se anulan en las fronteras y las
   bolas son conjuntos de red dependientes de `N`. No se ha obtenido una
   expansión uniforme con resto relativo ni una amplitud principal no nula
   para ninguna de las dieciséis respuestas. El uso de Schur evita
   singularidades para la upper bound, pero no resuelve esa obligación.
4. **Aproximación Weyl en la banda.** La cota heredada por paso es
   `||S-e^{-iH_W}||<=O(N^-2)` sobre `Pi`, y la telescópica hasta `N` pasos
   da error `O(N^-1)`. Para el estado codificado, el control IR probado es
   también algebraico. Estos errores no permiten resolver el signo de una
   cantidad cuya upper bound es exponencial. No se usan para atribuir la
   señal a una banda ni para reemplazarla por otra observable.

Estos son límites de lo demostrado en este run, **no** pruebas de que una
lower bound sea imposible. No se ejecutó un barrido de valores finitos de
`N` ni se usó coma flotante para inferir ceros. No se dispone de diagnóstico
numérico `SUPPORTED` con error certificado que añadir.

### 7.3 Tabla exhaustiva de la familia congelada

En la tabla, `P_j=(I+sigma_j)/2`, `U_N=min(1,36N^4e^{-JN})` y
`F_j` es la respuesta física exacta (F). «No decidida» significa que no se
ha demostrado ni cero exacto eventual ni estricta positividad eventual.
La lower bound `0` es sólo la trivial; no cumple ningún criterio positivo.
`OPEN_PAIR` es una etiqueta individual, no un estado terminal adicional.

| Encoder | Detector | Admisibilidad | Upper bound | Lower bound / asintótica | Signo / no nulidad | Estado individual |
| --- | --- | --- | --- | --- | --- | --- |
| `I` (REFERENCE_CONTROL) | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_I))` | no decidida | OPEN_PAIR |
| `I` (REFERENCE_CONTROL) | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_I))` | no decidida | OPEN_PAIR |
| `sigma1` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_1))` | no decidida | OPEN_PAIR |
| `sigma1` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_1))` | no decidida | OPEN_PAIR |
| `sigma2` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_2))` | no decidida | OPEN_PAIR |
| `sigma2` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_2))` | no decidida | OPEN_PAIR |
| `sigma3` | `I` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_0(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_1` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_1(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_2` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_2(R_3))` | no decidida | OPEN_PAIR |
| `sigma3` | `P_3` | PASS/PASS | `U_N` | `0`; sin asintótica de `abs(F_3(R_3))` | no decidida | OPEN_PAIR |

## 8. Clasificación final

**Único estado terminal asignado: `OPEN_AFTER_SCALED_IR_ANALYSIS`.**

Se aplica literalmente la regla explícita de §7 del charter: hay upper
bound exponencial con `J>0`, pero no lower bound positiva ni asintótica
de amplitud no nula para ningún par. Las operaciones son IR-admisibles;
la exclusión por admisibilidad no procede. No se ha demostrado la
obstrucción exacta `D_B=0` para la familia. La alternativa polinómica queda
excluida por (D1). La alternativa positiva exponencial no está certificada.

No se asignan constantes `C_1`, `c`, `p` ni `N_*` de una lower bound que
no se ha obtenido. Para las upper bounds sí se dan constantes efectivas:
`C_2=J=(1-sqrt3/2)log2`, `C=36`, `q=4`, para todo `N>=2` en el sector
congelado; y `C=288`, `q=7` para la cota CAR general (DF).

## 9. Techo de reclamo

Demostración analítica del autor: geometría y carta admisibles, encoders y
detectores de las familias congeladas IR-admisibles, sanity puntual correcto,
upper bound direccional exponencial para la propagación y la distinguibilidad.
No hay revisión independiente nueva ni certificación formal de las pruebas.

No demostrado: positividad eventual de `delta`, nulidad exacta de `D_B`,
lower bound, asintótica equivalente, tasa óptima, ni transporte de la señal
por el sector IR. No se califica la señal de «puramente de red» ni se adopta
la lectura positiva reservada por §7 al estado exponencial señalizante.

Las cotas IR son propiedades de las operaciones; la señal física siempre
es la estadística no proyectada del protocolo. La familia interna no es
exhaustiva fuera de los dieciséis pares declarados. `I` es exclusivamente
`REFERENCE_CONTROL`, con nulidad desconocida. La acción de `sigma3` como
fase inicial no autoriza a borrarla de la familia.

Se mantienen sin cambios los witnesses `3/128`, narrow-band, no-corner,
y `Delta T=2` como frente separado. No se fija `a`, `tau`, metros, segundos
ni eV; no hay predicción experimental ni afirmación sobre nuestro universo.
Tampoco se formula una reclamación de novedad bibliográfica.

## 10. Implementación

Sólo se crean este informe y `scripts/verify_scaled_ir_gate.py`. No se
modifica ningún archivo preexistente. El nuevo certificado está limitado a
este gate y reutiliza `walk2`, `is_zero`, `PAULI`, `PS` y `exact_blocks`.

Justificación: los helpers existentes bastan para extraer el símbolo y sus
bloques, pero no contienen la identidad de contracción de elipses ni las
identidades de las operaciones extendidas. Los helpers `evolve` y
`reduced_state` asumen estados de soporte espacial finito; no representan
el recurso actual. Añadir estas comprobaciones a un verificador revisado
cambiaría innecesariamente sus bytes. El archivo separado preserva esa
evidencia y deja trazabilidad permanente de las identidades nuevas.

Cobertura real: el script comprueba el hash del charter, geometría
algebraica, bloques orientados y recurrencia, símbolo y normalización,
identidades internas de las operaciones, límites del sanity puntual,
identidades racionales del lema de elipses, constantes del contorno, suma
de normas de los bloques y los dieciséis funcionales de respuesta.
**No** calcula señales ni certifica positividad. Tampoco formaliza
Plancherel/Minkowski, el conteo de los cubos para todo entero, las cotas de
denominadores y norma de traza, el paso de menores a contracción, el
argumento de contorno, Schur, la reducción CAR, ni las conclusiones
asintóticas que dependen de esas pruebas. Todo ello está demostrado o
declarado abierto en el texto [A], no inferido de un contador de checks.

Dependencias: biblioteca estándar de Python, SymPy y, transitivamente por
`verify_directional_saturation`, NumPy. SymPy y NumPy ya están declarados en
`scripts/requirements.txt` (`1.14.0` y `1.26.4`). SymPy depende a su vez de
mpmath, cuya versión instalada se registra en validación. No se instala
ninguna dependencia nueva. No se usa punto flotante en las cantidades
decisivas del certificado. Los diagnósticos numéricos de las regresiones
históricas conservan su nivel `SUPPORTED` y no apoyan este veredicto.

## 11. Validación

Todos los comandos científicos siguientes terminaron con código de salida
`0`. Se ejecutaron desde la raíz con `python3 -B`, sin `--output` ni
escritura sobre registros anteriores. Los logs de ejecución auxiliares se
capturaron en `/tmp/scaled-ir-*.log`; la procedencia permanente son los
scripts existentes y el certificado nuevo.

| Comando después de `python3 -B` | Resultado |
| --- | --- |
| `scripts/verify_scaled_ir_gate.py` | 53/53 identidades exactas |
| `scripts/verify_narrow_band_gate.py` | 34/34 exactas; negativo congelado conservado |
| `scripts/verify_directional_saturation.py` | 27/27; incluye diagnósticos históricos `SUPPORTED` |
| `scripts/verify_directional_saturation.py --local-preparation-only` | 21/21 exactas |
| `scripts/verify_directional_saturation.py --noncorner-gate-only` | 20/20 exactas |
| `scripts/verify_signaling_witness.py` | 17/17 exactas |
| `scripts/verify_weyl_dirac_gate.py` | PASS, 375 comprobaciones exactas |
| `scripts/cert_Aa_s4_counterexample.py` | PASS |
| `scripts/review_Aa_s4_exact.py` | PASS, 117 identidades matriciales o escalares |

Entorno efectivo: Python `3.12.3`, SymPy `1.14.0`, NumPy `1.26.4`,
mpmath `1.3.0`. No se añadieron dependencias. El import del helper hace
trabajo simbólico a nivel de módulo; no ejecuta sus suites ni aporta un
diagnóstico numérico al gate nuevo.

Durante la construcción del certificado, una comparación sintáctica de
`cosh(log 2)` con `5/4` produjo un fallo cerrado tras 29 checks. Se corrigió
la **normalización simbólica del checker**, usando la representación exacta
en exponenciales. No se cambió la igualdad objetivo, ninguna constante
científica ni el charter. La ejecución completa posterior dio 53/53.

`git diff --check`: sin incidencias. Se comprobó además whitespace de los
dos archivos nuevos con `git diff --no-index --check /dev/null <archivo>`:
sin salida de errores (el modo no-index señala la existencia de archivos
diferentes con exit 1). Los nuevos archivos no fueron staged.

SHA256 del certificado nuevo:
`b8c6b56ea114b7cf135c73d344dc7a4911d43d7cba8cef609ea3dcfee415763c`.

Manifiesto de preservación de los helpers revisados:

| Archivo | SHA256 inicial y final |
| --- | --- |
| `verify_directional_saturation.py` | `1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596` |
| `verify_narrow_band_gate.py` | `23be80f2dad55313eb7f0fc88a9dd4429666af3fb2172b10f17ac0951b8d4586` |
| `verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |
| `verify_weyl_dirac_gate.py` | `6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597` |

Manifiesto de los untracked preexistentes (bytes y mtimes preservados):

| Archivo | SHA256 |
| --- | --- |
| `Auditoría De Novedad Matemática.md` | `a5e2f98e74231be68641b73493d67a36d7ee1a891dc0985ce850899a5c2b92f1` |
| log `2026-09-15--1100--siguiente-gate-b-infinito-post-s4` | `b33727d824f711b1f4b8919870ea9edf6ef0b67cbeb91936fe7cb07e639bb1fa` |
| log `2026-09-16--ratificacion-gate-completitud-axial-n3` | `d4855e39d9800733fae01d3454cf14443d0b4aab1ce830fa58c21e57fe091486` |
| `__pycache__/verify_directional_saturation.cpython-312.pyc` | `39fa4fc6e2d61bd1d690951b6087f48eea1c040dc7963ecea4fb909a29a44272` |
| `__pycache__/verify_signaling_witness.cpython-312.pyc` | `d3eeec7b6ae396db63a4e33fd2377824d8aaa023ac12227b1b989d79b2fbe732` |

Estado final: los cuatro untracked previos más los dos archivos nuevos;
ningún cambio tracked ni staged. `HEAD` y la referencia remota local siguen
en el baseline exacto. Charter y `CURRENT_STATE.md` conservan los hashes
de §1. **Sin modificación del contrato, sin promoción, sin commit ni push.**
