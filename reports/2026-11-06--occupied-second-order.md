# Segundo orden ocupado: término instantáneo y memoria pendiente

2026-11-06. PRELIMINARY; autor, sin revisión independiente.
Contrato OCCUPIED_SECOND_ORDER_GATE.md, hash previo
6d03e638244f18efdb97f0e55b8e8242b96d1712ac00d7fb2a6bf4bf6960f9a8.

## Resultado exacto a un paso

La identidad V† c_a(x) V=exp(-i chi N_b(x)) c_a(x), b!=a,
y la factorización entre especies del estado de fugacidades implican
que la respuesta de un paso es el propagador libre multiplicado por

    K_b(chi) = <exp(-i chi N_b(x))>
             = (1-p_b+p_b exp(-i chi))^4.

Los cuatro modos locales tienen ocupaciones Bernoulli independientes
en este estado. La evolución libre no cambia el promedio porque rho
es estacionaria. El resultado es exacto para un paso, para cualquier
chi y cualquier símbolo libre de las especies dentro del contrato.

Separando la fase media:

    exp(4i p_b chi) K_b(chi)
       =1-2p_b(1-p_b)chi²+O(chi³).

En el punto fijado p_b=1/2:

    K_b(chi)=exp(-2i chi) cos^4(chi/2).

La contracción centrada es 1-chi²/2+O(chi⁴). El coeficiente procede
de la varianza 4p_b(1-p_b), no de un desplazamiento de la pendiente.
Ambas especies reciben el mismo factor a un paso en este estado.
Los controles p=0 y p=1 dan respectivamente K=1 y K=exp(-4i chi):
sin fluctuaciones no hay contracción a un paso.

Segunda vía: enumeración exacta de las 16 ocupaciones de la especie
opuesta y suma de sus pesos. Coincide con el polinomio binomial.

## Por qué no es aún una anchura ni una velocidad renormalizada

No se puede sustituir G(t) por K^t G_0(t). La misma otra especie
evoluciona, conserva información y vuelve a interactuar. Renovarla
independientemente en cada paso cambiaría la dinámica especificada.
En volumen finito la evolución completa es unitaria; pérdida de peso
en el subespacio de operadores lineales puede retornar desde otros
operadores. Una contracción de un paso no demuestra decaimiento
exponencial irreversible ni localiza un polo complejo.

## Núcleo exacto que organiza el cálculo restante

En volumen finito y p1=p2=1/2, rho es identidad normalizada. Sea L
la evolución unitaria de operadores por conjugación con U_chi. P es
la proyección Hilbert–Schmidt sobre todos los aniquiladores lineales
de una especie y Q=1-P. Sus coeficientes dan la respuesta de una
partícula, salvo normalización fija y el factor retarded. La traza
cíclica hace coincidir las dos mitades del anticomutador.

Con A=PLP, B=PLQ, C=QLP y D=QLQ, y M_t=PL^tP, la eliminación
exacta del componente Q da

    M_(t+1)=A M_t + sum_(j=0)^(t-1) B D^j C M_(t-1-j),
    M_0=P.

Se deriva iterando q_(t+1)=C p_t+D q_t con q_0=0 y sustituyendo en
p_(t+1)=A p_t+B q_t. No supone Markov ni límite termodinámico.
En chi=0 la evolución libre conserva el subespacio lineal y su
complemento, de modo que B_0=C_0=0. Así el primer término de memoria
es de orden chi²: B_1 D_0^j C_1, además del coeficiente A_2 ya fijado
por K. Precisamente el orden al que empieza la contracción exige
incluir esta memoria para interpretar dispersión y coherencia.

Esta fórmula es una organización del cálculo, no una evaluación de
su núcleo para los walks fijados. Sigue pendiente calcularlo, tomar
los límites en orden controlado y extraer conjuntamente desplazamiento
y anchura. No se declara que las velocidades se acerquen o alejen.

## Verificación y alcance

scripts/verify_occupied_second_order.py, SymPy 1.14.0, nueve identidades
exactas: binomial frente a enumeración, coeficientes hasta orden dos,
factorización a media ocupación y límites vacío/lleno. Registro en
2026-11-06--occupied-second-order-verifier.txt. Una comparación inicial
trigonométrica no simplificó automáticamente; reescribir cosenos en
exponenciales resolvió la identidad sin cambiar el resultado.

Estado: SECOND_ORDER_INSTANTANEOUS_TERM_EXACT /
TEMPORAL_MEMORY_NOT_EVALUATED. Resultado parcial explícito, sin prueba
de polos, igualación, novedad ni puente RG de baja energía.
Código y derivación permanentes; sin cálculo científico efímero.
