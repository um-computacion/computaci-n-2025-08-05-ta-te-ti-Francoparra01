import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("TestPlayer", "X")

    def test_atributos(self):
        self.assertEqual(self.jugador.nombre, "TestPlayer")
        self.assertEqual(self.jugador.simbolo, "X")

    def test_elegir_jugada_valida(self):
        self.assertTrue(callable(self.jugador.elegir_jugada))

if __name__ == '__main__':
    unittest.main()
