import unittest
from tateti import Tateti

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti()

    def test_turno_inicial(self):
        self.assertEqual(self.juego.turno, 'X')

    def test_marcar_casilla_valida(self):
        resultado = self.juego.marcar_casilla(0, 0)
        self.assertIsNone(resultado)
        self.assertEqual(self.juego.turno, 'O')

    def test_marcar_casilla_ocupada(self):
        self.juego.marcar_casilla(0, 0)
        resultado = self.juego.marcar_casilla(0, 0)
        self.assertEqual(resultado, "Casilla ocupada, intenta de nuevo.")
        self.assertEqual(self.juego.turno, 'O')

    def test_marcar_casilla_fuera_de_rango(self):
        resultado = self.juego.marcar_casilla(3, 3)
        self.assertEqual(resultado, "Posición fuera de rango (0-2).")
        self.assertEqual(self.juego.turno, 'X')

    def test_ganador(self):
        self.juego.marcar_casilla(0, 0)
        self.juego.marcar_casilla(1, 0)
        self.juego.marcar_casilla(0, 1)
        self.juego.marcar_casilla(1, 1)
        resultado = self.juego.marcar_casilla(0, 2)
        self.assertEqual(resultado, "Ganó X!")
        self.assertTrue(self.juego.terminado)

    def test_empate(self):
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        resultado = None
        for f, c in jugadas:
            resultado = self.juego.marcar_casilla(f, c)
        self.assertEqual(resultado, "Empate.")
        self.assertTrue(self.juego.terminado)

if __name__ == '__main__':
    unittest.main()

