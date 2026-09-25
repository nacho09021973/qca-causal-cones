# Congelación: afirmación de extremos \(O(N^{-3})\) no verificada

Fecha: 2026-09-25. Nota corta de registro. No hay cálculo nuevo, código ni
cambio de claims físicos. No modifica `state/CURRENT_STATE.md`, Schur,
Volterra, T1–T3 ni las piezas lineales \(A_{cP},A_{cQ}\).

## Estados congelados

\[
\boxed{\texttt{N^{-3} ENDPOINT CLAIM: UNVERIFIED}}
\]
\[
\boxed{\texttt{CURRENT CERTIFIED CHAIN: }N^{-6}}
\]

## Origen del agujero

En una conversación de trabajo no registrada en el repositorio se afirmó que las
normas \(L^2\) de los extremos inclinados son \(O(N^{-3})\). Combinada con la
cota Schur \(O(N^{-1})\), esa afirmación daba \(N^{-3}N^{-1}N^{-3}=N^{-7}\).
La afirmación no tiene derivación ni fichero que la sustente. Por eso la
cadena \(N^{-7}\) **no** existe como resultado.

## Cadena certificada

`state/CURRENT_STATE.md` §9.2 certifica solo masas absolutas inclinadas
\(O(N^{-5/2})\) por extremo. Esas masas son las de los extremos planos
heredados; su transferencia al modelo de dos canales no está certificada.
Como
\[
\|x\|_{\ell^2}\le\|x\|_{\ell^1},
\]
esas masas son también cotas \(\ell^2\) válidas. Con
`reports/2026-09-24--h1c-return-kernel-schur-audit.md` (8), la cadena es
\[
N^{-5/2}\,N^{-1}\,N^{-5/2}=N^{-6}
\]
(`reports/2026-09-24--two-channel-t2-trace.md`, (T2.2)). Frente al líder
\(N^{-13/2}\), la cadena pierde \(N^{1/2}\) y no prueba subordinación.

El \(O(N^{-15/2})\) del análisis Dyson con extremos planos
(`reports/2026-09-24--h1c-dyson-target-check.md`, (3)) es una cadena distinta.
No se aplica al contrato de dos canales.

## Qué exigiría la mejora

Sea \(S_{\rm eff}(x):=(\|x\|_{\ell^1}/\|x\|_{\ell^2})^2\) el soporte efectivo
del extremo inclinado. Entonces, de forma exacta,
\(\|x\|_{\ell^2}=\|x\|_{\ell^1}\,S_{\rm eff}^{-1/2}\). Con la masa
\(O(N^{-5/2})\), la condición \(S_{\rm eff}\gtrsim N\) uniforme basta para
tener \(\|x\|_{\ell^2}=O(N^{-3})\). Si la masa es \(\Theta(N^{-5/2})\), la
condición también es necesaria.

La idea de que una envolvente gaussiana tangencial de anchura \(\sqrt N\) en
dos direcciones dé \(S_{\rm eff}\sim N\) es una **HEURÍSTICA NO VERIFICADA**.
No se ha comprobado sobre el perfil real.

Aunque la mejora se probara, faltaría comprobar que el peso de inclinación y
la norma usada coinciden con la norma \(\ell^\infty_tL^2_p\) de Schur (8).

## Siguiente pregunta única

\[
\boxed{\text{¿el extremo físico inclinado del modelo de dos canales tiene
soporte efectivo }\gtrsim N\text{ uniformemente?}}
\]

Si la respuesta es no, la vía \(N^{-7}\) queda cerrada. Si es sí, hay que
demostrarla desde cero antes de reabrir \(N^{-7}\). No se toca Schur,
Volterra ni las cuatro piezas lineales hasta resolverla.
