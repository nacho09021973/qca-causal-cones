<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 16568209771dc898346bd4af0c78ec10530c3b9e; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 91bee96b008d707188487ad26871460296ba02cf99300ae272afd81dce1d64e6; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=enabled, reasoning_effort=low, max_tokens=32768, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 f60d4670d572e2f2dc66fbb87f072dd5a4861bca5d9c1c2a70c8801356c405bd
inicio: 2026-10-26T13:35:30Z  fin: 2026-10-26T13:43:10Z
documento: /home/ignac/qca-causal-cones/theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md ; último commit observado: 1ece734 ; sha256 de la copia enviada 9f823adb673f27cafc2fa90cb8c272c108e4d2af244f027a2aae2508687b5103
documento: /home/ignac/qca-causal-cones/reports/2026-10-26--w4-spectrum-audit.md ; último commit observado: 85e22e0 ; sha256 de la copia enviada 3adf31558c63c5d74a8ea3470e560efad9de6effcbd0e3cd20ae9da2325f6656
documento: /home/ignac/qca-causal-cones/scripts/verify_w4_long_wavelength_spectrum.py ; último commit observado: 85e22e0 ; sha256 de la copia enviada f6a6b8d4480b2144e30737a5861eabbbfcd32a3b5a2194564315e048286b1d50
documento: /home/ignac/qca-causal-cones/scripts/verify_w4_spectrum_observables.py ; último commit observado: 85e22e0 ; sha256 de la copia enviada 4bb140f6becb187c978639612ab36d28eadcf266f577b1c5512bc0c4537c489a
documento: /home/ignac/qca-causal-cones/scripts/certificate_utils.py ; último commit observado: cb1e038 ; sha256 de la copia enviada 5a3591e1c5351aedbea97ec65f4cdcffacfb4117f52bc983d550ba67feb270ba
documento: /home/ignac/qca-causal-cones/scripts/requirements.txt ; último commit observado: 90a56d2 ; sha256 de la copia enviada 03c88ea0349bff39d3d162f942aed8f7929e8e5021fe46cf603ac31d85ac8aa0
entrada_deepseek.txt sha256 c381322ed9d1b54e4b03bf257509afd1a8e7d33ca8300b0ddf2369790605d35e
respuesta sha256 6c1069f4d0b08076ff04815719a0f90489fb2aa45e2b5c1cfd003e5dadb2c2b4
-->

## Veredicto global

**ACCEPT_WITH_REPAIRS**

Las correcciones de la auditoría W4 están, en lo esencial, **justificadas**: la fase de sector debe conservarse para referir las cuasienergías al vacío; la rama uniforme del caso de igual signo es cuadrática en \(k=0\), no lineal; el control de signos opuestos es lineal en \(k=0\); las unidades de velocidad requieren el factor dos por celda de dos registros; y el observable \(Z_n\) no es cerrado por densidad ni detecta la fase relativa vacío-defecto.

Las reparaciones pendientes son de **presentación, cobertura y separación de evidencia**, no alteran las fórmulas. No encuentro un error de cálculo que invalide el informe.

---

## Punto 1 — Restricción de \(K(\kappa)\), vacío y producto de matchings

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | \(K(\kappa)=e^{-i\kappa}(\cos\kappa I+i\sin\kappa\,\mathrm{SWAP})\). En \(\{\ket{01},\ket{10}\}\) queda \(e^{-i\kappa}\begin{pmatrix}c&is\\ is&c\end{pmatrix}\), con \(c=\cos\kappa\), \(s=\sin\kappa\). El vacío \(\ket{00}\) y todo par idéntico quedan fijos. Para dos capas, \(U_{\sigma,\mathrm{full}}(k)=e^{-i(1+\sigma)\kappa}B_\sigma A\), con \(\frac12\operatorname{tr}(B_\sigma A)=c^2-\sigma s^2\cos k\), \(\det(B_\sigma A)=1\), \(\det U_{\sigma,\mathrm{full}}=e^{-2i(1+\sigma)\kappa}\). El circuito `ring_step` construye cada enlace mediante `stay*I + hop*SWAP`, con `stay=e^{-i\alpha}\cos\alpha`, `hop=i e^{-i\alpha}\sin\alpha`; esto reproduce exactamente la puerta microscópica y, al proyectar al sector de un defecto, coincide con el símbolo 2×2. |
| Objeción | **W4-R1-01**, gravedad **baja/informativa**: `verify_w4_spectrum_observables.py` importa `bloch_step` desde `verify_w4_long_wavelength_spectrum.py` para construir la comparación esperada. La construcción real-space es separada, pero la comparación no es una revisión independiente; un error correlacionado entre ambas convenciones de capas no sería detectado. |
| Reparación mínima | Declarar explícitamente, como ya hace el texto, que el anillo es una segunda formulación del autor, no una revisión independiente. No es necesario alterar los certificados. |

---

## Punto 2 — Autovalores, convención \(e^{-i\epsilon}\), fase de sector y observables

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | Para \(\sigma=+1\), los autovalores del bloque sin fase \(B_+A\) son \(e^{\pm i\omega_+}\), con \(\cos\omega_+=c^2-s^2\cos k\). El paso completo es \(e^{-2i\kappa}B_+A\). Con \(e^{-i\epsilon}\) se obtienen las ramas \(\epsilon=2\kappa\mp\omega_+\). En \(k=0\), \((1,1)\) tiene autovalor \(1\), es decir \(\epsilon=0\); \((1,-1)\) tiene \(e^{-4i\kappa}\), es decir \(\epsilon=4\kappa\) módulo \(2\pi\). En \(k=\pi\), el paso completo es \(e^{-2i\kappa}I\), de modo que el cruce está centrado en \(\epsilon=2\kappa\) módulo \(2\pi\), no en cero relativo al vacío para \(0<\kappa<\pi/2\). La fase \(e^{-2i\kappa}\) es global dentro del sector de un defecto, pero no respecto al vacío; \(Z\) no conecta ambos sectores, por lo que no ve esa fase relativa. |
| Objeción | **W4-R1-02**, gravedad **baja**: la caracterización de la rama cuadrática con coeficiente \(\tan(\kappa)/4\) se enuncia solo para \(0<\kappa<\pi/2\). Para \(\kappa\in(\pi/2,\pi)\), la misma derivación de función implícita sigue siendo válida mientras \(\sin(2\kappa)\neq 0\), pero el coeficiente cambia de signo y la elección de rama \(\omega_+(0)=2\kappa\) debe manejarse módulo \(2\pi\). El documento no generaliza incorrectamente, pero conviene dejarlo explícito. |
| Reparación mínima | Añadir una frase en §3: “Para \(\kappa\in(\pi/2,\pi)\) la rama local existe con el mismo argumento, pero la elección de rama de \(\omega_+\) y el signo del coeficiente no se extrapolan desde el intervalo \(0<\kappa<\pi/2\).” |

---

## Punto 3 — Rama uniforme del mismo signo y extremos

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | Con \(F(\epsilon,k)=\cos(2\kappa-\epsilon)-(c^2-s^2\cos k)\), se cumple \(F(0,0)=0\), \(F_\epsilon(0,0)=\sin(2\kappa)\neq 0\), \(F_k(0,0)=0\), \(F_{kk}(0,0)=-s^2\). El teorema de la función implícita da una rama analítica par; la ecuación \(\epsilon''=-F_{kk}/F_\epsilon\) produce \(\epsilon''=\tan(\kappa)/2\), por tanto \(\epsilon_{\mathrm{unif}}(k)=\frac{\tan\kappa}{4}k^2+O(k^4)\). Es correcto. En \(\kappa=0,\pi\) el paso es identidad; en \(\kappa=\pi/2\) es \(e^{-i\kappa}\cdot\mathrm{SWAP}\) por capa y el paso completo da \(\operatorname{diag}(e^{-ik},e^{ik})\), con ramas lineales, no extrapolables desde \(\kappa<\pi/2\). |
| Objeción | **W4-R1-03**, gravedad **informativa**: la expresión histórica `SMOOTH_MODE_GAPPED` puede confundir “no gap espectral” con “no linealidad”. Existe una rama con \(\epsilon(0)=0\); por tanto no hay un gap de energía estricto respecto al vacío. Lo que está ausente es una dispersión lineal suave en \(k=0\). La auditoría lo corrige, pero conviene usar “modo suave cuadrático” y no “gapped” sin matiz. |
| Reparación mínima | Sustituir en el resumen “gapped” por “sin modo lineal suave” o añadir “aunque \(\epsilon(0)=0\), la rama no es lineal”. |

---

## Punto 4 — Control de signos opuestos y cruce en \(k=\pi\)

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | Para \(\sigma=-1\), \(\frac12\operatorname{tr}(B_-A)=c^2+s^2\cos k\). Entonces \(\sin^2(\omega_-/2)=s^2\sin^2(k/2)\), de donde \(\omega_-(k)=2\arcsin(|s||\sin(k/2)|)=|s||k|+O(|k|^3)\). La expansión del script es correcta: término cúbico \(v(v^2-1)k^3/24\) con \(v=|s|\). Para el caso original \(\sigma=+1\) cerca de \(k=\pi\), con \(q=k-\pi\), la traza da \(\sin^2(\omega_+/2)=s^2\sin^2(q/2)\), con \(\omega_+\approx|s||q|\) y separación entre las dos ramas \(2|s||q|+O(|q|^3)\). La pendiente no nula requiere \(s\neq0\). |
| Objeción | Ninguna de cálculo. Como limitación de verificación permanente, el testigo finito cubre \(\kappa\in\{0,\pi/4,\pi/2\}\) y \(L\in\{4,6\}\); el argumento general está en el texto y en el script simbólico, no en el anillo. |
| Reparación mínima | No se requiere. |

---

## Punto 5 — Unidades: espaciado \(a\), período \(\tau\), factor dos

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | Con celda de dos registros, la longitud de celda es \(2a\), de modo que \(k=2ap\). La frecuencia física es \(\epsilon/\tau\). Por regla de la cadena, \(v_{\mathrm{grp}}=(2a/\tau)\,d\epsilon/dk\). Para el control lineal, \(\epsilon\approx|s||k|\), luego la velocidad en registros por paso completo es \(2a|s|/\tau\), equivalente a \(2|s|\) registros por paso completo. En \(\kappa=\pi/2\), \(\mathrm{SWAP}\) desplaza exactamente dos registros por paso completo: \(A_m\to A_{m+1}\) y \(B_m\to B_{m-1}\). El script verifica exactamente esos desplazamientos orientados para \(L=4,6\). |
| Objeción | Ninguna. La separación entre pendiente IR, velocidad máxima de grupo y soporte causal está correctamente declarada como no igualdad general. |
| Reparación mínima | No se requiere. |

---

## Punto 6 — Observable \(Z_n\), ejemplos y alcance

| Campo | Contenido |
|---|---|
| Resultado | **PASS** |
| Derivación comprobada | En vacío más un defecto, \(Z_n\) es diagonal con \(+1\) salvo \(-1\) si el defecto está en \(n\). Para amplitudes \(b\), \(\langle Z_n\rangle=1-2|b_n|^2/\|b\|^2\). El ejemplo \(k=\pi\) con \(\psi_n=(-1)^{\lfloor n/2\rfloor}/2\) produce \(\langle Z_n\rangle=1/2\) uniforme y es autoestado en \(\kappa=\pi/4\) para ambos signos; por tanto \(k=\pi\) no fuerza \(Z\) alternante. La mezcla \(\ket{\mathrm{vac}}+\epsilon\ket{\psi}\) da respuesta de orden \(\epsilon^2\) con derivada primera nula. Los estados de enlace \((1,\pm i)/\sqrt2\) tienen el mismo \(Z\) inicial y \(Z\) posterior opuesto, tanto tras un enlace como tras el paso completo \(L=4\); luego la densidad no es una variable dinámica cerrada. |
| Objeción | Ninguna de fondo. El texto distingue correctamente que esto no es un no-go universal para ondas del métrico ni para otros fondos/observables. |
| Reparación mínima | No se requiere. Podría añadirse una frase recordando que el no-cierre vale para la actualización cerrada de \(Z\) desde perfiles de \(Z\), no para la evolución unitaria subyacente. |

---

## Punto 7 — Verificaciones permanentes, circularidad, cobertura, helper

| Campo | Contenido |
|---|---|
| Resultado | **PASS_WITH_REPAIRS** |
| Derivación comprobada | `verify_w4_long_wavelength_spectrum.py` comprueba simbólicamente la puerta, las trazas, los determinantes, la rama cuadrática, el control lineal y los extremos. `verify_w4_spectrum_observables.py` construye circuitos de \(2^L\) estados desde permutaciones de bits para \(L=4,6\) y los proyecta al sector de un defecto; verifica unitariedad, vacío, sector, acuerdos Bloch/real-space y desplazamientos SWAP. Los dos certificados usan el mismo ayudante `assert_sym_equal`, que normaliza con `rewrite(exp)` y `simplify`. |
| Objeción | **W4-R1-01** ya citada: dependencia entre scripts. **W4-R1-04**, gravedad **baja**: ambos scripts confían en `certificate_utils`; un fallo sistemático del normalizador simbólico no sería detectado por una vía alternativa. **W4-R1-05**, gravedad **baja**: la cobertura finita es exacta pero puntual; no sustituye el argumento analítico. El texto declara correctamente que no es revisión independiente ni extrapolación. |
| Reparación mínima | Para W4-R1-04, añadir un control alternativo de igualdad algebraica, por ejemplo evaluar simbólicamente en puntos no triviales o usar `simplify(expr)` directamente en al menos un bloque. Para W4-R1-05, conservar la frase ya presente de que los anillos son testigos finitos, no prueba por extrapolación. No hay que modificar resultados. |

---

## Lista final de objeciones

| ID | Gravedad | Referencia concreta | Reparación mínima |
|---|---:|---|---|
| W4-R1-01 | Baja/informativa | `verify_w4_spectrum_observables.py` importa `bloch_step` desde `verify_w4_long_wavelength_spectrum.py`; comparación no independiente | Declarar que es una segunda formulación del autor, no revisión independiente; ya se declara en el informe, pero conviene repetirlo en el encabezado del script |
| W4-R1-02 | Baja | Documento 2 §3: dominio \(0<\kappa<\pi/2\) para la rama cuadrática | Añadir que para \(\kappa\in(\pi/2,\pi)\) la rama local sigue existiendo por función implícita, pero no se extrapola el signo ni la elección de rama |
| W4-R1-03 | Informativa | Documento 2 §1 y §3: uso heredado de `SMOOTH_MODE_GAPPED` | Sustituir por “modo suave cuadrático; \(\epsilon(0)=0\) y no lineal” para evitar confundir gap espectral con no linealidad |
| W4-R1-04 | Baja | `certificate_utils.py`; `verify_w4_long_wavelength_spectrum.py` y `verify_w4_spectrum_observables.py` dependen del mismo `assert_sym_equal` | Añadir una comprobación alternativa de igualdad simbólica en al menos un bloque para no depender exclusivamente del normalizador |
| W4-R1-05 | Baja | `verify_w4_spectrum_observables.py`, cobertura finita \(L=4,6\), \(\kappa=0,\pi/4,\pi/2\) | Mantener y reforzar la frase de que los anillos son testigos exactos, no extrapolación ni revisión independiente |

No se ha encontrado ningún error algebraico que invalide las correcciones de fase, ramas, unidades u observable de la auditoría W4. Las objeciones anteriores son de robustez y presentación; no cambian el estatus científico de las derivaciones.
