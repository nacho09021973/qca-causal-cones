# Hoja de trabajo — 22 de octubre de 2026

Rama: `research/inverse-gravity-design`, subida hasta `8986cfc` (más el commit de esta hoja).
La fuente de verdad sigue siendo `state/CURRENT_STATE.md`. Esta hoja ordena los próximos pasos,
pero no autoriza nada por sí misma.

## Qué se hizo hoy

1. **Auditoría documental del 08-10:** se hizo commit de `reports/2026-10-08--elastic-atlas-documentary-audit.md`.
2. **Revisión del coste de discriminación (28-09):** Astra dio PASS_WITH_REPAIRS y Gemini PASS. Las tres
   reparaciones se aplicaron como adenda. Estado: `REVIEWED_PASS_WITH_REPAIRS`.
3. **Reconciliación de `16c4f0f`/`13d398a`:** el informe 4B del 28-09 se importó como registro histórico.
   El resultado coincide con el del 25-09, y el registro de autorización del 25-09 se mantiene.
4. **Auditoría de integridad** (`reports/2026-10-22--escape-corruption-audit.md`):
   - **Certificados:** `verify_w2_*` y `verify_w5_tetrad_source` no podían pasar con SymPy 1.14.0. Se
     arreglaron con `certificate_utils.assert_sym_equal`, y ahora pasan los 42 verificadores.
   - **Documentos:** 36 tenían el LaTeX corrompido por una capa de escapes (commits `noreply` del 29–30 de
     septiembre). La reparación mecánica restauró 578 casos, con registro.
   - **Herramientas nuevas:** `run_all_verifiers.py`, `text_integrity.py`, `check_reconstruction.py` y
     `certificate_utils.py`. `AGENTS.md` y `CLAUDE.md` las exigen antes de cada commit.
5. **Reconstrucción manual de W3–W6** (contratos e informes, 8 documentos). `check_reconstruction` da PASS
   en todos.
6. **Revisión independiente de W3–W6:** Astra y DeepSeek dan ACCEPT_WITH_REPAIRS en los cuatro gates. Las
   reparaciones se añadieron como adendas. Estado: `REVIEWED_ACCEPT_WITH_REPAIRS`, con alcance reducido.

## Próximos pasos, por orden

### 1. Terminar la reconstrucción de los documentos corrompidos (26 ficheros, 611 avisos)

Mismo método que en W3–W6:
1. Leer el documento y su certificado.
2. Restaurar las barras invertidas a mano. Lo que no se pueda fijar sin ambigüedad se marca como tal; no
   se adivina.
3. Añadir la nota de cabecera «Typographic reconstruction».
4. Pasar `python3 -B scripts/check_reconstruction.py <fichero>` y
   `python3 -B scripts/text_integrity.py --check`.
5. Hacer un commit por gate (contrato e informe juntos).

Editar con las herramientas de edición, sin fragmentos de código sueltos. Vigilar los `\n` perdidos que
el detector no ve (`n\ne0`, `T_{\mu\nu}`).

Orden propuesto (primero lo que más se cita):

| Prioridad | Contrato | Informe | Avisos |
|---|---|---|---|
| a | `theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md` | `w2-transport-tetrad-bridge`, `w2-tetrad-backreaction-audit` | 26 + 70 + 16 |
| b | `theory/W1_PERTURBATIVE_BACKREACTION_BRIDGE_GATE.md` | `w1-perturbative-backreaction-bridge` | 22 + 66 |
| c | `theory/W1_GEOMETRICITY_GATE.md`, `theory/W1_COARSE_METRIC_GATE.md` | `w1-geometricity`, `w1-coarse-metric` | 14 + 18 + 44 + 34 |
| d | `theory/W3_CURVATURE_DYNAMICS_GATE.md` | `w3-curvature-dynamics` (contiene R⁽¹⁾ = −4g∂₂²z₁, que cita W4) | 6 + 46 |
| e | `theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md` | `w4-long-wavelength-spectrum` | 6 + 32 |
| f | `theory/W5_SPATIAL_TETRAD_COMPLETENESS_GATE.md` | `w5-spatial-tetrad-completeness` | 14 + 32 |
| g | `theory/W7_SPIN2_KINEMATICS_GATE.md` | `w7-spin2-kinematics` | 14 + 32 |
| h | `theory/EXPLICIT_CJWW_DYNAMIC_GRAPH_BRIDGE_GATE.md` | `explicit-cjww-dynamic-graph-bridge` | 14 + 40 |
| i | `theory/GRAVITATIONAL_NORMALIZATION_GATE.md`, `theory/DYNAMICAL_GEOMETRY_MODEL_CLASS_GATE.md` | `gravitational-normalization-g0`, `dynamical-geometry-model-class` | 10 + 8 + 12 + 4 |
| j | — | `state/CURRENT_STATE.md` (26), `reports/2026-09-20--roadmap-e-next-steps.md` (4), `debates/2026-09-23--irreducible-d2-deepseek-gemini-review.md` (1) | 31 |

En `CURRENT_STATE.md` hay que tener cuidado: es la fuente de verdad. Se reconstruye por secciones y no
se toca el contenido.

### 2. Certificados que deriven, no que comprueben lo que definen

Obligaciones que dejó la revisión de W3–W6:
- **W3:** derivar `E(z)=E_0-2g diag(z_a)D` desde el símbolo `J_a(p)` del walk, en lugar de definirlo.
- **W5:** comprobar `J_a(p)=2 sin(p·d_a)σ_a` para a = 1, 2, 3 y la derivada variacional `∂H/∂z`.
- **W6:** certificar F1 (recuperación de la materia con η = 0), F5 y F6, y dar un calendario explícito de
  coloración de profundidad finita para los nueve tipos de registro.
- Cada certificado reforzado se añade a `run_all_verifiers.py` (ya lo recoge el glob) y a `scripts/README.md`.

### 3. Documentar los 29 verificadores sin entrada en `scripts/README.md`

Para cada uno: qué informe y contrato certifica, cuántas comprobaciones hace y **qué no certifica**. Lista:
`grep` de los `verify_*.py` que no aparecen en el README (la orden está en el informe de auditoría, §4).

### 4. Revisiones independientes que siguen pendientes (cuando se reconstruya su texto)

- W1, W2, W7 y los puentes CJWW: sus resultados PRELIMINARY no se envían a revisión hasta tener el texto
  reconstruido.
- F2/F4 (familia elástica): revisión independiente pendiente según la auditoría documental del 08-10.
- La versión reparada del informe de coste de discriminación no se ha vuelto a revisar. Solo hace falta
  si se va a usar como base de algo nuevo.

### 5. Decisión de rumbo (no técnica): la línea de gravedad inversa

La cadena IG-S0 → IG-S2 (08–10 de octubre) acabó con la recomendación de pausar la transferencia directa.
Antes de abrir otro contrato técnico, convocar `/comite` con una sola pregunta: ¿hay un objetivo
alcanzable en esta línea, o se cierra como registro de obstrucciones? La decisión es del usuario.

## Comprobaciones antes de cada sesión

```sh
python3 -B scripts/run_all_verifiers.py --output reports/<fecha>--verifier-sweep.tsv   # 42/42 hoy
python3 -B scripts/text_integrity.py --check                                         # 611 avisos hoy (cola de reconstrucción)
```
