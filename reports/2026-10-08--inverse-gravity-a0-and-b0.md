# A0 falla; B0 activada y acceso local delimitado

Fecha: 2026-10-08. Rama `research/inverse-gravity-design`.
Contrato A0 y código congelados en `bc2da80e22525733ba8feef972e8ca801d0fbfa6`:
[contrato](../theory/INVERSE_GRAVITY_A0_CONSERVATION_GATE.md),
[script](../scripts/verify_inverse_gravity_a0_conservation.py).
Padre: [opciones A/B](../theory/INVERSE_GRAVITY_IR_OPTIONS_AB.md).

## 1. Resultado A0 y procedencia

Comando `python3 -B scripts/verify_inverse_gravity_a0_conservation.py`.
Código 0, exacto; salida íntegra en
[certificado](2026-10-08--inverse-gravity-a0-certificate.txt).
SymPy 1.14.0 para fases; rank y densidad calculados sobre F3 y racionales.
No cambió regla, estado testigo, θ, q ni H_A después de ejecutar.

`A0 = FAIL_NONCONSERVED_PHYSICAL_PARENT`.
La ejecución correcta del certificado da un fallo científico de la opción A,
no un error de ejecución. Evidencia propia, sin revisión independiente.

## 2. Demostración dentro del sector, para el tick completo

ψ0 del contrato vive en S=V=1 y tiene todos los R=1. U_R actúa como fase
en él y U_T conmuta con H_T. Por ello el cambio de expectativa de H_A
bajo U_T U_R es exactamente el cambio de H_R bajo U_T.

Cada R_aa tiene 16 puertas T con fase de Weyl no trivial en su conjugación.
El certificado construye las cargas de esas palabras T en todos los R que
pueden detectarles. Rank F3=16 para los tres tipos R. Esto significa que
ninguna combinación no trivial de esas 16 palabras devuelve todos los
eigenvalores R a 1. Su expectativa en ψ0 es por tanto cero.

Así, extraer el coeficiente identidad del producto de factores de conjugación
es exacto. No se supuso un estado producto de esas variables físicas.
Las cargas se comprueban por stencils y por vértices de cubos, dos
formulaciones ya independientes en IG1c.

La media de razón de fases de una puerta afectada, sobre las tres raíces,
es exactamente 1/3 para ambos signos de Weyl. La única combinación que
puede contribuir a la expectativa es la identidad, por la independencia:

`<ψ0,U_T† R_aa U_T ψ0>=3^-16=1/43046721`.

El valor es real, de modo que también da <A_R>. Traslaciones y permutaciones
cíclicas llevan el cálculo a cada uno de los 3L³ términos. La caja de cargas
local no sufre aliasing en los toros L≥6 múltiplo de 6 fijados. Entonces

`Delta <H_A>=3L³(1-3^-16)`,
`Delta <H_A>/L³=43046720/14348907 >0`.

H_A no conmuta con U dentro del sector físico. Por la equivalencia de IG1e,
el Gibbs de H_A a β=1 no es estacionario. A queda descartada al alcance
del contrato. No se excluye que algún estado correlacionado particular o un
proyector de mínima energía tenga otra propiedad; no se usa como rescate aquí.

## 3. B activada con la misma semilla

Se activa B0 por el fallo A0, sin una nueva elección:

`σ_B,L=P exp(-H_A) P / Tr_P exp(-H_A)`,
`ρ_B,L=lim_M M^-1 sum_(n=0)^(M-1) U^n σ_B,L U^-n`.

H_A selecciona la semilla; no se le exige conservarse en B. Tick, θ=π/3,
q=3, constraints y batería de respuesta siguen fijos. Existencia y
estacionariedad en volumen finito se demostraron en IG1e; B1/B2/B3 siguen OPEN.
No se calculó ρ_B ni una respuesta de la batería.

## 4. Avance B0: acceso por observables, sin matriz completa

Para cualquier observable local A y promedio truncado:

`Tr(ρ_M A)=Tr(σ_B,L Abar_M)`,
`Abar_M=M^-1 sum_(n=0)^(M-1) U^-n A U^n`.

Es una identidad dual exacta. Con el alcance ≤3 celdas por tick de IG1b,
Abar_M queda en el vecindario de radio ≤3(M-1) del soporte de A. Solo
se necesita la densidad reducida de σ_B,L en esa región para esa expectativa.
La reducción evita escribir la unitaria de toda la Hilbert space, pero no
demuestra un algoritmo eficiente: el soporte crece y las correlaciones Gibbs
restringidas siguen siendo un problema many-body.

No sustituir esa densidad reducida por el Gibbs del bloque aislado: el
acoplamiento con el exterior y las constraints pueden cambiarla. Haría falta
una cota de error de frontera o un método de contracción certificado.
No se implementó una aproximación sin ese control.

## 5. Error de promedio: dos controles distintos

El telescopado de IG1e da `||Uρ_M U†-ρ_M||_1≤2/M`. Es defecto de
estacionariedad; no es distancia al ensemble límite.

En volumen finito, con Π_φ los proyectores de quasifase, cada bloque de fase
diferente tiene el filtro geométrico

`f_M(δ)=exp[i(M-1)δ/2] sin(Mδ/2)/(M sin(δ/2))`,
`|f_M(δ)|≤min(1,1/(M|sin(δ/2)|))`.

Si se dispusiera de una cota positiva γ_L para todos los |sin(δ/2)| no
nulos y D_L=dim(H_P), la ortogonalidad Hilbert–Schmidt de los bloques daría

`||ρ_M-ρ_B,L||_1 ≤ sqrt(D_L) ||σ_B,L-ρ_B,L||_2/(M γ_L)`.

Es una cota condicional, no un método computable ya disponible. No se conocen
γ_L ni un control uniforme útil y la dimensión es grande. Las coherencias
degeneradas no se incluyen en γ_L: permanecen dentro de Π_φ σ Π_φ.

Para la respuesta de la batería, cualquier cota ε de distancia de estado
daría `|χ_M-χ_B|≤2||A||||B|| ε`. La mera cota 2/M de estacionariedad no
puede usarse como ε. Elegir un M cómodo y observar una respuesta sería
insuficiente para un PASS de B.

## 6. Decisión y frontera

`A = REJECTED_FOR_FROZEN_CONSERVED_GIBBS_ROUTE`.
`B0 = ACTIVE / CONTROLLED_LOCAL_ACCESS_OPEN`.
`B1/B2/B3 = NOT_EXECUTED`; `IR_STATE_SELECTION_OPEN`.

B dispone de una reducción exacta a observables locales y de las obligaciones
de error anteriores. El siguiente paso admisible es especificar un método
certificado para las expectativas de la semilla y el promedio: sin ambos
controles no se calcula ni anuncia respuesta convergida.

Si no se obtiene ese método en el expediente acotado B0, B seguirá OPEN por
limitación de control y se registrará `IR_SELECTION_OPEN_AFTER_AB`. No se
dedicará un barrido de matrices pequeñas o tiempos al circuito sin conexión
con el objetivo gravitatorio. No se cambian pesos, ángulos, β ni la meta.

La influencia de un paso del tick permanece válida; no implica una energía
conservada. No se afirma gravedad, dos polarizaciones ni dispersión IR.
