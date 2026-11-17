# Revisión sellada: gate S4 de isotropía DEP

Autorización: usuario «revision ciega Codex» (2026-11-17). Envío a OpenAI
(Astra, `gpt-6-astra` vía `codex exec`; generación comprobada el
2026-11-17 con una llamada de prueba). Autor: Claude (Opus 5.5); revisor:
Astra (OpenAI), otra familia. Herramientas: ~/herramientas 7d111a1.
Candidato: reports/2026-11-17--s4-dep-isotropy.md en `251c163`; contrato
congelado en `9188755`; verificador subido antes de ejecutar en `fdae12c`,
corrección de método en `36fb8fd` (ejecución 1 fallida, conservada).

Objetivo: decidir si el veredicto DEP_ISOTROPIC_IN_DECLARED_L está bien
fundado y bien acotado. Resultado esperado: dictamen por bloque. Máximo:
una ronda. Cierre: PASS → el usuario decide si promociona (no autorizado
por este encargo); otro dictamen → reparaciones y nueva decisión del
usuario.

---
Revisa adversarialmente el informe adjunto 2026-11-17--s4-dep-isotropy.md,
escrito por Claude (Anthropic). Se adjuntan: el contrato congelado
S4_DEP_ISOTROPY_GATE.md; la definición de la familia
S4_STRICT_CONE_COUNTEREXAMPLE.md; el verificador verify_s4_dep_isotropy.py;
la salida de la ejecución 1 (fallida) y de la ejecución 2; y la fuente
primaria D'Ariano-Erba-Perinotti, arXiv:1708.00826v2, en texto extraído.
No tienes herramientas: no ejecutes, edites ni navegues. Que el script
imprima PASS no prueba lo que el script no calcula: comprueba que calcula
lo que dice.

Dictámenes separados PASS / REPAIR_REQUIRED / OPEN:

1. FIDELIDAD A LA FUENTE. ¿Traducen el contrato y el informe con fidelidad
   la Definición 1 de 1708.00826 (grupo L de automorfismos del grafo de
   Cayley que actúa como permutaciones de S_+, transitivo en cada S_+^n,
   representación unitaria proyectiva, covarianza A_lambda(h) =
   U_l A_h U_l^dagger) y la condición de homogeneidad (2)? ¿Falta alguna
   condición de la fuente que haga falta para llamar «isótropo» al walk en
   su sentido (p. ej. A_h ≠ 0 en S_+ ∪ S_-, el tratamiento de S_-, la
   elección de S_+ en el BCC, fidelidad de la representación)?
2. FAMILIA. ¿Reconstruye el verificador exactamente la familia de
   S4_STRICT_CONE_COUNTEREXAMPLE.md en theta = pi/4 (T_i, Gamma_i, P_i^±,
   W_theta, coeficientes A_h, convención de signos h_s, orden del producto
   tensorial)? ¿Es correcta la identificación de las medias vueltas l y de
   la acción h -> l(h) usada en C2?
3. MÉTODO EXACTO DE C1 Y C4. ¿Es legítimo sustituir A_h por M_h
   (A_h = W M_h, W unitaria y conmutando con U_l)? ¿Es correcta la
   parametrización racional del arco (biyección de t en (0,1) sobre
   0<a<1, b>0)? ¿Es correcto que los ceros comunes de las entradas son las
   raíces reales en (0,1) del mcd de las partes real e imaginaria de los
   numeradores, sin perder ceros por denominadores ni por la separación
   real/imaginaria? ¿Hay algún paso que dependa de simplify o de una
   comparación no rigurosa?
4. C2, C3, C5. ¿Son correctas y suficientes las comprobaciones de
   covarianza (24 identidades), transitividad y representación
   proyectiva?
5. EJECUCIONES. ¿Es el cambio entre la ejecución 1 y la 2 un cambio de
   método sin cambio de expectativas, como dice el informe? ¿Hay algo en
   las salidas que contradiga el veredicto?
6. ALCANCE. ¿Separa el informe lo calculado de lo afirmado? ¿Es correcta
   la frase «la rigidez s=2 no persiste a s=4 dentro de esa noción de
   isotropía», dado que c_0 = a/sqrt3 se toma de un resultado anterior no
   adjuntado como prueba? ¿Evita afirmar novedad, isotropía cúbica,
   otros theta o grupos?

Para cada REPAIR_REQUIRED, da la reparación mínima concreta. Termina con
un dictamen global.
---
