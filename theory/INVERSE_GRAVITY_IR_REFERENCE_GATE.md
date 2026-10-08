# IG1d — filtro de referencia para respuesta IR

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Base `8b58aed8ba1c58fe91fab7bed3085cd7a8bcc446`.
Autorización: «commit, push y continua» tras IG1c.
Contrato previo a ejecución, sin cambio de tick, ángulo, celda o constraints.

## 1. Pregunta fijada

¿La referencia `ρ_L=P/Tr(P)` de IG1b puede aportar respuesta lineal dinámica
media a fuentes físicas internas? ¿Es admisible un vacío que satisfaga R=T=1
para todas las palabras de las puertas del tick?

Este filtro distingue una referencia estacionaria de una referencia apta
para la ruta de respuesta gravitatoria adoptada. No calcula dispersión ni
selecciona estados desde eigenvalores de un candidato incompleto.

## 2. Clase, observables y respuesta

Tick completo y sector físico de IG1b/IG1c; toros L≥6 múltiplo de 6.
Observables A,B hermíticos que preservan P. Perturbación física interna
`e^-iεB` aplicada al estado, después n ticks del mismo U.
Se fija la susceptibilidad discreta como derivada en ε=0 de

`Tr[ρ_L e^iεB U^-n A U^n e^-iεB]`.

Equivale a `i Tr(ρ_L[B,A(n)])`, con A(n)=U^-n A U^n.
No confundirla con norma de conmutador ni con correlador de cuatro puntos.
Si hay fuente externa que cambie el sector o la regla, no pertenece a este test.

## 3. Pruebas predeclaradas

1. Demostración por traza cíclica restringida: la susceptibilidad anterior
   se anula para todo n y volumen admitido.
2. Segunda derivación: cualquier unitaria interna deja ρ_L invariante,
   por lo que la respuesta se anula a todos los órdenes en ε.
3. Aclarar compatibilidad con IG1c: un operador no nulo puede tener traza cero;
   su norma y correlador positivo `Tr(ρ_L C†C)` no tienen por qué ser cero.
4. El par físico TR=ω^-1 RT excluye un vector no nulo con R=T=1.
   Esto descarta solo la receta de vacío que minimiza cada A_W por separado,
   no todos los estados estacionarios, estados correlacionados o estados IR.

Certificado permanente `scripts/verify_inverse_gravity_ir_reference.py`:
controles exactos 3×3 de las identidades de traza y pareja Weyl, y un control
positivo de respuesta en un estado no tracial. No modelan el tick espacial
ni certifican su espectro. Los teoremas generales se derivan en el informe.

Tolerancia cero. Si las identidades fallan, parar y rehacer la derivación;
no ajustar fuentes, definición de respuesta ni estado para obtener PASS.
Resultado esperado como categoría, no como claim gravitatorio:
`TRACIAL_REFERENCE_RESPONSE_NULL / TERMWISE_VACUUM_INCOMPATIBLE`.

## 4. Alcance y cierre

Una respuesta media nula impide usar esta referencia para demostrar los
polos de respuesta lineal buscados mediante esas fuentes. No impide
correlaciones simétricas, influencia, física a temperatura finita o un sector
gravitatorio en otra referencia. El objetivo Einstein no se sustituye.

Mantener IR OPEN, tick y resultados físicos previos. La siguiente obligación
es justificar un estado correlacionado estacionario con respuesta no trivial
y control IR; no escoger un «ground state» por orden arbitrario de eigenfases.
No calcular espectro many-body hasta fijar esa selección, observables y límites.
