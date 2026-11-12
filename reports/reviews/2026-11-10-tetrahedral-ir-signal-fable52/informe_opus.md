<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 97292a9f58c3450128293acacac071d0c1e2391a; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-fable-5-2, esfuerzo: high, vía: claude -p sellado (2.1.322 (Claude Code))
opus.json sha256 34597c91aab3ab72ebe53f1afc65f2da175ab0b585557bfc2e30f39b1c8e6b26
inicio: 2026-11-10T17:13:07Z  fin: 2026-11-10T17:28:50Z
documento: /home/ignac/qca-causal-cones/theory/TETRAHEDRAL_IR_SIGNAL_GATE.md ; último commit observado: 07d7ce6 ; sha256 de la copia enviada eeca234eeaacf893a6a58cfaef50f488beb61ee1f169f3137ea35ce4348f04d5
documento: /home/ignac/qca-causal-cones/theory/POLYHEDRAL_CORONA_TETRA_PREFLIGHT_GATE.md ; último commit observado: 8eed315 ; sha256 de la copia enviada bba1a9010c655be36e193c39e952815e8e23272a7887ba7f9cbca5a4ef09a684
documento: /home/ignac/qca-causal-cones/reports/2026-11-10--tetrahedral-ir-signal.md ; último commit observado: sin versionar ; sha256 de la copia enviada f7a164c12ac5b4883d9ba2269791bbe97ed27e28b21871a8027b5bc123cbc723
documento: /home/ignac/qca-causal-cones/scripts/diagnose_tetrahedral_ir_signal.py ; último commit observado: sin versionar ; sha256 de la copia enviada 11c51b5d95ae1d6e73c06800f8221af8373de36819c367173ad37c0e14079d31
documento: /home/ignac/qca-causal-cones/reports/2026-11-10--tetrahedral-corona-preflight.md ; último commit observado: 07d7ce6 ; sha256 de la copia enviada 5fdd3c845cfb5792fc570c5d43a7d2cd50e0e9e81b8762d1124248b192e9e879
documento: /home/ignac/qca-causal-cones/scripts/verify_s4_cyclic_realization.py ; último commit observado: 170910b ; sha256 de la copia enviada 9a13907240311d26e8db7bc356b9826efd63f0a65190182404a819461ba19224
entrada_opus.txt sha256 0f73adcd47f247bd61cab32a40f8269d99009ec2b210aca1424a56ce2d2b5a94
respuesta sha256 6cd3728400e9434100d42d223d8a405e16c159f30d1e47792f4aa3f0648c47b6
-->

# Obligación tetraédrica IR: prueba candidata de no cancelación

**Veredicto.** Para el protocolo exacto obtengo una prueba candidata de que `L_N > 0` para todo entero `N ≥ N_0`, con `c N^-5 ≤ L_N ≤ C N^-5`. El término cuadrático positivo domina y la interferencia es `o(N^-5)`. La señal la transportan modos de `|k| = O(1)` de la misma `U(k)`, con velocidad de grupo real hasta `(1+√2)/3 ≈ 0,805` a lo largo de `v`, excitados por el borde C^{1,1} del perfil del codificador. No es una señal de origen infrarrojo. `N_0` no es efectivo. Todo está derivado a mano en una sola pasada, sin herramientas ni revisión independiente.

Notación: `ρ0 = 1/32`, `β = b_N/N = 3v/4`, `n = −v = (1,1,1)/√3`, `κ = k/√3`, `dμ = V dk/(2π)^3`, `Γ*` la red recíproca, `f = (V_N − I)φ_N`, `a = U^N f`.

## 1. Convenciones, red y subredes temporales

- **Signo de Fourier.** Con `ψ̂(k) = Σ e^{-ik·x} ψ(x)` y `U(k) = Σ_h A_h e^{-ik·h/√3}` se obtiene `(Uψ)(y) = Σ_h A_h ψ(y − h/√3)`. Los desplazamientos son `+h/√3` con `h1h2h3 = −1`, y `h0/√3 = v`. El informe es correcto.
- **Base de Bell.** Los `G_i` conmutan y `GxGyGz = −I`, así que sus autovectores comunes `|h⟩` cumplen `Π_i(cos κ_i − i sin κ_i G_i)|h⟩ = e^{-iκ·h}|h⟩`. El estado `|h0⟩` es el singlete `S`.
- **Color Z_4.** Para coordenadas crudas `(a,b,c)` defino `col(x) = a+b+c mod 4`. Cada paso suma 1 al color, porque `h1+h2+h3 ∈ {−3, 1}`. Por tanto `K_N(z) = 0` salvo si `col(z) ≡ N (mod 4)`. En momento esto equivale a `U(k+g) = −i U(k)` con `g = (√3 π/2)(1,1,1)`.
- **Ceros pequeños.** Con un solo sitio activo en cada lado, la regla da `−9N/4 ≡ N (mod 4)`, es decir `16 | N`. Reproduce exactamente los ceros de N = 8 y 24.
- **N grande.** `A_N` y `B_N` contienen los cuatro colores. La señal se descompone en cuatro sectores, el término cuadrático es suma de cuatro términos no negativos, y no hay obstrucción de subred.

## 2. Espectro exacto de la misma U(k)

En la base de Bell `U = O·D`, con `D = diag(e^{-iκ·h})`, `O_hh = 1/√2` y `|O_hh'|² = 1/6` para `h ≠ h'`. Los menores principales 2×2 de `O` valen 2/3 y `U ∈ SU(4)`. Con `C = Π cos κ_i`, `S = Π sin κ_i`:

```
tr U = 2√2 (C − iS),   c_2 = (4/3) Σ_i cos 2κ_i
cos 2ω − 2√2 (C cos ω − S sin ω) + (2/3) Σ_i cos 2κ_i = 0      (λ = e^{-iω})
```

Esto reproduce el testigo axial del preflight (`cos ω = ±1/√6` en `x = π/2`).

**Eje k = 3s·n.** Aquí `D = e^{-is}[I + (e^{4is} − 1)|S⟩⟨S|]`, una perturbación de rango uno. Con `tr U = (3e^{-is} + e^{3is})/√2` y `det U = 1`:

```
ω_{1,2} = s ± π/4            (velocidad +1/3 a lo largo de n)
ω_{3,4} = −s ± α(s),   cos α = cos 2s/√2,   α'(s) = 2 sin 2s / √(1 + sin² 2s) ∈ [−√2, √2]
velocidad a lo largo de v:   (1 ∓ α'(s))/3 ∈ [(1−√2)/3, (1+√2)/3]
```

- **Simplicidad.** Las bandas 3 y 4 solo degeneran con 1 y 2 si `sin 2s = 0`, y nunca entre sí.
- **Dirección del gradiente.** Por la simetría ternaria `S`, en puntos simples del eje `∇ω` es paralelo a `n`.
- **Punto estacionario real.** `∇ω_3 = (3/4)v` ocurre en `sin 2s = −5/√39`, con `α'' = 39√14/128 ≠ 0`. El centro de la bola de velocidades relativas es una velocidad de grupo real.
- **Cobertura parcial.** El máximo axial `0,8047` es menor que `13/16`, así que el eje no cubre toda la bola. No hace falta.
- **Autovectores.** Los de las bandas 3 y 4 son `ψ ∝ Σ_± e^{∓iπ/4}(e^{2is}ν − e^{∓iπ/4})^{-1} S_±`, con `S_± = (1 ± N)S/2`. Como `Mχ = i|↓⟩⊗η_+` y `|⟨S, Mχ⟩|² = (1 + 1/√3)/4 ≠ 0`, se tiene `P_3(k)Mχ ≠ 0` en todo punto simple del eje.
- **Paridades.** La conjugación `C` da `ω_j(−k) = −ω_j'(k)` y el desplazamiento `g` suma `π/2` a las fases. Los puntos estacionarios vienen en órbitas. Esto puede cancelar coeficientes de la interferencia, pero nunca el término cuadrático.

## 3. Por qué no hay cancelación (conteo de potencias)

- **Perfil del codificador.** `sin(πF/2) ≈ 2π(ρ0 − |w|)²/ρ0²` cerca del borde: salto en la segunda derivada radial. La parte `cos − 1` es C³ y subdominante.
- **Cola UV.** En consecuencia `f̂(k) ~ N^-5/2` para `|k| = O(1)`. Lo mismo vale para `(E_N r_N)^` por el borde de `h_N`.
- **Término cuadrático.** Es la probabilidad UV de `f` (orden `N^-5`) por la fracción `O(1)` que llega balísticamente a `B_N`.
- **Interferencia.** Es `∫ ⟨(Er)^, U^N f̂⟩ dμ`, de tamaño `N^-5` por una integral oscilante. Con fase estacionaria no degenerada daría `N^-13/2`; ese exponente es heurístico y propio de este protocolo, no importado. Solo pruebo `o(N^-5)`.

## 4. Lemas

Fijo `χ ∈ C_c^∞(|k| < 2κ)` con `χ = 1` en `|k| ≤ κ`, y escribo `a = a^< + a^>` con `a^< = U^N χ(D) f`.

**Lema A (IR).** `sup { |K^χ_N(z)| : v·z ≥ 11N/16 } ≤ C_m N^-m` para todo `m`, con `K^χ_N(z) = ∫ e^{ik·z} U(k)^N χ dμ`.

1. Para `|k| ≤ 2κ`, `|η| ≤ τ`, los proyectores de Riesz `P_±(k+iη)` son analíticos y acotados.
2. `U^N P_+ = e^{-iNπ/4} exp(−iN H_+) P_+`, con `H_+` analítico y hermítico en `k` real. Además `η·∇H_+(0) = P(η·G)P/√3 = (η·R)P/3`, de norma `|η|/3` (identidad "compression" del verificador). Análogo para `Q`.
3. Por la cota de norma logarítmica, `‖exp(−iN H_+(k+iη))‖ ≤ exp(N|η|(1/3 + C|k| + C|η|))`.
4. Con una extensión casi analítica `χ̃` y Stokes:
   `∫Φ(k)dk = ∫Φ(k+iτv)dk + 2i ∫_0^τ dt ∫ v·∂̄Φ(k+itv) dk`, `Φ = e^{ik·z} U^N χ̃`.
   Como `|e^{i(k+itv)·z}| ≤ e^{-11Nt/16}`, el primer término es `O(e^{-cN})` y el segundo `≤ C_m ∫ t^m e^{-cNt} dt`. ∎

Consecuencia: `‖E^{1/2} a^<‖` y `⟨Er, a^<⟩` son `O(N^-∞)`, luego

```
L_N = Q_N + 2 Re J_N + O(N^-∞),   Q_N = ⟨a^>, E a^>⟩ ≥ 0,   J_N = ∫ (1−χ) ⟨(Er)^, U^N f̂⟩ dμ
```

**Lema B (UV).** Sea `g = 1_{|w| ≤ ρ0} g_in`, con `g_in` suave que se anula a orden 2 en la esfera, y `c(θ) = ∂_r² g_in(ρ0 θ)`. Entonces

```
g̃(ξ) = 2πρ0 |ξ|^-4 [c(ξ̂) e^{-iρ0|ξ|} + c(−ξ̂) e^{+iρ0|ξ|}] + O(|ξ|^-5)
```

- **Prueba.** `g̃(ξ) = ∫ e^{-i|ξ|t} m(t) dt` con `m(t) = π ∫_0^{ρ0² − t²} ḡ(t,u) du`, que es C^∞ en `[−ρ0, ρ0]`. Además `m = (πcρ0/3)(ρ0 ∓ t)³ + …` en los extremos. Cinco integraciones por partes dan el resultado. ∎
- **Comprobación.** Para `(1 − |w|²)²` da `32π cos|ξ|/|ξ|^4`, igual que la asintótica de `8(2π)^{3/2} J_{7/2}(t)/t^{7/2}`.

Con Poisson, `Σ_{x∈L} e^{-ik·x} g((x−b)/N) = (N³/V) Σ_G e^{-i(k+G)·b} g̃(N(k+G))`. Uniformemente en `dist(k, Γ*) ≥ κ`:

```
f̂(k)   = i C_f N^-5/2 Σ_G Σ_± e^{∓iρ0N|k+G|} |k+G|^-4 Mχ + O(N^-7/2),   C_f = 256π² Φ_0(ρ0)/√V
(Er)^(k) = C_h N^-5/2 Σ_G e^{-i(k+G)·b_N} Σ_± e^{∓iρ0N|k+G|} |k+G|^-4 Ψ_N(β ± ρ0(k+G)^) + O(N^-7/2)
```

Aquí `C_h = 512π/√V`, `Φ_0(ρ0) > 0`, y `r_N(y) = √V N^-3/2 Ψ_N(y/N)` con `Ψ_N` entera y derivadas acotadas uniformemente en `N`. El signo `±` corresponde al punto fuente `x = ±ρ0 N (k+G)^` del borde. En particular `‖a^>‖² = O(N^-5)`.

**Lema C (interferencia).** `J_N = o(N^-5)`.

1. Sustituyendo el Lema B, el error es `O(N^-6)`.
2. El término principal es `N^-5 Σ_{j,G,G',±,±'} ∫ e^{iNΦ} A_N dμ`, con `Φ = β·k ±' ρ0|k+G'| ∓ ρ0|k+G| − ω_j(k) + cte`. Las amplitudes son precompactas en L¹ y las sumas en `G, G'` convergen absolutamente.
3. Basta ver que `∇Φ ≠ 0` casi en todas partes. Si `∇Φ ≡ 0` en un abierto, la continuación analítica en el polinomio característico haría de `e^{-iΩ(k)}` un autovalor para todo `k`, con `Ω = cte + β·k ± ρ0|k+G| ∓' ρ0|k+G'|`.
4. En el eje, `dΩ/ds ∈ [−9/4 − 3/16, −9/4 + 3/16]`, que excluye la pendiente `+1` de las bandas 1 y 2. Para las bandas 3 y 4 haría falta que `α'(s)` fuera algebraica en un intervalo, lo que es imposible porque `cos 4s` es trascendente sobre `C(s)`.
5. Riemann–Lebesgue y convergencia dominada concluyen. ∎

**Lema D (cota inferior).** `liminf N^5 Q_N ≥ c_* > 0`.

1. Tomo `γ ∈ C_c^∞` con `0 ≤ γ ≤ h_0` y `γ > 0` en `|w| < ρ0/2`, así que `E_N ≥ γ_N`.
2. Tomo `Θ = θ(D) P_j(D)` con `θ = sin²ϑ` suave, soportada donde la banda `j` es simple. Los conmutadores `[Θ, γ_N]` y `[√(Θ(1−Θ)), γ_N]` son `O(1/N)` por Schur, luego `⟨a^>, γ_N a^>⟩ ≥ ⟨Θa^>, γ_N Θa^>⟩ − O(N^-6)`.
3. `(Θa^>)^ = e^{-iNω_j} θ P_j f̂`. Con `k' = k − p/N` y `γ̂_N(p/N) = (N³/V) e^{-ip·β} γ̃(p) + O(N^-∞)`, los términos diagonales dan transporte clásico. Los no diagonales tienen fase `N ρ0(±|k+G| ∓' |k+G'|)`, de gradiente no nulo casi en todas partes, y tienden a 0.
4. Resulta

```
c_* = C_f² Σ_G Σ_± ∫ θ² ‖P_j Mχ‖² |k+G|^-8 γ(∇ω_j(k) ± ρ0(k+G)^ − β) dμ
```

5. **Positividad.** Tomo `j = 3` y `k_1 = 3 s_1 n` con `α'(s_1) = −43/32`, es decir `sin² 2s_1 ≈ 0,823`. Entonces `∇ω_3(k_1) = (3/4 + ρ0)v`. Con `G = 0` y el signo `± = sgn(s_1)`, el argumento de `γ` es 0: el punto del borde de Alicia opuesto a Bob emite hacia el centro de `B_N`. La banda es simple y `P_3 Mχ ≠ 0`. Por continuidad, `c_* > 0` con `θ` concentrada en `k_1`. ∎

## 5. Teorema y alcance

```
c_* N^-5 (1 − o(1))  ≤  L_N  ≤  ‖(1−χ)f‖² + o(N^-5) = O(N^-5),      δ_N = L_N > 0 para N ≥ N_0
```

- **Todo N, sin subsecuencias.** Las cotas son uniformes en el desfase de `b_N` respecto de la red, porque Poisson lo absorbe en fases. La estructura Z_4 solo reorganiza `Q_N` en sumandos no negativos.
- **Resto.** `O(N^-6)` explícito más términos `o(1)` no cuantitativos de Riemann–Lebesgue. Basta para el signo, no da tasa.
- **Datos pequeños.** No uso ni extrapolo los valores flotantes. N = 8…32 quedan fuera de este régimen, que exige `R_N ≫ 1`.

## 6. Admisibilidad: no la uso, y no basta para interpretar

- **Álgebra del informe.** He comprobado y es correcta: el Gram con autovalores 1/3, 4/3, 4/3, la cota `4|k|²/(3π²)`, Leibniz desplazado, `Z_N`, `Φ_0 > 0`, `‖(V−I)φ‖² = Σ 2[1 − cos(πF/2)]|φ|²` y `‖Δ‖_1 = 2√(1 − a²)`.
- **Definición 3.1.** El manuscrito no está adjunto, así que no puedo certificar que esas tres razones sean exactamente las de la definición.
- **Insuficiencia.** `L_N = ⟨a^>, E a^>⟩ + o(N^-5)`: toda la señal vive en la componente `|k| ≥ κ` del estado codificado. Esa componente tiene norma `N^-5/2`, muy por debajo de la tolerancia `O(N^-1/2)`. La admisibilidad relativa se cumple en el límite, pero no controla ni etiqueta como IR una señal de orden `N^-5`.

## 7. Clasificación

**PROVED_IN_THIS_DERIVATION** (álgebra exacta, comprobable a mano)
- Signos de Fourier, base de Bell, regla de color Z_4 y su equivalencia con `16 | N`.
- Polinomio característico general y espectro exacto en el eje.
- Velocidad de grupo real `(3/4)v` y `(25/32)v`, simplicidad de la banda y `P_3 Mχ ≠ 0`.

**PROVED_IN_THIS_DERIVATION como prueba candidata** (lemas A–D con demostración escrita y comprimida)
- `L_N > 0` para `N ≥ N_0` y `L_N ≍ N^-5`.
- Herramientas externas usadas, pendientes de comprobar en fuente primaria:
  - perturbación analítica de proyectores de Riesz (espectro separado en dos cúmulos);
  - cota `‖e^A‖ ≤ exp λ_max((A + A*)/2)`;
  - extensión casi analítica con `∂̄χ̃ = O(|Im k|^m)`;
  - Poisson para función continua de soporte compacto con `Σ|F̃(G)| < ∞`;
  - Riemann–Lebesgue con fase analítica real de gradiente no nulo casi en todas partes;
  - medida nula de ceros de funciones analíticas reales no idénticamente nulas;
  - test de Schur para conmutadores.
- Puntos que un revisor debería atacar primero: el paso 3 del Lema A, la dominación uniforme de las sumas en `G`, y el paso 2 del Lema D.

**CONDITIONAL**
- Límite exacto `N^5 L_N → c_Q`, que requiere aproximar `h_0` por arriba y por abajo y una partición fuera del conjunto de degeneración:
  `c_Q = 8192π Φ_0(1/32)² Σ_j Σ_± ∫_{R³} ‖P_j(ξ)Mχ‖² |ξ|^-8 h_0(∇ω_j(ξ) ± ξ̂/32 − 3v/4) dξ`.
- Admisibilidad en el sentido de la Definición 3.1, por no estar adjunta.

**OPEN**
- Orden real de la interferencia (`N^-13/2` es heurístico) y coeficiente con signo.
- `N_0` efectivo y régimen intermedio.
- Conjunto completo de puntos estacionarios fuera del eje y cáusticas.

**Sobre la etiqueta de la gate.** El resultado apoya una señal no nula en el protocolo declarado, fuera del cono local. No apoya llamarla infrarroja, porque es fuga UV del borde del codificador propagada por la rama rápida ya detectada en el preflight. No promueve nada en el repositorio.
