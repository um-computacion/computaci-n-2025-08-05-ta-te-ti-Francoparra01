# test_tateti.py
import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):
    def test_estado_inicial(self):
        # Turno X, juego no terminado, tablero vacío
        juego = Tateti()
        self.assertEqual(juego.turno, 'X')
        self.assertFalse(juego.terminado)
        for f in range(3):
            for c in range(3):
                self.assertTrue(juego.tablero.consultar_pos(f, c))

    def test_jugada_valida_cambia_turno(self):
        # Marca y alterna turno
        juego = Tateti()
        msg = juego.marcar_casilla(0, 0)
        self.assertIsNone(msg)
        self.assertEqual(juego.tablero.casillas[0][0], 'X')
        self.assertEqual(juego.turno, 'O')
        self.assertFalse(juego.terminado)

    def test_fuera_de_rango_no_cambia_turno(self):
        # Rechaza fuera de rango y no alterna
        juego = Tateti()
        msg = juego.marcar_casilla(3, 0)
        self.assertEqual(msg, "Posición fuera de rango (0-2).")
        self.assertEqual(juego.turno, 'X')

    def test_casilla_ocupada_no_cambia_turno(self):
        # Rechaza casilla ocupada y no alterna
        juego = Tateti()
        self.assertIsNone(juego.marcar_casilla(0, 0))  # X
        self.assertEqual(juego.turno, 'O')
        msg = juego.marcar_casilla(0, 0)               # O intenta misma
        self.assertEqual(msg, "Casilla ocupada, intenta de nuevo.")
        self.assertEqual(juego.turno, 'O')

    def test_gana_por_fila(self):
        # X gana en la fila 0
        juego = Tateti()
        self.assertIsNone(juego.marcar_casilla(0, 0))  # X
        self.assertIsNone(juego.marcar_casilla(1, 0))  # O
        self.assertIsNone(juego.marcar_casilla(0, 1))  # X
        self.assertIsNone(juego.marcar_casilla(1, 1))  # O
        msg = juego.marcar_casilla(0, 2)               # X
        self.assertEqual(msg, "Ganó X!")
        self.assertTrue(juego.terminado)

    def test_gana_por_columna(self):
        # O gana en la columna 1
        juego = Tateti()
        self.assertIsNone(juego.marcar_casilla(0, 0))  # X
        self.assertIsNone(juego.marcar_casilla(0, 1))  # O
        self.assertIsNone(juego.marcar_casilla(2, 0))  # X
        self.assertIsNone(juego.marcar_casilla(1, 1))  # O
        self.assertIsNone(juego.marcar_casilla(2, 2))  # X
        msg = juego.marcar_casilla(2, 1)               # O
        self.assertEqual(msg, "Ganó O!")
        self.assertTrue(juego.terminado)

    def test_gana_diagonal_principal(self):
        # X gana en diagonal principal
        juego = Tateti()
        self.assertIsNone(juego.marcar_casilla(0, 0))  # X
        self.assertIsNone(juego.marcar_casilla(0, 1))  # O
        self.assertIsNone(juego.marcar_casilla(1, 1))  # X
        self.assertIsNone(juego.marcar_casilla(0, 2))  # O
        msg = juego.marcar_casilla(2, 2)               # X
        self.assertEqual(msg, "Ganó X!")
        self.assertTrue(juego.terminado)

    def test_empate(self):
        # Tablero lleno sin ganador
        # Final esperado:
        # X O X
        # X O O
        # O X X
        juego = Tateti()
        jugadas = [
            (0,0),  # X
            (1,1),  # O
            (0,2),  # X
            (0,1),  # O
            (2,1),  # X
            (1,2),  # O
            (1,0),  # X
            (2,0),  # O
            (2,2),  # X
        ]
        msg = None
        for i, (f, c) in enumerate(jugadas):
            msg = juego.marcar_casilla(f, c)
            if i < len(jugadas) - 1:
                self.assertIsNone(msg)
        self.assertEqual(msg, "Empate.")
        self.assertTrue(juego.terminado)

    def test_sin_mensaje_en_jugada_normal(self):
        # Una jugada intermedia no devuelve mensaje
        juego = Tateti()
        self.assertIsNone(juego.marcar_casilla(1, 1))
        self.assertEqual(juego.turno, 'O')

    def test_error_no_alterna_turno(self):
        # Error (rango/ocupada) no cambia el turno
        juego = Tateti()
        turno = juego.turno
        self.assertEqual(juego.marcar_casilla(-1, 0), "Posición fuera de rango (0-2).")
        self.assertEqual(juego.turno, turno)
        self.assertIsNone(juego.marcar_casilla(0, 0))  # X
        turno = juego.turno                            # O
        self.assertEqual(juego.marcar_casilla(0, 0), "Casilla ocupada, intenta de nuevo.")
        self.assertEqual(juego.turno, turno)


if __name__ == "__main__":
    unittest.main(verbosity=2)

