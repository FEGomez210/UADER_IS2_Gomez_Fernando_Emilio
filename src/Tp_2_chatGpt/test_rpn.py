import unittest
from rpn import RPN, RPNError
import math


class TestRPN(unittest.TestCase):

    def setUp(self):
        self.r = RPN()

    # ---------------------------
    # Operaciones básicas
    # ---------------------------
    def test_operaciones_basicas(self):
        self.assertEqual(self.r.run("3 4 +"), 7)
        self.assertEqual(self.r.run("10 5 -"), 5)
        self.assertEqual(self.r.run("2 3 *"), 6)
        self.assertEqual(self.r.run("8 2 /"), 4)

    def test_expresiones_complejas(self):
        self.assertEqual(self.r.run("5 1 2 + 4 * + 3 -"), 14)
        self.assertEqual(self.r.run("2 3 4 * +"), 14)

    # ---------------------------
    # Floats y negativos
    # ---------------------------
    def test_floats_y_negativos(self):
        self.assertAlmostEqual(self.r.run("2.5 2 *"), 5.0)
        self.assertAlmostEqual(self.r.run("-4 2 *"), -8.0)

    # ---------------------------
    # Errores
    # ---------------------------
    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            self.r.run("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            self.r.run("2 a +")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            self.r.run("+")
        with self.assertRaises(RPNError):
            self.r.run("2 +")

    def test_estado_final_invalido(self):
        with self.assertRaises(RPNError):
            self.r.run("2 3")

    # ---------------------------
    # Comandos de pila
    # ---------------------------
    def test_dup(self):
        self.assertEqual(self.r.run("2 dup +"), 4)

    def test_swap(self):
        self.assertEqual(self.r.run("2 3 swap -"), 1)

    def test_drop(self):
        with self.assertRaises(RPNError):
            self.r.run("drop")

    def test_clear(self):
        with self.assertRaises(RPNError):
            self.r.run("2 3 clear")

    # ---------------------------
    # Constantes
    # ---------------------------
    def test_constantes(self):
        self.assertAlmostEqual(self.r.run("p"), math.pi)
        self.assertAlmostEqual(self.r.run("e"), math.e)
        self.assertAlmostEqual(self.r.run("j"), (1 + 5 ** 0.5) / 2)

    # ---------------------------
    # Funciones matemáticas
    # ---------------------------
    def test_funciones(self):
        self.assertEqual(self.r.run("9 sqrt"), 3)
        self.assertEqual(self.r.run("100 log"), 2)
        self.assertAlmostEqual(self.r.run("1 ln ex"), 1)
        self.assertEqual(self.r.run("2 3 yx"), 8)
        self.assertEqual(self.r.run("2 1/x"), 0.5)

    # ---------------------------
    # Trigonometría
    # ---------------------------
    def test_trigonometria(self):
        self.assertAlmostEqual(self.r.run("90 sin"), 1, places=5)
        self.assertAlmostEqual(self.r.run("0 cos"), 1, places=5)
        self.assertAlmostEqual(self.r.run("45 tg"), 1, places=5)

    def test_trigonometria_inversa(self):
        self.assertAlmostEqual(self.r.run("1 asin"), 90, places=5)
        self.assertAlmostEqual(self.r.run("1 acos"), 0, places=5)
        self.assertAlmostEqual(self.r.run("1 atg"), 45, places=5)

    # ---------------------------
    # CHS
    # ---------------------------
    def test_chs(self):
        self.assertEqual(self.r.run("5 chs"), -5)

    # ---------------------------
    # Memoria
    # ---------------------------
    def test_memoria(self):
        self.assertEqual(self.r.run("10 0 sto 0 rcl"), 10)

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            self.r.run("10 10 sto")

    # ---------------------------
    # Tests EXTRA (para coverage)
    # ---------------------------
    def test_dup_error(self):
        with self.assertRaises(RPNError):
            self.r.run("dup")

    def test_swap_error(self):
        with self.assertRaises(RPNError):
            self.r.run("1 swap")

    def test_1_div_x_cero(self):
        with self.assertRaises(RPNError):
            self.r.run("0 1/x")

    def test_memoria_rcl_invalida(self):
        with self.assertRaises(RPNError):
            self.r.run("10 rcl")

    def test_expresion_vacia(self):
        with self.assertRaises(RPNError):
            self.r.run("")

    # ---------------------------
    # Validación de mensajes
    # ---------------------------
    def test_mensajes_error(self):
        try:
            self.r.run("3 0 /")
        except RPNError as e:
            self.assertIn("division por cero", str(e))

        try:
            self.r.run("a b +")
        except RPNError as e:
            self.assertIn("token invalido", str(e))


if __name__ == "__main__":
    unittest.main()