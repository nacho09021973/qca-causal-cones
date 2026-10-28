# A.int — especificación previa de una referencia Eon v4

Fecha: 2026-10-27. Autorización: «especificar y comprobar el estado de referencia».
Base del repositorio: `01fd957ec1f4fd80afdf8281d86fd19a94e45bd5`;
el informe de viabilidad previo ya existe localmente, aún sin commit.
Esta especificación se escribe antes de ejecutar el certificado nuevo.
No es un contrato de lazo ni modifica la regla de Eon.

## Modelo, candidato y criterio fijados

Fuente: `biblioteca/arXiv-2205.03148v4.pdf`, pp.6–7, 12–13, 15, 19–23,
25–29. Se usa `U=D_M D_E D_F`, ecuaciones (34)–(37), con el transporte
corregido de v4 y orden temporal de derecha a izquierda.

* Red: toro cúbico `(Z/LZ)^3`, L>=3; controles ejecutables L=3,4.
  No hay frontera externa ni carga neta.
* Celda: cuatro modos fermiónicos; registros gauge enteros sin truncar,
  con los dos extremos de cada enlace opuestos. No se sustituye U(1) por
  un grupo finito. Orden local de modos 0,1,2,3 como en el artículo.
* Magnetismo: exponencial exacta de plaquetas, ecuación (21), extendida
  por (36). No se usa la aproximación de dos subpasos (26).
* Sector: `G_x = div E_x + N_x - 2 = 0` para todo sitio.
* Único candidato: `Omega_occ = tensor_x |1100>_(3,2,1,0) tensor |E=0>`.
  Ocupa los modos 2,3 y deja vacíos 0,1. La identificación de esas
  etiquetas con partículas físicas no se presume. Es un candidato de
  ocupaciones locales, no un llenado de bandas negativas.

Criterios: primero Gauss; después estacionariedad de su densidad bajo
el **paso completo**, no solo bajo subpasos. Una diferencia de probabilidad
o de un observable gauge invariante de ocupación basta para rechazarlo.
Un PASS de estacionariedad no bastaría para llamarlo vacío: seguiría
pendiente su selección física y espectral.

Test principal: t=m epsilon=pi/4, epsilon=1, g_E=g_M=1, en unidades de
red para este test de referencia. Las ecuaciones de acoplamiento de p.19
se respetan. No se interpreta este punto como límite de acoplamiento débil.
También se deriva la dependencia exacta en t, si el certificado lo permite.

Control massless: t=0, ángulo magnético común
`theta=1/(8 N_p²)`, con `N_p=3 L³` plaquetas geométricas únicas. Tomar
epsilon=1 y `g_E²=1/(2 theta)`, `g_M=1/g_E` respeta la misma relación.
Se permite una cota de Taylor rigurosa del **paso completo**, usando normas
de operadores acotados, sin truncar el rotor ni diagonalizar un registro finito.

## Certificado y segunda vía

Artefacto permanente: `scripts/verify_eon_reference_state.py`.
La parte determinista sigue ocupaciones y flujos de todos los swaps del
transporte en la entrada declarada. No calcula sus fases JW: debe justificar
por qué basta una única configuración hasta la masa, y verificar que B
actúa allí por fase. No puede reutilizar esa simplificación en entradas
que produzcan superposición.

La masa local se comprueba por dos construcciones exactas: circuito de
dos modos con fSWAP y segunda cuantización por menores del bloque
unipartícula. Se comprueban Gauss, norma, ocupación y proyección sobre el
patrón inicial. La invariancia de ocupaciones bajo D_E y D_M se justifica
desde sus generadores; no se implementa una simulación total del gauge.

En t=0 se enumeran los flujos de una sola plaqueta y sus inversos, se
comprueban Gauss y ausencia de colisiones para L=3,4, y se conserva la
demostración analítica de la cota del resto. Los controles negativos deben
detectar una actualización de flujo con signo incorrecto y la omisión de
un swap relevante. Un control t=0 con magnetismo apagado es solo una
identidad de control; no se presenta como un punto físico a g_E finito.

Salida prevista: certificado JSON, informe con hipótesis y límites,
manifiesto de fuentes/código y barrido de todos los verificadores.
Máximo: un candidato. Si falla, STOP para este candidato; no reemplazarlo
por una mezcla estacionaria, un Hamiltoniano padre u otro circuito.
No se estudian velocidades, propagadores ni lazos en este encargo.
