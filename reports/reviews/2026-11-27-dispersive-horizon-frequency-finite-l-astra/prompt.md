# Revisión externa: ejecución del contrato de frecuencia y L finita (F1–F3, horizonte dispersivo)

Autorización: usuario «autorizo la revision de AStra 6.2» (2026-11-27); el contrato fija el modelo
(Q5). Modelo `gpt-6.2-astra` (OpenAI), vía `revision-ciega` del PATH con
`ASTRA_MODEL=gpt-6.2-astra`; generación comprobada antes del envío. Autor del contrato, del
informe y del verificador: Claude (Opus 5.5). Herramientas: `~/herramientas` commit `4a4fcca`.
Revisado: commit `e8952e3` (rama `research/dispersive-horizon-channels`). Máximo: una ronda. No se
autoriza calcular nada nuevo ni promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la **ejecución del contrato de frecuencia y L finita (F1–F3)** para el
paseo cuántico U = L₋W², W = S C(θ) S C(θ) S C(−2θ), t = cos²θ, A = t(2t−1), medios t = 5/16
(x → −∞) y 7/16 (x → +∞); puntos z(s) = (1 − s² + 2is)/(1 + s²). La matriz de transferencia, los
canales y la transmisión con perfil brusco ya pasaron revisiones externas (la transmisión con
REPAIR_REQUIRED solo de interpretación, aplicada como Amendment 1, no re-revisada). Se adjuntan:

(1) `DISPERSIVE_HORIZON_FREQUENCY_FINITE_L_GATE.md`: contrato congelado (`204f33b`), con F1–F3,
    regla de precisión predeclarada, veredictos por punto y de línea, umbral de abandono;
(2) `2026-11-27--dispersive-horizon-frequency-finite-l.md`: informe de ejecución, con veredictos
    de autor y una **objeción principal del propio autor** que lleva a no adoptar el veredicto de
    línea;
(3) `verify_dispersive_horizon_frequency_finite_l.py`: verificador (43 comprobaciones nuevas,
    SHA256 `3d585a54…80faa`, commit `00f09c9`, anterior a su única ejecución);
(4) `verify_dispersive_horizon_transmission.py`: verificador ya revisado que (3) importa sin
    modificarlo (helpers y encierros de z₀, z₁);
(5) `2026-11-27--dispersive-horizon-frequency-finite-l-run-1.txt`: registro de la ejecución
    (43/43 tras 61 + 53 + 33, exit 0);
(6) `2026-11-26--dispersive-horizon-transmission.md`: informe de transmisión con Amendment 1
    (definición de σ² como máximo sobre superposiciones interiores, tabla de canales en z₁ y
    argumento de hoja).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL / UNVERIFIED, con las
derivaciones necesarias:

1. **F1 (a), elección de método.** El contrato pide «el discriminante en τ de H_{A,ω} como curva»;
   el verificador sigue la rama de valores críticos (condición C3 4f′² = 1 − f² en u = cos²k,
   thr = (u − 1)q, y = (Re z_c)² = uR²) y polinomios de eventos en A. ¿Es correcta la
   parametrización (Re z_c = C·R(u, A), R(1, A) = 1, J = y_A q_u − y_u q_A como condición de
   estacionariedad)? ¿Cubre exactamente el conjunto «valor crítico o colisión» que define el
   contrato? ¿Es una desviación admisible o exige enmienda?
2. **F1 (a), resultado.** res_u(q, J) tiene una raíz en el rango de A; el verificador declara
   OPEN_AFTER_DISCRIMINANT_ANALYSIS. ¿Es correcto ese veredicto? El informe declara un defecto: la
   comprobación «declared points classified against y*» da PASS aunque la estructura no es simple,
   y sus etiquetas de región no estarían justificadas. ¿Es correcta esa lectura? ¿Hay otros
   falsos positivos?
3. **F1 (b).** Prueba de discriminante tipo T0 en cada punto declarado: CONNECTED en
   s = 1/4, 1/2, 3/4; una raíz en el arco. ¿Basta para CONNECTED punto a punto?
4. **Tubería F2/F3.** Krawczyk a radio 2⁻ᵖ; κ y la regla p = 256 + 2(2N + 1)⌈log₂κ⌉ (calculada a
   partir de cajas a 2⁻²⁵⁶); vectores de Bloch a p bits; propagación por intervalos con redondeo
   hacia fuera a 2⁻ᵖ; encierro de tanh mediante `mpmath.iv.exp` y monotonía; normalización por
   flujo aplicada al final, |S_rc|² = |x_rc|²·|F_r|/|F_c|; resolución con escalado de columnas por
   potencias de 2, precondicionador mpmath a p + 128 bits, β = ‖I − RA′‖ < 1/2 y cota de residuo.
   ¿Es todo riguroso? ¿Hay coma flotante en alguna cantidad certificada? ¿Es correcta la elección
   de sitios (modos interiores en x = −N − 1, exteriores en N + 1, producto M_N⋯M_{−N−1})?
5. **Resultados.** ¿Deciden las comprobaciones lo que dicen los encierros de T y σ² (anchura
   ~10⁻⁵⁷), los cotejos con z₀ y z₁ revisados, y los veredictos TRANSMISSION_NONZERO_CERTIFIED?
6. **Objeción principal (la pregunta física central).** σ² crece con L hacia 1
   (s = 1/50: 0.9605 → 0.9754 → 0.99945; s = 1/200: 0.9592 → 0.9647 → 0.9872). El autor sostiene,
   sin verificarlo, que σ² mide la continuidad adiabática de uno de los dos movedores a la derecha
   interiores hacia el único movedor a la derecha exterior, mientras el otro encuentra un punto de
   retorno (la raíz del discriminante de F1 (b)); que a ω fijo el modo exterior de bajo k tiene
   k ≈ ω/(8t − 3) y se desplaza a k finito en lugar de detenerse; y que por tanto el umbral de
   abandono (σ² ≥ 1/2) se dispara por un motivo trivial. ¿Es correcto este razonamiento? ¿Hay
   un argumento que lo confirme o lo refute con lo adjunto (p. ej. recuento de raíces, simetrías,
   estructura de la fila de S)? ¿Es σ² la cantidad adecuada para la pregunta del contrato, y si no,
   cuál lo sería (p. ej. mezcla en el punto de retorno de la rama reflejada)?
7. **Veredicto de línea y alcance.** ¿Es correcto no adoptar LEAKAGE_NOT_SUPPRESSED pese a
   cumplirse la condición formal del contrato? ¿O el contrato obliga a adoptarlo y la objeción solo
   puede ir a un contrato nuevo? ¿Es adecuada «Not claimed»? ¿Afecta a la validez que la ejecución
   se lanzara desde otra sesión con un encargo escrito?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que derivas a mano de lo
que solo inspeccionas. No calcules nuevas transmisiones ni seguimientos de ramas; si un punto
exige cálculo, dilo como obligación abierta.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y objeciones ordenadas
por gravedad con sección y reparación concreta. Si no hay fallos, dilo sin inventar objeciones.
---
