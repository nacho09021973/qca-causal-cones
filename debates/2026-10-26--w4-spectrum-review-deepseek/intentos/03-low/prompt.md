# Encargo W4: espectro completo y observable

Estado operativo: PREPARED_NOT_SENT. Revisor previsto: DeepSeek, familia
distinta del autor Codex. Una ronda; no hay permiso de envío en este encargo.
Sólo se envía el texto delimitado entre las dos líneas siguientes, más los
seis documentos enumerados en preparar.sh.

---
Audita desde las puertas microscópicas las afirmaciones de la auditoría W4
adjunta. No supongas que la interpretación corregida es cierta. No has
ejecutado código ni visto el resto del repositorio: el script es un argumento
que debes inspeccionar, no evidencia de una ejecución propia.

Objetivo: decidir si están justificadas las correcciones sobre fase respecto
al vacío, ramas de cuasienergía, unidades de velocidad y expectativa Z, en la
reducción 1D de un defecto. El contrato histórico también se adjunta para
comprobar que no se cambia silenciosamente el modelo. No abras una línea
3D/tensorial, no propongas rescates y no atribuyas novedad.

Comprobaciones requeridas:
1. Deriva la restricción de K(kappa)=exp[-i kappa(I-SWAP)] sin descartar
   fases, la invariancia del vacío y el producto de los dos matchings.
   Contrasta el símbolo con el circuito real de bits del segundo script.
2. Deriva los autovalores, fija la convención lambda=exp(-i epsilon) y
   distingue fase de sector, fase global, cruce entre bandas y frecuencia
   cero relativa al vacío. Determina qué observables ven esa fase.
3. Rehaz la expansión de la rama uniforme del mismo signo, comprueba signo,
   coeficiente, dominio y resto, y prueba los extremos 0, pi/2 y pi. Revisa
   si el calificativo cuadrático confunde no degeneración con gap espectral.
4. Rehaz la rama del control de signos opuestos y el cruce en k=pi del caso
   original. Comprueba los valores absolutos, la rama de arcsin y la necesidad
   de sin(kappa) distinto de cero para propagación lineal.
5. Restaura espaciado a y período tau: identifica el momento por celda y
   por registro. Comprueba el factor dos con el desplazamiento SWAP exacto,
   sin equiparar pendiente IR, velocidad máxima de grupo y soporte causal.
6. Deriva <Z_n> desde el operador en vacío más un defecto. Audita el ejemplo
   estacionario con k=pi y densidad uniforme, la respuesta de orden epsilon²
   al mezclar vacío y defecto, y los dos estados con igual Z inicial pero
   distinta Z posterior. Comprueba qué conclusiones generales permiten y
   cuáles NO: no conviertas una limitación de esta derivación en un no-go
   universal para ondas del métrico.
7. Examina las verificaciones permanentes: circularidad, omisiones, signos,
   convenciones, dependencia del mismo helper y cobertura finita frente al
   argumento general. Separar una segunda formulación del autor de una
   revisión independiente. No atribuyas al script lo que sólo prueba el texto.

Resultado esperado: informe autocontenido, con veredicto
ACCEPT / ACCEPT_WITH_REPAIRS / REJECT / INCONCLUSIVE y una tabla por cada
punto: resultado, derivación comprobada, objeción y reparación mínima.
Toda objeción llevará identificador W4-R1-NN, gravedad y referencia concreta
al documento o función; si señalas un error, proporciona cálculo o
contraejemplo. No hagas recomendaciones generales sin relación con W4.

Máximo: una ronda de revisión sobre estos bytes. Cierre: informe completo y
lista finita de objeciones, o declaración de insuficiencia. No inicies otra
ronda ni supongas autorización para ejecutar herramientas. Tu aceptación
no promueve por sí sola evidencia ni reabre W1–W12: las objeciones se
contrastarán localmente antes de registrar una decisión científica.
---

Procedencia: preparado por Codex el 2026-10-26. El manifiesto SHA256 identifica
el texto y los seis adjuntos. El modo de preparación no consulta al proveedor.
