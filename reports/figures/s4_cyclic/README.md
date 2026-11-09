# Visualización del walk s=4

Generada el 2026-11-06 por `scripts/plot_s4_cyclic_realization.py`.
Ilustración numérica del constructor fijo de
`reports/2026-11-06--s4-cyclic-realization.md`, sin promoción científica.

Reproducir desde la raíz:

```bash
PYTHONNOUSERSITE=1 python3 -B scripts/plot_s4_cyclic_realization.py
```

La ejecución sin esa variable falló por mezcla entre Matplotlib de usuario
y el módulo mplot3d del sistema. No se modificó ninguna instalación.
La ejecución registrada usa NumPy 1.26.4 y Matplotlib 3.6.3.

Salidas: `s4_cyclic.png`, `s4_cyclic.pdf`, `sampled_bands.npz` y
`provenance.json` (versiones, hash del script, base Git y diagnósticos).
El script y sus salidas son artefactos de trabajo, aún sin commit.

## Lectura de los paneles

- A: cuatro saltos reales forman un tetraedro; las cruces grises son los
  otros cuatro coeficientes, nulos. No es una densidad de probabilidad.
- B: corte kz=0 de las dos bandas que se tocan en omega=+pi/4.
  Se resta la fase nodal para mostrar el cruce. La altura es cuasienergía,
  no tiempo ni posición. No representa un paquete propagándose.
- C: las cuatro bandas sobre el eje kx y sus aproximaciones locales.
  Hay dos cruces, en ±pi/4, con igual pendiente en magnitud en el origen.
- D: semiseparación del par positivo dividida por |k|, en tres direcciones.
  Tiende a 1/3 al acercarse al origen y depende de la dirección a distancia
  finita. Esta razón no es una velocidad de grupo, que requiere derivar
  la cuasienergía; tampoco determina el frente causal asintótico.

Se diagonaliza el U(k) completo en cada punto, sin ajustar conos. La
ordenación por cuasienergía solo se usa en ventanas donde los dos pares
permanecen separados y no cruzan el corte de fase. Son secciones locales,
no una representación de toda la zona de Brillouin ni un censo de nodos.

## Diagnósticos de la ejecución

Error máximo de unitariedad y discrepancia con las eigenfases axiales
analíticas: ambos 7.78e-16. En |k|=1e-5, la semiseparación/|k| vale
aproximadamente 0.33333333334, 0.33333333334 y 0.33333222222 para
(100), (110) y (111), respectivamente. Estos controles son numéricos;
la comprobación exacta está en el verificador de la realización.

En |k|=0.8, esas razones son aproximadamente 0.30291, 0.33421 y 0.25163.
La diferencia ilustra correcciones más allá del término lineal, no un
fallo de la igualdad de velocidades locales. No se infiere una ley general
de estas tres secciones. PNG inspeccionado visualmente; sin revisión externa.
