import unittest
from calculadora_avancada import CalculadoraAvancada

class TestCalculadoraAvancada(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraAvancada()

    def test_calcula_soma(self):
        self.assertEqual(self.calc.calcula(2, 3, "soma"), 5)

    def test_calcula_subtrai(self):
        self.assertEqual(self.calc.calcula(5, 3, "subtrai"), 2)

    def test_calcula_operacao_desconhecida(self):
        with self.assertRaises(ValueError):
            self.calc.calcula(2, 3, "multiplica")

if __name__ == '__main__':
    unittest.main()