# Lectura del autor — revisión Grok del borrador v1 del charter s=3

Fecha: 2026-10-29. Autor: Claude, autor del borrador. **No es una revisión independiente.**
Bytes revisados: `5fe04ae`. Herramienta: `revision_ciega.sh` @ `a32e189`. Autorización: «D3 Grok».

## Veredicto del revisor

**NOT_READY**, con diez reparaciones G-S3-01..10.

## Contraste

| ID | Lectura del autor |
| --- | --- |
| G-S3-01 (paridad del determinante) | **Se acepta. Rehecho a mano.** Cada término de `det U` es un producto de tres coeficientes, así que su frecuencia es suma de tres vectores de `{±1}^3`: tres impares por coordenada, luego impar, nunca 0. A3 obliga a que `det U` sea un monomio `ζ e^{-ik·m}`, y la covarianza a que `g^T m = m`. `V4` solo fija `0`; el `C4` de cara solo fija el eje (dos coordenadas nulas). Ninguna de las cinco clases admite un símbolo unitario, para ninguna `R`. Mi B5 sacaba la consecuencia equivocada («reducción de variables»). Queda `[UNVERIFIED]` hasta certificarlo. Observación del autor: el argumento vale para todo `s` impar con soporte `N_3` sin término on-site; queda fuera del alcance de este charter. |
| G-S3-02 (codificación del sector por rango) | Se acepta. La codificación de 4b-2 es la de `s=2` y no se puede copiar. |
| G-S3-03 (equivalencia proyectiva, producto por un carácter, `C4`) | Se acepta. |
| G-S3-04 (B4 no vacía clases) | Se acepta. |
| G-S3-05 (frase sobre la dimensión no rígida mínima) | Se acepta. Excedía los techos. La marca de `s=2` ya es ESTABLISHED (4b-2 promovida en `ea3f401`, después del envío). |
| G-S3-06 (el testigo no tiene soporte en `N_3`) | **Se rechaza: error del revisor.** `e^{-iqσ_j} = cos q − i sin q σ_j` solo tiene frecuencias `±1`, así que el producto tiene soporte en `{±1}^3`, ocho modos, sin término on-site. El certificado de 4b-1 lo comprueba (ocho coeficientes no nulos y unitariedad de Laurent solo sobre `N_3`). Aun así, en v2 el control positivo pasa a ser el Pavia ya certificado, que es el mismo símbolo (quiralidad −1). |
| G-S3-07 (techo solo en `k_⋆ = 0` o con transporte; conflicto) | Se acepta. |
| G-S3-08 (resultados de la unión; cierre en el paso 0; B7) | Se acepta. |
| G-S3-09 (T3/O3 ESTABLISHED) | Se acepta en parte. El revisor no tenía `CURRENT_STATE`, que las promociona en `5424771` tras las revisiones de Gemini y Grok. La cabecera del charter de isotropía irreducible sigue diciendo PRELIMINARY: está desactualizada. v2 cita la promoción. |
| G-S3-10 (dominio de Q-a3; conjunto real completo; literatura; B1; B2) | Se acepta. |

## Conclusión del autor

v2 aplica G-S3-01..05 y 07..10. El paso 0 empieza por el lema de paridad: si el certificado
cierra, el desenlace de la unión es `S3_VACUOUS_IN_DECLARED_FAMILIES` en el paso 0, y los pasos
1 y 2 no tienen objeto. Congelar el charter y decidir si hace falta una segunda ronda lo decide
el usuario.
