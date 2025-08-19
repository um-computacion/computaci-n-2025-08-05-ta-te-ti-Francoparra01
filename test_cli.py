# test_cli.py
import unittest
from unittest.mock import patch
from io import StringIO

import cli  # tu cli.py con main()


class TestCLI(unittest.TestCase):
    def test_partida_con_victoria_de_x(self):
        # X gana por la fila 0
        entradas = [
            "0","0",  # X
            "1","0",  # O
            "0","1",  # X
            "1","1",  # O
            "0","2",  # X
        ]
        with patch('builtins.input', side_effect=entradas), \
             patch('sys.stdout', new_callable=StringIO) as out:
            cli.main()
        salida = out.getvalue()
        self.assertIn("que comience el juego", salida)
        self.assertIn("Ganó X!", salida)
        self.assertIn("X | X | X", salida)

    def test_partida_empate(self):
        # Tablero lleno sin ganador
        # Final esperado:
        # X O X
        # X O O
        # O X X
        entradas = [
            "0","0",  # X
            "1","1",  # O
            "0","2",  # X
            "0","1",  # O
            "2","1",  # X
            "1","2",  # O
            "1","0",  # X
            "2","0",  # O
            "2","2",  # X
        ]
        with patch('builtins.input', side_effect=entradas), \
             patch('sys.stdout', new_callable=StringIO) as out:
            cli.main()
        salida = out.getvalue()
        self.assertIn("Empate.", salida)
        self.assertIn("X | O | X", salida)
        self.assertIn("X | O | O", salida)


if __name__ == "__main__":
    unittest.main(verbosity=2)
