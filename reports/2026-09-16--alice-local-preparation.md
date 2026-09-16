# Preparación desde Alice y señalización fuera del cono emergente

Base inspeccionada: `research/b-infinity-post-s4-gate`, HEAD y referencia
local `origin/research/b-infinity-post-s4-gate` en
`dc9776016ad540ef54a1714e510b378670fa42d9`. No se consultó el remoto en vivo.
Autorización: petición directa del usuario del 2026-09-16, sólo existencia.
El witness anterior, su revisión y el estado canónico se conservan intactos.

## 1. VEREDICTO

**`EXISTENCE_CONSTRUCTED`**

Una partícula inicialmente en Alice basta. La dinámica genera la coherencia
necesaria antes de elegir el mensaje. En esta construcción **el sitio de Bob
está vacío tanto inicialmente como al codificar**.

Evidencia: derivación algebraica y **21/21 controles exactos**. El nuevo
resultado no tiene revisión independiente ni promoción al estado canónico.

## 2. DEFINICIÓN OPERACIONAL

«Inicialmente local» significa que, en tiempo absoluto `T=0`, hay exactamente
una partícula pura con soporte en `R_A={0}` y todos los modos exteriores están
en el vacío. No hay amplitud exterior, coherencia Alice–exterior ni un recurso
espacialmente separado. Se admite esa partícula como recurso local inicial;
no se presupone que una operación par cree una partícula desde el vacío.
Su densidad de número fijo respeta la superselección de paridad.

La preparación posterior usa exclusivamente la evolución libre ya declarada,
igual para ambos mensajes. Alice permanece en el origen. El bit se elige en
`T=2`; Bob mide en `T=3`. La coherencia que la dinámica produce entre `T=0`
y `T=2` es un recurso generado causalmente desde Alice.

Una definición más restrictiva que exija soporte sólo en Alice **al elegir**
impide señalizar con esta puerta de fase: actúa globalmente sobre un estado
de una partícula allí. Esto es una obstrucción para esa puerta y esa clase,
no para toda intervención interna local admisible. Más generalmente, si
la densidad al elegir carece de bloques coherentes Alice–resto, esta puerta
la deja invariante. La construcción no necesita coherencia con Bob al elegir.

## 3. ARGUMENTO

Se conserva el lift CAR de CJWW (5.15), dos modos internos por sitio,
`c_IR=1`, `C_micro=[-1,1]^3`, y la convención
`K_t(x,z)=(W^t)_{x,z}`. Escribimos `S=W†`; los estados evolucionan con `S`.
El símbolo ya existente es

\[
W(p)=\begin{pmatrix}
c_1c_2e^{ip_3}&-c_1s_2+i s_1\\
c_1s_2+i s_1&c_1c_2e^{-ip_3}
\end{pmatrix},\qquad c_j=\cos p_j,\ s_j=\sin p_j.
\]

El protocolo completo es

\[
|\psi_{\rm initial}\rangle=|0,\downarrow\rangle,
\quad t_{\rm prep}=2,\quad
U_A^{(0)}=I,\quad U_A^{(1)}=e^{i\pi n_0},
\]
\[
t_{\rm read}=1\ \text{después de elegir}\ (T_B=3),\qquad
y_B=(1,1,1),\qquad M_B=I-|\mathrm{vac}_B\rangle\langle\mathrm{vac}_B|.
\]

No hay intervenciones durante la preparación, ancillas, medidas intermedias
ni postselección. La clase se fijó antes de ejecutar: soporte inicial de un
sitio, espín down, esta misma puerta, dos pasos de preparación y un paso
de lectura al vértice `(1,1,1)`. Se detuvo la evaluación al certificarlo.
Los tiempos menores se descartan algebraicamente: con cero pasos la fase es
global; con uno el origen queda vacío, pues todos los saltos tienen primera
coordenada `±1`. Dos es el primer tiempo de preparación posible **en esta
clase de evolución libre y puerta en el origen**; no es optimización global.

Sea `P=P_0` el proyector uniparticular del sitio de Alice y
`Q=I-P`. La preparación común es `χ=S²|0,down>`. Para cualquier `χ`, los
dos brazos que llegan a Bob tras un paso son

\[
a=(SP\chi)_{y_B},\qquad r=(SQ\chi)_{y_B},\qquad
v_0=a+r,\quad v_1=-a+r.
\]

Por tanto el término físicamente necesario es

\[
p_1-p_0=-4\operatorname{Re}(a^\dagger r).
\]

Los bloques reutilizados y el bloque de un paso dan

\[
K_2(0,0)=-\frac34 I_2,\qquad
K_1(0,y_B)=\operatorname{diag}(0,1/4),\qquad
P\chi=-\frac34|0,\downarrow\rangle,
\]
\[
\|P\chi\|^2=\frac9{16},\qquad
\|Q\chi\|^2=\frac7{16},\qquad a=-\frac3{16}\downarrow.
\]

Para calcular la amplitud total sin selección de caminos, `det W=1` y
`tr W=2f`, con `f=c_1c_2c_3`, implican por Cayley–Hamilton

\[
W^3=(4f^2-1)W-2fI.
\]

En su entrada down–down, el coeficiente de `z_1^{-1}z_2^{-1}z_3^{-1}` es

\[
4\left(\frac38\right)^2\frac12-\frac14-\frac14
=-\frac7{32}.
\]

Las entradas no diagonales tienen exponente par en `z_3`, de modo que no
contribuyen a ese monomio. En la convención fijada resulta

\[
v_0=(S^3|0,\downarrow\rangle)_{y_B}=-\frac7{32}\downarrow,
\qquad r=v_0-a=-\frac1{32}\downarrow,
\qquad v_1=\frac5{32}\downarrow.
\]

Así, la propia evolución ha generado ambos brazos. Además, tras dos pasos
toda amplitud tiene primera coordenada par, luego `χ(y_B)=0`: el brazo
exterior no fue colocado en Bob y ni siquiera ocupa Bob al elegir el bit.

## 4. CAUSALIDAD

Los eventos del mensaje son `A=(T=2,0)` y `B=(T=3,(1,1,1))`:

\[
\Delta T=1,\qquad \|y_B\|_2=\sqrt3>c_{IR}\Delta T=1,
\qquad \|y_B\|_\infty=1.
\]

Bob está fuera del cono emergente de la elección y en un vértice de
`ΔT C_micro=[-1,1]^3`. El bloque no nulo `K_1(0,y_B)` demuestra pertenencia
al **soporte exacto**, además de pertenencia a su envolvente convexa.
Es frontera microscópica, no interior estricto.

Durante la preparación el soporte está contenido en `[-T,T]^3`, y tras la
lectura en `[-3,3]^3`, en ambas ramas. La intervención en el origen no altera
la dinámica ni el soporte instantáneo. Desde el inicio de la preparación
hasta la lectura, `sqrt(3)<3`: no se afirma que Bob esté fuera del cono
emergente del evento inicial. La referencia causal del mensaje es `T=2`.

## 5. WITNESS

En la base local `(vac,up,down,up-down)`, la medida es
`M_B=diag(0,1,1,1)`, una proyección par de norma uno. Las densidades son
`ρ_B^(b)=diag(1-p_b,0,p_b,0)`, y

\[
\boxed{p_0=\frac{49}{1024},\qquad p_1=\frac{25}{1024},\qquad
\Delta p_B:=|p_1-p_0|=\frac3{128}>0.}
\]

La diferencia con signo es `p_1-p_0=-3/128`: codificar reduce la ocupación.
Con `D=(1/2)||ρ_1-ρ_0||_1`, el bound para cualquier efecto da directamente
`D≥Δp_B=3/128`. No se optimizó la medida ni se necesitó calcular `D`.

## 6. CONTROLES

1. **Localidad inicial:** soporte `{0}`, norma uno, vacío exterior; ninguna
   coherencia Alice–Bob introducida externamente.
2. **Preparación común:** `S²|0,down>` coincide exactamente con dos pasos
   consecutivos. Las ramas se crean sólo después, al aplicar o no la puerta.
3. **Intervención única:** se niega sólo la componente en el origen. La
   puerta local completa es `diag(1,-1,-1,1)`, par y conservadora del número.
4. **Fase relativa:** pesos `9/16` y `7/16` de ambos brazos; no es una fase
   global. Sin preparación la señal es cero; tras un paso también.
5. **Geometría desde la elección:** desigualdad emergente estricta y bloque
   microscópico exacto no nulo, con las normalizaciones anteriores.
6. **Distinguibilidad:** las dos normas globales son uno y las densidades
   reducidas son positivas, normalizadas, con las probabilidades racionales
   indicadas. Extracción directa de `W³` y evolución secuencial concuerdan.
7. **Sin codificador:** sustituir la segunda opción por identidad iguala
   las densidades completas de Bob.
8. **Sin interferencia relevante:** sustituir sólo al elegir
   `|χ><χ|` por `P|χ><χ|P+Q|χ><χ|Q` preserva poblaciones y coherencia interna
   del resto. Esta densidad conmuta con `I-2P`; las dos ramas son idénticas.
   El cálculo explícito da `p_0=p_1=37/1024` y densidades de Bob iguales.
   Es un control contrafáctico, no una operación adicional del protocolo.
9. **Control fuera del soporte microscópico:** en `y_ax=(2,0,0)` con un
   paso desde la elección, `K_1(0,y_ax)=0` y las densidades locales coinciden,
   aunque la preparación anterior pueda haber alcanzado ese sitio. El cero
   del kernel excluye al origen del álgebra evolucionada de Bob.
10. **Bob vacío al elegir:** `χ(1,1,1)=0` exactamente. No hay coherencia con
    su sitio ni al inicio ni en el evento de codificación.

## 7. EVIDENCIA REUTILIZADA

Se leyeron antes de calcular el [witness congelado](../theory/COUPLING_MAP_SIGNALING_WITNESS.md),
su [revisión independiente](2026-09-16--signaling-witness-independent-review.md),
el [estado canónico](../state/CURRENT_STATE.md), las instrucciones del proyecto,
el [informe del mapa de acoplamiento](2026-09-16--coupling-map.md), su contrato
y los dos verificadores.

La sección 8 del estado fija el modelo y los dos conos; la 8.12 deja
explícitamente abierta la preparación desde Alice. El informe del mapa ya
contenía la identidad de interferencia y advertía que «localized» sólo
anula esta puerta cuando se aplica sin preparación espacial previa.
Eso resolvía el mecanismo y la obstrucción inmediata, pero no este protocolo.

Se reutilizan `walk2`, `laurent`, `exact_blocks`, `square_kernel`, `evolve`,
`phase_choice`, `norm_squared` y `reduced_state`, sin modificar sus cuerpos.
Los auxiliares exactos permiten responder sin el muestreo histórico de
rotaciones internas ni el helper de kernels con números Python `complex`.

## 8. CAMBIOS MÍNIMOS PROPUESTOS

Aplicado sólo lo necesario: este informe y una función de certificación con
opción `--local-preparation-only` en el verificador existente
[`verify_directional_saturation.py`](../scripts/verify_directional_saturation.py).
No se creó otro script ni se modificaron los cálculos anteriores. La opción
separa esta comprobación de las búsquedas históricas y conserva la procedencia
del cálculo nuevo sin tocar el verificador del witness congelado.

Reproducción desde la raíz:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_directional_saturation.py --local-preparation-only
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_signaling_witness.py
git diff --check
```

Resultado nuevo: **21/21 controles exactos**. Witness congelado: **17/17**.
No commit ni push. Estado canónico y archivos ajenos o previamente sin
seguimiento intactos. El archivo importado `verify_directional_saturation.py`
sí cambia por la nueva función y la selección CLI: el hash antiguo de ese
archivo sigue identificando la revisión histórica, no esta extensión.
El símbolo y los auxiliares importados por el witness conservan sus cuerpos.

## 9. LÍMITES

Es una construcción finita en el mismo modelo, con una partícula y la puerta
de fase original. Exige coherencia Alice–resto al elegir; demuestra que puede
generarse desde un recurso estrictamente local, y que no necesita alcanzar
el propio sitio de Bob antes de elegir. No exige mantener localizado el
estado durante toda la preparación.

No demuestra optimalidad, viabilidad experimental, señalización fuera del
soporte microscópico, comportamiento asintótico, capacidad de canal ni
conclusiones sobre nuestro universo. Tampoco prueba imposibilidad para otras
puertas si se exige localidad al elegir. Una partícula localizada no es una
preparación restringida al sector de baja energía de la teoría emergente.
El resultado previo y su revisión conservan exactamente su alcance; este
sucesor no hereda automáticamente su estado de revisión independiente.
