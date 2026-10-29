<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-29T10:32:52Z  fin: 2026-10-29T10:40:02Z
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: e117d2e ; sha256 de la copia enviada 6c7594a90c4eb1e24cd47338bbe49059144cb72e63cfc04b274adbfba0b209f5
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-charter-draft-review-astra/informe_astra.md ; último commit observado: 3f0d9aa ; sha256 de la copia enviada ceedc86d1ac4fd8bd103465e2d7d07c23bb31728e4c3d3f64825997a4e7a02f4
documento: /home/ignac/qca-causal-cones/theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md ; último commit observado: 05eb1eb ; sha256 de la copia enviada 2ef8690e5eb4c4e0799ae6c38038b988d0fe7f7ea64fdcc596095d5bab257e26
documento: /home/ignac/qca-causal-cones/theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md ; último commit observado: 88b07ed ; sha256 de la copia enviada bb12375faff7b16fcd5e40c85995dc9fe8f374f6d26b51c60819fa94bba176a6
documento: /home/ignac/qca-causal-cones/theory/STRICT_CONE_CEILING_N3_GATE.md ; último commit observado: 4135625 ; sha256 de la copia enviada aadaafb37d3e311fba39028699815f818322b02f9163661d1f96f30671b97827
documento: /home/ignac/qca-causal-cones/reports/2026-09-14--massless-rigidity-source-audit.md ; último commit observado: 5845eda ; sha256 de la copia enviada 468918501dd6bf84603cf78c201cb956ef11352c09506c98d3eb2c2999b05e72
documento: /home/ignac/qca-causal-cones/biblioteca/1708.00826v2.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_astra.txt sha256 f7bcfc6a7d76924894330bf78749388b9cc78b8b5704fdee1b35edc4cb567151
respuesta sha256 4611164aec406c22fce81d81c5f1e5a5795710253b20f9f80588f7252889141a
-->

**Veredicto global: NOT_READY.** La v2 corrige los errores de la cara y de la inclusión de \(O\) en la familia particionada. La nueva familia F es matemáticamente legítima, pero faltan convenciones para sus clases y para Q-a. Además, el Paso 0.4 omite una hipótesis esencial del Documento 5: la covarianza bajo las medias vueltas coordenadas \(D_2\). Las salidas tampoco contemplan íntegramente qué hacer si esa cota no resulta aplicable.

Uso exclusivamente los documentos suministrados. Las comprobaciones siguientes son derivaciones manuales; no certifican archivos, hashes ni ejecuciones. El Documento 5 contiene **un contrato**, no la demostración posterior de la cota. Ese resultado histórico y los certificados no adjuntos quedan **[UNVERIFIED]**. Las referencias a P17 se comprueban contra el texto extraído, no contra el PDF.

## 1. Reparaciones A-R1-01 a A-R1-14

| Reparación | Veredicto sobre v2 | Ubicación y observación |
|---|---|---|
| **A-R1-01** | **Resuelta**, salvo adaptación formal a F | Secs. 1–2: todos los nodos, sector completo, rama local, red BCC y dominio real. En F, \(S_\pm\) sigue apareciendo indebidamente en la tupla general. |
| **A-R1-02** | **Resuelta** | Sec. 1: normalización \(1/\sqrt3\), escalado de ambas velocidades y valor \(1\) en coordenadas no normalizadas. |
| **A-R1-03** | **Resuelta para P** | Sec. 2: se reconoce expresamente que P es una restricción del marco de P17; se define el núcleo proyectivo. F necesita su propio dominio para Eq. (2). |
| **A-R1-04** | **Resuelta mediante ampliación explícita** | Sec. 2 y Paso 0.2: \(O\) pertenece ahora a F; no se introduce como estabilizador de una partición imposible. |
| **A-R1-05** | **Resuelta** | Sec. 0: desplazamiento tangencial \((0,2,2)\), con la identidad normal corregida. Cálculo abajo. |
| **A-R1-06** | **Resuelta sustancialmente** | Sec. 0 y Paso 0: verificar o refutar; separación retrospectiva/prospectiva; precisión \(Q_8\). A4 queda cubierta geométricamente por 0′, aunque conviene asignarle expresamente allí su salida. |
| **A-R1-07** | **Resuelta para P; parcial para F** | Sec. 2 y Paso 0′: equivalencia proyectiva, representaciones reducibles y exhaustividad. La identificación de clases aún utiliza \((G,S_\pm,R)\) también donde no existe partición. |
| **A-R1-08** | **Resuelta como obligación contractual** | Paso 4a: transporte, conjugación de coeficientes, intercambio \(h_1\leftrightarrow h_4\), comprobación posterior de covarianza. Las leyes pendientes son coherentes y se detallan abajo. |
| **A-R1-09** | **Resuelta como protocolo de factibilidad** | Sec. 2 y Paso 4b-1: variables reales, soporte activo, certificado real y distinción entre componentes complejas y reales. Un testigo de existencia no certifica cobertura universal. |
| **A-R1-10** | **Parcial** | Sec. 5: separa preguntas y añade salidas necesarias. Persisten problemas de etapa de cierre, dominio de Q-a y cuantificación de la salida de saturación. |
| **A-R1-11** | **Parcial** | Predecesores y Paso 0.4: reconoce el problema de los nodos, pero omite la hipótesis \(D_2\) del Documento 5. Tampoco adjunta la demostración de la cota. |
| **A-R1-12** | **Resuelta en el texto suministrado** | Fuente primaria inicial: distingue nota [23] de referencia inédita [31] y separa los localizadores. El Documento 6 conserva la atribución antigua incorrecta. |
| **A-R1-13** | **Resuelta** | Sec. 4: presupuesto previo por etapa, alcance, entregable, cierre y paradas. El agotamiento no produce rigidez. |
| **A-R1-14** | **Resuelta como procedimiento** | Sec. 6 y Paso 0′: revisión previa de exhaustividad, ronda limitada, objeciones, cambios posteriores y procedencia. Su cumplimiento efectivo no está certificado aquí. |

## 2. Familia F: definición, transitividad y solapamientos

### Grupos transitivos sobre los ocho vértices

Tomo \(D_4\) como grupo diedral **de orden ocho**, realizado mediante rotaciones propias. Alrededor del eje \(z\), sean

\[
r(x,y,z)=(-y,x,z),\qquad s(x,y,z)=(x,-y,-z).
\]

Cumplen

\[
r^4=s^2=e,\qquad srs=r^{-1}.
\]

La órbita de \((1,1,1)\) bajo \(\langle r\rangle\) contiene los cuatro vértices con \(z=1\). La aplicación de \(s\) proporciona los cuatro con \(z=-1\). Por tanto, **este \(D_4\) sí es transitivo**, y su acción es regular.

La enumeración de F puede cerrarse a mano. Si \(H\le O\) es transitivo sobre ocho vértices, órbita-estabilizador y Lagrange dan

\[
8\mid |H|,\qquad |H|\mid24,
\]

de modo que \(|H|=8\) o \(24\). En el segundo caso \(H=O\). En el primero es un Sylow 2, y todos son conjugados al \(D_4\) anterior. Así, **hasta conjugación en \(O\), F contiene exactamente los grupos \(D_4\) y \(O\)**. Esto enumera grupos espaciales, no sus representaciones ni sus símbolos unitarios.

Como comprobación adicional, el \(D_4\) exhibido contiene el subgrupo

\[
V_4=\{e,r^2,s,r^2s\},
\]

formado por las tres medias vueltas coordenadas y la identidad.

### Compatibilidad con P

Las tres posibilidades geométricas anticipadas para P son correctas:

\[
(V_4,\text{tetraedro}),\qquad
(T,\text{tetraedro}),\qquad
(C_4,\text{cara}).
\]

Los ocho conjuntos «vértice más sus tres vecinos» no admiten transitividad: el vértice central tiene tres vecinos dentro del conjunto y cada vértice restante tiene uno. Esta propiedad se conserva bajo las rotaciones.

F es compatible con la ecuación de covarianza declarada. Para matrices ortogonales,

\[
U(gk)
=\sum_h e^{-ik\cdot h}T_{gh}
=R_gU(k)R_g^\dagger.
\]

No hace falta introducir reflexiones ni antiunitarias como simetrías.

Sin embargo, **P y F no son familias disjuntas de símbolos**. Todo grupo de F contiene el \(V_4\) coordenado. Al restringir \(R\) a ese subgrupo, cualquier símbolo de F satisface una clase P con partición tetraédrica. Además, un símbolo \(D_4\)-covariante se restringe al \(C_4\) que preserva una cara.

Por consiguiente:

- F añade clases con una declaración de simetría más fuerte.
- **No amplía la unión de símbolos ya admitida por P**, puesto que P incluye todas las representaciones bidimensionales de \(V_4\), también reducibles.
- Un mismo símbolo puede aparecer en varias filas. Esas filas no cuentan como ejemplos independientes.

No hay contradicción lógica si se respetan las inclusiones. Una prueba universal en una clase P se aplica a sus subclases F; un contraejemplo en F también es uno en la correspondiente clase P. La implicación inversa no vale.

### Dos convenciones que faltan

La identificación de clases debe distinguir

\[
(P,G,S_\pm,[R]),\qquad (F,G,[R]).
\]

Actualmente, Secs. 1–2 siguen usando \(S_\pm\) para F.

También falta definir Q-a en F. La Eq. (2) de P17 cuantifica sobre \(h\in S_+\). Una extensión natural y compatible con P17 p.3 es tomar, **solo para interpretar esa ecuación**,

\[
S_+=S_-=N_3
\]

y exigirla para todo \(h\in N_3\). Esto no introduce una partición, pero debe declararse. Sin esa convención, Q-a no tiene un dominio definido en F.

### Representación escalar sobre un subgrupo transitivo

Si \(K\le G\) actúa transitivamente y \(R_k\) es escalar para todo \(k\in K\), entonces

\[
T_{kh}=R_kT_hR_k^\dagger=T_h,
\]

por lo que los ocho coeficientes son una misma matriz \(A\).

La identidad de desplazamiento cero exige

\[
8A^\dagger A=I.
\]

El desplazamiento en etiquetas \(\varepsilon\),

\[
\ell=(2,2,2),
\]

tiene una única pareja: \((-1,-1,-1)\to(1,1,1)\). Su identidad exige

\[
A^\dagger A=0.
\]

Contradicción. **La clase es vacía**, para cualquier dimensión interna.

Como segunda comprobación,

\[
U(k)=8\prod_{j=1}^3\cos(k_j/\sqrt3)\,A
\]

se anula para ciertos momentos, y no puede ser unitario.

## 3. Anticipaciones: cara tangencial y \(Q_8\)

### A1 para una cara

Sea \(S_+=\{(1,y,z):y,z=\pm1\}\), con coeficientes \(A\) en \(S_+\) y \(B\) en \(-S_+\). Para \(\ell=(0,2,2)\), las únicas parejas son

\[
(1,-1,-1)\to(1,1,1),\qquad
(-1,-1,-1)\to(-1,1,1).
\]

La primera permanece en \(S_+\), la segunda en \(S_-\). Luego

\[
A^\dagger A+B^\dagger B=0,
\]

mientras que el desplazamiento cero da

\[
4(A^\dagger A+B^\dagger B)=I.
\]

La corrección es exacta. El desplazamiento normal \((2,0,0)\) da, en cambio,

\[
4B^\dagger A=0.
\]

Para el tetraedro definido por \(\varepsilon_x\varepsilon_y\varepsilon_z=1\), las dos parejas del desplazamiento tangencial anterior también permanecen respectivamente en las dos mitades, y producen la misma contradicción.

### A2 y su alcance

La acción de \(S_4\) sobre las tres particiones de cuatro objetos en dos parejas define

\[
S_4\longrightarrow S_3
\]

con núcleo \(V_4\). La representación estándar bidimensional de \(S_3\) es fiel. Su composición define la representación \(E\) de \(O\simeq S_4\), con

\[
E(v)=I_2\quad(v\in V_4).
\]

En el recubrimiento \(2O\to O\), la preimagen de ese \(V_4\) es

\[
Q_8=\{\pm I,\pm i\sigma_x,\pm i\sigma_y,\pm i\sigma_z\}.
\]

Por tanto, la representación lineal \(E\) de \(2O\) tiene núcleo \(Q_8\). **La precisión introducida en v2 es correcta.** Bajo cambios de fase proyectivos, la formulación invariante es que ese subgrupo actúa escalarmente.

Hay una distinción importante para Paso 0.2:

- \(V_4\) no es transitivo sobre los ocho vértices; tiene dos órbitas tetraédricas.
- Por tanto, \(E\) bajo \(O\) o \(D_4\) no obliga por este argumento a que los ocho coeficientes sean iguales.
- Sí obliga a que sean \(A\) y \(B\) en los dos tetraedros. **A1 basta entonces para demostrar vaciedad**.

Además,

\[
D_4/V_4\simeq C_2,\qquad E|_{D_4}\simeq 1\oplus\chi,
\]

donde \(\chi\) es el carácter no trivial de ese cociente. Esto confirma que la enumeración debe incluir restricciones reducibles.

A3 también es correcta: para un soporte escalar finito con al menos dos exponentes, una forma lineal genérica selecciona máximo y mínimo únicos. El coeficiente de su diferencia en \(p\,p^*\) es un único producto no nulo, incompatible con \(p\,p^*=1\). A4 es correcta únicamente como afirmación geométrica.

## 4. Unidades, red y valor basal

La red física es

\[
\Lambda=\frac1{\sqrt3}
\{m\in\mathbb Z^3:m_1\equiv m_2\equiv m_3\pmod2\}.
\]

Los generadores producen \((2,0,0)\), \((0,2,0)\), \((0,0,2)\) y \((1,1,1)\) en coordenadas \(\varepsilon\). Estos generan exactamente los puntos de paridad común. La identificación BCC es correcta.

Con la convención \(e^{-ik\cdot h}\), su red recíproca es

\[
\Lambda^*
=\pi\sqrt3\{m\in\mathbb Z^3:m_1+m_2+m_3\text{ es par}\},
\]

y el toro es \(\mathbb R^3/\Lambda^*\). Esta expresión eliminaría cualquier duda sobre qué significa «dual cell».

El cuerpo microscópico tiene función soporte

\[
h_{\rm micro}(q)
=\frac{|q_x|+|q_y|+|q_z|}{\sqrt3}.
\]

Para \(\|q\|_2=1\), el mínimo es \(1/\sqrt3\), alcanzado en los ejes. Así,

\[
\rho_{\rm micro}=1/\sqrt3.
\]

Al sustituir \(h=\varepsilon/\sqrt3\) por \(h'=\varepsilon\),

\[
U_{\rm nuevo}(k)=U_{\rm anterior}(\sqrt3\,k),
\]

y tanto \(c_0\) como \(c_{\rm strict}^{\rm iso}\) se multiplican por \(\sqrt3\). **La normalización y el valor basal declarado son coherentes.**

Esto comprueba geometría y escalado; no reemplaza la verificación del certificado basal histórico, que no está adjunto.

## 5. Paso 0.4 y alcance de la cota general

La cautela respecto a \(k_\star\ne0\) es correcta, pero el examen propuesto está incompleto.

El Documento 5 exige simultáneamente:

1. soporte normalizado \(N_3\);
2. covarianza bajo el \(D_2=V_4\) de medias vueltas coordenadas;
3. nodo en \(0\);
4. las restantes condiciones espectrales y de admisión.

Respecto al grupo:

- P con \(V_4\) o \(T\), y F con \(D_4\) u \(O\), admiten restricción al \(D_2\) requerido.
- **P con \(C_4\) sobre una cara no contiene ese \(D_2\)**. La cota congelada no cubre automáticamente esa clase, ni siquiera en \(k_\star=0\).
- Que un símbolo \(C_4\)-covariante tenga simetrías adicionales debe demostrarse; no se deduce del nombre de su clase.

Para mover un nodo, sea

\[
V(k)=U(k+k_\star),\qquad
T'_h=e^{-ik_\star\cdot h}T_h.
\]

Sus potencias cumplen

\[
V(k)^n=U(k+k_\star)^n,
\]

de modo que cada coeficiente en \(x\) adquiere el factor no nulo \(e^{-ik_\star\cdot x}\). Por tanto, conserva \(S_n\), el cuerpo estricto y la pendiente local.

Pero conservar la covarianza con el mismo \(R\) exige

\[
e^{-ik_\star\cdot gh}T_{gh}
=e^{-ik_\star\cdot h}T_{gh}.
\]

Como todos los coeficientes son activos, equivale a

\[
k_\star\cdot(gh-h)\in2\pi\mathbb Z
\quad\text{para todo }g,h,
\]

o, equivalentemente,

\[
g^{-1}k_\star-k_\star\in\Lambda^*.
\]

Para aplicar el Documento 5 **basta comprobar esto para su \(D_2\)**. No hace falta conservar toda la simetría \(G\) original. También podría existir otra representación que haga \(V\) covariante, pero habría que construirla.

Así, la cota congelada alcanza nodos distintos de cero cuando se demuestra un transporte hacia un símbolo que satisfaga **todas** sus hipótesis. El Documento 5, por sí solo, no afirma cobertura de todos los nodos.

Finalmente, puede que la demostración posterior no utilice realmente la simetría \(D_2\), y permita una extensión mayor. **[UNVERIFIED]**: esa demostración no está suministrada. No se puede ampliar un teorema leyendo solamente su contrato.

## 6. Transporte y derivación algebraica real

### Leyes de transporte

Si \(C_x^{(n)}\) denota el coeficiente de \(U^n\), las leyes pertinentes son:

| Operación | Efecto sobre \(S_n\) | Nodo y pendiente |
|---|---|---|
| \(U'=WUW^\dagger\) | \(S'_n=S_n\) | Mismo nodo y \(c_0\); transportar \(R\) a \(WRW^\dagger\). |
| \(U'=e^{i\phi}U\) | \(S'_n=S_n\) | \(\omega'_\star=\omega_\star-\phi\); mismo \(c_0\). |
| \(U'(k)=U(k+a)\) | \(S'_n=S_n\) | \(k'_\star=k_\star-a\); mismo \(c_0\); comprobar covarianza. |
| \(U'(k)=U(-k)\) | \(S'_n=-S_n\) | \(k'_\star=-k_\star\); mismo \(c_0\). |
| \(U'(k)=U(Q^{-1}k)\) | \(S'_n=QS_n\) | \(k'_\star=Qk_\star\); mismo \(c_0\) si \(Q\) es ortogonal. |
| \(T'_h=\overline{T_h}\) | \(S'_n=S_n\) | \((k'_\star,\omega'_\star)=(-k_\star,-\omega_\star)\); mismo \(c_0\). |

Para la última fila,

\[
U'(k)=\overline{U(-k)},\qquad
C_x'{}^{(n)}=\overline{C_x^{(n)}},\qquad
R'_g=\overline{R_g}.
\]

La conjugación cambia también el multiplicador proyectivo a su conjugado. No se puede conservar sin comprobación una fila representacional concreta.

Si originalmente

\[
\omega_\pm(k_\star+p)-\omega_\star
=\pm c_0|p|+O(|p|^2),
\]

entonces las fases transformadas son \(-\omega_\pm(k_\star-p)\). Sus pendientes son las mismas con las ramas intercambiadas. No aparece una inversión de \(S_n\): esa sería otra operación.

Para cualquier transformación ortogonal \(Q\),

\[
h'_\infty(q)=h_\infty(Q^Tq),
\]

por lo que el mínimo esférico permanece igual, aunque cambie el cuerpo.

### Intercambio \(h_1\leftrightarrow h_4\)

Elijo el etiquetado tetraédrico, en coordenadas \(\varepsilon\),

\[
h_1=(1,1,1),\quad h_2=(1,-1,-1),\quad
h_3=(-1,1,-1),\quad h_4=(-1,-1,1).
\]

La transformación

\[
M(x,y,z)=(-y,-x,z)
\]

intercambia \(h_1,h_4\), fija \(h_2,h_3\), y satisface

\[
M^TM=I,\qquad\det M=-1.
\]

Es una reflexión que preserva el cubo y la red. El intercambio incluye necesariamente

\[
-h_1\leftrightarrow-h_4.
\]

Entonces

\[
U'(k)=U(M^Tk),\qquad S'_n=MS_n,
\]

y las dos velocidades se conservan. La representación se transporta mediante

\[
G'=MGM^{-1},\qquad
R'_{MgM^{-1}}=R_g.
\]

Como \(M\) normaliza el grupo de rotaciones del cubo, \(G'\le O\). Permitir este transporte no exige que \(M\) sea una simetría del símbolo.

El intercambio de P17 p.7 viene acompañado de una conjugación interna constante. Ambas operaciones tienen leyes válidas. Falta, en la ejecución futura, identificar su etiquetado con el empleado en cada certificado.

**Límite de 4a:** transportar un certificado de un nodo solo certifica los nodos transportados. La clasificación de los símbolos no demuestra que todos sus nodos estén en esas órbitas. Sec. 0 debe conservar este límite, y 4b-2 debe cubrir los restantes.

### Soporte activo y existencia real

Para cada matriz, defínase

\[
d_h=\|T_h\|_F^2
=\sum_{a,b}\bigl((\Re T_{h,ab})^2+(\Im T_{h,ab})^2\bigr).
\]

El soporte activo equivale a \(d_h>0\). Una codificación puramente ecuacional válida sobre los reales es añadir una variable \(y\) y

\[
y\prod_h d_h-1=0.
\]

Esto evita admitir componentes que solo existen con coeficientes nulos.

Las identidades de unitariedad son polinomiales reales; la covarianza también lo es cuando se ha fijado un representante exacto de \(R\). El campo de cálculo debe tener una interpretación real especificada para sus constantes algebraicas.

Un certificado real de vaciedad puede tener, para el sistema ecuacional aumentado \(f_i=0\), la forma

\[
-1=\sum_i a_i f_i+\sum_j b_j^2.
\]

Evaluarlo en una supuesta solución real da la contradicción \(-1\ge0\). Un certificado Positivstellensatz que trate directamente desigualdades también sirve.

Las condiciones son:

- verificar exactamente la identidad;
- incorporar soporte activo y todas las demás restricciones pertinentes;
- no interpretar el fracaso de una búsqueda SOS de grado limitado como existencia;
- no interpretar una aproximación numérica como certificado exacto.

Un punto real explícito prueba existencia. No demuestra que las demás componentes sean reales, que tengan conos, ni que satisfagan una propiedad universal.

Para Q-a, la violación correspondiente a un par que mueve \(h\) puede expresarse como

\[
\|[R_g,T_h]\|_F^2=0.
\]

La implicación universal requiere excluir todas esas posibilidades dentro del dominio elegido. Un testigo de refutación debe pertenecer a ese mismo dominio.

### Admisibilidad de nodos

También puede formularse algebraicamente usando variables de círculo para los momentos en una base primitiva de la BCC. En dimensión interna dos, un nodo completo cumple

\[
U(k_\star)=aI,\qquad |a|=1.
\]

Sean

\[
H_j=i\overline a\,\partial_{k_j}U(k_\star).
\]

Son hermíticas por unitariedad. La condición de cono isotrópico sin inclinación equivale a

\[
\operatorname{tr}H_j=0,\qquad
\frac12\operatorname{tr}(H_jH_\ell)=c_0^2\delta_{j\ell},
\qquad c_0>0.
\]

En efecto, escribiendo \(H_j=v_j\cdot\sigma\), esas ecuaciones hacen que los \(v_j\) sean ortogonales y de longitud \(c_0\); las pendientes de \(\sum_jp_jH_j\) son \(\pm c_0|p|\).

Esto muestra que un tratamiento real exacto de la existencia de nodos es viable en principio. No garantiza un coste manejable ni resuelve el problema asintótico del cuerpo estricto.

La condición de rango uno usada en 4b-2 también se justifica sin Eq. (2): el desplazamiento \(2h\) tiene una única pareja antipodal, y las identidades de unitariedad obligan a productos nulos entre dos matrices no nulas. En dimensión dos, ambas tienen rango uno. Para ellas,

\[
T_h^2=(\operatorname{tr}T_h)T_h,
\]

de modo que no nilpotencia equivale a \(\operatorname{tr}T_h\ne0\). La alternativa con vértices nilpotentes sigue necesitando una demostración específica del cuerpo estricto.

## 7. Salidas, presupuesto, paradas y revisión

Hay tres problemas lógicos en Sec. 5.

**Primero, el contraejemplo se define demasiado estrechamente.** La pregunta principal es una igualdad, pero solo se admite como refutación

\[
0<c_0<c_{\rm strict}^{\rm iso}.
\]

Si el Paso 0.4 permite abandonar el uso de la cota para ciertas clases o nodos, también debe permitir registrar

\[
c_0>c_{\rm strict}^{\rm iso}.
\]

No estoy afirmando que exista tal símbolo. La laguna es que el contrato deja de asumir la premisa que justificaba excluir esa posibilidad, pero conserva la exclusión en sus salidas. Debe definir el contraejemplo mediante \(c_0\ne c_{\rm strict}^{\rm iso}\), indicando después el sentido, o condicionar expresamente la dicotomía a una cota ya certificada.

**Segundo, la etapa de cierre de la clasificación está mal asignada.** `EMPTY_CLASS` y existencia de símbolos unitarios pueden decidirse en 4b-1. En cambio, `NO_ADMISSIBLE_SECTOR` y `NONEMPTY_WITH_ADMISSIBLE_SECTORS` requieren análisis de nodos, situado en 4b-2.

Esto afecta a Q-a. «Todo miembro admisible» en Sec. 1 puede significar que posee un cono admitido; 4b-1 solo impone las restricciones sobre coeficientes. Hay que escoger:

- Q-a sobre todos los símbolos unitarios de la clase; o
- Q-a sobre los símbolos con al menos un nodo admisible.

Una refutación por un símbolo sin cono no decide la segunda pregunta.

**Tercero, falta cuantificar la salida de saturación.** `RIGIDITY_HOLDS_SATURATION_FAILS` figura «por clase», pero no dice si existe un miembro con fallo de saturación o si fallan todos. Conviene separar:

\[
\text{rigidez universal en la clase}
\]

de

\[
\exists U\text{ admisible con }c_{\rm strict}^{\rm iso}(U)<\rho_{\rm micro},
\]

o declarar expresamente otra cuantificación. Un testigo individual no debe recibir una etiqueta que parezca una clasificación universal.

Los presupuestos y las paradas son adecuados para un contrato previo. No es necesario garantizar que Gröbner, SOS o el cálculo del cuerpo estricto terminen satisfactoriamente: las salidas abiertas contemplan ese fracaso. Debe quedar claro que una anticipación `INCONCLUSIVE` no elimina su clase del universo posterior.

La revisión de Sec. 6 también es adecuada como procedimiento. Debe registrar de qué familia procede el contenido revisado para comprobar la independencia exigida. Esta revisión textual no certifica esa procedencia ni satisface por sí sola las obligaciones relativas a archivos y certificados futuros.

Los límites contra universalidad y novedad están bien formulados. Deben mantenerse también en títulos y resúmenes: una igualdad en esta unión de clases con \(s=2\) no es rigidez general de QCA. Tampoco la repetición del mismo símbolo bajo P y F constituye evidencia adicional.

## Errores nuevos A-R2-NN

| ID | Ubicación | Gravedad | Reparación |
|---|---|---|---|
| **A-R2-01** | Secs. 1–2, tuplas, identificación de clases y Q-a | **Laguna** | Definir las tuplas de F sin partición y el dominio de Eq. (2), por ejemplo \(h\in N_3\). |
| **A-R2-02** | Sec. 2 y Paso 0′ | **Redacción con efecto en el cómputo** | Declarar el solapamiento: todo símbolo F pertenece también a una clase P por restricción a \(V_4\). Distinguir número de clases declaradas y número de símbolos independientes. |
| **A-R2-03** | Predecesores y Paso 0.4 | **Laguna** | Incluir la hipótesis \(D_2\) del Documento 5. No atribuir cobertura automática a \(C_4\); comprobar transportes que conserven al menos el \(D_2\) requerido. |
| **A-R2-04** | Sec. 5, salida principal | **Laguna** | Si se permite retirar la cota, admitir ambos sentidos de desigualdad como refutaciones de la igualdad. |
| **A-R2-05** | Paso 4b-1, Paso 4b-2 y Sec. 5 | **Laguna** | Mover las decisiones sobre existencia de sectores a la etapa que los analiza y fijar si Q-a cuantifica sobre símbolos unitarios o sobre símbolos con cono admisible. |
| **A-R2-06** | Sec. 5, `RIGIDITY_HOLDS_SATURATION_FAILS` | **Laguna** | Separar rigidez universal de fallo de saturación existencial o universal; explicitar ambos cuantificadores. |

**El contrato debe permanecer DRAFT hasta reparar estas seis cuestiones.** No se ha encontrado un nuevo error en la identidad tangencial, en A2 con \(Q_8\), en la normalización ni en las leyes de transporte propuestas. Sí quedan límites formales que impedirían interpretar sin ambigüedad una futura salida terminal. Esta revisión no autoriza cálculos ni promociona resultados históricos.