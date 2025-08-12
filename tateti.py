from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = 'X'
        self.tablero = Tablero()
        self.terminado = False

    def marcar_casilla(self, fil, col):
        """Intenta marcar la casilla y verifica el estado del juego."""
        if not (0 <= fil < 3 and 0 <= col < 3):
            return "Posición fuera de rango (0-2)."

        if not self.tablero.consultar_pos(fil, col):
            return "Casilla ocupada, intenta de nuevo."

        self.tablero.colocar(fil, col, self.turno)

        ganador = self.tablero.hay_ganador()
        if ganador:
            self.terminado = True
            return f"Ganó {ganador}!"
        elif self.tablero.esta_lleno():
            self.terminado = True
            return "Empate."

        self.cambiar_turno()
        return None  # No hubo ganador ni empate

    def cambiar_turno(self):
        """Alterna entre X y O."""
        self.turno = 'O' if self.turno == 'X' else 'X'
