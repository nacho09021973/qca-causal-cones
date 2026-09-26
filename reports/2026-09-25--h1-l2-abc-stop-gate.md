# H1 / L2: gate A/B/C de parada sobre la subcontribución stay del término terminal-P físico

Fecha: 2026-09-25.

Estado:
```
L2_GATE = B / OPEN_BLOCKED_METHOD
EVIDENCE = PRELIMINARY_DECISION_AUDIT / PARTIAL_EXTERNAL_REVIEW + SOURCE_BOUNDS_REPRODUCED (§8)
H1 = OPEN
```

Este gate no demuestra que H1 sea falsa. Registra únicamente que, con las
hipótesis congeladas y el aparato ya disponible, no se alcanza la escala
necesaria para probar la estabilidad fuerte de la subcontribución `stay` del término terminal-P físico.
No se abre un nuevo lema de localización, no se ejecuta código numérico y no
se añaden hipótesis sobre `vartheta`.

## 1. Objeto y regla preescrita

El objeto es el resto dependiente de `vartheta` de la **subcontribución `stay`**
dentro del término terminal-P de `A_{+P}`, no el término terminal-P completo y
no `A_{+P}` completo. T1 (14) da la identidad exacta

\[
x_N=x^{stay}+f_{Q,N}+(\mathbb M_Nx)_N.
\]

Por tanto, “terminar en P” incluye también entradas desde Q y excursiones
`P→Q→P`; `stay` es únicamente `x^{stay}=\Phi_P(N,0)Ps`, la trayectoria que
permaneció siempre en P. La abreviatura `PP[vartheta]-PP[0]` usada en esta
discusión se refiere sólo al resto `stay`; no es el observable `Lpp` de la
Sec. 10.
La escala plana relevante es

\[
L_{\rm lead}(N)\asymp N^{-13/2}e^{-K_*N}.
\]

Salidas:
- **A — PROVED:** resto `o(N^-13/2 e^-K*N)` con las hipótesis congeladas.
- **B — OPEN/BLOCKED:** las cotas disponibles no llegan a esa escala o hacerlo
  exige nueva maquinaria/hipótesis. B es obstrucción del método, no refutación.
- **C — REFUTED:** aparece un perfil admisible con cota inferior,
  contraejemplo o equivalente que impide la subdominancia.

## 2. Cotas físicas disponibles

**Identidad exacta de alcance.** La salida terminal-P completa es
`x_N=x^{stay}+f_{Q,N}+(𝕄_Nx)_N`. Las dos cotas de este §2 controlan sólo la
subcontribución `stay`. Los términos `f_{Q,N}` y `(𝕄_Nx)_N` no se absorben
aquí; su revisión corresponde al hueco L3.

El informe de transferencia de extremos registra la resta exacta de la pieza
stay:

\[
\langle r_\vartheta,E V x_\vartheta^{\rm stay}\rangle
-\langle r_0,E V x_0^{\rm stay}\rangle
=
\langle r_\vartheta-r_0,E V x_\vartheta^{\rm stay}\rangle
+
\langle r_0,E V(x_\vartheta^{\rm stay}-x_0^{\rm stay})\rangle.
\]

Con el expediente actual:
- el primer sumando queda sólo en
  \(O_{W,\Theta}(N^{-5}e^{-K_*N})\), usando el control geométrico
  \(\|E\delta r\|\lesssim C_B\Theta N^{-2}\) y
  \(\|x_\vartheta^{\rm stay}\|=O_{W,\Theta}(N^{-3})\);
- el segundo queda sólo en
  \(O_{W,\Theta}(N^{-6}e^{-K_*N})\), aun usando el extremo plano de Bob.

Ambas potencias son mayores que \(N^{-13/2}=N^{-6.5}\). No prueban
subdominancia y tampoco prueban que ésta sea falsa. Incluso concediendo L1,
el producto normativo \(N^{-3}N^{-3}\) sólo da \(N^{-6}\), así que L1 no
resuelve L2.

## 3. Resultados finos existentes que no transfieren

`2026-09-20--h1-inhomogeneous-localization-reconstruction.md` obtiene
\(N^{-15/2}\) para una inserción G dentro de una ventana de saddle fija, pero
declara expresamente que no se sigue localización global y deja
`H1c_LOCALIZATION (L') = OPEN`: faltan cadenas a momento variable, visitas
a Q, transiciones entre las ocho ventanas y el exterior.

`2026-09-24--h1c-dyson-target-check.md` y la descomposición Dyson exacta
controlan un test de moneda constante sobre los caminos y extremos planos
fijados. El símbolo completo da allí una corrección relativa \(O(N^{-1})\).
Ese test conserva homogeneidad en la zona relevante y no controla el
`A_{+P}` físico con perfil espacial variable y ambos extremos dependientes
del propagador. No decide A ni C para L2 físico.

## 4. Aplicación de la regla de parada

El veredicto B se apoya únicamente en la comparación de escalas de §2. Las
cotas disponibles para los dos sumandos del resto físico son
\(O_{W,\Theta}(N^{-5}e^{-K_*N})\) y
\(O_{W,\Theta}(N^{-6}e^{-K_*N})\), mientras que A exige
\(o(N^{-13/2}e^{-K_*N})\). Por tanto, con el aparato actualmente
establecido, A no está demostrada.

La regla preescrita de §1 clasifica este caso como B cuando las cotas
disponibles no alcanzan la escala requerida. §3 registra resultados más finos
existentes que no transfieren al objeto físico aquí considerado, pero este
informe **no afirma que `H1c_LOCALIZATION` sea la única vía posible** para
cerrar A. Una prueba futura podría usar otra estructura, cancelación o
representación que no esté en el expediente actual.

No se abre en este gate ninguna de esas vías adicionales.

**Carácter estructural de B.** B es estructural para el método actual,
basado en normas: las mismas estimaciones por normas (Cauchy–Schwarz con
\(\|E\mathcal V\|\) y \(\|x^{\rm stay}\|\)) sólo acotan el **líder
plano** \(\langle r_0,E\mathcal V x_0^{\rm stay}\rangle\) por
\(O(N^{-3}\cdot N^{-3})=O(N^{-6}e^{-K_*N})\), por encima de su escala real
\(N^{-13/2}e^{-K_*N}\). Ese medio orden procede de la localización gaussiana
y de fase en momento, que ninguna cota de norma retiene. Por tanto B
diagnostica una limitación del método, no evidencia contra H1.

Por la regla preescrita:

\[
\boxed{\texttt{L2\_GATE = B / OPEN\_BLOCKED\_METHOD}}.
\]

## 5. Alcance

B significa que el objetivo fuerte de supervivencia queda bloqueado por el
método actual. No significa `H1=false`, no aporta contraejemplo ni cota
inferior, no decide dominancia y no afecta al resultado plano cerrado.

No hay salida C. No se ejecutó ningún barrido de

\[
PP[\vartheta]/PP[0].
\]

## 6. Decisión de programa

Se detiene aquí el intento fuerte de L2. H1 permanece **OPEN** y el objetivo
fuerte queda **OPEN/BLOCKED por el método actual**. Los huecos L1 y L3 no se
abren como rutas de rescate. Cualquier reapertura de la supervivencia fuerte
requiere una decisión explícita que acepte nueva maquinaria o hipótesis.

## 7. Revisión externa parcial

**Estado:** `PARTIAL_EXTERNAL_REVIEW`.

**Comprobado por la revisión:**
- la salida B puede justificarse sólo con §2 y la regla A/B/C de §1;
- \(N^{-5}\) y \(N^{-6}\) no alcanzan la escala \(o(N^{-13/2})\);
- B es una obstrucción del método disponible, no una refutación de H1 ni una salida C;
- el informe no necesita afirmar que `H1c_LOCALIZATION` sea la única vía posible;
- T1 (14) resuelve que “terminal-P” y `stay` **no coinciden**: `stay` es sólo el primer sumando de la salida terminal-P `x_N`.

**No comprobado por esta revisión:**
- las derivaciones fuente de las dos cotas de §2 no se han reconstruido desde sus artefactos anteriores;
- no se ha demostrado que no exista otra cancelación, identidad o representación capaz de cerrar A;
- esta revisión no reconstruye las cotas separadas de `f_{Q,N}` ni `(𝕄_Nx)_N`, que pertenecen al hueco L3.

**Pendiente:**
- si se desea promoción por encima de `PARTIAL_EXTERNAL_REVIEW`, realizar una revisión independiente que remonte las dos cotas de §2 a sus fuentes.
  Realizado en §8 para las dos cotas de §2.

## 8. Revisión externa de las cotas de §2 (Claude, 2026-09-26)

Revisor: Claude (Anthropic). El informe no declara su autor; por el nombre de
la rama (`chatgpt/…`), se toma como de otra familia.
Revisión en frío contra las fuentes; no modifica ninguna matemática.

**Alcance:** reproduce las dos cotas de §2 desde sus fuentes y valida la
salida B. **No** revisa ni cierra H1, no examina L1/L3 ni
`f_{Q,N}`/`(𝕄_Nx)_N`, y no demuestra la ausencia de otra vía hacia A.

- **Primer sumando.** Por Parseval,
  \(|\langle r_\vartheta-r_0,E\mathcal V x_\vartheta^{\rm stay}\rangle|
  \le\sup_y h_N(y)e^{-\xi_*\cdot(y-y_*)}\,\|\delta r\|\,\|x_\vartheta^{\rm stay}\|\).
  Con \(\sqrt{h_N}\le2s/R\) se obtiene
  \(\sup_y h_Ne^{-\xi_*\cdot(y-y_*)}\le C_BN^{-2}\) y
  \(C_B=256/(3e^2t_*^2)\). Por Duhamel,
  \(\|\delta r\|\le\Theta\) (N pasos con \(\|C_N-I\|\le\Theta/N\)).
  Además, \(\|x^{\rm stay}\|\le e^{C_P\Theta}C_P\|s\|=O(N^{-3})\), por el
  bloque \(A_j\) reparado y \(\|s\|=O(N^{-3})\). Resultado:
  \(O(N^{-5})\). **Se reproduce.**
- **Segundo sumando.** El extremo plano de Bob es \(O(N^{-3})\) (nota
  `2026-09-25--flat-endpoint-l2-n3.md`). Por telescopado,
  \(\|x_\vartheta^{\rm stay}-x_0^{\rm stay}\|=O(\Theta N^{-3})\), con N
  pasos y \(\|A^\vartheta-A^0\|\le C_P\Theta/N\); no hay ganancia en N.
  Resultado: \(O(N^{-6})\). **Se reproduce.**
- **Salida B:** correcta por la regla de §1. No procede C: no hay cota
  inferior ni contraejemplo.
- **Observación:** el primer sumando está limitado por \(\|\delta r\|\le\Theta\),
  que no reconoce ninguna pequeñez de \(r_\vartheta-r_0\) en la zona de Bob.
  Queda como observación; no es una cota nueva.

`H1 = OPEN` sin cambio. Por decisión del usuario, H1 queda en pausa; no se
abre `H1c_LOCALIZATION` ni otra vía.

