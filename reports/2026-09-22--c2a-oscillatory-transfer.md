# C2a: transferencia del funcional completo y cancelación del corte duro

Fecha: 2026-09-22. Base Git `2b29b19`, con las notas locales C1/C2.
Contrato: [IR_C2A_OSCILLATORY_TRANSFER_GATE](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md).
**Estado: TRANSFER_PROOF_WRITTEN / REVIEW_PENDING.**
Es una derivación analítica nueva sin revisión independiente ni promoción.
No se ha ejecutado código científico, barrido o ajuste para obtenerla.

## 1. Enunciado y cuantificadores

Se conserva exclusivamente el par `M=sigma2`, `M_B=I`, el recurso, los
perfiles, la geometría y el símbolo CJWW (5.15) congelados. N tiende a
infinito por enteros; `P=1_{|p|<=N^{-1/2}}`, sin suavizarlo. Sea
`K=sqrt(N)`, `b=1/4`, `u=(1,1,1)` y `B=Phi_0(b)>0`.
Se usan las definiciones exactas de
[la representación C2](2026-09-22--c2-projected-response-representation.md).

La referencia del contrato es el funcional continuo completo
\[
L^W_{PP}(N)=\int h(Y)\left[2\operatorname{Re}R_0(Y)^\dagger D_K^W(Y)
                              +\|D_K^W(Y)\|^2\right]d^3Y.
\]
La derivación que sigue establece
\[
\boxed{L^W_{PP}(N)=N^{-3}\left[\mathcal C_0+
                  \mathcal C_1\cos(\sqrt N/2)\right]+O(N^{-7/2}),
\quad \mathcal C_0>\mathcal C_1>0,}
\tag{1}
\]
y la transferencia, con todos los errores del funcional incluidos,
\[
\boxed{L_{PP}(N)-L^W_{PP}(N)=O(N^{-13/4})=o(N^{-3}).}
\tag{2}
\]
Por tanto el candidato de resultado discreto completo es
\[
\boxed{L_{PP}(N)=N^{-3}\left[\mathcal C_0+
                  \mathcal C_1\cos(\sqrt N/2)\right]+O(N^{-13/4}).}
\tag{3}
\]
La fase es proporcional a sqrt(N), determinada por el corte móvil.
Lpp es real y finalmente positivo. No se usa un ansatz complejo para
una probabilidad firmada. Las constantes y el umbral de validez del
resto no se hacen numéricamente explícitos.

## 2. Identidades y estimaciones auxiliares

Escribimos `A=A_sigma2`, `zeta=M chi=-i up`, `chi=down`,
`V_N(k)=S(k/N)^N`, `V_W(k)=exp(-i H_W(k))`.
La fuente es exactamente `a_N(x)=N^{-3/2} A(x/N)`.
Definamos `h(Y)=(1-16|Y-u|^2)_+^2`,
\[
\mathscr A_N(k)=\widehat A(k)+E_N^A(k),\qquad
E_N^A(k)=\sum_{m\ne0}\widehat A(k+2\pi Nm),
\]
y el campo continuo cuya muestra es el campo discreto escalado,
\[
D_N(Y)=\int_{|k|\le K}e^{-ik\cdot Y}V_N(k)\mathscr A_N(k)
                       \frac{d^3k}{(2\pi)^3}.
\]
Aquí no se ha omitido ninguna imagen. Denotamos `R_N=mathcal R_N`
del informe C2; el recurso físico libre es `N^{-3/2}R_N(y/N)`.
Sean `w_N=h R_N`, `w_0=h R_0`.

### 2.1. Fourier de fuente y detector

C1 proporciona `||Ahat(k)||<=C(1+|k|)^{-4}`. Además, para `k=r n`,
`r>=2`,
\[
\widehat A(rn)=r^{-4}\sum_{\epsilon=\pm1}
 e^{i\epsilon br}a_\epsilon+O(r^{-5}),
\qquad a_\epsilon=i32\pi^2B\zeta.
\tag{4}
\]
La fuente es radial vectorial, de modo que sus restos no dependen de n.
El perfil radial `f(Y)=(1-16|Y|^2)_+^2` satisface
\[
\widehat f(r)=128\pi\frac{\cos(br)}{r^4}+O(r^{-5}).
\]
Su transformada exacta es una suma finita de seno/coseno por potencias
de r, tal como se verifica en el certificado C1. Como R_N tiene soporte
de Fourier en `|q|<=1`, con norma L1 uniformemente acotada, la convolución
con `hhat(k)=exp(i k.u) fhat(k)` da
\[
\widehat w_N(rn)=e^{irn\cdot u}\left[
\frac{64\pi}{r^4}\sum_{\eta=\pm1}e^{i\eta br}
 R_N(u+\eta bn)+\mathcal E_N(r,n)\right],
\quad \|\mathcal E_N(r,\cdot)\|_{C^6(S^2)}\le Cr^{-5}.
\tag{5}
\]
En efecto, para `|q|<=1`,
`|rn-q|=r-n.q+O(r^{-1})`, con el mismo orden bajo cualquier número fijo
de derivadas angulares. Se expande la fórmula exacta de fhat dentro de
la convolución. Los factores `exp(-iq.u-i eta b n.q)` reconstruyen
`R_N(u+eta b n)`; las derivadas de R_N están acotadas uniformemente,
pues su soporte de Fourier queda fijo. Esto también prueba
`||what_N(k)||<=C(1+|k|)^{-4}` globalmente.

En todo el informe, los límites implícitos son uniformes en N grande,
en la bola de Bob y en las direcciones indicadas. No dependen de una
subsecuencia favorable de las fases.

### 2.2. Lema angular elemental

Para g suave en la esfera y `ell=|u|=sqrt(3)`,
\[
\int_{S^2}e^{-irn\cdot u}g(n)d\Omega
=\frac{2\pi}{ir\ell}
\left[e^{ir\ell}g(-\widehat u)-e^{-ir\ell}g(\widehat u)\right]
+O(r^{-2}).
\tag{6}
\]
También su valor absoluto está acotado por `C r^{-1}||g||_{C^6}`.
Para comprobarlo, se orienta el eje polar en u y se escribe la integral
como `integral_{-1}^1 exp(-ir ell z) G(z) dz`. El promedio azimutal G
tiene dos derivadas acotadas en el intervalo cerrado cuando g tiene seis
derivadas acotadas; sus valores extremos son `2pi g(+/- uhat)`.
Dos integraciones por partes dan (6). Los polos son los dos puntos
estacionarios angulares; no se los descarta por la ausencia de saddle
en el volumen tridimensional.

### 2.3. Dispersión: primer término local y resto

Para el símbolo literal, `S=f I-i a.sigma`,
`a=(sin p1,-cos p1 sin p2,cos p1 cos p2 sin p3)`.
Su logaritmo hermítico cerca del nodo es analítico e impar:
\[
H(p)=H_W(p)+H_3(p)+O(|p|^5),
\]
donde H3 es el polinomio matricial homogéneo cúbico
\[
H_3(k)=\tfrac16\left[
k_1(k_2^2+k_3^2)\sigma_1
+k_2(2k_1^2-k_3^2)\sigma_2
-2k_3(k_1^2+k_2^2)\sigma_3\right].
\]
Esta expresión sigue de `omega/sin(omega)=1+|p|^2/6+O(|p|^4)`
y el Taylor cúbico de las tres componentes de a. Así H3 es un operador
diferencial local de coeficientes constantes, no un multiplicador
pseudodiferencial de soporte desconocido. Entonces
\[
V_N(k)=V_W(k)+N^{-2}V_1(k)+\mathcal T_N(k),
\quad \|\mathcal T_N(k)\|\le C N^{-4}(|k|^5+|k|^6),\quad |k|\le K,
\tag{7}
\]
con
\[
V_1(k)=-i\int_0^1e^{-i(1-s)H_W(k)}H_3(k)e^{-isH_W(k)}ds.
\]
Este operador auxiliar está definido para todo k real; sólo la expansión
de V_N se restringe a la bola de radio K. Extender V1 para utilizar su
soporte espacial no supone aproximar el símbolo de la red fuera de esa bola.
La cota procede de Duhamel para el término de grado cinco y del resto
cuadrático en H3; todos los exponentes reales son unitarios.
En particular `||V_N-V_W||<=C |k|^3/N^2`.

Para r>0, si `J(n)=H_W(n)` y `P_sigma(n)=(I+sigma J(n))/2`, integrar
exactamente los factores de fase de V1 muestra
\[
V_1(rn)=\sum_{\sigma=\pm1}e^{-i\sigma r}
             [r^3 U_\sigma(n)+r^2 Z_\sigma(n)],
\tag{8}
\]
con matrices suaves en la esfera. Los términos diagonales en banda dan
`-i r^3 P_sigma H_3(n)P_sigma`; los cruzados se obtienen de
`(exp(-i tau r)-exp(-i sigma r))/(tau-sigma)`, multiplicado por r^2.
No hay denominador singular angular.

Finalmente, en el recurso fijo `|q|<=1`, Duhamel implica para todo m fijo
\[
\|R_N-R_0\|_{C^m}\le C_m N^{-2},\qquad
\|\widehat w_N-\widehat w_0\|\le C N^{-2}(1+|k|)^{-4}.
\tag{9}
\]

## 3. La escala líder de la referencia Weyl

### 3.1. Término lineal: cancelación espacial y oscilación de borde

La evolución Weyl sin corte de A tiene soporte en `|Y|<=1+b`.
Los soportes de w0 y de cualquier wN están en la bola de Bob,
`|Y-u|<=b`, separada por `gamma=sqrt(3)-3/2>0`.
La propagación finita de Weyl se sigue de la fórmula de ondas para
`cos(|D|)` y `sin(|D|)/|D|`, seguida por H_W. Por ello
\[
\langle w_0,D_K^W\rangle
=-\int_{|k|>K}\widehat w_0(k)^\dagger V_W(k)\widehat A(k)
                        \frac{d^3k}{(2\pi)^3}.
\tag{10}
\]
Las fórmulas (4)–(5) y `V_W=sum exp(-i sigma r)P_sigma(n)` dan en el
término líder integrandos radiales de orden r^-6, antes de la integral
angular. Por (6) adquieren r^-1 adicional, con fases radiales
\[
\pm\ell+\epsilon b-\eta b-\sigma.
\]
Ninguna se anula: su módulo es al menos `ell-(1+2b)=gamma`.
Integrar por partes en r da `O(K^{-7})`. El resto O(r^-2) de (6)
integra absolutamente al mismo orden. En los productos subdominantes,
el resto angular uniforme de (5) y la radialidad de (4) permiten usar
la cota O(r^-1) de (6): el integrando radial es O(r^-8) y su integral
es O(K^-7). En consecuencia,
\[
2\operatorname{Re}\langle w_0,D_K^W\rangle=O(K^{-7}).
\tag{11}
\]

### 3.2. Término cuadrático y coeficiente uniformemente positivo

La reducción radial de C2, obtenida integrando exactamente los ángulos,
da en Bob, uniformemente, con `rho=|Y|`, `n=Y/rho`,
\[
D_K^W(Y)=-\frac{i16B}{\rho K^3}
\sum_{\sigma=\pm1}P_\sigma(n)\zeta\,F_\sigma(K,\rho)+O(K^{-4}),
\]
\[
F_\sigma(K,\rho)=\sum_{\epsilon=\pm1}
\frac{\cos[(\rho+\sigma+\epsilon b)K]}{\rho+\sigma+\epsilon b}.
\tag{12}
\]
La fuente sin corte se anula en Bob. El campo con corte es el negativo
de su integral radial de K a infinito. La cola de fuente `r^-4 cos(br)`
y las funciones j0,j1 producen `integral_K^infinity r^-3 sin(cr)dr`,
cuya expansión es `K^-3 cos(cK)/c+O(K^-4)`. Los demás términos dan el
resto escrito; todos los c tienen módulo al menos gamma.

Sean
\[
t_{\sigma,\pm}(\rho)=\frac1{\rho+\sigma\pm b},\qquad
\nu_\sigma(Y)=\|P_\sigma(n)\zeta\|^2=\frac{1+\sigma n_3}{2}.
\]
Los proyectores son ortogonales, `nu_++nu_-=1`, y
\[
\|D_K^W(Y)\|^2=
\frac{256B^2}{\rho^2K^6}\sum_\sigma\nu_\sigma(Y)F_\sigma(K,\rho)^2
+O(K^{-7}).
\]
Al expandir F_sigma^2, los términos independientes de la fase radial son
\[
\tfrac12(t_{\sigma,+}^2+t_{\sigma,-}^2)
+t_{\sigma,+}t_{\sigma,-}\cos(2bK).
\]
Los otros términos llevan fases `2K rho+constant`. Su integral contra
los pesos de Bob es O(K^-1): `|grad rho|=1`, el soporte no toca el origen
y el peso h es C1 compacto. Una integración por partes con el campo
grad rho controla el error sin término de borde, pues h se anula allí.
De este modo
\[
\int h\|D_K^W\|^2
=K^{-6}[\mathcal C_0+\mathcal C_1\cos(2bK)]+O(K^{-7}),
\tag{13}
\]
donde las constantes explícitas son
\[
\begin{aligned}
\mathcal C_0&=128B^2\int\frac{h(Y)}{\rho^2}
 \sum_\sigma\nu_\sigma(Y)
       (t_{\sigma,+}^2+t_{\sigma,-}^2)\,d^3Y,\\
\mathcal C_1&=256B^2\int\frac{h(Y)}{\rho^2}
 \sum_\sigma\nu_\sigma(Y)t_{\sigma,+}t_{\sigma,-}\,d^3Y.
\end{aligned}
\tag{14}
\]
Todos los denominadores son positivos y mayores o iguales que gamma.
Además
\[
\mathcal C_0-\mathcal C_1
=128B^2\int\frac h{\rho^2}\sum_\sigma\nu_\sigma
                    (t_{\sigma,+}-t_{\sigma,-})^2d^3Y>0.
\tag{15}
\]
La positividad es estricta porque b>0, h>0 en el interior y la suma de
los nu es uno. También C1>0. Queda una cota inferior uniforme del
coeficiente oscilatorio, sin seleccionar subsecuencias. (11) y (13)
prueban (1). La escala A_N de transferencia es, por tanto, Theta(N^-3).

## 4. Transferencia del término lineal discreto

### 4.1. Muestreo e imágenes, conservados hasta acotarlos

La identidad exacta de Poisson aplicada a w_N da
\[
N^{-3}\sum_y w_N(y/N)^\dagger D_N(y/N)
=\int_{|k|\le K}\mathscr W_N(k)^\dagger V_N(k)\mathscr A_N(k)
                        \frac{d^3k}{(2\pi)^3},
\]
con `mathscr W_N(k)=sum_m what_N(k+2pi Nm)`.
Por (4)–(5), ambas sumas de imágenes no centrales son `O(N^{-4})`
en esta bola; se suma `|m|^{-4}` en dimensión tres. Las transformadas
centrales tienen norma L1 uniformemente acotada. La diferencia entre la
última integral y la que conserva sólo what_N y Ahat es, por tanto,
\[
O(N^{-4})+O(N^{-8}K^3)=O(K^{-8}).
\tag{16}
\]
Esto controla simultáneamente el muestreo de Bob y las imágenes de Alice
en el término lineal, sin asumir que el error puntual se suma sin fase.

### 4.2. El primer corrector de dispersión es local antes del corte

El operador V1 es una integral de evoluciones Weyl de duraciones s y
1-s intercaladas con el operador diferencial local H3. Su aplicación a
A tiene soporte en `|Y|<=b+1`, incluso si se interpreta distribucionalmente
por las derivadas de A en la esfera. En consecuencia
\[
\int_{\mathbb R^3}\widehat w_N^\dagger V_1\widehat A\,
                                    \frac{d^3k}{(2\pi)^3}=0.
\tag{17}
\]
Este emparejamiento es absolutamente convergente: el integrando radial
en valor absoluto es O(r^-3). Para justificar el uso de un w_N sólo C1,
se lo regulariza con mollificadores compactos de radio menor que la
separación; sus soportes siguen disjuntos. La identidad vale para los
tests suaves y pasa al límite por convergencia dominada en Fourier.

Por (17), el corrector restringido a la bola es el negativo de la cola.
Usando (4), (5) y (8), su término principal antes de integrar ángulos
es r^-3 por fase radial y una función suave de n. La oscilación
`exp(-ir n.u)` gana r^-1 por (6); integrar su valor absoluto radial
da O(K^-3). Los términos subdominantes son ya O(r^-4) radialmente y
dan el mismo orden sin necesitar otra ganancia. Así
\[
\left|N^{-2}\int_{|k|\le K}\widehat w_N^\dagger V_1\widehat A\right|
\le C N^{-2}K^{-3}=C K^{-7}.
\tag{18}
\]
No se descarta el borde: esta es precisamente su contribución después
de la cancelación del funcional completo sin corte.

El resto de (7) se controla ahora absolutamente porque contiene **dos**
factores Fourier de orden cuatro:
\[
\left|\int_{|k|\le K}\widehat w_N^\dagger\mathcal T_N\widehat A\right|
\le C N^{-4}\int_0^K r^2(1+r)^{-8}(r^5+r^6)dr
\le C N^{-4}(1+K+\log(1+K))=O(K^{-7}).
\tag{19}
\]

### 4.3. Cambio del recurso libre

El producto `(w_N-w_0)` tiene el mismo soporte separado. El emparejamiento
con V_W A sin corte es cero, por lo que (9) acota la diferencia truncada
por su cola:
\[
\left|\int_{|k|\le K}(\widehat w_N-\widehat w_0)^\dagger V_W\widehat A\right|
\le C N^{-2}\int_K^\infty r^2(1+r)^{-8}dr
=O(K^{-9}).
\tag{20}
\]
Las constantes de medida (2pi)^-3 se han absorbido sólo en estas cotas.
(16), (18)–(20) prueban que la diferencia de los términos lineales
completos, incluyendo su parte real y el factor dos, es **O(K^-7)**.

## 5. Transferencia del término cuadrático

### 5.1. Norma L2 para el error de campo, aplicada sólo al error cuadrático

Aquí no se intenta atribuir la señal mediante una norma: se acota el
error de una forma cuadrática cuya referencia en Bob ya se conoce.
Por Plancherel, unitariedad y Duhamel,
\[
\|D_N-D_K^W\|_{L^2(\mathbb R^3)}
\le\frac C{N^2}\left(\int_0^K r^8(1+r)^{-8}dr\right)^{1/2}
+C N^{-4}K^{3/2}
=O(K^{-7/2}).
\tag{21}
\]
El segundo sumando es el error de imágenes de Alice, conservado en
D_N. Por (12), `||sqrt(h)D_K^W||_2=O(K^-3)`. Por Cauchy–Schwarz,
\[
\left|\int h(\|D_N\|^2-\|D_K^W\|^2)\right|
\le2\|\sqrt h D_K^W\|_2\|D_N-D_K^W\|_2
+\|D_N-D_K^W\|_2^2=O(K^{-13/2}).
\tag{22}
\]
Esta cota es menor que K^-6 aunque la anterior aproximación puntual
O(N^-1) no lo fuera. El término lineal no se ha estimado con (21).

### 5.2. Error de muestreo del cuadrático

Falta comparar la integral con la suma de red. El transformado de D_N
tiene soporte en radio K y norma L1 uniformemente acotada, ya que
`||Ahat||_1=O(1)` y `||E_N^A||_{L1(B_K)}=O(N^{-4}K^3)`.
En Poisson aplicado a `h||D_N||^2`, los términos m no nulos contienen
\[
\widehat h(k-q+2\pi Nm),\qquad |k|,|q|\le K.
\]
Para N grande su argumento tiene módulo al menos `c N|m|`.
La cota `|hhat(ell)|<=C(1+|ell|)^{-4}` y la suma convergente de
`|m|^{-4}` dan
\[
\left|N^{-3}\sum_y h(y/N)\|D_N(y/N)\|^2
-\int h(Y)\|D_N(Y)\|^2d^3Y\right|=O(N^{-4})=O(K^{-8}).
\tag{23}
\]
Poisson es legítimo: la función muestreada es continua y compacta y
su transformada, una convolución con soporte central de radio 2K,
decae como |ell|^-4 fuera de ese radio. Para cada N es integrable y
la periodización converge absolutamente. No hay alias escondido
cerca del borde de la celda porque `2K=o(N)`.

## 6. Presupuesto de errores y cierre escrito de C2a

| Pieza | Error absoluto en potencias de K=sqrt(N) |
| --- | --- |
| Lineal: imágenes y muestreo exacto por Fourier | O(K^-8) |
| Lineal: corrector cúbico, tras separación de soportes y oscilación angular | O(K^-7) |
| Lineal: resto de dispersión después del corrector | O(K^-7) |
| Lineal: recurso R_N frente a R0 | O(K^-9) |
| Cuadrático: transferencia de campo en L2 y localización de la referencia | O(K^-13/2) |
| Cuadrático: muestreo restante | O(K^-8) |
| Referencia Weyl: resto de su líder completo | O(K^-7) |

El error dominante de transferencia es O(K^-13/2), mientras el líder
es K^-6 con coeficiente acotado inferiormente por C0-C1>0. Esto prueba
la separación solicitada, `r_N=o(Lpp_W,lead)`, sin una aproximación
puntual fuerte del campo.

La división geométrica pedida queda contabilizada así: el interior
sin corte se cancela por propagación finita de V_W y del corrector V1;
los puntos estacionarios **angulares** se conservan en (6); la frontera
móvil produce (12)–(15) y los correctores (18); las imágenes y el
muestreo se controlan en (16), (21) y (23). No se suaviza P.

**C2a = TRANSFER_PROOF_WRITTEN / REVIEW_PENDING.** No es todavía el PASS
independiente definido por el contrato. No se ha revisado de nuevo la
prueba del observable total ni se han calculado constantes explícitas
del resto para contrastar N=24 o 40. Un cambio de signo a N pequeño no
contradice una positividad meramente asintótica.

## 7. Consecuencia para la cancelación espectral, si la prueba es aceptada

Sea
\[
\mathcal A_N=N^{-3}[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)]>0,
\qquad R_N^{\rm blocks}=L-L_{PP}.
\]
Se distingue este residuo por bloques del recurso R_N. De (3),
\[
L_{PP}=\mathcal A_N+O(N^{-13/4}),\qquad
R_N^{\rm blocks}=-\mathcal A_N+L+O(N^{-13/4}).
\tag{24}
\]
Con la ley total ya registrada, `|L|~|C(theta_N)|N^{-13/2}exp(-K_*N)`,
la descomposición resulta asintóticamente mal condicionada. Por ejemplo,
\[
\frac{|L_{PP}|+|R_N^{\rm blocks}|}{|L|}
=\frac{2[\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)]}{|C(\theta_N)|}
 N^{7/2}e^{K_*N}(1+O(N^{-1/4})).
\tag{25}
\]
R incluye PQ, QP y QQ. (24) no prueba que QQ por sí solo cancele PP.
El cociente (25) caracteriza esta descomposición espectral; no demuestra
un fallo de precisión de las FFT ni de los diagnósticos conservados.
Tampoco identifica un término exponencial separado dentro de cada
bloque: el resto algebraico es mucho mayor que L, y añadir L a una
expansión con resto o(A_N) no permite resolver esa escala. La identidad
exacta `L=Lpp+R` y el líder algebraico opuesto son lo que se establece.

La respuesta proyectada no es una operación local nueva ni el
experimento condicionado de C3. El corte duro es espacialmente no local;
la ley algebraica de su bloque no demuestra transporte local físico
IR con esa ley. El resultado total conserva su alcance anterior.

## 8. Comprobación y límites de evidencia

La comprobación de esta nota es analítica: convenciones de Fourier,
ortogonalidad de los P_sigma, factores 8/16/256 en (12)–(14), positividad
por (15), presupuestos integrables en (18)–(23), y separación estricta
`gamma>0`. No se ha creado ni ejecutado un certificado nuevo.
El PASS independiente de C1 sólo aporta las estimaciones de la fuente;
no se extiende automáticamente a (1)–(25).

Puntos de ataque prioritarios para una revisión posterior: resto angular
uniforme en (5); cancelación distribucional (17); cola del corrector (18);
norma L2 frente a norma puntual en (21); Poisson para la forma cuadrática
(23); y no anulación del coeficiente completo, no sólo de un canal.
C1 permanece PASS, C2 queda pendiente de revisión de esta derivación,
C3 separado y E/AdS congelado. Sin cambios de estado canónico, manuscrito,
commit/push ni reivindicación de novedad.

Entradas preservadas (SHA256):

| Entrada | Hash |
| --- | --- |
| Contrato C2a | `f5dea4d2683468ffee5556381b2800a67be84803e732624fe800a1a1076b108f` |
| Representación C2 anterior | `fe50c58c237202514c8816184f853592999f4b70f49820db6256f11669974732` |
| Revisión independiente C1 | `22f5a10fefee1946eb481c36b4ea85c1fa74a89d1c91856bbbbacb523680794d` |
| Estado canónico, sin cambios | `47d77da9daeee9696c376c6a011096be6b73c38ad9343041660a7f5f8892142a` |
