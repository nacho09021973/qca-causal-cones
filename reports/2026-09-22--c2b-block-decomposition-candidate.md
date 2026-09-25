# C2b: derivación del candidato \(+1:+1:-2\)

Fecha: 2026-09-22. Contrato:
[IR_C2B_BLOCK_DECOMPOSITION_GATE](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md).
**Estado: CANDIDATE_LEMMA_WRITTEN / INDEPENDENT_REVIEW_PENDING.**

Autor: Claude Opus 5 (`claude-opus-5`) en Claude Code, la misma sesión que
revisó C2a. La identidad se propuso en el chat antes de congelar el contrato,
que así lo declara; aquí sólo se pone por escrito. No se ha ejecutado código
ni se ha hecho ningún cálculo numérico. No se modifica el estado canónico.

Notación: la del contrato. Par \(\sigma_2/I\), \(P=1_{|p|\le N^{-1/2}}\),
\(Q=I-P\), \(E=h_N\otimes I\).

## 1. Bloques exactos

Como \(P\phi=\phi\), se tiene \(Q\phi=0\), \(w=Pv=\phi+Pa\) y
\(t=Qv=Qa\). Entonces:

- \(P\Delta P=|w\rangle\langle w|-|\phi\rangle\langle\phi|\);
- \(P\Delta Q=|w\rangle\langle t|-|P\phi\rangle\langle Q\phi|=|w\rangle\langle t|\);
- \(Q\Delta P=|t\rangle\langle w|\);
- \(Q\Delta Q=|t\rangle\langle t|\).

\(S^N\) conmuta con \(P\) y con \(Q\), y \(S^Nw=r+d_P\). Por tanto
\[
L_{PP}=\mathrm{Lin}_N+\mathcal Q_N,\quad
L_{PQ}=\langle d_Q,E(r+d_P)\rangle,\quad
L_{QP}=\overline{L_{PQ}},\quad
L_{QQ}=\langle d_Q,Ed_Q\rangle.
\]
La suma de los cuatro bloques es \(L\) de forma idéntica. Sólo se usa como
comprobación de consistencia.

## 2. Identidad crítica

\[
d_Q=S^NQa=S^Na-S^NPa=d-d_P .
\]
Es exacta: sólo usa \(Q=I-P\) y la linealidad de \(S^N\).

## 3. Localidad: \(d\) es exponencialmente pequeño en Bob

- \(U_M-I\) actúa como cero fuera de \(\mathcal A_N\), luego
  \(\operatorname{supp}a\subset\mathcal A_N\) y \(\|a\|\le\|U_M-I\|\le2\).
- \(E=P_{\mathcal B_N}EP_{\mathcal B_N}\) y \(0\le E\le I\).

De ahí
\[
\|E^{1/2}d\|=\|E^{1/2}P_{\mathcal B_N}S^NP_{\mathcal A_N}a\|\le T_N\|a\|\le2T_N,
\qquad T_N\le9N^4e^{-JN}\quad(N\ge2,\ \text{Teorema 4.1}).
\]
Es decir, dentro del soporte de Bob \(d_Q=-d_P+\varepsilon_N\) con
\(\varepsilon_N=d\). Del problema no proyectado sólo se usa esta cota
superior: no se usan \(L-L_{PP}\) ni el Teorema 4.4.

## 4. Sustitución con errores explícitos

Por Cauchy–Schwarz para la forma positiva \(E\):
- \(\|E^{1/2}r\|\le1\);
- \(\|E^{1/2}d_P\|\le\|Pa\|\le2\).

Sustituyendo:
\[
L_{QQ}-\mathcal Q_N=-2\operatorname{Re}\langle d_P,Ed\rangle+\langle d,Ed\rangle,
\qquad |L_{QQ}-\mathcal Q_N|\le8T_N+4T_N^2,
\]
\[
L_{PQ}=-\langle d_P,Er\rangle-\mathcal Q_N+\langle d,Er\rangle+\langle d,Ed_P\rangle,
\qquad |L_{PQ}+\langle d_P,Er\rangle+\mathcal Q_N|\le6T_N,
\]
\[
|L_{PQ}+L_{QP}+\mathrm{Lin}_N+2\mathcal Q_N|\le12T_N .
\]
Estas cotas valen para todo \(N\ge2\). No son numéricamente útiles hasta
\(N\gtrsim500\), donde \(9N^4e^{-JN}\) baja de \(N^{-3}\). Asintóticamente,
\(T_N=o(N^{-k})\) para todo \(k\).

## 5. Patrón asintótico (usa C2a)

C2a establece por separado:
- \(\mathrm{Lin}_N=O(N^{-7/2})\): término lineal de referencia (11) más la
  transferencia lineal (16)–(20);
- \(\mathcal Q_N=N^{-3}A_N+O(N^{-13/4})\): secciones 3.2 y 5.

Con la sección 4:

| Bloque | Líder | Resto |
| --- | --- | --- |
| \(L_{PP}\) | \(+N^{-3}A_N\) | \(O(N^{-13/4})\) |
| \(L_{QQ}\) | \(+N^{-3}A_N\) | \(O(N^{-13/4})\) |
| \(L_{PQ}+L_{QP}\) | \(-2N^{-3}A_N\) | \(O(N^{-13/4})\) |

\(A_N\ge\mathcal C_0-\mathcal C_1>0\). Hay dos comprobaciones de
consistencia, ninguna usada como prueba:
- los líderes suman cero, compatible con \(|L|\le36N^4e^{-JN}\);
- \(L_{QQ}\ge0\) se cumple, porque \(E\ge0\).

**Secundario (B4′).** Si C2a controla el emparejamiento complejo,
\(|\langle r,Ed_P\rangle|=O(N^{-7/2})\), entonces cada coherencia por
separado vale \(L_{PQ}=\overline{L_{QP}}=-N^{-3}A_N+O(N^{-13/4})\). Las
estimaciones (11) y (16)–(20) de C2a se escriben para integrales complejas
acotadas en valor absoluto, pero el enunciado revisado habla de
\(2\operatorname{Re}\). La revisión debe decidir B4′ aparte.

## 6. Lo que este candidato no afirma

- No afirma que la identidad sea la explicación estructural completa ni fija
  su alcance sobre los 16 pares; eso corresponde a C2c. Los pasos 1–4 no usan
  \(\sigma_2/I\), pero su generalidad no forma parte de este gate.
- No es una lectura física de las coherencias. El mecanismo candidato es que
  el corte duro da a \(Pa\) una cola no local, y como \(a\) es local y
  \(S^N\) causal, \(Qa\) la compensa en Bob. Es una propiedad de la
  descomposición espectral, no transporte local.
- No es novedad bibliográfica ni un protocolo condicionado.

**Estado: candidato escrito; pendiente de revisión independiente.** Queda
fuera del estado canónico hasta que pase la revisión.
