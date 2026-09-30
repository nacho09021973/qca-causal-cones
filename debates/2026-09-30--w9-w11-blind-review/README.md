# Revisión ciega W9–W11 — 2026-09-30

Objeto: W9, W10, W11 y la auditoría de prior art de W8 en
`research/gravitational-normalization-gate` @ `41d0e0d` (autor de los resultados: Astra/GPT).
Herramienta: `revision-ciega` (`~/herramientas` @ `574b5f3`), modo sellado, una ronda.
Documentos enviados: `documentos.txt` (+ `cjww_walk_definition.md`, transcripción de `walk2()`).
Encargo: `prompt.md`. Entradas exactas: `entrada_<modelo>.txt` (idénticas, mismo sha256).

| Revisor | Familia | Informe | W9 | W10 | W11 |
|---|---|---|---|---|---|
| DeepSeek `deepseek-v4-pro` (según la API, `deepseek.log`) | DeepSeek | `informe_deepseek.md` | ACCEPT | ACCEPT_WITH_REPAIRS | ACCEPT_WITH_REPAIRS |
| Opus `claude-opus-5-5` | Anthropic | `informe_opus.md` | ACCEPT_WITH_REPAIRS | ACCEPT_WITH_REPAIRS | ACCEPT_WITH_REPAIRS |

Opus es independiente del autor (GPT), pero no de Claude Code, que preparó el encargo.

## Comprobación de afirmaciones de los revisores

`verify_reviewer_claims.py` (SymPy, mismo `walk2()` que el certificado W11):

- CONFIRMADO (ambos): `H_eff − H_IR = Θ(|p|³)`; el informe W11 dice `O(|p|²)`, cierto pero no ajustado.
- REFUTADO (DeepSeek): su término cúbico `H_eff = −A − (p²/6)A + …`; en el eje `p3`,
  `W = exp(i p3 σ3)` exactamente y `H_eff = −p3 σ3` sin término cúbico.
- CONFIRMADO (Opus): `W = ±I` en las 8 esquinas `{0,π}³` (4 y 4); en los cuatro nodos `+I` el
  marco lineal tiene signos de determinante `−,+,−,+` (quiralidad neta 0): hay cuatro especies
  Weyl de cuasienergía 0, no una.
- CONFIRMADO (Opus): `[H_IR(p), W(p)] = O(|p|⁴)` y no nulo: `Σ_x H_IR` no se conserva.
- CONFIRMADO (Opus): `K = i(U − U†)/2` conmuta con `U` y `K − H_eff = O(|p|³)`.
- CONFIRMADO (Opus, F4): `Σ_x π_i(x)` tiene símbolo escalar `sin p_i` y conmuta con `W`.
- SIN COMPROBAR: el no-go de paridad de Opus para F3, las afirmaciones sobre núcleos con
  transferencia `q ≠ 0` / Belinfante, y todo el prior art (ambos lo marcan `[UNVERIFIED]`;
  hay que leer Gu–Wen arXiv:0907.1203 y Pretko en el original).

Estado: revisión recibida; reparaciones no aplicadas. Decide el usuario.
