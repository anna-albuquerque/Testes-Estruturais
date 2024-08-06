class CalculadoraAvancada:
    def calcula(self, a, b, operacao):
        if operacao == "soma":
            return a + b
        elif operacao == "subtrai":
            return a - b
        else:
            raise ValueError("Operação desconhecida")