# Comprobación de las objeciones de Claude al experimento Thirring

2026-11-08. Autor: Codex/OpenAI. **PRELIMINARY, comprobación de autor**.
Usuario: «comprueba lo que dice claude». Contrato acotado
[THIRRING_CLAUDE_OBJECTIONS_AUDIT.md](../theory/THIRRING_CLAUDE_OBJECTIONS_AUDIT.md),
versionado antes de ejecutar junto con el script en `45b933f`.

El [informe sellado de Claude](../debates/2026-11-08--thirring-two-node-rereview-opus/informe_opus.md)
se conserva intacto. Se ha comprobado contra la regla y el código, no se usa como
fuente científica. No se solicitó otra revisión. La comprobación distingue la
validez de una objeción de la aplicación de la reparación que propone.

## Dictamen por objeción

| Objeción | Comprobación del autor |
| --- | --- |
| O1: transferencia fuera del nodo 0 | Correcta la probabilidad modal sin²(chi/2). Excesivas las consecuencias si se extienden al sector de dos nodos o a circuitos cuyo número de colisiones crece. |
| O2: universalidad unitaria frente a potencia computacional | Válida la precisión: solo se ha excluido un conjunto unitario universal en este código; no se ha demostrado una separación de clases de complejidad con preparación/medida. |
| O3: ancillas | Válida como petición de cuantificadores explícitos. El contrato original admite paquetes de componente fija y soportes disjuntos de igual componente; no cualquier ancilla de Fock. La ampliación propuesta por Claude necesita un proyector de sector. |
| O4: geometría de cierre | Válida para evitar una lectura incondicional de la tabla. El cuerpo de la prueba ya exige cruce completo de todos los componentes. El contraejemplo solapado tiene fuga persistente, pero su valor NO es constante para todo T. |
| O5: pruebas redundantes y estructurales | Recuentos 49/9/40 y 18 confirmados. Son controles redundantes o de consistencia, no evidencia independiente de las leyes físicas. «No pueden fallar» es demasiado literal para código flotante. |
| O6: estadística fermiónica | Correcta: el propagador antisimétrico R+L no discrimina estadística de intercambio. Su valor es como implementación reticular distinta. El orden de modos de tres paquetes se justifica por álgebra. |
| O7: c_IR y alpha | Válida la aclaración terminológica: c_IR del nodo 0, misma velocidad de envolvente en pi tras retirar portador; alpha debe definirse. La velocidad de grupo general de muchos cuerpos sigue sin calcularse. |
| O8: dominio, fuente y observación masiva | (a) mu=0 es extensión al borde de la familia publicada. (b) la consulta del primer artículo faltaba, pero este también usa notación local esquemática: no aporta la supuesta definición global explícita ausente del segundo. (c) correcta la carga interna alternante; incorrecta su identificación directa con suma de X de nodo. |
| O9: redondeo y procedencia | Son aclaraciones válidas; los commits distintos y los valores redondeados no son una contradicción. Historial y hashes permiten reconstruir las ejecuciones. El campo contract_commit es metadato declarado. |

## O1: lo que sale del nodo 0 y lo que permanece cerrado

Desde la regla de contacto: cuando R empieza completamente a la izquierda de L
y se completan todos los encuentros, en el código nodal

\[
 S_\chi|00\rangle=a|00\rangle+b|11\rangle,\qquad
 |b|^2=\sin^2(\chi/2).
\]

Esta probabilidad de **modo lógico** es exacta para cualquier M. No es una
probabilidad de momento estrictamente limitado para M finito: los paquetes
uniformes tienen colas. Por la concentración de Fourier demostrada en el informe
original, en el límite M grande también da la probabilidad del sector próximo
a (pi,pi), para ventanas fijas separadas. Vale 1/2 en chi=pi/2 y 1 en chi=pi.
Se confirma O1(i): un sector restringido a ambos momentos cerca de cero no es
cerrado bajo esta colisión con chi fijo no trivial.

Pero el experimento ampliaba precisamente la codificación a **ambos** nodos.
Tras un cruce completo, su unión es cerrada en el sentido de envolventes
asintóticamente concentradas, y el código finito de cuatro modos es exactamente
cerrado. Ambos nodos poseen la misma cinemática libre de transporte tras retirar
el portador. Por tanto, la afirmación «son sectores distintos» requiere especificar
si se habla del sector de baja cuasienergía de un paso o del sector ampliado de
Floquet. O1 no demuestra que toda descripción relativista de dos nodos sea
imposible. Tampoco se ha probado que la dinámica interactuante sea relativista.

Además, dos portadores pi producen cuasienergía total 2pi, equivalente a cero
módulo 2pi; no cabe inferir un coste energético físico arbitrario de este salto.
El resultado de la colisión es una coherencia nodal, sin reinterpretarla como
un procesador de baja cuasienergía aislado.

O1(iii) se confirma solo para **un número fijo de colisiones**: si chi->0,
la concurrencia de una colisión |sin chi| tiende a cero. Nada en esa fórmula
excluye límites con número de interacciones creciente ni demuestra que un límite
continuo deba escalar chi de ese modo. No se ha estudiado tal límite aquí.

## O2: alcance lógico frente a complejidad

La prueba [sección 5 del informe](2026-11-08--thirring-two-node.md) establece
V† X_i V=+-X_i para las unitarias del código y recursos declarados. Por eso no
aproxima H sobre un dato desconocido y no es densa en U(2^n). El identificador
`MASSLESS_NODE_CODE_NOT_UNITARILY_UNIVERSAL` expresa exactamente ese resultado.
La fila «computación cuántica universal: no» y su lectura como imposibilidad
general de un procesador con entrada/salida clásica son demasiado amplias.

Preparaciones de producto y medidas finales en otra base producen distribuciones
de un circuito conmutante en X. No se demostró aquí ni simulabilidad clásica,
ni equivalencia o separación respecto de BQP, ni una reducción desde un modelo
IQP general: las geometrías de cruces son restringidas y chi es fijo. La analogía
IQP orienta, no prueba esas afirmaciones. El [artículo original de Shepherd y
Bremner](https://arxiv.org/abs/0809.0847) describe precisamente un modelo restringido
de cómputo y muestreo; su resumen fue consultado como orientación, no como prueba
de una clasificación de nuestro autómata.

No se necesita fijar una base de lectura para demostrar la no-densidad unitaria:
esa es una propiedad del canal sobre entradas cuánticas arbitrarias. Sí se debe
fijarla, junto con la preparación y el coste de la geometría/programa, antes de
formular una afirmación sobre la potencia de un modelo computacional completo.

## O3: identidad de región y cuantificadores de ancillas

Para un paquete R, sea S su soporte inicial y S_t=S+t; para L, S_t=S-t.
Definimos en Fock

\[
 \Gamma_t=(-1)^{\sum_{x\in S_t}x n_R(x)},\qquad
 N_t=\sum_{x\in S_t} n_R(x).
\]

Como U† n_R(x)U=n_R(x-1), la identidad exacta es

\[
 U^\dagger\Gamma_{t+1}U=\Gamma_t(-1)^{N_t}.
\]

Esta sí vale en todo Fock. En el **sector** N_t=1 se reduce a -Gamma_t.
No es una identidad sin proyector en todo Fock: el vacío da 1=1, mientras que
la versión con signo menos daría 1=-1. Hay además que seguir la región móvil;
una Gamma sobre una región fija no se convierte en sí misma al trasladar.
La frase de Claude «identidad de operadores en todo el Fock» seguida de
signo fijo y «con un solo R» necesita precisamente esa restricción sectorial.

Para todos M>=1, chi real, T>=0 y un número finito de paquetes de componentes
fijas, con soportes disjuntos de la misma componente y un fermión por paquete,
la identidad prueba la conservación de la paridad del dato en el marco móvil.
Ancillas inicialmente independientes en los demás paquetes del contrato no la
rompen, ni en cruces parciales. La ampliación a un estado externo de Fock con
soporte R fuera de S y L arbitrario se deduce de la misma identidad, a número
finito de partículas. No se reclama una extensión a representaciones de
densidad infinita ni a ancillas R dentro del soporte del dato.

Esa última clase de ancillas queda fuera del contrato original y la afirmación
de Claude sobre separar sus paridades en un «dato» no se adopta sin definir una
factorización de modos. No hace falta resolverla para el no-go ya probado.

## O4: soportes coincidentes y tiempo

En R y L con soporte {0,...,7}, un componente (x,y) recibe fase si
y-x es par y 0<=(y-x)/2<=T-1. Dentro de cada bloque de paridades de 16 pares,
si una fracción q ha recibido fase, su fuga es

\[
 1-|1-q+qe^{i\chi}|^2=2q(1-q)(1-\cos\chi).
\]

Por conteo exacto: en T=0, q=0; en T=1, q=1/4; desde T=4, q=10/16=5/8.
Por tanto, para chi=pi/2, las fugas máximas sobre entradas del código son
0, 3/8 y 15/32, respectivamente. La afirmación de Claude «15/32(1-cos chi)
para todo T» es falsa; se vuelve correcta **para T>=4** en ese ejemplo.
Se confirmó por dos vías: fracciones racionales de contactos y propagación
directa con proyección/SVD. No se completó un cruce de todos los componentes:
los que ya empezaban separados no se encuentran nunca.

Una condición suficiente limpia para la fórmula S_chi es
max supp(R)<min supp(L), y T mayor que el último tiempo de contacto permitido.
Es suficiente, no necesaria: por ejemplo una regla identidad también cierra
soportes solapados. La prueba original comenzaba con y>x y «cruce de todos
los componentes», por lo que este ejemplo no refuta su enunciado condicional.
Sí justifica hacer explícita la geometría en los resúmenes y en los metadatos.

## O5 y O6: contenido real de la verificación

Recuento desde el JSON versionado original, sin adoptar el recuento de Claude:

| Tipo al reclasificar los mismos 228 controles | Número |
| --- | ---: |
| Propagador frente a fórmula de mapa | 60 |
| Fuga en casos seleccionados | 60 |
| Diagnósticos derivados | 35 |
| Consistencia estructural, incluidos gramianos repetidos | 67 |
| Ilustraciones | 6 |

Dentro de los 67 controles estructurales hay 49 gramianos de 9 configuraciones
distintas (40 repeticiones), 12 controles de antisimetría y 6 identidades de
Fourier/cuasi-fase. Las identidades no son experimentos independientes de sus
propias definiciones, pero un bug o error flotante puede hacer fallar su
implementación; «no pueden fallar» no se acepta literalmente. Las comprobaciones
de concurrencia y unitariedad son diagnósticos derivados, no nueva evidencia
independiente del mapa. Las colas FFT están registradas sin un assert de cota:
es correcto señalarlo. La cota analítica no depende de ese diagnóstico.

Se confirma O6: el sector R+L antisimétrico es isomorfo al producto de dos
modos distinguibles. El propagador reticular sí es distinto del conteo por
trayectorias; no prueba un efecto de estadística de intercambio. La correcta
incorporación de L_1,L_2 disjuntos se justifica por el orden de operadores de
creación y por que nunca se solapan bajo la misma traslación; no por el
propagador de dos cuerpos. No hay un fallo de signo identificado en los mapas.

La etiqueta «H witness maximum fidelity» debe leerse como el solapamiento de
referencia calculado. El máximo 1/2 para todas las salidas admitidas se prueba
algebraicamente; el código no optimiza sobre protocolos ni ejecuta H mediante U.

## O7: velocidades y límites de alcance

La definición inequívoca sería c_IR=a/tau para las envolventes del nodo 0 en
el límite de momento pequeño y mu=0. Las envolventes alrededor de pi tienen
la misma velocidad de transporte v_env,pi=a/tau tras retirar el portador;
esa igualdad no las convierte en un qubit de baja cuasienergía de un paso.
Si se usa alpha, debe definirse por c_IR=alpha a/tau; aquí alpha=1.

La velocidad de grupo de una partícula sí está determinada por W(k).
Una velocidad de grupo general de excitaciones de muchos cuerpos no se ha
definido ni calculado. Eso es un límite de alcance declarado, no evidencia de
que la igualdad de velocidades libres sea falsa. El resultado computacional
negativo no requiere resolver esa cuestión adicional.

## O8: contraste primario y la observación masiva

Lecturas de esta sesión: `1804.08508v1.pdf` p.3 Ec.(1), Ec.(2), sección 3;
`1711.03920v1.pdf` pp.1–2, Ec.(1), interacción y Ec.(2).
Ambos escriben nu,mu>0 y la fase de interacción de forma local esquemática.
Mu=0 es una extensión continua al borde de la familia de operadores; no se
pueden importar sin más las fórmulas espectrales con divisiones por mu.
El informe ya decía «límite sin masa», pero la salvedad de dominio es útil.

O8(b) acierta en que no se había leído el primer original en la ejecución
anterior. Se ha adquirido y leído ahora. Sin embargo, este original **también**
escribe V_int=exp(i chi n_up(x)n_down(x)), sin producto global explícito, y
restringe su resolución a N=2. No puede invocarse para completar una definición
de Fock global que tampoco muestra en esos pasajes. En nuestro experimento
J=producto_x exp(i chi n_R(x)n_L(x)) es una definición explícita: en el sector
de partículas finitas su fase está bien definida y el argumento de tres
paquetes se deriva directamente de ella, sin importar una solución publicada
de tres cuerpos. Es compatible con la interacción local publicada, no un
teorema de tres cuerpos atribuido al artículo.

Para O8(c), Gamma=sigma_z Pi anticommuta con W para toda mu admisible:
la traslación anticommuta con Pi y la masa sigma_x anticommuta con sigma_z.
Como J es diagonal, la carga segundo-cuantizada Q=dGamma(Gamma) satisface
U†QU=-Q, y N_A se intercambia con N_B (en el sector N fijo).
Esto es correcto. Pero para paquetes de quiralidad fija al inicio,

\[
 Q|_{\rm code}=\sum_i s_i X_i,\qquad
 s_i=+1\ \text{o}\ -1\ \text{según la componente interna}.
\]

No es sum_i X_i en una geometría que contiene R y L. A mu distinto de cero
el código de paquetes con componentes fijas tampoco es invariante.
Contraejemplo de una partícula inicialmente en un sitio par y una componente:
tras un paso <Pi>=mu²-nu²=2mu²-1, que no vale -1 si mu!=0; en cambio
<Gamma> cambia exactamente de signo. El verificador encuentra
||W†Pi W+Pi||=2mu para mu=0,0.2,0.6 y residuo <1.12e-16 para la carga correcta.
No se adopta la inferencia de Claude sobre sum_i X_i ni se abre un gate masivo.

## O9: historia y números

Inspección directa de Git:

- `578f27c`: primera implementación versionada antes de su primera ejecución.
- `19c1608`: corrección de la expectativa +XX a -XX en chi=pi, adición de
  dos controles de paridad y conservación de la salida fallida 225/226.
- `20a78c4`: hash opcional para la nota inicial no versionada; permite reproducir
  el script sin ese fichero contextual. Es la ejecución posterior 228/228.
- `cfeb548`: clasificación de los 228 controles y reparación de presentación;
  no cambio del propagador físico.

Los cuatro valores de la tabla fueron redondeados por exceso a tres cifras
significativas: son techos decimales de los **residuos observados**, no cotas
certificadas del error científico o del cálculo. Son compatibles con el log.
Conviene explicitar el criterio, pero no hay discrepancia numérica.
`contract_commit` es una referencia declarada fija, no un test en tiempo real
del repositorio: así debe etiquetarse. El hash del contrato sí se registra.

## Evidencia reproducible y conclusión

[Script permanente](../scripts/check_thirring_claude_objections.py),
[datos](2026-11-08--thirring-claude-check.json),
[salida](2026-11-08--thirring-claude-check.txt): **28/28**, ejecutados con
Python del entorno `/home/adnac/venvs/torch-gpu`, NumPy. No aleatoriedad.
Las identidades generales provienen de las derivaciones anteriores; las
comprobaciones finitas son contrastes de sus implementaciones. Son del autor,
no una nueva revisión independiente. No se alteró el verificador original.

SHA256 del primer original adquirido:
`3032b33d1375d4a55008aafe1f0e74d228052fa120446694ba8e9ab8e41867ca`.
El JSON conserva las huellas del nuevo script, contrato de auditoría, ambos
PDF y datos originales inspeccionados.

La revisión identifica precisiones reales, especialmente la diferencia entre
universalidad unitaria y complejidad de muestreo, geometría y cuantificadores.
También contiene errores en «todo T», «todo Fock» sin sector, y la carga lógica
del caso masivo. Sus afirmaciones físicas más generales no se deducen del
salto entre nodos. No se ha encontrado un contraejemplo a la colisión completa
ordenada ni a la no-densidad unitaria en el código y recursos declarados.
No se promociona el resultado ni se adopta un PASS global; las reparaciones
aceptadas se distinguen aquí de las afirmaciones del revisor que se rechazan.
