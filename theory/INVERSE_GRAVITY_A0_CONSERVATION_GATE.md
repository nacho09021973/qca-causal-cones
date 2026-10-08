# A0 — conservación del Hamiltoniano auxiliar en el sector físico

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Padre [opciones A/B](INVERSE_GRAVITY_IR_OPTIONS_AB.md).
Tick y H_A exactamente los ya congelados; no se varían parámetros.
Contrato y código previos a la ejecución.

## Testigo y prueba fijados

Estado físico ψ0 de IG1c: producto X=1 promediado sobre los V, normalizado.
Todos los R_aa(i) tienen eigenvalor 1 en ψ0.
H_A=H_R+H_T, donde H_R=-sum A_R y H_T=-sum A_T.
U_R actúa como fase en ψ0; U_T conmuta con H_T. Por tanto

`<Uψ0,H_A Uψ0>-<ψ0,H_A ψ0>
 = <U_Tψ0,H_R U_Tψ0>-<ψ0,H_R ψ0>`.

Para cada tipo R_aa en el origen se enumeran exactamente todas las puertas
T que no conmutan con esa palabra. Las demás se cancelan en U_T† R U_T.
Construir las cargas R de esas palabras T y comprobar independencia lineal
de sus vectores de cargas sobre F3. Si son independientes, toda combinación
no trivial cambia algún eigenvalor R; su expectativa en ψ0 es cero.
Esto permite extraer el coeficiente identidad de la conjugación sin una
Hilbert space many-body ni una hipótesis de independencia estadística.

Para una puerta T con relación de Weyl no trivial s=±1, el factor constante
de la conjugación es la media sobre las tres raíces de la razón de fases
g(ω^s z)/g(z), con g(z)=exp[-iπ Re(z)/3]. Comprobar ambos signos exactamente.
Si los vectores de cargas son independientes, los factores constantes se
multiplican. Usar el resultado para cada R y la densidad de cambio de H_A.

## Criterios y segunda vía

Script permanente `scripts/verify_inverse_gravity_a0_conservation.py`.
Tolerancia cero. Comprobar incidencias por stencils y por la formulación
geométrica independiente de IG1c. Rank sobre F3, no sobre reales.
La prueba se aplica a toros L≥6 múltiplo de 6: la caja de cargas local no
sufre identificaciones periódicas. Traslaciones/permutaciones cíclicas
transportan la comprobación a todos los términos H_R.

Si la densidad de cambio de energía es no nula exactamente:
`A0_FAIL_NONCONSERVED_PHYSICAL_PARENT`, activar B0 sin cambiar la semilla.
Si es cero, solo `FROZEN_ENERGY_WITNESS_ZERO`: no proclamar conservación.
Si no se prueba independencia, `A0_METHOD_UNRESOLVED`: no atribuir factores
independientes por suposición ni cambiar testigo dentro del contrato.

No se calcula Gibbs, espectro, ground state, respuesta IR o gravedad.
Un fallo excluye la opción A de Gibbs conservado; no excluye otros estados.
