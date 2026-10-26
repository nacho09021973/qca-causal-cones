# Cierre de reconstrucción documental — opción 1

Fecha: 2026-10-26. Autor: Codex. Autorización: «1 y después 2».

Los contratos e informes pendientes de G0 y selección de clase fueron
restaurados manualmente, con cuatro PASS de `check_reconstruction.py` contra
`2d144d9`, y conservados en commits `4e30a39` y `3246226`. La restauración
no revalida sus afirmaciones bibliográficas ni ejecuta nuevos gates.

Los residuos reales eran la hoja histórica E y las fórmulas de CURRENT_STATE.
La hoja pasa contra `2d144d9`; el estado pasa contra `8dd9080` con la opción
explícita `--allow-lost-cr-newlines`. Esta permite comparar las restauraciones
de rho, right y rm cuyo retorno de carro se había convertido en LF, además
de las barras y los escapes n que ya admitía el comprobador. No se activa por
defecto. Se contrastaron las fórmulas del estado con los informes W1, W2,
W3, W5 y respuesta elástica ya reconstruidos. No se cambió el contenido de
los estados históricos; las notas canónicas posteriores siguen prevaleciendo.

El único aviso de la transcripción de revisión del 23 de septiembre era
el cierre de una lista Python dentro de código cercado (línea 2540 antes
de cambios). No había corrupción que restaurar. Se dejó la transcripción
intacta; `text_integrity.py` omite únicamente delimitadores matemáticos
desnudos dentro de cercas Markdown. Los caracteres de control y sospechas
de escapes n se siguen comprobando dentro y fuera del código.
Seis pruebas permanentes en `scripts/test_text_integrity.py` cubren este
falso positivo, el retorno a texto normal y que no se oculten controles.

```sh
python3 -B scripts/check_reconstruction.py reports/2026-09-20--roadmap-e-next-steps.md
python3 -B scripts/check_reconstruction.py state/CURRENT_STATE.md 8dd9080 --allow-lost-cr-newlines
python3 -B scripts/test_text_integrity.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Resultado: ambos documentos PASS, seis pruebas PASS, **cero problemas** de
integridad y diff sin errores. La reducción final es 65 a cero: 34 delimitadores
de G0/clase, 26 del estado, cuatro de la hoja E y un falso positivo de código.
El criterio solo certifica ausencia de los patrones que detecta; no prueba
corrección científica, novedad ni ausencia de toda posible corrupción.

Las limitaciones encontradas durante la reconstrucción, en particular W4,
siguen registradas y pendientes de revisión independiente. Esta conclusión
termina la opción 1. La opción 2 autorizada empieza con derivaciones ejecutables
desde corrientes y puertas para W3/W5, y después obligaciones F1/F5/F6 y
calendario de profundidad finita W6. W1–W12 sigue cerrado por contrato.
