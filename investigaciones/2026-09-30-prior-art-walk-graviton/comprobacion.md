# Comprobación de los informes de Gemini contra los originales — 2026-09-30

Informes: `informe_gemini.md` (dirigido) e `informe_gemini_abierto.md` (abierto), traídos por el
usuario desde la web de Gemini. Originales descargados de arXiv a `biblioteca/` (local, no
versionada) y leídos con `pdftotext -layout`; `p.N` es la página del PDF.

## Hallazgos generales

- **Citas circulares o débiles en el dirigido.** Las confirmaciones sobre Gu–Wen citan sobre todo
  la referencia 1, que es nuestro propio `prompt.md`. Otras fuentes: Wikipedia, Grokipedia,
  Scribd, gsjournal. La afirmación "Sección VI declara los fermiones como trabajo futuro" cita un
  PDF de Scribd sobre spin foams (ref. 8). Nada del dirigido cuenta como confirmación por sí solo.
- **Los dos informes se contradicen sobre Gu–Wen** (dispersión del modelo controlado). Resuelto
  abajo a favor del dirigido.

## Gu & Wen, arXiv:0907.1203v3 (`biblioteca/arXiv-0907.1203.pdf`)

| Atribución (W8–W10 / informes) | Resultado | Evidencia |
|---|---|---|
| Modelo L: modos ±2 como únicas excitaciones de baja energía, ε ∝ \|k\|³, enfoque semiclásico fiable | **CONFIRMADO** | p.1 (resumen) |
| Modelo N: ω ∝ k solo argumentado, sin enfoque fiable | **CONFIRMADO** | p.1: "no reliable approach … we argue"; p.22: "even though we can not show it reliably. Numerical calculations are needed" |
| Informe abierto: Gu–Wen obtienen ω ∝ k con control analítico | **REFUTADO** | p.1, p.22 |
| a₀₀ y a₀ᵢ como multiplicadores de Lagrange de las restricciones escalar y vectorial; al integrar E^{ij} sale la acción de Einstein linealizada | **CONFIRMADO**, con matiz | p.12, ec. (37). Se dice del modelo continuo con restricciones, no del modelo L en red (cuya dispersión es k³) |
| Restricciones impuestas en red mediante penalizaciones de energía | **CONFIRMADO** | p.1 (índice, §V "imposing constraints through energy penalties"); p.7; p.12 |
| Acoplar a fermiones casi sin masa queda como trabajo futuro | **CONFIRMADO en sustancia**, no como "Sección VI" | p.3 (§I, introducción): "We hope in the future, we can construct a local qubit model where light, gravity, and nearly massless fermions emerge at low energies." El "future efforts" de p.22 es otra cosa (dispersión lineal) |
| La dispersión k³ del modelo L es robusta frente a correcciones perturbativas | **CONFIRMADO** (dato nuevo, relevante para B3 de `reparaciones.md`) | p.22 |

Consecuencia para W10 (reparación B3): la dinámica de Einstein linealizada (G_lin) solo aparece
en el continuo (ec. 37) o en el modelo N sin control. El modelo L controlado no es Einstein
linealizado. C2 de W10 debe declarar qué sector usa.

## Arnault & Debbasch, arXiv:1609.00722v2 (`biblioteca/arXiv-1609.00722.pdf`)

- DTQW en red (1+2)D cuyo límite continuo es un fermión de Dirac acoplado a un campo gravitatorio
  relativista arbitrario, aplicado a ondas gravitatorias lineales dadas: **CONFIRMADO**, p.1
  (resumen).
- "La métrica es un fondo externo, sin backreaction": **CONSISTENTE**. No aparece fuente ni
  backreaction (búsqueda de "backreact", "source", "self-consistent"); las ondas son soluciones
  dadas de Einstein linealizado (p.3). Sin lectura completa.

## Arnault & Cedzich, arXiv:2208.14997 (`biblioteca/arXiv-2208.14997.pdf`) — solo en el abierto

- Acción tipo LGT en tiempo real para un espinor de una partícula en red (1+1)D basada en un DTQW,
  teorema de Noether en red para simetrías **internas**, y acoplamiento mínimo a un campo
  electromagnético: **CONFIRMADO**, p.1–2, §III en p.5.
- Relevancia: antecedente directo para corrientes conservadas locales en tiempo discreto (W11 F4 y
  reparación C3). No trata energía-momento ni gravedad; eso es inferencia del informe.

## Rasmussen, You & Xu, arXiv:1601.08235 (`biblioteca/arXiv-1601.08235.pdf`)

- Existe y trata líquidos de Bose algebraicos estables sin simetría, con excitaciones tipo
  gravitón: **CONFIRMADO**, p.1.
- Dirigido: "la dispersión k³ es una consecuencia universal": **NO APOYADO**. p.1 dice que el
  estado ABL de gravitón "has a close cousin with a different dispersion". Sin lectura completa.

## Xu & Hořava, arXiv:1003.0009 (`biblioteca/arXiv-1003.0009.pdf`)

- Líquido de Bose en red con gravedad de Lifshitz emergente en el punto fijo z = 3, y relación con
  una fase z = 2: **CONFIRMADO**, p.1–2.

## Pretko, arXiv:1606.08857 = Phys. Rev. B 96, 035119 (2017) (`biblioteca/arXiv-1606.08857.pdf`)

- Referencia de revista: **CONFIRMADA** (página de arXiv, journal-ref).
- Teoría de carga vectorial sin traza (`∂_i E^{ij} = ρ^j`, `E^i_i = 0`), 2 polarizaciones,
  `ω ∝ k³`: **CONFIRMADO**, p.2 (§B) y tabla de p.3. La misma tabla da `ω ∝ k²` y 3
  polarizaciones a la teoría de carga vectorial sin la condición de traza.

## Po, Fidkowski, Vishwanath, Potter, arXiv:1701.01440 (`biblioteca/arXiv-1701.01440.pdf`)

- Existe y trata fases Floquet quirales "radicales" en 2D, cuyo borde realiza una traslación
  quiral que no se puede generar con un Hamiltoniano local cerca del borde: **CONFIRMADO**, p.1.
- Uso del dirigido ("todo `i log U` de un QCA es no local", aplicado a CJWW): **NO APOYADO**. El
  paper trata traslaciones quirales de borde en sistemas 2D, no walks 3D invariantes por
  traslación. La cuestión de F3 sigue abierta (no-go de Opus sin comprobar).

## `i(U − U†)/2` como densidad de energía en la literatura

- **NO APOYADO.** La cita del dirigido (ref. 60) es una tesis sobre cristales de tiempo. No se
  encontró fuente primaria. La propiedad `[K, U] = 0` y `K − H_eff = O(|p|³)` está verificada por
  `debates/2026-09-30--w9-w11-blind-review/verify_reviewer_claims.py`, no por la literatura.

## Barceló et al., arXiv:2108.06582 (`biblioteca/arXiv-2108.06582.pdf`)

- Contiene una sección sobre el teorema de Weinberg–Witten y la gravedad emergente: **CONFIRMADO**,
  p.22–23.
- Mecanismo de evasión: el informe abierto lo atribuye a la ruptura de la invariancia de Lorentz en
  el UV. **MATIZADO**: el argumento de p.23 se basa en el carácter emergente de las simetrías gauge
  ("The key aspect is the emergent nature of gauge symmetries"). Los autores dicen que su resultado
  es para la teoría lineal. Sin lectura completa.

## Deser, arXiv:gr-qc/0411023 (= Gen. Rel. Grav. 1 (1970) 9) (`biblioteca/arXiv-gr-qc_0411023.pdf`)

- Existe; es la reimpresión de 1970 de "Self-Interaction and Gauge Invariance": **CONFIRMADO**,
  p.1. El argumento del bootstrap no se ha releído aquí; la objeción de Opus (B2 de
  `reparaciones.md`) queda pendiente de derivación propia.

## C. Xu, arXiv:cond-mat/0602443 (`biblioteca/arXiv-cond-mat_0602443.pdf`)

- Fase de líquido de bosones algebraico con excitaciones de "gravitón blando" y dispersión
  `ω ∼ k²`: **CONFIRMADO**, p.1.

## Arrighi, Facchini, Forets, arXiv:1505.07023 (`biblioteca/arXiv-1505.07023.pdf`)

- Límite continuo de una clase de QWs que da Dirac con masa en espacio-tiempo curvo **(1+1)D**,
  como "toy model of a test particle": **CONFIRMADO**, p.1. Partícula de prueba, sin backreaction.
- El dirigido le atribuye (3+1)D y redes de panal y triangulares: **NO EN ESTE PAPER**. Puede ser
  otro trabajo del grupo (el abierto cita arXiv:1803.01015); sin comprobar.

## Pendiente (sin comprobar)

- Programa de Pavia (D'Ariano–Perinotti): que no tenga ningún modelo QCA con gravedad emergente
  es una afirmación negativa; no comprobada.
- Pretko, arXiv:1702.07613 (gravedad emergente de fractones): descargado, no leído.
- Arrighi et al., arXiv:1803.01015 y el resto del grupo Debbasch/Di Molfetta.
- Gupta (1954): sin fuente descargada.

## Balance para W8–W11

- Las atribuciones de W8–W10 a Gu–Wen y Pretko se sostienen en el original. W10 debe precisar que
  la acción de Einstein linealizada es del continuo (Gu–Wen p.12) y no del modelo L en red (k³).
- Ningún paper comprobado acopla un walk o QCA de materia a un sector de gravitón con
  backreaction: Arnault–Debbasch y Arrighi et al. usan fondos fijos, y Gu–Wen deja los fermiones
  para el futuro. Esto **no prueba** la novedad (la búsqueda no es exhaustiva), pero no hay
  contraejemplo entre las fuentes leídas.
- Antecedente nuevo que conviene citar en W11: Arnault–Cedzich (Noether en red en tiempo
  discreto).
