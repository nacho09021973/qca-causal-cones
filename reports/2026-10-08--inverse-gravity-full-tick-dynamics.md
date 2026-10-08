# IG1c — influencia física espacial del tick completo

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato y código congelados antes del cálculo en
`10ddcf6aca8a73dcd07935fd2d473f5fb2e7d9a6`:
[contrato](../theory/INVERSE_GRAVITY_FULL_TICK_DYNAMICS_GATE.md),
[script](../scripts/verify_inverse_gravity_full_tick_dynamics.py).

## Resultado y evidencia

`FULL_TICK_ONE_STEP_PHYSICAL_INFLUENCE_PASS_AUTHOR_SIDE`.

Comando: `python3 -B scripts/verify_inverse_gravity_full_tick_dynamics.py`.
Código de salida 0, aritmética entera exacta; salida íntegra en
[certificado](2026-10-08--inverse-gravity-full-tick-certificate.txt).
Los imports utilizan los stencils permanentes de IG1a/IG1b. No se ha
modificado la regla, q, orden, ángulo ni el testigo después de calcular.
Evidencia propia, sin revisión independiente; no se promociona NOVELTY.

## 1. Testigo físico, no test de una puerta aislada

O=T_x^x en el cubo de origen (0,0,0); B=T_y^y en el cubo (1,1,1).
Sus soportes de registros son disjuntos y ambos preservan S=V=1.
En el tick fijado U=U_T U_R:

`O(1)=U† O U=U_R† O U_R`.

La desaparición de U_T es una identidad porque sus puertas son funciones de
palabras Z y conmutan con O. Es el Heisenberg del tick completo; no una
aproximación ni selección de puertas desde el resultado.

ψ0, definido en el contrato, pertenece al sector y tiene todos los R=1.
Existe en cada toro admitido: el promedio de V aplicado al producto X=1
es una suma no nula de estados de la base X con coeficientes positivos,
preserva S y todos los R, y normalizado da ψ0. No se aplicó este promedio
como paso de la dinámica ni se lo llamó vacío IR.

El certificado calcula la acción del bloque R sobre Oψ0, Bψ0 y OBψ0
mediante eigenvalores conjuntos de palabras conmutantes. No se diagonaliza
un Hamiltoniano o la unitaria many-body.

## 2. Dos formulaciones del cálculo

Por solapamientos completos de los stencils se obtienen cargas módulo 3 de
cada R afectado. Una formulación geométrica independiente las coloca en los
ocho vértices de cada cubo, con dos componentes opuestas por vértice:
para O, (0,-1,+1); para B, (+1,0,-1).
El script comprueba igualdad de ambos diccionarios de incidencias.

Los cubos solo comparten un vértice. Cada palabra sola afecta 16 R; en ese
vértice compartido una componente se cancela y las dos restantes no:

`M(O)=16`, `M(B)=16`, `M(OB)=30`.

Este conteo geométrico coincide con la enumeración de todas las puertas
influyentes, sin cortar una caja arbitraria ni omitir puertas del tick.
La periodicidad L≥6 múltiplo de 6 no identifica ninguno de estos soportes.

## 3. Acción exacta y norma en el sector

En Cψ0, un R no trivial tiene A_R=-1/2; los otros tienen A_R=1.
Con θ=π/3, las diferencias de fase son potencias de -i:

`O(1)ψ0 = exp[-iπ*16/2] Oψ0 = Oψ0`,

`O(1)Bψ0 = exp[-iπ*(30-16)/2] OBψ0 = -OBψ0`.

Como O y B conmutan al inicio,

`[O(1),B]ψ0 = -2 OBψ0`,
`||[O(1),B]ψ0||² = 4`.

Ambas palabras y el tick preservan el sector. El testigo vive por tanto en
la teoría física restringida, no solo en la Hilbert space sin constraints.
La cota general para el conmutador de dos unitarias es 2, así que esta norma
alcanza la cota y la norma del conmutador restringido al sector es exactamente 2.

O/B no son hermíticas; sus componentes real e imaginaria sí son observables
físicos. Si los cuatro conmutadores entre esas componentes fuesen cero,
también sería cero el de O/B. El test demuestra por ello influencia entre
observables físicos. No se especificó un protocolo de detector ni su contraste.

Si U fuese una fase en el sector, O(1)=O allí y este conmutador sería cero.
El resultado excluye esa posibilidad para el tick fijado. También prueba que
la evolución de un operador físico puede dejar de conmutar con un operador
en un soporte inicialmente disjunto en un tick.

## 4. Qué cierra y qué no

| Pregunta | Estado |
|---|---|
| ¿Puertas físicas no escalares? | IG1b PASS propio |
| ¿Tick completo no escalar en S=V=1? | IG1c PASS propio por testigo exacto |
| ¿Influencia espacial en un tick? | IG1c PASS propio, norma 2 |
| ¿Crecimiento sostenido o velocidad asintótica? | NOT_TESTED |
| ¿Estado/sector IR controlado y excitaciones gapless? | OPEN |
| ¿Dos polarizaciones, z=1 y cono común con materia? | OPEN |
| ¿Gravedad Einstein, fuente y escala física? | OPEN |

El estado mixto estacionario de IG1b conserva ese estatus. El estado ψ0 es
testigo algebraico del nuevo test y no sustituye un estado/sector IR.
No se infiere espectro relativista de esta influencia de un paso.

## 5. Frontera siguiente

El primer filtro dinámico del tick completo está cerrado al alcance declarado.
La siguiente pregunta de investigación es si existe un estado/sector de esta
regla con correlaciones y excitaciones colectivas controladas que permita
definir un límite IR. Antes de espectro se deben fijar observables, selección
de rama, orden de límites, escalas y errores; la referencia mixta no los aporta.

Un test multitik podría caracterizar influencia a tiempos finitos, pero no
resolvería por sí mismo esa selección IR. No se añade como continuación
automática ni se reemplaza la pregunta de gravedad por estudiar este circuito.
Los cierres anteriores y las restricciones de publicación permanecen.
