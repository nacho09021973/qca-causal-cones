# Revisión externa: realización s=4 con simetría cíclica

Autorización: usuario «que Grok revise también los s4» (2026-11-09). Autor
del texto: Codex (OpenAI); revisor: Grok (xAI), otra familia, mediante
revision-ciega grok del PATH. Herramientas: ~/herramientas commit 97292a9.
Resultado revisado: commit 170910b (contrato SHA256 c065cb8c…, script
9a139072…, coincidentes con los registrados en el informe).
Máximo: una ronda sustantiva. No se autoriza investigación nueva ni promoción.
Cierra el encargo: un informe completo de esta ronda.

---
Revisa adversarialmente la realización adjunta: U(k)=W prod_i
exp(-i k_i G_i/sqrt3), G_i=sigma_i tensor tau_i,
W=I tensor exp(-i pi (n.tau)/4), n=(1,1,1)/sqrt3, con veredicto
REALIZED_WITH_ACTUAL_SUPPORT: unitaria de alcance finito, conmutante común
escalar, D2 (R_j=sigma_j tensor I), C=VK con V=sigma_y tensor tau_y,
covariancia cíclica S=t tensor t, dos dobletes nodales en k=0 con fases
±pi/4 y pendientes lineales isotrópicas cP=cQ=1/3, soporte real tetraédrico
(cuatro de los ocho coeficientes permitidos se anulan). Tu objetivo es
encontrar un error, un supuesto oculto o un hueco real, o explicar por qué
se sostiene. No aceptes el recuento 143/143 como prueba.

Comprueba desde las definiciones:
(1) que W definido en el contrato coincide con (I-iN)/sqrt2 del informe, y
    la descomposición U(k)=sum_h W E_h exp(-ik.h/sqrt3) con soporte F;
    unitariedad;
(2) cada simetría: R_j y su acción sobre k; la condición antiunitaria
    V U(k)* V^dagger=U(-k) y si corresponde a la convención declarada de C;
    t cicla las Pauli, S conserva W y cicla G_i, y la dirección del giro
    S U(kx,ky,kz)S^dagger=U(kz,kx,ky);
(3) nodos: WP=e^{-i pi/4}P, WQ=e^{i pi/4}Q, rango dos, compresiones
    P J_i P=(sigma_i tensor I)P/3 y Q J_i Q=-(sigma_i tensor I)Q/3, y que de
    ahí salen conos no degenerados con c=1/3; la segunda vía axial;
(4) el argumento de irreducibilidad (conmutante común escalar);
(5) la geometría: conv(F) tetraedro regular, r_in=1/3, y que la coincidencia
    c=r_in se presenta solo como propia de esta realización;
(6) el argumento local de protección de la sección 6 (D2 fuerza W'=I tensor
    w', S fuerza eje n, igualdad de los v_i.n): huecos o supuestos;
(7) correspondencia del script con el informe;
(8) si el alcance declarado (variante de ocho saltos OPEN, sin cuerpo
    estricto asintótico, sin selección ni valor físico de c, no
    pertenencia a la clase de 1708.00826) es correcto o se excede.

Se adjuntan contrato, informe, script y registro de ejecución. No tienes
acceso al repositorio ni puedes ejecutar código. Distingue lo que derivas a
mano de lo que solo inspeccionas. No afirmes haber leído PDFs no adjuntados.

Entrega en español: veredicto (se sostiene / reparación necesaria /
refutado / no decidido), derivaciones críticas, objeciones ordenadas por
gravedad con sección y reparación concreta, y el alcance exacto que
aceptarías. Si no hay fallos, dilo sin inventar objeciones. Ninguna
propuesta de protocolo o búsqueda adicional es necesaria.
---
