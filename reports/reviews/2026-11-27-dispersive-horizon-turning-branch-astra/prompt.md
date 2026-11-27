# Revisión externa: ejecución del contrato de la rama del retorno (POST_RESULTS_EXPLORATORY)

Autorización: usuario «autorizo la revisión de Astra 6.2» (2026-11-27); el contrato fija el modelo
(Q4). Modelo `gpt-6.2-astra` (OpenAI), vía `revision-ciega` del PATH con
`ASTRA_MODEL=gpt-6.2-astra`; generación comprobada antes del envío. Autor del contrato, del
informe, del verificador y del script de comparación: Claude (Opus 5.5). Herramientas:
`~/herramientas` commit `4a4fcca`. Revisado: commit `75c7e30` (rama
`research/dispersive-horizon-channels`). Máximo: una ronda. No se autoriza calcular nada nuevo ni
promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la **ejecución del contrato de la rama del retorno**
(POST_RESULTS_EXPLORATORY) para el paseo U = L₋W², W = S C(θ) S C(θ) S C(−2θ), t = cos²θ, medios
t = 5/16 y 7/16, z(s) = (1 − s² + 2is)/(1 + s²), perfil brusco y tanh truncado (L = 4, N = 32;
L = 16, N = 128). Tú mismo revisaste antes la ejecución de frecuencia y L finita (REPAIR_REQUIRED;
sugeriste este observable y el argumento de sectores). Se adjuntan:

(1) `DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md`: contrato congelado (`08e0703`);
(2) `2026-11-27--dispersive-horizon-turning-branch.md`: informe de ejecución con veredictos de autor
    (seis TRANSMISSION_NONZERO_CERTIFIED; candidato de línea T_RET_DECREASING_AT_COMPUTED_L) y una
    comparación orientativa con la heurística del contrato;
(3) `verify_dispersive_horizon_turning_branch.py`: verificador (38 comprobaciones, SHA256
    `397f72b3…0676`, commit `b0bb720`, anterior a su única ejecución), con 4 procesos `fork` tras la
    importación;
(4) `verify_dispersive_horizon_frequency_finite_l.py`: verificador importado sin modificar (su
    tubería ya la revisaste: punto 4 PASS);
(5) `2026-11-27--dispersive-horizon-turning-branch-run-1.txt`: registro (38/38 tras
    61 + 53 + 33 + 43, exit 0);
(6) `compare_turning_branch_heuristic.py` y (7) su salida
    `2026-11-27--dispersive-horizon-turning-branch-heuristic.txt` (orientación, no certificado).

Comprueba, informando para cada punto PASS / REPAIR_REQUIRED / FAIL / UNVERIFIED, con las
derivaciones necesarias:

1. **Identificación de rama (R1).** ¿Identifica correctamente el signo de la caja de λ
   (Re λ > 0, Im λ > 0 ⇔ k = −arg λ ∈ (−π/2, 0)) la rama que encuentra el punto de retorno, según
   tu argumento de sectores? ¿Es correcta la asignación de columnas (`c_ret`, `c_cont`) en el
   código, independiente del orden de enumeración?
2. **Columna y unitariedad (R2).** ¿Es correcta la construcción de la columna |S|² para incidencia
   unitaria en la rama del retorno (filas: movedores a la izquierda interiores y movedor a la
   derecha exterior), la comprobación de que suma 1 y S^H S ∋ I? ¿Decide el verificador T_ret y
   T_cont como dice?
3. **Cotejos (R3).** T_ret + T_cont frente al σ² importado de cada caso, y T_ret en z₁ brusco
   frente al |t₂|² revisado. ¿Son controles independientes o comparten código de forma que
   pierden valor? ¿Confirman la atribución anterior de |t₂|² a la rama k < 0?
4. **Paralelismo.** Procesos `fork` tras la importación; los trabajadores devuelven Fractions y
   todas las comprobaciones se hacen en el padre. ¿Puede el reparto afectar a algún resultado o
   a la detección de fallos (excepciones en trabajadores, estado compartido, cachés)? ¿Es
   aceptable que las líneas PASS lleven todas la misma marca de tiempo?
5. **Veredictos.** ¿Se siguen los seis TRANSMISSION_NONZERO_CERTIFIED y el candidato
   T_RET_DECREASING_AT_COMPUTED_L de las reglas del contrato (comparaciones por encierros
   disjuntos)? ¿Hay algún motivo contractual para no adoptarlo al cierre?
6. **Destino del flujo reflejado.** El informe dice que casi todo lo no transmitido va al movedor
   a la izquierda con k < 0 de mayor |k| (k ≈ −0.083 en s = 1/50, k ≈ −0.020 en s = 1/200), y
   que el de s = 1/50 está en la hoja de bajo k según el argumento de hoja ya revisado. ¿Es
   correcta esa lectura con las cajas del registro? ¿Y para s = 1/200?
7. **Comparación heurística.** T_ret frente a X = 1/(1 + e^{4πωL}) (forma de Sabsovich et al. con
   α = |dv/dx| = 1/(2L), identificación del autor): cocientes 1.111, 0.971, 0.992, 1.008. ¿Está
   bien presentada como orientación, sin afirmar ley? ¿Es correcta la identificación
   α = 8 t_L′(0) = 1/(2L) a partir de v(k → 0) = −1 + 2(4t − 1)? ¿Hay algún motivo por el que la
   coincidencia sea trivial o esté forzada (p. ej. por construcción del observable)? El informe
   declara que el script imprime pero no compara el SHA256 del log.
8. **Alcance.** ¿Es adecuada «Not claimed»? ¿Hay afirmaciones del informe que excedan lo
   certificado (por ejemplo en «Reading»)?

No tienes acceso al repositorio ni puedes ejecutar código. Distingue lo que derivas a mano de lo
que solo inspeccionas. No calcules transmisiones nuevas; si un punto exige cálculo, dilo como
obligación abierta.

Entrega en español: un veredicto por punto, un único veredicto global
(PASS / REPAIR_REQUIRED / FAIL / INCONCLUSIVE), las derivaciones críticas, y objeciones ordenadas
por gravedad con sección y reparación concreta. Si no hay fallos, dilo sin inventar objeciones.
---
