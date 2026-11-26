<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 02519c02f53b612b897f17373b0680cf4f7ad3cd15505f9b1ef85143cda7d8bb
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-26T12:35:48Z  fin: 2026-11-26T12:54:29Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment3-grok/amendment3.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 046354617c56f64a6e0313c4d2f2f05e2f0e842e024f29675853bd98dc5a0540
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md ; último commit observado: f9dce97 ; sha256 de la copia enviada dc35f5e00d3356325aa0447b70df53effe81cef37ca6037263cd4fc2daaa6e90
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment2-astra/informe_astra.md ; último commit observado: f9dce97 ; sha256 de la copia enviada ee109fe4932f4964d067a2914cd730cb700ca24da6ab16cdd3565dbee8db5a87
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_amendment3.py ; último commit observado: f9dce97 ; sha256 de la copia enviada 535dec08c127a0db0cdbebb6ae7fa8ed1b876e42a42e495f02cbcd97f3067e27
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_amendment2.py ; último commit observado: b1c6d75 ; sha256 de la copia enviada b6c68dc431aba0b21425b1e24a3329ffbe560e673250261c234e064d0dcff243
entrada_grok.txt sha256 36896ad0f60fa80427bfdaab440c4ee82ece3c024670a0759b67f358b7168d78
respuesta sha256 5539a7325c3766c6fba3b4dd555098bfb26ae9a3255a72bda43a790a613a3ede
-->

**Veredicto global: PASS.** La partición es 3+1, el contacto en el horizonte es de orden exactamente 2, el borde interior es un mínimo no degenerado con un bloque de Jordan de tamaño 2, y la redacción de \(t=7/16\) queda bien. No hay objeciones que exijan reparación.

| Punto | Veredicto |
|---|---|
| 1. Jordan 3+1 y rango sobre \(\mathbb Q(\sqrt6,\sqrt{10})\) | **PASS** |
| 2. Contacto exacto \((u-1)^2\) (J2) | **PASS** |
| 3. Borde interior en \(t=5/16\) | **PASS** |
| 4. Redacción \(t=7/16\) | **PASS** |
| 5. Las 10 comprobaciones | **PASS** |
| 6. Alcance y atribución | **PASS** |

No ejecuté código. Lo que sigue como identidad polinómica, signos y cadena de Jordan está derivado a mano. Del verificador solo inspecciono el código adjunto. Las multiplicidades algebraica 4 y geométrica 2 del horizonte, y el coeficiente cúbico, se toman de las Enmiendas 1–2, sin reabrirlas.

## 1. Jordan 3+1 — PASS

Las nulidades deciden la partición solas. Con \(d_j=\dim\ker K^j\) y \(d_0=0\), el número de bloques de tamaño al menos \(j\) es \(d_j-d_{j-1}\):

- \(\ge 1\): \(2\)
- \(\ge 2\): \(3-2=1\)
- \(\ge 3\): \(4-3=1\)
- \(\ge 4\): \(4-4=0\)

Además \(d_3=d_4\) implica \(d_j=4\) para todo \(j\ge 3\): si \(\ker T^k=\ker T^{k+1}\), entonces \(\ker T^{k+m}=\ker T^k\). La multiplicidad algebraica es 4 y el índice es 3. La única partición de 4 en dos partes con una de ellas igual a 3 es **3+1**. La segunda aserción de J1 (`nul[0]==2`, incrementos 1 y 1, y `nul[3]==nul[2]==4`) es exactamente esa característica de Weyr; la comparación encadenada de Python es correcta.

El cuerpo es el adecuado. Con \(t=3/8\),

\[
\cos\theta=\sqrt{3/8}=\sqrt6/4,\qquad
\sin\theta=\sqrt{5/8}=\sqrt{10}/4,
\]
\[
\cos 2\theta=2t-1=-1/4,\qquad
\sin 2\theta=\sqrt{15}/4.
\]

Y \(\sqrt{15}\) está en el cuerpo: si \(\alpha=\sqrt6+\sqrt{10}\), entonces \(\alpha^2=16+4\sqrt{15}\), luego \(\sqrt{15}=(\alpha^2-16)/4\). Las entradas de \(M(\pm1)\) son funciones racionales de estos valores con denominadores de moneda no nulos en el perfil, así que viven en \(\mathbb Q(\sqrt6,\sqrt{10})\). `convert_to` o embebe de forma exacta o lanza `CoercionFailed` y el script aborta; el rango posterior es eliminación gaussiana sobre un cuerpo. No veo un camino de falso positivo que anule radicales en silencio. No recalculé a mano los rangos \(12\times12\).

La misma partición sale por otra vía, sin rangos. En \(t=3/8\), \(W(0)=I\) y

\[
W'(0)=i\Bigl[\sigma_z+\mathrm{Ad}_{C(\theta)}\sigma_z+\mathrm{Ad}_{C(2\theta)}\sigma_z\Bigr],
\]
con \(\mathrm{Ad}_{C(\beta)}\sigma_z=\cos 2\beta\,\sigma_z+\sin 2\beta\,\sigma_x\). Los coeficientes quedan \(-1/8\) y \(\sqrt{15}/8\), de norma \(1/2\), así que los autovalores de \(W'(0)\) son \(\pm i/2\), distintos. Hay un autovector analítico de la rama cúbica. Como \(z-1=O(k^3)=O(h^3)\) con \(h=\lambda-1\) y \(\lambda'(0)\ne0\), los coeficientes de \(h^0,h^1,h^2\) dan una cadena \(KY_0=0\), \(KY_1=Y_0\), \(KY_2=Y_1\) con \(Y_0\ne0\). Índice al menos 3. Con algebraica 4 y geométrica 2 (Enmienda 2) se excluyen \(4\) y \(2+2\). En \(k=\pi\), \(W(k+\pi)=-W(k)\) y \(W(\pi)=-I\), y el mismo argumento da el gemelo. Esas nulidades son, por tanto, 2, 3, 4, 4 también por esta vía.

## 2. Contacto \((u-1)^2\) — PASS

J2 sí decide que \((u-1)^3\) no divide. `div` en \(\mathbb Q[u]\) por un divisor mónico devuelve resto único; `Poly.is_zero` es booleano estricto. `r2.is_zero` es la divisibilidad por \((u-1)^2\); `not r3.is_zero` es la no divisibilidad por \((u-1)^3\); `q2(1)\ne0` dice además que el cofactor no aporta otro factor. Con el orden de sustitución del código, las potencias pares \(C^{2m}\) pasan a \(u^m\) y un resto con \(\sqrt u\) haría fallar `Poly`, no dar un falso PASS.

A mano, con \(A=-3/32\),

\[
P_{3/8}(u)=\frac{105}{64}(u-1)^2(4-3u).
\]

En \(u=1\) el cofactor vale \(105/64\ne0\). Multiplicidad exactamente 2, y la otra raíz es \(4/3\notin(0,1)\).

## 3. Borde interior — PASS

**Identidad.** Con símbolos libres, \(4(1-C^2)g'^2-(1-g^2)=(1-g^2)(4E'^2-1)\) si \(E'^2=(1-C^2)g'^2/(1-g^2)\), y \(4E'^2-1=v(v+2)\) si \(v=2E'-1\). Ambas son las dos aserciones de B1; las comprobé por expansión. En la rama, \(\cos E=g(\cos k)\) y \(E'=\sin k\,g'/\sin E\) convierten eso en

\[
P_t(u(k))=\sin^2 E\cdot v(v+2).
\]

Ese diccionario es el paso ya marcado como no certificado por el script en el apartado de velocidades; B1 certifica el álgebra, no la regla de la cadena. La enmienda no lo esconde: la equivalencia \(v_+=0\Leftrightarrow P_t=0\) sigue escrita como paso no mecánico.

**Derivada en el cero de \(v\).** Si \(v(k_*)=0\),

\[
\frac{d}{dk}\bigl[v(v+2)\bigr]\Big|_{k_*}=2v'(k_*),
\]
el término con derivada de \(\sin^2 E\) se anula, y

\[
P_t'(u_*)\,u'(k_*)=2\sin^2 E(k_*)\,\Omega_+''(k_*).
\]

**Valor y signos.** La factorización de G4 más el prefactor dan

\[
P_{5/16}(u)=\frac3{1024}(1-u)\,(2625w^2+5w-16),\quad w=u-1.
\]

El prefactor cuadra en \(u=0\): ambos lados valen \(7812/1024\). En la raíz negativa,

\[
w_*=\frac{-5-\sqrt{168025}}{5250},\qquad
5250w_*+5=-\sqrt{168025},
\]
luego

\[
P'(u_*)=-\frac3{1024}(1-u_*)\sqrt{168025}.
\]

Esa es la primera aserción de B2. Además \(u_*=(5245-\sqrt{168025})/5250\). Como \(410^2=168100>168025\) y \(5245>410\), se tiene \(168025<5245^2\), así que \(u_*>0\). Y \(u_*<1\) es automático: \(5245-\sqrt{168025}<5250\). Por tanto \(P'(u_*)<0\). En \((0,\pi/2)\), \(u'=-\sin 2k<0\). B3 da \(0<E<\pi/2\), luego \(\sin E>0\). El producto \(P'u'>0\) obliga a \(\Omega_+''(k_*)>0\): mínimo, y el cero de \(v\) es simple.

**Jordan.** Está marcado como argumento escrito, y el argumento es correcto. \(\det(U(k)-z_*I)=(e^{i\Omega_+}-z_*)(e^{i\Omega_-}-z_*)\) tiene un cero de orden exactamente 2 en \(k_*\): el primer factor por \(\Omega''\ne0\), el segundo porque \(0<E<\pi/2\) separa las bandas (\(4E\in(0,2\pi)\)). \(\lambda=e^{-ik}\) es coordenada local (\(\lambda'\ne0\)) y determina \(k\) módulo \(2\pi\); los factores \(-zA^2\) y \(\lambda^5\) de la identidad característica no se anulan (\(A=-15/128\)). Multiplicidad algebraica 2. El núcleo de moneda es de dimensión 1 y la correspondencia de Bloch lo conserva: geométrica 1, un bloque de tamaño 2.

La separación queda bien hecha. B1–B3 certifican el álgebra, el valor de \(P'\), \(0<u_*<1\) y los ingredientes de \(g\). La derivación de \(\Omega''\) y el bloque son texto, y el bloque se declara no comprobado por la máquina.

## 4. Redacción \(t=7/16\) — PASS

\(P_t(1)=0\) para todo \(t\), porque \(g(1)=1\). Atribuir «sin raíz en \([0,1]\)» al cociente, no a \(P_t\), es la corrección justa. A mano,

\[
P_{7/16}(u)=\frac5{1024}(1-u)\,(343w^2-525w+144).
\]

Suma y producto de las raíces del cuadrático son positivos, luego ambas son positivas: ninguna en \([-1,0]\). El cociente no tiene raíces en \([0,1]\), y en \(0<k<\pi/2\) se tiene \(u\in(0,1)\), así que no hay velocidad nula ahí. El extremo \(k=0\) no cae bajo esa equivalencia. Las pendientes son \(8t-3=1/2\) y \(1-8t=-5/2\), las dos distintas de cero. La frase del docstring de la Enmienda 2, que no se reescribe, corresponde a la aserción que de verdad evalúa `Q716`.

## 5. Las 10 comprobaciones — PASS

Hay exactamente diez llamadas a `ok`: cuatro de J1 (dos autovalores, nulidad y partición), una de J2, dos de B1, dos de B2 y una de B3.

- **Cuerpo.** El lazo reconstruye \(M(z)\) en \(z=\pm1\). Un fallo de coerción aborta. El criterio de nulidades es el del apartado 1.
- **B2.** `168025 < 5245**2` es comparación de enteros de Python, equivalente a \(\sqrt{168025}<5245\) con ambos lados positivos, es decir \(u_*>0\). No usa flotantes. \(u_*<1\) no hace falta comprobarlo aparte. El rótulo añade \(P'<0\) y \(u'<0\), que son corolarios válidos de esta desigualdad junto con la fórmula de \(P'\), no un booleano de más. No hay falso positivo.
- **B3.** El booleano prueba \(g(0)=0\), \(g(1)=1\), \(A<0\), \(g'(1)=(4t-1)^2=1/16\) y la identidad \(g'(C)-g'(1)=12A(C^2-1)\). La comparación encadenada `a == b == c` es `(a==b) and (b==c)`. En \([0,1]\), \(C^2-1\le0\) y \(A<0\) dan producto no negativo, luego \(g'\ge1/16>0\). Con \(0<u_*<1\) ya decidido por B2, \(C_*=\sqrt{u_*}\in(0,1)\) y \(0<g(C_*)<1\). Si B2 fallara, el script no llegaría a B3.
- **Recuentos.** La aserción final fija los recuentos previos: 61, 8 y 39. El impresión `n/n` no fija el 10. En el fichero adjunto ese 10 es cierto por inspección, y las diez aserciones se ejecutan siempre que el script termina. No es un falso PASS de contenido.

## 6. Alcance y atribución — PASS

Cada cita mecánica coincide con lo que el código evalúa: J1 las nulidades y la partición, J2 el orden exacto del factor, B1 el álgebra, B2 la derivada y la cota entera, B3 los ingredientes de \(g\), G4 el recuento de raíces y el cociente en \(t=7/16\). El bloque de Jordan del borde interior está declarado argumento escrito. \(\Omega_+''>0\) entra en lo validado como consecuencia derivada en la Enmienda 3, no como una aserción de más de G4: eso corrige el alcance que Astra marcó. La etiqueta `[UNVERIFIED]` de la partición se retira con motivo; la de la compacidad de \(\omega_*\) y \(k_+(t)\) sigue en la tabla y no se toca. No queda un `[UNVERIFIED]` mal puesto.

La frase del docstring nuevo que remite los pasos escritos a `scripts/README.md` no la puedo comprobar: ese fichero no está adjunto. La separación que importa está en el cuerpo de la auditoría, y sí está.

No hay objeciones.
