# Verificación del informe de DeepSeek (por Claude, 2026-11-04)

Informe: `informe_deepseek.md` (deepseek-v4-pro, `revision-ciega` @ ce09890,
estado COMPLETED, respuesta sha256 `8ff9f963…`). Generación comprobada antes del
envío con una petición trivial (respuesta `OK`, modelo devuelto
`deepseek-v4-pro`). Candidato: propuesta sha256 `ea7b8646…` en base `0d85366`.

Comprobado a mano:

- Vértices del zonótopo impreso en coordenadas `ISO` (generadores
  `±(1,−1)`, `±(1,0)`, `±(0,1)`): `±(2,0)`, `±(2,−2)`, `±(0,2)`. Correcto; en
  cartesianas `±(1,1)`, `±(2,0)`, `±(−1,1)`, como en la revisión de Claude.
- `conv F` con vértices `±(2,0)`, `±(0,2)` en `ISO` = `±(1,1)`, `±(−1,1)` en
  cartesianas: el cuadrado del zonótopo fusionado (generadores `(1,0)`,
  `(0,1)`). Correcto.
- «`Ŝ_2` y `Ŝ_3` conmutan»: cierto (ambos diagonales en L/R), aunque no hace
  falta: con `Û_2 = I` el producto `Ŝ_3 Ŝ_2` ya es un solo factor.
- Aclaración sobre «Sec. 2.1»: el contrato numera los puntos de su Sec. 2 sin
  subsecciones; el repositorio usa «Sec. 2.1/2.3/2.4» para esos puntos (p. ej.
  la auditoría). Convención, no error; no se corrige.

Dictamen aceptado: **PASS**, sin reparaciones obligatorias. Cierre del encargo
según `prompt.md`: se registra la adopción de la recomendación (decisión del
usuario, «si a las 3»).
