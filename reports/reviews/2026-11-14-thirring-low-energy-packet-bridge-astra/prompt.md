# Re-revisión acotada: puente paquete/dispersión del contrato 2 Thirring

Autorización: usuario «autorizado, te autorizo todos los pasos» (2026-11-14),
sobre la propuesta de re-revisar el puente antes de promocionar. Envío a
OpenAI (Astra), sin publicación ni promoción automática. Autor del informe
revisado: Claude (Opus 5.5), con reparaciones aplicadas tras la revisión de
Astra del 2026-11-09; revisor: Astra (OpenAI), otra familia respecto del
autor. Herramientas: ~/herramientas 2a7342b. Generación de la casa
comprobada el 2026-11-14 con `codex exec -m gpt-6-astra`. Texto revisado:
reports/2026-11-09--thirring-low-energy-packet.md en el commit actual
(918f7f4); revisión original: reports/reviews/2026-11-09-thirring-low-energy-packet-astra/.

Objetivo: decidir si el puente paquete/dispersión (Sec. 4) y las siete
reparaciones están correctamente cerrados. Resultado esperado: dictamen por
bloque. Máximo: una ronda. Cierre: PASS → el usuario ha autorizado
promocionar este resultado y el de la puerta de sabor (que reutiliza el
puente) en su alcance congelado; REPAIR_REQUIRED u OPEN en el puente → no
se promociona ninguno y la puerta de sabor vuelve a quedar condicionada.

---
Re-revisa adversarialmente el informe adjunto
2026-11-09--thirring-low-energy-packet.md (contrato 2 de la línea Thirring),
escrito por Claude (Anthropic). Ya lo revisaste una vez: se adjunta tu
informe original («reparación necesaria») y el texto actual lleva las siete
reparaciones aplicadas. Se adjuntan también el contrato, el verificador, su
salida y las fuentes 1711.03920 y 1804.08508. El veredicto negativo
(NO_ENTANGLER_IN_DECLARED_PACKET_CODE) no es el foco: el foco es el puente,
porque un resultado posterior lo reutiliza. No tienes herramientas: no
ejecutes, edites ni navegues. El recuento 39/39 no prueba pasos analíticos.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. AUTOFUNCIONES EXACTAS (Sec. 4(i)). ¿La derivación general por la
   condición de contacto vale en todo el soporte, no solo en los puntos
   certificados? ¿Es correcta T = (c + z b)/(b + z c) y |T| = 1 a chi = pi/2
   con denominador acotado lejos de cero?
2. SOLUCIÓN APROXIMADA EXACTA Y UNITARIEDAD (Sec. 4(ii)). ¿Está bien el
   factor 1/(2pi) restaurado, la normalización de espinores y la identidad
   ||U^T P B|ab> - psi~(T)|| = ||P B|ab> - psi~(0)||? ¿psi~(t) está en l^2?
3. ERROR INICIAL Y COLAS (Sec. 4(iii)-(v)). ¿Cierran uniformemente las
   cotas de cola con derivadas del espinor y de T y con el factor T no
   separable? ¿Es correcto el uso de |omega'| (signo de omega' para B) y la
   cota de velocidad 0.55?
4. VARIACIÓN DE FASE Y LÍMITE. ¿La variación O(mu^{1/2}) de T sobre el
   soporte y el paso al límite mu -> 0 en norma de operador están bien
   justificados? ¿Controla la separación 3mu frente a la anchura mu^{3/2}
   la cercanía al punto k = 0?
5. REPARACIONES. Para cada una de tus siete reparaciones originales: ¿está
   resuelta, resuelta parcialmente o no resuelta? Cita la frase.
6. ALCANCE. ¿Separa el informe lo escrito de lo certificado? ¿Se evita
   afirmar un no-go de Thirring?

Hasta 1800 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente.
---
