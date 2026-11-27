# Comprobación de citas: horizontes dispersivos en paseos cuánticos (2026-11-26)

## Procedencia

- **Fuente del encargo:** informe de Gemini pegado por el usuario en
  `biblioteca/Horizontes Dispersivos en Paseos Cuánticos.md` (150 110 bytes,
  git-ignored). Lo obtuvo el propio usuario fuera de `investigacion-gemini`, con
  un prompt redactado por Claude que no incluía nuestros resultados.
- **Regla:** el informe localiza y no prueba. Cada cita se ha leído aquí en el
  original, en el texto completo del PDF de arXiv obtenido mediante alphaXiv
  (`answer_pdf_queries`), con la página indicada.
- **Alcance:** solo las citas más pertinentes para la línea de canales y
  transmisión. Las demás quedan `[UNVERIFIED]`.

## Citas comprobadas

| Cita | Verificado en el original | Diferencias con Gemini |
| --- | --- | --- |
| Maertens, Bultinck, Van Acoleyen, arXiv:2204.06583v3 (PRB 109, 014309) | **p. 3, Ec. (5):** U_F = T̂_L e^{−iΔtH}, una traslación a la izquierda por paso tras la evolución local. **p. 4, Ec. (8):** ω(k) = v sin(ka)/a − k v_Fl. **p. 5:** fuera del horizonte, un modo hacia la derecha cerca de k = 0 y dos «doublers» hacia la izquierda en ±k*. **p. 6, Fig. 5:** paquete de doubler incidente desde fuera, transmitido con probabilidad f(−ω) y reflejado con f(ω) (numérico). **pp. 7–9, Sec. III.C–D:** modelo hamiltoniano local («leakage»), con estados de dispersión estacionarios y coeficiente de transmisión analítico por WKB y aproximación continua (Ecs. 29–37). | Gemini dice que no constaba si hay tratamiento estacionario. **Sí lo hay:** Sec. III.C «stationary scattering states» y III.D, para el modelo local. Para el Floquet, el tratamiento es numérico. |
| Tarasinski, Asbóth, Dahlhaus, arXiv:1401.2673v2 | **p. 2, Ec. (3.1):** guías sin rotaciones. **p. 3, Ecs. (3.3)–(3.10):** matriz S, con modos de guía normalizados a igual corriente. **p. 6, Sec. VI, Ec. (6.1):** en paseos no equilibrados, \|n₊ − n₋\| canales unidireccionales de transmisión perfecta, igual al enrollamiento en cuasienergía; argumento de rango de los bloques rectangulares de reflexión. | Coincide. |
| Kanda, Fujisawa, Yakubo, Kawakami, Obuse, arXiv:2505.16606v1 | **p. 2, Ecs. (4)–(6):** U = SC(θ). **p. 3, Ec. (22):** θ(x) = θ₀ tanh(ax). Estados de borde por el límite de Dirac; no calcula dispersión ni transmisión. | Gemini no identificó autores ni título: «Fast and high-fidelity transfer of edge states via dynamical control of topological phases and effects of dissipation». |
| Morioka, arXiv:1809.02988v2 (RMP 2019) | **p. 3, (A-1):** C(x) → C₀, **la misma moneda en ±∞**. U = SC de un paso. Matriz S mediante autofunciones generalizadas. | Gemini no pudo leerlo. **Resuelto:** no cubre dos medios distintos. |
| Richard, Suzuki, Tiedra de Aldecoa, «Quantum walks with an anisotropic coin II: scattering theory», arXiv:1801.02779 (LMP 2019) | **p. 1, Ec. (1.1); p. 7, Assumption 3.1:** C(x) → C_ℓ y C_r **distintas**, con convergencia de corto alcance. **p. 9, Teorema 3.3:** existencia y completitud de los operadores de onda para U = SC frente a U_ℓ ⊕ U_r. **p. 11, Proposición 3.4:** los espacios iniciales vienen dados por los signos de las velocidades V_ℓ y V_r. No calcula transmisión explícita. | **Gemini no lo encontró.** Es el antecedente matemático más cercano para dos medios asintóticos distintos, aunque solo para paseos de un paso U = SC. |

## Segunda tanda de comprobaciones (2026-11-26, a petición del usuario)

| Cita | Verificado en el original | Diferencias con Gemini |
| --- | --- | --- |
| Corley, Jacobson, «Lattice Black Holes», hep-th/9709166 (PRD 57, 6269) | **p. 7, Ec. (13):** \|v\|(ω + k) = ±2 sin(k/2), red escalar en caída libre. **pp. 8–10:** conversión de modos en el punto de retorno; los modos salientes vienen de modos entrantes de gran número de onda. **p. 12, Ecs. (21)–(22):** norma conservada y número de partículas saliente. **p. 16, Ec. (38):** espectro de Hawking, válido para κ ≪ ω^{1/3} ≪ 1. Método: WKB más transformada de Laplace. | Coincide. Leí la v1; Gemini cita la v2. |
| Horner, Hallam, Pachos, «Chiral spin chain interfaces exhibiting event horizon physics», arXiv:2207.08840 (PRL 130, 016701) | **p. 1, Ec. (3):** hamiltoniano de campo medio. **p. 3, Ec. (9):** v(x) = α tanh[β(x − x_h)] en el acoplamiento quiral. **pp. 3–4, Fig. 3:** una partícula localizada dentro tunela al exterior con espectro térmico a T_H = αβ/2π (numérico). | Gemini dice que el perfil está en los saltos u_n. En realidad está en el acoplamiento v (u = 1). Matiz menor. |
| Benhemou, Nixon, Deger, Schneider, Pachos, arXiv:2312.14058v4 | **p. 2, Ec. (1):** cadena de saltos; **Ec. (3):** perfil linealizado κ_{j,j+1} = α(j − j_h + 0.5)/4. **p. 3, Ec. (7):** T_H. **p. 4, Ec. (8):** t_f = γ(4πT̃_H)⁻¹. Paseo de un átomo localizado dentro: escape no nulo, numérico. | Gemini no identificó a los autores. |
| Sabsovich, Wunderlich, Fleurov, Pikulin, Ilan, Meng, «Hawking fragmentation and Hawking attenuation in Weyl semimetals», arXiv:2106.14553v3 (PRR 4, 013055) | **pp. 3–4, Ecs. (8)–(9):** matriz S numérica (KWANT) de un horizonte en red con «doublers» y perfil tanh. Una banda pasa con T ≈ 1; en la otra, la mezcla con los doublers tiene probabilidad X = 1/(1 + e^{2πω/α_t}). **p. 1:** sin doublers no hay análogo de Hawking en red. Su ref. [74] da una derivación analítica de la matriz S, que no he leído. | Gemini no pudo leerlo. **Es el antecedente más próximo en método:** matriz S estacionaria de un horizonte en red, numérica y en tiempo continuo. |
| Oguz, arXiv:2610.09814v2 | **p. 2:** «For dispersive index fronts the emitted spectrum is not fixed by the surface gravity alone; the profile of the front and the dispersion relation enter the mode conversion [26–28]». Es una cita a terceros (Linder–Schützhold–Unruh 2016; Jacquet–König 2015; Bermudez–Leonhardt 2016) en un trabajo sobre solitones ópticos. | Gemini lo presentó como resultado del preprint. Es una afirmación citada, con fuente primaria en sus refs. 26–28, que no he leído. |

**Búsqueda propia** (alphaXiv, dos consultas amplias: matriz S o transmisión entre dos medios en DTQW/QCA y análogos de Hawking; paseos con moneda dependiente de la posición que simulan un horizonte). No ha aparecido ningún trabajo con matriz S de un paseo cuántico discreto entre dos medios con cambio de signo de la velocidad de grupo. Aparecen trabajos de dispersión en DTQW con defectos o impurezas en un único medio (arXiv:1912.11555; Matsue et al., arXiv:1708.01052) y análogos de horizonte en otras plataformas (circuitos superconductores, polaritones, Weyl, óptica). Una búsqueda que no encuentra algo no prueba que no exista: la originalidad sigue OPEN.

## Consecuencias para la línea (deducciones de Claude, no de las fuentes)

1. **El mecanismo general es conocido.** En Maertens et al. (Floquet), la
   evolución local seguida de una traslación produce un horizonte con
   «doublers» y transmisión parcial a través de él. Nuestra U = L₋W² tiene la
   misma estructura: L₋ cumple el papel de T_L. Novedad del mecanismo: no.
2. **El enrollamiento fuerza transmisión perfecta hacia la izquierda.** Esto
   aplica a nuestro caso el argumento de Tarasinski et al. (Sec. VI), suponiendo
   que existe una matriz S unitaria sobre I, lo que no está establecido.
   - **Dimensiones:** entran 1 canal interior hacia la derecha y 3 exteriores
     hacia la izquierda; salen 1 canal exterior hacia la derecha y 3 interiores
     hacia la izquierda.
   - **Hacia la izquierda:** el bloque r′, de los canales exteriores entrantes
     al canal exterior saliente hacia la derecha, es 1×3. Por tanto t′†t′ tiene
     al menos dos autovalores iguales a 1: hay **al menos 2 canales hacia la
     izquierda con transmisión perfecta**.
   - **Hacia la derecha:** el bloque t, del canal interior hacia la derecha al
     exterior hacia la derecha, es 1×1. El argumento **no lo restringe**:
     |t|² = 1 − ‖r′‖² puede ser 0.

   Por tanto, nuestra pregunta (¿t ≠ 0?) no la decide el recuento de canales.
3. **Existencia de la matriz S.** Richard–Suzuki–Tiedra la dan para U = SC de
   un paso con monedas asintóticas distintas. Nuestra U es un paseo de varios
   pasos. Si su resultado se extiende al nuestro (agrupando pasos o por otra
   vía) es `[UNVERIFIED]`.

## Tercera tanda (2026-11-27): ref. [74] de Sabsovich et al.

A petición del usuario, para la cuestión bibliográfica del §7 de
`theory/DISPERSIVE_HORIZON_HEURISTIC_PREDICTION_GATE.md`. Ambos artículos se
leyeron en el texto completo de arXiv mediante alphaXiv (`answer_pdf_queries`).
Esta lectura no cambia nada del contrato congelado: X y α ya estaban fijados.

| Cita | Verificado en el original |
| --- | --- |
| Sabsovich et al., arXiv:2106.14553v3 (relectura) | **p. 3:** perfil V_t,1(x₁) = ±(1 + tanh(α_t x₁)), es decir, α_t = V′(0). Su ref. [74] se cita para el límite abrupto. **p. 4, Ecs. (8)–(9):** matriz S *numérica* (KWANT, tiempo continuo). X conecta el modo a₂ de la región normal con el doubler b₃ (agujero blanco). Para el agujero negro, la matriz es la misma «modulo a relabelling» (p. 4; Supl. p. 9). **p. 5, nota final:** [74] da «an analytical derivation of the S-matrix». **Supl. pp. 11–12, Fig. 6:** con perfiles tanh, lineal y arctan del mismo α_t, \|S₃₂\|² sigue X en ω ∈ (0, 0.1) y se desvía por encima. **[74] = De Beule, Groenendijk, Meng, Schmidt, arXiv:2106.14595** (p. 7). |
| De Beule, Groenendijk, Meng, Schmidt, «Artificial event horizons in Weyl semimetal heterostructures and their non-equilibrium signatures», arXiv:2106.14595v4 | **p. 7, Ec. (19):** modelo *continuo* en tiempo continuo, con ω = k[V + λ√(1+k²)]: un modo copropagante v y tres contrapropagantes u, w₁, w₂. **Ec. (26):** punto de retorno en ω_c. **p. 8, Ec. (37):** WKB a primer orden en V′, que exige \|k′/k\|, \|v′/v\| ≪ 1. **p. 9:** horizonte lineal V = 1 + αz, con punto de retorno en z_c = 3\|ω\|^{2/3}/2α. **Ec. (41):** supone \|αz\| ≪ 1 y α, \|ω\| ≪ 1. **pp. 10–12, Ecs. (42)–(55):** solución hipergeométrica cerca del horizonte, empalmada con WKB. T_{u←w₁,₂} = R_{u←w₂,₁} = 1/(1 + e^{±2πω/α}): los modos w, incidentes desde la región tipo II (dentro), transmiten al modo u de baja k de la región normal con X o 1 − X, y reflejan el resto al u interior. A este orden, v queda desacoplado y w₁ y w₂ no se mezclan. **Ec. (62):** normalización a corriente unidad. **p. 12:** «Corrections to this low-energy result yield an energy-dependent Hawking temperature»; el empalme empeora al crecer \|ω\| y α. **p. 5, Ec. (11):** e^{±2πω/ħV′(0)}, es decir, α es la pendiente en el horizonte de la velocidad de grupo de baja k (v_u ≈ V − 1, Ec. (64), p. 13). **p. 19 y App. B:** la red de KWANT (discretización del modelo continuo) concuerda «perfectly» en el límite lento. No da cifras de desviación. |

**Consecuencias para T_ret** (deducciones de Claude, no de las fuentes):

1. **El canal es análogo.** T_{u←w₁} es la transmisión, con flujo unidad, de
   un modo incidente desde dentro, en la rama con punto de retorno, al modo
   saliente de baja k fuera. Es la misma forma que T_ret. En ese modelo, la
   rama sin punto de retorno (w₂) transmite 1 − X, y la reflexión de w₁ va al
   modo u interior.
   - Nuestros datos van en esa dirección: T_ret + T_cont = σ² ≈ 1, y la
     reflexión de la rama de retorno va sobre todo al modo interior de baja k.
   - Esto es una lectura, no una identificación probada.
2. **La definición de α es compatible.** Su α es la derivada espacial, en el
   horizonte, de la velocidad de grupo del modo de baja k.
   - Nuestra hoja de baja k tiene velocidad 8t − 3 en k → 0. **Comprobado**
     (ver «Comprobación propia» abajo).
   - Con t′(0) = 1/(16L), esa derivada es 8t′(0) = 1/(2L): exactamente el α de
     la heurística.
3. **La derivación no se aplica directamente.** Es para un hamiltoniano
   continuo en tiempo continuo, con otra relación de dispersión. Nuestro QCA
   es de tiempo discreto, con 12 raíces y modos adicionales (doublers en
   \|k\| ≈ 2). Aplicarla exigiría:
   - rehacer el empalme WKB más la solución local para el QCA; o
   - apoyarse en la universalidad («no-hair»), que en ambos artículos es una
     comprobación numérica en sus modelos, no un teorema.
4. **El régimen de validez es dudoso en nuestros puntos.** Exige que el
   punto de retorno caiga en la parte lineal del perfil (α z_c ≪ 1).
   - Estimación propia, aproximada y no certificada, que usa
     ω ≈ (8t − 3)k + γk³ con γ = 35/32 fijo (γ comprobado abajo). La
     velocidad local en el punto de retorno, \|v_c\| ≈ 3γ(ω/2γ)^{2/3}, sale
     ≈ 0.09 en s = 1/200, ≈ 0.17 en 1/80, ≈ 0.23 en 1/50 y ≈ 0.27 en 1/40.
   - γ(t) crece hacia el interior (715/256 ≈ 2.79 en t = 5/16), así que
     estas cifras son algo bajas: con γ(t ≈ 0.35) ≈ 1.55 sale ≈ 0.30 en
     s = 1/40. Además, la serie cúbica truncada es dudosa con \|k\| ~ 0.3.
   - El rango asintótico es \|v\| ≤ 1/2. En s = 1/40 el punto de retorno cae
     donde tanh ya se aparta de lo lineal.
   - Así, son esperables desviaciones de X de orden no despreciable a ω
     alta. De Beule et al. no las cuantifican.

**Comprobación propia (2026-11-27)** de la velocidad 8t − 3 y del 35/32.
- Script `scripts/check_dispersive_horizon_low_k_sheet.py`; salida en
  `reports/2026-11-27--dispersive-horizon-low-k-sheet-check.txt`.
- Parte de la dispersión revisada, C2 del verificador de canales:
  2f² − 1 = cos(ω + k), con f = A cos 3k + (1 − A) cos k y A = t(2t − 1).
- Con cos E = f, las bandas son ω = −k ± 2E. La que pasa por k = 0 con
  pendiente −1 + 2(4t − 1) es
  ω = (8t − 3)k + γ(t)k³ + O(k⁵), con
  γ(t) = 16t(t − 1)(2t − 1)(2t + 1) / (3(4t − 1)).
- **Vía 1, exacta (SymPy):** a² = (4t − 1)², por lo que v₀ = 8t − 3, y
  γ(3/8) = 35/32. Al sustituir de vuelta, h = O(k⁶) idénticamente en t.
- **Vía 2, numérica:** raíces de h completa con mpmath a 50 dígitos, en
  t = 5/16, 3/8 y 7/16 y k = 10⁻² y 10⁻³. En k = 10⁻³ concuerdan con la
  serie en 5–6 cifras.
- Además: γ(5/16) = 715/256 y γ(7/16) = 105/256.

## Pendiente de comprobar `[UNVERIFIED]`

- arXiv:2609.03272, 2101.07617, 2306.10719, 2504.15584, 2111.15131 y
  2105.10962 (colas homogéneas o estados ligados; poca relevancia).
- Refs. 26–28 de Oguz. (La ref. [74] de Sabsovich et al. queda leída: ver la
  tercera tanda.)
- Di Molfetta–Brachet–Debbasch y Bisio–D'Ariano–Tosini.
- Wang–Li (fuente secundaria; el DOI no corresponde, según el propio Gemini).
- Coutant–Parentani–Finazzi.
- Una búsqueda propia de trabajos que Gemini pudo omitir, como ya pasó con
  Richard–Suzuki–Tiedra.
