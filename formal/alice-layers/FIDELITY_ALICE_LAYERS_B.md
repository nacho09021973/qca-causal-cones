# Correspondencia del enunciado escalar con la fuente congelada

Lectura local del 2026-11-11. Fuente primaria: `../runs/run_0/paper.tex`, SHA-256
`2075e8402142451b6dc0182f3c923608f11cd8839dcd11061ca844d87fc04cc4`.
La comparación se hizo con ese archivo, no con la revisión bibliográfica aportada
ni con resúmenes de modelos. Procedencia de las herramientas locales: herramientas
`8da0e09231ca9d7d6b6d5ea8861df3777be5ab18` más los cambios locales de bloques 4 y 5.

## Correspondencias leídas

| Objeto | Fuente primaria (líneas de paper.tex) | Definición y comprobación local |
|---|---|---|
| Región de Alice | 403–405: bola de radio N/4 en Z³ | `aliceSites`, `sqNorm`; `support_faithfulness` demuestra que la caja finita no recorta la esfera. |
| Perfil del encoder | 431–436: recorte esférico al cuadrado y seno de πF/2 | `cutoff`, `profileF`, `profileS`; mismos signo y factores. |
| Coeficiente del recurso | 425–427: c_r=√3465/(64π²), escala N^(-3/2) | `cResource`, `resource`; el perfil radial unidimensional es `phi0`. |
| Centro y signo de fase | 947–951: x_*=N uhat/4 y exp(+iη·(x-x_*)) | `centerCoordinate=N/(4√3)`, `phase`, `amplitude`; `phase_sub_center` y la separación normal/transversal comprueban el centrado. |
| Tilt crítico | 563–568: α y fórmula de cosh²(t_*) | `alpha`, `criticalCoshSquared`, `criticalTilt`; se usa el real exacto, no `diagnosticTilt`. La positividad de t_* está probada. |
| Profundidades e índice | 1021–1030: √3δ=θ_N+j, θ_N={√3N/4} y peso exp(-t_*(θ_N+j)) | `theta`, `indexedLayerDepth`, `depthPlaneIndex`, `layerNaturalIndex`, `depthTerm`; identidades formales e inyección sobre los índices activos. |
| Recurso de frontera | 1076–1079: φ_∂=c_r*16π*∫₀¹ k(1-k²)² sin(k/4) dk | `boundaryResource_eq_paper_integral` demuestra exactamente esa igualdad, incluido k=0; `boundaryResource_pos` permite normalizar. |
| Perfil Ψ y serie S_+ | 1082–1085: integral sobre R² y suma de todas las profundidades naturales | `psiIntegrand`, `psi`, `depthTerm`, `sPlus`; integrabilidad y sumabilidad probadas, con complemento de capas vacías y cola explícito. |
| Escala transversal | 1122–1124: τ=√(N/2)η_t | `tau` en una base ortonormal del plano; `frame_norm_identity` comprueba la descomposición de norma. |
| Prefactor principal | 1129 y 1164–1166: N^(-5/2)*(16π/√3)*φ_∂ | `leadingScale`; covolumen √3 y recolección del prefactor formalizados por separado. |
| Resto y uniformidad | 1127–1134: identidad más error C(N^(-1/2)+|η_n|), uniforme en θ_N | `AliceLayersB`; C se elige antes que N y η. `aliceLayersB_explicit_witnesses` fija r₀=π/6 y N₀=2; E se construye mediante `normalizedRemainder`. |

## Límites de esta correspondencia

La afirmación formal es exactamente `AliceLayersB` tal como estaba definida en
Targets.lean antes del cierre. Es el coeficiente escalar de Alice de Layers(b)
cerca del origen, con el spinor fijo χ factorizado. No incluye la expansión de
Bob, la matriz del paseo, el resto del artículo, las otras frecuencias ni la
novedad del resultado.

El paso del recurso tridimensional Φ₀ del paper a su representación radial con
sinc en `phi0` es la reducción angular convencional de una función radial. En
este desarrollo se parte de esa definición radial escalar: no se ha añadido
un teorema Lean de cambio a coordenadas esféricas de la integral tridimensional
del paper. La igualdad del recurso de frontera con la expresión unidimensional
impresa sí tiene una prueba Lean nueva, indicada en la tabla. Debe conservarse
esta distinción al comunicar la fidelidad al modelo completo.

La uniformidad formal usa el valor real θ_N de cada N. Las envolventes auxiliares
se probaron además para θ en [0,1], sin suponer que θ_N esté separado de cero.
No se introdujo una hipótesis de no vaciedad de capas ni un truncamiento en la
amplitud original. La caja finita representa exactamente su soporte esférico.

Esta lectura de correspondencia la realiza el mismo agente que ensambla la prueba.
No es revisión humana ni revisión por otra familia. El comparador comprueba
igualdad por desplegado de definiciones y rechazo de alteraciones; no decide
por sí mismo la interpretación física. La fidelidad externa y la novedad siguen
sin revisión independiente en este encargo. No se hicieron llamadas a proveedores.

## Comparador final y evidencia reproducible

`AliceComparator/FinalChallenge.lean` importa sólo Mathlib; copia 39 definiciones
exactas, sin estructuras del proyecto. `final_comparator_sources.json` enumera
su procedencia y hashes, comprobados por `verify.py`. Contiene 11 afirmaciones
seleccionadas de la orden del bloque 5, del estado y del guard de axiomas:
enunciado completo, testigos fijos, positividad e integral de frontera, signo y
uniformidad de fase, pertenencia a los índices activos, signo y uniformidad del
complemento de profundidades, identidad y uniformidad del resto normalizado.

`FinalSolution.lean` conecta cada afirmación con su teorema mediante `@AliceLayers...`;
`FinalAxioms.lean` audita las once pruebas. Los teoremas auxiliares no seleccionados
no tienen un comparador individual nuevo: sus dependencias sí son auditadas por
el guard del teorema final. Esto no sustituye su lectura matemática.

El generador permanente `write_final_comparator.py` produce el Challenge, sus
conexiones, el manifiesto y `mutaciones_final.toml`. El inventario contiene 39
alteraciones de definiciones, once de afirmaciones y una sustitución por sorry.
`build_final_comparator.py` compila únicamente los tres módulos del comparador
contra las dependencias ya verificadas. No compara texto antes de compilar:
las alteraciones deben fallar en FinalSolution o en FinalAxioms, no en un filtro
Python ni por un Challenge inválido. Resultados efectivos:
`verification/final_mutations01.json` registra PASA, 51/51 rechazos y compilaciones
limpias inicial y final correctas; los archivos se comprobaron restaurados por
hash. `verification/assembly_pre_mutations01/` y `verification/assembly_final01/`
registran success: true, 38 módulos, 313 auxiliares y once conexiones finales
bajo el guard estándar. Se comprueban 57 igualdades textuales de definiciones
entre los cuatro comparadores. Estos registros acreditan el target escalar
definido y sus controles locales, con los límites de correspondencia anteriores.
