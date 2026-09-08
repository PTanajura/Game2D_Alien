class IDesconto:

    """
    def calcular(self, tipo, valor):
        if tipo == "normal":
           return valor * 0.1
        elif tipo == "vip":
           return valor * 0.2
        elif tipo == "premium":
           return valor * 0.3
    """
    def calcular(self, valor):
        raise NotImplementedError
    
class ICupom:
    def aplicar_cupom(self, codigo):
        raise NotImplementedError

class IVIP:
    def validar_usuario_vip(self, usuario):
        raise NotImplementedError

class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1

class DescontoVip(IDesconto, ICupom, IVIP):
    def calcular(self, valor):
        return valor * 0.2

    def aplicar_cupom(self, codigo):
        return True

    def validar_usuario_vip(self, usuario):
        return usuario == "vip"

class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor * 0.3

def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

class Pedido:
    def __init__(self, desconto: IDesconto):
        self.desconto = desconto

    def total(self, valor):
        return valor - self.desconto.calcular(valor)

def main():
    valor = 100

    normal = Pedido(DescontoNormal())
    vip = Pedido(DescontoVip())

    print("Desconto Normal:", normal.total(valor))
    print("Desconto VIP:", vip.total(valor))
    print("Cupom VIP:", aplicar_cupom(vip.desconto, "DESC10"))

if __name__ == "__main__":
    main()