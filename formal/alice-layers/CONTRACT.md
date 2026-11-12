# Preparación Lean de Alice / Layers(b)

Autorización: «adelante» tras proponer descomponer Layers(b), fijar su enunciado
e identificar lemas demostrables y obligaciones pendientes. No se autoriza
promoción científica, nuevas llamadas a proveedores ni escritura en QCA.

Fuente congelada: ../runs/run_0/paper.tex, SHA-256
2075e8402142451b6dc0182f3c923608f11cd8839dcd11061ca844d87fc04cc4.
El experimento transversal es un diagnóstico de esa afirmación, no su prueba.

Alcance: componente escalar de Alice, red Z^3 y perfiles del paper. Se escriben
definiciones exactas y una proposición para la afirmación asintótica. No se asume
esa proposición como axioma ni se presenta como demostrada al compilarla.
No se formalizan Bob, el espinor completo, el paseo completo o todo el paper.

Objetivos iniciales comprobables: fase de frecuencia transversal, desigualdad
triangular de una suma finita, identidad algebraica del perfil por capas e
identidad del prefactor. Son ingredientes; ninguno sustituye el control de
error, la fórmula de Poisson bidimensional o su sumabilidad uniforme.
Las comprobaciones de fidelidad de las definiciones incluyen demostrar que la
caja finita cubre toda la esfera y que el marco normal/transversal preserva la
norma euclídea. El comparador cubrirá la lista completa de ingredientes probados.

Entorno: Lean 4.31.0 y Mathlib fabf563a7c95a166b8d7b6efca11c8b4dc9d911f,
ya disponibles en el cache local de QCA. Sólo se leen archivos de ese proyecto;
objetos compilados y logs se escriben aquí. No se usa lake dentro de QCA ni se
descargan paquetes. El compilador se invoca por un generador permanente.

El t_* matemático se define mediante su fórmula cerrada. El decimal
0.7357528144 se identifica aparte, sin afirmar que sea exactamente el mismo
real. Las integrales y tsum se definen, pero su buena definición analítica
requiere obligaciones explícitas de integrabilidad y sumabilidad.

El éxito de esta preparación es un inventario honesto y verificable: qué
enunciados compilan, cuáles tienen prueba y cuáles siguen abiertos. Un fallo
de Lean se conserva y se corrige; no se sustituye por sorry ni por axiomas propios.
