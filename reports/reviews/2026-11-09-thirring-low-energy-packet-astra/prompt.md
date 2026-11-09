# Revisión externa: puerta de paquetes de baja energía Thirring (contrato 2 de 2)

Autorización: usuario «bueno mejor codex que es de otra familia» (2026-11-09).
Autor del informe: Claude (Opus 5.5); contrato redactado por Codex.
Revisor: GPT-6 Astra (OpenAI), otra familia respecto al autor del informe,
mediante revision-ciega astra del PATH. Herramientas: ~/herramientas commit
97292a9. Resultado revisado: commit b4ac949 (contrato 715096f, verificador
8b41761). Máximo: una ronda sustantiva. No se autoriza investigación nueva
ni promoción. Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente el informe adjunto, que concluye
NO_ENTANGLER_IN_DECLARED_PACKET_CODE para el código de paquetes congelado en
el contrato adjunto: lim ||E_mu|ab>||^2 = |T_ab - 1|^2/4 (1/3, ~0.403, 4/9)
cuando mu -> 0. Tu objetivo es encontrar un error, un supuesto oculto o un
hueco real, o explicar por qué se sostiene. No aceptes el recuento 39/39 ni
el diagnóstico numérico como prueba del enunciado asintótico.

Comprueba desde las definiciones y las fuentes adjuntas:
(1) admisión: normalización, isometría, banda positiva, sentido de
    movimiento con la convención |q> = sum e^{-iqx}|x>, Q_D B = 0 y
    Q_D B_out = 0;
(2) estructura: Gamma W Gamma = -W, que el contacto sólo ocurre en
    Gamma1 Gamma2 = -1, que U(1-P) = F(1-P) exactamente, y que
    <B, Gamma1 Gamma2 B> = 0 con ||P B||^2 = 1/2;
(3) la autofunción de cuatro ondas planas (fase en RL en y=0, extensión
    antisimétrica, fórmula de T) y su certificación en dos puntos algebraicos;
    si dos puntos más la estructura bastan para todo el soporte;
(4) el puente: solución aproximada exacta psi~(t), unitaridad, error inicial
    por colas, posición de las partes entrante/saliente en t = T, cotas de
    colas con dispersión, variación de T sobre el soporte; exponentes
    O(mu^{3/4}) y O(mu^{1/2}); constantes y uniformidad sobre las entradas;
(5) el ensamblaje: K -> diag((1+T)/2), fuga y contenido doblador
    -> |T-1|^2/4; límite de T en forma de rapideces y valores exactos;
(6) si el veredicto corresponde a las reglas del contrato (condición
    necesaria refutada) y si el balance de cierre se excede;
(7) correspondencia del script exacto y del diagnóstico con lo que el informe
    dice, y el tratamiento de la ejecución fallida.

Se adjuntan contrato, informe, script exacto, su registro, script y registro
del diagnóstico, y los PDF 1804.08508 y 1711.03920 en texto extraído (las
fórmulas pueden llegar deformadas; el PDF manda). No tienes acceso al
repositorio ni puedes ejecutar código. Distingue lo que derivas a mano de lo
que sólo inspeccionas.

Entrega en español: veredicto (se sostiene / reparación necesaria /
refutado / no decidido), derivaciones críticas, objeciones ordenadas por
gravedad con sección y reparación concreta, y el alcance exacto que
aceptarías. Si no hay fallos, dilo sin inventar objeciones. Ninguna propuesta
de protocolo o búsqueda adicional es necesaria.
---
