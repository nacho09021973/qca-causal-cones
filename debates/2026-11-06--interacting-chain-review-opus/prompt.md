# Revisión autorizada por el usuario

Herramienta canónica revision-ciega, herramientas ce09890. Autor Codex;
revisor Claude, otra familia. Estado del trabajo sin commit, hashes del
snapshot registrados por el lanzador. Usuario: «adelante que la haga claude».

---
Revisa adversarialmente la cadena interactuante adjunta. No conoces otros
veredictos. No tienes herramientas; no afirmes ejecutar código o consultar
fuentes externas. Los PDF adjuntos son fuentes primarias extraídas a texto.

Objetivo: decidir qué resultados de esta cadena son correctos bajo sus
hipótesis y qué reparaciones son obligatorias antes de seguir investigando.
Todos son PRELIMINARY. No se solicita promocionar ni fusionar con main.
Máximo una ronda de revisión completa en este encargo. Cierra al entregar
un informe autocontenido con veredictos y objeciones trazables; no inicies
otra investigación ni una conversación con el autor.

Examina seis bloques:
1. Colisión de densidades: sector vacío/una partícula, estado ocupado
   estacionario y respuesta de primer orden, signos y convenciones.
2. Segundo orden: reducción de fuerza a u_a D_b, traspuestas y orden de
   matrices, posibles términos omitidos, recurrencia de memoria, mallas
   sin alias y las cotas Abel/derivadas. Los controles del propio código
   no prueban la fórmula: rederívala independientemente.
3. Circuito Wilson/Strang: localidad, homogeneidad realmente disponible,
   ground state finito, gaps y cotas de error; límites y alcance.
4. Flujo Yukawa: coeficientes desde fuentes, extensión dos sabores,
   acoplamientos iguales sobre línea de referencia y su estabilidad al
   perturbar velocidades, eigenmodos, potencias, flujo lambda/y² y
   validez de la afirmación de atracción efectiva.
5. Ajuste crítico y corte: tadpole/curvatura y signos/factores,
   operadores relevantes faltantes, prescripción de truncación,
   condiciones de momentos y secuencia diagonal de errores.
6. Cadena global: ¿hay saltos lógicos o afirmaciones demasiado fuertes
   incluso con las reservas escritas? Identifica qué premisas pueden
   usarse, cuáles deben retirarse y qué cálculo siguiente es justificable.

Por bloque: PASS / REPAIR_REQUIRED / FAIL / INSUFFICIENT_EVIDENCE.
Cada objeción indica archivo/sección, gravedad, razonamiento o
contraejemplo y reparación mínima. Distingue error demostrado de duda
o falta de prueba. Examina errores aunque la conclusión final diga OPEN:
una reserva no valida una fórmula equivocada. No confundir resolver ODE
truncadas con probar RG exacto o un QCA microscópico.

Salida esperada: resumen de veredictos, objeciones numeradas, derivaciones
decisivas, conclusión sobre alcance y prioridad de reparaciones. Si el
paquete no permite decidir algo, dilo con precisión. No inventes pruebas,
ejecuciones, citas ni consenso. No reescribas los documentos del autor.
---
