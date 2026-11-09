<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.167.0)
inicio: 2026-11-09T12:06:43Z  fin: 2026-11-09T12:10:54Z
documento: /home/ignac/qca-causal-cones/theory/THIRRING_LOW_ENERGY_PACKET_GATE.md ; último commit observado: 715096f ; sha256 de la copia enviada aa2da12d4211a969a010a64e122b793ac3ed26b9f060c1cf4cd21868bf7e19ee
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.md ; último commit observado: b4ac949 ; sha256 de la copia enviada 7afe034ed0e044ee22db5fe80038c4c04a1d08c6f14ccd62175e66e5f3ad1e42
documento: /home/ignac/qca-causal-cones/scripts/verify_thirring_low_energy_packet.py ; último commit observado: 8b41761 ; sha256 de la copia enviada a1900674990354db197e7daddfdefb46d0a23536ba3b5e0688c2b45250f4d517
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet.txt ; último commit observado: b4ac949 ; sha256 de la copia enviada 151cc20d86d6704d5b6067c10acc7d47bf2f83a313d3c8cbddccc4992f5ab9dd
documento: /home/ignac/qca-causal-cones/scripts/diag_thirring_low_energy_packet.py ; último commit observado: 75b33c3 ; sha256 de la copia enviada 232c0b330a804b4036d054b836e15b8367656b89cdec8621794b188cbcf89e51
documento: /home/ignac/qca-causal-cones/reports/2026-11-09--thirring-low-energy-packet-diagnostic.txt ; último commit observado: 8b41761 ; sha256 de la copia enviada a78bde4d67e800455dd53e7d952d59c3473ef6deb1c4d90efea6d14ab9b9d31b
documento: /home/ignac/qca-causal-cones/sources/1804.08508v1.pdf ; último commit observado: 58a345b ; sha256 de la copia enviada 495646b1a0c0a2822422c4d65536b8c4caa0d82c5efe7e48df878766af91f0d0
documento: /home/ignac/qca-causal-cones/sources/1711.03920v1.pdf ; último commit observado: 45b933f ; sha256 de la copia enviada 3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca
entrada_astra.txt sha256 dcd975456346fdd3ed4d9a67a16c945f99cf48fe64617e6bff76d1883f9a3b37
respuesta sha256 c539900803f70b717c766a2b4264de2b6dddddbc40fa4a9bee2fd39788b178bf
-->

**Veredicto: reparación necesaria.** La conclusión `NO_ENTANGLER_IN_DECLARED_PACKET_CODE` se sostiene al completar la demostración, sin cambiar la construcción congelada. Pero el informe contiene una omisión de normalización en la superposición, una justificación insuficiente de las cotas uniformes y una generalización injustificada al final del balance.

Las derivaciones siguientes son manuales. Los scripts y registros sólo los he inspeccionado; no los he ejecutado. Las referencias a los artículos corresponden al texto extraído adjunto, no a una consulta de los PDF originales.

**1. Admisión y estructura**

La normalización del sobre es correcta:
\[
\int h(t)^2\,dt
=\frac{15}{16}\left(2-\frac43+\frac25\right)=1.
\]
Como \(\delta/\mu=\sqrt\mu<1/\sqrt{10}<1/2\), los cuatro intervalos de momento son disjuntos. Además,
\[
0<\mu-\delta\le |q|\le2\mu+\delta<4\mu.
\]
Los espinores están normalizados y la transformación de Fourier es unitaria. Por tanto, los cuatro modos monoparticulares son ortonormales y sus productos exteriores satisfacen
\[
B_\mu^*B_\mu=I_4.
\]

La admisión energética también pasa. Usando
\[
\sin^2\omega(q)=\mu^2+\nu^2\sin^2q,
\]
se obtiene, uniformemente para \(Q=q/\mu\) en los soportes,
\[
\frac{\omega(\mu Q)}{\mu}\longrightarrow\sqrt{1+Q^2}.
\]
La banda positiva es una propiedad exacta de los modos preparados.

Con la convención declarada, la fase espacial y temporal es
\[
-q(x-x_c)-t\omega(q).
\]
Su centro se desplaza como \(x_c-t\omega'(q_c)\). Puesto que
\[
\omega'(q)=\frac{\nu\sin q}{\sin\omega(q)},
\]
A se mueve hacia la izquierda y B hacia la derecha. No encuentro inversión del sentido de colisión. **La frase de §4(iv), “\(\omega'(\mu K)\ge0.55\) para ambos paquetes”, debe decir \(|\omega'(q)|\ge0.55\): para B la derivada es negativa.**

La identidad \(\Gamma W\Gamma=-W\) se demuestra directamente sobre cada transición: los desplazamientos cambian la paridad espacial y las conversiones \(R\leftrightarrow L\) cambian el signo de \(\sigma_z\). Ambas reciben un signo negativo. Así, \(G=\Gamma_1\Gamma_2\) conmuta con \(F\).

En contacto, los componentes permitidos por antisimetría son \(RL\) y \(LR\), y ambos tienen \(G=-1\). Además, \(J\) conmuta con \(G\). En consecuencia,
\[
U(1-P)=F(1-P),\qquad P=(1-G)/2,
\]
exactamente, y la igualdad se conserva al iterar.

La identidad normalizada
\[
\sigma_zv_q^+=v_{q+\pi}^-
\]
es correcta: también coinciden los factores de normalización. Por separación de soportes,
\[
B_\mu^*GB_\mu=0,\qquad B_\mu^*PB_\mu=\tfrac12 I_4.
\]
Esto vale para cualquier entrada lógica, no sólo para las cuatro columnas. Asimismo,
\[
Q_DB_\mu=Q_DB_{\rm out}=0,\qquad Q_DGB_\mu=GB_\mu.
\]

**2. Autofunción: dos puntos no bastan, pero hay una prueba general**

Las comprobaciones en dos pares de momentos, ambas con \(\mu=3/5\), **no certifican una identidad sobre el soporte del contrato**. Tampoco la simetría \(G\), por sí sola, determina el coeficiente de dispersión.

La identidad general sí puede justificarse con las ecuaciones locales, coincidiendo con la derivación de 1804.08508, pp.8–9, Ecs.(14)–(18).

Escribamos
\[
v_{q_1}^+\otimes v_{q_2}^+=(a,b,c,d)^T,\qquad z=e^{-i\chi}.
\]
Sea \(H\) la combinación de cuatro ondas del informe, antes de modificar el contacto. Cada onda tiene el mismo autovalor libre: desplazar ambos momentos por \(\pi\) y cambiar ambas bandas introduce dos signos negativos, cuyo producto es positivo.

En \(y=0\), los componentes no nulos de \(H\) son proporcionales a
\[
H_{RL}=2(b-Tc),\qquad H_{LR}=2(c-Tb).
\]
La modificación propuesta da \(f_{RL}=zH_{RL}\), \(f_{LR}=H_{LR}\). La antisimetría en contacto exige
\[
z(b-Tc)=Tb-c.
\]
Por tanto,
\[
T=\frac{c+zb}{b+zc}
 =\frac{g_+(q_1)+zg_+(q_2)}
        {g_+(q_2)+zg_+(q_1)}.
\]

Esto comprueba también que la fase debe aplicarse **sólo a \(RL\)** en esa representación.

La suficiencia se puede ver directamente con `W_pre`: en el semiespacio positivo, las transiciones que alcanzan el contacto utilizan su componente \(RL\). Allí \(Jf_{RL}=H_{RL}\). Las ecuaciones restantes se obtienen por antisimetría; las componentes incompatibles con \(G=-1\) son nulas. Así se recupera la ecuación libre de \(H\) donde corresponde y queda satisfecha la ecuación de \(U\).

Para \(\chi=\pi/2\), poniendo \(g_+(q_j)=-ia_j\), se tiene \(a_j>0\) y
\[
T=\frac{a_1-ia_2}{a_2-ia_1},\qquad
|a_2-ia_1|^2=a_1^2+a_2^2>0,\qquad |T|=1.
\]
No aparece una singularidad en \(p=0\). Esta derivación cubre todo el soporte; también concuerda con el tratamiento de \(p=0\) en 1804.08508, pp.12–13.

No hace falta demostrar completitud espectral ni excluir todos los estados ligados. Basta construir esta solución y aproximar el estado inicial en norma: la unitaridad controla cualquier componente restante.

**3. Puente de paquetes: corrección y cotas uniformes**

Hay una omisión literal en §4(ii). Con \(f\) definido mediante exponentiales sin normalización espacial y \(c=\phi_A\phi_B\), la superposición correcta es
\[
\widetilde\psi(t)=
\frac1{2\pi\sqrt2}
\int\!\!\int c(q_1,q_2)e^{-it(\omega_1+\omega_2)}
\,\frac12 f_{q_1,q_2}\,dq_1dq_2.
\]
El factor \(1/(2\pi)\) proviene de las dos ondas monoparticulares normalizadas. **Tal como está escrita la fórmula del informe, falta ese factor**, y la identificación con \(PB\) no tiene error pequeño. Si se pretendía una medida normalizada implícita, debe declararse.

Con esta corrección, la superposición satisface exactamente
\[
U\widetilde\psi(t)=\widetilde\psi(t+1).
\]
La localidad de \(U\) permite intercambiar su acción con las integrales. La pertenencia a \(\ell^2\) resulta de las estimaciones siguientes.

El argumento de colas del informe necesita incluir los espinores, el multiplicador \(T(q_1,q_2)\), que no es separable, y la dispersión. Una forma de hacerlo sin perder los exponentes es reescalar
\[
q=q_c+\delta r,\qquad |r|\le1.
\]
En los soportes,
\[
\|\partial_q^jv_q^+\|\le C_j\mu^{-j},\qquad
|\partial_{q_i}^jT|\le C_j\mu^{-j},\qquad j=1,2,
\]
y \(|\omega''|\le C/\mu\). Estas cotas salen de las fórmulas explícitas: \(q/\mu\) permanece en un compacto y el denominador de \(T\) está separado de cero después de dividirlo por \(\mu\).

Separando la fase lineal en \(q_c\), la fase residual es
\[
t\big[\omega(q_c+\delta r)-\omega(q_c)
-\delta r\,\omega'(q_c)\big].
\]
Sus dos primeras derivadas respecto de \(r\) están uniformemente acotadas para \(0\le t\le4L\), porque
\[
t\delta^2/\mu\le4\lceil\mu^{-2}\rceil\mu^2=O(1).
\]
Por tanto, dos integraciones por partes, incluyendo los saltos de \(h'\), dan
\[
|\psi_t(x)|\le
C\delta^{1/2}
\big(1+\delta|x-x_c+t\omega'(q_c)|\big)^{-2}.
\]
Se sigue
\[
\sum_{|x-x_c+t\omega'(q_c)|\ge D}|\psi_t(x)|^2
\le C(\delta D)^{-3}.
\]

Para las ondas multiplicadas por \(T(q_1,q_2)\), se aplica la misma estimación en una variable y Parseval en la otra. Esto evita asumir que el paquete dispersado sigue siendo un producto.

La geometría necesaria es correcta:

- En \(t=0\), restringir una onda al lado incorrecto de \(y=0\) obliga a una desviación monoparticular de al menos \(L\).
- En \(t=4L\), los centros entrantes satisfacen \(x_1\le-1.2L\), \(x_2\ge1.2L\); los salientes tienen el orden contrario. La restricción incorrecta, incluida la línea de contacto, obliga a una desviación de al menos \(1.2L\).

Como \(\delta L\asymp\mu^{-1/2}\), estas colas tienen **norma**
\[
O((\delta L)^{-3/2})=O(\mu^{3/4}).
\]
Las constantes pueden elegirse comunes para las cuatro columnas. No hace falta que la dispersión residual tienda a cero: basta la acotación uniforme anterior.

Finalmente,
\[
\sup_{\rm soporte}|T-T_c|
\le C\delta/\mu=O(\mu^{1/2}).
\]
Parseval y la contractividad de las restricciones espaciales convierten esta cota en una cota de norma.

Un detalle que simplifica §4(iv): para \(\chi=0\), \(T=1\), la autofunción es exactamente la onda libre antisimetrizada y proyectada por \(P\). Con la normalización corregida,
\[
\widetilde\psi_{\rm free}(t)=F^tPB
\]
exactamente.

La unitaridad y las estimaciones anteriores proporcionan entonces
\[
U^TPB|ab\rangle
=T_cF^TPB|ab\rangle+O(\mu^{1/2}).
\]
Así queda cerrado el puente. La estimación aislada \((T/\mu)D^{-3}=O(\mu^3)\) escrita en el informe no era, por sí sola, una justificación suficiente.

**4. Ensamblaje y valores exactos**

Definiendo \(D_\mu=\operatorname{diag}(T_c)\), aquí sólo como matriz lógica, se obtiene
\[
U^TB_\mu=
F^TB_\mu\frac{I+D_\mu}{2}
+F^TGB_\mu\frac{I-D_\mu}{2}
+O(\mu^{1/2}).
\]
Los dos marcos son isometrías con rangos ortogonales. El segundo está íntegramente en el rango de \(Q_D\).

La uniformidad por columnas implica uniformidad en norma de operador, pues la dimensión lógica es cuatro. Por tanto,
\[
K_\mu\longrightarrow
\operatorname{diag}\left(\frac{1+T_{ab}}2\right),
\]
\[
E_\mu^*E_\mu\longrightarrow\operatorname{diag}(\ell_{ab}),
\qquad
B_\mu^*U^{-T}Q_DU^TB_\mu
\longrightarrow\operatorname{diag}(\ell_{ab}).
\]
Una comprobación independiente del ensamblaje es la identidad exacta
\[
E_\mu^*E_\mu=I-K_\mu^*K_\mu.
\]

Para los límites, escribamos
\[
A=e^{\operatorname{asinh}k_a},\quad
B=e^{-\operatorname{asinh}k_b},\quad
\Delta=\log(A/B).
\]
Entonces
\[
T_{ab}=\frac{A-iB}{B-iA},\qquad
\operatorname{Re}T_{ab}
=\frac{2AB}{A^2+B^2}=\frac1{\cosh\Delta},
\]
y
\[
\ell_{ab}=\frac{1-\operatorname{Re}T_{ab}}2
=\frac{\cosh\Delta-1}{2\cosh\Delta}.
\]
Como
\[
\cosh\Delta
=\sqrt{1+k_a^2}\sqrt{1+k_b^2}+k_ak_b,
\]
resultan exactamente
\[
\ell_{00}=\frac13,\qquad
\ell_{01}=\ell_{10}
=\frac{\sqrt{10}+1}{2(\sqrt{10}+2)},\qquad
\ell_{11}=\frac49.
\]

En particular,
\[
\lim_{\mu\to0}\|E_\mu\|=\frac23.
\]
Para cualquier entrada lógica normalizada, la fuga límite es la suma de estos valores ponderada por sus probabilidades en la base lógica; está entre \(1/3\) y \(4/9\). No hay una superposición lógica que elimine la fuga.

**5. Objeciones ordenadas por gravedad y reparación concreta**

1. **§4(ii)–(iii): normalización de Fourier omitida.**  
   La fórmula literal no aproxima \(PB\). Añadir \(1/(2\pi)\), o definir explícitamente que \(f\) ya incorpora ese factor. Es una reparación del escrito, no de la construcción.

2. **§4(iii)–(v): demostración incompleta de uniformidad.**  
   Faltan el control de las derivadas de los espinores y de \(T\), y el tratamiento del paquete no separable. Incorporar las cotas reescaladas anteriores cierra el hueco y conserva ambos exponentes. Corregir también el signo de la velocidad de B.

3. **§4(i), §6: alcance excesivo de la certificación en dos puntos.**  
   Dos puntos y la estructura no prueban la identidad paramétrica. La reparación es separar la prueba general de contacto de esos ejemplos exactos. La derivación anterior proporciona esa separación.

4. **§7, último punto: generalización no demostrada.**  
   No se deduce que cualquier código deba vivir enteramente en un sector de \(G\), o usar \(T=1\). La fuga depende del código de salida: un espacio que incluya los compañeros \(GB\) puede contener ambas componentes. Debe restringirse la observación al código y marco declarados. Llamarla “remark, not a theorem” no justifica la necesidad universal que enuncia.

5. **§5 y diagnóstico: la cantidad denominada `leakage` no es una fuga proyectiva exacta en la caja.**  
   El script calcula \(1-\sum_j|\langle C_j,\Psi\rangle|^2\), aunque sus modos truncados no están exactamente normalizados ni se acredita su ortogonalidad. Para un marco finito \(C\), con Gram \(H=C^*C\), la proyección ortogonal usa \(CH^{-1}C^*\), y la norma inicial tampoco es exactamente uno. Debe presentarse lo registrado como un estimador. Además, el script anuncia diagnósticos de envolvimiento periódico, pero no los calcula ni registra. Esto no afecta a la demostración analítica.

6. **§6: “39/39 exact checks” necesita matización.**  
   Las pruebas `P6-l_ab>0` incluyen `sp.N(...,30)>0`; esa parte es numérica. La positividad sí queda demostrada manualmente por \(\Delta>0\). P2 y P4 inspeccionan ventanas finitas; su generalidad procede de la estructura local, no del recuento. Los registros adjuntos concuerdan con las comprobaciones listadas, pero no constituyen una ejecución verificada por esta revisión.

Respecto al fallo inicial: bajar la cota auxiliar de \(0.555\) a \(0.55\) es matemáticamente legítimo y mantiene margen suficiente. No modifica paquetes, parámetros ni calendario. Sin embargo, la conservación del registro fallido, los commits y las autorizaciones de comandos están **[UNVERIFIED]**: esos materiales no se adjuntaron. Tampoco consta si el verificador modificado ya había sido revisado; no puede afirmarse ni descartarse una infracción de esa cláusula concreta.

**Alcance aceptable**

Aceptaría el resultado matemático, con las reparaciones indicadas, para los cuatro paquetes, interacción, tiempo y marco de salida congelados. Refuta una condición necesaria del contrato, por lo que corresponde el veredicto `NO_ENTANGLER_IN_DECLARED_PACKET_CODE`; no hace falta resolver adicionalmente si alguna fase sería entrelazante.

El balance es correcto al mantener abierto el contrato 1 y la coexistencia general, y al no abrir automáticamente un tercer contrato. Debe eliminarse la necesidad universal atribuida a otros códigos. No aceptaría ninguna exclusión del modelo Thirring ni una conclusión sobre su límite relativista interactuante.