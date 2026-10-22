<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ d32e8507c32aefc0acd0721a000eeeb2a261d824; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 9b4a1d94214494e23afece076b33e017e142a7c79f1b026be0dcea2a1a9b1557; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.163.0)
inicio: 2026-10-22T07:36:41Z  fin: 2026-10-22T07:41:27Z
documento: /home/ignac/qca-causal-cones/reports/2026-09-28--iid-message-discrimination-cost.md ; último commit observado: adba394 ; sha256 de la copia enviada 44244cd773cc0270b10bf8c75b7dc6c5f67a9a7001f83c426e6f69cf5ab26f81
documento: /home/ignac/qca-causal-cones/theory/SCALED_IR_SIGNALING_GATE.md ; último commit observado: 31b5797 ; sha256 de la copia enviada 325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c
entrada_astra.txt sha256 d8eb93c124c06b0283062ef2143d8c663f8b4f5ab0b01d62058ef477da6148e1
respuesta sha256 75bbdfdb49f6fd4e912240ee92fac1382e345b13a6ff7de772363f90384a5483
-->

**Veredicto global: PASS_WITH_REPAIRS.** Las derivaciones de (2)–(6) y (9)–(10) son correctas bajo las premisas heredadas y la interpretación de una partícula. La conclusión principal —coste \(\Theta(\delta_N^{-2})\) para el detector congelado— se sostiene. Hay una afirmación incorrecta sobre el coste de preparación, una justificación incompleta sobre \(C(\theta_N)\) y una ambigüedad de alcance que conviene eliminar.

Esta revisión es exclusivamente matemática y documental, en una ronda. Las asintóticas heredadas se aceptan como premisas; su demostración, las referencias externas y los estados del repositorio son **NO VERIFICADOS**.

**§2: PASS.** El límite, su positividad y la cota estricta superior se justifican.

Escribiendo \(Y=y/N\), la premisa uniforme implica
\[
r_N(y)^\dagger M_Br_N(y)
=N^{-3}R_0(Y)^\dagger M_BR_0(Y)+O(N^{-4}),
\]
porque \(R_0\) está acotado sobre la bola compacta y \(\|M_B\|\le1\). Al sumar \(O(N^3)\) sitios, el error es \(O(N^{-1})\). El término principal es la suma de Riemann de (1). El perfil extendido por cero es continuo, por lo que la frontera de la bola no introduce un problema.

Para comprobar la normalización con las convenciones del contrato, sea
\[
A=\int_{|q|\le1}|g(q)|^2\frac{d^3q}{(2\pi)^3}.
\]
El cambio de variable \(q=Np\) da exactamente \(Z_N=N^{-3}A\). Por tanto, con la representación de \(R_0\) declarada en §2,
\[
\widehat R_0(q)=A^{-1/2}g(q)e^{-iH_W(q)}\downarrow,
\]
y Plancherel da
\[
\int_{\mathbb R^3}\|R_0(Y)\|^2\,dY=1.
\]
Esto comprueba los factores de normalización, condicionado a la identificación heredada del campo límite.

La analiticidad real no exige que \(g\) sea analítica en el borde de su soporte. Basta que \(\widehat R_0\) sea integrable y tenga soporte compacto: su transformada inversa se extiende a una función entera de las coordenadas complejas. Por ello, si \(M_B^{1/2}R_0\) se anula en una bola abierta, se anula en todo \(\mathbb R^3\). La unicidad de Fourier obliga entonces a anular \(M_B^{1/2}\widehat R_0\).

Para \(I,P_1,P_2\), esto contradice su valor en \(q=0\). Para \(P_3\), la comprobación decisiva es
\[
\left.\partial_{q_1}
\big[P_3g(q)e^{-iH_W(q)}\downarrow\big]\right|_{q=0}
=-iP_3\sigma_1\downarrow
=-i\binom10\ne0.
\]
Si se deriva la transformada completa, aparece además el factor no nulo \(A^{-1/2}\). Su omisión en el texto no afecta al argumento de no nulidad.

Así, para cada detector existe un punto interior donde
\(\|M_B^{1/2}R_0\|^2>0\); por continuidad, existe un abierto de contribución positiva. Esto prueba \(p_\infty^{(M_B)}>0\).

La desigualdad estricta superior también es correcta:
\[
p_\infty^{(M_B)}
\le\int h(Y)\|R_0(Y)\|^2\,dY<1.
\]
En efecto, \(1-h>0\) casi en todas partes y \(\|R_0\|^2\) tiene integral uno. Por tanto,
\(\int(1-h)\|R_0\|^2>0\).

Finalmente, \(\delta_N\to0\) hace que ambos mensajes converjan al mismo límite interior. La separación \(m\le p_{b,N}\le1-m\) es válida eventualmente. Además, **puede elegirse un mismo \(m>0\) y un mismo \(N_0\) para los dieciséis pares**: hay cuatro límites positivos y menores que uno, y una cantidad finita de convergencias. No se obtiene un \(N_0\) efectivo.

**§3: PASS_WITH_REPAIRS.** Las fórmulas estadísticas y sus constantes son correctas. La reparación afecta a la afirmación de acotación de \(C\), no al orden en \(\delta_N\).

Para priors iguales, cada cadena \(x\in\{0,1\}^R\) contribuye al error óptimo con
\[
\frac12\min\{P_0(x),P_1(x)\}.
\]
Agrupar las cadenas por su número \(k\) de detecciones produce exactamente (2). El conteo es suficiente porque la razón de verosimilitudes depende únicamente de \(k\). Los empates no alteran el error óptimo.

Para comprobar (3), las identidades
\[
\sum_x(\sqrt{P(x)}-\sqrt{Q(x)})^2=2(1-B),
\qquad
\sum_x(\sqrt{P(x)}+\sqrt{Q(x)})^2=2(1+B)
\]
dan
\[
1-B\le\operatorname{TV}(P,Q)
\le\frac12\sqrt{2(1-B)\,2(1+B)}
=\sqrt{1-B^2}.
\]
La afinidad del producto es \(B_N^R\). Sustituir en
\(P_e^*=(1-\operatorname{TV})/2\) demuestra (3), incluidos todos sus factores.

La cota inferior de (3), junto con \(P_e^*\le\epsilon\), exige
\[
B_N^{2R}\le4\epsilon(1-\epsilon).
\]
Como \(B_N=e^{-a_N}\), resulta
\[
R\ge\frac{\log[1/(4\epsilon(1-\epsilon))]}{2a_N}.
\]
La condición suficiente \(B_N^R/2\le\epsilon\) produce el extremo superior de (4). El techo está correctamente colocado; podría añadirse un techo al extremo inferior para reforzarlo, pero no es necesario.

La expansión puede comprobarse término a término:
\[
\sqrt{p(p+d)}
=p+\frac d2-\frac{d^2}{8p}+\frac{d^3}{16p^2}+O(d^4),
\]
\[
\sqrt{(1-p)(1-p-d)}
=(1-p)-\frac d2-\frac{d^2}{8(1-p)}
-\frac{d^3}{16(1-p)^2}+O(d^4).
\]
Los términos lineales se cancelan y queda
\[
B_N=1-\frac{d^2}{8p(1-p)}+O(|d|^3).
\]
Para justificar uniformidad basta exigir \(p\in[m,1-m]\) y \(|d|\le m/2\): las terceras derivadas permanecen acotadas en ese dominio. La convergencia \(\delta_N\to0\) garantiza esta condición eventualmente, uniformemente sobre la familia finita.

Como \(-\log(1-x)=x+O(x^2)\),
\[
a_N=\frac{\delta_N^2}{8p_{0,N}(1-p_{0,N})}
+O(\delta_N^3),
\]
y después
\[
a_N=\frac{\delta_N^2}
{8p_\infty^{(M_B)}(1-p_\infty^{(M_B)})}(1+o(1)).
\]
No hace falta que \(p_{0,N}-p_\infty\) sea comparable con \(\delta_N\): basta que tienda a cero.

Para \(\epsilon\in(0,1/2)\) fijo, ambos numeradores de (4) son constantes positivas. Por tanto,
\[
R_\epsilon=\Theta(\delta_N^{-2}),
\]
y la sustitución de la asintótica heredada da correctamente (5). No demuestra un prefactor óptimo ni uniformidad cuando \(\epsilon\) depende de \(N\).

**Reparación obligatoria 1 — laguna de justificación.** La separación uniforme de \(C\) respecto de cero **no implica** que \(C\) esté acotada superiormente. La tabla de premisas no declara esa cota superior ni una regularidad de \(C\) que la implique. Debe explicitarse como premisa heredada o retirarse la frase «la dependencia oscilante de \(C\) permanece acotada».

La tasa logarítmica puede conservarse sin esa afirmación. Para los pares congelados, \(\delta_N\le D_B(N)\) y (8), junto con el resto relativo eventualmente menor que \(1/2\), dan
\[
|C(\theta_N)|
\le8N^{19/2}(1+10N)=O(N^{21/2}).
\]
Combinado con \(|C(\theta_N)|\ge c>0\), esto implica
\[
\frac{\log|C(\theta_N)|}{N}\longrightarrow0.
\]
Así, (5) sí conduce a
\[
\frac{\log R_\epsilon(N)}N\longrightarrow2K_*.
\]
Esta comprobación solo necesita controlar la sucesión efectiva \(\theta_N\); no demuestra una cota para un parámetro \(\theta\) arbitrario.

La segunda vía también es correcta. Si \(d>0\), se decide \(1\) cuando la media supera el punto medio; si \(d<0\), se invierte la orientación. Bajo cualquiera de los bits, un error exige una desviación de al menos \(\delta_N/2\). Por Chebyshev,
\[
P_b(\text{error})
\le\frac{p_{b,N}(1-p_{b,N})/R}{(\delta_N/2)^2}
\le\frac1{R\delta_N^2}.
\]
La constante uno es correcta.

Por otra parte,
\[
\chi^2(P_1\|P_0)
=\frac{d^2}{p_0}+\frac{d^2}{1-p_0}
=\frac{\delta_N^2}{p_0(1-p_0)}.
\]
La identidad de producto se obtiene multiplicando los segundos momentos de la razón de verosimilitudes. Cauchy–Schwarz da
\[
\operatorname{TV}(P_1^R,P_0^R)
\le\frac12\sqrt{
\left(1+\frac{\delta_N^2}{p_0(1-p_0)}\right)^R-1}.
\]
Exigir \(\operatorname{TV}\ge1-2\epsilon\) produce exactamente (6).

No hay confusión entre error medio y error por bit: (2)–(6) se formulan para error medio; para controlar ambos errores individuales, la cota inferior sigue siendo necesaria y Chebyshev da una condición suficiente del mismo orden. No se afirma igualdad entre sus constantes óptimas.

El caso límite también pasa. Para \(p_0=0\), cualquier detección identifica el mensaje \(1\); la única cadena ambigua es la de ceros. Por ello,
\[
P_e^*=\frac12(1-\delta)^R,\qquad
R_\epsilon=
\left\lceil
\frac{\log(1/(2\epsilon))}{-\log(1-\delta)}
\right\rceil
=\Theta_\epsilon(\delta^{-1})
\]
cuando \(\delta\downarrow0\). Esta es una fórmula de error medio, coherente con el contrato estadístico.

**§4: PASS_WITH_REPAIRS.** El recuento de recursos y el tratamiento de postselección son correctos, salvo una condición presentada incorrectamente como necesaria.

Los \(RN\) pasos-copia son el trabajo agregado de las evoluciones. Los \(RN\) ticks secuenciales y los \(N\) ticks paralelos corresponden a las modalidades descritas; no incluyen preparación y medición ni fijan una duración física.

**Reparación obligatoria 2 — error matemático en una condición necesaria.** La frase «Sólo si el coste por copia fuese como máximo polinómico podría afirmarse que el coste total tiene la misma tasa exponencial» es falsa.

Si el coste por copia es \(c_N\ge1\) y el coste agregado es \(R_\epsilon c_N\),
\[
\frac{\log(R_\epsilon c_N)}N
=\frac{\log R_\epsilon}N+\frac{\log c_N}N.
\]
Basta que \(\log c_N=o(N)\). Por ejemplo, \(c_N=e^{\sqrt N}\) es superpolinómico y conserva la tasa \(2K_*\).

Debe sustituirse por: «Un coste por copia subexponencial en \(N\), en particular polinómico, conservaría la tasa exponencial del coste agregado. Aquí no se demuestra ese control».

La distribución ternaria (7) incluye correctamente el fallo y ambos resultados condicionados al éxito. Para intentos independientes con probabilidad común \(s>0\), el tiempo hasta \(r\) éxitos tiene esperanza \(r/s\). Esto no es un presupuesto determinista ni una garantía de cola.

Si \(s_0\ne s_1\), los fallos y tiempos de espera contienen potencialmente información. La contracción de TV se aplica al posprocesamiento mediante una misma regla bajo ambas hipótesis. Condicionar al éxito puede aumentar la distancia condicionada, pero no convierte por sí solo esa distancia en un ahorro operacional. El documento mantiene correctamente esa distinción.

La implementación y localidad concreta de las proyecciones de C3 son **NO VERIFICADAS** con los documentos disponibles. Su exclusión del protocolo congelado es consistente con el contrato.

**§5: PASS_WITH_REPAIRS.** La telescopación y la cota de repeticiones son correctas; debe precisarse el dominio de las unitarias.

Con la convención
\[
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\]
se tiene
\[
\rho_0^{\otimes R}-\rho_1^{\otimes R}
=\sum_{j=1}^R
\rho_0^{\otimes(j-1)}
\otimes(\rho_0-\rho_1)
\otimes\rho_1^{\otimes(R-j)}.
\]
La desigualdad triangular y
\(\|A\otimes B\|_1=\|A\|_1\|B\|_1\), junto con
\(\|\rho_b\|_1=1\), dan
\[
D(\rho_0^{\otimes R},\rho_1^{\otimes R})
\le R D(\rho_0,\rho_1)\le R\eta_N.
\]
Además, \(D\le1\). La fórmula de discriminación binaria óptima produce exactamente (9), incluso permitiendo una medición conjunta sobre las salidas.

Para usos distintos predeterminados, la misma expansión da
\[
D\!\left(\bigotimes_{j=1}^R\rho_{0,j},
         \bigotimes_{j=1}^R\rho_{1,j}\right)
\le\sum_{j=1}^R D(\rho_{0,j},\rho_{1,j})
\le R\eta_N.
\]
La condición necesaria es la estructura de producto bajo cada bit y la aplicación de (8) a cada uso.

Exigir error medio \(\le\epsilon\) obliga a
\[
R\eta_N\ge1-2\epsilon.
\]
Para \(K_*>0\), eventualmente
\[
\eta_N=4N^3(1+10N)e^{-K_*N},
\]
de donde
\[
R\ge
\frac{1-2\epsilon}{4N^3(1+10N)}e^{K_*N}
=\frac{1-2\epsilon}{40}N^{-4}e^{K_*N}(1+o(1)).
\]
La constante y el signo exponencial de (10) son correctos.

Si \(R=e^{o(N)}\), entonces \(R\eta_N\to0\). En consecuencia, el error óptimo tiende a \(1/2\). Esto es una obstrucción necesaria; no establece alcanzabilidad de la tasa \(K_*\).

**Reparación obligatoria 3 — precisión de alcance.** Debe indicarse expresamente que las unitarias de (8) actúan en el espacio de una partícula y satisfacen
\[
U=U_A\oplus I_{A^c},
\]
o que sus implementaciones en Fock preservan el sector de una partícula.

Un estado inicial de una partícula, por sí solo, no garantiza que una unitaria local arbitraria en Fock deje la salida en ese sector. La justificación mediante bloques de vacío y una partícula necesita esa restricción. Bajo la lectura sectorial natural del contrato, no hay un error en (8)–(10); la reparación elimina una lectura más amplia que la prueba descrita no cubre.

Como comprobación adicional del factor cuatro, si \(v_b\) es la componente de la partícula en Bob,
\[
\rho_{b,B}=(1-\|v_b\|^2)|0\rangle\langle0|
+|v_b\rangle\langle v_b|.
\]
Entonces
\[
D_B\le(\|v_0\|+\|v_1\|)\|v_1-v_0\|
\le2\|v_1-v_0\|.
\]
La premisa \(\|v_1-v_0\|\le2T_N\) conduce a \(D_B\le4T_N\). Para estados iniciales mixtos de una partícula, la misma cota se extiende por convexidad. La estimación espacial de \(T_N\) permanece **NO VERIFICADA**, conforme al encargo.

**Alcance de §6: PASS.** Las exclusiones son suficientes para impedir que este informe se interprete como una frontera operacional universal: faltan geometrías y direcciones uniformes, recursos generales, entradas correlacionadas, adaptatividad, comunicación interior y estabilidad. También es correcta la separación entre el límite escalado de red y una duración física.

Las obligaciones de admisibilidad IR y los estados terminales del contrato no quedan certificados por esta revisión. El documento 1 no pretende certificarlos ni promocionar un gate, por lo que no hay contradicción. La compatibilidad concreta con el cierre de 4B es **NO VERIFICADA**: el expediente no está adjunto.

El resultado matemático central sobrevive a las tres reparaciones: \(\Theta(\delta_N^{-2})\) para los dieciséis pares congelados, con constantes uniformizables por finitud, y una obstrucción uniforme de tasa necesaria \(K_*\) para productos de salidas de protocolos de una partícula. Ninguna de esas conclusiones establece una tasa óptima universal ni una frontera en \(c\).