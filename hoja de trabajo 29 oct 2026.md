# Hoja de trabajo — 29 de octubre de 2026

Rama: `research/inverse-gravity-design`. Sustituye a la [hoja del 28 de octubre](hoja%20de%20trabajo%2028%20oct%202026.md).
La fuente de verdad sigue siendo `state/CURRENT_STATE.md`. Esta hoja ordena los próximos pasos y no autoriza
nada por sí misma.

## En una frase

La simetría fuerte (cubo completo con representación interna irreducible) **no** da modelos: las tres clases
son vacías. Con la simetría débil (D2) hay modelos en los que c sale de la geometría (Pavia, s = 2) y otros en
los que no (familia s = 4). Falta saber qué condición los distingue.

## Qué se hizo el 28 de octubre

1. **Paper de la corona (`papers/ir-corona/`):**
   - Sanedrín: los cuatro miembros dieron `ENVIABLE_CON_REPARACIONES`, con tres reparaciones obligatorias.
   - Las reparaciones están hechas.
   - Revisiones ciegas: astra dio `CERRADA_CON_ARREGLOS` (arreglos aplicados) y DeepSeek `CERRADA`.
   - Los certificados del Apéndice A pasan (156/156).
   - Auditoría de prioridad: `NO_ANTICIPATION_FOUND / NOVELTY OPEN`. La tesis de Bressler ya está leída.
   - Tag `ir-corona-v1` creado y subido. El DOI queda pendiente porque el repo es privado.
2. **`revision-ciega`:** DeepSeek usa ahora por defecto el máximo de tokens de la API (herramientas `83c04f9`).
3. **Hipótesis 3 (representación irreducible):**
   - Carta `theory/IRREDUCIBLE_ISOTROPY_MATCHING_GATE.md` (`d112bb0`); pasos 0–1 autorizados (`43fd00e`).
   - Ejecución: `88b07ed`. T3, O3 y O4 dan `EMPTY_CLASS` (PRELIMINARY), con 31/31 comprobaciones exactas.
   - Barrido completo: 47/47.
   - Revisión ciega con DeepSeek **en curso**: `debates/2026-10-28--irreducible-isotropy-step01-review-deepseek/`.

## Próximos pasos, por orden

### 1. Cerrar la revisión de DeepSeek sobre la hipótesis 3

1. Leer `informe_deepseek.md` sin editarlo.
2. Contrastar cada objeción con el certificado. Si alguna afecta al vacío de una clase, rehacer ese cálculo
   antes de dar nada por bueno.
3. Escribir `verificacion_autor.md` y hacer commit de la carpeta.
4. Si el veredicto lo permite, actualizar `CURRENT_STATE` (Sec. 4, filas `B_infty^*`) en un commit aparte.

Si DeepSeek no termina, se archiva el intento y se repite una vez, como permite el encargo.

### 2. Decidir la siguiente condición para B∞\* (la decide el usuario)

Las candidatas, todas con la simetría débil D2 y la red de los 8 vértices fija:

| # | Condición | Por qué |
|---|---|---|
| 1 | **La parte sin masa no se mezcla con el resto** (métrica cuántica entre sectores nula en el nodo) | La familia s = 4 cumple exactamente c² + 2 sin²(Δε/2)·g(0) = 1/3: lo que le falta a c se gasta en esa mezcla. Es la más concreta. **Recomendada.** |
| 2 | s = 2 sin la ecuación (2) de P17 | Cerraría el caso mínimo |
| 3 | Todas las bandas comparten el mismo cono | Más fuerte que la 1; probablemente la implica |
| 4 | D2 más paridad o inversión temporal | Sin mirar; podría separar Pavia de s = 4 |
| 5 | Cambiar la geometría (término en el sitio, más vecinos, otra red) | Cambia el sustrato; las reglas lo excluyen salvo con una carta propia. Para el final |

Si se elige la 1:
- Escribir su carta, con la clase congelada, la definición exacta de «sin mezcla» y sus resultados posibles.
- Antes de nada, comprobar si la identidad de la familia s = 4 tiene una versión general. Si no la tiene, la
  carta debe decir de qué clase se habla.
- Hacer commit de la carta y esperar la autorización.

### 3. Deuda documental del verificador nuevo

`scripts/verify_irreducible_isotropy_step01.py` no aparece en `scripts/README.md`. Hay que documentar qué
certifica, qué no certifica (representaciones reducibles, otros grupos, otros soportes, s = 1) y su tiempo, que
son unos 8,5 minutos, el más lento del barrido.

### 4. Paper de la corona: lo que falta para enviarlo

- DOI: decidir cómo se publica el código (repo público + Zenodo, o subir a Zenodo solo lo necesario).
- Quedan tres comprobaciones bibliográficas `[UNVERIFIED]`: libro ACSV, capítulo de Tate de 2016 y si la
  versión publicada de CJWW conserva la frase de los «dos estudios».
- Nadie ha revisado las líneas de autor de `f85f429` y `951bbe3`.
- Opcional: mover el tag `ir-corona-v1` al texto final. Reescribe una referencia pública: pedir confirmación.
- Enviar o no el paper: lo decide el usuario.

### 5. Pendientes heredados de la hoja del 28

- Decisión de rumbo de A.int (Eon), para `/comite`.
- Revisiones independientes: W3/W5/W6 reforzados, primer candidato de Eon, reparaciones de W4, W1/W2/W7 y
  puentes CJWW, F2/F4.
- Comité sobre la línea de gravedad inversa.

### 6. Mantenimiento

- Push: hay cuatro commits locales por delante de `origin` (`94fb130`, `d112bb0`, `43fd00e`, `88b07ed`).
- `debates/2026-10-28--eon-addendum-review-deepseek/` sigue sin commit. No es de esta sesión: preguntar
  antes de tocarlo.

## Comprobaciones antes de cada sesión

```sh
python3 -B scripts/run_all_verifiers.py --output reports/<fecha>--verifier-sweep.tsv   # ~10 min (47 verificadores)
python3 -B scripts/text_integrity.py --check        # 0 problemas el 28-10
sanedrin --listar
```
