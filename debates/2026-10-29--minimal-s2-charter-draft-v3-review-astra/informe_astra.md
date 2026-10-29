<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-29T10:43:40Z  fin: 2026-10-29T10:50:10Z
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 8d8802a ; sha256 de la copia enviada b24ca440495893058f3e08bde0be165c6179a932728d3183a9963d80b55426fc
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-charter-draft-v2-review-astra/informe_astra.md ; último commit observado: 8d8802a ; sha256 de la copia enviada 35cf800f1aec3765492914e039d237e1b395ae8fd88cd9d4477f3a7c861a9deb
documento: /home/ignac/qca-causal-cones/debates/2026-10-29--minimal-s2-charter-draft-review-astra/informe_astra.md ; último commit observado: 3f0d9aa ; sha256 de la copia enviada ceedc86d1ac4fd8bd103465e2d7d07c23bb31728e4c3d3f64825997a4e7a02f4
documento: /home/ignac/qca-causal-cones/theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md ; último commit observado: 05eb1eb ; sha256 de la copia enviada 2ef8690e5eb4c4e0799ae6c38038b988d0fe7f7ea64fdcc596095d5bab257e26
documento: /home/ignac/qca-causal-cones/theory/STRICT_CONE_CEILING_N3_GATE.md ; último commit observado: 4135625 ; sha256 de la copia enviada aadaafb37d3e311fba39028699815f818322b02f9163661d1f96f30671b97827
documento: /home/ignac/qca-causal-cones/biblioteca/1708.00826v2.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada dc4107946e6013640dd225bfd6792f8ff4be9cae48d4c9763a7d6da57bb91c81
entrada_astra.txt sha256 47faf57359bb60c7a49ee223617ccae57b0bfc51bd9f84b725c38e5a36d76631
respuesta sha256 01445f3c8b3bd82a3d1e3507cca14df85d0af00e4ab35cd0c1b85a42d729640a
-->

**Veredicto: NOT_READY por una laguna de alcance en la regla de transferencia entre P y F.** Las reparaciones sobre la cota, la red recíproca, los nodos, el testigo de Q-a y la saturación son correctas. No encuentro una anticipación falsa entre A5–A8.

Uso exclusivamente los textos adjuntos. Tomo \(D_4\) de orden ocho y «símbolo admisible» como un símbolo de la clase con al menos un nodo admisible. Las modificaciones explícitas de v3 prevalecen sobre el Documento 4. El certificado histórico de la cota y el certificado basal no están adjuntos: su estado como resultados del repositorio queda **[UNVERIFIED]** en esta revisión. El Documento 5 fija hipótesis y obligaciones; no contiene la demostración posterior.

## 1. Reparaciones A-R2-01..06

| ID | Estado en v3 | Ubicación y comprobación |
|---|---|---|
| **A-R2-01** | **Resuelta** | Secs. 1–2: las clases F son \((F,G,[R])\), sin partición. Q-a fija expresamente \(h\in N_3\). La identificación por conjugación distingue P y F. |
| **A-R2-02** | **Resuelta en el solapamiento; pendiente una precisión sobre las transferencias** | Sec. 2, fila «Overlap»: reconoce correctamente la restricción a \(V_4\), la restricción \(D_4\to C_4\) y el doble cómputo de símbolos. Pero «Results transfer» es demasiado general para Q-a, cuya propiedad cambia con el grupo y el dominio de generadores. Véase **A-R3-01**. |
| **A-R2-03** | **Resuelta como protocolo de aplicación** | Paso 0.4: incorpora \(D_2\), excluye la cobertura automática de \(C_4\) y exige comprobar la covarianza después del desplazamiento del nodo. La condición recíproca es correcta. |
| **A-R2-04** | **Resuelta** | Sec. 1 y Sec. 5, fila principal: admite ambos sentidos de desigualdad y trata el sentido superior como conflicto cuando existe cobertura certificada. Debe conservarse siempre el calificativo «para ese nodo». |
| **A-R2-05** | **Resuelta** | Pasos 4b-1 y 4b-2; Sec. 5: separa existencia de símbolos y existencia de sectores. Q-a cuantifica sobre símbolos con nodo admisible y exige ese nodo al testigo. |
| **A-R2-06** | **Resuelta** | Sec. 5, fila de saturación: separa claramente la afirmación universal de igualdad y el testigo existencial de desigualdad estricta. No atribuye rigidez al testigo de fallo de saturación. |

## 2. Salidas con dirección y conflicto con la cota

La pregunta principal es una igualdad. Para una tupla admisible, su negación es exactamente

\[
c_0\ne c_{\rm strict}^{\rm iso}
\iff
c_0<c_{\rm strict}^{\rm iso}
\quad\text{o}\quad
c_0>c_{\rm strict}^{\rm iso}.
\]

Como la admisión exige \(c_0>0\), la definición de `..._BELOW` es correcta. `..._ABOVE` tampoco debe exigir positividad de \(c_{\rm strict}^{\rm iso}\): el Documento 5, Sec. 4, incluye expresamente valores estrictos nulos o negativos.

Cuando la cota está certificada y cubre la tupla,

\[
c_0\le c_{\rm strict}^{\rm iso}
\quad\text{y}\quad
c_0>c_{\rm strict}^{\rm iso}
\]

son incompatibles. El estado de conflicto es, por tanto, correcto: obliga a revisar la admisión, el cálculo, el transporte y la cobertura o demostración del resultado previo antes de promocionar una conclusión.

Esto es coherente con el `FAIL_COUNTEREXAMPLE` del Documento 5. Un testigo superior auténtico bajo sus hipótesis refutaría la cota; si esta ya se considera demostrada, habría que identificar qué certificado o afirmación anterior falla. El contrato nuevo no puede resolver esa contradicción mediante una mera reclasificación.

**La v3 no concede permiso para relajar la cota.** Conservar una clase \(C_4\) que no está automáticamente cubierta significa ampliar el dominio de la pregunta de igualdad, no retirar hipótesis o modificar un teorema existente.

Hay una imprecisión menor: Sec. 5 abrevia «inside a certified class», aunque Paso 0.4 certifica cobertura **por clase y nodo**. Un mismo grupo puede tener cobertura establecida en \(0\) y pendiente en otro nodo. Debe decir:

> «Cuando la cota esté certificada y sea aplicable a la tupla considerada».

No interpreto esa abreviatura como una autorización contraria a la regla explícita de Sec. 1.

## 3. Red recíproca y condición del Paso 0.4

Ambas fórmulas son correctas.

La red física se genera por

\[
\frac{2e_1}{\sqrt3},\quad
\frac{2e_2}{\sqrt3},\quad
\frac{2e_3}{\sqrt3},\quad
\frac{(1,1,1)}{\sqrt3}.
\]

Con la convención \(e^{-ik\cdot h}\), un vector recíproco \(K\) satisface

\[
K\cdot\lambda\in2\pi\mathbb Z
\qquad(\lambda\in\Lambda).
\]

Los tres primeros generadores obligan a

\[
K_j=\pi\sqrt3\,m_j,\qquad m_j\in\mathbb Z.
\]

El último exige

\[
\frac{K_1+K_2+K_3}{\sqrt3}
=\pi(m_1+m_2+m_3)\in2\pi\mathbb Z.
\]

Por tanto,

\[
\boxed{\Lambda^*
=\pi\sqrt3\{m\in\mathbb Z^3:m_1+m_2+m_3\text{ es par}\}.}
\]

La suficiencia se comprueba directamente: si \(n\) tiene las tres coordenadas de igual paridad, entonces \(m\cdot n\) es par cuando \(\sum_jm_j\) es par. Así, \(K\cdot(n/\sqrt3)\in2\pi\mathbb Z\). No falta ningún factor de \(2\pi\).

Para trasladar el nodo, sea

\[
V(k)=U(k+k_\star),\qquad
T'_h=e^{-ik_\star\cdot h}T_h.
\]

Usando la covarianza original,

\[
T'_{gh}=e^{-ik_\star\cdot gh}R_gT_hR_g^\dagger,
\qquad
R_gT'_hR_g^\dagger
=e^{-ik_\star\cdot h}R_gT_hR_g^\dagger.
\]

Como \(T_h\ne0\), ambas expresiones coinciden si y solo si

\[
e^{-i(g^{-1}k_\star-k_\star)\cdot h}=1
\qquad\text{para todo }h\in N_3.
\]

Dado que \(N_3\) genera \(\Lambda\), esto equivale a

\[
\boxed{g^{-1}k_\star-k_\star\in\Lambda^*.}
\]

Para aplicar el Documento 5 basta imponerlo para todo \(g\in D_2\). No es necesario conservar el grupo \(G\) completo.

Además, si

\[
U(k)^n=\sum_x e^{-ik\cdot x}C_x^{(n)},
\]

entonces

\[
V(k)^n=\sum_x e^{-ik\cdot x}
e^{-ik_\star\cdot x}C_x^{(n)}.
\]

El factor añadido nunca es cero: se conservan exactamente \(S_n\), \(h_\infty\) y \(c_{\rm strict}^{\rm iso}\). La pendiente se conserva porque \(V(p)=U(k_\star+p)\).

El «si y solo si» concierne a conservar **la misma representación \(R\)**. Su incumplimiento no demuestra que sea imposible encontrar otra representación apropiada o demostrar una cota de alcance mayor. La v3 puede dejar esas posibilidades sin utilizar.

## 4. Q-a y su testigo de refutación

El dominio queda bien definido. Para una clase \(\mathcal C\), escribamos

\[
\mathcal A_{\mathcal C}
=\{U\in\mathcal C:U\text{ tiene al menos un nodo admisible}\}.
\]

La propiedad que se pregunta es

\[
\forall U\in\mathcal A_{\mathcal C},\
\forall h\in D_{\mathcal C},\
\forall g\in G:
\quad gh\ne h\Longrightarrow [R_g,T_h]\ne0,
\]

donde \(D_{\mathcal C}=S_+\) en P y \(D_{\mathcal C}=N_3\) en F.

Por tanto, un testigo de refutación debe incluir:

- un símbolo que satisfaga todas las restricciones de la clase;
- un nodo y una fase admisibles, con \(c_0>0\);
- un par \(g,h\) del dominio correspondiente con
  \[
  gh\ne h,\qquad [R_g,T_h]=0.
  \]

Por covarianza,

\[
[R_g,T_h]=0
\iff R_gT_hR_g^\dagger=T_h
\iff T_{gh}=T_h.
\]

Esta es una comprobación exacta y finita una vez dado el símbolo. No exige calcular su cuerpo estricto ni comprobar todos sus nodos: **un nodo basta para que el símbolo pertenezca al dominio de Q-a**.

La condición es también independiente del representante proyectivo. Bajo

\[
R'_g=c_gWR_gW^\dagger,\qquad T'_h=WT_hW^\dagger,
\]

se tiene

\[
[R'_g,T'_h]=c_gW[R_g,T_h]W^\dagger,
\]

por lo que su anulación se conserva.

La lectura de F con \(S_+=S_-=N_3\), únicamente a estos efectos, es compatible con la posibilidad expresamente contemplada en el Documento 6, p.3. No introduce una partición ficticia.

**La laguna está en la transferencia entre clases, no en el testigo.** Si una clase F se restringe a una clase P tetraédrica, se cumple

\[
\mathcal A_F\subseteq\mathcal A_P,
\]

pero las propiedades de distinguibilidad son diferentes. Denotándolas por \(E_F\) y \(E_P\),

\[
E_F(U)\Longrightarrow E_P(U),
\]

porque P comprueba menos pares \((g,h)\). La inclusión de símbolos no proporciona la implicación contraria. En consecuencia,

\[
\bigl(\forall U\in\mathcal A_P,\ E_P(U)\bigr)
\]

no certifica por sí sola

\[
\forall U\in\mathcal A_F,\ E_F(U).
\]

Tampoco una violación en F se transfiere automáticamente a P: el elemento infractor puede estar fuera del subgrupo restringido, o el generador fuera del dominio comprobado.

Esto no construye un contraejemplo unitario a Q-a. Identifica una implicación que **no queda justificada por la restricción de clases**. Sec. 2 debe limitar sus transferencias automáticas a propiedades que no cambian al restringir la simetría, como la igualdad principal y la saturación.

## 5. Saturación y etapas de cierre

La fila de saturación tiene ahora los cuantificadores correctos.

Para cualquier símbolo del soporte congelado,

\[
S_n\subseteq nC_{\rm micro},
\]

de donde

\[
h_\infty(q)\le h_{C_{\rm micro}}(q).
\]

Aquí,

\[
h_{C_{\rm micro}}(q)
=\frac{|q_x|+|q_y|+|q_z|}{\sqrt3},
\qquad
\rho_{\rm micro}=\frac1{\sqrt3}.
\]

Evaluando en una dirección que minimiza el soporte microscópico,

\[
c_{\rm strict}^{\rm iso}\le\rho_{\rm micro}.
\]

Esta cota superior microscópica no depende de la cota inferior \(c_0\le c_{\rm strict}^{\rm iso}\). Por ello, sobre el dominio admisible,

\[
\neg\bigl[\forall U,\ c_{\rm strict}^{\rm iso}(U)=\rho_{\rm micro}\bigr]
\iff
\exists U:\ c_{\rm strict}^{\rm iso}(U)<\rho_{\rm micro}.
\]

Las dos salidas de saturación cubren, pues, las posibilidades matemáticas; `OPEN` cubre la falta de decisión. La nilpotencia de un vértice no sustituye al certificado de desigualdad.

Las etapas también están sustancialmente bien separadas:

| Etapa | Qué puede cerrar |
|---|---|
| Paso 0 | Anticipaciones y, cuando proceda, vaciedad mediante sus certificados. |
| 4a | Leyes de transporte y Q-b. |
| 4b-1 | Vaciedad o existencia de símbolos unitarios. |
| 4b-2 | Existencia de nodos, Q-a, comparación principal y saturación. |

Tres precisiones de ejecución evitan lecturas incorrectas:

1. **Un punto real prueba existencia, no cobertura universal.** `UNITARY_SYMBOLS_EXIST` no autoriza ninguna salida universal posterior.
2. **Una respuesta puede quedar cerrada aunque otra quede abierta.** Por ejemplo, un testigo puede refutar Q-a aunque el cuerpo estricto siga sin determinarse. La regla de parada de 4b-2 no debe borrar resultados ya certificados.
3. **Los dominios vacíos requieren una convención de presentación.** Si no hay símbolos admisibles, saturación y Q-a son universalmente verdaderas por vacuidad. Puede anotarse esa vacuidad sin añadir necesariamente nuevas etiquetas. La fila de sectores no necesita ejecutarse para una clase ya declarada vacía.

Con esas lecturas, las salidas son exhaustivas como estados de decisión. No constituyen una partición excluyente de todas las filas, algo que la propia Sec. 5 ya advierte.

Finalmente, 4a transporta los nodos incluidos en el certificado de partida. No convierte automáticamente un certificado de un nodo en un resultado sobre todos los nodos del símbolo. La obligación universal permanece en 4b-2.

## 6. Anticipaciones A5–A8

La forma de registrarlas es correcta: atribución retrospectiva, marca `[UNVERIFIED]` y obligación de comprobación posterior. Un informe anterior de IA no actúa así como certificado.

Las siguientes son derivaciones manuales de esta revisión, no verificaciones de los futuros artefactos del repositorio.

**A5: correcta.** Si \(H\le O\) es transitivo sobre ocho vértices,

\[
8\mid |H|,\qquad |H|\mid24,
\]

por lo que \(|H|=8\) o \(24\). En el segundo caso, \(H=O\). En el primero es un Sylow 2.

Existe un subgrupo de orden ocho generado por

\[
r(x,y,z)=(-y,x,z),\qquad s(x,y,z)=(x,-y,-z).
\]

Satisface \(r^4=s^2=e\), \(srs=r^{-1}\). Las potencias de \(r\) recorren una cara y \(s\) lleva a la opuesta: actúa transitivamente. La conjugación de los Sylow prueba la unicidad hasta conjugación en \(O\).

Además,

\[
\{e,r^2,s,r^2s\}=V_4
\]

es el subgrupo axial. Como este \(V_4\) es normal en \(O\), todos los conjugados del \(D_4\) exhibido lo contienen. Esto verifica también la inclusión utilizada en Sec. 2.

**A6: correcta.** La covarianza escalar y la transitividad obligan a \(T_h=A\) para los ocho vértices. La identidad de desplazamiento cero da

\[
8A^\dagger A=I.
\]

El desplazamiento \((2,2,2)\), en etiquetas \(\varepsilon\), tiene una sola pareja, y exige

\[
A^\dagger A=0.
\]

Son incompatibles. Como comprobación adicional,

\[
U(k)=8A\prod_j\cos(k_j/\sqrt3)
\]

se anula para determinados momentos y no puede ser unitario.

**A7: correcta para la representación \(E\) especificada.** La acción de \(S_4\) sobre las tres particiones en dos parejas tiene núcleo \(V_4\). Al componerla con la representación estándar bidimensional de \(S_3\),

\[
E(v)=I\qquad(v\in V_4).
\]

Su restricción a \(D_4\) factoriza por \(D_4/V_4\simeq C_2\), cuya imagen actúa con autovalores \(+1,-1\). Por tanto,

\[
E|_{D_4}\simeq1\oplus\chi.
\]

El \(V_4\) axial conserva el producto \(\varepsilon_x\varepsilon_y\varepsilon_z\) y es transitivo en cada tetraedro. Los coeficientes son entonces \(A\) y \(B\) en las dos órbitas. Para \((0,2,2)\), las únicas parejas son

\[
(1,-1,-1)\to(1,1,1),\qquad
(-1,-1,-1)\to(-1,1,1),
\]

una dentro de cada tetraedro. Así,

\[
A^\dagger A+B^\dagger B=0,
\qquad
4(A^\dagger A+B^\dagger B)=I,
\]

lo que prueba vaciedad.

**A8: correcta bajo el soporte activo congelado.** Para cada vértice \(h\), el desplazamiento \(2h\) tiene únicamente la pareja \((-h,h)\). En particular,

\[
T_{-h}^\dagger T_h=0.
\]

Si alguna de estas matrices \(2\times2\) fuera invertible, la otra sería cero. Como ambas son no nulas, ambas tienen rango uno.

Entonces \(\det T_h=0\), y Cayley–Hamilton da

\[
T_h^2=(\operatorname{tr}T_h)T_h.
\]

Por inducción,

\[
T_h^n=(\operatorname{tr}T_h)^{n-1}T_h.
\]

Por tanto, \(T_h\) es no nilpotente si y solo si \(\operatorname{tr}T_h\ne0\).

Conviene asignar expresamente A8 a un subapartado del Paso 0; A4 y A5 se comprueban naturalmente en 0′. Es una mejora de trazabilidad, no una nueva dificultad matemática.

## 7. Qué impide congelar y qué puede esperar

**Bloquea únicamente la regla demasiado amplia de transferencia de resultados en Sec. 2.** El problema puede corregirse sin ejecutar ninguna clasificación:

> Las pruebas universales y los contraejemplos de rigidez y saturación se transfieren según las inclusiones indicadas. Para Q-a se debe comprobar separadamente el dominio de pares \((g,h)\); no se aplica automáticamente esa regla.

Esta precisión importa porque el contrato debe fijar de antemano qué permite una promoción de resultados.

Pueden resolverse durante la ejecución:

- la enumeración representacional y sus convenciones exactas;
- los certificados de las anticipaciones;
- la factibilidad real y la cobertura de componentes;
- la existencia y clasificación de nodos;
- los cuerpos estrictos con coeficientes nilpotentes;
- la cobertura efectiva de cada nodo por la cota;
- el transporte de los certificados basales y sus límites.

No es necesario resolver esas cuestiones antes de congelar: constituyen el trabajo contratado y tienen salidas abiertas previstas.

Las abreviaturas clase/nodo, la presentación de verdades vacuas y la asignación explícita de A8 merecen corrección editorial, pero no alteran por sí solas el universo matemático definido.

### Errores nuevos A-R3-NN

| ID | Ubicación | Gravedad | Reparación y efecto |
|---|---|---|---|
| **A-R3-01** | Sec. 2, «Overlap of P and F», regla «Results transfer» | **Laguna; bloquea congelación** | La inclusión \(\mathcal A_F\subseteq\mathcal A_P\) no identifica los predicados \(E_F\) y \(E_P\) de Q-a. Limitar la transferencia automática a propiedades invariantes bajo restricción, o formular reglas específicas para Q-a. El cálculo de cuantificadores está en el punto 4. |
| **A-R3-02** | Sec. 5, salida `COUNTEREXAMPLE_VERIFIED_ABOVE` | **Redacción; no bloqueante** | Sustituir «inside a certified class» por cobertura certificada de la tupla, incluido el nodo. Sec. 1 y Paso 0.4 ya proporcionan la lectura correcta. |

**Veredicto global: NOT_READY, con una reparación contractual localizada: A-R3-01.** No he encontrado un error matemático en A5–A8, en la red recíproca, en la condición de traslado del nodo ni en la nueva separación entre rigidez y saturación. La regla de conflicto preserva la cota previa y no autoriza relajarla.