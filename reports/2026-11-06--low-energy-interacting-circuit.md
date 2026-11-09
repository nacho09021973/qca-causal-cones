# Circuito, estado de baja energía y primer flujo RG

2026-11-06. PRELIMINARY, derivación de autor; sin revisión independiente
ni promoción. Contrato LOW_ENERGY_INTERACTING_CIRCUIT_GATE.md, SHA256
b8b8327b4779bd8b7fd064b30c393f61d559caa2b94e47b6c43fa3143f260252.
Usuario «haz los tres». Cambio explícito autorizado: red cúbica,
Hamiltoniano Wilson y estado de baja energía, en lugar del circuito BCC
y el estado infinito-temperatura. Los resultados anteriores se conservan.

## 1. Circuito unitario de alcance finito

Dos especies con cuatro modos locales cada una, v1=1/3,v2=2/3,
alpha_i=tau_x tensor sigma_i, beta=tau_z tensor I. Se define

    h_a(k)=v_a sum_i alpha_i sin(k_i)+beta sum_i(1-cos(k_i)),
    H=H_free+g sum_x (N1(x)-2)(N2(x)-2).

En espacio real, H_free tiene onsite 3 beta y enlace orientado
T_ai=(-i v_a alpha_i-beta)/2, con término
c_a(x)† T_ai c_a(x+e_i)+h.c. La reconstrucción Fourier se comprueba
exactamente. Cada modo conserva su carga de especie; la interacción
es genuinamente cuártica y local.

En un toro L³ con L par, separar los enlaces en seis capas disjuntas
(eje i y paridad x_i). Junto con la capa onsite, son siete H_l cuya
suma es H. La capa onsite incluye interacción y ambos términos 3 beta.
Definir el paso simétrico

    U_delta=exp(-i delta H_0/2)...exp(-i delta H_5/2)
             exp(-i delta H_6)
             exp(-i delta H_5/2)...exp(-i delta H_0/2).

Cada capa es producto de puertas pares unitarias en sitios o enlaces
disjuntos. Un paso tiene profundidad finita y alcance finito (cota
conservadora de doce enlaces); define un QCA fermiónico. La periodicidad
espacial puede ser dos; no se afirma covariancia cúbica exacta del paso.
Tiempo físico de un periodo delta, espaciado uno. El límite Hamiltoniano
es delta->0 a tiempo físico fijo, no una identificación exacta a delta finito.

## 2. Estado de referencia y régimen controlado

El álgebra de Clifford da eigenenergías ±E_a(k), cada una doble,

    E_a(k)^2=v_a² sum_i sin²(k_i)+[sum_i(1-cos(k_i))]².

Único cero en el toro: k=0. Cerca del cero E_a=v_a|k|+O(|k|³).
El término Wilson elimina otros ceros a cambio de permitir un operador
de masa: su estabilidad interactuante no se presupone.

Condiciones antiperiódicas en las tres direcciones, L par, eliminan
el momento cero en volumen finito. A medio llenado por especie, llenar
todas las bandas negativas da un estado libre único. Sea Delta_L el gap
muchos-cuerpos libre dentro de ese sector: Delta_L>=2 min_(a,k) E_a(k)>0.
La norma de V=sum_x(N1-2)(N2-2) satisface ||V||<=4L³. Weyl implica
que el gap perturbado es >=Delta_L-8|g|L³. Por tanto

    |g|<Delta_L/(8L³)

es una condición suficiente conservadora para un estado fundamental
interactuante único, definido como eigenvector de menor energía de H
en ese sector, conectado al estado libre. Es estacionario bajo H.
La cota NO es uniforme en L; no demuestra fase crítica termodinámica.

El estado no se declara eigenestado de U_delta. Hay control de esa
aproximación: si S=sum_l||H_l||, simetría y consistencia de Strang
hacen coincidir las expansiones hasta delta². Las cotas de restos de
exponenciales dan un error de un paso <=exp(delta S)(delta S)^3/3.
Telescopando n pasos, T=n delta,

    ||U_delta^n-exp(-i T H)|| <= T delta² S³ exp(delta S)/3.

Una cota conservadora es S<=L³(30+4|g|): onsite <=L³(12+4|g|),
cada capa de enlaces <=3L³. El régimen finito explícito es el lado
derecho mucho menor que uno. Para observables acotados su error de
expectación es <=2||O|| por esa cota; controla también correlaciones
de operadores fermiónicos acotados a tiempos fijos. No ofrece por sí
sola control uniforme termodinámico o a tiempo infinito.

Observable propuesto: respuesta retarded sobre ese estado fundamental
de H y su aproximación por el circuito en el régimen anterior. Apagar
g recupera exactamente las dos pendientes v1,v2 del Hamiltoniano.

## 3. Flujo: lo calculado y lo pendiente

En el continuo local cerca del nodo, z=1,d=3, la acción cinética fija
[psi]=3/2. El operador de contacto (psi1†psi1)(psi2†psi2) tiene dimensión
6, mientras la densidad lagrangiana tiene dimensión 4. El acoplamiento
tiene dimensión -2. Para acoplamientos adimensionales u_I, incluidos
los canales cuárticos que puedan generarse, y ell=log(Lambda0/Lambda):

    du_I/dell=-2u_I+O(u²).

La superficie de velocidades libres distintas es una familia de puntos
fijos gaussianos: los términos cinéticos tienen dimensión marginal.
Para el único vértice inter-especie inicial, la autoenergía a orden g
es un tadpole independiente del momento. En el estado libre de medio
llenado <N_a>=2, la sustracción escogida lo cancela. No hay contracción
Fock entre especies sin coherencia entre ellas. Así no hay corrección
de pendiente a orden g; posibles correcciones empiezan en orden dos.

    dv_a/dell=O(u²),
    d(v1-v2)/dell=O(u²).

NO se ha calculado el coeficiente ni el signo de ese orden dos. El
conteo de potencias no los determina. Además deben seguirse masas,
potenciales químicos y otros operadores relevantes permitidos;
mantener el régimen sin gap puede requerir contratérminos ajustados.
No se declara que las interacciones conserven automáticamente el nodo.

En el régimen débil gaussiano, si esos coeficientes son regulares y
se permanece en la superficie crítica, u(ell)~u0 exp(-2ell). Entonces
integral_0^infinito u(ell)² dell=u0²/4: la corrección acumulada es
finita O(u0²). No obliga a borrar una separación inicial finita de
velocidades, como 1/3. Aun si un término fuese -A u²(v1-v2), con A
positivo acotado, dejaría un factor final no nulo; esto es un argumento
condicional, no el coeficiente calculado de este modelo.

Resultado del intento débil: NO_COMMON_SPEED_ATTRACTOR_ESTABLISHED;
el conteo RG y la familia gaussiana descartan inferir universalidad
solo por añadir este contacto débil. No se refutan regímenes críticos
interactuantes, interacciones mediadas o fuertes, que no se ejecutan aquí.

## Evidencia y obligaciones pendientes

scripts/verify_low_energy_circuit.py comprueba Clifford, dispersión,
reconstrucción de enlaces, derivadas nodales y flujo canónico; registro
en 2026-11-06--low-energy-circuit-verifier.txt. El circuito interactuante
y las cotas se justifican arriba; no se simula su espectro completo.

Antecedentes primarios consultados: Roy–Das Sarma, Phys. Rev. B 94,
115137, https://link.aps.org/accepted/10.1103/PhysRevB.94.115137,
identifica interacciones cortas irrelevantes cerca del régimen gaussiano;
no prueba nuestro modelo particular. Childs et al., arXiv:1912.08854v3,
https://arxiv.org/abs/1912.08854, antecedente de fórmulas de producto;
la cota conservadora usada aquí se deriva por Taylor y telescopado,
no se atribuye a un teorema no leído. Biblioteca local ausente.

Se completan construcción explícita y estado con régimen finito
controlado. El flujo está derivado a orden canónico y primer orden
cinético, NO a segundo orden. Pendientes: coeficientes a dos lazos,
masa crítica y régimen termodinámico/de tiempo largo. Resultado
PRELIMINARY; ninguna de esas obligaciones se marca resuelta.
