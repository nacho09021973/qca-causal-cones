# Opción 11: estabilidad de una velocidad común — filtro documental

2026-11-05. Codex. PRELIMINARY; sin revisión independiente.
Autorización: usuario «adelante» a localizar un modelo publicado con dos
sectores y parámetros independientes, y comprobar las perturbaciones
admisibles. Sin cálculos, scripts o nuevos modelos en este filtro.

## Pregunta y corte

Conocido: CURRENT_STATE Sec. 4 mantiene la universalidad OPEN. El constructor
s=4 del repo tiene dos dobletes nodales. Pregunta: ¿hay una clase concreta
en la que pueda ponerse a prueba c_1/c_2=1 mediante perturbaciones locales,
unitarias y de simetría fijada? No confundir variar juntos ambos c con
poner a prueba su igualdad. Corte de esta etapa: sin parámetros
independientes o sin clase exacta de perturbaciones, no comenzar el cálculo.
Un filtro negativo no prueba inexistencia de modelos en toda la literatura.

## Constructor local

theory/S4_STRICT_CONE_COUNTEREXAMPLE.md Secs. 2 y 7:
A_(a,theta)=W_theta prod_i exp(-i k_i Gamma_i/sqrt3), con
W_theta=I tensor exp(-i theta tau_z).
Dos sectores de rango dos en fases opuestas; las compresiones impresas
tienen orientación opuesta y la misma magnitud a/sqrt3. Variar a modifica
ambas velocidades conjuntamente; variar theta cambia la separación de
fases. Esa familia no contiene en sus parámetros declarados una prueba de
estabilidad frente a perturbaciones generales.

La irreducibilidad establecida en Sec. 6 excluye que sea simplemente una
suma directa de dos walks constantes; no prueba que todas las
perturbaciones admisibles conserven la igualdad. No se rescata la
candidatura de novedad de esta familia, abandonada en CURRENT_STATE.

## Literatura localizada

- Murshed y Roy, arXiv:2407.18250v2, original HTML, abstract e introducción:
  https://arxiv.org/html/2407.18250v2 . Dos velocidades en fermiones Dirac
  birrefringentes; simetrías que protegen ausencia de gap y convergencia
  por interacciones son cuestiones distintas. El escenario es un modelo
  Hamiltoniano con generalización no hermítica, no un constructor QCA
  unitario de alcance finito que podamos adoptar sin demostración.
- Kennett y colaboradores, arXiv:1011.1502: localizado por título y
  abstract como antecedente de birrefringencia en red cuadrada. Texto
  completo no leído aquí; alcance exacto [UNVERIFIED].
- Apadula y colaboradores, arXiv:1806.03940, abstract original consultado:
  https://arxiv.org/abs/1806.03940 . Incorpora masa como grado de libertad
  y estudia cambios de referencia. El abstract no proporciona la clase de
  perturbaciones de dos velocidades independientes requerida aquí.

Búsquedas: quantum walks birefringent Dirac fermions velocity symmetry
perturbations; quantum cellular automata multiple species different speeds
symmetry stability; birefringent Dirac fermions velocity equality symmetry
protection lattice. Índice local leído antes de investigar. Búsqueda
orientativa, no exhaustiva; ninguna equivalencia de hipótesis acreditada.

## Resultado del filtro

NO_READY_TEST_CLASS_IDENTIFIED_IN_SCOPED_READING.
No se abre un cálculo: falta una clase exacta de perturbaciones que pueda
romper la igualdad y a la vez respete el contrato físico. La opción 11
queda como propuesta abierta, sin novedad acreditada. El constructor local
es un punto de comparación, no una prueba de protección ni un descarte de
la posibilidad de separar sus conos mediante otras deformaciones.

Una continuación requeriría un charter propio que fije soporte, dimensión,
representación de simetría, nodos y conservación de conos. No convertir una
derivada nula dentro del ansatz en estabilidad en toda la clase. No se
promueve resultado ni se modifica CURRENT_STATE en esta nota.
