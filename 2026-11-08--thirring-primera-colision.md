# Primera colisión del QCA de Thirring: obstrucción para una codificación en un solo sector de momentos

Fecha: 8 de noviembre de 2026. Estado: exploración analítica con comprobación numérica; sin revisión independiente.

## Pregunta y criterio

¿Puede la extensión mínima del Dirac 1D mediante una fase de contacto producir una puerta entrelazante entre dos qubits, con error y salida de la codificación arbitrariamente pequeños, manteniendo ambas partículas alrededor de \(k=0\)?

Se analiza exclusivamente el QCA fermiónico de Thirring con interacción en el mismo sitio. Es un modelo publicado, no una construcción nueva. Se abandonaría esta codificación si el efecto de la interacción exigiese una salida persistente del sector elegido.

**Resultado:** una simetría exacta obliga a que todo cambio inducido por la interacción dentro del sector próximo a cero tenga una componente de igual norma en el sector donde ambos momentos están próximos a \(\pi\). Una colisión explícita reproduce esta obstrucción. El resultado descarta el criterio anterior para este candidato; no establece una imposibilidad general de universalidad computacional con emergencia relativista.

## Modelo y relación con el trabajo existente

La revisión se ancla al repositorio [qca-causal-cones](https://github.com/nacho09021973/qca-causal-cones), commit `bce55999a909cebe1a39b2a86a0ae37b5aecda38`. El punto de partida es su bloque Dirac 1D, relacionado por convenciones de base y orientación con

\[
W(k)=
\begin{pmatrix}
\nu e^{ik}&-i\mu\\
-i\mu&\nu e^{-ik}
\end{pmatrix},\qquad \nu^2+\mu^2=1.
\]

Aquí \(\mu\) es un parámetro de masa adimensional. El régimen continuo masivo requiere escalar conjuntamente momento, masa y paso temporal; el argumento siguiente no depende de esa aproximación.

En el sector de dos fermiones:

\[
F=(W\otimes W)|_{\wedge^2\mathcal H},\qquad
J=e^{i\chi C},\qquad U=FJ,
\]

donde \(C\) proyecta sobre coincidencia espacial con componentes internas opuestas. Se aplica primero la fase y después el paso libre. En Fock, corresponde a \(J=\prod_x e^{i\chi n_R(x)n_L(x)}\). La interacción es identidad con una sola partícula, por lo que conserva exactamente su dinámica libre.

La definición del modelo se encuentra en [1, ecuaciones 1–2]. La separación en un subespacio que interacciona y otro libre ya está publicada en [2, ecuación 8 y páginas 5–6]. La consecuencia cuantitativa para una codificación restringida se desarrolla abajo. No se afirma originalidad de este resultado.

## Una colisión con dos qubits definidos

Tomemos \(\mu=0\): una componente avanza una celda a la derecha y la otra a la izquierda por paso. Elegimos la orientación espacial de modo que se llamen \(R\) y \(L\), respectivamente.

Cada qubit ocupa uno de dos paquetes espaciales disjuntos de una misma componente. Para un entero \(M\geq1\),

\[
f_s(x)=\frac{1}{\sqrt{2M}}\,
\mathbf 1_{\{s,\ldots,s+2M-1\}}(x).
\]

Los cuatro estados lógicos son

\[
|ab\rangle=
c_R^\dagger(f_{r_a})c_L^\dagger(f_{l_b})|\mathrm{vac}\rangle,
\]

con \(r_0=-12M,\ r_1=-4M,\ l_0=12M,\ l_1=4M\). Se mantiene ese orden de operadores de creación, de modo que no se introduce una fase artificial al intercambiar el orden espacial de los paquetes. Son dos qubits en modos, con número total fijo de partículas.

Leemos el resultado tras \(T=5M\) pasos y descontamos matemáticamente la traslación libre. Hasta ese momento solo la rama \(11\) puede haber colisionado. Sus componentes con separación inicial par coinciden en un sitio; las impares se cruzan entre sitios y no sienten la interacción.

Definiendo \((\Pi f)(x)=(-1)^x f(x)\), el operador sobre la rama \(11\), una vez completado su cruce, es

\[
S_\chi=aI+b\,\Pi_R\Pi_L,\qquad
a=\frac{1+e^{i\chi}}2,\quad b=\frac{e^{i\chi}-1}2.
\]

Como los paquetes tienen longitud par, \(\langle f_s,\Pi f_s\rangle=0\). La segunda componente queda fuera de los cuatro modos lógicos. Por tanto, la compresión de la evolución a la codificación original es exactamente

\[
\boxed{K_\chi=\operatorname{diag}(1,1,1,a)}
\]

y la máxima probabilidad de salida, alcanzada con entrada \(11\), es

\[
\boxed{p_{\mathrm{salida,max}}=\sin^2(\chi/2).}
\]

| Fase de contacto | Amplitud retenida de \(11\) | Probabilidad de salida para \(11\) |
|---|---|---|
| \(0\) | \(1\) | \(0\) |
| \(\pi/2\) | \((1+i)/2\) | \(1/2\) |
| \(\pi\) | \(0\) | \(1\) |

Para una entrada general, la probabilidad de salida es \(|\alpha_{11}|^2\sin^2(\chi/2)\); en particular, para \(++\) es la cuarta parte del máximo. No debe interpretarse el 50 % como una pérdida común a todas las entradas.

El mapa comprimido no es unitario cuando la interacción tiene efecto. En particular, \(\chi=\pi\) no implementa una puerta CZ en esta codificación. La postselección tendría un análisis diferente.

Estos paquetes tienen soporte espacial finito y no son estrictamente limitados en momento. Al crecer \(M\), su distribución de momento se concentra en cualquier entorno fijo de cero, mientras que la de \(\Pi f_s\) se concentra en torno a \(\pi\), módulo \(2\pi\). La salida calculada no disminuye con \(M\).

## Prueba general: incluye masa y cualquier tiempo finito

Sea \(\mathcal H=\ell^2(\mathbb Z)\otimes\mathbb C^2\) y definamos

\[
(Zf)(x)=(-1)^x\sigma_zf(x),\qquad Q=Z\otimes Z.
\]

La traslación cambia la paridad espacial; el término de masa cambia la componente interna. En ambos casos se obtiene

\[
WZ=-ZW,\qquad [F,Q]=0.
\]

En contacto, las dos componentes internas son opuestas y \(Q=-1\). Así, \(J\) conmuta con \(Q\) y actúa como identidad en \(P_+=(I+Q)/2\). El proyector \(P_-=(I-Q)/2\) coincide con el proyector de la ecuación 8 de [2], escrito en otras coordenadas.

Descontando la evolución libre mediante \(M_t=F^{-t}U^t\), tenemos

\[
[M_t,Q]=0,\qquad M_tP_+=P_+.
\]

Por consiguiente, para cualquier estado \(\psi\),

\[
\delta=(M_t-I)\psi\quad\Longrightarrow\quad Q\delta=-\delta.
\]

Sea \(P_0\) el proyector que restringe **ambos** momentos a \(|k|\leq\Lambda<\pi/2\), conservando las dos componentes internas. El proyector

\[
P_\pi=QP_0Q
\]

restringe ambos momentos al entorno trasladado de \(\pi\). Los dos subespacios son ortogonales. Para \(\psi=P_0\psi\),

\[
P_\pi M_t\psi
=P_\pi\delta
=QP_0Q\delta
=-QP_0\delta.
\]

Como \(Q\) es unitario,

\[
\boxed{\|P_\pi M_t\psi\|^2
=\|P_0(M_t-I)\psi\|^2.}
\]

Esta es una identidad exacta, no una estimación asintótica. La fuga total fuera de \(P_0\) es al menos el miembro izquierdo. Además, \(F\) conserva ambos sectores de momento, de modo que las probabilidades son las mismas antes y después de descontar la evolución libre.

Si la fuga total es como máximo \(\varepsilon^2\) para todas las entradas normalizadas de un código contenido en \(P_0\), entonces

\[
\|P_0(M_t-I)\psi\|\leq\varepsilon.
\]

Hacer que la fuga tienda a cero fuerza a que la acción de la interacción dentro del sector tienda a la identidad. Por tanto, no puede converger a una puerta entrelazante fija distinta de la evolución libre bajo estas hipótesis.

Para paquetes aproximadamente contenidos en \(P_0\), con
\(\eta=\|(I-P_0)\psi\|\), la misma demostración y la desigualdad triangular dan

\[
\|P_0(M_t-I)\psi\|
\leq \|P_\pi M_t\psi\|+3\eta.
\]

La obstrucción persiste cuando la contaminación inicial del otro sector tiende a cero.

## Comprobación realizada

Se contrastó la identidad en un anillo de 32 sitios, en el espacio antisimétrico de dos fermiones, con 11 pasos, masas \(\mu=0,0.2,0.6\) y fases \(\chi=0,0.7,\pi\). Se usó una entrada aleatoria normalizada y proyectada a \(|k|<0.6\), con semilla fija. También se comprobaron unitariedad, anticomutación, antisimetría y norma.

El mayor residuo observado fue \(2.53\times10^{-15}\). La colisión de los paquetes se verificó por evolución directa de sus trayectorias para \(M=1,2,8,32\) y \(\chi=0,0.7,\pi/2,\pi\); el mayor residuo fue \(2.21\times10^{-15}\).

Los números verifican la implementación de las identidades en esos casos. La conclusión para todos los parámetros cubiertos procede del argumento algebraico, no de extrapolar estas pruebas.

## Alcance físico y decisión

Se cierra negativamente esta primera prueba: contacto en el mismo sitio, dos fermiones, codificación en torno a un solo nodo y puerta determinista con fuga arbitrariamente pequeña.

El entorno de \(\pi\) puede representar otro sector relativista de la dinámica de Floquet. Salir de \(k\approx0\) no equivale por sí solo a perder toda interpretación relativista ni a producir energía física arbitrariamente alta. La prueba utiliza una restricción explícita de la codificación.

Quedan fuera del resultado codificaciones que incluyan ambos nodos, otras interacciones, partículas auxiliares, medidas y controles adicionales. Tampoco se demuestra ni se refuta aquí la universalidad computacional del QCA completo. No se deduce el valor de \(c\) ni una frecuencia absoluta de reloj.

Si se continúa con este mismo modelo, la siguiente pregunta delimitada es si ambos nodos pueden incorporarse a la codificación y proporcionar operaciones componibles. Eso requeriría otra prueba; no queda establecido por esta colisión.

## Fuentes y trazabilidad

1. A. Bisio, G. M. D'Ariano, P. Perinotti y A. Tosini, *The Thirring quantum cellular automaton*, Physical Review A 97, 032132 (2018). [arXiv:1711.03920](https://arxiv.org/abs/1711.03920), ecuaciones 1–2 para el paso libre y el sector de dos partículas.
2. A. Bisio, G. M. D'Ariano, N. Mosco, P. Perinotti y A. Tosini, *Solutions of a two-particle interacting quantum walk*, Entropy 20, 435 (2018). [arXiv:1804.08508](https://arxiv.org/abs/1804.08508). PDF consultado, versión de 24 de abril de 2018: página 3, ecuación 1; página 5, ecuación 8; página 6, descripción del subespacio libre.
3. Repositorio de partida: [informe Dirac/Weyl en el commit revisado](https://github.com/nacho09021973/qca-causal-cones/blob/bce55999a909cebe1a39b2a86a0ae37b5aecda38/reports/2026-09-14--weyl-dirac-exact-gate.md). Esta nota no modifica el estado ni certifica un nuevo resultado del repositorio.

## Apéndice reproducible

Python 3 con NumPy. El primer bloque simula directamente las trayectorias de los paquetes; el segundo representa los estados antisimétricos como matrices de amplitudes. No requiere descargar datos.

```python
import numpy as np

def collision_check(M, chi):
    offsets = np.arange(2*M)
    starts_R, starts_L, T = (-12*M, -4*M), (12*M, 4*M), 5*M
    kept, leaked = [], []
    for a in range(2):
        for b in range(2):
            x = starts_R[a] + offsets[:, None]
            y = starts_L[b] + offsets[None, :]
            amplitude = np.ones((2*M, 2*M), dtype=complex)/(2*M)
            for t in range(T):
                amplitude *= np.where(x+t == y-t, np.exp(1j*chi), 1)
            overlap = amplitude.sum()/(2*M)
            kept.append(overlap)
            leaked.append(np.linalg.norm(amplitude - overlap/(2*M))**2)
    expected = np.array([1,1,1,(1+np.exp(1j*chi))/2])
    expected_leak = np.array([0,0,0,np.sin(chi/2)**2])
    return max(np.max(np.abs(kept-expected)),
               np.max(np.abs(leaked-expected_leak)))

L, steps = 32, 11
d = 2*L
x = np.arange(L)
k = 2*np.pi*np.fft.fftfreq(L)
B = np.exp(1j*np.outer(x,k))/np.sqrt(L)
Psmall = B[:, np.abs(k)<0.6] @ B[:, np.abs(k)<0.6].conj().T
P0 = np.kron(Psmall,np.eye(2))
z = ((-1.0)**x[:,None]*np.array([1.,-1.])).reshape(-1)
Z = np.diag(z)
Ppi = Z@P0@Z
modes = np.arange(d)
contact = (modes[:,None]//2 == modes[None,:]//2) & (
    modes[:,None]%2 != modes[None,:]%2)
rng = np.random.default_rng(20261108)
A = rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
A = P0@(A-A.T)@P0.T
A /= np.linalg.norm(A)
residuals = []

for mass in (0.,0.2,0.6):
    speed = np.sqrt(1-mass**2)
    W = np.zeros((d,d),complex)
    for site in range(L):
        W[2*((site+1)%L),2*site] = speed
        W[2*((site-1)%L)+1,2*site+1] = speed
        W[2*site+1,2*site] = -1j*mass
        W[2*site,2*site+1] = -1j*mass
    residuals.extend((np.linalg.norm(W.conj().T@W-np.eye(d)),
                      np.linalg.norm(W@Z+Z@W)))
    for chi in (0.,0.7,np.pi):
        phase = np.where(contact,np.exp(1j*chi),1)
        out = A.copy()
        for _ in range(steps):
            out = W@(phase*out)@W.T
        for _ in range(steps):
            out = W.conj().T@out@W.conj()
        change = out-A
        lo = P0@change@P0.T
        hi = Ppi@out@Ppi.T
        residuals.extend((np.linalg.norm(hi+z[:,None]*lo*z[None,:]),
                          np.linalg.norm(z[:,None]*change*z[None,:]+change),
                          np.linalg.norm(out+out.T), abs(np.linalg.norm(out)-1)))
        print(f"mu={mass:.1f} chi={chi:.8f} "
              f"low_change2={np.linalg.norm(lo)**2:.12g} "
              f"pi_probability={np.linalg.norm(hi)**2:.12g}")
collision_residual = max(collision_check(M,chi)
    for M in (1,2,8,32) for chi in (0.,0.7,np.pi/2,np.pi))
max_residual = max(residuals)
print("identity_residual_max =",max_residual)
print("timebin_gate_residual_max =",collision_residual)
assert max_residual < 1e-12
assert collision_residual < 1e-12
```

