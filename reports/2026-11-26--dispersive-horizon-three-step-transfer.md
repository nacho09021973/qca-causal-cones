# Horizonte dispersivo en una caminata unitaria: regla, obstrucciones y matriz de transferencia

Fecha: 2026-11-26. Repositorio: `qca-causal-cones`.

**Estado: DERIVACION_DE_AUTOR — NO AUDITADA.** Se incluyen identidades algebraicas y comprobaciones numéricas no certificadas. **TRANSMISSION = OPEN; NOVELTY = OPEN.** No se afirma radiación de Hawking, horizonte de sucesos de la relatividad general, universalidad computacional ni recuperación de una métrica dinámica. La construcción es un paseo cuántico unitario monopartícula con perfil espacial impuesto, no la regla homogénea e interactuante que constituye el objetivo principal del repositorio.

## 1. Objetivo y techo de afirmaciones

Se buscan simultáneamente: (A) una velocidad infrarroja saliente negativa dentro y positiva fuera; (B) una velocidad de grupo positiva para algún número de onda de orden de red dentro; y (C) soporte causal microscópico estricto. La existencia de una rama de Bloch saliente a cuasienergía constante es una comprobación adicional **local**. La transmisión a través de la dinámica espacial completa es una obligación distinta.

Esta nota recoge también dos construcciones preliminares descartadas para no confundir el éxito cinemático de la tercera con los fallos anteriores.

## 2. Convenciones independientes de las de otros modelos del repositorio

Hilbert de una partícula: \(\mathcal H=\ell^2(\mathbb Z)\otimes\mathbb C^2\), con base \(|x,\uparrow\rangle,|x,\downarrow\rangle\).

\[
C(\beta)=e^{-i\beta\sigma_y}
=\begin{pmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{pmatrix},
\]
\[
S|x,\uparrow\rangle=|x+1,\uparrow\rangle,\qquad
S|x,\downarrow\rangle=|x-1,\downarrow\rangle,
\qquad
L_-|x,s\rangle=|x-1,s\rangle.
\]

Usamos \(L_-\), no \(T_-\), porque \(T_\pm\) ya nombra amplitudes de dispersión en la línea Thirring del repositorio. En representación de coordenadas, \((L_-f)(x)=f(x+1)\). Un estado plano tiene amplitudes proporcionales a \(e^{-ikx}\), de modo que
\[
S(k)=\operatorname{diag}(e^{ik},e^{-ik}),\qquad
L_-(k)=e^{-ik}I.
\]
En esta convención escribimos autovalores de Floquet como \(e^{i\Omega(k)}\), con velocidad física \(v=\partial_k\Omega\); si se emplea \(e^{-i\omega}\), hay que transformar los signos conjuntamente. Las definiciones anteriores, no una convención implícita de Thirring/Weyl, fijan el operador de esta nota.

## 3. Dos intentos descartados

**Una sola moneda.** Para \(U=L_-S_\eta C(\theta)S_\eta C(\theta)\), la fase constante \(\eta\) se elimina mediante una conjugación de fase espacial, salvo una fase global. La supuesta frontera obtenida tomando \(k=0\) como «IR» no corresponde al verdadero nodo de Dirac. En el nodo, la velocidad saliente es \(-1+2a\), con \(a=\cos\theta\), y para todo \(k\) se verifica \(v_\pm(k)\le-1+2a\). Si \(a<1/2\) atrapa al modo IR, no queda modo UV de velocidad saliente positiva en esa región. Esto no excluye amplitudes no balísticas dentro del cono microscópico.

**Dos monedas split-step en la subfamilia real sin masa.** Para \(W_{\rm ss}=S_+C(\theta_2)S_-C(\theta_1)\) y \(U=L_-W_{\rm ss}^2\), el símbolo congelado cumple
\[
\cos E=\cos\theta_1\cos\theta_2\cos k-\sin\theta_1\sin\theta_2.
\]
En \(|\theta_j|<\pi/2\), la existencia de un nodo sin masa obliga a \(\theta_2=\pm\theta_1\) (nodos en \(0\) o \(\pi\)). En esos dos casos \(|E'(k)|\le|\cos\theta_1|\) para todo \(k\), y reaparece la obstrucción \(\max v_{\rm grupo}\le-1+2|\cos\theta_1|\). **No es un teorema sobre todas las monedas \(U(2)\) ni sobre todos los split-step.**

## 4. Bloque de tres desplazamientos y evolución completa

Sea un perfil \(0<t_x<1\), con
\[
\theta_x=\arccos\sqrt{t_x},\qquad
W=S C(\theta)S C(\theta)S C(-2\theta),\qquad
\boxed{U=L_-W^2}.
\]
Cada \(C(\cdot)\) se aplica localmente en el sitio en que está la excitación en esa etapa. El bloque \(W\) contiene **tres** desplazamientos condicionales, mientras que una actualización completa \(U\) contiene **seis**, más el desplazamiento global \(L_-\). Todos los factores son unitarios y de alcance finito.

En una actualización, el soporte está dentro de \([-7,5]\); para los parámetros declarados abajo, los desplazamientos extremos tienen coeficientes no nulos. Así,
\[
C_{\rm micro}=[-7,5],\qquad
\operatorname{supp}U^n\delta_x\subseteq[x-7n,x+5n].
\]

Tomamos el perfil congelado en el espacio
\[
\boxed{t_L(x)=\frac38+\frac1{16}\tanh(x/L),\quad L>0.}
\]
Sus límites son \(t_{\rm int}=5/16\), \(t_h=3/8\) y \(t_{\rm ext}=7/16\). No se ha fijado ni calculado un coeficiente de transmisión para ningún \(L\).

## 5. Dispersión congelada y criterio cinemático

Escribiendo \(t=\cos^2\theta\) y \(A=t(2t-1)\), la mitad de la traza del bloque homogéneo es exactamente
\[
\boxed{\cos E(k;t)=f_t(k)=A\cos3k+(1-A)\cos k}.
\]
Se puede obtener seleccionando el coeficiente de \(\cos3k\), igual al producto \(\cos(-2\theta)\cos^2\theta=A\), y usando \(W(0)=I\).

Las fases de \(U\) son
\[
\Omega_\pm(k;t)=-k\pm2E(k;t).
\]
En \(k=0\) hay un nodo sin masa; su pendiente del bloque es
\[
c_{\rm IR}(t)=\sqrt{1+8A}=|4t-1|.
\]
Como todo el perfil satisface \(t>1/4\), la velocidad infrarroja saliente de \(U\) vale
\[
\boxed{v_{\rm IR,out}(t)=-1+2(4t-1)=8t-3}.
\]
Da \(-1/2,0,+1/2\) respectivamente en interior, horizonte y exterior. La otra rama infrarroja es entrante en las tres regiones.

En \(k=\pi/2\), \(E=\pi/2\) y \(E'=1-4A\), por lo que
\[
\boxed{v_{\rm UV,out}(\pi/2;t)=1-8A(t)}.
\]
Los valores exactos son \(31/16,7/4,23/16\) respectivamente en interior, horizonte y exterior; todos son positivos y menores que el soporte derecho microscópico \(5\).

Además, la fase \(\Omega_+(\pi/2;t)=\pi/2\) es independiente de \(t\). Por continuidad y compacidad existe un \(\omega_*<\pi/2\) suficientemente próximo y una rama \(k_+(t)<\pi/2\), no degenerada, con \(\Omega_+(k_+(t);t)=\omega_*\) y \(\partial_k\Omega_+>0\) en todo el perfil congelado. **Este es un resultado sobre el símbolo local; no demuestra transmisión estacionaria.**

Precaución: el punto exacto \(k=\pi/2\) es una degeneración adicional de Floquet causada por \(W^2\). Antes de interpretar su vecindad como una corrección UV del *mismo* campo infrarrojo hay que auditar la posible especie adicional/doblamiento.

## 6. Matriz de transferencia espacial exacta \(12\times12\)

Para \(z=e^{i\omega}\) buscamos \(U\psi=z\psi\). En el orden de aplicación de las monedas, definimos
\[
(\beta_1,\ldots,\beta_6)=(-2\theta,\theta,\theta,-2\theta,\theta,\theta),
\]
\[
q_1=\psi,\qquad q_{j+1}=SC(\beta_j)q_j\quad (1\le j\le6).
\]
Así \(q_7=W^2\psi\) y la ecuación estacionaria es exactamente
\[
q_7(x+1)=zq_1(x).
\]

Escribimos \(q_j(x)=(a_j(x),b_j(x))^T\) y elegimos
\[
\boxed{
Y_x=(a_1(x),\ldots,a_6(x),b_1(x-1),\ldots,b_6(x-1))^T.
}
\]
Poniendo \(c_j(x)=\cos\beta_j(x)\), \(s_j(x)=\sin\beta_j(x)\), para \(1\le j\le5\) se obtienen las diez filas
\[
a_{j+1}(x+1)=\frac{a_j(x)-s_j(x)b_{j+1}(x-1)}{c_j(x)},
\]
\[
b_j(x)=\frac{b_{j+1}(x-1)-s_j(x)a_j(x)}{c_j(x)}.
\]
Las dos filas de cierre son
\[
b_6(x)=\frac{c_6(x)a_6(x)-za_1(x)}{s_6(x)},
\]
\[
a_1(x+1)=\frac{a_6(x+1)/z-s_6(x+1)b_1(x-1)}{c_6(x+1)}.
\]

Por tanto \(Y_{x+1}=M_x(z)Y_x\), donde **todas** las entradas de \(M_x\) quedan dadas por las doce filas anteriores. Para ofrecer además una forma matricial compacta, sean \(E_{ij}\) las unidades matriciales \(6\times6\), y abreviemos \(c_j=c_j(x)\), \(s_j=s_j(x)\), \(c_+=c_6(x+1)\), \(s_+=s_6(x+1)\). Entonces
\[
\boxed{M_x(z)=\begin{pmatrix}P_x&Q_x\\R_x&H_x\end{pmatrix}},
\]
con bloques
\[
P_x=\sum_{j=1}^{5}\frac{E_{j+1,j}}{c_j}+\frac{E_{1,5}}{zc_+c_5},
\]
\[
Q_x=-\sum_{j=1}^{5}\frac{s_j}{c_j}E_{j+1,j+1}
-\frac{s_+}{c_+}E_{1,1}-\frac{s_5}{zc_+c_5}E_{1,6},
\]
\[
R_x=-\sum_{j=1}^{5}\frac{s_j}{c_j}E_{j,j}
-\frac{z}{s_6}E_{6,1}+\frac{c_6}{s_6}E_{6,6},
\]
\[
H_x=\sum_{j=1}^{5}\frac{E_{j,j+1}}{c_j}.
\]
No se ha sustituido el perfil espacial por coeficientes congelados en esta matriz: aparecen exactamente los valores de moneda en \(x\) y \(x+1\).

En \(5/16\le t\le7/16\), \(\sin\theta\), \(\cos\theta\) y \(\cos2\theta=2t-1\) son no nulos, así que todas las divisiones son legítimas.

La eliminación por bloques da
\[
\boxed{
\det M_x(z)=\frac{\cot\theta_x}{\cot\theta_{x+1}}.
}
\]
En el medio homogéneo \(\det M=1\); en un intervalo el determinante del producto telescopa.

### Comprobación homogénea

Sea \(\lambda=e^{-ik}\), el multiplicador del vector espacial \(Y_{x+1}=\lambda Y_x\), y
\[
f_t(\lambda)=\frac A2(\lambda^3+\lambda^{-3})
+\frac{1-A}{2}(\lambda+\lambda^{-1}).
\]
La ecuación característica es
\[
\boxed{
z^2\lambda^5-z\lambda^6[4f_t(\lambda)^2-2]+\lambda^7=0.
}
\]
Es un polinomio de grado doce cuando \(A\ne0\), y coincide con la ecuación de Bloch de \(U(k)=e^{-ik}W(k)^2\). En particular, la matriz no debe confundirse con la fórmula obtenida reemplazando ingenuamente \(t\) por \(t(x)\) en el polinomio homogéneo: esa operación omitiría los desplazamientos entre monedas de sitios distintos.

## 7. Transmisión: obligación abierta

Para \(z=e^{i\omega_*}\), la matriz de transferencia de un tramo es
\[
\mathcal M_{m:n}(z)=M_n(z)M_{n-1}(z)\cdots M_m(z).
\]
Los dos límites \(x\to\pm\infty\) son matrices homogéneas diferentes. El problema requiere los subespacios propagantes y evanescentes de ambas matrices, una onda incidente desde el interior, ninguna incidente desde el exterior y normalización de flujo.

Sea \(\mathcal T_L(\omega_*)\) la probabilidad física de transmisión resultante. Permanece abierto decidir
\[
\boxed{\mathcal T_L(\omega_*)>0.}
\]
La afirmación más fuerte \(\lim_{L\to\infty}\mathcal T_L(\omega_*)=1\) es solo una **conjetura**: la existencia de una raíz de Bloch saliente en cada medio congelado no controla automáticamente las amplitudes de conversión entre canales.

## 8. Evidencias y controles existentes

- Derivación algebraica directa de las etapas y cierre estacionario, escrita arriba. No auditada por otra familia.
- Comprobaciones aritméticas propias de la matriz dispersiva homogénea y su determinante en los tres valores racionales del perfil: concuerdan a precisión flotante; no son certificados.
- Comprobación comunicada por otro modelo: las 144 entradas concuerdan con la regla definida, 54 relaciones de etapa con residuo máximo comunicado \(3\cdot10^{-11}\), determinante y autovalores compatibles con el polinomio hasta los residuos comunicados \(10^{-13}\)–\(10^{-9}\). Es una revisión numérica de convenciones deducidas, **no revisión formal ni certificación intervalar**, y no se atribuye independencia no acreditada.
- Lectura de convenciones en el repositorio: la línea Thirring usa \(R\) hacia la derecha y \(L\) hacia la izquierda y ya reserva \(T_\pm\) para amplitudes. Se adopta aquí el nombre \(L_-\) para el desplazamiento, sin cambiar el operador. Diferentes líneas documentan distintas elecciones de signo Fourier; las definiciones de §2 son la fuente de verdad para esta nueva construcción.
- Ninguna simulación temporal o cálculo estacionario del coeficiente \(\mathcal T_L\) se presenta como prueba.

Antecedentes generales, sin pretensión de novedad: Di Molfetta, Brachet y Debbasch, *Phys. Rev. A* 88, 042301 (2013), DOI 10.1103/PhysRevA.88.042301; *Bounds on the dynamics of periodic quantum walks and emergence of the gapless and gapped Dirac equation*, *Phys. Rev. A* 97, 012116 (2018), DOI 10.1103/PhysRevA.97.012116; R. Tiedra de Aldecoa, *J. Funct. Anal.* 2020, DOI 10.1016/j.jfa.2020.108704 (teoría de dispersión unitaria, aplicación directa a esta regla aún no verificada); Bisio, Mosco y Perinotti, arXiv:1912.09768 (dispersión en tiempo discreto).


### Cruce conceptual con la cuantización gravitatoria desde conos nulos (2026-11-25)

**Referencia primaria — CONTEXTO, NO VALIDACIÓN DEL MODELO:** V. Chandrasekaran, *An algebraic quantization of gravity from the null cone*, [arXiv:2611.34924v1](https://arxiv.org/abs/2611.34924) (25-11-2026). El artículo parte de relatividad general clásica en conos nulos que se intersectan, reduce sus restricciones, construye observables y amplitudes cuánticas y discute la composición (*gluing*) de regiones nulas, los diamantes causales y su entropía. Es pertinente por la **organización de observables y amplitudes en fronteras causales nulas**, no porque contenga una teoría de caminatas discretas con dispersión.

**Correspondencia limitada:** en este informe, el «horizonte dispersivo» es el cero de la velocidad de grupo **IR de un símbolo local congelado** para un perfil espacial impuesto externamente, mientras que la evolución microscópica conserva soporte causal finito y puede mantener canales salientes de alta frecuencia. En Chandrasekaran las fronteras son superficies nulas de una geometría gravitatoria dinámica y las variables de horizonte incluyen la expansión y la cizalla de congruencias nulas. El empalme de amplitudes sobre conos nulos **no es** la composición de las matrices de transferencia espaciales \(M_x(z)\); son problemas matemáticos distintos.

**Límite inferencial:** el preprint no demuestra para esta regla que \(\mathcal T_L(\omega_*)>0\), ni identifica sus especies Floquet, ni aporta radiación de Hawking. Tampoco se pueden importar a esta caminata sus afirmaciones sobre cuantización de gravedad, dimensión del espacio de Hilbert o entropía de Bekenstein–Hawking. La conexión es una **pregunta de arquitectura causal y comparación conceptual**. La prueba pendiente sigue siendo la revisión independiente de la matriz 12×12 y la dispersión estacionaria inhomogénea normalizada en flujo; esta referencia no altera el estado **OPEN** de esas compuertas.

## 9. Estado y próximo punto de control

**CLOSED AS AUTHOR DERIVATION:** construcción unitaria local; símbolos congelados; desigualdad cinemática IR atrapado / alto número de onda saliente; rama local saliente a cuasienergía constante; matriz espacial exacta y chequeos algebraicos propios.

**OPEN:** revisión independiente de la matriz y de todas las convenciones; existencia/identificación de la matriz de dispersión para el perfil tanh; \(\mathcal T_L(\omega_*)>0\); cota adiabática; interpretación de especies Floquet; comparación de originalidad; obtención de un perfil dinámico bajo una regla homogénea; computación universal e interacciones.

**Siguiente compuerta:** revisión ciega de la equivalencia \(Y_{x+1}=M_x(z)Y_x\iff U\psi=z\psi\), su determinante y la dispersión homogénea, sin reclamar signo de transmisión. Ningún resultado queda promocionado por el solo hecho de estar documentado aquí.
