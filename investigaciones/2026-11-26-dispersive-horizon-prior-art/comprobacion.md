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

## Pendiente de comprobar `[UNVERIFIED]`

- Corley–Jacobson, hep-th/9709166.
- Horner–Hallam–Pachos, arXiv:2207.08840.
- arXiv:2312.14058, 2106.14553, 2610.09814, 2609.03272, 2101.07617,
  2306.10719, 2504.15584, 2111.15131 y 2105.10962.
- Di Molfetta–Brachet–Debbasch y Bisio–D'Ariano–Tosini.
- Wang–Li (fuente secundaria; el DOI no corresponde, según el propio Gemini).
- Coutant–Parentani–Finazzi.
- Una búsqueda propia de trabajos que Gemini pudo omitir, como ya pasó con
  Richard–Suzuki–Tiedra.
