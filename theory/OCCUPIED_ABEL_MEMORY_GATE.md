# Suma temporal regularizada con cota de cola

2026-11-06. Usuario «adelante». Conocido: F_a,r y K_a,r-1 están
evaluados para r<=8; falta controlar la cola. Pregunta: ¿qué suma de
memoria y derivadas puede calcularse con error acotado a resolución
temporal finita? Mismos walks, estado e interacción.

Fijar R=24, radios Abel rho=0.5,0.65,0.8 y frecuencias nodales
omega=±pi/4. Evaluar sum_(r>=1) rho^r exp(i omega r) K_a,r-1(0)
y sus derivadas físicas, usando cota analítica de coeficientes.
No llamar a esta suma una velocidad o un polo sin resolver la ecuación
de Dyson y justificar el límite rho->1. Unidades del repo sin cambios.
Control: reproducir r<=8; comprobar primer retardo por coeficientes.
Corte: si las cotas divergen al retirar el regulador, registrar la
obligación pendiente, sin extrapolación del dato finito a tiempo infinito.
