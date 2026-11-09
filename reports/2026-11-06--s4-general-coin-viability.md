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
