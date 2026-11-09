<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 03c66606af766858f5571dd331887b79b0d733977821df57649c665fb3cfde23
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-09T07:48:08Z  fin: 2026-11-09T08:04:40Z
documento: /home/ignac/qca-causal-cones/theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md ; último commit observado: 61a8215 ; sha256 de la copia enviada 2f81be0d1120170d86b945bf34f53bfbd660a35607f737a90f965c9a1c99c47c
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-approximate-recovery.md ; último commit observado: ad01e20 ; sha256 de la copia enviada cc32cff910016b19c93caedb8101ea50e0a0a7eaeb3ff810872d793986b684aa
documento: /home/ignac/qca-causal-cones/scripts/verify_thirring_approximate_recovery.py ; último commit observado: f5c0d16 ; sha256 de la copia enviada 53094142066d85de1f831cac3a6ea9b621597de04fdf3054e29735e88803b0cf
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-approximate-recovery.txt ; último commit observado: ad01e20 ; sha256 de la copia enviada a18e1ab7920ec39601b4ab127cd841c4071d89e906e250acdcd1e2161aa0c681
documento: /home/ignac/qca-causal-cones/reports/2026-11-08--thirring-exact-recovery.md ; último commit observado: dbfd6d8 ; sha256 de la copia enviada ea1538babdc5e559e0d59c491fef67998a7d353861bb2064fbbcd10a9364b0cb
documento: /home/ignac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_grok.txt sha256 0a5e63b327527b110f61399b30afc13e1b47407d3dcd36ae41af197f8a30b970
respuesta sha256 4b74b8dbfb6ce84588c57952eb9d35d657f0740759bce58fdebf850556d2fab2
-->

**Veredicto: se sostiene.**

Para este código, esta regla y estos parámetros, \(\liminf_{T\to\infty}\|E_T|00\rangle\|^2\ge c>0\). Eso impide \(\|U^{T_n}B-e^{i\theta_n}B_{T_n}V\|\to 0\) para toda subsucesión, toda fase y toda matriz \(V\). No hay error que obligue a reparar el argumento ni que lo refute. El recuento 16/16 no se usa como prueba: las identidades que importan se rehacen abajo.

## Derivaciones

**(1) Fibras.** \(w=x_1+x_2\), \(y=x_1-x_2\), misma paridad. La traslación diagonal mueve \(w\) de 2 en 2, así que el carácter \(e^{ipw}\) tiene zona \((-\pi/2,\pi/2]\). Con
\[
\psi_p(y)=\sum_w e^{ipw}\psi(w,y),\qquad
\psi(w)=\frac1\pi\int_{-\pi/2}^{\pi/2}e^{-ipw}\psi_p\,dp,
\]
el cambio \(w=2m\), \(q=2p\) da \(\|\psi\|^2=(1/\pi)\int\|\psi_p\|^2\,dp\). En la entrada 00 solo hay dos amplitudes, \(w=1\), \(y=\pm 1\), componente \(\uparrow\uparrow\): \(\|b_p\|^2=1\) para todo \(p\), y \((1/\pi)\int_{-\pi/2}^{\pi/2}1\,dp=1\). La medida es la correcta.

\(J\) y \(W\otimes W\) conmutan con esa traslación, luego \(U=FJ\) y \(F\) actúan fibra a fibra. En la fibra, \(J(p)-I\) solo es distinto de cero en \(y=0\) y en las dos componentes opuestas; como \(z=i\neq 1\), el rango es 2. \(W_2(p)\) es invertible, así que \(U(p)-W_2(p)\) tiene rango 2.

**(2) Autovector.** El vector del informe, caso «+», \(p_0=\pi/4\),
\[
f(1)=(-ie^{ip_0},0,0,0),\quad
f(0)=(0,\mu/\nu,-\mu/\nu,0),\quad
f(-1)=(ie^{ip_0},0,0,0),
\]
con \(\mu/\nu=3/4\), cumple \(U\psi=i\psi\) para \(\psi(w,y)=e^{-ip_0 w}f(y)\). No hace falta el PDF: se calcula la amplitud relativa de \(F(J\psi)\) con
\((W\phi)_R(x)=\nu\phi_R(x-1)-i\mu\phi_L(x)\), \((W\phi)_L(x)=-i\mu\phi_R(x)+\nu\phi_L(x+1)\), que es el \(W(p)\) de 1711.03920 (Fourier) y el \(W\) del contrato si \((T\phi)(x)=\phi(x-1)\).

Tras factorizar \(e^{-ipw}\), las únicas fuentes no nulas son \(\mathrm{RR}\) en \(y=\pm 1\) y, después de \(J\), \(\mathrm{RL},\mathrm{LR}\) en \(y=0\). En todos los \(y\) y las cuatro componentes el resultado es \(if(y)\). Los puntos no triviales cierran por aritmética exacta: en \(\mathrm{RR}\), \(y=1\), \(16/25+9/25=1=i f_{\mathrm{RR}}(1)\) en la normalización de fase usada; en \(\mathrm{LL}\), \(y=\pm 1\), el residuo es proporcional a \(ie^{ip}+e^{-ip}=0\); en \(\mathrm{RL}\) y \(\mathrm{LR}\), \(y=0\), sale \(\pm 3i/4\). El resto de los \(y\) no alcanza el soporte.

La traslación diagonal \(S\psi(x_1,x_2)=\psi(x_1-1,x_2-1)\) cumple \(S\psi=i\psi\) y conmuta con \(U\). El defecto \(\delta=U\psi-i\psi\) cumple \(S\delta=i\delta\), así que basta un representante por órbita. Cada órbita tiene \(y\) fijo y \(w\) de una sola paridad; \(w\in\{0,1\}\) es exactamente ese conjunto. El soporte de \(\psi\) está en \(|y|\le 1\) y \(W\) mueve cada partícula a lo sumo un sitio, así que el de \(U\psi\) está en \(|y|\le 3\). La ventana del script es más grande de lo necesario; la identidad en toda la recta queda cerrada por el cálculo anterior, no por el 16/16.

Además, a mano: \(f(y)=-Ef(-y)\), \(\|f\|^2=2+2(3/4)^2=25/8\), y
\[
\langle f,b_{p_0}\rangle=-i\sqrt2,\qquad
\frac{|\langle f,b_{p_0}\rangle|^2}{\|f\|^2}=\frac{2}{25/8}=\frac{16}{25}.
\]
El signo de la entrada 00 es el del informe previo: \((|R0\rangle\otimes|R1\rangle-|R1\rangle\otimes|R0\rangle)/\sqrt2\).

**(3) Aislamiento.** \(W(q)\) tiene determinante 1 y traza \(2\nu\cos q\), así que sus autovalores son \(e^{\pm i\omega(q)}\) con \(\cos\omega=\nu\cos q\) y \(\omega\in[0,\pi]\). El espectro de \(W_2(p)\) es la imagen de
\[
k\mapsto\exp\bigl(-i(s\omega(p+k)+r\omega(p-k))\bigr),\qquad s,r=\pm,\ k\in\mathbb R/2\pi\mathbb Z.
\]
Igualar a \(i=e^{i\pi/2}\) es \(sa+rb\equiv-\pi/2\pmod{2\pi}\). Con \(a,b\in[0,\pi]\) solo hay cuatro posibilidades: \(a+b=\pi/2\), \(a+b=3\pi/2\), \(a-b=\pi/2\), \(a-b=-\pi/2\). En las cuatro, \(\cos^2 a=\sin^2 b\), luego \(\cos^2 a+\cos^2 b=1\). La identidad trigonométrica del informe da
\[
\nu^2\bigl(1+\cos 2p\cos 2k\bigr)=1.
\]
En \(p_0\), \(\cos 2p_0=0\), luego \(\nu^2=1\). Falso: \(\nu^2=16/25\). La imagen es compacta y no contiene a \(i\), así que \(\mathrm{dist}(i,\sigma(W_2(p_0)))>0\). Por Weyl, \(\sigma_{\mathrm{ess}}(U(p_0))=\sigma_{\mathrm{ess}}(W_2(p_0))\). Como \(i\) ni siquiera está en \(\sigma(W_2(p_0))\), no está en el espectro esencial. El paso 1 lo mete en el espectro, luego es autovalor aislado de multiplicidad finita. \(U(p_0)\) es unitario: no hay bloques de Jordan.

**(4) Peso positivo.** \(U(p)=W_2(p)\tilde V\) es continuo en norma (\(e^{ip}\), \(e^{2ip}\) y saltos de \(y\) acotados; \(\tilde V\) no depende de \(p\)). Se fija un círculo \(\Gamma\) alrededor de \(i\) dentro de la resolvente en \(p_0\) y luego un intervalo \(I\ni p_0\) en el que \(\Gamma\) sigue en la resolvente. La proyección de Riesz \(P(p)\) es continua en norma y de rango finito constante. En \(p_0\), si \(\Gamma\) separa solo a \(i\),
\[
\langle b_{p_0},P(p_0)b_{p_0}\rangle\ge\frac{16}{25},
\]
porque \(P(p_0)\) es ortogonal. Por continuidad el integrando es \(\ge 8/25\) en un entorno, y
\[
c=\|P_I B|00\rangle\|^2=\frac1\pi\int_I\langle b_p,P(p)b_p\rangle\,dp>0.
\]
\(P_I\) conmuta con \(U\). No se obtiene un valor numérico de \(c\); no hace falta.

**(5) Decaimiento.** En un \(I\) pequeño alrededor de \(\pi/4\), \(\sin p\neq 0\) y \(p\neq\pi/2\). Cada rama es analítica real porque \(|\nu\cos|\le 4/5<1\). No es constante:
\[
\omega_{++}(p,0)=2\omega(p)\neq\pi=\omega_{++}(p,\pi/2),
\]
\[
\omega_{+-}(p,0)=0\neq\omega_{+-}(p,\pi/2),
\]
y las otras dos son las negativas. \(W_2(p)\) es multiplicación, en el momento relativo, por esas ramas: espectro puramente absolutamente continuo en todo \(I\), sin autovalores ni espectro singular. El lema de Riemann-Lebesgue da \(\langle W_2(p)^T\xi,\eta\rangle\to 0\) para vectores fijos.

El vector \(U(p)^T P(p)b_p\) se mueve con \(T\), pero permanece en \(\mathrm{ran}\,P(p)\), de dimensión finita fija. Si \((e_j)\) es una base de ese subespacio,
\[
\|P(p)W_2(p)^T b_{j,p}\|^2=\sum_j|\langle W_2(p)^T b_{j,p},e_j\rangle|^2\to 0.
\]
El cruce de autovalores no interviene: \(U(p)^T P(p)\) es continuo en \(p\) aunque las proyecciones espectrales individuales no lo sean. El integrando es continuo, está dominado por \(\|b_{j,p}\|\,\|b_p\|\), integrable en \(I\) compacto, y tiende a 0 en cada \(p\). Convergencia dominada: \(B_T^\dagger U^T P_I B|00\rangle\to 0\).

**(6) Cierre.** \(B_T\) es isometría, \(E_T|00\rangle\perp\mathrm{ran}\,B_T\) y \(\|U^T B|00\rangle\|=1\), luego
\[
\|E_T|00\rangle\|^2=1-\|K_T|00\rangle\|^2.
\]
Con \(\psi=B|00\rangle\),
\[
\|K_T|00\rangle\|\le\|(I-P_I)\psi\|+o(1)=\sqrt{1-c}+o(1),
\]
y por tanto \(\|E_T|00\rangle\|^2\ge c-o(1)\). El \(\liminf\) es al menos \(c\). El vector \(E_T|00\rangle\) no depende de \(V\) ni de \(\theta\). Para cualquier \(V_n\) y \(\theta_n\),
\[
\|(U^{T_n}B-e^{i\theta_n}B_{T_n}V_n)|00\rangle\|\ge\|E_{T_n}|00\rangle\|,
\]
que no tiende a 0. Tampoco \(\ell_{T_n}=\|E_{T_n}\|^2\), porque \(\|E_T\|\ge\|E_T|00\rangle\|\).

**(7) Script y ejecución fallida.** Inspeccionado, no ejecutado. Las 16 comprobaciones son las que el informe dice: autovector en la ventana, antisimetría, determinantes/traza/identidad trigonométrica, solapes y \(16/25\). No certifican el análisis de casos, Riesz, continuidad absoluta ni las fibras; el informe lo dice. Los solapes que rehice coinciden con el registro: \(00\mapsto -i\sqrt2\), \(01\mapsto 3\sqrt2/4\), \(10\mapsto -3i\sqrt2/4\), \(11\mapsto 0\). La primera ejecución falló por una predicción falsa (esperar solape nulo en 01 y 10, que son pares opuestos en el mismo sitio y tocan \(f(0)\)), no por un cálculo falso. Esos solapes no entran en la cota de 00. El tratamiento del fallo es fiel al script.

**(8) Alcance.** El texto no sale del código \(M=1\), de \(U=FJ\), de \(\mu=3/5\), \(\nu=4/5\), \(z=i\) ni del marco \(B_T=F^T B\). No da valor numérico de \(c\). No decide la entrada 11. No convierte las muestras \(p_{01}(T)\) ni la cota que tiende a cero del informe anterior en evidencia. La frase sobre 01 y 10 es un corolario del mismo peso (en \(p_0\) el de 01 es \(9/25>0\)); no hace falta para el teorema.

## Objeciones

Ninguna. La frase «\(a\pm b\) congruente con \(\pm\pi/2\)» cubre \(a+b=3\pi/2\), y ese caso también da \(\cos^2 a=\sin^2 b\). La descomposición en \(\lambda_i(p)^T P_i(p)\) no necesita ramas continuas: vale el subespacio entero de \(P(p)\). \(\sigma(W_2)=\sigma_{\mathrm{ess}}(W_2)\) está justificado por la ausencia de espectro puntual, no solo por Weyl.

## Alcance que acepto

Solo este código, \(U=FJ\), \(\mu=3/5\), \(\nu=4/5\), \(z=i\), recta infinita y salida \(B_T=F^T B\): existe \(c>0\), sin valor numérico exhibido, tal que
\[
\liminf_{T\to\infty}\|E_T|00\rangle\|^2\ge c.
\]
Veredicto del contrato: `APPROXIMATE_RECOVERY_EXCLUDED` para esta recuperación aproximada. No es un no-go del autómata de Thirring, de otros códigos, de medidas, de auxiliares ni de otra geometría. La puerta exacta de \(T=1\) no queda tocada. La entrada 11 sigue sin decidir.
