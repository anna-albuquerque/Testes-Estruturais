import unittest
from verificador_idade import VerificadorIdade

class TestVerificadorIdade(unittest.TestCase):
    def setUp(self):
        self.verificador = VerificadorIdade()

    def test_verifica_idade_adulto(self):
        self.assertEqual(self.verificador.verifica_idade(20), "Adulto")

    def test_verifica_idade_menor(self):
        self.assertEqual(self.verificador.verifica_idade(17), "Menor de idade")

if __name__ == '__main__':
    unittest.main()