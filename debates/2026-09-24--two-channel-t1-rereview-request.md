# Revisión de reparaciones T1: nueva ejecución

## Decisión solicitada

Revisar si la versión reparada resuelve las objeciones obligatorias del
acta de Opus y si aparece algún error nuevo. El objeto es sólo T1. No
ejecutar T2 ni hacer inferencias sobre las potencias del observable.

## Reparaciones declaradas por el autor

1. Fija una vez para T1–T3 vecindades abiertas \(W_\alpha\) de los ocho
   saddles, con cierres disjuntos contenidos en dominios \(O_\alpha\)
   de ramas dominantes espectralmente aisladas, independientes de N,
   encoder, detector y moneda. Declara explícitamente que las diez piezas
   son relativas a este W fijo, que pueden depender de W y que T2 deberá
   conservar esa dependencia o probar uniformidad. No se afirma un radio
   numérico ni independencia de las piezas con respecto a W.
2. Deriva la acotación de P desde la fórmula espectral de rango uno sobre
   los cierres compactos y concluye \(C_P(W)<\infty\), sin usar P*=P.
3. Define \(\mathcal V\) por restricción ponderada a Bob finito y deduce
   que \(\mathcal H_c=\mathcal V_c^*E\mathcal V_c\) es acotado para N
   fijo.
4. Añade una multiplicación directa para N=2 con bloques genéricos y un
   ejemplo de una fibra en la que B,C y BC son no nulos.
5. Aclara que el control \(U_{enc}=I\) es una prueba algebraica de bits
   iguales, no el encoder del caso M=I.

## Cuestiones que deben atacarse

- ¿Las condiciones nuevas de W garantizan realmente existencia y cota
  uniforme del idempotente, especialmente con ramas negativas en saddles
  trasladados y al extender P=0 fuera de W? ¿El argumento de traza,
  determinante y continuidad basta?
- ¿Las piezas quedan ahora bien definidas como objetos para cada W fijo,
  con una dependencia que T2 puede trazar? ¿Hay ambigüedad que impida
  llamarlas piezas matemáticas? No exigir invariancia en W si no se
  afirma. Separar dependencia paramétrica de indefinición.
- ¿El caso de fibra de (18) es consistente con D, beta, normalización,
  orden C_N D y N=2? ¿Es válido como control algebraico de la recurrencia,
  sin presentarlo como resultado del protocolo físico?
- ¿Queda resuelto el dominio del peso, acotación de V y H_c, signo de
  Fourier, factor exponencial, fórmula firmada y salida Volterra?
- ¿El cierre de T1 se mantiene dentro del alcance sin trasladar cotas o
  concluir nada sobre O(N^-6)?

Distinguir objeciones matemáticas, preferencias de presentación y aspectos
fuera de alcance. Para cada reparo decisivo, indicar ecuación y condición
de concesión. Dictamen: `T1_PASS`, `T1_REPAIR_REQUIRED` o `T1_OPEN`.
No crear reparos por formalidad si las condiciones explícitas bastan.

## Integridad e independencia

La revisión anterior fue una ejecución incompleta de sanedrín:
Claude Opus produjo T1_REPAIR_REQUIRED; Gemini falló dos veces con HTTP
402 y no emitió juicio. No se presenta aquella ronda como consenso.
Esta revisión vuelve a consultar Claude Opus y DeepSeek v4-Pro. El segundo
miembro es la verificación de otra familia; la discusión es deliberativa,
no ciega. Si DeepSeek falla, consignar T1 como pendiente de revisión
externa al autor, no como PASS ni como consenso.

Revisad el snapshot adjunto; las afirmaciones del prompt son resumen
contrastable, no fuentes. No ejecutéis T2/T3 ni editéis archivos.
