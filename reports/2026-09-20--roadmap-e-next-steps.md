# Hoja de ruta — frente E

**Fecha:** 2026-09-20  
**Inicio operativo:** 2026-09-21  
**Rama:** `research/b-infinity-post-s4-gate`

## Estado de partida

El paper plano se considera cerrado. El frente científico activo es **E: estabilidad de la corona bajo la deformación inhomogénea/AdS**.

Estado de trabajo reconstruido:

- H2: `PASS`.
- H1: abierto.
- Límite local inclinado uniforme: abierto.
- E0: abierto.
- No heredar como certificados los `PASS` provisionales de exploraciones previas.
- No reabrir 4B por ahora.
- No volver a demostrar desde cero la asintótica plana: reutilizar §7.1–§7.7 como plantilla y auditar qué permanece, qué recibe un remainder controlable y qué falla.

## Gate 1 — test exploratorio falsable

Antes de invertir en la demostración completa, comprobar con la misma deformación/perfil (w) congelado:

[
R_N =
\frac{\mathrm{tail}_{AdS}(N)}
     {\mathrm{tail}_{flat}(N)}.
]

Predicción de E:

[
R_N = 1 + O(N^{-1}).
]

### Implementación

1. Localizar primero el código y los runs ya existentes del walk plano.
2. No crear un script nuevo mientras la infraestructura existente pueda reutilizarse.
3. Como la moneda es *on-site*, explotar que conmuta con la inclinación (e^{\xi_*\cdot x}).
4. Evolucionar directamente el operador inclinado para trabajar con amplitudes (O(1)), en vez de perseguir numéricamente la cola (e^{-K_*N}).
5. Explorar únicamente (N) moderados, aproximadamente (50\text{–}100), si el coste lo permite.

### Criterio de parada

Este cálculo es **exploratorio, no confirmatorio**.

- Si (R_N) se aleja de 1 al crecer (N), E queda refutada en esta formulación y se detiene el frente.
- Si la aproximación a 1 es claramente más lenta que (1/N), se detiene el frente.
- Si los datos son compatibles con (1+O(1/N)), no se declara E confirmada: se autoriza únicamente pasar al Gate 2.

## Gate 2 — congelar el objeto matemático

Fijar de forma inequívoca:

- el operador inhomogéneo (U_N=C_N(x)D);
- la inclinación;
- la definición exacta de la cola comparada;
- las hipótesis de regularidad de (artheta);
- el dominio complejo relevante para el saddle.

**Salida:** contrato matemático único antes de cualquier prueba larga.

## Gate 3 — control espectral uniforme

Demostrar persistencia del subespacio dominante en la región compleja relevante:

- gap uniforme;
- proyector de Riesz bien definido;
- control uniforme de las variaciones del proyector.

**Gate:** gap uniforme demostrado o `FAIL`.

## Gate 4 — H1

Convertir el esqueleto existente de H1 en una demostración bajo el contrato congelado.

Objetivo: controlar la acumulación de errores del producto inhomogéneo y justificar la reducción al subespacio dominante.

**Gate:** H1 = `PASS` o `FAIL`. No continuar con H1 abierto.

## Gate 5 — levantar la maquinaria plana

Auditar, uno a uno, los pasos §7.1–§7.7 del manuscrito plano.

Cada paso debe clasificarse exclusivamente como:

- `UNCHANGED`;
- `PERTURBED_WITH_CONTROLLED_REMAINDER`;
- `FAIL`.

Orden de trabajo:

1. representación inclinada;
2. saddles;
3. capas/perfiles;
4. límite local inclinado uniforme;
5. control de remainder.

## Gate 6 — estabilidad de la asintótica

Separar tres afirmaciones que no deben darse por equivalentes:

1. estabilidad del exponente (K_*);
2. estabilidad de la potencia (13/2);
3. estabilidad/control del coeficiente líder (C).

Cada una requiere su propio gate.

## Gate 7 — E0

E0 sólo pasa a `PASS` cuando exista una derivación ensamblada a partir de resultados ya cerrados, con fórmula explícita y remainder uniforme.

No declarar E0 cerrado por evidencia numérica, plausibilidad física o analogía con el caso plano.

## Gate 8 — decisión científica

Sólo después de E0:

- decidir si E se integra como extensión del paper;
- si justifica una nota separada;
- o si el resultado negativo debe registrarse y cerrar el frente.

No abrir mientras tanto una nueva búsqueda fenomenológica ni una nueva realización física.

## Regla operativa

**Un gate cada vez.** La primera tarea del 2026-09-21 es exclusivamente localizar la infraestructura existente y determinar si el test de (R_N) puede ejecutarse mediante modificación mínima. No generar código nuevo antes de esa inspección.
