# Auditoría de correspondencia de los enunciados Lean

2026-11-08. Autor Codex/OpenAI. Usuario «adelante con b».
Objeto: correspondencia entre Challenge.lean y el informe de dos contactos.
Es una auditoría del propio autor, no una revisión independiente.

Sabido: 53a9868 conserva nueve teoremas computacionales y un informe que
separa el certificado finito del puente de Fock y de la fórmula general.
Pregunta: ¿los enunciados, dominios y factores representan exactamente
el cálculo descrito? Corte: no declarar correspondencia si hay desajuste;
documentarlo o corregir la descripción, sin sustituir la física para hacer
pasar los teoremas. No se abre recuperación a tiempos posteriores.

Procedimiento: lectura de definiciones y nueve proposiciones; contraste
con el propagador y el informe; recompilación limpia; inspección de
axiomas y del registro de controles negativos existente. No nuevo
experimento científico ni llamadas a revisores externos.

## Resultado

**Correspondencia confirmada para las nueve identidades finitas declaradas**,
con dos precisiones documentales sobre columnas de base y soporte final.
No se ha identificado una proposición vacía, un signo diferente, una
normalización incorrecta ni una hipótesis que asuma la fuga buscada.
Se mantiene el resultado físico de dos contactos con el alcance ya declarado.

El certificado no demuestra dentro de Lean el teorema general de norma o
fuga máxima del modelo físico: produce identidades de enteros que lo sustentan
mediante el puente matemático escrito. No es una formalización completa del
espacio de Fock ni una revisión independiente del autor.

## 1. Definiciones auditadas

En [Challenge.lean](../formal/thirring-two-contact/ThirringTwoContact/Challenge.lean),
`G=Int × Int` codifica real e imaginario. `add`, `mul`, `conj`, `scale`
y `normSq` coinciden con las operaciones de enteros gaussianos: en particular
el producto interno conjuga el primer argumento. No hay floats ni divisiones
enteras que trunquen una amplitud. Los denominadores comunes se restauran
en la interpretación, de forma explícita.

`Amp=Nat → Nat → G` es un tipo de funciones, no un Hilbert de la recta
ya formalizado. Las proposiciones cuantifican coordenadas `Fin 8`, columnas
`Fin 4`, o suman exactamente 0,...,7 y 0,...,3. No se afirma nada sobre
amplitudes en todos los naturales por el mero tipo `Amp`.

`input j` da, para j=0,1,2,3 respectivamente:

| j / estado lógico | x de A | y de B | fase del primer contacto |
| --- | ---: | ---: | --- |
| 0 / 00 | 2 | 3 | 1 |
| 1 / 01 | 2 | 2 | i |
| 2 / 10 | 3 | 3 | i |
| 3 / 11 | 3 | 2 | 1 |

Es la traslación par de origen +2 del código físico M=1. La resta natural
`3-j%2` toma solo 3 o 2: no hay saturación oculta que altere el código.

`perm true` intercambia 0/1,2/3,4/5,6/7; `perm false` intercambia
7/0,1/2,3/4,5/6. Ambas son involuciones. Son precisamente los intercambios
de posición de los sectores Gamma opuestos. Usar la misma permutación al
evaluar la amplitud inversa es correcto porque son involuciones.

`contact` multiplica por i si x=y. En `free`, los cuatro pesos enteros son
16,-12i,-12i,-9, es decir el numerador de

\[
 \big((4P_s-3iI)\otimes(4P_{-s}-3iI)\big)/25.
\]

Así se codifican nu=4/5,mu=3/5, con un denominador 25 por paso de dos
partículas. `step = free (contact ...)` aplica J antes de F, y las capas
`true` y `false` alternan en `free2` y `actual2`. No se invirtió el orden FJ
ni se introdujo una proyección entre contactos.

`kNum` coincide entrada por entrada con la matriz del informe (coeficientes
481+144i, -81+544i y las cuatro entradas -108+-108i en sus posiciones).
`hNum` es la matriz real simétrica de diagonal 16,9,9,16 y entradas 12
en (0,2),(2,0),(1,3),(3,1). No es un dato de propagación insertado en
`free` o `actual2`: solo aparece en las conclusiones a contrastar.

## 2. Correspondencia de cada proposición

| Proposición de Challenge | Qué afirma exactamente | Interpretación y límite |
| --- | --- | --- |
| `FirstGate` | Las amplitudes de cada una de las cuatro columnas tras un paso son las libres multiplicadas por 1,i,i,1 en todas las 64 coordenadas. | Primera puerta sobre las columnas; el paso a una superposición compleja arbitraria usa linealidad, no un teorema formal adicional. |
| `FreeGram` | Gram de las cuatro columnas libres de dos pasos =390625 I. | Al dividir los estados por 625, certifica sus coeficientes de ortonormalidad. |
| `ActualGram` | El mismo Gram para las cuatro columnas interactuantes. | La dinámica completa conserva el Gram: no se confunde fuga del código con pérdida de norma global. |
| `SecondCompression` | inner(free2_a,actual2_b)=625 kNum_ab. | Como cada estado tiene denominador 625, K2=kNum/625. |
| `DefectGram` | kNum† kNum=390625 I-7200 hNum. | La normalización da I-K2†K2=(288/625)(hNum/25). |
| `ProjectorIdentity` | hNum²=25 hNum. | hNum/25 es idempotente; su carácter autoadjunto se lee de la matriz real simétrica, no de esta proposición sola. |
| `WitnessEigenvector` | hNum (4,0,3,0)=25(4,0,3,0). | Tras dividir el vector por 5, da un testigo normalizado en el rango del proyector. Su norma y su interpretación física son pasos escritos. |
| `StrictColumnDefect` | La suma de cuadrados de la columna 00 de kNum es 275425; 390625-275425=115200>0. | Defecto de esa columna =115200/390625=4608/15625, positivo. No es por sí solo un teorema formal de fuga máxima. |
| `NoWrap` | En el estado final de dos pasos, libre e interactuante, las coordenadas 6 o 7 tienen amplitud cero. | Es soporte final. No afirma por sí solo una propiedad de todos los recorridos o tiempos intermedios. |

Las nueve proposiciones tienen instancias no vacías: cuatro columnas, ocho
coordenadas y el dominio finito completo que se indica. Ninguna toma como
hipótesis un valor del propagador o de la fuga. Todas son cálculos cerrados.

## 3. Reconstrucción del resultado y pasos que siguen fuera de Lean

Sea N=kNum y H=hNum. Los estados libres y reales se dividen por 625:

\[
 K_{ab}=\frac{\langle\texttt{free2}_a,\texttt{actual2}_b\rangle}{625^2}
 =\frac{625N_{ab}}{390625}=\frac{N_{ab}}{625}.
\]

De `DefectGram`,

\[
 I-K^\dagger K=\frac{7200}{390625}H
 =\frac{288}{625}\frac H{25}.
\]

H es simétrica real por definición y H²=25H por el certificado. Por tanto
H/25 es un proyector ortogonal. El autovector certificado es no nulo, de
norma 5. La norma del defecto es así 288/625 y el testigo v/5 la alcanza.
Este argumento usa álgebra lineal de operadores complejos y el significado
de un Gram de isometrías; esas estructuras y el teorema de norma no aparecen
en Challenge. Esta distinción concuerda con el alcance formal del informe.

También sigue fuera del certificado la identificación de las amplitudes
reducidas con Fock mediante sectores opuestos de Gamma. La comprobación
del script de espín explícito es otro contraste del autor, no un reemplazo
de la definición matemática de ese puente.

Sobre frontera: empezar en {2,3} y dar dos pasos de alcance uno implica
posiciones intermedias en {1,2,3,4} y finales en {0,...,5}. No se aplica
durante esos dos pasos el salto periódico 0/7 de una trayectoria ocupada.
Este argumento causal justifica la equivalencia con la recta. `NoWrap`
confirma el soporte final, pero no formaliza por sí solo ese argumento.

La fórmula general 2mu²nu²(1-cos chi), otras masas, otros acoplamientos,
límites IR y universalidad no son proposiciones de este certificado.

## 4. Pruebas, axiomas y validación de construcción

[Solution.lean](../formal/thirring-two-contact/ThirringTwoContact/Solution.lean)
demuestra cada proposición por reducción con `decide` después de desplegar
su definición. No usa `native_decide`, `sorry` ni una hipótesis científica.
`maxHeartbeats 0` quita el límite de recursos del elaborador, no el chequeo
del núcleo. `maxRecDepth` solo permite la profundidad de reducción necesaria.

[Axioms.lean](../formal/thirring-two-contact/ThirringTwoContact/Axioms.lean)
vigila con `#guard_msgs` la salida de `#print axioms` para los nueve
teoremas individualmente. Ocho no usan axiomas; el del autovector usa solo
`propext`. Si aparece `sorryAx`, una nueva dependencia o falta el mensaje,
el guard correspondiente falla. La raíz del proyecto importa Axioms;
el target por defecto sí ejecuta esos controles. El manifiesto no incluye
paquetes externos: solo Std/Lean de v4.31.0.

Se ejecutó una **recompilación limpia**, no solo la aceptación de un cache:

```sh
cd formal/thirring-two-contact
lake clean
lake build
```

[Salida conservada](2026-11-08--thirring-lean-statement-audit-build.txt):
Challenge, Solution, Axioms y la raíz recompilados, código de salida 0.
No se modificó ningún `.lean`, ni se regeneraron resultados físicos.

Se compararon los SHA256 actuales de Challenge y Solution con el
[registro de mutaciones](2026-11-08--thirring-two-contact-lean-mutations.json):
coinciden. El registro conservado acredita que los cambios de signo y de
coeficiente fallaron en Solution, y `sorry` falló en Axioms, con builds
limpios inicial y final de salida 0. No se repitieron esas mutaciones al
permanecer inalterados los ficheros comprobados. Herramienta canónica
`lean-mutar`, commit herramientas `ce09890`; MAPA.md consultado.

## 5. Ajustes de descripción y cierre de b

Se precisó en el informe y el README que la primera puerta se comprueba
por sus cuatro columnas, que la superposición requiere linealidad en el
puente escrito y que `NoWrap` es una afirmación de soporte final. Son
precisiones de cobertura; no cambios de modelo ni de resultado.

Se completa la opción **b**. El certificado dice lo que corresponde al
cálculo finito documentado, con las delimitaciones anteriores. Su contenido
no es una formalización completa de la fórmula física general. La
interpretación permanece PRELIMINARY y no se promociona ni se abre la
opción c. Al ser la auditoría del propio autor, no añade una revisión de
otra familia o una persona a la evidencia existente.
