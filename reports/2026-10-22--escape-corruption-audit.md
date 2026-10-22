# Auditoría de integridad: LaTeX corrompido y certificados que no se ejecutaban

Fecha: 2026-10-22. Rama `research/inverse-gravity-design`. Autor: Claude Opus 5.5.
Origen: al preparar la revisión independiente de W3–W6, autorizada por el usuario
(«adelante»), aparecieron dos defectos. Instrucción humana posterior: «es un proyecto
a largo plazo, no se trata de poner parches». Este informe registra causa, alcance,
reparación hecha y trabajo pendiente. No cambia ningún nivel de evidencia científica.

## 1. Certificados que fallaban con la versión fijada

`scripts/run_all_verifiers.py` (nuevo, permanente) ejecutó los 42 `verify_*.py`
con Python 3.12, SymPy 1.14.0 y NumPy 1.26.4:
[registro previo](2026-10-22--verifier-sweep.tsv), 2 fallos.

| Script | Commit de alta | Causa | Identidad |
|---|---|---|---|
| `verify_w2_transport_tetrad.py` | `6f81a52` | `==` estructural tras `simplify` | `(E1ᵀE1)₀₀=(1−2gb₁)²`, verdadera |
| `verify_w5_tetrad_source.py` | `bd91e1a` | ídem | `i(e^{−iq}−e^{iq})=2 sin q`, verdadera |

Con la versión fijada, ninguno de los dos podía pasar tal como se dio de alta. Sus
informes daban PASS a los criterios correspondientes sin registrar una ejecución con
éxito. Reparación (`cb1e038`): helper común `scripts/certificate_utils.py`
(`assert_sym_equal`, igualdad de valor normalizando trig/exp, con control negativo) y
sustitución de las aserciones frágiles. [Registro posterior](2026-10-22--verifier-sweep-after-fix.tsv):
42/42 pasan.

## 2. LaTeX corrompido por una capa de escapes

**Causa.** Los documentos de la serie de gravedad del 29–30 de septiembre se
introdujeron en 25 commits con autor `noreply` de GitHub, es decir, escritos a través
de una API o agente web. Su texto pasó por una capa de escapes de tipo JSON:
- las secuencias válidas se convirtieron en caracteres de control: `\b`oxed →
  retroceso, `\f`rac → salto de página, `\t`ext → tabulador, `\r`angle → CR suelto,
  `\n`abla → salto de línea;
- las demás barras invertidas se **perdieron sin dejar rastro**: `\omega` → `omega`,
  `\[` → `[`, `\otimes\sigma_a` → `otimessigma_a`.

**Alcance** (`scripts/text_integrity.py --check`, todos los `.md`/`.tex` versionados):
36 ficheros. Son la serie W1–W7 (informes y **contratos congelados**), los puentes
CJWW, G0 y la selección de clase, 32 líneas de `state/CURRENT_STATE.md` y una
revisión del 23-09. Los demás documentos que escriben fórmulas en ASCII lo hacen a
propósito y no están afectados.

**Reparación mecánica** (`2d144d9`): 578 cambios en 32 ficheros, cada uno en el
[registro](2026-10-22--escape-corruption-mechanical-repair.tsv). Restaura solo lo
inequívoco: los caracteres de control vuelven a su barra más letra, y se aplican dos
uniones de `\n` decididas a mano (`scripts/text_integrity_newline_decisions.tsv`).
Los finales de línea CRLF se respetan.

**Lo que no se puede reparar mecánicamente:** las barras perdidas sin rastro. Tras la
reparación, `--check` sigue señalando 901 problemas, casi todos delimitadores `[`/`]`
desnudos. Las fórmulas de esos documentos son ilegibles o ambiguas (`pm` puede ser
`\pm` o texto), y su contenido matemático tiene que **reconstruirse a mano**.

**Consecuencias para la evidencia registrada:**
- Los revisores de W12 (DeepSeek, Opus, 2026-09-30) recibieron el contrato W6 en su
  forma corrompida. Su veredicto se emitió sobre ese texto. [Por comprobar en cada
  revisión cuánto dependía de las fórmulas rotas.]
- Las cifras y conclusiones de los informes W1–W7 no cambian por esta auditoría.
  Pero su texto matemático, tal como está, no es revisable, y los resultados
  PRELIMINARY de esa serie no pueden enviarse a revisión independiente hasta
  reconstruirlo.

## 3. Prevención

- `python3 -B scripts/text_integrity.py --check` falla con caracteres de control, CR
  sueltos, sospechas de `\n` perdido sin decisión y delimitadores desnudos.
- `python3 -B scripts/run_all_verifiers.py --output <tsv>` vuelve a ejecutar todos los
  certificados.
- `AGENTS.md` y `CLAUDE.md` exigen ambos antes de cualquier commit que añada texto o
  certificados, y prohíben escribir LaTeX a través de capas que interpreten escapes
  sin comprobarlo después.
- Otros repos locales: una búsqueda de solo lectura encuentra caracteres de control
  sobre todo en extractos de `pdftotext` (saltos de página) y en transcripciones, que
  son legítimos. Solo se revisaron muestras; no es una auditoría de esos repos.

## 4. Trabajo pendiente, en orden

1. **Reconstrucción manual** de los 36 documentos, empezando por W3–W6 y sus
   contratos. Para cada fórmula: restaurar el LaTeX a partir del contexto y
   contrastarlo con el certificado (`scripts/verify_w*.py`). Lo que no se pueda fijar
   sin ambigüedad se marca como tal; no se adivina. Los contratos congelados
   conservan su versión original en el commit de congelación. La reconstrucción es
   tipográfica y se registra como tal.
2. **Documentar en `scripts/README.md`** los 29 verificadores sin entrada, con lo que
   certifican y lo que no.
3. **Revisión independiente de W3–W6** sobre el texto reconstruido.
