# IG1e — dos opciones ordenadas para seleccionar una referencia IR

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Base `edf584e9864d035b163ba4916dcc545dc075e930`.
Autorización: «selecciona al menos dos opciones de modo que si la primera
falla, usamos la opcion B». Se fijan A y B antes de probar el tick candidato.

## 1. Invariantes y objetivo

Mismo tick U=U_T U_R, q=3, θ=π/3, orden, soportes y constraints de IG1b.
No cambiar puertas ni ángulos si una selección de estado falla.
No sustituir Einstein por física térmica o Lifshitz.

Objetivo de esta etapa: una selección físicamente motivada y estacionaria,
con respuesta interna no nula y controles que permitan plantear el IR.
Ni A ni B se consideran estados gravitatorios por definición. Su viabilidad
en la red está OPEN. El charter mantiene R1/R3–R8 sin promoción.

## 2. Opción A — selección por Hamiltoniano local auxiliar conservado

Fijar en cada toro admitido

`H_A=-sum_(i,a) [(R_aa(i)+R_aa(i)†)/2 + (T_a^a(i)+T_a^a(i)†)/2]`.

Son los términos del tick, con pesos iguales fijados ahora; no reconstruir
pesos tras comprobar si se conserva. H_A es un operador local que preserva
P. No se identifica a priori con i log(U), energía Floquet o gravedad.

Familia de estados definida, con β adimensional:

`σ_A,L(β)=P exp(-β H_A) P / Tr_P exp(-β H_A)`, β>0.

Control inicial β=1. La receta de vacío, si pasa la conservación, será
`ρ_A,L^0=lim_(β→∞) σ_A,L(β)=P_0,L/Tr(P_0,L)`, donde P_0,L es el proyector
al mínimo de H_A restringido a P. Mantener degeneración; no escoger un
eigenvector arbitrario favorable. El límite β→∞ se toma a L fijo y luego
L→∞ por L múltiplos de 6; no confundirlo con un límite continuo de red.

**Primer filtro A0:** demostrar `[U,H_A]|H_P=0` exactamente para la regla.
Es equivalente a estacionariedad de σ_A,L(β) a β=1 en cada volumen finito:
la exponencial es inyectiva sobre eigenvalores reales y el logaritmo
positivo recupera H_A hasta la constante de normalización.

Si no conmuta, falla esta opción de selección térmica conservada y se activa
B. No concluye que el proyector de mínimo aislado no pueda ser estacionario;
esa ruta más débil no se usa como rescate de A bajo este contrato.
Un test sin P no basta para demostrar fallo en el sector físico.

**A1:** si A0 pasa, justificar existencia y control local del límite de estado;
no transferir gap, excitaciones o Lorentz de H_A a U sin prueba.
**A2:** comprobar respuesta no nula en la batería fijada abajo, con el estado
seleccionado; después definir su régimen de excitaciones y rama de quasifases.

Motivo físico: si existe una energía local exactamente conservada, ofrece
un criterio de selección independiente de ordenar quasifases módulo 2π.
Es hipótesis, no un hecho del tick. La frustración de H_A no impide que tenga
un mínimo; impide únicamente el mínimo término a término descartado en IG1d.

## 3. Opción B — ensemble estacionario por promedio del tick real

Se activa tras fallo de A0, A1 o A2, o tras un cierre explícito
`A_UNRESOLVED_AFTER_BOUNDED_ATTEMPT`. Tiempo transcurrido solo no es FAIL.
La semilla está fijada sin ajuste:
`σ_B,L=σ_A,L(1)`, usando el mismo H_A como criterio local de preparación,
aunque H_A no resulte conservado. No tratar la semilla como estacionaria.

Definir

`ρ_B,L=lim_(M→∞) (1/M) sum_(n=0)^(M-1) U^n σ_B,L U^-n`.

En volumen finito existe y equivale a
`sum_φ Π_φ σ_B,L Π_φ`, donde Π_φ agrupa cada eigenfase distinta de U|H_P.
Conservar coherencias dentro de bloques degenerados; no elegir eigenbasis
arbitraria ni asignar temperatura a quasifases ordenadas.

El estado es físico, positivo, normalizado y exactamente estacionario.
Esto no asegura que sea distinto de P/Tr(P), localmente no tracial o vacío.
La preparación usa una semilla de criterio local y la regla original;
el promedio es selección de ensemble, no una proyección aplicada cada tick.

**B0:** justificar el promedio y su acceso computacional sin diagonalizar la
Hilbert space completa; una fórmula formal no es algoritmo escalable.
**B1:** excluir convergencia a referencia localmente tracial en los observables
del test; no basta que ρ_B,L sea globalmente distinta en un toro pequeño.
**B2:** respuesta no nula y persistencia local controlada al aumentar volumen.
**B3:** definir si existe un sector de excitaciones con selección física de
rama; el ensemble estacionario por sí solo no es un vacío energético.

Orden de límites: promedio M→∞ a L fijo, luego L→∞ por múltiplos de 6.
Antes de usar promedios truncados se fijarán error, ventana y algoritmo
en un contrato de ejecución separado; no asumir que ambos límites conmutan.

Motivo físico: cuando falla una energía conservada, la selección usa la
dinámica que realmente existe, en lugar de suponer un generador auxiliar.
Riesgo: pérdida local de memoria/respuesta. No se afirma que este QCA sea
ergódico ni que necesariamente caliente a temperatura infinita.

## 4. Batería inicial común, anterior a cualquier respuesta de la red

Observables: Re(W), Im(W) para los seis tipos W=R_xx,R_yy,R_zz,T_x^x,T_y^y,T_z^z
en la celda de origen. Fuentes: las mismas doce palabras hermíticas trasladadas
a s∈{-1,0,1}³. Tiempos n=1,2 ticks. Respuesta
`χ_AB(n)=i Tr(ρ [B,U^-n A U^n])`.

Primer filtro: al menos una respuesta de esta batería debe ser exactamente
no nula en el estado seleccionado. Todas nulas significa fallo de la batería
de selección, no ausencia de toda respuesta para observables desconocidos.
No elegir un observable después para rescatarla.

Una respuesta finita no es PASS IR: antes de extrapolar se requiere una
familia de volumen con error explícito, control local y un criterio uniforme
congelado en contrato posterior. No se inventa un umbral desde los datos.
No se ejecuta esta batería many-body mientras falte el método controlado.

## 5. Orden, límites de trabajo y estados

1. Primero A0: intento algebraico localizado. Un certificado de conmutador
   físico no nulo activa B; un control 3×3 no sustituye ese certificado.
2. Si el intento no cierra, un expediente acotado documenta lo intentado,
   artefactos y límite de método. Se puede activar B con A OPEN, sin llamarla
   refutada. No añadir pesos, annealing ni ángulos como tercer rescate.
3. B no hereda PASS de estacionariedad como PASS de respuesta/IR. Si B también
   falla o queda sin método controlado, registrar `IR_SELECTION_OPEN_AFTER_AB`
   y volver al diseño inverso, conservando el tick como control limitado.

Presupuesto del primer intento A0: una derivación algebraica con la regla
fijada y, si se puede especificar sin Hilbert space exponencial, un certificado
permanente; sin barrido espectral. Para B0, un expediente separado de promedio
y acceso local. La presente etapa cierra la selección y criterios de A/B,
no sus pruebas many-body.

## 6. Controles algebraicos y antecedentes

Código `scripts/verify_inverse_gravity_ir_options_ab.py` verifica en controles
3×3 que un Gibbs auxiliar no es automáticamente estacionario, y que un
promedio puede ser estacionario, no tracial y tener respuesta no nula.
Esos controles no deciden A0 ni B1/B2 del tick espacial.
Contrato y código se versionan antes de ejecución.

Prior art y distinciones comprobadas están en
[el informe A/B](../reports/2026-10-08--inverse-gravity-ir-options-ab.md).
