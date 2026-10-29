# Revisión ciega — borrador v1 del charter de rigidez isótropa s=3

Bytes revisados: commit `5fe04ae`.
Fecha: 2026-10-29. Autorización del usuario: «D1 ambos rangos, D2 mantener F, D3 Grok, commit».
Objetivo: revisión de otra familia del borrador antes de congelarlo como preregistro.
Resultado esperado: READY / READY_WITH_REPAIRS / NOT_READY, con reparaciones obligatorias
numeradas G-S3-NN, y un veredicto sobre cada anticipación B1–B7 (correcta / incorrecta /
incompleta), con el cálculo o el contraejemplo.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). Todo lo revisado lo escribió Claude.
Cierre: informe y lectura del autor en `verificacion_autor.md`. Congelar lo decide el usuario.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH.

---
Responde en español. Eres un revisor independiente de física matemática (QCA en red,
representaciones proyectivas de grupos finitos, símbolos de Laurent unitarios, cuerpos causales).
Solo tienes los documentos adjuntos; no tienes herramientas y no puedes ejecutar código. No
supongas que nada es correcto.

Documento 1: el borrador del charter s=3. Documento 2: el charter s=2 del que hereda casi todo.
Documento 3: el informe de la etapa (a) de s=2, con la enumeración geométrica que el borrador
reutiliza. Documento 4: el charter de la cota general `c_0 <= c_strict^iso`. Documento 5: el
charter predecesor con las definiciones (`S_n`, `h_infty`, `c_strict^iso`, `rho_micro`, lema del
vértice). Documento 6: el charter de isotropía irreducible (clases T3 y O3, ya vacías).

Comprueba:
1. Pregunta y cuantificadores: ¿están bien fijados? ¿Es correcta y suficiente la definición del
   sector de rango 2 y de rango 3, incluida la rama plana? ¿Es coherente con la cota general?
2. Anticipaciones B1–B7, una por una. En particular B1 (multiplicadores de Schur de los
   subgrupos de `O` y el argumento del determinante), B2 (cota de rangos), B4 (no hay símbolos
   diagonales por bloques) y B5 (determinante constante).
3. ¿Es legítimo reutilizar sin rehacerla la enumeración geométrica de s=2? ¿Hay algo en ella que
   dependa de `s`?
4. Clases: ¿falta alguna representación de dimensión 3, o alguna identificación de clases bajo
   conjugación que haya que fijar antes de calcular?
5. Secuencia, paradas y resultados: ¿pueden coexistir? ¿Hay resultados sin pregunta o preguntas
   sin resultado? ¿Es correcto que no haya Q-b?
6. Alcance: ¿alguna frase promete más de lo que el charter puede decidir?

Salida: veredicto global; tabla B1–B7; una sección por punto; reparaciones obligatorias G-S3-NN
con ubicación y gravedad (error demostrado, laguna o redacción). Una sola ronda: declara tus
supuestos.
---
