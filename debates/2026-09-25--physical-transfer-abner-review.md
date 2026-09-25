---
tipo: sanedrín — deliberación adversarial multi-modelo
fecha: 2026-09-25 14:10
proyecto: /home/ignac/qca-causal-cones
tema: debates/2026-09-25--physical-transfer-abner-review-request.md
rondas: 1
reintentos: 1
max_fallos: 2
reglas: /home/ignac/sanedrin/reglas/base.md
miembros:
  - ABNER — DeepSeek — api.deepseek.com/deepseek-v4-pro
  - CLAUDE OPUS — Claude (Anthropic) — claude -p --model claude-opus-5 --effort high (sellado)
acceso: sellado — ningún miembro lee ficheros, terminal ni web; todos ven sólo el acta
conductor: sanedrin — sin intervención humana entre turnos
---

## Tema sometido al sanedrín

# Revisión focalizada de la versión reparada: transferencia a `A_{cP}`, `A_{cQ}`

## Decisión solicitada

Revisar únicamente la **versión reparada** de
`reports/2026-09-25--physical-linear-endpoint-transfer-gate.md` (las
reparaciones están marcadas `[rev. 2026-09-25]`). No reconstruir H1c. No
revisar Schur (`SCHUR_STABILITY_PASS`, ya revisado) salvo cómo se usa. No
buscar cancelaciones, simetrías ni observables nuevos; no proponer rutas
nuevas; no abrir L2; no ordenar L1/L2/L3 por importancia.

Toda afirmación que no pueda comprobarse con el material adjunto debe
marcarse `[UNVERIFIED]`.

## Seis puntos a verificar

1. La distinción `w_c^{fis} = E r_c` frente a su versión inclinada
   `w~_c = e^{-ξ_*·(y−y_*)}1_{B_N} w_c^{fis}` es ya correcta y consistente en
   fórmulas, diferencias de Duhamel y tabla final (a `ϑ=0`, `w_+^{fis}=w_N`,
   `w_-^{fis}=0`).
2. La única afirmación fuerte sobre Bob es: no hay `O(N^{-3})` demostrado para
   `ϑ≠0`; la cota disponible es `C_BΘN^{-2}`, con `C_B = 256/(3e²t_*²)`
   (≈21.3, sin redondear a la baja). Atacar expresamente si con el material
   adjunto existe un argumento que sí dé `O(N^{-3})` sin invariancia por
   traslación de `U_N`.
3. La descomposición de `y_N` usa exactamente T1 (14), con Q inicial y
   entradas desde `x_k^{stay}`, `f_{Q,k}`, `(𝕄x)_k`, sin partición inventada ni
   dominancia del último paso; `N_0` y `q` correctos.
4. El informe ya no atribuye `A_{cQ}=O(N^{-6}e^{-K_*N})` al PASS de Schur: con
   lo certificado sólo sale `N^{-5}`, y la mejora adicional depende de sumas
   de la clase de L3.
5. L1, L2 y L3 están formulados correctamente y son los únicos huecos
   identificados; ninguno está formulado con más de lo que exige.
6. La conclusión no dice más que `ENDPOINT_TRANSFER_PARTIAL` en el sentido
   concreto: Alice transfiere `O(N^{-3})` (preliminar); Bob no transfiere
   `O(N^{-3})` para `ϑ≠0`; ninguna conclusión sobre la supervivencia de la
   señal, sobre dominancia ni sobre subdominancia (salvo que `A_{+P}` a `ϑ=0`
   contiene el líder plano).

## Criterio de veredicto

`PASS`, `PASS_WITH_REPAIRS` o `REPAIR_REQUIRED` **sobre la versión reparada**,
con el primer paso que falla (si lo hay) y la condición exacta que lo
desactiva. No convertir una cota preliminar en resultado certificado.

## Contexto

### Contexto adjunto: reports/2026-09-25--physical-linear-endpoint-transfer-gate.md
```
# Transferencia de los extremos planos a las piezas lineales físicas A_{cP}, A_{cQ}

Fecha: 2026-09-25. Estado final:

```text
ENDPOINT_TRANSFER_PARTIAL
```

Alice transfiere (relación exacta con el extremo plano más una corrección
explícita de orden inferior). El extremo dual de Bob y la referencia `r_c`
no transfieren la ganancia `N^{-3}`. Aun con esa ganancia, el término
terminal P no queda subdominante por Cauchy–Schwarz (§7).

Además, **el objetivo tal como está escrito no es alcanzable para `A_{+P}`**
(§0). Esto se dice aquí y no se reformula en silencio.

Revisión (acta `debates/2026-09-25--physical-transfer-astra-review.md`):
Astra (GPT) `REPAIR_REQUIRED` en la ronda 1, Ciro (Grok) `PASS_WITH_REPAIRS`;
el turno de residuo y veredicto de Astra falló por cuota (`QUOTA`), de modo
que Astra **no** confirmó la versión reparada. Las reparaciones que ambos
piden están aplicadas en esta versión (marcadas `[rev. 2026-09-25]`); no ha
habido segunda revisión. Estado del informe: preliminar, sin registrar.

Etiquetas cuantitativas: `EXACT`, `ESTABLISHED_BOUND`, `PRELIMINARY_BOUND`,
`NO_CURRENT_BOUND`. Convención de este informe: `ESTABLISHED_BOUND` es sólo
lo que tiene revisión independiente documentada (Schur, `SCHUR_STABILITY_PASS`);
lo derivado aquí y sin revisar es `PRELIMINARY_BOUND`, aunque sus ingredientes
sean `ESTABLISHED_BOUND`. No se ejecutó código; la única aritmética es a mano
(§4).

Fuentes: `reports/2026-09-25--flat-endpoint-l2-n3.md`,
`reports/2026-09-25--schur-block-stability-repaired.md`, T1, T2,
`reports/2026-09-24--two-channel-reconstruction-operator-norms.md`,
`reports/2026-09-24--h1c-exact-dyson-decomposition.md`, Schur audit,
`papers/ir-corona/ir-corona.tex` §3 y Lemma `lem:layers`, informe regional
2026-09-17 vía la nota plana, `reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md` §§5–7.
No se modifica el manuscrito, el observable ni H1/H1c.

## 0. El objetivo literal no es alcanzable para `A_{+P}`

Para `vartheta=0`, `C_N=I`, `U_N=D=S⊕S^{-1}` y `J` coloca en el canal `+`
(§5, exacto): `r_+ = r` (referencia plana), `r_-=0`, `d_+ = a` (perturbación
plana), `d_-=0`. Entonces `L_+ = 2Re⟨r,Ea⟩+⟨a,Ea⟩ = L_flat`, cuyo término lineal
es exactamente el líder plano, de orden `N^{-13/2}e^{-K_*N}` con coeficiente
certificado no nulo (TeX, Thm. main). Ese término lineal es
`A_{+P}+A_{+Q}`; y `A_{+Q}` es exponencialmente pequeño a `vartheta=0`
(`d_{+,Q} = e^{-K_*N}V_+M^N Qs`, `‖M^N‖≤C_0ρ_1^N`, §4). Luego
`A_{+P}|_{vartheta=0} = L_flat^{lin} − O(ρ_1^N …)`: **`A_{+P}` contiene el
líder** y no puede ser subdominante frente a él. Lo que sí puede pedirse es
que la parte que depende de `vartheta` (el resto respecto de la pieza de
cero inserciones, §6) sea subdominante. Ese resto es el objeto que se acota
en §§4–5 siempre que se puede separar; donde no, se declara.

## 1. Obligación 1 — fuente de Alice

Con `φ_N = b_N ↓` (nota plana §3(a), `b_N` escalar real) y
`U_M−I = c_N I + i s_N M` (TeX §3), y `M↓ ∈ {↓,↑,−i↑,−↓}` para
`M ∈ {I,σ_1,σ_2,σ_3}`:

```text
f^{T1} = J(U_M−I)φ_N = J[ c_N b_N ↓ + ε_M s_N b_N χ_M ]        (EXACT)
ε_M ∈ {i, i, 1, −i},  χ_M ∈ {↓, ↑, ↑, ↓}.
```

- `ε_M f_N(χ_M)`, con `f_N = s_N b_N χ` el extremo plano heredado: **igualdad
  exacta módulo una fase unimodular**, embebido por `J` en el canal `+`.
- Resto explícito `J c_N b_N ↓`. De `c_N = cos(πF_N/2)−1`, `|c_N| ≤ π²F_N²/8`,
  `F_N = 64ε_⊥²/N² ≤ 64δ²/N²`, `δ ≤ (1+j)/√3` (nota plana §3(c)–(d)):
  `e^{ξ_*·(x−x_*)}|c_N b_N| ≤ C N^{-11/2}(1+j)^4 e^{-t_*j}`; con `#_j ≤ kN(1+j)`
  (nota plana §4), `‖c_N b_N‖_{ℓ²_tilt} = O(N^{-5})`. Constantes no evaluadas.
  `PRELIMINARY_BOUND` (mismos ingredientes que la nota plana, derivado aquí).
- Relación con `s`: `s = F H_ξ f^{T1}` y, por Parseval con `dμ=d³p/(2π)³`,
  `‖s‖_{L²} = ‖f^{T1}‖_{ℓ²_tilt}` **exactamente**; además `s(η)=e^{iη·x_*}𝔄_f(η)`
  con fase unimodular, luego `|s(η)|=|𝔄_f(η)|` puntualmente. La cota
  `‖s‖≤2` de T1/Schur era gruesa.

```text
‖s‖_2 = ‖f^{T1}‖_{ℓ²_tilt} ≤ ‖f_N‖_{ℓ²_tilt} + ‖c_N b_N‖_{ℓ²_tilt} = O(N^{-3}).
```

Rama: `ALICE: igualdad exacta con el extremo plano más un resto explícito de
orden N^{-5}`. La potencia `N^{-3}` hereda el estado `PRELIMINARY_BOUND` de la
nota plana. También transfiere `sup_η|s(η)| = O(N^{-5/2})` (Lemma `lem:layers`(a),
misma fase), no usada abajo.

Consecuencia con Schur (`ESTABLISHED_BOUND`): como el enunciado
`‖t_j‖_2 ≤ C(W,Θ)‖s‖_2` es lineal en `s`,

```text
sup_{j≤N} ‖t_j‖_2 ≤ ν_j-bound = O_{W,Θ}(N^{-3}),     ‖x_N‖_2,‖y_N‖_2 ≤ ν_N.
```

(`x_N=Pt_N`, `y_N=Qt_N`, `‖y‖_2≤‖y‖_*`; composición `PRELIMINARY_BOUND`.)

## 2. Obligación 2 — Bob y la referencia `r_c`

**[rev. 2026-09-25]** Se separan dos objetos que la versión anterior llamaba
igual: el vector físico `w_c^{fis} := E r_c` y su versión inclinada
`w~_c(y) := e^{-ξ_*·(y−y_*)}1_{B_N}(y) w_c^{fis}(y)`. Exacto (T1 (6)–(8),
`F` unitaria):

```text
⟨r_c, E V_c z⟩ = ⟨F w~_c, π_c z⟩_{L²(dμ)},        ‖F w~_c‖ = ‖w~_c‖_2 = ‖E r_c‖_{ℓ²_tilt(Bob)}.   (EXACT)
A_{cP} = 2e^{-K_*N} Re⟨F w~_c, π_c x_N⟩,   A_{cQ} = 2e^{-K_*N} Re⟨F w~_c, π_c y_N⟩.
```

`w_c^{fis}` es el extremo dual de Bob (vector físico); no hay conjugación por
traslaciones.

1. **¿Aparece `w_N` para `c=+`, `vartheta=0`?** Sí, exacto, como vector físico:
   `E r_+ = h_N M_B r = w_N` (`r_+=r`), es decir `w_+^{fis} = w_N` y
   `w~_+ = e^{-ξ_*·(y−y_*)}w_N`. Para `c=−`, `w_-^{fis}=w~_-=0`.
2. **Para `vartheta≠0`:** el objeto es `w_c = E B π_c U_N^N Jφ_N`. Con Duhamel
   `U_N^N−D^N = Σ_k U_N^{N−1−k}(C_N−I)D·D^k`, `‖C_N−I‖≤Θ/N`, unitariedad:
   `‖δr_c‖_2 ≤ Θ` para `δr_c = r_c − r^{(0)}_c`, luego
   `w_+^{fis} = w_N + Eδr_+`, `w_-^{fis} = Eδr_-`. Sólo relación parcial.
3. **Norma inclinada de `w_c`:** de `h_N ≤ 4s²/R²=64s²/N²` (`s=û·(y−y_*)≥0`,
   informe de normas §1) y `sup_s s²e^{-λs}=4/(e²λ²)`, `λ=√3t_*`:

```text
‖E V_c‖_{L²→ℓ²} ≤ sup_y h_N(y)e^{-ξ_*·(y−y_*)} ≤ C_B N^{-2},   C_B := 256/(3e²t_*²) ≈ 21.3,   (PRELIMINARY_BOUND)
‖w~_c‖_2 = ‖E r_c‖_{ℓ²_tilt} ≤ C_B N^{-2} ‖r_c‖_{ℓ²(B)} ≤ C_B N^{-2}            (usa ‖r_c‖≤1, EXACT).
```

   `[rev. 2026-09-25]` Se conserva la constante exacta `C_B`; el valor
   aproximado es `21.3` (máximo en `s=2/(√3t_*)`), no una mayorante `21`.

   Esto mejora a `N^{-1}` el uso simétrico `E^{1/2}` de las normas
   (§1 de ese informe): aquí se carga `E` entero del lado de la referencia.
   **`N^{-3}` no se puede probar:** el bound plano usa `sup_y‖r(y)‖≤c_φN^{-3/2}`
   por unitariedad de `S(p)` en el toro (nota plana §3(b)), que exige
   invariancia por traslación; `U_N` no la tiene (T1 §1 (1), nota plana §6).
   Con sólo `‖r_c‖_2≤1` no hay control de la masa de `r_c` en cada capa de
   Bob (`‖r_c‖_{ℓ²(capa j')}` debería ser `O(N^{-1})`; sólo se sabe `≤1`).
   `NO_CURRENT_BOUND` para `‖E r_c‖_{ℓ²_tilt}=O(N^{-3})` y para cualquier
   potencia mejor que `N^{-2}` con `Θ≠0` fijo. La diferencia
   `‖E δr_+‖_{tilt} ≤ C_BΘN^{-2}` tampoco se puede llevar bajo `N^{-3}`. Esto
   respalda `NO_CURRENT_BOUND` con el material adjunto; no prueba que no exista
   otra deducción.

La unitariedad `‖r_c‖≤1` sola no cuenta como transferencia de la mejora.
Lo que sí se obtiene es un factor `N^{-2}` puramente geométrico.

## 3. Obligación 3 — término terminal P

Con T1 (14): `x_N = x^{stay} + f_{Q,N} + (𝕄_N x)_N`. Bloques de Schur
(`ESTABLISHED_BOUND`, nota reparada §4), `N ≥ N_0(W,Θ)` para `ρ_2:=ρ_1(1+C_0C_QΘ/N)<1`:

| Parte | Norma L² (todo con `‖s‖`) | Estado |
| --- | --- | --- |
| `x^{stay}=Φ_P(N,0)Ps`: quedarse en P | `≤ e^{C_PΘ}C_P‖s‖ = O(N^{-3})` | `PRELIMINARY_BOUND` (composición; ingrediente `A_j` ESTABLISHED) |
| `f_{Q,N}`: Q inicial, `Q→P` | `≲ C N^{-1}‖s‖ = O(N^{-4})`, vía `‖B_m‖≤ρ_1C_PΘ/N`, `‖G_Q(m,0)Qs‖_*≤ρ_2^mC_0C_Q‖s‖` | `PRELIMINARY_BOUND` |
| `(𝕄_Nx)_N`: excursiones `P→Q→P` | `≲ C N^{-1}‖s‖ = O(N^{-4})`, sumando `Σ_{m>k}ρ_2^{m−k−1}≤N/(1−ρ_2)` sobre `(C_PΘ/N)(C_0C_QΘ/N)` | `PRELIMINARY_BOUND`; **es la cota tipo Schur (7)–(8), fuera del PASS** |

La identidad `𝒫β𝒫=0` (H1-SR) no se usa: vale a momento fijo y `Ĉ_N` mezcla
momentos; el selector `O(|q|)` de §9.4 no está probado. El coeficiente de
cada parte sólo entra por normas.

Estado: la potencia `N^{-3}·N^{-1}·N^{-3}=N^{-7}` para las correcciones de
retorno y de Q inicial exige **dos** cosas: (i) la cota tipo `𝕄_N` sin revisar
(aquí derivada en cuatro líneas a partir de los bloques revisados, pero no
revisada), y (ii) `‖E r_c‖_{ℓ²_tilt}=O(N^{-3})`, que no existe (§2). Me detengo
en el punto (ii): sin él el recuento `N^{-7}` es un recuento formal, no un
teorema. Con lo disponible, `f_{Q,N}` y `(𝕄_Nx)_N` contribuyen como máximo
`C_BN^{-2}·O(N^{-4}) = O(N^{-6})e^{-K_*N}`.

El término `x^{stay}`: aun con `‖E r_c‖=O(N^{-3})`, Cauchy–Schwarz da
`N^{-3}·N^{-3}=N^{-6}`, mayor que el líder `N^{-13/2}`; la potencia del líder
sale de `sup|𝔅_w|·sup|𝔄_f|·∫|m|^N ~ N^{-5/2}N^{-5/2}N^{-3/2}`
(localización gaussiana), no de la norma L². Con `Φ_P(N,0)≠m^N` (N inserciones
`PEm` de tamaño `Θ/N`, acumulan `O(1)`, no `o(1)`), no hay estimación de
`x^{stay}` por debajo de `N^{-6}`: `NO_CURRENT_BOUND` (es H1c_LOCALIZATION,
abierto). **[rev. 2026-09-25]** "Por debajo de `N^{-6}`" no equivale a
`o(N^{-13/2})`; para subdominancia hay que alcanzar esta última escala sobre
el **resto pertinente**, no sobre `A_{+P}` completo. Además, al restar el
protocolo plano varían ambos extremos:
`⟨r_ϑ,E V x_ϑ⟩−⟨r_0,E V x_0⟩ = ⟨r_ϑ−r_0, E V x_ϑ^{stay}⟩ + ⟨r_0, E V(x_ϑ^{stay}−x_0^{stay})⟩`.
El segundo sumando puede usar el extremo plano de Bob (`N^{-3}`) y da a lo sumo
`N^{-6}`; el primero lleva `‖δr‖` sólo con el peso geométrico `N^{-2}` y queda en
`N^{-5}`. Controlar sólo `Φ_P−m^N` no lo cierra.

## 4. Obligación 4 — término terminal Q

`y_N = G_Q(N,0)Qs + Σ_{k<N}G_Q(N,k+1)C_kx_k`, con `‖D_j‖_*≤ρ_2`,
`‖C_k‖_{2→*}≤C_0C_QΘ/N`, `‖x_k‖_2≤ν_k≤e^κν_0`:

**[rev. 2026-09-25]** Partición exacta por sustitución de `x_k = x_k^{stay}+f_{Q,k}+(𝕄x)_k` en T1 (14)
(las cuatro filas anteriores no eran disjuntas: `k=N−1` pertenece a las historias ya
contadas, y no se prueba que sea dominante). Con `q=(1+ρ_1)/2`,
`N ≥ N_0 := max{2, ⌈2ρ_1C_0C_QΘ/(1−ρ_1)⌉}` (entonces `ρ_2≤q`):

| Origen | Cota de `‖·‖_*` | Estado |
| --- | --- | --- |
| Q inicial `G_Q(N,0)Qs` | `≲ q^N N^{-3}` | `PRELIMINARY_BOUND` |
| entradas desde `x_k^{stay}` | `≲ N^{-1}‖s‖ = O(N^{-4})` | `PRELIMINARY_BOUND` |
| entradas desde `f_{Q,k}` | `≲ N^{-1}·N^{-1}‖s‖ = O(N^{-5})` | `PRELIMINARY_BOUND` |
| entradas desde `(𝕄x)_k` | `≲ N^{-1}·N^{-1}‖s‖ = O(N^{-5})` | `PRELIMINARY_BOUND` |

Total: `‖y_N‖_2 ≤ C(N^{-1}+q^N)‖s‖ = O(N^{-4})`. Sólo con el PASS de Schur
(`‖y_N‖_2≤‖t_N‖`-tipo) se tendría `O(N^{-3})` y por tanto `A_{cQ}=O(N^{-5})`; el factor
`N^{-1}` adicional exige las sumas `Σ_kG_Q(N,k+1)C_kx_k`, de la misma clase que L3
(fuera del PASS). Con `‖E V_c‖ ≤ C_BN^{-2}`:

```text
|A_{cQ}| ≤ 2e^{-K_*N}‖r_c‖‖E V_c‖‖y_N‖ = O(N^{-6}) e^{-K_*N}       (PRELIMINARY_BOUND; N^{-5} sólo con el PASS de Schur)
```

`N^{-6}` no demuestra `o(N^{-13/2})` (la cota superior no es una asintótica). Si existiera `‖E r_c‖_{ℓ²_tilt}=O(N^{-3})`, el mismo
argumento daría `O(N^{-3}·N^{-4})=O(N^{-7})=o(N^{-13/2})` (cociente `N^{-1/2}`).
Es el único término lineal para el que Cauchy–Schwarz bastaría, y depende
exactamente del lema que falta en Bob. Sin él, el control fino de `A_{cQ}`
**sigue abierto**; la cota previa `O(N^{-1}e^{-K_*N})` mejora a `O(N^{-6}e^{-K_*N})`.

Reutilización de `FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW`
(`…reconstruction.md` §7): **no se transfiere**. (i) Bob es el extremo plano
`𝔅_w`, `w=h_BM_Br`, no `w_c=E r_c` con `U_N`; (ii) es una ventana local de
Riesz con "frozen frame" `𝒫_N=𝒫+O(N^{-1})`, sin `P=0` fuera de `W`, sin
transiciones entre ocho ventanas ni con `W^c`; (iii) usa `sup_η‖𝔅_w‖` y el factor
gaussiano `N^{-3/2}`, no la norma L² de los bloques Schur; (iv) el producto
`N^{-1}N^{-5/2}N^{-5/2}N^{-3/2}=N^{-15/2}` no proviene de la contracción
`ρ_1` en `Q`.

## 5. Obligación 5 — cero inserciones

Para `vartheta=0`: `C_N≡I`, `U_N=D=S⊕S^{-1}`, `Jφ_N=(φ_N,0)`, luego
`U_N^NJφ_N=(S^Nφ_N,0)` (**EXACT**, `D` diagonal por bloques). Así `r_+=r=P_BS^Nφ_N`,
`r_-=0`; `d=U_N^N f^{T1}=(S^N(U_M−I)φ_N,0)`, `d_+=a`, `d_-=0`. De T1 (10):

```text
L_+ = 2Re⟨r,Ea⟩ + ⟨a,Ea⟩ = L_flat (TeX (Lexp)),    L_- = 0.          (EXACT)
```

Es el par `(L_+,L_-)|_{ϑ=0} = (L_flat,0)`, y el término de cero inserciones del
desarrollo de Dyson (`h1c-exact-dyson-decomposition` (1), `n=0`). Sólo fija la
referencia. Los restos `L_+−L_flat` y `L_-` recogen todo lo que depende de
`vartheta`; para `c=−` ambos extremos (`r_-`, `d_-`) son restos y `A_{-P},A_{-Q}`
son un par de correcciones. No se infiere ninguna cota de esto.

## 6. Tabla final

Todas las filas comparten la misma cadena; los cuatro términos difieren sólo
por el canal `c` y por `P/Q`. `‖π_c‖≤1`, sin ganancia adicional; no se ha
usado ninguna cancelación entre `+` y `−` ni entre piezas.

| TERM | EXACT_PHYSICAL_ENDPOINTS | ALICE_NORM | BOB_DUAL_NORM | INTERNAL_BOUND | EXPONENTIAL_SCALE | POWER_OF_N | SUBDOMINANT_TO_N^-13/2? | TRANSFER_STATUS | MISSING_LEMMA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `A_{+P}` | `s=FH_ξJ(U_M−I)φ_N`; `w_+^{fis}=E B π_+U_N^NJφ_N` (`=w_N` si `ϑ=0`); `w~_+`= su versión inclinada; `x_N=Pt_N` | `‖s‖=‖f^{T1}‖_{tilt}`: EXACT igualdad; `O(N^{-3})` PRELIMINARY_BOUND | `‖E V_c‖≤C_BN^{-2}` PRELIMINARY_BOUND; `‖w~_+‖=O(N^{-3})`: NO_CURRENT_BOUND | `‖x_N‖≲‖s‖`: ESTABLISHED_BOUND (Schur); partes stay/`f_Q`/`𝕄_N`: PRELIMINARY_BOUND | `e^{-K_*N}` EXACT | `N^{-5}` PRELIMINARY_BOUND | **NO PROBADO**; a `ϑ=0` contiene el líder (§0), luego no puede serlo | ENDPOINT_TRANSFER_PARTIAL | L1 (capa de Bob de `r_c`); L2 (líder gaussiano con `Φ_P≠m^N`); L3 (revisar 𝕄_N) |
| `A_{+Q}` | igual con `y_N=Qt_N` | igual | igual | `‖y_N‖_2≲(N^{-1}+ρ_2^N)‖s‖`: PRELIMINARY_BOUND | `e^{-K_*N}` EXACT | `N^{-6}` PRELIMINARY_BOUND; `N^{-7}` si L1 | **NO PROBADO**; `o(N^{-13/2})` (`N^{-7}`) sólo si L1 | ENDPOINT_TRANSFER_PARTIAL | L1 |
| `A_{-P}` | `w_-^{fis}=Eδr_-` (`=0` si `ϑ=0`); `π_-x_N` | igual que `+` | `‖E δr_-‖_{tilt}≤C_BΘN^{-2}`: PRELIMINARY_BOUND; `N^{-3}`: NO_CURRENT_BOUND | igual que `+P` | `e^{-K_*N}` EXACT | `N^{-5}` PRELIMINARY_BOUND (`Θ`-dep.) | **NO PROBADO** | ENDPOINT_TRANSFER_PARTIAL | L1; L2; L3 |
| `A_{-Q}` | `w_-`; `π_-y_N` | igual | igual | igual que `+Q` | `e^{-K_*N}` EXACT | `N^{-6}`; `N^{-7}` si L1 | **NO PROBADO**; condicional a L1 | ENDPOINT_TRANSFER_PARTIAL | L1 |

Lemas que faltan:

- **L1** `[rev.]`. `‖r_c‖_{ℓ²(capa j')} ≤ N^{-1}a_{j'}` con
  `Σ_j(1+j)^4e^{-2t_*j}a_j²<∞`, uniformemente en los parámetros declarados
  (`W`, `Θ`), para `r_c=Bπ_cU_N^NJφ_N` con moneda no invariante por traslación;
  un `O(N^{-1})` con constante no controlada en `j` no basta. La alternativa
  puntual `sup_y‖r_c(y)‖=O(N^{-3/2})` sí lo da. Análogo de la unitariedad de
  `S(p)` en el toro, que aquí no aplica.
- **L2** `[rev.]`. Sobre el **resto `ϑ`-dependiente** de `A_{+P}` (no sobre `A_{+P}`
  completo): probar `o(N^{-13/2}e^{-K_*N})` incluyendo la variación de ambos
  extremos (`δr` y `δx^{stay}`, no sólo `Φ_P−m^N`); pairing con localización
  gaussiana (H1c_LOCALIZATION).
- **L3** `[rev.]`. Revisión independiente de las sumas tipo Schur (7)–(8): `f_{Q,N}`,
  `(𝕄_Nx)_N` y también `Σ_kG_Q(N,k+1)C_kx_k` (la cota `‖y_N‖=O(N^{-4})`).

## 7. Conclusión

- **Alice: transferencia establecida** (igualdad exacta con el plano más un resto
  `N^{-5}`), potencia `N^{-3}` heredada como `PRELIMINARY_BOUND`.
- **Bob/referencia: transferencia parcial.** Sólo `‖E V_c‖=O(N^{-2})` (geométrico) y
  la representación exacta con `w_c^{fis}=E r_c` (y `w~_c` su versión inclinada). Para `ϑ≠0`
  no hay `O(N^{-3})` demostrado (`NO_CURRENT_BOUND`); la cota disponible es `C_BΘN^{-2}`,
  `C_B=256/(3e²t_*²)`.
- **Los cuatro términos lineales** quedan acotados por `N^{-5}` (P) y `N^{-6}` (Q)
  (`N^{-5}` para Q con sólo el PASS de Schur). Estas cotas **no demuestran**
  subdominancia frente a `N^{-13/2}`; tampoco la excluyen, salvo para `A_{+P}` a
  `ϑ=0`, que contiene el líder (y `A_{-P}=A_{-Q}=0` a `ϑ=0`).
- **Si L1 se probara,** `A_{±Q}` pasaría a `N^{-7}=o(N^{-13/2})` (`o` del líder, no
  del resto absoluto conocido `O(N^{-7})` del líder plano, nota plana §6); el término
  terminal P **no**, por Cauchy–Schwarz (necesita L2). Así el estado
  `PHYSICAL_LINEAR_TRANSFER_PASS` o `P_TRANSFER_PASS_Q_OPEN` no se alcanza
  ni con L1; el cierre sería, como mucho, `Q_TRANSFER_CONDITIONAL_P_OPEN`
  (etiqueta no permitida por el encargo; se registra sólo como descripción).
- `N^{-3}·N^{-1}·N^{-3}=N^{-7}` **no se convierte en teorema**: exige L1 y la
  cota tipo `𝕄_N` sin revisar. No hay término líder firmado ni cancelación.
- **Ninguna conclusión sobre la supervivencia de la señal** ni sobre dominancia. El
  estado `ENDPOINT_TRANSFER_PARTIAL` significa sólo: Alice transfiere `O(N^{-3})`
  (preliminar); Bob no transfiere `O(N^{-3})` para `ϑ≠0`.
- No se ordena aquí cuál de L1/L2/L3 es decisivo con las cotas corregidas.
- H1/H1c, manuscrito, observable y `CURRENT_STATE.md`: sin cambios.
```

### Contexto adjunto: reports/2026-09-25--schur-block-stability-repaired.md
```
# Estabilidad L² del producto normalizado: reparación de Schur §2 con E5 explícito

Fecha: 2026-09-25. Estado: `SCHUR_STABILITY_PASS` (revisión independiente
documentada, §5) para la conclusión de §1 y nada más.
Alcance: **sólo** la cota uniforme de `||t_j||_2`, `0<=j<=N`, con `W`
admisible fijo y `vartheta` real acotado. No cubre Schur (7)–(8), ni
`||M_N|| = O_W(N^-1)`, ni las cotas de las diez piezas físicas, ni H1/H1c.
Revisión: ver §5. Las consecuencias físicas que usan `t_N` (informe de
normas (5)–(6), piezas) conservan su propio nivel; este `PASS` no las
promueve.

## 1. Enunciado

Con las definiciones de T1 §§1–2 y (13) (`T = C^_N L`, `L = D_xi/Lambda`,
`t_j = T^j s`, `x_j = P t_j`, `y_j = Q t_j`), fijados `W` admisible y
`Theta < infinito`:

> Para cada `W` admisible fijo y cada `Theta < infinito` existe `C(W,Theta)`
> tal que, para todo `N>=2`, todo perfil real
> `vartheta` con `||vartheta||_inf <= Theta`, todo encoder `M` y todo
> `0<=j<=N`, `||t_j||_2 <= C(W,Theta) ||s||_2 <= 2 C(W,Theta)`.

No hay uniformidad en `W` (ver §4, cierre): el cuantificador sobre `W` va
delante. La dependencia es `O_{W,Theta}(1)`, no `O_W(1)`: la constante contiene
`e^kappa` con `kappa = Theta (C_P + C_0 C_Q)`. `C_P, C_Q, K_D, C_0, rho_0,
rho_1` dependen de `W` y del símbolo, no de `N`, `j`, `M` ni `vartheta`.

## 2. Datos y constantes

- (E3) `C^_N = F C_N F^-1`, `C_N(x) = exp(-i vartheta(x/N) beta / N)`,
  `beta` hermítica e involutiva. Como `|e^{-i a}-1| <= |a|`,
  `E := C^_N - I` cumple `||E||_{2->2} <= Theta/N`. La moneda conmuta con
  `H_xi` (ambas son multiplicaciones en posición), y `F` es unitaria.
- (E4) `C_P = ess sup ||P(p)||`, `C_Q = ess sup ||Q(p)||` (T1 (3a)),
  `K_D = sup_p ||D_xi(p)|| / Lambda` (símbolo continuo en el toro).
  Normas de fibra: euclídea en `C^4`; la norma de un multiplicador en
  `L^2(T^3; C^4, dmu)` es el supremo esencial de la norma de fibra.
- (E1) En `W`, `D_xi = diag(S_xi, S_xi^-1)` y `P = diag(p_S, I-p_S)`;
  por (3a) y `det S_xi = 1`,
  `D_xi P = lambda P`, `D_xi Q = lambda^-1 Q`, con `|lambda| > 1`.
  Fuera de `W`, `P = 0`, `Q = I`. Luego `P D_xi Q = 0 = Q D_xi P`
  en casi todo punto, y `D_xi Q = Q D_xi Q`.
- (E2) `m(p) = lambda(p)/Lambda` en `W`, `m = 0` fuera. `lem:specrad`
  (TeX) da `rho(S(eta - i xi_*)) <= Lambda`; `lambda` es la raíz de
  módulo mayor, así que `|m| <= 1`. Es una cota **escalar**: no se usa
  como cota de la norma de ninguna matriz.
- `M(p) = Q(p) D_xi(p) Q(p) / Lambda`, multiplicador en momento.
  `||M(p)|| <= K_M := max(1,C_Q)^2 K_D`.

## 3. E5 ejecutado: norma `||.||_*`

**Separación espectral uniforme.**

- En `W`: de `D_xi Q = lambda^-1 Q` y `Q^2 = Q`, `M(p) = (lambda Lambda)^-1 Q(p)`,
  `M^h = (lambda Lambda)^-h Q`. Espectro contenido en
  `{0, (lambda Lambda)^-1}` y, como `|lambda| > 1` y `Lambda = e^{Phi_*} > 1`,
  `rho(M(p)) <= Lambda^-1 < 1`. No hace falta continuidad de la familia
  partida `p -> M(p)` a través de `partial W`. La compacidad que sí se
  usa dentro de `W` es la de los cierres `closure(W_alpha)` subset `O_alpha`,
  a través de `C_P` (T1 (3a)), y por tanto de `C_Q <= 1 + C_P` y `K_M`:
  la admisibilidad de `W` se paga ahí.
- Fuera de `W`: `M = D_xi/Lambda` y `rho(D_xi) = rho(S_xi)` (mismo
  espectro, `det S = 1`). `K = T^3 \ W` es compacto (W abierto) y no
  contiene ningún punto de `Sigma`, y `xi_* = t_* (1,1,1)` tiene todas
  las componentes no nulas: por `lem:specrad`, `rho(D_xi/Lambda) < 1` en
  cada punto de `K`. El símbolo es continuo y `rho` es continuo sobre
  matrices `4x4`, luego `r_ext := max_K rho(D_xi/Lambda) < 1`.
- `rho_0 := max{Lambda^-1, r_ext} < 1`, y `rho(M(p)) <= rho_0` para casi
  todo `p`. La frontera `partial W` pertenece a `W^c = K`
  (T1 §2, `W` abierto), de modo que queda cubierta por el caso exterior.
  No se usa que tenga medida nula.

**Resolvente sin diagonalizabilidad.** Se fija por convención
`rho_1 := (1 + rho_0)/2`, con lo que `C_0` y `C(W,Theta)` son funciones
bien definidas de `W`.
Para `|z| = rho_1`: `|det(zI - M)| >= (rho_1 - rho_0)^4`, y, para
matrices `4x4`, `||adj(A)|| <= ||A||^3` (los valores singulares de
`adj(A)` son productos de tres valores singulares de `A`). Con
`||zI - M|| <= rho_1 + K_M`,
`||(zI-M(p))^-1|| <= R := (rho_1+K_M)^3 / (rho_1-rho_0)^4`.
Sin número de condición ni base propia.

**Cauchy.** `M^h = (2 pi i)^-1 ∮_{|z|=rho_1} z^h (zI-M)^-1 dz`, luego
`||M(p)^h|| <= R rho_1^{h+1}` y, con `C_0 := max{1, R rho_1}`,
`||M^h||_{2->2} <= C_0 rho_1^h`.

**Norma.** Para `y in ran Q`, `||y||_* := sup_{h>=0} rho_1^-h ||M^h y||_2`.
Entonces `||y||_2 <= ||y||_* <= C_0 ||y||_2` y
`||M y||_* <= rho_1 ||y||_*` (desplazar el índice `h`).

## 4. Bloques, recurrencia y dato inicial

Como `T = (I+E) L`, `L x = m x in ran P` para `x in ran P`
y `L y = M y in ran Q` para `y in ran Q` (E1):

| Bloque | Identidad | Cota |
|---|---|---|
| `A_j` en `ran P` | `A_j x = m x + P E m x` | `||A_j x||_2 <= (1 + C_P Theta/N) ||x||_2` |
| `B_j`, `ran Q -> ran P` | `B_j y = P E M y` (porque `P D_xi Q = 0`) | `||B_j y||_2 <= rho_1 C_P Theta/N ||y||_*` |
| `C_j`, `ran P -> ran Q` | `C_j x = Q E m x` (porque `Q m x = 0`) | `||C_j x||_* <= C_0 C_Q Theta/N ||x||_2` |
| `D_j` en `ran Q` | `D_j y = M y + Q E M y` | `||D_j y||_* <= rho_1 (1 + C_0 C_Q Theta/N) ||y||_*` |

En `B_j`, `D_j` se usó `||M y||_2 <= ||M y||_* <= rho_1 ||y||_*`. Los
productos `P(p') Q(p)` con `p' != p` no se anulan: viven dentro de `E`
y se pagan con `||E|| <= Theta/N`. La identidad de `A_j` exige el orden
`T = C^_N L` (moneda después del bloque libre) de T1 (4).

Con `nu_j := ||x_j||_2 + ||y_j||_*`, de T1 (13),
`nu_{j+1} <= (1 + (a+c)/N) ||x_j||_2 + (rho_1 + rho_1 (a+c)/N) ||y_j||_*`,
con `a = C_P Theta`, `c = C_0 C_Q Theta`. Como `rho_1 < 1`, ambos
coeficientes son `<= 1 + kappa/N`, `kappa = a + c`, **para todo `N`** (no
se requiere `N >= N_0`; `rho_1 < 1` sólo se usa para que el coeficiente
de `||y_j||_*` no exceda `1`, y `rho_1 <= 1` bastaría aquí). Por tanto
`nu_j <= (1+kappa/N)^j nu_0 <= e^kappa nu_0` para `0 <= j <= N`.

**Dato inicial.** `s = F H_xi f`, `f = J(U_M - I) phi_N`, `||f|| <= 2`
(T1 (1)). En el soporte de Alice, `xi_* . (x - x_*) = sqrt(3) t_* (u^ . x - R) <= 0`
(`x_* = R u^`, `xi_* = sqrt(3) t_* u^`, `|x| <= R`), luego `||H_xi f|| <= ||f||` y
`||s||_2 <= 2`. `nu_0 <= (C_P + C_0 C_Q) ||s||_2`. Como
`t_j = x_j + y_j` y `||y||_2 <= ||y||_*`:

`||t_j||_2 <= nu_j <= e^kappa (C_P + C_0 C_Q) ||s||_2`, `kappa = Theta (C_P + C_0 C_Q)`.

Esto es el enunciado de §1 con `C(W,Theta) = (C_P+C_0 C_Q) e^{Theta (C_P+C_0 C_Q)}`.

**Formulación por norma equivalente (segunda vía).** Sobre todo `L^2`,
`nu(t) := ||P t||_2 + ||Q t||_*` cumple `||t||_2 <= nu(t) <= (C_P + C_0 C_Q) ||t||_2`,
y la tabla anterior afirma `||T||_{nu -> nu} <= 1 + kappa/N`; de ahí
`||T^j s||_2 <= (1+kappa/N)^j nu(s) <= e^kappa (C_P+C_0 C_Q) ||s||_2`, la
misma constante sin manejar la recurrencia acoplada. Se prueba
`sup_{j<=N} ||T^j|| < infinito`, no `||T^j|| -> 0`: el sector P no decae,
porque `m(0) = 1` en los saddles (`|m| <= 1` es exactamente lo que impide
crecimiento; una cota `rho(S) <= Lambda(1+eps)` con `eps` fijo daría
`e^{eps N}`).

**Controles.**
- `Theta = 0`: `E = 0`, `T = L`, `t_j = m^j x_0 + M^j y_0` y
  `||t_j||_2 <= ||x_0||_2 + C_0 rho_1^j ||y_0||_2 <= (C_P + C_0 C_Q) ||s||_2`,
  que coincide con la fórmula (y con `C_P + C_Q` no cerraría).
- Fibra de T1 (18) (saddle `p=0`, moneda constante, `a = theta/2`,
  `P = diag(1,0)`, `m = 1`, `L = diag(1, Lambda^-2)`,
  `I + E = [[cos a, -i sin a], [-i sin a, cos a]]`): la tabla da
  `A = cos a`, `B = -i sin a Lambda^-2`, `C = -i sin a`, `D = cos a Lambda^-2`,
  las cuatro entradas de `T` en (18). Es un contraste en una sola fibra:
  no dice nada sobre `P(p') Q(p)` con `p' != p` ni sobre las interfaces con
  `W^c`, que la cota `||E||_{2->2} <= Theta/N` paga globalmente.

**Sobre `W`.** `r_ext = max_K rho(D_xi/Lambda)` tiende a `1` al encoger `W`
(`K` se acerca a `Sigma`), y `C_P` crece al dilatar `W` hacia
`partial O_alpha` (el denominador `lambda - lambda^-1` en (3a) se degrada).
No hay uniformidad en `W` recuperable de esta prueba; cualquier uso con
`W = W_N` queda fuera de este enunciado.

## 5. Las tres reparaciones y la procedencia

Reparaciones incorporadas (las tres pedidas por el sanedrín):

1. Schur §2, (6): `||A_j|| <= 1 + C/N` es una cota **sobre `ran P`**, no sobre
   `L^2` entero (allí el bloque libre es `m P` con `||P||` posiblemente `> 1`).
   La premisa original `rho <= 1 + C/N => ||.|| <= 1 + C/N` se abandona.
2. Schur §2, antes de (5): el resolvente se controla por adjunta/determinante
   con dos ramas (`W` puntual, `K` compacto), no por continuidad de la
   familia partida.
3. `two-channel-reconstruction-operator-norms.md` §2: `nu_0` lleva
   `C_P + C_0 C_Q`, no `C_P + C_Q`.

Correcciones en los informes fuente: ver los avisos `[corregido 2026-09-25]`
en Schur §2 y en el informe de normas. Tras la revisión focalizada de §5 se
aplicaron además: `rho_1` fijado por convención, símbolo `lambda` del dato
inicial sustituido por `sqrt(3) t_*`, frase sobre compacidad recalibrada,
control de fibra T1 (18), cuantificador sobre `W` explícito.

Procedencia de las revisiones (herramientas: `~/herramientas` 18028a9,
`~/sanedrin` 8162508):

| Acta | Miembros (orden) | Resultado |
|---|---|---|
| `debates/2026-09-24--two-channel-stability-review.md` | Opus, ABNER | Opus `REPAIR_REQUIRED`; el turno de ABNER no llegó |
| `debates/2026-09-25--schur-repair-deepseek-review.md` | ABNER, Opus | ambos `PASS_WITH_REPAIRS`; ABNER: E5 no ejecutado, conclusión abierta hasta que conste E5 o la vía Dyson |
| `debates/2026-09-25--schur-repair-astra-review.md` | Astra (GPT), Ciro (Grok) | ambos `PASS_WITH_REPAIRS`; Astra ejecuta E5, Ciro la suscribe |
| `debates/2026-09-25--schur-e5-abner-check.md` | ABNER, Opus | ABNER `PASS` (E5 ejecutado; su objeción original queda cerrada), Opus `PASS`; sólo cuenta ABNER como independiente. Reparaciones menores (fijar `rho_1`, renombrar `lambda`, frase de compacidad, control T1 (18)) aplicadas arriba |

La vía Dyson de Opus (`||T^N|| <= C_1 e^{C_1 K_D Theta}`, con
`C_1 = sup_a ||T_0^a||`) no se usa aquí y sigue sin reproducir por otro
revisor.

## 6. Límites

- Esta nota es una derivación por escrito; no incluye comprobación
  numérica. Las identidades de bloque sólo se han contrastado en la fibra de
  T1 (18); `[UNVERIFIED]` numéricamente fuera de ella.
- La revisión cubrió exclusivamente §1–§4 (ABNER lo declara así); no cubrió
  interfaces con `W^c` en piezas físicas, ni Schur (7)–(8).
- Se usan como fuente `lem:specrad`, `lem:symbol` del TeX y T1 §§1–2, (3a),
  (4), (13) sin reabrirlos.
- No implica `||M_N|| = O_W(N^-1)` ni ninguna cota física; ninguna
  transferencia a los extremos físicos ni a `A_cP`, `A_cQ`.
```

### Contexto adjunto: reports/2026-09-25--flat-endpoint-l2-n3.md
```
# Extremos planos heredados: norma ℓ² inclinada O(N^{-3})

Fecha: 2026-09-25. Base: `863fe8e`. Autor de la derivación: Claude (familia
Anthropic).

Estado:

```text
FLAT_ENDPOINT_L2_N3_PASS — PRELIMINARY
```

Revisión: sanedrín de una ronda, sin turnos fallidos, con veredicto
`PASS_WITH_REPAIRS` por consenso. DeepSeek (abner) es el único revisor externo;
Opus es de la misma familia que el autor. Acta:
`debates/2026-09-25--flat-endpoint-l2-n3-review-opus-abner.md`. Hubo antes una
ejecución **incompleta**, con DeepSeek y Gemini caído, que se conserva solo como
registro y no como veredicto: `debates/2026-09-25--flat-endpoint-l2-n3-review.md`.
Las cuatro
reparaciones acordadas y la opcional sobre \(F_N\) están aplicadas aquí.

**Esto no es `N^{-7} PROVED`.** Ver §6.

## 1. Pregunta

¿Implican las fórmulas registradas, para los extremos planos heredados
\(f=s_Nb_N\chi\) y \(w=h_BM_Br\), la cota
\(\|f\|_{\ell^2_{\rm tilt}},\|w\|_{\ell^2_{\rm tilt}}=O(N^{-3})\), con
\[
\|f\|_{\ell^2_{\rm tilt}}^2=\sum_x e^{2\xi_*\cdot(x-x_*)}\|f(x)\|^2,\qquad
\|w\|_{\ell^2_{\rm tilt}}^2=\sum_y e^{-2\xi_*\cdot(y-y_*)}\|w(y)\|^2 ?
\]
La derivación no usa la masa ℓ¹ de `CURRENT_STATE` §9.2, la heurística
gaussiana \(\sqrt N\), el "soporte efectivo" ni el Lema 3 del informe regional.

## 2. Definiciones usadas

- `papers/ir-corona/ir-corona.tex` §3:
  \(\hat\phi_N(p)=Z_N^{-1/2}g(Np)\downarrow\), con \(g(q)=(1-|q|^2)_+^2\ge0\),
  \(Z_N=64/(3465\pi^2N^3)\) y \(d\mu=d^3p/(2\pi)^3\) (l. 282–284).
  \(F_N(x)=(1-16|x|^2/N^2)_+^2\), \(s_N=\sin(\pi F_N/2)\),
  \(h_N(y)=(1-16|y-Nu|^2/N^2)_+^2\) y \(M_B\in\{I,(I+\sigma_j)/2\}\).
- `reports/2026-09-17--regional-laplace-coefficient-gate.md` §3.2:
  \(x=x_*-\delta\hat u+u\), \(\delta=(\theta_N+j)/\sqrt3\),
  \(j\in\mathbb Z_{\ge0}\), \(\theta_N\in[0,1)\); Bob análogo con \(\delta'\).
  \(\xi_*\cdot(y-x)=N\xi_*\cdot v_*+t_*(2\theta_N+j+j')\), con
  \(t_*=0.735752\ldots>0\).
  §7: \(\varepsilon_\perp=\delta-\delta^2/2R-|u|^2/2R\), \(R=N/4\).
- `reports/2026-09-17--scaled-ir-signaling-gate.md` §3:
  \(|\phi_N(0)|^2=11/(140\pi^2N^3)\).

## 3. Cota puntual

**(a)** \(\phi_N=b_N\downarrow\) con
\(b_N(x)=Z_N^{-1/2}\int g(Np)e^{-ip\cdot x}d\mu\). Como \(g\ge0\),
\(\sup_{x\in\mathbb Z^3}|b_N(x)|=b_N(0)=c_\phi N^{-3/2}\), con
\(c_\phi=\sqrt{11/140}/\pi=0.08922\ldots\)

**(b)** \(r(y)=\int e^{-ip\cdot y}S(p)^N\hat\phi_N(p)d\mu\). \(S(p)\) es
unitaria en el toro real, luego \(\sup_y\|r(y)\|\le\int\|\hat\phi_N\|d\mu=c_\phi N^{-3/2}\).

**(c)** \(0\le F_N\le1\) por definición. Además
\(1-16|x|^2/N^2=(R^2-|x|^2)/R^2=8\varepsilon_\perp/N\), luego
\(F_N=64\varepsilon_\perp^2/N^2\) exactamente. Con
\(0\le\varepsilon_\perp\le\delta\):
\(|s_N|\le\tfrac\pi2F_N\le32\pi\delta^2/N^2\). En Bob,
\(h_N\le64\delta'^2/N^2\) y \(\|M_B\|\le1\).

**(d)** \(\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)\) y
\(-\xi_*\cdot(y-y_*)=-t_*(\theta_N+j')\). Con \(\delta\le(1+j)/\sqrt3\):
\[
e^{\xi_*\cdot(x-x_*)}\|f(x)\|\le a_f\,N^{-7/2}(1+j)^2e^{-t_*j},\qquad
e^{-\xi_*\cdot(y-y_*)}\|w(y)\|\le a_w\,N^{-7/2}(1+j')^2e^{-t_*j'},
\]
con \(a_f=\tfrac{32\pi}{3}c_\phi=2.990\ldots\) y
\(a_w=\tfrac{64}{3}c_\phi=1.903\ldots\). Las cotas son uniformes en \(u\) y
en \(N\); la dependencia en \(j\) queda explícita.

## 4. Suma cuadrática

Cada plano de profundidad \(j\) es un trasladado de
\(\Lambda_0=\mathbb Z^3\cap\{x_1+x_2+x_3=0\}\), con covolumen \(\sqrt3\) y
celda generada por \((1,-1,0)\) y \((0,1,-1)\). Tomamos el diámetro de la celda
como \(\sqrt6\), que es conservador. El soporte en el plano es un disco de radio
\(\rho_j\le\sqrt{2R\delta}\). Así, para \(N\ge1\),
\[
\#_j\le\frac{\pi(\rho_j+\sqrt6)^2}{\sqrt3}
\le\frac{2\pi}{\sqrt3}\Bigl(\frac{N(1+j)}{2\sqrt3}+6\Bigr)
\le k\,N(1+j),\qquad k=\frac{2\pi}{\sqrt3}\Bigl(\frac1{2\sqrt3}+6\Bigr).
\]
Por tanto
\[
\|f\|_{\ell^2_{\rm tilt}}^2\le k\,a_f^2\,N^{-6}\sum_{j\ge0}(1+j)^5e^{-2t_*j},
\qquad \sum_{j\ge0}(1+j)^5e^{-2t_*j}=51.48\ldots
\]
Es decir, \(q(j)=(1+j)^4e^{-2t_*j}\) con \(\sum(1+j)q(j)<\infty\).
Para \(N\ge1\):
\[
\boxed{\|f\|_{\ell^2_{\rm tilt}}\le103\,N^{-3},\qquad
\|w\|_{\ell^2_{\rm tilt}}\le66\,N^{-3}.}
\]
Las constantes son burdas y no óptimas; no hay cota inferior. Opus propuso una
saturación \(\gtrsim cN^{-6}\), que queda como [UNVERIFIED]: exige comprobar
\(\varphi_\partial\neq0\) en la capa \(j=1\).

## 5. Norma de Schur (8), componente P

Dyson §2 y Volterra usan \(D_\xi(\eta)=D(\eta-i\xi_*)\), los centros
\(x_*,y_*\), \(\Lambda=e^{\Phi_*}\) y \(K_*=\xi_*\cdot v_*-\Phi_*\). Con
\(\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x)\) y
\(d\mu=d^3p/(2\pi)^3\), Parseval da exactamente
\(\|\mathfrak A_f\|_{L^2(d\mu)}=\|f\|_{\ell^2_{\rm tilt}}\); igual para
\(\mathfrak B_w\). Las fases \(e^{i\eta\cdot x_*}\) y \(e^{-i\eta\cdot y_*}\) son
unimodulares.

Lo verificado se limita a la **componente P** que entra en (8):
\(\|P\mathfrak A_f\|_{L^2}\le C_P\|f\|_{\ell^2_{\rm tilt}}\), con
\(C_P=\sup_p\|P(p)\|<\infty\) (multiplicador acotado, Schur §2); igual para
Bob. No se afirma compatibilidad para la parte Q de los extremos: (8) no la
controla (T2).

## 6. Alcance y lo que no se afirma

- **Cubierto:** los extremos planos heredados \(f,w\).
- **No transferido al contrato de dos canales.** La fuente de T1 es
  \(J(U_M-I)\phi_N\); no se ha comprobado.
- **No transferido a \(r_c=BU_N^NJ\phi_N\).** El paso 3(b) usa la invariancia
  por traslación del walk libre. \(U_N\) contiene \(C_N(X)\), que no la tiene.
- **La cuenta \(N^{-3}\cdot N^{-1}\cdot N^{-3}\) no está instalada en ninguna
  pieza firmada del contrato actual.** T2 es `BOUND_NOT_TRANSFERRED`, T3 es
  `STOPPED_NO_SIGNED_TERM`, el extremo de Bob del observable es \(r_c\) y no
  \(w\), y Schur (8) es PRELIMINARY. El traslado distinto de
  `reports/2026-09-24--two-channel-reconstruction-operator-norms.md`
  (`CURRENT_STATE` §9.7) usa \(\|s\|\le2\) y el multiplicador de Bob, no esta
  cota. Es PRELIMINARY y su revisión dio `REPAIR_REQUIRED`; esta nota no lo
  modifica.
- **Margen nulo.** Aunque se instalara, \(e^{-K_*N}N^{-7}\) coincide con el
  resto absoluto ya presente en el líder plano: informe regional §13,
  \(|R_N|\le C'N^{-1/2}\) sobre \(e^{-K_*N}N^{-13/2}\), con \(C'\) no explícita.
  La holgura frente a ese resto es \(N^0\). Una corrección \(O(N^{-7})\) queda
  por debajo del líder, pero no por debajo del resto conocido.

No se ejecutó código salvo el cálculo aritmético de \(a_f,a_w,k\) y de la serie.
No se modifican Schur, Volterra, H1c, T1–T3 ni las piezas lineales.
```

### Contexto adjunto: reports/2026-09-24--two-channel-t1-exact-signed-pq.md
```
# T1: lift exacto firmado de los dos canales al P/Q inclinado

Fecha: 2026-09-24. Base inspeccionada: `d8ca7b285129b8b29a304e232195e29f20095526`.
Estado: `T1: PASS`.
Review status: `INDEPENDENT_ADVERSARIAL_REVIEW_PASS`.
La revisión reparada de Claude Opus y DeepSeek V4-Pro acepta T1 en el
contrato y el W fijado aquí. El expediente y sus límites están en
`debates/2026-09-24--two-channel-t1-rereview.md`. El primer intento quedó
degradado porque Gemini falló por falta de crédito; no se cuenta como
consenso ni como evidencia a favor o en contra.
El snapshot matemático adjunto a la re-revisión tiene SHA256
`dc076059935d9b814c17f69390f202187768f75dfad30c9d912033c4c6d487ee`.
Después del dictamen se incorporó a este informe la relación local
\(\beta P=Q\beta\), recomendada y derivada en los turnos de revisión.

Los revisores comprobaron de forma separada el signo \(p-i\xi_*\), el
factor exacto \(e^{-K_*N}\), la fórmula de cinco piezas, los adjuntos,
la recurrencia Volterra y el control acoplado. No encontraron error en
las identidades de T1. Opus retiró sus reparaciones obligatorias iniciales
tras verificar la versión reparada; DeepSeek discrepó de su objeción
residual sobre una supuesta independencia necesaria de las etiquetas.
El acuerdo es `T1_PASS` dentro del contrato explícito y para cada W
admisible fijo de §2. El pase no evalúa escalas, uniformidad en W ni
las afirmaciones analíticas preliminares. Los controles (17)–(18) sólo
verifican las identidades de bloques en una fibra; no controlan
\(P(p')Q(p)\) a momentos distintos ni las interfaces con \(W^c\).
Ambos revisores recomiendan dejar ese límite registrado para T2.

La re-revisión fue un sanedrín deliberativo de una ronda, Claude Opus
(Anthropic) y DeepSeek V4-Pro (DeepSeek); el segundo tuvo acceso al turno
de Opus. Es revisión independiente del autor por dos familias, no dos
juicios ciegos ni revisión humana. Commit de la herramienta sanedrín:
`8162508e3bd0e3d05770b4dd544fe7c962d0272c`.
Alcance: T1 de `state/CURRENT_STATE.md`, §9.6, por instrucción del usuario.
No se ejecutan T2 ni T3. No se modifica el estado canónico.

## 1. Definiciones y procedencia

Se usan como definiciones del problema el contrato de dos canales de
`reports/2026-09-24--h1c-return-kernel-schur-audit.md`, §6, y la partición
auxiliar de su §2. Las identidades siguientes se derivan aquí; no se toman
las conclusiones analíticas de los prechecks como premisas probadas.
El índice `biblioteca/INDICE.md` fue inspeccionado; no se utiliza ningún
resultado bibliográfico para esta expansión algebraica.

Sean
\[
Jv=(v,0),\qquad D=S\oplus S^{-1},\qquad
U_N=C_ND,\quad C_N(x)=e^{-i\vartheta(x/N)\beta/N},
\quad \beta=\sigma_x\otimes I_2.
\]
Los perfiles, la preparación y los efectos son los de
`papers/ir-corona/ir-corona.tex`, §3. Se fija cualquier entero \(N\ge2\),
cualquiera de los cuatro encoders \(M\) y cualquiera de los cuatro
detectores \(M_B\) del contrato. El perfil real \(\vartheta\) conserva
las hipótesis del contrato H1. El producto interno es antilineal en el
primer argumento. Para \(c\in\{+,-\}\), \(\pi_c\) extrae el canal y
\[
F_c=\pi_c^*E\pi_c,\qquad E=h_N\otimes M_B.
\]
Definimos la referencia física y la perturbación de Alice **completas**:
\[
r=U_N^NJ\phi_N=\Psi_0,\qquad
f=J(U_M-I)\phi_N,\qquad d=U_N^Nf.
\tag{1}
\]
Así \(\Psi_b=r+b d\) para ambos bits \(b=0,1\). No se sustituye
\(r\) por la referencia plana. En particular,
\[
f=J\bigl(c_N\phi_N+i s_N M\phi_N\bigr),\quad
c_N=\cos(\pi F_N/2)-1,\quad s_N=\sin(\pi F_N/2).
\]
No se descarta la parte \(c_N\), ni ninguna contribución cuadrática.
Como \(U_M-I\) está soportado en Alice, \(f\) tiene soporte finito.

La expansión directa del POVM da, sin aproximaciones,
\[
\boxed{L_c=2\operatorname{Re}\langle r,F_cd\rangle
                 +\langle d,F_cd\rangle.}
\tag{2}
\]
Esto ya incluye la sustracción exacta de la probabilidad del bit cero.

## 2. La partición existente y el lift bien definido

Se mantiene la construcción de ventanas del precheck de Schur,
explicitando su cuantificador. Sean \(O_\alpha\) vecindades espectrales
de los ocho saddles \(\alpha\in\Sigma=\{0,\pi\}^3\), en el toro,
en las que existe una rama continua dominante \(\lambda_\alpha\),
con \(|\lambda_\alpha|>1\). Se fija, una vez para T1–T3, una familia
de vecindades abiertas \(W_\alpha\ni\alpha\) con cierres disjuntos
y \(\overline{W_\alpha}\subset O_\alpha\). Se define
\(W=\bigcup_\alpha W_\alpha\), independiente de N, del encoder,
del detector y del perfil de moneda.

Estas vecindades existen directamente para el símbolo explícito del
TeX: en cada saddle \(\tfrac12\operatorname{tr}S\) es
\(\pm\prod_j\cosh(\xi_{*,j})\), de módulo mayor que uno, mientras
\(\det S=1\). Las dos raíces del polinomio característico son
distintas y una tiene módulo mayor que uno. Por continuidad, la
separación persiste en vecindades pequeñas con cierres en ese dominio.
Ésta es la condición de admisibilidad de W usada aquí.

Para cada W así fijado, las identidades siguientes son exactas. Las
piezas se entienden como \(A_{cP}^{(W)},\ldots,B_{cPQ}^{(W)}\), aunque
se suprima el superíndice. No se fija un radio numérico ni se afirma
independencia de las piezas respecto de W: es una descomposición relativa
a un parámetro auxiliar fijo. Toda cota posterior deberá retener esa
dependencia, salvo prueba separada de uniformidad. No se permite elegir
\(W=W_N\) ni reajustarlo para mejorar una pieza.

Si \(p_S(p)\) es el Riesz idempotente de \(S(p-i\xi_*)\)
para la raíz dominante \(\lambda(p)\) en una ventana, entonces
\[
P(p)=
\begin{cases}
\operatorname{diag}(p_S(p),I_2-p_S(p)),&p\in W,\\
0,&p\notin W,
\end{cases}
\qquad Q=I-P.
\tag{3}
\]
En efecto, \(S^{-1}\) tiene autovalor \(\lambda\) en el subespacio
de \(S\) con autovalor \(\lambda^{-1}\). Se entiende (3) como
multiplicadores acotados en \(\mathscr H=L^2(\mathbb T^3;\mathbb C^4)\).
Sólo se usa \(P^2=P\), \(Q^2=Q\), \(P+Q=I\) y \(PQ=QP=0\).
No se presupone \(P^*=P\).

La acotación no requiere un radio efectivo. En cada cierre de ventana,
\[
p_S(p)=\frac{S(p-i\xi_*)-\lambda_\alpha(p)^{-1}I_2}
                    {\lambda_\alpha(p)-\lambda_\alpha(p)^{-1}}.
\tag{3a}
\]
El numerador es continuo y el denominador está separado de cero en
ese compacto. Hay sólo ocho ventanas; fuera de ellas P=0. Por tanto
\(\operatorname*{ess\,sup}_p\|P(p)\|\le C_P(W)<\infty\), y lo
mismo vale para Q=I-P. Los saltos en la frontera no afectan a esta
acotación de multiplicadores L2, y siguen presentes en los bloques.

Estos P/Q son los del símbolo **inclinado**. No son los canales
\(+/-\), ni el corte IR \(\Pi'\) del frente C2/C3. Ambos canales
tienen componentes en P y en Q dentro de las ventanas. El exterior
permanece en Q, con todas sus transiciones.

Hay, sin embargo, una relación entre las transiciones locales y los
canales que conviene dejar a la vista. En W, usando la convención del
contrato \(\beta=\sigma_x\otimes I_2\),
\[
\beta P(p)=Q(p)\beta,\qquad P(p)\beta=\beta Q(p),
\qquad p\in W.
\tag{3b}
\]
Se comprueba por bloques a partir de (3); requiere que W use la misma
ventana para los dos bloques recíprocos, como se ha fijado aquí.
Así, para moneda constante y una fibra individual, una transición
P\(\leftrightarrow\)Q mediante \(\beta\) conmuta los canales
\(+\leftrightarrow-\) a la vez. Fuera de W esta identidad no se afirma:
P=0 y Q=I allí. La identidad de cinco piezas no requiere que esos
mecanismos sean independientes; el control (18) comprueba la recurrencia
con acoplamiento en una fibra, pero no prueba el efecto de \(P(p')Q(p)\)
para \(p'\ne p\) ni los cruces con el exterior de W. Esas cantidades
quedan para el trazado de T2, no se estiman aquí.

Para justificar el lift sin inclinar la preparación de cola espacial
infinita, basta inclinar \(f\). Con la convención de Fourier del TeX,
\[
(\mathcal Fv)(p)=\sum_xe^{ip\cdot x}v(x),\qquad
(\mathcal F^{-1}z)(y)=\int e^{-ip\cdot y}z(p)\,d\mu(p),
\]
sean
\[
(H_\xi v)(x)=e^{\xi_*\cdot(x-x_*)}v(x),\quad
s=\mathcal F H_\xi f,\quad \Lambda=e^{\Phi_*},\quad
T=\Lambda^{-1}\mathcal F H_\xi U_NH_\xi^{-1}\mathcal F^{-1}.
\tag{4}
\]
La conjugación se define primero en vectores de soporte finito.
Como \(U_N\) tiene alcance finito y moneda local acotada, el operador
inclinado así obtenido tiene una extensión acotada en \(\mathscr H\).
La moneda conmuta con \(H_\xi\); el bloque libre es
\(D_\xi(p)=D(p-i\xi_*)\). Por tanto T es precisamente el paso
normalizado del precheck, con sus saltos de momento, no otro propagador.

Para cada \(0\le j\le N\),
\[
t_j=T^js=\Lambda^{-j}\mathcal F H_\xi U_N^jf.
\tag{5}
\]
Esta identidad se comprueba por inducción. Todos los \(U_N^jf\)
tienen soporte finito. No se necesita que \(H_\xi r\) o
\(H_\xi\phi_N\) pertenezcan a \(\ell^2\).

Sean \(B\) la restricción espacial a Bob y
\[
(\mathcal Vz)(y)=\mathbf1_{\mathcal B_N}(y)
 e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}z)(y),\qquad
\mathcal V_c=\pi_c\mathcal V.
\tag{6}
\]
Para cada N fijo esta aplicación está bien definida sobre \(L^2\),
pues Bob tiene soporte finito. Más explícitamente, \(\mathcal V\) es
la composición de la inversa de Fourier unitaria con el multiplicador
\(\mathbf1_{\mathcal B_N}(y)e^{-\xi_*\cdot(y-y_*)}\), cuyo máximo
es finito. Como \(0\le E\le I\) y \(\pi_c\) es acotado,
\(\mathcal H_c=\mathcal V_c^*E\mathcal V_c\) es un operador
acotado, positivo y autoadjunto. Este argumento sólo asegura que
los objetos existen para N fijo; no transfiere cotas asintóticas.
Con los centros y escala ya fijados,
\(y_*-x_*=Nv_*\) y \(K_*=\xi_*\cdot v_*-\Phi_*\), (5) da
\[
Bd=e^{-K_*N}\mathcal Vt_N.
\tag{7}
\]
El factor se obtiene exactamente de
\(\Lambda^Ne^{-\xi_*\cdot(y-x_*)}
=e^{-K_*N}e^{-\xi_*\cdot(y-y_*)}\).
Extraerlo no es una estimación del tamaño de los factores restantes.

Definimos las dos contribuciones de **salida**:
\[
d_{c,P}=e^{-K_*N}\mathcal V_cPt_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_cQt_N,\qquad
B\pi_cd=d_{c,P}+d_{c,Q}.
\tag{8}
\]
Son amplitudes en Bob. No se afirma que desinclinar por separado
P y Q produzca vectores globales en el Hilbert físico. La restricción
en (6) evita exigir esa propiedad, innecesaria para el efecto local.

## 3. Expresión firmada completa para cada canal

Escribiendo \(r_c=B\pi_cr\), las probabilidades de ambos bits son
\[
p_{c,0}=\langle r_c,Er_c\rangle,
\qquad
p_{c,1}=\langle r_c+d_{c,P}+d_{c,Q},
                 E(r_c+d_{c,P}+d_{c,Q})\rangle.
\tag{9}
\]
Al restarlas:
\[
\boxed{\begin{aligned}
L_c={}&2\operatorname{Re}\langle r_c,E d_{c,P}\rangle
      +2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle\\
 &+\langle d_{c,P},E d_{c,P}\rangle
  +\langle d_{c,Q},E d_{c,Q}\rangle
  +2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\quad c=+,-.
\end{aligned}}
\tag{10}
\]
Ésta es la fórmula de T1. No contiene normas ni valores absolutos de
las respuestas. Los dos términos cuadráticos diagonales son reales
y no negativos; los términos de interferencia conservan sus signos.

Por indicación del usuario, se congela el siguiente vocabulario para T2,
con cinco contribuciones por canal:
\[
\begin{aligned}
A_{cP}&=2\operatorname{Re}\langle r_c,E d_{c,P}\rangle,\\
A_{cQ}&=2\operatorname{Re}\langle r_c,E d_{c,Q}\rangle,\\
B_{cPP}&=\langle d_{c,P},E d_{c,P}\rangle,\\
B_{cQQ}&=\langle d_{c,Q},E d_{c,Q}\rangle,\\
B_{cPQ}&=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle,
\end{aligned}
\qquad
\boxed{L_c=A_{cP}+A_{cQ}+B_{cPP}+B_{cQQ}+B_{cPQ}.}
\tag{10a}
\]
Estas etiquetas designan escalares del observable. No son los bloques
de transporte \(A_j,B_j\) de §4 ni nuevos proyectores.

Si se llama
\[
L_{c,A}=2\operatorname{Re}\langle r_c,E d_{c,A}\rangle
              +\langle d_{c,A},E d_{c,A}\rangle\quad(A=P,Q),
\]
entonces la identidad es
\[
L_c=L_{c,P}+L_{c,Q}+L_{c,\mathrm{cross}},\qquad
L_{c,\mathrm{cross}}=2\operatorname{Re}\langle d_{c,P},E d_{c,Q}\rangle.
\tag{11}
\]
La aditividad de sólo dos términos requiere que este último escalar
sea cero para los datos considerados; T1 no establece tal anulación.
Repartirlo por convenio entre P y Q no demostraría una separación física.

En la representación auxiliar, sea
\[
\mathcal H_c=\mathcal V_c^*E\mathcal V_c,\qquad
\ell_c(z)=\langle r_c,E\mathcal V_cz\rangle.
\]
La misma fórmula, antes de agrupar términos conjugados, es
\[
\begin{aligned}
L_c={}&e^{-K_*N}\{
\ell_c(Pt_N)+\overline{\ell_c(Pt_N)}
+\ell_c(Qt_N)+\overline{\ell_c(Qt_N)}\}\\
&+e^{-2K_*N}\sum_{A,B\in\{P,Q\}}
  \langle t_N,A^*\mathcal H_c B t_N\rangle.
\end{aligned}
\tag{12}
\]
Aquí \(PQ=0\) no elimina \(P^*\mathcal H_cQ\). El efecto de Bob,
la reconstrucción y los adjuntos permanecen en su lugar. Incluso una
partición ortogonal no permitiría ese paso sin una condición adicional
sobre el efecto. El extremo lineal es exactamente el determinado por
\(w_c=F_cr\), soportado en Bob y dependiente de \(U_N\).

## 4. Compatibilidad con los bloques temporales existentes

No se estima ni se reabre la vía Volterra. Sólo se sustituyen los datos
de (4) en sus identidades finitas. Con \(x_j=Pt_j\), \(y_j=Qt_j\),
\[
A_j=PTP,\quad B_j=PTQ,\quad C_j=QTP,\quad D_j=QTQ,
\]
\[
x_{j+1}=A_jx_j+B_jy_j,\qquad
y_{j+1}=C_jx_j+D_jy_j,\qquad (x_0,y_0)=(Ps,Qs).
\tag{13}
\]
Los subíndices se conservan para coincidir con el precheck; en este
protocolo el paso T es el mismo en todas las capas. Los productos
vacíos son las identidades de los respectivos rangos.

Con \(\Phi_P(j,k)=A_{j-1}\cdots A_k\) y
\(G_Q(j,k)=D_{j-1}\cdots D_k\), la sustitución sucesiva de (13) da
\[
\begin{aligned}
x_N={}&\underbrace{\Phi_P(N,0)Ps}_{\text{trayectoria siempre en P}}\\
 &+\underbrace{\sum_{m=0}^{N-1}
 \Phi_P(N,m+1)B_mG_Q(m,0)Qs}_{f_{Q,N}}\\
 &+\underbrace{\sum_{m=0}^{N-1}\sum_{k=0}^{m-1}
 \Phi_P(N,m+1)B_mG_Q(m,k+1)C_kx_k}_{(\mathbb M_Nx)_N},\\
y_N={}&G_Q(N,0)Qs+
 \sum_{k=0}^{N-1}G_Q(N,k+1)C_kx_k.
\end{aligned}
\tag{14}
\]
Se verifica (14) primero resolviendo la segunda recurrencia de (13),
y sustituyéndola en la primera con su transporte \(\Phi_P\).
Así, los objetos de (8) son exactamente
\[
d_{c,P}=e^{-K_*N}\mathcal V_c x_N,\qquad
d_{c,Q}=e^{-K_*N}\mathcal V_c y_N.
\tag{15}
\]
La contribución que termina en P incluye retornos y entradas desde Q:
no es la contribución que permaneció siempre en P. Esta última es
únicamente el primer sumando de \(x_N\) en (14).

Si \(d_{c,0}\) denota la reconstrucción de ese primer sumando y
\(\delta d_c=d_{c,P}+d_{c,Q}-d_{c,0}\), la respuesta respecto de
esa amplitud, **manteniendo la referencia física r**, satisface
\[
\begin{aligned}
L_{c,0}&=2\operatorname{Re}\langle r_c,E d_{c,0}\rangle
                 +\langle d_{c,0},E d_{c,0}\rangle,\\
L_c-L_{c,0}&=2\operatorname{Re}\langle r_c+d_{c,0},E\delta d_c\rangle
                      +\langle\delta d_c,E\delta d_c\rangle.
\end{aligned}
\tag{16}
\]
Esto identifica el funcional exacto al que entrarían las correcciones
de (14); no les asigna potencia, pequeñez ni dominancia relativa.
Tampoco define una dinámica alternativa para el bit cero.

## 5. Comprobaciones internas por otra formulación y caso límite

**Segunda derivación, mediante la diferencia de estados.** Si
\(v=J\phi_N\), la diferencia inicial es exactamente
\[
\Delta=|v+f\rangle\langle v+f|-|v\rangle\langle v|
=|f\rangle\langle v|+|v\rangle\langle f|+|f\rangle\langle f|.
\]
Al conjugar por \(U_N^N\) y tomar la traza contra \(F_c\), los
dos primeros sumandos dan los términos lineales de (2) y el tercero
da su término cuadrático. Sustituir (8) genera las cuatro parejas
\(PP,PQ,QP,QQ\) de (12), incluidos ambos adjuntos cruzados.
Es la misma identidad obtenida desde las probabilidades (9).

**Control plano.** Si \(\vartheta=0\), T es diagonal por canales,
y también lo son P y Q de (3). Como \(f=J(U_M-I)\phi_N\),
\(r_-=d_{-,P}=d_{-,Q}=0\). Por (10), \(L_-=0\). En el canal
positivo \(r_+=BS^N\phi_N\) y
\(d_{+,P}+d_{+,Q}=BS^N(U_M-I)\phi_N\), por lo que (10) recupera
exactamente \(L_+=L_{\rm plano}\), para los dieciséis pares.
Este control verifica la reconstrucción, sin afirmar que se anule
el cruce P/Q dentro del canal positivo.

**Control acoplado de las recurrencias.** Para N=2 y bloques genéricos,
la multiplicación directa de dos matrices de bloques da
\[
\begin{aligned}
x_2&=A_1A_0x_0+A_1B_0y_0+B_1C_0x_0+B_1D_0y_0,\\
y_2&=C_1A_0x_0+C_1B_0y_0+D_1C_0x_0+D_1D_0y_0.
\end{aligned}
\tag{17}
\]
Por otra vía, (14) da
\(f_{Q,2}=A_1B_0y_0+B_1D_0y_0\),
\((\mathbb M_2x)_2=B_1C_0x_0\) y
\(y_2=D_1D_0y_0+D_1C_0x_0+C_1x_1\), con
\(x_1=A_0x_0+B_0y_0\). Esto reproduce (17) sin suponer que los
acoplamientos se anulen.

Un caso concreto con retorno no nulo es la fibra del saddle p=0,
restringida a un par intercambiado por beta, con moneda constante.
En la base donde \(D_\xi=\operatorname{diag}(\Lambda,\Lambda^{-1})\)
y \(\beta=\sigma_x\), para \(a=\theta/2\),
\[
T=\begin{pmatrix}
\cos a&-i\sin a\,\Lambda^{-2}\\
-i\sin a&\cos a\,\Lambda^{-2}
\end{pmatrix},\qquad P=\operatorname{diag}(1,0).
\tag{18}
\]
Si \(\sin a\ne0\), B y C son no nulos y
\(BC=-\sin^2a\,\Lambda^{-2}\). Para \((x_0,y_0)=(1,0)\),
\[
x_2=\cos^2a-\sin^2a\,\Lambda^{-2},\qquad
y_2=-i\sin a\cos a\,(1+\Lambda^{-2}),
\]
tanto por \(T^2\) como por (17). La diferencia de \(x_2\) respecto
de la trayectoria siempre P es exactamente BC. Es un test algebraico
de fibra; no se identifica un estado de una sola fibra con la preparación
normalizada del protocolo ni se amplía la clase de perfiles físicos.

**Control nulo.** Si en un test se toma \(U_{\rm enc}=I\), entonces
\(f=s=0\) y ambos bits preparan el mismo estado; todos los términos
de (10) son cero para cualquier moneda. No confundirlo con M=I:
el encoder congelado correspondiente es \(e^{i\pi F_N/2}I\ne I\).
Es un control algebraico, no una ampliación de la familia de encoders.

**POVM completo.** La unitariedad física y la normalización de ambos
bits dan \(L_\varnothing=-L_+-L_-\). La suma inclusiva conserva los
términos cruzados de (10) para ambos canales; T1 no demuestra que
se anulen en esa suma. No se infiere \(L_++L_-=0\).

## 6. Resultado y techo

T1 produce un observable firmado exacto compatible con el P/Q existente:
(10), con datos físicos (1), lift (4)–(8) y bloques (13)–(15).
La referencia y los dos bits están incluidos sin imponer una nueva
hipótesis de decaimiento exponencial a la preparación. El STOP por
incompatibilidad algebraica de T1 no se activa en esta derivación.

La derivación y sus controles son internos: no constituyen revisión
independiente ni promoción de un gate canónico. Sigue pendiente T2:
este documento no identifica un coeficiente de orden \(N^{-6}\),
no transfiere cotas de extremos y no demuestra una relación entre
los dos canales. T3 tampoco se ejecuta. H1/H1c, la justificación física,
E0, POWER_13/2_STABILITY, E/AdS y el manuscrito conservan su estado.

No se ha ejecutado código científico ni generado datos numéricos.
La procedencia de las fórmulas nuevas es su derivación explícita en
este archivo; los prechecks aportan la notación y el contrato, no una
certificación de sus estimaciones previas.

## 7. T2: alcance fijado, ejecución pendiente

Orden obligatorio por instrucción del usuario:
T1 → revisión independiente y cierre de sus reparaciones → T2 → T3.
No se ejecuta T2 mientras la versión reparada esté pendiente de revisión.

La pregunta es qué contribución, o sub-contribución identificada, hereda
realmente el techo previo \(O(N^{-6})\). No se asigna de antemano ese
orden a ninguna de las diez piezas de (10a).

T2 deberá producir diez filas, una por cada
\(A_{+P},A_{+Q},B_{+PP},B_{+QQ},B_{+PQ}\) y
\(A_{-P},A_{-Q},B_{-PP},B_{-QQ},B_{-PQ}\), con estos campos:

| Campo | Contenido requerido |
| --- | --- |
| Objeto previo | Fórmula y localización precisa del bloque o extremo que se pretende usar; distinguir pieza completa y sub-contribución. |
| Cota disponible | Enunciado, hipótesis, ámbito, dependencia en W fijo y nivel de revisión; marcar explícitamente cuando no haya transferencia justificada o uniformidad en W. |
| Información perdida | Signos, fases, interferencias o dependencia de la referencia que desaparecieron al tomar normas. |
| Escala resultante | Factores exponenciales y potencias de N, indicando si se trata del observable físico o de una cantidad normalizada; distinguir cota superior y término asintótico identificado. |

El producto \(N^{-5/2}N^{-1}N^{-5/2}=N^{-6}\) sólo proporciona
un recuento de cotas hasta que se identifique el elemento bilineal,
sus extremos físicos y su lugar exacto en (10a). Las cotas heredadas
para extremos planos no se transfieren automáticamente a \(r_c\).
P/Q final tampoco etiqueta el número de excursiones: se conserva (14).

No se introduce ninguna técnica nueva. Si una transferencia no está
justificada por lo ya disponible, se registra esa carencia sin abrir
una nueva vía de estimación. T2 no busca simetrías ni ejecuta T3.

Para cualquier posterior afirmación de cancelación, se mantendrán
separados estos tres niveles:

1. Dentro de una pieza de (10a).
2. Entre piezas de un mismo canal.
3. Entre canales, en \(L_++L_-\).

El tercer nivel no prueba cancelación en ninguno de los dos canales
por separado. El número de piezas que reciban una misma cota tampoco
decide por sí solo si hay una relación estructural.

Si T2 sólo recupera una cota gruesa sin coeficiente identificado, la
conclusión será que \(N^{-6}\) sigue siendo un techo sin término
asintótico aislado. Eso no prueba que un término de ese orden sea
inexistente, ni que su coeficiente sea cero. En ese caso se aplica el
STOP previsto: no buscar simetrías de un coeficiente no identificado.
```

### Contexto adjunto: reports/2026-09-24--two-channel-reconstruction-operator-norms.md
```
# Norma de la reconstrucción física P/Q sobre la salida normalizada

Fecha: 2026-09-24. Estado: `BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM`
al nivel **PRELIMINARY**, condicionado al lema de bloques Schur §2.
Alcance: sólo las cuatro normas
`||E^{1/2} V_c P t_N||`, `||E^{1/2} V_c Q t_N||`, `c=+,-`, y su uso
inmediato para acotar las diez piezas por Cauchy–Schwarz. No se cambia
Volterra, no se buscan cancelaciones y no se identifican términos líderes.

Este informe actualiza el resultado de la primera auditoría
`reports/2026-09-24--two-channel-physical-bound-transfer-audit.md`:
el STOP inicial localizó correctamente las normas que faltaban; la
presente estimación, usando la geometría explícita del efecto de Bob y
las cotas de bloques ya escritas, cierra ese hueco como cota superior.

## 1. Norma exacta del operador de reconstrucción

Del contrato en T1, §§2 y (6)–(8),
\[
(\mathcal V_c z)(y)=\mathbf1_{\mathcal B_N}(y)
e^{-\xi_*\cdot(y-y_*)}(\mathcal F^{-1}\pi_c z)(y),
\quad
d_{c,P/Q}=e^{-K_*N}\mathcal V_c(P/Q)t_N.
\]
El efecto del TeX plano, §3 y la definición del perfil Bob, es
\[
E=h_N\otimes M_B,\quad \|M_B\|=1,\quad
h_N(y)=\left(1-\frac{|y-Nu|^2}{R^2}\right)_+^2,
\quad R=N/4,\quad u=(1,1,1).
\]
Además, su representación inclinada fija
\(y_*=Nu-R\widehat u\), \(\widehat u=u/\sqrt3\), y
\(\xi_*=t_*u=\lambda\widehat u\), \(\lambda=\sqrt3t_*>0\).
Estas posiciones están en `papers/ir-corona/ir-corona.tex`, §§3,
exact tilted representation, y en T1 (6)–(8).

Como Fourier y la extracción de un canal tienen norma uno,
\[
\|E^{1/2}\mathcal V_c\|
=m_N:=\sup_{y\in\mathbb Z^3}
\sqrt{h_N(y)}e^{-\xi_*\cdot(y-y_*)}.
\]
Esta igualdad usa que \(M_B\) tiene autovalor máximo uno y que el
dominio permite cualquier función de Fourier L² en el canal elegido.
Para un y dentro de Bob, ponga
\(s=\widehat u\cdot(y-y_*)\) y descomponga
\(y-Nu=(s-R)\widehat u+q\), con \(q\perp\widehat u\). La condición
\(|y-Nu|\le R\) da \(0\le s\le2R\), y
\[
\sqrt{h_N(y)}
=\left(1-\frac{(s-R)^2+|q|^2}{R^2}\right)_+
\le \frac{2s}{R}-\frac{s^2}{R^2}
\le \frac{2s}{R}.
\]
Por ello
\[
0\le m_N\le\sup_{s\ge0}\frac{2s}{R}e^{-\lambda s}
=\frac{2}{e\lambda R}=\frac{8}{e\sqrt3t_*}\,N^{-1}.
\tag{1}
\]
El orden \(N^{-1}\) es ajustado para el operador sin P/Q: elija puntos
de red sobre la diagonal \(y=(m,m,m)\) con
\(s=\sqrt3(m-(y_*)_1)\) en un intervalo fijo positivo, por ejemplo
\([\sqrt3,2\sqrt3]\). Para N grande están dentro de Bob, con \(q=0\),
\(\sqrt{h_N}\ge c/N\), y el factor exponencial es uniformemente
positivo. Así \(m_N=\Theta(N^{-1})\). El factor exponencial de
desinclinación no hace crecer la norma: en la cara enfrentada donde
el peso sería máximo, \(h_N\) se anula; dentro, el peso decae.

Para W admisible y fijo, T1 §2 da
\(C_P(W)=\|P\|_{L^2\to L^2}<\infty\) y
\(C_Q(W)=\|Q\|_{L^2\to L^2}<\infty\), independientes de N. Por (1),
\[
\boxed{\|E^{1/2}\mathcal V_cP\|\le C_P(W)m_N=O_W(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQ\|\le C_Q(W)m_N=O_W(N^{-1}).}
\tag{2}
\]
Vale para ambos canales. No se afirma una cota inferior para ninguna
composición con P o Q.

## 2. Norma del vector normalizado actual

La fuente exacta T1 §1 es
\(s=\mathcal F H_\xi f\), con
\(f=J(U_M-I)\phi_N\), \(\|f\|\le2\), soportada en Alice.
Alice es la bola de radio R centrada en el origen y
\(x_*=R\widehat u\). Para todo x de Alice,
\(\xi_*\cdot(x-x_*)\le0\); luego el multiplicador \(H_\xi\) tiene
norma a lo sumo uno sobre el soporte de f y
\[
\|s\|_2=\|H_\xi f\|_2\le2.
\tag{3}
\]

No hace falta estimar Volterra. Se usan directamente las cotas de
bloques ya establecidas en la auditoría Schur, §2, ecuación (6): en
las normas P=L² y Q=\(\|\cdot\|_*\), uniformemente para N grande,
\[
\|A_j\|\le1+C/N,\quad \|B_j\|,\|C_j\|\le C/N,
\quad \|D_j\|_*\le\rho_2<1.
\]
(**[corregido 2026-09-25]** \(A_j\) sobre \(\operatorname{ran}P\), y los
bloques como aplicaciones entre rangos; ver
`2026-09-25--schur-block-stability-repaired.md`.)
En la norma producto \(\|x\|_2+\|y\|_*\), la recurrencia T1 (13)
queda acotada por \(1+C'/N\) paso a paso (absorbiendo la contracción
\(\rho_2\) y los dos bloques cruzados \(O(N^{-1})\)). Iterar N pasos
da una constante independiente de N. El dato inicial satisface
\(\nu_0=\|Ps\|_2+\|Qs\|_*\le(C_P(W)+C_0(W)C_Q(W))\|s\|\)
**[corregido 2026-09-25: la versión anterior, con \(C_P+C_Q\), ignoraba
la constante \(C_0\) de la norma \(\|\cdot\|_*\)]**. Por tanto
\[
\boxed{\|t_N\|_2\le C_{\rm stab}(W,\Theta)\|s\|_2
=O_{W,\Theta}(1),\quad\|\vartheta\|_\infty\le\Theta.}
\tag{4}
\]
Ésta es sólo estabilidad L² del producto ya normalizado, que sale de
las cotas de bloques Schur; no es una nueva cota de memoria ni una
afirmación sobre historias individuales. **[actualizado 2026-09-25]** La estabilidad (4) tiene ahora revisión
independiente documentada (ABNER/DeepSeek `PASS`; Astra/Ciro
`PASS_WITH_REPAIRS`, reparaciones aplicadas; ver
`2026-09-25--schur-block-stability-repaired.md` §5), con
\(O_{W,\Theta}(1)\) en lugar de \(O_W(1)\). Esa revisión se limitó a
(4); (5), (6) y las cotas por pieza que usan t_N son consecuencias
inmediatas de (2) y (4) que no se revisaron expresamente y conservan el
rótulo `PRELIMINARY`. En
cambio (1) y (2) son cotas operatoriales directas de la definición
geométrica, condicionadas sólo a W fijo y a la acotación P/Q de T1.

De (2) y (4), para c=+ y c=-,
\[
\boxed{\|E^{1/2}\mathcal V_cPt_N\|=O_{W,\Theta}(N^{-1}),\qquad
\|E^{1/2}\mathcal V_cQt_N\|=O_{W,\Theta}(N^{-1}).}
\tag{5}
\]
Al volver a las amplitudes físicas,
\[
\boxed{\|E^{1/2}d_{c,P}\|,
\|E^{1/2}d_{c,Q}\|=O_W(N^{-1}e^{-K_*N}).}
\tag{6}
\]
La fuente de la potencia \(N^{-1}\) es la norma del multiplicador
Bob ponderado en (1), no el antiguo retorno \(\mathbb M_N\) ni una
proyección de saddle. La cota es superior; no hay lower bound ni
asintótica equivalente para los vectores concretos \(t_N\).

## 3. Transferencia inmediata a las diez piezas

La unitariedad física y \(0\le E\le I\) dan
\(\|E^{1/2}r_c\|\le1\). Aplicando Cauchy–Schwarz a las identidades
exactas T1 (10a), sin cambiar los signos de las definiciones:
\[
|A_{cP}|,|A_{cQ}|=O_W(N^{-1}e^{-K_*N}),
\]
\[
0\le B_{cPP},B_{cQQ}=O_W(N^{-2}e^{-2K_*N}),\qquad
|B_{cPQ}|=O_W(N^{-2}e^{-2K_*N}),
\quad c=+,-.
\]
Estas son cotas superiores uniformes en N para W fijo, **condicionales
al lema de estabilidad preliminar Schur §2**; no se promueven a
`ESTABLISHED`. No son \(\sim\), no contienen lower bounds y no
identifican `LEADING_ASYMPTOTIC_TERM`. En particular, el operador bound no atribuye al observable el antiguo
\(O(N^{-6})\), que dependía de otros extremos y otro sandwich.

| TERM | BOUND | SOURCE | ASSUMPTIONS | EXPONENTIAL_SCALE | POWER_OF_N | SIGNED_INFORMATION_RETAINED | LOST_BY_ABSOLUTE_VALUE | STATUS |
|---|---|---|---|---|---|---|---|---|
| `A_{+P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{+Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{+PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-P}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` en identidad | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `A_{-Q}` | `O_W(N^-1 e^-K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; P→Q incluido; Schur §2 | `e^-K*N` | `N^-1` upper only | `Re` | C–S pierde signo/fase | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PP}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; W fijo; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-QQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | igual; borde Q sin historia separada; Schur §2 | `e^-2K*N` | `N^-2` upper only | no negativo exacto | cota no identifica tamaño | `PRELIMINARY_BOUNDS_TRANSFERRED` |
| `B_{-PQ}` | `O_W(N^-2 e^-2K*N)` upper bound, preliminary | (1)–(6), T1 (10a) | E efecto; ambas salidas; Schur §2 | `e^-2K*N` | `N^-2` upper only | `Re` y signo | C–S pierde fase relativa | `PRELIMINARY_BOUNDS_TRANSFERRED` |

Memoria Q: ambas salidas P contienen entradas/retornos desde Q; la salida
Q contiene Q inicial y las salidas desde P, con historia de retornos en
los \(x_k\) (T1 (14)). La tabla no separa una contribución de
“permanencia P” ni atribuye historias. El mismo bound operatorial cubre
ambos canales porque extracción de canal tiene norma uno; no suma ni
cancela \(L_+\) y \(L_-\).

## 4. Límite de la conclusión

Los términos lineales tienen una envolvente exponencial menos pequeña
que la de los cuadráticos. Eso los hace candidatos naturales si una
lower bound posterior los mantiene en esa escala; la auditoría no prueba
dominancia, porque todos los resultados aquí son cotas superiores y
pueden ser estrictamente no ajustados. No se abre esa pregunta ahora.

```text
PRELIMINARY: BOUNDS_TRANSFERRED / NO_SIGNED_LEADING_TERM
```

No se ejecutaron scripts ni barridos. No se modificó el manuscrito.
No se hizo commit ni push.
```

### Contexto adjunto: reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md
```
# H1 inhomogeneous localization — reconstruction and gate ledger

Date: 2026-09-20
Branch: \`research/b-infinity-post-s4-gate\`
Status: **research note / H1 remains OPEN**

## 0. Scope and locks

This note records the latest reconstruction of the inhomogeneous H1 front. It does not reopen the flat paper.

Locked and untouched:
- \`E0 = OPEN_AT_STOP\`.
- \`POWER_13/2_STABILITY = OPEN_AT_STOP\`.
- AdS / inhomogeneous extension \`E = STOPPED_UNPROVEN\`.

## 1. Operator contract

Use
\[
D(z)=S(z)\oplus S(z)^{-1},\qquad
C_N(X)=\exp[-i\vartheta(X)\beta/N],
\qquad
A_N(X,z)=C_N(X)D(z).
\]

Working beta contract:
\[
\beta=\sigma_x\otimes I_2,\quad \beta^2=I,\quad \beta D\beta=D^{-1}.
\]

The original-source gamma-matrix convention is not re-certified here.

## 2. H1-SR

Let \(\mathcal P\) be the dominant rank-two Riesz bundle and \(Q=I-\mathcal P\). Since beta exchanges the lambda and inverse-lambda sectors,
\[
\mathcal P\beta\mathcal P=0.
\]

Therefore the first-order frozen intrabundle compression vanishes; dominant feedback starts at \(O(N^{-2})\) per step and can accumulate to \(O(N^{-1})\). The frozen dominant projector may shift by \(O(N^{-1})\).

\[
\boxed{\texttt{H1-SR = PROVED_UNDER_FROZEN_BETA_CONTRACT}}.
\]

## 3. H1a and H1b

On fixed neighborhoods of the eight relevant maxima, choose the dominant root with \(|\lambda|>1\). Compactness gives a uniform local gap. Since
\[
A_N-D=O(N^{-1}),
\]
common local Riesz contours persist and
\[
P_N-P=O(N^{-1}).
\]
For bounded lattice steps,
\[
A_N(X+e/N)-A_N(X)=O(N^{-2}),
\quad
P_N(X+e/N)-P_N(X)=O(N^{-2}).
\]

\[
\boxed{\texttt{H1a = PROOF_WRITTEN / UNREVIEWED}}.
\]

No global torus gap is claimed.

For nearby idempotents \(P,Q\), use
\[
T(Q,P)=QP+(I-Q)(I-P),
\quad QT=TP,
\quad T-I=(Q-P)(2P-I).
\]
Then \(T^{\pm1}=I+O(N^{-1})\), while consecutive frames differ by \(O(N^{-2})\). After conjugation to a fixed bundle, the frozen symbol is exactly block diagonal. The complementary block contracts relatively by a uniform local factor \(\rho<1\). With H1-SR the dominant product is
\[
\lambda^N[I+O(N^{-1})].
\]

\[
\boxed{\texttt{H1b = PROOF_WRITTEN / UNREVIEWED}}.
\]

## 4. Derivative selection rule

For the Fourier-coordinate insertion,
\[
\mathcal P Y_j\beta\mathcal P
=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
(up to Fourier sign convention), using
\[
\mathcal P(\partial_j\mathcal P)\mathcal P=0,
\qquad
\mathcal P\beta\mathcal P=0.
\]
Thus
\[
\mathcal G_j(z)=i\mathcal P\beta(\partial_j\mathcal P)\mathcal P
\]
is a uniformly bounded analytic local amplitude by the Riesz formula.

\[
\boxed{\texttt{DERIVATIVE_SELECTION_RULE = PASS}}.
\]

## 5. Alice/Bob absolute layer scale recovered from the primary report

Verified against \`reports/2026-09-17--regional-laplace-coefficient-gate.md\`.

The layer lemma uses the complete endpoint spinors
\[
f=s_N b_N\chi,\qquad w=h_B M_B r,
\]
before spectral projection.

The report gives
\[
b_N=O(N^{-3/2}),\qquad
r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2}),
\]
and
\[
s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6}),
\qquad
h_B=\frac{64}{N^2}{\varepsilon'_\perp}^{\,2}.
\]

At normal depth \(j\), the tangential area is \(O(N(1+j))\), while the tilted normal factor is exponentially summable, of the form \(e^{-t_*(\theta_N+j)}\). Hence, without phase cancellation,
\[
\sum_x e^{\xi_*\cdot(x-x_*)}\|f(x)\|=O(N^{-5/2}),
\]
\[
\sum_y e^{-\xi_*\cdot(y-y_*)}\|w(y)\|=O(N^{-5/2}).
\]
Therefore
\[
\sup_\eta\|\mathfrak A_f(\eta)\|=O(N^{-5/2}),
\qquad
\sup_\eta\|\mathfrak B_w(\eta)\|=O(N^{-5/2}).
\]

This is an absolute full-spinor bound, not a dominant-bundle bound.

The same report records a tangential Poisson correction \(O(N^{-4})\) against the \(N^{-5/2}\) Alice scale, i.e. relative \(O(N^{-3/2})\).

\[
\boxed{\texttt{LAYER_ABSOLUTE_MASS_BOUND = PASS}}.
\]

## 6. G insertion: local-window stability

Inside a fixed saddle neighborhood, \(\mathcal G_j\) is uniformly bounded. With \(\vartheta\in C^1\), the accumulated intrabundle insertion is \(O(N^{-1})\). Combining endpoint bounds and the three-dimensional Gaussian factor:
\[
N^{-1}N^{-5/2}N^{-5/2}N^{-3/2}=N^{-15/2}.
\]
This is below the flat absolute remainder \(O(N^{-7})\).

\[
\boxed{\texttt{G_INSERTION_POWER_STABILITY = PASS_IN_LOCAL_WINDOW}}.
\]

No global localization statement is implied.

## 7. Final Q leakage: corrected local estimate

An earlier exploratory \(O(N^{-8})\) count omitted the zeroth-order coin term
\[
-\frac{i}{N}\vartheta(\bar X_k)\beta.
\]
Its \(\mathcal P\beta\mathcal P\) compression vanishes, but \(Q\beta\mathcal P\) need not. In the frozen-frame analysis this appears as the \(O(N^{-1})\) change of basis/projector,
\[
\mathcal P_N=\mathcal P+O(N^{-1}).
\]

Because the primary layer estimate bounds the complete Bob spinor,
\[
\|\mathfrak B_w(\eta)Q(\eta)\|
\le \|\mathfrak B_w(\eta)\|\,\|Q(\eta)\|
=O(N^{-5/2})
\]
uniformly on a local Riesz neighborhood.

Thus the safe local matrix-element estimate is
\[
|\Delta T_Q|\lesssim N^{-1}N^{-13/2}=O(N^{-15/2}).
\]
The linear-in-eta leakage has an additional Gaussian gain and is smaller.

\[
\boxed{\texttt{FINAL_Q_LEAKAGE_MATRIX_ELEMENT = PASS_IN_LOCAL_WINDOW}}.
\]

No calculation of a leading \(B_{Q,\sigma}^{(0)}\) coefficient is needed for this upper-bound gate.

## 8. H1c reformulation

A finite-range path carries individual hopping matrices \(D_h\), not the full symbol \(D(z)\), so literal pathwise use of H1b is invalid.

\[
\boxed{\texttt{H1c_GLOBAL = UNNECESSARY}},
\qquad
\boxed{\texttt{H1c_LOCALIZED = OPEN}}.
\]

The remaining bottleneck is
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

The required result concerns the exact tilted Alice/Bob matrix element, not merely an operator norm.

## 9. Candidate route for L': absolute Dyson expansion in momentum

**Status: unverified proposal, not a proved lemma.**

Schematically,
\[
C_N-I=-\frac{i}{N}\vartheta(x/N)\beta+O(N^{-2}).
\]
In Fourier space the leading perturbation is convolution with
\[
K_N(q)=N^3\widehat\vartheta(Nq)
\]
(up to Fourier normalization).

For nearby dominant bundles,
\[
\mathcal P(\eta+q)\beta\mathcal P(\eta)
=
[\mathcal P(\eta+q)-\mathcal P(\eta)]\beta\mathcal P(\eta),
\]
so locally
\[
\|\mathcal P(\eta+q)\beta\mathcal P(\eta)\|\le C|q|.
\]

Kernel moments:
\[
\int |K_N(q)|dq=\int|\widehat\vartheta(p)|dp,
\]
\[
\int |q||K_N(q)|dq
=\frac1N\int|p||\widehat\vartheta(p)|dp.
\]
Hence a candidate intrabundle Dyson insertion costs
\[
\frac1N\int |q||K_N(q)|dq=O(N^{-2}),
\]
provided
\[
\int_{\mathbb R^3}(1+|p|)|\widehat\vartheta(p)|dp<\infty.
\]

After summing insertion times, the hoped-for effective gain is \(O(N^{-1})\) per insertion. The target is
\[
e^{-N\varphi_*}|T_n|
\le C N^{-13/2}\frac{(C'/N)^n}{n!}.
\]

### Unresolved step (ii)

This Dyson estimate is **not proved**. The delicate point is uniform control of variable-momentum chains
\[
\eta_0\to\eta_1\to\cdots\to\eta_n,
\qquad q_j=\eta_j-\eta_{j-1},
\]
because the walk is non-normal and both spectral radii and Riesz projectors vary with momentum.

A proof must control dominant-bundle products after extracting the global tilted rate, chains visiting \(Q\), transitions among the eight saddle neighborhoods, and passages through regions where the local Riesz splitting is unavailable. It may not assume momentum conservation or the flat localization statement that L' is intended to replace.

Until that step is written and independently checked,
\[
\boxed{\texttt{H1c_LOCALIZATION (L') = OPEN}}.
\]

## 10. Current ledger

| Gate | Status |
|---|---|
| H1-SR | PROVED_UNDER_FROZEN_BETA_CONTRACT |
| H1a | PROOF_WRITTEN / UNREVIEWED |
| H1b | PROOF_WRITTEN / UNREVIEWED |
| DERIVATIVE_SELECTION_RULE | PASS |
| LAYER_ABSOLUTE_MASS_BOUND | PASS |
| G_INSERTION_POWER_STABILITY | PASS_IN_LOCAL_WINDOW |
| FINAL_Q_LEAKAGE_MATRIX_ELEMENT | PASS_IN_LOCAL_WINDOW |
| H1c_GLOBAL | UNNECESSARY |
| H1c_LOCALIZED | OPEN |
| H1c_LOCALIZATION (L') | OPEN |
| H1 | OPEN |
| E0 | OPEN_AT_STOP — untouched |
| POWER_13/2_STABILITY | OPEN_AT_STOP — untouched |
| E / AdS extension | STOPPED_UNPROVEN — not reactivated |

## 11. Next admissible step

Write and audit the missing dominant-transport estimate for the momentum-space Dyson chain. Do not promote L', H1c, or H1 until the non-normal variable-momentum product in step (ii) is controlled.

No further inference is authorized by this note.
```

### Contexto adjunto: papers/ir-corona/ir-corona.tex
```
\documentclass[11pt]{amsart}

\usepackage[margin=1.1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\Z}{\mathbb{Z}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\T}{\mathbb{T}}
\newcommand{\cA}{\mathcal{A}}
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cK}{\mathcal{K}}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\up}{{\uparrow}}
\newcommand{\dn}{{\downarrow}}
\newcommand{\Cmicro}{C_{\mathrm{micro}}}
\newcommand{\cIR}{c_{\mathrm{IR}}}
\newcommand{\arcosh}{\operatorname{arcosh}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Tr}{\operatorname{Tr}}
\newcommand{\Hess}{\operatorname{Hess}}
\newcommand{\re}{\operatorname{Re}}
\newcommand{\im}{\operatorname{Im}}
\newcommand{\vstar}{v_*}
\newcommand{\xistar}{\xi_*}
\newcommand{\uhat}{\hat u}

\begin{document}

\title[Infrared response outside the emergent light cone]{An infrared operational response outside the emergent light cone of a three-dimensional Weyl quantum walk}

% TODO(author): any AI-assistance disclosure required by the target journal.
\author{Jos\'e Ignacio Mart\'in Gandul}
\address{Independent Researcher, Seville, Spain}
\email{adnacho@gmail.com}

\date{\today}

\begin{abstract}
In a finite-range quantum walk the relativistic light cone that emerges at
long wavelength need not exhaust the strict microscopic causal support.  We
study the three-dimensional Weyl walk introduced by Cedzich, Joye, Werner and
Werner as a model with a spherical propagation region.  All of its group
velocities lie in the closed Euclidean unit ball, which is also the light
cone of its Weyl node.  Its one-step causal support is the cube $[-1,1]^3$.
Velocities in the cube but outside the ball form a \emph{corona}.  There,
propagation is non-ballistic but not causally forbidden.

We ask whether the corona carries an operational response that survives
infrared control.  Alice prepares a narrow-band state and applies a local
encoding, and Bob reads out with a local detector.  All three operations are
required to be infrared-admissible: acting on the band $|p|\le N^{-1}$, each
produces only a vanishing fraction of its output outside the wider band
$|p|\le N^{-1/2}$.  Bob's
region lies outside the emergent light cone of every site of Alice's region.
After $N$ steps, Bob's distinguishability $\delta(N)$ obeys the explicit
bound $\delta(N)\le 36N^4e^{-JN}$ with $J=(1-\sqrt3/2)\log 2$.  For a concrete
family of sixteen encoder--detector pairs, it has the exact leading
asymptotics
\[
\delta(N)=\bigl|C(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\qquad \theta_N=\{\sqrt3N/4\}.
\]
Here $K_*\approx0.1905$ is the value of a Legendre rate function at a unique
regional minimiser.  The coefficient $C(\theta)$ is given in closed form, and
interval arithmetic shows that it does not vanish for any $\theta$ in any of
the sixteen pairs.  The emergent cone is therefore not operationally sharp,
even for infrared-admissible operations.  The response is non-perturbatively
small, invisible to every power of the infrared scale, and it lies strictly
inside the microscopic causal support.  The result is purely asymptotic: the
remainder constants are not explicit, and numerical diagnostics indicate
that the leading term is quantitatively accurate only for $N$ of order
$10^3$ and beyond.
\end{abstract}

\maketitle

\section{Introduction}\label{sec:intro}

Quantum cellular automata and quantum walks are unitary dynamics on a lattice
with a strict bound on the speed of propagation
\cite{SchumacherWerner,Arrighi,Farrelly}.  After $N$ steps of a finite-range
walk, the propagator vanishes identically outside $N\Cmicro$.  Here
$\Cmicro=\operatorname{conv}F$ is the convex hull of the one-step jumps.
Many such walks have a conical point in their dispersion relation.  Near it,
the long-wavelength dynamics is that of a Weyl or Dirac equation with a
speed of light $\cIR$
\cite{BialynickiBirula,DArianoPerinotti,BDPT,DArianoErbaPerinotti}.

In spatial dimension $d\ge2$ the two causal structures cannot coincide.  The
infrared cone of a Weyl node is a Euclidean ball, and $\Cmicro$ is a
polytope.  Exact isotropy of the microscopic causal structure is incompatible
with a regular lattice.  It can be compatible with random discreteness, as in
the causal-set theorem of Bombelli, Henson and Sorkin \cite{BHS}, but that
setting lies outside the scope of this paper.  For a lattice walk, some
velocities are therefore causally allowed but not relativistic.  How much
physics can be sent through them?

Three questions must be kept apart.

\begin{description}
\item[(U) Ultraviolet propagator] Does the exact kernel assign non-zero
  amplitude to sites outside the infrared ball but inside $N\Cmicro$?  For
  the walk studied here it does: along the eight vertex rays a single
  lattice path contributes, with amplitude of norm $4^{-N}$
  (Proposition~\ref{prop:geometry}).  One-step Alice/Bob protocols built
  from localized operations turn this into a finite distinguishability
  (for instance $3/128$ after one step for a suitable localized
  preparation, as recorded in~\cite{Repo}).  Such protocols are broadband:
  their operations are not concentrated near the Weyl node.
\item[(I) Infrared operational response] Require the preparation, the
  encoder and the detector to be infrared-admissible, and put Bob outside
  the infrared cone of \emph{every} site of Alice.  Does Bob's
  distinguishability still fail to vanish as the infrared scale goes to
  zero, and at what rate?
\item[(N) Nature] Is there a physical system in which the lattice scale and
  the operations are given rather than engineered?  This question is not
  addressed here.
\end{description}

A non-zero ultraviolet kernel does not answer (I).  Infrared admissibility
could in principle force exact cancellations, and conversely an exponentially
small infrared response is compatible with (U).  This paper answers (I), for
one walk and one explicit protocol.

\subsection*{The walk}
We work with the Weyl walk of Cedzich, Joye, Werner and Werner
\cite[Eq.~(5.15)]{CJWW}.  They introduced it as a modification of the
Bialynicki-Birula Weyl automaton \cite[Eq.~(5.12)]{CJWW},
\cite{BialynickiBirula}, with the same conical points and with a
\emph{spherical} propagation region.  For this walk the three velocity sets
are nested as
\begin{equation}\label{eq:three-bodies}
\Gamma\;\subseteq\;B(1)\;\subsetneq\;\Cmicro=[-1,1]^3,
\qquad \sup_{v\in\Gamma}|v|=\cIR=1 .
\end{equation}
Here $B(1)=\overline B(0,1)$ is the closed infrared light cone ($\cIR=1$),
$\Gamma$ is the closed set of group velocities, and $\Cmicro$ is the strict
causal body.  Both statements in \eqref{eq:three-bodies} are exact, and
moreover $\partial B(1)\subseteq\Gamma$ (Proposition~\ref{prop:geometry}).
Numerically, $\Gamma$ fills the ball; this is not proved and not used.
Every ballistic mode, at every energy, therefore respects the emergent light
speed.  Nevertheless, in every non-axial direction $\hat n$ the causal
support extends to $\|\hat n\|_1\in(1,\sqrt3\,]$ times the light speed.
Probability outside $\Gamma$ is exponentially small in $N$ \cite{CJWW}.  The
question is whether it can be \emph{used} under infrared control.

\subsection*{Main results}
Section~\ref{sec:protocol} gives the precise definitions.  In outline,
Alice's region is the lattice ball $\cA_N$ of radius $N/4$ at the origin,
and Bob's region is the lattice ball $\cB_N$ of radius $N/4$ at $N(1,1,1)$.
After $N$ steps, every pair $(x,y)\in\cA_N\times\cB_N$ is separated by more
than $N+N/5$.  Bob is thus outside the emergent cone of every site of
Alice, with a margin of order $N$.  The resource is a narrow-band packet of
momentum width $\Lambda=1/N$.  Alice's encoder is a smooth local unitary
$\exp(i\frac\pi2F_N(x)M)$ with $M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$.  Bob's
effect is $h_N(y)\otimes M_B$ with $M_B\in\{I,(I+\sigma_j)/2\}$.  The
profiles $F_N,h_N$ are smooth bumps of width $N/4$ that vanish quadratically
on the spheres.

\begin{enumerate}[label=(\roman*)]
\item \emph{Infrared admissibility} (Theorem~\ref{thm:admissible}).  All
  eight operations map the band $|p|\le N^{-1}$ into the band
  $|p|\le N^{-1/2}$, up to relative errors $O(N^{-1/2})$ with explicit
  constants.  Single-site operations fail this criterion maximally
  (Lemma~\ref{lem:point}).
\item \emph{Explicit upper bound} (Theorem~\ref{thm:upper}).  For every
  $N\ge2$, every unitary acting in $\cA_N$, every one-particle state and
  every effect in $\cB_N$, Bob's distinguishability is at most
  $36N^4e^{-JN}$, with $J=(1-\tfrac{\sqrt3}{2})\log2$.  Polynomial infrared
  signalling is excluded.
\item \emph{Regional rate} (Theorem~\ref{thm:rate}).  The kernel between
  the two regions is $O(N^4)\,e^{-K_*N}$, where $K_*=I(v_*)$ is the minimal
  regional value of a Legendre rate function.  Here $I$ is the Legendre
  transform of $\Phi(\xi)=\arcosh(\prod_j\cosh\xi_j)$, and
  $v_*=(1-\frac1{2\sqrt3})(1,1,1)$ is the unique minimiser of $I$ over the
  regional velocity set.  Moreover $J<K_*<\log4$.  By (iv), the rate $K_*$
  is attained by an explicit response.
\item \emph{Leading asymptotics} (Theorem~\ref{thm:main}).  For all sixteen
  encoder--detector pairs,
  $\delta_{M,M_B}(N)=|C_{M,M_B}(\theta_N)|N^{-13/2}e^{-K_*N}(1+O(N^{-1/2}))$.
  The coefficient $C_{M,M_B}(\theta)$ is given in closed form and is
  uniformly non-zero, with relative oscillation in $\theta$ at most
  $1.5\times10^{-3}$.
\end{enumerate}

Result (iv) is an asymptotic statement and not a numerical approximation
valid from small $N$.  The constants in its remainder are not explicit, and
neither is the threshold $N_*$ beyond which $\delta_{M,M_B}(N)>0$ is
guaranteed.  Finite-$N$ diagnostics (Appendix~\ref{app:numerics}) indicate
a relative correction of about $-100/N$, so the leading term is
quantitatively accurate only for $N\gtrsim10^3$.  For the pairs with the
smallest coefficients, the next-order term $N^{-17/2}e^{-K_*N}$ dominates
throughout the diagnostic range $N\le56$ (Remark~\ref{rem:features}).

The coefficient is not a product of local factors.  It arises from the
interference between the \emph{free tail} of the resource at Bob, which is
only polynomially small, and the part of Alice's encoding that reaches Bob,
which is exponentially small.  Two points of the complex-shifted Brillouin
torus contribute, and they enter with different projectors.  The power
$13/2$ is not a count of Gaussian directions.  The two normal directions are
discrete sums over lattice planes of depth $O(1)$, and the common tangential
direction is a flat direction of the exponent that is confined only by the
profiles.

\subsection*{Relation to the literature}
Ballistic scaling and weak limit theorems for translation-invariant quantum
walks are classical \cite{Konno,GJS,AVWW}: $Q(t)/t$ converges in
distribution to the group velocity distributed by the initial state.
Cedzich, Joye, Werner and Werner \cite{CJWW} proved that the probability of
velocities outside the support of this limit decays exponentially.  They gave
a method for bounding the rate uniformly in the initial state and discussed
the ``fuzziness'' of the emergent light cone in exactly this language.  Our
upper bound (ii) uses their contour-shift idea, supplemented by an elementary
ellipse lemma and a Jordan-safe bound on matrix powers.  Their method bounds
rates; it does not give prefactor-level asymptotics.

Sharp asymptotics with prefactors outside the propagation region are known
in one dimension.  Sunada and Tate \cite{SunadaTate} obtained exact local
asymptotics of transition probabilities, including exponential decay with an
explicit prefactor in the region hidden from the weak limit.  Carteret,
Richmond and Temme \cite{CRT} obtained uniformly convergent asymptotics in
the exponentially decaying regions of coined walks on the line.  These are
the closest precursors of the saddle-point analysis of
Section~\ref{sec:asymptotics}.  In two dimensions, Baryshnikov, Brady,
Bressler and Pemantle \cite{BBBP} analysed quantum walks through multivariate
generating functions and determined the limiting profile in the feasible
region, outside of which the probability is exponentially small.  Analytic
combinatorics in several variables \cite{ACSV} provides general transfer
theorems for multivariate coefficient asymptotics, whose standard sharp
forms assume minimality hypotheses on the critical points.  We do not claim
that these methods cannot reproduce the present result.  We are not aware of
a transfer theorem that yields it directly, and we carry out the
model-specific saddle-point analysis explicitly.

What we add is a \emph{lower} bound, in the strong form of exact leading
asymptotics.  It concerns an \emph{operational} quantity: the
distinguishability produced by a local encoding.  The encoding is spread
over a region of size $O(N)$ and constrained to be infrared-admissible, in
dimension three, and at a point strictly inside the corona.  Upper bounds
alone cannot distinguish an exponentially small response from an exactly
vanishing one.  In the problem studied here that distinction is the
content of the result.  The novelty claim is correspondingly narrow.  To our
knowledge, Theorem~\ref{thm:main} is the first prefactor-level asymptotic,
with a leading coefficient that is oscillatory and certified to be
non-vanishing, for an infrared-controlled operational response in the
strictly outside-propagation-region regime of a three-dimensional
multi-component quantum walk.  Exponential decay outside the propagation
region, large-deviation rates, Weyl-cone dispersion and microscopic support
outside an emergent cone all have prior art, cited above.

Lieb--Robinson bounds \cite{LiebRobinson,BHV} give exponentially small
leakage outside a linear cone for continuous-time lattice dynamics.  For
quantum walks the strict cone $\Cmicro$ plays that role exactly, and the
question here is the one \emph{inside} it.

\subsection*{Organisation}
Section~\ref{sec:walk} sets up the walk and proves the geometric statements.
Section~\ref{sec:protocol} defines the protocol and infrared admissibility.
Section~\ref{sec:results} states the results.  Sections~\ref{sec:upper}
to~\ref{sec:asymptotics} contain the proofs.  Section~\ref{sec:discussion}
discusses scope and limitations.  Appendix~\ref{app:numerics} lists the
computer-assisted parts and the finite-$N$ diagnostics.

\section{The walk and its three velocity sets}\label{sec:walk}

\subsection{Conventions}
The one-particle Hilbert space is $\mathcal H=\ell^2(\Z^3;\C^2)$ with
internal basis $\up=(1,0)^T$ and $\dn=(0,1)^T$.  We use the Fourier
transform $\hat\psi(p)=\sum_{x}e^{ip\cdot x}\psi(x)$, with inverse
$\psi(x)=\int_{\T^3}e^{-ip\cdot x}\hat\psi(p)\,d\mu(p)$ and
$d\mu=d^3p/(2\pi)^3$ on $\T^3=[-\pi,\pi)^3$.  We write $c_j=\cos p_j$ and
$s_j=\sin p_j$.  $B(1)=\overline B(0,1)$ denotes the closed Euclidean unit
ball.

The walk $W$ of \cite[Eq.~(5.15)]{CJWW} has symbol
\[
W(p)=\begin{pmatrix} c_1c_2e^{ip_3} & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2e^{-ip_3}\end{pmatrix},
\qquad \det W(p)=1 .
\]
States evolve by the unitary $S$ with symbol
\begin{equation}\label{eq:symbol}
S(p)=W(p)^{-1}=\begin{pmatrix} c_1c_2e^{-ip_3} & c_1s_2-is_1\\ -c_1s_2-is_1 & c_1c_2e^{ip_3}\end{pmatrix}.
\end{equation}
Both are matrix-valued trigonometric polynomials, so they extend to entire
functions of $p\in\C^3$.  For $p\in\C^3$, $S(p)$ denotes the continuation of
\eqref{eq:symbol}, which is the inverse of $W(p)$ and not its adjoint.
Writing $S(p)=\sum_dS_de^{ip\cdot d}$, the walk acts as
$(S\psi)(y)=\sum_dS_d\psi(y-d)$.  The $N$-step kernel is
\begin{equation}\label{eq:kernel}
(S^N)_{y,x}=G_N(y-x),\qquad G_N(d)=\int_{\T^3}e^{-ip\cdot d}S(p)^N\,d\mu(p).
\end{equation}

\begin{lemma}[Jumps]\label{lem:jumps}
The set $F=\{d:S_d\ne0\}$ has fourteen elements: the eight vertices
$(\pm1,\pm1,\pm1)$, the four face diagonals $(\pm1,\pm1,0)$, and the two
axial jumps $(\pm1,0,0)$.  Each vertex block is $\frac14$ times a rank-one
diagonal projector; in particular $S_{(1,1,1)}=\frac14|\dn\rangle\langle\dn|$.
The face-diagonal blocks have norm $\frac14$ and the axial blocks have norm
$\frac12$, so that $\sum_d\|S_d\|=4$.
\end{lemma}

\begin{proof}
This is a direct expansion of \eqref{eq:symbol} in $z_j=e^{ip_j}$.  The
coefficient of $z_1z_2z_3$ comes only from the $(2,2)$ entry
$c_1c_2e^{ip_3}$ and equals $\frac14$.
\end{proof}

\subsection{Dispersion and the infrared node}
Since $\det S=1$ and $\tr S(p)=2c_1c_2c_3$, the eigenvalues of $S(p)$ are
$e^{\mp i\omega(p)}$ with
\begin{equation}\label{eq:dispersion}
\cos\omega(p)=\cos p_1\cos p_2\cos p_3 .
\end{equation}
At $p=0$ one has $S(p)=I-iH_W(p)+O(|p|^2)$ with
\[
H_W(p)=p_1\sigma_1-p_2\sigma_2+p_3\sigma_3,\qquad H_W(p)^2=|p|^2I .
\]
This is a Weyl Hamiltonian with speed $\cIR=1$.  The same conical structure
occurs at the eight points of $\{0,\pi\}^3$.

\begin{proposition}[Geometry]\label{prop:geometry}
\begin{enumerate}[label=(\alph*)]
\item The causal body is $\Cmicro=\operatorname{conv}F=[-1,1]^3$.  Its
  support function is $h_{\Cmicro}(\hat n)=\|\hat n\|_1$ for unit vectors
  $\hat n$.
\item At every $p$ where $\omega$ is differentiable,
  \begin{equation}\label{eq:SOS}
  \bigl(1-f^2\bigr)-|\nabla f|^2=s_2^2s_3^2+s_1^2s_2^2c_3^2+s_1^2c_2^2s_3^2\ \ge0,
  \qquad f=c_1c_2c_3,
  \end{equation}
  and hence $|\nabla\omega(p)|\le1$.  At the conical points $\nabla\omega$
  takes every value in the unit sphere.  Thus $\Gamma\subseteq B(1)$ and
  $\partial B(1)\subseteq\Gamma$, where $\Gamma$ is the closure of the set
  of group velocities.
\item For every vertex $\sigma\in\{\pm1\}^3$ and every $N\ge1$,
  $(S^N)_{N\sigma,0}=S_\sigma^N=4^{-N}\Pi_\sigma\ne0$, where $\Pi_\sigma$ is
  a diagonal rank-one projector.  In particular
  $(S^N)_{(N,N,N),0}=4^{-N}|\dn\rangle\langle\dn|$.  Hence the $N$-step
  support function equals $N\|\hat n\|_1$ exactly.
\end{enumerate}
\end{proposition}

\begin{proof}
(a) follows from Lemma~\ref{lem:jumps}.  The supremum of $\hat n\cdot x$ over
the cube is separable and equals $\sum_j|n_j|$.

(b) With $\cos\omega=f$ we have $\nabla\omega=-\nabla f/\sin\omega$ and
$\sin^2\omega=1-f^2$.  The identity \eqref{eq:SOS} is a polynomial identity
in $(c_j,s_j)$ modulo $c_j^2+s_j^2=1$, and is checked by expansion.  Near a
conical point, $\omega(p)=|p-p_\vee|+O(|p-p_\vee|^2)$, so
$\nabla\omega=(p-p_\vee)/|p-p_\vee|+o(1)$ sweeps the unit sphere.

(c) Let $d_1+\dots+d_N=N\sigma$ with $d_k\in F$.  Every $d\in F$ satisfies
$\sigma_i d_i\le1$ for each coordinate $i$, so
$\sum_k\sigma_i(d_k)_i=N$ forces $\sigma_i(d_k)_i=1$ for all $i$ and $k$,
that is, $d_k=\sigma$.  Hence $(S^N)_{N\sigma,0}=S_\sigma^N$.  By Lemma~\ref{lem:jumps},
$S_\sigma=\frac14\Pi_\sigma$, so $S_\sigma^N=4^{-N}\Pi_\sigma$.
\end{proof}

\begin{remark}
The reverse inclusion $B(1)\subseteq\Gamma$, that is, that $\Gamma$ fills
the ball, holds numerically but is not proved and not used.  What is used is
the exact inclusion $\Gamma\subseteq B(1)$, equivalently
$\sup|\nabla\omega|\le\cIR$, with equality by $\partial B(1)\subseteq\Gamma$.  Consequently the relation
$\sup|v_g|=\cIR$ does \emph{not} imply that the emergent cone coincides with
the causal boundary.  The two coincide only in the six axial directions.
The \emph{corona} is $\Cmicro\setminus B(1)$.  Propagation into $N$ times
the corona is not ballistic, but by (c) it is not forbidden.
\end{remark}

\begin{remark}
For the Bialynicki-Birula walk \cite[Eq.~(5.12)]{CJWW}, $\Gamma$ is contained
in the intersection of three orthogonal cylinders (and numerically equal to
it \cite[Fig.~5]{CJWW}).  It contains group velocities up to
$\sqrt{3/2}>\cIR$, attained at $p=-\frac\pi4(1,1,1)$.  In that walk the corona contains a ballistic sector
faster than the emergent light.  We restrict to \cite[Eq.~(5.15)]{CJWW}
precisely because it has no such sector.
\end{remark}

\section{Protocol and infrared admissibility}\label{sec:protocol}

Fix an integer $N\ge2$.  The infrared scale is $\Lambda_N=N^{-1}$ and the
admissibility budget is $\Lambda'_N=N^{-1/2}$.  Let $\Pi_\Lambda$ denote the
spectral projection onto $\{|p|_2\le\Lambda\}$, and write $\Pi=\Pi_{\Lambda_N}$
and $\Pi'=\Pi_{\Lambda'_N}$.  For $N\ge2$ both balls lie in $|p|<\pi/4$,
where $f>0$ and the only conical point is $p=0$.

\subsection{Regions}
Let
\[
\cA_N=\{x\in\Z^3:|x|\le N/4\},\qquad \cB_N=\{y\in\Z^3:|y-N(1,1,1)|\le N/4\},
\]
with Euclidean norms throughout.  For every $x\in\cA_N$ and $y\in\cB_N$,
\begin{equation}\label{eq:separation}
|y-x|-N\ge(\sqrt3-\tfrac32)N>\tfrac N5,
\qquad
u\cdot(y-x)\ge(3-\tfrac{\sqrt3}2)N,\quad u=(1,1,1).
\end{equation}
Both follow from the triangle inequality, and the last inequality in the
first display is $3>(17/10)^2$.  Each region has at most $(N/2+1)^3\le N^3$
sites.

\subsection{Resource, encoder, detector}
Let $g(q)=(1-|q|^2)_+^2$.  The resource is
\[
\hat\phi_N(p)=Z_N^{-1/2}\,g(Np)\,\dn,
\qquad Z_N=\frac{64}{3465\,\pi^2N^3},
\]
so that $\|\phi_N\|=1$ and $\Pi\phi_N=\phi_N$.  In position space
$\phi_N=\varphi_N\,\dn$ with the real, radial function
\begin{equation}\label{eq:resource}
\varphi_N(x)=N^{-3/2}\,\Phi_0(x/N),\qquad
\Phi_0(w)=c_r\int_{\R^3}g(q)\,e^{-iq\cdot w}\,d^3q,\qquad c_r=\frac{\sqrt{3465}}{64\pi^2}.
\end{equation}
This is exact, with no truncation of the spatial tail.

Alice's profile is $F_N(x)=(1-16|x|^2/N^2)_+^2$, supported in $\cA_N$.  For
$M\in\{I,\sigma_1,\sigma_2,\sigma_3\}$ the encoder is the multiplication
operator
\[
U_M=\exp\bigl(i\tfrac\pi2F_N(x)\,M\bigr)=I+c_N(x)I+is_N(x)M,
\qquad c_N=\cos(\tfrac\pi2F_N)-1,\ \ s_N=\sin(\tfrac\pi2F_N).
\]
It acts as the identity outside $\cA_N$.  In the second-quantized free
fermion picture it is the one-particle restriction of an even,
number-preserving local unitary.

Bob's profile is $h_N(y)=(1-16|y-Nu|^2/N^2)_+^2$, with $u=(1,1,1)$,
supported in $\cB_N$.
For $M_B\in\{I,P_1,P_2,P_3\}$, with $P_j=(I+\sigma_j)/2$, the effect is
\[
E=h_N\otimes M_B,\qquad 0\le E\le I .
\]

\subsection{Signal}
Alice encodes a bit $b\in\{0,1\}$ by applying $U^{(1)}=U_M$ or $U^{(0)}=I$ to
the resource.  After $N$ steps the state is
$\psi_b(N)=S^NU^{(b)}\phi_N$.  The signal is
\begin{equation}\label{eq:signal}
\delta_{M,M_B}(N)=\bigl|\langle\psi_1,E\psi_1\rangle-\langle\psi_0,E\psi_0\rangle\bigr|=|L_{M,M_B}(N)|,
\end{equation}
where $L_{M,M_B}(N)$ denotes the signed difference.  No spectral projection is
applied to the signal.  Infrared admissibility is a property of the
operations only.  We also consider the trace distance $D_B(N)$ between Bob's
reduced states.  In the free-fermion description, the reduced state of a
one-particle vector $\psi$ on the modes of $\cB_N$ is
$(1-\|P_B\psi\|^2)|\Omega\rangle\langle\Omega|+|P_B\psi\rangle\langle P_B\psi|$,
and $D_B=\frac12\|\rho_1-\rho_0\|_1\ge\delta$.

\subsection{Infrared admissibility}
\begin{definition}\label{def:admissible}
For a bounded operator $X$ on $\mathcal H$ with $X\Pi\ne0$, set
\[
\eta_{\mathrm{op}}(X)=\frac{\|(I-\Pi')X\Pi\|}{\|X\Pi\|}.
\]
The encoder $U_M$ is \emph{infrared-admissible} if
$\eta_{\mathrm{op}}(U_M-I)\to0$ and
\[
\eta_{\mathrm{enc}}^M=\frac{\|\Delta_M-\Pi'\Delta_M\Pi'\|_1}{\|\Delta_M\|_1}\to0,
\qquad \Delta_M=U_M|\phi_N\rangle\langle\phi_N|U_M^*-|\phi_N\rangle\langle\phi_N|,
\]
as $N\to\infty$, where $\Delta_M\ne0$ is required for $\eta_{\mathrm{enc}}^M$
to be defined.  The effect $E$ is infrared-admissible if
$\eta_{\mathrm{op}}(E)\to0$.
\end{definition}

For the operations of this paper all denominators are non-zero for every
$N\ge2$ (Theorem~\ref{thm:admissible}).

In words: acting on anything in the infrared band, an admissible operation
leaves only a vanishing fraction of its output outside the wider band
$\Pi'$.  A strictly local gate cannot do this.

\begin{lemma}[Single-site operations are ultraviolet]\label{lem:point}
If $X\Pi\ne0$ and $\operatorname{ran}X\subseteq\ell^2(\{x_0\};\C^2)$ for a
single site $x_0$, then
$\eta_{\mathrm{op}}(X)=\sqrt{1-\kappa'_N}\to1$, where
$\kappa'_N=(6\pi^2N^{3/2})^{-1}$.
\end{lemma}

\begin{proof}
For every vector $e_{x_0}\otimes\chi$,
$\|\Pi'(e_{x_0}\otimes\chi)\|^2=\mu(\{|p|\le\Lambda'_N\})=(\Lambda'_N)^3/(6\pi^2)$.
Hence every vector in $\operatorname{ran}X$ has exactly the fraction
$1-\kappa'_N$ of its squared norm outside $\Pi'$.
\end{proof}

This is the reason the encoder is spread over a region of size $O(N)$ with
a smooth profile.  A pointlike phase gate, such as $I-2P_{x_0}$, is
excluded by Lemma~\ref{lem:point}.  The regional operations pass:

\begin{theorem}[Admissibility]\label{thm:admissible}
Let $K_e=\frac\pi2(2+8\sqrt3\pi)$, $K_d=\frac\pi2(1+16\sqrt3)$ and
$m=11/(560\pi^2\,32^3)$.  For all $N\ge32$, all four $M$ and all four
$M_B$,
\[
\eta_{\mathrm{op}}(U_M-I)\le\frac{K_e}{\sqrt{(2-\sqrt2)m}}\,N^{-1/2},\qquad
\eta_{\mathrm{enc}}^M\le\frac{K_e}{m\sqrt{2-\sqrt2}}\,N^{-1/2},\qquad
\eta_{\mathrm{op}}(E)\le\frac{2K_d}{\sqrt m}\,N^{-1/2}.
\]
All denominators are non-zero for every $N\ge2$.
\end{theorem}

The constants are conservative.  The proof is in Section~\ref{sec:admissible}.

\section{Results}\label{sec:results}

\begin{theorem}[Explicit upper bound]\label{thm:upper}
Let $N\ge2$ and $T_N=\|P_{\cB_N}S^NP_{\cA_N}\|$.  Then
\[
T_N\le9N^4e^{-JN},\qquad J=\bigl(1-\tfrac{\sqrt3}2\bigr)\log2\approx0.0929 .
\]
Consequently, for every unitary $U$ acting as the identity outside
$\cA_N\otimes\C^2$, every one-particle state and every effect in $\cB_N$,
\[
\delta\le D_B\le4T_N\le36N^4e^{-JN}.
\]
\end{theorem}

\begin{remark}[Formal verification]
Theorem~\ref{thm:upper} is machine-checked in Lean~4 with Mathlib
(\texttt{formal/} in~\cite{Repo}), for every $N\ge2$ and without
additional axioms.  This covers the kernel bound, the geometry
\eqref{eq:separation}, the counting of lattice points, the operator bound on
$T_N$, and the step $\delta\le4T_N$.  The formal proof bounds the matrix
powers through Cayley--Hamilton and entrywise estimates instead of
Lemma~\ref{lem:schur}, and obtains the sharper constant
$T_N\le4N^4e^{-JN}$.  Both constants are valid; the proof in
Section~\ref{sec:upper} keeps the constant $9$ that the elementary
Lemma~\ref{lem:schur} gives.  The identification of Bob's amplitudes with the
restricted walk, and the second-quantized distance $D_B$, are not
formalized.
\end{remark}

For $\xi\in\R^3$ put $\Phi(\xi)=\arcosh\bigl(\prod_{j=1}^3\cosh\xi_j\bigr)$
and define the rate function
\begin{equation}\label{eq:rate}
I(v)=\sup_{\xi\in\R^3}\bigl[\xi\cdot v-\Phi(\xi)\bigr].
\end{equation}
Let $V_{\mathrm{reg}}=(1,1,1)+\overline B(0,\tfrac12)$.  This is the set of
velocities $(y-x)/N$ for $x,y$ in the continuum balls underlying
$\cA_N,\cB_N$.

\begin{theorem}[Regional rate]\label{thm:rate}
\begin{enumerate}[label=(\alph*)]
\item $I$ is convex, $I=0$ on $\overline B(0,1)$, $I>0$ outside it, and
  $I=+\infty$ outside $[-1,1]^3$.
\item On $V_{\mathrm{reg}}$, $I$ has the unique minimiser
  $v_*=\alpha(1,1,1)$, $\alpha=1-\frac1{2\sqrt3}$.  The corresponding dual
  tilt is $\xi_*=t_*(1,1,1)$, where $t_*>0$ is the unique solution of
  $\alpha=\nabla_1\Phi(t,t,t)$.  Moreover
  \[
  K_*:=I(v_*)=3\alpha t_*-\arcosh(\cosh^3t_*),\qquad
  \cosh^2t_*=\frac{\alpha\bigl(\alpha+\sqrt{4-3\alpha^2}\bigr)}{2(1-\alpha^2)} .
  \]
\item $J<K_*<\log4$.  Numerically $t_*=0.7357528144\ldots$ and
  $K_*=0.1905189296\ldots$.
\item For all $N\ge2$ and all $(x,y)\in\cA_N\times\cB_N$,
  \[
  \|G_N(y-x)\|\le\bigl(1+4e^{3t_*-\Phi_*}N\bigr)e^{-K_*N},\qquad \Phi_*=\Phi(\xi_*),
  \]
  and hence $\delta\le D_B\le4N^3(1+10N)e^{-K_*N}$.
\end{enumerate}
\end{theorem}

The main result identifies the exact leading behaviour of every signal in
the family.  Write $\theta_N=\{\sqrt3N/4\}\in[0,1)$ for the fractional part.

\begin{theorem}[Leading asymptotics]\label{thm:main}
For each of the sixteen pairs $(M,M_B)$ there is a continuous, $1$-periodic,
real function $C_{M,M_B}(\theta)$ such that, as $N\to\infty$,
\[
L_{M,M_B}(N)=e^{-K_*N}N^{-13/2}\Bigl(C_{M,M_B}(\theta_N)+O(N^{-1/2})\Bigr).
\]
Explicitly,
\begin{equation}\label{eq:C}
C_{M,M_B}(\theta)=\cK\,c_r\bigl[\Gamma_+(\theta)\,\ell_0+\Gamma_-(\theta)\,\ell_\pi\bigr],
\end{equation}
with the constants $\cK$, $c_r$, the functions $\Gamma_\pm$ and the numbers
$\ell_0,\ell_\pi$ defined in Section~\ref{sec:asymptotics}.  For every pair,
\[
C_{M,M_B}(\theta)=\overline C_{M,M_B}\bigl(1+\vartheta_{M,M_B}(\theta)\bigr),
\qquad \sup_\theta|\vartheta_{M,M_B}(\theta)|\le1.47\times10^{-3},
\qquad \overline C_{M,M_B}\ne0,
\]
with the values in Table~\ref{tab:C}.  Consequently, for every pair,
\[
\delta_{M,M_B}(N)=\bigl|C_{M,M_B}(\theta_N)\bigr|\,N^{-13/2}\,e^{-K_*N}\bigl(1+O(N^{-1/2})\bigr),
\]
and $\delta_{M,M_B}(N)>0$ for all $N$ larger than some finite $N_*$.
\end{theorem}

The constants implicit in the $O(N^{-1/2})$ terms are finite but not
explicit, and neither is $N_*$.  Theorem~\ref{thm:main} therefore does not
assert $\delta_{M,M_B}(N)>0$ at any specified $N$.  It also does not say from
which $N$ on the leading term is numerically accurate
(Section~\ref{sec:discussion}).

\begin{table}[t]
\centering
\small
\begin{tabular}{llrr}
\toprule
$M$ & $M_B$ & $\overline C_{M,M_B}$ & $\sup_\theta|C/\overline C-1|$\\
\midrule
$I$ & $I$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$I$ & $P_1$ & $+1.2072650683$ & $1.09\cdot10^{-3}$\\
$I$ & $P_2$ & $+0.8164098576$ & $1.08\cdot10^{-3}$\\
$I$ & $P_3$ & $-0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_1$ & $I$ & $-3.7206303938$ & $1.05\cdot10^{-3}$\\
$\sigma_1$ & $P_1$ & $-1.5567800857$ & $1.06\cdot10^{-3}$\\
$\sigma_1$ & $P_2$ & $-2.8203960182$ & $1.02\cdot10^{-3}$\\
$\sigma_1$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $I$ & $-2.9389199724$ & $1.05\cdot10^{-3}$\\
$\sigma_2$ & $P_1$ & $-0.5846543741$ & $1.02\cdot10^{-3}$\\
$\sigma_2$ & $P_2$ & $-1.7729950974$ & $1.04\cdot10^{-3}$\\
$\sigma_2$ & $P_3$ & $-0.1776542932$ & $1.05\cdot10^{-3}$\\
$\sigma_3$ & $I$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
$\sigma_3$ & $P_1$ & $-1.2072650683$ & $1.09\cdot10^{-3}$\\
$\sigma_3$ & $P_2$ & $-0.8164098576$ & $1.08\cdot10^{-3}$\\
$\sigma_3$ & $P_3$ & $+0.0752752093$ & $1.47\cdot10^{-3}$\\
\bottomrule
\end{tabular}
\caption{Mean leading coefficients $\overline C_{M,M_B}=\cK c_r\overline\Gamma\ell_0$
and the uniform bound on their relative oscillation in $\theta$.  Values are
certified by interval arithmetic (Appendix~\ref{app:numerics}).}
\label{tab:C}
\end{table}

\begin{corollary}\label{cor:suppressed}
In this protocol the emergent light cone is not operationally sharp for
infrared-admissible operations.  For each pair the response is
non-perturbatively small: $\delta_{M,M_B}(N)=o(N^{-k})$ for every $k$.  It is
nevertheless non-zero for all large $N$, with the exact rate $K_*$, the exact
power $13/2$ and an explicit non-vanishing coefficient.
\end{corollary}

\begin{remark}\label{rem:features}
Three features of Table~\ref{tab:C} were not assumed and come out of the
computation.  First, $C(\sigma_3,\cdot)=-C(I,\cdot)$ at leading order;
the two encoders differ only at lower orders.  Second, the three Pauli
encoders are not equivalent: with $M_B=I$ they give three different
coefficients.  Third, for $M=\sigma_2$ the two contributing saddles enter with
the same sign for every detector: $\ell_0$ and $\ell_\pi$ of
Appendix~\ref{app:numerics} have the same sign.  Since $\Gamma_+>0$ and
$\Gamma_-\ge0$ (Lemma~\ref{lem:depth}), non-vanishing then follows without
the margin estimate in the proof of Theorem~\ref{thm:main}, so for this
encoder the non-cancellation mechanism is particularly transparent.  The smallest coefficients,
$|\overline C|\approx0.0753$, occur for $M\in\{I,\sigma_3\}$ with
$M_B\in\{I,P_3\}$.  For these two encoders with $M_B=I$, the diagnostics of
Appendix~\ref{app:numerics} show that the next-order term, of size
$N^{-17/2}e^{-K_*N}$, dominates numerically throughout the diagnostic range
$N\le56$.
\end{remark}

\begin{remark}[Methodology]
The protocol (regions, profiles, encoders, detectors, scalings
$\Lambda_N=N^{-1}$, $\Lambda'_N=N^{-1/2}$ and the encoding angle $\pi/2$) was fixed before
the asymptotic analysis and was not tuned afterwards.  The family of
encoders and detectors is not exhaustive: a general generator
$M=aI+b\cdot\sigma$ is not covered, because no symmetry of the walk relating
the directions $\hat n\cdot\sigma$ has been established.
\end{remark}

\section{Proof of the upper bounds}\label{sec:upper}

\subsection{An ellipse lemma}
For $a\ge1$ let
$E_a=\{z\in\C:(\re z)^2/a^2+(\im z)^2/(a^2-1)\le1\}$, where $E_1=[-1,1]$.
These are the confocal ellipses with foci $\pm1$.  The Joukowski map
$\lambda\mapsto(\lambda+\lambda^{-1})/2$ sends the circle $|\lambda|=r\ge1$
onto $\partial E_{(r+r^{-1})/2}$.

\begin{lemma}\label{lem:ellipse}
Let $a,c\ge1$.  If $z\in\partial E_a$ and $w\in E_c$, then $zw\in E_{ac}$;
consequently $E_aE_c\subseteq E_{ac}$.  If moreover $a,c>1$, then
$zw\in\partial E_{ac}$ only if $z=\pm a$ and $w=\pm c$.
\end{lemma}

\begin{proof}
If $c=1$, then $w\in[-1,1]$ and $zw\in E_a$ by convexity and symmetry.  If
$a=1$, then $z\in[-1,1]$ and the same argument applies.  So let $a,c>1$.
Write
$z=a\cos p+i\sqrt{a^2-1}\sin p$ and $w=c\,x+i\sqrt{c^2-1}\,y$ with
$x^2+y^2\le1$.  In the coordinates adapted to $E_{ac}$, the point $zw$
corresponds to $L(x,y)^T$ with
\[
L=\begin{pmatrix}(ac)^{-1}&0\\0&(a^2c^2-1)^{-1/2}\end{pmatrix}
\begin{pmatrix}a\cos p&-\sqrt{a^2-1}\sin p\\ \sqrt{a^2-1}\sin p&a\cos p\end{pmatrix}
\begin{pmatrix}c&0\\0&\sqrt{c^2-1}\end{pmatrix}.
\]
With $A=a^2$, $C=c^2$ and $u=\cos^2p$, a direct computation gives
\[
(I-L^TL)_{11}=\frac{(1-u)(C-1)}{AC-1},\qquad
\det(I-L^TL)=\frac{(C-1)(1-u)\bigl[A-1+C(1-u)\bigr]}{AC(AC-1)} .
\]
Both are non-negative, so $I-L^TL\ge0$ by Sylvester's criterion and
$\|L\|\le1$.  If $u<1$, both are positive, so $\|L\|<1$ and $zw$ is
interior.  If $u=1$, then $z=\pm a$ and
\[
L=\pm\operatorname{diag}\Bigl(1,\ \frac{a\sqrt{c^2-1}}{\sqrt{a^2c^2-1}}\Bigr),
\]
whose second entry is $<1$.  Hence $|L(x,y)^T|=1$ forces $y=0$ and $|x|=1$,
that is, $w=\pm c$.
\end{proof}

\begin{lemma}\label{lem:specrad}
For $\eta\in\R^3$ and $\xi\in\R^3$,
$\rho\bigl(S(\eta-i\xi)\bigr)\le e^{\Phi(\xi)}$.  If all $\xi_j\ne0$, equality
holds if and only if $\eta\in\Sigma:=\{0,\pi\}^3$ modulo $2\pi$.
\end{lemma}

\begin{proof}
$\cos(\eta_j-i\xi_j)=\cos\eta_j\cosh\xi_j+i\sin\eta_j\sinh\xi_j\in\partial E_{\cosh\xi_j}$.
By Lemma~\ref{lem:ellipse} applied twice,
$f(\eta-i\xi)=\prod_j\cos(\eta_j-i\xi_j)\in E_{\prod\cosh\xi_j}$.  When all
$\xi_j\ne0$, it lies on the boundary only if every factor is a real vertex,
that is, only if every $\sin\eta_j=0$.  The eigenvalues $\lambda^{\pm1}$ of
the unimodular matrix $S(\eta-i\xi)$ satisfy $(\lambda+\lambda^{-1})/2=f$.
If $|\lambda|=r\ge1$, then $f\in\partial E_{(r+r^{-1})/2}$.  Since the
ellipses are nested, $(r+r^{-1})/2\le\prod\cosh\xi_j$, which is
$r\le e^{\Phi(\xi)}$, with strict inequality when $f$ is interior.  On
$\Sigma$, $f=\pm\prod\cosh\xi_j$ is real and equality holds.
\end{proof}

\begin{lemma}[Powers without a gap]\label{lem:schur}
Let $T$ be a $2\times2$ matrix with $\rho(T)\le e^{\varkappa}$ and
$\|T\|\le\beta$.  Then $\|T^N\|\le e^{N\varkappa}+\beta Ne^{(N-1)\varkappa}$.
\end{lemma}

\begin{proof}
Take a unitary Schur form $T=V\begin{psmallmatrix}\lambda_1&b\\0&\lambda_2\end{psmallmatrix}V^*$,
so $|b|\le\|T\|$.  The upper-right entry of the $N$-th power is
$b\sum_{j=0}^{N-1}\lambda_1^j\lambda_2^{N-1-j}$, also when
$\lambda_1=\lambda_2$.  The diagonal part has norm
$\max_j|\lambda_j|^N$.
\end{proof}

\subsection{Proof of Theorem~\ref{thm:upper}}
Since the integrand in \eqref{eq:kernel} is entire and $2\pi$-periodic in
each variable, the contour can be shifted to $p=\eta-i\xi$ for any
$\xi\in\R^3$ without boundary terms:
\begin{equation}\label{eq:tilt}
G_N(d)=e^{-\xi\cdot d}\int_{\T^3}e^{-i\eta\cdot d}\,S(\eta-i\xi)^N\,d\mu(\eta).
\end{equation}
Take $\xi=tu$ with $t=\log2$, so $\cosh^3t=125/64$.  Lemma~\ref{lem:specrad}
gives
\[
\rho\bigl(S(\eta-itu)\bigr)\le\exp\arcosh(125/64)<4,
\]
because $125/64<17/8=\cosh\log4$.  By Lemma~\ref{lem:jumps},
\[
\|S(\eta-itu)\|\le\sum_d\|S_d\|e^{t|u\cdot d|}\le4e^{3t}=32 .
\]
Lemma~\ref{lem:schur}, with the cruder bound $|\lambda_j|\le4$, gives
$\|S(\eta-itu)^N\|\le4^N+32N4^{N-1}\le9N4^N$.  With
\eqref{eq:separation},
\[
\|G_N(y-x)\|\le9N\exp\bigl[-t\,u\cdot(y-x)+N\log4\bigr]\le9Ne^{-JN}
\]
for all $(x,y)\in\cA_N\times\cB_N$.  The Schur test with $|\cA_N|,|\cB_N|\le N^3$
gives $T_N\le9N^4e^{-JN}$.

Let $v_b=P_BS^NU^{(b)}\psi$ for a one-particle state $\psi$.  Then
$v_1-v_0=P_BS^NP_A(U-I)\psi$, so $\|v_1-v_0\|\le2T_N$.  The difference of
Bob's reduced states is $X=|v_1\rangle\langle v_1|-|v_0\rangle\langle v_0|$ on
the one-particle block, together with $-\tr X$ on the vacuum block.  Hence
$D_B=\frac12(|\tr X|+\|X\|_1)\le\|X\|_1\le(\|v_1\|+\|v_0\|)\|v_1-v_0\|\le4T_N$.
Mixed states follow by convexity, and $\delta\le D_B$ holds for every effect.
\qed

\subsection{Proof of Theorem~\ref{thm:rate}}
(a) $I$ is a supremum of affine functions, so it is convex, and $I\ge0$
(take $\xi=0$).  The inequality
$\cosh\sqrt{a^2+b^2}\le\cosh a\cosh b$, applied twice, gives
$\Phi(\xi)\ge|\xi|$, so $I=0$ on $\overline B(0,1)$.  Since
$\Phi(\xi)=|\xi|+O(|\xi|^3)$, $I(v)>0$ for $|v|>1$.  Finally $I=+\infty$ outside
$\operatorname{conv}F$ by \cite[Lemma~4.1]{CJWW}.  Directly, if
$v_j>1$, take $\xi=se_j$ and let $s\to\infty$, using $\Phi(se_j)=s$.

(b) $\Phi$ is smooth where $\Pi(\xi)=\prod_j\cosh\xi_j>1$, with
\[
\nabla\Phi(\xi)=\frac{\Pi(\xi)}{\sqrt{\Pi(\xi)^2-1}}\,(\tanh\xi_1,\tanh\xi_2,\tanh\xi_3).
\]
On the diagonal, $h(t)=\nabla_1\Phi(t,t,t)$ tends to $1/\sqrt3$ as
$t\to0^+$ and to $1$ as $t\to\infty$.  It is strictly increasing, since
$3h'(t)=u^T\Hess\Phi(t,t,t)\,u=3q_n(t)>0$, where $q_n(t)$ is given by the
formula of Lemma~\ref{lem:symbol}(d) with $c_*$ replaced by $\cosh t>1$.  Since
$\alpha\in(1/\sqrt3,1)$, there is a unique $t_*>0$ with $h(t_*)=\alpha$, and
then $\nabla\Phi(\xi_*)=v_*$.  Solving $h(t)=\alpha$ for $\cosh^2t$ gives the
stated closed form.  By the definition of $I$, for every $v$,
\[
I(v)\ge\xi_*\cdot v-\Phi(\xi_*)=I(v_*)+\xi_*\cdot(v-v_*)
=I(v_*)+\sqrt3\,t_*\bigl(\uhat\cdot v-|v_*|\bigr),
\qquad \uhat=u/\sqrt3 .
\]
On $V_{\mathrm{reg}}$ we have $\uhat\cdot v\ge\sqrt3-\frac12=|v_*|$, with
equality only at $v=v_*$.  Hence $v_*$ is the unique minimiser.

(c) The tilt $\xi=(\log2)u$ gives
$I(v_*)\ge3\alpha\log2-\arcosh(125/64)>(3-\tfrac{\sqrt3}2)\log2-\log4=J$.
Also $\xi_*\cdot v_*<\xi_*\cdot u$ because $\alpha<1$ and $t_*>0$, so
$I(v_*)<\xi_*\cdot u-\Phi(\xi_*)\le I(u)$.  Along the diagonal,
$3t-\arcosh(\cosh^3t)\uparrow\log4$, and $I(u)=\log4$ is also the exact
vertex rate of Proposition~\ref{prop:geometry}(c).  The numerical values are
enclosed by interval arithmetic.

(d) Apply \eqref{eq:tilt} with $\xi=\xi_*$.  By Lemma~\ref{lem:specrad},
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*}$ for all $\eta$.  By
Lemma~\ref{lem:jumps}, $\|S(\eta-i\xi_*)\|\le4e^{3t_*}$.
Lemma~\ref{lem:schur} gives
$\sup_\eta\|S(\eta-i\xi_*)^N\|\le e^{N\Phi_*}(1+4e^{3t_*-\Phi_*}N)$.  For
$(x,y)\in\cA_N\times\cB_N$, \eqref{eq:separation} and $\xi_*\parallel\uhat$
give $\xi_*\cdot(y-x)\ge N\,\xi_*\cdot v_*$, and
$N\xi_*\cdot v_*-N\Phi_*=NK_*$.  Numerically $4e^{3t_*-\Phi_*}<9.2$, so
$1+4e^{3t_*-\Phi_*}N\le1+10N$, and the Schur test concludes as before.
\qed

\section{Proof of admissibility}\label{sec:admissible}

\begin{lemma}\label{lem:IR1}
Let $a:\Z^3\to M_2(\C)$ satisfy $\sup\|a\|\le A$ and
$\|a(x+e_j)-a(x)\|\le L/N$ for all $x,j$.  Then
\[
\|(I-\Pi')\,a\,\Pi\|\le\tfrac\pi2(A+\sqrt3L)\,N^{-1/2}.
\]
\end{lemma}

\begin{proof}
Let $D_j\xi(x)=\xi(x+e_j)-\xi(x)$.  On the complement of $\Pi'$,
\[
\sum_j|e^{ip_j}-1|^2=\sum_j4\sin^2(p_j/2)\ge(2/\pi)^2|p|^2\ge(2/\pi)^2N^{-1},
\]
using $\sin s\ge2s/\pi$ on $[0,\pi/2]$.  By Plancherel,
$\|(I-\Pi')\xi\|\le\frac\pi2N^{1/2}(\sum_j\|D_j\xi\|^2)^{1/2}$.  For
$\psi=\Pi\psi$, $(\sum_j\|D_j\psi\|^2)^{1/2}\le N^{-1}\|\psi\|$.  The
discrete product rule
$D_j(a\psi)=a(\cdot+e_j)D_j\psi+(D_ja)\psi$ and Minkowski's inequality give
$(\sum_j\|D_j(a\psi)\|^2)^{1/2}\le(A+\sqrt3L)N^{-1}\|\psi\|$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:admissible}]
\emph{Numerators.}  $|\nabla F_N|=64|x|(1-16|x|^2/N^2)/N^2\le16/N$ inside
$\cA_N$, and the gradient vanishes on the sphere, so $F_N$ is
$16/N$-Lipschitz on $\Z^3$.  For $a_M=U_M-I$ we get $A=2$ and $L=8\pi$,
because $\|\frac{d}{dF}e^{i\pi FM/2}\|=\pi/2$.  For $E=h_N\otimes M_B$ we get
$A=1$ and $L=16$.  Lemma~\ref{lem:IR1} bounds the numerators by
$K_eN^{-1/2}$ and $K_dN^{-1/2}$.  For $\eta_{\mathrm{enc}}$, write
$v=U_M\phi_N$, $w=\Pi'v$ and $r=v-w=(I-\Pi')a_M\phi_N$.  Since
$\Pi'\phi_N=\phi_N$, $\Delta_M-\Pi'\Delta_M\Pi'=|r\rangle\langle v|+|w\rangle\langle r|$,
whose trace norm is at most $2\|r\|\le2K_eN^{-1/2}$.

\emph{Denominators.}  For $|x|\le N$ and $|p|\le N^{-1}$, $\cos(p\cdot x)\ge\frac12$.
Hence $\varphi_N(x)\ge\frac12\sqrt{11/(140\pi^2)}\,N^{-3/2}$ for $|x|\le N$.
Let $N\ge32$, and consider two auxiliary sets.  The first is
$Q_{\mathrm{in}}=\{|x_j|\le N/32\}$, with at least $(N/32)^3$ sites, on which
$F_N\ge(61/64)^2>\frac12$.  The second is
$Q_{\mathrm{out}}=\{N/2\le x_1\le5N/8,\ 0\le x_2,x_3\le N/8\}$, with at least
$(N/16)^3$ sites, on which $F_N=0$ and $|x|<N$.  Each carries resource
weight at least $m$.

On $Q_{\mathrm{in}}$, $\frac\pi2F_N\in[\frac\pi4,\frac\pi2]$, so
$a_M^*a_M=2(1-\cos\frac\pi2F_N)I\ge(2-\sqrt2)I$.  Thus
$\|a_M\Pi\|\ge\|a_M\phi_N\|\ge\sqrt{(2-\sqrt2)m}$.  For the detector, test
on the resource translated to $N(1,1,1)$, with internal state a
$+1$ eigenvector of $M_B$.  This test vector lies in $\operatorname{ran}\Pi$,
and it gives $\|E\Pi\|\ge\frac12\sqrt m$.

For $\eta_{\mathrm{enc}}$, $\|\Delta_M\|_1=2\sqrt{1-|z|^2}$ with
$z=\sum_xw_xt_x$, $w_x=|\varphi_N(x)|^2$ and
$t_x=\langle\dn|e^{i\pi F_N(x)M/2}|\dn\rangle$.  This gives $t_x=e^{i\pi F_N/2}$
for $M=I$, $\cos(\pi F_N/2)$ for $M=\sigma_{1,2}$, and $e^{-i\pi F_N/2}$ for
$M=\sigma_3$.  Then
$1-|z|^2=\sum_{x,y}w_xw_y(1-\re t_x\bar t_y)$.  All terms are non-negative,
and for $x\in Q_{\mathrm{in}}$, $y\in Q_{\mathrm{out}}$ one has
$\re t_x\bar t_y=\cos(\frac\pi2F_N(x))\le1/\sqrt2$.  Counting both orders
gives $1-|z|^2\ge(2-\sqrt2)m^2$.  For $2\le N<32$ the same argument, with
the origin and the site $(\lfloor N/4\rfloor+1,0,0)$, shows that the
denominators are non-zero.
\end{proof}

\section{Proof of the leading asymptotics}\label{sec:asymptotics}

Throughout, $C$ denotes a finite constant independent of $N$ whose value may
change from line to line.  The constants $r_0,c,c_3,c_P$ below are finite
but not made explicit.

\subsection{Reduction to one interference functional}
Let $P_B$ be the restriction to $\cB_N$ (not a spectral projection).  Write
$\widetilde r=S^N\phi_N$ for the free evolution of the resource on all of
$\Z^3$, and put
\[
r=P_B\widetilde r,\qquad a_c=P_BS^N(c_N\varphi_N\dn),\qquad
a_\up=P_BS^N(s_N\varphi_N\up),\qquad a_\dn=P_BS^N(s_N\varphi_N\dn).
\]
Since $\sigma_1\dn=\up$, $\sigma_2\dn=-i\up$ and $\sigma_3\dn=-\dn$, Bob's
encoded amplitude $P_B\psi_1$ is $v+ia_\dn$, $v+ia_\up$, $v+a_\up$ or
$v-ia_\dn$ for $M=I,\sigma_1,\sigma_2,\sigma_3$, where $v=r+a_c$.  Expanding
\eqref{eq:signal} with $E$ supported in $\cB_N$,
\begin{equation}\label{eq:Lexp}
\begin{aligned}
L_{I}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\dn\rangle+Q_I, &
L_{\sigma_3}&=2\re\langle r,Ea_c\rangle+2\im\langle r,Ea_\dn\rangle+Q_{\sigma_3},\\
L_{\sigma_1}&=2\re\langle r,Ea_c\rangle-2\im\langle r,Ea_\up\rangle+Q_{\sigma_1}, &
L_{\sigma_2}&=2\re\langle r,Ea_c\rangle+2\re\langle r,Ea_\up\rangle+Q_{\sigma_2}.
\end{aligned}
\end{equation}
Each $Q_M$ is a sum of terms quadratic in $(a_c,a_\up,a_\dn)$.  For
example, $Q_I=\langle a_c,Ea_c\rangle+\langle a_\dn,Ea_\dn\rangle-2\im\langle a_c,Ea_\dn\rangle$.
Positivity of $E$ does not fix the sign of $L$, because the interference
terms can have either sign.

By Theorem~\ref{thm:rate}(d), $a_c,a_\up,a_\dn$ have $\ell^2$-norm at most
$T_N=O(N^4e^{-K_*N})$, so $Q_M=O(N^{8}e^{-2K_*N})$.  The free tail is only polynomially
small (Lemma~\ref{lem:tail}).  The $e^{-K_*N}$ sector therefore consists of
the linear interference terms.  Define, for $\chi\in\{\up,\dn\}$,
\[
\mathcal T_\chi(N)=e^{K_*N}\,\bigl\langle r,\,E\,S^N(s_N\varphi_N\chi)\bigr\rangle .
\]
Theorem~\ref{thm:main} follows from Theorem~\ref{thm:T} below.  The piece
$\langle r,Ea_c\rangle$ is $O(N^{-17/2}e^{-K_*N})$ by the same argument,
because $c_N=\Theta(N^{-4})$ in the relevant layer while $s_N=\Theta(N^{-2})$.

\subsection{Exact tilted representation}
Let $R=N/4$, $x_*=R\uhat$ and $y_*=N u-R\uhat$, so that $y_*-x_*=Nv_*$.  For
$f$ supported in $\cA_N$ and $w$ supported in $\cB_N$, put
\[
\mathfrak A_f(\eta)=\sum_xe^{i\eta\cdot(x-x_*)}e^{\xi_*\cdot(x-x_*)}f(x),\qquad
\mathfrak B_w(\eta)=\sum_ye^{-i\eta\cdot(y-y_*)}e^{-\xi_*\cdot(y-y_*)}w(y)^\dagger .
\]
Let $\widetilde S_N(\eta)=e^{-N\Phi_*}S(\eta-i\xi_*)^N$.  By \eqref{eq:tilt}
with $\xi=\xi_*$, and using $\xi_*\cdot v_*-\Phi_*=K_*$,
\begin{equation}\label{eq:exactrep}
e^{K_*N}\sum_yw(y)^\dagger(S^Nf)(y)=\int_{\T^3}\mathfrak B_w(\eta)\,\widetilde S_N(\eta)\,\mathfrak A_f(\eta)\,e^{-iN\eta\cdot v_*}\,d\mu(\eta).
\end{equation}
This identity is exact: the sums are finite and no poles are crossed.

\subsection{The tilted symbol}\label{ssec:tilted}
\begin{lemma}\label{lem:symbol}
\begin{enumerate}[label=(\alph*)]
\item $S(-i\xi)$ is Hermitian for every real $\xi$, with $\det=1$.  At
  $\xi_*$, with $c_*=\cosh t_*$ and $s_*=\sinh t_*$,
  \[
  S(-i\xi_*)=\begin{pmatrix}c_*^2e^{-t_*}&-(1+ic_*)s_*\\-(1-ic_*)s_*&c_*^2e^{t_*}\end{pmatrix},
  \]
  with eigenvalues $e^{\pm\Phi_*}$, $e^{\Phi_*}=c_*^3+\sqrt{c_*^6-1}=3.97314\ldots$.
  The orthogonal projector onto the $e^{\Phi_*}$-eigenspace is
  \[
  P=\frac12\begin{pmatrix}1-\alpha&-(1+ic_*)\alpha/c_*^2\\-(1-ic_*)\alpha/c_*^2&1+\alpha\end{pmatrix}.
  \]
\item For all $p\in\C^3$: $S(p+\pi e_1)=-S(p)$, $S(p+\pi e_3)=-\sigma_3S(p)\sigma_3$,
  $S(p+\pi e_2)=-\sigma_3S(p)^T\sigma_3$ and $S(p+\pi(1,1,1))=-S(p)^T$.
\item The character $x\mapsto e^{i\eta_0\cdot x}$, $\eta_0\in\Sigma$,
  restricted to $\Lambda_0=\{u\in\Z^3:u_1+u_2+u_3=0\}$ is trivial if and only if
  $\eta_0\in\{0,\pi u\}$.
\item There is $r_0>0$ such that, for $|\eta|\le r_0$,
  $S(\eta-i\xi_*)=\lambda(\eta)P(\eta)+\lambda(\eta)^{-1}(I-P(\eta))$ with
  $\lambda,P$ analytic, $P(0)=P$, $\|P(\eta)-P\|\le c_P|\eta|$ and
  \[
  \lambda(\eta)=\exp\Bigl(\Phi_*+iv_*\cdot\eta-\tfrac12\eta^TQ\eta+\rho_3(\eta)\Bigr),\qquad
  |\rho_3(\eta)|\le c_3|\eta|^3\le\tfrac14\eta^TQ\eta .
  \]
  Here $Q=\Hess\Phi(\xi_*)=q_t(I-\uhat\uhat^T)+q_n\uhat\uhat^T$ with
  \[
  q_t=\frac{c_*}{D_*}=0.68956\ldots,\qquad
  q_n=\frac{c_*}{D_*}\frac{(c_*^2-1)(c_*^2+2)}{c_*^4+c_*^2+1}=0.30338\ldots,\qquad D_*=\sqrt{c_*^6-1}.
  \]
\item Outside $\bigcup_{\eta_0\in\Sigma}B(\eta_0,r_0)$,
  $\|\widetilde S_N(\eta)\|\le CNe^{-cN}$ for some $c>0$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) and (b) are identities between trigonometric polynomials and are checked
by expansion.  (c): $\Lambda_0$ is generated by $e_1-e_2$ and $e_2-e_3$, so
the character is trivial on it if and only if
$\eta_{0,1}\equiv\eta_{0,2}\equiv\eta_{0,3}\pmod{2\pi}$.  (d): the
eigenvalues of $S(\eta-i\xi_*)$ are
$\exp(\pm\arcosh f(\eta-i\xi_*))$ and
$f(\eta-i\xi)=\prod_j\cosh(\xi_j+i\eta_j)$.  Hence
$\log\lambda(\eta)=\Phi(\xi_*+i\eta)$, which is holomorphic near $\eta=0$
because $\Pi(\xi_*)>1$.  Taylor expansion gives $\nabla\Phi(\xi_*)=v_*$ and
$\Hess\Phi(\xi_*)=Q$.  The explicit Hessian is
$\Hess\Phi=\frac{\Pi}{D}\operatorname{diag}(\operatorname{sech}^2\xi_j)-\frac{\Pi}{D^3}(\tanh\xi_i\tanh\xi_j)$
with $D=\sqrt{\Pi^2-1}$.  The eigenvalues $\lambda^{\pm1}$ are separated
by the gap $e^{2\Phi_*}\approx15.8$, so the spectral projector is analytic.
(e): by Lemma~\ref{lem:specrad} and compactness,
$\rho(S(\eta-i\xi_*))\le e^{\Phi_*-c'}$ away from $\Sigma$.  Conclude with
Lemma~\ref{lem:schur}.
\end{proof}

By (b), near $\pi u$ we have $S(\pi u+\eta-i\xi_*)^N=(-1)^N(S(\eta-i\xi_*)^N)^T$,
whose Perron projector is $P^T=\overline P$.  The other six points of
$\Sigma$ have the same spectral radius, but by (c) their characters are
non-trivial on the lattice planes $u\cdot x=k$.  This is why only $0$ and
$\pi u$ contribute at leading order (Lemma~\ref{lem:layers}(d)).

\subsection{Lattice-plane coordinates and profiles}
The planes $\{u\cdot x=k\}$ are orthogonal to $\xi_*$, and each is a translate
of the two-dimensional lattice $\Lambda_0$, of covolume $\sqrt3$.  Write
Alice's sites as $x=x_*-\delta\uhat+u_\perp$ with $u_\perp\perp\uhat$ and
depth $\delta=(\sqrt3R-u\cdot x)/\sqrt3$.  Since $u\cdot x\in\Z$,
\[
\sqrt3\,\delta=\theta_N+j,\qquad j\in\Z_{\ge0},\qquad \theta_N=\{\sqrt3R\}=\{\sqrt3N/4\}.
\]
Similarly $y=y_*+\delta'\uhat+u'_\perp$ with $\sqrt3\delta'=\theta_N+j'$, with
the \emph{same} $\theta_N$.  Then
$\xi_*\cdot(x-x_*)=-t_*(\theta_N+j)$ and $\xi_*\cdot(y-y_*)=t_*(\theta_N+j')$.
Moreover $u\cdot(y-x)=3N-2\lfloor\sqrt3R\rfloor+j+j'$, so
$(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$.

On the plane at depth $\delta$, exactly,
\[
F_N=\frac{64}{N^2}\varepsilon_\perp^2,\qquad
\varepsilon_\perp=\delta-\frac{\delta^2}{2R}-\frac{|u_\perp|^2}{2R}\ \ (\ge0),
\]
and therefore
$s_N=\frac{32\pi}{N^2}\varepsilon_\perp^2+O(N^{-6})$ and
$c_N=-\frac{512\pi^2}{N^4}\varepsilon_\perp^4+O(N^{-8})$ for $\delta=O(1)$.  The
same holds for $h_N$ with $\delta'$ and $u'_\perp$.  Replacing
$\varepsilon_\perp$ by $\delta-|u_\perp|^2/2R$ costs a relative $O(N^{-1})$.

\subsection{The free tail}
\begin{lemma}\label{lem:tail}
Uniformly in $y\in\Z^3$,
$\widetilde r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$, where
\[
R_0(w)=c_r\bigl[\mathcal I_0(|w|)\,I-\mathcal I_1(|w|)\,H_W(\hat w)\bigr]\dn,
\]
\[
\mathcal I_0(\rho)=4\pi\int_0^1k^2(1-k^2)^2\cos k\;j_0(k\rho)\,dk,\qquad
\mathcal I_1(\rho)=4\pi\int_0^1k^2(1-k^2)^2\sin k\;j_1(k\rho)\,dk .
\]
At the facing point $w_*=u-\uhat/4$, with $\rho_*=|w_*|=\sqrt3-\frac14$ and
$\hat w_*=\uhat$, one has
$R_0(w_*)=c_r\bigl(-\tfrac{\mathcal I_1}{\sqrt3}(1+i),\ \mathcal I_0+\tfrac{\mathcal I_1}{\sqrt3}\bigr)^T$,
with $\mathcal I_0=0.716577\ldots>0$ and $\mathcal I_1=0.132252\ldots>0$.
In particular $r(y)=N^{-3/2}R_0(y/N)+O(N^{-5/2})$ uniformly in $y\in\cB_N$,
and $r=0$ outside $\cB_N$.
\end{lemma}

\begin{proof}
For $|p|\le N^{-1}$, $S(p)=e^{-iH(p)}$ with $H$ Hermitian, analytic, and
$H-H_W=O(|p|^2)$.  Duhamel's formula gives
$\|S(p)^N-e^{-iNH_W(p)}\|\le CN|p|^2\le C/N$.  With $q=Np$,
$e^{-iH_W(q)}=\cos|q|-i\sin|q|\,H_W(\hat q)$, and the angular integrals of
$e^{-iq\cdot w}$ and $e^{-iq\cdot w}\hat q$ are $4\pi j_0$ and
$-4\pi ij_1\hat w$.  The resource enters through $g(Np)$ and is not
truncated.  The integrands defining $\mathcal I_0,\mathcal I_1$ are positive
because $k\rho_*<\pi$.  The value of $H_W(\uhat)\dn=(1+i,-1)^T/\sqrt3$ follows
by direct computation.
\end{proof}

The resource on Alice's sphere has the exact value
$N^{3/2}\varphi_N=\Phi_0(\frac14)=c_rI_b$ with
$I_b=16\pi\int_0^1k(1-k^2)^2\sin(k/4)\,dk$.  We write
$\varphi_\partial=c_rI_b$.

\subsection{Layer sums}
Let $\Psi_\delta(\tau)=\int_{\R^2}(\delta-|\sigma|^2)_+^2e^{i\tau\cdot\sigma}\,d^2\sigma$,
which is real and radial in $\tau$.  Define
\[
\cS_\pm(\tau;\theta)=\sum_{j\ge0}(\pm1)^je^{-t_*(\theta+j)}\,\Psi_{(\theta+j)/\sqrt3}(\tau),
\qquad
\Gamma_\pm(\theta)=\int_{\R^2}e^{-q_t|\tau|^2}\,\cS_\pm(\tau;\theta)^2\,d^2\tau .
\]

\begin{lemma}[Depth sums]\label{lem:depth}
Let $c_g=2\pi/(3\sqrt3)$ and $s_\omega=t_*+i\omega$.  Then
\[
\cS_+=\sum_{n\in\Z}\hat g_\tau(2\pi n)e^{2\pi in\theta},\qquad
\cS_-=\sum_{n\in\Z}\hat g_\tau\bigl(\pi(2n+1)\bigr)e^{i\pi(2n+1)\theta},\qquad
\hat g_\tau(\omega)=c_g\,\frac{e^{-|\tau|^2/(4\sqrt3\,s_\omega)}}{s_\omega^4}.
\]
Consequently $|\cS_+-\hat g_\tau(0)|\le c_g/720$ and $|\cS_-|\le c_g/48$.
Moreover
\[
\overline\Gamma:=\int e^{-q_t|\tau|^2}\hat g_\tau(0)^2d^2\tau=\frac{c_g^2}{t_*^8}\frac{\pi}{q_t+\frac1{2\sqrt3t_*}}=49.44186\ldots,
\qquad |\Gamma_+-\overline\Gamma|\le\varepsilon_+,\qquad 0\le\Gamma_-\le\varepsilon_-,
\]
with
$\varepsilon_+=2\frac{c_g}{720}\frac{c_g}{t_*^4}\frac{\pi}{q_t+1/(4\sqrt3t_*)}+\bigl(\frac{c_g}{720}\bigr)^2\frac\pi{q_t}=0.04917\ldots$
and $\varepsilon_-=\bigl(\frac{c_g}{48}\bigr)^2\frac\pi{q_t}=0.00289\ldots$.
\end{lemma}

\begin{proof}
Radially, $\Psi_\delta(\tau)=\pi H(\delta)$ with
$H(\delta)=\int_0^\delta(\delta-s)^2J_0(|\tau|\sqrt s)\,ds$.  So $H'''=2J_0(|\tau|\sqrt\delta)$
and $H(0)=H'(0)=H''(0)=0$.  Since
$\int_0^\infty e^{-ps}J_0(|\tau|\sqrt s)\,ds=e^{-|\tau|^2/4p}/p$, the function
$g_\tau(x)=e^{-t_*x}\Psi_{x/\sqrt3}(\tau)\mathbf 1_{x\ge0}$ has Fourier
transform $\hat g_\tau$ as stated.  It is continuous, vanishing to third
order at $x=0$, and $\hat g_\tau\in\ell^1(2\pi\Z)$.  Poisson summation is
therefore exact.  The bounds use $|e^{-|\tau|^2/(4\sqrt3s)}|\le1$,
$|s_{2\pi n}|\ge2\pi|n|$, $\sum_{n\ne0}(2\pi n)^{-4}=1/720$ and
$\sum_n|\pi(2n+1)|^{-4}=1/48$.  The Gaussian integrals are elementary.
\end{proof}

\begin{lemma}[Layers]\label{lem:layers}
Let $\chi\in\{\up,\dn\}$, $f=s_N\varphi_N\chi$, $w=h_N\,M_B\,r$ and
$\tau=\sqrt{N/2}\,\eta_t$, where $\eta=\eta_n\uhat+\eta_t$ with
$\eta_t\perp\uhat$.
\begin{enumerate}[label=(\alph*)]
\item $|\mathfrak A_f(\eta)|,\ \|\mathfrak B_w(\eta)\|\le CN^{-5/2}$ for all $\eta$.
\item For $|\eta|\le r_0$,
  \[
  \mathfrak A_f(\eta)=N^{-5/2}\tfrac{16\pi}{\sqrt3}\varphi_\partial\bigl[\cS_+(\tau;\theta_N)+\mathcal E_A\bigr]\chi,\qquad
  \mathfrak B_w(\eta)=N^{-5/2}\tfrac{32}{\sqrt3}\,R_0(w_*)^\dagger M_B\bigl[\cS_+(\tau;\theta_N)+\mathcal E_B\bigr],
  \]
  with $|\mathcal E_{A,B}|\le C(N^{-1/2}+|\eta_n|)$.
\item Near $\pi u$ the same holds with $\cS_-$ in place of $\cS_+$.  The
  alternating sign comes from the parity $(-1)^{N+u\cdot(y-x)}=(-1)^{j+j'}$,
  combined with $S^N\mapsto(-1)^N(S^N)^T$.
\item For $\eta_0\in\Sigma\setminus\{0,\pi u\}$ and $|\eta|\le r_0$,
  $|\mathfrak A_f(\eta_0+\eta)|\le CN^{-4}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Decompose the sums into lattice planes.  On the plane at depth
$\delta=(\theta_N+j)/\sqrt3$ the tilt weight is $e^{-t_*(\theta_N+j)}$.  The
profile $s_N\varphi_N$ is supported in a disc of radius
$\varrho=\sqrt{2R\delta-\delta^2}=O(\sqrt N)$ and has size $O(N^{-7/2}\delta^2)$.
Planes with $\delta>R/2$ contribute $O(e^{-cN})$.  This gives (a).

For (b), apply Poisson summation on each plane.  The $m=0$ term is
$\frac1{\sqrt3}\int e^{i\eta_t\cdot u_\perp}G_0(u_\perp)\,d^2u_\perp$.  The
terms $m\ne0$ are bounded by $\|\partial^3G_0\|_{\mathcal M}|2\pi m-\eta_t|^{-3}$,
since the profile vanishes quadratically on the rim and its third
derivative is a finite measure.  After the weighted depth sum, they give a
relative error $O(N^{-3/2})$.  In the $m=0$ term, use the profile
expansions, $\varphi_N=N^{-3/2}\varphi_\partial(1+O(|u_\perp|/N+\delta/N))$ and
$|e^{-i\eta_n\delta}-1|\le|\eta_n|\delta$.  With the substitution
$u_\perp=\sqrt{2R}\,\sigma$,
\[
\int e^{i\eta_t\cdot u_\perp}\Bigl(\delta-\frac{|u_\perp|^2}{2R}\Bigr)_+^2d^2u_\perp=2R\,\Psi_\delta(\tau).
\]
Collecting the factors
$\frac1{\sqrt3}\cdot\frac{32\pi}{N^2}\cdot N^{-3/2}\varphi_\partial\cdot2R$ gives
the prefactor of $\mathfrak A_f$.  For $\mathfrak B_w$ the factors are
$\frac1{\sqrt3}\cdot\frac{64}{N^2}\cdot N^{-3/2}R_0(w_*)^\dagger\cdot2R$, using
Lemma~\ref{lem:tail}, the smoothness of $R_0$ and $M_B^\dagger=M_B$.  (c)
follows from Lemma~\ref{lem:symbol}(b) and the parity identity.  (d): by
Lemma~\ref{lem:symbol}(c), the character is non-trivial on each plane.  The
Poisson sum therefore has no $m=0$ term, and the remaining terms are
$O(N^{-4})$.
\end{proof}

\subsection{Assembly}
\begin{theorem}\label{thm:T}
For $\chi\in\{\up,\dn\}$ and each $M_B$,
\[
\mathcal T_\chi(N)=N^{-13/2}\,\cK\,c_r\bigl[\Gamma_+(\theta_N)\,x_0+\Gamma_-(\theta_N)\,x_\pi\bigr]+O(N^{-7}),
\]
where $x_0=\tilde R^\dagger M_BP\chi$, $x_\pi=\tilde R^\dagger M_B\overline P\chi$,
$\tilde R=R_0(w_*)/c_r$ and
\[
\cK=\frac{128}{3\pi^2}\sqrt{\frac{2\pi}{q_n}}\;\varphi_\partial=1.749269\ldots .
\]
\end{theorem}

\begin{proof}
Insert Lemmas~\ref{lem:symbol} and~\ref{lem:layers} into
\eqref{eq:exactrep}.  Away from the balls $B(\eta_0,r_0)$ the contribution is
$O(Ne^{-cN}N^{-5})$.  The six points of $\Sigma$ with non-trivial
characters give $O(N^{-4}\cdot N^{-5/2}\cdot N^{-3/2})=O(N^{-8})$, using the
Gaussian decay of $\widetilde S_N$.  Near $\eta_0\in\{0,\pi u\}$ we make
three replacements.  First, $\widetilde S_Ne^{-iN\eta\cdot v_*}$ is replaced
by $e^{-N\eta^TQ\eta/2}P$ (respectively $\overline P$), at cost
$N^{-5}\int(c_P|\eta|+Nc_3|\eta|^3)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.
Second, the layers are replaced by their leading forms, at cost
$N^{-5}\int(N^{-1/2}+|\eta_n|)e^{-N\eta^TQ\eta/4}d\eta=O(N^{-7})$.  Third,
the integral is extended to $\R^3$, at cost $O(e^{-cNr_0^2})$.  What
remains is
\[
N^{-5}\,\frac{512\pi}{3}\,\varphi_\partial\,c_r\,x_{0,\pi}\,\sqrt{\frac{2\pi}{Nq_n}}\;\frac2N\;(2\pi)^{-3}\int_{\R^2}e^{-q_t|\tau|^2}\cS_\pm^2\,d^2\tau .
\]
Here we used $d^2\eta_t=(2/N)d^2\tau$ and
$N\eta^TQ\eta/2=Nq_n\eta_n^2/2+q_t|\tau|^2$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:main}]
By \eqref{eq:Lexp}, the $e^{-K_*N}N^{-13/2}$ sector of $L_{M,M_B}$ is
$\ell(\mathcal T_\chi)$, where $\ell$ is the real-linear functional
$-2\im$ for $M\in\{I,\sigma_1\}$, $+2\im$ for $M=\sigma_3$ and $+2\re$ for
$M=\sigma_2$, and $\chi=\dn$ for $M\in\{I,\sigma_3\}$, $\chi=\up$ for
$M\in\{\sigma_1,\sigma_2\}$.  Since $\cK$, $c_r$ and $\Gamma_\pm$ are real,
Theorem~\ref{thm:T} gives \eqref{eq:C} with $\ell_0=\ell(x_0)$ and
$\ell_\pi=\ell(x_\pi)$.  Closed forms of $\ell_0,\ell_\pi$ in terms of
$\alpha,c_*,\mathcal I_0,\mathcal I_1$ are listed in
Appendix~\ref{app:numerics}.

The remainder budget, relative to $N^{-13/2}$, is as follows:
\begin{itemize}
\item $O(N^{-1/2})$ from the cubic term of the exponent, from
  $P(\eta)-P$, from the normal phase, and from the variation of
  $\varphi_N$ and $R_0$ across the layer;
\item $O(N^{-1})$ from $r-N^{-3/2}R_0$ and from the exact profile and disc
  geometry;
\item $O(N^{-3/2})$ from in-plane Poisson terms and from the six
  non-contributing torus points;
\item $O(N^{-2})$ from $2\re\langle r,Ea_c\rangle$;
\item exponentially small terms from the region away from $\Sigma$ and from
  the sector $e^{-2K_*N}$.
\end{itemize}
Hence $L=e^{-K_*N}N^{-13/2}(C(\theta_N)+R_N)$ with $|R_N|\le C'N^{-1/2}$.

For non-vanishing, note that $\Gamma_-\ge0$.  For every pair, interval
arithmetic certifies $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$.
Therefore $C(\theta)$ has the sign of $\ell_0$ for every $\theta$, and
$|C(\theta)/\overline C-1|\le(\varepsilon_+|\ell_0|+\varepsilon_-|\ell_\pi|)/(\overline\Gamma|\ell_0|)$,
which gives the bounds of Table~\ref{tab:C}.  Since
$\inf_\theta|C(\theta)|\ge(1-1.5\cdot10^{-3})|\overline C|>0$, the remainder
cannot cancel the leading term for $N$ large, and the asymptotics of
$\delta=|L|$ follow.
\end{proof}

\begin{remark}[Counting the power]
The exponent $13/2$ decomposes as follows.  The resource contributes
$\frac32$ at the layer and the free tail $\frac32$ at Bob.  The profiles
$s_N$ and $h_N$ contribute $2+2$.  The two in-plane areas contribute $-2$.
The normal Gaussian contributes $\frac12$, and the tangential rescaling
$d^2\eta_t=(2/N)d^2\tau$ contributes $1$.  The depths $j,j'$ are discrete
sums of size $O(1)$ and contribute no power.  The common tangential
direction $u_\perp+u'_\perp$ is a flat direction of the exponent, because
$\xi_*$ is orthogonal to the planes.  It is confined by the profiles and
produces the area factors, not a Gaussian factor.
\end{remark}

\begin{remark}[Dependence on $\theta_N$]
Since $\sqrt3/4\notin\mathbb Q$, the sequence $\theta_N$ is equidistributed.
$C(\theta_N)$ is therefore quasi-periodic in $N$ and not a constant.  The
oscillation comes from the commensurability of the lattice planes with the
spheres bounding the regions.  It is below $0.15\%$, and it never changes
the sign.
\end{remark}

\section{Discussion}\label{sec:discussion}

\subsection{What the theorem says and does not say}
The theorem is a statement about one walk and one explicitly specified
family of operations.  It shows that the gap between the emergent
relativistic cone and the microscopic causal support is not merely
geometric.  Under an infrared-controlled protocol it carries an
operational response whose asymptotic law is known exactly: rate, power
and coefficient.  It does not claim that $D_B>0$ for every protocol, that
every quantum walk behaves this way, or that every smooth encoder
$M=aI+b\cdot\sigma$ signals.  It is not a violation of the model's
microcausality, since Bob remains inside $N\Cmicro$.  The limit
$N\to\infty$ is an infrared scaling at fixed lattice units, not a continuum
limit $a,\tau\to0$.

The result is asymptotic.  The remainder constants and $N_*$ are finite but
not explicit.  The finite-$N$ diagnostics of Appendix~\ref{app:numerics}
indicate an effective relative correction of about $-100/N$.  The leading
formula is therefore quantitatively reliable only for $N\gtrsim10^3$.  For
$M\in\{I,\sigma_3\}$ with $M_B=I$, whose coefficient is among the smallest,
the $N^{-17/2}$ term dominates over the whole diagnostic range.

\subsection{Physical reading}
Restoring a lattice spacing $a$, the integer $N$ is both the number of
steps and the separation scale in lattice units, so $N\sim\ell/a$ for a
separation $\ell$, and $\delta\sim e^{-K_*N}$ up to algebraic factors.  The
response is therefore negligible at any separation large compared with the
lattice spacing, and by the preceding subsection the leading formula becomes
accurate only for $N\gtrsim10^3$.  We make no claim about observability, and
regard the result as a statement in the mathematical physics of finite-range
unitary dynamics.
Its interest lies in the structure it exhibits: an exact separation between
ballistic propagation, which respects $\cIR$, and operational influence,
which does not vanish inside the corona even under infrared control.

\subsection{Open problems}
\begin{enumerate}[label=(\arabic*)]
\item General encoders $M=aI+b\cdot\sigma$, and optimisation over
  admissible operations.
\item Other walks, in particular the Bialynicki-Birula walk
  \cite[Eq.~(5.12)]{CJWW}, whose corona contains ballistic modes faster than
  $\cIR$, and the massive Dirac case.
\item Explicit remainder constants and $N_*$, which would make the
  statement effective at finite $N$.
\item Many-particle and second-quantized versions.  The upper bound
  extends to even local unitaries on the full CAR algebra, with prefactor
  $288N^7$ in place of $36N^4$~\cite{Repo}, but no lower bound is available
  there.
\end{enumerate}

\appendix

\section{Computer-assisted parts and diagnostics}\label{app:numerics}

Theorem~\ref{thm:upper}, together with Lemma~\ref{lem:ellipse}, is
formally verified in Lean~4/Mathlib (\texttt{formal/} in~\cite{Repo}).  The
asymptotic results (Theorems~\ref{thm:rate} and~\ref{thm:main}) are not.
The analytic arguments above are complete up to the following verified
computations.  All of them are performed by the certificate scripts listed
in~\cite{Repo}, at the commit given there, with Python~3.12.3, SymPy~1.14.0
and mpmath~1.3.0.  Exact identities use SymPy.  Enclosures use the interval
context \texttt{mpmath.iv} with 50 digits, and only its elementary
operations: the four arithmetic operations, integer powers by repeated
multiplication, $\sqrt{\cdot}$, $\exp$, $\log$, $\sin$, $\cos$ and $\pi$.
No interval quadrature is used: $\mathcal I_0(\rho_*)$, $\mathcal I_1(\rho_*)$
and $I_b$ are enclosed through exact closed forms in $\sin$ and $\cos$,
obtained from the moments $\int_0^1k^m\{\sin,\cos\}(\omega k)\,dk$, $m\le5$,
which are checked symbolically.
\begin{itemize}
\item The symbol identities: Lemma~\ref{lem:jumps}, \eqref{eq:SOS}, and
  Lemma~\ref{lem:symbol}(a)--(b).  Also the ellipse-lemma polynomials,
  $\cosh^3(\log2)=125/64$ and the vertex blocks.
\item Closed forms and enclosures of $t_*$, $K_*$, $c_*^2$, $\Phi_*$,
  $q_t$, $q_n$, $P$, $\mathcal I_0$, $\mathcal I_1$, $\varphi_\partial$, $\cK$,
  $\overline\Gamma$ and $\varepsilon_\pm$.
\item The sixteen pairs $(\ell_0,\ell_\pi)$, the sign margin
  $|\ell_0|(\overline\Gamma-\varepsilon_+)>\varepsilon_-|\ell_\pi|$, the
  bounds of Table~\ref{tab:C}, and $C(\sigma_3,\cdot)=-C(I,\cdot)$.
\end{itemize}
Closed forms of $\ell_0,\ell_\pi$ are given below, with $c=c_*$,
$A=\mathcal I_0(\rho_*)$ and $B=\mathcal I_1(\rho_*)$.  The rows for
$\sigma_3$ are the negatives of the rows for $I$.

{\small
\[
\begin{array}{lll}
\toprule
(M,M_B) & \ell_0 & \ell_\pi\\
\midrule
(I,I),(I,P_3) & -\frac{\sqrt3}{3}\frac{B\alpha(c-1)}{c^2} & +\frac{\sqrt3}{3}\frac{B\alpha(c+1)}{c^2}\\[3pt]
(I,P_1) & \frac{3Ac\alpha-\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2} & -\frac{3Ac\alpha+\sqrt3B(c^2\alpha+c^2-\alpha)}{6c^2}\\[3pt]
(I,P_2) & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2+c\alpha-2\alpha)}{6c^2} & \frac{3A\alpha-\sqrt3B(c^2\alpha+c^2-c\alpha-2\alpha)}{6c^2}\\[3pt]
(\sigma_1,I) & -\frac{3A\alpha+\sqrt3B(c-c\alpha+\alpha)}{3c} & \frac{3A\alpha-\sqrt3B(c-c\alpha-\alpha)}{3c}\\[3pt]
(\sigma_1,P_1) & -\frac{3Ac\alpha+\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2} & \frac{3Ac\alpha-\sqrt3B(c^2-c^2\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_2) & -\frac{3A(c^2(1-\alpha)+c\alpha)+\sqrt3B(2c^2(1-\alpha)+2c\alpha-\alpha)}{6c^2} & -\frac{3A(c^2(1-\alpha)-c\alpha)+\sqrt3B(2c^2(1-\alpha)-2c\alpha-\alpha)}{6c^2}\\[3pt]
(\sigma_1,P_3),(\sigma_2,P_3) & -\frac{\sqrt3}{3}B(1-\alpha) & -\frac{\sqrt3}{3}B(1-\alpha)\\[3pt]
(\sigma_2,I) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+\alpha)}{3c^2}\\[3pt]
(\sigma_2,P_1) & -\frac{3A(\alpha-c^2(1-\alpha))+\sqrt3Bc\alpha}{6c^2} & -\frac{3A(\alpha-c^2(1-\alpha))-\sqrt3Bc\alpha}{6c^2}\\[3pt]
(\sigma_2,P_2) & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)+c\alpha+2\alpha)}{6c^2} & -\frac{3A\alpha+\sqrt3B(c^2(1-\alpha)-c\alpha+2\alpha)}{6c^2}\\
\bottomrule
\end{array}
\]
}

\medskip\noindent\emph{Finite-$N$ diagnostics.}  These are floating-point
and not used in any proof; they use NumPy~1.26.4 and are produced by the
\texttt{--diagnostics} option of the coefficient certificate~\cite{Repo}.  A
floating-point FFT evaluation of the exact discrete convolution formula in
tilted variables (``brute'') was compared with a reference that keeps the
exact lattice geometry but replaces the kernel by its Gaussian form at the
eight points of $\Sigma$.  Their ratio tends to $1$ with deviation of order
$c/N$, $c\in[-0.5,14]$, at $N=24,40,56$.  For $M\in\{I,\sigma_3\}$ and
$M_B=I$, the ratio of the $N^{-17/2}$ piece $2\re\langle r,Ea_c\rangle$ to
the piece $2\im\langle r,Ea_\dn\rangle$ that carries the $N^{-13/2}$ term is
$15.2$, $9.4$ and $6.4$ at $N=24,40,56$.  A semi-analytic evaluation with discrete
planes and exact profiles gives semi/lead $=0.906$, $0.990$ and $0.997$ at
$N=10^3$, $10^4$ and $3\cdot10^4$, consistent with a relative correction
$\approx-100/N$.  The free tail agrees with $N^{-3/2}R_0$ to relative
accuracy $2\cdot10^{-6}$ at $N=40$ and $8\cdot10^{-9}$ at $N=640$.

\begin{thebibliography}{99}

\bibitem{AVWW}
A.~Ahlbrecht, H.~Vogts, A.~H.~Werner, R.~F.~Werner,
\emph{Asymptotic evolution of quantum walks with random coin},
arXiv:1009.2019.

\bibitem{Arrighi}
P.~Arrighi,
\emph{An overview of quantum cellular automata},
arXiv:1904.12956.

\bibitem{BBBP}
Y.~Baryshnikov, W.~Brady, A.~Bressler, R.~Pemantle,
\emph{Two-dimensional quantum random walk},
J.\ Stat.\ Phys.\ \textbf{142}, 78--107 (2011), arXiv:0810.5495.

\bibitem{BialynickiBirula}
I.~Bialynicki-Birula,
\emph{Weyl, Dirac, and Maxwell equations on a lattice as unitary cellular automata},
Phys.\ Rev.\ D \textbf{49}, 6920 (1994), arXiv:hep-th/9304070.

\bibitem{BDPT}
A.~Bisio, G.~M.~D'Ariano, P.~Perinotti, A.~Tosini,
\emph{Free quantum field theory from quantum cellular automata: derivation of Weyl, Dirac and Maxwell quantum cellular automata},
arXiv:1601.04832.

\bibitem{BHS}
L.~Bombelli, J.~Henson, R.~D.~Sorkin,
\emph{Discreteness without symmetry breaking: a theorem},
arXiv:gr-qc/0605006.

\bibitem{BHV}
S.~Bravyi, M.~B.~Hastings, F.~Verstraete,
\emph{Lieb--Robinson bounds and the generation of correlations and topological quantum order},
Phys.\ Rev.\ Lett.\ \textbf{97}, 050401 (2006), arXiv:quant-ph/0603121.

\bibitem{CRT}
H.~A.~Carteret, B.~Richmond, N.~M.~Temme,
\emph{Evanescence in coined quantum walks},
J.\ Phys.\ A: Math.\ Gen.\ \textbf{38}, 8641--8665 (2005), arXiv:quant-ph/0506048.

\bibitem{CJWW}
C.~Cedzich, A.~Joye, A.~H.~Werner, R.~F.~Werner,
\emph{Exponential tail estimates for quantum lattice dynamics},
Ann.\ Henri Poincar\'e \textbf{27}, 2843--2870 (2026), doi:10.1007/s00023-025-01598-4, arXiv:2408.02108.

\bibitem{DArianoErbaPerinotti}
G.~M.~D'Ariano, M.~Erba, P.~Perinotti,
\emph{Isotropic quantum walks on lattices and the Weyl equation},
Phys.\ Rev.\ A \textbf{96}, 062101 (2017), arXiv:1708.00826.

\bibitem{DArianoPerinotti}
G.~M.~D'Ariano, P.~Perinotti,
\emph{Derivation of the Dirac equation from principles of information processing},
Phys.\ Rev.\ A \textbf{90}, 062106 (2014), arXiv:1306.1934.

\bibitem{Farrelly}
T.~Farrelly,
\emph{A review of quantum cellular automata},
Quantum \textbf{4}, 368 (2020), arXiv:1904.13318.

\bibitem{GJS}
G.~Grimmett, S.~Janson, P.~F.~Scudo,
\emph{Weak limits for quantum random walks},
Phys.\ Rev.\ E \textbf{69}, 026119 (2004), arXiv:quant-ph/0309135.

\bibitem{Konno}
N.~Konno,
\emph{Quantum random walks in one dimension},
Quantum Inf.\ Process.\ \textbf{1}, 345--354 (2002).

\bibitem{LiebRobinson}
E.~H.~Lieb, D.~W.~Robinson,
\emph{The finite group velocity of quantum spin systems},
Commun.\ Math.\ Phys.\ \textbf{28}, 251--257 (1972).

\bibitem{ACSV}
R.~Pemantle, M.~C.~Wilson, S.~Melczer,
\emph{Analytic Combinatorics in Several Variables}, 2nd ed.,
Cambridge University Press (2024), doi:10.1017/9781108874144.

\bibitem{Repo}
Repository \texttt{nacho09021973/qca-causal-cones},
% TODO(author): replace by an archived release (tag and DOI) before submission.
\url{https://github.com/nacho09021973/qca-causal-cones}, commit
\texttt{551addabe28b} (branch \texttt{research/b-infinity-post-s4-gate}).
Certificates
\texttt{scripts/verify\_scaled\_ir\_gate.py},
\texttt{scripts/verify\_regional\_directional\_asymptotics\_gate.py},
\texttt{scripts/verify\_regional\_laplace\_coefficient\_gate.py},
\texttt{scripts/verify\_directional\_saturation.py}; Lean formalization in
\texttt{formal/}.

\bibitem{SchumacherWerner}
B.~Schumacher, R.~F.~Werner,
\emph{Reversible quantum cellular automata},
arXiv:quant-ph/0405174.

\bibitem{SunadaTate}
T.~Sunada, T.~Tate,
\emph{Asymptotic behavior of quantum walks on the line},
J.\ Funct.\ Anal.\ \textbf{262}, 2608--2645 (2012), arXiv:1108.1878.

\end{thebibliography}

\end{document}
```


## Ronda 1 — ABNER

La versión más fuerte del informe reparado es esta: los cuatro términos lineales quedan representados exactamente por `A_{cP/Q}=2e^{-K_*N}Re⟨F w~_c,π_c(P/Q)t_N⟩`, con `w_c^{fis}=E r_c` y `w~_c` su versión inclinada; la potencia `N^{-3}` sólo se hereda en Alice como `PRELIMINARY_BOUND`; Bob no dispone de cota `O(N^{-3})` para `ϑ≠0`; las cotas `N^{-5}`/`N^{-6}` son superiores y no prueban subdominancia ni supervivencia de la señal. [SOURCE] Esa es la lectura que hay que atacar, no la versión que atribuiría a Schur certidumbre sobre (7)–(8), ni la que convertiría el recuento formal `N^{-3}·N^{-1}·N^{-3}=N^{-7}` en teorema. [RECONSTRUCTION]

El punto más débil es la afirmación negativa sobre Bob, punto 2 del encargo. La objeción más fuerte es la siguiente: la no-invariancia por traslación de `U_N` descalifica un mecanismo concreto —la representación de Fourier con `S(p)^N` unitaria puntualmente en el toro—, pero no demuestra que no exista ninguna cota de capa para `r_c`. [INFERENCE] Es la diferencia entre “la vía plana no se transfiere” y “no hay cota actual”. [INFERENCE] El informe, sin embargo, no comete el ascenso: dice explícitamente que su conclusión no prueba que no exista otra deducción. [SOURCE] Por tanto, para que esta objeción derrotara la versión reparada tendría que exhibirse, dentro del material adjunto, una cota puntual de capa de `r_c=Bπ_cU_N^NJφ_N` con moneda no invariante, del tipo `sup_y∈B‖r_c(y)‖=O(N^{-3/2})` o `‖r_c‖_{ℓ²(capa j')}=O(N^{-1}a_{j'})` con sumabilidad inclinada. [ORIGINAL]

Esa cota no consta. [ABSENCE] Busqué en el informe de Schur reparado, en T1, en el informe de normas de reconstrucción y en la nota regional: Schur da `‖t_j‖₂≤C(W,Θ)‖s‖₂`, no `sup_y‖r_c(y)‖`; T1 es algebraico; el informe de normas acota `E^{1/2}V_cP/Q`, no la referencia con moneda; la nota regional da decaimiento exponencial para el walk libre `S^N`, no para `U_N^N`. [ABSENCE] La cota exponencial del walk libre, además, no es la cota polinomial buscada: al sumar sobre Alice produce, en todo caso, un orden `N^{5/2}e^{-K_*N}` para el extremo plano, y no cubre `U_N`. [INFERENCE] Luego la objeción no prospera y la afirmación de Bob queda como `NO_CURRENT_BOUND` en el sentido limitado que el propio informe declara. [INFERENCE]

Un segundo foco de debilidad, menor, es la descomposición de `y_N` en el punto 3. Es exacta por sustitución de la identidad T1 (14): `y_N=G_Q(N,0)Qs+Σ_{k<N}G_Q(N,k+1)C_kx_k`, con `x_k=x_k^{stay}+f_{Q,k}+(𝕄x)_k`. [SOURCE] Las cotas resultantes no particionan mal ni hacen dominante el último paso; la cota `O(N^{-4})` para `y_N` depende de sumas tipo `𝕄_N` que están fuera del PASS y quedan etiquetadas `PRELIMINARY_BOUND`. [INFERENCE] La condición que desactivaría una objeción aquí sería mostrar que esas sumas están cubiertas por el PASS de Schur; no lo están, porque el PASS se limita a `‖t_j‖₂` uniforme y no a bloques acumulados. [SOURCE] No hay ascenso causal en ese punto. [INFERENCE]

Sobre la versión reparada no encuentro un primer paso que falle. El único punto que podría fallar es el 2, y no falla porque el material adjunto no contiene la cota alternativa que exigiría la objeción. Mi veredicto es `PASS`. [INFERENCE]

## Ronda 1 — CLAUDE OPUS

Concuerdo con ABNER en dos cosas y las doy por establecidas para no repetirlas: su reconstrucción de la versión fuerte del informe es la correcta, y el punto 2 no cae, porque el informe no asciende de «la vía plana no transfiere» a «no existe ninguna vía» — lo dice literalmente: «Esto respalda `NO_CURRENT_BOUND` con el material adjunto; no prueba que no exista otra deducción». [SOURCE] Donde su turno se queda corto es en el modo del ataque: buscó la cota alternativa y no la halló. Eso es `[ABSENCE]` sobre un catálogo. Es más fuerte construir la vía y medir dónde muere.

**Ataque construido al punto 2, y su fracaso cuantificado.** El encargo pide atacar si con el material adjunto existe un argumento que dé `O(N^{-3})` sin invariancia por traslación de `U_N`. Hay uno candidato que el informe no considera: usar Duhamel en el orden *inverso* al que usa §2.2. En vez de `U_N^N−D^N=Σ_kU_N^{N−1−k}(C_N−I)D\,D^k`, tomar `U_N^N−D^N=Σ_kD^{N−1−k}(C_N−I)U_N^k`. [ORIGINAL] Así el propagador invariante por traslación queda a la izquierda, es el último en actuar, y sobre él sí vale el mecanismo puntual de la nota plana §3(b). En concreto, con `dμ=d³p/(2π)³` sobre `[−π,π)³` se tiene `∫dμ=1`, luego para cualquier `v` y cualquier `m`, `sup_y‖(S^mv)(y)‖ ≤ ∫‖S(p)^m\hat v(p)‖dμ ≤ ∫‖\hat v‖dμ ≤ ‖v‖_2`, usando sólo que `S(p)` es unitaria en el toro real y Cauchy–Schwarz con μ de masa uno. [INFERENCE]

La vía funciona algebraicamente y falla numéricamente. Con `v_k=(C_N−I)U_N^kJφ_N` y `‖C_N−I‖≤Θ/N`, `‖U_N^kJφ_N‖=1`, sale `sup_y‖(D^{N−1−k}v_k)(y)‖ ≤ Θ/N` por término, y hay `N` términos: `sup_y‖δr_+(y)‖ = O(1)`, sin decaimiento. [INFERENCE] Peor aún, si esa cota puntual se introduce en la geometría de capas del propio informe (`#_{j'} ≲ kN(1+j')`, peso `e^{−2t_*j'}`, `h_N ≤ 64s²/N²`), el resultado es `‖Eδr_+‖_{ℓ²_tilt} ≲ N^{-2}·N^{1/2}=N^{-3/2}`, estrictamente **peor** que la cota `C_BΘN^{-2}` que el informe ya tiene por `‖r_c‖_2≤1`. [INFERENCE] Lo que hace falta para que la vía compita es `sup_y‖U_N^kJφ_N(y)‖=O(N^{-3/2})` uniformemente en `k≤N`, es decir, conservación de la concentración en la banda `|p|≲N^{-1}` bajo `N` convoluciones con el núcleo `K_N(q)=N³\hatϑ(Nq)`. Ese enunciado es exactamente la clase del paso no resuelto (ii) de `2026-09-20--h1-inhomogeneous-localization-reconstruction.md` §9, registrado como `H1c_LOCALIZATION (L') = OPEN`. [SOURCE] Condición de concesión de mi propio ataque, y por tanto de su desactivación: se reactivaría si se probara esa conservación de banda uniforme en `k`; con el material adjunto no está, y su ausencia no es accidental sino la de un gate declarado abierto. [INFERENCE] Conclusión: el punto 2 sobrevive por una razón más fuerte que la del informe y que la de ABNER — la vía natural que esquiva la invariancia por traslación existe, es explícita, y rinde `N^{-3/2}`, no `N^{-3}`.

**Verificaciones aritméticas que faltaban.** El punto 3 pide que `N_0` y `q` sean correctos, y eso no se ha comprobado, sólo se ha descrito. Con `q=(1+ρ_1)/2` y `ρ_2=ρ_1(1+C_0C_QΘ/N)`, la desigualdad `ρ_2≤q` equivale a `ρ_1C_0C_QΘ/N ≤ (1−ρ_1)/2`, es decir `N ≥ 2ρ_1C_0C_QΘ/(1−ρ_1)`, que es precisamente el `N_0:=max{2,⌈2ρ_1C_0C_QΘ/(1−ρ_1)⌉}` escrito en §4. Correcto y ajustado, no conservador de más. [INFERENCE] Del punto 1 verifico los dos exponentes: `c_Nb_N ≍ (δ²/N²)²·N^{-3/2} = N^{-11/2}δ⁴` con `δ≤(1+j)/√3`, cuadrado `N^{-11}(1+j)^8e^{-2t_*j}`, multiplicidad `kN(1+j)` y suma en `j` convergente dan `N^{-5}`; con `s_N ≍ N^{-2}δ²` el mismo cómputo da `N^{-3}`. Ambos coinciden con lo escrito y con `c_N=−512π²ε_⊥⁴/N⁴+O(N^{-8})` del TeX §Lattice-plane coordinates. [INFERENCE] El punto 4 también cierra: `C_BN^{-2}·O(N^{-3})=N^{-5}` con sólo el PASS, `C_BN^{-2}·O(N^{-4})=N^{-6}` con las sumas de clase L3, y el informe atribuye cada potencia a su fuente. [INFERENCE]

**Disenso delimitado: tres cosas que el informe registra mal, ninguna de ellas un paso que falle.**

Primera, y la más sustantiva. T1 §2 dice literalmente: «Toda cota posterior deberá retener esa dependencia [de `W`], salvo prueba separada de uniformidad.» [SOURCE] La nota de Schur refuerza: «No hay uniformidad en `W` recuperable de esta prueba». [SOURCE] La tabla final del informe de transferencia escribe `POWER_OF_N = N^{-5}`, `N^{-6}`, `N^{-7}` sin `O_{W,Θ}`, y la conclusión repite `N^{-5}`/`N^{-6}`/`N^{-7}` desnudos; sólo la fila `A_{-P}` anota «(`Θ`-dep.)», cuando las cuatro filas dependen de `W` y de `Θ` a través de `C_P`, `C_Q`, `C_0`, `e^κ`, `ρ_1`, `N_0` y `C_B` (éste último vía `t_*`, que no depende de `W`). [INFERENCE] La comparación asintótica con `N^{-13/2}` sigue siendo válida para cada `W` fijo, porque el coeficiente del líder es absoluto y las constantes no dependen de `N`; el defecto es de registro, no de derivación. [INFERENCE] Condición de desactivación: escribir `O_{W,Θ}(N^{-k})` en la tabla y en §7, o añadir una columna de dependencia paramétrica.

Segunda, dentro del punto 5. L1 pide la cota de capa «uniformemente en los parámetros declarados (`W`, `Θ`)». Leído como uniformidad **en** `W`, L1 exige más de lo que exige el resto del informe y más de lo que la fuente admite que sea posible (Schur §4, cierre). [INFERENCE] Leído como «para cada `W`, `Θ` declarados, con constantes que dependen de ellos y uniformidad en `j'` y en `N`», es lo justo. El encargo pregunta si algún lema está formulado con más de lo que exige: éste puede estarlo, y la ambigüedad es del texto, no de quien lo lee. Condición de desactivación: sustituir «uniformemente en los parámetros declarados (W, Θ)» por «para cada `W` admisible y `Θ` fijos, con constantes `C(W,Θ)` y uniformidad en `j'` y en `N`».

Tercera, en el punto 6. §0 establece que a `ϑ=0` `A_{+Q}` es exponencialmente pequeño: `d_{+,Q}=e^{-K_*N}V_+M^NQs` con `‖M^N‖≤C_0ρ_1^N`. [SOURCE] De ahí se sigue que a `ϑ=0` `A_{+Q}=O(ρ_1^Ne^{-K_*N})=o(N^{-13/2}e^{-K_*N})`: la subdominancia de `A_{+Q}` **está** probada en `ϑ=0`, sin L1. [INFERENCE] Pero la fila `A_{+Q}` de la tabla dice «**NO PROBADO**; `o(N^{-13/2})` (`N^{-7}`) sólo si L1», sin condicionarse a `ϑ≠0`, mientras la fila `A_{-P}` sí anota «(`=0` si `ϑ=0`)» y la fila `A_{+P}` afirma justamente lo contrario sobre `ϑ=0`. La tabla mezcla, en la misma columna, filas condicionadas a `ϑ≠0` y filas que hablan de `ϑ=0`. [INFERENCE] La lista de excepciones de §7 hereda el defecto: enumera `A_{+P}` y los dos `A_{-}` a `ϑ=0` y omite `A_{+Q}`. Condición de desactivación: anotar en la fila `A_{+Q}` y en §7 que a `ϑ=0` es `O(ρ_1^Ne^{-K_*N})` y por tanto subdominante allí, o bien declarar explícitamente que toda la columna `SUBDOMINANT_TO_N^{-13/2}?` se refiere a `ϑ≠0` y mover la observación de `A_{+P}` fuera de la tabla.

Cuarta, menor y sin consecuencia. §§3–4 usan `x_k^{stay}`, `f_{Q,k}`, `(𝕄x)_k` a índice `k` arbitrario y dicen «usa exactamente T1 (14)»; T1 (14) está escrito para el índice `N`. La extensión es inmediata (la misma sustitución sucesiva de (13) vale para todo índice) [INFERENCE], pero «exactamente T1 (14)» describe una familia `(14)_k` que la fuente no enuncia. Condición de desactivación: una línea señalando que (14) vale para todo `1≤k≤N` con los mismos transportes. Añado que la cota de `(𝕄x)_k` no se obtiene de la descomposición sino de la cota a priori `‖x_k‖_2≤ν_k≤e^κν_0` del PASS: no es circular, pero por eso lo de §4 es una mayoración triangular con tres sumandos y no una «partición exacta» en el sentido de que las tres filas recompongan `‖y_N‖`. La etiqueta «partición exacta» es más fuerte que el uso; el uso es correcto.

No encuentro un primer paso que falle en la derivación de la versión reparada: los seis puntos del encargo se sostienen, y los dos que más carga soportan —la afirmación negativa sobre Bob y la no atribución de `N^{-6}` al PASS de Schur— resisten un ataque construido, no sólo una búsqueda. Lo que falla es el registro: la dependencia en `(W,Θ)` que la fuente ordena retener, la uniformidad ambigua de L1 y la lista incompleta de casos `ϑ=0`. Ninguna de las tres convierte una cota preliminar en resultado certificado ni altera `ENDPOINT_TRANSFER_PARTIAL`. Mi veredicto es `PASS_WITH_REPAIRS`, y discrepo por tanto del `PASS` de ABNER sólo en esa medida: las tres reparaciones son de etiquetado y alcance, y las tres son verificables en el material adjunto.

## Ronda Residuo — ABNER

Suscribo el residuo de CLAUDE OPUS: PASS_WITH_REPAIRS. Mi PASS previo no registró dos defectos de alcance que tocan los puntos 5 y 6: la omisión de `O_{W,Θ}` en la tabla final y en §7, y la ambigüedad de L1 sobre uniformidad en `W`. [INFERENCE]

Queda en pie: la representación exacta de los cuatro términos; la negación de `O(N^{-3})` para Bob con `ϑ≠0`; la no atribución de `A_{cQ}=O(N^{-6})` al PASS de Schur. [SOURCE] El ataque por Duhamel inverso es explícito y rinde `N^{-3/2}`, peor que `C_BΘN^{-2}`; su reactivación exigiría conservación de banda uniforme de `U_N^kJφ_N`, que es `H1c_LOCALIZATION`, abierto. [INFERENCE]

Debe abandonarse la etiqueta “partición exacta” si se lee como recomposición de normas; el uso triangular a tres sumandos es correcto. [INFERENCE] No justificada todavía: la subdominancia de `A_{+Q}` para `ϑ≠0` sin L1, y la cota de capa de `r_c` con moneda no invariante. [INFERENCE] Acepto la corrección de registro: `A_{+Q}` a `ϑ=0` es exponencialmente pequeño, pero eso no se extiende a `ϑ≠0`. [INFERENCE]

## Ronda Residuo — CLAUDE OPUS

En pie: las tres reparaciones que enumeré, verificables en el adjunto, y la resistencia del punto 2 al ataque por Duhamel inverso. [INFERENCE] La concesión de ABNER no añade verificación: coincide con mi turno sobre un texto que ambos tenemos delante, y el material adjunto ya bastaba. [INFERENCE]

Debe abandonarse, además de «partición exacta»: la lectura de `N^{-5}`/`N^{-6}` como potencias absolutas: son `O_{W,Θ}` y sólo cotas superiores, sin cota inferior ni asintótica para ningún `A_{cP}`, `A_{cQ}`. [SOURCE]

No justificado todavía, más allá de lo que ABNER señala: que L1 sea demostrable —nadie ha exhibido una vía, y su ausencia coincide con `H1c_LOCALIZATION = OPEN` [SOURCE]—; y que este sanedrín autorice registrar el informe. Astra no confirmó la versión reparada (`QUOTA`) [SOURCE]; dos revisores en una ronda sellada no sustituyen la revisión que el propio informe declara pendiente. [INFERENCE]

Discrepancia residual con ABNER: ninguna sustantiva tras su concesión. Veredicto: `PASS_WITH_REPAIRS`, con las tres reparaciones de registro —`O_{W,Θ}` en tabla y §7, uniformidad de L1 acotada a `W`, `Θ` fijos, y `A_{+Q}` a `ϑ=0` en la lista de excepciones—; `ENDPOINT_TRANSFER_PARTIAL` inalterado.

## Ronda Veredicto — ABNER

1. ACUERDO

- Veredicto final de los dos turnos residuales: `PASS_WITH_REPAIRS` sobre la versión reparada del informe de transferencia. [SOURCE]
- No se identifica un primer paso que falle en la derivación; los seis puntos del encargo resisten, incluida la afirmación negativa sobre Bob para `ϑ≠0`. [SOURCE]
- La versión fuerte del informe es la que ambos miembros tomaron como objeto: representación exacta de los cuatro términos lineales con `w_c^{fis}=E r_c` y su versión inclinada, `ENDPOINT_TRANSFER_PARTIAL`, Alice hereda `O(N^{-3})` sólo como `PRELIMINARY_BOUND`, Bob no dispone de `O(N^{-3})` para `ϑ≠0`, y `N^{-5}`/`N^{-6}` son cotas superiores que no prueban subdominancia ni supervivencia de la señal. [SOURCE]
- El punto 2 sobrevive por una razón más fuerte que la mera ausencia de cota alternativa: el ataque por Duhamel inverso, construido por CLAUDE OPUS, existe y es explícito, pero rinde `N^{-3/2}`, estrictamente peor que `C_BΘN^{-2}`; su reactivación exigiría conservación uniforme de banda de `U_N^k Jφ_N`, que corresponde a `H1c_LOCALIZATION (L') = OPEN`. [SOURCE]
- El punto 4 se sostiene: el informe no atribuye `A_{cQ}=O(N^{-6}e^{-K_*N})` al PASS de Schur; con sólo el PASS sale `N^{-5}`, y la mejora a `N^{-6}` depende de sumas de clase L3, correctamente etiquetadas `PRELIMINARY_BOUND`. [SOURCE]
- La discrepancia inicial entre `PASS` y `PASS_WITH_REPAIRS` se cerró cuando ABNER adoptó las reparaciones de registro identificadas por CLAUDE OPUS. [SOURCE]
- Las tres reparaciones acordadas son: escribir `O_{W,Θ}(N^{-k})` en la tabla final y en §7, o consignar la dependencia paramétrica en todas las filas; reformular L1 para `W` y `Θ` fijos, con constantes `C(W,Θ)` y uniformidad en `j'` y en `N`; y registrar que `A_{+Q}` a `ϑ=0` es `O(ρ_1^N e^{-K_*N})`, por tanto subdominante allí, o declarar explícitamente que la columna de subdominancia se refiere a `ϑ≠0` y mover la observación de `A_{+P}` fuera de la tabla. [SOURCE]
- `ENDPOINT_TRANSFER_PARTIAL` queda inalterado: ninguna de las tres reparaciones convierte una cota preliminar en resultado certificado. [SOURCE]

2. DESACUERDO VIVO

- No subsiste desacuerdo sustantivo. [SOURCE]
- La única discrepancia residual que tuvo contenido, la de `PASS` frente a `PASS_WITH_REPAIRS`, quedó resuelta por la adhesión de ABNER a las tres reparaciones de registro. [SOURCE]
- Lo que queda pendiente no es objeto de disenso entre los miembros, sino trabajo previo a un hipotético cierre. [INFERENCE]

3. ABANDONADO

- El `PASS` inicial de ABNER queda abandonado: su propio turno residual lo reemplaza por `PASS_WITH_REPAIRS` al reconocer la omisión de `O_{W,Θ}` y la ambigüedad de L1. [SOURCE]
- La lectura de `N^{-5}`, `N^{-6}` y del condicional `N^{-7}` como potencias absolutas o independientes de `W` y `Θ` queda abandonada: son cotas superiores `O_{W,Θ}`, sin cota inferior ni asintótica para ningún `A_{cP}`, `A_{cQ}`. [SOURCE]
- La etiqueta “partición exacta” queda abandonada si se lee como recomposición de normas en §4; el uso correcto es una mayoración triangular de tres sumandos, no una reconstrucción de `‖y_N‖` a partir de las tres filas. [SOURCE]
- La pretensión de que el ataque por Duhamel inverso pudiera producir `O(N^{-3})` sin invariancia por traslación de `U_N` queda abandonada: con el material adjunto produce `N^{-3/2}`, y su mejora exigiría un resultado declarado abierto. [SOURCE]
- La tesis de que `A_{+Q}` carece de subdominancia en todo caso queda abandonada: a `ϑ=0` es `O(ρ_1^N e^{-K_*N})`, sin necesidad de L1. [SOURCE]
- Queda abandonada cualquier identificación de “no transferencia de la vía plana” con “inexistencia de toda deducción”: el informe no cometió ese ascenso y lo desactiva expresamente. [SOURCE]

4. PENDIENTE

- Para cerrar Bob en `O(N^{-3})` con `ϑ≠0` faltaría una cota de capa de `r_c=Bπ_cU_N^NJφ_N` con moneda no invariante por traslación, del tipo `sup_y‖r_c(y)‖=O(N^{-3/2})` o `‖r_c‖_{ℓ²(capa j')}=O(N^{-1}a_{j'})` con sumabilidad inclinada. [SOURCE]
- La vía natural, el Duhamel inverso, exigiría probar conservación uniforme en `k` de la concentración en banda de `U_N^k Jφ_N`; ese enunciado coincide con `H1c_LOCALIZATION (L') = OPEN` y no consta en el material adjunto. [SOURCE]
- Falta una demostración de L1; nadie ha exhibido una vía, y su ausencia es congruente con `H1c_LOCALIZATION` abierto. [SOURCE]
- Para el cierre de `A_{+P}` haría falta L2: probar `o(N^{-13/2}e^{-K_*N})` sobre el resto dependiente de `ϑ`, incluyendo la variación de `δr` y `δx^{stay}`, no sólo `Φ_P−m^N`. [SOURCE]
- Para cerrar `y_N` y los restantes términos Q sin L1 haría falta L3: revisión independiente de las sumas tipo Schur (7)–(8), `f_{Q,N}`, `(𝕄_Nx)_N` y `Σ_k G_Q(N,k+1)C_kx_k`. [SOURCE]
- Quedan por aplicar las tres condiciones concretas del veredicto: `O_{W,Θ}` en tabla y §7, reformulación de L1 para `W,Θ` fijos, y mención explícita de `A_{+Q}` a `ϑ=0` en la tabla y en §7. [SOURCE]
- Queda pendiente una aclaración no bloqueante: consignar que T1 (14) vale para todo `1≤k≤N` con los mismos transportes, no sólo para el índice `N`. [SOURCE]
- El registro del informe sigue pendiente: este sanedrín no sustituye la confirmación de Astra, ausente por `QUOTA`; la versión reparada carece todavía de esa revisión independiente. [SOURCE]

## Ronda Veredicto — ABNER

1. AGREEMENT

- Final verdict of the two residual turns: `PASS_WITH_REPAIRS` on the repaired version of the transfer report. [SOURCE]
- No first failing step in the derivation is identified; the six points of the commission withstand scrutiny, including the negative claim about Bob for `ϑ≠0`. [SOURCE]
- The strong version of the report is the one both members took as their object: exact representation of the four linear terms with `w_c^{fis}=E r_c` and its tilted version, `ENDPOINT_TRANSFER_PARTIAL`; Alice inherits `O(N^{-3})` only as `PRELIMINARY_BOUND`; Bob does not have `O(N^{-3})` for `ϑ≠0`; and `N^{-5}`/`N^{-6}` are upper bounds that prove neither subdominance nor survival of the signal. [SOURCE]
- Point 2 survives for a stronger reason than the mere absence of an alternative bound: the inverse Duhamel attack, constructed by CLAUDE OPUS, exists and is explicit, but yields `N^{-3/2}`, strictly worse than `C_BΘN^{-2}`; its reactivation would require uniform band preservation of `U_N^k Jφ_N`, which corresponds to `H1c_LOCALIZATION (L') = OPEN`. [SOURCE]
- Point 4 holds: the report does not attribute `A_{cQ}=O(N^{-6}e^{-K_*N})` to the Schur PASS; with only the PASS one gets `N^{-5}`, and the improvement to `N^{-6}` depends on class-L3 sums, correctly labeled `PRELIMINARY_BOUND`. [SOURCE]
- The initial discrepancy between `PASS` and `PASS_WITH_REPAIRS` closed when ABNER adopted the record repairs identified by CLAUDE OPUS. [SOURCE]
- The three agreed repairs are: write `O_{W,Θ}(N^{-k})` in the final table and in §7, or record the parametric dependence in all rows; reformulate L1 for fixed `W` and `Θ`, with constants `C(W,Θ)` and uniformity in `j'` and in `N`; and record that `A_{+Q}` at `ϑ=0` is `O(ρ_1^N e^{-K_*N})`, hence subdominant there, or explicitly state that the subdominance column refers to `ϑ≠0` and move the observation about `A_{+P}` outside the table. [SOURCE]
- `ENDPOINT_TRANSFER_PARTIAL` remains unchanged: none of the three repairs turns a preliminary bound into a certified result. [SOURCE]

2. LIVE DISAGREEMENT

- No substantive disagreement remains. [SOURCE]
- The only residual discrepancy with content, that of `PASS` versus `PASS_WITH_REPAIRS`, was resolved by ABNER's adherence to the three record repairs. [SOURCE]
- What remains outstanding is not an object of disagreement among the members, but work prior to a hypothetical closure. [INFERENCE]

3. ABANDONED

- ABNER's initial `PASS` is abandoned: his own residual turn replaces it with `PASS_WITH_REPAIRS` upon recognizing the omission of `O_{W,Θ}` and the ambiguity of L1. [SOURCE]
- The reading of `N^{-5}`, `N^{-6}`, and of the conditional `N^{-7}` as absolute powers or as independent of `W` and `Θ` is abandoned: they are upper bounds `O_{W,Θ}`, with no lower bound or asymptotic for any `A_{cP}`, `A_{cQ}`. [SOURCE]
- The label “exact partition” is abandoned if read as recomposition of norms in §4; the correct use is a triangular majorization of three summands, not a reconstruction of `‖y_N‖` from the three rows. [SOURCE]
- The claim that the inverse Duhamel attack could produce `O(N^{-3})` without translation invariance of `U_N` is abandoned: with the attached material it produces `N^{-3/2}`, and its improvement would require a result declared open. [SOURCE]
- The thesis that `A_{+Q}` lacks subdominance in every case is abandoned: at `ϑ=0` it is `O(ρ_1^N e^{-K_*N})`, without need of L1. [SOURCE]
- Any identification of “non-transfer of the flat path” with “nonexistence of any deduction” is abandoned: the report did not commit that upgrade and expressly disables it. [SOURCE]

4. OUTSTANDING

- To close Bob at `O(N^{-3})` with `ϑ≠0`, a layer bound for `r_c=Bπ_cU_N^NJφ_N` with non-translation-invariant coin would be needed, of the type `sup_y‖r_c(y)‖=O(N^{-3/2})` or `‖r_c‖_{ℓ²(layer j')}=O(N^{-1}a_{j'})` with tilted summability. [SOURCE]
- The natural route, the inverse Duhamel, would require proving uniform preservation in `k` of the band concentration of `U_N^k Jφ_N`; that statement coincides with `H1c_LOCALIZATION (L') = OPEN` and does not appear in the attached material. [SOURCE]
- A proof of L1 is missing; no one has exhibited a route, and its absence is consistent with `H1c_LOCALIZATION` open. [SOURCE]
- For the closure of `A_{+P}`, L2 would be needed: proving `o(N^{-13/2}e^{-K_*N})` over the remainder depending on `ϑ`, including the variation of `δr` and `δx^{stay}`, not only `Φ_P−m^N`. [SOURCE]
- To close `y_N` and the remaining Q terms without L1, L3 would be needed: independent review of the Schur-type sums (7)–(8), `f_{Q,N}`, `(𝕄_Nx)_N`, and `Σ_k G_Q(N,k+1)C_kx_k`. [SOURCE]
- The three concrete conditions of the verdict remain to be applied: `O_{W,Θ}` in the table and in §7, reformulation of L1 for fixed `W,Θ`, and explicit mention of `A_{+Q}` at `ϑ=0` in the table and in §7. [SOURCE]
- A non-blocking clarification remains outstanding: record that T1 (14) holds for every `1≤k≤N` with the same transports, not only for the index `N`. [SOURCE]
- The record of the report remains outstanding: this sanhedrin does not replace Astra's confirmation, absent due to `QUOTA`; the repaired version still lacks that independent review. [SOURCE]

## Resultado operativo

- Estado: `COMPLETED`
- Turnos con fallo, cuota, ausencia o respuesta corta: 0
- Un veredicto emitido en estado degradado es material de análisis, no consenso validado.

---

## Appendix — run log

| Field | Value |
|---|---|
| Started (UTC) | `2026-09-25T12:10:40Z` |
| Finished (UTC) | `2026-09-25T12:26:25Z` |
| Wall clock | 0h 15m 45s |
| Command | `sanedrin -r 1 -m abner,opus --secuencial -i es -p 1800 -t 900 -q 1 -R /home/ignac/sanedrin/reglas/base.md -c reports/2026-09-25--physical-linear-endpoint-transfer-gate.md -c reports/2026-09-25--schur-block-stability-repaired.md -c reports/2026-09-25--flat-endpoint-l2-n3.md -c reports/2026-09-24--two-channel-t1-exact-signed-pq.md -c reports/2026-09-24--two-channel-reconstruction-operator-norms.md -c reports/2026-09-20--h1-inhomogeneous-localization-reconstruction.md -c papers/ir-corona/ir-corona.tex -o debates/2026-09-25--physical-transfer-abner-review.md debates/2026-09-25--physical-transfer-abner-review-request.md` |
| Project | `/home/ignac/qca-causal-cones` |
| Rules | `/home/ignac/sanedrin/reglas/base.md` |
| Host | IGNACIO — Linux 6.6.87.2-microsoft-standard-WSL2 |

### Turns

| Finished (UTC) | Round | Member | Backend | Seconds | Words | Status |
|---|---|---|---|---:|---:|---|
| 2026-09-25T12:15:52Z | 1 | ABNER | api.deepseek.com/deepseek-v4-pro | 311 | 480 | ok |
| 2026-09-25T12:22:36Z | 1 | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 404 | 1280 | ok |
| 2026-09-25T12:23:30Z | Residuo | ABNER | api.deepseek.com/deepseek-v4-pro | 54 | 163 | ok |
| 2026-09-25T12:23:48Z | Residuo | CLAUDE OPUS | claude -p --model claude-opus-5 --effort high (sellado) | 18 | 179 | ok |
| 2026-09-25T12:25:13Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 85 | 795 | ok |
| 2026-09-25T12:26:25Z | Veredicto | ABNER | api.deepseek.com/deepseek-v4-pro | 72 | 785 | ok |

Turns: 6 · failed: 0 · model time: 15m 44s

Full log: `2026-09-25--physical-transfer-abner-review.log`
