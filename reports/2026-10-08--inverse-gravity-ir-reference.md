# IG1d — la referencia tracial no aporta respuesta lineal dinámica

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato/código previos en `dd40dee98776e7e83f5f5674ca54ba3e7900cf1f`:
[contrato](../theory/INVERSE_GRAVITY_IR_REFERENCE_GATE.md),
[script](../scripts/verify_inverse_gravity_ir_reference.py).
Se precisa en el contrato el signo del Hamiltoniano auxiliar: W=1 minimiza
-A_W, no A_W. La condición R=T=1, tests, tick y definición de respuesta
permanecen exactamente los congelados; no se ajusta el test desde resultados.

## 1. Ejecución y alcance

Comando: `python3 -B scripts/verify_inverse_gravity_ir_reference.py`.
SymPy 1.14.0, aritmética exacta, tolerancia cero, código de salida 0.
Salida íntegra en [certificado](2026-10-08--inverse-gravity-ir-reference-certificate.txt).

Resultado: `TRACIAL_REFERENCE_RESPONSE_NULL / TERMWISE_VACUUM_INCOMPATIBLE`.

Los controles 3×3 verifican identidades algebraicas, no simulan el tick
espacial. Las afirmaciones sobre el sector many-body se demuestran abajo;
no se transfieren del control qutrit a la red por analogía. Evidencia propia,
sin revisión independiente y sin claim de novedad.

No se modifica la dinámica, no se añade materia ni se hace una búsqueda
espectral. IG1c y su influencia espacial de un tick siguen válidos.

## 2. Teorema de respuesta nula para la referencia fijada

En cada toro admitido, restringir a H_P=im(P), dimensión d_P>0.
ρ_L es I_P/d_P; U, A y B preservan H_P. Por traza cíclica:

`Tr(ρ_L [B,A(n)]) = (Tr_P(B A(n))-Tr_P(A(n) B))/d_P = 0`.

Por tanto la susceptibilidad discreta fijada en el contrato es exactamente
cero para todo n, todos los observables físicos y todos los volúmenes admitidos.
La prueba no usa el detalle de puertas, ni un logaritmo de U, ni el espectro.

**Segunda derivación:** una perturbación unitaria interna deja el estado
invariante, `e^-iεB ρ_L e^iεB=ρ_L`. La evolución posterior también lo deja
invariante. La expectativa no cambia para ningún ε; la respuesta se anula
a todos los órdenes. Cualquier límite termodinámico de estas respuestas
exactamente nulas seguirá siendo nulo, si está bien definido.

Fuentes que cambien P, canales no unitarios o perturbaciones de la regla no
están incluidas. Tampoco se afirma que toda referencia a temperatura finita
tenga esta propiedad; la causa aquí es la identidad en el sector físico.

## 3. Por qué no contradice la influencia espacial

IG1c probó `C=[U† O U,B]` no nulo dentro de H_P. Un operador de traza cero
puede tener norma positiva. Además, como ρ_L es fiel en H_P,

`Tr(ρ_L C†C)>0`

para ese C no nulo en volumen finito. Su valor no se calcula aquí.
El control qutrit del script ofrece un ejemplo exacto de respuesta media
nula y conmutador cuadrático positivo; sus valores no son valores de la red.

Las correlaciones no ordenadas pueden ser no triviales. Para un observable
hermítico A, en cualquier base de eigenvectores de U|H_P,

`C_A(n)=d_P^-1 sum_ab |A_ab|² exp[i n(φ_a-φ_b)]`.

El intercambio a↔b hace C_A(n) real y par. En una representación espectral
de quasifases hay pesos simétricos de signo opuesto, módulo 2π. Esta identidad
no ordena energías, no selecciona una rama positiva y no cuenta modos IR.
Por ello no se puede usar la referencia tracial como un vacío de respuesta
gravitatoria sin una selección de estado/sector distinta y justificada.

## 4. El vacío de mínimos de cada término no existe

El par físico certificado en IG1b satisface `TR=ω^-1 RT`, ω≠1.
Si un vector no nulo satisficiera Rψ=Tψ=ψ, resultaría simultáneamente
TRψ=ψ y ω^-1 RTψ=ω^-1ψ, contradicción.

Así, no existe un estado que tenga W=1 para todas las palabras R/T del
tick. En el Hamiltoniano auxiliar `H_aux=-sum_W A_W`, W=1 minimiza cada
término -A_W, por lo que la receta de un vacío sin frustración término a
término queda descartada. No se ha introducido H_aux como generador del tick.

Este argumento no excluye estados fundamentales correlacionados de H_aux,
ni eigenestados estacionarios de U. Tampoco demuestra que H_aux sea
conservado por U, tenga gap o tenga un límite gravitatorio. Esas propiedades
no se heredan al escribirlo como auxiliar.

## 5. Decisión de diseño y frontera

Se conserva ρ_L como referencia algebraica de control. Se descarta su uso
para acreditar los polos de respuesta lineal buscados con fuentes unitarias
internas. Se descarta también la selección de vacío por W=1 simultáneo.
No se descarta el tick ni toda emergencia gravitatoria en otra referencia.

Estado: `IR_STATE_SELECTION_OPEN`; no hay estado IR seleccionado.
La referencia fija no cumple la ruta de respuesta adoptada, y la alternativa
correlacionada no está construida. No procede calcular una dispersión
gravitatoria bajo esa carencia ni escoger el eigenestado de menor quasifase
como si fuese un estado fundamental canónico.

La siguiente pregunta concreta es: **¿existe un criterio local, físicamente
justificado, que seleccione un estado correlacionado estacionario de este
tick, con respuesta dinámica no nula y control del régimen de excitaciones?**
La mera existencia de eigenestados en volumen finito no resuelve el problema.
Si no se obtiene ese mecanismo, se detiene esta ruta de control y se vuelve
al diseño de la arquitectura; no se dedica un barrido al circuito por sí mismo.

No se cambia la meta Einstein a una dinámica térmica, ni se añaden un
Hamiltoniano o un ángulo pequeño a posteriori bajo el mismo contrato.
