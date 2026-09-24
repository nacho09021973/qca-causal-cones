# H1c: auditoria del conteo de parejas Dyson

Fecha: 2026-09-24. Estado: `PRELIMINARY_LOCAL_FIBER_CHECK / H1c_LOCALIZATION (L') = OPEN`.
Sin revision independiente.

**Cierre documental del día:** este precheck conserva su alcance previo.
El contrato operacional posterior, los estados vigentes y el plan T1–T3
se fijan en [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Volterra/localización asintótica está PAUSED; este archivo no prueba las
respuestas físicas `(L_+, L_-)` del nuevo contrato.

## Objeto y fuentes

Se audita solo el presupuesto por numero de inserciones de la ruta propuesta
en [la reconstruccion H1](2026-09-20--h1-inhomogeneous-localization-reconstruction.md),
Sec. 9. La estructura espectral local procede del
[lema del simbolo inclinado](../papers/ir-corona/ir-corona.tex), Sec. 7.3,
y el contrato de beta y su regla de seleccion constan en
[`CURRENT_STATE.md`](../state/CURRENT_STATE.md), Sec. 9.1 y 9.4.
El barrido numerico antiguo de C2c no entra en esta auditoria.

En el maximo inclinado `eta=0`, escribamos

\[
D_0=\lambda P+\lambda^{-1}Q,\qquad
Q=I-P,\qquad \lambda=e^{\Phi_*}>1.
\]

En el modelo doblado, `P` y `Q` tienen rango dos. Bajo el contrato congelado
`beta^2=I` y `P beta P=0`, beta intercambia los dos haces, de modo que

\[
P\beta Q\beta P=P\beta(I-P)\beta P=P.
\tag{1}
\]

Esta identidad no requiere ortogonalidad de los proyectores de Riesz.

## Dos inserciones lineales

Para una moneda congelada de angulo `theta/N`, sea
`B_N=-i(theta/N) beta D_0`, el termino lineal de
`exp(-i theta beta/N)D_0-D_0`. La contribucion con exactamente dos
inserciones `B_N` en `(D_0+B_N)^N`, comprimida a `P`, es

\[
P\!\sum_{0\le j<k<N}
D_0^{N-1-k}B_ND_0^{k-j-1}B_ND_0^jP
=-\frac{\theta^2}{N^2}\lambda^N
\sum_{h=1}^{N-1}(N-h)\lambda^{-2h}P.
\tag{2}
\]

La distancia temporal `h=k-j` se suma geometricamente por la brecha
espectral, pero hay `N-h` posiciones para la pareja. Por tanto

\[
\lambda^{-N}(\text{lado izquierdo de (2)})
=-\frac{\theta^2}{N(\lambda^2-1)}P+O(N^{-2}).
\tag{3}
\]

Si `theta != 0`, la pareja tiene orden `N^-1` relativo, no `N^-2`.
El retorno por `Q` no recibe el factor `O(|q|)` de `P(eta+q) beta P(eta)`.

## Segunda comprobacion

En cada subespacio de dos dimensiones emparejado por beta, la matriz
`A_N=exp(-i theta beta/N)D_0` tiene determinante uno y traza
`cos(theta/N)(lambda+lambda^-1)`. Su autovalor dominante `mu_+` cumple

\[
\log\frac{\mu_+}{\lambda}
=-\frac{\lambda^2+1}{2(\lambda^2-1)}
\frac{\theta^2}{N^2}+O(N^{-4}),
\qquad
\left(\frac{\mu_+}{\lambda}\right)^N
=1-\frac{\theta^2}{2N}
\frac{\lambda^2+1}{\lambda^2-1}+O(N^{-2}).
\tag{4}
\]

Esto verifica por otra via una correccion dominante `O(N^-1)`. Su
coeficiente incluye tanto la pareja de (3) como el termino diagonal
`-theta^2 I/(2N^2)` de la moneda completa.

## Alcance para L'

El perfil globalmente constante usado para aislar el bloque no satisface la
condicion de momento de Fourier
`int (1+|p|)|hat vartheta(p)| dp < infinity` de la ruta espacial propuesta.
Sin embargo, un perfil suave de soporte compacto que valga `theta` en
`[-2,2]^3`, con la moneda evaluada en `x/N`, satisface esa condicion.
Los saltos de `D` desplazan cada coordenada a lo sumo una unidad por paso;
desde Alice, `|x_j|<=N/4`, todo camino de hasta `N` pasos permanece en
`|x_j/N|<=5/4`. En esos elementos Alice/Bob, tal perfil da exactamente
la misma moneda constante a lo largo de cada camino. La regularidad de
Fourier por si sola no elimina el mecanismo de (2).

Este calculo **no es un contraejemplo** a la cota propuesta para el elemento
Alice/Bob completo, ni prueba o refuta H1c: aun falta controlar si su
coeficiente particular cancela tras integrar los momentos y los extremos.
Comprueba que la identidad `P beta P=0` solo suprime la primera insercion lineal:
no proporciona un factor `N^-1` adicional por cada insercion Dyson cruda.
La meta `N^-13/2 (C'/N)^n/n!`, si `n` cuenta esas inserciones, necesita
una cancelacion adicional en el elemento completo o una reorganizacion
que cuente excursiones `P -> Q -> P` como unidades efectivas.

Siguen abiertos el control de productos no normales a momento variable,
las visitas al complemento, las transiciones entre los ocho entornos y la
localizacion fuera de las ventanas de Riesz. No se modifica ningun PASS ni
se promueve `H1c_LOCALIZATION (L')`. No se ejecuto codigo numerico.
