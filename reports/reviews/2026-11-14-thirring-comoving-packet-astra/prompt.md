# Revisión sellada: puerta de paquetes co-móviles Thirring

Autorización: usuario «autorizado para enviar a Astra» (2026-11-14). Envío
a OpenAI (Astra), sin publicación ni promoción automática. Autor del informe
revisado: Claude (Opus 5.5); revisor: Astra (OpenAI), otra familia.
Herramientas: ~/herramientas 2a7342b. Generación de la casa comprobada el
2026-11-14 con `codex exec -m gpt-6-astra`. Texto revisado:
reports/2026-11-14--thirring-comoving-packet.md en `e81a719`; contrato
congelado en `dca5ebc`; verificador subido antes de ejecutar en `2685635`.

Objetivo: decidir si el veredicto COMOVING_PACKET_GATE_SAME_FAMILY, la
Parte A y la lectura de A5 están bien fundados y bien acotados. Resultado
esperado: dictamen por bloque. Máximo: una ronda. Cierre: PASS → el
resultado queda listo para que el usuario decida si promociona (no
autorizado por este encargo); REPAIR_REQUIRED u OPEN → reparaciones y
nueva decisión del usuario.

---
Revisa adversarialmente el informe adjunto
2026-11-14--thirring-comoving-packet.md, escrito por Claude (Anthropic).
Se adjuntan el contrato congelado THIRRING_COMOVING_PACKET_GATE.md, el
verificador nuevo y su salida (52/52), los dos informes previos cuyo puente
reutiliza (contrato 2 de paquetes de baja energía, ya re-revisado con PASS;
puerta de sabor, revisada con PASS), los dos verificadores previos que el
nuevo importa sin modificarlos, y la fuente 1711.03920. No tienes
herramientas: no ejecutes, edites ni navegues. El recuento 52/52 no prueba
pasos analíticos; el informe dice qué es escrito y qué certificado.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. GEOMETRÍA CO-MÓVIL DEL PUENTE (Sec. 3 (ii)-(iv)). Con los dos paquetes
   moviéndose hacia x negativo, ¿es correcta la identificación de la onda
   entrante (momento rápido en la coordenada mayor sobre y >= 0)? ¿Bastan
   las cotas racionales de velocidad (omega'^2 >= 87/100 rápido,
   <= 16/25 lento, diferencia >= 13/100) y T = 20L para que ambos términos
   queden a distancia >= 3L/5 del lado erróneo? ¿Sigue valiendo la cota de
   colas del contrato 2 con t hasta 20L (constante cinco veces mayor) y
   desviación 3L/10, dando error O(mu^{3/4})?
2. AUTOFUNCIONES Y DEGENERACIONES (Sec. 3 (i), (v)). ¿El argumento general
   de contacto, en los sectores (+,+) y (+,-), vale para momentos del mismo
   signo en todo el soporte? ¿Está bien controlada la distancia a q1 = q2 y
   a las soluciones degeneradas del Lema 1? ¿Son E1 y E2 ejemplos válidos?
   ¿Siguen acotados lejos de cero los denominadores escalados de T_+ y T_-?
3. ORDEN, r_co Y ENSAMBLAJE (Secs. 1, 3 (vi), 4). ¿Fija el orden de
   creación r_co = a(3)/a(1) y no 1/r_co, sin elección a posteriori? ¿Son
   correctos los valores beta = (3 + 2 sqrt5)/11 y
   alpha = i sqrt(92 - 12 sqrt5)/11, y la ausencia de fase global extra?
   ¿Es coherente la lectura r = e^{theta_1 - theta_2} con el caso de
   sentidos opuestos?
4. PARTE A (A1-A4). ¿Certifican las comprobaciones lo que dicen (Delta =
   cos chi independiente de r; Yang-Baxter en forma R en las 64 entradas;
   relación de trenzas para P V)? ¿Está bien dicho lo que la Parte A no
   prueba (factorización física de tres paquetes; estructura graduada)?
5. A5 Y SU LECTURA. ¿Es correcto que, en una línea de paquetes, la puerta
   en orden de posición sea P V? ¿Están bien calculados los determinantes?
   ¿Está la consecuencia de simulabilidad (matchgates) marcada y acotada
   como no verificada, sin presentarse como veredicto? Si conoces una
   razón concreta por la que la condición de determinantes no implique
   aquí simulabilidad (por ejemplo, la traducción de qubits de sabor
   fermiónicos), dila.
6. ALCANCE. ¿Separa el informe lo escrito de lo certificado? ¿Evita
   afirmar factorización, universalidad o un no-go?

Hasta 1800 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente.
---
