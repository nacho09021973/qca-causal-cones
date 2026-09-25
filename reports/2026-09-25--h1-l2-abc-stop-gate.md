# H1 / L2: gate A/B/C de parada sobre el resto terminal-P físico

Fecha: 2026-09-25.

Estado:
```
L2_GATE = B / OPEN_BLOCKED_METHOD
EVIDENCE = PRELIMINARY_DECISION_AUDIT / NO_INDEPENDENT_REVIEW
H1 = OPEN
```

Este gate no demuestra que H1 sea falsa. Registra únicamente que, con las
hipótesis congeladas y el aparato ya disponible, no se alcanza la escala
necesaria para probar la estabilidad fuerte del término terminal-P físico.
No se abre un nuevo lema de localización, no se ejecuta código numérico y no
se añaden hipótesis sobre `vartheta`.

## 1. Objeto y regla preescrita

El objeto es el resto dependiente de `vartheta` de la contribución
terminal-P de `A_{+P}`, no `A_{+P}` completo. La abreviatura
`PP[vartheta]-PP[0]` usada en la discusión significa aquí esta pieza física
terminal-P/stay y no el observable `Lpp` de la Sec. 10.

La escala plana relevante es
[
L_{m lead}(N)asymp N^{-13/2}e^{-K_*N}.
]

Salidas:
- **A — PROVED:** resto `o(N^-13/2 e^-K*N)` con las hipótesis congeladas.
- **B — OPEN/BLOCKED:** las cotas disponibles no llegan a esa escala o hacerlo
  exige nueva maquinaria/hipótesis. B es obstrucción del método, no refutación.
- **C — REFUTED:** aparece un perfil admisible con cota inferior,
  contraejemplo o equivalente que impide la subdominancia.

## 2. Cotas físicas disponibles

El informe de transferencia de extremos registra la resta exacta de la pieza
stay:
[
langle r_artheta,E V x_artheta^{m stay}angle
-langle r_0,E V x_0^{m stay}angle
=
langle r_artheta-r_0,E V x_artheta^{m stay}angle
+
langle r_0,E V(x_artheta^{m stay}-x_0^{m stay})angle.
]

Con el expediente actual:
- el primer sumando queda sólo en
  (O_{W,Theta}(N^{-5}e^{-K_*N})), usando el control geométrico
  (|Edelta r|lesssim C_BTheta N^{-2}) y
  (|x_artheta^{m stay}|=O_{W,Theta}(N^{-3}));
- el segundo queda sólo en
  (O_{W,Theta}(N^{-6}e^{-K_*N})), aun usando el extremo plano de Bob.

Ambas potencias son mayores que (N^{-13/2}=N^{-6.5}). No prueban
subdominancia y tampoco prueban que ésta sea falsa. Incluso concediendo L1,
el producto normativo (N^{-3}N^{-3}) sólo da (N^{-6}), así que L1 no
resuelve L2.

## 3. Resultados finos existentes que no transfieren

`2026-09-20--h1-inhomogeneous-localization-reconstruction.md` obtiene
(N^{-15/2}) para una inserción G dentro de una ventana de saddle fija, pero
declara expresamente que no se sigue localización global y deja
`H1c_LOCALIZATION (L') = OPEN`: faltan cadenas a momento variable, visitas
a Q, transiciones entre las ocho ventanas y el exterior.

`2026-09-24--h1c-dyson-target-check.md` y la descomposición Dyson exacta
controlan un test de moneda constante sobre los caminos y extremos planos
fijados. El símbolo completo da allí una corrección relativa (O(N^{-1})).
Ese test conserva homogeneidad en la zona relevante y no controla el
`A_{+P}` físico con perfil espacial variable y ambos extremos dependientes
del propagador. No decide A ni C para L2 físico.

## 4. Aplicación de la regla de parada

Para mejorar (N^{-5})/(N^{-6}) hasta
(o(N^{-13/2})) en el resto físico hace falta precisamente la estructura que
el expediente llama `H1c_LOCALIZATION`: localización gaussiana/fase y
transporte a momento variable del elemento físico. Abrir esa prueba sería
nueva maquinaria, que la regla de parada decidió no iniciar en este intento.

No se reabre Schur (7)–(8), no se abre L1 ni L3 como ruta de rescate y no se
convierte la observación de paridad `Gamma` en un frente nuevo.

Por la regla preescrita:
[
oxed{	exttt{L2_GATE = B / OPEN_BLOCKED_METHOD}}.
]

## 5. Alcance

B significa que el objetivo fuerte de supervivencia queda bloqueado por el
método actual. No significa `H1=false`, no aporta contraejemplo ni cota
inferior, no decide dominancia y no afecta al resultado plano cerrado.

No hay salida C. No se ejecutó ningún barrido de
(PP[artheta]/PP[0]).

## 6. Decisión de programa

Se detiene aquí el intento fuerte de L2. H1 permanece **OPEN** y el objetivo
fuerte queda **OPEN/BLOCKED por el método actual**. Los huecos L1 y L3 no se
abren como rutas de rescate. Cualquier reapertura de la supervivencia fuerte
requiere una decisión explícita que acepte nueva maquinaria o hipótesis.
