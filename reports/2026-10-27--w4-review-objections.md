# W4: comprobación de las objeciones de la revisión

Fecha: 2026-10-27. Autor: Codex. Revisión: DeepSeek, una ronda, informe
`debates/2026-10-26--w4-spectrum-review-deepseek/intentos/03-low/informe_deepseek.md`,
`ACCEPT_WITH_REPAIRS`. La cabecera del informe identifica el lanzador de
`~/herramientas` en `16568209771dc898346bd4af0c78ec10530c3b9e`, la entrada y
los documentos enviados. El esfuerzo low y la revisión por un modelo no son
una garantía de corrección ni sustituyen una revisión humana. Las comprobaciones
y reparaciones siguientes son del autor, no una aceptación adicional del revisor.

| Objeción | Comprobación y tratamiento |
| --- | --- |
| W4-R1-01 | Confirmada: el circuito completo se construye desde SWAP, pero la comparación importa `bloch_step`. El informe ya decía que no era revisión independiente. Se aclara también en la cabecera del script; no elimina errores de convención compartidos. |
| W4-R1-02 | La derivada implícita `sin(2 kappa)` también es no nula en `(pi/2,pi)`. Allí la rama local que vale cero tiene coeficiente `tan(kappa)/4`, negativo; la rama angular requiere elección local módulo `2pi`. Esto sigue del mismo argumento, no de los anillos. El resultado certificado original permanece limitado a `(0,pi/2)` y no se amplía el contrato. |
| W4-R1-03 | Confirmada la ambigüedad de la etiqueta histórica: el informe ya distingue explícitamente la rama cero cuadrática. Se conserva la etiqueta histórica para identificar la conclusión sustituida; no significa un gap de cuasienergía respecto al vacío. |
| W4-R1-04 | Confirmada la dependencia común de `assert_sym_equal`. Se añadió en el certificado espectral una comprobación exacta puntual de la traza, usando `expand` y `simplify` directamente y una mutación que omite la fase. Esta vía aún depende de SymPy y no constituye prueba independiente de todas las identidades. |
| W4-R1-05 | Confirmada la cobertura: 12 circuitos con `L=4,6`, tres ángulos y dos signos. El informe y el encabezado del script ya los declaran testigos finitos, sin extrapolación ni revisión independiente. No se amplía esa cobertura. |

Los cinco puntos están atendidos localmente en el alcance indicado. No se ha
consultado de nuevo al revisor: las objeciones no se declaran resueltas por él.
El expediente sellado y el informe de auditoría revisado conservan su contenido.
Los dos scripts han cambiado después de la revisión: el manifiesto de entrada
original ya no coincide con esos archivos actuales y sigue identificando los
bytes enviados, disponibles en el commit `85e22e0` y en la entrada sellada.
La revisión se refiere a aquellos bytes; los cambios posteriores tienen
verificación del autor. W4 sigue `OPEN_AFTER_AUDIT`; no se abre W1–W12 ni se
infiere una onda métrica, un resultado tensorial o gravedad.

Validación: los dos certificados W4 pasan; el
[barrido completo](2026-10-27--w4-review-repairs-verifier-sweep.tsv) terminó
con 43 verificadores y cero fallos. El [manifiesto](2026-10-27--w4-review-repairs-inputs.sha256)
identifica los dos certificados W4, el helper, el lanzador y las dependencias
declaradas; no pretende identificar todos los archivos del barrido.
`text_integrity.py --check` devuelve cero problemas y `git diff --check` pasa.
