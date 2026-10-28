# A.int — comprobación de una referencia de ocupaciones en Eon v4

Fecha: 2026-10-27. Autor: Codex.
Autorización: «especificar y comprobar el estado de referencia».
Especificación previa: [A_INT_EON_REFERENCE_CHECK.md](../theory/A_INT_EON_REFERENCE_CHECK.md).
Procedencia: la subpregunta A.int fue formulada por Claude; la selección
concreta de candidato, este certificado y esta comprobación son de Codex.

## Resultado

`GAUSS_PASS / OCCUPATION_REFERENCE_STATIONARITY_FAIL / STOP_THIS_CANDIDATE`.
Evidencia: `EXACT_AUTHOR_CHECKED / INDEPENDENT_REVIEW_PENDING`.

El producto homogéneo con modos 2,3 llenos, modos 0,1 vacíos y flujo
eléctrico entero cero pertenece al sector físico fijado. **No es una
referencia estacionaria para el paso completo en los casos comprobados.**
Para masa t=m epsilon con sin(t) distinto de cero, el fallo se deduce
exactamente de un observable fermiónico conservado por los subpasos gauge.
En t=0 se obtiene además un fallo del paso completo en un intervalo
magnético explícito. No se prueba aquí un fallo en todos los ángulos
magnéticos massless ni la inexistencia de otro vacío físico de Eon.

No hay una referencia aceptada para construir propagadores o velocidades.
Se termina la comprobación de este candidato sin sustituirlo por otro
estado, Hamiltoniano padre, truncación o circuito.

## Fuente y cuantificadores

Fuente primaria: `biblioteca/arXiv-2205.03148v4.pdf`, especialmente p.12
(sector físico), p.13 (referencia de ocupaciones), pp.15 y 25–29 (gates,
masa y paso completo), pp.19–23 (plaquetas). Es el mismo PDF identificado
por el manifiesto de fuentes del preflight anterior; no es texto generado
por IA usado como fuente. Las páginas son páginas PDF.

Se comprueba una concreción explícita de esa referencia de ocupaciones en
3D; el artículo ejemplifica en p.13 la elección en 2D, no un vacío espectral
3D con estas etiquetas ya demostrado. El candidato de esta sesión es

`Omega_occ = tensor_x |1100>_(3,2,1,0) tensor |E=0>`.

Red periódica cúbica L>=3, cuatro modos fermiónicos por sitio y rotores
gauge enteros no truncados. Los extremos de cada enlace tienen valores
opuestos. Sector `G_x=div E_x+N_x-2=0`. Se usa el orden de v4,
`U=D_M D_E D_F`, y el magnetismo exponencial exacto (21)/(36), no la
aproximación de dos subpasos (26). No hay frontera que absorba carga.
Las identidades locales y el argumento de soporte valen para todo L>=3;
los controles ejecutables de cobertura se limitan expresamente a L=3,4.

## 1. Gauss y la parte anterior a la masa

Inicialmente `N_x=2` y todos los flujos son cero, luego `G_x=0`.
En el transporte de la dirección eta, los swaps de S1 llevan la ocupación
local `[0,0,1,1]` a `[0,1,0,1]` (orden de modos creciente).
En cada bloque T_eta de cuatro modos de p.27:

1. El primer swap transporta la ocupación de `(x,3)` a `(x+eta,0)`;
   sube el flujo saliente por una unidad, conservando Gauss en ambos sitios.
2. Los dos swaps centrales actúan sobre pares 00 y 11. Solo dan fases.
3. El segundo swap devuelve la ocupación y resta la unidad de flujo.
4. S2 devuelve `[0,0,1,1]` en cada sitio.

Los bloques usan pares de modos distintos incluso en sitios compartidos.
Las fases de K/JW no generan superposiciones en esta entrada determinista.
Por tanto cada capa direccional devuelve la misma configuración, salvo una
fase global. No se ha supuesto que las fases sean iguales en otras entradas.

Las B de (33) actúan sobre pares 00 y 11: cada una deja el candidato sobre
su mismo rayo. El certificado comprueba exactamente ese autovector local.
Así, respetando todo el orden kappa, B, nu, B, mu, B,

`D_F Omega_occ = exp(i chi) [tensor_x C_x(t)] Omega_occ`.

Esta reducción es específica del candidato; no elimina los campos gauge
de la evolución general. Los controles L=3,4 comprueban los swaps y Gauss
en las tres direcciones: 546 comprobaciones de Gauss después de swaps
de enlace. Una mutación del signo de flujo viola Gauss; omitir el segundo
swap de enlace impide restaurar la configuración. Ambos controles negativos
son detectados por el certificado.

## 2. Masa: dos construcciones exactas y un observable del paso completo

Se construye la matriz de 16 dimensiones de p.26 con dos gates C de dos
modos y el fSWAP central. Como segunda implementación, se levanta la
matriz unipartícula (31) a todos los sectores fermiónicos mediante menores
(potencias exteriores). Las dos matrices coinciden exactamente; también
se comprueban unitariedad y conservación del número local.

Para la entrada local |1100> se obtiene

`<n_0+n_1>_despues = 2 sin²(t)`;
`Prob(patron local original)_despues = cos⁴(t)`.

Antes del paso, el primer observable vale cero. Los generadores eléctricos
y de plaquetas no cambian las ocupaciones fermiónicas: los factores JW
pueden depender de sus paridades, pero son diagonales en ellas. Por tanto
`[D_E,n_(x,j)]=[D_M,n_(x,j)]=0`. Esto usa las definiciones (1), (6),
(14)–(15), (21), (35)–(36); no supone que el gauge no se entrelace.

En consecuencia, **para U completo**, en cada sitio,

`<Omega_occ|U†(n_0+n_1)_x U|Omega_occ> = 2 sin²(t)`.

Una diferencia en este observable gauge invariante rechaza la
estacionariedad de la densidad, aunque solo interesen observables físicos.
Es una comprobación del paso completo y evita la limitación de los
controles de subpaso del informe de viabilidad.

Test principal fijado: epsilon=1, m=pi/4, g_E=g_M=1. Conserva la relación
de p.19, sin interpretarse como acoplamiento débil. El valor posterior por
sitio es exactamente 1, frente a 0 inicialmente, para cualquier evolución
gauge posterior que conserve esas ocupaciones. La probabilidad de mantener
el patrón fermiónico original en todo el toro es `(1/4)^V`, V=L³;
la fidelidad con el estado completo inicial es **a lo sumo** esa cantidad,
pues además habría que recuperar el flujo original. No se identifica esta
cota con una fidelidad calculada del gauge.

El control t=0 anula este test de masa, como debe. Los puntos t múltiplo
de pi también requieren otro test; no se declaran estacionarios por eso.

## 3. Control massless: cota del paso magnético completo

En t=0, el resultado anterior reduce D_F al mismo rayo y E=0.
D_E actúa entonces como identidad. Sean `N_p=3 L³` las plaquetas
geométricas (una por sitio y plano positivo) y theta su ángulo magnético
común. Se escribe D_M(theta) como el producto ordenado de sus exponenciales.
No se necesita asumir conmutatividad entre planos para la cota siguiente.

Una plaqueta o su inversa cambia cuatro flujos por +/-1, sin cambiar
Gauss ni ocupaciones. Para L>=3, las `2 N_p` configuraciones obtenidas
desde flujo cero son distintas entre sí y de la inicial: su soporte
identifica el cuadrado orientado. Las fases JW tienen módulo uno; ningún
otro término de primer orden alcanza el mismo destino. El certificado
enumera esos destinos en L=3,4 y comprueba Gauss y su ortogonalidad en
la base de flujos. No diagonaliza ni recorta los rotores.

Cada generador `P_p+P_p†` tiene norma <=2, porque P_p es unitario.
La regla de derivación de un producto de exponenciales unitarias da
`||D_M''(theta)|| <= (2 N_p)²` para theta real. La fórmula integral del
resto de Taylor implica

`||D_M(theta)-I-i theta sum_p(P_p+P_p†)|| <= 2 N_p² theta²`.

Para cualquiera de los destinos de una plaqueta, la amplitud de primer
orden tiene módulo theta. Luego su amplitud total tiene módulo al menos
`theta-2 N_p² theta²`. Es estrictamente positiva si
`0<theta<1/(2 N_p²)`. No se extrapola esta cota a ángulos mayores.

Se ejecuta el punto fijado `theta=1/(8 N_p²)`, que deja una cota inferior
`3 theta/4`. Con epsilon=1, `g_E²=1/(2 theta)` y `g_M=1/g_E` se obtiene
ese ángulo y se respeta la relación del artículo. Aunque el ángulo eléctrico
dependa inversamente de theta, D_E actúa exactamente como identidad sobre
la entrada E=0 para todos esos valores. La expansión del estado completo
es por ello la de D_M(theta) Omega_occ; no se ha expandido D_E alrededor
de un parámetro singular.

| L | Plaquetas | Destinos ortogonales | theta | Probabilidad de salida: cota inferior por un destino |
| --- | --- | --- | --- | --- |
| 3 | 81 | 162 | 1/52488 | 1/4897760256 |
| 4 | 192 | 384 | 1/294912 | 1/154618822656 |

Son cotas racionales rigurosas obtenidas del resto, no probabilidades
ajustadas ni una simulación completa. La proyección sobre una configuración
de flujo del mismo sector es gauge invariante y tenía probabilidad cero
inicialmente. Su cota positiva rechaza también la estacionariedad física.
El tamaño diminuto de las cotas no es una estimación de un efecto observable;
solo se usa para demostrar que no son cero en estos puntos explícitos.

Apagar artificialmente el magnetismo con t=0 devuelve una referencia
estacionaria como control de identidad. No es un punto libre físico a
g_E finito de la familia con los dos acoplamientos relacionados.

## Cierre y límites

La referencia especificada pasa Gauss pero falla estacionariedad. No
cumple el requisito previo, así que no se intenta asignarle excitaciones
de vacío ni velocidades renormalizadas. No se sustituye por una mezcla
invariante obtenida promediando en tiempo: eso no seleccionaría el vacío.

El resultado rechaza este producto de ocupaciones como referencia en los
casos declarados. No rechaza Eon, todos los estados homogéneos, un estado
correlacionado con dressing, la existencia de un límite QED, ni la
universalidad de velocidades. A.int permanece abierta y no lista para lazos.

## Artefactos y reproducción

* Código permanente: [verify_eon_reference_state.py](../scripts/verify_eon_reference_state.py).
* Resultado exacto: [certificado JSON](2026-10-27--eon-reference-certificate.json).
* Especificación escrita antes de ejecutar: [contrato local](../theory/A_INT_EON_REFERENCE_CHECK.md).
* Barrido: `2026-10-27--eon-reference-verifier-sweep.tsv`.
* Manifiesto: `2026-10-27--eon-reference-inputs.sha256`.

Comando del certificado:
`python3 -B scripts/verify_eon_reference_state.py --output reports/2026-10-27--eon-reference-certificate.json`.
Un PASS del script significa que las identidades y testigos de rechazo
se verifican; **el candidato tiene FAIL de estacionariedad**.

La simulación determinista no contiene todas las fases del transporte ni
un circuito gauge completo. La prueba escrita explica exactamente por
qué esas fases no cambian el test de este candidato. Las hipótesis de
unitariedad de las plaquetas y conservación de ocupación gauge proceden
del modelo primario, no de una diagonalización independiente del código.
Las dos construcciones de masa son verificaciones de implementación,
no dos revisiones independientes. No se convocó revisión externa.

Validación final: los 44 verificadores del barrido terminan con código
cero; `text_integrity.py --check` devuelve cero problemas y
`git diff --check` pasa. El barrido registra el HEAD de base porque se
ejecutó con el certificado nuevo aún sin commit. El manifiesto adyacente
identifica los bytes de todos los verificadores, helper, runner,
especificación, PDF fuente y JSON de esta ejecución.
