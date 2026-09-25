# C2c — criterios de la revisión independiente

Fecha: 2026-09-23. Estado: **FROZEN**.

Este documento fija, antes de que el revisor lea la nota, qué se revisa, cómo y con qué
veredictos. Queda congelado por el commit que lo introduce, posterior al commit del objeto
(`fa9c07f`) y anterior a la revisión. No se modifica después de que empiece la revisión; un
cambio exige un documento nuevo y la decisión explícita del usuario.

**Provenance.** Redactado a partir de la
[decisión del comité 001](../reports/comite/comite_decision_001_c2c-lista-para-revision.md),
§7, pasos 1–2 y 4. El contrato de alcance sigue siendo
[IR_C2C_STRUCTURAL_SCOPE_GATE](IR_C2C_STRUCTURAL_SCOPE_GATE.md); este documento no lo modifica,
sólo concreta su revisión. Los criterios se escriben **después** de conocer la ejecución, igual
que el contrato C2c se escribió después de C2b: no son una preregistración de los resultados,
sino un límite a los grados de libertad de la revisión.

## Objeto revisado

- Nota: `reports/2026-09-22--c2c-structural-scope.md` en el commit
  `fa9c07f`, blob `94cdf0f8801a219fc45df5000b86bb04614027ef`,
  SHA256 `f6266e951d3f5ffed20aef9ef8a75fe189f56b90df2b2f2e9af0abf11d407fb5`.
  El revisor la lee con `git show fa9c07f:reports/2026-09-22--c2c-structural-scope.md` y
  comprueba el blob antes de empezar.
- Autor de la derivación: Codex, agente `/root`. Snapshot de entrada: `f4f937e`.
- **Fuera de alcance:** §12 (addendum bibliográfico Liu–Chen), posterior a la derivación y ajeno
  a la prueba. La revisión no lo evalúa ni lo usa. Tampoco forman parte del objeto los documentos
  FR1–FR3, la lectura de Liu–Chen ni el roadmap del 2026-09-21.

## Alcance

La revisión cubre:

1. Las afirmaciones 1–4 de §11 de la nota: extensión exacta de A/B a los dieciséis pares;
   criterio abstracto (C1) y su versión individual con control complejo; transferencia lineal y
   cuadrática con (C8)–(C12), cota inferior (C15) y expansiones (C16); agrupación de
   coeficientes líderes.
2. El argumento de no localidad de §9.2, incluida la frase «Este argumento se extiende a cortes
   escalares…» (línea 611): se acepta con prueba dentro de la revisión o se registra como
   afirmación no revisada. No se da por cubierta por omisión.
3. La dependencia de §5.1 de la
   [representación C2](../reports/2026-09-22--c2-projected-response-representation.md), que se
   declara `REPRESENTATION_DERIVED / PRELIMINARY` y sin revisión independiente propia; el PASS de
   C2a sólo la cubre para \(\sigma_2\). La revisión comprueba las fórmulas de C2 que §5.1 usa
   ((2)–(3), (8)–(9)) para los cuatro M, o marca OPEN lo que dependa de ellas.

Los «puntos prioritarios» de §10 de la nota, escritos por su autor, se incluyen, pero no fijan
el alcance: la revisión no se limita a ellos.

## Entradas permitidas y prohibidas

Entradas permitidas:

- identidades exactas;
- el Teorema 4.1, usado sólo como cota superior de \(T_N\); de la formalización Lean sólo
  `TN_bound` (`formal/README.md`);
- los PASS de C1, C2a (\(\sigma_2/I\)) y C2b (\(\sigma_2/I\)), con su alcance registrado en
  `state/CURRENT_STATE.md` §10.1;
- el texto primario de C2a (`reports/2026-09-22--c2a-oscillatory-transfer.md`), no sólo su
  revisión.

Queda prohibido usar como demostración:

- \(L-L_{PP}\), la ley total del Teorema 4.4 y los valores N=24/40;
- cualquier cálculo numérico, cuadratura, simulación o barrido nuevo. La cuadratura certificada
  de \(G^{M,D}\) queda fuera; sólo podría falsar y exigiría un ítem aparte autorizado.

## Obligaciones de la revisión

1. **Test mínimo de falsación, antes de leer §5.2.** Partiendo de `f4f937e` y de la
   representación C2, derivar a ciegas y por escrito el emparejamiento lineal
   \(c_{M,D,N}\) y la forma cuadrática para la fila más adversa, \(M=I\),
   \(D_3=(I+\sigma_3)/2\). Listar el conjunto completo de fases radiales y comprobar que todas
   tienen módulo \(\ge\gamma=\sqrt3-3/2\) y que ninguna es estacionaria. Comprobar el valor de
   (C14) en esa fila (1/6 para ambos \(\sigma\)). Sólo después comparar con (C6), (C7) y (C14).
   Una fase estacionaria o un cruce \(\Pi_+D\Pi_-\) no controlado refuta las columnas «ley
   \(N^{-3}\)» y «coherencias» de las filas de rango uno, sin afectar a A/B ni a (C1).
2. **Rederivar §5.2 lema a lema** con el test \(w_{D,N}=hDR_N\) y el espinor \(\zeta_M\),
   desde C2a: lema angular (6), muestreo (16), corrector de dispersión (17)–(19), cambio de
   recurso (20) y transferencia cuadrática (21)–(23). No basta el argumento «D es una matriz
   constante de norma a lo sumo uno» (líneas 283–287) sin comprobar cada cota.
3. Recalcular (C3) y (C4) con sus constantes, y (C1) con su versión individual.
4. Recalcular (C8)–(C11) con **todos** los cruces \(\Pi_+D\Pi_-\), y los factores 64 en (C11)
   y 512 en (C15).
5. Verificar la definitud positiva de §7: independencia racional por polos simples distintos y
   (C14) para los cuatro detectores congelados.
6. Decidir dos igualdades que la nota afirma sin prueba escrita:
   - «se agrupan en ocho familias» (línea 527): demostrar que son exactamente ocho o registrar
     «a lo sumo ocho»;
   - «para \(\sigma_2/I\) son exactamente \(\mathcal C_0,\mathcal C_1\)» (líneas 436–437):
     mostrar la comparación de normalizaciones con C2a.
7. Registrar si \(\mathrm{Lin}_N=o(\mathcal Q_N)\) es necesaria y suficiente para la componente
   PP, dado que \(L_{PP}/\mathcal Q_N=1+\mathrm{Lin}_N/\mathcal Q_N\) exactamente.
8. Establecer una tabla de notación que desambigüe: \(J\) (tasa) frente a \(J(n)\); D
   (detector) frente a \(D^W_{M,K}\) y \(D_{M,N}\); Q (proyector) frente a \(\mathcal Q_N\);
   \(\rho\) frente a \(\rho_N\); \(R_N\) frente a \(R_N^{\mathrm{blocks}}\).
9. Confirmar que no se usan \(L-L_{PP}\), el Teorema 4.4, N=24/40 ni cálculo numérico.

## Veredictos

Se emite un veredicto **por fila (M, D) y por nivel** de la tabla S3 del contrato (identidades
exactas; compensación localizada; patrón relativo; ley \(N^{-3}\) y coeficiente; coherencias
individuales), más uno para (C1) y otro para §9.2. Cada casilla es `PASS`,
`REPAIR_REQUIRED`, `FAIL` u `OPEN`. Un nivel que la revisión no resuelve queda `OPEN`; nunca se
absorbe en `PASS` ni en `FAIL`.

El veredicto global es uno de los del contrato:

- `C2C_PASS`: con el alcance delimitado exactamente por las casillas en `PASS`, que se enumeran.
- `C2C_REPAIR_REQUIRED`: hay huecos reparables; se identifican sin cambiar el objeto revisado.
- `C2C_FAIL`: un error invalida un nivel que la nota da por derivado.
- `C2C_INCOMPLETE`: la revisión no se completa.

Un fallo en las filas de rango uno no invalida A/B, (C1) ni la fila \(\sigma_2/I\) certificada.
Una revisión es una sola revisión: no es consenso de varios miembros, revisión humana externa
ni promoción al estado canónico. La nota corregida, si la hay, es un objeto nuevo con su propio
commit y su propia revisión.

## Salvedades obligatorias en cualquier PASS

- La ganancia relativa del resto sobre el término principal es sólo \(N^{-1/4}\).
- El régimen asintótico llega despacio (\(\gamma\sqrt N\approx1.1\) en N=24).
- (C2), (C15) y (C16) valen para \(N\ge N_0(M,D)\), con \(N_0\) no efectivo; \(\lambda_{M,D}\)
  puede ser pequeño con detectores de rango uno. Nada se lee a N finito.
- El exponente 3 es propiedad del protocolo de corte \(K=\sqrt N\), no de la dinámica.
- (C1) se acepta sólo como teorema condicional; no verifica sus hipótesis en ningún otro modelo.
- La novedad sigue `OPEN`. El patrón \(+1:+1:-2\) sólo puede presentarse como resultado
  condicional dentro de la clase declarada; el argumento de §9.2 es de tipo Paley–Wiener clásico.

## Revisor

**Claude Opus 5** (`claude-opus-5`, Anthropic), por decisión del usuario del 2026-09-23.

Conflictos declarados:

- Fue autor del candidato C2b, cuyas identidades (B1)–(B4) C2c extiende.
- Fue el revisor de C2a: la adaptación de §5 transfiere precisamente los lemas que certificó.
  Revisa, por tanto, la extensión de su propia certificación.
- No es autor de C2c. Es de una casa distinta de la del autor (Codex, agente `/root`).

Mitigaciones obligatorias por el conflicto:

- La obligación 1 (test ciego sobre \(M=I\), \(D_3\)) se hace antes de leer §5.2 de la nota.
- La obligación 2 se rederiva desde el texto primario de C2a, no desde la revisión de C2a ni de
  memoria.
- El informe de revisión repite esta declaración de conflictos en su cabecera.

Candidatos descartados: Codex `/root` (autor de C2c y revisor de C2b) y Astra (misma casa que el
autor). Si se usa `sanedrin` como tercera casa, sólo como segunda voz sobre §5.2, nunca como
sustituto de la revisión.

## Límites

La revisión no modifica la nota, el contrato C2c ni `state/CURRENT_STATE.md`. Ningún resultado
se promociona sin una decisión posterior y explícita del usuario. C1, C2a y C2b conservan su PASS
y su alcance; C3 sigue separado y E/AdS congelado. No hay push sin instrucción del usuario.
