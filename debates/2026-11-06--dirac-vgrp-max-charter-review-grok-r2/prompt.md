# Revisión ciega, ronda 2 (acotada) — borrador v3 de la carta DIRAC_VGRP_MAX

Bytes revisados: commit `7697593` de la rama `theory/massive-vgrp-bcc` (base `main` `bce5599`).
Fecha: 2026-11-06. Autorización del usuario: «SI» a aplicar las reparaciones, fijar las
tolerancias en `1e-9` y hacer una segunda ronda acotada con Grok antes de congelar.
Objetivo: comprobar que la v3 resuelve G-V-01..17 sin introducir errores nuevos, y decidir si
puede congelarse como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY; por cada objeción de la ronda 1,
RESUELTA / PARCIAL / NO RESUELTA; objeciones nuevas numeradas G-V-R2-NN, solo si las introduce
la v3 o si quedaron sin ver en la ronda 1 y cambian un veredicto.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude, salvo el contrato y el verificador Weyl/Dirac.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Herramienta: revision-ciega del PATH, `~/herramientas` `ce09890`.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, dispersión de sectores con masa, geometría algebraica real efectiva). Solo
tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar código. No supongas
que nada es correcto.

Documento 1: el borrador v3 de la carta `DIRAC_VGRP_MAX_GATE.md`, aún no congelada. Cada cambio
lleva la etiqueta `[G-V-NN]` o `[CLAUDE.md]`.
Documento 2: el informe de la ronda 1 (objeciones G-V-01..17).
Documento 3: la lectura del autor de esa ronda, con la reparación propuesta para cada objeción.
Documentos 4–6: la nota de las tres velocidades, el contrato de la puerta Weyl/Dirac estándar y
su verificador exacto.

Comprueba, con alcance acotado:
1. Cada objeción G-V-01..17: ¿la resuelve la v3? Pon especial atención a G-V-05 (muestreo por
   componente conexa real), G-V-06 (A5 y testigo), G-V-10 y G-V-11 (regla de acuerdo B3 con
   tolerancia `1e-9` en los dos sentidos) y G-V-13 (reglas de precedencia de los veredictos).
2. Los añadidos nuevos: el criterio de abandono de la línea (Sec. 0), `STOPPED_PRIOR_ART`, la
   definición del conjunto `A` de H3 y T3 limitado a signos algebraicos. ¿Son decidibles y
   coherentes con el resto?
3. ¿Hay ahora alguna contradicción interna, o alguna frase que prometa más de lo que la carta
   puede certificar?

No reabras decisiones del usuario (masas, malla 256³, `n` simbólico fuera, flag
`--diagnostics`, revisor, rama, tolerancia `1e-9`) salvo que hagan la carta incoherente.

Salida: veredicto global; tabla G-V-01..17 con su estado; una sección por punto; objeciones
nuevas G-V-R2-NN con ubicación y gravedad (error demostrado, laguna o redacción). Una sola ronda:
declara tus supuestos.
---
