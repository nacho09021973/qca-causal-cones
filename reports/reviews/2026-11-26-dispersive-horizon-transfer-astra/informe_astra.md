<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.172.0)
inicio: 2026-11-26T10:42:22Z  fin: 2026-11-26T10:46:41Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-three-step-transfer.md ; último commit observado: 8e5b540 ; sha256 de la copia enviada 7e372669d0155b26c26b50e464c33a4c7d6612dcf2d5e791b01d57cda90d63b6
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md ; último commit observado: d0114b2 ; sha256 de la copia enviada 9591e16e97347e660a7f4ba48156be7af66f79af3116e8d1e48abb700ec4d0d0
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_matrix.py ; último commit observado: d0114b2 ; sha256 de la copia enviada 98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2
entrada_astra.txt sha256 36549e24553fcdf0510327da4942f64a30f0810af4d14f7e06735bb84701af96
respuesta sha256 3bc70484eea6e7ddfdfc59cd17f6528ce7a0980fbf489ff85feb8a0d450c9e85
-->

**La matriz publicada es algebraicamente correcta y puede usarse como punto de partida para el problema estacionario del perfil tanh. El veredicto global es REPAIR_REQUIRED por dos afirmaciones de la auditoría que necesitan corrección, no por un fallo de la matriz.**

No he ejecutado código ni comprobado archivos, commits o hashes. Las conclusiones matemáticas siguientes proceden de derivaciones manuales; la valoración de (C) procede de inspeccionar el código adjunto. El resultado comunicado «61/61» queda **[UNVERIFIED] como ejecución**.

Presento primero la derivación desde el operador de (A), y después el contraste con (B) y (C).

### 1. Convenciones — PASS

Con la matriz de Pauli usual,
\[
-i\sigma_y=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
por lo que
\[
e^{-i\beta\sigma_y}
=I\cos\beta-i\sigma_y\sin\beta
=\begin{pmatrix}\cos\beta&-\sin\beta\\
\sin\beta&\cos\beta\end{pmatrix}.
\]

Los operadores actúan de derecha a izquierda. En consecuencia, las seis monedas de \(W^2\), en orden de aplicación, son
\[
(-2\theta,\theta,\theta,-2\theta,\theta,\theta).
\]
Esto sigue siendo cierto para un perfil variable: cada moneda se evalúa en el sitio ocupado durante esa etapa.

En coordenadas,
\[
(Sq)_\uparrow(x)=a(x-1),\qquad
(Sq)_\downarrow(x)=b(x+1).
\]
Definiendo \(q_{j+1}=SC(\beta_j)q_j\), se obtiene \(q_7=W^2\psi\). Como
\[
(L_-q_7)(x)=q_7(x+1),
\]
la ecuación estacionaria es exactamente
\[
\boxed{q_7(x+1)=zq_1(x)}.
\]

Para amplitudes \(e^{-ikx}\), los símbolos son
\[
S(k)=\operatorname{diag}(e^{ik},e^{-ik}),\qquad L_-(k)=e^{-ik}I.
\]
La fase temporal \(e^{in\Omega(k)}\) da fase total \(-kx+n\Omega(k)\); la condición estacionaria implica \(x/n=\Omega'(k)\). El signo de la velocidad de (A) es correcto.

### 2. Derivación de la matriz y equivalencia — PASS

Escribo \(c_j=\cos\beta_j(x)\), \(s_j=\sin\beta_j(x)\). Aplicar primero la moneda en \(x\) y después el desplazamiento da
\[
a_{j+1}(x+1)=c_ja_j(x)-s_jb_j(x), \tag{1}
\]
\[
b_{j+1}(x-1)=s_ja_j(x)+c_jb_j(x). \tag{2}
\]

Para \(j=1,\ldots,5\), despejar (2) y sustituir en (1) produce
\[
b_j(x)=\frac{b_{j+1}(x-1)-s_ja_j(x)}{c_j},
\]
\[
a_{j+1}(x+1)=\frac{a_j(x)-s_jb_{j+1}(x-1)}{c_j}.
\]
Aquí se ha usado \(c_j^2+s_j^2=1\).

El cierre superior en \(x\) es
\[
za_1(x)=c_6(x)a_6(x)-s_6(x)b_6(x),
\]
y, por tanto,
\[
\boxed{b_6(x)=\frac{c_6(x)a_6(x)-za_1(x)}{s_6(x)}}.
\]

Para el otro cierre hay que usar la moneda en \(x+1\). Escribiendo \(c_+=c_6(x+1)\), \(s_+=s_6(x+1)\),
\[
za_1(x+1)=c_+a_6(x+1)-s_+b_6(x+1),
\]
\[
zb_1(x-1)=s_+a_6(x+1)+c_+b_6(x+1).
\]
Multiplicar la primera por \(c_+\), la segunda por \(s_+\) y sumar elimina \(b_6(x+1)\):
\[
\boxed{a_1(x+1)=
\frac{a_6(x+1)/z-s_+b_1(x-1)}{c_+}}.
\]
Los coeficientes en \(x+1\) son necesarios.

Para explicitar las doce filas, sean
\[
u_j=a_j(x),\quad v_j=b_j(x-1),\qquad
u'_j=a_j(x+1),\quad v'_j=b_j(x).
\]
Entonces
\[
u'_1=\frac{u_5}{zc_+c_5}
-\frac{s_+}{c_+}v_1-\frac{s_5}{zc_+c_5}v_6,
\]
\[
u'_{j+1}=\frac{u_j}{c_j}-\frac{s_j}{c_j}v_{j+1}
\quad(j=1,\ldots,5),
\]
\[
v'_j=-\frac{s_j}{c_j}u_j+\frac{v_{j+1}}{c_j}
\quad(j=1,\ldots,5),
\]
\[
v'_6=-\frac z{s_6}u_1+\frac{c_6}{s_6}u_6.
\]

Estas filas dan exactamente los bloques
\[
P=\sum_{j=1}^5\frac{E_{j+1,j}}{c_j}
+\frac{E_{1,5}}{zc_+c_5},
\]
\[
Q=-\sum_{j=1}^5\frac{s_j}{c_j}E_{j+1,j+1}
-\frac{s_+}{c_+}E_{1,1}
-\frac{s_5}{zc_+c_5}E_{1,6},
\]
\[
R=-\sum_{j=1}^5\frac{s_j}{c_j}E_{j,j}
-\frac z{s_6}E_{6,1}+\frac{c_6}{s_6}E_{6,6},
\qquad
H=\sum_{j=1}^5\frac{E_{j,j+1}}{c_j}.
\]

La comparación por posiciones verifica las **144 entradas de (A) §6**: 25 entradas estructuralmente no nulas y 119 ceros.

**Equivalencia, incluida la ausencia de soluciones espurias.** Supónganse no nulos los denominadores y \(z\).

La dirección \(U\psi=z\psi\Rightarrow Y_{x+1}=M_xY_x\) resulta de los despejes anteriores.

Recíprocamente, dada una órbita de la recurrencia en toda \(\mathbb Z\), defínanse
\[
a_j(x)=(Y_x)_j,\qquad b_j(x)=(Y_{x+1})_{6+j}.
\]
Las diez filas de etapa recuperan (1)–(2) para \(j\le5\). Defínase después \(q_7=SC(\beta_6)q_6\). La fila de \(b_6(x)\) garantiza
\[
a_7(x+1)=za_1(x).
\]
En \(x+1\), la misma fila y la fila de \(a_1(x+1)\) dan
\[
\begin{aligned}
b_7(x)
&=s_+a_6(x+1)
+c_+\frac{c_+a_6(x+1)-za_1(x+1)}{s_+}\\
&=\frac{a_6(x+1)-zc_+a_1(x+1)}{s_+}\\
&=zb_1(x-1).
\end{aligned}
\]
Esto es el cierre inferior en todos los sitios. Por tanto,
\[
\boxed{Y_{x+1}=M_xY_x\iff U\psi=z\psi}
\]
para soluciones formales en \(\mathbb Z\).

La reconstrucción es única; si \(\psi=0\), todas sus etapas son cero. No hay soluciones espurias. La condición \(\ell^2\), o las condiciones de dispersión, se imponen después: no toda órbita formal es un estado normalizable.

### 3. Determinante — PASS

Las cinco transformaciones de pares
\[
(a_j,b_{j+1})\longmapsto(a'_{j+1},b'_j)
\]
tienen matriz
\[
\frac1{c_j}
\begin{pmatrix}1&-s_j\\-s_j&1\end{pmatrix}
\]
y determinante \(1\).

Tras estas transformaciones quedan las dos variables \(a_6,b_1\). Los cierres tienen factores diagonales
\[
\frac{c_6}{s_6},\qquad-\frac{s_+}{c_+}.
\]
Los términos adicionales dependen de variables ya transformadas y no alteran el determinante. La asignación de posiciones forma el ciclo
\[
1\to2\to3\to4\to5\to6\to12\to11\to10\to9\to8\to7\to1,
\]
cuyo signo es \(-1\). Así,
\[
\det M_x
=(-1)\frac{c_6}{s_6}\left(-\frac{s_+}{c_+}\right)
=\boxed{\frac{\cot\theta_x}{\cot\theta_{x+1}}}.
\]

No aparecen factores de \(z\), ni factores de las primeras cinco monedas. Es una identidad para perfiles variables. En el perfil considerado es positiva; en el caso homogéneo vale \(1\).

Además,
\[
\det(M_n\cdots M_m)
=\frac{\cot\theta_m}{\cot\theta_{n+1}},
\]
lo que comprueba el telescopado y sus índices.

### 4. Dispersión, multiplicidades y degeneraciones — PASS para (A); reparación en (B)

Para derivar la traza directamente del operador, pongo
\[
c=\cos\theta,\quad s=\sin\theta,\quad
d=\cos2\theta,\quad r=\sin2\theta.
\]
La multiplicación de los tres factores \(SC\) da
\[
\frac12\operatorname{tr}W
=c^2d\cos3k+\bigl(-s^2d+2csr\bigr)\cos k.
\]
Con \(t=c^2\),
\[
c^2d=t(2t-1)=A,
\qquad
-s^2d+2csr=(1-t)(2t+1)=1-A.
\]
Por tanto,
\[
\boxed{\cos E=A\cos3k+(1-A)\cos k}.
\]

Como \(\det W=1\), Cayley–Hamilton da
\[
\operatorname{tr}W^2=(\operatorname{tr}W)^2-2=4f_t^2-2.
\]
Para \(\lambda=e^{-ik}\), \(U=\lambda W^2\), de modo que
\[
\det(zI-U)
=z^2-z\lambda(4f_t(\lambda)^2-2)+\lambda^2.
\]
Multiplicando por \(\lambda^5\) resulta exactamente
\[
\boxed{\mathcal P(\lambda,z)
=z^2\lambda^5-z\lambda^6[4f_t(\lambda)^2-2]+\lambda^7}.
\]

El término extremo de \(f_t^2\) da coeficientes principal y constante iguales a
\[
-zA^2.
\]
Para \(zA\ne0\), \(\mathcal P\) tiene grado doce y no tiene raíz cero. Multiplicar por \(\lambda^5\) no introduce una raíz espuria en cero.

La correspondencia de Bloch es explícita:
\[
q_{j+1}=S(\lambda)C(\beta_j)q_j,\qquad
Y=\bigl((q_j)_\uparrow,\lambda^{-1}(q_j)_\downarrow\bigr)_{j=1}^6.
\]
La equivalencia ya demostrada identifica los núcleos de \(M-\lambda I\) y \(zI-\lambda W^2\).

También se obtiene la identidad, incluida la normalización,
\[
\boxed{\det(\lambda I-M)=\frac{\mathcal P(\lambda,z)}{-zA^2}}.
\]
Una justificación de las multiplicidades es usar primero valores genéricos de \(z\), donde las doce raíces son simples, y extender la identidad racional. La simplicidad genérica puede comprobarse tomando \(z\) pequeño: siete raíces tienen balance \(\lambda^7\sim zA^2\), y cinco tienen balance \(\lambda^5\sim1/(zA^2)\); ambos balances producen raíces simples. La identidad se extiende después a los valores degenerados. No se está infiriendo multiplicidad únicamente de la igualdad de núcleos.

**En \((z,\lambda)=(i,-i)\).** A \(k=\pi/2\), \(f_t=0\); Cayley–Hamilton implica
\[
W^2=-I,\qquad U=iI.
\]
Hay dos vectores de Bloch independientes. Las pendientes de las dos fases son
\[
v_+=1-8A,\qquad v_-=-3+8A.
\]
En todo el intervalo del perfil, \(A<0\), por lo que ambas pendientes son no nulas. Cada factor espectral tiene un cero simple al fijar \(z=i\). La raíz \(\lambda=-i\) tiene multiplicidad algebraica dos y geométrica dos: es **semisimple en todo el intervalo**, no solo en los tres valores examinados por T6.

**Una degeneración relevante que obliga a precisar (B).** En el valor del horizonte,
\[
t=\frac38,\qquad A=-\frac3{32},
\]
la expansión directa es
\[
f(k)=1-\frac{k^2}{8}-\frac{13k^4}{48}+O(k^6).
\]
Tomando la continuación analítica de la rama con pendiente positiva,
\[
E(k)=\frac k2+\frac{35}{64}k^3+O(k^5),
\]
y, por tanto,
\[
\Omega_+(k)=\frac{35}{32}k^3+O(k^5),\qquad
\Omega_-(k)=-2k-\frac{35}{32}k^3+O(k^5).
\]

A \(z=1\), el determinante de Bloch tiene orden \(3+1=4\):
\[
\det(I-U(k))=\frac{35}{16}k^4+O(k^5).
\]
Así, \(\lambda=1\) es una raíz **cuádruple**, con espacio propio de dimensión dos porque \(U(0)=I\).

Esto no contradice (A). Sí impide interpretar como regla general la frase de (B), «Band edges \((\partial_k\Omega=0)\) give double roots». Una derivada nula no basta: aquí hay una inflexión estacionaria cúbica, no un extremo cuadrático ordinario.

### 5. Comprobaciones adicionales — PASS

**Soporte.** Seis desplazamientos de \(\pm1\) y uno global de \(-1\) limitan los desplazamientos a \([-7,5]\). Más precisamente, solo pueden aparecer desplazamientos impares en una actualización.

El camino extremo derecho, desde espín superior hasta espín superior, tiene amplitud
\[
\prod_{j=1}^6\cos\beta_j(x+j-1).
\]
El extremo izquierdo correspondiente tiene amplitud
\[
\prod_{j=1}^6\cos\beta_j(x-j+1).
\]
Son caminos únicos para esos extremos, y todos sus factores son no nulos en el perfil. Quedan verificados tanto la cota como sus extremos efectivos.

**Denominadores.**
\[
\cos\theta=\sqrt t>0,\qquad
\sin\theta=\sqrt{1-t}>0,\qquad
\cos2\theta=2t-1\in[-3/8,-1/8].
\]
Junto con \(z\ne0\), esto cubre todas las divisiones de la matriz.

**Velocidades.**
\[
f(k)=1-\frac{1+8A}{2}k^2+O(k^4),
\qquad 1+8A=(4t-1)^2.
\]
Para \(k>0\), \(E'(0^+)=4t-1\) en este intervalo. De aquí
\[
v_{\mathrm{IR,out}}=8t-3
\]
y los valores \(-1/2,0,1/2\). La otra pendiente infrarroja es
\[
-1-2(4t-1)=1-8t<0.
\]

En \(k=\pi/2\),
\[
E'=-\frac{f'}{\sin E}=1-4A,
\qquad
v_{\mathrm{UV,out}}=1-8A.
\]
Los valores publicados \(31/16,7/4,23/16\) son correctos.

**Continuidad de la rama.** Con \(C=\cos k\),
\[
f=g(C)=4AC^3+(1-4A)C.
\]
Como \(A<0\),
\[
g'(C)=12AC^2+1-4A
\ge1+8A=(4t-1)^2>0
\]
para \(C\in[0,1]\). Puesto que \(g(0)=0\), \(g(1)=1\), resulta
\[
0\le f(k)<1\qquad(0<k\le\pi/2).
\]
Así, \(E=\arccos f\) y \(\Omega_+\) son suaves en ese intervalo y continuas hasta el nodo.

**El paso de compacidad también puede cerrarse manualmente.** En el extremo,
\[
\partial_k\Omega_+(\pi/2;t)\ge23/16.
\]
La continuidad conjunta y la compacidad del intervalo de \(t\) proporcionan una franja uniforme \([\pi/2-\delta,\pi/2]\) donde \(\partial_k\Omega_+\ge m>0\). Por tanto,
\[
\Omega_+(\pi/2-\delta;t)\le\pi/2-m\delta.
\]
Para \(0<\varepsilon<m\delta\), la ecuación
\[
\Omega_+(k;t)=\omega_*:=\pi/2-\varepsilon
\]
tiene una única solución en esa franja para cada \(t\), con derivada positiva. El teorema de la función implícita da su dependencia suave de \(t\). Reduciendo la franja se evitan otras degeneraciones.

Esto verifica el argumento local de (A); no determina transmisión.

### 6. Auditoría y verificador — REPAIR_REQUIRED

La derivación anterior respalda el núcleo algebraico de (B). La inspección de (C) permite distinguir los siguientes alcances:

| Grupo | Qué decide el código, si termina satisfactoriamente | Qué requiere argumento adicional |
|---|---|---|
| T1 | Identidad de la moneda y orden del término de operador transcrito | Interpretación espacial y signo de velocidad |
| T2 | Eliminación simbólica, comparación de las 144 entradas y unicidad local | Bijección de soluciones en toda \(\mathbb Z\) |
| T3 | Una órbita concreta con monedas variables y aritmética exacta | Equivalencia universal |
| T4 | Identidad racional del determinante y ausencia de \(z\) | Dominio admisible y consecuencias de signo |
| T5 | Traza, determinante de \(W\) e identidad característica simbólica | Correspondencia física de los canales |
| T6 | Semisimplicidad en los tres valores indicados | Extensión a todo el intervalo y otras degeneraciones |
| T7 | Soporte y extremos para una configuración concreta | Resultado universal, probado mediante caminos extremos |
| T8 | Identidades y valores que aparecen en las desigualdades | Desigualdades continuas, derivación de \(E'\) y compacidad |

**No encuentro un mecanismo de falso positivo que invalide los tests centrales.**

- `zero` exige una igualdad simbólica exacta con cero. Una simplificación insuficiente puede provocar un falso negativo; no se acepta una tolerancia numérica como prueba.
- La reducción módulo \(s_j^2+c_j^2-1\) es adecuada: las relaciones son mónicas en variables \(s_j\) distintas. Un resto cero demuestra la identidad en el dominio donde los denominadores están definidos.
- `nonzero_alg` usa un criterio exacto apropiado para los números algebraicos de T6.
- T3 controla que haya suficientes sitios y comparaciones; sus `all(...)` no pasan por una colección vacía.
- Los dos controles negativos de T2 comprueban errores pertinentes. No son una prueba exhaustiva del verificador, pero tampoco se necesita atribuirles ese alcance.

Hay comprobaciones redundantes o de alcance reducido, sin que ello invalide el conjunto:

- La comprobación del auxiliar \(b_6(x+1)\) reutiliza una ecuación incluida en el sistema que se resolvió. Es una comprobación de consistencia, no una segunda demostración independiente de la equivalencia global.
- En T8, comprobar que \(A\) es negativo en ambos extremos no demuestra por sí solo negatividad en todo el intervalo. Aquí la conclusión sí sigue de \(A=t(2t-1)\) y \(0<t<1/2\), como explica el texto.
- El test etiquetado con \(E'(\pi/2)\) comprueba realmente \(-f'(\pi/2)=1-4A\). La relación con \(E'\) se demuestra por escrito; (B) lo reconoce.
- Se pueden contar 61 llamadas efectivas de comprobación en el código. Eso no acredita que se hayan ejecutado satisfactoriamente.

Las objeciones, ordenadas por gravedad, son:

1. **(B), “Homogeneous dispersion”, afirmación general sobre raíces dobles en puntos de velocidad nula.**  
   Necesita las hipótesis de una banda simple y un extremo cuadrático no degenerado. El contraejemplo dentro del perfil es \(t=3/8,\ z=1,\lambda=1\), de multiplicidad cuatro, derivado arriba.  
   **Reparación:** restringir la afirmación a bordes ordinarios y documentar por separado esta degeneración del horizonte. T6 no la examina.

2. **(B), “Second route (T3)”: el número de sitios es incorrecto.**  
   Con `NS=34`, el diccionario inicial tiene claves \(0,\ldots,33\). Los seis pasos `S` lo reducen a \(6,\ldots,27\). La implementación de `L` conserva las claves cuyo sucesor existe, dejando \(6,\ldots,26\): **21 sitios**, no 22. Las 280 comparaciones de etapas sí concuerdan con el código.  
   **Reparación:** sustituir 22 por 21, o hacer que el verificador imprima el número efectivo. Esto no debilita la prueba algebraica.

3. **(B), listado final: “characteristic polynomial for all θ”.**  
   Debe leerse dentro del dominio de definición de la transferencia. La matriz publicada no existe en los valores donde se anulan sus denominadores.  
   **Reparación:** escribir «para todo \(\theta\) admisible, con \(z\ne0\)». La identidad tras eliminar denominadores puede extenderse formalmente más allá; la matriz no.

La ejecución, duración, hashes, commits e historia de independencia declarados por (B) permanecen **[UNVERIFIED]** en esta revisión. No los he usado como evidencia matemática.

### Veredictos y respuesta final

| Apartado | Veredicto |
|---|---|
| 1. Convenciones y cierre estacionario | **PASS** |
| 2. Doce filas, cuatro bloques, 144 entradas y equivalencia | **PASS** |
| 3. Determinante | **PASS** |
| 4. Dispersión y multiplicidades publicadas en (A) | **PASS** |
| 5. Soporte, denominadores, velocidades y continuidad | **PASS** |
| 6. Exactitud de las afirmaciones de la auditoría | **REPAIR_REQUIRED** |
| Ejecución comunicada de (C) | **UNVERIFIED** |
| **Global** | **REPAIR_REQUIRED** |

**Sí: puede usarse matemáticamente la matriz \(M_x(z)\) publicada para estudiar la transmisión estacionaria a través del perfil tanh**, para cualquier \(L>0\) y \(|z|=1\). No encuentro ninguna entrada que deba corregirse, ningún factor perdido en el determinante ni soluciones espurias introducidas por la recurrencia.

Las reparaciones afectan al alcance y a la precisión de la auditoría. La existencia y normalización de canales, el tratamiento de las degeneraciones y el coeficiente de transmisión requieren trabajo posterior. La interpretación de especies de Floquet es una cuestión física separada y no invalida la matriz.