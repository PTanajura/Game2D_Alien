from desconto import IDesconto

class StubSemDesconto(IDesconto):
    def calcular(self, valor):
        return 0
