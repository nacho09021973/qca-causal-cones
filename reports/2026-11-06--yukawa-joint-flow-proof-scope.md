# Flujo conjunto cerrado; prueba microscópica pendiente

2026-11-06. PRELIMINARY, autor; sin revisión independiente o promoción.
Contrato YUKAWA_JOINT_FLOW_GATE.md, hash previo
0ba5b29026f368bb0ff909a740b352348fd4113c9bca78708e8d8f8d0a964e86.

## Fuente y normalización comprobadas

Fei, Giombi, Klebanov, Tarnopolsky, *Yukawa conformal field theories
and emergent supersymmetry*, PTEP 2016, 12C105; PDF original adquirido
desde https://inspirehep.net/files/ffbb5687cb89ebffbb5cffb7e40dcb64.
Archivo sources/fei_giombi_klebanov_tarnopolsky_2016_yukawa.pdf,
SHA256 83cdf266ca7c6c03fb58872a527679acbe380bbc78d8ad2052ea20bca3470393.
Leídas pp.2–5: N=4Nf, acción (1.4), beta (2.1). Para dos Dirac,
N=8, y=g1, lambda=g2 y potencial lambda phi^4/24. Se retienen un
lazo y epsilon=0; no se traslada un fijo de 4-epsilon a cuatro dimensiones.

## Solución de las ecuaciones efectivas

En unidades donde la velocidad de la línea de referencia es c=1,
u=y², ell=log(Lambda0/Lambda), P=16pi²:

    u'=-14u²/P,
    lambda'=-(3lambda²+16u lambda-96u²)/P.

Son las beta de fuente cambiadas al sentido IR. Con r=lambda/u:

    r'=-(u/P)(3r²+2r-96)=-(u/P)(r+6)(3r-16).

Para u0>0 y r0>0, el campo apunta hacia r*=16/3 a ambos lados.
La solución permanece positiva y acotada entre r0 y r*. Además

    u(ell)=u0/[1+14u0 ell/P],
    integral_0^ell u(s)ds=(P/14)log[1+14u0 ell/P] -> infinito.

Al cambiar al tiempo tau=integral u/P, la ecuación de r es autónoma
y tau->infinito; la monotonía y el único cero positivo prueban
r->16/3. Si u0 y lambda0 son pequeños, ambos siguen pequeños en
esta trayectoria de un lazo, con potencial cuártico positivo.

Sustituyendo en los modos lineales de velocidades del informe anterior:

    Delta(ell)=Delta0 [1+14u0 ell/P]^(-1/21),
    E(ell)=E0 [1+14u0 ell/P]^(-13/21).

Delta=v1-v2, E=(v1+v2)/2-cb. Ambos tienden a cero. La velocidad
común sigue siendo el modo libre, no una constante fijada por el cálculo.
Se completa así la prueba de atracción del sistema de ODE congelado,
en la aproximación de un lazo y lineal en diferencias de velocidades.

La beta de acoplamiento se evalúa sobre la línea de referencia de
velocidades iguales. Perturbaciones de acoplamiento inducidas por las
diferencias no alteran el generador lineal de velocidad a este orden:
lo multiplicarían por otra diferencia. Esto no controla diferencias
finitas, no prueba simetría exacta de sabores fuera de la línea y no
justifica extrapolar a los valores 1/3 y 2/3.

## Por qué todavía no prueba el QCA

1. La masa crítica y el tadpole del Hamiltoniano de Wilson con escalar
   truncado no se han calculado ni demostrado que admitan la ventana
   sin gap requerida en el límite termodinámico.
2. El defecto CCR al corte no se ha acotado en el estado interactuante.
   Falta convergencia de observables al aumentar M.
3. La cota de Strang contiene S_LM y crece con volumen/corte. No es
   uniforme y no controla T->infinito a delta fijo. No se puede aplicar
   primero un límite RG infrarrojo infinito y después justificarlo con
   una cota de tiempo finito.
4. No se ha derivado el matching de parámetros y operadores del circuito
   a esta teoría ni acotado operadores generados por el paso Floquet.
5. La solución exacta de beta truncadas no demuestra que las beta exactas,
   ni un sistema microscópico concreto, mantengan esa trayectoria.

Estas son obligaciones sustantivas, no controles editoriales. Tampoco
constituyen una prueba de imposibilidad del mecanismo. El resultado
es EFFECTIVE_ONE_LOOP_LINEAR_ATTRACTION_SOLVED /
MICROSCOPIC_QCA_THEOREM_NOT_PROVED.

La instrucción de commit, push y fusión se condicionó a conseguir esa
prueba. No se activa la fusión ni se presenta la teoría efectiva como
teorema del QCA. No promoción automática. Los artefactos quedan locales.

## Verificación

scripts/verify_yukawa_joint_flow.py comprueba beta del cociente,
factorización, trayectoria Yukawa, soluciones de los dos modos y límites
con SymPy. Registro 2026-11-06--yukawa-joint-flow-verifier.txt.
La prueba de positividad y convergencia del cociente está arriba.
No revisión independiente ni novedad acreditada. git diff --check.
