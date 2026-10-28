# Ejecución de los certificados del Apéndice A (2026-10-28)

Pedido tras el sanedrín `debates/2026-10-28--ir-corona-sanedrin.md`, donde ABNER exigía
ejecutar los certificados antes de enviar.

- Repo en el commit `929fd44` (rama `research/inverse-gravity-design`). Los cuatro scripts
  son idénticos a los del commit que cita `\bibitem{Repo}` (`551addabe28b`): `git diff
  551addabe28b 929fd44` sobre ellos está vacío.
- Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0, NumPy 1.26.4 (las versiones que declara el paper).
- Orden: `python3 -B scripts/<script>.py` desde la raíz del repo, sin `--diagnostics`.

| script | resultado | salida |
|---|---|---|
| `verify_scaled_ir_gate.py` | 53/53, exit 0 | `verify_scaled_ir_gate.out` |
| `verify_regional_directional_asymptotics_gate.py` | 18/18, exit 0 | `verify_regional_directional_asymptotics_gate.out` |
| `verify_regional_laplace_coefficient_gate.py` | 58/58, exit 0 | `verify_regional_laplace_coefficient_gate.out` |
| `verify_directional_saturation.py` | 27/27, exit 0 | `verify_directional_saturation.out` |

Lo que esto comprueba: que los cálculos listados en el Apéndice A pasan en esta máquina. No
comprueba los lemas analíticos (resto O(N^{-1/2}), punto de silla, Lemma «Layers»), que los
propios scripts declaran fuera de su alcance.
