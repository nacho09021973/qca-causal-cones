# Revisión independiente de la reducción escalar hexagonal

---
Revisa adversarialmente el informe adjunto «Scalar method beyond S19».
Su autor es Codex (OpenAI). El usuario ha pedido expresamente que esta
revisión la haga Claude. No se solicita resolver la factibilidad escalar,
probar no saturación universal, buscar literatura ni extender soportes.

Objetivo: determinar si las secciones 2 y 3 son demostraciones correctas
con los cuantificadores y la normalización indicados. Resultado esperado:
PASS / REPAIR_REQUIRED / FAIL por cada bloque y un dictamen global:

1. Del coseno normal en tres direcciones a D^2 f(0)=-r^2 I.
2. Fórmula de proyección para cualquier v=a*g1+b*g2, grid delta,
   grado entero N y argumento de los 2N ceros que anula la derivada
   transversal sin introducir reflexiones ilícitas.
3. Familia alineada v=m*g1: interpolante f_m^0 y disponibilidad de D6.
4. Divisibilidad por Delta: factores dobles en el anillo de Laurent,
   multiplicidades derivadas de reflexiones, realidad y simetría del
   cociente h, y suficiencia para interpolación (no para acotación).
5. Polígonos de Newton: si d=f-f_m^0 tiene soporte en H_m y Delta tiene
   polígono H_2, ¿se sigue rigurosamente supp(h) dentro de H_(m-2)?
   Revisa m=1, m=2, d=0 y la posibilidad de cancelaciones.
6. Alcance del verificador y del resultado: identidades verificadas no
   equivalen al teorema general; la reducción alineada no cubre por sí
   sola todas las orientaciones; un candidato escalar no es un walk.

Re-deriva los pasos, no uses el texto de Codex como fuente de autoridad.
Identifica cualquier hipótesis ausente, ambigüedad de escala o brecha.
Si objetas, da una derivación o contraejemplo concreto. Distingue cambios
obligatorios de sugerencias opcionales. No atribuyas ejecución de código:
esta sesión está sellada, sin herramientas ni búsqueda. Se adjuntan el
script, su salida local y el contrato para delimitar las pretensiones.
La prueba S19 adjunta es contexto para la especialización m=2; no heredes
ningún PASS previo ni necesitas revisar el antiguo certificado matricial.

Máximo: una ronda inicial y, solo si procede, una revisión adicional
acotada de las reparaciones. Cierre: informe completo sin objeciones
obligatorias pendientes, o identificación explícita de fallo/obligación
abierta. Una falta de entrega operativa no es revisión ni rechazo
matemático. No se promociona ningún resultado por este encargo.
---

Autorización: usuario «que lo haga codex», corregido inmediatamente por
«perdon claude», tras la propuesta de revisar primero la reducción general.
Herramienta: revision-ciega del PATH; herramientas
ce09890a0d5f68a6634f358eff2e477ac5f15ec7.
