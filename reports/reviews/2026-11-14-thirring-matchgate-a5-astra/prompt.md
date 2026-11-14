# Revisión sellada: gate A5 de matchgates (cruces Thirring)

Autorización: usuario «commit, push y revicion independiente» (2026-11-14).
Envío a OpenAI (Astra), sin publicación ni promoción automática. Autor:
Claude (Opus 5.5); revisor: Astra (OpenAI), otra familia. Herramientas:
~/herramientas 2a7342b. Generación de la casa comprobada el 2026-11-14 con
`codex exec -m gpt-6-astra`. Texto revisado:
reports/2026-11-14--thirring-matchgate-a5.md en `3fa82c8`; contrato
congelado en `915e55f`; verificador subido antes de ejecutar en `eae7876`.

Objetivo: decidir si el veredicto MATCHGATE_SIMULABLE_UNDER_F está bien
fundado bajo la premisa F y bien acotado. Resultado esperado: dictamen por
bloque. Máximo: una ronda. Cierre: PASS → listo para que el usuario decida
si promociona (no autorizado por este encargo); otro dictamen →
reparaciones y nueva decisión del usuario.

---
Revisa adversarialmente el informe adjunto
2026-11-14--thirring-matchgate-a5.md, escrito por Claude (Anthropic). Se
adjuntan el contrato congelado THIRRING_MATCHGATE_A5_GATE.md, el
verificador y su salida (26/26), el informe co-móvil que fija la familia
V(r) y la convención de signo de alpha, el verificador co-móvil que el
nuevo importa, y tres fuentes primarias en texto extraído: Valiant (STOC
2001), Terhal-DiVincenzo (quant-ph/0108010v2) y Jozsa-Miyake
(0804.4050v2). F (factorización multipaquete) es una premisa declarada por
decisión del usuario: no la ataques como tal, pero sí si el informe la usa
de forma distinta a como el contrato la declara. No tienes herramientas:
no ejecutes, edites ni navegues. El recuento 26/26 no prueba pasos
escritos.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. FORMALIZACIÓN DE F (Sec. 2). ¿Es el operador par W_ab una lectura fiel
   de F tal como la declara el contrato y del resultado de dos paquetes
   promocionado (orden de creación, primer factor = paquete en la
   coordenada mayor, marco B_out)? ¿Introduce supuestos adicionales?
2. SIGNO FERMIÓNICO (Sec. 3, S1-S3). ¿Es correcto que el cruce actúa en
   el registro ordenado por posición como -P v en slots adyacentes, con
   signo -1 común a los cuatro estados de base e independiente de los
   espectadores? ¿Implementa el modelo de Fock con Jordan-Wigner del
   verificador lo que dice (signos, orden de operadores, cadena de
   creación)? ¿Es v genérico suficiente?
3. ADYACENCIA Y COINCIDENCIAS (Sec. 3). ¿Es correcto el argumento de
   continuidad? ¿Está bien tratada la coincidencia triple (S4) y es
   correcto que para k >= 4 la unicidad no hace falta para la
   simulabilidad?
4. CLASE DE PUERTA (Sec. 4, M1-M4). ¿Es G = -P V(r) = G(A, B) con A, B en
   SU(2) para todo r > 0 con el signo del repositorio? ¿Se aplican bien las
   cinco identidades de Valiant (p. 118) y la Proposición 3, incluida la
   correspondencia entre la matriz carácter y la matriz de la puerta en
   la base computacional (y la lectura complementada que Valiant llama
   inesencial)? ¿Es correcta la segunda vía exp(+i theta/2 (XX+YY)) y el
   paso de Jordan-Wigner?
5. HIPÓTESIS DE LOS TEOREMAS (Sec. 5). Contrasta cada fila de la tabla con
   el texto de las fuentes adjuntas y sus páginas. ¿Está bien dicha la
   noción de simulación obtenida (marginales de subconjuntos, muestreo,
   <Z_k>, precisión)? ¿Es legítima la inferencia a P de Jozsa-Miyake p. 3?
   ¿Falta alguna hipótesis (por ejemplo uniformidad, tamaño, cálculo de
   los parámetros r_pq)?
6. ALCANCE (Secs. 1, 6-8). ¿Separa lo escrito de lo certificado? ¿Evita
   afirmar F, un no-go de Thirring o algo sobre chi != pi/2 u otros
   recursos?

Hasta 1800 palabras en español. Cada reparación obligatoria debe citar la
frase afectada, por qué falla y qué la cerraría. Distingue aclaración de
error. Dictamen global y lista de reparaciones obligatorias; si no hay
ninguna, dilo expresamente.
---
