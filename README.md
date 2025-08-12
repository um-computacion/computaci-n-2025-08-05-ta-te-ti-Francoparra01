ALUMNO: Franco Agustin Parra
CARRERA: Ingenieria Informatica
Trabajo: Tateti 

Proyecto Tateti - Arquitectura por Capas y Testing
Este proyecto de Tateti en Python está diseñado siguiendo una arquitectura en capas como la que vimos en clase, que separa claramente la interfaz, las reglas de negocio y el juego, para lograr un código modular, mantenible y fácil de probar.

Capas y responsabilidades
Interfaz (cli.py):
Es la capa encargada de mostrar información al usuario y recibir sus inputs. No contiene reglas del juego ni lógica, solo maneja la interaccion.

Reglas de negocio (modelo):
Aquí se definen las reglas del juego, como que siempre arrancan las X. Incluye:

tablero.py: Representa el tablero, valida posiciones, actualiza el estado y detecta ganador o empate. No conoce detalles del jugador ni la interfaz.

jugador.py: Representa a un jugador, guarda su nombre y símbolo, y elige movimientos válidos (puede ser humano o CPU). No sabe sobre turnos ni estado general.

Juego (tateti.py):
Esta capa maneja el juego: coordina los turnos, solicita jugadas a los jugadores, actualiza el tablero y determina el fin de la partida. Es el “cerebro” que integra las reglas con la interfaz.


Aplique tests a cada modulo por separados porque como vimos en clases eso tiene ciertas ventajas, como reconocer en donde esta el error, si hiciese un solo test al proyecto completo y falla, no sabria donde esta el error, tambien podemos modificar modulos individualmente sin afectar a otros.
