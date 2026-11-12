# Estado comprobado de esta preparación

SCALAR_ALICE_LAYERS_B_FORMALLY_PROVED / EXTERNAL_REVIEW_OPEN.

Plan de continuación vigente: [PLAN_CIERRE_2026-11-11.md](PLAN_CIERRE_2026-11-11.md).
La planificación original no añade resultados probados. La ejecución posterior
de los cinco bloques se registra al final. El target escalar tiene prueba Lean;
la revisión externa y la novedad permanecen separadas del cierre formal.

Estado vigente (continuación 2026-11-11): `AliceLayers.aliceLayersB_proved` demuestra
exactamente `AliceLayersB`, sin cambiar Targets.lean, con r₀=π/6 y N₀=2. Se
incluyen sumabilidad, fase normal, todas las profundidades con capas vacías y
colas, normalización e identidad de la amplitud escalar. Registro final
`assembly_final01/`: success: true, 38 módulos, 313 auxiliares bajo el guard
estándar, once pruebas del comparador final y 57 comparaciones textuales de
definiciones. `final_mutations01.json`: PASA, 51/51 rechazadas y fuentes
restauradas. Los cinco bloques formales quedan cerrados. No hay revisión
externa ni afirmación de novedad o prueba de Bob/todo Layers. Detalles al final.
Los comentarios de apertura de Targets.lean se conservan como parte del archivo
original; la prueba posterior está en Assembly.lean.

Resumen anterior (2026-11-11): ambas sumabilidades espectrales y Poisson
iterado para ℤ² y para el perfil principal sobre la red tangencial desplazada
y escalada están demostrados. El cambio de medida y los coeficientes están en
`TangentTransport.lean`; las condiciones espectrales y la identidad sumada, en
`TangentSpectral.lean`. `FiniteProfile.lean` conecta esta identidad con la
amplitud original mediante una profundidad efectiva y errores finitos explícitos.
`RemainderBounds.lean` acota uniformemente los errores del seno y del recurso
tras sumar todas las capas; también controla el cambio de profundidad por modo.
`DualDecay.lean` controla también los modos duales no nulos, con cota absoluta
`C/N⁴` en la amplitud para `frequencyNorm η≤π/6`. El resto total sigue abierto.
`ZeroModeDepth.lean` suma el cambio de profundidad del modo cero con cota
`C/N` antes de `leadingScale`, y `C/N^(7/2)` en la amplitud, para toda frecuencia.
Detalles y límites al final. Los apartados anteriores que
describen obligaciones abiertas son registros históricos.

- Nueve ingredientes de CLAIMS.md demostrados y compilados en Lean 4.31.0.
- Challenge independiente de las pruebas, importando únicamente Mathlib.
- Once definiciones copiadas verificadas como textualmente idénticas al original.
- Nueve teoremas pasan el guard de axiomas: sólo propext, Classical.choice y
  Quot.sound permitidos. Sin sorryAx, native_decide ni axiomas propios en esas pruebas.
- Dos lemas auxiliares nuevos, la expansión de la suma en `Fin 2` y la anulación
  del integrando de Ψ fuera del radio, compilan y pasan un guard separado de los
  mismos axiomas estándar (`AliceLayers/AuxiliaryAudit.lean`).
- Los doce lemas auxiliares pasan el guard separado de los mismos axiomas estándar;
  entre ellos, continuidad más soporte compacto demuestra `ProfileIntegrability`, y
  el kernel que define `phi0` es interval-integrable en `0..1` para todo `ρ`; además,
  `phi0` es continua en `ρ`. También se probaron los puentes `x^(-3/2)` y
  `x^(-5/2)` a sus formas con raíces, y la identidad del prefactor completamente
  escrita con `rpow`. Para `n>0`, `q≥0`, se probó la equivalencia exacta del dominio
  esférico por capas y la eliminación del recorte positivo en ese dominio.
- lean-mutar: 17/17 RECHAZADA; compilaciones limpias inicial y final correctas;
  fuentes restauradas. Registro: verification/mutations01.json.
- Verificación más reciente: verification/lattice_coordinates01/verification.json;
  compilaron los ocho módulos y los veintiún teoremas auditados pasan sus guards.

No demostrado: AliceLayersB y los puentes analíticos y
geométricos enumerados en README.md. Targets.lean contiene proposiciones bien
formadas, no axiomas ni teoremas que las afirmen. No se afirma una demostración
de la asintótica ni se cambia SUPPORTED_FINITE_DIAGNOSTIC del experimento.

Sin llamadas a proveedores, descargas, commit/push ni escrituras en QCA.
El cache Lean/Mathlib de QCA se usó para lectura; los objetos compilados propios
están en build/, ignorado por Git. Código, fuentes y registros permanecen aquí.

## Avance: capas enteras

`AliceLayers/Basic.lean` demuestra la parametrización inyectiva `(a,b) ↦
(a,b,k-a-b)` de cada plano entero y recupera cualquier punto desde sus dos
primeras coordenadas. Para los vectores `(1,0,-1)` y `(0,1,-1)` calcula las
entradas de Gram 2, 2, 1 y la raíz de su determinante, √3. Esto es el área
geométrica del paralelogramo de la base; la identificación posterior con una
medida formal de covolumen se registra más abajo. El factor en Poisson sigue pendiente.

Para cada punto de soporte con N>0 se demuestra que su índice está como máximo
en `floor(√3 N/4)` y que su profundidad es `(theta N + j)/√3` para algún
`j : ℕ`. La amplitud se reagrupa exactamente como suma finita sobre índices
enteros presentes y sus fibras. No se ha reindexado aún cada fibra por ℤ² ni se
ha sustituido esta suma finita por la serie infinita del término principal.

La verificación `verification/integer_layers01/` recompila los ocho módulos y
comprueba los doce nuevos lemas junto con los doce auxiliares anteriores mediante
el guard de axiomas. El comparador independiente sigue cubriendo los nueve
resultados anteriores, no estos doce nuevos. `AliceLayersB` sigue abierto.

## Avance: medida formal del covolumen

`AliceLayers/Covolume.lean` construye una base real en coordenadas tangenciales,
identifica su ℤ-span exactamente con la imagen del plano entero de índice cero
y demuestra `ZLattice.covolume tangentLattice = √3` para `volume` de Mathlib.
La prueba usa que `ZSpan.fundamentalDomain` es un dominio fundamental y la
fórmula de su medida mediante el determinante; comprueba además que las
coordenadas tangenciales preservan la norma euclídea en el plano real. Esta
medida es la medida de Lebesgue en el marco tangencial ortonormal; no es la
medida tridimensional del plano, que sería cero.

La comprobación `verification/covolume01/` recompila los nueve módulos y
audita los seis teoremas añadidos. La reindexación de fibras se registra en el avance posterior; Poisson y las
estimaciones asintóticas siguen pendientes. El comparador independiente sigue
cubriendo los nueve ingredientes anteriores, no los lemas nuevos de covolumen.

## Avance: reindexación de las capas

`AliceLayers/Reindex.lean` demuestra que el conjunto de coordenadas enteras
contiene exactamente los pares cuyo punto pertenece a `aliceSites`, y que su
imagen es la fibra de plano original. Por inyectividad, reindexa cada suma
finita y la amplitud completa sin alterar el soporte ni el perfil. Para N>0
expresa el soporte por la desigualdad esférica exacta.

También demuestra que la imagen tangencial del plano k es `layerShift k`
más `tangentLattice`, y descompone la fase centrada en componentes normal y
tangencial, incluyendo esa traslación. Estos resultados no aplican Poisson ni
pasan de la suma finita a la serie infinita.

La verificación `verification/reindex01/` recompila diez módulos y audita los
nueve teoremas nuevos con el guard de axiomas. El comparador independiente sigue
cubriendo los nueve ingredientes originales, no los lemas de reindexación.
`AliceLayersB` sigue abierto.

## Avance: Poisson iterado condicionado

`AliceLayers/Poisson.lean` demuestra `poisson_two_iterated` mediante dos
aplicaciones de `Real.tsum_eq_tsum_fourier` y un intercambio de sumas justificado
por la hipótesis explícita `hcross`. `psi_poisson_compact` especializa el
resultado al integrando de Ψ muestreado sobre ℤ² en coordenadas estándar. Para
δ≥0, se demuestra el soporte compacto de cada sección y de ahí la condición
de sumabilidad de traslaciones sobre compactos requerida por la primera
aplicación de Poisson.

La fórmula sigue condicionada a continuidad de las secciones transformadas,
sumabilidad de las frecuencias, sumabilidad de sus traslaciones e intercambio
de las sumas. La identificación posterior del modo cero con `psi` se registra más abajo.
No se ha tratado la red tangencial desplazada y escalada, ni demostrado la
fórmula de Poisson de cada capa real o cotas uniformes. `AliceLayersB` sigue
abierto. El comparador independiente sigue cubriendo los nueve ingredientes
originales, no los teoremas nuevos de Poisson.

`verification/poisson01/` recompila once módulos y audita los seis teoremas
nuevos mediante el guard de axiomas estándar.

## Avance: identificación del modo cero

`AliceLayers/PoissonZero.lean` demuestra la integrabilidad del integrando de Ψ
en ℝ × ℝ mediante la equivalencia que preserva medida con `Fin 2 → ℝ`. Aplica
Fubini con dicha integrabilidad e identifica las integrales iteradas con `psi`.
Con la convención de Fourier de Mathlib, la transformada en frecuencia cero es
la integral; por tanto `psi_double_fourier_zero` demuestra directamente que el
modo cero de la transformada iterada es `psi δ τ`, para δ≥0. No se requiere
una hipótesis sobre la función intermedia para ese último teorema.

`verification/poisson_zero01/` recompila doce módulos y audita los cinco nuevos
teoremas con el guard de axiomas estándar. No se ha identificado la transformada
iterada para frecuencias generales ni se han demostrado las condiciones restantes
de Poisson, su adaptación a cada capa o `AliceLayersB`. El comparador
independiente anterior no cubre estos cinco teoremas.

## Avance: frecuencias generales de la transformada iterada

`AliceLayers/PoissonZero.lean` demuestra `psi_double_fourier`: para δ≥0 y
frecuencias reales u,v arbitrarias, la transformada iterada en las coordenadas
(y,x) es `psi δ (shiftedTau τ u v)`, donde `shiftedTau` resta 2πu y 2πv a las
componentes respectivas de τ. La prueba desarrolla ambas integrales Fourier
y combina sus fases; utiliza la identidad de Fubini ya demostrada. El caso
u=v=0 se deriva además del teorema general como control de consistencia.

`psi_poisson_identified` sustituye todos los términos espectrales en la fórmula
iterada para ℤ² por sus valores en Ψ. Conserva explícitamente las hipótesis de
Poisson que siguen abiertas; no prueba por sí misma Poisson para la red
tangencial desplazada y escalada ni las estimaciones de `AliceLayersB`.

`verification/poisson_frequencies01/` recompila doce módulos y audita los cinco
teoremas nuevos. El comparador independiente original no cubre estos teoremas.

## Avance: función intermedia y geometría dual

`AliceLayers/PsiIntermediate.lean` construye la transformada de cada sección
de Ψ, demuestra continuidad en la coordenada restante y soporte compacto, y
obtiene su condición de sumabilidad de traslaciones. Demuestra que solo hay
un número finito de secciones en coordenadas enteras no nulas y deduce el
intercambio de las series de la primera sumabilidad espectral. Por ello la
fórmula `psi_poisson_two_summability` conserva solo dos hipótesis de
sumabilidad de frecuencias; `psi_poisson_spectral_condition` expresa la segunda
en términos de valores de Ψ. No se han probado las cotas de decaimiento ni
dichas hipótesis: la fórmula incondicional sobre ℤ² sigue abierta.

`AliceLayers/Dual.lean` calcula la base recíproca en ciclos y su emparejamiento
con las coordenadas de la red directa y con su traslación por capa. Esto no es
todavía la fórmula de Poisson en la red tangencial: faltan el cambio de medida,
el escalado, el tratamiento completo de la fase y las estimaciones uniformes.
`AliceLayersB` sigue abierto.

La verificación `verification/psi_intermediate_dual01/` recompila catorce
módulos y audita doce teoremas nuevos de la función intermedia y dos de la base
dual. El comparador independiente original no cubre estos teoremas.

## Avance: regularidad e integración por partes

`AliceLayers/SectionRegularity.lean` demuestra que la parte positiva al cuadrado
es C¹ en toda la recta. Calcula la derivada de cada sección real del recorte,
que es continua y se anula en la frontera del disco. Demuestra también que la
sección compleja completa de Ψ es C¹, que su derivada es integrable y que se
puede aplicar `Real.fourier_deriv` con las hipótesis verificadas. La desigualdad
`psiSlice_first_order_bound` acota `|2π u|` multiplicado por la norma de la transformada
mediante la norma L¹ de la derivada.

La cota de primer orden por sí sola no implica sumabilidad en ℤ. No se ha
justificado una segunda integración por partes ni una cota de variación o de
segundo orden, ni se han cerrado las hipótesis espectrales de Poisson. Tampoco
se han obtenido las estimaciones uniformes de `AliceLayersB`.

`verification/section_regularity01/` recompila quince módulos y audita los
catorce teoremas nuevos. El comparador independiente anterior no cubre estos
lemas. Las advertencias de estilo de Lean quedan registradas en el log.

## Comparador local nuevo: cobertura parcial

El comparador independiente adicional cubre siete resultados principales de
regularidad y Fourier enumerados en CLAIMS.md; cinco definiciones copiadas se
comprueban textualmente. La fuente de `lean-comparador` y `lean-mutar` es el
repo `herramientas`, commit `a32e189`. La construcción de `psiSlice` requiere
un lema local de continuidad; la prueba completa de cada afirmación comparada
permanece sólo en los módulos originales y Solution la conecta por nombre.

Primer ciclo `verification/new_mutations01.json`: 12/13 rechazos esperados y
una `FALLO_DISTINTO` en el propio Challenge para el cambio de exponente. Se
corrigió la prueba auxiliar de continuidad para que no fijara dicho exponente;
no se modificó el patrón de rechazo. Segundo ciclo
`verification/new_mutations02.json`: 13/13 `RECHAZADA`, con compilaciones limpias
inicial y final, incluidas las siete mutaciones de enunciado, cinco de
definiciones y una sustitución por `sorry` detectada por el guard.

El registro de verificación limpio `verification/comparator_new02/` corresponde
al Challenge corregido. Esta cobertura es parcial: los resultados posteriores
sobre retículo, covolumen, Poisson condicionado, función intermedia y demás
auxiliares no tienen todavía comparador independiente ni sus mutaciones propias.
El comparador no certifica la fidelidad global del enunciado al paper ni resuelve
`AliceLayersB`.

## Avance: segunda derivada por tramos

`AliceLayers/SectionSecond.lean` calcula la segunda derivada del recorte real
por separado dentro y fuera del disco. Demuestra que los puntos de frontera de
una sección son como máximo dos, que la fórmula por tramos coincide casi en
todas partes con la segunda derivada y que ambas son integrables. Esto incluye
las secciones degeneradas y no afirma derivabilidad en los puntos de frontera.

La igualdad casi en todas partes y la integrabilidad tienen un comparador
independiente en `AliceComparator/SecondChallenge.lean`; las definiciones se
comparan textualmente. `verification/second_mutations01.json` registra 5/5
mutaciones rechazadas y compilaciones limpias inicial y final; herramienta
`lean-mutar` en `herramientas` commit `a32e189`.

La segunda integración por partes para la sección compleja no está demostrada:
es preciso justificar el tratamiento del borde y ensamblar la fase oscilatoria.
Por tanto tampoco está demostrada una cota Fourier de segundo orden, ninguna
sumabilidad espectral nueva ni Poisson incondicional. `AliceLayersB` sigue
abierto. La verificación completa está en `verification/section_second01/`.

## Avance: integración por partes con excepciones finitas

`AliceLayers/WeakParts.lean` demuestra una integración por partes para un factor
complejo cuya derivada falla en un conjunto numerable, bajo las hipótesis de
continuidad e integrabilidad explícitas. La aplica a la derivada del recorte real
y a una fase exponencial, con términos de borde nulos. Esto cubre la segunda
integración por partes del recorte real contra esa fase; todavía falta combinarla
con la fase adicional de la sección completa y obtener la cota Fourier de segundo
orden y las condiciones de sumabilidad espectral.

`verification/weak_parts02/` recompila todos los módulos y audita los cuatro
teoremas nuevos con el guard de axiomas estándar. El primer intento
`verification/weak_parts01/` falló por el contador desactualizado del mensaje del
guard; se conserva. Estos cuatro enunciados no tienen comparador independiente
ni prueba de mutaciones. `AliceLayersB` sigue abierto.

## Inicio de la combinación de fases

`psiSlice_mul_oscillation` identifica exactamente el producto de la sección
compleja por una fase exponencial: la frecuencia en la coordenada de integración
es `τ 0 + ω`, y el factor `exp(i * τ 1 * x)` queda constante. La igualdad es
puntual, para todos los parámetros reales; todavía no aplica la integración por
partes a la integral de Fourier ni establece su decaimiento.

`verification/phase_combination01/` recompila todos los módulos y añade el lema
al guard de axiomas estándar. No hay comparador independiente ni mutaciones para
este lema. La integración de esta identidad con `cutoff_oscillation_parts`, la
cota de segundo orden, la sumabilidad espectral y `AliceLayersB` siguen abiertas.

## Avance: dos integraciones por partes de la sección compleja

`psiSlice_fourier_double_parts` combina la transformada de Fourier de la sección
compleja con las dos integraciones por partes del recorte real. Para δ ≥ 0 y
ω = τ 0 − 2πu demuestra la igualdad exacta entre la transformada multiplicada
por `(iω)²` y la integral de `cutoffSecond` por la fase desplazada y el factor
constante. La prueba incluye ω = 0: no divide por la frecuencia. Se justifica
además el paso de la integral sobre ℝ al intervalo que contiene el soporte.

`verification/fourier_double_parts01/` recompila los 23 módulos y audita los
cinco lemas nuevos junto con los anteriores: 101 lemas auxiliares bajo el guard
de axiomas estándar. Los nuevos enunciados no tienen comparador independiente ni
mutaciones específicas. La identidad no proporciona todavía una cota uniforme
de la integral, ni la sumabilidad espectral, ni demuestra `AliceLayersB`.

## Avance: decaimiento y primera sumabilidad espectral

`psiSlice_second_order_bound` acota la norma de la transformada multiplicada
por el cuadrado de la frecuencia desplazada mediante la norma L¹ de
`cutoffSecond` en el intervalo de soporte. `psiSlice_second_order_decay` obtiene
la cota dividida por ese cuadrado fuera de la frecuencia resonante.
`psiSlice_spectral_summable` demuestra la primera condición espectral sobre ℤ,
con una serie p desplazada y excluyendo la posible resonancia como conjunto
finito. Por tanto, `psi_poisson_one_summability` necesita únicamente la segunda
condición espectral. `psi_swap_coordinates` demuestra la simetría de Ψ al
intercambiar coordenadas mediante Fubini; no demuestra esa segunda condición.

`verification/first_spectral_symmetry01/` recompila los 23 módulos y audita
106 teoremas auxiliares con el guard de axiomas estándar. Estos cinco resultados
nuevos no disponen aún de comparador independiente ni mutaciones. Siguen abiertos
la segunda sumabilidad, Poisson incondicional y su transporte, las cotas
uniformes de profundidad y frecuencia, el resto E_A y `AliceLayersB`.

## Continuación 2026-11-11: constante uniforme por sección

`cutoffSecond_uniform_bound` demuestra `|cutoffSecond δ x y| ≤ 8δ` para
δ≥0, sin restringir x ni y. Dentro del disco se usa `y²+x²<δ`; fuera, la
derivada por tramos es cero. Integrando en `[-(δ+1),δ+1]`,
`cutoffSecond_integral_uniform_bound` obtiene `16δ(δ+1)`.
`psiSlice_second_order_uniform_bound` combina este resultado con la cota
Fourier existente, sin dividir por la frecuencia desplazada. Incluye δ=0 y
secciones degeneradas. La constante es uniforme en sección y fase, pero depende
de δ; no es una cota uniforme en profundidad para `AliceLayersB`.

Procedencia: continuación local sobre herramientas `97292a9`; fuente congelada
comprobada con el SHA-256 del contrato. Código permanente en `WeakParts.lean`;
verificación en `verification/uniform_section01/`. Los tres enunciados se añaden
al guard de axiomas estándar; todavía no tienen comparador ni mutaciones propios.
La verificación completa terminó correctamente: 23 módulos compilados, 109
teoremas auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
`git diff --check` también pasa. No se ejecutaron nuevas mutaciones.

La segunda sumabilidad sigue abierta. Siguiente obligación: integrar la cota de
secciones sobre el soporte compacto de la coordenada restante, justificar la
identificación mediante Fubini y aplicar la serie p desplazada, con las resonancias
como excepciones finitas. No se ha demostrado aún ese paso en Lean ni Poisson
incondicional; `AliceLayersB` sigue abierto.

## Continuación 2026-11-11: segunda sumabilidad y Poisson iterado

Este avance sustituye el estado abierto de la segunda sumabilidad indicado en
los apartados anteriores. `psiPartial_integral_interval` verifica el soporte
incluyendo el extremo izquierdo, sin descartar a mano un término de frontera.
`psi_second_order_bound` integra la cota anterior y demuestra, para δ≥0,

`‖psi δ τ‖ * |τ 0|² ≤ 32δ(δ+1)²`.

La identificación con la integral bidimensional usa `psi_double_fourier_zero`
y, por tanto, Fubini con `psi_prod_integrable`. La continuidad de `psiPartial`
justifica la integrabilidad en el intervalo y la comparación de integrales.
`psi_second_coordinate_bound` demuestra la misma cota en la otra coordenada
mediante la simetría ya probada. No se divide por una frecuencia nula.

`psiPartial_spectral_summable` demuestra la segunda sumabilidad para toda primera
frecuencia real u, comparando fuera de un conjunto finito con la serie
`1/|n+a|²`. `psi_poisson` cierra la identidad de Poisson como suma iterada en
la red estándar ℤ², con las únicas hipótesis δ≥0 y τ arbitraria. Esto no afirma
sumabilidad absoluta conjunta ni permite reordenaciones adicionales de la
serie dual. `psi_zero_depth` comprueba directamente el caso límite δ=0 por
anulación puntual del perfil, sin usar la cota Fourier.

Código permanente en `WeakParts.lean`; registro completo definitivo en
`verification/second_spectral02/`. El primer registro, `second_spectral01/`,
compiló los 23 módulos y el guard de 115 auxiliares, pero conservó el contador
109 cargado al arrancar el verificador antes de su actualización. Se conserva
esa discrepancia y se repite la verificación con fuentes y contador fijados.
La segunda verificación terminó con `success: true`: 23 módulos compilados,
115 auxiliares auditados y las 18 definiciones copiadas iguales. También pasa
`git diff --check`; no se ejecutaron nuevas mutaciones.
Los seis teoremas nuevos se añaden al guard
estándar (115 auxiliares en total). No tienen todavía comparador ni mutaciones
propios ni revisión externa. No se cambia el alcance del contrato.

El siguiente paso de la hoja de ruta es el transporte a la red tangencial
desplazada y escalada, incluyendo medida, covolumen y fase. Siguen pendientes
las cotas uniformes del resto y `AliceLayersB`.

## Continuación 2026-11-11: medida y coeficientes de la red tangencial

`AliceLayers/TangentTransport.lean` fija el mapa `q=b+s*tangentMap p`, con s>0,
y demuestra que su determinante es `s²√3`. Lo enlaza también con
`s² * ZLattice.covolume tangentLattice`. La medida es la de Lebesgue en las dos
coordenadas tangenciales ortonormales, no la medida ambiente de ℝ³.
`tangent_integral_transport` demuestra el cambio de variables para funciones
continuas. `tangent_profile_integrable` y `tangent_fourier_integrable` comprueban
por separado la integrabilidad del perfil y del integrando modulado para δ≥0;
no se infiere esa obligación del valor por defecto de una integral.

Con d=`dualCoordinate u v`, `tangent_fourier_coefficient` demuestra exactamente

`∫ dp exp(-2πi(up₀+vp₁)) psiIntegrand δ τ (b+s*tangentMap p)`

`= exp(i(2π/s)⟨d,b⟩) * (s²√3)⁻¹ * psi δ (τ-(2π/s)d)`.

Las frecuencias u,v son reales arbitrarias. El signo positivo de la fase y los
factores de escala se deducen del emparejamiento dual, no de una convención
verbal. `tangent_layer_translation_phase` especializa b=s*layerShift k y obtiene
`exp(-2πi*k*(u+v)/3)`, independiente de s. Los controles
`tangent_fourier_zero` y `tangent_fourier_no_translation` verifican por separado
el modo cero y la traslación nula. `tangent_fourier_zero_scaled` comprueba que
para s=1/√(2R), R>0, el modo cero es `(2R/√3)*psi δ τ`.

Procedencia: herramientas `97292a9` más los cambios locales de esta continuación;
fuente congelada y dependencias del contrato. Se conservan los fallos en
`verification/tangent_transport_attempt01.md` y los logs de build posteriores.
Verificación completa: `verification/tangent_transport01/`. Los 16 teoremas
nuevos se añaden al guard estándar (131 auxiliares); sin comparador, mutaciones
específicas ni revisión externa nuevos.
El registro final tiene `success: true`: 24 módulos compilados, 131 auxiliares
bajo el guard y las 18 definiciones copiadas iguales. `git diff --check` pasa.
La fuente congelada conserva el SHA-256 indicado en `CONTRACT.md`.

**Pendiente:** demostrar las condiciones espectrales de las secciones del
perfil compuesto con este mapa afín y enlazar su transformada iterada con los
coeficientes anteriores para aplicar `poisson_two_iterated`. `tangentMap` no
es una similitud: los vectores de su base tienen Gram 2,2,1. El disco da una
elipse en coordenadas enteras, por lo que `psi_poisson` no se puede aplicar
simplemente sustituyendo sus parámetros. No se ha demostrado todavía la
identidad sumada de cada capa tangencial ni se ha aplicado a la amplitud finita
reindexada. El bloque 3 de la hoja de ruta y `AliceLayersB` siguen abiertos.

## Continuación 2026-11-11: condiciones espectrales y Poisson tangencial

Este avance cierra las condiciones espectrales y la identidad sumada pendientes
en el apartado anterior. `TangentSpectral.lean` construye una rotación ortogonal
alineada con el primer vector tangencial. Comprueba que conserva la norma
cuadrática y el emparejamiento de fase, y demuestra la reducción puntual de
cada sección elíptica a una sección circular reparametrizada por `y↦Ay+d`,
con `A=s√2>0`. `fourier_affine_norm` demuestra el cambio exacto de la norma
Fourier bajo esa reparametrización, sin perder el factor A⁻¹.

`tangentSlice_second_order_bound` demuestra para la sección real x arbitraria:

`‖𝓕(tangentSlice δ τ s b x)(u)‖ * |A*(sectionRotation τ)₀-2πu|²`

`≤ A*16δ(δ+1)`.

`summable_of_shifted_square_bound` conserva la posible resonancia como conjunto
finito y compara fuera de ella con una serie p desplazada. Así se obtiene
`tangentSlice_spectral_summable`, la primera condición exacta de Poisson.

La segunda se demuestra por otra representación: los coeficientes transportados
del módulo anterior y la cota de Ψ en su segunda coordenada. Al variar la segunda
frecuencia entera n, esa coordenada es `τ₁-c*u-c*n`, con
`c=(2π/s)*√6/6>0`; la fase tiene norma uno y el jacobiano es constante.
`tangentCoefficient_spectral_summable` demuestra su sumabilidad.
`integral_finTwo_sections` y `tangentPartial_fourier` identifican estos
coeficientes con la transformada iterada mediante Fubini y la integrabilidad
bidimensional ya probada. Por tanto `tangentPartial_spectral_summable` es
exactamente la segunda condición requerida, no una condición distinta sobre
una función parecida.

`tangentProfile_compact` transporta el soporte mediante un homeomorfismo afín.
Un recubrimiento compacto común por una caja justifica la continuidad y el
soporte de la función intermedia, la sumabilidad de sus traslaciones y el
intercambio de las series intermedias. `tangent_poisson` aplica entonces
`poisson_two_iterated` sin hipótesis espectrales adicionales: δ≥0, s>0 y τ,b
arbitrarios. `tangent_poisson_identified` expone jacobiano, fase y frecuencia.

`tangent_layer_poisson` especializa la traslación b=s*layerShift k. Para el
perfil principal de cada capa obtiene exactamente la suma iterada espacial
igual a `(s²√3)⁻¹` por la suma iterada dual de

`exp(-2πi*k*(m+n)/3) * psi δ (τ-(2π/s)*dualCoordinate m n)`.

`tangentProfile_zero_depth` verifica además la anulación puntual en δ=0 por una
vía directa. Los controles de modo cero, escala y traslación nula del módulo
anterior permanecen vigentes. La identidad es iterada: no se afirma aquí
sumabilidad absoluta conjunta de la serie dual ni reordenaciones arbitrarias.

Código y pruebas permanentes en `AliceLayers/TangentSpectral.lean`; 20 teoremas
nuevos añadidos al guard estándar (151 auxiliares). Registro completo en
`verification/tangent_spectral01/`; intentos de construcción conservados en
`verification/tangent_spectral_build01.log` a `tangent_spectral_build08.log`.
Los primeros logs recogen fallos de normalización, coerciones y Fubini; el
octavo intento compiló el módulo completo. No hay nuevas mutaciones,
comparador específico ni revisión externa.
La verificación completa final terminó con `success: true`: 25 módulos
compilados, los 151 auxiliares bajo el guard estándar y las 18 definiciones
copiadas iguales. Pasa `git diff --check`. Herramientas sigue en `97292a9` con
estos avances locales sin commit; el paper congelado conserva el SHA-256 del
contrato. No hubo llamadas a proveedores ni escrituras en QCA.

Pendiente: conectar esta identidad del perfil principal con la capa finita
reindexada del perfil original, tratar sus diferencias y demostrar las cotas
uniformes del resto exigidas por `AliceLayersB`. No se ha demostrado esa
asintótica ni cambiado el alcance científico del contrato.

## Publicación y continuación 2026-11-11: perfil finito original

Por orden explícita del usuario se publicó primero el bloque anterior en
`origin/main`, commit `097afac86fa71f26f8de9be695335b4a5cc4f602`. Se comprobó
`git ls-remote origin refs/heads/main == HEAD` y el árbol limpio antes de escribir
esta continuación. Los cambios de este apartado son posteriores y quedan
separados de ese commit. Se verificaron los hashes de las 25 fuentes del último
registro antes de publicar. Los logs brutos de Lean conservan sus espacios de
diagnóstico mediante la regla acotada `verification/.gitattributes`.

`FiniteProfile.lean` introduce para cada índice de capa k:

- profundidad `δ = N/4-k/√3`;
- profundidad efectiva `d = δ-2δ²/N`;
- escala `s = 1/√(N/2)` y coordenada normalizada `σ=s*(layerShift k+tangentMap p)`.

`finite_cutoff_algebra` y `finite_profileF_identity` demuestran para N>0 la
identidad exacta, incluso fuera de la esfera:

`profileF = (64/N²) * (d-|σ|²)₊²`.

Por tanto `finite_profileS_identity` identifica exactamente el argumento del
seno como `z=(32π/N²)*(d-|σ|²)₊²`. No se ha sustituido sin(z) por z.
`effectiveLayerDepth_of_active_layer` demuestra d≥0 en toda capa presente en
la amplitud, usando el dominio esférico exacto ya probado. La identidad de
soporte se comprueba también por la vía original: fuera de `aliceSites N`,
`16*sqNorm>N²`, el recorte original es cero y, por la igualdad anterior, lo es
el kernel efectivo. `finite_effective_sum_eq_tsum` extiende la suma finita a
ℤ² sin introducir una cola espacial; la extensión tiene soporte finito y los
intercambios de sumas quedan justificados. `finite_effective_poisson` aplica
entonces la identidad tangencial al kernel de profundidad d.

Los errores se definen por sus expresiones originales, no como una diferencia
abstracta entre el resultado buscado y la amplitud. Con
`b_N=N^(-3/2)*boundaryResource`, son:

- error del seno: `(sin(z)-z)*resource N x`;
- error radial: `z*(resource N x-b_N)`.

`finite_profile_error_split` prueba su ensamblaje puntual exacto. Su suma con
la fase tangencial da `finiteLayerError`, una suma finita explícita. No se
atribuye todavía a estos errores una cota en N, δ o frecuencia.

`normalized_layer_phase` verifica que `tau N η` con σ conserva exactamente la
fase transversal original. `principalLayer_prefactor` recupera el mismo
`leadingScale N` de `Targets.lean`, usando el puente de potencias ya probado;
no divide por `boundaryResource` ni presupone su positividad. La fase normal
y el peso exponencial por capa permanecen en `layerGlobalFactor`.

`amplitude_finite_profile_poisson` demuestra finalmente, para todo N>0, t y η:

`amplitude N t η = Σ capas activas globalFactor *`

`(leadingScale N * layerDualSum N k (tau N η) + finiteLayerError N k (tau N η))`.

La serie dual usa Ψ en la profundidad efectiva d, con los desplazamientos y la
fase ya demostrados. Ésta es una conexión exacta con la amplitud original, no
todavía con `sPlus` a la profundidad δ. Restan el cambio d→δ, el control del
error del seno y radial, los modos duales no nulos, las capas profundas y el
paso de los índices finitos a la serie infinita de profundidades. Ésas son
obligaciones del bloque 4; `AliceLayersB` sigue abierto.

Procedencia: continuación local posterior a `097afac`; contrato y paper
congelado sin cambios. Código permanente en `AliceLayers/FiniteProfile.lean`,
19 teoremas nuevos añadidos al guard estándar (170 auxiliares). Registro de
verificación en `verification/finite_profile01/`. Los intentos de construcción
se conservan en `verification/finite_profile_build01.log` a
`finite_profile_build05.log`: los fallos fueron de elaboración de la
caracterización de soporte, inferencia del filtro de suma y asociación de
productos; el quinto intento compiló el módulo completo. Sin nuevas mutaciones,
comparador específico ni revisión externa.
La verificación completa terminó con `success: true`: 26 módulos compilados,
170 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
Pasa `git diff --check`. `HEAD` sigue siendo el commit publicado `097afac`;
el árbol queda con los cambios locales posteriores de esta conexión, sin un
segundo commit ni push.

## Publicación y continuación 2026-11-11: cotas uniformes del resto

Se publicó primero la conexión exacta del apartado anterior en `origin/main`,
commit `86bd60912a13022246d4ee9f1884c0527d1c6ec4`. Antes de publicar se comprobó
que el registro de 26 módulos y sus hashes seguían vigentes; después se
comprobó la igualdad del SHA remoto con HEAD y el árbol limpio. Este apartado
y `RemainderBounds.lean` son cambios posteriores, sin un segundo commit.

El módulo nuevo demuestra constantes explícitas y sus hipótesis:

1. `sinc_integral_cos` representa sinc como integral de cosenos en [0,1],
   incluyendo el argumento cero. De ahí se obtiene un módulo Lipschitz global.
   Con `M=resourceBound=4π|cResource|`, para todos ρ,σ:
   `|phi0 ρ|≤M` y `|phi0 ρ-phi0 σ|≤M|ρ-σ|`. No se introduce un denominador
   que requiera separar el argumento cero.
2. `sine_remainder_quadratic` demuestra `|sin z-z|≤z²/2` para z≥0, integrando
   la cota de `cos t-1`. Esta cota cuadrática, aunque no óptima, basta para
   la estimación que se demuestra después.
3. `radial_boundary_distance` obtiene directamente del soporte esférico
   `|sqrt(sqNorm x)/N-1/4|≤δ/N` para cada punto activo de profundidad δ.
   Se controla por tanto el recurso con `N^(-3/2) M`, y su diferencia respecto
   al recurso de frontera con `N^(-3/2) M δ/N`.
4. Las cotas puntuales del seno y del recurso se suman mediante una cota
   geométrica del número de puntos, no mediante el tamaño de toda la caja:
   `card(layerCoordinates N k)≤8(Nδ+1)`, para N>0 y δ≥0. La prueba centra
   ambas coordenadas enteras en k/3, comprueba su radio mediante la norma
   tangencial y cuenta los enteros en los intervalos correspondientes.

`finiteLayerError_uniform_decay` demuestra para N≥1, δ≥0 y toda τ:

`‖finiteLayerError N k τ‖ ≤ P(δ)/(N³√N)`, donde

`P(δ)=8(δ+1)M*((32π)²δ⁴/2+32πδ³)`.

Ésta es una cota absoluta por capa, uniforme en frecuencia y N, con un
polinomio explícito en la profundidad. No es todavía una cota del resto total.

La suma por capas también queda controlada para estos dos errores. Se
construye el índice natural `j=floor(√3N/4)-k` para cada capa activa y se prueba
su inyectividad, la identidad `δ=(theta N+j)/√3` y la cota δ≤j+1. Para t>0,
`weightedDepthEnvelope_summable` demuestra la convergencia de

`G(t)=Σ j≥0 (j+2)^5 exp(-t*j)`.

Definiendo `C0=8M*((32π)²/2+32π)` y `C(t)=C0*G(t)`, se prueba

`‖Σ capas activas layerGlobalFactor N t η k * finiteLayerError N k (tau N η)‖`

`≤ C(t)/(N³√N)`.

La constante no depende de N, η ni theta N; t se mantiene fijo y positivo.
`alpha_bounds`, `criticalCoshSquared_gt_one` y `criticalTilt_pos` demuestran
esa positividad para el parámetro exacto del contrato, sin usar su aproximación
decimal. `critical_weighted_finiteLayerError_bound` aplica por ello la cota al
peso crítico real. No se ha dividido por `boundaryResource`; la cota es
absoluta, no una estimación relativa normalizada por `leadingScale`.

Para el cambio de profundidad, el módulo demuestra por separado un módulo
uniforme en frecuencia para Ψ, incluyendo el movimiento de su soporte:

`‖psi δ τ-psi d τ‖≤8δ(δ+1)²(δ-d)` para 0≤d≤δ.

Con d=δ-2δ²/N resulta

`‖psi δ τ-psi d τ‖≤16δ³(δ+1)²/N`.

Esta última cota es por modo: no justifica sumarla sobre todos los modos
duales. Falta un control de decaimiento sumable para ese paso.

Estado de las obligaciones del resto:

- Errores finitos del seno y del recurso: cota absoluta uniforme después de
  sumar todas las capas, al peso crítico, demostrada como arriba.
- Cambio d→δ: cota uniforme por modo demostrada; pendiente su ensamblaje y
  suma en las contribuciones que correspondan.
- Modos duales no nulos, eliminación de fase normal, paso a la serie infinita
  de profundidades y control de sus colas: pendientes.
- Normalización final, testigos uniformes y `AliceLayersB`: abiertos.

Procedencia: `86bd609` más esta continuación local, paper congelado y
dependencias del contrato. Hay 36 teoremas nuevos en el guard estándar
(206 auxiliares en total). Registro completo: `verification/remainder_bounds01/`.
Los intentos y fallos están en `verification/remainder_bounds_build01.log` a
`remainder_bounds_build13.log`; el último compiló el módulo antes de la
verificación completa. No hay comparador específico, nuevas mutaciones ni
revisión externa de estos enunciados. No se afirma el cierre de la asintótica.
La verificación completa terminó con `success: true`: 27 módulos compilados,
206 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
Pasa `git diff --check`; el paper conserva el SHA-256 del contrato. Se volvió
a comprobar al finalizar que `origin/main` y HEAD coinciden en `86bd609`.
Los cambios posteriores de estas cotas quedan locales, con índice vacío,
sin segundo commit ni push; no hubo llamadas a proveedores ni escrituras en QCA.

## Continuación 2026-11-11: contribuciones duales no nulas

`DualDecay.lean` trata la insuficiencia de la cota de segundo orden para sumar
en dimensión dos. El módulo obtiene un decaimiento cúbico conservando los saltos
de la segunda derivada. En una sección con `a=δ-x²>0`, esa derivada es el
polinomio `12y²-4a` en `(-√a,√a)` y cero fuera. Sus valores límite en ambos
extremos son `8a`, no cero. La tercera integración por partes incluye los dos
términos de borde y la integral interior de `24y`. Se acotan sus normas por
`16a+48a=64a`. La restricción al intervalo real se justifica casi en todas
partes, sin afirmar igualdad puntual del polinomio en los extremos. Las
secciones degeneradas se tratan por anulación del perfil.

`psiSlice_third_order_bound` demuestra, sin dividir por frecuencia:

`‖𝓕(psiSlice δ τ x)(u)‖ * |τ₀-2πu|³ ≤ 64δ`.

Integrando sobre la coordenada restante y usando la simetría demostrada por
Fubini, `psi_third_order_bound` obtiene para δ≥0:

`‖psi δ τ‖ * (|τ₀|+|τ₁|)³ ≤ 1024δ(δ+1)`.

La geometría dual se controla por una reconstrucción explícita de sus índices:
`|m|+|n|≤3*tangentL1(dualCoordinate m n)`. Para `(m,n)≠(0,0)`, el tamaño de
los índices enteros es al menos uno. `dual_shift_separation` demuestra que,
si s>0 y `tangentL1 τ≤π/(3s)`, la frecuencia desplazada satisface

`tangentL1(τ-(2π/s)*dualCoordinate m n) ≥ (π/(3s))*(|m|+|n|)`.

Por tanto cada modo no nulo está acotado por

`27648δ(δ+1)s³/π³ * (|m|+|n|)^(-3)`.

La sumabilidad bidimensional no se presupone: se aplica
`ZLattice.summable_norm_rpow` de Mathlib al retículo entero estándar, se
demuestran su discreción, rango dos y la inyección de ℤ×ℤ, y se compara con
el kernel de norma ℓ¹. `integerL1CubicKernel_summable` demuestra la convergencia
de la suma `K=Σ_(m,n)≠0 (|m|+|n|)^(-3)`. El código anula explícitamente el
término dual cero; el kernel numérico tiene valor cero en ese índice.

`nonzeroDualTerm_summable` establece sumabilidad absoluta conjunta en la bola
anterior. `iterated_dual_zero_split` identifica esa suma con la serie iterada
empleada por Poisson, añade separadamente el modo cero y justifica la igualdad

`layerDualSum = psi d (tau N η) + nonzeroDualSum`,

para d=effectiveLayerDepth y capas activas. Ésta es una afirmación de
convergencia adicional en ese dominio pequeño, no una promoción global de las
identidades iteradas anteriores.

`transverse_l1_bound` y `tau_small_frequency` verifican que la condición angular
se cumple con la escala real `s=1/√(N/2)` cuando `frequencyNorm η≤π/6`,
independientemente de N≥1. Con `s³≤8/(N√N)`, el error dual por capa queda
acotado por `D*δ(δ+1)/(N√N)`, con `D=221184K/π³` independiente de N, k y η.
La profundidad efectiva se acota por la profundidad geométrica antes de sumar.

`weighted_nonzero_dual_bound` usa el índice natural inyectivo de capas y la
serie convergente `G(t)` del módulo anterior. Para todo t>0, y uniformemente
en N≥1, theta N y `frequencyNorm η≤π/6`, demuestra:

`‖Σ capas activas globalFactor * (layerDualSum-psi d (tau N η))‖`

`≤ D*G(t)/(N√N)`.

`critical_weighted_nonzero_dual_bound` lo aplica al peso crítico exacto.
Finalmente, `dual_amplitude_uniform_bound` incluye `leadingScale N` y obtiene

`‖leadingScale N * Σ capas activas globalFactor * (layerDualSum-psi d (tau N η))‖`

`≤ Cdual/N⁴`,

con `Cdual=|(16π/√3)*boundaryResource|*D*G(criticalTilt)` fijo. No se divide
por el recurso de frontera. Se trata de la contribución dual real de la
identidad exacta de amplitud, no de un coeficiente aislado ni de un diagnóstico
numérico. La fuente congelada conserva su SHA-256; la ruta cúbica corresponde
al paso descrito en `../runs/run_0/paper.tex`, líneas 1152–1158, pero aquí se
prueban las condiciones y los términos de borde.

Quedan abiertos la suma del cambio de profundidad **sobre el modo cero**, la
fase normal, el paso del conjunto de capas activas a la serie completa de
profundidades (incluidas las posibles capas sin puntos), las colas y el
ensamblaje final de `AliceLayersB`. Tras separar los modos no nulos no hace
falta sumar sobre toda la red dual la cota uniforme del cambio de profundidad.

Procedencia: `86bd609` más los avances locales de resto y esta continuación;
sin commit/push ni llamadas a proveedores ni escrituras en QCA. Código permanente
en `AliceLayers/DualDecay.lean`, con 30 teoremas nuevos añadidos al guard
estándar (236 auxiliares). Registro completo: `verification/dual_decay01/`.
Los fallos se conservan en `verification/dual_decay_build01.log` a
`dual_decay_build11.log`; el último fallo era la normalización de productos en
la cota final de amplitud, corregida antes de la verificación completa. No hay
comparador específico, mutaciones nuevas ni revisión externa de estos lemas.
La verificación completa terminó con `success: true`: 28 módulos compilados,
236 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
Pasa `git diff --check`. El objetivo `AliceLayersB` sigue marcado abierto en
el registro. HEAD permanece en `86bd609`; las cotas anteriores y esta
continuación permanecen como cambios locales sin commit/push.

## Continuación 2026-11-11: cambio de profundidad del modo cero

`ZeroModeDepth.lean` ensambla la cota por modo del cambio
`d=δ-2δ²/N → δ` sobre todas las capas activas. No se suma sobre frecuencias
duales: éstas ya se han separado en el módulo anterior. Para cada capa activa,
el índice natural j es inyectivo y satisface `0≤δ≤j+1`. Se comprueba

`δ³(δ+1)²≤(j+2)^5`,

por lo que el error está dominado por la misma serie convergente
`G(t)=Σ j≥0 (j+2)^5 exp(-t*j)` para t>0. Las capas activas pueden formar un
subconjunto de esos índices: la prueba usa su inyectividad y una cota de suma
finita por una serie no negativa, sin presuponer que los índices sean consecutivos.

`zeroModeDepthError` se define con el signo **profundidad efectiva menos
profundidad geométrica** y con el peso y la fase normal originales:

`Edepth = Σ capas activas globalFactor * (psi d (tau N η)-psi δ (tau N η))`.

`zeroModeDepthError_uniform_bound` demuestra, para N≥1, t>0 y toda η:

`‖Edepth‖≤16G(t)/N`.

La constante no depende de N, η ni theta N. `critical_zeroModeDepthError_bound`
usa el parámetro crítico exacto, cuya positividad ya está probada.
`zeroModeDepth_amplitude_bound` incluye `leadingScale N` y demuestra

`‖leadingScale N * Edepth‖≤Cdepth/(N³√N)`,

con `Cdepth=|(16π/√3)*boundaryResource|*16G(criticalTilt)`. La cota de este
componente vale para **todas** las frecuencias; no necesita la bola pequeña
utilizada para los modos duales. No se divide por el recurso de frontera.

La formulación independiente `zeroModeDepthError_eq_difference` comprueba el
signo como diferencia exacta entre las dos sumas finitas de modo cero. La
identidad `amplitude_geometric_zero_decomposition` conecta después la amplitud
original con `geometricZeroModeSum`, que ya evalúa Ψ en δ. Mantiene separados
`zeroModeDepthError`, el agregado de modos no nulos y el error finito del perfil.
La identidad es exacta y conserva la fase normal; no sustituye el conjunto
de capas activas por la serie infinita.

`amplitude_geometric_zero_error` combina los tres controles anteriores. Para
N≥1 y `frequencyNorm η≤π/6`, obtiene

`‖amplitude N criticalTilt η-leadingScale N * geometricZeroModeSum N criticalTilt η‖`

`≤ (Cfinite+Cdepth)/(N³√N)+Cdual/N⁴`.

La restricción de frecuencia en esta última estimación procede del control
dual, no del cambio de profundidad. Quedan pendientes retirar la fase normal,
pasar de las capas activas a todas las profundidades (incluidas las posibles
capas sin puntos), controlar las colas, normalizar el resto y ensamblar
`AliceLayersB`. Ese enunciado sigue abierto.

Procedencia: `86bd609` más los avances locales previos y esta continuación;
contrato y fuente congelada sin cambios. Código permanente en
`AliceLayers/ZeroModeDepth.lean`; ocho teoremas nuevos añadidos al guard estándar
(244 auxiliares). Registro completo: `verification/zero_mode_depth01/`.
Los intentos están en `verification/zero_mode_depth_build01.log` y
`zero_mode_depth_build02.log`: el primero conserva dos fallos de asociación
de productos y de elaboración de una desigualdad de suma; el segundo compiló.
Sin comparador específico, nuevas mutaciones ni revisión externa de estos
enunciados. Sin commit/push, llamadas a proveedores ni escrituras en QCA.
La verificación completa terminó con `success: true`: 29 módulos compilados,
244 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
Pasa `git diff --check`; el paper conserva el SHA-256 del contrato. HEAD sigue
en `86bd609` y el índice está vacío. Los avances de cotas y esta continuación
siguen como cambios locales, con `AliceLayersB` explícitamente abierto.

## Continuación 2026-11-11: envolvente en profundidad y fase normal

Ejecución de los bloques 1 y 2 de ORDEN_TRABAJO_2026-11-11.md sobre la base
publicada `21757cb5aa505350bebc97307b87daa202701615`. No se modifican contrato,
definiciones originales, objetivo ni paper congelado.

`DepthEnvelope.lean` demuestra una cota válida para toda frecuencia τ y δ≥0:

`‖psi δ τ‖≤8δ²(δ+1)²`, y `(1+δ)‖psi δ τ‖≤8(δ+1)^5`.

La primera se obtiene del módulo uniforme de profundidad existente con d=0,
usando la anulación del perfil a profundidad cero. Una comprobación por otra
formulación identifica directamente la norma del integrando con el recorte
real al cuadrado, acota la norma de Ψ por su integral y demuestra que Ψ a
frecuencia cero es exactamente esa integral real, incluida como complejo.

Con δ_j=(θ+j)/√3, t>0 y 0≤θ≤1, se prueba

`(1+δ_j)‖depthTerm t θ τ j‖≤8(j+2)^5 exp(-t*j)`.

La serie del lado derecho ya es sumable. Se demuestra la sumabilidad de
`depthTerm` y de `depthMomentTerm=δ_j*depthTerm`, sin restringir τ. Definiendo
`H(t)=8*Σ j≥0 (j+2)^5 exp(-t*j)`, se obtiene `‖sPlus t θ τ‖≤H(t)` y
`Σ j≥0 ‖depthMomentTerm t θ τ j‖≤H(t)`. La constante no depende de θ ni τ.
`critical_depthTerm_summable` lo aplica al t crítico exacto y theta N, para
todo N y τ. Hay 14 teoremas nuevos; registro completo del bloque 1:
`verification/depth_envelope01/`, con `success: true`, 30 módulos compilados,
258 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.

`NormalPhase.lean` demuestra primero la identidad exacta por capa

`globalFactor*psi δ τ = exp(-i*normalFrequency η*δ)*depthTerm t (theta N) τ j`.

Define `unphasedZeroModeSum` sobre las mismas capas activas, sin su fase normal,
y fija el signo mediante

`normalPhaseError = geometricZeroModeSum-unphasedZeroModeSum`.

Usando `‖exp(-iu)-1‖≤|u|`, el primer momento del perfil y la inyección de los
índices activos, prueba para N>0, t>0 y toda η:

`‖normalPhaseError N t η‖≤H(t)*|normalFrequency η|`.

No presupone que los índices activos sean consecutivos. Se demuestra también
la anulación exacta del error cuando `normalFrequency η=0`. La identidad
`amplitude_unphased_zero_decomposition` reconstruye la amplitud original con
esta corrección y los errores anteriores. `amplitude_unphased_zero_error`
da, para N≥1 y `frequencyNorm η≤π/6`, la cota absoluta

`‖amplitude-leadingScale*unphasedZeroModeSum‖`

`≤Cgeometric/(N³√N)+Cdual/N⁴+|leadingScale|*H(criticalTilt)*|normalFrequency η|`.

La restricción de frecuencia viene del control dual anterior; la retirada de
la fase normal vale para toda η. Hay nueve teoremas nuevos en este módulo.
La suma principal sigue siendo finita y sobre las capas activas: no se ha
identificado con sPlus. Falta el bloque 3 (índices omitidos, capas vacías y
colas), la normalización del resto y el ensamblaje final. AliceLayersB sigue abierto.

Los intentos se conservan en `verification/depth_envelope_build01.log` a
`depth_envelope_build03.log` y `verification/normal_phase_build01.log` a
`normal_phase_build05.log`. Los últimos compilaron; los anteriores conservan
fallos de elaboración, coerciones, sintaxis y el namespace de un lema de Mathlib.
El registro conjunto `verification/normal_phase01/` terminó con `success: true`:
31 módulos compilados, 267 auxiliares bajo el guard estándar y las 18
definiciones copiadas iguales. Pasa `git diff --check`; HEAD sigue en `21757cb`
y el índice está vacío. No hay comparador específico ni nuevas mutaciones o
revisión externa de estos 23 lemas. Sin commit/push, proveedores ni escrituras
en QCA. El SHA-256 del paper coincide con CONTRACT.md.

## Continuación 2026-11-11: todas las profundidades, capas vacías y colas

Implementación del bloque 3 sobre `28e45ad10f73597af2fd2fb134c1b14173d0c3e0`.
Código permanente en `AliceLayers/DepthGeometry.lean` y
`AliceLayers/DepthCompletion.lean`; 25 teoremas nuevos añadidos al guard estándar.

`depthPlaneIndex N j=floor(√3N/4)-j` representa cada índice natural, también
los que no corresponden a capas activas. Se demuestran su profundidad exacta
`δ_j=(theta N+j)/√3`, la inversión del índice natural y la equivalencia entre
pertenencia a `activeDepthIndices N` y existencia de un punto original en ese
plano. La suma finita sin fase se reindexa sobre este conjunto finito exacto;
no se sustituye por un intervalo de enteros consecutivos.

Para la geometría de las capas vacías se construye en cada plano k el punto
entero `(a,a,k-2a)`, con `a=k/3` (división entera). Su radio tangencial al
cuadrado es `(2/3)*(k-3a)^2≤3`, usando el resto entero entre 0 y 2. Si el
plano está inactivo y 0≤δ≤N/2, el dominio esférico exacto implica
`δ*(N/2-δ)<3`. En consecuencia, todo índice omitido satisface

`δ_j≤12/N` o `δ_j>N/4`, para N>0.

La primera alternativa cubre las capas superficiales sin puntos; la segunda
incluye las capas profundas, los posibles huecos profundos y toda la cola
fuera de la esfera. No se afirma que una capa vacía tenga Ψ nulo.

Con `G(t)=Σ j≥0 (j+2)^5 exp(-t*j)`, t>0, se prueban cotas separadas:

- Si `δ_j≤12/N`, `‖depthTerm t θ τ j‖≤(96/N)*(j+2)^5 exp(-t*j)`.
- Si `δ_j≥N/4`, `‖depthTerm t θ τ j‖≤(32/N)*(j+2)^5 exp(-t*j)`.

La segunda usa el primer momento uniforme del bloque 1. Es un ajuste de método
al plan: se controla la cola con una cota O(1/N), suficiente para el objetivo,
sin afirmar la estimación exponencial más fuerte inicialmente propuesta.
Las cotas por término valen para 0≤θ≤1 y toda τ. Se acotan tanto la subserie
profunda completa como la subserie de índices superficiales omitidos.

`depthCompletionError` suma, con sumabilidad demostrada, exactamente sobre el
complemento natural de `activeDepthIndices N`. El signo se fija por la identidad

`depthCompletionError = sPlus-unphasedZeroModeSum`.

Para N>0 y toda τ, `depthCompletionError_uniform_bound` demuestra

`‖depthCompletionError N t τ‖≤96*G(t)/N`.

La constante no depende de N, theta N ni τ. Se aplica al t crítico exacto;
para N≥1 se prueba además la cota requerida `96*G(t)/√N`. La identidad
`depthTerm t 0 τ 0=0` comprueba directamente el caso de profundidad cero.

`amplitude_full_depth_decomposition` reconstruye la amplitud original con
`sPlus+normalPhaseError-depthCompletionError+zeroModeDepthError+nonzeroLayerAggregate`
dentro del prefactor, más el error finito del perfil. La estimación correspondiente
para N≥1 y `frequencyNorm η≤π/6` es

`‖amplitude-leadingScale*sPlus‖`

`≤Cgeometric/(N³√N)+Cdual/N⁴`

` + |leadingScale|*(H(criticalTilt)*|normalFrequency η|+96*G(criticalTilt)/N)`.

Ésta sigue siendo una cota absoluta. No se ha dividido por boundaryResource
ni normalizado el resto de Targets.lean. Quedan los bloques 4 y 5;
AliceLayersB permanece abierto.

Los intentos se conservan en `verification/depth_geometry_build01.log` y
`depth_geometry_build02.log`, y en `verification/depth_completion_build01.log`
a `depth_completion_build04.log`. Los últimos compilaron; los fallos previos
corresponden a normalización de expresiones, elaboración de coordenadas y
el argumento de una desigualdad de potencias. Registro completo:
`verification/depth_completion01/`, con `success: true`, 33 módulos compilados,
292 auxiliares bajo el guard estándar y las 18 definiciones copiadas iguales.
Pasa `git diff --check`; el SHA-256 del paper coincide con CONTRACT.md. HEAD
sigue en `28e45ad` y el índice está vacío. Sin comparador específico, mutaciones nuevas
ni revisión externa de estos lemas. Sin commit/push, proveedores o escrituras
en QCA. Paper y contrato conservados.

## Continuación 2026-11-11: resto normalizado

Implementación del bloque 4 sobre `8da0e09231ca9d7d6b6d5ea8861df3777be5ab18`.
Código permanente en `AliceLayers/NormalizedRemainder.lean`, con 15 teoremas
nuevos añadidos al guard estándar. Contrato, Targets.lean y fuente congelada
sin cambios. No se ensambla aún un teorema de AliceLayersB.

`boundary_sinc_lower` demuestra `sinc(k/4)≥3/4` para 0≤k≤1, a partir de la
cota Lipschitz global y sinc(0)=1. El kernel del recurso de frontera es
continuo y no negativo en [0,1], y estrictamente positivo en k=1/2. Por la
positividad de la integral y del coeficiente exacto cResource, se demuestra
`boundaryResource>0`, sin aproximaciones decimales ni hipótesis nuevas.

Definiendo `L0=(16π/√3)*boundaryResource`, se prueban `L0>0` y, para N>0,

`leadingScale N = L0/(N²√N) > 0`.

Sólo después de esa prueba se define y utiliza el resto normalizado explícito

`E=(amplitude-leadingScale*sPlus)/leadingScale`.

`normalizedRemainder_identity` reconstruye exactamente la amplitud original:

`amplitude=leadingScale*(sPlus+E)`.

Como comprobación de las potencias, se prueban identidades separadas para
los dos restos absolutos anteriores. El geométrico, al dividir por leadingScale,
es `(Cgeometric/L0)/N`; el dual es `(Cdual/L0)/(N√N)`. No se absorben esos
factores mediante estimaciones antes de comprobar sus identidades exactas.

Con `A=|Cgeometric|/L0`, `B=|Cdual|/L0`, `J=depthCompletionConstant criticalTilt`
y `H=depthEnvelopeConstant criticalTilt`, todos no negativos, se demuestra
para N≥1 y `frequencyNorm η≤π/6` la cota por componentes

`‖E‖≤A/N+B/(N√N)+H*|normalFrequency η|+J/N`.

`normalizedTotalConstant=A+B+J+H` es una constante fija no negativa,
independiente de N, η y theta N. `normalizedRemainder_uniform_bound` prueba
exactamente la forma exigida para el error en Targets.lean:

`‖E‖≤normalizedTotalConstant*(Real.rpow N (-1/2)+|normalFrequency η|)`.

La equivalencia `Real.rpow N (-1/2)=1/√N` se prueba para N>0. Las hipótesis
de frecuencia son las ya usadas para el control dual; no se ha reducido la
bola π/6. Queda el bloque 5: construir los testigos del enunciado completo,
ampliar comparadores/mutaciones críticos y comprobar fidelidad al paper.
Una compilación y el guard no son revisión externa ni prueba de novedad.
AliceLayersB sigue marcado abierto.

Los intentos están en `verification/normalized_remainder_build01.log` a
`normalized_remainder_build03.log`; el último compiló el módulo. Los fallos
previos conservan los problemas de elaboración de potencias reales y de la
normalización de expresiones, corregidos sin cambiar los enunciados requeridos.
Registro completo: `verification/normalized_remainder01/`, con `success: true`,
34 módulos compilados, 307 auxiliares bajo el guard estándar y las 18
definiciones copiadas iguales. Pasa `git diff --check`. HEAD sigue en `8da0e09`
y el índice está vacío; los cambios de este bloque permanecen locales.
Sin comparador específico ni mutaciones nuevas o revisión externa de estos
lemas. Sin commit/push, proveedores ni escrituras en QCA. El SHA-256 del paper
coincide con CONTRACT.md.

## Continuación 2026-11-11: ensamblaje y comparador final

El bloque 5 usa `AliceLayers/Assembly.lean` sobre la base publicada `8da0e09`
más el bloque 4 local. El teorema `aliceLayersB_proved : AliceLayersB` ensambla
exactamente la proposición anterior de Targets.lean. No se cambia ese archivo,
sus definiciones ni el contrato. `aliceLayersB_explicit_witnesses` fija r₀=π/6,
N₀=2, C=normalizedTotalConstant y E=normalizedRemainder N η. C se elige antes
de N y η; la sumabilidad de depthTerm se aporta explícitamente.

Hay seis teoremas nuevos en Assembly: el enunciado completo, la versión con
testigos explícitos, tres formulaciones existenciales de constantes uniformes
para fase, complemento de profundidades y resto normalizado, y la igualdad
del recurso de frontera con la integral impresa en el paper. Esta última
incluye el caso k=0 por separado antes de usar sinc(k/4)=sin(k/4)/(k/4).
El primer intento de ese lema falló por elaboración de la función bajo la
integral; se conserva en `verification/assembly_build01.log`. El segundo
compiló (`assembly_build02.log`). No hubo fallo del ensamblaje del target.

La comprobación documental de la fuente congelada está en
`FIDELITY_ALICE_LAYERS_B.md`, con líneas concretas y límites. La representación
radial escalar es la definición del desarrollo; no se añade una formalización
de la reducción angular de la integral tridimensional original. La igualdad
de frontera sí está demostrada formalmente. La lectura documental la hace el
mismo agente; no es revisión externa ni de otra familia.

`AliceComparator/FinalChallenge.lean` importa sólo Mathlib y copia exactamente
39 definiciones, sin estructuras propias. `final_comparator_sources.json`
registra sus fuentes y hashes. Se cubren once afirmaciones de la orden de trabajo:
target completo, testigos fijos, positividad e integral de frontera, signo y
uniformidad de fase, pertenencia a los índices activos, signo y uniformidad del
complemento de profundidades, identidad y uniformidad del resto normalizado.
Cada conexión de `FinalSolution.lean` usa el teorema original mediante `@`;
`FinalAxioms.lean` audita sus once pruebas. El comparador no proporciona una
revisión individual de todos los auxiliares ni interpreta el significado físico.

Generadores y registros: `write_final_comparator.py` conserva la procedencia del
Challenge, conexiones, manifiesto y `mutaciones_final.toml`; no sobrescribe los
artefactos existentes. `build_final_comparator.py` compila los tres módulos
finales contra dependencias verificadas, sin un filtro previo de igualdad
textual que sustituya el rechazo en Lean. El motor común `lean-mutar` no se
modifica. Procedencia herramientas: `8da0e09` más bloques 4 y 5 locales.

La verificación previa completa `verification/assembly_pre_mutations01/` terminó
con `success: true`: 38 módulos, 313 auxiliares bajo el guard estándar, once
pruebas del comparador final bajo el mismo guard y 57 comparaciones textuales
de definiciones copiadas (39 del comparador final, 18 de los anteriores).
El target escalar ya tiene prueba formal en ese registro. La campaña
`verification/final_mutations01.json` terminó con `PASA`: 51/51 mutaciones
`RECHAZADA` (39 de definiciones, once de afirmaciones y un sorry), compilación
limpia inicial y final con código 0. Las alteraciones de definiciones y de
afirmaciones fallaron en FinalSolution por incompatibilidad de tipos; el sorry
falló en FinalAxioms con sorryAx. No hubo `ACEPTADA`, `FALLO_DISTINTO` ni timeout.
Se comprobaron después los hashes de ambos archivos mutados: restauración
byte a byte. El registro es sobre trabajo local aún sin commit, identificado
por los hashes, no sobre una publicación nueva.

La verificación completa posterior `verification/assembly_final01/` terminó
con `success: true`: 38 módulos, 313 auxiliares bajo el guard estándar, once
pruebas del comparador final y 57 comprobaciones textuales iguales. Los hashes
de las fuentes compiladas y de verify.py siguen vigentes tras la campaña.
El inventario de mutaciones detecta cambios
de enunciado, incluso algunos matemáticamente equivalentes o más débiles:
no demuestra que cada variante rechazada sea matemáticamente falsa.

La proposición escalar formal no abarca Bob, todo el lema Layers, el paseo
completo ni la novedad científica. La revisión externa de fidelidad y del
argumento sigue sin realizarse. Sin proveedores, escrituras en QCA ni commit/push.

Resultado del encargo: cinco bloques formales completados; el target escalar
original está demostrado en Lean. Se conservan contrato y SHA-256 del paper;
pasa `git diff --check`, el índice está vacío y HEAD sigue en `8da0e09`.
Bloques 4 y 5 permanecen locales, separados de la última publicación.
