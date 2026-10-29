# Revisión ciega — etapa (a) del charter de rigidez mínima s=2 (Pasos 0′ y 0)

Fecha: 2026-10-29. Autorización directa del usuario: «commit y push y que revise Gok» (Grok).
Objetivo: hacer la revisión de otra familia que exige la Sec. 6 del charter. Se revisa la
enumeración del Paso 0′ (exhaustividad y convenciones) antes de que la usen las etapas
posteriores, y los cierres del Paso 0. Bytes revisados: commit `dc4a6f7`. Certificado
`d6bf4189…`, informe `f10fcfb3…`.
Resultado esperado: un veredicto por punto y global (ACCEPT / ACCEPT_WITH_REPAIRS / REJECT), con
reparaciones obligatorias numeradas G-S0-NN.
Máximo: una ronda sellada; un reintento operativo si falla el transporte. Revisor: grok (familia
xAI). El charter, el certificado y el informe los escribió Claude.
Cierre: informe y lectura crítica del autor en `verificacion_autor.md`. No promociona nada ni
autoriza las etapas 4a o 4b.
Documentos: `docs.txt`, con sha256 en `inputs.sha256`.
Herramienta: revision-ciega del PATH; ~/herramientas `a32e189`.

---
Responde en español. Eres un revisor independiente de física matemática (grupos finitos y sus
representaciones proyectivas, QCA en red). Solo tienes los documentos adjuntos; no tienes
herramientas y no puedes ejecutar código. El script es un argumento que inspeccionas, no una
ejecución tuya. No supongas que nada es correcto.

Documento 1: el charter congelado. Documento 2: el informe de la etapa (a). Documento 3: el
certificado. Documento 4: utilidades simbólicas.

Comprueba:
1. Exhaustividad del Paso 0′.
   - ¿Basta cerrar todos los pares de elementos para obtener los 30 subgrupos de `O ≅ S4`?
   - ¿Es correcta la enumeración de los 16 `S_+` y de los pares transitivos de la familia P,
     `(V4, tetraedro)`, `(T, tetraedro)` y `(C4, cara)`, salvo conjugación?
   - ¿Es correcta la familia F, `{D4, O}`?
   - Comprueba en el código que la identificación salvo conjugación es correcta.
2. Representaciones.
   - ¿Es correcto identificar las representaciones proyectivas de dimensión 2, salvo
     equivalencia proyectiva, con homomorfismos `G → PU(2) ≅ SO(3)` salvo conjugación?
   - ¿Es exhaustivo enumerar homomorfismos hacia `O` y clasificarlos por el carácter
     tridimensional? El argumento es que todos los tipos de imagen son conjugados a subgrupos de
     `O`, y que caracteres iguales dan conjugación en `SO(3)`.
   - ¿Son correctos los recuentos 5, 3, 3, 6 y 4?
   - ¿Es correcto el criterio «reducible ⇔ multiplicidad trivial ≥ 1»?
3. Lema del núcleo.
   - ¿Es correcto el argumento? Si `R` es escalar en `ker ρ`, `T` es constante en las órbitas.
     Un desplazamiento con todos sus pares dentro de órbitas da una suma de términos
     semidefinidos positivos igual a cero, y eso contradice `T_h ≠ 0`.
   - ¿La función `emptying_shift` lo implementa fielmente?
   - Comprueba a mano al menos dos certificados impresos en el informe.
4. A3 y A8: el par único de los desplazamientos `(2,2,2)` y `2h`, el rango uno y
   Cayley–Hamilton.
5. Controles. ¿Es informativo el control negativo (la clase de Pauli no se vacía)? ¿Y el
   positivo (los símbolos de Pavia)?
6. Alcance. ¿Hay alguna afirmación del informe que exceda lo certificado? Fíjate en especial en
   la dependencia de la clasificación estándar de subgrupos finitos de `SO(3)` y en la lectura de
   los controles `T2s`/`O2s` del certificado anterior como simples anticipaciones.

Salida: una sección por punto, con su veredicto; un veredicto global; reparaciones obligatorias
G-S0-NN con ubicación y gravedad (error demostrado, laguna o redacción). Si señalas un error, da el
cálculo o el contraejemplo. Una sola ronda: declara tus supuestos en vez de preguntar.
---
