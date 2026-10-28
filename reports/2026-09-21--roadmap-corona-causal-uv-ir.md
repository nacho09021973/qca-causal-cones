# Hoja de ruta — corona causal: IR, UV y frente inhomogéneo

> **Nota — 2026-10-28.** Hoja de ruta histórica. Planificación vigente: [hoja de trabajo 28 oct 2026](../hoja%20de%20trabajo%2028%20oct%202026.md) y la guía de lectura al principio de `state/CURRENT_STATE.md`.

Fecha: 2026-09-21  
Inicio operativo: 2026-09-22  
Rama: `research/b-infinity-post-s4-gate`

## Addendum de prioridad — 2026-09-22

La propuesta [FRONT-RESOURCE SCALING](2026-09-22--front-resource-scaling.md)
abre una ruta teórica acotada: FR1, inventario estructural de las potencias
ya demostradas; FR2, contrato de optimización del encoder; FR3, eventual
operador límite. La referencia de Liu–Chen se incorpora como antecedente
variacional y del mecanismo de colas por corte duro.

Esta incorporación no activa el ratio inhomogéneo ni los pasos E/AdS
descritos abajo. Ese itinerario se conserva como planificación anterior,
sujeto al estado vigente y a sus contratos. En esta rama, C2c obtuvo
`C2C_PASS` para los dieciséis pares originales tras la revisión independiente del
[análisis reparado](2026-09-22--c2c-structural-scope.md) y su
[acta de revisión](2026-09-23--c2c-independent-review.md). FR2 y FR3 siguen
abiertos. La óptima deriva media
del CTQW citado no certifica optimalidad de nuestra señal.

Para esos dieciséis pares, con el corte duro y el protocolo congelados,
`Q_N = <d_P,E d_P> = Theta(N^-3)` con coeficiente líder uniformemente positivo.
La fuente local satisface `d_P+d_Q=d` y
`||E^(1/2)d|| <= 18 N^4 exp(-JN)`; por ello las amplitudes proyectadas se
compensan en Bob y los bloques tienen líderes relativos `+1:+1:-2`.
La prueba conserva los cruces entre bandas para los detectores de rango uno.
Las coincidencias líderes forman a lo sumo ocho familias; esta agrupación
no establece equivalencia exacta del walk ni igualdad a `N` finito.
`M=I` aplica una fase espacialmente variable y no representa ausencia de
encoder. El barrido exploratorio
`N=12,...,48` carece de código y salida conservados: `[UNVERIFIED]`, fuera
de los argumentos. C2c queda cerrado en este alcance; la atribución física
exclusiva IR/UV y las extensiones a otros protocolos no se siguen de él.

## Estado de partida

- El resultado plano CJWW (5.15) está cerrado dentro de su clase y protocolo
  congelados.
- La respuesta plana tiene la forma
  \[
  \delta(N)=|C(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2})).
  \]
- La extensión inhomogénea/AdS sigue `STOPPED_UNPROVEN`.
- H1 permanece abierto; el cuello de botella es
  `H1c_LOCALIZATION (L')`.
- `H1-SR` está probado bajo el contrato de beta congelado; H1a/H1b están
  escritos pero sin revisión independiente.
- `E0` y la estabilidad de la potencia `13/2` siguen abiertos.

No se heredan como certificados los PASS provisionales de exploraciones
anteriores.

## Qué ocurre en el ultravioleta

Hay que mantener separadas tres afirmaciones:

1. **Propagador UV/microscópico.** El kernel exacto tiene amplitudes fuera de
   la bola relativista IR pero dentro del soporte causal microscópico. Esto
   está cerrado para el walk plano.
2. **Respuesta operacional IR.** Con preparación, codificación y detección
   IR-admisibles, la respuesta plana puede ser no nula aunque quede fuera del
   cono IR, con supresión no perturbativa. El resultado no se reduce a una
   señal UV de un protocolo broadband.
3. **Realización física.** No está establecida. Ninguna de las dos anteriores
   demuestra que exista un sustrato natural que realice el mecanismo.

En el análisis de control IR, la fuga absoluta UV tiende a cero al reducir la
ventana IR, pero la mezcla relevante no desaparece automáticamente: los
bloques IR–UV y UV–IR dominan el residuo fuera del bloque IR–IR, mientras que
el bloque UV–UV es relativamente menor en el régimen estudiado. Esto no
autoriza a llamar UV a la información ni al señalamiento. Significa que la
extensión inhomogénea debe controlar explícitamente las visitas al complemento
dominante y las transiciones entre ventanas de momento.

Para H1c, por tanto, hay tres posibilidades que deben mantenerse abiertas:

- la contribución UV/complementaria queda en un remainder estrictamente menor
  que el término IR dominante;
- la mezcla IR–UV cambia el coeficiente o la potencia, aunque conserve la
  tasa exponencial;
- una contribución fuera de la ventana local tiene la misma tasa o una tasa
  dominante, en cuyo caso la extrapolación de la fórmula plana falla.

No se debe asumir por adelantado cuál de las tres ocurre.

## Día 1 — 22 de septiembre: infraestructura y contrato

1. Inspeccionar los verificadores existentes y el manuscrito plano, sin crear
   código nuevo inicialmente:
   - `scripts/verify_directional_saturation.py`;
   - `scripts/verify_regional_directional_asymptotics_gate.py`;
   - `scripts/verify_regional_laplace_coefficient_gate.py`;
   - §§7.1–7.7 de `papers/ir-corona/ir-corona.md`.
2. Determinar si existe una ruta de reutilización para evaluar directamente
   el operador inclinado inhomogéneo, evitando calcular colas de tamaño
   `e^{-K_*N}` por resta numéricamente inestable.
3. Congelar antes de ejecutar:
   - `U_N=C_N(x)D`;
   - la deformación `\vartheta` y su regularidad;
   - el tilt complejo;
   - la definición exacta de `tail_flat` y `tail_inhom`;
   - la ventana IR y el tratamiento del complemento UV;
   - los valores de `N` y la precisión numérica.

**Salida del día:** contrato de test o `NO_INFRAESTRUCTURA_REUTILIZABLE`.
No se declara ningún resultado científico todavía.

## Gate exploratorio — ratio inhomogéneo/plano

Si la infraestructura lo permite, evaluar un observable estable, idealmente en
la representación inclinada:

\[
R_N=\frac{\operatorname{tail}_{\mathrm{inhom}}(N)}
           {\operatorname{tail}_{\mathrm{flat}}(N)}.
\]

La predicción exploratoria de estabilidad es `R_N=1+O(N^{-1})`, pero el test
no confirma por sí solo H1 ni E0.

### Criterios falsables

- `R_N` se aleja sistemáticamente de 1: detener la extensión en esta
  formulación.
- La aproximación es claramente peor que `O(N^{-1})`: detener y revisar el
  contrato o la hipótesis de estabilidad.
- Los datos son compatibles con `1+O(N^{-1})`: autorizar únicamente el paso
  a la auditoría analítica de H1c.

Un ajuste numérico no puede promover `E0`, identificar la potencia `13/2` ni
probar un coeficiente líder.

## Gate H1c — localización y UV/complemento

El objetivo no es demostrar una vaga “decadencia UV”, sino controlar el
producto inhomogéneo completo:

- persistencia del proyector de Riesz en cada ventana local;
- transiciones `P↔Q` y visitas al complemento;
- cambios de momento inducidos por la moneda espacial;
- conexiones entre las ocho vecindades de saddle;
- ausencia de una falsa hipótesis de conservación del momento;
- suma absoluta compatible con
  \[
  e^{-N\varphi_*}|T_n|
  \le C N^{-13/2}\frac{(C'/N)^n}{n!}.
  \]

Sólo si este control se prueba y recibe revisión independiente puede H1 pasar
a `PASS`.

## Gates posteriores

Mantener separados:

1. estabilidad de la tasa `K_*`;
2. estabilidad de la potencia `13/2`;
3. control y no nulidad del coeficiente `C(\theta_N)`;
4. ensamblaje `E0` de la extensión completa.

El orden correcto es `infraestructura → contrato → test exploratorio → H1c →
tasa/potencia/coeficiente → E0`. Ningún PASS local de una etapa cierra las
siguientes.

## Reglas de parada

- No llamar “UV” a una respuesta sólo porque procede de bloques fuera de la
  ventana IR.
- No interpretar la fuga UV de un encoder como señal operacional.
- No convertir `N\to\infty` en un límite continuo `a,\tau\to0`.
- No reclamar una realización física ni un resultado sobre la naturaleza.
- Si la infraestructura no permite un test estable sin código nuevo, detenerse
  y redactar primero un contrato de implementación antes de programar.

## Estado que debe conservarse al cierre

`FLAT_IR_CORONA = CLOSED_IN_FROZEN_CLASS`  
`C2c = C2C_PASS (16 pares congelados)`  
`H1 = OPEN`  
`H1c_LOCALIZATION (L') = OPEN (frente activo)`  
`E0 = OPEN_AT_STOP`  
`E/AdS = STOPPED_UNPROVEN`  
`UV_INTERPRETATION = CONTROLLED_SEPARATION, NOT_SIGNALING_CLAIM`
