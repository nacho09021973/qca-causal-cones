# Primer control del puente: el vacío no permite esta igualación

2026-11-06. PRELIMINARY, derivación de autor, sin revisión independiente.
Contrato INTERACTING_VELOCITY_BRIDGE_GATE.md, hash previo
4d4f83abe318bee404051f878cf970f25b65cf92a7d4a3cad59908023ccd6f45.

## Resultado exacto en la clase fijada

Sea P_1 el proyector al sector global de una partícula. En cualquier
configuración de ese sector, N_1(x)N_2(x)=0 para toda celda: no pueden
estar ocupadas ambas especies. Por tanto V_chi P_1=P_1 para todo chi.
Como U_0 conserva número, U_chi P_1=U_0 P_1. Iterando,
U_chi^t P_1=U_0^t P_1 para todo entero t. El vacío también es invariante.

Así las dispersiones de una excitación sobre el vacío son exactamente
las libres, aunque la dinámica tenga interacciones genuinas en otros
sectores. Si las dos velocidades iniciales difieren, siguen distintas.
No hay corrección perturbativa escondida: el subespacio es invariante
y la igualdad de operadores allí es exacta.

Segunda formulación: el propagador de vacío
G_ab(x,t)=<0|c_a(x) U_chi^t c_b†(0)|0>
solo visita el sector de una partícula y coincide con el libre.
En cambio una configuración con ambas especies ocupando una celda
recibe la fase exp(-i chi); la interacción no es trivial globalmente.

Unitariedad y localidad del paso: U_0 es una evolución fermiónica libre
causal; V_chi es producto de puertas pares unitarias in situ. Su
composición sigue siendo causal de alcance finito. Esto no establece
que tenga un límite relativista interactuante ni una velocidad emergente.

## Consecuencia para el programa

Se descarta medir igualación mediante un paquete de una partícula en
vacío para esta colisión. No se descarta el mecanismo RG publicado:
su vacío relativista y sus grados de libertad no se identifican con
este vacío de Fock conservativo sin una derivación.

La siguiente obligación concreta es definir un estado ocupado
estacionario y su función de respuesta. Un relleno de bandas libres
no puede llamarse vacío interactuante estacionario sin comprobarlo.
En Floquet tampoco hay una energía fundamental canónica derivada solo
de ordenar quasienergías módulo 2pi. Elegir arbitrariamente una rama
del logaritmo no resuelve esa obligación.

Una posible ruta futura es un circuito cerca de un límite Hamiltoniano
y un régimen temporal controlado, pero su control, estado y escala son
[UNVERIFIED]. No se presenta esa propuesta como mecanismo realizado.

Este resultado determina dónde una simulación sería incapaz de probar
la hipótesis, antes de gastar recursos en ajustes de velocidades.
Estado: VACUUM_ONE_PARTICLE_ROUTE_CLOSED; MANY_BODY_STATE_REQUIRED.
No novedad, no promoción, no conclusión a densidad finita.

Control permanente: scripts/verify_interaction_vacuum_sector.py, enumera
los 256 estados locales de ocho modos. El argumento universal depende
de conservación del número, no del tamaño de esa enumeración.
Registro en 2026-11-06--interaction-vacuum-sector-verifier.txt.
