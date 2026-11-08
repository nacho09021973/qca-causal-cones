# Mediador común: atracción efectiva y circuito regularizado

2026-11-06. PRELIMINARY, autor; sin revisión independiente ni promoción.
Contrato YUKAWA_MEDIATOR_BRIDGE_GATE.md, hash previo
8000f69119a6ba8d1979bd7dcf4e1c57bace60ce39c748cdb440a13205a7abdc.
Usuario «haz las tres». No se identifica una construcción regulada
con una realización ya probada de su límite crítico.

## 1. Dos especies y un mediador

La teoría efectiva candidata es

    L=sum_a psi-bar_a(i gamma0 partial0-i v_a gamma_i partial_i)psi_a
      +(partial0 phi)^2/2-c_b²(grad phi)^2/2
      -m_b² phi²/2-lambda phi^4/4!
      -sum_a y_a phi psi-bar_a psi_a,

con masas fermiónicas, tadpole y otros contratérminos permitidos
incluidos al ajustar la superficie crítica. Son dos Dirac de cuatro
componentes, un escalar real, tres dimensiones espaciales. No se
impone igualdad de v1,v2,cb. El mediador interactúa con ambas especies.
Sus masas deben permitir una ventana efectiva sin gap; no basta elegir
masas desnudas cero para garantizarlo.

## 2. Flujo lineal de velocidades

Fuente primaria comprobada en esta sesión: sources/1102.0789v2.pdf
p.3, Ec.(18), Anber–Donoghue. Para un fermión sus funciones beta son

    beta(v)=y²(v-c_b)/(6 pi² c_b(v+c_b)²),
    beta(c_b)=y²(c_b²-v²)/(8 pi² c_b v³).

Para dos especies, a un lazo cada autoenergía fermiónica tiene su propio
escalar y fermión; la autoenergía escalar suma los dos bucles de sabor.
Esa aditividad extiende aquí las fórmulas, sin recalcular integrales.
No se usa una tercera especie virtual ni se impone intercambio exacto.

Sea ell=log(Lambda0/Lambda). Linealizando en diferencias alrededor
de un valor c>0, y tomando y1=y2=y sobre la trayectoria de referencia,

    d/dell (v1,v2,cb)^T = -A y² M (v1,v2,cb)^T + O(diferencias²,y^4),
    A=1/(24 pi² c³),
    M=[[1,0,-1],[0,1,-1],[-6,-6,12]].

M tiene eigenvalores 0,1,13. Los modos relevantes son

    Delta=v1-v2,       Delta'=-A y² Delta,
    E=(v1+v2)/2-cb,    E'=-13 A y² E.

La combinación 6v1+6v2+cb se conserva a este orden lineal. La velocidad
común queda libre. Con s(ell)=A integral_0^ell y(u)^2 du,
Delta(ell)=Delta(0)exp(-s), E(ell)=E(0)exp(-13s).
Así hay igualación asintótica si s->infinito; si la integral es finita
solo hay reducción parcial. No se presupone que todo acoplamiento débil
satisfaga la primera condición.

Segunda vía: para y1,y2 diferentes, escribir q_a=y_a² y sustituir las
filas por [q1,0,-q1], [0,q2,-q2], [-6q1,-6q2,6(q1+q2)]. La métrica
D=diag(6,6,1) simetriza el generador y

    v^T D M_q v=6q1(v1-cb)²+6q2(v2-cb)².

Con q1,q2>0, el único modo nulo tiene v1=v2=cb. Para acoplamientos
variables se requiere exposición acumulada suficiente de ambas aristas;
la positividad instantánea sola no garantiza convergencia asintótica.
Si una especie está desacoplada, no se obtiene universalidad.

En 3+1, Yukawa tiene dimensión canónica cero. Si la trayectoria crítica
débil satisface d(y²)/dell=-B y^4 con B>0, entonces
y²=y0²/(1+B y0² ell) y s=(A/B)log(1+B y0² ell) diverge. La atracción
es logarítmicamente lenta en escala de energía. Aquí B se mantiene
como coeficiente condicional: no se ha derivado su valor para dos
sabores ni el flujo conjunto con lambda. El flujo escalar y su cuenca
estable son una obligación para acreditar la trayectoria completa.
La dependencia y1=y2 al linealizar no impone igualdad inicial de
velocidades; lejos de la línea tampoco se supone que siga siendo exacta.

Esto establece atracción LOCAL a un lazo en la teoría efectiva,
condicionada a criticidad y al flujo de acoplamientos. No es una prueba
global desde v1=1/3,v2=2/3 ni una predicción del circuito a paso finito.

## 3. Realización local unitaria regularizada

Conservar el Hamiltoniano Wilson cúbico de la etapa anterior y añadir

    H_b=sum_x [pi_x²/2+m0² phi_x²/2+lambda0 phi_x^4/4!]
        +(cb0²/2)sum_<xy>(phi_x-phi_y)²,
    H_Y=sum_x,a y_a phi_x c_a(x)† beta c_a(x),

con lambda0>0 y parámetros desnudos ajustables. El término Yukawa es
escalar de masa psi-bar psi, no densidad N: esa diferencia respecto
al intento anterior es explícita. El potencial cuártico estabiliza
el campo en volumen finito incluso frente a la fuente fermiónica
acotada. Se debe ajustar tadpole para controlar <phi>.

Para obtener una dimensión local finita, fijar el oscilador truncado
n=0..M, phi_M=(a_M+a_M†)/sqrt2,
pi_M=(a_M-a_M†)/(i sqrt2). Dimensión local total 256(M+1).
Construir el Hamiltoniano usando estas matrices Hermíticas define un
modelo regularizado explícito. No equivale automáticamente a proyectar
cada potencia del Hamiltoniano infinito: esa prescripción está fijada.
Sus CCR tienen defecto de borde

    [phi_M,pi_M]=i[I-(M+1)|M><M|].

No se ignora el defecto. Convergencia al campo continuo exige control
de ocupación cerca del corte y de observables al aumentar M; no está
demostrada aquí. M finito no acredita por sí solo un escalar crítico.

Agrupar todos los términos onsite (incluidos H_Y y potencial) en una
capa y los enlaces fermiónicos y escalares en las mismas seis capas
de paridad anteriores. Dentro de cada capa los soportes son disjuntos.
La composición simétrica Strang tiene trece capas, puertas pares
unitarias exactas, alcance finito y periodicidad espacial dos permitida.
Para cada L,M finitos todos los generadores están acotados y vale la
cota de la etapa anterior con S_LM=sum_l||H_l||:

    ||U_delta^n-exp(-i T H_LM)||
        <= T delta² S_LM³ exp(delta S_LM)/3, T=n delta.

El estado de referencia es un ground state de H_LM en el sector de
medio llenado fermiónico. Existe por dimensión finita; no se afirma
unicidad, gap, simetría sin romper ni punto crítico termodinámico.
Es estacionario bajo H_LM, aproximadamente bajo el circuito solo en
el régimen controlado anterior. No se define un ground state Floquet
ordenando quasienergías. Los límites L->infinito, M->infinito,
delta->0 y masa crítica requieren análisis separado.

## Qué se ha logrado y qué falta

Se han definido mediador y circuito finito, derivado los modos de
atracción del flujo efectivo y obtenido una condición acumulada precisa.
No se ha probado matching crítico entre el circuito y esa teoría:
faltan trayectoria conjunta de acoplamientos, ajuste de masas/tadpole,
control de truncación y límites. No resultado de velocidad común
físicamente realizada, novedad o valor universal de c.

scripts/verify_yukawa_mediator_bridge.py, SymPy 1.14.0: comprueba las
cuatro derivadas de las beta de fuente, eigenvalores, modos izquierdos,
disipación ponderada y defecto CCR para tres cortes. Registro en
2026-11-06--yukawa-mediator-bridge-verifier.txt. La comprobación algebraica
no es revisión independiente ni simulación del circuito completo.
La búsqueda secundaria de la beta de acoplamiento no se utilizó como
prueba: el original adicional no fue accesible y B sigue condicional.
