# Auditoría de la hoja del 6 de noviembre: protección y selección

2026-11-06. Codex (OpenAI). Base: b434547432647ca72110d4f7b6c78583d70f27c9,
research/schur-stability-audit; árbol limpio al empezar.
Ejecución documental de las etapas 1–2 y diagnóstico de la etapa 5 de
`2026-11-06--work-plan-symmetry-common-cone.md`. Sin revisión externa,
promoción, nuevos modelos ni ejecución de verificadores.

## 1. Premisas auditadas

Leídos PROJECT_INSTRUCTIONS, CURRENT_STATE, índice de biblioteca, contrato
y reporte de forma normal, informes PHS y doble desplazamiento, y código
del verificador de forma normal. Los tres hashes de scripts coinciden con
los publicados en esos informes:

- forma normal: 16639f7fd11d3e42dd9385db58a373d0b2bb3ca976ec876dc41e973ae35cbf4b;
- PHS: b4bfffacf6a0629276d7427be16a5ea9225cce2e3b1b0631734e4c0fe90da75a;
- doble desplazamiento: 07bdcfbb2a9ffbdbaa9b798a0f3e99f9d91a3991fb40abb1c5b1ab9acdcfa2f6.

Se relee la derivación previa, sin extenderla: al derivar
V U(k)* V†=U(-k), aparecen dos cambios de signo en J_i=iW†∂_iU:
el de la derivada y el de i. Por ello C J_i C⁻¹=J_i, no -J_i.
La conjugación Pauli elimina sigma_i tensor I y conserva
sigma_i tensor tau_j. En las compresiones nodales, tau se sustituye por
±n, y las pendientes cuadráticas de ambos sectores coinciden.
Segunda lectura del mismo resultado: el emparejamiento espectral
(k,omega) ↔ (-k,-omega) impone la misma dispersión reflejada alrededor
de las fases nodales conjugadas. No requiere que sea isotrópica.

No se detecta reparación sustantiva en estos pasos. Se usan como premisa
provisional de autor; esta relectura no es revisión independiente.
«Separados» significa que los dos eigenvalores de W son distintos:
no hay gap dentro de cada doblete. El cruce cónico requiere además
u_x u_y u_z != 0. En el caso límite de algún u_i=0, la forma normal
sigue valiendo pero no garantiza un cono tridimensional no degenerado.
La estabilidad local invocada requiere continuidad de esas derivadas y
conservación de las simetrías y de la separación entre dobletes.

## 2. Comparación primaria y límite de novedad

| Afirmación | Original leído | Alcance y diferencia restante |
| --- | --- | --- |
| PHS empareja quasienergías | Asbóth, 1208.2143v2, HTML Sec. III.1, Ecs. (10)–(11) y párrafo siguiente | Antecedente explícito en 1D. Su aplicación al par conjugado s=4 es inferencia del autor; no atribuir ese modelo al artículo. |
| El operador de simetría debe permanecer fijo al variar parámetros | Mismo original, Sec. III.3 | Advertencia metodológica explícita. Aquí se mantiene C fijo. No se adopta una afirmación general sobre ausencia de simetría quiral en otros marcos temporales. |
| Isotropía microscópica exige covariancia del walk | `biblioteca/1708.00826v2.pdf` p.2, Def. 1 y Ec. (4); pp.3–4 | Se exige representación proyectiva unitaria y acción transitiva sobre generadores. La clasificación posterior se restringe a s=2; no clasifica nuestro s=4 con dos fases nodales. |
| El coeficiente continuo no queda fijado por unitariedad solamente | `biblioteca/1609.00305v2.pdf` p.4, Ecs. (18a), (27)–(29); p.5, recapitulación y Sec. IV; p.6, Sec. V | B1 es compresión de una involución, con espectro en [-1,1]; se construyen monedas y encoding para coeficientes prescritos. Es otra arquitectura y otro límite continuo: no certifica realización del soporte s=4 aquí fijado. |

Original web leído: https://arxiv.org/html/1208.2143v2 . Los otros dos
originales se leyeron en los PDFs locales, no en informes previos.

**Evaluación de autor:** el emparejamiento antiunitario y la restricción
local por representación son álgebra estándar. La propuesta de completar
la isotropía imponiendo una covariancia espacial que relacione direcciones
no aporta, por sí sola, un mecanismo de selección ni una candidatura de
novedad defendible. La clasificación citada ya exige equivalencia dinámica
de direcciones como hipótesis. Esto no identifica su definición de isotropía
con cualquier igualdad de pendientes en un Hamiltoniano efectivo.

No localizado en esta lectura: una clasificación del problema exacto s=4,
dos dobletes conjugados, con la representación y soporte de la hoja.
La cobertura no permite afirmar que tal realización esté publicada ni
que sea nueva. Tampoco se ha probado hoy el enunciado adicional de giro
cíclico: no se congeló su representación ni se abrió el cálculo.

Se aplica el corte de la etapa 2 **a la candidatura del argumento local
como contribución original**. Resultado de ese componente:
`STANDARD_SYMMETRY_COROLLARY` (evaluación documental de autor, no teorema
nuevo ni clasificación completa). No se abre una construcción para
rescatar esa candidatura. La cuestión más fuerte de realización exacta
queda `OPEN_WITH_NAMED_OBLIGATION`: fijar representación espacial y soporte,
y demostrar existencia compatible e irreducibilidad. No se ha demostrado
obstrucción ni se ha agotado una búsqueda. Etapas 3–4 no ejecutadas por
este corte, no por agotamiento del presupuesto de cuatro horas.

## 3. Selección: un mecanismo localizado, otra clase

Leído `biblioteca/arXiv-1102.0789.pdf` pp.1–2 (Anber–Donoghue,
The emergence of a universal limiting speed). Allí la variable es la
velocidad renormalizada de campos interactuantes al cambiar escala,
con ecuaciones beta, p.2 Ec. (2), y acoplamientos Yukawa/gauge. El resumen
y la introducción advierten que la convergencia usual es logarítmica;
el análisis declarado es a un loop. Esto localiza un mecanismo candidato
de flujo efectivo, no una relajación temporal de monedas del QW libre.
No se han comprobado aquí los cálculos de loops ni los modelos de otras
secciones, ni se traslada su conclusión a este repositorio.

En nuestra clase no se ha especificado una ley que haga evolucionar los
parámetros de actualización hacia mayor simetría, ni un criterio de
selección. Diagnóstico: `SELECTION_MECHANISM_NOT_SPECIFIED`.
Introducir interacción o un flujo efectivo necesita un contrato sucesor;
no se calcula ni se autoriza aquí. El valor físico de c sigue sin fijarse.

## 4. Cierre de esta ejecución

La hoja se ha continuado hasta su corte documental. Se conserva una
explicación provisional de protección entre dobletes conjugados. No se
obtiene una explicación de selección, universalidad entre pares distintos,
ni escala física. No se declara imposible ninguna de ellas.
La realización exacta con simetría espacial adicional no ha sido examinada;
no presentar este cierre como `PROTECTION_IN_NONEMPTY_CLASS` para esa
extensión. El cierre se limita a la candidatura local y no refuta la
intuición general de emergencia. Sin commit/push ni envíos a terceros.
