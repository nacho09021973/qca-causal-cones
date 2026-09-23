- Scripts: `scripts/` (`verify_*.py`, `cert_*`, `review_*`, `ir_precision_N24.py`,
  `ir_cancellation.py`); dependencias en `scripts/requirements.txt`.
- Regla del proyecto: álgebra y geometría exactas primero; los valores N=24/40 son diagnóstico
  finito (`CURRENT_STATE.md` §10: SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC) y no validan ni
  refutan signos asintóticos. No se autorizan barridos mayores sin gate.
- Comprobaciones propias:
  1. ¿Qué parte de la conclusión depende de un cálculo numérico y cuál es puramente analítica?
  2. ¿El régimen asintótico se alcanza en los N accesibles (ej. γ√N ≈ 1.1 en N=24)?
  3. Si se propone un cálculo, ¿es exacto/simbólico o de coma flotante, y qué error controla?
  4. ¿Puede un cálculo falsar barato la afirmación principal sin ser un barrido no autorizado?
