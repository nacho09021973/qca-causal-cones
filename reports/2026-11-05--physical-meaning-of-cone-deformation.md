# Qué cambio físico representa la deformación

2026-11-05. Codex. Especificación de interpretación y de pregunta,
autorizada por el usuario «empecemos como dices». PRELIMINARY, sin revisión
independiente. No nuevo cálculo, script, simulación ni promoción.

## Frase física elegida

En un simulador de un quantum walk de cuatro niveles internos, se modifica
la rotación interna que precede y deshace una traslación condicionada,
manteniendo fijas las distancias de desplazamiento, la secuencia de
subpasos y la duración de una actualización. Se comparan las velocidades
de paquetes próximos a los dos dobletes nodales del mismo operador.

Es una interpretación como dinámica controlable de laboratorio. No se
afirma que los cuatro niveles describan partículas fundamentales, ni que
el parámetro evolucione por una interacción o un flujo de renormalización.

## Operaciones y parámetro

El espacio interno se descompone en sigma y tau, dos factores de dimensión
dos. Son registros internos, no dos partículas. En el constructor vigente,
G_i=sigma_i tensor T_i, L_i=sigma_i tensor I; cada G_i define proyectores
(I±G_i)/2 que se trasladan en sentidos opuestos. T_i es una observable
binaria interna con T_i²=I.

Se interpreta a como el coseno de un ángulo de orientación de T_i respecto
a tau_z. Su componente transversal es b=sqrt(1-a²). Una rotación unitaria
en tau lleva tau_z a T_i: por tanto el desplazamiento condicionado por
G_i puede representarse como una rotación local, un desplazamiento con
base de control fija y la rotación inversa. No se ha diseñado un montaje
experimental específico para las tres direcciones y estos cuatro niveles.

W fija las dos fases nodales respecto al eje tau_z. Cambiar las orientaciones
de los T_i manteniendo W fijo modifica su alineamiento relativo; no se
conjugan simultáneamente todos los operadores por un mismo cambio de base.
El cociente espectral c_P/c_Q ya calculado cambia con a, por lo que esta
variación no es una equivalencia global que conserve las dispersiones.

La modificación se realiza igual en todas las celdas. La parametrización
anterior conserva D2; no se afirma que D2, por sí sola, obligue a conservar
isotropía para perturbaciones arbitrarias. Mantener isotropía por elegir
el mismo ángulo en tres direcciones es una restricción adicional del
constructor, que debe declararse.

## Qué podría medirse

Protocolo propuesto, no ejecutado: preparar paquetes estrechos en momento,
cerca de k=0 y con centro k0 no nulo, en las ramas de pendiente positiva
de cada doblete. La preparación correcta debe aproximar los proyectores
espectrales dependientes de k; usar solo P o Q en k=0 deja errores de
preparación que habría que cuantificar. Medir desplazamiento del centro
por actualización y tomar el régimen de k0 y anchura pequeños.

La predicción ya disponible es c_P/c_Q=(1+a)/(1-a). Es una predicción de
propagación de paquetes de baja energía relativa a cada fase nodal, no la
velocidad máxima de grupo de todo el espectro ni el frente causal estricto.
Usar la misma escala espacial y temporal para ambos permite comparar el
cociente sin calibrar por separado las unidades de cada rama. Relojes y
detectores son externos al simulador: no resuelve la opción de observadores
internos.

Los dobletes están en fases Floquet distintas; habría que especificar su
preparación y lectura antes de asignarles significado experimental. No se
los identifica con luz y materia ni con dos especies a una energía común.

## Qué pregunta queda y cuál ya está contestada

Conocido: el ejemplo de doble desplazamiento produce c_P!=c_Q manteniendo
localidad, unitariedad, D2 e irreducibilidad, con las verificaciones de autor
registradas en el informe anterior. Por tanto, dentro de este alcance,
esas propiedades no bastan para exigir una velocidad común. Una nueva
tabla o una deformación que solo vuelva a variar a repetiría ese contenido.

Pregunta relevante de protección: ¿una condición microscópica adicional,
justificada independientemente, obliga a igual velocidad para todas sus
perturbaciones admisibles? No se ha identificado aquí esa condición.
Exigir directamente igualdad, duplicar dos bloques idénticos o descartar
las perturbaciones porque separan velocidades no sería una explicación.

Criterio de corte antes de nuevos cálculos: no ejecutar una deformación
adicional hasta especificar la operación física que cambia y la hipótesis
independiente que se contrasta. La interpretación de laboratorio permite
dar sentido a a, pero por sí sola no justifica una candidatura de novedad
ni una explicación del valor físico de c.

## Fuente externa y alcance de comprobación

Rotaciones internas y traslaciones condicionadas son operaciones estándar
en quantum walks. Fuente primaria experimental localizada mediante
extracto del registro editorial: Kitagawa y colaboradores, Observation of
topologically protected bound states in photonic quantum walks,
Nature Communications 3, 882 (2012),
https://www.nature.com/articles/ncomms1872 . El extracto describe rotaciones controladas
con placas y un walk split-step. Es evidencia de esas operaciones básicas;
no evidencia de implementación de nuestro constructor 3D de cuatro niveles.
El acceso directo al texto completo falló por redirección del sitio;
la revisión completa del montaje queda [UNVERIFIED].
No se usa esa realización para atribuir novedad al mecanismo.
