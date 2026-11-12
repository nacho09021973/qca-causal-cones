# Ejecución de los certificados del Apéndice A (2026-11-12)

Repetición pedida por el usuario tras reconciliar las dos versiones del
manuscrito (`reports/2026-11-12--ir-corona-version-reconciliation.md`).

- Repo en el commit `2525211` (rama `research/tetrahedral-support-rigidity-2026-11-09`).
  Los cuatro scripts son idénticos a los del commit `551addabe28b`:
  `git diff 551addabe28b 2525211` sobre ellos está vacío.
- Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0, NumPy 1.26.4.
- Orden: `python3 -B scripts/<script>.py` desde la raíz del repo, sin `--diagnostics`.

| script | resultado | salida |
|---|---|---|
| `verify_scaled_ir_gate.py` | 53/53, exit 0 | `verify_scaled_ir_gate.out` |
| `verify_regional_directional_asymptotics_gate.py` | 18/18, exit 0 | `verify_regional_directional_asymptotics_gate.out` |
| `verify_regional_laplace_coefficient_gate.py` | 58/58, exit 0 | `verify_regional_laplace_coefficient_gate.out` |
| `verify_directional_saturation.py` | 27/27, exit 0 | `verify_directional_saturation.out` |

Las cuatro salidas son idénticas byte a byte a las de `../2026-10-28/`.

Alcance, igual que entonces: los cálculos listados en el Apéndice A pasan en
esta máquina. No comprueba los lemas analíticos, que los propios scripts
declaran fuera de su alcance.
