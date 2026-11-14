# Revisión externa: puerta de intercambio en el código de sabor Thirring

Autorización: usuario «AUTORIZO LA REVISIÓN CON GROK» (2026-11-14); autoriza
el envío a xAI, no publicación ni promoción. Autor del texto: Claude (Opus
5.5); revisor: Grok (xAI), otra familia, mediante revision-ciega grok del
PATH. Herramientas: ~/herramientas 2a7342b. Resultado revisado: commit
24b78e9 (contrato d0c59cb, verificador 8d7e444).

Objetivo: decidir si el veredicto FLAVOUR_PACKET_EXCHANGE_GATE_IN_DECLARED_CODE
se sostiene, en especial el puente paquete/dispersión adaptado al sector
(+,-). Resultado esperado: dictamen por bloque PASS / REPAIR_REQUIRED / OPEN.
Máximo: una ronda. Cierre: PASS → registrar la revisión, sin promoción
automática; REPAIR_REQUIRED → reparar y decidir el usuario si hay re-revisión;
una objeción que invalide la Sec. 2 o la Sec. 4 → el veredicto vuelve a
OPEN_AFTER_BOUNDED_EXACT_ATTEMPT o al que corresponda.

---
Revisa adversarialmente el informe adjunto 2026-11-14--thirring-flavour-packet.md
(escrito por Claude, Anthropic), su contrato congelado y su verificador.
Se adjuntan como contexto el informe del contrato 2 (cuyo puente
paquete/dispersión se reutiliza; fue reparado tras una revisión de otra
familia y no re-revisado), el verificador del contrato 2 que se importa, y
la fuente primaria 1711.03920. Tu objetivo es encontrar un error, un
supuesto oculto o un hueco real, o explicar por qué el argumento se
sostiene. El recuento de comprobaciones del script no prueba los pasos
analíticos; distingue lo certificado de lo escrito.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. CÓDIGO (Sec. 2). Con Gamma = sigma_z (-1)^x y las convenciones de W,
   ¿son ortonormales las columnas sqrt2 Pi_f phi? ¿Es correcto que AA y BB
   tienen G = +1 y evolucionan exactamente libres (U(1-P) = F(1-P))?
   ¿Son correctas AB = P(phi_r^phi_l) - P(phi_r^Gamma phi_l) y
   BA = P(phi_r^phi_l) + P(phi_r^Gamma phi_l), y la asignación del segundo
   vector al sector (+,-) con momento total desplazado en pi?
2. ADMISIÓN BAJO U^2 (Sec. 3). ¿W Pi_A phi = Pi_B W phi y W^2 Pi_f phi =
   Pi_f W^2 phi? ¿Comparten trayectoria y velocidad de grupo las dos
   componentes? (La decisión de admitir estos portadores bajo U^2 es del
   usuario; no la juzgues, juzga solo la matemática.)
3. SECTOR (+,+) (Sec. 4). ¿Es legítimo reutilizar el resultado del contrato
   2 para P(phi_r^phi_l) con estos paquetes (k = 1 a la derecha, k = 2 a la
   izquierda)? ¿Coincide la orientación de T_+ (partícula 1 = paquete
   derecho)?
4. SECTOR (+,-) (Sec. 4, puntos 1-5). Es el bloque crítico. ¿La derivación
   general de T por la condición de contacto se aplica con v+ (x) v-? ¿Es
   correcta T_- = (a_r - z a_l)/(z a_r - a_l) usando g_-(q+pi) = -g_+(q) y
   el orden de partículas del Ec.(12) inferior? ¿Transfieren realmente las
   cotas de cola, separación y velocidad del contrato 2 (Gamma actúa en el
   sitio)? ¿Controla la separación 3mu frente a la anchura mu^{3/2} la
   aproximación al punto degenerado q_l = q_r? ¿Falta algún término?
5. MAPA LÓGICO (Sec. 5). ¿Es V = 1 (+) [[al, be], [be, al]] (+) 1 con
   al = (T_+ + T_-)/2, be = (T_+ - T_-)/2, unitario, sin fuga en el
   límite? ¿Es correcta la fórmula T_+ - T_- = 2 a1 a2 (z^2 - 1)/(...), y
   los valores x = (sqrt10 - 2)/6, concurrencia 2xy?
6. ALCANCE Y VERIFICADOR (Secs. 6-7). ¿Dice el informe lo que el
   verificador no certifica? ¿Codifica F3 fielmente el álgebra (modelo
   finito de cuatro estados)? ¿El reemplazo del punto de prueba tras la
   ejecución 2 está justificado y documentado? ¿Se evita afirmar
   universalidad, componibilidad o un límite QFT?

Hasta 1800 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente. No exijas resultados nuevos fuera del contrato.
---
