# Lista canónica de resultados de esta preparación

Fuente: CONTRACT.md y AliceLayers/Basic.lean. Esta lista entra al comparador original; el comparador adicional se enumera abajo.

1. phase_sub_center: separar la fase respecto del centro de Alice.
2. transverse_phase: si la frecuencia tiene suma de componentes cero, se elimina
   la fase global del centro.
3. finite_phase_bound: desigualdad triangular para una suma finita con fases
   unitarias y pesos reales; no establece una tasa asintótica.
4. layer_profile_identity: identidad racional/polinómica del perfil sin recorte,
   con n distinto de cero; no aporta el dominio geométrico ni el resto analítico.
5. prefactor_identity: recolección de constantes en notación de inversos y raíz;
   el puente a rpow queda explícitamente separado.
6. frame_norm_identity: descomposición ortonormal normal/transversal.
7. support_faithfulness: la esfera completa de Z^3 coincide con la enumeración
   finita definida, sin restringir paridad ni eliminar capas.
8. lattice_layer_decomposition: para cada sitio x, la norma cuadrada es la suma
   del cuadrado de su coordenada normal y el cuadrado de su proyección tangencial.
9. lattice_layer_domain: con N>0, pertenecer a la esfera de Alice equivale a las
   cotas exactas de profundidad y radio tangencial de una capa.

En la versión inicial AliceLayersB y ProfileIntegrability, de Targets.lean,
eran proposiciones abiertas. ProfileIntegrability se probó después en Basic.lean;
el ensamblaje escalar de AliceLayersB y su comparador final se describen abajo.
Los nueve puntos anteriores conservan el alcance del comparador original.

## Comparador nuevo: regularidad y Fourier

El comparador adicional `AliceComparator/NewChallenge.lean` cubre, con enunciados
independientes, siete resultados seleccionados de `STATUS.md` y del guard
`AliceLayers/AuxiliaryAudit.lean`:

1. Derivada exacta de `positiveSquare` para todo punto.
2. Regularidad C¹ global de `positiveSquare`.
3. Derivada de la sección real del recorte.
4. Anulación de esa derivada en la frontera.
5. Regularidad C¹ de la sección compleja de Ψ.
6. Identificación de la transformada iterada para frecuencias reales generales.
7. Cota Fourier de primer orden de la sección.

El `Challenge` importa sólo Mathlib. Las cinco definiciones copiadas se cotejan
por texto; la prueba local de continuidad sirve para construir `psiSlice` como
`ContinuousMap`. Se revisó la definición de Ψ de `../runs/run_0/paper.tex`
líneas 1082–1085; el SHA-256 del documento coincide con CONTRACT.md. Esta
comparación cubre esa definición y los enunciados Lean indicados, no prueba
que toda la formulación de Layers(b) sea fiel al paper.

Los demás teoremas posteriores al comparador original, incluidos covolumen,
reindexación, base dual y Poisson condicionado, siguen fuera de la cobertura
independiente de enunciados. Sus guards de axiomas existentes no la sustituyen.
`ProfileIntegrability` fue demostrado posteriormente; la descripción inicial
anterior de que estaba abierto corresponde al estado original y no al actual.

## Comparador de la segunda derivada de la sección

`AliceComparator/SecondChallenge.lean` compara la igualdad casi en todas partes
entre la segunda derivada y su expresión por tramos, y la integrabilidad de esa
derivada segunda. Copia `positiveSquare` y `cutoffSecond`; `verify.py` comprueba
que ambas definiciones coincidan por texto. Los demás lemas del módulo son
auxiliares cubiertos por el guard de axiomas, no por este comparador. No hay una
cota Fourier de segundo orden ni Poisson incondicional entre estos enunciados.

## Comparador final del enunciado escalar y sus pasos críticos

La selección sigue los puntos de validación de la orden de trabajo del bloque 5
y los teoremas del guard `AliceLayers/AuxiliaryAudit.lean`. El nuevo
`AliceComparator/FinalChallenge.lean` importa sólo Mathlib, copia 39 definiciones
y no importa estructuras propias del proyecto. Las once afirmaciones son:

1. `FullScalarClaim`: exactamente AliceLayersB, de Targets.lean.
2. `ExplicitWitnessesClaim`: r₀=π/6 y N₀=2, con C fijo antes de N y η.
3. `BoundaryPositiveClaim`: positividad del recurso de frontera.
4. `BoundaryIntegralClaim`: igualdad con la integral de frontera impresa en el paper.
5. `PhaseSignClaim`: error de fase = suma con fase menos suma sin fase.
6. `PhaseUniformClaim`: constante independiente de N y η, para cada t>0.
7. `ActiveIndicesClaim`: pertenencia al conjunto finito exacto de índices activos.
8. `CompletionSignClaim`: complemento = serie completa menos suma activa sin fase.
9. `CompletionUniformClaim`: error de completar profundidades ≤C/N, para todo τ.
10. `NormalizedIdentityClaim`: reconstrucción exacta de la amplitud con E explícito.
11. `NormalizedUniformClaim`: error normalizado con la cota requerida y C uniforme.

`FinalSolution.lean` conecta cada afirmación mediante el teorema original,
sin demostraciones sustitutivas; `FinalAxioms.lean` audita sus once pruebas.
La lista de definiciones copiadas y sus fuentes está en
`final_comparator_sources.json`. El generador permanente es
`write_final_comparator.py`. El inventario `mutaciones_final.toml` contiene una
alteración de cada definición, una de cada afirmación y una prueba sustituida
por sorry: 51 en total. El resultado efectivo y las compilaciones completas se
registran en STATUS.md; el inventario por sí solo no acredita que se rechacen.

El teorema `AliceLayers.aliceLayersB_proved` ensambla la proposición escalar
original sin añadir hipótesis. Los auxiliares fuera de esta lista no reciben
un comparador individual nuevo. La auditoría de axiomas de la prueba final
recorre sus dependencias, pero no reemplaza la revisión semántica de cada lema.
La correspondencia leída con la fuente congelada y sus límites están en
`FIDELITY_ALICE_LAYERS_B.md`. Ninguno de estos controles constituye revisión
matemática externa ni una afirmación de novedad o de cierre del paper completo.
