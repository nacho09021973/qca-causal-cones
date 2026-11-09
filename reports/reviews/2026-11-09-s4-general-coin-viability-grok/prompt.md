# Revisión externa: moneda general U(4) y pendiente isotrópica en s=4

Autorización: usuario «que Grok revise también los s4» (2026-11-09). Autor
del texto: Codex (OpenAI); revisor: Grok (xAI), otra familia, mediante
revision-ciega grok del PATH. Herramientas: ~/herramientas commit 97292a9.
Resultado revisado: commit 170910b (contrato SHA256 a817034f…, script
6565ddc1…, coincidentes con los registrados en el informe).
Máximo: una ronda sustantiva. No se autoriza investigación nueva ni promoción.
Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la afirmación adjunta: para U(k)=W prod_i
exp(-i k_i G_i/sqrt3), G_i=sigma_i tensor tau_i, y cualquier W en U(4), todo
doblete nodal aislado de rango dos en k=0 con cono lineal isotrópico no
degenerado y sin inclinación tiene c=1/3. Tu objetivo es encontrar un error,
un supuesto oculto o un hueco real, o explicar por qué se sostiene. No
aceptes el recuento 55/55 como prueba del enunciado universal.

Comprueba desde las definiciones:
(1) que los G_i conmutan, son involuciones, G_xG_yG_z=-I y que los cuatro E_h
    (h_xh_yh_z=-1) son proyectores de rango uno que suman I, con
    sum_h h_i E_h=G_i;
(2) que las pendientes nodales de primer orden del doblete son exactamente
    las de H_i=T^dagger G_i T/sqrt3 (papel de la separación espectral, de z y
    de que iW^dagger d_iU(0)=G_i/sqrt3), sin término adicional de W;
(3) la fórmula B_h=[I+sqrt3 sum_i h_i H_i]/4, la definición de "sin
    inclinación" (tr H_i=0) y de isotropía (M=c^2 I), y la identidad
    det B_h=[1-3h^T M h]/16;
(4) que rango B_h<=1 fuerza det B_h=0 y por tanto c=1/3; y la segunda vía por
    suma de trazas cuadráticas;
(5) si las hipótesis (doblete exactamente de rango dos, separación, cono no
    degenerado) se usan todas y bastan; casos límite que escapen;
(6) correspondencia del script con lo que el informe dice que comprueba;
(7) si el alcance declarado (solo k=0, este desplazamiento, sin conos
    inclinados ni otros rangos) es correcto o se excede.

Se adjuntan contrato, informe, script y registro de ejecución. No tienes
acceso al repositorio ni puedes ejecutar código. Distingue lo que derivas a
mano de lo que solo inspeccionas.

Entrega en español: veredicto (se sostiene / reparación necesaria /
refutado / no decidido), derivaciones críticas, objeciones ordenadas por
gravedad con sección y reparación concreta, y el alcance exacto que
aceptarías. Si no hay fallos, dilo sin inventar objeciones. Ninguna
propuesta de protocolo o búsqueda adicional es necesaria.
---
