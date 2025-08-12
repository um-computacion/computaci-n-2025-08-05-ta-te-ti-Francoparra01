from jugador import Jugador
from tateti import Tateti

def main():
    print("que comience el juego")

    jugador1 = Jugador("Jugador 1", "X")
    jugador2 = Jugador("Jugador 2", "O")

    juego = Tateti()

    while not juego.terminado:
        print(juego.tablero)

        jugador_actual = jugador1 if juego.turno == "X" else jugador2

        fila, columna = jugador_actual.elegir_jugada()

        mensaje = juego.marcar_casilla(fila, columna)

        if mensaje:
            print(juego.tablero)
            print(mensaje)

if __name__ == "__main__":
    main()
