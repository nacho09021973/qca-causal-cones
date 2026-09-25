# H1 / L2: gate A/B/C de parada sobre el resto terminal-P físico

Fecha: 2026-09-25.

Estado:
\`\`\`
L2_GATE = B / OPEN_BLOCKED_METHOD
EVIDENCE = PRELIMINARY_DECISION_AUDIT / PARTIAL_EXTERNAL_REVIEW
H1 = OPEN
\`\`\`

Este gate no demuestra que H1 sea falsa. Registra únicamente que, con las
hipótesis congeladas y el aparato ya disponible, no se alcanza la escala
necesaria para probar la estabilidad fuerte del término terminal-P físico.
No se abre un nuevo lema de localización, no se ejecuta código numérico y no
se añaden hipótesis sobre \`vartheta\`.

## 1. Objeto y regla preescrita

El objeto es el resto dependiente de \`vartheta\` de la contribución
terminal-P de \`A_{+P}\`, no \`A_{+P}\` completo. La abreviatura
\`PP[vartheta]-PP[0]\` usada en la discusión significa aquí esta pieza física
terminal-P/stay y no el observable \`Lpp\` de la Sec. 10.

La escala plana relevante es

\[
L_{\rm lead}(N)\asymp N^{-13/2}e^{-K_*N}.
\]

Salidas:
- **A — PROVED:** resto \`o(N^-13/2 e^-K*N)\` con las hipótesis congeladas.
- **B — OPEN/BLOCKED:** las cotas disponibles no llegan a esa escala o hacerlo
  exige nueva maquinaria/hipótesis. B es obstrucción del método, no refutación.
- **C — REFUTED:** aparece un perfil admisible con cota inferior,
  contraejemplo o equivalente que impide la subdominancia.

## 2. Cotas físicas disponibles

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

\`2026-09-20--h1-inhomogeneous-localization-reconstruction.md\` obtiene
\(N^{-15/2}\) para una inserción G dentro de una ventana de saddle fija, pero
declara expresamente que no se sigue localización global y deja
\`H1c_LOCALIZATION (L') = OPEN\`: faltan cadenas a momento variable, visitas
a Q, transiciones entre las ocho ventanas y el exterior.

\`2026-09-24--h1c-dyson-target-check.md\` y la descomposición Dyson exacta
controlan un test de moneda constante sobre los caminos y extremos planos
fijados. El símbolo completo da allí una corrección relativa \(O(N^{-1})\).
Ese test conserva homogeneidad en la zona relevante y no controla el
\`A_{+P}\` físico con perfil espacial variable y ambos extremos dependientes
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

Por la regla preescrita:

\[
\boxed{\texttt{L2\_GATE = B / OPEN\_BLOCKED\_METHOD}}.
\]

## 5. Alcance

B significa que el objetivo fuerte de supervivencia queda bloqueado por el
método actual. No significa \`H1=false\`, no aporta contraejemplo ni cota
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
- el informe no necesita afirmar que `H1c_LOCALIZATION` sea la única vía posible.

**No comprobado por esta revisión:**
- las derivaciones fuente de las dos cotas de §2 no se han reconstruido desde sus artefactos anteriores;
- no se ha demostrado que no exista otra cancelación, identidad o representación capaz de cerrar A;
- no se ha resuelto si el objeto denominado aquí “resto terminal-P” coincide exactamente con la pieza `stay` usada en la resta de §2.

**Pendiente:**
- reconciliar documentalmente `terminal-P` frente a `stay`;
- si se desea promoción por encima de `PARTIAL_EXTERNAL_REVIEW`, realizar una revisión independiente que remonte las dos cotas de §2 a sus fuentes.
