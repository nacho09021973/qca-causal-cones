# Lectura del autor — revisión Astra de la etapa 4b-1 del charter s=2

Fecha: 2026-10-29. Autor: Claude, autor del certificado y del informe. **No es una revisión
independiente.**

## Ejecución

- `COMPLETED`, de 13:29:32Z a 13:44:08Z.
- Bytes revisados: `38f462c`, certificado `5f91feae…`.
- Herramienta: `revision_ciega.sh` @ `a32e189`.
- Autorización: «mejor Astra» y «los autorizo ya».

## Veredicto del revisor

**Los resultados por clase se aceptan matemáticamente; el informe no se puede promocionar tal
como está redactado.**

- Las cuatro clases vacías y la existencia en `(V4, Pauli)` quedan respaldadas por pruebas
  independientes del revisor, que no dependen de Gröbner.
- No encuentra ninguna representación fiel omitida ni defectos en las dos parametrizaciones.
- Pide seis reparaciones: A-4B1-01..06.

## Contraste

**Prueba corta de vaciedad para `C4`, `D4` y `O`. Rehecha a mano: correcta.**
- Con `q* = (π/2, π/2, 0)` en unidades `ε`, `w(h) = e^{-iq*·h} = −h_x h_y` y `w(rh) = −w(h)` para
  el giro de 90°.
- La covarianza da `R U(q*) R† = −U(q*)`.
- `Ad(R)` sobre `M_2` tiene autovalores `1, 1, i, −i`, ninguno igual a `−1`. Por tanto
  `U(q*) = 0`, lo que contradice la unitariedad.
- No usa soporte activo, y vale para los tres grupos porque todos contienen un `C4` axial.

**Prueba para `T`.** Usa el determinante de Laurent, que debe ser una unidad. No la he rehecho
entera; queda como derivación del revisor `[UNVERIFIED]`. Coincide con el resultado de Gröbner.

**Testigo explícito en `(V4, Pauli)`.**
`U(q) = e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}`, con
`T_{(x,y,z)} = P_x^x P_y^y P_z^z` y ocho coeficientes no nulos. Es un punto real que no depende de
la extracción de Pavia en `S1`. Plausible; no lo he rehecho entero.

**Q-a (resultado nuevo del revisor, `[UNVERIFIED]` hasta certificarlo).** Astra prueba que todo
símbolo unitario con soporte activo de la clase `(V4, Pauli)` cumple la distinguibilidad.
- Si `T_{gh} = T_h` para un semigiro, el rango uno fuerza `T_h = λP`, `T_{−h} = μ(I − P)`.
- El desplazamiento `gh − h` tiene exactamente dos pares, que dan `T_h†T_h + T_{−h}†T_{−h} = 0`.

Eso daría `DISTINGUISHABILITY_IMPLIED_IN_CLASS`, y además para todos los símbolos unitarios, no
solo para los que tienen nodo. Según el charter, Q-a se decide en 4b-2 y con certificado. Aquí
queda registrado como anticipación.

## Reparaciones

| ID | Valoración del autor |
| --- | --- |
| **A-4B1-01** (dependencias no adjuntas de `S1`) | Se acepta como laguna de auditabilidad. Opciones: adjuntar `verify_irreducible_isotropy_step01.py`, ya revisado, en la próxima revisión, o sustituir el punto de Pavia por el testigo explícito de Astra con su unitariedad comprobada en el propio certificado. |
| **A-4B1-02** (para `V4` no se calcula Gröbner en la segunda construcción) | **Se acepta: error demostrado del informe.** El código solo compara el número de parámetros en esa rama. |
| **A-4B1-03** (las construcciones comparten infraestructura) | Se acepta. Hay que describirlas como dos construcciones con infraestructura compartida. |
| **A-4B1-04** (identificación con P17) | Se acepta. Hay que nombrar la clase congelada sin equipararla con «P17 menos la Eq. (2)». |
| **A-4B1-05** (`..._ABOVE` sin objeto) | Se acepta. Solo vale para la clase `C4`; en la clase superviviente sigue pendiente el transporte de nodos. |
| **A-4B1-06** (DEP19 (14)) | **Se acepta: error demostrado del informe.** Comprobado en el texto extraído de DEP19 (línea ~270): (14) es `Σ_h A_h = I_s`, una normalización. El contraejemplo de Astra (`α_i = 1/2`, `θ = 0`, `V = I`) lo confirma. |

## Conclusión del autor

- Las conclusiones de 4b-1 se sostienen: cuatro clases vacías y `(V4, Pauli)` no vacía.
- Las seis reparaciones son de descripción, de alcance y de auditabilidad. Dos son errores del
  informe (02 y 06).
- No se ha aplicado nada. Aplicar reparaciones, promocionar o abrir 4a o 4b-2 lo decide el
  usuario.
