# test_jugador.py
import unittest
from unittest.mock import patch
from io import StringIO

from jugador import Jugador


class TestJugadorBasico(unittest.TestCase):

    def test_ingreso_valido(self):
        # jugada normal
        j = Jugador("Agus", "X")
        with patch('builtins.input', side_effect=["1", "2"]):
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (1, 2))

    def test_valor_no_numerico_luego_valido(self):
        # jugador pone una a
        # despues fila=0 y col=1
        j = Jugador("Agus", "X")
        with patch('builtins.input', side_effect=["a", "0", "1"]), \
             patch('sys.stdout', new_callable=StringIO) as fake_out:
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (0, 1))
        # exepcion
        self.assertIn("Por favor, ingresa números válidos.", fake_out.getvalue())

    def test_fuera_de_rango_luego_valido(self):
        # Jugada errores segun reglas de negocio (fila ingresada mayor a las que hay)
        # Segundo intento: fila=1, col=2 (validos).
        j = Jugador("Agus", "O")
        with patch('builtins.input', side_effect=["3", "0", "1", "2"]), \
             patch('sys.stdout', new_callable=StringIO) as fake_out:
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (1, 2))
        # Verificao que salte la excepcion
        self.assertIn("Las posiciones deben estar entre 0 y 2.", fake_out.getvalue())

    def test_limite_inferior_aceptado(self):
        # Una jugada valida con limites inferiores.
        j = Jugador("Agus", "X")
        with patch('builtins.input', side_effect=["0", "0"]):
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (0, 0))

    def test_limite_superior_aceptado(self):
        # JUgada legal con limites superiores.
        j = Jugador("Agus", "O")
        with patch('builtins.input', side_effect=["2", "2"]):
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (2, 2))

    def test_multiples_invalidos_hasta_valido(self):
        # Secuencia de entradas:
        # "a" → string → mensaje de error.
        # "0","5" → no cumples reglas de negocio (col=5) → mensaje de error.
        # "1","1" → válidos.
        j = Jugador("Agus", "X")
        with patch('builtins.input', side_effect=["a", "0", "5", "1", "1"]), \
             patch('sys.stdout', new_callable=StringIO) as fake_out:
            f, c = j.elegir_jugada()
        self.assertEqual((f, c), (1, 1))
        out = fake_out.getvalue()
        self.assertIn("Por favor, ingresa números válidos.", out)
        self.assertIn("Las posiciones deben estar entre 0 y 2.", out)

    def test_tipo_de_retorno(self):
        # Asegura que el método siempre devuelva una tupla de enteros
        j = Jugador("Agus", "X")
        with patch('builtins.input', side_effect=["1", "0"]):
            res = j.elegir_jugada()
        self.assertIsInstance(res, tuple)
        self.assertIsInstance(res[0], int)
        self.assertIsInstance(res[1], int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
