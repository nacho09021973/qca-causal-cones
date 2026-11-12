# Preparación formal de Alice / Layers(b)

Continuación del 2026-11-11: `AliceLayers/Assembly.lean` ensambla el enunciado
escalar `AliceLayersB` con r₀=π/6 y N₀=2. El estado de su verificación completa
y de las mutaciones está en `STATUS.md`: assembly_final01/ pasa con 38 módulos,
313 auxiliares bajo el guard estándar y 51/51 mutaciones rechazadas.
El comparador final legible está en `AliceComparator/FinalChallenge.lean` y el
cotejo de la fuente con sus límites en `FIDELITY_ALICE_LAYERS_B.md`. Los apartados
históricos siguientes describen la preparación original. Bob y el paper completo
quedan fuera del teorema escalar; la revisión externa no se ha realizado.

Esta carpeta separa tres cosas: el diagnóstico numérico previo, los ingredientes
demostrados en Lean y el enunciado asintótico escalar de Targets.lean.
**Compilar Targets.lean sólo comprueba que el enunciado está bien formado.**
Las pruebas de ProfileIntegrability y AliceLayersB están en Basic.lean y
Assembly.lean respectivamente; no se infieren de compilar sus definiciones.

## Qué leer

- `CONTRACT.md`: alcance autorizado y fuente congelada.
- `AliceLayers/Definitions.lean`: red Z^3, esfera finita, perfiles s_N y phi_N,
  fase centrada, recurso radial, t_* exacto, tau, Psi y S_plus.
- `AliceLayers/Targets.lean`: AliceLayersB como proposición explícita, con
  constantes uniformes, N0, sumabilidad de la serie y resto complejo acotado.
- `CLAIMS.md`: lista canónica de los siete ingredientes probados.
- `AliceComparator/Challenge.lean`: enunciados de esos siete ingredientes,
  importando sólo Mathlib y copiando sus nueve definiciones matemáticas.
- `AliceComparator/NewChallenge.lean`: siete resultados adicionales de regularidad y Fourier; sus límites están en `CLAIMS.md`.
- `AliceLayers/Basic.lean`: pruebas; `AliceComparator/Solution.lean` conecta cada
  enunciado con su prueba, y `Axioms.lean` comprueba axiomas estándar.

Se aplica la skill `herramientas/skills/lean_comparador/SKILL.md`, con el patrón
Challenge/Solution/Axioms y `lean-mutar`. El cuerpo del auditor de axiomas se copió
de herramientas/lean/HerramientasLean/AssertAxioms.lean, commit 83c04f9, con una
línea de procedencia añadida. La verificación comprueba que el resto sea idéntico.
No hay estructuras propias importadas por el Challenge. Los nombres de tipos
son notación local para funciones sobre Fin 3 y Fin 2, no nuevos tipos opacos.

## Alcance de los ingredientes

| Ingrediente | Qué establece | Qué no establece |
|---|---|---|
| Fase centrada/transversal | separación exacta y cancelación cuando sum eta=0 | asintóticas |
| Suma con fases | norma <= suma de valores absolutos de pesos | potencia N^-5/2 |
| Perfil por capas | dominio geométrico exacto en coordenadas de la retícula y fórmula tras quitar el recorte positivo | resto del seno |
| Prefactor | combinación exacta de 32 pi, N/2 y covolumen expresado como sqrt3 | Poisson, valor del covolumen ni puente a rpow |
| Marco | identidad de norma normal/transversal | cambio de variables de medida ni Poisson |
| Soporte | la caja filtrada representa toda la esfera de Z^3; el perfil Ψ se anula fuera de su radio | integrabilidad completa y descarte de capas profundas |

No se afirma novedad matemática de estos ingredientes elementales. La comprobación
de axiomas y de mutaciones no sustituye la revisión humana de que los enunciados
expresan fielmente el paper.

## Qué falta para demostrar Layers(b)

1. La integrabilidad del kernel que define `phi0` en `0..1` y la continuidad de
   `phi0` respecto a `ρ` están demostradas. La integrabilidad del perfil
   bidimensional `psiIntegrand` también está demostrada: el integrando es continuo y
   su soporte está contenido en `[-(δ+1), δ+1]^2`. Las integrales de Lean y tsum
   tienen valores por defecto si fallan sus hipótesis; esos valores no se usan como
   sustituto de las obligaciones analíticas.
2. Ya se probaron `x^(-3/2) = 1/(x * sqrt x)` y
   `x^(-5/2) = 1/(x^2 * sqrt x)` para `x>0`, y su ensamblaje en la identidad del
   prefactor escrito con `rpow`. También se probó que, para `n>0` y `q≥0`, la
   condición esférica equivale exactamente a `0≤δ≤n/2` y
   `q≤δ(n/2-δ)`; en ese dominio el recorte positivo desaparece y el perfil tiene
   la expresión por capas del lema `layer_profile_identity`. Siguen pendientes las
   positividades del parámetro crítico y del recurso de frontera.
3. Ya están probadas las coordenadas enteras de cada plano, las entradas de Gram
   de su base y el área √3, la reagrupación finita por fibras y la expresión
   de la profundidad con theta_N y un índice natural. `AliceLayers/Covolume.lean`
   identifica la imagen del plano entero en coordenadas tangenciales y demuestra
   que su `ZLattice.covolume` para la medida de Lebesgue es √3. Falta la
   enlace de la suma finita con la serie del término principal.
   `AliceLayers/Reindex.lean` demuestra la reindexación exacta de las fibras
   por pares enteros, su dominio esférico, la traslación de la red y la
   descomposición de la fase normal y tangencial.
4. `AliceLayers/Poisson.lean` encadena dos fórmulas unidimensionales de
   Mathlib y las especializa a `psiIntegrand` en la red entera estándar. Para
   profundidad no negativa demuestra la sumabilidad uniforme de las traslaciones
   de cada sección sobre compactos. La fórmula sigue condicionada a la existencia
   continua de las secciones transformadas, su sumabilidad y el intercambio de
   sumas. `AliceLayers/PsiIntermediate.lean` construye la función intermedia,
   demuestra su continuidad y soporte compacto, y deduce la condición de
   intercambio de sumas a partir de la primera sumabilidad espectral. Quedan
   dos condiciones de sumabilidad espectral. `AliceLayers/SectionRegularity.lean`
   demuestra regularidad C¹ de las secciones, una integración por partes y
   una cota Fourier de primer orden; no demuestra aún sumabilidad.
   `AliceLayers/SectionSecond.lean` identifica casi en todas partes e integra la
   segunda derivada del recorte real; falta la segunda integración por partes
   para la sección compleja.
   `AliceLayers/PoissonZero.lean` identifica el modo de frecuencia cero
   con la integral bidimensional Ψ mediante Fubini. Para frecuencias reales
   generales demuestra que la transformada iterada es Ψ con frecuencia
   desplazada por −2π(u,v), e identifica cada término de Poisson condicionado.
   `AliceLayers/Dual.lean` demuestra la base dual y su emparejamiento con la
   red trasladada. Faltan completar la adaptación desplazada y escalada y verificar las hipótesis
   restantes para el perfil y estimar los términos de frecuencia y el resto.
5. Sumabilidad uniforme en profundidad y control de las capas profundas.
6. Estimación uniforme del resto E_A y su ensamblaje con el coeficiente principal.

El cache inspeccionado contiene `Mathlib/Analysis/Fourier/PoissonSummation.lean`,
cuya formulación documentada es para funciones R→C. No se declara inexistente
una vía de formalización multidimensional; se identifica el trabajo de adaptación
que no se ha hecho aquí. No se encontró un archivo llamado Bessel en la búsqueda
por nombres; la definición integral de Psi permite enunciar la meta sin depender
de una fórmula especial de Bessel.

Las pendientes finitas del experimento no son hipótesis de ningún teorema Lean.
Incluso una prueba futura de la cota asintótica no certificará por sí sola el
redondeo del programa ni un ajuste de pendientes sobre un intervalo finito.
Bob y el espinor completo quedan fuera de esta preparación.

## Reproducir sin escribir en QCA

Lean 4.31.0 instalado, Mathlib fijado a
`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. `build.py` y `verify.py` leen los
objetos ya compilados de QCA y escriben objetos sólo en `build/` de esta carpeta.
No ejecutan lake dentro del repo QCA ni descargan paquetes. `lakefile.toml`
documenta las bibliotecas; la construcción de esta preparación es offline.

Desde herramientas:

```bash
python3 -I ai_scientist_local/experiments/alice_layers/formalization/build.py
python3 -I ai_scientist_local/experiments/alice_layers/formalization/verify.py \
  --output ai_scientist_local/experiments/alice_layers/formalization/verification/otro-registro
lean-mutar ai_scientist_local/experiments/alice_layers/formalization \
  ai_scientist_local/experiments/alice_layers/formalization/mutaciones.toml \
  --build-cmd 'python3 -I build.py' \
  --salida ai_scientist_local/experiments/alice_layers/formalization/verification/otras-mutaciones.json
```

Los registros exigen rutas nuevas. `write_mutations.py` es el generador permanente
del TOML: siete cambios de enunciado, nueve de definiciones copiadas y una prueba
sustituida por sorry. Las alteraciones deben fallar al conectar Solution; el caso
sorry debe fallar en la auditoría de axiomas. Los archivos se restauran siempre.
El registro diferencia un rechazo esperado de un fallo de compilación distinto.

## Reproducir el cierre escalar y el comparador final

Desde herramientas, la verificación completa incorpora Assembly y los tres
módulos FinalChallenge/FinalSolution/FinalAxioms, y coteja las 39 definiciones
finales con su manifiesto. Elegir carpetas y registros nuevos:

```bash
python3 -I ai_scientist_local/experiments/alice_layers/formalization/verify.py \
  --output ai_scientist_local/experiments/alice_layers/formalization/verification/cierre-nuevo
lean-mutar ai_scientist_local/experiments/alice_layers/formalization \
  ai_scientist_local/experiments/alice_layers/formalization/mutaciones_final.toml \
  --build-cmd 'python3 -I build_final_comparator.py' \
  --salida ai_scientist_local/experiments/alice_layers/formalization/verification/mutaciones-final-nuevo.json
python3 -I ai_scientist_local/experiments/alice_layers/formalization/verify.py \
  --output ai_scientist_local/experiments/alice_layers/formalization/verification/cierre-restaurado-nuevo
```

El compilador focalizado sólo usa objetos de dependencias ya verificados aquí;
por eso se ejecuta verify.py antes y después de las mutaciones. El generador
permanente `write_final_comparator.py` conserva las fuentes de los artefactos
ya presentes y rechaza sobrescribirlos. Los controles usan la herramienta común
`lean-mutar`, procedencia herramientas `8da0e09` más los cambios locales de este
cierre; no se ha modificado el motor compartido para obtener un resultado.
