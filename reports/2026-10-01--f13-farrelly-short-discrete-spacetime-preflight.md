# F13 — Preflight de Farrelly–Short: partículas causales en espacio-tiempo discreto

Fecha: 2026-10-01. Fuente primaria local:
`biblioteca/1312.2852v1.pdf`, *Discrete Spacetime and Relativistic Quantum
Particles*, arXiv:1312.2852v1. SHA256:
`a6babd4fdb67f84a24dc1b00fe3a8a484c0511c8da8d209eec14a352624fc95a`.

## Lectura primaria

Se leyeron las pp.1-6 mediante `pdftotext -layout`. Las pp.1-2 definen una
partícula en red discreta, translacionalmente invariante, causal y con espacio
interno finito; la evolución tiene la forma `U_D = sum_q A_q S_q` y soporte
finito (p.2, Ecs.3-8). Las pp.2-3 derivan el Hamiltoniano continuo de bajo
momento y una cota de convergencia bajo `a, delta t -> 0` con `a/delta t`
constante (pp.2-3, Ecs.9-16).

En d=3, las pp.3-4 muestran que el límite sin masa con espacio interno de
dimensión 2 es Weyl, tras una posible relabelación/rescalado de ejes; la
simetría rotacional en el límite también fuerza esa forma (p.3, Ec.17; p.4,
Ecs.18-19). La p.4 da el ejemplo BCC de desplazamientos condicionales que
realiza Weyl (Ecs.20-21). Para dimensión interna 3, las pp.4-5 presentan
`H = J dot P`, rotacional pero no Lorentziano, y una evolución como producto
de desplazamientos condicionales (pp.4-5, Ecs.22-25). La p.5 trata la masa y
la obtención de Dirac bajo hipótesis adicionales.

## Comprobaciones de alcance

La familia es una clase general de walks de una partícula con soporte finito y
espacio interno arbitrario; no es el QCA Weyl BCC de F12 ni una construcción
Maxwell compuesta. El resultado de Weyl depende de dimensión interna 2 y permite
relabelación/rescalado de coordenadas. El ejemplo de dimensión interna 3
muestra que simetría rotacional no basta para obtener invariancia de Lorentz;
no es un test sobre las cuatro especies CJWW del proyecto.

La fuente no especifica una regla CJWW en `Z^3` con controles geométricos, una
métrica variable, backreaction, stress/source local ni una equivalencia con el
contrato W6. No se ejecuta un test de universalidad ni se deduce una escala
física absoluta.

## Resultado documental

```text
F13_FARRELLY_SHORT_PREFLIGHT =
PUBLISHED_CAUSAL_SINGLE_PARTICLE_WALK_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT

THREE_COMPONENT_COUNTEREXAMPLE = ROTATIONAL_NOT_LORENTZIAN
FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

La ficha es una entrada nueva porque registra una clase general de partículas
causales discretas y su separación entre el teorema interno-2 y el
contraejemplo interno-3; no duplica F5, F6 ni F12.
