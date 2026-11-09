# Hoja de trabajo — 7 de noviembre de 2026

Preparada el 2026-11-06 por Codex a petición del usuario.
Rama: research/schur-stability-audit; HEAD observado 74db229.
Hay trabajo de hoy SIN COMMIT: contratos, informes, scripts, resultados,
fuentes y revisión sellada. Al reanudar comprobar HEAD, git status y
CURRENT_STATE antes de editar. No asumir que los archivos están subidos.
Plan de continuación, no ejecución futura anticipada ni promoción.

## Objetivo de mañana

Resolver las reparaciones de la revisión ciega de Claude antes de
continuar la investigación interactuante. Conservar separados:
identidades exactas, resultados numéricos finitos, ODE perturbativo,
hipótesis de límite y teorema microscópico aún no probado.

No empezar ampliando retardos, radios Abel o tamaños de simulación.
No construir otra arquitectura para eludir una objeción antes de
determinar si es un error, una reparación documental o un gap real.

## Punto de entrada obligatorio

1. PROJECT_INSTRUCTIONS.md y state/CURRENT_STATE.md.
2. reports/2026-11-06--interacting-chain-review-status.md.
3. debates/2026-11-06--interacting-chain-review-opus/informe_opus.md.
4. Los contratos e informes afectados por cada objeción, y sus scripts.

Revisión realizada con revision-ciega opus canónico, herramientas
ce09890; Claude Opus 5.5, high, sin herramientas, una ronda.
Entrada sellada SHA256
163969e76c07db60170ad37c5dfd3d57f419907c95650476d86f6077c918712c.
No editar el informe sellado ni sobrescribir sus entradas o salidas.
La revisión es de otra familia de modelos, no humana; no ejecutó código.
No usar sus derivaciones nuevas como fuente o resultado sin comprobarlas.

Veredictos: bloques 1 y 3 PASS; bloque 4 PASS SOLO para ODE efectivo
congelado; bloques 2, 5 y 6 REPAIR_REQUIRED. Ningún FAIL. No PASS global.
Las objeciones 15–16 han motivado dos correcciones de alcance en
CURRENT_STATE; no están re-revisadas. Las demás permanecen abiertas.

## 1. Registro de objeciones y alcance — primera prioridad

Crear un registro trazable de las 19 objeciones con archivo afectado,
tipo (error/gap/documental/informativa), respuesta del autor, evidencia
y estado. «Respondida» no significa «resuelta». Seguir la herramienta
canónica y su formato si se usa comprobar-objeciones: leer MAPA y ayuda
antes de elegirla y registrar el commit de herramientas.

Comprobar las correcciones 15–16: la cota es de Trotter a L,M fijos,
no de convergencia del corte; el flujo resuelto es de un lazo, lineal
en diferencias de velocidad, sobre acoplamientos de referencia iguales.

Antes de otro cálculo, escribir conocido/fuente, pregunta y abandono.
Los contratos Yukawa actuales tienen cortes de alcance que Claude
considera insuficientes como criterios de abandono de línea (Obj.17).
Fijar criterios científicos y de viabilidad explícitos, no retroactivos:

- abandonar la afirmación para un QCA fijo si solo se obtiene una
  familia con M creciente y delta decreciente, manteniendo ese resultado
  de aproximación con su propio alcance;
- abandonar una propuesta de detección numérica si la señal prevista
  queda por debajo de sus errores declarados y no existe una mejora
  justificada dentro del presupuesto fijado;
- si falla una identidad base, suspender los resultados que la usan y
  rehacerlos antes de ampliar la línea.

No imponer estos criterios como refutación general de emergencia de c.

## 2. Memoria: cerrar las convenciones y premisas

Obj.1: verificar y escribir la separación Hartree exacta
N1 N2=deltaN1 deltaN2+2N1+2N2-4; justificar PHP=0 para el generador
centrado antes de quitar proyectores Q del núcleo.

Obj.2: definir la transformada temporal G(z), derivar la recurrencia
transformada, su factor adicional z respecto de S_rho y el orden de
multiplicación en la convención de respuesta. No confundir matriz de
respuesta con matriz de coeficientes de operadores traspuesta.

Obj.3: añadir partial_omega Sigma a las obligaciones para extraer una
pendiente. Las cotas necesarias no se reducen a partial_k Sigma.

Obj.5: adjuntar el constructor s=4 original, comprobar Fourier y signo
mediante la pendiente libre conocida. Esa referencia faltó en el envío.
Los datos numéricos no fueron verificados por Claude.

Obj.4 es una mejora opcional de factor dos en la cota, no un fallo.
No regenerar tablas antiguas solo para embellecer una cota válida.

## 3. Ajuste crítico y corte: comprobaciones nuevas necesarias

Obj.7/D7: verificar por segunda vía la simetría partícula-hueco propuesta
para Wilson, contacto, Yukawa y cada capa. Si se confirma, registrar sus
condiciones y qué operadores prohíbe; no inferir invariancia del estado
sin las hipótesis de unicidad/simetría pertinentes.

Obj.13/D10: rederivar la tercera derivada del determinante fermiónico
y comprobar si el término cúbico escalar se genera en la clase fijada.
Crear tabla de operadores de dimensión <=4 y sus simetrías, distinguiendo
Hamiltoniano y circuito a delta finito. Incluir anisotropías marginales
que puede introducir el orden de capas, no solo operadores relevantes.

Obj.12: reducir las cifras mostradas de las cuadraturas o acompañarlas
de diferencias entre mallas y error explícitamente no certificado.
Preservar los JSON originales como registro; no inventar precisión.

Obj.14: explicitar que probabilidad de cola O(L^-1) implica error en
norma traza O(L^-1/2), y que Strang compara con H_LM, no con el campo
sin truncar. La uniformidad de momentos y el matching de estados
fundamentales siguen sin demostrarse.

## 4. Flujo Yukawa y magnitud del efecto

Obj.8: leer en el PDF original Anber–Donoghue Ec.(48), confirmar página
y reducción a acoplamientos diagonales antes de citarla.
Obj.9: corregir «modos relevantes» por «modos de atracción».
Obj.10: mantener y1=y2 como alcance del ODE resuelto; la propuesta de
beta para acoplamientos desiguales hecha por Claude NO está verificada.
Derivarla sería un cálculo posterior, con contrato, no reparación tácita.

Obj.11: calcular con script permanente la reducción prevista y la escala
necesaria para una reducción concreta, usando los exponentes 1/21 y
13/21 ya derivados. Mostrar parámetros y errores del escenario numérico.
No adoptar la afirmación absoluta «ninguna simulación finita puede
detectarlo»: depende de parámetros, precisión y pregunta experimental.
La lentitud sí debe incorporarse al criterio de viabilidad.

## 5. Comprobación y cierre

Cada reparación debe enlazar evidencia exacta o prueba primaria, y
distinguir autocomprobación de aceptación independiente. Tests nuevos
solo donde comprueben la obligación; conservar todo código científico.
No reejecutar verificadores no afectados salvo una duda nueva concreta.

Preparar un resumen autocontenido de reparaciones y snapshot con hashes.
Una re-revisión externa es una ronda nueva: preparar encargo acotado y
confirmar que está autorizada antes de enviar; no asumir autorización
ilimitada por la primera revisión. Usar solo los lanzadores canónicos.

Actualizar CURRENT_STATE con lo realmente cerrado. No promover por
un PASS de un verificador o por un PASS del ODE. No afirmar prueba del
QCA mientras ajuste crítico, corte y matching infrarrojo sigan abiertos.

## Git y líneas aparcadas

El usuario condicionó commit/push/fusión con main a la prueba suficiente;
esa condición no se ha cumplido. No interpretar esta hoja como orden
de fusionar o promover. Si se autoriza guardar avances parciales, commit
solo de archivos propios por nombre y con alcance PRELIMINARY explícito.
No añadir scripts/__pycache__/ por arrastre.

Hexagonal permanece aparcado; H1 abandonado por decisión del usuario.
No reabrirlos para sustituir la tarea de reparar esta cadena.

## Instrucción breve de reanudación

«Lee la hoja del 7 de noviembre, CURRENT_STATE y la revisión sellada de
Claude. Empieza por registrar las objeciones y reparar alcance y
convenciones; comprueba D7 y D10 antes de utilizarlas. Cuantifica la
lentitud del flujo antes de proponer simulaciones. No presentes el ODE
como prueba microscópica ni fusiones con main mientras falte esa prueba.»
