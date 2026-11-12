<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 83c04f9d6b3c9aaa2a45511cd36f568c75b922cf; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: stop (estado operativo, no validación del contenido)
modelo: deepseek-v4-pro, esfuerzo: thinking=por defecto de la API, reasoning_effort=por defecto de la API, max_tokens=393216, vía: API api.deepseek.com/chat/completions, sin herramientas
modelo devuelto por API: deepseek-v4-pro
deepseek.json sha256 0128e4be10f2df95edb309420155b6e5d4ecadac3ee056d5888f4e7afc6d3729
inicio: 2026-10-28T15:56:47Z  fin: 2026-10-28T16:09:59Z
documento: /home/ignac/qca-causal-cones/papers/ir-corona/ir-corona.tex ; último commit observado: f85f429 ; sha256 de la copia enviada 2075e8402142451b6dc0182f3c923608f11cd8839dcd11061ca844d87fc04cc4
documento: /home/ignac/qca-causal-cones/debates/2026-10-28--ir-corona-repairs-review-deepseek/reparaciones.diff ; último commit observado: sin versionar ; sha256 de la copia enviada 7234a1fe359288b3069b24e9e64a0ea88c4fee8185046e809a139c5cee2246c0
entrada_deepseek.txt sha256 a3b026ff56aa81fdd9f08116988089e5e002f2b14d749e5a03677893d3fb849f
respuesta sha256 0445bc77f9fe066452237d610d978c3332cb57899f4908d6ed4b32f3c72cd183
-->

## Veredicto global: **CERRADA**

No encuentro errores matemáticos nuevos en las reparaciones. Las tres reparaciones obligatorias quedan cerradas y los cambios adicionales cerca de \(\pi u\) son correctos. Los valores numéricos concretos de la Tabla dependen de los certificados de aritmética de intervalos citados en el manuscrito; no puedo ejecutarlos en esta sesión, así que esa parte numérica queda **NO VERIFICADO**, pero la leyenda reparada es matemáticamente correcta.

---

## 1. Reparación de Lemma «Layers»(b): **CERRADA**

La reparación separa correctamente el espinor de Bob:

\[
r(y)=N^{-3/2}R_0(w_*)+\rho(y),
\qquad
\|\rho(y)\|\le C N^{-2}(1+\delta').
\]

La cota de \(\rho\) es correcta:

- Por el Lemma «tail», en \(\mathcal B_N\),

\[
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}).
\]

- \(R_0\) es suave en \(\mathcal B_N\), ya que allí \(|y/N|\ge \sqrt3-\frac14>0\).
- Además,

\[
|y/N-w_*|\le C(1+\delta')N^{-1/2},
\]

porque en la capa \(\delta'\) el radio tangencial es \(O(\sqrt{N\delta'})\).

Por tanto,

\[
\rho(y)=N^{-3/2}\bigl(R_0(y/N)-R_0(w_*)\bigr)+O(N^{-5/2})
\]

y

\[
\|\rho(y)\|\le C N^{-2}(1+\delta').
\]

El recuento de sitios \(O(1+N\delta')\) también es correcto: en la capa \(\delta'\) el soporte de \(h_N\) es un disco de radio \(O(\sqrt{N\delta'})\), luego tiene \(O(1+N\delta')\) sitios reticulares.

El término con \(\rho\) se acota sin usar oscilación:

\[
\sum_{j'\ge0} e^{-t_*(\theta_N+j')}
\frac{64\delta'^2}{N^2}
O(1+N\delta')
CN^{-2}(1+\delta')
\le C N^{-3}.
\]

Al dividirlo por el prefactor \(N^{-5/2}\frac{32}{\sqrt3}\), produce una contribución a \(\mathbf E_B\) de orden \(O(N^{-1/2})\). Por tanto

\[
\|\mathbf E_B\|\le C(N^{-1/2}+|\eta_n|),
\]

uniforme en \(\theta_N\) y en \(\eta\), y válida también cerca de \(\pi u\), porque la cota de \(\rho\) no usa las fases.

En «Assembly», la diferencia de capas se propaga con

\[
N^{-5}\int_{\mathbb R^3}
(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}\,d\eta
=O(N^{-7}),
\]

así que no se pierde el orden requerido.

**Conclusión:** reparación correcta.

---

## 2. Reparación de Lemma «Layers»(d): **CERRADA**

La reparación reconoce correctamente que el término \(m=0\) está presente, pero en frecuencia desplazada.

El argumento reparado es:

- Para \(\eta=\eta_0+\eta'\), con \(\eta_0\in\Sigma\setminus\{0,\pi u\}\), la fase tangencial sobre el plano es

\[
e^{i(\eta_{0,t}+\eta_t)\cdot u_\perp}.
\]

- La fórmula de Poisson en cada plano da frecuencias

\[
2\pi m-\eta_{0,t}-\eta_t,\qquad m\in\Lambda_0^*.
\]

El término \(m=0\) está presente.

- Por el Lemma «symbol»(c), el carácter \(e^{i\eta_0\cdot x}\) es no trivial en \(\Lambda_0\), así que

\[
\eta_{0,t}\notin 2\pi\Lambda_0^*.
\]

Por finitud de los seis puntos,

\[
d_0=\min_{\eta_0\in\Sigma\setminus\{0,\pi u\}}
\operatorname{dist}(\eta_{0,t},2\pi\Lambda_0^*)>0.
\]

Tomando \(r_0\le d_0/2\), toda frecuencia, incluida \(m=0\), tiene módulo al menos \(d_0/2\). La suma sobre \(m\in\Lambda_0^*\) es finita en dimensión dos, luego es uniformemente acotada.

La cota clave

\[
\|\partial^3G_\delta\|_{\mathcal M}\le C N^{-4}(1+\delta)^3
\]

es correcta. Repasando sus piezas:

- Salto de la segunda derivada de \(s_N\) en el borde:

\[
\llbracket \partial^2 s_N\rrbracket
\le 2\kappa|\nabla\varepsilon_\perp|^2
\le \frac{4\kappa\delta}{R},
\]

sobre un círculo de longitud \(O((R\delta)^{1/2})\). Esto da una contribución de medida

\[
O(\kappa\delta^{3/2}R^{-1/2})
\le C N^{-5/2}(1+\delta)^{3/2}.
\]

- Parte interior de la tercera derivada de \(s_N\): usando

\[
|S'|\le C\kappa e,\quad |S''|\le C\kappa,\quad |S'''|\le C\kappa^2 e,
\]

se obtiene

\[
\|\partial^3s_N\|_{\mathcal M}
\le C(\kappa\delta^{3/2}R^{-1/2}
+\kappa^2\delta^{7/2}R^{-1/2}).
\]

- El factor \(\varphi_N\) aporta

\[
\|\partial^b\varphi_N\|_\infty\le C N^{-3/2-b}.
\]

Por Leibniz,

\[
\|\partial^3G_\delta\|_{\mathcal M}
\le C N^{-4}(1+\delta)^3.
\]

Finalmente, la suma en profundidad

\[
\sum_{j\ge0} e^{-t_*(\theta_N+j)}
(1+\theta_N+j)^3
\]

es finita uniformemente en \(\theta_N\), así que

\[
|A_f(\eta_0+\eta)|\le C N^{-4}.
\]

En «Assembly», esto da

\[
O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})
=O(N^{-8}),
\]

que es más pequeño que el término principal \(O(N^{-13/2})\).

**Conclusión:** reparación correcta.

---

## 3. Reparación de la Tabla 1: **CERRADA**

La nueva leyenda es correcta.

La función

\[
C(\theta)=
\mathcal K c_r
\bigl[
\Gamma_+(\theta)\ell_0+\Gamma_-(\theta)\ell_\pi
\bigr]
\]

no tiene por promedio

\[
\overline C_{M,M_B}
=\mathcal K c_r \overline\Gamma \ell_0.
\]

De hecho, de la fórmula de Poisson para \(\mathcal S_+\):

\[
\mathcal S_+(\tau;\theta)
=\sum_{n\in\mathbb Z}
\hat g_\tau(2\pi n)e^{2\pi i n\theta},
\]

se deduce que el promedio en \(\theta\) de \(\Gamma_+\) es

\[
\int_{\mathbb R^2}
e^{-q_t|\tau|^2}
\sum_{n\in\mathbb Z}
|\hat g_\tau(2\pi n)|^2
\,d^2\tau
>
\int_{\mathbb R^2}
e^{-q_t|\tau|^2}
|\hat g_\tau(0)|^2
\,d^2\tau
=
\overline\Gamma.
\]

Análogamente, el promedio de \(\Gamma_-\) es positivo porque

\[
\Gamma_-(\theta)
=
\int_{\mathbb R^2}
e^{-q_t|\tau|^2}
\mathcal S_-(\tau;\theta)^2
\,d^2\tau
\]

y \(\mathcal S_-\) tiene coeficientes de Fourier no nulos en frecuencias impares.

No queda ningún otro uso de \(\overline C\) como promedio en el texto. La corrección de la leyenda elimina el defecto sin introducir incoherencias.

**Conclusión:** reparación correcta.

---

## 4. Cambios adicionales cerca de \(\pi u\)

### a) Fase global \(e^{-i\pi\theta_N}\) en «Layers»(c)

Es correcta:

\[
e^{i\pi u\cdot(x-x_*)}
=
e^{-i\pi(\theta_N+j)}
=
e^{-i\pi\theta_N}(-1)^j,
\]

y

\[
e^{-i\pi u\cdot(y-y_*)}
=
e^{-i\pi(\theta_N+j')}
=
e^{-i\pi\theta_N}(-1)^{j'}.
\]

Por tanto, ambos desarrollos cerca de \(\pi u\) llevan la fase global \(e^{-i\pi\theta_N}\), y el signo alternante produce \(\mathcal S_-\).

### b) Cancelación en «Assembly»

También es correcta.

Se tiene

\[
u\cdot Nv_*
=
3N-\frac{\sqrt3N}{2}.
\]

Luego

\[
e^{-iN\pi u\cdot v_*}
=
(-1)^N e^{2\pi i\theta_N}.
\]

El factor \((-1)^N\) proveniente de

\[
S(\pi u+\eta-i\xi_*)^N
=
(-1)^N\bigl(S(\eta-i\xi_*)^N\bigr)^T
\]

cancela el \((-1)^N\) anterior. Las fases globales de Alice y Bob aportan \(e^{-2\pi i\theta_N}\). Por tanto, el producto total es

\[
e^{-2\pi i\theta_N}
\cdot
e^{2\pi i\theta_N}
=
1.
\]

Así la contribución cerca de \(\pi u\) queda con \(\mathcal S_-\) y el proyector transpuesto \(\overline P\), sin fase residual.

### c) Recuento \(O(1+N\delta')\) en «Layers»(b)

Es correcto. En la capa \(\delta'\), el soporte de \(h_N\) es un disco de radio

\[
O\bigl(\sqrt{N\delta'}\bigr),
\]

por lo que contiene \(O(1+N\delta')\) sitios. Esto cubre tanto el caso \(\delta'=O(1)\) como \(\delta'\) pequeño o grande.

---

## Observaciones menores no obligatorias

1. En «Layers»(b), podría explicitarse que \(r_0\) se elige además menor que la mitad de la norma mínima no nula de \(2\pi\Lambda_0^*\), para que el control de los términos \(m\ne0\) de Poisson sea uniforme en \(\eta_t\). Esto se puede hacer sin afectar el resto.

2. En «Assembly», la cota gaussiana cerca de los otros seis puntos de \(\Sigma\) se sigue del Lemma «symbol»(b) junto con el Lemma «symbol»(d). Sería útil escribir una línea explícita, pero la conclusión es válida.

3. Los valores numéricos de la Tabla y de \(\varepsilon_\pm\), \(\ell_0,\ell_\pi\), etc., dependen de los certificados de aritmética de intervalos citados. En esta sesión no puedo ejecutarlos, por lo que esa parte queda **NO VERIFICADO**.

---

**Arreglos obligatorios: ninguno.**
