import unittest
from tablero import Tablero

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_vacio(self):
        # El tablero al iniciar debe estar vacío
        for fila in range(3):
            for col in range(3):
                self.assertTrue(self.tablero.consultar_pos(fila, col))

    def test_colocar_ficha(self):
        # Se debe poder colocar ficha en posición que no tnga nada
        self.assertTrue(self.tablero.colocar(0, 0, 'X'))
        # no se debe poder colocar ficha en posición ocupada
        self.assertFalse(self.tablero.colocar(0, 0, 'O'))

    def test_ganador_fila(self):
        # Como se comporta eljuego si alguien llega a ganar
        self.tablero.colocar(0, 0, 'X')
        self.tablero.colocar(0, 1, 'X')
        self.tablero.colocar(0, 2, 'X')
        self.assertEqual(self.tablero.hay_ganador(), 'X')

if __name__ == '__main__':
    unittest.main()
