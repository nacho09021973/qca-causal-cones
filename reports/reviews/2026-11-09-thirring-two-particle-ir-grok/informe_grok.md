<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 76c67e130e69abd1bb64c0046e6ca4f6c8d5426166faaa8b9ef477017a4ce8a5
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-09T10:48:28Z  fin: 2026-11-09T11:05:10Z
documento: /home/ignac/qca-causal-cones/theory/THIRRING_TWO_PARTICLE_IR_PREFLIGHT_GATE.md ; último commit observado: 6d24fb8 ; sha256 de la copia enviada 73472f8ef1776321e2de29f69775d969593fc08177b9ed1906184f389fbbf786
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-two-particle-ir.md ; último commit observado: 3500cbc ; sha256 de la copia enviada 465b198b5ebe374468965ec554337ce9f37bca46874f8263a9554a8d18d02a83
documento: /home/ignac/qca-causal-cones/scripts/verify_thirring_two_particle_ir.py ; último commit observado: 68e1a55 ; sha256 de la copia enviada 9e3fafc8abe16ae336a7b3110c415377b92c354862765f28720035aeeb26603a
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-two-particle-ir.txt ; último commit observado: 3500cbc ; sha256 de la copia enviada c7b2d99df29f7cf360ef8bebdc5fbdbff49e59a4f2571b3d8ffde9f2127e24e4
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-two-particle-ir-failed-run-4-note.txt ; último commit observado: 68e1a55 ; sha256 de la copia enviada 635ff0fef0b72ee89166c41529b61d444b1a0ed7b6d27bdad95a8ed85ef65708
documento: /home/ignac/qca-causal-cones/sources/1804.08508v1.pdf ; último commit observado: 58a345b ; sha256 de la copia enviada 495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0
documento: /home/ignac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_grok.txt sha256 4d6cf40f754f1e6167b355eb6f2047393ef513b2d61c814fd647069135131074
respuesta sha256 c5d2cdea3c09398d6c4d8a2ffd455dd9d22af669ad4e634af6c2e73dd6c0cddd
-->

**Reparación necesaria.** Las identidades de O1, O2 y de la rama en \(k_R=\pi\) salen bien por derivación directa; el rótulo `IR_BOUND_BRANCH_RELATIVISTIC / DOUBLER_CHANNEL_OPEN` no es el cierre que autoriza el contrato cuando en la ventana no hay rama ligada y O4 sigue abierto. No hay una serie o un límite falso que invierta las cuentas de esa rama.

No ejecuté el script. Lo que sigue marcado como derivado está recalculado desde las definiciones y los dos PDF; lo demás es inspección del código, del registro y de la nota de la cuarta ejecución.

## Qué se sostiene

**O1.** Con \(U=FJ\) y \(J\) antes que \(F\), como en 1804.08508 (p. 3: \(U_N=W_N V_{\mathrm{int}}\)). En el código M=1 los únicos pares en el mismo sitio y de componentes opuestas son 01 y 10; ahí \(J\) multiplica por \(e^{i\chi}=i\) y en 00 y 11 por 1. Como ese factor es escalar en cada vector del código, \(UB=FJB=FBD\) con \(D=\mathrm{diag}(1,i,i,1)\) para todo \(\mu\). El soporte tras un paso cabe en la ventana que recorre el script. No depende de la convención de signo del salto.

**O2.** \(\omega(q)=\arccos(\nu\cos q)\), \(\omega_0=\arccos\nu=\arcsin\mu\in(0,\pi/2)\). De \(\omega'=\nu\sin q/\sin\omega\) salen \(\omega'(0)=0\) y
\[
\omega''(0)=\frac{\nu\sin\omega_0}{\sin^2\omega_0}=\frac{\nu}{\mu}.
\]
Como \(\omega\) es par, \(\omega^2=\omega_0^2+c_f^2 q^2+O(q^4)\) con \(c_f^2=\omega_0\nu/\mu\). Luego \(\omega_0/\mu\to 1\) y \(c_f^2\to 1\). El umbral de un par libre a momento total \(P=2p\) cumple \((2\omega(P/2))^2=(2\omega_0)^2+c_f^2 P^2+O(P^4)\).

**O3, lado \(\Gamma_0\).** Con \(e^{-i\chi}=-i\), \(k=i\kappa\) y \(\sin\omega(i\kappa)=S=\sqrt{1-\nu^2\cosh^2\kappa}\) (rama positiva en el eje real), el numerador de \(T_+\) es \((-i)(1-i)(S-\nu\sinh\kappa)\). Se anula solo si \(S=\nu\sinh\kappa\). Para \(\kappa\) real eso exige \(S\) real y \(\ge 0\), luego \(\kappa\ge 0\). En la hoja en que \(|\nu\cosh\kappa|>1\), \(G_0=1\neq i\), así que tampoco hay raíz. Con la onda del artículo, \(|e^{-iky}|=e^{k_I y}\) en \(y>0\): decae si y solo si \(k_I<0\) (1804.08508 ec. (19); 1711.03920, Lema 2). La raíz de \(\Gamma_0\) en \(p=0\) no es normalizable. El Lema 2 no se aplica en \(p=0\) (exige \(p\neq z\pi/2\)); en \(p\neq 0\) pequeño, \(\chi=\pi/2\) sí cae en su hipótesis (\(e^{i\chi}=i\notin\{1,-1,e^{\pm 2ip}\}\)).

**O3, rama \(k=\pi+i\kappa\).** \(\omega(q+\pi)=\pi-\omega(q)\) da \(g_+(x\pm\pi)=-g_-(x)\). En \(p=0\) la condición \(T_+=0\) se reduce a \(\sin\omega(i\kappa)=-\nu\sinh\kappa\), es decir \(\cosh 2\kappa=1/\nu^2\). La raíz normalizable es la negativa:
\[
\sinh\kappa_0=-\frac{\mu}{\nu\sqrt{2}},\qquad \cos\omega(i\kappa_0)=C_0=\sqrt{\frac{1+\nu^2}{2}},\qquad \sin\omega(i\kappa_0)=\frac{\mu}{\sqrt{2}}.
\]
Entonces \(\omega_{++}(0,\pi+i\kappa_0)=2(\pi-\theta)\) con \(\cos\theta=C_0\), y el autovalor unitario es
\[
e^{-i\omega_{++}}=e^{i 2\theta}=e^{i M_b},\qquad \cos M_b=\nu^2,\qquad M_b=2\arcsin(\mu/\sqrt{2}).
\]
En el convenio de 1804.08508 ec. (6), \(\lambda=e^{-i\phi}\), esto es \(\phi=-M_b\). Como \(\cos M_b=\nu^2>2\nu^2-1=\cos(2\omega_0)\) y ambos ángulos están en \((0,\pi)\), \(M_b<2\omega_0\), así que \(-2\omega_0<-M_b<0\): la rama está en el hueco del borde \(-2\omega_0\) (autovalor \(e^{i 2\omega_0}\)), no junto al umbral \((+,+)\) de cuasienergía \(+2\omega_0\) (autovalor \(e^{-i 2\omega_0}\)). El vector del script reproduce 1804.08508 ec. (19) y el Apéndice A: paridad par/impar de \(y\), factor \(e^{-i\chi}\) en la componente 2 en \(y=0\), y \(t=e^{\kappa}=(\sqrt{2-\mu^2}-\mu)/(\sqrt{2}\,\nu)\) con \(t^2=(1-\mu\sqrt{2-\mu^2})/\nu^2\in(0,1)\). La extensión por recurrencia es correcta aunque no esté certificada: para \(|y|\ge 3\) el stencil no ve \(y=0\), el residuo es geométrico de razón \(\lambda=-t\) y período 2, y \(y=3,4\) fijan las dos paridades; \(y<0\) sale de la antisimetría y el resto de los \(w\), de \(p=0\).

**O3, curvatura (solo esta rama).** En \(z_0=i\kappa_0\), \(\omega'=\nu\sin z/\sin\omega\) da \(\omega'(z_0)=-i\) y \(\omega''(z_0)=2\sqrt{2}\,C_0/\mu\). La condición equivalente, donde vale la reflexión de Schwarz (válida cerca de \(z_0\), lejos del corte), es \(F=\mathrm{Re}((1+i)X)=0\) con \(X=\sin\omega-\nu\sin\). Sale \(F_\kappa(0)=2C_0\neq 0\) y \(F_{pp}(0)=2\sqrt{2}/\mu\), luego por la función implícita la raíz en \(k_R=\pi\) continúa a \(p\) pequeño y
\[
\kappa''(0)=-\frac{\sqrt{2}}{\mu C_0},\qquad E''(0)=\frac{2\sqrt{2}\,\nu^2}{C_0\mu},
\]
con \(E(p)=2\mathrm{Re}\,\omega(p+i\kappa(p))\). Con \(P=2p\), \(E^2=M_b^2+c_b^2 P^2+O(P^4)\) y
\[
c_b^2=\frac{M_b\nu^2}{\sqrt{2}\,C_0\mu}.
\]
Límites: \(M_b/\mu\to\sqrt{2}\), \(C_0\to 1\), \(c_b^2\to 1\). Serie, a mano hasta \(O(\mu^2)\): \(c_b^2=1-(2/3)\mu^2+O(\mu^4)\), \(c_f^2=1-(1/3)\mu^2+O(\mu^4)\), así que \(c_b^2-c_f^2=-\mu^2/3+O(\mu^4)\). Hacer primero \(P\to 0\) a \(\mu\) fijo y después \(\mu\to 0\) es exactamente el observable congelado (coeficiente de \(P^2\)); no da \(\omega_b(\mu Q)/\mu\). El informe lo dice y no lo afirma.

**Signo de \(\chi\).** La conjugación \(W(q)\mapsto\sigma_z W(-q)\sigma_z\) y \(J(\chi)\mapsto J(-\chi)\) es correcta. Pasa \(e^{i M_b}\) a \(e^{-i M_b}\), es decir al lado \(+2\omega_0\). Eso es \(\chi=-\pi/2\), fuera de F. No entra en el veredicto. 1711.03920 ec. (4) usa \(e^{i\omega}\) y 1804.08508 ec. (6) usa \(e^{-i\omega}\); el informe sigue a 1804. El pie de la Fig. 4, en el texto extraído, no fija el eje con la seguridad bastante para contradecir esta cuenta.

**O4, el límite que sí está bien.** \(g_+(\mu Q)/(-i\mu)\to\sqrt{1+Q^2}+Q=e^{\theta}\), \(\theta=\mathrm{asinh}\,Q\). En el sistema de momento total nulo en rapideces, \(T_+\) tiende a una fase que depende solo de \(\Delta\). El script certifica el límite de \(g_+\), no el álgebra de \(T_+\); esa álgebra es inmediata. \(\Gamma W\Gamma=-W\) con \(\Gamma=\sigma_z(-1)^x\) también sale (un salto cambia el signo de \((-1)^x\)).

**Script y ejecuciones.** El registro tiene 34 PASS y el recuento de nombres cuadra. Esas líneas cubren lo que el informe dice que certifican, y el propio informe deja fuera la unicidad, la continuidad, la recurrencia global, el paso \(\chi\to-\chi\) y todo O4 salvo \(\Gamma\) y \(g_+\). La cuarta ejecución fallida encaja con el código: exigir que los dos coeficientes de \(A+BT\) se anulen es falso cuando \(t=\sqrt{r}\) desenreda, y el arreglo \(A+Bt_{\mathrm{exp}}\) no cambia el enunciado. Las otras tres son fallos de herramienta (radicales, serie de \(\arccos\)). No hay indicio de haber movido la expectativa. El 34/34 no prueba los pasos no escritos en `exact`.

## Objeciones

1. **Veredicto, contrato sec. 5 y sec. 3; informe sec. 1 y sec. 5.** Alta. En la ventana congelada —rama \((+,+)\) cerca de la cuasienergía \(+2\omega_0\)— no hay rama ligada: el único estado puntual que continúa desde \(p=0\) está en \(\phi=-M_b\). El contrato dice que eso no es un negativo, que O3 se informa como «no hay rama ligada» y que entonces (R) descansa en O2 y O4. O4 está abierto, así que (R) no está establecido. `IR_BOUND_BRANCH_RELATIVISTIC / DOUBLER_CHANNEL_OPEN` es «lo de arriba, pero O4 sin decidir»; «lo de arriba» incluye el régimen relativista. La lectura vacua de «toda rama ligada de la ventana» está dicha en el informe, pero la frase específica del caso vacío es la que manda y no se cumple. La sec. 5 reintroduce esa rama: «la puerta y un sector de baja energía coexisten» y «la única rama ligada (en \(-2\omega_0\)) tiende a la misma velocidad». Eso es otra pregunta que la ventana congelada. Reparación: dejar el rótulo en que O1 y O2 valen, que en la ventana no hay rama ligada, que la rama de \(-2\omega_0\) queda fuera del veredicto, y que el régimen (R) no está decidido mientras O4 siga abierto; quitar de la sec. 5 la coexistencia y el uso de \(c_b\to 1\) como respuesta a (R).

2. **Informe sec. 3.3, frase sobre \(E(p)\).** Media. \(E(0)=M_b=\arccos(\nu^2)\) es la distancia a la cuasienergía 0, no al borde \(-2\omega_0\). La distancia a ese borde es \(2\omega_0-M_b\). Las fórmulas posteriores usan \(E\) como \(|\phi|\) y son las que calculé; la frase no lo es. No cambia \(c_b^2\) ni los límites. Reparación: sustituirla por «\(E(p)\) es el módulo de la cuasienergía, \(\phi=-E\), contado desde el mismo cero que \(+2\omega_0\)».

3. **Informe sec. 4, identificación de subespacios.** Media, no sostiene el rótulo porque O4 queda abierto. \(\Gamma_1\Gamma_2=\sigma_z^{(1)}\sigma_z^{(2)}(-1)^{x_1+x_2}\) multiplica por \((-1)^w\) y manda el momento total \(p\) a \(p+\pi\). El proyector \(P\) de 1804.08508 ec. (8) fija la paridad de \(y\) según la componente y conserva \(p\). Los dos son invariantes por razones distintas; no son el mismo subespacio. El peso \(1/2\) no está demostrado: ec. (18) iguala coeficientes de \(v^{++}_k\) y \(v^{--}_{k-\pi}\), no el peso \(L^2\) de un paquete. Reparación: separar las dos simetrías y no tratar \(1/2\) como identidad certificada.

4. **O4 abierto.** No es evasión. El contrato pide un análisis de paquetes escrito antes de evaluar y a la vez usa «peso» en O4 y «transferencia» en `DOUBLER_TRANSFER_PERSISTS_IN_IR`. El contenido cinemático (presente también al entrar y sin interacción) y la transferencia dinámica no son la misma lectura; elegir una después de haber visto \(1/2\) y \(0\) sería posterior a los hechos. Dejar O4 en OPEN y marcar el contrato como defectuoso es lo correcto. No autoriza, por omisión, el régimen relativista.

No encontré otro fallo de identidad, serie o límite. En particular \(\omega''(0)=\nu/\mu\), \(c_f^2=\omega_0\nu/\mu\), \(\cosh 2\kappa=1/\nu^2\), \(\cos M_b=\nu^2\), \(\omega'(z_0)=-i\), \(E''(0)\) y \(c_b^2-c_f^2=-\mu^2/3+O(\mu^4)\) están bien. La ilustración a \(\mu=3/5\) no entra en el veredicto; el registro muestra que la diferencia finita y la forma cerrada coinciden hasta \(\sim 10^{-8}\), como corresponde a \(h=10^{-4}\), no que sean el mismo número digit a digit.

## Alcance que acepto

Familia F: \(\chi=\pi/2\), \(0<\mu<1\), solo el sector de dos fermiones y solo la regla.

- La puerta \(D=\mathrm{diag}(1,i,i,1)\) a \(T=1\) vale en todo F sobre los cuatro estados del código M=1. Son estados de escala de red, no paquetes de baja energía. No digo que la puerta actúe en el IR.
- Partícula libre: \(c_f\to 1\) y \(\omega_0/\mu\to 1\), en el sentido del coeficiente de \(q^2\) y, de hecho, de \(\omega(\mu Q)/\mu\to\sqrt{1+Q^2}\). Eso último sale de la fórmula exacta; el informe solo necesitaba el coeficiente.
- Ventana congelada, umbral \(+2\omega_0\), \(P\to 0\): no hay rama ligada.
- Fuera de esa ventana, umbral \(-2\omega_0\): una rama con \(M_b/\mu\to\sqrt{2}\) y \(c_b\to 1\), solo a nivel de masa en reposo y de coeficiente de \(P^2\), con \(P\to 0\) antes que \(\mu\to 0\). No es la función de escala. No forma parte de (R).
- O4 sin decidir. El límite de \(T_+\) en rapideces es un enunciado de dispersión a momentos reales, no un peso de doblador.
- Nada de esto es universalidad componible, ni un límite de QFT relativista en interacción, ni un enunciado fuera de dos partículas. El subespacio de autovalor 1 en \(p=0\) (cuasienergía 0, estados \(v^{+-}\)) queda fuera de la ventana, como dicen el contrato y 1804.08508 p. 13.
