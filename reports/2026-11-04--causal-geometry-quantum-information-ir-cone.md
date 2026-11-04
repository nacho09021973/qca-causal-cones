# Geometría causal + información cuántica: ¿determinan el cono infrarrojo?

**Fecha:** 2026-11-04.  
**Naturaleza:** nota de discusión exploratoria, transcrita de una respuesta en español.  
**Estado científico:** `OPEN / UNVERIFIED` en cuanto a la propuesta de un invariante microscópico. La identidad para `G_{ij}` es una consecuencia algebraica bajo las hipótesis indicadas, no un teorema nuevo.  
**Alcance:** QCA de rango finito y sus límites infrarrojos. La alusión a los conjuntos causales es una analogía conceptual, no una extensión de la investigación a esa teoría.  
**Efecto sobre el repositorio:** ninguno. No es un *gate*, no autoriza cálculos, no modifica `state/CURRENT_STATE.md` ni reivindica novedad.

Creo que aquí tenemos una línea de investigación más interesante que PH.

En conjuntos causales:

$$
\boxed{\text{Orden}+\text{Número}=\text{Geometría}}
$$

En nuestros QCA podríamos buscar un principio análogo:

$$
\boxed{\text{Geometría causal}+\text{Información cuántica}=\text{Cono infrarrojo}}
$$

La cuestión es **qué información cuántica mínima necesitamos**.

## Una pista matemática concreta

Para un *walk* unitario con nodo sin masa en \(k=0\), definamos sus generadores lineales:

$$
T_i=i\,U(0)^\dagger\partial_{k_i}U(0).
$$

Para dos componentes, con generadores hermíticos sin traza, podemos construir

$$
G_{ij}=\frac12\operatorname{Tr}(T_iT_j).
$$

La velocidad de propagación en la dirección \(n\) satisface, a primer orden,

$$
v_{\mathrm{IR}}^2(n)=n^iG_{ij}n^j.
$$

Si el cono es isotrópico,

$$
\boxed{G_{ij}=c_0^2\delta_{ij}}.
$$

Esta identidad es exacta bajo las hipótesis indicadas. Pero **todavía no es un descubrimiento**: hemos expresado la velocidad mediante los generadores que ya la definen.

## Dónde podría aparecer algo nuevo

En conjuntos causales, el número aporta información que el orden no contiene.

En QCA necesitamos encontrar una cantidad microscópica que:

- No esté determinada por la geometría del soporte.
- Distinga *walks* con el mismo cuerpo causal y distintas velocidades.
- Permita reconstruir \(G_{ij}\) sin limitarse a reformular la derivada espectral.

Podría estar relacionada con las amplitudes, los solapamientos entre proyectores o las interferencias entre caminos. **No sabemos todavía cuál es la cantidad adecuada.**

Tenemos incluso una prueba de discriminación ya disponible: L6a y L6d comparten sustrato hexagonal, pero presentan \(c_0=1/2\) y \(c_0=3/4\), respectivamente, con la misma normalización (véanse los resultados restringidos a esas filas en las referencias internas).

Cualquier candidato a nuestro equivalente del «número» debe distinguirlos.

La pregunta sería:

> **¿Existe un invariante microscópico, más simple que el espectro completo del *walk*, que junto con \(C_{\mathrm{micro}}\) determine la métrica infrarroja?**

Si existe y podemos caracterizarlo de forma no tautológica, tendríamos un resultado potencialmente más interesante que la conjetura PH. **No está demostrado que exista ni que la analogía sea fértil.**

## Referencias internas y límites

- [`state/CURRENT_STATE.md`](../state/CURRENT_STATE.md), sección 11: alcance y estado de las filas comparadas.
- [`reports/2026-11-02--c-across-substrates-answer.md`](2026-11-02--c-across-substrates-answer.md): síntesis preliminar de \(c_0\) por sustrato, incluidas L6a y L6d.
- La nota no propone un observable nuevo definido, un contrato de investigación ni una demostración de reconstrucción. **`NOVELTY = OPEN`.**
