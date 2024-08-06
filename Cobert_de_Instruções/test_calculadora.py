import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 3), 5)

    def test_subtrai(self):
        self.assertEqual(self.calc.subtrai(5, 3), 2)

if __name__ == '__main__':
    unittest.main()