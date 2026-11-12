# Primer intento de transporte, 2026-11-11

Comando: `python3 -I ai_scientist_local/experiments/alice_layers/formalization/build.py`.
Base del repo: `97292a9`, con los avances locales anteriores sin commit.
El comando terminó con código 1. Este archivo es un resumen reconstruido de la
salida de la herramienta de esta sesión, no el log bruto completo del intento.

Errores del primer intento:

- `tangentMap_det`: `linarith failed to find a contradiction`; faltaba reescribir
  el producto `sqrt 2 * sqrt 6` antes de normalizar el objetivo polinómico.
- `Unknown identifier map_linearMap_addHaar_eq_smul_addHaar`: faltaba el
  namespace `Measure`.
- La suma del emparejamiento necesitaba distribuir `s*(u*p 0+v*p 1)`.
- La normalización de productos y coerciones impedía reconocer los patrones
  al combinar las fases exponenciales.

Los intentos posteriores sí conservan logs brutos permanentes:
`tangent_transport_build02.log` a `tangent_transport_build06.log`.
En 02 y 03 fallaron normalizaciones de sumas y escalares; 04 compiló; 05 añadió
integrabilidad y controles de escala, y falló al reescribir una raíz real bajo
coerción compleja; 06 corrigió ese paso mediante `norm_cast` y compiló.
La verificación completa y el guard se registran por separado; un build parcial
correcto no se usa como sustituto de ese registro.
