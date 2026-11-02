# Auditoría del puente Schur → extremos físicos → cuatro términos lineales

Fecha: 2026-09-24. Base: 7f68fa7554c927c23c12c69591d49915b53ee5ab.
Autor: Codex (OpenAI).
Estado: **INDEPENDENT_REVIEW_COMPLETED / CLARIFICATIONS_APPLIED_NOT_REREVIEWED**.

Los primeros dos intentos externos terminaron sin dictamen. Véase el
[registro de ejecución](2026-09-25--schur-physical-bridge-review-status.md).
Gemini revisó el expediente congelado el 2026-10-31: cuatro bloques PASS y
SIGNED_REDUCTION REPAIR_REQUIRED. La objeción y su disposición, incluida
una desigualdad incorrecta del revisor, quedan registradas en la
[nota de revisión](2026-10-31--schur-physical-bridge-review-disposition.md).
Se explicita abajo la absorción geométrica solicitada; esta versión aclarada
no ha sido revisada de nuevo. No se registra un PASS global ni promoción de H1.

La instrucción es reparar el cuello de botella y continuar; la precisión
posterior del usuario exige comprobar, línea por línea, que los extremos
sean los del contrato actual. Este informe propone reparar ese puente.
No presenta la subordinación como una idea nueva ni reutiliza el extremo
de Bob plano sin demostrar su transferencia.

## 1. Objetos y dos niveles de hipótesis

Se conservan la preparación, fuente completa, referencia, observable y W
admisible fijo de [T1](2026-09-24--two-channel-t1-exact-signed-pq.md):
\[
f=J(U_M-I)\phi_N,\quad r=U_N^NJ\phi_N,\quad
r_c=\mathbf1_{\mathcal B_N}\pi_cr,\quad
s=\mathcal F H_\xi f,\quad t_j=T^js,\quad R=D_\xi/\Lambda.
\tag{1}
\]
Aquí \(T=C_NR\), \(D=S\oplus S^{-1}\),
\(C_N(x)=e^{-i\vartheta(x/N)\beta/N}\), \(\beta=\sigma_x\otimes I_2\),
y \(H_\xi f(x)=e^{\xi_*\cdot(x-x_*)}f(x)\).
La transformada de Fourier es unitaria con medida normalizada del toro.
P,Q son los idempotentes acotados de T1, no proyecciones ortogonales.
P es cero fuera de W; dentro de W selecciona las dos raíces dominantes.

Para no introducir hipótesis implícitas se distinguen:

- **B:** perfil real fijo y acotado, \(b=\|\vartheta\|_\infty<\infty\).
- **F:** además, con
  \(\vartheta(X)=\int e^{-ik\cdot X}\widehat\vartheta(k)d^3k/(2\pi)^3\),
  \[
  a_0=\int|\widehat\vartheta(k)|\,d^3k/(2\pi)^3<\infty,\qquad
  a_1=\int|k||\widehat\vartheta(k)|\,d^3k/(2\pi)^3<\infty.
  \tag{2}
  \]
  Es la hipótesis de momento Fourier de CURRENT_STATE §9.4.
  No se deduce de B ni de regularidad meramente \(C^1\).

Constantes O pueden depender del perfil y de W, nunca de N. Los encoders,
detectores y canales pertenecen a las familias finitas congeladas.
No se elige \(W=W_N\).

## 2. Estabilidad Schur en el espacio auxiliar, bajo B

Las identidades del símbolo en ir-corona.tex, lemas de radio espectral y
símbolo inclinado, dan
\[
\rho(R(p))\le1,\qquad \rho(R(p))=1
 \Longleftrightarrow p\in\{0,\pi\}^3.
\tag{3}
\]
Se comprueba la extensión de S a D: S es unimodular, con raíces recíprocas,
y ambos bloques S y su inversa tienen el mismo radio espectral. La traza
de S dividida por dos es \(\prod_j\cos(p_j-i\xi_{*,j})\).
El producto de elipses que acota esa traza es estricto salvo que todos
los factores estén en sus vértices reales, es decir, los ocho saddles.

En Ran P, \(R_P\) es multiplicación escalar por \(\lambda/\Lambda\),
luego es contracción en la norma L2 inducida. En Ran Q dentro de W
la raíz es \(\lambda^{-1}/\Lambda\), uniformemente menor que uno.
En el compacto exterior a W, que no contiene saddles, ambas raíces
son uniformemente menores que uno. Los saltos de P se tratan usando
por separado los cierres interiores y el exterior.

La posible no normalidad exterior no invalida el argumento: una
triangularización unitaria 2×2 acota las potencias por
\(r_0^h+C h r_0^{h-1}\), con \(r_0<1\), también para raíces repetidas.
Escogiendo \(\rho\in(r_0,1)\), e incluyendo el bloque interior, resulta
\[
\|R_Q^h\|\le C_0\rho^h,\qquad \sup_{h\ge0}\|R^h\|\le C_R.
\tag{4}
\]
Las normas son las inducidas en cada rango; la potencia cero allí es
la identidad del rango. La norma equivalente
\[
|y|_*=\sup_{h\ge0}\rho^{-h}\|R_Q^hy\|_2
\]
satisface \(\|y\|_2\le|y|_*\le C_0\|y\|_2\) y
\(|R_Qy|_*\le\rho|y|_*\).

Como la moneda conmuta con el peso de posición,
\(\|T-R\|\le b\|R\|/N\).
Para los bloques de T, escritos \(\mathsf A,\mathsf B,\mathsf C,\mathsf D\)
para distinguirlos de los observables, se obtiene
\[
\|\mathsf A\|\le1+a/N,\quad
\|\mathsf B\|,\|\mathsf C\|\le a/N,\quad
\|\mathsf D\|_*\le\rho+a/N\le\rho_2<1
\tag{5}
\]
para N suficientemente grande. Todas las normas entre rangos usan
L2 en P y la norma estrella en Q. En particular,
\[
\sup_{j\le N}\|T^j\|\le C_W,\qquad
\|Qt_N\|\le C_W(\rho_2^N+N^{-1})\|s\|.
\tag{6}
\]
La primera desigualdad se prueba sumando las dos recurrencias en la
norma \(\|Pz\|_2+|Qz|_*\), en la que
\(|Tz|_\oplus\le(1+2a/N)|z|_\oplus\).

La suma Schur correcta conserva ambos tiempos:
\[
\begin{split}
\|\mathbb M_N\|
&\le \sup_{n\le N}\sum_{m<n}\sum_{k<m}
 \|\Phi_P(n,m+1)\mathsf B G_Q(m,k+1)\mathsf C\|\\
&\le {e^a a^2\over N^2}
       \sup_{n\le N}\sum_{m<n}\sum_{k<m}\rho_2^{m-k-1}
 \le {e^a a^2\over N(1-\rho_2)}.
\end{split}
\tag{7}
\]
La norma es \(\ell^\infty_tL^2\to\ell^\infty_tL^2\) sobre Ran P.
La entrada inicial Q cuesta igualmente \(O_W(N^{-1})\|Qs\|\).
Para N grande la norma del inverso de \(I-\mathbb M_N\) queda
acotada por \((1-C_W/N)^{-1}\).

**Segunda vía para (6):** la identidad de Duhamel y (4) dan
\[
T^js=R^js+\sum_{k<j}R^{j-1-k}(T-R)T^ks.
\]
Gronwall discreto produce
\(\|T^js\|\le C_R e^{C_Rb\|R\|j/N}\|s\|\).
No requiere invertir la memoria. La estabilidad tampoco presupone
conservación del momento: la moneda sigue siendo convolución completa.

## 3. Auditoría de Alice: fuente física completa, después inclinada

El extremo entrante es exactamente s de (1). No es la fuente seno
del modelo viejo. La fórmula exacta del recurso da
\(\|\phi_N(x)\|\le C N^{-3/2}\).
En Alice, de radio \(R_b=N/4\), escribimos
\(x=x_*-\delta\widehat u+v\), \(v\perp\widehat u\),
\(u=(1,1,1)\), \(\widehat u=u/\sqrt3\). Entonces
\[
F_N(x)\le64\delta^2/N^2,\qquad
\|f(x)\|\le(\pi/2)F_N(x)\|\phi_N(x)\|.
\tag{8}
\]
Esto incluye tanto \(\cos(\pi F_N/2)-1\) como \(\sin(\pi F_N/2)\).

La capa \(\delta_j=(\theta_N+j)/\sqrt3\),
\(\theta_N=\{\sqrt3N/4\}\), tiene a lo sumo \(C(1+N\delta_j)\)
sitios. Su disco tiene radio cuadrado
\(2R_b\delta_j-\delta_j^2\le N\delta_j/2\); el conteo se obtiene
empaquetando celdas de la red planar fija, uniformemente en su traslación.
Con \(\xi_*=t_*u\), Plancherel da
\[
\|s\|_2^2
=\sum_{x\in\mathcal A_N}e^{2\xi_*\cdot(x-x_*)}\|f(x)\|^2
\le C N^{-7}\sum_{j\ge0}e^{-2t_*(\theta_N+j)}
     \delta_j^4(1+N\delta_j)
=O(N^{-6}).
\tag{9}
\]
Por tanto \(\|s\|=O(N^{-3})\), uniformemente en la profundidad
fraccional. **No se afirma que la fuente física sin inclinar tenga esa
norma.** Esta cota se obtiene directamente del encoder actual.

## 4. Auditoría de Bob: referencia física actual, bajo F

Ahora se demuestra la estimación que faltaba, sin usar la cola libre
plana. Sea \(\mu_N\) la imagen en el toro de la medida
\(\widehat\vartheta(k)d^3k/(2\pi)^3\) por \(k\mapsto k/N\) módulo
\(2\pi\), con el signo ajustado a Fourier. La multiplicación por
\(\vartheta(x/N)\) es exactamente convolución por \(\mu_N\), y
\[
\|\mu_N\|_{\rm TV}\le a_0,\qquad
\int d_{\mathbb T}(q,0)d|\mu_N|(q)\le a_1/N.
\tag{10}
\]
La representación incluye todas las imágenes periódicas.

En el toro real, D es unitario por fibra. Por ello no aumenta la
norma L1 de la transformada de Fourier. La expansión exponencial
de la moneda en convoluciones acota su norma L1 por \(e^{a_0/N}\).
Aplicándolo N veces a la preparación real \(J\phi_N\), cuya
transformada tiene norma L1 \(O(N^{-3/2})\), se obtiene
\[
\|\widehat{U_N^NJ\phi_N}\|_{L^1}
 \le e^{a_0}\|\widehat{J\phi_N}\|_{L^1}
 =O_\vartheta(N^{-3/2}),\qquad
\sup_y\|\pi_cU_N^NJ\phi_N(y)\|=O_\vartheta(N^{-3/2}).
\tag{11}
\]
Aquí basta \(a_0<\infty\); el momento \(a_1\) se usará en §6.
No se ha inclinado la preparación ni la referencia de cola infinita.

El extremo saliente exacto del funcional lineal es
\[
v_c=\mathcal V_c^*E r_c,\qquad
\ell_c(z)=\langle r_c,E\mathcal V_cz\rangle=\langle v_c,z\rangle.
\tag{12}
\]
Con \(y=y_*+\delta\widehat u+v\), \(y_*=Nu-R_b\widehat u\),
el mismo conteo de capas y \(h_N(y)\le64\delta^2/N^2\) dan
\[
\begin{split}
\|v_c\|_2^2
&=\sum_{y\in\mathcal B_N}e^{-2\xi_*\cdot(y-y_*)}
           h_N(y)^2\|M_Br_c(y)\|^2\\
&\le C_\vartheta N^{-7}\sum_{j\ge0}
       e^{-2t_*(\theta_N+j)}\delta_j^4(1+N\delta_j)
=O_\vartheta(N^{-6}).
\end{split}
\tag{13}
\]
Por tanto \(\|v_c\|=O_\vartheta(N^{-3})\).
Es la norma del extremo **con efecto e inclinación**; la norma global
de r es 1. El spinor de (13) es el del walk doblado inhomogéneo.

## 5. Reconstrucción ponderada y cotas de las diez piezas

La norma exacta de la reconstrucción es
\[
\|E^{1/2}\mathcal V_c\|
 =\max_{y\in\mathcal B_N}
      \sqrt{h_N(y)}e^{-\gamma\delta},\qquad
\gamma=|\xi_*|=\sqrt3t_*,
\]
pues Fourier es unitario, el canal puede escogerse libremente y todos
los detectores congelados tienen un autovalor 1.
La geometría da
\[
\sqrt{h_N(y)}
 ={2R_b\delta-\delta^2-|v|^2\over R_b^2}
 \le8\delta/N,\qquad
\|E^{1/2}\mathcal V_c\|\le8/(e\gamma N).
\tag{14}
\]
Para la cota inferior, tomar el sitio más próximo a
\(y_*+2\widehat u\). Su error de red tiene norma \(\le\sqrt3/2\);
la profundidad está en \([2-\sqrt3/2,2+\sqrt3/2]\) y el desplazamiento
tangencial es acotado. Para N grande está dentro de Bob y
\(\sqrt{h_N}\ge c/N\), mientras la exponencial está acotada por
debajo. Un vector localizado en ese sitio prueba
\(\|E^{1/2}\mathcal V_c\|=\Theta(N^{-1})\).
No da una cota inferior sobre un vector concreto \(Pt_N\).

De (6),(9),(14), ya bajo B,
\[
\|Pt_N\|=O_W(N^{-3}),\qquad \|Qt_N\|=O_W(N^{-4}),
\]
\[
\|E^{1/2}d_{c,P}\|=O_W(N^{-4}e^{-K_*N}),\quad
\|E^{1/2}d_{c,Q}\|=O_W(N^{-5}e^{-K_*N}).
\tag{15}
\]
Se ha absorbido \(\rho_2^N\) en \(O_W(N^{-1})\). Explícitamente, para
cualquier \(0<r<1\) fijo,
\[
\sup_{N\ge2}Nr^N\le\sup_{x\ge0}xe^{-x|\log r|}
=\frac1{e|\log r|}<\infty.
\]
Se aplica con \(r=\rho_2(W,\vartheta)\); las constantes y el umbral
pueden depender de W y del perfil fijo. No se afirma uniformidad al variar W.
La cota \(\|r_c\|\le1\) da bajo B
\(|A_{cP}|=O_W(N^{-4}e^{-K_*N})\),
\(|A_{cQ}|=O_W(N^{-5}e^{-K_*N})\).
Bajo F, usar el extremo (13) mejora las cotas lineales:

| Pieza, para cada c | Cota absoluta | Hipótesis |
| --- | --- | --- |
| \(A_{cP}\) | \(O_W(N^{-6}e^{-K_*N})\) | F |
| \(A_{cQ}\) | \(O_W(N^{-7}e^{-K_*N})\) | F |
| \(B_{cPP}\) | \(O_W(N^{-8}e^{-2K_*N})\) | B |
| \(B_{cQQ}\) | \(O_W(N^{-10}e^{-2K_*N})\) | B |
| \(B_{cPQ}\) | \(O_W(N^{-9}e^{-2K_*N})\) | B |

Hay tres piezas cuadráticas por canal, seis en total. Su suma en un
canal es \(\|E^{1/2}(d_{c,P}+d_{c,Q})\|^2\ge0\), y es
\(O_W(N^{-8}e^{-2K_*N})\). Comparar estos techos no demuestra
dominancia real sobre términos lineales que podrían ser mucho menores.

## 6. Qué operador intermedio es realmente \(O(N^{-1})\)

La cota de memoria (7) ya acota el retorno contra los extremos (9),(13)
por \(O_W(N^{-7}e^{-K_*N})\). No basta sola para comparar todo el
propagador con el libre: falta controlar el transporte siempre P.

Bajo F, para p,p' dentro de W,
\[
P(p')\beta P(p)=[P(p')-P(p)]\beta P(p),\qquad
\|P(p')\beta P(p)\|\le C_Wd_{\mathbb T}(p',p).
\tag{16}
\]
La primera identidad usa \(\beta P(p)=Q(p)\beta\).
La segunda usa la fórmula Riesz analítica en vecindades de los cierres
de cada ventana; puntos de distintas ventanas tienen separación
positiva y P está acotado. Si algún extremo está fuera de W, el
kernel doblemente comprimido es cero. **No se deriva ni se estima el
conmutador del proyector extendido discontinuamente.**

La medida (10), Young y (16) dan
\(\|P\vartheta(x/N)\beta P\|\le C_Wa_1/N\).
Además el resto de Taylor de la moneda tiene norma \(\le b^2/(2N^2)\).
Como R conmuta con P,
\[
\|\mathsf A-R_P\|\le C_W/N^2,\qquad
\|\mathsf A^N-R_P^N\|\le C_W/N.
\tag{17}
\]
El segundo paso es la suma telescópica, usando (5).
Ahora T1 (14), (6) y (7) sí controlan todas las partes:
\[
\|Pt_N-R_P^NPs\|\le C_WN^{-1}\|s\|.
\tag{18}
\]
Incluye la corrección siempre P, la entrada inicial Q y todos los
retornos, no sólo la primera excursión.

Para Q, restar el término homogéneo libre da
\[
\|\mathsf D^N-R_Q^N\|
\le {C_W\over N}\sum_{j=0}^{N-1}\rho_2^{N-1-j}\rho^j
\le C'_W/N.
\]
El término forzado por P está acotado por la suma geométrica en (6).
Por tanto, para cualquier dato s,
\[
\boxed{\|T^N-R^N\|_{\mathscr H\to\mathscr H}=O_W(N^{-1}).}
\tag{19}
\]
Se ha tratado Q inicial y final, no normalidad, cambio de momento e
interfaces de W. Sólo (16)–(19), no la mera estabilidad (6),
permiten reemplazar el transporte completo por el libre.

## 7. Veredicto del chequeo de extremos, línea por línea

Sea \(\mathcal E_N=T^N-R^N\). La cadena completa es
\[
\begin{split}
&2e^{-K_*N}\Re\langle r_c,E\mathcal V_c\mathcal E_Ns\rangle\\
&\quad=2e^{-K_*N}\Re\langle
 \underbrace{\mathcal V_c^*E\mathbf1_{\mathcal B_N}\pi_cU_N^NJ\phi_N}
 _{v_c:\ {\rm Bob\ actual}},
 \mathcal E_N
 \underbrace{\mathcal F H_\xi J(U_M-I)\phi_N}_{s:\ {\rm Alice\ actual}}
 \rangle,\\
&\left|\,\cdot\,\right|
 \le 2e^{-K_*N}
   \underbrace{\|v_c\|}_{O_\vartheta(N^{-3}),\ (13)}
   \underbrace{\|\mathcal E_N\|}_{O_W(N^{-1}),\ (19)}
   \underbrace{\|s\|}_{O(N^{-3}),\ (9)}
 =O_W(N^{-7}e^{-K_*N}).
\end{split}
\tag{20}
\]

| Línea | Objeto usado | ¿Sobrevive el extremo nuevo? |
| --- | --- | --- |
| (8)–(9) | \(J(U_M-I)\phi_N\), encoder completo inclinado | Sí; no se omite el coseno |
| (11) | \(U_N^NJ\phi_N\), evolución física real sin inclinar | Sí; moneda y canales incluidos |
| (12)–(13) | \(\mathcal V_c^*E r_c\) | Sí; efecto, adjunto y Bob actual explícitos |
| (17)–(19) | Error del propagador exacto frente al libre | Sí, bajo F; incluye memoria y transporte P |
| (20) | Funcional lineal con r actual en ambos lados de la comparación | Sí; nunca se sustituye por la referencia plana |

El resultado de esta derivación es que **ambos extremos actuales
sobreviven**, sujeto a F y a la revisión independiente. La escala
\(N^{-7}=o(N^{-13/2})\) se compara con la escala plana como referencia;
no prueba que el nuevo término principal tenga una cota inferior
de ese orden. No autoriza escribir error relativo al nuevo observable
si éste puede anularse.

## 8. Continuación sobre las cuatro piezas firmadas

R, P y Q son diagonales en canal, y s empieza en +.
De (18), el componente minus de \(Pt_N\) es \(O_W(N^{-4})\).
De (6), todo \(Qt_N\) es \(O_W(N^{-4})\).
El Q libre terminal es exponencialmente pequeño por (4).
En concreto, bajo F, (4),(9),(13) dan
\[
\left|2e^{-K_*N}\Re\langle v_+,R_Q^NQs\rangle\right|
\le C_{W,\vartheta}N^{-6}\rho(W)^N e^{-K_*N}
=O_{W,\vartheta}(N^{-7}e^{-K_*N}),
\]
por la cota explícita anterior, ahora con \(r=\rho(W)\). Con
\(f_0=(U_M-I)\phi_N\), la identidad
de reconstrucción libre de T1 implica
\[
2\Re\langle r_+,ES^N f_0\rangle
=2e^{-K_*N}\Re\langle v_+,R_P^NPs\rangle
 +2e^{-K_*N}\Re\langle v_+,R_Q^NQs\rangle.
\]
Así se reemplaza el término libre proyectado por el libre completo,
conservando la referencia física actual \(r_+\). El término completo no
depende de W; su comparación con la pieza P sí tiene constantes dependientes
de W y del perfil. Esto no permite tomar \(W=W_N\).
Emparejando con el extremo actual (13), se obtiene
\[
\begin{aligned}
A_{+P}
 &=2\Re\langle r_+,ES^N f_0\rangle
       +O_W(N^{-7}e^{-K_*N}),\\
A_{+Q},\ A_{-P},\ A_{-Q}
 &=O_W(N^{-7}e^{-K_*N}).
\end{aligned}
\tag{21}
\]
Así se aísla un funcional firmado concreto, conservando la nueva
referencia. La respuesta completa satisface
\[
\begin{aligned}
L_+&=2\Re\langle r_+,ES^N(U_M-I)\phi_N\rangle
 +O_W(N^{-7}e^{-K_*N})+O_W(N^{-8}e^{-2K_*N}),\\
L_-&=O_W(N^{-7}e^{-K_*N})+O_W(N^{-8}e^{-2K_*N}).
\end{aligned}
\tag{22}
\]
No se ha identificado el signo ni la no anulación del funcional en
la primera línea. Su referencia sigue siendo
\(r_+=\mathbf1_{\mathcal B_N}\pi_+U_N^NJ\phi_N\).

**Caso límite:** si \(\vartheta=0\), entonces T=R,
\(r_+=BS^N\phi_N\), \(r_-=0\) y todas las amplitudes minus son cero.
La comparación es exacta y se recupera el protocolo plano.
**Control de fuente cero:** si se prueba con encoder identidad,
s=0 y todos los términos desaparecen; M=I no es ese encoder identidad.

## 9. Alcance y procedencia

Esto repara un puente de estimación; no demuestra novedad, no calcula
el coeficiente del nuevo funcional y no cierra automáticamente H1/H1c,
POWER_13/2_STABILITY, E0 o AdS. En particular, boundedness sin F
no basta para justificar (11),(16)–(22) por esta ruta.

La próxima cantidad a estudiar es el extremo de referencia
\(\pi_+U_N^NJ\phi_N\) dentro del funcional firmado (21).
La forma general de \(\vartheta\) no está seleccionada por esta
conversación: cualquier coeficiente o afirmación de signo deberá
conservar esa dependencia o declarar una familia de perfiles.

El índice biblioteca/INDICE.md no está presente en esta copia.
Se han leído las definiciones, geometría y pruebas primarias locales
de papers/ir-corona/ir-corona.tex y el T1 revisado en la base indicada.
No se invoca literatura nueva ni se usa un resumen de IA como prueba.
La estabilidad se comprueba por las dos derivaciones de §2 y por
los casos límite; ningún ajuste numérico prueba las estimaciones.
La revisión independiente y los hashes del snapshot se registran
en un expediente separado.
