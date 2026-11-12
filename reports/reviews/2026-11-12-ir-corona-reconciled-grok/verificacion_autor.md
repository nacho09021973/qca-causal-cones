# Lectura del autor (sesión Claude, claude-fable-5-2), 2026-11-12

Informe: `informe_grok.md` (grok-4.7, `COMPLETED`, herramientas `7d111a1`,
08:54–09:22 UTC), sobre `ir-corona-anon.tex` = `papers/ir-corona/ir-corona.tex`
en `b5cc166` (etiqueta `ir-corona-v2`) con cinco cadenas identificativas
sustituidas. Una ronda. El revisor no tuvo herramientas, certificados ni
bibliografía.

Dictamen del revisor: global **REPAIR_REQUIRED**; A PASS, B PASS, C PASS,
D REPAIR_REQUIRED. «Nada de lo rederivado justifica REJECTED.» Los pasos
fusionados (planos, Poisson, Bob, (d), condiciones sobre r_0, rama
recíproca) «no se pisan».

Esta lectura comprueba cada objeción; no aplica ninguna reparación al
manuscrito: eso lo decide el usuario.

## Objeciones

1. **Lema de saltos: prueba incompleta.** Aceptada. La prueba impresa solo
   calcula el coeficiente de z1 z2 z3. El enunciado es cierto (rehecho en
   esta sesión y por el revisor: ocho vértices con 1/4 por proyector
   diagonal, cuatro diagonales de cara de norma 1/4, dos axiales de norma
   1/2, suma 4). Reparación de exposición: escribir la expansión completa.
   Lean ya la contiene para el núcleo (`formal/README.md`, «Found while
   formalizing»).

2. **Frase de las derivadas laterales de Phi.** Aceptada como ambigüedad,
   no como error. El texto dice «the one-sided directional derivatives are
   −|x| and |x|». Leída como derivadas por la izquierda y por la derecha de
   s ↦ Phi(s x) en s = 0 es correcta (Phi(sx) = |s||x| + O(s^3)) y es lo
   que hace falta: el salto es creciente, luego la restricción a cada recta
   es convexa. Leída como derivada direccional en las direcciones x y −x es
   falsa, como dice el revisor (vale +|x| en ambas). Reparación: decirlo
   con s ↦ Phi(sx).

3. **Presupuesto del término a_c frente al diagnóstico 15.2, 9.4, 6.4.**
   Aceptada como reparación de exposición; la cota no cambia.
   - La cota N^(-17/2) es absoluta: capa de Alice con c_N ≤ C N^(-4) d^4,
     recurso N^(-3/2) y área N da N^(-9/2) para todo eta; capa de Bob
     N^(-5/2) (Layers (a)); integral de ||S~_N|| de orden N^(-3/2). No
     depende de ningún desarrollo.
   - El manuscrito ya dice que esos cocientes «scale approximately as 1/N,
     not 1/N^2, and do not validate the relative asymptotic order». Lo que
     falta es decir por qué no hay contradicción: el propio apéndice da
     semi/lead = 0.906 en N = 10^3, es decir una corrección relativa de
     orden −100/N, de modo que N ≤ 56 está muy por debajo del régimen
     asintótico y un exponente aparente en ese rango no informa del orden.
     Además el coeficiente principal de esas parejas es el más pequeño
     (0.075) frente a un coeficiente de a_c sin esa cancelación.
   - El revisor señala, con razón, que aun con N^(-15/2) el teorema
     principal seguiría en pie (N^(-1) = o(N^(-1/2))).
   Esta explicación es del autor de la lectura y no está certificada.

4. **No anulación: NO_VERIFICADO por el revisor.** No es una objeción a la
   lógica (la da por suficiente) sino a que los certificados no van en el
   manuscrito. Estado: los cuatro certificados pasan hoy
   (`papers/ir-corona/certificados/2026-11-12/`), incluido el margen de las
   dieciséis parejas; doce entradas de la Tabla 1 y su margen se
   recalcularon hoy por una segunda vía en coma flotante. Pendiente real:
   el repositorio es privado; hace falta un archivo público con DOI antes
   de enviar (ya anotado como TODO en el bibitem).

5. **«Flat direction».** Aceptada. u_perp + u'_perp recorre un plano de
   dimensión 2; el texto dice «direction». Exposición.

6. **288 N^7.** El texto lo atribuye a [Repo], no lo demuestra. Sin cambio
   necesario; puede decirse «recorded in».

7. **4 e^(3t_* − Phi_*) < 9.2 (bloque B).** Aceptada. El texto dice
   «numerically» y ningún certificado lo comprueba (búsqueda en los tres
   scripts y en sus salidas: sin coincidencias). Se sigue de los
   encierros certificados de t_* y Phi_*: con t_* < 0.7358 y
   e^(Phi_*) > 3.9731, 4 e^(2.2074)/3.9731 < 9.16. Valor en coma flotante
   de esta sesión: 9.1522. Reparación: escribir esa deducción o añadir la
   comprobación a un certificado (lo segundo cambia bytes de un verificador
   revisado y exige nueva revisión de ese fichero).

## Balance

Ninguna objeción afecta a un enunciado ni a una constante. Cinco
reparaciones de exposición (1, 2, 3, 5, 7), una nota (6) y una obligación
de publicación (4). El revisor rederivó de forma independiente, entre otras
cosas, las fases cerca de pi u, la constante K, la potencia 13/2, los
prefactores de capa, la cota de rho, la rama recíproca y cuatro filas de
la tabla del apéndice.

Límites: una sola casa (xAI), una ronda, sin ejecución de código. No cubre
novedad ni bibliografía. No promociona nada. El manuscrito sigue
PRELIMINARY hasta que el usuario decida sobre las reparaciones.

## Reparaciones aplicadas (2026-11-12, usuario «sigue»)

Aplicadas en `.tex` y `.md`, solo exposición; ningún enunciado ni constante
cambia, y el enunciado de Lemma Layers sigue idéntico al de la prueba Lean.

1. Lemma Jumps: prueba completa (expansión en z_j de las cuatro entradas,
   bloques y normas, suma 4).
2. Convexidad de Phi: la frase de las derivadas laterales se reescribe con
   s ↦ Phi(sx) y se dice qué cubre el hessiano.
3. Apéndice: por qué los cocientes 15.2, 9.4, 6.4 no contradicen la cota
   absoluta N^(-17/2) del término a_c (régimen no asintótico en N ≤ 56,
   corrección relativa ≈ −100/N, coeficiente principal mínimo).
5. «Flat direction» → dos direcciones / un plano, en la introducción y en
   el recuento de la potencia.
6. 288 N^7: «as recorded in [Repo] and not proved here».
7. 4e^(3t_*−Phi_*) < 9.2 deducido de los encierros certificados de t_* y
   Phi_* (4e^(2.2074)/3.9731 ≈ 9.154).

Objeción 4 (certificados fuera del manuscrito) sigue abierta hasta que
exista un archivo público con DOI. Las reparaciones no se han re-revisado.
Bibitem y Markdown citan la etiqueta `ir-corona-v3`, creada en el commit de
estas reparaciones. Compila: 21 páginas, sin referencias sin definir.
SHA256: `.tex` 6b307c4c…, `.md` c70966aa….
