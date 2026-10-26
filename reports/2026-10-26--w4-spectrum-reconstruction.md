# W4 espectro de onda larga — reconstrucción y límites de interpretación

Fecha: 2026-10-26. Autor: Codex. Base: `e519c90`.
Autorización: «adelante» al bloque e de reconstrucción documental.
Este registro contiene comprobaciones locales del autor, no revisión independiente.

## Reconstrucción y certificados ejecutados

Se restauraron manualmente las barras invertidas del contrato
`theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md` y del informe
`reports/2026-09-30--w4-long-wavelength-spectrum.md`.
Ambos pasan `scripts/check_reconstruction.py` contra `2d144d9`:
fuera de las cabeceras no cambian palabras, coeficientes o criterios.
Las observaciones siguientes no se introducen como cambios silenciosos en
el contrato ni en la ejecución histórica.

Se leyeron y ejecutaron `scripts/verify_w4_long_wavelength_spectrum.py` y
`scripts/verify_w4_geometry_stiffness.py`. Cada uno imprime cinco PASS.
El primero multiplica las matrices A, Bp y Bm, comprueba sus trazas y
determinantes y la expansión del control de signo alternado.
El segundo comprueba la puerta K completa, su generador, el fondo fijo y
el transporte de un defecto. No se modificó código.

## Álgebra que sí queda comprobada

Para c = cos(kappa), s = sin(kappa), las diagonales del producto Bp A son
`c^2 - s^2 exp(-ik)` y `c^2 - s^2 exp(ik)`. Con Bm cambian los signos
menos a más. Sumar las diagonales y usar la fórmula del coseno reproduce
las dos trazas del certificado por cálculo manual.

Con determinante uno, los valores propios de estas matrices sin fase son
`exp(±i omega)`. Para el control de signo alternado se obtiene también

\[
\sin^2\frac{\omega_-(k)}2
=s^2\sin^2\frac{k}2,
\qquad
\omega_-(k)=2\arcsin\left(|s|\,|\sin(k/2)|\right)
\]

en la rama no negativa próxima a cero. Esta segunda formulación reproduce
la pendiente `|s|` con respecto a k. Para s = 0 no hay pendiente lineal
no nula: la afirmación de propagación requiere acoplamiento no degenerado.

## La fase omitida afecta al cero de cuasienergía

El contrato pide omitir la fase común del enlace. Sin embargo, la puerta
original es `K(kappa) = exp(-i kappa) M(kappa)` en el subespacio de un
defecto de un enlace, mientras que deja el par de vacío exactamente fijo.
En cada matching, un defecto pertenece a un único enlace ocupado; el resto
de pares de vacío aporta identidad. Por tanto el paso de dos capas en el
sector de un defecto es

\[
U_{+,\mathrm{full}}(k)=e^{-2i\kappa}U_+(k),
\qquad
U_{-,\mathrm{full}}(k)=U_-(k).
\]

Las fases se suman en el primer caso y se cancelan en el segundo. La fase
retirada es global dentro de ese sector, pero no común al sector de vacío.
No cambia velocidades de grupo ni degeneraciones entre las dos bandas;
sí cambia el cero de cuasienergía respecto al vacío fijo de la puerta completa.

En k = 0, el vector simétrico `(1,1)` tiene valor propio `exp(2i kappa)`
en U+, y por tanto valor propio uno en el paso completo. Hay una rama de
cuasienergía cero en ese punto. Como segunda comprobación, el estado uniforme
de un defecto es invariante bajo cualquier SWAP de vecinos: cada puerta K
lo deja fijo, exactamente igual que al vacío. No se puede afirmar que el
espectro completo carezca de una rama suave de frecuencia cero.

Para `0 < kappa < pi/2`, fijado lejos de los extremos, la expansión manual
de la traza es `cos(omega_+) = cos(2 kappa) + s^2 k^2/2 + O(k^4)`.
En la rama que vale 2 kappa en cero, eso da

\[
\omega_{\mathrm{uniforme,full}}(k)
=2\kappa-\omega_+(k)
=\frac{\tan\kappa}{4}k^2+O(k^4).
\]

El modo suave del paso original es cuadrático en ese régimen, no lineal.
La comparación defendible es entre ese modo y el cruce lineal del control
de signo alternado. La etiqueta histórica `SMOOTH_MODE_GAPPED` describe
el cero de la matriz sin fase, no una ausencia de rama cero del paso completo.
La reconstrucción no promueve esta interpretación corregida a resultado
independientemente revisado ni sustituye el modelo canónico.

## Unidades del momento y de la velocidad

Las fases `exp(±ik)` de Bp y Bm trasladan el índice m de la celda `(A_m,B_m)`.
Así, la pendiente `|sin(kappa)|` es en celdas por paso de dos capas.
Si cada registro vecino dista una unidad, la celda mide dos unidades:
con momento por registro p = k/2, la velocidad correspondiente es
`2 |sin(kappa)|` registros por paso de dos capas.
La frase histórica que expresa la primera pendiente en sitios de la red
necesita esta conversión; no se corrige añadiendo barras invertidas.

Hay un control manual exacto de ese factor: en kappa = pi/2, el producto
Bm A es `diag(exp(-ik), exp(ik))`. Un componente se desplaza una celda por
paso, es decir, dos registros. En ese mismo ángulo las dos puertas originales
K de signo opuesto son SWAP, así que el caso de igual signo también tiene
ese transporte. Las afirmaciones genéricas de modo suave no lineal no se
extienden a este ángulo excepcional.

## Un defecto no es todavía una onda del métrico

El símbolo calculado evoluciona amplitudes de un defecto de Z, no directamente
la expectativa z que controla el tetrad. Para un estado normalizado
`|psi> = sum_n psi_n |n>` con un único defecto sobre el fondo cero,

\[
\langle Z_n\rangle=1-2|\psi_n|^2.
\]

Esto se sigue directamente de los valores propios de Z en la base de defectos.
Una fase alternante de las amplitudes no obliga a alternar esa expectativa;
una onda de Bloch de módulo uniforme tiene densidad uniforme en cada
subred. Por tanto la afirmación histórica de que el nodo en pi implica
alternancia de la expectativa del control no está derivada por este cálculo.
Tampoco el cruce lineal reparado prueba por sí solo una onda lineal de z
o del métrico. Sigue faltando la identificación del observable y su límite
continuo, además del problema tensorial y tridimensional.

## Validación y decisión de alcance

```sh
python3 -B scripts/check_reconstruction.py theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md
python3 -B scripts/check_reconstruction.py reports/2026-09-30--w4-long-wavelength-spectrum.md
python3 -B scripts/verify_w4_long_wavelength_spectrum.py
python3 -B scripts/verify_w4_geometry_stiffness.py
python3 -B scripts/text_integrity.py --check
git diff --check
```

Reconstrucción 2/2 PASS; ambos certificados PASS en su alcance. El veredicto
impreso del primero sobre el gap no certifica una afirmación sobre el espectro
del paso completo respecto al vacío. Los contrastes adicionales anteriores son
manuales y quedan trazados aquí; no se ejecutó código científico temporal.
No se hizo un barrido nuevo de certificados porque no se cambió código.

Avisos: de 249 a 211, al retirar los 38 delimitadores desnudos del par
(6 + 32). El detector global conserva código 1 por la cola restante;
no aparecen avisos en este par ni en este registro. El diff pasa la
comprobación de espacios.

El estado `W4_REPAIR_AVAILABLE_SMOOTH_GAPLESS` se conserva como registro
histórico de las matrices sin fase y de un control 1D. No se usa aquí para
afirmar un gap respecto al vacío del paso original, una velocidad en sitios
sin conversión, ni una onda del métrico. No se promueve evidencia, no se
adopta el control como nuevo modelo y W1–W12 permanece cerrado por contrato.
Este bloque termina con esas limitaciones documentadas. La cola tipográfica
siguiente es W5 completitud espacial del tetrad (bloque f).
