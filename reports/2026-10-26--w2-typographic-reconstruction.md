# W2 — reconstrucción tipográfica y comprobación local

Fecha: 2026-10-26. Autor: Codex. Base de trabajo: `ba5c71c`.
Autorización: «adelante» a reconstruir el contrato W2 y sus dos informes,
sin cambiar el alcance científico. Este registro no es una revisión independiente.

## Alcance

Se restauraron manualmente los delimitadores y comandos LaTeX de:

- `theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md`;
- `reports/2026-09-30--w2-transport-tetrad-bridge.md`;
- `reports/2026-09-30--w2-tetrad-backreaction-audit.md`.

Cada documento lleva una cabecera de procedencia. El comprobador permanente
`scripts/check_reconstruction.py`, con base por defecto `2d144d9`, da PASS
en los tres: fuera de esas cabeceras solo se restauraron barras invertidas.
También se restauraron los dos saltos de línea que correspondían a `\ne0`.
No fue necesario elegir entre reconstrucciones matemáticas incompatibles.
El contrato de auditoría `theory/W2_TETRAD_BACKREACTION_AUDIT.md` usa ASCII
intencionadamente y no se modificó.

## Contraste de las fórmulas

Se leyó `scripts/verify_w2_transport_tetrad.py` y su función de base
`walk2()` en `scripts/verify_directional_saturation.py`. El certificado ejecutado
da sus seis PASS: derivadas del símbolo plano, determinante de D, matriz E,
control aislado de la primera familia, símbolo escalar de corriente y
determinante de E en acoplamiento nulo.

Como segunda comprobación manual del signo del transporte, con la convención
de Fourier del informe el operador de desplazamiento tiene símbolo
`exp(-i p·d)`. Su diferencia hermítica da `i(exp(-iq)-exp(iq)) = 2 sin(q)`.
Multiplicar el término `-2ig b_a (d_a·p) sigma_a` por la base plana, a primer
orden en g y momento, resta `2g diag(b) D` a E0. El límite g = 0 recupera E0.
En la base de los dos extremos, la parte espacial de la corriente es la matriz
de Pauli Y; los vectores `(1, ±i)/sqrt(2)` tienen valores propios ±1.
Esto fija también los signos de los estados de corriente de la sección 4.

La conservación de B se comprobó manualmente de dos formas:

- El conmutador de `B tensor J` con `B tensor I` es cero.
- En la base propia de B, cada bloque de la evolución es `exp(-ig beta J)`;
  la evolución no mezcla los sectores de B y conserva su valor esperado,
  también para estados conjuntos entrelazados.

Los restantes enlaces tienen registros distintos y la base CJWW actúa solo
en materia, por lo que tampoco cambian B en este modelo.

Estas comprobaciones manuales quedan trazadas aquí; no se ejecutó código
ad hoc ni se modificaron certificados. El certificado W2 existente no deriva
por sí solo la matriz E desde el producto de capas y no comprueba todas las
obligaciones de retroacción, localidad o síntesis del paso completo.

## Validación ejecutada

```sh
python3 -B scripts/check_reconstruction.py theory/W2_TRANSPORT_TETRAD_BRIDGE_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w2-transport-tetrad-bridge.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w2-tetrad-backreaction-audit.md
python3 -B scripts/verify_w2_transport_tetrad.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Resultado: reconstrucción 3/3 PASS, certificado W2 PASS y diff sin errores
de espacios. El detector global pasa de 611 a 499 avisos: se retiran los
112 delimitadores desnudos de estos tres documentos (26 + 70 + 16).
Los avisos restantes pertenecen a la cola previa; el detector global sigue
saliendo con código 1. No se ejecutó el barrido completo de certificados:
no se cambió código y se ejecutó el certificado directamente relacionado.

## Estado conservado y cierre

Se mantiene `W2_PRINCIPAL_SYMBOL_CONTROL = PASS` junto con
`W2_TETRAD_CONTROL_CONSERVED / BACKREACTION_FAIL`, conforme al informe
posterior de auditoría. La interpretación original de tetrad dinámico está
superada; las nuevas cabeceras lo advierten sin reescribir el registro histórico.
W1–W12 continúa cerrado por contrato. No se promueve evidencia científica,
no se abre un modelo sucesor y no se envía texto a terceros.

Este bloque termina en W2. La reconstrucción W1 y el refuerzo de certificados
siguen pendientes según la hoja del 22 de octubre.
