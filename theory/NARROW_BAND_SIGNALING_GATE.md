# NARROW_BAND_SIGNALING_GATE

**Fecha:** 2026-09-17. **Estado:** contrato fijado antes de cálculo;
`NOT_EXECUTED / OUTCOME_OPEN`. Alcance local de
`research/b-infinity-post-s4-gate`, sobre `HEAD=11efe1f` y el remoto
científico `780ecb0`. Su publicación/versionado y su ejecución quedan
pendientes de instrucciones posteriores. Este archivo no registra un resultado.

## 1. Pregunta única y cuantificadores

¿La familia y el protocolo únicos fijados en §§3–5 satisfacen, en algún
intervalo completo `0 < Lambda <= Lambda_*`, simultáneamente el control IR
de §6, el control de atribución UV de §8 y

\[
D_B(\Lambda)=\tfrac12\|\rho_B^{(1)}(\Lambda)-\rho_B^{(0)}(\Lambda)\|_1>0,
\]

con Bob fuera del cono emergente del evento de codificación y dentro de su
soporte causal microscópico exacto?

`Lambda_* > 0` será un dominio demostrado por las cotas, no un punto elegido
por inspección numérica. No se exige un límite positivo de `D_B`. La pregunta
general sobre todos los protocolos IR motiva este gate, pero un negativo aquí
se restringe a esta familia, intervención, sitio, tiempo y criterio de control.

## 2. Convenciones y nodo

Se conserva el CAR libre de CJWW (5.15), un sector global de una partícula,
dos modos internos por sitio, `S=W^dagger` para estados y
`K_t(x,z)=(W^t)_{x,z}` para el kernel previamente fijado. En coordenadas
adimensionales `p` del símbolo existente,

\[
W(p)=\begin{pmatrix}
\cos p_1\cos p_2e^{ip_3}&-\cos p_1\sin p_2+i\sin p_1\\
\cos p_1\sin p_2+i\sin p_1&\cos p_1\cos p_2e^{-ip_3}
\end{pmatrix}.
\]

Usamos la representación generatriz de los coeficientes de Laurent,
`hat psi(p)=sum_x exp(i p.x) psi(x)`, con inversa de signo negativo y medida
`dmu(p)=d^3p/(2pi)^3` en `B=[-pi,pi)^3`. Así el kernel con desplazamiento
`x-z` actúa con símbolo `W(p)` y la evolución de estados con `S(p)=W(p)^dagger`.
Esta declaración fija también el signo al comparar Fourier y posición.

Nodo único: `p=0`, donde `W(0)=I`. Es el nodo del límite ya utilizado en el
proyecto. La expansión lineal registrada para este símbolo fija

\[
H_{\mathrm W}(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,
\qquad S_{\mathrm W}(p)=e^{-iH_{\mathrm W}(p)},\qquad c_{\rm IR}=1.
\]

Es un gate Weyl sin masa; no se incorpora un nuevo acoplamiento Dirac.
Se conservan ambos componentes y ambas ramas cercanas a cero: no se presume
una partícula de energía positiva ni se introduce un proyector de helicidad.
Otros nodos quedan fuera; su enumeración en otros walks no se transfiere a
CJWW (5.15). No se cambiará de nodo al conocer el resultado.

## 3. Proyector y familia única de recursos

Se fija

\[
\Pi_\Lambda=\mathcal F^{-1}
 [\mathbf1_{\{|p|_2\le\Lambda\}}I_2]\mathcal F,
\qquad 0<\Lambda<\pi/4,
\]

con ambas ramas internas. El límite es `Lambda -> 0`. `pi/4` sólo delimita
una carta alrededor del origen, que deberá verificarse libre de otros nodos
y del corte del logaritmo; no constituye un umbral de validez IR. Esa validez
se decide con las cotas de §6 en un intervalo suficientemente pequeño.

La única envolvente admitida es

\[
g(q)=(1-|q|_2^2)^2\mathbf1_{\{|q|_2<1\}},\quad
Z_\Lambda=\int_B|g(p/\Lambda)|^2d\mu(p),\quad
\widehat\phi_\Lambda(p)=Z_\Lambda^{-1/2}g(p/\Lambda)\binom01.
\]

El recurso al elegir el bit será `psi_Lambda=S^2 phi_Lambda`. Los dos pasos
previos son comunes. Quedan congelados centro espacial en el origen, centro
espectral cero, perfil radial, exponente 2, espín `down`, fase escalar real,
normalización y dos pasos comunes. Sólo varía `Lambda`. No se ajustan fases,
espín, centro, envolvente ni duración para conseguir una señal.

El perfil tiene soporte espectral compacto y borde suavizado; permite
integrales finitas y estimaciones analíticas sin una cola gaussiana UV ni un
corte espacial numérico como parte de la definición. Es una elección
metodológica mínima, no una familia postulada por los artículos. Un positivo
respondería a existencia; un negativo no agotaría otras preparaciones IR.

Se asume disponible este recurso extendido antes de la elección. El filtro
es una definición del recurso, no un procedimiento de preparación local
certificado. No se afirma soporte espacial finito, vacancia de Bob ni
preparación exclusivamente desde Alice. La compatibilidad entre soporte
espectral compacto y localización espacial exacta no se presume.

## 4. Protocolo operacional congelado

- En `T=-2`: recurso `phi_Lambda`, independiente del bit.
- En `T=-2 -> 0^-`: sólo `S^2`, común a ambas historias.
- En `A=(T=0,x=0)`: bit exógeno independiente del recurso; Alice aplica
  `U_0=I` o `U_1=exp(i pi n_0)`. En el sector de una partícula,
  `U_1=I-2P_0`, `P_0=|0><0| tensor I_2`.
- Después: `psi_Lambda^(b)(n)=S^n U_b psi_Lambda`, `n=0,1`.
- Bob: dos modos del único sitio `y_B=(1,1,0)`, a `Delta T=1`.

La extensión CAR de la puerta es par, local en el origen y conservadora del
número. No se admiten ancillas, postselección, mensajes auxiliares ni filtros
dependientes del bit. Se exige demostrar igualdad exacta de las historias
pre-elección y de todas las estadísticas pre-elección de Bob. También se
verificará igualdad de los estados reducidos físicos de Bob en `0^+`, por
localidad de la puerta, aunque el recurso ya tenga amplitud en Bob.

El claim posible es señalización con un recurso IR preestablecido. No es
transporte de una partícula que sale de Alice al elegir el bit, ni preparación
estrictamente local del recurso. La localización del evento de elección y
la del recurso son requisitos distintos.

## 5. Causalidad y lectura de Bob

La admisibilidad conserva el criterio de los witnesses previos:

\[
|y_B|_2>c_{\rm IR}\Delta T,\qquad K_1(0,y_B)\ne0.
\]

Se re-certificará esa geometría bajo las convenciones de §2, sin recalcular
los valores de señal de los witnesses anteriores. La envolvente microscópica
es `C_micro=[-1,1]^3`; pertenecer a su envolvente convexa no sustituye al
test del kernel exacto. La referencia temporal es la elección en `T=0`.
La extensión previa del paquete no redefine ninguno de esos conos.

La cantidad principal es `D_B` entre los estados físicos completos reducidos
a Bob. En la base local `(vac,up,down,up-down)`, para una amplitud `v_b` en
Bob, se usa la convención ya fijada

\[
\rho_B^{(b)}=(1-\|v_b\|^2)|vac\rangle\langle vac|+v_bv_b^\dagger,
\]

con bloque de dos partículas nulo. Deben verificarse normalización,
positividad y tratamiento correcto de todos los bloques. Un efecto local
par `0<=E_B<=I` con diferencia estrictamente positiva puede certificar un
límite inferior; ocupación nula por sí sola no certifica `D_B=0`.

## 6. Control IR de los estados y de la evolución

Se registrarán por separado

\[
\epsilon_{\rm pre}(j,\Lambda)=\|(I-\Pi_\Lambda)S^j\phi_\Lambda\|^2,
\quad j=0,1,2,
\]

\[
\epsilon_b(n,\Lambda)=
\|(I-\Pi_\Lambda)S^nU_b\psi_\Lambda\|^2,
\quad b=0,1,\quad n=0,1.
\]

`epsilon_UV` es el máximo de esos valores. Se exige una cota explícita
uniforme en las etapas que tienda a cero con `Lambda`. El valor después de
Alice no se hereda del anterior. La eventual conservación de soporte
espectral bajo pasos libres debe justificarse mediante el conmutador con
`Pi_Lambda`, nunca suponerse para `U_1`.

El control dinámico usará

\[
r_{\mathrm W}(\Lambda)=
\max_{0\le j\le3}\operatorname*{ess\,sup}_{|p|\le\Lambda}
\|S(p)^j-e^{-ijH_{\mathrm W}(p)}\|_{\rm op}.
\]

Se deberá demostrar para nuestro símbolo una cota explícita
`r_W(Lambda)<=R_W(Lambda)` con `R_W -> 0`, dominio y constantes efectivos.
La literatura motiva Taylor; no aporta esas constantes para CJWW (5.15).
No basta escribir `O(Lambda^2)` sin acotar el resto. Definimos el presupuesto
adimensional `epsilon_IR=R_W+sqrt(epsilon_UV)`; se exige que tienda a cero.
Los factores necesarios para trasladarlo a estados y observables deberán
justificarse por normas de operadores, distancias entre estados y
contractividad de la reducción local.

La elección de un logaritmo para energía es la rama matricial continua en
el origen, con `H(0)=0`; no se asigna una energía IR ordinaria a modos UV.
Para la comparación basta el propagador `exp(-ij H_W)` dentro de la banda.
Su uso no define un nuevo walk físico ni certifica localidad exacta de un
operador proyectado sobre la red.

## 7. Control de la diferencia codificada: primera prueba y stop rule

La norma UV absoluta puede tender a cero porque toda la intervención se
vuelve pequeña. Para impedir que eso esconda una codificación UV, se fija un
segundo requisito, independiente de un observable particular.

Inmediatamente después de Alice, sean

\[
\varrho_b=|U_b\psi_\Lambda\rangle\langle U_b\psi_\Lambda|,\quad
\Delta=\varrho_1-\varrho_0,\quad
L=\Pi_\Lambda\Delta\Pi_\Lambda,\quad R=\Delta-L.
\]

Para `||Delta||_1>0`, exigimos

\[
\eta_{\rm enc}(\Lambda)=\frac{\|R\|_1}{\|\Delta\|_1}\longrightarrow0.
\]

Es un criterio metodológico conservador, invariante ante fases globales,
para exigir que la diferencia codificada esté asintóticamente en la banda.
No es un teorema bibliográfico ni una condición necesaria para toda posible
noción física de señal IR.

**Convención para `Delta=0`.** El criterio relativo se evalúa sólo cuando
`||Delta||_1>0`. Si `Delta=0` exactamente para algún `Lambda` o para todo un
régimen considerado, no se asigna valor de `eta_enc` en ese régimen: ese caso
se clasifica por separado como ausencia de diferencia codificada, no cuenta
como cumplimiento del control de esta sección y no puede por sí solo
satisfacer ningún criterio positivo de señalización. La misma convención rige
para la diferencia propagada definida abajo. Si además se demuestra `Delta=0`
en todo un entorno perforado del origen, ésa es la obstrucción por ausencia
de dependencia del bit de §10, no un positivo obtenido de un cociente
indefinido.

Se certificará también este control para la diferencia propagada
`Delta(n)=S^n Delta S^{n dagger}`, `n=1`: podrá reutilizarse el valor de
`n=0` sólo después de justificar la conmutación del proyector con la
evolución y la invariancia de las normas implicadas.

**Primera prueba de ejecución:** examinar analíticamente §§6–7 antes de
evaluar cualquier señal en Bob. La puerta puntual queda sujeta a esta prueba;
su compatibilidad con el control IR no se presupone.

Una demostración de incompatibilidad en todo entorno perforado del origen
cierra negativamente la clase por control IR, sin calcular `D_B`. Una cota
demasiado débil o un intento de prueba fallido deja el resultado abierto.
No se sustituirá la puerta por `Pi_Lambda U_1 Pi_Lambda`, una operación
postseleccionada, una fase espacialmente extendida o una puerta dependiente
de `Lambda` para salvar el gate. Tales cambios requieren otro contrato y,
si amplían la región de Alice, otro test causal desde toda esa región.

## 8. Atribución operacional y presupuesto UV en Bob

Superar §7 tampoco basta para resolver un observable local muy pequeño.
Se exige un control adicional de la contribución UV a ese observable.

Sea `T_B` la aplicación lineal de reducción del sector global de una
partícula al Fock local de Bob. Se aplica por linealidad también a operadores
hermíticos no positivos. Para `n=0,1`, definimos únicamente como diagnósticos

\[
L_B(n)=T_B(S^n L S^{n\dagger}),\quad
R_B(n)=T_B(S^n R S^{n\dagger}),\quad
d_L(n)=\tfrac12\|L_B(n)\|_1.
\]

`L` no es una diferencia de estados normalizados de un nuevo protocolo.
La proyección no se ejecuta ni se renormalizan ramas. Se debe certificar la
identidad `rho_B^(1)(n)-rho_B^(0)(n)=L_B(n)+R_B(n)` y la cota triangular

\[
|D_B(n)-d_L(n)|\le\tfrac12\|R_B(n)\|_1.
\]

La certificación positiva requerirá funciones justificadas

\[
0<\ell_B(\Lambda)\le d_L(1),\quad
\tfrac12\|R_B(1)\|_1\le u_B(\Lambda),\quad
d_L(0)\le q_B(\Lambda),
\]

que satisfagan en un intervalo completo `0<Lambda<=Lambda_*`

\[
u_B+q_B\le\tfrac12\ell_B,
\qquad (u_B+q_B)/\ell_B\longrightarrow0.
\]

El margen `1/2` es una regla de certificación fijada de antemano; no una
escala de momento ni un ajuste a los datos. Las funciones no son leyes de
escala asumidas: habrá que obtenerlas de la prueba.

`q_B` controla la no-localidad artificial introducida al proyectar: aunque
la diferencia física en `0^+` sea cero, `L_B(0)` puede no serlo y cancelarse
con `R_B(0)`. No se atribuirá esa diferencia instantánea a Alice ni a
propagación IR. Las cotas anteriores exigen que tanto esa contaminación
como la contribución UV al resultado queden por debajo de la señal IR
certificada. Incluyen términos cruzados IR–UV, no sólo población UV.

Estas desigualdades, si se demuestran, darán un límite inferior positivo de
la distancia física; aquí no se evalúa ninguna de sus cantidades.

Además se deberá publicar una cota del error al reemplazar la propagación
de `L` por la propagación Weyl lineal, obtenida de §6, y compararla con la
señal. Si ese error no permite resolver su signo, el resultado sólo podrá
llamarse señal del walk de baja energía con correcciones lattice
controladas. No podrá presentarse como señal predicha por la ecuación Weyl
lineal. No se exige que el término lineal produzca el efecto: ésa sería una
pregunta más fuerte. La distancia física se calcula siempre con el walk
exacto, con error certificado si se aproxima el cálculo.

Bob conserva una lectura local microscópica; su aparato tampoco queda
identificado con un detector relativista de baja energía. Las cotas de este
apartado controlan su estadística, no un modelo de detector experimental.

## 9. Criterio positivo conjunto

Se requieren todas las condiciones siguientes, en un intervalo perforado
completo y con un único `Lambda_*` compatible con todas las cotas:

1. Recurso normalizado, familia y nodo fijados; control de §§6–7 demostrado.
2. Historias pre-elección idénticas, bit independiente e igualdad física
   inmediata en Bob; intervención local par atribuible a Alice.
3. Admisibilidad causal de §5 re-certificada.
4. `D_B>0` certificado, o efecto local par con diferencia positiva rigurosa;
   estados completos usados aunque la ocupación no detecte la diferencia.
5. Presupuesto de §8 demostrado: la señal no se sostiene en fuga UV no
   resuelta, coherencias IR–UV omitidas o artefactos de proyección.
6. Error dinámico respecto a Weyl y errores de evaluación publicados con
   el alcance interpretativo especificado en §8.

Una señal positiva del walk con sólo `epsilon_UV -> 0` no satisface este
criterio. Tampoco lo hace un valor aislado en una malla de momentos.

## 10. Criterio negativo y estados posibles

Un negativo requiere una identidad, desigualdad o argumento analítico que
excluya la conjunción anterior para toda la familia asintótica congelada.
Se indicará su razón: ausencia de dependencia del bit, incompatibilidad del
encoder con el criterio IR, inadmisibilidad causal, u otra obstrucción
demostrada. Una prueba de incompatibilidad no afirma `D_B=0` para el walk.

Una cota superior que tienda a cero sólo establece desaparición en el
límite, no nulidad a ancho finito. Una relación hipotética
`D_B<=C epsilon_UV` tendría que demostrarse; no se adopta como premisa.
No hallar un ejemplo o no lograr una cota suficientemente fina no constituye
un resultado negativo.

Los estados terminales se asignan en el siguiente orden, sin solapamientos:

| Estado | Condición |
| --- | --- |
| `IR_SIGNALING_NONZERO_BUT_VANISHES_AS_LAMBDA_TO_ZERO` | Se cumplen todos los criterios positivos y además se demuestra `D_B(Lambda)->0`. |
| `IR_CONTROLLED_SIGNALING_CONSTRUCTED` | Se cumplen todos los criterios positivos, pero no está demostrada la desaparición del renglón anterior. Se registra por separado si el límite es desconocido, no existe o es positivo demostrado. |
| `NO_IR_CONTROLLED_SIGNALING_WITHIN_FROZEN_CLASS` | Existe una obstrucción probada a los criterios positivos para esta familia asintótica. No es una imposibilidad general ni una retractación de witnesses anteriores. |
| `OPEN_AFTER_CONTROLLED_ANALYSIS` | No hay construcción ni obstrucción suficiente, incluidas cotas insuficientes o inconsistencias de convenciones no resueltas. |

Se usa `AS_LAMBDA_TO_ZERO` en vez de `IN_CONTINUUM_LIMIT`: aquí permanecen
fijos sitio y número de pasos. Reducir la banda no define por sí mismo un
límite de continuo con separaciones y tiempos físicos fijos. Tampoco se
presume convergencia en norma de los estados globales al reducir `Lambda`.

## 11. NON-TRANSFER OF THE FROZEN 3/128 WITNESS

`3/128` pertenece al protocolo ultralocal exacto previamente cerrado y
revisado. Este gate no lo recalcula, no intenta conservarlo, no lo usa como
baseline cuantitativo IR y no considera una señal menor una degradación.
No autoriza extrapolarlo a observables relativistas. Cualquier positivo que
satisfaga este contrato sería un resultado nuevo.

`ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED`
y `NONCORNER_SIGNALING_CONSTRUCTED / INDEPENDENTLY_REVIEWED` conservan sus
alcances con cualquiera de los cuatro resultados posibles.

## 12. Escala absoluta y techo de reclamo

Se conserva `DIMENSIONAL_MAP_CONDITIONAL`: `x=a n`, `t=N tau`,
`k_phys=p/a`, `E=hbar omega/tau` módulo `2pi hbar/tau`,
`c_IR^phys=a/tau`. Imponer el `c` observado sólo fija `a=c tau`.
No se eligen escalas de Planck, eV, metros, segundos ni una realización.

Incluso un positivo sólo establecería señalización en este walk discreto,
con recurso extendido preestablecido y control IR según este contrato. No
establecería señalización relativista en la naturaleza, violación de
causalidad relativista, violación de la microcausalidad del modelo,
conversión de `3/128` en predicción experimental, señal no nula en el
continuo, preparación exclusivamente desde Alice, optimalidad o viabilidad.

El control de baja energía no identifica nuestro walk con el QCA de los
artículos ni transfiere sus simetrías, escalas o correcciones. El marco de
referencia y la lectura espacial siguen siendo los de la red congelada.

## 13. Plan posterior a la publicación del preregistro

Este plan no se ejecuta al redactar el contrato.

1. Verificar representación Fourier, rama en el origen y carta; obtener
   cotas analíticas de normalización, fuga en cada etapa y resto de Weyl.
2. Examinar `eta_enc` analíticamente. Si se prueba incompatibilidad
   asintótica, aplicar la stop rule sin evaluar señal ni buscar otra puerta.
   Si el control queda irresuelto, cerrar la pasada como abierta.
3. Sólo si se certifican los controles previos, re-certificar la geometría
   fijada y construir las dos reducciones de Bob mediante integrales del
   único paquete. Evaluar `D_B` y el presupuesto de §8, sin scans.
4. Si hay positividad certificada, examinar su límite con las mismas
   expresiones. No ajustar una ley a datos ni ampliar sitios o tiempos.
   Registrar la comparación con el error Weyl y clasificar con §10.

Se priorizan identidades, integrales analíticas y restos acotados.
Los helpers existentes del símbolo y de la reducción local pueden servir
posteriormente; los helpers para estados de soporte espacial finito no
pueden usarse truncando sin control este paquete extendido. No se crea un
script nuevo salvo necesidad demostrada y autorización de implementación.
Los verifiers previamente revisados conservan sus bytes en esta fase.

Si se necesita evaluación numérica posterior, deberán separarse y acotarse
error de cuadratura/discretización, truncación espacial si la hubiera,
redondeo, resto de Weyl y fuga UV. Esta última es una propiedad física del
protocolo, no un error de cuadratura. Una cota inferior positiva debe seguir
siéndolo tras todo el presupuesto. No se aceptan tolerancias redefinidas por
el resultado, exploraciones de gaussianas ni barridos de `Lambda`.

## 14. Fuentes primarias y atribuciones

Las páginas siguientes son las del PDF local identificado. Los PDFs de
`biblioteca/` permanecen locales e ignorados; no se incorporan a Git.

**DP14:** D'Ariano–Perinotti, *Derivation of the Dirac Equation from
Principles of Information Processing*, arXiv:1306.1934v2, 28-12-2014.
Archivo: `biblioteca/Derivation of the Dirac Equation from Principles of
Information Processing.pdf` (nombre en una sola línea en el filesystem).
SHA256: `940dde862ab1ba74a4ce1b3f85f8056f7e0f00abd93b403fdbf6543849a9c72f`.

**BDP17:** Bisio–D'Ariano–Perinotti, *Quantum Walks, Weyl equation and the
Lorentz group*, arXiv:1707.08455v1, 26-07-2017.
Archivo: `biblioteca/Quantum Walks, Weyl equation and the Lorentz group.pdf`.
SHA256: `fa93f4e4aee220cf17ccdf3471a142fda43f6646a18fcea9c9d5361ef40439c3`.

**BB93:** Bialynicki-Birula, *Dirac and Weyl Equations on a Lattice as
Quantum Cellular Automata*, arXiv:hep-th/9304070v1, 19-04-1993.
Archivo: `biblioteca/Dirac and Weyl Equations on a Lattice as Quantum
Cellular Automata.pdf` (nombre en una sola línea en el filesystem).
SHA256: `656a1345b77c6b1288fb54492f40213e59ead8f58e67b42203e722cc3bb04842`.
Es el preprint Weyl/Dirac, no la versión publicada ampliada con Maxwell de
1994. No se atribuyen aquí al preprint secciones de esa versión posterior.

| Procedencia | Evidencia | Uso y límite |
| --- | --- | --- |
| `EXPLICIT`, DP14 | §VII, p. 8, Ecs. (57)–(63) | Hamiltoniano interpolante y expansión Weyl/Dirac para pequeño vector de onda; narrow-band y pequeña masa en Dirac. Motivan §6, sin aportar cotas para nuestro símbolo. |
| `EXPLICIT`, DP14 | pp. 8–9, Fig. 3, Ec. (65) | Distinguen estado localizado y paquete de partícula; expansión dispersiva alrededor de un momento central para banda estrecha. No certifican nuestro encoder. |
| `EXPLICIT`, DP14 | pp. 8–9, Ec. (64) | La identificación Planckiana es una hipótesis dimensional. No determina una escala para este gate. |
| `EXPLICIT`, BDP17 | p. 1; §II, p. 3, Ecs. (6)–(7) | Emergencia para estados deslocalizados y vecindades de nodos; fermion doubling en su walk. Motiva fijar un nodo, sin importar su clasificación. |
| `EXPLICIT`, BDP17 | §III, pp. 4–5, Ecs. (14)–(18); p. 7, Ec. (31) y texto | Eigenfase discreta, dispersión no lineal y recuperación de Lorentz a pequeño momento. No da un protocolo experimental local. |
| `EXPLICIT`, BB93 | pp. 2–3, Ecs. (1)–(3), (13)–(18) | Coordenadas `a n`, paso `Delta t` y expansión de primer orden con `c=a/Delta t`. |
| `EXPLICIT`, BB93 | pp. 4–5, Ecs. (25)–(34) | Integración sobre Brillouin, eigenfases y límite a momento físico fijo. No avala aplicar esa aproximación a una delta de red a ancho finito. |
| `DERIVED / obligación de prueba` | §§6–8 de este contrato | Cotas de evolución y su traducción a estados/observables, fuga inducida por Alice y su contribución a Bob. No son resultados ya obtenidos. |
| `METHODOLOGICAL CHOICE` | §§1–10 | Perfil `g`, nodo único, espín, dos pasos comunes, puerta puntual, sitio, tiempo, criterios relativos, márgenes, stop rule y taxonomía. Ninguno se atribuye a los artículos. |

Convenciones del modelo y antecedentes cerrados leídos antes de redactar:
[`ALICE_LOCAL_PREPARATION_WITNESS.md`](ALICE_LOCAL_PREPARATION_WITNESS.md),
[`NONCORNER_SIGNALING_GATE.md`](NONCORNER_SIGNALING_GATE.md),
[`PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md`](PHYSICAL_DIMENSIONAL_TRANSLATION_GATE.md)
y la [auditoría dimensional](../reports/2026-09-17--physical-dimensional-translation-audit.md).
La inspección de `walk2()` sólo fija el símbolo; no se ejecutó código científico.

Las etiquetas bibliográficas provisionales
`CURRENT_WITNESS_OUTSIDE_CONTROLLED_IR_REGIME` y
`PHYSICAL_PREDICTION_MAP_REQUIRES_NEW_PHYSICAL_INPUT` motivan la pregunta.
Este contrato no las promueve a estado canónico.

## 15. Decisiones y ambigüedades resueltas antes de ejecución

Se adopta la clase mínima con Alice puntual y prueba de compatibilidad
previa. No se declara ya inconsistente ni ya IR-compatible. Si falla,
relajar su extensión espacial sería una decisión física sustancial y un
sucesor distinto; no un ajuste permitido durante este gate.

La preparación extendida, la mezcla de ramas de energía, la lectura
microscópica de Bob y el carácter conservador de `eta_enc` son límites
explícitos. Un negativo debido a ese criterio significa imposibilidad bajo
esa definición preregistrada, no bajo todas las definiciones de control IR.

No queda un parámetro de protocolo por elegir después de observar datos.
Las constantes y el dominio de las cotas serán objetos de prueba; su
ausencia actual no autoriza asignar valores ni presupone el resultado.
No se ha calculado ninguna nueva señal, fuga ni ley de escala al fijar
este contrato. Su estado científico permanece `OUTCOME_OPEN`.
