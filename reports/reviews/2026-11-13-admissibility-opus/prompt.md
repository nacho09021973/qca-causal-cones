# Encargo de revisión ciega: admisibilidad general y Bravais

Autorización: usuario «que lo revise claude», 2026-11-13.
Base: `6ddda9784da2fb41aed3f054409eab68773d00ef`.
Herramienta: revision-ciega del PATH, herramientas
`7d111a158edda04a469b59f0d380cd69d35bbdea`.
Una ronda, sin reparación ni segunda ronda automática. Cierra con un
informe completo del proveedor, o con un fallo conservado sin dictamen.

---
Actúa como revisor matemático adversarial independiente. Revisa las
pruebas adjuntas de admisibilidad infrarroja para codificadores activos
en Z^d y en una red de Bravais fija. No aceptes los veredictos del autor
como evidencia. No tienes herramientas ni acceso al repositorio: deriva
los pasos desde lo adjunto y declara cualquier dependencia no verificable.
No incluyas llamadas simuladas a herramientas.

Objetivo: decidir si las tres razones de fuga son O(N^(-1/2)) con
denominadores positivos para N suficientemente grande, bajo los
cuantificadores congelados, y si el enlace condicionado con B1 es válido.
No se solicita un nuevo examen completo de la tasa B1, ni novedad.

Los tres informes de 2026-11-13 son los candidatos. Los contratos fijan
el alcance. El informe de leading-term B1 y su transferencia Bravais son
solo dependencias del enlace condicionado: separa expresamente lo que
rederivas de lo que asumes de esas derivaciones.

Comprueba en particular:
1. Identidades de Fourier, constante c_d, factor sqrt(covol(L)),
   normalización y masas positivas en cajas arbitrarias mediante
   analiticidad y conteos. No asumir que Alice está cerca del origen.
2. Estimación de multiplicadores matriciales, normas y factores de B;
   representación del toro, bolas físicas y complemento de Pi'.
3. Identidad de traza para Delta, suma doble no negativa, cota inferior
   para todo M chi != 0, y los casos de fase escalar y generador nulo.
4. Denominadores de operador mediante estados de prueba trasladados;
   umbrales dependientes de la red y ausencia de uniformidad indebida.
5. Compatibilidad del par activo con B1: bilinealidad del término
   principal frente al codificador exponencial no lineal; determina si
   el razonamiento elimina legítimamente los miembros nulos.
6. Cumplimiento del contrato, excepciones, hipótesis ocultas y cualquier
   afirmación más fuerte de lo que se demuestra. Una comprobación
   analítica por ti no equivale a ejecutar un verificador.

Entrega en español: veredicto global PASS / REPAIR_REQUIRED / FAIL,
dictamen separado por bloque, y para cada objeción obligatoria una
localización, derivación o contraejemplo y reparación mínima. Distingue
error fatal, hueco de prueba y mejora expositiva opcional. Si no encuentras
objeciones, justifica los pasos delicados sin repetir meramente el texto.
Una ronda solamente; no promociones el resultado.
---
