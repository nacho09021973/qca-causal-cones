# Revisión externa: exclusión de la recuperación aproximada Thirring

Autorización: usuario «la revision que la haga Grok» (2026-11-09). Autor del
texto: Claude (Opus 5.5); revisor: Grok (xAI), otra familia, mediante
revision-ciega grok del PATH. Herramientas: ~/herramientas commit 97292a9.
Resultado revisado: commit ad01e20 (contrato 61a8215, verificador f5c0d16).
Máximo: una ronda sustantiva. No se autoriza investigación nueva ni promoción.
Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la demostración adjunta de que, para el código
microscópico Thirring M=1 declarado (U=FJ, mu=3/5, nu=4/5, z=i, salida libre
B_T=F^T B), liminf_{T->inf} ||E_T|00>||^2 >= c > 0, y por tanto no hay
recuperación aproximada en el sentido del contrato. Tu objetivo es encontrar
un error, un supuesto oculto o un hueco real, o explicar por qué el
argumento se sostiene. No aceptes el recuento de comprobaciones del script
como prueba de los pasos analíticos.

Comprueba desde las definiciones:
(1) descomposición en fibras: convención w=x1+x2, y=x1-x2, paridad, medida
    (1/pi)dp sobre (-pi/2,pi/2], y que U y F actúan fibra a fibra;
(2) que el vector de la Ec.(14) de 1711.03920 (caso "+", p=pi/4) es vector
    propio de U(p) con autovalor i, con el orden U=FJ y las convenciones de W;
    revisa si la comprobación del script en w en {0,1} basta con la
    covariancia por traslación diagonal;
(3) el aislamiento: reducción de exp(-i(s w(p+k)+r w(p-k)))=i a
    nu^2(1+cos2p cos2k)=1 en los cuatro casos de signo, y que el espectro
    esencial de U(p) coincide con el de W_2(p) (perturbación de rango finito);
(4) continuidad en norma de U(p), proyección de Riesz de rango constante y
    positividad de c a partir del peso 16/25 en p0;
(5) espectro absolutamente continuo de W_2(p) en un entorno de pi/4,
    Riemann-Lebesgue y convergencia dominada, incluida la medibilidad y el
    caso de autovalores que se cruzan;
(6) la desigualdad final ||E_T|00>||^2 >= c - o(1) y que excluye toda
    subsucesión y toda matriz V;
(7) correspondencia del script con lo que el informe dice que certifica,
    y el tratamiento de la ejecución fallida;
(8) si el alcance declarado (solo este código, regla y parámetros; c sin valor
    numérico; entrada 11 sin decidir) es correcto o se excede.

Se adjuntan: contrato, informe, script, registro de la ejecución correcta,
el informe previo de recuperación exacta (contexto de definiciones del
código; es texto de otro autor, no fuente independiente) y el PDF de
1711.03920 en texto extraído (las fórmulas pueden llegar deformadas; el PDF
manda). No tienes acceso al repositorio ni puedes ejecutar código. Distingue
lo que derivas a mano de lo que solo inspeccionas.

Entrega en español: veredicto (se sostiene / reparación necesaria /
refutado / no decidido), derivaciones críticas, objeciones ordenadas por
gravedad con sección y reparación concreta, y el alcance exacto que
aceptarías. Si no hay fallos, dilo sin inventar objeciones. Ninguna
propuesta de protocolo o búsqueda adicional es necesaria.
---
