<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 77845075a7acd93077e0247a85812d6eef0782f652153564037baa821b3f051d
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-01T19:58:52Z  fin: 2026-11-01T20:13:28Z
documento: /home/adnac/qca-causal-cones/reports/2026-10-31--h1-small-gaussian-profile.md ; último commit observado: 11ea2d8 ; sha256 de la copia enviada 98e96a47fdb584e921210e71c07559b773a2bd85258ab8fc1606ac6bc5972611
documento: /home/adnac/qca-causal-cones/theory/H1_SMALL_GAUSSIAN_PROFILE_GATE.md ; último commit observado: 067f8fa ; sha256 de la copia enviada d739db6b4b476c79c4a51d9a26f0dcf03dda31b5c3d818b8b0d040f6e972cddd
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--two-channel-t1-exact-signed-pq.md ; último commit observado: 7f68fa7 ; sha256 de la copia enviada c320aaa5060f343f1f0e726f663058f62fb6c1d2f19f71da43ef4bd759e24e8d
documento: /home/adnac/qca-causal-cones/reports/2026-09-24--schur-stability-physical-transfer.md ; último commit observado: 2e6af3a ; sha256 de la copia enviada caee6fa254fd83d64ac16ce6de2f04b359087e9a8f1668b0d4f93a089589bf65
documento: /home/adnac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: 3a44725 ; sha256 de la copia enviada a3849451dbac2d3e3a68ace47b0b50ae2bbf5ae3f6902c8bc92b9c2d820a42c5
documento: /home/adnac/qca-causal-cones/scripts/verify_small_gaussian_profile_algebra.py ; último commit observado: 11ea2d8 ; sha256 de la copia enviada 5647b1d52cce9392bac6d239ae4dd40b31b147b1e3541ee170b08c475990cfa2
documento: /home/adnac/qca-causal-cones/scripts/verify_regional_laplace_coefficient_gate.py ; último commit observado: ae6dd3e ; sha256 de la copia enviada d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2
entrada_grok.txt sha256 60df1c1e292ee78ff8416cad02addae2cccc391bb0c6d24ac3565c4acf5850b1
respuesta sha256 4faf3cc2be3ed4d4132d672befbf03a352649e85350e3217130798691414a0a2
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias. Los seis bloques cierran con las cuantificaciones del contrato: paridad exacta, coeficiente cuadrático general en \(N\) sin afirmar que sea distinto de cero, cota de núcleo integrado, comparación en la escala \(A_N=N^{-13/2}e^{-K_*N}\) con resto \(\varepsilon^4\), y supervivencia uniforme del signo y de la escala de \(L_+\) en un rectángulo \(|\varepsilon|\le\varepsilon_0\), \(N\ge N_0\). El puente y el teorema plano \(\sigma_2/I\) se usan solo dentro de sus hipótesis congeladas. No se atribuye a este gate novedad, H1/H1c general, E0, estabilidad general de la potencia \(13/2\) ni AdS. \(Q_N\neq0\) y su desarrollo asintótico siguen abiertos, como el propio informe declara.

## 1. PROFILE_AND_PARITY — PASS

Con la convención del contrato, \(\widehat v(k)=\pi^{3/2}e^{-|k|^2/4}\). En una dimensión, \(\int e^{-k^2/4}e^{-ikx}\,dk=2\sqrt\pi\,e^{-x^2}\), y el producto de tres factores recupera \(e^{-|X|^2}\). La medida positiva tiene masa
\[
a_0=\int\widehat v(k)\frac{d^3k}{(2\pi)^3}=1,
\]
porque \(\int_0^\infty r^2e^{-r^2/4}\,dr=2\sqrt\pi\) y el prefactor radial es \(1/(2\sqrt\pi)\). El mismo prefactor con \(\int_0^\infty r^3e^{-r^2/4}\,dr=8\) da \(a_1=4/\sqrt\pi\). La densidad radial citada, \(r^2e^{-r^2/4}/(2\sqrt\pi)\), es exactamente la de esa medida de masa 1. Para \(\vartheta=\varepsilon v\) y \(|\varepsilon|\le1\), la hipótesis F del puente queda uniformemente satisfecha: \(b\le1\), \(a_0\le1\), \(a_1\le4/\sqrt\pi\).

La norma de Wiener \(\|\psi\|_{\mathcal W}=\int_{\mathbb T^3}\|\widehat\psi\|\,d\mu\) domina el supremo por inversión de Fourier. \(D\) es unitario en cada fibra real y \(\beta\) también, así que ambos conservan \(\mathcal W\). La multiplicación por \(V_N\) es convolución con la periodización de una gaussiana positiva de masa 1; las imágenes periódicas suman y no cancelan, luego \(\|V_N\|_{\mathcal W\to\mathcal W}\le1\).

El recurso no truncado da \(\|J\phi_N\|_{\mathcal W}=C_\phi N^{-3/2}\) con \(C_\phi=\sqrt{3465}/(210\pi)\). En efecto, \(Z_N^{-1/2}=N^{3/2}\pi\sqrt{3465}/8\) y \(\int g\,d\mu=4/(105\pi^2 N^3)\); el producto es ese \(C_\phi\). Es la norma \(L^1\) de Fourier completa, no un corte espacial.

Paridad. \(ZDZ=D\), \(ZB_NZ=-B_N\) y \(ZJ=J\), así que \(ZU_\varepsilon Z=U_{-\varepsilon}\) y
\[
U_{-\varepsilon}^N J=ZU_\varepsilon^N J.
\]
Todo dato inicial del canal \(+\) (tanto \(J\phi_N\) como \(Jf_0\)) queda fijo por \(Z\). Por tanto la amplitud \(+\) es par y la \(-\) impar. De ahí \(L_+\), \(L_-\) y \(\mathcal F_N\) son pares, y \(\mathcal F_N'(0)=0\) para cada \(N\), sin conservación de momento. La objeción de que la anulación lineal exigiría una hipótesis espectral extra no se sostiene: sale solo de la conjugación por \(Z\).

## 2. FIRST_CORRECTION — PASS

Sea \(C(\varepsilon)=\exp(-i\varepsilon B_N/N)\). Como \(B_N^2=V_N^2\),
\[
C=I+\varepsilon\Bigl(-\frac{i}{N}V_N\beta\Bigr)+\varepsilon^2\Bigl(-\frac{V_N^2}{2N^2}\Bigr)+O(\varepsilon^3)
\]
en bloques, con el mismo término fuera de diagonal en ambos sentidos. Con \(U=CD\) actuando a la izquierda y correcciones iniciales nulas, las recurrencias del informe son exactas. Al resolver el canal \(-\),
\[
b_{1,j}=-\frac{i}{N}\sum_{\ell=0}^{j-1}S^{-(j-1-\ell)}V_NS^{\ell+1}\phi,
\]
y al sustituir en el canal \(+\) el producto de los dos factores \(-i\) produce el signo menos y el exponente \(-(j-\ell)\). Reindexando \(0\le j<k\le N-1\) se obtiene (7), con \(1/(2N^2)\) solo en la moneda única y \(1/N^2\) en el término a dos tiempos. No hay doble conteo: los pares ya van ordenados. Omitir la moneda única cambia el polinomio no conmutativo; el control formal a tres pasos del verificador apunta en esa dirección, pero la identidad general está en la recurrencia, no en ese caso.

El mayorante (6) es correcto: \(\sum_{n_1+\cdots+n_N=m}1/(n_1!\cdots n_N!)=N^m/m!\), luego el prefactor \(N^{-m}\) deja \(1/m!\). Vale en \(\mathcal W\) y en \(\ell^2\). Solo los \(m\) pares entran en \(\pi_+\). Por tanto, uniformemente en \(N\) y en \(y\),
\begin{align*}
\|\pi_+U_\varepsilon^NJ\phi-S^N\phi\|_\infty
&\le C_\phi N^{-3/2}(\cosh|\varepsilon|-1),\\
\|\mathscr A_N\phi\|_\infty&\le\tfrac12 C_\phi N^{-3/2},\\
\|\rho_N(\varepsilon)\|_\infty
&\le C_\phi N^{-3/2}\bigl(\cosh|\varepsilon|-1-\varepsilon^2/2\bigr).
\end{align*}
En \([0,1]\), \((\cosh x-1)/x^2\) y \((\cosh x-1-x^2/2)/x^4\) crecen (el numerador de cada derivada tiene cuarta derivada no negativa y ceros iniciales). De ahí los factores \(\cosh1-1\) y \(\cosh1-3/2\). Con \(\mathcal Q_N\) el coeficiente de \(\varepsilon^2\) en \(\mathcal F_N\), se tiene \(\mathcal F_N''(0)=2\mathcal Q_N\): el \(2\) es el paso de coeficiente de Taylor a derivada segunda, no un segundo \(1/2\) sobre el término a dos tiempos. No se afirma \(\mathcal Q_N\neq0\). El coeficiente completo de \(L_+\) tiene además \(2\Re\langle a_0,Eb_2\rangle\) y \(2\Re\langle b_0,Eb_2\rangle\); el informe no los absorbe en \(\mathcal Q_N\).

Aclaración, no fallo: (6) se leería mejor exhibiendo \(N^m/m!\) antes de cancelar. La igualdad escrita ya es cierta.

## 3. INTEGRATED_KERNEL — PASS

\(M(p)=S(p-i\xi_*)/\Lambda\) y \(I_N=\int_{\mathbb T^3}\|M^N\|\,d\mu\). El lema de radio del manuscrito, con las tres componentes de \(\xi_*\) no nulas, da \(\rho(M)\le1\) con igualdad exactamente en los ocho puntos de \(\Sigma=\{0,\pi\}^3\): el producto de elipses toca la frontera solo si cada \(\sin p_j=0\). No se descarta ningún máximo.

En \(p=0\), \(\operatorname{Re}\log(\lambda/\Lambda)=-\frac12 p^TQp+O(|p|^3)\) con \(Q=q_t(I-\hat u\hat u^T)+q_n\hat u\hat u^T\). Las dos expresiones de \(q_n\) coinciden:
\[
\frac{c}{d}\frac{(c^2-1)(c^2+2)}{c^4+c^2+1}
=\frac{c(c^2-1)^2(c^2+2)}{d^3}
=\frac{c(c^6-3c^2+2)}{d^3},
\]
usando \(d^2=c^6-1=(c^2-1)(c^4+c^2+1)\) y \((c^2-1)^2(c^2+2)=c^6-3c^2+2\). Para \(c>1\) se tiene \(q_t>0\) y \(q_n>0\). En una bola fija, el resto cúbico se absorbe y \(\operatorname{Re}\log(\lambda/\Lambda)\le -c_0|p|^2\).

En \(\alpha\in\Sigma\), \(f(\alpha+p-i\xi_*)=s_\alpha f(p-i\xi_*)\) con \(s_\alpha=\pm1\), así que los módulos de las raíces son idénticos a los de \(p=0\), no solo sus hessianos. El proyector de Riesz
\[
\frac{S-(s_\alpha\lambda)^{-1}I}{s_\alpha\lambda-(s_\alpha\lambda)^{-1}}
\]
es analítico y acotado en un cierre menor: el denominador en el silla es \(\Lambda-\Lambda^{-1}\neq0\). No se le supone autoadjunto. Como las raíces están separadas, \(M^N=\mu^N P+\mu^{-N}(I-P)\) sin parte nilpotente, y la no normalidad queda en \(\|P\|\), constante en ese cierre. La raíz subdominante aporta \(r^N\) con \(r<1\). Eso es (12).

Fuera de las ocho bolas, compacidad y radio estricto dan \(\rho\le r_{\mathrm{out}}<1\). La triangularización de Schur \(2\times2\), válida con raíz repetida, produce \(r_{\mathrm{out}}^N+CN r_{\mathrm{out}}^{N-1}\). Integrar la gaussiana tridimensional da \(O(N^{-3/2})\); el término \(N r^N\) también, porque \(\sup_{x\ge2}x^{5/2}e^{-ax}<\infty\). No se confunde \(\int\|M^N\|\) con \(\|\int M^N\|\): \(I_N\) es la integral de la norma, que es lo que entra en (16). No hace falta cancelación de los otros seis sillas; para esta cota superior suman del mismo orden.

## 4. SCALE_BOUND — PASS

El disco a profundidad \(\delta\) cumple \(|u_\perp|^2\le N\delta/2\). En el plano \(u\cdot x=k\) la proyección a las dos primeras coordenadas es inyectiva y no aumenta la norma euclídea, así que el número de sitios es \(\le(2\rho+2)^2\le8(1+\rho^2)\le8(1+N\delta)\), uniforme en la traslación y en \(\theta_N\). Además \(F_N,h_N\le64\delta^2/N^2\). Como \(M=\sigma_2\) es involución hermítica y \(|e^{it}-1|\le|t|\),
\[
\|(U_M-I)\phi_N(x)\|\le\frac\pi2 F_N(x)\,C_\phi N^{-3/2},
\]
coseno incluido. El peso de Alice es \(e^{\xi_*\cdot(x-x_*)}=e^{-t_*(\theta_N+j)}\) y el de Bob es \(e^{-\xi_*\cdot(y-y_*)}=e^{-t_*(\theta_N+j)}\): el tilt saliente lleva signo menos y no se inclina la cola global de la preparación.

Con \(\delta\le(j+1)/\sqrt3\), \(q^{ \theta+j}(\theta+j)^2\le q^j(j+1)^2\) y lo análogo al cubo,
\[
\sum_{j\ge0}e^{-t_*(\theta+j)}\delta_j^2(1+\delta_j)\le H,
\]
donde \(H\) es exactamente (13) vía \(\sum(j+1)^2 q^j=(1+q)/(1-q)^3\) y \(\sum(j+1)^3 q^j=(1+4q+q^2)/(1-q)^4\). Para \(N\ge2\), \(1+N\delta\le N(1+\delta)\) convierte el factor de área en \(N^{-1}\). Sale \(a_N\le256\pi C_\phi H\,N^{-5/2}\) y, sin el \(\pi/2\) del encoder, \(b_N(z)\le512 C_\phi H\,h\,N^{-5/2}\). El símbolo \(h\) de (15) es la cota escalar del espinor, no el perfil \(h_N\).

La representación de contorno es exacta sobre soportes finitos: \(f_0\) vive en Alice. Con fases de módulo uno,
\[
\bigl|2\Re\langle 1_Bz,ES^Nf_0\rangle\bigr|
\le2e^{-K_*N}a_Nb_N(z)I_N.
\]
Aplicada a (9), con \(D_*=2C_AC_BC_K\),
\begin{align*}
|\mathcal F_N(\varepsilon)-\mathcal F_N(0)|
&\le D_*(\cosh|\varepsilon|-1)A_N
\le C_*\varepsilon^2 A_N,\\
|\mathcal Q_N|&\le\tfrac12 D_*A_N,\\
|\mathcal R_N(\varepsilon)|
&\le D_*(\cosh1-\tfrac32)\varepsilon^4 A_N,
\end{align*}
en \(|\varepsilon|\le1\), con \(C_*=D_*(\cosh1-1)\) independiente de \(N\) y de \(\varepsilon\). La potencia es \(5/2+5/2+3/2=13/2\). El resto de orden \(\varepsilon^4\) está en la misma escala. La cota de continuidad en \(\ell^2\), sin los dos extremos físicos ni \(I_N\), no daría este orden; aquí sí se trazan ambos extremos.

## 5. FULL_SIGNAL_SURVIVAL — PASS

La objeción decisiva sería una continuidad en \(\varepsilon\) solo a \(N\) fijo, cuyo módulo empeorara con \(N\). No es el argumento del informe.

Las constantes del puente dependen de \(b,a_0,a_1\) y de la ventana fija \(W\), nunca por una división por \(\varepsilon\). En \(|\varepsilon|\le1\) esos tres parámetros están acotados por sus valores en \(|\varepsilon|=1\), y las estimaciones son monótonas en ellos. \(R,P,Q\) y la separación exterior son los del símbolo libre: no dependen de la moneda. Se elige un solo \(\rho_2\in(\rho,1)\) y un solo \(N_1\) tal que \(\rho+a/N\le\rho_2\) para todo \(|\varepsilon|\le1\). El conmutador comprimido cuesta \(|\varepsilon|a_1(v)/N\) y el resto de Taylor de la moneda \(\varepsilon^2/N^2\); tras el \(1/N\) ya presente en el generador, \(\|\mathsf A_\varepsilon-R_P\|=O(1/N^2)\) con constante común, y la suma telescópica deja \(O(1/N)\). La norma \(L^1\) de Bob cuesta a lo sumo \(e^{a_0}\le e\). Alice no depende de \(\varepsilon\). Así (18) tiene constantes uniformes en el intervalo, dependientes del \(W\) fijo. No se pide uniformidad en \(W\).

En \(\varepsilon=0\) el teorema plano, aplicado al par congelado \(M=\sigma_2\), \(M_B=I\), da \(L_{+,0}/A_N=C_0(\theta_N)+O(N^{-1/2})\) con \(m=\min(-C_0)>0\). La diferencia entre \(L_{+,0}\) y \(\mathcal F_N(0)\) es el término cuadrático de fuente, \(O(N^{-8}e^{-2K_*N})=o(N^{-1/2}A_N)\). Aunque se mayorara de forma pesimista por el \(O(N^{-7}e^{-K_*N})\) del puente, seguiría siendo \(O(N^{-1/2}A_N)\) y (19) permanecería válida. Hipótesis del teorema plano respetadas: caminata libre, mismas bolas, mismo recurso, mismo par.

Con \(\varepsilon_0=\min\{1,\sqrt{m/(4C_*)}\}>0\), independiente de \(N\), se tiene \(|\mathcal F_N(\varepsilon)-\mathcal F_N(0)|\le(m/4)A_N\). Después se elige \(N_0<\infty\), independiente de \(\varepsilon\), que absorba el resto plano y el error de puente, cada uno \(\le(m/4)A_N\). El cociente del error lineal es \(N^{-7}e^{-K_*N}/A_N=N^{-1/2}\); el cuadrático es menor. Para \(|\varepsilon|\le\varepsilon_0\) y \(N\ge N_0\),
\[
L_{+,\varepsilon}\le-\tfrac14 m A_N<0,
\qquad
\tfrac14 m A_N\le|L_{+,\varepsilon}|\le C A_N,
\qquad
|L_{-,\varepsilon}|\le C_W N^{-7}e^{-K_*N}=o(A_N).
\]
El balance es \(-m\) más tres contribuciones de \(m/4\). Los cuantificadores son de producto: \(\varepsilon_0\) no depende de \(N\) y \(N_0\) no depende de \(\varepsilon\). El signo adverso de \(\mathcal Q_N\) ya está cubierto por el valor absoluto de (17); por eso no hace falta \(\mathcal Q_N\neq0\). No se exige \(\varepsilon_0\) numérico: \(C_K\) y el umbral del resto plano no son efectivos, y el contrato no lo pide.

Los cuadráticos del puente se conservan agrupados como \(\|E^{1/2}(d_P+d_Q)\|^2\ge0\), de orden \(N^{-8}e^{-2K_*N}\). No se descarta un cruce firmado que pudiera competir con \(A_N\).

## 6. SCOPE_AND_CODE — PASS

El verificador algebraico, leído como texto y no ejecutado, encierra 21 identidades: momentos gaussianos, \(C_\phi\), paridad formal de \(Z\), la fórmula cuadrática no conmutativa a tres pasos con control negativo si se omite la moneda única, la factorización del hessiano, los dos momentos geométricos y la aritmética \(5/2+5/2+3/2=13/2\), \(-7+13/2=-1/2\). Su propio encabezado excluye núcleo analítico, restos uniformes, supervivencia del signo y coeficiente no nulo. El informe no presenta ese chequeo como barrido en \(N\) ni como ley asintótica. El verificador plano certifica, en su alcance escrito, álgebra, formas cerradas y margen de signo de los dieciséis coeficientes; no codifica el resto analítico \(O(N^{-1/2})\), que entra aquí como parte del teorema congelado. No he ejecutado ninguno de los dos.

El observable transferido es el de T1 y del puente: referencia física \(r_+=1_{\mathcal B}\pi_+U_\varepsilon^N J\phi_N\) y fuente completa \(f_0=(U_M-I)\phi_N\). \(\mathcal F_N\) no sustituye a \(L_+\); (18) los separa. Se distingue con claridad supervivencia de signo y escala, coeficiente asintótico no calculado, \(\mathcal Q_N\) posiblemente nulo, y H1 general. El estado declarado sigue siendo preliminar y pendiente de revisión. Eso coincide con el cierre del contrato.

**Reparaciones obligatorias: ninguna.**
