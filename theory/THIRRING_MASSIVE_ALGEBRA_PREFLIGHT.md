# Thirring masivo: filtro algebraico de código compatible con Gamma

2026-11-08. Autor Codex/OpenAI. Usuario «adelante» a la propuesta de prueba
algebraica acotada antes de otra simulación de dispersión completa.

Sabido: la auditoría 078554c deriva {W,Gamma}=0, Gamma=sigma_z Pi, y U†QU=-Q
para Q=dGamma(Gamma). La obstrucción sin masa es del código de nodo previo;
no se traslada automáticamente al masivo. Fuentes primarias disponibles:
1711.03920v1.pdf pp.1–2 y 1804.08508v1.pdf p.3 (se releen antes del cálculo).

Pregunta: ¿un código quiral/paridad de carga alternante definida convierte la
mezcla de masa en una operación lógica, y proporciona una segunda operación
no conmutante con efecto finito y fuga controlable bajo una regla autónoma fija?

Código congelado: f_M uniforme en M sitios pares consecutivos, norma uno;
g_M=T f_M, T|x>=|x+1>. C_+ = span{R f_M,L g_M},
C_- = span{R g_M,L f_M}, con sigma_z R=+R, sigma_z L=-L.
Cada qubit lleva un fermión. Para dos qubits se ocupa un modo de C_+ y uno
de C_- en ese orden de creación; carga Q=0. Se contrastará también la
obstrucción de contacto para dos fermiones con el mismo signo de Gamma.

Regla U=FJ, J=producto_x exp(i chi n_R(x)n_L(x)), F=segunda cuantización
de W con R a derecha, L a izquierda, mezcla -i mu entre componentes,
nu²+mu²=1. Parámetros físicos congelados mu=3/5,nu=4/5,chi=pi/2 para
contrastes numéricos; derivaciones retienen 0<mu<1 y chi real.
F,J y un variador de chi NO son operaciones externas disponibles.
No espejos, medidas intermedias, postselección ni cambios temporales de masa.
Preparación y lectura finales ideales del código en base lógica Z; preparación
de datos cuánticos arbitrarios para exigir aproximación unitaria del canal.
No se deduce una clasificación de complejidad de muestreo.

El marco de comparación sigue la alternancia C_+<->C_- de cada etiqueta;
no se aplica físicamente una inversión F^{-t}. Se analiza el error de
envolvente a M creciente para uno y dos pasos, y el contacto instantáneo
en el código. No se confunde invariancia del sector Gamma con invariancia
del código de dimensión dos.

Abandono del candidato de puerta elemental de duración fija: si la acción
no conmutante de contacto desaparece cuando la fuga tiende a cero, o si una
restricción exacta impide entrelazar. Un conmutador de generadores no prueba
dos puertas autónomas. Si solo queda abierta la acumulación a tiempos que
crecen con M, terminar con OPEN, sin abrir una simulación de dispersión o
un barrido de masas. Si se obtienen dos operaciones finitas componibles
con error controlado, continuar a la colisión conforme a la autorización.

Verificación: álgebra exacta de W y de los proyectores de contacto; evolución
reticular antisimétrica de dos cuerpos para mu fijo y M=1,2,4,8,16;
contrastes con conteo de coincidencias; consistencia de Gamma y casos límite.
Todo código y salida se conserva; contrato y script se versionan antes de
ejecutar. Nivel de autor PRELIMINARY. No nuevos envíos externos ni promoción.

Entorno: biblioteca/ no existe en este checkout; sources/README.md consultado.
No se crea índice alternativo.
