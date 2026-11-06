# Revisión ciega, ronda 3 (acotada) — borrador v4 de la carta DIRAC_VGRP_MAX

Bytes revisados: commit `ef4c9f5` de la rama `theory/massive-vgrp-bcc` (base `main` `bce5599`).
Fecha: 2026-11-06. Autorización del usuario: «si» a escribir la v4, fijar la tolerancia espacial
`1e-6` y hacer una tercera ronda acotada con Grok antes de congelar.
Objetivo: comprobar que la v4 resuelve G-V-R2-01..11 y los dos parciales de la ronda 1 (G-V-05,
G-V-11) sin introducir errores nuevos, y decidir si puede congelarse como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY; por cada objeción de la ronda 2 y por
G-V-05 y G-V-11: RESUELTA / PARCIAL / NO RESUELTA; objeciones nuevas G-V-R3-NN, solo si las
introduce la v4 o si cambian un veredicto.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude, salvo el contrato y el verificador Weyl/Dirac.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Herramienta: revision-ciega del PATH, `~/herramientas` `ce09890`.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red, símbolos de
Laurent unitarios, dispersión de sectores con masa, geometría algebraica real efectiva). Solo
tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar código. No supongas
que nada es correcto.

Documento 1: el borrador v4 de la carta `DIRAC_VGRP_MAX_GATE.md`, aún no congelada. Los cambios
de esta versión llevan la etiqueta `[G-V-R2-NN]`.
Documento 2: el informe de la ronda 2 (objeciones G-V-R2-01..11).
Documento 3: la lectura del autor de la ronda 2, con la reparación propuesta para cada objeción.
Documentos 4–6: la nota de las tres velocidades, el contrato de la puerta Weyl/Dirac estándar y
su verificador exacto.

Comprueba, con alcance acotado:
1. Cada objeción G-V-R2-01..11, y los parciales G-V-05 y G-V-11: ¿los resuelve la v4? Atención
   especial a:
   - el orden único A3 → A5 → OPEN;
   - la separación entre `VGRP_MAX_VALUE_CERTIFIED` y `MAXIMIZER_SET_CERTIFIED`, y la regla de
     H3;
   - el certificado de muestreo sobre el modelo compacto `(s_i, c_i)`;
   - la regla unilateral de B3 para `CEILING_ONLY` y la suspensión por veto;
   - el predicado de `STOPPED_PRIOR_ART`.
2. ¿Hay ahora alguna contradicción interna, o alguna frase que prometa más de lo que la carta
   puede certificar?

No reabras decisiones del usuario (masas, malla 256³, `n` simbólico fuera, flag `--diagnostics`,
revisor, rama, tolerancias `1e-9` y `1e-6`) salvo que hagan la carta incoherente. No reabras
objeciones de rondas anteriores que diste por resueltas, salvo que la v4 las haya roto.

Salida: veredicto global; tabla de estado; una sección por punto; objeciones nuevas G-V-R3-NN con
ubicación y gravedad (error demostrado, laguna o redacción). Una sola ronda: declara tus
supuestos.
---
