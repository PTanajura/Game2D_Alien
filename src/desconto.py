from abc import ABC, abstractmethod

class Desconto(ABC):

    """
    def calcular(self, tipo, valor):
        if tipo == "normal":
           return valor * 0.1
        elif tipo == "vip":
           return valor * 0.2
        elif tipo == "premium":
           return valor * 0.3
    """

    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1

class DescontoVip(Desconto):
    def calcular(self, valor):
        return valor * 0.2

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3

def main():
    valor = 100

    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVip()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: R$ {desconto_normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R$ {desconto_vip.calcular(valor):.2f}")
    print(f"Desconto Premium: R$ {desconto_premium.calcular(valor):.2f}")

