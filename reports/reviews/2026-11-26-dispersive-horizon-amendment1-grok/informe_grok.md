<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 4a4fccaecc259da07956a30c50ea620f7e21ebd9; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 30b387d714e1d349a2cff1510b3b3439f2918a69b3db666d415a75768426b229
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-26T10:54:01Z  fin: 2026-11-26T11:10:13Z
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-amendment1-grok/amendment1.diff ; último commit observado: sin versionar ; sha256 de la copia enviada f5e3387cd2b4c6df56dba70066d70669f340016c991cb9eedfd2a547d280fe34
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/2026-11-26--dispersive-horizon-transfer-matrix-audit.md ; último commit observado: 63db34b ; sha256 de la copia enviada 838cc16f09872206e00ea27173d9f0ed078297dfabc465c63da8b14824ce6c3b
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/reports/reviews/2026-11-26-dispersive-horizon-transfer-astra/informe_astra.md ; último commit observado: 63db34b ; sha256 de la copia enviada 49f77a0054bed8abf7821cb4693896c1c2e01398de4a54239c57bd2506315da9
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_repairs.py ; último commit observado: 63db34b ; sha256 de la copia enviada 5a315b68b7f48ded51290408a256e2c7485e8edb22a8b0299fbcfc750c99b0e8
documento: /home/ignac/qca-causal-cones/.worktrees/dispersive-horizon-audit/scripts/verify_dispersive_horizon_transfer_matrix.py ; último commit observado: d0114b2 ; sha256 de la copia enviada 98af2f6b90c51c170e1e92b6577cfe62a74fb734ee6e9191bbd5639bf3efbca2
entrada_grok.txt sha256 4d372a14676d6e78d4936b5da27f2dd388e55eee52b26f99659d137b962f2ff0
respuesta sha256 0ac67e3da1c5de983cf658ea6459915e08b295017f518ab4272668eb21c4de03
-->

**Veredicto global: REPAIR_REQUIRED.**

Las tres correcciones numéricas de la Enmienda 1 son ciertas: 21 sitios, multiplicidades 4 y 2 en el horizonte y 2 en los extremos, y el dominio «θ admisible, z ≠ 0». No hay fallo de la matriz ni de esas cifras. La enmienda no queda cerrada: atribuye a R2/R3 el desarrollo cúbico, que ese verificador no mira, y la sección de velocidad nula deja fuera una degeneración del mismo tipo.

El coeficiente de Astra, que la enmienda deja abierto, es correcto: \(\Omega_+=\dfrac{35}{32}k^3+O(k^5)\). Lo derivé a mano; no ejecuté ningún script. La ejecución de las 8 comprobaciones queda **UNVERIFIED**.

## 1. Multiplicidad en velocidad nula — PASS

En \(t=3/8\), \(A=t(2t-1)=-3/32\) y \(1+8A=(4t-1)^2=1/4\). Con
\[
f(k)=A\cos 3k+(1-A)\cos k
\]
la serie par es
\[
f=1-\frac{1+8A}{2}k^2+\Bigl(\frac{10A}{3}+\frac{1}{24}\Bigr)k^4+O(k^6)
=1-\frac{k^2}{8}-\frac{13}{48}k^4+O(k^6).
\]
La rama impar con \(E(0)=0\) y \(E'(0)=4t-1=1/2\) es \(E=\frac12 k+\beta k^3+O(k^5)\). Igualar \(\cos E=f\) en \(k^4\) da
\[
-\frac{\beta}{2}+\frac{1}{384}=-\frac{13}{48},\qquad \beta=\frac{35}{64}.
\]
Por tanto
\[
\Omega_+=-k+2E=\frac{35}{32}k^3+O(k^5),\qquad
\Omega_-=-2k-\frac{35}{32}k^3+O(k^5).
\]
Solo hay potencias impares porque \(\Omega_+\) es impar. El coeficiente \(35/32\) no es 0, así que el orden es exactamente 3, no mayor. Astra acierta también en
\[
\det(I-U(k))=(1-e^{i\Omega_+})(1-e^{i\Omega_-})=\frac{35}{16}k^4+O(k^5):
\]
el primer factor aporta orden 3 y el segundo orden 1.

Ese orden pasa al polinomio característico. Con \(zA\neq 0\),
\[
\det(\lambda I-M_{\mathrm{hom}})\cdot(-zA^2)=\mathcal P(\lambda,z),
\]
ambos de grado 12, y \(\mathcal P(\lambda,z)=\lambda^5\det(z-\lambda W^2)\) con \(\lambda^5(1)=1\). Como \(\lambda=e^{-ik}\) cumple \(\lambda-1\sim -ik\) (cambio de coordenada local), \(\lambda=1\) es raíz de multiplicidad algebraica **exactamente 4**. En los extremos el prefactor tampoco se anula: \(A(5/16)=-15/128\), \(A(7/16)=-7/128\).

La multiplicidad geométrica es 2 en los tres valores de \(t\). En \(k=0\), \(S(0)=I\) y \(W(0)=C(\theta)^2C(-2\theta)=C(0)=I\), luego \(U(0)=I\): todo el espacio de moneda, de dimensión 2, es núcleo. Dos espinores independientes dan dos vectores de Bloch independientes en el núcleo de \(M-I\) (la componente \(q_1\) se lee en \(Y\)). La cota superior usa la biyección de (B) §2, que esta enmienda no toca y que no reabrí entrada por entrada: un vector propio con \(\lambda=1\) produce un \(\psi\) espacialmente constante, y esos \(\psi\) forman un espacio de dimensión 2. En \(t=3/8\) y \(z=1\) los denominadores no se anulan (\(\cos\theta\), \(\sin\theta\), \(\cos 2\theta\) y \(z\)).

En \(t=5/16\) y \(t=7/16\),
\[
\Omega_+'(0)=8t-3=-\tfrac12,\ \tfrac12,\qquad
\Omega_-'(0)=1-8t=-\tfrac32,\ -\tfrac52,
\]
ambos distintos de 0. Cada banda aporta orden 1, la algebraica es exactamente 2 y, como la geométrica sigue siendo 2, la raíz es **semisimple**. No es un borde de banda.

La partición de Jordan en el horizonte, que la enmienda no afirma, es **3+1**, no 2+2: los órdenes de contacto 3 y 1 son los ciclos de Puiseux de \(\lambda(z)\) junto a \(z=1\).

## 2. Formulación sobre velocidad de grupo nula — REPAIR_REQUIRED

Lo que la enmienda afirma del punto \((z,\lambda)=(1,1)\) es correcto, y es correcto retirar la frase general: un cero de \(\partial_k\Omega\) no es, por sí solo, una raíz doble no semisimple. Hace falta una banda simple y un extremo cuadrático no degenerado (\(\Omega''\neq 0\)).

No es suficiente.

- En el mismo \(t=3/8\) la degeneración se repite en \((z,\lambda)=(-1,-1)\). Con \(k=\pi+q\) se tiene \(f(\pi+q)=-f(q)\). Si \(E_0\) es la rama pequeña de arriba, \(E=\pi+E_0(q)\) da
  \[
  \Omega=\pi+\frac{35}{32}q^3+O(q^5)
  \]
  y la otra banda sale con pendiente \(-2\). Otra vez orden \(3+1\). Además \(S(\pi)=-I\), \(W(\pi)=-I\), \(U(\pi)=-I\), así que la geométrica es 2. Mismos denominadores, \(z=-1\neq 0\).
- Para \(t\in[5/16,3/8)\) sigue habiendo un borde ordinario. En \(t=5/16\), \(\Omega_+'(0^+)=-1/2<0\) y \(\Omega_+'(\pi/2)=31/16>0\), con \(\Omega_+'\) continua en \((0,\pi/2]\); hay un cero en \((0,\pi/2)\). El polinomio en \(w=\cos^2 k-1\)
  \[
  2625w^2+5w-16=0
  \]
  tiene discriminante \(168025\neq 0\) y una raíz \(w\in(-1,0)\). Es simple, \(\sin E\neq 0\) y las dos velocidades no se anulan a la vez, luego \(\Omega''\neq 0\): raíz doble no semisimple, el caso que la frase retirada sí cubría. En \(t=7/16\) ese cero real no está (las dos raíces caen en \(\cos^2 k>1\)).
- En los extremos, «multiplicidad 2» es algebraica y geométrica, y es semisimple. Tal como está, se lee como si fuera el borde doble que se acaba de restringir. R3 solo certifica la algebraica.

\(z=i\) no es un borde: las pendientes \(1-8A\) y \(-3+8A\) no se anulan en el perfil. Eso ya estaba en (B) y no obliga a otra reparación.

## 3. Recuento de T3 — PASS

`psi` tiene claves \(0,\ldots,33\) (`NS = 34`). Cada `S` exige \(x-1\) y \(x+1\), así que en un intervalo quita un sitio por cada extremo. Cada `L` exige \(x+1\) y quita solo el extremo derecho. Las monedas no cambian las claves. Hay seis `S` y un `L`; sobre un intervalo conmutan. Resultado: \([6,26]\), es decir \(34-12-1=21\) sitios. `range(6, 27)` es exactamente ese conjunto. R1 decide eso y no otra cosa.

## 4. «θ admisible, z ≠ 0» — PASS

Para \(M_{\mathrm{hom}}\) los denominadores son \(\cos\theta\), \(\sin\theta\) (solo en la etapa 6: el orden termina en \(+\theta\)), \(\cos 2\theta\) (etapas de ángulo \(-2\theta\)) y \(z\). No aparece \(\sin 2\theta\) en el denominador. En el caso homogéneo eso es \(t\in(0,1)\), \(t\neq 1/2\), \(z\neq 0\). Ahí \(A=\cos^2\theta\cos 2\theta\neq 0\), el prefactor \(-zA^2\) no es cero y las multiplicidades de \(\det(\lambda I-M)\) y de \(\mathcal P\) coinciden. La identidad de T5 es de funciones racionales en ese dominio; el verificador la obtiene por resto módulo \(q_c^2+p_c^2-1\), no por evaluación en el perfil. Restringir la matriz y el polinomio característico a ese dominio es correcto y completo. La extensión formal tras eliminar denominadores, que Astra separa, no queda negada ni hace falta para el enunciado enmendado.

## 5. Verificador de la enmienda — PASS (la ejecución, UNVERIFIED)

Por inspección, las ocho comprobaciones deciden lo que dice su propio texto.

- El bucle de multiplicidad es correcto y cierra en falso negativo. `det(λI−M)` por Berkowitz es mónico de grado 12, no el polinomio nulo, así que el `while` termina. Solo divide por \(λ-1\) cuando el resto es el polinomio cero. Si `radsimp` no reconoce un cero, el bucle se detiene antes, `eval(1)` sigue siendo 0 y `nonzero_alg` devuelve falso: la aserción falla. Un falso PASS exigiría que `radsimp` convirtiera un coeficiente no nulo en 0, que no es su fallo típico, o que `minimal_polynomial` declarara no nulo un cero exacto. `nonzero_alg(0)` es falso, porque el mínimo de 0 es \(X\).
- Los dos vectores de Bloch están bien construidos. `order[:5]` aplica las cinco primeras monedas; \(S(0)=I\) justifica no insertar desplazamientos ni dividir por \(λ\). En T6, con \(λ=-i\), esa división sí está. \(Y=(a_1,\ldots,a_6,b_1,\ldots,b_6)\) es el orden de (B), y en \(k=0\) da igual \(b_j(x-1)\) que \(b_j(x)\). \(q_1\) es \((1,0)\) o \((0,1)\), así que ninguno es el vector cero. La independencia es un menor \(2\times 2\) no nulo.
- Un menor \(10\times 10\) no nulo da \(\mathrm{rango}(M-I)\ge 10\), luego nulidad \(\le 2\). Los dos vectores propios independientes dan nulidad \(\ge 2\). Juntos, geométrica exactamente 2. El `ok` final solo pone `found is not None` en el booleano; el «exactamente 2» se sostiene porque `ok` aborta si un propio anterior falla.
- Importar (5) no enmascara un fallo: `exec_module` ejecuta los 61 `ok` y cualquiera que falle lanza antes de R1. R1 lee `rv.interior`, asignado antes de los `ok` de T3, pero solo se alcanza si esos `ok` pasaron. El `print` final es `n/n` y no contrastaría un recuento esperado; el propio código tiene ocho `ok` fijos, así que si termina son ocho.

No reabrí las 144 entradas: la enmienda no las modifica.

## 6. Alcance — REPAIR_REQUIRED

R1–R3 cubren el recuento, la multiplicidad algebraica 4 con geométrica 2 en \(t=3/8\), y la algebraica 2 en los extremos. No cubren \(\Omega_+\sim k^3\), ni el valor \(35/32\), ni la geométrica en los extremos, ni \((z,\lambda)=(-1,-1)\).

La frase «These facts are certified exactly (repairs verifier R2, R3)» mete en ese saco el primer bloque, velocidad nula y \(\Omega_+\sim k^3\). La velocidad nula racional está en T8 de (5), no en R2/R3; el desarrollo cúbico no está en ningún verificador. El coeficiente \(35/32\) sí queda, correctamente, como no comprobado por la auditoría. No se cuela el resto de lo que solo argumenta Astra: la semisimplicidad en todo el intervalo en \(z=i\), ni el paso de compacidad de \(\omega^*\), que sigue en UNVERIFIED. Que los bytes de (5) sean los que vio Astra no lo he podido comprobar; por inspección, (4) no escribe en (5).

## Objeciones, por gravedad

1. **Alta.** «Points of zero group velocity», frase de certificación por R2/R3. Esa frase es falsa para \(\Omega_+\sim k^3\) y para la anulación de la velocidad. **Reparación:** dejar en R2/R3 solo las multiplicidades; escribir aparte que \(\Omega_+=(35/32)k^3+O(k^5)\) (el coeficiente ya no está abierto: la serie de arriba lo fija) y que la partición es 3+1. Si se quiere certificado de máquina, añadir el desarrollo al verificador, no atribuírselo al bucle de \((λ-1)\).

2. **Alta.** La misma sección no menciona la degeneración excepcional gemela. En \(t=3/8\), \((z,\lambda)=(-1,-1)\) tiene algebraica 4 y geométrica 2, con el mismo coeficiente \(35/32\) medido desde \(\pi\). **Reparación:** enunciarla junto a \((1,1)\) y extender R2 a \(z=-1\), \(λ=-1\).

3. **Media.** En \(t=5/16\) y \(t=7/16\) la raíz \((1,1)\) es semisimple (algebraica = geométrica = 2) y no es un borde. R3 no mira la geométrica. Además, para \(t\in[5/16,3/8)\) hay un extremo cuadrático ordinario de \(\Omega_+\) en \((0,\pi/2)\); en \(t=7/16\) no. **Reparación:** escribir «algebraica 2 y geométrica 2, semisimple» en los extremos, y una frase que localice el borde ordinario en \([5/16,3/8)\) y su ausencia en \((3/8,7/16]\).
