import pytest
from src.desconto import DescontoNormal, DescontoVip, DescontoPremium

#Parametrize
@pytest.mark.parametrize("valor, esperado", [
    (100, 30),
    (200, 60),
    (300, 90)
])

#Assert
def test_desconto_premium(valor, esperado):
    desconto = DescontoPremium()
    resultado = desconto.calcular(valor)
    assert resultado == esperado

def test_desconto_normal():
    desconto = DescontoNormal()
    resultado = desconto.calcular(100)
    assert resultado == 10.0

#Fixture
@pytest.fixture
def desconto_vip():
    return DescontoVip()

def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20.0

def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40.0