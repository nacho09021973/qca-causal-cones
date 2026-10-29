<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ a32e18975abd59f30d66e7515944fa2ba97cf98b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.165.0)
inicio: 2026-10-29T13:29:32Z  fin: 2026-10-29T13:44:08Z
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step4b1.md ; último commit observado: 38f462c ; sha256 de la copia enviada 74392ecd2f29a489b72584c0529cf09ca2aaa3aec5486f7dfb1d1c626c98a1ec
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step4b1.py ; último commit observado: 38f462c ; sha256 de la copia enviada 5f91feaeece0d36a4151c05069f71c303f51d7aec2edffe62dafcd216c93c609
documento: /home/ignac/qca-causal-cones/scripts/verify_minimal_s2_step00.py ; último commit observado: ebebca7 ; sha256 de la copia enviada adeb8afc4d4be5ed8d692f47727882e688991a36e7e5739a3eeb1bd053bbec5b
documento: /home/ignac/qca-causal-cones/reports/2026-10-29--minimal-s2-step00.md ; último commit observado: aea9f60 ; sha256 de la copia enviada ca0cfb14771788ad297dbc1b9b2358b5750ef83839120b94b351c6a409bd6df4
documento: /home/ignac/qca-causal-cones/theory/MINIMAL_S2_RIGIDITY_GATE.md ; último commit observado: 785565c ; sha256 de la copia enviada 657fa6d3e9f17b69fedfde5d592d038b1eca90e90c496a8da1b43ffaa5ae8ea5
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/biblioteca/arXiv-1902.10227.pdf ; último commit observado: sin versionar ; sha256 de la copia enviada 663d7ca3ba6a38cbb2073d1f2e65f59b22901eb778f24f9d78a9ecc2b2b8a5d4
entrada_astra.txt sha256 320dd0958f9ef90aaf83612937515612d9cd5518f4c09e82cf41ae2e84af75ac
respuesta sha256 bd456b957056c77a1827b905647b31dbfa0d22e564ae870b2560f645a88381bb
-->

**Veredicto: las cinco conclusiones de existencia/vaciedad son correctas para las clases congeladas.** Puedo sostenerlas mediante argumentos algebraicos independientes de las ejecuciones declaradas. El informe necesita, sin embargo, reparaciones de alcance y de descripción del certificado antes de promocionarse.

## Supuestos y límites

No he ejecutado código ni comprobado archivos, hashes, tiempos o registros. Las ejecuciones declaradas quedan **[UNVERIFIED]** en esta revisión. Tampoco están adjuntas las implementaciones de `S1.unitarity_equations`, `S1.groebner_is_unit` y `S1.WD.published_symbol`.

Interpreto P17 Eq. (2) como la condición de distinguibilidad descrita en los documentos:
\[
gh\ne h\Longrightarrow [R_g,T_h]\ne0,
\]
equivalentemente, por covarianza, \(T_{gh}\ne T_h\). No tengo el original de P17 para comprobar literalmente esa equivalencia documental.

En los cálculos uso vértices \(h\in\{\pm1\}^3\) y momento \(q=k/\sqrt3\), de modo que la normalización del charter queda respetada. Las referencias a DEP19 corresponden a **la extracción adjunta**, no a una inspección del PDF.

| Clase fiel | Parámetros reales antes de unitariedad | Veredicto | Comprobación independiente |
|---|---:|---|---|
| \(O\), F | 4 | `EMPTY_CLASS` | Contiene un \(C_4\) axial; la covarianza obliga a que el símbolo se anule en un momento concreto. |
| \(T\), tetraedro, P | 8 | `EMPTY_CLASS` | Contradicción algebraica mediante el determinante Laurent; también excluye soluciones de la complexificación. |
| \(D_4\), F | 8 | `EMPTY_CLASS` | Restricción al \(C_4\) axial. |
| \(C_4\), cara, P | 16 | `EMPTY_CLASS` | Argumento explícito de anulación, sin exigir soporte activo. |
| \(V_4\), tetraedro, Pauli, P | 16 | `UNITARY_SYMBOLS_EXIST` | Producto explícito de tres desplazamientos condicionados, con ocho coeficientes no nulos. Componentes no determinadas. |

## 1. Parametrización y representaciones fieles

### Reducción a la inclusión

Es correcta **para estos cinco grupos**. No basta, en general, con conocer el subgrupo imagen: hay que controlar también las distintas identificaciones del dominio con esa imagen. Aquí existe un argumento que resuelve ambas cuestiones.

Una representación fiel \(\rho:G\to SO(3)\) conserva el orden de cada elemento. Los únicos órdenes presentes son \(1,2,3,4\), y la traza de una rotación tridimensional queda determinada por ellos:

\[
\begin{array}{c|rrrr}
\operatorname{ord}(g)&1&2&3&4\\ \hline
\operatorname{tr}\rho(g)&3&-1&0&1.
\end{array}
\]

Por tanto, toda \(\rho\) fiel tiene exactamente el carácter de la inclusión, elemento por elemento. Dos representaciones reales de un grupo finito con igual carácter son equivalentes; al ser ortogonales, puede elegirse un entrelazador ortogonal \(Q\). Si \(\det Q=-1\), se sustituye por \(-Q\), que produce la misma conjugación y pertenece a \(SO(3)\).

Así,
\[
\rho(g)=QgQ^{-1}.
\]
Un levantamiento unitario \(W\) de \(Q\) permite sustituir \(T_h\) por \(W^\dagger T_hW\), obteniendo la inclusión. Esto preserva unitariedad y soporte activo.

**No se pierde una clase fiel por automorfismos exteriores.** Precomponer con cualquier automorfismo conserva los órdenes y, por tanto, el mismo carácter. Por ejemplo, un automorfismo exterior de \(D_4\) puede requerir una conjugación espacial de \(45^\circ\), exterior a \(O\); eso no es un obstáculo: el cambio de base interno admite cualquier \(W\) unitario, no solamente levantamientos de elementos de \(O\).

### Acción sobre Pauli

También es correcta. Con las matrices de Pauli utilizadas,

\[
R_g(b\cdot\sigma)R_g^\dagger=(gb)\cdot\sigma,
\qquad
R_gIR_g^\dagger=I.
\]

La fórmula se extiende por linealidad compleja a \(b\in\mathbb C^3\). El signo del levantamiento y las fases proyectivas desaparecen en la conjugación.

Los elementos de los grupos espaciales elegidos son matrices enteras de permutación con signos. No hace falta que sus levantamientos espinoriales tengan entradas enteras.

## 2. Las dos construcciones del espacio covariante

### `class_symbol`

La restricción al espacio fijo del estabilizador es necesaria y suficiente.

Si \(h=gh_0\), la propuesta es
\[
b_h=gb_0.
\]
Cuando \(gh_0=g'h_0\), se tiene \(g'^{-1}g\in\operatorname{Stab}(h_0)\). Por tanto, ambas definiciones coinciden exactamente cuando
\[
sb_0=b_0\quad\text{para todo }s\in\operatorname{Stab}(h_0).
\]

El código impone estas ecuaciones sobre las partes real e imaginaria. Son homogéneas y lineales; resolverlas no introduce ramas algebraicas ni pierde soluciones mediante divisiones por parámetros. Los símbolos libres restantes parametrizan todo el espacio fijo. La comprobación posterior de las imágenes repetidas verifica la buena definición.

La variable `base` no se utiliza, pero es código redundante, no un error matemático.

### `class_symbol_linear`

También construye el espacio correcto: empieza con ocho matrices complejas libres e impone todas las ecuaciones lineales de covarianza. La solución general de ese sistema proporciona exactamente el mismo espacio vectorial real.

Los recuentos son:

| Clase | Órbitas en \(N_3\) | Espacio vectorial fijo del estabilizador | Parámetros reales |
|---|---:|---|---:|
| \(O\) | 1 | Una dirección compleja, paralela a \(h_0\) | 4 |
| \(T\) | 2 | Una dirección compleja por órbita | 8 |
| \(D_4\) | 1 | \(\mathbb C^3\), estabilizador trivial | 8 |
| \(C_4\) | 2 | \(\mathbb C^3\) por órbita | 16 |
| \(V_4\) | 2 | \(\mathbb C^3\) por órbita | 16 |

Estos números son dimensiones del **espacio lineal covariante anterior a imponer unitariedad**, no dimensiones de las clases unitarias.

### Independencia y discrepancia con el informe

Son dos implementaciones útiles para detectar errores en el tratamiento de órbitas y estabilizadores. Comparten, sin embargo:

- la enumeración y acción de los grupos;
- la convención de Pauli;
- el generador de ecuaciones de unitariedad;
- la función que decide el ideal unidad;
- SymPy.

No constituyen dos certificaciones independientes de toda la cadena.

Además, hay una discrepancia demostrable: **para \(V_4\), la segunda construcción no calcula ninguna base de Gröbner**. En la rama `else`, únicamente comprueba `len(p2) == len(params)` y busca el punto de Pavia. La frase «same Groebner outcome in every class» no describe el código adjunto.

Igualar dimensiones tampoco demuestra, por sí solo, que dos subespacios sean iguales. Aquí la igualdad se justifica mediante los argumentos anteriores; una comprobación computacional directa podría comparar sus bases en las mismas 64 coordenadas reales.

## 3. Vaciedad y bases de Gröbner

### Prueba corta para \(C_4\), y por restricción para \(D_4\) y \(O\)

Elijamos como generador espacial
\[
r(x,y,z)=(-y,x,z),
\]
y sea \(R\) su levantamiento espinorial. Consideremos
\[
q_*=(\pi/2,\pi/2,0).
\]

Para cualquier vértice,
\[
w(h):=e^{-iq_*\cdot h}=-h_xh_y,
\qquad
w(rh)=-w(h).
\]

La covarianza implica
\[
R\,U(q_*)\,R^\dagger
=\sum_h w(h)T_{rh}
=-U(q_*).
\]

Pero la conjugación por un levantamiento de una rotación de \(90^\circ\) tiene autovalores
\[
1,1,i,-i
\]
en \(M_2(\mathbb C)\). No tiene autovalor \(-1\). Por tanto,
\[
U(q_*)=0,
\]
incompatible con la unitariedad.

Esto vacía \(C_4\), \(D_4\) y \(O\), **incluso permitiendo coeficientes nulos**.

También prueba vaciedad de la complexificación del sistema real. La anulación es una identidad lineal en los parámetros; sigue siendo cierta al complexificarlos. Si
\[
E_\ell=\sum_{h,h+\ell\in N_3}T_h^\dagger T_{h+\ell}
-\delta_{\ell,0}I,
\]
entonces
\[
\sum_\ell e^{-iq_*\cdot\ell}E_\ell=-I.
\]
Aquí los pesos son exactamente
\[
e^{-iq_*\cdot\ell}=(-1)^{(\ell_x+\ell_y)/2}.
\]
Una entrada diagonal proporciona una combinación constante de las identidades que vale \(-1\). Es una contradicción algebraica exacta.

### Prueba algebraica para \(T\)

La covarianza tetraédrica obliga a escribir
\[
T_h=a_pI+c_p\,h\cdot\sigma,
\qquad p=h_xh_yh_z\in\{+,-\}.
\]

Trabajemos incluso sobre la complexificación. Las identidades de unitariedad proporcionan un inverso Laurent para
\[
U(z)=\sum_hT_hz^h.
\]
En consecuencia, \(\det U(z)\) es una unidad del anillo Laurent:
\[
\det U(z)=d\,z^m,\qquad d\ne0.
\]

La covarianza hace que el determinante sea invariante bajo \(T\). Como \(T\) no fija ningún vector no nulo, \(m=0\). Así, el determinante debe ser una constante no nula.

Escribiendo \(U=fI+b\cdot\sigma\),
\[
\det U=f^2-b\cdot b.
\]

Sus coeficientes no constantes dan:

- En el exponente \(2h\):
  \[
  a_+^2=3c_+^2,\qquad a_-^2=3c_-^2.
  \]
- En el exponente \((0,2,2)\), cuyas dos contribuciones ordenadas proceden de \((1,1,1)\) y \((-1,1,1)\):
  \[
  a_+a_-=c_+c_-.
  \]

Multiplicando las primeras dos igualdades y usando la tercera,
\[
(c_+c_-)^2=9(c_+c_-)^2,
\]
luego \(c_+c_-=a_+a_-=0\).

Sin embargo, el coeficiente constante del determinante es
\[
d=8(a_+a_-+3c_+c_-)=0,
\]
contradicción.

Esta prueba tampoco utiliza soporte activo y excluye soluciones complejas.

Como segunda comprobación, sobre el dominio real con soporte activo, el rango uno da
\[
|a_\pm|^2=3|c_\pm|^2.
\]
La traza de la identidad del desplazamiento \((0,2,2)\) da
\[
|a_+|^2+|a_-|^2=|c_+|^2+|c_-|^2,
\]
lo que fuerza que todos sean cero.

### Fiabilidad de `[1]`

**Sí:** una base de Gröbner exacta igual a `[1]` certifica vaciedad compleja, con `grevlex` o con cualquier otro orden monomial admisible.

La condición esencial es que se haya calculado para el sistema correcto, en un anillo polinómico sobre un cuerpo exacto, sin especializaciones o divisiones injustificadas. Las hipótesis `real=True` no convierten Gröbner en un procedimiento de geometría real: se está estudiando la complexificación de las ecuaciones obtenidas al separar partes reales e imaginarias.

La implementación concreta no es auditable completamente con los adjuntos: faltan las funciones de `S1`. Los argumentos anteriores validan las conclusiones matemáticas, pero no verifican que las ejecuciones declaradas produjeran `[1]`.

## 4. La clase \((V_4,\mathrm{Pauli})\) y DEP19

### Existencia y comprobación de Pavia

Un solo punto real basta para `UNITARY_SYMBOLS_EXIST`, siempre que se comprueben:

1. unitariedad;
2. covarianza;
3. los ocho coeficientes no nulos.

La comprobación de covarianza de `pavia_point` es correcta:
\[
a=\tfrac12\operatorname{tr}T,\qquad
b_j=\tfrac12\operatorname{tr}(T\sigma_j).
\]
La igualdad de trazas verifica la parte escalar, y el otro test verifica \(b_{gh}=gb_h\).

La extracción también tiene el signo correcto **si** `M` usa
\[
M(z)=\sum_h z^{-h}T_h.
\]
El coeficiente de \(z^{v+\mathbf1}\) en \(z^{\mathbf1}M(z)\) es \(T_{-v}\).

La función no comprueba actualmente unitariedad ni soporte activo: los hereda de la etapa anterior, que utiliza dependencias no adjuntas. Por ello, la identificación exacta «Pavia, quiralidad 1» queda **[UNVERIFIED]** aquí.

Existe, no obstante, un testigo explícito que puede verificarse directamente. Definamos
\[
P_j^\epsilon=\frac{I+\epsilon\sigma_j}{2},\qquad
T_{(x,y,z)}=P_x^xP_y^yP_z^z.
\]
Entonces
\[
U(q)=e^{-iq_x\sigma_x}e^{-iq_y\sigma_y}e^{-iq_z\sigma_z}
\]
es unitario y tiene exactamente esos ocho coeficientes.

Cada producto tiene norma de Frobenius \(1/2\), pues los dos solapamientos entre autoestados de ejes consecutivos tienen módulo \(1/\sqrt2\). Todos los coeficientes son no nulos. La conjugación por Pauli cambia exactamente los dos signos correspondientes al semigiro espacial. Es, por tanto, un punto real exacto de la clase.

### Qué falta para conocer las componentes

El cálculo declarado no determina:

- la dimensión del conjunto unitario;
- sus componentes algebraicas complejas;
- cuáles contienen puntos reales;
- las componentes del conjunto real con soporte activo;
- su identificación bajo las equivalencias permitidas.

Para estudiar el dominio activo debe incorporarse esa condición, por ejemplo mediante la variable auxiliar del charter. Una descomposición primaria compleja no determina por sí sola las componentes conexas reales ni la existencia real en cada componente.

Estas tareas no son necesarias para cerrar únicamente la fila de existencia de 4b-1.

### Comparación con A30

A30 es la familia pertinente: en la extracción de DEP19 se obtiene **antes** de imponer la normalización (14), con \(V\) unitario libre y sin asumir distinguibilidad. Deben conservarse las condiciones
\[
\alpha_i>0,\qquad
\alpha_1\alpha_2=\alpha_3\alpha_4,\qquad
\sum_i\alpha_i^2=1.
\]

Según la exhaustividad que anuncia DEP19, la clase estudiada debe quedar contenida en A30 y sus variantes por las transformaciones enumeradas. **La exhaustividad global de esa reducción queda [UNVERIFIED] en esta revisión**: no tomo los pasos de eliminación resumidos en el artículo como una certificación adicional. Sí puedo comprobar consecuencias directas de las matrices transcritas.

El unitario libre \(V\) **no es libre después de exigir covarianza Pauli**. Por irreducibilidad,
\[
U(0)=e^{i\phi}I.
\]
Si \(A_h=VB_h\), esto obliga a
\[
V=e^{i\phi}\left(\sum_hB_h\right)^\dagger.
\]
No debe confundirse este \(V\) con una multiplicación izquierda arbitraria que preserve la clase.

Además, la transitividad sobre el tetraedro iguala las normas de los cuatro coeficientes positivos. En A30 resulta
\[
\alpha_i=\tfrac12.
\]
La fórmula anterior fija \(V\), salvo fase, como A31. Las trazas positivas pasan a ser
\[
\operatorname{tr}A_{+1}=\operatorname{tr}A_{+2}
=e^{i\phi}\frac{1+e^{i\theta}}4,
\]
\[
\operatorname{tr}A_{+3}=\operatorname{tr}A_{+4}
=e^{i\phi}\frac{1-e^{-i\theta}}4.
\]
Su igualdad exige
\[
\cos\theta=0.
\]
Por tanto, A30 con \(V\) arbitrario es mucho mayor que su intersección con esta clase covariante.

### A30 no sugiere violaciones de Eq. (2) dentro de esta clase

En A30, los cuatro coeficientes positivos son, salvo factores no nulos,
\[
VP_0,\quad VP_1,\quad V|0\rangle\langle1|,
\quad V|1\rangle\langle0|.
\]
Son matrices distintas para cualquier \(V\) invertible: corresponden a cuatro unidades matriciales diferentes. Una multiplicación izquierda invertible no puede crear una igualdad entre dos coeficientes.

Hay además una prueba directa para **toda** la clase \(V_4\), sin utilizar la exhaustividad de A30.

Supongamos que un semigiro no trivial \(g\in V_4\) satisface
\[
T_{gh}=T_h.
\]
Entonces \(T_h\) conmuta con \(R_g\). Por soporte activo y las identidades antipodales, \(T_h\) y \(T_{-h}\) tienen rango uno. Como \(R_g\) tiene dos autovalores distintos,
\[
T_h=\lambda P
\]
para uno de sus proyectores espectrales. Las dos identidades antipodales fuerzan
\[
T_{-h}=\mu(I-P).
\]
Este último también conmuta con \(R_g\), de modo que \(T_{-gh}=T_{-h}\).

El desplazamiento \(\ell=gh-h\) tiene exactamente dos pares:
\[
(h,gh),\qquad(-gh,-h).
\]
Su identidad de unitariedad se convierte en
\[
T_h^\dagger T_h+T_{-h}^\dagger T_{-h}=0,
\]
imposible.

**Así, bajo la interpretación declarada de Eq. (2), todo símbolo unitario activo de esta clase satisface distinguibilidad.** Este resultado algebraico no necesita estudiar nodos. No determina las componentes ni verifica las condiciones de admisión de 4b-2.

### Error sobre A32 y la condición (14)

DEP19 (14) es
\[
\sum_h A_h=I.
\]
Es una normalización; no es la condición de isotropía.

Un contraejemplo explícito, usando A30, es
\[
\alpha_i=\tfrac12,\qquad \theta=0,\qquad V=I.
\]
Entonces \(\sum_hA_h=I\), pero las trazas de los cuatro coeficientes positivos son
\[
\tfrac12,\quad\tfrac12,\quad0,\quad0.
\]
No puede haber covarianza por conjugación transitiva sobre ese tetraedro.

La unitariedad puede comprobarse sin apelar al artículo. Si \(q_j=e^{-iq\cdot h_j}\), entonces \(\prod_jq_j=1\), y el símbolo es
\[
\begin{pmatrix}f&g\\-\bar g&\bar f\end{pmatrix},
\quad
f=\frac{q_1+q_2^{-1}}2,\quad
g=\frac{-q_3+q_4^{-1}}2.
\]
La relación entre los \(q_j\) da \(|f|^2+|g|^2=1\). Es unitario, normalizado en cero y no covariante transitivamente sobre el tetraedro indicado.

## 5. Alcance del informe

La conclusión correcta es:

> Dentro de las familias congeladas, y usando las eliminaciones de la etapa (a), la única clase declarada no vacía es \((P,V_4,\text{tetraedro},\text{Pauli})\).

Esto no clasifica todos los símbolos unitarios BCC sin hipótesis de isotropía.

La frase «P17’s isotropy setting without its Eq. (2)» debe ajustarse al charter, que distingue expresamente entre su universo congelado y «P17 menos Eq. (2)». Es aceptable identificar el grupo y la representación con el marco Pauli de P17; no presentar ambos universos como idénticos.

La vaciedad de \(C_4\) elimina cualquier contraejemplo, superior o inferior, **en esa clase**. No elimina por sí sola `COUNTEREXAMPLE_VERIFIED_ABOVE` en toda la unión: todavía no se ha comprobado el transporte de todos los nodos de la clase superviviente.

La condición indicada por el charter sigue siendo
\[
g^{-1}k_\star-k_\star\in\Lambda^*
\quad\text{para todo }g\in D_2.
\]
La frase final del informe sobre la cota, restringida a nodos con transporte admisible, tiene el alcance correcto. No he revisado el teorema previo de la cota, cuyo certificado no está adjunto.

## Reparaciones obligatorias

| Identificador | Ubicación | Gravedad | Reparación |
|---|---|---|---|
| **A-4B1-01** | D1, «Provenance», «Unitarity», «Existence»; D2, importaciones de `S1` | **Laguna de auditabilidad** | Incorporar al paquete las implementaciones congeladas de las tres dependencias críticas y su procedencia, o sustituir las afirmaciones computacionales pertinentes por certificados algebraicos explícitos. Las revisiones anteriores no permiten inspeccionar código ausente. |
| **A-4B1-02** | D1, «Two independent constructions…»; D2, rama no unitaria del ideal | **Error demostrado de descripción** | Eliminar «same Groebner outcome in every class». Para \(V_4\), la segunda construcción sólo compara el número de parámetros. Corregir el texto basta; no es necesario repetir Gröbner para demostrar existencia. |
| **A-4B1-03** | D1, «Two independent constructions…» | **Redacción** | Describirlas como dos construcciones del espacio covariante con infraestructura compartida. Precisar qué errores pueden detectar y que igualdad de dimensiones no prueba igualdad de subespacios. |
| **A-4B1-04** | D1, «Consequence»: identificación con P17 | **Redacción de alcance** | Nombrar exactamente la clase congelada y su coincidencia de grupo/representación con P17. Respetar la distinción expresa del charter respecto de «P17 menos Eq. (2)». |
| **A-4B1-05** | D1, «The outcome `COUNTEREXAMPLE_VERIFIED_ABOVE` therefore has no object» | **Laguna de alcance si se pretende global; redacción si se pretende local** | Restringir la afirmación a \(C_4\). Una exclusión global requiere justificar la cobertura de todos los nodos relevantes de la clase superviviente. |
| **A-4B1-06** | D1, «DEP19 (A30), audit only» | **Error demostrado** | Sustituir «isotropy condition (14)» por «normalización \(\sum_hA_h=I\)». A32 no impone por sí sola la covarianza Pauli; el ejemplo anterior demuestra la diferencia. |

La falta de una descomposición en componentes **no es una reparación obligatoria para cerrar existencia en 4b-1**. Tampoco debe exigirse resolver nodos o velocidades en esta etapa.

## Veredicto global

**Resultados por clase aceptados matemáticamente; informe no promocionable tal como está redactado.**

Las vaciedades admiten pruebas exactas independientes, y la clase Pauli tiene un testigo explícito con soporte completo. No encuentro una representación fiel omitida ni un defecto en las dos parametrizaciones.

Quedan por reparar la descripción de las comprobaciones, la auditabilidad de las dependencias y las afirmaciones de alcance. A30 no proporciona un contraejemplo a distinguibilidad en la clase Pauli; el argumento directo anterior, de hecho, la establece para todos sus símbolos unitarios activos bajo la interpretación indicada de Eq. (2).