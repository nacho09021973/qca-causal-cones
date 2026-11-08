# Auditoría de decaimiento: el límite real requiere control global

2026-11-06. PRELIMINARY, derivación de autor sin revisión independiente.
Contrato OCCUPIED_MEMORY_DECAY_GATE.md, hash previo
77e490fae06589afb39b78abdc02dd7c7946ae2c9afaff22a9d63b627f5ac756.
Continuación del cálculo Abel, sin cambiar modelo, estado o parámetros.
Biblioteca local ausente; esta nota deriva identidades del símbolo
definido en el repo, no atribuye un teorema dispersivo a una fuente.

## Cotas más informativas que la unitariedad sola

Sean D_a(r,x)=||u_a(r,x)||_F²/4, distribuciones normalizadas. Para
F_a,r=sum_x u_a(r,x)D_b(r,x)exp(-iq.x), vale

    ||F_a,r|| <= 2 sum_x sqrt(D_a) D_b
              <= 2 sqrt(sum_x D_a D_b),
    ||F_a,r|| <= sup_x ||u_a(r,x)||_F.

La primera desigualdad de Cauchy usa sum_x D_b=1. La segunda cota
usa directamente la media convexa de los propagadores. Son vías
independientes para mejorar la cota uniforme, si se controlan solapamiento
o dispersión puntual. El solapamiento no tiene una ley temporal probada
en los cálculos actuales.

Si se demostrara ||u_a(r,x)||_F<=C r^-alpha uniformemente en x,
se obtendría ||K_r-1||<=C r^-alpha y, por soporte finito,
||partial_ki K_r-1||<=C(r+1)r^-alpha/sqrt3.
Por tanto alpha>1 basta para sumar absolutamente la memoria y alpha>2
para sumar también estas cotas de las primeras derivadas. Una cota
puntual de orden r^-3/2, incluso si estuviese demostrada globalmente,
no bastaría por esta vía para las pendientes. No se afirma aquí que
ese exponente sea válido para estos walks.

## Representación oscilatoria exacta

Con medida normalizada de Haar en el toro de coordenadas crudas,

    F_a,r(q)=(1/4) integral dp dl U_a(p)^r
                  tr[U_b(l)^r U_b(p+l-q)^(r dagger)].

La identidad se obtiene sustituyendo los tres Fourier e imponiendo
q=p+l-m; no es una aproximación de continuo. Es también válida usando
la parametrización redundante del BCC del evaluador, con su medida
normalizada y sus condiciones de paridad.

En una región sin cruces, descomponer los símbolos en eigenfases
omega_a,alpha y omega_b,beta, omega_b,gamma da fases

    Phi(p,l;q)=omega_a,alpha(p)+omega_b,beta(l)
                                      -omega_b,gamma(p+l-q).

Las condiciones estacionarias son

    v_a,alpha(p)=v_b,gamma(p+l-q),
    v_b,beta(l)=v_b,gamma(p+l-q).

Son coincidencias de velocidades de grupo de tres ramas en toda la
zona de Brillouin, no solo igualdad de las dos pendientes IR. Las
amplitudes contienen proyectores espectrales y sus productos.

Si las contribuciones relevantes tuvieran fases suaves, puntos críticos
aislados y Hessianos no degenerados en seis variables, la estimación
usual de fase estacionaria daría una potencia r^-3 para F; una derivada
externa puede perder una potencia, dejando r^-2, todavía sumable.
Esto es un criterio CONDICIONAL: no se ha verificado para estos símbolos.
No se presenta como prueba de su convergencia.

## Hipótesis que faltan y decisión

Los walks fijados tienen cruces cónicos en k=0 en ambas fases ±pi/4:
la forma nodal documentada es ±c_a|k|. Las eigenfases individuales no
son diferenciables allí y sus proyectores no tienen una prolongación
individual suave a través del cruce. En la integral existen regiones
con p, l o p+l-q en esos cruces. El símbolo matricial sí es suave;
la singularidad de ramas podría cancelarse al sumarlas, pero esa
cancelación debe demostrarse antes de aplicar el criterio anterior.

También falta clasificar puntos estacionarios y Hessianos en el resto
del toro. No se conoce aquí una cota que elimine contribuciones de
variedades críticas o degeneraciones. No se deduce que existan ni que
la suma diverja: las hipótesis suficientes permanecen sin verificar.

El estado usado asigna la misma ocupación a todos los modos. No
suprime los de gran momento: la aproximación de cono IR no tiene un
pequeño parámetro que justifique reemplazar toda esta integral. Ello
explica por qué el resultado RG de una teoría de baja energía no puede
trasladarse simplemente al cálculo actual.

Estado: GLOBAL_DISPERSIVE_ESTIMATE_REQUIRED /
REAL_FREQUENCY_LIMIT_NOT_PROVED. La ruta de justificar el límite
mediante una potencia inferida del cono local queda descartada. No
queda refutada la convergencia real del núcleo ni la hipótesis física.

Para continuar este modelo hace falta una prueba dispersiva global que
trate cruces y estacionariedad degenerada, con control de derivadas.
Elegir un estado de baja energía sería otra ruta y cambiaría el problema;
no se hace silenciosamente aquí. Un barrido mayor de retardos puede
orientar, pero no satisfaría la obligación analítica identificada.

Sin nuevos resultados numéricos o scripts; toda la derivación está
conservada en esta nota. Las dos formulaciones (cotas espaciales e
integral oscilatoria) coinciden en exigir más que unitariedad y localidad.
Autocomprobación, no revisión independiente. git diff --check.
