# Prompt que Claude dio al usuario (2026-11-27) para el encargo a Astra 6.2

Nota de procedencia:
- El usuario lo envió por la web de ChatGPT, no con `revision-ciega`.
- `[UNVERIFIED]`: si se envió literalmente y qué adjuntos acompañaron al
  envío.
- La respuesta cita la nota en el commit `73fc0b8` y una «línea 194» que
  existe en `theory/DISPERSIVE_HORIZON_CHANNELS_GATE.md`. Esto sugiere que
  el modelo tuvo acceso a ficheros del repositorio.
- Los «[pendiente]» de la cabecera son los del texto original y se dejan
  tal cual.

---

# Encargo externo: intento de demostración de la conjetura del punto de retorno (OPEN)

Autorización: usuario, pendiente («dame un prompt para que Astra 6.2 trate de demostrarla»; el envío
requiere autorización aparte). Modelo `gpt-6.2-astra` (OpenAI), vía `revision-ciega` del PATH con
`ASTRA_MODEL=gpt-6.2-astra`; generación comprobada antes del envío. Autor de la conjetura y de la nota:
Claude (Opus 5.5). Herramientas: `~/herramientas` commit `4a4fcca`. Base: commit `73fc0b8` (rama
`research/dispersive-horizon-channels`). Máximo: una ronda. No se autoriza calcular nada nuevo ni
promoción. Cierra el encargo: un informe completo de esta ronda con uno de los veredictos listados.

---
Intenta **demostrar o refutar** la conjetura (C) de la nota adjunta, para el paseo cuántico
U = L₋W², W = S C(θ) S C(θ) S C(−2θ), t = cos²θ, con parámetro de moneda local t(x). No es una
revisión de cálculos: es trabajo matemático. Tú mismo propusiste el observable T_ret en una ronda
anterior; consta como límite de independencia.

Se adjuntan:
(1) `DISPERSIVE_HORIZON_TURNING_POINT_CONJECTURE.md`: la nota con el enunciado (C1)–(C4), el escalado
    heurístico y un esbozo de ruta;
(2) `DISPERSIVE_HORIZON_CHANNELS_GATE.md` y `verify_dispersive_horizon_channels.py`: el modelo, la
    matriz de transferencia 12×12, la forma de flujo y la relación de dispersión (comprobación C2:
    2f² − 1 = cos(ω + k), f = A cos 3k + (1 − A) cos k, A = t(2t − 1), λ = e^{−ik}, z = e^{iω});
(3) `check_dispersive_horizon_low_k_sheet.py` y su salida: hoja de bajo k
    ω = (8t − 3)k + γ(t)k³ + O(k⁵), γ(t) = 16t(t − 1)(2t − 1)(2t + 1)/(3(4t − 1)), γ(3/8) = 35/32;
(4) `comprobacion.md` (tercera tanda): lectura de De Beule et al., arXiv:2106.14595, con páginas y
    ecuaciones (resultado T_{u←w₁,₂} = 1/(1 + e^{±2πω/α}), modelo continuo de tiempo continuo, WKB más
    solución hipergeométrica, hipótesis α, |ω| ≪ 1).

**Enunciado a tratar (resumen; manda la nota).** Perfiles t_L(x) = 3/8 + φ(x/L), con φ suave,
estrictamente creciente, φ(0) = 0, φ → ±1/16 exponencialmente, κ = 8φ′(0). Con ω = μ/L, μ > 0 fijo, y
L → ∞, uniformemente en compactos de μ:
(C1) T_ret → X(μ) = 1/(1 + e^{2πμ/κ}); (C2) T_cont → 1 − X(μ); (C3) reflexión de la rama del retorno
al movedor interior de bajo k → 1 − X(μ), y las demás entradas de su columna → 0; (C4) los límites
solo dependen de φ′(0), no de γ(3/8).

**Qué se pide, en este orden:**
1. **Enunciado preciso.** Si (C) está mal planteada (límite equivocado, hipótesis insuficientes,
   observable mal definido para L finito o para el perfil sin truncar), corrígela antes de nada y
   di exactamente qué cambias y por qué. No demuestres una versión distinta sin declararlo.
2. **Existencia de la matriz S** para estos perfiles (dos medios asintóticos distintos, paseo de
   varios pasos). Demuéstrala o reduce a un resultado publicado citando enunciado exacto; si citas,
   marca la cita `[UNVERIFIED]` salvo que reproduzcas el argumento.
3. **Región exterior** (|x| ≫ L^{1/3}): desacoplo adiabático de los modos de la hoja de bajo k
   frente a los demás (otra hoja, canales |k| ≈ 2, evanescentes) con cota de error explícita.
4. **Región interior**: deducción del problema límite κyq + γ_h q³ = μ (o el correcto, si este no lo
   es) como operador en y, su solución exacta y sus coeficientes de conexión; muestra de dónde sale
   e^{2πμ/κ} y si γ_h desaparece del orden principal (C4).
5. **Empalme** en L^{1/3} ≪ |x| ≪ L con control de errores, y la consecuencia para (C1)–(C3).

**Reglas.**
- Separa en cada paso: DEMOSTRADO (argumento completo aquí), DEMOSTRADO_BAJO_HIPÓTESIS (lista
  explícita), HEURÍSTICO, o NO_HECHO. Nada heurístico puede presentarse como demostrado.
- Ningún cálculo numérico cuenta como prueba. Si usas números, márcalos como orientación.
- No atribuyas resultados a la literatura sin referencia exacta (autor, arXiv, teorema o ecuación);
  lo que no puedas comprobar, `[UNVERIFIED]`.
- Si encuentras un argumento de que (C) es falsa, o de que (C4) falla (dependencia de γ o del perfil
  más allá de φ′(0)), dalo con el mismo rigor: una refutación vale tanto como una prueba.
- Si el problema completo excede una ronda, prioriza: (a) enunciado correcto, (b) región interior
  exacta, (c) qué falta para lo demás. Dilo claramente; no rellenes.

**Veredicto global (uno):** PROVED · PROVED_UNDER_STATED_ASSUMPTIONS · PARTIAL (qué pasos sí y cuáles
no) · REFUTED (con el argumento) · STATEMENT_REPAIRED_THEN_<uno de los anteriores> · NO_PROOF_FOUND.

**Entrega:** enunciado final usado; demostración por pasos con su etiqueta; lista de hipótesis no
demostradas; lista de citas `[UNVERIFIED]`; veredicto; y qué cálculo o comprobación independiente
pondría a prueba con más eficacia lo que no hayas podido demostrar.
---
