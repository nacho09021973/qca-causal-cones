---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-24 17:00
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-09-24--two-channel-t1-review-request.md
rondas: 1
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - CLAUDE OPUS — Claude (Anthropic) — claude -p --model claude-opus-5 --effort high (sellado)
  - GEMINI — Google — generativelanguage.googleapis.com/gemini-3.1-pro-preview
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Revisión independiente adversarial de T1: dos canales y P/Q inclinado

Fecha: 2026-09-24. Autor de T1: Codex (familia OpenAI).
Encargo del usuario: T1 → revisión independiente → T2 → T3.
Esta sesión ejecuta únicamente la revisión de T1.

## Pregunta y límite

¿Es exacta y bien definida la descomposición firmada de T1 para el
contrato TWO_DISTINGUISHABLE_CHANNELS y el P/Q auxiliar ya existente?
Intentad refutarla mediante un error de dominio, peso, adjunto, fuente,
referencia física, recurrencia o caso límite. No basta aprobar la
expansión elemental de una forma cuadrática: revisad su lift inclinado.

Revisores solicitados: Claude Opus (Anthropic) y Gemini (Google), ambos
distintos de la familia autora. Esto es una revisión externa al autor
por agentes, no una revisión humana. El protocolo es deliberativo:
los turnos posteriores ven los anteriores; no se afirmará que sean dos
evaluaciones ciegas. No se convoca un comité ni se delegan decisiones.

El estado declarado en la cabecera de T1 NO es evidencia. Los informes
previos proporcionan definiciones y notación; sus cotas preliminares
no son premisas probadas. Rehaced las identidades algebraicas a partir
de esas definiciones. No hace falta literatura externa ni novedad.

## Criterios que deben puntuarse separadamente

1. (1)–(2), (9)–(10a): referencia real r=U_N^N J phi_N, encoder completo,
   ambos bits, cinco piezas por canal y signos/adjuntos de los cruces.
2. (3): P=diag(p_S,I-p_S) dentro de W, P=0 fuera, Q=I-P.
   Compatibilidad con D=S⊕S^-1 y el P/Q previo, sin ortogonalidad ficticia
   ni identificación con los canales o con el corte IR.
3. (4)–(7): conjugación exponencial sobre la fuente compacta f,
   extensión del operador inclinado, convención Fourier y signo del
   desplazamiento p-i xi; recuperación exacta del factor e^(-K_* N).
   Buscar cualquier aplicación ilegítima del peso no acotado a phi_N/r.
4. (8), (12), (15): reconstrucción en Bob de cada sector y adjuntos
   P* H_c Q. ¿Es suficiente la restricción finita a Bob sin exigir que
   cada sector desinclinado sea globalmente l2? ¿Falta alguna hipótesis?
5. (13)–(16): índices temporales, productos vacíos, fuente inicial Q,
   memoria y salida Q; distinguir salida P de trayectoria siempre P.
6. Controles: rederivación por diferencia de estados, moneda nula,
   encoder identidad, POVM completo. Intentar al menos un control propio.
7. Techo: ¿se introduce subrepticiamente alguna afirmación de escala,
   cancelación, transferencia de cotas, H1/H1c o realización física?

Para cada objeción, indicar ecuación, derivación o contraejemplo y qué
reparación la resolvería. Distinguir FATAL, REQUIRED_REPAIR y OPTIONAL.
Si no hay objeción matemática, decirlo sin inventar una para disentir.

Veredicto final explícito: T1_PASS, T1_REPAIR_REQUIRED o T1_OPEN.
Enumerar reparaciones obligatorias, si las hay. T1_PASS sólo acepta la
identidad exacta en su contrato, no las cotas de los prechecks.
No ejecutar T2, no mapear N^-6, no buscar cancelaciones de T3, no cambiar
P/Q, perfiles o detectores y no proponer un frente intermedio.

## Snapshot y procedencia

Repositorio base: d8ca7b285129b8b29a304e232195e29f20095526.
T1 es un archivo de trabajo todavía no incluido en commit; se congela
por SHA256 y por su copia íntegra en el acta de sanedrin:

| Archivo adjunto | SHA256 |
| --- | --- |
| reports/2026-09-24--two-channel-t1-exact-signed-pq.md | 4c3eec6e4d60090695e2f9f5db431c196a9cc6e3d1371f9a7d4005c583b11644 |
| reports/2026-09-24--h1c-return-kernel-schur-audit.md | ac92cb8c10fa49a94dd36387846e38ce3a8885bfbdc2b0c8001e407f046e4e9b |
| reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md | ab06bb4136a4a96565670bc87d66eb6c8b13679abc7f9f3db31cfbe0b58dee9d |
| papers/ir-corona/ir-corona.tex | 05a2eb09d2f103608683978c292de939511359677727982de441970f2e655636 |

Se adjunta el TeX completo para las definiciones originales: convención
Fourier y símbolo (§2.1), protocolo (§3), representación inclinada (§7.3).
Sus teoremas asintóticos y sus afirmaciones de certificación no son
objeto de esta revisión ni premisas necesarias para el álgebra de T1.

Herramienta: /home/ignac/sanedrin, commit
8162508e3bd0e3d05770b4dd544fe7c962d0272c.
Herramientas compartidas: /home/ignac/herramientas, commit 18028a9.
Diagnóstico de esta sesión: opus, abner y gemini disponibles; astra
disponible con cuota sin verificar; ciro ausente por autenticación.
Sólo se solicitan opus y gemini; la ausencia de ciro no es un voto.

Una ronda adversarial, residuos individuales y veredicto del protocolo;
máximo 1600 palabras por turno, timeout 900 s, un reintento transitorio.
Si falla algún turno solicitado, se conserva el diagnóstico operativo:
una ejecución incompleta no se presentará como consenso.

## Contexto

### Contexto adjunto: reports/2026-09-24--two-channel-t1-exact-signed-pq.md
```
# T1: lift exacto firmado de los dos canales al P/Q inclinado

Fecha: 2026-09-24. Base inspeccionada: `d8ca7b285129b8b29a304e232195e29f20095526`.
Estado: `T1: ALGEBRAICALLY CLOSED / INDEPENDENT REVIEW PENDING`.
El cierre algebraico recoge la aceptación del usuario tras la derivación;
las comprobaciones realizadas siguen siendo internas.
Alcance: T1 de `state/CURRENT_STATE.md`, §9.6, por instrucción del usuario.
No se ejecutan T2 ni T3. No se modifica el estado canónico.

## 1. Definiciones y procedencia

Se usan como definiciones del problema el contrato de dos canales de
`reports/2026-09-24--h1c-return-kernel-schur-audit.md`, §6, y la partición
auxiliar de su §2. Las identidades siguientes se derivan aquí; no se toman
las conclusiones analíticas de los prechecks como premisas probadas.
El índice `biblioteca/INDICE.md` fue inspeccionado; no se utiliza ningún
resultado bibliográfico para esta expansión algebraica.

Sean
\[
Jv=(v,0),\qquad D=S\oplus S^{-1},\qquad
U_N=C_ND,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N},
\quad \beta=\sigma_x\otimes I_2.
\]
Los perfiles, la preparación y los efectos son los de
`papers/ir-corona/ir-corona.tex`, §3. Se fija cualquier entero \(N\ge2\),
cualquiera de los cuatro encoders \(M\) y cualquiera de los cuatro
detectores \(M_B\) del contrato. El perfil real \(\vartheta\) conserva
las hipótesis del contrato H1. El producto interno es antilineal en el
primer argumento. Para \(c\in\{+,-\}\), \(\pi_c\) extrae el canal y
\[
F_c=\pi_c^*E\pi_c,\qquad E=h_N\otimes M_B.
\]
Definimos la referencia física y la perturbación de Alice **completas**:
\[
r=U_N^NJ\phi_N=\Psi_0,\qquad
f=J(U_M-I)\phi_N,\qquad d=U_N^Nf.
\tag{1}
\]
Así \(\Psi_b=r+b d\) para ambos bits \(b=0,1\). No se sustituye
\(r\) por la referencia plana. En particular,
\[
f=J\bigl(c_N\phi_N+i s_N M\phi_N\bigr),\quad
c_N=\cos(\pi F_N/2)-1,\quad s_N=\sin(\pi F_N/2).
\]
No se descarta la parte \(c_N\), ni ninguna contribución cuadrática.
Como \(U_M-I\) está soportado en Alice, \(f\) tiene soporte finito.

La expansión directa del POVM da, sin aproximaciones,
\[
\boxed{L_c=2\operatorname{Re}\langle r,F_cd\rangle
                 +\langle d,F_cd\rangle.}
\tag{2}
\]
Esto ya incluye la sustracción exacta de la probabilidad del bit cero.

## 2. La partición existente y el lift bien definido

Se mantiene la unión fija \(W\) de las ocho ventanas del precheck de
Schur. Si \(p_S(p)\) es el Riesz idempotente de \(S(p-i\xi_*)\)
para la raíz dominante \(\lambda(p)\) en una ventana, entonces
\[
P(p)=
\begin{cases}
\operatorname{diag}(p_S(p),I_2-p_S(p)),&p\in W,\\
0,&p\notin W,
\end{cases}
\qquad Q=I-P.
\tag{3}
\]
En efecto, \(S^{-1}\) tiene autovalor \(\lambda\) en el subespacio
de \(S\) con autovalor \(\lambda^{-1}\). Se entiende (3) como
multiplicadores acotados en \(\mathscr H=L^2(\mathbb T^3;\mathbb C^4)\).
Sólo se usa \(P^2=P\), \(Q^2=Q\), \(P+Q=I\) y \(PQ=QP=0\).
No se presupone \(P^*=P\).

Estos P/Q son los del símbolo **inclinado**. No son los canales
\(+/-\), ni el corte IR \(\Pi'\) del frente C2/C3. Ambos canales
tienen componentes en P y en Q dentro de las ventanas. El exterior
permanece en Q, con todas sus transiciones.

Para justificar el lift sin inclinar la preparación de cola espacial
infinita, basta inclinar \(f\). Con la convención de Fourier del TeX,
\[
(\mathcal Fv)(p)=\sum_xe^{ip\cdot x}v(x),\qquad
(\mathcal F^{-1}z)(y)=\int e^{-ip\cdot y}z(p)\,d\mu(p),
\]
sean
\[
(H_\xi v)(x)=e^{\xi_*\cdot(x-x_*)}v(x),\quad
s=\mathcal F H_\xi f,\quad \Lambda=e^{\Phi_*},\quad
T=\Lambda^{-1}\mathcal F H_\xi U_NH_\xi^{-1}\mathcal F^{-1}.
\tag{4}
\]
La conjugación se define primero en vectores de soporte finito.
Como \(U_N\) tiene alcance finito y moneda local acotada, el operador
inclinado así obtenido tiene una extensión acotada en \(\mathscr H\).
La moneda conmuta con \(H_\xi\); el bloque libre es
\(D_\xi(p)=D(p-i\xi_*)\). Por tanto T es precisamente el paso
normalizado del precheck, con sus saltos de momento, no otro propagador.

Para cada \(0\le j\le N\),
\[
t_j=T^js=\Lambda^{-j}\mathcal F H_\xi U_N^jf.
\tag{5}
\]
Esta identidad se comprueba por inducción. Todos los \(U_N^jf\)
tienen soporte finito. No se necesita que \(H_\xi r\) o
\(H_\xi\phi_N\) pertenezcan a \(\ell^2\).

Sean \(B\) la restricción espacial a Bob y
\[
(\mathcal Vz)(y)=\mathbf1_{\mathcal B_N}(y)
 e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}z)(y),\qquad
\mathcal V_c=\pi_c\mathcal V.
\tag{6}
\]
Para cada N fijo esta aplicación está bien definida sobre \(L^2\),
pues Bob tiene soporte finito. Con los centros y escala ya fijados,
\(y_*-x_*=Nv_*\) y \(K_*=\xi_*\cdot v_*-\Phi_*\), (5) da
\[
Bd=e^{-K_*N}\mathcal Vt_N.
\tag{7}
\]
El factor se obtiene exactamente de
\(\Lambda^Ne^{-\xi_*\cdot(y-x_*)}
=e^{-K_*N}e^{-\xi_*\cdot(y-y_*)}\).
Extraerlo no es una estimación del tamaño de los factores restantes.

Definimos las dos contribuciones de **salida**:
\[
d_{c,P}=e^{-K_*N}\mathcal V_cPt_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_cQt_N,\qquad
B\pi_cd=d_{c,P}+d_{c,Q}.
\tag{8}
\]
Son amplitudes en Bob. No se afirma que desinclinar por separado
P y Q produzca vectores globales en el Hilbert físico. La restricción
en (6) evita exigir esa propiedad, innecesaria para el efecto local.

## 3. Expresión firmada completa para cada canal

Escribiendo \(r_c=B\pi_cr\), las probabilidades de ambos bits son
\[
p_{c,0}=\langle r_c,Er_c\rangle,
\qquad
p_{c,1}=\langle r_c+d_{c,P}+d_{c,Q},
                 E(r_c+d_{c,P}+d_{c,Q})\rangle.
\tag{9}
\]
Al restarlas:
\[
\boxed{\begin{aligned}
L_c={}&2\operatorname{Re}\langle r_c,E d_{c,P}\rangle
      +2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle\\
 &+\langle d_{c,P},E d_{c,P}\rangle
  +\langle d_{c,Q},E d_{c,Q}\rangle
  +2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\quad c=+,-.
\end{aligned}}
\tag{10}
\]
Ésta es la fórmula de T1. No contiene normas ni valores absolutos de
las respuestas. Los dos términos cuadráticos diagonales son reales
y no negativos; los términos de interferencia conservan sus signos.

Por indicación del usuario, se congela el siguiente vocabulario para T2,
con cinco contribuciones por canal:
\[
\begin{aligned}
A_{cP}&=2\operatorname{Re}\langle r_c,E d_{c,P}\rangle,\\
A_{cQ}&=2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle,\\
B_{cPP}&=\langle d_{c,P},E d_{c,P}\rangle,\\
B_{cQQ}&=\langle d_{c,Q},E d_{c,Q}\rangle,\\
B_{cPQ}&=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\end{aligned}
\qquad
\boxed{L_c=A_{cP}+A_{cQ}+B_{cPP}+B_{cQQ}+B_{cPQ}.}
\tag{10a}
\]
Estas etiquetas designan escalares del observable. No son los bloques
de transporte \(A_j,B_j\) de §4 ni nuevos proyectores.

Si se llama
\[
L_{c,A}=2\operatorname{Re}\langle r_c,E d_{c,A}\rangle
              +\langle d_{c,A},E d_{c,A}\rangle\quad(A=P,Q),
\]
entonces la identidad es
\[
L_c=L_{c,P}+L_{c,Q}+L_{c,\mathrm{cross}},\qquad
L_{c,\mathrm{cross}}=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle.
\tag{11}
\]
La aditividad de sólo dos términos requiere que este último escalar
sea cero para los datos considerados; T1 no establece tal anulación.
Repartirlo por convenio entre P y Q no demostraría una separación física.

En la representación auxiliar, sea
\[
\mathcal H_c=\mathcal V_c^*E\mathcal V_c,\qquad
\ell_c(z)=\langle r_c,E\mathcal V_cz\rangle.
\]
La misma fórmula, antes de agrupar términos conjugados, es
\[
\begin{aligned}
L_c={}&e^{-K_*N}\{
\ell_c(Pt_N)+\overline{\ell_c(Pt_N)}
+\ell_c(Qt_N)+\overline{\ell_c(Qt_N)}\}\\
&+e^{-2K_*N}\sum_{A,B\in\{P,Q\}}
  \langle t_N,A^*\mathcal H_c B t_N\rangle.
\end{aligned}
\tag{12}
\]
Aquí \(PQ=0\) no elimina \(P^*\mathcal H_cQ\). El efecto de Bob,
la reconstrucción y los adjuntos permanecen en su lugar. Incluso una
partición ortogonal no permitiría ese paso sin una condición adicional
sobre el efecto. El extremo lineal es exactamente el determinado por
\(w_c=F_cr\), soportado en Bob y dependiente de \(U_N\).

## 4. Compatibilidad con los bloques temporales existentes

No se estima ni se reabre la vía Volterra. Sólo se sustituyen los datos
de (4) en sus identidades finitas. Con \(x_j=Pt_j\), \(y_j=Qt_j\),
\[
A_j=PTP,\quad B_j=PTQ,\quad C_j=QTP,\quad D_j=QTQ,
\]
\[
x_{j+1}=A_jx_j+B_jy_j,\qquad
y_{j+1}=C_jx_j+D_jy_j,\qquad (x_0,y_0)=(Ps,Qs).
\tag{13}
\]
Los subíndices se conservan para coincidir con el precheck; en este
protocolo el paso T es el mismo en todas las capas. Los productos
vacíos son las identidades de los respectivos rangos.

Con \(\Phi_P(j,k)=A_{j-1}\cdots A_k\) y
\(G_Q(j,k)=D_{j-1}\cdots D_k\), la sustitución sucesiva de (13) da
\[
\begin{aligned}
x_N={}&\underbrace{\Phi_P(N,0)Ps}_{\text{trayectoria siempre en P}}\\
 &+\underbrace{\sum_{m=0}^{N-1}
 \Phi_P(N,m+1)B_mG_Q(m,0)Qs}_{f_{Q,N}}\\
 &+\underbrace{\sum_{m=0}^{N-1}\sum_{k=0}^{m-1}
 \Phi_P(N,m+1)B_mG_Q(m,k+1)C_kx_k}_{(\mathbb M_Nx)_N},\\
y_N={}&G_Q(N,0)Qs+
 \sum_{k=0}^{N-1}G_Q(N,k+1)C_kx_k.
\end{aligned}
\tag{14}
\]
Se verifica (14) primero resolviendo la segunda recurrencia de (13),
y sustituyéndola en la primera con su transporte \(\Phi_P\).
Así, los objetos de (8) son exactamente
\[
d_{c,P}=e^{-K_*N}\mathcal V_c x_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_c y_N.
\tag{15}
\]
La contribución que termina en P incluye retornos y entradas desde Q:
no es la contribución que permaneció siempre en P. Esta última es
únicamente el primer sumando de \(x_N\) en (14).

Si \(d_{c,0}\) denota la reconstrucción de ese primer sumando y
\(\delta d_c=d_{c,P}+d_{c,Q}-d_{c,0}\), la respuesta respecto de
esa amplitud, **manteniendo la referencia física r**, satisface
\[
\begin{aligned}
L_{c,0}&=2\operatorname{Re}\langle r_c,E d_{c,0}\rangle
                 +\langle d_{c,0},E d_{c,0}\rangle,\\
L_c-L_{c,0}&=2\operatorname{Re}\langle r_c+d_{c,0},E\delta d_c\rangle
                      +\langle\delta d_c,E\delta d_c\rangle.
\end{aligned}
\tag{16}
\]
Esto identifica el funcional exacto al que entrarían las correcciones
de (14); no les asigna potencia, pequeñez ni dominancia relativa.
Tampoco define una dinámica alternativa para el bit cero.

## 5. Comprobaciones internas por otra formulación y caso límite

**Segunda derivación, mediante la diferencia de estados.** Si
\(v=J\phi_N\), la diferencia inicial es exactamente
\[
\Delta=|v+f\rangle\langle v+f|-|v\rangle\langle v|
=|f\rangle\langle v|+|v\rangle\langle f|+|f\rangle\langle f|.
\]
Al conjugar por \(U_N^N\) y tomar la traza contra \(F_c\), los
dos primeros sumandos dan los términos lineales de (2) y el tercero
da su término cuadrático. Sustituir (8) genera las cuatro parejas
\(PP,PQ,QP,QQ\) de (12), incluidos ambos adjuntos cruzados.
Es la misma identidad obtenida desde las probabilidades (9).

**Control plano.** Si \(\vartheta=0\), T es diagonal por canales,
y también lo son P y Q de (3). Como \(f=J(U_M-I)\phi_N\),
\(r_-=d_{-,P}=d_{-,Q}=0\). Por (10), \(L_-=0\). En el canal
positivo \(r_+=BS^N\phi_N\) y
\(d_{+,P}+d_{+,Q}=BS^N(U_M-I)\phi_N\), por lo que (10) recupera
exactamente \(L_+=L_{\rm plano}\), para los dieciséis pares.
Este control verifica la reconstrucción, sin afirmar que se anule
el cruce P/Q dentro del canal positivo.

**Control nulo.** Si el encoder es la identidad, entonces \(f=s=0\)
y todos los términos de (10) son cero, cualquiera que sea la moneda.
Es un control algebraico, no una ampliación de la familia de encoders.

**POVM completo.** La unitariedad física y la normalización de ambos
bits dan \(L_\varnothing=-L_+-L_-\). La suma inclusiva conserva los
términos cruzados de (10) para ambos canales; T1 no demuestra que
se anulen en esa suma. No se infiere \(L_++L_-=0\).

## 6. Resultado y techo

T1 produce un observable firmado exacto compatible con el P/Q existente:
(10), con datos físicos (1), lift (4)–(8) y bloques (13)–(15).
La referencia y los dos bits están incluidos sin imponer una nueva
hipótesis de decaimiento exponencial a la preparación. El STOP por
incompatibilidad algebraica de T1 no se activa en esta derivación.

La derivación y sus controles son internos: no constituyen revisión
independiente ni promoción de un gate canónico. Sigue pendiente T2:
este documento no identifica un coeficiente de orden \(N^{-6}\),
no transfiere cotas de extremos y no demuestra una relación entre
los dos canales. T3 tampoco se ejecuta. H1/H1c, la justificación física,
E0, POWER_13/2_STABILITY, E/AdS y el manuscrito conservan su estado.

No se ha ejecutado código científico ni generado datos numéricos.
La procedencia de las fórmulas nuevas es su derivación explícita en
este archivo; los prechecks aportan la notación y el contrato, no una
certificación de sus estimaciones previas.

## 7. T2: alcance fijado, ejecución pendiente

La pregunta es qué contribución, o sub-contribución identificada, hereda
realmente el techo previo \(O(N^{-6})\). No se asigna de antemano ese
orden a ninguna de las diez piezas de (10a).

T2 deberá producir diez filas, una por cada
\(A_{+P},A_{+Q},B_{+PP},B_{+QQ},B_{+PQ}\) y
\(A_{-P},A_{-Q},B_{-PP},B_{-QQ},B_{-PQ}\), con estos campos:

| Campo | Contenido requerido |
| --- | --- |
| Objeto previo | Fórmula y localización precisa del bloque o extremo que se pretende usar; distinguir pieza completa y sub-contribución. |
| Cota disponible | Enunciado, hipótesis, ámbito y nivel de revisión; marcar explícitamente cuando no haya transferencia justificada. |
| Información perdida | Signos, fases, interferencias o dependencia de la referencia que desaparecieron al tomar normas. |
| Escala resultante | Factores exponenciales y potencias de N, indicando si se trata del observable físico o de una cantidad normalizada; distinguir cota superior y término asintótico identificado. |

El producto \(N^{-5/2}N^{-1}N^{-5/2}=N^{-6}\) sólo proporciona
un recuento de cotas hasta que se identifique el elemento bilineal,
sus extremos físicos y su lugar exacto en (10a). Las cotas heredadas
para extremos planos no se transfieren automáticamente a \(r_c\).
P/Q final tampoco etiqueta el número de excursiones: se conserva (14).

No se introduce ninguna técnica nueva. Si una transferencia no está
justificada por lo ya disponible, se registra esa carencia sin abrir
una nueva vía de estimación. T2 no busca simetrías ni ejecuta T3.

Para cualquier posterior afirmación de cancelación, se mantendrán
separados estos tres niveles:

1. Dentro de una pieza de (10a).
2. Entre piezas de un mismo canal.
3. Entre canales, en \(L_++L_-\).

El tercer nivel no prueba cancelación en ninguno de los dos canales
por separado. El número de piezas que reciban una misma cota tampoco
decide por sí solo si hay una relación estructural.

Si T2 sólo recupera una cota gruesa sin coeficiente identificado, la
conclusión será que \(N^{-6}\) sigue siendo un techo sin término
asintótico aislado. Eso no prueba que un término de ese orden sea
inexistente, ni que su coeficiente sea cero. En ese caso se aplica el
STOP previsto: no buscar simetrías de un coeficiente no identificado.
```

### Contexto adjunto: reports/2026-09-24--h1c-return-kernel-schur-audit.md
```
# H1c: auditoría de la cota Schur y cierre del contrato operacional

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: el resolvente Volterra de
`reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md`.
`H1c_LOCALIZATION (L') = OPEN`.

**Cierre de sesión, 2026-09-24:** §§1–5 conservan el precheck analítico
previo, preliminar y sin revisión independiente. §6 congela por instrucción
expresa del usuario `TWO_DISTINGUISHABLE_CHANNELS`, con observable primario
`(L_+, L_-)`. H1c-0a está CLOSED; H1c-0b está
FIXED_BY_EXPLICIT_ASSUMPTION. La justificación física concreta sigue OPEN.
Volterra/localización asintótica: PAUSED; la prueba de H1c sigue abierta.
§7 fija el orden de la próxima sesión y no registra su ejecución.

## 1. La suma propuesta no implica la cota de susceptibilidad

Pongamos `R_{m,k}=B_mG_Q(m,k+1)C_k` para `m>k`. La memoria exacta es
\[
(\mathbb M_Nx)_n=
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\Phi_P(n,m+1)R_{m,k}x_k.
\tag{1}
\]
El kernel propuesto
`\widetilde R_{m,k}=\Phi_P(N,m+1)R_{m,k}\Phi_P(k,0)`
es la contribución de **una excursión** al elemento final cuando la
entrada sigue el transporte P libre. No es el kernel de `\mathbb M_N`
sobre secuencias arbitrarias `x_k`: (1) debe evaluarse también en
tiempos intermedios y con todas las posibles entradas `x_k`.

Contraejemplo algebraico: en espacios P y Q escalares, durante N pasos
tomar `A_j=D_j=1` y `B_j=C_j=1/N`, con pesos `w_j=1`. Entonces
`\Phi_P=1`, `G_Q=1`, y para `j>k`,
\[
R_{j,k}=\widetilde R_{j,k}=N^{-2},\qquad
\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|\le N^{-1}.
\tag{2}
\]
Sin embargo, para la secuencia `x_k=1`,
\[
(\mathbb M_Nx)_N
=N^{-2}\sum_{m=0}^{N-1}m
=\frac{N-1}{2N}\longrightarrow\frac12.
\tag{3}
\]
Así, la cota de (2) con `C/N` no implica
`\|\mathbb M_N\|=O(N^{-1})`. El ejemplo refuta sólo esa implicación;
no pretende representar el sector Q del walk inclinado.

Una condición suficiente que sí conserva el transporte temporal es
\[
\boxed{
\mathcal S_N(w):=
\sup_{0\le n\le N}\frac1{w_n}
\sum_{m=0}^{n-1}\sum_{k=0}^{m-1}
\|\Phi_P(n,m+1)R_{m,k}\|w_k
\le\frac{C}{N}.}
\tag{4}
\]
Por la desigualdad triangular, (4) implica
`\chi_N=\|\mathbb M_N\|_{w\to w}\le C/N`. También basta controlar
uniformemente el transporte P ponderado y exigir
`\sup_m w_{m+1}^{-1}\sum_{k<m}\|R_{m,k}\|w_k=O(N^{-2})`.
Con transporte P acotado y pesos unitarios, una suma por columnas
`\sup_k\sum_{m>k}\|R_{m,k}\|=O(N^{-2})` es otra condición suficiente.
El orden `N^{-2}` en estas sumas deja una suma adicional de `O(N)`
tiempos P en (1).
Como caso límite independiente, si `D_j=\rho` con `0<\rho<1`
fijo en el ejemplo escalar, entonces
`R_{j,k}=N^{-2}\rho^{j-k-1}`. La suma en duración es `O(N^{-2})`
por tiempo de origen y (1) es `O(N^{-1})`, como predice (4).

## 2. Cota completa en una norma auxiliar L2

Hay una forma de acotar el retorno **sandwichado** sin exigir una
estimación final para el Green Q desnudo. Se usa una partición
auxiliar que no afirma un Riesz splitting global. Sea W la unión de
vecindades fijas y disjuntas de los ocho saddles. En W, `P(p)` es el
proyector Riesz dominante de rango dos del símbolo libre inclinado;
fuera de W se define `P(p)=0` y `Q(p)=I`. Esta partición es medible y
acotada en `L^2(\mathbb T^3;\mathbb C^4)`; el salto en el borde de W
forma parte de los bloques de la moneda.

Normalicemos por el escalar global `\Lambda=e^{\Phi_*}>1`. El lema
espectral del TeX plano (`papers/ir-corona/ir-corona.tex`,
`lem:specrad` y `lem:symbol(d,e)`) da esa propiedad para S; para
`D=S\oplus S^{-1}` se sigue porque S es unimodular y ambos sumandos
tienen el mismo radio espectral. Por tanto
`\rho(D_\xi(p)/\Lambda)\le1`, con igualdad sólo en los ocho saddles.
En W, el bloque libre Q tiene autovalor
`\lambda(p)^{-1}/\Lambda`, uniformemente dentro del disco unidad.
Fuera de W, `Q=I` y el radio espectral libre es estrictamente menor
que uno por compacidad. En consecuencia existe `\rho_0<1` que
acota el radio espectral de todo el bloque libre Q, aun donde la
matriz exterior sea no normal.

En dimensión finita por fibra, el resolvente de la familia libre en
una circunferencia `\rho_0<\rho_1<1` es uniformemente acotado en
cada uno de los dos compactos (cierres de W y de su exterior).
Por la fórmula de Cauchy,
\[
\|(D_Q^{(0)})^h\|_{L^2\to L^2}
\le C_0\rho_1^h,
\qquad D_Q^{(0)}=Q(D_\xi/\Lambda)Q.
\tag{5}
\]
La norma equivalente
`\|y\|_*:=\sup_{h\ge0}\rho_1^{-h}\|(D_Q^{(0)})^hy\|_2`
satisface `\|D_Q^{(0)}y\|_*\le\rho_1\|y\|_*`.

En la representación de momento, la moneda espacial es convolución,
pero su norma `L^2\to L^2` es la norma del multiplicador en posición:
`\|C_N-I\|\le C/N` para `\vartheta` acotada. Las proyecciones
auxiliares son multiplicadores acotados en momento. Por ello, en
las normas P=`L^2`, Q=`\|\cdot\|_*`, los bloques exactos satisfacen
\[
\|B_j\|,\|C_j\|\le C/N,\quad
\|D_j\|_*\le\rho_1+C/N<\rho_2<1,
\quad\|A_j\|_2\le1+C/N.
\tag{6}
\]
La última desigualdad usa `|\lambda(p)|/\Lambda\le1` en W.
Permite variación uniforme de la moneda entre pasos; no presume
conservación del momento.

De (6) se obtiene directamente para el **retorno completo**
\[
\|R_{m,k}\|_{P\to P}
\le\frac{C}{N^2}\rho_2^{m-k-1},\qquad
\|\Phi_P(n,m+1)\|\le e^C.
\tag{7}
\]
La suma de (4) con `w=1` da
\[
\boxed{\|\mathbb M_N\|_{\ell^\infty_t L^2_p\to
\ell^\infty_t L^2_p}=O(N^{-1}).}
\tag{8}
\]
Esta es una cota preliminar en un espacio auxiliar para el producto
normalizado; la no normalidad exterior queda absorbida en la norma
equivalente de (5). No demuestra la cota física ponderada de `L'`.

## 3. Techo físico de la cota auxiliar

La cota (8) no recupera por sí sola el factor gaussiano tangencial
de los elementos Alice/Bob. `state/CURRENT_STATE.md`, §9.2, sólo
certifica masas absolutas inclinadas `O(N^{-5/2})` para cada extremo.
Usándolas sin información adicional, (8) produciría para la
corrección interna una cota `O(N^{-6})`. La escala líder que se intenta
conservar es `N^{-13/2}`: esa cota gruesa pierde `N^{1/2}` y no prueba
dominancia relativa. Una norma física con envolventes de momento,
fases y endpoints podría recuperar la potencia, pero aún no se ha
fijado ni estimado.

Además, definir `P=0` fuera de W asigna todas las trayectorias
exteriores a Q. Sus entradas/salidas y los saltos entre W y su
exterior siguen presentes en `B,C,D`; (8) no demuestra que la
contribución Q inicial/final al elemento físico sea pequeña.

## 4. Resultado del subgate

- **REFUTADO:** la condición
  `\sup_k\sum_{j>k}\|\widetilde R_{j,k}\|_w\le C/N`
  implica por sí sola `\chi_N=O(N^{-1})`.
- **PRELIMINARY:** la condición correcta es una suma Volterra doble
  como (4), o una suma de retornos `O(N^{-2})` por tiempo bajo
  transporte P controlado.
- **PRELIMINARY:** en `\ell^\infty_t L^2_p`, el splitting auxiliar
  local-en-W / exterior-en-Q y el lema espectral plano dan (8).
- **OPEN:** trasladar (8) a una envolvente física que preserve el
  factor de saddle, y controlar los términos Q de los extremos
  reales de `L'`.

En el precheck de §§1–4 no se ejecutó código numérico ni se modificaron
C2c, el manuscrito o `state/CURRENT_STATE.md`. El cierre documental de §6
sí se resume ahora en el estado canónico, por instrucción del usuario.

## 5. Cortafuegos del elemento físico

Antes del cierre de §6, la prueba propuesta era comparar directamente la primera
corrección `\ell_P(\mathbb M_Nx^{(0)})_N` y los términos con entrada o
salida Q de (8) en el precheck Volterra con el líder `L'_{N,P}`.
La búsqueda en `state/CURRENT_STATE.md`, §9,
`reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md`,
§§8–9, y `reports/2026-09-20--h1-chat-research-log.md`, §§12–13,
no proporciona los extremos físicos de cuatro componentes, el
funcional firmado final ni una cota inferior uniforme para
`|L'_{N,P}|`. El TeX plano, §7.3, fija un elemento de dos componentes;
su embedding en cuatro componentes es un test auxiliar, no una
definición del observable inhomogéneo.

Por ello los cocientes físicos
`\ell_P(\mathbb M_Nx^{(0)})_N/L'_{N,P}` y
`L'_{\mathrm{boundary}-Q}/L'_{N,P}` son **NO EVALUABLES CON EL
CONTRATO ACTUAL**. La cota (8) no se convierte en un PASS de H1c.
Según el cortafuegos de esta línea, se detiene aquí la vía Volterra:
no se introducen nuevas normas, proyectores o resolventes para
suplantar esos datos físicos. Ese diagnóstico describe el contrato anterior.
§6 fija ahora el protocolo por hipótesis explícita; su traducción exacta a
P/Q sigue pendiente y no se obtiene automáticamente de (1)–(8).

## 6. Cierre H1c-0 / decisión explícita de modelo — 2026-09-24

### 6.1 Procedencia y alcance del cierre

La búsqueda local previa al cierre no encontró las etiquetas
`H1C0_UNDERSPECIFIED`, `CONTRACT_VALID`, `PHYSICAL_INTERPRETATION_OPEN`
o `MODEL_CHOICE_REQUIRED` en archivos del repositorio. Se registran aquí
como etapas de la auditoría y decisión de esta sesión, sin atribuirlas
retroactivamente a un commit anterior:

1. `H1C0_UNDERSPECIFIED`: el contrato H1 fijaba propagación y beta,
   pero no el lift operacional del protocolo plano.
2. `CONTRACT_VALID / PHYSICAL_INTERPRETATION_OPEN`: el candidato con
   preparación en el primer bloque y POVM refinado supera las identidades
   de normalización, positividad y recuperación plana, en auditoría interna.
3. `MODEL_CHOICE_REQUIRED`: el repositorio anterior no seleccionaba qué
   significado operacional dar a los bloques.
4. Decisión aceptada y congelada por el usuario:
   **`TWO_DISTINGUISHABLE_CHANNELS`**, como nueva hipótesis de modelo.

El contrato algebraico figura en la
[reconstrucción H1, §1](2026-09-20--h1-inhomogeneous-localization-reconstruction.md),
introducida en `bbc898be6c68cd8594449a7a52988c95b655dff4`. La
[bitácora H1, §§1–2](2026-09-20--h1-chat-research-log.md),
archivada en `3f8ae75f327aa06d23a2e5ee726a81866bcdfe33`, se identifica
como reconstrucción de chat y no certifica la convención gamma original.
Esos textos documentan las identidades del doblado; no derivan la
accesibilidad física de sus dos bloques. La falta de ese diccionario
tampoco demuestra que el doblado se introdujera exclusivamente como
dispositivo auxiliar.

El cierre H1c-0a se limita a la consistencia y definición del contrato
matemático siguiente. No certifica los prechecks de §§1–5, no constituye
revisión independiente y no cierra la localización H1c ni H1.

### 6.2 Espacio, propagación, preparación y encoder

El Hilbert operacional completo de una partícula es
\[
\mathcal H=
\ell^2(\mathbb Z^3)\otimes
\mathbb C^2_{\rm canal}\otimes\mathbb C^2_{\rm espín}.
\]
Para esta extensión candidata, los bloques de
\[
D=S\oplus S^{-1},\qquad
\beta=\sigma_x^{\rm canal}\otimes I_{\rm espín},\qquad
U_N=C_N(x)D,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N}
\]
se interpretan como canales internos distinguibles `+` y `-`. Se conserva
el perfil real y las hipótesis de regularidad del contrato H1 existente.
Beta intercambia los canales y la moneda los mezcla coherentemente.
La interpretación y la capacidad de Bob para resolver el canal son
**supuestos nuevos**, no consecuencias de esas identidades algebraicas.

Se heredan sin cambio el recurso, las regiones, los perfiles y las familias
de encoder/detector de [ir-corona.tex, §3](../papers/ir-corona/ir-corona.tex):
\[
\widehat\phi_N(p)=Z_N^{-1/2}g(Np)|\downarrow\rangle,
\quad \|\phi_N\|=1,\qquad
U_M=e^{i\pi F_N M/2},\qquad E=h_N\otimes M_B,
\quad 0\le E\le I.
\]
Aquí `M` recorre `I, sigma_1, sigma_2, sigma_3` y `M_B` recorre
`I, (I+sigma_j)/2`, como en el protocolo plano.
Con `Jx=(x,0)`, la preparación fijada es
\[
\Phi_N=J\phi_N=\binom{\phi_N}{0}.
\]
El bit `b=0` aplica la identidad; para `b=1` se usa un representante
\[
\mathcal U_M^{(1)}=U_M\oplus U_M,\qquad
\mathcal U_M^{(0)}=I_{\mathcal H}.
\]
La identidad
\[
(U_M\oplus U_M)J=(U_M\oplus I)J=JU_M
\]
registra equivalencia operacional en el instante del encoding bajo esta
preparación. No afirma identidad física de ambos encoders sobre otros
estados o protocolos. Ambos son unitarios y actúan como identidad fuera
de Alice. Para el mismo perfil real, `U_N` es unitario en el Hilbert físico.

Tras encoding y `N` pasos,
\[
\Psi_b=U_N^N\mathcal U_M^{(b)}\Phi_N
=\binom{\psi_b^+}{\psi_b^-},\qquad \|\Psi_b\|=1.
\]
La referencia no codificada de Bob procede de
`Psi_0=U_N^N Phi_N`; depende del walk doblado. No se reemplaza por la
referencia plana al activar la moneda.

### 6.3 POVM y respuesta física primaria

Bob resuelve la etiqueta de canal, por hipótesis de modelo. Su POVM es
\[
F_+=E\oplus0,\qquad F_-=0\oplus E,\qquad
F_\varnothing=I_4-(E\oplus E).
\]
En esta fórmula `I_4` abrevia la identidad completa
`I_{ell^2(Z^3)} tensor I_4`; no se restringe el espacio a la región Bob.
Como `0<=E<=I`, los tres efectos son positivos y suman
`I_{mathcal H}`. El resultado vacío incluye toda ausencia de detección.

Con la dependencia en `N,M,M_B` implícita, se fija como respuesta primaria
\[
\boxed{(L_+,L_-)},\qquad
L_\pm=
\langle\psi_1^\pm,E\psi_1^\pm\rangle
-\langle\psi_0^\pm,E\psi_0^\pm\rangle.
\]
Por normalización de las dos distribuciones de resultados,
\[
L_\varnothing=-L_+-L_-.
\]
Las dos lecturas binarias posibles son coarse-grainings explícitos:
\[
L_{\rm block}=L_+,\qquad L_{\rm incl}=L_++L_-.
\]
La primera cuenta `+` frente a `-` o ausencia de detección; la segunda
cuenta cualquiera de los dos canales frente a ausencia de detección.
Ninguna es el observable primario del contrato. Las respuestas se suman
con signo antes de tomar cualquier valor absoluto. No se seleccionará
posteriormente una lectura porque proporcione mejores potencias.

Los canales pueden mantener coherencia cuántica. Este POVM conserva la
información de sus tres resultados; no reconstruye todas las coherencias
del estado. Tampoco identifica los canales físicos `+/-` con los sectores
espectrales auxiliares `P/Q` de los prechecks.

### 6.4 Control plano exacto y límites

Para `vartheta=0`,
\[
C_N=I,\qquad U_N=D=S\oplus S^{-1},\qquad
U_N^N\binom{x}{0}=\binom{S^Nx}{0}.
\]
Por tanto para ambos bits y todos los pares heredados,
\[
\Psi_b=\binom{S^NU_M^{(b)}\phi_N}{0},\qquad
L_+=L_{\rm plano},\quad L_-=0,\quad
L_{\rm incl}=L_{\rm plano}.
\]
Esta recuperación exacta justifica inicialmente la extensión propuesta.
No se usa comportamiento asintótico favorable para elegirla.

Sigue **OPEN** la justificación de este doubled walk como representación
de un sistema físico concreto. Ningún resultado futuro de esta extensión
se presentará como universal para el protocolo plano original: quedará
condicionado a la hipótesis de dos canales distinguibles accesibles a Bob.

Estado conceptual congelado por instrucción del usuario:

```text
model choice: TWO_DISTINGUISHABLE_CHANNELS
H1c-0a mathematical doubled-walk contract: CLOSED
H1c-0b operational model choice: FIXED_BY_EXPLICIT_ASSUMPTION
physical realization/justification: OPEN
Volterra/asymptotic localization: PAUSED
primary observable: (L_+, L_-)
```

H1c y H1 permanecen matemáticamente abiertos. El cierre de contrato no
promueve ninguna cota preliminar. En particular, el `O(N^-6)` de §3
procede de multiplicar cotas absolutas auxiliares; no se ha aislado un
coeficiente `E_6`, ni se ha trasladado esa cota a cada respuesta firmada
del protocolo recién fijado.

## 7. Next session / 2026-09-25

Plan registrado; T1–T3 no se ejecutan en este cierre documental.

### T1 — Lift exacto del observable a P/Q

Partir del POVM de §6 y derivar, sin estimaciones de norma, las expresiones
exactas firmadas de `L_+` y `L_-` dentro de la descomposición P/Q existente.
Determinar si tiene sentido escribir
`L_± = L_{±,P} + L_{±,Q}`. No asumir esa aditividad: si el observable
cuadrático genera términos cruzados, escribir la expansión exacta completa,
incluyendo la referencia de Bob y ambos bits. No confundir canal físico con
proyector de Riesz ni cambiar la partición para obtener el resultado.

### T2 — Identificar qué significa realmente el actual O(N^-6)

Sólo tras cerrar T1, trazar la cota auxiliar
`||mathbb M_N||=O(N^-1)` de (8) y las cotas de extremo hasta cada
contribución firmada de `L_+` y `L_-`. Distinguir cota de norma, término
asintótico real, términos cruzados y posible cancelación firmada.
Comprobar el alcance de las cotas heredadas para la nueva referencia de Bob.
No llamar `E_6` a nada salvo que exista un coeficiente realmente aislado.

### T3 — Test de proyección

Sólo cuando T1 y T2 estén cerrados, comprobar separadamente qué contenido
del techo `O(N^-6)` sobrevive en `L_+`, en `L_-`, se cancela en alguno,
o se cancela únicamente en `L_++L_-`. Toda afirmación de cancelación
requiere contribuciones firmadas identificadas; una cota sola no basta.
Una cancelación en `L_incl` no permite cambiar el observable primario.

### STOP GATE

- Si T1 no produce un observable firmado exacto compatible con la
  descomposición existente, parar.
- Si T2 muestra que `N^-6` sólo es una cota gruesa sin coeficiente
  identificable, no buscar simetrías de un término inexistente.
- No introducir otra técnica analítica hasta cerrar T1–T3. La vía Volterra
  y la localización asintótica permanecen PAUSED durante este cierre.

## 8. Cadena documental archivada

Los siete informes de hoy pertenecen a esta cadena. Se conservan sus
argumentos previos con su alcance y falta de revisión independiente:

- [Conteo de parejas Dyson](2026-09-24--h1c-dyson-pair-audit.md).
- [Cota por inserción Dyson](2026-09-24--h1c-dyson-target-check.md).
- [Descomposición Dyson exacta](2026-09-24--h1c-exact-dyson-decomposition.md).
- [Masa de excursiones: kill-tests](2026-09-24--h1c-excursion-mass-kill-tests.md).
- [Resolvente de excursiones](2026-09-24--h1c-kernel-excursion-resolvent-audit.md).
- [Núcleo de memoria Volterra](2026-09-24--h1c-volterra-memory-kernel-precheck.md).
- Este informe de Schur y cierre operacional.

El cierre añade documentación y el resumen de `state/CURRENT_STATE.md`.
No ejecuta Volterra, nuevos fits, cálculos asintóticos, scripts científicos
ni el plan de mañana. El manuscrito plano y el código no se modifican.
```

### Contexto adjunto: reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md
```
# H1c: precheck del núcleo de memoria Volterra

Fecha: 2026-09-24. Estado: `PRELIMINARY / SIN REVISIÓN INDEPENDIENTE`.
Objeto: probar o matar la ruta de memoria P/Q en el elemento Alice/Bob
inclinado. `H1c_LOCALIZATION (L') = OPEN`.

**Cierre documental del día:** este precheck precede a la decisión
operacional de [el cierre H1c, §§6–8](2026-09-24--h1c-return-kernel-schur-audit.md).
Las carencias físicas descritas abajo son el diagnóstico previo; el nuevo
contrato fija `(L_+, L_-)`, pero su lift exacto al P/Q de este informe sigue
pendiente en T1. Volterra/localización asintótica está PAUSED; estas
identidades para extremos genéricos no son por sí solas el lift firmado.

## 1. Identidad finita y cuantificadores

Fijada una partición `P_j(p)+Q_j(p)=I` en cada capa de momento, sean
`A_j=P_{j+1}T_jP_j`, `B_j=P_{j+1}T_jQ_j`, `C_j=Q_{j+1}T_jP_j` y
`D_j=Q_{j+1}T_jQ_j`. Estos son operadores integrales entre capas;
sus argumentos de entrada y salida pueden tener momentos distintos.
Escribiendo `x_j=P_j\psi_j`, `y_j=Q_j\psi_j`, se tiene exactamente
\[
x_{j+1}=A_jx_j+B_jy_j,\qquad
y_{j+1}=C_jx_j+D_jy_j.
\tag{1}
\]
Para `j\ge k`, `G_Q(j,k)=D_{j-1}\cdots D_k` y
`G_Q(k,k)=I` en el espacio Q de la capa `k`. La eliminación exacta es
\[
y_j=G_Q(j,0)y_0+
\sum_{k=0}^{j-1}G_Q(j,k+1)C_kx_k,
\tag{2}
\]
\[
x_{j+1}=A_jx_j+B_jG_Q(j,0)y_0
 +\sum_{k=0}^{j-1}K_{j,k}x_k,
\quad K_{j,k}=B_jG_Q(j,k+1)C_k.
\tag{3}
\]
En particular, `K_{k+1,k}=B_{k+1}C_k`: no hay paso Q interno.

Para evitar esconder el transporte P, definamos
`\Phi_P(j,k)=A_{j-1}\cdots A_k`, `\Phi_P(k,k)=I` en P. La forma
Volterra exacta para `0\le j\le N` es
\[
x_j=x_j^{(0)}+f_{Q,j}+(\mathbb M_Nx)_j,
\qquad x_j^{(0)}=\Phi_P(j,0)x_0,
\tag{4}
\]
\[
f_{Q,j}=\sum_{m=0}^{j-1}
\Phi_P(j,m+1)B_mG_Q(m,0)y_0,
\tag{5}
\]
\[
(\mathbb M_Nx)_j
=\sum_{m=0}^{j-1}\sum_{k=0}^{m-1}
\Phi_P(j,m+1)B_mG_Q(m,k+1)C_kx_k.
\tag{6}
\]
`\mathbb M_N` es estrictamente triangular en tiempo; por tanto
`(I-\mathbb M_N)^{-1}` existe como polinomio finito y
\[
x=(I-\mathbb M_N)^{-1}(x^{(0)}+f_Q).
\tag{7}
\]
Las excursiones repetidas están incluidas en (7). La salida Q sigue
siendo una obligación separada:
\[
y_N=G_Q(N,0)y_0+
\sum_{k=0}^{N-1}G_Q(N,k+1)C_kx_k,
\quad L_N=\ell_Px_N+\ell_Qy_N.
\tag{8}
\]

La identidad requiere una partición P/Q definida en todos los momentos
que visitan los kernels. El Riesz projector del proyecto sólo está
controlado en ventanas locales (`state/CURRENT_STATE.md`, §9.1).
Una extensión fuera de ellas es una elección auxiliar y sus cruces
deben entrar en `A,B,C,D`. Además siguen sin fijarse los extremos
físicos de cuatro componentes y el funcional final de `L'`; (1)-(8)
son identidades para extremos genéricos.

## 2. Primer núcleo no nulo con el kernel exacto

Trabajamos en una ventana local del símbolo libre inclinado
`D_\xi(p)=\lambda(p)P(p)+\lambda(p)^{-1}Q(p)` y fijamos la
normalización **escalar global** `\Lambda=e^{\Phi_*}`. Así se conserva
la relación con el elemento físico inclinado; dividir por
`\lambda(p)` en cada paso y cada momento sería otra dinámica y
exigiría reponer su cociclo. Pongamos
\[
a(p)=\lambda(p)/\Lambda,\qquad
d(p)=\lambda(p)^{-1}/\Lambda,\qquad
\Theta_N(q)=\sum_{x\in\mathbb Z^3}e^{iq\cdot x}\vartheta(x/N).
\tag{9}
\]
El kernel de un paso es exactamente
`T(p',p)=\delta(p'-p)D_\xi(p)/\Lambda+
\widehat M_N(p'-p)D_\xi(p)/\Lambda`, con
`M_N=e^{-i\vartheta\beta/N}-I`. Su parte impar lineal en la moneda
da, a primer orden en `1/N`,
\[
C^{(1)}(r,p)
=-\frac{i}{N}\Theta_N(r-p)a(p)
 Q(r)\beta P(p),
\tag{10}
\]
\[
B^{(1)}(p',r)
=-\frac{i}{N}\Theta_N(p'-r)d(r)
 P(p')\beta Q(r).
\tag{11}
\]
La parte libre Q entre ambos factores conserva el momento y, para
`h=j-k\ge1`, aporta `d(r)^{h-1}Q(r)`. Por tanto el primer término
cuadrático de la memoria, para `h` **fijo**, es
\[
\boxed{
K_{j,k}^{(2)}(p',p)
=-\frac{a(p)}{N^2}
\int_{\mathbb T^3}
\Theta_N(p'-r)\Theta_N(r-p)
d(r)^h
P(p')\beta Q(r)\beta P(p)\,d\mu(r).
}
\tag{12}
\]
La fórmula conserva ambos saltos de momento. Es el término de dos
factores impares del **kernel exacto**; no convierte
`\Theta_N` en una delta. El resto de la expansión a `h` fijo no
establece uniformidad para `h=O(N)` ni control fuera de las ventanas.
La afirmación `K_{j,k}=O(N^{-2})` se refiere aquí a la norma de
operador de una excursión con separación fija y propagación Q
controlada; el valor puntual de `\Theta_N` puede crecer como `N^3`.

Como segunda comprobación, si la moneda es globalmente constante
`\vartheta=\theta`, el kernel se hace diagonal en momento. En el
saddle `p'=p=0`, `a(0)=1`, `d(0)=\Lambda^{-2}` y
`P\beta Q\beta P=P`; el **coeficiente de la delta diagonal** de
(12) en esa fibra se reduce a
\[
K_{j,k}^{(2)}(0,0)
=-\frac{\theta^2}{N^2}\Lambda^{-2h}P.
\tag{13}
\]
Sumar las `N-h` posiciones de cada pareja da
`-\theta^2/[N(\Lambda^2-1)]P+O(N^{-2})`, de acuerdo con el
cálculo Dyson independiente en
`reports/2026-09-24--h1c-dyson-pair-audit.md`.
Un perfil suave con meseta constante sobre los caminos Alice/Bob
reproduce ese test para el elemento pertinente, aunque su kernel
global no sea diagonal.

## 3. Qué falta para una cota de susceptibilidad

La propuesta `\chi_N=\|\mathbb M_N\|_{w\to w}` es un criterio
condicional claro **después** de fijar una envolvente `w_j>0` para
el elemento inclinado y una norma de los campos en momento.
Como (7) es finita, `\chi_N<1` implica
`\|(I-\mathbb M_N)^{-1}\|_{w\to w}\le(1-\chi_N)^{-1}`.
El orden `N^{-2}` de (12) para cada pareja no prueba
`\chi_N=O(N^{-1})`. Una cota de ese tipo requeriría, uniformemente
en ventanas y pesos elegidos, controlar:

1. el transporte `\Phi_P(j,m+1)` con el tilt y las fases físicas;
2. la suma en duración de `G_Q(m,k+1)` con momentos variables y
   posibles picos no normales;
3. la suma en `m,k`, que cuenta `O(N)` posiciones aun cuando las
   duraciones Q sean sumables;
4. interfaces de ventanas y contribuciones fuera de ellas.

Bajo **hipótesis adicionales** de transporte P ponderado uniforme,
dos acoplamientos mixtos `O(N^{-1})` en la norma apropiada y suma
Q ponderada uniforme, (6) permite una cota `O(N^{-1})`: una suma
temporal de `O(N)` posiciones multiplica el coste `O(N^{-2})` de
cada excursión. Ninguna de esas hipótesis globales está demostrada
para el elemento Alice/Bob de `L'`. Su líder firmado también puede
cancelar, de modo que `\chi_N=o(1)` no implica por sí solo
que el complemento sea `o(|L'_{N,P}|)`.

Los bordes no están incluidos en `\chi_N`: hay que estimar `f_Q`
y los dos términos Q de (8) con los extremos físicos. El test plano
embebido de `reports/2026-09-24--h1c-kernel-excursion-resolvent-audit.md`,
§3, muestra que `s_Q,\ell_Q` no reciben automáticamente una
potencia extra de N.

## 4. Estado del precheck

El núcleo (12) es un candidato concreto de orden dos para una
excursión interna y es no nulo en el test de fibra constante (13).
La ecuación Volterra (1)-(8) incluye
exactamente excursiones repetidas y bordes Q. Es una ruta
algebraicamente consistente para un gate de H1c, condicionada a
la partición global, los extremos físicos, la envolvente `w` y
las cotas de transporte/sumabilidad indicadas. No se promueve
`H1c_LOCALIZATION (L')`: el control uniforme de momentos variables
y regiones sin Riesz splitting sigue abierto.

No se ejecutó código numérico, ni se modificaron C2c, el manuscrito,
`state/CURRENT_STATE.md`, E0 o E/AdS.
```

### Contexto adjunto: papers/ir-corona/ir-corona.tex
```
\documentclass[11pt]{amsart}

\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\T}{\mathbb{T}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cK}{\mathcal{K}}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\up}{{\uparrow}}
\newcommand{\dn}{{\downarrow}}
\newcommand{\Cmicro}{C_{\mathrm{micro}}}
\newcommand{\cIR}{c_{\mathrm{IR}}}
\newcommand{\arcosh}{\operatorname{arcosh}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Tr}{\operatorname{Tr}}
\newcommand{\Hess}{\operatorname{Hess}}
\newcommand{\re}{\operatorname{Re}}
\newcommand{\im}{\operatorname{Im}}
\newcommand{\vstar}{v_*}
\newcommand{\xistar}{\xi_*}
\newcommand{\uhat}{\hat u}

\begin{document}

\title[Infrared response outside the emergent light cone]{An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk}

% TODO(author): any AI-assistance disclosure required by the target journal.
\author{Jos\'e Ignacio Mart\'in Gandul}
\address{Independent Researcher, Seville, Spain}
\email{adnacho@gmail.com}

\date{\today}

\begin{abstract}
In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support.  We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region.  All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node.  Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a \emph{corona}.  There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control.  Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector.  All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
produces only a vanishing fraction of its output outside the wider band
$|p|\le N^{-1/2}$.  Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$.  For a concrete
family of sixteen encoder--detector pairs, it has the exact leading
asymptotics
\[
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
\]
Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser.  The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
the sixteen pairs.  The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations.  The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support.  The result is purely asymptotic: the
remainder constants are not explicit, and numerical diagnostics indicate
that the leading term is quantitatively accurate only for $N$ of order
$10^3$ and beyond.
\end{abstract}

\maketitle

\section{Introduction}\label{sec:intro}

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation
\cite{SchumacherWerner,Arrighi,Farrelly}.  After $N$ steps of a finite-range
walk, the propagator vanishes identically outside $N\Cmicro$.  Here
$\Cmicro=\operatorname{conv}F$ is the convex hull of the one-step jumps.
Many such walks have a conical point in their dispersion relation.  Near it,
the long-wavelength dynamics is that of a Weyl or Dirac equation with a
speed of light $\cIR$
\cite{BialynickiBirula,DArianoPerinotti,BDPT,DArianoErbaPerinotti}.

In spatial dimension $d\ge2$ the two causal structures cannot coincide.  The
infrared cone of a Weyl node is a Euclidean ball, and $\Cmicro$ is a
polytope.  Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice.  It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin \cite{BHS}, but that
setting lies outside the scope of this paper.  For a lattice walk, some
velocities are therefore causally allowed but not relativistic.  How much
physics can be sent through them?

Three questions must be kept apart.

\begin{description}
\item[(U) Ultraviolet propagator] Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside $N\Cmicro$?  For
  the walk studied here it does: along the eight vertex rays a single
  lattice path contributes, with amplitude of norm $4^{-N}$
  (Proposition~\ref{prop:geometry}).  One-step Alice/Bob protocols built
  from localized operations turn this into a finite distinguishability
  (for instance $3/128$ after one step for a suitable localized
  preparation, as recorded in~\cite{Repo}).  Such protocols are broadband:
  their operations are not concentrated near the Weyl node.
\item[(I) Infrared operational response] Require the preparation, the
  encoder and the detector to be infrared-admissible, and put Bob outside
  the infrared cone of \emph{every} site of Alice.  Does Bob's
  distinguishability still fail to vanish as the infrared scale goes to
  zero, and at what rate?
\item[(N) Nature] Is there a physical system in which the lattice scale and
  the operations are given rather than engineered?  This question is not
  addressed here.
\end{description}

A non-zero ultraviolet kernel does not answer (I).  Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U).  This paper answers (I), for
one walk and one explicit protocol.

\subsection*{The walk}
We work with the Weyl walk of Cedzich, Joye, Werner and Werner
\cite[Eq.~(5.15)]{CJWW}.  They introduced it as a modification of the
Bialynicki-Birula Weyl automaton \cite[Eq.~(5.12)]{CJWW},
\cite{BialynickiBirula}, with the same conical points and with a
\emph{spherical} propagation region.  For this walk the three velocity sets
are nested as
\begin{equation}\label{eq:three-bodies}
\Gamma\;\subseteq\;B(1)\;\subsetneq\;\Cmicro=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=\cIR=1 .
\end{equation}
Here $B(1)=\overline B(0,1)$ is the closed infrared light cone ($\cIR=1$),
$\Gamma$ is the closed set of group velocities, and $\Cmicro$ is the strict
causal body.  Both statements in \eqref{eq:three-bodies} are exact, and
moreover $\partial B(1)\subseteq\Gamma$ (Proposition~\ref{prop:geometry}).
Numerically, $\Gamma$ fills the ball; this is not proved and not used.
Every ballistic mode, at every energy, therefore respects the emergent light
speed.  Nevertheless, in every non-axial direction $\hat n$ the causal
support extends to $\|\hat n\|_1\in(1,\sqrt3\,]$ times the light speed.
Probability outside $\Gamma$ is exponentially small in $N$ \cite{CJWW}.  The
question is whether it can be \emph{used} under infrared control.

\subsection*{Main results}
Section~\ref{sec:protocol} gives the precise definitions.  In outline,
Alice's region is the lattice ball $\cA_N$ of radius $N/4$ at the origin,
and Bob's region is the lattice ball $\cB_N$ of radius $N/4$ at $N(1,1,1)$.
After $N$ steps, every pair $(x,y)\in\cA_N\times\cB_N$ is separated by more
than $N+N/5$.  Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$.  The resource is a narrow-band packet of
momentum width $\Lambda=1/N$.  Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$.  Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$.  The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish quadratically
on the spheres.

\begin{enumerate}[label=(\roman*)]
\item \emph{Infrared admissibility} (Theorem~\ref{thm:admissible}).  All
  eight operations map the band $|p|\le N^{-1}$ into the band
  $|p|\le N^{-1/2}$, up to relative errors $O(N^{-1/2})$ with explicit
  constants.  Single-site operations fail this criterion maximally
  (Lemma~\ref{lem:point}).
\item \emph{Explicit upper bound} (Theorem~\ref{thm:upper}).  For every
  $N\ge2$, every unitary acting in $\cA_N$, every one-particle state and
  every effect in $\cB_N$, Bob's distinguishability is at most
  $36N^4e^{-JN}$, with $J=(1-\tfrac{\sqrt3}{2})\log2$.  Polynomial infrared
  signalling is excluded.
\item \emph{Regional rate} (Theorem~\ref{thm:rate}).  The kernel between
  the two regions is $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal
  regional value of a Legendre rate function.  Here $I$ is the Legendre
  transform of $\Phi(\xi)=\arcosh(\prod_j\cosh\xi_j)$, and
  $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
  regional velocity set.  Moreover $J<K_*<\log4$.  By (iv), the rate $K_*$
  is attained by an explicit response.
\item \emph{Leading asymptotics} (Theorem~\ref{thm:main}).  For all sixteen
  encoder--detector pairs,
  $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
  The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
  uniformly non-zero, with relative oscillation in $\theta$ at most
  $1.5\times10^{-3}$.
\end{enumerate}

Result (iv) is an asymptotic statement and not a numerical approximation
valid from small $N$.  The constants in its remainder are not explicit, and
neither is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is
guaranteed.  Finite-$N$ diagnostics (Appendix~\ref{app:numerics}) indicate
a relative correction of about $-100/N$, so the leading term is
quantitatively accurate only for $N\gtrsim10^3$.  For the pairs with the
smallest coefficients, the next-order term $N^{-17/2}e^{-K_*N}$ dominates
throughout the diagnostic range $N\le56$ (Remark~\ref{rem:features}).

The coefficient is not a product of local factors.  It arises from the
interference between the \emph{free tail} of the resource at Bob, which is
only polynomially small, and the part of Alice's encoding that reaches Bob,
which is exponentially small.  Two points of the complex-shifted Brillouin
torus contribute, and they enter with different projectors.  The power
$13/2$ is not a count of Gaussian directions.  The two normal directions are
discrete sums over lattice planes of depth $O(1)$, and the common tangential
direction is a flat direction of the exponent that is confined only by the
profiles.

\subsection*{Relation to the literature}
Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical \cite{Konno,GJS,AVWW}: $Q(t)/t$ converges in
distribution to the group velocity distributed by the initial state.
Cedzich, Joye, Werner and Werner \cite{CJWW} proved that the probability of
velocities outside the support of this limit decays exponentially.  They gave
a method for bounding the rate uniformly in the initial state and discussed
the ``fuzziness'' of the emergent light cone in exactly this language.  Our
upper bound (ii) uses their contour-shift idea, supplemented by an elementary
ellipse lemma and a Jordan-safe bound on matrix powers.  Their method bounds
rates; it does not give prefactor-level asymptotics.

Sharp asymptotics with prefactors outside the propagation region are known
in one dimension.  Sunada and Tate \cite{SunadaTate} obtained exact local
asymptotics of transition probabilities, including exponential decay with an
explicit prefactor in the region hidden from the weak limit.  Carteret,
Richmond and Temme \cite{CRT} obtained uniformly convergent asymptotics in
the exponentially decaying regions of coined walks on the line.  These are
the closest precursors of the saddle-point analysis of
Section~\ref{sec:asymptotics}.  In two dimensions, Baryshnikov, Brady,
Bressler and Pemantle \cite{BBBP} analysed quantum walks through multivariate
generating functions and determined the limiting profile in the feasible
region, outside of which the probability is exponentially small.  Analytic
combinatorics in several variables \cite{ACSV} provides general transfer
theorems for multivariate coefficient asymptotics, whose standard sharp
forms assume minimality hypotheses on the critical points.  We do not claim
that these methods cannot reproduce the present result.  We are not aware of
a transfer theorem that yields it directly, and we carry out the
model-specific saddle-point analysis explicitly.

What we add is a \emph{lower} bound, in the strong form of exact leading
asymptotics.  It concerns an \emph{operational} quantity: the
distinguishability produced by a local encoding.  The encoding is spread
over a region of size $O(N)$ and constrained to be infrared-admissible, in
dimension three, and at a point strictly inside the corona.  Upper bounds
alone cannot distinguish an exponentially small response from an exactly
vanishing one.  In the problem studied here that distinction is the
content of the result.  The novelty claim is correspondingly narrow.  To our
knowledge, Theorem~\ref{thm:main} is the first prefactor-level asymptotic,
with a leading coefficient that is oscillatory and certified to be
non-vanishing, for an infrared-controlled operational response in the
strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk.  Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb--Robinson bounds \cite{LiebRobinson,BHV} give exponentially small
leakage outside a linear cone for continuous-time lattice dynamics.  For
quantum walks the strict cone $\Cmicro$ plays that role exactly, and the
question here is the one \emph{inside} it.

\subsection*{Organisation}
Section~\ref{sec:walk} sets up the walk and proves the geometric statements.
Section~\ref{sec:protocol} defines the protocol and infrared admissibility.
Section~\ref{sec:results} states the results.  Sections~\ref{sec:upper}
to~\ref{sec:asymptotics} contain the proofs.  Section~\ref{sec:discussion}
discusses scope and limitations.  Appendix~\ref{app:numerics} lists the
computer-assisted parts and the finite-$N$ diagnostics.

\section{The walk and its three velocity sets}\label{sec:walk}

\subsection{Conventions}
The one-particle Hilbert space is $\mathcal H=\ell^2(\Z^3;\C^2)$ with
internal basis $\up=(1,0)^T$ and $\dn=(0,1)^T$.  We use the Fourier
transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\T^3=[-\pi,\pi)^3$.  We write $c_j=\cos p_j$ and
$s_j=\sin p_j$.  $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of \cite[Eq.~(5.15)]{CJWW} has symbol
\[
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
\]
States evolve by the unitary $S$ with symbol
\begin{equation}\label{eq:symbol}
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\end{equation}
Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\C^3$.  For $p\in\C^3$, $S(p)$ denotes the continuation of
\eqref{eq:symbol}, which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$.  The $N$-step kernel is
\begin{equation}\label{eq:kernel}
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\end{equation}

\begin{lemma}[Jumps]\label{lem:jumps}
The set $F=\{d:S_d\ne0\}$ has fourteen elements: the eight vertices
$(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$, and the two
axial jumps $(\pm1,0,0)$.  Each vertex block is $\frac14$ times a rank-one
diagonal projector; in particular $S_{(1,1,1)}=\frac14|\dn\rangle\langle\dn|$.
The face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.
\end{lemma}

\begin{proof}
This is a direct expansion of \eqref{eq:symbol} in $z_j=e^{ip_j}$.  The
coefficient of $z_1z_2z_3$ comes only from the $(2,2)$ entry
$c_1c_2e^{ip_3}$ and equals $\frac14$.
\end{proof}

\subsection{Dispersion and the infrared node}
Since $\det S=1$ and $\tr S(p)=2c_1c_2c_3$, the eigenvalues of $S(p)$ are
$e^{\mp i\omega(p)}$ with
\begin{equation}\label{eq:dispersion}
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\end{equation}
At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with
\[
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
\]
This is a Weyl Hamiltonian with speed $\cIR=1$.  The same conical structure
occurs at the eight points of $\{0,\pi\}^3$.

\begin{proposition}[Geometry]\label{prop:geometry}
\begin{enumerate}[label=(\alph*)]
\item The causal body is $\Cmicro=\operatorname{conv}F=[-1,1]^3$.  Its
  support function is $h_{\Cmicro}(\hat n)=\|\hat n\|_1$ for unit vectors
  $\hat n$.
\item At every $p$ where $\omega$ is differentiable,
  \begin{equation}\label{eq:SOS}
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \end{equation}
  and hence $|\nabla\omega(p)|\le1$.  At the conical points $\nabla\omega$
  takes every value in the unit sphere.  Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set
  of group velocities.
\item For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector.  In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|\dn\rangle\langle\dn|$.  Hence the $N$-step
  support function equals $N\|\hat n\|_1$ exactly.
\end{enumerate}
\end{proposition}

\begin{proof}
(a) follows from Lemma~\ref{lem:jumps}.  The supremum of $\hat n\cdot x$ over
the cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$.  The identity \eqref{eq:SOS} is a polynomial identity
in $(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion.  Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$.  Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so
$\sum_k\sigma_i(d_k)_i=N$ forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$,
that is, $d_k=\sigma$.  Hence $(S^N)_{N\sigma,0}=S_\sigma^N$.  By Lemma~\ref{lem:jumps},
$S_\sigma=\frac14\Pi_\sigma$, so $S_\sigma^N=4^{-N}\Pi_\sigma$.
\end{proof}

\begin{remark}
The reverse inclusion $B(1)\subseteq\Gamma$, that is, that $\Gamma$ fills
the ball, holds numerically but is not proved and not used.  What is used is
the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le\cIR$, with equality by $\partial B(1)\subseteq\Gamma$.  Consequently the relation
$\sup|v_g|=\cIR$ does \emph{not} imply that the emergent cone coincides with
the causal boundary.  The two coincide only in the six axial directions.
The \emph{corona} is $\Cmicro\setminus B(1)$.  Propagation into $N$ times
the corona is not ballistic, but by (c) it is not forbidden.
\end{remark}

\begin{remark}
For the Bialynicki-Birula walk \cite[Eq.~(5.12)]{CJWW}, $\Gamma$ is contained
in the intersection of three orthogonal cylinders (and numerically equal to
it \cite[Fig.~5]{CJWW}).  It contains group velocities up to
$\sqrt{3/2}>\cIR$, attained at $p=-\frac\pi4(1,1,1)$.  In that walk the corona contains a ballistic sector
faster than the emergent light.  We restrict to \cite[Eq.~(5.15)]{CJWW}
precisely because it has no such sector.
\end{remark}

\section{Protocol and infrared admissibility}\label{sec:protocol}

Fix an integer $N\ge2$.  The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$.  Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write $\Pi=\Pi_{\Lambda_N}$
and $\Pi'=\Pi_{\Lambda'_N}$.  For $N\ge2$ both balls lie in $|p|<\pi/4$,
where $f>0$ and the only conical point is $p=0$.

\subsection{Regions}
Let
\[
\cA_N=\{x\in\Z^3:|x|\le N/4\},\qquad \cB_N=\{y\in\Z^3:|y-N(1,1,1)|\le N/4\},
\]
with Euclidean norms throughout.  For every $x\in\cA_N$ and $y\in\cB_N$,
\begin{equation}\label{eq:separation}
|y-x|-N\ge(\sqrt3-\tfrac32)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge(3-\tfrac{\sqrt3}2)N,\quad u=(1,1,1).
\end{equation}
Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$.  Each region has at most $(N/2+1)^3\le N^3$
sites.

\subsection{Resource, encoder, detector}
Let $g(q)=(1-|q|^2)_+^2$.  The resource is
\[
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,\dn,
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
\]
so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$.  In position space
$\phi_N=\varphi_N\,\dn$ with the real, radial function
\begin{equation}\label{eq:resource}
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\end{equation}
This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in $\cA_N$.  For
$M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the multiplication
operator
\[
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
\]
It acts as the identity outside $\cA_N$.  In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\cB_N$.
For $M_B\in\{I,P_1,P_2,P_3\}$, with $P_j=(I+\sigma_j)/2$, the effect is
\[
E=h_N\otimes M_B,\qquad 0\le E\le I .
\]

\subsection{Signal}
Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$ to
the resource.  After $N$ steps the state is
$\psi_b(N)=S^NU^{(b)}\phi_N$.  The signal is
\begin{equation}\label{eq:signal}
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\end{equation}
where $L_{M,M_B}(N)$ denotes the signed difference.  No spectral projection is
applied to the signal.  Infrared admissibility is a property of the
operations only.  We also consider the trace distance $D_B(N)$ between Bob's
reduced states.  In the free-fermion description, the reduced state of a
one-particle vector $\psi$ on the modes of $\cB_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

\subsection{Infrared admissibility}
\begin{definition}\label{def:admissible}
For a bounded operator $X$ on $\mathcal H$ with $X\Pi\ne0$, set
\[
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
\]
The encoder $U_M$ is \emph{infrared-admissible} if
$\eta_{\mathrm{op}}(U_M-I)\to0$ and
\[
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
\]
as $N\to\infty$, where $\Delta_M\ne0$ is required for $\eta_{\mathrm{enc}}^M$
to be defined.  The effect $E$ is infrared-admissible if
$\eta_{\mathrm{op}}(E)\to0$.
\end{definition}

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem~\ref{thm:admissible}).

In words: acting on anything in the infrared band, an admissible operation
leaves only a vanishing fraction of its output outside the wider band
$\Pi'$.  A strictly local gate cannot do this.

\begin{lemma}[Single-site operations are ultraviolet]\label{lem:point}
If $X\Pi\ne0$ and $\operatorname{ran}X\subseteq\ell^2(\{x_0\};\C^2)$ for a
single site $x_0$, then
$\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.
\end{lemma}

\begin{proof}
For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$.
\end{proof}

This is the reason the encoder is spread over a region of size $O(N)$ with
a smooth profile.  A pointlike phase gate, such as $I-2P_{x_0}$, is
excluded by Lemma~\ref{lem:point}.  The regional operations pass:

\begin{theorem}[Admissibility]\label{thm:admissible}
Let $K_e=\frac\pi2(2+8\sqrt3\pi)$, $K_d=\frac\pi2(1+16\sqrt3)$ and
$m=11/(560\pi^2\,32^3)$.  For all $N\ge32$, all four $M$ and all four
$M_B$,
\[
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
\]
All denominators are non-zero for every $N\ge2$.
\end{theorem}

The constants are conservative.  The proof is in Section~\ref{sec:admissible}.

\section{Results}\label{sec:results}

\begin{theorem}[Explicit upper bound]\label{thm:upper}
Let $N\ge2$ and $T_N=\|P_{\cB_N}S^NP_{\cA_N}\|$.  Then
\[
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
\]
Consequently, for every unitary $U$ acting as the identity outside
$\cA_N\otimes\C^2$, every one-particle state and every effect in $\cB_N$,
\[
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
\]
\end{theorem}

\begin{remark}[Formal verification]
Theorem~\ref{thm:upper} is machine-checked in Lean~4 with Mathlib
(\texttt{formal/} in~\cite{Repo}), for every $N\ge2$ and without
additional axioms.  This covers the kernel bound, the geometry
\eqref{eq:separation}, the counting of lattice points, the operator bound on
$T_N$, and the step $\delta\le4T_N$.  The formal proof bounds the matrix
powers through Cayley--Hamilton and entrywise estimates instead of
Lemma~\ref{lem:schur}, and obtains the sharper constant
$T_N\le4N^4e^{-JN}$.  Both constants are valid; the proof in
Section~\ref{sec:upper} keeps the constant $9$ that the elementary
Lemma~\ref{lem:schur} gives.  The identification of Bob's amplitudes with the
restricted walk, and the second-quantized distance $D_B$, are not
formalized.
\end{remark}

For $\xi\in\R^3$ put $\Phi(\xi)=\arcosh\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$
and define the rate function
\begin{equation}\label{eq:rate}
I(v)=\sup_{\xi\in\R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\end{equation}
Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$.  This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\cA_N,\cB_N$.

\begin{theorem}[Regional rate]\label{thm:rate}
\begin{enumerate}[label=(\alph*)]
\item $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
\item On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$.  The corresponding dual
  tilt is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$.  Moreover
  \[
  K_*:=I(v_*)=3\alpha t_*-\arcosh(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  \]
\item $J<K_*<\log4$.  Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
\item For all $N\ge2$ and all $(x,y)\in\cA_N\times\cB_N$,
  \[
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  \]
  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.
\end{enumerate}
\end{theorem}

The main result identifies the exact leading behaviour of every signal in
the family.  Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

\begin{theorem}[Leading asymptotics]\label{thm:main}
For each of the sixteen pairs $(M,M_B)$ there is a continuous, $1$-periodic,
real function $C_{M,M_B}(\theta)$ such that, as $N\to\infty$,
\[
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
\]
Explicitly,
\begin{equation}\label{eq:C}
C_{M,M_B}(\theta)=\cK\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\end{equation}
with the constants $\cK$, $c_r$, the functions $\Gamma_\pm$ and the numbers
$\ell_0,\ell_\pi$ defined in Section~\ref{sec:asymptotics}.  For every pair,
\[
C_{M,M_B}(\theta)=\overline C_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline C_{M,M_B}\ne0,
\]
with the values in Table~\ref{tab:C}.  Consequently, for every pair,
\[
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\]
and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.
\end{theorem}

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$.  Theorem~\ref{thm:main} therefore does not
assert $\delta_{M,M_B}(N)>0$ at any specified $N$.  It also does not say from
which $N$ on the leading term is numerically accurate
(Section~\ref{sec:discussion}).

\begin{table}[t]
\centering
\small
\begin{tabular}{llrr}
\toprule
$M$ & $M_B$ & $\overline C_{M,M_B}$ & $\sup_\theta|C/\overline C-1|$\\
\midrule
$I$ & $I$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$I$ & $P_1$ & $+1.2072650683$ & $1.09\cdot10^{-3}$\\
$I$ & $P_2$ & $+0.8164098576$ & $1.08\cdot10^{-3}$\\
$I$ & $P_3$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_1$ & $I$ & $-3.7206303938$ & $1.05\cdot10^{-3}$\\
$\sigma_1$ & $P_1$ & $-1.5567800857$ & $1.06\cdot10^{-3}$\\
$\sigma_1$ & $P_2$ & $-2.8203960182$ & $1.02\cdot10^{-3}$\\
$\sigma_1$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $I$ & $-2.9389199724$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $P_1$ & $-0.5846543741$ & $1.02\cdot10^{-3}$\\
$\sigma_2$ & $P_2$ & $-1.7729950974$ & $1.04\cdot10^{-3}$\\
$\sigma_2$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_3$ & $I$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_3$ & $P_1$ & $-1.2072650683$ & $1.09\cdot10^{-3}$\\
$\sigma_3$ & $P_2$ & $-0.8164098576$ & $1.08\cdot10^{-3}$\\
$\sigma_3$ & $P_3$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
\bottomrule
\end{tabular}
\caption{Mean leading coefficients $\overline C_{M,M_B}=\cK c_r\overline\Gamma\ell_0$
and the uniform bound on their relative oscillation in $\theta$.  Values are
certified by interval arithmetic (Appendix~\ref{app:numerics}).}
\label{tab:C}
\end{table}

\begin{corollary}\label{cor:suppressed}
In this protocol the emergent light cone is not operationally sharp for
infrared-admissible operations.  For each pair the response is
non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every $k$.  It is
nevertheless non-zero for all large $N$, with the exact rate $K_*$, the exact
power $13/2$ and an explicit non-vanishing coefficient.
\end{corollary}

\begin{remark}\label{rem:features}
Three features of Table~\ref{tab:C} were not assumed and come out of the
computation.  First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order;
the two encoders differ only at lower orders.  Second, the three Pauli
encoders are not equivalent: with $M_B=I$ they give three different
coefficients.  Third, for $M=\sigma_2$ the two contributing saddles enter with
the same sign for every detector: $\ell_0$ and $\ell_\pi$ of
Appendix~\ref{app:numerics} have the same sign.  Since $\Gamma_+>0$ and
$\Gamma_-\ge0$ (Lemma~\ref{lem:depth}), non-vanishing then follows without
the margin estimate in the proof of Theorem~\ref{thm:main}, so for this
encoder the non-cancellation mechanism is particularly transparent.  The smallest coefficients,
$|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$ with
$M_B\in\{I,P_3\}$.  For these two encoders with $M_B=I$, the diagnostics of
Appendix~\ref{app:numerics} show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.
\end{remark}

\begin{remark}[Methodology]
The protocol (regions, profiles, encoders, detectors, scalings
$\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the encoding angle $\pi/2$) was fixed before
the asymptotic analysis and was not tuned afterwards.  The family of
encoders and detectors is not exhaustive: a general generator
$M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk relating
the directions $\hat n\cdot\sigma$ has been established.
\end{remark}

\section{Proof of the upper bounds}\label{sec:upper}

\subsection{An ellipse lemma}
For $a\ge1$ let
$E_a=\{z\in\C:(\re z)^2/a^2+(\im z)^2/(a^2-1)\le1\}$, where $E_1=[-1,1]$.
These are the confocal ellipses with foci $\pm1$.  The Joukowski map
$\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle $|\lambda|=r\ge1$
onto $\partial E_{(r+r^{-1})/2}$.

\begin{lemma}\label{lem:ellipse}
Let $a,c\ge1$.  If $z\in\partial E_a$ and $w\in E_c$, then $zw\in E_{ac}$;
consequently $E_aE_c\subseteq E_{ac}$.  If moreover $a,c>1$, then
$zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.
\end{lemma}

\begin{proof}
If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and symmetry.  If
$a=1$, then $z\in[-1,1]$ and the same argument applies.  So let $a,c>1$.
Write
$z=a\cos p+i\sqrt{a^2-1}\sin p$ and $w=c\,x+i\sqrt{c^2-1}\,y$ with
$x^2+y^2\le1$.  In the coordinates adapted to $E_{ac}$, the point $zw$
corresponds to $L(x,y)^T$ with
\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]
With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives
\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
\]
Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$.  If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is
interior.  If $u=1$, then $z=\pm a$ and
\[
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
\]
whose second entry is $<1$.  Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$.
\end{proof}

\begin{lemma}\label{lem:specrad}
For $\eta\in\R^3$ and $\xi\in\R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$.  If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.
\end{lemma}

\begin{proof}
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma~\ref{lem:ellipse} applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$.  When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$.  The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$.
If $|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$.  Since the
ellipses are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is
$r\le e^{\Phi(\xi)}$, with strict inequality when $f$ is interior.  On
$\Sigma$, $f=\pm\prod\cosh\xi_j$ is real and equality holds.
\end{proof}

\begin{lemma}[Powers without a gap]\label{lem:schur}
Let $T$ be a $2\times2$ matrix with $\rho(T)\le e^{\varkappa}$ and
$\|T\|\le\beta$.  Then $\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.
\end{lemma}

\begin{proof}
Take a unitary Schur form $T=V\begin{psmallmatrix}\lambda_1&b\\0&\lambda_2\end{psmallmatrix}V^*$,
so $|b|\le\|T\|$.  The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$.  The diagonal part has norm
$\max_j|\lambda_j|^N$.
\end{proof}

\subsection{Proof of Theorem~\ref{thm:upper}}
Since the integrand in \eqref{eq:kernel} is entire and $2\pi$-periodic in
each variable, the contour can be shifted to $p=\eta-i\xi$ for any
$\xi\in\R^3$ without boundary terms:
\begin{equation}\label{eq:tilt}
G_N(d)=e^{-\xi\cdot d}\int_{\T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\end{equation}
Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$.  Lemma~\ref{lem:specrad}
gives
\[
\rho\bigl(S(\eta-itu)\bigr)\le\exp\arcosh(125/64)<4,
\]
because $125/64<17/8=\cosh\log4$.  By Lemma~\ref{lem:jumps},
\[
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
\]
Lemma~\ref{lem:schur}, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$.  With
\eqref{eq:separation},
\[
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
\]
for all $(x,y)\in\cA_N\times\cB_N$.  The Schur test with $|\cA_N|,|\cB_N|\le N^3$
gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$.  Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$.  The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$ on
the one-particle block, together with $-\tr X$ on the vacuum block.  Hence
$D_B=\frac12(|\tr X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
\qed

\subsection{Proof of Theorem~\ref{thm:rate}}
(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$).  The inequality
$\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$, applied twice, gives
$\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.  Since
$\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$.  Finally $I=+\infty$ outside
$\operatorname{conv}F$ by \cite[Lemma~4.1]{CJWW}.  Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with
\[
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
\]
On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$.  It is strictly increasing, since
$3h'(t)=u^T\Hess\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is given by the
formula of Lemma~\ref{lem:symbol}(d) with $c_*$ replaced by $\cosh t>1$.  Since
$\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with $h(t_*)=\alpha$, and
then $\nabla\Phi(\xi_*)=v_*$.  Solving $h(t)=\alpha$ for $\cosh^2t$ gives the
stated closed form.  By the definition of $I$, for every $v$,
\[
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\uhat\cdot v-|v_*|\bigr),
\qquad \uhat=u/\sqrt3 .
\]
On $V_{\mathrm{reg}}$ we have $\uhat\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$.  Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\arcosh(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$.  Along the diagonal,
$3t-\arcosh(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also the exact
vertex rate of Proposition~\ref{prop:geometry}(c).  The numerical values are
enclosed by interval arithmetic.

(d) Apply \eqref{eq:tilt} with $\xi=\xi_*$.  By Lemma~\ref{lem:specrad},
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$.  By
Lemma~\ref{lem:jumps}, $\|S(\eta-i\xi_*)\|\le4e^{3t_*}$.
Lemma~\ref{lem:schur} gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$.  For
$(x,y)\in\cA_N\times\cB_N$, \eqref{eq:separation} and $\xi_*\parallel\uhat$
give $\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and
$N\xi_*\cdot v_*-N\Phi_*=NK_*$.  Numerically $4e^{3t_*-\Phi_*}<9.2$, so
$1+4e^{3t_*-\Phi_*}N\le1+10N$, and the Schur test concludes as before.
\qed

\section{Proof of admissibility}\label{sec:admissible}

\begin{lemma}\label{lem:IR1}
Let $a:\Z^3\to M_2(\C)$ satisfy $\sup\|a\|\le A$ and
$\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$.  Then
\[
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
\]
\end{lemma}

\begin{proof}
Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$.  On the complement of $\Pi'$,
\[
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
\]
using $\sin s\ge2s/\pi$ on $[0,\pi/2]$.  By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$.  For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$.  The
discrete product rule
$D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's inequality give
$(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:admissible}]
\emph{Numerators.}  $|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside
$\cA_N$, and the gradient vanishes on the sphere, so $F_N$ is
$16/N$-Lipschitz on $\Z^3$.  For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$,
because $\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$.  For $E=h_N\otimes M_B$ we get
$A=1$ and $L=16$.  Lemma~\ref{lem:IR1} bounds the numerators by
$K_eN^{-1/2}$ and $K_dN^{-1/2}$.  For $\eta_{\mathrm{enc}}$, write
$v=U_M\phi_N$, $w=\Pi'v$ and $r=v-w=(I-\Pi')a_M\phi_N$.  Since
$\Pi'\phi_N=\phi_N$, $\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$,
whose trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

\emph{Denominators.}  For $|x|\le N$ and $|p|\le N^{-1}$, $\cos(p\cdot x)\ge\frac12$.
Hence $\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$.
Let $N\ge32$, and consider two auxiliary sets.  The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$.  The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$.  Each carries resource
weight at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$.  Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$.  For the detector, test
on the resource translated to $N(1,1,1)$, with internal state a
$+1$ eigenvector of $M_B$.  This test vector lies in $\operatorname{ran}\Pi$,
and it gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle\dn|e^{i\pi F_N(x)M/2}|\dn\rangle$.  This gives $t_x=e^{i\pi F_N/2}$
for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and $e^{-i\pi F_N/2}$ for
$M=\sigma_3$.  Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\re t_x\bar t_y)$.  All terms are non-negative,
and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\re t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$.  Counting both orders
gives $1-|z|^2\ge(2-\sqrt2)m^2$.  For $2\le N<32$ the same argument, with
the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows that the
denominators are non-zero.
\end{proof}

\section{Proof of the leading asymptotics}\label{sec:asymptotics}

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line.  The constants $r_0,c,c_3,c_P$ below are finite
but not made explicit.

\subsection{Reduction to one interference functional}
Let $P_B$ be the restriction to $\cB_N$ (not a spectral projection).  Write
$\widetilde r=S^N\phi_N$ for the free evolution of the resource on all of
$\Z^3$, and put
\[
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N\dn),\qquad
a_\up=P_BS^N(s_N\varphi_N\up),\qquad a_\dn=P_BS^N(s_N\varphi_N\dn).
\]
Since $\sigma_1\dn=\up$, $\sigma_2\dn=-i\up$ and $\sigma_3\dn=-\dn$, Bob's
encoded amplitude $P_B\psi_1$ is $v+ia_\dn$, $v+ia_\up$, $v+a_\up$ or
$v-ia_\dn$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.  Expanding
\eqref{eq:signal} with $E$ supported in $\cB_N$,
\begin{equation}\label{eq:Lexp}
\begin{aligned}
L_{I}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\dn\rangle+Q_I, &
L_{\sigma_3}&=2\re\langle r,Ea_c\rangle+2\im\langle r,Ea_\dn\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\up\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\re\langle r,Ea_c\rangle+2\re\langle r,Ea_\up\rangle+Q_{\sigma_2}.
\end{aligned}
\end{equation}
Each $Q_M$ is a sum of terms quadratic in $(a_c,a_\up,a_\dn)$.  For
example, $Q_I=\langle a_c,Ea_c\rangle+\langle a_\dn,Ea_\dn\rangle-2\im\langle a_c,Ea_\dn\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem~\ref{thm:rate}(d), $a_c,a_\up,a_\dn$ have $\ell^2$-norm at most
$T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$.  The free tail is only polynomially
small (Lemma~\ref{lem:tail}).  The $e^{-K_*N}$ sector therefore consists of
the linear interference terms.  Define, for $\chi\in\{\up,\dn\}$,
\[
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
\]
Theorem~\ref{thm:main} follows from Theorem~\ref{thm:T} below.  The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
because $c_N=\Theta(N^{-4})$ in the relevant layer while $s_N=\Theta(N^{-2})$.

\subsection{Exact tilted representation}
Let $R=N/4$, $x_*=R\uhat$ and $y_*=N u-R\uhat$, so that $y_*-x_*=Nv_*$.  For
$f$ supported in $\cA_N$ and $w$ supported in $\cB_N$, put
\[
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
\]
Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$.  By \eqref{eq:tilt}
with $\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,
\begin{equation}\label{eq:exactrep}
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\end{equation}
This identity is exact: the sums are finite and no poles are crossed.

\subsection{The tilted symbol}\label{ssec:tilted}
\begin{lemma}\label{lem:symbol}
\begin{enumerate}[label=(\alph*)]
\item $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$.  At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,
  \[
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  \]
  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is
  \[
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  \]
\item For all $p\in\C^3$: $S(p+\pi e_1)=-S(p)$, $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
\item The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\Z^3:u_1+u_2+u_3=0\}$ is trivial if and only if
  $\eta_0\in\{0,\pi u\}$.
\item There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and
  \[
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  \]
  Here $Q=\Hess\Phi(\xi_*)=q_t(I-\uhat\uhat^T)+q_n\uhat\uhat^T$ with
  \[
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  \]
\item Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) and (b) are identities between trigonometric polynomials and are checked
by expansion.  (c): $\Lambda_0$ is generated by $e_1-e_2$ and $e_2-e_3$, so
the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$.  (d): the
eigenvalues of $S(\eta-i\xi_*)$ are
$\exp(\pm\arcosh f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$.  Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$.  Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\Hess\Phi(\xi_*)=Q$.  The explicit Hessian is
$\Hess\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$.  The eigenvalues $\lambda^{\pm1}$ are separated
by the gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic.
(e): by Lemma~\ref{lem:specrad} and compactness,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from $\Sigma$.  Conclude with
Lemma~\ref{lem:schur}.
\end{proof}

By (b), near $\pi u$ we have $S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$,
whose Perron projector is $P^T=\overline P$.  The other six points of
$\Sigma$ have the same spectral radius, but by (c) their characters are
non-trivial on the lattice planes $u\cdot x=k$.  This is why only $0$ and
$\pi u$ contribute at leading order (Lemma~\ref{lem:layers}(d)).

\subsection{Lattice-plane coordinates and profiles}
The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a translate
of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.  Write
Alice's sites as $x=x_*-\delta\uhat+u_\perp$ with $u_\perp\perp\uhat$ and
depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$.  Since $u\cdot x\in\Z$,
\[
\sqrt3\,\delta=\theta_N+j,\qquad j\in\Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
\]
Similarly $y=y_*+\delta'\uhat+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$, with
the \emph{same} $\theta_N$.  Then
$\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and $\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$.
Moreover $u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,
\[
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
\]
and therefore
$s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.  The
same holds for $h_N$ with $\delta'$ and $u'_\perp$.  Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

\subsection{The free tail}
\begin{lemma}\label{lem:tail}
Uniformly in $y\in\Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where
\[
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]\dn,
\]
\[
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
\]
At the facing point $w_*=u-\uhat/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\uhat$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in $y\in\cB_N$,
and $r=0$ outside $\cB_N$.
\end{lemma}

\begin{proof}
For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic, and
$H-H_W=O(|p|^2)$.  Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$.  With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$.  The resource enters through $g(Np)$ and is not
truncated.  The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$.  The value of $H_W(\uhat)\dn=(1+i,-1)^T/\sqrt3$ follows
by direct computation.
\end{proof}

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$.  We write
$\varphi_\partial=c_rI_b$.

\subsection{Layer sums}
Let $\Psi_\delta(\tau)=\int_{\R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$.  Define
\[
\cS_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\R^2}e^{-q_t|\tau|^2}\,\cS_\pm(\tau;\theta)^2\,d^2\tau .
\]

\begin{lemma}[Depth sums]\label{lem:depth}
Let $c_g=2\pi/(3\sqrt3)$ and $s_\omega=t_*+i\omega$.  Then
\[
\cS_+=\sum_{n\in\Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\cS_-=\sum_{n\in\Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
\]
Consequently $|\cS_+-\hat g_\tau(0)|\le c_g/720$ and $|\cS_-|\le c_g/48$.
Moreover
\[
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
\]
with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.
\end{lemma}

\begin{proof}
Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$.  So $H'''=2J_0(|\tau|\sqrt\delta)$
and $H(0)=H'(0)=H''(0)=0$.  Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated.  It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\Z)$.  Poisson summation is
therefore exact.  The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$.  The Gaussian integrals are elementary.
\end{proof}

\begin{lemma}[Layers]\label{lem:layers}
Let $\chi\in\{\up,\dn\}$, $f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and
$\tau=\sqrt{N/2}\,\eta_t$, where $\eta=\eta_n\uhat+\eta_t$ with
$\eta_t\perp\uhat$.
\begin{enumerate}[label=(\alph*)]
\item $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
\item For $|\eta|\le r_0$,
  \[
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\cS_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\cS_+(\tau;\theta_N)+\mathcal E_B\bigr],
  \]
  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
\item Near $\pi u$ the same holds with $\cS_-$ in place of $\cS_+$.  The
  alternating sign comes from the parity $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$,
  combined with $S^N\mapsto(-1)^N(S^N)^T$.
\item For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Decompose the sums into lattice planes.  On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$.  The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size $O(N^{-7/2}\delta^2)$.
Planes with $\delta>R/2$ contribute $O(e^{-cN})$.  This gives (a).

For (b), apply Poisson summation on each plane.  The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$.  The
terms $m\ne0$ are bounded by $\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$,
since the profile vanishes quadratically on the rim and its third
derivative is a finite measure.  After the weighted depth sum, they give a
relative error $O(N^{-3/2})$.  In the $m=0$ term, use the profile
expansions, $\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$.  With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,
\[
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
\]
Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$ gives
the prefactor of $\mathfrak A_f$.  For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$, using
Lemma~\ref{lem:tail}, the smoothness of $R_0$ and $M_B^\dagger=M_B$.  (c)
follows from Lemma~\ref{lem:symbol}(b) and the parity identity.  (d): by
Lemma~\ref{lem:symbol}(c), the character is non-trivial on each plane.  The
Poisson sum therefore has no $m=0$ term, and the remaining terms are
$O(N^{-4})$.
\end{proof}

\subsection{Assembly}
\begin{theorem}\label{thm:T}
For $\chi\in\{\up,\dn\}$ and each $M_B$,
\[
\mathcal T_\chi(N)=N^{-13/2}\,\cK\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
\]
where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and
\[
\cK=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
\]
\end{theorem}

\begin{proof}
Insert Lemmas~\ref{lem:symbol} and~\ref{lem:layers} into
\eqref{eq:exactrep}.  Away from the balls $B(\eta_0,r_0)$ the contribution is
$O(Ne^{-cN}N^{-5})$.  The six points of $\Sigma$ with non-trivial
characters give $O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the
Gaussian decay of $\widetilde S_N$.  Near $\eta_0\in\{0,\pi u\}$ we make
three replacements.  First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced
by $e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.  Third,
the integral is extended to $\R^3$, at cost $O(e^{-cNr_0^2})$.  What
remains is
\[
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\R^2}e^{-q_t|\tau|^2}\cS_\pm^2\,d^2\tau .
\]
Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:main}]
By \eqref{eq:Lexp}, the $e^{-K_*N}N^{-13/2}$ sector of $L_{M,M_B}$ is
$\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear functional
$-2\im$ for $M\in\{I,\sigma_1\}$, $+2\im$ for $M=\sigma_3$ and $+2\re$ for
$M=\sigma_2$, and $\chi=\dn$ for $M\in\{I,\sigma_3\}$, $\chi=\up$ for
$M\in\{\sigma_1,\sigma_2\}$.  Since $\cK$, $c_r$ and $\Gamma_\pm$ are real,
Theorem~\ref{thm:T} gives \eqref{eq:C} with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$.  Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in
Appendix~\ref{app:numerics}.

The remainder budget, relative to $N^{-13/2}$, is as follows:
\begin{itemize}
\item $O(N^{-1/2})$ from the cubic term of the exponent, from
  $P(\eta)-P$, from the normal phase, and from the variation of
  $\varphi_N$ and $R_0$ across the layer;
\item $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
\item $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
\item $O(N^{-2})$ from $2\re\langle r,Ea_c\rangle$;
\item exponentially small terms from the region away from $\Sigma$ and from
  the sector $e^{-2K_*N}$.
\end{itemize}
Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$.  For every pair, interval
arithmetic certifies $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$.
Therefore $C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline C-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table~\ref{tab:C}.  Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow.
\end{proof}

\begin{remark}[Counting the power]
The exponent $13/2$ decomposes as follows.  The resource contributes
$\frac32$ at the layer and the free tail $\frac32$ at Bob.  The profiles
$s_N$ and $h_N$ contribute $2+2$.  The two in-plane areas contribute $-2$.
The normal Gaussian contributes $\frac12$, and the tangential rescaling
$d^2\eta_t=(2/N)d^2\tau$ contributes $1$.  The depths $j,j'$ are discrete
sums of size $O(1)$ and contribute no power.  The common tangential
direction $u_\perp+u'_\perp$ is a flat direction of the exponent, because
$\xi_*$ is orthogonal to the planes.  It is confined by the profiles and
produces the area factors, not a Gaussian factor.
\end{remark}

\begin{remark}[Dependence on $\theta_N$]
Since $\sqrt3/4\notin\mathbb Q$, the sequence $\theta_N$ is equidistributed.
$C(\theta_N)$ is therefore quasi-periodic in $N$ and not a constant.  The
oscillation comes from the commensurability of the lattice planes with the
spheres bounding the regions.  It is below $0.15\%$, and it never changes
the sign.
\end{remark}

\section{Discussion}\label{sec:discussion}

\subsection{What the theorem says and does not say}
The theorem is a statement about one walk and one explicitly specified
family of operations.  It shows that the gap between the emergent
relativistic cone and the microscopic causal support is not merely
geometric.  Under an infrared-controlled protocol it carries an
operational response whose asymptotic law is known exactly: rate, power
and coefficient.  It does not claim that $D_B>0$ for every protocol, that
every quantum walk behaves this way, or that every smooth encoder
$M=aI+b\cdot\sigma$ signals.  It is not a violation of the model's
microcausality, since Bob remains inside $N\Cmicro$.  The limit
$N\to\infty$ is an infrared scaling at fixed lattice units, not a continuum
limit $a,\tau\to0$.

The result is asymptotic.  The remainder constants and $N_*$ are finite but
not explicit.  The finite-$N$ diagnostics of Appendix~\ref{app:numerics}
indicate an effective relative correction of about $-100/N$.  The leading
formula is therefore quantitatively reliable only for $N\gtrsim10^3$.  For
$M\in\{I,\sigma_3\}$ with $M_B=I$, whose coefficient is among the smallest,
the $N^{-17/2}$ term dominates over the whole diagnostic range.

\subsection{Physical reading}
Restoring a lattice spacing $a$, the integer $N$ is both the number of
steps and the separation scale in lattice units, so $N\sim\ell/a$ for a
separation $\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors.  The
response is therefore negligible at any separation large compared with the
lattice spacing, and by the preceding subsection the leading formula becomes
accurate only for $N\gtrsim10^3$.  We make no claim about observability, and
regard the result as a statement in the mathematical physics of finite-range
unitary dynamics.
Its interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $\cIR$, and operational influence,
which does not vanish inside the corona even under infrared control.

\subsection{Open problems}
\begin{enumerate}[label=(\arabic*)]
\item General encoders $M=aI+b\cdot\sigma$, and optimisation over
  admissible operations.
\item Other walks, in particular the Bialynicki-Birula walk
  \cite[Eq.~(5.12)]{CJWW}, whose corona contains ballistic modes faster than
  $\cIR$, and the massive Dirac case.
\item Explicit remainder constants and $N_*$, which would make the
  statement effective at finite $N$.
\item Many-particle and second-quantized versions.  The upper bound
  extends to even local unitaries on the full CAR algebra, with prefactor
  $288N^7$ in place of $36N^4$~\cite{Repo}, but no lower bound is available
  there.
\end{enumerate}

\appendix

\section{Computer-assisted parts and diagnostics}\label{app:numerics}

Theorem~\ref{thm:upper}, together with Lemma~\ref{lem:ellipse}, is
formally verified in Lean~4/Mathlib (\texttt{formal/} in~\cite{Repo}).  The
asymptotic results (Theorems~\ref{thm:rate} and~\ref{thm:main}) are not.
The analytic arguments above are complete up to the following verified
computations.  All of them are performed by the certificate scripts listed
in~\cite{Repo}, at the commit given there, with Python~3.12.3, SymPy~1.14.0
and mpmath~1.3.0.  Exact identities use SymPy.  Enclosures use the interval
context \texttt{mpmath.iv} with 50 digits, and only its elementary
operations: the four arithmetic operations, integer powers by repeated
multiplication, $\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$.
No interval quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$
and $I_b$ are enclosed through exact closed forms in $\sin$ and $\cos$,
obtained from the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$,
which are checked symbolically.
\begin{itemize}
\item The symbol identities: Lemma~\ref{lem:jumps}, \eqref{eq:SOS}, and
  Lemma~\ref{lem:symbol}(a)--(b).  Also the ellipse-lemma polynomials,
  $\cosh^3(\log2)=125/64$ and the vertex blocks.
\item Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$,
  $q_t$, $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$, $\cK$,
  $\overline\Gamma$ and $\varepsilon_\pm$.
\item The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table~\ref{tab:C}, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.
\end{itemize}
Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$.  The rows for
$\sigma_3$ are the negatives of the rows for $I$.

{\small
\[
\begin{array}{lll}
\toprule
(M,M_B) & \ell_0 & \ell_\pi\\
\midrule
(I,I),(I,P_3) & -\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2} & +\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}\\[3pt]
(I,P_1) & \frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2} & -\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}\\[3pt]
(I,P_2) & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2} & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}\\[3pt]
(\sigma_1,I) & -\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c} & \frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}\\[3pt]
(\sigma_1,P_1) & -\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2} & \frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_2) & -\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2} & -\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_3),(\sigma_2,P_3) & -\frac{\sqrt3}{3}B(1-\alpha) & -\frac{\sqrt3}{3}B(1-\alpha)\\[3pt]
(\sigma_2,I) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}\\[3pt]
(\sigma_2,P_1) & -\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2} & -\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}\\[3pt]
(\sigma_2,P_2) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}\\
\bottomrule
\end{array}
\]
}

\medskip\noindent\emph{Finite-$N$ diagnostics.}  These are floating-point
and not used in any proof; they use NumPy~1.26.4 and are produced by the
\texttt{--diagnostics} option of the coefficient certificate~\cite{Repo}.  A
floating-point FFT evaluation of the exact discrete convolution formula in
tilted variables (``brute'') was compared with a reference that keeps the
exact lattice geometry but replaces the kernel by its Gaussian form at the
eight points of $\Sigma$.  Their ratio tends to $1$ with deviation of order
$c/N$, $c\in[-0.5,14]$, at $N=24,40,56$.  For $M\in\{I,\sigma_3\}$ and
$M_B=I$, the ratio of the $N^{-17/2}$ piece $2\re\langle r,Ea_c\rangle$ to
the piece $2\im\langle r,Ea_\dn\rangle$ that carries the $N^{-13/2}$ term is
$15.2$, $9.4$ and $6.4$ at $N=24,40,56$.  A semi-analytic evaluation with discrete
planes and exact profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at
$N=10^3$, $10^4$ and $3\cdot10^4$, consistent with a relative correction
$\approx-100/N$.  The free tail agrees with $N^{-3/2}R_0$ to relative
accuracy $2\cdot10^{-6}$ at $N=40$ and $8\cdot10^{-9}$ at $N=640$.

\begin{thebibliography}{99}

\bibitem{AVWW}
A.~Ahlbrecht, H.~Vogts, A.~H.~Werner, R.~F.~Werner,
\emph{Asymptotic evolution of quantum walks with random coin},
arXiv:1009.2019.

\bibitem{Arrighi}
P.~Arrighi,
\emph{An overview of quantum cellular automata},
arXiv:1904.12956.

\bibitem{BBBP}
Y.~Baryshnikov, W.~Brady, A.~Bressler, R.~Pemantle,
\emph{Two-dimensional quantum random walk},
J.\ Stat.\ Phys.\ \textbf{142}, 78--107 (2011), arXiv:0810.5495.

\bibitem{BialynickiBirula}
I.~Bialynicki-Birula,
\emph{Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata},
Phys.\ Rev.\ D \textbf{49}, 6920 (1994), arXiv:hep-th/9304070.

\bibitem{BDPT}
A.~Bisio, G.~M.~D'Ariano, P.~Perinotti, A.~Tosini,
\emph{Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata},
arXiv:1601.04832.

\bibitem{BHS}
L.~Bombelli, J.~Henson, R.~D.~Sorkin,
\emph{Discreteness without symmetry breaking: a theorem},
arXiv:gr-qc/0605006.

\bibitem{BHV}
S.~Bravyi, M.~B.~Hastings, F.~Verstraete,
\emph{Lieb--Robinson bounds and the generation of correlations and topological quantum order},
Phys.\ Rev.\ Lett.\ \textbf{97}, 050401 (2006), arXiv:quant-ph/0603121.

\bibitem{CRT}
H.~A.~Carteret, B.~Richmond, N.~M.~Temme,
\emph{Evanescence in coined quantum walks},
J.\ Phys.\ A: Math.\ Gen.\ \textbf{38}, 8641--8665 (2005), arXiv:quant-ph/0506048.

\bibitem{CJWW}
C.~Cedzich, A.~Joye, A.~H.~Werner, R.~F.~Werner,
\emph{Exponential tail estimates for quantum lattice dynamics},
Ann.\ Henri Poincar\'e \textbf{27}, 2843--2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.

\bibitem{DArianoErbaPerinotti}
G.~M.~D'Ariano, M.~Erba, P.~Perinotti,
\emph{Isotropic quantum walks on lattices and the Weyl equation},
Phys.\ Rev.\ A \textbf{96}, 062101 (2017), arXiv:1708.00826.

\bibitem{DArianoPerinotti}
G.~M.~D'Ariano, P.~Perinotti,
\emph{Derivation of the Dirac equation from principles of information processing},
Phys.\ Rev.\ A \textbf{90}, 062106 (2014), arXiv:1306.1934.

\bibitem{Farrelly}
T.~Farrelly,
\emph{A review of quantum cellular automata},
Quantum \textbf{4}, 368 (2020), arXiv:1904.13318.

\bibitem{GJS}
G.~Grimmett, S.~Janson, P.~F.~Scudo,
\emph{Weak limits for quantum random walks},
Phys.\ Rev.\ E \textbf{69}, 026119 (2004), arXiv:quant-ph/0309135.

\bibitem{Konno}
N.~Konno,
\emph{Quantum random walks in one dimension},
Quantum Inf.\ Process.\ \textbf{1}, 345--354 (2002).

\bibitem{LiebRobinson}
E.~H.~Lieb, D.~W.~Robinson,
\emph{The finite group velocity of quantum spin systems},
Commun.\ Math.\ Phys.\ \textbf{28}, 251--257 (1972).

\bibitem{ACSV}
R.~Pemantle, M.~C.~Wilson, S.~Melczer,
\emph{Analytic Combinatorics in Several Variables}, 2nd ed.,
Cambridge University Press (2024), doi:10.1017/9781108874144.

\bibitem{Repo}
Repository \texttt{nacho09021973/qca-causal-cones},
% TODO(author): replace by an archived release (tag and DOI) before submission.
\url{https://github.com/nacho09021973/qca-causal-cones}, commit
\texttt{551addabe28b} (branch \texttt{research/b-infinity-post-s4-gate}).
Certificates
\texttt{scripts/verify\_scaled\_ir\_gate.py},
\texttt{scripts/verify\_regional\_directional\_asymptotics\_gate.py},
\texttt{scripts/verify\_regional\_laplace\_coefficient\_gate.py},
\texttt{scripts/verify\_directional\_saturation.py}; Lean formalization in
\texttt{formal/}.

\bibitem{SchumacherWerner}
B.~Schumacher, R.~F.~Werner,
\emph{Reversible quantum cellular automata},
arXiv:quant-ph/0405174.

\bibitem{SunadaTate}
T.~Sunada, T.~Tate,
\emph{Asymptotic behavior of quantum walks on the line},
J.\ Funct.\ Anal.\ \textbf{262}, 2608--2645 (2012), arXiv:1108.1878.

\end{thebibliography}

\end{document}
```


## Ronda 1 — CLAUDE OPUS

**Reconstrucción de la versión más fuerte de T1.** Despojado de retórica, T1 afirma exactamente esto: fijados $N\ge2$, un encoder $M$ y un detector $M_B$, y aceptado el contrato `TWO_DISTINGUISHABLE_CHANNELS` de la auditoría Schur §6 como definición [SOURCE], se tiene (i) $\Psi_b=r+bd$ con $r=U_N^NJ\phi_N$, $d=U_N^Nf$, $f=J(U_M-I)\phi_N$ de soporte finito; (ii) $L_c=2\operatorname{Re}\langle r,F_cd\rangle+\langle d,F_cd\rangle$; (iii) la amplitud de $d$ en Bob admite la reescritura exacta $Bd=e^{-K_*N}\mathcal Vt_N$ con $t_N=T^Ns$; (iv) por tanto $L_c$ se escribe como suma de cinco escalares (10a) una vez elegido un idempotente medible $P$; y (v) esos cinco escalares se conectan con la recurrencia (13)–(14) del precheck. T1 no afirma tamaño, orden, cancelación ni aditividad en dos términos: dice explícitamente que $B_{cPQ}$ no se anula y que repartirlo por convenio no probaría nada [SOURCE T1 §3]. Ésa es la versión fuerte, y es contra ella que hay que argumentar.

**Lo que he rehecho y no es objetable.** El desplazamiento de contorno: con $\hat\psi(p)=\sum_xe^{ip\cdot x}\psi(x)$ [SOURCE tex §2.1] y $(H_\xi v)(x)=e^{\xi_*\cdot(x-x_*)}v(x)$, sale $\mathcal FH_\xi v=e^{-\xi_*\cdot x_*}\hat v(\cdot-i\xi_*)$, y la conjugación de una convolución $\sum_dD_dv(\cdot-d)$ da símbolo $\sum_dD_de^{i(p-i\xi_*)\cdot d}=D(p-i\xi_*)$. El signo $p-i\xi$ de T1 (4) es el del TeX \eqref{eq:tilt} [SOURCE]; no hay error de convención [INFERENCE]. El factor exponencial: $\mathcal Vt_N(y)=\mathbf1_{\mathcal B}(y)e^{-\xi_*(y-y_*)}\Lambda^{-N}e^{\xi_*(y-x_*)}d(y)=e^{+K_*N}Bd(y)$ usando $y_*-x_*=Nv_*$ y $K_*=\xi_*\cdot v_*-\Phi_*$; luego (7) es exacta [INFERENCE]. Además, con $x_*=R\hat u$, $y_*=Nu-R\hat u$, $R=N/4$ [SOURCE tex §7.4], se comprueba $y_*-x_*=N(\sqrt3-\tfrac12)\hat u=N\alpha u=Nv_*$, y ambos pesos exponenciales son $\le1$ en sus regiones ($\hat u\cdot(y-y_*)\ge0$ en Bob, $\hat u\cdot(x-x_*)\le0$ en Alice): $\|\mathcal V\|\le1$ y $\|s\|\le\|f\|$ [INFERENCE]. Esto desactiva de antemano la sospecha de que extraer $e^{-K_*N}$ esconda un peso divergente. La acotación de $T$, que T1 sólo asevera, es cierta y cuantificable: $\sum_d\|S_d\|=4$ [SOURCE lem:jumps], $W(p)=S(p)^{-1}$ tiene los mismos monomios en $z_j$ y por tanto la misma suma [INFERENCE], de donde $\|D(\eta-i\xi_*)\|\le4e^{3t_*}\approx36.4$ y $\|T\|\le4e^{3t_*}/e^{\Phi_*}\approx9.2$, uniformemente en $N$; la moneda conmuta con $H_\xi$ y es unitaria. Finalmente verifiqué (14) por expansión directa en $N=2$: $x_2=A_1A_0x_0+A_1B_0y_0+B_1D_0y_0+B_1C_0x_0$ coincide término a término con los tres bloques de (14) [INFERENCE]. Y (16) sale de $D=d_{c,0}+\delta d$ sin residuo [INFERENCE]. No he encontrado ningún error algebraico en (1)–(16).

**El punto más débil: $P$ no está definido, sólo nombrado.** La objeción más fuerte que veo no ataca una identidad sino el cuantificador que la precede. T1 dice «se mantiene la unión fija $W$ de las ocho ventanas del precheck» [SOURCE T1 §2]. Pero el precheck escribe únicamente «sea $W$ la unión de vecindades fijas y disjuntas de los ocho saddles» [SOURCE Schur §2]: no fija radios, ni prueba que $\sup_p\|P(p)\|<\infty$, ni exhibe la condición bajo la cual el idempotente de Riesz existe en todo $W$. Busqué en los tres informes y en el TeX una especificación numérica de $W$ o una cota de $\|p_S\|$: [ABSENCE]. Lo único disponible es `lem:symbol`(d), que garantiza separación espectral y analiticidad de $P(\eta)$ sólo para $|\eta|\le r_0$, con $r_0$ explícitamente «finito pero no explícito» [SOURCE tex §7, preámbulo de la sección de asintóticas y lem:symbol(d)], transportable a los otros siete puntos por `lem:symbol`(b).

Las consecuencias son dos y son distintas. Primera, técnica: $P$ es un multiplicador acotado sólo si las ventanas son suficientemente pequeñas para que no colisionen $\lambda$ y $\lambda^{-1}$ (es decir, para que $f(\eta-i\xi_*)\ne\pm1$); sin esa condición, $P$ puede no ser acotado y (3), (8), (12), (13) carecen de sujeto. T1 declara «se entiende (3) como multiplicadores acotados» como si fuera una lectura, no un teorema [SOURCE T1 §2]; con las herramientas del acta la afirmación es *verdadera bajo hipótesis no enunciada*, no verificada. Segunda, y más grave para el encargo: aun acotado, $P$ depende de un parámetro libre $r_W$. Entonces (10a) no define diez números sino una familia de diez funciones de $r_W$, sujeta sólo a dos ligaduras ($L_+$ y $L_-$ fijos). El contrato de esta revisión pregunta si la descomposición es «exacta **y bien definida**». Es exacta; bien definida no lo es todavía. Y esto no es pedantería administrativa, porque §7 encarga a T2 decir «qué contribución hereda realmente el techo $O(N^{-6})$» [SOURCE T1 §7]: una potencia atribuida a $A_{cP}$ o a $B_{cQQ}$ es una afirmación sobre la familia entera, y puede ser no uniforme en $r_W$; con $r_W\to0$ todas las piezas con $P$ tienden a cero y $A_{cQ}$ absorbe todo $L_c$, sin que ninguna identidad de T1 se rompa. Clasificación: **REQUIRED_REPAIR**, no FATAL.

**Condición de concesión.** Retiro esta objeción si T1 añade (a) una condición de admisibilidad explícita sobre $W$ —por ejemplo $W\subseteq\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$ con el $r_0$ de `lem:symbol`(d), trasladado por `lem:symbol`(b)— junto con el enunciado «bajo esa condición $\sup_p\|P(p)\|\le C_P<\infty$», y (b) la declaración de que (10a) es una descomposición *relativa a $W$*, de modo que toda fila de la tabla de T2 deba llevar su dependencia en $W$ o un $W$ congelado numéricamente. No exijo que $r_0$ se haga explícito: basta con que la cuantificación exista y sea la misma en T1, T2 y T3.

**Segunda objeción, sobre el criterio 6.** Los cuatro controles de §5 son todos ciegos a la estructura nueva. El control plano es el más serio en apariencia y el más vacío en realidad: con $\vartheta=0$, $T=D_\xi/\Lambda$ es un multiplicador que conmuta puntualmente con $P$ dentro de $W$ y con $Q=I$ fuera, luego $B_j=PTQ=0$ y $C_j=QTP=0$ [INFERENCE]. La recurrencia (13) se desacopla, $x_N=A^NPs$, $y_N=D^NQs$, y la distinción entre $d_{c,P}$ y $d_{c,0}$ —que es la advertencia central de §4— se vuelve idénticamente trivial. El control nulo anula $f$. La «segunda derivación» por $\Delta=|f\rangle\langle v|+|v\rangle\langle f|+|f\rangle\langle f|$ reutiliza $E=BEB$, (7) y (8): es la misma expansión en otro orden, no una segunda vía en el sentido de robustez. El POVM completo es normalización. Es decir: **ningún control ejercita (13)–(15) con $B,C\ne0$**, que es justamente lo que T1 aporta sobre (2). Aporto el control que falta, en su forma mínima, hecho arriba: la expansión a mano en $N=2$ con bloques genéricos reproduce (14) [INFERENCE]. Clasificación: **REQUIRED_REPAIR** (incorporar un control con acoplamiento no nulo, aunque sea el caso $N=2$ o $N=3$ genérico); su condición de concesión es que T1 incluya tal control o declare explícitamente que los cuatro controles sólo certifican (2), (9)–(10) y no (13)–(16).

**Tercera, menor.** «Si el encoder es la identidad, entonces $f=s=0$» [SOURCE T1 §5] sólo vale para $\mathcal U^{(0)}_M=I$; con $M=I$ el encoder es $e^{i\pi F_N/2}I\ne I$ y $f\ne0$, como el propio §1 registra. La frase invita a leer «$M=I$». **OPTIONAL**: reformular como «bit cero».

**Veredicto provisional de este turno:** `T1_REPAIR_REQUIRED`, con dos reparaciones obligatorias (condición de admisibilidad y acotación de $P$ con $W$ cuantificado; control con $B,C\ne0$). No he hallado error en las identidades, y no fabricaré uno.

## Ronda 1 — GEMINI

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
{
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

## Ronda Residuo — CLAUDE OPUS

Queda en pie el álgebra: (1)–(2), (7), (9)–(12) y (13)–(16) son identidades exactas, rehechas en este turno por conjugación, por el cómputo directo del factor $e^{-K_*N}$ y por expansión a mano en $N=2$ [INFERENCE]. Queda en pie también el techo declarado: T1 no afirma orden, aditividad ni cancelación, y dice que $B_{cPQ}\ne0$ en general [SOURCE T1 §3].

Debe abandonarse la pretensión de que (10a) esté *bien definida* tal como está escrita. $W$ no tiene radios fijados en ningún documento del acta [ABSENCE: busqué en T1 §2, Schur §2, Volterra §1 y tex §7]; sin condición de admisibilidad, $P$ ni siquiera está garantizado acotado, y con ella sigue siendo una familia parametrizada. Debe abandonarse igualmente la lectura de §5 como verificación de la parte nueva: los cuatro controles anulan $B_j$ y $C_j$ o anulan $f$, de modo que (13)–(15) no se ejercita en ninguno.

La afirmación no justificada todavía es que las diez piezas de (10a) sean objetos determinados a los que T2 pueda asignar una potencia de $N$. Mientras $W$ sea libre, «$A_{cP}$ hereda $O(N^{-6})$» carece de referente: el reparto entre piezas varía con $r_W$ sin romper ninguna identidad.

No hay residuo ajeno con el que discrepar: el turno de GEMINI falló por agotamiento de crédito (HTTP 402) [SOURCE acta]. Este sanedrín es, por tanto, una sola familia de modelos, y no cuenta como revisión independiente en el sentido de la regla 5 propia del usuario.

Veredicto: `T1_REPAIR_REQUIRED`. Reparaciones obligatorias: (a) cuantificar $W$ y enunciar la acotación de $P$; (b) añadir un control con $B,C\ne0$ o declarar que los existentes no cubren (13)–(16). Menor: reformular el «control nulo» como bit cero.

## Ronda Residuo — GEMINI

**TURNO FALLIDO.** El backend no devolvió mensaje. Traza:

```
{
  "error": {
    "code": 402,
    "message": "Your prepayment credits are depleted. Please go to AI Studio at https://ai.studio/projects to manage your project and billing. Learn more at https://ai.google.dev/gemini-api/docs/billing#prepay. ",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

> GEMINI queda fuera del resto de la sesión tras 2 fallos; no se interpreta su ausencia como acuerdo.

## Ronda Veredicto — CLAUDE OPUS

**1. ACUERDO**

El acuerdo es degenerado y hay que decirlo antes de nada: GEMINI no emitió turno en ninguna de las dos ocasiones previstas, por agotamiento de crédito de facturación (HTTP 402, `RESOURCE_EXHAUSTED`) [SOURCE acta]. Por tanto «lo que todos los miembros aceptan» es, literalmente, lo que aceptó el único miembro que habló. No es consenso ni corroboración: es una posición no contestada. Según la regla 5 del usuario, un modelo de una sola familia no constituye verificación independiente; esta sesión no satisface el encargo de «revisión independiente de T1» y no debe citarse como tal.

Con esa reserva, queda registrado lo siguiente como aceptado por el sanedrín tal como se constituyó:

(i) Las identidades algebraicas de T1 no contienen error localizado. Se rehicieron en sesión (1)–(2), (7), (9)–(12) y (13)–(16) [INFERENCE de CLAUDE OPUS]: la conjugación $\mathcal FH_\xi$ de una convolución de alcance finito da símbolo $D(p-i\xi_*)$, con el mismo signo $p-i\xi$ de \eqref{eq:tilt} del TeX [SOURCE tex §2.1, §6]; el factor $e^{-K_*N}$ de (7) sale exacto de $y_*-x_*=Nv_*$ y $K_*=\xi_*\cdot v_*-\Phi_*$; y (14) coincide término a término con la expansión a mano en $N=2$.

(ii) El techo declarado por T1 se respeta. T1 no afirma orden en $N$, ni aditividad en dos términos, ni cancelación; dice explícitamente que $B_{cPQ}$ no se anula y que repartirlo por convenio no probaría separación física [SOURCE T1 §3]. No se detectó contrabando de una afirmación de escala, de $H1$/$H1c$ ni de realización física (criterio 7).

(iii) Veredicto del único turno emitido: `T1_REPAIR_REQUIRED`, con dos reparaciones obligatorias —cuantificar $W$ y enunciar la acotación de $P$; añadir un control con $B_j,C_j\ne0$ o declarar que los existentes no cubren (13)–(16)— y una menor (reformular el «control nulo» como bit cero, ya que con $M=I$ el encoder es $e^{i\pi F_N/2}I\ne I$ y $f\ne0$).

**2. DESACUERDO VIVO**

Entre miembros del sanedrín, ninguno: no hubo segundo turno. Esto es un dato negativo importante y no una formalidad. Las dos objeciones que sostienen el veredicto no fueron atacadas por nadie, ni su clasificación como `REQUIRED_REPAIR` frente a `FATAL` o `OPTIONAL` fue sometida a contraste. Su condición de concesión está formulada, pero no ha sido puesta a prueba.

Queda vivo, en cambio, un desacuerdo entre el revisor y el texto revisado, que el autor de T1 no ha respondido en esta sesión:

(a) T1 escribe «se entiende (3) como multiplicadores acotados en $\mathscr H$» [SOURCE T1 §2]. El revisor sostiene que eso es un enunciado condicional a una hipótesis no escrita, no una lectura: sin una condición de tamaño sobre las ventanas que impida $f(\eta-i\xi_*)=\pm1$, no está garantizado $\sup_p\|P(p)\|<\infty$. El único soporte disponible en el acta es `lem:symbol`(d), válido sólo para $|\eta|\le r_0$ con $r_0$ «finito pero no explícito» [SOURCE tex §7.3], trasladable a los otros siete puntos por `lem:symbol`(b).

(b) Consecuencia disputada y más relevante para el encargo: si $W$ conserva un radio libre $r_W$, (10a) no designa diez escalares sino una familia de diez funciones de $r_W$ con sólo dos ligaduras ($L_+$, $L_-$). El revisor concluye que la descomposición es exacta pero no *bien definida*, que es exactamente la conjunción que la pregunta sometida exigía. T1 no contempla esta dependencia.

**3. ABANDONADO**

Registro primero lo que perdí como parte, para no premiar mi propia posición previa.

(i) Abandonada la sospecha del criterio 3 de que el lift aplique un peso no acotado a $\phi_N$ o a $r$. Al calcularlo, $\hat u\cdot(y-y_*)\ge0$ en Bob y $\hat u\cdot(x-x_*)\le0$ en Alice, de donde $\|\mathcal V\|\le1$ y $\|s\|\le\|f\|$ [INFERENCE]; T1 tenía razón al inclinar sólo $f$ y restringir a Bob, y su observación de que no se necesita $H_\xi r\in\ell^2$ es correcta. La objeción no existe.

(ii) Abandonada la sospecha de error de convención Fourier o de signo en el desplazamiento $p-i\xi$: coincide con el TeX.

(iii) Abandonada la sospecha de que la acotación de $T$ quedara sin justificar: es cuantificable con los datos del acta, $\|T\|\le4e^{3t_*}/e^{\Phi_*}\approx9.2$ uniformemente en $N$, usando $\sum_d\|S_d\|=4$ [SOURCE lem:jumps] y que $W(p)=S(p)^{-1}$ tiene los mismos monomios en $z_j$.

(iv) Abandonada, por el propio revisor, la lectura de §5 de T1 como verificación de la aportación nueva de T1. Con $\vartheta=0$ el paso $T$ conmuta puntualmente con $P$ dentro de $W$ y $Q=I$ fuera, luego $B_j=C_j=0$ y (13) se desacopla; el control nulo anula $f$; la «segunda derivación» por $\Delta$ reutiliza (7)–(8) y es la misma expansión reordenada; el POVM completo es normalización. Ninguno de los cuatro ejercita (13)–(15) con acoplamiento no nulo.

(v) Abandonada la pretensión de que esta sesión sea la revisión independiente encargada, por el fallo de GEMINI.

No se ha refutado ninguna identidad de T1. No se fabricó objeción algebraica donde no la había, conforme al enunciado del encargo.

**4. PENDIENTE**

(i) *Cuantificación de $W$.* Se buscó una especificación de radios o una cota de $\|p_S\|$ en T1 §2, Schur §2, Volterra §1 y el TeX §7.3: [ABSENCE]. Hace falta un enunciado del tipo $W\subseteq\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$ con el $r_0$ de `lem:symbol`(d) trasladado por `lem:symbol`(b), más «bajo esa condición $\sup_p\|P(p)\|\le C_P<\infty$». No se exige hacer explícito $r_0$; se exige que la cuantificación exista y sea la misma en T1, T2 y T3.

(ii) *Congelación o trazado de la dependencia en $W$.* Si $W$ no se fija numéricamente, cada fila de la tabla de T2 debe llevar su dependencia en $W$. Falta además la prueba de la afirmación que sostiene la objeción: que el reparto entre las diez piezas varía efectivamente con $r_W$ sin romper identidad alguna, y en particular que $A_{cQ}$ absorbe $L_c$ cuando $r_W\to0$. Eso es hoy [INFERENCE] de un solo modelo, no cálculo hecho; y el intervalo admisible de $r_W$ está acotado también por arriba por (i). Sin esa prueba, la objeción (b) del apartado 2 está bien formulada pero no demostrada.

(iii) *Control con $B_j,C_j\ne0$.* La expansión a mano en $N=2$ la hizo el revisor, no T1, y sólo para $N=2$; no está versionada ni reproducida por una segunda vía. Falta un control con acoplamiento no nulo dentro de T1 (p. ej. $N=2$ o $N=3$ con bloques genéricos), o la declaración explícita de que §5 certifica (2), (9)–(10) y no (13)–(16).

(iv) *Criterio 4, resuelto sólo en parte.* La suficiencia de la restricción finita a Bob queda apoyada por $\|\mathcal V\|\le1$ y el soporte finito de $\mathcal B_N$, y (12) conserva correctamente $P^*\mathcal H_cQ$. Falta comprobar si el efecto $E=h_N\otimes M_B$ requiere alguna hipótesis adicional para que $\mathcal H_c=\mathcal V_c^*E\mathcal V_c$ quede acotado con las convenciones de (6) una vez fijado $W$; nadie lo atacó.

(v) *Revisión independiente real.* Hace falta un miembro de otra familia con crédito disponible, o una persona. Mientras no exista, el estado documental de T1 no debe pasar de `INDEPENDENT REVIEW PENDING`, y el veredicto del apartado 1(iii) debe citarse como opinión de un revisor de una sola familia.

## Ronda Veredicto — CLAUDE OPUS

**1. AGREEMENT**

The agreement is degenerate and this must be said before anything else: GEMINI issued no turn on either of the two scheduled occasions, owing to exhaustion of billing credit (HTTP 402, `RESOURCE_EXHAUSTED`) [SOURCE record]. Therefore "what all members accept" is, literally, what the only member who spoke accepted. This is neither consensus nor corroboration: it is an uncontested position. Under the user's rule 5, a model from a single family does not constitute independent verification; this session does not satisfy the commission of an "independent review of T1" and must not be cited as such.

With that reservation, the following is recorded as accepted by the sanhedrin as it was in fact constituted:

(i) The algebraic identities of T1 contain no localized error. Identities (1)–(2), (7), (9)–(12) and (13)–(16) were redone in session [INFERENCE by CLAUDE OPUS]: the conjugation $\mathcal FH_\xi$ of a finite-range convolution gives symbol $D(p-i\xi_*)$, with the same sign $p-i\xi$ as \eqref{eq:tilt} of the TeX [SOURCE tex §2.1, §6]; the factor $e^{-K_*N}$ in (7) comes out exactly from $y_*-x_*=Nv_*$ and $K_*=\xi_*\cdot v_*-\Phi_*$; and (14) matches term by term the by-hand expansion at $N=2$.

(ii) The ceiling declared by T1 is respected. T1 asserts no order in $N$, no additivity in two terms, and no cancellation; it says explicitly that $B_{cPQ}$ does not vanish and that apportioning it by convention would not prove physical separation [SOURCE T1 §3]. No smuggling in of a scaling claim, of $H1$/$H1c$, or of physical realization was detected (criterion 7).

(iii) Verdict of the only turn issued: `T1_REPAIR_REQUIRED`, with two mandatory repairs —quantify $W$ and state the boundedness of $P$; add a control with $B_j,C_j\ne0$ or declare that the existing ones do not cover (13)–(16)— and one minor one (reformulate the "null control" as a zero bit, since with $M=I$ the encoder is $e^{i\pi F_N/2}I\ne I$ and $f\ne0$).

**2. LIVE DISAGREEMENT**

Among members of the sanhedrin, none: there was no second turn. This is an important negative datum and not a formality. The two objections that sustain the verdict were attacked by no one, nor was their classification as `REQUIRED_REPAIR` rather than `FATAL` or `OPTIONAL` subjected to contrast. Their concession condition is formulated, but has not been put to the test.

What does remain live is a disagreement between the reviewer and the reviewed text, which the author of T1 has not answered in this session:

(a) T1 writes "(3) is to be understood as bounded multipliers on $\mathscr H$" [SOURCE T1 §2]. The reviewer holds that this is a statement conditional on an unwritten hypothesis, not a reading: without a size condition on the windows preventing $f(\eta-i\xi_*)=\pm1$, $\sup_p\|P(p)\|<\infty$ is not guaranteed. The only support available in the record is `lem:symbol`(d), valid only for $|\eta|\le r_0$ with $r_0$ "finite but not explicit" [SOURCE tex §7.3], transferable to the other seven points by `lem:symbol`(b).

(b) Disputed consequence, and the one most relevant to the commission: if $W$ retains a free radius $r_W$, (10a) designates not ten scalars but a family of ten functions of $r_W$ with only two constraints ($L_+$, $L_-$). The reviewer concludes that the decomposition is exact but not *well defined*, which is exactly the conjunction that the question submitted required. T1 does not consider this dependence.

**3. ABANDONED**

I record first what I lost as a party, so as not to reward my own prior position.

(i) Abandoned: the suspicion under criterion 3 that the lift applies an unbounded weight to $\phi_N$ or to $r$. On computing it, $\hat u\cdot(y-y_*)\ge0$ on Bob and $\hat u\cdot(x-x_*)\le0$ on Alice, whence $\|\mathcal V\|\le1$ and $\|s\|\le\|f\|$ [INFERENCE]; T1 was right to tilt only $f$ and restrict to Bob, and its observation that $H_\xi r\in\ell^2$ is not needed is correct. The objection does not exist.

(ii) Abandoned: the suspicion of a Fourier-convention error or a sign error in the shift $p-i\xi$: it matches the TeX.

(iii) Abandoned: the suspicion that the boundedness of $T$ was left unjustified: it is quantifiable with the data in the record, $\|T\|\le4e^{3t_*}/e^{\Phi_*}\approx9.2$ uniformly in $N$, using $\sum_d\|S_d\|=4$ [SOURCE lem:jumps] and the fact that $W(p)=S(p)^{-1}$ has the same monomials in $z_j$.

(iv) Abandoned, by the reviewer himself: the reading of T1 §5 as verification of T1's new contribution. With $\vartheta=0$ the step $T$ commutes pointwise with $P$ inside $W$ and $Q=I$ outside, hence $B_j=C_j=0$ and (13) decouples; the null control annihilates $f$; the "second derivation" via $\Delta$ reuses (7)–(8) and is the same expansion rearranged; the complete POVM is normalization. None of the four exercises (13)–(15) with nonzero coupling.

(v) Abandoned: the claim that this session is the commissioned independent review, owing to GEMINI's failure.

No identity of T1 has been refuted. No algebraic objection was manufactured where there was none, in accordance with the terms of the commission.

**4. OUTSTANDING**

(i) *Quantification of $W$.* A specification of radii or a bound on $\|p_S\|$ was sought in T1 §2, Schur §2, Volterra §1 and TeX §7.3: [ABSENCE]. What is needed is a statement of the type $W\subseteq\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$ with the $r_0$ of `lem:symbol`(d) transferred by `lem:symbol`(b), plus "under that condition $\sup_p\|P(p)\|\le C_P<\infty$". Making $r_0$ explicit is not required; what is required is that the quantification exist and be the same in T1, T2 and T3.

(ii) *Freezing or tracking of the dependence on $W$.* If $W$ is not fixed numerically, each row of the T2 table must carry its dependence on $W$. Also missing is the proof of the claim that sustains the objection: that the apportionment among the ten pieces does in fact vary with $r_W$ without breaking any identity, and in particular that $A_{cQ}$ absorbs $L_c$ as $r_W\to0$. That is today [INFERENCE] by a single model, not a computation carried out; and the admissible interval of $r_W$ is also bounded above by (i). Without that proof, objection (b) of section 2 is well formulated but not demonstrated.

(iii) *Control with $B_j,C_j\ne0$.* The by-hand expansion at $N=2$ was done by the reviewer, not by T1, and only for $N=2$; it is neither versioned nor reproduced by a second route. What is missing is a control with nonzero coupling inside T1 (e.g. $N=2$ or $N=3$ with generic blocks), or the explicit declaration that §5 certifies (2), (9)–(10) and not (13)–(16).

(iv) *Criterion 4, only partly resolved.* The sufficiency of the finite restriction to Bob is supported by $\|\mathcal V\|\le1$ and the finite support of $\mathcal B_N$, and (12) correctly preserves $P^*\mathcal H_cQ$. What is missing is checking whether the effect $E=h_N\otimes M_B$ requires any additional hypothesis for $\mathcal H_c=\mathcal V_c^*E\mathcal V_c$ to be bounded under the conventions of (6) once $W$ is fixed; no one attacked this.

(v) *Real independent review.* A member of another family with available credit is needed, or a person. Until one exists, the documentary status of T1 must not advance beyond `INDEPENDENT REVIEW PENDING`, and the verdict of section 1(iii) must be cited as the opinion of a reviewer from a single family.

## Resultado operativo

- Estado: `DEGRADED_NO_CONSENSUS`
- Turnos con fallo, cuota, ausencia o respuesta corta: 2
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-24T15:00:45Z` |
| Finished (UTC) | `2026-09-24T15:07:55Z` |
| Wall clock | 0h 7m 10s |
| Command | `sanedrin -r 1 -m opus,gemini -i es -p 1600 -t 900 -q 1 -R /home/ignac/sanedrin/reglas/base.md -c reports/2026-09-24--two-channel-t1-exact-signed-pq.md -c reports/2026-09-24--h1c-return-kernel-schur-audit.md -c reports/2026-09-24--h1c-volterra-memory-kernel-precheck.md -c papers/ir-corona/ir-corona.tex -o debates/2026-09-24--two-channel-t1-independent-review.md debates/2026-09-24--two-channel-t1-review-request.md` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-24T15:05:42Z | 1 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 297 | 1082 | ok |
| 2026-09-24T15:05:45Z | 1 | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 3 | 43 | FAILED |
| 2026-09-24T15:05:59Z | Residuo | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 14 | 271 | ok |
| 2026-09-24T15:06:02Z | Residuo | GEMINI | generativelanguage.googleapis.com/gemini-3.1-pro-preview | 3 | 43 | FAILED |
| 2026-09-24T15:07:09Z | Veredicto | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 67 | 1121 | ok |
| 2026-09-24T15:07:55Z | Veredicto | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 46 | 1147 | ok |

Turns: 6 · failed: 2 · model time: 7m 10s

Full log: `2026-09-24--two-channel-t1-independent-review.log`
