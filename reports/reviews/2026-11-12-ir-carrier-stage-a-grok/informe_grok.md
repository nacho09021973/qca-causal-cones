<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 9b0810646a24d3142ecbf79154de5f65c8570ecc7d4e3e477d760a04dfa10ca9
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-12T11:48:13Z  fin: 2026-11-12T12:12:16Z
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/IR_CARRIER_DICHOTOMY_GATE.md ; último commit observado: sin versionar ; sha256 de la copia enviada cf4186fef149944263c4d9d1bebf72391723438496dd09b43fb9b49d3ca176fa
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/IR_CARRIER_DICHOTOMY_GATE_AMENDMENT_1.md ; último commit observado: sin versionar ; sha256 de la copia enviada 8a567a2908de8927ce1c622d87d08369aff8c8a0c79469e394343d9b783850fa
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/2026-11-12--ir-carrier-stage-a.md ; último commit observado: sin versionar ; sha256 de la copia enviada dc89aef50e2255f2d00b8d4008ea799918fbd3b1eb0f1577d49744024ff13a62
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/2026-11-12--general-ir-rate-stage2-leading-term.md ; último commit observado: sin versionar ; sha256 de la copia enviada ace6c7bfbbbebb7f0c42a89c926c2bf637e84c7a655dcb2a040fab05f54e14c0
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/2026-11-12--ir-carrier-r1-diagnostic-stdout.txt ; último commit observado: sin versionar ; sha256 de la copia enviada b20f65ccb6a5401faae6d74359dc6292e59f18b5e5edfd38c7d1fff7c7a9123a
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-ir-carrier-stage-a-grok/ir-corona-anon.tex ; último commit observado: sin versionar ; sha256 de la copia enviada 70b74038aa81d0ca0982e43209af318c1ee64352a21db5f616968bd9946a28f9
entrada_grok.txt sha256 eece7683423da7ddfea69cc882f93c4bfe395718cd05ed2e09b41b2692536e59
respuesta sha256 c8dc2a1f8e0a3dc02739dd58c342c6bb2641c62c07ec599343a5d0528a2f5a21
-->

**Dictamen: REPAIR_REQUIRED**

La afirmación no está demostrada bajo todo el bloque de hipótesis que la enmienda declara. Cierran la reducción de fases a \(e^{iN\psi_k}\), las sumas de profundidad con \(\sigma=\kappa+i\varphi\), la herencia de las cotas \(O(N^{-1/2})\) y la pérdida de positividad en H9(ii), con \(\mu_k\neq 0\) condición suficiente correcta para el argumento de primer momento. No cierra el momento segundo en todo el producto de hipótesis: el caso H9(i) con portadores inseparables queda sin prueba, y en el caso de un solo desfase faltan en el texto el rayo complejo que hace funcionar H10\(_k\) y el paso de la media de \(|h|^2\) a densidad positiva. No hay contraejemplo que vuelva falsa la afirmación; tampoco está probada.

## Objeciones

**O1. H9(i) con grupo inseparable: la media cruzada no tiende a 0.** Reparación necesaria. Enmienda (H6\(_k\)(ii) y H9\(_k\)) y etapa A, §§8–9.

H6\(_k\)(ii) pide que \(1\), \(u\cdot w_A\) y \((\psi_i-\psi_j)/(2\pi)\) sean racionalmente independientes, por pares. H9(i) pide lo mismo para \(1\), \(u\cdot w_A\), \(u\cdot w_B\). Las dos cláusulas se pueden afirmar a la vez. La §8 sólo trata un desfase \(\theta_N\) y la equidistribución de \((Nu\cdot w_A,\, N(\psi_i-\psi_j)/(2\pi))\) en \(\mathbb{T}^2\).

Eso no mata el cruce si \(\Gamma_j\) depende de \((\theta^A_N,\theta^B_N)\). Contraejemplo a la implicación escrita, no a un paseo concreto: sean \(1,\alpha,\beta\) independientes, \(\alpha=u\cdot w_A\), \(\beta=u\cdot w_B\) y \((\psi_1-\psi_2)/(2\pi)=\beta\). Entonces H9(i) y H6\(_k\)(ii) valen, pero
\[
e^{iN(\psi_1-\psi_2)}=e^{2\pi i\{N\beta\}}=e^{-2\pi i\theta^B_N}
\]
es función de \(\theta^B_N\). La integral
\[
\int_{\mathbb{T}^2} e^{-2\pi i\theta^B}\Gamma_i\overline{\Gamma_j}\,d\theta^A\,d\theta^B
\]
no tiene por qué anularse, y la §8 no estima la forma de Gram resultante. No comprobé que esa forma sea definida positiva para todo cociente de coeficientes compatible con los \(\Gamma_j\); queda NO_VERIFICADO. Mientras no se pruebe, o se excluya esta celda, el veredicto de la §9 cubre un caso no demostrado.

**O2. H10\(_k\) no da, tal como está escrito, un giro común del grupo.** Reparación necesaria. Etapa A §8; enmienda, H10\(_k\).

La §8 toma razones fijas \(a_j\) y aplica el giro de la §6 (\(c\) e \(ic\)). Eso es inmediato si los \(e_j\) son paralelos, que es lo que el diagnóstico interpreta, pero H6\(_k\)(ii) no lo impone. H10\(_k\) sólo dice que un \(e_k\) no es múltiplo complejo de \(\widetilde R\).

El hueco se llena sin hipótesis nueva. Para \(M=M^\dagger\), \(u=M\widetilde R\) recorre \(\{\,u:\langle\widetilde R,u\rangle\in\mathbb{R}\,\}\) y
\[
\widetilde R^\dagger M e_j=u^\dagger e_j.
\]
Si \(e_k\notin\mathbb{C}\widetilde R\), existe \(u_0\) con \(\langle\widetilde R,u_0\rangle=0\) y \(u_0^\dagger e_k\neq 0\). Entonces \(u_0\) y \(-iu_0\) son admisibles y
\[
(-iu_0)^\dagger e_j=i\,u_0^\dagger e_j
\]
para todo \(j\) a la vez. Los múltiplos complejos de \((u_0^\dagger e_j\,f_j^\dagger v)_j\) están en la familia, con componente \(k\) no nula si \(f_k^\dagger v\neq 0\). Sobre ese rayo el momento segundo de la §8 sí es el de la §6. Esa reducción no está en el texto.

**O3. Media positiva de \(|h|^2\) no implica densidad positiva.** Reparación necesaria. Etapa A §8.

La §8 prueba, en el régimen de un desfase, que los cruces cesàro tienden a 0 y que
\[
\lim\frac1N\sum_{n\le N}|h(n)|^2=\sum_j|a_j|^2\int|\Gamma_j|^2\ge\sum_j|a_j|^2|\mu_j|^2>0
\]
si \(\mu_j\neq 0\) y algún \(a_j\neq 0\). De ahí no sale un conjunto de densidad positiva donde \(|h|\ge c\). Una sucesión puede valer \(0\) salvo bloques de densidad nula y altura grande y tener media cesàro positiva.

Hace falta el argumento que la §8 no escribe. El cierre de \(N\omega\) en el toro, con \(\omega\) formado por \(u\cdot w_A\) y las diferencias \((\psi_i-\psi_j)/(2\pi)\), lleva la medida de Haar del cierre; la independencia por pares hace que cada proyección bidimensional sea Haar, así que los cruces integran a 0 también en el cierre. Si \(\int|h|^2>0\), el conjunto \(\{|h|^2\ge c\}\) tiene medida positiva y, por equidistribución, densidad positiva. Eso vale para H9(ii). No repara O1.

**O4. El informe afirma más de lo que prueban el diagnóstico y la clase.** Reparación necesaria (en el informe, no en el teorema). Etapa A §§8–9, contra la salida del diagnóstico.

La §9 dice que no hay ejemplo en la clase \(\mathbb{Z}^d\) porque los tres paseos R1 viven en redes BCC. En la salida sólo W3 está etiquetado BCC («Pavia Weyl A+ (BCC)»). W2 es «CJWW (5.12) Bialynicki-Birula» y W6 «cyclic s=4 (tetrahedron)», sin red. El manuscrito discute (5.12) dentro de una teoría en \(\mathbb{Z}^3\); no dice que esa caminata sea BCC. La red de W2 y de W6 es NO_VERIFICADO.

Lo que sí sostiene la salida: H6\(_k\) y H6\(_k\) derecho salen falsos; los \(|\mu|\) son punto flotante; la §8 dice con razón que la independencia racional de los \(\psi\) no se decide en flotante. La enmienda acierta al no tomar esos \(|\mu|\) como verificación. El veredicto `PROVED_UNDER_FROZEN_CONTRACT` de la §9, en cambio, cubre el bloque entero de la enmienda, O1 incluida, y por eso afirma más de lo demostrado. La cautela sobre el resultado (b) del contrato (sólo parcial, §§6 y 9) es correcta y no hay que tocarla.

**O5. El paso de \(\operatorname{Re}\mu\) a \(|\mu|\) está omitido.** Exposición. Etapa A §6, frente a la derivación general §6.

La §6 dice que la §7 general «sigue igual» y escribe \(|\Gamma_k|\ge|\mu_k|/2\). La §6 general prueba \(\operatorname{Re}\Gamma\ge\operatorname{Re}\mu/2\). El traslado es cierto: si \(\alpha=\arg\mu\), la media de \(\operatorname{Re}(e^{-i\alpha}\Gamma)\) es \(|\mu|\), y en ese conjunto \(|\Gamma|\) hereda la cota. Conviene escribirlo. No cambia la constante de densidad más que en sustituir \(\operatorname{Re}\mu\) por \(|\mu|\).

**O6. \(\mu_k\neq 0\) es la condición suficiente correcta, no la necesaria.** Exposición. Etapa A §5; enmienda, H9\(_k\).

Bajo H9(ii) la media es exactamente
\[
\mu_k=\sum_n\int e^{-\zeta^T S_{C_k}\zeta/2}\,g^A(2\pi n;\sigma)\,g^B(-2\pi n;\sigma)\,d^m\zeta.
\]
Para \(\varphi\neq 0\), \(g(-2\pi n;\sigma)\) no es el conjugado de \(g(2\pi n;\sigma)\): el conjugado lleva \(\overline\sigma=\kappa-i\varphi\), no \(\sigma\). La positividad término a término de la derivación general §6 no pasa. Nada de lo que está en vigor implica \(\mu_k\neq 0\). Para el argumento de primer momento (nivel \(|\Gamma|\ge|\mu|/2\)) esa es la condición correcta.

No es necesaria. \(\Gamma(\theta)=e^{2\pi i\theta}\) tiene media \(0\) y módulo \(1\). En el momento segundo basta \(\int|\Gamma_j|^2>0\), y \(|\mu_j|^2\) es sólo una cota inferior cómoda. Pedir \(\mu_j\neq 0\) para todo \(j\in G\) es suficiente y algo más fuerte de lo necesario; no sobra como hipótesis de suficiencia. Bajo H9(i) la media sí sale no nula sin hipótesis extra (apartado siguiente).

## Lo que cierra

**Fases (etapa A §2).** Para \(x\) de red, \(e^{i\eta_k\cdot x}=e^{i\varphi\, u\cdot x}\). Con \(u\cdot x=\lfloor u\cdot x_*\rfloor-j\) y \(u\cdot x_*=\lfloor u\cdot x_*\rfloor+\theta^A\),
\[
e^{i\eta_k\cdot(x-x_*)}=\alpha_A e^{-i\varphi(\theta^A+j)},\qquad\alpha_A=e^{i\varphi\, u\cdot x_*}e^{-i\eta_k\cdot x_*}.
\]
Bob, con \(u\cdot y=\lceil u\cdot y_*\rceil+j'\), da el signo análogo. El producto con el factor de Fourier \(e^{-iN\eta_k\cdot v_*}\) es
\[
\alpha_A\alpha_B e^{-iN\eta_k\cdot v_*}=e^{-iN\varphi\, u\cdot v_*}.
\]
Los factores \(e^{\pm i\eta_k\cdot(y_*-x_*)}\) se cancelan aunque \(x_*,y_*\) no sean de red: esa cancelación usa el vector real \(Nv_*\), no el carácter. Junto con \(e^{iN\varphi_k}\) y \(e^{iN\omega_0}\),
\[
\psi_k=\varphi_k+\omega_0-\varphi\, u\cdot v_*.
\]
La fase global no depende de los desfases; éstos quedan dentro de las sumas de profundidad.

Comprobación en \(\pi u\). Datos del manuscrito (asamblea de la prueba del teorema principal): \(\varphi=\pi\), \(\varphi_k=\pi\), \(\omega_0=0\), \(u\cdot v_*=3-\sqrt3/2\), \(\theta_N=\{\sqrt3\, N/4\}\). Entonces \(\psi_k=\pi(-2+\sqrt3/2)\) y \(e^{iN\psi_k}=e^{i\pi\sqrt3\, N/2}\). El autovalor de \(S(\pi u-i\xi_*)\) es \(-e^{\Phi_*}\), así que \(e^{iN\varphi_k}=(-1)^N\) ya incluye el \((-1)^N\) de \(S(p+\pi u)=-S(p)^T\). Además \((-1)^N e^{-iN\pi u\cdot v_*}=e^{i\pi\sqrt3\, N/2}\), y
\[
e^{i\pi\sqrt3\, N/2}=e^{2\pi i(\sqrt3\, N/4)}=e^{2\pi i\theta_N},
\]
luego \(e^{-2\pi i\theta_N}e^{i\pi\sqrt3\, N/2}=1\), que es la identidad citada del manuscrito. Cada suma de profundidad absorbe un \(e^{-i\pi\theta_N}\); el producto de los dos con \(e^{iN\psi_k}\) es 1. No hay desfase residual.

**Sumas con decaimiento complejo (etapa A §3).** \(f(x)=e^{-\sigma x}\Psi_{x/|u|}(\tau)\mathbf{1}_{x\ge 0}\) cumple \(|f(x)|=e^{-\kappa x}|\Psi|\) y \(\Psi_0=0\), así que \(f(0)=0\). Para \(\theta\in[0,1)\) la periodización coincide con la suma \(j\ge 0\). Con \(\operatorname{Re}p=|u|\kappa>0\),
\[
\int_0^\infty e^{-p\delta}(\delta-|\sigma|^2)_+^2\,d\delta=2e^{-p|\sigma|^2}/p^3,
\]
y la gaussiana \((\pi/p)^{m/2}e^{-|\tau|^2/(4p)}\) vale en la rama \(|\arg p|<\pi/2\). El cambio \(x=|u|\delta\) reproduce el prefactor escrito. La serie de Fourier está en \(\ell^1\) porque \(|\hat g(2\pi n;\sigma)|\lesssim|n|^{-3-m/2}\), así que \(S_\sigma\) es continua; \(S_\sigma(0)=S_\sigma(1)\) la hace 1-periódica. Las cotas de capa de la derivación general §3 son absolutas y sólo ven \(e^{-\kappa(\theta+j)}\).

**Término principal (etapa A §4).** Las tres sustituciones de la derivación general §5 (símbolo gaussiano, formas de capa, extensión a \(\mathbb{R}^d\)) usan \(|e^{-N\eta^T C\eta/2}|=e^{-N\eta^T Q\eta/2}\) y errores de capa \(O(N^{-1/2}+|\eta_n|)\), uniformes en los desfases. Sacar \(e^{iN\psi_k}\), que es exacto y unimodular, no los cambia. La potencia sigue siendo \(5+d/2\). El portador entra por \(c_k\), \(\psi_k\), \(C_k\) y \(\sigma\); la banda del recurso, sólo por \(\varphi_\partial\) y \(\widetilde R\).

**H9(i), media no nula (etapa A §5).** Por Weyl, \((\theta^A_N,\theta^B_N)\) equidistribuye en \(\mathbb{T}^2\) y sólo sobrevive el modo cero. El prefactor \((|u|\sigma)^{-3-m/2}\) no es cero: \(\operatorname{Re}\sigma=\kappa>0\). La forma
\[
S_C/2+\frac{\rho_A+\rho_B}{2|u|}\operatorname{Re}(1/\sigma)\,I,\qquad\operatorname{Re}(1/\sigma)=\kappa/|\sigma|^2>0,
\]
es estrictamente acretiva, luego la integral gaussiana es finita y no nula. No hace falta parte real positiva, ni \(d\in\{2,3\}\). La parte real puede ser negativa; el giro de O5 cubre el paso a densidad.

## Rederivado

- Producto \(\alpha_A\alpha_B e^{-iN\eta_k\cdot v_*}=e^{-iN\varphi\, u\cdot v_*}\) y \(\psi_k=\varphi_k+\omega_0-\varphi\, u\cdot v_*\).
- Identidad del punto \(\pi u\): \(e^{i\pi\sqrt3\, N/2}e^{-2\pi i\theta_N}=1\), con \((-1)^N\) dentro de \(\varphi_k=\pi\).
- Transformada de \(e^{-\sigma x}\Psi_{x/|u|}\) para \(\operatorname{Re}\sigma>0\), rama \(|\arg p|<\pi/2\), y periodicidad vía \(f(0)=0\).
- Media H9(i) igual al modo cero, no nula por acretividad.
- Media H9(ii) igual al emparejamiento \(n\) con \(-n\); se pierde el conjugado si \(\varphi\neq 0\).
- Paso \(|\int\Gamma|=|\mu|\) más continuidad del toro compacto a medida positiva de \(\{|\Gamma|\ge|\mu|/2\}\), girando la parte real.
- Imagen hermitiana \(\{u^\dagger e_j:\langle\widetilde R,u\rangle\in\mathbb{R}\}\) y rayo \(u\perp\widetilde R\) girado por \(-i\).
- Equidistribución por pares en un desfase implica cruces nulos en el cierre; la media cesàro sola no da densidad.
- Dependencia \(\Delta\psi/2\pi=u\cdot w_B\) compatible con H9(i) y H6\(_k\)(ii) en la que el cruce no es nulo.

## NO_VERIFICADO

- Enunciados literales de H1, H2, H4′, H5, H7, H8: no están en los documentos. Se usó sólo lo que la derivación general y la etapa A hacen con ellos. En particular, que en todo punto dominante el drift sea \(v_*\) y el proyector sea de rango uno se da por hipótesis, no se rederivó.
- Que la familia declarada genere, en su span real, las hermíticas necesarias para el rayo de O2. La derivación general §7 lo usa; aquí no está el contrato de la familia.
- Que la forma de Gram de O1 sea definida positiva para todo lazo racional que las hipótesis actuales permiten.
- Redes de W2 y de W6. Valores numéricos de \(\mu\), de los \(\psi\) y de \(\cos(e_0,\widetilde R)\): son salida de punto flotante, no una comprobación. \(|\widetilde R|=0.700\) del paseo hexagonal no aparece en la salida adjunta.
- Independencia racional de los \(\psi\) en los tres paseos: la propia §8 la declara fuera del alcance del flotante. No la doy por buena ni por mala.

## Obligaciones pendientes

1. Restringir el enunciado, en la enmienda y en la §9, o completar la prueba. Opción mínima: H6\(_k\)(ii) sólo junto con H9(ii). Opción completa: independencia racional conjunta de \(1\), \(u\cdot w_A\), \(u\cdot w_B\) y \((\psi_i-\psi_j)/(2\pi)\), equidistribución en \(\mathbb{T}^3\) y cota de la forma de Gram. Mientras O1 siga abierto, el veredicto no puede ser `PROVED_UNDER_FROZEN_CONTRACT` para el bloque tal como está escrito.
2. Insertar en la §8 el rayo \(u\perp\widetilde R\) (O2) y el paso por la medida de Haar del cierre (O3), incluido el error \(O(N^{-1/2})\) dentro del corchete.
3. Sustituir «cannot be separated» / «isolated as in (i)» por álgebra lineal: \(f_k\notin\operatorname{span}\{f_j:j\notin G\}\) y cada punto fuera de \(G\) separable por la izquierda. Es el contenido que la prueba usa.
4. Corregir la §9: no atribuir BCC a los tres paseos. Lo defendible con la salida es que ninguno es un ejemplo verificado (H6\(_k\) falso en el diagnóstico; independencia racional no decidible en flotante; \(\mu\) numérico y fuera del veredicto).
5. Una frase en la §6: girar \(\Gamma\) por \(e^{-i\arg\mu}\) antes de citar la parte real de la derivación general. No es una hipótesis nueva.
