# Thirring: tiempos crecientes y salida libre exacta

2026-11-08. Autor Codex/OpenAI. Usuario «adelante» a la propuesta de estudiar
acumulación de interacción con T(M) y código de salida libre exacto.

Sabido: e030faf demuestra para el código peine inicial y marco alternante
una cota 2T delta_M, delta_M=nu sqrt(2/M), y la cota de interacción
d_chi[T/sqrt(M)+delta_M T(T-1)]. La trayectoria extrema solo obstruye
el marco de soporte fijo. La identidad de Gamma y la regla se contrastan con
1711.03920v1.pdf pp.1–2 y 1804.08508v1.pdf pp.3,5–6.
Biblioteca/ no existe; sources/README.md consultado.

Pregunta: ¿existe una escala de tiempos crecientes que permita, sobre todas
las entradas, una unitaria entrelazante finita con fuga y error tendiendo a cero,
si el código de salida es exactamente F^T B y no una envolvente congelada?

Contrato: misma regla U=FJ, mu=3/5,nu=4/5,chi=pi/2 constantes; mismo código
inicial B=B_+ wedge B_- de dos fermiones y Q=0 del preflight cbfae56.
No controles independientes de F/J, ninguna inversión libre física,
postselección, variación de acoplamiento, perfil o masa. Preparación/lectura
ideal en los modos definidos, datos cuánticos arbitrarios. Salida B_T=F^T B;
su definición es un marco de lectura, no una operación adicional.

Primero: establecer exactamente compresión K=B_T† U^T B, defecto de unitariedad,
fuga máxima, error respecto de su polar unitaria y restricciones algebraicas.
Derivar el régimen de tiempos excluido por las cotas existentes, sin extender
una cota que deja de ser pequeña a un teorema de imposibilidad.

Contraste numérico congelado: M=1,2,4,8,16; T=M y T=M² (una misma evolución
por M), más T=1 para validación. Dos representaciones: sector exacto de
Gamma opuestos como amplitud sobre dos posiciones, y espacio antisimétrico
completo para M=1,2 y T<=4. Margen de luz L>=2M+2T_max+8, sin aproximación
de frontera periódica. No optimización de tiempos ni selección por éxito.

Diagnósticos de puerta: singular mínimo de K; fuga 1-sigma_min²; polar Q;
error completo ||U^T B-B_T Q||; distancia de Q a la identidad módulo fase;
concurrencia de Q sobre un conjunto fijo de productos (0,1,+,+i) tensor
(0,1,+,+i), que da testigos, no una optimización ni una prueba de límite.
Se conservarán matrices complejas y errores, también resultados negativos.

Corte: una prueba de que todo efecto finito requiere fuga persistente cierra
esta familia. Una puerta solo se declarará si hay estimaciones uniformes de
fuga/error, unitaria límite definida y entrelazamiento finito. Si los datos
no proporcionan ese control, terminar OPEN en los tiempos no excluidos,
sin convertir muestras en un no-go ni barrer más M, tiempos o parámetros.
No se abre composición de puertas mientras no se alcance ese criterio.

Contrato y código permanentes versionados antes de ejecutar. Resultado de
autor PRELIMINARY; no revisión externa, promoción o push automáticos.
