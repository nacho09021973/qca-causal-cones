# Dos contactos consecutivos: la primera puerta exacta no se compone sin fuga

2026-11-08. Autor Codex/OpenAI. **PRELIMINARY para el puente físico y la
derivación general; certificado Lean compilado para las identidades finitas
exactas que se indican abajo. Sin revisión independiente ni promoción.**

Usuario: «y puedes hacerlo solo o con lean?», referido a la comprobación
de composición propuesta. Contrato
[THIRRING_TWO_CONTACT_COMPOSITION_GATE.md](../theory/THIRRING_TWO_CONTACT_COMPOSITION_GATE.md)
en `d2279da`, escrito antes de los verificadores pero después de anunciar la
fórmula manual preliminar de fuga. No se presenta como preregistración anterior
a esa derivación. No se convocaron otros agentes ni modelos.

## Resultado

Para el mismo código microscópico M=1, regla U=FJ constante y salida libre
exacta F²B, la compresión tras dos pasos tiene fuga máxima

\[
 \boxed{p_{\max}^{(2)}=2\mu^2\nu^2(1-\cos\chi).}
\]

Con mu=3/5,nu=4/5,chi=pi/2 vale **288/625 = 0.4608**. Hay entradas producto
que alcanzan ese máximo. Así, la primera puerta exacta D_chi en F B no se
encadena con la segunda aplicación de la misma regla como una puerta
determinista sobre F²B. No se contó F ni J como control independiente.

Veredicto: `FIRST_CONTACT_EXACT /
SECOND_CONSECUTIVE_CONTACT_LEAKS_IN_EXACT_FREE_OUTPUT_CODE`.

Esto cierra esa composición concreta. No demuestra imposibilidad de recuperar
el código después, usar otros tiempos, geometrías o auxiliares, ni refuta
universalidad del autómata completo. La puerta exacta de un paso sigue siendo
válida. No se ha construido un procesador universal relativista.

## 1. Modelo y código de entrada

Misma regla del trabajo previo, W con R a derecha, L a izquierda, mezcla
-i mu y nu²+mu²=1. J=producto_x exp(i chi n_R(x)n_L(x)), antes de F.
Mu y chi son constantes durante ambos pasos. Fuente primaria local:
`1711.03920v1.pdf` pp.1–2 (W y regla de dos partículas, Ecs.(1)–(2));
`1804.08508v1.pdf` p.3 y pp.5–6 (modelo y sector interactuante/libre).
Las fórmulas siguientes se derivan de los W y J explícitos del contrato.

Trasladamos el origen a cero en la derivación. Los modos lógicos de A son
(R|0>, L|1>) en Gamma=+1; los de B son (R|1>, L|0>) en Gamma=-1.
El producto de creación en orden A,B define la isometría B de cuatro
estados al sector fermiónico Q=0. Se compara al final con F²B, construido
con modos libres de una partícula; no se aplica F^{-2} físicamente.

El primer contacto preserva B:

\[
 JB=BD,\quad D=\operatorname{diag}(1,z,z,1),\quad z=e^{i\chi}.
\]

Por tanto UB=FB D es la puerta exacta de un paso ya encontrada.

## 2. Qué hace el segundo contacto

En coordenadas de posición del sector Gamma de A, el primer paso libre
actúa sobre sus dos modos por

\[
 S=\nu X-i\mu I,\qquad S^\dagger S=I.
\]

Ambos modos de A quedan en posiciones {0,1}. Los de B evolucionan a
nu R|2>-i mu L|1> y nu L|-1>-i mu R|0>, respectivamente.
Solo las ramas de masa de B pueden volver a coincidir con A.

Sean P_0=S†|0><0|S y P_1=S†|1><1|S. Son proyectores ortogonales de
rango uno. En las entradas lógicas A tensor B,

\[
 P=P_1\otimes|0\rangle\langle0|
   +P_0\otimes|1\rangle\langle1|,
 \quad P^2=P=P^\dagger,\quad \operatorname{rank}P=2.
\]

Si C es el proyector de contacto de dos partículas,

\[
 C_1=B^\dagger F^\dagger CFB=\mu^2 P.
\]

No es un proyector para 0<mu<1: la rama que puede coincidir tiene peso
mu² y las ramas desplazadas de B son ortogonales a los modos de A.
Las dos coincidencias ocurren en sitios distintos, así que no hay términos
cruzados entre los modos lógicos 0 y 1 de B.

La matriz lógica de dos pasos se obtiene sin proyección intermedia:

\[
 K_2=(F^2B)^\dagger U^2B
 =B^\dagger F^\dagger JFB\,D
 =\left[I+(z-1)\mu^2P\right]D.
\]

Para comprobar el defecto se usa |z|=1 y P²=P:

\[
 I-K_2^\dagger K_2
 =\lambda D^\dagger PD,\qquad
 \lambda=2\mu^2(1-\mu^2)(1-\cos\chi)
 =2\mu^2\nu^2(1-\cos\chi).
\]

D†PD es un proyector no nulo y la salida libre es una isometría. Por ello
la norma de este defecto es la fuga máxima, igual a lambda. Los valores
singulares son 1,1,sqrt(1-lambda),sqrt(1-lambda). Si 0<mu,nu<1 y
chi no es múltiplo de 2pi, la fuga es estrictamente positiva.

Los controles chi=0,mu=0 o nu=0 dan lambda=0. Son casos degenerados;
no establecen una nueva arquitectura universal. No se varían parámetros
entre los pasos para realizar una puerta.

## 3. Matriz exacta y testigos a los parámetros congelados

Con mu=3/5,nu=4/5,z=i, la matriz es

\[
 K_2=\frac1{625}\begin{pmatrix}
 481+144i&0&-108+108i&0\\
 0&-81+544i&0&-108-108i\\
 -108-108i&0&-81+544i&0\\
 0&-108+108i&0&481+144i
 \end{pmatrix}.
\]

Además

\[
 D^\dagger PD=\frac1{25}
 \begin{pmatrix}16&0&12&0\\0&9&0&12\\12&0&9&0\\0&12&0&16\end{pmatrix}.
\]

El vector v=(4,0,3,0)/5, un estado producto del dato A y B=0, pertenece
al rango de ese proyector y alcanza fuga 288/625. La entrada 00 ya tiene
fuga positiva 4608/15625=0.294912. Por tanto ni siquiera es necesario
usar una entrada entrelazada para detectar la falta de cierre.

La parte algebraica de contacto no comparte necesariamente eje con la masa.
Ese hecho no remedia el defecto de unitariedad ni autoriza contar dos
generadores abstractos como controles que el autómata pueda seleccionar.

## 4. Qué comprueba exactamente Lean

Subproyecto autónomo [formal/thirring-two-contact](../formal/thirring-two-contact/README.md),
Lean v4.31.0, sin Mathlib ni descargas adicionales. El proyecto formal
anterior del repo no se modifica. Las definiciones y enunciados están en
[Challenge.lean](../formal/thirring-two-contact/ThirringTwoContact/Challenge.lean);
las pruebas están separadas en Solution.lean y los controles de axiomas
en Axioms.lean.

Lean comprueba, por reducción exacta de enteros gaussianos, nueve identidades:

- Acción del primer contacto en todo el código.
- Gramianos libres y reales de los cuatro estados tras dos pasos.
- Matriz comprimida K_2 exacta.
- Su defecto de Gram exacto.
- Identidad de proyector para la matriz entera H=25D†PD.
- Un autovector de H de autovalor 25.
- Déficit positivo de norma de la columna 00.
- Soporte final fuera de los sitios 6 y 7 nulo.

Cada paso libre reducido de dos partículas tiene denominador 25, y tras
dos pasos los estados tienen denominador 625. Lean verifica numeradores
enteros: Gram de estados 390625 I, inner(free2,actual2)=625 K_num,
y K_num†K_num=390625 I-7200 H. H²=25H. No usa floats, `sorry`,
`native_decide` ni axiomas científicos. Ocho teoremas no dependen de
axiomas; el del autovector usa solo `propext`, según las salidas vigiladas
por `#guard_msgs`. No se presume un resultado matemático por compilar sin
leer qué enunciados se han comprobado.

**Puente no formalizado:** se usa la identificación matemática del sector
de Gamma opuestos con dos posiciones, mediante el producto exterior
isométrico. Se sigue la regla reducida en un anillo de ocho sitios con
entrada en {2,3}; por localidad de alcance uno, en dos pasos no hay retorno
por frontera y coincide con la recta. La antisimetrización de Fock, la
interpretación de las normas y la fórmula general en mu,chi se justifican
por las derivaciones escritas; no se afirma que estén formalizadas en este
certificado. El certificado asegura el cálculo exacto finito declarado,
no un teorema de todos los QCA, un límite IR ni universalidad.

## 5. Verificación independiente de implementación y controles negativos

[verify_thirring_two_contacts.py](../scripts/verify_thirring_two_contacts.py)
implementa dos vías: propagación dispersa de enteros gaussianos y W tensor W
en amplitudes antisimétricas con espín explícito. La segunda vía no usa la
matriz K_2 esperada en el propagador. Resultado **44/44 controles de autor**;
[JSON](2026-11-08--thirring-two-contacts.json),
[registro](2026-11-08--thirring-two-contacts.txt). Los controles degenerados
chi=0 y mu=0,1 comprueban los factores de la fórmula. No se buscó un
parámetro por éxito ni se amplió a otros tiempos.

La herramienta canónica `lean-mutar` (herramientas `ce09890`) comprobó
compilaciones limpias inicial y final, y rechazó **3/3 mutaciones**:
signo incorrecto de la primera fase, coeficiente incorrecto de K_2,
y sustitución de una prueba por `sorry`. Las dos primeras fallan en
Solution.lean al intentar demostrar una proposición falsa; la tercera
falla en Axioms.lean. Se restauraron los bytes originales.
[Registro de mutaciones](2026-11-08--thirring-two-contact-lean-mutations.json),
[salida](2026-11-08--thirring-two-contact-lean-mutations.txt).

Durante la construcción se corrigieron dos incidencias de infraestructura:
hubo que desplegar los enunciados antes de sintetizar Decidable, y el
control inicial que exigía cero axiomas para el autovector rechazó
`propext`. Se fijó el mensaje a la dependencia estándar realmente usada,
sin relajar el resto. La salida fallida del control de axiomas está
[conservada](2026-11-08--thirring-two-contact-axiom-check-first.txt).
La [compilación final](2026-11-08--thirring-two-contact-lean-build.txt) y
la recompilación limpia final de las mutaciones pasan.

## 6. Decisión

La respuesta a «solo o con Lean» es: derivación física explícita,
contraste por otra implementación y un núcleo finito verificado en Lean.
Para esta arquitectura, ya el segundo contacto consecutivo tiene fuga
positiva. Se cierra esa composición y se detiene el trabajo bajo su
contrato, sin inventar una nueva geometría para esquivar el resultado.
Una arquitectura con auxiliares, otros intervalos o recuperación posterior
seguiría siendo una pregunta distinta. No hay conclusión sobre c, una
frecuencia absoluta de reloj o universalidad del modelo completo.
