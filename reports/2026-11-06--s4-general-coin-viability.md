# Moneda general: exclusión de una pendiente isotrópica distinta

**Promocionado el 2026-11-09 en su alcance congelado** (instrucción del
usuario; ver `state/CURRENT_STATE.md`). La línea de estado siguiente es la previa.

2026-11-06. Codex (OpenAI). **PRELIMINARY: derivación y controles de autor**.

[Revisión ciega de Grok](reviews/2026-11-09-s4-general-coin-viability-grok/informe_grok.md)
(2026-11-09, grok-4.7, herramientas 97292a9, texto en 170910b): «se sostiene»,
sin objeciones; rederiva a mano las dos vías, inspecciona el script sin
ejecutarlo. Añade por su cuenta un corolario (no hay cono isótropo inclinado)
y un testigo de no vacuidad; no se incorporan aquí. Una ronda; informe sin editar.
Contrato: `theory/S4_GENERAL_COIN_VIABILITY.md`, SHA256
`a817034f28736469d5ecccb0901bc9ba2c49832dde5dcff6117bc4bca2b1de13`.
Hash registrado a las 08:51:26 UTC antes de ejecutar el verificador;
ejecución completada antes de las 08:52:24 UTC. La vía de prueba había
sido advertida durante el razonamiento, como declara el contrato.
No prerregistro Git. Base: `b434547432647ca72110d4f7b6c78583d70f27c9`.

## Resultado

Para cualquier W en U(4), sea

    U(k)=W product_i exp(-i k_i G_i/sqrt(3)),
    G_i=sigma_i tensor tau_i.

Si U(0)=W posee un eigenvalor de multiplicidad exactamente dos, separado
del resto, y su doblete define un cono lineal isotrópico no degenerado
sin inclinación, entonces **c=1/3** en las unidades fijadas.

No se exige antiunitaria, covariancia espacial, forma tensorial de W,
segundo doblete ni irreducibilidad. Por eso la exclusión también se aplica
a la subclase irreducible solicitada. No existe el testigo c distinto de
1/3 dentro del contrato. El constructor anterior muestra que c=1/3 sí es
realizable; la exclusión no procede de una clase vacía.

## 1. Reducción que elimina la moneda

Los G_i conmutan, son involuciones y G_x G_y G_z=-I4. Para
F_raw={h en {±1}³: h_x h_y h_z=-1}, sus cuatro proyectores conjuntos son

    E_h = (I4 + sum_i h_i G_i)/4.

Cada uno tiene rango uno, sum_h E_h=I4 y sum_h h_i E_h=G_i.
U(k)=sum_h W E_h exp(-i k.h/sqrt(3)). Como W es invertible, los cuatro
coeficientes W E_h siguen siendo no nulos. El soporte y la escala son
exactamente los del contrato, sin ajuste posterior.

Sea T:C²->C⁴ una isometría sobre el doblete, WT=zT, |z|=1.
Al comprimir la expansión de U en el doblete, el término de primer orden
es z[I2-i sum_i q_i H_i], donde

    H_i = T†G_i T/sqrt(3).

La separación espectral permite usar esta compresión para las pendientes
nodales de primer orden. W determina T y z, pero no añade un término a
H_i: iW†partial_i U(0)=G_i/sqrt(3).

## 2. Primera prueba: rango de las compresiones

Definir B_h=T†E_h T. Son matrices positivas 2x2 de rango a lo sumo uno,
con suma I2. La fórmula de E_h da exactamente

    B_h = [I2 + sqrt(3) sum_i h_i H_i]/4.                 (1)

Ausencia de inclinación significa tr H_i=0. Escribimos H_i=a_i.sigma,
con a_i real. La métrica del cono es M_ij=a_i.a_j=tr(H_i H_j)/2.
Isotropía no degenerada significa M=c² I3 y c>0.

De (1), tr B_h=1/2, y la identidad de determinante de Pauli produce

    det B_h = [1-3 h^T M h]/16
            = [1-9 c²]/16.                            (2)

Pero rango B_h<=1 exige det B_h=0. Por tanto c²=1/9 y c=1/3.
La traza 1/2 asegura además que ninguna de estas compresiones sea nula.
Esto vale para cualquier T que satisfaga las hipótesis, no para una
muestra de monedas o de subespacios.

## 3. Segunda vía: suma de trazas cuadráticas

Cada B_h tiene rango uno y traza 1/2, luego tr(B_h²)=1/4 y
sum_h tr(B_h²)=1. Por otra parte, usando (1), sum_h h_i=0 y
sum_h h_i h_j=4 delta_ij,

    sum_h tr(B_h²) = 1/2 + (3/4) sum_i tr(H_i²)
                  = 1/2 + (9/2)c².

Igualar ambas expresiones vuelve a dar c²=1/9. Es una segunda derivación
algebraica de autor con las mismas hipótesis; no es revisión independiente.

## 4. Qué queda excluido y qué no

Queda excluido construir el bloque inicial de pendiente diferente cambiando
solo W, incluso con una moneda U(4) arbitraria, bajo las condiciones de
nodo k=0, doblete separado, isotropía lineal y ausencia de inclinación.
Dos bloques de esta clase que cumplan esas condiciones tendrán ambos
c=1/3. El barrido de acoplamiento no se abre.

No se ha clasificado cuáles monedas producen conos ni se han impuesto
las simetrías de la realización anterior. La restricción procede de los
cuatro proyectores de rango uno del desplazamiento fijo, no de una
antiunitaria adicional sobre la moneda.

No cubierto: otros desplazamientos o números/rangos de canales, dimensiones
internas distintas, conos inclinados, degeneraciones nodales de otro rango
ni modelos interactuantes. El contrato se limita al origen; no se reclama
una clasificación global de nodos. El mecanismo general de alineación
permanece sin evaluar. No se amplía la familia para salvar la propuesta.

## 5. Evidencia reproducible

Comando: `python3 -B scripts/verify_s4_general_coin_viability.py`.
SymPy 1.14.0, salida 0: **55/55 comprobaciones algebraicas auxiliares PASS**.
Registro: `reports/2026-11-06--s4-general-coin-viability-verifier.txt`.
Script SHA256:
`6565ddc135215e371279b97c298422e809124110b3b3b439f79941fe6437a5f4`.
Comprueba proyectores, inversión tetraédrica, momentos, identidad de
determinante para nueve coeficientes reales generales, suma de trazas
cuadráticas y consecuencia isotrópica. El argumento universal de rango
está en la prueba anterior; los controles no sustituyen esa prueba.

Índice de biblioteca consultado. La clasificación s=2 de 1708.00826 no se
invoca para esta exclusión s=4. No se ha investigado la novedad de la
identidad de compresión; no se atribuye originalidad al resultado.

Resultado: `NO_DIFFERENT_UNTILTED_ISOTROPIC_SPEED_AT_ORIGIN_FOR_GENERAL_U4_COIN`.
Se cierra esta ampliación mínima. Sin búsqueda numérica, barrido,
revisión externa, promoción, commit ni push. Se preservan cambios ajenos.


---

## Apéndice A — contrato de ampliación por soporte (2026-11-09)

**Estado inicial: OPEN.** Este apéndice es nuevo y no está cubierto por la
revisión ni por la promoción de las secciones anteriores.

**Autorización:** el usuario responde «Sigue» a comprobar si la rigidez
sobrevive al ampliar las reglas conservando el soporte tetraédrico y las
condiciones del cono. Precisa que busca diferencias físicas entre modelos,
no el valor numérico de c en unidades humanas.

**Base leída:** d4f06d0ddd7a9ddc2619e0562f48168cba8e7bd9.
Rama de trabajo: research/tetrahedral-support-rigidity-2026-11-09.
Se conserva íntegro el informe anterior. Por la instrucción actual de
«un paso, una pregunta, un fichero», contrato y posterior ejecución se
registran como apéndices de este único informe existente, en commits
separados. El primer commit congela el contrato; no se modifica el contrato
histórico ni se promociona ningún resultado.

### A.1 Conocido, pregunta y criterio de abandono

Conocido: las secciones 1–4 de este informe prueban c0=1/3 para cualquier
moneda U(4) con los cuatro proyectores de desplazamiento fijados, bajo
sus condiciones nodales. CURRENT_STATE.md registra su promoción en ese
alcance el 2026-11-09.

Pregunta única: ¿todo símbolo unitario homogéneo de cuatro componentes con
soporte REAL exactamente
F={(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)}/sqrt(3)
tiene c0=1/3 cuando posee en k=0 un doblete espectral separado, con cono
lineal isotrópico no degenerado y sin inclinación?

Se admite U(k)=sum_{v in F} A_v exp(-i k.v), con A_v matrices complejas
4x4 arbitrarias y no nulas, U(k) unitaria para todo k. No se presupone
moneda-desplazamiento, rango de A_v, base interna, covariancia D2/C/S,
irreducibilidad ni un segundo doblete. La red es el subgrupo aditivo
generado por F; no hay cociente espacial finito. Longitud de cada salto y
duración de actualización: uno.

El cono se define por los generadores comprimidos
H_i=T†[i U(0)† partial_i U(0)]T, para una isometría nodal T:C²->C⁴.
Se exige tr H_i=0 y tr(H_i H_j)/2=c0² delta_ij, c0>0.
La fase nodal puede ser cualquiera; su multiplicidad es exactamente dos.

Criterio de abandono de la búsqueda de otra velocidad en esta clase:
una reducción algebraica de TODA la clase a la familia ya resuelta, o
una prueba directa de c0=1/3. No se ampliarán soporte, dimensión o tipo
de nodo para evitar ese cierre.

### A.2 Método y límites

Primero comparar coeficientes de Fourier en U†U y UU†; después estudiar
las consecuencias sobre los rangos y los generadores nodales. La posible
vía mediante diferencias únicas del soporte y proyectores ortogonales
ya se ha advertido antes de este registro: se congela el alcance, no
se reivindica prerregistro del descubrimiento.

Una derivación manual completa dará PRELIMINARY; un testigo exacto de
otra velocidad refutará la extensión; una obligación no resuelta dará
OPEN_AFTER_BOUNDED_ANALYSIS. Una sesión, sin barrido ni programa nuevo.
Si hiciera falta cálculo automatizado adicional, no se ejecutará como
script efímero. Las comprobaciones 55/55 del informe histórico no se
atribuirán a esta extensión.

No están cubiertos: interacciones, universalidad computacional, estabilidad
del nodo bajo perturbaciones que lo destruyan, otros soportes o dimensiones,
otros nodos, cuerpo causal estricto asintótico, máxima velocidad de grupo,
selección cosmológica o valor físico de c.

Se consultaron las instrucciones versionadas, el estado y los informes
relevantes, además de scripts/biblioteca_catalog/curated.csv. El índice
local biblioteca/INDICE.md no forma parte del árbol remoto; las reglas
locales ~/herramientas/REGLAS.md no están disponibles en este entorno.
No se declara haberlos leído. La búsqueda bibliográfica inicial no
certifica novedad ni ausencia de antecedentes. NOVELTY = OPEN.
No se encarga revisión externa ni se actualiza el estado canónico.


## Apéndice B — ejecución algebraica de A (2026-11-09)

**PRELIMINARY — derivación manual de autor; sin revisión independiente ni
promoción. NOVELTY = OPEN.**

Contrato congelado en el commit
c7ac2d9f748bf19f2f0690d573e2f3e22fe0e607, apéndice A.
No se han ejecutado programas, simulaciones o nuevos verificadores para
este apéndice. No se atribuyen a él los controles del informe original.

**Resultado en el alcance de A:** toda regla admitida es equivalente,
mediante un cambio de base interna constante, a una moneda U(4) seguida
del desplazamiento tetraédrico ya estudiado. Por tanto todo doblete que
cumpla las condiciones nodales de A tiene c0=1/3. La búsqueda de otra
pendiente en esta clase termina por reducción algebraica, no por falta
de ejemplos.

### B.1 El soporte obliga a anular cada término cruzado

Los cuatro vértices v de F son afínmente independientes. Por tanto,
para v!=w, la diferencia w-v determina de manera única el par ordenado
(v,w): una igualdad w-v=w'-v' daría una relación afín entre los cuatro
vértices; la independencia solo admite el mismo par (excluido el caso
de diferencia cero). Equivalentemente, este tetraedro no tiene un
paralelogramo formado por cuatro vértices.

En la red infinita, los caracteres de Fourier de desplazamientos
distintos son independientes. Al comparar los coeficientes de U†U=I y
UU†=I se obtiene, para v!=w,

    A_v† A_w = 0,                 A_v A_w† = 0,

y, para el desplazamiento cero,

    sum_v A_v† A_v = I4,          sum_v A_v A_v† = I4.

Las dos ortogonalidades provienen de las dos identidades unitarias;
no se deduce una de ellas asumiendo que los A_v sean normales.

### B.2 La forma moneda-desplazamiento es una consecuencia

Definir W=U(0)=sum_v A_v. Es unitario. Definir

    P_v = W† A_v = A_v† A_v.

La segunda igualdad usa A_w† A_v=0 para w!=v. Así P_v es positivo y
sum_v P_v=I4. Para v!=w,

    P_v P_w = A_v† (A_v A_w†) A_w = 0.

Por ello P_v=P_v sum_w P_w=P_v²: son proyectores ortogonales.
Cada P_v es no nulo porque el soporte REAL exige A_v!=0.
Cuatro proyectores no nulos que suman I4 tienen todos rango uno.
Finalmente,

    A_v = W P_v,
    U(k) = W sum_v P_v exp(-i k.v).

No se supuso esta factorización, ni se eligió una base que la impusiera.

Existe una unitaria interna constante S con S†P_v S=E_v, donde E_v son
los cuatro proyectores fijos de las secciones 1–2, emparejados con los
mismos vértices. Entonces

    S†U(k)S = (S†WS) sum_v E_v exp(-i k.v).

Es exactamente la familia anterior, con moneda W'=S†WS arbitraria.
La conjugación constante conserva espectro, multiplicidades, separación
del doblete y la métrica de las pendientes; no cambia posiciones,
momentos, duración del paso ni unidades.

### B.3 Comprobación directa de la pendiente

Para no depender únicamente de la remisión al resultado anterior,
se deriva la pendiente de nuevo. Con el signo de Fourier de A,

    J_i = i U(0)† partial_i U(0) = sum_v v_i P_v,
    B_v = T† P_v T,
    H_i = T† J_i T = sum_v v_i B_v.

Los B_v son positivos, de rango a lo sumo uno, y suman I2.
Como los vértices tienen norma uno y v.w=-1/3 para v!=w,
la inversión tetraédrica da

    B_v = (I2 + 3 sum_i v_i H_i)/4.                    (B1)

En efecto, al sustituir H_i=sum_w w_i B_w, el coeficiente de B_v
es 1 y el de cada B_w con w!=v es cero.

Sin inclinación, H_i=a_i.sigma con a_i real. La isotropía completa
exige a_i.a_j=c0² delta_ij. En particular,

    |sum_i v_i a_i|² = c0² |v|² = c0²,
    tr B_v = 1/2,
    det B_v = (1-9 c0²)/16.                           (B2)

Como rango B_v<=1, su determinante se anula. La traza 1/2 evita la
compresión nula. Se sigue c0²=1/9 y, por c0>0, c0=1/3.

La ecuación (B2) es la misma obstrucción por rango de la prueba original.
Lo añadido es que unitariedad, soporte exacto y s=4 obligan a que ese
mecanismo se aplique a TODOS los coeficientes permitidos por A.
No se necesita un segundo doblete ni una hipótesis de irreducibilidad.

### B.4 Alcance físico y cierre

La formulación independiente de unidades es

    c_IR tau / ell = 1/3,

si ell es la longitud física del salto elemental y tau su duración.
Bajo un cambio de unidades, los cambios de c_IR, tau y ell se cancelan.
Comparar ese cociente entre modelos exige mantener claro qué se
considera salto y actualización elementales; reagrupar actualizaciones
no equivale por sí solo a cambiar la física.

La dependencia es estructural: geometría de diferencias del soporte,
unitariedad, dimensión interna cuatro y condiciones del doblete.
La geometría causal sola sigue sin determinar la velocidad en clases
más amplias. Tampoco se ha identificado ell/tau con la máxima velocidad
de grupo ni con una velocidad estricta asintótica.

Esta prueba da rigidez CONDICIONAL: si una perturbación conserva el
soporte, s=4 y el tipo de nodo, no puede cambiar c0. No prueba que una
perturbación genérica conserve el doblete, su separación o su isotropía.
No selecciona el soporte ni explica por qué nuestro universo lo usaría.
No demuestra una velocidad universal entre sectores ajenos a esta clase.

Se aplica el criterio de abandono de A.1: buscar una velocidad distinta
cambiando estos A_v no abre una familia espectral nueva. No se inicia
otra ampliación.

**Registro de evidencia:** reducción algebraica completa de autor,
PRELIMINARY; revisión independiente pendiente; sin verificación formal,
sin promoción y sin afirmación de novedad. La promoción del 2026-11-09
al principio del fichero sigue cubriendo solo las secciones originales.


---

## Apéndice C — auditoría de antecedentes (2026-11-09)

**NOVELTY = OPEN. Riesgo alto de que el resultado sea una aplicación o un
corolario de resultados conocidos.** Esta auditoría no es revisión
independiente de B, ni promoción científica. Se conserva la historia del
informe; la evaluación bibliográfica siguiente sustituye cualquier
impresión de novedad basada únicamente en no haber localizado una fórmula.

### C.1 Pregunta y método

Pregunta: ¿qué parte de la cadena de B —soporte tetraédrico exacto,
unitariedad, factorización con cuatro proyectores de rango uno, compresión
nodal e isotropía que fuerzan c_IR tau/ell=1/3— está publicada o se deduce
directamente de antecedentes?

Se buscaron trabajos sobre paseos en grafos de Cayley, clasificación
isotrópica, redes tetraédricas relativistas y POVM/SIC de qubit. Se
contrastaron los textos primarios indicados abajo, incluyendo las
ecuaciones decisivas de los PDF. Se distinguieron fechas del preprint y de
publicación; las fechas de subida de copias a repositorios no se usaron
como prioridad científica.

La comparación se limita a A. No es una revisión exhaustiva de todo
qca-causal-cones, ni evalúa la novedad de la corona IR, el techo hexagonal,
las interacciones o la universalidad computacional. Una búsqueda negativa
no establece prioridad.

### C.2 Antecedentes decisivos y diferencias de hipótesis

**[C1] O. López Acevedo y T. Gobron, *Quantum walks on Cayley graphs*.**
Preprint 2005; J. Phys. A: Math. Gen. 39, 585 (2006).
[arXiv:quant-ph/0503078v4](https://arxiv.org/abs/quant-ph/0503078v4);
[DOI](https://doi.org/10.1088/0305-4470/39/3/011).

En la p. 6 del preprint, ecuaciones (20)–(23) y teorema 1, las mismas
ortogonalidades bilaterales y normalizaciones llevan a
M_delta=U P_delta, con proyectores ortogonales completos. También se
identifica el rango uno cuando la dimensión interna es mínima.

**Comparación propia:** el teorema está enunciado para grupos libres;
nuestra red es abeliana. No se invoca sin comprobar hipótesis. Pero B.1
establece precisamente las identidades algebraicas que usa su prueba,
porque las diferencias no nulas del tetraedro son únicas. El paso B.2
reutiliza ese argumento conocido. La diferencia de grupo no aporta, por
sí sola, una nueva dificultad de factorización.

**[C2] J. M. Renes, R. Blume-Kohout, A. J. Scott y C. M. Caves,
*Symmetric Informationally Complete Quantum Measurements*.**
Preprint 2003; J. Math. Phys. 45, 2171 (2004).
[arXiv:quant-ph/0310075](https://arxiv.org/abs/quant-ph/0310075);
[DOI](https://doi.org/10.1063/1.1737053).

La sección III, ecuaciones (17)–(18), y IV.A describen la geometría simplex
de las SIC y el caso de qubit: cuatro estados puros con vectores de Bloch
tetraédricos.

**Comparación propia:** escribir H_i=c0 sum_a R_ia sigma_a, R ortogonal,
convierte (B1) en B_v=[I+3c0 (R^T v).sigma]/4. El rango uno exige longitud
de Bloch uno, luego 3c0=1. Los B_v son entonces los efectos de una SIC
tetraédrica, y 2B_v son sus proyectores puros. El artículo no enuncia un
teorema de velocidad; la conexión con el nodo es nuestra identificación,
mientras que la geometría empleada es conocida. No se identifica un
solapamiento SIC con una velocidad por mera coincidencia numérica.

**[C3] B. Z. Foster y T. Jacobson, *Propagating spinors on a tetrahedral
spacetime lattice*.**
Preprint 2003, revisión 2004.
[arXiv:hep-th/0310166v2](https://arxiv.org/abs/hep-th/0310166v2).

En pp. 1–2, ecuaciones (2)–(9), los pasos son epsilon(1,alpha n_i),
con n_i tetraédricos unitarios. Con velocidad relativista continua fijada
a uno, eligen alpha=3 para que las caras causales discretas sean nulas;
aparecen los proyectores (I+n_i.sigma)/2. En p. 4 explicitan que la
evolución discreta no es unitaria.

**Comparación propia:** tau=epsilon y ell=3epsilon dan el mismo cociente
c_IR tau/ell=1/3. Es un antecedente físico directo de la proporción y de los
proyectores, no una demostración de la rigidez para toda la clase unitaria
s=4 de A. Además, parten de una ecuación continua cuya velocidad ya está
especificada; no seleccionan la velocidad de nuestro universo.

La continuación de los autores,
[*Spin on a 4D Feynman Checkerboard*](https://arxiv.org/abs/1610.01142)
(preprint 2016; DOI
[10.1007/s10773-016-3170-0](https://doi.org/10.1007/s10773-016-3170-0)),
desarrolla esta construcción. Véanse pp. 4–5, ecuaciones (5)–(11), y p. 14
sobre la falta de unitariedad discreta.

**[C4] G. M. D'Ariano, M. Erba y P. Perinotti,
*Isotropic quantum walks on lattices and the Weyl equation*.**
Phys. Rev. A 96, 062101 (2017).
[arXiv:1708.00826v2](https://arxiv.org/abs/1708.00826v2);
[DOI](https://doi.org/10.1103/PhysRevA.96.062101).

La proposición 5 (p. 7 del preprint) clasifica los paseos isotrópicos de dimensión interna
s=2 bajo sus hipótesis; en tres dimensiones aparece la red BCC. La
definición usa covariancia del paseo completo y un soporte con generadores
e inversos.

**Comparación propia:** A tiene s=4, solo cuatro direcciones tetraédricas y
una condición local sobre la métrica del doblete. No puede trasladarse
automáticamente la clasificación s=2. Es un antecedente de la estrategia
de obtener dinámica Weyl mediante restricciones microscópicas, no una
identificación demostrada de las dos clases.

**[C5] U. Nzongani, N. Eon, I. Márquez-Martín, A. Pérez, G. Di Molfetta
y P. Arrighi, *Dirac quantum walk on tetrahedra*.**
Phys. Rev. A 110, 042418 (2024).
[arXiv:2404.09840v1](https://arxiv.org/abs/2404.09840v1);
[DOI](https://doi.org/10.1103/PhysRevA.110.042418).

Las secciones II y IV construyen un paseo con límite Dirac sobre una
teselación obtenida dividiendo cubos en seis ortoesquemas tetraédricos.
Las amplitudes se sitúan en caras y la dinámica concatena operaciones
locales y desplazamientos.

**Comparación propia:** no es, por compartir la palabra tetraedro o usar
cuatro amplitudes, la clase homogénea de cuatro traslaciones de A. Haría
falta demostrar una equivalencia de símbolos, soportes y actualización.
El artículo no se usa para atribuir a A su clasificación ni su velocidad.

**[C6] L. Mlodinow y T. A. Brun, *Bounds on quantum cellular automaton
lattice spacing from data on Lorentz violation*.**
Phys. Rev. D 112, 074513 (2025).
[arXiv:2506.20136](https://arxiv.org/abs/2506.20136);
[DOI](https://doi.org/10.1103/5w6s-jr1d).

Como contexto físico reciente, estudian desviaciones de velocidad y
anisotropías en un QCA correspondiente a QED, y usan restricciones
experimentales y astrofísicas para acotar su espaciado. Aquí se verificaron
los metadatos y el resumen primario; no se auditaron sus cotas numéricas.
No se presenta como antecedente demostrado del teorema A. Ilustra que la
cuestión física de un sustrato discreto se investiga también mediante sus
consecuencias observables.

### C.3 Qué queda de la posible aportación

| Pieza del argumento | Evaluación |
| --- | --- |
| Diferencias tetraédricas únicas implican ortogonalidad de coeficientes | Aplicación geométrica de las identidades de unitariedad conocidas; comparación propia con [C1]. |
| Ortogonalidad implica moneda y proyectores; s=4 implica rango uno | Argumento algebraico ya presente en [C1]. |
| Compresión de rango uno y geometría tetraédrica fijan la longitud de Bloch | Geometría conocida de [C2], aplicada aquí a los generadores nodales. |
| La proporción tetraédrica 1/3 puede aparecer en una dinámica relativista discreta | Antecedente físico [C3], con distinta unitariedad y dirección de construcción. |
| Todas las reglas de A tienen esa pendiente si existe el doblete requerido | Enunciado exacto no localizado en los textos revisados; riesgo alto de corolario. Ausencia de localización no certifica novedad. |

El resultado de B sigue siendo útil para cerrar una búsqueda: cambiar los
coeficientes dentro de A no permite una pendiente distinta mientras se
mantengan las condiciones nodales. La auditoría no encuentra un motivo
bibliográfico para retractar esa derivación, pero tampoco constituye su
validación independiente.

La valoración científica se reduce: no hay base para presentar la
factorización, la geometría tetraédrica de qubit o la aparición del factor
1/3 como descubrimientos propios. El posible residuo es la formulación
conjunta, precisa y condicional para toda la clase de A. Que esa formulación
sea correcta no implica que tenga suficiente contenido nuevo para un
artículo autónomo.

### C.4 Próximo gate único

Antes de ampliar modelos o ejecutar nuevos barridos, contrastar con un
especialista el enunciado A y esta pregunta:

> ¿Queda algún paso matemático sustantivo que no sea una aplicación directa
> del argumento de [C1], la geometría tetraédrica/SIC de [C2] y la
> compresión espectral de primer orden?

El resultado de esa comparación debe identificar el paso concreto y sus
hipótesis, o clasificar honestamente el enunciado como corolario/aplicación.
El contraste con [C3] debe mantener visible la diferencia entre evolución
discreta unitaria y no unitaria. No se ha solicitado esa revisión ni se
declara superado este gate.

Estado al cierre de esta auditoría: **B = PRELIMINARY; NOVELTY = OPEN;
antecedentes directos identificados; importancia física general no
establecida.** No se modifica CURRENT_STATE.md ni se extiende la promoción
histórica a los apéndices.


### C.5 Trazabilidad y control de la síntesis asistida

Se completó una búsqueda amplia asistida:
[informe automático sin corregir](https://agent.tinyfish.ai/research/01a1c0f9-face-7211-bbaf-bf8a534fe0e1).
Es material auxiliar para localizar candidatos, no revisión independiente
ni versión científica de esta auditoría.

Su conclusión de novedad no se adopta: omitió [C1] y [C3], y reconoció no
haber leído directamente la literatura SIC. Además, en algunos pasajes
presenta la existencia/isotropía del cono como conclusión, cuando en A son
hipótesis, y normaliza incorrectamente las compresiones. Las identidades
correctas son sum_v B_v=I2; a c0=1/3 los efectos SIC son B_v, y los
proyectores puros son 2B_v. Ningún párrafo de esa síntesis altera A o B.

Se comprobaron los originales que sostienen C.2. Algunas otras referencias
recientes sugeridas por la búsqueda no pudieron corroborarse directamente
en su texto primario y no se usan para sostener novedad ni prioridad. El
informe automático tampoco determina que una bibliografía sea exhaustiva.


---

## Apéndice D — síntesis y puente de un paso: contrato (2026-11-09)

**Estado al registrar: OPEN.** Autorización actual del usuario: reunir los
antecedentes y el resultado propio para construir una base sólida; reiterada
con «Sigue». Esta es una síntesis acotada dentro de A, no una promoción.

**Conocido.** B deriva la factorización, las compresiones SIC y c0=1/3
(PRELIMINARY). C identifica sus antecedentes. El constructor de
[2026-11-06--s4-cyclic-realization.md](2026-11-06--s4-cyclic-realization.md),
secciones 2 y 4, ya proporciona un ejemplo exacto; su alcance promovido se
registra en CURRENT_STATE.md, bloque de promociones del 2026-11-09.
No se construirá otro ejemplo ni se repetirán sus verificadores.

**Pregunta única.** ¿La compresión sobre el doblete fijo de k=0, retirando
su fase nodal, coincide con el operador de UN paso de Foster–Jacobson [C3],
y hasta dónde permite esa identidad reunir ambas construcciones?

Se mantienen íntegramente las hipótesis y normalización de A. Sean
W=U(0), WT=zT, T†T=I2, Pi=TT† y Q=I4-Pi. Se compararán
K(k)=z^(-1)T†U(k)T y el polinomio de pasos tetraédricos de [C3], pp. 1–2,
ecuaciones (2), (6) y (9), tras identificar longitud elemental, ejes y
convención de Fourier. La igualdad que se busca es algebraica de un paso,
no una identificación de los espacios-tiempo completos.

**Criterio de abandono.** Si no coinciden los coeficientes de ese
polinomio, se abandona la identificación con [C3]. Si comprimir después de
dos pasos difiere de iterar K, se rechaza cualquier equivalencia temporal
general basada solo en la coincidencia de un paso. El testigo para ese
contraste será exclusivamente el constructor ya existente.

**Método y cierre.** Derivación manual breve: usar B, calcular la
compresión, insertar Pi+Q en dos pasos y, si hace falta, especializar un
eje del constructor existente. La ruta de la identidad y de su posible
obstrucción ya fue advertida durante el razonamiento previo a este
registro: no se reivindica prerregistro del descubrimiento. Se registra
el alcance antes de incorporar la derivación al informe.

Una derivación completa se marca PRELIMINARY; una obligación no resuelta,
OPEN_AFTER_BOUNDED_ANALYSIS. No habrá nuevos programas, simulaciones,
clasificaciones, modelos, reejecuciones, revisión externa ni promoción.
Se reusan las referencias de C con atribución expresa; NOVELTY = OPEN.

Se han releído las instrucciones versionadas, los pasajes pertinentes del
estado, el informe existente, su constructor y el catálogo versionado.
Los originales [C1]–[C3] se han contrastado directamente. Las reglas
locales ~/herramientas/REGLAS.md no están disponibles aquí; no se declara
haberlas leído. El índice local no se sustituye por un índice inventado.


## Apéndice E — síntesis algebraica y límite de la identificación (2026-11-09)

**PRELIMINARY: derivación manual de autor bajo el contrato D.**
Contrato registrado en 610f86af3df46e20cae4b0e4b10e9b51fdd44ef6.
Sin nueva ejecución de código, revisión independiente o promoción.
**NOVELTY = OPEN.** Las identidades siguientes son una comparación propia
con fuentes atribuidas, no resultados que se atribuyan a esos autores.

### E.1 Base común y atribución

La base consiste en una cadena de implicaciones con sus hipótesis
visibles. Dentro de A, B.1 permite aplicar el argumento de factorización
de López Acevedo–Gobron [C1]; la dimensión interna cuatro fuerza cuatro
proyectores de rango uno. Su compresión al doblete, junto con isotropía y
ausencia de inclinación, produce la geometría SIC tetraédrica [C2].
El resultado condicionado es c_IR tau/ell=1/3.

La aportación del repositorio es formular y demostrar esa cadena para su
clase precisa, además de disponer de un constructor ya registrado.
Esta formulación se trata como aplicación/síntesis de antecedentes hasta
que una revisión de prioridad identifique contenido nuevo suficiente.
Una prueba más clara tiene valor aunque su conclusión sea un corolario.

[C4] y [C5] quedan como comparadores de clases. [C6] proporciona contexto
fenomenológico. Sus hipótesis y conclusiones no se incorporan como
premisas de esta prueba.

### E.2 Identidad exacta de la compresión de un paso

Usar la factorización de B:

    U(k)=W D(k),       D(k)=sum_v P_v exp(-i k.v),
    WT=zT,            T†T=I2,       |z|=1.

Como W es normal, el subespacio del eigenvalor z es reductor; por tanto
T†W=zT†. Al retirar la fase nodal se obtiene exactamente, para todo k,

    K(k):=z^(-1)T†U(k)T
         =sum_v B_v exp(-i k.v),     B_v=T†P_v T.          (E1)

T es la isometría FIJA del doblete en k=0. No es un marco espectral
dependiente de k, y K no se declara una evolución cerrada de ese doblete
a momento finito.

Escribir H_i=(1/3)sum_a R_ia sigma_a, con R ortogonal, como permite B.
Entonces, con n_v=R^T v,

    B_v=[I2+n_v.sigma]/4 = Pi_v^FJ/2,
    Pi_v^FJ=[I2+n_v.sigma]/2,
    sum_v B_v=I2.                                         (E2)

Los n_v son vértices de un tetraedro unitario. Si p=R^T k, (E1) se vuelve

    K(k)=(1/2)sum_v Pi_v^FJ exp(-i p.n_v).                 (E3)

Este es el polinomio de UN paso de [C3], p. 2, ecuaciones (6) y (9),
expresado con longitud elemental uno y los ejes consistentes. Allí el
salto espacial tiene longitud 3epsilon y el tiempo de paso epsilon, con
velocidad continua fijada a uno: el cociente adimensional vuelve a ser
1/3. El cambio ortogonal de ejes debe conservarse en la comparación,
incluida su orientación; no se identifica una reflexión con una
conjugación SU(2).

Se identifica el polinomio de un paso, no todo el espacio de estados ni
la foliación temporal de [C3]. Esta última usa capas espaciales que se
desplazan entre actualizaciones.

### E.3 El operador comprimido puede perder norma sin contradicción

Sean Pi_0=TT†, Q_0=I4-Pi_0 y V(k)=z^(-1)U(k). Puesto que V es unitario,

    I2-K(k)†K(k)=T†V(k)† Q_0 V(k)T >= 0.                 (E4)

La diferencia mide la amplitud que sale del subespacio retenido. La
unitariedad del sistema completo no exige unitariedad de esta compresión.
Es consistente con la no unitariedad de la regla discreta que señalan
Foster–Jacobson, p. 4 de [C3].

Insertar Pi_0+Q_0 entre dos pasos da otra identidad exacta:

    T†V(k)^2 T-K(k)^2 = T†V(k) Q_0 V(k)T.                (E5)

El miembro derecho no está obligado a anularse. K^2 inserta una
proyección intermedia; comprimir V^2 permite salir del subespacio y
regresar. Una coincidencia de un paso no autoriza a transferir los
propagadores completos ni sus resultados de convergencia.

### E.4 Obstrucción explícita usando el constructor existente

Se reutiliza, sin modificarlo, el constructor de
[2026-11-06--s4-cyclic-realization.md](2026-11-06--s4-cyclic-realization.md),
secciones 2 y 4:

    G_i=sigma_i tensor tau_i,
    n=(1,1,1)/sqrt(3),       N=I2 tensor (n.tau),
    W=(I4-iN)/sqrt(2),
    Pi_0=(I4+N)/2,          Q_0=(I4-N)/2.

Elegir T psi=psi tensor |n,+>, donde (n.tau)|n,+>=|n,+>.
Entonces z=exp(-i pi/4) y z^(-1)W=Pi_0+i Q_0. En el eje
k=(k_x,0,0), poniendo a=k_x/sqrt(3),

    D(k)=cos(a)I4-i sin(a)G_x,
    T†G_x T=sigma_x/sqrt(3),
    K(k)=cos(a)I2-i sin(a)sigma_x/sqrt(3).                (E6)

De G_x^2=I4 se sigue

    T†G_x Q_0 G_x T
      =I2-(T†G_x T)^2=(2/3)I2.                          (E7)

Sustituir V=(Pi_0+i Q_0)D en (E5) produce

    T†V(k)^2 T-K(k)^2
      =i T†D(k)Q_0 D(k)T
      =-(2i/3)sin(a)^2 I2.                              (E8)

Por tanto difieren siempre que sin(a)!=0. Es un contraejemplo algebraico
a la identificación temporal general dentro de la clase ya existente,
sin barrido ni nuevo modelo. También

    I2-K(k)†K(k)=(2/3)sin(a)^2 I2.                       (E9)

La diferencia de (E8) empieza en orden k_x^2; no contradice la coincidencia
del término lineal. Los controles históricos del constructor no se
atribuyen a (E8) o (E9): estas identidades se han derivado aquí a mano y
requieren su propia revisión.

### E.5 Afirmación consolidada y límites

**Afirmación que permite esta síntesis, con evidencia PRELIMINARY:**

> Para paseos homogéneos exactamente unitarios con soporte tetraédrico
> unitario de cuatro pasos no nulos y cuatro componentes internas,
> cualquier doblete separado en k=0 que tenga un cono lineal isotrópico
> no degenerado y sin inclinación tiene c_IR tau/ell=1/3. Su compresión
> de un paso, retirada la fase nodal, coincide con el polinomio tetraédrico
> de Foster–Jacobson tras identificar ejes y normalización. Esa identidad
> no se extiende en general a la evolución iterada; el constructor
> existente da una diferencia no nula ya en dos pasos.

La primera parte reexpone B con atribución a sus ingredientes conocidos.
La segunda explicita el puente documental y algebraico. La tercera
impide transferir indebidamente propiedades entre las dos dinámicas.
No se afirma originalidad de ninguna de las tres por no haber encontrado
el mismo enunciado en la bibliografía.

Esta base explica una rigidez CONDICIONAL dentro de un universo de
juguete definido. La existencia del cono, su isotropía y el tipo de nodo
siguen entre las condiciones; no aparecen como consecuencias nuevas de
juntar artículos. Tampoco se obtiene selección del sustrato de nuestro
universo, estabilidad genérica del nodo, igualdad entre todas las
especies, universalidad computacional o el cuerpo causal estricto.

### E.6 Resultado del contrato y revisión pendiente

La pregunta de D queda respondida por una derivación de autor: identidad
exacta de un paso y obstrucción explícita a la identificación temporal
general. Se aplica su criterio de abandono a esa identificación temporal;
no se abre otra familia para evitar el contraejemplo.

**PRELIMINARY; NOVELTY = OPEN.** La revisión especializada de C.4 sigue
pendiente. El paquete concreto para revisarla es ahora A–B, las fuentes
[C1]–[C3], y las ecuaciones (E1)–(E9), con atención a la fase z, la
normalización de los efectos SIC, la orientación de ejes y la distinción
entre compresión e iteración. Una revisión debe juzgar corrección y
novedad por separado. No se ha contactado a terceros ni se ha actualizado
el estado canónico.
