# Plan de cierre escalar de AliceLayersB

Plan prospectivo del 2026-11-11, solicitado por el usuario. No añade pruebas ni
cambia CONTRACT.md, Targets.lean o la fuente congelada. Estado inspeccionado:
HEAD ce07813fa2135deb3a993075efb6f0935b56d458. Prevalece sobre los siguientes
pasos históricos de ROADMAP_2026-10-30.md; STATUS.md conserva los registros.

## Punto de partida y objetivo

ZeroModeDepth.lean conecta la amplitud original con geometricZeroModeSum sobre
las capas activas, conservando su fase normal. La estimación disponible es
(Cfinite+Cdepth)/(N³√N)+Cdual/N⁴ para N≥1 y frequencyNorm η≤π/6.
Es una cota absoluta: todavía no proporciona el E normalizado de Targets.lean.
Este plan parte de la lectura del código y del estado; no se ha repetido aquí
la compilación de las verificaciones históricas.

Faltan retirar la fase normal, completar todas las profundidades con sus colas
y ensamblar los testigos uniformes de AliceLayersB. La revisión bibliográfica
aportada no se adopta como prueba ni como razón para introducir modelos de
polímeros, matrices de transferencia o gauge fixing.

## 1. Envolvente uniforme del perfil y sumabilidad

Pregunta: ¿qué cota polinómica en δ domina ‖psi δ τ‖ para toda τ y δ≥0?
Derivar una cota desde el integrando y su soporte, reutilizando la integrabilidad
existente. No hace falta calcular la integral exacta si basta una cota polinómica.
Demostrar la sumabilidad de depthTerm y de su versión multiplicada por δ,
uniformemente para 0≤θ<1 al peso criticalTilt>0.

Entrega prevista: AliceLayers/DepthEnvelope.lean y registro de verificación.
Cierre: constantes finitas independientes de τ y θ; sumabilidad explícita,
sin usar el valor por defecto de tsum. Segunda comprobación: δ=0 y τ=0,
con comparación directa con el integrando real no negativo.

## 2. Eliminación de la fase normal

Pregunta: ¿la diferencia entre geometricZeroModeSum y la misma suma sin fase
está acotada por Cphase*|normalFrequency η|, uniformemente en N≥1?
Reescribir exactamente layerGlobalFactor como
exp(-i*normalFrequency η*δ) exp(-criticalTilt*(θ+j)). Usar
‖exp(-iu)-1‖≤|u| y la envolvente ponderada por δ del bloque 1.

Entrega prevista: AliceLayers/NormalPhase.lean. Definir el error con signo
explícito y demostrar una identidad exacta antes de estimarlo.
Cierre: cota sobre todas las capas activas sin exigir que sus índices sean
consecutivos. Segunda comprobación: normalFrequency η=0 da error exactamente
cero, y la identidad reconstruye la suma original.

## 3. Todas las profundidades: índices omitidos y colas

Pregunta: ¿la suma sin fase sobre capas activas difiere de sPlus en
O(N^(-1/2)), uniformemente en θ_N y τ? Es la cota suficiente, no se exige una
tasa más fuerte para cerrar el objetivo.

Primero identificar la imagen finita J_N del índice natural, con inyectividad
y profundidad δ_j=(θ_N+j)/√3. Escribir la diferencia con sPlus como la suma
sobre ℕ\J_N, justificando la descomposición por la sumabilidad del bloque 1.
No identificar J_N con un intervalo sin prueba.

Separar dos situaciones:

- Profundidades fuera del intervalo geométrico 0≤δ≤N/2: probar una cota
  de cola exponencial con factor polinómico, uniforme en θ_N. Convertirla
  después en la potencia de N requerida, con constantes y umbral explícitos.
- Planos enteros dentro de ese intervalo cuya capa es vacía: un perfil continuo
  puede ser no nulo aunque la capa discreta esté vacía. Construir un punto
  entero del plano mediante coordenadas equilibradas y acotar su distancia
  tangencial. Derivar qué impone la vaciedad sobre δ(N/2-δ). Investigar con esa
  desigualdad la separación entre una franja superficial de profundidad pequeña
  y una franja profunda amortiguada por el peso exponencial. Estas conclusiones
  son metas pendientes, no hechos ya probados.

Entrega prevista: AliceLayers/DepthCompletion.lean; si el tamaño lo aconseja,
separar geometría de vaciedad y estimación de colas en módulos propios.
Cierre: identidad con signo y cota total Ccompletion/√N. Segunda comprobación:
θ=0, profundidad cero y capas de borde; verificar que la partición cubre todo
índice omitido sin duplicación. No presuponer separación positiva uniforme de
θ_N respecto de cero.

Si una capa vacía produce una contribución incompatible con la cota, detener
esta vía y registrar la obstrucción. No añadir una hipótesis de no vaciedad al
objetivo ni omitir el término para continuar.

Ejecución posterior del bloque 3: la implementación usa DepthGeometry.lean y
DepthCompletion.lean. Se ajusta el método de control de la cola previsto arriba:
el primer momento sumable ya demostrado proporciona una cota O(1/N), que basta
para el objetivo; no se ha probado ni se necesita aquí la cota exponencial más
fuerte sugerida inicialmente. Esto cambia la ruta de prueba, no el contrato ni
la cota exigida. El punto entero construido tiene radio tangencial al cuadrado
≤3; toda profundidad omitida satisface δ≤12/N o δ>N/4. Los errores de las dos
regiones se controlan explícitamente. Resultados y verificación en STATUS.md.

## 4. Normalización del resto

Pregunta: ¿las cotas absolutas existentes implican la cota del E de Targets.lean?
Probar boundaryResource>0 desde su integral y las constantes exactas: controlar
el signo de sinc en el intervalo pertinente y una contribución estrictamente
positiva. No dividir por boundaryResource antes de probar que es no nulo.
Con N≥1, controlar leadingScale y convertir los restos finitos, de profundidad
y duales en cotas normalizadas. Combinar con los bloques 2 y 3.

Entrega prevista: AliceLayers/NormalizedRemainder.lean. Cierre: un E explícito
con identidad exacta y ‖E‖≤C*(N^(-1/2)+|normalFrequency η|), con C fijo.
Segunda comprobación: reconstruir la identidad multiplicando por leadingScale
y cotejar potencias de N con las cotas absolutas originales. Si la positividad
o la normalización falla, registrar el motivo y no alterar el contrato.

## 5. Ensamblaje y validación

Entrega prevista: AliceLayers/Assembly.lean con un teorema que pruebe exactamente
AliceLayersB. Elegir r₀≤π/6, N₀≥2 y C≥0 a partir de las constantes demostradas;
respetar los cuantificadores, la sumabilidad y la identidad de Targets.lean.
No sustituir el objetivo por una versión condicionada.

Cerrar cada bloque con compilación y guard de axiomas estándar; conservar
intentos fallidos y registros mediante build.py/verify.py. Para el cierre final,
ampliar comparador y mutaciones a fase, conjunto de índices, signo del resto,
normalización y uniformidad; leer antes la skill del comparador. Cotejar la
identidad y el enunciado con el paper congelado. Una compilación o un comparador
no constituyen revisión matemática externa ni acreditan novedad.

## Orden y disciplina

Ejecutar 1 → 2 → 3 → 4 → 5. Tras cada bloque actualizar STATUS.md y la hoja
de ruta con lo efectivamente probado, hipótesis y límites. Si falla un criterio,
volver a la derivación y detener la afirmación afectada, sin cambiar el objetivo.
Todos los generadores y pruebas quedan como artefactos permanentes. No se
necesitan barridos numéricos para demostrar estas cotas.

Este encargo de planificación no ejecuta pruebas nuevas, no hace commit/push,
no llama a proveedores y no escribe en QCA. Al redactar el plan AliceLayersB
permanecía abierto; el seguimiento registra su cierre formal posterior.

## Seguimiento de ejecución

La continuación autorizada después de publicar el plan implementa los bloques
1 y 2 en DepthEnvelope.lean y NormalPhase.lean. El registro completo del bloque
1 es verification/depth_envelope01/; el registro conjunto de ambos está
en verification/normal_phase01/, con success: true (31 módulos y 267 auxiliares
bajo el guard estándar). El bloque 3 se implementa después en DepthGeometry.lean
y DepthCompletion.lean: verificación depth_completion01/ con success: true,
33 módulos y 292 auxiliares bajo el guard estándar. La suma finita sin fase
ya se conecta con sPlus mediante una corrección O(1/N) que incluye capas vacías
y colas. El bloque 4 se implementa en NormalizedRemainder.lean: positividad del
recurso de frontera, resto normalizado explícito y cota uniforme con la forma
exacta de Targets.lean. Registro y resultado de verificación en STATUS.md.
El bloque 5 se completa en Assembly.lean: prueba del target escalar exacto con
r₀=π/6, N₀=2 y resto explícito. El comparador final copia 39 definiciones y
conecta once afirmaciones; 51/51 mutaciones rechazadas con fuentes restauradas.
La verificación completa posterior assembly_final01/ pasa (38 módulos y 313
auxiliares bajo el guard estándar). Los cinco bloques formales quedan cerrados;
la correspondencia documental y sus límites están en FIDELITY_ALICE_LAYERS_B.md.
La revisión externa y la novedad no forman parte del cierre acreditado.
