# Selección por flujo efectivo: lectura y decisión de continuidad

2026-11-06. Codex (OpenAI). Base Git:
`b434547432647ca72110d4f7b6c78583d70f27c9`.
Sesión documental autorizada por «adelante» a la propuesta de examinar un
único mecanismo y justificar un contrato sucesor o aparcar la ruta.
Había cambios previos en la hoja, CURRENT_STATE y la auditoría de premisas;
se conservan. No se abre un contrato de cálculo ni una nueva clase.

## 1. Pregunta y criterio previo

Conocido según CURRENT_STATE y la auditoría de premisas del mismo día:
la protección D2+C es provisional, su candidatura local de novedad está
cerrada y no hay mecanismo de selección especificado para el walk libre.
Esos documentos fijan el estado del proyecto; no son fuentes primarias
para validar física.

Pregunta: ¿el mecanismo de Anber–Donoghue deja una diferencia concreta que
justifique investigar la selección de un cono común desde nuestro QCA?
Corte anunciado antes de la lectura: aparcar si solo se impone la igualdad
de velocidades o se reproduce el mecanismo conocido sin una diferencia
precisa. No convertir una obligación pendiente en un programa automático.

## 2. Original y cobertura

Fuente: M. M. Anber y J. F. Donoghue, *The emergence of a universal
limiting speed*, arXiv:1102.0789v2, 25-03-2011, Phys. Rev. D 83, 105027.
[Registro primario](https://arxiv.org/abs/1102.0789v2).
PDF local: `biblioteca/arXiv-1102.0789.pdf`, 13 páginas;
SHA256 `46b33eb09d810174b2e54c71e39970be96b9acfa7f1cf92bb345d4557d8ed67d`.

Leídos los pasajes pertinentes de pp.1–4 y 7–10; cotejo visual de pp.3 y 7
para las ecuaciones y sus condiciones. Se usaron `pdfinfo`, `pdftotext
-layout` y `pdftoppm` para inspeccionar el original, sin código científico
ni resultados numéricos nuevos. No se rehicieron las integrales de loops,
los apéndices ni las simulaciones del artículo. Las restricciones
observacionales de 2011 no se adoptan como datos actuales.

El índice local se consultó antes. Algunas entradas remiten a
`reports/2026-10-27--interaction-speed-primary-preflight.md`, ausente en
este checkout; no se usa ese antecedente como evidencia ni se reconstruye
desde sus etiquetas. La ausencia local no prueba que el trabajo no exista.

## 3. Qué mecanismo se ha localizado

**Dice el original:** los parámetros renormalizados cambian con la escala
de energía mu; las funciones beta proceden de autoenergías, y el tratamiento
se limita a un loop (PDF p.2, Sec.2, Ec.(2)). En el ejemplo Yukawa hay un
escalar y un fermión, velocidades iniciales distintas y un acoplamiento
entre ambos (p.2, Ecs.(3)–(6)).

Las Ecs.(18)–(19), p.3, presentan el flujo de velocidades y su razón.
El artículo identifica la línea de igualdad como atractora IR; en p.4
da un autovalor nulo y otro positivo para el Jacobiano transversal.
La segunda formulación de la misma conclusión está en pp.7–8:
la diferencia relativa eta = cb/cf - 1 obedece la Ec.(52), y la Ec.(55)
describe su supresión logarítmica cuando también corre el acoplamiento.
Es una comprobación de consistencia de lectura por dos formulaciones del
original, no una reproducción independiente del cálculo.

**Interpretación para esta decisión:** la variable elegida es la
descripción efectiva al cambiar escala. El artículo no suministra una
ley de evolución temporal de monedas ni de reglas de actualización.
La cantidad que se pretende reducir es una diferencia relativa entre
velocidades de campos interactuantes, no una energía de la simetría.

## 4. Límites relevantes para el proyecto

| Cuestión | Evidencia primaria | Consecuencia para esta ruta |
| --- | --- | --- |
| Igualdad entre especies | PDF pp.2–4, Yukawa, Ecs.(3), (18)–(19) | Hay un antecedente explícito de atracción IR con interacciones; repetirlo no constituye nuestra contribución. |
| Isotropía espacial | PDF p.2, Ecs.(3)–(4): un coeficiente espacial escalar por campo | En este ejemplo se presupone; no se analiza un tensor de velocidades inicialmente anisótropo. No explica por sí solo selección de isotropía. |
| Valor común | PDF p.4, línea fija y modo nulo; p.2, elección de unidades | La igualdad no determina un valor físico único de c ni su relación con el cuerpo causal del QCA. |
| Rapidez del acercamiento | PDF pp.7–8, Ecs.(52)–(55) | Atracción asintótica no basta para justificar igualdad efectiva en una ventana finita. No se importa una tolerancia experimental de 2011. |
| Extensión multiespecie | PDF p.7, antes y después de Ecs.(48)–(50) | Se ignora la evolución de mezclas cinéticas consideradas pequeñas y se informa evidencia numérica sobre el espectro del Jacobiano. No es una prueba general para cualquier acoplamiento. |
| Aceleración del flujo | PDF pp.8–9, Ecs.(56)–(63) | Añade numerosos campos y supuestos de velocidades iniciales comunes dentro de sectores. No se adopta como solución gratuita para s=4. |
| Simetría de Lorentz completa | PDF p.10, Sec.9 | El propio artículo advierte que no toda violación de Lorentz desaparece. No identificar igualación de velocidades con restauración completa. |

No localizado en los pasajes examinados: construcción de un QCA finito con
nuestro soporte y representación, derivación de sus funciones beta, ni
selección de la antiunitaria C. Esta lectura de un artículo no establece
ausencia de esos resultados en la literatura ni novedad del puente.

## 5. Diferencia posible y obligación que falta

Una pregunta distinta del antecedente sería: **¿una actualización QCA
local e interactuante, con especies cuyas velocidades no están igualadas
por hipótesis, produce una reducción controlada de su diferencia al
cambiar escala, manteniendo los modos propagantes?**

Esto nombra una obligación, no un modelo disponible ni una candidatura
de novedad validada. Para convertirla en un contrato ejecutable faltarían:

- una actualización microscópica y una interacción concretas, con espacio
  local, soporte y unidades fijados; el s=4 del símbolo de una partícula
  no especifica por sí solo el espacio local de muchos cuerpos;
- un estado de referencia y una definición de las excitaciones y de sus
  velocidades efectivas;
- una operación de cambio de escala y un régimen controlado donde comparar
  velocidades inicialmente distintas, sin imponer su igualdad;
- un antecedente primario que permita justificar ese puente o una diferencia
  estructural concreta cuya comprobación no sea repetir la teoría continua.

No se ha satisfecho esa lista en esta sesión. Introducir interacciones
cambia la clase del proyecto y necesita un contrato sucesor; no se
interpreta el «adelante» documental como autorización para construirlo
o calcular loops. Tampoco se propone reemplazar mu por tiempo en las
funciones beta: sería otra dinámica, sin justificación aquí.

## 6. Decisión

**Aparcar esta ruta de selección al terminar la lectura documental.**
Hay un mecanismo conocido de flujo efectivo, pero no un puente microscópico
concreto listo para justificar un contrato de cálculo en este proyecto.
La diferencia deseada está formulada como pregunta; no está acreditada
como nueva ni como realizable. Se aplica el corte previo sin iniciar una
búsqueda de modelos alternativos.

Estado del diagnóstico: `DOCUMENTARY_SELECTION_ROUTE_PARKED`;
`SELECTION_MECHANISM_NOT_SPECIFIED` permanece para la clase libre actual.
No es imposibilidad de selección, refutación del RG ni cierre de la
pregunta A. La realización exacta s=4 con simetría adicional sigue abierta
y separada. D2+C conserva su nivel PRELIMINARY.

Reabrir requeriría aportar un modelo/puente concreto que permita completar
las obligaciones anteriores y decidir un nuevo alcance. La pregunta amplia
por sí sola no basta. Sin nuevo cálculo científico, revisión externa,
promoción, commit ni push.
