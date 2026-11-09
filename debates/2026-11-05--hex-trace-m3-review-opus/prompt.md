# Revisión sellada: certificado escalar m=3

---
Revisa adversarialmente el nuevo resultado «m=3: exact scalar
incompatibility on the aligned 37-point hexagon». Autor: Codex (OpenAI).
El usuario autoriza esta revisión con Claude mediante «adelante» tras la
propuesta explícita de revisar las cuatro evaluaciones, los pesos del
certificado y el puente a la no saturación de walks. No se pide resolver
otros radios, construir walks, buscar literatura ni promocionar resultados.

Objetivo: comprobar la demostración exacta para m=3. Resultado esperado:
dictamen global y PASS / REPAIR_REQUIRED / FAIL para seis bloques:

1. Normalización del soporte alineado, 37 puntos, retícula Lambda/3,
   simetrías admisibles y reducción a h=alpha+beta*S1. Revisa la
   suficiencia del promedio para excluir también candidatos no simétricos.
2. Fórmulas sobre p=2q con x=cos(q), realizabilidad de los cuatro puntos,
   f0, Delta>0 y S1; rederiva las evaluaciones sin confiar en la salida.
3. Las cuatro desigualdades del informe, sentidos de las cotas al dividir
   por Delta y sus constantes racionales exactas.
4. Certificado: pesos positivos 64/169,64/169,64/245,64/245,
   cancelación de alpha,beta y suma negativa declarada. Determina si
   realmente excluye todo par real, no solo los puntos del muestreo.
5. Verificador: lectura de la aritmética racional, eliminación de alpha,
   selección de restricciones, segundo chequeo Laurent, condiciones de
   salida y límites de cobertura. No tienes herramientas: no afirmes
   que ejecutaste el código. Distingue certificado y procedimiento que
   lo descubre, y cualquier limitación operativa frente a la validez.
6. Puente a los walks: traza escalar, eliminación de fase, promedio,
   rigidez normal y conservación de s=2, nodo escalar, término lineal
   traceless/isotrópico, soporte dentro del hexágono y hull exacto.
   Comprueba los insumos adjuntos y que no se afirma un gap uniforme,
   otro soporte/orientación o una ley universal.

No heredes el PASS previo sobre la reducción general: se adjunta su
demostración, que debes contrastar en lo que m=3 necesite. El anterior
certificado S19 no se utiliza. Cada objeción debe precisar la brecha o dar
una derivación/contraejemplo. Separa reparaciones obligatorias de mejoras
opcionales. Un error de programa que no afecte al certificado matemático
debe describirse con ese alcance, sin ocultarlo ni confundir niveles.

Máximo de rondas: esta revisión inicial y, solo si hay reparaciones
obligatorias, una re-revisión acotada de ellas. Cierre: informe completo
sin objeciones obligatorias pendientes, o fallo/obligación abierta
identificados. Fallo de transporte o falta de informe no son revisión.
Ni un PASS ni la entrega operativa promocionan el resultado.
---

Herramienta canónica: revision-ciega del PATH; herramientas
ce09890a0d5f68a6634f358eff2e477ac5f15ec7.
Los documentos son copias selladas tomadas al ejecutar el lanzador.
