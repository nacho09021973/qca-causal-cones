# Revisión independiente adversarial de T1: dos canales y P/Q inclinado

Fecha: 2026-09-24. Autor de T1: Codex (familia OpenAI).
Encargo del usuario: T1 → revisión independiente → T2 → T3.
Esta sesión ejecuta únicamente la revisión de T1.

## Pregunta y límite

¿Es exacta y bien definida la descomposición firmada de T1 para el
contrato TWO_DISTINGUISHABLE_CHANNELS y el P/Q auxiliar ya existente?
Intentad refutarla mediante un error de dominio, peso, adjunto, fuente,
referencia física, recurrencia o caso límite. No basta aprobar la
expansión elemental de una forma cuadrática: revisad su lift inclinado.

Revisores solicitados: Claude Opus (Anthropic) y Gemini (Google), ambos
distintos de la familia autora. Esto es una revisión externa al autor
por agentes, no una revisión humana. El protocolo es deliberativo:
los turnos posteriores ven los anteriores; no se afirmará que sean dos
evaluaciones ciegas. No se convoca un comité ni se delegan decisiones.

El estado declarado en la cabecera de T1 NO es evidencia. Los informes
previos proporcionan definiciones y notación; sus cotas preliminares
no son premisas probadas. Rehaced las identidades algebraicas a partir
de esas definiciones. No hace falta literatura externa ni novedad.

## Criterios que deben puntuarse separadamente

1. (1)–(2), (9)–(10a): referencia real r=U_N^N J phi_N, encoder completo,
   ambos bits, cinco piezas por canal y signos/adjuntos de los cruces.
2. (3): P=diag(p_S,I-p_S) dentro de W, P=0 fuera, Q=I-P.
   Compatibilidad con D=S⊕S^-1 y el P/Q previo, sin ortogonalidad ficticia
   ni identificación con los canales o con el corte IR.
3. (4)–(7): conjugación exponencial sobre la fuente compacta f,
   extensión del operador inclinado, convención Fourier y signo del
   desplazamiento p-i xi; recuperación exacta del factor e^(-K_* N).
   Buscar cualquier aplicación ilegítima del peso no acotado a phi_N/r.
4. (8), (12), (15): reconstrucción en Bob de cada sector y adjuntos
   P* H_c Q. ¿Es suficiente la restricción finita a Bob sin exigir que
   cada sector desinclinado sea globalmente l2? ¿Falta alguna hipótesis?
5. (13)–(16): índices temporales, productos vacíos, fuente inicial Q,
   memoria y salida Q; distinguir salida P de trayectoria siempre P.
6. Controles: rederivación por diferencia de estados, moneda nula,
   encoder identidad, POVM completo. Intentar al menos un control propio.
7. Techo: ¿se introduce subrepticiamente alguna afirmación de escala,
   cancelación, transferencia de cotas, H1/H1c o realización física?

Para cada objeción, indicar ecuación, derivación o contraejemplo y qué
reparación la resolvería. Distinguir FATAL, REQUIRED_REPAIR y OPTIONAL.
Si no hay objeción matemática, decirlo sin inventar una para disentir.

Veredicto final explícito: T1_PASS, T1_REPAIR_REQUIRED o T1_OPEN.
Enumerar reparaciones obligatorias, si las hay. T1_PASS sólo acepta la
identidad exacta en su contrato, no las cotas de los prechecks.
No ejecutar T2, no mapear N^-6, no buscar cancelaciones de T3, no cambiar
P/Q, perfiles o detectores y no proponer un frente intermedio.

## Snapshot y procedencia

Repositorio base: d8ca7b285129b8b29a304e232195e29f20095526.
T1 es un archivo de trabajo todavía no incluido en commit; se congela
por SHA256 y por su copia íntegra en el acta de sanedrin:

| Archivo adjunto | SHA256 |
| --- | --- |
| reports/2026-09-24--two-channel-t1-exact-signed-pq.md | 4c3eec6e4d60090695e2f9f5db431c196a9cc6e3d1371f9a7d4005c583b11644 |
| reports/2026-09-24--h1c-return-kernel-schur-audit.md | ac92cb8c10fa49a94dd36387846e38ce3a8885bfbdc2b0c8001e407f046e4e9b |
| reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md | ab06bb4136a4a96565670bc87d66eb6c8b13679abc7f9f3db31cfbe0b58dee9d |
| papers/ir-corona/ir-corona.tex | 05a2eb09d2f103608683978c292de939511359677727982de441970f2e655636 |

Se adjunta el TeX completo para las definiciones originales: convención
Fourier y símbolo (§2.1), protocolo (§3), representación inclinada (§7.3).
Sus teoremas asintóticos y sus afirmaciones de certificación no son
objeto de esta revisión ni premisas necesarias para el álgebra de T1.

Herramienta: /home/ignac/sanedrin, commit
8162508e3bd0e3d05770b4dd544fe7c962d0272c.
Herramientas compartidas: /home/ignac/herramientas, commit 18028a9.
Diagnóstico de esta sesión: opus, abner y gemini disponibles; astra
disponible con cuota sin verificar; ciro ausente por autenticación.
Sólo se solicitan opus y gemini; la ausencia de ciro no es un voto.

Una ronda adversarial, residuos individuales y veredicto del protocolo;
máximo 1600 palabras por turno, timeout 900 s, un reintento transitorio.
Si falla algún turno solicitado, se conserva el diagnóstico operativo:
una ejecución incompleta no se presentará como consenso.
