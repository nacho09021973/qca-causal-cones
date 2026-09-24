# T2: trazabilidad del techo \(O(N^{-6})\) en las cinco piezas

Fecha: 2026-09-24. Estado: `TRACE_COMPLETE / BOUND_NOT_TRANSFERRED`.
Orden del usuario: después de la revisión independiente aceptada de T1,
antes de T3. Esta nota sólo sigue cotas y escalas registradas. No prueba
una asintótica, identifica un coeficiente ni busca cancelaciones.

## 1. Qué significa el techo anterior

El origen localizable está en `reports/2026-09-24--h1c-return-kernel-schur-audit.md`,
§§2–5, en particular (8), §§3 y 5. Allí se propone para el producto
inclinado **normalizado** la cota auxiliar
\[
\|\mathbb M_N\|_{\ell^\infty_tL^2_p\to\ell^\infty_tL^2_p}
=O(N^{-1}).
\tag{T2.1}
\]
El autor multiplica esa cota por dos masas absolutas inclinadas de extremos,
cada una \(O(N^{-5/2})\), registradas en `state/CURRENT_STATE.md`, §9.2.
La cadena de potencias es
\[
N^{-5/2}\,N^{-1}\,N^{-5/2}=N^{-6}.
\tag{T2.2}
\]
Esto es una **cota superior gruesa de una corrección bilineal normalizada**,
no una igualdad ni un término líder. No aparece un coeficiente firmado
\(E_6\); las fases se han eliminado con cotas absolutas.

En la reconstrucción T1, una amplitud de salida lleva el factor exacto
\(e^{-K_*N}\), mientras que el operador de memoria actúa sobre el producto
normalizado. Por tanto, si la cadena (T2.2) se transfiere a una contribución
lineal física, su escala sería a lo sumo
\(e^{-K_*N}O(N^{-6})\), no \(O(N^{-6})\) sin factor exponencial.
Una contribución cuadrática en amplitudes de salida lleva dos factores
\(e^{-K_*N}\). Las ecuaciones (7)–(12) de T1 hacen esta distinción exacta;
no determinan las potencias de sus factores normalizados.

El propio informe Schur limita (T2.1) al espacio auxiliar L2. Advierte que
no recupera por sí sola el perfil gaussiano tangencial, que las cotas de
extremo heredadas corresponden al protocolo plano, y que no controla las
entradas/salidas Q del nuevo elemento. §5 dice que los extremos físicos de
cuatro componentes, el funcional anterior \(L'\) y un denominador inferior
no estaban fijados entonces. T1 ya fijó el observable exacto, pero no
demostró que los extremos antiguos sean los extremos nuevos.

## 2. Descomposición que se debe rastrear

Para cada canal \(c\), las cinco piezas de T1 §3 son
\[
\begin{aligned}
A_{cP}&=2\Re\langle r_c,E d_{c,P}\rangle,&
A_{cQ}&=2\Re\langle r_c,E d_{c,Q}\rangle,\\
B_{cPP}&=\langle d_{c,P},E d_{c,P}\rangle,&
B_{cQQ}&=\langle d_{c,Q},E d_{c,Q}\rangle,\\
B_{cPQ}&=2\Re\langle d_{c,P},E d_{c,Q}\rangle.
\end{aligned}
\]
La dependencia en el W admisible y fijo de T1 se suprime en la notación,
pero cada fila conserva esa dependencia.

Con \(\ell_c(z)=\langle r_c,E\mathcal V_cz\rangle\) y
\(\mathcal H_c=\mathcal V_c^*E\mathcal V_c\), las escalas exponenciales
se leen exactamente de T1 (12):
\[
\begin{aligned}
A_{cP}&=2e^{-K_*N}\Re\ell_c(Pt_N),&
A_{cQ}&=2e^{-K_*N}\Re\ell_c(Qt_N),\\
B_{cPP}&=e^{-2K_*N}\langle t_N,P^*\mathcal H_cP t_N\rangle,&
B_{cQQ}&=e^{-2K_*N}\langle t_N,Q^*\mathcal H_cQ t_N\rangle,\\
B_{cPQ}&=2e^{-2K_*N}\Re\langle t_N,P^*\mathcal H_cQ t_N\rangle.
\end{aligned}
\tag{T2.4}
\]
Son factores exactos de normalización, no estimaciones de potencia.

Por (14)–(15) de T1,
\[
x_N=x_N^{\rm stay}+f_{Q,N}+(\mathbb M_Nx)_N,\qquad
y_N=G_Q(N,0)Qs+\sum_{k<N}G_Q(N,k+1)C_kx_k,
\]
\[
d_{c,P}=e^{-K_*N}\mathcal V_cx_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_cy_N.
\tag{T2.3}
\]
Sólo \(x_N^{\rm stay}=\Phi_P(N,0)Ps\) es trayectoria siempre P.
La salida final P también contiene la entrada desde Q y los retornos.
El operador \(\mathbb M_N\) aparece en \(x_N\); por sustitución de
\(x_k\), también influye en la salida Q. Por tanto las cinco piezas
pueden depender algebraicamente de retornos, pero esto no les transfiere
la cota (T2.1).

## 3. Trazabilidad por pieza

La tabla se aplica a \(c=+\) y a \(c=-\) por separado: da diez filas
con el mismo estado de transferencia. No se combinan respuestas entre
canales.

| Pieza | Objeto previo que la toca | Escala/cota disponible y su alcance | Resultado de transferencia a la pieza actual |
| --- | --- | --- | --- |
| \(A_{cP}\) | La corrección interna \(\ell_P(\mathbb M_Nx^{(0)})_N\) nombrada en Schur §5 cae en el sector que **termina** en P. Es la única correspondencia directa entre el sandwich bilineal de §3 y una pieza de T1: una sub-contribución de la interferencia lineal \(A_{cP}\), si sus extremos coinciden. | Condicionalmente, las masas antiguas \(N^{-5/2}\), (T2.1) y Cauchy–Schwarz dan el techo normalizado \(O(N^{-6})\) para ese sandwich; al deshacer el tilt, \(e^{-K_*N}O(N^{-6})\). Es cota de norma con signos/fases descartados. | **No se transfiere a \(A_{cP}\) completo ni a la sub-contribución nueva.** Aquí el extremo Bob es \(r_c=BU_N^NJ\phi_N\), no el extremo plano del precheck; la transferencia a la referencia nueva está explícitamente abierta. El vector fuente T1 es el encoder completo \(J(U_M-I)\phi_N\). Una parte \(\mathbb M_Nx\) puede integrar retornos iniciados en Q y retornos repetidos; la cota no aísla \(\mathbb M_Nx^{(0)}\) como coeficiente firmado. La atribución es candidato estructural, no una cota certificada para esta fila. |
| \(A_{cQ}\) | Interferencia de la referencia nueva con la salida que termina en Q. Según (T2.3), incluye Q inicial sobreviviente y salidas Q desde P mediante \(C_kx_k\). | El informe de resolvente, §3, muestra que las cargas P/Q de extremos planos embebidos pueden ser ambas del mismo orden \(N^{-5/2}\); por proyección final no aparece automáticamente una potencia extra. El control de fuga Q de CURRENT_STATE §9.3 es `PASS_IN_LOCAL_WINDOW`, no la respuesta actual completa. | **No hay cota \(O(N^{-6})\) transferible.** (T2.1) es una cota del retorno a P, no una cota de los términos Q de frontera. \(\mathbb M_N\) puede aparecer indirectamente por \(x_k\); la referencia \(r_c\) sigue sin cota de extremo certificada para este observable. |
| \(B_{cPP}\) | Forma cuadrática de la salida terminal P, que puede contener \(x_N^{\rm stay}\), \(f_{Q,N}\) y \((\mathbb M_Nx)_N\), además de sus interferencias entre sí. | Por T1, \(B_{cPP}=e^{-2K_*N}\langle \mathcal V_cx_N,E\mathcal V_cx_N\rangle\) exactamente. La positividad de E acota la diagonal completa por la norma de la amplitud, pero no asigna una potencia N al bloque de retorno. | **No hereda el \(N^{-6}\) bilineal.** No hay en (T2.1) un extremo de referencia: los dos lados son salidas del encoder. Acotar alguno de los sub-términos con retornos requeriría cotas de amplitud y cruces que el corpus no da para el lift actual. No se afirma una potencia para el factor normalizado que multiplica \(e^{-2K_*N}\). |
| \(B_{cQQ}\) | Forma cuadrática de la salida terminal Q: Q que sobrevive desde Alice y salida Q desde capas P. | Por T1, lleva exactamente \(e^{-2K_*N}\) por ser cuadrática en amplitudes. La cota auxiliar (T2.1) no controla por sí sola ni el Green Q físico ni las dos fronteras Q; la proyección no reduce necesariamente la masa de extremos (resolvente, §3). | **No hereda el \(N^{-6}\).** Faltan cotas físicas para ambas salidas y para sus cruces. No se prueba que la pieza sea grande ni pequeña. |
| \(B_{cPQ}\) | Cruce firmado entre salidas que terminan en P y Q. En (T2.4) es la suma conjugada de las dos composiciones cruzadas del efecto; no una norma de cada amplitud por separado. | Lleva exactamente \(e^{-2K_*N}\). No se localiza en el corpus una cota firmada o de norma del cruce para el observable actual. Que E sea positivo no anula el cruce; sólo impone la desigualdad de Cauchy–Schwarz ordinaria con las normas de ambas salidas. | **No hereda el \(N^{-6}\) bilineal.** \(\mathbb M_N\) puede entrar en la salida P y, vía \(x_k\), en la salida Q; las cotas existentes no acotan esa forma mixta con los extremos nuevos. T1 no afirma que el cruce sea distinto de cero. |

La dependencia indirecta de varias piezas en \(\mathbb M_N\) no equivale
a que cada una herede su norma como una cota para el escalar firmado.
La correspondencia de la primera fila es de **ubicación en el funcional**;
no selecciona un mecanismo dominante ni afirma que la vieja corrección
se conserve al cambiar los extremos.

## 4. Procedencia y datos que se perdieron

La fuente del \(O(N^{-6})\) no es un cálculo de cinco contribuciones.
Es la frase “Usándolas sin información adicional, (8) produciría para
la corrección interna una cota \(O(N^{-6})\)” de Schur §3. Schur §5
precisa su funcional como \(\ell_P(\mathbb M_Nx^{(0)})_N\), pero también
declara que esa traducción al elemento físico no era evaluable con el
contrato anterior. El cierre de modelo H1c §6 añadió la referencia nueva;
no certificó el traslado de extremos. T1 identificó el lift, pero no
modificó esa carencia cuantitativa.

Al tomar normas absolutas se pierden: (i) el signo y la fase de
\(\langle r_c,E d_{c,P}\rangle\); (ii) la relación entre saddle phases;
(iii) la fase interna y posible anulación de
\(\langle d_{c,P},E d_{c,Q}\rangle\); (iv) la dependencia de la nueva
referencia Bob en la moneda; (v) la dependencia de cada pieza en W; y
(vi) las correlaciones entre tiempo, momento y capa que la norma
\(\ell^\infty_tL^2_p\) suprime. Este registro describe información
perdida, no una hipótesis de que exista una cancelación.

No se probó que el coeficiente de una potencia \(N^{-6}\) exista. No
se afirmó que ninguna contribución esté físicamente en ese orden. El
resultado de T2 es más acotado: el techo previo sólo traza directamente
a la sub-contribución de retorno en el slot \(A_{cP}\) para el funcional
anterior y los extremos con que se obtuvo; no certifica ese techo para
ninguna de las diez piezas del observable nuevo. Puede haber cotas
distintas en los otros slots, pero no se deducen de la evidencia
inventariada.

## 5. Decisión sobre el paso siguiente

La trazabilidad algebraica queda cerrada al nivel que permiten los
registros existentes. El techo \(O(N^{-6})\) no se ha repartido entre
los diez observables firmados; sólo se ha localizado su antecedente
bilineal y las condiciones que faltan para transferirlo. Esto **no**
demuestra que el orden sea un artefacto sin efecto físico; sí impide
tratarlo como un término de \(L_c\).

Conforme al orden del usuario, el gate de T3 se evalúa ahora. Como T2
no aisló un término ni un coeficiente de orden \(N^{-6}\), no se buscan
simetrías ni cancelaciones de ese orden: hacerlo contradiría el STOP
congelado. Se registra la parada en
`reports/2026-09-24--two-channel-t3-stop.md`. La revisión de T1 aceptó
la álgebra; no revisó esta auditoría de escalas.

Herramienta sanedrín usada sólo para la revisión de T1: commit
`8162508e3bd0e3d05770b4dd544fe7c962d0272c`. Ningún script ni cálculo
numérico produjo este mapa; se obtiene trazando las identidades de T1
y los enunciados ya escritos en los informes citados.
