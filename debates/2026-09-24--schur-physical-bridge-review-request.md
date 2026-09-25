# Revisión independiente del puente hacia los extremos físicos actuales

Autor candidato: Codex (OpenAI). Revisor solicitado: Claude Opus (Anthropic).
Sólo revisar matemáticas; no editar archivos ni consultar fuentes no adjuntas.
La nota candidata no es una premisa: reconstruir cada desigualdad.

La petición del usuario es verificar línea por línea que O(N^-7 exp(-K*N))
usa la fuente completa del contrato de dos canales y su referencia actual
r=U_N^N J phi_N, no los extremos planos históricos. Revisar también la
continuación (21)–(22) hacia las cuatro piezas lineales, dentro de ese alcance.

Dictámenes separados:
1. SCHUR_STABILITY: (3)–(7), no normalidad exterior, rangos oblicuos y suma doble.
2. PHYSICAL_ENDPOINTS: (8)–(13), norma L2 de s y v_c con fuente y Bob actuales.
3. PROPAGATOR_ERROR: (16)–(19), primera-momento Fourier, proyección discontinua
   fuera de W, Young con medida periodizada y control de Q inicial/final.
4. SIGNED_REDUCTION: (20)–(22), exponentes, potencias, canales y referencia exacta.
5. CLAIM_CEILING: hipótesis B frente a F, independencia en N pero no en W/perfil,
   subordinación absoluta frente a líder no demostrado/no anulación.

Atacar especialmente:
- ¿El kernel P(p') beta P(p) es Lipschitz cuando AMBOS puntos están en W,
  aunque la extensión por cero no lo sea? ¿Las interfaces invalidan Young?
- ¿Puede acotarse la norma Fourier L1 de la referencia física inhomogénea
  por e^{a0} N^-3/2 al iterar exactamente la moneda y el símbolo real unitario?
- ¿El conteo de capas da las normas inclinadas N^-3, con el encoder completo?
- ¿Un dato Q inicial de orden uno impide T^N-R^N=O(1/N)?
- ¿A_-P, A_+Q y A_-Q quedan realmente en el resto N^-7?
- ¿Alguna fórmula confunde E con E^(1/2), o proyecciones con sus adjuntos?
- Verificar el control plano, el signo del tilt y la constante de la
  reconstrucción Theta(N^-1), incluyendo la cota inferior en la red.

Entregar PASS, REPAIR_REQUIRED u OPEN en cada punto; si hay reparación
obligatoria, indicar la ecuación exacta, contraargumento y condición de cierre.
Si pasa, delimitar que es una reparación del puente, no una afirmación de
novedad ni un líder firmado no nulo ni cierre de H1/AdS.
No exigir un perfil numérico para un teorema con cuantificadores explícitos.
Un único revisor independiente de otra familia no se presenta como consenso
ni revisión humana. No extender a nuevos gates.
