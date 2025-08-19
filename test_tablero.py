import unittest
from tablero import Tablero

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_tablero_vacio(self):
        for fil in range(3):
            for col in range(3):
                self.assertTrue(self.tablero.consultar_pos(fil, col))
        self.assertFalse(self.tablero.esta_lleno())
        self.assertIsNone(self.tablero.hay_ganador())

    def test_colocar_ficha_y_consultar(self):
        self.assertTrue(self.tablero.colocar(0, 0, 'X'))
        self.assertFalse(self.tablero.consultar_pos(0, 0))
        self.assertFalse(self.tablero.colocar(0, 0, 'O'))  
        self.assertTrue(self.tablero.colocar(1, 1, 'O'))

    def test_ganador_fila(self):
        self.tablero.colocar(0, 0, 'X')
        self.tablero.colocar(0, 1, 'X')
        self.tablero.colocar(0, 2, 'X')
        self.assertEqual(self.tablero.hay_ganador(), 'X')

    def test_ganador_columna(self):
        self.tablero.colocar(0, 1, 'O')
        self.tablero.colocar(1, 1, 'O')
        self.tablero.colocar(2, 1, 'O')
        self.assertEqual(self.tablero.hay_ganador(), 'O')  # agregar test en diagonal

    def test_ganador_diagonal_principal(self):
        self.tablero.colocar(0, 0, 'X')
        self.tablero.colocar(1, 1, 'X')
        self.tablero.colocar(2, 2, 'X')
        self.assertEqual(self.tablero.hay_ganador(), 'X')

    def test_ganador_diagonal_secundaria(self):
        self.tablero.colocar(0, 2, 'O')
        self.tablero.colocar(1, 1, 'O')
        self.tablero.colocar(2, 0, 'O')
        self.assertEqual(self.tablero.hay_ganador(), 'O')

    def test_sin_ganador_estado_intermedio(self):
        self.tablero.colocar(0, 0, 'X')
        self.tablero.colocar(0, 1, 'O')
        self.tablero.colocar(1, 1, 'X')
        self.assertIsNone(self.tablero.hay_ganador())

    def test_empate_y_tablero_lleno(self):
        # que pasaria si llenan el tablero pero no hay 3 en lienea:
        # X O X
        # X O O
        # O X X
        jugadas = [
            (0,0,'X'), (0,1,'O'), (0,2,'X'),
            (1,0,'X'), (1,1,'O'), (1,2,'O'),
            (2,0,'O'), (2,1,'X'), (2,2,'X'),
        ]
        for f, c, s in jugadas:
            self.assertTrue(self.tablero.colocar(f, c, s))
        self.assertTrue(self.tablero.esta_lleno())
        self.assertIsNone(self.tablero.hay_ganador())

if __name__ == '__main__':
    unittest.main(verbosity=2)

