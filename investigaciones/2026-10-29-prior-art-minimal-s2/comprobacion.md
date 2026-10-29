# Comprobación — búsqueda de prior art de Codex (charter de rigidez mínima s=2)

Fecha: 2026-10-29. Autor: Claude.
- El encargo lo redactó Claude y el usuario se lo dio personalmente a Codex.
- `informe_codex.md` es texto de IA (Codex, familia OpenAI). Localiza fuentes; no prueba nada.
- Este fichero contrasta con el original el hallazgo principal y registra qué PDF se
  incorporaron a la biblioteca.

## Hallazgo principal: DEP19, apéndice A.2 — CONFIRMADO en el original

D'Ariano, Erba y Perinotti, «Chirality from quantum walks without quantum coin», arXiv:1902.10227v2
(PRA 100, 012105 (2019), según Codex; la referencia de revista no se ha comprobado).

Texto extraído con `pdftotext -layout`:
- **Sección V.** Dice literalmente «in Appendix A we derive the most general QWs with a
  two-dimensional coin on the simple square and BCC lattices. These are shown in Eqs. (A2) and
  (A30).»
- **Apéndice A.2 («BCC lattice»).** Parte de la presentación de `Z^3` con cuatro generadores
  `h_1..h_4` y de las condiciones de unitariedad para los caminos de longitud 2, ecs. (A5)–(A7).
  Llega a (A30), con `α_i > 0`, `α_1 α_2 = α_3 α_4` y `Σ α_i^2 = 1`.
- **Equivalencia usada en (A30).** La familia se da «up to a left-multiplication by an
  arbitrary unitary».
- **Término on-site.** El apéndice incluye identidades con `A_e` (líneas ~1335 y ~1488 del texto
  extraído). Cómo trata ese término y si coincide con «sin on-site» del charter queda
  `[UNVERIFIED]` hasta leerlo entero.

**Consecuencias para el charter:**

1. **Paso 4b-1 cambia de naturaleza.** Si (A30) es de verdad la familia unitaria general s=2 en
   BCC, derivada solo de unitariedad, ya no hace falta resolver desde cero el sistema de
   unitariedad de cada una de las cinco clases. Bastaría imponer la covarianza de cada clase
   sobre (A30). Antes hay que auditar:
   - **Exhaustividad.** Si «most general» está probado o solo afirmado. Cómo eligen
     `V_{+i} = V_{−i}`: lo justifican por la no unicidad de la descomposición polar cuando el
     rango no es completo.
   - **Hipótesis implícitas:** coeficientes no nulos, rango uno, fidelidad y término on-site.
   - **Convenciones de la red:** que la presentación de los generadores coincida con nuestro
     `N_3`.
2. **La multiplicación por la izquierda es justo la operación que el charter excluye** como
   equivalencia, porque cambia el cuerpo estricto (contraejemplo de Astra, ronda 1). Para usar
   (A30) hay que tomar `V · A30` con el unitario `V` como **parámetro libre**, no cocientar por
   él. Esto es esencial: la velocidad estricta depende de `V`.
3. **Novedad.** La parte «clasificación unitaria s=2 en BCC sin la Eq. (2)» parece prior art de
   DEP19, salvo lo que diga la auditoría. Lo que el charter añade, si algo, es imponer la
   covarianza de las clases P/F con `R` no fiel o no Pauli, y la comparación entre `c_0` y
   `c_strict^iso`. Ninguna de las dos se ha localizado.

## Resto del informe

Solo se ha comprobado la identidad de los PDF por su p.1. Lo que Codex dice de cada uno no se
ha contrastado todavía:
- P17 sobre la nota [23] y la ref. [31]: coincide con la auditoría anterior del repo y con la
  ronda 1 de Astra.
- P14, Eq. (64): factor `√3` entre la velocidad relativista y la causal de un sitio por paso.
  `[UNVERIFIED]` en esta pasada.
- Raynal, Path-sum, Dirac 3+1, BBBP y Kempf–Portugal: sin contrastar.

Lagunas que Codex declara: Google Scholar no fue accesible, así que el seguimiento de citas de
P17, P14 y Raynal es parcial, y no se localizó la ref. [31].

## PDF incorporados

Duplicados comprobados por sha256 contra `biblioteca/` y `sources/`:

| Fichero de Codex | Estado |
|---|---|
| `arXiv-1902.10227.pdf` (DEP19) | **nuevo**, copiado a `biblioteca/` |
| `arXiv-1603.06442.pdf` (Dirac QW 3+1) | **nuevo**, copiado a `biblioteca/` |
| `arXiv-1705.08552.pdf` (path-sum Weyl) | **nuevo**, copiado a `biblioteca/` |
| `arXiv-0810.5495.pdf` (BBBP) | ya en `biblioteca/` |
| `arXiv-1306.1934.pdf` (P14) | ya en `biblioteca/` (otro nombre) |
| `arXiv-1703.05890.pdf` (Raynal) | ya en `sources/` |
| `arXiv-1708.00826.pdf` (P17) | ya en `biblioteca/` y `sources/` |

Catalogados en `scripts/biblioteca_catalog/curated.csv` (`proposed`). Índice regenerado: 73 PDF,
sin duplicados.
