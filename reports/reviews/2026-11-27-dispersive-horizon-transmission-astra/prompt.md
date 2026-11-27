# Revisión externa: ejecución del contrato de transmisión T0–T4 (horizonte dispersivo, perfil brusco)

Autorización: usuario «Yes, send» (2026-11-27), una ronda; el contrato fija el modelo (Q4). El
modelo es `gpt-6.2-astra` (OpenAI), vía `revision-ciega` del PATH con
`ASTRA_MODEL=gpt-6.2-astra`; generación comprobada antes del envío. Autor del contrato, del
informe y del verificador: Claude (Opus 5.5). Herramientas: `~/herramientas` commit `4a4fcca`.
Revisado: commit `d5a944d` (rama `research/dispersive-horizon-channels`). Máximo: una ronda. No
se autoriza calcular L finita, otras cuasienergías ni promoción. Cierra el encargo: un informe
completo de esta ronda.

---
Revisa adversarialmente la **ejecución del contrato de transmisión T0–T4** para el paseo
cuántico U = L₋W², W = S C(θ) S C(θ) S C(−2θ), con t = cos²θ, A = t(2t−1), en el perfil brusco
t(x) = 5/16 (x < 0), 3/8 (x = 0), 7/16 (x > 0), límite L → 0⁺ de t_L = 3/8 + tanh(x/L)/16. La
matriz de transferencia 12×12 M_x(z), la forma de flujo G_x y la clasificación de canales C1–C5
ya pasaron revisiones externas; no las revises de nuevo salvo donde T0–T4 dependan de ellas.
Se adjuntan:

(1) `DISPERSIVE_HORIZON_TRANSMISSION_GATE.md`: el contrato congelado (commit `8eb8be5`), con
    tareas, criterios de admisión, veredictos y «Not claimed»;
(2) `2026-11-26--dispersive-horizon-transmission.md`: el informe de ejecución, con veredictos de
    autor TRANSMISSION_NONZERO_CERTIFIED en z₀ = (3+4i)/5 (T0 = CONNECTED) y en
    z₁ = (2499+100i)/2501 (PRELIMINARY);
(3) `verify_dispersive_horizon_transmission.py`: el verificador (33 comprobaciones, SHA256
    `29ee9f12…316ea`, commit `0959251`, anterior a su ejecución registrada);
(4) `verify_dispersive_horizon_channels.py` y (5) `verify_dispersive_horizon_transfer_matrix.py`:
    verificadores ya revisados que (3) importa tras comprobar su SHA256, sin modificarlos;
(6) `2026-11-26--dispersive-horizon-transmission-run-2.txt`: registro de la ejecución (33/33
    tras 61/61 y 53/53, exit 0);
(7) `2026-11-26--dispersive-horizon-transmission-run-1.txt`: registro de la ejecución
    interrumpida (prueba simbólica de las filas de cierre, ~11 GB).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL / UNVERIFIED, con las
derivaciones necesarias:

1. **Vector de Bloch y filas de cierre.** Las filas 1–10 de (M − λ)Y = 0 se verifican
   idénticamente; las filas 0 y 11 solo en 9 puntos muestrales exactos (w, λ) módulo
   det(U − z), y el caso general se apoya en un paso escrito: una solución de Bloch de Uψ = zψ
   es una órbita de M, por la biyección certificada en T2 de (5). ¿Es correcto y suficiente ese
   paso? ¿Qué añade (o no) la comprobación muestral y el residuo por intervalos MY − λY ∋ 0 en
   cada raíz? ¿Es honesta la sustitución respecto de lo que intentaba la ejecución 1?
2. **Raíces por Krawczyk.** Cajas complejas disjuntas de radio 10⁻⁵⁰ para las 12 raíces de
   P(·, z) en cada medio y cada z, con conjeturas de numpy/mpmath. ¿Es correcta la prueba de
   Krawczyk implementada (inclusión estricta, unicidad, aritmética racional/dirigida)? ¿Es
   válida la clasificación |λ| < 1, > 1, = 1 frente al recuento exacto de Sturm, en particular
   para las raíces en el círculo?
3. **T0, continuidad de rama.** Coeficiente principal 8/5 en τ, discriminante de H_A de grado 28
   en A sin raíces en [−15/128, −7/128]. ¿Basta para que z₀ sea valor regular en todo medio
   intermedio (incluidas colisiones y k = π)? ¿Se sigue el paso escrito de que el único
   movedor a la derecha interior (k ≈ 1.231) continúa sin punto de retorno en el exterior
   (k ≈ 1.107)? ¿Es relevante que A(t) sea monótona en [5/16, 7/16]?
4. **T1, existencia y unitariedad.** Elección de incógnitas (salientes y evanescentes
   decrecientes en cada lado), invertibilidad por ‖I − RA‖_∞ ≤ 10⁻⁶ con R en coma flotante solo
   como precondicionador, cota de residuo de la solución, normalización |Y^H G Y| = 1 con signo
   como dirección, S^H S ∋ I. ¿Excluye esto estados ligados en z? ¿Es correcta la comprobación
   tr(t′^H t′) − 2 − T ∋ 0 como lectura del recuento de Tarasinski?
5. **T2 y T4, transmisión.** Encierros de t en z₀ y de t₁, t₂ en z₁; σ² como valor singular del
   bloque 2×1. ¿Decide el verificador lo que el informe afirma? ¿Hay coma flotante en alguna
   cantidad certificada?
6. **Interpretación física en z₁.** La tabla de movedores, la identificación de los dos
   movedores a la derecha interiores (k ≈ 0.596, −0.476) como «doublers» y del movedor a la
   derecha exterior (k ≈ 0.080) como la rama de bajo k cuyo signo de velocidad cambia en
   t = 3/8. ¿Está justificada por las cajas de λ y por v(k → 0) = −1 + 2(4t − 1), o es solo
   orientativa? ¿Es correcta la lectura «96.05 % del flujo saliente de ese modo viene de los
   doublers interiores» a partir de la unitariedad de la fila?
7. **Veredictos y alcance.** ¿Se siguen los dos TRANSMISSION_NONZERO_CERTIFIED de las reglas del
   contrato, incluida la cláusula de declarar continuidad adiabática si T0 = CONNECTED? ¿Separa
   el informe lo certificado, lo escrito y lo orientativo? ¿Es adecuada «Not claimed»
   (perfil tanh a L finita, otras z, Hawking, novedad)? ¿Afecta la desviación de proceso
   declarada a la validez?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que derivas a mano de lo
que solo inspeccionas. No calcules L finita, otras cuasienergías, asintóticas adiabáticas ni
originalidad.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y objeciones ordenadas
por gravedad con sección y reparación concreta. Si no hay fallos, dilo sin inventar objeciones.
---
