# Ajuste, corte bosónico y límite infrarrojo: avances y alcance

2026-11-06. PRELIMINARY, autor, sin revisión independiente o promoción.
Contrato YUKAWA_CRITICAL_CUTOFF_IR_GATE.md, SHA256 previo
765eeefb67954308c79f3e609167d510916525ba6bb48938f377b8d8e382d05a.
Se conserva la prescripción truncada anterior; no se sustituye por
Galerkin sin declarar el cambio. Biblioteca local ausente. Derivación
propia sobre el Hamiltoniano explícito, no prueba por informes de IA.

## 1. Primer ajuste estático explícito

Escribir W(k)=sum_i(1-cos k_i), S(k)=sum_i sin² k_i. Para un campo
uniforme phi, las bandas fermiónicas son ±E_a(k,phi), dobles, donde
E_a²=v_a²S+(W+m_a+y_a phi)². La contribución de bandas negativas a
la energía por celda es -2 sum_a integral_BZ E_a. Medida normalizada.

En m_a=phi=0, las dos primeras derivadas son W/E_a y v_a²S/E_a³.
Para imponer tadpole nulo a este orden, la fuente desnuda candidata es

    h0=2 sum_a y_a integral W/E_a.

No hay una simetría quiral exacta de Wilson que permita omitirla sin
comprobación. La curvatura fermiónica es negativa:
-2 sum_a y_a² integral v_a²S/E_a³. El lazo escalar de lambda phi^4/24
aporta +(lambda/4) integral 1/omega(k), omega²=2 cb² W, cb=1.
La compensación estática candidata es

    m_b0²=2 sum_a y_a² integral v_a²S/E_a³
                          -(lambda/4) integral 1/omega.

Se evalúan estas integrales por mallas de puntos medios 24³,48³,96³.
Son cuadraturas del toro, no condiciones antiperiódicas impuestas al
escalar físico. Las singularidades integrables en k=0 no se muestrean.
En 96³ los coeficientes son:

| cantidad | v1=1/3 | v2=2/3 |
|---|---:|---:|
| h0 por y_a |1.95801432416|1.87040288527|
| m_b0² por y_a² |0.104210112091|0.169314011552|

El coeficiente escalar por lambda es -0.113832549973. Valores numéricos
preliminares SIN cota rigurosa de cuadratura; las tres mallas y sus
diferencias se conservan en JSON. Las derivadas del determinante se
comprueban además simbólicamente. La curvatura estática de un lazo no
demuestra susceptibilidad crítica exacta ni posición de transición.

Faltan las autoenergías de masa fermiónica y correcciones superiores.
Además Wilson permite términos impares del potencial escalar: controlar
solo la fuente y la masa no prueba la ausencia de un término cúbico
relevante. El potencial efectivo y los contratérminos permitidos deben
cerrarse, o una simetría microscópica deberá justificar su exclusión.
No se afirma que dos ajustes basten para alcanzar criticidad.

A escala mu~1/L, condiciones necesarias de ajuste, por dimensiones
canónicas, incluyen m_f,R L->0, m_b,R² L²->0, h_R L³->0 y
mu_quim,R L->0; para un cúbico residual kappa_R, kappa_R L->0.
Correcciones logarítmicas pueden modificar la precisión requerida.
Estas condiciones no prueban que existan parámetros desnudos que las
satisfagan simultáneamente. La superficie crítica sigue OPEN.

## 2. Corte bosónico: condición suficiente y límite de la energía media

Para el oscilador truncado, el defecto CCR es
(M+1)|M><M|. Si en el estado considerado <n_x^s><=C_s uniforme,
s>1, entonces su expectación en valor absoluto es <=
C_s(M+1)/M^s y tiende a cero. El resultado depende de demostrar
esa cota de momentos en los estados críticos, no solo de elegir M grande.

Un primer momento acotado NO basta: la mezcla con probabilidad
1/(M+1) en |M> y el resto en |0> tiene <n><1 pero defecto CCR uno.
Este caso límite impide convertir una cota media en control canónico.

En el espacio no truncado, para el proyector que descarta n_x>M en
cualquier celda, la desigualdad de Markov y la unión dan

    Prob(al menos una celda fuera del corte)<=L³ C_s/(M+1)^s.

Para un estado puro, normalizar la proyección cambia su matriz densidad
en norma traza como máximo 2 sqrt(probabilidad descartada). Esto acota
expectaciones de observables acotados. Para los operadores phi, pi y H
no acotados se necesitan momentos adicionales o estimaciones de formas.
La cola pequeña tampoco identifica por sí sola el estado fundamental
del Hamiltoniano construido con potencias de phi_M con el proyectado.

Por tanto hay un criterio comprobable de corte, pero falta probarlo
uniformemente en L y cerca de criticidad. No convergencia bosónica
declarada. El defecto no se ignora en una simulación finita.

## 3. Circuito: un límite diagonal controlable, bajo hipótesis explícitas

Para parámetros desnudos acotados y lambda0>0, las normas de phi_M y
pi_M son O(sqrt M), la del cuártico O(M²). El Yukawa tiene norma
O(sqrt M) por celda porque la parte fermiónica está acotada. Por ello
S_LM=sum_l||H_l||<=C L³ M² para M>=1, con C dependiente de parámetros.
Si estos crecen con los ajustes, debe incluirse su crecimiento; no se
asume una constante uniforme sin esa condición.

La cota Strang previa es error<=T delta² S_LM³ exp(delta S_LM)/3.
Una secuencia suficiente explícita, CONDICIONAL, es

    T=L, M=ceil(L²), delta=L^-12.

Entonces delta S=O(L^-5) y T delta² S³=O(L^-2). Si además se dispone
de segundo momento uniforme por celda, la probabilidad descartada es
O(L^-1). El defecto CCR local esperado es O(L^-2). Así la cota de
circuito puede mantenerse pequeña a tiempos que aumentan como L;
ya no se aplica una estimación a T fijo a un T infinito sin justificarlo.

Pero esto es una FAMILIA de circuitos: dimensión local y paso cambian
con L. No prueba el infrarrojo de un único QCA con M y delta fijos.
Tampoco es un teorema de matching: la hipótesis de momentos, los ajustes
críticos y el límite efectivo siguen pendientes. La secuencia solo
resuelve la compatibilidad algebraica de los errores si se cumplen.

Para un QCA fijo haría falta controlar los operadores Floquet relevantes
y el posible calentamiento, o construir otra protección exacta; esa
estimación no está disponible aquí. El control a tiempo creciente de
una familia no debe promocionarse a universalidad de un automáta fijo.

## Verificación y decisión

scripts/verify_yukawa_ir_scaling.py: ocho identidades exactas de escalas,
límites y contraejemplo al primer momento. Una igualdad algebraica
inicial requirió comparar la diferencia simplificada; parámetros sin
cambios. Registro 2026-11-06--yukawa-ir-scaling-verifier.txt.
scripts/evaluate_yukawa_static_counterterms.py: dos derivadas exactas,
cuadraturas persistidas en 2026-11-06--yukawa-static-counterterms.json;
registro homónimo -run.txt. Ambos ejecutados con el entorno torch-gpu
existente, Python/SymPy/NumPy; sin código científico efímero.

Salida: STATIC_ONE_LOOP_TUNING_CANDIDATES /
CONDITIONAL_OCCUPATION_CUTOFF_BOUND /
DIAGONAL_CIRCUIT_ERROR_SCHEDULE. No prueba crítica termodinámica,
convergencia bosónica completa o QCA fijo infrarrojo. Resultado
PRELIMINARY; la condición para fusionar con main no se ha satisfecho.
