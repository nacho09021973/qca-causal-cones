# Diseño inverso de un QCA para gravedad emergente

Fecha: 2026-10-08. Rama: `research/inverse-gravity-design`.
Base: `0a4606c61a3f75e5516a245f3837ed009b0a56b4`.
Estado inicial: `CHARTER_OPEN / REQUIREMENTS_DEFINED / NO_RULE_SPECIFIED`.

## 0. Autorización y motivo independiente

Instrucción directa del usuario: «si, creamos una rama independiente con el
nombre que consideres y empezamos esta linea de investigacion», después de
proponer deducir requisitos microscópicos desde un objetivo gravitatorio IR.

Motivo: investigar qué mecanismo colectivo podría generar geometría dinámica,
universalidad del cono y dinámica tensorial relativista en un QCA. El objeto
es el par **regla microscópica + estado/sector colectivo**. El objetivo no es
ajustar los controles W6/CJWW tras el negativo de W12. No se exige recuperar
exactamente CJWW: la materia de esta línea podrá ser distinta y se deberá
especificar antes de cualquier cálculo. Los cierres anteriores se conservan.

La autorización cubre formulación, contraste primario, descarte conceptual y
construcción local dentro de este charter. No autoriza envíos a terceros,
publicación, promoción científica automática ni cambios retroactivos de gates.

## 1. Objetivo y distinciones

Objetivo final elegido: régimen efectivo de gravedad de Einstein en 3+1
dimensiones, acoplado a materia, con errores controlados. Es un objetivo de
investigación, no una propiedad que se suponga del QCA.

Primer objetivo: determinar si se puede especificar una arquitectura local
unitaria con sector tensorial físico de dos polarizaciones, dispersión lineal
y un mecanismo de cono común con al menos dos sectores de materia distintos.

Los tres últimos requisitos son parte del objetivo adoptado; esta lista no
es un teorema de condiciones necesarias y suficientes para toda gravedad.
Un campo tensorial, un fondo curvo prescrito o una fuerza atractiva aislada
no constituye cumplimiento del objetivo final.

## 2. Envolvente microscópica de esta primera fase

- Red abstracta fija `Z³`; celda finita con dimensión local finita, independiente
  del volumen. Bosones truncados o fermiones requieren definición explícita de
  sus álgebras; un rotor infinito no pasa automáticamente esta envolvente.
- Evolución reversible por automorfismo exactamente unitario y de alcance
  estricto finito por tick. Circuitos de profundidad finita son una ruta
  admisible, no una clasificación de todos los QCA.
- Interacciones y variables geométricas colectivas se permiten en esta línea.
  La red abstracta fija no exige que la métrica efectiva sea fija.
- Regla periódica en el espacio con celda y periodo fijos, sin controles externos
  dependientes del estado ni feedback clásico que sustituya la evolución unitaria.
- Estado/sector, simetrías, materia, modos y observables se especifican junto
  a la regla. Gauge puede ser efectivo en el IR; no se exige difeomorfismo
  microscópico exacto como condición previa.

Esta envolvente está fijada. Dimensión de celda, representación, puertas,
estado, parámetros y restricciones siguen **NO_RULE_SPECIFIED**. Se congelarán
en IG1 antes del primer cálculo; no se presenta este charter como contrato
microscópico ya completo. Grafos dinámicos, dimensión local creciente, ancillas
añadidas tras ver resultados o nuevas clases requieren revisión explícita.

## 3. Requisitos que se intentará derivar o verificar

| ID | Requisito de la ruta elegida | Evidencia exigida; fallo temprano |
|---|---|---|
| R0 | QCA exacto | Regla e inversa con alcance uniforme; exponentiar un Hamiltoniano local global no basta |
| R1 | Sector IR definido | Estado de referencia y selección de rama/sector reproducibles; no llamar energía a una quasienergía sin justificarlo |
| R2 | Geometría operacional dinámica | Observables internos reconstruyen el símbolo principal de materia, evolucionan en vacío y reciben respuesta de materia; un embedding externo no basta |
| R3 | Dos modos tensoriales físicos | Restricciones y redundancia derivadas o sector efectivo controlado; eliminar componentes por proyección manual no basta |
| R4 | Propagación relativista | `ω_g²=c_g²|k|²+o(|k|²)`, estabilidad y residuos físicos positivos en el sector retenido; z=2/3 no cumple el objetivo lineal |
| R5 | Universalidad | Dos sectores materiales especificados ven la misma métrica operacional y `c_g=c_m` por un mecanismo; ajustar velocidades individualmente no cumple robustez |
| R6 | Fuente y reciprocidad | Acoplamiento al stress efectivo total, identidad de conservación pertinente y respuesta recíproca; ocupación o carga interna aislada no basta |
| R7 | Cierre no lineal | Autointeracción compatible, constraints/Ward y acción efectiva de Einstein con correcciones acotadas; spin-2 libre no basta |
| R8 | Control y robustez | Familia de perturbaciones admisibles fijada antes del test, ventana IR, errores y límites declarados; un punto ajustado no acredita una fase |

No se exige igualdad entre `c_IR` y el borde del soporte microscópico.
`C_micro`, velocidad causal, velocidad de grupo y velocidades IR conservan
sus definiciones separadas. R5 no requiere que todo el espectro sea relativista.
R2–R8 no se prueban al escribir la acción efectiva deseada.

## 4. Secuencia y estados de salida

**IG0 — requisitos y obstrucciones.** Contrastar fuentes primarias, separar
arquitecturas y localizar el primer requisito sin mecanismo. Salidas:
`ARCHITECTURE_UNDERSPECIFIED`, `SCOPED_OBSTRUCTION`,
`ARCHITECTURE_READY_FOR_SPECIFICATION`. Ninguna significa gravedad obtenida.

**IG1 — especificación previa.** Un único candidato completo: dimensión local,
álgebra, representación de simetrías, tick e inversa, soporte, estado/sector,
parámetros y variables observables; procedimiento IR, ramas y todos los modos.
Registrar perturbaciones admisibles, orden de expansión, límites y umbrales.
Si falta un elemento, salida `NO_RULE_SPECIFIED`; no se calcula su espectro.

**IG2 — prueba mínima.** R0/R1 primero; luego R3/R4 antes del acoplamiento.
Solo después, materia y R2/R5. Un éxito sin materia se llama sector tensorial,
no gravedad acoplada. R5 inicial requiere al menos dos sectores de materia
inequivalentes explícitos; no generalizarlo a toda materia.

**IG3 — fuente, cierre y control.** R6–R8 requieren contratos cuantitativos
propios. El resultado de IG2 no autoriza un claim de Einstein ni una escala SI.

Los cálculos y figuras futuros usan scripts permanentes con procedencia.
Los requisitos exactos se comprueban con álgebra exacta; los aproximados
necesitan umbral congelado y control de error antes de ejecutar.

## 5. Límites y reglas de parada

- Registrar el primer fallo y su clase. Un fallo de ansatz no es un no-go general.
- No proyectar a TT a mano y contar luego dos modos como emergencia.
- No inferir protección de Lorentz o velocidades comunes de isotropía discreta sola.
- No inferir un sector IR estable de un paso Trotter ni de su error a tiempo fijo.
- No insertar Einstein–Hilbert en las puertas y presentar su recuperación como
  derivación independiente: explicitar lo impuesto, lo derivado y lo abierto.
- No aplicar el bootstrap de spin-2 antes de verificar sus hipótesis efectivas.
- No determinar escalas absolutas por conveniencia ni cambiar el objetivo a
  Lifshitz si el candidato falla z=1. Una variante necesita contrato distinto.
- Antes de una promoción, contrastar antecedentes y obtener la revisión
  pertinente; el charter y una auditoría propia no son revisión independiente.

Al cierre de IG0 se registra una decisión y una siguiente pregunta concreta.
No hay barrido de modelos ni ajuste tras observar resultados bajo el mismo contrato.

## 6. Fuentes y primer expediente

Las lecturas, páginas comprobadas, objeciones y decisión inicial están en
[el informe IG0](../reports/2026-10-08--inverse-gravity-ig0.md).
ESTABLISHED queda reservado a afirmaciones demostradas o a hechos de fuentes
comprobadas con su alcance. La viabilidad de esta línea es OPEN; NOVELTY OPEN.
