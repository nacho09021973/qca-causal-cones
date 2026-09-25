# C3 — revisión completa interna desde Astra

Fecha: 2026-09-23. Revisor: Codex, agente `/root`, revisión solicitada
por el usuario desde Astra. No se ha convocado otro modelo en esta revisión.

**Resultado matemático: PASS interno, sin reparaciones pendientes en el
objeto revisado dentro del contrato C3.**
**Nivel de evidencia: `C3_INTERNAL_REVIEW_PASS / INDEPENDENT_REVIEW_PENDING`.**
Esta etiqueta describe esta revisión, no introduce un nuevo veredicto
canónico del gate. La aceptación independiente exigida por el contrato
no se obtiene con una revisión de la misma familia que escribió la prueba.

## 1. Objeto, fuentes y autoría

Objeto: `reports/2026-09-23--c3-conditioning-execution.md`, commit
`479a25d6bb19c961abb386e53cbf3b7689811767`, SHA256
`030e2396a1f209ac9f86f8392d1c634f8175c5dd605fc22de3f24c10869118de`.
Contrato: `theory/IR_C3_CONDITIONING_GATE.md`, obligaciones 1–5.

Se han leído y contrastado directamente las definiciones y derivaciones:

- Manuscrito `papers/ir-corona/ir-corona.md`: §2.1 (medida Fourier y
  producto escalar de red), §2 (símbolo y Hamiltoniano Weyl), §§3.1–3.2
  (regiones, recurso y efecto), §7.5, Lema 7.2 (campo libre).
- C1: `reports/2026-09-22--ir-projection-leakage-and-conditioning.md`,
  §3, (2)–(4); su revisión independiente, §§2–5, para el estatus heredado.
- C2c: `reports/2026-09-22--c2c-structural-scope.md`, (C8)–(C16) y las
  cuatro filas `D_0=I` de §8; su revisión independiente del 2026-09-23
  y `state/CURRENT_STATE.md`, §10.1, para el estatus heredado.
  El SHA256 de C2c sigue siendo
  `0268d8c869fa1b4666df09327e9ce25c0f545401fd5159286287580a888153a0`,
  idéntico al objeto de esa revisión independiente.

Los veredictos previos no se usan como sustitutos del cálculo. C1 y C2c
son entradas congeladas; se audita su aplicación a C3, sin reabrir sus gates.
La revisión Claude/Gemini degradada se usa como lista de objeciones, no
como certificado de consenso. El revisor también corrigió el objeto:
esta es una revisión interna con conflicto de autoría declarado.

## 2. Estados, probabilidades e identidad exacta — PASS

El soporte Fourier de `phi_N` tiene radio `N^-1`, contenido en el del
proyector `P` de radio `N^-1/2`. Por tanto `P phi_N=phi_N`, `Q phi_N=0`.
La unitariedad de `U_M` y la ortogonalidad `P Q=0` dan
`||w||^2+||t||^2=1`, con `w=P U_M phi_N`, `t=Q U_M phi_N`.

El bit cero se retiene con probabilidad uno y estado `phi_N`; el bit uno
con probabilidad `1-q_N` y estado `w/sqrt(1-q_N)`. Además,
`Delta_PP=|w><w|-|phi_N><phi_N|`. Sustitución directa prueba (C3.1);
traza contra `S^{-N} E S^N` prueba (C3.2) y (C3.3).

Segunda comprobación, directamente con probabilidades: sea
`a_N=<S^N w,E S^N w>` (sólo en este párrafo; no la fuente de C1).
Entonces `L_PP=a_N-p0_N` y `L_cond=a_N/(1-q_N)-p0_N`. Su diferencia es
`q_N a_N/(1-q_N)`, exactamente (C3.3). Es no negativa siempre que
`q_N<1`, porque `E>=0`; para `q_N=0` se anula. El caso `q_N=1` queda
correctamente excluido por tener éxito nulo; la asintótica C1 garantiza
`q_N<1` para N suficientemente grande.

## 3. Identificación de q_N y definición de B — PASS

`Q U_M phi_N=Q(U_M-I)phi_N` identifica exactamente la fuga de C3 con
la de C1. No se transporta una cota para otra fuente o para otro corte.
La integral ahora escrita de `B=Phi_0(1/4)` coincide con el recurso
radial (7). Su integrando es positivo en `0<k<1`; así `B>0` y `D>0`.

Se comprobó también el coeficiente heredado: el cuadrado del líder de
C1 (2), con medida radial `4 pi k^2 dk/(2 pi)^3`, da
`2048 pi^2 B^2 k^-6 cos^2(k/4) dk`. El término no oscilatorio integra
a `K^-5/10`, y el oscilatorio es `O(K^-6)`. De ahí
`D=1024 pi^2 B^2/5`, `K=sqrt(N)` y (C3.4). La norma `||M down||=1`
vale para los cuatro encoders; la identificación no exige igualar sus
restos a N finito. Se conserva el control de imágenes de C1 §3.2.

## 4. Campo libre, normalización y límite de Bob — PASS

`h_N(y)=(1-16|y-Nu|^2/N^2)_+^2` es exactamente el efecto congelado.
El producto escalar en `ell^2(Z^3;C^2)` usa conteo: no hay un peso
`N^-3` adicional en la definición de `p0_N`. Ese factor procede del
cuadrado del campo, como indica ahora el objeto.

La atribución correcta del campo es el Lema 7.2, no C1. Su argumento
se comprueba además sin usar el Teorema 4.4. Sean
`A=S(q/N)`, `V=exp(-i H_W(q)/N)`, para `|q|<=1`. El símbolo da
`||A-V||<=C/N^2`; ambos son unitarios. La identidad telescópica de
`A^N-V^N` da `||A^N-V^N||<=C/N`, uniformemente. Insertada en la
transformada exacta del recurso resulta

\[
r_N(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),\qquad
R_0(Y)=c_r\int_{|q|\le1}g(q)e^{-iq\cdot Y}
                  e^{-iH_W(q)}\chi\,d^3q,
\]

con `c_r=sqrt(3465)/(64 pi^2)`, `g(q)=(1-|q|^2)_+^2`,
`chi=down`, `H_W(q)=q_1 sigma_1-q_2 sigma_2+q_3 sigma_3`.
La uniformidad no depende de y porque el factor Fourier tiene módulo uno.
La integración angular de esta fórmula reproduce las funciones `I_0,I_1`
del Lema 7.2. Es una comprobación del lema por una segunda vía, sin usar
asintóticas del observable total ni datos numéricos.

En la bola de Bob, `R_0` es acotado; por tanto
`||r_N(y)||^2=N^-3||R_0(y/N)||^2+O(N^-4)`.
Hay `O(N^3)` sitios y `0<=h_N<=1`. Se obtiene explícitamente

\[
p_{0,N}=N^{-3}\sum_{y\in\mathbb Z^3}
 h_N(y)\|R_0(y/N)\|^2+O(N^{-1}).
\]

El sumando, visto como función de `Y=y/N`, es continuo, compacto y nulo
en la frontera; la suma de Riemann converge a (C3.5). No se necesita una
tasa de discretización para concluir el límite usado en (C3.7).

Para la positividad, el integrando Fourier vectorial
`g(q) exp(-i H_W(q)) chi` tiene soporte compacto y no es cero: su norma
es `g(q)>0` en la bola unidad abierta. Su transformada `R_0` es entera
componente a componente. Si la integral no negativa (C3.5) fuera cero,
la continuidad y el peso estrictamente positivo obligarían a `R_0=0`
en la bola abierta de Bob. La unicidad analítica y la inyectividad de
Fourier implicarían que el integrando es cero, contradicción. Así
`p_infty>0`. Como control de normalización, Plancherel y la unitariedad
del multiplicador Weyl dan `integral ||R_0||^2=1`, luego `p_infty<=1`.

## 5. Entrada C2c y corrección de normalización — PASS

Las filas `M=I,sigma_1,sigma_2,sigma_3`, `D_0=I`, están explícitas en
C2c §8. (C16) aplica a cada una. La cota superior de su coeficiente puede
comprobarse sin positividad estricta de Gram: en (C9), la suma finita
queda acotada por `128 beta^2 sum_ij |G_ij|`, independientemente de K.
Las integrales (C8) son finitas en la bola fija y sus denominadores
permanecen separados de cero. Por tanto `L_PP=O(N^-3)` en las cuatro
filas. La cota inferior de (C15) añade `Theta(N^-3)`, como se registra,
pero no es una premisa necesaria del paso C3.

Escribiendo `p0_N=p_infty+epsilon_N`, `epsilon_N->0`, (C3.3) da

\[
\frac{L_{\mathrm{cond},N}-L_{PP,N}}{D p_\infty N^{-5/2}}
=\bigl(1+O(N^{-1/2})\bigr)
 \left(1+\frac{\epsilon_N+L_{PP,N}}{p_\infty}\right)
 \frac1{1-q_N}\longrightarrow1.
\]

No se ha dividido por un coeficiente que pudiera anularse: `D>0` y
`p_infty>0` se controlan por separado. La conclusión es uniforme sobre
la lista finita de cuatro encoders tomando el máximo de las constantes.
La segunda comprobación de §2 confirma el signo de la corrección.

## 6. Resolución de objeciones y alcance — PASS

Quedan resueltas la definición de B, la atribución al Lema 7.2, la
normalización de red, la importación explícita de C2c y la falsa reserva
de cancelación. Se corrigió además la errata que asignaba w al bit cero.
La explicación de Fourier de §4 hace explícita la positividad que Claude
había reconstruido. Se leyó la revisión independiente de C2c que faltaba
en los paquetes previos. No se usa una etiqueta PASS como prueba algebraica.

`O(N^-3)` no es falso por existir una cota `Theta(N^-3)` más fuerte.
Tampoco hay una obligación matemática de importar la cota inferior:
la petición de auditar (C15)–(C16) no la convierte en necesaria para C3.
Queda así resuelta la divergencia no cerrada del debate degradado.

`L_PP=o(N^-5/2)` impide una cancelación a ese orden. Mantener el líder
de `L_cond` fuera del dictamen responde al perímetro contractual; no
expresa indeterminación matemática producida por cancelación. No se
amplía aquí el contrato ni se emite un nuevo resultado para ese líder,
la señal total L, detectores de rango uno o protocolos locales.

## 7. Dictamen y límite de cierre

| Obligación contractual | Dictamen interno |
| --- | --- |
| 1. Estados condicionados e identidades | PASS |
| 2. Probabilidades y aplicación de C1 | PASS |
| 3. Límite y positividad de p0_N | PASS |
| 4. Corrección (C3.7), cuatro encoders, detector I | PASS |
| 5. Respeto del perímetro | PASS, con OPEN entendido como estado contractual |

Revisión matemática interna completa; no quedan reparaciones exigidas por
esta revisión. No se ejecutaron simulaciones, cuadraturas ni verificadores
simbólicos. Los cálculos analíticos conservados están escritos en esta acta.
No se declara consenso con Claude ni se sustituye su turno fallido.
La aceptación independiente y la promoción canónica siguen pendientes;
`state/CURRENT_STATE.md` no se modifica. No se añade un requisito de que
el revisor independiente deba ser específicamente Claude.
