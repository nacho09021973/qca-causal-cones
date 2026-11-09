# Mecanismo localizado: flujo de velocidades por interacciones

2026-11-06. Codex. Usuario: «adelante busca el mecanismo».
Filtro documental autorizado; no cálculo nuevo, simulación, modelo
interactuante ni ampliación ejecutada del alcance del proyecto.
Interpretación del filtro PRELIMINARY, sin revisión independiente.

## Pregunta y cierre fijado

Conocido: los filtros de hoy no han proporcionado protección nueva de
una velocidad común entre especies independientes en un QW irreducible.
Pregunta: ¿hay UN mecanismo publicado con variable, regla y condición
de atracción precisas que sirva de antecedente para la intuición del
usuario? Cierre: identificarlo en un original o registrar ausencia en
la búsqueda acotada. Si exige interacciones, señalar esa dependencia;
no introducirlas en el repo sin un contrato sucesor.

Biblioteca local ausente, como en los filtros anteriores. Se buscó en
originales con «emergent Lorentz symmetry velocity equalization
renormalization group interacting Dirac fermions bosons» y «Anber
Donoghue emergence universal limiting speed». Se seleccionó un solo
mecanismo para lectura, no un catálogo ni una búsqueda de novedad.

## Original y evidencia comprobada

M. M. Anber y J. F. Donoghue, *The emergence of a universal limiting
speed*, arXiv:1102.0789v2, Phys. Rev. D 83, 105027 (2011).
[Original](https://arxiv.org/pdf/1102.0789v2).
Copia sources/1102.0789v2.pdf, 13 páginas, SHA256
46b33eb09d810174b2e54c71e39970be96b9acfa7f1cf92bb345d4557d8ed67d.

Pasajes leídos mediante pdftotext -f/-l -layout:

- PDF p.2, Secs. 2–3, Ecs. (2)–(6): velocidades efectivas y acoplamientos
  corren con la escala mu; ejemplo fermión–escalar con interacción
  Yukawa g phi psi-bar psi. Cálculo limitado a un lazo.
- PDF p.3, Ecs. (18)–(19), y p.4, primer párrafo: c_b=c_f es una
  línea atractiva hacia el infrarrojo; el Jacobiano tiene eigenvalores
  0 y 7g²/(24 pi² c_f³). El cero deja libre la velocidad común.
- PDF pp.7–8, Ecs. (51)–(55): la diferencia relativa se suprime;
  al incluir el flujo de g la aproximación simple es logarítmica.
- PDF p.10, Sec. 9: no desaparece toda violación de Lorentz;
  las interacciones son necesarias para el mecanismo estudiado.

La atracción se comprueba en el original por dos formulaciones: flujo
del cociente (19) y Jacobiano al comienzo de p.4. No se han recalculado
diagramas ni integrado ecuaciones; no se presenta una verificación propia
de la aproximación perturbativa.

## Qué mecanismo es y qué no resuelve en este repo

La variable que cambia es la descripción efectiva al cambiar la escala
de energía. No se propone una dinámica temporal para a, theta, las
monedas o la geometría. Una trayectoria RG no es una trayectoria de
esos parámetros microscópicos bajo repetición de U.

La hipótesis útil para una eventual transferencia sería que la diferencia
de velocidades sea una perturbación irrelevante del régimen efectivo:
hay que definir el acoplamiento entre sectores, el régimen sin gap y
el mapa desde un sistema microscópico hasta esa teoría. Ninguno de esos
datos está construido para los QW libres actuales. La referencia no
acredita una realización QCA de alcance finito de su teoría.

Por tanto no modifica el resultado del filtro de simetrías internas:
la igualdad aquí se busca asintóticamente por flujo efectivo, no se
impone una simetría interna exacta a la actualización libre de un paso.

Tampoco responde por sí solo a por qué aparecerían los tres ejes
isotrópicos: el ejemplo leído asigna a cada campo una velocidad espacial
escalar desde su Lagrangiana. La selección de isotropía direccional
requeriría estudiar perturbaciones anisótropas adicionales, no incluidas
en esta lectura. Igualdad entre campos e isotropía son obligaciones distintas.

No se identifica la velocidad común con r_in, c_strict^iso o una velocidad
física medida. No se usan las cotas observacionales de 2011 como actuales.

## Decisión y condición de abandono de una transferencia futura

**LITERATURE_MECHANISM_IDENTIFIED: INTERACTION_DRIVEN_RG_ATTRACTION.**
**QW_TRANSFER_NOT_ESTABLISHED.** El mecanismo de selección de la regla
microscópica del QW sigue sin especificar. La referencia ofrece un
antecedente concreto de emergencia efectiva, no una solución del proyecto.

Una transferencia futura debería rechazarse si solo introduce mezcla
lineal entre sectores sin el flujo requerido; si el régimen queda
interrumpido por un gap; o si la diferencia no resulta irrelevante en
la teoría efectivamente derivada. No basta que el modelo de referencia
tenga una línea atractiva. Estas son condiciones de evaluación futuras,
no resultados calculados aquí.

Proseguir exigiría un contrato separado que autorice la clase
interactuante y fije su límite efectivo, observables y aproximación.
No queda autorizado por esta búsqueda. Se cierra al localizar y delimitar
este único mecanismo. Hexagonal aparcado; sin promoción ni envío a terceros.

## Provenance

Descarga sin transformación desde https://arxiv.org/pdf/1102.0789
(confirmado sello v2 en p.1), guardada con nombre versionado. Tamaño
291803 bytes. Lectura de pp.1–4, 7–10, hash mediante sha256sum e
inspección pdfinfo. No scripts científicos nuevos ni resultados numéricos.
La ficha de adquisición queda en sources/README.md. git diff --check.
