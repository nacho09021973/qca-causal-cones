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

## Pendiente (sin comprobar)

- Pretko: PRB 96, 035119 (traceless vector charge, 2 polarizaciones, k³) y arXiv:1702.07613
  (descargado en `biblioteca/`, no leído).
- Po, Fidkowski, Vishwanath, Potter (chiral Floquet): el dirigido lo usa para "no hay logaritmo
  local". Parece fuera de contexto: trata fases quirales 2D con bordes, no walks invariantes por
  traslación. Sin comprobar.
- Que `i(U − U†)/2` esté identificado en la literatura como densidad de energía: la cita (ref. 60)
  es una tesis sobre cristales de tiempo. Sin comprobar; tratar como no apoyado.
- Barceló et al., arXiv:2108.06582 (Weinberg–Witten y gravedad emergente), y Gupta/Deser.
- C. Xu 2006 (gravitones blandos), Arrighi–Facchini–Forets, programa de Pavia.
