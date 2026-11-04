# Lectura del autor de la revisión de gpt-6.1-sol de la traza G1

Autor: Claude (Anthropic). Objeto: `reports/2026-11-04--substrate-saturation-phase0-G1-trace.md`
en `cb814b5`. Revisor: `gpt-6.1-sol` (OpenAI, `codex exec`), COMPLETED,
2026-11-04. **REPAIR_REQUIRED**, dos reparaciones obligatorias. Puntos 1
(lemas), 2 (filas resueltas), 4 (G1-a, G1-b) y 5 (alcance) PASS; punto 3
(L6e) REPAIR_REQUIRED.

## Reparaciones obligatorias: comprobadas por el autor, ambas correctas

1. **L6e, resumen (l. 232).** Dice «two sign patterns vanish». El cuerpo
   de la traza dice que se anulan individualmente los cuatro patrones con
   `s_2 ≠ s_3` (dos en los vértices `±(2,−2)` y dos en `0`). El resumen
   contradice al cuerpo: son cuatro.
2. **F2 como condición necesaria (Sec. 0, l. 31).** La traza repite la
   formulación de F2 de la auditoría («presupposes every sign pattern has
   nonzero amplitude»). El propio Lema V da la condición exacta:
   `conv F = Z` sii todos los vértices de `Z` están en `F`. Contraejemplo
   del revisor, rehecho a mano: dos factores idénticos
   `P_+ T(a) + P_- T(−a)` dan `P_+ T(2a) + P_- T(−2a)` (los patrones mixtos
   son nulos porque `P_+ P_- = 0`); soporte `{±2a}`, envolvente
   `[−2a, 2a] = Z`. La condición «todos los patrones no nulos» es
   suficiente, no necesaria. La misma formulación excesiva está en la
   auditoría (F2, l. 177), en CURRENT_STATE Sec. 15 (l. 2582) y en el plan
   del día (l. 39). El diagnóstico de L6e no cambia: allí faltan vértices.

## Aclaraciones (no obligatorias)

- L6e y L6c: decir que el signo `+` designa la componente R (que se
  desplaza por `+N_j`); con `b` = desplazamiento de L, los `a_j` de L6c
  llevan el signo contrario. Los generadores reducidos, definidos salvo
  signo, no cambian.
- L6c/L6f: el fallo de la cláusula `±a` es de la presentación impresa; no
  prueba que no exista otra factorización. (La traza no afirma lo
  contrario.)
- CJWW (5.12): la cita de la revisión de gpt-6.1-sol sobre las amplitudes
  es innecesaria; basta el jump set afirmado.

No aplicadas: corregir la traza, y decidir si se anota también la F2 de la
auditoría y la Sec. 15, son decisiones del usuario.

Búsqueda de secretos en la carpeta: sin coincidencias.
