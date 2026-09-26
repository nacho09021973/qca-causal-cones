# Transferencia de los extremos planos a las piezas lineales físicas A_{cP}, A_{cQ}

Fecha: 2026-09-25. Estado final:

```text
ENDPOINT_TRANSFER_PARTIAL — PRELIMINARY
INDEPENDENT_REVIEW: PASS_WITH_REPAIRS; repaired version not re-reviewed
```

Alice transfiere (relación exacta con el extremo plano más una corrección
explícita de orden inferior). El extremo dual de Bob y la referencia `r_c`
no transfieren la ganancia `N^{-3}`. Aun con esa ganancia, el término
terminal P no queda subdominante por Cauchy–Schwarz (§7).

Además, **el objetivo tal como está escrito no es alcanzable para `A_{+P}`**
(§0). Esto se dice aquí y no se reformula en silencio.

Revisiones:

1. Acta `debates/2026-09-25--physical-transfer-astra-review.md`: Astra (GPT)
   `REPAIR_REQUIRED` en la ronda 1, Ciro (Grok) `PASS_WITH_REPAIRS`; el turno de
   residuo y veredicto de Astra falló por cuota (`QUOTA`), así que Astra **no**
   confirmó la versión reparada. Sus reparaciones están aplicadas (marcadas
   `[rev. 2026-09-25]`).
2. Acta `debates/2026-09-25--physical-transfer-abner-review.md`: ABNER
   (DeepSeek) y Opus, sobre la versión reparada, `PASS_WITH_REPAIRS`. Sus tres
   reparaciones de registro (`O_{W,Θ}` en tabla y §7, L1 para `W`,`Θ` fijos,
   casos `ϑ=0`) y la aclaración sobre T1 (14) están aplicadas y no han vuelto
   a revisarse. Opus no cuenta como independiente.

Estado del informe: preliminar, sin registrar.

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

**Duhamel inverso (observación de la revisión de ABNER/Opus, no rescata `N^{-3}`).**
Con `U_N^N−D^N=Σ_kD^{N−1−k}(C_N−I)U_N^k` el propagador invariante queda a la
izquierda y vale `sup_y‖(D^mv)(y)‖≤‖v‖_2` (unitariedad de `S(p)`, `μ(T³)=1`). Cada
término da `sup_y‖·‖≤Θ/N`, `N` términos: `sup_y‖δr_+(y)‖=O(1)`. Metido en la
geometría de capas, `‖Eδr_+‖_{ℓ²_tilt}≲N^{-2}·N^{1/2}=N^{-3/2}`, **peor** que
`C_BΘN^{-2}`. Para que compita haría falta `sup_y‖U_N^kJφ_N(y)‖=O(N^{-3/2})`
uniformemente en `k≤N` (conservación de banda `|p|≲N^{-1}` bajo la moneda), es
decir `H1c_LOCALIZATION (L') = OPEN`. Esta vía se registra como no útil con lo
disponible.

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

**[rev. 2026-09-25]** Mayoración triangular de tres sumandos (más el Q inicial) por sustitución de `x_k = x_k^{stay}+f_{Q,k}+(𝕄x)_k` en T1 (14), que vale para todo `1≤k≤N` con los mismos transportes de (13); las cotas de `(𝕄x)_k` usan la cota a priori `‖x_k‖_2≤ν_k` del PASS, y las filas no recomponen `‖y_N‖` con igualdad
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

| TERM | EXACT_PHYSICAL_ENDPOINTS | ALICE_NORM | BOB_DUAL_NORM | INTERNAL_BOUND | EXPONENTIAL_SCALE | POWER_OF_N | SUBDOMINANT_TO_N^-13/2? (`ϑ≠0`) | TRANSFER_STATUS | MISSING_LEMMA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `A_{+P}` | `s=FH_ξJ(U_M−I)φ_N`; `w_+^{fis}=E B π_+U_N^NJφ_N` (`=w_N` si `ϑ=0`); `w~_+`= su versión inclinada; `x_N=Pt_N` | `‖s‖=‖f^{T1}‖_{tilt}`: EXACT igualdad; `O(N^{-3})` PRELIMINARY_BOUND | `‖E V_c‖≤C_BN^{-2}` PRELIMINARY_BOUND; `‖w~_+‖=O(N^{-3})`: NO_CURRENT_BOUND | `‖x_N‖≲‖s‖`: ESTABLISHED_BOUND (Schur); partes stay/`f_Q`/`𝕄_N`: PRELIMINARY_BOUND | `e^{-K_*N}` EXACT | `O_{W,Θ}(N^{-5})` PRELIMINARY_BOUND | **NO PROBADO** | ENDPOINT_TRANSFER_PARTIAL | L1 (capa de Bob de `r_c`); L2 (líder gaussiano con `Φ_P≠m^N`); L3 (revisar 𝕄_N) |
| `A_{+Q}` | igual con `y_N=Qt_N` | igual | igual | `‖y_N‖_2≲(N^{-1}+ρ_2^N)‖s‖`: PRELIMINARY_BOUND | `e^{-K_*N}` EXACT | `O_{W,Θ}(N^{-6})` PRELIMINARY_BOUND; `O_{W,Θ}(N^{-7})` si L1 | **NO PROBADO**; `o(N^{-13/2})` (`O_{W,Θ}(N^{-7})`) sólo si L1 | ENDPOINT_TRANSFER_PARTIAL | L1 |
| `A_{-P}` | `w_-^{fis}=Eδr_-` (`=0` si `ϑ=0`); `π_-x_N` | igual que `+` | `‖E δr_-‖_{tilt}≤C_BΘN^{-2}`: PRELIMINARY_BOUND; `N^{-3}`: NO_CURRENT_BOUND | igual que `+P` | `e^{-K_*N}` EXACT | `O_{W,Θ}(N^{-5})` PRELIMINARY_BOUND | **NO PROBADO** | ENDPOINT_TRANSFER_PARTIAL | L1; L2; L3 |
| `A_{-Q}` | `w_-`; `π_-y_N` | igual | igual | igual que `+Q` | `e^{-K_*N}` EXACT | `O_{W,Θ}(N^{-6})`; `O_{W,Θ}(N^{-7})` si L1 | **NO PROBADO**; condicional a L1 | ENDPOINT_TRANSFER_PARTIAL | L1 |

Nota sobre `ϑ=0` (fuera de la columna de subdominancia, que se refiere a `ϑ≠0`):
`A_{+P}` contiene el líder plano (§0), luego no puede ser subdominante;
`A_{+Q}=O(ρ_1^N e^{-K_*N})`, subdominante allí sin L1; `A_{-P}=A_{-Q}=0`.
Todas las potencias de la tabla son cotas superiores `O_{W,Θ}` (constantes
que dependen de `W`, `Θ`, `C_P`, `C_Q`, `C_0`, `ρ_1`, `N_0`), sin cota inferior
ni asintótica; la comparación con `N^{-13/2}` vale para cada `W`, `Θ` fijos.

Lemas que faltan:

- **L1** `[rev.]`. `‖r_c‖_{ℓ²(capa j')} ≤ N^{-1}a_{j'}` con
  `Σ_j(1+j)^4e^{-2t_*j}a_j²<∞`,   para cada `W` admisible y `Θ` fijos, con constantes `C(W,Θ)` y uniformidad
  en `j'` y en `N`, para `r_c=Bπ_cU_N^NJφ_N` con moneda no invariante por traslación;
  un `O(N^{-1})` con constante no controlada en `j` no basta. La alternativa
  puntual `sup_y‖r_c(y)‖=O(N^{-3/2})` sí lo da. Análogo de la unitariedad de
  `S(p)` en el toro, que aquí no aplica.
- **L2** `[rev.]`. Sobre el **resto `ϑ`-dependiente de la subcontribución `stay`**
  dentro de `A_{+P}` (no sobre la salida terminal-P completa ni sobre `A_{+P}`
  completo): probar `o(N^{-13/2}e^{-K_*N})` incluyendo la variación de ambos
  extremos (`δr` y `δx^{stay}`, no sólo `Φ_P−m^N`). T1 (14) deja explícito que
  `x_N=x^{stay}+f_{Q,N}+(𝕄_Nx)_N`; por tanto `stay` no es sinónimo de terminal-P.
- **L3** `[rev.]`. Revisión independiente de las otras piezas terminal-P y de las
  sumas tipo Schur (7)–(8): `f_{Q,N}`, `(𝕄_Nx)_N` y también
  `Σ_kG_Q(N,k+1)C_kx_k` (la cota `‖y_N‖=O(N^{-4})`).

## 7. Conclusión

- **Alice: transferencia establecida** (igualdad exacta con el plano más un resto
  `N^{-5}`), potencia `N^{-3}` heredada como `PRELIMINARY_BOUND`.
- **Bob/referencia: transferencia parcial.** Sólo `‖E V_c‖=O(N^{-2})` (geométrico) y
  la representación exacta con `w_c^{fis}=E r_c` (y `w~_c` su versión inclinada). Para `ϑ≠0`
  no hay `O(N^{-3})` demostrado (`NO_CURRENT_BOUND`); la cota disponible es `C_BΘN^{-2}`,
  `C_B=256/(3e²t_*²)`.
- **Los cuatro términos lineales** quedan acotados por `O_{W,Θ}(N^{-5})` (P) y `O_{W,Θ}(N^{-6})` (Q)
  (`O_{W,Θ}(N^{-5})` para Q con sólo el PASS de Schur). Estas cotas **no demuestran**
  subdominancia frente a `N^{-13/2}`; tampoco la excluyen, salvo para `A_{+P}` a
  `ϑ=0`, que contiene el líder; a `ϑ=0` también `A_{+Q}=O(ρ_1^Ne^{-K_*N})`
  (subdominante allí sin L1) y `A_{-P}=A_{-Q}=0`.
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
