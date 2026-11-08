# Dos contactos consecutivos: prueba exacta y certificado Lean

2026-11-08. Autor Codex. Usuario «y puedes hacerlo solo o con lean?» referido
al siguiente paso de composición. Se ejecuta la derivación y un certificado
Lean de alcance explícito. No se envía texto a terceros.

Sabido: 3dbf099 obtiene para M=1 una puerta exacta D_chi tras un paso,
en el código de salida F B. Se comprobó Gamma y su representación de
dos posiciones en el sector Q=0. Fuente local: sources/README.md leído;
biblioteca/ no existe. Fuentes primarias: 1711.03920v1.pdf pp.1–2;
1804.08508v1.pdf pp.3,5–6.

Pregunta: ¿la segunda aplicación consecutiva de U=FJ conserva F²B,
y coincide con una composición de puertas unitarias sin fuga?

Contrato: M=1, mismo B=B_+ wedge B_-, misma regla constante mu=3/5,
nu=4/5,chi=pi/2, sin controles intermedios ni ancillas. Comparación tras
dos pasos con F²B; no redefine el código con U. Derivación conserva
mu²+nu²=1 y chi; los extremos mu=0,nu=0 y chi=0 son controles algebraicos,
no búsqueda de nuevas reglas. Termina si fuga positiva cierra esta
composición; no se extrapola a tiempos mayores o geometrías con auxiliares.

Antes de este archivo ya se anunció una derivación manual preliminar
p_max=2mu²nu²(1-cos chi). Este contrato es anterior a los verificadores y
certificados, no una preregistración anterior a esa derivación manual.

Verificación: conteo exacto gaussiano/racional del propagador de dos pasos;
contraste con amplitudes fermiónicas completas; matriz K2 y su defecto de
Gram, testigo de fuga y caso libre. Lean, sin Mathlib ni nuevas dependencias,
comprobará la representación finita exacta a parámetros racionales/chi=pi/2,
no un teorema de todos los QCA ni universalidad. Se conservarán enunciados
legibles separados de soluciones, axiom checks y controles negativos.

La identificación entre el modelo reducido y Fock es una derivación
matemática escrita, contrastada por implementación completa. No se presentará
como formalizada por Lean si el certificado solo cubre matrices reducidas.
Los números, códigos, enunciados, logs y resultados se conservarán.
Lean instalado: v4.31.0; el proyecto formal previo requiere Mathlib sin
cache local del proyecto, así que el certificado se aloja en subproyecto
autónomo sin dependencias dentro de formal/. Herramientas leídas ce09890;
no se copian herramientas compartidas ni se convocan agentes.
