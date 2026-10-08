# B0 — auditoría acotada de acceso y error

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato padre [A/B](INVERSE_GRAVITY_IR_OPTIONS_AB.md).
Tick, β=1 y semilla B permanecen fijos. No se calcula su espectro.

## Objetivo y cierre

Comprobar si las cotas ya disponibles permiten certificar expectativas de
ρ_B mediante promedios locales truncados, sin matriz exponencial ni cambio
de regla. Un único expediente acotado: reducción local, semilla, convergencia.
Si falta un control necesario, cerrar como `B0_METHOD_NOT_CLOSED`, no FAIL físico.

## Pruebas

1. Auditar la dependencia del soporte de observables promediados en M y de
   las correlaciones de la semilla. No reemplazar Gibbs global por Gibbs aislado.
2. Auditar la suficiencia del defecto de estacionariedad ≤2/M para acotar
   error al ensemble límite. Un control matricial no simula la red.
3. Registrar qué información adicional requiere el filtro geométrico de
   quasifases o una alternativa local. No asumir un gap de fase uniforme.

Control permanente `scripts/verify_inverse_gravity_b0_error_control.py`:
dos niveles auxiliares, no el tick QCA. Para N=2,4,8,16 fijar
`V_N=diag(1,(N²+i)/(N²-i))`, semilla |+><+| y promedio de N pasos.
El ensemble infinito es I/2. Calcular exactamente cuadrado de distancia
traza al ensemble y cuadrado del defecto de estacionariedad.
Comprobar distancia ≥1/2 y defecto ≤2/N²; ninguna aproximación o fitting.
El objetivo es falsar la inferencia general «pequeño defecto implica
proximidad al ensemble». La prueba uniforme se escribirá en el informe.

El control no demuestra un gap pequeño ni fallo de convergencia de nuestro
tick fijo. Se declaran los N antes de ejecutar; no buscar otros N tras fallos.

## Límites

No calcular la batería de respuestas de B con un error sin certificar.
Si no hay control de semilla y promedio, B1/B2/B3 siguen NOT_EXECUTED y
`IR_SELECTION_OPEN_AFTER_AB` registra el límite de este intento.
La línea de diseño inverso puede volver a la arquitectura, pero no se cambia
el tick, baño, β o objetivo dentro de B. No hay teorema de imposibilidad.
