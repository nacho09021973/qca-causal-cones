<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 7d111a158edda04a469b59f0d380cd69d35bbdea; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 566f2bcf27e2db341d118734b22449975a324eafd4c363f4839b3ec2480d8836
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-12T10:10:57Z  fin: 2026-11-12T10:41:20Z
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE.md ; último commit observado: aa6c5f6 ; sha256 de la copia enviada ce398b36d0d74bfd10c389adad471ed93abbd1e0930d50a6e671faff068d7548
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE_AMENDMENT_1.md ; último commit observado: 91be396 ; sha256 de la copia enviada c8f5f41097dfa1b103400e65c57b358c0202bc9e55266a7ca5b34d909754bb30
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE_AMENDMENT_2.md ; último commit observado: 34f0601 ; sha256 de la copia enviada 2ab7a1fd4599812629ec83a95660da1215fbf52e5f4d616ea874619cf1e6b38b
documento: /home/ignac/qca-causal-cones/theory/GENERAL_IR_RATE_GATE_AMENDMENT_3.md ; último commit observado: 65e1ec4 ; sha256 de la copia enviada 36718f3d83a4b2e0daa667609293f9ec2a95d9c01752b3fd34fd5a7cc2a7107f
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stages-0-1.md ; último commit observado: 19a2615 ; sha256 de la copia enviada 958324a03d58c742cdd9df70b3dff413495e3223605f58a3c7d0685a71dbb912
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stage2-progress.md ; último commit observado: bb28f0c ; sha256 de la copia enviada 694ab7c78ac4a6d28a0c2dad8eb2a3cb945bbe6d237f1750da3a8e0f25698224
documento: /home/ignac/qca-causal-cones/reports/2026-11-12--general-ir-rate-stage2-leading-term.md ; último commit observado: 65e1ec4 ; sha256 de la copia enviada caa990e844057652705638258544a48becd5b2b9029ca0b9c1d1de5a818ff5b0
documento: /home/ignac/qca-causal-cones/reports/reviews/2026-11-12-general-ir-rate-grok/ir-corona-anon.tex ; último commit observado: sin versionar ; sha256 de la copia enviada 70b74038aa81d0ca0982e43209af318c1ee64352a21db5f616968bd9946a28f9
entrada_grok.txt sha256 de17794bcf60aaf803bb1b690aa7bbeb8256afb50e0a112551594fdc444b192b
respuesta sha256 f112a1fb7ab64c2655844681ca351b5556156c295843d3ee071188e44a72c3f9
-->

El dictamen es **PASS** en la etapa 1 y **PASS** en la etapa 2. La cadena cierra el enunciado pedido (cota para toda operación; limsup \(=-K_*\) para algún par de la familia) bajo H1–H3, H4′, H5–H10 y la clase congelada. No hay error fatal. Hay tres agujeros de redacción que no cambian el resultado, y tres piezas citadas que no están en los documentos y quedan sin verificar; ninguna de esas tres entra en la dependencia de (T).

\(K_*\) e \(I\) son, en toda la ejecución, los del propio desarrollo: \(\Phi(\xi)=\max_\eta\log\rho(S(\eta-i\xi))\) e \(I=\Phi^*\). La identificación con la mitad de la tasa de CJWW se declara no comprobada y no se usa.

## Etapa 1 — PASS

La cota \(\delta\le C N^{d+s-1}e^{-K_*N}\) queda demostrada para todo unitario que actúa como la identidad fuera de \(A_N\), todo estado de una partícula y todo efecto soportado en \(B_N\). Usa H1 y \(K_*>0\) (esta última, de la clase). No usa H2–H10. Es más fuerte que el enunciado del contrato (sin pérdida \(\varepsilon\), y fuera de la familia), y el informe lo dice.

**Convexidad de \(\Phi\)** (informe de etapas 0–1, lema 1.1). El radio espectral del operador de multiplicación por \(S(\,\cdot\,-i\xi)\) es el máximo puntual. La fórmula del radio espectral escribe \(\Phi\) como límite de \(n^{-1}\log\|A(\xi)^n\|\). Para \(F(t)=A(\xi_0+te)^n\), el alcance finito hace \(F\) entera en \(t\in\mathbb C\). La traslación \(\eta\mapsto\eta+be\) es unitaria y conjuga \(A(\xi_0+(a+ib)e)\) con \(A(\xi_0+ae)\), y lo mismo sus potencias, así que \(\|F(a+ib)\|=\|F(a)\|\). El logaritmo de la norma de una familia holomorfa de operadores es subarmónico; si no depende de la parte imaginaria, su laplaciano se reduce a la segunda derivada real, luego esa restricción es convexa. Límite puntual de convexas es convexa, y una convexa finita en \(\mathbb R^d\) es continua. \(\Phi\) es finita: en el toro real \(S(p)\) es unitaria, así que \(\det S\) es un monomio de módulo 1 y \(|\det S(\eta-i\xi)|=e^{\xi\cdot d_0}>0\).

**Potencias** (lema 1.2). En una forma de Schur unitaria, \(U\) estrictamente triangular superior sube el nivel de la bandera al menos en uno y \(D\) lo conserva, así que todo producto con \(s\) o más factores \(U\) es cero, aunque \(D\) se intercale. Hay \(\binom{N}{k}\) palabras con \(k\) factores. \(\|U\|\le\|T\|+\|D\|\le 2\beta\) porque \(\|D\|\le e^{\Phi}\le\beta\). Sale \(\|S^N\|\le C N^{s-1}e^{N\Phi}\) en \(\xi_*\) fijo. Para \(s=2\) es el lema 5.3 del manuscrito con \(2\beta\) en lugar de \(\beta\).

**Fenchel–Young y primer orden.** H1 da \(\xi_*=\nabla I(v_*)\), luego igualdad \(I(v_*)=\xi_*\cdot v_*-\Phi(\xi_*)\). Como \(v_*\) minimiza la convexa \(I\) sobre el convexo \(B-A\), el cociente incremental en la dirección factible pasa al límite y da \(\xi_*\cdot(v-v_*)\ge 0\). No hace falta que el mínimo sea interior. La unicidad de H1 no se usa aquí; sí en la etapa 2.

Para \(x\in A_N\), \(y\in B_N\) se tiene \((y-x)/N\in B-A\) exactamente, no en aproximación, luego \(\xi_*\cdot(y-x)\ge N\xi_*\cdot v_*\). El desplazamiento de contorno vale para cualquier símbolo de Laurent (entero y periódico). El lema 1.2 da \(\|G_N(y-x)\|\le C N^{s-1}e^{-K_*N}\).

**Test de Schur.** Con \(\|K(y,x)\|\le M\), \(\sum_y\|K\|\le |B_N|M\) y \(\sum_x\|K\|\le |A_N|M\), así que \(\|P_BS^NP_A\|\le\sqrt{|A_N||B_N|}\,M\). Las bolas aportan \(|A_N|,|B_N|\le C N^d\) y el lema 1.2 aporta \(N^{s-1}\): potencia \(d+s-1\). El factor 4 de \(\delta\le D_B\le 4T_N\) es el del manuscrito (prueba del teorema de cota explícita): \(\|v_1-v_0\|\le 2T_N\), \(\|v_b\|\le 1\) y \(\|\,|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|\,\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\). Para \(d=3\), \(s=2\) sale \(N^4\), que es la potencia del teorema de tasa (d) del manuscrito.

## Etapa 2 — PASS

**(T)** queda demostrado para algún par de la base declarada. El informe no promociona el prefactor, la potencia ni el liminf a enunciado; la potencia \(5+d/2\) es un subproducto y el contrato sólo pedía limsup.

**3. Cola libre** (informe del término principal, §2). El recurso está soportado en \(|p|\le 1/N\) y \(\chi\) está en el plano nodal, como fija la clase. El proyector conjunto del par nodal es analítico porque el punto es aislado del resto del espectro; dentro del par, \(S(0)\) es unitaria, luego no hay bloque de Jordan. En un símbolo analítico, un cono lineal isótropo y sin deriva deja resto \(O(|p|^2)\) después de la parte lineal. Duhamel da \(e^{-iNH(q/N)}=e^{-iH_W(q)}+O(1/N)\) uniforme en la fase, y la norma \(L^1\) del error produce \(O(N^{-d/2-1})\) puntual, uniforme en \(y\). Para el limsup bastaría \(o(1)\); el \(O(N^{-1})\) es lo que da la analiticidad. H5 es \(R_0(w_B)\ne 0\).

**4. Capas** (§3). El perfil esférico es exacto: \(F_N=(4/R_A^2)\varepsilon^2\) con \(\varepsilon=\delta-\delta^2/(2R_A)-|u_\perp|^2/(2R_A)\), y \(\theta=(\pi/2)F_N=(2\pi/R_A^2)\varepsilon^2\). La cota absoluta \(N^{-5/2}\), independiente de \(d\), sale de recurso \(N^{-d/2}\), perfil \(N^{-2}\) y área \((N\delta)^{(d-1)/2}\), con la inclinación sumable en la profundidad. El término \(m=0\) de Poisson aporta el factor de covolumen \(1/|u|\). Reuniendo jacobiano \(y=\sqrt{2R}\,\sigma\),

\[
k_A=\frac{2\pi\,(2\rho_A)^{m/2}}{\rho_A^2|u|},\qquad k_B=\frac{4\,(2\rho_B)^{m/2}}{\rho_B^2|u|}.
\]

Para \(d=3\), \(u=(1,1,1)\), \(\rho=1/4\): \(k_A=16\pi/\sqrt 3\) y \(k_B=32/\sqrt 3\), como en el lema de capas del manuscrito. La variación total de la tercera derivada es del orden escrito \(O(N^{-4}\delta^{d/2})\): el salto de la segunda derivada en el borde es \(O(\delta/R)\) sobre una superficie \((R\delta)^{(m-1)/2}\), y el interior es del mismo orden. El exponente \(-4\) no depende de \(d\), y el relativo frente al término \(m=0\) es \(O(N^{-3/2})\). La suma \(|m'|^{-3}\) converge precisamente porque \(m=d-1\le 2\). El error es uniforme en el desfase: no se divide por la profundidad y \(\sum_j e^{-\kappa j}\mathrm{poly}(j)<\infty\). En un carácter no trivial sobre el plano, todas las frecuencias quedan a distancia \(\ge d_0/2\) y la capa cae a \(O(N^{-4})\), relativo \(O(N^{-3/2})\).

**5. Sumas de profundidad** (§4). \(\int_0^\infty e^{-p\delta}(\delta-|\sigma|^2)_+^2\,d\delta=2e^{-p|\sigma|^2}/p^3\) y la gaussiana en \(\mathbb R^m\) dan, con \(x=|u|\delta\) y \(\mathrm{Re}\,p=\kappa>0\),

\[
\hat g_\tau(\omega)=2\pi^{m/2}|u|\,(|u|s)^{-3-m/2}e^{-|\tau|^2/(4|u|s)},\quad s=\kappa+i\omega.
\]

Para \(d=3\), \(|u|=\sqrt 3\), esto es \(c_g/s^4\) con \(c_g=2\pi/(3\sqrt 3)\), como en el lema 7.3 del manuscrito. La función se anula en \(0\), es continua, y \(|\hat g|\) es sumable porque \(3+m/2\ge 7/2>1\). Poisson es exacto. \(\Psi_\delta\) es real por ser transformada de una función radial real, así que \(S^A\) y \(S^B\) son reales.

**6. Ensamblaje** (§5 y registro de progreso, §3.1). H2 da una rama simple y analítica; el máximo no degenerado hace la hessiana real en \(\eta\) definida negativa, y Cauchy–Riemann la identifica con \(-Q\), \(Q=\mathrm{Hess}_\xi\log|\lambda|>0\). H8 fija el término lineal en \(v_*\). Entonces \(C=Q+iQ'\) cumple \(\mathrm{Re}(z^*Cz)=z^*Qz\ge c\|z\|^2\): es estrictamente acretiva, no sólo en vectores reales. La inversa de una acretiva es acretiva, y la inversa del complemento de Schur es un bloque de \(C^{-1}\), luego una compresión; el complemento es acretivo. Integrar \(\eta_n\) primero es lícito (\(\mathrm{Re}\,C_{nn}=\hat u^T Q\hat u>0\)) y deja \(\sqrt{2\pi/(N C_{nn})}\) y la forma de Schur en el plano. Las formas principales de las capas no dependen de \(\eta_n\). El recuento es \(N^{-5/2}\cdot N^{-5/2}\) de las dos capas por \(N^{-d/2}\) de la gaussiana: \(N^{-5-d/2}\), que es \(N^{-13/2}\) si \(d=3\). El error relativo \(O(N^{-1/2})\) sale de \(N|\eta|^3\) y de \(|\eta|\) contra la gaussiana, de \(|E|\le C(N^{-1/2}+|\eta_n|)\) y de la cola \(|\eta|>r_0\); el módulo del integrando es \(e^{-N\eta^T Q\eta/2}\), así que \(Q'\) no cambia estas cotas. Si el gradiente no fuera \(v_*\), completar el cuadrado en \(\int e^{iNa\cdot\eta-N\eta Q\eta/2}\,d\eta\) produce \(e^{-(N/2)a\cdot Q^{-1}a}\): la motivación de H8 en la enmienda 2 es correcta.

**7. Promedio bajo H9** (§6). \(\Gamma_0\) es continua en el toro porque el sumando se anula en profundidad 0. Bajo (i), \(1,u\cdot w_A,u\cdot w_B\) independientes sobre \(\mathbb Q\) equivalen a la equidistribución de \((\{N\alpha\},\{-N\beta\})\) y el promedio retiene sólo \(\hat g^A(0)\hat g^B(0)\), gaussianas positivas. La forma total es acretiva. Bajo (ii), \(\theta^A_N=\theta^B_N\) y la media retiene \(\sum_n\hat g^A(2\pi n)\overline{\hat g^B(2\pi n)}\): el signo de Fourier fuerza el modo \(-n\), y \(\hat g(-\omega)=\overline{\hat g(\omega)}\) en el semiplano derecho. La parte real del coeficiente de \(|\zeta|^2\) es \((\rho_A+\rho_B)\kappa/(2|u||s|^2)>0\).

La frase «los autovalores están en el semiplano derecho, luego la parte real del integral es positiva» no está escrita con el detalle que hace falta, pero es verdadera en la clase. Para \(m\le 2\) y acretividad estricta, \(|\arg\lambda_j|\le\alpha<\pi/2\), así que \(|\arg\det|<\pi\) y no se cruza el corte; la mitad del argumento queda en \((-\pi/2,\pi/2)\). El segmento hasta la parte hermitiana permanece en ese sector, y en el extremo definido positivo la raíz es positiva. Por tanto \(\mathrm{Re}(\det^{-1/2})>0\) y \(\mathrm{Re}\,\mu>0\). Para \(m\ge 3\) el mismo principio es falso (tres argumentos pueden sumar más de \(\pi\)); la restricción \(d\in\{2,3\}\) es esencial y no está dicha en ese párrafo.

De \(\mathrm{Re}\,\mu=L>0\) y \(|\Gamma_0|\le M_\Gamma\) sale densidad inferior positiva del conjunto donde \(\mathrm{Re}\,\Gamma_0\ge L/2\): la cota escrita \(L/(2M_\Gamma)\) es más débil que \((L/2)/(M_\Gamma-L/2)\) y es válida. Ahí \(|\Gamma_0|\ge L/2\).

**8. No anulación** (§7). Los otros puntos de carácter trivial se anulan eligiendo \(M\) con H6 por la izquierda: el núcleo de las formas \(f_k^\dagger\) es un subespacio complejo no contenido en el núcleo de \(f_0^\dagger\), y multiplicar por una fase hace \(\langle\chi,v\rangle\) real (si ya es cero, ya es real). El mapa \(M\mapsto M\chi\) de hermíticas sobre ese hiperplano real es suprayectivo. El término que queda es \(-2e^{-K_*N}N^{-5-d/2}\mathrm{Im}(e^{iN\psi}\Gamma_0 c)+O(N^{-1/2})\) relativo. La fase no depende del protocolo. Si hay dos valores de \(c\) que forman base real de \(\mathbb C\), las formas \(z\mapsto\mathrm{Im}(zc_j)\) son independientes, así que para cada \(N\) bueno al menos un protocolo ve \(\ge c'|z_N|\). Por el principio del palomar uno de los dos lo hace en un subconjunto de densidad positiva. H10 es exactamente esa hipótesis; la condición suficiente (H6 por la izquierda y \(e_0\) no paralelo a \(\widetilde R\)) es correcta: \(\widetilde R^\dagger M_B e_0=\mathrm{tr}(M_B|e_0\rangle\langle\widetilde R|)\) recorre \(\mathbb C\) salvo si ese rango uno es múltiplo complejo de una hermítica, es decir salvo si \(e_0\parallel\widetilde R\).

El paso a un par de la base es válido. \(Z_1\) es bilineal en \((M,M_B)\) exactamente; \(L_N=-2\mathrm{Im}\,Z_1\) más términos de orden menor para todo protocolo (el registro de progreso, §2: \(Z_2\) es \(O(N^{-7-d/2}e^{-K_*N})\), el cuadrático es \(O(e^{-2K_*N})\), y el complemento de los puntos dominantes es exponencialmente menor usando el hueco de H2, no la cota cruda \(N^{s-1}\)). Si todo par de la base tuviera \(e^{K_*N}N^{5+d/2}\mathrm{Im}\,Z_1\to 0\), también toda combinación fija del span, en contradicción con H10. Luego algún par de la base tiene limsup del normalizado estrictamente positivo. La etapa 1 da el limsup \(\le -K_*\) (cualquier polinomio es \(o(N)\) en el logaritmo), y esa subsucesión da el limsup \(\ge -K_*\).

## Hipótesis

Son coherentes y no se pisan. H1 (diferenciabilidad de \(I\) en \(v_*\)) y H8 (diferenciabilidad de \(\Phi\) en \(\xi_*\)) son duales y ninguna implica la otra. H4′ no es el H4 original: hace falta el punto \(\eta=0\), no un carácter trivial cualquiera, porque sólo ahí el modo cero de la profundidad es la gaussiana positiva. Cada hipótesis se usa donde el informe dice:

| Hipótesis | Uso |
|---|---|
| H1 | Etapa 1: Fenchel y desigualdad variacional. Etapa 2: un solo par de puntos de contacto. La unicidad sobra en la etapa 1 y hace falta en la 2. |
| H2 | Hueco, rama simple, hessiana no degenerada, integral \(O(N^{-d/2})\). |
| H3 | Planos de red. |
| H4′ | El silla en momentum cero, acoplada a la cola del recurso. |
| H5 | \(\widetilde R\ne 0\). |
| H6 | Anular los otros puntos triviales. |
| H7 | \(\varphi_\partial\ne 0\). |
| H8 | Sin este gradiente el punto cero queda exponencialmente por debajo. |
| H9 | Densidad positiva donde \(\|\Gamma_0\|\) está acotado por debajo. |
| H10 | La fase \(e^{iN\psi}\) no puede anular la parte imaginaria en todo \(N\). |

No falta ninguna condición para este enunciado. El resto \(O(|p|^2)\) del cono y la analiticidad del proyector van con la clase (símbolo de Laurent, nodo aislado, cono lineal sin deriva), no con una H nueva. Las relaciones racionales de desfases distintas de H9(ii) quedan, como dicen las enmiendas, fuera del contrato. Ningún paso usa una hipótesis no declarada: la holomorfía de la rama dominante es H2 más el símbolo analítico; \(\kappa>0\) es \(K_*>0\); \(m\le 2\) es \(d\in\{2,3\}\).

## El caso del manuscrito (punto 9)

La sección 8 del informe del término principal, más el manuscrito, confirman H1–H10 para el paseo de Weyl. Lo rederivado, no sólo citado:

- \(q_t=c_*/D_*>0\) y \(q_n=h'(t)>0\), con la hessiana escrita en el lema del símbolo y \(h'(t)>0\) para \(t>0\) porque \(c^6-3c^2+2>0\) si \(c>1\). De ahí H1 (diferenciabilidad de \(I\)) y la parte de hessiana de H2.
- Únicos puntos dominantes: el lema espectral, con todas las componentes de \(\xi_*\) distintas de cero. Carácter trivial en los planos sólo en \(0\) y \(\pi u\).
- H5 y H7: los integrandos de \(\mathcal I_0\), \(\mathcal I_1\) e \(I_b\) son positivos (\(\rho_*=\sqrt 3-1/4<\pi/2\), \(j_0>0\), \(j_1>0\), \(\sin(k/4)>0\)).
- H8: las simetrías del símbolo preservan el módulo de los autovalores.
- H9(ii): \(u\cdot w_A=\sqrt 3/4\) irracional y \(u\cdot w_B=3-\sqrt 3/4\), luego los dos desfases coinciden.
- H6 y H10: \(c_*=\cosh t_*>1\) porque \(\alpha=1-1/(2\sqrt 3)>1/\sqrt 3\). Los argumentos de \(-(1+ic_*)\) y de \(-(1+i)\) coinciden sólo si \(c_*=1\), así que \(e_0\) no es paralelo a \(\widetilde R\). La segunda componente de \(e_0\) es real positiva y la primera no es real, así que \(e_0\) no es múltiplo complejo de un vector real, luego tampoco de \(\overline{e_0}\). Como \(S(-i\xi_*)\) es hermítica, los autovectores izquierdos son los derechos, y en \(\pi u\) el proyector es el conjugado.

## Lo que los informes afirman

No afirman más de lo que la cadena demuestra. La etapa 1 se presenta como adaptación autocontenida, no como corolario citado de CJWW. La etapa 2 limita el veredicto al limsup, dice que las constantes no son explícitas y no toca liminf, prefactor ni novedad. El resultado de línea «ninguno de (a), (b), (c)» coincide con haber probado (T) dentro de las enmiendas. El esbozo de la enmienda 2 dice «integral positiva» donde, si \(Q'\ne 0\), sólo hay parte real positiva; el informe del término principal lo corrige y es el que vale como prueba.

## Objeciones

Ninguna es fatal ni una hipótesis que falte.

1. **Exposición, no falsa en la clase.** Informe del término principal, §6: el salto de «acretiva» a «parte real positiva de \(\pi^{m/2}(\det)^{-1/2}\)» no explica el corte de la raíz. La derivación de arriba lo cierra para \(m\le 2\). Conviene escribirla en el texto, y decir que \(m\ge 3\) se sale de la clase.
2. **Exposición.** Mismo informe, §2: «\(H=H_W+O(|p|^2)\)» se usa sin recordar que sale de la analiticidad. Para el limsup sobra la tasa; para el \(O(N^{-1/2})\) escrito hace falta.
3. **Exposición.** Enmienda 2, párrafo «por qué H9 basta»: «integral positiva» debe leerse como en el informe final (parte real positiva) cuando la gaussiana es compleja. El registro de progreso, §3.1, ya lo anuncia.
4. **Exposición.** Etapas 0–1, lema 1.2: afirmar que las palabras con \(s\) o más factores \(U\) se anulan, sin la frase de la bandera. La afirmación es verdadera.
5. **Exposición.** Etapas 0–1, teorema 1.3: el test de Schur se nombra y no se escribe. La potencia que sale es la correcta.

## NO_VERIFICADO

- La identificación de este \(I\) con \(I_{\mathrm{CJWW}}/2\). El informe de etapas 0–1 la declara no comprobada. El PDF de CJWW no está entre los documentos. No está en la cadena de (T).
- Etapa 0(ii): el contraste línea a línea con los teoremas 9.5 y 9.12 de ACSV. El PDF no está adjunto. La conclusión «no disparan (b)» es conservadora y no sostiene la prueba positiva.
- Etapa 0(i), caso K4: que \(K_*=0\) se infiere de una auditoría que no está en los documentos. No se usa en las etapas 1 ni 2.
- El valor numérico del prefactor general contra \(\mathcal K\) del teorema 7.5 del manuscrito, más allá de la estructura. Coinciden \(k_A\), \(k_B\), la potencia \(13/2\), \(\psi=0\) y \(C=Q\). No hace falta para (T).

## Rederivado

Convexidad de \(\Phi\) por subarmonicidad; anulación de palabras con \(s\) factores \(U\); Fenchel–Young, desigualdad variacional y dirección del exponente; potencia \(d+s-1\) del test de Schur y el factor 4; \(k_A\), \(k_B\) y su especialización a \(16\pi/\sqrt 3\), \(32/\sqrt 3\); variación total \(O(N^{-4}\delta^{d/2})\) y relativo \(O(N^{-3/2})\); transformada \(\hat g\) y el caso \(d=3\); potencia \(5+d/2\); acretividad de \(C\) y del complemento de Schur; completación del cuadrado que hace exponencialmente pequeño un gradiente distinto de \(v_*\); parte real del integral gaussiano para \(m\le 2\); modos de H9(i) y H9(ii), incluida la conjugación \(\hat g(-\omega)=\overline{\hat g(\omega)}\); densidad del conjunto donde \(\mathrm{Re}\,\Gamma_0\ge L/2\); que \(e^{iN\psi}\) no rompe el argumento de rotación; bilinealidad hasta un par de la base; positividad de \(q_t\), \(q_n\), \(\mathcal I_0\), \(\mathcal I_1\), \(I_b\); \(c_*>1\) y la no colinealidad \(e_0\nparallel\widetilde R\), \(e_0\nparallel\overline{e_0}\).

## Obligaciones pendientes

Ninguna bloquea el dictamen. Si el texto va a fijarse: escribir en §6 el argumento del corte para \(m\le 2\); una frase en §2 sobre el resto \(O(|p|^2)\); alinear la frase «integral positiva» de la enmienda 2 con la parte real. La comparación con CJWW, ACSV y la auditoría tetraédrica siguen sin verificar porque esos documentos no estaban en el encargo; no forman parte de la prueba de (T).
