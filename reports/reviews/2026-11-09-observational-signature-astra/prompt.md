# Revisión externa: firma observacional de la saturación

Autorización: usuario «si, a codex» (2026-11-09). Autor del contrato y del
informe: Claude (Opus 5.5). Revisor: GPT-6 Astra (OpenAI), otra familia,
mediante revision-ciega astra del PATH. Herramientas: ~/herramientas commit
97292a9. Resultado revisado: commit f9a638e (contrato 21af1dd, verificador
658845a). Máximo: una ronda sustantiva. No se autoriza investigación nueva
ni promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente el informe adjunto. Afirmaciones centrales: (a) en las
filas techo L2 y L3, V_grp^max = c_0 exactamente (forma producto
cos omega = prod cos p_j y cota multilineal); (b) en L5a, L5b, L4, L6a, L6b y
L3s4 existen excitaciones con velocidad de grupo mayor que c_0 (signo exacto
de beta en rayos declarados más puntos certificados por intervalos);
(c) Hg refutada por L2, Hh refutada por L3s4; (d) veredicto de ruta
DISCRIMINATING_SIGNATURE_IN_DECLARED_ROWS, parcial; (e) la conclusión de la
sec. 5 (estar en el techo isótropo y ser insuperable son independientes en
esta clase). Tu objetivo es encontrar errores, supuestos ocultos o huecos,
o explicar por qué se sostiene. No aceptes el recuento 19/19 como prueba.

Comprueba desde las definiciones:
(1) la reducción de L2/L3 a omega = arccos(prod cos p_j), la fórmula de
    |grad omega|^2, la cota multilineal y su verificación en vértices, y
    c_0 = 1/L;
(2) el paso de beta(n)>0 a |grad eps| > c_0 cerca del nodo (rama analítica a
    lo largo del rayo, derivada radial como cota inferior), incluido L3s4
    con a simbólica;
(3) la fórmula de las dos velocidades de grupo de un bloque unitario 2x2 a
    partir de |Tr U|^2 y del argumento del determinante, y que ambas ramas
    son las del nodo sin masa; la corrección de la aritmética de intervalos
    (constantes, redondeo, comprobación de no cruce);
(4) la lectura de las firmas desde la tabla padre (orden, signo, isotropía)
    y la refutación de Hh por L3s4;
(5) si el veredicto de ruta y la sec. 5 se exceden respecto a lo probado
    (filas sin testigo ≠ V_grp^max = c_0; validez cerca del nodo);
(6) el defecto de contrato declarado y si la desviación a intervalos es
    aceptable;
(7) correspondencia del script con lo que el informe dice.

Se adjuntan contrato, informe, script, registro, el informe padre de
correcciones de dispersión y THREE_VELOCITIES.md. No tienes acceso al
repositorio ni puedes ejecutar código. Distingue lo que derivas a mano de lo
que sólo inspeccionas.

Entrega en español: veredicto (se sostiene / reparación necesaria /
refutado / no decidido), derivaciones críticas, objeciones ordenadas por
gravedad con sección y reparación concreta, y el alcance exacto que
aceptarías. Si no hay fallos, dilo sin inventar objeciones. Ninguna propuesta
de protocolo o búsqueda adicional es necesaria.
---
