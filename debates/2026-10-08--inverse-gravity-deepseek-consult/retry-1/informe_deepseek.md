<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 783f078e04c4a82d48968494714aefbb25acc81b; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 fa4f0575278ab314cd659ff67b13395712b70abef383df903fbf0afe37ea9e97; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=disabled, max_tokens=8192, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 cf7c5a07ed57d0b90a83e07e92f2952d427bcd27c683ed6678fa28b7d4cd17e5
inicio: 2026-10-08T08:51:47Z  fin: 2026-10-08T08:52:31Z
documento: /home/ignac/qca-causal-cones/theory/INVERSE_GRAVITY_DESIGN_CHARTER.md ; último commit observado: 36c9094 ; sha256 de la copia enviada bb6c8aa24d11962dd3d9cd9f7d5e4e51535443667996d31f84cb076fd063f8eb
documento: /home/ignac/qca-causal-cones/theory/INVERSE_GRAVITY_STATE_FIRST_GATE.md ; último commit observado: 9bd3003 ; sha256 de la copia enviada 1e880761110253cd01e68eb17c32e741032ecfbab86d08ddbcce9b16d96f1bb0
documento: /home/ignac/qca-causal-cones/theory/INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md ; último commit observado: 1798644 ; sha256 de la copia enviada 752c4c7f5264aac6fac95b3fbe84fcd7bbbee3c42d77c113690d48497e013870
documento: /home/ignac/qca-causal-cones/theory/INVERSE_GRAVITY_LOCAL_GATE_GATE.md ; último commit observado: 601463b ; sha256 de la copia enviada bcb105634f5a0216836a3d7f7eb576c0e11ed470d5d5d110b679b7cc6d1d0a09
documento: /home/ignac/qca-causal-cones/theory/INVERSE_GRAVITY_DRESSED_PARENT_GATE.md ; último commit observado: 67fd3b1 ; sha256 de la copia enviada 34f32ff6115d678ba725a43da3ab0fe88841c2b1750b5579828bbb055b5631ef
documento: /home/ignac/qca-causal-cones/reports/2026-10-08--inverse-gravity-dressed-parent.md ; último commit observado: 7774a89 ; sha256 de la copia enviada 4c5042683c22db6329b40c175550c295cf59c5cd7fdfe47757490922dc87e426
documento: /home/ignac/qca-causal-cones/scripts/verify_inverse_gravity_dressed_parent.py ; último commit observado: 67fd3b1 ; sha256 de la copia enviada e7be49c5a5c28a7966a7a5c49da784b124e1fdb349e4d41a65e67c242eb0cc4f
documento: /home/ignac/qca-causal-cones/reports/2026-10-08--inverse-gravity-dressed-parent-certificate.txt ; último commit observado: 7774a89 ; sha256 de la copia enviada 4e73ac2f6a28b11bc80c3564373cba6a80f9dfae81996e804a3b4e70e41f2d9a
entrada_deepseek.txt sha256 6b855e7e0d9a60a0ab156c70db2468e01fc51ccecfe5f1379b283142abbbbe30
respuesta sha256 65dad4bdc759406ed1906d9fbf4a142da74743fc3ea202cea70cda5129f9533d
-->

## (i) Veredicto corto de IG-S1

**Veredicto:** Las afirmaciones centrales de IG-S1 son **válidas bajo sus hipótesis explícitas**, con dos reparaciones obligatorias de formulación y una advertencia de alcance:

- **Válida:** conservación exacta `U_E† K_E U_E = K_E`, localidad estricta uniforme, referencia fundamental explícita, y el intervalo `2 ≤ gap ≤ 16` en el sector físico para los toros admitidos.
- **Reparación obligatoria 1 (formulación):** La afirmación “gap uniforme” debe precisarse como “gap uniforme en L para los toros admitidos L≥6 múltiplo de 6”, no como independencia del volumen en una secuencia arbitraria.
- **Reparación obligatoria 2 (alcance):** El “radio ≤ 4 para todo n” es correcto para la regla especificada, pero la prueba usa fuertemente que `D F D†` tiene cancelación exacta entre ticks (`U_E^n = D F^n D†`). No es una propiedad genérica de un QCA que conserve energía; no debe leerse como obstrucción a otros QCA.
- **Advertencia:** la deducción `gap ≥ 2` usa solo la condición necesaria local `r_x + r_y + r_z = 0 mod 3`. Es correcta para obtener una cota inferior, pero no determina si el gap real es 2, 16 o intermedio en cada volumen.

No encuentro errores de signo, fallos de cancelación, degeneración mal manejada, dependencia ilegítima del volumen o uso indebido del bloque qutrit. El bloque qutrit se usa solo como verificación auxiliar de identidades locales, tal como declara el contrato, y la prueba espacial es independiente.

**Conclusión:** el rechazo de IG-S1 para el objetivo tensorial gapless con propagación z=1 está justificado dentro del contrato. No es un no-go general.

---

## (ii) Hasta cinco objeciones prioritarias al rumbo

1. **Objeción estructural:** La ruta E de IG-S0, en su formulación actual, exige simultáneamente: energía estrictamente local exactamente conservada, referencia fundamental reproducible, y puente energía/quasifase uniforme sobre todo el sector de baja energía. IG-S1 muestra que una realización exacta de los dos primeros puede trivializar el tercero. El contrato IG-S0 no distingue suficientemente entre “condición suficiente de esta ruta” y “necesidad física”.

2. **Objeción de alcance:** El fallo de IG-S1 es por conmutatividad del parent `K_0` y cancelación exacta en ticks. El contrato no exige un análisis previo de si el candidato puede tener espectro con parte no conmutativa relevante en el sector físico. Falta un filtro temprano que distinga “energía conservada trivialmente por conmutación” de “energía conservada con dinámica no trivial”.

3. **Objeción metodológica:** El documento IG-S0 impone una cota `C Λ^(1+η)` con η>0 sobre todo el sector de baja energía, pero no define qué se considera físicamente aceptable cuando el gap es uniforme positivo. IG-S1 satisface formalmente la igualdad en la ventana vacía Λ<2, lo que muestra que el test puede ser vacío. El contrato necesita un criterio de no trivialidad de la ventana de baja energía.

4. **Objeción de prioridad:** La insistencia en energía estrictamente local exactamente conservada antes de cualquier dinámica gapless puede ser una condición innecesariamente fuerte. Una energía local conservada solo en promedio, o una quasilocal conservada, podría permitir el objetivo gravitatorio. El charter no exige conservación exacta estrictamente local; es una imposición de la ruta.

5. **Objeción de cierre:** IG-S1 descarta la receta, pero no proporciona un criterio operativo para distinguir “dressing que solo cambia la representación” de “dressing que introduce interacción espectral nueva”. Sin ese criterio, futuros intentos por conjugación podrían repetir el mismo fallo.

---

## (iii) Tabla de mecanismos A/B con primer test y coste/obstáculo

| | Mecanismo A (prioritario): defecto móvil con energía quasilocal conservada | Mecanismo B (contingencia): parent no conmutante frustrado |
|---|---|---|
| **Objeto inicial** | Álgebra local finita (q=3, celda 729) con sector físico S=V=1; energía `K_L = Σ_x h_x` con términos locales que **no conmutan** en el sector físico pero conservan `[U,K]=0`; `U` definido por circuito de puertas locales, no por exponencial global. | Parent `K_0` con términos proyectores `h_X` que **no conmutan** entre sí dentro del sector físico; vacío único `G_0` no trivial; tick `U` definido por circuito local independiente que conserva `K_0` solo en el sector físico. |
| **Patrón de regla local** | Puertas que intercambian un defecto local (violación de R) entre posiciones vecinas con fase dependiente del entorno; la energía se conserva porque el defecto se transporta, no se aniquila. | Puertas locales que mezclan dos configuraciones de defectos con igual energía total pero distinta distribución espacial; frustración que permite estados de baja energía no trivialmente degenerados. |
| **Hipótesis físicas que ofrece** | Propagación sostenida por movimiento de defectos; gap pequeño o nulo por modos de defecto móvil; referencia seleccionada por mínimo de energía. | Excitaciones de baja energía sin gap uniforme; dinámica no trivial sin cancelación entre ticks; posible rama tensorial colectiva si se elige el sector adecuado. |
| **Qué permanece sin construir** | Prueba de que el gap cierra en el límite IR; puente energía/quasifase; control de dos polarizaciones físicas. | Prueba de que el vacío es accesible; control del gap; existencia de propagación z=1. |
| **Primer test falsable antes de puertas/dispersiones** | Verificar si existe una única regla local con `[U,K]=0`, `U G_E = e^{-iφ} G_E`, y un testigo local `A` tal que `||[U^n(A), B]||` crece con `n` para `B` alejado; sin calcular espectro. | Verificar si existe un circuito local unitario que preserve `K_0` en el sector físico, con `K_0` no conmutante y gap condicional `gap ≥ ε` para algún ε→0 en L→∞; sin proyectar TT. |
| **Razón de prioridad vinculada a objetivo** | Aborda simultáneamente selección de referencia (mínimo de K) y transporte sostenido (movimiento de defectos), requisito previo para z=1. | Si la conservación conmutante trivializa la dinámica, la frustración no conmutante es la única vía restante dentro de la envolvente. |
| **Exigencia del charter que cambiaría** | R1 debe permitir energía quasilocal conservada, no estrictamente local; el puente energía/quasifase debe definirse en un sector con excitaciones no triviales. | La condición suficiente del punto 4 de IG-S0 debe relajarse: la cota `Λ^{1+η}` debe aplicarse solo en el sector con gap→0, no sobre un vacío único. |

---

## (iv) Recomendación de un único siguiente expediente acotado

**Expediente recomendado:** “Determinar si existe un par `(K,U)` con sector físico S=V=1 en la misma envolvente, tal que `K` es suma de términos locales no conmutantes en el sector físico, conservado por un circuito local `U`, y con un testigo local de transporte sostenido”.

**Alcance:**  
- No calcular espectro IR, no calcular dispersiones, no construir materia, no invocar bootstrap gravitatorio.  
- Probar existencia constructivamente con un ansatz específico: defectos de R que se mueven por puertas locales; verificar `[U,K]=0` exactamente; verificar `U G_E = e^{-iφ} G_E`; verificar `||[U^n(A_X), B_Y]||` crece con n para distancias crecientes.  
- Si no se encuentra un par con transporte sostenido en este expediente, cerrar con `CRITICAL_CONSERVED_ENERGY_CONSTRUCTION_OPEN` y reconsiderar la condición de energía estrictamente local exactamente conservada.

**Salida esperada:** o un candidato específico con las tres propiedades, o un fallo acotado que justifique reconsiderar la ruta E de IG-S0. Este es el paso mínimo que evita repetir IG-S1.
