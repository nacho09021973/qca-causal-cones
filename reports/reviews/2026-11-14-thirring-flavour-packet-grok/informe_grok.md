<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.70 (f50904eaee6c) [stable])
grok.json sha256 fc37f2da6fbb799e24defa9ebfd25929afb3624dbc6c893c0fcc73f4f8349d0f
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-14T14:01:28Z  fin: 2026-11-14T14:19:17Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-flavour-packet.md ; último commit observado: 24b78e9 ; sha256 de la copia enviada dd5c45475aeaed96a4d72791838c67273fe7baf90d14fbc35dd05937ae7019eb
documento: /home/adnac/qca-causal-cones/theory/THIRRING_FLAVOUR_PACKET_GATE.md ; último commit observado: d0c59cb ; sha256 de la copia enviada df61430f415eddc5e3186e19bfcd61f5fa15a33299c61a4d9880409f58a22231
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_flavour_packet.py ; último commit observado: 8d7e444 ; sha256 de la copia enviada 7e66c30ac95cb3b7f76f195831ec1d742e595dad52994361d44dcdcf8c0af6cd
documento: /home/adnac/qca-causal-cones/reports/2026-11-14--thirring-flavour-packet.txt ; último commit observado: 24b78e9 ; sha256 de la copia enviada e597668f5b3dc94d8e0270ec5071448d4b7bb51afd45dacab9fcc02c3e78537e
documento: /home/adnac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.md ; último commit observado: 77c9776 ; sha256 de la copia enviada 115240689eb2e1d47a94a5ac78aa5df8099158ae16c72420b7eaab323bd864ab
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_low_energy_packet.py ; último commit observado: 8b41761 ; sha256 de la copia enviada a1900674990354db197e7daddfdefb46d0a23536ba3b5e0688c2b45250f4d517
documento: /home/adnac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_grok.txt sha256 bb9e59f3dd099f2fd1c6a9873cdc39c0c40d73df4fbfaed2499d0289b168ea79
respuesta sha256 f7b48621ed1b6ba30a7b1083afba58ec6956aac23b499e95278b57820f21795d
-->

**Dictamen global: PASS.** No hay reparaciones obligatorias. La álgebra del código, la admisión bajo \(U^2\), la reutilización del sector \((+,+)\) y el mapa lógico cuadran con las convenciones de \(W\), con \(P=(1-G)/2\) y con la Ec. (12) de 1711.03920. El bloque \((+,-)\) también cierra: el signo de \(T_-\) sale de la condición de contacto, y la separación \(3\mu\) frente a la anchura \(\mu^{3/2}\) mantiene el paquete lejos del punto degenerado. El 32/32 certifica F1–F7; el puente de paquetes sigue siendo prueba escrita.

## 1. Código — PASS

\(\Gamma=\sigma_z(-1)^x\) es involución hermítica. En el soporte, \(\varphi\) y \(\Gamma\varphi\) no se solapan: F7 deja el paquete derecho en \((0,4\mu)\), el izquierdo en momenta negativos de orden \(\mu\), y \(8\mu<\pi\) separa las copias desplazadas en \(\pi\). Por tanto \(\langle\varphi,\Gamma\varphi\rangle=0\), \(\|\Pi_f\varphi\|^2=1/2\) y \(\sqrt2\,\Pi_f\varphi\) tiene norma 1. Los cuatro soportes (dos centros por dos bandas) son disjuntos, así que las cuatro columnas son ortonormales. F3 lo reproduce en el modelo de cuatro modos.

\(G=\Gamma_1\Gamma_2\): A es autovector \(+1\) y B es \(-1\), luego AA y BB tienen \(G=+1\). El contacto (mismo sitio, componentes opuestas) tiene \(G=-1\) (P4), \(J\) es la identidad en \(G=+1\) y \(G\) conmuta con \(F\). Así \(U(1-P)=F(1-P)\) y, con \(T\) cualquiera, \(U^T|\mathrm{AA}\rangle=F^T|\mathrm{AA}\rangle=B_\mathrm{out}|\mathrm{AA}\rangle\), igual para BB.

Con el producto antisimétrico normalizado y \(\varphi_r,\Gamma\varphi_r,\varphi_l,\Gamma\varphi_l\) ortonormales,
\[
\mathrm{AB}=P(\varphi_r\wedge\varphi_l)-P(\varphi_r\wedge\Gamma\varphi_l),\qquad
\mathrm{BA}=P(\varphi_r\wedge\varphi_l)+P(\varphi_r\wedge\Gamma\varphi_l).
\]
El primer vector \(P\) es \((+,+)\) con momento total cerca de \(q_r+q_l\); el segundo es \((+,-)\) (derecha \(+\), izquierda \(-\) en \(q_l+\pi\)) con momento total desplazado en \(\pi\). Son ortogonales y cada uno tiene norma al cuadrado \(1/2\). F3 lo certifica.

## 2. Admisión bajo \(U^2\) — PASS

De \(\Gamma W=-W\Gamma\): \(W\Pi_A= \Pi_B W\) y \(W\Pi_B=\Pi_A W\), luego \(W^2\Pi_f\varphi=\Pi_f W^2\varphi\). Como \(W^t\Gamma=(-1)^t\Gamma W^t\), la densidad de posición de \(\Gamma\varphi\) coincide con la de \(\varphi\) en todo tiempo entero. En momento, \(\omega(q+\pi)=\pi-\omega(q)\) y la banda \(-\) aporta \(e^{+i\omega(q+\pi)}=-e^{-i\omega(q)}\); al cuadrado, ambas componentes llevan \(e^{-2i\omega(q)}\) y la misma velocidad de grupo \(x=-\omega'(q)\,t\). En el soporte, \(\sin\omega(\mu K)/\mu\to\sqrt{1+K^2}\) (P5) y \(\omega\to0\), así que \(\omega(\mu K)/\mu\to\sqrt{1+K^2}\). No se juzga aquí la decisión Q2-A.

## 3. Sector \((+,+)\) — PASS

El contrato congelado fija los mismos paquetes que el canal 01 del contrato 2: partícula 1 = derecha, centro \(+\mu\) (\(k=1\)), en \(x=+L\); partícula 2 = izquierda, centro \(-2\mu\) (\(k=2\)), en \(x=-L\), con \(\omega'<0\). El puente escrito da
\[
U^T P(\varphi_r\wedge\varphi_l)=T_+ F^T P(\varphi_r\wedge\varphi_l)+o(1),
\]
\[
T_+\to\frac{a_r+za_l}{a_l+za_r},\quad a_r=\sqrt2+1,\quad a_l=\sqrt5-2,\quad z=e^{-i\chi}.
\]
Esa es la orientación de la Sec. 4(i) del contrato 2: \(T=(g_+(q_1)+zg_+(q_2))/(g_+(q_2)+zg_+(q_1))\) con \(q_1\) el paquete de \(+L\). F6 comprueba que \(|T_+-1|^2/4\) reproduce \(l_{01}\). Esa identidad es invariante al permutar rapideces (\(|T|=1\) implica \(|T-1|=|T^{-1}-1|\)); el orden lo fija la fórmula, no el número \(l_{01}\).

## 4. Sector \((+,-)\) — PASS

La condición de contacto se extiende a \(v^+_{q_1}\otimes v^-_{q_2'}\). Ambos espinores tienen componente superior \(-i\mu\). Con \((a,b,c,d)\) ese producto, \(\sigma_z\otimes\sigma_z\) sigue mandando \((a,b,c,d)\) a \((a,-b,-c,d)\), y el intercambio de partículas permuta \(b\propto g_-(q_2')\) con \(c\propto g_+(q_1)\). En \(y=0\), \((-1)^{x_1+x_2}=1\) y la antisimetría más la fase \(z=e^{-i\chi}\) solo en RL dan
\[
T_-=\frac{g_+(q_1)+zg_-(q_2')}{g_-(q_2')+zg_+(q_1)},
\]
que es el signo inferior de la Ec. (12) con partícula 1 en \(p+k\) (banda \(+\)) y partícula 2 en \(p-k\) (banda \(-\)). F2 confirma que esa función, con su pareja \(\Gamma_1\Gamma_2\), el canje y la fase de contacto, es autovector exacto en dos puntos no degenerados; son ejemplos, no la prueba. F1 da \(g_-(q+\pi)=-g_+(q)\). Con \(q_2'=q_l+\pi\) y \(g_+=-ia\) en el límite,
\[
T_-=\frac{a_r-za_l}{za_r-a_l}.
\]
Es \(T_+\) evaluado en \(a_l\to -a_l\). El autovalor libre \(e^{-i\omega(q_1)}e^{+i\omega(q_2')}\) se conserva al desplazar ambos momentos en \(\pi\) y voltear ambas bandas.

\(P\) del par plano es \(\tfrac12\bigl[v^{+-}-(-1)^{x_1+x_2}v^{-+}_{\mathrm{despl}}\bigr]\), la parte entrante del autovector, con el mismo reparto de factores que la Sec. 4(iii) del contrato 2. La fase temporal del autovector es \(-t\bigl(\omega(q_r)+\omega(q_l)\bigr)\) más \((-1)^t\): el desplazamiento \(\omega(q+\pi)=\pi-\omega(q)\) no cambia la fase estacionaria ni las derivadas que entran en las colas. \(\Gamma\) es unitaria de sitio y \(W^t\Gamma=(-1)^t\Gamma W^t\), así que centros, colas de posición y la cota \(|\omega'|\ge0.55\) se transfieren tal cual. En \(\chi=\pi/2\), \(g_s=-i\cdot(\mathrm{real})\) y \(|z|=1\) implican \(|T_-|=1\) en todo momento real; el denominador \(-a_l-ia_r\) solo se anula si ambos coeficientes se anulan, y \(g_+(q)\ne0\) para \(\mu>0\). En el límite, \(|za_r-a_l|^2=a_r^2+a_l^2>0\) sobre un entorno compacto de \((K_r,K_l)=(1,-2)\), así que \(|\nabla T_-|\le C/\mu\) y la variación en una anchura \(\mu^{3/2}\) es \(O(\mu^{1/2})\), como para \(T_+\).

La degeneración en que las cuatro ondas coinciden a pares es \(q_2'=q_1+\pi\), es decir \(q_l=q_r\) (el punto \(z_2=-z_1\) de la ejecución 2). Los centros están a \(3\mu\) y cada soporte mide \(2\mu^{3/2}\): en la variable \(K=q/\mu\) la distancia es \(3\) y la anchura es \(\sqrt\mu\to0\). No falta un término singular. Incluso en \(a_r=a_l\) y \(z=-i\), \(T_-=-1\) y el denominador vale \(2a^2>0\): \(\chi=\pi/2\) no es un polo. El semimomento total tiende a \(\pi/2\), punto especial de la fuente, pero en el soporte \(|q_r+q_l|\ge\mu(1-O(\sqrt\mu))>0\), así que \(p\neq\pi/2\) a \(\mu\) fijo, y \(T_-\) permanece acotada al tomar el límite.

## 5. Mapa lógico — PASS

\(F\) conmuta con \(P\) y los dos sectores tienen momentos totales separados por \(\pi\), luego no se mezclan. Con \(T\) par, \(W^T\Gamma=\Gamma W^T\). Entonces
\[
U^T|\mathrm{AB}\rangle\to\alpha\,B_\mathrm{out}|\mathrm{AB}\rangle+\beta\,B_\mathrm{out}|\mathrm{BA}\rangle,
\]
y lo análogo para BA, con \(\alpha=(T_++T_-)/2\), \(\beta=(T_+-T_-)/2\). F4 certifica esta combinación en el modelo finito, supuesto el puente. \(|T_\pm|=1\) y la ortogonalidad de sectores dan el bloque unitario; AA y BB salen con fase 1. Toda imagen cae en el rango de \(B_\mathrm{out}\) salvo \(o(1)\), y la dimensión lógica 4 pasa de columnas a norma de operador: \(\|E_\mu\|\to0\).

F5 certifica
\[
T_+-T_-=\frac{2a_1a_2(z^2-1)}{(a_2+za_1)(za_1-a_2)},
\]
así que \(\beta=0\) si y solo si \(z^2=1\) (\(\chi\in\{0,\pi\}\)), con \(a_i>0\). En \(\chi=\pi/2\),
\[
T_+=\frac{2a_ra_l+i(a_r^2-a_l^2)}{a_r^2+a_l^2}=x+iy,\qquad T_-=-x+iy,
\]
con \(x=2a_ra_l/(a_r^2+a_l^2)=(\sqrt{10}-2)/6\) y \(y=\sqrt{11/18+\sqrt{10}/9}\). Entonces \(\alpha=iy\), \(\beta=x\) y \(V=1\oplus[[iy,x],[x,iy]]\oplus1\). El estado \(V|\mathrm{AB}\rangle=iy|\mathrm{AB}\rangle+x|\mathrm{BA}\rangle\) tiene concurrencia \(2|xy|=2xy>0\). F6 certifica módulo, valor y positividad; el radical coincide con la evaluación numérica \(\approx0.193713\).

## 6. Alcance y verificador — PASS

La Sec. 6 dice qué no está certificado: el puente del contrato 2, su adaptación \((+,-)\), la admisión bajo \(U^2\) y el veredicto. El 32/32 no prueba esos pasos. F3 codifica bien el álgebra: \(\Gamma\) permuta los dos pares, \(G(X)=\Gamma X\Gamma^\top\) es \(\Gamma\otimes\Gamma\) sobre la matriz antisimétrica, y las identidades de AB, BA, normas y \(V\) son exactas en ese modelo. No modela colas ni dispersión.

El punto \(z_2=-z_1\) de la ejecución 2 es \(q_2=q_1+\pi\), donde las cuatro ondas coinciden a pares, y cae fuera de los soportes (\((0,4\mu)\) frente a \((\pi,\pi+4\mu)\)). Sustituirlo por \(z_2=\overline{z_1}\) mantiene dos puntos algebraicos no degenerados en la circunferencia unidad. Quedó escrito en el informe y en el comentario del script; la ejecución fallida se conserva. F2 sigue siendo un ejemplo de la derivación general.

La Sec. 7 acota el resultado a este código, esta regla, \(\chi=\pi/2\), estos dos paquetes y \(\mu\to0\). Niega universalidad, componibilidad y límite QFT interactivo. Conservar \(N_A\) es correcto: el bloque solo mezcla AB con BA.

## Aclaraciones (no son errores)

La etiqueta `left-inside-4mu(2-m>0)` de F7 repite el borde interior negativo y no comprueba el borde exterior \(2+m<4\). La inclusión en \((-4\mu,0)\) es cierta (\(2+\sqrt{1/10}<4\)) y el contrato 2 ya certifica \(2+m<4\) en P7; un chequeo homónimo en este script alinearía la docstring con la prueba ejecutada. No cambia la ortonormalidad.

El techo del argumento es el puente escrito del contrato 2, reparado y no re-revisado. El informe ya lo dice; la adaptación \((+,-)\) no lo reabre.

**Reparaciones obligatorias: ninguna.**
