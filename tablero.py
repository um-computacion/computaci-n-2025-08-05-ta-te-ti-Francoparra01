class Tablero:
    def __init__(self):
        # Matriz 3x3 vacía
        self.casillas = [[' ' for _ in range(3)] for _ in range(3)]

    def consultar_pos(self, fil, col):
        """Devuelve True si la posición está libre."""
        return self.casillas[fil][col] == ' '

    def colocar(self, fil, col, simbolo):
        """Coloca el símbolo si la casilla está libre. Retorna True si lo logra."""
        if self.consultar_pos(fil, col):
            self.casillas[fil][col] = simbolo
            return True
        return False

    def hay_ganador(self):
        """Devuelve 'X', 'O' o None según si hay ganador."""
        # Filas
        for fila in self.casillas:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        # Columnas
        for col in range(3):
            if (self.casillas[0][col] == self.casillas[1][col] ==
                self.casillas[2][col] != ' '):
                return self.casillas[0][col]
        # Diagonales
        if (self.casillas[0][0] == self.casillas[1][1] ==
            self.casillas[2][2] != ' '):
            return self.casillas[0][0]
        if (self.casillas[0][2] == self.casillas[1][1] ==
            self.casillas[2][0] != ' '):
            return self.casillas[0][2]
        return None

    def esta_lleno(self):
        """True si no hay espacios libres."""
        for fila in self.casillas:
            if ' ' in fila:
                return False
        return True

    def __str__(self):
        """Devuelve el tablero como string."""
        filas_str = []
        for fila in self.casillas:
            filas_str.append(" | ".join(fila))
        return "\n---------\n".join(filas_str)
