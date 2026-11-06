# Revisión ciega, ronda 1 — borrador v2 de la carta DIRAC_VGRP_MAX

Bytes revisados: commit `5ebe10d` de la rama `theory/massive-vgrp-bcc` (base `main` `bce5599`).
Fecha: 2026-11-06. Autorización del usuario: «Revisión primero: lanza revision-ciega deepseek,
autorizado»; DeepSeek sin saldo (fallo de cuenta), sustituto Grok aceptado por el usuario («vale»).
Objetivo: decidir si la carta puede congelarse como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY; objeciones numeradas G-V-NN con
ubicación y gravedad.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude, salvo los ficheros citados como contrato o verificador
ya revisados.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Herramienta: revision-ciega del PATH, `~/herramientas` `ce09890`.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, dispersión de sectores con masa, geometría algebraica real efectiva). Solo
tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar código. No supongas
que nada es correcto.

Documento 1: el borrador v2 de la carta `DIRAC_VGRP_MAX_GATE.md` (aún no congelada).
Documentos 2–4: la nota de las tres velocidades, el contrato de la puerta Weyl/Dirac estándar y
su verificador exacto (de donde salen `u`, `cos ω = n u` y la normalización de unidades).

Comprueba:
1. Definiciones: ¿son correctas `ω = acos(n u)`, la normalización `k = sqrt(3) q`, la fórmula de
   `Φ` y la afirmación `|n u| <= n < 1` en el toro? ¿Queda `V_grp^max` bien separado de `c_IR`,
   `c_H`, `c_{ω^2}` y `C_micro`?
2. Etapa A: ¿basta enumerar los puntos críticos de `Φ` en las cartas `tan(q/2)` / `cot(q/2)` para
   obtener el máximo global? ¿Cubren las cartas todo el toro? ¿Introduce el despeje de
   denominadores soluciones espurias o pierde alguna? ¿Es correcto el tratamiento de componentes
   de dimensión positiva? ¿Es válida la alternativa A5 (SOS racional más testigo exacto)?
3. Etapa 0: ¿falta alguna comprobación exacta (por ejemplo, la reducción entre los cuatro
   símbolos, o el signo de las dos ramas `±ω`) antes de usar simetrías?
4. Etapa B: ¿queda de verdad relegada a diagnóstico? ¿Es decidible y no circular la regla de
   discrepancia B3?
5. Hipótesis H1–H3 y veredictos: ¿son decidibles con lo que la carta calcula? ¿Algún veredicto
   promete más de lo que se puede certificar en cinco masas de una familia?
6. Reglas de parada, presupuesto y exclusiones: ¿son suficientes para que la puerta no se amplíe?
7. Alcance: ¿alguna frase afirma como sabido algo que la carta no ha comprobado?

Salida: veredicto global; una sección por punto; objeciones G-V-NN con ubicación y gravedad
(error demostrado, laguna o redacción). Una sola ronda: declara tus supuestos.
---
