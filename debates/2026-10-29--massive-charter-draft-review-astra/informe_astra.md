<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-29T17:54:18Z  fin: 2026-10-29T18:00:52Z
documento: /home/ignac/qca-causal-cones/theory/MASSIVE_RIGIDITY_GATE.md ; último commit observado: afc2b64 ; sha256 de la copia enviada b70881bb012dc3599e95b727d2730d467859587967fa6fa0e041a8559ad93a0f
documento: /home/ignac/qca-causal-cones/state/CURRENT_STATE.md ; último commit observado: ea3f401 ; sha256 de la copia enviada bcc1bbf8eccf483d252d10fdae8c02076254015bcf15122f1dee0748c4f11884
documento: /home/ignac/qca-causal-cones/theory/THREE_VELOCITIES.md ; último commit observado: 95f423f ; sha256 de la copia enviada bf1a746c557408d1ab5249210fba0566502677ab302e1068886f39b31d32ba41
documento: /home/ignac/qca-causal-cones/theory/S4_STRICT_CONE_COUNTEREXAMPLE.md ; último commit observado: 1dae941 ; sha256 de la copia enviada bc15165e1acb426884018860a78388facc7b98647eefb914e4f2bb2449f47d7c
documento: /home/ignac/qca-causal-cones/scripts/verify_weyl_dirac_gate.py ; último commit observado: 95f423f ; sha256 de la copia enviada 6c555cef8db0d8a7307a08e0251fa9278773aceeea8bf2bdb956ba2c3ca06597
documento: /home/ignac/qca-causal-cones/theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md ; último commit observado: 05eb1eb ; sha256 de la copia enviada 2ef8690e5eb4c4e0799ae6c38038b988d0fe7f7ea64fdcc596095d5bab257e26
documento: /home/ignac/qca-causal-cones/theory/STRICT_CONE_CEILING_N3_GATE.md ; último commit observado: 4135625 ; sha256 de la copia enviada aadaafb37d3e311fba39028699815f818322b02f9163661d1f96f30671b97827
entrada_astra.txt sha256 97eb26ed4348f2f89aef47512012e259286ded47b1e03a1355ec489b0de1f570
respuesta sha256 0fa14a7f6c28ac4f29b08eef267b21350fa887943c32f51b11e28920821ff481
-->

**Veredicto global: NO LISTO PARA CONGELAR.** La separación entre las dos extracciones es necesaria y la clase M4 es coherente, pero faltan convenciones esenciales para \(c_H\), el tratamiento de QM-3 y la justificación del método de clasificación. Además, una construcción exacta obtenida de los documentos adjuntos **refuta QM-1 para \(c_H\)** y proporciona testigos de ajustabilidad para ambas extracciones. Por tanto, algunas anticipaciones pueden sustituirse por resultados analíticos explícitos antes de congelar el charter.

**Supuestos de esta revisión.** Uso exclusivamente los siete documentos suministrados, sin ejecutar código ni verificar archivos, commits o revisiones citados. Sus estados históricos son declaraciones documentales, no comprobaciones independientes de esta sesión. Las conclusiones matemáticas nuevas que siguen incluyen su derivación. Mantengo las coordenadas, el paso temporal y la convención de Fourier declarados. No considero equivalentes los cambios de base dependientes de \(k\), salvo que el charter los incorpore expresamente.

| Anticipación | Evaluación |
|---|---|
| **C1** | Correcta para el acoplamiento estándar: su término de masa es on-site. Incorrecta como necesidad general. Más abajo exhibo un sector masivo admisible en M4 con \(T_0=0\). |
| **C2** | Schur y el conmutante \(I_2\otimes M_2(\mathbb C)\) son correctos. Debe sustituirse «no gap opens» por «no existe el par espectral masivo definido aquí». Reducibilidad y multiplicidad de una misma irrep tampoco son conceptos equivalentes en general. |
| **C3** | Correcta y demostrable directamente con el material adjunto. El término on-site no altera la unicidad del camino hacia un vértice extremo. La familia estándar tiene \(c_{\rm strict}^{\rm iso}=1/\sqrt3\) para \(0<m<1\). |
| **C4** | La continuidad propuesta no prueba nada a masa fija ni garantiza admisibilidad. Sin embargo, una familia explícita derivada del control estándar demuestra ajustabilidad para **ambas** extracciones. No es necesario conseguirla deformando el contraejemplo del documento 4. |
| **C5** | Sigue siendo una hipótesis estructural sin demostrar. En M4 pueden coexistir multiplicidad, masa y ajustabilidad; eso no prueba que la multiplicidad fuerce la ajustabilidad ni que ambas tengan un mecanismo universal común. |

### 1. Definiciones del sector, las extracciones y la masa

La definición espectral del nodo es razonable, pero necesita especificar que
\[
P=P_++P_-
\]
es la suma de los **proyectores espectrales completos** de los dos autovalores indicados, con
\[
\operatorname{rank}P_+=\operatorname{rank}P_-=r/2.
\]
Así, \(r\) es par: en M4, \(r=2\) o \(4\). Debe admitirse expresamente \(r=s\), con aislamiento del complemento vacuo.

En dimensión finita, el aislamiento en \(k_*\) permite continuar localmente el proyector conjunto \(P(k)\). No implica que cada rama dentro de un multiplete degenerado tenga una parametrización analítica conjunta en las tres componentes del momento.

La condición espectral debería escribirse como expansión local uniforme:
\[
(\omega_a(k_*+p)-\omega_*)^2
=M^2+c_{\omega^2}^2|p|^2+O(|p|^3),
\]
para todas las ramas del sector. La formulación mediante rayos es utilizable, pero debe declarar uniformidad angular o una condición equivalente sobre el desarrollo espectral.

Como \(M>0\), esta condición implica
\[
\omega_a-\omega_*=
\pm M\pm\frac{c_{\omega^2}^2}{2M}|p|^2+O(|p|^3).
\]
Por tanto, elimina todos los términos lineales de las fases. Exige algo más fuerte que eliminar una inclinación común: exige que todas las ramas tengan el mismo término cuadrático radial, con signos correlacionados con \(\pm M\). La covarianza \(D_2\) por sí sola no impone esa igualdad entre direcciones.

**La dificultad principal está en \(c_H\).** «\(H\) sobre el sector» no especifica cómo se identifican \(\operatorname{ran}P(k)\) y \(\operatorname{ran}P(k_*)\). A diferencia del caso sin masa, una base móvil puede cambiar el término lineal. Si
\[
V(p)=I+\sum_jp_jK_j+O(|p|^2),\qquad K_j^\dagger=-K_j,
\]
entonces
\[
V^\dagger HV
=M\beta+\sum_jp_j\bigl(\alpha_j+M[\beta,K_j]\bigr)+O(|p|^2).
\]
El espectro permanece idéntico, pero la norma usada para extraer \(c_H\) puede cambiar.

Una reparación concreta es definir el logaritmo espectral embebido en la base microscópica fija,
\[
H_P(k)=P(k)\,i\log(e^{i\omega_*}U(k))\,P(k),
\qquad
\alpha_j=P_*\partial_jH_P(k_*)P_*,
\]
con valores del logaritmo fijados en \(\pm M\). También sirve un transporte local especificado cuya conexión interna se anule en el nodo. Para \(P=I_4\), los ejemplos de esta revisión usan directamente la base microscópica fija y no presentan esta ambigüedad.

Además, la condición
\[
\frac1r\operatorname{tr}(\alpha_j\alpha_l)=c_H^2\delta_{jl}
\]
**no equivale al álgebra de Dirac**. Es ortogonalidad en norma de Hilbert–Schmidt. Por ejemplo,
\[
\beta=I\otimes\tau_z,\quad
\alpha_x=\sigma_x\otimes\tau_x,\quad
\alpha_y=\sigma_y\otimes\tau_y,\quad
\alpha_z=\sigma_z\otimes\tau_x
\]
satisfacen las condiciones escritas, con \(c_H=1\), pero
\[
\{\alpha_x,\alpha_y\}=-2\sigma_z\otimes\tau_z\ne0.
\]
Si se quiere llamar a la condición «forma de Dirac», hay que exigir
\[
\{\alpha_j,\alpha_l\}=2c_H^2\delta_{jl}I_P.
\]
Si se conserva el criterio de traza, debe presentarse como una extracción matricial más débil y cambiarse la interpretación de `NO_DIRAC_FORM`.

La distinción entre ambas extracciones sí está bien motivada. Para
\[
H=M\beta+A(p)+B(p,p)+O(|p|^3),
\]
se tiene
\[
H^2=M^2I+A(p)^2+M\{\beta,B(p,p)\}+O(|p|^3),
\]
cuando \(\{\beta,A\}=0\). El término cuadrático de \(H\) contribuye precisamente al coeficiente espectral que \(c_H\) no recoge.

**\(M\) es adecuado como semigap de cuasienergía**, con el intervalo y la rama declarados. No es automáticamente una masa inercial ni una masa física en unidades dimensionales. Las cantidades deben atribuirse a una tupla
\[
(U,k_*,\omega_*,P),
\]
no simplemente a \(U\): un mismo símbolo puede tener varios sectores y masas.

### 2. C1–C5 y una construcción que decide parte de las preguntas

**C2: alcance exacto de Schur.** En un nodo invariante,
\[
[U(k_*),R_g]=0.
\]
La irreducibilidad proyectiva compleja implica \(U(k_*)=\lambda I\). Eso impide tener los dos autovalores distintos necesarios para el sector masivo de §1. No impide que el espectro esté separado de una cuasienergía de referencia fijada externamente, ni demuestra por sí solo la existencia de un cono sin masa.

Para \(R_i=\sigma_i\otimes I_2\), expandir una matriz como
\[
X=I\otimes B_0+\sum_i\sigma_i\otimes B_i
\]
y exigir que conmute con las tres Pauli obliga a \(B_i=0\). Por tanto,
\[
\operatorname{Comm}(R)=I_2\otimes M_2(\mathbb C).
\]
Esto permite una separación espectral en el factor de multiplicidad; la dispersión admisible aún debe comprobarse.

**C3: el lema del vértice sí se aplica.** Escribiendo
\[
A(k)=\sum_h e^{-ik\cdot h}A_h,
\]
el símbolo estándar tiene
\[
T_h^{D}=n
\begin{pmatrix}
A_h&0\\
0&A_{-h}^{\dagger}
\end{pmatrix},
\qquad
T_0^D=
\begin{pmatrix}
0&imI\\
imI&0
\end{pmatrix}.
\]
Cada \(A_h\) tiene un autovalor no nulo, como puede comprobarse en la factorización y las identidades explícitas del documento 5. Para \(n>0\), cada \(T_h^D\) es no nilpotente.

Un camino que incorpora un paso \(0\) no puede alcanzar \(nh\) en \(n\) pasos cuando \(h\) es un vértice extremo del cubo. Sigue cumpliéndose
\[
(U^n)_{nh}=(T_h^D)^n\ne0.
\]
Por tanto,
\[
\operatorname{conv}(S_n/n)=C_{\rm micro},\qquad
c_{\rm strict}^{\rm iso}=\frac1{\sqrt3}.
\]
El extremo \(m=1\) queda excluido: allí desaparecen los saltos.

**Construcción explícita para C1, C4 y QM-1/QM-2.** Sea uno de los Weyl estándar tridimensionales,
\[
A(k)=u(k)I_2-i\,v(k)\cdot\sigma,
\]
con
\[
u^2+|v|^2=1,\quad
u(k)=1-\frac{|k|^2}{6}+O(|k|^3),\quad
v(k)=Lk+O(|k|^2),\quad L^TL=\frac13I.
\]
Estas identidades se obtienen directamente de las fórmulas del documento 5.

Uso provisionalmente el orden tensorial multiplicidad–espín; una permutación constante lo lleva al orden \(\sigma\otimes\tau\) de M4. Defino
\[
D_\eta(k)=
\begin{pmatrix}
\cos\eta\,A(k)&i\sin\eta\,I_2\\
i\sin\eta\,I_2&\cos\eta\,A(k)^\dagger
\end{pmatrix},
\]
y
\[
U_{\eta,t}(k)=
(e^{it\tau_x}\otimes I_2)D_\eta(k).
\]
Fijo
\[
0<M<\frac{\pi}{2},\qquad 0\le\eta\le M,\qquad t=M-\eta.
\]

La unitariedad sigue de la del acoplamiento estándar y de la rotación constante. Ambos factores son covariantes bajo \(I_2\otimes\sigma_i\). El soporte está contenido en \(N_3\cup\{0\}\).

En el origen,
\[
U_{\eta,t}(0)=e^{iM\tau_x}\otimes I_2,
\]
con semigap \(M\) y multiplicidades \(2+2\).

Su parte escalar es
\[
a(k)=\cos\eta\cos t\,u(k)-\sin\eta\sin t.
\]
El resto es \(i\) por una matriz hermítica cuyo cuadrado es \((1-a^2)I_4\). Así, sus fases son \(\pm\omega(k)\), cada una doble, y
\[
\cos\omega(k)=a(k).
\]
La expansión y el logaritmo dan, respectivamente,
\[
\boxed{
c_{\omega^2}^{\,2}
=\frac13\,\frac{M\cos\eta\cos t}{\sin M}},
\qquad
\boxed{
c_H=\frac1{\sqrt3}\,\frac{M\cos\eta}{\sin M}}.
\]
Los generadores lineales satisfacen incluso las relaciones completas de Clifford.

También puede comprobarse la diferencia por la segunda vía \(H^2\). Con \(\beta=-\tau_x\otimes I_2\), el coeficiente radial en la dirección de masa es
\[
b=\frac{\cos\eta}{6\sin M}
\left(\cos t-\frac{M\cos\eta}{\sin M}\right),
\]
y se verifica
\[
c_H^2+2Mb=c_{\omega^2}^{\,2}.
\]

Falta comprobar el cuerpo estricto, y aquí también hay una identidad exacta. Para los coeficientes Weyl,
\[
\operatorname{tr}A_h=\gamma_h\in
\left\{\frac{1-i}{4},\frac{1+i}{4}\right\},
\qquad
\overline{\operatorname{tr}A_{-h}}=\gamma_h.
\]
Los coeficientes de esquina de \(U_{\eta,t}\) satisfacen
\[
\operatorname{tr}T_h=2\cos\eta\cos t\,\gamma_h\ne0.
\]
Todos sobreviven bajo potencias. En toda esta familia,
\[
C_\infty^{\rm strict}=C_{\rm micro},
\qquad
c_{\rm strict}^{\rm iso}=\frac1{\sqrt3}.
\]

Tres consecuencias:

1. **Masa sin término on-site.** Para \(\eta=0,\ t=M\),
   \[
   U_{0,M}=(e^{iM\tau_x}\otimes I_2)
   \operatorname{diag}(A,A^\dagger).
   \]
   Tiene \(T_0=0\) y un nodo masivo admisible. Una rotación interna constante multiplicando al símbolo no es un coeficiente Fourier on-site añadido.

2. **Violación de QM-1 para \(H\).**
   \[
   c_H(U_{0,M})
   =\frac1{\sqrt3}\frac{M}{\sin M}
   >\frac1{\sqrt3}=c_{\rm strict}^{\rm iso}.
   \]
   La desigualdad es estricta porque \(\sin M<M\).

3. **Ajustabilidad de ambas extracciones.** Compárense, a igual \(M\),
   \[
   (\eta,t)=(M,0)
   \quad\text{y}\quad
   (\eta,t)=(M/2,M/2).
   \]
   Tienen el mismo cuerpo estricto completo, pero
   \[
   c_H^{\rm estándar}=\frac1{\sqrt3}M\cot M,
   \qquad
   c_H^{\rm simétrico}
   =\frac1{\sqrt3}\frac{M}{2\sin(M/2)},
   \]
   y
   \[
   (c_{\omega^2}^{\rm estándar})^2=\frac13M\cot M,
   \qquad
   (c_{\omega^2}^{\rm simétrico})^2
   =\frac13\frac M2\cot(M/2).
   \]
   Son distintos. Puede fijarse \(M=\pi/3\) para obtener dos símbolos concretos con coeficientes algebraicos.

Estas son derivaciones manuales de esta revisión, no ejecuciones de certificados ni promociones del estado del repositorio.

El argumento original de C4 sigue necesitando corrección: los dos dobletes del documento 4 tienen pendientes lineales no nulas alrededor de \(\pm\theta\). Agruparlos no produce un sector masivo admisible, pues aparecen términos lineales en \((\omega-\omega_*)^2\). Su separación espectral no es la masa definida en este charter.

### 3. Coherencia de la clase y efecto del término on-site

La declaración es coherente si se dice **soporte permitido** \(N_3\cup\{0\}\), con las ocho esquinas obligatoriamente activas. Si \(T_0=0\), el soporte efectivo es \(N_3\).

La covarianza en \(h=0\) exige
\[
[T_0,R_g]=0.
\]
Por tanto, «\(T_0\) libre» significa libre sujeto a covarianza y unitariedad. En M4,
\[
T_0=I_2\otimes B;
\]
en el control Pauli \(s=2\), \(T_0\) debe ser escalar. No es una matriz arbitraria.

Añadir la posibilidad on-site conserva
\[
C_{\rm micro}=[-1/\sqrt3,1/\sqrt3]^3,
\]
pero amplía la clase de símbolos y cambia las ecuaciones de unitariedad, incluidos los términos cruzados con \(T_0\). **No conserva automáticamente \(S_n\), \(h_\infty\) ni \(c_{\rm strict}^{\rm iso}\).**

El lema del vértice sigue siendo suficiente. La nilpotencia de algún vértice sigue sin demostrar por sí sola una pérdida de saturación.

Debe declararse también que no se exige irreducibilidad dinámica. El documento 4 la demuestra para su ejemplo, pero eso no la convierte en una condición de M4.

### 4. QM-0..QM-3, resultados y secuencia

La secuencia es un programa de investigación con salida `OPEN`, no un procedimiento cuya terminación decisoria esté justificada.

- **QM-0:** la familia estándar ya proporciona existencia en M4. La etapa de controles puede certificarla; no es necesario esperar a una nueva construcción en (b). Schur solo decide la inexistencia en los nodos invariantes del control \(s=2\), no en todos sus nodos.
- **QM-1:** la construcción anterior proporciona un testigo de violación para \(H\). Para \(\omega^2\), esta revisión no aporta prueba general ni contraejemplo.
- **QM-2:** los dos símbolos anteriores satisfacen el criterio literal de ajustabilidad para ambas extracciones.
- **QM-3:** tiene resultados previstos en la tabla, pero ninguna etapa asignada a estudiarla. Falta además definir «familia admisible».

**Sí, basta un testigo explícito**, entendido como un par de símbolos exactos con todos los requisitos certificados. No hace falta una clasificación ni una deformación continua. Un símbolo aislado solo basta si se acompaña de otro comparador ya certificado.

Hay, sin embargo, una asimetría lógica en QM-2. La negación de
\[
c_X/c_{\rm strict}^{\rm iso}=f_X(M)
\]
requiere dos tuplas con igual \(M\) y cocientes distintos; no exige que sus valores de \(c_{\rm strict}^{\rm iso}\) coincidan. El testigo declarado impone esa condición adicional. Es suficiente, pero no es la negación exhaustiva del resultado `FORCED`. Conviene separar «dependencia no determinada por \(M\)» de «ajustabilidad a igual límite estricto».

También debe justificarse la positividad del denominador para todos los sectores admitidos. El documento 7 no la proporciona directamente para esta clase masiva.

**QM-3 debe comparar con \(c_0(U_0)\).** Comparar con \(c_{\rm strict}^{\rm iso}\) introduciría la igualdad sin masa que el documento 4 refuta. Pero deben seguirse el nodo, la fase y el sector:
\[
k_*(\mu)\to k_*(0),\qquad
\omega_*(\mu)\to\omega_*(0),\qquad
P_\mu\to P_0.
\]
Hace falta fijar una convergencia de coeficientes, mantener aislamiento del sector conjunto frente al complemento en el límite y especificar qué cono de \(U_0\) se recupera.

Con soporte finito fijo, la convergencia de coeficientes controla las derivadas en \(k\). Si además el logaritmo sectorial tiene un segundo desarrollo uniformemente controlado, la identidad de \(H^2\) explica por qué la diferencia entre las extracciones puede desaparecer al multiplicarse la corrección por \(M\). Esas condiciones no están actualmente formuladas.

Por último, Gröbner puede tratar las identidades polinómicas de unitariedad, pero no constituye por sí solo un método completo para fases desempaquetadas, logaritmos, desigualdades reales, aislamiento espectral y soporte asintótico. Hace falta separar la parte algebraica de las obligaciones analíticas.

### 5. QM-1 y el alcance de la cota sin masa

QM-1 tiene sentido como pregunta nueva, pero **no como consecuencia del documento 7**. Cambian al menos tres hipótesis: masa no nula, posibilidad de término on-site y admisión de nodos distintos del origen.

Para un cono sin masa, \(c_0\) es una pendiente espectral real. En un nodo masivo admitido,
\[
\nabla\omega(k_*)=0.
\]
Ni \(c_H\) ni \(c_{\omega^2}\) son esa pendiente.

Una cota sobre velocidades de grupo tampoco acota automáticamente la curvatura:
\[
\omega(p)=M+\frac{c_{\omega^2}^2}{2M}p^2+\cdots.
\]
El comportamiento infinitesimal no permite identificar \(c_{\omega^2}\) con una velocidad alcanzada por alguna rama.

Para \(H\), la construcción anterior muestra que **la cota propuesta es falsa incluso con álgebra de Clifford exacta y cuerpo estricto saturado**. No hay una extensión general que pueda probarse bajo los cuantificadores actuales.

Para \(\omega^2\), haría falta un nuevo argumento que controle la curvatura de las fases mediante el soporte exacto, o hipótesis adicionales que relacionen esa curvatura local con pendientes espectrales realizables. La coincidencia en la familia estándar no basta.

### 6. Alcance y relación con la pregunta A

Los límites de §5 son adecuados, pero la apertura excede ligeramente los objetos definidos:

- «Effective light speed» sugiere una velocidad característica única; a masa finita aquí se estudian dos coeficientes diferentes.
- «Function of its mass alone» no coincide con QM-2, que pregunta por el cociente respecto a \(c_{\rm strict}^{\rm iso}\).
- «Same causal limit» puede entenderse como igualdad de cuerpos; el testigo requerido solo fija el mínimo de sus funciones soporte.
- «Every admissible family» promete un dominio todavía sin definir para QM-3.

El alcance correcto es: **dependencia de dos coeficientes locales de sectores masivos entre símbolos de M4, con unidades y comparador causal explícitos**.

Dos dinámicas con velocidades distintas no son dos especies coexistentes en una misma dinámica. Tampoco una función universal de \(M\) daría igualdad de velocidades entre especies de masas distintas. Los resultados pueden informar la pregunta A, pero no decidirla.

Las frases históricas sobre verificadores y revisiones deben conservar su carácter documental. Esta revisión no sustituye ni acredita la revisión por Grok registrada como decisión D4.

### Reparaciones obligatorias

| ID | Ubicación | Gravedad | Reparación |
|---|---|---|---|
| **A-M-01** | §1, nodo y notación de §3 | **Laguna** | Definir proyectores completos \(P_\pm\), rango par, caso \(r=s\), continuación local y expansión uniforme. Cuantificar sobre tuplas, no solo símbolos. |
| **A-M-02** | §1, \(c_H\) | **Laguna bloqueante** | Fijar la identificación de fibras y el logaritmo. Excluir cambios de base dependientes de \(k\) no declarados; fijar también la raíz no negativa y el tratamiento de \(c_H=0\). |
| **A-M-03** | §1, `NO_DIRAC_FORM` | **Error demostrado de identificación** | La condición de traza no implica forma de Dirac. Añadir Clifford o renombrar y limitar la extracción. Aplicar la exclusión de \(H\) también a QM-1. |
| **A-M-04** | §0 C1; §4(a) | **Error demostrado si se afirma necesidad** | Limitar C1 al acoplamiento estándar. Incorporar como control la construcción masiva \(U_{0,M}\) con \(T_0=0\). |
| **A-M-05** | §0 C2; control de §4(a) | **Redacción con efecto lógico** | Sustituir «no gap» por ausencia del par masivo definido. Separar reducibilidad general de multiplicidad isótípica. No extender el control a nodos no invariantes. |
| **A-M-06** | §0 C3 | **Laguna subsanada analíticamente aquí** | Incorporar los coeficientes masivos por bloques y la prueba de supervivencia de vértices. Retener \(m<1\). |
| **A-M-07** | §0 C4–C5 | **Laguna** | Retirar la continuidad como argumento de ajustabilidad a masa fija. Incorporar el testigo explícito o mantener la anticipación sin inferencia; conservar C5 como hipótesis. |
| **A-M-08** | §2, clase | **Redacción** | Distinguir soporte permitido y efectivo; expresar \(T_0\) libre sujeto a conmutante y unitariedad; declarar ausencia de requisito de irreducibilidad dinámica. |
| **A-M-09** | §3 QM-1; §4(c) | **Error demostrado para la cota \(H\)** | Registrar el contraejemplo \(c_H=M/(\sqrt3\sin M)>c_{\rm strict}^{\rm iso}\). Separar completamente el problema pendiente para \(\omega^2\). |
| **A-M-10** | §3 QM-2 | **Laguna lógica** | Justificar denominadores positivos; distinguir falsificación de dependencia normalizada y ajustabilidad a igual \(c_{\rm strict}^{\rm iso}\). No identificar igualdad del escalar con igualdad del cuerpo. |
| **A-M-11** | §3 QM-3; §4 | **Laguna bloqueante** | Definir familias, seguimiento de sectores, convergencia y aislamiento en el límite; asignar una etapa y un criterio de cierre a QM-3. Mantener \(c_0(U_0)\) como comparador. |
| **A-M-12** | §4(c) | **Laguna metodológica** | Delimitar qué resuelve Gröbner y qué requiere pruebas analíticas, desigualdades reales y argumentos de soporte asintótico. No prometer decisión completa. |
| **A-M-13** | §0, pregunta física; §5 | **Redacción de alcance** | Hablar de coeficientes locales especificados y de comparación entre dinámicas. Mantener explícitamente fuera la universalidad entre especies A. |