<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 897b933e5b6792ecf8413c2c0668b1ba0a1d0cb90795615fbb1eec489891a99a
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-12T08:54:11Z  fin: 2026-11-12T09:22:24Z
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-corona-reconciled-grok/ir-corona-anon.tex ; último commit observado: sin versionar ; sha256 de la copia enviada 71b94937f3164a1e0d7785b086b4c85d474ded858587c000c7454b4c0ba378b4
entrada_grok.txt sha256 716d87aa934f6a25b2df0a7ba3e2d580a75e1f8689ff68ac3ce3dffb47f052be
respuesta sha256 55d5b4a1b4079af8af06d89a89095b82ab8931ec4f2c3bc14f411c3b6de40354
-->

El manuscrito no se cae: las constantes, la fase, la potencia \(13/2\) y la reducción operacional rederivadas cierran. No es publicable tal cual. El lema de saltos no está probado en el texto, una frase de convexidad es falsa, y la no anulación de \(C\) no es una prueba cerrada.

**Dictamen global: REPAIR_REQUIRED.** Nada de lo rederivado justifica REJECTED.

## Bloques

**A. PASS.** \(T_N\le 9N^4e^{-JN}\) y \(\delta\le D_B\le 4T_N\le 36N^4e^{-JN}\) salen del texto. Con \(t=\log 2\), \(\cosh t=5/4\) y \(\cosh^3 t=125/64<17/8=\cosh\log 4\), el radio es \(<4\). El lema de potencias da \(\|S^N\|\le 4^N+32N\,4^{N-1}=(1+8N)4^N\le 9N\,4^N\). La separación \(u\cdot(y-x)\ge(3-\sqrt3/2)N\) convierte el exponente en \(-JN\), con \(J=(1-\sqrt3/2)\log 2\). Schur con \(\le N^3\) sitios produce el \(N^4\). En el bloque de una partícula, \(X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|\) cumple \(\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le 4T_N\), y \(D_B=\frac12(|\operatorname{tr} X|+\|X\|_1)\le\|X\|_1\). La constante \(4N^4\) de Lean no contradice el \(9\): es otra cota, y el texto lo dice.

**B. PASS** en lo analítico. \(I\) es convexa, \(I=0\) en \(\overline B(0,1)\) porque \(\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b\) (la derivada de \(\log\cosh\) y la concavidad de \(\tanh\) en \([0,\infty)\)), \(I=\infty\) fuera del cubo, y \(\Phi\) tiene hessiano semidefinido por Cauchy–Schwarz y \(\sum\sinh^2\xi_j\le\prod\cosh^2\xi_j-1\). El minimizador es único: \(v_*=u-\hat u/2\) es el único punto de contacto del plano de apoyo con la bola \(V_{\mathrm{reg}}\), y \(I(v)\ge I(v_*)+\sqrt3\,t_*(\hat u\cdot v-|v_*|)\). La forma cerrada de \(\cosh^2 t_*\) es la raíz positiva de \((1-\alpha^2)z^2-\alpha^2 z-\alpha^2=0\). \(3\alpha=3-\sqrt3/2\), así que el tilt \(\xi=(\log 2)u\) da \(K_*>J\) en sentido estricto; el vértice da \(I(u)=\log 4\) y \(K_*<\log 4\). El factor \(1+10N\) no está demostrado en el texto: depende de \(4e^{3t_*-\Phi_*}<9.2\).

**C. PASS.** El lema de un sitio es exacto: el volumen de la bola es \((6\pi^2)^{-1}N^{-3/2}\). El lema de Lipschitz reproduce \(K_e=\frac\pi2(2+8\sqrt3\pi)\) y \(K_d=\frac\pi2(1+16\sqrt3)\). La cota \(\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}\) para \(|x|\le N\) es igualdad en el umbral \(\cos\ge 1/2\), y \(m=11/(560\pi^2\,32^3)\) es el peso de \((N/32)^3\) sitios. Los tres cocientes del teorema salen de esos denominadores, incluido \(\|\Delta\|_1=2\sqrt{1-|z|^2}\) y \(1-|z|^2\ge(2-\sqrt2)m^2\).

**D. REPAIR_REQUIRED.** La forma asintótica, \(\mathcal K\), la potencia y la cancelación de fases están bien. La no anulación de las dieciséis parejas y el presupuesto escrito del término \(a_c\) no quedan cerrados.

## Objeciones

1. **Lema de saltos (sec. 2). Reparación necesaria, no fatal.** La prueba solo calcula el coeficiente de \(z_1z_2z_3\). No deduce los catorce saltos, las normas ni \(\sum\|S_d\|=4\), y esos datos entran en A y en B. El enunciado sí es cierto: \(c_j\) no tiene modo cero, así que la diagonal solo produce los ocho vértices, cada uno \(\frac14\) por un proyector diagonal; \(c_1s_2\) produce las cuatro diagonales de cara, de norma \(\frac14\); \(-is_1\) produce \((\pm1,0,0)\), de norma \(\frac12\). Suma \(8\cdot\frac14+4\cdot\frac14+2\cdot\frac12=4\). Además \(\det S=1\) y \(\operatorname{tr} S=2c_1c_2c_3\).

2. **Convexidad de \(\Phi\) (prueba de la tasa regional). Exposición, la conclusión es cierta.** \(\Phi\) es par, así que la derivada direccional en \(0\) vale \(+|x|\) en toda dirección. La frase «derivadas laterales \(-|x|\) y \(|x|\)» es falsa. El hessiano fuera del origen y \(\Phi(\xi)=|\xi|+O(|\xi|^3)\) bastan.

3. **Presupuesto de \(a_c\) (reducción y apéndice). Reparación necesaria, no un contraejemplo del \(O(N^{-1/2})\).** El texto afirma \(\langle r,Ea_c\rangle=O(N^{-17/2}e^{-K_*N})\), relativo \(O(N^{-2})\), y lo anota así en el presupuesto. El mismo apéndice mide el cociente de ese término frente al de \(N^{-13/2}\) en \(15.2\), \(9.4\), \(6.4\) para \(N=24,40,56\), y dice que escala como \(1/N\), no como \(1/N^2\). La cuenta del boceto (recurso \(N^{-3/2}\), \(c_N=O(N^{-4})\), área \(N\), Bob \(N^{-5/2}\), gaussiana \(N^{-3/2}\)) sí da \(N^{-17/2}\). No la he refutado, pero el manuscrito no explica su propio diagnóstico. Aunque el orden verdadero fuera \(N^{-15/2}\), seguiría dentro del \(O(N^{-1/2})\) del teorema principal: \(N^{-1}=o(N^{-1/2})\). Hay que reconciliar o bajar la potencia afirmada en el presupuesto.

4. **No anulación. NO_VERIFICADO en las dieciséis filas; la implicación lógica sí basta.** \(|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|\) implica que \(C\) tiene el signo de \(\ell_0\), usando \(|\Gamma_+-\overline\Gamma|\le\varepsilon_+\) y \(0\le\Gamma_-\le\varepsilon_-\), que se deducen del lema de profundidades. Esas desigualdades numéricas viven en certificados privados. No las doy por buenas. Para \((I,I)\) el margen no es ajustado: \(\ell_\pi/\ell_0=-(c+1)/(c-1)\approx-8.07\) y \((\overline\Gamma-\varepsilon_+)/\varepsilon_-\sim 10^3\). La columna \(1.47\cdot10^{-3}\) de la Tabla 1 coincide con \((\varepsilon_++\varepsilon_-(c+1)/(c-1))/\overline\Gamma\).

5. **«Dirección tangencial plana» (observación del exponente). Exposición.** El traslado común de los dos planos es un plano de dimensión \(2\), no una dirección. El exponente lineal es plano en esas direcciones; \(q_t>0\) curva el momento. La potencia no cambia: el jacobiano \(d^2\eta_t=(2/N)\,d^2\tau\) ya aporta \(N^{-1}\).

6. **Alcance (discusión, problema abierto 4). Exposición.** El prefactor \(288N^7\) no se demuestra aquí. Resumen, teoremas y discusión delimitan bien el carácter asintótico, que \(N_*\) no es explícito, que la admisibilidad no controla la escala \(e^{-K_*N}\) y que el punto de silla en \(\pi u\) está fuera de la banda infrarroja. Lean cubre el núcleo, la separación, el recuento, \(T_N\) y \(\delta\le 4T_N\); no cubre \(D_B\) ni la identificación con el protocolo. Eso está dicho dos veces y coincide.

No hay incoherencia bibliográfica demostrable solo con este texto. La relación \(\ell=2\sqrt3\,t\mapsto 2\Phi(tu)\) es álgebra interna; no he contrastado la cita con Cedzich–Joye–Werner–Werner.

## Lo que sí cierra, y dónde está el hueco de la fusión

La rama \(\lambda^{-1}\) queda controlada al encoger \(r_0\): con \(|\rho_3|\le\frac14\eta^TQ\eta\), la parte real del exponente normalizado es \(\le -2N\Phi_*+\frac34 N\eta^TQ\eta\), y basta \(r_0\) pequeño. Eso es compatible con \(r_0\le\frac12\min_{m\neq0}|2\pi m|\), con \(r_0\le d_0/2\) y con el resto cúbico. El lema espectral (e) vale para cualquier \(r_0>0\). Los pasos fusionados de planos, Poisson, Bob y (d) no se pisan.

Las sumas \(1/720\) y \(1/48\) son correctas: \(\sum_{n\neq0}(2\pi n)^{-4}=1/720\) y \(\sum_n|\pi(2n+1)|^{-4}=1/48\). La transformada \(\hat g_\tau(\omega)=c_g e^{-|\tau|^2/(4\sqrt3\,s_\omega)}/s_\omega^4\) con \(c_g=2\pi/(3\sqrt3)\) sale de \(\mathcal L\{H'''\}=2e^{-|\tau|^2/(4p)}/p\), \(p=s\sqrt3\), y del covolumen. Los prefactores \(16\pi/\sqrt3\) y \(32/\sqrt3\) salen de \(\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot 2R\) y de \(\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot 2R\), con \(2R=N/2\).

La cancelación cerca de \(\pi u\) es exacta. Las fases espaciales aportan \(e^{-2\pi i\theta_N}\); el símbolo, \((-1)^N\); el factor \(e^{-iN\pi u\cdot v_*}\) con \(u\cdot v_*=3-\sqrt3/2\) aporta otro \((-1)^N e^{i\pi\sqrt3 N/2}\). El producto de los dos signos es \(1\), y \(e^{i\pi\sqrt3 N/2}=e^{2\pi i\theta_N}\).

El ensamblaje da
\[
N^{-5}\cdot\frac{512\pi}{3}\cdot\sqrt{\frac{2\pi}{Nq_n}}\cdot\frac2N\cdot(2\pi)^{-3}
=N^{-13/2}\cdot\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}.
\]
Eso es \(\mathcal K\) sin \(\varphi_\partial\). La potencia es \(5+1/2+1=13/2\). Los tres reemplazos cuestan \(O(N^{-7})\), que es relativo \(O(N^{-1/2})\).

Los cuatro signos de (eq:Lexp) son correctos, con el producto escalar lineal en el segundo argumento. En particular \(\sigma_2\downarrow=-i\uparrow\) convierte \(i s_N\sigma_2\) en \(+s_N\uparrow\), y el cruce es \(+2\operatorname{Re}\). La cota \(N^{-17/2}\) del boceto es la de la objeción 3.

Tabla y apéndice coinciden en las filas que rehice, no por copia. \(P_{22}=(1+\alpha)/2\) y \(P_{12}=-(1+ic)\alpha/(2c^2)\) salen de \((S-e^{-\Phi}I)/(2D_*)\). Con eso, \(\ell_0(I,I)=-2\operatorname{Im}(x_0)\) reproduce \(-\frac{\sqrt3}{3}B\alpha(c-1)/c^2\), y \(\ell_\pi\) el signo opuesto. \((I,P_3)\) da el mismo imaginario porque el término real no entra en \(\operatorname{Im}\). \((\sigma_1,P_3)\) y \((\sigma_2,P_3)\) dan el mismo número porque \(x\propto-(1-i)\) y \(-2\operatorname{Im}\) frente a \(+2\operatorname{Re}\) coinciden. \(C(\sigma_3,\cdot)=-C(I,\cdot)\) es el cambio de signo del funcional, con \(a_c\) subdominante.

## Rederivado

Saltos, \(\det S=1\), (eq:SOS) —los dos polinomios difieren en \(0\)—, cono, separación \(3>(17/10)^2\), \(Z_N\), \(c_r\), \(m\), \(K_e\), \(K_d\), elipse numérica solo en casos, radio espectral en la dirección \(\le\), forma cerrada de \(\cosh^2 t_*\), unicidad de \(v_*\), \(J<K_*<\log 4\), identidades de medio periodo, carácter sobre \(\Lambda_0\), desarrollo de \(\lambda(\eta)\), \(q_t\) y \(q_n\), proyector \(P\), \(\theta_N\) común, paridad \((-1)^{j+j'}\), perfiles \(64/N^2\) y \(32\pi/N^2\), cola libre y el signo de \(H_W(\hat u)\downarrow\), Poisson, \(1/720\), \(1/48\), \(\overline\Gamma\), \(\varepsilon_\pm\), prefactores, \(\rho=O(N^{-2}(1+\delta'))\), compatibilidad de \(r_0\), rama recíproca, cancelación de fases, \(\mathcal K\), potencia \(13/2\), signos de (eq:Lexp), y las filas \((I,I)\), \((I,P_3)\), \((\sigma_1,P_3)\), \((\sigma_2,P_3)\).

## NO_VERIFICADO

Los dieciséis valores de \(\overline C\), el margen intervalo a intervalo, \(t_*=0.73575\ldots\), \(K_*=0.19052\ldots\), \(4e^{3t_*-\Phi_*}<9.2\), y el álgebra de Sylvester del lema de la elipse entrada por entrada. No he usado hipótesis para tapar eso. Las comprobaciones a mano (\(\varepsilon_+\approx0.049\), \(\varepsilon_-\approx0.00289\), \(\overline\Gamma\approx49\), \(e^{\Phi_*}\approx3.97\)) cuadran con los decimales impresos, pero no son una certificación por intervalos.

## Obligaciones

Completar la expansión del lema de saltos. Corregir la frase de las derivadas de \(\Phi\). Dejar probada en el texto, o citada como cota certificada con intervalo explícito, la desigualdad \(4e^{3t_*-\Phi_*}\le 10\). Explicar el cociente \(\sim 1/N\) del apéndice o retirar el \(O(N^{-2})\) relativo de \(a_c\). Mientras los certificados sigan fuera del manuscrito, la no anulación de las dieciséis parejas no está demostrada en el artículo; el criterio del margen sí es el correcto, y en \((I,I)\) sobra del orden de \(10^3\).
