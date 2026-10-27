class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError


class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1


class DescontoVIP(IDesconto):
    def calcular(self, valor):
        return valor * 0.2


class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)


if __name__ == "__main__":
    valor = 100

    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())

    print("Normal:", pedido_normal.total(valor))
    print("VIP:", pedido_vip.total(valor))
