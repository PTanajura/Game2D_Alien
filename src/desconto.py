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

def main():
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVip()

    print("Desconto Normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Cupom VIP:", aplicar_cupom(vip, "DESC10"))


