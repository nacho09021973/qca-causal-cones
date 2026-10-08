# IG-S1 — construcción exacta por conjugación de un parent conmutante

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Padre: [IG-S0](INVERSE_GRAVITY_STATE_FIRST_GATE.md).
Autorización: «adelante» después de proponer construir conjuntamente K y U.

## 1. Motivo y cierre acotado

Primer intento explícito de selección de estado por construcción: un parent
de proyectores físicos conmutantes, conjugado por un circuito físico de
profundidad fija. La solvencia de esta receta permite comprobar exactamente
energía, referencia y tick. No se presume crítica ni gravitatoria.

Se especifica un solo par. Primera batería: conservación, estado fundamental
y localidad; filtro inmediato: gap y alcance a n ticks. Si no hay excitaciones
de energía arbitrariamente pequeña o propagación sostenida, cerrar esta receta
para el objetivo tensorial z=1. No ajustar pesos, profundidad ni q para rescatarla.
El intento anterior A/B conserva su tick y contratos.

## 2. Especificación completa del par

Álgebra, constraints S/V, R_aa y T_a^a: los stencils congelados en
[IG1a](INVERSE_GRAVITY_CONSTRAINT_PREFLIGHT.md) y
[IG1b](INVERSE_GRAVITY_LOCAL_GATE_GATE.md). Se incorporan por referencia:
Z³, seis qutrits por celda, dimensión 729, ZX=omega XZ, omega³=1.
Sector físico S=V=1; toros L>=6 múltiplo de 6; coeficientes uniformes y
simetría cíclica C3. Sin materia ni ancillas nuevas. No se afirma SO(3).

Para cada R_aa(i), definir el proyector
`Pi_R=(I+R+R²)/3` y `h_R=I-Pi_R`.

`K_0 = sum_(i,a) h_Raa(i)`.

Todos los h son proyectores físicos conmutantes; sus pesos son 1.
La normalización de energía fija una duración de tick adimensional 1.
No se adjudica una escala física absoluta.

Definir D como el bloque completo de puertas T de IG1b:
`D=prod_(i,a) exp[-i(pi/3) A_Ta(i)]`, `A_T=(T+T†)/2`.
Las puertas conmutan dentro de D. El ángulo es fijo antes de las pruebas.

La regla nueva se define **por circuito**:

`F=prod_(i,a) [Pi_R + exp(-i)(I-Pi_R)]`,
`U_E=D F D†`, `U_E^-1=D F† D†`,
`K_E=D K_0 D† = sum_(i,a) D h_Raa(i) D†`.

La identidad F=exp(-iK_0) se debe a la conmutación, y sirve para la prueba;
una exponencial global genérica no sustituye la regla por circuito.
Por ello también U_E=exp(-iK_E) como identidad, que se verificará.

Capas: 24 para D†, 81 para F y 24 para D, en los órdenes/colores de IG1b;
total 129, independiente del volumen. El periodo de coloración es 6,
pero los bloques completos tienen traslación de una celda.

## 3. Referencia y acceso

`G_0 = prod_(i,a) Pi_Raa(i) prod_(i,a) Pi_Va(i)`,
con `Pi_V=(I+V+V²)/3`. R/V conmutan y Rxx Ryy Rzz=S.
Demostrar G_0 no nulo y que es todo el proyector fundamental de K_0 en
el sector físico. No escoger un vector de su degeneración.

`G_E=D G_0 D†`, `rho_E,L=G_E/Tr G_E`.

Acceso en cada volumen por álgebra estabilizadora sobre F3: para una palabra
Pauli, su esperanza en G_0/Tr G_0 se obtiene por pertenencia al grupo de
R/V, con sus fases. La conjugación local por D requiere solo puertas que
tocan el soporte inicial. No se sustituye por un Gibbs de región aislada.
La existencia de un límite local uniforme debe auditarse si el candidato
supera los filtros; el algoritmo finito no lo demuestra por sí mismo.

## 4. Pruebas congeladas

Certificado permanente: `scripts/verify_inverse_gravity_dressed_parent.py`.

1. Revalidar R/V y T/S por stencils reales, todas las traslaciones; comprobar
   redundancia Rxx Ryy Rzz=S también mediante Laurent.
2. En el bloque auxiliar qutrit R=X, T=Z^-1, verificar projector, dressing,
   conservación y referencia. La puerta F se verifica con un símbolo p
   unimodular y después se identifica p=exp(-i); no fitting numérico.
   Este bloque no simula el espectro de la red.
3. Escribir la prueba de localidad del parent conjugado y el tick, incluyendo
   U_E^n para todos los enteros n, sin extrapolar desde muestras temporales.
4. Derivar el espectro de K_0 como número entero de R violados. En el sector
   S=1, la redundancia excluye una única violación en un vértice.
   Comprobar M>=2 por los 27 caracteres locales, no asumir independencia
   entre vértices ni contar modos desde ese número.
5. Testigo superior fijado: T_x del cubo origen actuando sobre una referencia
   física R=1. Comparar stencils y geometría de cubo de IG1c; exigir 16 R
   violados. Proporciona una excitación física de energía 16, no el gap exacto.

La derivación espacial decide la receta. Un PASS de matrices auxiliares no
autoriza espectro IR, respuesta de materia o gravedad. Mantener separados
construcción exacta, límite del estado, gap, propagación y objetivo Einstein.
Si el gap es uniforme positivo y la influencia permanece en soporte fijo,
salida `DRESSED_COMMUTING_PARENT_REJECTED_FOR_GAPLESS_PROPAGATING_TARGET`.
No declarar un no-go de todos los QCA con energía conservada.
