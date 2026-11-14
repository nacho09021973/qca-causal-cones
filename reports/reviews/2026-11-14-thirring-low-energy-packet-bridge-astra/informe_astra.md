<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 2a7342b9b98093585e3f8114524ec6840b6dc70f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.169.0)
inicio: 2026-11-14T14:22:26Z  fin: 2026-11-14T14:24:41Z
documento: /home/adnac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.md ; último commit observado: 77c9776 ; sha256 de la copia enviada 115240689eb2e1d47a94a5ac78aa5df8099158ae16c72420b7eaab323bd864ab
documento: /home/adnac/qca-causal-cones/reports/reviews/2026-11-09-thirring-low-energy-packet-astra/informe_astra.md ; último commit observado: 77c9776 ; sha256 de la copia enviada 02c396890d55f04236d94179ebfc33a8df06be567297283f9a47ca12f2130792
documento: /home/adnac/qca-causal-cones/theory/THIRRING_LOW_ENERGY_PACKET_GATE.md ; último commit observado: 715096f ; sha256 de la copia enviada aa2da12d4211a969a010a64e122b793ac3ed26b9f060c1cf4cd21868bf7e19ee
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_low_energy_packet.py ; último commit observado: 8b41761 ; sha256 de la copia enviada a1900674990354db197e7daddfdefb46d0a23536ba3b5e0688c2b45250f4d517
documento: /home/adnac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.txt ; último commit observado: b4ac949 ; sha256 de la copia enviada 151cc20d86d6704d5b6067c10acc7d47bf2f83a313d3c8cbddccc4992f5ab9dd
documento: /home/adnac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
documento: /home/adnac/qca-causal-cones/sources/1804.08508v1.pdf ; último commit observado: 58a345b ; sha256 de la copia enviada 495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0
entrada_astra.txt sha256 41e827cfebd9045a326f830710c748058c7309c1822fe07eac0370dae84f40c5
respuesta sha256 083f0e9ac4bee37a7081647eac170470ce8e9410efab59af7c39d5163cd6b3ed
-->

**Dictamen global: PASS para el puente del contrato declarado. No encuentro reparaciones obligatorias pendientes.** Las siete correcciones están resueltas. Hay aclaraciones de notación y alcance que conviene incorporar antes de reutilizar el puente.

Revisión manual del material adjunto, sin ejecución. No uso el informe anterior como prueba. Las referencias a páginas corresponden al texto extraído suministrado; la fidelidad de la extracción al PDF original queda **[UNVERIFIED]**.

**1. Autofunciones exactas — PASS**

La condición de contacto da correctamente
\[
z(b-Tc)=Tb-c
\quad\Longrightarrow\quad
T=\frac{c+zb}{b+zc}.
\]
Con los espinores normalizados,
\[
b=-\frac{\mu a_2}{N_1N_2},\qquad
c=-\frac{\mu a_1}{N_1N_2},\qquad
a_j=\sin\omega(q_j)+\nu\sin q_j,
\]
de donde se recupera la fórmula en términos de \(g_+\).

La antisimetría por sí sola no demostraría la ecuación de evolución. Aquí sí existe una comprobación local suficiente: usando `W_pre`, las ecuaciones en \(y>0\) que reciben contribuciones del contacto utilizan \(RL\), para el cual \(Jf_{RL}=H_{RL}\). La ecuación de salida \(LR\) en \(y=0\) recibe únicamente fuentes de \(y\ge0\), incluida esa misma componente corregida; por tanto coincide con la ecuación libre de \(H\). La ecuación \(RL\) restante sigue por antisimetría. Las componentes excluidas por \(G=-1\) permanecen nulas porque \(U\) conserva ese sector. Esto vale paramétricamente, sin apoyarse en los dos puntos certificados.

La comprobación concuerda con las ecuaciones locales (10), (15)–(18) de 1804.08508, pp.6, 8–9 del extracto.

Para precisar la uniformidad, defino
\[
s_\mu(Q)=\nu\frac{\sin(\mu Q)}{\mu},\qquad
A_\mu(Q)=\sqrt{1+s_\mu(Q)^2}+s_\mu(Q).
\]
Entonces \(a_j=\mu A_\mu(Q_j)>0\). En \(|Q|\le2.32\), \(A_\mu\) tiene cotas positivas superior e inferior independientes de \(\mu\). Así,
\[
T=\frac{a_1-ia_2}{a_2-ia_1},\qquad |T|=1,
\qquad |a_2-ia_1|\ge c\mu.
\]

**Aclaración:** el denominador escrito con \(g_+\) no está separado de cero por una constante independiente de \(\mu\); lo está **después de dividirlo por \(\mu\)**. El informe ya introduce esa precisión en §4(iii)–(v). El denominador \(b+zc\), con espinores normalizados, sí admite una cota uniforme positiva. No hay singularidad en \(p=0\).

**2. Solución exacta que aproxima el paquete y unitariedad — PASS**

El coeficiente
\[
\frac1{2\pi\sqrt2}\,\frac12
\]
es correcto: \(1/(2\pi)\) procede de las dos transformadas de Fourier, \(1/\sqrt2\) del producto exterior normalizado y \(1/2\) de \(P=(1-G)/2\).

La normalización de los cuatro espinores es compatible: el intercambio conserva \(N_1N_2\), y
\[
g_-(q+\pi)=-g_+(q)
\]
conserva cada norma y da exactamente \(\sigma_zv_q^+=v_{q+\pi}^-\).

Además, \(\widetilde\psi(t)\in\ell^2\) puede demostrarse **sin depender de las cotas de cola**. Cada onda integrada es la transformada de Fourier de una función en \(L^2\): \(c\in L^2\), los espinores están normalizados y \(|T|=1\). Las restricciones a semiespacios, la reflexión con intercambio y la modificación de fase en el contacto son operadores acotados. Su combinación finita sigue en \(\ell^2\).

La acción de \(U\), de alcance finito, puede intercambiarse con las integrales; para cada \(\mu>0\) los integrandos son integrables. Por ello,
\[
\widetilde\psi(t)=U^t\widetilde\psi(0)
\]
para tiempos enteros, y la igualdad de normas solicitada es exacta. No se acumula un error por cada uno de los \(4L\) pasos.

Como comprobación adicional, al poner \(\chi=0\), \(T=1\), la fórmula reproduce exactamente \(F^tPB\).

**3. Error inicial, colas y velocidades — PASS**

La representación mediante \(A_\mu(Q)\) anterior también cierra las cotas de derivadas. Esa familia es suave hasta \(\mu=0\) en el compacto utilizado; lo mismo ocurre con
\[
v_{\mu Q}^+=-i\,\frac{(1,A_\mu(Q))}{\sqrt{1+A_\mu(Q)^2}}
\]
y con \(T\). Por cambio de variable se obtienen las cotas \(C_j\mu^{-j}\) para \(j=1,2\).

La dispersión cumple exactamente
\[
\omega''(q)=
\frac{\nu\mu^2\cos q}
{(\mu^2+\nu^2\sin^2q)^{3/2}},
\qquad |\omega''(q)|\le\mu^{-1}.
\]
Las dos derivadas reescaladas de la fase residual están acotadas por \(C t\delta^2/\mu=O(1)\).

Las dos integraciones por partes son legítimas: \(h\) se anula en los extremos y su segunda derivada distribucional es una medida finita, incluidos los saltos de \(h'\). Se obtiene el decaimiento cuadrático anunciado.

El factor no separable no introduce un hueco. Fijando \(q_2\), se aplica la estimación en \(q_1\); después Parseval en la segunda variable integra el factor \(|\phi_B(q_2)|^2\), cuya integral es uno. Esto controla las colas marginales. Intercambiando las variables se controla la otra marginal. **No se necesitan derivadas mixtas ni factorización de \(T\).**

La masa de cola es \(O((\delta D)^{-3})\); su norma es \(O((\delta D)^{-3/2})\). Para \(D\asymp L\), resulta \(O(\mu^{3/4})\).

La geometría también cierra, incluido el contacto: estar en el semiespacio incorrecto obliga a una desviación monoparticular de al menos \(L\) inicialmente o \(1.2L\) finalmente.

La cota de velocidad se comprueba con
\[
|\omega'(\mu Q)|\ge
\sqrt{0.99}
\left(1-\frac{0.01(2.32)^2}{6}\right)
\frac{0.68}{\sqrt{1+0.68^2}}>0.55.
\]
Para B, \(\omega'<0\); con la convención Fourier declarada, B se desplaza hacia la derecha.

**Aclaración editorial:** §2 conserva «\(\omega'(q)>0\)». Debe leerse, como explica la frase siguiente, para \(q>0\); añadir esa condición evitaría una contradicción aparente. §4(iv) ya está correctamente corregida.

**4. Variación de fase y límite — PASS**

La suavidad uniforme de \(A_\mu\) y la cota del denominador proporcionan
\[
|\nabla_qT|\le C/\mu.
\]
Como cada rectángulo de soporte tiene diámetro \(O(\delta)\),
\[
\sup|T-T_c|=O(\sqrt\mu).
\]
Parseval controla el multiplicador \(T-T_c\), y las restricciones espaciales no aumentan la norma. Esto justifica el presupuesto de errores anunciado.

Respecto de \(k=0\), hay que distinguir coordenadas:
\[
q_1-q_2=\mu(k_a+k_b)+[-2\delta,2\delta],
\qquad
k=\frac{q_1-q_2}{2}\ge\mu-\delta>0.
\]
La separación central \(3\mu\) corresponde a las columnas mixtas; el mínimo entre todas las columnas es \(2\mu\). La distancia del soporte de \(k\) a cero, medida en anchuras \(\delta\), diverge como \(\mu^{-1/2}\). No existe una distancia absoluta positiva al tomar el límite, pero tampoco se necesita: las estimaciones son uniformes en las variables reescaladas.

Para explicitar la norma de operador, sea \(D_\mu=\operatorname{diag}(T_c^{ab})\). El puente da
\[
U^TB_\mu=
F^TB_\mu\frac{I+D_\mu}{2}
+F^TGB_\mu\frac{I-D_\mu}{2}+R_\mu,
\qquad \|R_\mu\|=O(\sqrt\mu).
\]
Cuatro cotas uniformes por columnas bastan, pues \(\|R_\mu\|\le2\max_{ab}\|R_\mu|ab\rangle\|\).

Una segunda comprobación del ensamblaje es
\[
E_\mu^*E_\mu=I-K_\mu^*K_\mu.
\]
Con el límite de \(K_\mu\), reproduce los \(\ell_{ab}\) y \(\lim\|E_\mu\|=2/3\).

**Aclaración:** esto demuestra una aproximación en norma de operador con marcos dependientes de \(\mu\), y convergencia de \(K_\mu\) y \(E_\mu^*E_\mu\). No afirma que \(E_\mu\) converja como operador hacia un operador fijo.

**5. Estado de las siete reparaciones — PASS**

Uso la numeración de siete reparaciones del informe actual:

| Reparación | Estado | Frase que la resuelve |
|---|---|---|
| Fourier | Resuelta | «the factor \(1/(2pi)\) comes from the two normalized one-particle waves» |
| Colas uniformes | Resuelta | «including the jumps of \(h'\)» y «combined with Parseval in the other variable» |
| Velocidad de B | Resuelta | «\(|\omega'(q)|\ge0.55\)» y «For B, omega' < 0» |
| Identidad paramétrica | Resuelta | «General argument, for every \((q1,q2)\) in the support»; los puntos son «worked examples … not its proof» |
| Generalización universal | Resuelta | «The universal remark in the previous version is withdrawn» |
| Diagnóstico | Resuelta en su presentación | «the estimator … not an exact projective leakage» y «was not computed» |
| Recuento | Resuelta en el informe | «use a 30-digit numerical evaluation» y «their generality comes from the local structure, not from the count» |

**6. Alcance — PASS**

El informe separa suficientemente prueba escrita y comprobaciones: declara expresamente que las constantes no están verificadas por máquina y limita P3 a ejemplos. El encabezamiento histórico «39/39 exact» es impreciso, pero §6 lo corrige explícitamente; no aporta certificación del puente.

También excluye expresamente un no-go de Thirring y limita el descarte al código, interacción, calendario y marco congelados. Esa separación es correcta.

La ejecución efectiva, los commits y los valores del diagnóstico permanecen **OPEN / [UNVERIFIED]** en esta revisión documental; no son premisas necesarias del puente.

**Reparaciones obligatorias: ninguna.** Las aclaraciones señaladas precisan cómo reutilizar el resultado, sin cambiar su demostración ni ampliar su alcance.