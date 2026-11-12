# Orden de trabajo: cierre escalar de AliceLayersB

Fecha: 2026-11-11. Encargo: ejecutar en orden los cinco bloques del
[plan de cierre](PLAN_CIERRE_2026-11-11.md), con sus criterios de parada.
Esta orden organiza trabajo futuro; no certifica resultados nuevos.

## Alcance y punto de entrada

Trabajar en esta carpeta de formalización. Leer CONTRACT.md, STATUS.md,
PLAN_CIERRE_2026-11-11.md, AliceLayers/Definitions.lean, Targets.lean y
ZeroModeDepth.lean antes de implementar. Conservar el contrato y el paper
congelado. El objetivo es exactamente AliceLayersB, componente escalar de Alice.
Pendientes iniciales: fase normal y paso a todas las profundidades con sus colas.
El seguimiento al final identifica los bloques ejecutados posteriormente.

## 1. Envolvente uniforme y sumabilidad

- Obtener una cota polinómica de ‖psi δ τ‖ uniforme en τ para δ≥0.
- Probar sumabilidad de depthTerm y del término ponderado por δ, con constantes
  uniformes en 0≤θ<1 al peso crítico exacto.
- Entregar DepthEnvelope.lean y registro de verificación; comprobar δ=0 y τ=0.
- Cerrar únicamente con integrabilidad y sumabilidad explícitas, sin valores
  por defecto de las integrales o las series como sustitutos de prueba.

## 2. Fase normal

- Reescribir exactamente el factor de capa en términos de δ y del índice natural.
- Definir el error entre geometricZeroModeSum y la suma sin fase, fijar su signo
  y demostrar la identidad antes de estimarlo.
- Aplicar ‖exp(-iu)-1‖≤|u| y el bloque 1 para obtener
  Cphase*|normalFrequency η|, independiente de N y η.
- Entregar NormalPhase.lean y registro. Comprobar error cero cuando
  normalFrequency η=0 y reconstrucción exacta de la suma con fase.

## 3. Todas las profundidades, capas vacías y colas

- Identificar la imagen finita J_N de los índices activos y reindexar la suma;
  no presuponer índices consecutivos.
- Expresar la diferencia con sPlus mediante los índices de ℕ que faltan.
- Acotar por separado la cola fuera de 0≤δ≤N/2 y las capas vacías interiores.
  Investigar la geometría de estas últimas con puntos enteros de coordenadas
  equilibradas; no atribuirles perfil continuo cero sin prueba.
- Entregar DepthCompletion.lean o módulos separados si resulta necesario, con
  identidad y cota total Ccompletion/√N uniforme en θ_N y τ para N grande.
- Comprobar θ=0, profundidad cero, bordes y cobertura de todos los índices omitidos.
  Si falla la cota, registrar la obstrucción y detener esa vía.

## 4. Normalización del resto

- Probar boundaryResource>0 desde su integral antes de dividir por él.
- Convertir las cotas absolutas existentes a cotas del resto normalizado y
  añadir los errores de los bloques 2 y 3.
- Entregar NormalizedRemainder.lean con E explícito, identidad exacta y
  ‖E‖≤C*(N^(-1/2)+|normalFrequency η|), con C independiente de N y η.
- Reconstruir la amplitud multiplicando por leadingScale y comprobar las
  potencias de N contra las cotas absolutas originales.

## 5. Ensamblaje y validación

- Entregar Assembly.lean con un teorema del enunciado exacto AliceLayersB:
  testigos r₀>0, C≥0, N₀≥2, sumabilidad e identidad con el resto requerido.
- Usar r₀≤π/6 y un N₀ compatible con todos los bloques; no añadir hipótesis.
- Ejecutar la verificación completa y el guard de axiomas estándar, sin sorry,
  native_decide ni axiomas propios. Ampliar comparador y mutaciones a los
  enunciados críticos, leyendo antes la skill correspondiente.
- Comprobar fidelidad de definiciones y enunciado al paper congelado. Distinguir
  prueba formal, fidelidad al paper, revisión externa y novedad.

## Registro, límites y entrega

Después de cada bloque, conservar código, generadores y logs permanentes;
actualizar STATUS.md y la hoja de ruta con hipótesis, resultados y pendientes.
Usar build.py/verify.py con carpetas nuevas de verificación. Registrar fallos y
correcciones. No pasar al siguiente bloque dependiente si falta su criterio de cierre.

No cambiar el objetivo para acomodar un fallo. No escribir en QCA, descargar
dependencias ni llamar a proveedores. No convocar comités ni revisiones externas
con esta orden. Los futuros commits/push requieren el encargo correspondiente;
la autorización de publicación de esta orden y del plan no autoriza publicaciones
posteriores. AliceLayersB permanece abierto hasta satisfacer el bloque 5.

## Seguimiento

Continuación del 2026-11-11: completados los cinco bloques formales; resultados y
registros de verificación en STATUS.md. El bloque 3 controla las capas vacías
y las colas con error C/N, suficiente para la cota exigida. El bloque 4 prueba
la positividad del recurso de frontera y normaliza el resto con la cota exacta
requerida. El bloque 5 demuestra AliceLayersB con r₀=π/6, N₀=2 y C fijo,
y completa el comparador y sus mutaciones: 51/51 rechazadas. Verificación final
assembly_final01/: success: true, 38 módulos y 313 auxiliares bajo el guard
estándar. El cierre es del target escalar definido, con los límites de
FIDELITY_ALICE_LAYERS_B.md; no es revisión externa ni prueba del paper completo.
