# F12 — Preflight QCA de la luz

Fecha: 2026-10-01. Fuente local:
`biblioteca/Quantum Cellular Automaton Theory of Light.pdf`.
SHA256: `8f36b0936fd8ab3f396d8495f15bd66033657fd860f94179db2819d708672fa0`.

## Lectura primaria

Se leyeron las pp.1-7 mediante `pdftotext -layout`. La p.1 presenta el
objetivo: dos Weyl QCA producen Maxwell a bajo vector de onda, con dispersión
y polarización longitudinal a alta frecuencia. Las pp.2-3 definen QCA,
localidad, homogeneidad, transitividad e isotropía; fijan `G=Z^3`, dos
componentes y la red BCC, y dan las matrices `A_k^±`. Las pp.3-5 construyen
los bilineales de dos campos y su régimen bosónico de baja densidad. La p.6
da `ω(k)` y la corrección `c(k)`; la p.7 deja abierta la acción de Poincaré
y recalca el marco de referencia fijo.

## Comprobaciones de alcance

La regla es una QCA lineal de un paso con soporte finito, no un Hamiltoniano
continuo. El objeto Maxwell es compuesto: dos campos fermiónicos y operadores
bilineales. La derivación no introduce un campo de tetrad, una métrica
variable, un stress tensor local ni una respuesta a controles de hopping.

La fuente afirma que el límite `|k| << 1` recupera Maxwell y que para `k`
finito la velocidad de grupo depende de `k`; también afirma que la corrección
no es isotrópica y puede ser superluminal aunque acotada (p.6). Esto se
registra como resultado atribuido al artículo, no como cálculo independiente.

## Resultado documental

```text
F12_BISIO_DARIANO_PERINOTTI_LIGHT_PREFLIGHT =
PUBLISHED_3D_WEYL_QCA_MAXWELL_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT

FOUR_SPECIES_TEST = NOT_EXECUTED
EVIDENCE = BOUNDED_PRIMARY_SOURCE_READING
INDEPENDENT_REVIEW = NOT_PERFORMED
```

La ficha es una entrada nueva porque el objeto es un QCA Weyl 3D con
Maxwell compuesto; no duplica F5 (walk curvo por operator splitting), F10
(CA gauge-invariant) ni F11 (acción U(1) 1+1D).
