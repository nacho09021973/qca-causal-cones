# H1c: comprobación adversarial de la cota por inserción Dyson

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Alcance: únicamente la cota propuesta para los términos Dyson crudos en
`reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md`, §9.
`H1c_LOCALIZATION (L') = OPEN`.

**Cierre documental del día:** este precheck conserva su alcance previo.
El contrato operacional posterior, los estados vigentes y el plan T1–T3
se fijan en [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Volterra/localización asintótica está PAUSED; la conclusión sobre extremos
fijados no se transfiere aquí a las respuestas físicas `(L_+, L_-)`.

## Especialización admisible

Usamos el contrato `D=S\oplus S^{-1}` y
`\beta=\sigma_x\otimes I_2` de la reconstrucción H1, §1. Sea
`\vartheta\in C_c^\infty(\mathbb R^3)` real, igual a una constante
`\theta\ne0` en `[-2,2]^3`. Su transformada satisface la condición de
momento de Fourier de §9. Por propagación de alcance uno, los caminos de
`N` pasos que parten del soporte Alice, `|x_j|\le N/4`, sólo visitan
`|X_j/N|\le5/4`. Para el elemento Alice/Bob congelado, la moneda a lo
largo de cada camino es por tanto exactamente

\[
C_N=e^{-i\theta\beta/N}.
\]

La especialización permite analizar el término de dos inserciones del
operador `B_N=-i(\theta/N)\beta D`, sin asumir conservación de momento para
un perfil general. Aquí la constancia de la moneda sobre los caminos sí
reduce el elemento considerado al símbolo de moneda constante.

## Bloque dominante de dos inserciones

En una vecindad de cualquiera de los ocho máximos inclinados, escribimos
`D(\eta)=\lambda(\eta)\mathcal P(\eta)+\lambda(\eta)^{-1}\mathcal Q(\eta)`, con
`\mathcal Q=I-\mathcal P`, `|\lambda|>1`, y
`\beta\mathcal P\beta=\mathcal Q`. Esta última igualdad sigue de
`\beta D\beta=D^{-1}`. No se presupone ortogonalidad de los proyectores.
La suma exacta de los `0\le j<k<N` lugares de inserción satisface

\[
\mathcal P\sum_{j<k}D^{N-1-k}B_ND^{k-j-1}B_ND^j\mathcal P
=-\frac{\theta^2}{N^2}\lambda^N
  \sum_{h=1}^{N-1}(N-h)\lambda^{-2h}\mathcal P.
\tag{1}
\]

En cada ventana fija con `|\lambda|\ge1+\epsilon`, uniformemente,

\[
\sum_{h=1}^{N-1}(N-h)\lambda^{-2h}
=\frac{N}{\lambda^2-1}+O(1).
\tag{2}
\]

Así, el término principal del bloque dominante es
`-\theta^2\lambda^N\mathcal P/[N(\lambda^2-1)]`.
El bloque `\mathcal Q\to\mathcal Q` exige dos cambios cerca de los extremos
temporales para alcanzar el crecimiento `\lambda^N`, y aporta a lo sumo
`O(N^{-2}|\lambda|^N)` en estas ventanas. Los bloques cruzados se anulan
en orden Dyson dos porque cada `B_N` intercambia `\mathcal P` y
`\mathcal Q`.

## Consecuencia para un elemento Alice/Bob con líder plano no nulo

Embebamos los extremos planos del Teorema `T` de
`papers/ir-corona/ir-corona.tex`, §7.3, en la primera componente de la
duplicación: `f\mapsto(f,0)` y `w\mapsto(w,0)`. Su elemento de orden cero
es exactamente el elemento plano de `S^N`. El lema del símbolo inclinado
de ese TeX da los ocho máximos, la brecha fuera de sus ventanas y el mismo
desarrollo gaussiano local; el lema de capas deja sólo `0` y
`\pi(1,1,1)` al orden `N^{-13/2}`. En ambos,
`\lambda(\eta_0)^2=e^{2\Phi_*}`. Por (1)-(2), el multiplicador de la pareja
en el líder de ambos saddles es el mismo número real no nulo

\[
a=-\frac{\theta^2}{e^{2\Phi_*}-1}.
\]

Sea `\mathcal T_0(N)` el elemento plano, normalizado por `e^{K_*N}` como
en el Teorema `T`, y `\mathcal T_2(N)` su término con exactamente dos
inserciones de `B_N` en la especialización anterior. Denotamos por
`F(\theta_N)` el coeficiente complejo completo del Teorema `T`, con sus
dos saddles y capas discretas. La transferencia de
los lemas locales da, para la componente que contribuye al observable
plano,

\[
\mathcal T_2(N)
=\frac{a}{N}\,N^{-13/2}F(\theta_N)+O(N^{-8}),
\qquad
\mathcal T_0(N)=N^{-13/2}F(\theta_N)+O(N^{-7}).
\tag{3}
\]

El resto de (3) usa la misma ganancia gaussiana `O(N^{-1/2})` del Teorema
`T`, multiplicada por `N^{-1}`; las seis ventanas con carácter no trivial
y el exterior quedan por debajo de ese orden. Para el par plano
`(M,M_B)=(\sigma_2,I)`, el Teorema principal y su certificado de
coeficiente dan `2\operatorname{Re}F(\theta_N)` uniformemente separado de
cero. Al aplicar esa funcional real lineal a (3), la pareja tiene magnitud
`\Theta(N^{-15/2})` en la escala inclinada. La cota propuesta en la
reconstrucción para `n=2` exigiría `O(N^{-17/2})`; por tanto, **esa cota no
puede valer para inserciones Dyson crudas bajo esta especialización y esta
elección de extremos**.

Esta conclusión depende de que `T_n` en la propuesta incluya el término
Dyson crudo de `B_N` y permita la inserción de los extremos planos en la
primera componente. Si el contrato de `T_n` se restringe a otra
combinación de extremos o a grupos renormalizados de inserciones, esa
definición debe fijarse antes de aplicar la conclusión.

## Comprobación por el símbolo de moneda completa

En un par de autovectores recíprocos, la matriz
`e^{-i\theta\beta/N}D` tiene determinante uno y traza
`\cos(\theta/N)(\lambda+\lambda^{-1})`. Su autovalor dominante satisface

\[
\log(\mu_+/\lambda)
=-\frac{\theta^2}{2N^2}\frac{\lambda^2+1}{\lambda^2-1}
 +O(N^{-4}).
\]

Después de `N` pasos, la corrección es de orden `N^{-1}`. En el coeficiente
de `\theta^2`, la parte `-\theta^2/(2N)` procede del término diagonal de
segundo orden de `C_N-I`, y la parte
`-\theta^2/[N(\lambda^2-1)]` coincide con (1). Esta vía independiente
comprueba la contabilidad de escala; no sustituye una revisión
independiente del argumento Alice/Bob.

## Estado y reformulación necesaria

La prueba local por parejas de
`reports/2026-09-24--h1c-dyson-pair-audit.md` se extiende aquí a una
especialización del elemento completo con líder plano no nulo. Esto
descarta la fórmula `N^{-13/2}(C'/N)^n/n!` **para la lectura de `n` como
número de inserciones crudas**. No descarta una cota relativa `O(N^{-1})`
para la suma completa, ni una expansión reorganizada por excursiones
`\mathcal P\to\mathcal Q\to\mathcal P`. Tampoco controla productos a
momento variable, conexiones entre ventanas ni el exterior sin brecha
local. `H1c_LOCALIZATION (L')` y H1 permanecen abiertos. C2c, E0,
`POWER_13/2_STABILITY` y E/AdS no se modifican.

No se ejecutó código numérico ni se usó el barrido antiguo de C2c.
