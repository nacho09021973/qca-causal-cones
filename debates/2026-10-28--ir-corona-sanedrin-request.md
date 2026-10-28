# Sanedrín: ¿está el paper de la corona listo para enviarse?

Solicitud del P.I. (2026-10-28): «lanza el sanedrín con el paper de la corona».

## Objetivo

Atacar las afirmaciones centrales de `papers/ir-corona/ir-corona.tex` (adjunto, versión
autoritativa) antes de decidir si se envía como preprint. El manuscrito se escribió con ayuda de
Claude; por eso este sanedrín no incluye ningún miembro de esa familia.

## Qué se pide atacar

1. **Corrección del resultado principal (Theorem 4.3, leading asymptotics).** ¿Hay algún paso
   del análisis de punto de silla, de la unicidad del minimizador regional que fija
   `K_* ≈ 0.1905`, del exponente `N^{-13/2}` o del coeficiente `C(θ)` que no esté justificado o
   que dependa de una hipótesis no declarada? La no anulación de `C(θ)` se certifica con
   aritmética de intervalos: ¿qué cubre exactamente ese certificado y qué no?
2. **Theorem 4.1 (cota explícita) y 4.2 (tasa regional).** La parte no asintótica de 4.1 está
   formalizada en Lean (README adjunto, con lo que *no* se formaliza). ¿Es coherente lo que el
   paper atribuye a Lean con lo que el README dice que se demostró?
3. **Novedad.** El párrafo de novedad (sección 1) afirma ser «the first prefactor-level
   asymptotic, with a leading coefficient that is oscillatory and certified to be non-vanishing,
   for an infrared-controlled operational response in the strictly outside-propagation-region
   regime of a three-dimensional multi-component quantum walk». ¿Es defendible y
   suficientemente estrecho frente a la literatura de grandes desviaciones de paseos cuánticos,
   ACSV (Pemantle–Wilson) y la desigualdad de Bernstein (trabajo previo reconocido en la nota
   adjunta)? Si conocéis un resultado previo concreto que lo cubra, citadlo con autores, año y
   título; marcad como no verificado lo que no podáis asegurar.
4. **Lectura física.** ¿Se sigue del teorema la conclusión «the emergent cone is not
   operationally sharp, even for infrared-admissible operations»? ¿Es la definición de
   admisibilidad infrarroja razonable o está hecha a medida del resultado?

## Resultado esperado

Cada miembro termina con un veredicto de esta lista y nada más:

- `ENVIABLE`: ningún cambio obligatorio.
- `ENVIABLE_CON_REPARACIONES`: con una lista numerada de reparaciones **obligatorias**, separada
  de las sugerencias **opcionales**.
- `NO_ENVIABLE`: con el defecto que lo impide, localizado (sección, ecuación o teorema).

Cada objeción debe señalar el lugar exacto del paper. Lo que no se pueda comprobar con el material
adjunto se marca `[NO VERIFICADO]`.

## Límites y cierre

- Máximo **2 rondas**. Se cierra con los veredictos finales de la segunda ronda.
- Sólo cuenta como fuente lo adjunto: el `.tex`, `formal/README.md` y `sources/README.md`.
- El resultado no autoriza nada: no se envía el paper ni se cambia `CURRENT_STATE.md` sin decisión
  del P.I. Las reparaciones que se acepten se harán en commits aparte.
