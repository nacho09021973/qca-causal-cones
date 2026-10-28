<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 16568209771dc898346bd4af0c78ec10530c3b9e; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 91bee96b008d707188487ad26871460296ba02cf99300ae272afd81dce1d64e6; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 df3563a2081dbba73415d9508eb22e52925ed53059ab56405c30b5b56c0456d9
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-10-28T07:45:05Z  fin: 2026-10-28T07:59:26Z
documento: /home/ignac/qca-causal-cones/reports/2026-09-28--iid-message-discrimination-cost.md ; último commit observado: 262ce03 ; sha256 de la copia enviada 9838662a64401b1ae5e34f61599d3d3fbd4279096f8a9c1321b1c166b5954e01
documento: /home/ignac/qca-causal-cones/theory/SCALED_IR_SIGNALING_GATE.md ; último commit observado: 31b5797 ; sha256 de la copia enviada 325fd41679e9f43c4e697414c1f8936e4576afe2cd8c866c2c32515eba87843c
entrada_grok.txt sha256 8b5acba6a1a13352a5d984a36b41389daeb980029a9ebeacc46522e0fdaae0de
respuesta sha256 00b709765b48b65401505d1c6445428e0b123d143a7ec5556e0421dcbe2e3e39
-->

La versión reparada queda en **PASS**. Las tres reparaciones son matemáticamente correctas; no hay reparación obligatoria.

| Reparación | Veredicto | Tipo de observación residual |
|---|---|---|
| 1. Cota de \(C\) | **PASS** | Cuantificador eventual; la cota es suficiente, no necesaria |
| 2. Coste por copia | **PASS** | Ninguna |
| 3. Alcance de (8) | **PASS** | El manuscrito de la cota no está en esta sesión |
| Global | **PASS** | Residuos de redacción, no de inferencia |

Las asintóticas de la corona (\(\delta_N\), \(r_N\), \(D_B\), \(K_*>0\), y que \(C\) queda uniformemente separado de cero) se usan solo como premisas.

## 1. Cota de \(C\)

Premisa heredada, para cada par congelado:

\[
\delta_N=\lvert C(\theta_N)\rvert\,N^{-13/2}e^{-K_*N}(1+\rho_N),\qquad\rho_N=O(N^{-1/2}).
\]

«Resto relativo» es ese \(\rho_N\). Hace falta la lectura bilateral \(\lvert\rho_N\rvert<1/2\): como \(\rho_N\to0\), existe \(N_*\) tal que para \(N\ge N_*\) se tiene \(1/2<1+\rho_N<3/2\). Una lectura solo por la derecha (\(\rho_N<1/2\), permitiendo \(\rho_N\to-1\)) no bastaría: el denominador podría hacerse arbitrariamente pequeño y el factor 2 fallaría. Con la premisa \(O(N^{-1/2})\) esa lectura bilateral es la correcta, y basta.

Dirección de las desigualdades, para \(N\ge N_*\):

\[
\lvert C\rvert
=\frac{\delta_N\,N^{13/2}e^{K_*N}}{1+\rho_N}
\le 2\,\delta_N\,N^{13/2}e^{K_*N}.
\]

El contrato fija \(D_B\ge\delta\), y la premisa es \(D_B(N)\le4N^3(1+10N)e^{-K_*N}\). El recorte \(\min\{1,\cdot\}\) de (8) no afloja la cuenta: \(\min\{1,x\}\le x\). Por tanto

\begin{align*}
\lvert C(\theta_N)\rvert
&\le 2\cdot4N^3(1+10N)e^{-K_*N}\cdot N^{13/2}e^{K_*N}\\
&=8\,N^{3+13/2}(1+10N)
=8\,N^{19/2}(1+10N).
\end{align*}

El exponente \(3+13/2=19/2\) y la constante \(8=2\cdot4\) cierran. La desigualdad es no estricta aunque \(\lvert\rho_N\rvert<1/2\) sea estricta. El \(N_*\) a partir del cual \(\lvert\rho_N\rvert<1/2\) es **NO VERIFICADO**: depende de la constante del \(O\) del otro manuscrito. Para todo lo que se deduce después solo importa que sea finito.

Esa cota no es necesaria para nada de lo que se concluye con ella.

- Dado (4) y \(a_N=\delta_N^2\big/\bigl(8p_\infty(1-p_\infty)\bigr)\,(1+o(1))\) con \(p_\infty\in(0,1)\), se tiene \(R_\varepsilon(N)=\Theta(\delta_N^{-2})\). Sustituyendo la premisa, \(\delta_N^{-2}=\Theta\bigl(N^{13}e^{2K_*N}/\lvert C(\theta_N)\rvert^2\bigr)\) en cuanto \(\rho_N\to0\) y \(C\neq0\). Eso es exactamente (5) con \(C\) explícito, y no usa la cota polinómica. Mantener \(C\) dentro del \(\Theta\) es obligatorio: la cota nueva no impide que \(\lvert C\rvert\) crezca, así que \(C\) no puede absorberse en la constante del \(\Theta_{\varepsilon,M,M_B}\).
- El límite sí usa la cota, pero solo como mayorante cómoda. De (5),

\[
\frac{\log R_\varepsilon(N)}{N}
=2K_*+\frac{13\log N}{N}-\frac{2\log\lvert C(\theta_N)\rvert}{N}+o(1).
\]

La condición necesaria y suficiente, dadas las premisas de §2 y §3, es \(\log\lvert C(\theta_N)\rvert=o(N)\). La cota polinómica da la mitad superior, \(\log\lvert C\rvert=O(\log N)\). La mitad inferior ya estaba en la tabla de §1: \(C\) uniformemente separado de cero, esto es \(\lvert C\rvert\ge c>0\), que no fue retirada. Con las dos, \(\log R_\varepsilon(N)/N\to2K_*\).

La frase «es una cota polinómica, así que el límite se mantiene» es correcta dentro del documento reparado, no aislada: la cota sola da \(\liminf(\log R_\varepsilon)/N\ge2K_*\); el \(\limsup\le2K_*\) lo da la separación de cero. Cualquier mayorante \(\lvert C\rvert\le e^{o(N)}\) serviría igual. Además el 8 no es agudo: como \(\rho_N\to0\), el mismo argumento produce \(\limsup\lvert C\rvert\big/\bigl(N^{19/2}(1+10N)\bigr)\le4\), de modo que cualquier constante \(>4\) vale desde algún \(N\). Nada de esto contradice \(\le8\).

El \(o(1)\) de \(a_N\) sigue siendo válido con \(C\) polinómico, porque \(\delta_N\le D_B(N)\to0\) y §2 mantiene \(p_{b,N}\) en un compacto de \((0,1)\). El caso límite \(p_0=0\), \(p_1=\delta\), \(R=\Theta(\delta^{-1})\), queda fuera de ese compacto y no afecta a (5).

## 2. Coste por copia

Sea \(c_N\) el coste por copia y el coste agregado el producto \(R_\varepsilon(N)\,c_N\) (o \(R_\varepsilon(N)\,N\,c_N\): el factor \(N\) no cambia la tasa). Entonces

\[
\frac{\log(R_\varepsilon c_N)}{N}
=\frac{\log R_\varepsilon}{N}+\frac{\log c_N}{N}.
\]

Si \(\log R_\varepsilon/N\to2K_*\), la tasa del agregado sigue siendo \(2K_*\) si y solo si \(\log c_N=o(N)\), es decir \(c_N=e^{o(N)}\). Es una condición bilateral: \(c_N=e^{N/\log N}\) la cumple y conserva la tasa; \(c_N=e^{-N}\) no es \(e^{o(N)}\) y bajaría la tasa a \(2K_*-1\). El paréntesis del texto dice exactamente eso, no el limsup unilateral que a veces se lee en «subexponencial».

«En particular polinómico» es correcto: \(N^k\) cumple \(\log c_N=k\log N=o(N)\), y es un subcaso estricto. La frase no dice que el control esté demostrado, no atribuye a \(R c_N\) el \(\Theta\) completo de (5) (falso si, por ejemplo, \(c_N=e^{\sqrt N}\)), ni condiciona el volumen \(RN\) de pasos-copia, cuyo logaritmo ya da \(2K_*\) sin hipótesis extra. No afirma de más ni de menos.

## 3. Alcance de (8)–(10)

La prueba descrita en §5 necesita, a la vez, las dos cosas, y no necesita más:

- Entrada de una partícula, y salida en ese mismo sector, para que el estado reducido en \(B_N\) tenga solo bloque de vacío y bloque de una partícula.
- Sobre ese sector, \(U=U_A\oplus I_{A^c}\). Si no, \((U-I)\psi\) no está soportado en \(A_N\) y \(\lVert P_B S^N(U-I)\rVert\le2\lVert P_B S^N P_A\rVert\) no vale para todo estado inicial. Para un unitario, \(P_{A^c}U=P_{A^c}\) equivale a esa suma directa.

Preservar el sector sin la suma directa no basta (una traslación preserva el sector y destruye la cola). La suma directa sobre el sector de una partícula sí basta para el argumento de norma y de bloques; no hace falta restringir \(U_A\) a la familia \(\{I,\sigma_i\}\), ni controlar sectores de más partículas, porque (8) solo cuantifica entradas de una partícula. El «sus» de la adenda ata la implementación de Fock a esas mismas \(U\), no a cualquier unitario que preserve el sector. Los dieciséis encoders del contrato caen dentro: en una partícula son multiplicación por \(e^{i\theta F_A(x)M}\) dentro de \(A_N\) e identidad fuera.

La segunda frase de la adenda no recorta de más: una unitaria local que saque la salida del sector deja de tener los dos bloques, y la prueba indicada no la cubre. Que la cota siga siendo cierta para esas unitarias por otro argumento es **NO VERIFICADO**.

(9) y (10) solo usan (8) como caja negra, más independencia de las copias. La telescopía \(\lVert\bigotimes\rho_0-\bigotimes\rho_1\rVert_1\le R\lVert\rho_0-\rho_1\rVert_1\) y Helstrom \(P_e\ge(1-D)/2\), con \(D\in[0,1]\), dan

\[
\min\{1,R\eta_N\}\ge1-2\varepsilon\iff R\ge\frac{1-2\varepsilon}{\eta_N}.
\]

Para \(N\) grande, \(\eta_N=4N^3(1+10N)e^{-K_*N}\asymp N^4 e^{-K_*N}\), así que el umbral es \(\Omega_\varepsilon(N^{-4}e^{K_*N})\). El grado \(-4\) viene de \(N^3\cdot(1+10N)\); no sobra ni falta un \(N\). Estrechar (8) estrecha (9)–(10) en el mismo grado, que es lo que la adenda dice. Sigue en pie que \(R=e^{o(N)}\) no separa el error de \(1/2\), y que \(2K_*\) no se transfiere a toda la clase: (9) es lineal en la distancia de traza, mientras que el detector congelado paga \(1/\delta_N^2\) por el fondo en \((0,1)\).

§6 sigue coherente. El punto 2 ya deja fuera muchas partículas, ancillas, entradas correlacionadas y adaptatividad; no afirma que (8) cubra unitarias que salen del sector. «La clase de una partícula descrita en §5», leída con la adenda, es exactamente esta clase.

## 4. Lo que la adenda no deja incoherente

La única frase retirada, «la dependencia oscilante de \(C\) permanece acotada», no alimenta ninguna otra inferencia. (5) ya llevaba \(C(\theta_N)\) explícito; «no se sustituye \(C\) por una constante» sigue siendo cierto, y de hecho necesario. La separación de cero de la tabla de §1 es una cota inferior y no contradice la mayorante polinómica. \(\delta_N\to0\), usado en §2, sale de \(\delta_N\le D_B(N)\to0\) sin usar que \(C\) esté acotado. El estado del encabezado («sin revisión independiente») queda sustituido por el estado de la adenda; es residuo editorial, no una afirmación matemática en conflicto.

El argumento propio de §2, que (5) necesita para tener \(p_\infty\in(0,1)\), cierra si se acepta la representación de \(R_0\): soporte compacto en momento implica analiticidad real; anularse en la bola de Bob implicaría anularse en todas partes; \(I\), \(P_1\) y \(P_2\) contradicen el valor en \(q=0\), y \(P_3\) contradice \(\partial_{q_1}\widehat{R_0}(0)\propto -i P_3\sigma_1\mathrm{down}\neq0\); Plancherel más \(0\le h<1\) en casi todo punto da \(p_\infty<1\). El error \(O(N^{-5/2})\) de amplitud, sumado en \(O(N^3)\) sitios, es \(O(N^{-1})\). La fórmula de Fourier de \(R_0\) es **NO VERIFICADO**; la deducción a partir de ella no tiene hueco.

## NO VERIFICADO

Depende de fuentes que no están en la sesión: el teorema de asintótica principal y la separación de \(C\); `thm:upper`, `thm:rate` (d) y `lem:tail`; el valor de \(K_*\) y el \(N\) desde el cual \(\lvert\rho_N\rvert<1/2\); la prueba manuscrita de (8) más allá del esquema \(\lVert v_1-v_0\rVert\le2T_N\) y los dos bloques; las páginas citadas de Fuchs–van de Graaf y del PDF local (las desigualdades (3), (4) y (6) sí se rehicieron y cuadran); los dictámenes Astra y Gemini; la compatibilidad con el cierre de 4B.

Reparaciones obligatorias: ninguna.
