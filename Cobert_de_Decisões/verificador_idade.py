class VerificadorIdade:
    def verifica_idade(self, idade):
        if idade >= 18:
            return "Adulto"
        else:
            return "Menor de idade"