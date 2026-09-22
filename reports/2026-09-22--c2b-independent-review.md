# C2b: revisión matemática independiente y adversarial

Fecha: 2026-09-22. Revisor: Codex, agente `/root`, distinto del autor del
candidato (Claude Opus 5). Revisión analítica de un agente; no es revisión
humana, consenso de varios miembros ni formalización de C2b.

## 1. VERDICT

**Veredicto principal: `C2B_PASS`.**

**Veredicto secundario: `B4_PRIME_PASS`.**

B1–B4 están demostrados bajo el contrato congelado, para el par
\(M=\sigma_2, M_B=I\). No se requieren reparaciones. El líder opuesto al
de PP se localiza mediante la expansión directa en las coherencias:
\(PP:QQ:(PQ+QP)=+1:+1:-2\). No se infiere ningún bloque restando PP
del observable total.

B4′ pasa porque las estimaciones escritas de C2a controlan el
emparejamiento complejo completo. No se deduce ese control de una cota
de su parte real. La sección 8 identifica los pasos precisos que lo
justifican. B4 no depende de esta conclusión secundaria.

## 2. SNAPSHOT REVIEWED

Único snapshot científico revisado:

- Rama: `research/b-infinity-post-s4-gate`.
- Commit: `19eb7a383cbb09464e91b64e89f724204e58cccb`.
- Clasificación: **`POST-DISCOVERY VERIFICATION GATE`**. El candidato
  precedió al contrato; no se trata de una preregistración de la hipótesis.

Las entradas se leyeron mediante `git show <commit>:<ruta>`. La rama y
HEAD locales coincidían con los indicados. No había diferencias de
archivos versionados frente a ese commit. El archivo no versionado
`reports/2026-09-21--roadmap-corona-causal-uv-ir.md`, presente al comenzar,
no se utilizó como evidencia ni se modificó. Ningún contenido posterior
al snapshot entra en las conclusiones.

Identificación de las siete entradas obligatorias por objeto Git:

| Entrada | Blob en el snapshot |
| --- | --- |
| [Contrato C2b](../theory/IR_C2B_BLOCK_DECOMPOSITION_GATE.md) | `d304e4581d97cf9ed82cca763f29451386cceb08` |
| [Candidato C2b](2026-09-22--c2b-block-decomposition-candidate.md) | `840c94cf52438cdd6235279cef34298ed7402fbb` |
| [Revisión C2a](2026-09-22--c2a-independent-review.md) | `d50b6a9682ede3d813ed1b6e8b605857dd255357` |
| [Derivación C2a](2026-09-22--c2a-oscillatory-transfer.md) | `65732ccc96aec18239fbd5bfec3856dfe6c999cf` |
| [Contrato C2a](../theory/IR_C2A_OSCILLATORY_TRANSFER_GATE.md) | `b5c78fd9cc611c6a04b886c7f5734fed99ee7d51` |
| [Contrato C1/C2/C3](../theory/IR_ATTRIBUTION_C1_C2_C3_GATE.md) | `3910337cf5bed50a818c9d4fbe29f57d1281623a` |
| [CURRENT_STATE](../state/CURRENT_STATE.md), especialmente §10.1 | `188ec590e664089ea578078ef8db0df67a3cc902` |

Dependencias consultadas en el mismo commit:

- [Manuscrito](../papers/ir-corona/ir-corona.md), §§2–3, Teorema 4.1 y
  §§5.1–5.2; contrastados con la
  [fuente TeX](../papers/ir-corona/ir-corona.tex).
- [Representación C2](2026-09-22--c2-projected-response-representation.md),
  especialmente §§1–4.
- [Fuente y fuga C1](2026-09-22--ir-projection-leakage-and-conditioning.md),
  §§2–3 y 5, y su
  [revisión independiente](2026-09-22--c1-leakage-independent-review.md).
- [Alcance de la formalización](../formal/README.md) y las definiciones de
  regiones y el enunciado `TN_bound` en
  [Theorem41.lean](../formal/QcaFormal/Theorem41.lean).

También se leyeron las instrucciones de trabajo aplicables. No se ejecutó
ningún cálculo científico, simulación, cuadratura, barrido, certificado ni
compilación Lean. Las comprobaciones matemáticas siguientes son analíticas
sobre las fórmulas del snapshot. Las inspecciones Git son de provenance.

## 3. CLAIMS REVIEWED

Se trabaja en \(\ell^2(\mathbb Z^3;\mathbb C^2)\), con producto interno
antilineal en el primer argumento. Todos los vectores y operadores llevan
la dependencia en \(N\) del contrato, aunque se suprima el subíndice.

\[
P=1_{|p|\le N^{-1/2}}I_2,\quad Q=I-P,\quad
a=(U_M-I)\phi_N,\quad v=U_M\phi_N,
\]
\[
r=S^N\phi_N,\quad d=S^Na,\quad d_P=S^NPa,\quad d_Q=S^NQa,
\qquad E=h_N\otimes I.
\]

\(P,Q\) son proyectores ortogonales complementarios; no son los
proyectores de las dos bandas de Weyl. \(P_{\mathcal A_N}\) y
\(P_{\mathcal B_N}\) serán exclusivamente las restricciones espaciales.

| Afirmación | Resultado de la revisión |
| --- | --- |
| B1: identidad exacta | Demostrada |
| B2: los cuatro bloques del observable firmado | Demostrados |
| B3: compensación localizada y constantes \(8,4,12\) | Demostradas para todo entero \(N\ge2\) |
| B4: patrón principal y restos | Demostrado cuando \(N\to\infty\) por enteros |
| B4′: coherencias individuales | Demostradas, con control complejo explícitamente auditado |

El estado de partida es C1 PASS, C2a PASS para \(\sigma_2/I\), C2b
OPEN/UNBLOCKED, C2c BLOCKED ON C2b, C3 SEPARATE y E/AdS FROZEN.

## 4. B1 — EXACT IDENTITY

Para cada \(N\) fijo, por linealidad de la evolución acotada,

\[
d_Q=S^N(I-P)a=S^Na-S^NPa=d-d_P.
\]

El signo negativo es exacto. **Esta igualdad sólo necesita \(Q=I-P\)
y linealidad**; no necesita conmutación, localidad ni un límite asintótico.
La hipótesis adicional \([S,P]=0\) sí está disponible: en Fourier,
\(S(p)\) es el símbolo matricial homogéneo del manuscrito, mientras que
\(P(p)\) es un multiplicador escalar por \(I_2\). Por ello
\([S^N,P]=[S^N,Q]=0\), y \(d_P=Pd\), \(d_Q=Qd\).

El recurso tiene soporte de Fourier en \(|p|\le N^{-1}\), contenido
en \(|p|\le N^{-1/2}\) para todo \(N\ge2\). Así
\(P\phi_N=\phi_N\), \(Q\phi_N=0\) y \(Pr=r\). El borde de la bola
no introduce un término adicional: son igualdades de multiplicadores en
\(L^2\), con el mismo corte duro del contrato.

## 5. B2 — EXACT BLOCK DECOMPOSITION

El observable original del manuscrito §3.3 es la diferencia firmada

\[
L=\langle S^Nv,ES^Nv\rangle-\langle r,Er\rangle
 =\operatorname{tr}(ES^N\Delta S^{-N}),
\quad \Delta=|v\rangle\langle v|-|\phi_N\rangle\langle\phi_N|.
\]

Se usa \(S^{-N}=(S^N)^\dagger\), por unitariedad. Todos los operadores
de rango uno que aparecen son de clase traza y \(E\) es acotado, de modo
que las trazas están bien definidas. Insertar \(I=P+Q\) a ambos lados
de \(\Delta\) produce exactamente cuatro sumandos
\(L_{XY}=\operatorname{tr}(ES^NX\Delta YS^{-N})\).

Poniendo \(w=Pv=\phi_N+Pa\) y \(t=Qv=Qa\), se obtiene directamente:

\[
\begin{aligned}
P\Delta P&=|w\rangle\langle w|-|\phi_N\rangle\langle\phi_N|,\\
P\Delta Q&=|w\rangle\langle t|,\\
Q\Delta P&=|t\rangle\langle w|,\\
Q\Delta Q&=|t\rangle\langle t|.
\end{aligned}
\]

Los tres últimos términos de referencia son exactamente cero porque
\(Q\phi_N=0\), no porque sean pequeños. Como
\(S^Nw=r+d_P\), \(S^Nt=d_Q\) y
\(\operatorname{tr}(E|x\rangle\langle y|)=\langle y,Ex\rangle\),

\[
\begin{aligned}
L_{PP}&=\langle r+d_P,E(r+d_P)\rangle-\langle r,Er\rangle\\
 &=2\operatorname{Re}\langle r,Ed_P\rangle+\langle d_P,Ed_P\rangle
 =\mathrm{Lin}_N+\mathcal Q_N,\\
L_{PQ}&=\langle d_Q,E(r+d_P)\rangle,\\
L_{QP}&=\langle r+d_P,Ed_Q\rangle=\overline{L_{PQ}},\\
L_{QQ}&=\langle d_Q,Ed_Q\rangle.
\end{aligned}
\]

La conjugación y el factor dos usan \(E=E^\dagger\). En particular,

\[
L_{PQ}+L_{QP}=2\operatorname{Re}\langle d_Q,E(r+d_P)\rangle.
\]

Esta reconstrucción identifica cada bloque antes de sumarlos. No se
deduce una fórmula desconocida exigiendo que la suma dé \(L\). No aparece
normalización condicionada, factor \(1/2\) de distancia traza ni término
\(q_Np0_N\). Aunque \(d_P\perp d_Q\) globalmente, no se puede eliminar
\(\langle d_Q,Ed_P\rangle\): no se dispone de \([E,P]=0\).

Para el efecto congelado, \(E\ge0\); por tanto
\(L_{QQ}=\|E^{1/2}d_Q\|^2\ge0\) exactamente. Esta positividad no se
atribuye a los bloques de coherencia ni al bloque firmado PP.

## 6. B3 — BOB COMPENSATION AND EXPLICIT BOUNDS

### Normalización, soporte y normas

El recurso del manuscrito tiene
\(\hat\phi_N(p)=Z_N^{-1/2}(1-|Np|^2)_+^2\downarrow\), con
\(Z_N=64/(3465\pi^2N^3)\). Con su medida \(d^3p/(2\pi)^3\),

\[
\int_0^1 r^2(1-r^2)^4dr=\frac{128}{3465},\qquad
\int_{\mathbb T^3}|g(Np)|^2\frac{d^3p}{(2\pi)^3}
=\frac{64}{3465\pi^2N^3}=Z_N.
\]

Así \(\|\phi_N\|=1\) exactamente. \(U_M\) es unitario, pues
\(M=\sigma_2\) es hermítico y el perfil es real. Además \(U_M-I\)
se anula fuera de \(\mathcal A_N\). Por tanto

\[
P_{\mathcal A_N}a=a,\qquad \|a\|\le\|U_M-I\|\|\phi_N\|\le2.
\]

**No se normaliza \(a\) a uno.** La localización es la de la
perturbación, no la del recurso \(\phi_N\), que tiene cola espacial.
La unitariedad de \(S\) y la contractividad de \(P,Q\) dan

\[
\|r\|=1,\quad \|d\|=\|a\|\le2,\quad
\|d_P\|\le2,\quad \|d_Q\|\le2.
\]

Incluso \(\|d_Q\|=\|Qv\|\le1\), pero no hace falta mejorar la cota
dos del candidato. Ninguna de estas constantes depende de \(N\).

Como \(0\le h_N\le1\), se tiene
\(0\le E\le I\), \(\|E^{1/2}\|\le1\), y
\(E=P_{\mathcal B_N}EP_{\mathcal B_N}\). En este protocolo
\(E^{1/2}=\sqrt{h_N}\otimes I\), de modo que
\(E^{1/2}=E^{1/2}P_{\mathcal B_N}\). No se invierte \(E\), que puede
anularse; sus ceros en la frontera no son un problema.

### Aplicabilidad y alcance del Teorema 4.1

Se comprobaron el enunciado y la prueba escrita del teorema, no sólo su
referencia. Las regiones son exactamente las bolas de radio \(N/4\)
centradas en \(0\) y \(N(1,1,1)\); la evolución es exactamente el símbolo
CJWW (5.15) del manuscrito durante \(N\) pasos. La estimación es una cota
de operador sobre **cualquier** vector soportado en Alice, sin exigir
limitación espectral de ese vector.

En la prueba de §§5.1–5.2, el desplazamiento de contorno por
\(-i(\log2)(1,1,1)\) es legítimo para el símbolo trigonométrico entero.
La inclusión de elipses y \(\det S=1\) dan radio espectral menor que
cuatro, porque \((\cosh\log2)^3=125/64<17/8=\cosh\log4\).
La suma de normas de los saltos es cuatro y \(|u\cdot d|\le3\), de
donde la norma del símbolo desplazado es a lo sumo 32. La forma de Schur
de una matriz \(2\times2\), incluyendo autovalores coincidentes, da

\[
\|S(\eta-i(\log2)u)^N\|
\le4^N+32N4^{N-1}\le9N4^N.
\]

La geometría \(u\cdot(y-x)\ge(3-\sqrt3/2)N\) proporciona
\(\|G_N(y-x)\|\le9Ne^{-JN}\), con
\(J=(1-\sqrt3/2)\log2>0\). Cada región tiene a lo sumo
\((N/2+1)^3\le N^3\) sitios para todo \(N\ge2\). El paso de núcleo a
operador multiplica por a lo sumo
\(\sqrt{|\mathcal A_N||\mathcal B_N|}\le N^3\), dando

\[
T_N:=\|P_{\mathcal B_N}S^NP_{\mathcal A_N}\|
\le9N^4e^{-JN}\qquad(N\ge2).
\]

La fuente Lean inspeccionada usa las mismas regiones y enuncia una cota
más fuerte con constante cuatro. No se recompiló ni se usa ese dato para
sustituir la comprobación de aplicabilidad anterior. Tampoco se necesita
la identificación de una distancia reducida de Fock.

Ahora, para los objetos exactos de C2b,

\[
E^{1/2}d=E^{1/2}P_{\mathcal B_N}S^NP_{\mathcal A_N}a,
\qquad \|E^{1/2}d\|\le T_N\|a\|\le2T_N.
\]

Se aplica el teorema a \(a\), **no** a \(Pa\) o \(Qa\), que ya no
tienen el soporte requerido. B1 es una identidad global; sólo la pequeñez
de su residuo \(\varepsilon_N=d\) es localizada en Bob. No se afirma
\(\|d\|=O(T_N)\) en todo el espacio.

### Derivación de las constantes explícitas

Escribamos \(x=E^{1/2}d_P\), \(e=E^{1/2}d\) y
\(z=E^{1/2}r\). Se tienen \(\|x\|\le2\), \(\|e\|\le2T_N\),
\(\|z\|\le1\) y \(E^{1/2}d_Q=e-x\).

Primero,

\[
L_{QQ}-\mathcal Q_N
=\|e-x\|^2-\|x\|^2
=-2\operatorname{Re}\langle x,e\rangle+\|e\|^2.
\]

Cauchy–Schwarz da, sin omitir el término cuadrático,

\[
|L_{QQ}-\mathcal Q_N|
\le2\|x\|\|e\|+\|e\|^2
\le2\cdot2\cdot2T_N+(2T_N)^2
=8T_N+4T_N^2.
\]

Segundo, expandiendo el bloque PQ de B2 y sólo después su conjugado,

\[
L_{PQ}=-\langle d_P,Er\rangle-\mathcal Q_N+\eta_N,
\qquad \eta_N=\langle d,Er\rangle+\langle d,Ed_P\rangle.
\]

Cada emparejamiento se escribe con \(E^{1/2}\) en ambos argumentos:

\[
|\eta_N|\le\|e\|\|z\|+\|e\|\|x\|
\le2T_N(1+2)=6T_N.
\]

Como \(2\operatorname{Re}\langle d_P,Er\rangle=\mathrm{Lin}_N\)
y \(\mathcal Q_N\) es real,

\[
L_{PQ}+L_{QP}+\mathrm{Lin}_N+2\mathcal Q_N
=2\operatorname{Re}\eta_N,
\qquad
|L_{PQ}+L_{QP}+\mathrm{Lin}_N+2\mathcal Q_N|\le12T_N.
\]

Las constantes ocho, cuatro y doce quedan derivadas. No aparece un
\(T_N^2\) en la segunda cota porque PQ es lineal en \(d_Q\), y su otro
factor es \(r+d_P\). Todas estas desigualdades valen para todo entero
\(N\ge2\), aunque la cota exponencial pueda ser poco informativa a
\(N\) pequeño. No necesitan \(9N^4e^{-JN}<1\) ni la asintótica de C2a.

## 7. B4 — +1:+1:-2 ASYMPTOTICS

La auditoría de la sección 9 permite importar separadamente

\[
\mathcal Q_N=N^{-3}A_N+O(N^{-13/4}),\qquad
\mathrm{Lin}_N=O(N^{-7/2}),
\quad A_N=\mathcal C_0+\mathcal C_1\cos(\sqrt N/2).
\]

Como \(J>0\) es fijo,

\[
N^{13/4}T_N\le9N^{29/4}e^{-JN}\longrightarrow0,
\qquad
N^{13/4}T_N^2\le81N^{45/4}e^{-2JN}\longrightarrow0.
\]

Además \(N^{-7/2}=o(N^{-13/4})\). Por B2 y B3, sin usar información
sobre la asintótica del observable total,

\[
\boxed{\begin{aligned}
L_{PP}&=+N^{-3}A_N+O(N^{-13/4}),\\
L_{QQ}&=+N^{-3}A_N+O(N^{-13/4}),\\
L_{PQ}+L_{QP}&=-2N^{-3}A_N+O(N^{-13/4}).
\end{aligned}}
\]

Puesto que \(\mathcal C_0>\mathcal C_1>0\), el coeficiente oscila pero
no se anula: \(A_N\ge\mathcal C_0-\mathcal C_1>0\). El patrón
\(+1:+1:-2\) es una equivalencia relativa uniforme respecto de
\(N^{-3}A_N\), con error relativo \(O(N^{-1/4})\), no una elección
de subsecuencias favorables.

En particular,

\[
L_{PP}+L_{QQ}=2N^{-3}A_N+O(N^{-13/4}),
\]

que es positivo para \(N\) suficientemente grande y no se cancela a
escala \(N^{-3}\). La contribución opuesta está en la suma de
coherencias. Esto es una conclusión sobre los bloques del observable
congelado, no una interpretación física adicional.

## 8. B4 PRIME — INDIVIDUAL COHERENCES

Definamos \(\mathfrak c_N=\langle r,Ed_P\rangle\). De B3 se tiene
exactamente

\[
L_{PQ}=-\overline{\mathfrak c_N}-\mathcal Q_N+\eta_N,
\qquad
L_{QP}=-\mathfrak c_N-\mathcal Q_N+\overline{\eta_N},
\quad |\eta_N|\le6T_N.
\]

Una cota de \(2\operatorname{Re}\mathfrak c_N\) no controla por sí sola estos
dos números complejos. Se revisó por ello el argumento que antecede a
(11) de C2a, y no sólo su enunciado:

1. La identidad (10) de C2a es para el emparejamiento complejo
   \(\mathfrak c_N^W=\langle w_0,D_K^W\rangle\), con \(K=\sqrt N\).
   No toma partes reales al sustituir la integral truncada por la cola.
2. En esa cola, los términos principales tienen orden radial
   \(r^{-6}\) antes de integrar ángulos. El lema (6), que vale para
   amplitudes complejas, da una parte principal de orden \(r^{-7}\)
   y un resto \(O(r^{-8})\). Las frecuencias principales
   \(\pm\sqrt3+(\epsilon-\eta)b-\sigma\), con \(b=1/4\), tienen
   módulo al menos \(\gamma=\sqrt3-3/2>0\).
   La integración por partes radial ya escrita en C2a acota
   \(\left|\int_K^\infty r^{-7}e^{i\alpha r}dr\right|\le C K^{-7}\)
   para esas frecuencias. El resto integra absolutamente a
   \(O(K^{-7})\).
3. Los productos subdominantes de (4)–(5) también se acotan en módulo:
   el resto angular uniforme y el carácter radial de la fuente permiten
   la ganancia \(r^{-1}\) de (6), dejando una cola radial
   \(O(r^{-8})\). No hay cancelación exclusiva de la parte real.
4. La identidad de Poisson de §4.1 es para el emparejamiento complejo
   discreto. Sus errores (16), (18), (19), (20) son cotas en módulo,
   respectivamente \(O(K^{-8}),O(K^{-7}),O(K^{-7}),O(K^{-9})\).
   La identidad de soporte (17) es asimismo compleja.

En consecuencia, el argumento ya escrito y auditado da

\[
|\mathfrak c_N^W|=O(K^{-7}),\qquad
|\mathfrak c_N-\mathfrak c_N^W|=O(K^{-7}),
\qquad |\mathfrak c_N|=O(N^{-7/2}).
\]

Esta es una extracción del alcance de las estimaciones existentes, no
una nueva saddle analysis ni una reparación de C2a. La revisión previa
C2a §§3(i), 5 y 6 verifica esos mecanismos; su dictamen final no los
enuncia como un teorema separado sobre \(\mathfrak c_N\). Esta revisión hace
explícita la consecuencia compleja, sin atribuir al dictamen previo un
enunciado que no escribió.

Al sustituir en las dos identidades de bloques,

\[
L_{PQ}=-N^{-3}A_N+O(N^{-13/4}),\qquad
L_{QP}=-N^{-3}A_N+O(N^{-13/4}).
\]

Los restos aquí se acotan en módulo complejo. Las coherencias son
conjugadas exactamente, pero no se afirma que cada una sea real a
\(N\) finito. De hecho, la prueba controla sus partes imaginarias por
\(O(N^{-7/2})+O(T_N)\). Resultado secundario: **B4′ demostrado**.

## 9. C2A DEPENDENCY AUDIT

Se verificó la correspondencia entre los objetos, no sólo la etiqueta
PASS. La representación C2 (2)–(3), recogida en §2 de la revisión C2a,
da exactamente

\[
d_P(y)=N^{-3/2}D_N(y/N),\qquad
r(y)=N^{-3/2}R_N(y/N),
\]
\[
\mathcal Q_N=N^{-3}\sum_yh(y/N)\|D_N(y/N)\|^2,
\qquad
\langle r,Ed_P\rangle
=N^{-3}\sum_yh(y/N)R_N(y/N)^\dagger D_N(y/N).
\]

El factor \(N^{-3}\) y la medida \((2\pi)^{-3}\) proceden de la
misma convención de Fourier del manuscrito. Los interpolantes incluyen
el símbolo exacto \(S(k/N)^N\), todas las imágenes de Alice y el corte
\(|k|\le\sqrt N\). No se cambian recurso, región, detector o
normalización al importar C2a.

| Resultado necesario | Derivación C2a | Revisión C2a que lo comprueba |
| --- | --- | --- |
| Lineal Weyl \(O(K^{-7})\) | §3.1, (10)–(11) | §3(i) y tabla de §5 |
| Error lineal discreto \(O(K^{-7})\) | §§4.1–4.3, (16)–(20) | §§5–6, con imágenes, corrector y recurso separados |
| Cuadrático Weyl \(K^{-6}A_N+O(K^{-7})\) | §3.2, (12)–(15) | §§3(g)–(h), 4 y 5 |
| Error cuadrático \(O(K^{-13/2})\) | §5.1, (21)–(22) | §7 y tabla de §5 |
| Muestreo cuadrático \(O(K^{-8})\) | §5.2, (23) | §5, fila de muestreo cuadrático |

En particular, el error de campo \(O(K^{-7/2})\) se aplica sólo a la
forma cuadrática, contra una referencia localizada de norma
\(O(K^{-3})\). Su producto es \(O(K^{-13/2})\) y el cuadrado del
error es \(O(K^{-7})\). El muestreo añade \(O(K^{-8})\). Así

\[
\mathcal Q_N=K^{-6}A_N+O(K^{-13/2}),
\quad \mathrm{Lin}_N=O(K^{-7}),
\]

**por separado**. No se resta una estimación de la suma para intentar
probar una de sus partes. Las constantes son uniformes para \(N\)
grande: la geometría escalada y \(\gamma>0\) son fijas, los recursos
tienen soporte de Fourier fijo y normas de derivadas uniformes, y los
aliases y errores de muestreo están incluidos en el presupuesto.

La separación \(\mathcal C_0>\mathcal C_1>0\) procede de C2a (14)–(15)
y la revisión §4: los denominadores \(\rho+\sigma\pm b\) son positivos
en Bob; los pesos \(h\nu_\sigma/\rho^2\) son no negativos;
\(\nu_++\nu_-=1\); y la diferencia de coeficientes integra
\((t_{\sigma,+}-t_{\sigma,-})^2\) con peso positivo en el interior.
\(\Phi_0(b)>0\) está justificado por la integral positiva del recurso
en C1. No se necesita una evaluación decimal de esos coeficientes.

La revisión C2a excluye expresamente de su PASS la sección 7 de la
derivación, ecuaciones (24)–(25), que trata el residuo y usa la ley total.
Esa sección tampoco es una entrada de esta prueba. La dependencia
aceptada termina en los presupuestos independientes de §§3–6 de C2a.

## 10. AUTONOMY CHECK

La cadena de prueba empleada es

\[
\begin{gathered}
\Delta,\ P\phi_N=\phi_N\ \longrightarrow\
\text{cuatro bloques exactos},\\
Q=I-P\ \longrightarrow\ d_Q=d-d_P,\\
\operatorname{supp}a\subset\mathcal A_N,\ \text{Teorema 4.1}
\ \longrightarrow\ \|E^{1/2}d\|\le2T_N,\\
\text{sustitución en QQ y PQ/QP}\ \longrightarrow\ \text{cotas B3},\\
\text{C2a lineal y cuadrático separados}\ \longrightarrow\ +1:+1:-2.
\end{gathered}
\]

No se usaron \(L-L_{PP}\), el Teorema 4.4, la ley asintótica de \(L\),
los diagnósticos \(N=24,40\), un nuevo cálculo numérico ni una nueva
aproximación de saddle. Las consecuencias de C1 o C2a que citan la ley
total se excluyen. El Teorema 4.1 entra únicamente a través de su cota
de operador \(T_N\).

La igualdad \(L=\sum_{X,Y}L_{XY}\) se reconstruyó por linealidad de la
traza para comprobar la identificación del observable. No se utilizó
para despejar ningún bloque. Tampoco fue necesario usar
\(L-L_{PP}\) como comprobación posterior de consistencia.

## 11. FAILURE SEARCH

| Intento de ruptura | Comprobación y resultado |
| --- | --- |
| Signo erróneo en B1 | \(S^N(I-P)a=d-d_P\): signo negativo forzado |
| Conmutación ausente | \(P\) es un multiplicador escalar y \(S\) matricial; conmutan. B1 ni siquiera requiere esa hipótesis |
| Referencia omitida en QQ o PQ | \(Q\phi_N=0\) exactamente por inclusión de soportes espectrales |
| PQ y QP intercambiados o sin conjugación | La identidad de traza de rango uno fija el orden; \(E=E^\dagger\) da conjugación |
| Factor dos o signo lineal incorrectos | La suma da \(-2\operatorname{Re}\langle d_P,Er\rangle-2\mathcal Q_N+2\operatorname{Re}\eta_N\) |
| Ortogonalidad global usada dentro de Bob | No: \(E\) no conmuta necesariamente con \(P\); las coherencias se retienen |
| Positividad aplicada a un observable firmado | Sólo \(E\), \(\mathcal Q_N\) y QQ son positivos; PP conserva la resta de referencia |
| Raíz cuadrada injustificada | \(E=\sqrt{h_N}^{\,2}\otimes I\), \(0\le E\le I\), soporte en Bob; no se divide por \(h_N\) |
| Fuente normalizada artificialmente | Se usa \(\|\phi_N\|=1\) y \(\|a\|\le2\), no \(\|a\|=1\) |
| Teorema 4.1 aplicado a una fuente no local | Se aplica sólo a \(a\), nunca a \(Pa\), \(Qa\) o \(\phi_N\) |
| Normas o constantes crecientes con \(N\) | Las normas de vectores se controlan por unitariedad y contracciones, sin contar sitios; el factor regional \(N^3\) ya está en \(T_N\) |
| Constantes 8, 4, 12 no uniformes | Derivadas en §6 para todo \(N\ge2\), sin condición asintótica adicional |
| C2a sólo demuestra una suma | Sus pruebas lineal y cuadrática, y sus presupuestos de transferencia, están separados (§9) |
| Parte imaginaria grande oculta | Se comprobaron las cotas complejas anteriores a tomar \(2\operatorname{Re}\) (§8) |
| Exponencial insuficiente o \(J\) variable | \(J=(1-\sqrt3/2)\log2>0\) fijo; los dos cocientes explícitos de §7 tienden a cero |
| Ceros de \(A_N\) | \(A_N\ge\mathcal C_0-\mathcal C_1>0\) sin subsecuencias |
| Circularidad o dependencia numérica oculta | Se excluyen C2a §7, Teorema 4.4 y los datos retenidos; ninguna ecuación de esta prueba los necesita |

No se encontró un defecto que invalide B1–B4 ni B4′. Dos precisiones de
alcance no constituyen reparaciones: la pequeñez de \(d\) es localizada,
y el control complejo de B4′ se obtiene del argumento de C2a, no de su
enunciado reducido a la parte real. La indicación informal del candidato
sobre un umbral numérico de utilidad de la cota no se certifica ni se usa.

## 12. STRUCTURAL INTERPRETATION

**Identidad algebraica.** La perturbación \(a\) tiene soporte en Alice
y satisface \(a=Pa+Qa\). El proyector duro es espacialmente no local.
Para esta fuente no nula de soporte finito, \(Pa\) no puede tener
soporte finito: en tal caso su transformada sería un polinomio
trigonométrico que se anula en el abierto exterior a la banda, por lo
que sería idénticamente cero; a su vez esto obligaría a que
\(\hat a\) se anulara en el abierto interior, y por analiticidad a
\(a=0\). Se contradice \(a(0)\ne0\). Fuera de Alice,
\(Qa=-Pa\) exactamente, por lo que Qa tampoco tiene soporte finito.

**Estimación localizada.** Tras evolucionar, la formulación demostrada
de la compensación es

\[
\|E^{1/2}(d_Q+d_P)\|\le2T_N.
\]

No es una igualdad aproximada en norma global. De C2a,
\(\|E^{1/2}d_P\|^2=\mathcal Q_N=\Theta(N^{-3})\), de modo que
la suma de las amplitudes localizadas es exponencialmente menor que
cada contribución proyectada a escala algebraica. Al cuadrar,
\(\|-x\|^2=\|x\|^2\) y el término cruzado es
\(2\operatorname{Re}\langle-x,x\rangle=-2\|x\|^2\).
El emparejamiento con \(r\) queda en el orden menor probado por C2a.
Esto justifica matemáticamente la lectura cuadrática del patrón.

**Interpretación física limitada.** La localidad de \(a\), junto con
la cota de propagación del walk y la geometría concretos, explica por
qué las dos componentes proyectadas deben compensarse en Bob. La
causalidad de rango finito por sí sola no daría la cota exponencial en
esta región: se ha usado el Teorema 4.1 del modelo congelado. No se
identifica el corte duro con una operación física local ni sus colas
con transporte local desde Alice. Las coherencias son sumandos de la
descomposición del observable, no probabilidades independientes.

Esta lectura matemática es compatible con la explicación propuesta;
su desarrollo físico, generalidad y evaluación como explicación
estructural completa siguen reservados a C2c.

## 13. LIMITATIONS

- La conclusión asintótica se restringe al par \(\sigma_2/I\), el recurso,
  perfiles, regiones, nodo, dimensión interna, símbolo y corte congelados.
  No se promueve una extensión a los dieciséis pares.
- B3 es válido para todo entero \(N\ge2\); B4 y B4′ son asintóticos,
  con constantes de resto y umbral no explícitos heredados de C2a.
  No se fija el signo de PP o de las coherencias a un \(N\) pequeño.
- Los restos algebraicos no resuelven una contribución exponencial
  subdominante de cada bloque. No se recalcula ni recertifica la ley
  completa del observable total.
- No se afirma novedad, atribución exclusivamente UV, protocolo
  condicionado, transporte físico local del proyector o violación de
  microcausalidad. C3 y E/AdS no entran en la prueba.
- Esta es una revisión independiente de agente. La inspección de una
  formalización previa no constituye una nueva ejecución de Lean ni una
  formalización de los pasos de C2b.

## 14. STATE CONSEQUENCE

La única promoción recomendada por este dictamen es

\[
\boxed{\mathrm{C2b}=\mathrm{PASS}}.
\]

Se registra por separado que B4′ también pasa. C1 y C2a conservan su
PASS y alcance. La dependencia matemática de C2c respecto de C2b queda
satisfecha: puede considerarse **UNBLOCKED para una revisión separada**,
pero no se le asigna PASS, no se ejecuta C2c ni se promueve su explicación
física. C3 continúa SEPARATE y E/AdS FROZEN.

No se modifica `state/CURRENT_STATE.md`, el contrato, el candidato, la
revisión C2a ni el manuscrito. Este informe es el único archivo nuevo de
la tarea; no hay commit ni push.
