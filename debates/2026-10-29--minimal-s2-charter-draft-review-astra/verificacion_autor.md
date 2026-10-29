# Lectura crítica del autor — revisión Astra del borrador de charter s=2

Fecha: 2026-10-29. Autor de esta lectura: Claude, autor del borrador. **No es una revisión
independiente.** La revisión independiente es la de Astra (gpt-6-astra, familia OpenAI).

## Ejecución

Un intento: `COMPLETED`, de 10:21:12Z a 10:28:41Z. Antes del envío, `sha256sum -c inputs.sha256`
dio OK. Se enviaron cinco documentos: el borrador `8541cf72…` (sin commit), los dos charters
predecesores, la auditoría de fuentes y el PDF de P17. Herramienta: `revision_ciega.sh` @
`a32e189`. Autorización: «mandale el borrador a Astra».

## Veredicto del revisor

`NOT_READY`, con 14 reparaciones (A-R1-01 a 14). Hay dos errores matemáticos y uno de
normalización:

- La identidad para la partición en caras está mal.
- La clase con grupo espacial `O` no cabe en la definición.
- El cambio a vectores sin normalizar cambia el valor basal a 1.

## Contraste

**A-R1-05 (identidad para la cara). Se acepta: el borrador estaba mal.**
- El error es mío; está en la nota del presidente añadida a A1. Rehecho para la cara
  `S_+ = {(1,y,z)}`: el desplazamiento `ℓ=(2,0,0)` es normal a la cara. Lleva `(−1,y,z) ∈ −S_+` a
  `(1,y,z) ∈ S_+`, así que da `4 B^†A = 0`, no `A^†A + B^†B = 0`.
- Yo lo había comprobado con la cara `z=1` y el desplazamiento en `x`, que es tangencial. En el
  borrador escribí `(2,0,0)` sin fijar qué cara.
- La reparación del revisor funciona: con un desplazamiento tangencial a la cara, por ejemplo
  `(0,2,2)` para la cara `x=1`, salen dos pares, uno en cada mitad, y queda
  `A^†A + B^†B = 0`. Comprobado a mano:
  - `(1,−1,−1) → (1,1,1)` cae en `S_+`;
  - `(−1,−1,−1) → (−1,1,1)` cae en `−S_+`.

**A-R1-04 (`O` fuera de la clase). Se acepta: es correcto.** `O` es transitivo sobre los ocho
vértices (charter de isotropía, §0), así que no preserva ningún `S_+` de cuatro vértices. Las
filas «`E` bajo `O`» y «`O` reducible» del Paso 0.2 contradicen la definición de la Sec. 2. La
contradicción viene de mezclar dos formatos de isotropía:
- el de P17, transitivo sobre `S_+`;
- el del charter de isotropía, transitivo sobre todo `N_3`.

Esto requiere una **decisión del usuario**. Una opción es ampliar la definición con una segunda
familia: grupos transitivos sobre los ocho vértices, sin partición. `O` está en ella, y también
`D4` en torno a un eje, `[UNVERIFIED]`, que comprobaría el Paso 0′. La otra opción es dejar `E`
bajo `O` fuera de este charter.

**A-R1-02 (unidades). Se acepta.** Con `N_3` sin normalizar, `U_nuevo(k) = U_antiguo(√3 k)` y las
dos velocidades se multiplican por `√3`. El valor basal en estas unidades es `1`, no `1/√3`. La
igualdad no cambia, pero el número sí. El charter de isotropía también usaba vectores sin
normalizar; esto debe declararse.

**A-R1-12 (citas). Se acepta.** [23] es una nota publicada dentro de P17 (p.15) que remite a [31],
que sí es inédita. El borrador decía «unpublished refs. [23]/[31]». El revisor confirma el resto
de localizaciones (Eq. (2) en p.2; s=1 en p.4 citando [24]; Eqs. (12)–(13) en p.4; Fig. 1(c) en
p.6; Prop. 5 en p.7). Advierte además que la auditoría de fuentes usa paginación publicada y el
borrador paginación arXiv. No las he releído en esta sesión.

**Enumeración del Paso 0′.** El revisor la hace a mano: de las 16 elecciones de `S_+` salen dos
tetraedros, seis caras y ocho «vértice más tres vecinos». Estas últimas no son transitivas. Quedan
tres pares geométricos: `(V4, tetraedro)`, `(T, tetraedro)` y `(C4, cara)`. Es plausible y
coincide con la objeción del falsificador del comité. Sigue sin certificar: el Paso 0′ debe
comprobarlo.

**Lagunas (A-R1-01, 03, 06–11, 13, 14). Se aceptan como reparaciones de redacción o diseño:**
- cuantificar sobre todos los nodos admisibles;
- describir la clase sin presentarla como «P17 menos la Eq. (2)», y definir la fidelidad en
  `PU(2)`;
- reformular el Paso 0 como «verificar o refutar A1–A4»;
- incluir todas las representaciones de dimensión dos, también las reducibles;
- sustituir la invariancia por leyes de transporte en 4a, añadiendo el intercambio `h_1↔h_4` de
  P17 p.7;
- en 4b, variables reales, soporte activo y certificado de existencia real;
- separar en la Sec. 5 las salidas por pregunta, añadiendo «sin sectores admisibles» y «Q-a
  refutada», y renombrando `INADMISSIBLE_SATURATION`;
- citar el certificado de la cota general;
- presupuesto y parada por etapa;
- revisar la enumeración antes de usarla.

El contraejemplo del revisor contra la multiplicación por la izquierda
(`U = diag(e^{-ik}, e^{ik})`, `V = σ_x`, `(VU)^2 = I`) es correcto: `σ_x diag(a, ā)` tiene cuadrado
`|a|^2 I`. Confirma que esa exclusión está justificada.

## Conclusión del autor

- El borrador no está listo para congelar. Los dos errores (A-R1-04, 05) son de diseño y de una
  nota mía, no de resultados.
- Las anticipaciones A2 (con la precisión de `Q8` en `2O`), A3 y A4 quedan confirmadas a mano por
  el revisor. A1 es correcta para el tetraedro y queda reparada para la cara.
- Hace falta un borrador v2 con las 14 reparaciones. Antes, el usuario decide la ampliación de
  A-R1-04.
- Nada de esto autoriza congelar ni calcular.
