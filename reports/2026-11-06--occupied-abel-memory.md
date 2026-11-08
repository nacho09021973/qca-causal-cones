# Suma Abel de la memoria con error temporal acotado

2026-11-06. PRELIMINARY, sin revisión independiente ni promoción.
Contrato OCCUPIED_ABEL_MEMORY_GATE.md, hash previo
1144fe75652357ba4c5c2b0a3be08b304d8eb077acdeb1141f6124f72149fb7c.
Mismos walks, ocupación, unidades e interacción del cálculo anterior.

## Cantidad calculada

Se evalúa S_rho(omega,k)=sum_(r>=1) rho^r exp(i omega r) K_(r-1)(k)
en k=0, omega=±pi/4, rho=0.5,0.65,0.8, para ambas especies,
incluidas sus tres derivadas físicas respecto de k. La suma finita usa
r<=24. Las matrices completas están en occupied-abel-memory.json.

Es una transformada regularizada del núcleo, no el polo de la respuesta:
el denominador completo requiere además el bloque instantáneo y la
convención de transformada de la recurrencia. No se sustituye S_rho
directamente por una corrección de velocidad. rho fija el amortiguamiento
temporal de la suma; no representa un baño ni un cambio de dinámica.

## Cota analítica de la cola

Para propagadores unitarios con cuatro modos, sum_x ||u_a(r,x)||_F²=4.
D_b(r,x)=||u_b(r,x)||_F²/4 es no negativa y suma uno. Por tanto
sum_x D_b²<=1 y Cauchy–Schwarz implica

    ||F_a,r(q)||_op <= sum_x ||u_a(r,x)||_F D_b(r,x) <=2.

Cada coordenada del soporte cumple |x_i|<=r. Luego
||partial_ki F||<=2r/sqrt3. Como ||partial_ki U||=1/sqrt3 para
los productos de desplazamientos fijados, K=-F U satisface

    ||K_(r-1)||<=2,
    ||partial_ki K_(r-1)||<=2(r+1)/sqrt3.

Son cotas uniformes conservadoras, no leyes de decaimiento. Sumando
las series geométricas, para la cola r>R:

    error <= 2 rho^(R+1)/(1-rho),
    error_derivada <= (2/sqrt3) rho^(R+1)
        [(R+2)/(1-rho)+rho/(1-rho)^2].

La segunda fórmula también se obtiene derivando la serie geométrica
de la cola y añadiendo su suma: controla el factor r+1. No requiere
suponer que los valores observados sigan decreciendo.

## Resultado y validación

| rho | cota norma operador, cola | cota por derivada física, cola |
|---|---:|---:|
|0.50|1.19209289551e-7|1.85828891613e-6|
|0.65|1.20169946379e-4|1.93273277480e-3|
|0.80|3.77789318630e-2|6.54350294423e-1|

Estas cotas cubren truncación temporal, no errores de punto flotante
ni la incertidumbre de la derivación física. Se empleó complex128 en
una malla 52³, sin alias espacial hasta r=24 (52>48). Se comprueban
normalización y primer retardo por coeficientes directos. La ventana
r<=8 coincide con el archivo anterior dentro de 1.716587549445839e-16.

El evaluador previo solo cambia para aceptar max_delay, conservando
su valor por defecto ocho y añadiendo la condición anti-alias.
No se sobrescribe su JSON anterior. Código nuevo permanente:
scripts/evaluate_occupied_abel_memory.py. Ejecución:

    /home/adnac/venvs/torch-gpu/bin/python scripts/evaluate_occupied_abel_memory.py

Salida en 2026-11-06--occupied-abel-memory.json y
2026-11-06--occupied-abel-memory-run.txt. git diff --check satisfactorio.

## Qué queda abierto

Estado: ABEL_MEMORY_SUM_WITH_TEMPORAL_TAIL_BOUND /
REAL_FREQUENCY_LIMIT_OPEN. Se ha pasado de una ventana sin control de
cola a una suma a resolución finita con cota explícita. Las cotas divergen
al tomar rho->1: no prueban existencia ni regularidad del límite real.
La precisión buena a rho=0.5 no equivale a precisión cerca de un polo.

La corrección de pendiente y la anchura espectral siguen sin determinar.
El obstáculo preciso es ahora una estimación de decaimiento/cancelación
del núcleo y de sus derivadas que permita retirar el regulador, o un
régimen de acoplamiento y tiempo en que una reordenación perturbativa
pueda justificarse. Extrapolar tres radios o aumentar R sin ese control
no resolvería la obligación matemática. No se afirma igualación de c.
