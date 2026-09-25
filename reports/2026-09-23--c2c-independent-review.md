# C2c — revisión independiente del objeto reparado

Fecha: 2026-09-23. Objeto revisado: `reports/2026-09-22--c2c-structural-scope.md`
en el commit `1d33130`, blob `af44a754f3c79447c507ac778adf6d8a74283efe`,
SHA256 `0268d8c869fa1b4666df09327e9ce25c0f545401fd5159286287580a888153a0`.

Este registro conserva la revisión independiente aportada por el usuario. La
revisión es analítica y de consistencia estructural/algebraica; no reejecuta
SymPy ni recomputa íntegramente las integrales tridimensionales de (C8)–(C12).
No modifica archivos del objeto revisado, no usa `L-L_PP`, Teorema 4.4,
`N=24,40`, simulaciones, cuadraturas ni barridos.

## Verificaciones load-bearing

- Las referencias a C2a (6), (16), (17)–(23) y a C2 (2)–(3), (8)–(9)
  corresponden a las ecuaciones de las entradas permitidas.
- La reducción de C2 (9) a C2a (12) usa
  `(I+sigma J)=2 Pi_sigma`; los factores de (C9) y (C11) son consistentes.
- Para `M=I`, `D_3=(I+sigma_3)/2`, en `n_0=(1,1,1)/sqrt(3)`, (C14) vale
  `1/6` para ambos signos `sigma`.
- El contraejemplo de §4 confirma que `Lin_N=o(Q_N)` es necesario para la
  componente PP del patrón, mientras C1 lo usa como condición suficiente.
- La transferencia reparada a los cuatro espinores y cuatro detectores se
  acepta como identidad matricial operatorial; los cruces `Pi_+ D Pi_-`
  permanecen en la matriz de Gram y la independencia racional por polos
  simples da la no anulación dentro de la lista congelada.
- La clasificación queda limitada a **a lo sumo ocho familias** y §9.2 a
  cortes escalares indicadores `p=1_Omega` con abiertos no vacíos y fuente
  finitamente soportada no nula.

## Veredictos

Para los 16 pares originales del walk CJWW (5.15), nodo cero, perfiles,
geometría y corte congelados:

| Nivel S3 | Veredicto |
| --- | --- |
| Identidades exactas | PASS |
| Compensación localizada | PASS |
| Patrón relativo | PASS |
| Ley `N^-3` y coeficiente | PASS |
| Coherencias individuales | PASS |

Los mismos veredictos se aplican al caso `sigma_2/I` ya certificado, sin
ampliar su alcance histórico.

`C1 = PASS`.

`§9.2 = PASS`, únicamente bajo la formulación escalar-indicadora indicada.

## Techo y estado

Veredicto global: **`C2C_PASS`**, acotado a los 16 pares originales y al
protocolo congelado. Se mantienen `N_0` no efectivo, constantes de resto no
explícitas, régimen asintótico lento, exponente 3 propio de `K=sqrt(N)` y
`NOVELTY=OPEN`. No se establece ninguna extensión a otros QCA, detectores,
geometrías, dimensiones o cortes.

Esta revisión no reabre C3 ni E/AdS y no autoriza FR1–FR3. El estado canónico
se actualiza por decisión explícita del usuario; este documento no constituye
una ratificación humana ni consenso de comité.
