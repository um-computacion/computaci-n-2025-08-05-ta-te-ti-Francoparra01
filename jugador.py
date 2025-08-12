class Jugador:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo

    def elegir_jugada(self):
        while True:
            try:
                fila = int(input(f"{self.nombre} ({self.simbolo}), ingresa fila (0-2): "))
                columna = int(input(f"{self.nombre} ({self.simbolo}), ingresa columna (0-2): "))
                if 0 <= fila <= 2 and 0 <= columna <= 2:
                    return fila, columna
                else:
                    print("Las posiciones deben estar entre 0 y 2.")
            except ValueError:
                print("Por favor, ingresa números válidos.")

