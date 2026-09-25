# Auditoría de atribución IR y comprobación numérica en N=24 y N=40

Registro consolidado de la conversación y ejecuciones del 21–22 de septiembre de 2026.
Base: research/b-infinity-post-s4-gate, commit 2071cea52bf8b0dd2d20b4e1f214b2daf9b4e8fd.
Autorización: el usuario pidió auditar Meyer, comprobar la atribución IR, ejecutar
N=24, después N=40, contrastar mediante evolución directa y finalmente commit y push.
Es una síntesis trazable, no una transcripción literal ni un preregistro retroactivo.
Los contratos exploratorios se fijaron en conversación/cabeceras antes de las
ejecuciones; su primer registro Git se hace ahora, después de observar resultados.

## 1. Pregunta y antecedentes

El punto de partida fue el artículo de Meyer, *From quantum cellular automata
to quantum lattice gases*, https://arxiv.org/html/quant-ph/9604003v2 .
Su no-go escalar en este artículo está formulado en 1D; una descripción anterior
como resultado de este mismo artículo en cualquier red euclídea fue corregida.

De su ecuación (24) se dedujo en la conversación
cos omega(k) = cos rho cos theta cos k + sin rho sin theta.
Para rho=theta fijo en (0,pi/2), c_IR=cos theta<1 mientras el frente estricto es 1:
los bloques extremos satisfacen w_+-^N=(cos^2 theta)^(N-1) w_+- !=0.
Es una deducción de esa familia, revisada por un segundo agente, no una
conclusión atribuida literalmente a Meyer ni una nueva certificación software.
No afecta al contrato específico BCC tridimensional.

CJWW ya aporta el walk (5.15), la cota de velocidades de grupo y colas
exponenciales: https://arxiv.org/html/2408.02108v1 .
Sunada–Tate proporciona antecedentes de asintóticas fuera del soporte del
límite débil: https://arxiv.org/abs/1108.1878 .
La posible novedad debe restringirse al observable operacional regional y
su asintótica específica. No se certificó originalidad bibliográfica completa.

## 2. Qué se está auditando

El resultado plano de Sec. 8.20 se refiere al observable TOTAL del protocolo
homogéneo CJWW, con ley asintótica |C(theta_N)| N^(-13/2) exp(-K_* N).
Aquí se examina una lectura más fuerte: predominio del bloque espectral IR–IR.
No son afirmaciones equivalentes.

Se conserva la familia regional, M=sigma2, M_B=I, Lambda=N^-1 y
P=Pi'=1_{|p|<=N^-1/2}, Q=I-P. El corte móvil forma parte del contrato.
Delta=U|phi><phi|U* - |phi><phi|, [S,P]=0, y

Lpp = tr(E S^N P Delta P S^(-N)),
R = L-Lpp.

R incluye coherencias PQ y QP además de QQ. No se debe llamarlo
automáticamente señal UV. La cota de admisibilidad en norma traza O(N^-1/2)
no controla el error a la escala exponencial de L. Es insuficiencia de esa
cota para una atribución más fuerte, no refutación de la asintótica total.

Para a=(U-I)phi, soporte finito no nulo y P phi=phi:
tr(P Delta P)=-||Qa||^2<0. La positividad estricta sigue de que un polinomio
trigonométrico no nulo no puede anularse en el abierto exterior a la banda.
Así, la compresión no es una diferencia de dos estados normalizados.
Proyectar/normalizar cambia el protocolo y pierde localidad estricta.
Demostrar R=o(|L|) acreditaría predominio bajo esta descomposición, no
automáticamente un protocolo local estrictamente limitado en banda.

Se localizaron dos problemas editoriales en la transcripción ir-corona.md
del commit a3bb725: "no desaparecer en el límite" debe distinguirse de
"no nulo para N grande"; Gamma=B(1) excede la inclusión demostrada si
llenar el interior sólo se apoya numéricamente. No se editó el manuscrito
ni se auditó aquí si versiones posteriores ya los corrigen.

## 3. Reutilización y alcance numérico

Se revisaron verify_regional_laplace_coefficient_gate.py y sus diagnósticos.
No incluían Lpp ni R/L. El antiguo narrow-band gate trata una puerta puntual
diferente; su negativo no decide este protocolo regional.

El diagnóstico nuevo reutiliza los auxiliares del certificado regional,
conservando el verificador original. Añade cuadratura sobre momentos REALES
para la proyección: no se puede insertar sin justificación la máscara abrupta
IR en el contorno complejo inclinado. Se conservan todos los sitios con
perfil no nulo y se incluyen los términos cuadráticos de la señal.

r=S^N phi, d=S^N(U-I)phi, dP=P d:
L=2 Re<r,E d>+<d,E d>,
Lpp=2 Re<r,E dP>+<dP,E dP>.

Resoluciones (radial,polar,azimutal): (12,16,32), (18,24,48), (24,32,64).
Criterio EMPÍRICO fijado: último cambio de Lpp < 1e-3 |L| y
diferencia entre FFT inclinada y no inclinada < 1e-3 |L|.
No es una cota rigurosa ni una prueba de convergencia asintótica.

La versión inicial N=24 se conserva byte por byte, incluida su salida
registrada. La copia aportada por el usuario tenía SHA256
8c448d9c73db6aecfa8c5db1aff206f790ad5a2559f1ed56a88cd908baaa7a79;
se verificó antes de ejecutar N=40. Añadía N por argv y

A_L=2 sum_y F_y |r_y^dagger d_y| + sum_y F_y ||d_y||^2,
kappa_sum=A_L/|L|.

Esta agrupación no mide errores ya presentes en el campo ni cancelaciones
entre componentes dentro de r_y^dagger d_y. Una kappa pequeña no localiza
la cancelación espectral en cada sitio ni indica un problema de FFT.

## 4. Resultados observados

| Magnitud | N=24 | N=40 |
| --- | ---: | ---: |
| L | -3.768512636646024e-12 | -1.2441072898797711e-14 |
| Lpp | -3.807990219362049e-7 | +2.6839421188805568e-8 |
| R/L | -101046.564026511 | +2157324.6815772774 |
| último cambio Lpp / abs(L) | 1.1800207142313945e-9 | 4.2472460341417844e-7 |
| diferencia FFT absoluta | 3.2701785801652672e-21 | 4.251919610206146e-21 |
| criterio empírico | true | true |

En N=40, el primer refinamiento de Lpp cambia 0.1859093481 |L|; sólo el
último satisface el umbral. kappa_sum_L=1.4264936646595356.
La reproducción externa aportada por el usuario informó kappa~1.31 en N=24;
ese dato no tiene aquí una salida local retenida y se distingue de la tabla.

Dos puntos no establecen tendencia. El cambio de signo y magnitud se registra
sin ajuste ni extrapolación. El bloque PP y el residuo casi se cancelan en
ambos puntos; ninguno de estos resultados acredita origen exclusivamente UV.

## 5. Comparación independiente del algoritmo FFT

Se inspeccionó el código de nivel superior de verify_signaling_witness.py
y verify_directional_saturation.py: asignaciones, importaciones, derivaciones
SymPy y registro de checks; los main no se ejecutan al importar.
No basta buscar el guard __main__ para justificar esta revisión.

exact_blocks() devuelve dict[tuple[int,int,int], matriz SymPy 2x2] de W_h,
con W(p)=sum_h W_h exp(i p.h). Para estados:
S_d=W_{-d}^dagger, desplazamiento x->x+d.
La comparación simbólica exacta mediante Laurent reconstruyó la W escrita
en el diagnóstico: PASS, 14 bloques.

Se aplicaron 40 pasos locales numéricos en caja NO periódica, sin FFT,
recurrencia de Chebyshev ni recortes de amplitud. La caja contiene el soporte
alcanzable completo: 99^3, pues las superficies de perfil cero no se almacenan.
No se trunca el recurso extendido: sólo se evoluciona la perturbación compacta.

| Comparación con FFT inclinada, N=40 | Valor |
| --- | ---: |
| max abs(d_direct-d) | 7.080991422964771e-26 |
| max abs(d_direct-d) / max abs(d) | 1.6156975277079201e-15 |
| L_direct | -1.2441072898797717e-14 |
| abs(L_direct-L) | 6.310887241768095e-30 |
| abs(L_direct-L)/abs(L) | 5.072622990882056e-16 |

Es independencia algorítmica, no independencia de la definición física:
se comparte W, la fuente y la cuadratura de r. La métrica del campo es
normalizada por su máximo, no un error relativo uniforme por sitio.
El acuerdo refuerza L; no certifica Lpp ni reemplaza su control por cuadratura.
Todos los campos preexistentes de las tres filas y del resumen N=40
coinciden exactamente con la salida anterior al añadir la opción directa.

## 6. Reproducir desde la raíz del repositorio

Dependencias de las ejecuciones retenidas: Python 3.12.14, NumPy 2.3.5.
La opción directa utilizó SymPy 1.14.0 y mpmath 1.3.0; se instalaron en el
entorno de trabajo porque faltaban. No se alteró requirements.txt del repo.
El entorno histórico fijado del repositorio no es idéntico: se requiere
reproducción local antes de tratar cambios entre entornos como física.

~~~bash
OPENBLAS_NUM_THREADS=1 python -B scripts/ir_precision_N24.py
OPENBLAS_NUM_THREADS=1 python -B scripts/ir_cancellation.py 24
OPENBLAS_NUM_THREADS=1 python -B scripts/ir_cancellation.py 40
OPENBLAS_NUM_THREADS=1 python -B scripts/ir_cancellation.py 40 --direct --scripts-dir scripts
~~~

La opción directa es explícita; el comportamiento numérico por defecto
permanece igual. No se ejecutó una nueva serie de N ni se ajustó una ley.

Salidas originales:
- [N24](ir-spectral-audit/out_canc_N24.jsonl)
- [N40](ir-spectral-audit/out_canc_N40.jsonl)
- [N40 directo](ir-spectral-audit/out_canc_N40_direct.jsonl)

## 7. Estado y límites

SUPPORTED / FINITE_N_NUMERICAL_DIAGNOSTIC.
No es un nuevo PASS del teorema plano, ni una refutación de ese teorema.
La atribución exclusiva o asintóticamente dominante al bloque PP sigue OPEN.
La auditoría completa del remainder y la originalidad completa siguen fuera
de lo certificado por estas ejecuciones. H1c, E0 y la extensión AdS conservan
sus estados previos; los proyectores espectrales IR de este informe no se
confunden con los proyectores de Riesz del frente H1.

El siguiente paso científico requiere una decisión: no se lanza por este
commit una serie mayor, ni se publica el manuscrito. Las correcciones de
interpretación de esta conversación se conservan en este informe.

## 8. Integridad de artefactos

SHA256 antes del commit:

| Archivo | SHA256 |
| --- | --- |
| ir_precision_N24.py | bb607b1b7a1f95a6a8f64c77734c587306d6ef97d7dfe6c28b6842113fba2665 |
| ir_cancellation.py | ebc5a4afba1fcf4e7cf5311289b1655adc05aee29886266ea56253db245a496b |
| ir_precision_N24_output.txt | 13a49ae54dccb8d83b1fba570a22aa35ce5fa6f4d55227c3a7a5c48bb11474af |
| out_canc_N40.jsonl | d100e60141b3c542ef1db959669fbb6b3651b06c8184a3843ebb03dccc2bdec3 |
| out_canc_N40_direct.jsonl | dcf2732f258f4fe64e17d10f515118f5eeaec162ae445334eebea8651de15e48 |
