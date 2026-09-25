# C2a — transferencia oscilatoria discreto a Weyl

Fecha: 2026-09-22. Autorización: instrucción del usuario de atacar una sola
afirmación matemática, el error de transferencia dentro del funcional
completo de Bob, sin nuevo barrido ni extensión AdS.
Antecedente: [contrato C1/C2/C3](IR_ATTRIBUTION_C1_C2_C3_GATE.md) y
[representación exacta C2](../reports/2026-09-22--c2-projected-response-representation.md).
Este contrato registra los criterios antes de escribir el nuevo desarrollo;
no modifica los contratos ni las pruebas anteriores.

## Objetos fijos

M=sigma2, M_B=I, el símbolo CJWW (5.15), dimensión interna dos, nodo cero,
recurso y perfiles regionales originales, P=1_{|p|<=N^{-1/2}}, N entero.
K=sqrt(N), variables escaladas Y=y/N, u=(1,1,1), b=1/4.
No suavizar el corte, variar el perfil ni sustituir la red.

La referencia se define sin ambigüedad por

`Lpp_W(N)=integral h(Y)[2 Re R0(Y)^dagger D_K^W(Y)+|D_K^W(Y)|^2] dY`,

donde R0 es el recurso Weyl libre y D_K^W la integral Weyl proyectada de
la sección 4 del informe C2. El objeto discreto Lpp conserva la suma de
red, el recurso R_N, el símbolo exacto y todas las imágenes de Poisson.

## Criterio de cierre

Primero determinar el líder de Lpp_W, con signo/no anulación y resto
controlado. Después demostrar

`Lpp(N)-Lpp_W(N)=o(A_N)`

para su escala líder A_N, incluyendo los términos lineal y cuadrático,
el cambio R_N a R0 y los errores de muestreo y de imágenes.
Si el coeficiente es oscilatorio, demostrar una cota inferior uniforme o
explicitar subsecuencias y ceros: una envolvente no sustituye el líder.

Se permiten particiones auxiliares de demostración en interior, puntos
estacionarios cuando existan, frontera móvil y aliases, pero no cambiar
el observable. Se deben calcular los términos de borde relevantes.
No es requisito una buena aproximación uniforme del campo: pueden usarse
normas para acotar errores, pero no para atribuir la respuesta a un sector.

## Resultados y evidencia

- `TRANSFER_PROOF_WRITTEN / REVIEW_PENDING`: derivación completa con
  separación de escalas, todavía no revisada independientemente.
- `PASS`: transferencia y líder aceptados después de revisión independiente.
- `FAIL_TO_CLOSE`: no se logra separación; identificar la estimación que
  falla. No equivale a refutar la transferencia.
- `TRANSFER_REFUTED`: un término demostrado contradice la condición.

Ni una cota superior demasiado grande ni un intento fallido se convierte
en prueba de que el error real es grande. La cancelación entre bloques,
si se obtiene, usa `R=L-Lpp`; R incluye PQ, QP y QQ, no sólo QQ.
No identificar una parte exponencial subdominante dentro de cada bloque
si el resto de la expansión sigue siendo algebraico.

## Límites

C1 conserva su PASS; C3 sigue separado; E/AdS queda congelado.
Sin barridos, código científico nuevo, publicación, commit/push ni cambios
del estado canónico. Ninguna conclusión será una señal local del
protocolo condicionado ni una afirmación bibliográfica de novedad.
