# Respuesta de Astra 6.2 (web) — texto íntegro tal como lo pegó el usuario

Procedencia:
- Usuario, 2026-11-27: «es de Astra 6.2 por la web».
- Pegado en la sesión de Claude Code el 2026-11-27.
- No pasó por `revision-ciega`, así que no hay cabecera sellada, SHA256 de
  entrada ni registro de modelo o esfuerzo. Son `[UNVERIFIED]`:
  - qué prompt exacto se envió (el que dio Claude está en `prompt.md` de esta
    carpeta);
  - qué ficheros se adjuntaron o leyó el modelo;
  - el modelo exacto y su configuración.
- Las marcas sueltas del texto («Nota, §3», «Contrato del paseo · Perfil
  completo y truncación de los cálculos previos», «Alcance del contrato, línea
  194», etc.) parecen anclas de citas de la interfaz web, perdidas al copiar.
  Se conservan sin tocar.

Texto (sin modificar):

---

La conjetura necesita una corrección de dominio antes de intentar demostrarla. La nota admite perfiles con κ=0, para los cuales (C1) ni siquiera define X(μ). Además, (C3) debe nombrar las dos salidas que conservan flujo, y (C4) debe distinguir qué parámetro puede variar en el paseo fijado. He contrastado el enunciado con la nota de la rama research/dispersive-horizon-channels, commit 73fc0b8. Nota, §3

### 1. El cruce debe ser simple — DEMOSTRADO

Considérese
\[
\phi(s)=\frac1{16}\tanh(s^3).
\]
Es suave y estrictamente creciente porque tanto s↦ s³ como \(\tanh\) lo son. Cumple ϕ(0)=0. Para s≥1,
  1             1          1
0<──-ϕ(s)= ──────────── ≤  ─ e⁻²ˢ,
  16       8(e^{2s³}+1)    8
y la otra cola satisface la misma cota por imparidad. Sin embargo, ϕ'(0)=0. Por tanto, el perfil satisface las hipótesis escritas y deja indefinido el cociente 2πμ/κ.

Hay una segunda razón para corregir el dominio. En este ejemplo 8ϕ(s)=s³/2+O(s⁹). Bajo el escalado propuesto x=L^{1/3}y, k=L^{-1/3}q, el término L 8ϕ(x/L)k tiende a cero para y,q fijos. Así se pierde precisamente el término κ yq que debía describir el cruce. Asignar X=0 por continuidad en κ dejaría pendiente un problema asintótico distinto.

Corrección: exigir ϕ'(0)>0. El ejemplo demuestra el defecto del enunciado original. La ley para cruces simples sigue abierta.

### 2. Enunciado final que usaría — CONJETURA ABIERTA

Fíjese el paseo U=L₋W² con las convenciones del contrato. Sea ϕ∈ C^{∞}(ℝ) estrictamente creciente, con ϕ(0)=0, ϕ'(0)>0 y límites ±1/16 alcanzados con error exponencial en los extremos respectivos. Para x∈ℤ, úsese el perfil completo t_{L}(x)=3/8+ϕ(x/L). Escríbase κ=8ϕ'(0). La uniformidad que sigue se exige en μ para cada perfil fijo. Contrato del paseo · Perfil completo y truncación de los cálculos previos

Para cada compacto no vacío K⊂(0,∞), se conjetura que existe L₀(ϕ,K) tal que, para todo L≥ L₀ y toda μ∈ K, a cuasienergía ω=μ/L están definidos los canales indicados abajo y la matriz de dispersión S_{L}(ω) entre los medios asintóticos t₋=5/16 y t₊=7/16. Por «definida» entiendo que cada incidencia admite una solución física sin componentes evanescentes crecientes en ninguno de los extremos y que sus amplitudes propagantes salientes quedan determinadas de manera única. Esto permite definir S incluso si la solución interior solo fuera única módulo un estado localizado. La existencia puntual para toda μ∈ K queda como obligación del punto 2.

En bases de flujo unitario, denótense por r,c los dos canales incidentes interiores de velocidad positiva de la nota, con -π/2<kᵣ<0<k_{c}<π/2. Denótese por e el canal saliente exterior de la hoja de bajo k que llega a k=0 cuando ω↓0, y por u el saliente interior de esa misma hoja que llega a k=0. Los índices de S_{b,a} indican salida b e incidencia a. Definiciones originales de los observables

Con X_{ϕ}(μ)=(1+e^{2πμ/κ})⁻¹ y todas las entradas evaluadas en ω=μ/L, el enunciado es

| Apartado | Límite conjeturado, uniforme en K |
|---|---|
| C1 | | S_{e,r}|²→ X_{ϕ}(μ). |
| C2 | | S_{e,c}|²→ 1-X_{ϕ}(μ). |
| C3 | | S_{u,r}|²→ 1-X_{ϕ}(μ) y \(\displaystyle\sum_{b\notin\{e,u\}}\lvert S_{b,r}\rvert^2\to0\), sumando sobre las salidas propagantes. |
| C4 | Dos perfiles admisibles con la misma ϕ'(0) tienen los mismos límites anteriores. |

En C3 hay que exceptuar ambas salidas, e y u. Para μ>0 y κ>0, C1 asigna a e una probabilidad límite estrictamente positiva. Si en el punto 2 se establece unitariedad en flujo, la desaparición del resto de la columna se deducirá de C1 y del límite de | S_{u,r}|², restando ambas probabilidades de uno.

Alcance de C4 — DEMOSTRADO como cuestión de formulación. Todos los perfiles del enunciado cruzan el mismo tₕ=3/8 bajo la misma regla. En la expresión de γ(t) de la nota, esto fija γₕ=35/32. La comparación entre perfiles solo pone a prueba la universalidad respecto de ϕ. La posible cancelación de γₕ en el coeficiente de conexión es una pregunta bien definida para el punto 4. Una ley entre paseos con distintos γₕ requeriría especificar qué familia se compara. Coeficiente cúbico de la hoja

Veredicto del punto 1: STATEMENT_REPAIRED_THEN_PARTIAL. Queda demostrado el defecto de dominio y queda formulada la versión de cruce simple. La primera obligación abierta es justificar que S_{L}(μ/L) y las etiquetas de canal existen en todo el rango cuantificado para el perfil completo. El contrato anterior excluyó expresamente la existencia y unicidad de esa matriz. Alcance del contrato, línea 194
