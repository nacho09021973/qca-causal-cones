# Revisión ciega de Claude: estado y reparaciones pendientes

2026-11-06. Usuario autorizó «adelante que la haga claude».
Lanzador canónico revision-ciega opus, herramientas ce09890.
Claude Opus 5.5, esfuerzo high, sesión sellada sin herramientas.
Autor revisado: Codex. Otra familia de modelos; revisión de agente,
no humana. Una ronda completa; no re-revisión autorizada implícitamente.

Informe íntegro sin editar:
../debates/2026-11-06--interacting-chain-review-opus/informe_opus.md.
Entrada SHA256 163969e76c07db60170ad37c5dfd3d57f419907c95650476d86f6077c918712c.
Estado operativo COMPLETED, salida 0; no equivale a PASS científico.
Snapshot de documentos sin commit identificado por hashes del lanzador.

## Veredictos de la ronda

| Bloque | Claude |
|---|---|
| Colisión de densidades | PASS |
| Segundo orden y memoria | REPAIR_REQUIRED |
| Circuito Wilson/Strang | PASS |
| Flujo Yukawa | PASS para el sistema ODE congelado |
| Ajuste crítico y corte | REPAIR_REQUIRED |
| Cadena global | REPAIR_REQUIRED |

No FAIL. El revisor declara no haber ejecutado código ni verificado
los valores numéricos o preregistros fuera de la evidencia adjunta.
No revisó el constructor s=4 original porque no fue adjuntado: queda
una limitación concreta del paquete, no una objeción demostrada al modelo.

## Tratamiento del autor

Se corrigen ahora dos sobreafirmaciones documentales señaladas por Claude:
la cota del circuito a L,M fijos no es una cota de convergencia del corte,
y el flujo resuelto es un ODE a un lazo linealizado con acoplamientos
de referencia iguales, no un flujo no lineal completo. No promoción.

Todas las demás objeciones permanecen ABIERTAS para reparación o
comprobación. No se presentan como resueltas por recibir el informe:

1. Escribir y comprobar la separación Hartree exacta antes de suprimir Q.
2. Fijar transformada temporal, factor z y orden matricial de Dyson.
3. Incluir derivada en frecuencia en los criterios para pendientes.
4. Cota de cola mejorable por factor dos: informativa, no error de la cota.
5. Adjuntar constructor y verificar convención Fourier/signo de pendiente.
6. Explicitar limitación del gap perturbativo: informativa.
7. Verificar la simetría partícula-hueco propuesta por el revisor.
8. Contrastar y citar AD Ec.(48) para dos sabores.
9. Corregir terminología de modos «relevantes» a modos de atracción.
10. Mantener alcance y1=y2 o derivar flujo de acoplamientos desiguales.
11. Verificar y registrar la escala cuantitativa del efecto de atracción.
12. Reducir precisión mostrada de cuadraturas no certificadas.
13. Verificar cúbico generado y completar tabla de operadores/simetrías,
    incluidos operadores marginales del circuito a paso fijo.
14. Explicitar error de norma traza O(L^-1/2), distinto de probabilidad
    de cola O(L^-1), y separar error de Trotter del error de corte.
15–16. Sobreafirmaciones canónicas corregidas; no re-revisadas.
17. Fijar criterio de abandono físico de la línea, distinto de una mera
    restricción sobre qué se puede afirmar, antes de otro cálculo.
18. Discontinuidad entre arquitecturas: mantenerla explícita, informativa.
19. Revisión sin ejecución/preregistro comprobable: limitación informativa.

Las derivaciones D7, D10 y la beta de acoplamientos desiguales sugerida
por Claude NO son fuentes ni resultados comprobados del proyecto.
También requiere comprobación su estimación de escalas y su interpretación
de detectabilidad. No se afirma que ninguna simulación finita pueda
detectar el efecto bajo cualquier precisión o cualquier parámetro.

El informe rederiva los exponentes lentos 1/21 y 13/21 y pide cuantificar
su magnitud antes de una propuesta numérica. La siguiente tarea útil es
resolver las objeciones, no ampliar el barrido o interpretar el ODE como
prueba del circuito. La condición para fusionar con main sigue incumplida.

Artefactos conservados: prompt, lista de documentos, hashes, entrada,
respuesta original JSON, informe y estado operativo, en la carpeta del
encargo. No se modifica el informe sellado. git diff --check.
