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
