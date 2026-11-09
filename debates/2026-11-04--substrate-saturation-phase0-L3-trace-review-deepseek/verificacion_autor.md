# Lectura del autor de la revisión de DeepSeek de la traza del nodo de L3

Autor: Claude (Anthropic). Objeto: el párrafo «Definition check (contract
Sec. 3.4)» de `reports/2026-11-03--substrate-saturation-phase0.md`
(l. 86–118, sha256 `3b88e925…`, último commit 2f6160e), base `78eb306`.
DeepSeek (`deepseek-v4-pro`), COMPLETED, 2026-11-04: **PASS** en los cinco
puntos, **sin reparaciones obligatorias**.

## Comprobaciones del autor sobre lo que afirma el revisor

- `spatial_derivative` es `i z ∂_z / sqrt(d)` (verificador l. 133–134) y
  `hull_geometry` divide el soporte por `sqrt(d)` (l. 109). Comprobado.
- El revisor lee `z_j = e^{i k_j / sqrt(d)}`. El extracto de CURRENT_STATE
  (l. 486–490) no escribe esa fase; fija `N_d = {±1}^d / sqrt(d)`. La fase
  se sigue de ahí: el monomio `z^n`, `n ∈ {±1}^d`, es el desplazamiento
  `n / sqrt(d)`. Con ella, `∂_{k_j} = (i/sqrt(d)) z_j ∂_{z_j}`, que es
  `spatial_derivative`. Con la convención opuesta `e^{-ik/sqrt(d)}` cambia
  el signo de `T_a`, lo que no afecta a hermiticidad, traza nula ni
  anticonmutador (el revisor lo dice en el punto 3).
- Siete casos en `run()` (l. 296), entre ellos d=3 A±, B±. Comprobado.

## Aclaraciones no bloqueantes del revisor (no aplicadas)

1. l. 159–160: `spatial = i ∂W` depende de la convención de fase anterior.
2. l. 172–173: «massless matching» comprueba `c_0 = r_in`; el valor
   `1/sqrt(d)` lo fija el chequeo de Clifford.

Ninguna cambia la traza. No se aplican al informe sin decisión del
usuario; quedan registradas aquí.

## Lo que esto no hace

No promociona la fase 0, no usa todavía L3 como testigo en la auditoría y
no cambia sus salidas (`OPEN_AFTER_ROW_SURVEY`; L4 sigue sin clasificar).
Usar L3 como testigo es decisión del usuario. Revisión de una sola casa;
el usuario revisó las derivaciones (ii) y (v) el 2026-11-03.

Búsqueda de secretos en la carpeta (clave de DeepSeek y patrón `sk-…`):
sin coincidencias.
