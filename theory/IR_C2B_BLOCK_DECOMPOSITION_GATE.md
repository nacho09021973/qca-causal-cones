# C2b — descomposición por bloques PP / QQ / PQ / QP

Fecha: 2026-09-22. Autorización: decisión explícita del usuario después del
PASS de C2a.

**Status: `POST-DISCOVERY VERIFICATION GATE`.**

**Provenance.** El patrón candidato \(+1:+1:-2\) y su derivación los propuso
Claude (sesión de Claude Code, la misma que revisó C2a) en el chat del
2026-09-22, **antes** de congelar este contrato. Este documento **no es una
preregistración de la hipótesis**. Su función es fijar el candidato y los
criterios de revisión independiente, e impedir cambios posteriores de
objetivo. La derivación del autor está en
[el informe del candidato](../reports/2026-09-22--c2b-block-decomposition-candidate.md).
El revisor debe ser independiente del autor de ese informe.

Antecedentes: [contrato C1/C2/C3](IR_ATTRIBUTION_C1_C2_C3_GATE.md),
[contrato C2a](IR_C2A_OSCILLATORY_TRANSFER_GATE.md),
[derivación C2a](../reports/2026-09-22--c2a-oscillatory-transfer.md) y
[revisión independiente C2a, PASS](../reports/2026-09-22--c2a-independent-review.md).

## Objetos fijos

- El par congelado es \(M=\sigma_2\), \(M_B=I\), con el símbolo CJWW (5.15),
  dimensión interna dos, nodo cero, y el recurso, las regiones
  \(\mathcal A_N,\mathcal B_N\) y los perfiles originales.
- \(P=1_{|p|\le N^{-1/2}}\) es el corte duro, sin suavizar; \(Q=I-P\);
  \(E=h_N\otimes I\).
- Vectores:
  - \(a=(U_M-I)\phi_N\);
  - \(v=U_M\phi_N=\phi_N+a\);
  - \(w=Pv\) y \(t=Qv=Qa\);
  - \(r=S^N\phi_N\) y \(d=S^Na\);
  - \(d_P=S^NPa\) y \(d_Q=S^NQa\).
- \(\Delta=|v\rangle\langle v|-|\phi_N\rangle\langle\phi_N|\) y
  \(L_{XY}=\operatorname{tr}(E\,S^N X\Delta Y\,S^{-N})\) para
  \(X,Y\in\{P,Q\}\).
- \(\mathrm{Lin}_N=2\operatorname{Re}\langle r,Ed_P\rangle\) y
  \(\mathcal Q_N=\langle d_P,Ed_P\rangle\), de modo que
  \(L_{PP}=\mathrm{Lin}_N+\mathcal Q_N\).
- \(T_N=\|P_{\mathcal B_N}S^NP_{\mathcal A_N}\|\) es la cantidad del Teorema
  4.1 del manuscrito, y \(A_N=\mathcal C_0+\mathcal C_1\cos(\sqrt N/2)\) es
  el coeficiente de C2a.

## Candidato congelado

**(B1) Identidad crítica, exacta:** \(d_Q=d-d_P\).

**(B2) Bloques, exactos:**
\[
L_{QQ}=\langle d_Q,Ed_Q\rangle,\qquad
L_{PQ}=\langle d_Q,E(r+d_P)\rangle,\qquad
L_{QP}=\overline{L_{PQ}}.
\]

**(B3) Localidad.** Dentro del soporte de Bob,
\(d_Q=-d_P+\varepsilon_N\) con \(\varepsilon_N=d\) y
\(\|E^{1/2}\varepsilon_N\|\le T_N\|a\|\le2T_N\). En consecuencia, para todo
\(N\ge2\):
\[
|L_{QQ}-\mathcal Q_N|\le8T_N+4T_N^2,\qquad
|L_{PQ}+L_{QP}+\mathrm{Lin}_N+2\mathcal Q_N|\le12T_N,
\]
con \(T_N\le9N^4e^{-JN}\).

**(B4) Patrón asintótico.** Se usan de C2a sus dos afirmaciones separadas,
\(\mathrm{Lin}_N=O(N^{-7/2})\) y
\(\mathcal Q_N=N^{-3}A_N+O(N^{-13/4})\):
\[
\begin{aligned}
L_{PP}&=+N^{-3}A_N+O(N^{-13/4}),\\
L_{QQ}&=+N^{-3}A_N+O(N^{-13/4}),\\
L_{PQ}+L_{QP}&=-2N^{-3}A_N+O(N^{-13/4}).
\end{aligned}
\]

**(B4′) Secundario.** Individualmente,
\(L_{PQ}=\overline{L_{QP}}=-N^{-3}A_N+O(N^{-13/4})\). Esto exige que C2a
controle el emparejamiento complejo, \(|\langle r,Ed_P\rangle|=O(N^{-7/2})\),
y no sólo su parte real. Si la revisión encuentra que sólo la parte real
está cubierta, B4′ queda `OPEN` y B4 no se ve afectado.

## Entradas permitidas y prohibidas

Entradas permitidas:

- identidades exactas;
- el Teorema 4.1, formalizado en Lean, usado **sólo** como cota superior de
  \(T_N\);
- las afirmaciones separadas, lineal y cuadrática, del PASS de C2a.

Queda prohibido usar como demostración:

- \(L-L_{PP}\);
- la ley total del Teorema 4.4;
- los valores numéricos N=24/40;
- cualquier cálculo, cuadratura o barrido nuevo.

Dos comprobaciones de consistencia están permitidas sin valor de prueba:
que la suma de los cuatro bloques sea \(L\), y que \(L_{QQ}\ge0\) porque
\(E\ge0\). No se cambia el observable ni se suaviza \(P\).

## Obligaciones de la revisión

1. Reconstruir los cuatro bloques a partir de \(\Delta\) con
   \(P\phi_N=\phi_N\), \(Q\phi_N=0\) y \([S,P]=0\). En particular, comprobar
   que \(P\Delta Q=|w\rangle\langle t|\) no tiene término en \(\phi_N\).
2. Reconstruir \(d_Q=d-d_P\).
3. Verificar la cota de \(\varepsilon_N\): \(\operatorname{supp}a\subset\mathcal A_N\),
   \(E=P_{\mathcal B_N}EP_{\mathcal B_N}\), \(0\le E\le I\) y \(\|a\|\le2\).
   Comprobar además que \(T_N\), las regiones y las hipótesis del Teorema
   4.1 son exactamente las del protocolo.
4. Verificar que el PASS de C2a cubre \(\mathrm{Lin}_N\) y \(\mathcal Q_N\)
   **por separado** con los órdenes indicados, no sólo su suma.
5. Recalcular las constantes de (B3) y los coeficientes \(+1,+1,-2\) de
   (B4), y comprobar que \(T_N=o(N^{-13/4})\).
6. Decidir B4′ por separado.
7. Confirmar que no se usan ni \(L-L_{PP}\) ni el Teorema 4.4.

## Veredictos

- `PASS`: B1–B4 aceptados; B4′ se registra aparte como `PASS` u `OPEN`.
- `REPAIR_REQUIRED`: hay un hueco reparable. Se identifica, sin cambiar el
  candidato.
- `FAIL`: un error invalida el patrón.
- `INCOMPLETE`: la revisión no se completa.

Una revisión es una sola revisión. Un PASS de C2b no es consenso de varios
miembros, revisión humana externa ni promoción del resultado al estado
canónico sin decisión explícita.

## Qué no decide C2b

Queda reservado a C2c, que sigue `BLOCKED ON C2b`:

- si esta identidad es la explicación estructural;
- su alcance sobre los 16 pares;
- qué parte de la escala \(N^{-3}\) depende específicamente de
  \(\sigma_2/I\);
- cualquier lectura física de las coherencias.

C2b no afirma transporte local físico, novedad bibliográfica ni un
protocolo condicionado.

## Límites

C1 y C2a conservan su PASS; C3 sigue separado; E/AdS queda congelado. No hay
cálculos nuevos antes de la revisión. No hay commit ni push sin instrucción
del usuario. `state/CURRENT_STATE.md` registra C2b sólo como `OPEN/UNBLOCKED`;
el candidato no entra allí como hecho hasta que pase la revisión.
